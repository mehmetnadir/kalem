// Kalem darbesi geometrisi — düz canvas 2D sürümü (Paper.js yok).
// Kaynak: ornek/ucan-makine/sahneler/01-paperjs/sayfa.html (cizgi, cokgen). Tohumlu; Math.random ve Date yok.
// Kullanım: const c = kalemCizgi(noktalar, { w: 3.5 }); ... darbeCiz(ctx, c, ilerleme 0..1);

import { renkCoz, RT } from "./kunye.js";

// Kanca (yalnız kayıt): pencerede yoksa oluştur
if (typeof window !== "undefined" && !window.__kalemKutu) {
  window.__kalemKutu = {
    kare: [],
    ekle(tur, ad, x, y, w, h) {
      // Çizim anındaki dönüşüm (grup küçülmesi, kaydırma) kutuya uygulanır; ctx'i sahne kare() kancası verir
      const m = this.ctx && this.ctx.getTransform ? this.ctx.getTransform() : null;
      if (m && !m.isIdentity && w > 0 && h > 0) {
        const xs = [], ys = [];
        for (const [px, py] of [[x, y], [x + w, y], [x, y + h], [x + w, y + h]]) {
          xs.push(m.a * px + m.c * py + m.e);
          ys.push(m.b * px + m.d * py + m.f);
        }
        x = Math.min(...xs); y = Math.min(...ys); w = Math.max(...xs) - x; h = Math.max(...ys) - y;
      }
      if (w > 0 && h > 0) {
        this.kare.push({
          tur,
          ad: String(ad || ""),
          x: Math.round(x),
          y: Math.round(y),
          w: Math.round(w),
          h: Math.round(h),
        });
      }
    },
  };
}

// ---------- küçük yardımcılar ----------
// [a,b] aralığına sıkıştırır.
export const kis = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
// Doğrusal aradeğer.
export const lerp = (a, b, t) => a + (b - a) * t;
// Ease-out cubic (giriş hareketi).
export const yavasla = (x) => 1 - Math.pow(1 - kis(x), 3);
// Yumuşak adım (smoothstep).
export const yumus = (x) => { x = kis(x); return x * x * (3 - 2 * x); };
// Geri taşmalı ease-out (pop).
export const geriTasma = (x, s = 1.7) => { x = kis(x) - 1; return 1 + x * x * ((s + 1) * x + s); };
// Tohumlu 3 girdili karma, 0..1 döner.
export const hash = (a, b = 0, c = 0) => {
  let h = (Math.imul(a | 0, 374761393) + Math.imul(b | 0, 668265263) + Math.imul(c | 0, 1274126177)) | 0;
  h = Math.imul(h ^ (h >>> 13), 1274126177); h ^= h >>> 16; return (h >>> 0) / 4294967296;
};
// Tohumlu 1B değer gürültüsü, -0,5..0,5 döner.
export const gurul = (x, s) => {
  const i = Math.floor(x), f = x - i, u = f * f * (3 - 2 * f);
  return lerp(hash(i, s, 7), hash(i + 1, s, 7), u) - 0.5;
};

let tohumSayaci = 1;
// Darbe tohum sayacını başa alır (her sahne kur() başında çağırır; iki koşu aynı kareyi verir).
export function tohumSifirla(n = 1) { tohumSayaci = n; }

// ---------- çizgi örnekleme ----------
// Noktalardan Catmull-Rom eğrisi (ara px aralıkla yoğun polyline).
function yumusat(pts, ara = 10) {
  const n = pts.length, cik = [];
  for (let i = 0; i < n - 1; i++) {
    const p0 = pts[Math.max(0, i - 1)], p1 = pts[i], p2 = pts[i + 1], p3 = pts[Math.min(n - 1, i + 2)];
    const m = Math.max(1, Math.ceil(Math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / ara));
    for (let k = 0; k < m; k++) {
      const t = k / m, t2 = t * t, t3 = t2 * t;
      cik.push([0, 1].map((j) => 0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t +
        (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2 + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3)));
    }
  }
  cik.push(pts[n - 1].slice());
  return cik;
}

// Polyline'ı yay uzunluğuna göre eşit aralıkla örnekler; [noktalar, toplam uzunluk] döner.
function esitOrnekle(poly, ara) {
  const cum = [0];
  for (let i = 1; i < poly.length; i++) cum.push(cum[i - 1] + Math.hypot(poly[i][0] - poly[i - 1][0], poly[i][1] - poly[i - 1][1]));
  const L = cum[cum.length - 1], n = Math.max(3, Math.ceil(L / ara) + 1), cik = [];
  let j = 0;
  for (let i = 0; i < n; i++) {
    const s = L * i / (n - 1);
    while (j < poly.length - 2 && cum[j + 1] < s) j++;
    const d = cum[j + 1] - cum[j] || 1, u = kis((s - cum[j]) / d);
    cik.push([lerp(poly[j][0], poly[j + 1][0], u), lerp(poly[j][1], poly[j + 1][1], u)]);
  }
  return [cik, L];
}

// Kalem darbesi: titrek merkez çizgisi + uçlarda incelen kalınlık. o: {w, duz, amp, uc0, uc1, renk, alfa, tohum, ses}.
export function kalemCizgi(pts, o = {}) {
  const sd = o.tohum == null ? tohumSayaci++ : o.tohum;
  const yol = (!o.duz && pts.length > 2) ? yumusat(pts) : pts;
  const [ham, L0] = esitOrnekle(yol.length > 1 ? yol : [pts[0], [pts[0][0] + 0.01, pts[0][1]]], o.aralik || 2.4);
  const L = Math.max(1, L0), n = ham.length, amp = o.amp == null ? 1.1 : o.amp, w0 = o.w || 3.5;
  const nrm0 = ham.map((_, i) => {
    const a = ham[Math.max(0, i - 1)], b = ham[Math.min(n - 1, i + 1)];
    const dx = b[0] - a[0], dy = b[1] - a[1], l = Math.hypot(dx, dy) || 1; return [-dy / l, dx / l];
  });
  const p = ham.map((q, i) => {
    const s = L * i / (n - 1), sap = amp * (gurul(s / 55, sd) * 1.6 + gurul(s / 14, sd + 99) * 0.5);
    return [q[0] + nrm0[i][0] * sap, q[1] + nrm0[i][1] * sap];
  });
  const tb = Math.min(L * 0.3, o.uc0 == null ? 16 : o.uc0), te = Math.min(L * 0.4, o.uc1 == null ? 34 : o.uc1);
  const w = p.map((_, i) => {
    const s = L * i / (n - 1), tp = Math.pow(kis(s / tb), 0.6) * Math.pow(kis((L - s) / te), 0.7);
    return Math.max(0.3, w0 * (0.12 + 0.88 * tp) * (0.82 + 0.36 * (gurul(s / 70, sd + 5) + 0.5)));
  });
  return { p, nrm: nrm0, w, n, L, renk: o.renk || "@murekkep", alfa: o.alfa == null ? 0.9 : o.alfa,
    ses: o.ses, yol2d: null };
}

// İlerleme t (0..1) için kapalı çokgen noktaları (sol kenar ileri, sağ kenar geri).
function cokgenNoktalari(c, t) {
  const m = t * (c.n - 1), k = Math.floor(m), fr = m - k, sol = [], sag = [];
  const ekle = (q, nr, w) => {
    sol.push([q[0] + nr[0] * w / 2, q[1] + nr[1] * w / 2]); sag.push([q[0] - nr[0] * w / 2, q[1] - nr[1] * w / 2]);
  };
  for (let i = 0; i <= Math.min(k, c.n - 1); i++) ekle(c.p[i], c.nrm[i], c.w[i]);
  if (k < c.n - 1 && fr > 0) {
    ekle([lerp(c.p[k][0], c.p[k + 1][0], fr), lerp(c.p[k][1], c.p[k + 1][1], fr)], c.nrm[k], lerp(c.w[k], c.w[k + 1], fr));
  }
  return sol.concat(sag.reverse());
}

// Darbeyi t ilerlemesine kadar çizer (ctx.fill). carpan: ek şeffaflık çarpanı. Biten darbe Path2D önbelleğinden gelir.
export function darbeCiz(ctx, c, t, carpan = 1) {
  if (t <= 0 || carpan <= 0) return;
  ctx.save(); ctx.globalAlpha = c.alfa * carpan; ctx.fillStyle = renkCoz(c.renk);
  if (t >= 1) {
    if (!c.yol2d) {
      const seg = cokgenNoktalari(c, 1), y = new Path2D();
      y.moveTo(seg[0][0], seg[0][1]); for (let i = 1; i < seg.length; i++) y.lineTo(seg[i][0], seg[i][1]);
      y.closePath(); c.yol2d = y;
    }
    ctx.fill(c.yol2d);
  } else {
    const seg = cokgenNoktalari(c, t);
    if (seg.length >= 4) {
      ctx.beginPath(); ctx.moveTo(seg[0][0], seg[0][1]);
      for (let i = 1; i < seg.length; i++) ctx.lineTo(seg[i][0], seg[i][1]);
      ctx.closePath(); ctx.fill();
    }
  }
  ctx.restore();
}

// Darbenin t ilerlemesindeki uç (kalem ucu) noktası.
export function basUcu(c, t) {
  const m = kis(t) * (c.n - 1), k = Math.min(c.n - 2, Math.floor(m)), u = kis(m - k);
  return [lerp(c.p[k][0], c.p[k + 1][0], u), lerp(c.p[k][1], c.p[k + 1][1], u)];
}

// ---------- SVG yolları ----------
const SVG_NS = "http://www.w3.org/2000/svg";
const PAPER_YOL = globalThis.KALEM_PAPER_YOL                       // başka projede sayfa ezer
  || "/motorlar/paperjs/node_modules/paper/dist/paper-core.js";

// Yol örnekleme Paper.js eğri geometrisiyle (yalnız geometri; çizim motoru düz canvas kalır).
// Ölçüm 05.11: Blink getPointAtLength her çağrıda yolu baştan yürür; Open Peeps figüründe tek iş
// 1,7–2,5 s → editörde sonraki sahne yüklenirken (3 s önce) takılma. Paper Curve#getPointAt eğri
// başına sabit maliyet (~0,1 s). Sayfada paper yoksa burada yüklenir; modül üst düzey await: sahne
// betiği paper hazır olmadan başlamaz. Node testinde document yok, adım atlanır; yükleme düşerse
// uyarı yazılır, DOM örnekleyici kullanılır.
if (typeof document !== "undefined" && !globalThis.paper) {
  await new Promise((ok, hata) => {
    const s = document.createElement("script"); s.src = PAPER_YOL; s.onload = ok;
    s.onerror = () => hata(new Error("paper-core yüklenemedi: " + PAPER_YOL));
    document.head.appendChild(s);
  }).catch((e) => console.warn(e.message + " — DOM örnekleyici (yavaş) kullanılır"));
}

// Tek <path> öğesini kaynak koordinatta ~adimK yay aralığıyla örnekler; alt yol başına dizi.
function yolOrnekle(yol, adimK) {
  const P = globalThis.paper;
  if (P) {
    if (!P.project) P.setup(new P.Size(2, 2));
    const cp = new P.CompoundPath({ pathData: yol.getAttribute("d"), insert: false });
    const altYollar = cp.children && cp.children.length ? cp.children : [cp], dizi = [];
    for (const py of altYollar) {
      const pts = [];
      for (const c of py.curves || []) {
        const L = c.length; if (!(L > 1e-6)) continue;
        const n = Math.max(1, Math.ceil(L / adimK));
        for (let j = 0; j < n; j++) { const q = c.getPointAt(L * j / n); pts.push([q.x, q.y]); }
      }
      if (py.segments && py.segments.length) {
        const q = py.closed ? py.firstSegment.point : py.lastSegment.point; pts.push([q.x, q.y]);
      }
      if (pts.length >= 2) dizi.push(pts);
    }
    cp.remove();
    return dizi;
  }
  const len = yol.getTotalLength(), N = Math.min(6000, Math.max(2, Math.ceil(len / adimK) + 1));
  const pts = [];
  for (let i = 0; i < N; i++) {
    const q = yol.getPointAtLength(len * i / (N - 1)); pts.push([q.x, q.y]);
  }
  return [pts];
}

// SVG metnini çözer; yolları örnekler, viewBox'ı kutuya (x,y,w,h; oran korunur) oturtur; uzun→kısa nokta dizileri döner.
export function svgYollari(svgMetin, kutuHedef, { enCok = 60, esik = 0.02, adim = 5 } = {}) {
  const doc = new DOMParser().parseFromString(svgMetin, "image/svg+xml");
  const kok = document.importNode(doc.documentElement, true);
  const vb = (kok.getAttribute("viewBox") || "0 0 24 24").trim().split(/[\s,]+/).map(Number);
  const kap = document.createElement("div");
  kap.style.cssText = "position:absolute;left:-9999px;top:0;width:10px;height:10px;visibility:hidden";
  kok.setAttribute("width", String(vb[2])); kok.setAttribute("height", String(vb[3]));
  kap.appendChild(kok); document.body.appendChild(kap);
  const s = Math.min(kutuHedef.w / vb[2], kutuHedef.h / vb[3]);
  const ox = kutuHedef.x + (kutuHedef.w - vb[2] * s) / 2 - vb[0] * s;
  const oy = kutuHedef.y + (kutuHedef.h - vb[3] * s) / 2 - vb[1] * s;
  const dizgi = [];
  for (const yol of kok.querySelectorAll("path")) {
    if (yol.getAttribute("stroke") === "none" && yol.getAttribute("fill") === "none") continue;
    if (!yol.getAttribute("d")) continue;
    if (/^(#fff|#ffffff|white)$/i.test((yol.getAttribute("fill") || "").trim())) continue;  // beyaz örtü yolu çizilmez
    let zincir = [], e = yol;
    while (e && e !== kok.parentNode) { zincir.unshift(e); e = e.parentNode; if (e === kap) break; }
    let M = new DOMMatrix();
    for (const el of zincir) {
      const tr = el.transform && el.transform.baseVal && el.transform.baseVal.consolidate();
      if (tr) M = M.multiply(new DOMMatrix([tr.matrix.a, tr.matrix.b, tr.matrix.c, tr.matrix.d, tr.matrix.e, tr.matrix.f]));
    }
    const msc = Math.sqrt(Math.abs(M.a * M.d - M.b * M.c)) || 1, len = yol.getTotalLength();
    const adimK = Math.max(adim / (msc * s), len / 5999);   // çıktı px'te adim; ≤ 6000 nokta/yol
    for (const ham of yolOrnekle(yol, adimK)) {
      let parca = [], onceki = null;
      const bitir = () => { if (parca.length >= 2) dizgi.push(parca); parca = []; };
      for (const q of ham) {
        const X = M.a * q[0] + M.c * q[1] + M.e, Y = M.b * q[0] + M.d * q[1] + M.f;
        const pt = [X * s + ox, Y * s + oy];
        if (onceki && Math.hypot(pt[0] - onceki[0], pt[1] - onceki[1]) > adim * 2.2) bitir();
        parca.push(pt); onceki = pt;
      }
      bitir();
    }
  }
  document.body.removeChild(kap);
  const uz = (a) => { let L = 0; for (let i = 1; i < a.length; i++) L += Math.hypot(a[i][0] - a[i - 1][0], a[i][1] - a[i - 1][1]); return L; };
  for (const a of dizgi) a.L = uz(a);
  const toplam = dizgi.reduce((t, a) => t + a.L, 0);
  return dizgi.filter((a) => a.L >= toplam * esik).sort((a, b) => b.L - a.L).slice(0, enCok);
}

// ---------- el çizimi şekiller (hepsi nokta dizisi; kalemCizgi'ye verilir) ----------
// El çizimi elips: açılı başlangıç, hafif kapanmayan (dışa kayan) uç. egim: radyan.
export function elips(cx, cy, rx, ry, egim = 0, tohum = 1) {
  const a0 = hash(tohum, 1, 3) * Math.PI * 2, tur = 1.06 + 0.04 * hash(tohum, 2, 3);
  const n = Math.max(24, Math.ceil(Math.PI * (rx + ry) * tur / 9)), ce = Math.cos(egim), se = Math.sin(egim), cik = [];
  for (let i = 0; i <= n; i++) {
    const u = i / n, a = a0 + u * tur * Math.PI * 2, r = 1 + 0.06 * u + 0.025 * gurul(u * 5, tohum);
    const x = rx * r * Math.cos(a), y = ry * r * Math.sin(a);
    cik.push([cx + x * ce - y * se, cy + x * se + y * ce]);
  }
  return cik;
}

// Kalem oku: a'dan b'ye gövde + iki uç çizgisi → 3 nokta dizisi [gövde, uç1, uç2].
export function ok(a, b, tohum = 1) {
  const dx = b[0] - a[0], dy = b[1] - a[1], L = Math.hypot(dx, dy) || 1, d = [dx / L, dy / L], nr = [-d[1], d[0]];
  const egri = (hash(tohum, 4, 5) - 0.5) * L * 0.08;
  const govde = [a, [a[0] + dx * 0.5 + nr[0] * egri, a[1] + dy * 0.5 + nr[1] * egri], b];
  const h = Math.min(36, L * 0.32), aci = 0.5 + 0.08 * (hash(tohum, 6, 5) - 0.5);
  const uc = (sg) => {
    const ca = Math.cos(aci * sg), sa = Math.sin(aci * sg), gx = -d[0], gy = -d[1];
    return [[b[0] + (gx * ca - gy * sa) * h, b[1] + (gx * sa + gy * ca) * h], [b[0] + d[0] * 0.5, b[1] + d[1] * 0.5]];
  };
  return [govde, uc(1), uc(-1)];
}

// El çizimi dikdörtgen: 4 kenar (4 nokta dizisi), köşeler hafif taşar.
export function kutu(x, y, w, h, tohum = 1) {
  const j = (k) => (hash(tohum, k, 9) - 0.5) * 5, e = (k) => 3 + 6 * hash(tohum, k, 11);
  const kenar = (a, b, k) => {
    const dx = b[0] - a[0], dy = b[1] - a[1], L = Math.hypot(dx, dy) || 1, bos = (hash(tohum, k, 13) - 0.5) * 5;
    return [a, [a[0] + dx / 2 - dy / L * bos, a[1] + dy / 2 + dx / L * bos], b];
  };
  return [
    kenar([x - e(1), y + j(1)], [x + w + e(2), y + j(2)], 1),
    kenar([x + w + j(3), y - e(3)], [x + w + j(4), y + h + e(4)], 2),
    kenar([x + w + e(5), y + h + j(5)], [x - e(6), y + h + j(6)], 3),
    kenar([x + j(7), y + h + e(7)], [x + j(8), y - e(8)], 4),
  ];
}

// El çizimi alt çizgi: x0'dan x1'e, y çevresinde hafif eğik ve dalgalı.
export function altCizgi(x0, x1, y, tohum = 1) {
  const d = (k) => (hash(tohum, k, 17) - 0.5) * 5;
  return [[x0, y + d(1)], [(x0 + x1) / 2, y + d(2) * 0.6], [x1, y + d(3)]];
}

// ---------- el yazısı: tegaki glif verisi → kalem darbeleri ----------
// G = tegaki glyphData (font birimi, y aşağı pozitif, 0 taban çizgisi; t/d/a sn; n nib
// damgaları: [noktaIdx, dx, dy, çapA, çapB, açı]). o: {upm, asc, boy (px), x, y (sol üst),
// ya da taban (taban çizgisi y), w (kalınlık çarpanı), renk, alfa, tohum, bosluk (em payı),
// hedefSure (sn: bütün yazı bu
// süreye sığar; yoksa doğal süre), sozcukler ([{t0,t1}]: i. sözcük [t0,t1] penceresine sığar,
// hedefSure yok sayılır; sözcükler boşlukla ayrılır)}.
// Döner: {darbeler: [{bas, sure, c, nib: [{u, x, y, rx, ry, a}]}], sure, gen, taban}; zamanlar
// sn, yazının kendi başlangıcına göre (sözcük penceresi verilmişse mutlak anlatım sn).
// Saf geometri + zaman: darbeler [{bas, sure, pts (px), gen (kalınlık px), nib, soz, nokta}]; motor
// bağımsız (kalem-canvas kalemCizgi'ye, kalem-paper kendi ciz()'ine verir).
export function yaziNoktalari(metin, G, o = {}) {
  const upm = o.upm || 1000, asc = o.asc || 960, boy = o.boy || 48, k = boy / upm;
  const taban = o.taban != null ? o.taban : (o.y || 0) + asc * k;
  const kal = o.w == null ? 1 : o.w, sozler = metin.split(" "), darbeler = [];
  let x = o.x || 0, t0 = 0, tSoz0 = 0;
  for (let si = 0; si < sozler.length; si++) {
    if (si > 0) x += (o.bosluk == null ? 0.3 : o.bosluk) * upm * k;
    const ilk = darbeler.length; tSoz0 = t0;
    for (const ch of sozler[si]) {
      const g = G[ch]; if (!g) throw new Error("glif yok: " + ch);
      g.s.forEach((st) => {
        const pts = st.p.map((q) => [x + q[0] * k, taban + q[1] * k]);
        const gen = st.p.reduce((a, q) => a + (q[2] || 60), 0) / st.p.length * k * kal;
        const uz = pts.slice(1).reduce((a, q, m) =>
          a + Math.hypot(q[0] - pts[m][0], q[1] - pts[m][1]), 0);
        const nib = (st.n || []).map((n) => ({ u: n[0] / Math.max(1, pts.length - 1),
          x: pts[n[0]][0] + n[1] * k, y: pts[n[0]][1] + n[2] * k,
          rx: n[3] / 2 * k, ry: n[4] / 2 * k, a: n[5] }));
        const nokta = uz < 0.6;
        if (nokta) {
          nib.push({ u: 0, x: pts[0][0], y: pts[0][1], rx: gen / 2, ry: gen / 2, a: 0 });
        }
        darbeler.push({ bas: t0 + st.d, sure: Math.max(0.02, st.a), pts, gen, nib, soz: si,
          nokta });
      });
      x += g.w * k; t0 += g.t;
    }
    if (o.sozcukler && o.sozcukler[si]) {         // sözcük penceresi: [tSoz0, t0] → [t0_i, t1_i]
      const q = o.sozcukler[si], dogal = Math.max(0.05, t0 - tSoz0);
      const hiz = (q.t1 - q.t0) / dogal;
      for (let m = ilk; m < darbeler.length; m++) {
        darbeler[m].bas = q.t0 + (darbeler[m].bas - tSoz0) * hiz; darbeler[m].sure *= hiz;
      }
    }
  }
  let sure = t0;
  if (!o.sozcukler && o.hedefSure) {
    const hiz = o.hedefSure / Math.max(0.05, t0);
    for (const d of darbeler) { d.bas *= hiz; d.sure *= hiz; }
    sure = o.hedefSure;
  } else if (o.sozcukler) sure = Math.max(...darbeler.map((d) => d.bas + d.sure));
  return { darbeler, sure, gen: x - (o.x || 0), taban };
}

// Düz canvas: darbeler kalemCizgi nesnesi (c) taşır; nokta darbesinde c yok, yalnız nib.
export function yaziDarbeleri(metin, G, o = {}) {
  const sd = o.tohum == null ? 1 : o.tohum, Y = yaziNoktalari(metin, G, o);
  Y.darbeler = Y.darbeler.map((d, i) => ({ bas: d.bas, sure: d.sure, soz: d.soz, nib: d.nib,
    c: d.nokta ? null : kalemCizgi(d.pts, { w: Math.max(1.4, d.gen), duz: true, amp: 0.25,
      uc0: 2.5, uc1: 3, aralik: 1.6, renk: o.renk, alfa: o.alfa, tohum: sd + i }),
  }));
  Y.renk = o.renk || "@murekkep"; Y.alfa = o.alfa == null ? 0.9 : o.alfa;   // nokta darbeleri (c yok)
  return Y;
}

// El yazısını t anına (sn, yaziDarbeleri zaman ekseni) kadar çizer. Nib damgaları kalem noktayı
// geçince basılır.
export function yaziCiz(ctx, Y, t, carpan = 1) {
  for (const d of Y.darbeler) {
    const u = kis((t - d.bas) / d.sure); if (u <= 0) continue;
    if (d.c) darbeCiz(ctx, d.c, u, carpan);
    const renk = d.c ? d.c.renk : (Y.renk || "@murekkep");          // 05.11: nokta yazının rengini alır
    const alfa = d.c ? d.c.alfa : (Y.alfa == null ? 0.9 : Y.alfa);
    for (const m of d.nib) {
      if (m.u > u) continue;
      ctx.save(); ctx.globalAlpha = alfa * carpan; ctx.fillStyle = renkCoz(renk);
      ctx.beginPath();
      ctx.ellipse(m.x, m.y, Math.max(0.8, m.rx), Math.max(0.8, m.ry), m.a, 0, Math.PI * 2);
      ctx.fill(); ctx.restore();
    }
  }
}

// El yazısının t anındaki kalem ucu (yazan darbe yoksa null).
export function yaziUcu(Y, t) {
  for (const d of Y.darbeler) {
    const u = (t - d.bas) / d.sure;
    if (u > 0 && u < 1) return d.c ? basUcu(d.c, u) : [d.nib[0].x, d.nib[0].y];
  }
  return null;
}

// ---------- Yönlendirici Nokta Pilot (Nadir 12.11) ----------
// Bayrak: ?nokta=1 ya da window.KALEM_NOKTA === true (yayın varsayılanı kapalı).
export function noktaAktif() {
  if (typeof window === "undefined") return false;
  if (window.KALEM_NOKTA === true) return true;
  try {
    const q = new URLSearchParams(window.location.search).get("nokta");
    return q === "1" || q === "true";
  } catch (e) {
    console.warn("nokta bayrağı okunamadı:", e);
    return false;
  }
}

// Yumuşak geçiş: ease-in-out cubic
export function easeInOutCubic(t) {
  t = Math.min(1, Math.max(0, t));
  return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

function hexToRgb(hex) {
  if (typeof hex !== "string") return [242, 169, 59];
  hex = hex.replace("#", "");
  if (hex.length === 3) hex = hex.split("").map((c) => c + c).join("");
  const num = parseInt(hex, 16);
  if (Number.isNaN(num)) return [242, 169, 59];
  return [(num >> 16) & 255, (num >> 8) & 255, num & 255];
}

// Nokta görünümü: çap 14 px (yarıçap 7 px), dolgu tema vurgu rengi, 6 px yumuşak hale (alfa 0.25).
export function noktaCizCanvas(ctx, x, y, alpha = 1) {
  if (alpha <= 0.001) return;
  const r = 7;
  const rHale = 13;
  const renkVurgu = renkCoz(RT.vurgu);
  const rgb = hexToRgb(renkVurgu);

  ctx.save();
  // 1. Yumuşak hale (6 px, alfa 0.25 * alpha)
  const grad = ctx.createRadialGradient(x, y, r, x, y, rHale);
  grad.addColorStop(0, `rgba(${rgb[0]},${rgb[1]},${rgb[2]},${0.25 * alpha})`);
  grad.addColorStop(1, `rgba(${rgb[0]},${rgb[1]},${rgb[2]},0)`);

  ctx.fillStyle = grad;
  ctx.beginPath();
  ctx.arc(x, y, rHale, 0, Math.PI * 2);
  ctx.fill();

  // 2. Çekirdek nokta (çap 14 px, yarıçap 7 px)
  ctx.fillStyle = `rgba(${rgb[0]},${rgb[1]},${rgb[2]},${alpha})`;
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI * 2);
  ctx.fill();

  ctx.restore();
}

// Zaman çizelgesi ve konum yöneticisi (deterministik, durum birikimi yok).
export class NoktaYoneticisi {
  constructor(fps = 30) {
    this.fps = fps;
    this.darbeler = [];
    this.sirali = false;
  }

  ekle({ bas, sure, konum, basKonum, bitKonum }) {
    this.darbeler.push({
      bas,
      sure: Math.max(1, sure),
      konum,
      basKonum: basKonum || (() => konum(bas)),
      bitKonum: bitKonum || (() => konum(bas + sure)),
      idx: this.darbeler.length,
    });
    this.sirali = false;
  }

  hazirla() {
    if (this.sirali) return;
    this.darbeler.sort((a, b) => a.bas - b.bas || a.idx - b.idx);
    this.sirali = true;
  }

  durum(f) {
    this.hazirla();
    if (this.darbeler.length === 0) return { x: 0, y: 0, alfa: 0 };

    // (a) Çizim sürerken: o anda ilerleyen darbenin ucu (birden çok ise en son başlayan)
    let aktif = null;
    for (let i = 0; i < this.darbeler.length; i++) {
      const d = this.darbeler[i];
      if (f >= d.bas && f < d.bas + d.sure) {
        if (!aktif || d.bas > aktif.bas || (d.bas === aktif.bas && d.idx > aktif.idx)) {
          aktif = d;
        }
      }
    }
    if (aktif) {
      const p = aktif.konum(f);
      return { x: p[0], y: p[1], alfa: 1 };
    }

    // Hiçbir darbe aktif değil: önceki ve sonraki darbeyi bul
    let onceki = null, oncekiBit = -Infinity;
    for (let i = 0; i < this.darbeler.length; i++) {
      const d = this.darbeler[i], dBit = d.bas + d.sure;
      if (dBit <= f) {
        if (!onceki || dBit > oncekiBit || (dBit === oncekiBit && d.bas > onceki.bas)) {
          onceki = d;
          oncekiBit = dBit;
        }
      }
    }

    let sonraki = null, sonrakiBas = Infinity;
    for (let i = 0; i < this.darbeler.length; i++) {
      const d = this.darbeler[i];
      if (d.bas > f) {
        if (!sonraki || d.bas < sonrakiBas || (d.bas === sonrakiBas && d.idx < sonraki.idx)) {
          sonraki = d;
          sonrakiBas = d.bas;
        }
      }
    }

    // İki darbe arasında
    if (onceki && sonraki) {
      const tPrevEnd = onceki.bas + onceki.sure;
      const tNextStart = sonraki.bas;
      const boslukSn = (tNextStart - tPrevEnd) / this.fps;

      if (boslukSn <= 1.5) {
        // (b) Boşluk <= 1.5 sn: yumuşak geçiş (easeInOutCubic)
        const u = (f - tPrevEnd) / (tNextStart - tPrevEnd);
        const e = easeInOutCubic(u);
        const p0 = onceki.bitKonum(), p1 = sonraki.basKonum();
        return {
          x: p0[0] + (p1[0] - p0[0]) * e,
          y: p0[1] + (p1[1] - p0[1]) * e,
          alfa: 1,
        };
      } else {
        // (c) Boşluk > 1.5 sn: 0.6 sn durur, 0.3 sn'de söner; yeni darbeden 0.4 sn önce belirir
        const tGecen = (f - tPrevEnd) / this.fps;
        const tKalan = (tNextStart - f) / this.fps;

        if (tGecen <= 0.6) {
          const p = onceki.bitKonum();
          return { x: p[0], y: p[1], alfa: 1 };
        } else if (tGecen <= 0.9) {
          const p = onceki.bitKonum();
          const al = 1 - (tGecen - 0.6) / 0.3;
          return { x: p[0], y: p[1], alfa: Math.max(0, Math.min(1, al)) };
        } else if (tKalan <= 0.4) {
          const p = sonraki.basKonum();
          const al = (0.4 - tKalan) / 0.4;
          return { x: p[0], y: p[1], alfa: Math.max(0, Math.min(1, al)) };
        } else {
          return { x: 0, y: 0, alfa: 0 };
        }
      }
    }

    // İlk darbeden önce: 0.4 sn önce başlangıç noktasında belirir
    if (sonraki && !onceki) {
      const tKalan = (sonraki.bas - f) / this.fps;
      if (tKalan <= 0.4) {
        const p = sonraki.basKonum();
        const al = (0.4 - tKalan) / 0.4;
        return { x: p[0], y: p[1], alfa: Math.max(0, Math.min(1, al)) };
      }
      return { x: 0, y: 0, alfa: 0 };
    }

    // Son darbeden sonra: 0.6 sn durur, 0.3 sn'de söner
    if (onceki && !sonraki) {
      const tPrevEnd = onceki.bas + onceki.sure;
      const tGecen = (f - tPrevEnd) / this.fps;
      if (tGecen <= 0.6) {
        const p = onceki.bitKonum();
        return { x: p[0], y: p[1], alfa: 1 };
      } else if (tGecen <= 0.9) {
        const p = onceki.bitKonum();
        const al = 1 - (tGecen - 0.6) / 0.3;
        return { x: p[0], y: p[1], alfa: Math.max(0, Math.min(1, al)) };
      }
      return { x: 0, y: 0, alfa: 0 };
    }

    return { x: 0, y: 0, alfa: 0 };
  }

  ciz(ctx, f) {
    const d = this.durum(f);
    if (d.alfa <= 0.001) return;
    noktaCizCanvas(ctx, d.x, d.y, d.alfa);
  }
}

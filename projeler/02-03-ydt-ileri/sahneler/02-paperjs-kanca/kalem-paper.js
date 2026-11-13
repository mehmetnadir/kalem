// Paper.js "kendini çizen kalem" ortak modülü — sahne 02 ve 03 buradan import eder.
// Zaman yalnız kare numarasından gelir; Math.random / Date yok (tohumlu hash).
// Kullanım: const S = await sahneKur(paper, { KARE, tBas, bolum, etkin }); ...içerik...; S.kare(f) -> canvas
import { kunyeHazirla, zeminCiz, kunyeCiz, RENK, RT, renkCoz, temaSurum, KOK } from "/projeler/02-03-ydt-ileri/ortak/kunye.js";
import { yaziNoktalari } from "/projeler/02-03-ydt-ileri/ortak/kalem-canvas.js";
// Geliştirme günlüğü (12.11, pp g-11): POST /log yalnız yerel geliştirme sunucusunda; yayında istek yok.
const YEREL_SUNUCU = /^(localhost|127\.0\.0\.1|\[::1\]|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+)$/
  .test(location.hostname);
const logGonder = (o) => (YEREL_SUNUCU ? fetch("/log", o).catch(() => {}) : Promise.resolve());

const W = 1920, H = 1080;
export { RENK, RT, renkCoz };
export const kis = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const yumus = (x) => { x = kis(x); return x * x * (3 - 2 * x); };
export const cikis = (x) => 1 - Math.pow(1 - kis(x), 3);          // ease-out cubic
const lerp = (a, b, t) => a + (b - a) * t;
const hash = (a, b = 0, c = 0) => { let h = (Math.imul(a | 0, 374761393) + Math.imul(b | 0, 668265263) +
  Math.imul(c | 0, 1274126177)) | 0; h = Math.imul(h ^ (h >>> 13), 1274126177); h ^= h >>> 16; return (h >>> 0) / 4294967296; };
const gurul = (x, s) => { const i = Math.floor(x), f = x - i, u = f * f * (3 - 2 * f);
  return lerp(hash(i, s, 7), hash(i + 1, s, 7), u) - 0.5; };

export async function sahneKur(P, { KARE, tBas, bolum, etkin, kayma = 0 }) {   // kayma: sözcüklerin eski çerçeveye çevrilmesi (sn)
  const K = await kunyeHazirla();
  const sozcukJson = await (await fetch(`${KOK}/anlatim/sozcukler.json`)).json();
  // El yazısı verisi (tegaki, Caveat 700 Türkçe; ortak/tegaki/caveat-tr/KAYNAK.md)
  const [eyM, eyG] = await Promise.all([fetch(`/ortak/tegaki/caveat-tr/metrik.json`),
    fetch(`/ortak/tegaki/caveat-tr/glyphData-700.json`)]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  P.setup(document.getElementById("cv")); P.view.autoUpdate = false;
  const out = document.createElement("canvas"); out.width = W; out.height = H;
  const oc = out.getContext("2d");
  const olc = document.createElement("canvas").getContext("2d");
  const SON = KARE - 13;                                           // son 12 kare durgun: zaman burada donar
  const pt = (q) => new P.Point(q[0], q[1]);
  const fr = (t) => Math.round((t - tBas) * 30);
  const CIZGILER = [], YAZILAR = [], DINAMIK = [], OGELER = [], OLAY = new Map(), ZAMAN = [];
  let tohum = 1, sonSurum = temaSurum();

  const olay = (k, tur, guc) => { k = Math.max(0, Math.min(KARE - 1, Math.round(k))); const a = k + "|" + tur;
    if (!OLAY.has(a) || OLAY.get(a).guc < guc) OLAY.set(a, { kare: k, tur, guc: +guc.toFixed(2) }); };
  const not = (ad, kare) => ZAMAN.push({ ad, kare: Math.round(kare) });
  const genislik = (s, font) => { olc.font = font; return olc.measureText(s).width; };

  // ---------- kalem darbesi geometrisi (ornek/ucan-makine/01-paperjs cizgi() uyarlaması) ----------
  function ornekDuz(pts, ara) {                                    // çizgi parçalı, yay uzunluğuna göre eşit aralık
    const cum = [0]; for (let i = 1; i < pts.length; i++) cum.push(cum[i - 1] + Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]));
    const L = Math.max(1, cum[cum.length - 1]), n = Math.max(3, Math.ceil(L / ara) + 1), r = [];
    let j = 0;
    for (let i = 0; i < n; i++) {
      const s = L * i / (n - 1); while (j < pts.length - 2 && cum[j + 1] < s) j++;
      const l = Math.max(1e-6, cum[j + 1] - cum[j]), u = kis((s - cum[j]) / l), a = pts[j], b = pts[j + 1];
      const dx = b[0] - a[0], dy = b[1] - a[1], dl = Math.hypot(dx, dy) || 1;
      r.push({ s, x: a[0] + dx * u, y: a[1] + dy * u, nx: -dy / dl, ny: dx / dl });
    }
    return { L, r };
  }
  function ornekEgri(pts, ara) {                                   // catmull-rom ile yumuşatılmış az noktalı yol
    const yolu = new P.Path({ segments: pts.map(pt), insert: false }); if (pts.length > 2) yolu.smooth({ type: "catmull-rom" });
    const L = Math.max(1, yolu.length), n = Math.max(3, Math.ceil(L / ara) + 1), r = [];
    for (let i = 0; i < n; i++) { const s = Math.min(L * i / (n - 1), yolu.length - 1e-3), q = yolu.getPointAt(s), nr = yolu.getNormalAt(s) || new P.Point(0, 0);
      r.push({ s: L * i / (n - 1), x: q.x, y: q.y, nx: nr.x, ny: nr.y }); }
    yolu.remove(); return { L, r };
  }
  function kalemGeo(pts, o = {}) {
    const sd = o.tohum || tohum++;
    const { L, r } = o.duz ? ornekDuz(pts, o.aralik || 2.4) : ornekEgri(pts, o.aralik || 2.4), n = r.length;
    const amp = o.amp == null ? 1.1 : o.amp, w0 = o.w || 3.4;
    const p = r.map((q) => { const sap = amp * (gurul(q.s / 55, sd) * 1.6 + gurul(q.s / 14, sd + 99) * 0.5); return [q.x + q.nx * sap, q.y + q.ny * sap]; });
    const nrm = p.map((_, i) => { const a = p[Math.max(0, i - 1)], b = p[Math.min(n - 1, i + 1)], dx = b[0] - a[0], dy = b[1] - a[1], l = Math.hypot(dx, dy) || 1; return [-dy / l, dx / l]; });
    const tb = Math.min(L * 0.3, o.uc0 || 16), te = Math.min(L * 0.4, o.uc1 || 34);
    const w = p.map((_, i) => { const s = L * i / (n - 1), tp = Math.pow(kis(s / tb), 0.6) * Math.pow(kis((L - s) / te), 0.7);
      return Math.max(0.3, w0 * (0.12 + 0.88 * tp) * (0.82 + 0.36 * (gurul(s / 70, sd + 5) + 0.5))); });
    return { p, nrm, w, n, L, renk: o.renk || RT.murekkep, alfa: o.alfa == null ? 0.9 : o.alfa };
  }
  function cokgen(c, t) {                                          // t kadar çizilmiş kalem darbesi: kapalı dolgu çokgen
    const m = t * (c.n - 1), k = Math.floor(m), fr_ = m - k, sol = [], sag = [];
    const ekle = (q, nr, w) => { sol.push([q[0] + nr[0] * w / 2, q[1] + nr[1] * w / 2]); sag.push([q[0] - nr[0] * w / 2, q[1] - nr[1] * w / 2]); };
    for (let i = 0; i <= Math.min(k, c.n - 1); i++) ekle(c.p[i], c.nrm[i], c.w[i]);
    if (k < c.n - 1 && fr_ > 0) ekle([lerp(c.p[k][0], c.p[k + 1][0], fr_), lerp(c.p[k][1], c.p[k + 1][1], fr_)], c.nrm[k], lerp(c.w[k], c.w[k + 1], fr_));
    const seg = sol.concat(sag.reverse());
    return new P.Path({ segments: seg.map(pt), closed: true, fillColor: renkCoz(c.renk), opacity: c.alfa, insert: false });
  }
  const ilerle = (c, f) => { const t = kis((f - c.bas) / c.sure); return 0.35 * t + 0.65 * yumus(t); };

  // ---------- öğe (grup + hareket) ----------
  // o.kay = {f0, f1, dx, dy} yürüme; o.nefes = {bas, cx, cy} 6 sn'de bir 1,00 -> 1,012; o.alfa(f) -> 0..1
  function oge(o = {}) {
    const g = new P.Group({ applyMatrix: false }); const e = { g, ...o }; OGELER.push(e); return e;
  }
  const kok = oge({});

  // ---------- darbe ----------
  // ciz(pts, {bas, sure, w, renk, alfa, duz, uc0, uc1, amp, oge, ses}) ; ses: false | "tik" | "parilti" | (varsayılan "cizgi")
  function ciz(pts, o = {}) {
    const c = kalemGeo(pts, o); c.bas = o.bas || 0; c.sure = Math.max(2, o.sure || 20); c.og = o.oge || kok; c.yolP = null; c.tam = false;
    c.tur = o.tur || "cizim"; c.ad = o.ad || "cizgi";
    CIZGILER.push(c);
    if (o.ses !== false) {
      if (o.ses === "tik") olay(c.bas, "tik", 0.5); else if (o.ses === "parilti") olay(c.bas, "parilti", 0.5);
      else olay(c.bas, "cizgi", Math.min(0.7, 0.4 + c.L / 1500));
    }
    return c;
  }
  const bitis = (c) => c.bas + c.sure;

  // el çizimi daire/elips (hafif eğik, biraz taşan); sarı belirteç
  function daire(cx, cy, rx, ry, o = {}) {
    const tur = o.tur || 1.08, a0 = o.a0 == null ? -2.3 : o.a0, egim = o.egim == null ? -0.07 : o.egim, sd = tohum + 500;
    const per = Math.PI * (rx + ry), n = Math.max(24, Math.ceil(per * tur / 6)), ce = Math.cos(egim), se = Math.sin(egim);
    const pts = Array.from({ length: n }, (_, i) => { const u = i / (n - 1), a = a0 + u * tur * 2 * Math.PI, k = 1 + 0.05 * gurul(u * 4, sd) + 0.05 * (u - 0.5);
      const x = Math.cos(a) * rx * k, y = Math.sin(a) * ry * k; return [cx + x * ce - y * se, cy + x * se + y * ce]; });
    return ciz(pts, { w: 7.5, renk: RT.vurgu, alfa: 0.85, amp: 0.4, uc0: 14, uc1: 40, tur: "isaret", ad: o.ad || "daire", ...o });
  }
  // eğri: a'dan b'ye dik yönde sin profiliyle bükülmüş nokta dizisi
  function egri(a, b, bukum, yon, n = 9) {
    const d = [b[0] - a[0], b[1] - a[1]], l = Math.hypot(d[0], d[1]);
    let pr = [-d[1] / l, d[0] / l]; if (yon && (pr[0] * yon[0] + pr[1] * yon[1]) < 0) pr = [-pr[0], -pr[1]];
    return Array.from({ length: n }, (_, i) => { const u = i / (n - 1), s = Math.sin(Math.PI * u) * bukum * l; return [a[0] + d[0] * u + pr[0] * s, a[1] + d[1] * u + pr[1] * s]; });
  }
  // kalemle ok: gövde + uç çizgileri (cift: iki yönlü)
  function ok(a, b, o = {}) {
    const pts = egri(a, b, o.bukum == null ? 0.06 : o.bukum, o.yon), sure = o.sure || 18, w = o.w || 7, renk = o.renk || RT.vurgu, alfa = o.alfa == null ? 0.85 : o.alfa;
    const g = ciz(pts, { w, renk, alfa, bas: o.bas, sure, uc0: 10, uc1: 14, amp: 0.7, oge: o.oge, tur: "isaret", ad: o.ad || "ok" });
    const uc = (tip, ard, ses) => { const dx = tip[0] - ard[0], dy = tip[1] - ard[1], l = Math.hypot(dx, dy) || 1, ux = dx / l, uy = dy / l, k = o.uzun || 24;
      const rot = (a_) => [-(ux * Math.cos(a_) - uy * Math.sin(a_)) * k + tip[0], -(ux * Math.sin(a_) + uy * Math.cos(a_)) * k + tip[1]];
      return ciz([rot(0.5), tip, rot(-0.5)], { w: w * 0.9, renk, alfa, bas: o.bas + sure - 2, sure: 8, uc0: 6, uc1: 6, amp: 0.4, duz: true, oge: o.oge, ses, tur: "isaret", ad: (o.ad || "ok") + ":uc" }); };
    uc(pts[pts.length - 1], pts[pts.length - 3], false);
    if (o.cift) uc(pts[0], pts[2], false);
    return g;
  }
  // el çizimi kutu: dört kenar sırayla, köşeler hafif taşar
  function kutu(x, y, w, h, o = {}) {
    const sure = o.sure || 40, k = [[[x - 6, y + 2], [x + w + 8, y - 2]], [[x + w + 2, y - 8], [x + w - 2, y + h + 9]],
      [[x + w + 7, y + h + 2], [x - 8, y + h - 2]], [[x + 2, y + h + 8], [x - 2, y - 10]]];
    const top = k.reduce((s, q) => s + Math.hypot(q[1][0] - q[0][0], q[1][1] - q[0][1]), 0); let cur = o.bas;
    k.forEach((q, i) => { const l = Math.hypot(q[1][0] - q[0][0], q[1][1] - q[0][1]), sr = Math.max(4, sure * l / top);
      ciz([q[0], [(q[0][0] + q[1][0]) / 2 + 1.5 * (i % 2 ? 1 : -1), (q[0][1] + q[1][1]) / 2 + 1.2], q[1]], { w: o.w || 3.6, renk: o.renk || RT.ikincil, alfa: 0.9,
        bas: cur, sure: sr, uc0: 10, uc1: 12, oge: o.oge, ses: i === 0 ? true : false, tur: "kart", ad: o.ad || "kutu" }); cur += sr; });
    return { bit: cur };
  }
  // sarı tik
  function tik(cx, cy, o = {}) {
    return ciz([[cx - 14, cy + 1], [cx - 4, cy + 12], [cx + 17, cy - 15]], { w: 7, renk: RT.vurgu, alfa: 0.9, bas: o.bas, sure: 9, uc0: 5, uc1: 8, amp: 0.3, ses: "tik", oge: o.oge, tur: "isaret", ad: o.ad || "tik" });
  }

  // ---------- SVG (figür / nesne) ----------
  // svgCiz(dosya, {kutu:[x,y,w,h], bas, sure, azami, kisaAtla, yuz, ayna, w, sesAralik, oge}) -> {oge, sinir}
  async function svgCiz(dosya, o) {
    const metin = await (await fetch(`${KOK}/cizim/${dosya}`)).text();
    const g = P.project.importSVG(metin, { insert: false, expandShapes: true, applyMatrix: true });
    if (o.ayna) g.scale(-1, 1);
    g.fitBounds(new P.Rectangle(o.kutu[0], o.kutu[1], o.kutu[2], o.kutu[3]));
    const yollar = g.getItems({ match: (it) => it instanceof P.Path && ((it.parent instanceof P.CompoundPath ? it.parent : it).fillColor || (it.parent instanceof P.CompoundPath ? it.parent : it).strokeColor) && it.length > 0.5 });
    const top = yollar.reduce((s, p) => s + p.length, 0), esik = top * (o.kisaAtla == null ? 0.02 : o.kisaAtla);
    let uzun = yollar.filter((p) => p.length >= esik).sort((a, b) => b.length - a.length);
    const kisa = yollar.filter((p) => p.length < esik).sort((a, b) => b.length - a.length).slice(0, o.yuz || 0);   // yüz çizgileri korunur
    const az = o.azami || 25; uzun = uzun.slice(0, Math.max(1, az - kisa.length));
    const liste = uzun.concat(kisa).sort((a, b) => b.length - a.length);
    const ogeS = o.oge || oge({}); const sinir = g.bounds.clone();
    const agirlik = liste.map((p) => 6 + Math.pow(p.length, 0.72)), ust = 2.1;
    const tp = agirlik.reduce((s, a) => s + a, 0) + agirlik[agirlik.length - 1] * (ust - 1), kf = o.sure / tp; let cur = o.bas;
    liste.forEach((p, i) => {
      const n = Math.max(6, Math.ceil(p.length / 4.5)), pts = [];
      for (let j = 0; j < n; j++) { const q = p.getPointAt(Math.min(p.length * j / (n - 1), p.length - 1e-3)); pts.push([q.x, q.y]); }
      if (p.closed) pts.push(pts[0]);
      const sa = o.sesAralik || 4;
      ciz(pts, { duz: true, w: o.w || 3.4, amp: o.amp == null ? 0.8 : o.amp, renk: o.renk, alfa: 0.92, bas: cur, sure: Math.max(3, agirlik[i] * kf * ust), oge: ogeS,
        uc0: 10, uc1: 22, ses: i % sa === 0 });
      cur += agirlik[i] * kf;
    });
    g.remove();
    return { oge: ogeS, sinir, adet: liste.length };
  }

  // ---------- yazı ----------
  // yazi(str, {x,y,boyut,aile,agirlik,renk,bas,sure,olcek,hizala,ses}) -> {x0,x1,y,boyut}
  function yazi(str, o) {
    const boyut = o.boyut || 48, aile = o.aile || "Caveat", agirlik = o.agirlik || 700, font = `${agirlik} ${boyut}px ${aile}`;
    const w = genislik(str, font), x0 = o.hizala === "orta" ? o.x - w / 2 : o.hizala === "sag" ? o.x - w : o.x;
    const g = new P.Group({ applyMatrix: false });
    const tx = new P.PointText({ point: [x0, o.y], content: str, fillColor: renkCoz(o.renk || RT.murekkep), fontFamily: aile, fontWeight: agirlik, fontSize: boyut });
    g.addChild(tx); g.visible = false;
    const y = { g, tx, renk: o.renk || RT.murekkep, str, x0, x1: x0 + w, y: o.y, boyut, bas: o.bas, sure: o.sure || 4, olcek: !!o.olcek, w, oge: o.oge, sondur: o.sondur };
    YAZILAR.push(y);
    if (o.ses) olay(o.bas, o.ses === true ? "tik" : o.ses, 0.5);
    return y;
  }
  function yaziGuncelle(y, f) {
    const u = kis((f - y.bas) / y.sure);
    if (f < y.bas) { y.g.visible = false; return; }
    y.g.visible = true;
    const renk = renkCoz(y.renk);   // her karede atanırsa Paper metin yerleşimini siler (10.11)
    if (y.sonRenk !== renk) { y.tx.fillColor = renk; y.sonRenk = renk; }
    const k = y.g.children;
    if (u < 1) {
      if (k.length > 1) k[0].remove();
      const m = new P.Path.Rectangle({ from: [y.x0 - 8, y.y - y.boyut * 1.15], to: [y.x0 - 8 + (y.w + 16) * cikis(u), y.y + y.boyut * 0.5], clipMask: true, insert: false });
      y.g.insertChild(0, m);
    } else if (k.length > 1) { k[0].remove(); y.g.clipped = false; }
    y.g.opacity = kis((f - y.bas) / Math.max(2, y.sure * 0.6));
    if (y.sondur) { const q = kis((f - y.sondur[0]) / (y.sondur[1] - y.sondur[0])); y.g.opacity *= 1 - q; if (q >= 1) y.g.visible = false; }   // 02-03: faz geçişinde sönme
    if (y.olcek) { const s = 0.92 + 0.08 * cikis((f - y.bas) / 10.5), cx = y.x0 + y.w / 2, cy = y.y - y.boyut * 0.3;
      y.g.matrix = new P.Matrix().translate(cx, cy).scale(s).translate(-cx, -cy); }
  }
  // cumle(kelimeler=[{s, f, satir}], {x, y, boyut, aile, agirlik, renk, aralik}) -> kelime dizisi (konumlarla)
  function cumle(kel, o) {
    const font = `${o.agirlik || 700} ${o.boyut}px ${o.aile || "Fredoka"}`, bosluk = genislik(" ", font) * 1.0, sat = {};
    const sonuc = [];
    for (const k of kel) {
      const s = k.satir || 0; const x = sat[s] == null ? o.x : sat[s];
      const yz = yazi(k.s, { x, y: o.y + s * (o.aralik || 80), boyut: o.boyut, aile: o.aile || "Fredoka", agirlik: o.agirlik || 700, renk: o.renk, bas: k.f, sure: 4 });
      sat[s] = yz.x1 + bosluk; sonuc.push(yz);
    }
    return sonuc;
  }
  // konuşulan sözcüğün altında kayan sarı kalem çizgisi; son sözcükte durur, sonra solar
  function altCizgi(kel, o = {}) {
    const hold = o.tut || 36, solma = 16, kay = 3;
    const g = new P.Group({ applyMatrix: false }), son = kel[kel.length - 1].bas;
    olay(kel[0].bas, "cizgi", 0.5);
    DINAMIK.push((f) => {
      g.removeChildren();
      if (f < kel[0].bas || f > son + hold + solma) return;
      let i = 0; while (i + 1 < kel.length && kel[i + 1].bas <= f) i++;
      const a = kel[Math.max(0, i - 1)], b = kel[i], u = i === 0 ? 1 : yumus((f - b.bas) / kay);
      const sp = (z) => ({ x0: z.x0 - 3, x1: z.x1 + 3, y: z.y + z.boyut * 0.16 });
      const A = sp(a), B = sp(b);
      let x0 = lerp(A.x0, B.x0, u), x1 = lerp(A.x1, B.x1, u); const y = lerp(A.y, B.y, u);
      if (i === 0) x1 = lerp(x0, x1, cikis((f - b.bas) / 5));
      const c = kalemGeo([[x0, y + 1.5], [x1, y - 1.5]], { duz: true, w: o.w || 7, renk: RT.vurguDolgu, alfa: 0.85, amp: 1.2, uc0: 8, uc1: 12, tohum: 77 });
      const p = cokgen(c, 1); p.opacity = 0.85 * (f > son + hold ? 1 - (f - son - hold) / solma : 1); g.addChild(p);
    });
    return g;
  }
  const dinamik = (fn) => { const g = new P.Group({ applyMatrix: false }); DINAMIK.push((f) => { g.removeChildren(); fn(f, g); }); return g; };

  // parıltı: 4 uçlu küçük yıldız (kalem darbeleri), bas'ta açılıp 20 karede söner; periyot > 0 ise tekrarlanır
  function parilti(cx, cy, o = {}) {
    const r = o.r || 26, sure = 22, per = o.periyot || 0, adet = o.adet || 1;
    for (let i = 0; i < adet; i++) olay(o.bas + i * per, "parilti", 0.5);
    dinamik((f, g) => {
      for (let i = 0; i < adet; i++) {
        const t = (f - o.bas - i * per) / sure; if (t < 0 || t > 1) continue;
        const e = Math.sin(Math.PI * t) * r;
        for (const [a, k] of [[0, 1], [Math.PI / 2, 1], [Math.PI / 4, 0.6], [-Math.PI / 4, 0.6]]) {
          const dx = Math.cos(a) * e * k, dy = Math.sin(a) * e * k;
          const c = kalemGeo([[cx - dx, cy - dy], [cx + dx, cy + dy]], { duz: true, w: 4.6, renk: o.renk || RT.vurgu, alfa: 0.9, amp: 0.2, tohum: 31 + i });
          g.addChild(cokgen(c, 1));
        }
      }
    });
  }

  // ---------- el yazısı (tegaki Caveat darbeleri, kendi kalemimizle; pilot 05.11, karar 5–6) ----------
  // elYazisi(str, {x, y (taban), boyut, renk, alfa, bas (kare), sure (kare, hedef), sozcukler ([{f0, f1}] kare:
  //   her sözcük kendi konuşma penceresinde), oge, ses}) -> {x0, x1, y, boyut, bas, bit, w, g}
  function elYazisi(str, o) {
    const boyut = o.boyut || 48, renk = o.renk || RT.murekkep, alfa = o.alfa == null ? 0.9 : o.alfa;
    const soz = o.sozcukler ? o.sozcukler.map((q) => ({ t0: q.f0 / 30, t1: q.f1 / 30 })) : null;
    const Y = yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm, asc: EY.M.ascender, boy: boyut, x: o.x, taban: o.y,
      sozcukler: soz, hedefSure: o.sure ? o.sure / 30 : undefined });
    const bas0 = soz ? 0 : (o.bas || 0);                             // sözcük penceresi: zamanlar mutlak kare
    const darbeler = Y.darbeler.map((d) => {
      const fb = bas0 + d.bas * 30, fs = Math.max(2, d.sure * 30);
      const c = d.nokta ? null : ciz(d.pts, { duz: true, w: Math.max(1.4, d.gen), amp: 0.25, uc0: 2.5,
        uc1: 3, aralik: 1.6, renk, alfa, bas: fb, sure: fs, oge: o.oge, ses: false, tur: "yazi", ad: str });
      return { c, fb, fs, nib: d.nib };
    });
    if (o.ses !== false) (soz ? soz.map((q) => q.t0 * 30) : [bas0]).forEach((f) => olay(f, "cizgi", 0.35));
    const g = dinamik((f, gr) => {                                   // nib damgaları: kalem noktayı geçince
      for (const d of darbeler) {
        const t = d.c ? ilerle(d.c, f) : kis((f - d.fb) / d.fs); if (t <= 0) continue;
        for (const m of d.nib) {
          if (m.u > t) continue;
          const e = new P.Path.Ellipse({ center: [m.x, m.y], radius: [Math.max(0.8, m.rx), Math.max(0.8, m.ry)],
            fillColor: renkCoz(renk), opacity: alfa, insert: false });
          e.rotate(m.a * 180 / Math.PI); gr.addChild(e);
        }
      }
    });
    g.data = { kalemTur: "yazi", kalemAd: str };
    if (o.oge) { o.oge.g.addChild(g); o.oge.g.data = { kalemTur: "yazi", kalemAd: str }; }
    const bas = Math.min(...darbeler.map((d) => d.fb)), bit = Math.max(...darbeler.map((d) => d.fb + d.fs));
    return { x0: o.x, x1: o.x + Y.gen, y: o.y, boyut, bas, bit, w: Y.gen, g };
  }

  // ---------- sözcük zamanları ----------
  const sozcukler = (cumleNo) => sozcukJson.filter((s) => s.cumle === cumleNo).map((s) => ({ s: s.sozcuk, t: s.t0 + kayma, f: fr(s.t0 + kayma),
    t1: s.t1 + kayma, f1: fr(s.t1 + kayma) }));

  // ---------- Kanca (paperTopla) ----------
  if (typeof window !== "undefined") {
    if (!window.__kalemKutu) {
      window.__kalemKutu = {
        kare: [],
        ekle(tur, ad, x, y, w, h) {
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
    window.__kalemKutu.paperTopla = function () {
      if (!P || !P.project) return;
      const kunyeler = (this.kare || []).filter((k) => k.tur === "kunye");
      this.kare = kunyeler;
      function topla(item) {
        if (!item || item.visible === false) return;
        if (item.opacity != null && item.opacity < 0.2) return;
        if (item.data && item.data.kalemTur) {
          let b = item.bounds;
          if (item.clipped && item.children && item.children.length > 0) {
            const mask = item.children.find((c) => c.clipMask);
            const icerikler = item.children.filter((c) => !c.clipMask && c.visible !== false);
            if (mask && icerikler.length > 0) {
              let ix0 = Infinity, iy0 = Infinity, ix1 = -Infinity, iy1 = -Infinity;
              for (const c of icerikler) {
                const cb = c.bounds;
                if (cb.width > 0 && cb.height > 0) {
                  ix0 = Math.min(ix0, cb.x);
                  iy0 = Math.min(iy0, cb.y);
                  ix1 = Math.max(ix1, cb.x + cb.width);
                  iy1 = Math.max(iy1, cb.y + cb.height);
                }
              }
              if (ix0 < ix1 && iy0 < iy1) {
                const mb = mask.bounds;
                const x0 = Math.max(ix0, mb.x);
                const y0 = Math.max(iy0, mb.y);
                const x1 = Math.min(ix1, mb.x + mb.width);
                const y1 = Math.min(iy1, mb.y + mb.height);
                const w = x1 - x0;
                const h = y1 - y0;
                if (w > 0 && h > 0) {
                  b = { x: x0, y: y0, width: w, height: h };
                } else {
                  return;
                }
              }
            }
          }
          if (b && b.width > 0 && b.height > 0) {
            window.__kalemKutu.ekle(item.data.kalemTur, item.data.kalemAd || "", b.x, b.y, b.width, b.height);
            return;
          }
        }
        if (item.children && item.children.length > 0) {
          for (const child of item.children) topla(child);
        }
      }
      for (const layer of P.project.layers) topla(layer);
    };
  }

  // olaylar.json kaynağı (02-03): canlı kipte /log yutulur; sahne-kare --olc "JSON.stringify(window.__kalemOlaylar())"
  if (typeof window !== "undefined") window.__kalemOlaylar = () => {
    const say = {}; return [...OLAY.values()].sort((a, b) => a.kare - b.kare || b.guc - a.guc)
      .filter((e) => { if (e.kare > SON) return false; say[e.kare] = (say[e.kare] || 0) + 1; return say[e.kare] <= 3; });
  };

  // ---------- kare ----------
  function matrisUygula(e, f) {
    let tx = 0, ty = 0, s = 1, cx = 0, cy = 0;
    if (e.kay) { const u = yumus((f - e.kay.f0) / (e.kay.f1 - e.kay.f0)); tx = e.kay.dx * u; ty = (e.kay.dy || 0) * u; }
    if (e.nefes && f > e.nefes.bas) { const ph = (f - e.nefes.bas) / 180; s = 1 + 0.012 * (0.5 - 0.5 * Math.cos(2 * Math.PI * ph)); cx = e.nefes.cx; cy = e.nefes.cy; }
    e.g.matrix = new P.Matrix().translate(tx, ty).translate(cx, cy).scale(s).translate(-cx, -cy);
    if (e.tit && f >= e.tit.f0 && f < e.tit.f1) { const a = e.tit.g || 2; e.g.translate(new P.Point((hash(f, 3, 5) - 0.5) * a, (hash(f, 4, 6) - 0.5) * a)); }
    if (e.alfa) e.g.opacity = e.alfa(f);
  }
  async function kare(f) {
    if (typeof window !== "undefined" && window.__kalemKutu) {
      window.__kalemKutu.kare = [];
    }
    const fe = Math.min(f, SON);
    if (temaSurum() !== sonSurum) { sonSurum = temaSurum(); for (const c of CIZGILER) c.tam = false; }   // tema değişti: biten darbeler yeniden boyanır
    for (const c of CIZGILER) {
      const t = ilerle(c, fe);
      if (t <= 0) { if (c.yolP) { c.yolP.remove(); c.yolP = null; c.tam = false; } continue; }
      if (c.tam && t >= 1) continue;
      if (c.yolP) c.yolP.remove();
      c.yolP = cokgen(c, t);
      c.yolP.data = { kalemTur: c.tur, kalemAd: c.ad };
      c.og.g.addChild(c.yolP); c.tam = t >= 1;
    }
    for (const y of YAZILAR) yaziGuncelle(y, fe);
    for (const d of DINAMIK) d(fe);
    for (const e of OGELER) matrisUygula(e, fe);
    P.view.update();
    zeminCiz(oc, f, K); oc.drawImage(document.getElementById("cv"), 0, 0); kunyeCiz(oc, { bolum, etkin, logo: K.logo });
    if (f === KARE - 1) {
      const ev = [...OLAY.values()].sort((a, b) => a.kare - b.kare || b.guc - a.guc), say = {}, son = [];
      for (const e of ev) { if (e.kare > SON) continue; say[e.kare] = (say[e.kare] || 0) + 1; if (say[e.kare] <= 3) son.push(e); }   // son 12 kare durgun: olay yok
      await logGonder({ method: "POST", body: "OLAYLAR " + JSON.stringify(son) });
      ZAMAN.push({ ad: "DARBE toplam", kare: CIZGILER.length });
      await logGonder({ method: "POST", body: "ZAMANLAR " + JSON.stringify(ZAMAN) });
    }
    return out;
  }
  return { P, K, kalemGeo, cokgen, fr, not, olay, ciz, daire, egri, ok, kutu, tik, svgCiz, yazi, elYazisi, cumle, altCizgi, dinamik, parilti, sozcukler, oge, kok,
    kare, bitis, ilerle, genislik, hash, gurul, kis, yumus, cikis, lerp };
}

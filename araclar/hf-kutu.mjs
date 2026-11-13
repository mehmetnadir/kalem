// araclar/hf-kutu.mjs
// HyperFrames (DOM/SVG + GSAP) sahnelerinde yazı × çizim çakışması ölçümü (13.11).
// Canvas/Paper.js sahneleri kutuyu kendi kancasıyla (window.__kalemKutu) verir; HyperFrames sayfasına
// kanca gömülmez (sahne uret.py dosyaları değişmez). Bunun yerine cakisma-kapisi her örnek zamanda
// sahne-kare `--olc` ile HF_TOPLA_JS'yi sayfaya enjekte eder; sayfa HAM öğeleri döner, hfKutular()
// bunları cakisma-olcer.mjs şemasına çevirir ({tur, ad, x, y, w, h, muaf?}).
//
// Tür eşlemesi (cakisma-olcer ile aynı anlam):
//   yazi     <text>: tarayıcıda ölçülen mürekkep kutusu, clip-path (kalemle açılan kırpma) ile kesilmiş
//   cizim    yalnız çizgili şekil (path/rect/circle…): görünen uzunluğu boyunca ~14 px'lik parçalara bölünür
//            (köşegen ok/halka tek AABB ile yanlış alarm vermesin)
//            düz köşegen çizgi sözcüğün (16 px şişirilmiş) kutusunda kalıyorsa çarpıdır: o sözcük muaf
//   halka    küçük kapalı çizgi (işaret halkası, harf dairesi): içindeki hedef sözcük muaftır (kutusu
//            %75+ içeride, merkezi elipsin içinde; kenara yapışan komşu harf muaf değil)
//   altcizgi yassı açık çizgi: üstünde duran (en çok 24 px yakın) sözcük muaftır; iki altçizgi üst üste = hata
//            (aynı çizginin yeniden çizimi, yani yatayda %80+ örtüşen ve orta çizgisi kapanan çift, kasıtlıdır;
//            uç uca temas, yani örtüşme < 30 px, kasıtlıdır; sözcüğün orta bandındaki çizgi üstü çizilidir: muaf)
//   kart     dolgulu şekil (rozet, şık satırı, dolgu): üstündeki yazı kasıtlıdır
//   kunye    #kunye / #logo içindeki her şey
// Opaklık eşiği 0,5: geçiş sırasında çapraz solan çiftler (başlık → künye) kusur sayılmaz; kalıcı
// çakışma tam opaklıkta zaten örneklenir.

export const OPAK_ESIK = 0.5;
export const PARCA_PX = 14;

// Sayfada koşan ölçüm: JSON {W,H,og:[ham öğe]} döner. Koordinatlar #root (1920x1080) uzayındadır.
//   t: {k:"t",tag,grp,kn,op,x,y,w,h}   f: dolgulu şekil   i: görsel
//   s: {k:"s",tag,grp,kn,op,sw,p:[x0,y0,x1,y1,…]}  görünen uzunluk boyunca örneklenmiş nokta dizisi
export const HF_TOPLA_JS = `JSON.stringify((() => {
  const kok = document.getElementById("root"), sah = document.getElementById("sahne");
  if (!kok || !sah) return { W: 0, H: 0, og: [], hata: "root/sahne yok" };
  const W = +kok.dataset.width || 1920, H = +kok.dataset.height || 1080;
  const rr = kok.getBoundingClientRect(), sx = rr.width / W || 1, sy = rr.height / H || 1;
  const don = (m, x, y) => [((m.a * x + m.c * y + m.e) - rr.left) / sx, ((m.b * x + m.d * y + m.f) - rr.top) / sy];
  const kutu = (n) => { const xs = n.map((q) => q[0]), ys = n.map((q) => q[1]);
    const x = Math.min(...xs), y = Math.min(...ys);
    return { x, y, w: Math.max(...xs) - x, h: Math.max(...ys) - y }; };
  const kes = (a, b) => { const x = Math.max(a.x, b.x), y = Math.max(a.y, b.y);
    const w = Math.min(a.x + a.w, b.x + b.w) - x, h = Math.min(a.y + a.h, b.y + b.h) - y;
    return w > 0 && h > 0 ? { x, y, w, h } : null; };
  const GEN = new Set(["sahne", "icerik", "root", "balg"]);
  const etkin = (el) => { let o = 1;
    for (let e = el; e && e.nodeType === 1; e = e.parentNode) {
      const cs = getComputedStyle(e);
      if (cs.display === "none" || cs.visibility === "hidden") return 0;
      o *= parseFloat(cs.opacity); }
    return o; };
  const klipler = (el) => { const out = [];
    for (let e = el; e && e.nodeType === 1 && e !== sah.parentNode; e = e.parentNode) {
      const cp = e.getAttribute("clip-path"); if (!cp) continue;
      const mm = /url\\(#([^)]+)\\)/.exec(cp); if (!mm) continue;
      const c = document.getElementById(mm[1]), r = c && c.querySelector("rect"), M = e.getScreenCTM();
      if (!r || !M) continue;
      const x = +r.getAttribute("x"), y = +r.getAttribute("y"), w = +r.getAttribute("width"), h = +r.getAttribute("height");
      out.push(kutu([don(M, x, y), don(M, x + w, y), don(M, x, y + h), don(M, x + w, y + h)])); }
    return out; };
  const kirp = (b, el) => { let r = b; for (const k of klipler(el)) { r = r && kes(r, k); if (!r) return null; }
    return kes(r, { x: 0, y: 0, w: W, h: H }); };
  const grup = (el) => { for (let e = el.parentNode; e && e !== sah; e = e.parentNode)
      if (e.id && !GEN.has(e.id)) return e.id;
    return el.id || "oge"; };
  const kn = (el) => !!el.closest("#kunye, #logo");
  const cv = document.createElement("canvas").getContext("2d");
  const og = [];
  const yuvarla = (b) => ({ x: +b.x.toFixed(1), y: +b.y.toFixed(1), w: +b.w.toFixed(1), h: +b.h.toFixed(1) });
  for (const e of sah.querySelectorAll("*")) {
    if (e.closest("defs, clipPath, filter, mask, pattern, symbol")) continue;
    const tag = e.tagName.toLowerCase();
    if (!/^(text|path|rect|circle|ellipse|line|polyline|polygon|image)$/.test(tag)) continue;
    const op = etkin(e); if (!(op > 0.05)) continue;
    const M = e.getScreenCTM(); if (!M) continue;
    if (tag === "text") {
      let bb; try { bb = e.getBBox(); } catch (er) { continue; }
      if (!(bb.width > 0 && bb.height > 0)) continue;
      let top = bb.y, bot = bb.y + bb.height;
      const s = e.textContent || "";
      if (s.trim() && !e.querySelector("tspan[y], tspan[dy]")) {
        const cs = getComputedStyle(e);
        cv.font = cs.fontWeight + " " + cs.fontSize + " " + cs.fontFamily;
        const m = cv.measureText(s.trim()), by = e.getStartPositionOfChar(0).y;
        if (m.actualBoundingBoxAscent > 0) { top = by - m.actualBoundingBoxAscent; bot = by + Math.max(0, m.actualBoundingBoxDescent); }
      }
      const b = kirp(kutu([don(M, bb.x, top), don(M, bb.x + bb.width, top), don(M, bb.x, bot), don(M, bb.x + bb.width, bot)]), e);
      if (b) og.push({ k: "t", tag, grp: grup(e), kn: kn(e), op: +op.toFixed(2), ...yuvarla(b) });
      continue;
    }
    const cs = getComputedStyle(e);
    const bos = (v) => !v || v === "none" || /rgba\\(.*,\\s*0\\)$/.test(v);
    const doldur = !bos(cs.fill), cizgi = !bos(cs.stroke) && parseFloat(cs.strokeWidth) > 0;
    if (tag === "image" || (doldur && tag !== "line")) {
      let bb; try { bb = e.getBBox(); } catch (er) { continue; }
      if (!(bb.width > 0 && bb.height > 0)) continue;
      const b = kirp(kutu([don(M, bb.x, bb.y), don(M, bb.x + bb.width, bb.y), don(M, bb.x, bb.y + bb.height), don(M, bb.x + bb.width, bb.y + bb.height)]), e);
      if (b) og.push({ k: tag === "image" ? "i" : "f", tag, grp: grup(e), kn: kn(e), op: +op.toFixed(2), ...yuvarla(b) });
      continue;
    }
    if (!cizgi || typeof e.getTotalLength !== "function") continue;
    let L; try { L = e.getTotalLength(); } catch (er) { continue; }
    if (!(L > 0)) continue;
    const da = parseFloat(cs.strokeDasharray);
    let vis = L;
    if (isFinite(da) && da > 0) vis = Math.max(0, Math.min(L, da - (parseFloat(cs.strokeDashoffset) || 0)));
    if (!(vis > 0.5)) continue;
    const k = Math.sqrt(Math.abs(M.a * M.d - M.b * M.c)) / (sx || 1);
    const n = Math.min(300, Math.max(2, Math.ceil(vis * k / 10) + 1));
    const kl = klipler(e), p = [];
    for (let i = 0; i < n; i++) {
      const q = e.getPointAtLength(vis * i / (n - 1)), z = don(M, q.x, q.y);
      if (kl.every((c) => z[0] >= c.x && z[0] <= c.x + c.w && z[1] >= c.y && z[1] <= c.y + c.h))
        p.push(+z[0].toFixed(1), +z[1].toFixed(1));
    }
    if (p.length >= 2) og.push({ k: "s", tag, grp: grup(e), kn: kn(e), op: +op.toFixed(2), sw: +(parseFloat(cs.strokeWidth) * k).toFixed(1), p });
  }
  return { W, H, og };
})())`;

const kes = (a, b) => {
  const x = Math.max(a.x, b.x), y = Math.max(a.y, b.y);
  const w = Math.min(a.x + a.w, b.x + b.w) - x, h = Math.min(a.y + a.h, b.y + b.h) - y;
  return w > 0 && h > 0 ? { x, y, w, h } : null;
};
const alan = (b) => b.w * b.h;
const yuvarla = (b) => ({ x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.w), h: Math.round(b.h) });

/** Nokta dizisi [x0,y0,x1,y1,…] → {x,y,w,h} (pay: yarım çizgi kalınlığı). */
export function noktaKutusu(p, pay = 0) {
  let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
  for (let i = 0; i + 1 < p.length; i += 2) {
    x0 = Math.min(x0, p[i]); x1 = Math.max(x1, p[i]);
    y0 = Math.min(y0, p[i + 1]); y1 = Math.max(y1, p[i + 1]);
  }
  return { x: x0 - pay, y: y0 - pay, w: x1 - x0 + 2 * pay, h: y1 - y0 + 2 * pay };
}

/**
 * Çizgi türü: 'altcizgi' (yassı açık çizgi) | 'halka' (küçük kapalı çizgi) | 'cizim'.
 * Büyük kapalı çerçeve (kart kenarı) ve ikon yolları 'cizim' kalır, muaf listesi almaz.
 */
export function cizgiTuru(p, sw = 4) {
  const b = noktaKutusu(p, 0);
  const ilk = [p[0], p[1]], son = [p[p.length - 2], p[p.length - 1]];
  const uc = Math.hypot(ilk[0] - son[0], ilk[1] - son[1]);
  const buyuk = Math.max(b.w, b.h);
  const kapali = buyuk > 0 && uc <= 0.4 * buyuk;
  // Çizilmekte olan halka henüz kapanmamıştır: kordon / yay uzunluğu <= 0,7 olan güçlü eğri yay da halkadır
  // (düz ok ve çizgi ~1, tik işareti ~0,71'de kalır ve zaten içinde sözcük taşımaz).
  const egri = yayOrani(p) <= 0.7;
  if (!kapali && b.h <= Math.max(2 * sw, 14) && b.w >= 3 * Math.max(b.h, sw)) return "altcizgi";
  if ((kapali || egri) && b.w >= 24 && b.h >= 24 && buyuk <= 560 && b.h <= 260) return "halka";
  return "cizim";
}

/** Kordon uzunluğu / yay uzunluğu (düz çizgi 1, kapalı halka 0'a yakın). */
export function yayOrani(p) {
  let uz = 0;
  for (let i = 2; i + 1 < p.length; i += 2) uz += Math.hypot(p[i] - p[i - 2], p[i + 1] - p[i - 1]);
  if (!(uz > 0)) return 1;
  return Math.hypot(p[p.length - 2] - p[0], p[p.length - 1] - p[1]) / uz;
}

/** Noktaları ~parca px'lik yollara böler; her parçanın kutusu çizgi kalınlığı kadar şişirilir. */
export function parcala(p, sw = 4, parca = PARCA_PX) {
  const pay = Math.max(1, sw / 2);
  const kutular = [];
  let bas = 0, uz = 0;
  for (let i = 2; i + 1 < p.length; i += 2) {
    uz += Math.hypot(p[i] - p[i - 2], p[i + 1] - p[i - 1]);
    if (uz >= parca || i + 2 >= p.length) {
      kutular.push(noktaKutusu(p.slice(bas, i + 2), pay));
      bas = i;
      uz = 0;
    }
  }
  if (!kutular.length) kutular.push(noktaKutusu(p, pay));
  return kutular;
}

/** Aynı gruptaki öğelere ayırt edici ad verir: grup tek öğeyse grup adı, çoksa grup:tagN. */
export function adlandir(ogeler) {
  const sayac = new Map(), sira = new Map();
  for (const o of ogeler) sayac.set(o.grp, (sayac.get(o.grp) || 0) + 1);
  for (const o of ogeler) {
    const anahtar = o.grp + ":" + o.tag;
    const n = sira.get(anahtar) || 0;
    sira.set(anahtar, n + 1);
    const ad = sayac.get(o.grp) > 1 ? `${o.grp}:${o.tag}${n}` : o.grp;
    o.ad = o.kn ? "kunye:" + ad : ad;
  }
  return ogeler;
}

/**
 * Ham öğeleri cakisma-olcer şemasına çevirir.
 * @param {{og: Array}} ham HF_TOPLA_JS çıktısı
 * @returns {Array} [{tur, ad, x, y, w, h, muaf?}]
 */
export function hfKutular(ham, { opakEsik = OPAK_ESIK, parca = PARCA_PX } = {}) {
  const ogeler = adlandir((ham?.og || []).filter((o) => o.op >= opakEsik));
  const kutular = [];
  const yazilar = [];
  const cizgiler = [];

  for (const o of ogeler) {
    if (o.k === "s") continue;
    if (o.w <= 0 || o.h <= 0) continue;
    const tur = o.kn ? "kunye" : o.k === "t" ? "yazi" : o.k === "f" ? "kart" : "cizim";
    const kt = { tur, ad: o.ad, ...yuvarla(o) };
    if (kt.w <= 0 || kt.h <= 0) continue;
    kutular.push(kt);
    if (tur === "yazi") yazilar.push(kt);
  }

  for (const o of ogeler) {
    if (o.k !== "s" || !o.p || o.p.length < 4) continue;
    if (o.kn) {
      const b = yuvarla(noktaKutusu(o.p, Math.max(1, o.sw / 2)));
      if (b.w > 0 && b.h > 0) kutular.push({ tur: "kunye", ad: o.ad, ...b });
      continue;
    }
    const tur = cizgiTuru(o.p, o.sw);
    const govde = noktaKutusu(o.p, 0);
    const muaf = [];
    for (const y of yazilar) {
      if (tur === "halka") {
        // hedef sözcük halkanın içinde durur: kutusu %75+ içeride ve merkezi elipsin içinde (halkanın kenarına
        // yapışan komşu harf, örneğin sağ ya da sol uçtaki "I", hedef sayılmaz)
        const k = kes(y, govde);
        const dx = (y.x + y.w / 2 - (govde.x + govde.w / 2)) / (govde.w / 2);
        const dy = (y.y + y.h / 2 - (govde.y + govde.h / 2)) / (govde.h / 2);
        if (k && alan(k) >= 0.75 * alan(y) && dx * dx + dy * dy <= 0.85 * 0.85) muaf.push(y.ad);
      } else if (tur === "altcizgi") {
        const k = kes({ x: y.x, y: -1e6, w: y.w, h: 2e6 }, { x: govde.x, y: -1e6, w: govde.w, h: 2e6 });
        const yatay = k ? k.w / Math.min(y.w, govde.w) : 0;
        // üstü çizili: çizgi sözcüğün orta bandında yatay duruyor ve x aralığı sözcüğün içinde (±16 px)
        const orta = govde.y + govde.h / 2;
        if (orta >= y.y + 0.35 * y.h && orta <= y.y + 0.75 * y.h && govde.x >= y.x - 16
            && govde.x + govde.w <= y.x + y.w + 16) { muaf.push(y.ad); continue; }
        // çizgi sözcüğün alt yarısında ya da hemen altında durur (en çok 24 px aşağıda)
        const merkez = govde.y + govde.h / 2;
        const altinda = merkez >= y.y + y.h / 2 && merkez <= y.y + y.h + 24;
        if (yatay >= 0.4 && altinda) muaf.push(y.ad);
      }
    }
    if (tur === "cizim" && duzCapraz(o.p, govde)) {
      // çarpı (üstünü çizme): düz köşegen çizgi bir sözcüğün (16 px şişirilmiş) kutusunun içinde kalır
      for (const y of yazilar) {
        if (icinde16(govde, y)) muaf.push(y.ad);
      }
    }
    cizgiler.push({ o, tur, govde, muaf });
  }

  // Aynı çizginin yeniden çizilmesi kasıtlıdır (boşluk çizgisi altta, vurgusu ve dolgusu aynı yolda üstte):
  // iki altçizgi yatayda büyük ölçüde örtüşüyor ve biri ötekinin orta çizgisini kapatıyorsa karşılıklı muaf.
  const ust = cizgiler.filter((c) => c.tur === "altcizgi");
  for (let i = 0; i < ust.length; i++) {
    for (let j = i + 1; j < ust.length; j++) {
      if (ustuste(ust[i], ust[j]) || ucUca(ust[i], ust[j])) {
        ust[i].muaf.push(ust[j].o.ad);
        ust[j].muaf.push(ust[i].o.ad);
      }
    }
  }

  for (const { o, tur, muaf } of cizgiler) {
    for (const b of parcala(o.p, o.sw, parca)) {
      const kt = { tur, ad: o.ad, ...yuvarla(b) };
      if (kt.w <= 0 || kt.h <= 0) continue;
      if (muaf.length) kt.muaf = muaf;
      kutular.push(kt);
    }
  }
  return kutular;
}

// Düz (kıvrımsız) ve köşegen (iki boyutu >= 10 px) çizgi mi? Çarpı çizgileri böyledir.
export function duzCapraz(p, govde = noktaKutusu(p, 0)) {
  let uz = 0;
  for (let i = 2; i + 1 < p.length; i += 2) uz += Math.hypot(p[i] - p[i - 2], p[i + 1] - p[i - 1]);
  const kiris = Math.hypot(p[p.length - 2] - p[0], p[p.length - 1] - p[1]);
  return uz > 0 && kiris / uz >= 0.97 && govde.w >= 10 && govde.h >= 10;
}

// Çizgi kutusu, sözcük kutusunun 16 px şişirilmişinin içinde mi?
function icinde16(c, y, pay = 16) {
  return c.x >= y.x - pay && c.y >= y.y - pay && c.x + c.w <= y.x + y.w + pay && c.y + c.h <= y.y + y.h + pay;
}

// İki altçizgi uç uca mı? (yatay örtüşme < 30 px ve kısa olanın %25'i: çizgi + ok ucu devamı)
export function ucUca(a, b) {
  const yatay = Math.min(a.govde.x + a.govde.w, b.govde.x + b.govde.w) - Math.max(a.govde.x, b.govde.x);
  return yatay < Math.max(30, 0.25 * Math.min(a.govde.w, b.govde.w));
}

// İki altçizgi aynı çizginin üst üste çizimi mi? (yatay örtüşme >= %80, orta çizgiler <= yarım kalınlık + 2 px)
export function ustuste(a, b) {
  const yatay = Math.min(a.govde.x + a.govde.w, b.govde.x + b.govde.w) - Math.max(a.govde.x, b.govde.x);
  if (yatay < 0.8 * Math.min(a.govde.w, b.govde.w)) return false;
  const fark = Math.abs(a.govde.y + a.govde.h / 2 - (b.govde.y + b.govde.h / 2));
  return fark <= Math.max(a.o.sw, b.o.sw) / 2 + 2;
}

// Ortak künye (HUD) + zemin — her sahnede aynı px'ler. Paper.js ve düz canvas sahneleri bunu çağırır;
// HyperFrames sahneleri aynı sayıları HTML/CSS ile uygular (BRIEF.md §3 tablosu).
// Kullanım: const K = await kunyeHazirla(); ... zeminCiz(ctx, f); ... kunyeCiz(ctx, { bolum: "Hook", etkin: 0, logo: K.logo });
export const KOK = "/projeler/deneme-doku/ortak";
export const TEMALAR = {
  koyu: { zemin: "#1b1a17", murekkep: "#f3efe6", ikincil: "#c9c2b3", vurgu: "#f2a93b", vurguDolgu: "#f2a93b",
    logoSari: "#fece00", logoMetin: "#ffffff", kirmizi: "#e0473b" },
  acik: { zemin: "#f7f3ea", murekkep: "#1b2440", ikincil: "#5a6275", vurgu: "#d9900f", vurguDolgu: "#ffe066",
    logoSari: "#fece00", logoMetin: "#13204D", kirmizi: "#d6453a" } };
// Canlı renk nesnesi: temaSec() alanları yerinde değiştirir; çizim anında RENK.x okunur.
export const RENK = { ...TEMALAR.koyu };
// Renk adı belirteçleri ("@vurgu"): kur() anında saklanır, çizim anında renkCoz() ile RENK'ten çözülür (tema sonradan değişebilir).
export const RT = Object.fromEntries(Object.keys(TEMALAR.koyu).map((a) => [a, "@" + a]));
export const renkCoz = (r) => (typeof r === "string" && r[0] === "@" ? RENK[r.slice(1)] : r);
let temaAd = "koyu", surum = 0;
export const temaAdi = () => temaAd;
export const temaSurum = () => surum;                              // her tema değişiminde artar (önbellekli çizimler yenilensin)
// kraft zemininde marka turuncusu okunmaz (06.11 Nadir: sarı metinler neredeyse okunmuyor; 1,6:1).
// kraft'a özel koyu vurgu ve ikincil (kontrast.py ile ölçüldü: #5c2e00 4,7:1 · #2b3040 5,1:1).
const KRAFT_RENK = { acik: { vurgu: "#5c2e00", ikincil: "#2b3040" }, koyu: {} };
const dokuErken = () => (typeof window !== "undefined" && window.DOKU) || "kagit";
export function temaSec(ad) {
  if (!TEMALAR[ad] || ad === temaAd) return; temaAd = ad; surum++; Object.assign(RENK, TEMALAR[ad]);
  if (dokuErken() === "kraft") Object.assign(RENK, KRAFT_RENK[ad]);
}
try { temaSec(new URLSearchParams(location.search).get("tema") || "koyu");
  if (dokuErken() === "kraft") Object.assign(RENK, KRAFT_RENK[temaAd]);
} catch (e) { /* tarayıcı dışı */ }
export const KUNYE = { kenar: 56, ustTaban: 72, altTaban: 1030, logoYuk: 34, dersYazi: 30, seviyeYazi: 22,
  bolumYazi: 24, ajandaYazi: 20, ders: "SIMPLE PRESENT", seviye: "YDT ADVANCED", ajanda: ["Hook", "Examples", "Form"] };
const W = 1920, H = 1080;

const FONTLAR = [["Fredoka", "fredoka-latin-700-normal.woff2", 700], ["Fredoka", "fredoka-latin-ext-700-normal.woff2", 700],
  ["Fredoka", "fredoka-latin-600-normal.woff2", 600], ["Lexend", "lexend-latin-500-normal.woff2", 500],
  ["Lexend", "lexend-latin-ext-500-normal.woff2", 500], ["Lexend", "lexend-latin-700-normal.woff2", 700],
  ["Lexend", "lexend-latin-ext-700-normal.woff2", 700], ["Caveat", "caveat-latin-700-normal.woff2", 700],
  ["Caveat", "caveat-latin-ext-700-normal.woff2", 700]];

let dinleyici = false;
export async function kunyeHazirla() {
  if (!dinleyici && typeof addEventListener === "function") {      // önizleme: {tip:"tema", ad} ile yeniden yüklemeden değişir
    dinleyici = true; addEventListener("message", (e) => { if (e.data && e.data.tip === "tema") temaSec(e.data.ad); });
  }
  for (const [ad, dosya, agirlik] of FONTLAR) {
    const f = new FontFace(ad, `url(${KOK}/font/${dosya})`, { weight: String(agirlik) });
    await f.load(); document.fonts.add(f);
  }
  const yukle = (ad) => new Promise((ok, hata) => {
    const im = new Image(); im.onload = () => ok(im); im.onerror = hata; im.src = `${KOK}/logo/${ad}`;
  });
  const [koyuLogo, acikLogo] = [await yukle("yds-publishing-seffaf.svg"), await yukle("yds-publishing-lacivert.svg")];
  return { get logo() { return temaAd === "acik" ? acikLogo : koyuLogo; }, grenler: grenUret() };
}

// Gren: 3 tohumlu 512 px karo; kare numarasıyla karo ve kayma değişir (yaşayan gren), rastgele yok.
function grenUret() {
  const hash = (a, b, c) => { let h = (Math.imul(a | 0, 374761393) + Math.imul(b | 0, 668265263) +
    Math.imul(c | 0, 1274126177)) | 0; h = Math.imul(h ^ (h >>> 13), 1274126177); h ^= h >>> 16; return (h >>> 0) / 4294967296; };
  return [0, 1, 2].map((s) => {
    const c = document.createElement("canvas"); c.width = c.height = 512; const x = c.getContext("2d");
    const d = x.createImageData(512, 512);
    for (let i = 0; i < 512 * 512; i++) { const v = 128 + Math.round((hash(i % 512, i / 512 | 0, s) - 0.5) * 255);
      d.data[i * 4] = d.data[i * 4 + 1] = d.data[i * 4 + 2] = v; d.data[i * 4 + 3] = 255; }
    x.putImageData(d, 0, 0); return c;
  });
}

// ---------- doku rotasyonu (deneme 5): window.DOKU || 'kagit'; sayfa.html ?doku= geçirir ----
// Üç yeni doku tohumlu ve kareden bağımsızdır (titremez); bir kez çizilip önbelleğe alınır.
const DOKU_AD = (typeof window !== "undefined" && window.DOKU) || "kagit";
export const dokuAdi = () => DOKU_AD;
export const KRAFT = { acik: "#c2a278", koyu: "#3d3024" };      // kraft zemin tonu (tema başına)
const tohumlu = (s) => () => {
  s = (s + 0x6D2B79F5) | 0; let t = Math.imul(s ^ (s >>> 15), 1 | s);
  t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
};
let dokuKatman = null, dokuSurum = -1;

function dokuUret(K) {
  const c = document.createElement("canvas"); c.width = W; c.height = H;
  const x = c.getContext("2d");
  const acik = temaAd === "acik", PI2 = Math.PI * 2;
  const r = tohumlu(DOKU_AD === "riso" ? 11 : DOKU_AD === "kraft" ? 23 : 37);
  x.fillStyle = DOKU_AD === "kraft" ? KRAFT[temaAd] : RENK.zemin; x.fillRect(0, 0, W, H);
  if (DOKU_AD === "riso") {
    // iki renk baskı: A = mürekkep (çerçeve + daire), B = vurgu (aynı şekil, +1,5 px kayık)
    if (K && K.grenler) {
      x.globalAlpha = acik ? 0.05 : 0.06; x.globalCompositeOperation = "overlay";
      for (let y = 0; y < H; y += 512) {
        for (let xx = 0; xx < W; xx += 512) x.drawImage(K.grenler[0], xx, y);
      }
    }
    x.globalAlpha = 1; x.globalCompositeOperation = "source-over";
    const sekil = (ctx) => {
      ctx.beginPath(); ctx.rect(22, 22, W - 44, H - 44); ctx.moveTo(1960, 180);
      ctx.arc(1700, 180, 260, 0, PI2);
    };
    x.save(); x.translate(1.5, 1.5); x.globalAlpha = acik ? 0.16 : 0.2;
    x.strokeStyle = RENK.vurgu; x.lineWidth = 2.5; sekil(x); x.stroke();
    x.beginPath(); x.arc(1700, 180, 260, 0, PI2);
    x.globalAlpha = 0.07; x.fillStyle = RENK.vurgu; x.fill();
    x.restore();
    x.save(); x.globalAlpha = acik ? 0.12 : 0.14; x.strokeStyle = RENK.murekkep; x.lineWidth = 2.5;
    sekil(x); x.stroke(); x.restore();
    x.fillStyle = RENK.murekkep; x.globalAlpha = 0.08;           // mürekkep benekleri
    for (let i = 0; i < 2200; i++) {
      x.beginPath(); x.arc(r() * W, r() * H, 0.5 + r() * 0.8, 0, PI2); x.fill();
    }
  } else if (DOKU_AD === "yarimton") {
    // ışık sol üstten düşer: nokta yarıçapı sağ alta (gölge tarafı) doğru büyür; aydınlık yarı boş
    const s = 21;                                                // 45° ızgara, aralık ≈ 30 px
    x.fillStyle = RENK.murekkep; x.globalAlpha = 0.1;
    for (let i = -50; i <= 50; i++) for (let j = -50; j <= 50; j++) {
      const px = W / 2 + (i - j) * s, py = H / 2 + (i + j) * s;
      if (px < 0 || px > W || py < 0 || py > H) continue;
      const t = (px * W + py * H) / (W * W + H * H);             // ışık ekseni boyunca 0..1
      if (t < 0.4) continue;                                     // seyrek: aydınlık taraf boş
      x.beginPath(); x.arc(px, py, 1 + 4.2 * (t - 0.4) / 0.6, 0, PI2); x.fill();
    }
  } else if (DOKU_AD === "kraft") {
    // lif dokusu: kısa, hafif eğri tohumlu çizgiler (koyu ve açık lif karışık)
    x.lineCap = "round";
    for (let i = 0; i < 1800; i++) {
      const px = r() * W, py = r() * H, a = r() * Math.PI, l = 18 + r() * 60, e = (r() - 0.5) * 0.9;
      const koyuLif = r() < 0.6, co = Math.cos(a), si = Math.sin(a);
      x.strokeStyle = koyuLif ? (acik ? "#5a4026" : "#000000") : (acik ? "#e6cfa8" : "#8a6c48");
      x.globalAlpha = 0.05 + r() * 0.09; x.lineWidth = 0.6 + r() * 1.0;
      x.beginPath(); x.moveTo(px, py);
      x.quadraticCurveTo(px + Math.cos(a + e) * l * 0.5, py + Math.sin(a + e) * l * 0.5,
        px + co * l, py + si * l);
      x.stroke();
    }
    x.globalAlpha = 0.5;                                         // geniş lekeler (bulutlu ton)
    for (let i = 0; i < 40; i++) {
      const px = r() * W, py = r() * H, rr = 120 + r() * 220;
      const g = x.createRadialGradient(px, py, 0, px, py, rr);
      g.addColorStop(0, r() < 0.5 ? "rgba(60,38,16,0.05)" : "rgba(255,235,200,0.05)");
      g.addColorStop(1, "rgba(0,0,0,0)"); x.fillStyle = g;
      x.fillRect(px - rr, py - rr, rr * 2, rr * 2);
    }
  }
  return c;
}

export function zeminCiz(ctx, f, K) {
  ctx.save(); ctx.globalCompositeOperation = "source-over"; ctx.globalAlpha = 1;
  if (DOKU_AD === "kagit") {
    ctx.fillStyle = RENK.zemin; ctx.fillRect(0, 0, W, H);
    if (K && K.grenler) {
      ctx.globalAlpha = temaAd === "acik" ? 0.03 : 0.045; ctx.globalCompositeOperation = "overlay";
      const g = K.grenler[f % 3], ox = (f * 97) % 512, oy = (f * 61) % 512;
      for (let y = -oy; y < H; y += 512) for (let x = -ox; x < W; x += 512) ctx.drawImage(g, x, y);
    }
  } else {
    if (!dokuKatman || dokuSurum !== surum) { dokuKatman = dokuUret(K); dokuSurum = surum; }
    ctx.drawImage(dokuKatman, 0, 0);
  }
  ctx.globalAlpha = 1; ctx.globalCompositeOperation = "source-over";
  const v = ctx.createRadialGradient(W / 2, H / 2, H * 0.45, W / 2, H / 2, H * 0.95);
  v.addColorStop(0, "rgba(0,0,0,0)"); v.addColorStop(1, temaAd === "acik" ? "rgba(0,0,0,0.10)" : "rgba(0,0,0,0.38)");
  ctx.fillStyle = v; ctx.fillRect(0, 0, W, H); ctx.restore();
}

// bolum: sağ üst metin ("Hook", "Example 1 / 3", "Question", "Form") · etkin: ajanda dizini 0/1/2 · alfa: 0–1 (giriş uçuşu için)
export function kunyeCiz(ctx, { bolum, etkin = 0, logo, alfa = 1 }) {
  const k = KUNYE, R = RENK; ctx.save(); ctx.globalAlpha = alfa; ctx.textBaseline = "alphabetic";
  ctx.textAlign = "left"; ctx.fillStyle = R.murekkep; ctx.font = `700 ${k.dersYazi}px Fredoka`;
  ctx.fillText(k.ders, k.kenar, k.ustTaban);
  const dw = ctx.measureText(k.ders).width;
  ctx.fillStyle = R.ikincil; ctx.font = `500 ${k.seviyeYazi}px Lexend`; ctx.fillText(`· ${k.seviye}`, k.kenar + dw + 14, k.ustTaban);
  ctx.textAlign = "right"; ctx.fillStyle = R.vurgu; ctx.font = `700 ${k.bolumYazi}px Lexend`;
  ctx.fillText(bolum || "", W - k.kenar, k.ustTaban);
  if (logo) { const h = k.logoYuk, w = h * 1920 / 476.3; ctx.drawImage(logo, k.kenar, H - 44 - h, w, h); }
  ctx.font = `500 ${k.ajandaYazi}px Lexend`; let x = W - k.kenar;
  for (let i = k.ajanda.length - 1; i >= 0; i--) {
    const ad = k.ajanda[i], w = ctx.measureText(ad).width;
    ctx.fillStyle = i === etkin ? R.vurgu : R.ikincil; ctx.fillText(ad, x, k.altTaban);
    if (i === etkin) { ctx.beginPath(); ctx.arc(x - w - 12, k.altTaban - 7, 4, 0, Math.PI * 2); ctx.fill(); }
    x -= w + 36;
  }
  ctx.restore();
}

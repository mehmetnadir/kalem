// Ortak künye (HUD) + zemin — her sahnede aynı px'ler. Paper.js ve düz canvas sahneleri bunu çağırır;
// HyperFrames sahneleri aynı sayıları HTML/CSS ile uygular (BRIEF.md §3 tablosu).
// Kullanım: const K = await kunyeHazirla(); ... zeminCiz(ctx, f); ... kunyeCiz(ctx, { bolum: "Hook", etkin: 0, logo: K.logo });
export const KOK = "/projeler/deneme-metro/ortak";
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
export function temaSec(ad) {
  if (!TEMALAR[ad] || ad === temaAd) return; temaAd = ad; surum++; Object.assign(RENK, TEMALAR[ad]);
}
try { temaSec(new URLSearchParams(location.search).get("tema") || "koyu"); } catch (e) { /* tarayıcı dışı */ }
export const KUNYE = { kenar: 56, ustTaban: 72, altTaban: 1030, logoYuk: 34, dersYazi: 30, seviyeYazi: 22,
  bolumYazi: 24, ajandaYazi: 20, ders: "PRESENT PERFECT", seviye: "YDT BASIC", ajanda: ["Hook", "Examples", "Form"] };
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

export function zeminCiz(ctx, f, K) {
  ctx.save(); ctx.globalCompositeOperation = "source-over"; ctx.globalAlpha = 1;
  ctx.fillStyle = RENK.zemin; ctx.fillRect(0, 0, W, H);
  if (K && K.grenler) {
    ctx.globalAlpha = temaAd === "acik" ? 0.03 : 0.045; ctx.globalCompositeOperation = "overlay";
    const g = K.grenler[f % 3], ox = (f * 97) % 512, oy = (f * 61) % 512;
    for (let y = -oy; y < H; y += 512) for (let x = -ox; x < W; x += 512) ctx.drawImage(g, x, y);
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

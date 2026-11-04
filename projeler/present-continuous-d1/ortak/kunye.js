// Ortak künye (HUD) + zemin — DİKEY 1080x1920 sürüm (D1). Paper.js ve düz canvas sahneleri bunu çağırır;
// HyperFrames sahneleri aynı sayıları HTML/CSS ile uygular (BRIEF-D1.md §3).
// Kullanım: const K = await kunyeHazirla(); ... zeminCiz(ctx, f, K); ... kunyeCiz(ctx, { bolum: "Hook", logo: K.logo });
export const KOK = "/projeler/present-continuous-d1/ortak";
export const TEMALAR = {
  koyu: { zemin: "#1b1a17", murekkep: "#f3efe6", ikincil: "#c9c2b3", vurgu: "#f2a93b", vurguDolgu: "#f2a93b",
    logoSari: "#fece00", logoMetin: "#ffffff", kirmizi: "#e0473b", pilMetin: "#1b1a17" },
  acik: { zemin: "#f7f3ea", murekkep: "#1b2440", ikincil: "#5a6275", vurgu: "#d9900f", vurguDolgu: "#ffe066",
    logoSari: "#fece00", logoMetin: "#13204D", kirmizi: "#d6453a", pilMetin: "#1b2440" } };
export const RENK = { ...TEMALAR.koyu };
export const RT = Object.fromEntries(Object.keys(TEMALAR.koyu).map((a) => [a, "@" + a]));
export const renkCoz = (r) => (typeof r === "string" && r[0] === "@" ? RENK[r.slice(1)] : r);
let temaAd = "koyu", surum = 0;
export const temaAdi = () => temaAd;
export const temaSurum = () => surum;
export function temaSec(ad) {
  if (!TEMALAR[ad] || ad === temaAd) return; temaAd = ad; surum++; Object.assign(RENK, TEMALAR[ad]);
}
try { temaSec(new URLSearchParams(location.search).get("tema") || "koyu"); } catch (e) { /* tarayıcı dışı */ }
// Dikey HUD (y 0-288): ders adı, rozet, "şu an" çipi; logo sol alt (y 1464-1512); y 1536-1920 platform bandı BOŞ.
export const KUNYE = { kenar: 48, dersTaban: 104, dersYazi: 36, rozetY: 136, rozetH: 46, rozetYazi: 24,
  cipY: 62, cipH: 48, cipYazi: 26, logoY: 1464, logoYuk: 48, ders: "PRESENT CONTINUOUS", rozet: "YDT · BASIC" };
const W = 1080, H = 1920;
export const GEN = W, YUK = H;

const FONTLAR = [["Fredoka", "fredoka-latin-700-normal.woff2", 700], ["Fredoka", "fredoka-latin-ext-700-normal.woff2", 700],
  ["Fredoka", "fredoka-latin-600-normal.woff2", 600], ["Lexend", "lexend-latin-500-normal.woff2", 500],
  ["Lexend", "lexend-latin-ext-500-normal.woff2", 500], ["Lexend", "lexend-latin-700-normal.woff2", 700],
  ["Lexend", "lexend-latin-ext-700-normal.woff2", 700], ["Caveat", "caveat-latin-700-normal.woff2", 700],
  ["Caveat", "caveat-latin-ext-700-normal.woff2", 700]];

let dinleyici = false;
export async function kunyeHazirla() {
  if (!dinleyici && typeof addEventListener === "function") {
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

// bolum: sağ üst "şu an" çipi ("Hook", "Examples", "Form") · alfa: 0–1
export function kunyeCiz(ctx, { bolum, logo, alfa = 1 }) {
  const k = KUNYE, R = RENK; ctx.save(); ctx.globalAlpha = alfa; ctx.textBaseline = "alphabetic"; ctx.textAlign = "left";
  ctx.fillStyle = R.murekkep; ctx.font = `700 ${k.dersYazi}px Fredoka`; ctx.fillText(k.ders, k.kenar, k.dersTaban);
  // rozet hapı
  ctx.font = `700 ${k.rozetYazi}px Lexend`; const rw = ctx.measureText(k.rozet).width + 44;
  ctx.fillStyle = R.vurguDolgu; ctx.beginPath(); ctx.roundRect(k.kenar, k.rozetY, rw, k.rozetH, k.rozetH / 2); ctx.fill();
  ctx.fillStyle = R.pilMetin; ctx.textAlign = "center"; ctx.fillText(k.rozet, k.kenar + rw / 2, k.rozetY + k.rozetH / 2 + 8.5);
  // şu an çipi
  if (bolum) {
    ctx.font = `700 ${k.cipYazi}px Lexend`; const cw = ctx.measureText(bolum).width + 44, cx = W - k.kenar - cw;
    ctx.strokeStyle = R.vurgu; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.roundRect(cx, k.cipY, cw, k.cipH, k.cipH / 2); ctx.stroke();
    ctx.fillStyle = R.vurgu; ctx.fillText(bolum, cx + cw / 2, k.cipY + k.cipH / 2 + 9.3);
  }
  if (logo) { const h = k.logoYuk, w = h * 1920 / 476.3; ctx.drawImage(logo, k.kenar, k.logoY, w, h); }
  ctx.restore();
}

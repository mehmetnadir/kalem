// Ortak künye (HUD) + zemin — her sahnede aynı px'ler. Paper.js ve düz canvas sahneleri bunu çağırır;
// HyperFrames sahneleri aynı sayıları HTML/CSS ile uygular (BRIEF.md §3 tablosu).
// Kullanım: const K = await kunyeHazirla(); ... zeminCiz(ctx, f); ... kunyeCiz(ctx, { bolum: "Hook", etkin: 0, logo: K.logo });
export const KOK = "/projeler/present-continuous/ortak";
export const TEMALAR = {
  koyu: { zemin: "#1b1a17", murekkep: "#f3efe6", ikincil: "#c9c2b3", vurgu: "#f2a93b", vurguDolgu: "#f2a93b",
    logoSari: "#fece00", logoMetin: "#ffffff", kirmizi: "#e0473b" },
  acik: { zemin: "#f7f3ea", murekkep: "#1b2440", ikincil: "#5a6275", vurgu: "#d9900f", vurguDolgu: "#ffe066",
    logoSari: "#fece00", logoMetin: "#13204D", kirmizi: "#d6453a" } };
// Canlı renk nesnesi: temaSec() alanları yerinde değiştirir; çizim anında RENK.x okunur.
export const RENK = { ...TEMALAR.koyu };

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
  bolumYazi: 24, ajandaYazi: 20, ders: "PRESENT CONTINUOUS", seviye: "YDT BASIC", ajanda: ["Hook", "Examples", "Form"] };
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

// Zemin önbelleği (10.11, P2-3, Nadir: "zemin değişimi oranımız çok düşük"): zemin kareden kareye
// değişmez, yalnız gren karosu kayar. Zemin rengi düz olduğundan "zemin ⊕ gren overlay" sonucu tema
// başına 3 karoda (zeminKaroAl), vinyet gradyanı tema başına 1 gizli tuvalde (vinyetAl) bir kez
// hesaplanır; karede 15 düz karo kopyası + 1 vinyet kopyası kalır. Ölçüm (tam tuval, kısmasız):
// zemin 9,7 → 1,6 ms/kare (yatay ve dikey); eski algoritmaya karşı piksel farkı en çok 1/255.
export function zeminCiz(ctx, f, K) {
  ctx.save(); ctx.globalCompositeOperation = "source-over"; ctx.globalAlpha = 1;
  if (K && K.grenler) {
    const g = zeminKaroAl(K)[f % 3], ox = (f * 97) % 512, oy = (f * 61) % 512;
    for (let y = -oy; y < H; y += 512) for (let x = -ox; x < W; x += 512) ctx.drawImage(g, x, y);
  } else { ctx.fillStyle = RENK.zemin; ctx.fillRect(0, 0, W, H); }
  ctx.drawImage(vinyetAl(), 0, 0); ctx.restore();
}

function zeminKaroAl(K) {
  if (K.zeminKaro && K.zeminKaro.surum === surum) return K.zeminKaro.karolar;
  const karolar = K.grenler.map((g) => {
    const c = document.createElement("canvas"); c.width = c.height = 512;
    const x = c.getContext("2d");
    x.fillStyle = RENK.zemin; x.fillRect(0, 0, 512, 512);
    x.globalAlpha = temaAd === "acik" ? 0.03 : 0.045; x.globalCompositeOperation = "overlay";
    x.drawImage(g, 0, 0); return c;
  });
  K.zeminKaro = { surum, karolar }; return karolar;
}

let vinyet = null, vinyetSurum = -1;
function vinyetAl() {
  if (vinyet && vinyetSurum === surum) return vinyet;
  const c = document.createElement("canvas"); c.width = W; c.height = H;
  const x = c.getContext("2d");
  const v = x.createRadialGradient(W / 2, H / 2, H * 0.45, W / 2, H / 2, H * 0.95);
  v.addColorStop(0, "rgba(0,0,0,0)");
  v.addColorStop(1, temaAd === "acik" ? "rgba(0,0,0,0.10)" : "rgba(0,0,0,0.38)");
  x.fillStyle = v; x.fillRect(0, 0, W, H); vinyet = c; vinyetSurum = surum; return c;
}


// bolum: sağ üst metin ("Hook", "Example 1 / 3", "Question", "Form") · etkin: ajanda dizini 0/1/2 · alfa: 0–1 (giriş uçuşu için)
export function kunyeCiz(ctx, { bolum, etkin = 0, logo, alfa = 1 }) {
  const k = KUNYE, R = RENK; ctx.save(); ctx.globalAlpha = alfa; ctx.textBaseline = "alphabetic";
  ctx.textAlign = "left"; ctx.fillStyle = R.murekkep; ctx.font = `700 ${k.dersYazi}px Fredoka`;
  ctx.fillText(k.ders, k.kenar, k.ustTaban);
  const dw = ctx.measureText(k.ders).width;
  ctx.fillStyle = R.ikincil; ctx.font = `500 ${k.seviyeYazi}px Lexend`; ctx.fillText(`· ${k.seviye}`, k.kenar + dw + 14, k.ustTaban);
  const sw = ctx.measureText(`· ${k.seviye}`).width;
  ctx.textAlign = "right"; ctx.fillStyle = R.vurgu; ctx.font = `700 ${k.bolumYazi}px Lexend`;
  ctx.fillText(bolum || "", W - k.kenar, k.ustTaban);
  const bw = bolum ? ctx.measureText(bolum).width : 0;
  let logoW = 0, logoH = 0;
  if (logo) { logoH = k.logoYuk; logoW = logoH * 1920 / 476.3; ctx.drawImage(logo, k.kenar, H - 44 - logoH, logoW, logoH); }
  ctx.font = `500 ${k.ajandaYazi}px Lexend`; let x = W - k.kenar;
  for (let i = k.ajanda.length - 1; i >= 0; i--) {
    const ad = k.ajanda[i], w = ctx.measureText(ad).width;
    ctx.fillStyle = i === etkin ? R.vurgu : R.ikincil; ctx.fillText(ad, x, k.altTaban);
    if (i === etkin) { ctx.beginPath(); ctx.arc(x - w - 12, k.altTaban - 7, 4, 0, Math.PI * 2); ctx.fill(); }
    x -= w + 36;
  }
  ctx.restore();

  // Kanca: künye bölgelerini 'kunye' türü olarak ekle (alfa >= 0.2 ise)
  if (typeof window !== "undefined" && window.__kalemKutu && alfa >= 0.2) {
    window.__kalemKutu.ekle("kunye", "kunye:sol-ust", k.kenar, k.ustTaban - k.dersYazi, dw + 14 + sw, k.dersYazi + 6);
    if (bolum && bw > 0) {
      window.__kalemKutu.ekle("kunye", "kunye:sag-ust", W - k.kenar - bw, k.ustTaban - k.bolumYazi, bw, k.bolumYazi + 6);
    }
    if (logo && logoW > 0) {
      window.__kalemKutu.ekle("kunye", "kunye:logo", k.kenar, H - 44 - logoH, logoW, logoH);
    }
    const ajandaGen = (W - k.kenar) - x;
    if (ajandaGen > 0) {
      window.__kalemKutu.ekle("kunye", "kunye:ajanda", x, k.altTaban - k.ajandaYazi - 4, ajandaGen, k.ajandaYazi + 8);
    }
  }
}

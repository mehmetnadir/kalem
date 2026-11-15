// huni v2 (15.11): kanal katmanı + v2 bantları
// Paper.js ve düz canvas sahneleri bunu çağırır; HyperFrames sahneleri aynı sayıları HTML/CSS ile uygular.
// Kullanım: const K = await kunyeHazirla(); ... zeminCiz(ctx, f, K); ... kunyeCiz(ctx, { logo: K.logo });
//           altyaziCiz(ctx, altyaziMetin(K.altyazi, t));   // t = küresel sn
// simple-present-temel-s1 (15.11, P0202-S1-C): 02-04-ydt-temel-s1/ortak/kunye.js (v2) kopyası; yalnız KOK ve KUNYE.konu değişti.
export const KOK = "/projeler/simple-present-temel-s1b/ortak";
export const TEMALAR = {
  koyu: { zemin: "#1b1a17", murekkep: "#f3efe6", ikincil: "#c9c2b3", vurgu: "#f2a93b", vurguDolgu: "#f2a93b",
    logoSari: "#fece00", logoMetin: "#ffffff", kirmizi: "#e0473b", pilMetin: "#1b1a17" },
  acik: { zemin: "#f7f3ea", murekkep: "#1b2440", ikincil: "#5a6275", vurgu: "#d9900f", vurguDolgu: "#ffe066",
    logoSari: "#fece00", logoMetin: "#13204D", kirmizi: "#d6453a", pilMetin: "#1b2440" } };
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

export const RT = Object.fromEntries(Object.keys(TEMALAR.koyu).map((a) => [a, "@" + a]));
export const renkCoz = (r) => (typeof r === "string" && r[0] === "@" ? RENK[r.slice(1)] : r);
let temaAd = "koyu", surum = 0;
export const temaAdi = () => temaAd;
export const temaSurum = () => surum;
export function temaSec(ad) {
  if (!TEMALAR[ad] || ad === temaAd) return; temaAd = ad; surum++; Object.assign(RENK, TEMALAR[ad]);
}
try { temaSec(new URLSearchParams(location.search).get("tema") || "koyu"); } catch (e) { /* tarayıcı dışı */ }
// Bantlar: 0–280 boş · 291–339 kanal · 360–450 künye · 460–1380 içerik · 1400–1550 altyazı · 1570–1920 / sağ 960 boş.
export const KANAL = {
  logoX: 53.2,
  logoY: 291,
  logoH: 48,
  logoW: 193.5,
  yazi: "@ydspublishing",
  yaziFont: "700 42px Lexend",
  yaziX: 263,
  yaziTaban: 330,
  gorunurX: 60,
  kutuY: 291,
  kutuH: 50,
};

export function kanalCiz(ctx, K) {
  const kn = KANAL;
  ctx.save();
  ctx.globalAlpha = 1;
  ctx.textAlign = "left";
  ctx.textBaseline = "alphabetic";
  if (K && K.logo) ctx.drawImage(K.logo, kn.logoX, kn.logoY, kn.logoW, kn.logoH);
  ctx.font = kn.yaziFont;
  ctx.fillStyle = RENK.murekkep;
  ctx.fillText(kn.yazi, kn.yaziX, kn.yaziTaban);
  const yaziGen = ctx.measureText(kn.yazi).width;
  ctx.restore();
  if (typeof window !== "undefined" && window.__kalemKutu) {
    window.__kalemKutu.ekle("kunye", "kunye:kanal", kn.gorunurX, kn.kutuY, kn.yaziX + yaziGen - kn.gorunurX, kn.kutuH);
  }
}

export const KUNYE = {
  kenar: 60,
  sag: 960,
  icerikBas: 460,
  icerikSon: 1380,
  altyaziBas: 1400,
  altyaziSon: 1550,
  altyaziYazi: 44,
  altyaziSatir: 56,
  konu: "Simple Present",
  konuX: 60,
  konuTaban: 420,
  konuAzami: 34,
  konuAsgari: 28,
  rozet: "YDT · BASIC",
  rozetY: 386,
  rozetH: 48,
  rozetYazi: 26,
  rozetAra: 20,
  rozetPay: 20,
};
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
  let altyazi = [];
  try { altyazi = await (await fetch(`${KOK}/anlatim/altyazi.json`)).json(); } catch (e) { /* altyazı yok */ }
  let soz = [];
  try { soz = await (await fetch(`${KOK}/anlatim/sozcukler.json`)).json(); } catch (e) { /* sözcük zamanı yok */ }
  altyazi = altyaziDilimle(altyazi, soz);
  return { get logo() { return temaAd === "acik" ? acikLogo : koyuLogo; }, grenler: grenUret(), altyazi };
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


function konuDuzen(ctx) {
  const k = KUNYE;
  ctx.font = `700 ${k.rozetYazi}px Lexend`;
  const rw = ctx.measureText(k.rozet).width + 2 * k.rozetPay;
  for (let boy = k.konuAzami; boy >= k.konuAsgari; boy--) {
    ctx.font = `700 ${boy}px Fredoka`;
    const kw = ctx.measureText(k.konu).width;
    if (k.konuX + kw + k.rozetAra + rw <= k.sag) {
      return { boy, kw, rx: k.konuX + kw + k.rozetAra, rw };
    }
  }
  throw new Error("künye: konu + rozet 960'a sığmıyor");
}

export function kunyeCiz(ctx, { logo, alfa = 1 } = {}) {
  kanalCiz(ctx, { logo });
  const k = KUNYE, R = RENK;
  ctx.save();
  ctx.globalAlpha = alfa;
  ctx.textBaseline = "alphabetic";
  ctx.textAlign = "left";
  const D = konuDuzen(ctx);
  ctx.font = `700 ${D.boy}px Fredoka`;
  ctx.fillStyle = R.murekkep;
  ctx.fillText(k.konu, k.konuX, k.konuTaban);

  // rozet hapı
  ctx.fillStyle = R.vurguDolgu;
  ctx.beginPath();
  ctx.roundRect(D.rx, k.rozetY, D.rw, k.rozetH, k.rozetH / 2);
  ctx.fill();
  ctx.font = `700 ${k.rozetYazi}px Lexend`;
  ctx.fillStyle = R.pilMetin;
  ctx.textAlign = "center";
  ctx.fillText(k.rozet, D.rx + D.rw / 2, k.rozetY + k.rozetH / 2 + 9);
  ctx.restore();

  // Kanca (alfa >= 0.2 ve __kalemKutu varsa)
  if (typeof window !== "undefined" && window.__kalemKutu && alfa >= 0.2) {
    window.__kalemKutu.ekle("kunye", "kunye:konu", k.konuX, k.konuTaban - D.boy, D.kw, D.boy + 8);
    window.__kalemKutu.ekle("kunye", "kunye:rozet", D.rx, k.rozetY, D.rw, k.rozetH);
  }
}

// Altyazı bandı (y 1400–1550): konuşulan parça, en çok 2 satır, ortalı. Sessiz izleme için zorunlu (kalıp §1 kural 3).
export function altyaziMetin(liste, t) {
  if (!liste) return "";
  const p = liste.find((a) => t >= a.t0 - 0.05 && t < a.t1 + 0.35);
  return p ? p.metin : "";
}
export function altyaziCiz(ctx, metin, { alfa = 1 } = {}) {
  if (!metin) return;
  const k = KUNYE, R = RENK, genislik = k.sag - k.kenar;
  const ortaX = (k.kenar + k.sag) / 2;
  ctx.save();
  ctx.globalAlpha = alfa;
  ctx.textAlign = "center";
  ctx.textBaseline = "alphabetic";
  let satirlar = [];
  for (const boy of [k.altyaziYazi, 40, 36]) {
    ctx.font = `500 ${boy}px Lexend`;
    satirlar = altyaziSar(ctx, metin, genislik);
    if (satirlar.length <= 2) break;
  }
  if (satirlar.length > 2) {
    throw new Error("altyazı 2 satıra sığmıyor: " + metin);
  }
  const y0 = k.altyaziBas + (satirlar.length === 1 ? 84 : 56);
  ctx.fillStyle = R.murekkep;
  satirlar.forEach((sat, i) => ctx.fillText(sat, ortaX, y0 + i * k.altyaziSatir));
  ctx.restore();
}

// 2 satıra sığmayan parça sözcük zamanıyla dilimlenir; sözcük sayısı tutmazsa karakter oranı.
function altyaziDilimle(liste, soz) {
  if (!liste || !liste.length) return [];
  const ctx = document.createElement("canvas").getContext("2d");
  ctx.font = `500 ${KUNYE.altyaziYazi}px Lexend`;
  const genislik = KUNYE.sag - KUNYE.kenar, cikti = [];
  for (const p of liste) {
    if (altyaziSar(ctx, p.metin, genislik).length <= 2) {
      cikti.push(p);
      continue;
    }
    const kelimeler = p.metin.split(" ");
    const z = (soz || []).filter((s) => s.cumle === p.cumle && s.t0 >= p.t0 - 0.06 && s.t0 < p.t1);
    const zaman = (i) => (z.length === kelimeler.length
      ? z[i].t0
      : p.t0 + ((p.t1 - p.t0) * kelimeler.slice(0, i).join(" ").length) / p.metin.length);
    const dilimler = [];
    let grup = "", bas = 0;
    for (let i = 0; i < kelimeler.length; i++) {
      const d = grup ? grup + " " + kelimeler[i] : kelimeler[i];
      if (grup && altyaziSar(ctx, d, genislik).length > 2) {
        dilimler.push({ metin: grup, bas });
        grup = kelimeler[i];
        bas = i;
      } else {
        grup = d;
      }
    }
    if (grup) dilimler.push({ metin: grup, bas });
    for (let j = 0; j < dilimler.length; j++) {
      const d = dilimler[j];
      const t0 = zaman(d.bas);
      const t1 = j < dilimler.length - 1 ? zaman(dilimler[j + 1].bas) - 0.4 : p.t1;
      cikti.push({ ...p, metin: d.metin, t0, t1 });
    }
  }
  return cikti;
}

function altyaziSar(ctx, metin, genislik) {
  const satirlar = []; let s = "";
  for (const w of metin.split(" ")) {
    const d = s ? s + " " + w : w;
    if (ctx.measureText(d).width > genislik && s) { satirlar.push(s); s = w; } else s = d;
  }
  if (s) satirlar.push(s);
  return satirlar;
}

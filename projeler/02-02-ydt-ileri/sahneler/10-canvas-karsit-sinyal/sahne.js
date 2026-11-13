// SAHNE 10 — Sinyaller ve çiftçiler (02-02-ydt-ileri; düz canvas, 1075 kare, t_bas 224,18; cümle 34–37).
// Kendini çizen kalem; zaman yalnız kare numarasından, sözcük zamanları sozcukler.json'dan (T() ile okunur).
// Akış: iki sütun (geçici | kalıcı sinyaller) → kalıcı uzun bant, geçici kısa bant; «yarın da sürer mi?»
// işaretçisi (sürer / sürmez) → Farmers kartı (grow halkası, kalıcı oku) → çeviri → sürekli mi, geçici mi?
// Kırmızı yok; renkler yalnız kunye.js TEMALAR token'ları. Öğrenci sesi bu sahnede yok.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, olc, kis, altCizgi } from "./sahne-ortak.js";

const KARE = 1075, TBAS = 224.56, ICERIK = 1063;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Contrast", etkin: 2,
  cumle: [34, 35, 36, 37] });
window.__S = S;                                   // önizleme ölçümü (olaylar.json)
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`;

// Anlatım sözcüğünün t0'ı (küresel sn); bulunamazsa sahne hiç yüklenmez (sessiz yanlış zaman olmaz).
const T = (ad, yakin) => {
  const r = S.dizi(ad, yakin, 1);
  if (!r.length || r[0].sozcuk !== ad) throw new Error("sözcük yok: " + ad + " @" + yakin);
  return r[0].t0;
};
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

// Öğeyi [t0, t1] sn arasında gerçekten söndürür: öğe kendi globalAlpha değerini mutlak yazdığı için
// (darbeCiz, metinPop) örnek üstünde globalAlpha yazımı sönme çarpanıyla çarpılır; söndükten sonra çizilmez.
const ALFA = (typeof CanvasRenderingContext2D !== "undefined")
  ? Object.getOwnPropertyDescriptor(CanvasRenderingContext2D.prototype, "globalAlpha") : null;
function sondur(e, t0, t1) {
  if (Array.isArray(e)) return e.map((x) => sondur(x, t0, t1));
  return { ...e, ciz: (ctx, f) => {
    const m = 1 - kis((S.zm(f) - t0) / (t1 - t0));
    if (m <= 0.01) return;
    if (m >= 0.999 || !ALFA) { e.ciz(ctx, f); return; }
    let v = 1;
    Object.defineProperty(ctx, "globalAlpha", { configurable: true, get: () => v,
      set: (x) => { v = x; ALFA.set.call(ctx, x * m); } });
    ALFA.set.call(ctx, m);
    try { e.ciz(ctx, f); } finally { delete ctx.globalAlpha; ALFA.set.call(ctx, 1); }
  } };
}
// Sönme grupları: A = sinyal sütunları (234,4) · B = «yarın» işaretçisi ve soru (248,3) · C = Farmers kartı (253,7).
const SON = { A: [234.78, 235.18], B: [248.68, 248.93], C: [254.08, 254.33] };
const koy = (e, g) => S.koy(g ? sondur(e, SON[g][0], SON[g][1]) : e);

async function kur() {
  await S.kur();
  const F52 = FF(52), F56 = FF(56), F64 = FF(64), F72 = FF(72);

  // ---------------- 34 (224,73–234,36) sinyaller: sol geçici, sağ kalıcı ----------------
  koy(S.darbe([[960, 150], [960, 600]], { duz: true, w: 5, renk: IKINCIL, uc0: 14, uc1: 30 },
    T("Geçici", 225.11), 0.6, 0.5), "A");
  koy(S.metinPop({ parca: [["geçici", KREM]], x: 150, y: 230, font: F64, tb: T("Geçici", 225.11), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }), "A");
  koy(S.metinPop({ parca: [["kalıcı", KREM]], x: 1010, y: 230, font: F64, tb: T("Kalıcı", 230.57), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }), "A");
  [["this week", "this", 226.64, 150, 340, 41], ["this semester", "this", 227.76, 150, 430, 42],
    ["these days", "these", 228.96, 150, 520, 43], ["every", "every,", 232.42, 1010, 340, 44],
    ["always", "always.", 233.46, 1010, 430, 45]].forEach(([m, ad, yk, x, y, th]) => {
    const tb = T(ad, yk), w = olc(F64, m);
    koy(S.metinPop({ parca: [[m, KREM]], x, y, font: F64, tb, sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }), "A");
    koy(S.darbe(altCizgi(x - 4, x + w + 4, y + 16, th), { w: 7, renk: RT.vurguDolgu, alfa: 0.9, uc0: 8, uc1: 12 },
      tb + 0.2, 0.3, false), "A");
  });

  // ---------------- 35 (234,91–243,95) kalıcı uzun bant · geçici kısa bant · yarın da sürer mi? ----------------
  S.koy(S.metinPop({ parca: [["kalıcı", KREM]], x: 150, y: 318, font: F56, tb: T("Kalıcı", 235.29), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.darbe([[330, 300], [1500, 300]], { duz: true, w: 34, renk: RT.vurguDolgu, alfa: 0.9, uc0: 6, uc1: 6 },
    T("kimliğin", 236.09), 1.0, 0.5));
  koy(S.elYazisi({ metin: "yaşadığın şehir", x: 330, y: 372, boy: 48, renk: IKINCIL,
    sozcukler: pen("yaşadığın", 237.61, 2) }), "B");
  S.koy(S.metinPop({ parca: [["geçici", KREM]], x: 150, y: 498, font: F56, tb: T("Geçici", 238.97), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.darbe([[330, 480], [700, 480]], { duz: true, w: 34, renk: RT.vurguDolgu, alfa: 0.9, uc0: 6, uc1: 6 },
    T("haftalık", 240.01), 0.5, 0.5));
  koy(S.elYazisi({ metin: "bir haftalık otel", x: 330, y: 552, boy: 48, renk: IKINCIL,
    sozcukler: pen("bir", 239.85, 3) }), "B");
  // 242,83 «yarın»: işaretçi çizgisi · 243,23 «sürer»: ok + sürer · sürmez (geçici bant yarına varmaz)
  const tY = T("yarın", 243.21);
  koy(S.darbe([[1000, 250], [1000, 590]], { duz: true, w: 5, renk: SARI, alfa: 0.9, uc0: 8, uc1: 12 }, tY, 0.4,
    0.6), "B");
  koy(S.metinPop({ parca: [["yarın", SARI]], x: 1000, y: 232, font: F52, hiza: "orta", tb: tY + 0.1, sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }), "B");
  const tS = T("sürer", 243.61);
  koy(S.darbeler(ok([1510, 300], [1580, 300], 7), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, tS, 0.16, 0.1, 0.5), "B");
  koy(S.metinPop({ parca: [["sürer", SARI]], x: 1600, y: 318, font: F56, tb: tS + 0.15, sure: 0.3, olcek0: 0.85,
    ses: 0.5, turu: "tik" }), "B");
  koy(S.metinPop({ parca: [["sürmez", IKINCIL]], x: 730, y: 498, font: F56, tb: T("mi?", 244.01), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }), "B");
  koy(S.elYazisi({ metin: "bu durum yarın da sürer mi?", x: 150, y: 700, boy: 80, renk: KREM,
    sozcukler: pen("bu", 242.57, 6) }), "B");

  // ---------------- 36 (244,50–248,02) Farmers: kart, grow halkası, kalıcı oku ----------------
  koy(S.darbeler(kutu(110, 770, 1500, 150, 75), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, 244.68, 0.14, 0.1,
    0.55), "C");
  const cum = S.cumleYaz({ sozcukler: S.dizi("Farmers", 244.88, 8), x: 150, y: 860, maxGen: 1450, font: FF(56),
    satirH: 90, satirSay: [8], bosluk: 4 });
  koy(cum, "C");
  koy(S.halka(cum.kel[1], T("grow", 245.44), 0.4, 17, 6, true), "C");
  koy(S.darbeler(ok([1440, 748], [1440, 348], 8), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, T("sunflowers", 246.80),
    0.3, 0.12, 0.5), "C");
  koy(S.elYazisi({ metin: "kalıcı", x: 1470, y: 680, boy: 72, renk: SARI, tb: T("Thrace.", 247.68), sure: 0.7 }), "C");

  // ---------------- 37 (248,57–259,61) çeviri · Bu da kalıcı · zaman sözcüğü yok · sürekli mi, geçici mi? ----------------
  koy(S.elYazisi({ metin: "Çiftçiler Trakya'da çoğunlukla buğday ve ayçiçeği yetiştirir.", x: 150, y: 660,
    boy: 52, renk: IKINCIL, sozcukler: pen("Çiftçiler", 248.95, 7) }), "C");
  koy(S.darbe(elips(1545, 650, 100, 50, -0.03, 19), { w: 6, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 },
    T("kalıcı.", 253.35), 0.4, 0.55), "C");
  S.koy(S.elYazisi({ metin: "zaman sözcüğü yok", x: 150, y: 700, boy: 64, renk: IKINCIL,
    sozcukler: pen("zaman", 254.87, 3) }));
  S.koy(S.elYazisi({ metin: "anlama bak", x: 150, y: 800, boy: 80, renk: SARI,
    sozcukler: pen("anlama", 257.03, 2) }));
  const tK = T("sürekli", 258.47), tG = T("geçici", 259.35);
  S.koy(S.metinPop({ parca: [["sürekli mi, geçici mi?", KREM]], x: 150, y: 920, font: F72, tb: tK, sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.darbeler(ok([1700, 300], [1535, 300], 9), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, tK + 0.1, 0.15, 0.1,
    0.5));
  S.koy(S.elYazisi({ metin: "?", x: 1710, y: 345, boy: 110, renk: SARI, tb: tK + 0.3, sure: 0.3 }));
  // QA 13.11: son olay sahne sonundan (259,61) en az 0,45 sn önce bitsin (t_son − 0,45 = 259,16).
  S.koy(S.darbeler(ok([900, 480], [735, 480], 10), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, tG - 0.2, 0.12, 0.05, 0.5));
  S.koy(S.elYazisi({ metin: "?", x: 910, y: 525, boy: 110, renk: SARI, tb: tG - 0.1, sure: 0.2 }));
}

surucu(kur, (f) => S.kare(f), KARE);

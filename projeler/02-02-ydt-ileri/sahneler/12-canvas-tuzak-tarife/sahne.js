// SAHNE 12 — Tuzak uçak ve tarife (düz canvas, 796 kare, t_bas 289,65; cümle 43–46). Kendini çizen kalem;
// zaman yalnız kare numarasından, sözcük zamanları sozcukler.json'dan (T() ile okunur, elle yazılmaz).
// Akış: konser kartı küçük yerinde · ikinci kart (takes off sarı daire, uçak) · TR çeviri · dört ikon
// (otobüs, uçak, müzik, okul) + tarife çizgisi · fark tablosu (kişisel plan ↔ resmî program).
// Kırmızı yok (tuzak ünlemi sahne 11'de); doğru/yanlış işareti yok.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, altCizgi, kutu, olc, kis } from "./sahne-ortak.js";

const KARE = 796, TBAS = 290.03, ICERIK = 784;
const KOKDIZ = "/projeler/02-02-ydt-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Trap", etkin: 2,
  cumle: [43, 44, 45, 46] });
window.__S = S;                                   // önizleme ölçümü (olaylar.json)
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, SARI_D = RT.vurguDolgu;
const F56 = "700 56px Fredoka", F44 = "700 44px Fredoka";

// Anlatım sözcüğünün t0'ı (küresel sn); bulunamazsa sahne hiç yüklenmez (sessiz yanlış zaman olmaz).
const T = (ad, yakin) => {
  const r = S.dizi(ad, yakin, 1);
  if (!r.length || r[0].sozcuk !== ad) throw new Error("sözcük yok: " + ad + " @" + yakin);
  return r[0].t0;
};
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

// Öğeyi [t0, t1] sn arasında gerçekten söndürür: öğe kendi globalAlpha değerini mutlak yazdığı için
// (darbeCiz, metinPop) örnek üstünde globalAlpha yazımı fade çarpanıyla çarpılır; söndükten sonra çizilmez.
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
// Öğe grupları: C = TR çeviri (299,97–300,27 söner) · D = kartlar + ikon sırası (308,10–308,42 söner,
// fark tablosuna yer açar) · yok = kalıcı.
const SON = { C: [300.35, 300.65], D: [308.48, 308.80] };
const koy = (e, g) => S.koy(g ? sondur(e, SON[g][0], SON[g][1]) : e);

async function kur() {
  await S.kur();
  const [ucak, otobus, muzik, okul] = await Promise.all([svgOku("tabler/plane.svg"), svgOku("../../sahneler/12-canvas-tuzak-tarife/tren.svg"),
    svgOku("tabler/music.svg"), svgOku("tabler/school.svg")]);

  // ---------------- konser kartı küçük yerinde (sahne 11 sonu; 290,08'de kalemle yeniden belirir) ----------------
  {
    const f34 = "700 34px Fredoka";
    const m1 = "The concert begins at 8 o'clock tomorrow evening", m2 = "and ends at around 11.";
    const w = Math.round(olc(f34, m1) + 44);
    koy(S.darbeler(kutu(110, 150, w, 150, 62), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, 290.46, 0.14, 0.1,
      0.4), "D");
    koy(S.metinPop({ parca: [[m1, KREM]], x: 132, y: 210, font: f34, tb: 290.50, sure: 0.2, olcek0: 0.95,
      ses: false }), "D");
    koy(S.metinPop({ parca: [[m2, KREM]], x: 132, y: 260, font: f34, tb: 290.54, sure: 0.2, olcek0: 0.95,
      ses: false }), "D");
  }

  // ---------------- 43 (290,20–294,76) ikinci kart: uçuş cümlesi, 2 satır ----------------
  koy(S.darbeler(kutu(110, 340, 1700, 260, 63), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, 290.50, 0.14, 0.1,
    0.55), "D");
  const say = { "six": "6", "four.": "4." };
  const soz = S.dizi("My", 290.58, 18).map((w) => ({ ...w, sozcuk: say[w.sozcuk] || w.sozcuk }));
  const cum = S.cumleYaz({ sozcukler: soz, x: 150, y: 452, maxGen: 1600, font: F56, satirH: 84,
    satirSay: [9, 9], bosluk: 4 });
  koy(cum, "D");
  const kel = cum.kel;                            // 0 My 1 flight 2 takes 3 off 4 at 5 6 6 in 7 the 8 morning, | 9 so …
  // 290,80 «takes»: takes off sarı daire (kalıcı)
  // QA 13.11 halka kuralı: komşu sözcüğe değen halka yerine el altçizgisi (off göründükten sonra)
  koy(S.darbe(altCizgi(kel[2].x - 4, kel[3].x + kel[3].w + 4, kel[2].y + 15, 73), { w: 6, renk: RT.vurgu, alfa: 0.9,
    uc0: 8, uc1: 12 }, T("takes", 291.18) + 0.6, 0.45, 0.55), "D");
  // 290,44 «flight»: uçak, kartın sağ boşluğunda (kalemle çizilir)
  {
    const sag = kel[8].x + kel[8].w, px = Math.round(sag + 60), pw = Math.min(260, 1790 - px);
    koy(S.cizim({ svg: ucak, ad: "ucak", kutu: { x: px, y: 390, w: pw, h: Math.min(pw, 190) }, esik: 0.004,
      enCok: 8, w: 5, tb: T("flight", 290.82), sure: 1.0, olayEnCok: 4, nefes: false }), "D");
  }

  // ---------------- 44 (295,23–299,87) TR çeviri (Caveat 54, iki satır) ----------------
  koy(S.elYazisi({ metin: "Uçağım sabah altıda kalkıyor;", x: 140, y: 695, boy: 54, renk: IKINCIL,
    sozcukler: pen("Uçağım", 295.61, 4) }), "C");
  koy(S.elYazisi({ metin: "bu yüzden dörde kadar havalimanında olmalıyım.", x: 140, y: 765, boy: 54,
    renk: IKINCIL, sozcukler: pen("bu", 297.65, 6) }), "C");

  // ---------------- 45 (300,34–308,02) dört ikon sırayla + tarife çizgisi ----------------
  const IK = [[otobus, "tren", "tren", T("Tren,", 300.72), 300], [ucak, "ucak", "uçak", T("uçak,", 301.36), 760],
    [muzik, "muzik", "konser", T("konser,", 302.04), 1220], [okul, "okul", "ders programı", T("ders", 302.76), 1660]];
  IK.forEach(([svg, ad, etiket, t, cx]) => {
    koy(S.cizim({ svg, ad, kutu: { x: cx - 85, y: 745, w: 170, h: 170 }, esik: 0.004, enCok: 8, w: 5, tb: t,
      sure: 0.8, olayEnCok: 3, nefes: false }), "D");
    koy(S.metinPop({ parca: [[etiket, KREM]], x: cx, y: 975, font: F44, hiza: "orta", tb: t, sure: 0.25,
      olcek0: 0.85, ses: 0.5, turu: "tik" }), "D");
  });
  // 303,78 «tarife»: dört ikonun üstünde sarı tarife çizgisi; 306,66 «geniş»: çizgiye parıltı
  koy(S.darbe([[200, 712], [980, 702], [1760, 712]], { w: 8, renk: SARI_D, alfa: 0.85, uc0: 10, uc1: 18 },
    T("tarife.", 304.16), 0.6, 0.55), "D");
  koy(S.parilti(980, 690, T("geniş", 307.04), 26), "D");

  // ---------------- 46 (308,49–315,85) fark tablosu: kişisel plan ↔ resmî program ----------------
  koy(S.darbe([[960, 200], [958, 560], [960, 900]], { w: 4.4, renk: IKINCIL, uc0: 8, uc1: 12 }, 308.93, 0.5,
    0.4));
  // sol sütun: kişisel plan → şimdiki zaman; 02-01 ileri cümlesi geri gelir
  S.koy(S.metinPop({ parca: [["kişisel plan", KREM]], x: 130, y: 270, font: F56, tb: T("Kendi", 308.87),
    sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.metinPop({ parca: [["→  ", IKINCIL], ["şimdiki zaman", SARI]], x: 130, y: 360, font: F56,
    tb: T("şimdiki", 310.15), sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.darbeler(kutu(110, 430, 810, 190, 64), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 },
    T("yarın", 311.75) - 0.3, 0.14, 0.1, 0.5));
  S.koy(S.metinPop({ parca: [["We are taking the bus", KREM]], x: 140, y: 510, font: "700 46px Fredoka",
    tb: T("yarın", 311.75), sure: 0.3, olcek0: 0.9, ses: 0.5, turu: "tik" }));
  S.koy(S.metinPop({ parca: [["to Izmir tomorrow morning", KREM]], x: 140, y: 578, font: "700 46px Fredoka",
    tb: T("İzmir'e", 312.39), sure: 0.3, olcek0: 0.9, ses: 0.5, turu: "tik" }));
  // sağ sütun: resmî program → geniş zaman; concert · flight
  S.koy(S.metinPop({ parca: [["resmî program", KREM]], x: 1000, y: 270, font: F56, tb: T("Resmî", 313.83),
    sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.darbeler(kutu(990, 430, 810, 190, 65), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, 313.93, 0.14, 0.1,
    0.5));
  S.koy(S.cizim({ svg: muzik, ad: "muzik2", kutu: { x: 1010, y: 465, w: 110, h: 110 }, esik: 0.004, enCok: 8,
    w: 4.5, tb: T("program", 314.23), sure: 0.5, olayEnCok: 2, nefes: false }));
  S.koy(S.metinPop({ parca: [["concert", KREM]], x: 1135, y: 540, font: "700 48px Fredoka",
    tb: T("program", 314.23), sure: 0.25, olcek0: 0.9, ses: 0.5, turu: "tik" }));
  S.koy(S.cizim({ svg: ucak, ad: "ucak2", kutu: { x: 1400, y: 465, w: 110, h: 110 }, esik: 0.004, enCok: 8,
    w: 4.5, tb: T("varsa", 314.75), sure: 0.5, olayEnCok: 2, nefes: false }));
  S.koy(S.metinPop({ parca: [["flight", KREM]], x: 1525, y: 540, font: "700 48px Fredoka",
    tb: T("varsa", 314.75), sure: 0.25, olcek0: 0.9, ses: 0.5, turu: "tik" }));
  S.koy(S.metinPop({ parca: [["→  ", IKINCIL], ["geniş zaman", SARI]], x: 1000, y: 360, font: F56,
    tb: T("geniş", 315.27), sure: 0.3, olcek0: 0.85, ses: 0.6, turu: "vurus" }));
}

surucu(kur, (f) => S.kare(f), KARE);

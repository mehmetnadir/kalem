// SAHNE 07 — Karşıt çift (düz canvas, 1845 kare, t_bas 157,88; cümle 28–38). Kendini çizen kalem;
// zaman yalnız kare numarasından, sözcük zamanları sozcukler.json'dan (T() ile okunur, elle yazılmaz).
// Akış: bölünmüş ekran (sol: She eats fish every day · sağ: She is eating fish now) → TR çeviri, zaman
// çizgisi (takvim noktaları | now noktası nabız), her gün → rutin / şu anda → olay sürüyor → fark tablosu
// (geniş zaman sinyalleri | şimdiki zaman sinyalleri) → yor ↔ ing bağı + çarpı, rutin → geniş zaman →
// kanca cümlesi geri gelir (every morning, çarpı → yeşil tik, -ing yok, am yok) → ek değil, anlam.
// Kırmızı yok (kırmızı yalnız tuzak sahnesinde); yanlış = ikincil/mürekkep çarpı, doğru = yeşil tik.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, altCizgi, olc, kis } from "./sahne-ortak.js";

const KARE = 1871, TBAS = 157.54, ICERIK = 1859;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Contrast pair", etkin: 2,
  cumle: [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38] });
window.__S = S;                                   // önizleme ölçümü (olaylar.json)
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, SARI_D = RT.vurguDolgu;
const YESIL = RT.vurgu;                           // doğru işareti: yeşil token yok → vurgu (QA 13.11)
const F56 = "700 56px Fredoka", F64 = "700 64px Fredoka";

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
// Öğe grupları: her grup kendi sönme anında kalkar. koy(e, g): g = "A" | "B" | "C" | "D" | yok (kalıcı).
const SON = { A: [178.16, 178.56], B: [191.51, 191.86], C: [200.61, 200.96], D: [214.84, 215.14] };
const koy = (e, g) => S.koy(g ? sondur(e, SON[g][0], SON[g][1]) : e);
// Parıltı gibi kendi alfasını yöneten ve süresi kısa öğeler sondurulmadan eklenir (koy(e) ile).

async function kur() {
  await S.kur();

  // ---------------- 28 «Şimdi bir karşıt çift» (158,43–160,35): ortada dikey ayraç ----------------
  koy(S.darbe([[960, 150], [960, 950]], { duz: true, w: 5, renk: IKINCIL, uc0: 14, uc1: 30 },
    T("karşıt", 158.89), 0.8, 0.5), "B");

  // ---------------- 29 «She eats fish every day.» (160,82–162,90): sol kart ----------------
  koy(S.darbeler(kutu(110, 150, 820, 250, 31), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, 160.11, 0.14, 0.1,
    0.55), "B");
  const sol = S.cumleYaz({ sozcukler: S.dizi("She", 160.48, 5), x: 150, y: 250, maxGen: 780,
    font: "700 60px Fredoka", satirH: 84, satirSay: [3, 2], bosluk: 4 });
  koy(sol, "B");
  const sk = sol.kel;                              // 0 She 1 eats 2 fish | 3 every 4 day.
  // sol zaman çizgisi: «day» (162,34) ile takvim: eksen + 7 gün noktası (tekrar)
  {
    const Y = 760, X0 = 190, ADIM = 105;
    koy(S.darbe([[140, Y], [900, Y]], { duz: true, w: 5, renk: KREM, uc0: 6, uc1: 12 }, 162, 0.4, 0.4), "A");
    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].forEach((g, i) => {
      const tb = 162.26 + i * 0.12, x = X0 + ADIM * i;
      koy(S.darbe(elips(x, Y, 15, 15, 0.1, 31 + i), { w: 5, renk: SARI, alfa: 0.9, uc0: 6, uc1: 10 }, tb, 0.25,
        i < 3 ? 0.45 : false), "A");
      koy(S.metinPop({ parca: [[g, IKINCIL]], x, y: Y + 62, font: "500 30px Lexend", hiza: "orta", tb: tb + 0.1,
        sure: 0.2, ses: false }), "A");
    });
  }
  // sol TR çeviri (163,37–166,09): her sözcük kendi konuşma penceresinde yazılır
  koy(S.elYazisi({ metin: "Her gün balık yer.", x: 140, y: 470, boy: 52, renk: IKINCIL,
    sozcukler: pen("Her", 163.03, 4) }), "A");
  koy(S.elYazisi({ metin: "Bu onun alışkanlığı.", x: 140, y: 535, boy: 52, renk: IKINCIL,
    sozcukler: pen("Bu", 164.47, 3) }), "A");
  // every day sarı altı çizgi (kayan çizgi söndükten sonra kalıcı, 163,50)
  koy(S.darbe(altCizgi(sk[3].x - 4, sk[4].x + sk[4].w + 4, sk[3].y + 15, 91),
    { w: 8.5, renk: SARI_D, alfa: 0.85, uc0: 8, uc1: 14 }, 163.16, 0.4, 0.5), "B");
  // 166,34 «Every day»: sarı halka + her gün; 167,55 «rutin»: → rutin
  const tEv = T("Every", 166);
  koy(S.halka(sk[3], T("day", 166.4), 0.45, 21, 6, sk[4]), "B");
  koy(S.metinPop({ parca: [["her gün", KREM]], x: 140, y: 650, font: F56, tb: tEv, sure: 0.3, olcek0: 0.85,
    ses: 0.5, turu: "tik" }), "A");
  koy(S.metinPop({ parca: [["→  ", IKINCIL], ["rutin", SARI]], x: 140 + olc(F56, "her gün") + 20, y: 650,
    font: F56, tb: T("rutin", 167.21), sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }), "A");

  // ---------------- 31 «She is eating fish now.» (169,14–170,90): sağ kart ----------------
  koy(S.darbeler(kutu(990, 150, 820, 250, 32), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, 168.46, 0.14, 0.1,
    0.55), "B");
  const sag = S.cumleYaz({ sozcukler: S.dizi("She", 168.8, 5), x: 1030, y: 250, maxGen: 780,
    font: "700 60px Fredoka", satirH: 84, satirSay: [3, 2], bosluk: 4 });
  koy(sag, "B");
  const gk = sag.kel;                              // 0 She 1 is 2 eating | 3 fish 4 now.
  // sağ zaman çizgisi: «now» (170,34): eksen + büyük nokta, nabız atar (178,5'te söner)
  {
    const Y = 760, X = 1400;
    koy(S.darbe([[1010, Y], [1790, Y]], { duz: true, w: 5, renk: KREM, uc0: 6, uc1: 12 }, 170, 0.4, 0.4), "A");
    koy(S.darbe(elips(X, Y, 20, 20, 0.1, 33), { w: 6, renk: SARI, alfa: 0.9, uc0: 6, uc1: 10 }, 170.36, 0.3, 0.6),
      "A");
    koy(S.metinPop({ parca: [["now", IKINCIL]], x: X, y: Y + 62, font: "500 30px Lexend", hiza: "orta", tb: 170.66,
      sure: 0.2, ses: false }), "A");
    koy(S.nabiz(X, Y, 20, 170.76), "A");
  }
  // sağ TR çeviri (171,37–175,21)
  koy(S.elYazisi({ metin: "Şu anda balık yiyor.", x: 1020, y: 470, boy: 52, renk: IKINCIL,
    sozcukler: pen("Şu", 171.03, 4) }), "A");
  koy(S.elYazisi({ metin: "Tabağı önünde, olay sürüyor.", x: 1020, y: 535, boy: 52, renk: IKINCIL,
    sozcukler: pen("Tabağı", 172.71, 4) }), "A");
  // now sarı altı çizgi (kayan çizgi söndükten sonra kalıcı, 171,55)
  koy(S.darbe(altCizgi(gk[4].x - 4, gk[4].x + gk[4].w + 4, gk[4].y + 15, 92),
    { w: 8.5, renk: SARI_D, alfa: 0.85, uc0: 8, uc1: 14 }, 171.21, 0.4, 0.5), "B");
  // 175,46 «Now»: sarı halka + şu anda → olay sürüyor
  const tNow = T("Now", 175.12);
  koy(S.halka(gk[4], tNow, 0.45, 22), "B");
  koy(S.metinPop({ parca: [["şu anda", KREM]], x: 1020, y: 650, font: F56, tb: tNow, sure: 0.3, olcek0: 0.85,
    ses: 0.5, turu: "tik" }), "A");
  koy(S.metinPop({ parca: [["→  ", IKINCIL], ["olay sürüyor", SARI]], x: 1020 + olc(F56, "şu anda") + 20, y: 650,
    font: F56, tb: tNow + 0.4, sure: 0.3, olcek0: 0.85, ses: 0.4, turu: "tik" }), "A");

  // ---------------- 33 (178,98–191,76) fark tablosu: sinyal sözcükleri sırayla dolar ----------------
  // 179,86 «balık»: iki cümlede de balık (soluk halka), 181,18 zaman sözcüğü: parıltı
  const fish = (k, tohum) => S.halka(k, T("balık", 179.52), 0.4, tohum);
  const f1 = sondur(fish(sk[2], 41), 180.46, 180.86), f2 = sondur(fish(gk[3], 43), 180.46, 180.86);
  S.koy([f1, f2]);
  S.koy(S.parilti((sk[3].x + sk[4].x + sk[4].w) / 2, sk[3].y - 74, 180.84));
  S.koy(S.parilti(gk[4].x + gk[4].w / 2, gk[4].y - 74, 180.84));
  // sol sütun: every day · always · usually → geniş zaman
  [["every day", T("Every", 182.73), 560], ["always", T("always,", 183.85), 640],
    ["usually", T("usually:", 184.89), 720]].forEach(([m, t, y], i) => {
    koy(S.metinPop({ parca: [[m, KREM]], x: 140, y, font: F64, tb: t, sure: 0.3, olcek0: 0.85, ses: 0.5,
      turu: "tik" }), "B");
  });
  koy(S.metinPop({ parca: [["→  ", IKINCIL], ["geniş zaman", SARI]], x: 140, y: 830, font: F56,
    tb: T("geniş", 186.1), sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }), "B");
  // sağ sütun: now · look (çoğunlukla) → şimdiki zaman
  koy(S.metinPop({ parca: [["now", KREM]], x: 1020, y: 560, font: F64, tb: T("Now", 187.71), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }), "B");
  koy(S.metinPop({ parca: [["look", KREM]], x: 1020, y: 640, font: F64, tb: T("look", 188.85), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }), "B");
  koy(S.elYazisi({ metin: "çoğunlukla", x: 1020 + olc(F64, "look") + 50, y: 640, boy: 56, renk: IKINCIL,
    sozcukler: pen("çoğunlukla", 189.5, 1) }), "B");
  koy(S.metinPop({ parca: [["→  ", IKINCIL], ["şimdiki zaman", SARI]], x: 1020, y: 830, font: F56,
    tb: T("şimdiki", 190.38), sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }), "B");

  // ---------------- 34 (192,23–200,87) yor ↔ ing: Türkçe ek İngilizcede ing değil ----------------
  // 193,03 «her sabah kalkıyorum»: Türkçe cümle (el yazısı); 195,75 «yor»: -yor çipi
  koy(S.elYazisi({ metin: "her sabah kalkıyorum", x: 300, y: 330, boy: 64, renk: KREM,
    sozcukler: pen("her", 192.69, 3) }), "C");
  const FB = "700 96px Fredoka", wYor = olc(FB, "-yor"), wIng = olc(FB, "-ing");
  koy(S.metinPop({ parca: [["-yor", KREM]], x: 560 - wYor / 2, y: 540, font: FB, tb: T("yor,", 195.41),
    sure: 0.3, olcek0: 0.8, ses: 0.6, turu: "tik" }), "C");
  // 197,11 «rutin»: rutin → geniş zaman (199,67 «geniş»)
  koy(S.metinPop({ parca: [["rutin", SARI]], x: 300, y: 770, font: F64, tb: T("rutin.", 196.77), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }), "C");
  koy(S.metinPop({ parca: [["→  ", IKINCIL], ["geniş zaman", KREM]], x: 300 + olc(F64, "rutin"), y: 770,
    font: F64, tb: T("geniş", 199.33), sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }), "C");
  // 197,99 «İngilizcede»: -ing çipi + bağ çizgisi; 198,95: bağın üstüne çarpı (ing yok)
  koy(S.metinPop({ parca: [["-ing", KREM]], x: 1360 - wIng / 2, y: 540, font: FB, tb: T("İngilizcede", 197.65),
    sure: 0.3, olcek0: 0.8, ses: 0.6, turu: "tik" }), "C");
  koy(S.darbeler(ok([950, 500], [1210, 500], 5), { w: 6, renk: IKINCIL, uc0: 10, uc1: 14 }, 197.96, 0.18, 0.1,
    0.45), "C");
  koy(S.darbeler(ok([970, 500], [710, 500], 6), { w: 6, renk: IKINCIL, uc0: 10, uc1: 14 }, 197.96, 0.18, 0.1,
    false), "C");
  koy(S.darbe([[900, 440], [1020, 560]], { duz: true, w: 9, renk: KREM, uc0: 8, uc1: 12 }, T("o", 198.61), 0.2,
    0.55), "C");
  koy(S.darbe([[1020, 440], [900, 560]], { duz: true, w: 9, renk: KREM, uc0: 8, uc1: 12 }, T("o", 198.61) + 0.2,
    0.2, false), "C");

  // ---------------- 35–36 kanca cümlesi geri gelir (201,34 «Kanca»; 203,33 «I get up …») ----------------
  S.koy(S.darbeler(kutu(110, 130, 900, 170, 33), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, T("Kanca", 201),
    0.14, 0.1, 0.55));
  const kanca = S.koy(S.cumleYaz({ sozcukler: S.dizi("I", 202.99, 7), x: 150, y: 240, maxGen: 860,
    font: "700 52px Fredoka", satirH: 84, satirSay: [7], bosluk: 4 }));
  const kk = kanca.kel;                            // 0 I 1 get 2 up 3 at 4 seven 5 every 6 morning.
  // 204,53 «every»: every morning sarı halka (kalıcı)
  S.koy(S.halka(kk[5], T("morning.", 204.51), 0.45, 23, 6, kk[6]));
  // 205,6: yanlış kalıp I am getting up + çarpı (mürekkep); 209,82 «I get up»: çarpı söner, yeşil tik gelir
  const wA = olc("700 52px Fredoka", "I am getting up");
  koy(S.metinPop({ parca: [["I am getting up", IKINCIL]], x: 1180, y: 240, font: "700 52px Fredoka", tb: 205.26,
    sure: 0.3, olcek0: 0.9, ses: false }), "D");
  const t209 = T("I", 209.88);
  const capraz = [S.darbe([[1170, 195], [1180 + wA + 10, 262]], { duz: true, w: 7, renk: KREM, uc0: 8, uc1: 12 },
    205.61, 0.2, 0.5),
    S.darbe([[1180 + wA + 10, 195], [1170, 262]], { duz: true, w: 7, renk: KREM, uc0: 8, uc1: 12 }, 205.81, 0.2,
      false)];
  koy(capraz.map((e) => sondur(e, t209, t209 + 0.3)));
  S.koy(S.darbe([[1040, 220], [1070, 255], [1130, 180]], { duz: true, w: 11, renk: YESIL, alfa: 0.95, uc0: 8,
    uc1: 12 }, t209 + 0.1, 0.3, 0.6));
  // 208,33 «rutin»: Caveat etiket kartın altında (214,3'te söner)
  koy(S.elYazisi({ metin: "rutin", x: 150, y: 380, boy: 64, renk: SARI, sozcukler: pen("rutin.", 208.11, 1) }), "D");
  // 211,35 «Ing yok» · 212,81 «am yok»: -ing ve am çarpılı
  const FS2 = "700 72px Fredoka";
  const yokluk = (m, x, tYaz, tCarpi) => {
    const w = olc(FS2, m);
    koy(S.metinPop({ parca: [[m, IKINCIL]], x, y: 560, font: FS2, tb: tYaz, sure: 0.25, olcek0: 0.9, ses: 0.5,
      turu: "tik" }), "D");
    koy(S.darbe([[x - 8, 500], [x + w + 8, 575]], { duz: true, w: 8, renk: KREM, uc0: 8, uc1: 12 }, tCarpi, 0.2,
      0.5), "D");
    koy(S.darbe([[x + w + 8, 500], [x - 8, 575]], { duz: true, w: 8, renk: KREM, uc0: 8, uc1: 12 }, tCarpi + 0.2,
      0.2, false), "D");
  };
  yokluk("-ing", 330, T("Ing", 211.33), T("yok,", 212.38));
  yokluk("am", 650, T("am", 213.35), T("yok.", 213.92));

  // ---------------- 38 (214,65–219,05) kural: ek değil, anlam; zaman sözcüğü sarı ----------------
  const FK = "700 110px Fredoka", FA = "700 130px Fredoka";
  const wEk = olc(FK, "ek değil,"), wAn = olc(FA, "anlam");
  const tEk = T("ekine", 216.47);
  S.koy(S.metinPop({ parca: [["ek değil,", IKINCIL]], x: 960 - wEk / 2, y: 640, font: FK, tb: tEk, sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.darbe([[960 - wEk / 2 - 10, 612], [960 + wEk / 2 + 10, 604]], { duz: true, w: 9, renk: KREM, uc0: 8,
    uc1: 12 }, T("değil,", 216.79), 0.3, 0.5));
  // 216,89 «zaman»: kartta every morning halkası parlar
  S.koy(S.parilti((kk[5].x + kk[6].x + kk[6].w) / 2, kk[5].y - 70, T("zaman", 217.43), 26));
  S.koy(S.metinPop({ parca: [["anlam", SARI]], x: 960 - wAn / 2, y: 820, font: FA, tb: T("anlama", 218.71),
    sure: 0.3, olcek0: 0.8, ses: 0.7, turu: "vurus" }));
}

surucu(kur, (f) => S.kare(f), KARE);

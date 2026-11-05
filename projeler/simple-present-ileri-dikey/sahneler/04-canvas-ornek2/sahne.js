// SAHNE 04 (İLERİ, DİKEY 1080x1920) — Örnek 2 (düz canvas, 487 kare, t_bas 32,45; cümle 4). Zaman yalnız kare numarasından.
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (sahne-ortak.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–722) · TR 3 satır (740–930) · sahne 940–1370 (43,5'te 0,42'ye toplanır, sol) · durum fiili kutusu
// (sağ, 950–1100) · formül kartı (1135–1390).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 487, TBAS = 32.45, ICERIK = 475;
const KOKDIZ = "/projeler/simple-present-ileri-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;

async function kur() {
  await S.kur();
  const [araba, otobus] = await Promise.all([svgOku("coco/car.svg"), svgOku("coco/bus.svg")]);

  // 33,00: kart çerçevesi (el kutusu, 4 px). İlk 12 kare boş: künye hazır, tuval boş.
  S.koy(S.darbeler(kutu(48, 372, 984, 350, 4), { w: 4.2, renk: IKINCIL, uc0: 10, uc1: 18 }, 33.0, 0.2, 0.14, 0.55));

  // 34,13–39,17 İngilizce kök (Fredoka 64, sözcük zamanlı, 4 satır: 4 / 4 / 4 / 3 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Mike", 34.13, 15), x: 88, y: 452, maxGen: 904, font: "700 64px Fredoka",
    satirH: 78, satirSay: [4, 4, 4, 3], bosluk: 4 }));
  const kel = (i) => cum.kel[i];             // satır 1: 0 Mike … 3 cars, | 2: 4 but … 7 takes | 3: 8 the … 11 parking | 4: 12 costs 13 so 14 much.
  const cevre = (i, tb, egim, tohum) => {                          // tek sözcüğe sarı daire (turuncu belirteç)
    const A = kel(i);
    S.koy(S.darbe(elips(A.x + A.w / 2, A.y - 24, A.w / 2 + 12, 48, egim, tohum),
      { w: 9, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, tb, 0.4, 0.55));
  };
  cevre(1, 34.62, -0.03, 11);                                      // owns
  cevre(12, 38.28, -0.03, 13);                                     // costs
  {                                                                // usually: kalıcı sarı alt çizgi
    const u = kel(6);
    S.koy(S.darbe(altCizgi(u.x - 4, u.x + u.w + 4, u.y + 17, 55), { w: 10, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14, tohum: 3 }, 36.55, 0.3, 0.55));
  }

  // 34,13–39,77 ORTA sahne (940–1370): araba 420 px + otobüs 420 px, ok; 43,5'te sola 0,42 toplanır
  const sahne = [];
  sahne.push(S.cizim({ svg: araba, ad: "araba", kutu: { x: 48, y: 880, w: 420, h: 420 }, enCok: 12, w: 4.4, tb: 34.6, sure: 1.0, olayEnCok: 5 }));
  sahne.push(S.cizim({ svg: otobus, ad: "otobus", kutu: { x: 612, y: 880, w: 420, h: 420 }, enCok: 14, w: 4.4, tb: 37.4, sure: 1.2, olayEnCok: 5 }));
  sahne.push(...S.darbeler(ok([486, 1090], [596, 1090], 4), { w: 9, renk: SARI, uc0: 10, uc1: 14 }, 36.4, 0.2, 0.14, 0.5));
  S.koy(S.grup(sahne, { f0: S.fr(43.5), f1: S.fr(44.2), ax: 200, ay: 940, olcek: 0.42, dy: 0 }));
  S.koy(S.parilti(960, 980, 39.4, 30));

  // 39,90–42,94 Türkçe çeviri (Caveat 64 mürekkep, 3 satır, ≤ 24 karakter)
  S.koy(S.not({ parca: [["Mike'ın iki arabası var,", KREM]], x: 88, y: 790, font: "700 64px Caveat", tb: 39.9, sure: 1.1 }));
  S.koy(S.not({ parca: [["ama genellikle", KREM]], x: 88, y: 856, font: "700 64px Caveat", tb: 41.62, sure: 0.8 }));
  S.koy(S.not({ parca: [["otobüse biner.", KREM]], x: 88, y: 922, font: "700 64px Caveat", tb: 42.46, sure: 0.7 }));

  // 44,29–48,29 durum fiilleri: formül kartı (owns · costs ; is own-ing ✗), kutu "durum fiili: own · cost · know"
  const F = "700 110px Fredoka", y1 = 1244, y2 = 1362, x0 = 100;
  S.koy(S.darbeler(kutu(48, 1135, 984, 252, 6), { w: 4.2, renk: IKINCIL, uc0: 10, uc1: 18 }, 44.0, 0.14, 0.1, 0.5));
  S.koy(S.metinPop({ parca: [["owns", SARI]], x: x0, y: y1, font: F, tb: 44.29, sure: 0.35, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["  ·  ", IKINCIL], ["costs", SARI]], x: x0 + olc(F, "owns"), y: y1, font: F, tb: 45.25, sure: 0.35, ses: 0.5 }));
  cevre(1, 44.35, -0.03, 21);                                      // owns yeniden vurgulanır
  cevre(12, 45.3, -0.03, 23);                                      // costs yeniden vurgulanır
  S.koy(S.darbeler(kutu(590, 948, 442, 158, 41), { w: 5, renk: SARI, uc0: 8, uc1: 14 }, 46.05, 0.12, 0.08, 0.5));
  S.koy(S.not({ parca: [["durum fiili:", SARI]], x: 612, y: 1018, font: "700 64px Caveat", tb: 46.3, sure: 0.5, ses: 0.5 }));
  S.koy(S.not({ parca: [["own · cost · know", KREM]], x: 612, y: 1088, font: "700 64px Caveat", tb: 46.6, sure: 0.9, ses: 0.4 }));
  // is own-ing: ing kırmızı çizgiyle silinir (47,37) + büyük kırmızı ✗
  const w1 = olc(F, "is own"), w2 = olc(F, "ing");
  S.koy(S.metinPop({ parca: [["is own", KREM], ["ing", KREM]], x: x0, y: y2, font: F, tb: 46.9, sure: 0.35, ses: 0.4 }));
  S.koy(S.darbe([[x0 + w1 - 8, y2 - 38], [x0 + w1 + w2 / 2, y2 - 41], [x0 + w1 + w2 + 10, y2 - 36]],
    { duz: true, w: 12, renk: KIRMIZI, alfa: 0.9, uc0: 8, uc1: 12 }, 47.37, 0.2, 0.7));
  S.koy(S.darbeler([[[790, 1290], [880, 1372]], [[880, 1290], [790, 1372]]],
    { duz: true, w: 12, renk: KIRMIZI, alfa: 0.9, uc0: 6, uc1: 8 }, 47.62, 0.14, 0.1, 0.6));
  S.koy(S.parilti(960, 1180, 47.9, 30));
}

surucu(kur, (f) => S.kare(f), KARE);

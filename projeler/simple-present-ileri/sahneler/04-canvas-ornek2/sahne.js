// SAHNE 04 (İLERİ) — Örnek 2 (düz canvas, 487 kare, t_bas 32,45; cümle 4). Kendini çizen kalem; zaman yalnız kare numarasından.
// Kök: "Mike owns two cars, but he usually takes the bus because parking costs so much." (durum fiili, araba + otobüs).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, kutu, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 487, TBAS = 32.45, ICERIK = 475;
const KOKDIZ = "/projeler/simple-present-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;

async function kur() {
  await S.kur();
  const [araba, otobus] = await Promise.all([svgOku("coco/car.svg"), svgOku("coco/bus.svg")]);

  // 33,00–34,13 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 200, 190, 33.0));

  // 34,13–39,17 İngilizce kök (Fredoka 56, sözcük zamanlı, sarı alt çizgi kayar); satırlar 6 / 5 / 4 sözcük
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Mike", 34.13, 15), x: 140, y: 300, maxGen: 980, font: "700 56px Fredoka",
    satirH: 76, satirSay: [6, 5, 4], bosluk: 4 }));
  const kel = (i) => cum.kel[i];             // satır 1: 0 Mike … 5 he | satır 2: 6 usually … 10 because | satır 3: 11 parking … 14 much.
  S.koy(S.halka(kel(1), 34.62, 0.4, 11));                          // owns: turuncu daire
  S.koy(S.halka(kel(12), 38.28, 0.4, 13));                         // costs: turuncu daire
  {                                                                // usually: kalıcı sarı alt çizgi
    const u = kel(6);
    S.koy(S.darbe(altCizgi(u.x - 4, u.x + u.w + 4, u.y + 15, 55), { w: 8.5, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14, tohum: 3 }, 36.55, 0.3, 0.55));
  }

  // 34,13–39,77 sağ sahne: araba (300 px) = sahip, otobüs (300 px) = genellikle
  S.koy(S.cizim({ svg: araba, ad: "araba", kutu: { x: 1030, y: 190, w: 300, h: 300 }, enCok: 12, w: 3.8, tb: 34.6, sure: 1.0, olayEnCok: 5 }));
  S.koy(S.cizim({ svg: otobus, ad: "otobus", kutu: { x: 1520, y: 190, w: 300, h: 300 }, enCok: 14, w: 3.8, tb: 37.4, sure: 1.2, olayEnCok: 5 }));
  S.koy(S.darbeler(ok([1345, 340], [1500, 340], 4), { w: 7, renk: SARI, uc0: 10, uc1: 14 }, 36.4, 0.2, 0.14, 0.5));
  S.koy(S.metinPop({ parca: [["sahip", SARI]], x: 1180, y: 490, font: "700 48px Caveat", hiza: "orta", tb: 35.2, sure: 0.35, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["genellikle", SARI]], x: 1670, y: 490, font: "700 48px Caveat", hiza: "orta", tb: 37.9, sure: 0.35, ses: 0.5 }));
  S.koy(S.parilti(1680, 215, 39.4));

  // 39,90–42,94 Türkçe çeviri (Caveat 48 ikincil, 2 satır)
  S.koy(S.not({ parca: [["Mike'ın iki arabası var,", IKINCIL]], x: 140, y: 590, tb: 39.9, sure: 1.1 }));
  S.koy(S.not({ parca: [["ama genellikle otobüse biner.", IKINCIL]], x: 140, y: 650, tb: 41.62, sure: 1.3 }));

  // 44,29–48,29 durum fiilleri: kart (owns · costs, is owning ✗), kutu "durum fiili: own · cost · know", ing silinir
  {
    const kx = 1190, ky = 700, F = "700 60px Fredoka", y1 = ky + 90, y2 = ky + 185;
    S.koy(S.kart({ x: kx, y: ky, w: 640, h: 235, tb: 44.29, tohum: 4, satirlar: [
      { parca: [["owns", SARI], ["  ·  ", IKINCIL], ["costs", SARI]], x: kx + 60, y: y1, font: F, tb: 44.55 },
    ] }));
    S.koy(S.halka(kel(1), 44.35, 0.35, 21, 4));                    // owns yeniden vurgulanır
    S.koy(S.halka(kel(12), 45.3, 0.35, 23, 4));                    // costs yeniden vurgulanır
    // durum fiili kutusu (46,05)
    S.koy(S.darbeler(kutu(140, 790, 900, 96, 40), { w: 4, renk: SARI, uc0: 8, uc1: 14 }, 46.05, 0.12, 0.08, 0.5));
    S.koy(S.metinPop({ parca: [["durum fiili: ", SARI], ["own · cost · know", KREM]], x: 170, y: 856, font: "700 52px Fredoka",
      tb: 46.3, sure: 0.35, ses: 0.5 }));
    // is own-ing: ing kırmızı çizgiyle silinir (47,37)
    const x0 = kx + 60, w1 = olc(F, "is own"), w2 = olc(F, "ing");
    S.koy(S.metinPop({ parca: [["is own", KREM], ["ing", KREM]], x: x0, y: y2, font: F, tb: 46.9, sure: 0.35, ses: 0.4 }));
    S.koy(S.darbe([[x0 + w1 - 6, y2 - 20], [x0 + w1 + w2 / 2, y2 - 22], [x0 + w1 + w2 + 8, y2 - 18]],
      { duz: true, w: 11, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 12 }, 47.37, 0.2, 0.7));
    S.koy(S.darbeler([[[kx + 540, y2 - 52], [kx + 600, y2 + 4]], [[kx + 600, y2 - 52], [kx + 540, y2 + 4]]],
      { duz: true, w: 8, renk: KIRMIZI, alfa: 0.9, uc0: 6, uc1: 8 }, 47.62, 0.14, 0.1, 0.6));
    S.koy(S.parilti(kx + 600, ky + 40, 47.9));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

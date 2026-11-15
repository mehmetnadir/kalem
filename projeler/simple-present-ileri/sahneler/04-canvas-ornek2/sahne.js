// SAHNE 04 (İLERİ) — Örnek 2 (düz canvas, 497 kare, t_bas 33,33; cümle 4). Kendini çizen kalem; zaman yalnız kare numarasından.
// Kök: "Mike owns two cars, but he usually takes the bus because parking costs so much." (durum fiili, araba + otobüs).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, kutu, altCizgi, olc } from "./sahne-ortak.js";
import { yaziNoktalari } from "/projeler/simple-present-ileri/ortak/kalem-canvas.js";

const KARE = 497, TBAS = 33.33, ICERIK = 485;
const KOKDIZ = "/projeler/simple-present-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
// El yazısı (Caveat 700 tegaki, dalga 5b / K26): ortalı yazının x'i için genişlik glif verisinden
const eyGen = (m, b) => yaziNoktalari(m, S.EY.G, { upm: S.EY.M.unitsPerEm, asc: S.EY.M.ascender,
  boy: b, x: 0, taban: 0 }).gen;
// Sözcük penceresi: < 0,2 sn kısa pencere sonraki sözcüğün başına dek uzar (2–3 harflik sözcük)
const pen = (w) => w.map((q, i) => ({ t0: q.t0,
  t1: q.t1 - q.t0 < 0.2 && w[i + 1] ? w[i + 1].t0 : q.t1 }));

async function kur() {
  await S.kur();
  const [araba, otobus] = await Promise.all([svgOku("coco/car.svg"), svgOku("coco/bus.svg")]);

  // 33,88–35,01 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 200, 190, 33.88));

  // 35,01–40,05 İngilizce kök (Fredoka 56, sözcük zamanlı, sarı alt çizgi kayar); satırlar 6 / 5 / 4 sözcük
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Mike", 35.01, 15), x: 140, y: 300, maxGen: 980, font: "700 56px Fredoka",
    satirH: 76, satirSay: [6, 5, 4], bosluk: 4 }));
  const kel = (i) => cum.kel[i];             // satır 1: 0 Mike … 5 he | satır 2: 6 usually … 10 because | satır 3: 11 parking … 14 much.
  S.koy(S.halka(kel(1), 35.5, 0.4, 11));                          // owns: turuncu daire
  S.koy(S.halka(kel(12), 39.16, 0.4, 13));                         // costs: turuncu daire
  {                                                                // usually: kalıcı sarı alt çizgi
    const u = kel(6);
    S.koy(S.darbe(altCizgi(u.x - 4, u.x + u.w + 4, u.y + 15, 55), { w: 8.5, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14, tohum: 3 }, 37.43, 0.3, 0.55));
  }

  // 35,01–40,65 sağ sahne: araba (300 px) = sahip, otobüs (300 px) = genellikle
  S.koy(S.cizim({ svg: araba, ad: "araba", kutu: { x: 1030, y: 190, w: 300, h: 300 }, enCok: 12, w: 3.8, tb: 35.48, sure: 1.0, olayEnCok: 5 }));
  S.koy(S.cizim({ svg: otobus, ad: "otobus", kutu: { x: 1520, y: 190, w: 300, h: 300 }, enCok: 14, w: 3.8, tb: 38.28, sure: 1.2, olayEnCok: 5 }));
  S.koy(S.darbeler(ok([1345, 340], [1500, 340], 4), { w: 7, renk: SARI, uc0: 10, uc1: 14 }, 37.28, 0.2, 0.14, 0.5));
  // 36,08 `sahip` ve 38,78 `genellikle`: anlatımsız etiket, hedef 0,5 / 0,6 sn;
  // x 1180 / 1670 ortalı
  S.koy(S.elYazisi({ metin: "sahip", x: 1180 - eyGen("sahip", 48) / 2, y: 490, renk: SARI,
    tb: 36.08, sure: 0.5, ses: 0.5 }));
  S.koy(S.elYazisi({ metin: "genellikle", x: 1670 - eyGen("genellikle", 48) / 2, y: 490,
    renk: SARI, tb: 38.78, sure: 0.6, ses: 0.5 }));
  S.koy(S.parilti(1680, 215, 40.28));

  // 40,78–45,02 Türkçe çeviri (Caveat 48 ikincil, 2 satır), her sözcük kendi konuşma penceresinde
  // (Mike'ın 40,78 · iki 41,26 · arabası 41,50 · var, 42,02 |
  // ama 42,50 · genellikle 42,78 · otobüse 43,34 · biner. 43,82)
  S.koy(S.elYazisi({ metin: "Mike'ın iki arabası var,", x: 140, y: 590, renk: IKINCIL,
    sozcukler: pen(S.dizi("Mike'ın", 40.78, 4)) }));
  S.koy(S.elYazisi({ metin: "ama genellikle otobüse biner.", x: 140, y: 650, renk: IKINCIL,
    sozcukler: pen(S.dizi("ama", 42.5, 4)) }));

  // 45,17–49,49 «Owns ve costs burada durum anlatır: -ing almaz.» (DUZ3 16.11): kart (owns · costs, is owning ✗),
  // kutu "durum anlamı: own · cost · know", ing silinir
  {
    const kx = 1190, ky = 700, F = "700 60px Fredoka", y1 = ky + 90, y2 = ky + 185;
    S.koy(S.kart({ x: kx, y: ky, w: 640, h: 235, tb: 45.17, tohum: 4, satirlar: [
      { parca: [["owns", SARI], ["  ·  ", IKINCIL], ["costs", SARI]], x: kx + 60, y: y1, font: F, tb: 45.43 },
    ] }));
    S.koy(S.halka(kel(1), 45.23, 0.35, 21, 4));                    // owns yeniden vurgulanır
    S.koy(S.halka(kel(12), 46.18, 0.35, 23, 4));                    // costs yeniden vurgulanır
    // durum anlamı kutusu (durum 47,41)
    S.koy(S.darbeler(kutu(140, 790, 900, 96, 40), { w: 4, renk: SARI, uc0: 8, uc1: 14 }, 47.41, 0.12, 0.08, 0.5));
    S.koy(S.metinPop({ parca: [["durum anlamı: ", SARI], ["own · cost · know", KREM]], x: 170, y: 856, font: "700 52px Fredoka",
      tb: 47.66, sure: 0.35, ses: 0.5 }));
    // is own-ing: ing kırmızı çizgiyle silinir (-ing 48,57)
    const x0 = kx + 60, w1 = olc(F, "is own"), w2 = olc(F, "ing");
    S.koy(S.metinPop({ parca: [["is own", KREM], ["ing", KREM]], x: x0, y: y2, font: F, tb: 48.1, sure: 0.35, ses: 0.4 }));
    S.koy(S.darbe([[x0 + w1 - 6, y2 - 20], [x0 + w1 + w2 / 2, y2 - 22], [x0 + w1 + w2 + 8, y2 - 18]],
      { duz: true, w: 11, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 12 }, 48.57, 0.2, 0.7));
    S.koy(S.darbeler([[[kx + 540, y2 - 52], [kx + 600, y2 + 4]], [[kx + 600, y2 - 52], [kx + 540, y2 + 4]]],
      { duz: true, w: 8, renk: KIRMIZI, alfa: 0.9, uc0: 6, uc1: 8 }, 48.82, 0.14, 0.1, 0.6));
    S.koy(S.parilti(kx + 600, ky + 40, 49.1));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

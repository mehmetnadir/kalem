// SAHNE 04 — Örnek 2 (düz canvas, 482 kare, t_bas 27,69; cümle 4). Kendini çizen kalem; zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, kutu, ok, olc } from "./sahne-ortak.js";

const KARE = 482, TBAS = 27.69, ICERIK = 470;
const KOKDIZ = "/projeler/simple-present-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const TIK = (cx, cy) => [[cx - 14, cy + 1], [cx - 4, cy + 12], [cx + 17, cy - 15]];

async function kur() {
  await S.kur();
  const [kardes, otobus] = await Promise.all([svgOku("open-peeps/sitting-4.svg"), svgOku("coco/bus.svg")]);

  // 28,24–29,53 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 190, 205, 28.24));

  // 29,53–32,01 cümle + sarı alt çizgi (sözcük sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("My", 29.53, 8), x: 140, y: 330, maxGen: 980 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 29,53–32,81 sağ: oturan figür + otobüs
  S.koy(S.cizim({ svg: kardes, kutu: { x: 1030, y: 190, w: 380, h: 540 }, ad: "kardes", esik: 0.004, enCok: 60, w: 3.2,
    tb: 29.6, sure: 1.7, olayEnCok: 7 }));
  S.koy(S.cizim({ svg: otobus, kutu: { x: 1420, y: 400, w: 430, h: 330 }, ad: "otobus", enCok: 25, w: 3.8,
    tb: 31.3, sure: 1.1, olayEnCok: 5 }));
  S.koy(S.darbe([[1030, 736], [1300, 733], [1560, 738], [1850, 735]], { duz: true, w: 3.4, renk: IKINCIL, alfa: 0.75, uc0: 10, uc1: 30 },
    32.3, 0.7, 0.4));

  // usually ayrıca sarı daire (söylendikten hemen sonra)
  S.koy(S.halka(kel("usually"), 30.55, 0.35, 11));

  // 32,74–38,53 Türkçe çeviri (Caveat 48)
  const ytr = sonSatir + 78;
  S.koy(S.not({ parca: [["Kardeşim genellikle okula otobüsle gider.", IKINCIL]], x: 140, y: ytr, tb: 32.74, sure: 1.6 }));

  // 35,53–41,36 etiketler el kutusunda tik: usually · always · every day
  const yE = ytr + 62, eh = 76, FE = "700 38px Lexend";
  let ex = 140;
  [["usually", 35.53], ["always", 36.73], ["every day", 37.45]].forEach(([m, tb], i) => {
    const w = olc(FE, m) + 48 + 52;
    S.darbeler(kutu(ex, yE, w, eh, 30 + i), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, tb, 0.12, 0.08, 0.5).forEach((e) => S.koy(e));
    S.koy(S.metinPop({ parca: [[m, KREM]], x: ex + 24, y: yE + 52, font: FE, tb: tb + 0.2, sure: 0.3 }));
    S.koy(S.darbe(TIK(ex + w - 34, yE + 40), { w: 7, renk: SARI, alfa: 0.9, uc0: 5, uc1: 8 }, tb + 0.55, 0.16, 0.5));
    ex += w + 26;
  });

  // 37,69–41,36 altında 5 küçük gün kutusu (el çizimi), her günde tik
  const yG = yE + eh + 50, gh = 84, gw = 120, FG = "500 28px Lexend";
  ["Pzt", "Sal", "Çar", "Per", "Cum"].forEach((g, i) => {
    const x = 140 + i * (gw + 24), tb = 37.9 + i * 0.16;
    S.darbeler(kutu(x, yG, gw, gh, 40 + i), { w: 3.4, renk: KREM, uc0: 8, uc1: 14 }, tb, 0.1, 0.06, i === 0 ? 0.5 : false)
      .forEach((e) => S.koy(e));
    S.koy(S.metinPop({ parca: [[g, IKINCIL]], x: x + gw / 2, y: yG + 34, font: FG, hiza: "orta", tb: tb + 0.2, sure: 0.25 }));
    S.koy(S.darbe(TIK(x + gw / 2, yG + 62), { w: 6, renk: SARI, alfa: 0.9, uc0: 5, uc1: 8 }, 38.9 + i * 0.12, 0.14, i === 0 ? 0.5 : false));
  });

  // 40,96–43,36 goes sarı daire; formül kartı: he + go → go-es
  S.koy(S.halka(kel("goes"), 40.96, 0.35, 12));
  const kx = 1040, ky = 800, F = "700 64px Fredoka", yy = ky + 92;
  S.darbeler(kutu(kx, ky, 790, 140, 4), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, 41.35, 0.14, 0.1, 0.55).forEach((e) => S.koy(e));
  S.koy(S.metinPop({ parca: [["he", KREM]], x: kx + 50, y: yy, font: F, tb: 41.7, sure: 0.3, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["+", IKINCIL]], x: kx + 150, y: yy, font: F, tb: 41.95, sure: 0.25 }));
  S.koy(S.metinPop({ parca: [["go", KREM]], x: kx + 225, y: yy, font: F, tb: 42.1, sure: 0.3 }));
  S.darbeler(ok([kx + 340, yy - 24], [kx + 440, yy - 24], 3), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 42.25, 0.14, 0.1, 0.5).forEach((e) => S.koy(e));
  S.koy(S.metinPop({ parca: [["go", KREM]], x: kx + 480, y: yy, font: F, tb: 42.45, sure: 0.3 }));
  S.koy(S.metinPop({ parca: [["-es", SARI]], x: kx + 480 + olc(F, "go") + 4, y: yy, font: F, tb: 42.6, sure: 0.3, ses: 0.5 }));
  S.koy(S.parilti(kx + 740, ky + 20, 42.85));
}

surucu(kur, (f) => S.kare(f), KARE);

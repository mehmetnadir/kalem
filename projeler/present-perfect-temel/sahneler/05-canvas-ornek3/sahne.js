// SAHNE 05 — Örnek 3 (düz canvas, 482 kare, t_bas 52,56; cümle 5; çıkış geçişi fade). Zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, kutu, ok, elips, olc } from "./sahne-ortak.js";

const KARE = 482, TBAS = 52.56, ICERIK = 470;
const KOKDIZ = "/projeler/present-perfect-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

async function kur() {
  await S.kur();
  const [ucak, kisi] = await Promise.all([svgOku("coco/plane.svg"), svgOku("open-peeps/standing-1.svg")]);

  // 53,11–53,9 daire içinde 3 (16.11 DUZ3 sesi; bütün sabitler yeni sözcük zamanlarında)
  S.koy(S.daireSayi(3, 190, 205, 53.11));

  // 54,40–56,64 cümle (sözcük zamanında) + sarı alt çizgi; never sarı daire 54,88
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("I", 54.40, 7), x: 140, y: 340, maxGen: 640 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y)), kel = (ad) => cum.kel.find((k) => k.m === ad);
  S.koy(S.halka(kel("never"), 54.88, 0.3, 31));

  // 54,52–56,5 sağ: uçak (440 px geniş) + yanında ayakta figür
  const UX = 1020, UY = 330, UW = 560, UH = 300;
  S.koy(S.cizim({ svg: ucak, kutu: { x: UX, y: UY, w: UW, h: UH }, ad: "ucak", esik: 0.01, enCok: 30,
    w: 3.8, tb: 54.52, sure: 1.3, olayEnCok: 6 }));
  S.koy(S.cizim({ svg: kisi, kutu: { x: 1650, y: 190, w: 200, h: 660 }, ad: "kisi", esik: 0.01, enCok: 60, w: 3.4,
    tb: 55.12, sure: 1.4, olayEnCok: 6 }));
  S.koy(S.parilti(UX + UW - 40, UY - 20, 56.02, 26));

  // 56,81–60,0 Türkçe çeviri; uçak üstüne sarı çarpı 58,34
  const ytr = sonSatir + 78;
  // pencere: Hayatımda 56,81–57,45 · hiç 57,53–57,65 · uçağa 57,69–58,01 · binmedim. –58,86
  S.koy(S.elYazisi({ metin: "Hayatımda hiç uçağa binmedim.", x: 140, y: ytr, renk: IKINCIL,
    sozcukler: S.dizi("Hayatımda", 56.81, 4).map((w) => ({ t0: w.t0, t1: w.t1 })) }));
  const cx0 = UX + UW / 2, cy0 = UY + UH / 2;
  S.koy(S.darbe([[cx0 - 190, cy0 - 120], [cx0, cy0], [cx0 + 190, cy0 + 120]],
    { duz: true, w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 71 }, 58.34, 0.22, 0.7));
  S.koy(S.darbe([[cx0 + 190, cy0 - 120], [cx0, cy0], [cx0 - 190, cy0 + 120]],
    { duz: true, w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 72 }, 58.54, 0.22, 0.7));

  // 58,92–61,0 yaşam çizgisi: birth ●━━━━━● now, sarı bant kapatır
  const ly = ytr + 120, bx = 170, nx = 880;
  S.koy(S.darbe(elips(bx, ly, 9, 9, 0, 33), { w: 16, uc0: 3, uc1: 3, tohum: 33 }, 58.92, 0.2, 0.5));
  S.koy(S.elYazisi({ metin: "birth", x: bx - 30, y: ly - 28, boy: 44, renk: IKINCIL, tb: 58.99,
    sure: 0.45, ses: false }));
  S.koy(S.darbe([[bx + 14, ly], [(bx + nx) / 2, ly - 3], [nx - 14, ly + 1]],
    { duz: true, w: 4.2, uc0: 8, uc1: 14, tohum: 34 }, 59.17, 0.5, 0.55));
  S.koy(S.darbe(elips(nx, ly, 9, 9, 0, 35), { w: 16, uc0: 3, uc1: 3, tohum: 35 }, 59.61, 0.2, 0.5));
  S.koy(S.elYazisi({ metin: "now", x: nx - 24, y: ly - 28, boy: 44, renk: SARI, tb: 59.67,
    sure: 0.45, ses: false }));
  S.koy(S.darbe([[bx - 14, ly + 1], [(bx + nx) / 2, ly - 2], [nx + 14, ly]],
    { duz: true, w: 24, renk: SARI, alfa: 0.3, uc0: 20, uc1: 30, tohum: 36 }, 59.92, 1.0, 0.5));
  // pencere: Bugüne 58,92–59,13 · kadar 59,17–59,53 · hiç 59,61–59,77 (anlatımla eş zamanlı)
  S.koy(S.elYazisi({ metin: "bugüne kadar hiç", x: bx, y: ly + 62, renk: KREM,
    sozcukler: S.dizi("Bugüne", 58.92, 3).map((w) => ({ t0: w.t0, t1: w.t1 })) }));

  // 61,12–65,2 etiket (el kutusu + tik): never 61,84 (16.11: ses "Burada never …"; ever ve just etiketi kalktı)
  const yb = ly + 100, bh = 62, lfn = "700 34px Lexend";
  let xx = 140;
  [["never", 61.84]].forEach(([m, tb], i) => {
    const w = olc(lfn, m) + 44;
    S.koy(S.darbeler(kutu(xx, yb, w, bh, 30 + i), { w: 3.4, renk: KREM, uc0: 8, uc1: 14 }, tb, 0.1, 0.06, false));
    S.koy(S.metinPop({ parca: [[m, KREM]], x: xx + 22, y: yb + 43, font: lfn, tb: tb + 0.22, sure: 0.3, ses: 0.5 }));
    xx += w + 28;
  });
  // 63,12–64,3 sarı ok → now noktası (bugüne), nabız (kadarki)
  S.koy(S.darbeler(ok([xx - 10, yb + 20], [nx - 12, ly + 26], 5), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 },
    63.12, 0.3, 0.2, 0.55));
  S.koy(S.nabiz(nx, ly, 12, 63.52));

  // 65,35–68,23 have / flown sarı daire; formül kartı have + flown
  S.koy(S.halka(kel("flown"), 67.51, 0.3, 32));
  const ky = yb + bh + 50, fo = "700 72px Fredoka";
  S.koy(S.kart({ x: 140, y: ky, w: 640, h: 150, tb: 65.56, tohum: 7, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [
    { parca: [["have", KREM]], x: 190, y: ky + 98, font: fo, tb: 65.99, sure: 0.3 },
    { parca: [["+", IKINCIL]], x: 410, y: ky + 98, font: fo, tb: 66.87, sure: 0.3 },
    { parca: [["flown", SARI]], x: 490, y: ky + 98, font: fo, tb: 67.51, sure: 0.3 },
  ] }));
  S.koy(S.halka(kel("have"), 65.99, 0.3, 31 + 7));
}

surucu(kur, (f) => S.kare(f), KARE);

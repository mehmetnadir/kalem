// SAHNE 05 — Örnek 3 (düz canvas, 494 kare, t_bas 51,12; cümle 5; çıkış geçişi fade). Zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, kutu, ok, elips, olc } from "./sahne-ortak.js";

const KARE = 494, TBAS = 51.12, ICERIK = 482;
const KOKDIZ = "/projeler/present-perfect-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

async function kur() {
  await S.kur();
  const [ucak, kisi] = await Promise.all([svgOku("coco/plane.svg"), svgOku("open-peeps/standing-1.svg")]);

  // 51,67–52,5 daire içinde 3
  S.koy(S.daireSayi(3, 190, 205, 51.67));

  // 52,88–54,4 cümle (sözcük zamanında) + sarı alt çizgi; never sarı daire 53,28
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("I", 52.88, 7), x: 140, y: 340, maxGen: 640 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y)), kel = (ad) => cum.kel.find((k) => k.m === ad);
  S.koy(S.halka(kel("never"), 53.28, 0.3, 31));

  // 53,0–55,0 sağ: uçak (440 px geniş) + yanında ayakta figür
  const UX = 1020, UY = 330, UW = 560, UH = 300;
  S.koy(S.cizim({ svg: ucak, kutu: { x: UX, y: UY, w: UW, h: UH }, ad: "ucak", esik: 0.01, enCok: 30,
    w: 3.8, tb: 53.0, sure: 1.3, olayEnCok: 6 }));
  S.koy(S.cizim({ svg: kisi, kutu: { x: 1650, y: 190, w: 200, h: 660 }, ad: "kisi", esik: 0.01, enCok: 60, w: 3.4,
    tb: 53.6, sure: 1.4, olayEnCok: 6 }));
  S.koy(S.parilti(UX + UW - 40, UY - 20, 54.5, 26));

  // 55,37–58,6 Türkçe çeviri; uçak üstüne sarı çarpı 56,9
  const ytr = sonSatir + 78;
  // pencere: Hayatımda 55,37–55,93 · hiç 56,01–56,21 · uçağa 56,25–56,57 · binmedim. –57,42
  S.koy(S.elYazisi({ metin: "Hayatımda hiç uçağa binmedim.", x: 140, y: ytr, renk: IKINCIL,
    sozcukler: S.dizi("Hayatımda", 55.37, 4).map((w) => ({ t0: w.t0, t1: w.t1 })) }));
  const cx0 = UX + UW / 2, cy0 = UY + UH / 2;
  S.koy(S.darbe([[cx0 - 190, cy0 - 120], [cx0, cy0], [cx0 + 190, cy0 + 120]],
    { duz: true, w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 71 }, 56.9, 0.22, 0.7));
  S.koy(S.darbe([[cx0 + 190, cy0 - 120], [cx0, cy0], [cx0 - 190, cy0 + 120]],
    { duz: true, w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 72 }, 57.1, 0.22, 0.7));

  // 57,48–59,5 yaşam çizgisi: birth ●━━━━━● now, sarı bant kapatır
  const ly = ytr + 120, bx = 170, nx = 880;
  S.koy(S.darbe(elips(bx, ly, 9, 9, 0, 33), { w: 16, uc0: 3, uc1: 3, tohum: 33 }, 57.48, 0.2, 0.5));
  S.koy(S.elYazisi({ metin: "birth", x: bx - 30, y: ly - 28, boy: 44, renk: IKINCIL, tb: 57.55,
    sure: 0.45, ses: false }));
  S.koy(S.darbe([[bx + 14, ly], [(bx + nx) / 2, ly - 3], [nx - 14, ly + 1]],
    { duz: true, w: 4.2, uc0: 8, uc1: 14, tohum: 34 }, 57.73, 0.5, 0.55));
  S.koy(S.darbe(elips(nx, ly, 9, 9, 0, 35), { w: 16, uc0: 3, uc1: 3, tohum: 35 }, 58.09, 0.2, 0.5));
  S.koy(S.elYazisi({ metin: "now", x: nx - 24, y: ly - 28, boy: 44, renk: SARI, tb: 58.15,
    sure: 0.45, ses: false }));
  S.koy(S.darbe([[bx - 14, ly + 1], [(bx + nx) / 2, ly - 2], [nx + 14, ly]],
    { duz: true, w: 24, renk: SARI, alfa: 0.3, uc0: 20, uc1: 30, tohum: 36 }, 58.4, 1.0, 0.5));
  // pencere: Bugüne 57,48–57,69 · kadar 57,73–58,01 · hiç 58,09–58,29 (anlatımla eş zamanlı)
  S.koy(S.elYazisi({ metin: "bugüne kadar hiç", x: bx, y: ly + 62, renk: KREM,
    sozcukler: S.dizi("Bugüne", 57.48, 3).map((w) => ({ t0: w.t0, t1: w.t1 })) }));

  // 59,68–63,8 etiketler (el kutusu + tik): never 60,40 · ever 61,52 · just 62,48
  const yb = ly + 100, bh = 62, lfn = "700 34px Lexend";
  let xx = 140;
  [["never", 60.40], ["ever", 61.52], ["just", 62.48]].forEach(([m, tb], i) => {
    const w = olc(lfn, m) + 44;
    S.koy(S.darbeler(kutu(xx, yb, w, bh, 30 + i), { w: 3.4, renk: KREM, uc0: 8, uc1: 14 }, tb, 0.1, 0.06, false));
    S.koy(S.metinPop({ parca: [[m, KREM]], x: xx + 22, y: yb + 43, font: lfn, tb: tb + 0.22, sure: 0.3, ses: 0.5 }));
    xx += w + 28;
  });
  // 62,8–63,9 sarı ok → now noktası, nabız
  S.koy(S.darbeler(ok([xx - 10, yb + 20], [nx - 12, ly + 26], 5), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 },
    62.8, 0.3, 0.2, 0.55));
  S.koy(S.nabiz(nx, ly, 12, 63.5));

  // 63,99–67,19 have / flown sarı daire; formül kartı have + flown
  S.koy(S.halka(kel("flown"), 66.39, 0.3, 32));
  const ky = yb + bh + 50, fo = "700 72px Fredoka";
  S.koy(S.kart({ x: 140, y: ky, w: 640, h: 150, tb: 64.2, tohum: 7, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [
    { parca: [["have", KREM]], x: 190, y: ky + 98, font: fo, tb: 64.87, sure: 0.3 },
    { parca: [["+", IKINCIL]], x: 410, y: ky + 98, font: fo, tb: 65.67, sure: 0.3 },
    { parca: [["flown", SARI]], x: 490, y: ky + 98, font: fo, tb: 66.39, sure: 0.3 },
  ] }));
  S.koy(S.halka(kel("have"), 64.87, 0.3, 31 + 7));
}

surucu(kur, (f) => S.kare(f), KARE);

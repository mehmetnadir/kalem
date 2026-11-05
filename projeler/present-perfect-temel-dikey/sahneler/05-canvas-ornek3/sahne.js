// SAHNE 05 (DİKEY) — Örnek 3: düz canvas, 494 kare, t_bas 51,12; cümle 5. Zaman yalnız kare numarasından.
// Yerleşim BRIEF-DIKEY §4: kart (cümle) -> TR çeviri -> uçak + çarpı -> yaşam çizgisi -> etiketler -> formül.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, kutu, ok, elips, olc } from "./sahne-ortak.js";

const KARE = 494, TBAS = 51.12, ICERIK = 482;
const KOKDIZ = "/projeler/present-perfect-temel-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const ucak = await svgOku("coco/plane.svg");

  // Kart (tam genişlik 984, iç boşluk 40): cümle sözcük zamanında; never sarı daire 53,28
  S.koy(S.darbeler(kutu(48, 372, 984, 232, 11), { w: 4, renk: IKINCIL, uc0: 10, uc1: 16 }, 51.67, 0.12, 0.1, 0.5));
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("I", 52.88, 7), x: 88, y: 470, maxGen: 780, font: FF(72),
    satirH: 84, bosluk: 8 }));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);
  S.koy(S.halka(kel("never"), 53.28, 0.3, 31));

  // Türkçe çeviri (Caveat 64, mürekkep) 55,37
  S.koy(S.not({ parca: [["Hayatımda hiç uçağa binmedim.", KREM]], x: 88, y: 672, font: CV(64), tb: 55.37, sure: 0.6 }));

  // ORTA: uçak (640 x 340) 53,0; sarı çarpı 56,9
  const UX = 220, UY = 704, UW = 640, UH = 340;
  S.koy(S.cizim({ svg: ucak, kutu: { x: UX, y: UY, w: UW, h: UH }, ad: "ucak", esik: 0.01, enCok: 30, w: 4.4,
    tb: 53.0, sure: 1.3, olayEnCok: 6 }));
  S.koy(S.parilti(UX + UW - 20, UY + 10, 54.4, 32));
  const cx0 = UX + UW / 2, cy0 = UY + UH / 2;
  S.koy(S.darbe([[cx0 - 230, cy0 - 125], [cx0, cy0], [cx0 + 230, cy0 + 125]],
    { duz: true, w: 11, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 71 }, 56.9, 0.22, 0.7));
  S.koy(S.darbe([[cx0 + 230, cy0 - 125], [cx0, cy0], [cx0 - 230, cy0 + 125]],
    { duz: true, w: 11, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 72 }, 57.1, 0.22, 0.7));

  // Yaşam çizgisi: birth ● ━━ ● now (57,48–59,5); orta metin 58,09; sarı bant kapatır
  const ly = 1160, bx = 110, nx = 970, ey = ly - 36;
  S.koy(S.darbe(elips(bx, ly, 10, 10, 0, 33), { w: 18, uc0: 3, uc1: 3, tohum: 33 }, 57.48, 0.2, 0.5));
  S.koy(S.not({ parca: [["birth", KREM]], x: 56, y: ey, font: CV(64), tb: 57.55, sure: 0.3, ses: false }));
  S.koy(S.darbe([[bx + 16, ly], [(bx + nx) / 2, ly - 3], [nx - 16, ly + 1]],
    { duz: true, w: 5, uc0: 8, uc1: 14, tohum: 34 }, 57.73, 0.5, 0.55));
  S.koy(S.darbe(elips(nx, ly, 10, 10, 0, 35), { w: 18, uc0: 3, uc1: 3, tohum: 35 }, 58.09, 0.2, 0.5));
  S.koy(S.not({ parca: [["now", SARI]], x: 892, y: ey, font: CV(64), tb: 58.15, sure: 0.3, ses: false }));
  const mf = CV(64), mw = olc(mf, "bugüne kadar hiç");
  S.koy(S.not({ parca: [["bugüne kadar hiç", KREM]], x: 540 - mw / 2 - 10, y: ey, font: mf, tb: 58.1, sure: 0.5 }));
  S.koy(S.darbe([[bx - 16, ly + 1], [(bx + nx) / 2, ly - 2], [nx + 16, ly]],
    { duz: true, w: 30, renk: SARI, alfa: 0.3, uc0: 24, uc1: 36, tohum: 36 }, 58.4, 1.0, 0.5));

  // Etiketler (Caveat 64, el kutusu + tik): never 60,40 · ever 61,52 · just 62,48
  const yb = 1196, bh = 76, lfn = CV(64), boslar = [["never", 60.40], ["ever", 61.52], ["just", 62.48]];
  const gen = boslar.map(([m]) => olc(lfn, m) + 56), top = gen.reduce((a, b) => a + b, 0) + 24 * 2;
  let xx = 540 - top / 2;
  boslar.forEach(([m, tb], i) => {
    const w = gen[i];
    S.koy(S.darbeler(kutu(xx, yb, w, bh, 30 + i), { w: 4, renk: KREM, uc0: 8, uc1: 14 }, tb, 0.1, 0.06, false));
    S.koy(S.metinPop({ parca: [[m, KREM]], x: xx + 28, y: yb + 56, font: lfn, tb: tb + 0.22, sure: 0.3, ses: 0.5 }));
    xx += w + 24;
  });
  // 62,8 sarı ok -> now noktası, nabız
  S.koy(S.darbeler(ok([xx - 10, yb + 20], [nx - 6, ly + 24], 5), { w: 9, renk: SARI, uc0: 10, uc1: 14 },
    62.8, 0.3, 0.2, 0.55));
  S.koy(S.nabiz(nx, ly, 14, 63.5));

  // 64,87 have, 66,39 flown sarı daire; formül have + flown (Fredoka 110)
  S.koy(S.halka(kel("have"), 64.87, 0.3, 38));
  S.koy(S.halka(kel("flown"), 66.39, 0.3, 32));
  const fo = FF(110), p1 = "have", p2 = " + ", p3 = "flown", fy = 1366;
  const toplam = olc(fo, p1) + olc(fo, p2) + olc(fo, p3);
  let fx = 540 - toplam / 2;
  S.koy(S.metinPop({ parca: [[p1, KREM]], x: fx, y: fy, font: fo, tb: 64.87, sure: 0.35, ses: 0.8, turu: "vurus" }));
  fx += olc(fo, p1);
  S.koy(S.metinPop({ parca: [[p2, IKINCIL]], x: fx, y: fy, font: fo, tb: 65.67, sure: 0.3, ses: false }));
  fx += olc(fo, p2);
  S.koy(S.metinPop({ parca: [[p3, SARI]], x: fx, y: fy, font: fo, tb: 66.39, sure: 0.35, ses: 0.8, turu: "vurus" }));
}

surucu(kur, (f) => S.kare(f), KARE);

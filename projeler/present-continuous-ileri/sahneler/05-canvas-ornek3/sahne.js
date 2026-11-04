// SAHNE 05 — Örnek 3 (düz canvas, 372 kare, t_bas 42,07; cümle 5; çıkış geçişi fade). İLERİ seviye.
// Zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json (küresel sn).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, elips, altCizgi, kutu, olc } from "./sahne-ortak.js";

const KARE = 372, TBAS = 42.07, ICERIK = 360;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5 });
const KOKDIZ = "/projeler/present-continuous-ileri/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const [otobus, takvim, saat, yolcu] = await Promise.all([svgOku("tabler/bus.svg"),
    svgOku("tabler/calendar.svg"), svgOku("tabler/clock.svg"), svgOku("open-peeps/standing-4.svg")]);

  // 42,62 daire içinde 3 (ilk 12 kare boş)
  S.koy(S.daireSayi(3, 190, 205, 42.62));

  // 43,83–48,79 İngilizce cümle (Fredoka 56, 3 satır, sözcük zamanlı)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("We", 43.83, 16), x: 140, y: 300, maxGen: 980,
    font: FF(56), satirH: 88 }));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));
  // iki sözcüğü kapsayan halka (aynı satırdaysa tek, değilse sözcük başına)
  const halkaIki = (a, b, tb, tohum) => {
    if (a.satir === b.satir) S.koy(S.halka({ x: a.x, y: a.y, w: b.x + b.w - a.x }, tb, 0.4, tohum));
    else { S.koy(S.halka(a, tb, 0.3, tohum)); S.koy(S.halka(b, tb + 0.16, 0.3, tohum + 1)); }
  };
  halkaIki(kel("are"), kel("taking"), 43.99, 31);                 // are taking
  halkaIki(kel("am"), kel("packing"), 46.98, 33);                 // am packing
  S.koy(S.halka(kel("tonight."), 47.83, 0.35, 35));               // tonight
  // 45,43–45,83 tomorrow morning: sarı alt çizgi (satır bölünürse her satıra)
  const tm = kel("tomorrow"), mo = kel("morning,");
  const cizgiler = tm.satir === mo.satir ? [[tm.x, mo.x + mo.w, tm.y]] : [[tm.x, tm.x + tm.w, tm.y],
    [mo.x, mo.x + mo.w, mo.y]];
  cizgiler.forEach(([x0, x1, y], i) => S.koy(S.darbe(altCizgi(x0 - 4, x1 + 4, y + 26, 51 + i),
    { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 520 + i }, 45.45 + i * 0.2, 0.4, 0.55)));

  // 43,9–47,0 sağ: otobüs (460 px) kalemle + yol çizgisi, yolcu (standing-4), üstte takvim (200 px)
  S.koy(S.cizim({ svg: otobus, ad: "otobus", kutu: { x: 1400, y: 440, w: 460, h: 460 }, enCok: 12, w: 4,
    tb: 43.95, sure: 1.2, olayEnCok: 5 }));
  S.koy(S.cizim({ svg: yolcu, ad: "yolcu", kutu: { x: 1150, y: 370, w: 230, h: 470 }, esik: 0.004, enCok: 50,
    w: 3.4, tb: 45.9, sure: 1.5, olayEnCok: 5 }));
  S.koy(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 1560, y: 130, w: 200, h: 200 }, enCok: 8, w: 4,
    tb: 45.1, sure: 0.8, olayEnCok: 3 }));
  S.koy(S.darbe([[1180, 862], [1520, 866], [1860, 861]], { duz: true, w: 3.4, renk: IKINCIL, alfa: 0.8, uc0: 6,
    uc1: 10, tohum: 77 }, 46.7, 0.45, 0.45));
  S.koy(S.parilti(1700, 560, 47.4, 26));

  // 49,04–51,04 Türkçe çeviri + takvim etiketi "yarın"
  const yTR = sonSatir + 80;
  S.koy(S.not({ parca: [["Yarın sabah İzmir'e gidiyoruz.", IKINCIL]], x: 140, y: yTR, font: CV(48), tb: 49.04,
    sure: 0.7 }));
  const yw = olc(CV(64), "yarın");
  S.koy(S.not({ parca: [["yarın", KREM]], x: 1660 - yw / 2, y: 392, font: CV(64), tb: 49.4, sure: 0.4 }));

  // 51,12–52,14 Planlı gelecek: yarın sarı daire → ok → PLAN
  S.koy(S.darbe(elips(1660, 372, yw / 2 + 26, 46, -0.04, 41), { w: 6, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 },
    51.14, 0.4, 0.55));
  S.koy(S.darbeler(ok([1540, 240], [1450, 246], 4), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 51.5, 0.3, 0.2, 0.5));
  S.koy(S.not({ parca: [["PLAN", SARI]], x: 1250, y: 262, font: CV(76), tb: 51.8, sure: 0.4 }));

  // 52,20–54,08 bilet ✓ (52,40) + saat (53,04) + formül kartı
  const bx = 140, by = 614, bw = 300, bh = 84, fb = FF(46), bwid = olc(fb, "bilet");
  S.koy(S.darbeler(kutu(bx, by, bw, bh, 61), { w: 3.6, renk: KREM, uc0: 8, uc1: 14 }, 52.22, 0.1, 0.06, false));
  S.koy(S.metinPop({ parca: [["bilet", KREM]], x: bx + 26, y: by + 58, font: fb, tb: 52.3, sure: 0.3, ses: 0.5 }));
  const tx = bx + 26 + bwid + 36;
  S.koy(S.darbe([[tx, by + 44], [tx + 22, by + 64], [tx + 62, by + 18]], { w: 8, renk: SARI, alfa: 0.9, uc0: 4,
    uc1: 10, tohum: 63 }, 52.4, 0.3, 0.55));
  S.koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 520, y: 584, w: 200, h: 200 }, enCok: 4, w: 4, tb: 52.7,
    sure: 0.6, olayEnCok: 2 }));
  S.koy(S.darbe([[740, 682], [762, 704], [808, 654]], { w: 8, renk: SARI, alfa: 0.9, uc0: 4, uc1: 10, tohum: 65 },
    53.04, 0.3, 0.55));
  const ky = 812, fo = FF(60), fo2 = FF(52);
  S.koy(S.kart({ x: 140, y: ky, w: 860, h: 170, tb: 53.4, tohum: 7, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [
    { parca: [["be", KREM]], x: 190, y: ky + 64, font: fo, tb: 53.4, sure: 0.3 },
    { parca: [["+", IKINCIL]], x: 330, y: ky + 64, font: fo, tb: 53.42, sure: 0.3 },
    { parca: [["V", KREM], ["-ing", SARI]], x: 410, y: ky + 64, font: fo, tb: 53.44, sure: 0.3 },
    { parca: [["are", KREM], [" tak", KREM], ["-ing", SARI]], x: 190, y: ky + 136, font: fo2, tb: 53.58, sure: 0.3 },
    { parca: [["am", KREM], [" pack", KREM], ["-ing", SARI]], x: 560, y: ky + 136, font: fo2, tb: 53.66,
      sure: 0.3 },
  ] }));
}

surucu(kur, (f) => S.kare(f), KARE);

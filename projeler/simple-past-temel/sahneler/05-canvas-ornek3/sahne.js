// SAHNE 05 — Örnek 3 (düz canvas, 521 kare, t_bas 47,82; cümle 5; çıkış geçişi fade). Zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, olc } from "./sahne-ortak.js";

const KARE = 521, TBAS = 47.82, ICERIK = 509;
const KOKDIZ = "/projeler/simple-past-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;

async function kur() {
  await S.kur();
  const [figur, top] = await Promise.all([svgOku("open-peeps/standing-6.svg"), svgOku("tabler/ball-football.svg")]);

  // 47,82–48,86 daire içinde 3 (ilk 12 kare boş)
  S.koy(S.daireSayi(3, 190, 205, S.zm(12)));

  // 49,11–51,27 cümle + sarı alt çizgi (didn't 49,27)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("We", 49.11, 5), x: 140, y: 330, maxGen: 980 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y)), kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 49,2–51,0 sağ: ayakta figür (standing-6) + futbol topu; topun üstüne büyük kırmızı çarpı (50,6)
  S.koy(S.cizim({ svg: figur, kutu: { x: 1500, y: 170, w: 330, h: 640 }, ad: "figur", esik: 0.004, enCok: 60,
    w: 3.2, tb: 49.2, sure: 1.8, olayEnCok: 7 }));
  S.koy(S.cizim({ svg: top, kutu: { x: 1100, y: 470, w: 360, h: 360 }, ad: "top", enCok: 6, w: 3.8, tb: 49.9,
    sure: 0.9, olayEnCok: 4 }));
  S.koy(S.darbe([[1130, 500], [1430, 800]], { duz: true, w: 14, renk: KIRMIZI, alfa: 0.92, uc0: 10, uc1: 24, tohum: 71 },
    50.55, 0.22, 0.7));
  S.koy(S.darbe([[1430, 500], [1130, 800]], { duz: true, w: 14, renk: KIRMIZI, alfa: 0.92, uc0: 10, uc1: 24, tohum: 72 },
    50.8, 0.22, 0.6));
  S.koy(S.parilti(1470, 480, 50.1, 24));

  // 51,52–53,12 Türkçe çeviri (el yazısı; sözcük penceresi: Dün 51,52 · futbol 51,84 ·
  // oynamadık. 52,20–53,12 sn; kaynak cümle 5)
  const ytr = sonSatir + 78;
  S.koy(S.elYazisi({ metin: "Dün futbol oynamadık.", x: 140, y: ytr, renk: IKINCIL,
    sozcukler: S.dizi("Dün", 51.52, 3).map((w) => ({ t0: w.t0, t1: w.t1 })) }));

  // 53,44–54,80 didn't sarı daire; formül kartı did + not + V1
  S.koy(S.halka(kel("didn't"), 53.44, 0.3, 31));
  const ky = ytr + 68, fo = "700 60px Fredoka";
  const x0 = 190;
  const wDid = olc(fo, "did"), wPlus = olc(fo, " + "), wNot = olc(fo, "not");
  S.koy(S.kart({ x: 140, y: ky, w: 640, h: 140, tb: 53.9, tohum: 9, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [
    { parca: [["did", KREM]], x: x0, y: ky + 90, font: fo, tb: 54.32, sure: 0.3 },
    { parca: [[" + ", IKINCIL]], x: x0 + wDid, y: ky + 90, font: fo, tb: 54.4, sure: 0.3 },
    { parca: [["not", KIRMIZI]], x: x0 + wDid + wPlus, y: ky + 90, font: fo, tb: 54.48, sure: 0.3 },
    { parca: [[" + ", IKINCIL]], x: x0 + wDid + wPlus + wNot, y: ky + 90, font: fo, tb: 54.56, sure: 0.3 },
    { parca: [["V1", SARI]], x: x0 + wDid + wPlus + wNot + wPlus, y: ky + 90, font: fo, tb: 54.64, sure: 0.3 },
  ] }));

  // 55,51 Did: küçük geçmiş bayrağı (direk + flama) + Caveat etiket
  const fx = 860, fy = ky + 20;
  S.koy(S.darbe([[fx, fy + 105], [fx - 2, fy + 50], [fx + 1, fy]], { duz: true, w: 4, renk: KREM, uc0: 4, uc1: 8, tohum: 41 },
    55.51, 0.25, 0.55));
  S.koy(S.darbeler([[[fx + 1, fy + 2], [fx + 74, fy + 22], [fx + 2, fy + 46]]], { duz: true, w: 4, renk: SARI, uc0: 4, uc1: 8 },
    55.75, 0.3, 0.1, 0.5));
  S.koy(S.elYazisi({ metin: "geçmiş", x: fx + 96, y: fy + 80, boy: 48, renk: IKINCIL, tb: 56.07,
    sure: 0.45 }));                                 // etiket, 56,07–56,52 sn

  // 59,43 play sarı daire; yanında played kırmızı çizili (59,7)
  S.koy(S.halka(kel("play"), 59.43, 0.3, 32));
  const py = ky + 228, pf = "700 56px Fredoka", pw = olc(pf, "played");
  S.koy(S.metinPop({ parca: [["played", IKINCIL]], x: 140, y: py, font: pf, tb: 59.7, sure: 0.3, ses: 0.5 }));
  S.koy(S.darbe([[128, py - 20], [140 + pw + 14, py - 24]], { duz: true, w: 8, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 16, tohum: 73 },
    60.0, 0.3, 0.65));

  // 60,30–61,74 Soruda Did başa: sarı kalem oku soru satırının başına
  const qy = 975;
  S.koy(S.elYazisi({ metin: "did başa", x: 230, y: py + 56, boy: 48, renk: SARI, tb: 60.6,
    sure: 0.55, ses: false }));                     // etiket, 60,60–61,15 sn
  S.koy(S.darbeler(ok([100, py + 28], [100, qy - 78], 6), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 60.3, 0.4, 0.2, 0.55));

  // 62,87–64,23 soru cümlesi
  S.koy(S.cumleYaz({ sozcukler: S.dizi("Did", 62.87, 4), x: 140, y: qy, maxGen: 980 }));
}

surucu(kur, (f) => S.kare(f), KARE);

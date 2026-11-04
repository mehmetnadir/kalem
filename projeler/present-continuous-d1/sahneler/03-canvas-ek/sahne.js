// SAHNE 03 (D1, dikey) — Ek: düz canvas, 551 kare, t_bas 16,97; cümle 4 + 5. Zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, elips, FONT, olc } from "./sahne-ortak.js";

const KARE = 551, TBAS = 16.97, ICERIK = 539;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Examples", cumle: 4 });
const KREM = RT.murekkep, IKI = RT.ikincil, SARI = RT.vurgu;
const svgOku = async (yol) => (await fetch(`/projeler/present-continuous-d1/ortak/cizim/${yol}`)).text();
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const kosucu = await svgOku("open-peeps/standing-4.svg");

  // 17,55 etiket: fiil + -ing
  S.koy(S.not({ parca: [["fiil", IKI], [" + ", IKI], ["-ing", SARI]], x: 70, y: 370, font: CV(70), tb: 17.55, sure: 0.5 }));

  // 18,81 go -> 19,61 go-ing (ek kalemle yazılır)
  const R1 = 500, g1 = olc(FF(140), "go");
  S.koy(S.metinPop({ parca: [["go", KREM]], x: 70, y: R1, font: FF(140), tb: 18.81, sure: 0.35, ses: 0.5 }));
  S.koy(S.darbeler(ok([70 + g1 + 40, R1 - 52], [70 + g1 + 150, R1 - 52], 3), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 19.25, 0.16, 0.1, 0.5));
  const x2 = 70 + g1 + 190;
  S.koy(S.metinPop({ parca: [["go", KREM]], x: x2, y: R1, font: FF(140), tb: 19.61, sure: 0.3, ses: 0.5 }));
  const ingX = x2 + g1;
  S.koy(S.not({ parca: [["-ing", SARI]], x: ingX, y: R1, font: FF(140), tb: 19.95, sure: 0.4, ses: 0.5 }));
  const ingW = olc(FF(140), "-ing");
  S.koy(S.darbe([[ingX, R1 + 22], [ingX + ingW * 0.5, R1 + 18], [ingX + ingW, R1 + 23]],
    { w: 8, renk: RT.vurguDolgu, alfa: 0.85, uc0: 8, uc1: 14, duz: true }, 20.4, 0.3, 0.55));
  S.koy(S.not({ parca: [["= -yor", SARI]], x: ingX, y: R1 + 100, font: CV(72), tb: 21.2, sure: 0.45 }));
  S.koy(S.parilti(ingX + ingW + 8, R1 - 120, 21.9, 26));

  // 22,79 gidi-yor-um <-> going (ikisi de iş sürüyor)
  const R2 = 760, fT = CV(100), fE = FF(96);
  const gA = olc(fT, "gidi"), gB = olc(fT, "-yor"), gC = olc(fT, "um");
  S.koy(S.not({ parca: [["gidi", KREM], ["-yor", SARI], ["um", KREM]], x: 70, y: R2, font: fT, tb: 22.79, sure: 0.6 }));
  const ex = 640, eg = olc(fE, "go");
  S.koy(S.metinPop({ parca: [["go", KREM], ["-ing", SARI]], x: ex, y: R2, font: fE, tb: 23.83, sure: 0.35, ses: 0.5 }));
  const mid = 70 + gA + gB + gC;
  S.koy(S.darbeler(ok([mid + 24, R2 - 34], [ex - 30, R2 - 34], 4), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 24.87, 0.16, 0.1, 0.5));
  S.koy(S.darbe(elips(70 + gA + gB / 2, R2 - 30, gB / 2 + 14, 52, -0.05, 21), { w: 6, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 }, 25.1, 0.35, 0.55));
  S.koy(S.darbe(elips(ex + eg + olc(fE, "-ing") / 2 + 4, R2 - 28, olc(fE, "-ing") / 2 + 8, 50, 0.05, 22), { w: 6, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 }, 25.35, 0.35, 0.55));
  S.koy(S.not({ parca: [["= iş sürüyor", IKI]], x: 70, y: R2 + 110, font: CV(70), tb: 25.75, sure: 0.6 }));

  // 29,11 running / 30,24 koşuyor
  const R3 = 1010;
  S.koy(S.metinPop({ parca: [["runn", KREM], ["-ing", SARI]], x: 70, y: R3, font: FF(112), tb: 29.11, sure: 0.35, ses: 0.5 }));
  S.koy(S.cizim({ svg: kosucu, kutu: { x: 810, y: 880, w: 180, h: 270 }, ad: "kosucu", esik: 0.004, enCok: 50, w: 3.2, tb: 29.2, sure: 1.3, olayEnCok: 6 }));
  S.koy(S.not({ parca: [["koşu", KREM], ["-yor", SARI]], x: 70, y: R3 + 115, font: CV(100), tb: 30.24, sure: 0.6 }));
  S.koy(S.parilti(700, R3 - 90, 31.0, 24));

  // 31,19 ek değişmez: -ing, -yor
  S.koy(S.darbeler(
    [[[48, 1180], [1032, 1177]], [[1034, 1171], [1030, 1312]], [[1034, 1314], [50, 1318]], [[48, 1312], [46, 1173]]],
    { w: 3.6, renk: IKI, uc0: 10, uc1: 14, duz: true }, 31.0, 0.14, 0.1, 0.55));
  S.koy(S.not({ parca: [["ek değişmez:", IKI]], x: 80, y: 1262, font: CV(72), tb: 31.19, sure: 0.7 }));
  S.koy(S.metinPop({ parca: [["-ing", SARI]], x: 480, y: 1262, font: FF(68), tb: 32.63, sure: 0.3, ses: 0.5 }));
  S.koy(S.not({ parca: [["-yor", SARI]], x: 760, y: 1262, font: CV(86), tb: 33.83, sure: 0.4 }));
}

surucu(kur, (f) => S.kare(f), KARE);

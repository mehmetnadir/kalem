// SAHNE 12 — Kapanış (düz canvas, 190 kare, t_bas 336,09; cümle 18). Kendini çizen kalem; zaman yalnız
// kare numarasından. SIGNAL → VERB kalemle ok; sonraki ders kartı. Anlatım sonundan 0,5 sn sonra biter.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 190, TBAS = 336.09, ICERIK = 160;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Next lesson", etkin: 3, cumle: 18 });
window.__S = S;                                   // önizleme ölçümü (olaylar.json)
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

async function kur() {
  await S.kur();
  const t = (ad) => S.dizi(ad, ad === "Önce" ? 337.01 : 338, 1)[0].t0;
  // 337,41 «sinyal»: SIGNAL (Fredoka 150), sarı alt çizgi kayar
  const FB = "700 150px Fredoka", Y = 430;
  const wS = olc(FB, "SIGNAL"), wV = olc(FB, "VERB"), ara = 230, top = wS + ara + wV, x0 = (1920 - top) / 2;
  const tSig = S.dizi("sinyal,", 337.41, 1)[0].t0, tSonra = S.dizi("sonra", 338.21, 1)[0].t0,
    tFiil = S.dizi("fiil.", 338.53, 1)[0].t0;
  S.koy(S.metinPop({ parca: [["SIGNAL", KREM]], x: x0, y: Y, font: FB, tb: tSig, sure: 0.3, olcek0: 0.8,
    ses: 0.6, turu: "tik" }));
  S.koy(S.darbe(altCizgi(x0 - 6, x0 + wS + 6, Y + 28, 71), { w: 9, renk: RT.vurguDolgu, alfa: 0.85, uc0: 8,
    uc1: 14 }, tSig + 0.25, 0.3, 0.5));
  // 338,21 «sonra»: kalem oku SIGNAL → VERB
  S.koy(S.darbeler(ok([x0 + wS + 40, Y - 56], [x0 + wS + ara - 40, Y - 56], 7), { w: 9, renk: SARI, uc0: 12,
    uc1: 16 }, tSonra, 0.3, 0.12, 0.6));
  // 338,53 «fiil»: VERB + sarı daire
  const xv = x0 + wS + ara;
  S.koy(S.metinPop({ parca: [["VERB", SARI]], x: xv, y: Y, font: FB, tb: tFiil, sure: 0.3, olcek0: 0.8,
    ses: 0.6, turu: "tik" }));
  S.koy(S.darbe(elips(xv + wV / 2, Y - 54, wV / 2 + 34, 106, -0.03, 81), { w: 7, renk: SARI, alfa: 0.85,
    uc0: 14, uc1: 30 }, tFiil + 0.3, 0.5, 0.55));

  // 339,41 «Sonraki derste görüşürüz»: sonraki ders kartı (GR-02-04)
  const tS = S.dizi("Sonraki", 339.41, 1)[0].t0, tD = S.dizi("derste", 339.81, 1)[0].t0,
    tG = S.dizi("görüşürüz.", 340.09, 1)[0].t0;
  const kx = 440, ky = 640, kw = 1040, kh = 290;
  S.koy(S.darbeler(
    [[[kx - 6, ky + 2], [kx + kw + 8, ky - 2]], [[kx + kw + 2, ky - 8], [kx + kw - 2, ky + kh + 9]],
      [[kx + kw + 7, ky + kh + 2], [kx - 8, ky + kh - 2]], [[kx + 2, ky + kh + 8], [kx - 2, ky - 10]]]
      .map((q) => [q[0], [(q[0][0] + q[1][0]) / 2 + 1.5, (q[0][1] + q[1][1]) / 2 + 1.2], q[1]]).flat(0),
    { duz: true, w: 3.6, renk: IKINCIL, uc0: 10, uc1: 12 }, tS, 0.14, 0.1, 0.55));
  S.koy(S.metinPop({ parca: [["Next lesson", IKINCIL]], x: kx + 56, y: ky + 74, font: "500 36px Lexend", tb: tS + 0.2,
    sure: 0.3, olcek0: 0.9, ses: false }));
  S.koy(S.metinPop({ parca: [["GR-02-04", KREM]], x: kx + 56, y: ky + 170, font: "700 84px Fredoka", tb: tD,
    sure: 0.3, olcek0: 0.9, ses: 0.5, turu: "tik" }));
  S.koy(S.metinPop({ parca: [["Simple Present vs Present Continuous", SARI]], x: kx + 56, y: ky + 244,
    font: "600 44px Fredoka", tb: tG, sure: 0.3, olcek0: 0.9, ses: false }));
  S.koy(S.darbeler(ok([kx + kw - 190, ky + 70], [kx + kw - 60, ky + 70], 9), { w: 7, renk: SARI, uc0: 10, uc1: 14 },
    tG + 0.1, 0.18, 0.1, false));
  S.koy(S.parilti(kx + kw - 30, ky - 6, 340.15));
}

surucu(kur, (f) => S.kare(f), KARE);

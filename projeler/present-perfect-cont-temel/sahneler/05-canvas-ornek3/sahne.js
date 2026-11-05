// SAHNE 05 — Örnek 3 (PPC temel; düz canvas, 439 kare, t_bas 47,27; cümle 5; çıkış geçişi fade).
// Zaman yalnız kare numarasından. Küresel sn: BRIEF §4 sahne 05 tablosu.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, ok, elips, olc, geriTasma, kis } from "./sahne-ortak.js";

const KARE = 439, TBAS = 47.27, ICERIK = 427;
const KOKDIZ = "/projeler/present-perfect-cont-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;

async function kur() {
  await S.kur();
  const [bulut, semsiye] = await Promise.all([svgOku("tabler/cloud-rain.svg"), svgOku("coco/umbrella.svg")]);

  // 47,82–48,86 daire içinde 3
  S.koy(S.daireSayi(3, 190, 205, 47.82));

  // 49,11–49,75 Look! kırmızı pop (0,6→1 taşmalı, vurus 0,9) + kalem ünlem çizgisi
  const lx = 140, ly = 350, lf = "700 110px Fredoka", lw = olc(lf, "Look"), lfb = S.fr(49.11);
  S.bas(lfb); S.olay(lfb, "vurus", 0.9);
  S.koy({ ciz: (ctx, f) => {
    const u = (f - lfb) / 13; if (u <= 0) return;
    const s = 0.6 + 0.4 * geriTasma(u, 2.2), cx = lx + lw / 2, cy = ly - 40;
    ctx.save(); ctx.globalAlpha = kis(u * 3); ctx.translate(cx, cy); ctx.scale(s, s); ctx.translate(-cx, -cy);
    ctx.font = lf; ctx.textAlign = "left"; ctx.textBaseline = "alphabetic"; ctx.fillStyle = renkCoz(KIRMIZI);
    ctx.fillText("Look", lx, ly); ctx.restore();
  } });
  const ux = lx + lw + 14;
  S.koy(S.darbe([[ux - 2, ly - 86], [ux + 2, ly - 56], [ux + 3, ly - 28]],
    { w: 16, renk: KIRMIZI, alfa: 0.95, uc0: 6, uc1: 18, tohum: 61 }, 49.3, 0.22, 0.7));
  S.koy(S.darbe(elips(ux + 3, ly - 6, 3.5, 3.5, 0, 62), { w: 13, renk: KIRMIZI, alfa: 0.95, uc0: 4, uc1: 4, tohum: 63 },
    49.55, 0.12, false));

  // 49,83–52,87 cümle sözcük sözcük + sarı alt çizgi (2 satır, x 140, y 460)
  // iki cümleyi ayrı satırda kur: "has been" aynı satırda kalsın (halka tek elips)
  S.koy(S.cumleYaz({ sozcukler: S.dizi("The", 49.83, 4), x: 140, y: 460, maxGen: 900 }));
  const c2 = S.koy(S.cumleYaz({ sozcukler: S.dizi("It", 51.23, 4), x: 140, y: 544, maxGen: 900 }));
  const sonSatir = 544, kel = (ad) => c2.kel.find((k) => k.m === ad);

  // 49,83–51,1 yağmur bulutu (rain, 520 px) sağ sütun
  S.koy(S.cizim({ svg: bulut, kutu: { x: 1330, y: 190, w: 520, h: 520 }, ad: "bulut", esik: 0.01, enCok: 30, w: 4.2,
    tb: 49.83, sure: 1.3, olayEnCok: 6, nefes: false }));
  S.koy(S.parilti(1820, 250, 51.3, 24));
  // 50,51 (wet) sokak çizgisi + 3 su birikintisi
  S.koy(S.darbe([[1010, 900], [1250, 897], [1520, 902], [1860, 899]],
    { w: 4.2, renk: KREM, uc0: 10, uc1: 20, tohum: 71 }, 50.51, 0.5, 0.6));
  [[1180, 940, 80, 11], [1520, 948, 96, 12], [1740, 938, 70, 10]].forEach(([cx, cy, rx, ry], i) => {
    S.koy(S.darbe(elips(cx, cy, rx, ry, 0.03 * i, 72 + i), { w: 3.4, renk: IKINCIL, alfa: 0.9, uc0: 10, uc1: 14 },
      50.85 + i * 0.12, 0.3, i === 0 ? 0.45 : false));
  });
  // 51,23 (It) şemsiye (260 px) sokağın üstünde
  S.koy(S.cizim({ svg: semsiye, kutu: { x: 1060, y: 620, w: 260, h: 260 }, ad: "semsiye", esik: 0.01, enCok: 25, w: 3.8,
    tb: 51.23, sure: 0.8, olayEnCok: 4, nefes: false }));

  // 53,12–56,40 Türkçe çeviri (Caveat 48): iki cümle alt alta
  const ytr = sonSatir + 78;
  S.koy(S.not({ parca: [["Bak, sokak ıslak.", IKINCIL]], x: 140, y: ytr, tb: 53.12, sure: 0.5 }));
  S.koy(S.not({ parca: [["Yağmur bir süredir yağıyor.", IKINCIL]], x: 140, y: ytr + 56, tb: 54.88, sure: 0.7 }));

  // 56,56–57,76 sarı ok ıslak sokağa + Caveat vurgu (sonuç ipucu)
  const yn = ytr + 56 + 74;
  S.koy(S.not({ parca: [["izi şimdi görünüyor", SARI]], x: 140, y: yn, font: "700 56px Caveat", tb: 56.56, sure: 0.6 }));
  S.koy(S.darbeler(ok([560, yn - 18], [1000, 884], 5), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 57.1, 0.4, 0.2, 0.55));

  // 57,91–61,51 formül kartı: has been + V-ing / has been / rain-ing; halka has been (59,51) ve raining (60,79)
  const ky = 820, fo = "700 60px Fredoka", fo2 = "700 52px Fredoka";
  S.koy(S.kart({ x: 140, y: ky, w: 640, h: 160, tb: 57.91, tohum: 7, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [
    { parca: [["has been", KREM]], x: 180, y: ky + 64, font: fo, tb: 57.91, sure: 0.3 },
    { parca: [["+", IKINCIL]], x: 440, y: ky + 64, font: fo, tb: 57.95, sure: 0.3 },
    { parca: [["V", KREM], ["-ing", SARI]], x: 510, y: ky + 64, font: fo, tb: 58.0, sure: 0.3 },
    { parca: [["has been", KREM]], x: 180, y: ky + 132, font: fo2, tb: 58.4, sure: 0.3 },
    { parca: [["rain", KREM], ["-ing", SARI]], x: 510, y: ky + 132, font: fo2, tb: 58.5, sure: 0.3 },
  ] }));
  const has = kel("has"), been = kel("been");
  if (has.satir === been.satir) {
    S.koy(S.halka({ x: has.x, w: been.x + been.w - has.x, y: has.y, boy: has.boy }, 59.51, 0.4, 21, 8));
  } else {
    S.koy(S.halka(has, 59.51, 0.3, 21)); S.koy(S.halka(been, 59.8, 0.3, 22));
  }
  S.koy(S.halka(kel("raining."), 60.79, 0.3, 23));
}

surucu(kur, (f) => S.kare(f), KARE);

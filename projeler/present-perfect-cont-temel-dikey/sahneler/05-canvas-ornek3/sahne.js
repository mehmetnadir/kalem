// SAHNE 05 (DİKEY) — PPC temel Örnek 3: düz canvas, 439 kare, t_bas 47,27; cümle 5.
// Zaman yalnız kare numarasından.
// Yerleşim BRIEF-DIKEY §4: kart (Look! + cümle) -> TR çeviri ->
// bulut + şemsiye + ıslak sokak + not -> formül.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, elips, ok, olc, geriTasma, kis } from "./sahne-ortak.js";

const KARE = 439, TBAS = 47.27, ICERIK = 427;
const KOKDIZ = "/projeler/present-perfect-cont-temel-dikey/ortak/cizim";
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5
});
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const [bulut, semsiye] = await Promise.all([svgOku("tabler/cloud-rain.svg"),
    svgOku("coco/umbrella.svg")]);

  // Kart (tam genişlik 984, iç boşluk 40): 49,11 Look! kırmızı pop +
  // cümle sözcük zamanında
  S.koy(S.darbeler(
    kutu(48, 372, 984, 300, 11), { w: 4, renk: IKINCIL, uc0: 10, uc1: 16 }, 47.82, 0.12, 0.1, 0.5
  ));
  const lx = 88, ly = 470, lf = FF(110), lw = olc(lf, "Look"), lfb = S.fr(49.11);
  S.bas(lfb); S.olay(lfb, "vurus", 0.9);
  S.koy({ ciz: (ctx, f) => {
    const u = (f - lfb) / 13; if (u <= 0) return;
    const s = 0.6 + 0.4 * geriTasma(u, 2.2), cx = lx + lw / 2, cy = ly - 40;
    ctx.save(); ctx.globalAlpha = kis(u * 3); ctx.translate(cx, cy); ctx.scale(s, s);
    ctx.translate(-cx, -cy);
    ctx.font = lf; ctx.textAlign = "left"; ctx.textBaseline = "alphabetic";
    ctx.fillStyle = renkCoz(KIRMIZI);
    ctx.fillText("Look", lx, ly); ctx.restore();
  } });
  const ux = lx + lw + 14;
  S.koy(S.darbe([[ux - 2, ly - 86], [ux + 2, ly - 56], [ux + 3, ly - 28]],
    { w: 16, renk: KIRMIZI, alfa: 0.95, uc0: 6, uc1: 18, tohum: 61 }, 49.3, 0.22, 0.7));
  S.koy(S.darbe(
    elips(ux + 3, ly - 6, 3.5, 3.5, 0, 62),
    { w: 13, renk: KIRMIZI, alfa: 0.95, uc0: 4, uc1: 4, tohum: 63 }, 49.55, 0.12, false
  ));

  // iki cümle ayrı satırda: "has been" aynı satırda kalsın (halka tek elips)
  S.koy(S.cumleYaz({
    sozcukler: S.dizi("The", 49.83, 4), x: 88, y: 566, maxGen: 900,
    font: FF(72), satirH: 84, bosluk: 8
  }));
  const c2 = S.koy(S.cumleYaz({
    sozcukler: S.dizi("It", 51.23, 4), x: 88, y: 646, maxGen: 900, font: FF(72), satirH: 84,
    bosluk: 8
  }));
  const sonSatir = 646, kel = (ad) => c2.kel.find((k) => k.m === ad);

  // 53,12 / 54,88 Türkçe çeviri (Caveat 64, mürekkep) iki satır
  const ytr = sonSatir + 84;
  S.koy(S.not({
    parca: [["Bak, sokak ıslak.", KREM]], x: 88, y: ytr, font: CV(64), tb: 53.12, sure: 0.5
  }));
  S.koy(S.not({
    parca: [["Yağmur bir süredir yağıyor.", KREM]], x: 88, y: ytr + 66, font: CV(64),
    tb: 54.88, sure: 0.7
  }));

  // ORTA (y 850–1290): şemsiye (sol) + yağmur bulutu (orta, 420 px) +
  // ıslak sokak; not + ok sağda
  const SY = 1250;
  S.koy(S.cizim({
    svg: bulut, kutu: { x: 470, y: 880, w: 420, h: 420 }, ad: "bulut", esik: 0.01, enCok: 30,
    w: 4.2, tb: 49.83, sure: 1.3, olayEnCok: 6, nefes: false
  }));
  S.koy(S.parilti(850, 960, 51.3, 28));
  S.koy(S.darbe([[48, SY], [330, SY - 3], [700, SY + 2], [1032, SY - 1]],
    { w: 4.6, renk: KREM, uc0: 10, uc1: 20, tohum: 71 }, 50.51, 0.5, 0.6));
  [[250, SY + 14, 90, 9], [600, SY + 15, 110, 10], [940, SY + 13, 70, 9]].forEach(
    ([cx, cy, rx, ry], i) => {
      S.koy(S.darbe(
        elips(cx, cy, rx, ry, 0.03 * i, 72 + i),
        { w: 3.8, renk: IKINCIL, alfa: 0.9, uc0: 10, uc1: 14 },
        50.85 + i * 0.12, 0.3, i === 0 ? 0.45 : false
      ));
    }
  );
  S.koy(S.cizim({
    svg: semsiye, kutu: { x: 48, y: 830, w: 420, h: 420 }, ad: "semsiye", esik: 0.01, enCok: 25,
    w: 4.2, tb: 51.23, sure: 0.8, olayEnCok: 4, nefes: false
  }));

  // 56,56 sonuç ipucu: Caveat 64 (vurgu) + sarı ok ıslak sokağa
  S.koy(S.not({
    parca: [["izi şimdi", SARI]], x: 735, y: 760, font: CV(64), tb: 56.56, sure: 0.4
  }));
  S.koy(S.not({
    parca: [["görünüyor", SARI]], x: 735, y: 826, font: CV(64), tb: 56.9, sure: 0.4
  }));
  S.koy(S.darbeler(
    ok([950, 850], [960, SY - 14], 5), { w: 9, renk: SARI, uc0: 10, uc1: 14 }, 57.3, 0.4, 0.2,
    0.55
  ));

  // 57,91 formül: has been + V-ing (Fredoka 110, taban 1380);
  // 59,51 has been halka; 60,79 raining halka
  S.koy(S.metinPop({
    parca: [["has been", KREM], [" + ", IKINCIL], ["V", KREM], ["-ing", SARI]], x: 540, y: 1364,
    font: FF(110), hiza: "orta", tb: 57.91, sure: 0.4, ses: 0.8, turu: "vurus"
  }));
  const has = kel("has"), been = kel("been");
  if (has.satir === been.satir) {
    S.koy(S.halka(
      { x: has.x, w: been.x + been.w - has.x, y: has.y, boy: has.boy }, 59.51, 0.4, 21, 8
    ));
  } else {
    S.koy(S.halka(has, 59.51, 0.3, 21)); S.koy(S.halka(been, 59.8, 0.3, 22));
  }
  S.koy(S.halka(kel("raining."), 60.79, 0.3, 23));
}

surucu(kur, (f) => S.kare(f), KARE);

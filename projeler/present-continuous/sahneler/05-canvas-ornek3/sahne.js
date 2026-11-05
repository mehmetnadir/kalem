// SAHNE 05 — Örnek 3 (düz canvas, 517 kare, t_bas 51,98; cümle 5; çıkış geçişi fade). Zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, ok, elips, olc, geriTasma, yavasla, kis } from "../04-canvas-ornek2/sahne-ortak.js";

const KARE = 517, TBAS = 51.98, ICERIK = 505, KAYMA = 6.0;   // TBAS: eski çerçeve; zaman.json t_bas 45,98
const KOKDIZ = "/projeler/present-continuous/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: KAYMA, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;

async function kur() {
  await S.kur();
  const [agac, kedi] = await Promise.all([svgOku("coco/tree.svg"), svgOku("coco/cat.svg")]);

  // 51,98–53,02 daire içinde 3 (ilk 12 kare boş)
  S.koy(S.daireSayi(3, 190, 205, S.zm(12)));

  // 53,27 Look! kırmızı pop (0,6→1 taşmalı, vurus 0,9) + kalem ünlem çizgisi
  const lx = 140, ly = 350, lf = "700 110px Fredoka", lw = olc(lf, "Look"), lfb = S.fr(53.27);
  S.bas(lfb); S.olay(lfb, "vurus", 0.9);
  S.koy({ ciz: (ctx, f) => {
    const u = (f - lfb) / 13; if (u <= 0) return;
    const s = 0.6 + 0.4 * geriTasma(u, 2.2), cx = lx + lw / 2, cy = ly - 40;
    ctx.save(); ctx.globalAlpha = kis(u * 3); ctx.translate(cx, cy); ctx.scale(s, s); ctx.translate(-cx, -cy);
    ctx.font = lf; ctx.textAlign = "left"; ctx.textBaseline = "alphabetic"; ctx.fillStyle = renkCoz(KIRMIZI); ctx.fillText("Look", lx, ly); ctx.restore();
  } });
  const ux = lx + lw + 14;
  S.koy(S.darbe([[ux - 2, ly - 86], [ux + 2, ly - 56], [ux + 3, ly - 28]], { w: 16, renk: KIRMIZI, alfa: 0.95, uc0: 6, uc1: 18, tohum: 61 }, 53.5, 0.22, 0.7));
  S.koy(S.darbe(elips(ux + 3, ly - 6, 3.5, 3.5, 0, 62), { w: 13, renk: KIRMIZI, alfa: 0.95, uc0: 4, uc1: 4, tohum: 63 }, 53.78, 0.12, false));

  // 53,99–55,59 cümle + sarı alt çizgi
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("The", 53.99, 6), x: 140, y: 460, maxGen: 980 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y)), kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 53,3–54,6 ağaç (Coco, ≈640 px); 54,4–56,5 kedi (Coco, ≈170 px) gövde boyunca aşağıdan ortaya tırmanır
  S.koy(S.cizim({ svg: agac, kutu: { x: 1200, y: 260, w: 640, h: 640 }, ad: "agac", esik: 0.01, enCok: 40, w: 3.8, tb: 53.3,
    sure: 1.3, olayEnCok: 8, nefes: false }));
  S.koy(S.parilti(1650, 330, 54.65, 26));
  const kx = 1520 - 85, ky0 = 775, fTir = S.fr(55.15), fTirSon = S.fr(56.5), MES = 340;
  const kg = S.cizim({ svg: kedi, kutu: { x: kx, y: ky0, w: 170, h: 170 }, ad: "kedi", esik: 0.01, enCok: 30, w: 4.6, tb: 54.4,
    sure: 0.6, olayEnCok: 2, nefes: false });
  kg.dolgu = { nokta: kg.yollar, renk: RT.zemin, fb: S.fr(54.4) };
  kg.donusum = (f) => {
    const u = kis((f - fTir) / (fTirSon - fTir)), e = yavasla(u), fi = Math.min(f, ICERIK), son = f >= fTirSon;
    const sal = u > 0 ? (son ? 0 : 4 * Math.sin(u * Math.PI * 6)) : 0;
    const dur = son ? 2 * Math.sin((fi - fTirSon) / 22) : 0;
    return { cx: kx + 85, cy: ky0 + 160, tx: sal, ty: -MES * e + dur, dondur: u > 0 && !son ? 0.052 * Math.sin(u * Math.PI * 6) : 0, olcek: 1 };
  };
  S.koy(kg);
  [[[1500, 905], [1476, 917]], [[1528, 910], [1528, 932]], [[1556, 905], [1580, 917]]].forEach((p, i) => {
    const d = S.darbe(p, { duz: true, w: 3.4, renk: IKINCIL, alfa: 0.8, uc0: 4, uc1: 8, tohum: 80 + i }, 55.15 + i * 0.05, 0.15, i === 0 ? 0.45 : false);
    const f0 = S.fr(55.95), oc = d.ciz; d.ciz = (ctx, f) => { d.carpan = 1 - kis((f - f0) / 8); if (d.carpan > 0) oc(ctx, f); };
    S.koy(d);
  });

  // 56,32–57,60 Türkçe çeviri
  const ytr = sonSatir + 78;
  S.koy(S.elYazisi({ metin: "Bak, kedi ağaca tırmanıyor.", x: 140, y: ytr, renk: IKINCIL,
    sozcukler: S.dizi("Bak,", 56.32, 4) }));   // el yazısı, sözcük penceresi (pilot 05.11)

  // 58,88–63,96 etiketler (el kutusu + tik): Look! / Listen! / Watch out!
  const yb = ytr + 56, bh = 62, lfn = "700 34px Lexend";
  let xx = 140;
  [["Look!", 58.88], ["Listen!", 59.6], ["Watch out!", 60.52]].forEach(([m, tb], i) => {
    const w = olc(lfn, m) + 44;
    S.koy(S.darbeler(kutu(xx, yb, w, bh, 30 + i), { w: 3.4, renk: KREM, uc0: 8, uc1: 14 }, tb, 0.1, 0.06, false));
    S.koy(S.metinPop({ parca: [[m, KREM]], x: xx + 22, y: yb + 43, font: lfn, tb: tb + 0.22, sure: 0.3, ses: 0.5 }));
    xx += w + 28;
  });
  // 62,80–63,96 sarı ok → NOW noktası (x≈830, y≈800)
  S.koy(S.darbeler(ok([600, yb + bh + 16], [790, 778], 5), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 62.8, 0.3, 0.2, 0.55));
  const nxx = 830, ay = 802;
  S.koy(S.darbe(elips(nxx, ay, 8, 8, 0, 9), { w: 17, renk: SARI, alfa: 0.9, uc0: 3, uc1: 3, tohum: 91 }, 63.5, 0.25, 0.5));
  S.koy(S.nabiz(nxx, ay, 12, 63.8));
  S.koy(S.elYazisi({ metin: "NOW", x: nxx + 28, y: ay + 18, boy: 56, renk: SARI, tb: 63.6, sure: 0.4, ses: false }));

  // 65,37–65,69 is / climbing daire
  S.koy(S.halka(kel("is"), 65.37, 0.3, 21));
  S.koy(S.halka(kel("climbing"), 65.69, 0.3, 22));

  // 67,14–67,51 formül kartı: be + V-ing / is / climb-ing
  const ky = 820, fo = "700 60px Fredoka", fo2 = "700 52px Fredoka";
  S.koy(S.kart({ x: 140, y: ky, w: 620, h: 160, tb: 67.14, tohum: 7, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [
    { parca: [["be", KREM]], x: 190, y: ky + 64, font: fo, tb: 67.14, sure: 0.3 },
    { parca: [["+", IKINCIL]], x: 330, y: ky + 64, font: fo, tb: 67.16, sure: 0.3 },
    { parca: [["V", KREM], ["-ing", SARI]], x: 410, y: ky + 64, font: fo, tb: 67.18, sure: 0.3 },
    { parca: [["is", KREM]], x: 190, y: ky + 130, font: fo2, tb: 67.3, sure: 0.3 },
    { parca: [["climb", KREM], ["-ing", SARI]], x: 410, y: ky + 130, font: fo2, tb: 67.34, sure: 0.3 },
  ] }));
}

surucu(kur, (f) => S.kare(f), KARE);

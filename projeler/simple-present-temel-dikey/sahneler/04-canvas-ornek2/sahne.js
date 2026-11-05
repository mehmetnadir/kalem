// SAHNE 04 (DİKEY) — Örnek 2: düz canvas, 1080x1920, 482 kare, t_bas 27,69; cümle 4.
// Zaman yalnız kare numarasından; zamanlar sozcukler.json / altyazi.json ile aynı çerçevede (küresel sn).
// Yerleşim sıfırdan dikey: kart (tam genişlik) → TR çeviri → ORTA figür + otobüs → alışkanlık listesi → alt formül.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, kutu, olc } from "./sahne-ortak.js";

const KARE = 482, TBAS = 27.69, ICERIK = 470;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const KOKDIZ = "/projeler/simple-present-temel-dikey/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKI = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const [kardes, otobus] = await Promise.all([svgOku("open-peeps/sitting-4.svg"), svgOku("coco/bus.svg")]);

  // kart: tam genişlik 984, Fredoka 72, sözcük zamanlı (ilk 12 kare boş; kutu 12. kareden çizilir)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("My", 29.53, 8), x: 88, y: 470, maxGen: 904, font: FF(72),
    satirH: 88 }));
  const sonTaban = Math.max(...cum.kel.map((k) => k.y)), kartAlt = sonTaban + 20 + 28;
  S.koy(S.darbeler(kutu(48, 372, 984, kartAlt - 372, 7), { w: 4, renk: IKI, uc0: 10, uc1: 18 }, S.zm(12), 0.2,
    0.12, 0.55));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);
  S.koy(S.halka(kel("usually"), 30.55, 0.35, 11, 4));

  // 32,74 Türkçe çeviri (Caveat 64, mürekkep, tek satır)
  const yTR = kartAlt + 72;
  S.koy(S.not({ parca: [["Kardeşim genellikle okula otobüsle gider.", KREM]], x: 64, y: yTR, font: CV(64),
    tb: 32.74, sure: 1.6 }));

  // ORTA: oturan figür (440 px) + otobüs (460 px) tek ufuk çizgisinde; bant yTR+30 → 1215
  const yZ = 1222, fUst = Math.min(yTR + 32, 780);
  S.koy(S.darbe([[48, yZ], [330, yZ - 3], [700, yZ + 2], [1032, yZ - 1]],
    { duz: true, w: 4, renk: IKI, alfa: 0.8, uc0: 10, uc1: 30 }, 29.7, 0.8, 0.4));
  S.koy(S.cizim({ svg: kardes, kutu: { x: 70, y: fUst, w: 440, h: yZ - 8 - fUst }, ad: "kardes", esik: 0.004,
    enCok: 60, w: 4.4, tb: 29.6, sure: 1.7, olayEnCok: 7 }));
  S.koy(S.cizim({ svg: otobus, kutu: { x: 560, y: yZ - 8 - 350, w: 460, h: 350 }, ad: "otobus", enCok: 25, w: 4,
    tb: 31.3, sure: 1.1, olayEnCok: 5 }));
  S.koy(S.parilti(980, yZ - 380, 32.5, 26));

  // 35,53–37,69 alışkanlık listesi (otobüsün üstünde, sağ sütun): usually · always · every day (Caveat 72, sarı tik)
  const fN = CV(72), xN = 600, TIK = (cx, cy) => [[cx - 16, cy + 2], [cx - 4, cy + 14], [cx + 20, cy - 16]];
  [["usually", 35.53, 762], ["always", 36.73, 840], ["every day", 37.45, 918]].forEach(([m, tb, y]) => {
    S.koy(S.not({ parca: [[m, KREM]], x: xN, y, font: fN, tb, sure: 0.4 }));
    S.koy(S.darbe(TIK(xN + olc(fN, m) + 44, y - 20), { w: 8, renk: SARI, alfa: 0.9, uc0: 5, uc1: 8 }, tb + 0.5, 0.16, 0.5));
  });

  // 40,96 goes: kartta sarı halka; alt formül `he + go-es` (Fredoka 130)
  S.koy(S.halka(kel("goes"), 40.96, 0.35, 12, 4));
  const yF = 1350, bs = 30, f110 = FF(130);
  const par = [[["he", KREM]], [["+", IKI]], [["go", KREM]], [["-es", SARI]]];
  const gw = par.map((p) => olc(f110, p[0][0]));
  const tF = [41.3, 41.55, 41.75, 42.1], gap = [bs, bs, 2];
  let xF = (1080 - gw.reduce((a, b) => a + b, 0) - gap.reduce((a, b) => a + b, 0)) / 2;
  par.forEach((p, i) => {
    S.koy(S.metinPop({ parca: p, x: xF, y: yF, font: f110, tb: tF[i], sure: 0.3, ses: i === 0 || i === 3 ? 0.5 : false }));
    xF += gw[i] + (gap[i] == null ? 0 : gap[i]);
  });
  S.koy(S.parilti(xF + 20, yF - 90, 42.5, 26));
}

surucu(kur, (f) => S.kare(f), KARE);

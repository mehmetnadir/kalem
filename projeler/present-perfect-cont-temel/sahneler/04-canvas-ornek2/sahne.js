// SAHNE 04 — Örnek 2 (PPC temel, düz canvas, 462 kare, t_bas 32,28; cümle 4). Kendini çizen kalem.
// Zaman yalnız kare numarasından; zamanlar küresel sn (sozcukler.json ile aynı çerçeve), kayma yok.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, ok, geriTasma } from "./sahne-ortak.js";
import { yaziNoktalari } from "/projeler/present-perfect-cont-temel/ortak/kalem-canvas.js";

const KARE = 462, TBAS = 32.28, ICERIK = 450;
const KOKDIZ = "/projeler/present-perfect-cont-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
// t1 < 0,2 sn olan sözcük penceresi sonraki sözcüğün başına dek uzar (karar 6)
const pencere = (liste) => liste.map((w, i, a) => ({ t0: w.t0,
  t1: w.t1 - w.t0 < 0.2 && a[i + 1] ? a[i + 1].t0 : w.t1 }));
// El yazısı (Caveat 700 tegaki, dalga 5b-2 / K26): ortalı etiketin genişliği tegaki verisinden
const eyGen = (str, boy) => yaziNoktalari(str, S.EY.G, { upm: S.EY.M.unitsPerEm,
  asc: S.EY.M.ascender, boy, x: 0, taban: 0 }).gen;
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

async function kur() {
  await S.kur();
  const [kardes, gitar, nota, gunes] = await Promise.all([svgOku("open-peeps/sitting-2.svg"),
    svgOku("coco/guitar.svg"), svgOku("tabler/music.svg"), svgOku("coco/sun.svg")]);

  // 32,83–33,87 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 190, 205, 32.83));

  // 34,12–37,48 cümle + sarı alt çizgi
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("My", 34.12, 10), x: 140, y: 330, maxGen: 980 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 34,2–37,4 kardeş (sitting-2) + gitar (440 px) + 3 nota teker teker
  S.koy(S.cizim({ svg: kardes, kutu: { x: 1450, y: 190, w: 380, h: 580 }, ad: "kardes", esik: 0.004, enCok: 60,
    w: 3.4, tb: 34.2, sure: 1.8, olayEnCok: 7 }));
  S.koy(S.cizim({ svg: gitar, ad: "gitar", kutu: { x: 1120, y: 300, w: 330, h: 440 }, enCok: 24, w: 3.8, tb: 35.4,
    sure: 1.1, olayEnCok: 4 }));
  [[1130, 190, 35.9], [1240, 140, 36.5], [1340, 200, 37.1]].forEach(([x, y, tb], i) => {
    const g = S.cizim({ svg: nota, kutu: { x, y, w: 100, h: 100 }, ad: "nota", enCok: 4, w: 3.6, tb, sure: 0.5,
      olayEnCok: 1, nefes: false });
    g.donusum = (f) => ({ cx: x, cy: y, tx: 0, ty: f < S.fr(tb + 0.5) ? 0 :
      4 * Math.sin((Math.min(f, ICERIK) - S.fr(tb + 0.5)) / 15 + i * 2), dondur: 0, olcek: 1 });
    S.koy(g); S.koy(S.parilti(x + 60, y + 48, tb + 0.45));
  });

  // 35,96–37,48 zaman çizgisi: güneş (this morning) → kalem oku → now
  {
    const yT = 620, nx = 800, nf = S.fr(37.1);
    S.koy(S.cizim({ svg: gunes, ad: "gunes", kutu: { x: 140, y: yT - 70, w: 110, h: 110 }, enCok: 24, w: 3.8,
      tb: 35.96, sure: 0.6, olayEnCok: 3, nefes: false }));
    // 36,28–36,98 «this morning»: pencere yok («this» 0,08 sn); anlatım 36,28–37,48 içinde,
    // hedef 0,7 sn
    S.koy(S.elYazisi({ metin: "this morning", x: 195 - eyGen("this morning", 36) / 2, y: yT + 90,
      boy: 36, renk: SARI, tb: 36.28, sure: 0.7, ses: 0.5 }));
    S.koy(S.darbeler(ok([290, yT - 15], [nx - 60, yT - 15], 3), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 36.6,
      0.2, 0.12, 0.5));
    S.olay(nf, "tik", 0.5);
    S.koy({ ciz: (ctx, f) => {
      const u = geriTasma((f - nf) / 10); if (u <= 0) return;
      ctx.save(); ctx.fillStyle = renkCoz(SARI); ctx.beginPath(); ctx.arc(nx, yT - 15, 13 * u, 0, Math.PI * 2);
      ctx.fill(); ctx.restore();
    } });
    S.koy(S.nabiz(nx, yT - 15, 13, 37.1));
    // 37,20–37,65 anlatımsız etiket `now`: hedef 0,45 sn; x ortalı
    S.koy(S.elYazisi({ metin: "now", x: nx - eyGen("now", 36) / 2, y: yT + 50, boy: 36, renk: SARI,
      tb: 37.2, sure: 0.45, ses: false }));
  }

  // 37,73–40,37 Türkçe çeviri
  const ytr = sonSatir + 78;
  // pencere: Kardeşim 37,73–38,29 · sabahtan 38,37–38,77 · beri 38,85→39,05 · gitar 39,05–39,33 ·
  // çalıyor. 39,41–40,37
  S.koy(S.elYazisi({ metin: "Kardeşim sabahtan beri gitar çalıyor.", x: 140, y: ytr, renk: IKINCIL,
    sozcukler: pencere(S.dizi("Kardeşim", 37.73, 5)) }));

  // 40,62–42,22 since (Fredoka 130 sarı) + soluk for = süre uzunluğu; 42,47 başlangıç noktası
  S.koy(S.metinPop({ parca: [["since", SARI]], x: 1010, y: 870, font: "700 130px Fredoka", tb: 40.62, sure: 0.4,
    olcek0: 0.6, ses: 0.8, turu: "vurus" }));
  // 41,30–42,10 anlatımsız (Since this morning. 41,26–42,22 içinde): hedef 0,8 sn
  S.koy(S.elYazisi({ metin: "for = süre uzunluğu", x: 1010, y: 1000, boy: 44, renk: IKINCIL,
    tb: 41.3, sure: 0.8, ses: false }));
  // pencere: başlangıç 42,47–43,07 · noktası. 43,11–44,15
  S.koy(S.elYazisi({ metin: "başlangıç noktası", x: 1010, y: 940, boy: 56, renk: SARI,
    sozcukler: pencere(S.dizi("Başlangıç", 42.47, 2)) }));
  S.koy(S.parilti(1330, 790, 40.9));

  // 45,11 has: cümlede sarı daire
  S.koy(S.halka(kel("has"), 45.11, 0.3, 11));

  // 44,23–47,27 formül kartı: has been + V-ing / play-ing
  {
    const ky = 745, F = "700 60px Fredoka";
    S.koy(S.kart({ x: 140, y: ky, w: 640, h: 235, tb: 44.23, tohum: 4, satirlar: [
      { parca: [["has been", KREM]], x: 200, y: ky + 95, font: F, tb: 45.11 },
      { parca: [["+", IKINCIL]], x: 480, y: ky + 95, font: F, tb: 46.07 },
      { parca: [["V", KREM], ["-ing", SARI]], x: 560, y: ky + 95, font: F, tb: 46.3 },
      { parca: [["play", KREM], ["-ing", SARI]], x: 200, y: ky + 200, font: F, tb: 46.63 },
    ] }));
    S.koy(S.parilti(740, 770, 46.9));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

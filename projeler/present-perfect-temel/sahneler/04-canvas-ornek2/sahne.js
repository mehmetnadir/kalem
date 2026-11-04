// SAHNE 04 — Örnek 2 (düz canvas, 521 kare, t_bas 34,16; cümle 4). Kendini çizen kalem; zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, ok, geriTasma } from "./sahne-ortak.js";

const KARE = 521, TBAS = 34.16, ICERIK = 509;
const KOKDIZ = "/projeler/present-perfect-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

async function kur() {
  await S.kur();
  const [kardes, gitar, nota] = await Promise.all([svgOku("open-peeps/sitting-6.svg"), svgOku("coco/guitar.svg"),
    svgOku("tabler/music.svg")]);

  // 34,71–35,5 daire içinde 2
  S.koy(S.daireSayi(2, 190, 205, 34.71));

  // 36,00–39,12 cümle + sarı alt çizgi (My … years.)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("My", 36.0, 9), x: 140, y: 330, maxGen: 980 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 36,2–38,6 oturan figür (sitting-6) + gitar (420 px) + 3 nota
  S.koy(S.cizim({ svg: kardes, kutu: { x: 1480, y: 200, w: 360, h: 560 }, ad: "figur", esik: 0.004, enCok: 60, w: 3.4,
    tb: 36.2, sure: 1.8, olayEnCok: 7 }));
  S.koy(S.cizim({ svg: gitar, ad: "gitar", kutu: { x: 1150, y: 330, w: 300, h: 420 }, enCok: 24, w: 3.8, tb: 37.5,
    sure: 1.1, olayEnCok: 4 }));
  [[1160, 220, 39.4], [1280, 170, 40.1], [1390, 235, 40.8]].forEach(([x, y, tb], i) => {
    const g = S.cizim({ svg: nota, kutu: { x, y, w: 110, h: 110 }, ad: "nota", enCok: 4, w: 3.6, tb, sure: 0.5,
      olayEnCok: 1, nefes: false });
    g.donusum = (f) => ({ cx: x, cy: y, tx: 0, ty: f < S.fr(tb + 0.5) ? 0 :
      4 * Math.sin((Math.min(f, ICERIK) - S.fr(tb + 0.5)) / 15 + i * 2), dondur: 0, olcek: 1 });
    S.koy(g); S.koy(S.parilti(x + 62, y + 52, tb + 0.45));
  });

  // 39,37–41,0 Türkçe çeviri
  const ytr = sonSatir + 78;
  S.koy(S.not({ parca: [["Kardeşim beş yıldır gitar çalıyor.", IKINCIL]], x: 140, y: ytr, tb: 39.37, sure: 0.6 }));

  // 41,77–43,69 takvim şeridi: 5 el kutusu (5 years), sarı ayraç, sağ uçta now noktası
  const yEtiket = ytr + 76, yBrk = yEtiket + 14, yKutu = yBrk + 30, kh = 90;
  for (let i = 0; i < 5; i++) {
    S.koy(S.darbeler(kutu(140 + 170 * i, yKutu, 150, kh, 20 + i), { w: 3.4, renk: KREM, uc0: 8, uc1: 14 },
      41.77 + i * 0.2, 0.12, 0.07, 0.45));
  }
  S.koy(S.metinPop({ parca: [["5 years", SARI]], x: 140 + 415, y: yEtiket, font: "700 26px Lexend", hiza: "orta",
    tb: 42.1, sure: 0.35, ses: 0.5 }));
  S.koy(S.darbe([[140, yBrk + 18], [140, yBrk], [140 + 830, yBrk], [140 + 830, yBrk + 18]],
    { duz: true, w: 7, renk: SARI, alfa: 0.85, uc0: 12, uc1: 24 }, 42.15, 0.5, 0.6));
  const nx = 140 + 850 + 56, ny = yKutu + kh / 2, nf = S.fr(42.65);
  S.olay(nf, "tik", 0.5);
  S.koy({ ciz: (ctx, f) => {
    const u = geriTasma((f - nf) / 10); if (u <= 0) return;
    ctx.save(); ctx.fillStyle = renkCoz(SARI); ctx.beginPath(); ctx.arc(nx, ny, 13 * u, 0, Math.PI * 2); ctx.fill();
    ctx.restore();
  } });
  S.koy(S.darbe([[140 + 830 + 8, ny], [nx - 22, ny]], { duz: true, w: 5, renk: SARI, alfa: 0.85, uc0: 6, uc1: 10 },
    42.5, 0.2, false));
  S.koy(S.nabiz(nx, ny, 13, 42.65));
  S.koy(S.not({ parca: [["now", SARI]], x: nx - 30, y: yKutu + kh + 52, tb: 42.8, sure: 0.3, ses: false }));
  S.koy(S.not({ parca: [["başladı, hâlâ sürüyor", IKINCIL]], x: 140, y: yKutu + kh + 62, tb: 43.05, sure: 0.6 }));

  // 43,84–47,9 for → süre (sarı); 47,12 soluk since → başlangıç
  const yF = yKutu + kh + 150;
  S.koy(S.not({ parca: [["for → süre", SARI]], x: 140, y: yF, tb: 43.84, sure: 0.5 }));
  S.koy(S.not({ parca: [["since → başlangıç", IKINCIL]], x: 140, y: yF + 72, tb: 47.12, sure: 0.6 }));

  // 36,0–39,12 for (37,6) sarı daire; 48,32–51,12 has sarı daire (48,88), formül kartı has + played
  S.koy(S.halka(kel("for"), 37.6, 0.3, 11));
  S.koy(S.halka(kel("has"), 48.88, 0.35, 12));
  const ky = yF - 70, fo = "700 64px Fredoka";
  S.koy(S.kart({ x: 760, y: ky, w: 600, h: 170, tb: 48.32, tohum: 4, satirlar: [
    { parca: [["has", KREM]], x: 830, y: ky + 108, font: fo, tb: 48.88 },
    { parca: [["+", IKINCIL]], x: 1000, y: ky + 108, font: fo, tb: 49.6 },
    { parca: [["played", SARI]], x: 1080, y: ky + 108, font: fo, tb: 50.4 },
  ] }));
  S.koy(S.parilti(1330, ky + 20, 50.8, 24));
}

surucu(kur, (f) => S.kare(f), KARE);

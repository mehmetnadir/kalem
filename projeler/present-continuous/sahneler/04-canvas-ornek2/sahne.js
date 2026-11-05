// SAHNE 04 — Örnek 2 (düz canvas, 487 kare, t_bas 36,15; cümle 4). Kendini çizen kalem; zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, ok, geriTasma } from "./sahne-ortak.js";

const KARE = 487, TBAS = 36.15, ICERIK = 475, KAYMA = 6.0;   // TBAS: eski çerçeve; zaman.json t_bas 30,15
const KOKDIZ = "/projeler/present-continuous/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: KAYMA, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

async function kur() {
  await S.kur();
  const [kiz, piyano, nota] = await Promise.all([svgOku("open-peeps/sitting-2.svg"), svgOku("tabler/piano.svg"), svgOku("tabler/music.svg")]);

  // 36,15–37,19 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 190, 205, S.zm(12)));

  // 37,44–39,76 cümle + sarı alt çizgi
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("My", 37.44, 8), x: 140, y: 330, maxGen: 980 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 37,6–39,6 kız kardeş (Peeps) + piyano + 3 nota
  S.koy(S.cizim({ svg: kiz, kutu: { x: 1440, y: 200, w: 400, h: 620 }, ad: "kiz", esik: 0.004, enCok: 60, w: 3.2, tb: 37.6, sure: 1.8, olayEnCok: 7 }));
  S.koy(S.cizim({ svg: piyano, ad: "piyano", kutu: { x: 1060, y: 480, w: 420, h: 420 }, enCok: 6, w: 3.8, tb: 38.5, sure: 0.9, olayEnCok: 4 }));
  [[1080, 380, 39.0], [1200, 320, 39.55], [1310, 390, 40.1]].forEach(([x, y, tb], i) => {
    const g = S.cizim({ svg: nota, kutu: { x, y, w: 110, h: 110 }, ad: "nota", enCok: 4, w: 3.6, tb, sure: 0.5, olayEnCok: 1, nefes: false });
    g.donusum = (f) => ({ cx: x, cy: y, tx: 0, ty: f < S.fr(tb + 0.5) ? 0 : 4 * Math.sin((Math.min(f, ICERIK) - S.fr(tb + 0.5)) / 15 + i * 2), dondur: 0, olcek: 1 });
    S.koy(g); S.koy(S.parilti(x + 62, y + 52, tb + 0.45));
  });

  // 40,89–43,37 Türkçe çeviri: el yazısı, her sözcük kendi konuşma penceresinde (pilot 05.11, karar 5–6)
  const ytr = sonSatir + 78;
  S.koy(S.elYazisi({ metin: "Kardeşim bu dönem piyano dersi alıyor.", x: 140, y: ytr, renk: IKINCIL,
    sozcukler: S.dizi("Kardeşim", 40.89, 6) }));

  // 43,41–46,65 takvim şeridi: 5 el kutusu, bracket, now noktası
  const yEtiket = ytr + 76, yBrk = yEtiket + 14, yKutu = yBrk + 30, kh = 90;
  for (let i = 0; i < 5; i++) {
    S.koy(S.darbeler(altKutu(140 + 170 * i, yKutu, 150, kh, 20 + i), { w: 3.4, renk: KREM, uc0: 8, uc1: 14 }, 43.41 + i * 0.22, 0.12, 0.07, 0.45));
  }
  const nx = 140 + 170 * 2 + 75, ny = yKutu + kh / 2, nf = S.fr(44.65);
  S.olay(nf, "tik", 0.5);
  S.koy({ ciz: (ctx, f) => {
    const u = geriTasma((f - nf) / 10); if (u <= 0) return;
    ctx.save(); ctx.fillStyle = renkCoz(SARI); ctx.beginPath(); ctx.arc(nx, ny, 13 * u, 0, Math.PI * 2); ctx.fill(); ctx.restore();
  } });
  S.koy(S.nabiz(nx, ny, 13, 44.65));
  S.koy(S.not({ parca: [["now", SARI]], x: nx - 38, y: yKutu + kh + 52, tb: 44.8, sure: 0.3, ses: false }));
  const n1 = S.not({ parca: [["not at this moment", IKINCIL]], x: 140, y: yKutu + kh + 112, tb: 44.9, sure: 0.5 });
  S.koy(n1);
  S.koy(S.metinPop({ parca: [["this semester", SARI]], x: nx, y: yEtiket, font: "700 26px Lexend", hiza: "orta", tb: 45.53, sure: 0.35, ses: 0.5 }));
  S.koy(S.darbe([[140, yBrk + 18], [140, yBrk], [140 + 830, yBrk], [140 + 830, yBrk + 18]],
    { duz: true, w: 7, renk: SARI, alfa: 0.85, uc0: 12, uc1: 24 }, 45.55, 0.5, 0.6));
  const ax = 140 + n1.w + 22, ay = yKutu + kh + 112 - 16;
  S.koy(S.darbeler(ok([ax, ay], [ax + 62, ay], 3), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 46.0, 0.18, 0.12, 0.5));
  S.koy(S.not({ parca: [["these days", SARI]], x: ax + 82, y: yKutu + kh + 112, tb: 46.15, sure: 0.4, ses: false }));

  // 47,12–47,92 is / taking daire (sözcük başlarında)
  S.koy(S.halka(kel("is"), 47.6, 0.3, 11));
  S.koy(S.halka(kel("taking"), 47.92, 0.35, 12));

  // 49,03–50,63 formül kartı: be + V-ing / is / tak-ing
  const ky = yKutu + kh + 112 + 28, fo = "700 60px Fredoka", fo2 = "700 52px Fredoka";
  S.koy(S.kart({ x: 230, y: ky, w: 700, h: 156, tb: 49.03, tohum: 4, satirlar: [
    { parca: [["be", KREM]], x: 300, y: ky + 62, font: fo, tb: 49.03 },
    { parca: [["+", IKINCIL]], x: 450, y: ky + 62, font: fo, tb: 50.0 },
    { parca: [["V", KREM], ["-ing", SARI]], x: 540, y: ky + 62, font: fo, tb: 50.23 },
    { parca: [["is", KREM]], x: 300, y: ky + 128, font: fo2, tb: 49.4 },
    { parca: [["tak", KREM], ["-ing", SARI]], x: 540, y: ky + 128, font: fo2, tb: 50.5 },
  ] }));
}

const altKutu = kutu;

surucu(kur, (f) => S.kare(f), KARE);

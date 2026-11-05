// SAHNE 04 (DİKEY) — Örnek 2: düz canvas, 1080x1920, 521 kare, t_bas 34,16; cümle 4.
// Zaman yalnız kare numarasından; zamanlar sozcukler.json / altyazi.json ile aynı çerçevede (küresel sn).
// Yerleşim sıfırdan dikey: kart (tam genişlik) → TR çeviri → ORTA figür + gitar (sol), notlar (sağ)
// → takvim şeridi `5 years` → alt formül.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, olc, geriTasma } from "./sahne-ortak.js";

const KARE = 521, TBAS = 34.16, ICERIK = 509;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 2 / 3", cumle: 4 });
const KOKDIZ = "/projeler/present-perfect-temel-dikey/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKI = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;
// El yazısı (tegaki Caveat, dalga 5 / K26): sözcük penceresi = anlatım t0/t1 (küresel sn)
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

async function kur() {
  await S.kur();
  const [kardes, gitar, nota] = await Promise.all([svgOku("open-peeps/sitting-6.svg"), svgOku("coco/guitar.svg"),
    svgOku("tabler/music.svg")]);

  // kart: tam genişlik 984, Fredoka 72, sözcük zamanlı (ilk 12 kare boş; kutu 12. kareden çizilir)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("My", 36.0, 9), x: 88, y: 470, maxGen: 904, font: FF(72),
    satirH: 88 }));
  const sonTaban = Math.max(...cum.kel.map((k) => k.y)), kartAlt = sonTaban + 20 + 28;
  S.koy(S.darbeler(kutu(48, 372, 984, kartAlt - 372, 7), { w: 4, renk: IKI, uc0: 10, uc1: 18 }, S.zm(12), 0.2,
    0.12, 0.55));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 39,37 Türkçe çeviri (Caveat 64, mürekkep)
  const yTR = kartAlt + 58;
  // 39,37–41,45 «Kardeşim beş yıldır gitar çalıyor.» (pencere: 5 sözcük)
  S.koy(S.elYazisi({ metin: "Kardeşim beş yıldır gitar çalıyor.", x: 64, y: yTR, boy: 64,
    renk: KREM, sozcukler: pen("Kardeşim", 39.37, 5) }));

  // ORTA sol: figür (sitting-6) + gitar, ≥ 420 px; sağ sütunda 3 nota
  const fUst = yTR + 28, fAlt = fUst + 430;
  S.koy(S.cizim({ svg: kardes, kutu: { x: 56, y: fUst, w: 330, h: fAlt - fUst }, ad: "figur", esik: 0.004, enCok: 60,
    w: 4.4, tb: 36.2, sure: 1.8, olayEnCok: 7 }));
  S.koy(S.cizim({ svg: gitar, ad: "gitar", kutu: { x: 335, y: fUst + 80, w: 215, h: fAlt - fUst - 80 }, enCok: 24, w: 4,
    tb: 37.5, sure: 1.1, olayEnCok: 4 }));
  [[620, fUst - 4, 39.4], [750, fUst - 22, 40.1], [880, fUst + 2, 40.8]].forEach(([x, y, tb], i) => {
    const g = S.cizim({ svg: nota, kutu: { x, y, w: 100, h: 100 }, ad: "nota", enCok: 4, w: 4, tb, sure: 0.5,
      olayEnCok: 1, nefes: false });
    g.donusum = (f) => ({ cx: x, cy: y, tx: 0, ty: f < S.fr(tb + 0.5) ? 0 :
      6 * Math.sin((Math.min(f, ICERIK) - S.fr(tb + 0.5)) / 15 + i * 2), dondur: 0, olcek: 1 });
    S.koy(g); S.koy(S.parilti(x + 62, y + 40, tb + 0.45));
  });

  // 37,6 for sarı daire (kartta)
  S.koy(S.halka(kel("for"), 37.6, 0.3, 11, 4));

  // sağ sütun notları: başladı / hâlâ sürüyor (41,77 / 42,65); for → süre (43,84); since → başlangıç (47,12)
  const xS = 600, y0 = fUst + 160;
  // 41,77–42,25 «Başladı» (pencere: 1 sözcük)
  S.koy(S.elYazisi({ metin: "başladı,", x: xS, y: y0, boy: 64, renk: KREM,
    sozcukler: pen("Başladı", 41.77, 1) }));
  S.koy(S.not({ parca: [["hâlâ sürüyor", SARI]], x: xS, y: y0 + 72, font: CV(64), tb: 42.65, sure: 0.55 }));
  S.koy(S.not({ parca: [["for → süre", SARI]], x: xS, y: y0 + 170, font: CV(72), tb: 43.84, sure: 0.55 }));
  S.koy(S.not({ parca: [["since → başlangıç", IKI]], x: xS - 40, y: y0 + 246, font: CV(72), tb: 47.12, sure: 0.7 }));

  // takvim şeridi (41,77–42,9): 5 el kutusu, sarı ayraç `5 years`, sağ uçta now noktası (42,65)
  const yB = fAlt + 78, yK = yB + 24, kh = 70, kx = (i) => 70 + 180 * i;
  for (let i = 0; i < 5; i++) {
    S.koy(S.darbeler(kutu(kx(i), yK, 150, kh, 20 + i), { w: 4, renk: KREM, uc0: 8, uc1: 14 },
      41.77 + i * 0.2, 0.12, 0.07, 0.45));
  }
  // 42,10 anlatımsız etiket `5 years`: hedef 0,45 sn → 42,55
  S.koy(S.elYazisi({ metin: "5 years", x: 70, y: yB - 14, boy: 64, renk: SARI, tb: 42.1,
    sure: 0.45 }));
  S.koy(S.darbe([[70, yB + 16], [70, yB], [940, yB], [940, yB + 16]],
    { duz: true, w: 9, renk: SARI, alfa: 0.85, uc0: 12, uc1: 24 }, 42.15, 0.5, 0.6));
  const nx = 985, ny = yK + kh / 2, nf = S.fr(42.65);
  S.olay(nf, "tik", 0.5);
  S.koy({ ciz: (ctx, f) => {
    const u = geriTasma((f - nf) / 10); if (u <= 0) return;
    ctx.save(); ctx.fillStyle = renkCoz(SARI); ctx.beginPath(); ctx.arc(nx, ny, 15 * u, 0, Math.PI * 2); ctx.fill();
    ctx.restore();
  } });
  S.koy(S.darbe([[948, ny], [nx - 26, ny]], { duz: true, w: 6, renk: SARI, alfa: 0.85, uc0: 6, uc1: 10 }, 42.5, 0.2,
    false));
  S.koy(S.nabiz(nx, ny, 15, 42.65));
  // 42,80 anlatımsız etiket `now`: hedef 0,45 sn → 43,25
  S.koy(S.elYazisi({ metin: "now", x: nx - 40, y: yB, boy: 64, renk: SARI, tb: 42.8, sure: 0.45,
    ses: false }));

  // 48,88 has sarı daire; alt formül (Fredoka 110): has + played (48,88 / 49,6 / 50,4)
  S.koy(S.halka(kel("has"), 48.88, 0.35, 12, 4));
  const yF = 1384, f = FF(110), gen = [olc(f, "has"), olc(f, "+"), olc(f, "played")], bs = 26;
  let x = (1080 - gen.reduce((a, b) => a + b, 0) - bs * 2) / 2;
  [[["has", KREM]], [["+", IKI]], [["played", SARI]]].forEach((p, i) => {
    S.koy(S.metinPop({ parca: p, x, y: yF, font: f, tb: [48.88, 49.6, 50.4][i], sure: 0.3, ses: i !== 1 ? 0.5 : false }));
    x += gen[i] + bs;
  });
  S.koy(S.parilti(930, yF - 40, 50.8, 24));
}

surucu(kur, (f) => S.kare(f), KARE);

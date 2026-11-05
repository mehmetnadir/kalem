// SAHNE 05 (DİKEY, İLERİ) — Örnek 3: düz canvas, 1080x1920, 372 kare, t_bas 42,07; cümle 5; çıkış geçişi fade.
// Zaman yalnız kare numarasından; zamanlar sozcukler.json / altyazi.json ile aynı çerçevede (küresel sn).
// Yerleşim sıfırdan dikey: kart (tam genişlik) → TR çeviri → ORTA yolcu + otobüs + takvim/saat → alt formül.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, elips, kutu, olc } from "./sahne-ortak.js";

const KARE = 372, TBAS = 42.07, ICERIK = 360;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5 });
const KOKDIZ = "/projeler/present-continuous-ileri-dikey/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKI = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`;

async function kur() {
  await S.kur();
  const [otobus, takvim, saat, yolcu] = await Promise.all([svgOku("tabler/bus.svg"),
    svgOku("tabler/calendar.svg"), svgOku("tabler/clock.svg"), svgOku("open-peeps/standing-4.svg")]);

  // kart: tam genişlik 984, Fredoka 64, sözcük zamanlı (ilk 12 kare boş; kutu 12. kareden çizilir)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("We", 43.83, 16), x: 88, y: 452, maxGen: 904, font: FF(64),
    satirH: 80 }));
  const sonTaban = Math.max(...cum.kel.map((k) => k.y)), kartAlt = sonTaban + 24 + 34;
  S.koy(S.darbeler(kutu(48, 372, 984, kartAlt - 372, 9), { w: 4, renk: IKI, uc0: 10, uc1: 18 }, S.zm(12), 0.2,
    0.12, 0.55));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);
  const halkaIki = (a, b, tb, tohum) => {
    if (a.satir === b.satir) S.koy(S.halka({ x: a.x, y: a.y, w: b.x + b.w - a.x }, tb, 0.4, tohum, 5));
    else { S.koy(S.halka(a, tb, 0.3, tohum, 5)); S.koy(S.halka(b, tb + 0.16, 0.3, tohum + 1, 5)); }
  };
  halkaIki(kel("are"), kel("taking"), 43.99, 31);                 // are taking
  halkaIki(kel("am"), kel("packing"), 46.98, 33);                 // am packing
  S.koy(S.halka(kel("tonight."), 47.83, 0.35, 35, 5));            // tonight
  const tm = kel("tomorrow"), mo = kel("morning,");               // 45,43–45,83 tomorrow morning altı sarı
  const alt = (x0, x1, y, i) => S.koy(S.darbe([[x0 - 4, y + 4], [(x0 + x1) / 2, y + 7], [x1 + 4, y + 3]],
    { w: 10, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 520 + i }, 45.45 + i * 0.2, 0.4, 0.55));
  if (tm.satir === mo.satir) alt(tm.x, mo.x + mo.w, tm.y + 16, 0);
  else { alt(tm.x, tm.x + tm.w, tm.y + 16, 0); alt(mo.x, mo.x + mo.w, mo.y + 16, 1); }

  // 49,04 Türkçe çeviri (Caveat 64, mürekkep)
  const yTR = kartAlt + 62;
  S.koy(S.elYazisi({ metin: "Yarın sabah İzmir'e gidiyoruz.", x: 64, y: yTR, boy: 64, renk: KREM,
    sozcukler: S.dizi("Yarın", 49.04, 4).map((k) => ({ t0: k.t0, t1: k.t1 })) }));

  // ORTA bant: yolcu (standing-4) + otobüs + takvim; sağ sütun: yarın → PLAN, bilet ✓, saat ✓
  const B0 = yTR + 34, B1 = 1190, BH = B1 - B0;
  S.koy(S.cizim({ svg: otobus, ad: "otobus", kutu: { x: 245, y: B1 - 0.804 * 440 - 4, w: 440, h: 440 }, enCok: 12,
    w: 4.2, tb: 43.95, sure: 1.2, olayEnCok: 5 }));
  S.koy(S.cizim({ svg: yolcu, ad: "yolcu", kutu: { x: 40, y: B0, w: 210, h: BH }, esik: 0.004, enCok: 50,
    w: 4.4, tb: 45.9, sure: 1.5, olayEnCok: 5 }));
  S.koy(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 404, y: B0 - 30, w: 168, h: 168 }, enCok: 8, w: 4.2,
    tb: 45.1, sure: 0.8, olayEnCok: 3 }));
  S.koy(S.darbe([[30, B1 + 4], [400, B1 + 8], [700, B1 + 3]], { duz: true, w: 4, renk: IKI, alfa: 0.8, uc0: 6,
    uc1: 10, tohum: 77 }, 46.7, 0.45, 0.45));
  S.koy(S.parilti(540, B0 + 16, 47.4, 28));

  const yx = 600, yy = B0 + 80;                    // "yarın" etiketi (takvimin sağında)
  const yz = S.elYazisi({ metin: "yarın", x: yx, y: yy, boy: 64, renk: KREM, tb: 49.4,
    sure: 0.45 });
  S.koy(yz);
  const yw = yz.w;                                 // tegaki genişliği (115 px)
  // 51,12 yarın sarı daire → ok → PLAN
  S.koy(S.darbe(elips(yx + yw / 2, yy - 22, yw / 2 + 28, 48, -0.04, 41), { w: 9, renk: SARI, alfa: 0.85, uc0: 14,
    uc1: 30 }, 51.14, 0.4, 0.55));
  S.koy(S.darbeler(ok([yx + yw + 36, yy - 26], [yx + yw + 112, yy - 26], 4), { w: 9, renk: SARI, uc0: 10, uc1: 14 },
    51.5, 0.3, 0.2, 0.5));
  S.koy(S.elYazisi({ metin: "PLAN", x: yx + yw + 130, y: yy - 2, boy: 88, renk: SARI, tb: 51.8,
    sure: 0.4 }));

  // 52,20 sağ sütun: bilet ✓ (52,40), saat (53,04) ✓
  const bx = 720, by = B0 + 150, bw = 310, bh = 100, fb = FF(56);
  S.koy(S.darbeler(kutu(bx, by, bw, bh, 61), { w: 4.2, renk: KREM, uc0: 8, uc1: 14 }, 52.22, 0.1, 0.06, false));
  S.koy(S.metinPop({ parca: [["bilet", KREM]], x: bx + 26, y: by + 70, font: fb, tb: 52.3, sure: 0.3, ses: 0.5 }));
  const tx = bx + 26 + olc(fb, "bilet") + 34;
  S.koy(S.darbe([[tx, by + 50], [tx + 24, by + 74], [tx + 68, by + 22]], { w: 10, renk: SARI, alfa: 0.9, uc0: 4,
    uc1: 10, tohum: 63 }, 52.4, 0.3, 0.55));
  const cy0 = by + bh + 30;
  S.koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 720, y: cy0, w: 200, h: Math.min(200, B1 - cy0 + 24) }, enCok: 4,
    w: 4.4, tb: 52.7, sure: 0.6, olayEnCok: 2 }));
  S.koy(S.darbe([[930, cy0 + 100], [954, cy0 + 126], [1004, cy0 + 72]], { w: 10, renk: SARI, alfa: 0.9, uc0: 4,
    uc1: 10, tohum: 65 }, 53.04, 0.3, 0.55));

  // alt formül (Fredoka 100): are + tak-ing (53,58) / am + pack-ing (53,66)
  const yA = 1285, yB = 1383, fz = FF(96);
  const satir = (parcalar, y, tb) => {
    const gen = parcalar.map(([m]) => olc(fz, m)), bs = 22;
    let x = (1080 - gen.reduce((a, b) => a + b, 0) - bs * (parcalar.length - 1)) / 2;
    parcalar.forEach(([m, r], i) => { S.koy(S.metinPop({ parca: [[m, r]], x, y, font: fz, tb: tb + i * 0.08,
      sure: 0.3, ses: i === 0 ? 0.5 : false })); x += gen[i] + bs; });
  };
  const A = [["are", KREM], ["+", IKI], ["tak", KREM], ["-ing", SARI]], Bq = [["am", KREM], ["+", IKI], ["pack", KREM],
    ["-ing", SARI]];
  satir(A, yA, 53.4); satir(Bq, yB, 53.62);
  S.koy(S.parilti(960, yB - 90, 53.9, 24));
}

surucu(kur, (f) => S.kare(f), KARE);

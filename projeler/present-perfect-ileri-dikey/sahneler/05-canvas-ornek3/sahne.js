// SAHNE 05 (DİKEY, İLERİ) — Kök 3, tuzak: düz canvas, 1080x1920, 532 kare, t_bas 51,25; cümle 5; çıkış fade.
// Zaman yalnız kare numarasından; sözcük zamanları sozcukler.json (küresel sn).
// Yerleşim sıfırdan dikey (içerik bandı 352–1392): kart (rozet 3 + TUZAK + cümle) → TR çeviri →
// ORTA: solda saat + zaman çizgisi, sağda uçak (450 px) kalkış eğrisi → alt: iki etiket (yığılı).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, kutu, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 532, TBAS = 51.25, ICERIK = 520;
const KOKDIZ = "/projeler/present-perfect-ileri-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Trap 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKI = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const [ucak, saat] = await Promise.all([svgOku("tabler/plane.svg"), svgOku("tabler/clock.svg")]);

  // kart (tam genişlik 984): 12. kareden çizilir; içinde rozet 3 + TUZAK + cümle
  S.koy(S.darbeler(kutu(48, 372, 984, 306, 9), { w: 4, renk: IKI, uc0: 10, uc1: 18 }, S.zm(12), 0.2, 0.12, 0.55));
  S.koy(S.daireSayi(3, 120, 446, 51.82));
  S.koy(S.not({ parca: [["TUZAK", KIRMIZI]], x: 760, y: 464, font: CV(88), tb: 53.0, sure: 0.5, ses: 0.6 }));

  // 54,21–58,05 cümle (Fredoka 64, 3 satır 4 / 5 / 3 sözcük, sözcük zamanlı)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("The", 54.21, 12), x: 214, y: 452, maxGen: 800, font: FF(64),
    satirH: 86, satirSay: [4, 5, 3], bosluk: 4 }));
  const kel = (i) => cum.kel[i];   // 0 The 1 plane 2 took 3 off | 4 two 5 hours 6 ago, 7 but 8 it | 9 hasn't 10 landed 11 yet.
  const a = kel(4), z = kel(6);    // 55,09 two hours ago: kırmızı alt çizgi (tuzak)
  S.koy(S.darbe(altCizgi(a.x - 4, z.x + z.w + 4, a.y + 22, 61), { w: 10, renk: KIRMIZI, alfa: 0.9, uc0: 8, uc1: 14,
    tohum: 610 }, 55.09, 0.5, 0.55));
  const h = kel(9), y = kel(11);   // 56,61 hasn't landed yet: sarı daire
  S.koy(S.darbe(elips((h.x + y.x + y.w) / 2, h.y - 18, (y.x + y.w - h.x) / 2 + 26, 36, -0.03, 71),
    { w: 9, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, 56.61, 0.5, 0.55));

  // 58,30 Türkçe çeviri (Caveat 64, mürekkep, 2 satır)
  S.koy(S.not({ parca: [["Uçak iki saat önce kalktı, ama", KREM]], x: 64, y: 744, font: CV(64), tb: 58.3, sure: 1.2 }));
  S.koy(S.not({ parca: [["henüz inmedi.", KREM]], x: 64, y: 816, font: CV(64), tb: 59.55, sure: 0.6 }));

  // 54,3–58,0 sağ sütun: uçak (450 px) + kalkış eğrisi + zemin çizgisi; sol: saat + 2 saat
  S.koy(S.darbe([[570, 1190], [650, 1182], [720, 1160], [790, 1118], [830, 1080]], { w: 4, renk: IKI, alfa: 0.85,
    uc0: 8, uc1: 16, tohum: 93 }, 54.3, 0.7, 0.45));
  S.koy(S.cizim({ svg: ucak, ad: "ucak", kutu: { x: 584, y: 790, w: 450, h: 450 }, enCok: 12, w: 4.6, tb: 54.6,
    sure: 1.3, olayEnCok: 5 }));
  S.koy(S.darbe([[560, 1206], [800, 1209], [1032, 1204]], { duz: true, w: 4, renk: IKI, alfa: 0.8, uc0: 6, uc1: 10,
    tohum: 77 }, 55.0, 0.5, 0.4));
  S.koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 60, y: 832, w: 160, h: 160 }, enCok: 4, w: 4.4, tb: 55.1,
    sure: 0.7, olayEnCok: 3 }));
  S.koy(S.not({ parca: [["2 saat", KREM]], x: 250, y: 944, font: CV(72), tb: 55.9, sure: 0.4 }));
  S.koy(S.parilti(1000, 880, 57.5, 26));

  // 59,0–61,5 zaman çizgisi (sol sütun, 480 px): took off · now · unfinished
  const ty = 1080, x0 = 60, xTook = 150, xNow = 370, x1 = 520;
  S.koy(S.darbe([[x0, ty + 2], [(x0 + xNow) / 2, ty - 2], [xNow, ty + 1]], { w: 5, renk: KREM, uc0: 8, uc1: 14 },
    59.0, 0.6, 0.5));
  S.koy(S.darbe([[xTook, ty - 18], [xTook + 1, ty + 18]], { duz: true, w: 5, renk: KREM, uc0: 4, uc1: 6 }, 59.46,
    0.15, 0.5));
  S.koy(S.not({ parca: [["took off", KREM]], x: xTook - 54, y: ty - 36, font: CV(64), tb: 59.5, sure: 0.35 }));
  S.koy(S.darbe([[x0, ty + 44], [x0, ty + 60], [xNow, ty + 60], [xNow, ty + 44]], { duz: true, w: 5, renk: KREM,
    uc0: 8, uc1: 10 }, 59.7, 0.5, 0.5));
  S.koy(S.not({ parca: [["finished", KREM]], x: 74, y: ty + 126, font: CV(64), tb: 59.9, sure: 0.4 }));
  S.koy(S.darbe([[xNow, ty - 26], [xNow + 1, ty + 26]], { duz: true, w: 8, renk: SARI, alfa: 0.9, uc0: 4, uc1: 6 },
    60.3, 0.15, 0.5));
  S.koy(S.not({ parca: [["now", SARI]], x: xNow - 34, y: ty - 42, font: CV(72), tb: 60.4, sure: 0.3 }));
  for (let i = 0; i < 2; i++) {
    const xa = xNow + 14 + i * 64;
    S.koy(S.darbe([[xa, ty], [xa + 38, ty + 1]], { duz: true, w: 5, renk: SARI, alfa: 0.9, uc0: 6, uc1: 8 },
      60.54 + i * 0.2, 0.18, i === 0 ? 0.4 : false));
  }
  S.koy(S.not({ parca: [["unfinished", SARI]], x: 296, y: ty + 126, font: CV(64), tb: 60.8, sure: 0.5 }));

  // 61,65–65,33 kırmızı etiket (tuzak): ago → Simple Past · 65,48–68,60 sarı etiket: yet → Present Perfect
  const f64 = FF(64), bh = 70;
  const etiket = (by, renk, ilk, tIlk, tSon, son, tohum) => {
    S.koy(S.darbeler(kutu(48, by, 984, bh, tohum), { w: 4.4, renk, uc0: 8, uc1: 14 }, tIlk, 0.12, 0.08, 0.5));
    S.koy(S.metinPop({ parca: [[ilk, renk]], x: 84, y: by + 52, font: f64, tb: tIlk + 0.05, sure: 0.3, ses: 0.5 }));
    S.koy(S.metinPop({ parca: [["→ " + son, KREM]], x: 84 + olc(f64, ilk + " "), y: by + 52, font: f64, tb: tSon,
      sure: 0.35, ses: 0.5 }));
  };
  etiket(1240, KIRMIZI, "ago", 61.65, 64.05, "Simple Past", 81);
  etiket(1320, SARI, "yet", 65.48, 67.64, "Present Perfect", 83);
  S.koy(S.parilti(1000, 1320, 68.1, 26));
}

surucu(kur, (f) => S.kare(f), KARE);

// SAHNE 05 (İLERİ) — Kök 3, tuzak (düz canvas, 532 kare, t_bas 51,25; cümle 5; çıkış geçişi fade).
// Kök: "The plane took off two hours ago, but it hasn't landed yet." (ago → Simple Past, yet → Present Perfect).
// Zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json (küresel sn).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 532, TBAS = 51.25, ICERIK = 520;
const KOKDIZ = "/projeler/present-perfect-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Trap 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const [ucak, saat] = await Promise.all([svgOku("tabler/plane.svg"), svgOku("tabler/clock.svg")]);

  // 51,82 daire içinde 3 (ilk 12 kare boş) · 53,00 TUZAK (kırmızı, yalnız tuzak anında)
  S.koy(S.daireSayi(3, 200, 190, 51.82));
  S.koy(S.not({ parca: [["TUZAK", KIRMIZI]], x: 300, y: 218, font: CV(84), tb: 53.0, sure: 0.5, ses: 0.6 }));

  // 54,21–58,05 İngilizce kök (Fredoka 56, sözcük zamanlı); satırlar 4 / 5 / 3 sözcük
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("The", 54.21, 12), x: 140, y: 320, maxGen: 1000, font: FF(56),
    satirH: 96, satirSay: [4, 5, 3], bosluk: 4 }));
  const kel = (i) => cum.kel[i];   // 0 The 1 plane 2 took 3 off | 4 two 5 hours 6 ago, 7 but 8 it | 9 hasn't 10 landed 11 yet.
  // 55,09–55,65 two hours ago: kırmızı alt çizgi (tuzak)
  const a = kel(4), z = kel(6);
  S.koy(S.darbe(altCizgi(a.x - 4, z.x + z.w + 4, a.y + 22, 61), { w: 8, renk: KIRMIZI, alfa: 0.9, uc0: 8, uc1: 14,
    tohum: 610 }, 55.09, 0.5, 0.55));
  // 56,61–57,25 hasn't landed yet: sarı daire
  const h = kel(9), y = kel(11);
  S.koy(S.darbe(elips((h.x + y.x + y.w) / 2, h.y - 20, (y.x + y.w - h.x) / 2 + 40, 46, -0.03, 71),
    { w: 6, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, 56.61, 0.5, 0.55));

  // 54,3–58,0 sağ: uçak (440 px) kalkış eğrisi + yanında saat (2 saat)
  S.koy(S.darbe([[1130, 640], [1250, 632], [1340, 600], [1410, 548], [1450, 500]], { w: 3.4, renk: IKINCIL, alfa: 0.85,
    uc0: 8, uc1: 16, tohum: 93 }, 54.3, 0.7, 0.45));
  S.koy(S.cizim({ svg: ucak, ad: "ucak", kutu: { x: 1400, y: 150, w: 440, h: 440 }, enCok: 12, w: 4, tb: 54.6,
    sure: 1.3, olayEnCok: 5 }));
  S.koy(S.darbe([[1110, 664], [1500, 668], [1860, 662]], { duz: true, w: 3.4, renk: IKINCIL, alfa: 0.8, uc0: 6,
    uc1: 10, tohum: 77 }, 55.0, 0.5, 0.4));
  S.koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 1130, y: 160, w: 200, h: 200 }, enCok: 4, w: 4, tb: 55.1,
    sure: 0.7, olayEnCok: 3 }));
  S.koy(S.not({ parca: [["2 saat", KREM]], x: 1140, y: 420, font: CV(60), tb: 55.9, sure: 0.4 }));
  S.koy(S.not({ parca: [["not yet", SARI]], x: 1560, y: 730, font: CV(64), tb: 57.25, sure: 0.5 }));
  S.koy(S.parilti(1830, 200, 57.5, 24));

  // 58,30–61,5 Türkçe çeviri (Caveat 48 ikincil)
  S.koy(S.not({ parca: [["Uçak iki saat önce kalktı, ama henüz inmedi.", IKINCIL]], x: 140, y: 618, font: CV(48),
    tb: 58.3, sure: 1.9 }));

  // 59,0–61,5 zaman çizgisi: sol finished (took off), ortada now, sağ unfinished
  const ty = 706, x0 = 140, xTook = 330, xNow = 800, x1 = 1040;
  S.koy(S.darbe([[x0, ty + 2], [(x0 + xNow) / 2, ty - 2], [xNow, ty + 1]], { w: 4.2, renk: KREM, uc0: 8, uc1: 14 },
    59.0, 0.6, 0.5));
  S.koy(S.darbe([[xTook, ty - 16], [xTook + 1, ty + 16]], { duz: true, w: 4, renk: KREM, uc0: 4, uc1: 6 }, 59.46, 0.15,
    0.5));
  S.koy(S.not({ parca: [["took off", KREM]], x: xTook - 62, y: ty - 30, font: CV(48), tb: 59.5, sure: 0.35 }));
  S.koy(S.darbe([[x0, ty + 40], [x0, ty + 54], [xNow, ty + 54], [xNow, ty + 40]], { duz: true, w: 4.4, renk: KREM,
    uc0: 8, uc1: 10 }, 59.7, 0.5, 0.5));
  S.koy(S.not({ parca: [["finished", KREM]], x: 360, y: ty + 100, font: CV(60), tb: 59.9, sure: 0.4 }));
  S.koy(S.darbe([[xNow, ty - 22], [xNow + 1, ty + 22]], { duz: true, w: 6, renk: SARI, alfa: 0.9, uc0: 4, uc1: 6 },
    60.3, 0.15, 0.5));
  S.koy(S.not({ parca: [["now", SARI]], x: xNow - 36, y: ty - 36, font: CV(60), tb: 60.4, sure: 0.3 }));
  for (let i = 0; i < 3; i++) {
    const xa = xNow + 16 + i * 74;
    S.koy(S.darbe([[xa, ty], [xa + 44, ty + 1]], { duz: true, w: 4.2, renk: SARI, alfa: 0.9, uc0: 6, uc1: 8 },
      60.54 + i * 0.2, 0.18, i === 0 ? 0.4 : false));
  }
  S.koy(S.darbeler(ok([x1 - 8, ty + 1], [x1 + 30, ty + 1], 7), { w: 4.2, renk: SARI, uc0: 6, uc1: 8 }, 61.1, 0.2, 0.1,
    false));
  S.koy(S.not({ parca: [["unfinished", SARI]], x: xNow + 10, y: ty + 100, font: CV(60), tb: 60.8, sure: 0.5 }));

  // 61,65–65,33 kırmızı etiket: ago → Simple Past (took off)
  const f60 = FF(60), by = 860, bh = 96;
  S.koy(S.darbeler(kutu(140, by, 650, bh, 81), { w: 4.2, renk: KIRMIZI, uc0: 8, uc1: 14 }, 61.65, 0.12, 0.08, 0.5));
  S.koy(S.metinPop({ parca: [["ago", KIRMIZI]], x: 176, y: by + 68, font: f60, tb: 61.7, sure: 0.3, ses: 0.5 }));
  const aw = olc(f60, "ago ");
  S.koy(S.metinPop({ parca: [["→ ", KREM], ["Simple Past", KREM]], x: 176 + aw, y: by + 68, font: f60, tb: 64.05,
    sure: 0.35, ses: 0.5 }));
  S.koy(S.not({ parca: [["(took off)", IKINCIL]], x: 300, y: by + 134, font: CV(44), tb: 64.6, sure: 0.4 }));

  // 65,48–68,60 sarı etiket: yet → Present Perfect (hasn't landed)
  const ex = 900, ew = 800;
  S.koy(S.darbeler(kutu(ex, by, ew, bh, 83), { w: 4.2, renk: SARI, uc0: 8, uc1: 14 }, 65.48, 0.12, 0.08, 0.5));
  S.koy(S.metinPop({ parca: [["yet", SARI]], x: ex + 36, y: by + 68, font: f60, tb: 65.5, sure: 0.3, ses: 0.5 }));
  const yw = olc(f60, "yet ");
  S.koy(S.metinPop({ parca: [["→ ", KREM], ["Present Perfect", KREM]], x: ex + 36 + yw, y: by + 68, font: f60,
    tb: 67.64, sure: 0.35, ses: 0.5 }));
  S.koy(S.not({ parca: [["(hasn't landed)", IKINCIL]], x: ex + 36, y: by + 134, font: CV(44), tb: 68.0, sure: 0.4 }));
  S.koy(S.parilti(ex + ew - 40, by - 10, 68.1, 26));
}

surucu(kur, (f) => S.kare(f), KARE);

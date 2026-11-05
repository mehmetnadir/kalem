// SAHNE 04 (İLERİ) — Örnek 2 (düz canvas, 478 kare, t_bas 33,68; cümle 4). Kendini çizen kalem; zaman yalnız kare numarasından.
// Kök: "I have been reading this novel all week, but I have only finished two chapters." (süreç / sonuç).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu } from "./sahne-ortak.js";

const KARE = 478, TBAS = 33.68, ICERIK = 466;
const KOKDIZ = "/projeler/present-perfect-cont-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

async function kur() {
  await S.kur();
  const [okur, roman] = await Promise.all([svgOku("open-peeps/sitting-1.svg"), svgOku("tabler/book.svg")]);

  // 34,23–35,27 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 200, 190, 34.23));

  // 35,52–40,24 İngilizce kök (Fredoka 56, sözcük zamanlı, sarı alt çizgi kayar); satırlar 5 / 5 / 5 sözcük
  const F56 = "700 56px Fredoka";
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("I", 35.52, 15), x: 140, y: 340, maxGen: 1000, font: F56, satirH: 84,
    satirSay: [5, 5, 5], bosluk: 4 }));
  const kel = (i) => cum.kel[i];             // 1: I have been reading this | 2: novel all week, but I | 3: have only finished two chapters.
  const cevre = (a, b, tb, egim, tohum) => {                       // iki sözcüğe tek sarı daire
    const A = kel(a), B = kel(b);
    S.koy(S.darbe(elips((A.x + B.x + B.w) / 2, A.y - 19, (B.x + B.w - A.x) / 2 + 6, 37, egim, tohum),
      { w: 6, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, tb, 0.4, 0.55));
  };
  // all week (37,04–37,60): sarı alt çizgi
  S.koy(S.darbe([[kel(6).x - 4, kel(6).y + 20], [(kel(6).x + kel(7).x + kel(7).w) / 2, kel(6).y + 17],
    [kel(7).x + kel(7).w + 4, kel(6).y + 21]], { w: 7.5, renk: SARI, alfa: 0.85, uc0: 12, uc1: 26 }, 37.04, 0.5, 0.55));

  // 35,84–37,95 have been reading: sarı daire + kalem oku -> Caveat `process`
  cevre(1, 3, 35.84, -0.03, 11);
  {
    const A = kel(1), B = kel(3), mx = (A.x + B.x + B.w) / 2;
    S.koy(S.darbeler(ok([mx + 90, 262], [mx + 18, 296], 3), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 36.5, 0.16, 0.12, 0.5));
    // 36,80–37,25 `process` (anlatımsız etiket, sure 0,45 sn)
    S.koy(S.elYazisi({ metin: "process", x: mx + 100, y: 262, boy: 52, renk: SARI, tb: 36.8,
      sure: 0.45, ses: 0.5 }));
  }

  // 35,5–39,5 sağ sahne: okuyan figür (sitting-1) + roman (440 px)
  S.koy(S.cizim({ svg: okur, ad: "figur", kutu: { x: 1130, y: 190, w: 310, h: 410 }, esik: 0.004, enCok: 60, w: 3.2, tb: 35.6, sure: 1.7, olayEnCok: 6 }));
  S.koy(S.cizim({ svg: roman, ad: "roman", kutu: { x: 1450, y: 170, w: 410, h: 430 }, enCok: 25, w: 4, tb: 36.9, sure: 1.0, olayEnCok: 4 }));
  S.koy(S.parilti(1800, 200, 38.2, 22));

  // 38,56–40,24 have only finished two chapters: ikinci daire (tik) -> Caveat `result`
  cevre(10, 14, 38.56, -0.02, 13);
  S.koy(S.darbeler(ok([700, 572], [700, 534], 3), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 39.3, 0.16, 0.12, 0.5));
  // 39,55–40,00 `result` (anlatımsız etiket, sure 0,45 sn; "chapters." 39,20–40,24)
  S.koy(S.elYazisi({ metin: "result", x: 640, y: 618, boy: 52, renk: SARI, tb: 39.55, sure: 0.45,
    ses: 0.5 }));

  // 40,41–44,57 Türkçe çeviri (Caveat 48 ikincil)
  // el yazısı, her sözcük kendi penceresinde (Bütün 40,41 … bitirdim. 43,29–44,57); 0,2 sn'den kısa
  // pencereler (ama 0,16 · iki 0,08) sonraki sözcüğün başına dek uzatıldı
  const trSoz = S.dizi("Bütün", 40.41, 9);
  S.koy(S.elYazisi({ metin: "Bütün hafta okuyorum, ama yalnızca iki bölümü bitirdim.", x: 140,
    y: 690, renk: IKINCIL, sozcukler: trSoz.map((w, i) => ({ t0: w.t0,
      t1: w.t1 - w.t0 < 0.2 && trSoz[i + 1] ? trSoz[i + 1].t0 : w.t1 })) }));

  // 44,72–49,20 iki sütunlu el kartı: PROCESS been reading · RESULT have finished + sayı
  {
    const F = "700 60px Fredoka", E = "500 30px Lexend";
    S.koy(S.darbeler(kutu(140, 740, 760, 250, 41), { w: 4.2, renk: KREM, uc0: 8, uc1: 14 }, 44.72, 0.1, 0.08, 0.5));
    S.koy(S.metinPop({ parca: [["PROCESS", SARI]], x: 190, y: 800, font: E, tb: 44.95, sure: 0.3, ses: 0.5 }));
    S.koy(S.metinPop({ parca: [["been reading", KREM]], x: 190, y: 905, font: F, tb: 45.6, sure: 0.35, ses: 0.6 }));
    S.koy(S.darbeler(kutu(960, 740, 800, 250, 42), { w: 4.2, renk: KREM, uc0: 8, uc1: 14 }, 46.96, 0.1, 0.08, 0.5));
    S.koy(S.metinPop({ parca: [["RESULT", SARI]], x: 1010, y: 800, font: E, tb: 47.2, sure: 0.3, ses: 0.5 }));
    // 47,52–48,04 `+ sayı (two)` ("sayı," 47,52–48,04; sure 0,52 sn)
    S.koy(S.elYazisi({ metin: "+ sayı (two)", x: 1010, y: 862, boy: 48, renk: SARI, tb: 47.52,
      sure: 0.52, ses: 0.4 }));
    S.koy(S.metinPop({ parca: [["have finished", KREM]], x: 1010, y: 950, font: F, tb: 48.24, sure: 0.35, ses: 0.6 }));
    S.koy(S.parilti(1700, 770, 48.9, 22));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

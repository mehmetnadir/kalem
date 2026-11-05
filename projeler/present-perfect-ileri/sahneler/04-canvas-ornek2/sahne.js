// SAHNE 04 (İLERİ) — Kök 2 (düz canvas, 533 kare, t_bas 33,89; cümle 4). Kendini çizen kalem; zaman yalnız kare numarasından.
// Kök: "Selim has worked at this bank for thirty years, so he knows every customer." (for + süre).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu } from "./sahne-ortak.js";
import { yaziDarbeleri } from "/projeler/present-perfect-ileri/ortak/kalem-canvas.js";

const KARE = 533, TBAS = 33.89, ICERIK = 521;
const KOKDIZ = "/projeler/present-perfect-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Exam Q 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

// El yazısı genişliği (px): orta hizalı etiketlerin x'ini bulmak için saf geometri (çizim yok).
const gen = (metin, boy) => yaziDarbeleri(metin, S.EY.G, { upm: S.EY.M.unitsPerEm,
  asc: S.EY.M.ascender, boy, x: 0, taban: 0 }).gen;

async function kur() {
  await S.kur();
  const [kiz, laptop] = await Promise.all([svgOku("open-peeps/sitting-5.svg"), svgOku("coco/laptop.svg")]);

  // 34,44–35,30 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 200, 190, 34.44));

  // 35,57–39,90 İngilizce kök (Fredoka 56, sözcük zamanlı, sarı alt çizgi kayar); satırlar 5 / 4 / 5 sözcük
  const F56 = "700 56px Fredoka";
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Selim", 35.57, 14), x: 140, y: 300, maxGen: 1000, font: F56, satirH: 76,
    satirSay: [5, 4, 5], bosluk: 4 }));
  const kel = (i) => cum.kel[i];             // satır 1: 0 Selim 1 has 2 worked 3 at 4 this | 2: 5 bank 6 for 7 thirty 8 years, | 3: 9 so … 13 customer.
  const cevre = (a, b, tb, egim, tohum) => {                       // iki sözcüğe tek sarı daire
    const A = kel(a), B = kel(b);
    S.koy(S.darbe(elips((A.x + B.x + B.w) / 2, A.y - 20, (B.x + B.w - A.x) / 2 + 3, 38, egim, tohum),
      { w: 6, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, tb, 0.4, 0.55));
  };
  cevre(6, 8, 37.13, -0.03, 11);                                   // for thirty years (37,13–37,73)

  // 36,0–39,0 sağ sahne: oturan figür (sitting-5) + dizüstü (360 px)
  S.koy(S.cizim({ svg: kiz, ad: "figur", kutu: { x: 1110, y: 210, w: 330, h: 430 }, esik: 0.004, enCok: 60, w: 3.2, tb: 36.0, sure: 1.7, olayEnCok: 6 }));
  S.koy(S.cizim({ svg: laptop, ad: "dizustu", kutu: { x: 1450, y: 300, w: 390, h: 340 }, enCok: 25, w: 4, tb: 37.8, sure: 1.0, olayEnCok: 4 }));
  S.koy(S.parilti(1760, 270, 39.0, 22));

  // 40,70–45,74 Türkçe çeviri (Caveat 48 ikincil, 2 satır; el yazısı, sözcük penceresi:
  // satır 1 Selim 40,70 … çalışıyor, –43,18 · satır 2 bu 43,22 … tanıyor. –45,74)
  S.koy(S.elYazisi({ metin: "Selim bu bankada otuz yıldır çalışıyor,", x: 140, y: 560, boy: 48,
    renk: IKINCIL, sozcukler: S.dizi("Selim", 40.70, 6).map((w) => ({ t0: w.t0, t1: w.t1 })) }));
  S.koy(S.elYazisi({ metin: "bu yüzden her müşteriyi tanıyor.", x: 140, y: 620, boy: 48,
    renk: IKINCIL, sozcukler: S.dizi("bu", 43.22, 5).map((w) => ({ t0: w.t0, t1: w.t1 })) }));

  // takvim şeridi (sağ alt): 12 işaret, sarı köşeli ayraç `30 years`, sağ uçta `now` (nabız)
  {
    const x0 = 1040, x1 = 1800, y = 800;
    S.koy(S.darbe([[x0 - 6, y + 2], [(x0 + x1) / 2, y - 2], [x1 + 6, y + 1]], { w: 4.4, renk: IKINCIL, uc0: 10, uc1: 20 }, 41.0, 0.8, 0.5));
    for (let i = 0; i <= 12; i++) {
      const x = x0 + (x1 - x0) * i / 12, t = 41.7 + i * 0.05;
      S.koy(S.darbe([[x, y - 12 + (i % 2)], [x + 1, y + 12]], { duz: true, w: 3.6, renk: IKINCIL, uc0: 4, uc1: 6 }, t, 0.12, i === 0 ? 0.4 : false));
    }
    S.koy(S.darbe([[x0 - 4, y - 36], [x0 - 4, y - 52], [x1 + 4, y - 52], [x1 + 4, y - 36]],
      { duz: true, w: 7, renk: SARI, alfa: 0.85, uc0: 12, uc1: 24 }, 42.3, 0.7, 0.6));
    // 42,90–43,40 `30 years` (taban y−80: ayraçla ≥ 10 px pay) ve 43,50–43,95 `1995`:
    // el yazısı etiket (anlatımsız; sure 0,5 / 0,45 sn)
    S.koy(S.elYazisi({ metin: "30 years", x: (x0 + x1) / 2 - gen("30 years", 52) / 2,
      y: y - 80, boy: 52,
      renk: SARI, tb: 42.9, sure: 0.5, ses: 0.5 }));
    S.koy(S.elYazisi({ metin: "1995", x: x0 - gen("1995", 40) / 2, y: y + 58, boy: 40,
      renk: IKINCIL,
      tb: 43.5, sure: 0.45, ses: false }));
    S.koy(S.nabiz(x1, y, 11, 44.2));
    S.koy(S.metinPop({ parca: [["now", IKINCIL]], x: x1, y: y + 58, font: "500 28px Lexend", hiza: "orta", tb: 44.2, sure: 0.3, ses: 0.4 }));
  }

  // 45,89–51,25 iki kutu: for + süre (47,17) / since + başlangıç (50,29); has worked daire; ok `since 1995`
  cevre(1, 2, 46.3, -0.025, 17);                                   // has worked
  {
    const F = "700 56px Fredoka";
    S.koy(S.darbeler(kutu(140, 700, 560, 120, 51), { w: 4.2, renk: KREM, uc0: 8, uc1: 14 }, 46.75, 0.1, 0.08, 0.5));
    S.koy(S.metinPop({ parca: [["for", SARI], ["  +  ", IKINCIL], ["süre", KREM]], x: 180, y: 782, font: F, tb: 47.17, sure: 0.35, ses: 0.6 }));
    S.koy(S.darbeler(kutu(140, 860, 660, 120, 52), { w: 4.2, renk: KREM, uc0: 8, uc1: 14 }, 49.9, 0.1, 0.08, 0.5));
    S.koy(S.metinPop({ parca: [["since", SARI], ["  +  ", IKINCIL], ["başlangıç", KREM]], x: 180, y: 942, font: F, tb: 50.29, sure: 0.35, ses: 0.6 }));
    S.koy(S.darbeler(ok([830, 920], [940, 920], 3), { w: 6, renk: IKINCIL, uc0: 10, uc1: 14 }, 50.7, 0.16, 0.12, 0.5));
    // 50,55–51,15 `since 1995` (el yazısı; "gelirdi." 50,61–51,33 bitmeden yazılır, sure 0,6 sn)
    S.koy(S.elYazisi({ metin: "since 1995", x: 970, y: 934, boy: 48, renk: IKINCIL, tb: 50.55,
      sure: 0.6, ses: 0.4 }));
    S.koy(S.parilti(760, 860, 50.3, 22));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

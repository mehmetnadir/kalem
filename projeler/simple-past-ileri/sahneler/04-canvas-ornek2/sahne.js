// SAHNE 04 (SIMPLE PAST İLERİ) — Örnek 2, kök 2 (düz canvas, 487 kare, t_bas 33,15; cümle 4). Zaman yalnız kare numarasından.
// Kök: "We used to live in a village, and we would walk to school every morning." (used to durum + alışkanlık, would yalnız alışkanlık).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, yavasla, kis } from "./sahne-ortak.js";

const KARE = 487, TBAS = 33.15, ICERIK = 475;
const KOKDIZ = "/projeler/simple-past-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIR = RT.kirmizi;

async function kur() {
  await S.kur();
  const [ev, okul, takvim, yuruyen] = await Promise.all([svgOku("tabler/home.svg"), svgOku("tabler/school.svg"),
    svgOku("tabler/calendar.svg"), svgOku("open-peeps/standing-4.svg")]);

  // 33,55: daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 200, 190, 33.55));

  // 34,36–37,80 İngilizce kök (Fredoka 56, sözcük zamanlı, 3 satır: 5 / 6 / 4 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("We", 34.36, 15), x: 140, y: 310, maxGen: 1000, font: "700 56px Fredoka",
    satirH: 78, satirSay: [5, 6, 4], bosluk: 4 }));
  const kel = (i) => cum.kel[i];             // satır 1: 0 We … 4 in | satır 2: 5 a … 10 walk | satır 3: 11 to … 14 morning.
  const sariKutu = (a, b, tb, tohum, egim) => {
    const A = kel(a), B = kel(b), x = A.x - 10, w = B.x + B.w - A.x + 20;
    S.koy(S.darbeler(kutu(x, A.y - 48, w, 68, tohum), { w: 5, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14 }, tb, 0.12, 0.09, 0.5));
  };
  sariKutu(1, 2, 34.52, 21);                 // used to
  sariKutu(9, 9, 36.12, 37);                 // would

  // 34,5–37,8 sağ üst sahne: ev ile okul arasında yol; figür yolda yürür
  S.koy(S.cizim({ svg: ev, ad: "ev", kutu: { x: 1190, y: 190, w: 300, h: 300 }, enCok: 6, w: 4, tb: 34.5, sure: 0.8, olayEnCok: 4 }));
  S.koy(S.cizim({ svg: okul, ad: "okul", kutu: { x: 1540, y: 190, w: 300, h: 300 }, enCok: 8, w: 4, tb: 34.95, sure: 0.8, olayEnCok: 4 }));
  S.koy(S.darbe([[1215, 560], [1360, 548], [1520, 566], [1700, 552], [1820, 560]], { w: 5, renk: IKINCIL, alfa: 0.9, uc0: 12, uc1: 18 }, 35.4, 0.8, 0.5));
  S.koy(S.darbe([[1235, 612], [1380, 600], [1530, 618], [1710, 604], [1800, 610]], { w: 5, renk: IKINCIL, alfa: 0.9, uc0: 12, uc1: 18 }, 35.7, 0.8, false));
  const yur = S.cizim({ svg: yuruyen, ad: "yuruyen", kutu: { x: 1250, y: 320, w: 160, h: 270 }, esik: 0.004, enCok: 60, w: 3.4, tb: 35.9, sure: 1.1,
    olayEnCok: 6, nefes: false });
  {
    const f0 = S.fr(36.4), f1 = S.fr(37.8), cx = 1330, cy = 590;
    yur.donusum = (f) => { const u = kis((Math.min(f, ICERIK) - f0) / (f1 - f0)), g = Math.min(f, ICERIK) - f0;
      return { cx, cy, tx: 190 * yavasla(u), ty: g < 0 || u >= 1 ? 0 : -7 * Math.abs(Math.sin(g / 5)), dondur: 0, olcek: 1 }; };
  }
  S.koy(yur);

  // 39,01–41,73 used to = durum + alışkanlık; ok -> takvim, üstü çizili: artık yok
  const F72 = "700 72px Fredoka", C64 = "700 64px Caveat";
  S.koy(S.metinPop({ parca: [["used to", KREM]], x: 140, y: 695, font: F72, tb: 39.01, sure: 0.35, ses: 0.5 }));
  S.koy(S.darbeler(ok([420, 672], [560, 640], 3), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 39.6, 0.16, 0.12, 0.5));
  S.koy(S.not({ parca: [["durum", SARI]], x: 580, y: 655, font: C64, tb: 39.81, sure: 0.4, ses: 0.4 }));
  S.koy(S.darbeler(ok([420, 705], [560, 745], 5), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 40.7, 0.16, 0.12, 0.5));
  S.koy(S.not({ parca: [["alışkanlık", SARI]], x: 580, y: 760, font: C64, tb: 40.93, sure: 0.5, ses: 0.4 }));
  S.koy(S.darbeler(ok([870, 742], [1000, 742], 7), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 41.2, 0.16, 0.12, 0.5));
  S.koy(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 1030, y: 650, w: 150, h: 150 }, enCok: 8, w: 4, tb: 41.3, sure: 0.4, olayEnCok: 3, nefes: false }));
  S.koy(S.darbe([[1015, 815], [1100, 730], [1195, 640]], { duz: true, w: 8, renk: KREM, alfa: 0.9, uc0: 6, uc1: 10 }, 41.5, 0.2, 0.6));
  S.koy(S.not({ parca: [["artık yok", IKINCIL]], x: 1215, y: 760, font: C64, tb: 41.6, sure: 0.3, ses: 0.4 }));

  // 42,44–47,72 would yalnız tekrarlanan eylem: would + walk ✓ (45,44–46,04), would + live ✗ (46,92–47,72)
  S.koy(S.metinPop({ parca: [["would", SARI]], x: 140, y: 855, font: F72, tb: 42.44, sure: 0.35, ses: 0.5 }));
  S.koy(S.not({ parca: [["= tekrarlanan eylem", KREM]], x: 360, y: 855, font: C64, tb: 43.64, sure: 1.2, ses: 0.4 }));
  const F60 = "700 60px Fredoka";
  S.koy(S.darbeler(kutu(140, 895, 450, 84, 41), { w: 4, renk: KREM, uc0: 8, uc1: 14 }, 45.44, 0.12, 0.09, 0.45));
  S.koy(S.metinPop({ parca: [["would + walk", KREM]], x: 165, y: 953, font: F60, tb: 45.5, sure: 0.3, ses: 0.5 }));
  S.koy(S.darbe([[615, 940], [632, 962], [668, 905]], { w: 9, renk: SARI, alfa: 0.95, uc0: 5, uc1: 8 }, 46.04, 0.2, 0.6));
  S.koy(S.darbeler(kutu(700, 895, 450, 84, 43), { w: 4, renk: KREM, uc0: 8, uc1: 14 }, 46.92, 0.12, 0.09, 0.45));
  S.koy(S.metinPop({ parca: [["would + live", KREM]], x: 725, y: 953, font: F60, tb: 46.98, sure: 0.3, ses: 0.5 }));
  S.koy(S.darbe([[1180, 905], [1222, 962]], { duz: true, w: 9, renk: KIR, alfa: 0.95, uc0: 5, uc1: 8 }, 47.2, 0.14, 0.7));
  S.koy(S.darbe([[1222, 905], [1180, 962]], { duz: true, w: 9, renk: KIR, alfa: 0.95, uc0: 5, uc1: 8 }, 47.34, 0.14, false));
  S.koy(S.not({ parca: [["durum fiili", KREM]], x: 1255, y: 953, font: "700 56px Caveat", tb: 47.45, sure: 0.3, ses: 0.4 }));
  S.koy(S.darbeler(ok([1450, 935], [1520, 935], 9), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 47.55, 0.12, 0.1, false));
  S.koy(S.not({ parca: [["used to", SARI]], x: 1545, y: 953, font: "700 56px Caveat", tb: 47.7, sure: 0.3, ses: 0.4 }));
  S.koy(S.parilti(1780, 900, 47.9, 24));
}

surucu(kur, (f) => S.kare(f), KARE);

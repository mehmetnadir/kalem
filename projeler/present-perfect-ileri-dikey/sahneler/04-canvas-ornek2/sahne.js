// SAHNE 04 (İLERİ, DİKEY 1080x1920) — Kök 2 (düz canvas, 533 kare, t_bas 33,89; cümle 4). Zaman yalnız kare numarasından.
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (sahne-ortak.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–708) · TR 3 satır (740–920) · sahne 930–1360 (40,4'te 0,6'ya sola toplanır) · takvim şeridi 1170–1392 ·
// 46,4'te ikisi 0,48'e toplanır · formül kartı (1170–1392).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, yavasla } from "./sahne-ortak.js";

const KARE = 533, TBAS = 33.89, ICERIK = 521;
const KOKDIZ = "/projeler/present-perfect-ileri-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Exam Q 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

async function kur() {
  await S.kur();
  const [kiz, laptop] = await Promise.all([svgOku("open-peeps/sitting-5.svg"), svgOku("coco/laptop.svg")]);

  // 34,44: kart çerçevesi (el kutusu, 4 px) + sağ üst köşede daire içinde 2. İlk 12 kare boş: künye hazır, tuval boş.
  S.koy(S.darbeler(kutu(48, 372, 984, 336, 4), { w: 4.2, renk: IKINCIL, uc0: 10, uc1: 18 }, 34.44, 0.2, 0.14, 0.55));
  {
    const d = S.darbe(elips(962, 442, 46, 44, 0.1, 5), { w: 5, uc0: 18, uc1: 34 }, 34.7, 0.55, 0.6);
    S.koy(d);
    S.koy(S.metinPop({ parca: [["2", KREM]], x: 962, y: 474, font: "700 78px Fredoka", hiza: "orta", tb: 35.0, sure: 0.35, olcek0: 0.7, ses: 0.8, turu: "vurus" }));
  }

  // 35,57–39,90 İngilizce kök (Fredoka 64, sözcük zamanlı, 4 satır: 4 / 4 / 4 / 2 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Selim", 35.57, 14), x: 88, y: 452, maxGen: 904, font: "700 64px Fredoka",
    satirH: 78, satirSay: [4, 4, 4, 2], bosluk: 4 }));
  const kel = (i) => cum.kel[i];   // 1: Selim has worked at | 2: this bank for thirty | 3: years, so he knows | 4: every customer.
  const tek = (x0, x1, y, t, th, egim = -0.03) => S.darbe(elips((x0 + x1) / 2, y - 22, (x1 - x0) / 2 + 8, 39, egim, th),
    { w: 9, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, t, 0.4, 0.55);
  const cevre = (a, b, tb, egim, tohum) => {                       // iki sözcüğe sarı daire; satır ayrıysa her birine
    const A = kel(a), B = kel(b);
    if (A.y === B.y) S.koy(tek(A.x, B.x + B.w, A.y, tb, tohum, egim));
    else { S.koy(tek(A.x, A.x + A.w, A.y, tb, tohum, egim)); S.koy(tek(B.x, B.x + B.w, B.y, tb + 0.15, tohum + 1, egim)); }
  };
  cevre(6, 7, 37.13, -0.03, 11);                                   // for thirty (satır 2)
  cevre(8, 8, 37.55, -0.03, 13);                                   // years, (satır 3)

  // 36,0–40,4 ORTA sahne (930–1360): oturan figür (sitting-5, 430 px) + dizüstü.
  const sahne = [];
  sahne.push(S.cizim({ svg: kiz, ad: "figur", kutu: { x: 70, y: 935, w: 340, h: 425 }, esik: 0.004, enCok: 60, w: 4.4, tb: 36.0, sure: 1.7, olayEnCok: 6 }));
  sahne.push(S.cizim({ svg: laptop, ad: "dizustu", kutu: { x: 440, y: 1000, w: 480, h: 360 }, enCok: 25, w: 4.4, tb: 37.8, sure: 1.0, olayEnCok: 4 }));
  const sahneG = S.grup(sahne, { f0: S.fr(40.4), f1: S.fr(41.1), ax: 70, ay: 930, olcek: 0.6, dy: 0 });
  S.koy(S.parilti(960, 1000, 39.0, 28));

  // 40,70–45,74 Türkçe çeviri (Caveat 64 mürekkep, 3 satır)
  [["Selim bu bankada otuz yıldır", 40.70, 772, 1.5], ["çalışıyor, bu yüzden", 42.34, 838, 1.0], ["her müşteriyi tanıyor.", 43.82, 904, 1.0]]
    .forEach(([m, tb, y, sure]) => S.koy(S.not({ parca: [[m, KREM]], x: 88, y, font: "700 64px Caveat", tb, sure })));

  // takvim şeridi (alt bant 1170–1392): işaretler, sarı köşeli ayraç `30 years`, sol uçta 1995, sağ uçta `now` (nabız).
  // Yazılar 96 px: 46,4'te sahne + takvim birlikte 0,48'e toplanınca 46 px kalır.
  const takvim = [];
  {
    const x0 = 100, x1 = 990, y = 1290;
    takvim.push(S.darbe([[x0 - 6, y + 2], [(x0 + x1) / 2, y - 2], [x1 + 6, y + 1]], { w: 5, renk: IKINCIL, uc0: 10, uc1: 20 }, 41.3, 0.7, 0.5));
    for (let i = 0; i <= 8; i++) {
      const x = x0 + (x1 - x0) * i / 8;
      takvim.push(S.darbe([[x, y - 14 + (i % 2)], [x + 1, y + 14]], { duz: true, w: 4, renk: IKINCIL, uc0: 4, uc1: 6 }, 41.9 + i * 0.05, 0.12, i === 0 ? 0.4 : false));
    }
    takvim.push(S.darbe([[x0 - 4, y - 40], [x0 - 4, y - 60], [x1 + 4, y - 60], [x1 + 4, y - 40]],
      { duz: true, w: 9, renk: SARI, alfa: 0.85, uc0: 12, uc1: 24 }, 42.4, 0.6, 0.6));
    takvim.push(S.metinPop({ parca: [["30 years", SARI]], x: 790, y: y - 78, font: "700 96px Caveat", hiza: "orta", tb: 43.0, sure: 0.35, ses: 0.5 }));
    takvim.push(S.metinPop({ parca: [["1995", KREM]], x: x0, y: 1382, font: "700 96px Caveat", tb: 43.5, sure: 0.3, ses: false }));
    takvim.push(S.nabiz(x1, y, 14, 44.2));
    takvim.push(S.metinPop({ parca: [["now", KREM]], x: 925, y: 1382, font: "700 96px Caveat", hiza: "orta", tb: 44.2, sure: 0.3, ses: 0.4 }));
  }
  S.koy(S.grup([sahneG, ...takvim], { f0: S.fr(46.4), f1: S.fr(47.1), ax: 540, ay: 930, olcek: 0.48, dy: 0 }));

  // 45,89–51,25 formül kartı: for + süre (47,17) / since + başlangıç (50,29); has worked daire (46,3)
  cevre(1, 2, 46.3, -0.025, 17);
  S.koy(S.darbeler(kutu(48, 1170, 984, 222, 51), { w: 4.2, renk: IKINCIL, uc0: 8, uc1: 14 }, 46.75, 0.1, 0.08, 0.5));
  S.koy(S.metinPop({ parca: [["for", SARI], [" + ", IKINCIL], ["süre", KREM]], x: 100, y: 1262, font: "700 96px Fredoka", tb: 47.17, sure: 0.35, ses: 0.6 }));
  S.koy(S.metinPop({ parca: [["since", SARI], [" + ", IKINCIL], ["başlangıç", KREM]], x: 100, y: 1362, font: "700 96px Fredoka", tb: 50.29, sure: 0.35, ses: 0.6 }));
  S.koy(S.parilti(960, 1215, 50.9, 28));
}

surucu(kur, (f) => S.kare(f), KARE);

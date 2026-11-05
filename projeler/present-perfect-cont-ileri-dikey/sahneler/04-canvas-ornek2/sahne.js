// SAHNE 04 (İLERİ, DİKEY 1080x1920) — Örnek 2 (düz canvas, 478 kare, t_bas 33,68; cümle 4). Zaman yalnız kare numarasından.
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (sahne-ortak.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–720, 4 satır) · iki sütun: solda figür 430 px (750–1180), sağda TR 3 satır (800–932) + roman (960–1190) ·
// süreç / sonuç kartı (1205–1392). Toplanma / küçültme YOK: figür baştan sona 430 px.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, kutu } from "./sahne-ortak.js";

const KARE = 478, TBAS = 33.68, ICERIK = 466;
const KOKDIZ = "/projeler/present-perfect-cont-ileri-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
// El yazısı (tegaki Caveat, dalga 5b-2 / K26): sözcük penceresi = anlatım t0/t1 (küresel sn)
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

async function kur() {
  await S.kur();
  const [okur, roman] = await Promise.all([svgOku("open-peeps/sitting-1.svg"), svgOku("tabler/book.svg")]);

  // 34,23: kart çerçevesi (el kutusu, 4 px) + sağ üst köşede daire içinde 2. İlk 12 kare boş: künye hazır, tuval boş.
  S.koy(S.darbeler(kutu(48, 372, 984, 348, 4), { w: 4.2, renk: IKINCIL, uc0: 10, uc1: 18 }, 34.23, 0.2, 0.14, 0.55));
  {
    const d = S.darbe(elips(990, 410, 30, 28, 0.1, 5), { w: 5, uc0: 18, uc1: 34 }, 34.5, 0.55, 0.6);
    S.koy(d);
    S.koy(S.metinPop({ parca: [["2", KREM]], x: 990, y: 432, font: "700 56px Fredoka", hiza: "orta", tb: 34.8, sure: 0.35, olcek0: 0.7, ses: 0.8, turu: "vurus" }));
  }

  // 35,52–40,24 İngilizce kök (Fredoka 64, sözcük zamanlı, 4 satır: 4 / 4 / 4 / 3 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("I", 35.52, 15), x: 88, y: 452, maxGen: 904, font: "700 64px Fredoka",
    satirH: 78, satirSay: [4, 4, 4, 3], bosluk: 4 }));
  const kel = (i) => cum.kel[i];   // 1: I have been reading | 2: this novel all week, | 3: but I have only | 4: finished two chapters.
  const tek = (x0, x1, y, t, th, egim = -0.03) => S.darbe(elips((x0 + x1) / 2, y - 24, (x1 - x0) / 2 + 8, 42, egim, th),
    { w: 9, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, t, 0.4, 0.55);
  const cevre = (a, b, tb, egim, tohum) => {                       // iki sözcüğe sarı daire; satır ayrıysa her birine
    const A = kel(a), B = kel(b);
    if (A.y === B.y) S.koy(tek(A.x, B.x + B.w, A.y, tb, tohum, egim));
    else { S.koy(tek(A.x, A.x + A.w, A.y, tb, tohum, egim)); S.koy(tek(B.x, B.x + B.w, B.y, tb + 0.15, tohum + 1, egim)); }
  };
  cevre(1, 3, 35.84, -0.03, 11);                                   // have been reading (35,84)
  // all week (37,04–37,60): sarı alt çizgi
  S.koy(S.darbe([[kel(6).x - 4, kel(6).y + 26], [(kel(6).x + kel(7).x + kel(7).w) / 2, kel(6).y + 22],
    [kel(7).x + kel(7).w + 4, kel(6).y + 27]], { w: 9, renk: SARI, alfa: 0.85, uc0: 12, uc1: 26 }, 37.04, 0.5, 0.55));
  cevre(10, 11, 38.19, -0.02, 13);                                 // have only (38,19)
  cevre(12, 14, 38.56, -0.02, 15);                                 // finished two chapters (38,56)

  // 35,5–39,5 sol sütun: okuyan figür (sitting-1, 430 px); sağ sütun altı: roman
  S.koy(S.cizim({ svg: okur, ad: "figur", kutu: { x: 48, y: 750, w: 330, h: 430 }, esik: 0.004, enCok: 60, w: 4.4, tb: 35.6, sure: 1.7, olayEnCok: 6 }));
  S.koy(S.cizim({ svg: roman, ad: "roman", kutu: { x: 470, y: 960, w: 400, h: 230 }, enCok: 25, w: 4.2, tb: 36.9, sure: 1.0, olayEnCok: 4 }));
  S.koy(S.parilti(900, 990, 38.2, 28));

  // 40,41–44,57 Türkçe çeviri (el yazısı Caveat 64, 3 satır, sağ sütun x 430; sağ uç 939)
  // satır 1: Bütün 40,41–40,65 · hafta 40,73–41,01 · okuyorum, 41,05–41,77
  // satır 2: ama 41,93–42,17 (pencere 0,16 sn → sonrakinin başına uzatıldı) ·
  //   yalnızca 42,17–42,73 ·
  //   iki 42,81–42,97 (0,08 sn → uzatıldı) · satır 3: bölümü 42,97–43,21 · bitirdim. 43,29–44,57
  const s2 = pen("ama", 41.93, 3);
  s2[0].t1 = s2[1].t0; s2[2].t1 = 42.97;
  [["Bütün hafta okuyorum,", 800, pen("Bütün", 40.41, 3)], ["ama yalnızca iki", 866, s2],
    ["bölümü bitirdim.", 932, pen("bölümü", 42.97, 2)]].forEach(([m, y, sozcukler]) =>
    S.koy(S.elYazisi({ metin: m, x: 430, y, boy: 64, renk: KREM, sozcukler })));

  // 44,72–49,20 süreç / sonuç kartı (Fredoka 72): PROCESS been reading (45,6) · RESULT have finished + sayı (48,24)
  S.koy(S.darbeler(kutu(48, 1205, 984, 187, 51), { w: 4.2, renk: IKINCIL, uc0: 8, uc1: 14 }, 44.72, 0.1, 0.08, 0.5));
  S.koy(S.metinPop({ parca: [["PROCESS", SARI]], x: 80, y: 1272, font: "700 36px Lexend", tb: 44.95, sure: 0.3, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["been reading", KREM]], x: 300, y: 1280, font: "700 72px Fredoka", tb: 45.6, sure: 0.35, ses: 0.6 }));
  S.koy(S.metinPop({ parca: [["RESULT", SARI]], x: 80, y: 1362, font: "700 36px Lexend", tb: 46.96, sure: 0.3, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["have finished", KREM]], x: 300, y: 1370, font: "700 72px Fredoka", tb: 48.24, sure: 0.35, ses: 0.6 }));
  // 47,52 «sayı,» anında etiket `+ sayı`: hedef 0,5 sn → 48,02 (sağ uç 972)
  S.koy(S.elYazisi({ metin: "+ sayı", x: 840, y: 1370, boy: 64, renk: SARI, tb: 47.52,
    sure: 0.5 }));
  S.koy(S.parilti(970, 1245, 48.9, 28));
}

surucu(kur, (f) => S.kare(f), KARE);

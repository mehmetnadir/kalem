// SAHNE 04 — Örnek 2/3 (düz canvas, 762 kare, t_bas 43,85; cümle 4). 02-04 YDT temel.
// Kendini çizen kalem; zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json.
// Sol kart: "I live in İstanbul with my family." (ev, PERMANENT)
// Sağ kart: "My parents are out of town, so I am living with my uncle." (bavul, TEMPORARY)
// Altta iki zaman çizgisi: solda uzun bant (hep), sağda kısa bant (şimdilik) + now noktaları.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 762, TBAS = 43.85, ICERIK = 750;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const KOKDIZ = "/projeler/02-04-ydt-temel/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();

const u = (n) => (n * S.cv.width) / 1920;
const FF = (b) => `700 ${u(b)}px Fredoka`;
const FL = (b) => `500 ${u(b)}px Lexend`;
const t = (i) => S.sozc[i].t0;

const BAVUL_SVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" ` +
  `stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">` +
  `<path d="M6 8a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v11a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2z"/>` +
  `<path d="M10 6v-3h4v3"/>` +
  `<path d="M10 9v9"/>` +
  `<path d="M14 9v9"/>` +
  `<path d="M8.5 21v1.8"/>` +
  `<path d="M15.5 21v1.8"/>` +
  `</svg>`;

async function kur() {
  await S.kur();
  if (S.sozc.length !== 49) {
    throw new Error(`Beklenen 49 sözcük, gelen ${S.sozc.length}`);
  }
  const evSvg = await svgOku("tabler/home.svg");

  // 44,40 İkinci: daire içinde 2
  S.koy(S.daireSayi(2, u(196), u(176), t(0)));

  // 45,76 Kancadaki: sol kart çerçevesi
  S.koy(S.kart({
    x: u(110), y: u(250), w: u(820), h: u(410), tb: t(2), tohum: 4, kutuSure: 0.2,
    kutuAralik: 0.2, satirlar: [],
  }));

  // 47,20 live.: "live" başlık pop
  S.koy(S.metinPop({
    parca: [["live", RT.murekkep]], x: u(290), y: u(202), font: FF(72), tb: t(4),
    sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik",
  }));

  // 47,55 live.: "live" altında sarı altçizgi
  const wLive = olc(FF(72), "live");
  S.koy(S.darbe(altCizgi(u(290) - u(4), u(290) + wLive + u(4), u(220), 4),
    { w: u(8), renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 401 }, t(4) + 0.35, 0.35, 0.55));

  // 48,09 sol cümle: I live in İstanbul with my family.
  const solSozc = S.sozc.slice(5, 12).map((w) => (w.sozcuk === "Istanbul" ? { ...w, sozcuk: "İstanbul" } : w));
  const cumSol = S.cumleYaz({
    sozcukler: solSozc, x: u(150), y: u(334), maxGen: u(740), font: FF(56), satirH: u(86),
    satirSay: [4, 3], bosluk: u(4),
  });
  S.koy(cumSol);

  // 50,82 Ailemle: ev
  S.koy(S.cizim({
    svg: evSvg, ad: "ev", kutu: { x: u(710), y: u(440), w: u(180), h: u(180) },
    enCok: 10, w: u(4), sure: 1.0, olayEnCok: 4, tb: t(12),
  }));

  // Sol zaman ekseni ve bant (S.koy sırası: bant → eksen → now noktası → "now" etiketi)
  // 53,30 hep: uzun bant
  S.koy(S.darbe([[u(170), u(800)], [u(860), u(800)]],
    { duz: true, w: u(30), renk: RT.vurguDolgu, alfa: 0.8, uc0: 4, uc1: 8, tohum: 101 }, t(16), 1.0, 0.5));

  // 52,90 Orada: sol eksen
  {
    const [, uc1, uc2] = ok([u(140), u(800)], [u(910), u(800)], 21);
    S.koy(S.darbeler([[[u(140), u(800)], [u(910), u(800)]], uc1, uc2],
      { duz: true, w: u(4), renk: RT.ikincil, uc0: 6, uc1: 12 }, t(15), 0.4, 0.15, 0.4));
  }

  // 53,15 Orada: sol now noktası + etiket
  S.koy(S.darbe(elips(u(520), u(800), u(15), u(15), 0, 31),
    { w: u(6), renk: RT.murekkep, tohum: 71 }, t(15) + 0.25, 0.35, 0.45));
  S.koy(S.metinPop({
    parca: [["now", RT.ikincil]], x: u(520), y: u(858), font: FL(30), hiza: "orta",
    tb: t(15) + 0.40, sure: 0.3, ses: false,
  }));

  // 54,58 Kalıcı: PERMANENT
  S.koy(S.elYazisi({
    metin: "PERMANENT", x: u(150), y: u(604), boy: u(64), renk: RT.murekkep,
    sozcukler: [{ t0: t(18), t1: t(20) }],
  }));

  // 55,54 geniş: odak live
  {
    const A = cumSol.kel[1];
    S.koy(S.darbe(altCizgi(A.x - u(4), A.x + A.w + u(4), A.y + u(56 * 0.48), 11),   // kuyruğa değmez
      { w: u(8), renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 }, t(20), 0.4, 0.55));
  }

  // 56,64 My: sağ kart çerçevesi
  S.koy(S.kart({
    x: u(990), y: u(250), w: u(820), h: u(410), tb: t(22) - 0.35, tohum: 6, kutuSure: 0.14,
    kutuAralik: 0.08, satirlar: [],
  }));

  // 56,99 sağ cümle: My parents are out of town, so I am living with my uncle.
  const sagSozc = S.sozc.slice(22, 35);
  const cumSag = S.cumleYaz({
    sozcukler: sagSozc, x: u(1030), y: u(334), maxGen: u(740), font: FF(56), satirH: u(86),
    satirSay: [6, 7], bosluk: u(4),
  });
  S.koy(cumSag);

  // 62,28 dışında,: bavul
  S.koy(S.cizim({
    svg: BAVUL_SVG, ad: "bavul", kutu: { x: u(1590), y: u(440), w: u(180), h: u(180) },
    enCok: 10, esik: 0.01, w: u(4), sure: 1.0, olayEnCok: 4, tb: t(37),
  }));

  // Sağ zaman ekseni ve bant (S.koy sırası: bant → eksen → now noktası → "now" etiketi)
  // 65,60 şimdilik.: kısa bant
  S.koy(S.darbe([[u(1320), u(800)], [u(1480), u(800)]],
    { duz: true, w: u(30), renk: RT.vurguDolgu, alfa: 0.8, uc0: 4, uc1: 8, tohum: 102 }, t(44), 0.4, 0.5));

  // 66,00 şimdilik.: kısa bant uç çizgileri
  S.koy(S.darbe([[u(1320), u(774)], [u(1320), u(826)]],
    { duz: true, w: u(6), renk: RT.vurgu, uc0: 3, uc1: 3, tohum: 103 }, t(44) + 0.4, 0.18, 0.4));
  S.koy(S.darbe([[u(1480), u(774)], [u(1480), u(826)]],
    { duz: true, w: u(6), renk: RT.vurgu, uc0: 3, uc1: 3, tohum: 104 }, t(44) + 0.52, 0.18, 0.4));

  // 65,00 Bu: sağ eksen
  {
    const [, uc1, uc2] = ok([u(1020), u(800)], [u(1790), u(800)], 22);
    S.koy(S.darbeler([[[u(1020), u(800)], [u(1790), u(800)]], uc1, uc2],
      { duz: true, w: u(4), renk: RT.ikincil, uc0: 6, uc1: 12 }, t(42), 0.4, 0.15, 0.4));
  }

  // 65,25 Bu: sağ now noktası + etiket
  S.koy(S.darbe(elips(u(1400), u(800), u(15), u(15), 0, 32),
    { w: u(6), renk: RT.murekkep, tohum: 81 }, t(42) + 0.25, 0.35, 0.45));
  S.koy(S.metinPop({
    parca: [["now", RT.ikincil]], x: u(1400), y: u(858), font: FL(30), hiza: "orta",
    tb: t(42) + 0.40, sure: 0.3, ses: false,
  }));

  // 66,84 Geçici: TEMPORARY
  S.koy(S.elYazisi({
    metin: "TEMPORARY", x: u(1030), y: u(604), boy: u(64), renk: RT.murekkep,
    sozcukler: [{ t0: t(45), t1: t(47) }],
  }));

  // 67,88 şimdiki: odak am living
  {
    const A = cumSag.kel[8], B = cumSag.kel[9];
    S.koy(S.darbe(altCizgi(A.x - u(4), B.x + B.w + u(4), A.y + u(56 * 0.48), 12),   // kuyruğa değmez
      { w: u(8), renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 502 }, t(47), 0.4, 0.55));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

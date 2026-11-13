// SAHNE 11 — Tuzak fiilleri (düz canvas, 1150 kare, t_bas 188,50; cümle 14). Kendini çizen kalem;
// zaman yalnız kare numarasından.
// Sol: üç kart alt alta (We believe / We are believing ✗ · It has … · I … recommend …).
// Sağ köşe: liste — believe · think · have (own) → simple present · performative: promise · agree ·
// recommend → NO -ing. Kategori etiketi yalnız promise · agree · recommend için (believe/think yok).
import { surucu } from "/ortak/surucu.js";
import { KUNYE } from "/projeler/02-03-ydt-temel/ortak/kunye.js";
import { Sahne, RT, elips, kutu, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 1131, TBAS = 187.54, ICERIK = 1119;
const ETKIN = ((i) => (i >= 0 ? i : 3))(KUNYE.ajanda.findIndex((a) => /trap/i.test(a)));
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Trap verbs", cumle: 14,
  etkin: ETKIN });
const KOKDIZ = "/projeler/02-03-ydt-temel/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

// Düz ok (gövde + iki uç çizgisi)
function duzOk(x0, y0, x1, y1) {
  const dx = x1 - x0, dy = y1 - y0, L = Math.hypot(dx, dy), d = [dx / L, dy / L];
  const uc = (sg) => {
    const aci = 0.5 * sg, c = Math.cos(aci), s = Math.sin(aci), gx = -d[0], gy = -d[1];
    return [[x1 + (gx * c - gy * s) * 26, y1 + (gx * s + gy * c) * 26], [x1 + d[0] * 0.5, y1 + d[1] * 0.5]];
  };
  return [[[x0, y0], [(x0 + x1) / 2, (y0 + y1) / 2], [x1, y1]], uc(1), uc(-1)];
}

async function kur() {
  await S.kur();

  // ---- yerleşim: sol sütun x 100–1010 (üç kart), sağ sütun x 1090–1830 (liste + iki ikon) ----
  const XK = 100, KW = 910, PAD = 40, IC = KW - 2 * PAD;       // kart iç genişliği 830
  const K1 = { y: 150, h: 320 }, K2 = { y: 510, h: 210 }, K3 = { y: 755, h: 225 };
  const XS = 1090;                                              // liste sol kenarı

  // Cümleler (sözcük zamanları sozcukler.json, küresel sn)
  const a = S.dizi("We", 192.94, 2);          // We believe.
  const b = S.dizi("We", 195.6, 3);          // We are believing.
  const c = S.dizi("It", 208.66, 8);          // It has a great view of the sea.
  const d = S.dizi("I", 215.32, 9);            // I definitely recommend a holiday in this lovely city.
  const metin = (s) => s.map((k) => k.sozcuk).join(" ");
  const sigdir = (px0, genis, satirlar) => {                   // en geniş satırı iç genişliğe sığdır
    const en = Math.max(...satirlar.map((s) => olc(`700 ${px0}px Fredoka`, metin(s)) + (s.length - 1) * 4));
    return Math.min(px0, Math.floor((px0 * genis) / en));
  };
  const P1 = sigdir(76, IC, [a, b]);
  const P2 = sigdir(50, IC, [c]);
  const P3 = sigdir(46, IC, [d.slice(0, 4), d.slice(4)]);
  const F1 = `700 ${P1}px Fredoka`, F2 = `700 ${P2}px Fredoka`, F3 = `700 ${P3}px Fredoka`;
  const kartCiz = (k, tb, tohum, ad) => S.koy(S.kart({ x: XK, y: k.y, w: KW, h: k.h, tb, tohum,
    satirlar: [], ad, kutuSure: 0.12, kutuAralik: 0.08 }));
  const halka = (k, px, tb, tohum) => S.koy(S.darbe(altCizgi(k.x - 2, k.x + k.w + 2, k.y + 26, tohum), { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14 },
  tb, 0.4, 0.55));   // halka yerine el altçizgisi (13.11 QA)

  // 189,30 kart 1 çerçevesi (Olmaz.)
  kartCiz(K1, 188.34, 1, "kart-1");

  // ---- sağ liste (köşe): satır 1 believe · think · have (own); satır 2 → simple present ----
  const FL = Math.min(46, Math.floor((46 * (1830 - XS)) / (olc("700 46px Fredoka",
    "believe · think · have (own)") + 4)));
  const FLS = `700 ${FL}px Fredoka`, Y_L1 = 230, Y_L2 = 305, Y_P = 425, Y_V = 500, Y_N = 585;
  const wB = olc(FLS, "believe"), wBT = olc(FLS, "believe · think");
  const pop = (parca, x, y, tb, ses) => S.koy(S.metinPop({ parca, x, y, font: FLS, tb, sure: 0.3, ses }));
  pop([["believe", KREM]], XS, Y_L1, 189.41, 0.5);                       // 190,37 Believe
  pop([[" · ", IKINCIL], ["think", KREM]], XS + wB, Y_L1, 190.21, false);  // 191,17 think
  duzOk(XS, Y_L2 - 14, XS + 64, Y_L2 - 14).forEach((p, i) => S.koy(S.darbe(p, { duz: true, w: 6,
    renk: SARI, alfa: 0.9, uc0: 6, uc1: 10, tohum: 400 + i }, 191.41 + (i ? 0.2 : 0),
  i ? 0.12 : 0.22, i ? false : 0.5)));
  pop([["simple present", SARI]], XS + 90, Y_L2, 191.55, 0.45);           // 192,37 geniş zamanla
  // 212,83 Have: have (own) listeye eklenir
  const xH = XS + wBT;
  pop([[" · ", IKINCIL], ["have (own)", KREM]], xH, Y_L1, 211.31, 0.5);
  S.koy(S.parilti(xH + olc(FLS, " · have (own)") + 30, Y_L1 - 30, 213.55, 22));   // 215,07 -ing almaz

  // performative grubu: 199,85 promise · 200,85 agree · 201,45 recommend · 202,65 performative:
  const wP = olc(FLS, "promise"), wPA = olc(FLS, "promise · agree"), wDot = olc(FLS, " · ");
  pop([["promise", KREM]], XS, Y_V, 198.49, 0.5);
  pop([[" · ", IKINCIL], ["agree", KREM]], XS + wP, Y_V, 199.57, false);
  pop([[" · ", IKINCIL], ["recommend", KREM]], XS + wPA, Y_V, 200.25, false);
  S.koy(S.elYazisi({ metin: "performative:", x: XS, y: Y_P, boy: 60, renk: KREM,
    sozcukler: S.dizi("performative", 201.37, 1).map((w) => ({ t0: w.t0, t1: w.t1 })) }));
  // 206,57 → NO -ing
  duzOk(XS, Y_N - 16, XS + 64, Y_N - 16).forEach((p, i) => S.koy(S.darbe(p, { duz: true, w: 6,
    renk: SARI, alfa: 0.9, uc0: 6, uc1: 10, tohum: 410 + i }, 205.08 + (i ? 0.2 : 0),
  i ? 0.12 : 0.22, i ? false : 0.5)));
  S.koy(S.elYazisi({ metin: "NO -ing", x: XS + 90, y: Y_N, boy: 72, renk: SARI, tb: 205.59,
    sure: 0.55 }));

  // ---- kart 1: 193,82 We believe. · 195,35 ✓ · 196,88 We are believing. · 198,57 ing üstüne çarpı ----
  const Y_A = K1.y + 135, Y_B = K1.y + 250;
  const cA = S.koy(S.cumleYaz({ sozcukler: a, x: XK + PAD, y: Y_A, font: F1, satirH: 0, bosluk: 4,
    maxGen: IC + 400 }));
  const kA = cA.kel[cA.kel.length - 1];
  const tx = kA.x + kA.w + 46;
  S.koy(S.darbe([[tx, Y_A - 0.35 * P1], [tx + 0.3 * P1, Y_A - 0.05 * P1],
    [tx + 0.85 * P1, Y_A - 0.72 * P1]], { w: 9, renk: SARI, alfa: 0.9, uc0: 4, uc1: 10,
    tohum: 421 }, 194.47, 0.35, 0.55));
  const cB = S.koy(S.cumleYaz({ sozcukler: b, x: XK + PAD, y: Y_B, font: F1, satirH: 0, bosluk: 4,
    maxGen: IC + 400 }));
  const kB = cB.kel[cB.kel.length - 1];                       // believing.
  const ix0 = kB.x + olc(F1, "believ") - 6, ix1 = kB.x + olc(F1, "believing") + 6;
  S.koy(S.darbe([[ix0, Y_B - 0.86 * P1], [ix1, Y_B + 0.1 * P1]], { duz: true, w: 10, renk: SARI,
    alfa: 0.9, uc0: 4, uc1: 8, tohum: 431 }, 197.29, 0.2, 0.6));
  S.koy(S.darbe([[ix1, Y_B - 0.86 * P1], [ix0, Y_B + 0.1 * P1]], { duz: true, w: 10, renk: SARI,
    alfa: 0.9, uc0: 4, uc1: 8, tohum: 432 }, 197.43, 0.2, false));

  // ---- kart 2: 209,60 çerçeve · 210,18 cümle · 210,42 has sarı kutu · 210,74 güneş ikonu ----
  kartCiz(K2, 207.51, 2, "kart-2");
  const Y_C = K2.y + 110;
  const cC = S.koy(S.cumleYaz({ sozcukler: c, x: XK + PAD, y: Y_C, font: F2, satirH: 0,
    bosluk: 4, maxGen: IC + 400 }));
  const has = cC.kel[1];
  S.koy(S.darbe(altCizgi(has.x - 2, has.x + has.w + 2, has.y + 24, 440), { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14 },
    208.82, 0.3, 0.55));   // kutu yerine el altçizgisi (13.11 QA: kutu It ve a'ya değiyordu)

  // ---- kart 3: 216,90 çerçeve · 217,00 cümle (2 satır) · 217,80 recommend daire · 218,60 yatak ----
  kartCiz(K3, 215.23, 3, "kart-3");
  const Y_D = K3.y + 85, SAT = Math.round(P3 * 1.5);
  const cD = S.koy(S.cumleYaz({ sozcukler: d, x: XK + PAD, y: Y_D, font: F3, satirH: SAT,
    satirSay: [4, 5], bosluk: 4 }));
  halka(cD.kel[2], P3, 216.12, 451);
  // 220,85 Tavsiye: listedeki recommend sarı altı çizili (performative'in örneği)
  const xR = XS + wPA + wDot, wR = olc(FLS, "recommend");
  S.koy(S.darbe(altCizgi(xR - 3, xR + wR + 3, Y_V + 24, 61), { w: 8, renk: SARI, alfa: 0.9,
    uc0: 8, uc1: 14, tohum: 580 }, 219.25, 0.4, 0.5));
  // 225,97 Geniş zaman.: simple present sarı altı çizili
  const wS = olc(FLS, "simple present");
  S.koy(S.darbe(altCizgi(XS + 90 - 3, XS + 90 + wS + 3, Y_L2 + 22, 62), { w: 8, renk: SARI,
    alfa: 0.9, uc0: 8, uc1: 14, tohum: 581 }, 224.29, 0.3, 0.5));
}

surucu(kur, (f) => S.kare(f), KARE);

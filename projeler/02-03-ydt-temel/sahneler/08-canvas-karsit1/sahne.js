// SAHNE 08 — Karşıt çift 1 (düz canvas, 646 kare, t_bas 109,61; cümle 9). Kendini çizen kalem;
// zaman yalnız kare numarasından.
// Kök: "Nancy usually spends the weekend at home, but she is meeting her friends now."
// Aynı cümlede iki sinyal, iki fiil: usually → spends (alışkanlık), now → is meeting (şu an).
import { surucu } from "/ortak/surucu.js";
import { KUNYE } from "/projeler/02-03-ydt-temel/ortak/kunye.js";
import { Sahne, RT, elips, kutu, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 646, TBAS = 109.53, ICERIK = 634;
// Künye ajandasında "Contrast" varsa o, yoksa Rule (karşıt çift kuraldan sonra gelir)
const ETKIN = ((i) => (i >= 0 ? i : 2))(KUNYE.ajanda.findIndex((a) => /contrast|pair/i.test(a)));
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Contrast 1 / 3", cumle: 9,
  etkin: ETKIN });
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

// Yukarıdan iner: a→b yayı (yt yüksekliğinde, lift kadar kabarır) + ok başı.
function yayOk(x0, x1, yt, lift) {
  const N = 16, g = [];
  for (let i = 0; i <= N; i++) {
    const t = i / N;
    g.push([x0 + (x1 - x0) * t, yt - lift * Math.sin(Math.PI * t)]);
  }
  const dx = x1 - x0, dy = lift * Math.PI, L = Math.hypot(dx, dy), d = [dx / L, dy / L];
  const uc = (sg) => {
    const aci = 0.5 * sg, c = Math.cos(aci), s = Math.sin(aci), gx = -d[0], gy = -d[1];
    return [[x1 + (gx * c - gy * s) * 24, yt + (gx * s + gy * c) * 24], [x1 + d[0] * 0.5, yt + d[1] * 0.5]];
  };
  return [g, uc(1), uc(-1)];
}

// Düz ok: gövde + iki uç çizgisi (eksen çizgisi için yay yok).
function duzOk(x0, y0, x1, y1) {
  const dx = x1 - x0, dy = y1 - y0, L = Math.hypot(dx, dy), d = [dx / L, dy / L];
  const uc = (sg) => {
    const aci = 0.5 * sg, c = Math.cos(aci), s = Math.sin(aci), gx = -d[0], gy = -d[1];
    return [[x1 + (gx * c - gy * s) * 30, y1 + (gx * s + gy * c) * 30], [x1 + d[0] * 0.5, y1 + d[1] * 0.5]];
  };
  return [[[x0, y0], [(x0 + x1) / 2, (y0 + y1) / 2], [x1, y1]], uc(1), uc(-1)];
}

async function kur() {
  await S.kur();

  // Kök: 14 sözcük, 2 satır (7 + 7): satır 1 alışkanlık, satır 2 şu an. Yazı tipi iki satırı
  // 1640 px'e (x 140–1780) sığdırır.
  const kelimeler = S.dizi("Nancy", 111.45, 14);
  const parca = (a, b) => kelimeler.slice(a, b).map((k) => k.sozcuk).join(" ");
  const EK = 4, KAT = 64;
  const enGen = Math.max(olc(`700 ${KAT}px Fredoka`, parca(0, 7)),
    olc(`700 ${KAT}px Fredoka`, parca(7, 14))) + 6 * EK;
  const PX = Math.min(KAT, Math.floor((KAT * 1640) / enGen));
  const F = `700 ${PX}px Fredoka`;
  const Y1 = 300, SATIR = 170;

  // Tek kart: 110,20–110,90 (Karşıt çift.)
  S.koy(S.kart({ x: 100, y: 150, w: 1720, h: 420, tb: 110.12, tohum: 8, satirlar: [], ad: "kart",
    kutuSure: 0.2, kutuAralik: 0.12 }));

  // 111,53–116,01 cümle, sözcük sözcük (sarı alt çizgi kayar)
  const cum = S.koy(S.cumleYaz({ sozcukler: kelimeler, x: 140, y: Y1, font: F, satirH: SATIR,
    satirSay: [7, 7], bosluk: EK }));
  const kel = (i) => cum.kel[i];                 // 1 usually · 2 spends · 9 is · 10 meeting · 13 now
  const boy = cum.boy;

  // Zaman çizgisi (alt): 116,30–117,00 eksen + 117,54 alışkanlık noktaları + 119,38 şimdi noktası
  const TY = 760;
  duzOk(140, TY, 1790, TY).forEach((p, i) => S.koy(S.darbe(p, { duz: true, w: 4, renk: IKINCIL,
    alfa: 0.85, uc0: 8, uc1: 12, tohum: 300 + i }, 116.22 + (i ? 0.7 : 0), i ? 0.15 : 0.7,
    i ? false : 0.45)));
  for (let i = 0; i < 8; i++) {                  // genellikle: tekrarlayan noktalar (alışkanlık)
    S.koy(S.darbe(elips(220 + 135 * i, TY, 9, 9, 0, 90 + i), { w: 11, renk: KREM, alfa: 0.9,
      uc0: 4, uc1: 8 }, 117.46 + i * 0.09, 0.14, i === 0 ? 0.5 : false));
  }
  S.koy(S.elYazisi({ metin: "usually", x: 215, y: TY + 100, boy: 60, renk: IKINCIL, tb: 117.46,
    sure: 0.55 }));
  S.koy(S.darbe(elips(1560, TY, 28, 28, 0.1, 99), { w: 11, renk: SARI, alfa: 0.9, uc0: 8,
    uc1: 14 }, 119.3, 0.45, 0.6));              // şu anda: şimdi noktası
  S.koy(S.nabiz(1560, TY, 28, 119.82));
  S.koy(S.elYazisi({ metin: "now", x: 1535, y: TY + 100, boy: 64, renk: SARI, tb: 119.46,
    sure: 0.4 }));

  // 122,98 / 123,10 «sinyal»: usually ve now sarı altı çizili
  const isaret = (k, tb, tohum) => S.koy(S.darbe(altCizgi(k.x - 4, k.x + k.w + 4, k.y + 26, tohum),
    { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 520 + tohum }, tb, 0.4, 0.55));
  isaret(kel(1), 122.9, 51);
  isaret(kel(13), 123.02, 52);

  // 123,78 / 123,90 «fiil»: spends ve is meeting daire
  const halka = (a, b, tb, tohum) => S.koy(S.darbe(altCizgi(a.x - 2, b.x + b.w + 2, a.y + 26, tohum),
  { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14 }, tb, 0.4, 0.55));   // halka yerine el altçizgisi (13.11 QA)
  halka(kel(2), kel(2), 123.7, 61);
  halka(kel(9), kel(10), 123.82, 63);

  // 124,90 Usually → spends · 128,10 Now → is meeting (yay ok, sinyalden fiile)
  const yt = (k) => k.y - 1.2 * boy - 10;
  const merkez = (a, b) => (a.x + b.x + b.w) / 2;
  S.koy(S.darbeler(yayOk(kel(1).x + kel(1).w / 2, merkez(kel(2), kel(2)), yt(kel(1)), 40),
    { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 124.82, 0.22, 0.14, 0.5));
  S.koy(S.darbeler(yayOk(kel(13).x + kel(13).w / 2, merkez(kel(9), kel(10)), yt(kel(9)), 40),
    { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 128.02, 0.22, 0.14, 0.5));
  // 126,98 spends. · 130,10 is meeting.: ok ucunun yanında parıltı
  S.koy(S.parilti(merkez(kel(2), kel(2)) + 80, yt(kel(2)) - 6, 126.9, 24));
  S.koy(S.parilti(merkez(kel(9), kel(10)) + 150, yt(kel(9)) - 6, 130.02, 24));
}

surucu(kur, (f) => S.kare(f), KARE);

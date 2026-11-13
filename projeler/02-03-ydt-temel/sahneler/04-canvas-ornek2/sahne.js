// SAHNE 04 — Örnek 2/3 (düz canvas, 569 kare, t_bas 33,00; cümle 4). 02-03 YDT temel.
// Kendini çizen kalem; zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json.
// Kök: "Our company is going through a hard period these days." (bulut + takvim, geçici dönem).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, olc, altCizgi } from "./sahne-ortak.js";

const KARE = 569, TBAS = 33.0, ICERIK = 557;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const KOKDIZ = "/projeler/02-03-ydt-temel/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, DOLGU = RT.vurguDolgu;
const FF = (b) => `700 ${b}px Fredoka`;
const t = (i) => S.sozc[i].t0;   // cümle 4: 0 İkinci · 1 örnek. · 2–11 kök · 12–17 TR · 18–22 These days … · 23–29 Dönem … ister. · 30–35 Yapı … going.
// El yazısı penceresi: her sözcük kendi t0'ından sonraki sözcüğün t0'ına dek (kısa pencere uzar)
const pen = (a, n) => S.sozc.slice(a, a + n).map((w, i, d) => ({ t0: w.t0,
  t1: i < n - 1 ? d[i + 1].t0 : w.t1 }));

async function kur() {
  await S.kur();
  const [bulut, takvim] = await Promise.all([svgOku("tabler/cloud-rain.svg"),
    svgOku("tabler/calendar.svg")]);

  // 33,55 İkinci: daire içinde 2 (ilk 12 kare boş) · 34,03 örnek.: tek kart (0,8 sn)
  S.koy(S.daireSayi(2, 196, 176, t(0)));
  S.koy(S.kart({ x: 140, y: 250, w: 1640, h: 450, tb: t(1), tohum: 4, kutuSure: 0.2,
    kutuAralik: 0.2, satirlar: [] }));

  // 34,84–37,90 kök (Fredoka 80, 3 satır: 4/4/2 sözcük), sözcük zamanlı; sarı alt çizgi kayar
  const cum = S.cumleYaz({ sozcukler: S.sozc.slice(2, 12), x: 230, y: 400, maxGen: 1100,
    font: FF(80), satirH: 112, satirSay: [4, 4, 2], bosluk: 4 });
  const kel = (i) => cum.kel[i];               // 0 Our 1 company 2 is 3 going 4 through 5 a 6 hard 7 period 8 these 9 days.
  // 37,12 these: `these days.` sarı belirteç (yazının altında; önce koy = yazı üstte)
  {
    const A = kel(8), B = kel(9);
    S.koy(S.darbe([[A.x - 8, A.y - 26], [B.x + B.w + 8, A.y - 30]], { duz: true, w: 56,
      renk: DOLGU, alfa: 0.65, uc0: 6, uc1: 14, tohum: 91 }, t(10), 0.6, 0.5));
  }
  S.koy(cum);
  // 35,56 is: `is going` sarı daire
  {
    const A = kel(2), B = kel(3), x0 = A.x, x1 = B.x + B.w;
    S.koy(S.darbe(altCizgi(x0 - 2, x1 + 2, A.y + 26, 11),
      { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14 }, t(4), 0.4, 0.55));   // halka yerine el altçizgisi (13.11 QA)
  }

  // 36,28 hard: yağmur bulutu (zor dönem) · 37,12 these: takvim (sağ yarı, kartın içinde)
  S.koy(S.cizim({ svg: bulut, ad: "bulut", kutu: { x: 1170, y: 290, w: 230, h: 230 }, enCok: 10,
    w: 4, tb: t(8), sure: 0.9, olayEnCok: 4 }));
  S.koy(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 1430, y: 262, w: 290, h: 290 }, enCok: 10,
    w: 4, tb: t(10), sure: 1.0, olayEnCok: 4 }));

  // 38,53–41,00 Şirketimiz bugünlerde zor bir dönemden geçiyor.: Türkçe çeviri (el yazısı 48, y 785)
  S.koy(S.elYazisi({ metin: "Şirketimiz bugünlerde zor bir dönemden geçiyor.", x: 140, y: 785,
    boy: 48, renk: IKINCIL, sozcukler: pen(12, 6) }));

  // 42,21 These: ok `these days.` → takvim · 43,41 dönemi: takvimin altında sarı ayraç (dönem)
  {
    const B = kel(9);
    S.koy(S.darbeler(ok([B.x + B.w + 40, B.y - 30], [1405, 575], 3), { w: 6, renk: SARI, uc0: 10,
      uc1: 14 }, t(18), 0.3, 0.2, 0.5));
    S.koy(S.darbe([[1430, 575], [1430, 597], [1720, 597], [1720, 575]], { duz: true, w: 7,
      renk: SARI, alfa: 0.85, uc0: 12, uc1: 24 }, t(21), 0.4, 0.6));
  }

  // 45,09 geçici.: `geçici` (sarı) · 46,93 şimdiki: ok · 47,33 zaman: `-ing`
  S.koy(S.elYazisi({ metin: "geçici", x: 1330, y: 658, boy: 56, renk: SARI,
    sozcukler: [{ t0: t(24), t1: t(24) + 0.6 }] }));
  S.koy(S.darbeler(ok([1452, 640], [1530, 640], 4), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, t(27),
    0.3, 0.2, 0.5));
  S.koy(S.elYazisi({ metin: "-ing", x: 1552, y: 658, boy: 56, renk: SARI,
    sozcukler: [{ t0: t(28), t1: t(29) }] }));

  // 48,45 Yapı: formül kartı · 49,09 aynı: be + V-ing · 49,73 is · 50,29 artı · 50,93 going.
  {
    const kx = 140, ky = 815, fo = FF(54), y1 = ky + 72, y2 = ky + 148, x = kx + 50;
    const xa = x + olc(fo, "is") + 28, xb = xa + olc(fo, "+") + 28;
    S.koy(S.kart({ x: kx, y: ky, w: 760, h: 170, tb: t(30), tohum: 5, kutuSure: 0.14,
      kutuAralik: 0.1, satirlar: [
        { parca: [["be", KREM], ["  +  ", IKINCIL], ["V", KREM], ["-ing", SARI]], x, y: y1, font: fo,
          tb: t(32), sure: 0.3 },
        { parca: [["is", KREM]], x, y: y2, font: fo, tb: t(33), sure: 0.3 },
        { parca: [["+", IKINCIL]], x: xa, y: y2, font: fo, tb: t(34), sure: 0.3 },
        { parca: [["go", KREM], ["ing", SARI]], x: xb, y: y2, font: fo, tb: t(35), sure: 0.3 },
      ] }));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

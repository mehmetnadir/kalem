// SAHNE 05 (İLERİ) — Örnek 3 (düz canvas, 406 kare, t_bas 48,29; cümle 5; çıkış geçişi fade).
// Kök: "Our flight takes off at eleven tomorrow morning, so we have to leave home at nine." (tarife + tomorrow tuzağı).
// Zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json (küresel sn).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, olc } from "./sahne-ortak.js";
import { yaziNoktalari } from "/projeler/simple-present-ileri/ortak/kalem-canvas.js";

const KARE = 406, TBAS = 48.29, ICERIK = 394;
const KOKDIZ = "/projeler/simple-present-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;
// El yazısı (Caveat 700 tegaki, dalga 5b / K26): ortalı yazının x'i için genişlik glif verisinden
const eyGen = (m, b) => yaziNoktalari(m, S.EY.G, { upm: S.EY.M.unitsPerEm, asc: S.EY.M.ascender,
  boy: b, x: 0, taban: 0 }).gen;
// Sözcük penceresi: < 0,2 sn kısa pencere sonraki sözcüğün başına dek uzar (2–3 harflik sözcük)
const pen = (w) => w.map((q, i) => ({ t0: q.t0,
  t1: q.t1 - q.t0 < 0.2 && w[i + 1] ? w[i + 1].t0 : q.t1 }));

async function kur() {
  await S.kur();
  const [ucak, takvim, saat] = await Promise.all([svgOku("coco/plane.svg"), svgOku("tabler/calendar.svg"),
    svgOku("coco/clock.svg")]);

  // 48,84–50,05 daire içinde 3 (ilk 12 kare boş)
  S.koy(S.daireSayi(3, 200, 190, 48.84));

  // 50,05–54,21 İngilizce kök (Fredoka 56, 3 satır, sözcük zamanlı)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Our", 50.05, 16), x: 140, y: 300, maxGen: 980, font: FF(56),
    satirH: 88 }));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));
  const iki = (a, b, tb, tohum, renk) => {   // iki sözcüğü kapsayan halka (satır bölünürse sözcük başına)
    if (a.satir === b.satir) S.koy(S.halka({ x: a.x, y: a.y, w: b.x + b.w - a.x }, tb, 0.4, tohum, 6, renk));
    else { S.koy(S.halka(a, tb, 0.3, tohum, 6, renk)); S.koy(S.halka(b, tb + 0.16, 0.3, tohum + 1, 6, renk)); }
  };
  iki(kel("takes"), kel("off"), 50.7, 31, SARI);                   // takes off: sarı
  S.koy(S.halka(kel("tomorrow"), 51.72, 0.4, 33, 8, KIRMIZI));     // tomorrow: kırmızı daire (tuzak)

  // 50,05–54,81 sağ: takvim (yarın) + saat (11:00) üstte, uçak altta
  S.koy(S.cizim({ svg: ucak, ad: "ucak", kutu: { x: 1230, y: 560, w: 560, h: 300 }, enCok: 14, w: 4, tb: 50.4,
    sure: 1.3, olayEnCok: 5 }));
  S.koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 1560, y: 150, w: 200, h: 200 }, enCok: 6, w: 4, tb: 51.2,
    sure: 0.8, olayEnCok: 3 }));
  S.koy(S.metinPop({ parca: [["11:00", KREM]], x: 1660, y: 418, font: FF(64), hiza: "orta", tb: 52.0, sure: 0.35,
    ses: 0.5 }));
  S.koy(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 1230, y: 150, w: 200, h: 200 }, enCok: 8, w: 4, tb: 51.7,
    sure: 0.8, olayEnCok: 3 }));
  // 52,40 `yarın` etiketi: anlatımsız, hedef 0,5 sn; x 1330 ortalı (takvim altı)
  S.koy(S.elYazisi({ metin: "yarın", x: 1330 - eyGen("yarın", 64) / 2, y: 418, boy: 64,
    renk: KREM, tb: 52.4, sure: 0.5 }));
  S.koy(S.darbe([[1215, 880], [1500, 884], [1810, 879]], { duz: true, w: 3.4, renk: IKINCIL, alfa: 0.8, uc0: 6,
    uc1: 10, tohum: 77 }, 53.0, 0.45, 0.45));
  S.koy(S.parilti(1700, 600, 53.9, 26));

  // 54,94–57,34 Türkçe çeviri: her sözcük kendi penceresinde (Uçuşumuz 54,94 · yarın 55,58 ·
  // on 55,98 · birde 56,14 · kalkıyor. 56,38–57,34). `sabah` anlatım verisinde yok:
  // yarın penceresi ikiye bölünür (yarın 55,58–55,74 · sabah 55,74–55,98)
  const yTR = sonSatir + 80;
  const tr = S.dizi("Uçuşumuz", 54.94, 5), ya = tr[1];
  const trSoz = pen([tr[0], { t0: ya.t0, t1: 55.74 }, { t0: 55.74, t1: tr[2].t0 }, ...tr.slice(2)]);
  S.koy(S.elYazisi({ metin: "Uçuşumuz yarın sabah on birde kalkıyor.", x: 140, y: yTR,
    renk: IKINCIL, sozcukler: trSoz }));

  // 57,41–61,41 tarife tablosu: kutu + başlık + "11:00 takes off"; tomorrow kırmızı çizgi ≠ will
  const kx = 140, ky = 660, kw = 1000, kh = 310;
  S.koy(S.kart({ x: kx, y: ky, w: kw, h: kh, tb: 57.41, tohum: 5, kutuSure: 0.12, kutuAralik: 0.06, satirlar: [
    { parca: [["tarife kesin → ", KREM], ["Simple Present", SARI]], x: kx + 50, y: ky + 80, font: CV(64), tb: 57.6,
      sure: 0.4 },
  ] }));
  S.koy(S.metinPop({ parca: [["11:00", KREM]], x: kx + 50, y: ky + 185, font: FF(76), tb: 58.2, sure: 0.3, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["takes off", SARI]], x: kx + 340, y: ky + 185, font: FF(76), tb: 58.6, sure: 0.3,
    ses: 0.5 }));
  const fz = FF(64), yT = ky + 275;
  S.koy(S.metinPop({ parca: [["tomorrow", KREM]], x: kx + 50, y: yT, font: fz, tb: 60.17, sure: 0.3, ses: 0.5 }));
  const tw = olc(fz, "tomorrow");
  S.koy(S.darbe([[kx + 44, yT + 12], [kx + 50 + tw / 2, yT + 9], [kx + 56 + tw, yT + 13]],
    { duz: true, w: 8, renk: KIRMIZI, alfa: 0.9, uc0: 8, uc1: 12 }, 60.4, 0.2, 0.7));
  S.koy(S.metinPop({ parca: [["≠ will", KIRMIZI]], x: kx + 50 + tw + 40, y: yT, font: fz, tb: 60.6, sure: 0.3,
    ses: 0.5 }));
  S.koy(S.parilti(kx + kw - 70, ky + 60, 60.8));
}

surucu(kur, (f) => S.kare(f), KARE);

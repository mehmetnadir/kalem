// SAHNE 05 (İLERİ) — Örnek 3 (düz canvas, 406 kare, t_bas 49,49; cümle 5; çıkış geçişi fade).
// Kök: "Our flight takes off at eleven tomorrow morning, so we have to leave home at nine." (tarife + tomorrow tuzağı).
// Zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json (küresel sn).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, olc } from "./sahne-ortak.js";
import { yaziNoktalari } from "/projeler/simple-present-ileri/ortak/kalem-canvas.js";

const KARE = 406, TBAS = 49.49, ICERIK = 394;
const KOKDIZ = "/projeler/simple-present-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`;
// El yazısı (Caveat 700 tegaki, dalga 5b / K26): ortalı yazının x'i için genişlik glif verisinden
const eyGen = (m, b) => yaziNoktalari(m, S.EY.G, { upm: S.EY.M.unitsPerEm, asc: S.EY.M.ascender,
  boy: b, x: 0, taban: 0 }).gen;
// El yazısı `sol → sağ` (06.11): `→` fontta yok; ok() darbesi. Süre: sol %40, ok %15, sağ %45
const okluYazi = (sol, sag, a) => {
  const { x, y, boy: b, tb, sure: u } = a, bos = 0.3 * b;
  const xo = x + eyGen(sol, b) + bos, yo = y - 0.25 * b;
  const yz = (metin, xx, t, s, renk) =>
    S.elYazisi({ metin, x: xx, y, boy: b, renk, tb: t, sure: s });
  return [yz(sol, x, tb, u * 0.4, a.renk),
    ...S.darbeler(ok([xo, yo], [xo + b, yo], a.tohum), { w: a.w, renk: a.renk, uc0: 8, uc1: 12 },
      tb + u * 0.4, u * 0.05, u * 0.025, 0.3),
    yz(sag, xo + b + bos, tb + u * 0.55, u * 0.45, a.sag || a.renk)];
};
// Sözcük penceresi: < 0,2 sn kısa pencere sonraki sözcüğün başına dek uzar (2–3 harflik sözcük)
const pen = (w) => w.map((q, i) => ({ t0: q.t0,
  t1: q.t1 - q.t0 < 0.2 && w[i + 1] ? w[i + 1].t0 : q.t1 }));

async function kur() {
  await S.kur();
  const [ucak, takvim, saat] = await Promise.all([svgOku("coco/plane.svg"), svgOku("tabler/calendar.svg"),
    svgOku("coco/clock.svg")]);

  // 50,04–51,25 daire içinde 3 (ilk 12 kare boş)
  S.koy(S.daireSayi(3, 200, 190, 50.04));

  // 51,25–55,41 İngilizce kök (Fredoka 56, 3 satır, sözcük zamanlı)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Our", 51.25, 16), x: 140, y: 300, maxGen: 980, font: FF(56),
    satirH: 88 }));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));
  const iki = (a, b, tb, tohum, renk) => {   // iki sözcüğü kapsayan halka (satır bölünürse sözcük başına)
    if (a.satir === b.satir) S.koy(S.halka({ x: a.x, y: a.y, w: b.x + b.w - a.x }, tb, 0.4, tohum, 6, renk));
    else { S.koy(S.halka(a, tb, 0.3, tohum, 6, renk)); S.koy(S.halka(b, tb + 0.16, 0.3, tohum + 1, 6, renk)); }
  };
  iki(kel("takes"), kel("off"), 51.9, 31, SARI);                   // takes off: sarı
  S.koy(S.halka(kel("tomorrow"), 52.92, 0.4, 33, 8, KIRMIZI));     // tomorrow: kırmızı daire (tuzak)

  // 51,25–56,01 sağ: takvim (yarın) + saat (11:00) üstte, uçak altta
  S.koy(S.cizim({ svg: ucak, ad: "ucak", kutu: { x: 1230, y: 560, w: 560, h: 300 }, enCok: 14, w: 4, tb: 51.6,
    sure: 1.3, olayEnCok: 5 }));
  S.koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 1560, y: 150, w: 200, h: 200 }, enCok: 6, w: 4, tb: 52.4,
    sure: 0.8, olayEnCok: 3 }));
  S.koy(S.metinPop({ parca: [["11:00", KREM]], x: 1660, y: 418, font: FF(64), hiza: "orta", tb: 53.2, sure: 0.35,
    ses: 0.5 }));
  S.koy(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 1230, y: 150, w: 200, h: 200 }, enCok: 8, w: 4, tb: 52.9,
    sure: 0.8, olayEnCok: 3 }));
  // 53,60 `yarın` etiketi: anlatımsız, hedef 0,5 sn; x 1330 ortalı (takvim altı)
  S.koy(S.elYazisi({ metin: "yarın", x: 1330 - eyGen("yarın", 64) / 2, y: 418, boy: 64,
    renk: KREM, tb: 53.6, sure: 0.5 }));
  S.koy(S.darbe([[1215, 880], [1500, 884], [1810, 879]], { duz: true, w: 3.4, renk: IKINCIL, alfa: 0.8, uc0: 6,
    uc1: 10, tohum: 77 }, 54.2, 0.45, 0.45));
  S.koy(S.parilti(1700, 600, 55.1, 26));

  // 56,14–58,54 Türkçe çeviri: her sözcük kendi penceresinde (Uçuşumuz 56,14 · yarın 56,78 ·
  // on 57,18 · birde 57,34 · kalkıyor. 57,58–58,54). `sabah` anlatım verisinde yok:
  // yarın penceresi ikiye bölünür (yarın 56,78–56,94 · sabah 56,94–57,18)
  const yTR = sonSatir + 80;
  const tr = S.dizi("Uçuşumuz", 56.14, 5), ya = tr[1];
  const trSoz = pen([tr[0], { t0: ya.t0, t1: 56.94 }, { t0: 56.94, t1: tr[2].t0 }, ...tr.slice(2)]);
  S.koy(S.elYazisi({ metin: "Uçuşumuz yarın sabah on birde kalkıyor.", x: 140, y: yTR,
    renk: IKINCIL, sozcukler: trSoz }));

  // 58,61–62,61 tarife tablosu: kutu + başlık + "11:00 takes off"; tomorrow kırmızı çizgi + "tuzak" (DUZ3 16.11: "≠ will" mutlaktı)
  const kx = 140, ky = 660, kw = 1000, kh = 310;
  S.koy(S.kart({ x: kx, y: ky, w: kw, h: kh, tb: 58.61, tohum: 5, kutuSure: 0.12, kutuAralik: 0.06,
    satirlar: [] }));
  S.koy(okluYazi("tarife kesin", "Simple Present",
    { x: kx + 50, y: ky + 80, boy: 64, renk: KREM, sag: SARI, w: 6, tb: 58.8, sure: 0.6,
      tohum: 8 }));
  S.koy(S.metinPop({ parca: [["11:00", KREM]], x: kx + 50, y: ky + 185, font: FF(76), tb: 59.4, sure: 0.3, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["takes off", SARI]], x: kx + 340, y: ky + 185, font: FF(76), tb: 59.8, sure: 0.3,
    ses: 0.5 }));
  const fz = FF(64), yT = ky + 275;
  S.koy(S.metinPop({ parca: [["tomorrow", KREM]], x: kx + 50, y: yT, font: fz, tb: 61.37, sure: 0.3, ses: 0.5 }));
  const tw = olc(fz, "tomorrow");
  S.koy(S.darbe([[kx + 44, yT + 12], [kx + 50 + tw / 2, yT + 9], [kx + 56 + tw, yT + 13]],
    { duz: true, w: 8, renk: KIRMIZI, alfa: 0.9, uc0: 8, uc1: 12 }, 61.6, 0.2, 0.7));
  S.koy(S.metinPop({ parca: [["tuzak", KIRMIZI]], x: kx + 50 + tw + 40, y: yT, font: fz, tb: 61.85, sure: 0.3,
    ses: 0.5 }));
  S.koy(S.parilti(kx + kw - 70, ky + 60, 62.0));
}

surucu(kur, (f) => S.kare(f), KARE);

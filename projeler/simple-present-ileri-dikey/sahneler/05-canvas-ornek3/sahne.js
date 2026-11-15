// SAHNE 05 (DİKEY, İLERİ) — Örnek 3: düz canvas, 1080x1920, 406 kare,
// t_bas 49,49; cümle 5; çıkış geçişi fade.
// Kök: "Our flight takes off at eleven tomorrow morning, so we have to
// leave home at nine." (tarife + tomorrow tuzağı).
// Zaman yalnız kare numarasından; zamanlar sozcukler.json / altyazi.json
// ile aynı çerçevede (küresel sn).
// Yerleşim sıfırdan dikey: kart (tam genişlik) → TR çeviri →
// ORTA uçak + takvim/saat → alt tarife (2 satır).
import { surucu } from "/ortak/surucu.js";
import { yaziNoktalari } from "/projeler/simple-present-ileri-dikey/ortak/kalem-canvas.js";
import { Sahne, RT, kutu, olc } from "./sahne-ortak.js";

const KARE = 406, TBAS = 49.49, ICERIK = 394;
const S = new Sahne({
  tbas: TBAS,
  kare: KARE,
  icerik: ICERIK,
  bolum: "Example 3 / 3",
  cumle: 5
});
const KOKDIZ = "/projeler/simple-present-ileri-dikey/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKI = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;
// El yazısı (tegaki Caveat, dalga 5b / K26): sözcük penceresi = anlatım t0/t1
// (küresel sn); 2-3 harflik kısa pencere sonraki sözcüğün başına dek uzar.
const pen = (ad, t, n) => {
  const L = S.dizi(ad, t, n);
  return L.map((w, i) => ({
    t0: w.t0,
    t1: w.t1 - w.t0 < 0.2 && L[i + 1] ? L[i + 1].t0 : w.t1
  }));
};

async function kur() {
  await S.kur();
  const [ucak, takvim, saat] = await Promise.all([
    svgOku("coco/plane.svg"),
    svgOku("tabler/calendar.svg"),
    svgOku("coco/clock.svg")
  ]);

  // kart: tam genişlik 984, Fredoka 64, sözcük zamanlı
  // (ilk 12 kare boş; kutu 12. kareden çizilir)
  const cum = S.koy(S.cumleYaz({
    sozcukler: S.dizi("Our", 51.25, 16),
    x: 88,
    y: 452,
    maxGen: 904,
    font: FF(64),
    satirH: 80
  }));
  const sonTaban = Math.max(...cum.kel.map((k) => k.y));
  const kartAlt = sonTaban + 24 + 34;
  S.koy(S.darbeler(
    kutu(48, 372, 984, kartAlt - 372, 9),
    { w: 4, renk: IKI, uc0: 10, uc1: 18 },
    S.zm(12),
    0.2,
    0.12,
    0.55
  ));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);
  const iki = (a, b, tb, tohum, renk) => {
    // iki sözcüğü kapsayan halka (satır bölünürse sözcük başına)
    if (a.satir === b.satir) {
      S.koy(S.halka({ x: a.x, y: a.y, w: b.x + b.w - a.x }, tb, 0.4, tohum, 6, renk, 9));
    } else {
      S.koy(S.halka(a, tb, 0.3, tohum, 6, renk, 9));
      S.koy(S.halka(b, tb + 0.16, 0.3, tohum + 1, 6, renk, 9));
    }
  };
  iki(kel("takes"), kel("off"), 51.9, 31, SARI); // takes off: sarı
  // tomorrow: kırmızı daire (tuzak)
  S.koy(S.halka(kel("tomorrow"), 52.92, 0.4, 33, 8, KIRMIZI, 9));

  // 56,14–58,54 Türkçe çeviri (Caveat 64, mürekkep, tek satır): her sözcük kendi
  // penceresinde; `sabah` anlatım verisinde yok → yarın penceresi ikiye bölünür
  // (yarın 56,78–56,94 · sabah 56,94–57,18); `on` 0,2 sn altı → birde başına dek.
  // Yatay kardeşle aynı yol (simple-present-ileri 05). İnceleme DÜZELT 2.
  const yTR = kartAlt + 62;
  const tr = pen("Uçuşumuz", 56.14, 5), ya = tr[1];
  const trSoz = [tr[0], { t0: ya.t0, t1: 56.94 }, { t0: 56.94, t1: tr[2].t0 }, ...tr.slice(2)];
  S.koy(S.elYazisi({
    metin: "Uçuşumuz yarın sabah on birde kalkıyor.",
    x: 64,
    y: yTR,
    boy: 64,
    renk: KREM,
    sozcukler: trSoz
  }));

  // ORTA bant: solda uçak (660 px), sağda takvim (yarın) + saat (11:00)
  const B0 = yTR + 34, B1 = 1170;
  S.koy(S.cizim({
    svg: ucak,
    ad: "ucak",
    kutu: { x: 48, y: B1 - 352, w: 660, h: 352 },
    enCok: 14,
    w: 4.2,
    tb: 51.6,
    sure: 1.3,
    olayEnCok: 5
  }));
  S.koy(S.darbe(
    [[40, B1 + 6], [380, B1 + 10], [720, B1 + 5]],
    { duz: true, w: 4, renk: IKI, alfa: 0.8, uc0: 6, uc1: 10, tohum: 77 },
    54.2,
    0.45,
    0.45
  ));
  S.koy(S.cizim({
    svg: takvim,
    ad: "takvim",
    kutu: { x: 722, y: B0 + 16, w: 150, h: 150 },
    enCok: 8,
    w: 4.2,
    tb: 52.9,
    sure: 0.8,
    olayEnCok: 3
  }));
  // 53,60 anlatımsız etiket `yarın`: hedef 0,45 sn → 54,05; orta x 797
  const eyGen = (str, boy) => yaziNoktalari(str, S.EY.G, {
    upm: S.EY.M.unitsPerEm,
    asc: S.EY.M.ascender,
    boy,
    x: 0,
    taban: 0
  }).gen;
  S.koy(S.elYazisi({
    metin: "yarın",
    x: 797 - eyGen("yarın", 64) / 2,
    y: B0 + 238,
    boy: 64,
    renk: KREM,
    tb: 53.6,
    sure: 0.45
  }));
  S.koy(S.cizim({
    svg: saat,
    ad: "saat",
    kutu: { x: 882, y: B0 + 16, w: 150, h: 150 },
    enCok: 6,
    w: 4.2,
    tb: 52.4,
    sure: 0.8,
    olayEnCok: 3
  }));
  S.koy(S.metinPop({
    parca: [["11:00", KREM]],
    x: 962,
    y: B0 + 238,
    font: FF(64),
    hiza: "orta",
    tb: 53.2,
    sure: 0.35,
    ses: 0.5
  }));
  S.koy(S.parilti(600, B0 + 40, 55.1, 28));

  // 58,61–62,61 alt tarife: 11:00 takes off / tomorrow + "tuzak" (kırmızı çizgi; DUZ3 16.11: "≠ will" mutlaktı)
  const fz = FF(88), y1 = 1290, y2 = 1375;
  const w11 = olc(fz, "11:00");
  S.koy(S.metinPop({
    parca: [["11:00", KREM]],
    x: 88,
    y: y1,
    font: fz,
    tb: 58.8,
    sure: 0.3,
    ses: 0.5
  }));
  S.koy(S.metinPop({
    parca: [["takes off", SARI]],
    x: 88 + w11 + 56,
    y: y1,
    font: fz,
    tb: 59.8,
    sure: 0.3,
    ses: 0.5
  }));
  const tw = olc(fz, "tomorrow");
  S.koy(S.metinPop({
    parca: [["tomorrow", KREM]],
    x: 88,
    y: y2,
    font: fz,
    tb: 61.37,
    sure: 0.3,
    ses: 0.5
  }));
  S.koy(S.darbe(
    [[80, y2 + 10], [88 + tw / 2, y2 + 8], [96 + tw, y2 + 11]],
    { duz: true, w: 10, renk: KIRMIZI, alfa: 0.9, uc0: 8, uc1: 12 },
    61.6,
    0.2,
    0.7
  ));
  S.koy(S.metinPop({
    parca: [["tuzak", KIRMIZI]],
    x: 88 + tw + 56,
    y: y2,
    font: fz,
    tb: 61.85,
    sure: 0.3,
    ses: 0.5
  }));
  S.koy(S.parilti(990, y1 - 70, 62.0, 26));
}

surucu(kur, (f) => S.kare(f), KARE);

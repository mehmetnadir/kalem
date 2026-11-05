// SAHNE 04 (İLERİ, DİKEY 1080x1920) — Örnek 2 (düz canvas, 487 kare,
// t_bas 32,45; cümle 4). Zaman yalnız kare numarasından.
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (sahne-ortak.js çizer),
// platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–694) · sol TR 3 satır + sağ durum fiili kutusu
// (700–870) · formül kartı tek satır (878–962)
// · alt bant 972–1392: araba + otobüs kutuları 430x420 sabit.
// Toplanma / küçültme YOK.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 487, TBAS = 32.45, ICERIK = 475;
const TR0 = 752, TRA = 52, DB0 = 712, FK0 = 878;
const KOKDIZ = "/projeler/simple-present-ileri-dikey/ortak/cizim";
const S = new Sahne({
  tbas: TBAS,
  kare: KARE,
  icerik: ICERIK,
  bolum: "Example 2 / 3",
  cumle: 4
});
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
// El yazısı (tegaki Caveat, dalga 5b / K26): sözcük penceresi = anlatım t0/t1
// (küresel sn); 2-3 harflik kısa pencere sonraki sözcüğün başına dek uzar.
const pen = (ad, t, n) => {
  const L = S.dizi(ad, t, n);
  return L.map((w, i) => ({
    t0: w.t0,
    t1: w.t1 - w.t0 < 0.2 && L[i + 1] ? L[i + 1].t0 : w.t1
  }));
};
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;

async function kur() {
  await S.kur();
  const [araba, otobus] = await Promise.all([
    svgOku("coco/car.svg"),
    svgOku("coco/bus.svg")
  ]);

  // 33,00: kart çerçevesi (el kutusu, 4 px). İlk 12 kare boş: künye hazır,
  // tuval boş.
  S.koy(S.darbeler(
    kutu(48, 372, 984, 322, 4),
    { w: 4.2, renk: IKINCIL, uc0: 10, uc1: 18 },
    33.0,
    0.2,
    0.14,
    0.55
  ));

  // 34,13–39,17 İngilizce kök (Fredoka 64, sözcük zamanlı, 4 satır:
  // 4 / 4 / 4 / 3 sözcük)
  const cum = S.koy(S.cumleYaz({
    sozcukler: S.dizi("Mike", 34.13, 15),
    x: 88,
    y: 448,
    maxGen: 904,
    font: "700 64px Fredoka",
    satirH: 70,
    satirSay: [4, 4, 4, 3],
    bosluk: 4
  }));
  const kel = (i) => cum.kel[i];
  // satır 1: 0 Mike … 3 cars, | 2: 4 but … 7 takes | 3: 8 the … 11 parking |
  // 4: 12 costs 13 so 14 much.
  const cevre = (i, tb, egim, tohum) => {
    // tek sözcüğe sarı daire (turuncu belirteç)
    const A = kel(i);
    S.koy(S.darbe(
      elips(A.x + A.w / 2, A.y - 24, A.w / 2 + 12, 48, egim, tohum),
      { w: 9, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 },
      tb,
      0.4,
      0.55
    ));
  };
  cevre(1, 34.62, -0.03, 11); // owns
  cevre(12, 38.28, -0.03, 13); // costs
  { // usually: kalıcı sarı alt çizgi
    const u = kel(6);
    S.koy(S.darbe(
      altCizgi(u.x - 4, u.x + u.w + 4, u.y + 17, 55),
      { w: 10, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14, tohum: 3 },
      36.55,
      0.3,
      0.55
    ));
  }

  // 34,13–39,77 ALT BANT (972–1392): araba kutusu 430x420 (sol) +
  // otobüs kutusu 430x420 (sağ), ok; sabit, küçülme yok
  S.koy(S.cizim({
    svg: araba,
    ad: "araba",
    kutu: { x: 48, y: 972, w: 430, h: 420 },
    enCok: 12,
    w: 4.4,
    tb: 34.6,
    sure: 1.0,
    olayEnCok: 5
  }));
  S.koy(S.darbeler(
    ok([492, 1182], [590, 1182], 4),
    { w: 9, renk: SARI, uc0: 10, uc1: 14 },
    36.4,
    0.2,
    0.14,
    0.5
  ));
  S.koy(S.cizim({
    svg: otobus,
    ad: "otobus",
    kutu: { x: 602, y: 972, w: 430, h: 420 },
    enCok: 14,
    w: 4.4,
    tb: 37.4,
    sure: 1.2,
    olayEnCok: 5
  }));
  S.koy(S.parilti(1000, 1000, 39.4, 26));

  // 39,90–44,14 SOL ÜST SÜTUN: Türkçe çeviri (Caveat 64 mürekkep, 3 satır,
  // ≤ 24 karakter); 3 satır = 4 / 2 / 2 sözcük penceresi (39,90–41,50 ·
  // 41,62–42,38 · 42,46–44,14)
  S.koy(S.elYazisi({
    metin: "Mike'ın iki arabası var,",
    x: 88,
    y: TR0,
    boy: 64,
    renk: KREM,
    sozcukler: pen("Mike'ın", 39.9, 4)
  }));
  S.koy(S.elYazisi({
    metin: "ama genellikle",
    x: 88,
    y: TR0 + TRA,
    boy: 64,
    renk: KREM,
    sozcukler: pen("ama", 41.62, 2)
  }));
  S.koy(S.elYazisi({
    metin: "otobüse biner.",
    x: 88,
    y: TR0 + 2 * TRA,
    boy: 64,
    renk: KREM,
    sozcukler: pen("otobüse", 42.46, 2)
  }));

  // 46,05–48,29 SAĞ ÜST SÜTUN: durum fiili kutusu (412 px)
  S.koy(S.darbeler(
    kutu(620, DB0, 412, 150, 41),
    { w: 4.5, renk: SARI, uc0: 8, uc1: 14 },
    46.05,
    0.12,
    0.08,
    0.5
  ));
  // 46,05–47,17 «durum fiilidir:» (pencere: durum 46,05–46,29 · fiilidir 46,37–47,17)
  S.koy(S.elYazisi({
    metin: "durum fiili:",
    x: 642,
    y: DB0 + 60,
    boy: 64,
    renk: SARI,
    sozcukler: pen("durum", 46.05, 2),
    ses: 0.5
  }));
  S.koy(S.not({
    parca: [["own · cost · know", KREM]],
    x: 642,
    y: DB0 + 126,
    font: "700 64px Caveat",
    tb: 46.6,
    sure: 0.9,
    ses: 0.4
  }));

  // 44,00–48,29 FORMÜL KARTI TEK SATIR (FK0–962): owns · costs  ·  is owning ✗
  const F = "700 64px Fredoka", yK = FK0 + 66, x0 = 80, xs = 540;
  S.koy(S.darbeler(
    kutu(48, FK0, 984, 962 - FK0, 6),
    { w: 4.2, renk: IKINCIL, uc0: 10, uc1: 18 },
    44.0,
    0.14,
    0.1,
    0.5
  ));
  S.koy(S.metinPop({
    parca: [["owns", SARI]],
    x: x0,
    y: yK,
    font: F,
    tb: 44.29,
    sure: 0.35,
    ses: 0.5
  }));
  S.koy(S.metinPop({
    parca: [["  ·  ", IKINCIL], ["costs", SARI]],
    x: x0 + olc(F, "owns"),
    y: yK,
    font: F,
    tb: 45.25,
    sure: 0.35,
    ses: 0.5
  }));
  cevre(1, 44.35, -0.03, 21); // owns yeniden vurgulanır
  cevre(12, 45.3, -0.03, 23); // costs yeniden vurgulanır

  // is own-ing: ing kırmızı çizgiyle silinir (47,37) + kırmızı ✗
  const w1 = olc(F, "is own"), w2 = olc(F, "ing");
  S.koy(S.metinPop({
    parca: [["is own", KREM], ["ing", KREM]],
    x: xs,
    y: yK,
    font: F,
    tb: 46.9,
    sure: 0.35,
    ses: 0.4
  }));
  S.koy(S.darbe(
    [[xs + w1 - 4, yK - 20], [xs + w1 + w2 + 6, yK - 20]],
    { duz: true, w: 10, renk: KIRMIZI, alfa: 0.9, uc0: 8, uc1: 12 },
    47.37,
    0.2,
    0.7
  ));
  const cx1 = xs + w1 + w2 + 24, cx2 = cx1 + 48;
  S.koy(S.darbeler(
    [[[cx1, yK - 46], [cx2, yK + 6]], [[cx2, yK - 46], [cx1, yK + 6]]],
    { duz: true, w: 10, renk: KIRMIZI, alfa: 0.9, uc0: 6, uc1: 8 },
    47.62,
    0.14,
    0.1,
    0.6
  ));
  S.koy(S.parilti(990, 912, 47.9, 28));
}

surucu(kur, (f) => S.kare(f), KARE);

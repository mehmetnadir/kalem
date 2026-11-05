// SAHNE 04 (DİKEY) — Örnek 2: düz canvas, 1080x1920, 487 kare, t_bas 30,15; cümle 4.
// Zaman yalnız kare numarasından;
// zamanlar sozcukler.json / altyazi.json ile aynı çerçevede (küresel sn).
// Yerleşim sıfırdan dikey:
// kart (tam genişlik) → TR çeviri → not → ORTA figür + piyano → alt formül.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, kutu, olc } from "./sahne-ortak.js";
import { yaziNoktalari }
  from "/projeler/present-continuous-dikey/ortak/kalem-canvas.js";

const KARE = 487, TBAS = 30.15, ICERIK = 475;
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 2 / 3", cumle: 4
});
const KOKDIZ = "/projeler/present-continuous-dikey/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKI = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`;
// El yazısı (tegaki Caveat, dalga 5 / K26): sözcük penceresi = anlatım t0/t1 (küresel sn);
// <0,2 sn pencere sonraki sözcüğün başına uzar. Genişlik tegaki verisinden ölçülür.
const pen = (ad, t, n) => {
  const q = S.dizi(ad, t, n + 1);
  return q.slice(0, n).map((w, k) => ({ t0: w.t0, t1: w.t1 - w.t0 < 0.2 ? q[k + 1].t0 : w.t1 }));
};
const eyGen = (m, b) => yaziNoktalari(m, S.EY.G, { upm: S.EY.M.unitsPerEm,
  asc: S.EY.M.ascender, boy: b, x: 0, taban: 0 }).gen;

async function kur() {
  await S.kur();
  const [kiz, piyano, nota] = await Promise.all([svgOku("open-peeps/sitting-2.svg"),
    svgOku("tabler/piano.svg"), svgOku("tabler/music.svg")]);

  // kart: tam genişlik 984, Fredoka 72, sözcük zamanlı
  // (ilk 12 kare boş; kutu 12. kareden çizilir)
  const cum = S.koy(S.cumleYaz({
    sozcukler: S.dizi("My", 31.44, 8), x: 88, y: 470, maxGen: 904, font: FF(72),
    satirH: 88 }));
  const sonTaban = Math.max(...cum.kel.map((k) => k.y)), kartAlt = sonTaban + 20 + 28;
  S.koy(S.darbeler(
    kutu(48, 372, 984, kartAlt - 372, 7), { w: 4, renk: IKI, uc0: 10, uc1: 18 }, S.zm(12), 0.2,
    0.12, 0.55));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 34,89–37,37 «Kardeşim bu dönem piyano dersi alıyor.» (pencere: 6 sözcük)
  const yTR = kartAlt + 58;
  S.koy(S.elYazisi({ metin: "Kardeşim bu dönem piyano dersi alıyor.", x: 64, y: yTR, boy: 64,
    renk: KREM, sozcukler: pen("Kardeşim", 34.89, 6) }));

  // 37,41 not: şu anda değil → bu günlerde (Caveat 64, ok kalemle)
  const yN = yTR + 70, w1 = eyGen("şu anda değil", 64), w2 = eyGen("bu günlerde", 64);
  const xN = Math.max(64, (1080 - (w1 + w2 + 190)) / 2);
  // 37,41–39,13 «şu anda (piyanonun başında) değil» (pencere: şu 37,41 · anda 37,65 · değil 38,65)
  S.koy(S.elYazisi({ metin: "şu anda değil", x: xN, y: yN, boy: 64, renk: KREM,
    sozcukler: [...pen("Şu", 37.41, 2), ...pen("değil.", 38.65, 1)] }));
  S.koy(S.darbeler(
    ok([xN + w1 + 22, yN - 20], [xN + w1 + 150, yN - 20], 3),
    { w: 7, renk: SARI, uc0: 10, uc1: 14 },
    38.9, 0.18, 0.12, 0.5));
  // 39,53–40,01 «bu günlerde» (pencere: bu 39,53 → günlerde başına · günlerde 39,69–40,01)
  S.koy(S.elYazisi({ metin: "bu günlerde", x: xN + w1 + 172, y: yN, boy: 64, renk: SARI,
    sozcukler: pen("bu", 39.53, 2) }));

  // ORTA: kız kardeş (sitting-2) + piyano + 3 nota; bant yN+36 → 1150
  const fUst = yN + 22, fAlt = 1180, fYuk = fAlt - fUst;
  S.koy(S.cizim({
    svg: kiz, kutu: { x: 70, y: fUst, w: 440, h: fYuk }, ad: "kiz", esik: 0.004, enCok: 60, w: 4.4,
    tb: 31.6, sure: 1.8, olayEnCok: 7 }));
  S.koy(S.cizim({
    svg: piyano, ad: "piyano", kutu: { x: 560, y: fUst + 90, w: 440, h: fYuk - 90 }, enCok: 6, w: 4,
    tb: 32.5, sure: 0.9, olayEnCok: 4 }));
  [[600, fUst + 4, 33.0], [740, fUst - 10, 33.55],
   [880, fUst + 8, 34.1]].forEach(([x, y, tb], i) => {
    const g = S.cizim({
      svg: nota, kutu: { x, y, w: 100, h: 100 }, ad: "nota", enCok: 4, w: 4, tb, sure: 0.5,
      olayEnCok: 1, nefes: false });
    g.donusum = (f) => ({ cx: x, cy: y, tx: 0, ty: f < S.fr(tb + 0.5) ? 0 :
      6 * Math.sin((Math.min(f, ICERIK) - S.fr(tb + 0.5)) / 15 + i * 2), dondur: 0, olcek: 1 });
    S.koy(g); S.koy(S.parilti(x + 62, y + 40, tb + 0.45));
  });
  [35.4, 36.2, 36.9].forEach((t, i) =>
    S.koy(S.parilti(780 + i * 70, fUst + 130 + (i % 2) * 40, t, 24)));

  // 41,60 is ve 41,92 taking: kartta sarı halka
  S.koy(S.halka(kel("is"), 41.6, 0.3, 11, 4));
  S.koy(S.halka(kel("taking"), 41.92, 0.35, 12, 4));

  // alt formül (Fredoka 110): satır A `is + taking` (41,60–41,92) →
  // satır B `be + V-ing` (43,03–44,23)
  const yA = 1274, yB = 1382;
  const satir = (parcalar, y, boy) => {          // parcalar: [{p:[[m, renk]...], tb, ses}], ortalı
    const f = FF(boy), gen = parcalar.map((q) => q.p.reduce((t, [m]) => t + olc(f, m), 0)), bs = 26;
    let x = (1080 - gen.reduce((a, b) => a + b, 0) - bs * (parcalar.length - 1)) / 2;
    parcalar.forEach((q, i) => {
      S.koy(S.metinPop({ parca: q.p, x, y, font: f, tb: q.tb, sure: 0.3, ses: q.ses || false }));
      x += gen[i] + bs; });
  };
  satir([{ p: [["is", KREM]], tb: 41.6, ses: 0.5 }, { p: [["+", IKI]], tb: 41.76 },
    { p: [["tak", KREM], ["-ing", SARI]], tb: 41.92, ses: 0.5 }], yA, 110);
  satir([{ p: [["be", KREM]], tb: 43.03, ses: 0.5 }, { p: [["+", IKI]], tb: 44.0 },
    { p: [["V", KREM], ["-ing", SARI]], tb: 44.23, ses: 0.5 }], yB, 110);
  S.koy(S.darbeler(
    ok([130, yA - 50], [130, yB - 10], 3), { w: 8, renk: SARI, uc0: 10, uc1: 14 }, 42.7, 0.2, 0.12,
    0.5));
  S.koy(S.parilti(870, yB - 80, 44.6, 24));
}

surucu(kur, (f) => S.kare(f), KARE);

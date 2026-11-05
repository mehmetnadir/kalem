// SAHNE 05 (DİKEY 1080x1920) — Örnek 3: düz canvas, 521 kare, t_bas 47,82; cümle 5.
// Zaman yalnız kare numarasından.
// Bantlar: HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 ·
// platform boş (BRIEF-DIKEY §2).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, kutu, ok, olc } from "./sahne-ortak.js";

const KARE = 521, TBAS = 47.82, ICERIK = 509;
const KOKDIZ = "/projeler/simple-past-temel-dikey/ortak/cizim";
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5
});
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`;
// El yazısı (tegaki Caveat, dalga 5b / K26): sözcük penceresi = anlatım t0/t1 (küresel sn)
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

async function kur() {
  await S.kur();
  const [figur, top] = await Promise.all([
    svgOku("open-peeps/standing-6.svg"), svgOku("tabler/ball-football.svg")
  ]);

  // A bandı (352–476): sol daire içinde 3 (ilk 12 kare boş); sağda formül kartı 53,9'dan
  S.koy(S.daireSayi(3, 104, 414, S.zm(12)));

  // B bandı (490–740): cümle kartı, Fredoka 72, sözcük zamanlı;
  // didn't 49,27 sarı alt çizgi
  S.koy(S.darbeler(
    kutu(48, 492, 984, 250, 51), { w: 4, renk: RT.ikincil, uc0: 10, uc1: 18 },
    48.85, 0.12, 0.05, 0.5
  ));
  const cum = S.koy(S.cumleYaz({
    sozcukler: S.dizi("We", 49.11, 5), x: 92, y: 586, maxGen: 896, font: FF(72), satirH: 88
  }));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);

  // C bandı: Türkçe çeviri Caveat 64, 51,52–53,12 (pencere: 3 sözcük)
  S.koy(S.elYazisi({
    metin: "Dün futbol oynamadık.", x: 56, y: 806, boy: 64, renk: KREM,
    sozcukler: pen("Dün", 51.52, 3)
  }));

  // D bandı (830–1270): ayakta figür 440 px + futbol topu 400 px;
  // topun üstüne kırmızı çarpı (50,55)
  S.koy(S.cizim({
    svg: figur, kutu: { x: 56, y: 830, w: 250, h: 440 }, ad: "figur", esik: 0.004, enCok: 60,
    w: 4.4, tb: 49.2, sure: 1.8, olayEnCok: 7
  }));
  S.koy(S.cizim({
    svg: top, kutu: { x: 350, y: 860, w: 400, h: 400 }, ad: "top", enCok: 6, w: 4.4, tb: 49.9,
    sure: 0.9, olayEnCok: 4
  }));
  S.koy(S.darbe(
    [[385, 895], [715, 1225]],
    { duz: true, w: 14, renk: KIRMIZI, alfa: 0.92, uc0: 10, uc1: 24, tohum: 71 },
    50.55, 0.22, 0.7
  ));
  S.koy(S.darbe(
    [[715, 895], [385, 1225]],
    { duz: true, w: 14, renk: KIRMIZI, alfa: 0.92, uc0: 10, uc1: 24, tohum: 72 },
    50.8, 0.22, 0.6
  ));
  S.koy(S.parilti(740, 880, 50.1, 28));

  // 53,44–54,80 didn't sarı daire; A bandı sağ: formül didn't + V1 (Fredoka 110)
  S.koy(S.halka(kel("didn't"), 53.44, 0.3, 31, 8));
  const fo = FF(104), wA = olc(fo, "didn't"), wP = olc(fo, " + "), wV = olc(fo, "V1");
  const kx = 214, kw = 818, fy = 458, x0 = kx + (kw - (wA + wP + wV)) / 2;
  S.koy(S.kart({
    x: kx, y: 354, w: kw, h: 124, tb: 53.9, tohum: 9, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [
      { parca: [["didn't", KREM]], x: x0, y: fy, font: fo, tb: 54.32, sure: 0.3 },
      { parca: [[" + ", RT.ikincil]], x: x0 + wA, y: fy, font: fo, tb: 54.42, sure: 0.3 },
      { parca: [["V1", SARI]], x: x0 + wA + wP, y: fy, font: fo, tb: 54.52, sure: 0.3 },
    ]
  }));

  // 55,51 Did: geçmiş bayrağı (direk + flama) sağ sütunda + Caveat etiket
  const fx = 830, by = 880;
  S.koy(S.darbe(
    [[fx, by + 120], [fx - 2, by + 60], [fx + 1, by]],
    { duz: true, w: 5, renk: KREM, uc0: 4, uc1: 8, tohum: 41 },
    55.51, 0.25, 0.55
  ));
  S.koy(S.darbeler(
    [[[fx + 2, by + 2], [fx + 120, by + 28], [fx + 3, by + 58]]],
    { duz: true, w: 5, renk: SARI, uc0: 4, uc1: 8 },
    55.75, 0.3, 0.1, 0.5
  ));
  // 56,07 anlatımsız etiket `geçmiş` (zaten 56,07 · geçmişi 56,55–56,95): hedef 0,5 sn
  S.koy(S.elYazisi({
    metin: "geçmiş", x: fx + 24, y: by + 170, boy: 64, renk: KREM, tb: 56.07, sure: 0.5
  }));

  // 59,43 play sarı daire; played kırmızı çizili (59,7)
  S.koy(S.halka(kel("play"), 59.43, 0.3, 32, 8));
  const pf = FF(60), pw = olc(pf, "played"), px = 800, py = 1170;
  S.koy(S.metinPop({
    parca: [["played", RT.ikincil]], x: px, y: py, font: pf, tb: 59.7, sure: 0.3, ses: 0.5
  }));
  S.koy(S.darbe(
    [[px - 10, py - 20], [px + pw + 10, py - 24]],
    { duz: true, w: 9, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 16, tohum: 73 },
    60.0, 0.3, 0.65
  ));

  // 60,30–61,74 Soruda did başa: sarı kalem oku soru satırının başına
  // 60,60 anlatımsız etiket `did başa` (Soruda 60,30–60,78): hedef 0,5 sn → 61,10
  S.koy(S.elYazisi({
    metin: "did başa", x: 790, y: 1240, boy: 64, renk: SARI, tb: 60.6, sure: 0.5, ses: false
  }));
  S.koy(S.darbeler(
    ok([770, 1291], [60, 1291], 6), { w: 9, renk: SARI, uc0: 10, uc1: 14 },
    60.3, 0.4, 0.2, 0.55
  ));

  // E bandı: 62,87–64,23 soru cümlesi Fredoka 72
  S.koy(S.cumleYaz({
    sozcukler: S.dizi("Did", 62.87, 4), x: 56, y: 1378, maxGen: 984, font: FF(72)
  }));
}

surucu(kur, (f) => S.kare(f), KARE);

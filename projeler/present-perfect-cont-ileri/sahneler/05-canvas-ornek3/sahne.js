// SAHNE 05 (İLERİ) — Örnek 3: tuzak, durum fiili (düz canvas, 428 kare, t_bas 50,80; cümle 5; çıkış fade).
// Kök: "We have known each other since we were at primary school." Zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { yaziNoktalari } from "/projeler/present-perfect-cont-ileri/ortak/kalem-canvas.js";
import { Sahne, RT, ok, elips, kutu, olc } from "./sahne-ortak.js";

const KARE = 428, TBAS = 50.80, ICERIK = 416;
const KOKDIZ = "/projeler/present-perfect-cont-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`;

async function kur() {
  await S.kur();
  const [kisi1, kisi2, okul] = await Promise.all([svgOku("open-peeps/sitting-2.svg"),
    svgOku("open-peeps/sitting-7.svg"), svgOku("tabler/school.svg")]);

  // 51,35–52,39 daire içinde 3 + sarı TRAP etiketi (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(3, 200, 205, 51.35));
  // 51,80–52,30 `TRAP` (anlatımsız etiket, sure 0,5 sn; "Üçüncü örnek." 51,35–52,39)
  S.koy(S.elYazisi({ metin: "TRAP", x: 290, y: 236, boy: 84, renk: SARI, tb: 51.80, sure: 0.5,
    ses: 0.6 }));
  S.koy(S.darbe([[288, 262], [380, 256], [470, 262]], { w: 7, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14, tohum: 91 },
    52.25, 0.4, 0.5));

  // 52,64–55,76 İngilizce kök (Fredoka 64, sözcük zamanlı, 3 satır: 4 / 4 / 3 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("We", 52.64, 11), x: 140, y: 340, maxGen: 840, font: FF(64),
    satirH: 86, satirSay: [4, 4, 3], bosluk: 4 }));
  const kel = (i) => cum.kel[i];      // 0 We 1 have 2 known 3 each | 4 other 5 since 6 we 7 were | 8 at 9 primary 10 school.
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));

  // 53,04 known: sarı daire; altında Caveat `have known` + `have been knowing` değil
  S.koy(S.halka(kel(2), 53.04, 0.3, 31, 8));
  const yN = sonSatir + 86;
  // 53,27–53,71 `have known` (sure 0,5 sn) · 54,20–55,07 `have been knowing değil` (sure 0,8 sn);
  // el yazısı, ikincisinin x'i birincinin tegaki genişliğinden (w) gelir
  const hk = S.koy(S.elYazisi({ metin: "have known", x: 140, y: yN, boy: 64, renk: SARI, tb: 53.27,
    sure: 0.5 }));
  S.koy(S.elYazisi({ metin: "have been knowing değil", x: 140 + hk.w + 36, y: yN, boy: 52,
    renk: IKINCIL, tb: 54.20, sure: 0.8 }));

  // sağ sahne (52,60–55,80): iki figür + okul (380 px) kalemle
  S.koy(S.cizim({ svg: kisi1, ad: "kisi1", kutu: { x: 1010, y: 190, w: 300, h: 420 }, esik: 0.004, enCok: 60, w: 3.4,
    tb: 52.72, sure: 1.6, olayEnCok: 6 }));
  S.koy(S.cizim({ svg: kisi2, ad: "kisi2", kutu: { x: 1290, y: 190, w: 300, h: 420 }, esik: 0.004, enCok: 60, w: 3.4,
    tb: 53.80, sure: 1.6, olayEnCok: 6 }));
  S.koy(S.cizim({ svg: okul, ad: "okul", kutu: { x: 1500, y: 120, w: 340, h: 340 }, enCok: 14, w: 4, tb: 54.98,
    sure: 0.9, olayEnCok: 4 }));
  S.koy(S.darbe([[1010, 612], [1400, 616], [1850, 611]], { duz: true, w: 3.4, renk: IKINCIL, alfa: 0.8, uc0: 6,
    uc1: 10, tohum: 77 }, 54.64, 0.5, 0.45));
  S.koy(S.parilti(1790, 130, 55.61, 24));

  // 55,93–58,65 Türkçe çeviri (Caveat 48 ikincil)
  const yTR = yN + 70;
  // el yazısı, her sözcük kendi penceresinde (İlkokuldan 55,93 … tanıyoruz. 57,45–58,65);
  // beri 0,16 sn → birbirimizi başına dek uzatıldı
  const trSoz = S.dizi("İlkokuldan", 55.93, 4);
  S.koy(S.elYazisi({ metin: "İlkokuldan beri birbirimizi tanıyoruz.", x: 140, y: yTR, boy: 52,
    renk: IKINCIL, sozcukler: trSoz.map((w, i) => ({ t0: w.t0,
      t1: w.t1 - w.t0 < 0.2 && trSoz[i + 1] ? trSoz[i + 1].t0 : w.t1 })) }));

  // 58,90–61,14 STATE VERB kartı: know-ing yazılır, kırmızı tek çizgiyle üstü çizilir
  const ky = yTR + 56, kh = 250;
  S.koy(S.darbeler(kutu(140, ky, 720, kh, 61), { w: 4, renk: KREM, uc0: 8, uc1: 14 }, 58.90, 0.12, 0.08, 0.5));
  S.koy(S.metinPop({ parca: [["know", KREM]], x: 190, y: ky + 186, font: FF(120), tb: 58.98, sure: 0.35, ses: 0.6 }));
  const kw = olc(FF(120), "know");
  S.koy(S.metinPop({ parca: [["-ing", SARI]], x: 190 + kw, y: ky + 186, font: FF(120), tb: 59.58, sure: 0.35, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["STATE VERB", SARI]], x: 190, y: ky + 82, font: FF(56), tb: 59.86, sure: 0.4, ses: 0.6 }));
  const iw = olc(FF(120), "-ing");
  S.koy(S.darbe([[176, ky + 164], [190 + (kw + iw) / 2, ky + 154], [204 + kw + iw, ky + 144]],
    { w: 10, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 14, tohum: 93 }, 60.36, 0.35, 0.7));

  // 61,39–64,59 Caveat `durum fiili: genellikle -ing yok` (16.11 DUZ3: ses "Durum anlatan fiiller genellikle
  // -ing almaz."; eski mutlak `-ing yok`); Present Perfect etiketi tik. Dört parça dört çağrı; x'ler tegaki
  // genişliğinden (önek = tam metin − parça), sağ uç 930 + 712 = 1642. `durum fiili:` Durum 61,39 · anlatan
  // fiiller 61,71–62,67 · `genellikle` 62,83 · `-ing` 63,55–63,79 · `yok` "almaz." 63,87–64,67
  const gx = (str) => yaziNoktalari(str, S.EY.G, { upm: S.EY.M.unitsPerEm, asc: S.EY.M.ascender,
    boy: 72, x: 0, taban: 0 }).gen;
  const pn = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));
  const d3 = pn("Durum", 61.39, 3), dz = [d3[0], { t0: d3[1].t0, t1: d3[2].t1 }];
  const gn = pn("genellikle", 62.83, 1), ing = pn("-ing", 63.55, 1), alm = pn("almaz.", 63.87, 1);
  const yd = ky + 100, TAM = "durum fiili: genellikle -ing yok";
  S.koy(S.elYazisi({ metin: "durum fiili:", x: 930, y: yd, boy: 72, renk: KREM, sozcukler: dz }));
  S.koy(S.elYazisi({ metin: "genellikle", x: 930 + gx("durum fiili: genellikle") - gx("genellikle"), y: yd,
    boy: 72, renk: KREM, sozcukler: gn }));
  S.koy(S.elYazisi({ metin: "-ing", x: 930 + gx("durum fiili: genellikle -ing") - gx("-ing"), y: yd, boy: 72,
    renk: SARI, sozcukler: ing }));
  S.koy(S.elYazisi({ metin: "yok", x: 930 + gx(TAM) - gx("yok"), y: yd, boy: 72,
    renk: KREM, sozcukler: alm }));
  S.koy(S.darbeler(ok([1010, ky + 140], [960, ky + 112], 5), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 62.19, 0.16,
    0.12, 0.5));
  const px = 930, py = ky + 150;
  S.koy(S.darbeler(kutu(px, py, 700, 100, 63), { w: 3.6, renk: KREM, uc0: 8, uc1: 14 }, 62.9, 0.1, 0.07, 0.4));
  S.koy(S.metinPop({ parca: [["Present Perfect", KREM]], x: px + 32, y: py + 70, font: FF(58), tb: 63.05, sure: 0.35,
    ses: 0.5 }));
  S.koy(S.darbe([[px + 620, py + 54], [px + 646, py + 78], [px + 692, py + 20]], { w: 9, renk: SARI, alfa: 0.9,
    uc0: 4, uc1: 10, tohum: 95 }, 63.9, 0.3, 0.55));
}

surucu(kur, (f) => S.kare(f), KARE);

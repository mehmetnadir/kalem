// SAHNE 05 (İLERİ) — Örnek 3: tuzak, durum fiili (düz canvas, 392 kare, t_bas 49,20; cümle 5; çıkış fade).
// Kök: "We have known each other since we were at primary school." Zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, elips, kutu, olc } from "./sahne-ortak.js";

const KARE = 392, TBAS = 49.20, ICERIK = 380;
const KOKDIZ = "/projeler/present-perfect-cont-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const [kisi1, kisi2, okul] = await Promise.all([svgOku("open-peeps/sitting-2.svg"),
    svgOku("open-peeps/sitting-7.svg"), svgOku("tabler/school.svg")]);

  // 49,75–50,79 daire içinde 3 + sarı TRAP etiketi (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(3, 200, 205, 49.75));
  S.koy(S.not({ parca: [["TRAP", SARI]], x: 290, y: 236, font: CV(84), tb: 50.2, sure: 0.5, ses: 0.6 }));
  S.koy(S.darbe([[288, 262], [380, 256], [470, 262]], { w: 7, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14, tohum: 91 },
    50.65, 0.4, 0.5));

  // 51,04–54,16 İngilizce kök (Fredoka 64, sözcük zamanlı, 3 satır: 4 / 4 / 3 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("We", 51.04, 11), x: 140, y: 340, maxGen: 840, font: FF(64),
    satirH: 86, satirSay: [4, 4, 3], bosluk: 4 }));
  const kel = (i) => cum.kel[i];      // 0 We 1 have 2 known 3 each | 4 other 5 since 6 we 7 were | 8 at 9 primary 10 school.
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));

  // 51,44 known: sarı daire; altında Caveat `have known` + `have been knowing` değil
  S.koy(S.halka(kel(2), 51.44, 0.3, 31, 8));
  const yN = sonSatir + 86;
  S.koy(S.not({ parca: [["have known", SARI]], x: 140, y: yN, font: CV(64), tb: 51.7, sure: 0.5 }));
  const wN = olc(CV(64), "have known");
  S.koy(S.not({ parca: [["have been knowing değil", IKINCIL]], x: 140 + wN + 36, y: yN, font: CV(52), tb: 52.6,
    sure: 0.9 }));

  // sağ sahne (51,0–54,2): iki figür + okul (380 px) kalemle
  S.koy(S.cizim({ svg: kisi1, ad: "kisi1", kutu: { x: 1010, y: 190, w: 300, h: 420 }, esik: 0.004, enCok: 60, w: 3.4,
    tb: 51.2, sure: 1.6, olayEnCok: 6 }));
  S.koy(S.cizim({ svg: kisi2, ad: "kisi2", kutu: { x: 1290, y: 190, w: 300, h: 420 }, esik: 0.004, enCok: 60, w: 3.4,
    tb: 52.3, sure: 1.6, olayEnCok: 6 }));
  S.koy(S.cizim({ svg: okul, ad: "okul", kutu: { x: 1500, y: 120, w: 340, h: 340 }, enCok: 14, w: 4, tb: 53.3,
    sure: 0.9, olayEnCok: 4 }));
  S.koy(S.darbe([[1010, 612], [1400, 616], [1850, 611]], { duz: true, w: 3.4, renk: IKINCIL, alfa: 0.8, uc0: 6,
    uc1: 10, tohum: 77 }, 53.0, 0.5, 0.45));
  S.koy(S.parilti(1790, 130, 54.0, 24));

  // 54,33–56,97 Türkçe çeviri (Caveat 48 ikincil)
  const yTR = yN + 70;
  S.koy(S.not({ parca: [["İlkokuldan beri birbirimizi tanıyoruz.", IKINCIL]], x: 140, y: yTR, font: CV(52),
    tb: 54.33, sure: 2.4 }));

  // 57,22–59,38 STATE VERB kartı: know-ing yazılır, kırmızı tek çizgiyle üstü çizilir
  const ky = yTR + 56, kh = 250;
  S.koy(S.darbeler(kutu(140, ky, 720, kh, 61), { w: 4, renk: KREM, uc0: 8, uc1: 14 }, 57.22, 0.12, 0.08, 0.5));
  S.koy(S.metinPop({ parca: [["know", KREM]], x: 190, y: ky + 186, font: FF(120), tb: 57.3, sure: 0.35, ses: 0.6 }));
  const kw = olc(FF(120), "know");
  S.koy(S.metinPop({ parca: [["-ing", SARI]], x: 190 + kw, y: ky + 186, font: FF(120), tb: 57.9, sure: 0.35, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["STATE VERB", SARI]], x: 190, y: ky + 82, font: FF(56), tb: 58.3, sure: 0.4, ses: 0.6 }));
  const iw = olc(FF(120), "-ing");
  S.koy(S.darbe([[176, ky + 164], [190 + (kw + iw) / 2, ky + 154], [204 + kw + iw, ky + 144]],
    { w: 10, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 14, tohum: 93 }, 58.78, 0.35, 0.7));

  // 59,63–61,87 Caveat `durum fiili: -ing yok`; Present Perfect etiketi tik
  S.koy(S.not({ parca: [["durum fiili: ", KREM], ["-ing", SARI], [" yok", KREM]], x: 930, y: ky + 100, font: CV(72),
    tb: 59.63, sure: 0.8 }));
  S.koy(S.darbeler(ok([1010, ky + 140], [960, ky + 112], 5), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 59.9, 0.16,
    0.12, 0.5));
  const px = 930, py = ky + 150;
  S.koy(S.darbeler(kutu(px, py, 700, 100, 63), { w: 3.6, renk: KREM, uc0: 8, uc1: 14 }, 60.67, 0.1, 0.07, 0.4));
  S.koy(S.metinPop({ parca: [["Present Perfect", KREM]], x: px + 32, y: py + 70, font: FF(58), tb: 60.8, sure: 0.35,
    ses: 0.5 }));
  S.koy(S.darbe([[px + 620, py + 54], [px + 646, py + 78], [px + 692, py + 20]], { w: 9, renk: SARI, alfa: 0.9,
    uc0: 4, uc1: 10, tohum: 95 }, 61.1, 0.3, 0.55));
}

surucu(kur, (f) => S.kare(f), KARE);

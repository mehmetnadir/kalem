// SAHNE 05 (İLERİ, DİKEY 1080x1920) — Örnek 3: tuzak, durum fiili (düz canvas, 392 kare, t_bas 49,20; cümle 5; fade).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (sahne-ortak.js çizer), platform boş. Telefon ölçeği: yazı >= 64 px.
// Üstten alta: kart (372–650) · not satırı (735) · sahne: iki figür + okul (770–1198, 56,9'da sola alta toplanır) ·
// Türkçe çeviri (sağ alt) · 57,2'de STATE VERB kartı (790–1160).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, elips, kutu, olc } from "./sahne-ortak.js";

const KARE = 392, TBAS = 49.20, ICERIK = 380;
const KOKDIZ = "/projeler/present-perfect-cont-ileri-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`;
// El yazısı (tegaki Caveat, dalga 5b-2 / K26): sözcük penceresi = anlatım t0/t1 (küresel sn)
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

async function kur() {
  await S.kur();
  const [kisi1, kisi2, okul] = await Promise.all([svgOku("open-peeps/sitting-2.svg"),
    svgOku("open-peeps/sitting-7.svg"), svgOku("tabler/school.svg")]);

  // kart çerçevesi (el kutusu) + sağ üst köşede daire içinde 3; ilk 12 kare boş (künye hazır, tuval boş)
  S.koy(S.darbeler(kutu(48, 372, 984, 278, 5), { w: 4.2, renk: RT.ikincil, uc0: 10, uc1: 18 }, 49.62, 0.2, 0.14,
    0.55));
  S.koy(S.darbe(elips(962, 442, 46, 44, 0.1, 5), { w: 5, uc0: 18, uc1: 34 }, 49.75, 0.55, 0.6));
  S.koy(S.metinPop({ parca: [["3", KREM]], x: 962, y: 474, font: FF(78), hiza: "orta", tb: 50.05, sure: 0.35,
    olcek0: 0.7, ses: 0.8, turu: "vurus" }));
  // 50,2 sarı TRAP etiketi (kartın sağ alt köşesi)
  // anlatımsız etiket `TRAP`: hedef 0,45 sn → 50,65 (alt çizgi 50,65'te başlar; sağ uç 954)
  S.koy(S.elYazisi({ metin: "TRAP", x: 780, y: 622, boy: 88, renk: SARI, tb: 50.2, sure: 0.45,
    ses: 0.6 }));
  S.koy(S.darbe([[772, 636], [880, 630], [1000, 637]], { w: 9, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14, tohum: 91 },
    50.65, 0.4, 0.5));

  // 51,04–54,16 İngilizce kök (Fredoka 64, sözcük zamanlı; 3 satır 4 / 4 / 3 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("We", 51.04, 11), x: 88, y: 440, maxGen: 904, font: FF(64),
    satirH: 76, satirSay: [4, 4, 3], bosluk: 4 }));
  const kel = (i) => cum.kel[i];      // 0 We 1 have 2 known 3 each | 4 other 5 since 6 we 7 were | 8 at 9 primary 10 school.
  S.koy(S.halka(kel(2), 51.44, 0.3, 31, 8));           // known (51,44–51,60)

  // 51,7 not satırı: `have known` (sarı) + `have been knowing değil`
  // anlatımsız etiketler: `have known` 51,70 → 52,20 · `have been knowing değil` 52,60 → 53,40
  // (hedef 0,8 sn; x tegaki genişliğinden: 64 + 292 + 34 = 390, sağ uç 918)
  const nHK = S.elYazisi({ metin: "have known", x: 64, y: 735, boy: 72, renk: SARI, tb: 51.7,
    sure: 0.5 });
  S.koy(nHK);
  S.koy(S.elYazisi({ metin: "have been knowing değil", x: 64 + nHK.w + 34, y: 735, boy: 64,
    renk: KREM, tb: 52.6, sure: 0.8 }));

  // 51,2–54,2 sahne (770–1198): iki oturan figür (420 px) + okul; 56,9'da sola alta toplanır
  const sahne = [];
  sahne.push(S.cizim({ svg: kisi1, ad: "kisi1", kutu: { x: 60, y: 770, w: 290, h: 420 }, esik: 0.004, enCok: 60,
    w: 4.4, tb: 51.2, sure: 1.6, olayEnCok: 6 }));
  sahne.push(S.cizim({ svg: kisi2, ad: "kisi2", kutu: { x: 350, y: 770, w: 250, h: 420 }, esik: 0.004, enCok: 60,
    w: 4.4, tb: 52.3, sure: 1.6, olayEnCok: 6 }));
  sahne.push(S.cizim({ svg: okul, ad: "okul", kutu: { x: 650, y: 820, w: 380, h: 370 }, enCok: 14, w: 4.4, tb: 53.3,
    sure: 0.9, olayEnCok: 4 }));
  sahne.push(S.darbe([[48, 1198], [540, 1202], [1032, 1197]], { duz: true, w: 4, renk: RT.ikincil, alfa: 0.8, uc0: 6,
    uc1: 10, tohum: 77 }, 53.0, 0.5, 0.45));
  S.koy(S.grup(sahne, { f0: S.fr(56.9), f1: S.fr(57.6), ax: 48, ay: 770, olcek: 0.4, dy: 450 }));
  S.koy(S.parilti(980, 800, 54.0, 28));

  // 54,33–56,97 Türkçe çeviri (Caveat 64, mürekkep; sağ alt, 3 satır)
  // pencere: İlkokuldan 54,33–54,97 · beri 55,05–55,29 (0,16 sn → birbirimizi başına uzatıldı) ·
  // birbirimizi 55,29–55,77 · tanıyoruz. 55,85–56,97; sağ uç 887
  const bb = pen("beri", 55.05, 2);
  bb[0].t1 = bb[1].t0;
  [["İlkokuldan", 1250, pen("İlkokuldan", 54.33, 1)], ["beri birbirimizi", 1310, bb],
    ["tanıyoruz.", 1370, pen("tanıyoruz.", 55.85, 1)]].forEach(([m, y, sozcukler]) =>
    S.koy(S.elYazisi({ metin: m, x: 560, y, boy: 64, renk: KREM, sozcukler })));

  // 57,22–59,38 STATE VERB kartı: `know` + `-ing` yazılır, kırmızı tek çizgiyle üstü çizilir
  const ky = 790;
  S.koy(S.darbeler(kutu(48, ky, 984, 370, 61), { w: 4.2, renk: KREM, uc0: 8, uc1: 14 }, 57.22, 0.12, 0.08, 0.5));
  S.koy(S.metinPop({ parca: [["know", KREM]], x: 88, y: ky + 290, font: FF(150), tb: 57.3, sure: 0.35, ses: 0.6 }));
  const kw = olc(FF(150), "know"), iw = olc(FF(150), "-ing");
  S.koy(S.metinPop({ parca: [["-ing", SARI]], x: 88 + kw, y: ky + 290, font: FF(150), tb: 57.9, sure: 0.35,
    ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["STATE VERB", SARI]], x: 88, y: ky + 100, font: FF(64), tb: 58.3, sure: 0.4,
    ses: 0.6 }));
  S.koy(S.darbe([[66, ky + 240], [88 + (kw + iw) / 2, ky + 222], [112 + kw + iw, ky + 205]],
    { w: 12, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 14, tohum: 93 }, 58.78, 0.35, 0.7));

  // 59,63–61,87 `durum fiili: -ing yok`; Present Perfect etiketi tik
  const nx = Math.max(88 + kw + iw + 50, 730);
  // `durum fiili:` penceresi: Durum 59,63–59,95 · fiili 60,03–60,43 (x 730, sağ uç 963)
  S.koy(S.elYazisi({ metin: "durum fiili:", x: nx, y: ky + 235, boy: 64, renk: KREM,
    sozcukler: pen("Durum", 59.63, 2) }));
  // `-ing yok` anlatımsız (eski belirme 60,20): `-ing` 60,20 → 60,50 · `yok` → 60,80; sağ uç 901
  const nIng = S.elYazisi({ metin: "-ing", x: nx, y: ky + 305, boy: 64, renk: SARI, tb: 60.2,
    sure: 0.3 });
  S.koy(nIng);
  S.koy(S.elYazisi({ metin: "yok", x: nx + nIng.w + 16, y: ky + 305, boy: 64, renk: KREM, tb: 60.5,
    sure: 0.3 }));
  S.koy(S.darbeler(kutu(540, ky + 26, 460, 90, 63), { w: 4, renk: KREM, uc0: 8, uc1: 14 }, 60.67, 0.1, 0.07, 0.4));
  S.koy(S.metinPop({ parca: [["Present Perfect", KREM]], x: 568, y: ky + 88, font: FF(48), tb: 60.8, sure: 0.35,
    ses: 0.5 }));
  S.koy(S.darbe([[930, ky + 56], [948, ky + 78], [986, ky + 32]], { w: 10, renk: SARI, alfa: 0.9,
    uc0: 4, uc1: 10, tohum: 95 }, 61.1, 0.3, 0.55));
}

surucu(kur, (f) => S.kare(f), KARE);

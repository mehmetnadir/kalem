// SAHNE 05 (İLERİ, DİKEY 1080x1920) — Örnek 3: tuzak, durum fiili (düz canvas, 428 kare, t_bas 50,80; cümle 5; fade).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (sahne-ortak.js çizer), platform boş. Telefon ölçeği: yazı >= 64 px.
// Üstten alta: kart (372–650) · not satırı (735) · sahne: iki figür + okul (770–1198, 58,57'de sola alta toplanır) ·
// Türkçe çeviri (sağ alt) · 58,88'de STATE VERB kartı (790–1160).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, ok, elips, kutu, olc } from "./sahne-ortak.js";

const KARE = 428, TBAS = 50.80, ICERIK = 416;
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
  S.koy(S.darbeler(kutu(48, 372, 984, 278, 5), { w: 4.2, renk: RT.ikincil, uc0: 10, uc1: 18 }, 51.22, 0.2, 0.14,
    0.55));
  S.koy(S.darbe(elips(962, 442, 46, 44, 0.1, 5), { w: 5, uc0: 18, uc1: 34 }, 51.35, 0.55, 0.6));
  S.koy(S.metinPop({ parca: [["3", KREM]], x: 962, y: 474, font: FF(78), hiza: "orta", tb: 51.65, sure: 0.35,
    olcek0: 0.7, ses: 0.8, turu: "vurus" }));
  // 51,80 sarı TRAP etiketi (kartın sağ alt köşesi)
  // anlatımsız etiket `TRAP`: hedef 0,45 sn → 52,25 (alt çizgi 52,25'te başlar; sağ uç 954)
  S.koy(S.elYazisi({ metin: "TRAP", x: 780, y: 622, boy: 88, renk: SARI, tb: 51.80, sure: 0.45,
    ses: 0.6 }));
  S.koy(S.darbe([[772, 636], [880, 630], [1000, 637]], { w: 9, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14, tohum: 91 },
    52.25, 0.4, 0.5));

  // 52,64–55,76 İngilizce kök (Fredoka 64, sözcük zamanlı; 3 satır 4 / 4 / 3 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("We", 52.64, 11), x: 88, y: 440, maxGen: 904, font: FF(64),
    satirH: 76, satirSay: [4, 4, 3], bosluk: 4 }));
  const kel = (i) => cum.kel[i];      // 0 We 1 have 2 known 3 each | 4 other 5 since 6 we 7 were | 8 at 9 primary 10 school.
  S.koy(S.halka(kel(2), 53.04, 0.3, 31, 8));           // known (53,04–53,20)

  // 53,27 not satırı: `have known` (sarı) + `have been knowing değil`
  // anlatımsız etiketler: `have known` 53,27 → 53,71 · `have been knowing değil` 54,20 → 55,07
  // (hedef 0,8 sn; x tegaki genişliğinden: 64 + 292 + 34 = 390, sağ uç 918)
  const nHK = S.elYazisi({ metin: "have known", x: 64, y: 735, boy: 72, renk: SARI, tb: 53.27,
    sure: 0.5 });
  S.koy(nHK);
  S.koy(S.elYazisi({ metin: "have been knowing değil", x: 64 + nHK.w + 34, y: 735, boy: 64,
    renk: KREM, tb: 54.20, sure: 0.8 }));

  // 52,72–55,80 sahne (770–1198): iki oturan figür (420 px) + okul; 58,57'de sola alta toplanır
  const sahne = [];
  sahne.push(S.cizim({ svg: kisi1, ad: "kisi1", kutu: { x: 60, y: 770, w: 290, h: 420 }, esik: 0.004, enCok: 60,
    w: 4.4, tb: 52.72, sure: 1.6, olayEnCok: 6 }));
  sahne.push(S.cizim({ svg: kisi2, ad: "kisi2", kutu: { x: 350, y: 770, w: 250, h: 420 }, esik: 0.004, enCok: 60,
    w: 4.4, tb: 53.80, sure: 1.6, olayEnCok: 6 }));
  sahne.push(S.cizim({ svg: okul, ad: "okul", kutu: { x: 650, y: 820, w: 380, h: 370 }, enCok: 14, w: 4.4, tb: 54.98,
    sure: 0.9, olayEnCok: 4 }));
  sahne.push(S.darbe([[48, 1198], [540, 1202], [1032, 1197]], { duz: true, w: 4, renk: RT.ikincil, alfa: 0.8, uc0: 6,
    uc1: 10, tohum: 77 }, 54.64, 0.5, 0.45));
  S.koy(S.grup(sahne, { f0: S.fr(58.57), f1: S.fr(59.28), ax: 48, ay: 770, olcek: 0.4, dy: 450 }));
  S.koy(S.parilti(980, 800, 55.61, 28));

  // 55,93–58,65 Türkçe çeviri (Caveat 64, mürekkep; sağ alt, 3 satır)
  // pencere: İlkokuldan 55,93–56,57 · beri 56,65–56,89 (0,16 sn → birbirimizi başına uzatıldı) ·
  // birbirimizi 56,89–57,37 · tanıyoruz. 57,45–58,65; sağ uç 887
  const bb = pen("beri", 56.65, 2);
  bb[0].t1 = bb[1].t0;
  [["İlkokuldan", 1250, pen("İlkokuldan", 55.93, 1)], ["beri birbirimizi", 1310, bb],
    ["tanıyoruz.", 1370, pen("tanıyoruz.", 57.45, 1)]].forEach(([m, y, sozcukler]) =>
    S.koy(S.elYazisi({ metin: m, x: 560, y, boy: 64, renk: KREM, sozcukler })));

  // 58,90–61,14 STATE VERB kartı: `know` + `-ing` yazılır, kırmızı tek çizgiyle üstü çizilir
  const ky = 790;
  S.koy(S.darbeler(kutu(48, ky, 984, 370, 61), { w: 4.2, renk: KREM, uc0: 8, uc1: 14 }, 58.90, 0.12, 0.08, 0.5));
  S.koy(S.metinPop({ parca: [["know", KREM]], x: 88, y: ky + 290, font: FF(150), tb: 58.98, sure: 0.35, ses: 0.6 }));
  const kw = olc(FF(150), "know"), iw = olc(FF(150), "-ing");
  S.koy(S.metinPop({ parca: [["-ing", SARI]], x: 88 + kw, y: ky + 290, font: FF(150), tb: 59.58, sure: 0.35,
    ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["STATE VERB", SARI]], x: 88, y: ky + 100, font: FF(64), tb: 59.86, sure: 0.4,
    ses: 0.6 }));
  S.koy(S.darbe([[66, ky + 240], [88 + (kw + iw) / 2, ky + 222], [112 + kw + iw, ky + 205]],
    { w: 12, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 14, tohum: 93 }, 60.36, 0.35, 0.7));

  // 61,39–64,59 `durum fiili: / genellikle / -ing yok` (3 satır; 16.11 DUZ3: ses "Durum anlatan fiiller genellikle
  // -ing almaz.", eski mutlak `-ing yok`); Present Perfect etiketi tik. Satırlar ky+180/250/320 (70 px aralık; kutu altı 906'dan 16 px).
  const nx = Math.max(88 + kw + iw + 50, 730);
  // pencere: Durum 61,39–61,63 · anlatan fiiller 61,71–62,67 (x 730, sağ uç 963) · genellikle 62,83–63,47 (sağ uç 917)
  const d3 = pen("Durum", 61.39, 3);
  S.koy(S.elYazisi({ metin: "durum fiili:", x: nx, y: ky + 180, boy: 64, renk: KREM,
    sozcukler: [d3[0], { t0: d3[1].t0, t1: d3[2].t1 }] }));
  S.koy(S.elYazisi({ metin: "genellikle", x: nx, y: ky + 250, boy: 64, renk: KREM, sozcukler: pen("genellikle", 62.83, 1) }));
  // `-ing` 63,55–63,79 · `yok` "almaz." 63,87–64,67; sağ uç 904
  const nIng = S.elYazisi({ metin: "-ing", x: nx, y: ky + 320, boy: 64, renk: SARI, sozcukler: pen("-ing", 63.55, 1) });
  S.koy(nIng);
  S.koy(S.elYazisi({ metin: "yok", x: nx + nIng.w + 16, y: ky + 320, boy: 64, renk: KREM, sozcukler: pen("almaz.", 63.87, 1) }));
  S.koy(S.darbeler(kutu(540, ky + 26, 460, 90, 63), { w: 4, renk: KREM, uc0: 8, uc1: 14 }, 62.9, 0.1, 0.07, 0.4));
  S.koy(S.metinPop({ parca: [["Present Perfect", KREM]], x: 568, y: ky + 88, font: FF(48), tb: 63.05, sure: 0.35,
    ses: 0.5 }));
  S.koy(S.darbe([[930, ky + 56], [948, ky + 78], [986, ky + 32]], { w: 10, renk: SARI, alfa: 0.9,
    uc0: 4, uc1: 10, tohum: 95 }, 63.9, 0.3, 0.55));
}

surucu(kur, (f) => S.kare(f), KARE);

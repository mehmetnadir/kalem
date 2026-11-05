// SAHNE 05 (SIMPLE PAST İLERİ, DİKEY 1080x1920) — Örnek 3, asıl tuzak (düz canvas, 528 kare, t_bas 48,99; cümle 5).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (sahne-ortak.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: TRAP satırı (360–490) · kart (500–830, 3 satır) · satır A takvim (860–1120) · satır B saat (1150–1390).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 528, TBAS = 48.99, ICERIK = 516;
const KOKDIZ = "/projeler/simple-past-ileri-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIR = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const [takvim, saat] = await Promise.all([svgOku("tabler/calendar.svg"), svgOku("tabler/clock.svg")]);

  // 49,35: kart çerçevesi + daire içinde 3 (ilk 12 kare boş) · TRAP Fredoka 150 kırmızı, vuruş 50,51
  S.koy(S.daireSayi(3, 120, 420, 49.35));
  S.koy(S.metinPop({ parca: [["TRAP", KIR]], x: 230, y: 472, font: FF(150), tb: 50.4, sure: 0.45, olcek0: 0.6,
    ses: 0.9, turu: "vurus" }));
  S.koy(S.darbeler(kutu(48, 508, 984, 322, 5), { w: 4.2, renk: IKINCIL, uc0: 10, uc1: 18 }, 51.0, 0.2, 0.14, 0.55));

  // 51,32–55,64 İngilizce cümle (Fredoka 64, 3 satır: 5 / 6 / 4 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("The", 51.32, 15), x: 88, y: 592, maxGen: 920,
    font: FF(64), satirH: 100, satirSay: [4, 6, 5], bosluk: 3 }));
  const kel = (i) => cum.kel[i]; // satır 1: 0 The … 3 two | 4 weeks … 9 has | 10 not … 14 yet.
  const altSari = (k, tb, tohum) => S.koy(S.darbe(altCizgi(k.x - 4, k.x + k.w + 4, k.y + 24, tohum),
    { w: 9, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 500 + tohum }, tb, 0.4, 0.55));
  altSari(kel(5), 52.92, 1);     // ago
  altSari(kel(14), 55.32, 2);    // yet

  // 56,45–59,81 satır A: takvim + kapalı nokta; resigned ve ago sarı daire; etiket Simple Past
  S.koy(S.halka(kel(2), 56.45, 0.35, 11));
  S.koy(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 60, y: 870, w: 250, h: 250 }, enCok: 8, w: 4.4,
    tb: 56.6, sure: 0.8, olayEnCok: 4 }));
  S.koy(S.halka(kel(5), 57.65, 0.35, 13));
  S.koy(S.darbe(elips(338, 922, 12, 12, 0, 3), { w: 22, renk: KREM, alfa: 0.95, uc0: 4, uc1: 4 }, 57.5, 0.15, 0.6));
  // 57,90 anlatımsız etiket `two weeks ago` (Caveat 72; sağ uç 732): hedef 0,8 sn → 58,70
  S.koy(S.elYazisi({ metin: "two weeks ago", x: 380, y: 945, boy: 72, renk: KREM, tb: 57.9,
    sure: 0.8 }));
  S.koy(S.darbeler(ok([420, 975], [420, 1020], 15), { w: 8, renk: SARI, uc0: 10, uc1: 14 }, 59.1, 0.25, 0.12, 0.5));
  S.koy(S.metinPop({ parca: [["Simple Past", SARI]], x: 370, y: 1100, font: FF(88), tb: 59.49, sure: 0.4,
    ses: 0.8, turu: "vurus" }));

  // 60,84–65,32 satır B: saat + ok → now; has not found ve yet sarı daire; etiket Present Perfect
  S.koy(S.halka(kel(9), 60.84, 0.3, 21));     // has
  S.koy(S.halka(kel(10), 61.0, 0.3, 22));     // not
  S.koy(S.halka(kel(11), 61.16, 0.3, 23));    // found
  S.koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 60, y: 1150, w: 240, h: 240 }, enCok: 6, w: 4.4,
    tb: 61.0, sure: 0.8, olayEnCok: 4 }));
  // 62,00 anlatımsız etiket `yet = belirsiz` (sağ uç 689): hedef 0,8 sn → 62,80
  S.koy(S.elYazisi({ metin: "yet = belirsiz", x: 370, y: 1215, boy: 72, renk: KREM, tb: 62.0,
    sure: 0.8 }));
  S.koy(S.halka(kel(14), 62.6, 0.35, 19));
  S.koy(S.darbeler(ok([830, 1190], [980, 1190], 17), { w: 8, renk: SARI, uc0: 10, uc1: 14 }, 63.3, 0.3, 0.15, 0.5));
  // 63,50 anlatımsız etiket `now` (sağ uç 986): hedef 0,45 sn → 63,95
  S.koy(S.elYazisi({ metin: "now", x: 900, y: 1170, boy: 64, renk: KREM, tb: 63.5, sure: 0.45 }));
  const fPP = FF(80);
  S.koy(S.darbeler(ok([420, 1245], [420, 1285], 25), { w: 8, renk: SARI, uc0: 10, uc1: 14 }, 64.5, 0.25, 0.12, 0.5));
  S.koy(S.metinPop({ parca: [["Present Perfect", SARI]], x: 370, y: 1355, font: fPP, tb: 64.76, sure: 0.4,
    ses: 0.8, turu: "vurus" }));
  S.koy(S.parilti(960, 1300, 65.0, 28));
}

surucu(kur, (f) => S.kare(f), KARE);

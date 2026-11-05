// SAHNE 05 (SIMPLE PAST İLERİ) — Örnek 3, asıl tuzak (düz canvas, 528 kare, t_bas 48,99; cümle 5;
// çıkış fade).
// Kök: "The manager resigned two weeks ago, and the board has not found a replacement yet."
// Zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json (küresel sn).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, altCizgi } from "./sahne-ortak.js";

const KARE = 528, TBAS = 48.99, ICERIK = 516;
const KOKDIZ = "/projeler/simple-past-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIR = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`;

async function kur() {
  await S.kur();
  const [takvim, saat] = await Promise.all([svgOku("tabler/calendar.svg"),
    svgOku("tabler/clock.svg")]);

  // 49,35: daire içinde 3 (ilk 12 kare boş) + TRAP (vuruş 50,51)
  S.koy(S.daireSayi(3, 200, 190, 49.35));
  S.koy(S.metinPop({ parca: [["TRAP", KIR]], x: 310, y: 228, font: FF(110), tb: 50.4, sure: 0.45,
    olcek0: 0.6,
    ses: 0.9, turu: "vurus" }));

  // 51,32–55,64 İngilizce cümle (Fredoka 56, 2 satır: 6 / 9 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("The", 51.32, 15), x: 140, y: 355, maxGen: 1640,
    font: FF(56), satirH: 112, satirSay: [6, 9], bosluk: 6 }));
  // 0 The … 2 resigned · 5 ago, | 6 and … 9 has · 10 not · 11 found · 14 yet.
  const kel = (i) => cum.kel[i];
  const altSari = (k, tb, tohum) => S.koy(S.darbe(altCizgi(k.x - 4, k.x + k.w + 4, k.y + 24, tohum),
    { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 500 + tohum }, tb, 0.4, 0.55));
  altSari(kel(5), 52.92, 1);     // ago
  altSari(kel(14), 55.32, 2);    // yet

  // 56,45–59,81 SOL: takvim + kapalı nokta "two weeks ago"; resigned ve ago sarı daire; etiket
  // Simple Past
  S.koy(S.halka(kel(2), 56.45, 0.35, 11));
  S.koy(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 150, y: 545, w: 290, h: 290 }, enCok: 8,
    w: 4,
    tb: 56.6, sure: 0.8, olayEnCok: 4 }));
  S.koy(S.darbe([[150, 900], [380, 893], [620, 903], [880, 897]], { w: 4, renk: IKINCIL,
    alfa: 0.9, uc0: 8,
    uc1: 12 }, 57.1, 0.5, 0.45));
  S.koy(S.darbe(elips(330, 898, 11, 11, 0, 3), { w: 20, renk: KREM, alfa: 0.95, uc0: 4, uc1: 4 },
    57.5, 0.15, 0.6));
  S.koy(S.halka(kel(5), 57.65, 0.35, 13));
  // El yazısı (Caveat tegaki, dalga 5b / K26): not ve etiketler kalemle yazılır.
  // 57,90 anlatımsız etiket `two weeks ago` («ago» 57,65–57,89; «var,» 57,97): hedef 0,7 sn → 58,60
  S.koy(S.elYazisi({ metin: "two weeks ago", x: 190, y: 972, boy: 64, renk: KREM, tb: 57.9,
    sure: 0.7 }));
  S.koy(S.metinPop({ parca: [["Simple Past", SARI]], x: 500, y: 665, font: FF(72), tb: 59.49,
    sure: 0.4, ses: 0.8,
    turu: "vurus" }));

  // 60,84–65,32 SAĞ: saat + now'a uzanan ok; has not found ve yet sarı daire; etiket Present
  // Perfect
  const hnf = [kel(9), kel(10), kel(11)];
  S.koy(S.darbe(elips(hnf[0].x + (hnf[2].x + hnf[2].w - hnf[0].x) / 2, hnf[0].y - 22,
    (hnf[2].x + hnf[2].w - hnf[0].x) / 2 + 10, 52, -0.03, 21), { w: 6, renk: SARI, alfa: 0.85,
      uc0: 14, uc1: 30 },
    60.84, 0.5, 0.55));
  S.koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 1020, y: 545, w: 290, h: 290 }, enCok: 6, w: 4,
    tb: 61.0, sure: 0.8, olayEnCok: 4 }));
  S.koy(S.darbe([[1000, 900], [1250, 893], [1500, 903], [1760, 897]], { w: 4, renk: IKINCIL,
    alfa: 0.9, uc0: 8,
    uc1: 12 }, 61.6, 0.6, 0.45));
  S.koy(S.darbeler(ok([1560, 840], [1730, 888], 17), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 61.9,
    0.3, 0.15, 0.5));
  // 62,00 anlatımsız etiket `now` («found:» 61,48–62,44): hedef 0,45 sn → 62,45
  S.koy(S.elYazisi({ metin: "now", x: 1690, y: 972, boy: 64, renk: KREM, tb: 62.0, sure: 0.45 }));
  S.koy(S.halka(kel(14), 62.6, 0.35, 19));
  // 63,00 anlatımsız etiket `yet = belirsiz` («var, zaman belirsiz,» 63,00–64,60): hedef 0,8 sn
  // → 63,80
  S.koy(S.elYazisi({ metin: "yet = belirsiz", x: 1010, y: 972, boy: 64, renk: KREM, tb: 63.0,
    sure: 0.8 }));
  S.koy(S.metinPop({ parca: [["Present Perfect", SARI]], x: 1370, y: 665, font: FF(64), tb: 64.76,
    sure: 0.4, ses: 0.8, turu: "vurus" }));
  S.koy(S.parilti(1760, 560, 65.0, 24));
}

surucu(kur, (f) => S.kare(f), KARE);

// SAHNE 05 (DİKEY) — Örnek 3: düz canvas, 482 kare, t_bas 52,56; cümle 5 (16.11 DUZ3 sesi). Zaman yalnız kare numarasından.
// Yerleşim BRIEF-DIKEY §4: kart (cümle) -> TR çeviri -> uçak + çarpı -> yaşam çizgisi -> etiketler -> formül.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, kutu, ok, elips, olc } from "./sahne-ortak.js";

const KARE = 482, TBAS = 52.56, ICERIK = 470;
const KOKDIZ = "/projeler/present-perfect-temel-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;
// El yazısı (tegaki Caveat, dalga 5 / K26): sözcük penceresi = anlatım t0/t1 (küresel sn)
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

async function kur() {
  await S.kur();
  const ucak = await svgOku("coco/plane.svg");

  // Kart (tam genişlik 984, iç boşluk 40): cümle sözcük zamanında; never sarı daire 54,88
  S.koy(S.darbeler(kutu(48, 372, 984, 214, 11), { w: 4, renk: IKINCIL, uc0: 10, uc1: 16 },
    53.11, 0.12, 0.1, 0.5));
  const cum = S.koy(S.cumleYaz({
    sozcukler: S.dizi("I", 54.40, 7), x: 88, y: 462, maxGen: 660, font: FF(72),
    satirH: 80, bosluk: 8
  }));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);
  S.koy(S.halka(kel("never"), 54.88, 0.3, 31));

  // Türkçe çeviri (Caveat 64, mürekkep) 56,81
  // 56,81–58,86 «Hayatımda hiç uçağa binmedim.» (pencere: 4 sözcük)
  S.koy(S.elYazisi({
    metin: "Hayatımda hiç uçağa binmedim.", x: 88, y: 646, boy: 64, renk: KREM,
    sozcukler: pen("Hayatımda", 56.81, 4)
  }));

  // ORTA: uçak (788 x 420, kutu ≥ 420) 54,52; sarı çarpı 58,34
  const UX = 146, UY = 671, UW = 788, UH = 420;
  S.koy(S.cizim({
    svg: ucak, kutu: { x: UX, y: UY, w: UW, h: UH }, ad: "ucak", esik: 0.01, enCok: 30, w: 4.4,
    tb: 54.52, sure: 1.3, olayEnCok: 6
  }));
  S.koy(S.parilti(UX + UW - 24, UY + 14, 55.92, 32));
  const cx0 = UX + UW / 2, cy0 = UY + UH / 2;
  S.koy(S.darbe([[cx0 - 270, cy0 - 145], [cx0, cy0], [cx0 + 270, cy0 + 145]],
    { duz: true, w: 11, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 71 }, 58.34, 0.22, 0.7));
  S.koy(S.darbe([[cx0 + 270, cy0 - 145], [cx0, cy0], [cx0 - 270, cy0 + 145]],
    { duz: true, w: 11, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 72 }, 58.54, 0.22, 0.7));

  // Yaşam çizgisi: birth ● ━━ ● now (58,92–61,0); orta metin 59,61; sarı bant kapatır
  const ly = 1181, bx = 110, nx = 970, ey = ly - 34;
  S.koy(S.darbe(elips(bx, ly, 10, 10, 0, 33), { w: 18, uc0: 3, uc1: 3, tohum: 33 },
    58.92, 0.2, 0.5));
  // 58,99 anlatımsız etiket `birth`: hedef 0,45 sn → 59,44
  S.koy(S.elYazisi({ metin: "birth", x: 56, y: ey, boy: 64, renk: KREM, tb: 58.99, sure: 0.45,
    ses: false }));
  S.koy(S.darbe([[bx + 16, ly], [(bx + nx) / 2, ly - 3], [nx - 16, ly + 1]],
    { duz: true, w: 5, uc0: 8, uc1: 14, tohum: 34 }, 59.17, 0.5, 0.55));
  S.koy(S.darbe(elips(nx, ly, 10, 10, 0, 35), { w: 18, uc0: 3, uc1: 3, tohum: 35 },
    59.61, 0.2, 0.5));
  // 59,67 anlatımsız etiket `now`: hedef 0,45 sn → 60,12
  S.koy(S.elYazisi({ metin: "now", x: 892, y: ey, boy: 64, renk: SARI, tb: 59.67, sure: 0.45,
    ses: false }));
  const mf = CV(64), mw = olc(mf, "bugüne kadar hiç");
  // 58,92–59,77 «Bugüne kadar hiç» (pencere: 58,92–59,13 · 59,17–59,53 · 59,61–59,77)
  S.koy(S.elYazisi({
    metin: "bugüne kadar hiç", x: 540 - mw / 2 - 10, y: ey, boy: 64, renk: KREM,
    sozcukler: pen("Bugüne", 58.92, 3)
  }));
  S.koy(S.darbe([[bx - 16, ly + 1], [(bx + nx) / 2, ly - 2], [nx + 16, ly]],
    { duz: true, w: 30, renk: SARI, alfa: 0.3, uc0: 24, uc1: 36, tohum: 36 }, 59.92, 1.0, 0.5));

  // Etiket (Caveat 64, el kutusu + tik): never 61,84 (16.11: ses "Burada never …"; ever ve just etiketi kalktı)
  const yb = ly + 28, bh = 72, lfn = CV(64);
  const boslar = [["never", 61.84]];
  const gen = boslar.map(([m]) => olc(lfn, m) + 56), top = gen.reduce((a, b) => a + b, 0) + 24 * (boslar.length - 1);
  let xx = 540 - top / 2;
  boslar.forEach(([m, tb], i) => {
    const w = gen[i];
    S.koy(S.darbeler(kutu(xx, yb, w, bh, 30 + i), { w: 4, renk: KREM, uc0: 8, uc1: 14 },
      tb, 0.1, 0.06, false));
    // anlatımsız etiket (kutudan 0,22 sn sonra): hedef 0,45 sn
    S.koy(S.elYazisi({
      metin: m, x: xx + 28, y: yb + 52, boy: 64, renk: KREM, tb: tb + 0.22, sure: 0.45
    }));
    xx += w + 24;
  });
  // 63,12 sarı ok -> now noktası (bugüne), nabız 63,52 (kadarki)
  S.koy(S.darbeler(ok([xx - 10, yb + 18], [nx - 6, ly + 24], 5),
    { w: 9, renk: SARI, uc0: 10, uc1: 14 }, 63.12, 0.3, 0.2, 0.55));
  S.koy(S.nabiz(nx, ly, 14, 63.52));

  // 65,99 have, 67,51 flown sarı daire; formül have + flown (Fredoka 110)
  S.koy(S.halka(kel("have"), 65.99, 0.3, 38));
  S.koy(S.halka(kel("flown"), 67.51, 0.3, 32));
  const fo = FF(110), p1 = "have", p2 = " + ", p3 = "flown", fy = 1380;
  const toplam = olc(fo, p1) + olc(fo, p2) + olc(fo, p3);
  let fx = 540 - toplam / 2;
  S.koy(S.metinPop({
    parca: [[p1, KREM]], x: fx, y: fy, font: fo, tb: 65.99, sure: 0.35, ses: 0.8, turu: "vurus"
  }));
  fx += olc(fo, p1);
  S.koy(S.metinPop({
    parca: [[p2, IKINCIL]], x: fx, y: fy, font: fo, tb: 66.87, sure: 0.3, ses: false
  }));
  fx += olc(fo, p2);
  S.koy(S.metinPop({
    parca: [[p3, SARI]], x: fx, y: fy, font: fo, tb: 67.51, sure: 0.35, ses: 0.8, turu: "vurus"
  }));
}

surucu(kur, (f) => S.kare(f), KARE);

// SAHNE 09 — Karşıt çift 2–3 (düz canvas, 1118 kare, t_bas 130,74; cümle 10 ve 11). Kendini çizen
// kalem; zaman yalnız kare numarasından.
// Üst çift: I am staying here for a week ≠ My holiday package includes trips … (geçici ≠ genel)
// Alt çift: The region offers some of the best beaches … ≠ People are really enjoying … (genel ≠ şu an)
import { surucu } from "/ortak/surucu.js";
import { KUNYE } from "/projeler/02-03-ydt-temel/ortak/kunye.js";
import { Sahne, RT, elips, altCizgi, olc } from "./sahne-ortak.js";

const KARE = 1118, TBAS = 130.66, ICERIK = 1106;
const ETKIN = ((i) => (i >= 0 ? i : 2))(KUNYE.ajanda.findIndex((a) => /contrast|pair/i.test(a)));
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Contrast 2–3 / 3", cumle: 10,
  etkin: ETKIN });
const KOKDIZ = "/projeler/02-03-ydt-temel/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

// Yerleşim (1920×1080): iki kart sütunu, ortada ≠ ; üst çift y 140–430, alt çift y 470–980
const KW = 810, XL = 100, XR = 1010, PAD = 40, GEN = KW - 2 * PAD;
const P1 = { y: 140, h: 290 }, P2 = { y: 470, h: 510 };

// Sağa/sola kalem çizgisi dizileri
const dalga = (x0, x1, y, genlik, periyot) => {
  const g = [], n = Math.ceil((x1 - x0) / 20);
  for (let i = 0; i <= n; i++) {
    const x = x0 + ((x1 - x0) * i) / n;
    g.push([x, y + genlik * Math.sin(((x - x0) / periyot) * Math.PI * 2)]);
  }
  return g;
};
// ≠ işareti: iki yatay çizgi + eğik çizgi (yazı tipinde ≠ yok; kalemle çizilir)
const esitDegil = (cx, cy) => [[[cx - 24, cy - 13], [cx + 24, cy - 13]],
  [[cx - 24, cy + 13], [cx + 24, cy + 13]], [[cx + 13, cy - 36], [cx - 13, cy + 36]]];

async function kur() {
  await S.kur();
  // Bu sahne iki cümle taşır (10, 11): sözcük zamanları ikisinden
  const tum = await (await fetch("/projeler/02-03-ydt-temel/ortak/anlatim/sozcukler.json")).json();
  S.sozc = tum.filter((s) => s.cumle === 10 || s.cumle === 11);
  const [sahilSvg, kisi] = await Promise.all([svgOku("tabler/umbrella.svg"),
    svgOku("open-peeps/standing-2.svg")]);

  // 4 cümle (EN) ortak yazı tipi: en geniş satır kart içine (730 px) sığar
  const dizi = {
    l1: S.dizi("I", 133.06, 7), r1: S.dizi("My", 137.56, 10),
    l2: S.dizi("The", 150.69, 11), r2: S.dizi("People", 159.83, 8),
  };
  const bol = { l1: [7], r1: [4, 6], l2: [5, 6], r2: [4, 4] };
  const KAT = 44, EK = 4;
  const satirlar = (ad) => {
    let i = 0;
    return bol[ad].map((n) => { const s = dizi[ad].slice(i, i + n); i += n; return s; });
  };
  let enGen = 0;
  for (const ad of Object.keys(dizi)) {
    for (const s of satirlar(ad)) {
      enGen = Math.max(enGen, olc(`700 ${KAT}px Fredoka`, s.map((k) => k.sozcuk).join(" "))
        + (s.length - 1) * EK);
    }
  }
  const PX = Math.min(KAT, Math.floor((KAT * GEN) / enGen));
  const F = `700 ${PX}px Fredoka`, SATIR = Math.round(PX * 1.6);

  // Bir kartın cümlesi: x, ilk satır taban çizgisi y
  const yaz = (ad, x, y) => S.koy(S.cumleYaz({ sozcukler: dizi[ad], x, y, font: F, satirH: SATIR,
    satirSay: bol[ad], bosluk: EK }));
  const kartCiz = (x, y, h, tb, tohum, ad) => S.koy(S.kart({ x, y, w: KW, h, tb, tohum, satirlar: [],
    ad, kutuSure: 0.12, kutuAralik: 0.08 }));
  // sarı daire (sözcük ya da sözcük çifti): aynı satırda
  const halka = (a, b, tb, tohum) => S.koy(S.darbe(altCizgi(a.x - 2, b.x + b.w + 2, a.y + 26, tohum),
  { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14 }, tb, 0.4, 0.55));   // halka yerine el altçizgisi (13.11 QA)
  // sarı belirteç (alt çizgi)
  const belirtec = (a, b, tb, tohum) => S.koy(S.darbe(altCizgi(a.x - 4, b.x + b.w + 4, a.y + 26,
    tohum), { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 520 + tohum }, tb, 0.4, 0.55));
  // el yazısı etiket; alt çizgisi için {x, w} döner
  const etiket = (metin, x, y, renk, tb, sure) => S.koy(S.elYazisi({ metin, x, y, boy: 64, renk,
    tb, sure }));
  const altCiz = (e, y, tb, tohum) => S.koy(S.darbe(altCizgi(e.x - 4, e.x + e.w + 4, y + 18, tohum),
    { w: 7, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 560 + tohum }, tb, 0.4, 0.5));
  const esit = (cy, tb) => esitDegil(960, cy).forEach((p, i) => S.koy(S.darbe(p, { duz: true,
    w: 7, renk: KREM, alfa: 0.9, uc0: 4, uc1: 8, tohum: 700 + i }, tb + i * 0.12, 0.14,
  i ? false : 0.5)));

  // ===== Üst çift (cümle 10: 131,29–148,93) =====
  const Y1 = P1.y + 85, YE1 = P1.y + 255;
  // 131,35 sol kart · 133,14 cümle · 134,10 for a week sarı belirteç · 136,35 TEMPORARY
  kartCiz(XL, P1.y, P1.h, 131.27, 1, "kart-sol-1");
  const l1 = yaz("l1", XL + PAD, Y1);
  belirtec(l1.kel[4], l1.kel[6], 134.02, 71);
  const tmp = etiket("TEMPORARY", XL + PAD, YE1, SARI, 136.27, 0.7);
  // 137,50 sağ kart · 137,64 cümle · 138,92 includes daire · 142,05 ≠ · 142,61 GENERAL
  kartCiz(XR, P1.y, P1.h, 137.42, 2, "kart-sag-1");
  const r1 = yaz("r1", XR + PAD, Y1);
  halka(r1.kel[3], r1.kel[3], 138.84, 73);
  esit(P1.y + P1.h / 2, 141.97);
  const gen1 = etiket("GENERAL", XR + PAD, YE1, KREM, 142.53, 0.6);
  // 145,33 Geçici: · 147,33 Genel: etiket altı sarı çizgi
  altCiz(tmp, YE1, 145.25, 81);
  altCiz(gen1, YE1, 147.25, 82);

  // ===== Alt çift (cümle 11: 149,48–167,68) =====
  const Y2 = P2.y + 85, YE2 = P2.y + 475;
  // 149,55 sol kart · 150,77 cümle · 151,33 offers sarı belirteç
  kartCiz(XL, P2.y, P2.h, 149.47, 3, "kart-sol-2");
  const l2 = yaz("l2", XL + PAD, Y2);
  belirtec(l2.kel[2], l2.kel[2], 151.25, 91);
  // 154,30–156,6 sahil çizgisi: iki dalga, kıyı, şemsiye; 157,26 GENERAL
  S.koy(S.darbe(dalga(150, 640, 705, 9, 110), { w: 5, renk: IKINCIL, alfa: 0.9, uc0: 10,
    uc1: 16, tohum: 311 }, 154.22, 0.6, 0.45));
  S.koy(S.darbe(dalga(190, 600, 755, 9, 100), { w: 5, renk: IKINCIL, alfa: 0.9, uc0: 10,
    uc1: 16, tohum: 312 }, 154.78, 0.55, false));
  S.koy(S.darbe([[140, 860], [330, 835], [540, 848], [720, 815], [880, 832]], { w: 6, renk: KREM,
    alfa: 0.9, uc0: 12, uc1: 20, tohum: 313 }, 155.5, 0.7, 0.5));
  S.koy(S.cizim({ svg: sahilSvg, ad: "semsiye", kutu: { x: 690, y: 640, w: 180, h: 180 },
    enCok: 6, w: 4, tb: 155.74, sure: 0.8, olayEnCok: 3 }));
  etiket("GENERAL", XL + PAD, YE2, KREM, 157.18, 0.6);
  // 159,80 sağ kart · 159,91 cümle · 160,23 are really enjoying daire
  kartCiz(XR, P2.y, P2.h, 159.72, 4, "kart-sag-2");
  const r2 = yaz("r2", XR + PAD, Y2);
  halka(r2.kel[1], r2.kel[3], 160.15, 93);
  // 163,76 figür (standing) · 164,00 RIGHT NOW · 165,36 ≠ · 166,72 figür kollarını açar
  const FX = 1420, FY = 650, FW = 150, FH = 300;
  const kisiOge = S.cizim({ svg: kisi, ad: "figur", kutu: { x: FX, y: FY, w: FW, h: FH },
    esik: 0.004, enCok: 60, w: 3.2, tb: 163.68, sure: 1.2, olayEnCok: 5 });
  const fHop = S.fr(166.64), fCx = FX + FW / 2, fCy = FY + FH;
  kisiOge.donusum = (f) => ({ cx: fCx, cy: fCy, tx: 0, dondur: 0, olcek: 1,
    ty: f < fHop ? 0 : -16 * Math.sin(Math.PI * Math.min(1, (f - fHop) / 14)) });
  S.koy(kisiOge);
  etiket("RIGHT NOW", XR + PAD, YE2, SARI, 163.92, 0.7);
  esit(P2.y + P2.h / 2, 165.28);
  // kollar açılır: figürün iki yanında sarı çizgiler (ışın) 166,72
  [[[FX - 36, FY + 92], [FX - 8, FY + 112]], [[FX + FW + 36, FY + 92], [FX + FW + 8, FY + 112]],
    [[FX - 44, FY + 150], [FX - 14, FY + 150]], [[FX + FW + 44, FY + 150], [FX + FW + 14,
      FY + 150]]].forEach((p, i) => S.koy(S.darbe(p, { duz: true, w: 6, renk: SARI, alfa: 0.9,
    uc0: 3, uc1: 6, tohum: 330 + i }, 166.64 + i * 0.04, 0.12, i ? false : 0.5)));
}

surucu(kur, (f) => S.kare(f), KARE);

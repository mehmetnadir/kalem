// SAHNE 04 (İLERİ) — Örnek 2 (düz canvas, 387 kare, t_bas 29,58; cümle 4). Kendini çizen kalem;
// zaman yalnız kare numarasından.
// Kök: "Because the roof is leaking, we are staying at my uncle's house this week." (çatı + ev,
// geçici durum).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu } from "./sahne-ortak.js";

const KARE = 387, TBAS = 29.58, ICERIK = 375;
const KOKDIZ = "/projeler/present-continuous-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
// El yazısı (tegaki Caveat, dalga 5 / K26): sözcük penceresi = anlatım t0/t1 (küresel sn)
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

async function kur() {
  await S.kur();
  const [ev, damla, kiz] = await Promise.all([svgOku("tabler/home.svg"), svgOku("coco/rain.svg"),
    svgOku("open-peeps/sitting-7.svg")]);

  // 30,13–31,09 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 200, 190, 30.13));

  // 31,34–35,50 İngilizce kök (Fredoka 56, sözcük zamanlı, sarı alt çizgi kayar)
  const F56 = "700 56px Fredoka";
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Because", 31.34, 14), x: 140, y: 300,
    maxGen: 980, font: F56, satirH: 76, satirSay: [5, 6, 3], bosluk: 4 }));
  // satır 1: 0 Because … 4 leaking, | satır 2: 5 we … 10 uncle's | satır 3: 11 house 12 this 13
  // week.
  const kel = (i) => cum.kel[i];
  // iki sözcüğe tek sarı daire; satır ayrıysa her birine
  const cevre = (a, b, tb, egim, tohum) => {
    const A = kel(a), B = kel(b);
    const tek = (x0, x1, y, t, th) => S.darbe(elips((x0 + x1) / 2, y - 22, (x1 - x0) / 2 + 5, 42,
      egim, th),
      { w: 6, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, t, 0.4, 0.55);
    if (A.y === B.y) S.koy(tek(A.x, B.x + B.w, A.y, tb, tohum));
    else { S.koy(tek(A.x, A.x + A.w, A.y, tb, tohum)); S.koy(tek(B.x, B.x + B.w, B.y, tb + 0.15,
      tohum + 1)); }
  };
  cevre(3, 4, 32.14, -0.03, 11);                                   // is leaking
  cevre(6, 7, 33.02, -0.03, 13);                                   // are staying
  // this week: sarı köşeli ayraç (34,38–34,70)
  {
    const A = kel(12), B = kel(13), y = A.y + 30;
    const parca = A.y === B.y ? [[[A.x - 4, y - 10], [A.x - 4, y + 6], [B.x + B.w + 4, y + 6],
      [B.x + B.w + 4, y - 10]]]
      : [[[A.x - 4, y - 10], [A.x - 4, y + 6], [A.x + A.w + 4, y + 6]], [[B.x - 4, B.y + 36],
        [B.x + B.w + 4, B.y + 36], [B.x + B.w + 4, B.y + 20]]];
    parca.forEach((p, i) => S.koy(S.darbe(p, { duz: true, w: 7, renk: SARI, alfa: 0.85, uc0: 12,
      uc1: 24 }, 34.38 + i * 0.12, 0.35, 0.6)));
  }

  // 31,3–35,0 sağ sahne: büyük ev + 3 damla, ok, küçük ev (uncle's), önünde figür
  S.koy(S.cizim({ svg: ev, ad: "ev", kutu: { x: 1190, y: 220, w: 330, h: 330 }, enCok: 6, w: 4,
    tb: 31.4, sure: 0.9, olayEnCok: 4 }));
  [[1262, 372, 31.95], [1330, 300, 32.4], [1397, 372, 32.85]].forEach(([x, y, tb], i) => {
    const g = S.cizim({ svg: damla, ad: "damla", kutu: { x, y, w: 52, h: 104 }, enCok: 6,
      esik: 0.004, w: 3.4, tb, sure: 0.35, olayEnCok: 1, nefes: false });
    g.donusum = (f) => ({ cx: x, cy: y, tx: 0,
      ty: f < S.fr(tb + 0.35) ? 0 : 7 * Math.sin((Math.min(f,
        ICERIK) - S.fr(tb + 0.35)) / 9 + i * 2), dondur: 0, olcek: 1 });
    S.koy(g);
  });
  S.koy(S.darbeler(ok([1545, 380], [1625, 372], 3), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 33.3,
    0.16, 0.12, 0.5));
  S.koy(S.cizim({ svg: ev, ad: "kucuk-ev", kutu: { x: 1640, y: 235, w: 190, h: 190 }, enCok: 6,
    w: 4, tb: 33.5, sure: 0.7, olayEnCok: 3 }));
  // 33,82–34,06 «uncle's» (pencere: 1 sözcük); orta eksen x 1735, tegaki genişliği 95,6 px → x
  // 1687,2
  S.koy(S.elYazisi({ metin: "uncle's", x: 1735 - 95.6 / 2, y: 215, boy: 44, renk: SARI,
    sozcukler: pen("uncle's", 33.82, 1) }));
  S.koy(S.cizim({ svg: kiz, ad: "kiz", kutu: { x: 1690, y: 435, w: 160, h: 210 }, esik: 0.004,
    enCok: 60, w: 3.2, tb: 34.0, sure: 1.3, olayEnCok: 6 }));

  // 35,75–38,87 Türkçe çeviri (Caveat 48 ikincil, y 620)
  const ytr = 620;
  // 35,75–38,83 «Çatı aktığı için bu hafta amcamlarda kalıyoruz.» (7 sözcük penceresi);
  // "bu" penceresi (0,08 sn) sonraki sözcüğün başına (37,15) dek uzatıldı
  const trPen = pen("Çatı", 35.75, 7); trPen[3].t1 = trPen[4].t0;
  S.koy(S.elYazisi({ metin: "Çatı aktığı için bu hafta amcamlarda kalıyoruz.", x: 140, y: ytr,
    boy: 48,
    renk: IKINCIL, sozcukler: trPen }));

  // 38,87–40,27 geçici durum: 7 günlük takvim şeridi, ayraç this week, ok -> eve dönüş
  {
    const gun = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], x0 = 140, kw = 120, ad = 138,
      ky = 740, kh = 84;
    gun.forEach((g, i) => {
      S.koy(S.darbeler(kutu(x0 + ad * i, ky, kw, kh, 30 + i), { w: 3.4, renk: KREM, uc0: 8,
        uc1: 14 }, 38.87 + i * 0.07, 0.1, 0.07, i === 0 ? 0.45 : false));
      S.koy(S.metinPop({ parca: [[g, IKINCIL]], x: x0 + ad * i + kw / 2, y: ky + 54,
        font: "500 28px Lexend", hiza: "orta", tb: 38.95 + i * 0.07, sure: 0.2, ses: false }));
    });
    const xe = x0 + ad * 7 - 18;
    S.koy(S.darbe([[x0 - 6, ky - 12], [x0 - 6, ky - 28], [xe + 6, ky - 28], [xe + 6, ky - 12]],
      { duz: true, w: 7, renk: SARI, alfa: 0.85, uc0: 12, uc1: 24 }, 39.35, 0.4, 0.6));
    // 39,50 anlatımsız etiket «this week»: hedef 0,45 sn → 39,95; orta eksen 614, tegaki genişliği
    // 141,2 px
    S.koy(S.elYazisi({ metin: "this week", x: (x0 + xe) / 2 - 141.2 / 2, y: ky - 44, boy: 44,
      renk: SARI,
      tb: 39.5, sure: 0.45 }));
    // 39,30 anlatımsız etiket «geçici» (Geçici 38,87–39,19): hedef 0,45 sn → 39,75
    S.koy(S.elYazisi({ metin: "geçici", x: 140, y: 905, boy: 48, renk: SARI, tb: 39.3,
      sure: 0.45 }));
    S.koy(S.darbeler(ok([330, 890], [440, 890], 3), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 39.8,
      0.16, 0.12, 0.5));
    // 40,00 anlatımsız etiket «eve dönüş»: hedef 0,45 sn → 40,45 (sonraki daire 40,47)
    S.koy(S.elYazisi({ metin: "eve dönüş", x: 470, y: 905, boy: 48, renk: KREM, tb: 40.0,
      sure: 0.45 }));
  }

  // 40,27–42,07 This week bunu söyler: this week sarı daire; formül kartı be + V-ing -> is leak-ing
  // / are stay-ing
  cevre(12, 13, 40.47, -0.03, 17);
  {
    const kx = 1190, ky = 675, fo = "700 60px Fredoka";
    S.koy(S.kart({ x: kx, y: ky, w: 640, h: 305, tb: 40.75, tohum: 4, satirlar: [
      { parca: [["be", KREM], ["  +  ", IKINCIL], ["V", KREM], ["-ing", SARI]], x: kx + 60,
        y: ky + 90, font: fo, tb: 41.1 },
      { parca: [["is leak", KREM], ["-ing", SARI]], x: kx + 60, y: ky + 185, font: fo, tb: 41.35 },
      { parca: [["are stay", KREM], ["-ing", SARI]], x: kx + 60, y: ky + 280, font: fo, tb: 41.6 },
    ] }));
    S.koy(S.parilti(kx + 600, ky + 40, 41.75));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

// Sahne 02 İLERİ (Simple Present) — Kanca + kural (451 kare, t_bas 3,00; cümle 2). Yerel kare = round((t − 3,00) × 30).
// Cümle 1 yazısı 0. karede yerinde (sahne 01 ile aynı yer, x 140 y 300); içerik 17,25 sn'de biter.
import { sahneKur, RT, renkCoz }
  from "/projeler/deneme-doku/sahneler/02-paperjs-kanca/kalem-paper.js";
import { yaziNoktalari } from "/projeler/deneme-doku/ortak/kalem-canvas.js";

export const KARE = 451, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { P: PP, fr, daire, yazi, elYazisi, dinamik, cumle, tik, parilti, olay, not, bitis, kutu,
    svgCiz } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  // El yazısı (Caveat 700 tegaki, dalga 5b / K26): ortalı yazının x'i için genişlik glif verisinden
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  // etiket önü dolu nokta (`·` Caveat paketinde yok): r 4, zamanı gelince görünür
  const nokta = (cx, cy, renk, bas) => dinamik((f, gr) => { if (f < bas) return;
    gr.addChild(new PP.Path.Circle({ center: [cx, cy], radius: 4, fillColor: renkCoz(renk),
      opacity: 0.9, insert: false })); });
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm, asc: EY.M.ascender,
    boy: boyut, x: 0, taban: 0 }).gen;

  // --- cümle 1: "Uçak yarın dokuzda kalkıyor." (Caveat 64, x 140, y 300); 0. karede hazır
  const c1 = cumle(["Uçak", "yarın", "dokuzda", "kalkıyor."].map((s) => ({ s, f: -10 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 yerinde", 0);
  {   // kalkıyor sarı daire titrer (3,00–3,71)
    const g = c1[3], tit = S.oge({ tit: { f0: 0, f1: fr(3.71), g: 2.4 } });
    daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 12, 38, { bas: -30, sure: 20, ses: false, oge: tit });
    not("kalkıyor daire titrer", 0);
  }
  // uçak (sağ üst), kalemle
  await svgCiz("coco/plane.svg", { kutu: [1400, 330, 400, 213], bas: fr(3.12), sure: 44, azami: 25, w: 4, sesAralik: 2 });
  not("uçak çizimi", fr(3.12));

  // --- 3,95–6,0: büyük ? ve iki kutu: will / Simple Present
  // 3,95 anlatımsız büyük `?`: hedef 14 kare (0,47 sn) → 4,42 (kutu will 4,51'de başlar);
  // x 540 ortalı
  elYazisi("?", { x: 540 - eyGen("?", 210) / 2, y: 575, boyut: 210, renk: SARI, bas: fr(3.95),
    sure: 14 });
  not("büyük ?", fr(3.95));
  kutu(140, 430, 300, 150, { bas: fr(4.51), sure: 26, w: 4 });
  yazi("will", { x: 290, y: 535, boyut: 84, aile: "Fredoka", agirlik: 700, hizala: "orta", renk: KRE, bas: fr(4.79), sure: 8, olcek: true, ses: true });
  not("kutu will", fr(4.51));
  kutu(660, 430, 640, 150, { bas: fr(5.0), sure: 28, w: 4 });
  yazi("Simple Present", { x: 980, y: 530, boyut: 72, aile: "Fredoka", agirlik: 700, hizala: "orta", renk: KRE, bas: fr(5.23), sure: 9, olcek: true, ses: true });
  not("kutu Simple Present", fr(5.0));

  // --- 6,19: "Önce kural" etiketi
  const k1 = elYazisi("ÖNCE KURAL", { x: 140, y: 690, boyut: 48, renk: IKI, bas: fr(6.19),
    sure: 12 });
  not("ÖNCE KURAL", fr(6.19));
  parilti(1320, 400, { bas: fr(6.5), r: 26, periyot: 0, adet: 1 });

  // --- 7,24–10,60: pozitif kural: he · she · it → V-s (Fredoka 72, taban y 735)
  {
    nokta(k1.x1 + 18, 690 - 0.22 * 48, SARI, fr(7.24));
    elYazisi("Positive", { x: k1.x1 + 36, y: 690, boyut: 48, renk: SARI, bas: fr(7.24),
      sure: 12 });
    not("Positive etiketi", fr(7.24));
    const Y = 795; let x = 140; const gap = 22;
    const koy = (s, t, o = {}) => { const y = yazi(s, { x, y: Y, boyut: 72, aile: "Fredoka", agirlik: 700, renk: o.renk || KRE,
      bas: fr(t), sure: 8, olcek: true, ses: o.ses !== false }); x = y.x1 + gap; return y; };
    koy("he", 8.32); koy("·", 8.42, { renk: IKI, ses: false }); koy("she", 8.52); koy("·", 8.7, { renk: IKI, ses: false });
    koy("it", 8.84); not("he · she · it", fr(8.32));
    koy("→", 9.0, { renk: IKI, ses: false });
    const v = koy("V-s", 9.16, { renk: SARI }); not("V-s (takes)", fr(9.16));
    const d = daire((v.x0 + v.x1) / 2, Y - 26, v.w / 2 + 14, 48, { bas: fr(9.45), sure: 20 });
    olay(bitis(d), "tik", 0.5); not("V-s daire", d.bas);
  }

  // --- 10,60–13,97: olumsuz + soru: does + base verb (taban y 945)
  {
    const e1 = elYazisi("Negative", { x: 140, y: 868, boyut: 48, renk: SARI, bas: fr(10.6),
      sure: 12 });
    not("Negative etiketi", fr(10.6));
    nokta(e1.x1 + 18, 868 - 0.22 * 48, SARI, fr(11.24));
    elYazisi("Question", { x: e1.x1 + 36, y: 868, boyut: 48, renk: SARI, bas: fr(11.24),
      sure: 12 });
    const Y = 955; let x = 140; const gap = 22;
    const koy = (s, t, o = {}) => { const y = yazi(s, { x, y: Y, boyut: 72, aile: "Fredoka", agirlik: 700, renk: o.renk || KRE,
      bas: fr(t), sure: 8, olcek: true, ses: o.ses !== false }); x = y.x1 + gap; return y; };
    const dz = koy("does", 12.28, { renk: SARI }); not("does", fr(12.28));
    const dd = daire((dz.x0 + dz.x1) / 2, Y - 26, dz.w / 2 + 14, 48, { bas: fr(12.45), sure: 18 });
    olay(bitis(dd), "tik", 0.5); not("does daire", dd.bas);
    koy("+", 12.6, { renk: IKI, ses: false }); koy("base", 12.92); koy("verb", 13.24); not("base verb", fr(12.92));
  }

  // --- 13,97–17,25: ajanda kutusu (sağ alt): form · time expressions · 3 YDT roots; saat 6 min
  kutu(1000, 650, 840, 340, { bas: fr(13.97), sure: 30, w: 4 }); not("ajanda kutusu", fr(13.97));
  await svgCiz("tabler/clock.svg", { kutu: [1640, 700, 160, 160], bas: fr(14.1), sure: 24, azami: 25, w: 4, sesAralik: 2 });
  elYazisi("6 min", { x: 1720 - eyGen("6 min", 64) / 2, y: 950, boyut: 64, renk: SARI,
    bas: fr(14.4), sure: 12 });
  not("saat + 6 min", fr(14.1));
  [["form", 14.85, 745], ["time expressions", 15.41, 835], ["3 YDT roots", 16.05, 925]].forEach(([s, t, y]) => {
    const z = yazi(s, { x: 1040, y, boyut: 56, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8, olcek: true, ses: true });
    tik(z.x1 + 44, y - 20, { bas: fr(t) + 9 }); not("madde " + s, fr(t));
  });
  parilti(1590, 690, { bas: fr(16.9), r: 28, periyot: 0, adet: 1 });
  return S;
}

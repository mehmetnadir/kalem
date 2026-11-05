// Sahne 03 — Örnek 1 (379 kare, t_bas 15,45; cümle 3 = 16,00–27,69). Yerel kare = round((t − 15,45)
// × 30).
import { sahneKur,
  RT } from "/projeler/simple-present-temel/sahneler/03-paperjs-ornek1/kalem-paper.js";
import { yaziNoktalari } from "/projeler/simple-present-temel/ortak/kalem-canvas.js";

export const KARE = 379, T_BAS = 15.45;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1 });
  const { fr, ciz, daire, ok, yazi, elYazisi, cumle, altCizgi, parilti, olay, not, bitis,
    kutu } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  // geçiş karesi: çizimler bundan sonra
  const GB = 12;

  // El yazısı: S.elYazisi (03 kalem-paper.js, 96b0651). Ortalı x için genişlik glif verisinden.
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm, asc: EY.M.ascender,
    boy: boyut, x: 0, taban: 0 }).gen;

  // --- 16,00–17,21: büyük el çizimi daire içinde 1 (x 140, y 200)
  const d1 = daire(200, 190, 66, 62, { bas: fr(16.0), sure: 20, a0: -2.6 });
  olay(bitis(d1), "tik", 0.5); not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 226, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700,
    bas: fr(16.0) + 4, sure: 10, olcek: true });

  // --- 17,21–18,65: Fredoka 64, x 140, y 320, 2 satır, sözcük sözcük + sarı alt çizgi
  const sz = S.sozcukler(3).slice(2, 8);                           // The sun rises in the east.
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: i < 3 ? 0 : 1 })),
    { x: 140, y: 320, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 84 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (The)", cz[0].bas); not("east.", cz[5].bas);

  // --- 17,21–19,45: sağ sütun: ufuk çizgisi, güneş, ok east
  const yUfuk = 740;
  const uf = ciz([[1020, yUfuk + 2], [1300, yUfuk - 2], [1580, yUfuk + 1], [1840, yUfuk - 1]],
    { w: 4, renk: IKI, alfa: 0.9, bas: fr(17.21), sure: 24, uc0: 10, uc1: 30 });
  not("ufuk çizgisi", uf.bas);
  const gunOge = S.oge({ nefes: { bas: fr(19.5), cx: 1480, cy: yUfuk } });
  await S.svgCiz("coco/sun.svg", { kutu: [1270, 290, 420, 420], bas: fr(17.4),
    sure: fr(19.2) - fr(17.4), azami: 30, w: 4, oge: gunOge, sesAralik: 3 });
  not("güneş çizimi başı", fr(17.4));
  parilti(1700, 300, { bas: fr(19.3), r: 26, periyot: 150, adet: 2 });
  {
    const b0 = fr(18.65);                                           // east. söylenir
    const o = ok([1320, 830], [1780, 830], { bas: b0, sure: 24, w: 7,
      bukum: 0.03 }); not("ok east", o.bas);
    // anlatımsız etiket: hedef 14 kare (0,47 sn); x 1550 ortalı
    elYazisi("east", { x: 1550 - eyGen("east", 64) / 2, y: 890, boyut: 64, renk: SARI,
      bas: bitis(o) - 4,
      sure: 14, ses: true });
    not("east etiketi", bitis(o) - 4);
  }

  // --- 19,86–21,94: Türkçe çeviri (Caveat 48 ikincil, y 520) + doğa kanunu etiketi (el kutusu)
  {   // pencere: Güneş 19,86–20,26 · doğudan 20,34–20,74 · doğar. 20,86–21,22
    const tr = S.sozcukler(3), i0 = tr.findIndex((w) => w.s === "Güneş");
    elYazisi("Güneş doğudan doğar.", { x: 140, y: 520, boyut: 48, renk: IKI,
      sozcukler: tr.slice(i0, i0 + 3).map((w) => ({ f0: w.f, f1: w.f1 })) });
  }
  not("Türkçe çeviri", fr(19.86));
  {
    const kb = fr(21.7);                                            // "Doğa" söylenir
    const k = kutu(140, 575, 330, 90, { bas: kb, sure: 22 }); not("doğa kanunu kutusu", kb);
    // anlatımsız etiket: hedef 18 kare (0,6 sn); x 305 ortalı
    elYazisi("doğa kanunu", { x: 305 - eyGen("doğa kanunu", 48) / 2, y: 636, boyut: 48, renk: SARI,
      bas: k.bit - 6, sure: 18, ses: true });
    not("doğa kanunu", k.bit - 6);
  }

  // --- 24,93: rises sarı daire; 26,65: sonundaki s ayrı sarı daire
  {
    const g = cz[2];
    const da = daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 6, 38, { bas: fr(24.93), sure: 18,
      a0: -2.2 });
    olay(bitis(da), "tik", 0.5); not("rises daire", da.bas);
    const ws = S.genislik("s", "700 64px Fredoka"), sx = g.x1 - ws / 2;
    const ds = daire(sx, g.y - 22, ws / 2 + 12, 40, { bas: fr(26.65), sure: 14, a0: -1.2 });
    olay(bitis(ds), "tik", 0.5); not("s daire", ds.bas);
  }

  // --- 27,01–27,69: formül kartı (el kutusu): it + V-s → rise-s; kare 366'dan sonra durgun
  {
    const kb = fr(26.9), F = { boyut: 64, aile: "Fredoka", agirlik: 700 }, y = 862;
    const k = kutu(140, 770, 800, 130, { bas: kb, sure: 8 }); not("formül kartı kutusu", kb);
    yazi("it", { ...F, x: 190, y, bas: kb + 4, sure: 5, olcek: true, ses: true }); not("it",
      kb + 4);
    yazi("+", { ...F, x: 290, y, bas: kb + 6, sure: 4, olcek: true });
    const v = yazi("V", { ...F, x: 360, y, bas: kb + 7, sure: 4, olcek: true });
    yazi("-s", { ...F, x: v.x1 + 4, y, bas: kb + 8, sure: 5, olcek: true, renk: SARI, ses: true });
    ok([550, 846], [640, 846], { bas: kb + 9, sure: 6, w: 6, renk: IKI, bukum: 0.02, uzun: 16 });
    const r = yazi("rise", { ...F, x: 660, y, bas: kb + 13, sure: 5, olcek: true });
    yazi("-s", { ...F, x: r.x1 + 4, y, bas: kb + 15, sure: 5, olcek: true, renk: SARI,
      ses: true }); not("rise-s", kb + 13);
    void k;
  }
  return S;
}

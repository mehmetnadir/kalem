// Sahne 03 (İLERİ) — Örnek 1 (456 kare, t_bas 17,65; cümle 3). Zamanlar BRIEF §4; yerel kare = round((t − 17,65) × 30).
// Kök: "Although the sun looks small from here, it gives plants the energy they need." (güneş + ağaç, bağlaç).
import { sahneKur, RT } from "/projeler/simple-present-ileri/sahneler/03-paperjs-ornek1/kalem-paper.js";
import { yaziNoktalari } from "/projeler/simple-present-ileri/ortak/kalem-canvas.js";

export const KARE = 456, T_BAS = 17.65;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, parilti, olay, not,
    bitis } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12;                                                   // geçiş karesi: çizimler bundan sonra başlar
  const f0 = (t) => Math.max(GB, fr(t));
  // El yazısı (Caveat 700 tegaki, dalga 5b / K26): ortalı yazının x'i için genişlik glif verisinden
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm, asc: EY.M.ascender,
    boy: boyut, x: 0, taban: 0 }).gen;

  // --- 18,20–19,41: büyük el çizimi daire içinde 1
  const d1 = daire(200, 168, 64, 58, { bas: f0(18.20), sure: 22, a0: -2.6 }); olay(bitis(d1), "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 204, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700, bas: f0(18.55), sure: 10, olcek: true });

  // --- 19,41–23,17: İngilizce kök (Fredoka 56, 3 satır, sözcük zamanlı) satır başı 0 / 5 / 10
  const sz = S.sozcukler(3).slice(2, 16);                          // Although … need.
  const satirNo = (i) => (i < 5 ? 0 : i < 10 ? 1 : 2);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 140, y: 300, boyut: 56, aile: "Fredoka", agirlik: 700, aralik: 76 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (Although)", cz[0].bas);
  // gives (21,73): kalıcı sarı alt çizgi
  {
    const g = cz[8], c = ciz([[g.x0 - 4, g.y + 12], [g.x1 + 4, g.y + 9]], { w: 8, renk: SARI, alfa: 0.85, duz: true,
      bas: fr(21.78), sure: 12, uc0: 8, uc1: 14, amp: 0.8 });
    not("gives alt çizgisi", c.bas);
  }

  // --- 19,41–23,77: sağ sahne. Güneş (360 px) ve ağaç (360 px); ok = enerji (gives)
  const ogeGunes = S.oge({ nefes: { bas: fr(23.2), cx: 1180, cy: 350 } });
  await S.svgCiz("coco/sun.svg", { kutu: [1000, 170, 360, 360], bas: f0(19.5), sure: fr(20.9) - f0(19.5), azami: 30, w: 3.6,
    oge: ogeGunes, sesAralik: 4 });
  not("güneş çizimi başı", f0(19.5));
  const ogeAgac = S.oge({ nefes: { bas: fr(24.0), cx: 1680, cy: 360 } });
  await S.svgCiz("coco/tree.svg", { kutu: [1500, 180, 360, 380], bas: f0(22.0), sure: fr(23.77) - f0(22.0), azami: 40, w: 3.6,
    oge: ogeAgac, sesAralik: 5 });
  not("ağaç çizimi başı", f0(22.0));
  const a1 = ok([1385, 352], [1478, 352], { bas: fr(21.80), sure: 14, w: 7, uzun: 20, bukum: 0.1 }); not("enerji oku", a1.bas);
  // 22,75 anlatımsız etiket `enerji`: hedef 14 kare (0,47 sn) → 23,22; x 1432 ortalı
  elYazisi("enerji", { x: 1432 - eyGen("enerji", 44) / 2, y: 322, boyut: 44, renk: SARI,
    bas: fr(22.75), sure: 14 });
  parilti(1190, 210, { bas: fr(23.0), r: 24 });

  // --- 24,30–28,78: Türkçe çeviri (Caveat 48 ikincil, 2 satır), her sözcük kendi penceresinde
  // (cümle 3: Güneş 24,30 · küçük 24,70 · görünse 25,02 · de 25,50 |
  // bitkilere 25,94 · gereken 26,38 · enerjiyi 26,94 · verir. 27,34–28,78)
  const tr = S.sozcukler(3).slice(16, 24);                         // Güneş küçük görünse de bitkilere gereken enerjiyi verir.
  const pen = (w) => w.map((k) => ({ f0: k.f, f1: k.f1 }));
  const tz = elYazisi("Güneş küçük görünse de", { x: 140, y: 560, boyut: 48, renk: IKI,
    sozcukler: pen(tr.slice(0, 4)) });
  elYazisi("bitkilere gereken enerjiyi verir.", { x: 140, y: 620, boyut: 48, renk: IKI,
    sozcukler: pen(tr.slice(4)) });
  not("Türkçe çeviri", tz.bas);
  parilti(1250, 480, { bas: fr(26.9), r: 20 });

  // --- 28,93–32,45: Although kutu -> ok "zaman değişmez" -> gives daire ; formül kartı it gives (V-s)
  {
    const a = cz[0];
    const k = kutu(a.x0 - 10, a.y - 46, a.w + 20, 66, { bas: fr(28.93), sure: 14, w: 5, renk: SARI });
    olay(k.bit, "tik", 0.5); not("Although kutusu", fr(28.93));
    yazi("Although", { x: 140, y: 790, boyut: 64, aile: "Fredoka", agirlik: 700, bas: fr(29.1), sure: 10, olcek: true, ses: true });
    kutu(130, 735, 330, 80, { bas: fr(29.15), sure: 16, w: 4.4, renk: SARI });
    const o1 = ok([485, 777], [585, 777], { bas: fr(29.55), sure: 12, w: 7, uzun: 20, bukum: 0.08 });
    not("ok bağlaç -> zaman", o1.bas);
    const zy = S.sozcukler(3).filter((q) => ["zaman", "değişmez:"].includes(q.s));
    // 29,97–31,57 «zaman değişmez:» (pencere: zaman 29,97–30,29 · değişmez: 30,37–31,57)
    const zz = elYazisi("zaman değişmez:", { x: 610, y: 792, boyut: 56, renk: SARI,
      sozcukler: zy.map((q) => ({ f0: q.f, f1: q.f1 })) });
    not("zaman değişmez", zz.bas);
    // gives (31,65): sarı daire cümlede + formül
    const g = cz[8];
    const dg = daire((g.x0 + g.x1) / 2, g.y - 20, (g.x1 - g.x0) / 2 + 7, 40, { bas: fr(31.62), sure: 18, a0: -2.6, egim: -0.03 });
    olay(bitis(dg), "tik", 0.5); not("gives daire", dg.bas);
    const kx = 1190, ky = 700;
    kutu(kx, ky, 640, 220, { bas: fr(30.55), sure: 22 }); not("formül kartı kutusu", fr(30.55));
    const F = { boyut: 64, aile: "Fredoka", agirlik: 700 }, y1 = ky + 90, y2 = ky + 185;
    yazi("it", { ...F, x: kx + 60, y: y1, bas: fr(30.95), sure: 10, olcek: true, ses: true });
    yazi("+", { ...F, x: kx + 150, y: y1, bas: fr(31.05), sure: 8, olcek: true });
    const v = yazi("V", { ...F, x: kx + 230, y: y1, bas: fr(31.15), sure: 8, olcek: true });
    yazi("-s", { ...F, x: v.x1 + 4, y: y1, bas: fr(31.27), sure: 10, olcek: true, renk: SARI, ses: true }); not("it + V-s", fr(31.27));
    const s1 = yazi("it give", { ...F, x: kx + 60, y: y2, bas: fr(31.66), sure: 10, olcek: true });
    yazi("s", { ...F, x: s1.x1 + 2, y: y2, bas: fr(31.72), sure: 10, olcek: true, renk: SARI, ses: true }); not("it gives", fr(31.66));
    parilti(kx + 600, ky + 40, { bas: fr(31.9), r: 22 });
  }
  return S;
}

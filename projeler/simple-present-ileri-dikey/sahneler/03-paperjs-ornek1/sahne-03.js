// Sahne 03 (İLERİ, DİKEY 1080x1920) — Örnek 1 (456 kare, t_bas 17,65; cümle 3). Yerel kare = round((t − 17,65) × 30).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (kalem-paper.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–722) · TR 3 satır (740–930) · sahne 940–1370 (27,9'da 0,42'ye toplanır) · formül kartı (1135–1390).
import { sahneKur, RT } from "/projeler/simple-present-ileri-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 456, T_BAS = 17.65;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, cumle, altCizgi, parilti, olay, not, bitis } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  const GB = 12;
  const f0 = (t) => Math.max(GB, fr(t));

  // --- 18,20: kart çerçevesi (el kutusu, 4 px) — içerik bandı 352–1392'nin üst parçası
  kutu(48, 372, 984, 350, { bas: f0(18.20), sure: 30, w: 4.2, renk: IKI }); not("kart çerçevesi", f0(18.20));

  // --- 19,41–23,17: İngilizce kök (Fredoka 64, 4 satır, sözcük zamanlı); satır başı 4 / 8 / 12
  const sz = S.sozcukler(3).slice(2, 16);                          // Although … need.
  const satirNo = (i) => (i < 4 ? 0 : i < 8 ? 1 : i < 12 ? 2 : 3);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 88, y: 452, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 78 });
  altCizgi(cz, { tut: 40, w: 8 }); not("cümle başı (Although)", cz[0].bas);
  {                                                                // gives (21,73): kalıcı sarı alt çizgi
    const g = cz[8], c = ciz([[g.x0 - 4, g.y + 14], [g.x1 + 4, g.y + 10]], { w: 10, renk: SARI, alfa: 0.85, duz: true,
      bas: fr(21.78), sure: 12, uc0: 8, uc1: 14, amp: 0.8 });
    not("gives alt çizgisi", c.bas);
  }

  // --- 19,41–23,77: ORTA sahne (940–1370): güneş 430 px + ağaç 430 px, ok "enerji"; 27,9'da 0,42'ye toplanır
  const G = S.oge({ topla: { f0: fr(27.9), f1: fr(28.7), ax: 540, ay: 940, olcek: 0.42, dy: 0 } });
  await S.svgCiz("coco/sun.svg", { kutu: [48, 940, 430, 430], bas: f0(19.5), sure: fr(20.9) - f0(19.5), azami: 30, w: 4.4,
    oge: G, sesAralik: 4 });
  not("güneş çizimi başı", f0(19.5));
  await S.svgCiz("coco/tree.svg", { kutu: [602, 940, 430, 430], bas: f0(22.0), sure: fr(23.77) - f0(22.0), azami: 40, w: 4.4,
    oge: G, sesAralik: 5 });
  not("ağaç çizimi başı", f0(22.0));
  const a1 = ok([492, 1150], [590, 1150], { bas: fr(21.80), sure: 14, w: 10, uzun: 24, bukum: 0.1, oge: G }); not("enerji oku", a1.bas);
  const lbl = yazi("enerji", { x: 541, y: 1240, hizala: "orta", boyut: 64, aile: "Caveat", agirlik: 700, renk: SARI, bas: fr(22.75), sure: 9,
    ses: true });
  G.g.addChild(lbl.g);                                             // yazı grubu da toplanır

  // --- 24,30–27,34: Türkçe çeviri (Caveat 64 mürekkep, 3 satır, ≤ 24 karakter/satır)
  const tr = S.sozcukler(3).slice(16, 24);                         // Güneş küçük görünse de bitkilere gereken enerjiyi verir.
  const tz = cumle(tr.map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : i < 6 ? 1 : 2 })),
    { x: 88, y: 790, boyut: 64, aile: "Caveat", agirlik: 700, aralik: 66, renk: KRE });
  not("Türkçe çeviri", tz[0].bas);

  // --- 27,9–28,7: sahne toplanır (grup 0,42) ; parıltı
  parilti(760, 1010, { bas: fr(27.9), r: 28 }); not("sahne toplanır (0,42)", fr(27.9));

  // --- 28,93–32,45: Although kutu -> formül kartı: "zaman değişmez" (Fredoka 110) ve "it gives" (V-s)
  {
    const a = cz[0];
    const k = kutu(a.x0 - 10, a.y - 54, a.w + 20, 76, { bas: fr(28.93), sure: 14, w: 6, renk: SARI });
    olay(k.bit, "tik", 0.5); not("Although kutusu", fr(28.93));
    kutu(48, 1135, 984, 252, { bas: fr(28.4), sure: 26, w: 4.2, renk: IKI }); not("formül kartı kutusu", fr(28.4));
    const F = { boyut: 110, aile: "Fredoka", agirlik: 700 };
    const z = yazi("zaman", { ...F, x: 100, y: 1244, bas: fr(29.97), sure: 10, olcek: true, ses: true });
    yazi("değişmez", { ...F, x: z.x1 + 30, y: 1244, bas: fr(30.37), sure: 10, olcek: true, renk: SARI, ses: true });
    not("zaman değişmez", fr(29.97));
    const g = cz[8];
    const dg = daire((g.x0 + g.x1) / 2, g.y - 22, (g.x1 - g.x0) / 2 + 8, 46, { bas: fr(31.62), sure: 18, a0: -2.6, egim: -0.03, w: 10 });
    olay(bitis(dg), "tik", 0.5); not("gives daire", dg.bas);
    const s1 = yazi("it give", { ...F, x: 100, y: 1362, bas: fr(31.66), sure: 10, olcek: true });
    const s2 = yazi("s", { ...F, x: s1.x1 + 2, y: 1362, bas: fr(31.72), sure: 10, olcek: true, renk: SARI, ses: true });
    yazi("(V-s)", { x: s2.x1 + 36, y: 1362, boyut: 80, aile: "Caveat", agirlik: 700, renk: SARI, bas: fr(31.9), sure: 9, ses: true });
    not("it gives (V-s)", fr(31.66));
    parilti(960, 1180, { bas: fr(32.0), r: 28 });
  }
  return S;
}

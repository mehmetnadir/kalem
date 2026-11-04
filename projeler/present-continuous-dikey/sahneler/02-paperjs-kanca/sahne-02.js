// Sahne 02 (DİKEY 1080x1920) — Kanca (385 kare, t_bas 3,00; cümle 2). Zamanlar KÜRESEL sn (sozcukler.json);
// yerel kare = round((t − 3,00) × 30). Cümle 1 ses olarak sahne 01'de söylendi: burada 0. kareden hazır durur
// (sahne 01 sonundaki yerle aynı: Caveat 80, taban 440 / 525), ilk 12 kare durgun.
// Yerleşim (BRIEF-DIKEY §4): faz 1 (3,0–6,4 sn) cümle 1 + notlar + 510 px'lik sahne; faz 2 (6,4 sn sonrası) sahne
// 0,58'e toplanır, yer açılan alana İngilizce cümle + -yor ⇄ -ing + ajanda kutusu gelir. Hiçbir öğe kaybolmaz.
import { sahneKur, RT } from "/projeler/present-continuous-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 385, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, ciz, daire, ok, yazi, cumle, altCizgi, tik, parilti, olay, not, bitis } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep, IKI = RT.ikincil;
  const GB = 12;                                                   // geçiş karesi: çizimler bundan sonra başlar

  // --- cümle 1: Caveat 80, iki satır; kare 0'da hazır (bas −8: maske açık, tam görünür)
  const c1 = cumle([["Bu", 0], ["akşam", 0], ["amcamlara", 0], ["gidiyorum.", 1]].map(([s, satir]) => ({ s, f: -8, satir })),
    { x: 48, y: 440, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 85 });
  not("cümle 1 hazır (kare 0)", 0);

  // --- sahne grubu (faz 1: y 750–1260; faz 2'de 0,6 ölçeğe pivot (48, 750))
  const KUCUL = { f0: 86, f1: 106, px: 48, py: 750, s: 0.58, dx: 0, dy: 0 };
  const sahneOge = S.oge({ kucul: KUCUL });
  const figOge = S.oge({ kucul: KUCUL, kay: { f0: 30, f1: 100, dx: 405 }, nefes: { bas: 110, cx: 540, cy: 1255 } });
  await S.svgCiz("tabler/home.svg", { kutu: [640, 860, 390, 380], bas: GB, sure: 30, azami: 25, w: 4, sesAralik: 2, oge: sahneOge });
  await S.svgCiz("open-peeps/standing-2.svg", { kutu: [60, 755, 150, 500], bas: GB, sure: 48, azami: 60, yuz: 3,
    w: 4.4, oge: figOge, sesAralik: 4, ayna: false });
  ciz([[48, 1256], [300, 1252], [560, 1258], [800, 1253], [1032, 1256]],
    { w: 4, renk: IKI, alfa: 0.8, bas: 36, sure: 30, uc0: 10, uc1: 30, oge: sahneOge });
  {   // hilal: dış yay + iç yay tek darbe
    const C = [940, 808], R = 46, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 6) pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 6) pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    const h = ciz(pts, { w: 4.4, alfa: 0.92, bas: 24, sure: 28, uc0: 12, uc1: 20, amp: 0.7, oge: sahneOge });
    not("hilal çizimi", h.bas);
    parilti(C[0] + 34, C[1] - 40, { bas: bitis(h) + 2, r: 26, periyot: 150, adet: 1 });
  }
  not("ev + figür çizimi başı", GB);

  // --- 3,39 gidiyorum sarı daire; 4,19 -yor → şimdiki zaman + saat; 5,15 takvim; 5,63 bu akşam → gelecek
  {
    const g = c1[3], d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 12, 56, { bas: fr(3.39), sure: 24, egim: -0.04 });
    olay(bitis(d), "tik", 0.5); not("gidiyorum daire", d.bas);
    const y1 = 625, a = yazi("-yor", { x: 48, y: y1, boyut: 64, renk: SARI, bas: fr(4.19), sure: 8, ses: true });
    not("-yor notu", a.bas);
    ok([a.x1 + 18, y1 - 24], [a.x1 + 120, y1 - 24], { bas: fr(4.19) + 6, sure: 12, w: 6, uzun: 20, bukum: 0.08 });
    const b = yazi("şimdiki zaman", { x: a.x1 + 140, y: y1, boyut: 64, renk: KRE, bas: fr(4.19) + 16, sure: 14 });
    not("şimdiki zaman", b.bas);
    await S.svgCiz("tabler/clock.svg", { kutu: [740, 548, 96, 96], bas: fr(4.63), sure: 22, azami: 25, w: 4, sesAralik: 2 });
    not("saat çizimi", fr(4.63));
    const y2 = 705;
    await S.svgCiz("tabler/calendar.svg", { kutu: [760, 650, 96, 96], bas: fr(5.15), sure: 24, azami: 25, w: 4, sesAralik: 3 });
    not("takvim çizimi", fr(5.15));
    const n1 = yazi("bu akşam", { x: 48, y: y2, boyut: 64, renk: KRE, bas: fr(5.63), sure: 10 });
    ok([n1.x1 + 18, y2 - 24], [n1.x1 + 110, y2 - 24], { bas: fr(5.63) + 6, sure: 10, w: 6, uzun: 20, bukum: 0.08 });
    yazi("gelecek", { x: n1.x1 + 130, y: y2, boyut: 64, renk: SARI, bas: fr(5.63) + 18, sure: 12, ses: true });
    not("bu akşam → gelecek", n1.bas);
  }

  // --- 6,5–8,58 faz 2: I'm going to my uncle's tonight. (Fredoka 64, tek satır 890 px) + going daire + -yor ⇄ -ing
  {
    const tl = [6.5, 6.86, 7.06, 7.22, 7.42, 7.62], kel = ["I'm", "going", "to", "my", "uncle's", "tonight."];
    const e = cumle(kel.map((s, i) => ({ s, f: fr(tl[i]) })), { x: 48, y: 1122, boyut: 64, aile: "Fredoka", agirlik: 700 });
    altCizgi(e, { tut: 40 }); not("İngilizce cümle başı", e[0].bas);
    const g = e[1], d = daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 6, 40, { bas: fr(7.62) - 8, sure: 22, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("going daire", d.bas);
    const a = yazi("-yor", { x: 700, y: 835, boyut: 110, aile: "Fredoka", agirlik: 700, renk: SARI, bas: fr(7.95), sure: 8, ses: true });
    const ar = ok([a.x0 + 80, 868], [a.x0 + 80, 940], { bas: fr(7.95) + 5, sure: 18, w: 8, cift: true, uzun: 26, bukum: 0.05 });
    yazi("-ing", { x: 700, y: 1010, boyut: 110, aile: "Fredoka", agirlik: 700, renk: SARI, bas: bitis(ar) + 4, sure: 8, ses: true });
    not("ok -yor ⇄ -ing", ar.bas);
  }

  // --- 8,73–13,6 ajanda kutusu: sol sütun saat + "6 dakikada:", sağ sütun üç madde (tik zamanlı)
  {
    S.kutu(48, 1155, 984, 237, { bas: fr(8.73) - 8, sure: 38, w: 4 }); not("kutu çizimi", fr(8.73) - 8);
    await S.svgCiz("tabler/clock.svg", { kutu: [90, 1180, 130, 130], bas: fr(8.73), sure: 22, azami: 25, w: 4, sesAralik: 3 });
    yazi("6 dakikada:", { x: 80, y: 1362, boyut: 64, renk: SARI, bas: fr(8.73) + 14, sure: 12 });
    parilti(214, 1186, { bas: fr(9.6), r: 24, periyot: 170, adet: 3 });
    const m = [["Form", 10.97, 1222], ["Zaman ifadeleri", 11.65, 1300], ["6 kullanım", 13.29, 1378]];
    for (const [s, t, y] of m) {
      yazi(s, { x: 500, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8 });
      tik(470, y - 20, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

// Sahne 02 — Kanca (PPC temel, 436 kare, t_bas 3,00; cümle 2). Zaman: yerel kare = round((t − 3,00) × 30).
import { sahneKur, RT } from "/projeler/present-perfect-cont-temel/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 436, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0 });
  const { fr, ciz, daire, ok, yazi, cumle, altCizgi, tik, parilti, olay, not, bitis, genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12;                                                    // geçiş karesi: çizimler bundan sonra başlar

  // --- cümle 1: İki saattir çalışıyorum. (Caveat 64, x 140, y 300); sesi sahne 01'de söylendi, 0–0,3 sn'de belirir
  const F64 = "700 64px Caveat";
  const c1 = cumle(["İki", "saattir", "çalışıyorum."].map((s, i) => ({ s, f: i * 3 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 başı (İki)", c1[0].bas); not("çalışıyorum", c1[2].bas);

  // --- sağ eskiz: oturan figür + dizüstü + saat
  const figOge = S.oge({ nefes: { bas: fr(7.0), cx: 1285, cy: 585 } });
  const fig = await S.svgCiz("open-peeps/sitting-5.svg", { kutu: [1120, 125, 330, 455], bas: GB, sure: 44, azami: 60, yuz: 3, w: 3.2, oge: figOge, sesAralik: 5 });
  not("figür çizimi başı", GB);
  ciz([[1090, 590], [1300, 586], [1520, 592], [1800, 588]], { w: 3, renk: IKI, alfa: 0.75, bas: 40, sure: 28, uc0: 10, uc1: 30 });
  await S.svgCiz("tabler/device-laptop.svg", { kutu: [1500, 410, 270, 180], bas: 36, sure: 30, azami: 25, w: 4, sesAralik: 2 });
  not("dizüstü çizimi", 36);
  const clk = await S.svgCiz("tabler/clock.svg", { kutu: [1560, 150, 170, 170], bas: 60, sure: 26, azami: 25, w: 4, sesAralik: 2 });
  not("saat çizimi", 60);
  parilti(1760, 150, { bas: 92, r: 24, periyot: 150, adet: 3 });

  // --- 4,91–5,43: saat-tir içindeki -dir sarı daire; not "-dir → süre"
  {
    const x1 = 140 + genislik("İki ", F64), xs = x1 + genislik("saat", F64), wt = genislik("tir", F64);
    const d = daire(xs + wt / 2, 300 - 22, wt / 2 + 12, 36, { bas: fr(4.91), sure: 14, egim: -0.04 });
    olay(bitis(d), "tik", 0.5); not("-dir daire", d.bas);
    const y1 = 380, a = yazi("-dir", { x: 140, y: y1, boyut: 48, renk: IKI, bas: fr(5.0), sure: 8 });
    ok([a.x1 + 14, y1 - 14], [a.x1 + 84, y1 - 14], { bas: fr(5.0) + 4, sure: 10, w: 5, uzun: 16, bukum: 0.08 });
    yazi("süre", { x: a.x1 + 100, y: y1, boyut: 48, renk: SARI, bas: fr(5.0) + 14, sure: 10, ses: true });
    not("not -dir → süre", a.bas);
  }
  // --- 6,91–7,95: çalış-ıyor-um içindeki -yor sarı daire; not; zaman çizgisi
  {
    const xc = c1[2].x0, xy = xc + genislik("çalışı", F64), wy = genislik("yor", F64);
    const d = daire(xy + wy / 2, 300 - 22, wy / 2 + 12, 36, { bas: fr(6.91), sure: 14, egim: 0.04 });
    olay(bitis(d), "tik", 0.5); not("-yor daire", d.bas);
    const y2 = 462, a = yazi("-yor", { x: 140, y: y2, boyut: 48, renk: IKI, bas: fr(7.0), sure: 8 });
    ok([a.x1 + 14, y2 - 14], [a.x1 + 84, y2 - 14], { bas: fr(7.0) + 4, sure: 10, w: 5, uzun: 16, bukum: 0.08 });
    yazi("iş sürüyor", { x: a.x1 + 100, y: y2, boyut: 48, renk: SARI, bas: fr(7.0) + 14, sure: 12, ses: true });
    not("not -yor → iş sürüyor", a.bas);
    // zaman çizgisi: 2 saat önce • ~~~ • now (y 570)
    const ty = 572, b0 = fr(7.35);
    ciz([[170, ty], [520, ty - 2], [880, ty]], { w: 3.4, renk: RT.murekkep, bas: b0, sure: 14, uc0: 8, uc1: 20 });
    daire(190, ty, 10, 10, { bas: b0 + 12, sure: 8, tur: 1.1, w: 5 });
    const dalga = Array.from({ length: 22 }, (_, i) => [200 + i * 31, ty - 2 + Math.sin(i * 0.9) * 7]);
    ciz(dalga, { w: 11, renk: SARI, alfa: 0.55, bas: b0 + 14, sure: 22, uc0: 10, uc1: 14, amp: 0.4 });
    daire(870, ty, 10, 10, { bas: b0 + 34, sure: 8, tur: 1.1, w: 5 });
    yazi("2 saat önce", { x: 190, y: ty + 58, boyut: 44, hizala: "orta", renk: RT.murekkep, bas: b0 + 8, sure: 8 });
    yazi("now", { x: 870, y: ty + 58, boyut: 44, hizala: "orta", renk: SARI, bas: b0 + 36, sure: 8, ses: true });
    not("zaman çizgisi", b0);
  }
  // --- 8,10–10,66: I have been working for two hours. (Fredoka 56) + daireler + çift yönlü ok
  {
    const kel = ["I", "have", "been", "working", "for", "two", "hours."];
    const tl = [8.10, 8.36, 8.66, 8.98, 9.30, 9.52, 9.74];
    const e = cumle(kel.map((s, i) => ({ s, f: fr(tl[i]) })), { x: 140, y: 730, boyut: 56, aile: "Fredoka", agirlik: 700 });
    altCizgi(e, { tut: 40 }); not("İngilizce cümle başı", e[0].bas);
    const hb = daire((e[1].x0 + e[2].x1) / 2, 730 - 20, (e[2].x1 - e[1].x0) / 2 + 10, 34, { bas: fr(9.66), sure: 16, a0: -2.0 });
    olay(bitis(hb), "tik", 0.5); not("have been daire", hb.bas);
    const w = e[3], xi = w.x0 + genislik("work", "700 56px Fredoka"), wi = genislik("ing", "700 56px Fredoka");
    const di = daire(xi + wi / 2, 730 - 20, wi / 2 + 10, 33, { bas: fr(10.0), sure: 14, a0: -2.2 });
    olay(bitis(di), "tik", 0.5); not("-ing daire", di.bas);
    const y = 820, a = yazi("-dir … -yor", { x: 140, y, boyut: 52, renk: IKI, bas: fr(10.1), sure: 10 });
    const ar = ok([a.x1 + 22, y - 16], [a.x1 + 132, y - 16], { bas: fr(10.1) + 8, sure: 18, w: 6.5, cift: true, uzun: 20, bukum: 0.05 });
    yazi("have been … -ing", { x: a.x1 + 156, y, boyut: 52, renk: SARI, bas: bitis(ar) + 4, sure: 12, ses: true });
    not("ok -dir…-yor ⇄ have been…-ing", ar.bas);
  }
  // --- 10,73–17,13: alt sağ el kutusu, saat + 6 min, 3 madde
  {
    S.kutu(1100, 700, 720, 290, { bas: fr(10.73) - 8, sure: 38 }); not("kutu çizimi", fr(10.73) - 8);
    await S.svgCiz("tabler/clock.svg", { kutu: [1136, 722, 76, 76], bas: fr(11.05), sure: 20, azami: 25, w: 3.4, sesAralik: 3 });
    yazi("6 min", { x: 1236, y: 782, boyut: 56, renk: SARI, bas: fr(11.05) + 14, sure: 12 }); not("saat + 6 min", fr(11.05));
    parilti(1216, 724, { bas: fr(12.2), r: 22, periyot: 170, adet: 3 });
    const m = [["form", 13.29, 850], ["time expressions", 14.17, 905], ["result clue", 15.61, 960]];
    for (const [s, t, y] of m) {
      yazi(s, { x: 1180, y, boyut: 44, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, bas: fr(t), sure: 8 });
      tik(1148, y - 12, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

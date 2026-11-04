// Sahne 02 — Kanca (385 kare, t_bas 3,00; cümle 2). Zamanlar eski çerçevede (t − 7,00) × 30 yazılı;
// cümle 2'den sonraki her şey fr() ile 60 kare (2,0 sn) öne alınır (K23 sıkıştırma, 04.11).
import { sahneKur, RT } from "/projeler/present-continuous/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 385, T_BAS = 7.0, KAYMA = 6.0;   // T_BAS: eski çerçeve; zaman.json t_bas 3,00

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: KAYMA });
  const { fr: fr0, ciz, daire, ok, yazi, cumle, altCizgi, tik, parilti, olay, not, bitis } = S;
  const fr = (t) => fr0(t) - 60;                                    // cümle 2 sonrası: 2,0 sn öne
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12;                                                    // geçiş karesi: çizimler bundan sonra başlar

  // --- cümle 1: Bu akşam amcamlara gidiyorum. (Caveat 64, x 140, y 300). Sesi sahne 01'de söylendi;
  // yazı sahne başında hazır sayılır: 0–0,4 sn'de hızlı belirir (kare 0, 3, 6, 9).
  const c1 = cumle(["Bu", "akşam", "amcamlara", "gidiyorum."].map((s, i) => ({ s, f: i * 3 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 başı (Bu)", c1[0].bas); not("gidiyorum", c1[3].bas);

  // --- sağ eskiz: ev + yürüyen figür + hilal
  const ev = await S.svgCiz("tabler/home.svg", { kutu: [1330, 190, 260, 260], bas: GB, sure: 26, azami: 25, w: 4, sesAralik: 2 });
  const figOge = S.oge({ kay: { f0: GB, f1: fr0(8.8), dx: 70 }, nefes: { bas: fr0(8.9), cx: 1190, cy: 450 } });
  const fig = await S.svgCiz("open-peeps/standing-2.svg", { kutu: [1090, 120, 190, 330], bas: GB, sure: 42, azami: 60, yuz: 3, w: 3.2, oge: figOge, sesAralik: 5, ayna: false });
  not("ev çizimi başı", GB); not("figür çizimi başı", GB); not("figür yürüme biter", fr0(8.8));
  ciz([[1040, 456], [1220, 452], [1420, 457], [1650, 453]], { w: 3, renk: IKI, alfa: 0.75, bas: 36, sure: 30, uc0: 10, uc1: 30 });
  {   // hilal: dış yay + iç yay tek darbe (el elipsi)
    const C = [1730, 240], R = 56, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 6) pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 6) pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    const h = ciz(pts, { w: 4, alfa: 0.92, bas: fr0(8.0), sure: 30, uc0: 12, uc1: 20, amp: 0.7 }); not("hilal çizimi başı", h.bas);
    parilti(C[0] + 40, C[1] - 52, { bas: bitis(h) + 2, r: 24, periyot: 150, adet: 3 });
  }

  // --- 9,39–12,35: gidiyorum sarı daire, Caveat not, ok -> takvim
  {
    const g = c1[3], d = daire((g.x0 + g.x1) / 2 + 3, g.y - 24, g.w / 2 + 6, 36, { bas: fr(9.39), sure: 24, egim: -0.04 });
    olay(bitis(d), "tik", 0.5); not("gidiyorum daire", d.bas);
    const y1 = 372, a = yazi("-yor", { x: 140, y: y1, boyut: 48, renk: IKI, bas: fr(10.19), sure: 8 });
    ok([a.x1 + 14, y1 - 14], [a.x1 + 84, y1 - 14], { bas: fr(10.19) + 4, sure: 10, w: 5, uzun: 16, bukum: 0.08 });
    const b = yazi("şimdiki zaman", { x: a.x1 + 100, y: y1, boyut: 48, renk: IKI, bas: fr(10.19) + 16, sure: 14 }); not("not -yor → şimdiki zaman", a.bas);
    ok([b.x1 + 26, y1 - 12], [b.x1 + 112, y1 - 6], { bas: fr(11.0), sure: 12, w: 5, uzun: 18, bukum: 0.1 });
    await S.svgCiz("tabler/calendar.svg", { kutu: [b.x1 + 130, 336, 88, 88], bas: fr(11.15), sure: 24, azami: 25, w: 3.4, sesAralik: 3 });
    not("takvim çizimi", fr(11.15));
    const y2 = 470, n1 = yazi("bu akşam", { x: 520, y: y2, boyut: 48, renk: IKI, bas: fr(11.63), sure: 10 });
    ok([n1.x1 + 14, y2 - 14], [n1.x1 + 84, y2 - 14], { bas: fr(11.63) + 6, sure: 10, w: 5, uzun: 16, bukum: 0.08 });
    yazi("gelecek", { x: n1.x1 + 100, y: y2, boyut: 48, renk: SARI, bas: fr(11.63) + 18, sure: 12, ses: true }); not("not bu akşam → gelecek", n1.bas);
  }

  // --- 12,50–14,58: I'm going to my uncle's tonight. (Fredoka 56 krem)
  {
    const tl = [12.5, 12.86, 13.06, 13.22, 13.42, 13.62], kel = ["I'm", "going", "to", "my", "uncle's", "tonight."];
    const e = cumle(kel.map((s, i) => ({ s, f: fr(tl[i]) })), { x: 140, y: 570, boyut: 56, aile: "Fredoka", agirlik: 700 });
    altCizgi(e, { tut: 30 }); not("İngilizce cümle başı", e[0].bas);
    const g = e[1], d = daire((g.x0 + g.x1) / 2, g.y - 20, g.w / 2 + 3, 33, { bas: fr(13.62) - 8, sure: 22, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("going daire", d.bas);
    const y = 668, a = yazi("-yor", { x: 140, y, boyut: 52, renk: IKI, bas: fr(13.95), sure: 8 });
    const ar = ok([a.x1 + 22, y - 16], [a.x1 + 132, y - 16], { bas: fr(13.95) + 5, sure: 18, w: 6.5, cift: true, uzun: 20, bukum: 0.05 });
    yazi("-ing", { x: a.x1 + 156, y, boyut: 52, renk: SARI, bas: bitis(ar) + 4, sure: 8, ses: true }); not("ok -yor ⇄ -ing", ar.bas);
  }

  // --- 14,73–20,89: el kutusu, saat, 3 madde
  {
    S.kutu(1060, 690, 760, 280, { bas: fr(14.73) - 8, sure: 38 }); not("kutu çizimi", fr(14.73) - 8);
    await S.svgCiz("tabler/clock.svg", { kutu: [1096, 712, 76, 76], bas: fr(14.73), sure: 20, azami: 25, w: 3.4, sesAralik: 3 });
    yazi("6 min", { x: 1196, y: 772, boyut: 56, renk: SARI, bas: fr(14.73) + 14, sure: 12 }); not("saat + 6 min", fr(14.73));
    parilti(1176, 714, { bas: fr(15.9), r: 22, periyot: 170, adet: 3 });
    const m = [["form", 16.97, 835], ["time expressions", 17.65, 890], ["6 uses", 19.29, 945]];
    for (const [s, t, y] of m) {
      yazi(s, { x: 1140, y, boyut: 44, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, bas: fr(t), sure: 8 });
      tik(1108, y - 12, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

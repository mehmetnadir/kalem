// Sahne 02 (D1, dikey) — Kanca (431 kare, t_bas 3,00; cümle 2 sonu + cümle 3). Yerel kare = round((t − 3,00) × 30).
// İlk 12 kare (geçiş altı) boş: yalnız künye. Önceden konuşulmuş sözcükler 12. kareden hızlı belirir.
import { sahneKur, RT } from "/projeler/present-continuous-d1/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 431, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, ciz, daire, ok, yazi, cumle, altCizgi, tik, parilti, olay, not, bitis } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  const GB = 12;                                                   // geçiş karesi: çizimler bundan sonra başlar
  const f2 = (t) => Math.max(GB, fr(t));

  // --- TR cümle (Caveat 70, x 64, y 400): sahne başında konuşulmuş sözcükler hızlı belirir
  const w2 = [["Bu", 2.27], ["akşam", 2.51], ["amcamlara", 2.83], ["gidiyorum.", 3.35]];
  const c1 = cumle(w2.map(([s, t], i) => ({ s, f: Math.max(GB + i * 3, fr(t)) })),
    { x: 64, y: 400, boyut: 70, aile: "Caveat", agirlik: 700 });
  not("cümle başı (Bu)", c1[0].bas); not("gidiyorum", c1[3].bas);

  // --- eskiz bölgesi (y 590-870): ev + yürüyen figür + zemin çizgisi
  await S.svgCiz("tabler/home.svg", { kutu: [770, 610, 240, 240], bas: GB, sure: 26, azami: 25, w: 4, sesAralik: 1 });
  const figOge = S.oge({ kay: { f0: GB, f1: fr(9.0), dx: 560 }, nefes: { bas: fr(9.1), cx: 600, cy: 870 } });
  await S.svgCiz("open-peeps/standing-2.svg", { kutu: [96, 590, 170, 280], bas: GB, sure: 42, azami: 60, yuz: 3,
    w: 3.2, oge: figOge, sesAralik: 3, ayna: false });
  ciz([[60, 874], [300, 870], [560, 876], [800, 872], [1020, 875]],
    { w: 3, renk: IKI, alfa: 0.75, bas: 36, sure: 30, uc0: 10, uc1: 30 });
  not("ev + figür çizimi başı", GB);

  // --- gidiyorum sarı daire (3,75), -yor notu (4,90), ok, "şimdiki zaman" (7,21) + saat
  {
    const g = c1[3], d = daire((g.x0 + g.x1) / 2, g.y - 24, g.w / 2 + 8, 44, { bas: fr(3.75), sure: 22, egim: -0.04 });
    olay(bitis(d), "tik", 0.5); not("gidiyorum daire", d.bas);
    const y1 = 520, a = yazi("-yor", { x: 64, y: y1, boyut: 64, renk: SARI, bas: fr(4.90), sure: 8, ses: true });
    not("-yor notu", a.bas);
    const ar = ok([a.x1 + 18, y1 - 20], [a.x1 + 120, y1 - 20], { bas: fr(6.6), sure: 12, w: 5.5, uzun: 18, bukum: 0.08 });
    const b = yazi("şimdiki zaman", { x: a.x1 + 140, y: y1, boyut: 60, renk: IKI, bas: fr(7.21), sure: 14 });
    not("şimdiki zaman", b.bas);
    await S.svgCiz("tabler/clock.svg", { kutu: [900, 440, 100, 100], bas: fr(7.93), sure: 22, azami: 25, w: 3.4, sesAralik: 2 });
    parilti(985, 450, { bas: fr(9.0), r: 22, periyot: 150, adet: 2 });
    void ar;
  }

  // --- 9,9-10,8 EN cümle için el çizimi kutu; 11,53'ten cümle sözcük sözcük
  {
    const kb = S.kutu(48, 930, 984, 230, { bas: fr(9.9), sure: 36, w: 3.6 }); not("kutu çizimi", fr(9.9));
    void kb;
    const tl = [11.53, 11.65, 11.77, 11.97, 12.09, 12.25, 12.77];
    const kel = ["I", "am", "going", "to", "my", "uncle's", "tonight."];
    const e = cumle(kel.map((s, i) => ({ s, f: fr(tl[i]), satir: i < 5 ? 0 : 1 })),
      { x: 100, y: 1030, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 92 });
    altCizgi(e, { tut: 40 }); not("İngilizce cümle başı", e[0].bas);
    const g = e[2], d = daire((g.x0 + g.x1) / 2, g.y - 20, g.w / 2 + 4, 36, { bas: fr(13.1), sure: 22, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("going daire", d.bas);
  }

  // --- 14,02-16,5 "aynı plan": -yor ⇄ -ing bağ çizgisi
  {
    const y = 1290;
    yazi("aynı plan", { x: 64, y: 1225, boyut: 60, renk: IKI, bas: fr(14.02), sure: 12 });
    const a = yazi("-yor", { x: 200, y, boyut: 72, renk: SARI, bas: fr(14.98), sure: 8, ses: true });
    const ar = ok([a.x1 + 24, y - 24], [a.x1 + 190, y - 24], { bas: fr(15.38), sure: 18, w: 6.5, cift: true, uzun: 22, bukum: 0.05 });
    yazi("-ing", { x: a.x1 + 220, y, boyut: 72, renk: SARI, bas: fr(15.7), sure: 8, ses: true });
    not("bağ -yor ⇄ -ing", ar.bas);
  }
  return S;
}

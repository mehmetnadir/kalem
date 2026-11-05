// Sahne 02 (DİKEY 1080x1920) — Kanca (385 kare, t_bas 3,00; cümle 2).
// Zamanlar KÜRESEL sn (sozcukler.json); yerel kare = round((t − 3,00) × 30).
// Cümle 1 ses olarak sahne 01'de söylendi: burada 0. kareden hazır durur.
// Telefon ölçeği: figür kutusu ≥ 420 px (küçültülmez, sol sütunda sabit 500 px).
// Kart tek satır: "Bu akşam amcamlara gidiyorum." (Caveat 76).
// Sağ sütunda faz 1'de ev + hilal, faz 2'de -yor ⇄ -ing + ajanda kutusu
// (6 dakikada: Form / Zaman ifadeleri / 6 kullanım).
import { sahneKur, RT }
  from "/projeler/present-continuous-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 385, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, ciz, daire, ok, yazi, cumle, altCizgi, tik, parilti, olay, not, bitis } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep, IKI = RT.ikincil;
  const GB = 12; // geçiş karesi: çizimler bundan sonra başlar

  // --- Cümle 1: kart tek satır (kutu 48..1032, y 364..464, h 100 px); Caveat 76 tek satır
  S.kutu(48, 364, 984, 100, { bas: -8, sure: 1, w: 4, renk: IKI });
  const c1 = cumle(
    [["Bu", 0], ["akşam", 0], ["amcamlara", 0], ["gidiyorum.", 0]]
      .map(([s, satir]) => ({ s, f: -8, satir })),
    { x: 74, y: 432, boyut: 76, aile: "Caveat", agirlik: 700 });
  not("cümle 1 hazır (kare 0)", 0);

  // --- SOL SÜTUN: Figür baştan sona sabit (kutu h=500 px ≥ 420 px, KÜÇÜLME YOK)
  const figOge = S.oge({ nefes: { bas: 110, cx: 195, cy: 1280 } });
  await S.svgCiz("open-peeps/standing-2.svg", {
    kutu: [60, 780, 270, 500], bas: GB, sure: 48, azami: 60, yuz: 3,
    w: 4.4, oge: figOge, sesAralik: 4, ayna: false });
  ciz([[48, 1280], [180, 1278], [340, 1280]],
    { w: 4, renk: IKI, alfa: 0.8, bas: 36, sure: 24, uc0: 10, uc1: 20, oge: figOge });
  not("figür çizimi başı", GB);

  // --- SAĞ SÜTUN FAZ 1 (3,0–6,5 sn): Ev + hilal
  // (t=6.5 sonrası solarak yerini ajandaya bırakır)
  const evOge = S.oge({ alfa: (f) => f < fr(6.5) ? 1 : Math.max(0, 1 - (f - fr(6.5)) / 20) });
  await S.svgCiz("tabler/home.svg", {
    kutu: [500, 810, 420, 420], bas: GB, sure: 32, azami: 25, w: 4, sesAralik: 2, oge: evOge
  });
  {   // hilal: dış yay + iç yay tek darbe
    const C = [860, 760], R = 44, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 6) {
      pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    }
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 6) {
      pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    }
    const h = ciz(pts, {
      w: 4.4, alfa: 0.92, bas: 24, sure: 28, uc0: 12, uc1: 20, amp: 0.7, oge: evOge
    });
    not("hilal çizimi", h.bas);
    parilti(C[0] + 30, C[1] - 36, { bas: bitis(h) + 2, r: 24, periyot: 150, adet: 1 });
  }

  // --- 3,39 gidiyorum sarı daire; 4,19 -yor → şimdiki zaman + saat;
  // 5,15 takvim; 5,63 bu akşam → gelecek
  {
    const g = c1[3],
      d = daire((g.x0 + g.x1) / 2, g.y - 24, g.w / 2 + 10, 52, {
        bas: fr(3.39), sure: 24, egim: -0.04
      });
    olay(bitis(d), "tik", 0.5); not("gidiyorum daire", d.bas);
    const y1 = 524,
      a = yazi("-yor", { x: 74, y: y1, boyut: 64, renk: SARI, bas: fr(4.19), sure: 8, ses: true });
    not("-yor notu", a.bas);
    ok([a.x1 + 18, y1 - 24], [a.x1 + 110, y1 - 24], {
      bas: fr(4.19) + 6, sure: 12, w: 6, uzun: 20, bukum: 0.08
    });
    const b = yazi("şimdiki zaman", {
      x: a.x1 + 130, y: y1, boyut: 64, renk: KRE, bas: fr(4.19) + 16, sure: 14
    });
    not("şimdiki zaman", b.bas);
    await S.svgCiz("tabler/clock.svg", {
      kutu: [760, y1 - 62, 76, 76], bas: fr(4.63), sure: 22, azami: 25, w: 4, sesAralik: 2
    });
    not("saat çizimi", fr(4.63));
    const y2 = 598;
    await S.svgCiz("tabler/calendar.svg", {
      kutu: [760, y2 - 62, 76, 76], bas: fr(5.15), sure: 24, azami: 25, w: 4, sesAralik: 3
    });
    not("takvim çizimi", fr(5.15));
    const n1 = yazi("bu akşam", { x: 74, y: y2, boyut: 64, renk: KRE, bas: fr(5.63), sure: 10 });
    ok([n1.x1 + 18, y2 - 24], [n1.x1 + 110, y2 - 24], {
      bas: fr(5.63) + 6, sure: 10, w: 6, uzun: 20, bukum: 0.08
    });
    yazi("gelecek", {
      x: n1.x1 + 130, y: y2, boyut: 64, renk: SARI, bas: fr(5.63) + 18, sure: 12, ses: true
    });
    not("bu akşam → gelecek", n1.bas);
  }

  // --- 6,5–8,58 FAZ 2: I'm going to my uncle's tonight. (Fredoka 64 tek satır)
  // + going daire + -yor ⇄ -ing
  {
    const tl = [6.5, 6.86, 7.06, 7.22, 7.42, 7.62],
      kel = ["I'm", "going", "to", "my", "uncle's", "tonight."];
    const e = cumle(
      kel.map((s, i) => ({ s, f: fr(tl[i]) })),
      { x: 74, y: 686, boyut: 64, aile: "Fredoka", agirlik: 700 }
    );
    altCizgi(e, { tut: 40 }); not("İngilizce cümle başı", e[0].bas);
    const g = e[1],
      d = daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 6, 40, {
        bas: fr(7.62) - 8, sure: 22, a0: -2.0
      });
    olay(bitis(d), "tik", 0.5); not("going daire", d.bas);

    // Sağ sütun üstünde: -yor ⇄ -ing (yatay ok ile)
    const yIng = 785;
    const a = yazi("-yor", {
      x: 420, y: yIng, boyut: 76, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: fr(7.95), sure: 8, ses: true
    });
    const ar = ok([a.x1 + 18, yIng - 26], [a.x1 + 120, yIng - 26], {
      bas: fr(7.95) + 5, sure: 16, w: 7, cift: true, uzun: 22, bukum: 0.05
    });
    yazi("-ing", {
      x: a.x1 + 140, y: yIng, boyut: 76, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: bitis(ar) + 4, sure: 8, ses: true
    });
    not("ok -yor ⇄ -ing", ar.bas);
  }

  // --- 8,73–13,6 AJANDA KUTUSU: sağ sütunda x 370..1032, y 835..1280
  // Saat + "6 dakikada:" üst satırda yan yana;
  // maddeler x 450'den başlar (en geniş madde ≤ 1032)
  {
    S.kutu(370, 835, 662, 445, { bas: fr(8.73) - 8, sure: 36, w: 4 });
    not("kutu çizimi", fr(8.73) - 8);
    await S.svgCiz("tabler/clock.svg", {
      kutu: [405, 868, 110, 110], bas: fr(8.73), sure: 22, azami: 25, w: 4, sesAralik: 3
    });
    yazi("6 dakikada:", { x: 535, y: 940, boyut: 64, renk: SARI, bas: fr(8.73) + 14, sure: 12 });
    parilti(510, 885, { bas: fr(9.6), r: 24, periyot: 170, adet: 3 });
    const m = [
      ["Form", 10.97, 1060], ["Zaman ifadeleri", 11.65, 1155], ["6 kullanım", 13.29, 1250]
    ];
    for (const [s, t, y] of m) {
      yazi(s, {
        x: 450, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8
      });
      tik(410, y - 22, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

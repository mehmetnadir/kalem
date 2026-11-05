// Sahne 02 — Kanca, DİKEY 1080x1920 (366 kare, t_bas 3,00; cümle 2 = 3,39–14,25).
// Bantlar: içerik 352–1392 · altyazı 1400–1536 (kalem-paper.js çizer) · platform boş.
// Yerleşim: solda figür (440 px sabit), sağda ev (8,05'te solar) →
// saat + ajanda kartı (360–1032);
// alt bantta İngilizce cümle + -di ⇄ -ed. Figür hiç küçülmez.
import {
  sahneKur, RT
} from "/projeler/simple-past-temel-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 366, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook" });
  const {
    fr, ciz, daire, ok, yazi, cumle, altCizgi, tik, parilti, olay, not, bitis, kutu, genislik
  } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const GB = 12; // geçiş karesi: çizimler bundan sonra

  // --- cümle 1 (Caveat 80, iki satır, taban y 450 / 540): sahne 01'den devam;
  // 0–0,4 sn'de hazır belirir
  const c1 = cumle(
    ["Dün", "akşam", "amcamlara", "gittim."].map((s, i) => ({
      s, f: i * 3, satir: i < 3 ? 0 : 1
    })),
    { x: 56, y: 450, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 90 }
  );
  not("cümle 1 başı (Dün)", c1[0].bas); not("gittim.", c1[3].bas);

  // --- orta bant sol sütun: ayakta figür 440 px (baştan sona sabit, hiç küçülmez)
  const figOge = S.oge({
    kay: { f0: GB, f1: fr(7.2), dx: 40 },
    nefes: { bas: fr(7.3), cx: 190, cy: 1190 }
  });
  await S.svgCiz("open-peeps/standing-2.svg", { kutu: [60, 760, 260, 440], bas: GB, sure: 42,
    azami: 60, yuz: 3, w: 4.4, oge: figOge, sesAralik: 5 });
  not("figür çizimi başı", GB); not("figür yürüme biter", fr(7.2));
  ciz([[48, 1200], [330, 1195]], {
    w: 3.6, renk: IKI, alfa: 0.75, bas: 36, sure: 24, uc0: 10, uc1: 20
  });

  // --- orta bant sağ sütun: ev + hilal (8,05'te solar, yerini saat + ajandaya bırakır)
  const evGrup = S.oge({
    alfa: (f) => (f < fr(8.05) ? 1 : Math.max(0, 1 - (f - fr(8.05)) / 15))
  });
  await S.svgCiz("tabler/home.svg", { kutu: [430, 800, 380, 380], bas: GB, sure: 26, azami: 25,
    w: 4, sesAralik: 2, oge: evGrup });
  not("ev çizimi başı", GB);
  ciz([[330, 1195], [700, 1200], [1030, 1195]], { w: 3.6, renk: IKI, alfa: 0.75, bas: 36,
    sure: 30, uc0: 10, uc1: 30, oge: evGrup });
  {   // hilal: dış yay + iç yay tek darbe (el elipsi)
    const C = [930, 850], R = 66, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 6) {
      pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    }
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 6) {
      pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    }
    const h = ciz(pts, {
      w: 5, alfa: 0.92, bas: fr(4.2), sure: 30, uc0: 12, uc1: 20, amp: 0.7, oge: evGrup
    });
    not("hilal çizimi başı", h.bas);
    parilti(C[0] + 46, C[1] - 60, { bas: bitis(h) + 2, r: 28, periyot: 60, adet: 2, oge: evGrup });
  }

  // --- 3,39–5,87: gittim sarı daire; -di sarı kutu (4,83);
  // ok → biten iş; ok → takvim + dün (taban y 650)
  {
    const g = c1[3], d = daire((g.x0 + g.x1) / 2 + 3, g.y - 28, g.w / 2 + 10, 46,
      { bas: fr(3.39), sure: 24, egim: -0.04, w: 10 });
    olay(bitis(d), "tik", 0.5); not("gittim daire", d.bas);
    const y1 = 650, a = yazi("-di", {
      x: 76, y: y1, boyut: 72, renk: MUR, bas: fr(4.83), sure: 8, ses: true
    });
    kutu(a.x0 - 18, y1 - 60, a.w + 36, 84, { bas: fr(4.83) + 6, sure: 14, w: 8, renk: SARI });
    not("-di sarı kutu", fr(4.83));
    const o1 = ok([a.x1 + 30, y1 - 20], [a.x1 + 112, y1 - 20],
      { bas: fr(4.83) + 20, sure: 10, w: 9, uzun: 22, bukum: 0.08 });
    const b = yazi("biten iş", {
      x: a.x1 + 130, y: y1, boyut: 64, renk: MUR, bas: bitis(o1) + 2, sure: 12
    });
    not("biten iş", b.bas);
    const o2 = ok([b.x1 + 26, y1 - 16], [b.x1 + 104, y1 - 10],
      { bas: fr(5.45), sure: 10, w: 9, uzun: 22, bukum: 0.1 });
    await S.svgCiz("tabler/calendar.svg", { kutu: [b.x1 + 122, y1 - 84, 100, 100], bas: bitis(o2),
      sure: 20, azami: 25, w: 4, sesAralik: 3 });
    yazi("dün", {
      x: b.x1 + 244, y: y1, boyut: 64, renk: SARI, bas: bitis(o2) + 16, sure: 10, ses: true
    });
    not("takvim + dün", bitis(o2));
  }

  // --- 6,02–8,10: I visited my uncle last night.
  // (Fredoka 64, iki satır, taban 1310 / 1376); -ed daire; -di ⇄ -ed
  {
    const tl = [6.02, 6.30, 6.62, 6.78, 7.10, 7.44];
    const kel = ["I", "visited", "my", "uncle", "last", "night."];
    const e = cumle(kel.map((s, i) => ({ s, f: fr(tl[i]), satir: i < 4 ? 0 : 1 })),
      { x: 56, y: 1310, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 66 });
    altCizgi(e, { tut: 40, w: 9 }); not("İngilizce cümle başı", e[0].bas);
    const v = e[1], font = "700 64px Fredoka";
    const wv = genislik("visit", font), we = genislik("ed", font);
    const d = daire(v.x0 + wv + we / 2, v.y - 22, we / 2 + 8, 36, {
      bas: fr(6.90) - 6, sure: 18, a0: -2.0, w: 9
    });
    olay(bitis(d), "tik", 0.5); not("-ed daire", d.bas);
    const y = 1376, a = yazi("-di", { x: 540, y, boyut: 64, renk: MUR, bas: fr(7.14), sure: 8 });
    const ar = ok([a.x1 + 24, y - 20], [a.x1 + 130, y - 20],
      { bas: fr(7.14) + 5, sure: 18, w: 9, cift: true, uzun: 24, bukum: 0.05 });
    yazi("-ed", {
      x: a.x1 + 154, y, boyut: 64, renk: SARI, bas: bitis(ar) + 4, sure: 8, ses: true
    });
    not("ok -di ⇄ -ed", ar.bas);
  }

  // --- 8,25–14,25: sağ sütun: saat (6 min) + ajanda kartı (3 madde);
  // figür sol sütunda tam boy kalır
  {
    await S.svgCiz("tabler/clock.svg", { kutu: [380, 750, 110, 110], bas: fr(8.57), sure: 20,
      azami: 25, w: 4.4, sesAralik: 3 });
    yazi("6 min", { x: 510, y: 835, boyut: 84, renk: SARI, bas: fr(8.57) + 14, sure: 12 });
    not("saat + 6 min", fr(8.57));
    parilti(680, 750, { bas: fr(9.6), r: 26, periyot: 170, adet: 3 });
    kutu(360, 880, 672, 330, { bas: fr(9.7), sure: 30, w: 4 }); not("kart çizimi", fr(9.7));
    const m = [
      ["form", 10.17, 955], ["time expressions", 11.29, 1045], ["irregular verbs", 13.01, 1135]
    ];
    for (const [s, t, y] of m) {
      yazi(s, {
        x: 440, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: MUR, bas: fr(t), sure: 8
      });
      tik(395, y - 22, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

// Sahne 02 — Örnek (DİKEY 1080x1920, 478 kare, t_bas 3,00; cümle 1 devamı + cümle 2).
// Sahne 01'in son hali (HUD + iki Caveat satırı) kare 0'da hazır; zamanlar küresel sn, fr(t) = round((t - 3,00) x 30).
import { sahneKur, RT } from "/projeler/present-continuous-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 478, T_BAS = 3.0;
const CIP = "BU AKŞAM = I AM GOING";

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: CIP });
  const { fr, ciz, daire, yazi, cumle, tik, parilti, olay, not, bitis, kutu, genislik } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil;
  const GB = 12;                                                    // geçiş karesi: çizimler bundan sonra başlar
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 10], [z.x1 + 4, z.y + 7]],
    { w: 8, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, ...o });

  // --- cümle 1 (sahne 01'in son hali, hazır): Caveat 64, x 72, y 430 / 505
  const tr1 = cumle(s1.slice(0, 3).map((w) => ({ s: w.s, f: -30 })), { x: 72, y: 430, boyut: 64, aile: "Caveat", agirlik: 700 });
  const en1 = cumle(s1.slice(3, 7).map((w) => ({ s: w.s, f: -30 })), { x: 72, y: 505, boyut: 64, aile: "Caveat", agirlik: 700 });
  const going1 = en1[2];
  altCiz(going1, fr(3.0) + 14); not("going altı çizgi (cümle 1)", fr(3.0) + 14);

  // --- 4,38–7,74: "İki dilde de şimdiki zaman, ama gelecek demek." (Caveat 46 ikincil, 2 satır)
  {
    const w = s1.slice(7);                                           // 8 sözcük
    const e = cumle(w.map((k, i) => ({ s: k.s, f: k.f, satir: i < 5 ? 0 : 1 })),
      { x: 72, y: 600, boyut: 46, aile: "Caveat", agirlik: 700, renk: IKI, aralik: 60 });
    not("TR not başı", e[0].bas);
    altCiz(e[3], e[3].bas + 2, { w: 7 }); not("şimdiki altı çizgi", e[3].bas + 2);          // şimdiki
    const d = daire((e[6].x0 + e[6].x1) / 2, e[6].y - 16, e[6].w / 2 + 8, 28, { bas: e[6].bas + 3, sure: 20, egim: -0.05 });
    olay(bitis(d), "tik", 0.5); not("gelecek daire", d.bas);
  }

  // --- 8,2–10,6: sağ üst eskiz: figür + ev + hilal (cümle 2 anlatılırken çizilir)
  const f0 = fr(8.3);
  const fig = await S.svgCiz("open-peeps/standing-3.svg", { kutu: [690, 318, 120, 270], bas: f0, sure: 50, azami: 60, yuz: 3, w: 3.0,
    oge: S.oge({ nefes: { bas: f0 + 70, cx: 750, cy: 590 } }), sesAralik: 5 });
  await S.svgCiz("tabler/home.svg", { kutu: [850, 395, 160, 160], bas: fr(9.0), sure: 24, azami: 25, w: 3.6, sesAralik: 2 });
  ciz([[650, 592], [780, 590], [900, 593], [1020, 591]], { w: 3, renk: IKI, alfa: 0.75, bas: f0 + 6, sure: 30, uc0: 10, uc1: 30 });
  {   // hilal (akşam): dış yay + iç yay tek darbe
    const C = [968, 340], R = 34, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 8) pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 8) pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    const h = ciz(pts, { w: 3.6, alfa: 0.92, bas: fr(9.9), sure: 24, uc0: 10, uc1: 16, amp: 0.6 }); not("hilal çizimi", h.bas);
    parilti(C[0] + 30, C[1] - 34, { bas: bitis(h) + 2, r: 18, periyot: 140, adet: 3 });
  }
  not("figür çizimi başı", f0); not("ev çizimi başı", fr(9.0));

  // --- 8,0–12,6: kart: I'm going to my uncle's tonight. / Bu akşam amcamlara gidiyorum.
  kutu(48, 705, 984, 220, { bas: fr(8.0) - 8, sure: 36, renk: IKI }); not("kart kutusu", fr(8.0) - 8);
  {
    const en = s2.slice(0, 6), metin = en.map((k) => k.s).join(" ");
    const boyut = Math.min(54, Math.floor(54 * 880 / genislik(metin, "700 54px Fredoka")));
    const w = genislik(metin, `700 ${boyut}px Fredoka`), x = 72 + (936 - w) / 2;
    const e = cumle(en.map((k) => ({ s: k.s, f: k.f })), { x, y: 802, boyut, aile: "Fredoka", agirlik: 700 });
    not("EN cümle başı", e[0].bas);
    const g = e[1], d = daire((g.x0 + g.x1) / 2, g.y - boyut * 0.36, g.w / 2 + 4, 30, { bas: g.bas + 6, sure: 20, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("going daire", d.bas);
    const tr = s2.slice(6, 10), tm = tr.map((k) => k.s).join(" ");
    const tw = genislik(tm, "700 50px Caveat"), tx = 72 + (936 - tw) / 2;
    const t = cumle(tr.map((k) => ({ s: k.s, f: k.f })), { x: tx, y: 884, boyut: 50, aile: "Caveat", agirlik: 700, renk: IKI });
    altCiz(t[3], t[3].bas + 4, { w: 7 }); not("gidiyorum altı çizgi", t[3].bas + 4);
  }

  // --- 12,77–14,6: formül: go + -ing  (Fiil artı -ing)
  {
    const bz = 112, f = "700 " + bz + "px Fredoka", gw = genislik("go", f), pw = genislik("+", f), iw = genislik("-ing", f), bos = 38;
    const top = gw + pw + iw + 2 * bos, x0 = (1080 - top) / 2, y = 1088;
    kutu(110, 955, 860, 200, { bas: fr(12.77) - 10, sure: 34, renk: IKI }); not("formül kutusu", fr(12.77) - 10);
    const a = yazi("go", { x: x0, y, boyut: bz, aile: "Fredoka", agirlik: 700, bas: fr(12.77), sure: 8, olcek: true, ses: "tik" });
    yazi("+", { x: a.x1 + bos, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(13.33), sure: 6, olcek: true, ses: "tik" });
    const b = yazi("-ing", { x: a.x1 + 2 * bos + pw, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: SARI, bas: fr(13.73), sure: 8, olcek: true });
    olay(b.bas, "vurus", 0.8); not("go", a.bas); not("-ing (sarı)", b.bas);
    altCiz(b, b.bas + 8, { w: 10 }); parilti(b.x1 + 18, y - 98, { bas: b.bas + 10, r: 22, periyot: 130, adet: 2 });
  }

  // --- 14,61–17,4: önüne am · is · are (üç hap, sırayla tik)
  {
    yazi("önüne gelir:", { x: 122, y: 1198, boyut: 46, renk: IKI, bas: fr(14.61), sure: 12 }); not("önüne gelir", fr(14.61));
    const pil = [["am", 15.41], ["is", 16.05], ["are", 17.09]];
    pil.forEach(([s, t], i) => {
      const x = 122 + i * 293, y = 1224, w = 250, h = 100;
      kutu(x, y, w, h, { bas: fr(t) - 14, sure: 20, renk: IKI, w: 3.6 });
      yazi(s, { x: x + w / 2, y: y + 70, boyut: 64, aile: "Fredoka", agirlik: 700, hizala: "orta", bas: fr(t), sure: 8, olcek: true });
      tik(x + w - 44, y + 52, { bas: fr(t) + 8 }); not("hap " + s, fr(t));
    });
  }
  return S;
}

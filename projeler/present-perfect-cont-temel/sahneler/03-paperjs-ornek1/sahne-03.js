// Sahne 03 — Örnek 1 (PPC temel, 467 kare, t_bas 17,13; cümle 3). Zamanlar BRIEF §4 (küresel sn);
// yerel kare = round((t − 17,13) × 30). Sözcük zamanları sozcukler.json'dan, kayma yok.
import { sahneKur, RT, renkCoz } from "/projeler/present-perfect-cont-temel/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 467, T_BAS = 17.13;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1 });
  const { fr, ciz, daire, yazi, cumle, altCizgi, parilti, olay, not, bitis, dinamik, genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;

  // --- 17,68–18,64: büyük el çizimi daire içinde 1 (x 200, y 190)
  const d1 = daire(200, 190, 66, 62, { bas: fr(17.68), sure: 20, a0: -2.6 }); olay(bitis(d1), "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 226, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700, bas: fr(17.68) + 4,
    sure: 10, olcek: true });

  // --- 18,89–21,93: cümle (Fredoka 64, x 140, y 320, 2 satır), sözcük sözcük + sarı alt çizgi
  const sz = S.sozcukler(3).slice(2, 12);                          // I … minutes.
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: i < 5 ? 0 : 1 })),
    { x: 140, y: 320, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 80 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (I)", cz[0].bas); not("minutes", cz[9].bas);

  // --- 18,89–21,93: sağda bekleyen figür (sitting-4) + otobüs (440 px) + küçük saat
  const figOge = S.oge({ nefes: { bas: fr(22.0), cx: 1250, cy: 640 } });
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [1080, 170, 340, 470], bas: fr(18.9),
    sure: fr(20.7) - fr(18.9), azami: 60, yuz: 3, w: 3.2, oge: figOge, sesAralik: 5 });
  not("figür çizimi başı", fr(18.9));
  await S.svgCiz("tabler/bus.svg", { kutu: [1430, 190, 430, 430], bas: fr(20.1), sure: 30, azami: 25, w: 4,
    sesAralik: 2 });
  not("otobüs çizimi", fr(20.1));
  await S.svgCiz("tabler/clock.svg", { kutu: [1560, 690, 190, 190], bas: fr(21.2), sure: 22, azami: 25, w: 4,
    sesAralik: 2 });
  not("saat çizimi", fr(21.2));
  parilti(1760, 700, { bas: fr(21.9), r: 24, periyot: 170, adet: 3 });

  // --- 20,41–21,93: for twenty minutes altına sarı yay; Caveat 20 dk
  {
    const a = cz[7], b = cz[9], xm = (a.x0 + b.x1) / 2, y0 = a.y + 24;
    const yay = ciz([[a.x0, y0 - 8], [xm - 120, y0 + 10], [xm + 120, y0 + 10], [b.x1, y0 - 8]],
      { w: 8, renk: SARI, alfa: 0.85, bas: fr(20.41), sure: 26, uc0: 14, uc1: 30, amp: 0.7 });
    not("for twenty minutes yayı", yay.bas);
    yazi("20 dk", { x: b.x1 - 170, y: a.y + 82, boyut: 52, renk: SARI, bas: bitis(yay) - 4,
      sure: 12, ses: true });
  }

  // --- 22,10–24,26: Yirmi dakikadır otobüs bekliyorum. (Caveat 48 ikincil, y 505)
  yazi("Yirmi dakikadır otobüs bekliyorum.", { x: 140, y: 505, boyut: 48, renk: IKI, bas: fr(22.1), sure: 22 });
  not("Türkçe çeviri", fr(22.1));

  // --- 24,30–25,62: zaman çizgisi (y 640), 20 dk önce noktası, nabız atan now, dalgalı in progress bandı
  {
    const yT = 640, xP = 260, xN = 760;
    const tl = ciz([[140, yT + 2], [420, yT - 2], [700, yT + 1], [925, yT - 1]],
      { w: 4.2, renk: IKI, alfa: 0.9, bas: fr(24.3), sure: 18, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[900, yT - 17], [928, yT - 1], [900, yT + 14]], { w: 4.2, renk: IKI, alfa: 0.9, bas: bitis(tl) - 2,
      sure: 7, duz: true, uc0: 5, uc1: 5, ses: false });
    const fp = fr(24.66), fn = fr(25.0);
    dinamik((f, g) => {
      if (f >= fp) g.addChild(new P.Path.Circle({ center: [xP, yT], radius: 10 * Math.min(1, (f - fp) / 5),
        fillColor: renkCoz(IKI), insert: false }));
      if (f < fn) return;
      const t = f - fn, s = 1 + 0.16 * Math.sin(2 * Math.PI * t / 36), u = (t % 45) / 45, a = Math.min(1, t / 5);
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 11 * s * a, fillColor: renkCoz(SARI), insert: false }));
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 13 + 30 * (1 - Math.pow(1 - u, 3)),
        strokeColor: renkCoz(SARI), strokeWidth: 4, opacity: 0.75 * (1 - u) * a, insert: false }));
    });
    olay(fp, "tik", 0.5); olay(fn, "tik", 0.5); not("20 dk önce noktası", fp); not("now noktası (nabız)", fn);
    yazi("20 dk önce", { x: xP, y: yT + 68, hizala: "orta", boyut: 28, aile: "Lexend", agirlik: 500, renk: IKI,
      bas: fp + 2, sure: 8 });
    yazi("now", { x: xN, y: yT + 68, hizala: "orta", boyut: 28, aile: "Lexend", agirlik: 500, renk: IKI,
      bas: fn + 2, sure: 8 });
    const dalga = Array.from({ length: 40 }, (_, i) => { const u = i / 39, x = xP + 40 + u * (xN - xP - 80);
      return [x, yT - 56 + 11 * Math.sin(u * 7.5 * Math.PI) * (0.55 + 0.45 * Math.sin(u * Math.PI))]; });
    const w = ciz(dalga, { w: 7.5, renk: SARI, alfa: 0.85, bas: fr(25.08), sure: 22, duz: true, uc0: 12, uc1: 24,
      amp: 0.5 });
    not("in progress bandı", w.bas);
    yazi("in progress", { x: (xP + xN) / 2, y: yT - 82, hizala: "orta", boyut: 44, renk: SARI,
      bas: bitis(w) - 6, sure: 12, ses: true });
  }

  // --- 25,87–28,28: for (Fredoka 130 sarı, vurus) + Caveat süre uzunluğu
  {
    const f0 = fr(25.87);
    yazi("for", { x: 1010, y: 870, boyut: 130, aile: "Fredoka", agirlik: 700, renk: SARI, bas: f0, sure: 10,
      olcek: true, ses: "vurus" });
    olay(f0, "vurus", 0.85); not("for (vurgu)", f0);
    yazi("süre uzunluğu", { x: 1010, y: 950, boyut: 56, renk: IKI, bas: fr(27.64), sure: 14, ses: true });
    not("süre uzunluğu", fr(27.64));
    parilti(1190, 780, { bas: f0 + 8, r: 24 });
  }

  // --- 29,72 have been ve 31,08 waiting: cümlede sarı daire
  {
    const a = cz[1], b = cz[2], c = cz[3];
    const da = daire((a.x0 + b.x1) / 2, a.y - 22, (b.x1 - a.x0) / 2 + 4, 38, { bas: fr(29.72), sure: 18, a0: -1.8 });
    olay(bitis(da), "tik", 0.5); not("have been daire", da.bas);
    const dc = daire((c.x0 + c.x1) / 2, c.y - 22, c.w / 2 + 2, 38, { bas: fr(31.08), sure: 18, a0: -2.8 });
    olay(bitis(dc), "tik", 0.5); not("waiting daire", dc.bas);
  }

  // --- 28,84–32,28: formül kartı (el kutusu): have been + V-ing / wait-ing
  {
    S.kutu(140, 745, 640, 235, { bas: fr(28.84) - 10, sure: 24 }); not("formül kartı kutusu", fr(28.84) - 10);
    const y1 = 840, y2 = 945, F = { boyut: 60, aile: "Fredoka", agirlik: 700 };
    const hb = yazi("have been", { ...F, x: 200, y: y1, bas: fr(29.72), sure: 10, olcek: true, ses: true });
    not("have been", fr(29.72));
    const pl = yazi("+", { ...F, x: hb.x1 + 36, y: y1, bas: fr(30.68), sure: 8, olcek: true });
    const v = yazi("V", { ...F, x: pl.x1 + 36, y: y1, bas: fr(31.08), sure: 8, olcek: true }); not("V", fr(31.08));
    yazi("-ing", { ...F, x: v.x1 + 4, y: y1, bas: fr(31.64), sure: 10, olcek: true, renk: SARI, ses: true });
    not("-ing", fr(31.64));
    const w = yazi("wait", { ...F, x: 200, y: y2, bas: fr(31.2), sure: 10, olcek: true });
    yazi("-ing", { ...F, x: w.x1 + 4, y: y2, bas: fr(31.7), sure: 10, olcek: true, renk: SARI, ses: true });
    not("wait-ing", fr(31.7));
    parilti(v.x1 + 140, y2 - 40, { bas: fr(31.9), r: 22 });
  }
  void genislik;
  return S;
}

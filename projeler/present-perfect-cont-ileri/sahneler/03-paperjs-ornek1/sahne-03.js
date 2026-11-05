// Sahne 03 (İLERİ) — Örnek 1 (505 kare, t_bas 17,25; cümle 3). Zamanlar BRIEF §4; yerel kare = round((t − 17,25) × 30).
// Kök: "Since the school changed the timetable, students have been complaining." (since + geçmiş yan cümle).
import { sahneKur, RT, renkCoz } from "/projeler/present-perfect-cont-ileri/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 505, T_BAS = 17.25;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, cumle, altCizgi, parilti, olay, not, bitis, dinamik, tik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12;                                                   // geçiş karesi: çizimler bundan sonra başlar
  const f0 = (t) => Math.max(GB, fr(t));

  // --- 17,80–18,84: büyük el çizimi daire içinde 1
  const d1 = daire(200, 190, 66, 62, { bas: f0(17.80), sure: 22, a0: -2.6 }); olay(bitis(d1), "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 226, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700, bas: f0(18.15), sure: 10, olcek: true });

  // --- 19,09–23,41: İngilizce kök (Fredoka 64, 3 satır 4 / 3 / 3 sözcük, sözcük zamanlı)
  const sz = S.sozcukler(3).slice(2, 12);                          // Since … complaining.
  const satirNo = (i) => (i < 4 ? 0 : i < 7 ? 1 : 2);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 140, y: 330, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 92 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (Since)", cz[0].bas);

  // Since … changed (19,89–20,21): sarı köşeli ayraç + Caveat `geçmiş yan cümle`
  {
    const x0 = cz[0].x0 - 6, x1 = cz[3].x1 + 6, y = cz[0].y + 20;
    const a = ciz([[x0, y - 12], [x0, y + 2], [x1, y + 2], [x1, y - 12]],
      { duz: true, w: 7, renk: SARI, alfa: 0.85, bas: fr(19.89), sure: 14, uc0: 12, uc1: 24 });
    not("Since … changed ayraç", a.bas); olay(bitis(a), "tik", 0.5);
    yazi("geçmiş yan cümle", { x: 310, y: cz[0].y - 70, boyut: 44, aile: "Caveat", agirlik: 700, renk: SARI,
      bas: fr(20.21), sure: 12, ses: true });
  }
  // have been complaining (21,81–23,41): ikinci sarı daire + `ana cümle`
  {
    const x0 = cz[7].x0, x1 = cz[9].x1, y = cz[7].y - 20;
    const d = daire((x0 + x1) / 2, y, (x1 - x0) / 2 + 8, 42, { bas: fr(21.81), sure: 22, a0: -2.6, egim: -0.025 });
    olay(bitis(d), "tik", 0.5); not("have been complaining daire", d.bas);
    yazi("ana cümle", { x: x1 + 40, y: cz[7].y - 10, boyut: 44, aile: "Caveat", agirlik: 700, renk: SARI,
      bas: fr(22.6), sure: 12, ses: true });
  }

  // --- 19,09–23,41: sağ sahne. Okul (420 px) + oturan öğrenci (sitting-6) + takvim
  const ogeOkul = S.oge({ nefes: { bas: fr(24.5), cx: 1400, cy: 580 } });
  await S.svgCiz("coco/school.svg", { kutu: [1110, 190, 440, 420], bas: f0(19.09), sure: fr(20.2) - f0(19.09), azami: 25, yuz: 1,
    w: 4, oge: ogeOkul, sesAralik: 3 });
  not("okul çizimi başı", f0(19.09));
  const ogeOgr = S.oge({ nefes: { bas: fr(25.4), cx: 1730, cy: 640 } });
  await S.svgCiz("open-peeps/sitting-6.svg", { kutu: [1590, 300, 280, 340], bas: f0(19.7), sure: fr(21.5) - f0(19.7), azami: 60, yuz: 3,
    w: 3.2, oge: ogeOgr, sesAralik: 5 });
  not("öğrenci figürü çizimi başı", f0(19.7));
  await S.svgCiz("tabler/calendar.svg", { kutu: [1700, 150, 130, 130], bas: fr(20.4), sure: 14, azami: 25, w: 4, sesAralik: 2 });
  not("takvim (timetable) çizimi başı", fr(20.4));
  parilti(1640, 200, { bas: fr(21.0), r: 22 });

  // --- 23,66–26,86: Türkçe çeviri (Caveat 48 ikincil, y 620), sözcük zamanlı
  const tr = S.sozcukler(3).slice(12, 17);                          // Program değişeli beri öğrenciler yakınıyor.
  const tz = cumle(tr.map((k) => ({ s: k.s, f: k.f, satir: 0 })), { x: 140, y: 630, boyut: 48, aile: "Caveat", agirlik: 700, renk: IKI });
  not("Türkçe çeviri", tz[0].bas);

  // --- 27,11–30,07: zaman çizgisi (y 760): changed noktası -> since yayı -> now (nabız)
  {
    const yT = 795, xC = 420, xN = 1180;
    const tl = ciz([[140, yT + 2], [520, yT - 2], [900, yT + 1], [1500, yT - 1]], { w: 4.4, renk: IKI, alfa: 0.9, bas: fr(27.11), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[1470, yT - 17], [1502, yT - 1], [1470, yT + 14]], { w: 4.4, renk: IKI, alfa: 0.9, bas: bitis(tl) - 2, sure: 7, duz: true, uc0: 5, uc1: 5, ses: false });
    const fc = fr(27.75);
    dinamik((f, g) => {
      if (f < fc) return;
      const a = Math.min(1, (f - fc) / 5);
      g.addChild(new P.Path.Circle({ center: [xC, yT], radius: 11 * a, fillColor: renkCoz(SARI), insert: false }));
    });
    olay(fc, "tik", 0.5); not("changed noktası", fc);
    yazi("changed", { x: xC, y: yT + 52, hizala: "orta", boyut: 44, aile: "Caveat", agirlik: 700, renk: IKI, bas: fc + 2, sure: 10 });
    const yay = Array.from({ length: 24 }, (_, i) => { const u = i / 23;
      return [xC + 20 + u * (xN - xC - 40), yT - 18 - 56 * Math.sin(u * Math.PI)]; });
    const ya = ciz(yay, { w: 7.5, renk: SARI, alfa: 0.85, bas: fr(28.07), sure: 26, duz: true, uc0: 12, uc1: 24, amp: 0.5 });
    not("since yayı", ya.bas);
    yazi("since", { x: (xC + xN) / 2, y: yT - 92, hizala: "orta", boyut: 52, aile: "Caveat", agirlik: 700, renk: SARI,
      bas: fr(28.45), sure: 10, ses: true });
    const fn = fr(29.1);
    dinamik((f, g) => {
      if (f < fn) return;
      const t = f - fn, s = 1 + 0.16 * Math.sin(2 * Math.PI * t / 36), u = (t % 45) / 45, a = Math.min(1, t / 5);
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 11 * s * a, fillColor: renkCoz(SARI), insert: false }));
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 13 + 30 * (1 - Math.pow(1 - u, 3)), strokeColor: renkCoz(SARI), strokeWidth: 4, opacity: 0.75 * (1 - u) * a, insert: false }));
    });
    olay(fn, "tik", 0.5); not("now noktası (nabız)", fn);
    yazi("now", { x: xN, y: yT + 52, hizala: "orta", boyut: 44, aile: "Caveat", agirlik: 700, renk: IKI, bas: fn + 2, sure: 8 });
    yazi("past simple", { x: xC + 190, y: yT + 52, boyut: 44, aile: "Caveat", agirlik: 700, renk: SARI, bas: fr(29.3), sure: 10, ses: true });
    not("past simple etiketi", fr(29.3));
  }

  // --- 30,32–33,68: kural kartı (alt): since + past simple, have been + V-ing + tik
  {
    const ky = 870, y = ky + 92, F = { boyut: 60, aile: "Fredoka", agirlik: 700 };
    kutu(140, ky, 1600, 130, { bas: fr(30.32), sure: 24, w: 4.2, renk: IKI }); olay(fr(30.32), "tik", 0.5);
    not("kural kartı kutusu", fr(30.32));
    const a = yazi("since", { ...F, x: 200, y, bas: fr(30.6), sure: 10, olcek: true, renk: SARI, ses: true });
    const b = yazi("+ past simple", { ...F, x: a.x1 + 18, y, bas: fr(30.95), sure: 10, olcek: true, ses: true });
    const c = yazi(",", { ...F, x: b.x1 + 4, y, bas: fr(31.1), sure: 6, renk: IKI });
    const d = yazi("have been", { ...F, x: c.x1 + 44, y, bas: fr(31.36), sure: 10, olcek: true, ses: true });
    const e = yazi("+ V", { ...F, x: d.x1 + 18, y, bas: fr(32.1), sure: 8, olcek: true });
    const g = yazi("-ing", { ...F, x: e.x1 + 4, y, bas: fr(32.56), sure: 10, olcek: true, renk: SARI, ses: true });
    not("since + past simple, have been + V-ing", fr(30.6));
    tik(g.x1 + 70, ky + 56, { bas: fr(33.12) });
    parilti(1700, ky + 20, { bas: fr(33.2), r: 22 });
  }
  return S;
}

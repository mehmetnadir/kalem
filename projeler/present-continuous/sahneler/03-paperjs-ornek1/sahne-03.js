// Sahne 03 — Örnek 1 (453 kare, t_bas 21,44; cümle 3). Zamanlar BRIEF §4; yerel kare = round((t − 21,44) × 30).
import { sahneKur, RT, renkCoz } from "/projeler/present-continuous/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 453, T_BAS = 21.44, KAYMA = 6.0;   // T_BAS: eski çerçeve; zaman.json t_bas 15,44
export const FIGUR_AYNA = false;                                   // sitting-4 yönü: kameraya bakması için

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: KAYMA });
  const { fr, ciz, daire, yazi, cumle, altCizgi, parilti, olay, not, bitis, dinamik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12;

  // --- 21,44–22,48: büyük el çizimi daire içinde 1 (x 140, y 200)
  const d1 = daire(200, 190, 66, 62, { bas: GB, sure: 20, a0: -2.6 }); olay(bitis(d1), "tik", 0.5); not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 226, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700, bas: GB + 4, sure: 10, olcek: true });

  // --- 22,73–24,65: cümle (Fredoka 64, x 140, y 320, 2 satır), sözcük sözcük + sarı alt çizgi
  const sz = S.sozcukler(3).slice(2, 11);                           // I … now.
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: i < 6 ? 0 : 1 })), { x: 140, y: 320, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 80 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (I)", cz[0].bas); not("now", cz[8].bas);

  // --- 22,5–24,6: oturan figür + kamera + sehpa
  const figOge = S.oge({ nefes: { bas: fr(24.7), cx: 1195, cy: 670 } });
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [1010, 170, 370, 500], bas: fr(22.5), sure: fr(24.6) - fr(22.5), azami: 60, yuz: 3, w: 3.2,
    oge: figOge, sesAralik: 5, ayna: FIGUR_AYNA });
  not("figür çizimi başı", fr(22.5));
  await S.svgCiz("tabler/camera.svg", { kutu: [1520, 240, 210, 210], bas: fr(23.8), sure: 14, azami: 25, w: 4, sesAralik: 1 });
  not("kamera çizimi başı", fr(23.8));
  [[[1625, 424], [1545, 655]], [[1625, 424], [1627, 665]], [[1625, 424], [1712, 655]]].forEach((p, i) => {
    ciz([p[0], [(p[0][0] + p[1][0]) / 2 + 2, (p[0][1] + p[1][1]) / 2], p[1]], { w: 4, bas: fr(23.8) + 14 + i * 4, sure: 6, uc0: 6, uc1: 12, amp: 0.6 }); });
  not("sehpa (3 çizgi)", fr(23.8) + 14);
  parilti(1700, 262, { bas: fr(24.7), r: 24, periyot: 170, adet: 4 });

  // --- 24,65: now sarı daire + NOW etiketi
  {
    const g = cz[8], d = daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 3, 38, { bas: fr(24.65), sure: 16 });
    olay(bitis(d), "tik", 0.5); not("now daire", d.bas);
    yazi("NOW", { x: g.x1 + 56, y: g.y + 4, boyut: 56, renk: SARI, bas: bitis(d) + 2, sure: 10, olcek: true });
  }

  // --- 25,30–25,78: Şu anda oturuyorum. (Caveat 48 ikincil, y 490)
  yazi("Şu anda oturuyorum.", { x: 140, y: 490, boyut: 48, renk: IKI, bas: fr(25.3), sure: 17 }); not("Türkçe çeviri", fr(25.3));

  // --- 26,78–28,26: zaman çizgisi, nabız atan now noktası, dalgalı in progress bandı
  {
    const yT = 650, xN = 520, tl = ciz([[140, yT + 2], [420, yT - 2], [700, yT + 1], [925, yT - 1]], { w: 4.2, renk: IKI, alfa: 0.9, bas: fr(26.78), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[900, yT - 17], [928, yT - 1], [900, yT + 14]], { w: 4.2, renk: IKI, alfa: 0.9, bas: bitis(tl) - 2, sure: 7, duz: true, uc0: 5, uc1: 5, ses: false });
    const f0 = fr(27.5);
    dinamik((f, g) => {
      if (f < f0) return;
      const t = f - f0, s = 1 + 0.16 * Math.sin(2 * Math.PI * t / 36), u = (t % 45) / 45, a = Math.min(1, t / 5);
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 11 * s * a, fillColor: renkCoz(SARI), insert: false }));
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 13 + 30 * (1 - Math.pow(1 - u, 3)), strokeColor: renkCoz(SARI), strokeWidth: 4, opacity: 0.75 * (1 - u) * a, insert: false }));
    });
    olay(f0, "tik", 0.5); not("now noktası (nabız)", f0);
    yazi("now", { x: xN, y: yT + 52, hizala: "orta", boyut: 28, aile: "Lexend", agirlik: 500, renk: IKI, bas: f0 + 2, sure: 8 });
    const dalga = Array.from({ length: 40 }, (_, i) => { const u = i / 39, x = 330 + u * 380; return [x, 592 + 11 * Math.sin(u * 7.5 * Math.PI) * (0.55 + 0.45 * Math.sin(u * Math.PI))]; });
    const w = ciz(dalga, { w: 7.5, renk: SARI, alfa: 0.85, bas: fr(27.5) + 8, sure: 24, duz: true, uc0: 12, uc1: 24, amp: 0.5 }); not("in progress bandı", w.bas);
    yazi("in progress", { x: 520, y: 566, hizala: "orta", boyut: 44, renk: SARI, bas: bitis(w) - 6, sure: 14, ses: true });
  }

  // --- 29,29–31,85: am (30,73) ve sitting (31,85) sarı daire
  {
    const a = cz[1], s = cz[2];
    const da = daire((a.x0 + a.x1) / 2, a.y - 22, a.w / 2 + 1, 36, { bas: fr(30.73), sure: 16, a0: -1.8 }); olay(bitis(da), "tik", 0.5); not("am daire", da.bas);
    const ds = daire((s.x0 + s.x1) / 2, s.y - 22, s.w / 2 + 1, 36, { bas: fr(31.85), sure: 18, a0: -2.8 }); olay(bitis(ds), "tik", 0.5); not("sitting daire", ds.bas);
  }

  // --- 33,04–35,60: formül kartı (el kutusu): be + V-ing / am / sitt-ing
  {
    const k = S.kutu(140, 745, 560, 235, { bas: fr(33.04) - 10, sure: 24 }); not("formül kartı kutusu", fr(33.04) - 10);
    const y1 = 840, y2 = 945, F = { boyut: 60, aile: "Fredoka", agirlik: 700 };
    yazi("be", { ...F, x: 200, y: y1, bas: fr(33.04), sure: 10, olcek: true, ses: true }); not("be", fr(33.04));
    yazi("+", { ...F, x: 335, y: y1, bas: fr(34.12), sure: 8, olcek: true });
    const v = yazi("V", { ...F, x: 420, y: y1, bas: fr(34.4), sure: 8, olcek: true }); not("V", fr(34.4));
    yazi("-ing", { ...F, x: v.x1 + 4, y: y1, bas: fr(34.96), sure: 10, olcek: true, renk: SARI, ses: true }); not("-ing", fr(34.96));
    yazi("am", { ...F, x: 200, y: y2, bas: fr(33.6), sure: 10, olcek: true }); not("am (kart)", fr(33.6));
    const st = yazi("sitt", { ...F, x: 420, y: y2, bas: fr(35.0), sure: 10, olcek: true });
    yazi("-ing", { ...F, x: st.x1 + 4, y: y2, bas: fr(35.0) + 3, sure: 10, olcek: true, renk: SARI, ses: true }); not("sitt-ing", fr(35.0));
    parilti(700, 790, { bas: fr(35.1), r: 22 });
  }
  return S;
}

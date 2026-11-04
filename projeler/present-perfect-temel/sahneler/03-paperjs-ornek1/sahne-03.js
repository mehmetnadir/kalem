// Sahne 03 — Örnek 1 (475 kare, t_bas 18,73; cümle 3). Zamanlar BRIEF §4; yerel kare = round((t − 18,73) × 30).
import { sahneKur, RT, renkCoz } from "/projeler/present-perfect-temel/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 475, T_BAS = 18.73;

// Yuvarlak köşeli dikdörtgen çevresi (el çizimi akıllı telefon gövdesi için), nokta dizisi.
function yuvarlakKutu(x, y, w, h, r) {
  const p = [], ad = 5;
  const kose = (cx, cy, a0) => { for (let i = 0; i <= ad; i++) {
    const a = a0 + (Math.PI / 2) * (i / ad); p.push([cx + Math.cos(a) * r, cy + Math.sin(a) * r]); } };
  kose(x + w - r, y + r, -Math.PI / 2); kose(x + w - r, y + h - r, 0);
  kose(x + r, y + h - r, Math.PI / 2); kose(x + r, y + r, Math.PI);
  p.push(p[0]);
  return p;
}

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1 });
  const { fr, ciz, daire, yazi, cumle, altCizgi, parilti, olay, not, bitis, dinamik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;

  // --- 19,28–19,9: büyük el çizimi daire içinde 1 (x 200, y 190)
  const d1 = daire(200, 190, 66, 62, { bas: fr(19.28), sure: 20, a0: -2.6 }); olay(bitis(d1), "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 226, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700, bas: fr(19.28) + 4,
    sure: 10, olcek: true });

  // --- 20,49–22,41: cümle (Fredoka 64, x 140, y 320), sözcük sözcük + sarı alt çizgi
  const sz = S.sozcukler(3).slice(2, 7);                           // I have broken my phone.
  const cz = cumle(sz.map((k) => ({ s: k.s, f: k.f, satir: 0 })),
    { x: 140, y: 320, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 80 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (I)", cz[0].bas); not("phone", cz[4].bas);

  // --- 20,5–22,3: sağda akıllı telefon (420 px), el çizgisiyle; 25,2–26,5 ekranda 3 çatlak
  const PX = 1430, PY = 230, PW = 215, PH = 420, pcx = PX + PW / 2;
  const tel = S.oge({ nefes: { bas: fr(23.0), cx: pcx, cy: PY + PH } });
  const b0 = fr(20.5);
  ciz(yuvarlakKutu(PX, PY, PW, PH, 30), { duz: true, w: 4.2, bas: b0, sure: 20, oge: tel, uc0: 10, uc1: 20 });
  ciz(yuvarlakKutu(PX + 18, PY + 62, PW - 36, PH - 140, 8), { duz: true, w: 3.2, bas: b0 + 16, sure: 14, oge: tel });
  ciz([[pcx - 28, PY + 32], [pcx + 28, PY + 32]], { duz: true, w: 3.4, bas: b0 + 26, sure: 6, oge: tel, ses: false });
  const dugme = Array.from({ length: 16 }, (_, i) => { const a = -1.2 + (i / 15) * 2 * Math.PI * 1.04;
    return [pcx + Math.cos(a) * 17, PY + PH - 36 + Math.sin(a) * 17]; });
  ciz(dugme, { duz: true, w: 3.2, bas: b0 + 30, sure: 8, oge: tel, ses: false });
  not("telefon çizimi başı", b0);
  const sx = PX + 18, sy = PY + 62, sw = PW - 36;
  [[[sx + sw * 0.62, sy + 4], [sx + sw * 0.5, sy + 70], [sx + sw * 0.66, sy + 118], [sx + sw * 0.42, sy + 190],
    [sx + sw * 0.52, sy + 240]],
   [[sx + sw * 0.5, sy + 70], [sx + sw * 0.2, sy + 96], [sx + 4, sy + 150]],
   [[sx + sw * 0.66, sy + 118], [sx + sw * 0.92, sy + 150], [sx + sw - 4, sy + 214]]].forEach((p, i) => {
    ciz(p, { w: 4, bas: fr(25.2) + i * 12, sure: 12, uc0: 4, uc1: 8, amp: 0.8, oge: tel }); });
  not("çatlaklar (3 çizgi)", fr(25.2));
  parilti(PX + PW - 20, PY + 40, { bas: fr(25.2) + 36, r: 26 });

  // --- 22,66–23,6: Telefonumu kırdım. (Caveat 48, y 470)
  yazi("Telefonumu kırdım.", { x: 140, y: 470, boyut: 48, renk: IKI, bas: fr(22.66), sure: 17 });
  not("Türkçe çeviri", fr(22.66));

  // --- 24,18–27,86: zaman çizgisi (y 620): past noktası (24,74) → now noktası (26,5) nabız atar
  {
    const yT = 620, xP = 240, xN = 760;
    const tl = ciz([[140, yT + 2], [420, yT - 2], [700, yT + 1], [925, yT - 1]],
      { w: 4.2, renk: IKI, alfa: 0.9, bas: fr(24.18), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[900, yT - 17], [928, yT - 1], [900, yT + 14]], { w: 4.2, renk: IKI, alfa: 0.9, bas: bitis(tl) - 2, sure: 7,
      duz: true, uc0: 5, uc1: 5, ses: false });
    const fp = fr(24.74), fn = fr(26.5);
    dinamik((f, g) => {
      if (f >= fp) g.addChild(new P.Path.Circle({ center: [xP, yT], radius: 10 * Math.min(1, (f - fp) / 5),
        fillColor: renkCoz(IKI), insert: false }));
      if (f < fn) return;
      const t = f - fn, s = 1 + 0.16 * Math.sin(2 * Math.PI * t / 36), u = (t % 45) / 45, a = Math.min(1, t / 5);
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 11 * s * a, fillColor: renkCoz(SARI), insert: false }));
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 13 + 30 * (1 - Math.pow(1 - u, 3)),
        strokeColor: renkCoz(SARI), strokeWidth: 4, opacity: 0.75 * (1 - u) * a, insert: false }));
    });
    olay(fp, "tik", 0.5); olay(fn, "tik", 0.5); not("past noktası", fp); not("now noktası (nabız)", fn);
    yazi("past", { x: xP, y: yT + 68, hizala: "orta", boyut: 28, aile: "Lexend", agirlik: 500, renk: IKI,
      bas: fp + 2, sure: 8 });
    yazi("now", { x: xN, y: yT + 68, hizala: "orta", boyut: 28, aile: "Lexend", agirlik: 500, renk: IKI,
      bas: fn + 2, sure: 8 });
    yazi("ekran şimdi de kırık", { x: 430, y: yT - 36, hizala: "orta", boyut: 48, renk: SARI, bas: fr(26.1),
      sure: 17, ses: true });
  }

  // --- 29,37 have ve 30,33 broken: sarı daire
  {
    const a = cz[1], b = cz[2];
    const da = daire((a.x0 + a.x1) / 2, a.y - 22, a.w / 2 + 2, 36, { bas: fr(29.37), sure: 16, a0: -1.8 });
    olay(bitis(da), "tik", 0.5); not("have daire", da.bas);
    const db = daire((b.x0 + b.x1) / 2, b.y - 22, b.w / 2 + 2, 36, { bas: fr(30.33), sure: 18, a0: -2.8 });
    olay(bitis(db), "tik", 0.5); not("broken daire", db.bas);
  }

  // --- 31,44–34,16: formül kartı (el kutusu): have + V3 / have · broken
  {
    S.kutu(140, 745, 560, 235, { bas: fr(31.44) - 10, sure: 24 }); not("formül kartı kutusu", fr(31.44) - 10);
    const y1 = 840, y2 = 945, F = { boyut: 60, aile: "Fredoka", agirlik: 700 };
    const h1 = yazi("have", { ...F, x: 200, y: y1, bas: fr(31.44), sure: 10, olcek: true, ses: true });
    const pl = yazi("+", { ...F, x: h1.x1 + 36, y: y1, bas: fr(32.32), sure: 8, olcek: true });
    const v3 = yazi("V3", { ...F, x: pl.x1 + 36, y: y1, bas: fr(33.32), sure: 8, olcek: true, ses: true });
    not("have + V3", fr(31.44));
    yazi("have", { ...F, x: 200, y: y2, bas: fr(31.9), sure: 10, olcek: true });
    yazi("broken", { ...F, x: v3.x0, y: y2, bas: fr(33.72), sure: 10, olcek: true, renk: SARI, ses: true });
    not("have / broken", fr(33.72));
    parilti(745, y2 - 40, { bas: fr(33.9), r: 22 });
  }
  return S;
}

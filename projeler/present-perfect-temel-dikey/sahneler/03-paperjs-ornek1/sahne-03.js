// Sahne 03 (DİKEY) — Örnek 1: Paper.js, 1080x1920, 475 kare, t_bas 18,73; cümle 3.
// Yerel kare = round((t − 18,73) × 30); zamanlar sozcukler.json ve altyazi.json ile aynı çerçevede.
// Yerleşim sıfırdan dikey: kart (tam genişlik) → TR çeviri → ORTA telefon (sol) + zaman çizgisi ve notlar (sağ)
// → alt formül (iki satır).
import { sahneKur, RT, renkCoz } from "/projeler/present-perfect-temel-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 475, T_BAS = 18.73;

// Yuvarlak köşeli dikdörtgen çevresi (el çizimi akıllı telefon gövdesi), nokta dizisi.
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
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, yazi, cumle, altCizgi, parilti, olay, not, bitis, dinamik, genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const GB = 12;                                                   // ilk 12 kare geçiş altında: yalnız künye
  const CV = (b) => ({ boyut: b, aile: "Caveat", agirlik: 700 });

  // --- kart: tam genişlik (984), Fredoka 72, sözcük zamanlı; satır kırılımı ölçülür
  const sz = S.sozcukler(3).slice(2, 7);                           // I have broken my phone.
  const FK = "700 72px Fredoka", MAKS = 984 - 80, SB = genislik(" ", FK);
  const satirlar = [[]]; let gen = 0;
  for (const k of sz) {
    const w = genislik(k.s, FK);
    if (satirlar[satirlar.length - 1].length && gen + SB + w > MAKS) { satirlar.push([]); gen = 0; }
    gen += (satirlar[satirlar.length - 1].length ? SB : 0) + w; satirlar[satirlar.length - 1].push(k);
  }
  const SH = 88, B1 = 372 + 40 + 58;                               // kart üstü 372, iç boşluk 40, ilk taban
  const sonTaban = B1 + (satirlar.length - 1) * SH, kartAlt = sonTaban + 24 + 36;
  S.kutu(48, 372, 984, kartAlt - 372, { bas: GB, sure: 36, w: 4, renk: IKI });
  not("kart kutusu çizimi", GB);
  const kel = satirlar.flatMap((a, si) => a.map((k) => ({ s: k.s, f: k.f, satir: si })));
  const cz = cumle(kel, { x: 88, y: B1, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: SH });
  altCizgi(cz, { tut: 40, w: 9 }); not("cümle başı (I)", cz[0].bas); not("phone", cz[4].bas);

  // --- TR çeviri (Caveat 64, mürekkep) 22,66
  const yTR = kartAlt + 66;
  yazi("Telefonumu kırdım.", { x: 64, y: yTR, ...CV(64), renk: MUR, bas: fr(22.66), sure: 17 });
  not("Türkçe çeviri", fr(22.66));

  // --- ORTA sol: akıllı telefon (≥ 420 px), el çizgisiyle; 25,2 ekranda 3 çatlak
  const fUst = yTR + 56, fAlt = 1185, PH = fAlt - fUst, PW = Math.round(PH * 0.5), PX = 90, PY = fUst;
  const pcx = PX + PW / 2;
  const tel = S.oge({ nefes: { bas: fr(23.0), cx: pcx, cy: fAlt } });
  const b0 = fr(20.5);
  ciz(yuvarlakKutu(PX, PY, PW, PH, 36), { duz: true, w: 4.6, bas: b0, sure: 22, oge: tel, uc0: 10, uc1: 20 });
  ciz(yuvarlakKutu(PX + 20, PY + 76, PW - 40, PH - 170, 10), { duz: true, w: 3.6, bas: b0 + 18, sure: 16, oge: tel });
  ciz([[pcx - 32, PY + 38], [pcx + 32, PY + 38]], { duz: true, w: 4, bas: b0 + 28, sure: 6, oge: tel, ses: false });
  const dugme = Array.from({ length: 16 }, (_, i) => { const a = -1.2 + (i / 15) * 2 * Math.PI * 1.04;
    return [pcx + Math.cos(a) * 20, PY + PH - 44 + Math.sin(a) * 20]; });
  ciz(dugme, { duz: true, w: 3.6, bas: b0 + 32, sure: 8, oge: tel, ses: false });
  not("telefon çizimi başı", b0);
  const sx = PX + 20, sy = PY + 76, sw = PW - 40, sh = PH - 170;
  [[[sx + sw * 0.62, sy + 4], [sx + sw * 0.5, sy + sh * 0.25], [sx + sw * 0.66, sy + sh * 0.45],
    [sx + sw * 0.42, sy + sh * 0.72], [sx + sw * 0.52, sy + sh - 6]],
   [[sx + sw * 0.5, sy + sh * 0.25], [sx + sw * 0.2, sy + sh * 0.34], [sx + 4, sy + sh * 0.55]],
   [[sx + sw * 0.66, sy + sh * 0.45], [sx + sw * 0.92, sy + sh * 0.56], [sx + sw - 4, sy + sh * 0.8]]].forEach((p, i) => {
    ciz(p, { w: 4.6, bas: fr(25.2) + i * 10, sure: 12, uc0: 4, uc1: 8, amp: 0.8, oge: tel }); });
  not("çatlaklar (3 çizgi)", fr(25.2));
  parilti(PX + PW - 10, PY + 50, { bas: fr(25.2) + 34, r: 30 });

  // --- ORTA sağ: zaman çizgisi (24,18–26,5) + notlar; sütun x 400–1010
  {
    const xA = 410, xB = 1010, yT = fUst + 150, xP = 490, xN = 900;
    const tl = ciz([[xA, yT + 2], [xA + 200, yT - 2], [xA + 400, yT + 1], [xB - 24, yT - 1]],
      { w: 4.6, renk: IKI, alfa: 0.9, bas: fr(24.18), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[xB - 44, yT - 18], [xB - 16, yT - 1], [xB - 44, yT + 15]], { w: 4.6, renk: IKI, alfa: 0.9,
      bas: bitis(tl) - 2, sure: 7, duz: true, uc0: 5, uc1: 5, ses: false });
    const fp = fr(24.74), fn = fr(26.5);
    dinamik((f, g) => {
      if (f >= fp) g.addChild(new P.Path.Circle({ center: [xP, yT], radius: 13 * Math.min(1, (f - fp) / 5),
        fillColor: renkCoz(MUR), insert: false }));
      if (f < fn) return;
      const t = f - fn, s = 1 + 0.16 * Math.sin(2 * Math.PI * t / 36), u = (t % 45) / 45, a = Math.min(1, t / 5);
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 14 * s * a, fillColor: renkCoz(SARI), insert: false }));
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 16 + 34 * (1 - Math.pow(1 - u, 3)),
        strokeColor: renkCoz(SARI), strokeWidth: 5, opacity: 0.75 * (1 - u) * a, insert: false }));
    });
    olay(fp, "tik", 0.5); olay(fn, "tik", 0.5); not("past noktası", fp); not("now noktası (nabız)", fn);
    yazi("past", { x: xP, y: yT - 44, hizala: "orta", ...CV(72), renk: MUR, bas: fp + 2, sure: 8 });
    yazi("now", { x: xN, y: yT - 44, hizala: "orta", ...CV(72), renk: SARI, bas: fn + 2, sure: 8 });
    yazi("geçmişte oldu", { x: xA + 4, y: yT + 104, ...CV(64), renk: MUR, bas: fr(24.74), sure: 17 });
    not("geçmişte oldu notu", fr(24.74));
    yazi("ekran şimdi", { x: xB, y: yT + 190, hizala: "sag", ...CV(72), renk: SARI, bas: fr(26.1), sure: 14, ses: true });
    yazi("de kırık", { x: xB, y: yT + 266, hizala: "sag", ...CV(72), renk: SARI, bas: fr(26.74), sure: 12 });
    not("ekran şimdi de kırık notu", fr(26.1));
    S.ok([xN, yT + 56], [xN, yT + 100], { bas: fr(26.7), sure: 12, w: 8, uzun: 22, bukum: 0.05 });
  }

  // --- 29,37 have ve 30,33 broken: kartta sarı daire (sözcük başlarında)
  {
    const a = cz[1], b = cz[2];
    const da = daire((a.x0 + a.x1) / 2, a.y - 26, a.w / 2 + 4, 40, { bas: fr(29.37), sure: 16, a0: -1.8 });
    olay(bitis(da), "tik", 0.5); not("have daire", da.bas);
    const db = daire((b.x0 + b.x1) / 2, b.y - 26, b.w / 2 + 4, 40, { bas: fr(30.33), sure: 18, a0: -2.8 });
    olay(bitis(db), "tik", 0.5); not("broken daire", db.bas);
  }

  // --- alt formül: satır A `have + broken` (31,44–32,92) → ok → satır B `have + V3` (33,1–33,72)
  {
    const boy = 100, F = (b) => `700 ${b}px Fredoka`, GAP = 30;
    const topla = (p) => p.reduce((t, m) => t + genislik(m, F(boy)), 0) + GAP * (p.length - 1);
    const yA = 1286, yB = 1384;
    const sat = (p, y, t, renkler, sesIlk) => {
      let x = 540 - topla(p) / 2; const out = [];
      p.forEach((m, i) => {
        const o = yazi(m, { x, y, boyut: boy, aile: "Fredoka", agirlik: 700, renk: renkler[i], bas: fr(t[i]),
          sure: 10, olcek: true, ses: i === 0 && sesIlk }); out.push(o); x = o.x1 + GAP; });
      return out;
    };
    sat(["have", "+", "broken"], yA, [31.44, 32.32, 32.92], [MUR, IKI, SARI], true); not("have + broken", fr(31.44));
    const b = sat(["have", "+", "V3"], yB, [33.1, 33.3, 33.72], [MUR, IKI, SARI], true); not("have + V3", fr(33.1));
    S.ok([110, yA - 70], [110, yB - 40], { bas: fr(33.0), sure: 14, w: 8, uzun: 26, bukum: 0.14 });
    parilti(b[2].x1 + 50, yB - boy * 0.8, { bas: fr(33.9), r: 26 });
  }
  return S;
}

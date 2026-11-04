// Sahne 02 (DİKEY 1080x1920) — Kanca (484 kare, t_bas 3,00; cümle 2). Zamanlar KÜRESEL sn (sozcukler.json);
// yerel kare = round((t − 3,00) × 30). Cümle 1 ses olarak sahne 01'de söylendi: burada 0. kareden hazır durur
// (sahne 01 uçuş sonundaki yerle aynı: Caveat 96 tek satır, taban 450); ilk 12 kare durgun.
// Bant yerleşimi (BRIEF-DIKEY §2): cümle 380–470 · zaman çizgisi + notlar 490–640 · sahne 645–1084 ·
// ajanda kartı 1096–1392. Hiçbir öğe kaybolmaz; sağ sütun (x 780–1032) `-dı ⇄ have + V3` yığınıdır.
import { sahneKur, RT } from "/projeler/present-perfect-temel-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 484, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, ciz, daire, ok, yazi, cumle, tik, parilti, olay, not, bitis } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep, IKI = RT.ikincil;
  const GB = 12;                                                   // geçiş karesi: çizimler bundan sonra başlar
  const FR = { aile: "Fredoka", agirlik: 700 };

  // --- cümle 1: Caveat 96 tek satır; kare 0'da hazır
  const c1 = cumle(["Kaybettim,", "kapıda", "kaldım."].map((s) => ({ s, f: -8 })),
    { x: 48, y: 450, boyut: 96, aile: "Caveat", agirlik: 700 });
  not("cümle 1 hazır (kare 0)", 0);

  // --- sahne: figür (437 px) + ev (400 px) + yer çizgisi + anahtar (3 darbe, kapıda)
  const figOge = S.oge({ nefes: { bas: 150, cx: 145, cy: 1080 } });
  await S.svgCiz("tabler/home.svg", { kutu: [300, 680, 400, 400], bas: GB, sure: 30, azami: 25, w: 4, sesAralik: 2 });
  await S.svgCiz("open-peeps/standing-4.svg", { kutu: [48, 645, 194, 435], bas: GB + 6, sure: 48, azami: 60,
    yuz: 3, w: 4.4, oge: figOge, sesAralik: 4 });
  ciz([[48, 1086], [250, 1083], [480, 1088], [740, 1085]], { w: 4, renk: IKI, alfa: 0.8, bas: 40, sure: 30, uc0: 10, uc1: 30 });
  not("ev + figür çizimi başı", GB);
  {   // anahtar: halka + gövde + diş; ev kapısının önünde
    const cx = 400, cy = 1048, pts = [];
    for (let a = 0; a <= 360; a += 24) pts.push([cx + 22 * Math.cos(a * Math.PI / 180), cy + 22 * Math.sin(a * Math.PI / 180)]);
    const k1 = ciz(pts, { w: 5, bas: 62, sure: 12, uc0: 4, uc1: 4, amp: 0.4 });
    const k2 = ciz([[cx + 23, cy], [cx + 70, cy + 2], [cx + 120, cy + 1]], { w: 5, bas: bitis(k1), sure: 10, amp: 0.5 });
    ciz([[cx + 92, cy + 2], [cx + 93, cy + 17], [cx + 108, cy + 17], [cx + 108, cy + 2]],
      { w: 5, bas: bitis(k2), sure: 8, amp: 0.3, duz: true });
    not("anahtar çizimi başı", k1.bas);
    parilti(cx + 62, cy - 44, { bas: bitis(k2) + 14, r: 24, periyot: 160, adet: 2 });
  }

  // --- 4,27 Kaybettim sarı daire; 5,39 `geçmişte oldu`
  const halka = (x, y, r, w, bas, ses) => ciz(Array.from({ length: 17 }, (_, i) => [x + r * Math.cos(i * Math.PI / 8 - 1.2),
    y + r * Math.sin(i * Math.PI / 8 - 1.2)]), { w, bas, sure: 6, uc0: 1, uc1: 1, amp: 0.05, ses });
  const nokta = (x, y, bas) => { halka(x, y, 3.6, 7, bas + 4, false); return halka(x, y, 8, 9, bas, "tik"); };
  {
    const g = c1[0], d = daire((g.x0 + g.x1) / 2 + 2, g.y - 32, g.w / 2 + 12, 56, { bas: fr(4.27), sure: 24, egim: -0.04 });
    olay(bitis(d), "tik", 0.5); not("kaybettim daire", d.bas);
    const a = yazi("geçmişte oldu", { x: 48, y: 625, boyut: 64, renk: KRE, bas: fr(5.39), sure: 14, ses: true });
    not("not geçmişte oldu", a.bas);
  }

  // --- 6,91–8,35: zaman çizgisi past ● ━━ ● now; now daire; `sonucu şimdi bizimle`
  {
    const Y0 = 535, XA = 205, XB = 880;
    yazi("past", { x: 48, y: Y0 + 17, boyut: 64, renk: KRE, bas: fr(6.91), sure: 8 });
    const p = nokta(XA, Y0, fr(6.91));
    const l = ciz([[XA + 14, Y0], [XA + 230, Y0 - 3], [XA + 450, Y0 + 2], [XB - 14, Y0 - 1]],
      { w: 5, bas: fr(6.91) + 4, sure: 26, uc0: 6, uc1: 8, renk: KRE });
    const n = nokta(XB, Y0, bitis(l));
    const nw = yazi("now", { x: XB + 30, y: Y0 + 17, boyut: 64, renk: SARI, bas: fr(7.3), sure: 8, ses: true });
    const d = daire((nw.x0 + nw.x1) / 2, nw.y - 22, nw.w / 2 + 16, 40, { bas: fr(7.39), sure: 22, egim: -0.06 });
    olay(bitis(d), "tik", 0.5); not("şimdi daire (now)", d.bas);
    parilti(XB, Y0 - 4, { bas: bitis(n) + 6, r: 30, periyot: 60, adet: 4 });
    const b = yazi("sonucu şimdi bizimle", { x: 1024, y: 625, boyut: 64, renk: SARI, bas: fr(7.0), sure: 18, hizala: "sag" });
    not("zaman çizgisi başı", p.bas); not("not sonucu şimdi bizimle", b.bas);
  }

  // --- 8,50–11,62: sağ sütun yığını `-dı` ⇅ `have + V3`; Caveat `ayrı zaman`
  {
    const X = 790, a = yazi("-dı", { x: X, y: 735, boyut: 80, ...FR, renk: KRE, bas: fr(8.5), sure: 8, ses: true });
    const ar = ok([X + 70, 765], [X + 70, 828], { bas: fr(8.5) + 5, sure: 18, w: 8, cift: true, uzun: 26, bukum: 0.05 });
    const h = yazi("have", { x: X, y: 925, boyut: 80, ...FR, renk: SARI, bas: bitis(ar) + 4, sure: 10, ses: true });
    yazi("+ V3", { x: X, y: 1005, boyut: 80, ...FR, renk: SARI, bas: bitis(ar) + 12, sure: 10 });
    not("ok -dı ⇅ have + V3", ar.bas);
    const n = yazi("ayrı zaman", { x: X, y: 1075, boyut: 64, renk: KRE, bas: fr(9.86), sure: 16 });
    not("not ayrı zaman", n.bas);
  }

  // --- 11,77–18,73: ajanda kartı: saat + `6 dakikada:` + 3 madde tik zamanlı
  {
    S.kutu(48, 1096, 984, 296, { bas: fr(11.77) - 8, sure: 38, w: 4 }); not("kutu çizimi", fr(11.77) - 8);
    await S.svgCiz("tabler/clock.svg", { kutu: [72, 1112, 84, 84], bas: fr(12.05), sure: 20, azami: 25, w: 4, sesAralik: 3 });
    yazi("6 dakikada:", { x: 176, y: 1176, boyut: 64, renk: SARI, ...FR, bas: fr(12.05) + 14, sure: 12 });
    not("saat + 6 dakikada", fr(12.05));
    parilti(150, 1114, { bas: fr(12.9), r: 24, periyot: 170, adet: 3 });
    const m = [["form", 13.85, 1250], ["since / for", 15.17, 1316], ["sinyal sözcükleri", 16.89, 1382]];
    for (const [s, t, y] of m) {
      yazi(s, { x: 136, y, boyut: 64, ...FR, renk: KRE, bas: fr(t), sure: 8 });
      tik(92, y - 22, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

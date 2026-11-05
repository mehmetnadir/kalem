// Sahne 02 (PPC ileri S1 Shorts) — Örnek: Paper.js, 1080x1920, 423 kare, t_bas 3,00; cümle 1 sonu + cümle 2.
// Yerel kare = round((t − 3,00) × 30). İlk 12 kare geçiş altında: sahne 01'in son hali hazır çizili
// (Sınav tek şey sorar: / süreç + figür + kitap). Dikey v2 bantları:
// içerik 352–1392, alt bölge (940–1392) figür + nesne, üst bölge (392–900) yazı, altyazı 1400–1536.
import { sahneKur, RT } from "/projeler/present-perfect-cont-ileri-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 423, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Süreç / Sonuç" });
  const { fr, ciz, daire, yazi, cumle, kutu, parilti, olay, not, bitis, kis, oge, svgCiz } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil;
  const sol = (f0, f1) => (f) => 1 - kis((f - f0) / (f1 - f0));     // oge: [f0, f1] arası söner
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, ...o });
  const SOL = 72;

  // ---------- Faz A (3,0–7,75): cümle 1 sonu + kalıp (Have been plus the -ing form.) + figür + kitap ----------
  const A0 = fr(7.5), A1 = fr(7.75);
  const gA = oge({ alfa: sol(A0, A1) }), fSon = [A0, A1];
  const B0 = fr(12.45), B1 = fr(12.68);
  const kitapOge = oge({ alfa: sol(B0, B1) });                  // kitap + zemin çizgisi Faz B sonuna kadar kalır
  // satır 1–2 sahne 01'den hazır (f −30): Sınav tek şey sorar: / süreç; kalanı sözcük zamanlı
  cumle([{ s: "Sınav", f: -30 }, { s: "tek", f: -30 }, { s: "şey", f: -30 }, { s: "sorar:", f: -30 }],
    { x: SOL, y: 470, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  const t2 = cumle([{ s: "süreç", f: -30 }, { s: "mi,", f: s1[5].f }, { s: "sonuç", f: s1[6].f },
    { s: "mu?", f: s1[7].f }], { x: SOL, y: 620, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  not("mi, sonuç mu? yazılır", t2[1].bas);
  // kalıp: Have been plus / the -ing form. (Fredoka 88, iki satır)
  const kal = cumle(s1.slice(8).map((w, i) => ({ s: w.s, f: w.f, satir: i < 3 ? 0 : 1 })),
    { x: SOL, y: 780, boyut: 88, aile: "Fredoka", agirlik: 700, aralik: 110, son: fSon });
  not("kalıp satırı başı", kal[0].bas);
  {
    const g = kal[1], d = daire((g.x0 + g.x1) / 2, g.y - 28, g.w / 2 + 8, 48, { bas: g.bas + 2, sure: 16, oge: gA });
    olay(bitis(d), "tik", 0.5); not("been daire", d.bas);
    const ing = kal[4];
    altCiz(ing, ing.bas + 4, { oge: gA, w: 11 }); not("-ing altı çizgi", ing.bas + 4);
  }
  // figür (standing-3) + kitap + zemin çizgisi: sahne 01 ile aynı kutular, hazır çizili
  await svgCiz("open-peeps/standing-3.svg", { kutu: [150, 950, 213 * 0.628, 701 * 0.628], bas: -400, sure: 100,
    azami: 60, yuz: 3, w: 4.4, oge: gA, sessiz: true });
  await svgCiz("tabler/book.svg", { kutu: [408, 870, 576, 576], bas: -400, sure: 100, azami: 25, w: 4,
    oge: kitapOge, sessiz: true });
  ciz([[96, 1388], [560, 1386], [1000, 1388]], { w: 4, bas: -400, sure: 2, ses: false, duz: true, oge: kitapOge });

  // ---------- Faz B (7,75–12,68): EN kart + figür (sitting-4) okurken ----------
  const gB = oge({ alfa: sol(B0, B1) }), bSon = [B0, B1];
  const KY = 392, SH = 104, B1Y = KY + 40 + 64;                 // kart üstü 392, ilk taban 496
  kutu(48, KY, 984, 476, { bas: fr(7.8) - 6, sure: 30, w: 4, renk: IKI, oge: gB });
  not("kart kutusu", fr(7.8) - 6);
  const satirNo = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3];
  const en = s2.slice(0, 15).map((k, i) => ({ s: k.s, f: k.f, satir: satirNo[i] }));
  const e = cumle(en, { x: 88, y: B1Y, boyut: 80, aile: "Fredoka", agirlik: 700, aralik: SH, son: bSon });
  not("EN cümle başı", e[0].bas);
  {   // been reading sarı daire (8,20) · have only finished sarı daire (11,00)
    const a = e[2], b = e[3], d = daire((a.x0 + b.x1) / 2, a.y - 28, (b.x1 - a.x0) / 2 + 8, 48,
      { bas: fr(8.2), sure: 24, oge: gB });
    olay(bitis(d), "tik", 0.5); not("been reading daire", d.bas);
    const h = e[10], f2 = e[12], d2 = daire((h.x0 + f2.x1) / 2, h.y - 28, (f2.x1 - h.x0) / 2 + 8, 48,
      { bas: fr(11.0), sure: 26, a0: -2.6, oge: gB });
    olay(bitis(d2), "tik", 0.5); not("have only finished daire", d2.bas);
  }
  // figür sitting-4 (okuyan) — alt bölge 930–1390; kitap hazır
  await svgCiz("open-peeps/sitting-4.svg", { kutu: [100, 930, 340, 460], bas: fr(7.9), sure: fr(9.1) - fr(7.9),
    azami: 60, yuz: 3, w: 4.4, sesAralik: 5, oge: gB });
  not("figür çizimi başı", fr(7.9));
  parilti(930, 960, { bas: fr(9.4), r: 28, periyot: 150, adet: 3 });

  // ---------- Faz C (12,68–16,69): PROCESS / RESULT iki sütun kartı ----------
  const CY = 392, CH = 960, C0 = fr(12.69);
  kutu(48, CY, 480, CH, { bas: C0 - 4, sure: 30, w: 4, renk: IKI });
  kutu(552, CY, 480, CH, { bas: C0 - 4, sure: 30, w: 4, renk: IKI });
  not("iki sütun kartı", C0 - 4);
  const LX = 288, RX = 792;
  yazi("PROCESS", { x: LX, y: CY + 110, boyut: 80, aile: "Fredoka", agirlik: 700, hizala: "orta", bas: C0 + 10,
    sure: 8, ses: "tik" });
  yazi("RESULT", { x: RX, y: CY + 110, boyut: 80, aile: "Fredoka", agirlik: 700, hizala: "orta", bas: C0 + 12,
    sure: 8 });
  const trL = yazi("Süreç,", { x: LX, y: CY + 205, boyut: 88, aile: "Caveat", agirlik: 700, hizala: "orta",
    bas: s2[15].f, sure: 10 });
  const trR = yazi("Sonuç,", { x: RX, y: CY + 205, boyut: 88, aile: "Caveat", agirlik: 700, hizala: "orta",
    bas: s2[18].f, sure: 10 });
  not("Süreç, yazılır", trL.bas); not("Sonuç, yazılır", trR.bas);
  // sol: kitap simgesi + been / reading
  await svgCiz("tabler/book.svg", { kutu: [LX - 200, 650, 400, 400], bas: fr(13.45), sure: 30, azami: 25, w: 4,
    sesAralik: 1 });
  not("kitap simgesi", fr(13.45));
  yazi("been", { x: LX, y: 1150, boyut: 92, aile: "Fredoka", agirlik: 700, hizala: "orta", bas: s2[16].f, sure: 6 });
  const rd = yazi("reading", { x: LX, y: 1255, boyut: 92, aile: "Fredoka", agirlik: 700, hizala: "orta",
    bas: s2[17].f, sure: 8 });
  not("been reading yazılır", s2[16].f);
  altCiz(rd, rd.bas + 6, { w: 11 }); not("reading altı çizgi", rd.bas + 6);
  // sağ: büyük tik + have / finished
  const tk = ciz([[RX - 120, 860], [RX - 35, 950], [RX + 125, 760]],
    { w: 26, renk: SARI, alfa: 0.92, bas: fr(15.6), sure: 14, uc0: 8, uc1: 12, amp: 0.4, ses: "tik" });
  not("büyük tik", tk.bas);
  yazi("have", { x: RX, y: 1150, boyut: 92, aile: "Fredoka", agirlik: 700, hizala: "orta", bas: s2[19].f, sure: 6 });
  const fn = yazi("finished", { x: RX, y: 1255, boyut: 92, aile: "Fredoka", agirlik: 700, hizala: "orta",
    bas: s2[20].f, sure: 10 });
  not("have finished yazılır", s2[19].f);
  {
    const d = daire((fn.x0 + fn.x1) / 2, fn.y - 30, (fn.x1 - fn.x0) / 2 + 20, 58, { bas: fn.bas + 8, sure: 20 });
    olay(bitis(d), "tik", 0.5); not("finished daire", d.bas);
  }
  parilti(RX + 150, 750, { bas: fr(15.95), r: 30 });
  return S;
}

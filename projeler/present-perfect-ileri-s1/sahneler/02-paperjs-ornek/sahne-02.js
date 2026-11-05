// Sahne 02 (present-perfect-ileri-s1) — Örnek: Paper.js, 1080x1920, 383 kare, t_bas 3,00; cümle 1 sonu + cümle 2.
// Yerel kare = round((t − 3,00) × 30). İlk 12 kare geçiş altında: sahne 01'in son hali hazır çizili
// (Ago gördün mü, / Present Perfect + figür + saat). Dikey v2 bantları:
// içerik 352–1392, üst bölge (392–900) yazı, alt bölge (912–1392) nesneler, altyazı 1400–1536.
// Kırmızı yalnız `Has moved` çarpısında kullanılır (tuzak çarpısı).
import { sahneKur, RT } from "/projeler/present-perfect-ileri-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 383, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Trap" });
  const { fr, ciz, daire, yazi, cumle, kutu, olay, not, bitis, genislik, kis, oge, parilti } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil, KIRMIZI = RT.kirmizi;
  const sol = (f0, f1) => (f) => 1 - kis((f - f0) / (f1 - f0));     // oge: [f0, f1] arası söner
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, ...o });

  // ---------- Faz A (3,0–6,22): sahne 01'in son hali hazır; cümle 1 sonu yazılır; 6,00–6,22 söner ----------
  const A0 = fr(6.00), A1 = fr(6.22);
  const gA = oge({ alfa: sol(A0, A1) }), fSon = [A0, A1];
  const SOL = 72;
  cumle(s1.slice(0, 3).map((w) => ({ s: w.s, f: -30 })),
    { x: SOL, y: 500, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  cumle(s1.slice(3, 5).map((w) => ({ s: w.s, f: -30 })),
    { x: SOL, y: 640, boyut: 88, aile: "Fredoka", agirlik: 700, son: fSon });
  cumle([{ s: s1[5].s, f: s1[5].f }], { x: SOL, y: 770, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  cumle(s1.slice(6, 10).map((w) => ({ s: w.s, f: w.f })),
    { x: SOL, y: 890, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  // figür (standing-2) + saat + zemin çizgisi: sahne 01 ile aynı kutular, hazır çizili
  await S.svgCiz("open-peeps/standing-2.svg", { kutu: [190, 940, 213 * 0.6, 733 * 0.6], bas: -400,
    sure: 100, azami: 60, yuz: 3, w: 4.4, oge: gA, sessiz: true });
  await S.svgCiz("tabler/clock.svg", { kutu: [376, 906, 528, 528], bas: -400, sure: 100, azami: 25, w: 4,
    oge: gA, sessiz: true });
  ciz([[96, 1388], [560, 1386], [1000, 1388]], { w: 4, bas: -400, sure: 2, ses: false, duz: true, oge: gA });

  // ---------- Faz B (6,34–10,93): EN kart + TR çeviri + nesneler (ev, figür, takvim) ----------
  const B0 = fr(10.93), B1 = fr(11.10);
  const gB = oge({ alfa: sol(B0, B1) }), bSon = [B0, B1];
  const KY = 392, SH = 88, B1Y = KY + 40 + 58;                  // kart üstü 392, ilk taban 490, ikinci 578
  kutu(48, KY, 984, 246, { bas: fr(6.34) - 6, sure: 30, w: 4, renk: IKI, oge: gB });
  not("kart kutusu", fr(6.34) - 6);
  const en = s2.slice(0, 7).map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 }));
  const e = cumle(en, { x: 88, y: B1Y, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: SH, son: bSon });
  not("EN cümle başı", e[0].bas);
  altCiz(e[6], fr(8.02) + 4, { oge: gB }); not("ago altı çizgi", fr(8.02) + 4);
  // TR çeviri (8,75–10,91) Caveat 80 mürekkep
  const tr = cumle(s2.slice(7, 12).map((k, i) => ({ s: k.s, f: k.f, satir: i < 3 ? 0 : 1 })),
    { x: 72, y: 735, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 90, son: bSon });
  not("TR çeviri başı", tr[0].bas);

  // nesneler (alt bölge 912–1392, üç sütun; ev 200 / figür 540 / takvim 870) — sahne sonuna kadar kalır
  const LB = 1342, ETIKET = 64;
  await S.svgCiz("open-peeps/standing-2.svg", { kutu: [470, 912, 213 * 0.655, 733 * 0.655], bas: fr(6.40),
    sure: 40, azami: 60, yuz: 3, w: 4.4 });
  not("figür çizimi", fr(6.40));
  await S.svgCiz("tabler/home.svg", { kutu: [30, 950, 340, 340], bas: fr(6.98), sure: 22, azami: 25,
    w: 4, sesAralik: 2 });
  not("ev çizimi", fr(6.98));
  yazi("Berlin", { x: 200, y: LB, boyut: ETIKET, aile: "Fredoka", agirlik: 700, hizala: "orta",
    bas: fr(7.25), sure: 8, olcek: true, ses: "tik" });
  await S.svgCiz("tabler/calendar.svg", { kutu: [700, 950, 340, 340], bas: fr(7.54), sure: 22, azami: 25,
    w: 4, sesAralik: 1 });
  not("takvim çizimi", fr(7.54));
  yazi("2 years", { x: 870, y: LB, boyut: ETIKET, aile: "Fredoka", agirlik: 700, hizala: "orta",
    bas: fr(7.78), sure: 8, olcek: true, ses: "tik" });

  // ---------- Faz C (11,06–15,38): Ago var → Simple Past; Has moved yanlış ----------
  const lab = cumle(s2.slice(12, 15).map((k) => ({ s: k.s, f: k.f })),
    { x: SOL, y: 455, boyut: 88, aile: "Caveat", agirlik: 700 });
  not("Ago var yani", lab[0].bas);
  {   // Simple Past (12,34 / 12,66): büyük, sarı daire
    const y = 625, x0 = (1080 - genislik("Simple Past", "700 130px Fredoka")) / 2;
    const sp = cumle([{ s: "Simple", f: s2[15].f }, { s: "Past", f: s2[16].f }],
      { x: x0, y, boyut: 130, aile: "Fredoka", agirlik: 700 });
    not("Simple Past yazılır", sp[0].bas);
    const cx = (sp[0].x0 + sp[1].x1) / 2, w = sp[1].x1 - sp[0].x0;
    const d = daire(cx, y - 46, w / 2 + 34, 86, { bas: fr(12.80), sure: 18 });
    olay(bitis(d), "tik", 0.5); not("Simple Past daire", d.bas);
    parilti(sp[1].x1 + 36, y - 120, { bas: fr(12.80) + 10, r: 30, periyot: 150, adet: 1 });
  }
  {   // Has moved (13,62 / 13,94) + kırmızı çarpı (14,50 yanlış) + yanlış olurdu.
    const y = 790, x0 = (1080 - genislik("Has moved", "700 110px Fredoka")) / 2;
    const hm = cumle([{ s: "Has", f: s2[17].f }, { s: "moved", f: s2[18].f }],
      { x: x0, y, boyut: 110, aile: "Fredoka", agirlik: 700 });
    not("Has moved yazılır", hm[0].bas);
    const xa = hm[0].x0 - 14, xb = hm[1].x1 + 14, ust = y - 84, alt = y + 18;
    const o = { w: 12, renk: KIRMIZI, alfa: 0.92, bas: fr(14.50), sure: 7, duz: true, uc0: 6, uc1: 6, amp: 0.3 };
    ciz([[xa, ust], [xb, alt]], o);
    ciz([[xb, ust], [xa, alt]], { ...o, bas: fr(14.50) + 6 });
    not("Has moved kırmızı çarpı", fr(14.50));
    const yo = 880, wy = genislik("yanlış olurdu.", "700 80px Caveat");
    cumle([{ s: "yanlış", f: s2[19].f }, { s: "olurdu.", f: s2[20].f }],
      { x: (1080 - wy) / 2, y: yo, boyut: 80, aile: "Caveat", agirlik: 700 });
  }
  return S;
}

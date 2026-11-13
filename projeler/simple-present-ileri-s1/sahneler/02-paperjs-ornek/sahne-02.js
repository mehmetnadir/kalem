// Sahne 02 (simple-present-ileri-s1) — Örnek: Paper.js, 1080x1920, 297 kare, t_bas 3,00; cümle 1 sonu + cümle 2.
// Yerel kare = round((t − 3,00) × 30). İlk 12 kare geçiş altında: sahne 01'in son hali hazır çizili
// (Tarife varsa / will + kırmızı çarpı / deme. + figür + otobüs). Dikey v2 bantları:
// içerik 352–1392, üst bölge (392–900) yazı, alt bölge (920–1392) nesneler, altyazı 1400–1536.
import { sahneKur, RT } from "/projeler/simple-present-ileri-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 297, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Trap" });
  const { fr, ciz, daire, yazi, elYazisi, cumle, kutu, olay, not, bitis, genislik, kis, oge,
    parilti } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil, KIRMIZI = RT.kirmizi;
  const sol = (f0, f1) => (f) => 1 - kis((f - f0) / (f1 - f0));     // oge: [f0, f1] arası söner
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, tur: "isaret", ad: o.ad || "altCiz", ...o });

  // ---------- Faz A (3,0–3,58): sahne 01'in son hali hazır; 3,40–3,58 söner ----------
  const A0 = fr(3.40), A1 = fr(3.58);
  const gA = oge({ alfa: sol(A0, A1) }), fSon = [A0, A1];
  const SOL = 72;
  cumle(s1.slice(0, 2).map((w) => ({ s: w.s, f: -30 })),
    { x: SOL, y: 500, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  const wl = cumle([{ s: "will", f: -30 }],
    { x: SOL, y: 650, boyut: 88, aile: "Fredoka", agirlik: 700, son: fSon });
  cumle([{ s: s1[3].s, f: -30 }], { x: SOL, y: 800, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  {   // kırmızı çarpı (sahne 01 ile aynı yol; hazır çizili)
    const x0 = SOL - 14, x1 = wl[0].x1 + 14, ust = 650 - 72, alt = 650 + 26;
    const o = { w: 12, renk: KIRMIZI, alfa: 0.92, bas: -400, sure: 2, duz: true, uc0: 6, uc1: 6, amp: 0.3,
      ses: false, oge: gA };
    ciz([[x0, ust], [x1, alt]], o); ciz([[x1, ust], [x0, alt]], o);
  }
  // figür (standing-3) + otobüs + zemin çizgisi: sahne 01 ile aynı kutular, hazır çizili
  await S.svgCiz("open-peeps/standing-3.svg", { kutu: [150, 950, 213 * 0.628, 701 * 0.628], bas: -400,
    sure: 100, azami: 60, yuz: 3, w: 4.4, oge: gA, sessiz: true });
  await S.svgCiz("tabler/bus.svg", { kutu: [408, 912, 576, 576], bas: -400, sure: 100, azami: 25, w: 4,
    oge: gA, sessiz: true });
  ciz([[96, 1388], [560, 1386], [1000, 1388]], { w: 4, bas: -400, sure: 2, ses: false, duz: true, oge: gA });

  // ---------- Faz B (3,55–8,60): EN kart + TR çeviri + nesneler (uçak, saat, takvim) ----------
  const B0 = fr(8.60), B1 = fr(8.78);
  const gB = oge({ alfa: sol(B0, B1) }), bSon = [B0, B1];
  const KY = 392, SH = 88, B1Y = KY + 40 + 58;                  // kart üstü 392, ilk taban 490, ikinci 578
  kutu(48, KY, 984, 246, { bas: fr(3.55) - 6, sure: 30, w: 4, renk: IKI, oge: gB });
  not("kart kutusu", fr(3.55) - 6);
  const en = s2.slice(0, 7).map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 }));
  const e = cumle(en, { x: 88, y: B1Y, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: SH, son: bSon });
  not("EN cümle başı", e[0].bas);
  altCiz({ x0: e[2].x0, x1: e[3].x1, y: e[2].y }, fr(4.15), { oge: gB }); not("takes off altı çizgi", fr(4.15));
  {   // tomorrow. sarı daire (5,07)
    const g = e[6], d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 8, 44, { bas: g.bas + 3, sure: 16, oge: gB });
    olay(bitis(d), "tik", 0.5); not("tomorrow daire", d.bas);
  }
  // TR çeviri (5,96–8,60 sn; kare 89–168): her sözcük kendi penceresinde, el yazısı Caveat 80;
  // sözcük arası 0,3 × boyut (motor aralığı); satır 1 = Uçuşumuz yarın, satır 2 = dokuzda kalkar.
  // "kalkar." penceresi 7,28–8,60 sn; sözcük sonu sessizliği: yazı 24 karede (8,08 sn) biter,
  // kart 8,60'ta söner. Altı çizgi yazı bitişinden önce başlar.
  const tr = [];
  {
    let tx = 72;
    s2.slice(7, 11).forEach((k, i) => {
      if (i === 2) tx = 72;
      tr.push(elYazisi(k.s, { x: tx, y: 735 + (i < 2 ? 0 : 90), boyut: 80, oge: gB,
        sozcukler: [{ f0: k.f, f1: i === 3 ? Math.min(k.f1, k.f + 24) : k.f1 }] }));
      tx = tr[i].x1 + 0.3 * 80;
    });
  }
  not("TR çeviri başı", tr[0].bas);
  altCiz(tr[3], Math.min(tr[3].bit - 6, B0 - 12), { oge: gB });
  not("kalkar altı çizgi", Math.min(tr[3].bit - 6, B0 - 12));

  // nesneler (alt bölge 920–1392, üç sütun; sütun ortaları 200 / 540 / 870) — sahne sonuna kadar kalır
  const LB = 1342, ETIKET = 64;
  await S.svgCiz("tabler/plane.svg", { kutu: [20, 920, 360, 360], bas: fr(3.79), sure: 22, azami: 25,
    w: 4, sesAralik: 2 });
  not("uçak çizimi", fr(3.79));
  yazi("takes off", { x: 200, y: LB, boyut: ETIKET, aile: "Fredoka", agirlik: 700, hizala: "orta",
    bas: fr(4.15) + 3, sure: 8, olcek: true, ses: "tik" });
  {   // saat 9:00: kadran + akrep sola (9), yelkovan yukarı (12); tabler/clock'un 4:30 elleri kullanılmaz
    const cx = 540, cy = 1100, r = 135, f0 = fr(4.75), k = { renk: RT.murekkep, duz: true, amp: 0.5 };
    daire(cx, cy, r, r, { renk: RT.murekkep, w: 5, alfa: 0.92, tur: 1.04, bas: f0, sure: 14 });
    for (const [x1, y1, x2, y2] of [[cx, cy - r + 14, cx, cy - r + 32], [cx + r - 14, cy, cx + r - 32, cy],
      [cx, cy + r - 14, cx, cy + r - 32], [cx - r + 14, cy, cx - r + 32, cy]]) {
      ciz([[x1, y1], [x2, y2]], { ...k, w: 5, bas: f0 + 10, sure: 3, ses: false });
    }
    ciz([[cx, cy], [cx, cy - 92]], { ...k, w: 6, bas: f0 + 12, sure: 5 });
    ciz([[cx, cy], [cx - 66, cy]], { ...k, w: 8, bas: f0 + 15, sure: 5, ses: false });
  }
  not("saat çizimi", fr(4.75));
  yazi("9:00", { x: 540, y: LB + 4, boyut: 96, aile: "Fredoka", agirlik: 700, hizala: "orta", renk: SARI,
    bas: fr(4.75) + 8, sure: 8, olcek: true, ses: "tik" });
  await S.svgCiz("tabler/calendar.svg", { kutu: [690, 920, 360, 360], bas: fr(5.07), sure: 22, azami: 25,
    w: 4, sesAralik: 1 });
  not("takvim çizimi", fr(5.07));
  yazi("tomorrow", { x: 870, y: LB, boyut: ETIKET, aile: "Fredoka", agirlik: 700, hizala: "orta",
    bas: fr(5.07) + 8, sure: 8, olcek: true, ses: "tik" });

  // ---------- Faz C (8,75–12,51): Tarife kesin: tomorrow ≠ will → Simple Present ----------
  // "Tarife kesin:" 8,75–10,03 sn (kare 172–211): her sözcük kendi penceresinde, Caveat 88
  const lab = [];
  {
    let tx = SOL;
    s2.slice(11, 13).forEach((k, i) => {
      lab.push(elYazisi(k.s, { x: tx, y: 480, boyut: 88, sozcukler: [{ f0: k.f, f1: k.f1 }] }));
      tx = lab[i].x1 + 0.3 * 88;
    });
  }
  not("Tarife kesin", lab[0].bas);
  altCiz(lab[1], lab[1].bit - 6, { w: 10 }); not("kesin altı çizgi", lab[1].bit - 6);
  {
    const F = "700 120px Fredoka", gT = genislik("tomorrow", F), gW = genislik("will", F), gE = 96, bos = 36;
    const x0 = (1080 - (gT + bos + gE + bos + gW)) / 2, y = 690;
    const t = yazi("tomorrow", { x: x0, y, boyut: 120, aile: "Fredoka", agirlik: 700, bas: fr(10.07), sure: 10,
      olcek: true, ses: "tik" });
    not("tomorrow yazılır", t.bas);
    const cx = t.x1 + bos + gE / 2, cy = y - 44, k = { w: 10, renk: SARI, alfa: 0.92, duz: true, amp: 0.4 };
    ciz([[cx - 40, cy - 14], [cx + 40, cy - 14]], { ...k, bas: fr(10.51), sure: 6, uc0: 5, uc1: 6 });
    ciz([[cx - 40, cy + 18], [cx + 40, cy + 18]], { ...k, bas: fr(10.51) + 5, sure: 6, uc0: 5, uc1: 6 });
    ciz([[cx + 24, cy - 52], [cx - 24, cy + 56]], { ...k, bas: fr(10.51) + 10, sure: 6, uc0: 5, uc1: 6 });
    not("≠ işareti", fr(10.51));
    const w = yazi("will", { x: cx + gE / 2 + bos, y, boyut: 120, aile: "Fredoka", agirlik: 700, bas: fr(10.83),
      sure: 10, olcek: true, ses: "tik" });
    not("will yazılır", w.bas);
    const c = ciz([[w.x0 - 14, y - 36], [w.x1 + 14, y - 52]], { w: 13, renk: KIRMIZI, alfa: 0.92, bas: fr(11.23),
      sure: 9, duz: true, uc0: 6, uc1: 8, amp: 0.4 });
    not("will kırmızı çizgi", c.bas);
  }
  {   // Simple Present (11,47 / 11,79): büyük, sarı çizgi + parıltı
    const x3 = (1080 - genislik("Simple Present", "700 130px Fredoka")) / 2;
    const sp = cumle([{ s: "Simple", f: s2[17].f }, { s: "Present", f: s2[18].f }],
      { x: x3, y: 870, boyut: 130, aile: "Fredoka", agirlik: 700 });
    not("Simple Present yazılır", sp[0].bas);
    const u = altCiz({ x0: sp[0].x0, x1: sp[1].x1, y: 870 + 14 }, fr(11.79) + 8, { w: 14, sure: 12 });
    not("Simple Present altı çizgi", u.bas);
    parilti(sp[1].x1 + 36, 870 - 120, { bas: fr(11.79) + 10, r: 30, periyot: 150, adet: 1 });
  }
  return S;
}

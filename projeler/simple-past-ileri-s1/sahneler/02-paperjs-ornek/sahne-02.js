// Sahne 02 (simple-past-ileri-s1) — Örnek: Paper.js, 1080x1920, 362 kare, t_bas 3,00; cümle 1 sonu + cümle 2.
// Yerel kare = round((t − 3,00) × 30). İlk 12 kare geçiş altında: sahne 01'in son hali hazır çizili
// (Ago görürsen / Present Perfect + figür + saat); `yazma.` ve Perfect üstündeki kırmızı çizgi 3,04'te yazılır.
// Dikey v2 bantları: içerik 352–1392, üst bölge (392–900) yazı, alt bölge (920–1392) nesneler,
// altyazı 1400–1536 (altyazi.json).
import { sahneKur, RT } from "/projeler/simple-past-ileri-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 362, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Trap" });
  const { fr, ciz, daire, yazi, elYazisi, cumle, kutu, olay, not, bitis, genislik, kis, oge,
    parilti } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil, KIRMIZI = RT.kirmizi;
  const sol = (f0, f1) => (f) => 1 - kis((f - f0) / (f1 - f0));     // oge: [f0, f1] arası söner
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  // El yazısı cümlesi (Caveat 700 tegaki, dalga 5 / K26): her sözcük kendi konuşma penceresinde;
  // sözcük arası 0,3 × boyut (motor aralığı); pencere en az 10 kare, aynı satırdaki sonraki
  // sözcüğün başını aşmaz. kel = [{s, f, f1, satir}] -> elYazisi dönüşleri.
  const elCumle = (kel, o) => {
    const sat = {};
    return kel.map((k, i) => {
      const s = k.satir || 0, x = sat[s] == null ? o.x : sat[s];
      const n = kel.find((q, j) => j > i && (q.satir || 0) === s);
      const f1 = Math.min(Math.max(k.f1, k.f + 10), n ? Math.max(n.f, k.f1) : 1e9);
      const q = elYazisi(k.s, { x, y: o.y + s * (o.aralik || 80), boyut: o.boyut, oge: o.oge,
        sozcukler: [{ f0: k.f, f1 }] });
      sat[s] = q.x1 + 0.3 * o.boyut;
      return q;
    });
  };
  // söner + 36 px yukarı kayar (eski yazi `son` davranışı)
  const sonKay = (f0, f1) => oge({ alfa: sol(f0, f1), kay: { f0, f1, dx: 0, dy: -36 } });
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, ...o });

  // ---------- Faz A (3,0–3,68): sahne 01'in son hali; 3,50–3,68 söner ----------
  const A0 = fr(3.50), A1 = fr(3.68);
  const gA = oge({ alfa: sol(A0, A1) }), fSon = [A0, A1];
  const SOL = 72;
  cumle(s1.slice(0, 2).map((w) => ({ s: w.s, f: -30 })),
    { x: SOL, y: 500, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  const pp = cumle(s1.slice(2, 4).map((w) => ({ s: w.s, f: -30 })),
    { x: SOL, y: 650, boyut: 88, aile: "Fredoka", agirlik: 700, son: fSon });
  // 3,04–3,50 «yazma.» (kare 1–15): sönme A0 = 15'te başlar, yazı sönme başlamadan biter
  // (konuşma 3,56'ya dek sürer; pencere A0'a kısılır — inceleme DÜZELT)
  elYazisi(s1[4].s, { x: SOL, y: 800, boyut: 88, sozcukler: [{ f0: s1[4].f, f1: A0 }],
    oge: sonKay(A0, A1) });
  {   // Perfect üstünde kırmızı çizgi (3,04): tek hızlı çizgi, hafif eğik
    const pf = pp[1];
    ciz([[pf.x0 - 12, 650 - 20], [pf.x1 + 12, 650 - 42]], { w: 12, renk: KIRMIZI, alfa: 0.92,
      bas: fr(3.04), sure: 7, duz: true, uc0: 6, uc1: 6, amp: 0.3, oge: gA });
  }
  // figür (standing-3) + saat + zemin çizgisi: sahne 01 ile aynı kutular, hazır çizili; 5,85–5,98 söner
  const gAlt = oge({ alfa: sol(fr(5.85), fr(5.98)) });
  await S.svgCiz("open-peeps/standing-3.svg", { kutu: [150, 950, 213 * 0.628, 701 * 0.628], bas: -400,
    sure: 100, azami: 60, yuz: 3, w: 4.4, oge: gAlt, sessiz: true });
  await S.svgCiz("tabler/clock.svg", { kutu: [500, 950, 480, 480], bas: -400, sure: 100, azami: 25, w: 4,
    oge: gAlt, sessiz: true });
  ciz([[96, 1388], [560, 1386], [1000, 1388]], { w: 4, bas: -400, sure: 2, ses: false, duz: true,
    oge: gAlt });

  // ---------- Faz A2 (3,71–5,92): Sınav bu tuzağı sever ----------
  {
    const L0 = fr(5.75), L1 = fr(5.92), gL = oge({ alfa: sol(L0, L1) });
    // 3,71–5,55 «Sınav bu tuzağı sever.» (kare 21–77): "bu" penceresi 2 → 10 kare (satır 1'de
    // sonraki sözcük yok); altı çizgi tuzağı bitince (bit − 6)
    const e = elCumle(s1.slice(5, 9).map((k, i) => ({ s: k.s, f: k.f, f1: k.f1,
      satir: i < 2 ? 0 : 1 })), { x: SOL, y: 620, boyut: 120, aralik: 150, oge: sonKay(L0, L1) });
    not("Sınav bu tuzağı sever", e[0].bas);
    altCiz(e[2], e[2].bit - 6, { w: 11, sure: 14, oge: gL });
    not("tuzağı altı çizgi", e[2].bit - 6);
  }

  // ---------- Faz B (5,96–11,0): EN kart + TR çeviri + figür + takvim ----------
  const B0 = fr(10.85), B1 = fr(10.98);
  const gB = oge({ alfa: sol(B0, B1) }), bSon = [B0, B1];
  const KY = 392, SH = 88, B1Y = KY + 40 + 58;                  // kart üstü 392, ilk taban 490, ikinci 578
  kutu(48, KY, 984, 246, { bas: fr(5.96), sure: 30, w: 4, renk: IKI, oge: gB });
  not("kart kutusu", fr(5.96));
  const en = s2.slice(0, 6).map((k, i) => ({ s: k.s, f: k.f, satir: i < 3 ? 0 : 1 }));
  const e = cumle(en, { x: 88, y: B1Y, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: SH, son: bSon });
  not("EN cümle başı", e[0].bas);
  {   // ago. sarı daire (7,94)
    const g = e[5], d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 8, 44, { bas: g.bas + 3, sure: 16, oge: gB });
    olay(bitis(d), "tik", 0.5); not("ago daire", d.bas);
  }
  // TR çeviri (8,59–10,83; kare 168–235) Caveat 80: "iki" penceresi 5 → 7 kare (hafta başına dek),
  // "önce" 6 → 10 kare; altı çizgi önce bitince (bit − 6)
  const tr = elCumle(s2.slice(6, 12).map((k, i) => ({ s: k.s, f: k.f, f1: k.f1,
    satir: i < 4 ? 0 : 1 })), { x: 72, y: 735, boyut: 80, aralik: 90, oge: sonKay(B0, B1) });
  not("TR çeviri başı", tr[0].bas);
  altCiz({ x0: tr[2].x0, x1: tr[3].x1, y: tr[3].y }, tr[3].bit - 6, { oge: gB });
  not("hafta önce altı çizgi", tr[3].bit - 6);

  // alt bölge (920–1392): yeni figür (standing-1) + takvim + geri ok + etiket; Faz C boyunca kalır
  const LB = 1360, ETIKET = 64;
  await S.svgCiz("open-peeps/standing-1.svg", { kutu: [150, 950, 213 * 0.6, 715 * 0.6], bas: fr(6.2),
    sure: 48, azami: 60, yuz: 3, w: 4.4 });
  not("figür çizimi", fr(6.2));
  await S.svgCiz("tabler/calendar.svg", { kutu: [610, 920, 440, 440], bas: fr(6.2), sure: 30, azami: 25,
    w: 4, sesAralik: 2 });
  not("takvim çizimi", fr(6.2));
  yazi("2 weeks", { x: 830, y: LB, boyut: ETIKET, aile: "Fredoka", agirlik: 700, hizala: "orta",
    bas: fr(7.54), sure: 8, olcek: true, ses: "tik" });
  S.ok([660, 1150], [380, 1150], { bas: fr(7.94) + 4, sure: 18, w: 7, bukum: 0.05 });
  not("geri ok", fr(7.94) + 4);

  // ---------- Faz C (10,98–14,65): Ago belirli zaman, yani Simple Past ----------
  // 10,98–12,58 «Ago belirli zaman,» (kare 239–287); altı çizgi zaman, bitince (bit − 6)
  const lab = elCumle(s2.slice(12, 15).map((k) => ({ s: k.s, f: k.f, f1: k.f1 })),
    { x: SOL, y: 480, boyut: 88 });
  not("Ago belirli zaman", lab[0].bas);
  altCiz({ x0: lab[1].x0, x1: lab[2].x1, y: lab[2].y }, lab[2].bit - 6, { w: 10 });
  not("belirli zaman altı çizgi", lab[2].bit - 6);
  {
    const F = "700 120px Fredoka", gA2 = genislik("ago", F);
    const ox = (1080 - (gA2 + 36 + 158)) / 2;                       // "ago" + ok satırı ortalı
    const ag = yazi("ago", { x: ox, y: 700, boyut: 120, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: s2[15].f, sure: 10, olcek: true, ses: "tik" });
    not("ago yazılır", ag.bas);
    const ax = ox + gA2 + 36, k = { w: 10, renk: SARI, alfa: 0.92, duz: true, amp: 0.4 };
    ciz([[ax, 656], [ax + 150, 656]], { ...k, bas: fr(12.9), sure: 8, uc0: 5, uc1: 6 });
    ciz([[ax + 112, 616], [ax + 158, 656]], { ...k, bas: fr(12.9) + 7, sure: 5, uc0: 4, uc1: 5 });
    ciz([[ax + 158, 656], [ax + 112, 696]], { ...k, bas: fr(12.9) + 11, sure: 5, uc0: 4, uc1: 5 });
    not("ok", fr(12.9));
  }
  {   // Simple Past (13,14 / 13,70): büyük, sarı çizgi + parıltı
    const x3 = (1080 - genislik("Simple Past", "700 130px Fredoka")) / 2;
    const sp = cumle([{ s: "Simple", f: s2[16].f }, { s: "Past", f: s2[17].f }],
      { x: x3, y: 870, boyut: 130, aile: "Fredoka", agirlik: 700 });
    not("Simple Past yazılır", sp[0].bas);
    const u = altCiz({ x0: sp[0].x0, x1: sp[1].x1, y: 870 + 14 }, fr(13.70) + 8, { w: 14, sure: 12 });
    not("Simple Past altı çizgi", u.bas);
    parilti(sp[1].x1 + 36, 870 - 120, { bas: fr(13.70) + 10, r: 30, periyot: 150, adet: 1 });
  }
  return S;
}

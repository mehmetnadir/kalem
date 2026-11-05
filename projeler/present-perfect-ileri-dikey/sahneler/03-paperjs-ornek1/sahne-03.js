// Sahne 03 (İLERİ, DİKEY 1080x1920) — Kök 1 (490 kare, t_bas 17,97; cümle 3). Yerel kare = round((t − 17,97) × 30).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (kalem-paper.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–708) · TR 3 satır (740–920) · sahne 940–1360 (29,4'te 0,52'ye toplanır) · formül kartı (1172–1392).
import { sahneKur, RT } from "/projeler/present-perfect-ileri-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 490, T_BAS = 17.97;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Exam Q 1 / 3", etkin: 2, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, cumle, altCizgi, parilti, olay, not, bitis } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  const GB = 12;
  const f0 = (t) => Math.max(GB, fr(t));

  // --- 18,52: kart çerçevesi (el kutusu, 4 px) + sağ üst köşede daire içinde 1
  kutu(48, 372, 984, 336, { bas: f0(18.52), sure: 30, w: 4.2, renk: IKI }); not("kart çerçevesi", f0(18.52));
  const d1 = daire(962, 442, 46, 44, { bas: f0(18.75), sure: 22, a0: -2.6, w: 9 }); olay(bitis(d1), "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 962, y: 474, hizala: "orta", boyut: 78, aile: "Fredoka", agirlik: 700, bas: f0(19.1), sure: 10, olcek: true });

  // --- 19,65–23,80: İngilizce kök (Fredoka 64, 4 satır, sözcük zamanlı); satır başı 0 / 4 / 8 / 12
  const sz = S.sozcukler(3).slice(2, 16);                          // Ever … doubled.
  const satirNo = (i) => (i < 4 ? 0 : i < 8 ? 1 : i < 12 ? 2 : 3);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 88, y: 452, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 78 });
  altCizgi(cz, { tut: 40, w: 8 }); not("cümle başı (Ever)", cz[0].bas);

  const cevre = (a, b, bas, egim, ad, pay = 6, ry = 40) => {       // sözcük(ler)i saran sarı daire
    const x0 = cz[a].x0, x1 = cz[b].x1, y = cz[a].y - 24;
    const d = daire((x0 + x1) / 2, y, (x1 - x0) / 2 + pay, ry, { bas, sure: 22, a0: -2.6, egim, w: 10 });
    olay(bitis(d), "tik", 0.5); not(ad, d.bas); return d;
  };
  cevre(1, 1, fr(20.01), -0.03, "since daire", 10);
  cevre(4, 4, fr(20.69), -0.025, "launched daire", 10);

  // --- 20,0–23,5: ORTA sahne (940–1360): tek grupta; telefon (420 px) + 3 sütunlu grafik, sayı ikiye katlanır
  const G = S.oge({ topla: { f0: fr(29.4), f1: fr(30.1), ax: 540, ay: 940, olcek: 0.52, dy: 0 } });
  await S.svgCiz("tabler/phone.svg", { kutu: [40, 950, 400, 400], bas: f0(20.0), sure: fr(21.0) - f0(20.0), azami: 12, yuz: 1,
    w: 5, oge: G, sesAralik: 2 });
  not("telefon çizimi başı", f0(20.0));
  const yT = 1350, bx = [470, 640, 810], bh = [150, 225, 300];
  ciz([[440, yT + 2], [700, yT - 1], [990, yT + 1]], { w: 5, renk: IKI, alfa: 0.9, bas: fr(21.1), sure: 14, uc0: 10, uc1: 16, oge: G });
  not("grafik tabanı", fr(21.1));
  bx.forEach((x, i) => {
    const b = fr(21.3 + i * 0.55);
    kutu(x, yT - bh[i], 130, bh[i], { bas: b, sure: 16, w: 5, renk: i === 2 ? SARI : IKI, oge: G });
    olay(b + 16, "tik", 0.5); not(`sütun ${i + 1}`, b);
  });
  const o1 = ok([700, 1085], [830, 1020], { bas: fr(23.2), sure: 12, w: 9, uzun: 26, bukum: -0.1, oge: G });
  const x2 = yazi("x2", { x: 480, y: 1085, boyut: 130, aile: "Fredoka", agirlik: 700, renk: SARI, bas: bitis(o1) + 2, sure: 10, ses: true });
  G.g.addChild(x2.g);                                              // yazı da grupla birlikte toplanır
  not("x2 ve ok", fr(23.2));

  // --- 24,46–29,58: Türkçe çeviri (Caveat 64 mürekkep, 3 satır), sözcük zamanlı
  const tr = S.sozcukler(3).slice(16, 25);                          // Şirket … katlandı.
  const tz = cumle(tr.map((k, i) => ({ s: k.s, f: k.f, satir: i < 3 ? 0 : i < 6 ? 1 : 2 })),
    { x: 88, y: 772, boyut: 64, aile: "Caveat", agirlik: 700, aralik: 66, renk: KRE });
  not("Türkçe çeviri", tz[0].bas);
  not("sahne toplanır (0,52)", fr(29.4));

  // --- 30,0–33,89: formül kartı (el kutusu 4 px): since + Simple Past -> Present Perfect (Fredoka 72)
  kutu(48, 1172, 984, 220, { bas: fr(30.0), sure: 26, w: 4.2, renk: IKI }); not("formül kartı kutusu", fr(30.0));
  const F = { boyut: 72, aile: "Fredoka", agirlik: 700 };
  const a1 = yazi("since", { ...F, x: 100, y: 1262, bas: fr(30.25), sure: 10, olcek: true, renk: SARI, ses: true });
  const a2 = yazi("+", { ...F, x: a1.x1 + 18, y: 1262, bas: fr(30.5), sure: 8, olcek: true });
  yazi("Simple Past", { ...F, x: a2.x1 + 18, y: 1262, bas: fr(30.77), sure: 10, olcek: true, ses: true }); not("since + Simple Past", fr(30.25));
  parilti(cz[4].x1 + 40, cz[4].y - 70, { bas: fr(30.77), r: 26 }); not("launched vurgusu (parıltı)", fr(30.77));
  const b1 = yazi("→", { ...F, x: 100, y: 1358, bas: fr(32.45), sure: 8, olcek: true, renk: IKI });
  yazi("Present Perfect", { ...F, x: b1.x1 + 22, y: 1358, bas: fr(32.85), sure: 10, olcek: true, ses: true }); not("Present Perfect", fr(32.85));
  cevre(12, 13, fr(32.85), -0.02, "has doubled daire", 10);
  parilti(960, 1215, { bas: fr(33.3), r: 28 });
  return S;
}

// Sahne 03 (İLERİ, DİKEY 1080x1920) — Kök 1 (490 kare, t_bas 17,97; cümle 3). Yerel kare = round((t − 17,97) × 30).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (kalem-paper.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–664) · TR 2 satır (720–785) · ORTA telefon 420 px + grafik (816–1236) · iki satır formül kartı (1252–1392).
// Toplanma / küçültme YOK: figür/grafik baştan sona ≥ 420 px.
import { sahneKur, RT } from "/projeler/present-perfect-ileri-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 490, T_BAS = 17.97;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Exam Q 1 / 3", etkin: 2, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, parilti, olay, not,
    bitis } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  const GB = 12;
  const f0 = (t) => Math.max(GB, fr(t));

  // --- 18,52: kart çerçevesi (el kutusu, 4 px) + sağ üst köşede daire içinde 1
  kutu(48, 372, 984, 292, { bas: f0(18.52), sure: 30, w: 4.2, renk: IKI }); not("kart çerçevesi", f0(18.52));
  const d1 = daire(962, 420, 36, 36, { bas: f0(18.75), sure: 22, a0: -2.6, w: 8 }); olay(bitis(d1), "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 962, y: 442, hizala: "orta", boyut: 64, aile: "Fredoka", agirlik: 700, bas: f0(19.1), sure: 10, olcek: true });

  // --- 19,65–23,80: İngilizce kök (Fredoka 64, 4 satır, sözcük zamanlı); satır başı 0 / 4 / 8 / 12
  const sz = S.sozcukler(3).slice(2, 16);                          // Ever … doubled.
  const satirNo = (i) => (i < 4 ? 0 : i < 8 ? 1 : i < 12 ? 2 : 3);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 88, y: 442, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 68 });
  altCizgi(cz, { tut: 40, w: 8 }); not("cümle başı (Ever)", cz[0].bas);

  const cevre = (a, b, bas, egim, ad, pay = 6, ry = 38) => {       // sözcük(ler)i saran sarı daire
    const x0 = cz[a].x0, x1 = cz[b].x1, y = cz[a].y - 24;
    const d = daire((x0 + x1) / 2, y, (x1 - x0) / 2 + pay, ry, { bas, sure: 22, a0: -2.6, egim, w: 10 });
    olay(bitis(d), "tik", 0.5); not(ad, d.bas); return d;
  };
  cevre(1, 1, fr(20.01), -0.03, "since daire", 10);
  cevre(4, 4, fr(20.69), -0.025, "launched daire", 10);

  // --- 24,46–29,58: Türkçe çeviri (Caveat 64 mürekkep, 2 satır), el yazısı, sözcük penceresi.
  // Satır 1 tegaki genişliği 949 px: x = 88 → sağ uç 1037 > 1032; x = 76 → 1025 (iki satır aynı x).
  // 0,2 sn'den kısa pencere (yeni 25,02–25,18 · ama gibi) sonraki sözcüğün başına dek uzar.
  const tr = S.sozcukler(3).slice(16, 25);                          // Şirket … katlandı.
  const pen = (i0, n) => tr.slice(i0, i0 + n).map((w, i) => ({ f0: w.f,
    f1: w.f1 - w.f < 6 && tr[i0 + i + 1] ? tr[i0 + i + 1].f : w.f1 }));
  elYazisi("Şirket yeni uygulamasını çıkardığından beri", { x: 76, y: 720, boyut: 64, renk: KRE,
    sozcukler: pen(0, 5) });
  const tz = elYazisi("kullanıcı sayısı ikiye katlandı.", { x: 76, y: 785, boyut: 64, renk: KRE,
    sozcukler: pen(5, 4) });
  not("Türkçe çeviri", tz.bas);

  // --- 20,0–23,5: ORTA sahne (816–1236, 420 px): telefon (420 px) + 3 sütunlu grafik, sayı ikiye katlanır
  await S.svgCiz("tabler/phone.svg", { kutu: [50, 816, 380, 420], bas: f0(20.0), sure: fr(21.0) - f0(20.0), azami: 12, yuz: 1,
    w: 5, sesAralik: 2 });
  not("telefon çizimi başı", f0(20.0));
  const yT = 1236, bx = [480, 650, 820], bh = [150, 240, 330];
  ciz([[460, yT + 2], [720, yT - 1], [990, yT + 1]], { w: 5, renk: IKI, alfa: 0.9, bas: fr(21.1), sure: 14, uc0: 10, uc1: 16 });
  not("grafik tabanı", fr(21.1));
  bx.forEach((x, i) => {
    const b = fr(21.3 + i * 0.55);
    kutu(x, yT - bh[i], 130, bh[i], { bas: b, sure: 16, w: 5, renk: i === 2 ? SARI : IKI });
    olay(b + 16, "tik", 0.5); not(`sütun ${i + 1}`, b);
  });
  const o1 = ok([710, 971], [840, 906], { bas: fr(23.2), sure: 12, w: 9, uzun: 26, bukum: -0.1 });
  yazi("x2", { x: 500, y: 976, boyut: 130, aile: "Fredoka", agirlik: 700, renk: SARI, bas: bitis(o1) + 2, sure: 10, ses: true });
  not("x2 ve ok", fr(23.2));

  // --- 30,0–33,89: formül kartı iki satır (el kutusu 4 px): since + Simple Past / → Present Perfect (Fredoka 64)
  kutu(48, 1252, 984, 140, { bas: fr(30.0), sure: 26, w: 4.2, renk: IKI }); not("formül kartı kutusu", fr(30.0));
  const F = { boyut: 64, aile: "Fredoka", agirlik: 700 };
  const a1 = yazi("since", { ...F, x: 100, y: 1310, bas: fr(30.25), sure: 10, olcek: true, renk: SARI, ses: true });
  const a2 = yazi("+", { ...F, x: a1.x1 + 18, y: 1310, bas: fr(30.5), sure: 8, olcek: true, renk: IKI });
  const a3 = yazi("Simple Past", { ...F, x: a2.x1 + 18, y: 1310, bas: fr(30.77), sure: 10, olcek: true, ses: true });
  not("since + Simple Past", fr(30.25));
  parilti(cz[4].x1 + 40, cz[4].y - 70, { bas: fr(30.77), r: 26 }); not("launched vurgusu (parıltı)", fr(30.77));
  const b1 = yazi("→", { ...F, x: 100, y: 1378, bas: fr(32.45), sure: 8, olcek: true, renk: IKI });
  yazi("Present Perfect", { ...F, x: b1.x1 + 22, y: 1378, bas: fr(32.85), sure: 10, olcek: true, ses: true });
  not("Present Perfect", fr(32.85));
  cevre(12, 13, fr(32.85), -0.02, "has doubled daire", 10);
  parilti(960, 1322, { bas: fr(33.3), r: 28 });
  return S;
}

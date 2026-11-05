// Sahne 03 (İLERİ) — Kök 1 (490 kare, t_bas 17,97; cümle 3). Zamanlar BRIEF §4; yerel kare = round((t − 17,97) × 30).
// Kök: "Ever since the company launched its new app, the number of users has doubled." (since + Simple Past).
// elYazisi: 03 kopyası da taşır (05.11 motor taşıması 96b0651).
import { sahneKur, RT } from "/projeler/present-perfect-ileri/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 490, T_BAS = 17.97;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Exam Q 1 / 3", etkin: 2, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, cumle, altCizgi, parilti, olay, not, bitis,
    elYazisi } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12;                                                   // geçiş karesi: çizimler bundan sonra başlar
  const f0 = (t) => Math.max(GB, fr(t));

  // --- 18,52–19,30: büyük el çizimi daire içinde 1
  const d1 = daire(200, 190, 66, 62, { bas: f0(18.52), sure: 22, a0: -2.6 }); olay(bitis(d1), "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 226, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700, bas: f0(18.85), sure: 10, olcek: true });

  // --- 19,65–23,80: İngilizce kök (Fredoka 56, 3 satır, sözcük zamanlı)
  const sz = S.sozcukler(3).slice(2, 16);                          // Ever … doubled.
  const satirNo = (i) => (i < 5 ? 0 : i < 12 ? 1 : 2);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 140, y: 300, boyut: 56, aile: "Fredoka", agirlik: 700, aralik: 76 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (Ever)", cz[0].bas);

  // since (20,01) ve launched (20,69): sarı daire
  const cevre = (a, b, bas, egim, ad, pay = 4) => {
    const x0 = cz[a].x0, x1 = cz[b].x1, y = cz[a].y - 20;
    const d = daire((x0 + x1) / 2, y, (x1 - x0) / 2 + pay, 40, { bas, sure: 22, a0: -2.6, egim });
    olay(bitis(d), "tik", 0.5); not(ad, d.bas); return d;
  };
  cevre(1, 1, fr(20.01), -0.03, "since daire", 1);
  cevre(4, 4, fr(20.69), -0.025, "launched daire", 3);

  // --- 20,0–23,5: sağ sahne. Telefon (380 px) + 3 basamaklı sütun grafik (sayı ikiye katlanır)
  const ogeTel = S.oge({ nefes: { bas: fr(23.8), cx: 1300, cy: 540 } });
  await S.svgCiz("tabler/phone.svg", { kutu: [1150, 160, 300, 380], bas: f0(20.0), sure: fr(21.0) - f0(20.0), azami: 12, yuz: 1,
    w: 4, oge: ogeTel, sesAralik: 2 });
  not("telefon çizimi başı", f0(20.0));
  const yT = 560, bx = [1540, 1650, 1760], bh = [80, 120, 160];
  ciz([[1500, yT + 2], [1700, yT - 1], [1860, yT + 1]], { w: 4, renk: IKI, alfa: 0.9, bas: fr(21.1), sure: 14, uc0: 10, uc1: 16 });
  not("grafik tabanı", fr(21.1));
  bx.forEach((x, i) => {
    const b = fr(21.3 + i * 0.55);
    kutu(x, yT - bh[i], 80, bh[i], { bas: b, sure: 16, w: 4, renk: i === 2 ? SARI : IKI });
    olay(b + 16, "tik", 0.5); not(`sütun ${i + 1}`, b);
  });
  // 21,50–21,97 `launch` ve 22,90–23,37 `now`: el yazısı etiket (anlatımsız; sure 14 kare =
  // 0,47 sn), orta hizalı
  const ort = (s, cx, b) => cx - S.genislik(s, `700 ${b}px Caveat`) / 2;
  elYazisi("launch", { x: ort("launch", bx[0] + 40, 40), y: yT + 52, boyut: 40, renk: IKI,
    bas: fr(21.5), sure: 14 });
  elYazisi("now", { x: ort("now", bx[2] + 40, 40), y: yT + 52, boyut: 40, renk: IKI,
    bas: fr(22.9), sure: 14 });
  // doubled (23,25): x2 ve ok
  const o1 = ok([bx[0] + 40, yT - bh[0] - 30], [bx[2] + 40, yT - bh[2] - 34], { bas: fr(23.2), sure: 12, w: 6.5, uzun: 20, bukum: -0.12 });
  yazi("x2", { x: 1640, y: yT - 215, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700, renk: SARI, bas: bitis(o1) + 2, sure: 10, olcek: true, ses: true });
  not("x2 ve ok", fr(23.2));
  parilti(1760, yT - 250, { bas: fr(23.4), r: 24 });

  // --- 24,46–29,58: Türkçe çeviri (Caveat 48 ikincil, 2 satır), sözcük zamanlı
  const tr = S.sozcukler(3).slice(16, 25);                          // Şirket … katlandı.
  // el yazısı, her sözcük kendi konuşma penceresinde (Şirket 24,46 … katlandı. 28,38–29,58)
  // satır 1: 5 sözcük, satır 2: 4 sözcük
  const pen = (a) => a.map((w) => ({ f0: w.f, f1: w.f1 }));
  elYazisi("Şirket yeni uygulamasını çıkardığından beri", { x: 140, y: 590, boyut: 48, renk: IKI,
    sozcukler: pen(tr.slice(0, 5)) });
  elYazisi("kullanıcı sayısı ikiye katlandı.", { x: 140, y: 590 + 58, boyut: 48, renk: IKI,
    sozcukler: pen(tr.slice(5, 9)) });
  not("Türkçe çeviri", tr[0].f);

  // --- 29,73–33,89: iki kutu + ok. since + Simple Past -> Present Perfect (has doubled)
  {
    const F = { aile: "Fredoka", agirlik: 700 };
    const k1 = { x: 140, y: 740, w: 640, h: 200 }, k2 = { x: 1040, y: 740, w: 720, h: 200 };
    kutu(k1.x, k1.y, k1.w, k1.h, { bas: fr(29.73), sure: 22, w: 4.2, renk: IKI }); olay(fr(29.73), "tik", 0.5);
    not("kutu 1 (since + Simple Past)", fr(29.73));
    yazi("since", { ...F, boyut: 60, x: k1.x + 40, y: k1.y + 84, bas: fr(30.13), sure: 10, olcek: true, ses: true });
    const p1 = yazi("+ Simple Past", { ...F, boyut: 60, x: k1.x + 210, y: k1.y + 84, bas: fr(30.85), sure: 10, olcek: true, ses: true });
    // 30,28–30,78 `launched` (el yazısı, daire 30,77'de başlamadan biter; eski belirme 30,60)
    const l1 = elYazisi("launched", { boyut: 52, x: k1.x + 40, y: k1.y + 164, renk: SARI,
      bas: fr(30.28), sure: 15 });
    const dl = daire((l1.x0 + l1.x1) / 2, k1.y + 150, (l1.x1 - l1.x0) / 2 + 26, 40, { bas: fr(30.77), sure: 18, a0: -2.6, egim: -0.03 });
    olay(bitis(dl), "tik", 0.5); not("launched daire (kutuda)", dl.bas);
    const a = ok([k1.x + k1.w + 24, k1.y + 100], [k2.x - 24, k2.y + 100], { bas: fr(31.9), sure: 16, w: 7, uzun: 24, bukum: 0.05 });
    not("kutu 1 -> kutu 2 oku", fr(31.9));
    kutu(k2.x, k2.y, k2.w, k2.h, { bas: fr(32.3), sure: 22, w: 4.2, renk: IKI }); olay(fr(32.3), "tik", 0.5);
    not("kutu 2 (Present Perfect)", fr(32.3));
    yazi("Present Perfect", { ...F, boyut: 60, x: k2.x + 40, y: k2.y + 84, bas: fr(32.85), sure: 10, olcek: true, ses: true });
    not("Present Perfect yazısı", fr(32.85));
    // 32,30–32,87 `has doubled` (el yazısı, daire 32,85'te başlar; eski belirme 32,70)
    const l2 = elYazisi("has doubled", { boyut: 52, x: k2.x + 40, y: k2.y + 164, renk: SARI,
      bas: fr(32.30), sure: 17 });
    const d2 = daire((l2.x0 + l2.x1) / 2, k2.y + 150, (l2.x1 - l2.x0) / 2 + 26, 40, { bas: fr(32.85), sure: 18, a0: -2.6, egim: -0.03 });
    olay(bitis(d2), "tik", 0.5); not("has doubled daire (kutuda)", d2.bas);
    parilti(k2.x + k2.w - 50, k2.y + 20, { bas: fr(33.3), r: 22 });
  }
  return S;
}

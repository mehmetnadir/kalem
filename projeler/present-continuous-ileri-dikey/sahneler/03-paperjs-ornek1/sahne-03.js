// Sahne 03 (İLERİ, DİKEY 1080x1920) — Örnek 1 (442 kare, t_bas 15,25; cümle 3). Yerel kare = round((t − 15,25) × 30).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (kalem-paper.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–708) · TR 3 satır (720–912) · sahne 940–1370 (27,9'da 0,42'ye toplanır) · formül kartı (1135–1390).
import { sahneKur, RT } from "/projeler/present-continuous-ileri-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 442, T_BAS = 15.25;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, kutu, yazi, cumle, altCizgi, parilti, olay, not, bitis } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  const GB = 12;
  const f0 = (t) => Math.max(GB, fr(t));

  // --- 15,80: kart çerçevesi (el kutusu, 4 px) — içerik bandı 352–1392'nin üst parçası
  kutu(48, 372, 984, 336, { bas: f0(15.80), sure: 30, w: 4.2, renk: IKI }); not("kart çerçevesi", f0(15.80));

  // --- 16,93–22,05: İngilizce kök (Fredoka 64, 4 satır, sözcük zamanlı); satır başı 5 / 10 / 15
  const sz = S.sozcukler(3).slice(2, 20);                          // Please … phone.
  const satirNo = (i) => (i < 5 ? 0 : i < 10 ? 1 : i < 15 ? 2 : 3);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 88, y: 452, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 78 });
  altCizgi(cz, { tut: 40, w: 8 }); not("cümle başı (Please)", cz[0].bas);

  const cevre = (a, b, bas, egim, ad) => {                         // iki sözcüğü saran sarı daire
    const x0 = cz[a].x0, x1 = cz[b].x1, y = cz[a].y - 24;
    const d = daire((x0 + x1) / 2, y, (x1 - x0) / 2 + 5, 46, { bas, sure: 22, a0: -2.6, egim, w: 10 });
    olay(bitis(d), "tik", 0.5); not(ad, d.bas); return d;
  };
  cevre(5, 6, fr(18.75), -0.03, "is sleeping daire");
  cevre(13, 14, fr(20.40), -0.025, "am talking daire");
  {
    const w = cz[11], k = kutu(w.x0 - 10, w.y - 52, w.w + 6, 74, { bas: fr(20.13), sure: 14, w: 6, renk: SARI });
    not("while kutusu", fr(20.13)); olay(k.bit, "tik", 0.5);
  }

  // --- 16,9–20,0: ORTA sahne (940–1370): tek grupta; duvar, solda uyuyan bebek, sağda telefonda konuşan figür
  const G = S.oge({ topla: { f0: fr(27.9), f1: fr(28.7), ax: 540, ay: 940, olcek: 0.42, dy: 0 } });
  const wall = ciz([[528, 950], [524, 1090], [531, 1230], [526, 1370]], { w: 6, renk: IKI, alfa: 0.9, bas: f0(16.9), sure: 22, uc0: 12, uc1: 30, oge: G });
  not("duvar çizgisi", wall.bas);
  await S.svgCiz("open-peeps/sitting-6.svg", { kutu: [80, 1080, 400, 290], bas: f0(17.3), sure: fr(18.5) - f0(17.3), azami: 60, yuz: 3,
    w: 4.4, oge: G, sesAralik: 5 });
  not("uyuyan figür çizimi başı", f0(17.3));
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [580, 950, 420, 420], bas: f0(17.6), sure: fr(19.2) - f0(17.6), azami: 60, yuz: 3,
    w: 4.4, oge: G, sesAralik: 5 });
  not("konuşan figür çizimi başı", f0(17.6));
  await S.svgCiz("tabler/phone.svg", { kutu: [560, 940, 150, 150], bas: fr(19.3), sure: 14, azami: 6, w: 5, sesAralik: 1, oge: G });
  not("telefon çizimi başı", fr(19.3));
  [[150, 1060, 44], [226, 1000, 54], [316, 936, 64]].forEach(([x, y, b], i) => {   // z z z
    ciz([[x, y + 8], [x + b, y + 8], [x, y + b + 8], [x + b, y + b + 8]], { duz: true, w: 6, renk: IKI, alfa: 0.9, bas: fr(18.7) + i * 7, sure: 9,
      uc0: 4, uc1: 6, amp: 0.5, oge: G });
  });
  not("z z z", fr(18.7));

  // --- 22,30–26,18: Türkçe çeviri (Caveat 64 mürekkep, ≤ 24 karakter/satır) + "iki iş de sürüyor" (sarı, aynı blok)
  const tr = S.sozcukler(3).slice(20, 25);                          // Bebek uyuyor, ben telefonda konuşuyorum.
  const tz = cumle(tr.map((k, i) => ({ s: k.s, f: k.f, satir: i < 2 ? 0 : 1 })), { x: 88, y: 772, boyut: 64, aile: "Caveat", agirlik: 700, aralik: 66, renk: KRE });
  not("Türkçe çeviri", tz[0].bas);
  const it = S.sozcukler(3).slice(25, 31).filter((k) => ["İki", "iş", "de", "sürüyor."].includes(k.s));
  const iz = cumle(it.map((k) => ({ s: k.s, f: k.f, satir: 2 })), { x: 88, y: 772, boyut: 64, aile: "Caveat", agirlik: 700, aralik: 66, renk: SARI });
  not("iki iş de sürüyor", iz[0].bas);

  // --- 27,66: While vurgusu (kutu yerinde kalır, parıltı) ; 27,9–28,7 sahne toplanır
  olay(fr(27.66), "vurus", 0.8);
  parilti(cz[11].x1 + 34, cz[11].y - 70, { bas: fr(27.66), r: 26 }); not("While vurgusu", fr(27.66));
  not("sahne toplanır (0,42)", fr(27.9));

  // --- 28,30–29,58: formül kartı (el kutusu 4 px) + is sleep-ing / am talk-ing (Fredoka 110, -ing sarı)
  kutu(48, 1135, 984, 252, { bas: fr(28.30), sure: 26, w: 4.2, renk: IKI }); not("formül kartı kutusu", fr(28.30));
  const F = { boyut: 110, aile: "Fredoka", agirlik: 700 };
  const s1 = yazi("is sleep", { ...F, x: 100, y: 1244, bas: fr(28.9), sure: 10, olcek: true });
  yazi("-ing", { ...F, x: s1.x1 + 4, y: 1244, bas: fr(28.98), sure: 10, olcek: true, renk: SARI, ses: true }); not("is sleep-ing", fr(28.9));
  const s2 = yazi("am talk", { ...F, x: 100, y: 1362, bas: fr(29.2), sure: 10, olcek: true });
  yazi("-ing", { ...F, x: s2.x1 + 4, y: 1362, bas: fr(29.28), sure: 10, olcek: true, renk: SARI, ses: true }); not("am talk-ing", fr(29.2));
  parilti(960, 1180, { bas: fr(29.3), r: 28 });
  return S;
}

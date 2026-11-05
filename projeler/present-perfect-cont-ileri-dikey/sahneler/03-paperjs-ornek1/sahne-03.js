// Sahne 03 (İLERİ, DİKEY 1080x1920) — Örnek 1 (505 kare, t_bas 17,25; cümle 3). Yerel kare = round((t − 17,25) × 30).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (kalem-paper.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–664, 3 satır) · iki sütun: solda figür 430 px (705–1135), sağda TR 2 satır (760–830) + okul + takvim (880–1130) ·
// formül kartı (1150–1392). Toplanma / küçültme YOK: figür baştan sona 430 px.
import { sahneKur, RT } from "/projeler/present-perfect-cont-ileri-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 505, T_BAS = 17.25;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, kutu, yazi, cumle, altCizgi, parilti, olay, not, bitis, tik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  const GB = 12;
  const f0 = (t) => Math.max(GB, fr(t));

  // --- 17,80: kart çerçevesi (el kutusu, 4 px) + sağ üst köşede daire içinde 1
  kutu(48, 372, 984, 292, { bas: f0(17.80), sure: 30, w: 4.2, renk: IKI }); not("kart çerçevesi", f0(17.80));
  const d1 = daire(985, 412, 30, 28, { bas: f0(18.05), sure: 22, a0: -2.6, w: 8 }); olay(bitis(d1), "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 985, y: 432, hizala: "orta", boyut: 56, aile: "Fredoka", agirlik: 700, bas: f0(18.4), sure: 10, olcek: true });

  // --- 19,09–23,41: İngilizce kök (Fredoka 64, 3 satır 4 / 3 / 3 sözcük, sözcük zamanlı)
  const sz = S.sozcukler(3).slice(2, 12);                          // Since … complaining.
  const satirNo = (i) => (i < 4 ? 0 : i < 7 ? 1 : 2);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 88, y: 462, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 84 });
  altCizgi(cz, { tut: 40, w: 8 }); not("cümle başı (Since)", cz[0].bas);

  const cevre = (a, b, bas, egim, ad, pay = 8, ry = 48) => {       // sözcük(ler)i saran sarı daire
    const x0 = cz[a].x0, x1 = cz[b].x1, y = cz[a].y - 24;
    const d = daire((x0 + x1) / 2, y, (x1 - x0) / 2 + pay, ry, { bas, sure: 22, a0: -2.6, egim, w: 10 });
    olay(bitis(d), "tik", 0.5); not(ad, d.bas); return d;
  };
  {   // Since … changed (19,89–20,21): sarı köşeli ayraç
    const x0 = cz[0].x0 - 6, x1 = cz[3].x1 + 6, y = cz[0].y + 22;
    const a = ciz([[x0, y - 10], [x0, y + 4], [x1, y + 4], [x1, y - 10]],
      { duz: true, w: 9, renk: SARI, alfa: 0.85, bas: fr(19.89), sure: 14, uc0: 12, uc1: 24 });
    not("Since … changed ayraç", a.bas); olay(bitis(a), "tik", 0.5);
  }
  cevre(7, 9, fr(21.81), -0.02, "have been complaining daire", 14, 50);

  // --- 19,09–23,41: sol sütun öğrenci (sitting-6, 430 px); sağ sütun altı okul (440) + takvim
  await S.svgCiz("coco/school.svg", { kutu: [430, 880, 440, 260], bas: f0(19.09), sure: fr(20.2) - f0(19.09), azami: 25, yuz: 1,
    w: 4.4, sesAralik: 3 });
  not("okul çizimi başı", f0(19.09));
  await S.svgCiz("open-peeps/sitting-6.svg", { kutu: [48, 705, 330, 430], bas: f0(19.7), sure: fr(21.5) - f0(19.7), azami: 60, yuz: 3,
    w: 4.4, sesAralik: 5 });
  not("öğrenci figürü çizimi başı", f0(19.7));
  await S.svgCiz("tabler/calendar.svg", { kutu: [890, 905, 140, 140], bas: fr(20.4), sure: 14, azami: 25, w: 4.6, sesAralik: 2 });
  not("takvim (timetable) çizimi başı", fr(20.4));

  // --- 23,66–26,86: Türkçe çeviri (Caveat 64 mürekkep, ≤ 24 karakter/satır, 2 satır, sağ sütun x 430)
  const tr = S.sozcukler(3).slice(12, 17);                          // Program değişeli beri öğrenciler yakınıyor.
  const tz = cumle(tr.map((k, i) => ({ s: k.s, f: k.f, satir: i < 3 ? 0 : 1 })), { x: 430, y: 770, boyut: 64, aile: "Caveat",
    agirlik: 700, aralik: 70, renk: KRE });
  not("Türkçe çeviri", tz[0].bas);

  // --- 27,11–29,11 formül kartı (el kutusu 4 px): since + past simple ; since sözcüğü kökte yeniden daire
  kutu(48, 1150, 984, 242, { bas: fr(27.0), sure: 26, w: 4.2, renk: IKI }); not("formül kartı kutusu", fr(27.0));
  const F = { boyut: 80, aile: "Fredoka", agirlik: 700 };
  const a1 = yazi("since", { ...F, x: 100, y: 1240, bas: fr(27.11), sure: 10, olcek: true, renk: SARI, ses: true });
  const a2 = yazi("+", { ...F, x: a1.x1 + 24, y: 1240, bas: fr(28.07), sure: 8, olcek: true, renk: IKI });
  yazi("past simple", { ...F, x: a2.x1 + 24, y: 1240, bas: fr(28.47), sure: 10, olcek: true, ses: true });
  not("since + past simple", fr(27.11));
  cevre(0, 0, fr(27.2), -0.03, "Since ikinci daire", 12, 50);

  // --- 30,32–33,68: → have been + V-ing (Fredoka 80, -ing sarı) ; kökte have been yeniden vurgulanır
  const b1 = yazi("→", { ...F, x: 100, y: 1348, bas: fr(30.32), sure: 8, olcek: true, renk: IKI });
  const b2 = yazi("have been", { ...F, x: b1.x1 + 26, y: 1348, bas: fr(31.36), sure: 10, olcek: true, ses: true });
  const b3 = yazi("+ V", { ...F, x: b2.x1 + 24, y: 1348, bas: fr(32.1), sure: 8, olcek: true });
  const b4 = yazi("-ing", { ...F, x: b3.x1 + 4, y: 1348, bas: fr(32.56), sure: 10, olcek: true, renk: SARI, ses: true });
  not("have been + V-ing", fr(31.36));
  cevre(7, 8, fr(31.36), 0.02, "have been ikinci daire", 12, 50);
  tik(b4.x1 + 70, 1296, { bas: fr(33.12) });
  parilti(960, 1190, { bas: fr(33.2), r: 28 });
  return S;
}

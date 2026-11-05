// Sahne 02 SIMPLE PAST İLERİ — Kanca + kural (326 kare, t_bas 3,00; cümle 2 = 3,71–12,92). Yerel kare = round((t − 3,00) × 30).
// Cümle 1 yazısı 0. karede yerinde (sahne 01 ile aynı yer, x 140 y 300); içerik 12,9 sn'de (kare 297) biter.
import { sahneKur, RT } from "/projeler/simple-past-ileri/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 326, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, ciz, daire, yazi, cumle, tik, parilti, olay, not, bitis, kutu, svgCiz } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;

  // --- cümle 1: "Ago varsa Perfect yok." (Caveat 64, x 140, y 300); 0. karede hazır, Perfect kırmızı çizili
  const c1 = cumle(["Ago", "varsa", "Perfect", "yok."].map((s) => ({ s, f: -10 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 yerinde", 0);
  {
    const g = c1[2];
    ciz([[g.x0 - 6, g.y - 6], [(g.x0 + g.x1) / 2, g.y - 20], [g.x1 + 8, g.y - 32]],
      { w: 8, renk: KIR, alfa: 0.9, bas: -30, sure: 10, uc0: 8, uc1: 12, amp: 0.7, ses: false });
    not("Perfect kırmızı çizili", 0);
  }
  // --- sağda eskiz: takvim (260 px) 0,2 sn'den; saat 4,03'te + 6 min
  await svgCiz("tabler/calendar.svg", { kutu: [1340, 190, 260, 260], bas: 6, sure: 30, azami: 25, w: 4, sesAralik: 1 });
  not("takvim eskizi", 6);
  await svgCiz("tabler/clock.svg", { kutu: [1650, 210, 200, 200], bas: fr(4.03), sure: 24, azami: 25, w: 4, sesAralik: 1 });
  yazi("6 min", { x: 1670, y: 480, boyut: 64, renk: SARI, bas: fr(4.03) + 20, sure: 12, ses: true });
  not("saat + 6 min", fr(4.03));

  // --- 3,71–9,07: el çizimi kutu, 3 madde tik (rule 5,55 · time words 6,99 · traps 8,51)
  kutu(140, 400, 860, 270, { bas: fr(3.71), sure: 34, w: 4 }); not("madde kutusu", fr(3.71));
  [["rule", 5.55, 480], ["time words", 6.99, 565], ["traps", 8.51, 650]].forEach(([s, t, y]) => {
    yazi(s, { x: 220, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8, olcek: true, ses: true });
    tik(185, y - 22, { bas: fr(t) + 6 }); not("madde " + s, fr(t));
  });

  // --- 9,72–12,76: tanım Fredoka 56, iki satır (y 800 / 872), sözcük zamanlı
  {
    const kel = [["A", 9.72, 0], ["finished", 9.88, 0], ["action", 10.36, 0], ["at", 10.84, 0], ["a", 11.00, 0],
      ["definite", 11.24, 0], ["time", 11.80, 0], ["in", 12.00, 1], ["the", 12.12, 1], ["past.", 12.44, 1]];
    const e = cumle(kel.map(([s, t, satir]) => ({ s, f: fr(t), satir })),
      { x: 140, y: 800, boyut: 56, aile: "Fredoka", agirlik: 700, aralik: 72 });
    not("tanım başı (A)", e[0].bas);
    const f = e[1], d = daire((f.x0 + f.x1) / 2, f.y - 18, f.w / 2 + 14, 38, { bas: fr(9.88) + 6, sure: 20, w: 8 });
    olay(bitis(d), "tik", 0.5); not("finished daire", d.bas);
    const a = e[5], b = e[6];
    const u = ciz([[a.x0 - 4, a.y + 12], [(a.x0 + b.x1) / 2, a.y + 9], [b.x1 + 6, a.y + 13]],
      { w: 9, renk: RT.vurguDolgu, alfa: 0.85, bas: fr(11.24) + 4, sure: fr(12.12) - fr(11.24) - 4, uc0: 8, uc1: 14, amp: 1.0 });
    not("definite time altı", u.bas);
  }

  // --- 11,5–12,9: zaman çizgisi (y 960): kapalı kutu sarı + now noktası
  {
    ciz([[140, 960], [700, 958], [1300, 962], [1700, 960]], { w: 4, renk: IKI, alfa: 0.85, bas: fr(11.5), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", fr(11.5));
    kutu(300, 925, 520, 70, { bas: fr(12.0), sure: 18, w: 8, renk: SARI }); not("kapalı kutu", fr(12.0));
    const dn = daire(1300, 960, 14, 14, { bas: fr(12.45), sure: 10, w: 8, tur: 1.1 });
    yazi("now", { x: 1300, y: 1010, boyut: 64, hizala: "orta", renk: KRE, bas: bitis(dn), sure: 8, ses: true });
    not("now noktası", dn.bas);
    parilti(830, 925, { bas: fr(12.7), r: 24, periyot: 0, adet: 1 });
  }
  return S;
}

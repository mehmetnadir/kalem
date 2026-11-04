// Sahne 02 İLERİ — Kanca + formül (380 kare, t_bas 3,00; cümle 2). Yerel kare = round((t − 3,00) × 30).
// Cümle 1 yazısı 0. karede yerinde (sahne 01 ile aynı yer, x 140 y 300); içerik 15,25 sn'de biter.
import { sahneKur, RT } from "/projeler/present-continuous-ileri/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 380, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, daire, yazi, cumle, tik, parilti, olay, not, bitis, kutu, svgCiz } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;

  // --- cümle 1: "YDT'nin -ing tuzağına düşme." (Caveat 64, x 140, y 300); 0. karede hazır
  const c1 = cumle(["YDT'nin", "-ing", "tuzağına", "düşme."].map((s) => ({ s, f: -10 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 yerinde", 0);
  {   // -ing sarı daire titrer (3,00–3,71)
    const g = c1[1], tit = S.oge({ tit: { f0: 0, f1: fr(3.71), g: 2.4 } });
    daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 12, 38, { bas: -30, sure: 20, ses: false, oge: tit });
    not("-ing daire titrer", 0);
  }

  // --- 3,71–5,07: FORMÜL etiketi + el kutusu (x 140–1280, y 420–660)
  yazi("FORMÜL", { x: 140, y: 408, boyut: 48, renk: IKI, bas: fr(3.71), sure: 10, ses: true }); not("FORMÜL etiketi", fr(3.71));
  kutu(140, 420, 1140, 240, { bas: fr(4.0), sure: 32, w: 4 }); not("formül kutusu", fr(4.0));

  // --- 5,32–10,68: formül tek satır (Fredoka 84, taban y 545), sözcük zamanlı
  {
    const F = "700 84px Fredoka", gap = 18, Y = 545; let x = 160;
    const koy = (s, t, o = {}) => { const y = yazi(s, { x, y: Y, boyut: 84, aile: "Fredoka", agirlik: 700, renk: o.renk || KRE,
      bas: fr(t), sure: 8, olcek: true, ses: o.ses !== false }); x = y.x1 + gap; return y; };
    const ayrac = (t) => { const y = yazi("/", { x: x - 6, y: Y, boyut: 84, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(t), sure: 6 });
      x = y.x1 + gap - 10; };
    const sub = koy("Subject", 5.32);
    yazi("özne", { x: sub.x0 + 40, y: 630, boyut: 64, renk: SARI, bas: fr(5.6), sure: 10, ses: true }); not("Subject + özne", fr(5.32));
    koy("+", 6.4, { renk: IKI, ses: false });
    koy("am", 6.84); ayrac(7.6); koy("is", 7.68); ayrac(8.24); koy("are", 8.32); not("am / is / are", fr(6.84));
    koy("+", 9.0, { renk: IKI, ses: false });
    const v = koy("V-ing", 9.40); not("V-ing", fr(9.40));
    const d = daire((v.x0 + v.x1) / 2, Y - 30, v.w / 2 + 10, 52, { bas: fr(9.7), sure: 22 });
    olay(bitis(d), "tik", 0.5); not("V-ing daire", d.bas);
  }

  // --- 10,93–12,57: altı dakika: saat + 6 min
  await svgCiz("tabler/clock.svg", { kutu: [1450, 300, 260, 260], bas: fr(10.93), sure: 26, azami: 25, w: 4, sesAralik: 2 });
  yazi("6 min", { x: 1480, y: 625, boyut: 64, renk: SARI, bas: fr(11.5), sure: 12, ses: true }); not("saat + 6 min", fr(10.93));
  parilti(1700, 310, { bas: fr(12.2), r: 26, periyot: 0, adet: 1 });

  // --- 12,57–14,05: üç sınav kökü: 3 el kutusu, rakam + tik
  [[1, 140, 12.57], [2, 440, 13.09], [3, 740, 13.65]].forEach(([n, x, t]) => {
    kutu(x, 730, 260, 220, { bas: fr(t), sure: 16, w: 4 });
    yazi(String(n), { x: x + 130, y: 880, boyut: 130, aile: "Fredoka", agirlik: 700, hizala: "orta", renk: KRE, bas: fr(t) + 8, sure: 8, olcek: true });
    tik(x + 215, 775, { bas: fr(t) + 16 }); not("kutu " + n, fr(t));
  });

  // --- 14,05–15,25: bir tuzak: dördüncü kutu, kırmızı ünlem + "1 tuzak" (kırmızı yalnız burada)
  kutu(1040, 730, 380, 220, { bas: fr(14.05), sure: 16, w: 4, renk: KIR }); not("tuzak kutusu", fr(14.05));
  yazi("!", { x: 1100, y: 890, boyut: 170, aile: "Fredoka", agirlik: 700, renk: KIR, bas: fr(14.3), sure: 8, olcek: true, ses: "vurus" });
  yazi("1 tuzak", { x: 1170, y: 870, boyut: 64, renk: KIR, bas: fr(14.6), sure: 10, ses: true }); not("1 tuzak", fr(14.6));
  return S;
}

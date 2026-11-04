// Sahne 02 İLERİ DİKEY — Kanca + formül (380 kare, t_bas 3,00; cümle 2), 1080x1920.
// Bantlar: içerik 352–1392 (dolu), altyazı 1400–1536 (kalem-paper.js çizer), platform 1536–1920 boş.
import { sahneKur, RT } from "/projeler/present-continuous-ileri-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 380, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, daire, yazi, cumle, tik, parilti, olay, not, bitis, kutu, svgCiz } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;

  // --- cümle 1: iki satır Caveat 80 (x 64, taban 450 / 540); 0. karede hazır (sahne 01 ile aynı yer)
  const c1 = cumle([["YDT'nin", 0], ["-ing", 0], ["tuzağına", 1], ["düşme.", 1]].map(([s, satir]) => ({ s, f: -10, satir })),
    { x: 64, y: 450, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 90 });
  not("cümle 1 yerinde", 0);
  {   // -ing sarı daire titrer (3,00–3,71)
    const g = c1[1], tit = S.oge({ tit: { f0: 0, f1: fr(3.71), g: 3 } });
    daire((g.x0 + g.x1) / 2, g.y - 28, g.w / 2 + 16, 46, { bas: -30, sure: 20, ses: false, oge: tit, w: 10 });
    not("-ing daire titrer", 0);
  }

  // --- 3,71–5,07: formül kartı (tam genişlik, y 600–940) el kutusu; FORMÜL etiketi kartın sağ üstünde
  kutu(48, 596, 984, 366, { bas: fr(3.71), sure: 36, w: 4.4 }); not("formül kartı", fr(3.71));

  // --- 5,32–10,68: formül üç satır alt alta (Fredoka 96, taban 700 / 805 / 910), sözcük zamanlı
  {
    const Y1 = 700, Y2 = 818, Y3 = 936;
    const koy = (s, x, y, t, o = {}) => yazi(s, { x, y, boyut: o.boyut || 96, aile: "Fredoka", agirlik: 700,
      renk: o.renk || KRE, bas: fr(t), sure: 8, olcek: true, ses: o.ses !== false });
    const sub = koy("Subject", 110, Y1, 5.32); not("Subject", fr(5.32));
    yazi("özne", { x: 520, y: Y1, boyut: 72, renk: SARI, bas: fr(5.62), sure: 10, ses: true });
    koy("+", 80, Y2, 6.4, { renk: IKI, ses: false });
    let x = 170;
    const a = koy("am", x, Y2, 6.84); x = a.x1 + 14;
    const s1 = yazi("/", { x, y: Y2, boyut: 96, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(7.55), sure: 6 }); x = s1.x1 + 14;
    const i = koy("is", x, Y2, 7.68); x = i.x1 + 14;
    const s2 = yazi("/", { x, y: Y2, boyut: 96, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(8.2), sure: 6 }); x = s2.x1 + 14;
    koy("are", x, Y2, 8.32); not("am / is / are", fr(6.84));
    koy("+", 80, Y3, 9.0, { renk: IKI, ses: false });
    const v = koy("V-ing", 170, Y3, 9.40); not("V-ing", fr(9.40));
    const d = daire((v.x0 + v.x1) / 2, Y3 - 34, v.w / 2 + 18, 52, { bas: fr(9.7), sure: 22, w: 10 });
    olay(bitis(d), "tik", 0.5); not("V-ing daire", d.bas);
    void sub;
  }

  // --- 10,93–12,57: saat (210 px) + 6 min (Caveat 80)
  await svgCiz("tabler/clock.svg", { kutu: [64, 992, 196, 196], bas: fr(10.93), sure: 26, azami: 25, w: 4.2, sesAralik: 2 });
  yazi("6 min", { x: 320, y: 1112, boyut: 96, renk: SARI, bas: fr(11.5), sure: 12, ses: true }); not("saat + 6 min", fr(10.93));
  parilti(290, 1005, { bas: fr(12.2), r: 28, periyot: 0, adet: 1 });

  // --- 12,57–14,05: üç sınav kökü: 3 el kutusu (y 1215–1385), rakam + tik
  [[1, 48, 12.57], [2, 262, 13.09], [3, 476, 13.65]].forEach(([n, x, t]) => {
    kutu(x, 1215, 190, 170, { bas: fr(t), sure: 16, w: 4.2 });
    yazi(String(n), { x: x + 95, y: 1335, boyut: 120, aile: "Fredoka", agirlik: 700, hizala: "orta", renk: KRE, bas: fr(t) + 8, sure: 8, olcek: true });
    tik(x + 160, 1255, { bas: fr(t) + 16 }); not("kutu " + n, fr(t));
  });

  // --- 14,05–15,25: bir tuzak: dördüncü kutu, kırmızı ünlem + "1 tuzak" (kırmızı yalnız burada)
  kutu(690, 1215, 342, 170, { bas: fr(14.05), sure: 16, w: 4.2, renk: KIR }); not("tuzak kutusu", fr(14.05));
  yazi("!", { x: 715, y: 1340, boyut: 130, aile: "Fredoka", agirlik: 700, renk: KIR, bas: fr(14.3), sure: 8, olcek: true, ses: "vurus" });
  yazi("1 tuzak", { x: 775, y: 1320, boyut: 72, renk: KIR, bas: fr(14.6), sure: 10, ses: true }); not("1 tuzak", fr(14.6));
  return S;
}

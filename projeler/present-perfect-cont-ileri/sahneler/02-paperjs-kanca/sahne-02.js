// Sahne 02 İLERİ — Kural + kanca: Paper.js, 1920x1080, 440 kare, t_bas 3,00; cümle 2 (3,39–17,25).
// Yerel kare = round((t − 3,00) × 30). Cümle 1 0. karede yerinde (sahne 01 ile aynı yer, x 140 y 300).
import { sahneKur, RT } from "/projeler/present-perfect-cont-ileri/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 440, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, daire, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu, svgCiz } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep;
  const CS = S.sozcukler(2);                                    // cümle 2 sözcükleri (f / f1 kare)
  const pen = (ilk, adet) => { const i = CS.findIndex((w) => w.s === ilk);
    return CS.slice(i, i + adet).map((w) => ({ f0: w.f, f1: w.f1 })); };

  // --- cümle 1: "Süreç mi, sonuç mu?" (Caveat 64, x 140, y 300); 0. karede hazır
  const c1 = cumle(["Süreç", "mi,", "sonuç", "mu?"].map((s) => ({ s, f: -10 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 yerinde", 0);
  {   // "sonuç" üstündeki sarı daire titrer (3,00–3,71)
    const g = c1[2], tit = S.oge({ tit: { f0: 0, f1: fr(3.71), g: 2.4 } });
    daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 12, 38, { bas: -30, sure: 20, ses: false, oge: tit });
    not("sonuç daire titrer", 0);
  }

  // --- 3,39–5,79: "sınav bunu sorar" (Caveat, sağda), kural kartı el kutusu
  // el yazısı, sözcük penceresi: sınav 3,39–3,79 · bunu 3,83 (4,03 → 4,07'ye uzatıldı) ·
  // sorar. 4,07–4,71
  elYazisi("sınav", { x: 700, y: 300, boyut: 64, renk: SARI, sozcukler: pen("Sınav", 1) });
  elYazisi("bunu", { x: 860, y: 300, boyut: 64, renk: SARI,
    sozcukler: [{ f0: pen("bunu", 1)[0].f0, f1: pen("sorar.", 1)[0].f0 }] });
  elYazisi("sorar.", { x: 990, y: 300, boyut: 64, renk: SARI, sozcukler: pen("sorar.", 1) });
  not("sınav bunu sorar", fr(3.39));
  kutu(140, 430, 1640, 320, { bas: fr(4.2), sure: 36, w: 4 }); not("kural kartı", fr(4.2));
  // 5,27–5,79 «kural.» penceresi
  elYazisi("KURAL", { x: 180, y: 478, boyut: 48, renk: SARI, sozcukler: pen("kural.", 1) });
  not("KURAL etiketi", fr(5.27));

  // --- 6,04–10,76: formül tek satır (Fredoka 112, taban y 620), sözcük zamanlı, üç parça üç daire
  {
    const Y = 620, B = 112, gap = 24; let x = 200;
    const koy = (s, t, o = {}) => { const z = yazi(s, { x, y: Y, boyut: B, aile: "Fredoka", agirlik: 700,
      renk: o.renk || KRE, bas: fr(t), sure: 8, olcek: true, ses: o.ses !== false }); x = z.x1 + gap; return z; };
    const have = koy("have", 6.04);
    const s1 = yazi("/", { x: x - 8, y: Y, boyut: B, aile: "Fredoka", agirlik: 700, renk: SARI, bas: fr(6.52), sure: 6 });
    x = s1.x1 + gap - 12;
    const has = koy("has", 6.76); not("have / has", fr(6.04));
    const d1 = daire((have.x0 + has.x1) / 2, Y - 36, (has.x1 - have.x0) / 2 + 22, 66, { bas: fr(7.1), sure: 22, w: 7 });
    olay(bitis(d1), "tik", 0.5); not("have / has daire", d1.bas);
    koy("+", 7.56, { renk: SARI, ses: false });
    const been = koy("been", 7.88); not("been", fr(7.88));
    const d2 = daire((been.x0 + been.x1) / 2, Y - 36, been.w / 2 + 20, 66, { bas: fr(8.4), sure: 22, a0: -2.2, w: 7 });
    olay(bitis(d2), "tik", 0.5); not("been daire", d2.bas);
    koy("+", 8.64, { renk: SARI, ses: false });
    const ing = koy("-ing", 9.08); not("-ing", fr(9.08));
    const d3 = daire((ing.x0 + ing.x1) / 2, Y - 36, ing.w / 2 + 20, 66, { bas: fr(9.6), sure: 22, a0: -1.9, w: 7 });
    olay(bitis(d3), "tik", 0.5); not("-ing daire", d3.bas);
    // üç parçanın altında kısa TR not (Caveat 56, vurgu): anlatımsız etiketler, sure 0,67–0,73 sn
    // (7,50–8,17 · 8,90–9,63 · 10,00–10,67; cümle sonu 10,76)
    elYazisi("yardımcı fiil", { x: have.x0, y: 722, boyut: 56, renk: SARI, bas: fr(7.5),
      sure: 20 });
    elYazisi("be'nin 3. formu", { x: been.x0 - 30, y: 722, boyut: 56, renk: SARI, bas: fr(8.9),
      sure: 22 });
    elYazisi("fiil + -ing", { x: ing.x0 - 30, y: 722, boyut: 56, renk: SARI, bas: fr(10.0),
      sure: 20 });
    not("üç not", fr(7.5));
  }

  // --- 11,01–: altı dakika: saat + 6 min (sol alt), 3 madde kutusu (sağ alt)
  await svgCiz("tabler/clock.svg", { kutu: [140, 790, 200, 200], bas: fr(11.01), sure: 26, azami: 25, w: 4, sesAralik: 2 });
  // 11,33–11,90 «dakikada» penceresi (iki sözcüklü metin: tek pencere yetmez → sure 17 kare)
  elYazisi("6 min", { x: 400, y: 900, boyut: 80, renk: SARI, bas: fr(11.33), sure: 17 });
  not("saat + 6 min", fr(11.01));
  parilti(380, 810, { bas: fr(12.3), r: 26, periyot: 0, adet: 1 });
  kutu(900, 790, 880, 205, { bas: fr(12.05), sure: 28, w: 4 }); not("madde kutusu", fr(12.05));
  [["form", 13.57, 850], ["time clues", 14.77, 910], ["2 traps", 16.05, 970]].forEach(([s, t, y]) => {
    yazi(s, { x: 990, y, boyut: 56, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8, olcek: true });
    tik(945, y - 18, { bas: fr(t) + 6 }); not("madde " + s, fr(t));
  });
  return S;
}

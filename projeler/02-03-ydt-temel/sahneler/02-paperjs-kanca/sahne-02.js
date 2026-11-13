// Sahne 02 — Kanca (Paper.js, 381 kare, t_bas 3,00; cümle 1'in kalanı + cümle 2). 02-03 YDT temel.
// Yerel kare = round((t − 3,00) × 30). Sözcük zamanları ortak/anlatim/sozcukler.json'dan okunur.
// Sahne 01 künyeye uçup kartları söndürerek biter; bu sahne kartları kalemle yeniden çizer (ilk 12 kare durgun).
import { sahneKur,
  RT } from "/projeler/02-03-ydt-temel/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 381, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, daire, ok, kutu, yazi, elYazisi, ciz, parilti, olay, not, bitis, svgCiz } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu;
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);   // cümle 1: 7 sözcük · cümle 2: 20 sözcük
  const f0 = (t) => Math.max(12, fr(t));            // ilk 12 kare durgun

  // --- 3,40–3,98: iki kart sağda (01 ile aynı yer): goes üstte, is going altta; kalemle yeniden çizilir
  const CX = 1160, CW = 620, CH = 200, CY = [310, 570], YAZI = 100;
  [["goes", 12], ["is going", 18]].forEach(([m, b], k) => {
    kutu(CX, CY[k], CW, CH, { bas: b, sure: 16, w: 4 });
    yazi(m, { x: CX + CW / 2, y: CY[k] + CH / 2 + YAZI * 0.36, hizala: "orta", boyut: YAZI,
      aile: "Fredoka", agirlik: 700, bas: b + 14, sure: 8, olcek: true, ses: true });
  });
  not("kartlar (goes, is going)", 12);

  // --- 3,72 sinyal · 4,16 sözcüğünde: SIGNAL WORD, sarı belirteç yazının altında
  {
    const F = 96, XS = 140, Y = 420, wTum = 635, wSig = 354;      // Fredoka 700 96: ölçülü genişlikler
    ciz([[XS - 14, Y - 30], [XS + wTum + 16, Y - 34]], { duz: true, w: 58, renk: DOLGU, alfa: 0.7,
      bas: fr(s1[5].t) - 5, sure: fr(4.72) - fr(s1[5].t) + 5, uc0: 6, uc1: 14, amp: 1.2, tur: "isaret",
      ad: "SIGNAL WORD belirteç" });
    not("SIGNAL WORD belirteç (sinyal)", fr(s1[5].t));
    yazi("SIGNAL", { x: XS, y: Y, boyut: F, aile: "Fredoka", agirlik: 700, bas: fr(s1[5].t), sure: 8,
      olcek: true, ses: true });
    yazi("WORD", { x: XS + wSig, y: Y, boyut: F, aile: "Fredoka", agirlik: 700, bas: fr(s1[6].t),
      sure: 8, olcek: true, ses: true });
    not("WORD (sözcüğünde)", fr(s1[6].t));
  }

  // --- çipler: sol 6,83 şimdiki (PRESENT CONTINUOUS), sağ 8,11 geniş (SIMPLE PRESENT)
  const CIP_Y = 560, CIP_H = 90, CIP_F = 40;
  const cip = (m, x, w, t) => {
    kutu(x, CIP_Y, w, CIP_H, { bas: f0(t), sure: 16, w: 4 });
    yazi(m, { x: x + w / 2, y: CIP_Y + CIP_H / 2 + CIP_F * 0.35, hizala: "orta", boyut: CIP_F,
      aile: "Fredoka", agirlik: 700, bas: f0(t) + 4, sure: 8, olcek: true, ses: true });
  };
  cip("PRESENT CONTINUOUS", 140, 476, s2[2].t);
  not("sol çip (şimdiki)", fr(s2[2].t));
  // sarı daire: sol çip 7,31 zamanı · sağ çip 8,43 zamanı (ses sırasıyla)
  const dL = daire(378, CIP_Y + CIP_H / 2, 260, 70, { bas: fr(s2[3].t), sure: 22, a0: -2.4 });
  olay(bitis(dL), "tik", 0.5); not("sol çip daire (zamanı)", dL.bas);
  cip("SIMPLE PRESENT", 736, 364, s2[5].t);
  not("sağ çip (geniş)", fr(s2[5].t));
  const dR = daire(918, CIP_Y + CIP_H / 2, 204, 70, { bas: fr(s2[6].t), sure: 22, a0: -2.4,
    egim: -0.05 });
  olay(bitis(dR), "tik", 0.5); not("sağ çip daire (zamanı)", dR.bas);

  // --- 11,15 ikisini: iki çipin altında sarı köşeli ayraç
  {
    const b = ciz([[140, 712], [140, 728], [1100, 728], [1100, 712]], { duz: true, w: 7, renk: SARI,
      alfa: 0.85, bas: fr(s2[12].t), sure: 18, uc0: 8, uc1: 14, amp: 0.5, tur: "isaret",
      ad: "ikisini ayraç" });
    not("ayraç (ikisini)", b.bas);
  }
  // --- 11,67 yan yana: aralarına `vs` kalemle yazılır (çipler arası x 616–736, orta 676)
  const vs = elYazisi("vs", { x: 676 - 30, y: 612, boyut: 88, renk: SARI,
    sozcukler: [{ f0: fr(s2[13].t), f1: fr(s2[14].t) + 4 }] });
  not("vs (yan yana)", vs.bas);

  // --- 12,99 Alıştırma: kalem simgesi · 14,19 farkı: iki uçlu sarı ok · 14,51 yakalıyoruz: parıltı
  await svgCiz("tabler/pencil.svg", { kutu: [140, 790, 150, 150], bas: fr(s2[16].t), sure: 28,
    azami: 8, w: 4, sesAralik: 2 });
  not("kalem simgesi (Alıştırma)", fr(s2[16].t));
  const fa = ok([1845, 430], [1845, 650], { bas: fr(s2[18].t), sure: 18, w: 7, cift: true,
    uzun: 24, bukum: 0.04 });
  not("fark oku (farkı)", fa.bas);
  parilti(1845, 540, { bas: fr(s2[19].t), r: 26 });
  not("parıltı (yakalıyoruz)", fr(s2[19].t));
  return S;
}

// Sahne 03 (DİKEY) — Örnek 1: Paper.js, 1080x1920, 379 kare, t_bas 15,45; cümle 3 = 16,00–27,69.
// Yerel kare = round((t − 15,45) × 30). Yerleşim dikey için sıfırdan: kart → TR çeviri → ORTA güneş + ok → alt formül.
import { sahneKur, RT } from "/projeler/simple-present-temel-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 379, T_BAS = 15.45;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1 });
  const { fr, ciz, daire, yazi, cumle, altCizgi, parilti, olay, not, bitis, genislik, kutu } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;

  // --- kart: tam genişlik (984), Fredoka 72, sözcük zamanlı; satır kırılımı ölçülür
  const sz = S.sozcukler(3).slice(2, 8);                           // The sun rises in the east.
  const FK = "700 72px Fredoka";
  const satirlar = [sz.slice(0, 3), sz.slice(3)];                 // 2 satır: The sun rises / in the east.
  const SH = 88, B1 = 372 + 40 + 58;                               // kart üstü 372, iç boşluk 40, ilk taban
  const sonTaban = B1 + (satirlar.length - 1) * SH, kartAlt = sonTaban + 24 + 36;
  kutu(48, 372, 984, kartAlt - 372, { bas: fr(16.2), sure: 30, w: 4, renk: IKI });
  not("kart kutusu çizimi", fr(16.2));
  const kel = satirlar.flatMap((a, si) => a.map((k) => ({ s: k.s, f: k.f, satir: si })));
  const cz = cumle(kel, { x: 88, y: B1, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: SH });
  altCizgi(cz, { tut: 40, w: 9 }); not("cümle başı (The)", cz[0].bas); not("east.", cz[5].bas);

  // --- 19,86 TR çeviri (Caveat 64, mürekkep) + 21,70 doğa kanunu etiketi (el kutusu, sağda)
  const yTR = kartAlt + 86;
  yazi("Güneş doğudan doğar.", { x: 64, y: yTR, boyut: 64, aile: "Caveat", agirlik: 700, renk: RT.murekkep,
    bas: fr(19.86), sure: 18 });
  not("Türkçe çeviri", fr(19.86));
  {
    const kb = fr(21.7), k = kutu(610, yTR - 54, 420, 92, { bas: kb, sure: 22 });
    not("doğa kanunu kutusu", kb);
    yazi("doğa kanunu", { x: 820, y: yTR + 4, hizala: "orta", boyut: 64, aile: "Caveat", agirlik: 700, renk: SARI,
      bas: k.bit - 6, sure: 14, ses: true });
    not("doğa kanunu", k.bit - 6);
  }

  // --- ORTA: güneş (430 px) + ufuk çizgisi + ok east (17,21–19,45)
  const yUfuk = 1196;
  const uf = ciz([[56, yUfuk + 2], [330, yUfuk - 2], [700, yUfuk + 1], [1024, yUfuk - 1]],
    { w: 4.4, renk: IKI, alfa: 0.9, bas: fr(17.21), sure: 24, uc0: 10, uc1: 30 });
  not("ufuk çizgisi", uf.bas);
  const gunOge = S.oge({ nefes: { bas: fr(19.5), cx: 285, cy: yUfuk } });
  await S.svgCiz("coco/sun.svg", { kutu: [70, 760, 430, 430], bas: fr(17.4), sure: fr(19.2) - fr(17.4), azami: 30,
    w: 4.2, oge: gunOge, sesAralik: 3 });
  not("güneş çizimi başı", fr(17.4));
  parilti(520, 790, { bas: fr(19.3), r: 30, periyot: 150, adet: 2 });
  {
    const o = S.ok([590, 1010], [1000, 1010], { bas: fr(18.65), sure: 24, w: 8, bukum: 0.03, uzun: 28 });
    not("ok east", o.bas);
    yazi("east", { x: 795, y: 960, hizala: "orta", boyut: 96, aile: "Caveat", agirlik: 700, renk: SARI,
      bas: bitis(o) - 4, sure: 12, olcek: true, ses: true });
    not("east etiketi", bitis(o) - 4);
  }

  // --- 24,93 rises sarı daire (kartta); 26,65 sonundaki s ayrı sarı daire
  {
    const g = cz[2];
    const da = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 8, 42, { bas: fr(24.93), sure: 18, a0: -2.2 });
    olay(bitis(da), "tik", 0.5); not("rises daire", da.bas);
    const ws = genislik("s", FK), sx = g.x1 - ws / 2;
    const ds = daire(sx, g.y - 26, ws / 2 + 14, 44, { bas: fr(26.65), sure: 14, a0: -1.2 });
    olay(bitis(ds), "tik", 0.5); not("s daire", ds.bas);
  }

  // --- alt formül (Fredoka 100): satır A `it + rise-s` (26,80), satır B `V + s` (27,01); kare 366'dan sonra durgun
  {
    const boy = 96, yA = 1294, yB = 1390, F = `700 ${boy}px Fredoka`;
    const topla = (p, G) => p.reduce((t, m) => t + genislik(m, F), 0) + G.reduce((a, b) => a + b, 0);
    const sat = (p, y, t, renkler, G) => {
      let x = 600 - topla(p, G) / 2; const out = [];
      p.forEach((m, i) => {
        const o = yazi(m, { x, y, boyut: boy, aile: "Fredoka", agirlik: 700, renk: renkler[i], bas: t[i], sure: 5,
          olcek: true, ses: i === 0 }); out.push(o); x = o.x1 + (G[i] == null ? 0 : G[i]); });
      return out;
    };
    const kA = fr(26.8), kB = fr(27.01);
    sat(["it", "+", "rise", "-s"], yA, [kA, kA + 3, kA + 5, kA + 8], [RT.murekkep, IKI, RT.murekkep, SARI], [26, 26, 2]);
    not("it + rise-s", kA);
    sat(["V", "+", "s"], yB, [kB + 8, kB + 11, kB + 13], [RT.murekkep, IKI, SARI], [26, 26]);
    not("V + s", kB + 8);
    const ar = S.ok([130, yA - 56], [130, yB - 14], { bas: kA + 8, sure: 8, w: 8, uzun: 24, bukum: 0.1 });
    not("ok A → B", ar.bas);
  }
  return S;
}

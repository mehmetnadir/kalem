// Sahne 03 (DİKEY) — Örnek 1 (PPC temel): Paper.js, 1080x1920, 467 kare, t_bas 17,13; cümle 3.
// Yerel kare = round((t − 17,13) × 30); zamanlar sozcukler.json ve altyazi.json ile aynı çerçevede.
// Yerleşim sıfırdan dikey: kart (tam genişlik) → TR çeviri → ORTA figür + otobüs → for satırı → formül.
import { sahneKur, RT } from "/projeler/present-perfect-cont-temel-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 467, T_BAS = 17.13;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1 });
  const { fr, ciz, daire, yazi, cumle, altCizgi, parilti, olay, not, bitis, genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;

  // --- kart: tam genişlik (984), Fredoka 72, 3 satır (anlam sınırında kırılır), sözcük zamanlı
  const sz = S.sozcukler(3).slice(2, 12);                          // I … minutes.
  const SATIR = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2], SH = 84, B1 = 360 + 34 + 54;
  const kartAlt = B1 + 2 * SH + 46;
  S.kutu(48, 360, 984, kartAlt - 360, { bas: fr(17.68), sure: 36, w: 4, renk: IKI });
  not("kart kutusu çizimi", fr(17.68));
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: SATIR[i] })),
    { x: 88, y: B1, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: SH });
  altCizgi(cz, { tut: 40, w: 9 }); not("cümle başı (I)", cz[0].bas); not("minutes", cz[9].bas);

  // --- 20,41–21,93: for twenty minutes altına sarı yay + 20 dk (kartın sağ alt köşesi)
  {
    const a = cz[7], b = cz[9], xm = (a.x0 + b.x1) / 2, y0 = a.y + 26;
    const yay = ciz([[a.x0, y0 - 8], [xm - 130, y0 + 9], [xm + 130, y0 + 9], [b.x1, y0 - 8]],
      { w: 10, renk: SARI, alfa: 0.85, bas: fr(20.41), sure: 26, uc0: 14, uc1: 30, amp: 0.7 });
    not("for twenty minutes yayı", yay.bas);
    const gen = genislik("20 dk", "700 72px Caveat");
    yazi("20 dk", { x: Math.min(b.x1 + 36, 1020 - gen), y: a.y - 6, boyut: 72, renk: SARI,
      bas: bitis(yay) - 4, sure: 12, ses: true });
  }

  // --- 22,10 Türkçe çeviri (Caveat 64, mürekkep)
  const yTR = kartAlt + 56;
  yazi("Yirmi dakikadır otobüs bekliyorum.", { x: 56, y: yTR, boyut: 64, aile: "Caveat", agirlik: 700,
    renk: RT.murekkep, bas: fr(22.1), sure: 22 });
  not("Türkçe çeviri", fr(22.1));

  // --- ORTA: bekleyen figür + otobüs + küçük saat (bant: TR altı → for satırı üstü)
  const fUst = yTR + 20, fAlt = fUst + 420;
  const figOge = S.oge({ nefes: { bas: fr(22.0), cx: 215, cy: fAlt } });
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [48, fUst, 340, 420], bas: fr(18.9),
    sure: fr(20.7) - fr(18.9), azami: 60, yuz: 3, w: 4.4, oge: figOge, sesAralik: 5 });
  not("figür çizimi başı", fr(18.9));
  await S.svgCiz("tabler/bus.svg", { kutu: [400, fUst, 460, 420], bas: fr(20.1), sure: 30, azami: 25, w: 4,
    sesAralik: 2 });
  not("otobüs çizimi", fr(20.1));
  await S.svgCiz("tabler/clock.svg", { kutu: [880, fUst + 150, 140, 140], bas: fr(21.2), sure: 22, azami: 25,
    w: 4, sesAralik: 2 });
  not("saat çizimi", fr(21.2));
  parilti(1000, fUst + 140, { bas: fr(21.9), r: 26, periyot: 170, adet: 3 });

  // --- 25,87–28,28: for (Fredoka 130 sarı, vurus) + Caveat süre uzunluğu
  const yFor = 1262;
  {
    const f0 = fr(25.87);
    const fo = yazi("for", { x: 56, y: yFor, boyut: 130, aile: "Fredoka", agirlik: 700, renk: SARI, bas: f0,
      sure: 10, olcek: true, ses: "vurus" });
    olay(f0, "vurus", 0.85); not("for (vurgu)", f0);
    yazi("süre uzunluğu", { x: fo.x1 + 40, y: yFor, boyut: 64, aile: "Caveat", agirlik: 700, renk: RT.murekkep,
      bas: fr(27.64), sure: 14, ses: true });
    not("süre uzunluğu", fr(27.64));
  }

  // --- 29,72 have been ve 31,08 waiting: kartta sarı daire
  {
    const a = cz[1], b = cz[2], c = cz[3];
    const da = daire((a.x0 + b.x1) / 2, a.y - 24, (b.x1 - a.x0) / 2 + 4, 40, { bas: fr(29.72), sure: 18, a0: -1.8 });
    olay(bitis(da), "tik", 0.5); not("have been daire", da.bas);
    const dc = daire((c.x0 + c.x1) / 2, c.y - 24, c.w / 2 + 2, 40, { bas: fr(31.08), sure: 18, a0: -2.8 });
    olay(bitis(dc), "tik", 0.5); not("waiting daire", dc.bas);
  }

  // --- 28,84–32,28 alt formül: have been + V-ing (Fredoka 100'e kadar, 900 px'e sığar)
  {
    let boy = 110; const F = (b) => `700 ${b}px Fredoka`;
    const GAP = [26, 26, 2];
    const P4 = ["have been", "+", "V", "-ing"];
    const topla = (b) => P4.reduce((t, m) => t + genislik(m, F(b)), 0) + GAP.reduce((a, g) => a + g, 0);
    while (topla(boy) > 900 && boy > 80) boy -= 4;
    const yF = 1372, t = [29.72, 30.68, 31.08, 31.64], renk = [RT.murekkep, IKI, RT.murekkep, SARI];
    let x = 540 - topla(boy) / 2; const o = [];
    P4.forEach((m, i) => {
      const y = yazi(m, { x, y: yF, boyut: boy, aile: "Fredoka", agirlik: 700, renk: renk[i], bas: fr(t[i]),
        sure: 10, olcek: true, ses: i === 0 || i === 3 }); o.push(y); x = y.x1 + (GAP[i] == null ? 0 : GAP[i]); });
    not("have been + V-ing", fr(29.72));
    parilti(o[3].x1 + 40, yF - boy * 0.8, { bas: fr(31.9), r: 24 });
  }
  return S;
}

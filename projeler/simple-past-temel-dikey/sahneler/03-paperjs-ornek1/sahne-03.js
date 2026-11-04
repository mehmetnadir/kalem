// Sahne 03 (DİKEY 1080x1920) — Örnek 1 (448 kare, t_bas 14,80; cümle 3). Yerel kare = round((t − 14,80) × 30).
// Bantlar: HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 (kalem-paper.js çizer) · platform boş. Yerleşim BRIEF-DIKEY §4.
import { sahneKur, RT, renkCoz } from "/projeler/simple-past-temel-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 448, T_BAS = 14.8;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, ok, yazi, cumle, altCizgi, tik, parilti, olay, not, bitis, genislik, kutu } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep;
  const GB = 12;                                                   // geçiş karesi: çizimler bundan sonra başlar
  const FF = { aile: "Fredoka", agirlik: 700 }, CV = { aile: "Caveat", agirlik: 700 };

  // --- kart (tam genişlik 984, kenar 4 px kalem çizgisi) + daire içinde 1 (sağ üst köşe)
  kutu(48, 372, 984, 308, { bas: GB, sure: 26, w: 4, renk: KRE }); not("kart kutusu", GB);
  const d1 = daire(940, 452, 48, 46, { bas: GB + 8, sure: 20, a0: -2.6, w: 9 }); olay(bitis(d1), "tik", 0.5); not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 940, y: 482, hizala: "orta", boyut: 84, ...FF, bas: GB + 12, sure: 10, olcek: true });

  // --- 16,09–18,09: cümle (Fredoka 72, x 96, y 475/565, 2 satır), sözcük sözcük + sarı alt çizgi
  const sz = S.sozcukler(3).slice(2, 8);                           // I watched a movie last night.
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 })), { x: 96, y: 475, boyut: 72, ...FF, aralik: 90 });
  altCizgi(cz, { tut: 60, w: 9 }); not("cümle başı (I)", cz[0].bas); not("night", cz[5].bas);

  // --- 17,37–18,09: last night sarı daire + LAST NIGHT etiketi (satır 2, sağda)
  {
    const a = cz[4], b = cz[5], cx = (a.x0 + b.x1) / 2, w = b.x1 - a.x0;
    const d = daire(cx, a.y - 24, w / 2 + 14, 50, { bas: fr(17.37), sure: 16, a0: -2.2, w: 10 });
    olay(bitis(d), "tik", 0.5); not("last night daire", d.bas);
    yazi("LAST NIGHT", { x: b.x1 + 90, y: a.y + 2, boyut: 64, ...CV, renk: SARI, bas: bitis(d) + 2, sure: 12, olcek: true, ses: true });
  }

  // --- 18,34–20,0: Dün gece bir film izledim. (Caveat 64 murekkep, y 650)
  yazi("Dün gece bir film izledim.", { x: 96, y: 650, boyut: 64, ...CV, bas: fr(18.34), sure: 24, ses: true });
  not("Türkçe çeviri", fr(18.34));

  // --- 16,1–18,0: orta: oturan figür + televizyon (420 px), ekranda 3 parıltı çizgisi; 20,0–20,6 küçülüp yukarıda toplanır
  const grup = S.oge({ nefes: { bas: fr(18.3), cx: 300, cy: 1100 }, kucul: { f0: fr(20.0), f1: fr(20.6), s: 0.55, cx: 540, cy: 705 } });
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [90, 705, 380, 430], bas: fr(16.1), sure: fr(18.0) - fr(16.1),
    azami: 60, yuz: 3, w: 4.4, oge: grup, sesAralik: 5, ayna: false });
  not("figür çizimi başı", fr(16.1));
  await S.svgCiz("tabler/device-tv.svg", { kutu: [560, 725, 440, 440], bas: fr(17.2), sure: 24, azami: 25, w: 4.4, oge: grup, sesAralik: 1 });
  not("televizyon çizimi başı", fr(17.2));
  [[[640, 960], [720, 890]], [[640, 1010], [760, 915]], [[640, 1060], [800, 940]]].forEach((p, i) => {
    ciz([p[0], [(p[0][0] + p[1][0]) / 2 + 2, (p[0][1] + p[1][1]) / 2], p[1]],
      { w: 9, renk: RT.vurgu, alfa: 0.85, bas: fr(18.1) + i * 5, sure: 8, uc0: 6, uc1: 12, amp: 0.6, oge: grup }); });
  not("ekran parıltı çizgileri", fr(18.1));
  parilti(980, 790, { bas: fr(18.5), r: 26, periyot: 170, adet: 1, oge: grup });

  // --- 20,22–22,90: zaman çizgisi (y 1085): bitti kutusu, belli tik, last night noktası, now
  {
    const yT = 1085, tl = ciz([[60, yT + 2], [330, yT - 2], [700, yT + 1], [1010, yT - 1]],
      { w: 5, renk: RT.ikincil, alfa: 0.9, bas: fr(20.22), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[975, yT - 22], [1012, yT - 1], [975, yT + 20]], { w: 5, renk: RT.ikincil, alfa: 0.9, bas: bitis(tl) - 2, sure: 7, duz: true,
      uc0: 5, uc1: 5, ses: false });
    kutu(250, 975, 500, 84, { bas: fr(20.63) - 4, sure: 22, w: 4 }); not("bitti kutusu", fr(20.63) - 4);
    yazi("bitti", { x: 500, y: 1035, hizala: "orta", boyut: 64, ...CV, renk: SARI, bas: fr(20.63), sure: 10, olcek: true, ses: true });
    const b = yazi("belli", { x: 790, y: 1035, boyut: 64, ...CV, bas: fr(21.78), sure: 10, olcek: true, ses: true }); not("belli", b.bas);
    tik(b.x1 + 36, 1015, { bas: fr(21.78) + 10 });
    const f0 = fr(22.5);
    S.dinamik((f, g) => {
      if (f < f0) return;
      g.addChild(new P.Path.Circle({ center: [140, yT], radius: 16 * Math.min(1, (f - f0) / 5), fillColor: renkCoz(SARI), insert: false }));
    });
    olay(f0, "tik", 0.5); not("last night noktası", f0);
    yazi("last night", { x: 48, y: yT + 75, boyut: 64, ...CV, bas: f0 + 2, sure: 10 });
    const dn = daire(930, yT, 19, 19, { bas: fr(22.7), sure: 10, w: 6, tur: 1.05 }); not("now noktası", dn.bas);
    yazi("now", { x: 1032, y: yT + 75, hizala: "sag", boyut: 64, ...CV, bas: fr(22.8), sure: 10 });
  }

  // --- 25,21 / 26,17: watched içinde watch ve -ed sarı daire
  {
    const w = cz[1], f = "700 72px Fredoka", g1 = genislik("watch", f), g2 = genislik("ed", f);
    const d1_ = daire(w.x0 + g1 / 2, w.y - 24, g1 / 2 + 10, 48, { bas: fr(25.21), sure: 16, a0: -1.8, w: 10 });
    olay(bitis(d1_), "tik", 0.5); not("watch daire", d1_.bas);
    const d2 = daire(w.x0 + g1 + g2 / 2 + 2, w.y - 24, g2 / 2 + 12, 48, { bas: fr(26.17), sure: 14, a0: -2.8, w: 10 });
    olay(bitis(d2), "tik", 0.5); not("-ed daire", d2.bas);
  }

  // --- 27,04–28,80: formül (Fredoka 110, alt bant): V + -ed / watch → watch-ed; Caveat izle-di
  {
    const y1 = 1275, y2 = 1380, F = { boyut: 110, ...FF };
    yazi("V", { ...F, x: 60, y: y1, bas: fr(27.04), sure: 8, olcek: true, ses: true }); not("V", fr(27.04));
    yazi("+", { ...F, x: 190, y: y1, bas: fr(27.4), sure: 8, olcek: true });
    yazi("-ed", { ...F, x: 300, y: y1, bas: fr(27.76), sure: 10, olcek: true, renk: SARI, ses: true }); not("-ed (formül)", fr(27.76));
    const fs = Math.min(110, Math.floor(110 * 900 / (genislik("watch", "700 110px Fredoka") * 2 + genislik("-ed", "700 110px Fredoka") + 110)));
    const F2 = { boyut: fs, ...FF };
    const a = yazi("watch", { ...F2, x: 60, y: y2, bas: fr(27.9), sure: 9, olcek: true });
    ok([a.x1 + 26, y2 - fs * 0.32], [a.x1 + 100, y2 - fs * 0.32], { bas: fr(28.1), sure: 14, w: 9 });
    const w1 = yazi("watch", { ...F2, x: a.x1 + 130, y: y2, bas: fr(28.3), sure: 9, olcek: true });
    yazi("-ed", { ...F2, x: w1.x1 + 2, y: y2, bas: fr(28.3) + 4, sure: 9, olcek: true, renk: SARI, ses: true }); not("watch-ed", fr(28.3));
    yazi("izle-di", { x: 600, y: y1 - 6, boyut: 80, ...CV, bas: fr(28.5), sure: 12, ses: true }); not("izle-di", fr(28.5));
    parilti(960, 1220, { bas: fr(28.65), r: 26 });
  }
  return S;
}

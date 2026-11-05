// Sahne 03 — Örnek 1 (Simple Past, 448 kare, t_bas 14,80; cümle 3). Zamanlar BRIEF §4; yerel kare = round((t − 14,80) × 30).
// elYazisi: 03 kopyası da taşır (05.11 motor taşıması 96b0651).
import { sahneKur, RT, renkCoz }
  from "/projeler/simple-past-temel/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 448, T_BAS = 14.8;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, ok, yazi, elYazisi, cumle, altCizgi, tik, parilti, olay, not, bitis,
    genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12;                                                   // geçiş karesi: çizimler bundan sonra başlar
  const FF = { aile: "Fredoka", agirlik: 700 };

  // --- 14,80–15,84: büyük el çizimi daire içinde 1 (x 200, y 190)
  const d1 = daire(200, 190, 66, 62, { bas: GB, sure: 20, a0: -2.6 }); olay(bitis(d1), "tik", 0.5); not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 226, hizala: "orta", boyut: 100, ...FF, bas: GB + 4, sure: 10, olcek: true });

  // --- 16,09–18,09: cümle (Fredoka 64, x 140, y 320, 2 satır), sözcük sözcük + sarı alt çizgi
  const sz = S.sozcukler(3).slice(2, 8);                           // I watched a movie last night.
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 })),
    { x: 140, y: 320, boyut: 64, ...FF, aralik: 82 });
  altCizgi(cz, { tut: 60 }); not("cümle başı (I)", cz[0].bas); not("night", cz[5].bas);

  // --- 16,1–18,0: sağ sütun: oturan figür + televizyon (420 px), ekranda 3 parıltı çizgisi
  const figOge = S.oge({ nefes: { bas: fr(18.3), cx: 1200, cy: 790 } });
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [1000, 250, 400, 540], bas: fr(16.1), sure: fr(18.0) - fr(16.1),
    azami: 60, yuz: 3, w: 3.4, oge: figOge, sesAralik: 5, ayna: false });
  not("figür çizimi başı", fr(16.1));
  await S.svgCiz("tabler/device-tv.svg", { kutu: [1440, 330, 420, 420], bas: fr(17.2), sure: 24, azami: 25, w: 4, sesAralik: 1 });
  not("televizyon çizimi başı", fr(17.2));
  [[[1530, 555], [1600, 495]], [[1530, 605], [1640, 515]], [[1530, 655], [1680, 535]]].forEach((p, i) => {
    ciz([p[0], [(p[0][0] + p[1][0]) / 2 + 2, (p[0][1] + p[1][1]) / 2], p[1]],
      { w: 5, renk: RT.vurgu, alfa: 0.85, bas: fr(18.1) + i * 5, sure: 8, uc0: 6, uc1: 12, amp: 0.6 }); });
  not("ekran parıltı çizgileri", fr(18.1));
  parilti(1810, 385, { bas: fr(18.5), r: 24, periyot: 170, adet: 5 });

  // --- 17,37–18,09: last night sarı daire + LAST NIGHT etiketi
  {
    const a = cz[4], b = cz[5], cx = (a.x0 + b.x1) / 2, w = b.x1 - a.x0;
    const d = daire(cx, a.y - 20, w / 2 + 12, 44, { bas: fr(17.37), sure: 16, a0: -2.2 });
    olay(bitis(d), "tik", 0.5); not("last night daire", d.bas);
    elYazisi("LAST NIGHT", { x: b.x1 + 80, y: a.y + 4, boyut: 56, renk: SARI, bas: bitis(d) + 2,
      sure: 14, ses: true });                   // etiket: anlatımsız, 17,97–18,43 sn
  }

  // --- 18,34–20,0: Dün gece bir film izledim. (el yazısı 48 ikincil, y 495, 5 sözcük penceresi)
  {   // el yazısı: her sözcük kendi konuşma penceresinde (Dün 18,34 · gece 18,58 · bir 18,82 ·
    // film 19,10 · izledim. 19,30–20,18 sn; kaynak cümle 3: "Dün gece bir film izledim.")
    const tr = S.sozcukler(3), i0 = tr.findIndex((w) => w.s === "Dün");
    elYazisi("Dün gece bir film izledim.", { x: 140, y: 495, boyut: 48, renk: IKI, ses: true,
      sozcukler: tr.slice(i0, i0 + 5).map((w) => ({ f0: w.f, f1: w.f1 })) });
    not("Türkçe çeviri", fr(18.34));
  }

  // --- 20,22–22,90: zaman çizgisi: bitti kutusu, belli tik, last night noktası, now
  {
    const yT = 645, tl = ciz([[140, yT + 2], [420, yT - 2], [700, yT + 1], [965, yT - 1]],
      { w: 4.2, renk: IKI, alfa: 0.9, bas: fr(20.22), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[935, yT - 17], [966, yT - 1], [935, yT + 14]], { w: 4.2, renk: IKI, alfa: 0.9, bas: bitis(tl) - 2, sure: 7, duz: true,
      uc0: 5, uc1: 5, ses: false });
    const kt = S.kutu(330, 560, 480, 66, { bas: fr(20.63) - 4, sure: 22, w: 3.6 }); not("bitti kutusu", fr(20.63) - 4);
    // el yazısı, konuşma penceresinde: bitti, 20,63–21,14 sn · belli: 21,78–22,42 sn (cümle 3)
    const tr3 = S.sozcukler(3);
    const pen = (ad) => { const q = tr3.find((w) => w.s === ad); return { f0: q.f, f1: q.f1 }; };
    elYazisi("bitti", { x: 570 - S.genislik("bitti", "700 52px Caveat") / 2, y: 610, boyut: 52,
      renk: SARI, sozcukler: [pen("bitti,")], ses: true });
    const b = elYazisi("belli", { x: 520, y: 722, boyut: 52, sozcukler: [pen("belli:")],
      ses: true });
    not("belli", b.bas);
    tik(b.x1 + 36, 706, { bas: fr(21.78) + 10 });
    const f0 = fr(22.5);
    S.dinamik((f, g) => {
      if (f < f0) return;
      g.addChild(new P.Path.Circle({ center: [260, yT], radius: 13 * Math.min(1, (f - f0) / 5), fillColor: renkCoz(SARI),
        insert: false }));
    });
    olay(f0, "tik", 0.5); not("last night noktası", f0);
    yazi("last night", { x: 260, y: yT + 62, hizala: "orta", boyut: 28, aile: "Lexend", agirlik: 500, renk: IKI, bas: f0 + 2, sure: 8 });
    const dn = daire(910, yT, 15, 15, { bas: fr(22.7), sure: 10, w: 5, tur: 1.05 }); not("now noktası", dn.bas);
    yazi("now", { x: 910, y: yT + 62, hizala: "orta", boyut: 28, aile: "Lexend", agirlik: 500, renk: IKI, bas: fr(22.8), sure: 8 });
  }

  // --- 25,21 / 26,17: watched içinde watch ve -ed sarı daire
  {
    const w = cz[1], f = "700 64px Fredoka", g1 = genislik("watch", f), g2 = genislik("ed", f);
    const d1_ = daire(w.x0 + g1 / 2, w.y - 22, g1 / 2 + 8, 40, { bas: fr(25.21), sure: 16, a0: -1.8 });
    olay(bitis(d1_), "tik", 0.5); not("watch daire", d1_.bas);
    const d2 = daire(w.x0 + g1 + g2 / 2 + 2, w.y - 22, g2 / 2 + 10, 40, { bas: fr(26.17), sure: 14, a0: -2.8 });
    olay(bitis(d2), "tik", 0.5); not("-ed daire", d2.bas);
  }

  // --- 27,04–28,80: formül kartı (el kutusu): V + -ed / watch → watch-ed, el yazısı izle-di
  {
    S.kutu(140, 745, 780, 220, { bas: fr(27.04) - 10, sure: 24 }); not("formül kartı kutusu", fr(27.04) - 10);
    const y1 = 835, y2 = 930, F = { boyut: 60, ...FF }, F2 = { boyut: 56, ...FF };
    yazi("V", { ...F, x: 200, y: y1, bas: fr(27.04), sure: 8, olcek: true, ses: true }); not("V", fr(27.04));
    yazi("+", { ...F, x: 290, y: y1, bas: fr(27.4), sure: 8, olcek: true });
    yazi("-ed", { ...F, x: 370, y: y1, bas: fr(27.76), sure: 10, olcek: true, renk: SARI, ses: true }); not("-ed (kart)", fr(27.76));
    const a = yazi("watch", { ...F2, x: 200, y: y2, bas: fr(27.9), sure: 9, olcek: true });
    ok([a.x1 + 24, y2 - 20], [a.x1 + 104, y2 - 20], { bas: fr(28.1), sure: 14, w: 6 });
    const x2 = a.x1 + 130;
    const w1 = yazi("watch", { ...F2, x: x2, y: y2, bas: fr(28.3), sure: 9, olcek: true });
    yazi("-ed", { ...F2, x: w1.x1 + 2, y: y2, bas: fr(28.3) + 4, sure: 9, olcek: true, renk: SARI, ses: true }); not("watch-ed", fr(28.3));
    elYazisi("izle-di", { x: 960, y: y2, boyut: 56, renk: IKI, bas: fr(28.5), sure: 11,
      ses: true });
    not("izle-di", fr(28.5));                       // sure 11: cümle 3 sonu 28,88 sn
    parilti(880, 790, { bas: fr(28.65), r: 22 });
  }
  return S;
}

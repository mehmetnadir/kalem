// Sahne 03 (DİKEY 1080x1920) — Örnek 1 (448 kare, t_bas 14,80; cümle 3).
// Yerel kare = round((t − 14,80) × 30).
// Bantlar: HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 (kalem-paper.js çizer)
// · platform boş.
// Yerleşim BRIEF-DIKEY §4.
import {
  sahneKur, RT, renkCoz
} from "/projeler/simple-past-temel-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 448, T_BAS = 14.8;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const {
    fr, ciz, daire, ok, yazi, cumle, altCizgi, tik, parilti, olay, not, bitis, genislik, kutu
  } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep;
  const GB = 12; // geçiş karesi: çizimler bundan sonra başlar
  const FF = { aile: "Fredoka", agirlik: 700 }, CV = { aile: "Caveat", agirlik: 700 };

  // --- kart (tam genişlik 984, kenar 4 px kalem çizgisi) + daire içinde 1 (sağ üst köşe)
  kutu(48, 372, 984, 308, { bas: GB, sure: 26, w: 4, renk: KRE }); not("kart kutusu", GB);
  const d1 = daire(940, 452, 48, 46, { bas: GB + 8, sure: 20, a0: -2.6, w: 9 });
  olay(bitis(d1), "tik", 0.5); not("daire 1 çizimi", d1.bas);
  yazi("1", {
    x: 940, y: 482, hizala: "orta", boyut: 84, ...FF, bas: GB + 12, sure: 10, olcek: true
  });

  // --- 16,09–18,09: cümle (Fredoka 72, x 96, y 475/565, 2 satır),
  // sözcük sözcük + sarı alt çizgi
  const sz = S.sozcukler(3).slice(2, 8); // I watched a movie last night.
  const cz = cumle(
    sz.map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 })),
    { x: 96, y: 475, boyut: 72, ...FF, aralik: 90 }
  );
  altCizgi(cz, { tut: 60, w: 9 }); not("cümle başı (I)", cz[0].bas); not("night", cz[5].bas);

  // --- 17,37–18,09: last night sarı daire + LAST NIGHT etiketi (satır 2, sağda)
  {
    const a = cz[4], b = cz[5], cx = (a.x0 + b.x1) / 2, w = b.x1 - a.x0;
    const d = daire(cx, a.y - 24, w / 2 + 14, 50, {
      bas: fr(17.37), sure: 16, a0: -2.2, w: 10
    });
    olay(bitis(d), "tik", 0.5); not("last night daire", d.bas);
    yazi("LAST NIGHT", {
      x: b.x1 + 90, y: a.y + 2, boyut: 64, ...CV, renk: SARI, bas: bitis(d) + 2,
      sure: 12, olcek: true, ses: true
    });
  }

  // --- 18,34–20,0: Dün gece bir film izledim. (Caveat 64 murekkep, y 650)
  yazi("Dün gece bir film izledim.", {
    x: 96, y: 650, boyut: 64, ...CV, bas: fr(18.34), sure: 24, ses: true
  });
  not("Türkçe çeviri", fr(18.34));

  // --- 16,1–18,0: orta: oturan figür 430 px + televizyon 380 px, ekranda 3 parıltı çizgisi;
  // 19,7–20,3'te ikisi alt bölgeye (955–1385) iner, hiç küçülmez;
  // TV 26,4–26,9'da solar (formüle yer)
  const KAY = { f0: fr(19.7), f1: fr(20.3), dx: 0, dy: 165 };
  const grup = S.oge({ kay: KAY, nefes: { bas: fr(18.3), cx: 300, cy: 1100 } });
  const tvGrup = S.oge({
    kay: KAY, alfa: (f) => 1 - Math.min(1, Math.max(0, (f - fr(26.4)) / 15))
  });
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [60, 790, 380, 430], bas: fr(16.1),
    sure: fr(18.0) - fr(16.1), azami: 60, yuz: 3, w: 4.4, oge: grup, sesAralik: 5, ayna: false });
  not("figür çizimi başı", fr(16.1));
  await S.svgCiz("tabler/device-tv.svg", { kutu: [620, 800, 380, 380], bas: fr(17.2), sure: 24,
    azami: 25, w: 4.4, oge: tvGrup, sesAralik: 1 });
  not("televizyon çizimi başı", fr(17.2));
  [
    [[689, 1003], [758, 943]], [[689, 1046], [793, 965]], [[689, 1090], [828, 987]]
  ].forEach((p, i) => {
    ciz([p[0], [(p[0][0] + p[1][0]) / 2 + 2, (p[0][1] + p[1][1]) / 2], p[1]],
      { w: 9, renk: RT.vurgu, alfa: 0.85, bas: fr(18.1) + i * 5, sure: 8, uc0: 6, uc1: 12, amp: 0.6,
        oge: tvGrup }); });
  not("ekran parıltı çizgileri", fr(18.1));
  parilti(985, 830, { bas: fr(18.5), r: 26, periyot: 170, adet: 1, oge: tvGrup });

  // --- 20,22–22,90: zaman çizgisi ORTA bölge (700–930):
  // bitti kutusu, belli tik, last night, now
  {
    const yT = 840, tl = ciz([[60, yT + 2], [330, yT - 2], [700, yT + 1], [1010, yT - 1]],
      { w: 5, renk: RT.ikincil, alfa: 0.9, bas: fr(20.22), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[975, yT - 22], [1012, yT - 1], [975, yT + 20]], { w: 5, renk: RT.ikincil, alfa: 0.9,
      bas: bitis(tl) - 2, sure: 7, duz: true, uc0: 5, uc1: 5, ses: false });
    kutu(250, 718, 500, 84, {
      bas: fr(20.63) - 4, sure: 22, w: 4
    }); not("bitti kutusu", fr(20.63) - 4);
    yazi("bitti", { x: 500, y: 778, hizala: "orta", boyut: 64, ...CV, renk: SARI, bas: fr(20.63),
      sure: 10, olcek: true, ses: true });
    const b = yazi("belli", {
      x: 790, y: 778, boyut: 64, ...CV, bas: fr(21.78), sure: 10, olcek: true, ses: true
    }); not("belli", b.bas);
    tik(b.x1 + 36, 758, { bas: fr(21.78) + 10 });
    const f0 = fr(22.5);
    S.dinamik((f, g) => {
      if (f < f0) return;
      g.addChild(new P.Path.Circle({ center: [140, yT], radius: 16 * Math.min(1, (f - f0) / 5),
        fillColor: renkCoz(SARI), insert: false }));
    });
    olay(f0, "tik", 0.5); not("last night noktası", f0);
    yazi("last night", { x: 48, y: yT + 72, boyut: 64, ...CV, bas: f0 + 2, sure: 10 });
    const dn = daire(930, yT, 19, 19, {
      bas: fr(22.7), sure: 10, w: 6, tur: 1.05
    }); not("now noktası", dn.bas);
    yazi("now", { x: 1032, y: yT + 72, hizala: "sag", boyut: 64, ...CV, bas: fr(22.8), sure: 10 });
  }

  // --- 25,21 / 26,17: watched içinde watch ve -ed sarı daire
  {
    const w = cz[1], f = "700 72px Fredoka", g1 = genislik("watch", f), g2 = genislik("ed", f);
    const d1_ = daire(w.x0 + g1 / 2, w.y - 24, g1 / 2 + 10, 48, {
      bas: fr(25.21), sure: 16, a0: -1.8, w: 10
    });
    olay(bitis(d1_), "tik", 0.5); not("watch daire", d1_.bas);
    const d2 = daire(w.x0 + g1 + g2 / 2 + 2, w.y - 24, g2 / 2 + 12, 48, {
      bas: fr(26.17), sure: 14, a0: -2.8, w: 10
    });
    olay(bitis(d2), "tik", 0.5); not("-ed daire", d2.bas);
  }

  // --- 27,04–28,80: formül alt bölge sağ sütun (x 470–1032, Fredoka ≥ 64):
  // V + -ed / watch → watch-ed
  {
    const X0 = 470, WMAX = 560, GAP = 100, y1 = 1120, y2 = 1240;
    const fw = (m, k) => genislik(m, `700 ${k}px Fredoka`);
    let fs = 96;
    while (fs > 64 && 2 * fw("watch", fs) + fw("-ed", fs) + GAP > WMAX) fs -= 1;
    const F = { boyut: 96, ...FF }, k = 96 / 110;
    yazi("V", {
      ...F, x: X0, y: y1, bas: fr(27.04), sure: 8, olcek: true, ses: true
    }); not("V", fr(27.04));
    yazi("+", { ...F, x: X0 + 130 * k, y: y1, bas: fr(27.4), sure: 8, olcek: true });
    const e = yazi("-ed", { ...F, x: X0 + 240 * k, y: y1, renk: SARI, bas: fr(27.76), sure: 10,
      olcek: true, ses: true }); not("-ed (formül)", fr(27.76));
    const F2 = { boyut: fs, ...FF };
    const a = yazi("watch", { ...F2, x: X0, y: y2, bas: fr(27.9), sure: 9, olcek: true });
    ok(
      [a.x1 + 14, y2 - fs * 0.32], [a.x1 + GAP - 14, y2 - fs * 0.32],
      { bas: fr(28.1), sure: 14, w: 9 }
    );
    const w1 = yazi("watch", { ...F2, x: a.x1 + GAP, y: y2, bas: fr(28.3), sure: 9, olcek: true });
    yazi("-ed", { ...F2, x: w1.x1 + 2, y: y2, renk: SARI, bas: fr(28.3) + 4, sure: 9, olcek: true,
      ses: true }); not("watch-ed", fr(28.3));
    yazi("izle-di", {
      x: e.x1 + 40, y: y1 - 4, boyut: 72, ...CV, bas: fr(28.5), sure: 12, ses: true
    });
    not("izle-di", fr(28.5));
    parilti(1000, 1030, { bas: fr(28.65), r: 26 });
  }
  return S;
}

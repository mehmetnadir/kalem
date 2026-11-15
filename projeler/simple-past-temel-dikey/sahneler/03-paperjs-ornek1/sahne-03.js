// Sahne 03 (DİKEY 1080x1920) — Örnek 1 (465 kare, t_bas 16,24; cümle 3).
// Yerel kare = round((t − 16,24) × 30).
// Bantlar: HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 (kalem-paper.js çizer)
// · platform boş.
// Yerleşim BRIEF-DIKEY §4.
import {
  sahneKur, RT, renkCoz
} from "/projeler/simple-past-temel-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";
import { yaziNoktalari } from "/projeler/simple-past-temel-dikey/ortak/kalem-canvas.js";

export const KARE = 465, T_BAS = 16.24;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const {
    fr, ciz, daire, ok, yazi, elYazisi, cumle, altCizgi, tik, parilti, olay, not, bitis, genislik,
    kutu
  } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep;
  const GB = 12; // geçiş karesi: çizimler bundan sonra başlar
  const FF = { aile: "Fredoka", agirlik: 700 };

  // --- el yazısı (Caveat 700 tegaki, dalga 5b / K26): not ve etiketler kalemle yazılır.
  // Ortaya/sağa hizalı x çizimden önce hesaplanır (yaziNoktalari.gen); sözcük pencereleri
  // anlatımın f / f1 karelerinden gelir.
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm,
    asc: EY.M.ascender, boy: boyut, x: 0, taban: 0 }).gen;
  const CS = S.sozcukler(3); // cümle 3: f / f1 yerel kare
  const norm = (s) => s.replace(/[.,:;?!]/g, "");
  const pen = (ilk, adet, tMin = 0) => {
    const i = CS.findIndex((w) => norm(w.s) === ilk && w.f >= fr(tMin));
    return CS.slice(i, i + adet).map((w) => ({ f0: w.f, f1: w.f1 }));
  };

  // --- kart (tam genişlik 984, kenar 4 px kalem çizgisi) + daire içinde 1 (sağ üst köşe)
  kutu(48, 372, 984, 308, { bas: GB, sure: 26, w: 4, renk: KRE }); not("kart kutusu", GB);
  const d1 = daire(940, 452, 48, 46, { bas: GB + 8, sure: 20, a0: -2.6, w: 9 });
  olay(bitis(d1), "tik", 0.5); not("daire 1 çizimi", d1.bas);
  yazi("1", {
    x: 940, y: 482, hizala: "orta", boyut: 84, ...FF, bas: GB + 12, sure: 10, olcek: true
  });

  // --- 17,53–19,53: cümle (Fredoka 72, x 96, y 475/565, 2 satır),
  // sözcük sözcük + sarı alt çizgi
  const sz = S.sozcukler(3).slice(2, 8); // I watched a movie last night.
  const cz = cumle(
    sz.map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 })),
    { x: 96, y: 475, boyut: 72, ...FF, aralik: 90 }
  );
  altCizgi(cz, { tut: 60, w: 9 }); not("cümle başı (I)", cz[0].bas); not("night", cz[5].bas);

  // --- 18,81–19,53: last night sarı daire + LAST NIGHT etiketi (satır 2, sağda)
  {
    const a = cz[4], b = cz[5], cx = (a.x0 + b.x1) / 2, w = b.x1 - a.x0;
    const d = daire(cx, a.y - 24, w / 2 + 14, 50, {
      bas: fr(18.81), sure: 16, a0: -2.2, w: 10
    });
    olay(bitis(d), "tik", 0.5); not("last night daire", d.bas);
    // anlatımsız etiket `LAST NIGHT` (daire biterken başlar): hedef 14 kare (0,47 sn) → 19,67
    elYazisi("LAST NIGHT", {
      x: b.x1 + 90, y: a.y + 2, boyut: 64, renk: SARI, bas: bitis(d) - 4, sure: 14
    });
  }

  // --- 19,78–21,44: Dün gece bir film izledim. (Caveat 64 murekkep, y 650)
  // 19,78–21,62 «Dün gece bir film izledim.» (pencere: her sözcük kendi konuşmasında)
  elYazisi("Dün gece bir film izledim.", {
    x: 96, y: 650, boyut: 64, renk: KRE, sozcukler: pen("Dün", 5)
  });
  not("Türkçe çeviri", fr(19.78));

  // --- 17,54–19,44: orta: oturan figür 430 px + televizyon 380 px, ekranda 3 parıltı çizgisi;
  // 21,14–21,74'te ikisi alt bölgeye (955–1385) iner, hiç küçülmez;
  // TV 27,84–28,34'te solar (formüle yer)
  const KAY = { f0: fr(21.14), f1: fr(21.74), dx: 0, dy: 165 };
  const grup = S.oge({ kay: KAY, nefes: { bas: fr(19.74), cx: 300, cy: 1100 } });
  const tvGrup = S.oge({
    kay: KAY, alfa: (f) => 1 - Math.min(1, Math.max(0, (f - fr(27.84)) / 15))
  });
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [60, 790, 380, 430], bas: fr(17.54),
    sure: fr(19.44) - fr(17.54), azami: 60, yuz: 3, w: 4.4, oge: grup, sesAralik: 5, ayna: false });
  not("figür çizimi başı", fr(17.54));
  await S.svgCiz("tabler/device-tv.svg", { kutu: [620, 800, 380, 380], bas: fr(18.64), sure: 24,
    azami: 25, w: 4.4, oge: tvGrup, sesAralik: 1 });
  not("televizyon çizimi başı", fr(18.64));
  [
    [[689, 1003], [758, 943]], [[689, 1046], [793, 965]], [[689, 1090], [828, 987]]
  ].forEach((p, i) => {
    ciz([p[0], [(p[0][0] + p[1][0]) / 2 + 2, (p[0][1] + p[1][1]) / 2], p[1]],
      { w: 9, renk: RT.vurgu, alfa: 0.85, bas: fr(19.54) + i * 5, sure: 8, uc0: 6, uc1: 12, amp: 0.6,
        oge: tvGrup }); });
  not("ekran parıltı çizgileri", fr(19.54));
  parilti(985, 830, { bas: fr(19.94), r: 26, periyot: 170, adet: 1, oge: tvGrup });

  // --- 21,66–24,34: zaman çizgisi ORTA bölge (700–930):
  // bitti kutusu, belli tik, last night, now
  {
    const yT = 840, tl = ciz([[60, yT + 2], [330, yT - 2], [700, yT + 1], [1010, yT - 1]],
      { w: 5, renk: RT.ikincil, alfa: 0.9, bas: fr(21.66), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[975, yT - 22], [1012, yT - 1], [975, yT + 20]], { w: 5, renk: RT.ikincil, alfa: 0.9,
      bas: bitis(tl) - 2, sure: 7, duz: true, uc0: 5, uc1: 5, ses: false });
    kutu(250, 718, 500, 84, {
      bas: fr(22.07) - 4, sure: 22, w: 4
    }); not("bitti kutusu", fr(22.07) - 4);
    // 22,07–22,58 «bitti» (ortalı x = 500; pencere 22,07–22,58)
    elYazisi("bitti", { x: 500 - eyGen("bitti", 64) / 2, y: 778, boyut: 64, renk: SARI,
      sozcukler: pen("bitti", 1) });
    // 23,22–23,86 «belli» (pencere 23,22–23,86); tik yazı bitince
    const b = elYazisi("belli", {
      x: 790, y: 778, boyut: 64, renk: KRE, sozcukler: pen("belli", 1)
    }); not("belli", b.bas);
    tik(b.x1 + 36, 758, { bas: b.bit });
    const f0 = fr(23.94);
    S.dinamik((f, g) => {
      if (f < f0) return;
      g.addChild(new P.Path.Circle({ center: [140, yT], radius: 16 * Math.min(1, (f - f0) / 5),
        fillColor: renkCoz(SARI), insert: false }));
    });
    olay(f0, "tik", 0.5); not("last night noktası", f0);
    // 23,94–25,14 «last night» (pencere: last 23,94–24,26 · night 24,34–25,14)
    elYazisi("last night", { x: 48, y: yT + 72, boyut: 64, renk: KRE,
      sozcukler: pen("last", 2, 22) });
    const dn = daire(930, yT, 19, 19, {
      bas: fr(24.14), sure: 10, w: 6, tur: 1.05
    }); not("now noktası", dn.bas);
    // 24,24 anlatımsız etiket `now`: hedef 14 kare (0,47 sn); sağ uç 1026 (+4 px çizgi payı)
    elYazisi("now", { x: 1026 - eyGen("now", 64), y: yT + 72, boyut: 64, renk: KRE,
      bas: fr(24.24), sure: 14 });
  }

  // --- 26,65 / 27,61: watched içinde watch ve -ed sarı daire
  {
    const w = cz[1], f = "700 72px Fredoka", g1 = genislik("watch", f), g2 = genislik("ed", f);
    const d1_ = daire(w.x0 + g1 / 2, w.y - 24, g1 / 2 + 10, 48, {
      bas: fr(26.65), sure: 16, a0: -1.8, w: 10
    });
    olay(bitis(d1_), "tik", 0.5); not("watch daire", d1_.bas);
    const d2 = daire(w.x0 + g1 + g2 / 2 + 2, w.y - 24, g2 / 2 + 12, 48, {
      bas: fr(27.61), sure: 14, a0: -2.8, w: 10
    });
    olay(bitis(d2), "tik", 0.5); not("-ed daire", d2.bas);
  }

  // --- 28,48–30,80: formül alt bölge sağ sütun (x 470–1032, Fredoka ≥ 64):
  // V + -ed / watch → watch-ed
  {
    const X0 = 470, WMAX = 560, GAP = 100, y1 = 1120, y2 = 1240;
    const fw = (m, k) => genislik(m, `700 ${k}px Fredoka`);
    let fs = 96;
    while (fs > 64 && 2 * fw("watch", fs) + fw("-ed", fs) + GAP > WMAX) fs -= 1;
    const F = { boyut: 96, ...FF }, k = 96 / 110;
    yazi("V", {
      ...F, x: X0, y: y1, bas: fr(29.04), sure: 8, olcek: true, ses: true
    }); not("V", fr(29.04));
    yazi("+", { ...F, x: X0 + 130 * k, y: y1, bas: fr(29.36), sure: 8, olcek: true });
    yazi("-ed", { ...F, x: X0 + 240 * k, y: y1, renk: SARI, bas: fr(29.68), sure: 10,
      olcek: true, ses: true }); not("-ed (formül)", fr(29.68));
    const F2 = { boyut: fs, ...FF };
    const a = yazi("watch", { ...F2, x: X0, y: y2, bas: fr(30.0), sure: 9, olcek: true });
    ok(
      [a.x1 + 14, y2 - fs * 0.32], [a.x1 + GAP - 14, y2 - fs * 0.32],
      { bas: fr(30.2), sure: 14, w: 9 }
    );
    const w1 = yazi("watch", { ...F2, x: a.x1 + GAP, y: y2, bas: fr(30.4), sure: 9, olcek: true });
    yazi("-ed", { ...F2, x: w1.x1 + 2, y: y2, renk: SARI, bas: fr(30.4) + 4, sure: 9, olcek: true,
      ses: true }); not("watch-ed", fr(30.4));
    // DUZ3 (16.11): `düzenli fiil` sözle (Düzenli 28,48 · fiile 29,04), formülün üstünde;
    // `izle-di` etiketi -di = -ed denkliği kurduğu için kalktı
    elYazisi("düzenli fiil", {
      x: X0, y: 1022, boyut: 64, renk: KRE, sozcukler: pen("Düzenli", 2)
    });
    not("düzenli fiil", fr(28.48));
    parilti(1000, 1030, { bas: fr(30.65), r: 26 });
  }
  return S;
}

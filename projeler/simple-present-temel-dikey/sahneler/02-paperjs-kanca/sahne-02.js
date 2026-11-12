// Sahne 02 — Kanca (DİKEY 1080x1920, 386 kare, t_bas 3,00; cümle 2 = 3,31–15,45).
// Yerel kare = round((t − 3,00) × 30).
// Sahne 01'in son hali (HUD + çip `Hook` + iki Caveat 80 satırı) kare 0'da hazır.
// Bantlar: HUD 0-320, içerik 352-1392, altyazı 1400-1536 (kalem-paper.js çizer).
// Yerleşim dikey için sıfırdan (BRIEF-DIKEY §3-§4).
import {
  sahneKur,
  RT,
} from "/projeler/simple-present-temel-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";
import { yaziNoktalari } from "/projeler/simple-present-temel-dikey/ortak/kalem-canvas.js";

export const KARE = 386, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook" });
  const {
    fr, ciz, daire, ok, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu, genislik,
    oge,
  } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const GB = 12; // geçiş karesi: çizimler bundan sonra

  // El yazısı (Caveat 700 tegaki, dalga 5b / K26): not ve etiketler kalemle yazılır. Ortalı
  // yazıda genişlik tegaki verisinden ölçülür; sözcük pencereleri anlatımın f/f1 karelerinden
  // gelir.
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm,
    asc: EY.M.ascender, boy: boyut, x: 0, taban: 0 }).gen;
  const CS = S.sozcukler(2); // cümle 2 sözcükleri (f0 / f1 yerel kare)
  const pen = (ilk, adet, t) => {
    const i = CS.findIndex((w) => w.s === ilk && w.t >= t - 0.01);
    return CS.slice(i, i + adet).map((w) => ({ f0: w.f, f1: w.f1 }));
  };

  // --- cümle 1 (sahne 01'in son hali): Caveat 80, x 72, y 440 / 524, kare 0'da hazır
  const c80 = { boyut: 80, aile: "Caveat", agirlik: 700 };
  const c1 = cumle(
    ["Her", "sabah", "yedide"].map((s) => ({ s, f: -30 })),
    { x: 72, y: 440, ...c80 }
  );
  cumle([{ s: "kalkarım.", f: -30 }], { x: 72, y: 524, ...c80 });
  not("cümle 1 (hazır)", 0);

  // --- orta bant: figür 450 px + yatak + duvar saati (y 780-1236), zemin çizgisi
  const figOge = oge({ nefes: { bas: fr(5.2), cx: 220, cy: 1230 } });
  await S.svgCiz("open-peeps/standing-1.svg", {
    kutu: [72, 780, 300, 450],
    bas: GB,
    sure: 46,
    azami: 60,
    yuz: 3,
    w: 4.4,
    oge: figOge,
    sesAralik: 5,
  });
  not("figür çizimi başı", GB);
  await S.svgCiz("coco/bed.svg", {
    kutu: [420, 830, 610, 400],
    bas: GB + 20,
    sure: 44,
    azami: 30,
    w: 4.0,
    sesAralik: 4,
  });
  not("yatak çizimi başı", GB + 20);
  await S.svgCiz("coco/clock.svg", {
    kutu: [850, 765, 170, 170],
    bas: GB + 50,
    sure: 30,
    azami: 25,
    w: 4.0,
    sesAralik: 3,
  });
  not("saat çizimi başı", GB + 50);
  ciz(
    [[60, 1238], [500, 1235], [1020, 1239]],
    { w: 4, renk: IKI, alfa: 0.75, bas: GB + 40, sure: 30, uc0: 10, uc1: 30 }
  );
  parilti(1000, 760, { bas: GB + 84, r: 22, periyot: 150, adet: 3 });

  // --- 5,71–7,77: kalkar · gider · yapar (Fredoka 64, sözcük zamanlı) + sarı daire
  {
    const kel = [["kalkar,", 5.71], ["gider,", 6.47], ["yapar.", 7.07]];
    let x = 72;
    const e = kel.map(([t, f]) => {
      const w = yazi(t, {
        x, y: 632, boyut: 64, aile: "Fredoka", agirlik: 700, renk: MUR, bas: fr(f), sure: 8,
      });
      x = w.x1 + 64; return w;
    });
    e.forEach((g, i) => {
      const d = daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 12, 40, {
        bas: fr(kel[i][1]) + 6, sure: 22, egim: -0.04 * (i + 1),
      });
      olay(bitis(d), "tik", 0.5); not("daire " + g.str, d.bas);
    });
    not("kalkar başı", e[0].bas);
  }

  // --- 7,78–10,42: not "geniş zaman" ⇄ "Simple Present" (el oku, iki yönlü),
  // tek satır y 735
  {
    const y = 735, f1 = "700 64px Caveat", f2 = "700 64px Fredoka",
      g1 = genislik("geniş zaman", f1),
      g2 = genislik("Simple Present", f2), ar = 104, bos = 24;
    const x0 = (1080 - (g1 + ar + g2 + 2 * bos)) / 2;
    // 7,78 anlatımsız etiket `geniş zaman` (anlatım 4,27'de geçti): hedef 18 kare (0,6 sn) → 8,38
    const a = elYazisi("geniş zaman", { x: x0, y, boyut: 64, renk: MUR, bas: fr(7.78), sure: 18 });
    not("not geniş zaman", a.bas);
    const o = ok([a.x1 + bos, y - 22], [a.x1 + bos + ar, y - 22], {
      bas: fr(8.7), sure: 18, w: 9, cift: true, uzun: 24, bukum: 0.06,
    });
    not("ok geniş zaman ⇄", o.bas);
    const s = yazi("Simple Present", {
      x: a.x1 + 2 * bos + ar, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: fr(9.3), sure: 14, olcek: true, ses: true,
    });
    not("Simple Present yazılır", s.bas);
    parilti(s.x1 + 6, y - 66, { bas: fr(10.1), r: 22, periyot: 160, adet: 3 });
  }

  // --- 10,65–15,45: ajanda: form · zaman ifadeleri · kullanımlar (üç kutu, sırayla tik),
  // y 1262-1382
  {
    // pencere: formunu, 11,53–12,17 · zaman 12,41–12,65 + ifadelerini 12,73–13,45 ·
    // kullanımlarını 13,77–14,41
    const ad = [["form", 11.53, pen("formunu,", 1, 11.5)],
      ["zaman ifadeleri", 12.41, pen("zaman", 2, 12.4)],
      ["kullanımlar", 13.77, pen("kullanımlarını", 1, 13.7)]];
    const f = "700 64px Caveat", pad = 56, bos = 16;
    const gw = ad.map(([s]) => genislik(s, f) + pad), top = gw.reduce((s, w) => s + w, 0) + bos * 2;
    let x = (1080 - top) / 2;
    ad.forEach(([s, t, pz], i) => {
      const w = gw[i], y = 1262, h = 120;
      kutu(x, y, w, h, { bas: fr(10.65) + i * 8, sure: 26, renk: IKI, w: 4.2 });
      const k = elYazisi(s, {
        x: x + w / 2 - eyGen(s, 64) / 2, y: y + 82, boyut: 64, renk: MUR, sozcukler: pz,
      });
      tik(x + w - 22, y + 14, { bas: fr(t) + 4 }); not("madde " + s, k.bas);
      x += w + bos;
    });
    not("ajanda kutuları başı", fr(10.65));
  }
  return S;
}

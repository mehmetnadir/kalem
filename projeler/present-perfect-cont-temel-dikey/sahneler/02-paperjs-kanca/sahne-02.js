// Sahne 02 — Kanca, DİKEY 1080x1920 (PPC temel, 436 kare, t_bas 3,00; cümle 2 = 3,39–17,13).
// Yerel kare = round((t − 3,00) × 30).
// Bantlar: içerik 352–1392 · altyazı 1400–1536 (kalem-paper.js çizer) ·
// platform 1536–1920 boş.
// Yerleşim: üstte kanca cümlesi + iki not satırı; ORTA solda figür (470 px, hep aynı boy),
// sağda saat + zaman çizgisi + dizüstü; altta İngilizce cümle.
// 10,6 sn'de saat karta taşınır, zaman çizgisi + dizüstü sağ alta toplanır
// (yazı ≥ 48 px).
import { sahneKur, RT }
  from "/projeler/present-perfect-cont-temel-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";
import { yaziNoktalari } from "/projeler/present-perfect-cont-temel-dikey/ortak/kalem-canvas.js";

export const KARE = 436, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook" });
  const {
    fr, ciz, daire, ok, yazi, elYazisi, cumle, altCizgi, tik, parilti, olay, not, bitis, kutu,
    genislik
  } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const GB = 12;                                                    // geçiş karesi: çizimler
                                                                    // bundan sonra
  const TOPLA0 = fr(10.6), TOPLA1 = fr(11.1);

  // El yazısı (Caveat 700 tegaki, dalga 5 / K26): not ve etiketler kalemle yazılır. Sağa hizada
  // genişlik tegaki verisinden ölçülür; sözcük pencereleri anlatımın f / f1 karelerinden gelir
  // (6 kareden kısa pencere sonraki sözcüğün başına dek uzar).
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm,
    asc: EY.M.ascender, boy: boyut, x: 0, taban: 0 }).gen;
  const CS = S.sozcukler(2);                                        // cümle 2 (f / f1 yerel kare)
  const pen = (ilk, adet) => { const i = CS.findIndex((w) => w.s === ilk);
    return CS.slice(i, i + adet).map((w, k, a) => ({ f0: w.f,
      f1: k < a.length - 1 && w.f1 - w.f < 6 ? a[k + 1].f : w.f1 })); };

  // --- cümle 1 (Caveat 80, tek satır, taban y 420): sahne 01'den devam;
  // 0–0,3 sn'de hazır belirir
  const c1 = cumle(["İki", "saattir", "çalışıyorum."].map((s, i) => ({ s, f: i * 3 })),
    { x: 48, y: 420, boyut: 80, aile: "Caveat", agirlik: 700 });
  not("cümle 1 başı (İki)", c1[0].bas); not("çalışıyorum", c1[2].bas);

  // --- orta bant sol: oturan figür 470 px + zemin çizgisi
  const figOge = S.oge({ nefes: { bas: fr(7.0), cx: 215, cy: 1185 } });
  await S.svgCiz("open-peeps/sitting-5.svg", {
    kutu: [48, 715, 340, 470], bas: GB, sure: 44, azami: 60, yuz: 3, w: 4.4, oge: figOge,
    sesAralik: 5
  });
  not("figür çizimi başı", GB);
  ciz([[40, 1192], [320, 1188], [700, 1194], [1040, 1190]],
    { w: 3.6, renk: IKI, alfa: 0.75, bas: 40, sure: 28, uc0: 10, uc1: 30 });
  // sağ grup: zaman çizgisi + dizüstü (10,6 sn'de sağ alta toplanır); saat ayrı
  // (karta taşınır)
  const sag = S.oge({
    topla: { f0: TOPLA0, f1: TOPLA1, dx: 0, dy: 0, s: 0.55, ax: 1032, ay: 1190 }
  });
  await S.svgCiz("tabler/device-laptop.svg", {
    kutu: [393, 952, 300, 300], bas: 56, sure: 30, azami: 25, w: 4.2, sesAralik: 2, oge: sag
  });
  not("dizüstü çizimi", 56);
  const saatOge = S.oge({
    topla: { f0: TOPLA0, f1: TOPLA1, dx: -379.5, dy: -49.5, s: 0.43, ax: 884.5, ay: 764.5 }
  });
  await S.svgCiz("tabler/clock.svg", {
    kutu: [760, 640, 250, 250], bas: 36, sure: 26, azami: 25, w: 7, sesAralik: 2, oge: saatOge
  });
  not("saat çizimi", 36);
  parilti(1000, 660, { bas: 92, r: 28, periyot: 150, adet: 3 });

  // --- iki not satırı (Caveat 72 + not 64): saat-tir / çalış-ıyor-um
  // Parçalar art arda yazılır: her parça önceki bitince başlar (süre = hedef kare).
  const parca = (liste, x, y, bas) => {
    let cx = x, b = bas; const sonuc = [];
    for (const [s, renk, sure] of liste) {
      const z = elYazisi(s, { x: cx, y, boyut: 72, renk: renk || MUR, bas: b, sure });
      sonuc.push(z); cx = z.x1; b += sure;
    }
    return sonuc;
  };
  {   // 4,91: -tir sarı daire; -dir → süre
    // 4,20 `saat` (10 kare → 4,53) · 4,53 `-tir` (10 kare → 4,87); anlatım: «süre için -dir»
    // 4,19–5,43
    const yA = 505, [a1, a2] = parca([["saat", null, 10], ["-tir", null, 10]], 48, yA, fr(4.2));
    const d = daire((a2.x0 + a2.x1) / 2, yA - 26, a2.w / 2 + 14, 36,
      { bas: fr(4.91), sure: 16, egim: -0.04, w: 10 });
    olay(bitis(d), "tik", 0.5); not("-dir daire", d.bas);
    const o1 = ok([a2.x1 + 40, yA - 22], [a2.x1 + 150, yA - 22],
      { bas: fr(5.2), sure: 12, w: 9, uzun: 24, bukum: 0.08 });
    // 5,63–6,03 «süren» penceresi (eski belirme 5,67)
    elYazisi("süre", { x: a2.x1 + 170, y: yA, boyut: 72, renk: SARI, sozcukler: pen("süren", 1) });
    not("not -dir → süre", fr(5.2));
  }
  {   // 6,91: -ıyor sarı daire; -yor → iş sürüyor
    // 6,03 `çalış` (9 kare) · `-ıyor` (9) · `-um` (9) → 6,93 biter; -ıyor daire 6,91 başlar.
    // Etiket alt sınırı 0,3 sn (inceleme: 8/8/6 kare 0,27/0,27/0,20 sn idi; bitiş aynı kaldı)
    const yB = 600, [b1, b2, b3] = parca([["çalış", null, 9], ["-ıyor", null, 9], ["-um", null, 9]],
      48, yB, fr(6.03));
    const d = daire((b2.x0 + b2.x1) / 2, yB - 26, b2.w / 2 + 14, 36,
      { bas: fr(6.91), sure: 16, egim: 0.04, w: 10 });
    olay(bitis(d), "tik", 0.5); not("-yor daire", d.bas);
    const o2 = ok([b3.x1 + 30, yB - 22], [b3.x1 + 110, yB - 22],
      { bas: fr(7.2), sure: 12, w: 9, uzun: 24, bukum: 0.08 });
    // 7,67 anlatımsız etiket `iş sürüyor`: hedef 16 kare (0,53 sn) → 8,20
    elYazisi("iş sürüyor", { x: b3.x1 + 126, y: yB, boyut: 72, renk: SARI, bas: bitis(o2) + 2,
      sure: 16 });
    not("not -yor → iş sürüyor", fr(7.2));
  }
  {   // 7,5–: zaman çizgisi `2 saat önce → now`
    const ty = 890, b0 = fr(7.5);
    ciz([[450, ty], [740, ty - 2], [1032, ty]],
      { w: 4, renk: MUR, bas: b0, sure: 14, uc0: 8, uc1: 20, oge: sag });
    daire(470, ty, 11, 11, { bas: b0 + 12, sure: 8, tur: 1.1, w: 6, oge: sag });
    const dalga = Array.from({ length: 20 }, (_, i) =>
      [480 + i * 27, ty - 2 + Math.sin(i * 0.9) * 8]);
    ciz(dalga, {
      w: 13, renk: SARI, alfa: 0.55, bas: b0 + 14, sure: 22, uc0: 10, uc1: 14, amp: 0.4, oge: sag
    });
    daire(1010, ty, 11, 11, { bas: b0 + 34, sure: 8, tur: 1.1, w: 6, oge: sag });
    // 7,77 `2 saat önce` (16 kare → 8,30) · 8,70 `now` (14 kare → 9,17; sağ uç 1018);
    // anlatımsız etiketler
    elYazisi("2 saat önce", { x: 450, y: 978, boyut: 88, renk: MUR, bas: b0 + 8, sure: 16,
      oge: sag });
    elYazisi("now", { x: 1018 - eyGen("now", 88), y: 978, boyut: 88, renk: SARI, bas: b0 + 36,
      sure: 14, oge: sag });
    not("zaman çizgisi", b0);
  }

  // --- 8,10–10,66: I have been working / for two hours. (Fredoka 72, iki satır);
  // have been + -ing daire
  {
    const kel = ["I", "have", "been", "working", "for", "two", "hours."];
    const tl = [8.10, 8.36, 8.66, 8.98, 9.30, 9.52, 9.74];
    const e = cumle(kel.map((s, i) => ({ s, f: fr(tl[i]), satir: i < 4 ? 0 : 1 })),
      { x: 48, y: 1275, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: 82 });
    altCizgi(e, { tut: 40, w: 9 }); not("İngilizce cümle başı", e[0].bas);
    const hb = daire((e[1].x0 + e[2].x1) / 2, 1275 - 24, (e[2].x1 - e[1].x0) / 2 + 12, 44,
      { bas: fr(9.66), sure: 18, a0: -2.0, w: 10 });
    olay(bitis(hb), "tik", 0.5); not("have been daire", hb.bas);
    const w = e[3], font = "700 72px Fredoka", wk = genislik("work", font),
      wi = genislik("ing", font);
    const di = daire(w.x0 + wk + wi / 2, 1275 - 24, wi / 2 + 12, 42,
      { bas: fr(10.0), sure: 14, a0: -2.2, w: 10 });
    olay(bitis(di), "tik", 0.5); not("-ing daire", di.bas);
  }

  // --- 10,73–17,13: ajanda kartı (sağ üst): saat + "6 dakikada:" + 3 madde
  {
    kutu(430, 655, 602, 340, { bas: fr(10.73), sure: 30, w: 4.4 }); not("kart çizimi", fr(10.73));
    // 10,73–11,61 «Altı dakikada» (pencere: 10,73–11,01 · 11,05–11,61)
    elYazisi("6 dakikada:", { x: 570, y: 740, boyut: 72, renk: SARI, sozcukler: pen("Altı", 2) });
    not("6 dakikada", fr(11.05));
    parilti(520, 668, { bas: fr(12.2), r: 24, periyot: 170, adet: 3 });
    const m = [["form", 13.29, 825], ["time expressions", 14.17, 900], ["result clue", 15.61, 975]];
    for (const [s, t, y] of m) {
      yazi(s,
        { x: 505, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: MUR, bas: fr(t), sure: 8 });
      tik(468, y - 20, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

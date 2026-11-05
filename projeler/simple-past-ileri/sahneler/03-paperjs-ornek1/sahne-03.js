// Sahne 03 (SIMPLE PAST İLERİ) — Örnek 1, kök 1 (602 kare, t_bas 13,47; cümle 3). Yerel kare =
// round((t − 13,47) × 30).
// Kök: "Marie Curie won her second Nobel Prize in 1911, three years before the war began." (belirli
// zaman + düzensiz fiil).
import { sahneKur, RT,
  renkCoz } from "/projeler/simple-past-ileri/sahneler/03-paperjs-ornek1/kalem-paper.js";
import { yaziNoktalari } from "/projeler/simple-past-ileri/ortak/kalem-canvas.js";

export const KARE = 602, T_BAS = 13.47;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, parilti, olay, not, bitis,
    dinamik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;
  // geçiş karesi: çizimler bundan sonra başlar
  const GB = 12;
  const f0 = (t) => Math.max(GB, fr(t));
  // El yazısı (Caveat 700 tegaki, dalga 5b / K26): not ve etiketler kalemle yazılır. Ortaya hizada
  // genişlik tegaki verisinden ölçülür (yaziNoktalari.gen); sözcük pencereleri cümle 3
  // anlatımından.
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm, asc: EY.M.ascender,
    boy: boyut, x: 0, taban: 0 }).gen;
  const CS = S.sozcukler(3);                                  // cümle 3 sözcükleri (f / f1 kare)
  const pen = (ilk, adet) => { const i = CS.findIndex((w) => w.s === ilk);
    return CS.slice(i, i + adet).map((w) => ({ f0: w.f, f1: w.f1 })); };

  // --- 13,47–14,51: büyük el çizimi daire içinde 1
  const d1 = daire(200, 190, 66, 62, { bas: f0(13.47), sure: 22, a0: -2.6 }); olay(bitis(d1),
    "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 226, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700,
    bas: f0(13.85), sure: 10, olcek: true });

  // --- 14,68–19,92: İngilizce kök (Fredoka 56, 3 satır, sözcük zamanlı)
  const sz = S.sozcukler(3).slice(2, 17);                          // Marie … began.
  const satirNo = (i) => (i < 6 ? 0 : i < 11 ? 1 : 2);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 140, y: 310, boyut: 56, aile: "Fredoka", agirlik: 700, aralik: 78 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (Marie)", cz[0].bas);

  // won (15,56) ve began (19,60): sarı kutu; 1911 (17,24): sarı daire
  const sariKutu = (w, bas, ad) => {
    const k = kutu(w.x0 - 10, w.y - 46, w.w + 14, 66, { bas, sure: 14, w: 5, renk: SARI });
    not(ad, bas); olay(k.bit, "tik", 0.5);
  };
  sariKutu(cz[2], fr(15.56), "won kutusu");
  {
    const w = cz[8], d = daire((w.x0 + w.x1) / 2, w.y - 20, w.w / 2 + 14, 40, { bas: fr(17.24),
      sure: 22, a0: -2.6, egim: -0.03 });
    olay(bitis(d), "tik", 0.5); not("1911 dairesi", d.bas);
  }
  sariKutu(cz[14], fr(19.60), "began kutusu");

  // --- 14,7–16,6: sağ üst sahne. Oturan figür (sitting-2) + kitap + kalem
  const ogeF = S.oge({ nefes: { bas: fr(17.5), cx: 1350, cy: 550 } });
  await S.svgCiz("open-peeps/sitting-2.svg", { kutu: [1190, 185, 340, 370], bas: f0(14.7),
    sure: fr(15.9) - f0(14.7), azami: 60, yuz: 3,
    w: 3.2, oge: ogeF, sesAralik: 5 });
  not("figür çizimi başı", f0(14.7));
  await S.svgCiz("tabler/book.svg", { kutu: [1555, 270, 290, 280], bas: fr(15.9), sure: 22,
    azami: 12, w: 4.2, sesAralik: 2 });
  not("kitap çizimi başı", fr(15.9));
  await S.svgCiz("tabler/pencil.svg", { kutu: [1640, 140, 120, 120], bas: fr(16.45), sure: 14,
    azami: 8, w: 4, sesAralik: 2 });
  not("kalem çizimi başı", fr(16.45));
  parilti(1780, 170, { bas: fr(16.9), r: 20 });

  // --- 20,85–23,97: zaman çizgisi (y 640): 1911 ve war noktası, aralarında 3 years köprüsü; In
  // 1911 -> belirli zaman -> Simple Past
  {
    const yT = 630, x1911 = 330, xWar = 860;
    const tl = ciz([[140, yT + 2], [420, yT - 2], [760, yT + 1], [1100, yT - 1]], { w: 4.4,
      renk: IKI, alfa: 0.9, bas: fr(20.85), sure: 22, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[1072, yT - 17], [1102, yT - 1], [1072, yT + 14]], { w: 4.4, renk: IKI, alfa: 0.9,
      bas: bitis(tl) - 2, sure: 7, duz: true, uc0: 5, uc1: 5, ses: false });
    const nokta = (x, fn) => dinamik((f, g) => {
      if (f < fn) return;
      const a = Math.min(1, (f - fn) / 6);
      g.addChild(new P.Path.Circle({ center: [x, yT], radius: 13 * a, fillColor: renkCoz(SARI),
        insert: false }));
    });
    nokta(x1911, fr(21.0)); olay(fr(21.0), "tik", 0.5);
    yazi("In 1911", { x: x1911, y: yT + 70, hizala: "orta", boyut: 44, aile: "Fredoka",
      agirlik: 700, bas: fr(20.95), sure: 10 });
    not("In 1911 etiketi", fr(20.95));
    {
      const d = daire(x1911, yT + 56, 104, 40, { bas: fr(21.09), sure: 22, a0: -2.6, egim: -0.03 });
      olay(bitis(d), "tik", 0.5); not("In 1911 dairesi", d.bas);
    }
    nokta(xWar, fr(21.5)); olay(fr(21.5), "tik", 0.5);
    yazi("war", { x: xWar, y: yT + 70, hizala: "orta", boyut: 44, aile: "Fredoka", agirlik: 700,
      bas: fr(21.5), sure: 10 });
    // 3 years köprüsü (çizginin üstünde, sarı ayraç)
    ciz([[x1911, yT - 36], [x1911, yT - 52], [xWar, yT - 52], [xWar, yT - 36]], { w: 6,
      renk: SARI, alfa: 0.85, bas: fr(21.8), sure: 24, duz: true, uc0: 10, uc1: 14 });
    not("3 years köprüsü", fr(21.8));
    // 22,00 anlatımsız etiket `3 years`: hedef 14 kare (0,47 sn) → 22,47; orta x = (1911 + war) / 2
    elYazisi("3 years", { x: (x1911 + xWar) / 2 - eyGen("3 years", 56) / 2, y: yT - 74, boyut: 56,
      renk: IKI, bas: fr(22.0), sure: 14 });
    // 22,21–23,17 «belirli zaman,» (pencere: belirli 22,21–22,53 · zaman 22,61–23,17)
    elYazisi("belirli zaman", { x: 140, y: yT + 150, boyut: 56, renk: SARI,
      sozcukler: pen("belirli", 2),
      ses: true });
    not("belirli zaman", fr(22.21));
    const a = ok([470, yT + 140], [1170, yT + 78], { bas: fr(23.25), sure: 18, w: 6, uzun: 20,
      bukum: 0.05 });
    kutu(1200, 590, 590, 145, { bas: fr(23.5), sure: 24, w: 5, renk: KRE });
    not("Simple Past kutusu", fr(23.5));
    yazi("Simple Past", { x: 1495, y: 686, hizala: "orta", boyut: 76, aile: "Fredoka",
      agirlik: 700, bas: fr(23.65), sure: 12, olcek: true, ses: true });
    parilti(1780, 598, { bas: bitis(a) + 6, r: 24 });
  }

  // --- 25,05–26,69: iki satır Fredoka 72 (win → won, begin → began) + düzensiz
  {
    const F = { boyut: 68, aile: "Fredoka", agirlik: 700 }, y1 = 872, y2 = 960;
    const w1 = yazi("win", { ...F, x: 140, y: y1, bas: fr(25.05), sure: 8, olcek: true });
    ok([w1.x1 + 18, y1 - 24], [w1.x1 + 92, y1 - 24], { bas: fr(25.12), sure: 12, w: 6, uzun: 16,
      bukum: 0.05 });
    yazi("won", { ...F, x: w1.x1 + 112, y: y1, bas: fr(25.3), sure: 8, olcek: true, renk: SARI,
      ses: true }); not("win → won", fr(25.05));
    const w2 = yazi("begin", { ...F, x: 140, y: y2, bas: fr(25.65), sure: 8, olcek: true });
    ok([w2.x1 + 18, y2 - 24], [w2.x1 + 92, y2 - 24], { bas: fr(25.72), sure: 12, w: 6, uzun: 16,
      bukum: 0.05 });
    yazi("began", { ...F, x: w2.x1 + 112, y: y2, bas: fr(25.88), sure: 8, olcek: true, renk: SARI,
      ses: true }); not("begin → began", fr(25.65));
    ciz([[640, y1 - 50], [662, y1 - 28], [662, y1 + 10], [680, y1 + 36], [662, y1 + 60], [662,
      y2 - 12], [640, y2 + 8]],
      { w: 5.5, renk: IKI, alfa: 0.9, bas: fr(26.25), sure: 16, uc0: 8, uc1: 10 });
    // 26,37–27,25 «düzensiz.» (tek sözcük penceresi 0,88 sn)
    elYazisi("düzensiz", { x: 710, y: 930, boyut: 64, renk: SARI, sozcukler: pen("düzensiz.", 1),
      ses: true });
    not("düzensiz", fr(26.37));
  }

  // --- 27,40–32,20: tuzak: begin · began · begun; began sarı daire, begun kırmızı çarpı
  {
    const yR = 958, F = { boyut: 68, aile: "Fredoka", agirlik: 700 };
    // 27,40–28,28 «Tuzak:» (tek sözcük penceresi 0,88 sn)
    elYazisi("Tuzak:", { x: 1000, y: 860, boyut: 72, renk: KIR, sozcukler: pen("Tuzak:", 1),
      ses: true });
    not("Tuzak: (kırmızı)", fr(27.40));
    const b1 = yazi("begin", { ...F, x: 1000, y: yR, bas: fr(28.52), sure: 8, olcek: true,
      ses: true }); not("begin", fr(28.52));
    const n1 = yazi("·", { ...F, x: b1.x1 + 16, y: yR, bas: fr(29.04), sure: 4 });
    const b2 = yazi("began", { ...F, x: n1.x1 + 16, y: yR, bas: fr(29.04), sure: 8, olcek: true,
      ses: true }); not("began", fr(29.04));
    const n2 = yazi("·", { ...F, x: b2.x1 + 16, y: yR, bas: fr(29.92), sure: 4 });
    const b3 = yazi("begun", { ...F, x: n2.x1 + 16, y: yR, bas: fr(29.92), sure: 8, olcek: true,
      ses: true }); not("begun", fr(29.92));
    {
      const d = daire((b2.x0 + b2.x1) / 2, yR - 22, b2.w / 2 + 18, 44, { bas: fr(29.35), sure: 22,
        a0: -2.6, egim: -0.03 });
      olay(bitis(d), "tik", 0.5); not("began dairesi", d.bas);
    }
    const x0 = b3.x0 - 12, x1 = b3.x1 + 12, y0 = yR - 64, y1 = yR + 14;
    const c1 = ciz([[x0, y0], [(x0 + x1) / 2, (y0 + y1) / 2 - 2], [x1, y1]], { w: 8, renk: KIR,
      alfa: 0.9, bas: fr(31.32), sure: 10, uc0: 6, uc1: 8, amp: 0.6 });
    ciz([[x1, y0], [(x0 + x1) / 2 + 2, (y0 + y1) / 2], [x0, y1]], { w: 8, renk: KIR, alfa: 0.9,
      bas: bitis(c1) + 2, sure: 10, uc0: 6, uc1: 8, amp: 0.6 });
    olay(fr(31.32), "vurus", 0.8); not("begun çarpısı", fr(31.32));
    parilti(x1 + 24, y0 - 6, { bas: fr(31.9), r: 22 });
  }
  return S;
}

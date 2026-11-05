// Sahne 03 (SIMPLE PAST İLERİ, DİKEY 1080x1920) — Örnek 1 (602 kare, t_bas 13,47; cümle 3). Yerel kare = round((t − 13,47) × 30).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (kalem-paper.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–672) · ORTA bölge M (690–950: zaman çizgisi + Simple Past) · alt bölge B (960–1392):
// solda figür 430 px (20,5'te aşağı iner, hiç küçülmez), sağda sütun (kitap → rows → tuzak).
import { sahneKur, RT, renkCoz } from "/projeler/simple-past-ileri-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 602, T_BAS = 13.47;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, cumle, altCizgi, parilti, olay, not, bitis, dinamik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;
  const GB = 12;
  const f0 = (t) => Math.max(GB, fr(t));

  // --- 13,47: kart çerçevesi (el kutusu, 4 px) — içerik bandının üst parçası
  kutu(48, 372, 984, 300, { bas: f0(13.47), sure: 30, w: 4.2, renk: IKI }); not("kart çerçevesi", f0(13.47));

  // --- 14,68–19,92: İngilizce kök (Fredoka 64, 3 satır, sözcük zamanlı); satır başı 5 / 10
  const sz = S.sozcukler(3).slice(2, 17);                          // Marie … began.
  const satirNo = (i) => (i < 5 ? 0 : i < 10 ? 1 : 2);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 88, y: 452, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 78 });
  altCizgi(cz, { tut: 40, w: 8 }); not("cümle başı (Marie)", cz[0].bas);

  const sariKutu = (w, bas, ad) => {                               // sarı belirteç kutusu
    const k = kutu(w.x0 - 10, w.y - 52, w.w + 16, 74, { bas, sure: 14, w: 6, renk: SARI });
    not(ad, bas); olay(k.bit, "tik", 0.5);
  };
  sariKutu(cz[2], fr(15.56), "won kutusu");
  {
    const w = cz[8], d = daire((w.x0 + w.x1) / 2, w.y - 24, w.w / 2 + 16, 46, { bas: fr(17.24), sure: 22, a0: -2.6, egim: -0.03, w: 10 });
    olay(bitis(d), "tik", 0.5); not("1911 dairesi", d.bas);
  }
  sariKutu(cz[14], fr(19.60), "began kutusu");

  // --- 14,7–16,6: ORTA sahne: oturan figür (sitting-2, 430 px) + kitap + kalem. Figür 20,45–21,25'te alt bölgeye iner.
  const GF = S.oge({ topla: { f0: fr(20.45), f1: fr(21.25), ax: 0, ay: 0, olcek: 1, dy: 165 } });
  await S.svgCiz("open-peeps/sitting-2.svg", { kutu: [60, 790, 400, 430], bas: f0(14.7), sure: fr(15.9) - f0(14.7), azami: 60, yuz: 3,
    w: 4.6, oge: GF, sesAralik: 5 });
  not("figür çizimi başı", f0(14.7));
  // kitap + kalem: tek grup; 20,45'te figürün kucağına küçülür (hedef T), sütun rows için boşalır
  const k = 0.5, C = [740, 1040], T = [318, 1318], A = [(T[0] - k * C[0]) / (1 - k), (T[1] - k * C[1]) / (1 - k)];
  const GK = S.oge({ topla: { f0: fr(20.45), f1: fr(21.25), ax: A[0], ay: A[1], olcek: k, dy: 0 } });
  await S.svgCiz("tabler/book.svg", { kutu: [500, 830, 480, 420], bas: fr(15.9), sure: 24, azami: 12, w: 6.6, sesAralik: 2, oge: GK });
  not("kitap çizimi başı", fr(15.9));
  await S.svgCiz("tabler/pencil.svg", { kutu: [840, 700, 150, 150], bas: fr(16.5), sure: 14, azami: 8, w: 6.6, sesAralik: 2, oge: GK });
  not("kalem çizimi başı", fr(16.5));
  parilti(985, 760, { bas: fr(16.95), r: 26 });

  // --- 20,85–23,97: ORTA bölge M (690–950): zaman çizgisi (sol) + belirli zaman -> Simple Past (sağ)
  {
    const yT = 832, x1911 = 200, xWar = 540;
    const tl = ciz([[88, yT + 2], [260, yT - 2], [450, yT + 1], [660, yT - 1]], { w: 5, renk: IKI, alfa: 0.9, bas: fr(20.85), sure: 22, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[634, yT - 20], [664, yT - 1], [634, yT + 18]], { w: 5, renk: IKI, alfa: 0.9, bas: bitis(tl) - 2, sure: 7, duz: true, uc0: 5, uc1: 5, ses: false });
    const renkNokta = (x, fn) => dinamik((f, g) => {
      if (f < fn) return;
      const c = new P.Path.Circle({ center: [x, yT], radius: 15 * Math.min(1, (f - fn) / 6), insert: false });
      c.fillColor = renkCoz(SARI); g.addChild(c);
    });
    renkNokta(x1911, fr(21.0)); olay(fr(21.0), "tik", 0.5);
    yazi("In 1911", { x: x1911, y: yT + 84, hizala: "orta", boyut: 64, aile: "Fredoka", agirlik: 700, bas: fr(20.95), sure: 10 });
    not("In 1911 etiketi", fr(20.95));
    {
      const d = daire(x1911, yT + 62, 138, 48, { bas: fr(21.09), sure: 22, a0: -2.6, egim: -0.03, w: 10 });
      olay(bitis(d), "tik", 0.5); not("In 1911 dairesi", d.bas);
    }
    renkNokta(xWar, fr(21.5)); olay(fr(21.5), "tik", 0.5);
    yazi("war", { x: xWar, y: yT + 84, hizala: "orta", boyut: 64, aile: "Fredoka", agirlik: 700, bas: fr(21.5), sure: 10 });
    // 3 years köprüsü (çizginin üstünde, sarı ayraç)
    ciz([[x1911, yT - 40], [x1911, yT - 62], [xWar, yT - 62], [xWar, yT - 40]], { w: 9, renk: SARI, alfa: 0.85, bas: fr(21.8), sure: 24, duz: true, uc0: 10, uc1: 14 });
    not("3 years köprüsü", fr(21.8));
    yazi("3 years", { x: (x1911 + xWar) / 2, y: yT - 86, hizala: "orta", boyut: 64, aile: "Caveat", agirlik: 700, renk: KRE, bas: fr(22.0), sure: 10 });
    // sağ blok: belirli zaman (Caveat 64) -> Simple Past kutusu (iki satır)
    yazi("belirli zaman", { x: 700, y: 752, boyut: 64, aile: "Caveat", agirlik: 700, renk: SARI, bas: fr(22.21), sure: 20, ses: true });
    not("belirli zaman", fr(22.21));
    const a = ok([860, 774], [860, 806], { bas: fr(23.3), sure: 12, w: 8, uzun: 20, bukum: 0.06 });
    kutu(700, 820, 330, 130, { bas: fr(23.5), sure: 24, w: 5, renk: KRE });
    not("Simple Past kutusu", fr(23.5));
    yazi("Simple", { x: 865, y: 880, hizala: "orta", boyut: 64, aile: "Fredoka", agirlik: 700, bas: fr(23.65), sure: 10, olcek: true, ses: true });
    yazi("Past", { x: 865, y: 938, hizala: "orta", boyut: 64, aile: "Fredoka", agirlik: 700, bas: fr(23.97), sure: 10, olcek: true });
    parilti(1010, 836, { bas: bitis(a) + 6, r: 26 });
  }

  // --- 25,05–26,69: alt bölge sağ sütun: win → won, begin → began (Fredoka 80) + düzensiz
  {
    const F = { boyut: 80, aile: "Fredoka", agirlik: 700 }, y1 = 1040, y2 = 1138, X = 456;
    const w1 = yazi("win", { ...F, x: X, y: y1, bas: fr(25.05), sure: 8, olcek: true });
    ok([w1.x1 + 20, y1 - 28], [w1.x1 + 96, y1 - 28], { bas: fr(25.12), sure: 12, w: 8, uzun: 18, bukum: 0.05 });
    yazi("won", { ...F, x: w1.x1 + 116, y: y1, bas: fr(25.3), sure: 8, olcek: true, renk: SARI, ses: true }); not("win → won", fr(25.05));
    const w2 = yazi("begin", { ...F, x: X, y: y2, bas: fr(25.65), sure: 8, olcek: true });
    ok([w2.x1 + 20, y2 - 28], [w2.x1 + 96, y2 - 28], { bas: fr(25.72), sure: 12, w: 8, uzun: 18, bukum: 0.05 });
    yazi("began", { ...F, x: w2.x1 + 116, y: y2, bas: fr(25.88), sure: 8, olcek: true, renk: SARI, ses: true }); not("begin → began", fr(25.65));
    yazi("düzensiz", { x: X, y: 1218, boyut: 64, aile: "Caveat", agirlik: 700, renk: SARI, bas: fr(26.37), sure: 14, ses: true });
    not("düzensiz", fr(26.37));
  }

  // --- 27,40–32,20: tuzak: begin · began · begun; began sarı daire, begun kırmızı çarpı
  {
    const yR = 1366, F = { boyut: 64, aile: "Fredoka", agirlik: 700 }, X = 442;
    yazi("Tuzak:", { x: X, y: 1296, boyut: 72, aile: "Caveat", agirlik: 700, renk: KIR, bas: fr(27.40), sure: 14, ses: true });
    not("Tuzak: (kırmızı)", fr(27.40));
    const b1 = yazi("begin", { ...F, x: X, y: yR, bas: fr(28.52), sure: 8, olcek: true, ses: true }); not("begin", fr(28.52));
    const n1 = yazi("·", { ...F, x: b1.x1 + 6, y: yR, bas: fr(29.04), sure: 4 });
    const b2 = yazi("began", { ...F, x: n1.x1 + 6, y: yR, bas: fr(29.04), sure: 8, olcek: true, ses: true }); not("began", fr(29.04));
    const n2 = yazi("·", { ...F, x: b2.x1 + 6, y: yR, bas: fr(29.92), sure: 4 });
    const b3 = yazi("begun", { ...F, x: n2.x1 + 6, y: yR, bas: fr(29.92), sure: 8, olcek: true, ses: true }); not("begun", fr(29.92));
    {
      const d = daire((b2.x0 + b2.x1) / 2, yR - 22, b2.w / 2 + 14, 46, { bas: fr(29.35), sure: 22, a0: -2.6, egim: -0.03, w: 10 });
      olay(bitis(d), "tik", 0.5); not("began dairesi", d.bas);
    }
    const x0 = b3.x0 - 10, x1 = b3.x1 + 10, y0 = yR - 66, y1 = yR + 14;
    const c1 = ciz([[x0, y0], [(x0 + x1) / 2, (y0 + y1) / 2 - 2], [x1, y1]], { w: 10, renk: KIR, alfa: 0.9, bas: fr(31.32), sure: 10, uc0: 6, uc1: 8, amp: 0.6 });
    ciz([[x1, y0], [(x0 + x1) / 2 + 2, (y0 + y1) / 2], [x0, y1]], { w: 10, renk: KIR, alfa: 0.9, bas: bitis(c1) + 2, sure: 10, uc0: 6, uc1: 8, amp: 0.6 });
    olay(fr(31.32), "vurus", 0.8); not("begun çarpısı", fr(31.32));
    parilti(x1 + 6, y0 - 16, { bas: fr(31.9), r: 24 });
  }
  return S;
}

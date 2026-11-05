// Sahne 02 (ileri S1 Shorts) — Örnek: Paper.js, 1080x1920, 397 kare, t_bas 3,00; cümle 1 sonu + cümle 2.
// Yerel kare = round((t − 3,00) × 30). İlk 12 kare geçiş altında: sahne 01'in son hali hazır çizili
// (Biliyorum / I am knowing + kırmızı çarpı / diyemezsin. + figür + kitap). Dikey v2 bantları:
// içerik 352–1392, alt bölge (940–1392) figür + nesne, üst bölge (392–900) yazı, altyazı 1400–1536.
import { sahneKur, RT } from "/projeler/present-continuous-ileri-s1/sahneler/02-paperjs-ornek/kalem-paper.js";
import { yaziNoktalari } from "/projeler/present-continuous-ileri-s1/ortak/kalem-canvas.js";

export const KARE = 397, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Trap" });
  const { fr, ciz, daire, yazi, elYazisi, cumle, kutu, tik, parilti, olay, not, bitis,
    genislik, kis, oge } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil, KIRMIZI = RT.kirmizi;
  const sol = (f0, f1) => (f) => 1 - kis((f - f0) / (f1 - f0));     // oge: [f0, f1] arası söner
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  // El yazısı (Caveat 700 tegaki, dalga 5b / K26): notlar kalemle yazılır; sözcük ofseti ve
  // genişlik tegaki verisinden ölçülür, sözcük pencereleri anlatımın t0/t1 karelerinden gelir.
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm, asc: EY.M.ascender,
    boy: boyut, x: 0, taban: 0 }).gen;
  const pen = (ws) => ws.map((w, i) => ({ f0: w.f,
    f1: w.f1 - w.f < 6 && ws[i + 1] ? ws[i + 1].f : w.f1 }));
  // satır(sözcükler, pencereler, {x, y, boyut, renk, oge}) -> sözcük başına elYazisi sonucu
  const satir = (soz, pn, o) => soz.map((k, i) => elYazisi(k, { ...o,
    x: o.x + eyGen(soz.join(" "), o.boyut) - eyGen(soz.slice(i).join(" "), o.boyut),
    sozcukler: [pn[i]] }));
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, ...o });

  // ---------- Faz A (3,0–6,93): kanca cümlesi 4 satır + figür + kitap; 6,5–6,85 söner ----------
  const A0 = fr(6.5), A1 = fr(6.85);
  const gA = oge({ alfa: sol(A0, A1) }), fSon = [A0, A1];
  const SOL = 72;
  // satır 1–3 sahne 01'den hazır (f -30): Biliyorum / I am knowing / diyemezsin.
  cumle([{ s: "Biliyorum", f: -30 }], { x: SOL, y: 500, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  const en1 = cumle([{ s: "I", f: -30 }, { s: "am", f: -30 }, { s: "knowing", f: -30 }],
    { x: SOL, y: 650, boyut: 88, aile: "Fredoka", agirlik: 700, son: fSon });
  cumle([{ s: "diyemezsin.", f: -30 }], { x: SOL, y: 800, boyut: 88, aile: "Caveat", agirlik: 700, son: fSon });
  {   // kırmızı çarpı (sahne 01 ile aynı yol; hazır çizili)
    const x0 = SOL - 14, x1 = en1[2].x1 + 14, ust = 650 - 72, alt = 650 + 26;
    const o = { w: 12, renk: KIRMIZI, alfa: 0.92, bas: -400, sure: 2, duz: true, uc0: 6, uc1: 6, amp: 0.3,
      ses: false, oge: gA };
    ciz([[x0, ust], [x1, alt]], o); ciz([[x1, ust], [x0, alt]], o);
  }
  // satır 4: YDT tam burada tuzak kurar. (4,14–5,90, sözcük zamanlı) + tuzak sarı daire
  // 4,14–6,46 sn (kare 34–133): sözcük penceresi; tam (0,16 sn) kurar'a kadar uzar;
  // sağ uç ölçülür
  const tz = satir(s1.slice(5).map((w) => w.s), pen(s1.slice(5)),
    { x: SOL, y: 915, boyut: 80, renk: RT.murekkep, oge: gA });
  not("YDT satırı başı", tz[0].bas);
  {
    const g = tz[3], d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 8, 44,
      { bas: g.bit - 6, sure: 16, oge: gA });
    olay(bitis(d), "tik", 0.5); not("tuzak daire", d.bas);
  }
  // figür (standing-3) + kitap + zemin çizgisi: sahne 01 ile aynı kutular, hazır çizili
  await S.svgCiz("open-peeps/standing-3.svg", { kutu: [150, 950, 213 * 0.628, 701 * 0.628], bas: -400, sure: 100,
    azami: 60, yuz: 3, w: 4.4, oge: gA, sessiz: true });
  await S.svgCiz("tabler/book.svg", { kutu: [408, 870, 576, 576], bas: -400, sure: 100, azami: 25, w: 4,
    oge: gA, sessiz: true });
  ciz([[96, 1388], [560, 1386], [1000, 1388]], { w: 4, bas: -400, sure: 2, ses: false, duz: true, oge: gA });

  // ---------- Faz B (6,93–13,7): kart + TR + figür (sitting-4) + telefon ----------
  const B0 = fr(13.5), B1 = fr(13.78);
  const gB = oge({ alfa: sol(B0, B1) }), bSon = [B0, B1];
  const KY = 392, SH = 88, B1Y = KY + 40 + 58;                  // kart üstü 392, ilk taban 490, ikinci 578
  kutu(48, KY, 984, 246, { bas: fr(6.93) - 6, sure: 30, w: 4, renk: IKI, oge: gB });
  not("kart kutusu", fr(6.93) - 6);
  const en = s2.slice(0, 10).map((k, i) => ({ s: k.s, f: k.f, satir: i < 5 ? 0 : 1 }));
  const e = cumle(en, { x: 88, y: B1Y, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: SH, son: bSon });
  not("EN cümle başı", e[0].bas);
  {   // know sarı daire (7,25) · am not telling oval (8,81–9,29)
    const g = e[1], d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 6, 42, { bas: g.bas + 3, sure: 16, oge: gB });
    olay(bitis(d), "tik", 0.5); not("know daire", d.bas);
    const a = e[6], t = e[8], cx = (a.x0 + t.x1) / 2;
    const d2 = daire(cx, a.y - 26, (t.x1 - a.x0) / 2 + 14, 46, { bas: a.bas, sure: 24, a0: -2.6, oge: gB });
    olay(bitis(d2), "tik", 0.5); not("am not telling oval", d2.bas);
  }
  // TR çeviri (10,70–13,74 sn) Caveat 80 mürekkep: satır 1 Cevabı biliyorum ama /
  // satır 2 kimseye söylemiyorum. Sözcük penceresi; söylemiyorum. 13,25'te biter
  // (13,5 sönme başlamadan önce)
  const ts = s2.slice(10, 15), tp = pen(ts);
  tp[4].f1 = Math.min(tp[4].f1, fr(13.25));
  const TRO = { x: 72, boyut: 80, renk: RT.murekkep, oge: gB };
  const tr = [...satir(ts.slice(0, 3).map((k) => k.s), tp.slice(0, 3), { ...TRO, y: 735 }),
    ...satir(ts.slice(3).map((k) => k.s), tp.slice(3), { ...TRO, y: 825 })];
  not("TR çeviri başı", tr[0].bas);
  altCiz(tr[4], tr[4].bit - 6, { oge: gB }); not("söylemiyorum altı çizgi", tr[4].bit - 6);
  // figür + telefon (7,4–9,6): alt bölge 930–1390
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [100, 930, 340, 460], bas: fr(7.4), sure: fr(8.9) - fr(7.4),
    azami: 60, yuz: 3, w: 4.4, sesAralik: 5 });
  not("figür çizimi başı", fr(7.4));
  await S.svgCiz("tabler/phone.svg", { kutu: [445, 855, 600, 600], bas: fr(8.9), sure: 22, azami: 25, w: 4,
    sesAralik: 1 });
  not("telefon çizimi başı", fr(8.9));
  ciz([[96, 1388], [560, 1386], [1000, 1388]], { w: 4, bas: fr(7.3), sure: 20, duz: true });
  parilti(930, 960, { bas: fr(9.7), r: 28, periyot: 150, adet: 3 });

  // ---------- Faz C (13,78–15,82): Bilmek durumdur, → I know + -ing çizilip kalemle çizilir ----------
  // 13,78–14,94 sn (kare 323–358): Bilmek durumdur, sözcük penceresi
  const lab = satir(s2.slice(15, 17).map((k) => k.s), pen(s2.slice(15, 17)),
    { x: SOL, y: 480, boyut: 84, renk: RT.murekkep });
  not("Bilmek durumdur", lab[0].bas);
  {
    const F = "700 170px Fredoka", gI = genislik("I ", F), gK = genislik("know", F), gN = genislik("-ing", F);
    const x0 = (1080 - (gI + gK + 30 + gN)) / 2, y = 700, f0 = fr(14.2);
    const a = yazi("I", { x: x0, y, boyut: 170, aile: "Fredoka", agirlik: 700, bas: f0, sure: 8, olcek: true, ses: "tik" });
    const k = yazi("know", { x: x0 + gI, y, boyut: 170, aile: "Fredoka", agirlik: 700, bas: f0 + 4, sure: 10, olcek: true });
    not("I know", f0);
    const d = daire((a.x0 + k.x1) / 2, y - 62, (k.x1 - a.x0) / 2 + 10, 104, { bas: fr(14.62), sure: 18, a0: -2.2 });
    olay(bitis(d), "tik", 0.5); not("I know daire", d.bas);
    const ing = yazi("-ing", { x: k.x1 + 30, y, boyut: 170, aile: "Fredoka", agirlik: 700, renk: KIRMIZI,
      bas: fr(15.06), sure: 8, olcek: true, ses: "tik" });
    not("-ing yazılır", fr(15.06));
    const st = ciz([[ing.x0 - 16, y - 46], [(ing.x0 + ing.x1) / 2, y - 50], [ing.x1 + 16, y - 54]],
      { w: 15, renk: KIRMIZI, alfa: 0.92, bas: fr(15.2), sure: 8, uc0: 6, uc1: 8, amp: 0.4 });
    not("-ing çizilir (kalem)", st.bas);
    // 15,06–15,90 sn: -ing (0,12 sn) almaz.'a kadar uzar; almaz. 15,60'ta biter
    // (son 12 kare durgun)
    const np = pen(s2.slice(17)); np[1].f1 = Math.min(np[1].f1, fr(15.6));
    const nt = satir(s2.slice(17).map((w) => w.s), np,
      { x: (1080 - eyGen("-ing almaz.", 92)) / 2, y: 850, boyut: 92, renk: RT.murekkep });
    not("-ing almaz.", nt[0].bas);
    altCiz(nt[1], nt[1].bit - 6, { w: 10 });
  }
  void tik;
  return S;
}

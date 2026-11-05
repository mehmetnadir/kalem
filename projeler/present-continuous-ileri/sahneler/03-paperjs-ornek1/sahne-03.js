// Sahne 03 (İLERİ) — Örnek 1 (442 kare, t_bas 15,25; cümle 3). Zamanlar BRIEF §4; yerel kare =
// round((t − 15,25) × 30).
// Kök: "Please be quiet! The baby is sleeping ... while I am talking on the phone." (bebek +
// telefon, while).
import { sahneKur, RT,
  renkCoz } from "/projeler/present-continuous-ileri/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 442, T_BAS = 15.25;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, parilti, olay, not, bitis,
    dinamik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  // geçiş karesi: çizimler bundan sonra başlar
  const GB = 12;
  const f0 = (t) => Math.max(GB, fr(t));

  // --- 15,80–16,68: büyük el çizimi daire içinde 1
  const d1 = daire(200, 190, 66, 62, { bas: f0(15.80), sure: 22, a0: -2.6 }); olay(bitis(d1),
    "tik", 0.5);
  not("daire 1 çizimi", d1.bas);
  yazi("1", { x: 200, y: 226, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700,
    bas: f0(16.15), sure: 10, olcek: true });

  // --- 16,93–22,05: İngilizce kök (Fredoka 56, 3 satır, sözcük zamanlı)
  const sz = S.sozcukler(3).slice(2, 20);                          // Please … phone.
  const satirNo = (i) => (i < 5 ? 0 : i < 11 ? 1 : 2);
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 140, y: 300, boyut: 56, aile: "Fredoka", agirlik: 700, aralik: 76 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (Please)", cz[0].bas);

  // is sleeping (18,69–19,01) ve am talking (20,40–20,49): sarı daire; while (20,13): sarı kutu
  const cevre = (a, b, bas, egim, ad) => {
    const x0 = cz[a].x0, x1 = cz[b].x1, y = cz[a].y - 20;
    const d = daire((x0 + x1) / 2, y, (x1 - x0) / 2 + 4, 40, { bas, sure: 22, a0: -2.6, egim });
    olay(bitis(d), "tik", 0.5); not(ad, d.bas); return d;
  };
  cevre(5, 6, fr(18.75), -0.03, "is sleeping daire");
  cevre(13, 14, fr(20.40), -0.025, "am talking daire");
  {
    const w = cz[11], k = kutu(w.x0 - 10, w.y - 46, w.w + 13, 66, { bas: fr(20.13), sure: 14,
      w: 5, renk: SARI });
    not("while kutusu", fr(20.13)); olay(k.bit, "tik", 0.5);
  }

  // --- 16,9–20,0: sağ sahne. Duvar ortada; solda uyuyan bebek (sitting-6), sağda telefonda konuşan
  // figür (sitting-4)
  const wall = ciz([[1500, 190], [1496, 330], [1503, 470], [1498, 620]], { w: 5, renk: IKI,
    alfa: 0.9, bas: f0(16.9), sure: 22, uc0: 12, uc1: 30 });
  not("duvar çizgisi", wall.bas);
  const ogeBebek = S.oge({ nefes: { bas: fr(20.5), cx: 1320, cy: 600 } });
  await S.svgCiz("open-peeps/sitting-6.svg", { kutu: [1190, 340, 270, 290], bas: f0(17.3),
    sure: fr(18.5) - f0(17.3), azami: 60, yuz: 3,
    w: 3.2, oge: ogeBebek, sesAralik: 5 });
  not("uyuyan figür çizimi başı", f0(17.3));
  const ogeKonusan = S.oge({ nefes: { bas: fr(20.6), cx: 1690, cy: 640 } });
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [1540, 250, 300, 400], bas: f0(17.6),
    sure: fr(19.2) - f0(17.6), azami: 60, yuz: 3,
    w: 3.2, oge: ogeKonusan, sesAralik: 5 });
  not("konuşan figür çizimi başı", f0(17.6));
  await S.svgCiz("tabler/phone.svg", { kutu: [1560, 150, 120, 120], bas: fr(19.3), sure: 14,
    azami: 6, w: 4, sesAralik: 1 });
  not("telefon çizimi başı", fr(19.3));
  // z z z (duvarın ardında uyuyan bebeğin üstünde)
  [[1260, 318, 34], [1318, 268, 44], [1386, 210, 54]].forEach(([x, y, b], i) => {
    ciz([[x, y], [x + b, y], [x, y + b], [x + b, y + b]], { duz: true, w: 4.4, renk: IKI,
      alfa: 0.9, bas: fr(18.7) + i * 7, sure: 9, uc0: 4, uc1: 6, amp: 0.5 });
  });
  not("z z z", fr(18.7));
  parilti(1640, 190, { bas: fr(19.9), r: 22 });

  // --- 22,30–25,14: Türkçe çeviri (el yazısı 48 ikincil, y 620), sözcük zamanlı
  // 22,30–25,10 sn «Bebek uyuyor, ben telefonda konuşuyorum.»: her sözcük kendi penceresinde;
  // "ben" penceresi (0,12 sn) sonraki sözcüğün başına (23,78) dek uzatıldı
  const tr = S.sozcukler(3).slice(20, 25);
  let tx = 140; const tz = [];
  tr.forEach((k, i) => {
    const f1 = i === 2 ? tr[3].f : k.f1;
    const q = elYazisi(k.s, { x: tx, y: 620, boyut: 48, renk: IKI, sozcukler: [{ f0: k.f, f1 }] });
    tx = q.x1 + 0.3 * 48; tz.push(q);
  });
  not("Türkçe çeviri", tz[0].bas);

  // --- 25,14–27,66: zaman çizgisi, nabız atan now noktası, iki dalgalı sarı bant
  {
    const yT = 812, xN = 660;
    const tl = ciz([[140, yT + 2], [420, yT - 2], [760, yT + 1], [1090, yT - 1]], { w: 4.4,
      renk: IKI, alfa: 0.9, bas: fr(25.14), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", tl.bas);
    ciz([[1062, yT - 17], [1092, yT - 1], [1062, yT + 14]], { w: 4.4, renk: IKI, alfa: 0.9,
      bas: bitis(tl) - 2, sure: 7, duz: true, uc0: 5, uc1: 5, ses: false });
    const fn = fr(25.9);
    dinamik((f, g) => {
      if (f < fn) return;
      const t = f - fn, s = 1 + 0.16 * Math.sin(2 * Math.PI * t / 36), u = (t % 45) / 45,
        a = Math.min(1, t / 5);
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 11 * s * a,
        fillColor: renkCoz(SARI), insert: false }));
      g.addChild(new P.Path.Circle({ center: [xN, yT], radius: 13 + 30 * (1 - Math.pow(1 - u, 3)),
        strokeColor: renkCoz(SARI), strokeWidth: 4, opacity: 0.75 * (1 - u) * a, insert: false }));
    });
    olay(fn, "tik", 0.5); not("now noktası (nabız)", fn);
    yazi("now", { x: xN, y: yT + 50, hizala: "orta", boyut: 28, aile: "Lexend", agirlik: 500,
      renk: IKI, bas: fn + 2, sure: 8 });
    const bant = (y0, bas, ad, etiket) => {
      const dalga = Array.from({ length: 40 }, (_, i) => { const u = i / 39, x = 400 + u * 520;
        return [x, y0 + 9 * Math.sin(u * 8 * Math.PI) * (0.55 + 0.45 * Math.sin(u * Math.PI))]; });
      const w = ciz(dalga, { w: 7.5, renk: SARI, alfa: 0.85, bas, sure: 26, duz: true, uc0: 12,
        uc1: 24, amp: 0.5 }); not(ad, w.bas);
      // bant başından 8 kare sonra, hedef 0,53 sn (bant: 26 kare; sonraki bant ≥ 18 kare sonra)
      elYazisi(etiket, { x: 140, y: y0 + 12, boyut: 44, renk: SARI, bas: bas + 8, sure: 16 });
    };
    bant(700, fr(25.95), "is sleeping bandı", "is sleeping");
    bant(756, fr(26.55), "am talking bandı", "am talking");
    const it = S.sozcukler(3).slice(25, 31).filter((k) => ["İki", "iş", "de",
      "sürüyor."].includes(k.s));
    // 25,14–27,42 sn «İki iş de sürüyor.» ("şu anda" yazılmaz): 2–3 harflik pencereler (0,12–0,16
    // sn)
    // sonraki sözcüğün başına dek uzatıldı: İki → 25,34 · iş → 25,58 · de → 25,74
    let ix = 760; const iz = [];
    const uz = [25.34, 25.58, 25.74];
    it.forEach((k, i) => {
      const f1 = i < 3 ? fr(uz[i]) : k.f1;
      const q = elYazisi(k.s, { x: ix, y: 905, boyut: 48, renk: SARI, sozcukler: [{ f0: k.f,
        f1 }] });
      ix = q.x1 + 0.3 * 48; iz.push(q);
    });
    not("iki iş de sürüyor", iz[0].bas);
  }

  // --- 27,66–29,58: While kutusu -> ok -> NOW ; formül kartı be + V-ing -> is sleep-ing / am
  // talk-ing
  {
    const w = cz[11], ax = (w.x0 + w.x1) / 2 - 8;
    olay(fr(27.66), "vurus", 0.8);
    parilti(w.x1 + 22, w.y - 60, { bas: fr(27.66), r: 20 });
    const a = ok([ax, w.y + 30], [ax + 20, w.y + 78], { bas: fr(27.72), sure: 12, w: 6.5,
      uzun: 18, bukum: 0.12 });
    const n = yazi("NOW", { x: ax + 34, y: w.y + 112, boyut: 52, aile: "Fredoka", agirlik: 700,
      renk: SARI, bas: bitis(a) + 4, sure: 10, olcek: true, ses: true });
    not("While -> ok -> NOW", fr(27.72));
    const kx = 1190, ky = 675;
    kutu(kx, ky, 640, 305, { bas: fr(28.05), sure: 24 }); not("formül kartı kutusu", fr(28.05));
    const y1 = ky + 90, y2 = ky + 185, y3 = ky + 280, F = { boyut: 60, aile: "Fredoka",
      agirlik: 700 };
    yazi("be", { ...F, x: kx + 60, y: y1, bas: fr(28.42), sure: 10, olcek: true,
      ses: true }); not("be", fr(28.42));
    yazi("+", { ...F, x: kx + 170, y: y1, bas: fr(28.52), sure: 8, olcek: true });
    const v = yazi("V", { ...F, x: kx + 250, y: y1, bas: fr(28.62), sure: 8, olcek: true });
    yazi("-ing", { ...F, x: v.x1 + 4, y: y1, bas: fr(28.74), sure: 10, olcek: true, renk: SARI,
      ses: true }); not("be + V-ing", fr(28.74));
    const s1 = yazi("is sleep", { ...F, x: kx + 60, y: y2, bas: fr(28.95), sure: 10, olcek: true });
    yazi("-ing", { ...F, x: s1.x1 + 4, y: y2, bas: fr(29.02), sure: 10, olcek: true, renk: SARI,
      ses: true }); not("is sleep-ing", fr(28.95));
    const s2 = yazi("am talk", { ...F, x: kx + 60, y: y3, bas: fr(29.18), sure: 10, olcek: true });
    yazi("-ing", { ...F, x: s2.x1 + 4, y: y3, bas: fr(29.25), sure: 10, olcek: true, renk: SARI,
      ses: true }); not("am talk-ing", fr(29.18));
    parilti(kx + 600, ky + 40, { bas: fr(29.3), r: 22 });
  }
  return S;
}

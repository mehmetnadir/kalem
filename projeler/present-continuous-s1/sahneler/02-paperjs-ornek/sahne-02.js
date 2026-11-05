// Sahne 02 — Örnek (DİKEY 1080x1920, 478 kare, t_bas 3,00; cümle 1 devamı + cümle 2). 05.11 telefon ölçeği düzeltmesi.
// Sahne 01'in son hali (HUD + iki Caveat 80 satırı + figür/ev eskizi) kare 0'da hazır; zamanlar küresel sn,
// fr(t) = round((t - 3,00) x 30). Bantlar: HUD 0-320, içerik 352-1392, altyazı 1400-1536 (kalem-paper.js çizer).
import { sahneKur, RT } from "/projeler/present-continuous-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 478, T_BAS = 3.0;
const CIP = "BU AKŞAM = I AM GOING";

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: CIP });
  const { fr, ciz, daire, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu, genislik,
    oge, kis } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const solma = (t0, t1) => (f) => 1 - kis((f - fr(t0)) / (fr(t1) - fr(t0)));   // 1 -> 0
  // ust: cümle 1 + not (8,0'a kadar); eskiz: figür + ev + hilal (14,5'te solar)
  const ust = oge({ alfa: solma(7.85, 8.15) });
  const eskizAlfa = solma(14.45, 14.85);
  const figOge = oge({ alfa: eskizAlfa, nefes: { bas: fr(9.0), cx: 250, cy: 1140 } });
  const evOge = oge({ alfa: eskizAlfa });
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, ...o });

  // --- cümle 1 (sahne 01'in son hali, hazır): Caveat 80, x 72, y 440 / 530
  // 01'den devralındı, kare 0'da hazır (0. karede görünür): Caveat yazi kalır (pilot kararı)
  const c80 = { boyut: 80, aile: "Caveat", agirlik: 700, oge: ust };
  cumle(s1.slice(0, 3).map((w) => ({ s: w.s, f: -30 })), { x: 72, y: 440, ...c80 });
  const en1 = cumle(s1.slice(3, 7).map((w) => ({ s: w.s, f: -30 })), { x: 72, y: 530, ...c80 });
  altCiz(en1[2], fr(3.0) + 14, { oge: ust }); not("going altı çizgi (cümle 1)", fr(3.0) + 14);

  // --- eskiz (sahne 01'den hazır): figür 480 px + ev (kutu 460) + zemin çizgisi, y 900-1380
  await S.svgCiz("open-peeps/standing-3.svg", { kutu: [177, 900, 146, 480], bas: -200, sure: 2, azami: 60,
    yuz: 3, w: 4.4, oge: figOge, sessiz: true });
  await S.svgCiz("tabler/home.svg", { kutu: [522.5, 977.4, 460, 460], bas: -200, sure: 2, azami: 25, w: 4.0,
    oge: evOge, sessiz: true });
  ciz([[96, 1384], [560, 1382], [1000, 1384]], { w: 4, renk: IKI, alfa: 0.75, bas: -200, sure: 2, uc0: 10,
    uc1: 30, oge: evOge, ses: false });

  // --- 4,38–7,74: "İki dilde de şimdiki zaman, ama gelecek demek." (Caveat 64 mürekkep, 2 satır)
  // el yazısı: her sözcük kendi penceresinde (4,38–7,74 sn); sözcük arası 0,3 x boyut
  // (motor aralığı);
  // satır 1 = İki dilde de şimdiki zaman,  satır 2 = ama gelecek demek.  "ama" penceresi 4 kare
  // (6,49–6,62 sn) → sonraki sözcüğün başına dek (6,70 sn) uzatıldı
  {
    const w = s1.slice(7), t = [];                                   // 8 sözcük
    let tx = 72;
    w.forEach((k, i) => {
      if (i === 0 || i === 5) tx = 72;
      const f1 = k.f1 - k.f < 6 && w[i + 1] ? w[i + 1].f : k.f1;
      const q = elYazisi(k.s, { x: tx, y: 640 + (i < 5 ? 0 : 82), boyut: 64, renk: MUR, oge: ust,
        sozcukler: [{ f0: k.f, f1 }] });
      tx = q.x1 + 0.3 * 64; t.push(q);
    });
    not("TR not başı", t[0].bas);
    altCiz(t[3], t[3].bit - 6, { w: 8, oge: ust });                  // şimdiki
    not("şimdiki altı çizgi", t[3].bit - 6);
    const d = daire((t[6].x0 + t[6].x1) / 2, t[6].y - 18, t[6].w / 2 + 10, 34,
      { bas: t[6].bit - 6, sure: 20, egim: -0.05, oge: ust });
    olay(bitis(d), "tik", 0.5); not("gelecek daire", d.bas);
  }

  // --- 8,9–12,0: hilal (akşam), eskizin sağ üstü (ev çatısının üstü)
  {
    const C = [965, 975], R = 40, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 8) pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 8) pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    const h = ciz(pts, { w: 4.2, alfa: 0.92, bas: fr(9.9), sure: 24, uc0: 10, uc1: 16, amp: 0.6, oge: evOge });
    not("hilal çizimi", h.bas);
    parilti(C[0] + 36, C[1] - 40, { bas: bitis(h) + 2, r: 20, periyot: 140, adet: 3 });
  }

  // --- 8,0–12,6: kart (tam genişlik): I'm going to my uncle's tonight. / Bu akşam amcamlara gidiyorum.
  kutu(48, 372, 984, 332, { bas: fr(8.0) - 8, sure: 36, renk: IKI, w: 4.2 }); not("kart kutusu", fr(8.0) - 8);
  {
    const en = s2.slice(0, 6);
    const e = cumle(en.map((k, i) => ({ s: k.s, f: k.f, satir: i < 5 ? 0 : 1 })),
      { x: 88, y: 478, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: 88 });
    not("EN cümle başı", e[0].bas);
    const g = e[1], d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 8, 36, { bas: g.bas + 6, sure: 20, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("going daire", d.bas);
    // 10,22–12,62 sn ("Bu akşam amcamlara gidiyorum."): her sözcük kendi penceresinde;
    // "Bu" penceresi 2 kare (10,22–10,30 sn) → "akşam" başına dek (10,38 sn) uzatıldı
    const tr = s2.slice(6, 10), t = [];
    let tx = 88;
    tr.forEach((k, i) => {
      const f1 = k.f1 - k.f < 6 && tr[i + 1] ? tr[i + 1].f : k.f1;
      const q = elYazisi(k.s, { x: tx, y: 664, boyut: 64, renk: MUR,
        sozcukler: [{ f0: k.f, f1 }] });
      tx = q.x1 + 0.3 * 64; t.push(q);
    });
    altCiz(t[3], t[3].bit - 6, { w: 8 }); not("gidiyorum altı çizgi", t[3].bit - 6);
  }

  // --- 12,77–14,6: formül: go + -ing  (Fiil artı -ing), Fredoka 110
  {
    const bz = 110, f = "700 " + bz + "px Fredoka", gw = genislik("go", f), pw = genislik("+", f);
    const iw = genislik("-ing", f), bos = 44;
    const top = gw + pw + iw + 2 * bos, x0 = (1080 - top) / 2, y = 850;
    kutu(48, 735, 984, 150, { bas: fr(12.77) - 10, sure: 34, renk: IKI, w: 4.2 }); not("formül kutusu", fr(12.77) - 10);
    const a = yazi("go", { x: x0, y, boyut: bz, aile: "Fredoka", agirlik: 700, bas: fr(12.77), sure: 8, olcek: true, ses: "tik" });
    yazi("+", { x: a.x1 + bos, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(13.33), sure: 6,
      olcek: true, ses: "tik" });
    const b = yazi("-ing", { x: a.x1 + 2 * bos + pw, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: fr(13.73), sure: 8, olcek: true });
    olay(b.bas, "vurus", 0.8); not("go", a.bas); not("-ing (sarı)", b.bas);
    altCiz(b, b.bas + 8, { w: 11 }); parilti(b.x1 + 20, y - 100, { bas: b.bas + 10, r: 24, periyot: 130, adet: 2 });
  }

  // --- 14,61–18,0: önüne am · is · are (üç kutu, sırayla tik); eskiz solmuş, bant alt yarısı kutularla dolar
  {
    // etiket 14,61 sn'de belirir (kare 348); anlatımla pencere uyuşmaz → sure 16 kare (0,53 sn),
    // bitiş kare 364 < kutu am (15,41 sn)
    elYazisi("önüne gelir:", { x: 72, y: 1050, boyut: 72, renk: MUR, bas: fr(14.61), sure: 16 });
    not("önüne gelir", fr(14.61));
    const pil = [["am", 15.41], ["is", 16.05], ["are", 17.09]];
    pil.forEach(([s, t], i) => {
      const w = 296, h = 200, x = 48 + i * (w + 48), y = 1110;
      kutu(x, y, w, h, { bas: fr(t) - 14, sure: 20, renk: IKI, w: 4.2 });
      yazi(s, { x: x + w / 2, y: y + 128, boyut: 96, aile: "Fredoka", agirlik: 700, hizala: "orta", bas: fr(t),
        sure: 8, olcek: true });
      tik(x + w - 52, y + 56, { bas: fr(t) + 8 }); not("kutu " + s, fr(t));
    });
  }
  return S;
}

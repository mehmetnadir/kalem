// Sahne 02 — Örnek (DİKEY 1080x1920, 403 kare, t_bas 3,00; cümle 1 devamı + cümle 2). Telefon ölçeği (BRIEF-DIKEY §3).
// Sahne 01'in son hali (HUD + Caveat 80 satırı "Gider, İngilizcede goes" + figür/otobüs eskizi) kare 0'da hazır;
// zamanlar küresel sn, fr(t) = round((t - 3,00) x 30). Bantlar: HUD 0-320, içerik 352-1392, altyazı 1400-1536.
import { sahneKur, RT } from "/projeler/simple-present-temel-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 403, T_BAS = 3.0;
const CIP = "GİDER = GOES";

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: CIP });
  const { fr, ciz, daire, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu, genislik,
    oge, kis } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const solma = (t0, t1) => (f) => 1 - kis((f - fr(t0)) / (fr(t1) - fr(t0)));   // 1 -> 0
  // ust: cümle 1 + büyük "fiil + s" (6,35'e kadar); eskiz: figür + otobüs + okul (10,2'de solar)
  const ust = oge({ alfa: solma(6.1, 6.35) });
  const eskizAlfa = solma(9.85, 10.2);
  const figOge = oge({ alfa: eskizAlfa, nefes: { bas: fr(4.0), cx: 320, cy: 1140 } });
  const evOge = oge({ alfa: eskizAlfa });
  const okulOge = oge({ alfa: eskizAlfa });
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, tur: "isaret", ad: o.ad || "altCiz", ...o });

  // --- cümle 1 (sahne 01'in son hali + devamı): Caveat 80, x 72, y 440 / 530
  // satır 1: Gider, İngilizcede goes olur:   satır 2: fiilin sonuna s gelir.
  const c80 = { x: 72, y: 440, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 90, oge: ust };
  // sözcük 0–2 (Gider, İngilizcede goes): 01'den devralınan son görünüm, kare 0'da hazır
  // (01 dokunulmaz); Caveat yazi kalır
  const e1 = cumle(s1.slice(0, 3).map((w) => ({ s: w.s, f: -30, satir: 0 })), c80);
  altCiz(e1[2], fr(3.0) + 6, { oge: ust }); not("goes altı çizgi (cümle 1)", fr(3.0) + 6);
  {
    // sözcük 3–7 (3,32–5,88 sn, kare 10–86): her sözcük kendi konuşma penceresinde;
    // "olur:" satır 1'de goes'un sağında (x1 = 72 + 744 = 816 px),
    // satır 2 y 530 (x1 = 72 + 548 = 620 px); sözcük arası 0,3 × boyut (motor aralığı)
    const gap = 0.3 * c80.boyut, q = [];
    let tx = e1[2].x1 + gap;
    s1.slice(3).forEach((w, i) => {
      const sat = i < 1 ? 0 : 1; if (i === 1) tx = c80.x;
      const k = elYazisi(w.s, { x: tx, y: c80.y + sat * c80.aralik, boyut: c80.boyut, renk: MUR,
        oge: ust, sozcukler: [{ f0: w.f, f1: w.f1 }] });
      tx = k.x1 + gap; q.push(k);
    });
    const s = q[3], d = daire((s.x0 + s.x1) / 2, s.y - 22, Math.max(34, s.w / 2 + 18), 36,
      { bas: s.bit - 4, sure: 20, egim: -0.05, oge: ust });
    olay(bitis(d), "tik", 0.5); not("s daire (cümle 1)", d.bas);
  }

  // --- eskiz (sahne 01'den hazır): figür 480 px + otobüs (kutu 460) + zemin çizgisi, y 900-1384
  await S.svgCiz("open-peeps/standing-2.svg", { kutu: [250, 900, 146, 480], bas: -200, sure: 2, azami: 60,
    yuz: 3, w: 4.4, oge: figOge, sessiz: true });
  await S.svgCiz("tabler/bus.svg", { kutu: [520, 1000, 460, 460], bas: -200, sure: 2, azami: 25, w: 4.0,
    oge: evOge, sessiz: true });
  ciz([[96, 1384], [560, 1382], [1000, 1384]], { w: 4, renk: IKI, alfa: 0.75, bas: -200, sure: 2, uc0: 10,
    uc1: 30, oge: evOge, ses: false });

  // --- 4,08–6,1: büyük "fiil + s" (Fredoka 150, y 800) cümle 1'in altında, "s" sarı
  {
    const bz = 150, f = "700 " + bz + "px Fredoka", gw = genislik("fiil", f), pw = genislik("+", f);
    const sw = genislik("s", f), bos = 48, top = gw + pw + sw + 2 * bos, x0 = (1080 - top) / 2, y = 800;
    const a = yazi("fiil", { x: x0, y, boyut: bz, aile: "Fredoka", agirlik: 700, bas: s1[4].f, sure: 8,
      olcek: true, ses: "tik", oge: ust });
    yazi("+", { x: a.x1 + bos, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(4.75), sure: 6,
      olcek: true, ses: "tik", oge: ust });
    const b = yazi("s", { x: a.x1 + 2 * bos + pw, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: s1[6].f, sure: 8, olcek: true, oge: ust });
    olay(b.bas, "vurus", 0.8); not("fiil", a.bas); not("s (sarı)", b.bas);
    parilti(b.x1 + 24, y - 110, { bas: b.bas + 6, r: 24, periyot: 130, adet: 1, oge: ust });
  }

  // --- 7,2: okul (eskizin sağ üstü); 7,95 otobüste parıltı
  await S.svgCiz("tabler/school.svg", { kutu: [600, 760, 380, 380], bas: fr(7.2), sure: 24,
    azami: 4, w: 4.0, oge: okulOge });
  not("okul çizimi", fr(7.2));
  parilti(930, 1110, { bas: fr(7.95), r: 22, periyot: 130, adet: 1, oge: evOge });

  // --- 6,35–10,4: kart (tam genişlik): My brother goes to school by bus. / Kardeşim okula otobüsle gider.
  kutu(48, 372, 984, 332, { bas: fr(6.35) - 8, sure: 36, renk: IKI, w: 4.2 }); not("kart kutusu", fr(6.35) - 8);
  {
    const en = s2.slice(0, 7);
    const e = cumle(en.map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 })),
      { x: 88, y: 478, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: 88 });
    not("EN cümle başı", e[0].bas);
    const g = e[2], d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 8, 36, { bas: g.bas + 6, sure: 20, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("goes daire", d.bas);
    // 8,76–11,24 sn (kare 173–247; "Kardeşim okula otobüsle gider."): her sözcük kendi
    // penceresinde, tek satır x 88, y 664 (x1 = 88 + 664 = 752 px)
    const t = [];
    let tx = 88;
    s2.slice(7, 11).forEach((k) => {
      const q = elYazisi(k.s, { x: tx, y: 664, boyut: 64, renk: MUR,
        sozcukler: [{ f0: k.f, f1: k.f1 }] });
      tx = q.x1 + 0.3 * 64; t.push(q);
    });
    altCiz(t[3], t[3].bit - 6, { w: 8 }); not("gider altı çizgi", t[3].bit - 6);
  }

  // --- 10,39–11,6: formül: go + es  (Fiil artı es), Fredoka 120
  {
    const bz = 120, f = "700 " + bz + "px Fredoka", gw = genislik("go", f), pw = genislik("+", f);
    const iw = genislik("es", f), bos = 48;
    const top = gw + pw + iw + 2 * bos, x0 = (1080 - top) / 2, y = 858;
    kutu(48, 735, 984, 150, { bas: fr(10.39) - 6, sure: 34, renk: IKI, w: 4.2 }); not("formül kutusu", fr(10.39) - 6);
    const a = yazi("go", { x: x0, y, boyut: bz, aile: "Fredoka", agirlik: 700, bas: fr(10.39), sure: 8, olcek: true,
      ses: "tik" });
    yazi("+", { x: a.x1 + bos, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(10.75), sure: 6,
      olcek: true, ses: "tik" });
    const b = yazi("es", { x: a.x1 + 2 * bos + pw, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: fr(11.05), sure: 8, olcek: true });
    olay(b.bas, "vurus", 0.8); not("go", a.bas); not("es (sarı)", b.bas);
    altCiz(b, b.bas + 8, { w: 11 }); parilti(b.x1 + 20, y - 110, { bas: b.bas + 10, r: 24, periyot: 130, adet: 1 });
  }

  // --- 11,39–15,6: Özne: he · she · it (üç kutu, sırayla tik); altında "fiile + s"
  {
    // 11,39–12,03 sn (kare 252–271; "Özne"), "he" 273'te başlar; x1 = 72 + 130 = 202 px
    const oz = s2[11];
    elYazisi("Özne:", { x: 72, y: 1030, boyut: 72, renk: MUR,
      sozcukler: [{ f0: oz.f, f1: oz.f1 }] });
    not("Özne", oz.f);
    const pil = [["he", 12.11], ["she", 12.75], ["it", 13.75]];
    pil.forEach(([k, t], i) => {
      const w = 296, h = 160, x = 48 + i * (w + 48), y = 1070;
      kutu(x, y, w, h, { bas: fr(t) - 14, sure: 20, renk: IKI, w: 4.2 });
      yazi(k, { x: x + w / 2, y: y + 110, boyut: 96, aile: "Fredoka", agirlik: 700, hizala: "orta", bas: fr(t),
        sure: 8, olcek: true });
      tik(x + w - 52, y + 50, { bas: fr(t) + 8 }); not("kutu " + k, fr(t));
    });
    const bz = 84, f = "700 " + bz + "px Fredoka", fw = genislik("fiile", f), pw = genislik("+", f);
    const sw = genislik("s", f), bos = 40, top = fw + pw + sw + 2 * bos, x0 = (1080 - top) / 2, y = 1350;
    const a = yazi("fiile", { x: x0, y, boyut: bz, aile: "Fredoka", agirlik: 700, bas: fr(14.67), sure: 8,
      olcek: true, ses: "tik" });
    yazi("+", { x: a.x1 + bos, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(15.0), sure: 6,
      olcek: true, ses: "tik" });
    const b = yazi("s", { x: a.x1 + 2 * bos + pw, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: fr(15.23), sure: 8, olcek: true });
    olay(b.bas, "vurus", 0.8); not("fiile", a.bas); not("s (sarı)", b.bas);
    altCiz(b, b.bas + 8, { w: 9 }); parilti(b.x1 + 20, y - 90, { bas: b.bas + 10, r: 22, periyot: 130, adet: 1 });
  }
  return S;
}

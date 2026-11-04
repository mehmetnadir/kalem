// Sahne 02 — Örnek (DİKEY 1080x1920, 395 kare, t_bas 3,00; cümle 1 devamı + cümle 2). Telefon ölçeği (BRIEF-DIKEY §3).
// Sahne 01'in son hali (HUD + Caveat 80 iki satır "Anahtarımı kaybettim, / kapıda kaldım." + figür/ev eskizi)
// kare 0'da hazır; zamanlar küresel sn, fr(t) = round((t - 3,00) x 30). Bantlar: HUD 0-320, içerik 352-1392,
// altyazı 1400-1536.
import { sahneKur, RT } from "/projeler/present-perfect-temel-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 395, T_BAS = 3.0;
const CIP = "I HAVE LOST";

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: CIP });
  const { fr, ciz, daire, yazi, cumle, tik, parilti, olay, not, bitis, kutu, oge, kis } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const solma = (t0, t1) => (f) => 1 - kis((f - fr(t0)) / (fr(t1) - fr(t0)));   // 1 -> 0
  // ust: cümle 1 (iki parça); 7,28-7,50'de solar. eskiz: figür + ev + anahtar, sahne boyunca kalır
  const ust = oge({ alfa: solma(7.28, 7.5) });
  const figOge = oge({ nefes: { bas: fr(4.0), cx: 437, cy: 1150 } });
  const evOge = oge({});
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, ...o });

  // --- cümle 1 parça 1 (sahne 01'in son hali): Caveat 80, x 72, y 440 / 530
  const c80 = { x: 72, y: 440, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 90, oge: ust };
  cumle(s1.slice(0, 4).map((w, i) => ({ s: w.s, f: -30, satir: i < 2 ? 0 : 1 })), c80);

  // --- cümle 1 parça 2 (3,63-7,15): Caveat 64, x 72, y 650 / 726; "şimdi" sarı daire
  {
    const p2 = s1.slice(4);
    const e = cumle(p2.map((w, i) => ({ s: w.s, f: w.f, satir: i < 4 ? 0 : 1 })),
      { x: 72, y: 650, boyut: 64, aile: "Caveat", agirlik: 700, aralik: 76, oge: ust });
    altCiz(e[1], e[1].bas + 4, { oge: ust, w: 8 }); not("geçmiş altı çizgi", e[1].bas + 4);
    const s = e[6], d = daire((s.x0 + s.x1) / 2, s.y - 20, s.w / 2 + 16, 32,
      { bas: s.bas + 3, sure: 20, egim: -0.05, oge: ust });
    olay(bitis(d), "tik", 0.5); not("şimdi daire", d.bas);
    parilti(s.x1 + 26, s.y - 60, { bas: s.bas + 8, r: 22, periyot: 130, adet: 1, oge: ust });
  }

  // --- eskiz (sahne 01'den hazır): figür 470 px + ev (kutu 460) + zemin çizgisi, y 910-1384
  await S.svgCiz("open-peeps/standing-4.svg", { kutu: [330, 910, 210, 470], bas: -200, sure: 2, azami: 60,
    yuz: 3, w: 4.4, oge: figOge, sessiz: true });
  await S.svgCiz("tabler/home.svg", { kutu: [580, 982, 460, 460], bas: -200, sure: 2, azami: 25, w: 4.0,
    oge: evOge, sessiz: true });
  ciz([[96, 1384], [560, 1382], [1000, 1384]], { w: 4, renk: IKI, alfa: 0.75, bas: -200, sure: 2, uc0: 10,
    uc1: 30, oge: evOge, ses: false });

  // --- 7,50-: kart (tam genişlik): I have lost my keys. / Anahtarlarımı kaybettim, hâlâ bulamadım.
  kutu(48, 372, 984, 330, { bas: fr(7.5), sure: 36, renk: IKI, w: 4.2 }); not("kart kutusu", fr(7.5));
  {
    const en = s2.slice(0, 5);
    const e = cumle(en.map((k) => ({ s: k.s, f: k.f })),
      { x: 88, y: 478, boyut: 72, aile: "Fredoka", agirlik: 700 });
    not("EN cümle başı", e[0].bas);
    [e[1], e[2]].forEach((g, i) => {          // have (8,02) ve lost (8,18) sarı daire
      const d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 5, 38, { bas: g.bas + 3, sure: 18, a0: -2.0 + i });
      olay(bitis(d), "tik", 0.5); not(g.str + " daire", d.bas);
    });
    const tr = s2.slice(5, 9);
    const t = cumle(tr.map((k, i) => ({ s: k.s, f: k.f, satir: i < 2 ? 0 : 1 })),
      { x: 88, y: 590, boyut: 64, aile: "Caveat", agirlik: 700, renk: MUR, aralik: 76 });
    altCiz(t[3], t[3].bas + 4, { w: 8 }); not("bulamadım altı çizgi", t[3].bas + 4);
  }

  // --- 8,94: anahtar işareti (halka + gövde + iki diş) eskizin solunda; 11,71: "?"
  {
    const b = fr(8.94), W = { renk: SARI, alfa: 0.92, sessiz: true };
    const hk = daire(120, 1270, 34, 34, { bas: b, sure: 16, a0: -1.2, oge: evOge });
    ciz([[154, 1270], [292, 1272]], { w: 8, renk: SARI, bas: b + 14, sure: 10, uc0: 8, uc1: 8, oge: evOge });
    ciz([[240, 1272], [240, 1316]], { w: 8, renk: SARI, bas: b + 24, sure: 7, uc0: 4, uc1: 4, oge: evOge });
    ciz([[274, 1272], [274, 1302]], { w: 8, renk: SARI, bas: b + 30, sure: 6, uc0: 4, uc1: 4, oge: evOge });
    not("anahtar işareti", b); parilti(292, 1240, { bas: b + 36, r: 22, periyot: 130, adet: 1, oge: evOge });
    yazi("?", { x: 150, y: 1190, boyut: 120, aile: "Fredoka", agirlik: 700, renk: SARI, bas: fr(11.71), sure: 8,
      olcek: true, ses: "tik", oge: evOge });
    not("soru işareti", fr(11.71));
  }

  // --- 13,06-15,78: formül have + V3 (Fredoka 112) kutuda; V3 sarı; not: lost = lose'un 3. hâli
  {
    const bz = 112, f = "700 " + bz + "px Fredoka", gw = S.genislik("have", f), pw = S.genislik("+", f);
    const vw = S.genislik("V3", f), bos = 48, top = gw + pw + vw + 2 * bos, x0 = (1080 - top) / 2, y = 836;
    kutu(48, 726, 984, 140, { bas: fr(13.06) - 6, sure: 34, renk: IKI, w: 4.2 }); not("formül kutusu", fr(13.06) - 6);
    const a = yazi("have", { x: x0, y, boyut: bz, aile: "Fredoka", agirlik: 700, bas: fr(13.06), sure: 8,
      olcek: true, ses: "tik" });
    yazi("+", { x: a.x1 + bos, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(13.86), sure: 6,
      olcek: true, ses: "tik" });
    const b = yazi("V3", { x: a.x1 + 2 * bos + pw, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: fr(14.82), sure: 8, olcek: true });
    olay(b.bas, "vurus", 0.8); not("have", a.bas); not("V3 (sarı)", b.bas);
    altCiz(b, b.bas + 8, { w: 11 }); parilti(b.x1 + 20, y - 100, { bas: b.bas + 10, r: 24, periyot: 130, adet: 1 });
    const n = yazi("lost = lose'un 3. hâli", { x: 1020, y: 985, boyut: 64, aile: "Caveat", agirlik: 700,
      renk: MUR, hizala: "sag", bas: fr(15.22), sure: 14 });
    not("lost notu", n.bas);
  }
  return S;
}

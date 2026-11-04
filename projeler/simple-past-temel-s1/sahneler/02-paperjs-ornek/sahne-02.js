// Sahne 02 — Örnek (DİKEY 1080x1920, 381 kare, t_bas 3,00; cümle 1 devamı + cümle 2).
// Sahne 01'in son hali (HUD + Caveat 80 cümle + figür/ev eskizi) kare 0'da hazır; zamanlar küresel sn,
// fr(t) = round((t - 3,00) x 30). Bantlar: HUD 0-320, içerik 352-1392, altyazı 1400-1536.
// 3,0-7,9: cümle + iki Caveat 72 satır + ok formülü + eskiz (950-1384).
// 8,0-15,3: kart (372-722), figür + televizyon (760-1190), formül kutusu (1215-1385).
import { sahneKur, RT } from "/projeler/simple-past-temel-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 381, T_BAS = 3.0;
const CIP = "-Dİ = -ED";

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: CIP });
  const { fr, ciz, daire, yazi, cumle, tik, parilti, olay, not, bitis, kutu, genislik, oge, kis, ok } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const solma = (t0, t1) => (f) => 1 - kis((f - fr(t0)) / (fr(t1) - fr(t0)));   // 1 -> 0
  const ust = oge({ alfa: solma(7.85, 8.15) });
  const eskizAlfa = solma(7.9, 8.25);
  const evOge = oge({ alfa: eskizAlfa });
  const figOge = oge({ alfa: eskizAlfa });
  const tvFig = oge({ nefes: { bas: fr(10.0), cx: 226, cy: 975 } });
  const tvOge = oge({});
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, ...o });
  // geçiş altındaki ilk 12 kare durgun: yazı en erken 12. karede başlar
  const gec = (w) => ({ s: w.s, f: Math.max(12, w.f) });

  // --- cümle 1 (sahne 01'in son hali, hazır): Caveat 80, x 72, y 440
  cumle(s1.slice(0, 4).map((w) => ({ s: w.s, f: -30 })),
    { x: 72, y: 440, boyut: 80, aile: "Caveat", agirlik: 700, oge: ust });

  // --- eskiz (sahne 01'den hazır): figür 430 px + ev (kutu 440) + zemin çizgisi, y 950-1384
  await S.svgCiz("open-peeps/standing-3.svg", { kutu: [230, 950, 130.65, 430], bas: -200, sure: 2,
    azami: 60, yuz: 3, w: 4.4, oge: figOge, sessiz: true });
  await S.svgCiz("tabler/home.svg", { kutu: [480, 999, 440, 440], bas: -200, sure: 2, azami: 25,
    w: 4.0, oge: evOge, sessiz: true });
  ciz([[96, 1384], [560, 1382], [1000, 1384]], { w: 4, renk: IKI, alfa: 0.75, bas: -200, sure: 2,
    uc0: 10, uc1: 30, oge: evOge, ses: false });

  // --- 3,4-5,4: "Türkçede biten işe -di ekleriz." (Caveat 72, y 580), -di sarı kutu 4,35
  {
    const e = cumle(s1.slice(4, 9).map(gec), { x: 72, y: 580, boyut: 72, aile: "Caveat",
      agirlik: 700, renk: MUR, oge: ust });
    not("TR satırı başı", e[0].bas);
    const d = e[3];
    kutu(d.x0 - 7, 580 - 62, d.w + 14, 88, { bas: d.bas + 4, sure: 22, renk: SARI, w: 7, oge: ust });
    not("-di sarı kutu", d.bas + 4);
  }
  // --- 5,6-7,6: "İngilizce de -ed ekler." (y 700), -ed sarı kutu 6,59
  {
    const e = cumle(s1.slice(9, 13).map(gec), { x: 72, y: 700, boyut: 72, aile: "Caveat",
      agirlik: 700, renk: MUR, oge: ust });
    not("EN satırı başı", e[0].bas);
    const d = e[2];
    kutu(d.x0 - 7, 700 - 62, d.w + 14, 88, { bas: d.bas + 4, sure: 22, renk: SARI, w: 7, oge: ust });
    not("-ed sarı kutu", d.bas + 4);
  }
  // --- 6,95-7,8: ok formülü  -di <-> -ed  (Fredoka 130, y 860)
  {
    const a = yazi("-di", { x: 290, y: 860, boyut: 130, aile: "Fredoka", agirlik: 700, hizala: "orta",
      bas: fr(6.9), sure: 8, olcek: true, ses: "tik", oge: ust });
    const b = yazi("-ed", { x: 790, y: 860, boyut: 130, aile: "Fredoka", agirlik: 700, hizala: "orta",
      renk: SARI, bas: fr(7.0), sure: 8, olcek: true, ses: "tik", oge: ust });
    const o = ok([a.x1 + 40, 818], [b.x0 - 40, 818], { bas: fr(7.12), sure: 14, cift: true, w: 8, oge: ust });
    not("ok -di <-> -ed", o.bas);
  }

  // --- 8,0-12,0: kart (tam genişlik): I watched a movie last night. / Dün gece film izledim.
  kutu(48, 372, 984, 350, { bas: fr(8.0) - 8, sure: 36, renk: IKI, w: 4.2 }); not("kart kutusu", fr(8.0) - 8);
  let en;
  {
    en = cumle(s2.slice(0, 6).map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 })),
      { x: 88, y: 478, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: 88 });
    not("EN cümle başı", en[0].bas);
    const g = en[1], d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 8, 36, { bas: g.bas + 6, sure: 20, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("watched daire", d.bas);
    const t = cumle(s2.slice(6, 10).map((k) => ({ s: k.s, f: k.f })),
      { x: 88, y: 672, boyut: 72, aile: "Caveat", agirlik: 700, renk: MUR });
    altCiz(t[3], t[3].bas + 4); not("izledim altı çizgi", t[3].bas + 4);
  }

  // --- 8,3-: oturan figür (430 px) + televizyon (kutu 520), y 760-1190
  await S.svgCiz("open-peeps/sitting-6.svg", { kutu: [90, 760, 272, 430], bas: fr(8.3), sure: 36,
    azami: 60, yuz: 3, w: 4.4, oge: tvFig });
  await S.svgCiz("tabler/device-tv.svg", { kutu: [470, 757, 520, 520], bas: fr(8.3) + 32, sure: 30,
    azami: 20, w: 4.0, oge: tvOge });
  // hilal (gece), televizyonun sağ üstü, "night." 9,30
  {
    const C = [985, 850], R = 42, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 8) pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 8) pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    const h = ciz(pts, { w: 4.2, alfa: 0.92, bas: fr(9.35), sure: 24, uc0: 10, uc1: 16, amp: 0.6, oge: tvOge });
    not("hilal çizimi", h.bas);
    parilti(C[0] - 30, C[1] - 60, { bas: bitis(h) + 2, r: 20, periyot: 140, adet: 3 });
  }

  // --- 11,5-13,0: formül kutusu  watch + -ed  (Fredoka 120, y 1335)
  {
    const bz = 120, f = "700 " + bz + "px Fredoka", gw = genislik("watch", f), pw = genislik("+", f);
    const iw = genislik("-ed", f), bos = 44, top = gw + pw + iw + 2 * bos, x0 = (1080 - top) / 2, y = 1335;
    kutu(48, 1215, 984, 170, { bas: fr(11.5) - 10, sure: 30, renk: IKI, w: 4.2 }); not("formül kutusu", fr(11.5) - 10);
    const a = yazi("watch", { x: x0, y, boyut: bz, aile: "Fredoka", agirlik: 700, bas: fr(11.54), sure: 8,
      olcek: true, ses: "tik" });
    yazi("+", { x: a.x1 + bos, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: IKI, bas: fr(11.85),
      sure: 6, olcek: true, ses: "tik" });
    const b = yazi("-ed", { x: a.x1 + 2 * bos + pw, y, boyut: bz, aile: "Fredoka", agirlik: 700, renk: SARI,
      bas: fr(12.02), sure: 8, olcek: true });
    olay(b.bas, "vurus", 0.8); not("watch", a.bas); not("-ed (sarı)", b.bas);
    altCiz(b, b.bas + 8, { w: 11 }); parilti(b.x1 + 20, y - 110, { bas: b.bas + 10, r: 24, periyot: 130, adet: 2 });
  }

  // --- 13,86-14,8: kartta "last night" sarı belirteç
  {
    const a = en[4], b = en[5], y = a.y;
    const c = ciz([[a.x0 - 4, y + 14], [b.x1 + 4, y + 8]], { w: 10, renk: DOLGU, alfa: 0.9, bas: fr(13.86),
      sure: 24, uc0: 8, uc1: 12, amp: 1.0 });
    not("last night altı çizgi", c.bas);
    parilti(b.x1 + 36, y - 70, { bas: fr(14.38), r: 22, periyot: 0, adet: 1 });
  }
  return S;
}

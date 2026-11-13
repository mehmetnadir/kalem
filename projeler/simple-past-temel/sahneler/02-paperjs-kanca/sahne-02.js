// Sahne 02 — Kanca (366 kare, t_bas 3,00; cümle 2 = 3,39–14,25). Yerel kare = round((t − 3,00) × 30).
// Cümle 1 (Dün akşam amcamlara gittim.) sahne 01'de söylendi; yazı sahne başında hazır belirir (kare 0–9).
import { sahneKur, RT } from "/projeler/simple-past-temel/sahneler/02-paperjs-kanca/kalem-paper.js";

// Kart süresi (12.11, g-29): paket zaman.json son t_son'dan; sabit 6 dakika iddiası yanlıştı.
// Göreli yol: sahneler/<sahne>/ → paket kökü (yayında da aynı). Okunamazsa etiket boş kalır.
const SURE_METNI = await fetch(new URL("../../zaman.json", location.href))
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error("HTTP " + r.status))))
  .then((z) => {
    const t = z.sahneler[z.sahneler.length - 1].t_son;
    return t < 60 ? `${Math.round(t)} sec` : `${Math.round(t / 30) / 2} min`;
  })
  .catch((e) => { console.warn("zaman.json süre okunamadı:", e); return ""; });

export const KARE = 366, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0 });
  const { fr, ciz, daire, ok, yazi, elYazisi, cumle, altCizgi, tik, parilti, olay, not, bitis, kutu,
    genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12;                                                    // geçiş karesi: çizimler bundan sonra

  // --- cümle 1 (Caveat 64, x 140, y 300): sahne başında hazır, 0–0,4 sn'de belirir
  const c1 = cumle(["Dün", "akşam", "amcamlara", "gittim."].map((s, i) => ({ s, f: i * 3 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 başı (Dün)", c1[0].bas); not("gittim.", c1[3].bas);

  // --- sağ eskiz: ev + ona yürüyen figür + hilal
  await S.svgCiz("tabler/home.svg", { kutu: [1330, 190, 260, 260], bas: GB, sure: 26, azami: 25, w: 4, sesAralik: 2 });
  const figOge = S.oge({ kay: { f0: GB, f1: fr(7.2), dx: 70 }, nefes: { bas: fr(7.3), cx: 1190, cy: 450 } });
  await S.svgCiz("open-peeps/standing-2.svg", { kutu: [1090, 120, 190, 330], bas: GB, sure: 42, azami: 60, yuz: 3, w: 3.2, oge: figOge, sesAralik: 5 });
  not("ev çizimi başı", GB); not("figür çizimi başı", GB); not("figür yürüme biter", fr(7.2));
  ciz([[1040, 456], [1220, 452], [1420, 457], [1650, 453]], { w: 3, renk: IKI, alfa: 0.75, bas: 36, sure: 30, uc0: 10, uc1: 30 });
  {   // hilal: dış yay + iç yay tek darbe (el elipsi)
    const C = [1730, 240], R = 56, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 6) pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 6) pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    const h = ciz(pts, { w: 4, alfa: 0.92, bas: fr(4.2), sure: 30, uc0: 12, uc1: 20, amp: 0.7 }); not("hilal çizimi başı", h.bas);
    parilti(C[0] + 40, C[1] - 52, { bas: bitis(h) + 2, r: 24, periyot: 150, adet: 3 });
  }

  // --- 3,39–5,87: gittim sarı daire; -di sarı kutu (4,83); ok → biten iş; ok → takvim + dün
  // El yazısı (K26, 05.11): Caveat notlar kalemle yazılır; "-di" konuşma penceresinde
  // (4,83–5,07 sn; kaynak cümle 2: "Türkçede biten işe -di ekleriz.").
  const sz2 = S.sozcukler(2);
  const pen = (ad) => { const w = sz2.find((q) => q.s === ad); return { f0: w.f, f1: w.f1 }; };
  {
    const g = c1[3], d = daire((g.x0 + g.x1) / 2 + 3, g.y - 24, g.w / 2 + 6, 36, { bas: fr(3.39), sure: 24, egim: -0.04 });
    olay(bitis(d), "tik", 0.5); not("gittim daire", d.bas);
    const y1 = 392, a = elYazisi("-di", { x: 150, y: y1, boyut: 56, renk: RT.murekkep,
      sozcukler: [pen("-di")], ses: true });
    kutu(a.x0 - 14, y1 - 46, a.w + 28, 66, { bas: fr(4.83) + 6, sure: 14, w: 5, renk: SARI }); not("-di sarı kutu", fr(4.83));
    const o1 = ok([a.x1 + 28, y1 - 14], [a.x1 + 108, y1 - 14], { bas: fr(4.83) + 20, sure: 10, w: 5, uzun: 16, bukum: 0.08 });
    const b = elYazisi("biten iş", { x: a.x1 + 124, y: y1, boyut: 48, renk: IKI, bas: bitis(o1) + 2,
      sure: 14 }); not("biten iş", b.bas);                         // etiket, kare 87–101
    const o2 = ok([b.x1 + 26, y1 - 12], [b.x1 + 108, y1 - 6], { bas: fr(5.45), sure: 10, w: 5, uzun: 18, bukum: 0.1 });
    await S.svgCiz("tabler/calendar.svg", { kutu: [b.x1 + 124, y1 - 62, 84, 84], bas: bitis(o2), sure: 20, azami: 25, w: 3.4, sesAralik: 3 });
    elYazisi("dün", { x: b.x1 + 226, y: y1, boyut: 48, renk: SARI, bas: bitis(o2) + 16, sure: 12,
      ses: true });
    not("takvim + dün", bitis(o2));
  }

  // --- 6,02–8,10: I visited my uncle last night. (Fredoka 56, y 520); -ed sarı daire; -di ⇄ -ed oku
  {
    const tl = [6.02, 6.30, 6.62, 6.78, 7.10, 7.44], kel = ["I", "visited", "my", "uncle", "last", "night."];
    const e = cumle(kel.map((s, i) => ({ s, f: fr(tl[i]) })), { x: 140, y: 520, boyut: 56, aile: "Fredoka", agirlik: 700 });
    altCizgi(e, { tut: 40 }); not("İngilizce cümle başı", e[0].bas);
    const v = e[1], font = "700 56px Fredoka", wv = genislik("visit", font), we = genislik("ed", font);
    const d = daire(v.x0 + wv + we / 2, v.y - 20, we / 2 + 7, 32, { bas: fr(6.90) - 6, sure: 18, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("-ed daire", d.bas);
    const y = 630, a = elYazisi("-di", { x: 140, y, boyut: 52, renk: IKI, bas: fr(7.14),
      sure: 12 });
    const ar = ok([a.x1 + 22, y - 16], [a.x1 + 132, y - 16], { bas: fr(7.14) + 5, sure: 18, w: 6.5, cift: true, uzun: 20, bukum: 0.05 });
    elYazisi("-ed", { x: a.x1 + 156, y, boyut: 52, renk: SARI, bas: bitis(ar) + 4, sure: 12,
      ses: true }); not("ok -di ⇄ -ed", ar.bas);
  }

  // --- 8,25–14,25: el kutusu, saat + süre etiketi (derste 8,45), 3 madde
  {
    kutu(1060, 690, 760, 280, { bas: fr(8.25) - 4, sure: 36 }); not("kutu çizimi", fr(8.25) - 4);
    await S.svgCiz("tabler/clock.svg", { kutu: [1096, 712, 76, 76], bas: fr(8.53), sure: 20, azami: 25, w: 3.4, sesAralik: 3 });
    elYazisi(SURE_METNI, { x: 1196, y: 772, boyut: 56, renk: SARI, bas: fr(8.53) + 14,
      sure: 14 }); not("saat + süre etiketi", fr(8.53));
    parilti(1176, 714, { bas: fr(9.56), r: 22, periyot: 170, adet: 3 });
    const m = [["form", 9.93, 835], ["time expressions", 11.05, 890], ["irregular verbs", 12.73, 945]];
    for (const [s, t, y] of m) {
      yazi(s, { x: 1140, y, boyut: 44, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, bas: fr(t), sure: 8 });
      tik(1108, y - 12, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

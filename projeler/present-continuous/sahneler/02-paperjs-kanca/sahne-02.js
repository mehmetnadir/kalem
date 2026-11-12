// Sahne 02 — Kanca (385 kare, t_bas 3,00; cümle 2). Zamanlar eski çerçevede (t − 7,00) × 30 yazılı;
// cümle 2'den sonraki her şey fr() ile 60 kare (2,0 sn) öne alınır (K23 sıkıştırma, 04.11).
import { sahneKur, RT } from "/projeler/present-continuous/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 385, T_BAS = 7.0, KAYMA = 6.0;   // T_BAS: eski çerçeve; zaman.json t_bas 3,00

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: KAYMA });
  const { fr: fr0, ciz, daire, ok, yazi, elYazisi, cumle, altCizgi, tik, parilti, olay, not, bitis } = S;
  const fr = (t) => fr0(t) - 60;                                    // cümle 2 sonrası: 2,0 sn öne
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12;                                                    // geçiş karesi: çizimler bundan sonra başlar

  // --- cümle 1: Bu akşam amcamlara gidiyorum. (Caveat 64, x 140, y 300). Sesi sahne 01'de söylendi;
  // yazı sahne başında hazır sayılır: 0–0,4 sn'de hızlı belirir (kare 0, 3, 6, 9).
  const c1 = cumle(["Bu", "akşam", "amcamlara", "gidiyorum."].map((s, i) => ({ s, f: i * 3 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 başı (Bu)", c1[0].bas); not("gidiyorum", c1[3].bas);

  // --- sağ eskiz: ev + yürüyen figür + hilal (dikeyde ortalandı, zemin çizgisi ≈ y 600)
  const ev = await S.svgCiz("tabler/home.svg", { kutu: [1330, 336, 260, 260], bas: GB, sure: 26, azami: 25, w: 4, sesAralik: 2 });
  const figOge = S.oge({ kay: { f0: GB, f1: fr0(8.8), dx: 70 }, nefes: { bas: fr0(8.9), cx: 1190, cy: 596 } });
  const fig = await S.svgCiz("open-peeps/standing-2.svg", { kutu: [1090, 266, 190, 330], bas: GB, sure: 42, azami: 60, yuz: 3, w: 3.2, oge: figOge, sesAralik: 5, ayna: false });
  not("ev çizimi başı", GB); not("figür çizimi başı", GB); not("figür yürüme biter", fr0(8.8));
  ciz([[1040, 602], [1220, 598], [1420, 603], [1650, 599]], { w: 3, renk: IKI, alfa: 0.75, bas: 36, sure: 30, uc0: 10, uc1: 30 });
  {   // hilal: dış yay + iç yay tek darbe (el elipsi)
    const C = [1730, 386], R = 56, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 6) pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 6) pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    const h = ciz(pts, { w: 4, alfa: 0.92, bas: fr0(8.0), sure: 30, uc0: 12, uc1: 20, amp: 0.7 }); not("hilal çizimi başı", h.bas);
    parilti(C[0] + 40, C[1] - 52, { bas: bitis(h) + 2, r: 24, periyot: 150, adet: 3 });
  }

  // --- 9,39–12,35: gidiyorum sarı daire, Caveat not, ok -> takvim
  {
    const g = c1[3], d = daire((g.x0 + g.x1) / 2 + 3, g.y - 24, g.w / 2 + 6, 36, { bas: fr(9.39), sure: 24, egim: -0.04 });
    olay(bitis(d), "tik", 0.5); not("gidiyorum daire", d.bas);
    const y1 = 372, a = elYazisi("-yor", { x: 140, y: y1, boyut: 48, renk: IKI, bas: fr(10.19), sure: 10 });
    ok([a.x1 + 14, y1 - 14], [a.x1 + 84, y1 - 14], { bas: fr(10.19) + 4, sure: 10, w: 5, uzun: 16, bukum: 0.08 });
    const b = elYazisi("şimdiki zaman", { x: a.x1 + 100, y: y1, boyut: 48, renk: IKI, bas: fr(10.19) + 16, sure: 20 }); not("not -yor → şimdiki zaman", a.bas);
    ok([b.x1 + 26, y1 - 12], [b.x1 + 112, y1 - 6], { bas: fr(11.0), sure: 12, w: 5, uzun: 18, bukum: 0.1 });
    await S.svgCiz("tabler/calendar.svg", { kutu: [b.x1 + 130, 336, 88, 88], bas: fr(11.15), sure: 24, azami: 25, w: 3.4, sesAralik: 3 });
    not("takvim çizimi", fr(11.15));
    const y2 = 470, n1 = elYazisi("bu akşam", { x: 520, y: y2, boyut: 48, renk: IKI, bas: fr(11.63), sure: 14 });
    ok([n1.x1 + 14, y2 - 14], [n1.x1 + 84, y2 - 14], { bas: fr(11.63) + 6, sure: 10, w: 5, uzun: 16, bukum: 0.08 });
    elYazisi("gelecek", { x: n1.x1 + 100, y: y2, boyut: 48, renk: SARI, bas: fr(11.63) + 18, sure: 14, ses: true }); not("not bu akşam → gelecek", n1.bas);
  }

  // --- 12,50–14,58: I'm going to my uncle's tonight. (Fredoka 56 krem)
  {
    const tl = [12.5, 12.86, 13.06, 13.22, 13.42, 13.62], kel = ["I'm", "going", "to", "my", "uncle's", "tonight."];
    const e = cumle(kel.map((s, i) => ({ s, f: fr(tl[i]) })), { x: 140, y: 570, boyut: 56, aile: "Fredoka", agirlik: 700 });
    altCizgi(e, { tut: 30 }); not("İngilizce cümle başı", e[0].bas);
    const g = e[1], d = daire((g.x0 + g.x1) / 2, g.y - 20, g.w / 2 + 3, 33, { bas: fr(13.62) - 8, sure: 22, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("going daire", d.bas);
    const y = 668, a = elYazisi("-yor", { x: 140, y, boyut: 52, renk: IKI, bas: fr(13.95), sure: 10 });
    const ar = ok([a.x1 + 22, y - 16], [a.x1 + 132, y - 16], { bas: fr(13.95) + 5, sure: 18, w: 6.5, cift: true, uzun: 20, bukum: 0.05 });
    elYazisi("-ing", { x: a.x1 + 156, y, boyut: 52, renk: SARI, bas: bitis(ar) + 4, sure: 10, ses: true }); not("ok -yor ⇄ -ing", ar.bas);
  }

  // --- 14,49–20,89: sol alta taşınan el kutusu (x>=140, alt kenar y<=960), saat, zaman.json süresi, 3 madde
  {
    let sureMetni = "";
    try {
      const res = await fetch(new URL("../../zaman.json", location.href)); // paket kökü: yayında da aynı göreli yol
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const veri = await res.json();
      const sahneler = veri?.sahneler;
      const son = Array.isArray(sahneler) && sahneler.length ? sahneler[sahneler.length - 1] : null;
      const tSon = son?.t_son;
      if (typeof tSon !== "number") throw new Error("t_son sayı değil");
      if (tSon < 60) {
        sureMetni = `${Math.round(tSon)} sec`;
      } else {
        const dk = Math.round((tSon / 60) * 2) / 2;
        sureMetni = `${dk} min`;
      }
    } catch (err) {
      console.warn("zaman.json süre okunamadı:", err);
    }

    const kx = 140, ky = 705, kw = 560, kh = 245;
    S.kutu(kx, ky, kw, kh, { bas: fr(14.49) - 8, sure: 38 }); not("kutu çizimi", fr(14.49) - 8);
    await S.svgCiz("tabler/clock.svg", { kutu: [kx + 32, ky + 18, 68, 68], bas: fr(14.49), sure: 20, azami: 25, w: 3.4, sesAralik: 3 });
    if (sureMetni) {
      elYazisi(sureMetni, { x: kx + 120, y: ky + 68, boyut: 56, renk: SARI, bas: fr(14.49) + 14, sure: 14 });
    }
    not("saat + süre", fr(14.49));
    parilti(kx + 100, ky + 20, { bas: fr(15.66), r: 22, periyot: 170, adet: 3 });
    const m = [["form", 16.41, ky + 126], ["time expressions", 17.25, ky + 172], ["6 uses", 18.73, ky + 218]];
    for (const [s, t, y] of m) {
      yazi(s, { x: kx + 76, y, boyut: 40, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, bas: fr(t), sure: 8 });
      tik(kx + 44, y - 12, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

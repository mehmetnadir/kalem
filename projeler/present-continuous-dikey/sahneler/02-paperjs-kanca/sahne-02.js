// Sahne 02 (DİKEY 1080x1920) — Kanca (416 kare, t_bas 3,00; cümle 2).
// Zamanlar KÜRESEL sn (sozcukler.json); yerel kare = round((t − 3,00) × 30).
// Cümle 1 ses olarak sahne 01'de söylendi: burada 0. kareden hazır durur.
// Telefon ölçeği: figür kutusu ≥ 420 px (küçültülmez, sol sütunda sabit 500 px).
// Kart tek satır: "Bu akşam amcamlara gidiyorum." (Caveat 76).
// Sağ sütunda faz 1'de ev + hilal, faz 2'de tonight → planlı gelecek + ajanda kutusu
// (Bu derste: Form / Zaman ifadeleri / 3 kullanım). DUZ3: eski "-yor ⇄ -ing" ve "6 kullanım" düzeltildi.
import { sahneKur, RT }
  from "/projeler/present-continuous-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 416, T_BAS = 3.0;   // 16.11 DUZ3-0201T: cümle 2 yeniden sentezlendi (12,54 sn), sahne 3,00–16,48

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, ciz, daire, ok, yazi, elYazisi, cumle, altCizgi, tik, parilti, olay, not, bitis } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep, IKI = RT.ikincil;
  const GB = 12; // geçiş karesi: çizimler bundan sonra başlar
  // El yazısı (Caveat 700 tegaki, dalga 5 / K26): not ve etiketler kalemle yazılır.
  // Sözcük pencereleri cümle 2 anlatımından (f0 / f1 kare); <6 kare pencere sonraki sözcüğe uzar.
  const CS = S.sozcukler(2);
  const pen = (ilk, adet) => { const i = CS.findIndex((w) => w.s === ilk);
    return CS.slice(i, i + adet).map((w, k) => ({ f0: w.f,
      f1: w.f1 - w.f < 6 && CS[i + k + 1] ? CS[i + k + 1].f : w.f1 })); };

  // --- Cümle 1: kart tek satır (kutu 48..1032, y 364..464, h 100 px); Caveat 76 tek satır
  S.kutu(48, 364, 984, 100, { bas: -8, sure: 1, w: 4, renk: IKI });
  const c1 = cumle(
    [["Bu", 0], ["akşam", 0], ["amcamlara", 0], ["gidiyorum.", 0]]
      .map(([s, satir]) => ({ s, f: -8, satir })),
    { x: 74, y: 432, boyut: 76, aile: "Caveat", agirlik: 700 });
  not("cümle 1 hazır (kare 0)", 0);

  // --- SOL SÜTUN: Figür baştan sona sabit (kutu h=500 px ≥ 420 px, KÜÇÜLME YOK)
  const figOge = S.oge({ nefes: { bas: 110, cx: 195, cy: 1280 } });
  await S.svgCiz("open-peeps/standing-2.svg", {
    kutu: [60, 780, 270, 500], bas: GB, sure: 48, azami: 60, yuz: 3,
    w: 4.4, oge: figOge, sesAralik: 4, ayna: false });
  ciz([[48, 1280], [180, 1278], [340, 1280]],
    { w: 4, renk: IKI, alfa: 0.8, bas: 36, sure: 24, uc0: 10, uc1: 20, oge: figOge });
  not("figür çizimi başı", GB);

  // --- SAĞ SÜTUN FAZ 1 (3,0–6,5 sn): Ev + hilal
  // (t=6.5 sonrası solarak yerini ajandaya bırakır)
  const evOge = S.oge({ alfa: (f) => f < fr(6.62) ? 1 : Math.max(0, 1 - (f - fr(6.62)) / 20) });
  await S.svgCiz("tabler/home.svg", {
    kutu: [500, 810, 420, 420], bas: GB, sure: 32, azami: 25, w: 4, sesAralik: 2, oge: evOge
  });
  {   // hilal: dış yay + iç yay tek darbe
    const C = [860, 760], R = 44, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 6) {
      pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    }
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 6) {
      pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    }
    const h = ciz(pts, {
      w: 4.4, alfa: 0.92, bas: 24, sure: 28, uc0: 12, uc1: 20, amp: 0.7, oge: evOge
    });
    not("hilal çizimi", h.bas);
    parilti(C[0] + 30, C[1] - 36, { bas: bitis(h) + 2, r: 24, periyot: 150, adet: 1 });
  }

  // --- 3,39 gidiyorum sarı daire; 4,19 -yor → şimdiki zaman + saat 4,71;
  // 5,27 takvim; 5,79 bu akşam → gelecek (DUZ3 zamanları)
  {
    const g = c1[3],
      d = daire((g.x0 + g.x1) / 2, g.y - 24, g.w / 2 + 10, 52, {
        bas: fr(3.39), sure: 24, egim: -0.04
      });
    olay(bitis(d), "tik", 0.5); not("gidiyorum daire", d.bas);
    const y1 = 524,
      // 4,19 anlatımsız etiket `-yor`: hedef 10 kare (0,33 sn) → 4,52
      a = elYazisi("-yor", { x: 74, y: y1, boyut: 64, renk: SARI, bas: fr(4.19), sure: 10 });
    not("-yor notu", a.bas);
    ok([a.x1 + 18, y1 - 24], [a.x1 + 110, y1 - 24], {
      bas: fr(4.19) + 6, sure: 12, w: 6, uzun: 20, bukum: 0.08
    });
    // 4,19–5,07 «şimdiki zamanla» (pencere: şimdiki 4,19–4,59 · zaman 4,63–5,07)
    const b = elYazisi("şimdiki zaman", {
      x: a.x1 + 130, y: y1, boyut: 64, renk: KRE, sozcukler: pen("şimdiki", 2)
    });
    not("şimdiki zaman", b.bas);
    await S.svgCiz("tabler/clock.svg", {
      kutu: [760, y1 - 62, 76, 76], bas: fr(4.71), sure: 22, azami: 25, w: 4, sesAralik: 2
    });
    not("saat çizimi", fr(4.71));
    const y2 = 598;
    await S.svgCiz("tabler/calendar.svg", {
      kutu: [760, y2 - 62, 76, 76], bas: fr(5.27), sure: 24, azami: 25, w: 4, sesAralik: 3
    });
    not("takvim çizimi", fr(5.27));
    // 5,63 anlatımsız etiket `bu akşam`: hedef 14 kare (0,47 sn) → 6,10
    const n1 = elYazisi("bu akşam", { x: 74, y: y2, boyut: 64, renk: KRE, bas: fr(5.79),
      sure: 14 });
    ok([n1.x1 + 18, y2 - 24], [n1.x1 + 110, y2 - 24], {
      bas: fr(5.79) + 6, sure: 10, w: 6, uzun: 20, bukum: 0.08
    });
    // 6,23 anlatımsız etiket `gelecek`: hedef 12 kare (0,4 sn) → 6,63 (eski belirme ile aynı)
    elYazisi("gelecek", {
      x: n1.x1 + 130, y: y2, boyut: 64, renk: SARI, bas: fr(5.79) + 18, sure: 12
    });
    not("bu akşam → gelecek", n1.bas);
  }

  // --- 6,62–9,04 FAZ 2 (DUZ3): I'm going to my uncle's tonight. (Fredoka 64 tek satır)
  // + going daire + tonight → planlı gelecek
  {
    const tl = [6.62, 6.78, 6.9, 7.0, 7.12, 7.26],
      kel = ["I'm", "going", "to", "my", "uncle's", "tonight."];
    const e = cumle(
      kel.map((s, i) => ({ s, f: fr(tl[i]) })),
      { x: 74, y: 686, boyut: 64, aile: "Fredoka", agirlik: 700 }
    );
    altCizgi(e, { tut: 40 }); not("İngilizce cümle başı", e[0].bas);
    const g = e[1],
      d = daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 6, 40, {
        bas: fr(8.58) - 8, sure: 22, a0: -2.0
      });
    olay(bitis(d), "tik", 0.5); not("going daire", d.bas);

    // Sağ sütun üstünde: tonight → planlı gelecek (DUZ3; eski "-yor ⇄ -ing" yanlış denklikti)
    const yIng = 785;
    const a = elYazisi("tonight", { x: 420, y: yIng, boyut: 64, renk: KRE, bas: fr(7.46), sure: 12 });
    ok([a.x1 + 18, yIng - 24], [a.x1 + 110, yIng - 24], { bas: fr(7.46) + 8, sure: 10, w: 6, uzun: 20, bukum: 0.08 });
    elYazisi("planlı gelecek", { x: a.x1 + 130, y: yIng, boyut: 64, renk: SARI, bas: fr(7.86), sure: 18, ses: true });
    not("tonight → planlı gelecek", a.bas);
  }

  // --- 10,09–15,2 AJANDA KUTUSU (DUZ3; eski 8,49–13,6): sağ sütunda x 370..1032, y 835..1280
  // Saat + "Bu derste:" üst satırda yan yana;
  // maddeler x 450'den başlar (en geniş madde ≤ 1032)
  {
    S.kutu(370, 835, 662, 445, { bas: fr(10.09) - 8, sure: 36, w: 4 });
    not("kutu çizimi", fr(10.09) - 8);
    await S.svgCiz("tabler/clock.svg", {
      kutu: [405, 868, 110, 110], bas: fr(10.09), sure: 22, azami: 25, w: 4, sesAralik: 3
    });
    // 10,09–10,73 «Bu derste» (pencere: Bu 10,09–10,17 · derste 10,25–10,73)
    elYazisi("Bu derste:", { x: 535, y: 940, boyut: 64, renk: SARI, sozcukler: pen("Bu", 2) });
    parilti(510, 885, { bas: fr(10.73), r: 24, periyot: 170, adet: 3 });
    const m = [
      ["Form", 12.01, 1060], ["Zaman ifadeleri", 12.89, 1155], ["3 kullanım", 14.49, 1250]
    ];
    for (const [s, t, y] of m) {
      yazi(s, {
        x: 450, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8
      });
      tik(410, y - 22, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

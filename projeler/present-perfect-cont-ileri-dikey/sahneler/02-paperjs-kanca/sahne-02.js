// Sahne 02 İLERİ DİKEY — Kural + kanca (440 kare, t_bas 3,00; cümle 2 = 3,39–17,25), 1080x1920.
// Bantlar: içerik 352–1392 (dolu), altyazı 1400–1536 (kalem-paper.js çizer), platform 1536–1920 boş.
// Yerleşim: üstte cümle 1 + "sınav bunu sorar"; ORTA tam genişlik kural kartı (üç satır formül);
// alt: saat + SURE_METNI ve üç maddelik kutu.
import { sahneKur, RT } from "/projeler/present-perfect-cont-ileri-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

// Kart süresi (12.11, g-29): paket zaman.json son t_son'dan; sabit 6 dakika iddiası yanlıştı.
// Göreli yol: sahneler/<sahne>/ → paket kökü (yayında da aynı). Okunamazsa etiket boş kalır.
const SURE_METNI = await fetch(new URL("../../zaman.json", location.href))
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error("HTTP " + r.status))))
  .then((z) => {
    const t = z.sahneler[z.sahneler.length - 1].t_son;
    return t < 60 ? `${Math.round(t)} sec` : `${Math.round(t / 30) / 2} min`;
  })
  .catch((e) => { console.warn("zaman.json süre okunamadı:", e); return ""; });

export const KARE = 440, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, daire, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu, svgCiz } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep;
  // El yazısı (Caveat 700 tegaki, dalga 5b-2 / K26): not ve etiketler kalemle yazılır; sözcük
  // pencereleri anlatımın f / f1 karelerinden gelir.
  const CS = S.sozcukler(2);                                  // cümle 2 sözcükleri (f / f1 kare)
  const pen = (ilk, adet) => { const i = CS.findIndex((w) => w.s === ilk);
    return CS.slice(i, i + adet).map((w) => ({ f0: w.f, f1: w.f1 })); };

  // --- cümle 1: tek satır Caveat 80 (x 64, taban 470); 0. karede hazır (sahne 01 ile aynı yer)
  const c1 = cumle(["Süreç", "mi,", "sonuç", "mu?"].map((s) => ({ s, f: -10 })),
    { x: 64, y: 470, boyut: 80, aile: "Caveat", agirlik: 700 });
  not("cümle 1 yerinde", 0);
  {   // "sonuç" sarı daire titrer (3,00–3,71)
    const g = c1[2], tit = S.oge({ tit: { f0: 0, f1: fr(3.71), g: 3 } });
    daire((g.x0 + g.x1) / 2, g.y - 28, g.w / 2 + 16, 46, { bas: -30, sure: 20, ses: false, oge: tit, w: 10 });
    not("sonuç daire titrer", 0);
  }

  // --- 3,39–5,79: "sınav bunu sorar." (Caveat 72, vurgu), kural kartı el kutusu (y 600–1150)
  // pencere: Sınav 3,39–3,79 · bunu 3,83–4,03 · sorar. 4,07–4,71
  [["sınav", "Sınav", 64, true], ["bunu", "bunu", 280, false], ["sorar.", "sorar.", 470, false]]
    .forEach(([s, ilk, x, ses]) =>
      elYazisi(s, { x, y: 560, boyut: 72, renk: SARI, sozcukler: pen(ilk, 1), ses }));
  not("sınav bunu sorar", fr(3.39));
  kutu(48, 610, 984, 540, { bas: fr(4.2), sure: 36, w: 4.4 }); not("kural kartı", fr(4.2));
  // 5,27–5,79 «kural.» penceresi
  elYazisi("KURAL", { x: 88, y: 672, boyut: 64, renk: SARI, sozcukler: pen("kural.", 1) });
  not("KURAL etiketi", fr(5.27));

  // --- 6,04–10,76: formül üç satır (Fredoka 110, taban 810 / 950 / 1090), sözcük zamanlı, her satıra daire
  {
    const B = 110, gap = 22, X0 = 96, Y1 = 810, Y2 = 950, Y3 = 1090;
    const koy = (s, x, y, t, o = {}) => yazi(s, { x, y, boyut: B, aile: "Fredoka", agirlik: 700,
      renk: o.renk || KRE, bas: fr(t), sure: 8, olcek: true, ses: o.ses !== false });
    const have = koy("have", X0, Y1, 6.12); not("have", fr(6.12));
    const sl = yazi("/", { x: have.x1 + gap, y: Y1, boyut: B, aile: "Fredoka", agirlik: 700, renk: SARI, bas: fr(6.52), sure: 6 });
    const has = koy("has", sl.x1 + gap, Y1, 6.76); not("has", fr(6.76));
    const d1 = daire((have.x0 + has.x1) / 2, Y1 - 36, (has.x1 - have.x0) / 2 + 22, 70, { bas: fr(7.1), sure: 22, w: 10 });
    olay(bitis(d1), "tik", 0.5); not("have / has daire", d1.bas);
    // 7,50 anlatımsız etiket: hedef 14 kare (0,47 sn) → 7,97
    elYazisi("yardımcı", { x: has.x1 + 50, y: Y1 - 4, boyut: 64, renk: SARI, bas: fr(7.5),
      sure: 14 });

    const p1 = koy("+", X0, Y2, 7.56, { renk: SARI, ses: false });
    const been = koy("been", p1.x1 + gap, Y2, 7.88); not("been", fr(7.88));
    const d2 = daire((been.x0 + been.x1) / 2, Y2 - 36, been.w / 2 + 22, 70, { bas: fr(8.4), sure: 22, a0: -2.2, w: 10 });
    olay(bitis(d2), "tik", 0.5); not("been daire", d2.bas);
    // 8,90 anlatımsız etiket: hedef 14 kare → 9,37
    elYazisi("3. form", { x: been.x1 + 50, y: Y2 - 4, boyut: 64, renk: SARI, bas: fr(8.9),
      sure: 14 });

    const p2 = koy("+", X0, Y3, 8.64, { renk: SARI, ses: false });
    const ing = koy("-ing", p2.x1 + gap, Y3, 9.0); not("-ing", fr(9.0));
    const d3 = daire((ing.x0 + ing.x1) / 2, Y3 - 36, ing.w / 2 + 22, 70, { bas: fr(9.6), sure: 22, a0: -1.9, w: 10 });
    olay(bitis(d3), "tik", 0.5); not("-ing daire", d3.bas);
    // 10,00 anlatımsız etiket: hedef 14 kare → 10,47
    elYazisi("süreç", { x: ing.x1 + 50, y: Y3 - 4, boyut: 64, renk: SARI, bas: fr(10.0),
      sure: 14 });
  }

  // --- 10,69–: saat etiketi (sol alt), üç maddelik kutu (sağ alt); bant 1180–1392
  await svgCiz("tabler/clock.svg", { kutu: [80, 1192, 140, 140], bas: fr(10.69), sure: 26, azami: 25, w: 4.4, sesAralik: 2 });
  // 10,85 «derste» anında etiket: 14 kare
  elYazisi(SURE_METNI, { x: 80, y: 1385, boyut: 72, renk: SARI, bas: fr(10.85), sure: 14 });
  not("saat etiketi", fr(10.69));
  parilti(235, 1205, { bas: fr(11.85), r: 26, periyot: 0, adet: 1 });
  kutu(300, 1180, 732, 212, { bas: fr(11.49), sure: 28, w: 4.4 }); not("madde kutusu", fr(11.49));
  [["form", 13.01, 1246], ["time clues", 14.21, 1309], ["2 traps", 15.41, 1372]].forEach(([s, t, y]) => {
    yazi(s, { x: 400, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8, olcek: true });
    tik(355, y - 20, { bas: fr(t) + 6 }); not("madde " + s, fr(t));
  });
  return S;
}

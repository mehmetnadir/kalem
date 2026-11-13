// Sahne 02 — Kanca (02-02-ydt-ileri, 520 kare, t_bas 3,00; cümle 1 kuyruğu + 2–4). Yerel kare = round((t − 3,00) × 30).
// Cümle 1 (Sizi karı koca ilan ediyorum., 1,00–3,08) sahne 01'den gelir: kare 0'da büyük yazı yerinde, durgun.
// Akış: (kare 12) TR cümle küçülüp sola-üste çıkar + EN kart + iki halka (c2) → ediyorum ↔ pronounce, -ing çarpı (c3)
//       → başlık künyeye uçar, ajanda Rule · Roots, 3 kök + 1 tuzak (c4).
import { sahneKur,
  RT } from "/projeler/02-02-ydt-ileri/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 520, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, daire, ciz, ok, kutu, yazi, elYazisi, cumle, parilti, olay, not, dinamik, kis, yumus,
    genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  // QA 13.11 halka kuralı: komşu harfe değen halka yerine vurgu renginde el altçizgisi
  const alt = (x0, x1, y, bas, o = {}) => {
    const pts = Array.from({ length: 10 }, (_, i) => { const u = i / 9; return [x0 + (x1 - x0) * u, y + 2.5 * Math.sin(u * 3)]; });
    return ciz(pts, { w: 6, renk: RT.vurgu, alfa: 0.9, amp: 0.5, uc0: 6, uc1: 8, tur: "isaret", ad: "altçizgi", bas, sure: 14, ...o });
  };
  const sol = (f0, f1) => (f) => kis(1 - (f - f0) / (f1 - f0));
  const G1 = S.oge({ alfa: sol(fr(15.2), fr(15.55)) });           // cümle 2–3 öğeleri; cümle 3 biter 15,14
  const ekle = (...ys) => ys.forEach((y) => G1.g.addChild(y.g));
  const kel = (cNo, ad) => S.sozcukler(cNo).find((k) => k.s.replace(/[.,;:]/g, "") === ad);

  // --- cümle 1 kuyruğu (sahne 01'den gelen yazı): kare 0'da ortada büyük; kare 12'de (3,40 sn) sol üste küçülür; 'I' (3,63) EN kartı açar
  const SZ0 = 104, F0 = `700 ${SZ0}px Fredoka`, Y0 = 560, S1 = 64 / SZ0, TX = 140, TY = 250;
  const trK = S.sozcukler(1);
  const topW = trK.reduce((a, k) => a + genislik(k.s, F0), 0) + genislik(" ", F0) * (trK.length - 1);
  const X0 = 960 - topW / 2;
  const tz = cumle(trK.map((k) => ({ s: k.s, f: -60 })), { x: X0, y: Y0, boyut: SZ0,
    aile: "Fredoka", agirlik: 700 });                              // f < 0: baştan tam görünür
  const ilan = new P.Group({ applyMatrix: false });
  ilan.addChildren(tz.map((z) => z.g));
  const U0 = 12, UD = 12, SOL0 = fr(15.2), SOL1 = fr(15.55);
  dinamik((f) => {
    const u = yumus((f - U0) / UD), s = 1 + (S1 - 1) * u;
    ilan.matrix = new P.Matrix().translate(X0 + (TX - X0) * u, Y0 + (TY - Y0) * u).scale(s)
      .translate(-X0, -Y0);
    ilan.opacity = kis(1 - (f - SOL0) / (SOL1 - SOL0));
  });
  olay(U0, "cizgi", 0.5); not("TR cümle küçülür (cümle 1 bitti 3,08; ilk 12 kare durgun)", U0);
  const fx = (x) => TX + (x - X0) * S1;                            // küçülmüş TR cümlede konum
  const ed = tz[tz.length - 1];                                    // ediyorum.

  // --- cümle 2 (3,63–6,51): EN kart (Fredoka 80, sözcük zamanlı), pronounce sarı daire, iki halka
  const SZ = 80, CX = 140, CY = 470;
  const cz = cumle(S.sozcukler(2).map((k) => ({ s: k.s, f: k.f })), { x: CX, y: CY, boyut: SZ,
    aile: "Fredoka", agirlik: 700 });
  ekle(...cz);
  not("cümle 2 başı (I)", cz[0].bas);
  kutu(CX - 32, CY - 95, cz[cz.length - 1].x1 - CX + 64, 140, { bas: cz[0].bas, sure: 30, w: 4,
    oge: G1 });
  not("kart kutusu", cz[0].bas);
  const pr = cz[2];                                                // pronounce
  const dPr = alt(pr.x0 - 2, pr.x1 + 2, CY + 14, pr.bas + 10, { oge: G1 });
  olay(dPr.bas + dPr.sure, "tik", 0.5); not("pronounce daire", dPr.bas);
  const halka = (cx, cy, rot, a0) => {                             // kalemle halka: eğik elips, hafif taşan
    const n = 44, pts = Array.from({ length: n }, (_, i) => {
      const a = a0 + (i / (n - 1)) * 1.06 * 2 * Math.PI, x = Math.cos(a) * 76, y = Math.sin(a) * 54;
      return [cx + x * Math.cos(rot) - y * Math.sin(rot), cy + x * Math.sin(rot) + y * Math.cos(rot)];
    });
    return pts;
  };
  const h1 = kel(2, "husband"), h2 = kel(2, "wife");
  ciz(halka(1490, 245, -0.35, -2.2), { w: 7, renk: KRE, alfa: 0.9, bas: h1.f, sure: 28, uc0: 10,
    uc1: 20, amp: 0.5, oge: G1, tur: "cizim", ad: "halka 1" });
  not("halka 1 (husband)", h1.f);
  ciz(halka(1600, 255, 0.35, -1.0), { w: 7, renk: KRE, alfa: 0.9, bas: h2.f, sure: 28, uc0: 10,
    uc1: 20, amp: 0.5, oge: G1, tur: "cizim", ad: "halka 2" });
  not("halka 2 (wife)", h2.f);

  // --- cümle 3 (7,06–15,14): ediyorum ≠ -ing
  {
    const LF = { boyut: 120, aile: "Fredoka", agirlik: 700 }, LY = 830;
    const e0 = kel(3, "ediyorum"), ing = kel(3, "ing"), yok = kel(3, "yok");
    const ede = yazi("ediyorum", { ...LF, x: 300, y: LY, renk: KRE, bas: e0.f, sure: 8, olcek: true,
      ses: "vurus" });
    ekle(ede); not("ediyorum (alt satır)", ede.bas);
    // küçük TR cümlede ediyorum sarı daire
    alt(fx(ed.x0) - 2, fx(ed.x1) + 2, TY + 12, e0.f + 10, { oge: G1 });
    not("ediyorum daire (küçük cümle)", e0.f);
    // şimdiki zaman: el yazısı etiket (Caveat 56), sözcük sözcük
    {
      const a = kel(3, "şimdiki"), b = kel(3, "zaman");
      const q1 = elYazisi("şimdiki", { x: 300, y: 915, boyut: 56, renk: IKI,
        sozcukler: [{ f0: a.f, f1: b.f }], oge: G1 });
      elYazisi("zaman", { x: q1.x1 + 0.3 * 56, y: 915, boyut: 56, renk: IKI,
        sozcukler: [{ f0: b.f, f1: b.f1 }], oge: G1 });
      not("şimdiki zaman etiketi (şimdiki)", a.f);
    }
    // bag: alt ediyorum ↔ EN pronounce (İngilizcede)
    const bg = kel(3, "İngilizcede");
    ok([552, 725], [(pr.x0 + pr.x1) / 2, CY + 72], { bas: bg.f, sure: 16, w: 6, uzun: 20, cift: true,
      bukum: 0.04, oge: G1, ad: "ediyorum pronounce bağı" });
    not("ediyorum ↔ pronounce oku (İngilizcede)", bg.f);
    // -ing + ≠ (ing), çarpı (yok.)
    const igz = yazi("-ing", { ...LF, x: 1130, y: LY, renk: KRE, bas: ing.f, sure: 8, olcek: true,
      ses: "vurus" });
    ekle(igz); not("-ing (ing)", igz.bas);
    [[[925, 800], [1020, 800]], [[925, 842], [1020, 842]], [[998, 762], [950, 880]]].forEach((q, i) => {
      ciz(q, { duz: true, w: 8, renk: KRE, alfa: 0.9, bas: ing.f + i * 4, sure: 5, uc0: 3, uc1: 3,
        amp: 0.5, oge: G1, ses: i === 0, tur: "cizim", ad: "≠" });
    });
    not("≠ işareti (ing)", ing.f);
    [[[1100, 738], [1368, 862]], [[1368, 738], [1100, 862]]].forEach((q, i) => {
      ciz(q, { duz: true, w: 10, renk: IKI, alfa: 0.95, bas: yok.f + i * 6, sure: 8, uc0: 4, uc1: 4,
        amp: 0.6, oge: G1, ses: i === 0, tur: "isaret", ad: "ing çarpı" });
    });
    olay(yok.f, "tik", 0.5); not("-ing çarpı (yok.)", yok.f);
    // güvenirsen: ediyorum altı sarı çizgi
    const gv = kel(3, "güvenirsen");
    ciz([[300, 858], [556, 854], [812, 860]], { w: 7, renk: SARI, alfa: 0.85, bas: gv.f, sure: 14,
      uc0: 8, uc1: 14, amp: 0.7, oge: G1, tur: "isaret", ad: "ediyorum altı" });
    not("ediyorum altı çizgi (güvenirsen)", gv.f);
    // seni: ediyorum → -ing yaya (seçenekler seni şimdiki zamana götürür)
    const sn = kel(3, "seni"), gt = kel(3, "götürür");
    ok([700, 722], [1300, 722], { bas: sn.f, sure: 22, w: 6, uzun: 22, bukum: 0.2, yon: [0, -1],
      oge: G1, ad: "ediyorum ing yayı" });
    not("ediyorum → ing yayı (seni)", sn.f);
    parilti(1330, 690, { bas: gt.f, r: 24 });
    not("parıltı (götürür)", gt.f);
  }

  // --- cümle 4 (15,69–19,93): başlık büyür, künyeye uçar; ajanda Rule · Roots; 3 kök + 1 tuzak
  {
    const F = { boyut: 140, aile: "Fredoka", agirlik: 700 }, TYY = 585, GAP = 36;
    const wS = genislik("SIMPLE", "700 140px Fredoka"), wP = genislik("PRESENT", "700 140px Fredoka");
    const x0 = 960 - (wS + GAP + wP) / 2;
    const bu = kel(4, "Bu"), de = kel(4, "derste"), fo = kel(4, "formülü");
    const G2 = S.oge({ alfa: sol(fr(16.41), fr(16.7)) });
    kutu(x0 - 60, 440, wS + GAP + wP + 120, 230, { bas: bu.f, sure: 24, w: 4, oge: G2 });
    not("başlık kutusu (Bu)", bu.f);
    const ucus = new P.Group({ applyMatrix: false });
    const s1 = yazi("SIMPLE", { ...F, x: x0, y: TYY, renk: KRE, bas: de.f, sure: 8, olcek: true,
      ses: "vurus" });
    const s2 = yazi("PRESENT", { ...F, x: x0 + wS + GAP, y: TYY, renk: KRE, bas: de.f + 4, sure: 8,
      olcek: true, ses: "vurus" });
    ucus.addChildren([s1.g, s2.g]);
    not("SIMPLE (derste)", s1.bas); not("PRESENT (derste)", s2.bas);
    // künyeye uçuş (formülü): künye "SIMPLE PRESENT" x 56, taban 72, 30 px
    const UF = fo.f, UU = 20, ES = 30 / 140;
    olay(UF, "cizgi", 0.6); not("başlık künyeye uçar (formülü)", UF);
    dinamik((f) => {
      const u = yumus((f - UF) / UU), s = 1 + (ES - 1) * u;
      ucus.matrix = new P.Matrix().translate(x0 + (56 - x0) * u, TYY + (72 - TYY) * u).scale(s)
        .translate(-x0, -TYY);
      ucus.opacity = f < UF + 14 ? 1 : kis(1 - (f - UF - 14) / 6);
    });
    // ajanda: formülü → Rule, kökünü → Roots (künye kutusunun ALTINDA sarı çizgi, y 1047)
    const LF = "500 20px Lexend", gen = (a) => genislik(a, LF);
    const sagRoots = 1864, sagRule = sagRoots - gen("Roots") - 36;
    const alt2 = (sag, ad, f0) => {
      const xa = sag + 4, xb = sag - gen(ad) - 4;
      ciz([[xb, 1047], [(xb + xa) / 2, 1045], [xa, 1047]], { w: 6, renk: SARI, alfa: 0.85, bas: f0,
        sure: 12, uc0: 6, uc1: 10, amp: 0.4, tur: "isaret", ad: "ajanda " + ad });
    };
    alt2(sagRule, "Rule", fo.f + 4); not("ajanda Rule (formülü)", fo.f + 4);
    const kk = kel(4, "kökünü");
    alt2(sagRoots, "Roots", kk.f); not("ajanda Roots (kökünü)", kk.f);
    // 3 kök + 1 tuzak: üç sarı halka (1, 2, 3), dördüncü ikincil boş halka
    const DY = 585, DX = [705, 875, 1045, 1215];
    [["üç", 1], ["sınav", 2], ["kökünü", 3]].forEach(([ad, n], i) => {
      const k = kel(4, ad);
      daire(DX[i], DY, 56, 56, { bas: k.f, sure: 20, a0: -1.8, egim: 0 });
      yazi(String(n), { x: DX[i], y: DY + 26, hizala: "orta", boyut: 72, aile: "Fredoka",
        agirlik: 700, renk: KRE, bas: k.f + 8, sure: 8, olcek: true, ses: true });
      not(`kök halkası ${n} (${ad})`, k.f);
    });
    const bir = kel(4, "bir");
    daire(DX[3], DY, 56, 56, { bas: bir.f, sure: 20, a0: -1.8, egim: 0, renk: IKI, w: 6 });
    not("tuzak halkası (bir)", bir.f);
    parilti(1215, 500, { bas: kel(4, "görüyoruz").f, r: 26 });
    not("parıltı (görüyoruz)", kel(4, "görüyoruz").f);
  }
  return S;
}

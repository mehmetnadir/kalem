// Sahne 05 — Kök 1 haber (02-02-ydt-ileri, 515 kare, t_bas 74,89; cümle 11–13). Yerel kare = round((t − 74,89) × 30).
// İlk söz 75,44 (kare 16). Akış: Kök 1 · Özet başlığı + haber / film / spor (c11) → gazete başlığı kartı,
// blocks sarı daire (c12) → TR çeviri, car çizimi, haber sunumu → geniş zaman (c13).
import { sahneKur,
  RT } from "/projeler/02-02-ydt-ileri/sahneler/05-paperjs-kok1-haber/kalem-paper.js";

export const KARE = 515, T_BAS = 74.89;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Root 1 / 3", etkin: 2, kayma: 0 });
  const { fr, daire, ciz, ok, kutu, yazi, elYazisi, cumle, parilti, olay, not, svgCiz, kis,
    genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  // QA 13.11 halka kuralı: komşu harfe değen halka yerine vurgu renginde el altçizgisi
  const alt = (x0, x1, y, bas, o = {}) => {
    const pts = Array.from({ length: 10 }, (_, i) => { const u = i / 9; return [x0 + (x1 - x0) * u, y + 2.5 * Math.sin(u * 3)]; });
    return ciz(pts, { w: 6, renk: RT.vurgu, alfa: 0.9, amp: 0.5, uc0: 6, uc1: 8, tur: "isaret", ad: "altçizgi", bas, sure: 14, ...o });
  };
  const sol = (f0, f1) => (f) => kis(1 - (f - f0) / (f1 - f0));
  const kel = (cNo, ad) => S.sozcukler(cNo).find((k) => k.s.replace(/[.,;:]/g, "") === ad);
  const sz = (cNo) => S.sozcukler(cNo);

  // --- cümle 11 (75,44–80,24): Kök 1 · Özet, haber / film / spor. 80,30–80,65 arası solar (cümle 12: 80,79)
  const G1 = S.oge({ alfa: sol(fr(80.3), fr(80.65)) });
  const ekle = (...ys) => ys.forEach((y) => G1.g.addChild(y.g));
  {
    const F = { boyut: 150, aile: "Fredoka", agirlik: 700 }, FS = "700 150px Fredoka", TY = 400, GAP = 44;
    const wA = genislik("Kök 1", FS), wD = genislik("·", FS), wO = genislik("Özet", FS);
    const x0 = 960 - (wA + GAP + wD + GAP + wO) / 2;
    const bi = kel(11, "Birinci"), oz = kel(11, "özet");
    const a = yazi("Kök 1", { ...F, x: x0, y: TY, renk: KRE, bas: bi.f, sure: 8, olcek: true,
      ses: "vurus" });
    const d = yazi("·", { ...F, x: x0 + wA + GAP, y: TY, renk: IKI, bas: oz.f, sure: 6 });
    const o = yazi("Özet", { ...F, x: x0 + wA + GAP + wD + GAP, y: TY, renk: SARI, bas: oz.f, sure: 8,
      olcek: true, ses: "vurus" });
    ekle(a, d, o);
    not("Kök 1 (Birinci)", bi.f); not("· Özet (özet.)", oz.f);
    ciz([[o.x0 - 6, TY + 30], [(o.x0 + o.x1) / 2, TY + 27], [o.x1 + 6, TY + 30]], { w: 8, renk: SARI,
      alfa: 0.85, bas: oz.f + 3, sure: 14, uc0: 8, uc1: 14, amp: 0.8, oge: G1, tur: "isaret",
      ad: "Özet altı" });
    not("Özet altı çizgi", oz.f + 3);
    // haber / film / spor: el yazısı etiketler (Caveat 100), her biri kendi sözcüğünde
    const CF = "700 100px Caveat", AR = 150;
    const w1 = genislik("haber başlığı", CF), w2 = genislik("film", CF), w3 = genislik("spor yorumu", CF);
    let lx = 960 - (w1 + w2 + w3 + 2 * AR) / 2;
    const LY = 700, hb = sz(11).filter((k) => ["Haber", "başlığı,", "film,", "spor", "yorumu."].includes(k.s));
    const [kH, kB, kF, kS, kY] = hb;
    const yaz = (s, x, k, f1) => elYazisi(s, { x, y: LY, boyut: 100, renk: KRE,
      sozcukler: [{ f0: k.f, f1 }], oge: G1 });
    const q1 = yaz("haber", lx, kH, kB.f);
    yaz("başlığı", q1.x1 + 0.3 * 100, kB, kF.f);
    not("haber başlığı (Haber)", kH.f);
    lx += w1 + AR;
    yaz("film", lx, kF, kS.f); not("film (film)", kF.f);
    lx += w2 + AR;
    const q3 = yaz("spor", lx, kS, kY.f);
    yaz("yorumu", q3.x1 + 0.3 * 100, kY, kY.f1); not("spor yorumu (spor)", kS.f);
  }

  // --- cümle 12 (80,79–84,39): gazete başlığı kartı; blocks sarı daire
  const KX = 100, KY = 250, KW = 1230, KH = 370;
  kutu(KX, KY, KW, KH, { bas: kel(12, "Truck").f, sure: 34, w: 4.4, renk: RT.murekkep });
  kutu(KX + 14, KY + 14, KW - 28, KH - 28, { bas: kel(12, "Truck").f + 6, sure: 30, w: 2.6 });
  not("gazete çerçevesi (Truck)", kel(12, "Truck").f);
  const cz = cumle(sz(12).map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 })),
    { x: 150, y: 375, boyut: 84, aile: "Fredoka", agirlik: 700, aralik: 105 });
  not("başlık yazısı (Truck)", cz[0].bas);
  const bl = cz[2];                                                // blocks
  const dB = alt(bl.x0 - 2, bl.x1 + 2, bl.y + 14, bl.bas + 10);
  olay(dB.bas + dB.sure, "tik", 0.5); not("blocks daire", dB.bas);
  // gazete sütun çizgileri (hours. 83,59): üç ince kural
  [[1280, 530], [1280, 556], [900, 582]].forEach(([xe, y], i) => {
    ciz([[150, y], [xe, y + 1]], { duz: true, w: 3, renk: IKI, alfa: 0.55, bas: kel(12, "hours").f + i * 5,
      sure: 14, uc0: 6, uc1: 8, amp: 0.5, ses: i === 0, tur: "cizim", ad: "gazete kuralı" });
  });
  not("gazete kuralları (hours.)", kel(12, "hours").f);

  // --- cümle 13 (84,94–91,66): car çizimi, TR çeviri, haber sunumu → geniş zaman
  {
    const kk = sz(13);
    await svgCiz("../../sahneler/05-paperjs-kok1-haber/kamyon.svg", { kutu: [1450, 290, 340, 260], bas: fr(84.94), sure: 36, azami: 10,
      w: 4.4, sesAralik: 2 });
    not("kamyon çizimi (Kamyon)", fr(84.94));
    let tx = 140;                                                  // Kamyon kazası otoyolu saatlerce kilitledi.
    kk.slice(0, 5).forEach((k, i) => {
      const f1 = i < 4 ? Math.max(k.f1, kk[i + 1].f) : k.f1;
      const q = elYazisi(k.s, { x: tx, y: 740, boyut: 56, renk: IKI, sozcukler: [{ f0: k.f, f1 }] });
      tx = q.x1 + 0.3 * 56;
    });
    not("TR çeviri (Kamyon)", kk[0].f);
    // haber sunumu → geniş zaman (Haber / olay / geniş / zaman)
    const F = { boyut: 80, aile: "Fredoka", agirlik: 700 }, FS = "700 80px Fredoka", RY = 900;
    const hs = kel(13, "Haber"), ol = kel(13, "olay"), ge = kel(13, "geniş"), za = kel(13, "zamanla");
    const hz = yazi("haber sunumu", { ...F, x: 140, y: RY, renk: KRE, bas: hs.f, sure: 8, olcek: true,
      ses: "vurus" });
    not("haber sunumu (Haber)", hs.f);
    const ax = hz.x1 + 40;
    ok([ax, RY - 28], [ax + 150, RY - 28], { bas: ol.f, sure: 14, w: 6, uzun: 20, bukum: 0.06 });
    not("ok (olay)", ol.f);
    const g1 = yazi("geniş", { ...F, x: ax + 190, y: RY, renk: SARI, bas: ge.f, sure: 8, olcek: true,
      ses: "vurus" });
    const g2 = yazi("zaman", { ...F, x: g1.x1 + genislik(" ", FS), y: RY, renk: SARI, bas: za.f,
      sure: 8, olcek: true, ses: "vurus" });
    not("geniş (geniş)", ge.f); not("zaman (zamanla)", za.f);
    parilti(g2.x1 + 50, RY - 80, { bas: za.f + 4, r: 26 });
    not("parıltı (zamanla)", za.f + 4);
  }
  return S;
}

// Sahne 02 — Kanca (02-02-ydt-temel, 410 kare, t_bas 3,00; cümle 2–4). Yerel kare = round((t − 3,00) × 30).
// 0–3 sn giriş kapağı ayrı sahne (01); burada ilk söz 3,39 sn (kare 12). Sözcük zamanları sozcukler.json'dan.
// Akış: kart + saat (c2) → yor ↔ ing bağı (c3) → başlık künyeye uçar, iki kullanım (c4).
import { sahneKur,
  RT } from "/projeler/02-02-ydt-temel/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 410, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, daire, ciz, ok, kutu, yazi, cumle, parilti, olay, not, bitis, svgCiz,
    dinamik, kis, yumus, genislik } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep;
  const sol = (f0, f1) => (f) => kis(1 - (f - f0) / (f1 - f0));
  // c2 + c3 öğeleri tek grupta; 11,55–11,90 sn arası solar (cümle 3 biter 11,48; cümle 4 12,03)
  const G1 = S.oge({ alfa: sol(fr(11.55), fr(11.9)) });
  const ekle = (...ys) => ys.forEach((y) => G1.g.addChild(y.g));

  // --- cümle 2 (3,39–5,63): kart, sözcük zamanlı İngilizce cümle (Fredoka 68, taban y 395)
  const SZ = 68, CX = 140, CY = 395;
  const cz = cumle(S.sozcukler(2).map((k) => ({ s: k.s, f: k.f })),
    { x: CX, y: CY, boyut: SZ, aile: "Fredoka", agirlik: 700 });
  ekle(...cz);
  not("cümle 2 başı (I)", cz[0].bas);
  kutu(CX - 32, 300, cz[cz.length - 1].x1 - CX + 64, 140, { bas: cz[0].bas, sure: 30, w: 4,
    oge: G1 });
  not("kart kutusu", cz[0].bas);
  // odak: get up (3,63) ve every morning (4,59) altı çizilir
  const alt = (a, b, f0, ad) => {
    const x0 = cz[a].x0 - 4, x1 = cz[b].x1 + 4;
    ciz([[x0, CY + 22], [(x0 + x1) / 2, CY + 19], [x1, CY + 22]], { w: 7, renk: SARI, alfa: 0.85,
      bas: f0, sure: 14, uc0: 8, uc1: 14, amp: 0.8, oge: G1, tur: "isaret", ad });
  };
  alt(1, 2, fr(3.63), "get up altı"); not("get up altı çizgi", fr(3.63));
  alt(5, 6, fr(4.59), "every morning altı"); not("every morning altı çizgi", fr(4.59));

  // saat 07:00 (seven 4,11) + güneş (morning 4,91)
  {
    const cx = 1640, cy = 400, R = 112;
    const cem = Array.from({ length: 41 }, (_, i) => { const a = -Math.PI / 2 + (i / 40) * 2 *
      Math.PI * 1.03; return [cx + Math.cos(a) * R, cy + Math.sin(a) * R]; });
    ciz(cem, { w: 6, renk: KRE, alfa: 0.9, bas: fr(4.11), sure: 26, uc0: 10, uc1: 20, oge: G1,
      tur: "cizim", ad: "saat" });
    not("saat çemberi (seven)", fr(4.11));
    [0, 90, 180, 270].forEach((d, i) => {
      const a = (d - 90) * Math.PI / 180, c = Math.cos(a), s = Math.sin(a);
      ciz([[cx + c * (R - 8), cy + s * (R - 8)], [cx + c * (R - 24), cy + s * (R - 24)]],
        { duz: true, w: 5, renk: KRE, alfa: 0.9, bas: fr(4.3) + i * 2, sure: 6, oge: G1,
          ses: false, tur: "cizim", ad: "saat tik" });
    });
    // akrep 7'yi, yelkovan 12'yi gösterir (07:00)
    ciz([[cx, cy], [cx, cy - R * 0.74]], { duz: true, w: 6, renk: KRE, alfa: 0.9,
      bas: fr(4.43), sure: 8, uc0: 4, uc1: 6, oge: G1, tur: "cizim", ad: "yelkovan" });
    ciz([[cx, cy], [cx - 0.5 * R * 0.52, cy + 0.866 * R * 0.52]], { duz: true, w: 8,
      renk: SARI, alfa: 0.9, bas: fr(4.5), sure: 8, uc0: 4, uc1: 6, oge: G1, tur: "isaret",
      ad: "akrep" });
    not("saat akrep 07:00", fr(4.5));
    ekle(yazi("07:00", { x: cx, y: cy + R + 84, hizala: "orta", boyut: 56, aile: "Fredoka",
      agirlik: 700, renk: KRE, bas: fr(4.55), sure: 8, olcek: true, ses: true }));
    await svgCiz("tabler/sun.svg", { kutu: [1440, 190, 110, 110], bas: fr(4.91), sure: 20,
      azami: 10, w: 4, sesAralik: 2, oge: G1 });
    not("güneş (morning)", fr(4.91));
  }

  // --- cümle 3 (6,10–11,48): -yor ↔ -ing bağı
  {
    const F = { boyut: 130, aile: "Fredoka", agirlik: 700 }, Y = 800;
    const yor = yazi("-yor", { ...F, x: 330, y: Y, renk: KRE, bas: fr(7.1), sure: 8, olcek: true,
      ses: "vurus" });
    const ing = yazi("-ing", { ...F, x: 1130, y: Y, renk: KRE, bas: fr(9.15), sure: 8,
      olcek: true, ses: "vurus" });
    ekle(yor, ing);
    not("-yor (kalkıyorum)", yor.bas); not("-ing", ing.bas);
    const ic = (ing.x0 + ing.x1) / 2;
    // QA 13.11: -ing halkası g kuyruğuna değiyordu → vurgu el altçizgisi (kuyruğun altında)
    const ux0 = ing.x0 - 6, ux1 = ing.x1 + 6, uy = Y + 50;
    const d = ciz([[ux0, uy + 1], [(ux0 + ux1) / 2, uy - 2], [ux1, uy + 1]], { w: 7, renk: SARI, alfa: 0.9,
      bas: fr(9.6), sure: 16, uc0: 8, uc1: 12, amp: 0.8, oge: G1, tur: "isaret", ad: "-ing altçizgi" });
    olay(bitis(d), "tik", 0.5); not("-ing altçizgi", d.bas);
    ok([yor.x1 + 50, Y - 46], [ing.x0 - 60, Y - 46], { bas: fr(9.8), sure: 18, w: 6, uzun: 22,
      cift: true, bukum: 0.05, oge: G1, ad: "yor ing bağı" });
    not("yor ↔ ing bağ çizgisi", fr(9.8));
    ekle(yazi("?", { x: (yor.x1 + ing.x0) / 2, y: Y - 80, hizala: "orta", boyut: 120,
      aile: "Fredoka", agirlik: 700, renk: SARI, bas: fr(10.64), sure: 8, olcek: true,
      ses: "vurus" }));
    not("soru işareti (Neden?)", fr(10.64));
  }

  // --- cümle 4 (12,03–16,35): başlık büyür, künyeye uçar; iki kullanım
  {
    const F = { boyut: 140, aile: "Fredoka", agirlik: 700 }, TY = 585, GAP = 36;
    const wS = genislik("SIMPLE", "700 140px Fredoka"), wP = genislik("PRESENT",
      "700 140px Fredoka");
    const x0 = 960 - (wS + GAP + wP) / 2;
    const G2 = S.oge({ alfa: sol(fr(13.71), fr(13.95)) });
    kutu(x0 - 60, 440, wS + GAP + wP + 120, 230, { bas: fr(12.1), sure: 24, w: 4, oge: G2 });
    not("başlık kutusu (Bu derste)", fr(12.1));
    const ucus = new P.Group({ applyMatrix: false });
    const s1 = yazi("SIMPLE", { ...F, x: x0, y: TY, renk: KRE, bas: fr(12.91), sure: 8,
      olcek: true, ses: "vurus" });
    const s2 = yazi("PRESENT", { ...F, x: x0 + wS + GAP, y: TY, renk: KRE, bas: fr(13.23),
      sure: 8, olcek: true, ses: "vurus" });
    ucus.addChildren([s1.g, s2.g]);
    not("SIMPLE (geniş)", s1.bas); not("PRESENT (zamanın)", s2.bas);
    // künyeye uçuş: formunu 13,71 → kare 321, 22 kare; künye "SIMPLE PRESENT" x 56, taban 72, 30 px
    const U0 = fr(13.71), UD = 22, ES = 30 / 140;
    olay(U0, "cizgi", 0.6); not("başlık künyeye uçar (formunu)", U0);
    dinamik((f) => {
      const u = yumus((f - U0) / UD), s = 1 + (ES - 1) * u;
      const px = x0 + (56 - x0) * u, py = TY + (72 - TY) * u;
      ucus.matrix = new P.Matrix().translate(px, py).scale(s).translate(-x0, -TY);
      ucus.opacity = f < U0 + 16 ? 1 : kis(1 - (f - U0 - 16) / 6);
    });
    // ajanda: formunu → Rule, kullanımını → Examples (künye kutusunun ALTINDA sarı çizgi, y 1046)
    const LF = "500 20px Lexend", gen = (a) => genislik(a, LF);
    const sagTrap = 1864, sagRule = sagTrap - gen("Trap") - 36,
      sagEx = sagRule - gen("Rule") - 36;
    const alt2 = (sag, ad, f0) => {
      const x1 = sag + 4, x0 = sag - gen(ad) - 4;
      ciz([[x0, 1047], [(x0 + x1) / 2, 1045], [x1, 1047]], { w: 6, renk: SARI, alfa: 0.85,
        bas: f0, sure: 12, uc0: 6, uc1: 10, amp: 0.4, tur: "isaret", ad: "ajanda " + ad });
    };
    alt2(sagRule, "Rule", fr(14.35)); not("ajanda Rule (ve)", fr(14.35));
    alt2(sagEx, "Examples", fr(14.91)); not("ajanda Examples (kullanımını)", fr(14.91));
    // iki kullanım: iki numaralı el kutusu (iki 14,67 / kullanımını 14,91 / ikinci kutu 15,35)
    [[1, 14.91], [2, 15.35]].forEach(([n, t], i) => {
      const x = 740 + i * 250;
      kutu(x, 430, 190, 200, { bas: fr(t), sure: 16, w: 4 });
      yazi(String(n), { x: x + 95, y: 570, hizala: "orta", boyut: 130, aile: "Fredoka",
        agirlik: 700, renk: KRE, bas: fr(t) + 8, sure: 8, olcek: true, ses: true });
      not("kullanım kutusu " + n, fr(t));
    });
    parilti(1200, 420, { bas: fr(15.5), r: 26 });
  }
  return S;
}

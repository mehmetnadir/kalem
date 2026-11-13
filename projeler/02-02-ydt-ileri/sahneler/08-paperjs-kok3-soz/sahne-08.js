// Sahne 08 — Kök 3 söz ve durum fiilleri (02-02-ydt-ileri, 1177 kare, t_bas 157,59; cümle 24–27).
// Yerel kare = round((t − 157,59) × 30). İlk söz 158,14 (kare 17).
// Akış: Kök 3 · Söz ve durum fiilleri + kanca cümlesi küçük kartta (c24) → kök kartı, think / promise
// daireleri, pencil + clock (c25) → TR çeviri, yor altı çizgi (c26) → söz fiili kutusu, durum fiili kutusu,
// -yor ↔ -ing çarpı (c27).
import { sahneKur,
  RT } from "/projeler/02-02-ydt-ileri/sahneler/08-paperjs-kok3-soz/kalem-paper.js";

export const KARE = 1177, T_BAS = 157.59;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Root 3 / 3", etkin: 2, kayma: 0 });
  const { fr, daire, ciz, ok, kutu, tik, yazi, elYazisi, cumle, parilti, olay, not, svgCiz, kis,
    genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  // QA 13.11 halka kuralı: komşu harfe değen halka yerine vurgu renginde el altçizgisi
  const alt = (x0, x1, y, bas, o = {}) => {
    const pts = Array.from({ length: 10 }, (_, i) => { const u = i / 9; return [x0 + (x1 - x0) * u, y + 2.5 * Math.sin(u * 3)]; });
    return ciz(pts, { w: 6, renk: RT.vurgu, alfa: 0.9, amp: 0.5, uc0: 6, uc1: 8, tur: "isaret", ad: "altçizgi", bas, sure: 14, ...o });
  };
  const sol = (f0, f1) => (f) => kis(1 - (f - f0) / (f1 - f0));
  const sz = (cNo) => S.sozcukler(cNo);
  const kel = (cNo, ad) => sz(cNo).find((k) => k.s.replace(/[.,;:]/g, "") === ad);

  // --- cümle 24 (158,14–163,5): Kök 3 · Söz ve durum fiilleri; kanca cümlesi küçük kartta. 164,2–164,55 solar
  {
    const G = S.oge({ alfa: sol(fr(164.2), fr(164.55)) });
    const ekle = (...ys) => ys.forEach((y) => G.g.addChild(y.g));
    const F1 = { boyut: 150, aile: "Fredoka", agirlik: 700 }, uc = kel(24, "Üçüncü"), kok = kel(24, "kök");
    const wK = genislik("Kök 3", "700 150px Fredoka");
    const k3 = yazi("Kök 3", { ...F1, x: 960 - wK / 2, y: 330, renk: KRE, bas: uc.f, sure: 8,
      olcek: true, ses: "vurus" });
    ekle(k3); not("Kök 3 (Üçüncü)", uc.f);
    ciz([[k3.x0 - 6, 362], [(k3.x0 + k3.x1) / 2, 359], [k3.x1 + 6, 362]], { w: 8, renk: SARI, alfa: 0.85,
      bas: kok.f, sure: 14, uc0: 8, uc1: 14, amp: 0.8, oge: G, tur: "isaret", ad: "Kök 3 altı" });
    not("Kök 3 altı çizgi (kök:)", kok.f);
    // Söz ve durum fiilleri (Fredoka 100): Söz (söz) · ve (ve) · durum (durum) · fiilleri (fiilleri.)
    const F2 = { boyut: 100, aile: "Fredoka", agirlik: 700 }, FS = "700 100px Fredoka", sp = genislik(" ", FS);
    const par = ["Söz", "ve", "durum", "fiilleri"], gen = par.map((p) => genislik(p, FS));
    let x = 960 - (gen.reduce((a, b) => a + b, 0) + sp * 3) / 2;
    const zam = [kel(24, "söz"), kel(24, "ve"), kel(24, "durum"), sz(24).filter((k) =>
      k.s === "fiilleri.")[0]];
    par.forEach((p, i) => {
      const y = yazi(p, { ...F2, x, y: 540, renk: KRE, bas: zam[i].f, sure: 8, olcek: true,
        ses: "vurus" });
      ekle(y); not(`${p} (${zam[i].s})`, y.bas); x += gen[i] + sp;
    });
    // kanca cümlesi küçük kartta (Açılıştaki 161,98 → kutu; tören 162,62 → sözcükler; burada. 163,50 → daire)
    const ac = kel(24, "Açılıştaki"), tr = kel(24, "tören"), bu = kel(24, "burada");
    const hk = sz(2).map((k, i) => ({ s: k.s, f: tr.f + i * 4 }));
    const cz = cumle(hk, { x: 140, y: 890, boyut: 56, aile: "Fredoka", agirlik: 700 });
    ekle(...cz);
    kutu(108, 810, cz[cz.length - 1].x1 - 140 + 64, 130, { bas: ac.f, sure: 26, w: 4, oge: G });
    not("kanca kartı kutusu (Açılıştaki)", ac.f); not("kanca cümlesi (tören)", tr.f);
    const pr = cz[2];
    const d = alt(pr.x0 - 2, pr.x1 + 2, pr.y + 12, bu.f + 8, { oge: G });
    olay(d.bas + d.sure, "tik", 0.5); not("pronounce daire (burada.)", bu.f);
  }

  // --- cümle 25–26 (164,61–176,2): kök kartı; think / promise daireleri; pencil + clock; TR çeviri
  {
    const G = S.oge({ alfa: sol(fr(176.35), fr(176.7)) });
    const ekle = (...ys) => ys.forEach((y) => G.g.addChild(y.g));
    const ks = sz(25), W = ks[0];
    kutu(108, 225, 1256, 270, { bas: W.f, sure: 34, w: 4, oge: G });
    not("kök kartı kutusu (We)", W.f);
    const cz = cumle(ks.map((k, i) => ({ s: k.s, f: k.f, satir: i < 8 ? 0 : i < 15 ? 1 : 2 })),
      { x: 140, y: 300, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 80 });
    ekle(...cz);
    const tek = (z, bas, ad) => {
      const d = alt(z.x0 - 2, z.x1 + 2, z.y + 14, bas + 8, { oge: G });
      olay(d.bas + d.sure, "tik", 0.5); not(ad, d.bas);
    };
    tek(cz[1], cz[1].bas + 2, "think daire");                      // think 164,89
    tek(cz[14], cz[14].bas + 2, "promise daire");                  // promise 168,05
    await svgCiz("tabler/pencil.svg", { kutu: [1480, 540, 260, 260], bas: kel(25, "report").f,
      sure: 28, azami: 8, w: 4.4, sesAralik: 2, oge: G });
    not("pencil çizimi (report)", kel(25, "report").f);
    await svgCiz("tabler/clock.svg", { kutu: [1480, 215, 260, 260], bas: kel(25, "tonight").f,
      sure: 30, azami: 8, w: 4.4, sesAralik: 2, oge: G });
    not("clock çizimi (tonight.)", kel(25, "tonight").f);
    // cümle 26: TR çeviri (Caveat 52), iki satır; düşünüyoruz ve veriyorum sözcüklerinde yor altı çizgi
    const kt = sz(26), CB = "700 52px Caveat";
    const yaz = (k, x, y, f1) => elYazisi(k.s, { x, y, boyut: 52, renk: IKI,
      sozcukler: [{ f0: k.f, f1 }], oge: G });
    let tx = 140, ty = 600;
    kt.forEach((k, i) => {
      if (i === 6) { tx = 140; ty = 690; }
      const f1 = i < kt.length - 1 ? Math.max(k.f1, kt[i + 1].f) : k.f1;
      const q = yaz(k, tx, ty, f1);
      tx = q.x1 + 0.3 * 52;
      const on = k.s === "düşünüyoruz;" ? "düşünü" : k.s === "veriyorum." ? "veri" : null;
      if (on) {                                                    // yor hecesi: kelime penceresinde orantılı
        const tam = genislik(k.s, CB), a = genislik(on, CB), b = genislik(on + "yor", CB);
        const xa = q.x0 + q.w * a / tam, xb = q.x0 + q.w * b / tam, fb = k.f + Math.round((k.f1 - k.f) * a / tam);
        ciz([[xa - 2, ty + 16], [(xa + xb) / 2, ty + 14], [xb + 2, ty + 16]], { w: 6, renk: SARI,
          alfa: 0.9, bas: fb, sure: 10, uc0: 6, uc1: 8, amp: 0.5, oge: G, tur: "isaret",
          ad: "yor altı " + k.s });
        not("yor altı çizgi (" + k.s + ")", fb);
      }
    });
    not("TR çeviri (İşin)", kt[0].f);
  }

  // --- cümle 27 (176,75–196,44): söz fiili kutusu, durum fiili kutusu, -yor ↔ -ing çarpı
  {
    const F = (b) => ({ boyut: b, aile: "Fredoka", agirlik: 700 });
    const pm = kel(27, "Promise"), so = kel(27, "söz"), sy = kel(27, "söylemek"), ya = kel(27, "yapmak");
    kutu(120, 170, 820, 580, { bas: pm.f, sure: 36, w: 4 });
    not("söz fiili kutusu (Promise)", pm.f);
    const l1 = yazi("promise", { ...F(64), x: 200, y: 430, renk: KRE, bas: pm.f + 8, sure: 8,
      olcek: true, ses: "vurus" });
    not("promise (Promise)", l1.bas);
    alt(l1.x0 - 2, l1.x1 + 2, 442, l1.bas + 12);
    yazi("söz fiili", { ...F(80), x: 160, y: 285, renk: KRE, bas: so.f, sure: 8, olcek: true,
      ses: "vurus" });
    not("söz fiili başlığı (söz)", so.f);
    const e1 = yazi("söylemek", { ...F(52), x: 160, y: 360, renk: IKI, bas: sy.f, sure: 8, olcek: true });
    not("söylemek (söylemek)", e1.bas);
    const eq = yazi("=", { ...F(52), x: e1.x1 + 24, y: 360, renk: SARI, bas: ya.f, sure: 6 });
    yazi("yapmak", { ...F(52), x: eq.x1 + 24, y: 360, renk: IKI, bas: ya.f, sure: 8, olcek: true });
    not("= yapmak (yapmak)", ya.f);
    const pn = kel(27, "Pronounce"), ac = kel(27, "accept"), dn = kel(27, "deny"), inf = kel(27, "inform");
    const l2 = yazi("pronounce", { ...F(64), x: 200, y: 500, renk: KRE, bas: pn.f, sure: 8,
      olcek: true, ses: "vurus" });
    alt(l2.x0 - 2, l2.x1 + 2, 512, pn.f + 12);
    not("pronounce + daire (Pronounce)", pn.f);
    [["accept", 570, ac], ["deny", 640, dn], ["inform", 710, inf]].forEach(([s, y, k]) => {
      yazi(s, { ...F(64), x: 200, y, renk: KRE, bas: k.f, sure: 8, olcek: true, ses: "vurus" });
      not(`${s} (${k.s})`, k.f);
    });
    // durum fiili: think / hope ayrı kutuda
    const th = kel(27, "Think"), ho = kel(27, "hope"), du = kel(27, "durum"), al = kel(27, "alır");
    kutu(1000, 170, 800, 580, { bas: th.f, sure: 36, w: 4 });
    not("durum fiili kutusu (Think)", th.f);
    yazi("think", { ...F(88), x: 1080, y: 470, renk: KRE, bas: th.f + 8, sure: 8, olcek: true,
      ses: "vurus" });
    not("think (Think)", th.f + 8);
    yazi("hope", { ...F(88), x: 1080, y: 610, renk: KRE, bas: ho.f, sure: 8, olcek: true,
      ses: "vurus" });
    not("hope (hope)", ho.f);
    yazi("durum fiili", { ...F(80), x: 1040, y: 285, renk: KRE, bas: du.f, sure: 8, olcek: true,
      ses: "vurus" });
    not("durum fiili başlığı (durum)", du.f);
    tik(1450, 445, { bas: al.f, ad: "think tik" }); tik(1450, 585, { bas: al.f + 4, ad: "hope tik" });
    not("tikler (alır)", al.f);
    // -yor ↔ -ing çarpı (alt şerit, Fredoka 120, taban 930)
    const yo = kel(27, "yor"), ig = kel(27, "ing"), alm = kel(27, "almaz"), ng = kel(27, "İngilizcesi");
    const yz = yazi("-yor", { ...F(120), x: 560, y: 930, renk: KRE, bas: yo.f, sure: 8, olcek: true,
      ses: "vurus" });
    not("-yor (yor)", yz.bas);
    ok([yz.x1 + 40, 884], [1070, 884], { bas: ng.f, sure: 16, w: 6, uzun: 20, cift: true, bukum: 0.04,
      ad: "yor ing bağı" });
    not("yor ↔ ing oku (İngilizcesi)", ng.f);
    const iz = yazi("-ing", { ...F(120), x: 1100, y: 930, renk: KRE, bas: ig.f, sure: 8, olcek: true,
      ses: "vurus" });
    not("-ing (ing)", iz.bas);
    [[[iz.x0 - 20, 838], [iz.x1 + 20, 950]], [[iz.x1 + 20, 838], [iz.x0 - 20, 950]]].forEach((q, i) => {
      ciz(q, { duz: true, w: 10, renk: IKI, alfa: 0.95, bas: alm.f + i * 6, sure: 8, uc0: 4, uc1: 4,
        amp: 0.6, ses: i === 0, tur: "isaret", ad: "ing çarpı" });
    });
    olay(alm.f, "tik", 0.5); not("-ing çarpı (almaz)", alm.f);
  }
  return S;
}

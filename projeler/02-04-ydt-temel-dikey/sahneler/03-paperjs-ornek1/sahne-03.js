// Sahne 03 (DİKEY) — Örnek 1: Paper.js, 1080×1920, 721 kare, t_bas 20,22; cümle 3.
// Yerel kare = round((t − 20,22) × 30). Sözcük zamanları sozcukler.json'dan okunur (s3).
// Kart A: She wears her coat in the winter. (mont, GENERAL)
// Kart B: She is wearing her pink T-shirt today. (tişört, RIGHT NOW)
import { sahneKur, RT } from "/projeler/02-04-ydt-temel-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";
import { KUNYE } from "/projeler/02-04-ydt-temel-dikey/ortak/kunye.js";
import { yaziNoktalari } from "/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js";

export const KARE = 721, T_BAS = 20.22;

// Cümle 3 parça 4 (EN "She is wearing her pink T-shirt today.") sozcukler.json'da yok.
const EN2 = [
  ["She", 32.41],
  ["is", 32.63],
  ["wearing", 32.77],
  ["her", 33.07],
  ["pink", 33.35],
  ["T-shirt", 33.63],
  ["today.", 34.13],
];

// Giysi çizimleri: birim ızgara (mont 100×120, tişört 100×90)
const MONT = [
  { n: [[40, 4], [20, 10], [6, 70], [17, 74], [26, 34], [23, 116], [50, 117]] },
  { n: [[60, 4], [80, 10], [94, 70], [83, 74], [74, 34], [77, 116], [50, 117]] },
  { n: [[40, 4], [50, 9], [60, 4]], egri: true },
  { n: [[40, 4], [44, 21], [50, 34]], egri: true },
  { n: [[60, 4], [56, 21], [50, 34]], egri: true },
  { n: [[50, 34], [50, 116]] },
  { n: [[28, 96], [38, 95]] }, { n: [[62, 95], [72, 96]] },
  { daire: [44, 48, 2.6] }, { daire: [44, 64, 2.6] }, { daire: [44, 80, 2.6] },
];

const TISORT = [
  { n: [[37, 4], [14, 12], [0, 36], [14, 46], [24, 37], [24, 88], [76, 88], [76, 37], [86, 46],
    [100, 36], [86, 12], [63, 4]] },
  { n: [[37, 4], [50, 14], [63, 4]], egri: true },
  { n: [[14, 12], [24, 37]] }, { n: [[86, 12], [76, 37]] },
];

export async function kur(P) {
  const S = await sahneKur(P, {
    KARE,
    tBas: T_BAS,
    bolum: KUNYE.cipler["03-paperjs-ornek1"],
    etkin: 1,
    kayma: 0,
  });

  // Altyazı düzeltmesi: cümle 3'ün 2. yarısında EN 32.41–34.55 ve TR bugün 35.37 başlar.
  // Ortak altyazi.json kaymasını sahne içi S.K.altyazi listesini güncelleyerek düzeltiyoruz.
  const kalan = S.K.altyazi.filter((a) => !(a.cumle === 3 && a.t0 >= 32));
  const eklenen = [
    { cumle: 3, konusan: "ogretmen", dil: "en", t0: 32.41, t1: 34.55, metin: "She is wearing her pink T-shirt today." },
    { cumle: 3, konusan: "ogretmen", dil: "tr", t0: 35.37, t1: 37.13, metin: "Bugün pembe tişörtünü giyiyor." },
    { cumle: 3, konusan: "ogretmen", dil: "tr", t0: 37.53, t1: 40.81,
      metin: "Bu yalnız bugüne ait, konuşma anında oluyor." },
    { cumle: 3, konusan: "ogretmen", dil: "tr", t0: 41.45, t1: 43.93, metin: "Şimdiki zaman: is wearing." },
  ];
  const sonC3Idx = kalan.reduce((son, a, i) => (a.cumle === 3 ? i : son), -1);
  if (sonC3Idx >= 0) kalan.splice(sonC3Idx + 1, 0, ...eklenen);
  else kalan.push(...eklenen);
  S.K.altyazi = kalan;

  // Tegaki Caveat verisi ile el yazısı metrikleri ve genişlik hesabı
  const [eyM, eyG] = await Promise.all([
    fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json"),
  ]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, {
    upm: EY.M.unitsPerEm,
    asc: EY.M.ascender,
    boy: boyut,
    x: 0,
    taban: 0,
  }).gen;

  const { fr, ciz, kutu, yazi, elYazisi, cumle, altCizgi, ok, olay, not, bitis, genislik } = S;
  const s3 = S.sozcukler(3);
  // 0 Birinci · 1 örnek. · 2 Fiil · 3 aynı: · 4 wear. · 5–11 She … winter. · 12–14 Kışın montunu giyer. ·
  // 15–17 Her kış böyle. · 18–21 Genel durum: geniş zaman. · 22–25 Bugün … giyiyor. ·
  // 26–32 Bu yalnız … oluyor. · 33–34 Şimdiki zaman: · 35 is · 36 wearing.
  const f = (i) => s3[i].f;

  // Kart A küçülme ve solma öğesi
  const kartA = S.oge({
    kucul: { f0: 350, f1: 360, s: 0.3, px: 48, py: 380, dx: 0, dy: -28 },
    alfa: (fe) => 1 - S.kis((fe - 350) / 10),
  });

  // El çizimi: birim ızgaradaki darbeleri kutuya yerleştirip çizer
  function elCizim(darbeler, [bx, by, bw, bh], [UW, UH], o) {
    const k = Math.min(bw / UW, bh / UH), ox = bx + (bw - UW * k) / 2, oy = by + (bh - UH * k) / 2;
    const yer = (q) => [ox + q[0] * k, oy + q[1] * k];
    const uz = darbeler.map((d) => (d.daire ? 2 * Math.PI * d.daire[2] : d.n.slice(1)
      .reduce((s, q, i) => s + Math.hypot(q[0] - d.n[i][0], q[1] - d.n[i][1]), 0)) * k);
    const ag = uz.map((l) => 4 + Math.pow(l, 0.75)), top = ag.reduce((s, a) => s + a, 0);
    let cur = o.bas;
    darbeler.forEach((d, i) => {
      const sr = Math.max(3, o.sure * ag[i] / top), ses = i % 3 === 0 ? undefined : false;
      if (d.daire) {
        const [cx, cy] = yer(d.daire), r = d.daire[2] * k;
        const pts = Array.from({ length: 19 }, (_, j) => {
          const a = -2.3 + j * 2.2 * Math.PI / 18;
          return [cx + Math.cos(a) * r, cy + Math.sin(a) * r];
        });
        ciz(pts, { duz: true, bas: cur, sure: Math.max(5, sr * 1.4), w: o.w * 0.9, renk: RT.murekkep,
          alfa: 0.92, amp: 0.3, uc0: 2, uc1: 3, tur: "cizim", ad: o.ad, ses: false, oge: o.oge });
      } else {
        ciz(d.n.map(yer), { duz: !d.egri, w: o.w, amp: 0.8, alfa: 0.92, bas: cur, sure: sr * 1.4,
          uc0: 8, uc1: 16, ses, tur: "cizim", ad: o.ad, oge: o.oge });
      }
      cur += sr;
    });
    return cur;
  }

  // Öbek ve vurgu altçizgisi
  function alti(x0, x1, y, bas, ad, ek = {}) {
    const d = ciz([[x0 - 2, y], [x1 + 2, y - 1]], {
      duz: true,
      w: 10,
      renk: RT.vurgu,
      alfa: 0.9,
      bas,
      sure: 14,
      uc0: 6,
      uc1: 14,
      amp: 1.2,
      tur: "isaret",
      ad,
      oge: ek.oge,
      donus: ek.donus,
    });
    olay(bitis(d), "tik", 0.5);
    not(ad, d.bas);
    return d;
  }

  const fnt = "700 72px Fredoka";
  const yalin = (z) => z.x0 + genislik(z.str.replace(/[.,:]$/, ""), fnt);
  // kuyruklu sözcükte (g, y) çizgi kuyruğun 8 px altından geçer (QA tur 1: +8 değiyordu)
  const altY = (z) => z.y + Math.max(72 * 0.28, (z.desc || 0) + 13);

  // #1: Kart A kutusu (20,77 / 17)
  kutu(48, 380, 984, 344, { w: 4, renk: RT.ikincil, oge: kartA, bas: f(0), sure: 28 });
  not("kart A kutusu", f(0));

  // #2: Kart A cümle sözcük sözcük + karaoke (24,22–25,78 / 120–167)
  const kelA = s3.slice(5, 12).map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 }));
  const czA = cumle(kelA, { x: 88, y: 478, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: 92, oge: kartA });
  altCizgi(czA, { tut: 40, w: 9, oge: kartA });
  not("kart A cümle", czA[0].bas);

  // #3: Mont çizimi (25,02 / 144)
  const mBit = elCizim(MONT, [320, 750, 440, 440], [100, 120],
    { w: 4.8, oge: kartA, bas: f(8), sure: 42, ad: "mont" });
  not("mont çizimi", f(8));
  not("mont bitti", mBit);

  // #4: TR 1 el yazısı (26,79 / 197)
  const tr1 = elYazisi("Kışın montunu giyer.", {
    x: 88,
    y: 680,
    boyut: 64,
    renk: RT.murekkep,
    oge: kartA,
    sozcukler: [12, 13, 14].map((i) => ({ f0: f(i), f1: i < 14 ? f(i + 1) : s3[i].f1 })),
  });
  not("TR 1 el yazısı", tr1.bas);

  // #5: Odak in the winter (28,55 / 250)
  alti(czA[4].x0, yalin(czA[6]), altY(czA[4]), f(15), "odak in the winter", { oge: kartA });

  // #6: GENERAL el yazısı (30,31 / 303)
  const g1 = elYazisi("GENERAL", {
    x: 540 - eyGen("GENERAL", 80) / 2,
    y: 1296,
    boyut: 80,
    renk: RT.murekkep,
    oge: kartA,
    sozcukler: [{ f0: f(18), f1: f(20) }],
  });
  not("GENERAL el yazısı", g1.bas);

  // #7: GENERAL altçizgisi (31,35 / 334)
  alti(g1.x0, g1.x1, 1296 + 18, f(20), "GENERAL altçizgi", { oge: kartA });

  // #8: Kart A küçülür + söner (31,89–32,22 / 350–360)
  not("kart A küçülür + söner", 350);

  // #9: Şerit kutusu (32,02 / 354)
  kutu(48, 352, 984, 120, { w: 4, renk: RT.ikincil, bas: 354, sure: 10 });
  not("şerit kutusu", 354);

  // #10: Şerit mont simgesi (32,09 / 356)
  elCizim(MONT, [916, 362, 100, 100], [100, 120], { w: 3.2, bas: 356, sure: 12, ad: "mont-simge" });
  not("şerit mont simgesi", 356);

  // #11: Kart B kutusu (32,15 / 358)
  kutu(48, 490, 984, 340, { w: 4, renk: RT.ikincil, bas: 358, sure: 8 });
  not("kart B kutusu", 358);

  // #12: Şerit wears (32,25 / 361)
  const wears = yazi("wears", {
    x: 88,
    y: 434,
    boyut: 64,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: 361,
    sure: 5,
  });
  not("şerit wears", 361);

  // #13: Şerit ok (32,32 / 363)
  ok([wears.x1 + 24, 414], [wears.x1 + 114, 414], { w: 6, renk: RT.ikincil, bukum: 0.04, bas: 363, sure: 6 });
  not("şerit ok", 363);

  // #14: Şerit GENERAL (32,35 / 364)
  elYazisi("GENERAL", { x: wears.x1 + 134, y: 436, boyut: 64, renk: RT.murekkep, bas: 364, sure: 9 });
  not("şerit GENERAL", 364);

  // #15: Kart B cümle sözcük sözcük + karaoke (32,41–34,13 / 366–417)
  const kelB = EN2.map(([s, t], i) => ({ s, f: fr(t), satir: i < 4 ? 0 : 1 }));
  // satır aralığı 92: 1. satır kuyruk altçizgisi 2. satırın T/t üstüne değmez (QA tur 1)
  const czB = cumle(kelB, { x: 88, y: 588, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: 92 });
  altCizgi(czB, { tut: 40, w: 9 });
  not("kart B cümle", czB[0].bas);

  // #16: Tişört çizimi (33,63 / 402)
  const tBit = elCizim(TISORT, [330, 860, 420, 400], [100, 90],
    { w: 4.8, bas: fr(33.63), sure: 36, ad: "tisort" });
  not("tişört çizimi", fr(33.63));
  not("tişört bitti", tBit);

  // #17: TR 2 el yazısı (35,37 / 454)
  const tr2 = elYazisi("Bugün pembe tişörtünü giyiyor.", {
    x: 88,
    y: 790,
    boyut: 64,
    renk: RT.murekkep,
    sozcukler: [22, 23, 24, 25].map((i) => ({ f0: f(i), f1: i < 25 ? f(i + 1) : s3[i].f1 })),
  });
  not("TR 2 el yazısı", tr2.bas);

  // #18: Odak today (38,17 / 539)
  alti(czB[6].x0, yalin(czB[6]), altY(czB[6]), f(28), "odak today", { donus: f(35) });

  // #19: RIGHT NOW el yazısı (39,05 / 565)
  const g2 = elYazisi("RIGHT NOW", {
    x: 540 - eyGen("RIGHT NOW", 80) / 2,
    y: 1340,
    boyut: 80,
    renk: RT.murekkep,
    sozcukler: [{ f0: f(30), f1: f(31) }, { f0: f(31), f1: f(32) + 8 }],
  });
  not("RIGHT NOW el yazısı", g2.bas);

  // #20: RIGHT NOW altçizgisi (41,45 / 637)
  alti(g2.x0, g2.x1, 1340 + 18, f(33), "RIGHT NOW altçizgi");

  // #21: is altçizgisi + today ikincile döner (42,81 / 678)
  alti(czB[1].x0, yalin(czB[1]), altY(czB[1]), f(35), "is altçizgi");

  // #22: -ing altçizgisi (43,05 / 685)
  alti(czB[2].x0 + genislik("wear", fnt), czB[2].x1, altY(czB[2]), f(36), "-ing altçizgi");

  return S;
}

// SAHNE 05 — Örnek 3 (düz canvas, 525 kare, t_bas 43,36; cümle 5; çıkış geçişi fade). Zaman yalnız
// kare numarasından.
// Simple Present: "Our plane takes off at nine tomorrow." (tarifeye bağlı gelecek). BRIEF §4 sahne
// 05.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, elips, olc, geriTasma, yavasla, kis } from "./sahne-ortak.js";

const KARE = 525, TBAS = 43.36, ICERIK = 513;
const KOKDIZ = "/projeler/simple-present-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3",
  cumle: 5 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`;

// Kalkış yayı: ikinci derece Bezier (başlangıç, kontrol, bitiş).
const P0 = [1250, 690], P1 = [1500, 690], P2 = [1620, 400];
const bez = (u) => [(1 - u) ** 2 * P0[0] + 2 * (1 - u) * u * P1[0] + u * u * P2[0],
  (1 - u) ** 2 * P0[1] + 2 * (1 - u) * u * P1[1] + u * u * P2[1]];
const egim = (u) => Math.atan2(2 * (1 - u) * (P1[1] - P0[1]) + 2 * u * (P2[1] - P1[1]),
  2 * (1 - u) * (P1[0] - P0[0]) + 2 * u * (P2[0] - P1[0]));

async function kur() {
  await S.kur();
  const [ucak0, takvim] = await Promise.all([svgOku("coco/plane.svg"),
    svgOku("tabler/calendar.svg")]);
  // Coco uçağı sola bakar; kalkış sağa-yukarı olduğu için yatay çevrilir (yol dönüşümü
  // svgYollari'nda işlenir).
  const ucak = ucak0.replace(/(<svg[^>]*>)/,
    '$1<g transform="matrix(-1 0 0 1 137.69057 0)">').replace("</svg>", "</g></svg>");

  // 43,91 daire içinde 3
  S.koy(S.daireSayi(3, 190, 205, 43.91));

  // 45,20–46,48 İngilizce cümle (sözcük zamanlı) + sarı alt çizgi
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Our", 45.2, 7), x: 140, y: 345, maxGen: 800 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y)),
    kel = (ad) => cum.kel.find((k) => k.m.startsWith(ad));
  S.koy(S.halka(kel("nine"), 46.52, 0.3, 31));
  S.koy(S.halka(kel("tomorrow"), 46.9, 0.35, 32));

  // 45,20–47,60 sağ: pist, uçak (Coco), kalkış yayı; 47,60'ta uçak yay boyunca kalkar
  S.koy(S.darbe([[1010, 826], [1250, 821], [1500, 828]], { w: 4, renk: KREM, uc0: 10, uc1: 20,
    tohum: 71 }, 45.2, 0.55, 0.5));
  const ug = S.cizim({ svg: ucak, kutu: { x: P0[0] - 240, y: P0[1] - 140, w: 480, h: 280 },
    ad: "ucak", esik: 0.01,
    enCok: 45, w: 3.8, tb: 45.45, sure: 1.4, olayEnCok: 6, nefes: false });
  const fK = S.fr(47.6), fKS = S.fr(50.0);
  ug.donusum = (f) => {
    const u = kis((f - fK) / (fKS - fK)), e = yavasla(u), fi = Math.min(f, ICERIK), q = bez(e);
    const bob = u >= 1 ? 5 * Math.sin((fi - fKS) / 26) : 0;
    return { cx: P0[0], cy: P0[1], tx: q[0] - P0[0], ty: q[1] - P0[1] + bob,
      dondur: -0.3 * Math.min(e * 2.5, 1), olcek: 1 };
  };
  S.koy(ug);
  // kalkış yayı: kesik çizgiler (46,00–47,40)
  for (let i = 0; i < 6; i++) {
    const a = 0.1 + i * 0.15, b = a + 0.08, nok = [];
    for (let k = 0; k <= 6; k++) nok.push(bez(a + (b - a) * k / 6));
    S.koy(S.darbe(nok, { w: 3.4, renk: IKINCIL, alfa: 0.8, uc0: 4, uc1: 8, tohum: 90 + i },
      46.0 + i * 0.22, 0.18, i === 0 ? 0.5 : false));
  }
  // 47,60 toz çizgileri (pistte, kısa ömürlü)
  [[[1050, 806], [1020, 818]], [[1062, 816], [1026, 830]], [[1070, 800], [1040, 804]]].forEach((p,
    i) => {
    const d = S.darbe(p, { duz: true, w: 3.4, renk: IKINCIL, alfa: 0.8, uc0: 4, uc1: 8,
      tohum: 120 + i }, 47.6 + i * 0.05, 0.15, i === 0 ? 0.45 : false);
    const f0 = S.fr(48.5), oc = d.ciz; d.ciz = (ctx,
      f) => { d.carpan = 1 - kis((f - f0) / 8); if (d.carpan > 0) oc(ctx, f); };
    S.koy(d);
  });
  S.koy(S.parilti(1700, 290, 49.9, 30));

  // 46,80 takvim (Tabler) + "tomorrow" (Caveat)
  S.koy(S.cizim({ svg: takvim, kutu: { x: 1570, y: 700, w: 230, h: 230 }, ad: "takvim",
    esik: 0.003, enCok: 12, w: 4,
    tb: 46.8, sure: 0.9, olayEnCok: 3, nefes: false }));
  S.koy(S.elYazisi({ metin: "tomorrow", x: 1570, y: 680, boy: 60, renk: SARI, tb: 47.2,
    sure: 0.5 }));

  // 48,01–52,01 Türkçe çeviri
  const ytr = sonSatir + 78;
  // pencere: Uçağımız 48,01–48,65 · yarın 48,73–48,97 (0,16 sn → sonraki başa dek) · dokuzda
  // 48,97–49,29 ·
  // kalkar. 49,37–50,25
  S.koy(S.elYazisi({ metin: "Uçağımız yarın dokuzda kalkar.", x: 140, y: ytr, renk: IKINCIL,
    sozcukler: S.dizi("Uçağımız", 48.01, 4).map((w, i, a) => ({ t0: w.t0,
      t1: i === 1 ? a[2].t0 : w.t1 })) }));

  // 52,88–56,32 tarife tablosu (el çizimi kutu) 09:00 | takes off + 3 etiket tik
  const ty = ytr + 52, tf = FF(60);
  S.koy(S.darbeler(kutu(140, ty, 660, 118, 41), { w: 3.6, renk: KREM, uc0: 10, uc1: 18 }, 52.88,
    0.14, 0.1, 0.55));
  S.koy(S.darbe([[360, ty + 14], [358, ty + 60], [362, ty + 104]], { w: 3.2, renk: IKINCIL,
    uc0: 8, uc1: 14, tohum: 44 }, 53.3, 0.2, 0.4));
  S.koy(S.metinPop({ parca: [["09:00", KREM]], x: 178, y: ty + 80, font: tf, tb: 53.1, sure: 0.35,
    ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["takes off", KREM]], x: 392, y: ty + 80, font: tf, tb: 53.45,
    sure: 0.35, ses: 0.5 }));
  const yb = ty + 150, bh = 62, lfn = "700 34px Lexend";
  let xx = 140;
  [["tarife", 52.88], ["program", 53.88], ["takvim", 54.36]].forEach(([m, tb], i) => {
    const w = olc(lfn, m) + 84;
    S.koy(S.darbeler(kutu(xx, yb, w, bh, 30 + i), { w: 3.4, renk: KREM, uc0: 8, uc1: 14 }, tb,
      0.1, 0.06, false));
    S.koy(S.metinPop({ parca: [[m, KREM]], x: xx + 22, y: yb + 43, font: lfn, tb: tb + 0.22,
      sure: 0.3, ses: 0.5 }));
    S.koy(S.darbe([[xx + w - 50, yb + 34], [xx + w - 40, yb + 46], [xx + w - 18, yb + 18]],
      { w: 6, renk: SARI, alfa: 0.9, uc0: 4, uc1: 8, tohum: 140 + i }, tb + 0.45, 0.2, 0.45));
    xx += w + 28;
  });
  S.koy(S.elYazisi({ metin: "= geniş zaman", x: xx + 10, y: yb + 46, boy: 56, renk: SARI, tb: 56.32,
    sure: 0.6 }));

  // 57,99–60,47 "takes off" sarı daire (cümlede); formül kartı it + V-s
  const kt = kel("takes"), ko = kel("off");
  const cx = (kt.x + ko.x + ko.w) / 2, rx = (ko.x + ko.w - kt.x) / 2 + 14;
  S.koy(S.darbe(elips(cx, kt.y - 22, rx, 46, -0.03, 25), { w: 6.5, renk: SARI, alfa: 0.85,
    uc0: 14, uc1: 30, tohum: 25 },
    57.99, 0.5, 0.55));
  S.koy(S.nabiz(cx, kt.y - 22, 30, 58.6));
  const ky = 816, fo = FF(60), fo2 = FF(52);
  S.koy(S.kart({ x: 140, y: ky, w: 620, h: 152, tb: 59.27, tohum: 7, kutuSure: 0.1,
    kutuAralik: 0.05, satirlar: [
    { parca: [["it", KREM]], x: 190, y: ky + 58, font: fo, tb: 59.27, sure: 0.3 },
    { parca: [["+", IKINCIL]], x: 330, y: ky + 58, font: fo, tb: 59.29, sure: 0.3 },
    { parca: [["V", KREM], ["-s", SARI]], x: 410, y: ky + 58, font: fo, tb: 59.59, sure: 0.3 },
    { parca: [["it", KREM]], x: 190, y: ky + 120, font: fo2, tb: 59.7, sure: 0.3 },
    { parca: [["take", KREM], ["-s", SARI]], x: 410, y: ky + 120, font: fo2, tb: 59.95, sure: 0.3 },
  ] }));
}

surucu(kur, (f) => S.kare(f), KARE);

// SAHNE 05 (DİKEY) — Örnek 3: düz canvas, 525 kare, t_bas 43,36; cümle 5.
// Zaman yalnız kare numarasından. Simple Present: "Our plane takes off at nine tomorrow."
// Yerleşim BRIEF-DIKEY §4 (içerik bandı 352–1392):
// kart (3 + cümle) -> TR çeviri -> uçak + takvim (orta) -> tarife kutusu -> etiketler ->
// formül (alt).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, elips, olc, yavasla, kis } from "./sahne-ortak.js";

const KARE = 525, TBAS = 43.36, ICERIK = 513;
const KOKDIZ = "/projeler/simple-present-temel-dikey/ortak/cizim";
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5,
});
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

// Kalkış yayı: ikinci derece Bezier (başlangıç, kontrol, bitiş) — uçak merkezi.
const P0 = [260, 935], P1 = [430, 935], P2 = [640, 855];
const bez = (u) => [(1 - u) ** 2 * P0[0] + 2 * (1 - u) * u * P1[0] + u * u * P2[0],
  (1 - u) ** 2 * P0[1] + 2 * (1 - u) * u * P1[1] + u * u * P2[1]];

async function kur() {
  await S.kur();
  const [ucak0, takvim] = await Promise.all([
    svgOku("coco/plane.svg"),
    svgOku("tabler/calendar.svg"),
  ]);
  // Coco uçağı sola bakar; kalkış sağa-yukarı olduğu için yatay çevrilir.
  const ucak = ucak0
    .replace(/(<svg[^>]*>)/, '$1<g transform="matrix(-1 0 0 1 137.69057 0)">')
    .replace("</svg>", "</g></svg>");

  // Kart (tam genişlik 984): daire içinde 3 (43,91) + cümle sözcük zamanında (45,20)
  S.koy(S.darbeler(
    kutu(48, 372, 984, 238, 11), { w: 4, renk: IKINCIL, uc0: 10, uc1: 16 }, 44.4, 0.12, 0.1, 0.5
  ));
  S.koy(S.daireSayi(3, 150, 470, 43.91));
  const cum = S.koy(S.cumleYaz({
    sozcukler: S.dizi("Our", 45.2, 7), x: 270, y: 468, maxGen: 720,
    font: FF(72), satirH: 80, bosluk: 8,
  }));
  const kel = (ad) => cum.kel.find((k) => k.m.startsWith(ad));
  S.koy(S.halka(kel("nine"), 46.52, 0.3, 31));
  S.koy(S.halka(kel("tomorrow"), 46.9, 0.35, 32));

  // 48,01 Türkçe çeviri (Caveat 64, mürekkep)
  S.koy(S.not({
    parca: [["Uçağımız yarın dokuzda kalkar.", KREM]],
    x: 48, y: 683, font: CV(64), tb: 48.01, sure: 0.8,
  }));

  // 45,20–47,60 pist + uçak (Coco, 440 px) + kalkış yayı; 47,60'ta uçak yay boyunca kalkar
  S.koy(S.darbe(
    [[48, 1042], [300, 1037], [560, 1044]],
    { w: 4.4, renk: KREM, uc0: 10, uc1: 20, tohum: 71 },
    45.2,
    0.55,
    0.5
  ));
  const ug = S.cizim({
    svg: ucak, kutu: { x: P0[0] - 220, y: P0[1] - 118, w: 440, h: 236 }, ad: "ucak", esik: 0.01,
    enCok: 45, w: 4.4, tb: 45.45, sure: 1.4, olayEnCok: 6, nefes: false,
  });
  const fK = S.fr(47.6), fKS = S.fr(50.0);
  ug.donusum = (f) => {
    const u = kis((f - fK) / (fKS - fK)), e = yavasla(u), fi = Math.min(f, ICERIK), q = bez(e);
    const bob = u >= 1 ? 5 * Math.sin((fi - fKS) / 26) : 0;
    return {
      cx: P0[0], cy: P0[1], tx: q[0] - P0[0], ty: q[1] - P0[1] + bob,
      dondur: -0.26 * Math.min(e * 2.5, 1), olcek: 1 - 0.1 * e,
    };
  };
  S.koy(ug);
  for (let i = 0; i < 6; i++) { // kalkış yayı: kesik çizgiler (46,00–47,40)
    const a = 0.1 + i * 0.15, b = a + 0.08, nok = [];
    for (let k = 0; k <= 6; k++) nok.push(bez(a + (b - a) * k / 6));
    S.koy(S.darbe(
      nok,
      { w: 4, renk: IKINCIL, alfa: 0.8, uc0: 4, uc1: 8, tohum: 90 + i },
      46.0 + i * 0.22,
      0.18,
      i === 0 ? 0.5 : false
    ));
  }
  [[[100, 1020], [66, 1032]], [[112, 1030], [72, 1044]], [[122, 1014], [88, 1018]]].forEach(
    (p, i) => { // toz
      const d = S.darbe(
        p, { duz: true, w: 4, renk: IKINCIL, alfa: 0.8, uc0: 4, uc1: 8, tohum: 120 + i },
        47.6 + i * 0.05, 0.15, i === 0 ? 0.45 : false
      );
      const f0 = S.fr(48.5), oc = d.ciz;
      d.ciz = (ctx, f) => {
        d.carpan = 1 - kis((f - f0) / 8); if (d.carpan > 0) oc(ctx, f);
      };
      S.koy(d);
    }
  );
  S.koy(S.parilti(740, 750, 49.9, 34));

  // 46,80 takvim (Tabler, 210 px) + "tomorrow" (Caveat 64, vurgu)
  S.koy(S.cizim({
    svg: takvim, kutu: { x: 810, y: 750, w: 210, h: 210 }, ad: "takvim", esik: 0.003, enCok: 12,
    w: 4.4, tb: 46.8, sure: 0.9, olayEnCok: 3, nefes: false,
  }));
  S.koy(S.not({
    parca: [["tomorrow", SARI]], x: 800, y: 1022, font: CV(64), tb: 47.2, sure: 0.5,
  }));

  // 52,88–56,32 tarife kutusu: 09:00 | takes off ; etiketler tik ; "= geniş zaman"
  const ty = 1062, tf = FF(64);
  S.koy(S.darbeler(
    kutu(48, ty, 600, 92, 41), { w: 4, renk: KREM, uc0: 10, uc1: 18 }, 52.88, 0.14, 0.1, 0.55
  ));
  S.koy(S.darbe(
    [[262, ty + 12], [260, ty + 46], [264, ty + 80]],
    { w: 3.6, renk: IKINCIL, uc0: 8, uc1: 14, tohum: 44 },
    53.3,
    0.2,
    0.4
  ));
  S.koy(S.metinPop({
    parca: [["09:00", KREM]], x: 78, y: ty + 66, font: tf, tb: 53.1, sure: 0.35, ses: 0.5,
  }));
  S.koy(S.metinPop({
    parca: [["takes off", KREM]], x: 292, y: ty + 66, font: tf, tb: 53.45, sure: 0.35, ses: 0.5,
  }));
  S.koy(S.not({
    parca: [["= geniş zaman", SARI]], x: 680, y: ty + 66, font: CV(64), tb: 56.32, sure: 0.6,
  }));
  const yb = ty + 112, bh = 72, lfn = CV(64);
  let xx = 48;
  [["tarife", 52.88], ["program", 53.88], ["takvim", 54.36]].forEach(([m, tb], i) => {
    const w = olc(lfn, m) + 56 + 44;
    S.koy(S.darbeler(
      kutu(xx, yb, w, bh, 30 + i), { w: 4, renk: KREM, uc0: 8, uc1: 14 }, tb, 0.1, 0.06, false
    ));
    S.koy(S.metinPop({
      parca: [[m, KREM]], x: xx + 28, y: yb + 54, font: lfn, tb: tb + 0.22, sure: 0.3, ses: 0.5,
    }));
    S.koy(S.darbe(
      [[xx + w - 58, yb + 38], [xx + w - 46, yb + 52], [xx + w - 20, yb + 20]],
      { w: 8, renk: SARI, alfa: 0.9, uc0: 4, uc1: 8, tohum: 140 + i },
      tb + 0.45,
      0.2,
      0.45
    ));
    xx += w + 26;
  });

  // 57,99 "takes off" sarı daire; formül it + take-s (Fredoka 110); 59,59 "-s" daire
  const kt = kel("takes"), ko = kel("off");
  if (kt.satir === ko.satir) {
    S.koy(S.darbe(
      elips((kt.x + ko.x + ko.w) / 2, kt.y - 22, (ko.x + ko.w - kt.x) / 2 + 22, 54, -0.03, 25),
      { w: 9, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30, tohum: 25 },
      57.99,
      0.5,
      0.55
    ));
  } else {
    S.koy(S.halka(kt, 57.99, 0.3, 25));
    S.koy(S.halka(ko, 58.39, 0.3, 26));
  }
  const fy = 1372, ff = FF(110);
  const wIt = olc(ff, "it"), wPl = olc(ff, " + "), wTk = olc(ff, "take"), wS = olc(ff, "-s");
  const fx0 = 540 - (wIt + wPl + wTk + wS) / 2;
  S.koy(S.metinPop({
    parca: [["it", KREM], [" + ", IKINCIL], ["take", KREM], ["-s", SARI]],
    x: fx0, y: fy, font: ff, tb: 57.99, sure: 0.4, ses: 0.8, turu: "vurus",
  }));
  const sx = fx0 + wIt + wPl + wTk + wS / 2;
  S.koy(S.darbe(
    elips(sx, fy - 38, wS / 2 + 26, 70, 0.05, 28),
    { w: 9, renk: SARI, alfa: 0.9, uc0: 14, uc1: 30, tohum: 28 },
    59.59,
    0.4,
    0.55
  ));
  S.koy(S.nabiz(sx, fy - 38, 40, 60.0));
}

surucu(kur, (f) => S.kare(f), KARE);

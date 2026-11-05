// SAHNE 05 (DİKEY) — Örnek 3: düz canvas, 517 kare, t_bas 45,98; cümle 5.
// Zaman yalnız kare numarasından.
// Yerleşim BRIEF-DIKEY §4: kart (Look! + cümle) -> TR çeviri ->
// ağaç+kedi (sol) + etiket sütunu (sağ) -> formül.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, elips, olc, geriTasma, yavasla, kis } from "./sahne-ortak.js";

const KARE = 517, TBAS = 45.98, ICERIK = 505;
const KOKDIZ = "/projeler/present-continuous-dikey/ortak/cizim";
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 3 / 3", cumle: 5
});
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;
// El yazısı (tegaki Caveat, dalga 5 / K26): sözcük penceresi = anlatım t0/t1 (küresel sn);
// <0,2 sn pencere sonraki sözcüğün başına uzar.
const pen = (ad, t, n) => {
  const q = S.dizi(ad, t, n + 1);
  return q.slice(0, n).map((w, k) => ({ t0: w.t0, t1: w.t1 - w.t0 < 0.2 ? q[k + 1].t0 : w.t1 }));
};

async function kur() {
  await S.kur();
  const [agac, kedi] = await Promise.all([svgOku("coco/tree.svg"), svgOku("coco/cat.svg")]);

  // Kart (tam genişlik 984, iç boşluk 40):
  // 47,27 Look! kırmızı pop + cümle sözcük zamanında
  S.koy(S.darbeler(
    kutu(48, 372, 984, 316, 11), { w: 4, renk: IKINCIL, uc0: 10, uc1: 16 },
    46.5, 0.12, 0.1, 0.5
  ));
  const lx = 88, ly = 480, lf = FF(110), lw = olc(lf, "Look"), lfb = S.fr(47.27);
  S.bas(lfb); S.olay(lfb, "vurus", 0.9);
  S.koy({ ciz: (ctx, f) => {
    const u = (f - lfb) / 13; if (u <= 0) return;
    const s = 0.6 + 0.4 * geriTasma(u, 2.2), cx = lx + lw / 2, cy = ly - 40;
    ctx.save(); ctx.globalAlpha = kis(u * 3);
    ctx.translate(cx, cy); ctx.scale(s, s); ctx.translate(-cx, -cy);
    ctx.font = lf; ctx.textAlign = "left"; ctx.textBaseline = "alphabetic";
    ctx.fillStyle = renkCoz(KIRMIZI);
    ctx.fillText("Look", lx, ly); ctx.restore();
  } });
  const ux = lx + lw + 14;
  S.koy(S.darbe([[ux - 2, ly - 86], [ux + 2, ly - 56], [ux + 3, ly - 28]],
    { w: 16, renk: KIRMIZI, alfa: 0.95, uc0: 6, uc1: 18, tohum: 61 }, 47.5, 0.22, 0.7));
  S.koy(S.darbe(
    elips(ux + 3, ly - 6, 3.5, 3.5, 0, 62),
    { w: 13, renk: KIRMIZI, alfa: 0.95, uc0: 4, uc1: 4, tohum: 63 },
    47.78, 0.12, false));

  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("The", 47.99, 6), x: 88, y: 574, maxGen: 740,
    font: FF(72), satirH: 84, bosluk: 8 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 50,32 Türkçe çeviri (Caveat 64, mürekkep)
  const ytr = sonSatir + 100;
  // 50,32–52,80 «Bak, kedi ağaca tırmanıyor.» (pencere: 4 sözcük)
  S.koy(S.elYazisi({ metin: "Bak, kedi ağaca tırmanıyor.", x: 88, y: ytr, boy: 64, renk: KREM,
    sozcukler: pen("Bak,", 50.32, 4) }));

  // 47,3–48,6 ağaç (460 px); 48,4 kedi (150 px) gövde boyunca aşağıdan ortaya tırmanır
  const TX = 80, TY = 810, TB = 460;
  S.koy(S.cizim({
    svg: agac, kutu: { x: TX, y: TY, w: TB, h: TB }, ad: "agac", esik: 0.01,
    enCok: 40, w: 4.2, tb: 47.3,
    sure: 1.3, olayEnCok: 8, nefes: false }));
  S.koy(S.parilti(TX + TB - 30, TY + 70, 48.65, 30));
  const KB = 150, kcx = TX + TB / 2, kx = kcx - KB / 2, ky0 = TY + TB - KB + 32;
  const fTir = S.fr(49.15), fTirSon = S.fr(50.5), MES = 245;
  const kg = S.cizim({
    svg: kedi, kutu: { x: kx, y: ky0, w: KB, h: KB }, ad: "kedi", esik: 0.01,
    enCok: 30, w: 4.6,
    tb: 48.4, sure: 0.6, olayEnCok: 2, nefes: false });
  kg.dolgu = { nokta: kg.yollar, renk: RT.zemin, fb: S.fr(48.4) };
  kg.donusum = (f) => {
    const u = kis((f - fTir) / (fTirSon - fTir)), e = yavasla(u);
    const fi = Math.min(f, ICERIK), son = f >= fTirSon;
    const sal = u > 0 ? (son ? 0 : 4 * Math.sin(u * Math.PI * 6)) : 0;
    const dur = son ? 2 * Math.sin((fi - fTirSon) / 22) : 0;
    return { cx: kcx, cy: ky0 + KB - 8, tx: sal, ty: -MES * e + dur,
      dondur: u > 0 && !son ? 0.052 * Math.sin(u * Math.PI * 6) : 0, olcek: 1 };
  };
  S.koy(kg);
  const yz = TY + TB + 8;
  [[[kcx - 22, yz], [kcx - 48, yz + 14]],
   [[kcx + 4, yz + 5], [kcx + 4, yz + 28]],
   [[kcx + 30, yz], [kcx + 54, yz + 14]]]
    .forEach((p, i) => {
      const d = S.darbe(
        p, { duz: true, w: 3.6, renk: IKINCIL, alfa: 0.8, uc0: 4, uc1: 8, tohum: 80 + i },
        49.15 + i * 0.05, 0.15, i === 0 ? 0.45 : false);
      const f0 = S.fr(49.95), oc = d.ciz;
      d.ciz = (ctx, f) => {
        d.carpan = 1 - kis((f - f0) / 8); if (d.carpan > 0) oc(ctx, f);
      };
      S.koy(d);
    });

  // 52,88–54,52 etiket sütunu (sağ): Look! / Listen! / Watch out! el kutusunda;
  // 57,12 "= şimdi"
  const RX = 610, bh = 80, lfn = CV(64);
  // pencereler: Look! 52,88–53,52 · Listen! 53,60–54,40 ·
  // Watch 54,52–54,72 (uzatıldı) · out 54,72–55,04
  [["Look!", 52.88, 830, pen("Look,", 52.88, 1)], ["Listen!", 53.6, 925, pen("listen,", 53.6, 1)],
    ["Watch out!", 54.52, 1020, pen("watch", 54.52, 2)]]
    .forEach(([m, tb, yy, soz], i) => {
    const w = olc(lfn, m) + 56;
    S.koy(S.darbeler(
      kutu(RX, yy, w, bh, 30 + i), { w: 4, renk: KREM, uc0: 8, uc1: 14 },
      tb, 0.1, 0.06, false
    ));
    S.koy(S.elYazisi({ metin: m, x: RX + 28, y: yy + 58, boy: 64, renk: KREM, sozcukler: soz }));
  });
  // 57,12 anlatımsız formül etiketi `= şimdi`: hedef 0,5 sn → 57,62; alt çizgi 57,70
  const sx = RX + 30, sy = 1170;
  const ey = S.elYazisi({ metin: "= şimdi", x: sx, y: sy, boy: 84, renk: SARI, tb: 57.12,
    sure: 0.5 });
  S.koy(ey);
  const sw = ey.w;
  S.koy(S.darbe([[sx, sy + 18], [sx + sw * 0.5, sy + 14], [sx + sw, sy + 19]],
    { w: 8, renk: RT.vurguDolgu, alfa: 0.85, uc0: 8, uc1: 14, duz: true }, 57.7, 0.3, 0.55));
  S.koy(S.parilti(sx + sw + 40, sy - 60, 58.0, 30));

  // 59,37–59,69 is / climbing halka; formül is + climb-ing (Fredoka 110); 61,14 be + V-ing
  S.koy(S.halka(kel("is"), 59.37, 0.3, 21));
  S.koy(S.halka(kel("climbing"), 59.69, 0.3, 22));
  S.koy(S.metinPop({
    parca: [["is", KREM], [" + ", IKINCIL], ["climb", KREM], ["-ing", SARI]],
    x: 540, y: 1364,
    font: FF(110), hiza: "orta", tb: 60.0, sure: 0.4, ses: 0.8, turu: "vurus" }));
  // 61,14 anlatımsız formül etiketi `be + V-ing`: hedef 0,7 sn → 61,84
  S.koy(S.elYazisi({ metin: "be + V-ing", x: RX + 30, y: 1255, boy: 72, renk: IKINCIL,
    tb: 61.14, sure: 0.7 }));
}

surucu(kur, (f) => S.kare(f), KARE);

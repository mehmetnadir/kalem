// SAHNE 11 (DİKEY) — Tuzak cevabı: düz canvas, 1080x1920, 657 kare, t_bas 183,79; cümle 13.
// Zaman yalnız kare numarasından; sözcük zamanları sozcukler.json'dan gelir.
// İki kart: I am living in İstanbul (for now) / I live in İstanbul (always).
// Zaman çizgileri ve aralarında "≠ meaning" sarı belirteci yer alır.
import { surucu } from "/ortak/surucu.js";
import {
  Sahne, RT, renkCoz, ok, altCizgi, lerp, yavasla
} from "./sahne-ortak.js";
import { yaziNoktalari }
  from "/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js";

const KARE = 657, TBAS = 183.79, ICERIK = 645;
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, klasor: "11-canvas-tuzak-cevap", cumle: 13
});
const KOKDIZ = "/projeler/02-04-ydt-temel-dikey/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();

const FF = (b) => `700 ${b}px Fredoka`;
const t = (i) => S.sozc[i].t0;

const eyGen = (m, b) => yaziNoktalari(m, S.EY.G, {
  upm: S.EY.M.unitsPerEm, asc: S.EY.M.ascender, boy: b, x: 0, taban: 0
}).gen;

function nowNokta(cx, cy, tb) {
  const fb = S.fr(tb);
  S.bas(fb);
  S.olay(fb, "tik", 0.4);
  return {
    ciz(ctx, f) {
      const u = yavasla((f - fb) / 7.5);
      if (u <= 0) return;
      const r = 13 * lerp(0.6, 1, u);
      ctx.save();
      ctx.globalAlpha = u;
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, Math.PI * 2);
      ctx.fillStyle = renkCoz(RT.vurgu);
      ctx.fill();
      ctx.lineWidth = 5;
      ctx.strokeStyle = renkCoz(RT.zemin);
      ctx.stroke();
      ctx.restore();
    }
  };
}

function esitDegil(tb, nx0) {
  const NE = 72, ncy = 814;
  const p1 = [[nx0, ncy - 15], [nx0 + NE, ncy - 15]];
  const p2 = [[nx0, ncy + 15], [nx0 + NE, ncy + 15]];
  const p3 = [[nx0 + NE * 0.68, ncy - 38], [nx0 + NE * 0.32, ncy + 38]];
  [p1, p2, p3].forEach((p, i) => {
    S.koy(S.darbe(
      p,
      { duz: true, w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 4, uc1: 6, tohum: 300 + i },
      tb + i * 0.1,
      0.16,
      i ? false : 0.5
    ));
  });
}

function notOk(yb, tb, tohum) {
  S.koy(S.darbeler(
    ok([88, yb - 18], [152, yb - 18], tohum),
    { w: 6, renk: RT.murekkep, uc0: 6, uc1: 10 },
    tb,
    0.16,
    0.06,
    0.4
  ));
}

function zamanCizgisi({ TY, bant, tEksen, tNokta, tBant, bantSure, tohum, nowY }) {
  S.koy(S.darbe(
    [[bant[0], TY], [bant[1], TY]],
    { duz: true, w: 30, renk: RT.vurguDolgu, alfa: 0.45, uc0: 4, uc1: 8, tohum },
    tBant,
    bantSure,
    0.5
  ));
  const [, u1, u2] = ok([96, TY], [984, TY], tohum + 1);
  S.koy(S.darbeler(
    [[[96, TY], [984, TY]], u1, u2],
    { duz: true, w: 4, renk: RT.ikincil, uc0: 6, uc1: 12 },
    tEksen,
    0.4,
    0.15,
    0.4
  ));
  bant.forEach((x, i) => {
    S.koy(S.darbe(
      [[x, TY - 24], [x, TY + 24]],
      { duz: true, w: 6, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: tohum + 4 + i },
      tBant + bantSure * 0.5 + i * 0.12,
      0.18,
      i ? false : 0.4
    ));
  });
  S.koy(nowNokta(760, TY, tNokta));
  S.koy(S.nabiz(760, TY, 14, tNokta + 0.35));
  const gNow = eyGen("now", 64);
  S.koy(S.elYazisi({
    metin: "now",
    x: 760 - gNow / 2,
    y: nowY,
    boy: 64,
    renk: RT.murekkep,
    tb: tNokta + 0.08,
    sure: 0.4,
    ses: false
  }));
}

function donenAlti(pts, o, tb, tDon, ses) {
  const dS = S.darbe(pts, { ...o, renk: RT.vurgu }, tb, 0.4, ses);
  const dI = S.darbe(pts, { ...o, renk: RT.ikincil }, tb, 0.4, false);
  const fDon = S.fr(tDon);
  return {
    ciz(ctx, f) {
      const u = yavasla((f - fDon) / 9);
      if (u <= 0) {
        dS.ciz(ctx, f);
        return;
      }
      dI.carpan = u;
      dI.ciz(ctx, f);
      if (u < 1) {
        dS.carpan = 1 - u;
        dS.ciz(ctx, f);
      }
    }
  };
}

async function kur() {
  await S.kur();
  if (S.sozc.length !== 39) {
    throw new Error(`Beklenen 39 sözcük, gelen ${S.sozc.length}`);
  }

  const basSvg = await svgOku("peeps-kit/ogrenci-bas.svg");

  const ist = (w) => ({ ...w, sozcuk: w.sozcuk.replace(/^Istanbul/, "İstanbul") });
  const a = S.sozc.slice(4, 9).map(ist);
  const b = S.sozc.slice(18, 22).map(ist);

  // 184,20 (cevap öncesi): Öğrenci başı sağ altta belirir
  const og = S.koy(S.cizim({
    svg: basSvg,
    ad: "ogrenci",
    kutu: { x: 892, y: 1222, w: 117, h: 160 },   // QA tur 1: 1228 → 1222 (sallama tepesi ≤ 1392)
    esik: 0.004,
    enCok: 60,
    w: 4,
    tb: 184.2,
    sure: 0.55,
    olayEnCok: 3,
    nefes: false
  }));

  // 184,54 Olur,: Kart 1 çerçevesi
  S.koy(S.kart({
    x: 48,
    y: 380,
    w: 984,
    h: 140,
    tb: t(0),
    ad: "kart-1",
    tohum: 11,
    kutuSure: 0.2,
    kutuAralik: 0.12,
    satirlar: []
  }));

  // 185,90 anlam: ≠ üç sarı darbe
  const wM = eyGen("meaning", 88);
  const nx0 = 540 - (72 + 26 + wM) / 2;
  esitDegil(t(2), nx0);

  // 186,22 değişir.: meaning el yazısı
  const nM = S.koy(S.elYazisi({
    metin: "meaning",
    x: nx0 + 72 + 26,
    y: 840,
    boy: 88,
    renk: RT.murekkep,
    tb: t(3),
    sure: 0.6
  }));

  // 187,11 I: Kart 1 cümlesi (I am living in İstanbul.)
  const c1 = S.koy(S.cumleYaz({
    sozcukler: a,
    x: 88,
    y: 460,
    font: FF(72),
    satirH: 92,
    satirSay: [5],
    bosluk: 6
  }));

  // 189,12 Şimdilik: Not oku ve for now el yazısı
  notOk(592, t(9), 231);
  S.koy(S.elYazisi({
    metin: "for now",
    x: 172,
    y: 592,
    boy: 64,
    renk: RT.murekkep,
    tb: t(9) + 0.18,
    sure: 0.5
  }));

  // 189,68 İstanbul'da: Zaman çizgisi 1 (kısa bant)
  zamanCizgisi({
    TY: 670,
    bant: [690, 830],
    tEksen: t(10),
    tNokta: 190.0,
    tBant: t(11),
    bantSure: 0.4,
    tohum: 600,
    nowY: 730
  });

  // 191,55 Geçici.: (temporary) el yazısı
  const nTmp = S.koy(S.elYazisi({
    metin: "(temporary)",
    x: 172 + eyGen("for now", 64) + 20,
    y: 592,
    boy: 64,
    renk: RT.murekkep,
    tb: t(13),
    sure: 0.75
  }));

  // 192,48 Ailenle: Kart 2 çerçevesi
  S.koy(S.kart({
    x: 48,
    y: 910,
    w: 984,
    h: 140,
    tb: t(14),
    ad: "kart-2",
    tohum: 12,
    kutuSure: 0.2,
    kutuAralik: 0.12,
    satirlar: []
  }));

  // 192,48 Ailenle: Zaman çizgisi 2 (uzun bant)
  zamanCizgisi({
    TY: 1196,
    bant: [150, 880],
    tEksen: t(14),
    tNokta: 192.9,
    tBant: t(16),
    bantSure: 0.85,
    tohum: 620,
    nowY: 1256
  });

  // 193,12 hep: Not oku ve always el yazısı
  notOk(1120, t(15), 241);
  S.koy(S.elYazisi({
    metin: "always",
    x: 172,
    y: 1120,
    boy: 64,
    renk: RT.murekkep,
    tb: t(15) + 0.16,
    sure: 0.45
  }));

  // 193,95 yaşıyorsan:: (permanent) el yazısı
  const nPer = S.koy(S.elYazisi({
    metin: "(permanent)",
    x: 172 + eyGen("always", 64) + 20,
    y: 1120,
    boy: 64,
    renk: RT.murekkep,
    tb: 193.95,
    sure: 0.7
  }));

  // 194,89 I: Kart 2 cümlesi (I live in İstanbul.)
  const c2 = S.koy(S.cumleYaz({
    sozcukler: b,
    x: 88,
    y: 990,
    font: FF(72),
    satirH: 92,
    satirSay: [4],
    bosluk: 6
  }));

  // 197,70 yor: Odak am living altçizgisi
  const A = c1.kel[1], B = c1.kel[2];
  S.koy(donenAlti(
    altCizgi(A.x - 6, B.x + B.w + 6, B.y + 0.48 * 72, 11),
    { w: 9, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 },
    t(23),
    t(31),
    0.55
  ));

  // 197,78 yor: Odak live altçizgisi
  const L = c2.kel[1];
  S.koy(donenAlti(
    altCizgi(L.x - 6, L.x + L.w + 6, L.y + 0.48 * 72, 12),
    { w: 9, alfa: 0.9, uc0: 8, uc1: 14, tohum: 502 },
    t(23) + 0.08,
    t(31),
    false
  ));

  // 201,30 ayrılır.: meaning sarı altçizgisi
  S.koy(S.darbe(
    altCizgi(nM.x - 6, nM.x + nM.w + 10, 840 + 0.52 * 88, 13),
    { w: 10, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 503 },
    t(31),
    0.4,
    0.55
  ));

  // 202,30 (cevap bitimi): Öğrenci baş sallama dönüşümü
  const fSal = S.fr(202.3);
  og.donusum = (f) => {
    const p = (f - fSal) / 30;
    const ty = p > 0 && p < 1 ? 160 * 0.06 * Math.sin(Math.PI * 2 * p) ** 2 : 0;
    return { cx: 892 + 58.5, cy: 1222 + 160, tx: 0, ty, dondur: 0, olcek: 1 };
  };

  // 202,74 Kalıcı: (permanent) sarı altçizgisi
  S.koy(S.darbe(
    altCizgi(nPer.x - 6, nPer.x + nPer.w + 10, 1120 + 0.52 * 64, 14),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 504 },
    t(32),
    0.4,
    0.5
  ));

  // 203,46 geçici: (temporary) sarı altçizgisi
  S.koy(S.darbe(
    altCizgi(nTmp.x - 6, nTmp.x + nTmp.w + 10, 592 + 0.52 * 64, 15),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 505 },
    t(34),
    0.4,
    0.5
  ));
}

surucu(kur, (f) => S.kare(f), KARE);

// SAHNE 09 (DİKEY) — Karşıt 2/2: düz canvas, 1080x1920, 523 kare, t_bas 145,29; cümle 10.
// Zaman yalnız kare numarasından; sözcük zamanları sozcukler.json'dan.
import { surucu } from "/ortak/surucu.js";
import {
  Sahne, RT, renkCoz, elips, ok, kutu, altCizgi, lerp, yavasla, geriTasma, olc, altY
} from "./sahne-ortak.js";
import { yaziNoktalari }
  from "/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js";

const KARE = 523, TBAS = 145.29, ICERIK = 511;
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, klasor: "09-canvas-karsit2", cumle: 10
});

const FF = (b) => `700 ${b}px Fredoka`;
const FC = (b) => `700 ${b}px Caveat`;
const t = (i) => S.sozc[i].t0;
const t1 = (i) => S.sozc[i].t1;

const eyGen = (m, b) => yaziNoktalari(m, S.EY.G, {
  upm: S.EY.M.unitsPerEm, asc: S.EY.M.ascender, boy: b, x: 0, taban: 0
}).gen;

const EKRAN = { Izmir: "İzmir", seven: "7", "p.m.": "pm" };
const goster = (d) => d.map((s) => ({ ...s, sozcuk: EKRAN[s.sozcuk] || s.sozcuk }));

const HZ = 144.0;
const NY = 860;
const TY = 1180, AX0 = 96, AX1 = 984;
const NX = 360, X7 = 780;
const ETY = 1240, EY = 1370;

function nowNokta(cx, cy, tb) {
  const fb = S.fr(tb);
  S.bas(fb);
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

let gizli, gizliCtx;

function grupKucul(ogeler, t0, sure) {
  const duzOgeler = ogeler.flat(Infinity);
  const f0 = S.fr(t0), f1 = S.fr(t0 + sure);
  return {
    ciz(ctx, f) {
      if (f >= f1) return;
      if (f < f0) {
        for (const e of duzOgeler) e.ciz(ctx, f);
        return;
      }
      const u = yavasla((f - f0) / (sure * 30));
      const kk = typeof window !== "undefined" ? window.__kalemKutu : null;
      const eskiEkle = kk ? kk.ekle : null;
      if (kk) kk.ekle = () => {};
      gizliCtx.clearRect(0, 0, 1080, 1920);
      for (const e of duzOgeler) e.ciz(gizliCtx, f);
      if (kk && eskiEkle) kk.ekle = eskiEkle;

      ctx.save();
      ctx.globalAlpha = 1 - u;
      const s = lerp(1, 0.12, u);
      ctx.translate(540, 380);
      ctx.scale(s, s);
      ctx.translate(-540, -380);
      ctx.drawImage(gizli, 0, 0);
      ctx.restore();
    }
  };
}

const uzunluk = (p) => p.reduce((tot, q, k) => (
  k ? tot + Math.hypot(q[0] - p[k - 1][0], q[1] - p[k - 1][1]) : 0
), 0);

function elCizim(ad, parcalar, tb, sure, olayEnCok = 3) {
  const n = parcalar.length, xs = [], ys = [];
  parcalar.forEach(({ p }) => p.forEach(([x, y]) => {
    xs.push(x);
    ys.push(y);
  }));
  const kut = { x: Math.min(...xs) - 6, y: Math.min(...ys) - 6 };
  kut.w = Math.max(...xs) + 6 - kut.x;
  kut.h = Math.max(...ys) + 6 - kut.y;
  const cocuk = parcalar.map(({ p, o }, i) => {
    const dur = Math.min(sure * 0.5, 0.1 + uzunluk(p) / 1800);
    const bas = tb + (n > 1 ? i / (n - 1) : 0) * (sure - dur);
    return S.darbe(p, { uc0: 8, uc1: 14, ...o }, bas, dur, i < olayEnCok ? undefined : false);
  });
  const fb = S.fr(tb);
  return {
    ciz(ctx, f) {
      if (typeof window !== "undefined" && f >= fb + 2) {
        window.__kalemKutu?.ekle("cizim", ad, kut.x, kut.y, kut.w, kut.h);
      }
      for (const c of cocuk) c.ciz(ctx, f);
    }
  };
}

function nokta(cx, cy, r, tb, renk) {
  const fb = S.fr(tb);
  S.bas(fb);
  S.olay(fb, "tik", 0.45);
  return {
    ciz(ctx, f) {
      if (f < fb) return;
      const k = Math.max(0, geriTasma((f - fb) / 8));
      ctx.save();
      ctx.globalAlpha = 0.95;
      ctx.fillStyle = renkCoz(renk);
      ctx.beginPath();
      ctx.arc(cx, cy, r * k, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }
  };
}

function yayOk(a, b, h) {
  const c = [(a[0] + b[0]) / 2, Math.min(a[1], b[1]) - 2 * h];
  const g = [];
  for (let i = 0; i <= 24; i++) {
    const tVal = i / 24, m = 1 - tVal;
    g.push([
      m * m * a[0] + 2 * m * tVal * c[0] + tVal * tVal * b[0],
      m * m * a[1] + 2 * m * tVal * c[1] + tVal * tVal * b[1]
    ]);
  }
  const dx = b[0] - c[0], dy = b[1] - c[1];
  const l = Math.hypot(dx, dy) || 1;
  const d = [dx / l, dy / l];
  const uc = (s) => {
    const ca = Math.cos(0.5 * s), sa = Math.sin(0.5 * s), q = 24;
    return [[b[0] - (d[0] * ca - d[1] * sa) * q, b[1] - (d[0] * sa + d[1] * ca) * q], b];
  };
  return [g, uc(1), uc(-1)];
}

function trenParcalari(ox, oy, s, k) {
  const P = (x, y) => [ox + s * x, oy + s * y];
  const K = (x, y, w, h, tohum) => kutu(ox + s * x, oy + s * y, s * w, s * h, tohum);
  const govde = { w: k.govde, renk: RT.murekkep };
  const ince = { w: k.ince, renk: RT.murekkep };
  const p = [];
  const ekle = (dizi, o) => dizi.forEach((q) => p.push({ p: q, o }));
  ekle(K(200, 55, 170, 75, 31), govde);
  ekle(K(200, 10, 75, 45, 32), govde);
  ekle(K(320, 22, 26, 33, 33), ince);
  p.push({ p: [P(370, 95), P(398, 130), P(370, 130)], o: { ...govde, duz: true } });
  ekle(K(0, 45, 175, 85, 34), govde);
  p.push({ p: [P(175, 112), P(200, 112)], o: { ...ince, duz: true } });
  ekle(K(20, 60, 50, 30, 35), ince);
  ekle(K(100, 60, 50, 30, 36), ince);
  ekle(K(215, 20, 42, 25, 37), ince);
  [40, 135, 240, 335].forEach((x, i) => p.push({
    p: elips(ox + s * x, oy + s * 138, s * 17, s * 17, 0, 50 + i),
    o: govde
  }));
  p.push({ p: [P(-10, 158), P(420, 158)], o: { w: k.ray, renk: RT.ikincil, duz: true } });
  p.push({
    p: elips(ox + s * 345, oy + s * 2, s * 11, s * 9, 0.2, 61),
    o: { w: k.duman, renk: RT.ikincil }
  });
  p.push({
    p: elips(ox + s * 372, oy + s * -16, s * 8, s * 7, 0.3, 62),
    o: { w: k.duman - 0.2, renk: RT.ikincil }
  });
  return p;
}

const TISORT = [
  {
    n: [
      [37, 4], [14, 12], [0, 36], [14, 46], [24, 37], [24, 88],
      [76, 88], [76, 37], [86, 46], [100, 36], [86, 12], [63, 4]
    ],
    duz: true
  },
  { n: [[37, 4], [50, 14], [63, 4]] },
  { n: [[14, 12], [24, 37]], duz: true },
  { n: [[86, 12], [76, 37]], duz: true }
];

function tisortParcalari(x, y, w, h, kal) {
  const k = Math.min(w / 100, h / 90);
  const ox = x + (w - 100 * k) / 2;
  const oy = y + (h - 90 * k) / 2;
  return TISORT.map((d) => ({
    p: d.n.map(([a, b]) => [ox + a * k, oy + b * k]),
    o: { w: kal, renk: RT.murekkep, duz: d.duz }
  }));
}

function bantDolgu(x0, y0, x1, y1, tb, alfa) {
  const fb = S.fr(tb);
  S.bas(fb);
  const w = x1 - x0, h = y1 - y0;
  return {
    ciz(ctx, f) {
      if (f < fb) return;
      ctx.save();
      ctx.globalAlpha = alfa;
      ctx.fillStyle = renkCoz(RT.vurguDolgu);
      ctx.fillRect(x0, y0, w, h);
      ctx.restore();
    }
  };
}

function sonenOdak(x0, x1, y, tohum, tb, tSon, ses) {
  const pts = altCizgi(x0, x1, y, tohum);
  const ayar = { w: 9, alfa: 0.9, uc0: 8, uc1: 14, tohum: 500 + tohum };
  const sari = S.darbe(pts, { ...ayar, renk: RT.vurgu }, tb, 0.4, ses);
  const ikincil = S.darbe(pts, { ...ayar, renk: RT.ikincil }, tb, 0.4, false);
  const fSon = S.fr(tSon);
  return {
    ciz(ctx, f) {
      if (f < fSon) sari.ciz(ctx, f);
      else ikincil.ciz(ctx, f);
    }
  };
}

const esitDegil = (cx, cy) => [
  [[cx - 24, cy - 13], [cx + 24, cy - 13]],
  [[cx - 24, cy + 13], [cx + 24, cy + 13]],
  [[cx + 13, cy - 36], [cx - 13, cy + 36]]
];

async function kur() {
  await S.kur();
  if (S.sozc.length !== 37) {
    throw new Error(`Beklenen 37 sözcük, gelen ${S.sozc.length}`);
  }

  gizli = document.createElement("canvas");
  gizli.width = 1080;
  gizli.height = 1920;
  gizliCtx = gizli.getContext("2d");

  // ===== Z — zaman çizgisi =====
  // 144,00 hazır: zaman ekseni today bandı
  S.koy(bantDolgu(200, 1040, 880, 1180, HZ, 0.32));

  // 144,00 hazır: bant uç çentikleri
  S.koy(S.darbe(
    [[200, 1040], [200, 1196]],
    { duz: true, w: 4.5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 212 },
    HZ,
    0.15,
    false
  ));
  S.koy(S.darbe(
    [[880, 1040], [880, 1196]],
    { duz: true, w: 4.5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 213 },
    HZ,
    0.15,
    false
  ));

  // 144,00 hazır: zaman ekseni oku
  const [, uc1Z, uc2Z] = ok([AX0, TY], [AX1, TY], 21);
  S.koy(S.darbeler(
    [[[AX0, TY], [AX1, TY]], uc1Z, uc2Z],
    { duz: true, w: 4, renk: RT.ikincil, uc0: 6, uc1: 12 },
    HZ,
    0.3,
    0.1,
    false
  ));

  // 144,00 hazır: now noktası ve nabız
  S.koy(nowNokta(NX, TY, HZ));
  S.koy(S.nabiz(NX, TY, 14, HZ));

  // 144,00 hazır: now etiketi
  S.koy(S.elYazisi({
    metin: "now",
    x: NX - eyGen("now", 64) / 2,
    y: ETY,
    boy: 64,
    renk: RT.murekkep,
    tb: HZ,
    sure: 0.3,
    ses: false
  }));

  // ===== H — sahne 08'in son düzeni =====
  const ogelerH = [];

  // 144,00 hazır: 08 üst notu today
  const eH1 = S.elYazisi({
    metin: "today",
    x: 88,
    y: 450,
    boy: 80,
    renk: RT.murekkep,
    tb: HZ,
    sure: 0.3,
    ses: false
  });
  ogelerH.push(eH1);

  // 144,00 hazır: 08 today söndü altçizgi
  ogelerH.push(S.darbe(
    altCizgi(84, 92 + eH1.w, 479, 2),
    { w: 7, renk: RT.ikincil, alfa: 0.9, uc0: 8, uc1: 14, tohum: 562 },
    HZ,
    0.3,
    false
  ));

  // 144,00 hazır: 08 kart çerçevesi
  ogelerH.push(...S.darbeler(
    kutu(48, 490, 984, 270, 91),
    { w: 4, renk: RT.ikincil, uc0: 10, uc1: 18 },
    HZ,
    0.1,
    0.05,
    false
  ));

  // 144,00 hazır: 08 cümle metni
  ogelerH.push(S.metinPop({
    parca: [["She is wearing her", RT.murekkep]],
    x: 88,
    y: 600,
    font: FF(72),
    tb: HZ,
    sure: 0.3
  }));
  ogelerH.push(S.metinPop({
    parca: [["pink T-shirt today.", RT.murekkep]],
    x: 88,
    y: 700,
    font: FF(72),
    tb: HZ,
    sure: 0.3
  }));

  // 144,00 hazır: 08 tişört çizimi
  ogelerH.push(elCizim("tisort", tisortParcalari(772, 526, 220, 198, 4.6), HZ, 0.3, 0));

  // 144,00 hazır: 08 tişört halkası
  ogelerH.push(S.darbe(
    elips(882, 625, 128, 116, -0.05, 31),
    { w: 6, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 },
    HZ,
    0.3,
    false
  ));

  // 144,00 hazır: 08 is wearing altçizgi
  const x0H7 = 88 + olc(FF(72), "She ") - 6;
  const x1H7 = 88 + olc(FF(72), "She is wearing") + 6;
  const yH7 = altY(600, 72, "wearing");
  ogelerH.push(S.darbe(
    altCizgi(x0H7, x1H7, yH7, 3),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 503 },
    HZ,
    0.4,
    false
  ));

  // 144,00 hazır: 08 pink T-shirt today söndü altçizgi
  const x0H8 = 88 + olc(FF(72), "pink T-shirt ") - 6;
  const x1H8 = x0H8 + olc(FF(72), "today") + 12;
  const yH8 = altY(700, 72, "today");
  ogelerH.push(S.darbe(
    altCizgi(x0H8, x1H8, yH8, 1),
    { w: 9, renk: RT.ikincil, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 },
    HZ,
    0.4,
    false
  ));

  // 144,00 hazır: 08 not satırı today -> this day only
  const eH9 = S.elYazisi({
    metin: "today",
    x: 88,
    y: NY,
    boy: 72,
    renk: RT.murekkep,
    tb: HZ,
    sure: 0.3,
    ses: false
  });
  ogelerH.push(eH9);
  const oxH9 = 88 + eH9.w + 18;
  ogelerH.push(...S.darbeler(
    ok([oxH9, NY - 20], [oxH9 + 56, NY - 20], 7),
    { duz: true, w: 4.5, renk: RT.murekkep, uc0: 4, uc1: 6 },
    HZ,
    0.1,
    0.03,
    false
  ));
  ogelerH.push(S.elYazisi({
    metin: "this day only",
    x: oxH9 + 74,
    y: NY,
    boy: 72,
    renk: RT.murekkep,
    tb: HZ,
    sure: 0.3,
    ses: false
  }));

  // ===== G — küçülme =====
  // 145,72 küçülme: 08 düzeni şeride küçülür
  S.koy(grupKucul(ogelerH, 145.72, 0.24));

  // ===== B — yeni kart =====
  // 145,80 kart: yeni kart çerçevesi
  S.koy(S.kart({
    x: 48,
    y: 490,
    w: 984,
    h: 270,
    tb: 145.80,
    ad: "kart",
    tohum: 2,
    kutuSure: 0.12,
    kutuAralik: 0.06,
    satirlar: []
  }));

  // 145,84 The: yeni kart cümlesi
  const cum = S.koy(S.cumleYaz({
    sozcukler: goster(S.sozc.slice(0, 9)),
    x: 88,
    y: 600,
    font: FF(72),
    satirH: 100,
    satirSay: [4, 5],
    bosluk: 6
  }));

  // 146,00 train: tren simgesi
  S.koy(elCizim(
    "tren",
    trenParcalari(732, 521, 0.62, { govde: 4.2, ince: 3.6, ray: 3.6, duman: 3.2 }),
    t(1),
    0.9
  ));

  // ===== Ş — şerit =====
  // 145,92 şerit: üst şerit çerçevesi
  S.koy(S.kart({
    x: 48,
    y: 352,
    w: 984,
    h: 120,
    tb: 145.92,
    ad: "serit",
    tohum: 8,
    kutuSure: 0.1,
    kutuAralik: 0.05,
    satirlar: []
  }));

  let seritBoy = 56;
  let wWearing = olc(FF(seritBoy), "is wearing … today");
  let wOnly = olc(FC(seritBoy), "this day only");
  if (88 + wWearing + 100 + wOnly > 910) {
    seritBoy = 52;
    wWearing = olc(FF(seritBoy), "is wearing … today");
  }
  const xL = 88 + wWearing;

  // 145,96 şerit: is wearing … today metni
  S.koy(S.metinPop({
    parca: [["is wearing … today", RT.murekkep]],
    x: 88,
    y: 430,
    font: FF(seritBoy),
    tb: 145.96,
    sure: 0.3,
    ses: 0.4
  }));

  // 146,02 şerit: şerit oku
  S.koy(S.darbeler(
    ok([xL + 20, 410], [xL + 80, 410], 23),
    { w: 5, renk: RT.ikincil, uc0: 6, uc1: 10 },
    146.02,
    0.16,
    0.06,
    false
  ));

  // 146,08 şerit: this day only metni
  S.koy(S.metinPop({
    parca: [["this day only", RT.murekkep]],
    x: xL + 100,
    y: 430,
    font: FC(seritBoy),
    tb: 146.08,
    sure: 0.3,
    ses: false
  }));

  // 146,04 şerit: tişört simgesi
  S.koy(elCizim("tisort-simge", tisortParcalari(922, 368, 96, 86, 3.4), 146.04, 0.35, 1));

  // ===== N — not satırı ve 7 pm =====
  // 149,69 today: not satırı today + 7 pm
  const eN1 = S.koy(S.elYazisi({
    metin: "today + 7 pm",
    x: 88,
    y: NY,
    boy: 72,
    renk: RT.murekkep,
    sozcukler: [
      { t0: t(10), t1: t1(10) },
      { t0: t(13), t1: t(13) + 0.22 },
      { t0: t(13) + 0.26, t1: t(13) + 0.42 },
      { t0: t(13) + 0.44, t1: t1(13) }
    ]
  }));

  // 150,57 saatle: 7 pm sönen odak
  const kel7 = cum.kel[6];
  const kelPm = cum.kel[7];
  S.koy(sonenOdak(
    kel7.x - 6,
    kelPm.x + kelPm.w + 6,
    altY(kelPm.y, 72, "7 pm"),
    11,
    t(12),
    t(24),
    0.55
  ));

  // 151,85 akşam: zaman ekseni 7 pm çentiği ve noktası
  S.koy(S.darbe(
    [[X7, TY - 16], [X7, TY + 16]],
    { duz: true, w: 5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 211 },
    t(14),
    0.15,
    0.45
  ));
  S.koy(nokta(X7, TY, 10, t(14) + 0.1, RT.murekkep));

  // 152,25 yedi.: 7 pm etiketi
  S.koy(S.elYazisi({
    metin: "7 pm",
    x: X7 - eyGen("7 pm", 64) / 2,
    y: ETY,
    boy: 64,
    renk: RT.murekkep,
    sozcukler: [
      { t0: t(15), t1: t(15) + 0.3 },
      { t0: t(15) + 0.32, t1: t(16) - 0.05 }
    ]
  }));

  // 153,45 henüz: now -> 7 pm yayı
  const [yayG, ucYay1, ucYay2] = yayOk([NX + 14, TY - 20], [X7 - 8, TY - 22], 50);
  S.koy(S.darbe(yayG, { w: 4.6, renk: RT.ikincil, uc0: 6, uc1: 8, tohum: 220 }, t(17), 0.8, 0.5));
  S.koy(S.darbe(
    ucYay1,
    { w: 4.6, renk: RT.ikincil, uc0: 6, uc1: 8, duz: true, tohum: 221 },
    t(17) + 0.75,
    0.12,
    false
  ));
  S.koy(S.darbe(
    ucYay2,
    { w: 4.6, renk: RT.ikincil, uc0: 6, uc1: 8, duz: true, tohum: 222 },
    t(17) + 0.75,
    0.12,
    false
  ));

  // 154,93 tarifede: not satırı oku
  const oxN = 88 + eN1.w + 18;
  S.koy(S.darbe(
    [[oxN, NY - 20], [oxN + 56, NY - 20]],
    { duz: true, w: 4.5, renk: RT.murekkep, uc0: 4, uc1: 6, tohum: 240 },
    t(20),
    0.2,
    0.45
  ));
  const [, ucN1, ucN2] = ok([oxN, NY - 20], [oxN + 56, NY - 20], 240);
  S.koy(S.darbe(
    ucN1,
    { duz: true, w: 4.5, renk: RT.murekkep, uc0: 4, uc1: 6, tohum: 241 },
    t(20) + 0.18,
    0.08,
    false
  ));
  S.koy(S.darbe(
    ucN2,
    { duz: true, w: 4.5, renk: RT.murekkep, uc0: 4, uc1: 6, tohum: 242 },
    t(20) + 0.18,
    0.08,
    false
  ));

  // 155,23 yazılı.: not satırı timetable
  S.koy(S.elYazisi({
    metin: "timetable",
    x: oxN + 74,
    y: NY,
    boy: 72,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(20) + 0.3, t1: t1(21) - 0.05 }]
  }));

  // ===== O — odak =====
  // 156,09 Geniş: leaves kalıcı odak
  const kelLeaves = cum.kel[4];
  S.koy(S.darbe(
    altCizgi(
      kelLeaves.x - 6, kelLeaves.x + kelLeaves.w + 6, altY(kelLeaves.y, 72, kelLeaves.m), 12
    ),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 502 },
    t(22),
    0.4,
    0.55
  ));

  // 157,21 Today: iki today eşzamanlı odak
  const xsSerit = 88 + olc(FF(seritBoy), "is wearing … ");
  const wsSerit = olc(FF(seritBoy), "today");
  S.koy(S.darbe(
    altCizgi(xsSerit - 6, xsSerit + wsSerit + 6, altY(430, seritBoy, "today"), 3),
    { w: 8, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 503 },
    t(24),
    0.4,
    0.55
  ));
  const kelToday = cum.kel[8];
  const wTodayKart = olc(FF(72), "today");
  S.koy(S.darbe(
    altCizgi(kelToday.x - 6, kelToday.x + wTodayKart + 6, altY(kelToday.y, 72, "today"), 4),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 504 },
    t(24),
    0.4,
    false
  ));

  // ===== E — alt satır =====
  // 159,05 Farkı: eşit değil simgesi
  esitDegil(570, 1346).forEach((p, i) => {
    S.koy(S.darbe(
      p,
      { duz: true, w: 7, renk: RT.murekkep, alfa: 0.9, uc0: 4, uc1: 8, tohum: 700 + i },
      t(29) + i * 0.12,
      0.14,
      i ? false : 0.5
    ));
  });

  // 160,57 konuşma: RIGHT NOW etiketi
  S.koy(S.elYazisi({
    metin: "RIGHT NOW",
    x: NX - eyGen("RIGHT NOW", 64) / 2,
    y: EY,
    boy: 64,
    renk: RT.murekkep,
    sozcukler: [
      { t0: t(32), t1: t1(32) },
      { t0: t(33), t1: t1(33) }
    ]
  }));

  // 161,61 tarife: TIMETABLE etiketi
  S.koy(S.elYazisi({
    metin: "TIMETABLE",
    x: X7 - eyGen("TIMETABLE", 64) / 2,
    y: EY,
    boy: 64,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(35), t1: t(35) + 0.5 }]
  }));
}

surucu(kur, (f) => S.kare(f), KARE);

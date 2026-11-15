// SAHNE 05 (DİKEY) — Örnek 3/3: düz canvas, 1080x1920, 747 kare, t_bas 68,84; cümle 5.
// Zaman yalnız kare numarasından; sözcük zamanları sozcukler.json'dan.
import { surucu } from "/ortak/surucu.js";
import {
  Sahne, RT, renkCoz, elips, ok, kutu, altCizgi, lerp, yavasla, geriTasma, olc, altY
} from "./sahne-ortak.js";
import { yaziNoktalari }
  from "/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js";

const KARE = 747, TBAS = 68.84, ICERIK = 735;
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, klasor: "05-canvas-ornek3", cumle: 5
});

const FF = (b) => `700 ${b}px Fredoka`;
const FC = (b) => `700 ${b}px Caveat`;
const t = (i) => S.sozc[i].t0;

const eyGen = (m, b) => yaziNoktalari(m, S.EY.G, {
  upm: S.EY.M.unitsPerEm, asc: S.EY.M.ascender, boy: b, x: 0, taban: 0
}).gen;

const EKRAN = { Izmir: "İzmir", seven: "7", "p.m.": "pm" };
const goster = (d) => d.map((s) => ({ ...s, sozcuk: EKRAN[s.sozcuk] || s.sozcuk }));

const TY = 1310, AX0 = 96, AX1 = 984, NX = 250, X7 = 580, XT = 850, ETY = 1376;
const anaTren = { govde: 4.6, ince: 4.0, ray: 4.0, duman: 3.6 };
const simgeTren = { govde: 3.4, ince: 3.0, ray: 3.0, duman: 2.8 };

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

function yayCiz(x, h, tb, sure, tohum) {
  const [g, uc1, uc2] = yayOk([NX + 14, TY - 20], [x - 8, TY - 22], h);
  S.koy(S.darbe(g, { w: 4.6, renk: RT.ikincil, uc0: 6, uc1: 8, tohum }, tb, sure, 0.5));
  S.koy(S.darbe(
    uc1,
    { w: 4.6, renk: RT.ikincil, uc0: 6, uc1: 8, duz: true, tohum: tohum + 1 },
    tb + sure - 0.05,
    0.12,
    false
  ));
  S.koy(S.darbe(
    uc2,
    { w: 4.6, renk: RT.ikincil, uc0: 6, uc1: 8, duz: true, tohum: tohum + 2 },
    tb + sure - 0.05,
    0.12,
    false
  ));
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

function saatParcalari(cx, cy, r) {
  const p = [{ p: elips(cx, cy, r, r * 0.97, 0.05, 41), o: { w: 4.8, renk: RT.murekkep } }];
  [[0, -1], [1, 0], [0, 1], [-1, 0]].forEach(([a, b]) => p.push({
    p: [[cx + a * r * 0.8, cy + b * r * 0.8], [cx + a * r * 0.66, cy + b * r * 0.66]],
    o: { w: 4.4, renk: RT.murekkep, duz: true, uc0: 2, uc1: 3 }
  }));
  p.push({
    p: [[cx, cy], [cx, cy - r * 0.66]],
    o: { w: 4.8, renk: RT.murekkep, duz: true, uc0: 3, uc1: 5 }
  });
  const aci = (7 / 12) * Math.PI * 2;
  p.push({
    p: [[cx, cy], [cx + Math.sin(aci) * r * 0.5, cy - Math.cos(aci) * r * 0.5]],
    o: { w: 10, renk: RT.vurgu, duz: true, uc0: 3, uc1: 6 }
  });
  return p;
}

function biletParcalari(cx, cy, egim, s) {
  const ce = Math.cos(egim), se = Math.sin(egim);
  const R = ([x, y]) => [
    cx + (s * x) * ce - (s * y) * se,
    cy + (s * x) * se + (s * y) * ce
  ];
  const yay = (x0, yon) => Array.from({ length: 13 }, (_, i) => {
    const a = -Math.PI / 2 + (i / 12) * Math.PI;
    return [x0 - yon * 22 * Math.cos(a), yon * 22 * Math.sin(a)];
  });
  const kenar = { w: 4.6, renk: RT.murekkep, duz: true, uc0: 6, uc1: 10 };
  const p = [
    { p: [[-180, -70], [180, -70]].map(R), o: kenar },
    { p: [[180, -70], [180, -22], ...yay(180, 1), [180, 70]].map(R), o: kenar },
    { p: [[180, 70], [-180, 70]].map(R), o: kenar },
    { p: [[-180, 70], [-180, 22], ...yay(-180, -1), [-180, -70]].map(R), o: kenar }
  ];
  for (let i = 0; i < 6; i++) {
    const y0 = -58 + i * 20;
    p.push({
      p: [[100, y0], [100, y0 + 11]].map(R),
      o: { w: 3.6, renk: RT.ikincil, duz: true, uc0: 2, uc1: 2 }
    });
  }
  [[-150, -30, 60], [-150, 0, 30], [-150, 30, 70]].forEach(([x0, y, x1]) => p.push({
    p: [[x0, y], [x1, y]].map(R),
    o: { w: 4.0, renk: RT.ikincil, duz: true, uc0: 4, uc1: 6 }
  }));
  return p;
}

async function kur() {
  await S.kur();
  if (S.sozc.length !== 49) {
    throw new Error(`Beklenen 49 sözcük, gelen ${S.sozc.length}`);
  }

  gizli = document.createElement("canvas");
  gizli.width = 1080;
  gizli.height = 1920;
  gizliCtx = gizli.getContext("2d");

  // --- Z: Zaman Çizgisi ---
  // 72,03 anlatıyor.: gelecek bandı
  S.koy(S.darbe(
    [[NX + 18, TY], [AX1 - 30, TY]],
    { duz: true, w: 26, renk: RT.vurguDolgu, alfa: 0.45, uc0: 4, uc1: 8, tohum: 201 },
    t(6),
    0.5,
    0.45
  ));

  // 71,55 geleceği: zaman ekseni
  const [, uc1Eksen, uc2Eksen] = ok([AX0, TY], [AX1, TY], 21);
  S.koy(S.darbeler(
    [[[AX0, TY], [AX1, TY]], uc1Eksen, uc2Eksen],
    { duz: true, w: 4, renk: RT.ikincil, uc0: 6, uc1: 12 },
    t(5),
    0.4,
    0.15,
    0.4
  ));

  // 71,80 geleceği: now noktası ve nabız
  S.koy(nowNokta(NX, TY, t(5) + 0.25));
  S.koy(S.nabiz(NX, TY, 14, t(5) + 0.60));

  // 71,95 geleceği: now etiketi
  S.koy(S.elYazisi({
    metin: "now",
    x: NX - eyGen("now", 64) / 2,
    y: ETY,
    boy: 64,
    renk: RT.murekkep,
    tb: t(5) + 0.40,
    sure: 0.4
  }));

  // 77,81 akşam: 7 pm çentiği ve noktası
  S.koy(S.darbe(
    [[X7, TY - 16], [X7, TY + 16]],
    { duz: true, w: 5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 211 },
    t(19),
    0.15,
    0.45
  ));
  S.koy(nokta(X7, TY, 10, t(19) + 0.1, RT.murekkep));

  // 77,81–78,53 akşam yedide: 7 pm el yazısı
  S.koy(S.elYazisi({
    metin: "7 pm",
    x: X7 - eyGen("7 pm", 64) / 2,
    y: ETY,
    boy: 64,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(19), t1: t(20) }, { t0: t(20), t1: t(21) }]
  }));

  // 78,53 kalkıyor.: now → 7 pm yayı
  yayCiz(X7, 26, t(21), 0.55, 220);

  // 87,75 akşam: tonight çentiği ve noktası
  S.koy(S.darbe(
    [[XT, TY - 16], [XT, TY + 16]],
    { duz: true, w: 5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 231 },
    t(39),
    0.15,
    0.45
  ));
  S.koy(nokta(XT, TY, 10, t(39) + 0.1, RT.murekkep));

  // 87,75–88,58 akşam sinemaya: tonight el yazısı
  S.koy(S.elYazisi({
    metin: "tonight",
    x: XT - eyGen("tonight", 64) / 2,
    y: ETY,
    boy: 64,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(39), t1: t(41) - 0.05 }]
  }));

  // 88,63 gidiyorum.: now → tonight yayı
  yayCiz(XT, 38, t(41), 0.65, 240);

  // --- A Evresi ---
  const ogelerA = [];

  // 72,60 —: Kart A çerçevesi
  ogelerA.push(S.kart({
    x: 48,
    y: 380,
    w: 984,
    h: 240,
    tb: 72.60,
    ad: "kartA",
    tohum: 4,
    kutuSure: 0.14,
    kutuAralik: 0.08,
    satirlar: []
  }));

  // 73,00–76,44 The … today.: Kart A cümlesi
  const sozcA = goster(S.sozc.slice(7, 16));
  const satirlarA = [
    sozcA.slice(0, 4).map((w) => w.sozcuk).join(" "),
    sozcA.slice(4, 9).map((w) => w.sozcuk).join(" ")
  ];
  const sayilarA = [4, 5];
  const boyA = satirlarA.some((s, i) => (
    olc(FF(72), s) + 6 * (sayilarA[i] - 1) > 904
  )) ? 64 : 72;
  const hA = boyA === 64 ? 84 : 92;
  const cumA = S.cumleYaz({
    sozcukler: sozcA,
    x: 88,
    y: 476,
    font: FF(boyA),
    satirH: hA,
    satirSay: [4, 5],
    bosluk: 6
  });
  ogelerA.push(cumA);

  // 73,16 train: tren çizimi
  ogelerA.push(elCizim("tren", trenParcalari(64, 747, 1.6, anaTren), t(8), 1.1));

  // 74,76 seven: saat çizimi
  ogelerA.push(elCizim("saat", saatParcalari(874, 850, 150), t(13), 0.6));

  // 80,37–81,83 tarifede: TIMETABLE el yazısı
  const eTT = S.elYazisi({
    metin: "TIMETABLE",
    x: 88,
    y: 1150,
    boy: 72,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(24), t1: t(26) - 0.1 }]
  });
  ogelerA.push(eTT);

  // 81,93 Tarifeli: TIMETABLE altçizgi
  ogelerA.push(S.darbe(
    altCizgi(84, 92 + eTT.w, altY(1150, 72, "TIMETABLE"), 61),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 561 },
    t(26),
    0.4,
    0.5
  ));

  // 83,17 geniş: leaves odak altçizgi
  const K = cumA.kel[4];
  ogelerA.push(S.darbe(
    altCizgi(K.x - 6, K.x + K.w + 6, altY(K.y, boyA, K.m), 11),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 },
    t(28),
    0.4,
    0.55
  ));

  // --- Geçiş (Çift Kart Kuralı) ---
  // 84,24–84,60 —: Grup A küçülür ve söner
  S.koy(grupKucul(ogelerA, 84.24, 0.36));

  // 84,54 —: şerit çerçevesi
  S.koy(S.kart({
    x: 48,
    y: 352,
    w: 984,
    h: 120,
    tb: 84.54,
    ad: "serit",
    tohum: 8,
    kutuSure: 0.1,
    kutuAralik: 0.05,
    satirlar: []
  }));

  // 84,58 —: şerit leaves metin
  S.koy(S.metinPop({
    parca: [["leaves", RT.murekkep]],
    x: 88,
    y: 434,
    font: FF(64),
    tb: 84.58,
    sure: 0.3,
    ses: 0.4
  }));

  // 84,64 —: şerit ok
  const xL = 88 + olc(FF(64), "leaves");
  let okBoy = 110;
  let xTT = xL + 24 + okBoy + 24;
  const wTT = olc(FC(64), "TIMETABLE");
  const SX = 779;
  if (xTT + wTT > SX - 20) {
    okBoy = 70;
    xTT = xL + 24 + okBoy + 24;
  }
  S.koy(S.darbeler(
    ok([xL + 24, 412], [xL + 24 + okBoy, 412], 23),
    { w: 6, renk: RT.ikincil, uc0: 6, uc1: 10 },
    84.64,
    0.16,
    0.06,
    false
  ));

  // 84,72 —: şerit TIMETABLE metin
  S.koy(S.metinPop({
    parca: [["TIMETABLE", RT.murekkep]],
    x: xTT,
    y: 434,
    font: FC(64),
    tb: 84.72,
    sure: 0.3,
    ses: false
  }));

  // 84,66 —: şerit tren simgesi
  S.koy(elCizim("tren-simge", trenParcalari(785, 375, 0.55, simgeTren), 84.66, 0.35, 1));

  // --- B Evresi ---
  // 84,60 I: Kart B çerçevesi
  S.koy(S.kart({
    x: 48,
    y: 490,
    w: 984,
    h: 240,
    tb: t(30) - 0.34,
    ad: "kartB",
    tohum: 6,
    kutuSure: 0.14,
    kutuAralik: 0.08,
    satirlar: []
  }));

  // 84,94–87,42 I … tonight.: Kart B cümlesi
  const sozcB = S.sozc.slice(30, 38);
  const satirlarB = [
    sozcB.slice(0, 5).map((w) => w.sozcuk).join(" "),
    sozcB.slice(5, 8).map((w) => w.sozcuk).join(" ")
  ];
  const sayilarB = [5, 3];
  const boyB = satirlarB.some((s, i) => (
    olc(FF(72), s) + 6 * (sayilarB[i] - 1) > 904
  )) ? 64 : 72;
  const hB = boyB === 72 ? 100 : 92;
  const cumB = S.koy(S.cumleYaz({
    sozcukler: sozcB,
    x: 88,
    y: 580,
    font: FF(boyB),
    satirH: hB,
    satirSay: [5, 3],
    bosluk: 6
  }));

  // 85,82 movie: bilet çizimi
  S.koy(elCizim("bilet", biletParcalari(540, 935, -0.06, 2.2), t(35), 1.0));

  // 89,63–90,97 Planı: ARRANGEMENT el yazısı
  const eAR = S.koy(S.elYazisi({
    metin: "ARRANGEMENT",
    x: 88,
    y: 1200,
    boy: 72,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(42), t1: t(45) - 0.1 }]
  }));

  // 91,07 Planlanmış: ARRANGEMENT altçizgi
  S.koy(S.darbe(
    altCizgi(84, 92 + eAR.w, altY(1200, 72, "ARRANGEMENT"), 62),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 562 },
    t(45),
    0.4,
    0.5
  ));

  // 92,43 şimdiki: am going odak altçizgi
  const A = cumB.kel[1];
  const B = cumB.kel[2];
  const yOdak = B.y + 0.48 * boyB;
  S.koy(S.darbe(
    altCizgi(A.x - 6, B.x + B.w + 6, yOdak, 12),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 502 },
    t(47),
    0.4,
    0.55
  ));
}

surucu(kur, (f) => S.kare(f), KARE);

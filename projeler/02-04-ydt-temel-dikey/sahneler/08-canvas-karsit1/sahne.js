// SAHNE 08 (DİKEY) — Karşıt 1/2: düz canvas, 1080x1920, 459 kare, t_bas 130,40; cümle 9.
// Zaman yalnız kare numarasından; sözcük zamanları sozcukler.json'dan.
import { surucu } from "/ortak/surucu.js";
import {
  Sahne, RT, renkCoz, elips, ok, altCizgi, kis, lerp, yavasla, olc, altY
} from "./sahne-ortak.js";
import { yaziNoktalari }
  from "/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js";

const KARE = 459, TBAS = 130.4, ICERIK = 447, KAYMA = -1.68;
// 16.11 DUZ3: zaman.json t_bas 132,08 (cümle 4/7 yeniden sentezlendi). TBAS ve sabit
// zamanlar eski çerçevede kalır; sözcük zamanları KAYMA ile ona çekilir.
const S = new Sahne({
  tbas: TBAS, kayma: KAYMA, kare: KARE, icerik: ICERIK, klasor: "08-canvas-karsit1", cumle: 9
});

const FF = (b) => `700 ${b}px Fredoka`;
const FC = (b) => `700 ${b}px Caveat`;
const t = (i) => S.sozc[i].t0;

const eyGen = (m, b) => yaziNoktalari(m, S.EY.G, {
  upm: S.EY.M.unitsPerEm, asc: S.EY.M.ascender, boy: b, x: 0, taban: 0
}).gen;

const EN = [
  ["She", 135.61, 135.87],
  ["is", 135.89, 135.97],
  ["wearing", 135.97, 136.31],
  ["her", 136.33, 136.47],
  ["pink", 136.51, 136.75],
  ["T-shirt", 136.87, 137.25],
  ["today.", 137.29, 137.69]
].map(([sozcuk, t0, t1]) => ({ sozcuk, t0, t1 }));

const uzunluk = (p) => p.reduce((acc, q, k) => (
  k ? acc + Math.hypot(q[0] - p[k - 1][0], q[1] - p[k - 1][1]) : 0
), 0);

function elCizim(ad, parcalar, tb, sure, olayEnCok = 3) {
  const n = parcalar.length, xs = [], ys = [];
  parcalar.forEach(({ p }) => p.forEach(([x, y]) => { xs.push(x); ys.push(y); }));
  const kut = { x: Math.min(...xs) - 6, y: Math.min(...ys) - 6 };
  kut.w = Math.max(...xs) + 6 - kut.x;
  kut.h = Math.max(...ys) + 6 - kut.y;
  const cocuk = parcalar.map(({ p, o }, i) => {
    const dur = Math.min(sure * 0.5, 0.1 + uzunluk(p) / 1800);
    const bas = tb + (n > 1 ? i / (n - 1) : 0) * (sure - dur);
    const ses = i < olayEnCok ? undefined : false;
    return S.darbe(p, { uc0: 8, uc1: 14, ...o }, bas, dur, ses);
  });
  const fb = S.fr(tb);
  return {
    kut,
    ciz(ctx, f) {
      if (f >= fb + 2) window.__kalemKutu?.ekle("cizim", ad, kut.x, kut.y, kut.w, kut.h);
      for (const c of cocuk) c.ciz(ctx, f);
    }
  };
}

function tisortParcalari(ox, oy, s) {
  const P = (x, y) => [ox + x * s, oy + y * s];
  const govde = { w: 4.5, renk: RT.murekkep };
  const ince = { w: 3.6, renk: RT.murekkep };
  return [
    {
      p: [
        [37, 4], [14, 12], [0, 36], [14, 46], [24, 37], [24, 88],
        [76, 88], [76, 37], [86, 46], [100, 36], [86, 12], [63, 4]
      ].map(([x, y]) => P(x, y)),
      o: { ...govde, duz: true }
    },
    { p: [P(37, 4), P(50, 14), P(63, 4)], o: ince },
    { p: [P(14, 12), P(24, 37)], o: { ...ince, duz: true } },
    { p: [P(86, 12), P(76, 37)], o: { ...ince, duz: true } }
  ];
}

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

function donen(pts, o, tb, sure, ses, tDon) {
  const sari = S.darbe(pts, { ...o }, tb, sure, ses);
  const gri = S.darbe(pts, { ...o, renk: RT.ikincil }, tb, sure, false);
  const fDon = S.fr(tDon);
  return {
    ciz(ctx, f) {
      const u = kis((f - fDon) / 9);
      sari.carpan = 1 - u;
      gri.carpan = u;
      gri.ciz(ctx, f);
      sari.ciz(ctx, f);
    }
  };
}

function bant(x0, x1, y0, y1, tb, sure) {
  const fb = S.fr(tb);
  S.bas(fb);
  S.olay(fb, "cizgi", 0.5);
  return {
    ciz(ctx, f) {
      const u = yavasla((f - fb) / (sure * 30));
      if (u <= 0) return;
      ctx.save();
      ctx.globalAlpha = 0.45;
      ctx.fillStyle = renkCoz(RT.vurguDolgu);
      ctx.fillRect(x0, y0, (x1 - x0) * u, y1 - y0);
      ctx.restore();
    }
  };
}

let olcAltyazi;

function altyaziSar(ctx, metin, genislik) {
  const satirlar = [];
  let s = "";
  for (const w of metin.split(" ")) {
    const d = s ? `${s} ${w}` : w;
    // 16.11 DUZ3 (DK-2): satır en çok 24 karakter; ortak/kunye.js altyaziSar ile aynı
    if ((ctx.measureText(d).width > genislik || d.length > 24) && s) {
      satirlar.push(s);
      s = w;
    } else {
      s = d;
    }
  }
  if (s) satirlar.push(s);
  return satirlar;
}

function altyaziDuzelt() {
  const L = S.K.altyazi;
  if (!L || !L.length) return;
  const i0 = L.findIndex((a) => a.cumle === 9);
  if (i0 < 0) return;
  let sayi = 0;
  while (i0 + sayi < L.length && L[i0 + sayi].cumle === 9) sayi++;
  const c9 = L.slice(i0, i0 + sayi);
  const en = c9.find((a) => a.dil === "en");
  if (!en) return;

  const tr1 = c9[0];
  const enIndex = c9.indexOf(en);
  const trKalan = c9.slice(enIndex + 1);
  const tr3Metin = trKalan.map((a) => a.metin).join(" ");
  // S.sozc eski çerçevede (KAYMA); altyazı yeni çerçevede aranır (sahne-ortak satır 450) → kayma geri alınır
  const k = S.kayma || 0;
  const yeniEn = { ...en, t0: EN[0].t0 - k, t1: EN[6].t1 - k };

  if (!olcAltyazi) {
    olcAltyazi = document.createElement("canvas").getContext("2d");
  }
  olcAltyazi.font = "500 44px Lexend";
  const genislik = 984;
  const kelimeler = tr3Metin.split(" ");
  const dilimler = [];
  let grup = "", bas = 0;
  for (let i = 0; i < kelimeler.length; i++) {
    const d = grup ? `${grup} ${kelimeler[i]}` : kelimeler[i];
    if (grup && altyaziSar(olcAltyazi, d, genislik).length > 2) {
      dilimler.push({ metin: grup, bas });
      grup = kelimeler[i];
      bas = i;
    } else {
      grup = d;
    }
  }
  if (grup) dilimler.push({ metin: grup, bas });

  const sablonTr = trKalan[0] || { ...tr1, dil: "tr" };
  const yeniTr3 = dilimler.map((d, j) => {
    const t0 = S.sozc[8 + d.bas].t0 - k;
    const t1 = (j < dilimler.length - 1
      ? S.sozc[8 + dilimler[j + 1].bas].t0 - 0.4
      : S.sozc[19].t1) - k;
    return { ...sablonTr, metin: d.metin, t0, t1 };
  });

  const yeniGirdiler = [tr1, yeniEn, ...yeniTr3];
  L.splice(i0, sayi, ...yeniGirdiler);
}

async function kur() {
  await S.kur();
  if (S.sozc.length !== 20) {
    throw new Error(`Beklenen 20 sözcük, gelen ${S.sozc.length}`);
  }
  altyaziDuzelt();

  // 134,95 today.: başlık notu
  const nT = S.koy(S.elYazisi({
    metin: "today",
    x: 88,
    y: 436,
    boy: 80,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(7), t1: S.sozc[7].t1 }]
  }));

  // 135,11 today.: kart çerçevesi
  S.koy(S.kart({
    x: 48,
    y: 490,
    w: 984,
    h: 270,
    tb: EN[0].t0 - 0.5,
    ad: "kart",
    tohum: 8,
    kutuSure: 0.14,
    kutuAralik: 0.08,
    satirlar: []
  }));

  // 135,61 She: kart cümlesi
  const cum = S.koy(S.cumleYaz({
    sozcukler: EN,
    x: 88,
    y: 596,
    font: FF(72),
    satirH: 92,
    satirSay: [4, 3],
    bosluk: 6
  }));

  // 136,87 T-shirt: kart köşesinde tişört
  const tis = S.koy(elCizim(
    "tisort",
    tisortParcalari(772, 524, 2.2),
    EN[5].t0,
    0.75
  ));

  // 139,93 bugünü: today gün bandı
  S.koy(bant(200, 880, 1040, 1180, t(10), 0.45));

  // 140,03 bugünü: gün bandı uç çentikleri
  S.koy(S.darbe(
    [[200, 1032], [200, 1198]],
    { duz: true, w: 5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 212 },
    t(10) + 0.10,
    0.15,
    0.45
  ));
  S.koy(S.darbe(
    [[880, 1032], [880, 1198]],
    { duz: true, w: 5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 213 },
    t(10) + 0.22,
    0.15,
    false
  ));

  // 138,57 Burada: zaman ekseni
  const [, uc1, uc2] = ok([96, 1180], [984, 1180], 21);
  S.koy(S.darbeler(
    [[[96, 1180], [984, 1180]], uc1, uc2],
    { duz: true, w: 4.5, renk: RT.ikincil, uc0: 6, uc1: 12 },
    t(8),
    0.5,
    0.15,
    0.45
  ));

  // 139,21 today: karttaki today sarı altçizgi
  const kT = cum.kel[6];
  const wT = olc(FF(72), "today");
  S.koy(donen(
    altCizgi(kT.x - 6, kT.x + wT + 6, altY(kT.y, 72, "today"), 11),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 },
    t(9),
    0.4,
    0.55,
    t(18)
  ));

  // 139,29 today: nottaki today sarı altçizgi
  S.koy(donen(
    altCizgi(84, 88 + nT.w + 4, 436 + 0.42 * 80, 12),
    { w: 8, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 502 },
    t(9) + 0.08,
    0.4,
    false,
    t(13)
  ));

  // 140,05 bugünü: karttan this day only notuna kanca ok (↳)
  const cx = kT.x + wT / 2;
  const wD = eyGen("this day only", 72);
  const xMetin = Math.min(cx + 92, 1000 - wD);
  const xa = cx;
  const xb = xMetin - 18;
  S.koy(S.darbe(
    [[xa, 774], [xa, 830]],
    { duz: true, w: 5, renk: RT.murekkep, uc0: 4, uc1: 8 },
    t(10) + 0.12,
    0.12,
    0.4
  ));
  S.koy(S.darbeler(
    ok([xa, 830], [xb, 830], 23),
    { duz: true, w: 5, renk: RT.murekkep, uc0: 4, uc1: 8 },
    140.17,
    0.12,
    0.06,
    false
  ));

  // 140,29 gösterir.: this day only el yazısı
  S.koy(S.elYazisi({
    metin: "this day only",
    x: xMetin,
    y: 852,
    boy: 72,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(11), t1: S.sozc[11].t1 }]
  }));

  // 141,77 kıyafet: tişört çevresine sarı halka
  const tc = {
    x: tis.kut.x + tis.kut.w / 2,
    y: tis.kut.y + tis.kut.h / 2
  };
  S.koy(S.darbe(
    elips(tc.x, tc.y, tis.kut.w / 2 + 14, tis.kut.h / 2 + 10, -0.05, 31),
    { w: 9, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 },
    t(13),
    0.45,
    0.55
  ));

  // 142,57 konuşma: now noktası ve nabız
  S.koy(nowNokta(360, 1180, t(14)));
  S.koy(S.nabiz(360, 1180, 14, t(14) + 0.1));

  // 143,05 anında: now etiketi
  const gNow = eyGen("now", 64);
  S.koy(S.elYazisi({
    metin: "now",
    x: 360 - gNow / 2,
    y: 1252,
    boy: 64,
    renk: RT.murekkep,
    tb: t(15),
    sure: 0.4
  }));

  // 144,37 şimdiki: is wearing sarı altçizgi
  const kelIs = cum.kel[1];
  const kelWear = cum.kel[2];
  S.koy(S.darbe(
    altCizgi(kelIs.x - 6, kelWear.x + kelWear.w + 6, altY(kelWear.y, 72, "wearing"), 13),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 503 },
    t(18),
    0.4,
    0.55
  ));
}

surucu(kur, (f) => S.kare(f), KARE);

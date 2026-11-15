// SAHNE 04 (DİKEY) — Örnek 2/3: düz canvas, 1080x1920, 779 kare, t_bas 43,85; cümle 4.
// 16.11 DUZ3: cümle 4 yeniden sentezlendi ("Orada hep yaşıyorum" → "Burası bizim evimiz"); cümle içi sabit
// zamanlar sözcüğe bağlandı (t(4) live., t(22) My).
// Zaman yalnız kare numarasından; sözcük zamanları sozcukler.json'dan.
import { surucu } from "/ortak/surucu.js";
import {
  Sahne, RT, renkCoz, ok, altCizgi, lerp, yavasla, olc, altY
} from "./sahne-ortak.js";
import { yaziNoktalari }
  from "/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js";

const KARE = 779, TBAS = 43.85, ICERIK = 767;
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, klasor: "04-canvas-ornek2", cumle: 4
});
const KOKDIZ = "/projeler/02-04-ydt-temel-dikey/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();

const FF = (b) => `700 ${b}px Fredoka`;
const FC = (b) => `700 ${b}px Caveat`;
const t = (i) => S.sozc[i].t0;

const eyGen = (m, b) => yaziNoktalari(m, S.EY.G, {
  upm: S.EY.M.unitsPerEm, asc: S.EY.M.ascender, boy: b, x: 0, taban: 0
}).gen;

const BAVUL_SVG_DIKEY =
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="5 2 14 22" fill="none" ` +
  `stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">` +
  `<path d="M6 8a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v11a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2z"/>` +
  `<path d="M10 6v-3h4v3"/>` +
  `<path d="M10 9v9"/>` +
  `<path d="M14 9v9"/>` +
  `<path d="M8.5 21v1.8"/>` +
  `<path d="M15.5 21v1.8"/>` +
  `</svg>`;

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

async function kur() {
  await S.kur();
  if (S.sozc.length !== 49) {
    throw new Error(`Beklenen 49 sözcük, gelen ${S.sozc.length}`);
  }

  gizli = document.createElement("canvas");
  gizli.width = 1080;
  gizli.height = 1920;
  gizliCtx = gizli.getContext("2d");

  const evHamSvg = await svgOku("tabler/home.svg");
  const evSvg = evHamSvg.replace('viewBox="0 0 24 24"', 'viewBox="2.5 2.5 19 19"');

  const ogelerA = [];

  // 44,40 İkinci: daire içinde 2
  ogelerA.push(S.daireSayi(2, 96, 428, t(0), 48));

  // 47,20 live.: "live" başlık pop
  ogelerA.push(S.metinPop({
    parca: [["live", RT.murekkep]],
    x: 184,
    y: 486,
    font: FF(140),
    tb: t(4),
    sure: 0.3,
    olcek0: 0.85,
    ses: 0.5,
    turu: "tik",
  }));

  // 47,55 live.: "live" sarı altçizgi
  const wLive = olc(FF(140), "live");
  ogelerA.push(S.darbe(
    altCizgi(184 - 6, 184 + wLive + 6, 520, 401),
    { w: 10, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 401 },
    t(4) + 0.35,
    0.35,
    0.55
  ));

  // live. + 0,50: Kart A çerçevesi
  ogelerA.push(S.kart({
    x: 48,
    y: 540,
    w: 984,
    h: 236,
    tb: t(4) + 0.50,
    ad: "kartA",
    tohum: 4,
    kutuSure: 0.14,
    kutuAralik: 0.08,
    satirlar: [],
  }));

  // 48,09 I … family.: sol cümle
  const solSozc = S.sozc.slice(5, 12).map((w) => (
    w.sozcuk === "Istanbul" ? { ...w, sozcuk: "İstanbul" } : w
  ));
  const cumA = S.cumleYaz({
    sozcukler: solSozc,
    x: 88,
    y: 636,
    font: FF(72),
    satirH: 92,
    satirSay: [4, 3],
    bosluk: 6,
  });
  ogelerA.push(cumA);

  // 50,82 Ailemle: ev çizimi
  ogelerA.push(S.cizim({
    svg: evSvg,
    ad: "ev",
    kutu: { x: 330, y: 792, w: 420, h: 420 },
    enCok: 10,
    esik: 0.01,
    w: 4.4,
    tb: t(12),
    sure: 1.0,
    olayEnCok: 4,
    nefes: false,
  }));

  // 53,06 bizim: uzun bant
  ogelerA.push(S.darbe(
    [[150, 1330], [930, 1330]],
    { duz: true, w: 30, renk: RT.vurguDolgu, alfa: 0.45, uc0: 4, uc1: 8, tohum: 101 },
    t(16),
    1.0,
    0.5
  ));

  // 52,66 Burası: sol zaman ekseni
  const [, uc1A, uc2A] = ok([96, 1330], [984, 1330], 21);
  ogelerA.push(S.darbeler(
    [[[96, 1330], [984, 1330]], uc1A, uc2A],
    { duz: true, w: 4, renk: RT.ikincil, uc0: 6, uc1: 12 },
    t(15),
    0.4,
    0.15,
    0.4
  ));

  // 52,91 Burası: sol now noktası ve nabız
  ogelerA.push(nowNokta(540, 1330, t(15) + 0.25));
  ogelerA.push(S.nabiz(540, 1330, 14, t(15) + 0.25 + 0.35));

  // 53,06 Burası: sol now etiketi
  const gNow = eyGen("now", 64);
  ogelerA.push(S.elYazisi({
    metin: "now",
    x: 540 - gNow / 2,
    y: 1390,
    boy: 64,
    renk: RT.murekkep,
    tb: t(15) + 0.40,
    sure: 0.4,
  }));

  // 54,58 Kalıcı: PERMANENT etiketi
  ogelerA.push(S.elYazisi({
    metin: "PERMANENT",
    x: 150,
    y: 1298,
    boy: 72,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(18), t1: t(20) }],
  }));

  // 55,54 geniş: odak live altçizgi
  const K = cumA.kel[1];
  ogelerA.push(S.darbe(
    altCizgi(K.x - 6, K.x + K.w + 6, altY(K.y, 72, K.m), 11),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 },
    t(20),
    0.4,
    0.55
  ));

  // My − 0,79: Grup A küçülür ve söner
  S.koy(grupKucul(ogelerA, t(22) - 0.79, 0.36));

  // My − 0,49: şerit çerçevesi
  S.koy(S.kart({
    x: 48,
    y: 352,
    w: 984,
    h: 120,
    tb: t(22) - 0.49,
    ad: "serit",
    tohum: 8,
    kutuSure: 0.1,
    kutuAralik: 0.05,
    satirlar: [],
  }));

  // My − 0,45: şerit live pop
  S.koy(S.metinPop({
    parca: [["live", RT.murekkep]],
    x: 88,
    y: 434,
    font: FF(64),
    tb: t(22) - 0.45,
    sure: 0.3,
    ses: 0.4,
  }));

  // My − 0,39: şerit ok
  const xL = 88 + olc(FF(64), "live");
  S.koy(S.darbeler(
    ok([xL + 24, 412], [xL + 134, 412], 23),
    { w: 6, renk: RT.ikincil, uc0: 6, uc1: 10 },
    t(22) - 0.39,
    0.16,
    0.06,
    false
  ));

  // My − 0,31: şerit PERMANENT pop
  S.koy(S.metinPop({
    parca: [["PERMANENT", RT.murekkep]],
    x: xL + 158,
    y: 434,
    font: FC(64),
    tb: t(22) - 0.31,
    sure: 0.3,
    ses: false,
  }));

  // My − 0,37: şerit ev simgesi
  S.koy(S.cizim({
    svg: evSvg,
    ad: "ev-simge",
    kutu: { x: 912, y: 364, w: 96, h: 96 },
    enCok: 10,
    esik: 0.01,
    w: 4,
    tb: t(22) - 0.37,
    sure: 0.35,
    olayEnCok: 1,
    nefes: false,
  }));

  // 56,64 My: Kart B çerçevesi
  S.koy(S.kart({
    x: 48,
    y: 490,
    w: 984,
    h: 328,
    tb: t(22) - 0.35,
    ad: "kartB",
    tohum: 6,
    kutuSure: 0.14,
    kutuAralik: 0.08,
    satirlar: [],
  }));

  // 56,99 My … uncle.: sağ cümle
  const sagSozc = S.sozc.slice(22, 35);
  const satirlarB = [
    sagSozc.slice(0, 5).map((w) => w.sozcuk).join(" "),
    sagSozc.slice(5, 10).map((w) => w.sozcuk).join(" "),
    sagSozc.slice(10, 13).map((w) => w.sozcuk).join(" "),
  ];
  const boyB = satirlarB.some((s) => olc(FF(72), s) > 904) ? 64 : 72;
  const satirHB = boyB === 64 ? 84 : 92;
  const cumB = S.koy(S.cumleYaz({
    sozcukler: sagSozc,
    x: 88,
    y: 586,
    font: FF(boyB),
    satirH: satirHB,
    satirSay: [5, 5, 3],
    bosluk: 6,
  }));

  // 62,28 dışında,: bavul çizimi
  S.koy(S.cizim({
    svg: BAVUL_SVG_DIKEY,
    ad: "bavul",
    kutu: { x: 356, y: 845, w: 268, h: 420 },   // sağda TEMPORARY'ye yer (QA tur 1)
    enCok: 10,
    esik: 0.01,
    w: 4.4,
    tb: t(37),
    sure: 1.0,
    olayEnCok: 4,
    nefes: false,
  }));

  // 65,60 şimdilik.: kısa bant
  S.koy(S.darbe(
    [[470, 1330], [610, 1330]],
    { duz: true, w: 30, renk: RT.vurguDolgu, alfa: 0.45, uc0: 4, uc1: 8, tohum: 102 },
    t(44),
    0.4,
    0.5
  ));

  // 65,00 Bu: sağ zaman ekseni
  const [, uc1B, uc2B] = ok([96, 1330], [984, 1330], 22);
  S.koy(S.darbeler(
    [[[96, 1330], [984, 1330]], uc1B, uc2B],
    { duz: true, w: 4, renk: RT.ikincil, uc0: 6, uc1: 12 },
    t(42),
    0.4,
    0.15,
    0.4
  ));

  // 66,00 şimdilik.: kısa bant uç çentikleri
  S.koy(S.darbe(
    [[470, 1304], [470, 1356]],
    { duz: true, w: 6, renk: RT.vurgu, uc0: 3, uc1: 3, tohum: 103 },
    t(44) + 0.40,
    0.18,
    0.4
  ));
  S.koy(S.darbe(
    [[610, 1304], [610, 1356]],
    { duz: true, w: 6, renk: RT.vurgu, uc0: 3, uc1: 3, tohum: 104 },
    t(44) + 0.52,
    0.18,
    0.4
  ));

  // 65,25 Bu: sağ now noktası ve nabız
  S.koy(nowNokta(540, 1330, t(42) + 0.25));
  S.koy(S.nabiz(540, 1330, 14, t(42) + 0.25 + 0.35));

  // 65,40 Bu: sağ now etiketi
  S.koy(S.elYazisi({
    metin: "now",
    x: 540 - gNow / 2,
    y: 1390,
    boy: 64,
    renk: RT.murekkep,
    tb: t(42) + 0.40,
    sure: 0.4,
  }));

  // 66,84 Geçici: TEMPORARY etiketi (QA tur 1: 72 px'te Y ucu x 1043'e taştı, kuyruğu ok ucuna
  // değdi → 64 px, x 632; bant ucu 610 ile ok ucu ≈ 952 arasında kalır)
  S.koy(S.elYazisi({
    metin: "TEMPORARY",
    x: 632,
    y: 1300,
    boy: 64,
    renk: RT.murekkep,
    sozcukler: [{ t0: t(45), t1: t(47) }],
  }));

  // 67,88 şimdiki: odak am living altçizgi
  const A = cumB.kel[8], B = cumB.kel[9];
  S.koy(S.darbe(
    altCizgi(A.x - 6, B.x + B.w + 6, altY(B.y, boyB, "living"), 12),
    { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 502 },
    t(47),
    0.4,
    0.55
  ));
}

surucu(kur, (f) => S.kare(f), KARE);

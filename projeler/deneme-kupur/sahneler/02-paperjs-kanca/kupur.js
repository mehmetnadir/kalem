// Kâğıt küpür kadro karakteri — renkli kesik kâğıt parçalarından figür (kalem modeli yok).
// kupur(S, {x, y, yas, duygu, kimlik, boy | h, bas, sure}) -> {h, boy, k, bit, sinir}
// kadro(n, tohum) -> n farklı kimlik (aynı tohum = aynı kadro). x: figür ekseni · y: ayak tabanı.
// Parçalar çizilmez, yapıştırılır: 6 karede ölçek 0,85 → 1 + alfa 0 → 1. Sıra: gövde → baş → saç →
// giysi → aksesuar → yüz. Yüz hatları kalem çizgisidir (RT.murekkep; koyu temada zemin rengi).
// Oran (ORAN, OGRETMEN) ve duygu (DUYGU) tabloları deneme-karakter/…/karakter.js'den kopyadır.
import { RT, renkCoz, kis,
  cikis } from "/projeler/deneme-kupur/sahneler/02-paperjs-kanca/kalem-paper.js";
import { temaAdi, temaSurum } from "/projeler/deneme-kupur/ortak/kunye.js";

// KÂĞIT PALETİ — açık tema: krem zemin (#f7f3ea) · koyu tema: #1b1a17 zemin
export const KAGIT = {
  acik: { gol: 0.18,
    ten: ["#f1c9a5", "#e0a77c", "#c07f56", "#8d5a3b"],
    giysi: ["#8fa8b8", "#b4c49a", "#d8a7a0", "#c9b17a", "#9a8fb3", "#7f9c93"],
    sac: ["#3a2e28", "#7a5233", "#c9a15a"] },
  koyu: { gol: 0.3,
    ten: ["#e9bf9a", "#d39c70", "#b3744c", "#8a5738"],
    giysi: ["#6f8fa3", "#8fa77a", "#c98a82", "#b89a55", "#8a7fa8", "#5f8f84"],
    sac: ["#6b5545", "#a8744a", "#dcb86e"] } };
export const AKSESUAR = ["gozluk", "sapka", "kulaklik", "toka"];
export const SAC = ["kisa", "diken", "uzun", "kuyruk", "topuz", "bob"];

export const ORAN = [
  { ad: "10–11", yas: 11, k: 4.5, omuz: 1.6 }, { ad: "12–13", yas: 13, k: 5.5, omuz: 1.8 },
  { ad: "14–15", yas: 15, k: 6.5, omuz: 2.0 }, { ad: "16–18", yas: 18, k: 7.0, omuz: 2.1 }];
export const OGRETMEN = { ad: "öğretmen", k: 7.5, omuz: 2.2 };
export const oran = (yas) => ORAN.find((r) => yas <= r.yas) || ORAN[ORAN.length - 1];

const kk = (a, y) => ({ a, y }), gz = (s, r, gx = 0, gy = 0) => ({ s, r, gx, gy });
const cift = (x) => [x, { ...x }];
export const DUYGU = {
  notr: { kas: [kk(0, 0), kk(0, 0)], goz: cift(gz("n", 0.055)),
    agiz: { w: 0.22, c: [-0.01, 0.01, -0.01] }, tilt: 0 },
  dikkat: { kas: [kk(-6, 0.03), kk(-6, 0.03)], goz: cift(gz("n", 0.068)),
    agiz: { w: 0.16, c: [0, 0, 0] }, tilt: -3 },
  dusunme: { kas: [kk(8, 0.07), kk(-6, 0)], goz: cift(gz("n", 0.055, 0.05, -0.045)),
    agiz: { w: 0.14, c: [0.02, 0, -0.02], dx: 0.07 }, tilt: 8 },
  saskin: { kas: [kk(8, 0.11), kk(8, 0.11)], goz: cift(gz("n", 0.09)),
    agiz: { w: 0.13, c: [0, 0, 0], ac: 0.13, tip: "o" }, tilt: 0 },
  kararsiz: { kas: [kk(16, 0.05), kk(10, -0.01)], goz: cift(gz("n", 0.055, -0.04, 0)),
    agiz: { w: 0.26, c: [0.03, -0.03, 0.03, -0.03, 0.03] }, tilt: -5 },
  yanlis: { kas: [kk(18, 0.01), kk(18, 0.01)], goz: cift(gz("k", 0.07)),
    agiz: { w: 0.22, c: [0.05, -0.03, 0.05] }, tilt: -6 },
  dogru: { kas: [kk(-2, 0.04), kk(-2, 0.04)], goz: cift(gz("n", 0.06)),
    agiz: { w: 0.28, c: [-0.06, 0.03, -0.06] }, tilt: 4 },
  sevinc: { kas: [kk(0, 0.08), kk(0, 0.08)], goz: cift(gz("y", 0.075)),
    agiz: { w: 0.32, c: [-0.06, 0.03, -0.06], ac: 0.12 }, tilt: 6 } };

// tohumlu hash (Math.random yok)
const hs = (a, b = 0, c = 0) => { let h = (Math.imul(a | 0, 374761393) + Math.imul(b | 0, 668265263)
  + Math.imul(c | 0, 1274126177)) | 0; h = Math.imul(h ^ (h >>> 13), 1274126177); h ^= h >>> 16;
  return (h >>> 0) / 4294967296; };

// Kadro üretici: eksen başına eş asal adımla döner → 12 kişide tekrar en aza iner.
export function kadro(n, tohum = 1) {
  const o = (k, m) => Math.floor(hs(tohum, k, 5) * m);
  const s = [o(1, 6), o(2, 4), o(3, 6), o(4, 4), o(5, 3), o(6, 3)];
  return Array.from({ length: n }, (_, i) => {
    let sac = (i + s[0]) % 6, aks = (i * 3 + s[3] + Math.floor(i / 4)) % 4;
    if (aks === 1 && sac === 4) sac = 0;                    // şapka + topuz çakışır
    if (aks === 3 && sac < 2) sac = 3;                      // toka: kuyruk / uzun / topuz / bob
    const ust = (i * 5 + s[2]) % 6;
    return { ad: "k" + i, sac, aks, ust, alt: (ust + 3) % 6, ten: (i * 3 + s[1]) % 4,
      sacRenk: (i * 2 + Math.floor(i / 3) + s[5]) % 3, yas: [11, 13, 15][(i * 2 + s[4]) % 3],
      etek: hs(tohum, i, 9) < (sac >= 2 ? 0.7 : 0.2) }; });
}

const golge = (hex, f) => "#" + [1, 3, 5].map((i) => Math.round(parseInt(hex.slice(i, i + 2), 16)
  * f).toString(16).padStart(2, "0")).join("");
const elips = (u, v, rx, ry, n = 14, a0 = 0) => Array.from({ length: n }, (_, i) => {
  const a = a0 + 2 * Math.PI * i / n; return [u + Math.cos(a) * rx, v + Math.sin(a) * ry]; });
const uzun = (p) => p.reduce((s, q, i) => s + (i ? Math.hypot(q[0] - p[i - 1][0],
  q[1] - p[i - 1][1]) : 0), 0);

export function kupur(S, o) {
  const P = S.P, kim = o.kimlik, dg = DUYGU[o.duygu];
  if (!kim || !dg) throw new Error(`kupur: kimlik/duygu yok: ${o.duygu}`);
  const r = kim.ogretmen ? OGRETMEN : oran(o.yas || kim.yas);
  const k = r.k, h = o.boy ? o.boy / k : o.h || 42, T = k * h, X = o.x, Yg = o.y;
  const bas = o.bas || 0, sure = o.sure || 40, F = 14, YAP = 6;  // F: yüz kalemi kare sayısı
  const top = Yg - T, ys = top + 1.14 * h, R = T - 1.14 * h, hipY = ys + 0.44 * R;
  const sw = r.omuz * h, tw = sw * 0.78, hem = hipY + (kim.etek ? 0.32 * h : 0);
  const cx = X, cy = top + 0.5 * h, tilt = dg.tilt * Math.PI / 180;
  const hd = (u, v) => { const dv = v - 0.5, c = Math.cos(tilt), s = Math.sin(tilt);
    return [cx + (u * c - dv * s) * h, cy + (u * s + dv * c + 0.5) * h]; };
  const bk = (q) => q.map((p) => hd(p[0], p[1]));
  const og = S.oge({}), tohum = Math.round(X * 7 + Yg * 13 + bas) | 0;
  const PAR = [], AMP = Math.min(1.3, 0.04 * h + 0.2);
  const TEN = () => KAGIT[temaAdi()].ten[kim.ten], GIY = (i) => KAGIT[temaAdi()].giysi[i];
  const SAC_ = () => KAGIT[temaAdi()].sac[kim.sacRenk], VUR = () => renkCoz(RT.vurgu);
  const YM = temaAdi() === "acik" ? RT.murekkep : RT.zemin;  // yüz kalemi: kâğıtta okunur koyu ton

  // kenarı kesik çokgen: köşe ±amp px, kenar başına 1–2 ara nokta ±(1–2) px (tohumlu)
  const kes = (pts, sd, amp = AMP) => { const c = [];
    pts.forEach((p, i) => { const q = pts[(i + 1) % pts.length], dx = q[0] - p[0], dy = q[1] - p[1];
      const L = Math.hypot(dx, dy) || 1, j = (a) => (hs(sd, i, a) - 0.5) * 2 * amp;
      c.push([p[0] + j(1), p[1] + j(2)]);
      if (L < 8) return;
      const ad = hs(sd, i, 3) < 0.5 ? [0.5] : [0.35, 0.7];
      ad.forEach((u, m) => { const e = (hs(sd, i, 4 + m) < 0.5 ? -1 : 1)
        * (0.8 + hs(sd, i, 7 + m)) * amp / 1.3;
        c.push([p[0] + dx * u - dy / L * e, p[1] + dy * u + dx / L * e]); }); });
    return c; };
  const ekle = (faz, pts, renk, op = {}) => PAR.push({ faz, pts: kes(pts, tohum + PAR.length * 31,
    op.amp), delik: op.delik && kes(op.delik, tohum + PAR.length * 37 + 5, op.amp), renk });
  const dikd = (x0, y0, x1, y1) => [[x0, y0], [x1, y0], [x1, y1], [x0, y1]];

  // --- gövde: bacak, ayakkabı, kol, el, boyun
  const lw = tw * 0.36, ar = tw * 0.1, bacBit = Yg - 0.2 * h;
  for (const sg of [-1, 1]) {
    const x0 = sg < 0 ? X - ar / 2 - lw : X + ar / 2, x1 = x0 + lw;
    ekle("govde", dikd(x0, hipY - 0.1 * h, x1, bacBit + 0.02 * h), () => GIY(kim.alt));
    ekle("govde", dikd(sg < 0 ? x0 - 0.16 * h : x0 - 0.02 * h, bacBit, sg < 0 ? x1 + 0.02 * h
      : x1 + 0.16 * h, Yg), () => SAC_());
  }
  const aw = 0.2 * h, ay1 = ys + 0.5 * R;
  for (const sg of [-1, 1]) {
    const sx = X + sg * (sw / 2 - aw / 2), ex = sx + sg * 0.05 * h;
    ekle("govde", [[sx - aw / 2, ys + 0.08 * h], [sx + aw / 2, ys + 0.08 * h],
      [ex + aw / 2, ay1], [ex - aw / 2, ay1]], () => GIY(kim.ust));
    ekle("govde", elips(ex, ay1 + 0.08 * h, 0.11 * h, 0.12 * h, 10), TEN);
  }
  ekle("govde", dikd(X - 0.12 * h, top + 0.9 * h, X + 0.12 * h, ys + 0.05 * h),
    () => golge(TEN(), 0.9));

  // --- baş
  ekle("bas", bk(elips(0, 0, 0.41, 0.5, 16, 0.2)), TEN);

  // --- saç (stil kim.sac; renk kim.sacRenk)
  const KAP = [[-0.45, -0.02], [-0.46, -0.2], [-0.4, -0.38], [-0.26, -0.5], [-0.08, -0.56],
    [0.12, -0.55], [0.3, -0.47], [0.43, -0.33], [0.47, -0.15], [0.45, -0.02], [0.36, -0.22],
    [0.19, -0.31], [0, -0.34], [-0.19, -0.31], [-0.36, -0.22]];
  const yan = (sg) => [[sg * 0.47, -0.1], [sg * 0.3, -0.1], [sg * 0.3, 0.35], [sg * 0.52, 0.38]];
  if (kim.sac === 4) ekle("sac", bk(elips(0, -0.66, 0.2, 0.2, 10)), SAC_);
  if (kim.sac === 1) ekle("sac", bk(Array.from({ length: 14 }, (_, i) => {
    const a = (190 + i * 12.8) * Math.PI / 180, s = i % 2 ? 1.0 : 1.38;
    return [Math.cos(a) * 0.46 * s, Math.sin(a) * 0.52 * s - 0.04]; }).concat([[0.36, -0.22],
    [0.19, -0.31], [0, -0.34], [-0.19, -0.31], [-0.36, -0.22]])), SAC_);
  else ekle("sac", bk(KAP), SAC_);
  if (kim.sac === 2) for (const sg of [-1, 1]) ekle("sac", bk([[sg * 0.46, -0.1],
    [sg * 0.37, 0.05], [sg * 0.38, 0.72], [sg * 0.58, 0.78], [sg * 0.55, 0.1]]), SAC_);
  if (kim.sac === 3) ekle("sac", bk([[0.4, -0.35], [0.62, -0.3], [0.78, 0], [0.8, 0.5],
    [0.66, 0.62], [0.62, 0.12], [0.5, -0.05]]), SAC_);
  if (kim.sac === 5) for (const sg of [-1, 1]) ekle("sac", bk(yan(sg)), SAC_);

  // --- giysi: gövde üstü (+ etek)
  ekle("giysi", [[X - sw / 2, ys + 0.1 * h], [X - sw / 2 + 0.25 * h, ys],
    [X + sw / 2 - 0.25 * h, ys], [X + sw / 2, ys + 0.1 * h], [X + tw / 2, hipY],
    [X - tw / 2, hipY]], () => GIY(kim.ust));
  if (kim.etek) ekle("giysi", [[X - tw / 2, hipY - 0.06 * h], [X + tw / 2, hipY - 0.06 * h],
    [X + tw * 0.7, hem], [X - tw * 0.7, hem]], () => GIY(kim.alt));

  // --- aksesuar: tek parça, RT.vurgu (gözlük, şapka, kulaklık, toka)
  const aks = AKSESUAR[kim.aks];
  if (aks === "gozluk") {
    for (const sg of [-1, 1]) ekle("aks", bk(elips(sg * 0.19, 0.03, 0.17, 0.17, 12)), VUR,
      { amp: 0.35, delik: bk(elips(sg * 0.19, 0.03, 0.115, 0.115, 12)) });
    ekle("aks", bk(dikd(-0.04, -0.01, 0.04, 0.03)), VUR, { amp: 0.3 });
  } else if (aks === "sapka") {
    ekle("aks", bk([[-0.5, -0.27], [-0.5, -0.5], [-0.3, -0.72], [0, -0.8], [0.3, -0.72],
      [0.5, -0.5], [0.5, -0.27]]), VUR);
  } else if (aks === "kulaklik") {
    ekle("aks", bk([[-0.52, 0.06], [-0.58, -0.3], [-0.38, -0.58], [0, -0.68], [0.38, -0.58],
      [0.58, -0.3], [0.52, 0.06], [0.46, 0.06], [0.5, -0.28], [0.34, -0.5], [0, -0.6],
      [-0.34, -0.5], [-0.5, -0.28], [-0.46, 0.06]]), VUR, { amp: 0.5 });
    for (const sg of [-1, 1]) ekle("aks", bk(elips(sg * 0.5, 0.1, 0.1, 0.18, 8)), VUR);
  } else {
    const bx = kim.sac === 3 ? 0.46 : -0.4, by = -0.3, d = kim.sac === 3 ? 1 : -1;
    ekle("aks", bk([[bx, by], [bx + d * 0.17, by - 0.1], [bx + d * 0.17, by + 0.1]].concat([
      [bx, by],
      [bx - d * 0.17, by - 0.1], [bx - d * 0.17, by + 0.1]])), VUR, { amp: 0.4 });
  }

  // --- yapıştırma zamanı + Paper öğeleri
  const n = PAR.length, pencere = Math.max(1, sure - YAP - F), gol = [2.5, 3];
  PAR.forEach((p, i) => {
    const nokta = (q) => new P.Point(q[0], q[1]);
    const yol = (pts, d = [0, 0]) => new P.Path({ segments: pts.map((q) => nokta([q[0] + d[0],
      q[1] + d[1]])), closed: true, applyMatrix: false, insert: false });
    const yapi = (d) => p.delik ? new P.CompoundPath({ children: [yol(p.pts, d), yol(p.delik, d)],
      fillRule: "evenodd", applyMatrix: false, insert: false }) : yol(p.pts, d);
    p.gl = yapi(gol); p.pe = yapi([0, 0]); p.gl.fillColor = "#000000";
    p.g = new P.Group({ applyMatrix: false, children: [p.gl, p.pe], visible: false });
    og.g.addChild(p.g);
    p.bas = bas + pencere * (n > 1 ? i / (n - 1) : 0);
    const m = p.pts.length, c = p.pts.reduce((s, q) => [s[0] + q[0] / m, s[1] + q[1] / m], [0, 0]);
    p.cx = c[0]; p.cy = c[1]; p.rot = (hs(tohum, i, 11) - 0.5) * 6; p.tam = false; p.surum = -1;
    if (i % 5 === 0) S.olay(p.bas, "tik", 0.3);
  });
  S.dinamik((f) => {
    const sv = temaSurum(), pal = KAGIT[temaAdi()];
    for (const p of PAR) {
      if (f < p.bas) { p.g.visible = false; p.tam = false; continue; }
      p.g.visible = true;
      const t = kis((f - p.bas) / YAP);
      if (p.tam && sv === p.surum) continue;
      if (sv !== p.surum) { p.pe.fillColor = p.renk(); p.gl.opacity = pal.gol; p.surum = sv; }
      const s = 0.85 + 0.15 * cikis(t);
      p.g.matrix = new P.Matrix().translate(p.cx, p.cy).rotate(p.rot).scale(s)
        .translate(-p.cx, -p.cy);
      p.g.opacity = t; p.tam = t >= 1;
    }
  });

  // --- yüz: kaş, göz, ağız = kalem çizgisi (sahne yapıştırmasından sonra)
  const pf = Math.max(1.5, 0.05 * h), YUZ = { duz: true, w: pf, amp: 0.1, uc0: 1.5, uc1: 2,
    aralik: 1.2, alfa: 0.92, renk: YM, ses: false, oge: og };
  const yuz = [];
  const yay = (rx, ry, a0, a1) => { const m = Math.max(8, Math.ceil(Math.abs(a1 - a0) / 15));
    return Array.from({ length: m }, (_, i) => {
      const a = (a0 + (a1 - a0) * i / (m - 1)) * Math.PI / 180;
      return [Math.cos(a) * rx, Math.sin(a) * ry]; }); };
  const halka = (px, rad, m = 8) => Array.from({ length: m + 1 }, (_, i) => {
    const a = 2 * Math.PI * i / m;
    return [px[0] + Math.cos(a) * rad, px[1] + Math.sin(a) * rad]; });
  dg.kas.forEach((q, i) => { const sg = i ? 1 : -1, by = -0.11 - q.y, a = q.a * Math.PI / 180;
    const hf = 0.085;
    const dx = Math.cos(a) * hf, dy = Math.sin(a) * hf;
    yuz.push([bk([[sg * 0.19 + sg * dx, by + dy], [sg * 0.19, by - 0.012],
      [sg * 0.19 - sg * dx, by - dy]]),
      { w: Math.max(1.6, 0.055 * h) }, 3]); });
  dg.goz.forEach((g, i) => { const sg = i ? 1 : -1, ex = sg * 0.19 + g.gx, ey = 0.03 + g.gy;
    if (g.s === "n") { const R_ = g.r * h;
      yuz.push([halka(hd(ex, ey), R_ * 0.45), { w: R_ * 1.15 }, 2]); }
    else if (g.s === "y") yuz.push([bk([[ex - 0.075, ey + 0.03], [ex - 0.04, ey - 0.02],
      [ex, ey - 0.04],
      [ex + 0.04, ey - 0.02], [ex + 0.075, ey + 0.03]]), { duz: false }, 2]);
    else yuz.push([bk([[ex - 0.07, ey - 0.01], [ex - 0.035, ey + 0.025], [ex, ey + 0.035],
      [ex + 0.035, ey + 0.025], [ex + 0.07, ey - 0.01]]), { duz: false }, 2]); });
  { const m = dg.agiz, dx = m.dx || 0, nn = m.c.length, my = 0.27, mw = Math.max(1.6, 0.055 * h);
    const ust = m.c.map((c, i) => [dx + (i / (nn - 1) - 0.5) * m.w, my + c]);
    if (m.tip === "o") yuz.push([bk(yay(m.w / 2, m.ac / 2, 0, 360).map((p) => [p[0] + dx,
      p[1] + my + 0.02])), { w: mw }, 4]);
    else if (m.ac) yuz.push([bk(ust.concat([[dx + m.w * 0.3, my + m.c[1] + m.ac * 0.8],
      [dx, my + m.c[1] + m.ac], [dx - m.w * 0.3, my + m.c[1] + m.ac * 0.8], ust[0]])),
      { duz: false, w: mw }, 4]);
    else yuz.push([bk(ust), { duz: false, w: mw }, 4]); }
  const yt = yuz.reduce((s, q) => s + q[2], 0);
  let cur = bas + sure - F;
  S.olay(cur, "cizgi", 0.3);
  for (const [pts, op, ag] of yuz) { const d = Math.max(2, F * ag / yt);
    S.ciz(pts, { ...YUZ, ...op, bas: cur, sure: d }); cur += d; }

  return { h, boy: T, k, bit: bas + sure,
    sinir: { x0: X - 1.2 * h, x1: X + 1.2 * h, y0: Yg - T, y1: Yg } };
}

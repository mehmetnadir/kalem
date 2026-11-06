// Kadro karakteri — parametrik model sayfası figürü (K28: kendi karakterimiz, telifli parça yok).
// karakter(S, {x, y, yas, duygu, kimlik, poz, boy, bas, sure, h, oge}) -> {h, boy, k, bit, sinir}
// x: figür ekseni · y: ayak tabanı · boy: toplam boy (px) ya da h: baş yüksekliği (px).
// Birim h = baş yüksekliği; bütün ölçüler h ile orantılıdır. Zaman yalnız kare numarasından gelir.
import { RT } from "/projeler/deneme-karakter/sahneler/02-paperjs-kanca/kalem-paper.js";

// Oran tablosu: k = toplam boy / h · omuz = omuz genişliği / h
export const ORAN = [
  { ad: "10–11", yas: 11, k: 4.5, omuz: 1.6 }, { ad: "12–13", yas: 13, k: 5.5, omuz: 1.8 },
  { ad: "14–15", yas: 15, k: 6.5, omuz: 2.0 }, { ad: "16–18", yas: 18, k: 7.0, omuz: 2.1 }];
export const OGRETMEN = { ad: "öğretmen", k: 7.5, omuz: 2.2 };
export const oran = (yas, kimlik) => kimlik === "ogretmen" ? OGRETMEN
  : ORAN.find((r) => yas <= r.yas) || ORAN[ORAN.length - 1];

// Kimlik (sabit): saç siluet + vurgu aksesuarı; mürekkep tek renk (RT.murekkep)
export const KIMLIK = {
  ogrenci_kiz: { sac: "A", aksesuar: "toka", etek: true },
  ogrenci_erkek: { sac: "B", aksesuar: "atki", etek: false },
  ogretmen: { sac: "C", aksesuar: "gozluk", etek: false } };

// Duygu = 2 kaş + 2 göz + 1 ağız. kas: [sol, sağ] {a: iç uç yukarı açı (°), y: yükseklik (h)}
// goz: [sol, sağ] {s: n nokta · y yay · k kapalı, r: yarıçap (h), gx, gy: bakış kayması (h)}
// agiz: {w: genişlik (h), c: soldan sağa dy örnekleri (h), ac: açıklık (h), dx, tip}
// tilt: baş eğimi (°, ≤ 8)
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

const FAZ = [["bas", 0, 0.12], ["sac", 0.12, 0.26], ["govde", 0.26, 0.46], ["kol", 0.46, 0.62],
  ["bacak", 0.62, 0.80], ["yuz", 0.80, 1]];                         // darbe sırası: baş → yüz
const uzun = (p) => p.reduce((s, q, i) => s + (i ? Math.hypot(q[0] - p[i - 1][0],
  q[1] - p[i - 1][1]) : 0), 0);

export function karakter(S, o) {
  const r = oran(o.yas, o.kimlik), kim = KIMLIK[o.kimlik], dg = DUYGU[o.duygu];
  if (!kim || !dg) throw new Error(`karakter: kimlik/duygu yok: ${o.kimlik}/${o.duygu}`);
  const k = r.k, h = o.boy ? o.boy / k : o.h || 28, T = k * h, X = o.x, Yg = o.y;
  const bas = o.bas || 0, sure = o.sure || 66, oturur = o.poz === "oturur";
  const pw = Math.max(1.6, 0.075 * h), pf = Math.max(1.4, 0.05 * h);
  const armW = 0.028 * T, legW = 0.036 * T, sw = r.omuz * h;
  const MUR = RT.murekkep, VUR = RT.vurgu, IKI = RT.ikincil;
  // gövde ölçüleri (px): omuz çizgisi ys, kalça hipY, etek hemY
  let top = Yg - T;
  const ys0 = top + 1.14 * h, R = T - 1.14 * h, hip0 = ys0 + 0.40 * R, L = Yg - hip0;
  if (oturur) top += 0.5 * L;                       // otururken gövde 0,5 bacak boyu iner
  const ys = top + 1.14 * h, hipY = ys + 0.40 * R, A = 0.46 * R;
  const hw = sw * 0.82, hem = hipY + (kim.etek ? 0.28 * h : 0), tw = sw - 2.2 * armW,
    hwHem = tw * (kim.etek ? 1.25 : 0.92);
  const cx = X, cy = top + 0.5 * h, tilt = dg.tilt * Math.PI / 180;
  // baş koordinatı (h birimi, merkez 0,0; üst −0,5 · çene +0,5) → px; baş boyun dibinden eğilir
  const hd = (u, v) => { const du = u, dv = v - 0.5, c = Math.cos(tilt), s = Math.sin(tilt);
    return [cx + (du * c - dv * s) * h, cy + (du * s + dv * c + 0.5) * h]; };
  const L_ = { bas: [], sac: [], govde: [], kol: [], bacak: [], yuz: [] };
  const ekle = (faz, pts, op = {}) => L_[faz].push({ pts, op });
  const KON = { duz: true, w: pw, amp: 0.2, uc0: 3, uc1: 4, aralik: 1.8, alfa: 0.92, renk: MUR };
  const YUZ = { duz: true, w: pf, amp: 0.1, uc0: 1.5, uc1: 2, aralik: 1.2, alfa: 0.92, renk: MUR };
  const yay = (rx, ry, a0, a1) => { const n = Math.max(8, Math.ceil(Math.abs(a1 - a0) / 15));
    return Array.from({ length: n }, (_, i) => {
      const a = (a0 + (a1 - a0) * i / (n - 1)) * Math.PI / 180;
      return [Math.cos(a) * rx, Math.sin(a) * ry]; }); };
  const halka = (px, rad, n = 9) => Array.from({ length: n + 1 }, (_, i) => {
    const a = 2 * Math.PI * i / n;
    return [px[0] + Math.cos(a) * rad, px[1] + Math.sin(a) * rad]; });
  const baskoy = (q) => q.map((p) => hd(p[0], p[1]));

  // --- baş: çene hattı (sol şakaktan sağ şakağa)
  ekle("bas", baskoy(yay(0.41, 0.5, 190, -10)), KON);
  // --- saç: siluet A (kuyruk + toka) · B (diken) · C (topuz + yan tutam + ortadan ayrık)
  const kapak = (s) => baskoy(yay(0.41 * s, 0.5 * s, 195, 345));
  if (kim.sac === "A") {
    ekle("sac", kapak(1.1), KON);
    ekle("sac", baskoy([[-0.4, 0.02], [-0.2, -0.22], [0.1, -0.3], [0.36, -0.12]]), KON);
    ekle("sac", baskoy([[0.34, -0.46], [0.62, -0.58], [0.8, -0.3], [0.74, 0.08], [0.62, 0.3]]),
      { ...KON, duz: false, w: 0.15 * h, uc1: 0.4 * h });
    ekle("sac", halka(hd(0.4, -0.45), 0.05 * h, 8), { ...KON, w: 0.1 * h, renk: VUR, alfa: 0.95 });
  } else if (kim.sac === "B") {
    ekle("sac", Array.from({ length: 9 }, (_, i) => { const a = (190 + i * 20) * Math.PI / 180,
      s = i % 2 ? 1.34 : 1.04; return hd(Math.cos(a) * 0.41 * s, Math.sin(a) * 0.5 * s); }), KON);
    ekle("sac", baskoy([[-0.38, -0.04], [-0.16, -0.24], [0.12, -0.28], [0.36, -0.1]]), KON);
  } else {
    ekle("sac", kapak(1.14), KON);
    ekle("sac", baskoy([[-0.4, -0.02], [-0.22, -0.24], [0, -0.33], [0.22, -0.24],
      [0.4, -0.02]]), KON);
    for (const sg of [-1, 1]) ekle("sac", baskoy([[sg * 0.45, -0.12], [sg * 0.5, 0.15],
      [sg * 0.44, 0.38]]), { ...KON, duz: false });
    ekle("sac", baskoy(yay(0.17, 0.17, 0, 360).map((p) => [p[0] - 0.4, p[1] - 0.52])), KON);
  }
  // --- gövde: boyun + gömlek hattı (tek darbe) + aksesuar (atkı)
  ekle("govde", [[X - 0.13 * h, top + 0.96 * h], [X - 0.13 * h, ys - 0.03 * h],
    [X - tw / 2, ys + 0.07 * h], [X - tw * 0.4, (ys + hipY) / 2], [X - hwHem / 2, hem],
    [X + hwHem / 2, hem], [X + tw * 0.4, (ys + hipY) / 2], [X + tw / 2, ys + 0.07 * h],
    [X + 0.13 * h, ys - 0.03 * h], [X + 0.13 * h, top + 0.96 * h]], KON);
  if (kim.aksesuar === "atki") {
    ekle("govde", [[X - 0.26 * h, ys - 0.06 * h], [X, ys + 0.06 * h],
      [X + 0.26 * h, ys - 0.06 * h]],
      { ...KON, duz: false, w: 0.17 * h, renk: VUR, alfa: 0.95 });
    ekle("govde", [[X + 0.08 * h, ys + 0.04 * h], [X + 0.14 * h, ys + 0.42 * h]],
      { ...KON, w: 0.12 * h, renk: VUR, alfa: 0.95 });
  }
  // --- kollar: omuzdan ele tek kalın darbe (kalınlık = 0,028 boy)
  const KOL = { ...KON, duz: false, w: armW, uc0: 0.1 * h, uc1: 0.3 * h };
  for (const sg of [-1, 1]) {
    const sx = X + sg * (sw / 2 - armW / 2), sy = ys + 0.1 * h;
    if (oturur) ekle("kol", [[sx, sy], [sx + sg * 0.04 * h, sy + A * 0.5],
      [X + sg * (hw * 0.24 + 0.1 * h), hipY + 0.25 * h]], KOL);
    else ekle("kol", [[sx, sy], [sx + sg * 0.01 * h, sy + A * 0.5],
      [sx + sg * 0.04 * h, sy + A]], KOL);
  }
  // --- bacaklar: kalça/etekten yere; ayak iç içe değil, dışa bakar (oturur: dizler + sandalye)
  const BAC = { ...KON, duz: false, w: legW, uc0: 0.1 * h, uc1: 0.2 * h };
  for (const sg of [-1, 1]) {
    const a = hw * 0.22, ax = X + sg * (a + 0.05 * h);
    if (oturur) {
      const diz = hipY + 0.35 * h;
      ekle("bacak", [[X + sg * a, hem], [X + sg * (a + 0.1 * h), diz]], BAC);
      ekle("bacak", [[X + sg * (a + 0.1 * h), diz], [ax + sg * 0.05 * h, Yg]], BAC);
      ekle("bacak", [[ax + sg * 0.05 * h - sg * 0.02 * h, Yg], [ax + sg * 0.38 * h, Yg]],
        { ...BAC, duz: true, w: legW * 0.9 });
      ekle("bacak", [[X + sg * hw * 0.85, hipY + 0.06 * h], [X + sg * hw * 0.9, Yg]],
        { ...KON, w: Math.max(1.4, pw * 0.8), renk: IKI, alfa: 0.8 });
    } else {
      ekle("bacak", [[X + sg * a, hem], [X + sg * (a + 0.03 * h), (hem + Yg) / 2], [ax, Yg]], BAC);
      ekle("bacak", [[ax - sg * 0.02 * h, Yg], [ax + sg * 0.34 * h, Yg]],
        { ...BAC, duz: true, w: legW * 0.9 });
    }
  }
  if (oturur) {
    ekle("bacak", [[X - hw * 0.95, hipY + 0.06 * h], [X + hw * 0.95, hipY + 0.06 * h]],
      { ...KON, renk: IKI, alfa: 0.8 });
    for (const sg of [-1, 1]) ekle("bacak", [[X + sg * hw * 0.95, hipY + 0.06 * h],
      [X + sg * hw * 0.95, ys + 0.5 * R * 0.6]], { ...KON, renk: IKI, alfa: 0.8 });
  }
  // --- yüz: 2 kaş + 2 göz + 1 ağız (+ gözlük)
  dg.kas.forEach((q, i) => {
    const sg = i ? 1 : -1, by = -0.11 - q.y, a = q.a * Math.PI / 180, hf = 0.085;
    const dx = Math.cos(a) * hf, dy = Math.sin(a) * hf;
    ekle("yuz", baskoy([[sg * 0.19 + sg * dx, by + dy], [sg * 0.19, by - 0.012],
      [sg * 0.19 - sg * dx, by - dy]]), { ...YUZ, w: Math.max(1.5, 0.055 * h) });
  });
  dg.goz.forEach((g, i) => {
    const sg = i ? 1 : -1, ex = sg * 0.19 + g.gx, ey = 0.03 + g.gy;
    if (g.s === "n") { const R_ = g.r * h; ekle("yuz", halka(hd(ex, ey), R_ * 0.45, 8),
      { ...YUZ, w: R_ * 1.15 }); }
    else if (g.s === "y") ekle("yuz", baskoy([[ex - 0.075, ey + 0.03], [ex - 0.04, ey - 0.02],
      [ex, ey - 0.04], [ex + 0.04, ey - 0.02], [ex + 0.075, ey + 0.03]]), { ...YUZ, duz: false });
    else ekle("yuz", baskoy([[ex - 0.07, ey - 0.01], [ex - 0.035, ey + 0.025], [ex, ey + 0.035],
      [ex + 0.035, ey + 0.025], [ex + 0.07, ey - 0.01]]), { ...YUZ, duz: false });
  });
  {
    const m = dg.agiz, dx = m.dx || 0, n = m.c.length, my = 0.27;
    const ust = m.c.map((c, i) => [dx + (i / (n - 1) - 0.5) * m.w, my + c]);
    if (m.tip === "o") ekle("yuz", baskoy(yay(m.w / 2, m.ac / 2, 0, 360).map((p) => [p[0] + dx,
      p[1] + my + 0.02])), { ...YUZ, w: Math.max(1.5, 0.06 * h) });
    else if (m.ac) ekle("yuz", baskoy(ust.concat([[dx + m.w * 0.3, my + m.c[1] + m.ac * 0.8],
      [dx, my + m.c[1] + m.ac], [dx - m.w * 0.3, my + m.c[1] + m.ac * 0.8], ust[0]])),
      { ...YUZ, duz: false, w: Math.max(1.5, 0.055 * h) });
    else ekle("yuz", baskoy(ust), { ...YUZ, duz: false, w: Math.max(1.5, 0.055 * h) });
  }
  if (kim.aksesuar === "gozluk") {
    for (const sg of [-1, 1]) ekle("yuz", baskoy(yay(0.15, 0.15, 0, 360).map((p) => [
      p[0] + sg * 0.19,
      p[1] + 0.03])), { ...YUZ, w: Math.max(1.5, 0.06 * h), renk: VUR, alfa: 0.95 });
    ekle("yuz", baskoy([[-0.045, 0.01], [0.045, 0.01]]), { ...YUZ, renk: VUR, alfa: 0.95 });
  }

  // --- sıralı zamanlama: her faz kendi aralığında, darbe başına uzunluk ağırlığı
  S.olay(bas, "cizgi", 0.4);
  for (const [ad, a, b] of FAZ) {
    const liste = L_[ad], ag = liste.map((q) => 4 + uzun(q.pts));
    const top_ = ag.reduce((s, v) => s + v, 0);
    let cur = bas + sure * a;
    liste.forEach((q, i) => { const s = sure * (b - a) * ag[i] / top_;
      S.ciz(q.pts, { ...q.op, bas: cur, sure: s, ses: false, oge: o.oge }); cur += s; });
  }
  S.olay(bas + sure * 0.8, "cizgi", 0.3);
  return { h, boy: T, k, bit: bas + sure,
    sinir: { x0: X - 1.2 * h, x1: X + 1.2 * h, y0: Yg - T, y1: Yg } };
}

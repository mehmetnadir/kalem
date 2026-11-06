// Kadro karakteri v2b — parametrik model sayfası figürü (K28: kendi karakterimiz, telifsiz).
// karakter(S, {x, y, yas, duygu, kimlik, poz, h | boy, bas, sure, oge}) -> {h, boy, k, bit, sinir}
// x: figür ekseni · y: ayak tabanı · h: baş yüksekliği (px, varsayılan 56) ya da boy: toplam (px)
// poz: "ayakta" (varsayılan) | "oturur" (sıra çizgisi; eller sırada) · bas/sure: kare (0/62)
// kimlik: ogrenci_kiz | ogrenci_erkek | ogretmen · duygu: DUYGU anahtarı (yüz + gövde pozu)
// Birim h = baş yüksekliği; bütün ölçüler h ile orantılıdır. Zaman yalnız kare numarasından gelir.
import { RT } from "/projeler/deneme-karakter/sahneler/02-paperjs-kanca/kalem-paper.js";

// Oran tablosu (iri baş): k = toplam boy / h · omuz = omuz genişliği / h
export const ORAN = [
  { ad: "10–11", yas: 11, k: 3.1, omuz: 1.2 }, { ad: "12–13", yas: 13, k: 3.3, omuz: 1.3 },
  { ad: "14–15", yas: 15, k: 3.5, omuz: 1.4 }, { ad: "16–18", yas: 18, k: 3.7, omuz: 1.45 }];
export const OGRETMEN = { ad: "öğretmen", k: 3.8, omuz: 1.5 };
export const oran = (yas, kimlik) => kimlik === "ogretmen" ? OGRETMEN
  : ORAN.find((r) => yas <= r.yas) || ORAN[ORAN.length - 1];

// Kimlik (sabit siluet): saç + vurgu aksesuarı + üst giysi + alt giysi; mürekkep tek renk
export const KIMLIK = {
  ogrenci_kiz: { sac: "A", aksesuar: "toka", ust: "tisort", alt: "etek" },
  ogrenci_erkek: { sac: "B", aksesuar: "atki", ust: "gomlek", alt: "pantolon" },
  ogretmen: { sac: "C", aksesuar: "gozluk", ust: "ceket", alt: "pantolon" } };

// Duygu → gövde pozu. [ekranda sol kol, sağ kol]: el hedefi x (eksenden dışa), y (omuz çizgisinden
// aşağı), ikisi de h biriminde; e: dirsek yönü (alt|ust|dis|ic); t: el türü (yumruk|acik|basparmak)
const el = (x, y, e, t = "yumruk") => ({ x, y, e, t });
const YAN = el(0.74, 1.38, "dis");
export const POZ = {
  notr: [YAN, YAN],
  dikkat: [el(0.07, 1.05, "dis"), el(0.07, 1.05, "dis")],
  dusunme: [el(-0.5, 0.95, "alt"), el(0.17, -0.03, "alt")],
  saskin: [el(1.5, 0.55, "alt", "acik"), el(1.5, 0.55, "alt", "acik")],
  kararsiz: [el(0.62, 0.9, "dis"), el(0.32, -1.0, "dis", "acik")],
  yanlis: [YAN, el(0.55, -0.5, "dis")],
  dogru: [YAN, el(0.95, 0.5, "alt", "basparmak")],
  sevinc: [el(0.9, -1.05, "dis", "acik"), el(0.9, -1.05, "dis", "acik")] };
const OMUZ_DUS = { yanlis: 0.12 };                    // omuz çizgisi h biriminde aşağı iner

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

const FAZ = [["bas", 0, 0.1], ["sac", 0.1, 0.22], ["govde", 0.22, 0.44], ["kol", 0.44, 0.64],
  ["bacak", 0.64, 0.82], ["yuz", 0.82, 1]];                         // darbe sırası: baş → yüz
const uzun = (p) => p.reduce((s, q, i) => s + (i ? Math.hypot(q[0] - p[i - 1][0],
  q[1] - p[i - 1][1]) : 0), 0);

export function karakter(S, o) {
  const r = oran(o.yas, o.kimlik), kim = KIMLIK[o.kimlik], dg = DUYGU[o.duygu];
  if (!kim || !dg) throw new Error(`karakter: kimlik/duygu yok: ${o.kimlik}/${o.duygu}`);
  const k = r.k, h = o.boy ? o.boy / k : o.h || 56, T = k * h, X = o.x, Yg = o.y;
  const bas = o.bas || 0, sure = o.sure || 62, oturur = o.poz === "oturur";
  const pw = Math.max(1.6, 0.075 * h), pf = Math.max(1.4, 0.05 * h);
  const MUR = RT.murekkep, VUR = RT.vurgu, IKI = RT.ikincil;
  // dikey (px): omuz çizgisi ys, kalça hipY; gövde Lt, bacak Lg; oturunca kalça 0,55 Lg çıkar
  const R = T - 1.14 * h, Lt = 0.46 * R, Lg = R - Lt, sd = (OMUZ_DUS[o.duygu] || 0) * h;
  const ys = oturur ? Yg - 0.55 * Lg - Lt : Yg - T + 1.14 * h, top = ys - 1.14 * h, hipY = ys + Lt;
  const ws = r.omuz * h / 2, cw = ws - 0.12 * h, tisort = kim.ust === "tisort";
  const masa = ys + 0.7 * Lt, Lc = oturur ? 0.7 * Lt : Lt;      // masa üstü: görünen gövde boyu Lc
  const ya = Yg - 0.1 * h, legC = cw * 0.5, hl = cw * 0.46, hb = cw * 0.34;
  const cx = X, cy = top + 0.5 * h, tilt = dg.tilt * Math.PI / 180;
  // baş koordinatı (h birimi, merkez 0,0; üst −0,5 · çene +0,5) → px; baş boyun dibinden eğilir
  const hd = (u, v) => { const du = u, dv = v - 0.5, c = Math.cos(tilt), s = Math.sin(tilt);
    return [cx + (du * c - dv * s) * h, cy + (du * s + dv * c + 0.5) * h]; };
  const L_ = { bas: [], sac: [], govde: [], kol: [], bacak: [], yuz: [] };
  const ekle = (faz, pts, op = {}) => L_[faz].push({ pts, op });
  const KON = { duz: true, w: pw, amp: 0.2, uc0: 3, uc1: 4, aralik: 1.8, alfa: 0.92, renk: MUR };
  const YUZ = { duz: true, w: pf, amp: 0.1, uc0: 1.5, uc1: 2, aralik: 1.2, alfa: 0.92, renk: MUR };
  const EGRI = { ...KON, duz: false };
  const yay = (rx, ry, a0, a1) => { const n = Math.max(8, Math.ceil(Math.abs(a1 - a0) / 15));
    return Array.from({ length: n }, (_, i) => {
      const a = (a0 + (a1 - a0) * i / (n - 1)) * Math.PI / 180;
      return [Math.cos(a) * rx, Math.sin(a) * ry]; }); };
  const halka = (px, rad, n = 9) => Array.from({ length: n + 1 }, (_, i) => {
    const a = 2 * Math.PI * i / n;
    return [px[0] + Math.cos(a) * rad, px[1] + Math.sin(a) * rad]; });
  const baskoy = (q) => q.map((p) => hd(p[0], p[1]));
  const yan = (sg, u, v) => [X + sg * u, v];                     // eksenden sg·u dışa

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
  // --- gövde: omuz hattı + yan çizgi (yumuşak eğri) + yaka + hem; giysi kimliğe göre
  for (const sg of [-1, 1]) {
    ekle("govde", [yan(sg, 0.15 * h, ys - 0.03 * h), yan(sg, ws * 0.6, ys + 0.02 * h + sd * 0.5),
      yan(sg, ws - 0.02 * h, ys + 0.1 * h + sd)], { ...EGRI, uc0: 2, uc1: 2 });
    const wy = ys + 0.42 * h + (Lc - 0.42 * h) * 0.5;
    ekle("govde", [yan(sg, cw, ys + 0.4 * h + sd * 0.5), yan(sg, cw + 0.015 * h, ys + 0.55 * h),
      yan(sg, cw - 0.045 * h, wy), yan(sg, cw + (oturur ? 0 : 0.03 * h), ys + Lc)],
      { ...EGRI, uc0: 2, uc1: 2 });
  }
  if (tisort) ekle("govde", [yan(-1, 0.17 * h, ys - 0.03 * h), yan(-1, 0.1 * h, ys + 0.1 * h),
    yan(1, 0, ys + 0.14 * h), yan(1, 0.1 * h, ys + 0.1 * h), yan(1, 0.17 * h, ys - 0.03 * h)],
    { ...EGRI, w: pf });
  else {
    ekle("govde", [yan(-1, 0.16 * h, ys - 0.04 * h), yan(1, 0, ys + 0.22 * h),
      yan(1, 0.16 * h, ys - 0.04 * h)], { ...KON, w: pf });
    if (kim.ust === "gomlek") {
      ekle("govde", [yan(1, 0, ys + 0.22 * h), yan(1, 0, ys + Lc)], { ...KON, w: pf });
      for (const v of [0.4, 0.62, 0.84]) if (v * Lt < Lc - 0.05 * h)
        ekle("govde", halka(yan(1, 0.0, ys + v * Lt), 0.022 * h, 6), { ...KON, w: 0.06 * h });
    } else {
      for (const sg of [-1, 1]) ekle("govde", [yan(sg, 0.16 * h, ys - 0.04 * h),
        yan(sg, 0.21 * h, ys + 0.3 * Lc), yan(sg, 0.06 * h, ys + 0.62 * Lc)], { ...EGRI, w: pf });
      ekle("govde", [yan(1, 0, ys + 0.62 * Lc), yan(1, 0, ys + Lc)], { ...KON, w: pf });
    }
  }
  if (!oturur) ekle("govde", [yan(-1, cw + 0.04 * h, hipY - 0.04 * h), yan(1, 0, hipY - 0.02 * h),
    yan(1, cw + 0.04 * h, hipY - 0.04 * h)], { ...EGRI, uc0: 2, uc1: 2 });
  if (kim.aksesuar === "atki") {
    ekle("govde", [[X - 0.26 * h, ys - 0.06 * h], [X, ys + 0.06 * h],
      [X + 0.26 * h, ys - 0.06 * h]],
      { ...KON, duz: false, w: 0.17 * h, renk: VUR, alfa: 0.95 });
    ekle("govde", [[X + 0.08 * h, ys + 0.04 * h], [X + 0.14 * h, ys + 0.42 * h]],
      { ...KON, w: 0.12 * h, renk: VUR, alfa: 0.95 });
  }
  // --- kollar: omuz → dirsek → el (iki kemikli çözüm); tişört: kısa kol (üst kalın, alt ince),
  // gömlek/ceket: uzun kol (iki kemik eşit) + bilek manşeti; sonra el
  const aw = 0.034 * T, ua = 0.78 * h, fa = 0.72 * h, yd = (masa - ys) / h - 0.1;
  const kemik = (s, t, a, b, e) => {
    const dx = t[0] - s[0], dy = t[1] - s[1], dl = Math.hypot(dx, dy) || 1e-3;
    const d = Math.min(Math.max(dl, Math.abs(a - b) + 1), a + b - 1), ux = dx / dl, uy = dy / dl;
    const al = (a * a - b * b + d * d) / (2 * d), pp = Math.sqrt(Math.max(0, a * a - al * al));
    const c = [[s[0] + ux * al - uy * pp, s[1] + uy * al + ux * pp],
      [s[0] + ux * al + uy * pp, s[1] + uy * al - ux * pp]];
    const sk = (q) => e === "alt" ? q[1] : e === "ust" ? -q[1]
      : e === "dis" ? Math.abs(q[0] - X) : -Math.abs(q[0] - X);
    return { E: sk(c[0]) >= sk(c[1]) ? c[0] : c[1], H: [s[0] + ux * d, s[1] + uy * d] };
  };
  const elCiz = (Hp, dr, tip) => {
    const c = [Hp[0] + dr[0] * 0.04 * h, Hp[1] + dr[1] * 0.04 * h];
    if (tip === "acik") {
      ekle("kol", halka(c, 0.1 * h, 8), { ...YUZ, w: pf });
      for (const a of [-0.55, 0, 0.55]) {
        const ca = Math.cos(a), sa = Math.sin(a);
        const vx = dr[0] * ca - dr[1] * sa, vy = dr[0] * sa + dr[1] * ca;
        ekle("kol", [[c[0] + vx * 0.1 * h, c[1] + vy * 0.1 * h],
          [c[0] + vx * 0.38 * h, c[1] + vy * 0.38 * h]], { ...YUZ, w: 0.06 * h }); }
    } else {
      ekle("kol", halka(c, 0.15 * h, 9), { ...YUZ, w: pf });
      if (tip === "basparmak") ekle("kol", [[c[0] + 0.02 * h, c[1] - 0.1 * h],
        [c[0] + 0.02 * h, c[1] - 0.42 * h]], { ...YUZ, duz: false, w: 0.08 * h, uc0: 1, uc1: 2 });
    }
  };
  POZ[o.duygu].forEach((p, i) => {
    const sg = i ? 1 : -1, S0 = yan(sg, ws - 0.06 * h, ys + 0.1 * h + sd);
    let ty = ys + p.y * h, tx = X + sg * p.x * h;
    if (oturur && p.y > yd) { ty = ys + yd * h; tx = X + sg * 0.2 * h; }
    const { E, H } = kemik(S0, [tx, ty], ua, fa, p.e);
    const dr = [H[0] - E[0], H[1] - E[1]], dl = Math.hypot(dr[0], dr[1]) || 1;
    const ud = [dr[0] / dl, dr[1] / dl];
    const KOL = { ...KON, duz: false, uc0: 2, uc1: 2 };
    if (tisort) {
      ekle("kol", [S0, E], { ...KOL, w: aw * 1.4 });
      ekle("kol", [E, H], { ...KOL, w: aw * 0.8 });
      const m = [(S0[0] + E[0]) / 2, (S0[1] + E[1]) / 2];
      const l = Math.hypot(E[0] - S0[0], E[1] - S0[1]) || 1;
      ekle("kol", [[m[0] - (E[1] - S0[1]) / l * aw, m[1] + (E[0] - S0[0]) / l * aw],
        [m[0] + (E[1] - S0[1]) / l * aw, m[1] - (E[0] - S0[0]) / l * aw]], { ...YUZ, w: pf });
    } else {
      ekle("kol", [S0, E, H], { ...KOL, w: aw * 1.25 });
      const m = [H[0] - ud[0] * 0.12 * h, H[1] - ud[1] * 0.12 * h];
      ekle("kol", [[m[0] - ud[1] * aw * 0.9, m[1] + ud[0] * aw * 0.9],
        [m[0] + ud[1] * aw * 0.9, m[1] - ud[0] * aw * 0.9]], { ...YUZ, w: pf });
    }
    elCiz(H, ud, p.t);
  });
  // --- alt giysi + ayakkabı (ayak dışa bakar); oturunca: sıra üstü + ayakları, dizden aşağı bacak
  const ayakkabi = (sg) => ekle("bacak", [yan(sg, legC - hb - 0.02 * h, ya),
    yan(sg, legC - hb - 0.05 * h, Yg), yan(sg, legC + hb + 0.34 * h, Yg),
    yan(sg, legC + hb + 0.3 * h, Yg - 0.07 * h),
    yan(sg, legC + hb, ya - 0.01 * h)], { ...KON, w: pf * 1.3 });
  const bacakBas = oturur ? masa + 0.14 * h : hipY;                // bacak çizgisinin üst ucu
  for (const sg of [-1, 1]) {
    if (kim.alt === "pantolon") {
      ekle("bacak", [yan(sg, cw * 0.98, bacakBas), yan(sg, legC + (hl + hb) / 2 + 0.01 * h,
        (bacakBas + ya) / 2), yan(sg, legC + hb, ya)], { ...EGRI, uc0: 2, uc1: 2 });
      ekle("bacak", [yan(sg, 0.02 * h, oturur ? bacakBas : bacakBas + 0.28 * Lg),
        yan(sg, legC - (hl + hb) / 2 + 0.02 * h, (bacakBas + ya) / 2 + 0.1 * Lg),
        yan(sg, legC - hb, ya)], { ...EGRI, uc0: 2, uc1: 2 });
    } else {
      ekle("bacak", [yan(sg, legC, oturur ? bacakBas : hipY + 0.55 * h), yan(sg, legC, ya)],
        { ...KON, w: pw * 0.9 });
    }
    ayakkabi(sg);
  }
  if (kim.alt === "etek" && !oturur) {
    for (const sg of [-1, 1]) ekle("bacak", [yan(sg, cw, hipY - 0.04 * h),
      yan(sg, cw * 1.35, hipY + 0.25 * h),
      yan(sg, cw * 1.6, hipY + 0.52 * h)], { ...EGRI, uc0: 2, uc1: 2 });
    ekle("bacak", [yan(-1, cw * 1.6, hipY + 0.52 * h), yan(1, 0, hipY + 0.56 * h),
      yan(1, cw * 1.6, hipY + 0.52 * h)], { ...EGRI, uc0: 2, uc1: 2 });
  }
  if (oturur) {
    const dw = 1.5 * h;
    ekle("bacak", [[X - dw, masa], [X + dw, masa]], { ...KON, w: pw * 1.15 });
    ekle("bacak", [[X - dw + 0.04 * h, masa + 0.1 * h], [X + dw - 0.04 * h, masa + 0.1 * h]],
      { ...KON, w: pf, renk: IKI, alfa: 0.85 });
    for (const sg of [-1, 1]) ekle("bacak", [yan(sg, dw - 0.12 * h, masa + 0.1 * h),
      yan(sg, dw - 0.08 * h, Yg)], { ...KON, w: pw * 0.8, renk: IKI, alfa: 0.8 });
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
  return { h, boy: Yg - top, k, bit: bas + sure,
    sinir: { x0: X - 1.2 * h, x1: X + 1.2 * h, y0: top, y1: Yg } };
}

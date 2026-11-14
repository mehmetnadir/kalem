// SAHNE 05 — Örnek 3/3 (düz canvas, 747 kare, t_bas 68,84; cümle 5). 02-04 YDT temel.
// Kendini çizen kalem; zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json.
// Sol kart: The train to İzmir leaves at 7 pm today. (tren + saat 7, TIMETABLE)
// Sağ kart: I am going to the movie theater tonight. (sinema bileti, ARRANGEMENT)
// Altta zaman çizgisi: now (nabız) → gelecek; now'ın sağında 7 pm ve tonight, now'dan iki kalem yayı.
import { surucu } from "/ortak/surucu.js";
import { KUNYE } from "/projeler/02-04-ydt-temel/ortak/kunye.js";
import { Sahne, RT, renkCoz, elips, kutu, altCizgi, olc, geriTasma } from "./sahne-ortak.js";

const KARE = 747, TBAS = 68.84, ICERIK = 735;
const ETKIN = ((i) => (i >= 0 ? i : 1))(KUNYE.ajanda.findIndex((a) => /example/i.test(a)));
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3", cumle: 5,
  etkin: ETKIN });
const MUR = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, DOLGU = RT.vurguDolgu;

// Oran: bütün ölçüler 1920 genişliğe göre mantıksal birim; u() tuval genişliğine çevirir.
const u = (n) => (n * S.cv.width) / 1920;
// Ekran metni sözlüğü: ses metni (Izmir, seven p.m.) → ekran (İzmir, 7 pm)
const EKRAN = { Izmir: "İzmir", seven: "7", "p.m.": "pm" };
const goster = (d) => d.map((s) => ({ ...s, sozcuk: EKRAN[s.sozcuk] || s.sozcuk }));

// Yerleşim: iki kart (y 130–620), altta zaman çizgisi (y 790)
const yerlesim = () => {
  const KW = u(810), KY = u(130), KH = u(490), PAD = u(40);
  return { KW, KY, KH, PAD, XL: u(100), XR: u(1010), GEN: KW - 2 * PAD, Y1: KY + u(90),
    YE: KY + KH - u(35), TY: u(790), TX0: u(160), TX1: u(1760), NX: u(420), X7: u(1060),
    XT: u(1400) };
};

// Nokta dizisinin yay uzunluğu.
const uzunluk = (p) => p.reduce((t, q, k) => (k ? t + Math.hypot(q[0] - p[k - 1][0],
  q[1] - p[k - 1][1]) : 0), 0);

// Kalem çizimi grubu (el çizimi, SVG'siz): parçalar [{p, o}] sırayla çizilir; kapı kutusu "cizim".
function elCizim(ad, parcalar, tb, sure, olayEnCok = 3) {
  const n = parcalar.length, xs = [], ys = [];
  parcalar.forEach(({ p }) => p.forEach(([x, y]) => { xs.push(x); ys.push(y); }));
  const kut = { x: Math.min(...xs) - u(6), y: Math.min(...ys) - u(6) };
  kut.w = Math.max(...xs) + u(6) - kut.x; kut.h = Math.max(...ys) + u(6) - kut.y;
  const cocuk = parcalar.map(({ p, o }, i) => {
    const dur = Math.min(sure * 0.5, 0.1 + uzunluk(p) / u(1800));
    const bas = tb + (n > 1 ? i / (n - 1) : 0) * (sure - dur);
    return S.darbe(p, { uc0: 8, uc1: 14, ...o }, bas, dur, i < olayEnCok ? undefined : false);
  });
  const fb = S.fr(tb);
  return { ciz: (ctx, f) => {
    if (f >= fb + 2) window.__kalemKutu?.ekle("cizim", ad, kut.x, kut.y, kut.w, kut.h);
    for (const c of cocuk) c.ciz(ctx, f);
  } };
}

// Dolu nokta (geri taşmalı belirme). Kapı kutusu yok (işaret ailesi).
function nokta(cx, cy, r, tb, renk) {
  const fb = S.fr(tb);
  S.bas(fb); S.olay(fb, "tik", 0.45);
  return { ciz: (ctx, f) => {
    if (f < fb) return;
    const k = Math.max(0, geriTasma((f - fb) / 8));
    ctx.save(); ctx.globalAlpha = 0.95; ctx.fillStyle = renkCoz(renk); ctx.beginPath();
    ctx.arc(cx, cy, r * k, 0, Math.PI * 2); ctx.fill(); ctx.restore();
  } };
}

// Kalem yayı (ikinci dereceden eğri) + ok ucu: a → b, tepe yüksekliği h (yukarı).
function yayOk(a, b, h) {
  const c = [(a[0] + b[0]) / 2, Math.min(a[1], b[1]) - 2 * h], g = [];
  for (let i = 0; i <= 24; i++) {
    const t = i / 24, m = 1 - t;
    g.push([m * m * a[0] + 2 * m * t * c[0] + t * t * b[0],
      m * m * a[1] + 2 * m * t * c[1] + t * t * b[1]]);
  }
  const dx = b[0] - c[0], dy = b[1] - c[1], l = Math.hypot(dx, dy) || 1, d = [dx / l, dy / l];
  const uc = (s) => {
    const ca = Math.cos(0.5 * s), sa = Math.sin(0.5 * s), q = u(24);
    return [[b[0] - (d[0] * ca - d[1] * sa) * q, b[1] - (d[0] * sa + d[1] * ca) * q], b];
  };
  return [g, uc(1), uc(-1)];
}

// Tren (yandan, sağa bakar): vagon + lokomotif + 4 tekerlek + ray + duman. ox, oy: sol üst.
function trenParcalari(ox, oy) {
  const P = (x, y) => [ox + u(x), oy + u(y)];
  const K = (x, y, w, h, t) => kutu(ox + u(x), oy + u(y), u(w), u(h), t);
  const govde = { w: u(4.5), renk: MUR }, ince = { w: u(3.6), renk: MUR }, p = [];
  const ekle = (dizi, o) => dizi.forEach((q) => p.push({ p: q, o }));
  ekle(K(200, 55, 170, 75, 31), govde);                                   // lokomotif gövdesi
  ekle(K(200, 10, 75, 45, 32), govde);                                    // kabin
  ekle(K(320, 22, 26, 33, 33), ince);                                     // baca
  p.push({ p: [P(370, 95), P(398, 130), P(370, 130)], o: { ...govde, duz: true } });   // ön burun
  ekle(K(0, 45, 175, 85, 34), govde);                                     // vagon
  p.push({ p: [P(175, 112), P(200, 112)], o: { ...ince, duz: true } });   // bağlantı
  ekle(K(20, 60, 50, 30, 35), ince);                                      // vagon camları
  ekle(K(100, 60, 50, 30, 36), ince);
  ekle(K(215, 20, 42, 25, 37), ince);                                     // kabin camı
  [40, 135, 240, 335].forEach((x, i) => p.push({ p: elips(ox + u(x), oy + u(138), u(17), u(17),
    0, 50 + i), o: govde }));                                             // tekerlekler
  p.push({ p: [P(-10, 158), P(420, 158)], o: { w: u(4), renk: IKINCIL, duz: true } });   // ray
  p.push({ p: elips(ox + u(345), oy + u(2), u(11), u(9), 0.2, 61),
    o: { w: u(3.4), renk: IKINCIL } });                                   // duman
  p.push({ p: elips(ox + u(372), oy + u(-16), u(8), u(7), 0.3, 62),
    o: { w: u(3.2), renk: IKINCIL } });
  return p;
}

// Saat: kadran + 4 çentik + yelkovan 12'de + akrep 7'de (sarı). cx, cy merkez, r yarıçap.
function saatParcalari(cx, cy, r) {
  const p = [{ p: elips(cx, cy, r, r * 0.97, 0.05, 41), o: { w: u(5), renk: MUR } }];
  [[0, -1], [1, 0], [0, 1], [-1, 0]].forEach(([a, b]) => p.push({ p: [[cx + a * r * 0.8,
    cy + b * r * 0.8], [cx + a * r * 0.66, cy + b * r * 0.66]],
  o: { w: u(4), renk: MUR, duz: true, uc0: 2, uc1: 3 } }));
  p.push({ p: [[cx, cy], [cx, cy - r * 0.66]], o: { w: u(5), renk: MUR, duz: true, uc0: 3, uc1: 5 } });
  const aci = (7 / 12) * Math.PI * 2;   // 7: saat yönünde 210°
  p.push({ p: [[cx, cy], [cx + Math.sin(aci) * r * 0.5, cy - Math.cos(aci) * r * 0.5]],
    o: { w: u(7), renk: SARI, duz: true, uc0: 3, uc1: 6 } });
  return p;
}

// Sinema bileti: iki yanında çentik, delik çizgisi, 3 baskı satırı; hafif eğik. cx, cy merkez.
function biletParcalari(cx, cy, egim) {
  const ce = Math.cos(egim), se = Math.sin(egim);
  const R = ([x, y]) => [cx + u(x) * ce - u(y) * se, cy + u(x) * se + u(y) * ce];
  // Çentik yayı: x0 kenarında, yon 1 sağ kenar (içe = sola), -1 sol kenar (içe = sağa)
  const yay = (x0, yon) => Array.from({ length: 13 }, (_, i) => {
    const a = -Math.PI / 2 + (i / 12) * Math.PI;
    return [x0 - yon * 22 * Math.cos(a), yon * 22 * Math.sin(a)];
  });
  const kenar = { w: u(4.5), renk: MUR, duz: true, uc0: 6, uc1: 10 };
  const p = [
    { p: [[-180, -70], [180, -70]].map(R), o: kenar },
    { p: [[180, -70], [180, -22], ...yay(180, 1), [180, 70]].map(R), o: kenar },
    { p: [[180, 70], [-180, 70]].map(R), o: kenar },
    { p: [[-180, 70], [-180, 22], ...yay(-180, -1), [-180, -70]].map(R), o: kenar },
  ];
  for (let i = 0; i < 6; i++) {
    const y0 = -58 + i * 20;
    p.push({ p: [[100, y0], [100, y0 + 11]].map(R),
      o: { w: u(3.4), renk: IKINCIL, duz: true, uc0: 2, uc1: 2 } });
  }
  [[-150, -30, 60], [-150, 0, 30], [-150, 30, 70]].forEach(([x0, y, x1]) => p.push({
    p: [[x0, y], [x1, y]].map(R), o: { w: u(4), renk: IKINCIL, duz: true, uc0: 4, uc1: 6 } }));
  return p;
}

async function kur() {
  await S.kur();
  const Y = yerlesim(), t0 = (ad, yakin) => S.t0(ad, yakin);

  // Cümleler (EN): ortak Fredoka boyu, en geniş satır kart içine sığar (en çok 58, taban 30)
  const dizi = { l: goster(S.dizi("The", 73.0, 9)), r: goster(S.dizi("I", 84.94, 8)) };
  const bol = { l: [4, 5], r: [5, 3] }, EK = u(4);
  let enGen = 0;
  for (const ad of Object.keys(dizi)) {
    let i = 0;
    for (const n of bol[ad]) {
      const s = dizi[ad].slice(i, i + n); i += n;
      enGen = Math.max(enGen, olc(`700 ${u(58)}px Fredoka`, s.map((k) => k.sozcuk).join(" "))
        + (n - 1) * EK);
    }
  }
  const PX = Math.max(u(30), Math.min(u(58), Math.floor((u(58) * Y.GEN) / enGen)));
  const F = `700 ${PX}px Fredoka`, SATIR = Math.round(PX * 1.38);
  const yaz = (ad, x) => S.cumleYaz({ sozcukler: dizi[ad], x, y: Y.Y1, font: F, satirH: SATIR,
    satirSay: bol[ad], bosluk: EK });
  const kartCiz = (x, tb, tohum, ad) => S.koy(S.kart({ x, y: Y.KY, w: Y.KW, h: Y.KH, tb, tohum,
    satirlar: [], ad, kutuSure: 0.14, kutuAralik: 0.1 }));
  const odak = (a, b, tb, tohum) => S.koy(S.darbe(altCizgi(a.x - u(2), b.x + b.w + u(2),
    a.y + u(30), tohum), { w: u(8), renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 500 + tohum },
  tb, 0.4, 0.55));
  const etiket = (metin, x, y, boy, renk, pen) => S.koy(S.elYazisi({ metin, x, y, boy, renk,
    ...(pen.sozcukler ? { sozcukler: pen.sozcukler } : { tb: pen.tb, sure: pen.sure }) }));
  const etiketAlt = (e, y, tb, tohum) => S.koy(S.darbe(altCizgi(e.x - u(4), e.x + e.w + u(4),
    y + u(16), tohum), { w: u(7), renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 560 + tohum },
  tb, 0.4, 0.5));
  const ortala = (metin, cx, boy) => cx - olc(`700 ${boy}px Caveat`, metin) / 2;
  // Zaman çizgisinde olay: dikey çentik + dolu nokta
  const centik = (x, tb, tohum) => {
    S.koy(S.darbe([[x, Y.TY - u(18)], [x, Y.TY + u(18)]], { duz: true, w: u(4), renk: MUR,
      uc0: 3, uc1: 3, tohum }, tb, 0.15, 0.45));
    S.koy(nokta(x, Y.TY, u(9), tb + 0.1, MUR));
  };
  // now'dan olaya kalem yayı (gövde + iki ok ucu)
  const yay = (x, h, tb, sure, tohum) => yayOk([Y.NX + u(14), Y.TY - u(20)],
    [x - u(8), Y.TY - u(22)], h).forEach((p, i) => S.koy(S.darbe(p, { w: u(4.5), renk: IKINCIL,
    uc0: 6, uc1: 8, duz: i > 0, tohum: tohum + i }, tb + (i ? sure - 0.05 : 0), i ? 0.12 : sure,
  i ? false : 0.5)));

  // 69,39 Üçüncü: sol kart · 70,83 İki (cümle): sağ kart
  kartCiz(Y.XL, t0("Üçüncü", 69.4), 1, "kart-sol");
  kartCiz(Y.XR, t0("İki", 70.8), 2, "kart-sag");

  // 71,55 geleceği: zaman çizgisi (sağa ok) + now noktası + "now" · 72,03 anlatıyor: gelecek sarı
  const tGel = t0("geleceği", 71.5), tAnl = t0("anlatıyor.", 72.0);
  S.koy(S.darbe([[Y.NX + u(18), Y.TY], [Y.TX1 - u(26), Y.TY]], { duz: true, w: u(16),
    renk: DOLGU, alfa: 0.45, uc0: 6, uc1: 10, tohum: 201 }, tAnl, 0.5, 0.45));
  S.koy(S.darbe([[Y.TX0, Y.TY], [Y.TX1, Y.TY]], { duz: true, w: u(4.5), renk: IKINCIL,
    uc0: 8, uc1: 6, tohum: 202 }, tGel, 0.5, 0.5));
  [1, -1].forEach((s, i) => S.koy(S.darbe([[Y.TX1 - u(26), Y.TY - s * u(16)], [Y.TX1, Y.TY]],
    { duz: true, w: u(4.5), renk: IKINCIL, uc0: 4, uc1: 4, tohum: 203 + i }, tGel + 0.45, 0.12,
    false)));
  S.koy(S.nabiz(Y.NX, Y.TY, u(12), tGel + 0.15));
  S.koy(nokta(Y.NX, Y.TY, u(11), tGel + 0.15, MUR));
  const TL = Y.TY + u(70), TB = u(52);
  etiket("now", ortala("now", Y.NX, TB), TL, TB, IKINCIL, { tb: tGel + 0.25, sure: 0.4 });

  // 73,00–76,44 sol cümle sözcük sözcük (konuşulan sözcük altında sarı çizgi kayar)
  const l = S.koy(yaz("l", Y.XL + Y.PAD));
  // 73,16 train: tren çizilir (kartın alt yarısı) · 74,76 seven: saat, akrep 7'de
  S.koy(elCizim("tren", trenParcalari(Y.XL + u(50), Y.KY + u(222)), t0("train", 73.2), 1.1));
  S.koy(elCizim("saat", saatParcalari(Y.XL + u(625), Y.KY + u(306), u(62)), t0("seven", 74.8),
    0.6));

  // 77,81 akşam (yedide): 7 pm çentiği + etiket · 78,53 kalkıyor: now → 7 pm yayı
  const tAk1 = t0("akşam", 77.8), tYed = t0("yedide", 78.2), tKal = t0("kalkıyor.", 78.5);
  centik(Y.X7, tAk1, 211);
  etiket("7 pm", ortala("7 pm", Y.X7, TB), TL, TB, MUR,
    { sozcukler: [{ t0: tAk1, t1: tYed }, { t0: tYed, t1: tKal }] });
  yay(Y.X7, u(34), tKal, 0.55, 220);

  // 80,37 tarifede (yazılı): TIMETABLE · 81,93 Tarifeli: altı sarı · 83,17 geniş: leaves odak
  const tTar = t0("tarifede", 80.4), tTfl = t0("Tarifeli", 81.9);
  const tt = etiket("TIMETABLE", Y.XL + Y.PAD, Y.YE, u(60), MUR,
    { sozcukler: [{ t0: tTar, t1: tTfl - 0.1 }] });
  etiketAlt(tt, Y.YE, tTfl, 1);
  odak(l.kel[4], l.kel[4], t0("geniş", 83.2), 1);

  // 84,94–87,42 sağ cümle · 85,82 movie: sinema bileti
  const r = S.koy(yaz("r", Y.XR + Y.PAD));
  S.koy(elCizim("bilet", biletParcalari(Y.XR + u(405), Y.KY + u(306), -0.06), t0("movie", 85.8),
    1.0));

  // 87,75 akşam (sinemaya): tonight çentiği + etiket · 88,63 gidiyorum: now → tonight yayı
  const tAk2 = t0("akşam", 87.75), tGit = t0("gidiyorum.", 88.6);
  centik(Y.XT, tAk2, 231);
  etiket("tonight", ortala("tonight", Y.XT, TB), TL, TB, MUR,
    { sozcukler: [{ t0: tAk2, t1: tGit - 0.05 }] });
  yay(Y.XT, u(58), tGit, 0.65, 240);

  // 89,63 Planı (ben yaptım): ARRANGEMENT · 91,07 Planlanmış: altı sarı · 92,43 şimdiki: am going
  const tPln = t0("Planı", 89.6), tPlm = t0("Planlanmış", 91.1);
  const ar = etiket("ARRANGEMENT", Y.XR + Y.PAD, Y.YE, u(60), MUR,
    { sozcukler: [{ t0: tPln, t1: tPlm - 0.1 }] });
  etiketAlt(ar, Y.YE, tPlm, 2);
  odak(r.kel[1], r.kel[2], t0("şimdiki", 92.4), 2);
}

surucu(kur, (f) => S.kare(f), KARE);

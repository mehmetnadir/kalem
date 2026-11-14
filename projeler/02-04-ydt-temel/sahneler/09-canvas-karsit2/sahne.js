// SAHNE 09 — Karşıt çift 2 (düz canvas, 523 kare, t_bas 145,29; cümle 10). 02-04 YDT temel.
// Kendini çizen kalem; zaman yalnız kare numarasından; sözcük zamanları anlatim/sozcukler.json.
// Üst kart (alt0, sahne 08'den): She is wearing her pink T-shirt today. · today → this day only
// Alt kart (alt1): The train to İzmir leaves at 7 pm today. · today + 7 pm → timetable
// Altta zaman çizgisi: today gün bandı, now (nabız) → 7 pm kalem oku; sonda RIGHT NOW ≠ TIMETABLE.
import { surucu } from "/ortak/surucu.js";
import { KUNYE } from "/projeler/02-04-ydt-temel/ortak/kunye.js";
import { Sahne, RT, renkCoz, elips, altCizgi, olc, geriTasma, yavasla } from "./sahne-ortak.js";

const KARE = 523, TBAS = 145.29, ICERIK = 511;
const ETKIN = ((i) => (i >= 0 ? i : 2))(KUNYE.ajanda.findIndex((a) => /contrast|pair/i.test(a)));
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Contrast 2 / 2", cumle: 10,
  etkin: ETKIN });
const MUR = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

// Oran: bütün ölçüler 1920 genişliğe göre mantıksal birim; u() tuval genişliğine çevirir.
const u = (n) => (n * S.cv.width) / 1920;
// Ekran metni sözlüğü: ses metni (Izmir, seven p.m.) → ekran (İzmir, 7 pm)
const EKRAN = { Izmir: "İzmir", seven: "7", "p.m.": "pm" };
const goster = (d) => d.map((s) => ({ ...s, sozcuk: EKRAN[s.sozcuk] || s.sozcuk }));
// Üst kart cümlesi (sahne 08, cümle 9) bu cümlede okunmaz: sabit yazı olarak geri gelir.
const UST = ["She", "is", "wearing", "her", "pink", "T-shirt", "today."];

// Yerleşim: üst kart y 116–316 (alt0), alt kart y 340–560 (alt1), zaman çizgisi y 700,
// son etiketler taban 896; kartın sağında çizim yuvası (IKON).
const yerlesim = () => ({ KX: u(100), KW: u(1720), PAD: u(40), Y0: u(116), H0: u(200),
  Y1: u(340), H1: u(220), IKON: u(230), TY: u(700), TX0: u(160), TX1: u(1760), BX0: u(380),
  BX1: u(1560), NX: u(620), X7: u(1300), EY: u(896) });

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

// Dolu nokta (geri taşmalı belirme). Kapı kutusu yok (işaret ailesi). ses 0: olay yazılmaz.
function nokta(cx, cy, r, tb, renk, ses = 0.45) {
  const fb = S.fr(tb);
  S.bas(fb); if (ses) S.olay(fb, "tik", ses);
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

// Düz kalem oku (yazı tipinde → yok): x0 → x1, y yüksekliğinde; gövde + iki uç.
const okParca = (x0, x1, y) => {
  const q = u(15);
  return [[[x0, y], [x1, y]], [[x1 - q, y - q * 0.7], [x1, y]], [[x1 - q, y + q * 0.7], [x1, y]]];
};

// ≠ işareti (yazı tipinde yok; kalemle): iki yatay çizgi + eğik çizgi.
const esitDegil = (cx, cy) => [[[cx - u(24), cy - u(13)], [cx + u(24), cy - u(13)]],
  [[cx - u(24), cy + u(13)], [cx + u(24), cy + u(13)]],
  [[cx + u(13), cy - u(36)], [cx - u(13), cy + u(36)]]];

// Tişört (sahne 03 ile aynı birim ızgara 100×90), kutuya ortalanır.
const TISORT = [
  { n: [[37, 4], [14, 12], [0, 36], [14, 46], [24, 37], [24, 88], [76, 88], [76, 37], [86, 46],
    [100, 36], [86, 12], [63, 4]], duz: true },
  { n: [[37, 4], [50, 14], [63, 4]] },
  { n: [[14, 12], [24, 37]], duz: true }, { n: [[86, 12], [76, 37]], duz: true },
];
function tisortParcalari(x, y, w, h) {
  const k = Math.min(w / 100, h / 90), ox = x + (w - 100 * k) / 2, oy = y + (h - 90 * k) / 2;
  return TISORT.map((d) => ({ p: d.n.map(([a, b]) => [ox + a * k, oy + b * k]),
    o: { w: u(4), renk: MUR, duz: d.duz } }));
}

// Küçük tren (yandan, sağa bakar; birim ızgara 200×90): vagon, lokomotif, kabin, baca, burun,
// 4 tekerlek, ray, duman. Kutuya ortalanır.
function trenParcalari(x, y, w, h) {
  const k = Math.min(w / 200, h / 90), ox = x + (w - 200 * k) / 2, oy = y + (h - 90 * k) / 2;
  const P = (a, b) => [ox + a * k, oy + b * k];
  const dik = (a, b, c, d) => [P(a, b), P(c, b), P(c, d), P(a, d), P(a, b)];
  const govde = { w: u(4), renk: MUR, duz: true }, ince = { w: u(3.4), renk: MUR, duz: true };
  const p = [
    { p: dik(96, 28, 178, 64), o: govde }, { p: dik(96, 6, 132, 28), o: govde },
    { p: dik(150, 12, 162, 28), o: ince },
    { p: [P(178, 46), P(192, 64), P(178, 64)], o: govde },
    { p: dik(0, 22, 84, 64), o: govde }, { p: [P(84, 56), P(96, 56)], o: ince },
  ];
  [20, 64, 116, 160].forEach((a, i) => p.push({ p: elips(ox + a * k, oy + 72 * k, 9 * k, 9 * k,
    0, 50 + i), o: { w: u(3.6), renk: MUR } }));
  p.push({ p: [P(-4, 86), P(204, 86)], o: { w: u(3.4), renk: IKINCIL, duz: true } });
  p.push({ p: elips(ox + 160 * k, oy + 2 * k, 6 * k, 5 * k, 0.2, 61),
    o: { w: u(3), renk: IKINCIL } });
  return p;
}

// Sabit cümle (bu cümlede okunmayan, önceki sahneden süren kart yazısı): sözcükler soldan sağa
// maskeyle hızla belirir; karaoke çizgisi yok. Sözcük konumları (x, w, y) odak için döner.
function sabitCumle(sozler, x, y, font, ek, tb, sure) {
  const boy = parseFloat(font.match(/(\d+(?:\.\d+)?)px/)[1]), bos = olc(font, " ");
  let xx = x;
  const kel = sozler.map((m) => {
    const k = { m, x: xx, w: olc(font, m), y }; xx += k.w + bos + ek; return k;
  });
  const top = xx - x, fb = S.fr(tb), n = Math.max(1, sure * 30);
  S.bas(fb);
  return { kel, ciz: (ctx, f) => {
    const a = yavasla((f - fb) / n); if (a <= 0) return;
    if (a >= 0.2) {
      kel.forEach((k) => window.__kalemKutu?.ekle("yazi", k.m, k.x, k.y - boy * 0.9, k.w,
        boy * 1.1));
    }
    ctx.save(); ctx.beginPath(); ctx.rect(x - u(6), y - boy * 1.1, (top + u(12)) * a, boy * 1.6);
    ctx.clip(); ctx.font = font; ctx.textAlign = "left"; ctx.textBaseline = "alphabetic";
    ctx.fillStyle = renkCoz(MUR); kel.forEach((k) => ctx.fillText(k.m, k.x, k.y)); ctx.restore();
  } };
}

async function kur() {
  await S.kur();
  const Y = yerlesim(), t0 = (ad, yakin) => S.t0(ad, yakin);
  const t1 = (ad, yakin) => S.dizi(ad, yakin, 1)[0].t1;

  // Ortak Fredoka boyu: iki cümlenin en genişi kart yazı alanına (çizim yuvası hariç) sığar
  const alt = goster(S.dizi("The", 145.84, 9)), EK = u(8), BAZ = u(56);
  const gen = (s, px) => olc(`700 ${px}px Fredoka`, s.join(" ")) + (s.length - 1) * EK;
  const enGen = Math.max(gen(UST, BAZ), gen(alt.map((k) => k.sozcuk), BAZ));
  const GEN = Y.KW - 2 * Y.PAD - Y.IKON;
  const PX = Math.max(u(30), Math.min(BAZ, Math.floor((BAZ * GEN) / enGen)));
  const F = `700 ${PX}px Fredoka`;
  // Sözcüğün noktalamasız genişliği (today. → today) ile odak altçizgisi
  const yalin = (k) => ({ ...k, w: olc(F, k.m.replace(/[.,:]$/, "")) });
  const odak = (a, b, tb, tohum, ses = 0.55) => S.koy(S.darbe(altCizgi(a.x - u(2),
    b.x + b.w + u(2), a.y + u(30), tohum), { w: u(8), renk: SARI, alfa: 0.9, uc0: 8, uc1: 14,
    tohum: 500 + tohum }, tb, 0.4, ses));
  const yaz = (metin, x, y, boy, renk, pen) => S.koy(S.elYazisi({ metin, x, y, boy, renk,
    ...pen }));
  const ortala = (metin, cx, boy) => cx - olc(`700 ${boy}px Caveat`, metin) / 2;
  const kalemOk = (x0, x1, y, tb, tohum, ses) => okParca(x0, x1, y).forEach((p, i) => S.koy(
    S.darbe(p, { duz: true, w: u(4.5), renk: MUR, uc0: 4, uc1: 6, tohum: tohum + i },
      tb + (i ? 0.18 : 0), i ? 0.08 : 0.2, i ? false : ses)));
  const NB = u(50), LB = u(48);   // kart notu ve zaman çizgisi etiketi boyu (Caveat)

  // ===== 145,72 sahne 08'den süren durum (0,3 sn içinde geri gelir; olay sesi yok) =====
  const tR = 145.72;
  // Zaman çizgisi: taban + ok ucu, today bandı (iki uç çentiği), now noktası + nabız, etiketler
  S.koy(S.darbe([[Y.BX0, Y.TY], [Y.BX1, Y.TY]], { duz: true, w: u(30), renk: IKINCIL, alfa: 0.18,
    uc0: 4, uc1: 4, tohum: 204 }, tR + 0.05, 0.25, false));
  S.koy(S.darbe([[Y.TX0, Y.TY], [Y.TX1, Y.TY]], { duz: true, w: u(4.5), renk: IKINCIL, uc0: 8,
    uc1: 6, tohum: 202 }, tR, 0.25, false));
  [1, -1].forEach((s, i) => S.koy(S.darbe([[Y.TX1 - u(26), Y.TY - s * u(16)], [Y.TX1, Y.TY]],
    { duz: true, w: u(4.5), renk: IKINCIL, uc0: 4, uc1: 4, tohum: 203 + i }, tR + 0.22, 0.08,
    false)));
  [Y.BX0, Y.BX1].forEach((x, i) => S.koy(S.darbe([[x, Y.TY - u(24)], [x, Y.TY + u(24)]],
    { duz: true, w: u(4), renk: IKINCIL, uc0: 3, uc1: 3, tohum: 206 + i }, tR + 0.1, 0.1, false)));
  S.koy(S.nabiz(Y.NX, Y.TY, u(12), tR + 0.15));
  S.koy(nokta(Y.NX, Y.TY, u(11), tR + 0.15, MUR, 0));
  yaz("today", Y.BX0 + u(8), Y.TY - u(40), LB, IKINCIL, { tb: tR + 0.1, sure: 0.25, ses: false });
  yaz("now", ortala("now", Y.NX, LB), Y.TY + u(78), LB, IKINCIL,
    { tb: tR + 0.2, sure: 0.2, ses: false });
  // Üst kart: çerçeve, cümle, not (today → this day only), tişört
  S.koy(S.kart({ x: Y.KX, y: Y.Y0, w: Y.KW, h: Y.H0, tb: tR, tohum: 1, satirlar: [],
    ad: "kart-ust", kutuSure: 0.08, kutuAralik: 0.05 }));
  const ust = S.koy(sabitCumle(UST, Y.KX + Y.PAD, Y.Y0 + u(84), F, EK, tR + 0.02, 0.3));
  const NY0 = Y.Y0 + u(170), n0 = yaz("today", Y.KX + Y.PAD, NY0, NB, MUR,
    { tb: tR + 0.08, sure: 0.2, ses: false });
  const ox0 = Y.KX + Y.PAD + n0.w + u(18);
  okParca(ox0, ox0 + u(56), NY0 - u(16)).forEach((p, i) => S.koy(S.darbe(p, { duz: true,
    w: u(4.5), renk: MUR, uc0: 4, uc1: 6, tohum: 230 + i }, tR + 0.2, 0.06, false)));
  yaz("this day only", ox0 + u(74), NY0, NB, MUR, { tb: tR + 0.22, sure: 0.25, ses: false });
  S.koy(elCizim("tisort", tisortParcalari(Y.KX + Y.KW - Y.PAD - u(170), Y.Y0 + u(24), u(170),
    Y.H0 - u(48)), tR + 0.05, 0.3, 0));

  // ===== cümle 10 · EN 145,84–148,80: alt kart, sözcük sözcük (karaoke altçizgi) =====
  S.koy(S.kart({ x: Y.KX, y: Y.Y1, w: Y.KW, h: Y.H1, tb: 145.76, tohum: 2, satirlar: [],
    ad: "kart-alt", kutuSure: 0.12, kutuAralik: 0.08 }));
  const r = S.koy(S.cumleYaz({ sozcukler: alt, x: Y.KX + Y.PAD, y: Y.Y1 + u(88), font: F,
    satirSay: [alt.length], bosluk: EK }));
  // 146,00 train: kartın sağında küçük tren
  S.koy(elCizim("tren", trenParcalari(Y.KX + Y.KW - Y.PAD - u(200), Y.Y1 + u(62), u(200),
    u(96)), t0("train", 146.0), 0.9));

  // ===== 149,69 today: not "today" · 150,57 saatle: 7 pm odak · 151,05 geliyor: "+ 7 pm" =====
  const NY1 = Y.Y1 + u(178), tTo = t0("today", 149.69), tSa = t0("saatle", 150.57);
  const tGe = t0("geliyor:", 151.05), n1 = yaz("today + 7 pm", Y.KX + Y.PAD, NY1, NB, MUR,
    { sozcukler: [{ t0: tTo, t1: t1("today", 149.69) }, { t0: tGe, t1: tGe + 0.22 },
      { t0: tGe + 0.26, t1: tGe + 0.42 }, { t0: tGe + 0.44, t1: t1("geliyor:", 151.05) }] });
  odak(r.kel[6], r.kel[7], tSa, 1);

  // ===== 151,85 akşam: zaman çizgisinde 7 pm çentiği + nokta · 152,25 yedi: "7 pm" etiketi =====
  const tAk = t0("akşam", 151.85), tYe = t0("yedi.", 152.25), tKa = t0("Kalkış", 153.01);
  S.koy(S.darbe([[Y.X7, Y.TY - u(18)], [Y.X7, Y.TY + u(18)]], { duz: true, w: u(4), renk: MUR,
    uc0: 3, uc1: 3, tohum: 211 }, tAk, 0.15, 0.45));
  S.koy(nokta(Y.X7, Y.TY, u(9), tAk + 0.1, MUR));
  yaz("7 pm", ortala("7 pm", Y.X7, LB), Y.TY + u(78), LB, MUR,
    { sozcukler: [{ t0: tYe, t1: tYe + 0.3 }, { t0: tYe + 0.32, t1: tKa - 0.05 }] });

  // ===== 153,45 henüz (olmadı): now → 7 pm kalem yayı — kalkış ileride =====
  const tHe = t0("henüz", 153.45);
  yayOk([Y.NX + u(14), Y.TY - u(20)], [Y.X7 - u(8), Y.TY - u(22)], u(50)).forEach((p, i) =>
    S.koy(S.darbe(p, { w: u(4.5), renk: IKINCIL, uc0: 6, uc1: 8, duz: i > 0, tohum: 220 + i },
      tHe + (i ? 0.75 : 0), i ? 0.12 : 0.8, i ? false : 0.5)));

  // ===== 154,93 tarifede (yazılı): not oku + "timetable" =====
  const tTa = t0("tarifede", 154.93), ox1 = Y.KX + Y.PAD + n1.w + u(18);
  kalemOk(ox1, ox1 + u(56), NY1 - u(16), tTa, 240, 0.45);
  yaz("timetable", ox1 + u(74), NY1, NB, MUR,
    { sozcukler: [{ t0: tTa + 0.3, t1: t1("yazılı.", 155.33) - 0.05 }] });

  // ===== 156,09 Geniş (zaman): leaves odak =====
  odak(r.kel[4], r.kel[4], t0("Geniş", 156.09), 2);

  // ===== 157,21 Today (iki cümlede de var): iki kartta today aynı anda odak =====
  const tTd = t0("Today", 157.21);
  odak(yalin(ust.kel[6]), yalin(ust.kel[6]), tTd, 3);
  odak(yalin(r.kel[8]), yalin(r.kel[8]), tTd, 4, false);

  // ===== 159,05 Farkı: ≠ · 160,57 konuşma anı: RIGHT NOW · 161,61 tarife: TIMETABLE =====
  esitDegil(u(960), Y.EY - u(20)).forEach((p, i) => S.koy(S.darbe(p, { duz: true, w: u(7),
    renk: MUR, alfa: 0.9, uc0: 4, uc1: 8, tohum: 700 + i }, t0("Farkı", 159.05) + i * 0.12, 0.14,
  i ? false : 0.5)));
  const EB = u(64), tKo = t0("konuşma", 160.57), tAn = t0("anı", 160.97);
  yaz("RIGHT NOW", ortala("RIGHT NOW", Y.NX, EB), Y.EY, EB, MUR,
    { sozcukler: [{ t0: tKo, t1: t1("konuşma", 160.57) }, { t0: tAn, t1: t1("anı", 160.97) }] });
  const tTf = t0("tarife", 161.61);
  yaz("TIMETABLE", ortala("TIMETABLE", Y.X7, EB), Y.EY, EB, MUR,
    { sozcukler: [{ t0: tTf, t1: tTf + 0.5 }] });
}

surucu(kur, (f) => S.kare(f), KARE);

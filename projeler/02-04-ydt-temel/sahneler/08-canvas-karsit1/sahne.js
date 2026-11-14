// SAHNE 08 — Karşıt çift 1 (düz canvas, 459 kare, t_bas 130,40; cümle 9). 02-04 YDT temel.
// Kendini çizen kalem; zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json.
// Kart (alt0): She is wearing her pink T-shirt today. + köşede küçük tişört.
// Altta zaman çizgisi: today gün bandı, now noktası bandın içinde nabız; bandın üstünde
// "today → this day only" (ekran metni). Ölçü mantıksal px (1920 tabanı) → u(); sabit px yok.
import { surucu } from "/ortak/surucu.js";
import { KUNYE } from "/projeler/02-04-ydt-temel/ortak/kunye.js";
import { Sahne, RT, renkCoz, elips, ok, altCizgi, olc, geriTasma } from "./sahne-ortak.js";

const KARE = 459, TBAS = 130.4, ICERIK = 447;
// Künye ajandasında "Contrast" varsa o, yoksa Rule (karşıt çift kural kartından sonra gelir)
const ETKIN = ((i) => (i >= 0 ? i : 2))(KUNYE.ajanda.findIndex((a) => /contrast|pair/i.test(a)));
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Contrast 1 / 2", cumle: 9,
  etkin: ETKIN });
const MUR = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, DOLGU = RT.vurguDolgu;

// Cümle 9 parça 2 (EN "She is wearing her pink T-shirt today.") sozcukler.json'da YOK.
// Başlar: cumle-9.wav (md5 052b069b…) faster-whisper turbo sözcük zamanı (clip 4,5–7,5) + 40 ms
// RMS zarfı; parça penceresi 4,65–7,37 sn (sureler.json); küresel sn = 130,95 + yerel. Ölçüm 14.11.
const EN = [["She", 135.61, 135.87], ["is", 135.89, 135.97], ["wearing", 135.97, 136.31],
  ["her", 136.33, 136.47], ["pink", 136.51, 136.75], ["T-shirt", 136.87, 137.25],
  ["today.", 137.29, 137.69]].map(([sozcuk, t0, t1]) => ({ sozcuk, t0, t1 }));

// Oran: bütün ölçüler 1920 genişliğe göre mantıksal birim; u() tuval genişliğine çevirir.
const u = (n) => (n * S.cv.width) / 1920;

// Yerleşim: kart y 150–470 (alt0, tam genişlik), başlık notu y 680, zaman çizgisi y 800
const yerlesim = () => {
  const KX = u(120), KY = u(150), KW = u(1680), KH = u(320), PAD = u(60), IW = u(150);
  const IX = KX + KW - PAD - IW;                       // tişört kutusu sol kenarı
  return { KX, KY, KW, KH, PAD, IW, IX, IY: KY + KH / 2 - u(68), GEN: IX - u(60) - (KX + PAD),
    TY: u(800), TX0: u(200), TX1: u(1720), BX0: u(700), BX1: u(1220), NX: u(900), TL: u(680) };
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
  return { kut, ciz: (ctx, f) => {
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

// Tişört (02-04 sahne 03 ile aynı biçim): birim ızgara 100×90 → s ölçekli, ox, oy sol üst.
function tisortParcalari(ox, oy, s) {
  const P = (x, y) => [ox + x * s, oy + y * s];
  const govde = { w: u(4.5), renk: MUR }, ince = { w: u(3.6), renk: MUR };
  return [
    { p: [[37, 4], [14, 12], [0, 36], [14, 46], [24, 37], [24, 88], [76, 88], [76, 37], [86, 46],
      [100, 36], [86, 12], [63, 4]].map(([x, y]) => P(x, y)), o: { ...govde, duz: true } },
    { p: [P(37, 4), P(50, 14), P(63, 4)], o: ince },
    { p: [P(14, 12), P(24, 37)], o: { ...ince, duz: true } },
    { p: [P(86, 12), P(76, 37)], o: { ...ince, duz: true } },
  ];
}

async function kur() {
  await S.kur();
  const Y = yerlesim(), t0 = (ad, yakin) => S.t0(ad, yakin);

  // Cümle (EN): tek satır, Fredoka; tişört kutusunun soluna sığar (en çok 76, taban 30)
  const EK = u(6), KAT = u(76);
  const enGen = olc(`700 ${KAT}px Fredoka`, EN.map((k) => k.sozcuk).join(" ")) + (EN.length - 1) * EK;
  const PX = Math.max(u(30), Math.min(KAT, Math.floor((KAT * Y.GEN) / enGen)));
  const F = `700 ${PX}px Fredoka`;
  const Y1 = Y.KY + Y.KH / 2 + PX * 0.35;              // taban: kart ortası
  const odak = (a, b, tb, tohum, bw) => S.koy(S.darbe(altCizgi(a.x - u(2), b.x + (bw || b.w) + u(2),
    a.y + u(30), tohum), { w: u(8), renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 500 + tohum },
  tb, 0.4, 0.55));

  // 130,95 Karşıt (çift.): kart çerçevesi
  S.koy(S.kart({ x: Y.KX, y: Y.KY, w: Y.KW, h: Y.KH, tb: t0("Karşıt", 130.95), tohum: 8,
    satirlar: [], ad: "kart", kutuSure: 0.2, kutuAralik: 0.12 }));

  // Başlık notu "today → this day only": bant üstünde ortalı (Caveat, ölçüyle)
  const NB = u(64), CF = `700 ${NB}px Caveat`, ARA = u(22), OKW = u(84);
  const wT = olc(CF, "today"), wR = olc(CF, "this day only");
  const NX0 = (Y.BX0 + Y.BX1) / 2 - (wT + 2 * ARA + OKW + wR) / 2;
  // 134,95 today. («aynı sözcük var: today»): "today" yazılır
  const tTd1 = t0("today.", 134.95);
  const nT = S.koy(S.elYazisi({ metin: "today", x: NX0, y: Y.TL, boy: NB, renk: MUR,
    sozcukler: [{ t0: tTd1, t1: tTd1 + 0.4 }] }));

  // 135,61–137,69 cümle sözcük sözcük (konuşulan sözcük altında sarı çizgi kayar)
  const cum = S.koy(S.cumleYaz({ sozcukler: EN, x: Y.KX + Y.PAD, y: Y1, font: F,
    satirH: PX * 1.4, satirSay: [EN.length], bosluk: EK }));
  const kel = (i) => cum.kel[i];                       // 0 She · 1 is · 2 wearing · 5 T-shirt · 6 today.

  // 136,87 T-shirt: tişört kalemle (kart sağ köşesi, küçük)
  const tis = S.koy(elCizim("tisort", tisortParcalari(Y.IX, Y.IY, Y.IW / 100), EN[5].t0, 0.75));

  // 138,57 Burada: zaman çizgisi ekseni (sağa ok)
  const tBur = t0("Burada", 138.57);
  S.koy(S.darbe([[Y.TX0, Y.TY], [Y.TX1, Y.TY]], { duz: true, w: u(4.5), renk: IKINCIL,
    uc0: 8, uc1: 6, tohum: 202 }, tBur, 0.5, 0.5));
  [1, -1].forEach((s, i) => S.koy(S.darbe([[Y.TX1 - u(26), Y.TY - s * u(16)], [Y.TX1, Y.TY]],
    { duz: true, w: u(4.5), renk: IKINCIL, uc0: 4, uc1: 4, tohum: 203 + i }, tBur + 0.45, 0.12,
    false)));

  // 139,21 today: cümledeki today ve nottaki today aynı anda sarı altı çizili (çoklu odak)
  const tTd2 = t0("today", 139.21);
  odak(kel(6), kel(6), tTd2, 1, olc(F, "today"));
  S.koy(S.darbe(altCizgi(nT.x - u(4), nT.x + nT.w + u(4), Y.TL + u(16), 2),
    { w: u(7), renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 562 }, tTd2 + 0.08, 0.4, false));

  // 139,93 bugünü: today gün bandı + iki uç çentiği
  const tBug = t0("bugünü", 139.93), tGos = t0("gösterir.", 140.29);
  S.koy(S.darbe([[Y.BX0, Y.TY], [Y.BX1, Y.TY]], { duz: true, w: u(28), renk: DOLGU, alfa: 0.45,
    uc0: 4, uc1: 4, tohum: 211 }, tBug, 0.45, 0.5));
  [Y.BX0, Y.BX1].forEach((x, i) => S.koy(S.darbe([[x, Y.TY - u(28)], [x, Y.TY + u(28)]],
    { duz: true, w: u(4.5), renk: MUR, uc0: 3, uc1: 3, tohum: 212 + i }, tBug + 0.1 + i * 0.12,
    0.15, i ? false : 0.45)));

  // 140,05 → ve 140,29–140,89 (bugünü) gösterir: "this day only"
  const okY = Y.TL - NB * 0.28, okX0 = NX0 + wT + ARA;
  ok([okX0, okY], [okX0 + OKW, okY], 7).forEach((p, i) => S.koy(S.darbe(p, { duz: i > 0,
    w: u(4.5), renk: MUR, uc0: 4, uc1: 6, tohum: 221 + i }, tBug + 0.12 + (i ? 0.22 : 0),
  i ? 0.1 : 0.25, i ? false : 0.4)));
  S.koy(S.elYazisi({ metin: "this day only", x: okX0 + OKW + ARA, y: Y.TL, boy: NB, renk: MUR,
    tb: tGos, sure: Math.max(0.5, S.sozc.find((s) => s.t0 === tGos).t1 - tGos) }));

  // 141,77 kıyafet: tişörtün çevresine sarı kalem halkası (bugünkü kıyafet)
  const tc = { x: tis.kut.x + tis.kut.w / 2, y: tis.kut.y + tis.kut.h / 2 };
  S.koy(S.darbe(elips(tc.x, tc.y, tis.kut.w / 2 + u(16), tis.kut.h / 2 + u(14), -0.05, 31),
    { w: u(6), renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, t0("kıyafet:", 141.77), 0.45, 0.55));

  // 142,57 konuşma (anında): now noktası bandın içinde + nabız · 143,05 anında: "now"
  const tKon = t0("konuşma", 142.57), tAn = t0("anında", 143.05);
  S.koy(S.nabiz(Y.NX, Y.TY, u(12), tKon + 0.1));
  S.koy(nokta(Y.NX, Y.TY, u(12), tKon, MUR));
  const LB = u(54);
  S.koy(S.elYazisi({ metin: "now", x: Y.NX - olc(`700 ${LB}px Caveat`, "now") / 2,
    y: Y.TY + u(92), boy: LB, renk: IKINCIL, tb: tAn, sure: 0.4 }));

  // 144,37 şimdiki (zaman): is wearing sarı altı çizili
  odak(kel(1), kel(2), t0("şimdiki", 144.37), 3);
}

surucu(kur, (f) => S.kare(f), KARE);

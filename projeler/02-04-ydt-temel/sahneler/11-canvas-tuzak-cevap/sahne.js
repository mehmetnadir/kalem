// SAHNE 11 — Tuzak cevabı (düz canvas, 657 kare, t_bas 183,79; cümle 13). 02-04 YDT temel.
// Kendini çizen kalem; zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json.
// İki kart alt alta: I am living in İstanbul. → for now (temporary) · I live in İstanbul. → always (permanent).
// Her kartın altında zaman çizgisi (Örnek 2'den geri gelir): üstte kısa bant, altta uzun bant; now iki
// çizgide aynı x. Kartlar arasında kalemle "≠ meaning" (çarpı yok; iki cümle de doğru). Sağ altta öğrenci
// başı (peeps-kit/ogrenci-bas.svg); cevap bitiminde 1 sn baş sallar. Ölçü mantıksal px (1920) → u().
import { surucu } from "/ortak/surucu.js";
import { KUNYE } from "/projeler/02-04-ydt-temel/ortak/kunye.js";
import { Sahne, RT, renkCoz, ok, altCizgi, olc, geriTasma } from "./sahne-ortak.js";

const KARE = 657, TBAS = 183.79, ICERIK = 645;
const ETKIN = ((i) => (i >= 0 ? i : 3))(KUNYE.ajanda.findIndex((a) => /trap/i.test(a)));
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Trap · answer", cumle: 13,
  etkin: ETKIN });
const MUR = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, DOLGU = RT.vurguDolgu;
const KOKDIZ = "/projeler/02-04-ydt-temel/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();

// Oran: bütün ölçüler 1920 genişliğe göre mantıksal birim; u() tuval genişliğine çevirir.
const u = (n) => (n * S.cv.width) / 1920;

// Yerleşim: kart 1 y 140–310 · zaman çizgisi 1 y 380 · "≠ meaning" taban y 540 · kart 2 y 590–760 ·
// zaman çizgisi 2 y 830 · öğrenci başı sağ alt (zaman çizgisi bitiminin sağı, ajanda künyesinin üstü).
const yerlesim = () => ({
  KX: u(120), KW: u(1480), KH: u(170), PAD: u(56), GAP: u(56), K1Y: u(140), K2Y: u(590),
  T1Y: u(380), T2Y: u(830), AX0: u(200), AX1: u(1560), NX: u(1240),
  B1: [u(1120), u(1360)], B2: [u(250), u(1510)], MY: u(540),
  OG: { x: u(1660), y: u(770), w: u(140), h: u(192) },
});

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

async function kur() {
  await S.kur();
  const Y = yerlesim(), t0 = (ad, yakin) => S.t0(ad, yakin);
  const bas = await svgOku("peeps-kit/ogrenci-bas.svg");

  // Cümleler (EN parçalar sozcukler.json'da var). Ekran metni İstanbul (noktalı İ).
  const ist = (w) => ({ ...w, sozcuk: w.sozcuk.replace(/^Istanbul/, "İstanbul") });
  const a = S.dizi("I", 187.11, 5).map(ist);           // I am living in İstanbul.
  const b = S.dizi("I", 194.89, 4).map(ist);           // I live in İstanbul.
  const metin = (s) => s.map((k) => k.sozcuk).join(" ");

  // Yazı boyu: cümle + sağdaki not (→ for now (temporary)) kart iç genişliğine sığar; taban 30.
  const EK = u(6), OKW = u(70), ARA = u(20), P0 = u(72), L0 = u(64);
  const wCum = (px, s) => olc(`700 ${px}px Fredoka`, metin(s)) + (s.length - 1) * EK;
  const wNot = (px) => OKW + ARA + Math.max(olc(`700 ${px}px Caveat`, "for now (temporary)"),
    olc(`700 ${px}px Caveat`, "always (permanent)"));
  const IC = Y.KW - 2 * Y.PAD - Y.GAP;
  const oran = Math.min(1, IC / (Math.max(wCum(P0, a), wCum(P0, b)) + wNot(L0)));
  const PX = Math.max(u(30), Math.floor(P0 * oran)), LP = Math.max(u(30), Math.floor(L0 * oran));
  const F = `700 ${PX}px Fredoka`, CF = `700 ${LP}px Caveat`;
  const LX = Y.KX + Y.PAD + Math.max(wCum(PX, a), wCum(PX, b)) + Y.GAP;   // not sütunu (iki kartta aynı)
  const taban = (ky) => ky + Y.KH / 2 + PX * 0.35;
  const Y1 = taban(Y.K1Y), Y2 = taban(Y.K2Y);
  const sari = (x0, x1, y, tb, tohum, ses = 0.55) => S.koy(S.darbe(altCizgi(x0, x1, y, tohum),
    { w: u(8), renk: SARI, alfa: 0.9, uc0: 8, uc1: 14, tohum: 500 + tohum }, tb, 0.4, ses));

  // 184,20 öğrenci başı (soru anı 2'nin sahibi) sağ altta kalemle; 202,30'da 1 sn baş sallar
  const og = S.koy(S.cizim({ svg: bas, ad: "ogrenci", kutu: Y.OG, esik: 0.004, enCok: 60, w: u(3.2),
    tb: 184.2, sure: 0.55, olayEnCok: 3, nefes: false }));
  const fSal = S.fr(202.3), ocx = Y.OG.x + Y.OG.w / 2, ocy = Y.OG.y + Y.OG.h;
  og.donusum = (f) => {
    const p = (f - fSal) / 30, ty = p > 0 && p < 1 ? Y.OG.h * 0.06 * Math.sin(Math.PI * 2 * p) ** 2 : 0;
    return { cx: ocx, cy: ocy, tx: 0, ty, dondur: 0, olcek: 1 };
  };

  // 184,54 «Olur,»: kart 1 çerçevesi · 185,42 «ama»: kart 2 çerçevesi
  S.koy(S.kart({ x: Y.KX, y: Y.K1Y, w: Y.KW, h: Y.KH, tb: t0("Olur,", 184.54), tohum: 11,
    satirlar: [], ad: "kart-1", kutuSure: 0.2, kutuAralik: 0.12 }));
  S.koy(S.kart({ x: Y.KX, y: Y.K2Y, w: Y.KW, h: Y.KH, tb: t0("ama", 185.42), tohum: 12,
    satirlar: [], ad: "kart-2", kutuSure: 0.2, kutuAralik: 0.12 }));

  // 185,90 «anlam değişir.»: kartlar arasında "≠ meaning" (≠ sarı kalem, meaning el yazısı)
  const MP = u(72), MF = `700 ${MP}px Caveat`, wM = olc(MF, "meaning"), NE = MP * 0.6, NA = MP * 0.3;
  const nx0 = Y.KX + Y.KW / 2 - (NE + NA + wM) / 2, ncy = Y.MY - MP * 0.3, tAn = t0("anlam", 185.9);
  [[[nx0, ncy - MP * 0.11], [nx0 + NE, ncy - MP * 0.11]], [[nx0, ncy + MP * 0.11], [nx0 + NE, ncy + MP * 0.11]],
    [[nx0 + NE * 0.68, ncy - MP * 0.34], [nx0 + NE * 0.32, ncy + MP * 0.34]]].forEach((p, i) =>
    S.koy(S.darbe(p, { duz: true, w: u(6), renk: SARI, alfa: 0.9, uc0: 4, uc1: 6, tohum: 300 + i },
      tAn + i * 0.1, 0.16, i ? false : 0.5)));
  const tDeg = t0("değişir.", 186.22);
  const nM = S.koy(S.elYazisi({ metin: "meaning", x: nx0 + NE + NA, y: Y.MY, boy: MP, renk: MUR,
    tb: tDeg, sure: 0.6 }));

  // 187,11–188,95 kart 1 cümlesi sözcük sözcük (konuşulan sözcük altında sarı çizgi kayar)
  const c1 = S.koy(S.cumleYaz({ sozcukler: a, x: Y.KX + Y.PAD, y: Y1, font: F, satirH: PX * 1.4,
    satirSay: [a.length], bosluk: EK }));

  // Not: ok + el yazısı (→ for now · → always), parantezli sözcük ayrı anda yazılır
  const okY = (yb) => yb - LP * 0.28;
  const notOk = (yb, tb, tohum) => ok([LX, okY(yb)], [LX + OKW, okY(yb)], tohum).forEach((p, i) =>
    S.koy(S.darbe(p, { duz: i > 0, w: u(4.5), renk: MUR, uc0: 4, uc1: 6, tohum: tohum + i },
      tb + (i ? 0.2 : 0), i ? 0.1 : 0.22, i ? false : 0.4)));
  const NTX = LX + OKW + ARA;
  // 189,12 «Şimdilik»: → for now
  const tSim = t0("Şimdilik", 189.12);
  notOk(Y1, tSim, 231);
  S.koy(S.elYazisi({ metin: "for now", x: NTX, y: Y1, boy: LP, renk: MUR, tb: tSim + 0.18, sure: 0.5 }));

  // Zaman çizgisi: eksen + sağ ok, now noktası + etiket, bant (vurgu dolgusu %45) + uç çentikleri
  const LB = u(44), LBF = `700 ${LB}px Caveat`;
  const zamanCizgisi = (ad, TY, bant, tEksen, tNokta, tBant, bantSure, tohum) => {
    S.koy(S.darbe([[Y.AX0, TY], [Y.AX1, TY]], { duz: true, w: u(4.5), renk: IKINCIL, uc0: 8, uc1: 6,
      tohum }, tEksen, 0.45, 0.5));
    [1, -1].forEach((s, i) => S.koy(S.darbe([[Y.AX1 - u(26), TY - s * u(16)], [Y.AX1, TY]],
      { duz: true, w: u(4.5), renk: IKINCIL, uc0: 4, uc1: 4, tohum: tohum + 1 + i }, tEksen + 0.4, 0.12,
      false)));
    S.koy(S.darbe([[bant[0], TY], [bant[1], TY]], { duz: true, w: u(28), renk: DOLGU, alfa: 0.45,
      uc0: 4, uc1: 4, tohum: tohum + 3 }, tBant, bantSure, 0.5));
    bant.forEach((x, i) => S.koy(S.darbe([[x, TY - u(26)], [x, TY + u(26)]], { duz: true, w: u(4.5),
      renk: MUR, uc0: 3, uc1: 3, tohum: tohum + 4 + i }, tBant + bantSure * 0.5 + i * 0.12, 0.15,
    false)));
    S.koy(nokta(Y.NX, TY, u(12), tNokta, MUR));
    S.koy(S.elYazisi({ metin: "now", x: Y.NX - olc(LBF, "now") / 2, y: TY + u(84), boy: LB,
      renk: IKINCIL, tb: tNokta + 0.08, sure: 0.4, ses: false }));
    const fE = S.fr(tEksen) + 2;                     // kapı kutusu: eksen + bant + çentik
    S.koy({ ciz: (ctx, f) => { if (f >= fE) window.__kalemKutu?.ekle("cizim", ad, Y.AX0 - u(4),
      TY - u(30), Y.AX1 - Y.AX0 + u(8), u(60)); } });
  };

  // 189,68 «İstanbul'da»: eksen 1 · 190,00 now · 190,24 «yaşıyorum»: kısa bant (for now)
  zamanCizgisi("zaman-1", Y.T1Y, Y.B1, t0("İstanbul'da", 189.68), 190.0, t0("yaşıyorum", 190.24),
    0.4, 600);

  // 191,55 «Geçici.»: (temporary)
  const wFor = olc(CF, "for now "), wAlw = olc(CF, "always ");
  const nTmp = S.koy(S.elYazisi({ metin: "(temporary)", x: NTX + wFor, y: Y1, boy: LP, renk: MUR,
    tb: t0("Geçici.", 191.55), sure: 0.75 }));

  // 192,48 «Ailenle»: eksen 2 · 192,90 now · 193,12 «hep»: → always · 193,36 «orada yaşıyorsan»: uzun bant
  zamanCizgisi("zaman-2", Y.T2Y, Y.B2, t0("Ailenle", 192.48), 192.9, t0("orada", 193.36), 0.85, 620);
  const tHep = t0("hep", 193.12);
  notOk(Y2, tHep, 241);
  S.koy(S.elYazisi({ metin: "always", x: NTX, y: Y2, boy: LP, renk: MUR, tb: tHep + 0.16, sure: 0.45 }));
  // 193,95 «yaşıyorsan:» (hep orada → kalıcı): (permanent)
  const nPer = S.koy(S.elYazisi({ metin: "(permanent)", x: NTX + wAlw, y: Y2, boy: LP, renk: MUR,
    tb: 193.95, sure: 0.7 }));

  // 194,89–196,65 kart 2 cümlesi sözcük sözcük
  const c2 = S.koy(S.cumleYaz({ sozcukler: b, x: Y.KX + Y.PAD, y: Y2, font: F, satirH: PX * 1.4,
    satirSay: [b.length], bosluk: EK }));

  // 197,70 «yor (eki iki durumu da)»: iki fiil aynı anda sarı altı çizili (am living · live)
  const tYor = t0("yor", 197.7), dY = PX * 0.48;      // g kuyruğuna değmez (QA 1. tur)
  const k1 = c1.kel[1], k2 = c1.kel[2], k3 = c2.kel[1];
  sari(k1.x - u(2), k2.x + k2.w + u(2), k1.y + dY, tYor, 1);
  sari(k3.x - u(2), k3.x + k3.w + u(2), k3.y + dY, tYor + 0.08, 2, false);

  // 201,30 «ayrılır.»: meaning sarı altı çizili (İngilizcede ikisi ayrılır)
  sari(nM.x - u(4), nM.x + nM.w + u(4), Y.MY + MP * 0.34, t0("ayrılır.", 201.3), 3);

  // 202,74 «Kalıcı mı,»: (permanent) · 203,46 «geçici mi?»: (temporary) sarı altı çizili
  sari(nPer.x - u(4), nPer.x + nPer.w + u(4), Y2 + LP * 0.52, t0("Kalıcı", 202.74), 4);
  sari(nTmp.x - u(4), nTmp.x + nTmp.w + u(4), Y1 + LP * 0.52, t0("geçici", 203.46), 5);
}

surucu(kur, (f) => S.kare(f), KARE);

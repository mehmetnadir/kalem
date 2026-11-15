// Sahne 02 (02-04-ydt-temel-s2 Shorts) — Örnek: Paper.js, 1080x1920, 449 kare, t_bas 2.84.
// Soru satırı (Genel mi, şu an mı?), kart 1 (She wears her coat in the winter. / Simple Present / GENERAL),
// kış zaman çizgisi, kart 2 (She is wearing her pink T-shirt today. / Present Continuous / RIGHT NOW),
// MEANING sarı hapı ve today zaman çizgisi.
import { sahneKur, RT, KUNYE, renkCoz } from "/projeler/02-04-ydt-temel-s2/sahneler/02-paperjs-ornek/kalem-paper.js";
import { yaziNoktalari } from "/projeler/02-04-ydt-temel-s2/ortak/kalem-canvas.js";

export const KARE = 449, T_BAS = 2.84;

// Cümle 2 parça 3 (EN "She is wearing her pink T-shirt today.") sozcukler.json'da YOK: el.py T-shirt'ü sese "T shirt"
// gönderir, sözcük sayısı tutmaz. Çapa: ElevenLabs önbellek hizalaması ~/.local/share/elevenlabs-onbellek/
// 3e7a9af33838d05cd9a8083c218a882a935c6edf.hiz.json (T + shirt birleşik) + parça başı 8,37 (sureler.json cümle 2
// parcalar[2][0] 4,98 + cümle başı 3,39). BRIEF-S2 DİKKAT notu ile aynı. Küresel sn.
const EN2 = [
  ["She", 8.37], ["is", 8.61], ["wearing", 8.77], ["her", 9.21],
  ["pink", 9.45], ["T-shirt", 9.65], ["today.", 10.13],
];

// Giysi çizimleri: birim ızgara (mont 100×120, tişört 100×90); n = darbe noktaları, egri = yumuşak.
const MONT = [
  { n: [[40, 4], [20, 10], [6, 70], [17, 74], [26, 34], [23, 116], [50, 117]] },
  { n: [[60, 4], [80, 10], [94, 70], [83, 74], [74, 34], [77, 116], [50, 117]] },
  { n: [[40, 4], [50, 9], [60, 4]], egri: true },
  { n: [[40, 4], [44, 21], [50, 34]], egri: true },
  { n: [[60, 4], [56, 21], [50, 34]], egri: true },
  { n: [[50, 34], [50, 116]] },
  { n: [[28, 96], [38, 95]] }, { n: [[62, 95], [72, 96]] },
  { daire: [44, 48, 2.6] }, { daire: [44, 64, 2.6] }, { daire: [44, 80, 2.6] },
];
const TISORT = [
  { n: [[37, 4], [14, 12], [0, 36], [14, 46], [24, 37], [24, 88], [76, 88], [76, 37], [86, 46],
    [100, 36], [86, 12], [63, 4]] },
  { n: [[37, 4], [50, 14], [63, 4]], egri: true },
  { n: [[14, 12], [24, 37]] }, { n: [[86, 12], [76, 37]] },
];

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: KUNYE.cipler["02-paperjs-ornek"] });
  const {
    fr, not, olay, ciz, ok, kutu, yazi, elYazisi, cumle, altCizgi, dinamik, oge, genislik, kis, cikis,
  } = S;

  // Tegaki Caveat 700 metrik ve glif verisi (el yazısı genişlik ölçümü)
  const [eyM, eyG] = await Promise.all([
    fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json"),
  ]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, {
    upm: EY.M.unitsPerEm, asc: EY.M.ascender, boy: boyut, x: 0, taban: 0,
  }).gen;

  // Sözcük doğrulama bekçisi
  const noktasiz = (s) => s.replace(/[\p{P}\p{S}]/gu, "");
  const al = (dizi, i, beklenen) => {
    const w = dizi && dizi[i];
    if (!w) throw new Error(`al: dizi[${i}] sözcük bulunamadı (beklenen: "${beklenen}")`);
    const sTr = noktasiz(w.s).toLocaleLowerCase("tr");
    const bTr = noktasiz(beklenen).toLocaleLowerCase("tr");
    if (sTr !== bTr && sTr.replace(/ı/g, "i") !== bTr.replace(/ı/g, "i")) {
      throw new Error(`al: dizi[${i}] sözcük uyuşmazlığı: "${w.s}" ("${sTr}") !== "${beklenen}" ("${bTr}")`);
    }
    return w;
  };

  // Zaman çapaları (zaman sözcükten okunur)
  const s2 = S.sozcukler(2);
  const f0 = (f) => Math.max(12, f);

  const wShe = al(s2, 0, "She");
  const wCoat = al(s2, 3, "coat");
  const wIn = al(s2, 4, "in");
  const wWinter = al(s2, 6, "winter.");
  const wGenel = al(s2, 7, "Genel");
  const wDurum = al(s2, 8, "durum:");
  const wGenis = al(s2, 9, "geniş");
  const wZaman1 = al(s2, 10, "zaman.");
  const wToday = al(s2, 11, "Today");
  const wAnlam = al(s2, 17, "anlam");
  const wKonusma = al(s2, 19, "Konuşma");
  const wAni = al(s2, 20, "anı:");
  const wSimdiki = al(s2, 21, "şimdiki");
  const wZaman2 = al(s2, 22, "zaman.");

  // Ölçü ve sabitler (BRIEF-DIKEY §2–§3)
  const W = 1080;
  const KENAR = KUNYE.kenar;
  const SAG = W - KENAR;
  const SOL = KENAR + 24;
  const KX = KENAR;
  const KW = W - 2 * KENAR;
  const IC = KX + 40;
  const F_EN = "700 64px Fredoka";
  const BEN = 64;
  const ARA = 84;
  const ALT = 0.32;
  const BSORU = 80;
  const Y_SORU = 430;
  const KY1 = 478;
  const KH1 = 200;
  const KY2 = 912;
  const KH2 = 210;
  const yb1 = KY1 + 84;
  const yb2 = KY2 + 96;
  // 72 → 64 (QA tur 1 bekçisi): satır B'de Present Continuous (611 px) + RIGHT NOW (72'de 333 px) 28 px çakıştı.
  const BET = 64;
  const F_INCE = "500 64px Lexend";
  const BINCE = 64;
  const Y_ETA = KY1 + KH1 + 78;
  const Y_ETB = KY2 + KH2 + 78;
  const AXY1 = 820;
  const AXY2 = 1252;
  const BNOW = 64;
  const NOW_DY = 66;
  const AX0 = SOL;
  const AX1 = SAG - 24;
  const NX = Math.round(AX0 + 0.45 * (AX1 - AX0));
  const BW = 110;
  const BP = 230;
  const TB = 120;
  const BANT_W = 28;
  const BANT_A = 0.35;
  const IKON = 100;
  const IKX = KX + KW - 32 - IKON;
  const HAP_H = 80;
  const HAP_P = 34;

  // Türetilen konumlar
  const montKutu = [IKX, KY1 + KH1 - 14 - IKON, IKON, IKON];
  const tisortKutu = [IKX, KY2 + KH2 - 14 - IKON, IKON, IKON];

  const kisBantlari = [-3, -2, -1, 0, 1, 2]
    .map((k) => NX + BP * (k + 0.5))
    .filter((c) => c - BW / 2 >= AX0 + 8 && c + BW / 2 <= AX1 - 40);

  const xGeneral = SAG - 12 - eyGen("GENERAL", BET);
  const xRightNow = SAG - 12 - eyGen("RIGHT NOW", BET);

  const HAP_W = genislik("MEANING", F_EN) + 2 * HAP_P;
  const hx0 = SAG - 24 - HAP_W;
  const hcx = hx0 + HAP_W / 2;

  // Yardımcı işlevler
  const yalin = (z) => z.x0 + genislik(z.str.replace(/[.,:]$/, ""), F_EN);
  const kapat = (fk) => (f) => 1 - kis((f - fk) / 8);

  function elCizim(darbeler, [bx, by, bw, bh], [UW, UH], o) {
    const k = Math.min(bw / UW, bh / UH), ox = bx + (bw - UW * k) / 2, oy = by + (bh - UH * k) / 2;
    const yer = (q) => [ox + q[0] * k, oy + q[1] * k];
    const uz = darbeler.map((d) => (d.daire ? 2 * Math.PI * d.daire[2] : d.n.slice(1)
      .reduce((s, q, i) => s + Math.hypot(q[0] - d.n[i][0], q[1] - d.n[i][1]), 0)) * k);
    const ag = uz.map((l) => 4 + Math.pow(l, 0.75)), top = ag.reduce((s, a) => s + a, 0);
    let cur = o.bas;
    darbeler.forEach((d, i) => {
      const sr = Math.max(3, o.sure * ag[i] / top), ses = i % 3 === 0 ? undefined : false;
      if (d.daire) {
        const [dcx, dcy] = yer(d.daire), r = d.daire[2] * k;
        const pts = Array.from({ length: 19 }, (_, j) => {
          const a = -2.3 + j * 2.2 * Math.PI / 18;
          return [dcx + Math.cos(a) * r, dcy + Math.sin(a) * r];
        });
        ciz(pts, {
          duz: true, bas: cur, sure: Math.max(5, sr * 1.4), w: o.w * 0.9, renk: RT.murekkep,
          alfa: 0.92, amp: 0.3, uc0: 2, uc1: 3, tur: "cizim", ad: o.ad, ses: false,
        });
      } else {
        ciz(d.n.map(yer), {
          duz: !d.egri, w: o.w, amp: 0.8, alfa: 0.92, bas: cur, sure: sr * 1.4,
          uc0: 8, uc1: 16, ses, tur: "cizim", ad: o.ad,
        });
      }
      cur += sr;
    });
    return cur;
  }

  function kar(ccx, ccy, r, bas) {
    const acilar = [-Math.PI / 2, -Math.PI / 6, Math.PI / 6];
    acilar.forEach((a, j) => {
      const dx = r * Math.cos(a), dy = r * Math.sin(a);
      ciz([[ccx - dx, ccy - dy], [ccx + dx, ccy + dy]], {
        duz: true, w: 3, renk: RT.murekkep, alfa: 0.9, uc0: 2, uc1: 2,
        amp: 0.2, bas: bas + 2 * j, sure: 4, ses: false, tur: "isaret", ad: "kar",
      });
    });
  }

  function nokta(ccx, ccy, bas) {
    olay(bas, "tik", 0.45);
    return dinamik((f, g) => {
      if (f < bas) return;
      const k = cikis(kis((f - bas) / 6));
      const cr = new S.P.Path.Circle({
        center: [ccx, ccy],
        radius: Math.max(0.5, 11 * k),
        fillColor: renkCoz(RT.murekkep),
        opacity: 0.95,
        insert: false,
      });
      g.addChild(cr);
    });
  }

  function nabiz(ccx, ccy, bas) {
    return dinamik((f, g) => {
      if (f < bas) return;
      const ph = ((f - bas) % 24) / 24;
      const cr = new S.P.Path.Circle({
        center: [ccx, ccy],
        radius: 12 + 12 * cikis(ph),
        strokeColor: renkCoz(RT.murekkep),
        strokeWidth: 3,
        opacity: 0.6 * (1 - ph),
        insert: false,
      });
      g.addChild(cr);
    });
  }

  // Kart sözcükleri (konum okuma ve karaoke hazırlığı)
  const kel1 = cumle(
    s2.slice(0, 7).map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 })),
    { x: IC, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, aralik: ARA }
  );
  altCizgi(kel1, { tut: 0, alt: ALT });

  const kel2 = cumle(
    EN2.map(([s, t], i) => ({ s, f: fr(t), satir: i < 4 ? 0 : 1 })),
    { x: IC, y: yb2, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, aralik: ARA }
  );
  altCizgi(kel2, { tut: 12, alt: ALT });

  // today halkası: süper elips (n = 6) kutusu, sözcüğe yakın oturur (QA tur 2: elips T-shirt'ün t'sini kesti).
  // Sol kenar sözcük arası boşlukta (x0 − 11), sağ kenar noktayı içine alır, alt kenar y kuyruğunun altında.
  const zToday = kel2[6];
  const x1yToday = yalin(zToday);
  const HL = zToday.x0 - 11, HR = x1yToday + 22, HT = zToday.y - BEN * 0.8, HB = zToday.y + BEN * 0.36;
  const halkaNoktalari = () => Array.from({ length: 73 }, (_, i) => {
    const t = -2.3 + (i / 72) * 1.08 * 2 * Math.PI, us = (v) => Math.sign(v) * Math.pow(Math.abs(v), 1 / 3);
    return [(HL + HR) / 2 + (HR - HL) / 2 * us(Math.cos(t)), (HT + HB) / 2 + (HB - HT) / 2 * us(Math.sin(t))];
  });

  // Bekçiler (sessiz geçiş yok, throw new Error(...))
  const sagKart1_0 = kel1[3].x1;
  const sagKart1_1 = kel1[6].x1;
  if (sagKart1_0 > SAG - 40) {
    throw new Error(`Bekçi: Kart 1 satır 1 sağ ucu sınırı aştı (${sagKart1_0} > ${SAG - 40})`);
  }
  if (sagKart1_1 > IKX - 16) {
    throw new Error(`Bekçi: Kart 1 satır 2 sağ ucu giysi payını aştı (${sagKart1_1} > ${IKX - 16})`);
  }
  const sagKart2_0 = kel2[3].x1;
  const sagKart2_1 = kel2[6].x1;
  if (sagKart2_0 > SAG - 40) {
    throw new Error(`Bekçi: Kart 2 satır 1 sağ ucu sınırı aştı (${sagKart2_0} > ${SAG - 40})`);
  }
  if (sagKart2_1 > IKX - 16) {
    throw new Error(`Bekçi: Kart 2 satır 2 sağ ucu giysi payını aştı (${sagKart2_1} > ${IKX - 16})`);
  }
  if (HR > IKX - 12) {
    throw new Error(`Bekçi: today halkası giysi payını aştı (${HR} > ${IKX - 12})`);
  }

  const sagSimplePresent = SOL + genislik("Simple Present", F_INCE);
  if (sagSimplePresent + 32 > xGeneral) {
    throw new Error(`Bekçi: Simple Present ile GENERAL çakışıyor (${sagSimplePresent + 32} > ${xGeneral})`);
  }

  const sagPresentContinuous = SOL + genislik("Present Continuous", F_INCE);
  if (sagPresentContinuous + 32 > xRightNow) {
    throw new Error(`Bekçi: Present Continuous ile RIGHT NOW çakışıyor (${sagPresentContinuous + 32} > ${xRightNow})`);
  }

  const hapAlt = KY2 + HAP_H / 2;
  const k2s1Ust = yb2 - BEN * 0.72;
  const hapKesisiyor = !(hx0 + HAP_W < kel2[0].x0 || hx0 > sagKart2_0);
  if (hapAlt > k2s1Ust && hapKesisiyor) {
    throw new Error(`Bekçi: Hap kart 2 satır 1 ile çakışıyor (alt: ${hapAlt} > ${k2s1Ust})`);
  }

  if (kisBantlari.length < 3) {
    throw new Error(`Bekçi: Kış bandı sayısı < 3 (${kisBantlari.length})`);
  }
  const nxBantta = kisBantlari.some((c) => NX >= c - BW / 2 && NX <= c + BW / 2);
  if (nxBantta) {
    throw new Error(`Bekçi: NX noktası bir kış bandının içinde (${NX})`);
  }
  if (NX - TB < AX0 || NX + TB > AX1) {
    throw new Error(`Bekçi: today bandı eksen sınırlarını aştı ([${NX - TB}, ${NX + TB}] dışta [${AX0}, ${AX1}])`);
  }

  if (AXY2 + NOW_DY + 4 > KUNYE.icerikSon) {
    throw new Error(`Bekçi: Zaman çizgisi 2 alt sınırı aştı (${AXY2 + NOW_DY + 4} > ${KUNYE.icerikSon})`);
  }
  const sagSoru = SOL + genislik("Genel mi, şu an mı?", `700 ${BSORU}px Caveat`);
  if (sagSoru > SAG) {
    throw new Error(`Bekçi: Soru satırı sağ sınırı aştı (${sagSoru} > ${SAG})`);
  }

  // --- 0,00 hazır: Soru satırı hazır
  yazi("Genel mi, şu an mı?", {
    x: SOL, y: Y_SORU, boyut: BSORU, aile: "Caveat", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false,
  });
  not("soru satırı (hazır)", 0);

  // --- 3,06 She - 10 (geçiş payı: kare 12'ye çekilir): Kart 1 kutusu
  const fKutu1 = f0(fr(wShe.t) - 10);
  kutu(KX, KY1, KW, KH1, { bas: fKutu1, sure: 10, w: 4, renk: RT.ikincil, ad: "kart 1" });
  not("kart 1 kutusu (She)", fKutu1);

  // --- 3,39 She: Kart 1 sözcükleri + karaoke
  not("kart 1 sözcükleri (She)", kel1[0].bas);
  not("kart 1 karaoke (She)", kel1[0].bas);

  // --- 4,27 coat: Mont kalemle (sağ alt köşe)
  elCizim(MONT, montKutu, [100, 120], { bas: fr(wCoat.t), sure: 30, w: 4, ad: "mont" });
  not("mont (coat)", fr(wCoat.t));

  // --- 4,47 in: odak in the winter (sarı)
  const odak1 = oge({ alfa: kapat(fr(EN2[0][1])) });
  const yU1 = kel1[4].y + BEN * ALT;
  ciz([[kel1[4].x0 - 4, yU1], [yalin(kel1[6]) + 4, yU1 - 2]], {
    duz: true, w: 9, renk: RT.vurguDolgu, alfa: 0.9, uc0: 6, uc1: 8, amp: 0.8,
    bas: fr(wIn.t), sure: 12, tur: "isaret", ses: "tik", ad: "odak in the winter", oge: odak1,
  });
  not("odak in the winter (in)", fr(wIn.t));

  // --- 5,56 Genel: GENERAL
  elYazisi("GENERAL", {
    x: xGeneral, y: Y_ETA, boyut: BET, renk: RT.murekkep,
    sozcukler: [{ f0: fr(wGenel.t), f1: fr(wDurum.t) }],
  });
  not("GENERAL (Genel)", fr(wGenel.t));

  // --- 6,04 durum:: Zaman çizgisi 1 (eksen + ok ucu)
  ciz([[AX0, AXY1], [AX1, AXY1]], {
    duz: true, w: 4.5, renk: RT.ikincil, uc0: 8, uc1: 6, bas: fr(wDurum.t), sure: 12, ad: "zaman-1",
  });
  [1, -1].forEach((s) => {
    ciz([[AX1 - 26, AXY1 - s * 16], [AX1, AXY1]], {
      duz: true, w: 4.5, renk: RT.ikincil, uc0: 4, uc1: 4, bas: fr(wDurum.t) + 11,
      sure: 4, ses: false, ad: "zaman-1",
    });
  });
  not("zaman-1 eksen (durum:)", fr(wDurum.t));
  not("zaman-1 ok (durum:)", fr(wDurum.t) + 11);

  // --- 6,31 durum: + 8: now noktası 1 + now
  nokta(NX, AXY1, fr(wDurum.t) + 8);
  elYazisi("now", {
    x: NX - eyGen("now", BNOW) / 2, y: AXY1 + NOW_DY, boyut: BNOW,
    renk: RT.murekkep, bas: fr(wDurum.t) + 12, sure: 12, ses: false,
  });
  not("now 1 nokta (durum:)", fr(wDurum.t) + 8);
  not("now 1 metin (durum:)", fr(wDurum.t) + 12);

  // --- 6,68 geniş: Simple Present (ince yazı)
  yazi("Simple Present", {
    x: SOL, y: Y_ETA, boyut: BINCE, aile: "Lexend", agirlik: 500,
    renk: RT.murekkep, bas: fr(wGenis.t), sure: 12, ses: "tik",
  });
  not("Simple Present (geniş)", fr(wGenis.t));

  // --- 7,00 zaman.: Kış bantları + kar taneleri
  kisBantlari.forEach((c, i) => {
    ciz([[c - BW / 2, AXY1], [c + BW / 2, AXY1]], {
      duz: true, w: BANT_W, renk: RT.ikincil, alfa: BANT_A, uc0: 4, uc1: 4, amp: 0.6,
      bas: fr(wZaman1.t) + 4 * i, sure: 8, tur: "isaret", ses: i ? false : undefined, ad: "kış bandı",
    });
    kar(c, AXY1, 11, fr(wZaman1.t) + 4 * i + 6);
    not(`kış bandı ${i + 1} (zaman.)`, fr(wZaman1.t) + 4 * i);
    not(`kar tanesi ${i + 1} (zaman.)`, fr(wZaman1.t) + 4 * i + 6);
  });

  // --- 8,37 She: odak 1 kapanır
  not("odak 1 kapanır (She)", fr(EN2[0][1]));

  // --- 8,04 She - 10: Kart 2 kutusu
  const fKutu2 = fr(EN2[0][1]) - 10;
  kutu(KX, KY2, KW, KH2, { bas: fKutu2, sure: 14, w: 4, renk: RT.ikincil, ad: "kart 2" });
  not("kart 2 kutusu (She)", fKutu2);

  // --- 8,37 She: Kart 2 sözcükleri + karaoke
  not("kart 2 sözcükleri (She)", kel2[0].bas);
  not("kart 2 karaoke (She)", kel2[0].bas);

  // --- 9,65 T-shirt: Tişört kalemle (sağ alt köşe)
  elCizim(TISORT, tisortKutu, [100, 90], { bas: fr(EN2[5][1]), sure: 30, w: 4, ad: "tisort" });
  not("tisort (T-shirt)", fr(EN2[5][1]));

  // --- 10,13 today.: odak today (sarı)
  const odak2 = oge({ alfa: kapat(fr(wToday.t)) });
  const yU2 = kel2[6].y + BEN * ALT;
  ciz([[kel2[6].x0 - 4, yU2], [yalin(kel2[6]) + 4, yU2 - 2]], {
    duz: true, w: 9, renk: RT.vurguDolgu, alfa: 0.9, uc0: 6, uc1: 8, amp: 0.8,
    bas: fr(EN2[6][1]), sure: 10, tur: "isaret", ses: "tik", ad: "odak today", oge: odak2,
  });
  not("odak today (today.)", fr(EN2[6][1]));

  // --- 11,42 Today: today sarı daire (işaret)
  const FM = fr(wAnlam.t);
  const sariOge = oge({ alfa: (f) => 1 - kis((f - FM) / 8) });
  const murOge = oge({ alfa: (f) => kis((f - FM) / 8) });
  // Aynı noktalar + aynı tohum = aynı kalem biçimi (daire() ile aynı kalem ayarı)
  const halka = { duz: true, w: 7.5, alfa: 0.85, amp: 0.4, uc0: 14, uc1: 40, tohum: 4242, tur: "isaret",
    bas: fr(wToday.t), sure: 14 };
  ciz(halkaNoktalari(), { ...halka, renk: RT.vurgu, ses: "tik", ad: "today daire", oge: sariOge });
  ciz(halkaNoktalari(), { ...halka, renk: RT.murekkep, ses: false, ad: "today daire mürekkep", oge: murOge });
  not("today daire (Today)", fr(wToday.t));
  not("today daire mürekkep (Today)", fr(wToday.t));

  // --- 14,14 anlam: MEANING sarı hapı + soru altçizgi + daire mürekkebe döner
  dinamik((f, g) => {
    if (f < FM) return;
    const u = kis((f - FM) / 8);
    const s = 0.7 + 0.3 * cikis(u);
    const rw = HAP_W * s, rh = HAP_H * s;
    const rect = new S.P.Path.Rectangle({
      rectangle: new S.P.Rectangle(hcx - rw / 2, KY2 - rh / 2, rw, rh),
      radius: rh / 2,
      fillColor: renkCoz(RT.vurguDolgu),
      opacity: cikis(u),
      insert: false,
    });
    g.addChild(rect);
  });
  olay(FM, "parilti", 0.5);
  yazi("MEANING", {
    x: hcx, y: KY2 + 22, hizala: "orta", boyut: BEN, aile: "Fredoka", agirlik: 700,
    renk: RT.pilMetin, bas: FM + 3, sure: 6, ses: false,
  });
  not("MEANING hapı (anlam)", FM);

  const sagSoruStr = SOL + genislik("Genel mi, şu an mı?", `700 ${BSORU}px Caveat`);
  ciz([[SOL - 4, Y_SORU + 24], [sagSoruStr + 4, Y_SORU + 22]], {
    duz: true, w: 6, renk: RT.murekkep, alfa: 0.9, uc0: 6, uc1: 10, amp: 0.8,
    bas: FM + 2, sure: 12, tur: "isaret", ses: false, ad: "soru altçizgi",
  });
  not("soru altçizgi (anlam)", FM + 2);

  // --- 15,25 Konuşma: RIGHT NOW
  const RN = elYazisi("RIGHT NOW", {
    x: xRightNow, y: Y_ETB, boyut: BET, renk: RT.murekkep,
    sozcukler: [
      { f0: fr(wKonusma.t), f1: fr(wKonusma.t1) },
      { f0: fr(wKonusma.t1), f1: fr(wAni.t) + 6 },
    ],
  });
  not("RIGHT NOW (Konuşma)", fr(wKonusma.t));

  // --- 15,38 Konuşma + 4: Zaman çizgisi 2 (eksen + ok ucu)
  ciz([[AX0, AXY2], [AX1, AXY2]], {
    duz: true, w: 4.5, renk: RT.ikincil, uc0: 8, uc1: 6, bas: fr(wKonusma.t) + 4,
    sure: 10, ad: "zaman-2",
  });
  [1, -1].forEach((s) => {
    ciz([[AX1 - 26, AXY2 - s * 16], [AX1, AXY2]], {
      duz: true, w: 4.5, renk: RT.ikincil, uc0: 4, uc1: 4, bas: fr(wKonusma.t) + 13,
      sure: 4, ses: false, ad: "zaman-2",
    });
  });
  not("zaman-2 eksen (Konuşma)", fr(wKonusma.t) + 4);
  not("zaman-2 ok (Konuşma)", fr(wKonusma.t) + 13);

  // --- 15,73 Konuşma.t1: today dairesi -> RIGHT NOW ince oku
  // QA tur 2: ok başı RIGHT'ın I'sına düşüyordu (RÎGHT). Ok halkanın sağından çıkar, yukarı bombe yapar,
  // RIGHT NOW'un üst ortasına yukarıdan iner (uç yazı üstünden ≈ 12 px yukarıda).
  ok([HR + 2, (HT + HB) / 2], [RN.x0 + RN.w * 0.45, Y_ETB - BET * 0.84], {
    bas: fr(wKonusma.t1), sure: 10, w: 4.5, renk: RT.murekkep, alfa: 0.9,
    uzun: 16, bukum: 0.25, yon: [0.3, -1], ad: "bag today",
  });
  not("bag today (Konuşma)", fr(wKonusma.t1));

  // --- 15,81 anı:: now noktası 2 + nabız + now
  nabiz(NX, AXY2, fr(wAni.t) + 3);
  nokta(NX, AXY2, fr(wAni.t));
  elYazisi("now", {
    x: NX - eyGen("now", BNOW) / 2, y: AXY2 + NOW_DY, boyut: BNOW,
    renk: RT.murekkep, bas: fr(wAni.t) + 6, sure: 10, ses: false,
  });
  not("nabiz (anı:)", fr(wAni.t) + 3);
  not("now 2 nokta (anı:)", fr(wAni.t));
  not("now 2 metin (anı:)", fr(wAni.t) + 6);

  // --- 16,49 şimdiki: Present Continuous (ince yazı)
  yazi("Present Continuous", {
    x: SOL, y: Y_ETB, boyut: BINCE, aile: "Lexend", agirlik: 500,
    renk: RT.murekkep, bas: fr(wSimdiki.t), sure: 12, ses: "tik",
  });
  not("Present Continuous (şimdiki)", fr(wSimdiki.t));

  // --- 16,62 şimdiki + 4: today bandı + iki uç çentiği
  ciz([[NX - TB, AXY2], [NX + TB, AXY2]], {
    duz: true, w: BANT_W, renk: RT.ikincil, alfa: BANT_A, uc0: 4, uc1: 4, amp: 0.6,
    bas: fr(wSimdiki.t) + 4, sure: 8, tur: "isaret", ad: "today bandı",
  });
  [NX - TB, NX + TB].forEach((x, i) => {
    ciz([[x, AXY2 - 26], [x, AXY2 + 26]], {
      duz: true, w: 4.5, renk: RT.murekkep, alfa: 0.9, uc0: 3, uc1: 3, amp: 0.3,
      bas: fr(wSimdiki.t) + 8 + 3 * i, sure: 5, ses: false, tur: "isaret", ad: "today çentik",
    });
    not(`today çentik ${i + 1} (şimdiki)`, fr(wSimdiki.t) + 8 + 3 * i);
  });
  not("today bandı (şimdiki)", fr(wSimdiki.t) + 4);

  return S;
}

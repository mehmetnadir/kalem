// Sahne 02 (simple-present-temel-s3 Shorts) — Değer: Paper.js, 1080x1920, 281 kare, t_bas 3.89.
// Kart 0 (He doesn't goes.) -> sarı daire (does), ek oku (es->does), üstü çizili es ve carpi -> kart 1-2.
// huni v2 (15.11): yerleşim x 60–960, y 460–1380; çip yok; kanal katmanı kunye.js'te.
import { sahneKur, RT, KUNYE } from "/projeler/simple-present-temel-s3/sahneler/02-paperjs-deger/kalem-paper.js";

export const KARE = 281, T_BAS = 3.89;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS });
  const {
    fr, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, oge, not, genislik, kis,
  } = S;

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

  // Zaman ve sözcükler
  const s2 = S.sozcukler(2);

  const wDoes = al(s2, 3, "does");
  const wS1 = al(s2, 5, "s");
  const wOna = al(s2, 6, "ona");
  const wS2 = al(s2, 9, "s");
  const wGelmez = al(s2, 10, "gelmez.");
  const wHe = al(s2, 11, "He");
  const wDoesnt = al(s2, 12, "doesn't");
  const wGo1 = al(s2, 13, "go.");
  const wDoes2 = al(s2, 14, "Does");
  const wShe = al(s2, 15, "she");
  const wGo2 = al(s2, 16, "go?");

  const F_HE = fr(wHe.t);
  const F_S2 = fr(wS2.t);
  const F_GEL = fr(wGelmez.t);
  const sonma = (f0, n) => (f) => 1 - kis((f - f0) / n);

  // Ölçü ve sabitler (huni v2 §B)
  const KENAR = KUNYE.kenar;
  const SAG = KUNYE.sag;
  const KUTU_PAY = 10;
  const KX = KENAR + KUTU_PAY;
  const KW = 680;
  const IC = KX + 40;
  const KY0 = KUNYE.icerikBas + 20 + KUTU_PAY;
  const KH0 = 140;
  const Y0 = 582;
  const B0 = 80;
  const KY1 = KY0;
  const KH = 200;
  const KY2 = KY1 + 280;
  const Y1 = KY1 + 76;
  const Y2 = KY2 + 76;
  const T1 = KY1 + 154;
  const T2 = KY2 + 154;
  const B1 = 72;
  const BTR = 52;
  const ALT = 0.30;
  const XX = KX + KW + 40;
  const XS = 64;

  // Kart 0 parça konumları
  const F80 = "700 80px Fredoka";
  const g = (s) => genislik(s, F80);
  const xHe = IC;
  const xDo = xHe + g("He") + g(" ");
  const xEs1 = xDo + g("do");
  const xNt = xEs1 + g("es");
  const xGo = xNt + g("n't") + g(" ");
  const xEs2 = xGo + g("go");
  const xNokta = xEs2 + g("es");
  const gEs = g("es");

  // Türetilen geometriler
  // Şef kare turu 1: dikey yarıçap 50 → 70, merkez 2 px sola / 2 px aşağı (halka `s`'nin alt sağını kesiyordu).
  const DCX = (xDo + xNt) / 2 - 4;
  const DCY = Y0 - 26;
  const DRX = (xNt - xDo) / 2 + 8;
  const DRY = 70;
  const OA = [xEs2 + gEs / 2, Y0 - 50];
  const OB = [xEs1 + gEs / 2, Y0 - 50];
  const OBUK = 0.2;
  const BY = Y0 - B0 * 0.22;

  // Bekçiler
  if (xNokta + g(".") > KX + KW - 20) {
    throw new Error(`Bekçi: kart 0 yazısı kutuya sığmadı (${xNokta + g(".")} > ${KX + KW - 20})`);
  }
  const F72 = "700 72px Fredoka";
  if (IC + genislik("He doesn't go.", F72) > KX + KW - 20) {
    throw new Error(`Bekçi: kart 1 EN yazısı kutuya sığmadı`);
  }
  if (IC + genislik("Does she go?", F72) > KX + KW - 20) {
    throw new Error(`Bekçi: kart 2 EN yazısı kutuya sığmadı`);
  }
  if (XX + XS > SAG) {
    throw new Error(`Bekçi: ✗ sağ sınırı aştı (${XX + XS} > ${SAG})`);
  }
  if (KY0 - 10 < KUNYE.icerikBas) {
    throw new Error(`Bekçi: kart 0 üst kenarı içerik sınırını aştı (${KY0 - 10} < ${KUNYE.icerikBas})`);
  }
  if (KY2 + KH + 10 > KUNYE.icerikSon) {
    throw new Error(`Bekçi: kart 2 alt kenarı içerik sınırını aştı (${KY2 + KH + 10} > ${KUNYE.icerikSon})`);
  }
  const okTepe = OA[1] - OBUK * (OA[0] - OB[0]);
  if (okTepe < KUNYE.icerikBas) {
    throw new Error(`Bekçi: ok tepesi içerik sınırını aştı (${okTepe} < ${KUNYE.icerikBas})`);
  }
  if (DRX < (xNt - xDo) / 2) {
    throw new Error(`Bekçi: daire does'u kapsamadı (${DRX} < ${(xNt - xDo) / 2})`);
  }
  if (Y1 + B1 * 0.3 > T1 - BTR * 0.9) {
    throw new Error(`Bekçi: kart 1 EN ve TR çakışması (${Y1 + B1 * 0.3} > ${T1 - BTR * 0.9})`);
  }

  // Katman öğeleri (Paper'da sonra kurulan üstte; yazılardan ÖNCE kurulur)
  const BANT1 = oge({ alfa: sonma(F_S2, 6) });
  const SARI = oge({ alfa: sonma(F_GEL, 6) });
  const ESKI = oge({ alfa: sonma(F_HE, 4) });
  const DUSEN = oge({
    kay: { f0: F_HE, f1: F_HE + 10, dx: 0, dy: 120 },   // şef kare turu 1: 70 → 120 (5 karelik sönüşte düşüş görünsün)
    alfa: sonma(F_HE, 5),
  });
  const OK1 = oge({ alfa: sonma(F_S2, 6) });
  const CARPI = oge({ alfa: sonma(F_HE, 4) });

  // 1. Kart 0 kutusu hazır
  kutu(KX, KY0, KW, KH0, {
    bas: -40,
    sure: 14,
    w: 4,
    renk: RT.ikincil,
    oge: ESKI,
    ad: "kart 0 kutusu",
  });
  not("kart 0 kutusu", 0);

  // 2. Kart 0 yazısı hazır
  yazi("He", {
    x: xHe, y: Y0, boyut: B0, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: ESKI,
  });
  yazi("do", {
    x: xDo, y: Y0, boyut: B0, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: ESKI,
  });
  yazi("es", {
    x: xEs1, y: Y0, boyut: B0, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: ESKI,
  });
  yazi("n't", {
    x: xNt, y: Y0, boyut: B0, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: ESKI,
  });
  yazi("go", {
    x: xGo, y: Y0, boyut: B0, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: ESKI,
  });
  yazi("es", {
    x: xEs2, y: Y0, boyut: B0, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: DUSEN,
  });
  yazi(".", {
    x: xNokta, y: Y0, boyut: B0, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: ESKI,
  });
  not("kart 0 yazısı", 0);

  // 3. does sarı dairesi
  daire(DCX, DCY, DRX, DRY, {
    bas: fr(wDoes.t),
    sure: 12,
    oge: SARI,
    ad: "does dairesi",
  });
  not("does dairesi (does)", fr(wDoes.t));

  // 4. es (goes) arkası bant
  ciz([[xEs2 - 5, BY], [xEs2 + gEs + 6, BY]], {
    duz: true,
    w: B0 * 0.70,
    renk: RT.vurguDolgu,
    alfa: 0.6,
    uc0: 5,
    uc1: 9,
    amp: 1.0,
    bas: fr(wS1.t),
    sure: 8,
    tur: "isaret",
    ses: "tik",
    oge: BANT1,
    ad: "es bandı goes",
  });
  not("es bandı goes (s)", fr(wS1.t));

  // 5. Kavisli ok es -> does
  ok(OA, OB, {
    bas: fr(wS1.t),
    sure: 12,
    w: 6,
    uzun: 18,
    bukum: OBUK,
    yon: [0, -1],
    oge: OK1,
    ad: "es oku",
  });
  not("es oku (s)", fr(wS1.t));

  // 6. es (does) arkası bant
  ciz([[xEs1 - 5, BY], [xEs1 + gEs + 6, BY]], {
    duz: true,
    w: B0 * 0.70,
    renk: RT.vurguDolgu,
    alfa: 0.6,
    uc0: 5,
    uc1: 9,
    amp: 1.0,
    bas: fr(wOna.t),
    sure: 8,
    tur: "isaret",
    ses: "tik",
    oge: SARI,
    ad: "es bandı does",
  });
  not("es bandı does (ona)", fr(wOna.t));

  // 7. Kırmızı üstü çizgi es (goes)
  ciz([[xEs2 - 4, Y0 - 18], [xEs2 + gEs + 4, Y0 - 26]], {
    duz: true,
    w: 7,
    renk: RT.kirmizi,
    alfa: 0.95,
    uc0: 4,
    uc1: 6,
    amp: 0.5,
    bas: F_S2,
    sure: 8,
    tur: "isaret",
    oge: DUSEN,
    ad: "üstü çizili es",
  });
  not("üstü çizili es (s)", F_S2);

  // 8. Ok + bant 1 söner
  not("ok ve bant söner (s)", F_S2);

  // 9. Kırmızı ✗
  ciz([[XX, Y0 - 56], [XX + XS, Y0 + 8]], {
    duz: true,
    w: 8,
    renk: RT.kirmizi,
    alfa: 0.95,
    uc0: 5,
    uc1: 8,
    amp: 0.4,
    bas: F_GEL,
    sure: 7,
    tur: "isaret",
    oge: CARPI,
    ad: "carpi",
  });
  ciz([[XX + XS, Y0 - 56], [XX, Y0 + 8]], {
    duz: true,
    w: 8,
    renk: RT.kirmizi,
    alfa: 0.95,
    uc0: 5,
    uc1: 8,
    amp: 0.4,
    bas: F_GEL + 5,
    sure: 7,
    tur: "isaret",
    oge: CARPI,
    ad: "carpi",
    ses: false,
  });
  not("carpi (gelmez.)", F_GEL);

  // 10. does dairesi mürekkebe döner
  daire(DCX, DCY, DRX, DRY, {
    renk: RT.murekkep,
    bas: F_GEL,
    sure: 6,
    ses: false,
    oge: ESKI,
    ad: "does dairesi mürekkep",
  });
  not("does dairesi mürekkep (gelmez.)", F_GEL);

  // 11. es düşer ve solar; ✗ silinir; kart 0 söner
  not("kart 0 söner ve es düşer (He)", F_HE);

  // 12. Kart 1 kutusu
  kutu(KX, KY1, KW, KH, {
    bas: F_HE,
    sure: 12,
    w: 4,
    renk: RT.ikincil,
    ad: "kart 1 kutusu",
  });
  not("kart 1 kutusu (He)", F_HE);

  // 13. Kart 1 EN He doesn't go.
  const kel1 = cumle([
    { s: "He", f: F_HE + 4 },
    { s: "doesn't", f: fr(wDoesnt.t) },
    { s: "go", f: fr(wGo1.t) },
  ], {
    x: IC,
    y: Y1,
    boyut: B1,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
  });
  yazi(".", {
    x: kel1[2].x1,
    y: Y1,
    boyut: B1,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: fr(wGo1.t),
    sure: 4,
  });
  not("kart 1 EN (He)", F_HE + 4);

  // 14. Soluk TR O gitmez.
  elYazisi("O gitmez.", {
    x: IC,
    y: T1,
    boyut: BTR,
    renk: RT.ikincil,
    bas: fr(wGo1.t) + 8,
    sure: 14,
  });
  not("kart 1 TR (go. + 8)", fr(wGo1.t) + 8);

  // 15. Kart 2 kutusu
  kutu(KX, KY2, KW, KH, {
    bas: fr(wDoes2.t) - 8,
    sure: 12,
    w: 4,
    renk: RT.ikincil,
    ad: "kart 2 kutusu",
  });
  not("kart 2 kutusu (Does - 8)", fr(wDoes2.t) - 8);

  // 16. Kart 2 EN Does she go?
  const kel2 = cumle([
    { s: "Does", f: fr(wDoes2.t) },
    { s: "she", f: fr(wShe.t) },
    { s: "go", f: fr(wGo2.t) },
  ], {
    x: IC,
    y: Y2,
    boyut: B1,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
  });
  yazi("?", {
    x: kel2[2].x1,
    y: Y2,
    boyut: B1,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: fr(wGo2.t),
    sure: 4,
  });
  not("kart 2 EN (Does)", fr(wDoes2.t));

  // 17. Soluk TR O gider mi? (şef kare turu 1: go? 254'te başlayınca donma karesine (268) yetişmiyordu → she 249)
  elYazisi("O gider mi?", {
    x: IC,
    y: T2,
    boyut: BTR,
    renk: RT.ikincil,
    bas: fr(wShe.t),
    sure: 10,
  });
  not("kart 2 TR (she)", fr(wShe.t));

  // 18. Kart karaoke
  altCizgi([...kel1, ...kel2], { tut: 40, alt: ALT });
  not("kart karaoke", kel1[0].bas);

  return S;
}

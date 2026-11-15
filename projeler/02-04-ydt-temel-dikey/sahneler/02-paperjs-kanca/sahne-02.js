// Sahne 02 — Kanca (Paper.js, 1080×1920 dikey, 529 kare, t_bas 3,00). 02-04 YDT temel.
// Yerel kare = round((t − 3,00) × 30). Sözcük zamanları sozcukler.json'dan al() ile doğrulanır.
import { sahneKur, RT, KUNYE } from "/projeler/02-04-ydt-temel-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 529, T_BAS = 3.0;

export async function kur(P) {
  let FL0 = Infinity, FL1 = Infinity;
  const kis = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const S = await sahneKur(P, {
    KARE,
    tBas: T_BAS,
    bolum: KUNYE.cipler["02-paperjs-kanca"],
    etkin: 0,
    // ders adı künye yerinde belirir (FL0 → FL1): opaklık 0 → 1, 16 px aşağıdan yerine; sonra rozet açılır
    hud: (f) => {
      const q = S.yumus((f - FL0) / (FL1 - FL0));
      return { ders: f >= FL0, dersAlfa: q, dersDy: 16 * (1 - q), rozet: kis((f - FL1) / 9) };
    },
  });

  const { fr, ok, kutu, yazi, cumle, altCizgi, ciz, olay, not, lerp, yumus, genislik } = S;
  const F = (b) => "700 " + b + "px Fredoka";
  const MUR = RT.murekkep, SARI = RT.vurgu, DOLGU = RT.vurguDolgu, PIL = RT.pilMetin;
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const f0 = (t) => Math.max(12, fr(t));

  // Sözcük doğrulama
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

  const cumleGenislik = (kelimeler, fontStr) =>
    kelimeler.reduce((top, k) => top + genislik(k.s, fontStr), 0) +
    (kelimeler.length - 1) * genislik(" ", fontStr);

  // Sözcükler ve kritik zamanlar
  const wYasiyorum1 = al(s1, 3, "yaşıyorum");
  const wIkisi = al(s1, 5, "ikisi");
  const wDe = al(s1, 6, "de");
  const wYasiyorumSon = al(s1, 7, "yaşıyorum");

  const CF0 = fr(wYasiyorumSon.t1 + 0.06); // 105: şeride toplanma başı
  const CF1 = CF0 + 12;                   // 117: şeride toplanma sonu

  const wI1 = al(s2, 0, "I");
  const wLive = al(s2, 1, "live");
  const wIn = al(s2, 2, "in");
  const wIstanbul = al(s2, 3, "Istanbul");
  const wBiri = al(s2, 4, "Biri");
  const wGenis = al(s2, 5, "geniş");
  const wZaman1 = al(s2, 6, "zaman");
  const wI2 = al(s2, 7, "I");
  const wAm = al(s2, 8, "am");
  const wLiving = al(s2, 9, "living");
  const wWith = al(s2, 10, "with");
  const wMy = al(s2, 11, "my");
  const wUncle = al(s2, 12, "uncle");
  const wOteki = al(s2, 13, "Öteki");
  const wSimdiki = al(s2, 14, "şimdiki");
  const wZaman2 = al(s2, 15, "zaman");
  const wIki = al(s2, 18, "iki");
  const wZamanin = al(s2, 19, "zamanın");
  const wFarkini = al(s2, 22, "farkını");
  const wAnlam = al(s2, 25, "anlam");
  const wBelirler = al(s2, 26, "belirler");

  FL0 = fr(wZamanin.t) + 3; // 392: etiketler solar, ders adı künyede belirir
  FL1 = FL0 + 18;           // 410: ders adı yerinde, rozet açılışı
  const sol = (f) => 1 - yumus((f - FL0) / (FL1 - FL0));   // etiketlerin solarak çıkışı

  // Şeride toplanma matrisi (B4). sx: yatay kayma + küçülme, sy: dikey kayma (kare). 2. parçalar önce
  // yana kayar, sonra yükselir; 1. parçalar daha kısa sürede yerleşir — geçişte yazılar kesişmez.
  const topla = (x0, y0, tx, ty, sx = 12, sy = 12) => (f) => {
    const q = yumus((f - CF0) / sx), qy = yumus((f - CF0) / sy);
    return new P.Matrix()
      .translate(lerp(x0, tx, q), lerp(y0, ty, qy))
      .scale(lerp(1, 0.5, q))
      .translate(-x0, -y0);
  };

  // B2: Kare 0 düzeni ve şerit hedefleri
  const B = 128;
  const S1X = 1032 - genislik("İstanbul'da yaşı-yor-um.", F(64));
  const txL1 = S1X;
  const txL2 = S1X + genislik("İstanbul'da ", F(64));
  const txL3 = 48;
  const txL4 = 48 + genislik("Amcamla ", F(64));

  // L1: İstanbul'da (hazır)
  yazi("İstanbul'da", {
    x: 96,
    y: 560,
    boyut: B,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: -10,
    sure: 4,
    matris: topla(96, 560, txL1, 420, 8, 8),
  });
  not("L1 İstanbul'da (hazır)", 0);

  // L2: yor kutusu ve parçaları
  const yx0 = 96 + genislik("yaşı-", F(B));
  const yx1 = 96 + genislik("yaşı-yor", F(B));

  const ogeL2 = S.oge({
    kucul: { f0: CF0, f1: CF0 + 6, fy0: CF0, fy1: CF1, s: 0.5, px: 96, py: 740, dx: txL2 - 96, dy: 420 - 740 },
  });
  ciz(
    [
      [yx0 - 0.05 * B, 740 - 0.17 * B],
      [yx1 + 0.05 * B, 740 - 0.17 * B],
    ],
    {
      duz: true,
      w: 1.0 * B,
      renk: DOLGU,
      alfa: 0.95,
      uc0: 8,
      uc1: 12,
      amp: 0.6,
      tur: "isaret",
      ad: "yor kutu L2",
      bas: -30,
      sure: 10,
      ses: false,
      oge: ogeL2,
    }
  );
  not("L2 yor kutusu (hazır)", 0);

  yazi("yaşı-", {
    x: 96,
    y: 740,
    boyut: B,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: -10,
    sure: 4,
    matris: topla(96, 740, txL2, 420, 6, 12),
  });
  yazi("yor", {
    x: yx0,
    y: 740,
    boyut: B,
    aile: "Fredoka",
    agirlik: 700,
    renk: PIL,
    bas: -10,
    sure: 4,
    matris: topla(96, 740, txL2, 420, 6, 12),
  });
  yazi("-um.", {
    x: yx1,
    y: 740,
    boyut: B,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: -10,
    sure: 4,
    matris: topla(96, 740, txL2, 420, 6, 12),
  });
  not("L2 yaşı-yor-um (hazır)", 0);

  // L3: Amcamla (hazır)
  yazi("Amcamla", {
    x: 96,
    y: 960,
    boyut: B,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: -10,
    sure: 4,
    matris: topla(96, 960, txL3, 520, 9, 9),
  });
  not("L3 Amcamla (hazır)", 0);

  // L4: yor kutusu ve parçaları
  const ogeL4 = S.oge({
    kucul: { f0: CF0, f1: CF0 + 6, fy0: CF0, fy1: CF1, s: 0.5, px: 96, py: 1140, dx: txL4 - 96, dy: 520 - 1140 },
  });
  ciz(
    [
      [yx0 - 0.05 * B, 1140 - 0.17 * B],
      [yx1 + 0.05 * B, 1140 - 0.17 * B],
    ],
    {
      duz: true,
      w: 1.0 * B,
      renk: DOLGU,
      alfa: 0.95,
      uc0: 8,
      uc1: 12,
      amp: 0.6,
      tur: "isaret",
      ad: "yor kutu L4",
      bas: 18,
      sure: 8,
      ses: "tik",
      oge: ogeL4,
    }
  );
  not("L4 yor kutusu", 18);

  const fYasi = f0(wYasiyorum1.t); // 12
  yazi("yaşı-", {
    x: 96,
    y: 1140,
    boyut: B,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: fYasi,
    sure: 4,
    ses: true,
    matris: topla(96, 1140, txL4, 520, 6, 12),
  });
  yazi("yor", {
    x: yx0,
    y: 1140,
    boyut: B,
    aile: "Fredoka",
    agirlik: 700,
    renk: PIL,
    bas: fYasi + 2,
    sure: 4,
    ses: false,
    matris: topla(96, 1140, txL4, 520, 6, 12),
  });
  yazi("-um.", {
    x: yx1,
    y: 1140,
    boyut: B,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: fYasi + 4,
    sure: 4,
    ses: false,
    matris: topla(96, 1140, txL4, 520, 6, 12),
  });
  not("L4 yaşı-yor-um", fYasi);

  // B3: Eşittir (=) çizgileri
  const OEQ = S.oge({
    alfa: (f) => (f < CF0 ? 1 : Math.max(0, 1 - (f - CF0) / 6)),
  });
  const yOrta = (740 - 0.17 * B + 1140 - 0.17 * B) / 2;
  ciz(
    [
      [872, yOrta - 18],
      [972, yOrta - 18],
    ],
    {
      duz: true,
      w: 9,
      renk: SARI,
      alfa: 0.9,
      sure: 8,
      uc0: 5,
      uc1: 8,
      amp: 0.4,
      ses: "tik",
      tur: "isaret",
      ad: "esittir ust",
      oge: OEQ,
      bas: fr(wIkisi.t),
    }
  );
  not("eşittir üst (ikisi)", fr(wIkisi.t));

  ciz(
    [
      [872, yOrta + 18],
      [972, yOrta + 18],
    ],
    {
      duz: true,
      w: 9,
      renk: SARI,
      alfa: 0.9,
      sure: 8,
      uc0: 5,
      uc1: 8,
      amp: 0.4,
      ses: "tik",
      tur: "isaret",
      ad: "esittir alt",
      oge: OEQ,
      bas: fr(wDe.t),
    }
  );
  not("eşittir alt (de)", fr(wDe.t));

  // B4: Şeride toplanma kaydı
  not("şeride toplanma", CF0);

  // B5: Kart A (sağa hizalı)
  kutu(48, 600, 984, 140, { bas: CF1 - 1, sure: 14, w: 4, ad: "kart A" });
  not("kart A kutu", CF1 - 1);

  const kelA = [
    wI1,
    wLive,
    wIn,
    { ...wIstanbul, s: "İstanbul." },
  ];
  const wCumleA = cumleGenislik(kelA, F(72));
  const x0A = 992 - wCumleA;
  const kelimelerA = cumle(kelA, {
    x: x0A,
    y: 695,
    boyut: 72,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
  });
  altCizgi(kelimelerA, { tut: 12 });
  not("kart A sözcükleri (I live in İstanbul.)", kelA[0].f);

  // Kart B (sola hizalı)
  kutu(48, 880, 984, 140, { bas: fr(wI2.t) - 4, sure: 14, w: 4, ad: "kart B" });
  not("kart B kutu", fr(wI2.t) - 4);

  const kelB = [
    wI2,
    wAm,
    wLiving,
    wWith,
    wMy,
    wUncle,
  ];
  const kelimelerB = cumle(kelB, {
    x: 88,
    y: 975,
    boyut: 72,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
  });
  altCizgi(kelimelerB, { tut: 14 });
  not("kart B sözcükleri (I am living with my uncle.)", kelB[0].f);

  // B6: Etiketler
  const EX = 992 - genislik("SIMPLE PRESENT vs", F(64));
  const xSimple = EX;
  const xPresentA = EX + genislik("SIMPLE ", F(64));
  const xVs = EX + genislik("SIMPLE PRESENT ", F(64));

  const xPresentB = 88;
  const xContinuous = 88 + genislik("PRESENT ", F(64));

  yazi("SIMPLE", {
    x: xSimple,
    y: 825,
    boyut: 64,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: fr(wGenis.t),
    sure: 6,
    ses: true,
    son: FL1,
    alfa: sol,
  });
  not("SIMPLE (geniş)", fr(wGenis.t));

  yazi("PRESENT", {
    x: xPresentA,
    y: 825,
    boyut: 64,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: fr(wZaman1.t),
    sure: 6,
    ses: true,
    son: FL1,
    alfa: sol,
  });
  not("PRESENT A (zaman)", fr(wZaman1.t));

  yazi("vs", {
    x: xVs,
    y: 825,
    boyut: 64,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: fr(wIki.t),
    sure: 6,
    ses: true,
    son: FL1,
    alfa: sol,
  });
  not("vs (iki)", fr(wIki.t));

  yazi("PRESENT", {
    x: xPresentB,
    y: 1105,
    boyut: 64,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: fr(wSimdiki.t),
    sure: 6,
    ses: true,
    son: FL1,
    alfa: sol,
  });
  not("PRESENT B (şimdiki)", fr(wSimdiki.t));

  yazi("CONTINUOUS", {
    x: xContinuous,
    y: 1105,
    boyut: 64,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: fr(wZaman2.t),
    sure: 6,
    ses: true,
    son: FL1,
    alfa: sol,
  });
  not("CONTINUOUS (zaman)", fr(wZaman2.t));

  // B7: Etiketler solar, ders adı künyede belirir; rozet
  olay(FL1, "tik", 0.4);
  not("etiket solma + künye ders belirme (zamanın)", FL0);
  not("künye ders ve rozet belirdi", FL1);

  // B8: Bağ okları
  // Ok 1: şerit 1. yor -> live
  const yor1StartX = txL2 + genislik("yaşı-", F(64));
  const yor1EndX = yor1StartX + genislik("yor", F(64));
  const yor1OrtaX = (yor1StartX + yor1EndX) / 2;
  const s2SagUc = 48 + genislik("Amcamla yaşı-yor-um.", F(64));
  const liveOrtaX = (kelimelerA[1].x0 + kelimelerA[1].x1) / 2;

  const a1 = [yor1OrtaX, 420 + 22];
  const ara1 = [
    [s2SagUc + 34, 566],
    [liveOrtaX + 14, 598],
  ];
  const b1 = [liveOrtaX, 695 - 0.72 * 72 - 10];

  ok(a1, b1, {
    ara: ara1,
    bas: fr(wBiri.t),
    sure: 18,
    w: 6,
    uzun: 20,
    ad: "bag ok 1",
    donus: fr(wI2.t),
  });
  not("bağ oku 1 (Biri)", fr(wBiri.t));

  // Ok 2: şerit 2. yor -> am living
  const yor2StartX = txL4 + genislik("yaşı-", F(64));
  const yor2EndX = yor2StartX + genislik("yor", F(64));
  const yor2OrtaX = (yor2StartX + yor2EndX) / 2;
  const amLivingOrtaX = (kelimelerB[1].x0 + kelimelerB[2].x1) / 2;

  const a2 = [yor2OrtaX, 520 + 22];
  const ara2 = [
    [330, 700],
    [amLivingOrtaX + 6, 880],
  ];
  const b2 = [amLivingOrtaX, 975 - 0.72 * 72 - 10];

  ok(a2, b2, {
    ara: ara2,
    bas: fr(wOteki.t),
    sure: 18,
    w: 6,
    uzun: 20,
    ad: "bag ok 2",
    donus: fr(wFarkini.t),
  });
  not("bağ oku 2 (Öteki)", fr(wOteki.t));

  // B9: Fark oku ve MEANING
  ok([960, 748], [960, 872], {
    cift: true,
    bas: fr(wFarkini.t),
    sure: 16,
    w: 7,
    uzun: 22,
    bukum: 0.05,
    ad: "fark oku",
    donus: fr(wAnlam.t),
  });
  not("fark oku (farkını)", fr(wFarkini.t));

  // MEANING belirteci (yazının altında kalması için önce çizilir)
  const wMeaning = genislik("MEANING", F(140));
  const mx0 = 540 - wMeaning / 2;
  const mx1 = 540 + wMeaning / 2;
  const yMeaning = 1310;

  ciz(
    [
      [mx0 - 14, yMeaning - 0.18 * 140],
      [mx1 + 16, yMeaning - 0.18 * 140],
    ],
    {
      duz: true,
      w: 0.36 * 140,
      renk: DOLGU,
      alfa: 0.8,
      uc0: 6,
      uc1: 14,
      amp: 1.2,
      bas: fr(wAnlam.t),
      sure: fr(wBelirler.t) - fr(wAnlam.t),
      tur: "isaret",
      ses: false,
      ad: "MEANING belirtec",
    }
  );
  not("MEANING belirteç (anlam)", fr(wAnlam.t));

  yazi("MEANING", {
    x: 540,
    y: yMeaning,
    hizala: "orta",
    boyut: 140,
    aile: "Fredoka",
    agirlik: 700,
    renk: MUR,
    bas: fr(wAnlam.t),
    sure: 8,
    olcek: true,
    ses: true,
  });
  not("MEANING (anlam)", fr(wAnlam.t));

  return S;
}

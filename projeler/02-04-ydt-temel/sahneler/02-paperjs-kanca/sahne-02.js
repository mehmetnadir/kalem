// Sahne 02 — Kanca (Paper.js, 529 kare, t_bas 3,00). 02-04 YDT temel.
// Yerel kare = round((t − 3,00) × 30). Sözcük zamanları sozcukler.json'dan al() ile doğrulanır.
import { sahneKur, RT, KUNYE } from "/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 529, T_BAS = 3.0;

export async function kur(P) {
  let F_IN = Infinity;
  const S = await sahneKur(P, {
    KARE,
    tBas: T_BAS,
    bolum: "Hook",
    etkin: 0,
    kayma: 0,
    dersGoster: (f) => f >= F_IN,
  });

  const { fr, ok, kutu, yazi, cumle, altCizgi, ciz, olay, not, lerp, yumus, genislik } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu;
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const f0 = (t) => Math.max(12, fr(t));

  // Ölçü ve yardımcılar
  const W = 1920, H = 1080, u = (n) => (n * W) / 1920;
  const TABAN = u(30);
  const font = (b) => `700 ${b}px Fredoka`;
  const sigdir = (metinler, azami, gen) =>
    Math.max(TABAN, Math.min(azami, ...metinler.map((m) => (azami * gen) / genislik(m, font(azami)))));

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

  // Yerleşim (iki sütun)
  const CX = [W * 0.255, W * 0.745], CW = W * 0.42;
  const Y_TR = H * 0.262;
  const metinlerTR = ["İstanbul'da yaşı-yor-um.", "Amcamla yaşı-yor-um."];
  const BTR = sigdir(metinlerTR, u(64), CW - u(40));

  const Y_KART = H * 0.352, CH = H * 0.185;
  const metinlerEN = ["I live in İstanbul.", "I am living with my uncle."];
  const BEN = sigdir(metinlerEN, u(64), CW - u(70));
  const yb = Y_KART + CH / 2 + BEN * 0.36;

  const Y_AD = H * 0.63, BAD = u(44);
  const Y_ANLAM = H * 0.80, B_ANLAM = u(110);

  // Künye uçuş zamanları (Madde 16)
  const wZamanin = al(s2, 19, "zamanın");
  const FL0 = fr(wZamanin.t) + 3;
  const FL1 = FL0 + 18;
  F_IN = FL1;

  const fontKunye = font(KUNYE.dersYazi);
  const txSimple = KUNYE.kenar + genislik("", fontKunye);
  const txPresentSol = KUNYE.kenar + genislik("SIMPLE ", fontKunye);
  const txVs = KUNYE.kenar + genislik("SIMPLE PRESENT ", fontKunye);
  const txPresentSag = KUNYE.kenar + genislik("SIMPLE PRESENT vs ", fontKunye);
  const txContinuous = KUNYE.kenar + genislik("SIMPLE PRESENT vs PRESENT ", fontKunye);

  const ucusMatris = (x0, tx) => (f) => {
    if (f < FL0) return new P.Matrix();
    const q = yumus((f - FL0) / (FL1 - FL0));
    const sc = lerp(1, KUNYE.dersYazi / BAD, q);
    return new P.Matrix()
      .translate(lerp(x0, tx, q), lerp(Y_AD, KUNYE.ustTaban, q))
      .scale(sc)
      .translate(-x0, -Y_AD);
  };

  // 1. İki Türkçe satır hazır (sahne 01'den)
  const trSol = yazi("İstanbul'da yaşı-yor-um.", {
    x: CX[0],
    y: Y_TR,
    hizala: "orta",
    boyut: BTR,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: -10,
    sure: 4,
  });
  const trSag = yazi("Amcamla yaşı-yor-um.", {
    x: CX[1],
    y: Y_TR,
    hizala: "orta",
    boyut: BTR,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: -10,
    sure: 4,
  });
  not("Türkçe satırlar (hazır)", 0);

  // 2. 1. satır yor kutusu hazır
  const yx0Sol = trSol.x0 + genislik("İstanbul'da yaşı-", font(BTR));
  const yx1Sol = yx0Sol + genislik("yor", font(BTR));
  ciz(
    [
      [yx0Sol - u(5), Y_TR - BTR * 0.28],
      [yx1Sol + u(6), Y_TR - BTR * 0.28],
    ],
    {
      duz: true,
      w: BTR * 0.74,
      renk: DOLGU,
      alfa: 0.6, uc0: u(5), uc1: u(9), amp: 1.0,
      bas: -30,
      sure: 10,
      tur: "isaret",
      ses: false,
      ad: "sol yor bant",
    }
  );
  not("sol yor kutusu (hazır)", 0);

  // 3. 2. satır yor kutusu
  const wYasiyorum1 = al(s1, 3, "yaşıyorum");
  const yx0Sag = trSag.x0 + genislik("Amcamla yaşı-", font(BTR));
  const yx1Sag = yx0Sag + genislik("yor", font(BTR));
  ciz(
    [
      [yx0Sag - u(5), Y_TR - BTR * 0.28],
      [yx1Sag + u(6), Y_TR - BTR * 0.28],
    ],
    {
      duz: true,
      w: BTR * 0.74,
      renk: DOLGU,
      alfa: 0.6, uc0: u(5), uc1: u(9), amp: 1.0,
      bas: f0(wYasiyorum1.t),
      sure: 8,
      tur: "isaret",
      ses: "tik",
      ad: "sağ yor bant",
    }
  );
  not("sağ yor kutusu (yaşıyorum)", f0(wYasiyorum1.t));

  // 4 & 5. Satırlar arasında sarı "=" çizgileri
  const wIkisi = al(s1, 5, "ikisi");
  const wDe = al(s1, 6, "de");
  const xEsit = (trSol.x1 + trSag.x0) / 2;
  const yEsit = Y_TR - BTR * 0.3;
  ciz(
    [
      [xEsit - u(26), yEsit - u(10)],
      [xEsit + u(26), yEsit - u(10)],
    ],
    {
      duz: true,
      w: u(7),
      renk: SARI, alfa: 0.9, uc0: u(5), uc1: u(8), amp: 0.4,
      bas: fr(wIkisi.t),
      sure: 8,
      tur: "isaret",
      ses: "tik",
      ad: "esittir ust",
    }
  );
  not("eşittir 1. çizgi (ikisi)", fr(wIkisi.t));

  ciz(
    [
      [xEsit - u(26), yEsit + u(10)],
      [xEsit + u(26), yEsit + u(10)],
    ],
    {
      duz: true,
      w: u(7),
      renk: SARI, alfa: 0.9, uc0: u(5), uc1: u(8), amp: 0.4,
      bas: fr(wDe.t),
      sure: 8,
      tur: "isaret",
      ses: "tik",
      ad: "esittir alt",
    }
  );
  not("eşittir 2. çizgi (de)", fr(wDe.t));

  // 6. Sol kart kutusu
  const wI1 = al(s2, 0, "I");
  kutu(CX[0] - CW / 2, Y_KART, CW, CH, {
    bas: fr(wI1.t) - 14,
    sure: 16,
    w: u(4),
    ad: "sol kart",
  });
  not("sol kart kutusu (I)", fr(wI1.t) - 14);

  // 7. Sol kart sözcükleri + karaoke
  const kelSol = [
    al(s2, 0, "I"),
    al(s2, 1, "live"),
    al(s2, 2, "in"),
    { ...al(s2, 3, "Istanbul"), s: "İstanbul." },   // ekran metni İ ile (senaryo ekran sütunu)
  ];
  const wSolCumle = cumleGenislik(kelSol, font(BEN));
  const kelimelerSol = cumle(kelSol, {
    x: CX[0] - wSolCumle / 2,
    y: yb,
    boyut: BEN,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
  });
  altCizgi(kelimelerSol, { tut: 30 });
  not("sol kart sözcükleri (I live in Istanbul)", kelSol[0].f);

  // 8. bag: sol yor -> live
  const wBiri = al(s2, 4, "Biri");
  const ycSol = (yx0Sol + yx1Sol) / 2;
  const liveOrtasi = (kelimelerSol[1].x0 + kelimelerSol[1].x1) / 2;
  ok(
    [ycSol, Y_TR + BTR * 0.2 + u(10)],
    [liveOrtasi, yb - BEN * 0.86 - u(8)],
    {
      bas: fr(wBiri.t),
      sure: 16,
      w: u(6),
      uzun: u(20),
      bukum: 0.05,
      ad: "sol bag ok",
    }
  );
  not("sol bağ oku (Biri)", fr(wBiri.t));

  // 9 & 10. SIMPLE PRESENT (sol kart altı)
  const wGenis = al(s2, 5, "geniş");
  const wZaman1 = al(s2, 6, "zaman");
  const fontAD = font(BAD);
  const boslukAD = genislik(" ", fontAD);
  const wSimple = genislik("SIMPLE", fontAD);
  const wPresentSol = genislik("PRESENT", fontAD);
  const wSolAd = wSimple + boslukAD + wPresentSol;
  const xSimple = CX[0] - wSolAd / 2;
  const xPresentSol = xSimple + wSimple + boslukAD;

  yazi("SIMPLE", {
    x: xSimple,
    y: Y_AD,
    boyut: BAD,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: fr(wGenis.t),
    sure: 6,
    ses: true,
    son: FL1,
    matris: ucusMatris(xSimple, txSimple),
  });
  not("SIMPLE (geniş)", fr(wGenis.t));

  yazi("PRESENT", {
    x: xPresentSol,
    y: Y_AD,
    boyut: BAD,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: fr(wZaman1.t),
    sure: 6,
    ses: true,
    son: FL1,
    matris: ucusMatris(xPresentSol, txPresentSol),
  });
  not("PRESENT sol (zaman)", fr(wZaman1.t));

  // 11. Sağ kart kutusu
  const wI2 = al(s2, 7, "I");
  kutu(CX[1] - CW / 2, Y_KART, CW, CH, {
    bas: fr(wI2.t) - 14,
    sure: 16,
    w: u(4),
    ad: "sağ kart",
  });
  not("sağ kart kutusu (I)", fr(wI2.t) - 14);

  // 12. Sağ kart sözcükleri + karaoke
  const kelSag = [
    al(s2, 7, "I"),
    al(s2, 8, "am"),
    al(s2, 9, "living"),
    al(s2, 10, "with"),
    al(s2, 11, "my"),
    al(s2, 12, "uncle"),
  ];
  const wSagCumle = cumleGenislik(kelSag, font(BEN));
  const kelimelerSag = cumle(kelSag, {
    x: CX[1] - wSagCumle / 2,
    y: yb,
    boyut: BEN,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
  });
  altCizgi(kelimelerSag, { tut: 30 });
  not("sağ kart sözcükleri (I am living with my uncle)", kelSag[0].f);

  // 13. bag: sağ yor -> am living
  const wOteki = al(s2, 13, "Öteki");
  const ycSag = (yx0Sag + yx1Sag) / 2;
  const hedefX = (kelimelerSag[1].x0 + kelimelerSag[2].x1) / 2;
  ok(
    [ycSag, Y_TR + BTR * 0.2 + u(10)],
    [hedefX, yb - BEN * 0.86 - u(8)],
    {
      bas: fr(wOteki.t),
      sure: 16,
      w: u(6),
      uzun: u(20),
      bukum: 0.05,
      ad: "sağ bag ok",
    }
  );
  not("sağ bağ oku (Öteki)", fr(wOteki.t));

  // 14. PRESENT / CONTINUOUS (sağ kart altı)
  const wSimdiki = al(s2, 14, "şimdiki");
  const wZaman2 = al(s2, 15, "zaman");
  const wPresentSag = genislik("PRESENT", fontAD);
  const wContinuous = genislik("CONTINUOUS", fontAD);
  const wSagAd = wPresentSag + boslukAD + wContinuous;
  const xPresentSag = CX[1] - wSagAd / 2;
  const xContinuous = xPresentSag + wPresentSag + boslukAD;

  yazi("PRESENT", {
    x: xPresentSag,
    y: Y_AD,
    boyut: BAD,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: fr(wSimdiki.t),
    sure: 6,
    ses: true,
    son: FL1,
    matris: ucusMatris(xPresentSag, txPresentSag),
  });
  not("PRESENT sağ (şimdiki)", fr(wSimdiki.t));

  yazi("CONTINUOUS", {
    x: xContinuous,
    y: Y_AD,
    boyut: BAD,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: fr(wZaman2.t),
    sure: 6,
    ses: true,
    son: FL1,
    matris: ucusMatris(xContinuous, txContinuous),
  });
  not("CONTINUOUS (zaman)", fr(wZaman2.t));

  // 15. vs ortada
  const wIki = al(s2, 18, "iki");
  const wVs = genislik("vs", fontAD);
  const xVs = W / 2 - wVs / 2;
  yazi("vs", {
    x: xVs,
    y: Y_AD,
    boyut: BAD,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: fr(wIki.t),
    sure: 6,
    ses: true,
    son: FL1,
    matris: ucusMatris(xVs, txVs),
  });
  not("vs (iki)", fr(wIki.t));

  // 16. Başlık künyeye uçar
  olay(FL1, "tik", 0.4);
  not("başlık künyeye uçuş (zamanın)", FL0);
  not("künye ders belirdi", FL1);

  // 17. İki uçlu sarı fark oku
  const wFarkini = al(s2, 22, "farkını");
  ok([CX[0], H * 0.62], [CX[1], H * 0.62], {
    bas: fr(wFarkini.t),
    cift: true,
    sure: 20,
    w: u(7),
    uzun: u(24),
    bukum: 0.03,
    ad: "fark oku",
  });
  not("fark oku (farkını)", fr(wFarkini.t));

  // 18. MEANING + sarı belirteç
  const wAnlam = al(s2, 25, "anlam");
  const wBelirler = al(s2, 26, "belirler");
  const fontAnlam = font(B_ANLAM);
  const wMeaning = genislik("MEANING", fontAnlam);
  const x0Meaning = W / 2 - wMeaning / 2;
  const x1Meaning = x0Meaning + wMeaning;

  ciz(
    [
      [x0Meaning - u(14), Y_ANLAM - B_ANLAM * 0.18],
      [x1Meaning + u(16), Y_ANLAM - B_ANLAM * 0.18],
    ],
    {
      duz: true,
      w: B_ANLAM * 0.4,
      renk: DOLGU,
      alfa: 0.7, uc0: u(6), uc1: u(14), amp: 1.2,
      bas: fr(wAnlam.t) - 5,
      sure: fr(wBelirler.t) - fr(wAnlam.t) + 5,
      tur: "isaret",
      ses: false,
      ad: "MEANING belirteç",
    }
  );
  not("MEANING belirteç (anlam)", fr(wAnlam.t) - 5);

  yazi("MEANING", {
    x: W / 2,
    y: Y_ANLAM,
    hizala: "orta",
    boyut: B_ANLAM,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: fr(wAnlam.t),
    sure: 8,
    olcek: true,
    ses: true,
  });
  not("MEANING (anlam)", fr(wAnlam.t));

  return S;
}

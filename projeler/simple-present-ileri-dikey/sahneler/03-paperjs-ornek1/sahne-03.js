// Sahne 03 (İLERİ, DİKEY 1080x1920) — Örnek 1 (456 kare, t_bas 17,65;
// cümle 3). Yerel kare = round((t − 17,65) × 30).
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (kalem-paper.js çizer),
// platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–694) · TR 2 satır (708–832) · formül kartı tek
// satır (846–946) · sahne altta sabit 430 px (960–1390).
// Toplanma / küçültme YOK: figür baştan sona 430 px.
import {
  sahneKur,
  RT
} from "/projeler/simple-present-ileri-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";
import {
  yaziNoktalari
} from "/projeler/simple-present-ileri-dikey/ortak/kalem-canvas.js";

export const KARE = 456, T_BAS = 17.65;

export async function kur(P) {
  const S = await sahneKur(P, {
    KARE,
    tBas: T_BAS,
    bolum: "Example 1 / 3",
    etkin: 1,
    kayma: 0
  });
  const {
    fr,
    ciz,
    daire,
    ok,
    kutu,
    yazi,
    elYazisi,
    cumle,
    altCizgi,
    parilti,
    olay,
    not,
    bitis
  } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  const GB = 12;
  const f0 = (t) => Math.max(GB, fr(t));
  // El yazısı (Caveat 700 tegaki, dalga 5b / K26): not ve etiketler kalemle
  // yazılır. Ortaya hizada genişlik tegaki verisinden ölçülür; sözcük
  // pencereleri anlatımın f/f1 karelerinden gelir (2-3 harflik kısa pencere
  // sonraki sözcüğün başına dek uzar).
  const [eyM, eyG] = await Promise.all([
    fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")
  ]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, {
    upm: EY.M.unitsPerEm,
    asc: EY.M.ascender,
    boy: boyut,
    x: 0,
    taban: 0
  }).gen;
  const pen = (liste) => liste.map((w, i) => ({
    f0: w.f,
    f1: w.f1 - w.f < 6 && liste[i + 1] ? liste[i + 1].f : w.f1
  }));

  // --- 18,20: kart çerçevesi (el kutusu, 4 px) — içerik bandı 352–1392'nin
  // üst parçası
  kutu(48, 372, 984, 322, {
    bas: f0(18.20),
    sure: 30,
    w: 4.2,
    renk: IKI
  });
  not("kart çerçevesi", f0(18.20));

  // --- 19,41–23,17: İngilizce kök (Fredoka 64, 4 satır, sözcük zamanlı);
  // satır başı 4 / 8 / 12
  const sz = S.sozcukler(3).slice(2, 16); // Although … need.
  const satirNo = (i) => (i < 4 ? 0 : i < 8 ? 1 : i < 12 ? 2 : 3);
  const cz = cumle(
    sz.map((k, i) => ({ s: k.s, f: k.f, satir: satirNo(i) })),
    { x: 88, y: 448, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 72 }
  );
  altCizgi(cz, { tut: 40, w: 8 });
  not("cümle başı (Although)", cz[0].bas);
  { // gives (21,73): kalıcı sarı alt çizgi
    const g = cz[8], c = ciz(
      [[g.x0 - 4, g.y + 14], [g.x1 + 4, g.y + 10]],
      {
        w: 10,
        renk: SARI,
        alfa: 0.85,
        duz: true,
        bas: fr(21.78),
        sure: 12,
        uc0: 8,
        uc1: 14,
        amp: 0.8
      }
    );
    not("gives alt çizgisi", c.bas);
  }

  // --- 19,41–23,77: ALT sahne (960–1390): güneş 430 px + ağaç 430 px,
  // ok "enerji" — baştan sona sabit 430 px
  await S.svgCiz("coco/sun.svg", {
    kutu: [48, 960, 430, 430],
    bas: f0(19.5),
    sure: fr(20.9) - f0(19.5),
    azami: 30,
    w: 4.4,
    sesAralik: 4
  });
  not("güneş çizimi başı", f0(19.5));
  await S.svgCiz("coco/tree.svg", {
    kutu: [602, 960, 430, 430],
    bas: f0(22.0),
    sure: fr(23.77) - f0(22.0),
    azami: 40,
    w: 4.4,
    sesAralik: 5
  });
  not("ağaç çizimi başı", f0(22.0));
  const a1 = ok([492, 1175], [590, 1175], {
    bas: fr(21.80),
    sure: 14,
    w: 10,
    uzun: 24,
    bukum: 0.1
  });
  not("enerji oku", a1.bas);
  // 22,75 anlatımsız etiket `enerji`: hedef 14 kare (0,47 sn) → 23,22; orta x 541
  elYazisi("enerji", {
    x: 541 - eyGen("enerji", 64) / 2,
    y: 1260,
    boyut: 64,
    renk: SARI,
    bas: fr(22.75),
    sure: 14
  });

  // --- 24,30–27,34: Türkçe çeviri (Caveat 64 mürekkep, 2 satır, ≤ 34 k/satır)
  // Güneş küçük görünse de bitkilere gereken enerjiyi verir.
  // 24,30–27,34 «Güneş küçük görünse de / bitkilere gereken enerjiyi verir.»
  // (pencere: sözcük başına f–f1; `de` 0,32 sn, satır 1'in son sözcüğü; uzatma yok)
  const tr = S.sozcukler(3).slice(16, 24);
  const trSatir = (a, b, y) => elYazisi(
    tr.slice(a, b).map((k) => k.s).join(" "),
    { x: 88, y, boyut: 64, renk: KRE, sozcukler: pen(tr.slice(a, b)) }
  );
  const tz1 = trSatir(0, 4, 758);
  trSatir(4, 8, 814);
  not("Türkçe çeviri", tz1.bas);

  // --- 28,40–32,45: formül kartı tek satır (835–945):
  // zaman değişmez · it gives (V-s)
  {
    const a = cz[0];
    const k = kutu(a.x0 - 10, a.y - 54, a.w + 20, 76, {
      bas: fr(28.93),
      sure: 14,
      w: 6,
      renk: SARI
    });
    olay(k.bit, "tik", 0.5);
    not("Although kutusu", fr(28.93));
    kutu(48, 846, 984, 100, {
      bas: fr(28.4),
      sure: 26,
      w: 4.2,
      renk: IKI
    });
    not("formül kartı kutusu", fr(28.4));
    const F = { boyut: 64, aile: "Fredoka", agirlik: 700 };
    const YK = 918;
    const z = yazi("zaman", {
      ...F,
      x: 88,
      y: YK,
      bas: fr(29.97),
      sure: 10,
      olcek: true,
      ses: true
    });
    const zd = yazi("değişmez", {
      ...F,
      x: z.x1 + 18,
      y: YK,
      bas: fr(30.37),
      sure: 10,
      olcek: true,
      renk: SARI,
      ses: true
    });
    not("zaman değişmez", fr(29.97));
    const g = cz[8];
    const dg = daire(
      (g.x0 + g.x1) / 2,
      g.y - 22,
      (g.x1 - g.x0) / 2 + 8,
      46,
      { bas: fr(31.62), sure: 18, a0: -2.6, egim: -0.03, w: 10 }
    );
    olay(bitis(dg), "tik", 0.5);
    not("gives daire", dg.bas);
    const nok = yazi("·", {
      ...F,
      x: zd.x1 + 22,
      y: YK,
      bas: fr(31.66),
      sure: 8,
      renk: IKI
    });
    const s1 = yazi("it give", {
      ...F,
      x: nok.x1 + 22,
      y: YK,
      bas: fr(31.66),
      sure: 10,
      olcek: true
    });
    const s2 = yazi("s", {
      ...F,
      x: s1.x1 + 2,
      y: YK,
      bas: fr(31.72),
      sure: 10,
      olcek: true,
      renk: SARI,
      ses: true
    });
    // 31,90 anlatımsız etiket `(V-s)`: hedef 14 kare (0,47 sn) → 32,37
    elYazisi("(V-s)", {
      x: s2.x1 + 24,
      y: YK,
      boyut: 72,
      renk: SARI,
      bas: fr(31.9),
      sure: 14
    });
    not("it gives (V-s)", fr(31.66));
    parilti(1008, 880, { bas: fr(32.0), r: 18 });
  }
  return S;
}

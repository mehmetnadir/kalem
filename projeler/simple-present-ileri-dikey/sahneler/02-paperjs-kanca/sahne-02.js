// Sahne 02 İLERİ DİKEY (Simple Present) — Kanca + kural
// (451 kare, t_bas 3,00; cümle 2), 1080x1920.
// Bantlar: içerik 352–1392 (dolu), altyazı 1400–1536 (kalem-paper.js çizer),
// platform 1536–1920 boş.
// Dikey akış (üstten alta): cümle 1 · will ? Simple Present · KURAL positive ·
// negative/question · ajanda kartı.
import {
  sahneKur,
  RT
} from "/projeler/simple-present-ileri-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 451, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, {
    KARE,
    tBas: T_BAS,
    bolum: "Hook",
    etkin: 0,
    kayma: 0
  });
  const {
    fr,
    daire,
    yazi,
    cumle,
    tik,
    parilti,
    olay,
    not,
    bitis,
    kutu,
    ok,
    svgCiz
  } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep;

  // --- cümle 1: tek satır Caveat 80 (x 64, taban 430); 0. karede hazır
  // (sahne 01 ile aynı yer)
  const c1 = cumle(
    ["Uçak", "yarın", "dokuzda", "kalkıyor."].map((s) => ({ s, f: -10 })),
    { x: 64, y: 430, boyut: 80, aile: "Caveat", agirlik: 700 }
  );
  not("cümle 1 yerinde", 0);
  {   // kalkıyor sarı daire titrer (3,00–3,71)
    const g = c1[3], tit = S.oge({ tit: { f0: 0, f1: fr(3.71), g: 3 } });
    daire(
      (g.x0 + g.x1) / 2,
      g.y - 28,
      g.w / 2 + 16,
      46,
      { bas: -30, sure: 20, ses: false, oge: tit, w: 10 }
    );
    not("kalkıyor daire titrer", 0);
  }

  // --- 3,95–6,0: büyük ? ve iki kutu will / Simple Present (y 480–650)
  yazi("?", {
    x: 332,
    y: 640,
    boyut: 230,
    aile: "Caveat",
    agirlik: 700,
    hizala: "orta",
    renk: SARI,
    bas: fr(3.95),
    sure: 12,
    olcek: true,
    ses: "vurus"
  });
  not("büyük ?", fr(3.95));
  kutu(48, 480, 220, 170, { bas: fr(4.51), sure: 26, w: 4.4 });
  yazi("will", {
    x: 158,
    y: 593,
    boyut: 80,
    aile: "Fredoka",
    agirlik: 700,
    hizala: "orta",
    renk: KRE,
    bas: fr(4.79),
    sure: 8,
    olcek: true,
    ses: true
  });
  not("kutu will", fr(4.51));
  kutu(432, 480, 600, 170, { bas: fr(5.0), sure: 28, w: 4.4 });
  yazi("Simple Present", {
    x: 732,
    y: 593,
    boyut: 80,
    aile: "Fredoka",
    agirlik: 700,
    hizala: "orta",
    renk: KRE,
    bas: fr(5.23),
    sure: 9,
    olcek: true,
    ses: true
  });
  not("kutu Simple Present", fr(5.0));

  // --- 6,19: KURAL etiketi; 7,24: positive
  const k1 = yazi("KURAL", {
    x: 48,
    y: 750,
    boyut: 64,
    renk: SARI,
    bas: fr(6.19),
    sure: 10,
    ses: true
  });
  not("KURAL etiketi", fr(6.19));
  parilti(1000, 700, { bas: fr(6.5), r: 28, periyot: 0, adet: 1 });
  yazi("· Positive", {
    x: k1.x1 + 18,
    y: 750,
    boyut: 64,
    renk: SARI,
    bas: fr(7.24),
    sure: 10,
    ses: true
  });
  not("Positive etiketi", fr(7.24));

  // --- 7,24–10,60: he · she · it → V-s (Fredoka 96, taban 870)
  {
    const Y = 870; let x = 48; const gap = 26;
    const koy = (s, t, o = {}) => {
      const y = yazi(s, {
        x,
        y: Y,
        boyut: 96,
        aile: "Fredoka",
        agirlik: 700,
        renk: o.renk || KRE,
        bas: fr(t),
        sure: 8,
        olcek: true,
        ses: o.ses !== false
      });
      x = y.x1 + gap;
      return y;
    };
    koy("he", 8.32);
    koy("·", 8.42, { renk: SARI, ses: false });
    koy("she", 8.52);
    koy("·", 8.7, { renk: SARI, ses: false });
    koy("it", 8.84);
    not("he · she · it", fr(8.32));
    const a = ok([x - 6, Y - 36], [x + 92, Y - 36], {
      bas: fr(9.0),
      sure: 12,
      w: 10,
      uzun: 28,
      bukum: 0.04
    });
    void a;
    x += 112;
    const v = koy("V-s", 9.16, { renk: SARI });
    not("V-s (takes)", fr(9.16));
    const d = daire(
      (v.x0 + v.x1) / 2,
      Y - 32,
      v.w / 2 + 20,
      58,
      { bas: fr(9.45), sure: 20, w: 10 }
    );
    olay(bitis(d), "tik", 0.5);
    not("V-s daire", d.bas);
  }

  // --- 10,60–13,97: negative · question → does + base verb (taban 1085)
  {
    const e1 = yazi("Negative", {
      x: 48,
      y: 975,
      boyut: 64,
      renk: SARI,
      bas: fr(10.6),
      sure: 10,
      ses: true
    });
    not("Negative etiketi", fr(10.6));
    yazi("· Question", {
      x: e1.x1 + 18,
      y: 975,
      boyut: 64,
      renk: SARI,
      bas: fr(11.24),
      sure: 10,
      ses: true
    });
    const Y = 1085; let x = 80; const gap = 26;
    const koy = (s, t, o = {}) => {
      const y = yazi(s, {
        x,
        y: Y,
        boyut: 96,
        aile: "Fredoka",
        agirlik: 700,
        renk: o.renk || KRE,
        bas: fr(t),
        sure: 8,
        olcek: true,
        ses: o.ses !== false
      });
      x = y.x1 + gap;
      return y;
    };
    const dz = koy("does", 12.28, { renk: SARI });
    not("does", fr(12.28));
    const dd = daire(
      (dz.x0 + dz.x1) / 2,
      Y - 32,
      dz.w / 2 + 20,
      58,
      { bas: fr(12.45), sure: 18, w: 10 }
    );
    olay(bitis(dd), "tik", 0.5);
    not("does daire", dd.bas);
    koy("+", 12.6, { renk: SARI, ses: false });
    koy("base", 12.92);
    koy("verb", 13.24);
    not("base verb", fr(12.92));
  }

  // --- 13,97–17,25: ajanda kartı (y 1150–1390): form · zaman ifadeleri ·
  // 3 YDT kökü; saat + 6 min
  kutu(48, 1150, 984, 240, { bas: fr(13.97), sure: 30, w: 4.4 });
  not("ajanda kartı", fr(13.97));
  await svgCiz("tabler/clock.svg", {
    kutu: [830, 1178, 150, 150],
    bas: fr(14.1),
    sure: 24,
    azami: 25,
    w: 4.4,
    sesAralik: 2
  });
  yazi("6 min", {
    x: 905,
    y: 1372,
    boyut: 64,
    hizala: "orta",
    renk: SARI,
    bas: fr(14.4),
    sure: 12,
    ses: true
  });
  not("saat + 6 min", fr(14.1));
  [
    ["form", 14.85, 1224],
    ["zaman ifadeleri", 15.41, 1294],
    ["3 YDT kökü", 16.05, 1364]
  ].forEach(([s, t, y]) => {
    const z = yazi(s, {
      x: 96,
      y,
      boyut: 64,
      aile: "Fredoka",
      agirlik: 700,
      renk: KRE,
      bas: fr(t),
      sure: 8,
      olcek: true,
      ses: true
    });
    tik(z.x1 + 52, y - 22, { bas: fr(t) + 9 });
    not("madde " + s, fr(t));
  });
  parilti(1000, 1175, { bas: fr(16.9), r: 28, periyot: 0, adet: 1 });
  return S;
}

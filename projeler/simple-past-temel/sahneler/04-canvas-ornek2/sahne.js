// SAHNE 04 — Örnek 2 (Simple Past, düz canvas, 566 kare, t_bas 31,35; cümle 4). Zaman yalnız kare numarasından.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, ok, elips, olc } from "./sahne-ortak.js";

const KARE = 566, TBAS = 31.35, ICERIK = 554;
const KOKDIZ = "/projeler/simple-past-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIRMIZI = RT.kirmizi;
const FF = (b) => `700 ${b}px Fredoka`;
const pencere = (ad, yakin, adet) => S.dizi(ad, yakin, adet).map((w) => ({ t0: w.t0, t1: w.t1 }));

async function kur() {
  await S.kur();
  const [figur, ucak, kitap, takvim] = await Promise.all([svgOku("open-peeps/standing-5.svg"), svgOku("tabler/plane.svg"),
    svgOku("tabler/book.svg"), svgOku("tabler/calendar.svg")]);

  // 31,35–32,39 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 190, 205, S.zm(12)));

  // 32,64–35,60 cümle (2 satır) + sarı alt çizgi
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("My", 32.64, 8), x: 140, y: 335, maxGen: 800 }));
  const sonSatir = Math.max(...cum.kel.map((k) => k.y));
  const kel = (ad) => cum.kel.find((k) => k.m.replace(/[.,?!:]/g, "") === ad);

  // 32,8–35,0 sağ: ayakta figür + uçak (420 px), uçağın arkasında 3 hız çizgisi
  S.koy(S.cizim({ svg: figur, kutu: { x: 1010, y: 230, w: 300, h: 560 }, ad: "figur", esik: 0.004, enCok: 60, w: 3.4, tb: 32.8, sure: 1.6,
    olayEnCok: 7 }));
  S.koy(S.cizim({ svg: ucak, kutu: { x: 1420, y: 300, w: 420, h: 420 }, ad: "ucak", enCok: 12, w: 4, tb: 33.9, sure: 0.9, olayEnCok: 4 }));
  [[1325, 480, 1425], [1355, 520, 1430], [1335, 560, 1420]].forEach(([x0, y, x1], i) => {
    S.koy(S.darbe([[x0, y], [(x0 + x1) / 2, y + 1], [x1, y]], { w: 5.5, renk: SARI, alfa: 0.85, uc0: 8, uc1: 22, duz: true, tohum: 40 + i },
      34.75 + i * 0.12, 0.22, i === 0 ? 0.5 : false));
  });
  S.koy(S.parilti(1800, 330, 35.0, 24));

  // 34,64 ago sarı daire
  S.koy(S.halka(kel("ago"), 34.64, 0.3, 11));

  // 35,85–38,65 Türkçe çeviri (el yazısı 48 ikincil; sözcük penceresi: Amcam 35,85 · iki 36,41 ·
  // yıl 36,62 · önce 36,77 · Londra'ya 37,09 · gitti. 37,57–38,65 sn; kaynak cümle 4)
  const ytr = sonSatir + 80;
  S.koy(S.elYazisi({ metin: "Amcam iki yıl önce Londra'ya gitti.", x: 140, y: ytr, renk: IKINCIL,
    sozcukler: pencere("Amcam", 35.85, 6) }));

  // 38,73–41,13 takvim şeridi: 4 el kutusu `two years ago`, sağda now noktası, sola giden ok `ago = önce`, tik
  const yKutu = 590, kh = 80, xs = 140;
  S.koy(S.elYazisi({ metin: "two years ago", x: xs, y: yKutu - 22, boy: 52, renk: SARI, tb: 38.73,
    sure: 0.5 }));                                  // etiket, 38,73–39,23 sn
  for (let i = 0; i < 4; i++) {
    S.koy(S.darbeler(kutu(xs + 154 * i, yKutu, 140, kh, 20 + i), { w: 3.4, renk: KREM, uc0: 8, uc1: 14 }, 38.85 + i * 0.2, 0.12, 0.07, 0.45));
  }
  S.koy(S.cizim({ svg: takvim, kutu: { x: 790, y: 565, w: 80, h: 80 }, ad: "takvim", enCok: 8, w: 3.4, tb: 39.0, sure: 0.5, olayEnCok: 1, nefes: false }));
  const nx = 935, ny = yKutu + kh / 2, nf = S.fr(40.7);
  S.olay(nf, "tik", 0.5);
  S.koy({ ciz: (ctx, f) => {
    const u = Math.min(1, Math.max(0, (f - nf) / 8)); if (u <= 0) return;
    ctx.save(); ctx.fillStyle = renkCoz(SARI); ctx.beginPath(); ctx.arc(nx, ny, 13 * u, 0, Math.PI * 2); ctx.fill(); ctx.restore();
  } });
  S.koy(S.nabiz(nx, ny, 13, 40.7));
  S.koy(S.elYazisi({ metin: "now", x: nx - 30, y: ny + 60, boy: 44, renk: SARI, tb: 40.85,
    sure: 0.45, ses: false }));                     // etiket, 40,85–41,30 sn
  const okY = yKutu + kh + 62;
  S.koy(S.darbeler(ok([nx, okY], [xs + 20, okY], 3), { w: 6, renk: SARI, uc0: 10, uc1: 14 }, 39.2, 0.2, 0.12, 0.5));
  // el yazısı, sözcük pencereleri (kaynak: "Ago, yani önce: zaman belli."): ago = →
  // Ago, 38,73–39,45 · yani 39,49–39,85 sn; önce → önce: 40,01–40,73 sn;
  // zaman belli → zaman 40,77 · belli. 41,13–41,93 sn
  const ago = S.koy(S.elYazisi({ metin: "ago =", x: xs + 120, y: okY + 70, boy: 56, renk: SARI,
    sozcukler: pencere("Ago,", 38.73, 2) }));
  S.koy(S.elYazisi({ metin: "önce", x: xs + 120 + ago.w + 17, y: okY + 70, boy: 56, renk: KREM,
    sozcukler: pencere("önce:", 40.01, 1) }));
  const zb = S.koy(S.elYazisi({ metin: "zaman belli", x: 660, y: okY + 70, boy: 56, renk: KREM,
    sozcukler: pencere("zaman", 40.77, 2) }));
  S.koy(S.darbeler([[[660 + zb.w + 24, okY + 50], [660 + zb.w + 38, okY + 66],
    [660 + zb.w + 66, okY + 28]]], { w: 7, renk: SARI, uc0: 5, uc1: 8, duz: true },
    41.13, 0.25, 0.3, 0.5));

  // 42,08–44,24 -ed (42,56) kırmızı çizgiyle yok; go (43,84) sarı daire — alt satır, taban y 930
  const R = 930, ed = olc(FF(90), "-ed");
  S.koy(S.metinPop({ parca: [["-ed", KREM]], x: 160, y: R, font: FF(90), tb: 42.56, sure: 0.3, ses: 0.5 }));
  S.koy(S.darbe([[140, R - 30], [160 + ed / 2, R - 34], [180 + ed, R - 28]], { w: 9, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 14, duz: true, tohum: 90 },
    42.9, 0.3, 0.6));
  const gx = 470, gw = olc(FF(90), "go");
  S.koy(S.metinPop({ parca: [["go", KREM]], x: gx, y: R, font: FF(90), tb: 43.84, sure: 0.3, ses: 0.5 }));
  S.koy(S.darbe(elips(gx + gw / 2, R - 30, gw / 2 + 24, 62, -0.05, 31), { w: 7, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, 44.0, 0.35, 0.55));

  // 45,51–46,71 go -> kalem oku -> went (Fredoka 110, sarı)
  S.koy(S.darbeler(ok([gx + gw + 40, R - 38], [gx + gw + 170, R - 38], 5), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, 45.51, 0.2, 0.12, 0.5));
  const wx = gx + gw + 200;
  S.koy(S.metinPop({ parca: [["went", SARI]], x: wx, y: R + 4, font: FF(110), tb: 46.71, sure: 0.35, ses: 0.8, turu: "vurus" }));

  // 47,59–48,39 ezberle + küçük kitap; go -> went kutuya alınır
  S.koy(S.elYazisi({ metin: "ezberle", x: 1170, y: R, boy: 64, renk: KREM, tb: 47.59,
    sure: 0.6 }));                                  // etiket, 47,59–48,19 sn
  S.koy(S.cizim({ svg: kitap, kutu: { x: 1390, y: 830, w: 150, h: 150 }, ad: "kitap", enCok: 8, w: 3.6, tb: 47.85, sure: 0.5, olayEnCok: 2, nefes: false }));
  S.koy(S.parilti(1545, 850, 48.3, 22));
  S.koy(S.darbeler(kutu(gx - 40, R - 105, wx + olc(FF(110), "went") - gx + 80, 150, 77), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 },
    47.65, 0.16, 0.1, 0.5));
}

surucu(kur, (f) => S.kare(f), KARE);

// SAHNE 04 (SIMPLE PAST İLERİ, DİKEY 1080x1920) — Örnek 2 (düz canvas, 487 kare, t_bas 33,15; cümle 4). Zaman yalnız kare numarasından.
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (sahne-ortak.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–672) · ORTA bölge M (690–950: used to grubu, sonra would grubu) · alt bölge B (950–1392):
// ev + yol + okul + yürüyen figür (430 px). Sahne 38,5'te 110 px aşağı iner; figür hiç küçülmez.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, yavasla, kis, olc } from "./sahne-ortak.js";

const KARE = 487, TBAS = 33.15, ICERIK = 475;
const KOKDIZ = "/projeler/simple-past-ileri-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, KIR = RT.kirmizi;

async function kur() {
  await S.kur();
  const [ev, okul, takvim, yuruyen] = await Promise.all([svgOku("tabler/home.svg"), svgOku("tabler/school.svg"),
    svgOku("tabler/calendar.svg"), svgOku("open-peeps/standing-4.svg")]);

  // 33,15: kart çerçevesi (el kutusu, 4 px). İlk 12 kare boş: künye hazır, tuval boş.
  S.koy(S.darbeler(kutu(48, 372, 984, 300, 4), { w: 4.2, renk: IKINCIL, uc0: 10, uc1: 18 }, 33.55, 0.2, 0.14, 0.55));

  // 34,36–37,80 İngilizce kök (Fredoka 64, sözcük zamanlı, 3 satır: 6 / 5 / 4 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("We", 34.36, 15), x: 88, y: 452, maxGen: 920, font: "700 64px Fredoka",
    satirH: 78, satirSay: [6, 5, 4], bosluk: 3 }));
  const kel = (i) => cum.kel[i];             // satır 1: 0 We … 5 a | satır 2: 6 village, … 10 walk | satır 3: 11 to … 14 morning.
  const sariKutu = (a, b, tb, tohum) => {
    const A = kel(a), B = kel(b), x = A.x - 10, w = B.x + B.w - A.x + 20;
    S.koy(S.darbeler(kutu(x, A.y - 54, w, 76, tohum), { w: 7, renk: SARI, alfa: 0.85, uc0: 8, uc1: 14 }, tb, 0.12, 0.09, 0.5));
  };
  sariKutu(1, 2, 34.52, 21);                 // used to
  sariKutu(9, 9, 36.12, 37);                 // would

  // 34,5–37,8 + 38,5: ev · yol · okul · yürüyen figür. Tek grup: 38,5–39,2'de 110 px aşağı iner (M bölgesi açılır).
  const IN = 110, sahne = [];
  sahne.push(S.cizim({ svg: ev, ad: "ev", kutu: { x: 48, y: 1060, w: 220, h: 220 }, enCok: 6, w: 4.4, tb: 34.5, sure: 0.8, olayEnCok: 4 }));
  sahne.push(S.cizim({ svg: okul, ad: "okul", kutu: { x: 812, y: 1060, w: 220, h: 220 }, enCok: 8, w: 4.4, tb: 34.95, sure: 0.8, olayEnCok: 4 }));
  sahne.push(S.darbe([[60, 1280], [300, 1274], [560, 1284], [820, 1276], [1020, 1282]], { w: 5, renk: IKINCIL, alfa: 0.9, uc0: 12, uc1: 18 }, 35.4, 0.9, 0.5));
  sahne.push(S.darbe([[90, 1262], [330, 1256], [590, 1264], [850, 1258], [1000, 1262]], { w: 5, renk: IKINCIL, alfa: 0.9, uc0: 12, uc1: 18 }, 35.7, 0.9, false));
  const yur = S.cizim({ svg: yuruyen, ad: "yuruyen", kutu: { x: 300, y: 850, w: 200, h: 430 }, esik: 0.004, enCok: 60, w: 4.4, tb: 35.9, sure: 1.1,
    olayEnCok: 6, nefes: false });
  {
    const f0 = S.fr(36.4), f1 = S.fr(37.8), cx = 400, cy = 1280;
    yur.donusum = (f) => { const u = kis((Math.min(f, ICERIK) - f0) / (f1 - f0)), g = Math.min(f, ICERIK) - f0;
      return { cx, cy, tx: 280 * yavasla(u), ty: g < 0 || u >= 1 ? 0 : -9 * Math.abs(Math.sin(g / 5)), dondur: 0, olcek: 1 }; };
  }
  sahne.push(yur);
  S.koy(S.grup(sahne, { f0: S.fr(38.5), f1: S.fr(39.2), ax: 540, ay: 0, olcek: 1, dy: IN }));

  // M bölgesi için kaydırma: öğeler 330 px yukarı kayar, 690–950 bandına kırpılır (yer açma)
  const kaydir = (liste, tb0, tb1) => ({ ciz: (ctx, f) => {
    const u = yavasla((Math.min(f, ICERIK) - S.fr(tb0)) / (S.fr(tb1) - S.fr(tb0)));
    ctx.save(); ctx.beginPath(); ctx.rect(0, 690, 1080, 260); ctx.clip(); ctx.translate(0, -330 * u);
    for (const e of liste) e.ciz(ctx, f);
    ctx.restore();
  } });

  // 39,01–41,73 used to = durum + alışkanlık; ok -> takvim, üstü çizili: artık yok  (M bölgesi, sol-orta-sağ)
  const F80 = "700 80px Fredoka", C64 = "700 64px Caveat";
  const p1 = [];
  p1.push(S.metinPop({ parca: [["used to", KREM]], x: 70, y: 840, font: F80, tb: 39.01, sure: 0.35, ses: 0.5 }));
  p1.push(...S.darbeler(ok([330, 812], [418, 774], 3), { w: 8, renk: SARI, uc0: 10, uc1: 14 }, 39.6, 0.16, 0.12, 0.5));
  // 39,81–40,21 «durumu» · 40,61–41,25 «alışkanlığı» (sözcük penceresi)
  p1.push(S.elYazisi({ metin: "durum", x: 440, y: 790, boy: 64, renk: SARI,
    sozcukler: S.dizi("durumu", 39.81, 1).map((w) => ({ t0: w.t0, t1: w.t1 })), ses: 0.4 }));
  p1.push(...S.darbeler(ok([330, 856], [418, 896], 5), { w: 8, renk: SARI, uc0: 10, uc1: 14 }, 40.7, 0.16, 0.12, 0.5));
  p1.push(S.elYazisi({ metin: "alışkanlık", x: 440, y: 925, boy: 64, renk: SARI,
    sozcukler: S.dizi("alışkanlığı", 40.61, 1).map((w) => ({ t0: w.t0, t1: w.t1 })), ses: 0.4 }));
  p1.push(...S.darbeler(ok([735, 900], [800, 860], 7), { w: 8, renk: SARI, uc0: 10, uc1: 14 }, 41.2, 0.16, 0.12, 0.5));
  p1.push(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 815, y: 705, w: 160, h: 160 }, enCok: 8, w: 4.4, tb: 41.3, sure: 0.4, olayEnCok: 3, nefes: false }));
  p1.push(S.darbe([[800, 880], [895, 790], [990, 700]], { duz: true, w: 9, renk: KREM, alfa: 0.9, uc0: 6, uc1: 10 }, 41.5, 0.2, 0.6));
  // 41,60 anlatımsız etiket `artık yok`: hedef 0,6 sn → 42,20 (kaydırma 42,2'de başlar)
  p1.push(S.elYazisi({ metin: "artık yok", x: 790, y: 940, boy: 64, renk: KREM, tb: 41.6, sure: 0.6,
    ses: 0.4 }));
  S.koy(kaydir(p1, 42.2, 42.7));

  // 42,44–47,72 would yalnız tekrarlanan eylem: would + walk ✓ (45,44–46,04), would + live ✗ (46,92–47,72)
  S.koy(S.metinPop({ parca: [["would", SARI]], x: 70, y: 770, font: F80, tb: 42.44, sure: 0.35, ses: 0.5 }));
  // 43,64–44,60 «tekrarlanan eylemde»: `=` sözcüksüz, tek pencere (0,96 sn); sağ uç 778
  S.koy(S.elYazisi({ metin: "= tekrarlanan eylem", x: 330, y: 770, boy: 64, renk: KREM, tb: 43.64,
    sure: 0.96, ses: 0.4 }));
  const F64 = "700 64px Fredoka", g1 = olc(F64, "would + walk"), g2 = olc(F64, "would + live");
  S.koy(S.darbeler(kutu(48, 805, g1 + 104, 92, 41), { w: 4.2, renk: KREM, uc0: 8, uc1: 14 }, 45.44, 0.12, 0.09, 0.45));
  S.koy(S.metinPop({ parca: [["would + walk", KREM]], x: 70, y: 872, font: F64, tb: 45.5, sure: 0.3, ses: 0.5 }));
  S.koy(S.darbe([[48 + g1 + 22, 852], [48 + g1 + 38, 876], [48 + g1 + 68, 822]], { w: 10, renk: SARI, alfa: 0.95, uc0: 5, uc1: 8 }, 46.04, 0.2, 0.6));
  const x2 = 556;
  S.koy(S.darbeler(kutu(x2, 805, g2 + 104, 92, 43), { w: 4.2, renk: KREM, uc0: 8, uc1: 14 }, 46.92, 0.12, 0.09, 0.45));
  S.koy(S.metinPop({ parca: [["would + live", KREM]], x: x2 + 22, y: 872, font: F64, tb: 46.98, sure: 0.3, ses: 0.5 }));
  S.koy(S.darbe([[x2 + g2 + 32, 826], [x2 + g2 + 76, 878]], { duz: true, w: 10, renk: KIR, alfa: 0.95, uc0: 5, uc1: 8 }, 47.2, 0.14, 0.7));
  S.koy(S.darbe([[x2 + g2 + 76, 826], [x2 + g2 + 32, 878]], { duz: true, w: 10, renk: KIR, alfa: 0.95, uc0: 5, uc1: 8 }, 47.34, 0.14, false));
  // 47,45 anlatımsız etiket `durum fiili`: hedef 0,6 sn → 48,05
  S.koy(S.elYazisi({ metin: "durum fiili", x: 70, y: 945, boy: 64, renk: KREM, tb: 47.45, sure: 0.6,
    ses: 0.4 }));
  S.koy(S.darbeler(ok([390, 925], [470, 925], 9), { w: 8, renk: SARI, uc0: 10, uc1: 14 }, 47.55, 0.12, 0.1, false));
  // 47,70 anlatımsız etiket `used to` (sarı): hedef 0,5 sn → 48,20
  S.koy(S.elYazisi({ metin: "used to", x: 500, y: 945, boy: 64, renk: SARI, tb: 47.7, sure: 0.5,
    ses: 0.4 }));
  S.koy(S.parilti(960, 930, 47.9, 28));
}

surucu(kur, (f) => S.kare(f), KARE);

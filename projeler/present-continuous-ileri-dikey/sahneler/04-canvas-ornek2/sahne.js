// SAHNE 04 (İLERİ, DİKEY 1080x1920) — Örnek 2 (düz canvas, 387 kare, t_bas 29,58; cümle 4). Zaman yalnız kare numarasından.
// Bantlar: içerik 352–1392 dolu, altyazı 1400–1536 (sahne-ortak.js çizer), platform boş. Telefon ölçeği: yazı ≥ 64 px.
// Üstten alta: kart (372–708) · TR 2 satır (740–850) · sahne 860–1290 (38,5'te 0,42'ye toplanır) · geçici notu + takvim şeridi
// (1040–1170) · formül (1182–1380).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, yavasla } from "./sahne-ortak.js";

const KARE = 387, TBAS = 29.58, ICERIK = 375;
const KOKDIZ = "/projeler/present-continuous-ileri-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;

async function kur() {
  await S.kur();
  const [ev, damla, kiz] = await Promise.all([svgOku("tabler/home.svg"), svgOku("coco/rain.svg"), svgOku("open-peeps/sitting-7.svg")]);

  // 30,13: kart çerçevesi (el kutusu, 4 px). İlk 12 kare boş: künye hazır, tuval boş.
  S.koy(S.darbeler(kutu(48, 372, 984, 290, 4), { w: 4.2, renk: IKINCIL, uc0: 10, uc1: 18 }, 30.13, 0.2, 0.14, 0.55));

  // 31,34–35,50 İngilizce kök (Fredoka 64, sözcük zamanlı, 3 satır: 5 / 6 / 3 sözcük)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Because", 31.34, 14), x: 88, y: 452, maxGen: 904, font: "700 64px Fredoka",
    satirH: 78, satirSay: [5, 6, 3], bosluk: 4 }));
  const kel = (i) => cum.kel[i];             // satır 1: 0 Because … 4 leaking, | satır 2: 5 we … 10 uncle's | satır 3: 11 house 12 this 13 week.
  const cevre = (a, b, tb, egim, tohum) => {                       // iki sözcüğe tek sarı daire
    const A = kel(a), B = kel(b);
    S.koy(S.darbe(elips((A.x + B.x + B.w) / 2, A.y - 24, (B.x + B.w - A.x) / 2 + 6, 48, egim, tohum),
      { w: 9, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, tb, 0.4, 0.55));
  };
  cevre(3, 4, 32.14, -0.03, 11);                                   // is leaking,
  cevre(6, 7, 33.02, -0.03, 13);                                   // are staying
  {                                                                // this week: sarı köşeli ayraç (34,38–34,70)
    const A = kel(12), B = kel(13), y = A.y + 30;
    S.koy(S.darbe([[A.x - 4, y - 10], [A.x - 4, y + 8], [B.x + B.w + 4, y + 8], [B.x + B.w + 4, y - 10]],
      { duz: true, w: 9, renk: SARI, alfa: 0.85, uc0: 12, uc1: 24 }, 34.38, 0.4, 0.6));
  }

  // 31,3–35,0 ORTA sahne (830–1240): büyük ev + 3 damla, ok, küçük ev (uncle's), figür. Tek grup: 38,5'te toplanır.
  const sahne = [];
  sahne.push(S.cizim({ svg: ev, ad: "ev", kutu: { x: 60, y: 830, w: 400, h: 400 }, enCok: 6, w: 4.4, tb: 31.4, sure: 0.9, olayEnCok: 4 }));
  [[140, 960, 31.95], [250, 1020, 32.4], [350, 960, 32.85]].forEach(([x, y, tb], i) => {
    const g = S.cizim({ svg: damla, ad: "damla", kutu: { x, y, w: 58, h: 116 }, enCok: 6, esik: 0.004, w: 4, tb, sure: 0.35, olayEnCok: 1, nefes: false });
    g.donusum = (f) => ({ cx: x, cy: y, tx: 0, ty: f < S.fr(tb + 0.35) ? 0 : 8 * Math.sin((Math.min(f, ICERIK) - S.fr(tb + 0.35)) / 9 + i * 2), dondur: 0, olcek: 1 });
    sahne.push(g);
  });
  sahne.push(...S.darbeler(ok([480, 1040], [560, 1020], 3), { w: 9, renk: SARI, uc0: 10, uc1: 14 }, 33.3, 0.16, 0.12, 0.5));
  sahne.push(S.cizim({ svg: ev, ad: "kucuk-ev", kutu: { x: 575, y: 910, w: 230, h: 230 }, enCok: 6, w: 4.4, tb: 33.5, sure: 0.7, olayEnCok: 3 }));
  const TOP = { f0: S.fr(38.5), f1: S.fr(39.2), ax: 540, ay: 830, olcek: 0.42, dy: 0 };
  const etiket = S.metinPop({ parca: [["uncle's", SARI]], x: 690, y: 890, font: "700 64px Caveat", hiza: "orta", tb: 33.82, sure: 0.35, ses: 0.5 });
  S.koy({ ciz: (ctx, f) => {                                         // yazı küçülmez (≥ 64 px): toplanan evin üstüne taşınır, 48 px sola kayar (figürün saçına değmesin)
    const u = yavasla((Math.min(f, ICERIK) - TOP.f0) / (TOP.f1 - TOP.f0)), k = 1 + (TOP.olcek - 1) * u;
    ctx.save(); ctx.translate((TOP.ax + (690 - TOP.ax) * k) - 690 - 48 * u, (TOP.ay + (890 - TOP.ay) * k) - 890); etiket.ciz(ctx, f); ctx.restore();
  } });
  sahne.push(S.cizim({ svg: kiz, ad: "kiz", kutu: { x: 810, y: 830, w: 220, h: 410 }, esik: 0.004, enCok: 60, w: 4.4, tb: 34.0, sure: 1.3, olayEnCok: 6 }));
  S.koy(S.grup(sahne, TOP));

  // 35,75–38,87 Türkçe çeviri (Caveat 64 mürekkep, 2 satır)
  const tz = [["Çatı aktığı için bu hafta", 35.75, 722], ["amcamlarda kalıyoruz.", 37.43, 788]];
  tz.forEach(([m, tb, y]) => S.koy(S.not({ parca: [[m, KREM]], x: 88, y, font: "700 64px Caveat", tb, sure: tb === 35.75 ? 1.5 : 0.9 })));

  // 38,87–40,27 geçici durum: not "geçici -> this week" + 7 günlük takvim şeridi
  {
    const gun = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], kw = 124, ad = 140, x0 = 58, ky = 1090, kh = 58;
    S.koy(S.not({ parca: [["geçici", SARI]], x: 88, y: 1062, font: "700 64px Caveat", tb: 38.87, sure: 0.45, ses: 0.5 }));
    S.koy(S.darbeler(ok([300, 1042], [380, 1042], 3), { w: 8, renk: SARI, uc0: 10, uc1: 14 }, 39.3, 0.16, 0.12, 0.5));
    S.koy(S.metinPop({ parca: [["this week", SARI]], x: 410, y: 1062, font: "700 64px Caveat", tb: 39.5, sure: 0.35, ses: 0.5 }));
    gun.forEach((g, i) => {
      S.koy(S.darbeler(kutu(x0 + ad * i, ky, kw, kh, 30 + i), { w: 3.6, renk: KREM, uc0: 8, uc1: 14 }, 39.1 + i * 0.07, 0.1, 0.07, i === 0 ? 0.45 : false));
    });
  }

  // 40,27–42,07 This week bunu söyler: this week sarı daire; formül is leak-ing / are stay-ing (Fredoka 108, -ing sarı)
  cevre(12, 13, 40.47, -0.03, 17);
  S.koy(S.metinPop({ parca: [["is leak", KREM], ["-ing", SARI]], x: 88, y: 1268, font: "700 108px Fredoka", tb: 41.0, sure: 0.35, ses: 0.5 }));
  S.koy(S.metinPop({ parca: [["are stay", KREM], ["-ing", SARI]], x: 88, y: 1370, font: "700 108px Fredoka", tb: 41.4, sure: 0.35, ses: 0.5 }));
  S.koy(S.parilti(960, 1230, 41.6, 30));
}

surucu(kur, (f) => S.kare(f), KARE);

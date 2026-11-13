// SAHNE 04 — Gelecek ayrımı (düz canvas, 1053 kare, t_bas 48,59; cümle 4–6). Kendini çizen kalem;
// zaman yalnız kare numarasından, sözcük zamanları sozcukler.json'dan.
// Akış: tek cümle kartı (iki fiil sarı halka) · zaman çizgisi 9 → 11 · Türkçe çeviri · öğrenci balonu
// (soru anı 1) · fark tablosu (ARRANGEMENT ↔ TIMETABLE) · öğrenci baş sallar.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, elips, ok, kutu, altCizgi, olc, kis, lerp, yavasla } from "./sahne-ortak.js";

const KARE = 1053, TBAS = 48.59, ICERIK = 1041;
const KOKDIZ = "/projeler/02-03-ydt-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Future pair", etkin: 1,
  cumle: [4, 5, 6] });
window.__S = S;                                   // önizleme ölçümü (olaylar.json)
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, ZEMIN = "@zemin";
// Faz A öğeleri (zaman çizgisi, çeviri, balon): 65,00–65,40 arasında söner, tablo için yer açar.
const koyG = (e) => S.koy(Array.isArray(e) ? e.map((x) => solar(x, 65.0, 65.4)) : solar(e, 65.0, 65.4));
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

// Öğeyi [t0, t1] sn arasında söndürür; söndükten sonra hiç çizilmez (kutu da bildirmez).
const solar = (e, t0, t1) => ({ ...e, ciz: (ctx, f) => {
  const a = 1 - kis((S.zm(f) - t0) / (t1 - t0));
  if (a <= 0.02) return;
  ctx.save(); ctx.globalAlpha = a; e.ciz(ctx, f); ctx.restore();
} });

// Dolu sarı daire + içinde sayı (soru-ani sahne bağı: balon ↔ cümle). Pop ile belirir.
function numNokta(cx, cy, sayi, tb) {
  const fb = S.fr(tb);
  S.bas(fb); S.olay(fb, "tik", 0.6);
  return { ciz: (ctx, f) => {
    const u = yavasla((f - fb) / 8); if (u <= 0) return;
    ctx.save(); ctx.translate(cx, cy); ctx.scale(lerp(0.6, 1, u), lerp(0.6, 1, u)); ctx.globalAlpha = u;
    ctx.fillStyle = renkCoz(RT.vurgu);
    ctx.beginPath(); ctx.arc(0, 0, 22, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = renkCoz(ZEMIN); ctx.font = "700 30px Fredoka"; ctx.textAlign = "center";
    ctx.textBaseline = "alphabetic"; ctx.fillText(String(sayi), 0, 11); ctx.restore();
    if (u >= 0.2) window.__kalemKutu?.ekle("isaret", "nokta" + sayi, cx - 22, cy - 22, 44, 44);
  } };
}

// Konuşma balonu: yuvarlak köşeli çerçeve + sağ kenarda kuyruk (nokta dizisi, düz darbe).
function balonYol(x0, y0, x1, y1, r, kuyruk) {
  const arc = (cx, cy, a0, a1) => Array.from({ length: 7 }, (_, i) => {
    const a = a0 + (a1 - a0) * i / 6; return [cx + r * Math.cos(a), cy + r * Math.sin(a)];
  });
  const [tx, ty] = kuyruk, orta = (y0 + y1) / 2;
  return [...arc(x0 + r, y0 + r, Math.PI, 1.5 * Math.PI), ...arc(x1 - r, y0 + r, 1.5 * Math.PI, 2 * Math.PI),
    [x1, orta - 24], [tx, ty], [x1, orta + 18], ...arc(x1 - r, y1 - r, 0, 0.5 * Math.PI),
    ...arc(x0 + r, y1 - r, 0.5 * Math.PI, Math.PI), [x0, y0 + r]].concat([[x0 + r * 0.2, y0 + r * 0.5]]);
}

async function kur() {
  await S.kur();
  const [ayak, ucak, saat, bas] = await Promise.all([svgOku("open-peeps/standing-4.svg"),
    svgOku("tabler/plane.svg"), svgOku("tabler/clock.svg"), svgOku("peeps-kit/ogrenci-bas.svg")]);

  // 49,51 "İki gelecek kalıbı": daire içinde 2 (ilk 28 kare boş; künye hazır)
  S.koy(S.daireSayi(2, 200, 190, 49.55));

  // 51,12–55,20 İngilizce cümle (Fredoka 60, 2 satır: 8 + 7 sözcük); ekran metni rakamla (9, 11)
  const say = { "nine,": "9,", "eleven.": "11." };
  const soz = S.dizi("We", 51.12, 15).map((w) => ({ ...w, sozcuk: say[w.sozcuk] || w.sozcuk }));
  const cum = S.koy(S.cumleYaz({ sozcukler: soz, x: 140, y: 330, maxGen: 1500, font: "700 60px Fredoka",
    satirH: 90, satirSay: [8, 7], bosluk: 4 }));
  const kel = cum.kel;
  // iki fiil: her biri öbeğin SON sözcüğü yazıldıktan sonra el altçizgisiyle (vurgu rengi); dar sözcük
  // aralığında halka harfleri kesiyordu (13.11 QA)
  const cevre = (a, b, tohum) => {
    const A = kel[a], B = kel[b], tb = B.t0 + 0.3;
    const dar = S.darbe(altCizgi(A.x - 4, B.x + B.w + 4, A.y + 16, tohum), { w: 7.5, renk: SARI, alfa: 0.9,
      uc0: 8, uc1: 14 }, tb, 0.4, 0.55);
    S.koy(dar); return { cx: (A.x + B.x + B.w) / 2, ust: A.y - 22 - 44, alt: A.y - 22 + 44 };
  };
  const h1 = cevre(1, 2, 21), h2 = cevre(11, 12, 23);

  // 52,48–54,30 zaman çizgisi: 9 → 11 (çizgi, iki nokta, etiketler)
  {
    const Y = 600, X9 = 300, X11 = 780;
    koyG(S.darbe([[160, Y], [X9 - 18, Y]], { duz: true, w: 5, renk: KREM, uc0: 6, uc1: 8 }, 52.3, 0.22, 0.4));
    koyG(S.darbe(elips(X9, Y, 17, 17, 0.1, 31), { w: 5, renk: SARI, alfa: 0.9, uc0: 6, uc1: 10 }, 52.48,
      0.3, 0.6));
    koyG(S.metinPop({ parca: [["9", KREM]], x: X9, y: Y + 88, font: "700 64px Fredoka", hiza: "orta",
      tb: 52.55, sure: 0.25, olcek0: 0.7, ses: 0.5, turu: "tik" }));
    koyG(S.darbe([[X9 + 18, Y], [X11 - 18, Y]], { duz: true, w: 5, renk: KREM, uc0: 6, uc1: 12 }, 53.86,
      0.4, 0.5));
    koyG(S.darbe(elips(X11, Y, 17, 17, 0.1, 33), { w: 5, renk: SARI, alfa: 0.9, uc0: 6, uc1: 10 }, 54.24,
      0.3, 0.6));
    koyG(S.metinPop({ parca: [["11", KREM]], x: X11, y: Y + 88, font: "700 64px Fredoka", hiza: "orta",
      tb: 54.3, sure: 0.25, olcek0: 0.7, ses: 0.5, turu: "tik" }));
    koyG(S.darbeler(ok([X11 + 22, Y], [880, Y], 5), { w: 5, renk: KREM, uc0: 8, uc1: 10 }, 54.55, 0.2, 0.1,
      false));
  }

  // 55,45–59,21 Türkçe çeviri (Caveat 52, iki satır; her sözcük kendi konuşma penceresinde)
  koyG(S.elYazisi({ metin: "Dokuzda havalimanına çıkıyoruz,", x: 140, y: 800, boy: 52, renk: IKINCIL,
    sozcukler: pen("Dokuzda", 55.45, 3) }));
  koyG(S.elYazisi({ metin: "uçağımız on birde kalkıyor.", x: 140, y: 860, boy: 52, renk: IKINCIL,
    sozcukler: pen("uçağımız", 57.45, 4) }));

  // 59,76–64,32 SORU ANI 1: öğrenci başı + el çizimi balon, sözcük sözcük (Fredoka 600 44)
  const BF = "600 42px Fredoka", sp = olc(BF, " ");
  // ekran metni (taslak §4 satır 5): «Hocam,» yalnız seste; balonda 9 sözcük
  const sw = S.dizi("ikisi", 60.48, 9).map((w, i) => (i === 0 ? { ...w, sozcuk: "İkisi" } : w));
  const satir = [[0, 1, 2], [3, 4, 5, 6, 7, 8]];
  const gen = satir.map((s) => s.reduce((t, i) => t + olc(BF, sw[i].sozcuk), 0) + sp * (s.length - 1));
  const BX1 = 1650, BX0 = BX1 - Math.max(...gen) - 70, BY0 = 520, BASE = [BY0 + 64, BY0 + 130];
  const gb = S.cizim({ svg: bas, ad: "ogrenci", kutu: { x: 1690, y: 470, w: 150, h: 206 }, esik: 0.004,
    enCok: 60, w: 3.2, tb: 59.9, sure: 0.55, olayEnCok: 3, nefes: false });
  const hx = 1765, hy = 676;                                         // boyun tabanı: baş sallama ekseni
  S.koy(gb);
  const balon = [];
  balon.push(S.darbe(balonYol(BX0, BY0, BX1, BASE[1] + 80, 34, [1684, BY0 + 105]), { duz: true, w: 4.4,
    uc0: 12, uc1: 20 }, 60.1, 0.6, 0.6));
  satir.forEach((s, si) => {
    let x = BX0 + 35;
    s.forEach((i) => {
      balon.push(S.metinPop({ parca: [[sw[i].sozcuk, KREM]], x, y: BASE[si], font: BF, tb: sw[i].t0,
        sure: 0.2, olcek0: 0.9, ses: i === 0 || i === 3 ? 0.5 : false, turu: "tik" }));
      sw[i].x = x; sw[i].w = olc(BF, sw[i].sozcuk); x += sw[i].w + sp;
    });
  });
  // sahne bağı: numaralı sarı nokta, balondaki sözcük ↔ cümledeki fiil (1: -ing ↔ are leaving)
  const n1x = sw[5].x + sw[5].w / 2, n2x = (sw[7].x + sw[8].x + sw[8].w) / 2, ny = BASE[1] + 40;
  balon.push(numNokta(n1x, ny, 1, sw[5].t0), numNokta(n2x, ny, 2, sw[7].t0));
  koyG(numNokta(h1.cx, h1.ust - 26, 1, sw[5].t0 + 0.02));
  koyG(numNokta(h2.cx, h2.alt + 26, 2, sw[7].t0 + 0.02));
  koyG(balon);

  // 64,99–83,28 fark tablosu (sütun 1: ARRANGEMENT · sütun 2: TIMETABLE)
  const FO = "700 56px Fredoka";
  // sütun 1: We figürü + bavul (66,20–68,00)
  S.koy(S.cizim({ svg: ayak, ad: "we-figur", kutu: { x: 150, y: 470, w: 230, h: 320 }, esik: 0.004,
    enCok: 60, w: 3.2, tb: 66.2, sure: 1.3, olayEnCok: 6 }));
  {
    const bx = 440, by = 620, bw = 200, bh = 150, t = 67.2;
    kutu(bx, by, bw, bh, 51).forEach((p, i) => S.koy(S.darbe(p, { duz: true, w: 5, uc0: 8, uc1: 10 },
      t + i * 0.09, 0.14, i === 0 ? 0.5 : false)));
    S.koy(S.darbe([[bx + 55, by], [bx + 55, by - 38], [bx + bw - 55, by - 38], [bx + bw - 55, by]],
      { duz: true, w: 5, uc0: 8, uc1: 10 }, t + 0.4, 0.28, 0.5));
    S.koy(S.darbe([[bx + 50, by + 8], [bx + 50, by + bh - 8]], { duz: true, w: 3.4, renk: IKINCIL, uc0: 6,
      uc1: 8 }, t + 0.55, 0.15, false));
    S.koy(S.darbe([[bx + bw - 50, by + 8], [bx + bw - 50, by + bh - 8]], { duz: true, w: 3.4, renk: IKINCIL,
      uc0: 6, uc1: 8 }, t + 0.62, 0.15, false));
    S.koy(S.darbe(elips(bx + 40, by + bh + 14, 10, 10, 0, 61), { w: 4, uc0: 6, uc1: 8 }, t + 0.7, 0.18, false));
    S.koy(S.darbe(elips(bx + bw - 40, by + bh + 14, 10, 10, 0, 62), { w: 4, uc0: 6, uc1: 8 }, t + 0.75, 0.18,
      false));
  }
  const e1 = S.metinPop({ parca: [["ARRANGEMENT", KREM]], x: 150, y: 880, font: FO, tb: 68.13, sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" });
  const e2 = S.metinPop({ parca: [["→  ", IKINCIL], ["V-ing", SARI]], x: 150, y: 955, font: FO, tb: 69.41,
    sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" });
  S.koy([e1, e2]);
  // sütun 2: uçak + saat (71,02–73,00)
  S.koy(S.cizim({ svg: ucak, ad: "ucak", kutu: { x: 1000, y: 500, w: 300, h: 300 }, esik: 0.004, enCok: 8,
    w: 5, tb: 71.02, sure: 0.95, olayEnCok: 4, nefes: false }));
  S.koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 1350, y: 520, w: 230, h: 230 }, esik: 0.004, enCok: 8,
    w: 5, tb: 72.1, sure: 0.8, olayEnCok: 3, nefes: false }));
  const e3 = S.metinPop({ parca: [["TIMETABLE", KREM]], x: 1000, y: 880, font: FO, tb: 73.27, sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" });
  const e4 = S.metinPop({ parca: [["→  ", IKINCIL], ["V1 / V-s", SARI]], x: 1000, y: 955, font: FO, tb: 74.63,
    sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" });
  S.koy([e3, e4]);
  // 76,24 "Both mean the future": iki sütun arasında eşittir işareti
  S.koy(S.darbe([[770, 650], [870, 646]], { duz: true, w: 7, renk: SARI, alfa: 0.9, uc0: 8, uc1: 12 }, 76.26,
    0.22, 0.6));
  S.koy(S.darbe([[770, 700], [870, 696]], { duz: true, w: 7, renk: SARI, alfa: 0.9, uc0: 8, uc1: 12 }, 76.52,
    0.22, false));
  // 80,32 arrangement · 82,32 timetable: iki etiketin çevresine sarı halka
  const sar = (m, tb, tohum) => S.koy(S.darbe(elips(m.x + m.w / 2, 880 - 20, m.w / 2 + 14, 36, -0.03, tohum),
    { w: 6, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, tb, 0.45, 0.55));
  sar(e1, 80.32, 41); sar(e3, 82.3, 43);
  // 82,35–83,25 öğrenci onaylar: baş iki kez sallanır (1 sn)
  const f0 = S.fr(82.25), f1 = S.fr(83.25);
  gb.donusum = (f) => {
    const u = kis((f - f0) / (f1 - f0)), e = u <= 0 || u >= 1 ? 0 : Math.abs(Math.sin(u * Math.PI * 2));
    return { cx: hx, cy: hy, tx: 0, ty: 12 * e, dondur: 0.06 * e, olcek: 1 };
  };
  S.olay(f0, "tik", 0.4); S.olay(S.fr(82.75), "tik", 0.4);
}

surucu(kur, (f) => S.kare(f), KARE);

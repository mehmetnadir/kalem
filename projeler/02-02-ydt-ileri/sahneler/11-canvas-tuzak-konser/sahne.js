// SAHNE 11 — Tuzak konser (düz canvas, 913 kare, t_bas 259,61; cümle 38–42). Kendini çizen kalem;
// zaman yalnız kare numarasından, sözcük zamanları sozcukler.json'dan (T() ile okunur, elle yazılmaz).
// Akış: perde (kırmızı ünlem, gelecek oku) · kart büyür (begins ve ends sarı daire; saat + takvim) · TR çeviri ·
// öğrenci balonu (soru anı 1; sarı nokta begins) · yakın çekim «The concert» (kalan soluk) · tarife tablosu ·
// «resmî program / tarife → geniş zaman» · kart küçülür, ikinci kart için yer açılır.
// Kırmızı yalnız perdedeki ünlemde (tuzak işareti). Doğru/yanlış işareti bu sahnede yok.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, elips, ok, kutu, altCizgi, olc, kis, lerp, yavasla } from "./sahne-ortak.js";

const KARE = 913, TBAS = 259.99, ICERIK = 901;
const KOKDIZ = "/projeler/02-02-ydt-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Trap", etkin: 2,
  cumle: [38, 39, 40, 41, 42] });
window.__S = S;                                   // önizleme ölçümü (olaylar.json)
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu, SARI_D = RT.vurguDolgu, KIRMIZI = RT.kirmizi;
const ZEMIN = "@zemin";
const F56 = "700 56px Fredoka", F64 = "700 64px Fredoka";

// Anlatım sözcüğünün t0'ı (küresel sn); bulunamazsa sahne hiç yüklenmez (sessiz yanlış zaman olmaz).
const T = (ad, yakin) => {
  const r = S.dizi(ad, yakin, 1);
  if (!r.length || r[0].sozcuk !== ad) throw new Error("sözcük yok: " + ad + " @" + yakin);
  return r[0].t0;
};
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

// Öğeyi [t0, t1] sn arasında gerçekten söndürür: öğe kendi globalAlpha değerini mutlak yazdığı için
// (darbeCiz, metinPop) örnek üstünde globalAlpha yazımı fade çarpanıyla çarpılır; söndükten sonra çizilmez.
const ALFA = (typeof CanvasRenderingContext2D !== "undefined")
  ? Object.getOwnPropertyDescriptor(CanvasRenderingContext2D.prototype, "globalAlpha") : null;
function sondur(e, t0, t1) {
  if (Array.isArray(e)) return e.map((x) => sondur(x, t0, t1));
  return { ...e, ciz: (ctx, f) => {
    const m = 1 - kis((S.zm(f) - t0) / (t1 - t0));
    if (m <= 0.01) return;
    if (m >= 0.999 || !ALFA) { e.ciz(ctx, f); return; }
    let v = 1;
    Object.defineProperty(ctx, "globalAlpha", { configurable: true, get: () => v,
      set: (x) => { v = x; ALFA.set.call(ctx, x * m); } });
    ALFA.set.call(ctx, m);
    try { e.ciz(ctx, f); } finally { delete ctx.globalAlpha; ALFA.set.call(ctx, 1); }
  } };
}
// Öğe grupları: her grup kendi sönme anında kalkar. koy(e, g): g = "P" | "A" | "B" | yok (kalıcı).
const SON = { P: [263.28, 263.58], A: [273.53, 273.83], B: [278.18, 278.46] };
const koy = (e, g) => S.koy(g ? sondur(e, SON[g][0], SON[g][1]) : e);

// Kart grubu dönüşümü: «yaklas» (0,94 → 1, 263,22'den) ve sahne sonunda küçülme (1 → 0,56, sol üst köşeye).
const OR1 = [960, 285], OR2 = [110, 150];
const kartDon = (f) => {
  const t = S.zm(f);
  return [lerp(0.94, 1, yavasla((t - 263.60) / 0.55)), lerp(1, 0.56, yavasla((t - 288.93) / 0.7))];
};
function donustur(e, fn) {
  if (Array.isArray(e)) return e.map((x) => donustur(x, fn));
  return { ...e, ciz: (ctx, f) => {
    const [s1, s2] = fn(f);
    if (s1 === 1 && s2 === 1) { e.ciz(ctx, f); return; }
    ctx.save();
    ctx.translate(OR2[0], OR2[1]); ctx.scale(s2, s2); ctx.translate(-OR2[0], -OR2[1]);
    ctx.translate(OR1[0], OR1[1]); ctx.scale(s1, s1); ctx.translate(-OR1[0], -OR1[1]);
    e.ciz(ctx, f); ctx.restore();
  } };
}
const kart = (e) => S.koy(donustur(e, kartDon));

// Sarı dolu nokta (soru-ani sahne bağı: balon ↔ cümle). Pop ile belirir.
function nokta(cx, cy, tb) {
  const fb = S.fr(tb);
  S.bas(fb); S.olay(fb, "tik", 0.6);
  return { ciz: (ctx, f) => {
    const u = yavasla((f - fb) / 8); if (u <= 0) return;
    ctx.save(); ctx.translate(cx, cy); ctx.scale(lerp(0.6, 1, u), lerp(0.6, 1, u)); ctx.globalAlpha = u;
    ctx.fillStyle = renkCoz(SARI);
    ctx.beginPath(); ctx.arc(0, 0, 16, 0, Math.PI * 2); ctx.fill(); ctx.restore();
    if (u >= 0.2) window.__kalemKutu?.ekle("isaret", "nokta", cx - 16, cy - 16, 32, 32);
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
  const [saat, takvim, bas] = await Promise.all([svgOku("tabler/clock.svg"), svgOku("tabler/calendar.svg"),
    svgOku("peeps-kit/ogrenci-bas.svg")]);

  // ---------------- 38 «Şimdi tuzak. Gelecek anlamı var.» (260,16–263,12): perde ----------------
  // 260,80 «tuzak»: kırmızı ünlem (gövde + nokta); 261,76 «Gelecek»: sağa ok (gelecek yönü)
  koy(S.darbe([[960, 300], [957, 520], [963, 680]], { w: 26, renk: KIRMIZI, alfa: 0.95, uc0: 10, uc1: 14 },
    T("tuzak.", 261.18), 0.45, 0.7), "P");
  koy(S.darbe(elips(960, 770, 17, 17, 0.1, 51), { w: 14, renk: KIRMIZI, alfa: 0.95, uc0: 6, uc1: 8 },
    T("tuzak.", 261.18) + 0.4, 0.3, 0.6), "P");
  koy(S.darbeler(ok([1090, 520], [1480, 520], 7), { w: 9, renk: KREM, uc0: 10, uc1: 14 }, T("Gelecek", 262.14),
    0.3, 0.12, 0.55), "P");

  // ---------------- 39 (263,59–268,23) kart büyür: İngilizce cümle, 2 satır ----------------
  // kart çerçevesi 263,25'ten (cümleden 0,34 sn önce); ekran metni rakamla (8, 11)
  kart(S.darbeler(kutu(110, 150, 1700, 270, 61), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, 263.63, 0.14, 0.1,
    0.55));
  const say = { "eight": "8", "eleven.": "11." };
  const soz = S.dizi("The", 263.97, 13).map((w) => ({ ...w, sozcuk: say[w.sozcuk] || w.sozcuk }));
  const cum = S.cumleYaz({ sozcukler: soz, x: 150, y: 268, maxGen: 1600, font: "700 60px Fredoka", satirH: 90,
    satirSay: [8, 5], bosluk: 4 });
  kart(cum);
  const kel = cum.kel;                            // 0 The 1 concert 2 begins 3 at 4 8 5 o'clock 6 tomorrow 7 evening | 8 and 9 ends …
  // begins (264,23) ve ends (266,79): sarı daire, kartta kalıcı
  // QA 13.11 halka kuralı: komşu sözcüğe değen halka yerine el altçizgisi (sözcük göründükten sonra)
  const daire = (k, tb, tohum) => kart(S.darbe(altCizgi(k.x - 4, k.x + k.w + 4, k.y + 15, tohum),
    { w: 6, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 12 }, tb + 0.2, 0.45, 0.55));
  daire(kel[2], T("begins", 264.61), 71);
  daire(kel[9], T("ends", 267.17), 72);
  // saat (264,87 «eight») ve takvim (265,35 «tomorrow»): kalemle, sol alt
  koy(S.cizim({ svg: saat, ad: "saat", kutu: { x: 160, y: 520, w: 200, h: 200 }, esik: 0.004, enCok: 8, w: 5,
    tb: T("eight", 265.25), sure: 0.8, olayEnCok: 3, nefes: false }), "A");
  koy(S.cizim({ svg: takvim, ad: "takvim", kutu: { x: 420, y: 520, w: 200, h: 200 }, esik: 0.004, enCok: 8,
    w: 5, tb: T("tomorrow", 265.73), sure: 0.8, olayEnCok: 3, nefes: false }), "A");

  // ---------------- 40 (268,70–273,18) TR çeviri (Caveat 54, iki satır) + başlayacak altı çizgi ----------------
  const CB = 54, CF = "700 54px Caveat";
  const tr1 = S.elYazisi({ metin: "Konser yarın akşam saat sekizde başlayacak", x: 700, y: 580, boy: CB,
    renk: IKINCIL, sozcukler: pen("Konser", 269.08, 6) });
  const tr2 = S.elYazisi({ metin: "ve on bir civarı bitecek.", x: 700, y: 655, boy: CB, renk: IKINCIL,
    sozcukler: pen("ve", 271.80, 5) });
  koy([tr1, tr2], "A");
  {
    const bas1 = "Konser yarın akşam saat sekizde ", tum = "Konser yarın akşam saat sekizde başlayacak";
    const oran = tr1.w / olc(CF, tum), x0 = 700 + olc(CF, bas1) * oran, x1 = 700 + tr1.w;
    koy(S.darbe(altCizgi(x0 - 4, x1 + 4, 580 + 16, 93), { w: 8.5, renk: SARI_D, alfa: 0.85, uc0: 8, uc1: 14 },
      T("başlayacak", 271.08) + 0.12, 0.35, 0.5), "A");
  }

  // ---------------- 41 (273,65–277,43) SORU ANI 1: öğrenci başı + el çizimi balon ----------------
  const BF = "600 44px Fredoka", sp = olc(BF, " ");
  const sw = S.dizi("Hocam,", 274.03, 7);          // 0 Hocam, 1 konser 2 yarın. | 3 Will 4 begin 5 olmaz 6 mı?
  const satir = [[0, 1, 2], [3, 4, 5, 6]];
  const gen = satir.map((s) => s.reduce((t, i) => t + olc(BF, sw[i].sozcuk), 0) + sp * (s.length - 1));
  const BX1 = 1650, BX0 = BX1 - Math.max(...gen) - 70, BY0 = 520, BASE = [BY0 + 64, BY0 + 130];
  koy(S.cizim({ svg: bas, ad: "ogrenci", kutu: { x: 1690, y: 470, w: 150, h: 206 }, esik: 0.004, enCok: 60,
    w: 3.2, tb: 273.88, sure: 0.55, olayEnCok: 3, nefes: false }), "B");
  koy(S.darbe(balonYol(BX0, BY0, BX1, BASE[1] + 80, 34, [1684, BY0 + 105]), { duz: true, w: 4.4, uc0: 12,
    uc1: 20 }, 274.00, 0.6, 0.6), "B");
  satir.forEach((s, si) => {
    let x = BX0 + 35;
    s.forEach((i) => {
      koy(S.metinPop({ parca: [[sw[i].sozcuk, KREM]], x, y: BASE[si], font: BF, tb: sw[i].t0, sure: 0.2,
        olcek0: 0.9, ses: i === 0 || i === 3 ? 0.5 : false, turu: "tik" }), "B");
      sw[i].x = x; sw[i].w = olc(BF, sw[i].sozcuk); x += sw[i].w + sp;
    });
  });
  // sahne bağı: sarı nokta, balondaki «begin» (275,90) ↔ kartta «begins»
  koy(nokta(sw[4].x + sw[4].w / 2, BASE[1] + 42, sw[4].t0), "B");
  kart(sondur(nokta(kel[2].x + kel[2].w / 2, kel[2].y - 90, sw[4].t0 + 0.02), SON.B[0], SON.B[1]));

  // ---------------- 42 (278,13–289,73) cevap: yakın çekim · tarife · resmî program → geniş zaman ----------------
  // 278,53 «gelecek,»: iki sarı daireye parıltı (anlam gelecek)
  kart(S.parilti(kel[2].x + kel[2].w / 2, kel[2].y - 80, T("gelecek,", 278.91)));
  kart(S.parilti(kel[9].x + kel[9].w / 2, kel[9].y - 80, T("gelecek,", 278.91) + 0.1));
  // 280,93 «Konser»: yakın çekim «The concert» — sarı kutu, kartın kalanı soluk
  const bx0 = kel[0].x - 14, bx1 = kel[1].x + kel[1].w + 14, by0 = kel[0].y - 56, bh = 78;
  const tYak = T("Konser", 281.31);
  kart({ ciz: (ctx, f) => {
    const a = 0.62 * kis((S.zm(f) - tYak) / 0.35); if (a <= 0.01) return;
    ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = renkCoz(ZEMIN); ctx.beginPath();
    ctx.rect(110, 150, 1700, 270); ctx.rect(bx0, by0, bx1 - bx0, bh); ctx.fill("evenodd"); ctx.restore();
  } });
  kart(S.darbeler(kutu(bx0, by0, bx1 - bx0, bh, 81), { w: 6, renk: SARI, alfa: 0.9, uc0: 10, uc1: 18 }, tYak, 0.12,
    0.08, 0.6));
  // 281,41 «tarifeye»: «tarife» Caveat etiketi; 282,69 «Program»: tablo (çerçeve + ara çizgi)
  S.koy(S.elYazisi({ metin: "tarife", x: 150, y: 540, boy: 64, renk: SARI, sozcukler: pen("tarifeye", 281.79, 1) }));
  const tTab = T("Program", 283.07);
  S.koy(S.darbeler(kutu(150, 575, 520, 220, 82), { w: 3.6, renk: IKINCIL, uc0: 10, uc1: 18 }, tTab, 0.14, 0.1,
    0.55));
  S.koy(S.darbe([[150, 685], [670, 685]], { duz: true, w: 3.6, renk: IKINCIL, uc0: 6, uc1: 10 },
    T("yazılı,", 283.55), 0.3, 0.4));
  // 283,81 «saat» · 284,17 «değişmez»: iki satır saat (rakam kartın cümlesinden)
  S.koy(S.metinPop({ parca: [["8:00", KREM], ["   begins", IKINCIL]], x: 180, y: 650, font: "700 52px Fredoka",
    tb: T("saat", 284.19), sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.metinPop({ parca: [["11:00", KREM], ["   ends", IKINCIL]], x: 180, y: 757, font: "700 52px Fredoka",
    tb: T("değişmez.", 284.55), sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }));
  // 285,25 «Özne»: (özne cansız ya da kişi) — Caveat, her sözcük kendi penceresinde
  S.koy(S.elYazisi({ metin: "(özne cansız ya da kişi)", x: 800, y: 600, boy: 60, renk: IKINCIL,
    sozcukler: pen("Özne", 285.63, 5) }));
  // 288,61 «resmî» · 289,01 «program»: resmî program / tarife → geniş zaman
  S.koy(S.metinPop({ parca: [["resmî program / tarife", KREM]], x: 800, y: 730, font: F64, tb: T("resmî", 288.99),
    sure: 0.25, olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.metinPop({ parca: [["→  ", IKINCIL], ["geniş zaman", SARI]], x: 800, y: 820, font: F64,
    tb: T("program.", 289.39), sure: 0.25, olcek0: 0.85, ses: 0.6, turu: "vurus" }));
}

surucu(kur, (f) => S.kare(f), KARE);

// SAHNE 07 — Kök 2 tabela (02-02-ydt-ileri; düz canvas, 858 kare, t_bas 129,38; cümle 20–23).
// Kendini çizen kalem; zaman yalnız kare numarasından, sözcük zamanları sozcukler.json'dan (T() ile okunur).
// Akış: «2 · Kök · Tabela» başlığı → kök cümlesi kartı (says, keep halkası · kafesteki köpek) → Türkçe çeviri
// → tabela, mektup, kitap çizimleri: sabit içerik → says · the sign / letter / book says (says sarı).
// Kırmızı yok; renkler yalnız kunye.js TEMALAR token'ları. Öğrenci sesi bu sahnede yok (soru anı 3.6 ve 5.4).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, kutu, ok, olc, kis, altCizgi } from "./sahne-ortak.js";

const KARE = 858, TBAS = 129.38, ICERIK = 846;
const KOKDIZ = "/projeler/02-02-ydt-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Root 2 / 3", etkin: 2,
  cumle: [20, 21, 22, 23] });
window.__S = S;                                   // önizleme ölçümü (olaylar.json)
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`;

// Anlatım sözcüğünün t0'ı (küresel sn); bulunamazsa sahne hiç yüklenmez (sessiz yanlış zaman olmaz).
const T = (ad, yakin) => {
  const r = S.dizi(ad, yakin, 1);
  if (!r.length || r[0].sozcuk !== ad) throw new Error("sözcük yok: " + ad + " @" + yakin);
  return r[0].t0;
};
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

// Öğeyi [t0, t1] sn arasında gerçekten söndürür: öğe kendi globalAlpha değerini mutlak yazdığı için
// (darbeCiz, metinPop) örnek üstünde globalAlpha yazımı sönme çarpanıyla çarpılır; söndükten sonra çizilmez.
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
// Sönme grubu B: cümle 22 çevirisi (146,6–146,85), tabela çizimlerine yer açar. Grupsuz öğe sona kadar kalır.
const SON = { B: [146.6, 146.85] };
const koy = (e, g) => S.koy(g ? sondur(e, SON[g][0], SON[g][1]) : e);
// Elle çizilen nesne için tek «çizim» kutusu bildirir (çakışma kapısı); alt darbeler kutu bildirmez.
const kutuBildir = (ad, tb, x, y, w, h) => S.koy({ ciz: () => {
  if (S.zm(S.cur) >= tb) window.__kalemKutu?.ekle("cizim", ad, x, y, w, h);
} });

async function kur() {
  await S.kur();
  const [kopek, kitap] = await Promise.all([svgOku("tabler/cat.svg"), svgOku("tabler/book.svg")]);
  const F60 = FF(60), F64 = FF(64), F72 = FF(72);
  // kare numarasını kutu bildiriminde kullanmak için kare() sarılır
  const kare0 = S.kare.bind(S);
  S.kare = async (f, h) => { S.cur = f; return kare0(f, h); };

  // ---------------- 20 (129,93–131,85) «İkinci kök: tabela.» — daire içinde 2 · Kök · Tabela ----------------
  S.koy(S.daireSayi(2, 200, 190, T("İkinci", 129.93)));
  S.koy(S.metinPop({ parca: [["Kök", KREM]], x: 290, y: 215, font: F72, tb: T("kök:", 130.41), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" }));
  S.koy(S.elYazisi({ metin: "Tabela", x: 480, y: 215, boy: 96, renk: SARI, sozcukler: pen("tabela.", 131.13, 1) }));

  // ---------------- 21 (132,40–138,72) kök cümlesi: kart + 3 satır (7 + 7 + 8 sözcük) ----------------
  S.koy(S.darbeler(kutu(110, 280, 1300, 300, 71), { w: 3.6, renk: RT.ikincil, uc0: 10, uc1: 18 }, 132.1, 0.14,
    0.1, 0.55));
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("Because", 132.4, 22), x: 150, y: 360, maxGen: 1260,
    font: F60, satirH: 90, satirSay: [7, 7, 8], bosluk: 4 }));
  const k = cum.kel;      // 0 Because 1 the 2 sign 3 says … 6 forbidden | 7 to … 13 cages, | 14 the … 21 bags.
  S.koy(S.halka(k[3], T("says", 133.36), 0.4, 11, 6, true));
  S.koy(S.halka(k[16], T("keep", 137.04), 0.4, 13, 6, true));
  // kafesteki köpek: köpek 134,96 «animals»; kafes çerçevesi ve çubuklar 135,60 «cages,»
  S.koy(S.cizim({ svg: kopek, ad: "kedi", kutu: { x: 1510, y: 345, w: 220, h: 190 }, esik: 0.004, enCok: 20,
    w: 5, tb: T("animals", 134.96), sure: 0.9, olayEnCok: 4, nefes: false }));
  {
    const tc = T("cages,", 135.6);
    S.koy(S.darbeler(kutu(1470, 310, 300, 250, 72), { w: 4, renk: IKINCIL, uc0: 8, uc1: 12 }, tc, 0.12, 0.08, 0.55));
    [1520, 1570, 1620, 1670, 1720].forEach((x, i) => S.koy(S.darbe([[x, 316], [x, 554]], { duz: true, w: 3.4,
      renk: IKINCIL, uc0: 6, uc1: 8 }, tc + 0.45 + i * 0.07, 0.16, false)));
  }

  // ---------------- 22 (139,27–146,31) Türkçe çeviri: her sözcük kendi konuşma penceresinde ----------------
  koy(S.elYazisi({ metin: "Tabela, kafesteki hayvanları beslemenin yasak olduğunu söylüyor;", x: 150, y: 650,
    boy: 52, renk: IKINCIL, sozcukler: pen("Tabela,", 139.27, 7) }), "B");
  koy(S.elYazisi({ metin: "bu yüzden çocuklar atıştırmalıklarını çantada tutuyor.", x: 150, y: 715, boy: 52,
    renk: IKINCIL, sozcukler: pen("bu", 143.31, 6) }), "B");

  // ---------------- 23 (146,86–157,59) tabela, mektup, kitap: sabit içerik → says ----------------
  // tabela (146,86 «Tabelanın»): levha + direk + mesaj çizgileri; etiket «sabit mesaj» 147,90 «değişmez.»
  {
    const tb = T("Tabelanın", 146.86);
    S.koy(S.darbeler(kutu(150, 640, 230, 120, 73), { w: 4.4, uc0: 8, uc1: 12 }, tb, 0.14, 0.09, 0.55));
    S.koy(S.darbe([[265, 762], [265, 860]], { duz: true, w: 5, uc0: 8, uc1: 12 }, tb + 0.4, 0.2, 0.5));
    S.koy(S.darbe([[215, 862], [315, 862]], { duz: true, w: 5, uc0: 8, uc1: 12 }, tb + 0.6, 0.15, false));
    [[675, 345], [702, 315], [729, 335]].forEach(([y, x1], i) => S.koy(S.darbe([[185, y], [x1, y]], { duz: true,
      w: 3.4, renk: IKINCIL, uc0: 6, uc1: 8 }, T("mesajı", 147.54) + i * 0.12, 0.2, i === 0 ? 0.4 : false)));
    kutuBildir("tabela", tb, 150, 640, 230, 224);
  }
  S.koy(S.elYazisi({ metin: "sabit mesaj", x: 400, y: 850, boy: 56, renk: SARI, tb: T("değişmez.", 147.9),
    sure: 0.9 }));
  // mektup (148,94 «Mektup»): zarf
  {
    const tm = T("Mektup", 148.94);
    S.koy(S.darbeler(kutu(480, 650, 210, 140, 74), { w: 4.4, uc0: 8, uc1: 12 }, tm, 0.14, 0.09, 0.55));
    S.koy(S.darbe([[480, 650], [585, 730], [690, 650]], { duz: true, w: 4.4, uc0: 8, uc1: 12 }, tm + 0.4, 0.3,
      false));
    kutuBildir("mektup", tm, 480, 650, 210, 140);
  }
  // kitap (149,50 «kitap»)
  S.koy(S.cizim({ svg: kitap, ad: "kitap", kutu: { x: 790, y: 630, w: 170, h: 170 }, esik: 0.004, enCok: 10,
    w: 5, tb: T("kitap", 149.5), sure: 0.8, olayEnCok: 3, nefes: false }));
  // 149,98 «sabit»: sabit içerik · 152,14 «geniş»: ok · 152,94 «gelir:»: says (sarı)
  {
    const YB = 975, FB = F64;
    const m1 = S.koy(S.metinPop({ parca: [["sabit içerik", KREM]], x: 150, y: YB, font: FB, tb: T("sabit", 149.98),
      sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }));
    const ax = 150 + m1.w + 30;
    S.koy(S.darbeler(ok([ax, YB - 24], [ax + 130, YB - 24], 5),
      { w: 6.5, renk: SARI, uc0: 10, uc1: 14 }, T("geniş", 152.14), 0.18, 0.12, 0.5));
    S.koy(S.metinPop({ parca: [["says", SARI]], x: ax + 130 + 30, y: YB, font: FB, tb: T("gelir:", 152.94),
      sure: 0.3, olcek0: 0.8, ses: 0.7, turu: "vurus" }));
    S.koy(S.parilti(k[3].x + k[3].w / 2, k[3].y - 82, T("gelir:", 152.94) + 0.05, 26));
  }
  // 153,67 / 155,11 / 156,47: the sign says · the letter says · the book says (says sarı, altı çizili)
  [["sign", "the", 153.67, "says,", 154.23, 700, 91], ["letter", "the", 155.11, "says,", 155.59, 800, 92],
    ["book", "the", 156.47, "says.", 156.87, 900, 93]].forEach(([ad, , tThe, sz, tSay, y, th], i) => {
    const on = `the ${ad} `, son = i === 2 ? "." : ",";
    S.koy(S.metinPop({ parca: [[on, KREM], ["says", SARI], [son, KREM]], x: 1130, y, font: F60,
      tb: T("the", tThe), sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }));
    const xs = 1130 + olc(F60, on), ws = olc(F60, "says");
    S.koy(S.darbe(altCizgi(xs - 4, xs + ws + 4, y + 16, th), { w: 7, renk: RT.vurguDolgu, alfa: 0.9, uc0: 8,
      uc1: 12 }, T(sz, tSay), 0.3, 0.5));
  });
}

surucu(kur, (f) => S.kare(f), KARE);

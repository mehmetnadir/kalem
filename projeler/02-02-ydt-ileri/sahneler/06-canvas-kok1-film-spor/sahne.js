// SAHNE 06 — Kök 1 film ve spor (02-02-ydt-ileri; düz canvas, 1144 kare, t_bas 91,66; cümle 14–19).
// Kendini çizen kalem; zaman yalnız kare numarasından, sözcük zamanları sozcukler.json'dan (T() ile okunur).
// Akış: film kartı (acts, keeps halkası · tv çizimi) → Türkçe çeviri → öğrenci balonu (soru anı 1, yanılgı:
// "olay bitmiş, o halde geçmiş") → özet → geniş zaman (film · kitap · öykü, öğrenci baş sallar) → spor kartı
// (runs halkası · futbol topu) → Türkçe çeviri → spor yorumu → runs (özet etiketine spor eklenir).
// Kırmızı yok (kırmızı yalnız dördüncü çerçevede, 04. sahne); renkler yalnız kunye.js TEMALAR token'ları.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, olc, kis } from "./sahne-ortak.js";

const KARE = 1144, TBAS = 91.66, ICERIK = 1132;
const KOKDIZ = "/projeler/02-02-ydt-ileri/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Root 1 / 3", etkin: 2,
  cumle: [14, 15, 16, 17, 18, 19] });
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
// Sönme grupları: A = film bölümü + özet (117,0'de spor kartına yer açar) · B = film çevirisi (balona yer açar)
// · C = öğrenci balonu (özet satırına yer açar). Grupsuz öğe sahne sonuna kadar kalır.
const SON = { A: [116.75, 117.0], B: [104.9, 105.2], C: [110.2, 110.5] };
const koy = (e, g) => S.koy(g ? sondur(e, SON[g][0], SON[g][1]) : e);

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
  const [tv, top, bas] = await Promise.all([svgOku("tabler/device-tv.svg"), svgOku("tabler/ball-football.svg"),
    svgOku("peeps-kit/ogrenci-bas.svg")]);
  const F60 = FF(60), F52 = FF(52), F80 = FF(80), F96 = FF(96);

  // ---------------- 14 (92,21–98,53) film cümlesi: kart + 3 satır (4 + 6 + 8 sözcük) ----------------
  koy(S.darbeler(kutu(110, 160, 1240, 330, 61), { w: 3.6, renk: RT.ikincil, uc0: 10, uc1: 18 }, 92.1, 0.14, 0.1,
    0.55), "A");
  const film = S.cumleYaz({ sozcukler: S.dizi("Elisabeth", 92.21, 18), x: 150, y: 270, maxGen: 1240, font: F60,
    satirH: 90, satirSay: [4, 6, 8], bosluk: 4 });
  koy(film, "A");
  const fk = film.kel;          // 0 Elisabeth 1 Moss 2 acts 3 brilliantly | 4 in … 9 Man', | 10 and … 17 edge.
  koy(S.halka(fk[2], T("acts", 93.25), 0.4, 11, 6, true), "A");
  koy(S.halka(fk[13], T("keeps", 97.01), 0.4, 13, 6, true), "A");
  koy(S.cizim({ svg: tv, ad: "tv", kutu: { x: 1480, y: 200, w: 240, h: 230 }, esik: 0.004, enCok: 8, w: 5,
    tb: T("movie", 94.53), sure: 1.0, olayEnCok: 4, nefes: false }), "A");

  // ---------------- 15 (99,08–104,84) Türkçe çeviri: her sözcük kendi konuşma penceresinde ----------------
  koy(S.elYazisi({ metin: "Elisabeth Moss, Görünmez Adam filminde harika oynuyor;", x: 150, y: 580, boy: 52,
    renk: IKINCIL, sozcukler: pen("Elisabeth", 99.08, 7) }), "B");
  koy(S.elYazisi({ metin: "hikâye izleyiciyi tedirgin ediyor.", x: 150, y: 645, boy: 52, renk: IKINCIL,
    sozcukler: pen("hikâye", 102.73, 4) }), "B");

  // ---------------- 16 (105,39–109,88) SORU ANI 1: öğrenci başı + el çizimi balon ----------------
  const BF = "600 42px Fredoka", sp = olc(BF, " ");
  const sw = S.dizi("Hocam,", 105.39, 7);             // Hocam, film bitti. | Neden oynadı değil, acts?
  const satir = [[0, 1, 2], [3, 4, 5, 6]];
  const gen = satir.map((s) => s.reduce((t, i) => t + olc(BF, sw[i].sozcuk), 0) + sp * (s.length - 1));
  const BX1 = 1650, BX0 = BX1 - Math.max(...gen) - 70, BY0 = 520, BASE = [BY0 + 64, BY0 + 130];
  const gb = S.cizim({ svg: bas, ad: "ogrenci", kutu: { x: 1690, y: 470, w: 150, h: 206 }, esik: 0.004,
    enCok: 60, w: 3.2, tb: 105.0, sure: 0.55, olayEnCok: 3, nefes: false });
  const hx = 1765, hy = 676;                                        // boyun tabanı: baş sallama ekseni
  koy(gb, "A");
  const balon = [S.darbe(balonYol(BX0, BY0, BX1, BASE[1] + 80, 34, [1684, BY0 + 105]), { duz: true, w: 4.4,
    uc0: 12, uc1: 20 }, 105.15, 0.6, 0.6)];
  satir.forEach((s, si) => {
    let x = BX0 + 35;
    s.forEach((i) => {
      balon.push(S.metinPop({ parca: [[sw[i].sozcuk, KREM]], x, y: BASE[si], font: BF, tb: sw[i].t0,
        sure: 0.2, olcek0: 0.9, ses: i === 0 || i === 3 ? 0.5 : false, turu: "tik" }));
      sw[i].x = x; sw[i].w = olc(BF, sw[i].sozcuk); x += sw[i].w + sp;
    });
  });
  // sahne bağı: balondaki acts? halkası + karttaki acts sözcüğünde parıltı (aynı an)
  const ac = sw[6], tAc = T("acts?", 109.16);
  balon.push(S.darbe(elips(ac.x + ac.w / 2, BASE[1] - 14, ac.w / 2 + 14, 36, -0.03, 19),
    { w: 6, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, tAc, 0.4, 0.55));
  koy(balon, "C");
  koy(S.parilti(fk[2].x + fk[2].w / 2, fk[2].y - 82, tAc + 0.05, 26), "A");

  // ---------------- 17 (110,58–116,66) özet → geniş zaman; film · kitap · öykü ----------------
  // 110,58 «Özetin»: özet · 112,10 «olay»: ok · 113,54 «geniş»: geniş zaman · öğrenci 113,9 baş sallar
  const YR = 780;
  const ozet = S.metinPop({ parca: [["özet", SARI]], x: 150, y: YR, font: F96, tb: T("Özetin", 110.58), sure: 0.3,
    olcek0: 0.85, ses: 0.5, turu: "tik" });
  koy(ozet, "A");
  const ax = 150 + ozet.w + 36;
  koy(S.darbeler(ok([ax, YR - 34], [ax + 150, YR - 34], 5), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 },
    T("olay", 112.1), 0.18, 0.12, 0.5), "A");
  koy(S.metinPop({ parca: [["geniş zaman", KREM]], x: ax + 150 + 36, y: YR, font: F96, tb: T("geniş", 113.54),
    sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }), "A");
  // etiket satırı (kalıcı): film · kitap · öykü · (126,40) spor
  const YC = 905, chipler = [["film", T("bitmiş", 112.42)], ["kitap", T("Kitap", 114.66)],
    ["öykü", T("öykü", 115.62)], ["spor", T("yorumunda", 126.4)]];
  let cx = 150;
  chipler.forEach(([m, tb]) => {
    const w = olc(F52, m);
    S.koy(S.metinPop({ parca: [[m, KREM]], x: cx, y: YC, font: F52, tb, sure: 0.3, olcek0: 0.85, ses: 0.5,
      turu: "tik" }));
    S.koy(S.darbe([[cx - 6, YC + 14], [cx + w + 6, YC + 12]], { duz: true, w: 6, renk: RT.vurguDolgu, alfa: 0.9,
      uc0: 8, uc1: 12 }, tb + 0.15, 0.25, false));
    cx += w + 90;
  });
  // öğrenci onaylar (113,9–114,9): baş iki kez sallanır
  const f0 = S.fr(113.9), f1 = S.fr(114.9);
  gb.donusum = (f) => {
    const u = kis((f - f0) / (f1 - f0)), e = u <= 0 || u >= 1 ? 0 : Math.abs(Math.sin(u * Math.PI * 2));
    return { cx: hx, cy: hy, tx: 0, ty: 12 * e, dondur: 0.06 * e, olcek: 1 };
  };
  S.olay(f0, "tik", 0.4); S.olay(S.fr(114.4), "tik", 0.4);

  // ---------------- 18 (117,21–120,57) spor cümlesi: kart + 2 satır (5 + 5 sözcük) ----------------
  S.koy(S.darbeler(kutu(110, 160, 860, 250, 62), { w: 3.6, renk: RT.ikincil, uc0: 10, uc1: 18 }, 117.0, 0.14,
    0.1, 0.55));
  const ham = S.dizi("Chris", 117.21, 11), soz = [];       // fifty + yard → ekranda «50-yard»
  ham.forEach((w) => {
    if (w.sozcuk === "fifty") soz.push({ ...w, sozcuk: "50-yard" });
    else if (w.sozcuk === "yard") soz[soz.length - 1].t1 = w.t1;
    else soz.push(w);
  });
  const spor = S.koy(S.cumleYaz({ sozcukler: soz, x: 150, y: 270, maxGen: 860, font: F60, satirH: 90,
    satirSay: [5, 5], bosluk: 4 }));
  const sk = spor.kel;           // 0 Chris 1 runs 2 with 3 the 4 ball | 5 halfway 6 to 7 the 8 50-yard 9 line.
  S.koy(S.halka(sk[1], T("runs", 117.61), 0.4, 15, 6, true));
  S.koy(S.cizim({ svg: top, ad: "top", kutu: { x: 1100, y: 180, w: 230, h: 230 }, esik: 0.004, enCok: 8, w: 5,
    tb: T("ball", 118.17), sure: 1.0, olayEnCok: 4, nefes: false }));

  // ---------------- 19 (121,12–129,38) Türkçe çeviri · spor yorumu → runs ----------------
  S.koy(S.elYazisi({ metin: "Chris topla birlikte elli yarda çizgisine", x: 150, y: 560, boy: 52, renk: IKINCIL,
    sozcukler: pen("Chris", 121.12, 6) }));
  S.koy(S.elYazisi({ metin: "giden yolun yarısına kadar koşuyor.", x: 150, y: 625, boy: 52, renk: IKINCIL,
    sozcukler: pen("giden", 123.68, 5) }));
  const sp1 = S.koy(S.metinPop({ parca: [["spor yorumu", KREM]], x: 150, y: YR, font: F80, tb: T("Spor", 126.08),
    sure: 0.3, olcek0: 0.85, ses: 0.5, turu: "tik" }));
  const bx = 150 + sp1.w + 36;
  S.koy(S.darbeler(ok([bx, YR - 30], [bx + 150, YR - 30], 6), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 },
    T("çoğunlukla", 127.04), 0.18, 0.12, 0.5));
  const tRuns = T("runs", 127.93);
  const rx = bx + 150 + 36, rw = olc(F80, "runs");
  S.koy(S.metinPop({ parca: [["runs", SARI]], x: rx, y: YR, font: F80, tb: tRuns, sure: 0.3, olcek0: 0.8,
    ses: 0.7, turu: "vurus" }));
  S.koy(S.parilti(sk[1].x + sk[1].w / 2, sk[1].y - 82, tRuns + 0.05, 26));
  S.koy(S.darbe(elips(rx + rw / 2, YR - 28, rw / 2 + 16, 46, -0.03, 21), { w: 6, renk: SARI, alfa: 0.85,
    uc0: 14, uc1: 30 }, T("gelir.", 128.66), 0.4, 0.55));
}

surucu(kur, (f) => S.kare(f), KARE);

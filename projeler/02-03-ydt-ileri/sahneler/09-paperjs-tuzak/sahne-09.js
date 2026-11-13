// SAHNE 09 — Tuzak (Paper.js, 1277 kare, t_bas 221,32; cümle 11–13). Yerel kare = round((t − 221,32) × 30).
// Akış: «It has a great view of the sea.» kartı (has sarı kutu, deniz çizgisi) · soru anı 2 (öğrenci balonu,
// yanılgı: durum fiiline -ing) · has + -ing yazılır, kırmızı çarpıyla silinir · köşe listesi have · believe ·
// recommend → NO -ing · ikinci kart alt: I definitely recommend … (recommend sarı daire, performative etiketi).
import { sahneKur, RT } from "/projeler/02-03-ydt-ileri/sahneler/09-paperjs-tuzak/kalem-paper.js";

export const KARE = 1277, T_BAS = 221.32;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Trap", etkin: 3, kayma: 0 });
  const { fr, daire, yazi, elYazisi, cumle, altCizgi, ok, kutu, ciz, svgCiz, oge, sozcukler, genislik, kis,
    parilti, olay, not } = S;
  window.__S = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;
  const z11 = sozcukler(11), z12 = sozcukler(12), z13 = sozcukler(13);
  const pen = (z, i) => ({ f0: z[i].f, f1: z[i].f1 });              // sözcük penceresi (kare)

  // --- 222,24 «Tuzak.»: TRAP etiketi (sağ üst, sarı)
  yazi("TRAP", { x: 1780, y: 205, boyut: 64, aile: "Fredoka", agirlik: 700, hizala: "sag", renk: SARI,
    bas: z11[0].f, sure: 8, olcek: true, ses: true });
  not("TRAP etiketi", z11[0].f);

  // --- 225,77–228,20 kart 1: «It has a great view of the sea.» (Fredoka 84, sözcük zamanlı, sarı alt çizgi)
  const k1 = cumle(z11.slice(6, 14).map((w) => ({ s: w.s, f: w.f })), { x: 140, y: 345, boyut: 84,
    aile: "Fredoka", agirlik: 700 });
  altCizgi(k1, { tut: 40 });
  not("kart 1 cümle", k1[0].bas);
  const has = k1[1];
  // 225,93 «has»: sarı kutu
  kutu(has.x0 - 14, has.y - 76, has.w + 28, 108, { bas: z11[7].f + 2, sure: 22, w: 5, renk: SARI });
  not("has kutusu", z11[7].f);

  // 227,29 «sea.»: deniz çizgisi (üç dalga, sarı değil: ikincil)
  const dalga = (y0, x0, x1, g, tohum) => Array.from({ length: 30 }, (_, i) => {
    const u = i / 29, x = x0 + (x1 - x0) * u;
    return [x, y0 + g * Math.sin(u * Math.PI * 6 + tohum)];
  });
  [[480, 140, 760, 10], [515, 190, 700, 8], [548, 250, 640, 6]].forEach(([y, a, b, g], i) => {
    ciz(dalga(y, a, b, g, i), { bas: z11[13].f + i * 7, sure: 22, w: 5, renk: IKI, alfa: 0.9, duz: true,
      uc0: 10, uc1: 18, ses: i === 0 ? "cizgi" : false, tur: "cizim", ad: "deniz" });
  });
  not("deniz çizgisi", z11[13].f);

  // 228,26–229,70 «Manzara çok güzel.» Türkçe çeviri (Caveat 56, ikincil)
  elYazisi("Manzara çok güzel.", { x: 140, y: 625, boyut: 56, renk: IKI,
    sozcukler: [pen(z11, 14), pen(z11, 15), pen(z11, 16)] });
  not("Türkçe çeviri", z11[14].f);

  // --- 229,90–236,54 SORU ANI 2: öğrenci başı + balon (yanılgı: «şu anda» → It is having)
  const ogr = oge({ alfa: (f) => 1 - kis((f - fr(236.54)) / 12) });
  await svgCiz("peeps-kit/ogrenci-bas.svg", { kutu: [1650, 420, 150, 206], bas: fr(229.9), sure: 16, azami: 60,
    w: 3.2, oge: ogr, sesAralik: 6, cizgi: "#000", kisaAtla: 0.004 });
  not("öğrenci başı", fr(229.9));
  // ekran metni (taslak §4 satır 12): «Manzarası şu anda var. It is having olmaz mı?»
  const BF = 44, bfont = `600 ${BF}px Fredoka`, bos = genislik(" ", bfont);
  const kel = [[2, "Manzarası"], [3, "şu"], [4, "anda"], [5, "var."], [6, "It"], [7, "is"], [8, "having"],
    [9, "olmaz"], [10, "mı?"]];
  const satir = [kel.slice(0, 4), kel.slice(4)];
  const gen = satir.map((s) => s.reduce((t, [, m]) => t + genislik(m, bfont), 0) + bos * (s.length - 1));
  const BX1 = 1610, BX0 = BX1 - Math.max(...gen) - 70, BY0 = 470, BASE = [BY0 + 66, BY0 + 132];
  const arc = (cx, cy, r, a0, a1) => Array.from({ length: 7 }, (_, i) => {
    const a = a0 + (a1 - a0) * i / 6; return [cx + r * Math.cos(a), cy + r * Math.sin(a)];
  });
  const R = 34, BY1 = BASE[1] + 56;
  const yol = [...arc(BX0 + R, BY0 + R, R, Math.PI, 1.5 * Math.PI), ...arc(BX1 - R, BY0 + R, R, 1.5 * Math.PI,
    2 * Math.PI), [BX1, BY0 + 80], [1646, BY0 + 110], [BX1, BY0 + 130], ...arc(BX1 - R, BY1 - R, R, 0,
    0.5 * Math.PI), ...arc(BX0 + R, BY1 - R, R, 0.5 * Math.PI, Math.PI), [BX0, BY0 + R], [BX0 + 6, BY0 + R - 14]];
  ciz(yol, { bas: fr(230.1), sure: 18, w: 4.4, duz: true, uc0: 12, uc1: 20, oge: ogr, tur: "kart",
    ad: "balon" });
  const pos = {};
  satir.forEach((s, si) => {
    let x = BX0 + 35;
    s.forEach(([i, m]) => {
      const w = genislik(m, bfont);
      yazi(m, { x, y: BASE[si], boyut: BF, aile: "Fredoka", agirlik: 600, renk: KRE, bas: z12[i].f, sure: 6,
        olcek: true, ses: i === 2 || i === 6, solma: [fr(236.54), fr(236.9)] });
      pos[i] = { x, w }; x += w + bos;
    });
  });
  not("balon sözcükleri", z12[2].f);
  // sahne bağı (soru-ani §6): balondaki «having» ↔ kart 1'deki «has» (sarı ok)
  ok([BX0 + 30, BY0 - 14], [has.x0 + has.w / 2, has.y + 64], { bas: z12[8].f, sure: 24,
    bukum: 0.03, yon: [0, 1], w: 6, renk: SARI, oge: ogr, uzun: 22 });   // cümlenin altından geçer (yazıya değmez)
  not("having ↔ has oku", z12[8].f);

  // --- 237,50 «Sahip olmak»: has kutusu nabız (parıltı)
  parilti(has.x1 + 30, has.y - 70, { bas: fr(237.55), r: 26 });

  // --- 239,66–240,40 «-ing almaz»: has yanına -ing yazılır, kırmızı çarpıyla çizilir, silinir
  const ing = oge({ alfa: (f) => 1 - kis((f - fr(240.75)) / 10) });
  elYazisi("-ing", { x: has.x1 - 20, y: has.y - 108, boyut: 80, renk: SARI, sozcukler: [pen(z13, 5)], oge: ing });
  not("-ing yazılır", z13[5].f);
  ciz([[has.x1 - 34, has.y - 168], [has.x1 + 108, has.y - 100]], { bas: z13[6].f, sure: 8, w: 8, renk: KIR,
    alfa: 0.95, duz: true, uc0: 6, uc1: 8, oge: ing, tur: "isaret", ad: "carpi" });
  ciz([[has.x1 + 108, has.y - 172], [has.x1 - 34, has.y - 96]], { bas: z13[6].f + 8, sure: 8, w: 8, renk: KIR,
    alfa: 0.95, duz: true, uc0: 6, uc1: 8, oge: ing, ses: "tik", tur: "isaret", ad: "carpi" });
  not("-ing çarpısı", z13[6].f);

  // --- köşe listesi (sol alt, Fredoka 56): have (own) · believe · recommend → NO -ing
  const LF = 56, LX = 150, RY = [740, 810, 880];
  const sat1 = yazi("have (own)", { x: LX, y: RY[0], boyut: LF, aile: "Fredoka", agirlik: 700, renk: KRE,
    bas: z13[4].f, sure: 8, olcek: true, ses: true });
  not("have (own)", z13[4].f);
  const sat2 = yazi("believe", { x: LX, y: RY[1], boyut: LF, aile: "Fredoka", agirlik: 700, renk: KRE,
    bas: z13[7].f, sure: 8, olcek: true, ses: true });
  not("believe", z13[7].f);
  // 245,59–245,91 «are believing»: -ing ikincil + kırmızı çizgi (believe + -ing yok)
  elYazisi("-ing", { x: sat2.x1 + 26, y: RY[1] - 6, boyut: 56, renk: IKI, sozcukler: [{ f0: z13[18].f, f1: z13[19].f1 }] });
  ciz([[sat2.x1 + 14, RY[1] - 18], [sat2.x1 + 120, RY[1] - 28]], { bas: z13[19].f1, sure: 6, w: 6, renk: KIR,
    alfa: 0.95, duz: true, uc0: 5, uc1: 6, ses: "tik", tur: "isaret", ad: "carpi" });
  const sat3 = yazi("recommend", { x: LX, y: RY[2], boyut: LF, aile: "Fredoka", agirlik: 700, renk: KRE,
    bas: z13[20].f, sure: 8, olcek: true, ses: true });
  not("recommend", z13[20].f);
  // 248,56 «performative»: etiket yalnız recommend için (Caveat, sarı)
  elYazisi("performative", { x: sat3.x1 + 40, y: RY[2] - 4, boyut: 60, renk: SARI, sozcukler: [pen(z13, 22)] });
  not("performative etiketi", z13[22].f);
  // 253,30 «Tavsiye ediyorum»: recommend satırı sarı alt çizgi
  ciz([[sat3.x0 - 4, RY[2] + 12], [sat3.x1 + 6, RY[2] + 9]], { bas: z13[30].f, sure: 10, w: 7, renk: RT.vurguDolgu,
    alfa: 0.85, duz: true, uc0: 8, uc1: 12, tur: "isaret", ad: "alt-cizgi" });
  not("recommend alt çizgisi", z13[30].f);

  // --- 256,91–259,79 kart 2 (alt, sağ): «I definitely recommend a holiday in this lovely city.»
  const k2 = cumle(z13.slice(35, 44).map((w, i) => ({ s: w.s, f: w.f, satir: i < 5 ? 0 : 1 })), { x: 940,
    y: 790, boyut: 56, aile: "Fredoka", agirlik: 700, aralik: 76 });
  altCizgi(k2, { tut: 30 });
  not("kart 2 cümle", k2[0].bas);
  const rc = k2[2];
  daire((rc.x0 + rc.x1) / 2, rc.y - 20, rc.w / 2 + 12, 44, { bas: z13[37].f + 4, sure: 20 });
  not("recommend dairesi", z13[37].f);

  // --- 261,24–263,40 «Sinyal olsa bile -ing yok.»: → NO -ing (liste altı, sarı)
  const etk = yazi("→  NO  ", { x: LX, y: 955, boyut: 48, aile: "Fredoka", agirlik: 700, renk: IKI,
    bas: z13[44].f, sure: 8, olcek: true, ses: true });
  yazi("-ing", { x: etk.x1, y: 955, boyut: 48, aile: "Fredoka", agirlik: 700, renk: SARI,
    bas: z13[47].f, sure: 8, olcek: true, ses: true });
  not("→ NO -ing", z13[44].f);
  return S;
}

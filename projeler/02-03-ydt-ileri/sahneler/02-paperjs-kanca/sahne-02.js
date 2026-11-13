// Sahne 02 — Kanca (02-03 YDT ileri; 384 kare, t_bas 3,00; cümle 1 sonu + cümle 2). Yerel kare = round((t − 3,00) × 30).
// Faz A (3,40–9,50): iki kart (are leaving / takes off) + kalemle "?"; sözcük zamanları ortak/anlatim/sozcukler.json.
// Faz B (10,19–15,2): "Bu derste" planı: 4 kutu (KEY · PAIR · ITEMS · TRAP); anahtar çizimi "karar anahtarını" sözcüğünde.
// İlk 12 ve son 12 kare durgun (geçiş altında): içerik f12'de başlar, son olay f361.
import { sahneKur, RT } from "/projeler/02-03-ydt-ileri/sahneler/02-paperjs-kanca/kalem-paper.js";

export const KARE = 384, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, daire, yazi, elYazisi, kutu, ciz, tik, not, oge, genislik, kis } = S;
  const KRE = RT.murekkep, SARI = RT.vurgu, IKI = RT.ikincil;
  // sözcük zamanları: sabit sayı yok, sozcukler.json'dan (küresel sn)
  const c1 = S.sozcukler(1), c2 = S.sozcukler(2);
  const t2 = (i) => c2[i].t;            // cümle 2 sözcük t0
  const faz1 = oge({ alfa: (f) => 1 - kis((f - fr(9.2)) / 10) });   // 9,20–9,53 sönme
  const SON = [fr(9.2), fr(9.2) + 10];
  const fazVs = oge({ alfa: (f) => 1 - kis((f - fr(9.2)) / 10) });   // elYazisi kendi grubunda (kapı: oge yazıyla paylaşılmaz)

  // ---------- FAZ A ----------
  const FA = "700 80px Fredoka", yT = 420;
  const w1 = genislik("are leaving", FA), w2 = genislik("takes off", FA), pad = 48;
  const b1x1 = 960 - 120, b1x0 = b1x1 - (w1 + 2 * pad), b2x0 = 960 + 120, b2x1 = b2x0 + w2 + 2 * pad;
  const m1 = (b1x0 + b1x1) / 2, m2 = (b2x0 + b2x1) / 2;
  // kart 1 (are leaving): f12 = ilk durgun olmayan kare (3,40; "ayrı" 3,16 geçiş altında kaldı)
  kutu(b1x0, 328, b1x1 - b1x0, 136, { bas: 12, sure: 16, w: 4, oge: faz1 }); not("kart 1 kutusu", 12);
  yazi("are leaving", { x: m1, y: yT, boyut: 80, aile: "Fredoka", agirlik: 700, hizala: "orta", renk: KRE,
    bas: 16, sure: 10, olcek: true, ses: true, sondur: SON }); not("are leaving", 16);
  // kart 2 (takes off): "zaman." 3,48–4,12 içinde
  kutu(b2x0, 328, b2x1 - b2x0, 136, { bas: fr(3.80), sure: 16, w: 4, oge: faz1 }); not("kart 2 kutusu", fr(3.8));
  yazi("takes off", { x: m2, y: yT, boyut: 80, aile: "Fredoka", agirlik: 700, hizala: "orta", renk: KRE,
    bas: fr(4.0), sure: 10, olcek: true, ses: true, sondur: SON }); not("takes off", fr(4.0));
  // "?" kalemle (4,13 → 4,93): yay + gövde + nokta
  {
    const cx = 960, cy = 340, r = 58, pts = [];
    for (let d = -190; d <= 70; d += 12) { const a = d * Math.PI / 180; pts.push([cx + r * Math.cos(a), cy + r * Math.sin(a)]); }
    pts.push([cx + 6, cy + r + 18], [cx, cy + r + 44]);
    ciz(pts, { w: 9, renk: SARI, alfa: 0.9, bas: fr(4.13), sure: 20, oge: faz1, ad: "soru isareti", uc0: 14, uc1: 20 });
    ciz([[cx - 2, cy + r + 82], [cx + 3, cy + r + 85]], { w: 12, renk: SARI, alfa: 0.9, bas: fr(4.13) + 20, sure: 6,
      oge: faz1, ad: "soru noktasi", uc0: 2, uc1: 2, duz: true });
    not("? kalemle", fr(4.13));
  }
  // şimdiki zaman etiketi (6,03) + -ing daire (6,47)
  yazi("PRESENT CONTINUOUS", { x: m1, y: 300, boyut: 34, aile: "Lexend", agirlik: 700, hizala: "orta", renk: KRE,
    bas: fr(c2[3].t), sure: 12, ses: true, sondur: SON }); not("PRESENT CONTINUOUS", fr(c2[3].t));
  {
    const wl = genislik("leaving", FA), x0 = m1 - w1 / 2 + genislik("are ", FA);
    daire(x0 + wl / 2, yT - 30, wl / 2 + 16, 52, { bas: fr(c2[4].t), sure: 22, oge: faz1 }); not("leaving daire", fr(c2[4].t));
  }
  // geniş zaman etiketi (7,39) + takes belirteç (7,71)
  yazi("SIMPLE PRESENT", { x: m2, y: 300, boyut: 34, aile: "Lexend", agirlik: 700, hizala: "orta", renk: KRE,
    bas: fr(c2[6].t), sure: 12, ses: true, sondur: SON }); not("SIMPLE PRESENT", fr(c2[6].t));
  {
    const wt = genislik("takes", FA), x0 = m2 - w2 / 2;
    ciz([[x0 - 4, yT + 12], [x0 + wt + 4, yT + 9]], { duz: true, w: 12, renk: RT.vurguDolgu, alfa: 0.85,
      bas: fr(c2[7].t), sure: 14, oge: faz1, tur: "isaret", ad: "takes belirteci" }); not("takes belirteç", fr(c2[7].t));
  }
  // "yan yana" (8,23): kalemle "vs"; "koyar." (8,59): ? üstüne sarı daire
  elYazisi("vs", { x: 925, y: 560, boyut: 84, renk: KRE, sozcukler: [{ f0: fr(c2[8].t), f1: fr(c2[10].t) }], oge: fazVs });
  not("vs", fr(c2[8].t));
  daire(960, 392, 84, 128, { bas: fr(c2[10].t), sure: 22, oge: faz1 }); not("? daire", fr(c2[10].t));

  // ---------- FAZ B: bu derste ----------
  const TW = 340, TH = 330, TG = 54, TX = (1920 - (4 * TW + 3 * TG)) / 2, TY = 390;
  const tx = (i) => TX + i * (TW + TG), cxT = (i) => tx(i) + TW / 2;
  const etiket = (ad, i, t) => { yazi(ad, { x: cxT(i), y: TY + 84, boyut: 56, aile: "Fredoka", agirlik: 700,
    hizala: "orta", renk: KRE, bas: fr(t), sure: 8, olcek: true, ses: true }); not(ad, fr(t)); };
  const rakam = (n, i, t) => { yazi(n, { x: cxT(i), y: TY + 292, boyut: 170, aile: "Fredoka", agirlik: 700,
    hizala: "orta", renk: SARI, bas: fr(t), sure: 8, olcek: true, ses: true }); not("rakam " + n, fr(t)); };
  // KEY: "karar" (10,19) kutu, "anahtarını" (10,51) etiket; anahtar kalemle 10,25 → 11,25
  kutu(tx(0), TY, TW, TH, { bas: fr(c2[13].t), sure: 18, w: 4.2 }); not("kutu KEY", fr(c2[13].t));
  etiket("KEY", 0, c2[14].t);
  {
    const kx = cxT(0) - 70, ky = TY + 232, ring = [];
    for (let d = 0; d <= 360; d += 20) { const a = d * Math.PI / 180; ring.push([kx + 46 * Math.cos(a), ky + 46 * Math.sin(a)]); }
    ciz(ring, { w: 6.5, renk: KRE, alfa: 0.92, bas: fr(10.25), sure: 14, ad: "anahtar halka" });
    ciz([[kx + 46, ky], [kx + 170, ky]], { duz: true, w: 6.5, renk: KRE, alfa: 0.92, bas: fr(10.25) + 13, sure: 9, ad: "anahtar govde" });
    ciz([[kx + 120, ky], [kx + 120, ky + 38]], { duz: true, w: 6.5, renk: KRE, alfa: 0.92, bas: fr(10.25) + 21, sure: 5, ad: "anahtar dis 1" });
    ciz([[kx + 152, ky], [kx + 152, ky + 30]], { duz: true, w: 6.5, renk: KRE, alfa: 0.92, bas: fr(10.25) + 26, sure: 5, ad: "anahtar dis 2" });
    daire(kx, ky, 24, 24, { bas: fr(10.25) + 30, sure: 8, tur: 1.0 });
    not("anahtar çizimi", fr(10.25));
  }
  // PAIR: "iki" 11,47 kutu · "gelecek" 11,71 rakam 2 · "kalıbını" 12,11 etiket
  kutu(tx(1), TY, TW, TH, { bas: fr(c2[15].t), sure: 18, w: 4.2 }); not("kutu PAIR", fr(c2[15].t));
  rakam("2", 1, c2[16].t); etiket("PAIR", 1, c2[17].t);
  // ITEMS: "dört" 12,99 kutu + rakam 4 · "kökü" 13,23 etiket
  kutu(tx(2), TY, TW, TH, { bas: fr(c2[18].t), sure: 18, w: 4.2 }); not("kutu ITEMS", fr(c2[18].t));
  rakam("4", 2, c2[18].t + 0.1); etiket("ITEMS", 2, c2[19].t);
  // TRAP: "bir" 13,95 kutu + rakam 1 · "tuzağı" 14,19 etiket
  kutu(tx(3), TY, TW, TH, { bas: fr(c2[21].t), sure: 18, w: 4.2 }); not("kutu TRAP", fr(c2[21].t));
  rakam("1", 3, c2[21].t + 0.1); etiket("TRAP", 3, c2[22].t);
  // "görüyoruz." (14,59): her kutuya sarı tik
  [0, 1, 2, 3].forEach((i) => { tik(tx(i) + TW - 46, TY + 52, { bas: fr(c2[23].t) + 4 * i }); });
  not("dört tik", fr(c2[23].t));
  return S;
}

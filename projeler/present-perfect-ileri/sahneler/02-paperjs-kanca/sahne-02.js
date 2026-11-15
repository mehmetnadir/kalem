// Sahne 02 İLERİ — Kural (Present Perfect, 473 kare, t_bas 3,00; cümle 2, çip `Rule`). Yerel kare = round((t − 3,00) × 30).
// Cümle 1 (`Ago` kırmızı alt çizgili) 0. karede yerinde (sahne 01 ile aynı yer, x 140 y 300); içerik 17,94 sn'de biter.
import { sahneKur, RT } from "/projeler/present-perfect-ileri/sahneler/02-paperjs-kanca/kalem-paper.js";

// Kart süresi (12.11, g-29): paket zaman.json son t_son'dan; sabit süre iddiası yanlıştı.
// Göreli yol: sahneler/<sahne>/ → paket kökü (yayında da aynı). Okunamazsa etiket boş kalır.
const SURE_METNI = await fetch(new URL("../../zaman.json", location.href))
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error("HTTP " + r.status))))
  .then((z) => {
    const t = z.sahneler[z.sahneler.length - 1].t_son;
    return t < 60 ? `${Math.round(t)} sec` : `${Math.round(t / 30) / 2} min`;
  })
  .catch((e) => { console.warn("zaman.json süre okunamadı:", e); return ""; });

export const KARE = 473, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Rule", etkin: 1, kayma: 0 });
  const { fr, daire, yazi, cumle, tik, parilti, olay, not, bitis, kutu, svgCiz, ciz, elYazisi } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;
  const FR = (t) => fr(t);

  // --- cümle 1: "Ago varsa, fiil Simple Past." (Caveat 64, x 140, y 300); 0. karede hazır; `Ago` kırmızı alt çizgi
  const c1 = cumle(["Ago", "varsa,", "fiil", "Simple", "Past."].map((s) => ({ s, f: -10 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  {
    const g = c1[0], pts = Array.from({ length: 9 }, (_, i) => { const u = i / 8;
      return [g.x0 - 4 + u * (g.w + 14), 300 + 14 + 3.2 * Math.sin(u * 7) + 5 * u]; });
    ciz(pts, { w: 8, renk: KIR, alfa: 0.95, bas: -30, sure: 20, ses: false, amp: 0.5 });
  }
  not("cümle 1 yerinde (ago kırmızı çizgi)", 0);

  // --- 4,43–9,95: sol el kutusu, 3 madde (tik zamanlı) + küçük saat + süre etiketi
  kutu(120, 390, 590, 390, { bas: FR(4.43), sure: 36, w: 4 }); not("sol kutu", FR(4.43));
  [["formula", 5.11], ["since / for", 6.47], ["Simple Past trap", 8.11]].forEach(([s, t], i) => {
    const y = 495 + i * 105;
    yazi(s, { x: 215, y, boyut: 56, aile: "Fredoka", agirlik: 700, renk: KRE, bas: FR(t), sure: 9, olcek: true, ses: false });
    tik(160, y - 20, { bas: FR(t) + 6 }); not("madde " + s, FR(t));
  });
  await svgCiz("tabler/clock.svg", { kutu: [1000, 120, 200, 200], bas: FR(4.60), sure: 26, azami: 25, w: 4, sesAralik: 2 });
  // 5,00–5,47 el yazısı süre etiketi (zaman.json'dan; "Bu derste" 4,43–4,99 sonrası; anlatımsız etiket; sure 14 kare = 0,47 sn)
  elYazisi(SURE_METNI, { x: 1235, y: 250, boyut: 64, renk: SARI, bas: FR(5.00), sure: 14, ses: true });
  not("saat + süre etiketi", FR(4.60));
  parilti(1215, 130, { bas: FR(5.60), r: 26, periyot: 0, adet: 1 });

  // --- 10,36–15,72: formül kartı (orta) + EN cümle sözcük zamanlı
  kutu(740, 390, 1060, 270, { bas: FR(10.36), sure: 34, w: 4 }); not("formül kartı", FR(10.36));
  {
    const F = 100, Y = 530; let x = 790; const gap = 26;
    const koy = (s, t, o = {}) => { const y = yazi(s, { x, y: Y, boyut: o.boyut || F, aile: "Fredoka", agirlik: 700,
      renk: o.renk || KRE, bas: FR(t), sure: 8, olcek: true, ses: o.ses === true }); x = y.x1 + gap; return y; };
    koy("S", 11.64, { ses: true }); koy("+", 12.28, { renk: IKI });
    koy("have", 12.68, { ses: true }); koy("/", 13.08, { renk: IKI }); koy("has", 13.52, { ses: true });
    koy("+", 13.96, { renk: IKI }); const v = koy("V3", 14.20, { ses: true });
    not("formül S + have / has + V3", FR(11.64));
    // 14,85–15,65 el yazısı `V3 = past participle` (cümle 2 "participle." 14,52–;
    // sure 24 kare = 0,8 sn)
    elYazisi("V3 = past participle", { x: 790, y: 625, boyut: 56, renk: SARI, bas: FR(14.85),
      sure: 24, ses: true });
    not("V3 = past participle", FR(14.85));
    void v;
  }
  {
    const T = { The: 10.36, "formula:": 10.52, subject: 11.64, plus: 12.28, have: 12.68, or: 13.08, has: 13.52,
      past: 14.20, "participle.": 14.52 };
    const kel = [["The", 0, 10.36], ["formula:", 0, 10.52], ["subject", 0, 11.64], ["plus", 0, 12.28],
      ["have", 1, 12.68], ["or", 1, 13.08], ["has", 1, 13.52], ["plus", 1, 13.96],
      ["past", 2, 14.20], ["participle.", 2, 14.52]].map(([s, satir, t]) => ({ s, satir, f: FR(t) }));
    void T;
    const c = cumle(kel, { x: 770, y: 752, boyut: 56, aile: "Fredoka", agirlik: 700, aralik: 78 });
    not("EN cümle", FR(10.36));
    const hv = c[4], hs = c[6], pp = [c[8], c[9]];
    daire((hv.x0 + hv.x1) / 2, hv.y - 20, hv.w / 2 + 8, 31, { bas: FR(12.68) + 6, sure: 18, w: 6 }); not("have daire", FR(12.68));
    daire((hs.x0 + hs.x1) / 2, hs.y - 20, hs.w / 2 + 8, 31, { bas: FR(13.52) + 6, sure: 18, w: 6 }); not("has daire", FR(13.52));
    const px0 = pp[0].x0, px1 = pp[1].x1;
    daire((px0 + px1) / 2, pp[0].y - 20, (px1 - px0) / 2 + 14, 33, { bas: FR(14.20) + 8, sure: 22, w: 6 }); not("past participle daire", FR(14.20));
  }

  // --- 15,97–18,37: üç mini kutu `1 · 2 · 3` (exam roots), teker teker
  [[1, 140, 16.02], [2, 330, 16.60], [3, 520, 17.18]].forEach(([n, x, t]) => {
    kutu(x, 840, 160, 130, { bas: FR(t), sure: 14, w: 4 });
    yazi(String(n), { x: x + 80, y: 938, boyut: 90, aile: "Fredoka", agirlik: 700, hizala: "orta", renk: KRE, bas: FR(t) + 7, sure: 8, olcek: true });
    not("mini kutu " + n, FR(t));
  });
  olay(FR(17.18) + 14, "vurus", 0.8);
  return S;
}

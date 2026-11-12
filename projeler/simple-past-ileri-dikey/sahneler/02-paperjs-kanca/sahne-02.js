// Sahne 02 SIMPLE PAST İLERİ DİKEY — Kanca + kural (326 kare, t_bas 3,00; cümle 2 = 3,71–12,92), 1080x1920.
// Bantlar: içerik 352–1392 (dolu), altyazı 1400–1536 (kalem-paper.js çizer), platform 1536–1920 boş.
// Yerleşim sıfırdan dikey: cümle 1 (352–560) · takvim + saat sırası (600–900) · madde kartı (895–1165) ·
// İngilizce tanım (1210–1392). Her öğe bir kez çizilir, sahne sonuna kadar kalır.
import { sahneKur, RT } from "/projeler/simple-past-ileri-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

// Kart süresi (12.11, g-29): paket zaman.json son t_son'dan; sabit 6 dakika iddiası yanlıştı.
// Göreli yol: sahneler/<sahne>/ → paket kökü (yayında da aynı). Okunamazsa etiket boş kalır.
const SURE_METNI = await fetch(new URL("../../zaman.json", location.href))
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error("HTTP " + r.status))))
  .then((z) => {
    const t = z.sahneler[z.sahneler.length - 1].t_son;
    return t < 60 ? `${Math.round(t)} sec` : `${Math.round(t / 30) / 2} min`;
  })
  .catch((e) => { console.warn("zaman.json süre okunamadı:", e); return ""; });

export const KARE = 326, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, ciz, daire, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu, svgCiz } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep, KIR = RT.kirmizi;

  // --- cümle 1: iki satır Caveat 80 (x 64, taban 450 / 540); 0. karede hazır (sahne 01 ile aynı yer)
  const c1 = cumle([["Ago", 0], ["varsa", 0], ["Perfect", 1], ["yok.", 1]].map(([s, satir]) => ({ s, f: -10, satir })),
    { x: 64, y: 450, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 90 });
  not("cümle 1 yerinde", 0);
  {   // Perfect kırmızı çizili (tuzak çarpısı: kırmızı yalnız burada)
    const g = c1[2];
    ciz([[g.x0 - 6, g.y - 6], [(g.x0 + g.x1) / 2, g.y - 18], [g.x1 + 8, g.y - 30]],
      { w: 11, renk: KIR, alfa: 0.9, bas: -30, sure: 10, uc0: 8, uc1: 12, amp: 0.7, ses: false });
    not("Perfect kırmızı çizili", 0);
  }

  // --- orta: takvim (300 px) sahne başında, saat (300 px) 4,03'te + SURE_METNI (Caveat 96)
  await svgCiz("tabler/calendar.svg", { kutu: [48, 585, 270, 270], bas: 6, sure: 30, azami: 25, w: 4.4, sesAralik: 1 });
  not("takvim eskizi", 6);
  await svgCiz("tabler/clock.svg", { kutu: [370, 585, 270, 270], bas: fr(4.03), sure: 24, azami: 25, w: 4.4, sesAralik: 1 });
  // 4,70 anlatımsız etiket `6 min` (Caveat 104; sağ uç 907): hedef 20 kare (0,67 sn) → 5,37
  elYazisi(SURE_METNI, { x: 700, y: 765, boyut: 104, renk: SARI, bas: fr(4.03) + 20, sure: 20 });
  not("saat + 6 min", fr(4.03));
  parilti(650, 598, { bas: fr(5.2), r: 28, periyot: 0, adet: 1 });
  parilti(335, 590, { bas: 40, r: 26, periyot: 0, adet: 1 });
  parilti(1000, 880, { bas: fr(9.3), r: 26, periyot: 0, adet: 1 });

  // --- 3,71–9,07: madde kartı (y 895–1165), 3 madde + tik (rule 5,55 · time words 6,99 · traps 8,51)
  kutu(48, 890, 984, 292, { bas: fr(3.71), sure: 36, w: 4.4 }); not("madde kartı", fr(3.71));
  [["rule", 5.55, 972], ["time words", 6.99, 1056], ["traps", 8.51, 1140]].forEach(([s, t, y]) => {
    yazi(s, { x: 150, y, boyut: 72, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8, olcek: true, ses: true });
    tik(100, y - 26, { bas: fr(t) + 6 }); not("madde " + s, fr(t));
  });

  // --- 9,72–12,76: tanım Fredoka 64, iki satır (taban 1255 / 1327), sözcük zamanlı
  {
    const kel = [["A", 9.72, 0], ["finished", 9.88, 0], ["action", 10.36, 0], ["at", 10.84, 0], ["a", 11.00, 0],
      ["definite", 11.24, 1], ["time", 11.80, 1], ["in", 12.00, 1], ["the", 12.12, 1], ["past.", 12.44, 1]];
    const e = cumle(kel.map(([s, t, satir]) => ({ s, f: fr(t), satir })),
      { x: 48, y: 1275, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 72 });
    not("tanım başı (A)", e[0].bas);
    const f = e[1], d = daire((f.x0 + f.x1) / 2, f.y - 20, f.w / 2 + 14, 40, { bas: fr(9.88) + 6, sure: 20, w: 10 });
    olay(bitis(d), "tik", 0.5); not("finished daire", d.bas);
    const a = e[5], b = e[6];
    const u = ciz([[a.x0 - 4, a.y + 14], [(a.x0 + b.x1) / 2, a.y + 10], [b.x1 + 6, a.y + 15]],
      { w: 11, renk: RT.vurguDolgu, alfa: 0.85, bas: fr(11.24) + 4, sure: fr(12.12) - fr(11.24) - 4, uc0: 8, uc1: 14, amp: 1.0 });
    not("definite time altı", u.bas);
  }
  return S;
}

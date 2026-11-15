// Sahne 02 İLERİ DİKEY — Kural (Present Perfect, 473 kare, t_bas 3,00; cümle 2, çip `Rule`), 1080x1920.
// Bantlar: içerik 352–1392 (dolu), altyazı 1400–1536 (kalem-paper.js çizer), platform 1536–1920 boş.
import { sahneKur, RT } from "/projeler/present-perfect-ileri-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

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
  const { fr, daire, yazi, elYazisi, cumle, tik, parilti, olay, not, kutu, svgCiz, ciz } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;

  // --- cümle 1: iki satır Caveat 80 (x 64, taban 450 / 540); 0. karede hazır; `Ago` kırmızı alt çizgi
  const c1 = cumle([["Ago", 0], ["varsa,", 0], ["fiil", 1], ["Simple", 1], ["Past.", 1]]
    .map(([s, satir]) => ({ s, f: -10, satir })), { x: 64, y: 450, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 90 });
  {
    const g = c1[0], pts = Array.from({ length: 9 }, (_, i) => { const u = i / 8;
      return [g.x0 - 4 + u * (g.w + 16), 450 + 18 + 3.6 * Math.sin(u * 7) + 6 * u]; });
    ciz(pts, { w: 10, renk: KIR, alfa: 0.95, bas: -30, sure: 20, ses: false, amp: 0.5 });
  }
  not("cümle 1 yerinde (ago kırmızı çizgi)", 0);

  // --- 4,43–9,95: saat (230 px) + süre etiketi; sol kutu: 3 madde (tik zamanlı), Fredoka 64
  await svgCiz("tabler/clock.svg", { kutu: [800, 372, 190, 190], bas: fr(4.60), sure: 26, azami: 25, w: 4.4, sesAralik: 2 });
  // 5,10 anlatımsız süre etiketi ("Bu derste" 4,43–4,99): hedef 14 kare (0,47 sn) → 5,57
  elYazisi(SURE_METNI, { x: 800, y: 622, boyut: 72, renk: SARI, bas: fr(5.10), sure: 14 });
  not("saat + süre etiketi", fr(4.60));
  parilti(990, 385, { bas: fr(5.60), r: 28, periyot: 0, adet: 1 });
  kutu(48, 650, 984, 345, { bas: fr(4.43), sure: 36, w: 4.4 }); not("sol kutu", fr(4.43));
  [["formula", 5.11], ["since / for", 6.47], ["Simple Past trap", 8.11]].forEach(([s, t], i) => {
    const y = 746 + i * 96;
    yazi(s, { x: 160, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 9, olcek: true, ses: false });
    tik(104, y - 22, { bas: fr(t) + 6 }); not("madde " + s, fr(t));
  });

  // --- 10,36–15,72: formül kartı (tam genişlik, iki satır Fredoka 104) + Caveat not
  kutu(48, 1022, 984, 256, { bas: fr(10.36), sure: 34, w: 4.4 }); not("formül kartı", fr(10.36));
  let hv, hs, v3;
  {
    const F = 100, gap = 30;
    const koy = (s, x, y, t, o = {}) => yazi(s, { x, y, boyut: F, aile: "Fredoka", agirlik: 700, renk: o.renk || KRE,
      bas: fr(t), sure: 8, olcek: true, ses: o.ses === true });
    let x = 96; const Y1 = 1112, Y2 = 1218;
    const s0 = koy("S", x, Y1, 11.64, { ses: true }); x = s0.x1 + gap;
    const p1 = koy("+", x, Y1, 12.28, { renk: IKI }); x = p1.x1 + gap;
    hv = koy("have", x, Y1, 12.68, { ses: true }); x = hv.x1 + gap;
    const sl = koy("/", x, Y1, 13.08, { renk: IKI }); x = sl.x1 + gap;
    hs = koy("has", x, Y1, 13.52, { ses: true });
    not("formül S + have / has", fr(11.64));
    const p2 = koy("+", 96, Y2, 13.96, { renk: IKI });
    v3 = koy("V3", p2.x1 + gap, Y2, 14.20, { ses: true }); not("V3", fr(14.20));
    // 14,85 anlatımsız etiket (past participle. 14,52–15,72): hedef 20 kare (0,67 sn) → 15,52
    elYazisi("V3 = past participle", { x: v3.x1 + 44, y: Y2 - 6, boyut: 64, renk: SARI,
      bas: fr(14.85), sure: 20 });
    not("V3 = past participle", fr(14.85));
  }
  daire((hv.x0 + hv.x1) / 2, 1112 - 34, hv.w / 2 + 10, 50, { bas: fr(12.68) + 6, sure: 18, w: 10 }); not("have daire", fr(12.68));
  daire((hs.x0 + hs.x1) / 2, 1112 - 34, hs.w / 2 + 10, 50, { bas: fr(13.52) + 6, sure: 18, w: 10 }); not("has daire", fr(13.52));
  daire((v3.x0 + v3.x1) / 2, 1218 - 34, v3.w / 2 + 10, 50, { bas: fr(14.20) + 8, sure: 22, w: 10 }); not("V3 daire", fr(14.20));

  // --- 15,97–18,37: üç mini kutu `1 · 2 · 3` (exam roots), teker teker (y 1290–1392)
  [[1, 48, 16.02], [2, 408, 16.60], [3, 768, 17.18]].forEach(([n, x, t]) => {
    kutu(x, 1300, 264, 86, { bas: fr(t), sure: 14, w: 4.2 });
    yazi(String(n), { x: x + 132, y: 1370, boyut: 76, aile: "Fredoka", agirlik: 700, hizala: "orta", renk: KRE, bas: fr(t) + 7, sure: 8, olcek: true });
    not("mini kutu " + n, fr(t));
  });
  olay(fr(17.18) + 14, "vurus", 0.8);
  return S;
}

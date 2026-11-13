// Sahne 02 İLERİ — Kanca + formül (380 kare, t_bas 3,00; cümle 2). Yerel kare = round((t − 3,00) ×
// 30).
// Cümle 1 yazısı 0. karede yerinde (sahne 01 ile aynı yer, x 140 y 300); içerik 15,25 sn'de biter.
import { sahneKur,
  RT } from "/projeler/present-continuous-ileri/sahneler/02-paperjs-kanca/kalem-paper.js";

// Kart süresi (12.11, g-29): paket zaman.json son t_son'dan; sabit süre iddiası yanlıştı.
// Göreli yol: sahneler/<sahne>/ → paket kökü (yayında da aynı). Okunamazsa etiket boş kalır.
const SURE_METNI = await fetch(new URL("../../zaman.json", location.href))
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error("HTTP " + r.status))))
  .then((z) => {
    const t = z.sahneler[z.sahneler.length - 1].t_son;
    return t < 60 ? `${Math.round(t)} sec` : `${Math.round(t / 30) / 2} min`;
  })
  .catch((e) => { console.warn("zaman.json süre okunamadı:", e); return ""; });

export const KARE = 380, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, daire, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu, svgCiz } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;

  // --- cümle 1: "YDT'nin -ing tuzağına düşme." (Caveat 64, x 140, y 300); 0. karede hazır
  const c1 = cumle(["YDT'nin", "-ing", "tuzağına", "düşme."].map((s) => ({ s, f: -10 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 yerinde", 0);
  {   // -ing sarı daire titrer (3,00–3,71)
    const g = c1[1], tit = S.oge({ tit: { f0: 0, f1: fr(3.71), g: 2.4 } });
    daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 12, 38, { bas: -30, sure: 20, ses: false,
      oge: tit });
    not("-ing daire titrer", 0);
  }

  // --- 3,71–5,07: FORMÜL etiketi + el kutusu (x 140–1280, y 420–660)
  // 3,71–4,19 sn "Formül" penceresi (eski belirme 3,71)
  elYazisi("FORMÜL", { x: 140, y: 408, boyut: 48, renk: IKI, sozcukler: [{ f0: fr(3.71),
    f1: fr(4.19) }] });
  not("FORMÜL etiketi", fr(3.71));
  kutu(140, 420, 1140, 240, { bas: fr(4.0), sure: 32, w: 4 }); not("formül kutusu", fr(4.0));

  // --- 5,32–10,68: formül tek satır (Fredoka 84, taban y 545), sözcük zamanlı
  {
    const F = "700 84px Fredoka", gap = 18, Y = 545; let x = 160;
    const koy = (s, t, o = {}) => { const y = yazi(s, { x, y: Y, boyut: 84, aile: "Fredoka",
      agirlik: 700, renk: o.renk || KRE,
      bas: fr(t), sure: 8, olcek: true, ses: o.ses !== false }); x = y.x1 + gap; return y; };
    const ayrac = (t) => { const y = yazi("/", { x: x - 6, y: Y, boyut: 84, aile: "Fredoka",
      agirlik: 700, renk: IKI, bas: fr(t), sure: 6 });
      x = y.x1 + gap - 10; };
    const sub = koy("Subject", 5.32);
    // 5,60–6,20 sn: "Subject," sözcüğünün ikinci yarısı (eski belirme 5,60; cümle 6,20 sn'de
    // ilerler)
    elYazisi("özne", { x: sub.x0 + 40, y: 630, boyut: 64, renk: SARI, sozcukler: [{ f0: fr(5.6),
      f1: fr(6.2) }] });
    not("Subject + özne", fr(5.32));
    koy("+", 6.4, { renk: IKI, ses: false });
    koy("am", 6.84); ayrac(7.6); koy("is", 7.68); ayrac(8.24); koy("are",
      8.32); not("am / is / are", fr(6.84));
    koy("+", 9.0, { renk: IKI, ses: false });
    const v = koy("V-ing", 9.40); not("V-ing", fr(9.40));
    const d = daire((v.x0 + v.x1) / 2, Y - 30, v.w / 2 + 10, 52, { bas: fr(9.7), sure: 22 });
    olay(bitis(d), "tik", 0.5); not("V-ing daire", d.bas);
  }

  // --- 10,93–12,37: "Bu derste": saat + süre etiketi
  await svgCiz("tabler/clock.svg", { kutu: [1450, 300, 260, 260], bas: fr(10.93), sure: 26,
    azami: 25, w: 4, sesAralik: 2 });
  // 11,50 sn anlatımsız etiket SURE_METNI: hedef 0,53 sn → 12,03 (cümle: "Bu derste" 10,93–11,49)
  elYazisi(SURE_METNI, { x: 1480, y: 625, boyut: 64, renk: SARI, bas: fr(11.5), sure: 16 });
  not("saat etiketi", fr(10.93));
  parilti(1700, 310, { bas: fr(12.2), r: 26, periyot: 0, adet: 1 });

  // --- 12,37–13,97: üç sınav kökü: 3 el kutusu, rakam + tik
  [[1, 140, 12.37], [2, 440, 12.93], [3, 740, 13.49]].forEach(([n, x, t]) => {
    kutu(x, 730, 260, 220, { bas: fr(t), sure: 16, w: 4 });
    yazi(String(n), { x: x + 130, y: 880, boyut: 130, aile: "Fredoka", agirlik: 700,
      hizala: "orta", renk: KRE, bas: fr(t) + 8, sure: 8, olcek: true });
    tik(x + 215, 775, { bas: fr(t) + 16 }); not("kutu " + n, fr(t));
  });

  // --- 13,97–15,25: bir tuzak: dördüncü kutu, kırmızı ünlem + "1 tuzak" (kırmızı yalnız burada)
  kutu(1040, 730, 380, 220, { bas: fr(13.97), sure: 16, w: 4, renk: KIR }); not("tuzak kutusu",
    fr(13.97));
  yazi("!", { x: 1100, y: 890, boyut: 170, aile: "Fredoka", agirlik: 700, renk: KIR,
    bas: fr(14.22), sure: 8, olcek: true, ses: "vurus" });
  // 14,52 sn anlatımsız etiket "1 tuzak": hedef 0,6 sn → 15,12 (içerik 15,25 sn'de biter)
  elYazisi("1 tuzak", { x: 1170, y: 870, boyut: 64, renk: KIR, bas: fr(14.52), sure: 18 });
  not("1 tuzak", fr(14.52));
  return S;
}

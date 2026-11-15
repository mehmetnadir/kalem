// Sahne 02 SIMPLE PAST İLERİ — Kanca + kural (336 kare, t_bas 3,00; cümle 2 = 4,03–13,24). Yerel
// kare = round((t − 3,00) × 30).
// Cümle 1 yazısı 0. karede yerinde (sahne 01 ile aynı yer, x 140 y 300); içerik 13,24 sn'de (kare
// 307) biter.
import { sahneKur, RT } from "/projeler/simple-past-ileri/sahneler/02-paperjs-kanca/kalem-paper.js";
import { yaziNoktalari } from "/projeler/simple-past-ileri/ortak/kalem-canvas.js";

// Kart süresi (12.11, g-29): paket zaman.json son t_son'dan; sabit 6 dakika iddiası yanlıştı.
// Göreli yol: sahneler/<sahne>/ → paket kökü (yayında da aynı). Okunamazsa etiket boş kalır.
const SURE_METNI = await fetch(new URL("../../zaman.json", location.href))
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error("HTTP " + r.status))))
  .then((z) => {
    const t = z.sahneler[z.sahneler.length - 1].t_son;
    return t < 60 ? `${Math.round(t)} sec` : `${Math.round(t / 30) / 2} min`;
  })
  .catch((e) => { console.warn("zaman.json süre okunamadı:", e); return ""; });

export const KARE = 336, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, ciz, daire, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu, svgCiz } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep, KIR = RT.kirmizi;
  // El yazısı (Caveat 700 tegaki, dalga 5b / K26): not ve etiketler kalemle yazılır. Ortaya hizada
  // genişlik tegaki verisinden ölçülür (yaziNoktalari.gen). Cümle 1 (01'den devralındı) Caveat
  // kalır.
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm, asc: EY.M.ascender,
    boy: boyut, x: 0, taban: 0 }).gen;

  // --- cümle 1: "Ago, Simple Past'in işaretidir." (Caveat 64, x 140, y 300); 0. karede hazır,
  // «Simple Past'in» altı vurgu çizgisi (sahne 01 ile aynı; DUZ3-0210I, eski kırmızı Perfect çizgisi kalktı)
  const c1 = cumle(["Ago,", "Simple", "Past'in", "işaretidir."].map((s) => ({ s, f: -10 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 yerinde", 0);
  {
    const a = c1[1], b = c1[2];
    ciz([[a.x0 - 6, a.y + 20], [(a.x0 + b.x1) / 2, a.y + 19], [b.x1 + 6, a.y + 17]],
      { w: 8, renk: SARI, alfa: 0.95, bas: -30, sure: 10, uc0: 8, uc1: 12, amp: 0.7, ses: false });
    not("Simple Past'in altı vurgu", 0);
  }
  // --- sağda eskiz: takvim (260 px) 0,2 sn'den; saat 4,31'de + süre etiketi
  await svgCiz("tabler/calendar.svg", { kutu: [1340, 190, 260, 260], bas: 6, sure: 30, azami: 25,
    w: 4, sesAralik: 1 });
  not("takvim eskizi", 6);
  await svgCiz("tabler/clock.svg", { kutu: [1650, 210, 200, 200], bas: fr(4.31), sure: 24,
    azami: 25, w: 4, sesAralik: 1 });
  // anlatımsız etiket SURE_METNI (saat çizimi 4,31'de): hedef 16 kare
  elYazisi(SURE_METNI, { x: 1670, y: 480, boyut: 64, renk: SARI, bas: fr(4.31) + 20, sure: 16,
    ses: true });
  not("saat etiketi", fr(4.31));

  // --- 4,03–9,39: el çizimi kutu, 3 madde tik (rule 5,71 · time words 6,91 · traps 8,47)
  kutu(140, 400, 860, 270, { bas: fr(4.03), sure: 34, w: 4 }); not("madde kutusu", fr(4.03));
  [["rule", 5.71, 480], ["time words", 6.91, 565], ["traps", 8.47, 650]].forEach(([s, t, y]) => {
    yazi(s, { x: 220, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8,
      olcek: true, ses: true });
    tik(185, y - 22, { bas: fr(t) + 6 }); not("madde " + s, fr(t));
  });

  // --- 10,04–13,08: tanım Fredoka 56, iki satır (y 800 / 872), sözcük zamanlı
  {
    const kel = [["A", 10.04, 0], ["finished", 10.2, 0], ["action", 10.68, 0], ["at", 11.16, 0],
      ["a", 11.32, 0],
      ["definite", 11.56, 0], ["time", 12.12, 0], ["in", 12.32, 1], ["the", 12.44, 1], ["past.",
        12.76, 1]];
    const e = cumle(kel.map(([s, t, satir]) => ({ s, f: fr(t), satir })),
      { x: 140, y: 800, boyut: 56, aile: "Fredoka", agirlik: 700, aralik: 72 });
    not("tanım başı (A)", e[0].bas);
    const f = e[1], d = daire((f.x0 + f.x1) / 2, f.y - 18, f.w / 2 + 14, 38, { bas: fr(10.2) + 6,
      sure: 20, w: 8 });
    olay(bitis(d), "tik", 0.5); not("finished daire", d.bas);
    const a = e[5], b = e[6];
    const u = ciz([[a.x0 - 4, a.y + 12], [(a.x0 + b.x1) / 2, a.y + 9], [b.x1 + 6, a.y + 13]],
      { w: 9, renk: RT.vurguDolgu, alfa: 0.85, bas: fr(11.56) + 4,
        sure: fr(12.44) - fr(11.56) - 4, uc0: 8, uc1: 14, amp: 1.0 });
    not("definite time altı", u.bas);
  }

  // --- 11,5–12,9: zaman çizgisi (y 960): kapalı kutu sarı + now noktası
  {
    ciz([[140, 960], [700, 958], [1300, 962], [1700, 960]], { w: 4, renk: IKI, alfa: 0.85,
      bas: fr(11.82), sure: 20, uc0: 10, uc1: 20 });
    not("zaman çizgisi", fr(11.82));
    kutu(300, 925, 520, 70, { bas: fr(12.32), sure: 18, w: 8, renk: SARI }); not("kapalı kutu",
      fr(12.32));
    const dn = daire(1300, 960, 14, 14, { bas: fr(12.77), sure: 10, w: 8, tur: 1.1 });
    // `now` nokta bitince (≈12,8) anlatımsız etiket: hedef 12 kare (0,4 sn); «past.» 12,76–13,32;
    // orta x 1300
    elYazisi("now", { x: 1300 - eyGen("now", 64) / 2, y: 1010, boyut: 64, renk: KRE, bas: bitis(dn),
      sure: 12, ses: true });
    not("now noktası", dn.bas);
    parilti(830, 925, { bas: fr(13.02), r: 24, periyot: 0, adet: 1 });
  }
  return S;
}

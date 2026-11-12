// Sahne 02 — Kanca (386 kare, t_bas 3,00; cümle 2 = 3,31–15,45). Yerel kare = round((t − 3,00) ×
// 30).
// Cümle 1 (Her sabah yedide kalkarım.) sahne 01'de söylendi; yazı sahne başında hazır belirir (kare
// 0–9).
import { sahneKur,
  RT } from "/projeler/simple-present-temel/sahneler/02-paperjs-kanca/kalem-paper.js";
import { kupur, kadro } from "./stil/kupur.js";

// Kart süresi (12.11, g-29): paket zaman.json son t_son'dan; sabit 6 dakika iddiası yanlıştı.
// Göreli yol: sahneler/<sahne>/ → paket kökü (yayında da aynı). Okunamazsa etiket boş kalır.
const SURE_METNI = await fetch(new URL("../../zaman.json", location.href))
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error("HTTP " + r.status))))
  .then((z) => {
    const t = z.sahneler[z.sahneler.length - 1].t_son;
    return t < 60 ? `${Math.round(t)} sec` : `${Math.round(t / 30) / 2} min`;
  })
  .catch((e) => { console.warn("zaman.json süre okunamadı:", e); return ""; });

export const KARE = 386, T_BAS = 3.0;
// Kâğıt küpür kadro (seri kimliği "simple-present"; FNV-1a 32 bit). Kadro tohumu sabit, YDT 16–18.
const TOHUM = 2826477417, YAS = 17, BAS_H = 60;
// Sol alt figürler: ayak tabanı künye bandının (y 1002) 60 px üstünde; boy %10 küçük.
const AYAK = 940, BAS_K = 54;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0 });
  const { fr, ciz, daire, ok, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  // geçiş karesi: çizimler bundan sonra
  const GB = 12;

  // --- cümle 1 (Caveat 64, x 140, y 300): sahne başında hazır, 0–0,4 sn'de belirir
  const c1 = cumle(["Her", "sabah", "yedide", "kalkarım."].map((s, i) => ({ s, f: i * 3 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 başı (Her)", c1[0].bas); not("kalkarım.", c1[3].bas);

  // --- küpür kadro: öğrenci (k9) sahne başında, öğretmen (sabit) cümle 2 başında,
  // ikinci öğrenci (k11) "Altı dakikada" anında yapışır. Baş yüksekliği 60 px.
  const K = kadro(12, TOHUM);
  const OGRT = { ...K[1], ogretmen: true, sac: 5, aks: 0, etek: false, ten: 1, ust: 4, alt: 1,
    sacRenk: 0 };
  kupur(S, { x: 1245, y: 660, h: BAS_H, kimlik: K[9], yas: YAS, duygu: "notr", bas: GB,
    sure: 46 });
  not("öğrenci k9 (kalkış) yapışır", GB);
  kupur(S, { x: 975, y: AYAK, h: BAS_K, kimlik: OGRT, duygu: "dogru", bas: 34, sure: 46 });
  not("öğretmen yapışır", 34);
  kupur(S, { x: 780, y: AYAK, h: BAS_K, kimlik: K[11], yas: YAS, duygu: "sevinc", bas: fr(10.65),
    sure: 46 });
  not("öğrenci k11 (6 dk) yapışır", fr(10.65));
  await S.svgCiz("coco/bed.svg", { kutu: [1410, 400, 420, 290], bas: GB + 20, sure: 44, azami: 30,
    w: 3.6, sesAralik: 4 });
  not("yatak çizimi başı", GB + 20);
  const sa = await S.svgCiz("coco/clock.svg", { kutu: [1560, 130, 220, 220], bas: GB + 50,
    sure: 30, azami: 25, w: 3.6, sesAralik: 3 });
  not("saat çizimi başı", GB + 50);
  ciz([[1100, 662], [1300, 658], [1560, 664], [1830, 660]], { w: 3, renk: IKI, alfa: 0.75,
    bas: GB + 40, sure: 30, uc0: 10, uc1: 30 });
  parilti(1790, 150, { bas: GB + 84, r: 24, periyot: 150, adet: 3 });

  // --- 5,71–7,77: kalkar · gider · yapar (sözcük zamanlı) + sarı daire; not geniş zaman
  {
    const kel = [["kalkar,", 5.71], ["gider,", 6.47], ["yapar.", 7.07]];
    let x = 150; const e = kel.map(([t, f]) => { const w = yazi(t, { x, y: 420, boyut: 64,
      aile: "Fredoka", agirlik: 700, bas: fr(f), sure: 8 }); x = w.x1 + 64; return w; });
    kel.forEach((_, i) => {
      const g = e[i], d = daire((g.x0 + g.x1) / 2, g.y - 22, g.w / 2 + 10, 38,
        { bas: fr(kel[i][1]) + 6, sure: 22, egim: -0.04 * (i + 1) });
      olay(bitis(d), "tik", 0.5); not("daire " + g.str, d.bas);
    });
    not("kalkar başı", e[0].bas);
  }

  // --- 7,78–10,42: not "geniş zaman" ⇄ "Simple Present" (el oku, iki yönlü)
  {
    // anlatımsız etiket: hedef 20 kare (0,67 sn), el yazısı
    const y = 540, a = elYazisi("geniş zaman", { x: 140, y, boyut: 64, renk: RT.murekkep,
      bas: fr(7.78),
      sure: 20 });
    not("not geniş zaman", a.bas);
    const ar = ok([a.x1 + 22, y - 20], [a.x1 + 132, y - 20], { bas: fr(8.7), sure: 18, w: 7,
      cift: true, uzun: 20, bukum: 0.06 });
    not("ok geniş zaman ⇄", ar.bas);
    const s = yazi("Simple Present", { x: a.x1 + 156, y, boyut: 56, aile: "Fredoka", agirlik: 700,
      renk: SARI, bas: fr(9.3), sure: 14, olcek: true, ses: true });
    not("Simple Present yazılır", s.bas);
    parilti(s.x1 + 20, y - 62, { bas: fr(10.1), r: 22, periyot: 160, adet: 3 });
  }

  // --- 10,65–15,45: el kutusu, saat (6 min), 3 madde
  {
    kutu(1060, 700, 760, 280, { bas: fr(10.65) - 4, sure: 36 }); not("kutu çizimi", fr(10.65) - 4);
    await S.svgCiz("tabler/clock.svg", { kutu: [1096, 722, 76, 76], bas: fr(10.8), sure: 20,
      azami: 25, w: 3.4, sesAralik: 3 });
    elYazisi(SURE_METNI, { x: 1196, y: 782, boyut: 56, renk: SARI, bas: fr(10.8) + 14,
      sure: 14 }); not("saat + 6 min", fr(10.8));
    parilti(1176, 724, { bas: fr(11.2), r: 22, periyot: 170, adet: 3 });
    const m = [["form", 11.61, 845], ["time expressions", 12.41, 900], ["uses", 13.77, 955]];
    for (const [s, t, y] of m) {
      yazi(s, { x: 1140, y, boyut: 44, aile: "Fredoka", agirlik: 700, renk: RT.murekkep,
        bas: fr(t), sure: 8 });
      tik(1108, y - 12, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

// Sahne 03 — Örnek 1/3 (Paper.js, 543 kare, t_bas 15,31; cümle 3). 02-03 YDT temel.
// Yerel kare = round((t − 15,31) × 30). Sözcük zamanları ortak/anlatim/sozcukler.json'dan okunur.
// Kök: "We are leaving for the airport at 9." — tek kart, uçak simgesi, PLAN, are + leaving.
import { sahneKur,
  RT } from "/projeler/02-03-ydt-temel/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 543, T_BAS = 15.31;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, kutu, yazi, elYazisi, cumle, altCizgi, parilti, olay, not, bitis,
    svgCiz } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const f0 = (t) => Math.max(12, fr(t));            // ilk 12 kare durgun
  const s3 = S.sozcukler(3);   // 0 Birinci · 1 örnek. · 2 We … 9 nine. · 10–13 TR · 14–20 Plan … biziz. · 21–28 Kişisel … kullanır. · 29–34 Yapı … leaving.

  // --- 15,86 Birinci: büyük el çizimi daire içinde 1 (kartın sol üstünde)
  const d1 = daire(196, 176, 56, 54, { bas: f0(s3[0].t), sure: 22, a0: -2.6 });
  olay(bitis(d1), "tik", 0.5); not("daire 1 çizimi (Birinci)", d1.bas);
  yazi("1", { x: 196, y: 210, hizala: "orta", boyut: 90, aile: "Fredoka", agirlik: 700,
    bas: f0(s3[0].t) + 8, sure: 10, olcek: true });

  // --- 16,34 örnek.: tek kart (el kutusu, 0,87 sn; 'We' 17,07'den önce biter)
  kutu(140, 250, 1640, 450, { bas: fr(s3[1].t), sure: 26, w: 4 });
  not("kart kutusu (örnek.)", fr(s3[1].t));

  // --- 17,07–19,40: kök, Fredoka 96, sözcük sözcük (We are leaving / for the airport at 9.)
  const kel = s3.slice(2, 10).map((k, i) => ({ s: i === 7 ? "9." : k.s, f: k.f, satir: i < 3 ? 0 : 1 }));
  const cz = cumle(kel, { x: 230, y: 430, boyut: 96, aile: "Fredoka", agirlik: 700, aralik: 125 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (We)", cz[0].bas);
  const cevre = (a, b, bas, ad, ek = 0) => {          // a..b sözcük dizisine sarı daire
    const x0 = cz[a].x0, x1 = cz[b].x1, y = cz[a].y + 16;   // halka yerine el altçizgisi (13.11 QA)
    const d = ciz([[x0 - 2, y], [x1 + 2, y - 1]], { duz: true, w: 8, renk: SARI, alfa: 0.9, bas, sure: 14,
      uc0: 6, uc1: 14, amp: 1.2, tur: "isaret", ad });
    olay(bitis(d), "tik", 0.5); not(ad, d.bas); return d;
  };
  // 18,43 at: `at 9.` sarı odak
  cevre(6, 7, fr(s3[8].t), "at 9 daire (at)");

  // --- 17,95 airport: uçak simgesi kalemle (sağ yarı)
  await svgCiz("tabler/plane.svg", { kutu: [1180, 290, 480, 380], bas: fr(s3[7].t), sure: 40,
    azami: 10, w: 4.4, sesAralik: 2 });
  not("uçak çizimi başı (airport)", fr(s3[7].t));

  // --- 19,72 Saat dokuzda havalimanına çıkıyoruz.: Türkçe çeviri (el yazısı 48 ikincil, y 785)
  {
    const tr = s3.slice(10, 14), dizgi = ["Saat", "9'da", "havalimanına", "çıkıyoruz."];
    let tx = 140; const tz = [];
    tr.forEach((k, i) => {
      const f1 = i < 3 ? tr[i + 1].f : k.f1;     // kısa pencere sonraki sözcüğün başına dek uzar
      const q = elYazisi(dizgi[i], { x: tx, y: 785, boyut: 48, renk: IKI, sozcukler: [{ f0: k.f,
        f1 }] });
      tx = q.x1 + 0.3 * 48; tz.push(q);
    });
    not("Türkçe çeviri (Saat)", tz[0].bas);
  }

  // --- 22,52 Plan: PLAN etiketi (sarı) · 23,56 saat: saat simgesi
  {
    const q = elYazisi("PLAN", { x: 1130, y: 900, boyut: 120, renk: SARI,
      sozcukler: [{ f0: fr(s3[14].t), f1: fr(s3[15].t) }] });
    not("PLAN etiketi (Plan)", q.bas);
    ciz([[1124, 925], [1380, 920]], { duz: true, w: 7, renk: SARI, alfa: 0.85, bas: fr(s3[15].t),
      sure: 14, uc0: 8, uc1: 14, amp: 0.8, tur: "isaret", ad: "PLAN altçizgi" });
    await svgCiz("tabler/clock.svg", { kutu: [1450, 780, 160, 160], bas: fr(s3[16].t), sure: 24,
      azami: 8, w: 4, sesAralik: 2 });
    not("saat simgesi (saat)", fr(s3[16].t));
  }

  // --- 24,60 Planı: `We` sarı daire (planı yapan biziz)
  cevre(0, 0, fr(s3[18].t), "We daire (Planı)");

  // --- 27,80 şimdiki: `are leaving` sarı daire (şimdiki zaman)
  cevre(1, 2, fr(s3[26].t), "are leaving daire (şimdiki)", 2);

  // --- 29,48 Yapı: formül kartı (be + V-ing / are + leaving), sol altta
  {
    const kx = 140, ky = 815, F = { boyut: 54, aile: "Fredoka", agirlik: 700 }, y1 = ky + 72,
      y2 = ky + 148, fnt = "700 54px Fredoka";
    kutu(kx, ky, 760, 170, { bas: fr(s3[29].t), sure: 22, w: 4 }); not("formül kartı (Yapı)", fr(s3[29].t));
    // 29,96 bildiğimiz · 30,52 yapı: — satır 1: be + V-ing
    const b = yazi("be", { ...F, x: kx + 50, y: y1, bas: fr(s3[30].t), sure: 10, olcek: true, ses: true });
    not("be (bildiğimiz)", b.bas);
    const p = yazi("+", { ...F, x: b.x1 + 28, y: y1, bas: fr(s3[30].t) + 10, sure: 8, olcek: true });
    const v = yazi("V", { ...F, x: p.x1 + 28, y: y1, bas: fr(s3[31].t), sure: 8, olcek: true });
    yazi("-ing", { ...F, x: v.x1 + 4, y: y1, bas: fr(s3[31].t) + 6, sure: 10, olcek: true, renk: SARI,
      ses: true }); not("V-ing (yapı:)", fr(s3[31].t));
    // 31,20 are: `are` yakın çekim (kutu) + satır 2 · 31,72 artı · 32,36 leaving.
    const a = cz[1], k1 = ciz([[a.x0 - 2, a.y + 16], [a.x1 + 2, a.y + 15]], { duz: true, w: 8, renk: SARI, alfa: 0.9,
      bas: fr(s3[32].t), sure: 14, uc0: 6, uc1: 14, amp: 1.2, tur: "isaret", ad: "are altçizgi" });   // kutu yerine altçizgi (13.11 QA)
    olay(bitis(k1), "tik", 0.5); not("are yakın çekim kutusu (are)", fr(s3[32].t));
    const r = yazi("are", { ...F, x: kx + 50, y: y2, bas: fr(s3[32].t), sure: 10, olcek: true, ses: true });
    not("are (artı)", r.bas);
    const q = yazi("+", { ...F, x: r.x1 + 28, y: y2, bas: fr(s3[33].t), sure: 8, olcek: true });
    const l = yazi("leav", { ...F, x: q.x1 + 28, y: y2, bas: fr(s3[34].t), sure: 10, olcek: true });
    yazi("ing", { ...F, x: l.x1 + 2, y: y2, bas: fr(s3[34].t) + 4, sure: 10, olcek: true, renk: SARI,
      ses: true }); not("leav-ing (leaving.)", fr(s3[34].t));
    parilti(a.x1 + 26, a.y - 90, { bas: fr(s3[32].t) + 8, r: 22 });   // are kutusunun köşesi; 22 karede söner, SON'dan önce biter
  }
  return S;
}

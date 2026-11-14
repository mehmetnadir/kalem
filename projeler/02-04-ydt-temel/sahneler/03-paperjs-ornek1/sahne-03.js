// Sahne 03 — Örnek 1/3 (Paper.js, 721 kare, t_bas 20,22; cümle 3). 02-04 YDT temel.
// Yerel kare = round((t − 20,22) × 30). Sözcük zamanları ortak/anlatim/sozcukler.json'dan okunur.
// Sol kart: She wears her coat in the winter. (mont, GENERAL) · sağ kart: She is wearing her
// pink T-shirt today. (tişört, RIGHT NOW). Ölçü mantıksal px (1920 tabanı) → u(); sabit px yok.
import { sahneKur,
  RT } from "/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 721, T_BAS = 20.22;

// Cümle 3 parça 4 (EN "She is wearing her pink T-shirt today.") sozcukler.json'da YOK (açık).
// Başlar: cumle-3.wav (md5 4658616c…) faster-whisper turbo sözcük zamanı + 40 ms RMS zarfı, parça
// penceresi 11,63–14,35 sn (sureler.json); küresel sn = 20,77 + yerel. Ölçüm 14.11 (RAPOR.md).
const EN2 = [["She", 32.41], ["is", 32.63], ["wearing", 32.77], ["her", 33.07], ["pink", 33.35],
  ["T-shirt", 33.63], ["today.", 34.13]];

// Giysi çizimleri: birim ızgara (mont 100×120, tişört 100×90); n = darbe noktaları, egri = yumuşak.
const MONT = [
  { n: [[40, 4], [20, 10], [6, 70], [17, 74], [26, 34], [23, 116], [50, 117]] },
  { n: [[60, 4], [80, 10], [94, 70], [83, 74], [74, 34], [77, 116], [50, 117]] },
  { n: [[40, 4], [50, 9], [60, 4]], egri: true },
  { n: [[40, 4], [44, 21], [50, 34]], egri: true },
  { n: [[60, 4], [56, 21], [50, 34]], egri: true },
  { n: [[50, 34], [50, 116]] },
  { n: [[28, 96], [38, 95]] }, { n: [[62, 95], [72, 96]] },      // cep düğmeye değmez (QA 1)
  { daire: [44, 48, 2.6] }, { daire: [44, 64, 2.6] }, { daire: [44, 80, 2.6] },
];
const TISORT = [
  { n: [[37, 4], [14, 12], [0, 36], [14, 46], [24, 37], [24, 88], [76, 88], [76, 37], [86, 46],
    [100, 36], [86, 12], [63, 4]] },
  { n: [[37, 4], [50, 14], [63, 4]], egri: true },
  { n: [[14, 12], [24, 37]] }, { n: [[86, 12], [76, 37]] },
];

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, kutu, elYazisi, cumle, altCizgi, olay, not, bitis, genislik } = S;
  const u = (n) => n * P.view.size.width / 1920;           // mantıksal px → px (oran)
  const VURGU = RT.vurgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const s3 = S.sozcukler(3);
  // 0 Birinci · 1 örnek. · 2 Fiil · 3 aynı: · 4 wear. · 5–11 She … winter. · 12–14 Kışın montunu
  // giyer. · 15–17 Her kış böyle. · 18–21 Genel durum: geniş zaman. · 22–25 Bugün … giyiyor. ·
  // 26–32 Bu yalnız … oluyor. · 33–34 Şimdiki zaman: · 35 is · 36 wearing.
  const f = (i) => s3[i].f;

  // --- yerleşim: iki kart yan yana (AL 120–1800), içerik sol hizalı
  const KX = [u(120), u(980)], KY = u(230), KW = u(820), KH = u(600), PAD = u(50);
  const IC = KW - 2 * PAD, EN_Y = KY + u(350), ARA = u(82), TR_Y = KY + u(530);
  const LX = u(330), LY = KY + u(165);                      // etiket: simgenin sağı
  const sigdir = (azami, aile, metinler, alan) => Math.min(azami, ...metinler.map((s) =>
    azami * alan / genislik(s, `700 ${azami}px ${aile}`)));
  const SAT = ["She wears her coat", "in the winter.", "She is wearing her", "pink T-shirt today."];
  const ENB = sigdir(u(64), "Fredoka", SAT, IC);
  const TR = ["Kışın montunu giyer.", "Bugün pembe tişörtünü giyiyor."];
  const TRB = sigdir(u(46), "Caveat", TR, IC * 0.94);
  const ETB = sigdir(u(84), "Caveat", ["GENERAL", "RIGHT NOW"], (KW - LX - PAD) * 0.94);
  const fnt = `700 ${ENB}px Fredoka`;

  // el çizimi: birim ızgaradaki darbeler kutuya oturur, uzunluğa göre pay alarak sırayla çizilir
  function elCizim(darbeler, [bx, by, bw, bh], [UW, UH], o) {
    const k = Math.min(bw / UW, bh / UH), ox = bx + (bw - UW * k) / 2, oy = by + (bh - UH * k) / 2;
    const yer = (q) => [ox + q[0] * k, oy + q[1] * k];
    const uz = darbeler.map((d) => (d.daire ? 2 * Math.PI * d.daire[2] : d.n.slice(1)
      .reduce((s, q, i) => s + Math.hypot(q[0] - d.n[i][0], q[1] - d.n[i][1]), 0)) * k);
    const ag = uz.map((l) => 4 + Math.pow(l, 0.75)), top = ag.reduce((s, a) => s + a, 0);
    let cur = o.bas;
    darbeler.forEach((d, i) => {
      const sr = Math.max(3, o.sure * ag[i] / top), ses = i % 3 === 0 ? undefined : false;
      if (d.daire) {
        // daire() "tur" alanını dönüş sayısı sayar; düğme kendi noktalarıyla çizilir (tur = kutu türü)
        const [cx, cy] = yer(d.daire), r = d.daire[2] * k;
        const pts = Array.from({ length: 19 }, (_, j) => { const a = -2.3 + j * 2.2 * Math.PI / 18;
          return [cx + Math.cos(a) * r, cy + Math.sin(a) * r]; });
        ciz(pts, { duz: true, bas: cur, sure: Math.max(5, sr * 1.4), w: o.w * 0.9, renk: MUR,
          alfa: 0.92, amp: 0.3, uc0: 2, uc1: 3, tur: "cizim", ad: o.ad, ses: false });
      } else {
        ciz(d.n.map(yer), { duz: !d.egri, w: o.w, amp: 0.8, alfa: 0.92, bas: cur, sure: sr * 1.4,
          uc0: 8, uc1: 16, ses, tur: "cizim", ad: o.ad });
      }
      cur += sr;
    });
    return cur;
  }
  // öbek altçizgisi (odak / yakın çekim): halka yerine el altçizgisi (13.11 QA); nokta hariç
  const yalin = (z) => z.x0 + genislik(z.str.replace(/[.,:]$/, ""), fnt);
  function alti(x0, x1, y, bas, ad) {
    const d = ciz([[x0 - u(2), y], [x1 + u(2), y - u(1)]], { duz: true, w: u(8), renk: VURGU,
      alfa: 0.9, bas, sure: 14, uc0: u(6), uc1: u(14), amp: 1.2, tur: "isaret", ad });
    olay(bitis(d), "tik", 0.5); not(ad, d.bas); return d;
  }
  const altY = (z) => z.y + ENB * 0.3;                      // y/g kuyruğunun altında (QA 1)

  // --- 20,77 Birinci: sol kart · 22,13 Fiil: sağ kart (kartlar "wear." bitmeden hazır)
  kutu(KX[0], KY, KW, KH, { bas: f(0), sure: 26, w: u(4) }); not("sol kart (Birinci)", f(0));
  kutu(KX[1], KY, KW, KH, { bas: f(2), sure: 30, w: u(4) }); not("sağ kart (Fiil)", f(2));

  // --- 24,22–26,54 She wears her coat / in the winter.: sol kart, sözcük sözcük + karaoke
  const cz1 = cumle(s3.slice(5, 12).map((k, i) => ({ s: k.s, f: k.f, satir: i < 4 ? 0 : 1 })),
    { x: KX[0] + PAD, y: EN_Y, boyut: ENB, aile: "Fredoka", agirlik: 700, aralik: ARA });
  altCizgi(cz1, { tut: 30, w: u(7) }); not("sol cümle (She)", cz1[0].bas);

  // --- 25,02 coat: mont kalemle (sol kartın sol üstü)
  const mBit = elCizim(MONT, [KX[0] + PAD, KY + u(30), u(220), u(220)], [100, 120],
    { bas: f(8), sure: 42, w: u(4.4), ad: "mont" });
  not("mont çizimi (coat)", f(8)); not("mont bitti", mBit);

  // --- 26,79 Kışın montunu giyer.: TR çeviri, el yazısı ikincil, sözcük penceresiyle
  const tr1 = elYazisi(TR[0], { x: KX[0] + PAD, y: TR_Y, boyut: TRB, renk: IKI,
    sozcukler: [12, 13, 14].map((i) => ({ f0: f(i), f1: i < 14 ? f(i + 1) : s3[i].f1 })) });
  not("TR 1 (Kışın)", tr1.bas);

  // --- 28,55 Her kış: odak `in the winter`
  alti(cz1[4].x0, yalin(cz1[6]), altY(cz1[4]), f(15), "odak in the winter (Her kış)");

  // --- 30,31 Genel: GENERAL (Caveat) · 31,35 geniş zaman: etiket altçizgisi
  const g1 = elYazisi("GENERAL", { x: KX[0] + LX, y: LY, boyut: ETB, renk: MUR,
    sozcukler: [{ f0: f(18), f1: f(20) }] });
  not("GENERAL (Genel)", g1.bas);
  alti(g1.x0, g1.x1, LY + ETB * 0.22, f(20), "GENERAL altçizgi (geniş)");

  // --- 32,41–34,55 She is wearing her / pink T-shirt today.: sağ kart, sözcük sözcük + karaoke
  const cz2 = cumle(EN2.map(([s, t], i) => ({ s, f: fr(t), satir: i < 4 ? 0 : 1 })),
    { x: KX[1] + PAD, y: EN_Y, boyut: ENB, aile: "Fredoka", agirlik: 700, aralik: ARA });
  altCizgi(cz2, { tut: 30, w: u(7) }); not("sağ cümle (She)", cz2[0].bas);

  // --- 33,63 T-shirt: tişört kalemle (sağ kartın sol üstü)
  const tBit = elCizim(TISORT, [KX[1] + PAD, KY + u(40), u(240), u(200)], [100, 90],
    { bas: fr(33.63), sure: 36, w: u(4.4), ad: "tisort" });
  not("tişört çizimi (T-shirt)", fr(33.63)); not("tişört bitti", tBit);

  // --- 35,37 Bugün pembe tişörtünü giyiyor.: TR çeviri
  const tr2 = elYazisi(TR[1], { x: KX[1] + PAD, y: TR_Y, boyut: TRB, renk: IKI,
    sozcukler: [22, 23, 24, 25].map((i) => ({ f0: f(i), f1: i < 25 ? f(i + 1) : s3[i].f1 })) });
  not("TR 2 (Bugün)", tr2.bas);

  // --- 38,17 bugüne: odak `today`
  alti(cz2[6].x0, yalin(cz2[6]), altY(cz2[6]), f(28), "odak today (bugüne)");

  // --- 39,05 konuşma anında: RIGHT NOW · 41,45 Şimdiki zaman: etiket altçizgisi
  const g2 = elYazisi("RIGHT NOW", { x: KX[1] + LX, y: LY, boyut: ETB, renk: MUR,
    sozcukler: [{ f0: f(30), f1: f(31) }, { f0: f(31), f1: f(32) + 8 }] });
  not("RIGHT NOW (konuşma)", g2.bas);
  alti(g2.x0, g2.x1, LY + ETB * 0.22, f(33), "RIGHT NOW altçizgi (Şimdiki)");

  // --- 42,81 is: yakın çekim `is` · 43,05 wearing.: `-ing` (SON 708'den önce biter)
  alti(cz2[1].x0, yalin(cz2[1]), altY(cz2[1]), f(35), "yakın çekim is (is)");
  const w2 = cz2[2];
  alti(w2.x0 + genislik("wear", fnt), w2.x1, altY(w2), f(36), "ing altçizgi (wearing)");
  return S;
}

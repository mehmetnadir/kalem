// Sahne 02 — Kanca (484 kare, t_bas 3,00; cümle 2 = parçalar 3,71–8,35 · 8,50–11,62 · 11,77–18,73).
// Zamanlar KÜRESEL sn (sozcukler.json); yerel kare = round((t − 3,00) × 30).
// Cümle 1 (Kaybettim, kapıda kaldım.) sahne 01'de söylenir (1,00–3,16); sahne 01 uçuşuyla (140, 300)'e taşınır,
// burada 0. kareden hazır durur (sahne 01 sonundaki yerle aynı: Caveat 64), ilk 12 kare durgun.
import { sahneKur, RT, renkCoz }
  from "/projeler/present-perfect-temel/sahneler/02-paperjs-kanca/kalem-paper.js";
import { zamanHatti, aralik, baslangic, tren } from "./stil/zamanhatti.js";

export const KARE = 484, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { fr, ciz, daire, ok, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis } = S;
  const SARI = RT.vurgu, KRE = RT.murekkep, IKI = RT.ikincil;
  const GB = 12;                                                   // geçiş karesi: çizimler bundan sonra başlar
  // el yazısı sözcük pencereleri (cümle 2, yerel kare)
  const CS = S.sozcukler(2);
  const pen = (ilk, adet) => { const i = CS.findIndex((w) => w.s === ilk);
    return CS.slice(i, i + adet).map((w) => ({ f0: w.f, f1: w.f1 })); };

  // --- cümle 1: Caveat 64 (x 140, y 300); kare 0'da hazır (bas −8: maske açık, tam görünür)
  const c1 = cumle(["Kaybettim,", "kapıda", "kaldım."].map((s) => ({ s, f: -8 })),
    { x: 140, y: 300, boyut: 64, aile: "Caveat", agirlik: 700 });
  not("cümle 1 hazır (kare 0)", 0);

  // --- sağ eskiz: ev + kapıda duran figür + el çizimi anahtar (3 darbe)
  const figOge = S.oge({ nefes: { bas: 150, cx: 1280, cy: 640 } });
  await S.svgCiz("tabler/home.svg", { kutu: [1450, 330, 310, 310], bas: GB, sure: 28, azami: 25, w: 4,
    sesAralik: 2 });
  await S.svgCiz("open-peeps/standing-4.svg", { kutu: [1160, 100, 240, 540], bas: GB + 6, sure: 44,
    azami: 60, yuz: 3, w: 3.2, oge: figOge, sesAralik: 5 });
  ciz([[1130, 643], [1300, 639], [1500, 644], [1790, 641]],
    { w: 3, renk: IKI, alfa: 0.75, bas: 40, sure: 30, uc0: 10, uc1: 30 });
  not("ev + figür çizimi başı", GB);
  {   // anahtar: halka + gövde + diş (el çizimi, kütüphanede anahtar yok) — evin sol üstünde havada
    const cx = 1500, cy = 262, pts = [];
    for (let a = 0; a <= 360; a += 24) pts.push([cx + 17 * Math.cos(a * Math.PI / 180), cy + 17 * Math.sin(a * Math.PI / 180)]);
    const k1 = ciz(pts, { w: 4.4, bas: 58, sure: 12, uc0: 4, uc1: 4, amp: 0.4 });
    const k2 = ciz([[cx + 18, cy], [cx + 60, cy + 2], [cx + 104, cy + 1]], { w: 4.4, bas: bitis(k1), sure: 10, amp: 0.5 });
    ciz([[cx + 84, cy + 2], [cx + 85, cy + 20], [cx + 97, cy + 20], [cx + 97, cy + 2]], { w: 4.4, bas: bitis(k2), sure: 8, amp: 0.3,
      duz: true });
    not("anahtar çizimi başı", k1.bas);
    parilti(cx + 52, cy - 34, { bas: bitis(k2) + 14, r: 22, periyot: 160, adet: 2 });
  }

  // --- 4,27 kaybettim sarı daire; 5,39 not `geçmişte oldu`
  {
    const g = c1[0], d = daire((g.x0 + g.x1) / 2 + 2, g.y - 22, g.w / 2 + 8, 34, { bas: fr(4.27), sure: 24, egim: -0.04 });
    olay(bitis(d), "tik", 0.5); not("kaybettim daire", d.bas);
    // 5,39–6,51 «geçmişte oldu,» (pencere: 5,39–5,79 · 5,87–6,51)
    const a = elYazisi("geçmişte oldu", { x: 140, y: 372, boyut: 48, renk: IKI,
      sozcukler: pen("geçmişte", 2) });
    not("not geçmişte oldu", a.bas);
  }

  // --- 6,60–8,35: metro hattı past ● ━━ ● now ┈ will (düz zaman çizgisinin yerine; aynı bilgi);
  // `sonucu şimdi bizimle`; vagon «I» geçmişten şimdiye taşınır;
  // since/for hattı 14,7 sn'de kullanır.
  const HY = 590;
  const hat = zamanHatti(S, { x: 380, y: HY, w: 700, t0: 0, t1: 10, bas: fr(6.6), sure: 32,
    duraklar: [{ ad: "past", t: 2, tur: "gecmis" }, { ad: "now", t: 6, tur: "simdi" },
      { ad: "will", t: 8.5, tur: "gelecek" }] });
  {
    const pa = hat.durak("past"), no = hat.durak("now");
    // 6,91–8,35 «sonucu şimdi bizimle.» (pencere: 6,91–7,31 · 7,39–7,63 · 7,71–8,35);
    // hattın üstünde
    const b = elYazisi("sonucu şimdi bizimle", { x: 760, y: 472, boyut: 48, renk: SARI,
      sozcukler: pen("sonucu", 3) });
    ok([(b.x0 + b.x1) / 2 + 20, 490], [no.x, HY - 44], { bas: fr(7.71), sure: 14, w: 6, uzun: 18,
      bukum: 0.12 });
    not("not sonucu şimdi bizimle", b.bas);
    // vagon: öznesi «I» (cümle: I have lost the key); 7,45'te geçmişten şimdiye
    const bv = fr(7.45), sv = 36;
    tren(hat, "past", "now", { bas: bv, sure: sv });
    S.dinamik((f, g) => {
      const u = (f - bv) / sv; if (u < 0) return;
      const al = 1 - S.kis((f - bv - sv - 8) / 12); if (al <= 0) return;
      g.opacity = al * S.kis((f - bv) / 6);
      g.addChild(new S.P.PointText({ point: [pa.x + (no.x - pa.x) * S.yumus(u), HY + 11],
        content: "I", justification: "center", fontFamily: "Caveat", fontWeight: "bold",
        fontSize: 34, fillColor: renkCoz(KRE), insert: false }));
    });
  }

  // --- 8,50–11,62: iki yönlü kalem oku `-dı ⇄ have + V3`; el yazısı `İngilizce ayrı zaman`
  {
    const y = 805, a = yazi("-dı", { x: 140, y, boyut: 56, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(8.5), sure: 8, ses: true });
    const ar = ok([a.x1 + 22, y - 18], [a.x1 + 142, y - 18], { bas: fr(8.5) + 5, sure: 18, w: 6.5, cift: true, uzun: 22, bukum: 0.05 });
    yazi("have + V3", { x: a.x1 + 166, y, boyut: 56, aile: "Fredoka", agirlik: 700, renk: SARI, bas: bitis(ar) + 4, sure: 10, ses: true });
    not("ok -dı ⇄ have + V3", ar.bas);
    // 8,50–10,50 «İngilizce … ayrı bir zaman» (pencere: 8,50–9,14 · 9,86–10,22 · 10,22–10,50;
    // 'ayrı' 0,16 sn → 10,22'ye uzar)
    const iz = pen("İngilizce", 1), ay = pen("ayrı", 1), za = pen("zaman", 1);
    ay[0].f1 = za[0].f0;
    const n = elYazisi("İngilizce ayrı zaman", { x: 140, y: 905, boyut: 48, renk: IKI,
      sozcukler: [...iz, ...ay, ...za] });
    not("not İngilizce ayrı zaman", n.bas);
  }

  // --- 11,77–18,73: el kutusu, saat (6 min), 3 madde tik zamanlı
  {
    S.kutu(1060, 690, 760, 300, { bas: fr(11.77) - 8, sure: 38 }); not("kutu çizimi", fr(11.77) - 8);
    await S.svgCiz("tabler/clock.svg", { kutu: [1096, 712, 76, 76], bas: fr(12.05), sure: 20, azami: 25, w: 3.4, sesAralik: 3 });
    // 12,52: saatin yanında anlatımsız etiket, hedef 16 kare (0,53 sn; bitiş 13,05 < 13,85)
    elYazisi("6 min", { x: 1196, y: 772, boyut: 56, renk: SARI, bas: fr(12.05) + 14, sure: 16 });
    not("saat + 6 min", fr(12.05));
    parilti(1176, 714, { bas: fr(12.9), r: 22, periyot: 170, adet: 3 });
    // 14,73 since → başlangıç oku (past durağı); 15,45 for → süre bandı past→now (K26: yazı ≤ ses)
    baslangic(hat, "past", { etiket: "since", bas: fr(14.73) - 10 });
    aralik(hat, "past", "now", { etiket: "for", bas: fr(15.45) - 22, sure: 16 });
    const m = [["form", 13.85, 842], ["since / for", 15.17, 900], ["sinyal sözcükleri", 16.89, 958]];
    for (const [s, t, y] of m) {
      yazi(s, { x: 1140, y, boyut: 44, aile: "Fredoka", agirlik: 700, renk: KRE, bas: fr(t), sure: 8 });
      tik(1108, y - 12, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

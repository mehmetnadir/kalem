// Sahne 03 — Örnek 1 (02-02-ydt-temel, 855 kare, t_bas 16,27; cümle 5–9). Yerel kare = round((t − 16,27) × 30).
// Kök: "I go to Kaş every summer because I have a summer house there." (rutin + kalıcı durum).
import { sahneKur,
  RT } from "/projeler/02-02-ydt-temel/sahneler/03-paperjs-ornek1/kalem-paper.js";

export const KARE = 857, T_BAS = 16.27;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, parilti, olay, not, bitis,
    svgCiz, kis } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, KRE = RT.murekkep;
  const sol = (f0, f1) => (f) => kis(1 - (f - f0) / (f1 - f0));

  // --- cümle 5 (16,82–17,86): daire içinde 1
  const d1 = daire(200, 172, 66, 58, { bas: fr(16.85), sure: 22, a0: -2.6 });
  olay(bitis(d1), "tik", 0.5); not("daire 1 çizimi (Birinci)", d1.bas);
  yazi("1", { x: 200, y: 208, hizala: "orta", boyut: 100, aile: "Fredoka", agirlik: 700,
    bas: fr(17.3), sure: 10, olcek: true });

  // --- cümle 6 (18,41–22,01): İngilizce kök, 2 satır (Fredoka 56, aralık 90), sözcük zamanlı
  const sz = S.sozcukler(6);                                       // I go to Kaş every summer because I have a summer house there.
  const cz = cumle(sz.map((k, i) => ({ s: k.s, f: k.f, satir: i < 6 ? 0 : 1 })),
    { x: 140, y: 300, boyut: 56, aile: "Fredoka", agirlik: 700, aralik: 90 });
  altCizgi(cz, { tut: 40 }); not("cümle başı (I)", cz[0].bas);
  const tek = (k, bas, ad, k2 = k) => {          // sözcük(ler)in altına vurgu el altçizgisi (QA 13.11: halka harfe değiyordu)
    const x0 = k.x0 - 4, x1 = k2.x1 + 4, y = k.y + 24;
    ciz([[x0, y + 1], [(x0 + x1) / 2, y - 1], [x1, y + 1]], { w: 6.5, renk: SARI, alfa: 0.9, bas, sure: 14,
      uc0: 8, uc1: 14, amp: 0.7, tur: "isaret", ad });
    not(ad, bas);
  };
  tek(cz[1], fr(18.75), "go daire");                               // go 18,65
  tek(cz[8], fr(20.82), "have daire");                             // have 20,77
  {   // every summer (19,37–20,09): sarı alt çizgi (satır arası 90 px: ikinci satırın harflerine değmez)
    const x0 = cz[4].x0 - 4, x1 = cz[5].x1 + 4, y = cz[4].y + 24;
    ciz([[x0, y + 1], [(x0 + x1) / 2, y - 1], [x1, y + 1]], { w: 6.5, renk: SARI, alfa: 0.85,
      bas: fr(19.4), sure: 14, uc0: 8, uc1: 14, amp: 0.7, tur: "isaret", ad: "every summer altı" });
    not("every summer altı çizgi", fr(19.4));
  }

  // --- cümle 7 (22,48–25,68): sağda güneş + yazlık (kalemle); Türkçe çeviri (el yazısı 48, y 500)
  const GT = S.oge({ alfa: sol(fr(32.7), fr(33.0)) });             // çeviri 33,04'te başlayan satırlara yer açar
  {
    const ogeS = S.oge({ nefes: { bas: fr(25.8), cx: 1700, cy: 300 } });
    await svgCiz("tabler/sun.svg", { kutu: [1620, 150, 160, 160], bas: fr(22.76), sure: 22,
      azami: 10, w: 4.4, sesAralik: 2, oge: ogeS });
    not("güneş çizimi (yaz)", fr(22.76));
    const ogeE = S.oge({ nefes: { bas: fr(25.7), cx: 1560, cy: 650 } });
    await svgCiz("tabler/home.svg", { kutu: [1400, 330, 320, 320], bas: fr(24.64), sure: 30,
      azami: 8, w: 4.4, sesAralik: 2, oge: ogeE });
    not("yazlık çizimi (yazlığım)", fr(24.64));
  }
  {
    const tr = S.sozcukler(7); let tx = 140; const tz = [];
    tr.forEach((k, i) => {
      const f1 = i < tr.length - 1 ? Math.max(k.f1, tr[i + 1].f) : k.f1;   // kısa pencere sonraki sözcüğe uzar
      const q = elYazisi(k.s, { x: tx, y: 500, boyut: 48, renk: IKI, sozcukler: [{ f0: k.f, f1 }],
        oge: GT });
      tx = q.x1 + 0.3 * 48; tz.push(q);
    });
    not("Türkçe çeviri (Her)", tz[0].bas);
  }

  // --- cümle 8 (26,15–32,57): every summer → tekrar
  {
    const x0 = cz[4].x0, x1 = cz[5].x1, y = cz[4].y;
    tek(cz[4], fr(28.56), "every summer altçizgi (summer 28,56)", cz[5]);
    const ax = x1 + 34;
    const a = ok([ax, y - 22], [ax + 80, y - 22], { bas: fr(31.3), sure: 12, w: 6, uzun: 18,
      bukum: 0.1 });
    elYazisi("tekrar", { x: ax + 100, y: y - 4, boyut: 64, renk: SARI,
      sozcukler: [{ f0: fr(31.45), f1: fr(31.77) }] });
    not("ok + tekrar etiketi (tekrar)", bitis(a) - 12);
  }

  // --- cümle 9 (33,04–44,37): go → rutin · have → kalıcı durum; ikisi de geniş zaman; I + go / have
  const F64 = { boyut: 64, aile: "Fredoka", agirlik: 700 };
  const gz = yazi("go", { ...F64, x: 140, y: 640, renk: KRE, bas: fr(33.04), sure: 8, olcek: true,
    ses: true });
  not("go satırı (Gitmek)", gz.bas);
  ok([gz.x1 + 20, 620], [gz.x1 + 130, 620], { bas: fr(33.52), sure: 12, w: 6, uzun: 18,
    bukum: 0.1 });
  const r1 = elYazisi("rutin", { x: gz.x1 + 150, y: 640, boyut: 64, renk: SARI,
    sozcukler: [{ f0: fr(33.88), f1: fr(34.24) }] });
  not("rutin etiketi (rutin)", r1.bas);
  const hz = yazi("have", { ...F64, x: 140, y: 740, renk: KRE, bas: fr(34.64), sure: 8, olcek: true,
    ses: true });
  not("have satırı (Yazlığın)", hz.bas);
  ok([hz.x1 + 20, 720], [hz.x1 + 130, 720], { bas: fr(35.34), sure: 12, w: 6, uzun: 18,
    bukum: 0.1 });
  const k1 = S.sozcukler(9).find((k) => k.s === "kalıcı"), k2 = S.sozcukler(9).find((k) =>
    k.s === "durum.");
  const q1 = elYazisi("kalıcı", { x: hz.x1 + 150, y: 740, boyut: 64, renk: SARI,
    sozcukler: [{ f0: k1.f, f1: k2.f }] });
  const q2 = elYazisi("durum", { x: q1.x1 + 0.3 * 64, y: 740, boyut: 64, renk: SARI,
    sozcukler: [{ f0: k2.f, f1: k2.f1 }] });
  not("kalıcı durum etiketi (kalıcı)", q1.bas);
  {   // İkisi de geniş zaman (37,20): iki satırı birleştiren sarı süslü ayraç
    const bx = Math.max(r1.x1, q2.x1) + 50;
    ciz([[bx, 590], [bx + 22, 604], [bx + 22, 650], [bx + 46, 690], [bx + 22, 730],
      [bx + 22, 776], [bx, 790]], { w: 7, renk: SARI, alfa: 0.85, bas: fr(37.04), sure: 24, uc0: 10,
      uc1: 14, amp: 0.5, tur: "isaret", ad: "iki satır ayracı" });
    not("ayraç (İkisi de)", fr(37.04));
    parilti(bx + 90, 690, { bas: fr(37.92), r: 24 });
  }
  {   // Özne I (39,04; I. 39,69): kökteki iki I çevrelenir
    tek(cz[0], fr(39.45), "I daire (1. satır)");
    tek(cz[7], fr(39.95), "I daire (2. satır)");
    const FS = { boyut: 80, aile: "Fredoka", agirlik: 700 };
    const i1 = yazi("I", { ...FS, x: 140, y: 900, renk: KRE, bas: fr(39.45), sure: 8,
      olcek: true, ses: true });
    not("formül I (I.)", i1.bas);
    const p1 = yazi("+", { ...FS, x: i1.x1 + 26, y: 900, renk: IKI, bas: fr(40.74), sure: 8,
      olcek: true });
    const g2 = yazi("go", { ...FS, x: p1.x1 + 26, y: 900, renk: SARI, bas: fr(42.75), sure: 8,
      olcek: true, ses: true });
    not("formül go (go)", g2.bas);
    parilti(g2.x1 + 30, 840, { bas: fr(42.75), r: 22 });
    const s2 = yazi("/", { ...FS, x: g2.x1 + 26, y: 900, renk: IKI, bas: fr(43.4), sure: 6 });
    const h2 = yazi("have", { ...FS, x: s2.x1 + 26, y: 900, renk: SARI, bas: fr(43.81),
      sure: 8, olcek: true, ses: true });
    not("formül have (have)", h2.bas);
  }
  return S;
}

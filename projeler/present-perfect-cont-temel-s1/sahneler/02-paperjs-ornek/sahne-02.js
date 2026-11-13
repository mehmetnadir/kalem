// Sahne 02 — Örnek (DİKEY 1080x1920, 424 kare, t_bas 3,00; cümle 1 devamı + cümle 2). Telefon ölçeği (BRIEF-DIKEY §3).
// Sahne 01'in son hali (HUD + Caveat 80 satırı "İki saattir çalışıyorum." + figür/dizüstü/saat eskizi) kare 0'da hazır;
// zamanlar küresel sn, fr(t) = round((t - 3,00) x 30). Bantlar: HUD 0-320, içerik 352-1392, altyazı 1400-1536.
import { sahneKur, RT } from "/projeler/present-perfect-cont-temel-s1/sahneler/02-paperjs-ornek/kalem-paper.js";

export const KARE = 424, T_BAS = 3.0;
const CIP = "= HAVE BEEN";

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: CIP });
  const { fr, ciz, daire, ok, yazi, elYazisi, cumle, tik, parilti, olay, not, bitis, kutu,
    genislik, oge, kis } = S;
  const SARI = RT.vurgu, DOLGU = RT.vurguDolgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const s1 = S.sozcukler(1), s2 = S.sozcukler(2);
  const solma = (t0, t1) => (f) => 1 - kis((f - fr(t0)) / (fr(t1) - fr(t0)));   // 1 -> 0
  // ust: cümle 1 + have been formülü (7,86'ya kadar); eskiz: figür + dizüstü + saat (8,7'de solar)
  const ust = oge({ alfa: solma(7.5, 7.78) });
  const eskizAlfa = solma(8.35, 8.7);
  const figOge = oge({ alfa: eskizAlfa, nefes: { bas: fr(4.0), cx: 170, cy: 1140 } });
  const evOge = oge({ alfa: eskizAlfa });
  const saOge = oge({ alfa: eskizAlfa });
  const alt2 = oge({ alfa: solma(13.3, 13.65) });          // kardeş + gitar + güneş + ok (13,65'te solar)
  const altCiz = (z, f0, o = {}) => ciz([[z.x0 - 4, z.y + 12], [z.x1 + 4, z.y + 8]],
    { w: 9, renk: DOLGU, alfa: 0.9, bas: f0, sure: 12, uc0: 8, uc1: 12, amp: 1.0, tur: "isaret", ad: o.ad || "altCiz", ...o });
  // sıra: Fredoka formül sözcükleri bant genişliğine (900) sığacak boyda, ortalı; her öğe {s, renk, f, ara}
  const sira = (ogeler, { y, bz, ust: o, bos = 40 }) => {
    const f100 = (s) => genislik(s, "700 100px Fredoka");
    const ara = (g) => (g.ara == null ? bos : g.ara);
    const bosTop = ogeler.slice(0, -1).reduce((a, g) => a + ara(g), 0);
    const b = Math.floor(Math.min(bz, 100 * (900 - bosTop) / ogeler.reduce((a, g) => a + f100(g.s), 0)));
    const f = "700 " + b + "px Fredoka";
    const top = ogeler.reduce((a, g) => a + genislik(g.s, f), 0) + bosTop;
    let x = (1080 - top) / 2; const z = [];
    for (const g of ogeler) {
      const q = yazi(g.s, { x, y, boyut: b, aile: "Fredoka", agirlik: 700, renk: g.renk, bas: g.f, sure: 8,
        olcek: true, ses: g.ses || "tik", oge: o });
      x = q.x1 + ara(g); z.push(q);
    }
    return { z, b };
  };

  // --- cümle 1 (sahne 01'in son hali + devamı): Caveat 80, x 72, y 440 / 530
  // satır 1: İki saattir çalışıyorum.   satır 2: İngilizcede kalıp tek:
  const c80 = { x: 72, y: 440, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 90, oge: ust };
  // satır 1 (sözcük 0–2): 01'den devralınan son görünüm, kare 0'da hazır (01 dokunulmaz);
  // Caveat yazi kalır
  const e1 = cumle(s1.slice(0, 3).map((w) => ({ s: w.s, f: -30, satir: 0 })), c80);
  altCiz(e1[1], fr(3.0) + 6, { oge: ust }); not("saattir altı çizgi (cümle 1)", fr(3.0) + 6);
  // satır 2 (kare 2–48 = 3,07–4,59 sn; "İngilizcede kalıp tek:" 2,83–4,59): sözcük penceresi,
  // eski belirme anı kare 2 (İngilizcede), sağ uç x1 = 72 + 555 = 627 px
  elYazisi("İngilizcede kalıp tek:", { x: c80.x, y: c80.y + c80.aralik, boyut: c80.boyut, renk: MUR,
    oge: ust, sozcukler: s1.slice(3, 6).map((w, i) => ({ f0: i === 0 ? Math.max(2, w.f) : w.f,
      f1: w.f1 })) });

  // --- eskiz (sahne 01'den hazır): figür 480 px + dizüstü (kutu 460) + saat (kutu 330) + zemin çizgisi, y 900-1384
  await S.svgCiz("open-peeps/standing-2.svg", { kutu: [100, 900, 146, 480], bas: -200, sure: 2, azami: 60,
    yuz: 3, w: 4.4, oge: figOge, sessiz: true });
  await S.svgCiz("tabler/device-laptop.svg", { kutu: [300, 1000, 460, 460], bas: -200, sure: 2, azami: 25,
    w: 4.0, oge: evOge, sessiz: true });
  await S.svgCiz("tabler/clock.svg", { kutu: [690, 960, 330, 330], bas: -200, sure: 2, azami: 25, w: 4.0,
    oge: saOge, sessiz: true });
  ciz([[96, 1384], [560, 1382], [1000, 1384]], { w: 4, renk: IKI, alfa: 0.75, bas: -200, sure: 2, uc0: 10,
    uc1: 30, oge: evOge, ses: false });

  // --- 3,55: kart (have been + -ing); formül 4,67 / 5,71 / 6,75, "-ing" sarı
  kutu(48, 640, 984, 200, { bas: fr(3.55), sure: 36, renk: IKI, w: 4.2, oge: ust }); not("formül kartı", fr(3.55));
  {
    const r = sira([
      { s: "have", renk: MUR, f: s1[6].f, ara: 24 }, { s: "been", renk: MUR, f: s1[7].f },
      { s: "+", renk: IKI, f: s1[8].f }, { s: "-ing", renk: SARI, f: s1[10].f, ses: false }],
      { y: 785, bz: 130, ust });
    const g = r.z[3];
    olay(g.bas, "vurus", 0.8); not("have", r.z[0].bas); not("-ing (sarı)", g.bas);
    altCiz(g, g.bas + 8, { w: 10, oge: ust }); parilti(g.x1 + 24, 690, { bas: g.bas + 10, r: 24, periyot: 130, adet: 1, oge: ust });
  }

  // --- 7,86–10,8: örnek kartı (tam genişlik): My brother has been playing the guitar since this morning.
  kutu(48, 372, 984, 480, { bas: fr(7.86) - 8, sure: 36, renk: IKI, w: 4.2 }); not("örnek kartı", fr(7.86) - 8);
  {
    const en = s2.slice(0, 10), satir = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2];
    const e = cumle(en.map((k, i) => ({ s: k.s, f: k.f, satir: satir[i] })),
      { x: 88, y: 478, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: 88 });
    not("EN cümle başı", e[0].bas);
    const g = e[3], d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 14, 38, { bas: g.bas + 4, sure: 20, a0: -2.0 });
    olay(bitis(d), "tik", 0.5); not("been daire", d.bas);
    // 11,07–13,79 sn (kare 242–324; "Kardeşim sabahtan beri gitar çalıyor."): her sözcük kendi
    // penceresinde; sözcük arası 0,3 × boyut (motor aralığı); satır 1 = Kardeşim sabahtan beri,
    // satır 2 = gitar çalıyor.
    const tr = s2.slice(10, 15), t = [];
    let tx = 88;
    tr.forEach((k, i) => {
      const sat = i < 3 ? 0 : 1; if (i === 0 || i === 3) tx = 88;
      // "beri" penceresi 4 kare (0,13 sn): okunur kalsın diye 10 kareye uzatıldı
      // (bitiş 288 < cümle sonu 324)
      const q = elYazisi(k.s, { x: tx, y: 748 + sat * 70, boyut: 64, renk: MUR,
        sozcukler: [{ f0: k.f, f1: Math.max(k.f1, k.f + 10) }] });
      tx = q.x1 + 0.3 * 64; t.push(q);
    });
    altCiz(t[1], t[1].bit - 6, { w: 8 }); not("sabahtan altı çizgi", t[1].bit - 6);
  }

  // --- 8,75–11,9: kardeş + gitar (alt bant 900-1392), güneş + "sabahtan beri" yayı (9,78)
  await S.svgCiz("open-peeps/standing-3.svg", { kutu: [100, 900, 300, 480], bas: fr(8.7), sure: 34, azami: 60,
    yuz: 3, w: 4.4, oge: alt2 });
  not("kardeş çizimi", fr(8.7));
  await S.svgCiz("coco/guitar.svg", { kutu: [330, 1010, 280, 350], bas: fr(9.05), sure: 26, azami: 14, w: 4.0,
    oge: alt2 });
  not("gitar çizimi", fr(9.05));
  await S.svgCiz("tabler/sun.svg", { kutu: [760, 910, 250, 250], bas: fr(9.78), sure: 18, azami: 12, kisaAtla: 0, w: 4.0,
    oge: alt2 });
  not("güneş (since this morning)", fr(9.78));
  ok([790, 985], [360, 985], { bas: fr(10.2), sure: 26, bukum: 0.2, yon: [0, -1], w: 8, oge: alt2 });
  not("since yayı", fr(10.2));
  {
    // 11,71–12,39 sn (kare 261–282; "sabahtan beri"): orta eksen x 885; tegaki genişliği ölçüldü:
    // sabahtan 244,4 px (x0 762,8 → x1 1007,2), beri 96,0 px (x0 837 → x1 933);
    // "beri" penceresi 10 kareye uzatıldı
    const a = elYazisi("sabahtan", { x: 885 - 244.4 / 2, y: 1255, boyut: 72, renk: SARI,
      sozcukler: [{ f0: s2[11].f, f1: s2[11].f1 }], oge: alt2 });
    elYazisi("beri", { x: 885 - 96 / 2, y: 1330, boyut: 72, renk: SARI,
      sozcukler: [{ f0: s2[12].f, f1: Math.max(s2[12].f1, s2[12].f + 10) }], oge: alt2 });
    not("sabahtan beri", a.bas);
    parilti(960, 930, { bas: fr(11.0), r: 22, periyot: 130, adet: 1, oge: alt2 });
  }

  // --- 13,91–16,75: Tekil kişide: he · she · it, has been + -ing (kutu y 930-1330)
  kutu(48, 930, 984, 400, { bas: fr(13.91) - 6, sure: 34, renk: IKI, w: 4.2 }); not("has been kutusu", fr(13.91) - 6);
  yazi("he · she · it", { x: 540, y: 1045, boyut: 80, renk: MUR, hizala: "orta", bas: s2[16].f, sure: 12,
    ses: "tik" });
  not("he · she · it", s2[16].f);
  {
    const r = sira([
      { s: "has", renk: SARI, f: s2[17].f, ara: 24 }, { s: "been", renk: MUR, f: s2[18].f },
      { s: "+", renk: IKI, f: s2[19].f }, { s: "-ing", renk: SARI, f: s2[20].f, ses: false }],
      { y: 1235, bz: 140, ust: null });
    const g = r.z[3];
    olay(g.bas, "vurus", 0.8); not("has", r.z[0].bas); not("-ing (sarı)", g.bas);
    altCiz(g, g.bas + 8, { w: 10 }); parilti(g.x1 + 24, 1120, { bas: g.bas + 10, r: 24, periyot: 130, adet: 1 });
  }
  return S;
}

// Sahne 02 (02-04-ydt-temel-s1 Shorts) — Örnek: Paper.js, 1080x1920, 522 kare, t_bas 3.00.
// Cümle 1 sonu (Türkçe yaşıyorum satırları) + cümle 2 (İngilizce live / am living kartları ve zaman çizgileri).
import { sahneKur, RT, KUNYE } from "/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/kalem-paper.js";
import { yaziNoktalari } from "/projeler/02-04-ydt-temel-s1/ortak/kalem-canvas.js";

export const KARE = 522, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: KUNYE.cipler["02-paperjs-ornek"] });
  const {
    fr, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, svgCiz, oge, not, genislik,
  } = S;

  // Tegaki Caveat 700 metrik ve glif verisi (el yazısı genişlik ölçümü)
  const [eyM, eyG] = await Promise.all([
    fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json"),
  ]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, {
    upm: EY.M.unitsPerEm, asc: EY.M.ascender, boy: boyut, x: 0, taban: 0,
  }).gen;

  // Sözcük penceresi ve el yazısı satır yardımcısı
  const pen = (ws) => ws.map((w, i) => ({
    f0: w.f,
    f1: w.f1 - w.f < 6 && ws[i + 1] ? ws[i + 1].f : w.f1,
  }));
  const satir = (soz, pn, o) => soz.map((k, i) => elYazisi(k, {
    ...o,
    x: o.x + eyGen(soz.join(" "), o.boyut) - eyGen(soz.slice(i).join(" "), o.boyut),
    sozcukler: [pn[i]],
  }));

  // Sözcük doğrulama bekçisi
  const noktasiz = (s) => s.replace(/[\p{P}\p{S}]/gu, "");
  const al = (dizi, i, beklenen) => {
    const w = dizi && dizi[i];
    if (!w) throw new Error(`al: dizi[${i}] sözcük bulunamadı (beklenen: "${beklenen}")`);
    const sTr = noktasiz(w.s).toLocaleLowerCase("tr");
    const bTr = noktasiz(beklenen).toLocaleLowerCase("tr");
    if (sTr !== bTr && sTr.replace(/ı/g, "i") !== bTr.replace(/ı/g, "i")) {
      throw new Error(`al: dizi[${i}] sözcük uyuşmazlığı: "${w.s}" ("${sTr}") !== "${beklenen}" ("${bTr}")`);
    }
    return w;
  };

  // Zaman ve sözcükler
  const s1 = S.sozcukler(1);
  const s2 = S.sozcukler(2);
  const f0 = (t) => Math.max(12, fr(t));

  const wYasiyorum1 = al(s1, 3, "yaşıyorum.");
  const wTurkcede = al(s1, 4, "Türkçede");
  const wYasiyorum2 = al(s1, 7, "yaşıyorum.");

  const wAyrilir = al(s2, 2, "ayrılır.");
  const wI1 = al(s2, 3, "I");
  const wLive = al(s2, 4, "live");
  const wIn = al(s2, 5, "in");
  const wIstanbul = al(s2, 6, "Istanbul.");
  const wHep = al(s2, 7, "Hep");
  const wOrada = al(s2, 8, "orada:");
  const wKalici = al(s2, 9, "kalıcı");
  const wDurum1 = al(s2, 10, "durum,");
  const wGenis = al(s2, 11, "geniş");
  const wI2 = al(s2, 13, "I");
  const wAm = al(s2, 14, "am");
  const wLiving = al(s2, 15, "living");
  const wWith = al(s2, 16, "with");
  const wMy = al(s2, 17, "my");
  const wUncle = al(s2, 18, "uncle.");
  const wSimdilik = al(s2, 19, "Şimdilik:");
  const wGecici = al(s2, 20, "geçici");
  const wDurum2 = al(s2, 21, "durum,");
  const wSimdiki = al(s2, 22, "şimdiki");

  // Ölçü ve sabitler (BRIEF-DIKEY §2–§3)
  const KENAR = KUNYE.kenar;
  const W = 1080;
  const SAG = W - KENAR;
  const SOL = KENAR + 24;
  const KX = KENAR;
  const KW = W - 2 * KENAR;
  const IC = KX + 40;
  const BTR = 80;
  const Y_L1 = 470;
  const Y_L2 = 590;
  const BEN = 64;
  const BTR2 = 72;
  const BET = 72;
  const BNOW = 64;
  const KY1 = 460;
  const KH1 = 220;
  const KY2 = 935;
  const KH2 = 300;
  const YC1 = 430;
  const YC2 = 905;
  const AXY1 = 740;
  const AXY2 = 1290;
  const IKON = 100;
  const ALT = 0.30;

  // Türetilen konumlar
  const yb1 = KY1 + 88;
  const yTr1 = KY1 + 182;
  const yb2 = KY2 + 88;
  const yTr2 = KY2 + 267;
  const yEtiket1 = AXY1 + 24;
  const yNow1 = AXY1 + 76;
  const yEtiket2 = AXY2 + 24;
  const yNow2 = AXY2 + 76;
  const AX1 = W - KENAR - 24;
  const AX0 = SOL + Math.max(eyGen("PERMANENT", BET), eyGen("TEMPORARY", BET)) + 36;
  const NX = Math.round((AX0 + AX1) / 2);
  const ikonX = KX + KW - 40 - IKON;

  // Kart sözcükleri (konum okuma ve karaoke hazırlığı)
  const kel1 = cumle([
    { s: wI1.s, f: fr(wI1.t), satir: 0 },
    { s: wLive.s, f: fr(wLive.t), satir: 0 },
    { s: wIn.s, f: fr(wIn.t), satir: 0 },
    { s: "İstanbul.", f: fr(wIstanbul.t), satir: 0 },
  ], { x: IC, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep });
  altCizgi(kel1, { tut: 24, alt: ALT });

  const kel2 = cumle([
    { s: wI2.s, f: fr(wI2.t), satir: 0 },
    { s: wAm.s, f: fr(wAm.t), satir: 0 },
    { s: wLiving.s, f: fr(wLiving.t), satir: 0 },
    { s: wWith.s, f: fr(wWith.t), satir: 1 },
    { s: wMy.s, f: fr(wMy.t), satir: 1 },
    { s: wUncle.s, f: fr(wUncle.t), satir: 1 },
  ], { x: IC, y: yb2, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, aralik: 85 });
  altCizgi(kel2, { tut: 24, alt: ALT });

  // Çip hedef ve kayma hesapları
  const hedefOrta_1 = (kel1[1].x0 + kel1[1].x1) / 2;
  const hedefOrta_2 = (kel2[1].x0 + kel2[2].x1) / 2;

  const F_TR = "700 80px Caveat";
  const gYor = genislik("yor", F_TR);
  const XC1 = hedefOrta_1 + 150 - gYor / 2;
  const XC2 = hedefOrta_2 + 150 - gYor / 2;

  const pre1Str = "İstanbul'da yaşı-";
  const pre2Str = "Amcamla yaşı-";
  const postStr = "-um.";
  const xYor1 = SOL + genislik(pre1Str, F_TR);
  const xYor2 = SOL + genislik(pre2Str, F_TR);
  const xPost1 = xYor1 + gYor;
  const xPost2 = xYor2 + gYor;

  const dx1 = XC1 - xYor1;
  const dy1 = YC1 - Y_L1;
  const dx2 = XC2 - xYor2;
  const dy2 = YC2 - Y_L2;

  // ayrılır: TR parçaları G0–G0+8 söner; çipler G0+6'da kalkar (sönen "yaşı-" üstünden geçmesin), 15 karede iner
  const G0 = fr(wAyrilir.t);
  const GK0 = G0 + 6;
  const G1 = GK0 + 15;

  // Bekçiler
  const sagTR1 = xPost1 + genislik(postStr, F_TR);
  const sagTR2 = xPost2 + genislik(postStr, F_TR);
  if (sagTR1 > SAG || sagTR2 > SAG) {
    throw new Error(`Bekçi: TR satırı sağ ucu sınırı aştı (TR1: ${sagTR1}, TR2: ${sagTR2} > ${SAG})`);
  }
  const sagKart1 = kel1[kel1.length - 1].x1;
  if (sagKart1 > ikonX - 20) {
    throw new Error(`Bekçi: Kart 1 cümlesi sağ ucu ikon payını aştı (${sagKart1} > ${ikonX - 20})`);
  }
  const sagKart2_0 = kel2[2].x1;
  const sagKart2_1 = kel2[5].x1;
  if (sagKart2_0 > SAG - 40 || sagKart2_1 > SAG - 40) {
    throw new Error(`Bekçi: Kart 2 satır sağ ucu sınırı aştı (s0: ${sagKart2_0}, s1: ${sagKart2_1} > ${SAG - 40})`);
  }
  if (AX0 > NX - 120) {
    throw new Error(`Bekçi: AX0 > NX - 120 (${AX0} > ${NX - 120})`);
  }
  if (AXY2 + 76 > KUNYE.icerikSon) {
    throw new Error(`Bekçi: AXY2 + 76 > KUNYE.icerikSon (${AXY2 + 76} > ${KUNYE.icerikSon})`);
  }

  // Çip öğeleri (katman sırası: bandOge -> metinOge -> UST)
  const bandOge1 = oge({ kay: { f0: GK0, f1: G1, dx: dx1, dy: dy1 } });
  const bandOge2 = oge({ kay: { f0: GK0, f1: G1, dx: dx2, dy: dy2 } });
  const metinOge1 = oge({ kay: { f0: GK0, f1: G1, dx: dx1, dy: dy1 } });
  const metinOge2 = oge({ kay: { f0: GK0, f1: G1, dx: dx2, dy: dy2 } });
  const UST = oge({});
  // Kapı kutusu öğe grubundan okunur (kayma dahil); grup içindeki yazının yerel kutusu kayma öncesinde kalır.
  metinOge1.g.data = { kalemTur: "yazi", kalemAd: "yor çip 1" };
  metinOge2.g.data = { kalemTur: "yazi", kalemAd: "yor çip 2" };

  // 1. İki TR satırı (kare 0'da sahne 01'den hazır)
  const fSonTR = [G0, G0 + 8];
  yazi(pre1Str, {
    x: SOL, y: Y_L1, boyut: BTR, aile: "Caveat", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, son: fSonTR,
  });
  yazi("yor", {
    x: xYor1, y: Y_L1, boyut: BTR, aile: "Caveat", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: metinOge1,
  });
  yazi(postStr, {
    x: xPost1, y: Y_L1, boyut: BTR, aile: "Caveat", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, son: fSonTR,
  });

  yazi(pre2Str, {
    x: SOL, y: Y_L2, boyut: BTR, aile: "Caveat", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, son: fSonTR,
  });
  yazi("yor", {
    x: xYor2, y: Y_L2, boyut: BTR, aile: "Caveat", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: metinOge2,
  });
  yazi(postStr, {
    x: xPost2, y: Y_L2, boyut: BTR, aile: "Caveat", agirlik: 700,
    renk: RT.murekkep, bas: -30, sure: 4, ses: false, son: fSonTR,
  });
  not("TR satırları (hazır)", 0);

  // 2. Karaoke: satır 2 yaşı-yor-um. altı
  altCizgi([{
    x0: xYor2 - genislik("yaşı-", F_TR),
    x1: xYor2 + gYor + genislik("-um.", F_TR),
    y: Y_L2,
    boyut: BTR,
    bas: f0(wYasiyorum1.t),
  }], { tut: 20, alt: 0.32 });
  not("karaoke yaşıyorum (yaşıyorum.)", f0(wYasiyorum1.t));

  // 3. ek_ayir: satır 1 yor kutusu
  const by1 = Y_L1 - BTR * 0.22;
  ciz([[xYor1 - 5, by1], [xYor1 + gYor + 6, by1]], {
    duz: true,
    w: BTR * 0.70,
    renk: RT.vurguDolgu,
    alfa: 0.6,
    uc0: 5,
    uc1: 9,
    amp: 1.0,
    bas: f0(wTurkcede.t),
    sure: 10,
    tur: "isaret",
    ses: "tik",
    oge: bandOge1,
    ad: "yor kutusu 1",
  });
  not("ek_ayir yor 1 (Türkçede)", f0(wTurkcede.t));

  // 4. ek_ayir: satır 2 yor kutusu
  const by2 = Y_L2 - BTR * 0.22;
  ciz([[xYor2 - 5, by2], [xYor2 + gYor + 6, by2]], {
    duz: true,
    w: BTR * 0.70,
    renk: RT.vurguDolgu,
    alfa: 0.6,
    uc0: 5,
    uc1: 9,
    amp: 1.0,
    bas: fr(wYasiyorum2.t) + 9,
    sure: 10,
    tur: "isaret",
    ses: "tik",
    oge: bandOge2,
    ad: "yor kutusu 2",
  });
  not("ek_ayir yor 2 (yaşıyorum.)", fr(wYasiyorum2.t) + 9);

  // 5. TR satırlar solar, iki çip ayrılır
  not("çip ayrılır (ayrılır.)", G0);

  // 6. Kart 1 kutusu
  kutu(KX, KY1, KW, KH1, {
    bas: fr(wI1.t) - 10,
    sure: 14,
    w: 4,
    renk: RT.ikincil,
    ad: "kart 1 kutusu",
  });
  not("kart 1 kutusu (I)", fr(wI1.t) - 10);

  // 7. Kart 1 sözcükleri
  not("kart 1 sözcükleri (I)", fr(wI1.t));

  // 8. odak live (kalıcı sarı altçizgi)
  const yU1 = yb1 + BEN * ALT;
  ciz([[kel1[1].x0 - 4, yU1], [kel1[1].x1 + 4, yU1 - 2]], {
    duz: true,
    w: 9,
    renk: RT.vurguDolgu,
    alfa: 0.9,
    uc0: 6,
    uc1: 8,
    amp: 0.8,
    bas: fr(wLive.t),
    sure: 6,
    tur: "isaret",
    ses: "tik",
    ad: "odak live",
  });
  not("odak live (live)", fr(wLive.t));

  // 9. bag çip 1 -> live
  ok([XC1 - 8, YC1 + 10], [hedefOrta_1 + 10, yb1 - BEN * 0.95], {
    bas: fr(wIn.t),
    sure: 12,
    w: 6,
    uzun: 18,
    bukum: 0.12,
    ad: "bag 1",
  });
  not("bag 1 (in)", fr(wIn.t));

  // 10. Ev ikonu
  await svgCiz("tabler/home.svg", {
    kutu: [ikonX, KY1 + 14, IKON, IKON],
    bas: fr(wIstanbul.t),
    sure: 20,
    azami: 25,
    w: 4,
    sesAralik: 3,
  });
  not("ev ikonu (Istanbul.)", fr(wIstanbul.t));

  // 11. Soluk TR Hep orada.
  satir(["Hep", "orada."], pen(s2.slice(7, 9)), {
    x: IC,
    y: yTr1,
    boyut: BTR2,
    renk: RT.ikincil,
  });
  not("Hep orada. (Hep)", fr(wHep.t));

  // 12. PERMANENT etiketi
  elYazisi("PERMANENT", {
    x: SOL,
    y: yEtiket1,
    boyut: BET,
    renk: RT.murekkep,
    bas: fr(wKalici.t),
    sure: 18,
  });
  not("PERMANENT (kalıcı)", fr(wKalici.t));

  // 13. Zaman çizgisi 1: eksen + sağ ok
  ciz([[AX0, AXY1], [AX1, AXY1]], {
    duz: true,
    w: 4.5,
    renk: RT.ikincil,
    uc0: 8,
    uc1: 6,
    bas: fr(wDurum1.t),
    sure: 12,
    tur: "cizim",
    ad: "zaman-1",
  });
  [1, -1].forEach((s) => {
    ciz([[AX1 - 26, AXY1 - s * 16], [AX1, AXY1]], {
      duz: true,
      w: 4.5,
      renk: RT.ikincil,
      uc0: 4,
      uc1: 4,
      bas: fr(wDurum1.t) + 11,
      sure: 4,
      ses: false,
      tur: "cizim",
      ad: "zaman-1",
    });
  });
  not("zaman-1 eksen (durum,)", fr(wDurum1.t));

  // 14. now noktası + now
  daire(NX, AXY1, 12, 12, {
    renk: RT.murekkep,
    w: 4.5,
    alfa: 0.95,
    a0: -1.6,
    ad: "now 1",
    bas: fr(wDurum1.t) + 8,
    sure: 8,
    ses: "tik",
    oge: UST,
  });
  not("now 1 (durum,)", fr(wDurum1.t) + 8);

  elYazisi("now", {
    x: NX - eyGen("now", BNOW) / 2,
    y: yNow1,
    boyut: BNOW,
    renk: RT.murekkep,
    bas: fr(wDurum1.t) + 12,
    sure: 12,
    ses: false,
  });
  not("now 1 metin (durum,)", fr(wDurum1.t) + 12);

  // 15. Uzun bant (kalıcı)
  ciz([[AX0 + 24, AXY1], [AX1 - 44, AXY1]], {
    duz: true,
    w: 28,
    renk: RT.vurguDolgu,
    alfa: 0.55,
    uc0: 4,
    uc1: 4,
    amp: 0.6,
    bas: fr(wGenis.t),
    sure: 16,
    tur: "isaret",
    ad: "uzun bant",
  });
  not("uzun bant (geniş)", fr(wGenis.t));

  // 16. Kart 2 kutusu
  kutu(KX, KY2, KW, KH2, {
    bas: fr(wI2.t) - 10,
    sure: 14,
    w: 4,
    renk: RT.ikincil,
    ad: "kart 2 kutusu",
  });
  not("kart 2 kutusu (I)", fr(wI2.t) - 10);

  // 17. Kart 2 sözcükleri
  not("kart 2 sözcükleri (I)", fr(wI2.t));

  // 18. odak am living
  const yU2 = yb2 + BEN * ALT;
  ciz([[kel2[1].x0 - 4, yU2], [kel2[2].x1 + 4, yU2 - 2]], {
    duz: true,
    w: 9,
    renk: RT.vurguDolgu,
    alfa: 0.9,
    uc0: 6,
    uc1: 8,
    amp: 0.8,
    bas: fr(wLiving.t),
    sure: 8,
    tur: "isaret",
    ses: "tik",
    ad: "odak am living",
  });
  not("odak am living (living)", fr(wLiving.t));

  // 19. bag çip 2 -> am living
  ok([XC2 - 8, YC2 + 10], [hedefOrta_2 + 10, yb2 - BEN * 0.95], {
    bas: fr(wWith.t),
    sure: 12,
    w: 6,
    uzun: 18,
    bukum: 0.12,
    ad: "bag 2",
  });
  not("bag 2 (with)", fr(wWith.t));

  // 20. Bavul ikonu
  await svgCiz("/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/bavul.svg", {
    kutu: [ikonX, KY2 + 14, IKON, IKON],
    bas: fr(wUncle.t),
    sure: 20,
    azami: 12,
    w: 4,
    sesAralik: 3,
  });
  not("bavul ikonu (uncle.)", fr(wUncle.t));

  // 21. Soluk TR Şimdilik.
  satir(["Şimdilik."], pen(s2.slice(19, 20)), {
    x: IC,
    y: yTr2,
    boyut: BTR2,
    renk: RT.ikincil,
  });
  not("Şimdilik. (Şimdilik:)", fr(wSimdilik.t));

  // 22. TEMPORARY etiketi
  elYazisi("TEMPORARY", {
    x: SOL,
    y: yEtiket2,
    boyut: BET,
    renk: RT.murekkep,
    bas: fr(wGecici.t),
    sure: 18,
  });
  not("TEMPORARY (geçici)", fr(wGecici.t));

  // 23. Zaman çizgisi 2: eksen + ok, now + now
  ciz([[AX0, AXY2], [AX1, AXY2]], {
    duz: true,
    w: 4.5,
    renk: RT.ikincil,
    uc0: 8,
    uc1: 6,
    bas: fr(wDurum2.t),
    sure: 12,
    tur: "cizim",
    ad: "zaman-2",
  });
  [1, -1].forEach((s) => {
    ciz([[AX1 - 26, AXY2 - s * 16], [AX1, AXY2]], {
      duz: true,
      w: 4.5,
      renk: RT.ikincil,
      uc0: 4,
      uc1: 4,
      bas: fr(wDurum2.t) + 11,
      sure: 4,
      ses: false,
      tur: "cizim",
      ad: "zaman-2",
    });
  });
  not("zaman-2 eksen (durum,)", fr(wDurum2.t));

  daire(NX, AXY2, 12, 12, {
    renk: RT.murekkep,
    w: 4.5,
    alfa: 0.95,
    a0: -1.6,
    ad: "now 2",
    bas: fr(wDurum2.t) + 8,
    sure: 8,
    ses: "tik",
    oge: UST,
  });
  not("now 2 (durum,)", fr(wDurum2.t) + 8);

  elYazisi("now", {
    x: NX - eyGen("now", BNOW) / 2,
    y: yNow2,
    boyut: BNOW,
    renk: RT.murekkep,
    bas: fr(wDurum2.t) + 12,
    sure: 12,
    ses: false,
  });
  not("now 2 metin (durum,)", fr(wDurum2.t) + 12);

  // 24. Kısa bant + uç çentikleri
  ciz([[NX - 72, AXY2], [NX + 72, AXY2]], {
    duz: true,
    w: 28,
    renk: RT.vurguDolgu,
    alfa: 0.55,
    uc0: 4,
    uc1: 4,
    amp: 0.6,
    bas: fr(wSimdiki.t),
    sure: 10,
    tur: "isaret",
    ad: "kısa bant",
  });
  not("kısa bant (şimdiki)", fr(wSimdiki.t));

  [NX - 72, NX + 72].forEach((x, i) => {
    ciz([[x, AXY2 - 26], [x, AXY2 + 26]], {
      duz: true,
      w: 5,
      renk: RT.vurgu,
      alfa: 0.9,
      uc0: 3,
      uc1: 3,
      amp: 0.3,
      bas: fr(wSimdiki.t) + 6 + 3 * i,
      sure: 5,
      ses: false,
      tur: "isaret",
      ad: "kısa bant çentik",
    });
    not(`kısa bant çentik ${i + 1} (şimdiki)`, fr(wSimdiki.t) + 6 + 3 * i);
  });

  return S;
}

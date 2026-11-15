// Sahne 02 (simple-present-temel-s2 Shorts) — Değer: Paper.js, 1080x1920, 278 kare, t_bas 3.00.
// Cümle 2: My brother usually goes to school by bus. Alışkanlık işareti. Şu an değil, her sabah yedide kalkarım gibi.
// huni v2 (15.11): içerik x 60–960, y 460–1380; çip yok; kanal katmanı ve künye kunye.js'te.
import { sahneKur, RT, KUNYE } from "/projeler/simple-present-temel-s2/sahneler/02-paperjs-deger/kalem-paper.js";
import { yaziNoktalari } from "/projeler/simple-present-temel-s2/ortak/kalem-canvas.js";

export const KARE = 278, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS });
  const {
    fr, ciz, daire, kutu, yazi, elYazisi, cumle, svgCiz, oge, not, genislik, kis,
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

  // Sözcükler
  const s2 = S.sozcukler(2);
  const wMy = al(s2, 0, "My");
  const wBrother = al(s2, 1, "brother");
  const wUsually = al(s2, 2, "usually");
  const wGoes = al(s2, 3, "goes");
  const wTo = al(s2, 4, "to");
  const wSchool = al(s2, 5, "school");
  const wBy = al(s2, 6, "by");
  const wBus = al(s2, 7, "bus.");
  const wAliskanlik = al(s2, 8, "Alışkanlık");
  const wIsareti = al(s2, 9, "işareti.");
  const wSu = al(s2, 10, "Şu");
  const wAn = al(s2, 11, "an");
  const wDegil = al(s2, 12, "değil,");
  const wHer = al(s2, 13, "her");
  const wSabah = al(s2, 14, "sabah");
  const wYedide = al(s2, 15, "yedide");
  const wKalkarim = al(s2, 16, "kalkarım");

  // Sabitler
  const KENAR = KUNYE.kenar;
  const SAG = KUNYE.sag;
  const SOL = KENAR + 24;
  const KUTU_PAY = 10;
  const KX = KENAR + KUTU_PAY;
  const KW = SAG - KENAR - 2 * KUTU_PAY;
  const IC = KX + 40;
  const KY = 480;
  const KH = 196;
  const BEN = 64;
  const BTR = 64;
  const F_EN = `700 ${BEN}px Fredoka`;
  const F_TR = `700 ${BTR}px Caveat`;
  const yb1 = KY + 76;
  const yb2 = yb1 + 92;
  const EK = 40;
  const yTR1 = KY + KH + 76;
  const yTR2 = yTR1 + 80;
  const FIG_Y = 900;
  const ZEMIN_Y = FIG_Y + 458;
  const ySU = 1015;
  const yHS1 = ySU + 97;
  const yHS2 = yHS1 + 76;
  const GW = 104;
  const GH = 76;
  const GA = 28;
  const GY = yHS2 + 74;

  // Yardımcı: İnce kalem oku (çok noktalı eğri + uç)
  const okYol = (pts, o) => {
    const govde = ciz(pts, {
      w: 4,
      renk: RT.ikincil,
      alfa: 0.85,
      uc0: 10,
      uc1: 14,
      amp: 0.7,
      bas: o.bas,
      sure: o.sure,
      tur: "isaret",
      ad: o.ad,
    });
    const n = pts.length;
    const a = pts[n - 2], b = pts[n - 1];
    const dx = b[0] - a[0], dy = b[1] - a[1];
    const l = Math.hypot(dx, dy) || 1;
    const ux = dx / l, uy = dy / l;
    const k = 20;
    const rot = (r) => [
      -(ux * Math.cos(r) - uy * Math.sin(r)) * k + b[0],
      -(ux * Math.sin(r) + uy * Math.cos(r)) * k + b[1],
    ];
    ciz([rot(0.5), b, rot(-0.5)], {
      duz: true,
      w: 3.6,
      renk: RT.ikincil,
      alfa: 0.85,
      bas: o.bas + o.sure - 2,
      sure: 6,
      uc0: 6,
      uc1: 6,
      amp: 0.4,
      ses: false,
      tur: "isaret",
      ad: `${o.ad}:uc`,
    });
    return govde;
  };

  // 1. Boş kart çerçevesi (yazısız, tek hareket)
  kutu(KX, KY, KW, KH, {
    bas: 0,
    sure: 12,
    w: 4,
    renk: RT.ikincil,
    ad: "kart kutusu",
  });
  not("kart kutusu (boş)", 0);

  // 2. Alt öğe grubu
  const F_SU = fr(wSu.t);
  const altOge = oge({ alfa: (f) => 1 - kis((f - F_SU) / 4) });

  // 3. Kart satır 1 My brother
  const kel1 = cumle([
    { s: wMy.s, f: fr(wMy.t) },
    { s: wBrother.s, f: fr(wBrother.t) },
  ], {
    x: IC,
    y: yb1,
    boyut: BEN,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
  });
  not("kart satır 1 (My)", fr(wMy.t));

  // 4. usually
  const wU = yazi(wUsually.s, {
    x: kel1[1].x1 + genislik(" ", F_EN) + EK,
    y: yb1,
    boyut: BEN,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
    bas: fr(wUsually.t),
    sure: 4,
  });
  not("usually (usually)", fr(wUsually.t));

  // 5. Kart satır 2 goes to school by bus.
  const kel2 = cumle([
    { s: wGoes.s, f: fr(wGoes.t) },
    { s: wTo.s, f: fr(wTo.t) },
    { s: wSchool.s, f: fr(wSchool.t) },
    { s: wBy.s, f: fr(wBy.t) },
    { s: wBus.s, f: fr(wBus.t) },
  ], {
    x: IC,
    y: yb2,
    boyut: BEN,
    aile: "Fredoka",
    agirlik: 700,
    renk: RT.murekkep,
  });
  not("kart satır 2 (goes)", fr(wGoes.t));

  // Ölçümler
  const cx = (wU.x0 + wU.x1) / 2;
  const cy = yb1 - BEN * 0.21;
  const rx = (wU.x1 - wU.x0) / 2 + 36;
  const ry = BEN * 0.72;

  const TR1 = "Kardeşim genellikle";
  const TR2 = "okula otobüsle gider.";
  const genX1 = SOL + genislik(TR1, F_TR);
  const genX2 = SOL + genislik(TR2, F_TR);
  const L2X1 = kel2[4].x1;

  const alW = eyGen("alışkanlık", BTR);
  const alX = SAG - 24 - alW;

  // Bekçiler (1–9)
  if (wU.x1 + 16 > KX + KW - 30 || kel2[4].x1 > KX + KW - 30) {
    throw new Error(
      `Bekçi: kart yazısı taşar (wU.x1 + 16: ${wU.x1 + 16}, kel2[4].x1: ${kel2[4].x1} > ${KX + KW - 30})`
    );
  }
  if (cx + rx + 2 > SAG - 120) {
    throw new Error(`Bekçi: oklar için sağ koridor yok (${cx + rx + 2} > ${SAG - 120})`);
  }
  if (L2X1 + 48 > SAG - 64 - 60) {
    throw new Error(`Bekçi: iki ok koridoru arası < 60 (${L2X1 + 48} > ${SAG - 64 - 60})`);
  }
  if (genX1 + 18 + 40 > L2X1 + 48) {
    throw new Error(`Bekçi: köprü okunun sola giden kolu yok (${genX1 + 18 + 40} > ${L2X1 + 48})`);
  }
  if (genX2 + 40 > alX) {
    throw new Error(`Bekçi: TR satır 2 alışkanlık'a değer (${genX2 + 40} > ${alX})`);
  }
  if (Math.max(genX1, genX2) > SAG) {
    throw new Error(`Bekçi: TR satırları sağ sınırı aştı (TR1: ${genX1}, TR2: ${genX2} > ${SAG})`);
  }
  if (yb2 - yb1 < BEN * 1.22 || yTR2 - yTR1 < BTR * 1.22) {
    throw new Error(
      `Bekçi: satır aralığı yetersiz (yb2 - yb1: ${yb2 - yb1} < ${BEN * 1.22}`
      + ` veya yTR2 - yTR1: ${yTR2 - yTR1} < ${BTR * 1.22})`
    );
  }
  if (KY - 10 < KUNYE.icerikBas || GY + GH + 10 > KUNYE.icerikSon
      || ZEMIN_Y + 6 > KUNYE.icerikSon) {
    throw new Error(
      `Bekçi: içerik dikey sınırı aşıldı (KY - 10: ${KY - 10} < ${KUNYE.icerikBas},`
      + ` GY + GH + 10: ${GY + GH + 10} > ${KUNYE.icerikSon},`
      + ` ZEMIN_Y + 6: ${ZEMIN_Y + 6} > ${KUNYE.icerikSon})`
    );
  }
  if (FIG_Y < yTR2 + BTR * 0.3 + 30) {
    throw new Error(`Bekçi: FIG_Y TR altında değil (${FIG_Y} < ${yTR2 + BTR * 0.3 + 30})`);
  }

  // 6. Oturan figür (kalem)
  const fig = await svgCiz("open-peeps/sitting-4.svg", {
    kutu: [KX, FIG_Y, 340, 450],
    bas: fr(wMy.t),
    sure: 51,
    azami: 60,
    kisaAtla: 0.004,
    w: 3.2,
    sesAralik: 8,
    oge: altOge,
  });
  not("oturan figür (My)", fr(wMy.t));

  // 7. Halka usually (sarı, tek vurgu)
  // Şef (kare turu 1–3): halka `l` tepesine ve `y` koluna değmesin: rx +36, ry 0,72 boy, eğim 0 (varsayılan -0,07).
  daire(cx, cy, rx, ry, {
    egim: 0,
    bas: fr(wUsually.t) + 4,
    sure: 12,
    ses: "tik",
    ad: "usually halka",
  });
  not("usually halka (usually)", fr(wUsually.t) + 4);

  // 8. Otobüs (kalem)
  const bus = await svgCiz("coco/bus.svg", {
    kutu: [KX + 380, FIG_Y + 250, 480, 200],
    bas: fr(wGoes.t),
    sure: 33,
    azami: 25,
    w: 3.8,
    sesAralik: 5,
    oge: altOge,
  });
  not("otobüs (goes)", fr(wGoes.t));

  // Bekçi 10 (svgCiz sonrası)
  if (fig.sinir.bottom > KUNYE.icerikSon || bus.sinir.right > SAG
      || bus.sinir.left < fig.sinir.right + 10) {
    throw new Error(
      `Bekçi: SVG sınır ihlali (fig.bottom: ${fig.sinir.bottom} > ${KUNYE.icerikSon},`
      + ` bus.right: ${bus.sinir.right} > ${SAG},`
      + ` bus.left: ${bus.sinir.left} < ${fig.sinir.right + 10})`
    );
  }

  // 9. Zemin çizgisi
  ciz([[KX, ZEMIN_Y], [KX + 300, ZEMIN_Y - 3], [KX + 560, ZEMIN_Y + 2], [SAG - 30, ZEMIN_Y]], {
    duz: true,
    w: 3.4,
    renk: RT.ikincil,
    alfa: 0.75,
    uc0: 10,
    uc1: 30,
    bas: fr(wBus.t),
    sure: 15,
    oge: altOge,
    ad: "zemin",
  });
  not("zemin (bus.)", fr(wBus.t));

  // 10. Soluk TR (seslendirilmez)
  yazi(TR1, {
    x: SOL,
    y: yTR1,
    boyut: BTR,
    aile: "Caveat",
    agirlik: 700,
    renk: RT.ikincil,
    bas: wBus.f1,
    sure: 8,
  });
  not("soluk TR 1 (bus.)", wBus.f1);

  yazi(TR2, {
    x: SOL,
    y: yTR2,
    boyut: BTR,
    aile: "Caveat",
    agirlik: 700,
    renk: RT.ikincil,
    bas: wBus.f1 + 4,
    sure: 8,
  });
  not("soluk TR 2 (bus.)", wBus.f1 + 4);

  // 11. Ok 1: halka → alışkanlık
  okYol([
    [cx + rx + 2, cy - 12],
    [SAG - 70, KY + 36],
    [SAG - 64, yTR2 - 130],
    [alX + alW * 0.6, yTR2 - BTR * 0.85 - 6],
  ], {
    bas: fr(wAliskanlik.t),
    sure: 10,
    ad: "ok alışkanlık",
  });
  not("ok alışkanlık (Alışkanlık)", fr(wAliskanlik.t));

  // 12. alışkanlık (Caveat 64, kartın sağ altı)
  elYazisi("alışkanlık", {
    x: alX,
    y: yTR2,
    boyut: BTR,
    renk: RT.murekkep,
    bas: fr(wAliskanlik.t) + 6,
    sure: 14,
  });
  not("alışkanlık (Alışkanlık)", fr(wAliskanlik.t) + 6);

  // 13. Ok 2 (köprü): halka → TR genellikle
  okYol([
    [cx + rx + 2, cy + 12],
    [L2X1 + 40, cy + 30],
    [L2X1 + 48, yTR1 - 52],
    [genX1 + 18, yTR1 - 22],
  ], {
    bas: fr(wIsareti.t),
    sure: 14,
    ad: "ok köprü",
  });
  not("ok köprü (işareti.)", fr(wIsareti.t));

  // 14. Figür + otobüs + zemin solar
  not("alt bölge solar (Şu)", F_SU);

  // 15. şu an (ikincil)
  const suAn = elYazisi("şu an", {
    x: SOL,
    y: ySU,
    boyut: BTR,
    renk: RT.ikincil,
    bas: F_SU + 4,
    sure: 10,
  });
  not("şu an (Şu)", F_SU + 4);

  // 16. şu an üstüne kalem çizgisi
  const basSuAnCizgi = Math.max(fr(wDegil.t), suAn.bit);
  ciz([[suAn.x0 - 8, ySU - BTR * 0.26 + 3], [suAn.x1 + 10, ySU - BTR * 0.30]], {
    duz: true,
    w: 5,
    renk: RT.murekkep,
    alfa: 0.9,
    uc0: 4,
    uc1: 6,
    amp: 0.4,
    bas: basSuAnCizgi,
    sure: 7,
    ses: "tik",
    tur: "isaret",
    ad: "şu an çizgi",
  });
  not("şu an çizgi (değil,)", basSuAnCizgi);

  // 17. Her sabah yedide (sözcük zamanlı)
  const hs = satir(["Her", "sabah", "yedide"], pen(s2.slice(13, 16)), {
    x: SOL,
    y: yHS1,
    boyut: BTR,
    renk: RT.murekkep,
  });
  not("Her sabah yedide (her)", fr(wHer.t));

  // 18. 5 gün kutusu (el çizimi, yazısız)
  for (let i = 0; i < 5; i++) {
    kutu(SOL + i * (GW + GA), GY, GW, GH, {
      bas: fr(wHer.t) + 3 * i,
      sure: 9,
      w: 3.4,
      renk: RT.ikincil,
      ad: `gün ${i + 1}`,
    });
    not(`gün ${i + 1} (her)`, fr(wHer.t) + 3 * i);
  }

  // 19. her sabah altçizgi (mürekkep, sarı DEĞİL)
  ciz([[hs[0].x0 - 4, yHS1 + 12], [hs[1].x1 + 6, yHS1 + 10]], {
    duz: true,
    w: 5,
    renk: RT.murekkep,
    alfa: 0.85,
    uc0: 6,
    uc1: 8,
    amp: 0.8,
    bas: wSabah.f1,
    sure: 8,
    ses: "tik",
    tur: "isaret",
    ad: "her sabah altçizgi",
  });
  not("her sabah altçizgi (sabah)", wSabah.f1);

  // 20. kalkarım.
  satir(["kalkarım."], pen(s2.slice(16, 17)), {
    x: SOL,
    y: yHS2,
    boyut: BTR,
    renk: RT.murekkep,
  });
  not("kalkarım. (kalkarım)", fr(wKalkarim.t));

  // 21. 5 tik (mürekkep), 5/5
  for (let i = 0; i < 5; i++) {
    const tcx = SOL + i * (GW + GA) + GW / 2;
    const tcy = GY + GH / 2 + 2;
    ciz([[tcx - 18, tcy + 1], [tcx - 5, tcy + 16], [tcx + 22, tcy - 19]], {
      w: 6,
      renk: RT.murekkep,
      alfa: 0.9,
      uc0: 5,
      uc1: 8,
      amp: 0.3,
      bas: fr(wYedide.t) + 6 * i,
      sure: 7,
      ses: "tik",
      tur: "isaret",
      ad: `tik ${i + 1}`,
    });
    not(`tik ${i + 1} (yedide)`, fr(wYedide.t) + 6 * i);
  }

  return S;
}

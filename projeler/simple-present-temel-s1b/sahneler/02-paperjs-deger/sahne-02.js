// Sahne 02 (simple-present-temel-s1b Shorts, huni v2, A/B kol b) — Değer: Paper.js, 1080x1920, 371 kare, t_bas 3.00.
// Kol b (KBC-0202S1, kanca = yanlis-cumle): kanca kuyruğu `Hata nerede?` + kırmızı ✗ + kanca satırı kayışı; 3 kanca izi
// (cümledeki goes uçuşsuz yazılır · yanlış cümlenin `go` sözcüğü soluk go kartı olur · soluk `Kardeşim gider:` goes'tan sonra).
import {
  sahneKur, RT, KUNYE, kis, yumus,
} from "/projeler/simple-present-temel-s1b/sahneler/02-paperjs-deger/kalem-paper.js";

export const KARE = 371, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS });
  const {
    fr, not, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, dinamik, svgCiz, oge, genislik, lerp,
  } = S;

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

  // s1 sözcükleri (kol b): 0 My · 2 go · 6 bus. · 7 Hata · 8 nerede?
  al(s1, 0, "My");
  al(s1, 2, "go");
  al(s1, 6, "bus.");
  const wNerede = al(s1, 8, "nerede?");

  // s2 sözcükleri: 0 My · 1 brother · 2 goes · 3 to · 4 school · 5 by · 6 bus.
  // · 7 He, · 8 she, · 9 it · 12 s · 13 gelir. · 14 I, · 15 you, · 16 we, · 17 they · 19 gelmez.
  const wMy = al(s2, 0, "My");
  const wBrother = al(s2, 1, "brother");
  const wGoes2 = al(s2, 2, "goes");
  const wTo = al(s2, 3, "to");
  const wSchool = al(s2, 4, "school");
  const wBy = al(s2, 5, "by");
  const wBus = al(s2, 6, "bus.");
  const wHe = al(s2, 7, "He,");
  const wShe = al(s2, 8, "she,");
  const wIt = al(s2, 9, "it");
  const wS = al(s2, 12, "s");
  const wGelir = al(s2, 13, "gelir.");
  const wI = al(s2, 14, "I,");
  const wYou = al(s2, 15, "you,");
  const wWe = al(s2, 16, "we,");
  const wThey = al(s2, 17, "they");
  const wGelmez = al(s2, 19, "gelmez.");

  // Kare sabitleri (§2)
  const F_CARPI = fr(wNerede.t);
  const F_KAY0 = fr(wNerede.t1);
  const F_KAY1 = F_KAY0 + 10;
  const F_MY = fr(wMy.t);
  const F_UC0 = fr(wGoes2.t) - 6;
  const F_UC1 = fr(wGoes2.t) + 3;
  const F_GO0 = F_UC1;
  const F_GO1 = F_GO0 + 12;
  const F_TR = fr(wGoes2.t1);   // kol b: soluk `Kardeşim gider:` goes söylendikten sonra belirir (söylenmez)
  const F_HE = fr(wHe.t);
  const F_SHE = fr(wShe.t);
  const F_IT = fr(wIt.t);
  const F_S = fr(wS.t);
  const F_GELIR = fr(wGelir.t);
  const F_I = fr(wI.t);
  const F_YOU = fr(wYou.t);
  const F_WE = fr(wWe.t);
  const F_THEY = fr(wThey.t);
  const F_DON0 = fr(wGelmez.t);
  const F_DON1 = F_DON0 + 10;

  // Sabitler (§1)
  const KENAR = KUNYE.kenar;
  const SAG = KUNYE.sag;
  const SOL = KENAR + 24;
  const KUTU_PAY = 10;
  const TR_X = 60, TR_Y = 560, B_TR = 72;
  const KANCA_Y = 620;
  const B_KART = 120, Y_KART = 750;
  const KART_MX = 250, KART_MY = 720;
  const KART_YARIM = 188;
  const KAY_DY = 260;
  const KX = KENAR + KUTU_PAY;
  const KW = SAG - KENAR - 2 * KUTU_PAY;
  const KY = KANCA_Y + KUTU_PAY;
  const KH = 220;
  const IC = KX + 40;
  const BEN = 72, ALT = 0.30;
  const yb1 = KY + 82;
  const yb2 = yb1 + 92;
  const OTOBUS = [726, 730, 220, 85];
  const F_EN = "700 72px Fredoka";
  const F_KART = "700 120px Fredoka";
  // es kayma payı: tire + 20 (tire 4 px içeride; daire payı 10 → daire tireye değmez, şef kare turu 1)
  const DX_ES = genislik("-", F_EN) + 20;
  const Y_ESIT = 950;
  const YA = 1100, YB = 1250, BSAT = 72;
  const OK_ARA = 20, OK_BOY = 64;
  const KUCUK = 0.6;
  const BEKLE_X = 842, BEKLE_Y = 949;
  // kol b yanlış cümle kartı (sahne 01 son hâli; değer kartıyla aynı kutu ve satırlar, kanca satırında)
  const GO_X = IC + genislik("My brother ", F_EN);        // yanlış cümledeki `go`
  const GO_CX = GO_X + genislik("go", F_EN) / 2;
  const GO_CY = yb1 - (Y_KART - KART_MY) * KUCUK;        // soluk go kartı ölçeğinde (0,6) aynı sözcük
  const X2_CX = 760, X2_CY = yb1 - 0.33 * BEN, X2_R = 32;  // ✗: satır 1'in sağ boşluğu

  // Hazır kart kutusu (ses yok, kare 0'da tam görünür)
  const kutuHazir = (x, y, w, h, o = {}) => {
    const k = [
      [[x - 6, y + 2], [x + w + 8, y - 2]],
      [[x + w + 2, y - 8], [x + w - 2, y + h + 9]],
      [[x + w + 7, y + h + 2], [x - 8, y + h - 2]],
      [[x + 2, y + h + 8], [x - 2, y - 10]],
    ];
    k.forEach((q, i) => {
      ciz([q[0], [(q[0][0] + q[1][0]) / 2 + 1.5 * (i % 2 ? 1 : -1), (q[0][1] + q[1][1]) / 2 + 1.2], q[1]], {
        w: o.w || 3.6,
        renk: o.renk || RT.ikincil,
        alfa: 0.9,
        bas: -40,
        sure: 4,
        uc0: 10,
        uc1: 12,
        oge: o.oge,
        ses: false,
        tur: "kart",
        ad: o.ad || "kutu",
      });
    });
  };

  // 1. kol b: yanlış cümle kartı hazır (kanca satırında; kayar, goes yazılırken söner; `go` ayrı öğe)
  const kay = { f0: F_KAY0, f1: F_KAY1, dx: 0, dy: KAY_DY };
  const yanlis = oge({ kay, alfa: (f) => 1 - kis((f - F_UC0) / (F_UC1 - F_UC0)) });
  yanlis.g.data = { kalemTur: "kart", kalemAd: "yanlış cümle kartı" };
  kutuHazir(KX, KY, KW, KH, { oge: yanlis, w: 4, renk: RT.ikincil, ad: "kutu yanlış" });
  const enHazir = (s, x, y, og) => yazi(s, {
    x, y, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: og,
  });
  enHazir("My brother", IC, yb1, yanlis);
  enHazir("to school by bus.", IC, yb2, yanlis);
  const goKelime = oge({ kay, alfa: (f) => (f < F_GO0 ? 1 : 0) });  // F_GO0'da soluk go kartına devreder
  enHazir("go", GO_X, yb1, goKelime);
  not("yanlış cümle kartı (hazır)", 0);

  // 2. kart go (kol b: F_GO0'a dek gizli; yanlış cümlenin `go` sözcüğünün yerinden çıkar, çerçevesi yolda belirir)
  const kartGo = { g: new P.Group({ applyMatrix: false }) };
  kartGo.g.data = { kalemTur: "kart", kalemAd: "kart go" };
  const kutuGo = { g: new P.Group({ applyMatrix: false }) };
  kartGo.g.addChild(kutuGo.g);
  kutuHazir(70, 630, 360, 180, { oge: kutuGo, w: 4, renk: RT.ikincil, ad: "kutu go" });
  yazi("go", {
    x: 250, y: Y_KART, boyut: B_KART, aile: "Fredoka", agirlik: 700,
    hizala: "orta", renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge: kartGo,
  });
  not("kart go (hazır)", 0);

  // 3. küçük figür + küçük otobüs hazır
  const eskiz = oge({});
  await svgCiz("open-peeps/standing-2.svg", {
    kutu: [700, 460, 60, 140], bas: -200, sure: 2, sessiz: true, w: 3.4, oge: eskiz,
  });
  await svgCiz("coco/bus.svg", {
    kutu: [770, 530, 190, 70], ayna: true, bas: -200, sure: 2, sessiz: true, w: 3.4, oge: eskiz,
  });
  not("figür ve otobüs (hazır)", 0);

  // 4-5. kol b: kırmızı kalem ✗ ("nerede?"), satır 1'in sağ boşluğunda; kartla kayar, kol a `?` gibi söner
  const xOge = oge({ kay, alfa: (f) => 1 - kis((f - F_UC0) / 8) });
  const xd = (a, b, c, bas, ses) => ciz([a, b, c], {
    w: 10, renk: RT.kirmizi, alfa: 0.95, amp: 0.5, bas, sure: 6, uc0: 6, uc1: 8, oge: xOge, ses, tur: "isaret", ad: "✗ nerede",
  });
  xd([X2_CX - X2_R, X2_CY - 0.9 * X2_R], [X2_CX + 0.05 * X2_R, X2_CY], [X2_CX + X2_R, X2_CY + X2_R], F_CARPI, undefined);
  xd([X2_CX + 0.92 * X2_R, X2_CY - X2_R], [X2_CX, X2_CY + 0.08 * X2_R], [X2_CX - 0.96 * X2_R, X2_CY + 0.94 * X2_R],
    F_CARPI + 7, false);
  not("✗ (nerede?)", F_CARPI);

  // 6. kanca satırı aşağı kayar
  not("kanca satırı kayar (nerede? sonu)", F_KAY0);

  // 7. EN kart kutusu
  kutu(KX, KY, KW, KH, { bas: F_KAY1, sure: 14, w: 4, renk: RT.ikincil, ad: "EN kart kutusu" });
  not("EN kart kutusu (My)", F_KAY1);

  // 8. TR satırı soluk Caveat (kol b: kancada söylenmez; goes bitince aynı yerde soluk belirir, sahne sonuna dek kalır)
  const trB = oge({ alfa: (f) => kis((f - F_TR) / 10) });
  yazi("Kardeşim gider:", {
    x: TR_X, y: TR_Y, boyut: B_TR, aile: "Caveat", agirlik: 700,
    renk: RT.ikincil, bas: -30, sure: 4, ses: false, oge: trB,
  });
  not("TR soluk belirir (goes sonu)", F_TR);

  // 9. figür + küçük otobüs solar
  eskiz.alfa = (f) => 1 - kis((f - F_MY) / 12);
  not("figür ve otobüs solar (My)", F_MY);

  // 10. büyük otobüs kalemle
  await svgCiz("coco/bus.svg", {
    kutu: OTOBUS, ayna: true, bas: F_MY, sure: fr(wBus.t) - F_MY,
    azami: 25, w: 4, sesAralik: 3,
  });
  not("büyük otobüs (My)", F_MY);

  // 11. EN cümle + karaoke
  const kel = cumle([
    { s: wMy.s, f: fr(wMy.t), satir: 0 },
    { s: wBrother.s, f: fr(wBrother.t), satir: 0 },
    { s: wTo.s, f: fr(wTo.t), satir: 1 },
    { s: wSchool.s, f: fr(wSchool.t), satir: 1 },
    { s: wBy.s, f: fr(wBy.t), satir: 1 },
    { s: wBus.s, f: fr(wBus.t), satir: 1 },
  ], {
    x: IC, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, aralik: 92,
  });
  not("EN cümle (My)", F_MY);

  // 12. goes kartı cümledeki yerine uçar
  not("yanlış cümle kartı söner (goes)", F_UC0);

  // 13. cümledeki goes
  const goX = kel[1].x1 + genislik(" ", F_EN);
  yazi("go", {
    x: goX, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700, bas: F_UC1, sure: 2,
  });
  const esOge = oge({});
  esOge.g.data = { kalemTur: "yazi", kalemAd: "es" };
  yazi("es", {
    x: goX + genislik("go", F_EN), y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700,
    bas: F_UC1, sure: 2, oge: esOge,
  });
  not("cümlede goes (goes)", F_UC1);

  // 14. karaoke
  const goesK = {
    x0: goX, x1: goX + genislik("goes", F_EN), y: yb1, boyut: BEN, bas: fr(wGoes2.t),
  };
  altCizgi([kel[0], kel[1], goesK, kel[2], kel[3], kel[4], kel[5]], { tut: 24, alt: ALT });
  not("karaoke (My)", F_MY);

  // 15. goes sarı alt çizgi (kalıcı)
  const yU = yb1 + BEN * ALT;
  ciz([[goX - 4, yU], [goX + genislik("goes", F_EN) + 4, yU - 2]], {
    duz: true, w: 9, renk: RT.vurguDolgu, alfa: 0.9, bas: F_UC1 + 2, sure: 6,
    tur: "isaret", ses: "tik", ad: "odak goes",
  });
  not("odak goes (goes)", F_UC1 + 2);

  // 16. kart go soluk, sağ kenarda bekler
  not("kart go beklemede (goes)", F_GO0);

  // 17. My brother → = he kalem oku
  ok([IC - 14, yb1 - 0.3 * BEN], [IC - 4, Y_ESIT - 0.3 * 72], {
    bas: F_HE, sure: 12, w: 6, uzun: 18, bukum: 0.05, yon: [-1, 0],
    renk: RT.murekkep, ad: "ok he",
  });
  not("ok he (He,)", F_HE);

  // 18. Caveat = he
  elYazisi("= he", {
    x: IC + 8, y: Y_ESIT, boyut: 72, renk: RT.murekkep, bas: F_HE + 4, sure: 14,
  });
  not("= he (He,)", F_HE + 4);

  // 19. satır A zamirleri
  let curXA = SOL;
  const yzHe = yazi("he", {
    x: curXA, y: YA, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: F_HE, sure: 4, olcek: true, ses: "tik",
  });
  curXA = yzHe.x1;
  const yzAyracA1 = yazi(" · ", {
    x: curXA, y: YA, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.ikincil, bas: F_SHE, sure: 4, ses: false,
  });
  curXA = yzAyracA1.x1;
  const yzShe = yazi("she", {
    x: curXA, y: YA, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: F_SHE, sure: 4, olcek: true, ses: "tik",
  });
  curXA = yzShe.x1;
  const yzAyracA2 = yazi(" · ", {
    x: curXA, y: YA, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.ikincil, bas: F_IT, sure: 4, ses: false,
  });
  curXA = yzAyracA2.x1;
  const yzIt = yazi("it", {
    x: curXA, y: YA, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: F_IT, sure: 4, olcek: true, ses: "tik",
  });
  const xA1 = yzIt.x1;
  not("satır A he (He,)", F_HE);
  not("satır A she (she,)", F_SHE);
  not("satır A it (it)", F_IT);

  // 20. goes → go-es
  esOge.kay = { f0: F_S, f1: F_S + 6, dx: DX_ES, dy: 0 };
  yazi("-", {
    x: goX + genislik("go", F_EN) + 4, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: F_S + 6, sure: 4,
  });
  not("go-es ayrılır (s)", F_S);
  not("tire eklenir (s)", F_S + 6);

  // 21. es sarı daire
  const cxEs = goX + genislik("go", F_EN) + DX_ES + genislik("es", F_EN) / 2;
  daire(cxEs, yb1 - 0.3 * BEN, genislik("es", F_EN) / 2 + 10, BEN * 0.5, {
    bas: F_S + 8, sure: 18, a0: -2.0, ad: "es daire",
  });
  not("es daire (s)", F_S + 8);

  // 22. satır A oku + goes
  ok([xA1 + OK_ARA, YA - 0.3 * BSAT], [xA1 + OK_ARA + OK_BOY, YA - 0.3 * BSAT], {
    bas: F_GELIR, sure: 10, w: 6, uzun: 18, bukum: 0.04, renk: RT.murekkep, ad: "ok A",
  });
  const yzGoesA = yazi("goes", {
    x: xA1 + 2 * OK_ARA + OK_BOY, y: YA, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: F_GELIR + 6, sure: 4, olcek: true, ses: "tik",
  });
  not("satır A ok (gelir.)", F_GELIR);
  not("satır A goes (gelir.)", F_GELIR + 6);

  // 23. satır B zamirleri
  let curXB = SOL;
  const yzI = yazi("I", {
    x: curXB, y: YB, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: F_I, sure: 4, olcek: true, ses: "tik",
  });
  curXB = yzI.x1;
  const yzAyracB1 = yazi(" · ", {
    x: curXB, y: YB, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.ikincil, bas: F_YOU, sure: 4, ses: false,
  });
  curXB = yzAyracB1.x1;
  const yzYou = yazi("you", {
    x: curXB, y: YB, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: F_YOU, sure: 4, olcek: true, ses: "tik",
  });
  curXB = yzYou.x1;
  const yzAyracB2 = yazi(" · ", {
    x: curXB, y: YB, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.ikincil, bas: F_WE, sure: 4, ses: false,
  });
  curXB = yzAyracB2.x1;
  const yzWe = yazi("we", {
    x: curXB, y: YB, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: F_WE, sure: 4, olcek: true, ses: "tik",
  });
  curXB = yzWe.x1;
  const yzAyracB3 = yazi(" · ", {
    x: curXB, y: YB, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.ikincil, bas: F_THEY, sure: 4, ses: false,
  });
  curXB = yzAyracB3.x1;
  const yzThey = yazi("they", {
    x: curXB, y: YB, boyut: BSAT, aile: "Fredoka", agirlik: 700,
    renk: RT.murekkep, bas: F_THEY, sure: 4, olcek: true, ses: "tik",
  });
  const xB1 = yzThey.x1;
  not("satır B I (I,)", F_I);
  not("satır B you (you,)", F_YOU);
  not("satır B we (we,)", F_WE);
  not("satır B they (they)", F_THEY);

  // 24. soluk go kartı satır B'nin yanına döner
  const DON_X = xB1 + 2 * OK_ARA + OK_BOY + KART_YARIM * KUCUK;
  const DON_Y = YB - (Y_KART - KART_MY) * KUCUK;
  not("kart go döner (gelmez.)", F_DON0);

  // 25. satır B oku
  ok([xB1 + OK_ARA, YB - 0.3 * BSAT], [xB1 + OK_ARA + OK_BOY, YB - 0.3 * BSAT], {
    bas: F_DON0, sure: 10, w: 6, uzun: 18, bukum: 0.04, renk: RT.murekkep, ad: "ok B",
  });
  not("satır B ok (gelmez.)", F_DON0);

  // 26. s yuvası + kırmızı kalem çizgisi
  const sYuva = { g: new P.Group({ applyMatrix: false }) };
  sYuva.g.opacity = 0.5;
  kartGo.g.addChild(sYuva.g);
  const sYazi = yazi("s", {
    x: 250 + genislik("go", F_KART) / 2 + 6, y: Y_KART, boyut: B_KART, aile: "Fredoka",
    agirlik: 700, renk: RT.ikincil, bas: F_DON1, sure: 4, oge: sYuva,
  });
  const sx0 = sYazi.x0, sx1 = sYazi.x1;
  ciz([[sx0 - 8, Y_KART + 12], [sx1 + 8, Y_KART - 66]], {
    duz: true, w: 12, renk: RT.kirmizi, alfa: 0.95, bas: F_DON1 + 3, sure: 8,
    oge: kartGo, tur: "isaret", ad: "s yuvası kırmızı",
  });
  not("s yuvası (gelmez.)", F_DON1);
  not("s yuvası kırmızı (gelmez.)", F_DON1 + 3);

  // Dinamik matris ve ölçek kapları (§4)
  dinamik((f) => {
    // kartGo evreleri (kol b: F_GO0'a dek gizli; F_GO0'da yanlış cümledeki `go` yerinden çıkar, çerçeve yolda belirir)
    let cxGo, cyGo, sGo, alfaGo;
    kutuGo.g.opacity = kis((f - F_GO0) / (F_GO1 - F_GO0));
    if (f < F_GO0) {
      cxGo = GO_CX; cyGo = GO_CY + KAY_DY; sGo = KUCUK; alfaGo = 0;
    } else if (f <= F_GO1) {
      const u = yumus((f - F_GO0) / (F_GO1 - F_GO0));
      cxGo = lerp(GO_CX, BEKLE_X, u);
      cyGo = lerp(GO_CY + KAY_DY, BEKLE_Y, u);
      sGo = KUCUK;
      alfaGo = lerp(1, 0.4, u);
    } else if (f <= F_DON0) {
      cxGo = BEKLE_X;
      cyGo = BEKLE_Y;
      sGo = KUCUK;
      alfaGo = 0.4;
    } else if (f <= F_DON1) {
      const u = yumus((f - F_DON0) / (F_DON1 - F_DON0));
      cxGo = lerp(BEKLE_X, DON_X, u);
      cyGo = lerp(BEKLE_Y, DON_Y, u);
      sGo = KUCUK;
      alfaGo = lerp(0.4, 1, u);
    } else {
      cxGo = DON_X;
      cyGo = DON_Y;
      sGo = KUCUK;
      alfaGo = 1;
    }
    kartGo.g.matrix = new P.Matrix().translate(cxGo, cyGo).scale(sGo).translate(-250, -720);
    kartGo.g.opacity = alfaGo;
  });

  // Bekçiler (§5)
  if (TR_X + genislik("Kardeşim gider:", "700 72px Caveat") > SAG) {
    const trW = genislik("Kardeşim gider:", "700 72px Caveat");
    throw new Error(`Bekçi: TR_X + genislik("Kardeşim gider:") > SAG (${TR_X + trW} > ${SAG})`);
  }
  const satir1KaymisSonu = goX + genislik("go", F_EN) + DX_ES + genislik("es", F_EN) + 12;
  if (satir1KaymisSonu > OTOBUS[0] - 14) {
    throw new Error(`Bekçi: Satır 1 kaymış sonu > OTOBUS[0] - 14 (${satir1KaymisSonu} > ${OTOBUS[0] - 14})`);
  }
  if (kel[5].x1 > OTOBUS[0] - 20) {
    throw new Error(`Bekçi: Satır 2 sonu > OTOBUS[0] - 20 (${kel[5].x1} > ${OTOBUS[0] - 20})`);
  }
  if (OTOBUS[0] + OTOBUS[2] > SAG - 8) {
    throw new Error(`Bekçi: OTOBUS sağ ucu > SAG - 8 (${OTOBUS[0] + OTOBUS[2]} > ${SAG - 8})`);
  }
  if (KX + KW > KUNYE.sag - KUTU_PAY) {
    throw new Error(`Bekçi: KX + KW > KUNYE.sag - KUTU_PAY (${KX + KW} > ${KUNYE.sag - KUTU_PAY})`);
  }
  if (BEKLE_X + KART_YARIM * KUCUK > SAG - 4) {
    throw new Error(`Bekçi: BEKLE_X + KART_YARIM * KUCUK > SAG - 4 (${BEKLE_X + KART_YARIM * KUCUK} > ${SAG - 4})`);
  }
  if (yzGoesA.x1 > SAG) {
    throw new Error(`Bekçi: Satır A goes x1 > SAG (${yzGoesA.x1} > ${SAG})`);
  }
  if (DON_X + KART_YARIM * KUCUK > SAG - 4) {
    throw new Error(`Bekçi: DON_X + KART_YARIM * KUCUK > SAG - 4 (${DON_X + KART_YARIM * KUCUK} > ${SAG - 4})`);
  }
  if (TR_Y - B_TR * 0.9 < KUNYE.icerikBas) {
    throw new Error(`Bekçi: TR_Y - B_TR * 0.9 < KUNYE.icerikBas (${TR_Y - B_TR * 0.9} < ${KUNYE.icerikBas})`);
  }
  if (DON_Y + 100 * KUCUK > KUNYE.icerikSon) {
    throw new Error(`Bekçi: DON_Y + 100 * KUCUK > KUNYE.icerikSon (${DON_Y + 100 * KUCUK} > ${KUNYE.icerikSon})`);
  }
  if (YB + BSAT * 0.3 > KUNYE.icerikSon) {
    throw new Error(`Bekçi: YB + BSAT * 0.3 > KUNYE.icerikSon (${YB + BSAT * 0.3} > ${KUNYE.icerikSon})`);
  }
  // kol b: ✗ satır 1'in sağ boşluğunda ve kartın içinde; kanca işaretleri goes yazılmadan söner
  const s1Sonu = IC + genislik("My brother go", F_EN);
  if (X2_CX - X2_R - 10 < s1Sonu + 40 || X2_CX + X2_R + 10 > KX + KW - 20) {
    throw new Error(`Bekçi: ✗ yeri (${X2_CX - X2_R}..${X2_CX + X2_R}) satır 1 sonu ${s1Sonu} / kart sağı dışında`);
  }
  if (F_CARPI + 13 > F_KAY0) throw new Error(`Bekçi: ✗ kayıştan önce bitmiyor (${F_CARPI + 13} > ${F_KAY0})`);
  if (F_KAY1 > F_MY) throw new Error(`Bekçi: kanca satırı kayışı My'den sonra bitiyor (${F_KAY1} > ${F_MY})`);
  if (F_TR <= wGoes2.f) throw new Error(`Bekçi: soluk TR goes'tan önce (${F_TR} <= ${wGoes2.f})`);

  return S;
}

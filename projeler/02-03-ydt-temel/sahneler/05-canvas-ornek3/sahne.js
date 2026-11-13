// SAHNE 05 — Örnek 3/3 (düz canvas, 522 kare, t_bas 51,57; cümle 5). 02-03 YDT temel.
// Kendini çizen kalem; zaman yalnız kare numarasından; sözcük zamanları ortak/anlatim/sozcukler.json.
// Kök: "It is getting harder and harder to find a good job nowadays." (yükselen basamaklar + ok, laptop, CHANGING).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, elips, ok, kutu, altCizgi } from "./sahne-ortak.js";

const KARE = 522, TBAS = 51.57, ICERIK = 510;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3", cumle: 5 });
const KOKDIZ = "/projeler/02-03-ydt-temel/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const IKINCIL = RT.ikincil, SARI = RT.vurgu, DOLGU = RT.vurguDolgu;
const FF = (b) => `700 ${b}px Fredoka`;
const t = (i) => S.sozc[i].t0;   // cümle 5: 0 Üçüncü · 1 örnek. · 2–13 kök · 14–18 TR · 19–22 Nowadays da … · 23–27 Üstelik … var. · 28–32 Bu ifade … söyler.
// El yazısı penceresi: her sözcük kendi t0'ından sonraki sözcüğün t0'ına dek (kısa pencere uzar)
const pen = (a, n) => S.sozc.slice(a, a + n).map((w, i, d) => ({ t0: w.t0,
  t1: i < n - 1 ? d[i + 1].t0 : w.t1 }));

async function kur() {
  await S.kur();

  // 52,12 Üçüncü: daire içinde 3 (ilk 12 kare boş) · 52,60 örnek.: tek kart (0,8 sn)
  S.koy(S.daireSayi(3, 196, 176, t(0)));
  S.koy(S.kart({ x: 140, y: 250, w: 1640, h: 450, tb: t(1), tohum: 6, kutuSure: 0.2,
    kutuAralik: 0.2, satirlar: [] }));

  // 53,41–57,00 kök (Fredoka 80, 3 satır: 3/5/4 sözcük), sözcük zamanlı; sarı alt çizgi kayar
  const cum = S.cumleYaz({ sozcukler: S.sozc.slice(2, 14), x: 230, y: 400, maxGen: 1100,
    font: FF(80), satirH: 112, satirSay: [3, 5, 4], bosluk: 4 });
  const kel = (i) => cum.kel[i];   // 0 It 1 is 2 getting 3 harder 4 and 5 harder 6 to 7 find 8 a 9 good 10 job 11 nowadays.
  const A = kel(3), B = kel(5), N = kel(11);
  // 54,05 harder: `harder and harder` sarı belirteç (yazının altında; önce koy = yazı üstte)
  S.koy(S.darbe([[A.x - 8, A.y - 26], [B.x + B.w + 8, A.y - 30]], { duz: true, w: 56, renk: DOLGU,
    alfa: 0.65, uc0: 6, uc1: 14, tohum: 93 }, t(5), 1.0, 0.5));
  S.koy(cum);

  // 53,81 getting · 54,05 harder · 54,49 and · 54,73 harder: dört basamak yükselir (sağ, kartın içinde)
  [[1260, 60, 4], [1330, 110, 5], [1400, 160, 6], [1470, 210, 7]].forEach(([x, h, i], k) => {
    S.koy(S.darbeler(kutu(x, 600 - h, 50, h, 70 + k), { w: 3.6, renk: IKINCIL, uc0: 8, uc1: 14 },
      t(i), 0.08, 0.05, 0.5));
  });
  // 54,80: yükselen sarı ok basamakların üstünde
  S.koy(S.darbeler(ok([1250, 455], [1590, 300], 8), { w: 7, renk: SARI, uc0: 10, uc1: 14 },
    t(7) + 0.07, 0.45, 0.3, 0.5));
  // 56,13 nowadays.: sarı daire
  S.koy(S.darbe(altCizgi(N.x - 2, N.x + N.w + 2, N.y + 26, 31),
    { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14 }, t(13), 0.4, 0.55));   // halka yerine el altçizgisi (13.11 QA)

  // 57,34–59,90 Bugünlerde iş bulmak gittikçe zorlaşıyor.: Türkçe çeviri (el yazısı 48, y 785)
  S.koy(S.elYazisi({ metin: "Bugünlerde iş bulmak gittikçe zorlaşıyor.", x: 140, y: 785, boy: 48,
    renk: IKINCIL, sozcukler: pen(14, 5) }));


  // 63,83 harder: `harder and harder` sarı daire · 64,79 harder: ok ucunda parıltı
  S.koy(S.darbe(altCizgi(A.x - 2, B.x + B.w + 2, A.y + 26, 33),
    { w: 8, renk: SARI, alfa: 0.9, uc0: 8, uc1: 14 }, t(24), 0.45, 0.55));   // halka yerine el altçizgisi (13.11 QA)
  S.koy(S.parilti(1590, 300, t(26), 24));

  // 66,20 Bu: basamaklardan etikete ok · 67,44 değiştiğini: CHANGING · 68,00 söyler.: parıltı
  S.koy(S.darbeler(ok([1385, 642], [1385, 792], 4), { w: 6.5, renk: SARI, uc0: 10, uc1: 14 },
    t(28), 0.35, 0.2, 0.5));
  S.koy(S.elYazisi({ metin: "CHANGING", x: 1190, y: 905, boy: 110, renk: SARI,
    sozcukler: [{ t0: t(31), t1: t(32) }] }));
  S.koy(S.parilti(1690, 840, t(32), 24));
}

surucu(kur, (f) => S.kare(f), KARE);

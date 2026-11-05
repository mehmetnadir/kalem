// SAHNE 04 (DİKEY 1080x1920) — Örnek 2 (düz canvas, 566 kare, t_bas 29,35; cümle 4).
// Zaman yalnız kare numarasından.
// Bantlar: HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 (sahne-ortak.js çizer)
// · platform boş. Yerleşim BRIEF-DIKEY §4.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, ok, elips, olc, yavasla, lerp } from "./sahne-ortak.js";

const KARE = 566, TBAS = 29.35, ICERIK = 554;
const KOKDIZ = "/projeler/simple-past-temel-dikey/ortak/cizim";
const S = new Sahne({
  tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 2 / 3", cumle: 4
});
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, SARI = RT.vurgu, KIRMIZI = RT.kirmizi, IKINCIL = RT.ikincil;
const FF = (b) => `700 ${b}px Fredoka`;
// El yazısı (tegaki Caveat, dalga 5b / K26): sözcük penceresi = anlatım t0/t1 (küresel sn)
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

// Öğeleri tek grupta toplar;
// f0–f1 arası dy kadar aşağı iner (boyut korunur) ve alfa 1 → a1 olur.
const grupla = (liste, k) => ({ ciz: (ctx, f) => {
  const u = yavasla((f - k.f0) / (k.f1 - k.f0));
  ctx.save();
  ctx.translate(0, (k.dy || 0) * u);
  ctx.globalAlpha *= lerp(1, k.a1 == null ? 1 : k.a1, u);
  if (ctx.globalAlpha > 0.01) for (const e of liste) e.ciz(ctx, f);
  ctx.restore();
} });

async function kur() {
  await S.kur();
  const [figur, ucak, kitap, takvim] = await Promise.all([
    svgOku("open-peeps/standing-5.svg"), svgOku("tabler/plane.svg"),
    svgOku("tabler/book.svg"), svgOku("tabler/calendar.svg")
  ]);

  // 29,35–30,39 kart (tam genişlik, 4 px kalem çizgisi);
  // sayı çipi HUD sağ üstte (ilk 12 kare boş)
  S.koy(S.darbeler(
    kutu(48, 372, 984, 276, 71), { w: 4, renk: KREM, uc0: 10, uc1: 18 },
    S.zm(12), 0.14, 0.1, 0.55
  ));

  // 30,64–33,60 cümle (kart içi, Fredoka ≤ 72, 2 satır) + sarı alt çizgi
  const fs = Math.max(
    64, Math.min(72, Math.floor(72 * 900 / olc(FF(72), "My uncle went to London")))
  );
  const cum = S.koy(S.cumleYaz({
    sozcukler: S.dizi("My", 30.64, 8), x: 96, y: 450, maxGen: 900,
    font: FF(fs), satirH: 86, bosluk: 8
  }));
  const kel = (ad) => cum.kel.find((k) => k.m.replace(/[.,?!:]/g, "") === ad);
  S.koy(S.halka(kel("ago"), 32.64, 0.3, 11, 8));

  // 33,85–36,65 Türkçe çeviri (Caveat 64 murekkep, kart içi; pencere: 6 sözcük)
  S.koy(S.elYazisi({
    metin: "Amcam iki yıl önce Londra'ya gitti.", x: 96, y: 610, boy: 64, renk: KREM,
    sozcukler: pen("Amcam", 33.85, 6)
  }));

  // 30,8–33,0 orta: ayakta figür (430 px) + uçak, 3 hız çizgisi;
  // 35,7–36,5'te figür alt bölgeye (960–1390)
  // iner (boyutu korunur, 430 px), uçak + hız çizgileri solar;
  // zaman şeridi üstte (660–950) kurulur
  const grup = [], ucakGrup = [];
  const figCiz = S.cizim({
    svg: figur, kutu: { x: 60, y: 700, w: 340, h: 430 }, ad: "figur", esik: 0.004,
    enCok: 60, w: 4.4, tb: 30.8, sure: 1.6, olayEnCok: 7
  });
  grup.push(figCiz);
  ucakGrup.push(S.cizim({
    svg: ucak, kutu: { x: 580, y: 725, w: 440, h: 440 }, ad: "ucak", enCok: 12,
    w: 4.4, tb: 31.9, sure: 0.9, olayEnCok: 4
  }));
  [[440, 905, 565], [470, 945, 575], [450, 985, 560]].forEach(([x0, y, x1], i) => {
    ucakGrup.push(S.darbe(
      [[x0, y], [(x0 + x1) / 2, y + 1], [x1, y]],
      { w: 9, renk: SARI, alfa: 0.85, uc0: 8, uc1: 22, duz: true, tohum: 40 + i },
      32.75 + i * 0.12, 0.22, i === 0 ? 0.5 : false
    ));
  });
  S.koy(grupla(grup, { f0: S.fr(35.7), f1: S.fr(36.5), dy: 260 }));
  S.koy(grupla(ucakGrup, { f0: S.fr(35.7), f1: S.fr(36.3), a1: 0 }));
  S.koy(S.parilti(1000, 760, 33.0, 26));

  // 36,73–39,13 takvim şeridi (y 925–1200):
  // `two years ago`, 4 kutu, sağda now noktası, sola giden ok `ago = önce`, tik
  const yKutu = 735, kh = 80, xs = 48, yOk = yKutu + 125;
  // 36,73 anlatımsız etiket `two years ago` (Ago, 36,73–37,45): hedef 0,7 sn → 37,43
  S.koy(S.elYazisi({
    metin: "two years ago", x: xs, y: yKutu - 22, boy: 64, renk: SARI, tb: 36.73, sure: 0.7
  }));
  for (let i = 0; i < 4; i++) {
    S.koy(S.darbeler(
      kutu(xs + 165 * i, yKutu, 150, kh, 20 + i),
      { w: 4, renk: KREM, uc0: 8, uc1: 14 }, 36.85 + i * 0.2, 0.12, 0.07, 0.45
    ));
  }
  S.koy(S.cizim({
    svg: takvim, kutu: { x: 725, y: yKutu - 5, w: 90, h: 90 }, ad: "takvim",
    enCok: 8, w: 4, tb: 37.0, sure: 0.5, olayEnCok: 1, nefes: false
  }));
  const nx = 940, ny = yKutu + kh / 2, nf = S.fr(38.7);
  S.olay(nf, "tik", 0.5);
  S.koy({ ciz: (ctx, f) => {
    const u = Math.min(1, Math.max(0, (f - nf) / 8)); if (u <= 0) return;
    ctx.save();
    ctx.fillStyle = renkCoz(SARI);
    ctx.beginPath();
    ctx.arc(nx, ny, 17 * u, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  } });
  S.koy(S.nabiz(nx, ny, 17, 38.7));
  // 38,85 anlatımsız etiket `now`: hedef 0,45 sn → 39,30
  S.koy(S.elYazisi({
    metin: "now", x: nx - 36, y: yKutu - 22, boy: 64, renk: SARI, tb: 38.85, sure: 0.45,
    ses: false
  }));
  S.koy(S.darbeler(
    ok([nx + 10, yOk], [xs + 20, yOk], 3),
    { w: 9, renk: SARI, uc0: 10, uc1: 14 }, 37.2, 0.2, 0.12, 0.5
  ));
  // 37,49–37,89 `ago =` (yani 37,49–37,85): hedef 0,4 sn; `önce` 38,01–38,73 (pencere);
  // `önce` x = `ago =` genişliği + boşluk (0,3 em)
  const agoYaz = S.elYazisi({
    metin: "ago =", x: xs, y: yOk + 78, boy: 64, renk: SARI, tb: 37.49, sure: 0.4
  });
  S.koy(agoYaz);
  S.koy(S.elYazisi({
    metin: "önce", x: xs + agoYaz.w + 0.3 * 64, y: yOk + 78, boy: 64, renk: KREM,
    sozcukler: pen("önce:", 38.01, 1)
  }));
  // 38,77–39,93 `zaman belli` (pencere: zaman 38,77–39,05 · belli 39,13–39,93);
  // tik yazı bitince
  const zx = 520;
  const zYaz = S.elYazisi({
    metin: "zaman belli", x: zx, y: yOk + 78, boy: 64, renk: KREM,
    sozcukler: pen("zaman", 38.77, 2)
  });
  S.koy(zYaz);
  const zw = zYaz.w;
  S.koy(S.darbeler([[[zx + zw + 22, yOk + 50], [zx + zw + 40, yOk + 70], [zx + zw + 76, yOk + 22]]],
    { w: 9, renk: SARI, uc0: 5, uc1: 8, duz: true }, 39.8, 0.25, 0.3, 0.5));

  // 40,08–42,24 -ed (40,56) kırmızı çizgiyle yok; go (41,84) sarı daire
  // alt bölge sağ sütun (x 470–1032),
  // Fredoka 96: satır 1 taban y 1075 (-ed), satır 2 taban y 1320 (go → went)
  const R1 = 1075, R2 = 1320, X0 = 470, FS = 96;
  const ed = olc(FF(FS), "-ed"), gx = X0, gw = olc(FF(FS), "go");
  S.koy(S.metinPop({
    parca: [["-ed", KREM]], x: X0, y: R1, font: FF(FS), tb: 40.56, sure: 0.3, ses: 0.5
  }));
  S.koy(S.darbe([[X0 - 18, R1 - 34], [X0 + ed / 2, R1 - 38], [X0 + 22 + ed, R1 - 30]], { w: 12,
    renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 14, duz: true, tohum: 90 }, 40.9, 0.3, 0.6));
  S.koy(S.metinPop({
    parca: [["go", KREM]], x: gx, y: R2, font: FF(FS), tb: 41.84, sure: 0.3, ses: 0.5
  }));
  S.koy(S.darbe(elips(gx + gw / 2, R2 - 33, gw / 2 + 24, 66, -0.05, 31), {
    w: 9, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30
  }, 42.0, 0.35, 0.55));

  // 43,51–44,71 go -> kalem oku -> went (Fredoka 96, sarı)
  S.koy(S.darbeler(ok([gx + gw + 30, R2 - 37], [gx + gw + 108, R2 - 37], 5), {
    w: 9, renk: SARI, uc0: 10, uc1: 14
  }, 43.51, 0.2, 0.12, 0.5));
  const wx = gx + gw + 124, ww = olc(FF(FS), "went");
  S.koy(S.metinPop({
    parca: [["went", SARI]], x: wx, y: R2, font: FF(FS), tb: 44.71, sure: 0.35, ses: 0.8,
    turu: "vurus"
  }));

  // 45,59–46,39 ezberle + küçük kitap (sağ sütun üst); go -> went kutuya alınır
  S.koy(S.cizim({
    svg: kitap, kutu: { x: 870, y: 975, w: 140, h: 140 }, ad: "kitap", enCok: 8, w: 4,
    tb: 45.85, sure: 0.5, olayEnCok: 2, nefes: false
  }));
  // 45,59 anlatımsız etiket `ezberle` (ezberlersin 46,39–47,35): hedef 0,6 sn → 46,19
  S.koy(S.elYazisi({
    metin: "ezberle", x: 836, y: 1180, boy: 64, renk: KREM, tb: 45.59, sure: 0.6
  }));
  S.koy(S.parilti(1010, 975, 46.3, 24));
  S.koy(S.darbeler(kutu(gx - 28, R2 - 100, wx + ww - gx + 56, 130, 77), {
    w: 4, renk: IKINCIL, uc0: 10, uc1: 18
  }, 45.65, 0.16, 0.1, 0.5));
}

surucu(kur, (f) => S.kare(f), KARE);

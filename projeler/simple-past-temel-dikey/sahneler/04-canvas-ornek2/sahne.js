// SAHNE 04 (DİKEY 1080x1920) — Örnek 2 (düz canvas, 566 kare, t_bas 29,35; cümle 4). Zaman yalnız kare numarasından.
// Bantlar: HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 (sahne-ortak.js çizer) · platform boş. Yerleşim BRIEF-DIKEY §4.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, kutu, ok, elips, olc, yavasla, lerp } from "./sahne-ortak.js";

const KARE = 566, TBAS = 29.35, ICERIK = 554;
const KOKDIZ = "/projeler/simple-past-temel-dikey/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 2 / 3", cumle: 4 });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, SARI = RT.vurgu, KIRMIZI = RT.kirmizi, IKINCIL = RT.ikincil;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

// Öğeleri tek grupta toplar; f0–f1 arası (s, cx, cy) noktasına doğru küçülür (yer açmak için, kaybolmaz).
const grupla = (liste, k) => ({ ciz: (ctx, f) => {
  const u = yavasla((f - k.f0) / (k.f1 - k.f0)), s = lerp(1, k.s, u);
  ctx.save(); ctx.translate(k.cx, k.cy); ctx.scale(s, s); ctx.translate(-k.cx, -k.cy);
  for (const e of liste) e.ciz(ctx, f);
  ctx.restore();
} });

async function kur() {
  await S.kur();
  const [figur, ucak, kitap, takvim] = await Promise.all([svgOku("open-peeps/standing-5.svg"), svgOku("tabler/plane.svg"),
    svgOku("tabler/book.svg"), svgOku("tabler/calendar.svg")]);

  // 29,35–30,39 kart (tam genişlik, 4 px kalem çizgisi); sayı çipi HUD sağ üstte (ilk 12 kare boş)
  S.koy(S.darbeler(kutu(48, 372, 984, 276, 71), { w: 4, renk: KREM, uc0: 10, uc1: 18 }, S.zm(12), 0.14, 0.1, 0.55));

  // 30,64–33,60 cümle (kart içi, Fredoka ≤ 72, 2 satır) + sarı alt çizgi
  const fs = Math.max(64, Math.min(72, Math.floor(72 * 900 / olc(FF(72), "My uncle went to London"))));
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("My", 30.64, 8), x: 96, y: 450, maxGen: 900, font: FF(fs), satirH: 86, bosluk: 8 }));
  const kel = (ad) => cum.kel.find((k) => k.m.replace(/[.,?!:]/g, "") === ad);
  S.koy(S.halka(kel("ago"), 32.64, 0.3, 11, 8));

  // 33,85–35,57 Türkçe çeviri (Caveat 64 murekkep, kart içi)
  S.koy(S.not({ parca: [["Amcam iki yıl önce Londra'ya gitti.", KREM]], x: 96, y: 610, tb: 33.85, sure: 0.9, font: CV(64) }));

  // 30,8–33,0 orta: ayakta figür + uçak (430 px), uçağın arkasında 3 hız çizgisi; 33,9'dan sonra küçülüp yukarıda toplanır
  const grup = [];
  grup.push(S.cizim({ svg: figur, kutu: { x: 60, y: 700, w: 340, h: 430 }, ad: "figur", esik: 0.004, enCok: 60, w: 4.4, tb: 30.8, sure: 1.6,
    olayEnCok: 7 }));
  grup.push(S.cizim({ svg: ucak, kutu: { x: 580, y: 725, w: 440, h: 440 }, ad: "ucak", enCok: 12, w: 4.4, tb: 31.9, sure: 0.9, olayEnCok: 4 }));
  [[440, 905, 565], [470, 945, 575], [450, 985, 560]].forEach(([x0, y, x1], i) => {
    grup.push(S.darbe([[x0, y], [(x0 + x1) / 2, y + 1], [x1, y]], { w: 9, renk: SARI, alfa: 0.85, uc0: 8, uc1: 22, duz: true, tohum: 40 + i },
      32.75 + i * 0.12, 0.22, i === 0 ? 0.5 : false));
  });
  S.koy(grupla(grup, { f0: S.fr(35.7), f1: S.fr(36.5), s: 0.5, cx: 540, cy: 700 }));
  S.koy(S.parilti(1000, 760, 33.0, 26));

  // 36,73–39,13 takvim şeridi (y 925–1200): `two years ago`, 4 kutu, sağda now noktası, sola giden ok `ago = önce`, tik
  const yKutu = 1000, kh = 80, xs = 48, yOk = 1128;
  S.koy(S.not({ parca: [["two years ago", SARI]], x: xs, y: yKutu - 22, tb: 36.73, sure: 0.5, font: CV(64) }));
  for (let i = 0; i < 4; i++) {
    S.koy(S.darbeler(kutu(xs + 165 * i, yKutu, 150, kh, 20 + i), { w: 4, renk: KREM, uc0: 8, uc1: 14 }, 36.85 + i * 0.2, 0.12, 0.07, 0.45));
  }
  S.koy(S.cizim({ svg: takvim, kutu: { x: 725, y: 995, w: 90, h: 90 }, ad: "takvim", enCok: 8, w: 4, tb: 37.0, sure: 0.5, olayEnCok: 1,
    nefes: false }));
  const nx = 940, ny = yKutu + kh / 2, nf = S.fr(38.7);
  S.olay(nf, "tik", 0.5);
  S.koy({ ciz: (ctx, f) => {
    const u = Math.min(1, Math.max(0, (f - nf) / 8)); if (u <= 0) return;
    ctx.save(); ctx.fillStyle = renkCoz(SARI); ctx.beginPath(); ctx.arc(nx, ny, 17 * u, 0, Math.PI * 2); ctx.fill(); ctx.restore();
  } });
  S.koy(S.nabiz(nx, ny, 17, 38.7));
  S.koy(S.not({ parca: [["now", SARI]], x: nx - 36, y: yKutu - 22, tb: 38.85, sure: 0.3, font: CV(64), ses: false }));
  S.koy(S.darbeler(ok([nx + 10, yOk], [xs + 20, yOk], 3), { w: 9, renk: SARI, uc0: 10, uc1: 14 }, 37.2, 0.2, 0.12, 0.5));
  const aW = olc(CV(64), "ago = ");
  S.koy(S.not({ parca: [["ago = ", SARI]], x: xs, y: yOk + 78, tb: 37.49, sure: 0.4, font: CV(64) }));
  S.koy(S.not({ parca: [["önce", KREM]], x: xs + aW, y: yOk + 78, tb: 38.01, sure: 0.4, font: CV(64) }));
  const zx = 520, zw = olc(CV(64), "zaman belli");
  S.koy(S.not({ parca: [["zaman belli", KREM]], x: zx, y: yOk + 78, tb: 38.77, sure: 0.6, font: CV(64) }));
  S.koy(S.darbeler([[[zx + zw + 22, yOk + 50], [zx + zw + 40, yOk + 70], [zx + zw + 76, yOk + 22]]],
    { w: 9, renk: SARI, uc0: 5, uc1: 8, duz: true }, 39.13, 0.25, 0.3, 0.5));

  // 40,08–42,24 -ed (40,56) kırmızı çizgiyle yok; go (41,84) sarı daire — alt bant, taban y 1345, Fredoka 110
  const R = 1345, ed = olc(FF(110), "-ed"), gx = 330, gw = olc(FF(110), "go");
  S.koy(S.metinPop({ parca: [["-ed", KREM]], x: 48, y: R, font: FF(110), tb: 40.56, sure: 0.3, ses: 0.5 }));
  S.koy(S.darbe([[30, R - 38], [48 + ed / 2, R - 42], [70 + ed, R - 34]], { w: 12, renk: KIRMIZI, alfa: 0.95, uc0: 8, uc1: 14, duz: true, tohum: 90 },
    40.9, 0.3, 0.6));
  S.koy(S.metinPop({ parca: [["go", KREM]], x: gx, y: R, font: FF(110), tb: 41.84, sure: 0.3, ses: 0.5 }));
  S.koy(S.darbe(elips(gx + gw / 2, R - 38, gw / 2 + 26, 74, -0.05, 31), { w: 9, renk: SARI, alfa: 0.85, uc0: 14, uc1: 30 }, 42.0, 0.35, 0.55));

  // 43,51–44,71 go -> kalem oku -> went (Fredoka 110, sarı)
  S.koy(S.darbeler(ok([gx + gw + 30, R - 42], [gx + gw + 130, R - 42], 5), { w: 9, renk: SARI, uc0: 10, uc1: 14 }, 43.51, 0.2, 0.12, 0.5));
  const wx = gx + gw + 150;
  S.koy(S.metinPop({ parca: [["went", SARI]], x: wx, y: R, font: FF(110), tb: 44.71, sure: 0.35, ses: 0.8, turu: "vurus" }));

  // 45,59–46,39 ezberle + küçük kitap (küçülmüş grubun sağında); go -> went kutuya alınır
  S.koy(S.cizim({ svg: kitap, kutu: { x: 870, y: 700, w: 140, h: 140 }, ad: "kitap", enCok: 8, w: 4, tb: 45.85, sure: 0.5, olayEnCok: 2, nefes: false }));
  S.koy(S.not({ parca: [["ezberle", KREM]], x: 836, y: 905, tb: 45.59, sure: 0.5, font: CV(64) }));
  S.koy(S.parilti(1010, 700, 46.3, 24));
  S.koy(S.darbeler(kutu(gx - 28, R - 118, wx + olc(FF(110), "went") - gx + 56, 150, 77), { w: 4, renk: IKINCIL, uc0: 10, uc1: 18 },
    45.65, 0.16, 0.1, 0.5));
}

surucu(kur, (f) => S.kare(f), KARE);

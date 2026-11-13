// SAHNE 04 — Örnek 2 (02-02-ydt-temel; düz canvas, 783 kare, t_bas 44,37; cümle 10–14). Kendini çizen
// kalem; zaman yalnız kare numarasından. Yerel kare = (t − 44,37) × 30.
// Kök: "He gets up at seven every morning and swims in the pool." (özne he → gets, swims).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, elips, ok, kutu, altCizgi, olc,
  yavasla } from "./sahne-ortak.js";

const KARE = 768, TBAS = 44.45, ICERIK = 756;
const KOKDIZ = "/projeler/02-02-ydt-temel/ortak/cizim";
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 2 / 3",
  cumle: [10, 11, 12, 13, 14] });
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`;
// El yazısı penceresi = anlatım t0/t1 (küresel sn)
const pen = (ad, t, n) => S.dizi(ad, t, n).map((w) => ({ t0: w.t0, t1: w.t1 }));

// ek_ayir: kök sabit, ek (s) yukarıdan kayıp yerine oturur, ardından sarı el kutusu çevreler.
function ekS(ch, x, y, font, tb, tohum) {
  const fb = S.fr(tb), n = 11, boy = 80, w = olc(font, ch);
  S.bas(fb); S.olay(fb, "tik", 0.5);
  const kay = { ciz: (ctx, f) => {
    const u = yavasla((f - fb) / n); if (u <= 0) return;
    const dy = 70 * (1 - u);
    if (u >= 0.2) window.__kalemKutu?.ekle("yazi", ch, x, y - boy * 0.9 - dy, w, boy * 1.1);
    ctx.save(); ctx.globalAlpha = u; ctx.font = font; ctx.textAlign = "left";
    ctx.textBaseline = "alphabetic"; ctx.fillStyle = renkCoz(SARI); ctx.fillText(ch, x, y - dy);
    ctx.restore();
  } };
  const kut = S.darbeler(kutu(x - 12, y - 66, w + 24, 92, tohum), { w: 4.4, renk: SARI, uc0: 8,
    uc1: 14 }, tb + 0.4, 0.1, 0.05, false);
  return [kay, ...kut];
}

async function kur() {
  await S.kur();
  const peep = await svgOku("open-peeps/standing-3.svg");           // erkek figür (K22: ses öğretmen, özne he)

  // 44,95 daire içinde 2 (ilk 12 kare boş: künye hazır, tuval boş)
  S.koy(S.daireSayi(2, 200, 190, 45.03));

  // 46,43–50,03 İngilizce kök (Fredoka 56, 2 satır, sözcük zamanlı, sarı alt çizgi kayar)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("He", 46.51, 12), x: 140, y: 300, maxGen: 1100,
    font: FF(56), satirH: 90, satirSay: [7, 5], bosluk: 4 }));
  const kel = cum.kel;                                              // 0 He … 6 morning | 7 and … 11 pool.
  S.koy(S.halka(kel[1], 46.83, 0.4, 11));                           // gets (46,71)
  S.koy(S.halka(kel[8], 48.95, 0.4, 13));                           // swims (48,83)
  {   // every morning (47,71–48,51): sarı alt çizgi
    const A = kel[5], B = kel[6];
    S.koy(S.darbe(altCizgi(A.x - 4, B.x + B.w + 4, A.y + 30, 33), { w: 7, renk: SARI, alfa: 0.88,
      uc0: 8, uc1: 14, tohum: 800 }, 47.8, 0.42, 0.55));
  }

  // 50,50–53,70 Türkçe çeviri (el yazısı 48 ikincil, y 500), her sözcük kendi penceresinde
  {
    const tr = S.dizi("O", 50.58, 8); let tx = 140;
    tr.forEach((k, i) => {
      const t1 = i < tr.length - 1 ? Math.max(k.t1, tr[i + 1].t0) : k.t1;
      const q = S.koy(S.elYazisi({ metin: k.sozcuk, x: tx, y: 500, boy: 48, renk: IKINCIL,
        sozcukler: [{ t0: k.t0, t1 }] }));
      tx += q.w + 0.3 * 48;
    });
  }

  // 50,50–52,10 figür (peeps standing, erkek) · 52,58–53,60 havuz çizgisi
  S.koy(S.cizim({ svg: peep, ad: "figur", kutu: { x: 1290, y: 250, w: 230, h: 520 },
    esik: 0.004, enCok: 60, w: 3.2, tb: 50.58, sure: 1.6, olayEnCok: 5 }));
  {
    const y0 = 650, x0 = 1570, x1 = 1830;
    S.koy(S.darbe([[x0, y0 - 20], [x0 + 4, y0 + 70], [x0 + 6, y0 + 140], [(x0 + x1) / 2, y0 + 146],
      [x1 - 4, y0 + 140], [x1, y0 + 70], [x1 + 2, y0 - 20]], { w: 5, renk: KREM, uc0: 10,
      uc1: 20, tohum: 71 }, 52.66, 0.55, 0.55));
    [[y0 + 30, 52.93, 72], [y0 + 82, 53.13, 73]].forEach(([y, tb, th]) => {
      const dalga = Array.from({ length: 30 }, (_, i) => { const u = i / 29;
        return [x0 + 20 + u * (x1 - x0 - 36), y + 7 * Math.sin(u * 6 * Math.PI)]; });
      S.koy(S.darbe(dalga, { duz: true, w: 4.4, renk: IKINCIL, alfa: 0.85, uc0: 10, uc1: 20,
        tohum: th }, tb, 0.4, 0.45));
    });
    S.koy({ ciz: (ctx, f) => {                                        // havuz çizgileri tek çizim kutusu (çakışma kapısı)
      if (f >= S.fr(52.66)) window.__kalemKutu?.ekle("cizim", "havuz", x0 - 6, y0 - 26,
        x1 - x0 + 14, 176);
    } });
  }

  // 55,78–57,14 every morning: sarı daire (isaret)
  {
    const A = kel[5], B = kel[6], x0 = A.x, x1 = B.x + B.w;
    S.koy(S.halka(A, 56.26, 0.45, 21, 6, B));            // altçizgi: öbeğin son sözcüğü (morning 56,18) göründükten sonra
  }
  // 58,99–59,87 satır: every morning → rutin
  {
    const m = S.koy(S.metinPop({ parca: [["every morning", KREM]], x: 140, y: 680, font: FF(64),
      tb: 59.07, sure: 0.3, ses: 0.5 }));
    const ax = 140 + m.w + 24;
    S.koy(S.darbeler(ok([ax, 660], [ax + 110, 660], 5), { w: 6, renk: SARI, uc0: 10, uc1: 14 },
      59.18, 0.16, 0.12, 0.5));
    S.koy(S.elYazisi({ metin: "rutin", x: ax + 135, y: 680, boy: 64, renk: SARI,
      sozcukler: pen("rutin.", 59.31, 1) }));
  }

  // 60,34–70,08 özne he → gets · swims (+s)
  S.koy(S.halka(kel[0], 61.71, 0.4, 15));                           // he. (61,63)
  {
    const Y = 860, F80 = FF(80);
    const he = S.koy(S.metinPop({ parca: [["he", KREM]], x: 140, y: Y, font: F80, tb: 61.71,
      sure: 0.3, ses: 0.5 }));
    const ax = 140 + he.w + 30;
    S.koy(S.darbeler(ok([ax, Y - 30], [ax + 120, Y - 30], 6), { w: 6.5, renk: SARI, uc0: 10,
      uc1: 14 }, 63.72, 0.18, 0.12, 0.5));                          // özneye (63,72)
    const gx = ax + 160;
    S.koy(S.metinPop({ parca: [["get", KREM]], x: gx, y: Y, font: F80, tb: 65.17, sure: 0.3,
      ses: 0.5 }));
    const gw = olc(F80, "get");
    S.koy(ekS("s", gx + gw, Y, F80, 65.45, 41));
    const nok = gx + gw + olc(F80, "s") + 46;
    S.koy(S.metinPop({ parca: [["·", IKINCIL]], x: nok, y: Y, font: F80, tb: 66.22, sure: 0.2,
      ses: false }));
    const sx = nok + olc(F80, "·") + 46;
    S.koy(S.metinPop({ parca: [["swim", KREM]], x: sx, y: Y, font: F80, tb: 66.54, sure: 0.3,
      ses: 0.5 }));
    const sw = olc(F80, "swim");
    S.koy(ekS("s", sx + sw, Y, F80, 66.77, 43));
    const ex = sx + sw + olc(F80, "s") + 60;
    // 69,36 «se» (pencere 0,16 sn): anlatımsız etiket (+s), hedef 0,45 sn → 69,81
    S.koy(S.elYazisi({ metin: "(+s)", x: ex, y: Y, boy: 72, renk: SARI, tb: 68.94, sure: 0.45 }));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

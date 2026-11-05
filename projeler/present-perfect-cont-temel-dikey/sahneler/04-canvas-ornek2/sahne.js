// SAHNE 04 (DİKEY) — Örnek 2 (PPC temel): düz canvas, 1080x1920, 462 kare, t_bas 32,28; cümle 4.
// Zaman yalnız kare numarasından; zamanlar sozcukler.json / altyazi.json ile aynı çerçevede (küresel sn).
// Yerleşim sıfırdan dikey: kart (tam genişlik) → TR → ORTA figür + gitar (sağ sütun: nota, güneş → now)
// → since satırı → alt formül.
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, ok, kutu, olc, geriTasma } from "./sahne-ortak.js";

const KARE = 462, TBAS = 32.28, ICERIK = 450;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, kayma: 0, bolum: "Example 2 / 3", cumle: 4 });
const KOKDIZ = "/projeler/present-perfect-cont-temel-dikey/ortak/cizim";
const svgOku = async (yol) => (await fetch(`${KOKDIZ}/${yol}`)).text();
const KREM = RT.murekkep, IKI = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`, CV = (b) => `700 ${b}px Caveat`;

async function kur() {
  await S.kur();
  const [kardes, gitar, nota, gunes] = await Promise.all([svgOku("open-peeps/sitting-2.svg"),
    svgOku("coco/guitar.svg"), svgOku("tabler/music.svg"), svgOku("coco/sun.svg")]);

  // kart: tam genişlik 984, Fredoka 72, 3 satır, sözcük zamanlı (ilk 12 kare boş; kutu 32,83'ten çizilir)
  const cum = S.koy(S.cumleYaz({ sozcukler: S.dizi("My", 34.12, 10), x: 88, y: 446, maxGen: 904, font: FF(72),
    satirH: 84 }));
  const sonTaban = Math.max(...cum.kel.map((k) => k.y)), kartAlt = sonTaban + 46;
  S.koy(S.darbeler(kutu(48, 360, 984, kartAlt - 360, 7), { w: 4, renk: IKI, uc0: 10, uc1: 18 }, 32.83, 0.2,
    0.12, 0.55));
  const kel = (ad) => cum.kel.find((k) => k.m === ad);

  // 37,73 Türkçe çeviri (Caveat 64, mürekkep)
  const yTR = kartAlt + 56;
  S.koy(S.not({ parca: [["Kardeşim sabahtan beri gitar çalıyor.", KREM]], x: 56, y: yTR, font: CV(64),
    tb: 37.73, sure: 0.7 }));

  // ORTA (yTR+20 → +420): kardeş (sitting-2) + gitar solda; sağ sütun: nota, güneş → now
  const fUst = yTR + 20, fYuk = 420;
  S.koy(S.cizim({ svg: kardes, kutu: { x: 48, y: fUst, w: 340, h: fYuk }, ad: "kardes", esik: 0.004, enCok: 60,
    w: 4.4, tb: 34.2, sure: 1.8, olayEnCok: 7 }));
  S.koy(S.cizim({ svg: gitar, ad: "gitar", kutu: { x: 400, y: fUst, w: 330, h: fYuk }, enCok: 24, w: 4,
    tb: 35.4, sure: 1.1, olayEnCok: 4 }));
  [[760, fUst + 4, 35.9], [850, fUst - 10, 36.5], [940, fUst + 6, 37.1]].forEach(([x, y, tb], i) => {
    const g = S.cizim({ svg: nota, kutu: { x, y, w: 90, h: 90 }, ad: "nota", enCok: 4, w: 4, tb, sure: 0.5,
      olayEnCok: 1, nefes: false });
    g.donusum = (f) => ({ cx: x, cy: y, tx: 0, ty: f < S.fr(tb + 0.5) ? 0 :
      6 * Math.sin((Math.min(f, ICERIK) - S.fr(tb + 0.5)) / 15 + i * 2), dondur: 0, olcek: 1 });
    S.koy(g); S.koy(S.parilti(x + 56, y + 36, tb + 0.45, 24));
  });
  // 35,96–37,48 güneş (sabah) → kalem oku → now (sağ sütun, aşağı doğru)
  {
    const sx = 740, sy = fUst + 120, nx = 800, ny = fUst + 380, nf = S.fr(37.1);
    S.koy(S.cizim({ svg: gunes, ad: "gunes", kutu: { x: sx, y: sy, w: 120, h: 120 }, enCok: 24, w: 4,
      tb: 35.96, sure: 0.6, olayEnCok: 3, nefes: false }));
    S.koy(S.not({ parca: [["sabah", KREM]], x: sx + 132, y: sy + 78, font: CV(64), tb: 36.28, sure: 0.4 }));
    S.koy(S.darbeler(ok([sx + 60, sy + 135], [nx, ny - 40], 3), { w: 7, renk: SARI, uc0: 10, uc1: 14 }, 36.6,
      0.2, 0.12, 0.5));
    S.olay(nf, "tik", 0.5);
    S.koy({ ciz: (ctx, f) => {
      const u = geriTasma((f - nf) / 10); if (u <= 0) return;
      ctx.save(); ctx.fillStyle = renkCoz(SARI); ctx.beginPath(); ctx.arc(nx, ny, 14 * u, 0, Math.PI * 2);
      ctx.fill(); ctx.restore();
    } });
    S.koy(S.nabiz(nx, ny, 14, 37.1));
    S.koy(S.not({ parca: [["now", SARI]], x: nx + 36, y: ny + 22, font: CV(64), tb: 37.2, sure: 0.3, ses: false }));
  }

  // 40,62 since (Fredoka 150 sarı) + 42,47 başlangıç noktası (Caveat 64) — ORTA ile formül arası satır
  const yS = 1262, wS = olc(FF(150), "since");
  S.koy(S.metinPop({ parca: [["since", SARI]], x: 56, y: yS, font: FF(150), tb: 40.62, sure: 0.4, olcek0: 0.6,
    ses: 0.8, turu: "vurus" }));
  S.koy(S.not({ parca: [["başlangıç noktası", KREM]], x: 56 + wS + 40, y: yS, font: CV(64), tb: 42.47,
    sure: 0.6 }));
  S.koy(S.parilti(56 + wS + 10, yS - 120, 40.95, 26));

  // 45,11 has: kartta sarı halka
  S.koy(S.halka(kel("has"), 45.11, 0.3, 11, 4));

  // alt formül (Fredoka ≤ 110): has been + V-ing — 45,11 / 46,07 / 46,30 / 46,63
  {
    let boy = 110; const P4 = ["has been", "+", "V", "-ing"], bs = 26;
    const topla = (b) => P4.reduce((t, m) => t + olc(FF(b), m), 0) + bs * 2 + 2;
    while (topla(boy) > 900 && boy > 80) boy -= 4;
    const yF = 1372, tb = [45.11, 46.07, 46.3, 46.63], renk = [KREM, IKI, KREM, SARI];
    let x = 540 - topla(boy) / 2;
    P4.forEach((m, i) => {
      S.koy(S.metinPop({ parca: [[m, renk[i]]], x, y: yF, font: FF(boy), tb: tb[i], sure: 0.3,
        ses: i === 0 || i === 3 ? 0.5 : false }));
      x += olc(FF(boy), m) + (i === 2 ? 2 : bs);
    });
    S.koy(S.parilti(870, yF - 86, 47.0, 24));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

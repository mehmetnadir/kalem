// SAHNE 05 — Örnek 3 (02-02-ydt-temel; düz canvas, 809 kare, t_bas 70,08; cümle 15–19). Yerel kare =
// (t − 70,08) × 30. Zaman yalnız kare numarasından; sözcük zamanları sozcukler.json (küresel sn).
// Kök: "The Moon completes its orbit around the Earth in 27 days." (genel gerçek; it → completes).
import { surucu } from "/ortak/surucu.js";
import { Sahne, RT, renkCoz, elips, ok, kutu, olc,
  yavasla } from "./sahne-ortak.js";
import { kalemCizgi, darbeCiz } from "/projeler/02-02-ydt-temel/ortak/kalem-canvas.js";

const KARE = 812, TBAS = 69.66, ICERIK = 800;
const S = new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, bolum: "Example 3 / 3",
  cumle: [15, 16, 17, 18, 19] });
const KREM = RT.murekkep, IKINCIL = RT.ikincil, SARI = RT.vurgu;
const FF = (b) => `700 ${b}px Fredoka`;

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

  // 70,70 daire içinde 3 (ilk 12 kare boş)
  S.koy(S.daireSayi(3, 200, 190, 70.28));

  // 72,22–76,30 İngilizce kök (Fredoka 56, 2 satır). Anlatımda "twenty seven", ekranda "27": tek sözcük.
  const ham = S.dizi("The", 71.8, 12), iki = ham.findIndex((s) => s.sozcuk === "twenty");
  const sz = [...ham.slice(0, iki), { ...ham[iki], sozcuk: "27", t1: ham[iki + 1].t1 },
    ...ham.slice(iki + 2)];                                          // The Moon … in 27 days.
  const cum = S.koy(S.cumleYaz({ sozcukler: sz, x: 140, y: 300, maxGen: 1100, font: FF(56),
    satirH: 90, satirSay: [5, 6], bosluk: 4 }));
  const kel = cum.kel;                                              // 0 The … 4 orbit | 5 around … 9 27, 10 days.
  S.koy(S.halka(kel[2], 72.33, 0.4, 31));                           // completes (72,70)
  {
    const a = kel[9], b = kel[10];
    S.koy(S.halka(a, 75.16, 0.45, 33, 6, b));   // 27 days (twenty 74,86)
  }

  // 76,77–80,69 Ay, Dünya, yörünge: Ay (76,77) → Dünya (77,49) → yörünge (77,89) → tur (78,53–80,69)
  const EX = 1570, EY = 400, RX = 220, RY = 105;
  S.koy(S.darbe(elips(EX, EY, 62, 62, 0.1, 3), { w: 5, renk: KREM, uc0: 14, uc1: 24 }, 77.07,
    0.5, 0.6));
  S.koy(S.darbeler([
    [[EX - 40, EY - 8], [EX - 26, EY - 32], [EX - 6, EY - 24], [EX - 12, EY - 2], [EX - 34, EY + 8]],
    [[EX + 14, EY + 18], [EX + 34, EY + 4], [EX + 44, EY + 26], [EX + 26, EY + 42],
      [EX + 8, EY + 36]]], { w: 4, renk: IKINCIL, uc0: 8, uc1: 12 }, 77.33, 0.3, 0.2, 0.4));
  S.koy(S.darbe(elips(EX, EY, RX, RY, 0, 9), { w: 4.2, renk: IKINCIL, alfa: 0.85, uc0: 20,
    uc1: 40 }, 77.47, 0.9, 0.5));
  {
    const ayC = kalemCizgi(elips(0, 0, 24, 23, 0.1, 7), { w: 4.6, renk: "@murekkep", uc0: 10,
      uc1: 14, tohum: 7 });
    const krt = kalemCizgi([[-9, -4], [-3, -9], [4, -5]], { w: 3.4, renk: "@ikincil", uc0: 4,
      uc1: 6, tohum: 8 });
    const fb = S.fr(76.35), fm = S.fr(78.11), PER = 65;           // bir tur ≈ 2,16 sn (turunu → tamamlar)
    S.bas(fb); S.olay(fb, "cizgi", 0.5);
    S.koy({ ciz: (ctx, f) => {
      const t = yavasla((f - fb) / 14); if (t <= 0) return;
      const th = Math.PI + (f < fm ? 0 : 2 * Math.PI * (Math.min(f, ICERIK) - fm) / PER);
      const x = EX + RX * 1.03 * Math.cos(th), y = EY + RY * 1.03 * Math.sin(th);
      if (f >= S.fr(77.07)) window.__kalemKutu?.ekle("cizim", "dunya-ay-yorunge", EX - RX * 1.06 - 28,
        EY - RY * 1.06 - 28, 2 * (RX * 1.06 + 28), 2 * (RY * 1.06 + 28));   // Dünya + yörünge + Ay
      else window.__kalemKutu?.ekle("cizim", "ay", x - 27, y - 27, 54, 54);
      ctx.save(); ctx.translate(x, y); darbeCiz(ctx, ayC, t); darbeCiz(ctx, krt, t);
      ctx.restore();
    } });
    S.olay(fm, "tik", 0.5);
  }

  // 76,77–80,69 Türkçe çeviri (el yazısı 48 ikincil, y 500). Anlatımda "yirmi yedi", ekranda "27".
  {
    const ham2 = S.dizi("Ay,", 76.35, 8), yi = ham2.findIndex((s) => s.sozcuk === "yirmi");
    const tr = [...ham2.slice(0, yi), { ...ham2[yi], sozcuk: "27", t1: ham2[yi + 1].t1 },
      ...ham2.slice(yi + 2)];
    let tx = 140;
    tr.forEach((k, i) => {
      const t1 = i < tr.length - 1 ? Math.max(k.t1, tr[i + 1].t0) : k.t1;
      const q = S.koy(S.elYazisi({ metin: k.sozcuk, x: tx, y: 500, boy: 48, renk: IKINCIL,
        sozcukler: [{ t0: k.t0, t1 }] }));
      tx += q.w + 0.3 * 48;
    });
  }

  // 81,56–88,84 genel gerçek: etiket, iki yönlü ok (dün de, yarın da), tik (geniş zaman alır)
  {
    const g1 = S.koy(S.elYazisi({ metin: "genel", x: 140, y: 640, boy: 64, renk: SARI,
      sozcukler: [{ t0: 81.14, t1: 81.54 }] }));
    const g2 = S.koy(S.elYazisi({ metin: "gerçek", x: g1.x + g1.w + 0.3 * 64, y: 640, boy: 64,
      renk: SARI, sozcukler: [{ t0: 81.54, t1: 82.22 }] }));
    const bit = g2.x + g2.w;
    const mid = (140 + bit) / 2;                                    // dün de, yarın da: iki yöne ok
    S.koy(S.darbeler(ok([mid, 676], [140, 676], 8), { w: 6, renk: SARI, uc0: 10, uc1: 14 },
      82.68, 0.3, 0.2, 0.5));                                        // böyleydi (83,12)
    S.koy(S.darbeler(ok([mid, 676], [bit, 676], 9), { w: 6, renk: SARI, uc0: 10, uc1: 14 },
      82.68, 0.3, 0.2, false));
    S.koy(S.darbe([[bit + 40, 636], [bit + 58, 656], [bit + 94, 610]], { w: 8, renk: SARI,
      alfa: 0.9, uc0: 4, uc1: 10, tohum: 63 }, 87.94, 0.3, 0.55));  // alır (88,36)
  }

  // 89,31–96,73 özne it → complete|s (+s)
  {
    const a = kel[0], b = kel[1];
    S.koy(S.halka(a, 89.78, 0.4, 35, 6, b));   // the Moon (the 90,04)
    const Y = 830, F80 = FF(80);
    const it = S.koy(S.metinPop({ parca: [["it", KREM]], x: 140, y: Y, font: F80, tb: 91.56,
      sure: 0.3, ses: 0.5 }));
    const ax = 140 + it.w + 30;
    S.koy(S.darbeler(ok([ax, Y - 30], [ax + 120, Y - 30], 6), { w: 6.5, renk: SARI, uc0: 10,
      uc1: 14 }, 92.16, 0.18, 0.12, 0.5));
    const cx = ax + 160;
    S.koy(S.metinPop({ parca: [["complete", KREM]], x: cx, y: Y, font: F80, tb: 93.34,
      sure: 0.35, ses: 0.5 }));
    const cw = olc(F80, "complete");
    S.koy(ekS("s", cx + cw, Y, F80, 94.41, 47));
    const ex = cx + cw + olc(F80, "s") + 60;
    // 95,93 «se» (pencere 0,16 sn): anlatımsız etiket (+s), hedef 0,45 sn → 96,38
    S.koy(S.elYazisi({ metin: "(+s)", x: ex, y: Y, boy: 72, renk: SARI, tb: 95.59, sure: 0.45 }));
  }
}

surucu(kur, (f) => S.kare(f), KARE);

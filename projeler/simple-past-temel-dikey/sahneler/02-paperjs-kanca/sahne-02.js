// Sahne 02 — Kanca, DİKEY 1080x1920 (409 kare, t_bas 3,00; cümle 2 = 3,39–15,69).
// Bantlar: içerik 352–1392 · altyazı 1400–1536 (kalem-paper.js çizer) · platform boş.
// Yerleşim: solda figür (440 px sabit), sağda ev (9,49'te solar) →
// saat + ajanda kartı (360–1032);
// alt bantta İngilizce cümle + düzenli fiil → -ed (DUZ3 16.11). Figür hiç küçülmez.
import {
  sahneKur, RT
} from "/projeler/simple-past-temel-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";

// Kart süresi (12.11, g-29): paket zaman.json son t_son'dan; sabit 6 dakika iddiası yanlıştı.
// Göreli yol: sahneler/<sahne>/ → paket kökü (yayında da aynı). Okunamazsa etiket boş kalır.
const SURE_METNI = await fetch(new URL("../../zaman.json", location.href))
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error("HTTP " + r.status))))
  .then((z) => {
    const t = z.sahneler[z.sahneler.length - 1].t_son;
    return t < 60 ? `${Math.round(t)} sec` : `${Math.round(t / 30) / 2} min`;
  })
  .catch((e) => { console.warn("zaman.json süre okunamadı:", e); return ""; });

export const KARE = 409, T_BAS = 3.0;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook" });
  const {
    fr, ciz, daire, ok, yazi, elYazisi, cumle, altCizgi, tik, parilti, olay, not, bitis, kutu,
    genislik
  } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil, MUR = RT.murekkep;
  const GB = 12; // geçiş karesi: çizimler bundan sonra
  // El yazısı (Caveat 700 tegaki, dalga 5b / K26): not ve etiketler kalemle yazılır
  const CS = S.sozcukler(2); // cümle 2 sözcükleri (f / f1 yerel kare)
  const pen = (ilk, adet) => {
    const i = CS.findIndex((w) => w.s === ilk);
    return CS.slice(i, i + adet).map((w) => ({ f0: w.f, f1: w.f1 }));
  };

  // --- cümle 1 (Caveat 80, iki satır, taban y 450 / 540): sahne 01'den devam;
  // 0–0,4 sn'de hazır belirir
  const c1 = cumle(
    ["Dün", "akşam", "amcamlara", "gittim."].map((s, i) => ({
      s, f: i * 3, satir: i < 3 ? 0 : 1
    })),
    { x: 56, y: 450, boyut: 80, aile: "Caveat", agirlik: 700, aralik: 90 }
  );
  not("cümle 1 başı (Dün)", c1[0].bas); not("gittim.", c1[3].bas);

  // --- orta bant sol sütun: ayakta figür 440 px (baştan sona sabit, hiç küçülmez)
  const figOge = S.oge({
    kay: { f0: GB, f1: fr(7.2), dx: 40 },
    nefes: { bas: fr(7.3), cx: 190, cy: 1190 }
  });
  await S.svgCiz("open-peeps/standing-2.svg", { kutu: [60, 760, 260, 440], bas: GB, sure: 42,
    azami: 60, yuz: 3, w: 4.4, oge: figOge, sesAralik: 5 });
  not("figür çizimi başı", GB); not("figür yürüme biter", fr(7.2));
  ciz([[48, 1200], [330, 1195]], {
    w: 3.6, renk: IKI, alfa: 0.75, bas: 36, sure: 24, uc0: 10, uc1: 20
  });

  // --- orta bant sağ sütun: ev + hilal (9,49'te solar, yerini saat + ajandaya bırakır)
  const evGrup = S.oge({
    alfa: (f) => (f < fr(9.49) ? 1 : Math.max(0, 1 - (f - fr(9.49)) / 15))
  });
  await S.svgCiz("tabler/home.svg", { kutu: [430, 800, 380, 380], bas: GB, sure: 26, azami: 25,
    w: 4, sesAralik: 2, oge: evGrup });
  not("ev çizimi başı", GB);
  ciz([[330, 1195], [700, 1200], [1030, 1195]], { w: 3.6, renk: IKI, alfa: 0.75, bas: 36,
    sure: 30, uc0: 10, uc1: 30, oge: evGrup });
  {   // hilal: dış yay + iç yay tek darbe (el elipsi)
    const C = [930, 850], R = 66, d2r = Math.PI / 180, pts = [];
    for (let a = 65; a <= 295; a += 6) {
      pts.push([C[0] + R * Math.cos(a * d2r), C[1] + R * Math.sin(a * d2r)]);
    }
    const Ci = [C[0] + 0.5 * R, C[1]], Ri = R * 0.91;
    for (let a = 265; a >= 95; a -= 6) {
      pts.push([Ci[0] + Ri * Math.cos(a * d2r), Ci[1] + Ri * Math.sin(a * d2r)]);
    }
    const h = ciz(pts, {
      w: 5, alfa: 0.92, bas: fr(4.2), sure: 30, uc0: 12, uc1: 20, amp: 0.7, oge: evGrup
    });
    not("hilal çizimi başı", h.bas);
    parilti(C[0] + 46, C[1] - 60, { bas: bitis(h) + 2, r: 28, periyot: 60, adet: 2, oge: evGrup });
  }

  // --- 3,39–5,87: gittim sarı daire; -di sarı kutu (4,83);
  // ok → biten iş; ok → takvim + dün (taban y 650)
  {
    const g = c1[3], d = daire((g.x0 + g.x1) / 2 + 3, g.y - 28, g.w / 2 + 10, 46,
      { bas: fr(3.39), sure: 24, egim: -0.04, w: 10 });
    olay(bitis(d), "tik", 0.5); not("gittim daire", d.bas);
    // 4,83–5,15 «-di» (pencere: -di 4,83–5,07; sonraki sözcüğün başına dek uzatıldı: 5,15)
    const y1 = 650, a = elYazisi("-di", {
      x: 76, y: y1, boyut: 72, renk: MUR, sozcukler: [{ f0: fr(4.83), f1: fr(5.15) }]
    });
    kutu(a.x0 - 18, y1 - 60, a.w + 36, 84, { bas: fr(4.83) + 6, sure: 14, w: 8, renk: SARI });
    not("-di sarı kutu", fr(4.83));
    const o1 = ok([a.x1 + 30, y1 - 20], [a.x1 + 112, y1 - 20],
      { bas: fr(4.83) + 20, sure: 10, w: 9, uzun: 22, bukum: 0.08 });
    // anlatımsız etiket `biten iş` (okun ardından): hedef 12 kare (0,4 sn)
    const b = elYazisi("biten iş", {
      x: a.x1 + 130, y: y1, boyut: 64, renk: MUR, bas: bitis(o1) + 2, sure: 12
    });
    not("biten iş", b.bas);
    const o2 = ok([b.x1 + 26, y1 - 16], [b.x1 + 104, y1 - 10],
      { bas: fr(5.45), sure: 10, w: 9, uzun: 22, bukum: 0.1 });
    await S.svgCiz("tabler/calendar.svg", { kutu: [b.x1 + 122, y1 - 84, 100, 100], bas: bitis(o2),
      sure: 20, azami: 25, w: 4, sesAralik: 3 });
    // anlatımsız etiket `dün` (takvimden sonra): hedef 10 kare (0,33 sn)
    elYazisi("dün", {
      x: b.x1 + 244, y: y1, boyut: 64, renk: SARI, bas: bitis(o2) + 16, sure: 10
    });
    not("takvim + dün", bitis(o2));
  }

  // --- 6,02–9,54: I visited my uncle last night.
  // (Fredoka 64, iki satır, taban 1310 / 1376); -ed daire; düzenli fiil → -ed
  {
    const tl = [6.02, 6.30, 6.62, 6.78, 7.10, 7.44];
    const kel = ["I", "visited", "my", "uncle", "last", "night."];
    const e = cumle(kel.map((s, i) => ({ s, f: fr(tl[i]), satir: i < 4 ? 0 : 1 })),
      { x: 56, y: 1310, boyut: 64, aile: "Fredoka", agirlik: 700, aralik: 66 });
    altCizgi(e, { tut: 40, w: 9 }); not("İngilizce cümle başı", e[0].bas);
    const v = e[1], font = "700 64px Fredoka";
    const wv = genislik("visit", font), we = genislik("ed", font);
    const d = daire(v.x0 + wv + we / 2, v.y - 22, we / 2 + 8, 36, {
      bas: fr(7.94) - 6, sure: 18, a0: -2.0, w: 9
    });
    olay(bitis(d), "tik", 0.5); not("-ed daire", d.bas);
    // DUZ3 (16.11): `düzenli fiil` sözle (düzenli 6,90 · fiile 7,38); ok ve `-ed` -ed sözünde (7,94)
    const y = 1376, a = elYazisi("düzenli fiil", {
      x: e[5].x1 + 44, y, boyut: 56, renk: MUR, sozcukler: pen("düzenli", 2)
    });
    const ar = ok([a.x1 + 18, y - 18], [a.x1 + 88, y - 18],
      { bas: fr(7.94), sure: 14, w: 9, uzun: 22, bukum: 0.05 });
    elYazisi("-ed", {
      x: a.x1 + 104, y, boyut: 64, renk: SARI, bas: bitis(ar) + 2, sure: 12
    });
    not("ok düzenli fiil → -ed", ar.bas);
  }

  // --- 9,69–15,69: sağ sütun: saat + süre etiketi + ajanda kartı (3 madde);
  // figür sol sütunda tam boy kalır
  {
    await S.svgCiz("tabler/clock.svg", { kutu: [380, 750, 110, 110], bas: fr(9.97), sure: 20,
      azami: 25, w: 4.4, sesAralik: 3 });
    // 9,89 anlatımsız etiket SURE_METNI (derste 9,89–10,33): hedef 14 kare (0,47 sn)
    elYazisi(SURE_METNI, { x: 510, y: 835, boyut: 84, renk: SARI, bas: fr(9.97) + 14, sure: 14 });
    not("saat + süre etiketi", fr(9.97));
    parilti(680, 750, { bas: fr(11.0), r: 26, periyot: 170, adet: 3 });
    kutu(360, 880, 672, 330, { bas: fr(10.89), sure: 30, w: 4 }); not("kart çizimi", fr(10.89));
    const m = [
      ["form", 11.37, 955], ["time expressions", 12.49, 1045], ["irregular verbs", 14.17, 1135]
    ];
    for (const [s, t, y] of m) {
      yazi(s, {
        x: 440, y, boyut: 64, aile: "Fredoka", agirlik: 700, renk: MUR, bas: fr(t), sure: 8
      });
      tik(395, y - 22, { bas: fr(t) + 4 }); not("madde " + s, fr(t));
    }
  }
  return S;
}

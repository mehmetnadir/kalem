// Sahne 03 (DİKEY) — Örnek 1: Paper.js, 1080x1920, 453 kare, t_bas 15,44; cümle 3.
// Yerel kare = round((t − 15,44) × 30);
// zamanlar sozcukler.json ve altyazi.json ile aynı çerçevede.
// Yerleşim sıfırdan dikey tasarım: kart (tam genişlik) → TR çeviri →
// ORTA figür + kamera → alt formül.
import { sahneKur, RT, renkCoz }
  from "/projeler/present-continuous-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";
import { yaziNoktalari }
  from "/projeler/present-continuous-dikey/ortak/kalem-canvas.js";

export const KARE = 453, T_BAS = 15.44;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Example 1 / 3", etkin: 1, kayma: 0 });
  const { fr, ciz, daire, yazi, elYazisi, cumle, altCizgi, parilti, olay, not, bitis, dinamik,
    genislik } = S;
  const SARI = RT.vurgu, IKI = RT.ikincil;
  const GB = 12; // ilk 12 kare geçiş altında: yalnız künye
  // El yazısı (Caveat 700 tegaki, dalga 5 / K26): not ve etiketler kalemle yazılır. Ortalı yazıda
  // genişlik tegaki verisinden ölçülür; sözcük pencereleri anlatımdan (<6 kare → sonrakine uzar).
  const [eyM, eyG] = await Promise.all([fetch("/ortak/tegaki/caveat-tr/metrik.json"),
    fetch("/ortak/tegaki/caveat-tr/glyphData-700.json")]);
  const EY = { M: await eyM.json(), G: await eyG.json() };
  const eyGen = (str, boyut) => yaziNoktalari(str, EY.G, { upm: EY.M.unitsPerEm,
    asc: EY.M.ascender, boy: boyut, x: 0, taban: 0 }).gen;
  const CS = S.sozcukler(3);
  const pen = (ilk, adet) => { const i = CS.findIndex((w) => w.s === ilk);
    return CS.slice(i, i + adet).map((w, k) => ({ f0: w.f,
      f1: w.f1 - w.f < 6 && CS[i + k + 1] ? CS[i + k + 1].f : w.f1 })); };

  // --- kart: tam genişlik (984), Fredoka 72, sözcük zamanlı; satır kırılımı ölçülür
  const sz = S.sozcukler(3).slice(2, 11);                          // I … now.
  const FK = "700 72px Fredoka", MAKS = 984 - 80, SB = genislik(" ", FK);
  const satirlar = [[]]; let gen = 0;
  for (const k of sz) {
    const w = genislik(k.s, FK);
    if (satirlar[satirlar.length - 1].length && gen + SB + w > MAKS) { satirlar.push([]); gen = 0; }
    gen += (satirlar[satirlar.length - 1].length ? SB : 0) + w;
    satirlar[satirlar.length - 1].push(k);
  }
  const SH = 88, B1 = 372 + 40 + 58; // kart üstü 372, iç boşluk 40, ilk taban
  const sonTaban = B1 + (satirlar.length - 1) * SH, kartAlt = sonTaban + 24 + 36;
  const kb = S.kutu(48, 372, 984, kartAlt - 372, { bas: GB, sure: 36, w: 4, renk: IKI });
  not("kart kutusu çizimi", GB); void kb;
  const kel = satirlar.flatMap((a, si) => a.map((k) => ({ s: k.s, f: k.f, satir: si })));
  const cz = cumle(kel, { x: 88, y: B1, boyut: 72, aile: "Fredoka", agirlik: 700, aralik: SH });
  altCizgi(cz, { tut: 40, w: 9 }); not("cümle başı (I)", cz[0].bas); not("now", cz[8].bas);

  // --- TR çeviri (Caveat 64, mürekkep) 19,30 + in progress bandı
  const yTR = kartAlt + 66;
  // 19,30–20,74 «Şu anda oturuyorum.» (pencere: şu 19,30–19,58 · anda 19,58–19,78 ·
  // oturuyorum 19,78–20,74; kısa pencereler sonraki sözcüğün başına uzatıldı)
  const tr = elYazisi("Şu anda oturuyorum.", { x: 64, y: yTR, boyut: 64, renk: RT.murekkep,
    sozcukler: pen("Şu", 3) });
  not("Türkçe çeviri", fr(19.3));

  // --- ORTA: oturan figür + kamera + sehpa (bant: TR altı → formül üstü)
  const fUst = yTR + 40, fAlt = 1150, fYuk = fAlt - fUst;
  const figOge = S.oge({ nefes: { bas: fr(18.7), cx: 280, cy: fAlt } });
  await S.svgCiz("open-peeps/sitting-4.svg", { kutu: [70, fUst, 450, fYuk], bas: fr(16.5),
    sure: fr(18.6) - fr(16.5), azami: 60, yuz: 3, w: 4.4, oge: figOge, sesAralik: 5, ayna: false });
  not("figür çizimi başı", fr(16.5));
  const kY = fUst + 10, kBoy = 300, kX = 640, kcx = kX + kBoy / 2;
  await S.svgCiz("tabler/camera.svg", {
    kutu: [kX, kY, kBoy, kBoy], bas: fr(17.8), sure: 18, azami: 25, w: 4,
    sesAralik: 1 });
  not("kamera çizimi başı", fr(17.8));
  const ay = kY + kBoy - 24;
  [[[kcx, ay], [kcx - 120, fAlt]],
   [[kcx, ay], [kcx + 2, fAlt + 4]],
   [[kcx, ay], [kcx + 124, fAlt]]].forEach((p, i) => {
    ciz([p[0], [(p[0][0] + p[1][0]) / 2 + 2, (p[0][1] + p[1][1]) / 2], p[1]],
      { w: 4.4, bas: fr(17.8) + 18 + i * 4, sure: 8, uc0: 6, uc1: 12, amp: 0.6 }); });
  not("sehpa (3 çizgi)", fr(17.8) + 18);
  parilti(kX + kBoy - 10, kY + 20, { bas: fr(18.7), r: 28, periyot: 170, adet: 4 });

  // --- 18,65 now sarı daire + NOW etiketi (kartın son sözcüğü)
  {
    const g = cz[8];
    const d = daire((g.x0 + g.x1) / 2, g.y - 26, g.w / 2 + 2, 40, { bas: fr(18.65), sure: 16 });
    olay(bitis(d), "tik", 0.5); not("now daire", d.bas);
    // daire sonrası anlatımsız etiket `NOW`: hedef 14 kare (0,47 sn) → ≈ 19,72
    elYazisi("NOW", { x: g.x1 + 50, y: g.y, boyut: 72, renk: SARI, bas: bitis(d) + 2, sure: 14 });
  }

  // --- 20,78: in progress (dalgalı sarı bant, TR çevirinin sağında) + nabız noktası
  {
    const x0 = 600, x1 = 1020, yb = yTR - 4;
    const dalga = Array.from({ length: 40 }, (_, i) => { const u = i / 39, x = x0 + u * (x1 - x0);
      return [x,
        yb + 20 + 11 * Math.sin(u * 7.5 * Math.PI) * (0.55 + 0.45 * Math.sin(u * Math.PI))];
    });
    const w = ciz(dalga, {
      w: 9, renk: SARI, alfa: 0.85, bas: fr(20.78), sure: 24, duz: true, uc0: 12, uc1: 24, amp: 0.5
    });
    not("in progress bandı", w.bas);
    // 21,38 anlatımsız etiket `in progress`: hedef 16 kare (0,53 sn) → 21,91; ortalı (x = orta −
    // gen/2)
    elYazisi("in progress", { x: (x0 + x1) / 2 - eyGen("in progress", 64) / 2, y: yb - 6,
      boyut: 64, renk: SARI, bas: bitis(w) - 6, sure: 16 });
    const f0 = fr(21.5), nx = x0 + 30, ny = yb + 20;
    dinamik((f, g) => {
      if (f < f0) return;
      const t = f - f0, s = 1 + 0.16 * Math.sin(2 * Math.PI * t / 36);
      const u = (t % 45) / 45, a = Math.min(1, t / 5);
      g.addChild(new P.Path.Circle({
        center: [nx, ny], radius: 12 * s * a, fillColor: renkCoz(SARI), insert: false
      }));
      g.addChild(new P.Path.Circle({ center: [nx, ny], radius: 14 + 28 * (1 - Math.pow(1 - u, 3)),
        strokeColor: renkCoz(SARI), strokeWidth: 4, opacity: 0.75 * (1 - u) * a, insert: false }));
    });
    olay(f0, "tik", 0.5); not("now noktası (nabız)", f0);
  }

  // --- 24,73 am ve 25,85 sitting: kartta sarı daire (sözcük başlarında)
  {
    const a = cz[1], s = cz[2];
    const da = daire((a.x0 + a.x1) / 2, a.y - 24, a.w / 2 + 2, 40,
      { bas: fr(24.73), sure: 16, a0: -1.8 });
    olay(bitis(da), "tik", 0.5); not("am daire", da.bas);
    const ds = daire((s.x0 + s.x1) / 2, s.y - 24, s.w / 2 + 2, 40,
      { bas: fr(25.85), sure: 18, a0: -2.8 });
    olay(bitis(ds), "tik", 0.5); not("sitting daire", ds.bas);
  }

  // --- alt formül: satır A `am + sitting` (24,73–25,85),
  // satır B `be + V-ing` (27,04–29,00) → ok
  {
    let boy = 110; const F = (b) => `700 ${b}px Fredoka`;
    const GAP = [26, 26, 2];                                       // sitt-ing / V-ing bitişik
    const topla = (p, b) => p.reduce((t, [m]) => t + genislik(m, F(b)), 0)
      + GAP.reduce((a, g) => a + g, 0);
    const A = [["am"], ["+"], ["sitt"], ["-ing"]], B = [["be"], ["+"], ["V"], ["-ing"]];
    while (topla(A, boy) > 900 && boy > 88) boy -= 4;
    const yA = 1268, yB = 1378, hepsi = (p, y, t, renkler, sesIlk) => {
      let x = 540 - topla(p, boy) / 2; const out = [];
      p.forEach(([m], i) => {
        const o = yazi(m, {
          x, y, boyut: boy, aile: "Fredoka", agirlik: 700, renk: renkler[i],
          bas: fr(t[i]), sure: 10, olcek: true, ses: i === 0 && sesIlk
        });
        out.push(o);
        x = o.x1 + (GAP[i] == null ? 0 : GAP[i]);
      });
      return out;
    };
    const a = hepsi(A, yA, [24.73, 25.3, 25.85, 26.2], [RT.murekkep, IKI, RT.murekkep, SARI], true);
    not("am + sitting", fr(24.73));
    const b = hepsi(B, yB, [27.04, 28.12, 28.4, 28.96],
      [RT.murekkep, IKI, RT.murekkep, SARI], true);
    not("be + V-ing", fr(27.04));
    const ar = S.ok([130, yA - 50], [130, yB - 10], {
      bas: fr(26.5), sure: 16, w: 8, uzun: 26, bukum: 0.14
    });
    not("ok A → B", ar.bas);
    parilti(b[3].x1 + 40, yB - boy * 0.8, { bas: fr(29.1), r: 24 });
    void a;
  }
  return S;
}

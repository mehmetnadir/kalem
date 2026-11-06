// Zaman hattı (metro hattı) modülü — tense pedagojisi için. Kalem modeli ve kamera kullanmaz.
// Gramer: hat = zaman · durak = an · aktarma = tense geçişi · kesik = gelecek ·
//   band = süre (for) · ok = başlangıç (since).
// Kullanım: const hat = zamanHatti(S, { x, y, w, duraklar: [{ ad, t, tur, vurgu }], bas });
//   aralik(hat, d1, d2, { etiket, bas }) · baslangic(hat, d, { etiket, bas }) ·
//   tren(hat, d1, d2, { bas, sure }) · hat.durakEkle({ ad, t, tur, bas }): hat yeniden çizilmez.
// Her çizim kare numarasından türer (Math.random / Date yok); z sırası = çağrı sırası
//   (band hattın altına girer).
import { RT, renkCoz } from "/projeler/deneme-metro/ortak/kunye.js";

const kis = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const yumus = (x) => { x = kis(x); return x * x * (3 - 2 * x); };
const R = 20, KALIN = 10;                                  // durak yarıçapı, hat kalınlığı (px)

// kalem ilerlemesinin tersi (kalem-paper.js ilerle: 0,35 t + 0,65 yumus(t))
const gIl = (t) => 0.35 * t + 0.65 * yumus(t);
const ilerleTers = (u, sure) => {
  for (let f = 0; f <= sure; f++) if (gIl(f / sure) >= u) return f;
  return sure;
};

export function zamanHatti(S, { x, y, w, duraklar, bas = 0, sure = 70, t0, t1 }) {
  const { P, ciz, elYazisi, oge, dinamik, olay, not, parilti, genislik } = S;
  const ts = duraklar.map((d) => d.t);
  const a0 = t0 == null ? Math.min(...ts) - 1 : t0, a1 = t1 == null ? Math.max(...ts) + 1 : t1;
  const xt = (t) => x + (t - a0) / (a1 - a0) * w;
  const hatOg = oge({});
  const sim = duraklar.find((d) => d.tur === "simdi"), xSim = sim ? xt(sim.t) : x + w;
  // hat: şimdiye dek düz, sonrası kesik (gelecek)
  const lenD = xSim - x, KES = 30, ARA = 22, bos = xSim + R + 10, xs = x + w;
  const nKes = sim ? Math.max(0, Math.floor((xs - bos) / (KES + ARA)) + 1) : 0;
  const sureD = sim ? Math.round(sure * lenD / (lenD + (xs - bos))) : sure, sureK = sure - sureD;
  ciz([[x, y], [x + lenD, y]], { duz: true, w: KALIN, renk: RT.murekkep, alfa: 0.95, amp: 0.25,
    uc0: 4, uc1: 4, aralik: 3, bas, sure: sureD, oge: hatOg });
  const kesikBas = [];
  for (let i = 0; i < nKes; i++) {
    const xa = bos + i * (KES + ARA), xb = Math.min(xa + KES, xs);
    const b = bas + sureD + Math.round(i * sureK / nKes);
    kesikBas.push({ xa, b });
    ciz([[xa, y], [xb, y]], { duz: true, w: KALIN, renk: RT.murekkep, alfa: 0.8, amp: 0.2,
      uc0: 3, uc1: 3, aralik: 3, bas: b, sure: Math.max(3, Math.round(sureK / nKes) - 1),
      oge: hatOg, ses: false });
  }
  const bit = bas + sure;
  const hat = { S, x, y, w, xt, og: hatOg, bit, duraklar: [] };

  // durak: halka (sayfa renginde dolgu + mürekkep kontur); şimdi = vurgu dolgu + parıltı;
  // gelecek = kesik halka. Hat başı durağa varınca halka çizilir.
  const durakKaresi = (d) => {
    const dx = xt(d.t);
    if (dx <= xSim) return bas + ilerleTers((dx - x) / lenD, sureD);
    const k = kesikBas.filter((q) => q.xa <= dx + KES).pop();
    return k ? k.b : bit;
  };
  function durakEkle(d) {
    const dx = xt(d.t), b = d.bas == null ? durakKaresi(d) : d.bas, r = R + (d.vurgu ? 3 : 0);
    const o = { ...d, x: dx, bas: b };
    hat.duraklar.push(o);
    olay(b, "tik", 0.5); not("durak " + d.ad, b);
    dinamik((f, g) => {
      const u = kis((f - b) / 12); if (u <= 0) return;
      const dolgu = d.tur === "simdi" ? RT.vurgu : RT.zemin;
      g.addChild(new P.Path.Circle({ center: [dx, y], radius: r * (0.6 + 0.4 * yumus(u * 1.6)),
        fillColor: renkCoz(dolgu), opacity: kis(u * 2.2), insert: false }));
      const n = 30, son = Math.max(1, Math.round(n * yumus(u))), pts = [];
      for (let i = 0; i <= son; i++) {
        const a = -2 + i / n * 2 * Math.PI;
        pts.push(new P.Point(dx + r * Math.cos(a), y + r * Math.sin(a)));
      }
      const halka = new P.Path({ segments: pts, closed: son >= n, strokeCap: "round",
        strokeColor: renkCoz(d.vurgu ? RT.vurgu : RT.murekkep), strokeWidth: d.vurgu ? 7 : 5.5,
        opacity: d.tur === "gelecek" ? 0.7 : 0.95, insert: false });
      if (d.tur === "gelecek") halka.dashArray = [9, 7];
      g.addChild(halka);
    });
    if (d.tur === "simdi") parilti(dx, y, { bas: b + 10, r: 34, periyot: 70, adet: 2 });
    const boyut = 44, gw = genislik(d.ad, `700 ${boyut}px Caveat`);
    elYazisi(d.ad, { x: dx - gw / 2, y: y + 78, boyut, renk: RT.murekkep, bas: b + 4, sure: 12,
      ses: false });
    return o;
  }
  hat.durakEkle = durakEkle;
  hat.durak = (ad) => hat.duraklar.find((d) => d.ad === ad);
  duraklar.forEach(durakEkle);
  return hat;
}

const durakBul = (hat, d) => (typeof d === "string" ? hat.durak(d) : d);
const solma = (sil) => (f) => (sil ? 1 - kis((f - sil.bas) / sil.sure) : 1);

// sarı etiket: vurgu markeri (şeffaf) + el yazısı; cx = orta, taban = yazı tabanı
function etiketCiz(S, str, cx, taban, o) {
  const boyut = o.boyut || 44, gw = S.genislik(str, `700 ${boyut}px Caveat`);
  S.ciz([[cx - gw / 2 - 18, taban - 14], [cx + gw / 2 + 18, taban - 14]], { duz: true, w: 46,
    renk: RT.vurgu, alfa: 0.3, amp: 0.3, uc0: 3, uc1: 3, bas: o.bas, sure: 12, oge: o.og,
    ses: false });
  return S.elYazisi(str, { x: cx - gw / 2, y: taban, boyut, renk: RT.murekkep, bas: o.bas + 10,
    sure: o.sure || 22, oge: o.og, ses: false });
}

// iki durak arası kalın vurgu bandı (for = süre); hattın ALTINA girer, etiket üstte
export function aralik(hat, d1, d2, { etiket, bas, sure = 24, sil } = {}) {
  const S = hat.S, a = durakBul(hat, d1), b = durakBul(hat, d2);
  const og = S.oge({ alfa: solma(sil) });
  og.g.insertBelow(hat.og.g);
  S.ciz([[a.x, hat.y], [b.x, hat.y]], { duz: true, w: 34, renk: RT.vurgu, alfa: 0.5, amp: 0.3,
    uc0: 2, uc1: 2, aralik: 3, bas, sure, oge: og });
  S.not("band " + a.ad + "→" + b.ad, bas);
  if (etiket) {
    etiketCiz(S, etiket, (a.x + b.x) / 2, hat.y - 62,
      { bas: bas + sure - 6, og: S.oge({ alfa: solma(sil) }) });
  }
  return { bas, bit: bas + sure + 30 };
}

// durağa inen ok + etiket (since = başlangıç)
export function baslangic(hat, d, { etiket, bas, sure = 16, sil } = {}) {
  const S = hat.S, a = durakBul(hat, d), og = S.oge({ alfa: solma(sil) });
  if (etiket) etiketCiz(S, etiket, a.x, hat.y - 218, { bas, og });
  S.ok([a.x, hat.y - 200], [a.x, hat.y - 40], { bas: bas + 16, sure, w: 5, uzun: 20,
    bukum: 0.02, oge: og });
  S.not("başlangıç oku " + a.ad, bas + 16);
  return { bas, bit: bas + 16 + sure + 10 };
}

// cümle vagonu: d1 → d2 kayar; varınca kısa durur, sonra solar (kal: true ise kalır)
export function tren(hat, d1, d2, { bas, sure = 54, kal = false } = {}) {
  const S = hat.S, a = durakBul(hat, d1), b = durakBul(hat, d2), bek = 8, sol = 12;
  const { P } = S, mur = renkCoz(RT.murekkep);
  S.olay(bas, "cizgi", 0.4); S.not("vagon " + a.ad + "→" + b.ad, bas);
  S.dinamik((f, g) => {
    const u = (f - bas) / sure; if (u < 0) return;
    const al = kal ? 1 : 1 - kis((f - bas - sure - bek) / sol); if (al <= 0) return;
    const cx = a.x + (b.x - a.x) * yumus(u), cy = hat.y;
    g.opacity = al * kis((f - bas) / 6);
    g.addChild(new P.Path.Rectangle({ point: [cx - 29, cy - 19], size: [58, 38], radius: 9,
      fillColor: renkCoz(RT.vurgu), strokeColor: mur, strokeWidth: 4.5, insert: false }));
    g.addChild(new P.Path.Line({ from: [cx - 17, cy - 4], to: [cx + 17, cy - 4],
      strokeColor: mur, strokeWidth: 3.5, strokeCap: "round", insert: false }));
    for (const dx of [-14, 14]) {
      g.addChild(new P.Path.Circle({ center: [cx + dx, cy + 19], radius: 5, fillColor: mur,
        insert: false }));
    }
  });
  return { bas, bit: bas + sure + bek + sol };
}

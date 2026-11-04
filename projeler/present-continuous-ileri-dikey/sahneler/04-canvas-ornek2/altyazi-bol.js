// Altyazı bölücü (dikey): ortak kunye.js `altyaziCiz` en çok 2 satır çizer; üçüncü satır ikinciye eklenir ve güvenli alanın
// dışına taşar. Uzun parça (3+ satır) cümle sınırından bölünür; her dilim ilk sözcüğünün zamanında görünür.
const FONT = "500 44px Lexend", GEN = 984;

function satirSayisi(ctx, metin) {
  ctx.save(); ctx.font = FONT; let s = "", n = 1;
  for (const w of metin.split(" ")) {
    const d = s ? s + " " + w : w;
    if (ctx.measureText(d).width > GEN && s) { n++; s = w; } else s = d;
  }
  ctx.restore(); return n;
}

// liste: K.altyazi · sozc: sozcukler.json (hepsi) · t: küresel sn → çizilecek metin ("" ise yok)
export function altyaziSec(ctx, liste, sozc, t) {
  const p = (liste || []).find((a) => t >= a.t0 - 0.05 && t < a.t1 + 0.35);
  if (!p) return "";
  if (satirSayisi(ctx, p.metin) <= 2) return p.metin;
  const kel = (sozc || []).filter((s) => s.cumle === p.cumle && s.t0 >= p.t0 - 0.02 && s.t0 <= p.t1 + 0.02);
  const tum = p.metin.split(/(?<=[.!?])\s+/), dilim = [];
  let cur = [], ilk = 0, say = 0;
  for (const c of tum) {
    if (cur.length && satirSayisi(ctx, [...cur, c].join(" ")) > 2) { dilim.push({ metin: cur.join(" "), k: ilk }); cur = []; ilk = say; }
    cur.push(c); say += c.split(" ").length;
  }
  if (cur.length) dilim.push({ metin: cur.join(" "), k: ilk });
  let secili = dilim[0];
  for (const d of dilim) { const b = kel[d.k] ? kel[d.k].t0 : p.t0; if (t >= b - 0.05) secili = d; }
  return secili.metin;
}

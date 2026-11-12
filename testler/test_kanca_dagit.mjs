// testler/test_kanca_dagit.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";
import {
  kancaKalemCanvas,
  kancaKunye,
  kancaKalemPaper,
  kancaSahneOrtak,
  dosyayiKancala,
} from "../araclar/kanca-dagit.mjs";

const KOK = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");

test("kancaKalemCanvas: çapa bulunur, kanca eklenir, eşgüçlüdür (ikinci koşu VAR), çapa yoksa CAPA_YOK", () => {
  const mini = `import { renkCoz } from "./kunye.js";\n// ---------- küçük yardımcılar ----------\nexport const kis = 1;\n`;
  const res1 = kancaKalemCanvas(mini, "kalem-canvas.js");
  assert.equal(res1.durum, "DEGISTI");
  assert.ok(res1.icerik.includes("__kalemKutu"));
  assert.ok(res1.icerik.includes("// ---------- küçük yardımcılar ----------"));

  // İkinci koşu: eşgüçlülük
  const res2 = kancaKalemCanvas(res1.icerik, "kalem-canvas.js");
  assert.equal(res2.durum, "VAR");

  // Çapa yok
  const hatali = `export const kis = 1;\n`;
  const res3 = kancaKalemCanvas(hatali, "kalem-canvas.js");
  assert.equal(res3.durum, "CAPA_YOK");

  // ekle() kutuyu çizim anındaki ctx dönüşümünden geçirir (12.11: S.grup 0,42 küçültmesi dikeyde yanlış hata verdi)
  const bas = res1.icerik.indexOf("if (typeof window");
  const son = res1.icerik.indexOf("// ---------- küçük yardımcılar");
  const pencere = {};
  new Function("window", res1.icerik.slice(bas, son))(pencere);
  const K = pencere.__kalemKutu;
  K.ekle("cizim", "duz", 100, 200, 80, 40);
  K.ctx = { getTransform: () => ({ a: 1, b: 0, c: 0, d: 1, e: 0, f: 0, isIdentity: true }) };
  K.ekle("cizim", "birim", 100, 200, 80, 40);
  // (540, 830) çevresinde 0,5 ölçek: x' = 0,5x + 270, y' = 0,5y + 415
  K.ctx = { getTransform: () => ({ a: 0.5, b: 0, c: 0, d: 0.5, e: 270, f: 415, isIdentity: false }) };
  K.ekle("cizim", "kucuk", 100, 200, 80, 40);
  assert.deepEqual(K.kare.map((k) => [k.ad, k.x, k.y, k.w, k.h]), [
    ["duz", 100, 200, 80, 40], ["birim", 100, 200, 80, 40], ["kucuk", 320, 515, 40, 20]]);
});

test("kancaKunye: çapa bulunur, kanca eklenir, eşgüçlüdür, çapa yoksa CAPA_YOK", () => {
  const mini = `export const RENK = { ...TEMALAR.koyu };
export function kunyeCiz(ctx, { bolum, etkin = 0, logo, alfa = 1 }) {
  const dw = ctx.measureText(k.ders).width;
  ctx.fillStyle = R.ikincil; ctx.font = \`500 \${k.seviyeYazi}px Lexend\`; ctx.fillText(\`· \${k.seviye}\`, k.kenar + dw + 14, k.ustTaban);
  ctx.textAlign = "right"; ctx.fillStyle = R.vurgu; ctx.font = \`700 \${k.bolumYazi}px Lexend\`;
  ctx.fillText(bolum || "", W - k.kenar, k.ustTaban);
  if (logo) { const h = k.logoYuk, w = h * 1920 / 476.3; ctx.drawImage(logo, k.kenar, H - 44 - h, w, h); }
  ctx.restore();
}
`;
  const res1 = kancaKunye(mini, "kunye.js");
  assert.equal(res1.durum, "DEGISTI");
  assert.ok(res1.icerik.includes("__kalemKutu"));
  assert.ok(res1.icerik.includes("kunye:sol-ust"));

  // Eşgüçlülük
  const res2 = kancaKunye(res1.icerik, "kunye.js");
  assert.equal(res2.durum, "VAR");

  // Çapa yok
  const hatali = `export const x = 1;\n`;
  const res3 = kancaKunye(hatali, "kunye.js");
  assert.equal(res3.durum, "CAPA_YOK");
});

test("kancaKalemPaper: çapa bulunur, kanca eklenir, eşgüçlüdür, çapa yoksa CAPA_YOK", () => {
  const mini = `  function ciz(pts, o = {}) {
    const c = kalemGeo(pts, o); c.bas = o.bas || 0; c.sure = Math.max(2, o.sure || 20); c.og = o.oge || kok; c.yolP = null; c.tam = false;
    CIZGILER.push(c);
  }
  function daire(cx, cy, rx, ry, o = {}) {
    return ciz(pts, { w: 7.5, renk: RT.vurgu, alfa: 0.85, amp: 0.4, uc0: 14, uc1: 40, ...o });
  }
  function ok(a, b, o = {}) {
    const g = ciz(pts, { w, renk, alfa, bas: o.bas, sure, uc0: 10, uc1: 14, amp: 0.7, oge: o.oge });
    const uc = () => {
      return ciz([rot(0.5), tip, rot(-0.5)], { w: w * 0.9, renk, alfa, bas: o.bas + sure - 2, sure: 8, uc0: 6, uc1: 6, amp: 0.4, duz: true, oge: o.oge, ses }); };
    return g;
  }
  function kutu(x, y, w, h, o = {}) {
    ciz([q[0], [(q[0][0] + q[1][0]) / 2 + 1.5 * (i % 2 ? 1 : -1), (q[0][1] + q[1][1]) / 2 + 1.2], q[1]], { w: o.w || 3.6, renk: o.renk || RT.ikincil, alfa: 0.9,
      bas: cur, sure: sr, uc0: 10, uc1: 12, oge: o.oge, ses: i === 0 ? true : false }); cur += sr; });
  }
  function tik(cx, cy, o = {}) {
    return ciz([[cx - 14, cy + 1], [cx - 4, cy + 12], [cx + 17, cy - 15]], { w: 7, renk: RT.vurgu, alfa: 0.9, bas: o.bas, sure: 9, uc0: 5, uc1: 8, amp: 0.3, ses: "tik", oge: o.oge });
  }
  function yazi(str, o = {}) {
    if (o.oge) o.oge.g.addChild(g);
  }
  function elYazisi(str, o) {
    const darbeler = Y.darbeler.map((d) => {
      const c = d.nokta ? null : ciz(d.pts, { duz: true, w: Math.max(1.4, d.gen), amp: 0.25, uc0: 2.5,
        uc1: 3, aralik: 1.6, renk, alfa, bas: fb, sure: fs, oge: o.oge, ses: false });
    });
  }
  // ---------- kare ----------
  async function kare(f) {
    c.yolP = cokgen(c, t); c.og.g.addChild(c.yolP); c.tam = t >= 1;
  }
`;
  const res1 = kancaKalemPaper(mini, "kalem-paper.js");
  assert.equal(res1.durum, "DEGISTI");
  assert.ok(res1.icerik.includes("paperTopla"));
  assert.ok(res1.icerik.includes("kalemTur"));
  // El yazısı darbeleri yazı türüyle etiketlenir (yoksa kapı yazıyı kendi harfleriyle çakışık bulur)
  assert.ok(res1.icerik.includes('ses: false, tur: "yazi", ad: str });'));

  // El yazısı çapası yoksa dosya değişmez
  const yazisiz = mini.replace("oge: o.oge, ses: false });", "oge: o.oge });");
  const res4 = kancaKalemPaper(yazisiz, "kalem-paper.js");
  assert.equal(res4.durum, "CAPA_YOK");
  assert.equal(res4.capa, "elYazisi darbe ciz");

  // Eşgüçlülük
  const res2 = kancaKalemPaper(res1.icerik, "kalem-paper.js");
  assert.equal(res2.durum, "VAR");

  // Çapa yok
  const hatali = `function ciz() {}\n`;
  const res3 = kancaKalemPaper(hatali, "kalem-paper.js");
  assert.equal(res3.durum, "CAPA_YOK");
});

test("kancaSahneOrtak: çapa bulunur, kanca eklenir, eşgüçlüdür, çapa yoksa CAPA_YOK", async () => {
  const mini = `export class Sahne {
  cumle(a) {
    return { x: a.x, w: Y.gen, Y, sure: Y.sure, ciz: (ctx, f) => {
      const t = mutlak ? this.zm(f) : (f - fb) / 30; if (t <= (mutlak ? a.sozcukler[0].t0 : 0)) return;
      yaziCiz(ctx, Y, t, 1);
    } };
  }
  fr(t) { return t * 30; }
  gorsel(a) {
    const g = { donusum: a.donusum || null };
    g.ciz = (ctx, f) => {
      ctx.save();
      const d = g.donusum ? g.donusum(f) : null;
      ctx.restore();
    };
    return g;
  }
  metinPop(a) {
    return { x: x0, w: tw, y: a.y, fb, ciz: (ctx, f) => {
      const u = yavasla((f - fb) / n); if (u <= 0) return;
      ctx.save(); ctx.globalAlpha = u * (a.alfa == null ? 1 : a.alfa); ctx.font = a.font; ctx.textAlign = "left";
    } };
  }
  metinDaktilo(a) {
    return { x: a.x, w: tw, ciz: (ctx, f) => {
      const u = kis((f - fb) / n); if (u <= 0) return;
      ctx.save(); ctx.beginPath(); ctx.rect(a.x - 8, a.y - boy * 1.1, (tw + 16) * u, boy * 1.6); ctx.clip();
    } };
  }
  halka(k, tb, sure = 0.35, tohum = 1, pay = 6) {
    const el = elips(k.x + k.w / 2, k.y - 22, k.w / 2 + pay, 52, -0.04 + 0.03 * hash(tohum, 3, 3), tohum);
    return this.darbe(el, { w: 6, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 }, tb, sure, 0.55);
  }
  kart(a) {
    const o = [];
    this.darbeler(kutu(a.x, a.y, a.w, a.h, 90 + (a.tohum || 0)), { w: 3.6, renk: RT.ikincil, uc0: 10, uc1: 18 }, a.tb, a.kutuSure || 0.14,
      a.kutuAralik || 0.1, 0.55).forEach((e) => o.push(e));
    a.satirlar.forEach((s, i) => o.push(this.metinPop({ ...s, ses: i === 0 ? 0.5 : false })));
    return o;
  }
  async kare(f, hepsi) {
    const ctx = this.ctx;
  }
}
`;
  const res1 = kancaSahneOrtak(mini, "sahne-ortak.js");
  assert.equal(res1.durum, "DEGISTI");
  assert.ok(res1.icerik.includes("__kalemKutu"));
  assert.ok(res1.icerik.includes("window.__kalemKutu.ctx = this.ctx;"));

  // Çizim kutusu donusum'den geçer (12.11: kalkan uçağın kutusu pistte kalıyordu)
  const gecici = fs.mkdtempSync(path.join(os.tmpdir(), "kanca-"));
  const modYol = path.join(gecici, "sahne-ortak.mjs");
  fs.writeFileSync(modYol, res1.icerik);
  const kayit = [];
  const eskiWindow = globalThis.window;
  globalThis.window = { __kalemKutu: { ekle: (tur, ad, x, y, w, h) => kayit.push({ tur, ad, x, y, w, h }) } };
  try {
    const { Sahne } = await import(modYol);
    const S = new Sahne();
    const ctx = { save() {}, restore() {} };
    const kutu = { x: 100, y: 200, w: 80, h: 40 };
    S.gorsel({ tb: 0, ad: "duz", kutu }).ciz(ctx, 10);
    S.gorsel({ tb: 0, ad: "tasinan", kutu, donusum: () => ({ cx: 0, cy: 0, tx: 300, ty: -150, dondur: 0, olcek: 1 }) })
      .ciz(ctx, 10);
    S.gorsel({ tb: 0, ad: "donen", kutu, donusum: () => ({ cx: 140, cy: 220, tx: 0, ty: 0, dondur: Math.PI / 2, olcek: 1 }) })
      .ciz(ctx, 10);
    const yuvarla = (k) => [k.x, k.y, k.w, k.h].map((v) => Math.round(v));
    assert.deepEqual(yuvarla(kayit[0]), [100, 200, 80, 40]);
    assert.deepEqual(yuvarla(kayit[1]), [400, 50, 80, 40]);
    assert.deepEqual(yuvarla(kayit[2]), [120, 180, 40, 80]);
  } finally {
    globalThis.window = eskiWindow;
  }

  // Eşgüçlülük
  const res2 = kancaSahneOrtak(res1.icerik, "sahne-ortak.js");
  assert.equal(res2.durum, "VAR");

  // Çapa yok
  const hatali = `export class Sahne {}\n`;
  const res3 = kancaSahneOrtak(hatali, "sahne-ortak.js");
  assert.equal(res3.durum, "CAPA_YOK");
});

test("dosyayiKancala: çapası olmayan dosya değişmez ve CAPA_YOK döner", () => {
  const dosyaTurleri = ["kalem-canvas.js", "kunye.js", "kalem-paper.js", "sahne-ortak.js"];
  for (const ad of dosyaTurleri) {
    const res = dosyayiKancala(ad, "hatali icerik");
    assert.equal(res.durum, "CAPA_YOK");
    assert.ok(res.capa);
  }
});

test("CLI: present-continuous --kuru çıktısı tüm dosyalarda VAR olmalı ve kod 0", () => {
  const betik = path.join(KOK, "araclar", "kanca-dagit.mjs");
  const cikti = execFileSync("node", [betik, "present-continuous", "--kuru"], {
    cwd: KOK,
    encoding: "utf8",
  });
  const satirlar = cikti.trim().split("\n");
  assert.ok(satirlar.length >= 4);
  for (const s of satirlar) {
    assert.ok(s.startsWith("VAR "), `Beklenen VAR: ${s}`);
  }
});

test("CLI: present-perfect-temel --kuru çıktısı tüm dosyalarda VAR olmalı ve kod 0", () => {
  const betik = path.join(KOK, "araclar", "kanca-dagit.mjs");
  const cikti = execFileSync("node", [betik, "present-perfect-temel", "--kuru"], {
    cwd: KOK,
    encoding: "utf8",
  });
  const satirlar = cikti.trim().split("\n");
  assert.ok(satirlar.length >= 4);
  for (const s of satirlar) {
    assert.ok(s.startsWith("VAR "), `Beklenen VAR: ${s}`);
  }
});

test("kancaKunye (dikey/s1 varyantı): çapa bulunur, kanca eklenir, eşgüçlüdür", () => {
  const miniDikey = `export const RENK = { ...TEMALAR.koyu };
export function kunyeCiz(ctx, { bolum, logo, alfa = 1 }) {
  const k = KUNYE, R = RENK; ctx.save(); ctx.globalAlpha = alfa; ctx.textBaseline = "alphabetic"; ctx.textAlign = "left";
  if (logo) { const h = k.logoYuk, w = h * 1920 / 476.3; ctx.drawImage(logo, k.kenar, k.logoY, w, h); }
  ctx.fillStyle = R.murekkep; ctx.font = \`700 \${k.dersYazi}px Fredoka\`; ctx.fillText(k.ders, k.kenar, k.dersTaban);
  if (bolum) {
    ctx.font = \`700 \${k.cipYazi}px Lexend\`; const cw = ctx.measureText(bolum).width + 64, cx = W - k.kenar - cw;
  }
  ctx.restore();
}
`;
  const res1 = kancaKunye(miniDikey, "kunye.js");
  assert.equal(res1.durum, "DEGISTI");
  assert.ok(res1.icerik.includes("__kalemKutu"));
  assert.ok(res1.icerik.includes("kunye:logo"));
  assert.ok(res1.icerik.includes("kunye:ders"));
  assert.ok(res1.icerik.includes("kunye:sag-ust"));

  // Eşgüçlülük
  const res2 = kancaKunye(res1.icerik, "kunye.js");
  assert.equal(res2.durum, "VAR");
});

test("kancaSahneOrtak (dikey varyant 2: elYazisi/cizim/not/metinPop/kart): çapa bulunur, kanca eklenir, eşgüçlüdür", () => {
  const miniDikeySahne = `export class Sahne {
  elYazisi(a) {
    return { x: a.x, w: Y.gen, Y, sure: Y.sure, ciz: (ctx, f) => {
      const t = mutlak ? this.zm(f) : (f - fb) / 30;
      if (t <= (mutlak ? a.sozcukler[0].t0 : 0)) return;
      yaziCiz(ctx, Y, t, 1);
    } };
  }
  cizim(a) {
    g.ciz = (ctx, f) => {
      ctx.save();
      const d = g.donusum ? g.donusum(f) : null;
    };
  }
  metinPop(a) {
    return { x: x0, w: tw, y: a.y, fb, ciz: (ctx, f) => {
      const u = yavasla((f - fb) / n); if (u <= 0) return;
      ctx.save();
      ctx.globalAlpha = u * (a.alfa == null ? 1 : a.alfa);
      ctx.font = a.font;
      ctx.textAlign = "left";
    } };
  }
  not(a) {
    return { x: a.x, w: tw, ciz: (ctx, f) => {
      const u = kis((f - fb) / n); if (u <= 0) return;
      ctx.save();
      ctx.beginPath();
      ctx.rect(a.x - 8, a.y - boy * 1.1, (tw + 16) * u, boy * 1.6);
      ctx.clip();
    } };
  }
  halka(k, tb, sure = 0.35, tohum = 1, pay = 6) {
    const el = elips(
      k.x + k.w / 2, k.y - 22, k.w / 2 + pay, 52,
      -0.04 + 0.03 * hash(tohum, 3, 3), tohum
    );
    return this.darbe(el, { w: 6, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 }, tb, sure, 0.55);
  }
  kart(a) {
    const o = [];
    this.darbeler(
      kutu(a.x, a.y, a.w, a.h, 90 + (a.tohum || 0)),
      { w: 3.6, renk: RT.ikincil, uc0: 10, uc1: 18 }, a.tb, a.kutuSure || 0.14,
      a.kutuAralik || 0.1, 0.55).forEach((e) => o.push(e));
    a.satirlar.forEach((s, i) => o.push(this.metinPop({ ...s, ses: i === 0 ? 0.5 : false })));
    return o;
  }
  async kare(f, hepsi) {
    const ctx = this.ctx;
  }
}
`;
  const res1 = kancaSahneOrtak(miniDikeySahne, "sahne-ortak.js");
  assert.equal(res1.durum, "DEGISTI");
  assert.ok(res1.icerik.includes("__kalemKutu"));
  assert.ok(res1.icerik.includes("halka:"));
  assert.ok(res1.icerik.includes("kart"));

  // Eşgüçlülük
  const res2 = kancaSahneOrtak(res1.icerik, "sahne-ortak.js");
  assert.equal(res2.durum, "VAR");
});

test("kancaSahneOrtak (halka varyantları: renk parametreli / k.boy boyutlu): çapa bulunur, kanca eklenir, eşgüçlüdür", () => {
  const miniHalkaRenk = `export class Sahne {
  cumle(a) {
    return { x: a.x, w: Y.gen, Y, sure: Y.sure, ciz: (ctx, f) => {
      const t = mutlak ? this.zm(f) : (f - fb) / 30; if (t <= (mutlak ? a.sozcukler[0].t0 : 0)) return;
      yaziCiz(ctx, Y, t, 1);
    } };
  }
  gorsel(a) {
    g.ciz = (ctx, f) => {
      ctx.save();
      const d = g.donusum ? g.donusum(f) : null;
    };
  }
  metinPop(a) {
    return { x: x0, w: tw, y: a.y, fb, ciz: (ctx, f) => {
      const u = yavasla((f - fb) / n); if (u <= 0) return;
      ctx.save(); ctx.globalAlpha = u * (a.alfa == null ? 1 : a.alfa); ctx.font = a.font; ctx.textAlign = "left";
    } };
  }
  metinDaktilo(a) {
    return { x: a.x, w: tw, ciz: (ctx, f) => {
      const u = kis((f - fb) / n); if (u <= 0) return;
      ctx.save(); ctx.beginPath(); ctx.rect(a.x - 8, a.y - boy * 1.1, (tw + 16) * u, boy * 1.6); ctx.clip();
    } };
  }
  halka(k, tb, sure = 0.35, tohum = 1, pay = 6, renk = RT.vurgu) {
    const el = elips(k.x + k.w / 2, k.y - 22, k.w / 2 + pay, 52, -0.04 + 0.03 * hash(tohum, 3, 3), tohum);
    return this.darbe(el, { w: 6, renk, alfa: 0.85, uc0: 14, uc1: 30 }, tb, sure, 0.55);
  }
  kart(a) {
    const o = [];
    this.darbeler(kutu(a.x, a.y, a.w, a.h, 90 + (a.tohum || 0)), { w: 3.6, renk: RT.ikincil, uc0: 10, uc1: 18 }, a.tb, a.kutuSure || 0.14,
      a.kutuAralik || 0.1, 0.55).forEach((e) => o.push(e));
    a.satirlar.forEach((s, i) => o.push(this.metinPop({ ...s, ses: i === 0 ? 0.5 : false })));
    return o;
  }
  async kare(f, hepsi) {
    const ctx = this.ctx;
  }
}
`;
  const res1 = kancaSahneOrtak(miniHalkaRenk, "sahne-ortak.js");
  assert.equal(res1.durum, "DEGISTI");
  assert.ok(res1.icerik.includes("__kalemKutu"));
  assert.ok(res1.icerik.includes("halka:"));

  const res2 = kancaSahneOrtak(res1.icerik, "sahne-ortak.js");
  assert.equal(res2.durum, "VAR");
});

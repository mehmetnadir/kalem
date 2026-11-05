// El yazısı darbeleri (kalem-canvas.js yaziDarbeleri / yaziCiz / yaziUcu) — node --test araclar/test/
// Veri: projeler/present-continuous/ortak/tegaki/caveat-tr (Caveat 700 Türkçe tegaki glif verisi).
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const KOK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const ORTAK = path.join(KOK, "projeler", "present-continuous", "ortak");
const { yaziDarbeleri, yaziCiz, yaziUcu } = await import(path.join(ORTAK, "kalem-canvas.js"));
const G = JSON.parse(fs.readFileSync(path.join(ORTAK, "tegaki", "caveat-tr", "glyphData-700.json")));
const M = JSON.parse(fs.readFileSync(path.join(ORTAK, "tegaki", "caveat-tr", "metrik.json")));
const SEC = { upm: M.unitsPerEm, asc: M.ascender, boy: 48, x: 10, taban: 100, renk: "@ikincil" };
const sonZaman = (Y) => Math.max(...Y.darbeler.map((d) => d.bas + d.sure));

test("doğal süre glif sürelerinin toplamıdır; her darbe bir kalem çizgisi ya da nokta taşır", () => {
  const Y = yaziDarbeleri("dönem", G, SEC);
  const beklenen = [..."dönem"].reduce((a, ch) => a + G[ch].t, 0);
  assert.ok(Math.abs(Y.sure - beklenen) < 1e-9);
  assert.ok(Y.darbeler.length >= 5);
  for (const d of Y.darbeler) assert.ok(d.c || d.nib.length > 0);
  assert.ok(Y.gen > 48 && Y.gen < 48 * 5);
});

test("i, ö ve nokta nib damgasıyla gelir (gıdıyorum hatası)", () => {
  for (const ch of ["i", "ö", "ü", "."]) {
    const Y = yaziDarbeleri(ch, G, SEC);
    assert.ok(Y.darbeler.some((d) => d.nib.length > 0), ch + " için nib yok");
  }
});

test("taban çizgisi: harfler taban ± em içinde kalır", () => {
  const Y = yaziDarbeleri("Kardeşim", G, SEC), k = 48 / M.unitsPerEm;
  for (const d of Y.darbeler) {
    for (const p of d.c ? d.c.p : []) {
      assert.ok(p[1] >= 100 - M.ascender * k - 2 && p[1] <= 100 - M.descender * k + 2, "y " + p[1]);
    }
  }
  assert.equal(Y.taban, 100);
});

test("hedefSure: bütün yazı hedef saniyeye sığar", () => {
  const Y = yaziDarbeleri("piyano dersi", G, { ...SEC, hedefSure: 2 });
  assert.equal(Y.sure, 2);
  assert.ok(sonZaman(Y) <= 2 + 1e-9);
  assert.ok(sonZaman(Y) > 1.9);
});

test("sözcük penceresi: her sözcük kendi [t0, t1] aralığında yazılır (hız kuralı)", () => {
  const P = [{ t0: 10, t1: 10.5 }, { t0: 11, t1: 11.8 }, { t0: 12.2, t1: 12.9 }];
  const Y = yaziDarbeleri("bu dönem piyano", G, { ...SEC, sozcukler: P });
  for (const d of Y.darbeler) {
    const p = P[d.soz];
    assert.ok(d.bas >= p.t0 - 1e-9 && d.bas + d.sure <= p.t1 + 1e-6, `sözcük ${d.soz}: ${d.bas}+${d.sure}`);
  }
  assert.ok(Math.abs(Y.sure - 12.9) < 1e-6);
});

test("eksik glif hata verir (sessiz yedek yok)", () => {
  assert.throws(() => yaziDarbeleri("a → b", G, SEC), /glif yok: →/);
});

test("yaziCiz yazarken dolgu yapar, yaziUcu yazan darbenin ucunu verir", () => {
  const Y = yaziDarbeleri("bu", G, { ...SEC, hedefSure: 1 });
  let dolgu = 0;
  const ctx = { save() {}, restore() {}, beginPath() {}, moveTo() {}, lineTo() {}, closePath() {},
    ellipse() {}, fill() { dolgu++; }, globalAlpha: 1, fillStyle: "" };
  yaziCiz(ctx, Y, 0);
  assert.equal(dolgu, 0);
  yaziCiz(ctx, Y, 0.5);
  assert.ok(dolgu > 0);
  const uc = yaziUcu(Y, Y.darbeler[0].bas + Y.darbeler[0].sure / 2);
  assert.ok(Array.isArray(uc) && uc.length === 2);
  assert.equal(yaziUcu(Y, 5), null);
});

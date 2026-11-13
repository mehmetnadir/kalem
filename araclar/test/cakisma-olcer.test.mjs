// cakisma-olcer: muaf listesi ve altcizgi/halka aileleri (canvas kuralları değişmeden kalır).
// node --test araclar/test/cakisma-olcer.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { carpisma } from "../cakisma-olcer.mjs";

const K = (tur, ad, x, y, w, h, ek = {}) => ({ tur, ad, x, y, w, h, ...ek });

test("canvas kuralı: yazı × çizim hata, isaret sayılmaz, kart içi yazı sayılmaz", () => {
  assert.equal(carpisma([K("yazi", "a", 0, 0, 100, 40), K("cizim", "b", 50, 10, 100, 20)]).length, 1);
  assert.equal(carpisma([K("yazi", "a", 0, 0, 100, 40), K("isaret", "h", 50, 10, 100, 20)]).length, 0);
  assert.equal(carpisma([K("kart", "k", 0, 0, 300, 100), K("yazi", "a", 10, 10, 100, 40)]).length, 0);
});

test("muaf: listedeki ad iki yönde de sayılmaz", () => {
  const y = K("yazi", "w1", 0, 0, 100, 40), h = K("halka", "m0", 50, 10, 100, 20, { muaf: ["w1"] });
  assert.equal(carpisma([y, h]).length, 0);
  assert.equal(carpisma([h, y]).length, 0);
  assert.equal(carpisma([y, { ...h, muaf: ["baska"] }]).length, 1);
});

test("halka ve altcizgi yazı karşısında cizim sayılır; künye karşısında da", () => {
  const y = K("yazi", "w", 0, 0, 100, 40);
  assert.equal(carpisma([y, K("halka", "h", 20, 10, 100, 20)])[0].tip, "hata");
  assert.equal(carpisma([y, K("altcizgi", "u", 20, 10, 100, 20)])[0].tip, "hata");
  assert.equal(carpisma([K("kunye", "k", 0, 0, 100, 40), K("altcizgi", "u", 20, 10, 100, 20)])[0].tip, "hata");
});

test("altcizgi × altcizgi hata; cizim × cizim ve altcizgi × halka sayılmaz", () => {
  assert.equal(carpisma([K("altcizgi", "u1", 0, 0, 100, 10), K("altcizgi", "u2", 20, 2, 100, 10)]).length, 1);
  assert.equal(carpisma([K("cizim", "c1", 0, 0, 100, 10), K("cizim", "c2", 20, 2, 100, 10)]).length, 0);
  assert.equal(carpisma([K("altcizgi", "u", 0, 0, 100, 10), K("halka", "h", 20, 2, 100, 10)]).length, 0);
});

test("pay: dar kesişim sayılmaz", () => {
  assert.equal(carpisma([K("altcizgi", "u1", 0, 0, 100, 10), K("altcizgi", "u2", 98, 0, 100, 10)]).length, 0);
});

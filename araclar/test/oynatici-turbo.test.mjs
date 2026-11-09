// Basılı tutma 2× durum makinesi (ortak/oynatici/turbo.js) — node --test araclar/test/
import { test } from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { fileURLToPath } from "node:url";

const KOK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const T = await import(path.join(KOK, "ortak", "oynatici", "turbo.js"));

test("bas → bekliyor; süre dolunca aktif; bırakınca tık bastırılır ve bos'a döner", () => {
  const s = T.turboKur();
  T.bas(s, 100, 100, 80);
  assert.equal(s.evre, "bekliyor"); assert.equal(T.hizli(s), false);
  T.sure(s);
  assert.equal(s.evre, "aktif"); assert.equal(T.hizli(s), true);
  assert.equal(T.birak(s), true);
  assert.equal(s.evre, "bos"); assert.equal(s.u, 0);
});

test("bekliyorken küçük titreme kalır, sapma iptal eder; geç gelen süre etkinleştirmez", () => {
  const s = T.turboKur();
  T.bas(s, 100, 100, 80);
  T.hareket(s, 104, 103);
  assert.equal(s.evre, "bekliyor");
  T.hareket(s, 100, 120);                      // 20 px > SAPMA_PX: kaydırma niyeti
  assert.equal(s.evre, "bos");
  T.sure(s);
  assert.equal(s.evre, "bos");
  assert.equal(T.birak(s), false);             // normal tık geçer
});

test("aktifken aşağı sürükleme halkayı doldurur, eşikte kilitlenir, bırakınca kilit kalır", () => {
  const s = T.turboKur();
  T.bas(s, 50, 200, 80); T.sure(s);
  T.hareket(s, 50, 240);
  assert.equal(s.u, 0.5); assert.equal(s.evre, "aktif");
  T.hareket(s, 50, 180);                       // yukarı: halka boşalır, eksiye düşmez
  assert.equal(s.u, 0);
  T.hareket(s, 50, 281);
  assert.equal(s.evre, "kilit"); assert.equal(s.u, 1);
  assert.equal(T.birak(s), true);
  assert.equal(s.evre, "kilit"); assert.equal(T.hizli(s), true);
  T.hareket(s, 50, 400);                       // kilitte hareket bir şey değiştirmez
  assert.equal(s.u, 1);
  T.kapat(s);
  assert.equal(s.evre, "bos"); assert.equal(s.u, 0); assert.equal(s.tutuyor, false);
});

test("kilitliyken sıradan dokunuş kilidi bozmaz ve tık geçer (duraklat çalışır)", () => {
  const s = T.turboKur();
  T.bas(s, 50, 200, 80); T.sure(s); T.hareket(s, 50, 300); T.birak(s);
  assert.equal(s.evre, "kilit");
  T.bas(s, 90, 90, 80);                        // yeni basış: kilit kalır
  assert.equal(s.evre, "kilit"); assert.equal(s.tutuyor, false);
  T.sure(s);                                   // geç zamanlayıcı: değişmez
  assert.equal(s.evre, "kilit");
  assert.equal(T.birak(s), false);             // tık bastırılmaz
  assert.equal(s.evre, "kilit"); assert.equal(T.hizli(s), true);
});

test("eşik alt sınırı 24 px; sabitler", () => {
  const s = T.turboKur();
  T.bas(s, 0, 0, 5);
  assert.equal(s.esik, 24);
  assert.equal(T.TURBO_HIZ, 2); assert.equal(T.BASILI_MS, 500); assert.equal(T.SAPMA_PX, 12);
});

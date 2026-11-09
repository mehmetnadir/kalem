// Arayüz sözlüğü ve dil çözümleme testi — node --test araclar/test/
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const KOK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const { DILLER, SOZLUK, sozlukSec, dilCoz } =
  await import(path.join(KOK, "ortak", "oynatici", "sozluk.js"));

test("(a) tr ve en anahtar kümeleri eşit ve boş değil", () => {
  const trAnahtarlar = Object.keys(SOZLUK.tr).sort();
  const enAnahtarlar = Object.keys(SOZLUK.en).sort();
  assert.ok(trAnahtarlar.length > 0, "tr anahtarları boş olmamalı");
  assert.deepEqual(trAnahtarlar, enAnahtarlar, "tr ve en anahtar kümeleri eşit olmalı");
  assert.deepEqual(DILLER, ["tr", "en"]);
});

test("(b) her anahtarda tür aynı ve fonksiyonlar örnekle boş dönmez", () => {
  for (const k of Object.keys(SOZLUK.tr)) {
    const vTr = SOZLUK.tr[k];
    const vEn = SOZLUK.en[k];
    assert.equal(typeof vTr, typeof vEn, `${k} türü eşleşmeli`);
    if (typeof vTr === "function") {
      const resTr = vTr("deneme", 2);
      const resEn = vEn("test", 2);
      assert.equal(typeof resTr, "string", `${k} (tr) dize dönmeli`);
      assert.equal(typeof resEn, "string", `${k} (en) dize dönmeli`);
      assert.ok(resTr.length > 0, `${k} (tr) boş dize dönmemeli`);
      assert.ok(resEn.length > 0, `${k} (en) boş dize dönmemeli`);
    } else {
      assert.equal(typeof vTr, "string", `${k} (tr) dize olmalı`);
      assert.equal(typeof vEn, "string", `${k} (en) dize olmalı`);
      assert.ok(vTr.length > 0, `${k} (tr) boş dize olmamalı`);
      assert.ok(vEn.length > 0, `${k} (en) boş dize olmamalı`);
    }
  }
});

test("(c) en değerlerinde Türkçe harf yok; tr değerlerinde ASCII ikame yok", () => {
  const trHarfRegex = /[çğıöşü]/i;
  for (const k of Object.keys(SOZLUK.en)) {
    const val = typeof SOZLUK.en[k] === "function" ? SOZLUK.en[k]("1", 2) : SOZLUK.en[k];
    assert.equal(trHarfRegex.test(val), false, `en.${k} Türkçe harf içermemeli: "${val}"`);
  }
  const trZorunlu = ["yukleniyor", "bolum", "bolumler", "hiz", "altyazi", "sesDuzeyi"];
  for (const k of trZorunlu) {
    const val = typeof SOZLUK.tr[k] === "function" ? SOZLUK.tr[k]("1", 2) : SOZLUK.tr[k];
    assert.ok(trHarfRegex.test(val), `tr.${k} Türkçe karakter içermeli: "${val}"`);
  }
});

test("(d) sozlukSec ve dilCoz kök ve seçenekleri doğru çözer", () => {
  assert.equal(sozlukSec("xx"), SOZLUK.tr);
  assert.equal(sozlukSec("en"), SOZLUK.en);
  assert.equal(sozlukSec("tr"), SOZLUK.tr);

  assert.equal(dilCoz({ dil: "en" }, {}), "en");
  assert.equal(dilCoz({ dil: "tr" }, {}), "tr");
  assert.equal(dilCoz({}, { lang: "en-US" }), "en");
  assert.equal(dilCoz({}, { lang: "tr-TR" }), "tr");
  assert.equal(dilCoz({}, { lang: "de" }), "tr");
  assert.equal(dilCoz({}, {}), "tr");
  assert.equal(dilCoz(null, null), "tr");
  assert.equal(dilCoz({ dil: "en" }, { lang: "tr" }), "en");
});

test("(e) kalem-oynatici.js Türkçe harfli dize içermez ve sözlük importu var", () => {
  const yol = path.join(KOK, "ortak", "oynatici", "kalem-oynatici.js");
  const kod = fs.readFileSync(yol, "utf8");
  assert.ok(kod.includes('from "./sozluk.js"'), "sozluk.js import edilmeli");

  const kodSatirlari = kod.split("\n").map((l) => l.replace(/\/\/.*$/, ""));
  const temizKod = kodSatirlari.join("\n");

  const ciftRegex = /"[^"\n]*[çğıöşüÇĞİÖŞÜ][^"\n]*"/g;
  const tekRegex = /'[^'\n]*[çğıöşüÇĞİÖŞÜ][^'\n]*'/g;

  const cift = temizKod.match(ciftRegex) || [];
  const tek = temizKod.match(tekRegex) || [];

  assert.equal(
    cift.length + tek.length,
    0,
    `Türkçe harfli string literal bulundu: ${[...cift, ...tek].join(", ")}`
  );
});

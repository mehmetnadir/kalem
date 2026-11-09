// Yön çifti mantığı (ortak/oynatici/yon.js) — node --test araclar/test/
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const KOK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const Y = await import(path.join(KOK, "ortak", "oynatici", "yon.js"));
const oku = (p) => JSON.parse(fs.readFileSync(path.join(KOK, "projeler", p, "zaman.json"), "utf8"));

test("yonAdi: ölçüden yön; kare yatay sayılır", () => {
  assert.equal(Y.yonAdi(1920, 1080), "yatay");
  assert.equal(Y.yonAdi(1080, 1920), "dikey");
  assert.equal(Y.yonAdi(1000, 1000), "yatay");
});

test("yonIstek: portrede dikey, yoksa olan; zorlama yalnız yüklü yönde", () => {
  const iki = { yatay: 1, dikey: 1 };
  assert.equal(Y.yonIstek(true, iki), "dikey");
  assert.equal(Y.yonIstek(false, iki), "yatay");
  assert.equal(Y.yonIstek(true, { yatay: 1 }), "yatay");
  assert.equal(Y.yonIstek(false, { dikey: 1 }), "dikey");
  assert.equal(Y.yonIstek(true, iki, "yatay"), "yatay");
  assert.equal(Y.yonIstek(true, { yatay: 1 }, "dikey"), "yatay");
  assert.equal(Y.yonIstek(true, {}), "");
});

test("ciftUyumlu: aynı klasör sırası ve zamanlar; sapma 0,05 sn'ye kadar", () => {
  const a = [{ klasor: "01", t_bas: 0, t_son: 3 }, { klasor: "02", t_bas: 3, t_son: 18.73 }];
  const b = [{ klasor: "01", t_bas: 0, t_son: 3.04 }, { klasor: "02", t_bas: 3.04, t_son: 18.73 }];
  assert.equal(Y.ciftUyumlu(a, b), true);
  assert.equal(Y.ciftUyumlu(a, [a[0]]), false);
  assert.equal(Y.ciftUyumlu(a, [a[0], { ...a[1], klasor: "03" }]), false);
  assert.equal(Y.ciftUyumlu(a, [a[0], { ...a[1], t_bas: 3.2 }]), false);
  assert.equal(Y.ciftUyumlu([], []), false);
});

test("present-perfect-temel yatay ve dikey paketleri kesintisiz geçişe uygun", () => {
  const y = oku("present-perfect-temel"), d = oku("present-perfect-temel-dikey");
  assert.equal(Y.yonAdi(y.genislik, y.yukseklik), "yatay");
  assert.equal(Y.yonAdi(d.genislik, d.yukseklik), "dikey");
  assert.equal(Y.ciftUyumlu(y.sahneler, d.sahneler), true);
  assert.equal(y.anlatim || "ortak/anlatim/anlatim.wav", d.anlatim || "ortak/anlatim/anlatim.wav");
});

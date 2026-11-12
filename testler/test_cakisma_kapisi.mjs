// testler/test_cakisma_kapisi.mjs
// Kapı ölçemediği sahneyi "geçti" saymaz: tarayıcıya ulaşılamazsa çıkış 2 (12.11: ölçüm hatası 0 dönüyordu).
import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const KOK = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const KAPI = path.join(KOK, "araclar", "cakisma-kapisi.mjs");

test("ölçüm hatası çıkış 2 verir ve JSON'a sayılır", () => {
  const gecici = fs.mkdtempSync(path.join(os.tmpdir(), "kapi-"));
  const json = path.join(gecici, "sonuc.json");
  const r = spawnSync("node", [KAPI, "present-continuous", "--sahne", "02-paperjs-kanca", "--port", "1",
    "--sunucu", "1", "--bekle", "1", "--json", json], { encoding: "utf8", timeout: 60000 });
  assert.equal(r.status, 2, r.stderr);
  assert.match(r.stderr, /ölçüm hatası/);
  const d = JSON.parse(fs.readFileSync(json, "utf8"));
  assert.equal(d.ozet.olcumHatasi, 1);
  assert.equal(d.sahneler[0].durum, "hata");
});

test("HyperFrames sahnesi tek başına ölçülmedi sayılır, hata değildir", () => {
  const r = spawnSync("node", [KAPI, "present-continuous", "--sahne", "01-hyperframes-giris", "--port", "1",
    "--sunucu", "1"], { encoding: "utf8", timeout: 60000 });
  assert.equal(r.status, 0, r.stderr);
  assert.match(r.stdout, /ölçülmedi \(HyperFrames\)/);
});

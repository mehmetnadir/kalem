// testler/test_cakisma_kapisi.mjs
// Kapı ölçemediği sahneyi "geçti" saymaz: tarayıcıya ulaşılamazsa çıkış 2 (12.11: ölçüm hatası 0 dönüyordu).
import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { kareleriIsle, cdpGonderici } from "../araclar/sahne-kare.mjs";

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

test("örneksiz sahne çıkış 2 verir ve ozet.olcumHatasi artar", () => {
  const gecici = fs.mkdtempSync(path.join(os.tmpdir(), "kapi-ornek-"));
  const json = path.join(gecici, "sonuc.json");
  const dummyBetik = path.join(gecici, "dummy-sahne-kare.mjs");
  fs.writeFileSync(dummyBetik, "#!/usr/bin/env node\n// hicbir json satiri basmaz\nprocess.exit(0);\n");
  fs.chmodSync(dummyBetik, 0o755);

  const env = { ...process.env, SAHNE_KARE_BETIK: dummyBetik };
  const r = spawnSync("node", [KAPI, "present-continuous", "--sahne", "02-paperjs-kanca", "--json", json], {
    encoding: "utf8",
    env,
    timeout: 30000,
  });
  assert.equal(r.status, 2, r.stderr);
  assert.match(r.stdout, /ölçüm hatası: örnek kare alınamadı/);
  const d = JSON.parse(fs.readFileSync(json, "utf8"));
  assert.equal(d.ozet.olcumHatasi, 1);
  assert.equal(d.sahneler[0].durum, "hata");
  assert.equal(d.sahneler[0].hata, "örnek kare alınamadı");
});

test("PNG'siz kipte (--png 0) Page.captureScreenshot çağrılmaz", async () => {
  const cdpCagrilari = [];
  const fakeG = async (method, params = {}) => {
    cdpCagrilari.push(method);
    if (method === "Page.captureScreenshot") {
      return { data: Buffer.from("fake-png").toString("base64") };
    }
    return {};
  };
  let beklenenKare = 0;
  const fakeEv = async (expr) => {
    const postMatch = expr.match(/tip: "zaman", t: ([\d.]+)/);
    if (postMatch) {
      const t = Number(postMatch[1]);
      beklenenKare = Math.max(0, Math.min(S.kare - 1, Math.floor((t - S.t_bas) * 30)));
    }
    if (expr.includes("document.body.children")) return `${beklenenKare} / 100 · 0.33 sn`;
    return undefined;
  };
  const S = { klasor: "02-test", kare: 100, t_bas: 0, t_son: 1 };
  const zamanlar = [0.1, 0.2];
  const gecici = fs.mkdtempSync(path.join(os.tmpdir(), "kare-test-"));

  // 1. Durum: sec.png = "0" -> Page.captureScreenshot cagrilmaz
  const satirlar1 = await kareleriIsle({
    g: fakeG,
    ev: fakeEv,
    zamanlar,
    S,
    fps: 30,
    bekle: 1,
    cikti: gecici,
    sahne: "02-test",
    sec: { png: "0" },
    sessionId: "test-ses",
    log: () => {},
    uykuFn: () => Promise.resolve(),
  });
  assert.equal(satirlar1.length, 2);
  assert.ok(!cdpCagrilari.includes("Page.captureScreenshot"), "PNG'siz kipte Page.captureScreenshot çağrılmamalı");
  assert.equal(satirlar1[0].png, undefined);

  // 2. Durum: varsayılan kip (sec = {}) -> Page.captureScreenshot cagirilir
  cdpCagrilari.length = 0;
  const satirlar2 = await kareleriIsle({
    g: fakeG,
    ev: fakeEv,
    zamanlar,
    S,
    fps: 30,
    bekle: 1,
    cikti: gecici,
    sahne: "02-test",
    sec: {},
    sessionId: "test-ses",
    log: () => {},
    uykuFn: () => Promise.resolve(),
  });
  assert.equal(satirlar2.length, 2);
  assert.ok(cdpCagrilari.includes("Page.captureScreenshot"), "Varsayılan kipte Page.captureScreenshot çağrılmalı");
  assert.ok(satirlar2[0].png);
  assert.ok(fs.existsSync(satirlar2[0].png));
});

test("CDP çağrı zaman aşımı anlamlı hata fırlatır", async () => {
  const fakeWs = { send: () => {} };
  const { g } = cdpGonderici(fakeWs, { cdpZaman: 0.05 });
  await assert.rejects(
    () => g("Page.captureScreenshot"),
    /CDP zaman aşımı \(0\.05 sn\): Page\.captureScreenshot/
  );
});

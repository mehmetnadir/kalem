// bolum-kur.py testleri — node:test ile
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import crypto from "node:crypto";
import child_process from "node:child_process";
import { fileURLToPath } from "node:url";

const KOK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const BETIK_YOLU = path.join(KOK, "araclar", "bolum-kur.py");
const PYTHON = "/usr/bin/python3";

function sha256Hesapla(dosyaYolu) {
  const veri = fs.readFileSync(dosyaYolu);
  return crypto.createHash("sha256").update(veri).digest("hex");
}

function fixtureKur() {
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "kalem-bolum-test-"));
  const aDir = path.join(tmpDir, "projeler", "a");
  const denemeDir = path.join(tmpDir, "projeler", "deneme-x");
  fs.mkdirSync(aDir, { recursive: true });
  fs.mkdirSync(denemeDir, { recursive: true });

  const aZaman = {
    fps: 30,
    genislik: 1920,
    yukseklik: 1080,
    sahneler: [
      {
        no: 1,
        klasor: "01-hyperframes-giris",
        motor: "HyperFrames",
        kare: 102,
        ad: "Örnek 1",
        gecis: "BookFlip",
      },
      {
        no: 2,
        klasor: "04-canvas-ornek2",
        motor: "Canvas",
        kare: 120,
      },
    ],
  };

  const denemeZaman = {
    fps: 30,
    sahneler: [
      {
        no: 1,
        klasor: "01-hyperframes-deneme",
        ad: "Deneme",
      },
    ],
  };

  fs.writeFileSync(
    path.join(aDir, "zaman.json"),
    JSON.stringify(aZaman, null, 2) + "\n",
    "utf8"
  );
  fs.writeFileSync(
    path.join(denemeDir, "zaman.json"),
    JSON.stringify(denemeZaman, null, 2) + "\n",
    "utf8"
  );

  return tmpDir;
}

test("(1) kuru koşu dosyanın sha256'sını değiştirmez, a'yı basar ve deneme-x'i atlar", (t) => {
  const fixtureKok = fixtureKur();
  t.after(() => fs.rmSync(fixtureKok, { recursive: true, force: true }));

  const zamanYolu = path.join(fixtureKok, "projeler", "a", "zaman.json");
  const oncekiSha = sha256Hesapla(zamanYolu);

  const res = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok],
    { cwd: fixtureKok, encoding: "utf8" }
  );

  assert.equal(res.status, 0);
  assert.equal(sha256Hesapla(zamanYolu), oncekiSha);
  assert.match(res.stdout, /a \| sahne 2 \| yazılacak 2 \| değişmez 0/);
  assert.doesNotMatch(res.stdout, /deneme-x/);
});

test("(2) --yaz sonrası bolum değerleri, indent 2 ve anahtar sırası doğrudur", (t) => {
  const fixtureKok = fixtureKur();
  t.after(() => fs.rmSync(fixtureKok, { recursive: true, force: true }));

  const zamanYolu = path.join(fixtureKok, "projeler", "a", "zaman.json");

  const res = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz"],
    { cwd: fixtureKok, encoding: "utf8" }
  );

  assert.equal(res.status, 0);

  const metin = fs.readFileSync(zamanYolu, "utf8");
  assert.ok(metin.endsWith("\n"), "Dosya sonunda tek satır sonu bulunmalıdır");

  // Geçerli JSON ve sahne değerleri
  const veri = JSON.parse(metin);
  assert.equal(veri.sahneler.length, 2);

  const s1 = veri.sahneler[0];
  assert.equal(s1.bolum, "Örnek 1");
  assert.equal(s1.gecis, "BookFlip");

  const s2 = veri.sahneler[1];
  assert.equal(s2.bolum, "ornek2");

  // İndent 2 kontrolü: nesne derinliğine göre 2, 4, 6 boşluk
  assert.match(metin, /\n  "sahneler": \[/);
  assert.match(metin, /\n {6}"ad": "Örnek 1",\n {6}"bolum": "Örnek 1",/);

  // s1'de bolum anahtarı ad'dan hemen sonra
  const s1Anahtarlar = Object.keys(s1);
  const adKonum = s1Anahtarlar.indexOf("ad");
  const bolumKonum1 = s1Anahtarlar.indexOf("bolum");
  assert.equal(bolumKonum1, adKonum + 1);

  // s2'de ad yok, bolum anahtarı klasor'dan hemen sonra
  const s2Anahtarlar = Object.keys(s2);
  const klasorKonum = s2Anahtarlar.indexOf("klasor");
  const bolumKonum2 = s2Anahtarlar.indexOf("bolum");
  assert.equal(bolumKonum2, klasorKonum + 1);
});

test("(3) ikinci --yaz idempotenttir: yazılacak 0 | değişmez 2", (t) => {
  const fixtureKok = fixtureKur();
  t.after(() => fs.rmSync(fixtureKok, { recursive: true, force: true }));

  // İlk yazma
  const ilk = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz"],
    { cwd: fixtureKok, encoding: "utf8" }
  );
  assert.equal(ilk.status, 0);

  const zamanYolu = path.join(fixtureKok, "projeler", "a", "zaman.json");
  const ilkSha = sha256Hesapla(zamanYolu);

  // İkinci yazma (idempotent)
  const ikinci = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz"],
    { cwd: fixtureKok, encoding: "utf8" }
  );
  assert.equal(ikinci.status, 0);
  assert.match(ikinci.stdout, /a \| sahne 2 \| yazılacak 0 \| değişmez 2/);
  assert.equal(sha256Hesapla(zamanYolu), ilkSha);
});

test("(4) --zorla ile mevcut bolum değerleri yeniden yazılır", (t) => {
  const fixtureKok = fixtureKur();
  t.after(() => fs.rmSync(fixtureKok, { recursive: true, force: true }));

  // İlk yazma
  child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz"],
    { cwd: fixtureKok, encoding: "utf8" }
  );

  const zamanYolu = path.join(fixtureKok, "projeler", "a", "zaman.json");
  const veri = JSON.parse(fs.readFileSync(zamanYolu, "utf8"));
  veri.sahneler[0].bolum = "Eski Bolum";
  veri.sahneler[1].bolum = "eski2";
  fs.writeFileSync(zamanYolu, JSON.stringify(veri, null, 2) + "\n", "utf8");

  // Zorla yeniden yazma
  const res = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz", "--zorla"],
    { cwd: fixtureKok, encoding: "utf8" }
  );
  assert.equal(res.status, 0);
  assert.match(res.stdout, /a \| sahne 2 \| yazılacak 2 \| değişmez 0/);

  const sonVeri = JSON.parse(fs.readFileSync(zamanYolu, "utf8"));
  assert.equal(sonVeri.sahneler[0].bolum, "Örnek 1");
  assert.equal(sonVeri.sahneler[1].bolum, "ornek2");
});

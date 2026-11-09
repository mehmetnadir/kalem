// ses-paketle.py testleri — node:test ile
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import crypto from "node:crypto";
import child_process from "node:child_process";
import { fileURLToPath } from "node:url";

const KOK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const BETIK_YOLU = path.join(KOK, "araclar", "ses-paketle.py");
const PYTHON = "/usr/bin/python3";

function ffmpegYoluBul() {
  for (const aday of ["/opt/homebrew/bin/ffmpeg", "/usr/local/bin/ffmpeg"]) {
    if (fs.existsSync(aday)) return aday;
  }
  return null;
}

function ffprobeYoluBul() {
  for (const aday of ["/opt/homebrew/bin/ffprobe", "/usr/local/bin/ffprobe"]) {
    if (fs.existsSync(aday)) return aday;
  }
  return null;
}

function sha256Hesapla(dosyaYolu) {
  const veri = fs.readFileSync(dosyaYolu);
  return crypto.createHash("sha256").update(veri).digest("hex");
}

function fixtureKur() {
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "kalem-ses-test-"));
  const aDir = path.join(tmpDir, "projeler", "a");
  const aAnlatimDir = path.join(aDir, "ortak", "anlatim");
  const aDikeyDir = path.join(tmpDir, "projeler", "a-dikey");
  const aDikeyOrtakDir = path.join(aDikeyDir, "ortak");
  const denemeDir = path.join(tmpDir, "projeler", "deneme-x");

  fs.mkdirSync(aAnlatimDir, { recursive: true });
  fs.mkdirSync(aDikeyOrtakDir, { recursive: true });
  fs.mkdirSync(denemeDir, { recursive: true });

  const ffmpeg = ffmpegYoluBul();
  if (ffmpeg) {
    const wavYolu = path.join(aAnlatimDir, "anlatim.wav");
    child_process.execFileSync(
      ffmpeg,
      [
        "-y",
        "-f",
        "lavfi",
        "-i",
        "sine=frequency=440:duration=2",
        "-ar",
        "48000",
        "-ac",
        "1",
        "-c:a",
        "pcm_s16le",
        wavYolu,
      ],
      { stdio: "pipe" }
    );
  }

  const aZaman = {
    fps: 30,
    anlatim: "ortak/anlatim/anlatim.wav",
    sahneler: [],
  };
  fs.writeFileSync(
    path.join(aDir, "zaman.json"),
    JSON.stringify(aZaman, null, 2) + "\n",
    "utf8"
  );

  fs.symlinkSync(
    path.join("..", "..", "a", "ortak", "anlatim"),
    path.join(aDikeyOrtakDir, "anlatim")
  );

  const aDikeyZaman = {
    fps: 30,
    anlatim: "ortak/anlatim/anlatim.wav",
    sahneler: [],
  };
  fs.writeFileSync(
    path.join(aDikeyDir, "zaman.json"),
    JSON.stringify(aDikeyZaman, null, 2) + "\n",
    "utf8"
  );

  const denemeZaman = {
    fps: 30,
    anlatim: "ortak/anlatim/anlatim.wav",
    sahneler: [],
  };
  fs.writeFileSync(
    path.join(denemeDir, "zaman.json"),
    JSON.stringify(denemeZaman, null, 2) + "\n",
    "utf8"
  );

  return tmpDir;
}

test(
  "(1) kuru koşu dosya üretmez, zaman.json sha256 aynı, çıktıda a ve a-dikey satırı var",
  (t) => {
  const ffmpeg = ffmpegYoluBul();
  if (!ffmpeg) {
    t.skip("ffmpeg bulunamadı");
    return;
  }
  const fixtureKok = fixtureKur();
  t.after(() => fs.rmSync(fixtureKok, { recursive: true, force: true }));

  const aZaman = path.join(fixtureKok, "projeler", "a", "zaman.json");
  const aDikeyZaman = path.join(fixtureKok, "projeler", "a-dikey", "zaman.json");
  const aM4a = path.join(fixtureKok, "projeler", "a", "ortak", "anlatim", "anlatim.m4a");
  const aImza = path.join(fixtureKok, "projeler", "a", "ortak", "anlatim", "anlatim.m4a.imza");

  const shaAOnce = sha256Hesapla(aZaman);
  const shaADikeyOnce = sha256Hesapla(aDikeyZaman);

  const res = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok],
    { cwd: fixtureKok, encoding: "utf8" }
  );

  assert.equal(res.status, 0);
  assert.equal(fs.existsSync(aM4a), false);
  assert.equal(fs.existsSync(aImza), false);
  assert.equal(sha256Hesapla(aZaman), shaAOnce);
  assert.equal(sha256Hesapla(aDikeyZaman), shaADikeyOnce);
  assert.match(res.stdout, /\ba \| wav/);
  assert.match(res.stdout, /\ba-dikey \| wav/);
  assert.doesNotMatch(res.stdout, /deneme-x/);
});

test(
  "(2) --yaz: anlatim.m4a var, ffprobe süre 2,0 ± 0,1, imza var, zaman.json güncel",
  (t) => {
  const ffmpeg = ffmpegYoluBul();
  const ffprobe = ffprobeYoluBul();
  if (!ffmpeg || !ffprobe) {
    t.skip("ffmpeg veya ffprobe bulunamadı");
    return;
  }
  const fixtureKok = fixtureKur();
  t.after(() => fs.rmSync(fixtureKok, { recursive: true, force: true }));

  const aZamanYolu = path.join(fixtureKok, "projeler", "a", "zaman.json");
  const aDikeyZamanYolu = path.join(fixtureKok, "projeler", "a-dikey", "zaman.json");
  const aM4aYolu = path.join(fixtureKok, "projeler", "a", "ortak", "anlatim", "anlatim.m4a");
  const aImzaYolu = path.join(fixtureKok, "projeler", "a", "ortak", "anlatim", "anlatim.m4a.imza");

  const res = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz"],
    { cwd: fixtureKok, encoding: "utf8" }
  );

  assert.equal(res.status, 0);
  assert.equal(fs.existsSync(aM4aYolu), true);
  assert.equal(fs.existsSync(aImzaYolu), true);

  const probeRes = child_process.execFileSync(
    ffprobe,
    [
      "-v",
      "error",
      "-show_entries",
      "format=duration",
      "-of",
      "default=noprint_wrappers=1:nokey=1",
      aM4aYolu,
    ],
    { encoding: "utf8" }
  );
  const sure = parseFloat(probeRes.trim());
  assert.ok(Math.abs(sure - 2.0) <= 0.1, `Süre 2.0+-0.1 olmalı, bulunan: ${sure}`);

  const aMetin = fs.readFileSync(aZamanYolu, "utf8");
  const aDikeyMetin = fs.readFileSync(aDikeyZamanYolu, "utf8");
  const aVeri = JSON.parse(aMetin);
  const aDikeyVeri = JSON.parse(aDikeyMetin);

  assert.equal(aVeri.anlatim, "ortak/anlatim/anlatim.m4a");
  assert.equal(aDikeyVeri.anlatim, "ortak/anlatim/anlatim.m4a");
  assert.equal(aVeri.fps, 30);
  assert.deepEqual(aVeri.sahneler, []);
  assert.equal(aDikeyVeri.fps, 30);
  assert.deepEqual(aDikeyVeri.sahneler, []);

  const beklenenA = JSON.stringify(aVeri, null, 2) + "\n";
  assert.equal(aMetin, beklenenA);
});

test("(3) ikinci --yaz: m4a mtime değişmez (\"atlandı\"), çıkış 0", (t) => {
  const ffmpeg = ffmpegYoluBul();
  const ffprobe = ffprobeYoluBul();
  if (!ffmpeg || !ffprobe) {
    t.skip("ffmpeg veya ffprobe bulunamadı");
    return;
  }
  const fixtureKok = fixtureKur();
  t.after(() => fs.rmSync(fixtureKok, { recursive: true, force: true }));

  const aM4aYolu = path.join(fixtureKok, "projeler", "a", "ortak", "anlatim", "anlatim.m4a");

  const res1 = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz"],
    { cwd: fixtureKok, encoding: "utf8" }
  );
  assert.equal(res1.status, 0);
  assert.equal(fs.existsSync(aM4aYolu), true);

  const eskiZaman = 1000000;
  fs.utimesSync(aM4aYolu, eskiZaman, eskiZaman);
  const mtimeOnce = fs.statSync(aM4aYolu).mtimeMs;

  const res2 = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz"],
    { cwd: fixtureKok, encoding: "utf8" }
  );
  assert.equal(res2.status, 0);
  const mtimeSonra = fs.statSync(aM4aYolu).mtimeMs;
  assert.equal(mtimeSonra, mtimeOnce);
  assert.match(res2.stdout, /atlandı/);
});

test(
  "(4) --zorla: yeniden üretir (mtime ileri gider; gerekirse utimesSync ile eskit)",
  (t) => {
  const ffmpeg = ffmpegYoluBul();
  const ffprobe = ffprobeYoluBul();
  if (!ffmpeg || !ffprobe) {
    t.skip("ffmpeg veya ffprobe bulunamadı");
    return;
  }
  const fixtureKok = fixtureKur();
  t.after(() => fs.rmSync(fixtureKok, { recursive: true, force: true }));

  const aM4aYolu = path.join(fixtureKok, "projeler", "a", "ortak", "anlatim", "anlatim.m4a");

  const res1 = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz"],
    { cwd: fixtureKok, encoding: "utf8" }
  );
  assert.equal(res1.status, 0);

  const eskiZaman = 1000000;
  fs.utimesSync(aM4aYolu, eskiZaman, eskiZaman);

  const res2 = child_process.spawnSync(
    PYTHON,
    ["-I", BETIK_YOLU, "--kok", fixtureKok, "--yaz", "--zorla"],
    { cwd: fixtureKok, encoding: "utf8" }
  );
  assert.equal(res2.status, 0);
  const mtimeSonra = fs.statSync(aM4aYolu).mtimeMs;
  const msSinir = eskiZaman * 1000;
  assert.ok(mtimeSonra > msSinir, `mtime ileri gitmeli: ${mtimeSonra} > ${msSinir}`);
});

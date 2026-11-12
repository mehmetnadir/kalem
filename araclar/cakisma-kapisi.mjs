#!/usr/bin/env node
// araclar/cakisma-kapisi.mjs
// Videonun her karesinde yazı ile çizimin üst üste binip binmediğini otomatik ölçen kapı.
//   node araclar/cakisma-kapisi.mjs <paket> [--sahne <klasör>] [--sikilik 4] [--pay 4]
//     [--json çıktı.json] [--gorsel <dizin>] [--bekle 15] [--port 9333] [--sunucu 3012]
//
// Kural BRIEF 2.6: çakışma 0 px (yazı × çizim, yazı × künye).
// Çıkış kodları:
//   0: Hata yok (tüm kontroller geçti)
//   1: Hata var (çakışma tespit edildi)
//   2: Kullanım veya ölçüm yapılamadı

import fs from "node:fs";
import path from "node:path";
import { spawn } from "node:child_process";
import readline from "node:readline";
import { carpisma, olaylariBirlestir } from "./cakisma-olcer.mjs";

const argv = process.argv.slice(2), sec = {}, kon = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i].startsWith("--")) {
    sec[argv[i].slice(2)] = argv[i + 1];
    i++;
  } else {
    kon.push(argv[i]);
  }
}

const [paket] = kon;
if (!paket) {
  console.error("kullanım: node araclar/cakisma-kapisi.mjs <paket> [--sahne <klasör>] [--sikilik 4] [--pay 4] [--json çıktı.json] [--gorsel <dizin>]");
  process.exit(2);
}

const KOK = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const zamanYol = path.join(KOK, "projeler", paket, "zaman.json");
if (!fs.existsSync(zamanYol)) {
  console.error("HATA zaman.json bulunamadı:", zamanYol);
  process.exit(2);
}

const zaman = JSON.parse(fs.readFileSync(zamanYol, "utf8"));
const sikilik = +(sec.sikilik || 4);
const pay = +(sec.pay || 4);
const bekle = +(sec.bekle || 15);
const port = sec.port || "9333";
const sunucu = sec.sunucu || "3012";

let sahneler = zaman.sahneler || [];
if (sec.sahne) {
  sahneler = sahneler.filter((s) => s.klasor === sec.sahne);
  if (sahneler.length === 0) {
    console.error("HATA sahne bulunamadı:", sec.sahne);
    process.exit(2);
  }
}

// Geçici PNG deposu
const geciciPngDizin = path.join(KOK, "_is", "cakisma", "ham_png");
fs.mkdirSync(geciciPngDizin, { recursive: true });

if (sec.gorsel) {
  fs.mkdirSync(path.resolve(sec.gorsel), { recursive: true });
}

const sahneKareBetik = path.join(KOK, "araclar", "sahne-kare.mjs");
const olcKod = "JSON.stringify((() => { if (window.__kalemKutu?.paperTopla) window.__kalemKutu.paperTopla(); return window.__kalemKutu?.kare || []; })())";

function sahneKareCalistir(args) {
  return new Promise((resolve, reject) => {
    const cp = spawn("node", args, { stdio: ["ignore", "pipe", "pipe"] });
    const satirlar = [];
    let stderrMetin = "";

    const rl = readline.createInterface({ input: cp.stdout });
    rl.on("line", (line) => {
      const l = line.trim();
      if (l.startsWith("{")) satirlar.push(l);
    });

    cp.stderr.on("data", (d) => {
      stderrMetin += d.toString();
    });

    cp.on("error", (err) => reject(err));
    cp.on("close", (code) => {
      if (code !== 0 && satirlar.length === 0) {
        reject(new Error(stderrMetin.trim() || `sahne-kare çıkış kodu: ${code}`));
      } else {
        resolve(satirlar);
      }
    });
  });
}

const sonuclar = [];
let toplamHata = 0;
let toplamUyari = 0;
let olculenSayisi = 0;
let olculmediSayisi = 0;
let kutusuzSahne = 0;
let olcumHatasi = 0;

for (const S of sahneler) {
  if (S.motor === "HyperFrames") {
    console.log(`${S.klasor} | ölçülmedi (HyperFrames)`);
    sonuclar.push({
      sahne: S.klasor,
      motor: S.motor,
      durum: "olculmedi",
      neden: "HyperFrames",
      olaylar: [],
    });
    olculmediSayisi++;
    continue;
  }

  // Örnekleme zamanlarını oluştur (saniyede 'sikilik' örnek)
  const dt = 1 / sikilik;
  const zamanlar = [];
  for (let t = S.t_bas; t <= S.t_son + 0.0001; t += dt) {
    zamanlar.push(+t.toFixed(2));
  }
  if (zamanlar.length === 0 || zamanlar[zamanlar.length - 1] < S.t_son - 0.05) {
    zamanlar.push(+S.t_son.toFixed(2));
  }

  try {
    const args = [
      sahneKareBetik,
      paket,
      S.klasor,
      zamanlar.join(","),
      geciciPngDizin,
      "--bekle", String(bekle),
      "--port", String(port),
      "--sunucu", String(sunucu),
      "--olc", olcKod,
    ];

    const satirlar = await sahneKareCalistir(args);
    const ornekler = [];
    // Kancasız sahne hiç kutu üretmez; "çakışma yok" sanılmasın (12.11: present-perfect-temel 03/05
    // kancasızken 0 uyarı raporlanmıştı).
    let kutuToplam = 0;

    for (const sat of satirlar) {
      try {
        const veri = JSON.parse(sat);
        const kutular = JSON.parse(veri.olc || "[]");
        kutuToplam += Array.isArray(kutular) ? kutular.length : 0;
        const carpismalar = carpisma(kutular, { pay });
        ornekler.push({
          t: veri.t,
          carpismalar,
          png: veri.png,
        });
      } catch (er) {
        console.error("JSON parse hatası:", er.message, sat.slice(0, 80));
      }
    }

    if (kutuToplam === 0) {
      console.log(`${S.klasor} | ölçülmedi (kanca kutu üretmedi, ${ornekler.length} örnek)`);
      sonuclar.push({
        sahne: S.klasor,
        motor: S.motor,
        durum: "olculmedi",
        neden: "kutu yok (kanca eksik)",
        ornekSayisi: ornekler.length,
        olaylar: [],
      });
      olculmediSayisi++;
      kutusuzSahne++;
      continue;
    }

    const olaylar = olaylariBirlestir(ornekler);
    const sahneHatalar = olaylar.filter((o) => o.tip === "hata");
    const sahneUyarilar = olaylar.filter((o) => o.tip === "uyari");

    toplamHata += sahneHatalar.length;
    toplamUyari += sahneUyarilar.length;
    olculenSayisi++;

    if (olaylar.length === 0) {
      console.log(`${S.klasor} | çakışma yok (${ornekler.length} örnek, ${kutuToplam} kutu)`);
    } else {
      for (const o of olaylar) {
        const kesMetin = `${o.kesisim.w}x${o.kesisim.h} px`;
        console.log(`${S.klasor} | ${o.t0.toFixed(2)}-${o.t1.toFixed(2)} sn | ${o.a} × ${o.b} | kesişim ${kesMetin} | ${o.tip}`);

        // --gorsel verilirse hata olayının ilk karesini kopyala
        if (sec.gorsel && o.tip === "hata" && o.png && fs.existsSync(o.png)) {
          const hedefPng = path.join(path.resolve(sec.gorsel), `${S.klasor}-${o.t0}.png`);
          fs.copyFileSync(o.png, hedefPng);
          o.gorsel = hedefPng;
        }
      }
    }

    sonuclar.push({
      sahne: S.klasor,
      motor: S.motor,
      durum: "olculdu",
      ornekSayisi: ornekler.length,
      kutuSayisi: kutuToplam,
      t_bas: S.t_bas,
      t_son: S.t_son,
      olaylar,
    });
  } catch (er) {
    console.error(`${S.klasor} | ölçüm hatası: ${er.message.trim()}`);
    olcumHatasi++;
    sonuclar.push({
      sahne: S.klasor,
      motor: S.motor,
      durum: "hata",
      hata: er.message,
      olaylar: [],
    });
  }
}

// JSON çıktısı istenmişse yaz
if (sec.json) {
  const ciktiDosya = path.resolve(sec.json);
  fs.mkdirSync(path.dirname(ciktiDosya), { recursive: true });
  const ozet = {
    paket,
    sikilik,
    pay,
    tarih: new Date().toISOString(),
    ozet: {
      toplamSahne: sahneler.length,
      olculen: olculenSayisi,
      olculmedi: olculmediSayisi,
      olcumHatasi,
      toplamHata,
      toplamUyari,
    },
    sahneler: sonuclar,
  };
  fs.writeFileSync(ciktiDosya, JSON.stringify(ozet, null, 2), "utf8");
}

if (toplamHata > 0) {
  process.exit(1);
} else if (olcumHatasi > 0) {
  // 12.11: present-perfect-ileri 03 "sahne hazır olmadı" ile ölçülemedi, kapı yine 0 dönmüştü.
  console.error(`UYARI: ${olcumHatasi} sahne ölçülemedi (ölçüm hatası); kapı geçti sayılmaz`);
  process.exit(2);
} else if (kutusuzSahne > 0) {
  // Canvas/Paper.js sahnesi ölçülemedi: geçti sayılmaz.
  console.error(`UYARI: ${kutusuzSahne} sahne kutu üretmedi (kanca eksik); kapı geçti sayılmaz`);
  process.exit(2);
} else {
  process.exit(0);
}

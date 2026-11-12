#!/usr/bin/env node
// Başsız sahne karesi: sahneyi editör protokolüyle (?canli=1&mesaj=1&tbas) ortak Chrome'da
// (CDP 9333) açar, verilen anlatım zamanlarında {tip:"zaman",t} yollar, kare çizilince PNG alır.
//   node araclar/sahne-kare.mjs <paket> <sahne-klasörü> <t1,t2,…> <çıktı-dizini>
//     [--tema acik|koyu] [--port 9333] [--sunucu 3012] [--olc "<js>"] [--bekle 30]
//     [--cdp-zaman 20] [--png 0|1]
//   t = anlatım saniyesi (zaman.json t_bas…t_son). Çıktı: <dizin>/<sahne>-<t>.png
//   --olc: her karede koşan JS; sonucu JSON satırına "olc" olarak girer (ölçüm için).
//   --png 0: ekran görüntüsü (Page.captureScreenshot) almaz, salt veri ölçümü yapar.
//   --cdp-zaman: CDP çağrı zaman aşımı (sn, varsayılan 20).
//   --bekle: sayaç bekleme zaman aşımı (sn, varsayılan 30).
//   --dbg 1: ağ olaylarını ve hazır olmayan sayfanın durumunu yazar (arıza ayıklama).
//   Önkoşul: 3012 editör sunucusu (ortak/onizle-sunucu.mjs) ve 9333 ortak başsız Chrome açık.
//   Tarayıcı AÇMAZ, mp4 üretmez, yalnız PNG yazar. Ajanlar hyperframes/npx koşturmaz; bu araç
//   yeter.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

export const uyku = (ms) => new Promise((r) => setTimeout(r, ms));

// Sayaç kutusu: canliCekirdek gizli div'e "f / KARE · s sn" yazar; çizim bitince f beklenen
// kareye gelir.
export const SAYAC = `(() => { const d = [...document.body.children]
  .find((e) => /^\\d+ \\/ \\d+/.test(e.textContent || "")); return d ? d.textContent : ""; })()`;

export function cdpGonderici(ws, { cdpZaman = 20 } = {}) {
  let n = 0;
  const bk = new Map();

  const g = (method, params = {}, sessionId) => new Promise((ok, hata) => {
    const i = ++n;
    let zamanlayici = null;
    if (cdpZaman > 0) {
      zamanlayici = setTimeout(() => {
        if (bk.has(i)) {
          bk.delete(i);
          hata(new Error(`CDP zaman aşımı (${cdpZaman} sn): ${method}`));
        }
      }, cdpZaman * 1000);
    }
    bk.set(i, {
      ok: (res) => {
        if (zamanlayici) clearTimeout(zamanlayici);
        ok(res);
      },
      hata: (err) => {
        if (zamanlayici) clearTimeout(zamanlayici);
        hata(err);
      },
    });
    ws.send(JSON.stringify({ id: i, method, params, ...(sessionId ? { sessionId } : {}) }));
  });

  const mesajIsle = (data) => {
    const m = typeof data === "string" ? JSON.parse(data) : JSON.parse(data.toString());
    if (!m.id || !bk.has(m.id)) return m;
    const p = bk.get(m.id);
    bk.delete(m.id);
    m.error ? p.hata(new Error(m.error.message)) : p.ok(m.result);
    return m;
  };

  const temizle = () => {
    for (const [, p] of bk.entries()) {
      p.hata(new Error("CDP WebSocket kapandı"));
    }
    bk.clear();
  };

  return { g, mesajIsle, temizle, bk };
}

export async function kareleriIsle({
  g,
  ev,
  zamanlar,
  S,
  fps,
  bekle,
  cikti,
  sahne,
  sec = {},
  sessionId,
  log = console.log,
  uykuFn = uyku,
}) {
  const satirlar = [];
  const pngAl = sec.png !== "0" && sec.png !== "false";
  for (const t of zamanlar) {
    const f = Math.max(0, Math.min(S.kare - 1, Math.floor((t - S.t_bas) * fps)));
    await ev(`window.postMessage({ tip: "zaman", t: ${t} }, "*"); true`);
    let t0 = Date.now();
    let m = "";
    while (Date.now() - t0 < bekle * 1000) {
      m = await ev(SAYAC);
      if (m && m.startsWith(f + " /")) break;
      await uykuFn(50);
    }
    await uykuFn(200); // bekleyen async çizim / font için pay
    let ad = null, bayt = null;
    if (pngAl) {
      ad = path.join(cikti, `${sahne}-${t}.png`);
      const sc = await g("Page.captureScreenshot", { format: "png" }, sessionId);
      fs.writeFileSync(ad, Buffer.from(sc.data, "base64"));
      bayt = fs.statSync(ad).size;
    }
    const olc = sec.olc ? await ev(sec.olc) : undefined;
    const satir = { t, kare: f, sayac: m };
    if (pngAl) {
      satir.png = ad;
      satir.bayt = bayt;
    }
    if (olc !== undefined) satir.olc = olc;
    satirlar.push(satir);
    log(JSON.stringify(satir));
  }
  return satirlar;
}

const suAnkiDosya = fileURLToPath(import.meta.url);
if (process.argv[1] && path.resolve(process.argv[1]) === suAnkiDosya) {
  const argv = process.argv.slice(2), sec = {}, kon = [];
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith("--")) { sec[argv[i].slice(2)] = argv[i + 1]; i++; }
    else kon.push(argv[i]);
  }
  const [paket, sahne, tListe, cikti] = kon;
  if (!paket || !sahne || !tListe || !cikti) {
    console.error("kullanım: sahne-kare.mjs <paket> <sahne> <t1,t2,…> <çıktı-dizini> [--tema]"
      + " [--olc] [--png 0|1] [--cdp-zaman 20] [--bekle 30]");
    process.exit(2);
  }
  const KOK = process.env.KALEM_KOK || path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
  const zaman = JSON.parse(fs.readFileSync(path.join(KOK, "projeler", paket, "zaman.json"), "utf8"));
  const S = zaman.sahneler.find((s) => s.klasor === sahne);
  if (!S) {
    console.error("sahne yok:", sahne, "·", zaman.sahneler.map((s) => s.klasor).join(" "));
    process.exit(2);
  }
  const fps = zaman.fps || 30, W = zaman.genislik || 1920, H = zaman.yukseklik || 1080;
  const tema = sec.tema || zaman.tema || "koyu", port = sec.port || "9333";
  const sunucu = sec.sunucu || "3012", bekle = +(sec.bekle || 30);
  const cdpZaman = +(sec["cdp-zaman"] || 20);
  const sayfa = S.motor === "HyperFrames" ? "/proje/index.html" : "/sayfa.html";
  const url = `http://127.0.0.1:${sunucu}/projeler/${paket}/sahneler/${sahne}${sayfa}` +
    `?canli=1&mesaj=1&tbas=${S.t_bas}` + (tema === "acik" ? "&tema=acik" : "");
  const zamanlar = tListe.split(",").map(Number).filter((x) => !Number.isNaN(x));
  if (sec.png !== "0" && sec.png !== "false") {
    fs.mkdirSync(cikti, { recursive: true });
  }

  const v = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();
  const ws = new WebSocket(v.webSocketDebuggerUrl);
  const { g, mesajIsle, temizle } = cdpGonderici(ws, { cdpZaman });
  const ISTEK = new Map();

  ws.onmessage = (e) => {
    const m = mesajIsle(e.data);
    if (sec.dbg && m.method === "Network.requestWillBeSent") {
      ISTEK.set(m.params.requestId, m.params.request.method + " " + m.params.request.url);
    }
    if (sec.dbg && /^Network\.(responseReceived|loadingFailed)$/.test(m.method || "")) {
      const p = m.params, u = ISTEK.get(p.requestId) || "";
      console.error(m.method.slice(8), p.response ? p.response.status : "", p.errorText || "",
        u.slice(-80));
    }
  };
  ws.onclose = () => {
    temizle();
  };

  ws.onopen = async () => {
    let ctx;
    try {
      ctx = (await g("Target.createBrowserContext")).browserContextId;
      // Ölçü (05.11): navigasyondan ÖNCE Emulation.setDeviceMetricsOverride ikinci isteği (script)
      // askıda bırakıyor; pencere boyutu hedef açılırken verilir, emülasyon sayfa hazır olunca gelir.
      const { targetId } = await g("Target.createTarget",
        { url: "about:blank", width: W, height: H, browserContextId: ctx });
      const { sessionId } = await g("Target.attachToTarget", { targetId, flatten: true });
      if (sec.dbg) await g("Network.enable", {}, sessionId);
      await g("Page.navigate", { url }, sessionId);
      const ev = async (js) => (await g("Runtime.evaluate",
        { expression: js, awaitPromise: true, returnByValue: true }, sessionId)).result.value;
      let t0 = Date.now();                        // ilk kare (hazir): sayaç kutusu belirene dek
      while (Date.now() - t0 < bekle * 1000 && !(await ev(SAYAC))) await uyku(100);
      if (!(await ev(SAYAC))) {
        if (sec.dbg) console.error("durum:", await ev(`document.readyState + " " + innerWidth + "x"
          + innerHeight + " " + [...document.body.children].map((e) => e.tagName).join(",")`));
        throw new Error("sahne hazır olmadı (sayaç yok): " + url);
      }
      if ((await ev("innerWidth + 'x' + innerHeight")) !== `${W}x${H}`) {
        await g("Emulation.setDeviceMetricsOverride",
          { width: W, height: H, deviceScaleFactor: 1, mobile: false }, sessionId);
        await uyku(300);
      }
      await kareleriIsle({
        g,
        ev,
        zamanlar,
        S,
        fps,
        bekle,
        cikti,
        sahne,
        sec,
        sessionId,
      });
    } catch (er) {
      console.error("HATA", er.message);
      process.exitCode = 1;
    }
    if (ctx) await g("Target.disposeBrowserContext", { browserContextId: ctx }).catch(() => {});
    ws.close();
  };
}

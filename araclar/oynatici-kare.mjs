#!/usr/bin/env node
// Oynatıcı prototipi ekran görüntüsü: sayfayı ortak başsız Chrome'da (CDP 9333) verilen pencere
// ölçüsünde açar, OYNATICI'yı istenen saniyeye sarar, afişi kaldırır, PNG alır (sahne-kare.mjs
// kalıbı; tarayıcı AÇMAZ, yalnız PNG yazar). Tasarım teslim kapısı §7 (masaüstü 1440, telefon 390).
//   node araclar/oynatici-kare.mjs <url> <GxY> <çıktı.png> [--t 25] [--tema acik|koyu]
//     [--dokunma 1] [--tam 1] [--menu bolum|hiz] [--port 9333] [--bekle 8] [--oynat 1]
//     [--basili <px>] [--bekleSn 0]
//   --dokunma 1: dokunmatik düzen (orta kontroller) · --tam 1: sayfanın tamamı (kaydırmalı)
//   --oynat 1: büyük oynat düğmesine gerçek tık (CDP Input = kullanıcı hareketi; ses açık oynar)
//   --basili <px>: oynarken sahne ortasına bas-tut (650 ms), <px> aşağı sürükle, basılıyken kare al
//     (turbo.js: 0 = yalnız 2× kapsülü; eşik 48–96 px → kilit) · --bekleSn: oynatma sonrası bekleme
import fs from "node:fs";
import path from "node:path";

const argv = process.argv.slice(2), sec = {}, kon = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i].startsWith("--")) { sec[argv[i].slice(2)] = argv[i + 1]; i++; }
  else kon.push(argv[i]);
}
const [url, olcu, cikti] = kon, [W, H] = String(olcu || "").split("x").map(Number);
if (!url || !W || !H || !cikti) {
  console.error("kullanım: oynatici-kare.mjs <url> <GxY> <çıktı.png> [--t] [--tema] [--dokunma 1]");
  process.exit(2);
}
const t = +(sec.t || 0), bekle = +(sec.bekle || 8), port = sec.port || "9333";
fs.mkdirSync(path.dirname(path.resolve(cikti)), { recursive: true });

const v = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();
const ws = new WebSocket(v.webSocketDebuggerUrl); let n = 0;
const bk = new Map();
const g = (method, params = {}, sessionId) => new Promise((ok, hata) => {
  const i = ++n; bk.set(i, { ok, hata });
  ws.send(JSON.stringify({ id: i, method, params, ...(sessionId ? { sessionId } : {}) }));
});
ws.onmessage = (e) => {
  const m = JSON.parse(e.data); if (!m.id || !bk.has(m.id)) return;
  const p = bk.get(m.id); bk.delete(m.id);
  m.error ? p.hata(new Error(m.error.message)) : p.ok(m.result);
};
const uyku = (ms) => new Promise((r) => setTimeout(r, ms));

ws.onopen = async () => {
  let ctx;
  try {
    ctx = (await g("Target.createBrowserContext")).browserContextId;
    const { targetId } = await g("Target.createTarget",
      { url: "about:blank", width: W, height: H, browserContextId: ctx });
    const { sessionId } = await g("Target.attachToTarget", { targetId, flatten: true });
    await g("Target.activateTarget", { targetId });
    await g("Emulation.setFocusEmulationEnabled", { enabled: true }, sessionId);
    await g("Page.navigate", { url }, sessionId);
    const ev = async (js) => (await g("Runtime.evaluate",
      { expression: js, awaitPromise: true, returnByValue: true }, sessionId)).result.value;
    let t0 = Date.now();
    const HAZIR = "!!(window.OYNATICI && OYNATICI.durum().hazir)";
    while (Date.now() - t0 < bekle * 1000 && !(await ev(HAZIR))) await uyku(100);
    if (!(await ev(HAZIR))) throw new Error("oynatıcı hazır olmadı: " + url);
    if ((await ev("innerWidth + 'x' + innerHeight")) !== `${W}x${H}`) {
      await g("Emulation.setDeviceMetricsOverride",
        { width: W, height: H, deviceScaleFactor: 1, mobile: sec.dokunma === "1" }, sessionId);
      await uyku(300);
    }
    if (sec.tema) await ev(`OYNATICI.tema(${JSON.stringify(sec.tema)}); true`);
    const sinif = (s, c) => `document.querySelector('${s}').classList.add('${c}'); true`;
    if (sec.dokunma === "1") await ev(sinif(".ko", "ko-dokunma"));
    await ev(`OYNATICI.git(${t}); true`);
    if (sec.afis !== "1") await ev(sinif(".ko-poster", "ko-yok"));
    // sahne karesi: o anın tamponu görünür (opacity 1) olana dek bekle
    const GORUNUR = "[...document.querySelectorAll('.ko-yaprak')]" +
      ".some((y) => y.style.opacity === '1')";
    t0 = Date.now();
    while (Date.now() - t0 < bekle * 1000 && !(await ev(GORUNUR))) await uyku(100);
    if (sec.menu) {
      const d = sec.menu === "hiz" ? "hizd" : "bold";
      await ev(`document.querySelector('.ko-${d}').click(); true`);
    }
    // fx/fy: öğe içindeki oran (0,5 = orta). Bas-tut sol çeyrekten: orta düğmelere değmesin.
    const orta = async (s, fx = 0.5, fy = 0.5) => JSON.parse(await ev(`(() => { const r = document
      .querySelector(${JSON.stringify(s)}).getBoundingClientRect(); return JSON.stringify(
      { x: r.left + r.width * ${fx}, y: r.top + r.height * ${fy} }); })()`));
    const fare = (type, x, y, ek = {}) => g("Input.dispatchMouseEvent",
      { type, x, y, button: "left", clickCount: 1, ...ek }, sessionId);
    if (sec.oynat === "1") {                        // gerçek kullanıcı hareketi: ses kilidi açılır
      await ev(sinif(".ko-poster", "ko-hazir")); await ev("document.querySelector('.ko-poster')" +
        ".classList.remove('ko-yok'); true");
      const p = await orta(".ko-buyuk");
      await fare("mousePressed", p.x, p.y); await fare("mouseReleased", p.x, p.y);
      await uyku(400 + 1000 * +(sec.bekleSn || 0));
    }
    if (sec.basili != null) {                       // bas-tut 2× (turbo.js) — basılıyken kare
      const p = await orta(".ko-pane", 0.25, 0.22);  // dokunmatik orta düğme bandının üstü
      await fare("mousePressed", p.x, p.y); await uyku(650);
      const px = +sec.basili; if (px) await fare("mouseMoved", p.x, p.y + px, { buttons: 1 });
      await uyku(250);
    }
    await uyku(sec.basili != null ? 0 : 600);
    const param = { format: "png" };
    if (sec.tam === "1") {
      const lm = await g("Page.getLayoutMetrics", {}, sessionId);
      const cs = lm.cssContentSize || lm.contentSize;
      param.captureBeyondViewport = true;
      param.clip = { x: 0, y: 0, width: W, height: Math.ceil(cs.height), scale: 1 };
    }
    const sc = await g("Page.captureScreenshot", param, sessionId);
    fs.writeFileSync(cikti, Buffer.from(sc.data, "base64"));
    const durum = await ev("JSON.stringify(OYNATICI.durum())");
    const hiz = await ev("document.querySelector('.ko audio').playbackRate");
    const turbo = await ev("(() => { const t = document.querySelector('.ko-turbo'); return t ?" +
      " (t.hidden ? 'gizli' : t.className + ' u=' + t.style.getPropertyValue('--u')) : '-'; })()");
    if (sec.basili != null) {
      const p = await orta(".ko-pane", 0.25, 0.22); await fare("mouseReleased", p.x, p.y);
    }
    console.log(JSON.stringify({ png: cikti, bayt: fs.statSync(cikti).size, olcu: `${W}x${H}`,
      durum, hiz, turbo }));
  } catch (er) { console.error("HATA", er.message); process.exitCode = 1; }
  if (ctx) await g("Target.disposeBrowserContext", { browserContextId: ctx }).catch(() => {});
  ws.close();
};

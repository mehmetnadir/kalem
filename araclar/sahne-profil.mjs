#!/usr/bin/env node
// Sahne sayfası yük profili: ortak başsız Chrome'da (CDP 9333) sahneyi editör
// protokolüyle (?canli=1&mesaj=1&tbas) açar, hazır olana dek CPU profili alır; hazır
// süresi (ms), 50 ms üstü uzun işler ve öz süresi en yüksek işlevler yazılır. Editör
// sonraki sahneyi 3 s önce aynı iş parçacığında yükler: burada görünen uzun iş =
// oynatmada takılma (05.11: svgYollari 1,7–2,5 s).
//   node araclar/sahne-profil.mjs <paket> <sahne-klasörü> [--tema acik|koyu] [--port 9333]
//     [--sunucu 3012] [--ust 14]
//   Kapı: uzunIs boş ve hazirMs < 500 olmalı. Tarayıcı AÇMAZ; 3012 + 9333 açık olmalı.
import fs from "node:fs";
import path from "node:path";

const argv = process.argv.slice(2), sec = {}, kon = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i].startsWith("--")) { sec[argv[i].slice(2)] = argv[i + 1]; i++; }
  else kon.push(argv[i]);
}
const [paket, sahne] = kon;
if (!paket || !sahne) {
  console.error("kullanım: sahne-profil.mjs <paket> <sahne> [--tema acik|koyu]");
  process.exit(2);
}
const KOK = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const zaman = JSON.parse(fs.readFileSync(path.join(KOK, "projeler", paket, "zaman.json"), "utf8"));
const S = zaman.sahneler.find((s) => s.klasor === sahne);
if (!S) {
  console.error("sahne yok:", sahne, "·", zaman.sahneler.map((s) => s.klasor).join(" "));
  process.exit(2);
}
const W = zaman.genislik || 1920, H = zaman.yukseklik || 1080;
const tema = sec.tema || zaman.tema || "koyu", port = sec.port || "9333";
const sunucu = sec.sunucu || "3012", ust = +(sec.ust || 14);
const sayfa = S.motor === "HyperFrames" ? "/proje/index.html" : "/sayfa.html";
const url = `http://127.0.0.1:${sunucu}/projeler/${paket}/sahneler/${sahne}${sayfa}` +
  `?canli=1&mesaj=1&tbas=${S.t_bas}` + (tema === "acik" ? "&tema=acik" : "");

const v = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();
const ws = new WebSocket(v.webSocketDebuggerUrl); let n = 0; const bk = new Map();
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
const SAYAC = `(() => { const d = [...document.body.children]
  .find((e) => /^\\d+ \\/ \\d+/.test(e.textContent || "")); return d ? d.textContent : ""; })()`;
const LT = `window.__lt = []; new PerformanceObserver((l) => { for (const e of l.getEntries())
  window.__lt.push([Math.round(e.startTime), Math.round(e.duration)]); })
  .observe({ type: "longtask" });`;

ws.onopen = async () => {
  let ctx;
  try {
    ctx = (await g("Target.createBrowserContext")).browserContextId;
    const { targetId } = await g("Target.createTarget",
      { url: "about:blank", width: W, height: H, browserContextId: ctx });
    const { sessionId } = await g("Target.attachToTarget", { targetId, flatten: true });
    await g("Page.enable", {}, sessionId);
    await g("Page.addScriptToEvaluateOnNewDocument", { source: LT }, sessionId);
    await g("Profiler.enable", {}, sessionId);
    await g("Profiler.setSamplingInterval", { interval: 500 }, sessionId);
    await g("Profiler.start", {}, sessionId);
    const t0 = Date.now();
    await g("Page.navigate", { url }, sessionId);
    const ev = async (js) => (await g("Runtime.evaluate",
      { expression: js, awaitPromise: true, returnByValue: true }, sessionId)).result.value;
    while (Date.now() - t0 < 20000 && !(await ev(SAYAC))) await uyku(50);
    const hazirMs = Date.now() - t0;
    if (!(await ev(SAYAC))) throw new Error("sahne hazır olmadı (sayaç yok): " + url);
    const lt = JSON.parse(await ev("JSON.stringify(window.__lt || [])"));
    const { profile } = await g("Profiler.stop", {}, sessionId);
    const node = new Map(); for (const nd of profile.nodes) node.set(nd.id, nd);
    const oz = new Map(); let toplam = 0;
    for (let i = 0; i < profile.samples.length; i++) {
      const nd = node.get(profile.samples[i]), dt = (profile.timeDeltas[i] || 0) / 1000;
      toplam += dt;
      const cf = nd.callFrame, ad = (cf.functionName || "(anonim)") + " " +
        (cf.url || "").split("/").slice(-1)[0] + ":" + (cf.lineNumber + 1);
      oz.set(ad, (oz.get(ad) || 0) + dt);
    }
    const top = [...oz.entries()].sort((a, b) => b[1] - a[1]).slice(0, ust);
    console.log(JSON.stringify({ sahne, motor: S.motor, hazirMs, uzunIs: lt,
      ornekMs: Math.round(toplam) }));
    for (const [a, d] of top) console.log(String(Math.round(d)).padStart(6), "ms ", a);
    if (lt.length) process.exitCode = 3;
  } catch (er) { console.error("HATA", er.message); process.exitCode = 1; }
  if (ctx) await g("Target.disposeBrowserContext", { browserContextId: ctx }).catch(() => {});
  ws.close();
};

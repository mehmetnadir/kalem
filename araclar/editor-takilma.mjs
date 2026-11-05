#!/usr/bin/env node
// Editör takılma ölçümü: ortak başsız Chrome'da (CDP 9333) onizle.html'i t0'da açar,
// oynatır, t1'e dek ana çerçevede rAF aralıklarını ve longtask girdilerini kaydeder. Ses
// başsızda engellenirse editör sessiz saatle ilerler; ölçüm aynıdır. Geçiş öncesi 3 s
// pencereyi kapsayan bir aralık ver (örn. sahne 3→4 geçişi 30,15 ise 26–30,8).
//   node araclar/editor-takilma.mjs <paket> <t0> <t1> [--surum ana-yatay]
//     [--tema acik|koyu] [--png <dosya>] [--port 9333] [--sunucu 3012]
//   Çıktı: tek JSON satırı; kapı: enBuyukAralik[1] ≤ 50 ms ve uzunIs boş (05.11 taban:
//   1433 ms → 33 ms, svgYollari Paper eğri örnekleyicisi). Tarayıcı AÇMAZ; 3012 + 9333
//   açık olmalı.
import fs from "node:fs";

const argv = process.argv.slice(2), sec = {}, kon = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i].startsWith("--")) { sec[argv[i].slice(2)] = argv[i + 1]; i++; }
  else kon.push(argv[i]);
}
const [paket, t0s, t1s] = kon;
if (!paket || !t0s || !t1s) {
  console.error("kullanım: editor-takilma.mjs <paket> <t0> <t1> [--surum] [--tema] [--png]");
  process.exit(2);
}
const t0 = +t0s, t1 = +t1s, surum = sec.surum || "ana-yatay", tema = sec.tema || "acik";
const port = sec.port || "9333", sunucu = sec.sunucu || "3012";
const url = `http://127.0.0.1:${sunucu}/p/${paket}/onizle.html?surum=${surum}` +
  `&tema=${tema}&t=${t0}`;
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
// Editör sayfasında kurulur: rAF aralıkları [t, ms] ve longtask [{d, t, at}]
// (t = editör saniyesi).
const KUR = `
window.__olc = { gaps: [], lt: [] };
new PerformanceObserver((l) => { for (const e of l.getEntries()) {
  const a = e.attribution && e.attribution[0];
  window.__olc.lt.push({ d: Math.round(e.duration), t: +t.toFixed(2),
    at: a ? a.containerType + ":" + (a.containerSrc || "").split("/").slice(-2).join("/")
      .slice(0, 60) : "" });
} }).observe({ type: "longtask", buffered: false });
let __son = performance.now();
(function __tick(ms) { window.__olc.gaps.push([+t.toFixed(2), Math.round(ms - __son)]);
  __son = ms; requestAnimationFrame(__tick); })(performance.now());
true`;
const HAZIR = "typeof panes !== 'undefined' && panes[0] && " +
  "panes[0].slot.some((s) => s.hazir && s.goster)";
const SLOT = "panes[0].slot.map((s) => s.no + ':' + s.hazir + ':' + s.goster)" +
  ".join(' ')";

ws.onopen = async () => {
  let ctx;
  try {
    ctx = (await g("Target.createBrowserContext")).browserContextId;
    const { targetId } = await g("Target.createTarget",
      { url: "about:blank", width: 1600, height: 900, browserContextId: ctx });
    const { sessionId } = await g("Target.attachToTarget", { targetId, flatten: true });
    await g("Page.navigate", { url }, sessionId);
    const ev = async (js) => (await g("Runtime.evaluate",
      { expression: js, awaitPromise: true, returnByValue: true }, sessionId)).result.value;
    let b = Date.now();
    while (Date.now() - b < 15000 && !(await ev(HAZIR))) await uyku(100);
    if (!(await ev(HAZIR))) throw new Error("editör hazır olmadı: " + url);
    await ev(KUR);
    await ev("oyna(); true");
    b = Date.now();
    while (Date.now() - b < (t1 - t0 + 6) * 1000 && (await ev("t")) < t1) await uyku(100);
    const sessiz = await ev("sessiz"), tt = await ev("t"), slot = await ev(SLOT);
    if (sec.png) {
      const sc = await g("Page.captureScreenshot", { format: "png" }, sessionId);
      fs.writeFileSync(sec.png, Buffer.from(sc.data, "base64"));
    }
    await ev("dur(); true");
    const O = JSON.parse(await ev("JSON.stringify(window.__olc)"));
    const enb = O.gaps.reduce((a, x) => (x[1] > a[1] ? x : a), [0, 0]);
    console.log(JSON.stringify({ paket, surum, tema, t0, t1: +tt.toFixed(2), sessiz,
      kare: O.gaps.length, enBuyukAralik: enb, aralik50: O.gaps.filter((x) => x[1] >= 50),
      uzunIs: O.lt, slot }));
    if (enb[1] > 50 || O.lt.length) process.exitCode = 3;
  } catch (er) { console.error("HATA", er.message); process.exitCode = 1; }
  if (ctx) await g("Target.disposeBrowserContext", { browserContextId: ctx }).catch(() => {});
  ws.close();
};

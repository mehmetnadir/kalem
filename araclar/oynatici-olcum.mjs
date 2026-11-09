#!/usr/bin/env node
// Oynatıcı yük ölçümü (izleyen cihaza binen yük): ortak başsız Chrome'da (CDP 9333) sayfayı açar,
// büyük oynat düğmesine gerçek tık atar (CDP Input = kullanıcı hareketi, ses açık), N sn oynatırken
// her saniye Performance.getMetrics (ana iş parçacığı meşguliyeti, betik / yerleşim / stil payı, JS
// yığını, DOM düğümü), rAF kare hızı, uzun işler (≥ 50 ms) ve ağ aktarımını (tür bazında) toplar.
// Sahne iframe'leri aynı köken → aynı süreç: sayılar bütün sahneleri kapsar. --cpu 4: CPU kısma
// (orta sınıf telefon yaklaşımı; M1 Max'te 4× ≈ 2020 orta sınıf Android, kesin eşleme DEĞİL).
//   node araclar/oynatici-olcum.mjs <url> [--olcu 1440x900] [--sure 30] [--cpu 1] [--dokunma 1]
//     [--port 9333] [--bekle 10] [--json çıktı.json]
//   Kapı önerisi (PRD §7): ilk kare ≤ 2000 ms · meşguliyet ort. ≤ %30 (cpu 4) · uzun iş ≤ 2.
import fs from "node:fs";

const argv = process.argv.slice(2), sec = {}, kon = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i].startsWith("--")) { sec[argv[i].slice(2)] = argv[i + 1]; i++; }
  else kon.push(argv[i]);
}
const [url] = kon, [W, H] = String(sec.olcu || "1440x900").split("x").map(Number);
if (!url || !W || !H) {
  console.error("kullanım: oynatici-olcum.mjs <url> [--olcu GxY] [--sure 30] [--cpu 1|4|6]");
  process.exit(2);
}
const sure = +(sec.sure || 30), cpu = +(sec.cpu || 1), bekle = +(sec.bekle || 10);
const port = sec.port || "9333";

const v = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();
const ws = new WebSocket(v.webSocketDebuggerUrl); let n = 0;
const bk = new Map(), istek = new Map(), ag = {}; let sid = "";
const g = (method, params = {}, sessionId) => new Promise((ok, hata) => {
  const i = ++n; bk.set(i, { ok, hata });
  ws.send(JSON.stringify({ id: i, method, params, ...(sessionId ? { sessionId } : {}) }));
});
ws.onmessage = (e) => {
  const m = JSON.parse(e.data);
  if (m.id) {
    if (!bk.has(m.id)) return;
    const p = bk.get(m.id); bk.delete(m.id);
    return m.error ? p.hata(new Error(m.error.message)) : p.ok(m.result);
  }
  if (m.sessionId !== sid) return;
  if (m.method === "Network.responseReceived") {
    const r = m.params.response;
    istek.set(m.params.requestId, { tur: m.params.type, url: r.url,
      onbellek: !!(r.fromDiskCache || r.fromPrefetchCache || r.fromServiceWorker) });
  } else if (m.method === "Network.loadingFinished") {
    const r = istek.get(m.params.requestId); if (!r) return;
    const tur = /\.(wav|m4a|mp3|ogg)(\?|$)/.test(r.url) ? "Ses" : r.tur;
    const a = ag[tur] || (ag[tur] = { bayt: 0, istek: 0, onbellek: 0 });
    a.bayt += m.params.encodedDataLength; a.istek++; if (r.onbellek) a.onbellek++;
  }
};
const uyku = (ms) => new Promise((r) => setTimeout(r, ms));
const EK = `window.__lt = []; new PerformanceObserver((l) => { for (const e of l.getEntries())
  window.__lt.push([Math.round(e.startTime), Math.round(e.duration)]); })
  .observe({ type: "longtask" });
  window.__frN = 0; (function k() { window.__frN++; requestAnimationFrame(k); })();`;
const mb = (b) => Math.round(b / 1048576 * 100) / 100;

ws.onopen = async () => {
  let ctx;
  try {
    ctx = (await g("Target.createBrowserContext")).browserContextId;
    const { targetId } = await g("Target.createTarget",
      { url: "about:blank", width: W, height: H, browserContextId: ctx });
    sid = (await g("Target.attachToTarget", { targetId, flatten: true })).sessionId;
    await g("Target.activateTarget", { targetId });
    await g("Emulation.setFocusEmulationEnabled", { enabled: true }, sid);
    await g("Page.enable", {}, sid); await g("Network.enable", {}, sid);
    await g("Performance.enable", {}, sid);
    await g("Page.addScriptToEvaluateOnNewDocument", { source: EK }, sid);
    if (sec.dokunma === "1") {
      await g("Emulation.setDeviceMetricsOverride",
        { width: W, height: H, deviceScaleFactor: 2, mobile: true }, sid);
      await g("Emulation.setTouchEmulationEnabled", { enabled: true }, sid);
    }
    if (cpu > 1) await g("Emulation.setCPUThrottlingRate", { rate: cpu }, sid);
    const ev = async (js) => (await g("Runtime.evaluate",
      { expression: js, awaitPromise: true, returnByValue: true }, sid)).result.value;
    const olc = async () => {
      const r = {}, { metrics } = await g("Performance.getMetrics", {}, sid);
      for (const m of metrics) r[m.name] = m.value;
      return r;
    };
    const t0 = Date.now();
    await g("Page.navigate", { url }, sid);
    const HAZIR = "!!(window.OYNATICI && OYNATICI.durum().hazir)";
    while (Date.now() - t0 < bekle * 1000 && !(await ev(HAZIR))) await uyku(50);
    const ilkKareMs = Date.now() - t0;
    if (!(await ev(HAZIR))) throw new Error("oynatıcı hazır olmadı: " + url);
    const yuklemeAg = JSON.parse(JSON.stringify(ag));
    // gerçek tık: büyük oynat düğmesinin ortası
    const p = JSON.parse(await ev(`(() => { const r = document.querySelector('.ko-buyuk')
      .getBoundingClientRect(); return JSON.stringify({ x: r.left + r.width / 2,
      y: r.top + r.height / 2 }); })()`));
    for (const type of ["mousePressed", "mouseReleased"]) {
      await g("Input.dispatchMouseEvent",
        { type, x: p.x, y: p.y, button: "left", clickCount: 1 }, sid);
    }
    await uyku(600);
    let ses = "açık";
    if (!(await ev("OYNATICI.durum().oynuyor"))) {        // otomatik oynatma reddi: sessiz yedek
      await ev("document.querySelector('.ko audio').muted = true; OYNATICI.oyna(); true");
      await uyku(600); ses = "sessiz yedek";
      if (!(await ev("OYNATICI.durum().oynuyor"))) throw new Error("oynatma başlamadı");
    }
    const ltBas = JSON.parse(await ev("JSON.stringify(window.__lt)")).length;
    let onceki = await olc(), onFr = await ev("window.__frN");
    const satir = [];
    for (let k = 0; k < sure; k++) {
      await uyku(1000);
      const m = await olc(), fr = await ev("window.__frN"), dt = m.Timestamp - onceki.Timestamp;
      const yuzde = (a) => Math.round((m[a] - onceki[a]) / dt * 100);
      // görünürlük + ses durumu: ortak tarayıcıda başka hedef öne geçerse rAF durur, ses bekler
      const sd = JSON.parse(await ev(`(() => { const a = document.querySelector('.ko audio');
        return JSON.stringify({ t: OYNATICI.durum().t, gor: document.visibilityState[0],
          ses: a.paused ? 'durdu' : a.readyState < 3 ? 'bekliyor' : 'ok' }); })()`));
      satir.push({ t: Math.round(sd.t), mesgul: yuzde("TaskDuration"),
        betik: yuzde("ScriptDuration"), yerlesim: yuzde("LayoutDuration"),
        stil: yuzde("RecalcStyleDuration"), fps: Math.round((fr - onFr) / dt),
        yiginMB: mb(m.JSHeapUsedSize), dugum: m.Nodes, belge: m.Documents, gor: sd.gor,
        ses: sd.ses });
      onceki = m; onFr = fr;
      if (!(await ev("OYNATICI.durum().oynuyor"))) break;              // bitti ya da durdu
    }
    const lt = JSON.parse(await ev("JSON.stringify(window.__lt)")).slice(ltBas);
    const ort = (a) => Math.round(satir.reduce((s, r) => s + r[a], 0) / Math.max(1, satir.length));
    const ozet = {
      url, olcu: `${W}x${H}`, cpu, ses, ilkKareMs, saniye: satir.length,
      mesgulOrt: ort("mesgul"), mesgulEnYuksek: Math.max(...satir.map((r) => r.mesgul)),
      betikOrt: ort("betik"), yerlesimOrt: ort("yerlesim"), stilOrt: ort("stil"),
      fpsOrt: ort("fps"), fpsEnDusuk: Math.min(...satir.map((r) => r.fps)),
      yiginMBSon: satir.at(-1)?.yiginMB, dugumSon: satir.at(-1)?.dugum,
      uzunIs: lt.length, uzunIsEnUzunMs: lt.length ? Math.max(...lt.map((x) => x[1])) : 0,
      agYuklemeMB: mb(Object.values(yuklemeAg).reduce((s, a) => s + a.bayt, 0)),
      agToplamMB: mb(Object.values(ag).reduce((s, a) => s + a.bayt, 0)),
      agTur: Object.fromEntries(Object.entries(ag)
        .map(([k, a]) => [k, { MB: mb(a.bayt), istek: a.istek, onbellek: a.onbellek }])),
      gizliSn: satir.filter((r) => r.gor !== "v").length,
      sesBekledi: satir.filter((r) => r.ses !== "ok").length,
      durum: JSON.parse(await ev("JSON.stringify(OYNATICI.durum())")),
    };
    console.log(JSON.stringify(ozet, null, 1));
    console.log("\n  sn    t  meşgul%  betik%  yerl%  stil%  fps  yığınMB  düğüm  gör  ses");
    satir.forEach((r, i) => console.log(String(i + 1).padStart(4), String(r.t).padStart(4),
      String(r.mesgul).padStart(8), String(r.betik).padStart(7), String(r.yerlesim).padStart(6),
      String(r.stil).padStart(6), String(r.fps).padStart(4), String(r.yiginMB).padStart(8),
      String(r.dugum).padStart(6), String(r.gor).padStart(4), " " + r.ses));
    if (lt.length) console.log("uzun işler [başlangıç ms, süre ms]:", JSON.stringify(lt));
    if (sec.json) fs.writeFileSync(sec.json, JSON.stringify({ ozet, satir, uzunIs: lt }, null, 1));
  } catch (er) { console.error("HATA", er.message); process.exitCode = 1; }
  if (ctx) await g("Target.disposeBrowserContext", { browserContextId: ctx }).catch(() => {});
  ws.close();
};

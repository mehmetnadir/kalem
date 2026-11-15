#!/usr/bin/env node
// Başsız kare (YouTube ortak parçaları): sayfayı ortak Chrome'da (CDP 41333, qa-yerel ile aynı) ayrı tarayıcı
// bağlamında açar, window.__hazir bekler (yazı tipi + logo), her t için window.__seek(t) + PNG alır.
//   node ortak/youtube/kare.mjs <url> <t>=<png> [<t>=<png> …] [--boyut 1920x1080] [--seffaf] [--olc "<js>"]
//     [--port 41333] [--bekle 30]
//   t = sahne saniyesi; "-" = arama yok (durağan sayfa). --seffaf: zemin rengi şeffaf (RGBA PNG).
//   --olc: her karede koşan JS; sonucu satırın "olc" alanına girer. Çıktı: kare başına bir JSON satırı.
// Tarayıcı AÇMAZ, mp4 üretmez; yalnız PNG yazar.
import fs from "node:fs";
import path from "node:path";

const uyku = (ms) => new Promise((r) => setTimeout(r, ms));
const arg = process.argv.slice(2);
const sec = {}, isler = [];
let url = null;
for (let i = 0; i < arg.length; i++) {
  const a = arg[i];
  if (a === "--seffaf") sec.seffaf = true;
  else if (a.startsWith("--")) sec[a.slice(2)] = arg[++i];
  else if (!url) url = a;
  else {
    const k = a.indexOf("=");
    isler.push({ t: a.slice(0, k), png: a.slice(k + 1) });
  }
}
if (!url || !isler.length) {
  console.error("kullanım: kare.mjs <url> <t>=<png> […] [--boyut WxH] [--seffaf] [--olc js] [--port 41333]");
  process.exit(2);
}
const [W, H] = (sec.boyut || "1920x1080").split("x").map(Number);
const port = sec.port || "41333", bekle = +(sec.bekle || 30);

const v = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();
const ws = new WebSocket(v.webSocketDebuggerUrl);
let n = 0;
const bk = new Map();
const g = (method, params = {}, sessionId) => new Promise((ok, hata) => {
  const i = ++n;
  const z = setTimeout(() => { bk.delete(i); hata(new Error("CDP zaman aşımı: " + method)); }, 30000);
  bk.set(i, { ok: (r) => { clearTimeout(z); ok(r); }, hata: (e) => { clearTimeout(z); hata(e); } });
  ws.send(JSON.stringify({ id: i, method, params, ...(sessionId ? { sessionId } : {}) }));
});
ws.onmessage = (e) => {
  const m = JSON.parse(typeof e.data === "string" ? e.data : e.data.toString());
  if (!m.id || !bk.has(m.id)) return;
  const p = bk.get(m.id);
  bk.delete(m.id);
  m.error ? p.hata(new Error(m.error.message)) : p.ok(m.result);
};
await new Promise((ok) => { ws.onopen = ok; });

let ctx;
try {
  ctx = (await g("Target.createBrowserContext")).browserContextId;
  const { targetId } = await g("Target.createTarget", { url: "about:blank", width: W, height: H, browserContextId: ctx });
  const { sessionId } = await g("Target.attachToTarget", { targetId, flatten: true });
  const ev = async (js) => (await g("Runtime.evaluate",
    { expression: js, awaitPromise: true, returnByValue: true }, sessionId)).result.value;
  if (sec.seffaf) {
    await g("Emulation.setDefaultBackgroundColorOverride", { color: { r: 0, g: 0, b: 0, a: 0 } }, sessionId);
  }
  await g("Page.navigate", { url }, sessionId);
  const t0 = Date.now();
  while (Date.now() - t0 < bekle * 1000 && !(await ev("window.__hazir === true").catch(() => false))) await uyku(100);
  if (!(await ev("window.__hazir === true"))) throw new Error("sayfa hazır olmadı: " + url);
  if ((await ev("innerWidth + 'x' + innerHeight")) !== `${W}x${H}`) {
    await g("Emulation.setDeviceMetricsOverride", { width: W, height: H, deviceScaleFactor: 1, mobile: false }, sessionId);
    await uyku(300);
  }
  for (const is of isler) {
    if (is.t !== "-") await ev(`window.__seek(${Number(is.t)}); true`);
    await ev("new Promise((ok) => requestAnimationFrame(() => requestAnimationFrame(() => ok(true))))");
    await uyku(120);
    fs.mkdirSync(path.dirname(path.resolve(is.png)), { recursive: true });
    const sc = await g("Page.captureScreenshot",
      { format: "png", clip: { x: 0, y: 0, width: W, height: H, scale: 1 } }, sessionId);
    fs.writeFileSync(is.png, Buffer.from(sc.data, "base64"));
    const satir = { t: is.t, png: is.png, bayt: fs.statSync(is.png).size };
    if (sec.olc) satir.olc = await ev(sec.olc);
    console.log(JSON.stringify(satir));
  }
} catch (er) {
  console.error("HATA", er.message);
  process.exitCode = 1;
}
if (ctx) await g("Target.disposeBrowserContext", { browserContextId: ctx }).catch(() => {});
ws.close();

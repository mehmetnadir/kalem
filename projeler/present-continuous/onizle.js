// Present Continuous — kurgu editörü. Tek saat: <audio>.
// Sahneler iframe'de ?canli=1&mesaj=1 ile yalnız mesaj zamanıyla çizer.
"use strict";
var YOL = "/projeler/present-continuous/", FPS = 30, GECIS = 0.4, ONYUKLE = 3, ET = 104;
var RENK = ["var(--s0)", "var(--s1)", "var(--s2)", "var(--s3)", "var(--s4)", "var(--s5)"];
var BOLUM = ["Giriş", "Hook", "Example 1 / 3", "Example 2 / 3", "Example 3 / 3", "Question"];
var NTUR = { cizim: "var(--n-cizim)", metin: "var(--n-metin)", kart: "var(--n-kart)", isaret: "var(--n-isaret)" };
var $ = function (s) { return document.querySelector(s); };
var au = $("#au"), zk = $("#zk"), zi = $("#zi");
var D = null, S = [], T = 94.33, t = 0, calma = "dur", hiz = 1, zoom = 1, TEMA = "koyu", H = {};
var sessiz = false, panes = [], yan = false, sonMs = 0, wave = null, sonOlay = -1;

function e(tag, cls, html, ust) {
  var n = document.createElement(tag); if (cls) n.className = cls; if (html != null) n.innerHTML = html;
  if (ust) ust.appendChild(n); return n;
}
function pad(n, k) { n = String(n); while (n.length < (k || 2)) n = "0" + n; return n; }
function sn(x) { return x.toFixed(2).replace(".", ","); }
function kareNo(x) { return Math.floor(x * FPS + 1e-4); }
function mmss(x) {
  var f = Math.max(0, kareNo(x)), s = Math.floor(f / FPS);
  return pad(Math.floor(s / 60)) + ":" + pad(s % 60) + "." + pad(f % FPS);
}
function kisaSn(x) { return Math.floor(x / 60) + ":" + pad(Math.floor(x % 60)); }

// ---------- Veri sözleşmesi (dijital-anlatim paketi için yalnız bu bölüm değişir) ----------
function getJ(yol) { return fetch(yol).then(function (r) { if (!r.ok) throw new Error(yol + " " + r.status);
  return r.json(); }); }
// zaman.json sahneleri: klasor, motor, kare, t_bas, t_son
function zamanYukle() { return getJ("zaman.json"); }
function sozcukYukle() {                                                  // küresel sözcük zamanları → cümleler
  return Promise.all([getJ("ortak/anlatim/sozcukler.json"),
    fetch("ortak/anlatim/METIN.md").then(function (r) { return r.text(); })])
    .then(function (a) {
      var konusan = {};
      a[1].split("\n").forEach(function (l) {
        var m = l.match(/^\|\s*(\d+)\s*\|[^|]*\|[^|]*\|\s*([^|]+?)\s*\|/); if (m) konusan[+m[1]] = m[2];
      });
      var g = {};
      a[0].forEach(function (w) {
        var c = g[w.cumle] || (g[w.cumle] = { no: w.cumle, t0: 1e9, t1: 0, sozcuk: [],
          konusan: konusan[w.cumle] || "öğretmen" });
        c.t0 = Math.min(c.t0, w.t0); c.t1 = Math.max(c.t1, w.t1); c.sozcuk.push(w);
      });
      return Object.keys(g).map(function (k) { return g[k]; }).sort(function (x, y) { return x.t0 - y.t0; });
    });
}
function olayYukle(z) {                                                   // yerel kare → küresel sn
  return Promise.all(z.sahneler.map(function (s, i) {
    return getJ("sahneler/" + s.klasor + "/olaylar.json").then(function (L) {
      return L.map(function (o) { return { t: s.t_bas + o.kare / z.fps, tur: o.tur, guc: o.guc, sahne: i,
        kare: o.kare }; });
    }).catch(function () { return []; });
  })).then(function (a) { return [].concat.apply([], a).sort(function (x, y) { return x.t - y.t; }); });
}
function nesneYukle(z) {                                                  // nesneler.json: [{ad,t0,t1,tur}] küresel sn
  return Promise.all(z.sahneler.map(function (s, i) {
    return getJ("sahneler/" + s.klasor + "/nesneler.json").then(function (L) {
      return L.map(function (o) { return { ad: o.ad, t0: o.t0, t1: o.t1, tur: o.tur, sahne: i }; });
    }).catch(function () { return []; });
  })).then(function (a) { return [].concat.apply([], a); });
}
function veriYukle() {
  return zamanYukle().then(function (z) {
    return Promise.all([sozcukYukle(), olayYukle(z), nesneYukle(z), getJ("sahneler/" + z.sahneler[5].klasor
      + "/zamanlar.json")
      .catch(function () { return {}; })]).then(function (a) {
      return { z: z, cumle: a[0], olay: a[1], nesne: a[2], form: a[3].form || null };
    });
  });
}

// ---------- Sahne penceresi: her pencere kendi çift iframe tamponu, teması ve sürümü ----------
function sahneNo(p, x) { var L = p.S; for (var i = L.length - 1; i >= 0; i--) if (x >= L[i].t_bas) return i; return 0; }
function url(p, i) {
  var s = p.S[i];
  return p.yol + "sahneler/" + s.klasor + (s.motor === "HyperFrames" ? "/proje/index.html" : "/sayfa.html") +
    "?canli=1&mesaj=1&tbas=" + s.t_bas + (p.tema === "acik" ? "&tema=acik" : "");
}
function slotYukle(p, s, i) { s.no = i; s.hazir = false; s.goster = false; s.sonT = null; s.f.src = url(p, i); }
function slotBul(p, i, goster) {
  for (var k = 0; k < p.slot.length; k++) if (p.slot[k].no === i && (!goster || p.slot[k].goster)) return p.slot[k];
  return null;
}
function sahneYonet(p, x) {
  var i = sahneNo(p, x), cur = slotBul(p, i, true), L = p.S, slot = p.slot;
  if (cur) p.gosterilen = cur.idx;
  else if (!slotBul(p, i, false)) slotYukle(p, slot[p.gosterilen === 0 ? 1 : 0], i);
  if (cur && i + 1 < L.length && x >= L[i + 1].t_bas - ONYUKLE && !slotBul(p, i + 1, false)) {
    slotYukle(p, slot[1 - cur.idx], i + 1);
  }
  var onceki = (cur && i > 0 && x - L[i].t_bas < GECIS) ? slotBul(p, i - 1, true) : null;
  slot.forEach(function (s) {
    var op = 0, z = 0;
    if (cur) {
      if (s === cur) { z = 2; op = 1; if (onceki) { var u = Math.min(1, (x - L[i].t_bas) / GECIS);
        op = u * u * (3 - 2 * u); } }
      else if (s === onceki) { z = 1; op = 1; }
    } else if (s.idx === p.gosterilen) { z = 2; op = 1; }
    if (s.op !== op) { s.f.style.opacity = op; s.op = op; }
    if (s.z !== z) { s.f.style.zIndex = z; s.z = z; }
    if (s.hazir && s.sonT !== x) { try { s.f.contentWindow.postMessage({ tip: "zaman", t: x }, "*");
      } catch (er) {} s.sonT = x; }
  });
  if (p.k === 0) $("#bekle").style.display = p.gosterilen >= 0 ? "none" : "flex";
  return { i: i, cur: !!cur, sonraki: i + 1 < L.length ? slotBul(p, i + 1, true) : null };
}
window.addEventListener("message", function (ev) {
  var d = ev.data; if (!d || d.tip !== "hazir") return;
  panes.forEach(function (p) {
    p.slot.forEach(function (s) {
      if (s.f.contentWindow !== ev.source) return;
      s.hazir = true; s.sonT = null; if (d.zamanli) s.goster = true;
      try { s.f.contentWindow.postMessage({ tip: "tema", ad: p.tema }, "*"); } catch (er) {}
    });
  });
});
function olc() {
  var o = $("#orta"), n = yan ? 2 : 1, ara = yan ? 8 : 0, ust = yan ? 44 : 0, sh = $("#sahne");
  var w = Math.min((o.clientWidth - 24 - ara) / n, (o.clientHeight - 24 - ust) * 16 / 9);
  sh.style.width = (w * n + ara) + "px"; sh.style.height = (w * 9 / 16) + "px";
  panes.forEach(function (p, k) {
    p.el.style.display = k < n ? "block" : "none"; p.el.style.left = (k * (w + ara)) + "px";
    p.el.style.width = w + "px"; p.el.style.height = (w * 9 / 16) + "px";
    p.slot.forEach(function (s) { s.f.style.transform = "scale(" + (w / 1920) + ")"; });
  });
}
// pencerenin sahne kaynağını değiştirir, tamponları sıfırlar
function paneKaynak(p, yol, L) {
  p.yol = yol; p.S = L; p.gosterilen = -1;
  p.slot.forEach(function (s) {
    s.no = -1; s.hazir = false; s.goster = false; s.sonT = null; s.op = -1; s.z = -1; s.f.style.opacity = 0;
    s.f.src = "about:blank";
  });
}
function paneTema(p) {
  p.el.classList.toggle("acik", p.tema === "acik");
  p.slot.forEach(function (s) {
    try { s.f.contentWindow.postMessage({ tip: "tema", ad: p.tema }, "*"); } catch (er) {}
  });
}
function surumTaban(a) { return a.split("?")[0].replace(/[^\/]*$/, ""); }
function paneAyarla(p, v) {                            // v: "t:koyu" | "t:acik" | "s:<sürüm kimliği>"
  if (v.indexOf("t:") === 0) {
    p.tema = v.slice(2);
    if (p.surum) { p.surum = ""; paneKaynak(p, YOL, S); }
    paneTema(p); return;
  }
  var kid = v.slice(2), s = surumBul(kid), taban = s ? surumTaban(surumAdres(s)) : "";
  getJ(taban + "zaman.json").then(function (z) { p.surum = kid; paneKaynak(p, taban, z.sahneler); paneTema(p); })
    .catch(function () { durumMesaj("Sürümün sahneleri yüklenemedi"); paneSecenek(); });
}
function yanSec(a) {
  if (a === yan) return;
  if (a) zoomSec(1);
  yan = a; $("#yyb").classList.toggle("on", a); $("#yy").hidden = !a; document.body.classList.toggle("yan", a);
  if (a) {
    var p1 = panes[1]; p1.tema = panes[0].tema === "koyu" ? "acik" : "koyu"; p1.surum = "";
    paneKaynak(p1, YOL, S); paneTema(p1);
  }
  paneSecenek(); olc();
}
function paneSecenek() {
  [0, 1].forEach(function (k) {
    var sel = $("#ys" + k), p = panes[k]; if (!sel || !p) return;
    var o = "<option value='t:koyu'>Koyu tema</option><option value='t:acik'>Açık tema</option>";
    SU.forEach(function (s) {
      if (!surumAdres(s) || s.kimlik === SK) return;
      o += "<option value='s:" + ec(s.kimlik) + "'>Sürüm: " + ec(s.ad || s.kimlik) + "</option>";
    });
    sel.innerHTML = o; sel.value = p.surum ? "s:" + p.surum : "t:" + p.tema;
  });
}

// ---------- Oynatma ----------
function git(x) {
  t = Math.max(0, Math.min(T - 1 / FPS, x));
  try { au.currentTime = t; } catch (er) {}
  gorunurYap();
}
function gorunurYap() {                  // zaman çizgisi playhead'e kayar (yakınlaştırılmışsa)
  var px = t * pps(), a = zk.scrollLeft, b = a + zk.clientWidth - ET;
  if (px < a || px > b) zk.scrollLeft = Math.max(0, px - (zk.clientWidth - ET) * 0.3);
}
function adim(k) { git((Math.floor(t * FPS + 1e-4) + k) / FPS + 0.0001); }
function oyna() {
  if (calma === "ileri") return dur();
  if (t >= T - 0.1) git(0);
  calma = "ileri"; sessiz = false; au.playbackRate = hiz; au.currentTime = t;
  au.play().catch(function () { sessiz = true; durumMesaj("Tarayıcı sesi engelledi: sessiz oynatma"); });
}
function dur() { if (calma === "geri") au.currentTime = t; calma = "dur"; au.pause(); }
function geriOyna() { dur(); calma = "geri"; }
function hizSec(h) {
  hiz = h; au.playbackRate = h;
  document.querySelectorAll("#hiz button").forEach(function (b) { b.classList.toggle("on", +b.dataset.h === h); });
}
function temaSec(a) {
  TEMA = a; document.body.classList.toggle("acik", a === "acik");
  document.querySelectorAll("#tema button").forEach(function (b) { b.classList.toggle("on", b.dataset.t === a); });
  if (panes[0]) { panes[0].tema = a; paneTema(panes[0]); paneSecenek(); }
  try {
    var q = new URLSearchParams(location.search);
    if (a === "acik") q.set("tema", "acik"); else q.delete("tema");
    history.replaceState(null, "", q.toString() ? "?" + q.toString() : location.pathname);
  } catch (er) {}
}
function karePng() {
  var c = slotBul(panes[0], sahneNo(panes[0], t), true);
  if (!c) return durumMesaj("Sahne henüz hazır değil");
  if (panes[0].S[c.no].motor === "HyperFrames") return durumMesaj("HyperFrames sahneleri kare PNG vermez");
  c.f.contentWindow.postMessage({ tip: "kare" }, "*");
}
var mesajT = 0, mesajM = "";
function durumMesaj(m) { mesajM = m; mesajT = performance.now() + 3000; }

// ---------- Zaman çizgisi ----------
function pps() { return W() / T; }
function W() { return Math.max(300, (zk.clientWidth - ET)) * zoom; }
function yuzde(x) { return (x / T * 100) + "%"; }
function satir(ad, h, cls) {
  var s = e("div", "sat " + (cls || ""), null, zi); s.style.height = h + "px";
  var a = e("div", "et", ad, s), ic = e("div", "ic", null, s); return { et: a, ic: ic, sat: s };
}
function blok(ic, a, b, cls, html, ip) {
  var n = e("div", cls, html, ic); n.style.left = yuzde(a); n.style.width = yuzde(b - a);
  if (ip) n.dataset.ip = ip; return n;
}
function zamanCizgisiKur() {
  zi.innerHTML = "";
  var r = satir("", 22, "cetvel"); H.cetvel = r.ic;
  r.et.innerHTML = "<button data-z='-' title='Uzaklaştır'>−</button><span id='zoomE'>1×</span>" +
    "<button data-z='+' title='Yakınlaştır'>+</button>";
  H.bas = e("div", null, null, r.ic); H.bas.id = "bas";
  // bölüm
  var b = satir("Bölüm", 18), ad = BOLUM.slice(), form = D.form || S[5].t_bas + 3.91;
  H.bolum = [];
  S.forEach(function (s, i) {
    var son = i === 5 ? form : s.t_son;
    H.bolum.push(blok(b.ic, s.t_bas, son, "b bl", ad[i], ad[i]));
    H.bolum[i]._a = s.t_bas; H.bolum[i]._b = son;
  });
  H.bolum.push(blok(b.ic, form, S[5].t_son, "b bl", "Form", "Form")); H.bolum[6]._a = form; H.bolum[6]._b = S[5].t_son;
  // sahne
  var sr = satir("Sahne", 26); H.sbl = [];
  S.forEach(function (s, i) {
    var n = blok(sr.ic, s.t_bas, s.t_son, "b", pad(s.no) + " " + s.klasor.slice(3), s.klasor + " · " + s.motor);
    n.style.setProperty("--r", RENK[i]); n.onclick = function (ev) { ev.stopPropagation(); git(s.t_bas); };
      H.sbl.push(n);
  });
  // ses dalgası
  var w = satir("Ses dalgası", 56); H.dalga = e("canvas", null, null, w.ic); H.dalga.id = "dalga";
  // cümle
  var c = satir("Cümle", 36); H.cm = [];
  D.cumle.forEach(function (cu, i) {
    var n = blok(c.ic, cu.t0, cu.t1, "cm" + (cu.konusan === "öğrenci" ? " og" : ""), cu.no + " · " + cu.konusan,
      "Cümle " + cu.no + " · " + cu.konusan + " · " + sn(cu.t0) + "–" + sn(cu.t1) + " sn");
    n.onclick = function (ev) { ev.stopPropagation(); git(cu.t0); };
    n._w = cu.sozcuk.map(function (sz) {
      var k = e("i", null, null, n); k.style.left = ((sz.t0 - cu.t0) / (cu.t1 - cu.t0) * 100) + "%"; return k;
    });
    H.cm.push(n);
  });
  // kanca
  var k = satir("Kanca", 30); H.kn = [];
  D.olay.forEach(function (o, i) {
    var n = e("div", "kn " + o.tur, null, k.ic); n.style.left = yuzde(o.t);
    if (o.tur === "cizgi") n.style.height = (8 + 16 * o.guc) + "px";
    n.dataset.ip = o.tur + " · güç " + sn(o.guc) + " · " + pad(S[o.sahne].no) + " " + S[o.sahne].klasor.slice(3)
      + " · " + sn(o.t) + " sn";
    n.onclick = function (ev) { ev.stopPropagation(); git(o.t); };
  });
  // yorum işaretleri (görev haritası)
  var yr = satir("Yorum", 22); H.yorum = yr.ic; yorumSeritCiz();
  // nesne (şerit paketleme)
  var N = D.nesne.slice().sort(function (x, y) { return x.t0 - y.t0; }), bitis = [];
  var ns = satir("Nesne", 8, "ust"); H.nb = [];
  N.forEach(function (o) {
    var L = 0; while (bitis[L] > o.t0 + 0.01) L++; bitis[L] = o.t1;
    var n = blok(ns.ic, o.t0, o.t1, "nb", o.ad, o.ad + " · " + o.tur + " · " + sn(o.t0) + "–" + sn(o.t1) + " sn");
    n.style.top = (4 + L * 14) + "px"; n.style.setProperty("--c", NTUR[o.tur] || "#999");
    n.onclick = function (ev) { ev.stopPropagation(); git(o.t0); }; n._o = o; H.nb.push(n);
  });
  ns.sat.style.height = (bitis.length * 14 + 8) + "px";
  H.ph = e("div", null, null, zi); H.ph.id = "ph";
  zoomUygula(true);
}
function cetvelCiz() {
  var p = pps(), adimlar = [0.5, 1, 2, 5, 10, 15, 30], st = 30;
  for (var i = 0; i < adimlar.length; i++) if (adimlar[i] * p >= 64) { st = adimlar[i]; break; }
  H.cetvel.querySelectorAll(".tk").forEach(function (n) { n.remove(); });
  for (var x = 0; x <= T; x += st) {
    var n = e("div", "tk", kisaSn(x) + (st < 1 && x % 1 ? ".5" : ""), H.cetvel); n.style.left = yuzde(x);
  }
  for (var y = 0; y <= T && st >= 1; y += st / 5) {
    if (Math.abs(y / st - Math.round(y / st)) < 0.01) continue;
    var m = e("div", "tk k", "", H.cetvel); m.style.left = yuzde(y);
  }
}
function zoomUygula(ilk, merkezT, merkezX) {
  var w = W(); zi.style.setProperty("--W", w + "px"); zi.style.width = (w + ET) + "px";
  if (merkezT != null) zk.scrollLeft = merkezT * pps() - merkezX;
  var ze = $("#zoomE"); if (ze) ze.textContent = (Math.round(zoom * 10) / 10 + "×").replace(".", ",");
  cetvelCiz(); dalgaCiz();
}
function zoomSec(z, merkezX) {
  if (yan) z = 1;
  z = Math.max(1, Math.min(8, z)); if (z === zoom) return;
  var mx = merkezX == null ? (zk.clientWidth - ET) / 2 : merkezX;
  var mt = (zk.scrollLeft + mx) / pps(); zoom = z; zoomUygula(false, mt, mx);
}
function dalgaCiz() {
  var cv = H.dalga; if (!cv) return;
  var gen = Math.max(10, zk.clientWidth - ET), yuk = 56, dpr = window.devicePixelRatio || 1;
  cv.style.left = zk.scrollLeft + "px"; cv.style.width = gen + "px"; cv.style.height = yuk + "px";
  cv.width = Math.round(gen * dpr); cv.height = Math.round(yuk * dpr);
  var g = cv.getContext("2d"); g.scale(dpr, dpr); g.clearRect(0, 0, gen, yuk);
  g.fillStyle = "#2c2e34"; g.fillRect(0, yuk / 2, gen, 1);
  if (!wave) { g.fillStyle = "#8d9097"; g.font = "11px Lexend"; g.fillText("dalga çözülüyor", 8, 14); return; }
  var p = pps(), mid = yuk / 2, renk = "#5ec8b6", b = wave.bps;
  g.fillStyle = renk;
  for (var x = 0; x < gen; x++) {
    var a = Math.floor((zk.scrollLeft + x) / p * b), z = Math.max(a + 1, Math.floor((zk.scrollLeft + x + 1) / p * b));
    if (a >= wave.min.length) break;
    var lo = 0, hi = 0;
    for (var k = a; k < z && k < wave.min.length; k++) { if (wave.min[k] < lo) lo = wave.min[k];
      if (wave.max[k] > hi) hi = wave.max[k]; }
    var y0 = mid - hi * (mid - 2), y1 = mid - lo * (mid - 2);
    g.fillRect(x, y0, 1, Math.max(1, y1 - y0));
  }
}
// wav bir kez indirilir: <audio> blob'dan çalar, dalga aynı veriden çözülür
function sesYukle() {
  return fetch("ortak/anlatim/anlatim.wav").then(function (r) { return r.arrayBuffer(); }).then(function (buf) {
    au.src = URL.createObjectURL(new Blob([buf], { type: "audio/wav" }));
    return new OfflineAudioContext(1, 1, 44100).decodeAudioData(buf);
  }).then(function (ab) {
    var d = ab.getChannelData(0), bps = 200, n = Math.ceil(ab.duration * bps), per = Math.floor(ab.sampleRate / bps);
    var mn = new Float32Array(n), mx = new Float32Array(n);
    for (var i = 0; i < n; i++) {
      var lo = 0, hi = 0, e0 = i * per, e1 = Math.min(d.length, e0 + per);
      for (var j = e0; j < e1; j++) { var v = d[j]; if (v < lo) lo = v; if (v > hi) hi = v; }
      mn[i] = lo; mx[i] = hi;
    }
    wave = { min: mn, max: mx, bps: bps }; dalgaCiz();
  }).catch(function (er) { durumMesaj("Ses yüklenemedi: " + er); });
}
var dalgaBekle = 0;
zk.addEventListener("scroll", function () {
  if (!dalgaBekle) dalgaBekle = requestAnimationFrame(function () { dalgaBekle = 0; dalgaCiz(); });
});
zk.addEventListener("wheel", function (ev) {
  if (ev.altKey || ev.deltaX) return;
  var r = zk.getBoundingClientRect(), x = ev.clientX - r.left - ET;
  if (x < 0) return;
  ev.preventDefault(); zoomSec(zoom * Math.exp(-ev.deltaY * 0.002), x);
}, { passive: false });
zk.addEventListener("click", function (ev) {
  var b = ev.target.closest && ev.target.closest("[data-z]");
  if (b) zoomSec(zoom * (b.dataset.z === "+" ? 1.5 : 1 / 1.5));
});
var surukle = false;
function zamanTikla(ev) {
  var r = zk.getBoundingClientRect(), x = ev.clientX - r.left;
  git((zk.scrollLeft + x - ET) / pps());
}
zk.addEventListener("pointerdown", function (ev) {
  var r = zk.getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top;
  if (x < ET || x > zk.clientWidth || y > zk.clientHeight || ev.target.closest("[data-z]")) return;
  surukle = true; zk.setPointerCapture(ev.pointerId); zamanTikla(ev);
});
zk.addEventListener("pointermove", function (ev) { if (surukle) zamanTikla(ev); });
zk.addEventListener("pointerup", function () { surukle = false; });

// ---------- Kenar çubukları ----------
function sagKur() {
  var pa = $("#p-alt"); H.cu = [];
  D.cumle.forEach(function (c) {
    var d = e("div", "cu", null, pa);
    var h = e("h4", null, "<b>" + c.no + "</b><em>" + c.konusan + "</em><span>" + mmss(c.t0) + " – " + mmss(c.t1)
      + "</span>", d);
    h.onclick = function () { git(c.t0); };
    var p = e("p", null, null, d); d._w = c.sozcuk.map(function (sz) {
      var s = e("span", "w", sz.sozcuk, p); s.onclick = function () { git(sz.t0); };
        p.appendChild(document.createTextNode(" ")); return s;
    });
    d._c = c; H.cu.push(d);
  });
  var fl = $("#filtre"), turler = ["hepsi", "cizgi", "tik", "vurus", "parilti"], act = "hepsi";
  turler.forEach(function (tr) {
    var b = e("button", tr === act ? "on" : "", tr, fl);
    b.onclick = function () {
      act = tr; fl.querySelectorAll("button").forEach(function (x) { x.classList.toggle("on", x === b); });
      H.ol.forEach(function (n) { n.classList.toggle("gizli", tr !== "hepsi" && n._o.tur !== tr); });
    };
  });
  var po = $("#olaylar"); H.ol = [];
  D.olay.forEach(function (o) {
    var n = e("div", "sr", "<span class='zm'>" + mmss(o.t) + "</span><span class='ad'>" + o.tur
      + "</span><span class='chip'>güç " +
      sn(o.guc) + "</span><span class='chip'>" + pad(S[o.sahne].no) + "</span>", po);
    n.style.setProperty("--c", "var(--" + o.tur + ")"); n._o = o; n.onclick = function () { git(o.t); }; H.ol.push(n);
  });
  var sol = $("#sahneler");
  S.forEach(function (s, i) {
    var b = e("button", "sl", "<i></i><span><b>" + pad(s.no) + " " + BOLUM[i] + "</b><small>" + s.motor + " · " +
      sn(s.t_son - s.t_bas) + " sn</small></span>", sol);
    b.style.setProperty("--r", RENK[i]); b.onclick = function () { git(s.t_bas); }; b.dataset.i = i;
  });
  document.querySelectorAll("#sek2 button").forEach(function (b) {
    b.onclick = function () {
      document.querySelectorAll("#sek2 button").forEach(function (x) { x.classList.toggle("on", x === b); });
      document.querySelectorAll(".lp").forEach(function (p) { p.classList.toggle("on", p.id === b.dataset.l); });
    };
  });
  document.querySelectorAll("#sek button").forEach(function (b) {
    b.onclick = function () {
      document.querySelectorAll("#sek button").forEach(function (x) { x.classList.toggle("on", x === b); });
      document.querySelectorAll(".pn").forEach(function (p) { p.classList.toggle("on", p.id === "p-" + b.dataset.p); });
    };
  });
}
var kSahne = -1;
function sahneBilgiYaz(i) {
  var s = S[i], n = D.nesne.filter(function (o) { return o.sahne === i; }), pn = $("#p-nes"); pn.innerHTML = "";
  H.nr = n.map(function (o) {
    var r = e("div", "sr", "<span class='ad'>" + o.ad + "</span><span class='zm'>" + sn(o.t0) + "–" + sn(o.t1) +
      "</span><span class='chip'>" + o.tur + "</span>", pn);
    r.style.setProperty("--c", NTUR[o.tur]);
    r.onclick = function () { git(o.t0); secNesne = secNesne === o.ad ? "" : o.ad; nesneIsaretle(); yorumMetaYaz(); };
    r._o = o; return r;
  });
  secNesne = ""; yorumMetaYaz();
  var olSay = D.olay.filter(function (o) { return o.sahne === i; }).length;
  $("#p-sah").innerHTML = "<dl class='bil'><dt>Sahne</dt><dd>" + pad(s.no) + " · " + BOLUM[i]
    + "</dd><dt>Klasör</dt><dd>" +
    s.klasor + "</dd><dt>Motor</dt><dd>" + s.motor + "</dd><dt>Süre</dt><dd>" + sn(s.t_bas) + " – " + sn(s.t_son) +
    " sn</dd><dt>Kare</dt><dd>" + s.kare + " (içerik " + s.icerik_kare + ")</dd><dt>Geçiş</dt><dd>" + s.gecis +
    "</dd><dt>Nesne</dt><dd>" + n.length + "</dd><dt>Kanca olayı</dt><dd>" + olSay
      + "</dd><dt>Yerel kare</dt><dd id='yk'></dd>" +
    "<dt>Rapor</dt><dd><a target='_blank' href='sahneler/" + s.klasor + "/RAPOR.md'>RAPOR.md</a></dd></dl>";
  document.querySelectorAll(".sl").forEach(function (b) { b.classList.toggle("on", +b.dataset.i === i); });
  kSahne = i;
}

// ---------- Arayüz güncelleme (her karede, yalnız değişen) ----------
var son = {};
function aktifSec(liste, test) { var r = -1; for (var i = 0; i < liste.length; i++) if (test(liste[i], i)) r = i;
  return r; }
function arayuz(x, y) {
  var i = y.i;
  if (i !== kSahne) sahneBilgiYaz(i);
  var fr = kareNo(x), yerel = fr - Math.round(S[i].t_bas * FPS);
  if (son.fr !== fr) {
    yorumMetaYaz(); $("#zaman").textContent = mmss(x); $("#kare").textContent = "kare " + fr; son.fr = fr;
    var yk = $("#yk"); if (yk) yk.textContent = yerel + " / " + S[i].kare;
  }
  var pl = (ET + x * pps()), pxx = x * pps();
  if (son.px !== pxx) {
    H.ph.style.left = pl + "px"; H.bas.style.left = yuzde(x); son.px = pxx;
    if (calma !== "dur" && !surukle) {
      var gor = zk.scrollLeft + zk.clientWidth;
      if (pl > gor - 40 || pl < zk.scrollLeft + ET) zk.scrollLeft = Math.max(0, pxx - (zk.clientWidth - ET) * 0.2);
    }
  }
  var icon = calma === "dur" ? "<path d='M8 5l11 7-11 7z'/>" : "<path d='M7 5h4v14H7zM13 5h4v14h-4z'/>";
  if (son.ic !== icon) { $("#oyi").innerHTML = icon; son.ic = icon; }
  // cümle / sözcük
  var ci = aktifSec(D.cumle, function (c) { return x >= c.t0 && x < c.t1 + 0.5; }), wi = -1;
  if (ci >= 0) wi = aktifSec(D.cumle[ci].sozcuk, function (w) { return x >= w.t0 && x < w.t1 + 0.12; });
  if (son.ci !== ci || son.wi !== wi) {
    H.cu.forEach(function (d, k) {
      d.classList.toggle("on", k === ci);
      d._w.forEach(function (s, m) { s.classList.toggle("on", k === ci && m === wi); });
      H.cm[k].classList.toggle("on", k === ci);
      H.cm[k]._w.forEach(function (s, m) { s.classList.toggle("on", k === ci && m === wi); });
    });
    if (ci >= 0 && ci !== son.ci) H.cu[ci].scrollIntoView({ block: "nearest" });
    son.ci = ci; son.wi = wi;
  }
  // sahne, bölüm, nesne
  if (son.si !== i) { H.sbl.forEach(function (n, k) { n.classList.toggle("on", k === i); }); son.si = i; }
  var bi = aktifSec(H.bolum, function (n) { return x >= n._a && x < n._b; });
  if (son.bi !== bi) { H.bolum.forEach(function (n, k) { n.classList.toggle("on", k === bi); }); son.bi = bi; }
  var nk = "";
  H.nb.forEach(function (n) { var a = x >= n._o.t0 && x < n._o.t1; n._a = a; nk += a ? "1" : "0"; });
  if (son.nk !== nk) {
    H.nb.forEach(function (n) { n.classList.toggle("on", n._a); });
    if (H.nr) H.nr.forEach(function (r) { r.classList.toggle("on", x >= r._o.t0 && x < r._o.t1); });
    son.nk = nk;
  }
  // olay listesi: son geçen olay
  var oi = aktifSec(D.olay, function (o) { return o.t <= x; });
  if (son.oi !== oi) {
    if (son.oi >= 0 && H.ol[son.oi]) H.ol[son.oi].classList.remove("on");
    if (oi >= 0) { H.ol[oi].classList.add("on"); H.ol[oi].scrollIntoView({ block: "nearest" }); }
    son.oi = oi;
  }
  // durum satırı
  var sk = y.sonraki ? "hazır" : (i + 1 < S.length ? (slotBul(panes[0], i + 1, false) ? "yükleniyor" : "bekliyor")
    : "yok");
  var dm = performance.now() < mesajT ? " <b class='dur'>" + mesajM + "</b>" : "";
  var d = "<span>Sahne <b>" + pad(S[i].no) + " " + S[i].klasor.slice(3) + "</b></span><span>Yerel kare <b>" + yerel +
    " / " + S[i].kare + "</b></span><span>Küresel kare <b>" + fr + " / " + Math.round(T * FPS) + "</b></span>" +
    "<span>Bu sahne <b class='" + (y.cur ? "ok" : "dur") + "'>" + (y.cur ? "hazır" : "yükleniyor") + "</b></span>" +
    "<span>Sonraki sahne <b class='" + (sk === "hazır" || sk === "yok" ? "ok" : "dur") + "'>" + sk + "</b></span>" +
    "<span>Tema <b>" + TEMA + "</b></span><span>Hız <b>" + String(hiz).replace(".", ",") + "×</b></span>" + dm;
  if (son.d !== d) { $("#alt").innerHTML = d; son.d = d; }
}
function dongu(ms) {
  var dt = Math.min(0.1, (ms - sonMs) / 1000); sonMs = ms;
  if (calma === "ileri") { if (sessiz) t += dt * hiz; else t = au.currentTime; if (t >= T - 0.03) { t = T - 1 / FPS;
    dur(); } }
  else if (calma === "geri") { t -= dt * hiz; if (t <= 0) { t = 0; dur(); } }
  var y = sahneYonet(panes[0], t);
  if (yan) sahneYonet(panes[1], t);
  if (panes[0].S !== S) y = { i: sahneNo({ S: S }, t), cur: true, sonraki: {} };
  arayuz(t, y);
  requestAnimationFrame(dongu);
}

// ---------- Etiket ipucu, klavye, olaylar ----------
var ip = $("#ip");
document.addEventListener("mousemove", function (ev) {
  var n = ev.target.closest && ev.target.closest("[data-ip]");
  if (!n) { ip.style.display = "none"; return; }
  ip.textContent = n.dataset.ip; ip.style.display = "block";
  ip.style.left = Math.min(innerWidth - ip.offsetWidth - 8, ev.clientX + 12) + "px"; ip.style.top = (ev.clientY - 34)
    + "px";
});
addEventListener("keydown", function (ev) {
  if (ev.ctrlKey || ev.metaKey || ev.altKey) return;
  if (/^(INPUT|TEXTAREA|SELECT)$/.test(ev.target.tagName)) return;
  var k = ev.key, sh = ev.shiftKey, ok = true;
  if (k === " ") oyna();
  else if (k === "ArrowRight") { dur(); sh ? git(t + 1) : adim(1); }
  else if (k === "ArrowLeft") { dur(); sh ? git(t - 1) : adim(-1); }
  else if (k === "Home") git(0);
  else if (k === "End") git(T);
  else if (k === "j" || k === "J") geriOyna();
  else if (k === "k") { dur(); karePng(); }
  else if (k === "K") dur();
  else if (k === "l" || k === "L") { if (calma !== "ileri") oyna(); }
  else if (k === "Escape") { if (!kirintiUst()) ok = false; }
  else ok = false;
  if (ok) ev.preventDefault();
});
document.addEventListener("click", function (ev) {
  var b = ev.target.closest("button"); if (b) b.blur();
});
$("#tasima").addEventListener("click", function (ev) {
  var b = ev.target.closest("[data-e]"); if (!b) return; var c = b.dataset.e;
  if (c === "oyna") oyna(); else { dur(); if (c === "basa") git(0); else if (c === "sona") git(T);
    else if (c === "-1s") git(t - 1); else if (c === "+1s") git(t + 1); else adim(c === "-1k" ? -1 : 1); }
});
$("#hiz").addEventListener("click", function (ev) { var b = ev.target.closest("[data-h]");
  if (b) hizSec(+b.dataset.h); });
$("#tema").addEventListener("click", function (ev) { var b = ev.target.closest("[data-t]");
  if (b) temaSec(b.dataset.t); });
$("#png").onclick = karePng;
$("#yyb").onclick = function () { yanSec(!yan); };
[0, 1].forEach(function (k) { $("#ys" + k).onchange = function (ev) { paneAyarla(panes[k], ev.target.value); }; });
$("#sahne").onclick = function () { oyna(); };
addEventListener("resize", function () { olc(); zoomUygula(false); });

// ---------- Görev haritası verisi: API varsa yazılır, yoksa dosyadan salt okunur ----------
var API = "/api/present-continuous/", apiVar = false, SU = [], GO = [], YO = [], SK = "";
var VM = null, REV = [], secGorev = "", secNesne = "", vurYorum = "", tfAcik = false, gfAcik = false;
var DURUM = ["acik", "uretimde", "inceleme", "onay", "kapali"];
var DAD = { planli: "planlı", acik: "açık", uretimde: "üretimde", inceleme: "inceleme", onay: "onay",
  kapali: "kapalı" };
var TURAD = { "ana-yatay": "ana yatay", dikey: "dikey", shorts: "shorts", alternatif: "alternatif" };
var GTUR = { uret: "üret", duzelt: "düzelt", turev: "türev", karar: "karar" };
function ec(s) {
  return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;" }[c]; });
}
function listeAyir(x, ad) {
  if (x && !Array.isArray(x)) {
    if (x.video && typeof x.video === "object") VM = x.video;
    if (Array.isArray(x.revizyonlar)) REV = x.revizyonlar;
  }
  return Array.isArray(x) ? x : ((x && (x[ad] || x.liste)) || []); }
function listeAl(ad, dosya) {
  return getJ(API + ad).then(function (x) { apiVar = true; return listeAyir(x, ad); }).catch(function () {
    return getJ(dosya).then(function (x) { return listeAyir(x, ad); }).catch(function () { return []; });
  });
}
function apiIste(yontem, yol, govde) {
  if (!apiVar) return Promise.reject(new Error("sunucu API'si kapalı"));
  return fetch(API + yol, { method: yontem, headers: { "Content-Type": "application/json" },
    body: JSON.stringify(govde) }).then(function (r) {
    if (!r.ok) throw new Error(yol + " " + r.status);
    return r.text().then(function (m) { try { return JSON.parse(m); } catch (er) { return {}; } });
  });
}
// video meta ve revizyonlar: surumler.json içinde (API dizi dönerse dosyadan) ya da video.json
function metaYukle() {
  var a = (VM && REV.length) ? Promise.resolve() : getJ("surumler.json")
    .then(function (x) { listeAyir(x, "surumler"); })
    .catch(function () {});
  return a.then(function () { return VM ? null : getJ("video.json").then(function (v) { VM = v.video || v; }); })
    .catch(function () {});
}
function surumRev(s) {
  return (s.revizyonlar || []).concat(REV.filter(function (r) { return r.surum === s.kimlik; }));
}
function yenile() {
  return Promise.all([listeAl("surumler", "surumler.json"), listeAl("gorevler", "gorevler.json"),
    listeAl("yorumlar", "yorumlar.json")]).then(function (a) { SU = a[0]; GO = a[1]; YO = a[2]; return metaYukle(); })
    .then(hepsiCiz);
}
function hepsiCiz() { agacCiz(); gorevCiz(); yorumCiz(); yorumSeritCiz(); paneSecenek(); }
function uyariHtml() {
  return apiVar ? "" : "<div class='uy'>Sunucu API'si kapalı: kayıtlar salt okunur; ekleme ve durum değişimi "
    + "yok.</div>";
}
function adresMi(a) { return /\.html?(\?|#|$)/.test(a || ""); }
function surumAdres(s) {
  var r = surumRev(s).reverse();
  for (var i = 0; i < r.length; i++) {
    if (r[i].onizleme) return r[i].onizleme;
    if (adresMi(r[i].cikti)) return r[i].cikti;
  }
  return s.onizleme || s.adres || (adresMi(s.cikti) ? s.cikti : "");
}
function surumBul(k) { return SU.filter(function (x) { return x.kimlik === k; })[0]; }
function surumGorevleri() {
  var s = surumBul(SK), ana = !s || s.tur === "ana-yatay";
  if (!s) return GO;
  return GO.filter(function (g) { return g.surum ? g.surum === SK : ana; });
}
function surumYorumlari() {
  if (!surumBul(SK)) return YO;
  return YO.filter(function (y) { return !y.surum || y.surum === SK; });
}
function secenek(liste, secili, ad) {
  return liste.map(function (k) { return "<option value='" + ec(k) + "'" + (k === secili ? " selected" : "") + ">"
    + ec(ad ? ad[k] : k) + "</option>"; }).join("");
}
function formHata(kok, m) { var h = kok.querySelector(".hata"); if (h) h.textContent = m || ""; }

// ---------- Sol panel: İlgililer (sürüm ağacı) ----------
function surumAc(s) {
  var a = surumAdres(s);
  if (s.kimlik === SK) return durumMesaj("Bu sürüm zaten açık");
  if (!a) return durumMesaj("Planlı sürüm: önizleme adresi yok");
  location.href = a + (a.indexOf("?") < 0 ? "?" : "&") + "surum=" + encodeURIComponent(s.kimlik)
    + (YOLM ? "&yol=" + encodeURIComponent(YOLM) : "");
}
function agacDugum(s, kok, d, goruldu) {
  if (goruldu[s.kimlik]) return; goruldu[s.kimlik] = 1;
  var a = surumAdres(s), b = e("div", "ag" + (s.kimlik === SK ? " on" : ""), null, kok);
  b.style.paddingLeft = (8 + d * 14) + "px";
  var ust = e("button", "agb", "<i class='dt' style='--c:var(--d-" + ec(s.durum || "acik") + ")'></i><span><b>"
    + ec(s.ad || s.kimlik) + "</b><small>" + ec(TURAD[s.tur] || s.tur || "") + " · <span class='rz' data-d='"
    + ec(s.durum || "acik") + "'>" + ec(DAD[s.durum] || s.durum || "açık") + "</span>"
    + (a || s.durum === "planli" ? "" : " <span class='rz pl'>planlı</span>") + "</small></span>", b);
  ust.onclick = function () { surumAc(s); };
  surumRev(s).forEach(function (r) {
    var rv = e("div", "rv", "<b>" + ec(r.no) + "</b><span>" + ec(String(r.tarih || "").slice(0, 10)) + "</span><em>"
      + ec(r.degisiklik || "")
      + "</em>", b);
    rv.title = r.degisiklik || "";
  });
  SU.filter(function (x) { return x.kaynak === s.kimlik; }).forEach(function (x) {
    agacDugum(x, kok, d + 1, goruldu);
  });
}
function metaListe(kok, baslik, L) {
  if (!Array.isArray(L) || !L.length) return;
  var d = e("details", "mk", "<summary>" + ec(baslik) + " (" + L.length + ")</summary><ul>" + L.map(function (x) {
    return "<li>" + ec(x) + "</li>"; }).join("") + "</ul><button class='kop'>Kopyala</button>", kok);
  d.querySelector(".kop").onclick = function (ev) {
    var b = ev.target, m = L.join("\n");
    try { navigator.clipboard.writeText(m).then(function () { b.textContent = "Kopyalandı"; }); } catch (er) {
      var r = document.createRange(); r.selectNodeContents(d.querySelector("ul")); var sc = getSelection();
      sc.removeAllRanges(); sc.addRange(r); b.textContent = "Seçildi: Ctrl+C";
    }
  };
}
function metaKart(kok) {
  if (!VM) return;
  var k = e("div", "meta", "<b>" + ec(VM.kod || VM.kimlik || "") + "</b><span>" + ec(VM.konu || "") + "</span><small>"
    + ec([VM.ders, VM.seviye, VM.kitle].filter(Boolean).join(" · ")) + "</small>", kok);
  metaListe(k, "Amaçlar", VM.amaclar); metaListe(k, "Can alıcı", VM.canAlici);
  metaListe(k, "Kazanım", VM.kazanim);
  if (Array.isArray(VM.etiketler) && VM.etiketler.length) {
    e("div", "et2", VM.etiketler.map(function (x) { return "<span class='chip'>" + ec(x) + "</span>"; }).join(" "), k);
  }
}
function agacCiz() {
  var kok = $("#ilgili"); if (!kok) return; kok.innerHTML = uyariHtml();
  metaKart(kok);
  var goruldu = {}, ag = e("div", "agac", null, kok);
  if (!SU.length) e("div", "bosl", "Henüz sürüm kaydı yok.", ag);
  SU.filter(function (s) { return !s.kaynak || !surumBul(s.kaynak); }).forEach(function (s) {
    agacDugum(s, ag, 0, goruldu);
  });
  SU.forEach(function (s) { agacDugum(s, ag, 0, goruldu); });
  var tb = e("button", "ekle", tfAcik ? "Türev formunu kapat" : "+ Türev", kok);
  tb.onclick = function () { tfAcik = !tfAcik; agacCiz(); };
  if (!tfAcik) return;
  var f = e("div", "fm", "<label>Tür<select name='tur'>" + secenek(["dikey", "shorts", "alternatif"], "dikey", TURAD)
    + "</select></label><label>Ad<input name='ad' placeholder='ör. Dikey tanıtım'></label><label>Kaynak sürüm"
    + "<select name='kaynak'>" + SU.map(function (s) { return "<option value='" + ec(s.kimlik) + "'"
      + (s.kimlik === SK ? " selected" : "") + ">" + ec(s.ad || s.kimlik) + "</option>"; }).join("")
    + "</select></label><label>Senaryo notu<textarea name='not' rows='3'></textarea></label>"
    + "<div class='hata'></div><button class='ana'>Türev oluştur</button>", kok);
  f.querySelector("button").onclick = function () {
    var q = function (n) { return f.querySelector("[name=" + n + "]").value.trim(); };
    if (!q("ad")) return formHata(f, "Ad yaz.");
    apiIste("POST", "surum", { tur: q("tur"), ad: q("ad"), kaynak: q("kaynak"), "not": q("not") })
      .then(function () { tfAcik = false; return yenile(); })
      .catch(function (er) { formHata(f, "Kaydedilemedi: " + er.message); });
  };
}

// ---------- Sağ panel: Görevler + yorumlar ----------
function gorevKur() {
  var yf = $("#yf");
  yf.innerHTML = "<div class='ym2'>t <b id='yt'>00:00.00</b> · sahne <b id='ys'>—</b> · nesne <b id='yn' "
    + "title='Bırakmak için tıkla'>—</b></div><div class='ym2' id='yg'></div>"
    + "<textarea id='ymt' rows='3' placeholder='Yorum yaz'></textarea><div class='hata' id='yh'></div>"
    + "<button class='ana' id='yg2'>Gönder</button>";
  $("#ymt").addEventListener("focus", function () { dur(); });
  $("#yn").onclick = function () { secNesne = ""; nesneIsaretle(); yorumMetaYaz(); };
  $("#yg2").onclick = function () {
    var m = $("#ymt").value.trim(); if (!m) return formHata(yf, "Yorum boş.");
    var i = sahneNo(panes[0], t);
    apiIste("POST", "yorum", { gorev: secGorev || undefined, surum: SK, t: Math.round(t * 100) / 100,
      sahne: pad(S[i].no),
      nesne: secNesne || undefined, metin: m, yazar: "Nadir" }).then(function () {
      $("#ymt").value = ""; formHata(yf, ""); return yenile(); })
      .catch(function (er) { formHata(yf, "Gönderilemedi: " + er.message); });
  };
  yorumMetaYaz();
}
function yorumMetaYaz() {
  if (!$("#yt")) return;
  var i = sahneNo(panes[0], t), g = secGorev ? GO.filter(function (k) { return k.kimlik === secGorev; })[0] : null;
  $("#yt").textContent = mmss(t); $("#ys").textContent = pad(S[i].no); $("#yn").textContent = secNesne || "—";
  $("#yg").innerHTML = "Görev: <b>" + (g ? ec(g.baslik) : "genel (sürüm)") + "</b>";
  $("#yg2").disabled = !apiVar; $("#yg2").title = apiVar ? "" : "Sunucu API'si kapalı";
}
function nesneIsaretle() {
  if (H.nr) H.nr.forEach(function (r) { r.classList.toggle("sec", r._o.ad === secNesne); });
}
function gorevCiz() {
  var gu = $("#gu"), gl = $("#gl"); if (!gu) return;
  var L = surumGorevleri();
  gu.innerHTML = uyariHtml() + "<div class='bsl2'><span>Görevler (" + L.length + ")</span></div>";
  var gb = e("button", "ekle", gfAcik ? "Görev formunu kapat" : "+ Görev", gu);
  gb.onclick = function () { gfAcik = !gfAcik; gorevCiz(); };
  if (gfAcik) {
    var f = e("div", "fm", "<label>Başlık<input name='baslik'></label><label>Tür<select name='tur'>"
      + secenek(Object.keys(GTUR), "uret", GTUR) + "</select></label><label>Grup<input name='grup' "
      + "placeholder='ör. kapak'></label><label>Açıklama<textarea name='aciklama' rows='3'></textarea></label>"
      + "<div class='hata'></div><button class='ana'>Görev oluştur</button>", gu);
    f.querySelector("button").onclick = function () {
      var q = function (n) { return f.querySelector("[name=" + n + "]").value.trim(); };
      if (!q("baslik")) return formHata(f, "Başlık yaz.");
      apiIste("POST", "gorev", { baslik: q("baslik"), aciklama: q("aciklama"), tur: q("tur"), grup: q("grup"),
        surum: SK, atanan: "sef" }).then(function () { gfAcik = false; return yenile(); })
        .catch(function (er) { formHata(f, "Kaydedilemedi: " + er.message); });
    };
  }
  gl.innerHTML = "";
  if (!L.length) e("div", "bosl", "Bu sürümde görev yok.", gl);
  L.forEach(function (g) {
    var sy = YO.filter(function (y) { return y.gorev === g.kimlik; }).length;
    var r = e("div", "gr" + (g.kimlik === secGorev ? " on" : ""), "<b>" + ec(g.baslik) + "</b><div class='gs'>"
      + "<select class='dsel' data-d='" + ec(g.durum || "acik") + "' " + (apiVar ? "" : "disabled ")
      + "title='Durum'>" + secenek(DURUM, g.durum || "acik", DAD) + "</select>"
      + (g.grup ? "<span class='chip'>" + ec(g.grup) + "</span>" : "") + (g.atanan ? "<span class='chip'>"
      + ec(g.atanan) + "</span>" : "") + "<span class='chip'>" + ec(GTUR[g.tur] || g.tur || "") + "</span>"
      + (sy ? "<span class='chip'>" + sy + " yorum</span>" : "") + "</div>", gl);
    r.onclick = function (ev) {
      if (ev.target.closest("select")) return;
      secGorev = secGorev === g.kimlik ? "" : g.kimlik; gorevCiz(); yorumCiz(); yorumMetaYaz();
    };
    r.querySelector("select").onchange = function (ev) {
      var v = ev.target.value; ev.target.dataset.d = v;
      apiIste("PATCH", "gorev/" + encodeURIComponent(g.kimlik), { durum: v }).then(yenile)
        .catch(function (er) { durumMesaj("Durum değişmedi: " + er.message); yenile(); });
    };
  });
}
function yorumCiz() {
  var kok = $("#yl"); if (!kok) return; kok.innerHTML = "";
  var g = secGorev ? GO.filter(function (k) { return k.kimlik === secGorev; })[0] : null;
  var L = surumYorumlari().filter(function (y) { return !secGorev || y.gorev === secGorev; });
  L.sort(function (a, b) { return (a.t == null ? 1e9 : a.t) - (b.t == null ? 1e9 : b.t); });
  e("div", "bsl2", "<span>Yorumlar · " + (g ? ec(g.baslik) : "bu sürüm") + " (" + L.length + ")</span>", kok);
  if (!L.length) e("div", "bosl", "Yorum yok.", kok);
  L.forEach(function (y) {
    var d = e("div", "yr" + (y.kimlik === vurYorum ? " on" : "") + (y.durum === "cozuldu" ? " cz" : ""),
      "<div class='yb'>" + (y.t != null ? "<button class='yt'>" + mmss(y.t) + "</button>" : "") + "<em>" + ec(y.yazar)
      + "</em>" + (y.sahne != null ? "<span class='chip'>sahne " + ec(y.sahne) + "</span>" : "")
      + (y.nesne ? "<span class='chip'>" + ec(y.nesne) + "</span>" : "") + "</div><p>" + ec(y.metin) + "</p>", kok);
    d._k = y.kimlik;
    var b = d.querySelector(".yt"); if (b) b.onclick = function () { dur(); git(y.t); };
    var cb = e("button", "coz", y.durum === "cozuldu" ? "Yeniden aç" : "Çözüldü", d.querySelector(".yb"));
    cb.disabled = !apiVar;
    cb.onclick = function () {
      apiIste("PATCH", "yorum/" + encodeURIComponent(y.kimlik), { durum: y.durum === "cozuldu" ? "acik" : "cozuldu" })
        .then(yenile).catch(function (er) { durumMesaj("Yorum durumu değişmedi: " + er.message); });
    };
  });
}
function yorumSeritCiz() {
  if (!H.yorum) return; H.yorum.innerHTML = "";
  surumYorumlari().forEach(function (y) {
    if (y.t == null) return;
    var n = e("div", "ym" + (y.kimlik === vurYorum ? " on" : "") + (y.durum === "cozuldu" ? " cz" : ""), null, H.yorum);
    n.style.left = yuzde(y.t);
    n.dataset.ip = y.yazar + " · " + sn(y.t) + " sn · " + String(y.metin || "").slice(0, 60);
    n.onclick = function (ev) { ev.stopPropagation(); yorumaGit(y); };
  });
}
function yorumaGit(y) {
  dur(); git(y.t); vurYorum = y.kimlik; secGorev = y.gorev || "";
  document.querySelector("#sek [data-p=gor]").click(); gorevCiz(); yorumCiz(); yorumSeritCiz(); yorumMetaYaz();
  var d = document.querySelector("#yl .yr.on"); if (d) d.scrollIntoView({ block: "nearest" });
}

// ---------- Kırıntı: Harita > ünite > konu > video > sürüm; Esc = bir üst ----------
var YOLM = "", KIRINTI_UST = "";
function kirintiCiz(oge, surumAd) {
  var kok = $("#kirinti"); kok.textContent = "";
  var liste = oge.slice(); liste.push({ ad: surumAd, son: true });
  liste.forEach(function (o, i) {
    if (i) { var ay = document.createElement("span"); ay.className = "ay"; ay.textContent = "\u25B8"; kok.appendChild(ay); }
    if (o.son) { var b = document.createElement("b"); b.textContent = o.ad; kok.appendChild(b); return; }
    var q = [o.ac ? "ac=" + encodeURIComponent(o.ac) : "", o.sec ? "sec=" + encodeURIComponent(o.sec) : ""]
      .filter(Boolean).join("&");
    var a = document.createElement("a"); a.textContent = o.ad; a.href = "harita.html" + (q ? "?" + q : "");
    kok.appendChild(a); KIRINTI_UST = a.href;
  });
}
function kirintiUst() { if (!KIRINTI_UST) return false; location.href = KIRINTI_UST; return true; }
function kirintiKur(surumAd) {
  var proje = API.split("/")[2];
  return Promise.all([fetch("/projeler/katalog.json").then(function (r) { return r.json(); }),
    import("./harita-model.js")]).then(function (v) {
    var kat = v[0], M = v[1];
    YOLM = QS.get("yol") || M.projeYolu(kat, proje).join(",");
    kirintiCiz(M.kirinti(kat, YOLM), surumAd);
  }).catch(function () { kirintiCiz([{ ad: "Harita", ac: "", sec: "" }], surumAd); });
}

// ---------- Açılış ----------
sesYukle();
var QS = new URLSearchParams(location.search);
var haritaVeri = Promise.all([listeAl("surumler", "surumler.json"), listeAl("gorevler", "gorevler.json"),
  listeAl("yorumlar", "yorumlar.json")]);
veriYukle().then(function (v) {
  D = v; S = v.z.sahneler; FPS = v.z.fps; T = S[S.length - 1].t_son;
  TEMA = QS.get("tema") === "acik" ? "acik" : "koyu";
  panes = [0, 1].map(function (k) {
    return { k: k, el: $("#pn" + k), S: S, yol: YOL, tema: TEMA, surum: "", gosterilen: -1,
      slot: [0, 1].map(function (m) { return { idx: m, f: $("#f" + k + m), no: -1, hazir: false, goster: false,
        sonT: null, op: -1, z: -1 }; }) };
  });
  sagKur(); gorevKur(); zamanCizgisiKur(); temaSec(TEMA); hizSec(1); olc();
  window.EDITOR = { git: git, durum: function () { return { t: t, calma: calma, yan: yan, slot: panes[0].slot.map(
    function (s) { return { no: s.no, hazir: s.hazir, goster: s.goster, op: s.op }; }) }; }, oyna: oyna, dur: dur,
    zoom: zoomSec, yan: yanSec };
  requestAnimationFrame(dongu);
  return haritaVeri;
}).then(function (a) {
  SU = a[0]; GO = a[1]; YO = a[2];
  return metaYukle();
}).then(function () {
  var ana = SU.filter(function (s) { return s.tur === "ana-yatay"; })[0] || SU[0];
  SK = QS.get("surum") || (ana ? ana.kimlik : "");
  var s = surumBul(SK); if (s) $("#ad small").textContent = "YDT Basic · " + (s.ad || s.kimlik);
  kirintiKur(s ? (s.ad || s.kimlik) : SK);
  hepsiCiz(); yorumMetaYaz();
  if (QS.get("t")) git(+QS.get("t") || 0);
  if (QS.get("yan") === "1") yanSec(true);
}).catch(function (er) { $("#bekle").textContent = "Veri yüklenemedi: " + er; });

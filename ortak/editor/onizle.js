// Present Continuous — kurgu editörü. Tek saat: <audio>.
// Sahneler iframe'de ?canli=1&mesaj=1 ile yalnız mesaj zamanıyla çizer.
"use strict";
var PROJE = KalemYol.projeAdi() || "present-continuous", YOL = KalemYol.projeYolu(PROJE);
var FPS = 30, ET = 104;
var BOLUM = ["Giriş", "Hook", "Example 1 / 3", "Example 2 / 3", "Example 3 / 3", "Question"];
function bolumAd(i) {
  var s = S[i]; if (!s) return "";
  if (s.ad) return s.ad;
  if (PROJE === "present-continuous" && BOLUM[i]) return BOLUM[i];
  return s.klasor.replace(/^\d+-[a-z]+-/, "");
}
var NTUR = { cizim: "var(--n-cizim)", metin: "var(--n-metin)", kart: "var(--n-kart)", isaret: "var(--n-isaret)" };
var $ = function (s) { return document.querySelector(s); };
var au = $("#au"), zk = $("#zk"), zi = $("#zi");
var D = null, S = [], T = 94.33, GEN = 1920, YUK = 1080, t = 0, calma = "dur", hiz = 1, zoom = 1;
var TEMA = "koyu", H = {};
var sessiz = false, panes = [], yan = false, yyAcik = false, sonMs = 0, wave = null, sonOlay = -1;
var SUA = [], HOSTK = "", ARA = 8, MAXP = 8;      // karşılaştırma: ana projenin sürümleri, ana pencere kimliği

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
// Lexend yazı tipi proje dizinindedir (CSS projeyi bilmez): @font-face adresi YOL'dan kurulur.
(function () {
  var st = document.createElement("style");
  st.textContent = [500, 700].map(function (w) {
    return "@font-face{font-family:Lexend;font-weight:" + w + ";src:url(" + YOL + "ortak/font/lexend-latin-" + w
      + "-normal.woff2)}";
  }).join("");
  document.head.appendChild(st);
})();
function getJ(yol) { return fetch(yol).then(function (r) { if (!r.ok) throw new Error(yol + " " + r.status);
  return r.json(); }); }
// zaman.json sahneleri: klasor, motor, kare, t_bas, t_son
function zamanYukle() { return getJ(YOL + "zaman.json"); }
function sozcukYukle() {                                                  // küresel sözcük zamanları → cümleler
  return Promise.all([getJ(YOL + "ortak/anlatim/sozcukler.json"),
    fetch(YOL + "ortak/anlatim/METIN.md").then(function (r) { return r.text(); })])
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
    return getJ(YOL + "sahneler/" + s.klasor + "/olaylar.json").then(function (L) {
      return L.map(function (o) { return { t: s.t_bas + o.kare / z.fps, tur: o.tur, guc: o.guc, sahne: i,
        kare: o.kare }; });
    }).catch(function () { return []; });
  })).then(function (a) { return [].concat.apply([], a).sort(function (x, y) { return x.t - y.t; }); });
}
function nesneYukle(z) {                                                  // nesneler.json: [{ad,t0,t1,tur}] küresel sn
  return Promise.all(z.sahneler.map(function (s, i) {
    return getJ(YOL + "sahneler/" + s.klasor + "/nesneler.json").then(function (L) {
      return L.map(function (o) { return { ad: o.ad, t0: o.t0, t1: o.t1, tur: o.tur, sahne: i }; });
    }).catch(function () { return []; });
  })).then(function (a) { return [].concat.apply([], a); });
}
function veriYukle() {
  return zamanYukle().then(function (z) {
    var fs = z.sahneler.filter(function (s) { return /form/.test(s.klasor); }).pop();
    var formJ = fs ? getJ(YOL + "sahneler/" + fs.klasor + "/zamanlar.json")
      .catch(function () { return {}; }) : Promise.resolve({});
    return Promise.all([sozcukYukle(), olayYukle(z), nesneYukle(z), formJ]).then(function (a) {
      return { z: z, cumle: a[0], olay: a[1], nesne: a[2], form: a[3].form || null,
        formI: fs ? z.sahneler.indexOf(fs) : -1 };
    });
  });
}

// ---------- Sahne penceresi: ortak çekirdek ../oynatici/cekirdek.js (oynatıcıyla AYNI kod) ------
// Pencere p: S, paket (= yol), tema, slot[{idx, y, f, …}], gosterilen. Kıvrım/fade ve mesaj bütçesi
// (05.11: ikincil pencereler oynarken tek karede bir, 15 fps) çekirdekte.
var C = KalemCekirdek;
function sahneNo(p, x) { return C.sahneNo(p.S, x); }
function sahneYonet(p, x) {
  var r = C.sahneYonet(x, p, { FPS: FPS, seyrek: p.k > 0 && calma !== "dur" });
  if (p.k === 0) $("#bekle").style.display = p.gosterilen >= 0 ? "none" : "flex";
  return { i: r.i, cur: r.hazir, sonraki: r.sonraki };
}
window.addEventListener("message", function (ev) { C.hazirMesaj(ev, panes); });
function motorRenk(m) {
  return /hyper/i.test(m) ? "var(--m-hf)" : /paper/i.test(m) ? "var(--m-paper)" : /canvas/i.test(m)
    ? "var(--m-canvas)" : "var(--s5)";
}
function motorKisa(m) {
  return /hyper/i.test(m) ? "HyperFrames" : /paper/i.test(m) ? "Paper.js" : /canvas/i.test(m) ? "Canvas" : m;
}
// ---------- Karşılaştırma: N pencere (sürüm × tema), tek saat, tek ses ----------
var KISA = { "ana-yatay": "Yatay", "dikey-tam": "Dikey", shorts: "Shorts", dikey: "D1" };
function anaProje() { return PROJE.replace(/-(dikey|s1|d1)$/, ""); }
function suaBul(k) { return SUA.filter(function (x) { return x.kimlik === k; })[0]; }
function projeSeviye(ad) { var m = /-(temel|orta|ileri)(-|$)/.exec(ad || ""); return m ? m[1] : ""; }
function surumProje(k) {                        // sürüm kimliği → önizlediği proje adı
  var s = suaBul(k), a = s ? KalemYol.yeniAdres(surumAdres(s)) : "";
  return (a && KalemYol.projeAdi(a.split("?")[0])) || (k === HOSTK ? PROJE : "");
}
function surumSeviye(k) { var p = surumProje(k), sv = p ? projeSeviye(p) : ""; return sv === projeSeviye(PROJE) ? "" : sv; }
function surumBicim(k) {
  var proje = surumProje(k), s = suaBul(k);
  if (!proje) return KISA[k] || (s && TURAD[s.tur]) || k || PROJE;
  return /-d1$/.test(proje) ? "D1 parça" : /-dikey$/.test(proje) ? "Dikey" : /-s1$/.test(proje) ? "Shorts" : "Yatay";
}
function surumKisa(k) { var sv = surumSeviye(k); return surumBicim(k) + (sv ? " " + sv : ""); }
function suaYukle() {                            // sürüm listesi ana projeden (dikey/s1 projede surumler.json yok)
  if (anaProje() === PROJE) { SUA = SU; return Promise.resolve(); }
  return getJ("/api/" + encodeURIComponent(anaProje()) + "/surumler")
    .then(function (x) { SUA = Array.isArray(x) ? x : (x.surumler || x.liste || []); })
    .catch(function () { SUA = SU; });
}
function hostKimlik() {                          // bu projeyi önizleyen sürümün kimliği
  for (var i = 0; i < SUA.length; i++) {
    var a = KalemYol.yeniAdres(surumAdres(SUA[i])) || "";
    if (a && KalemYol.projeAdi(a.split("?")[0]) === PROJE) return SUA[i].kimlik;
  }
  return SK;
}
function pencereAdaylari() {                     // [{kimlik, ad, adres}] pencere açılabilen sürümler
  var L = [];
  SUA.forEach(function (s) {
    var a = KalemYol.yeniAdres(surumAdres(s)); if (!a || !KalemYol.projeAdi(a.split("?")[0])) return;
    L.push({ kimlik: s.kimlik, ad: surumKisa(s.kimlik), adres: a });
  });
  if (!L.some(function (x) { return x.kimlik === HOSTK; })) {
    L.unshift({ kimlik: HOSTK, ad: surumKisa(HOSTK), adres: KalemYol.editorYolu("onizle.html", "", PROJE) });
  }
  return L;
}
function paneOlustur(k, S0, yol0) {
  var el = e("div", "pw", null, $("#sahne")); el.id = "pn" + k;
  var ic = e("div", "pane", null, el);
  var slot = [0, 1].map(function (m) {
    var y = e("div", "yaprak", null, ic), f = e("iframe", null, null, y);   // yaprak: kıvrım yüzeyi
    f.title = "pencere " + k + " tampon " + (m + 1);
    return { idx: m, y: y, f: f, no: -1, hazir: false, goster: false, sonT: null, sonF: -1, op: -1,
      z: -1, tr: null };
  });
  var pl = e("div", "pz", null, el);
  var p = { k: k, el: el, ic: ic, pl: pl, S: S0 || [], yol: yol0 || "", paket: yol0 || "",
    tema: TEMA, surum: "", kimlik: HOSTK,
    gosterilen: -1, gen: GEN, yuk: YUK, slot: slot, etT: "" };
  pl.onclick = function (ev) { ev.stopPropagation(); paneEditorAc(p); };
  el.addEventListener("mouseenter", function () { if (panes.length > 1) sesSec(p.yol || YOL); });  // imleç = ses
  return p;
}
function paneEditorAc(p) {                       // pencerenin kendi editörünü aynı anda yeni sekmede aç
  var ad = pencereAdaylari().filter(function (x) { return x.kimlik === (p.kimlik || HOSTK); })[0];
  var a = ad ? ad.adres : KalemYol.editorYolu("onizle.html", "", PROJE);
  var q = "surum=" + encodeURIComponent(p.kimlik || HOSTK) + "&tema=" + p.tema + "&t=" + (Math.round(t * 100) / 100);
  window.open(a + (a.indexOf("?") < 0 ? "?" : "&") + q, "_blank");
}
function paneAnahtar(p) { return (p.kimlik || HOSTK) + ":" + p.tema; }
function paneBul(key) { for (var k = 1; k < panes.length; k++) if (paneAnahtar(panes[k]) === key) return k; return -1; }
function paneKapat(k) {
  if (k <= 0 || k >= panes.length) return;
  var p = panes[k]; p.slot.forEach(function (s) { s.f.src = "about:blank"; }); p.el.remove();
  panes.splice(k, 1); panes.forEach(function (q, i) { q.k = i; q.el.id = "pn" + i; });
}
function paneAc(kimlik, tema) {
  if (panes.length >= MAXP) { durumMesaj("En çok " + MAXP + " pencere"); return Promise.resolve(null); }
  var p = paneOlustur(panes.length); p.tema = tema; p.kimlik = kimlik; panes.push(p);
  if (kimlik === HOSTK) { paneKaynak(p, YOL, S); paneTema(p); olc(); return Promise.resolve(p); }
  var ad = pencereAdaylari().filter(function (x) { return x.kimlik === kimlik; })[0];
  var proje = ad ? KalemYol.projeAdi(ad.adres.split("?")[0]) : null;
  if (!proje) { paneKapat(p.k); durumMesaj("Sürümün projesi yok: " + kimlik); return Promise.resolve(null); }
  var yol = KalemYol.projeYolu(proje);
  return getJ(yol + "zaman.json").then(function (z) {
    p.gen = z.genislik || 1920; p.yuk = z.yukseklik || 1080; paneKaynak(p, yol, z.sahneler); paneTema(p); olc();
    return p;
  }).catch(function () { paneKapat(p.k); olc(); durumMesaj("Sürümün sahneleri yüklenemedi: " + kimlik); return null; });
}
function yanDurum() {                            // ≥2 pencere = karşılaştırma yerleşimi
  var a = panes.length > 1;
  if (a !== yan) {
    yan = a; if (a) zoomSec(1);
    document.body.classList.toggle("yan", a);
  }
  $("#yyb").classList.toggle("on", yyAcik); $("#yy").hidden = !yyAcik; olc();
}
function pencereToggle(key) {
  if (key === paneAnahtar(panes[0])) return durumMesaj("Ana pencere kapanmaz; temasını üstten değiştir");
  var k = paneBul(key), is = k > 0 ? (paneKapat(k), Promise.resolve())
    : paneAc(key.split(":")[0], key.split(":")[1] || "koyu");
  is.then(function () { yanDurum(); pencereCiz(); pencereYaz(); });
}
function pencereAc(keys) {                       // adresten: ?pencere=kimlik:tema,...
  var L = keys.filter(function (k) { return k && paneBul(k) < 0 && k !== paneAnahtar(panes[0]); });
  yyAcik = true;
  Promise.all(L.map(function (k) { return paneAc(k.split(":")[0], k.split(":")[1] || "koyu"); }))
    .then(function () { yanDurum(); pencereCiz(); pencereYaz(); });
  yanDurum(); pencereCiz();
}
function yanSec(a) {
  yyAcik = a;
  if (a && panes.length === 1) {
    var L = pencereAdaylari().filter(function (x) { return x.kimlik !== HOSTK; }).slice(0, MAXP - 1);
    Promise.all(L.map(function (x) { return paneAc(x.kimlik, TEMA); }))
      .then(function () { yanDurum(); pencereCiz(); pencereYaz(); });
  } else if (!a) { while (panes.length > 1) paneKapat(panes.length - 1); }
  yanDurum(); pencereCiz(); pencereYaz();
}
function hostCiftKapat() {                       // ana pencere temayı alınca aynı anahtarlı ek pencere kapanır
  var k = paneBul(paneAnahtar(panes[0])); if (k > 0) { paneKapat(k); yanDurum(); pencereYaz(); }
}
function pencereYaz() {
  try {
    var q = new URLSearchParams(location.search), L = panes.slice(1).map(paneAnahtar);
    if (L.length) q.set("pencere", L.join(",")); else q.delete("pencere");
    q.delete("yan");
    history.replaceState(null, "", q.toString() ? "?" + q.toString() : location.pathname);
  } catch (er) {}
}
function pencereCiz() {                          // çipler: sürüm × tema; açık pencereler vurgulu
  var kok = $("#yyc"); if (!kok) return; kok.innerHTML = "";
  var host = paneAnahtar(panes[0]), grup = {}, sira = [], dolu = panes.length >= MAXP;
  var sayac = document.querySelector("#yy > .yl"); if (sayac) sayac.textContent = "Pencereler " + panes.length + "/" + MAXP;
  pencereAdaylari().forEach(function (x) {                 // bu videonun sürümleri önce; başka seviye ayrı küme
    var g = surumSeviye(x.kimlik); if (!grup[g]) { grup[g] = []; sira.push(g); } grup[g].push(x);
  });
  sira.sort(function (a, b) { return (a ? 1 : 0) - (b ? 1 : 0); });
  sira.forEach(function (g) {
    e("span", "yg", g ? ec(g) + " seviye (başka video)" : "bu video", kok);
    grup[g].forEach(function (x) {
      ["koyu", "acik"].forEach(function (tm) {
        var key = x.kimlik + ":" + tm, on = key === host || paneBul(key) > 0;
        var b = e("button", "pc" + (on ? " on" : "") + (key === host ? " sabit" : "") + (g ? " baska" : "")
          + (!on && dolu ? " dolu" : ""),
          ec(surumBicim(x.kimlik)) + "<small>" + (tm === "acik" ? "açık" : "koyu") + "</small>", kok);
        b.dataset.pk = key; b.title = (g ? g + " seviye · " : "") + (key === host ? "Ana pencere (tema üstten)"
          : (on ? "Pencereyi kapat" : (dolu ? "En çok " + MAXP + " pencere: önce birini kapat" : "Pencere aç")));
      });
    });
  });
  sesSecenek();
}
var sesYol = YOL;
function sesSecenek() {
  var sel = $("#yss"); if (!sel) return; var o = "", gor = {};
  panes.forEach(function (p) {
    var y = p.yol || YOL; if (gor[y]) return; gor[y] = 1;
    o += "<option value='" + ec(y) + "'" + (y === sesYol ? " selected" : "") + ">" + ec(surumKisa(p.kimlik || HOSTK))
      + "</option>";
  });
  sel.innerHTML = o;
}
function sesSec(y) { if (!y || y === sesYol) return; sesYol = y; sesYukle(y); }
function paneEtiketYenile() {                    // pencere rozeti: sürüm · tema · sahne · motor (motor rengi)
  panes.forEach(function (p) {
    if (!p.S.length) return;
    var i = sahneNo(p, t), s = p.S[i];
    var sv = surumSeviye(p.kimlik || HOSTK);
    var tx = ec(surumBicim(p.kimlik || HOSTK)) + (sv ? " <b class='sev'>" + ec(sv) + " seviye</b>" : "") + " · "
      + (p.tema === "acik" ? "açık" : "koyu") + " · " + pad(s.no) + " " + ec(s.klasor.replace(/^\d+-[a-z]+-/, ""))
      + " · " + ec(motorKisa(s.motor));
    if (p.etT !== tx) {
      p.pl.innerHTML = "<i class='md' style='--m:" + motorRenk(s.motor) + "'></i>" + tx
        + "<span class='ac' title='Bu sürümün editörünü bu anda aç'>\u2197</span>";
      p.etT = tx;
    }
  });
}
function olc() {                                 // pencereleri 1–3 satıra paketler, en büyük ortak yüksekliği seçer
  var o = $("#orta"), sh = $("#sahne"), n = panes.length; if (!n) return;
  var ust = yyAcik ? (Math.min(72, $("#yy").offsetHeight) + 10) : 0;
  var kn = panelHepsiGizli() ? 8 : 24;
  var W = o.clientWidth - kn, Hh = o.clientHeight - kn - ust;
  var en = null, ETK = yan ? 22 : 0;             // karşılaştırmada her pencerenin altında rozet satırı
  for (var r = 1; r <= Math.min(3, n); r++) {
    var per = Math.ceil(n / r), sat = [], h = (Hh - (r - 1) * ARA - r * ETK) / r;
    for (var i = 0; i < n; i += per) {
      var g = panes.slice(i, i + per), or = g.reduce(function (a, p) { return a + p.gen / p.yuk; }, 0);
      sat.push({ g: g, or: or }); h = Math.min(h, (W - (g.length - 1) * ARA) / or);
    }
    if (!en || h > en.h) en = { h: h, sat: sat, r: r };
  }
  var h = en.h, gen = 0;
  en.sat.forEach(function (s) { s.w = h * s.or + (s.g.length - 1) * ARA; gen = Math.max(gen, s.w); });
  sh.style.width = gen + "px"; sh.style.height = (en.r * (h + ETK) + (en.r - 1) * ARA) + "px";
  sh.style.marginTop = ust + "px";
  en.sat.forEach(function (s, ri) {
    var x = (gen - s.w) / 2;
    s.g.forEach(function (p) {
      var w = h * p.gen / p.yuk;
      p.el.style.display = "block"; p.el.style.left = x + "px"; p.el.style.top = (ri * (h + ETK + ARA)) + "px";
      p.el.style.width = w + "px"; p.el.style.height = (h + ETK) + "px"; p.ic.style.height = h + "px"; x += w + ARA;
      p.slot.forEach(function (sl) {
        sl.f.style.width = p.gen + "px"; sl.f.style.height = p.yuk + "px"; sl.f.style.transform = "scale(" + (w / p.gen) + ")";
      });
    });
  });
}
// pencerenin sahne kaynağını değiştirir, tamponları sıfırlar
function paneKaynak(p, yol, L) {
  p.yol = yol; p.paket = yol; p.S = L; p.gosterilen = -1;
  p.slot.forEach(function (s) {
    C.slotSifirla(s); s.y.style.opacity = 0; s.y.style.transform = ""; s.f.src = "about:blank";
  });
}
function paneTema(p) {
  p.ic.classList.toggle("acik", p.tema === "acik");
  p.slot.forEach(function (s) {
    try { s.f.contentWindow.postMessage({ tip: "tema", ad: p.tema }, "*"); } catch (er) {}
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
  if (panes[0]) { panes[0].tema = a; paneTema(panes[0]); hostCiftKapat(); pencereCiz(); }
  try {
    var q = new URLSearchParams(location.search);
    if (a === "acik") q.set("tema", "acik"); else q.delete("tema");
    history.replaceState(null, "", q.toString() ? "?" + q.toString() : location.pathname);
  } catch (er) {}
}
function karePng() {
  var c = C.slotBul(panes[0], sahneNo(panes[0], t), true);
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
  var b = satir("Bölüm", 18), ad = S.map(function (_, i) { return bolumAd(i); }), fI = D.formI,
    form = D.form || (PROJE === "present-continuous" && fI === 5 ? S[5].t_bas + 3.91 : null);
  H.bolum = [];
  S.forEach(function (s, i) {
    var son = (form && i === fI) ? form : s.t_son;
    H.bolum.push(blok(b.ic, s.t_bas, son, "b bl", ad[i], ad[i]));
    H.bolum[i]._a = s.t_bas; H.bolum[i]._b = son;
  });
  if (form) {                                  // form bölümü: form sahnesinin ikinci yarısı
    var fb = blok(b.ic, form, S[fI].t_son, "b bl", "Form", "Form");
    fb._a = form; fb._b = S[fI].t_son;
    H.bolum.push(fb);
  }
  // sahne
  var sr = satir("Sahne", 26); H.sbl = [];
  S.forEach(function (s, i) {
    var n = blok(sr.ic, s.t_bas, s.t_son, "b", pad(s.no) + " " + s.klasor.slice(3), s.klasor + " · " + s.motor);
    n.style.setProperty("--r", motorRenk(s.motor)); n.onclick = function (ev) { ev.stopPropagation(); git(s.t_bas); };
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
var sesOnbellek = {}, sesImzaSimdi = "";       // yol → {src, wave, imza}; aynı dosya (dikey = yatay sesi) yeniden yüklenmez
function sesImza(buf) {
  var u = new Uint8Array(buf), h = 7;
  for (var i = 44; i < Math.min(u.length, 262144); i += 61) h = (h * 31 + u[i]) >>> 0;
  return buf.byteLength + ":" + h;
}
function dalgaCoz(buf) {
  return new OfflineAudioContext(1, 1, 44100).decodeAudioData(buf).then(function (ab) {
    var d = ab.getChannelData(0), bps = 200, n = Math.ceil(ab.duration * bps), per = Math.floor(ab.sampleRate / bps);
    var mn = new Float32Array(n), mx = new Float32Array(n);
    for (var i = 0; i < n; i++) {
      var lo = 0, hi = 0, e0 = i * per, e1 = Math.min(d.length, e0 + per);
      for (var j = e0; j < e1; j++) { var v = d[j]; if (v < lo) lo = v; if (v > hi) hi = v; }
      mn[i] = lo; mx[i] = hi;
    }
    return { min: mn, max: mx, bps: bps };
  });
}
function sesUygula(k, yol) {                    // k: önbellek kaydı; aynı imza = aynı dosya, kaynak değişmez (kesinti yok)
  var sel = $("#yss"); if (sel && sel.value !== yol) sel.value = yol;
  if (k.imza === sesImzaSimdi) return;
  var oynuyor = calma === "ileri", t0 = t; dur();
  sesImzaSimdi = k.imza; au.src = k.src;
  au.addEventListener("loadedmetadata", function () { git(t0); if (oynuyor) oyna(); }, { once: true });
  wave = k.wave; dalgaCiz();
}
function sesYukle(yol) {                        // yol: ses kaynağı projesi; karşılaştırmada seçici ya da imleç seçer
  yol = yol || YOL; var k = sesOnbellek[yol];
  if (k && !k.then) { sesUygula(k, yol); return Promise.resolve(); }
  if (k) return k.then(function (x) { if (sesYol === yol) sesUygula(x, yol); });
  var p = fetch(yol + "ortak/anlatim/anlatim.wav").then(function (r) {
    if (!r.ok) throw new Error(r.status); return r.arrayBuffer();
  }).then(function (buf) {
    var kayit = { src: URL.createObjectURL(new Blob([buf], { type: "audio/wav" })), imza: sesImza(buf), wave: null };
    return dalgaCoz(buf).then(function (w) { kayit.wave = w; return kayit; });
  });
  sesOnbellek[yol] = p;
  return p.then(function (x) { sesOnbellek[yol] = x; if (sesYol === yol) sesUygula(x, yol); })
    .catch(function (er) { delete sesOnbellek[yol]; durumMesaj("Ses yüklenemedi: " + er.message); });
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
  var sol = $("#sahneler"), lg = e("div", null, null, sol); lg.id = "motorl";
  [["HyperFrames", "var(--m-hf)"], ["Paper.js", "var(--m-paper)"], ["Canvas", "var(--m-canvas)"]].forEach(function (m) {
    e("span", null, "<i style='--m:" + m[1] + "'></i>" + m[0], lg);
  });
  S.forEach(function (s, i) {
    var b = e("button", "sl", "<i></i><span><b>" + pad(s.no) + " " + bolumAd(i) + "</b><small>"
      + s.motor + " · " + sn(s.t_son - s.t_bas) + " sn</small></span>", sol);
    b.style.setProperty("--r", motorRenk(s.motor)); b.onclick = function () { git(s.t_bas); }; b.dataset.i = i;
  });
  document.querySelectorAll("#sek2 button[data-l]").forEach(function (b) {
    b.onclick = function () {
      document.querySelectorAll("#sek2 button[data-l]").forEach(function (x) { x.classList.toggle("on", x === b); });
      document.querySelectorAll(".lp").forEach(function (p) { p.classList.toggle("on", p.id === b.dataset.l); });
    };
  });
  document.querySelectorAll("#sek button[data-p]").forEach(function (b) {
    b.onclick = function () {
      document.querySelectorAll("#sek button[data-p]").forEach(function (x) { x.classList.toggle("on", x === b); });
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
  $("#p-sah").innerHTML = "<dl class='bil'><dt>Sahne</dt><dd>" + pad(s.no) + " · " + bolumAd(i)
    + "</dd><dt>Klasör</dt><dd>" +
    s.klasor + "</dd><dt>Motor</dt><dd>" + s.motor + "</dd><dt>Süre</dt><dd>" + sn(s.t_bas) + " – " + sn(s.t_son) +
    " sn</dd><dt>Kare</dt><dd>" + s.kare + " (içerik " + s.icerik_kare + ")</dd><dt>Geçiş</dt><dd>" + s.gecis +
    "</dd><dt>Nesne</dt><dd>" + n.length + "</dd><dt>Kanca olayı</dt><dd>" + olSay
      + "</dd><dt>Yerel kare</dt><dd id='yk'></dd>" +
    "<dt>Rapor</dt><dd><a target='_blank' href='" + YOL + "sahneler/" + s.klasor + "/RAPOR.md'>RAPOR.md</a></dd></dl>";
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
  var sk = y.sonraki ? "hazır" : (i + 1 < S.length ? (C.slotBul(panes[0], i + 1, false) ? "yükleniyor" : "bekliyor")
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
  for (var k = 1; k < panes.length; k++) if (panes[k].S.length) sahneYonet(panes[k], t);
  if (yan) paneEtiketYenile();
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
// ---------- Paneller: gizle / göster; odak = hepsi gizli, sahne bütün alanı alır ----------
var PANEL = { sol: true, sag: true, zp: true };
try {
  var pk0 = JSON.parse(localStorage.getItem("kalem.editor.paneller") || "null");
  if (pk0) Object.keys(PANEL).forEach(function (k) { if (k in pk0) PANEL[k] = !!pk0[k]; });
} catch (er) {}
function panelHepsiGizli() { return !PANEL.sol && !PANEL.sag && !PANEL.zp; }
function panelUygula(kaydet) {
  var ed = $("#ed");
  Object.keys(PANEL).forEach(function (k) {
    ed.classList.toggle(k + "-gizli", !PANEL[k]);
  });
  ed.classList.toggle("odak", panelHepsiGizli());         // odak: durum satırı da gizli
  $("#odak").classList.toggle("on", panelHepsiGizli());
  if (kaydet) { try { localStorage.setItem("kalem.editor.paneller", JSON.stringify(PANEL)); } catch (er) {} }
  if (panes.length) { olc(); zoomUygula(false); }
}
function panelToggle(k) { PANEL[k] = !PANEL[k]; panelUygula(true); }
function odakToggle() {                          // hepsi gizliyse geri aç, değilse hepsini gizle
  var ac = panelHepsiGizli(); PANEL.sol = PANEL.sag = PANEL.zp = ac; panelUygula(true);
}
panelUygula(false);

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
  else if (k === "h" || k === "H") odakToggle();
  else if (k === "Escape") { if (panelHepsiGizli()) odakToggle(); else if (!kirintiUst()) ok = false; }
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
$("#yyb").onclick = function () { yanSec(!yyAcik); };
document.addEventListener("click", function (ev) { var b = ev.target.closest("[data-pn]");   // daralt / ray
  if (b) panelToggle(b.dataset.pn); });
$("#odak").onclick = odakToggle;
$("#yyc").onclick = function (ev) { var b = ev.target.closest("[data-pk]"); if (b) pencereToggle(b.dataset.pk); };
$("#yss").onchange = function (ev) { sesSec(ev.target.value); };
$("#sahne").onclick = function () { oyna(); };
au.addEventListener("ended", function () { if (calma === "ileri") dur(); });   // kısa ses kaynağı (shorts) bitince dur
addEventListener("resize", function () { olc(); zoomUygula(false); });

// ---------- Görev haritası verisi: API varsa yazılır, yoksa dosyadan salt okunur ----------
var API = "/api/" + encodeURIComponent(PROJE) + "/", apiVar = false, SU = [], GO = [], YO = [], SK = "";
var VM = null, VMA = {}, REV = [], secGorev = "", secNesne = "", vurYorum = "", tfAcik = false, gfAcik = false;
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
    return getJ(YOL + dosya).then(function (x) { return listeAyir(x, ad); }).catch(function () { return []; });
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
  var a = (VM && (REV.length || apiVar)) ? Promise.resolve() : getJ(YOL + "surumler.json")
    .then(function (x) { listeAyir(x, "surumler"); })
    .catch(function () {});
  return a.then(function () { return VM ? null : getJ(YOL + "video.json").then(function (v) { VM = v.video || v; }); })
    .catch(function () {}).then(adYaz);
}
// Üst başlık: video meta (konu, kitle, seviye); dikey/s1 projede meta ana projeden (05.11; önce sabitti).
function adYaz() {
  var v = VM || {}, ana = PROJE.replace(/-(dikey|s1|d1)$/, "");
  var p = (v.konu || v.ders || ana === PROJE) ? Promise.resolve(v)
    : getJ("/api/" + encodeURIComponent(ana) + "/surumler").then(function (x) { return x.video || v; })
      .catch(function () { return v; });
  return p.then(function (m) {
    VMA = m; var ad = m.konu || m.ders || PROJE, alt = kitleYazi();
    var ek = PROJE.slice(ana.length).replace("-", " · ");
    $("#ad").innerHTML = ec(ad + ek) + "<small>" + ec((alt ? alt + " · " : "") + "canlı önizleme") + "</small>";
    document.title = ad + ek + " — kurgu";
  }).catch(function () {});
}
function kitleYazi() { return [VMA.kitle, VMA.seviye].filter(Boolean).join(" "); }
function surumRev(s) {
  return (s.revizyonlar || []).concat(REV.filter(function (r) { return r.surum === s.kimlik; }));
}
function yenile() {
  return Promise.all([listeAl("surumler", "surumler.json"), listeAl("gorevler", "gorevler.json"),
    listeAl("yorumlar", "yorumlar.json")]).then(function (a) { SU = a[0]; GO = a[1]; YO = a[2]; return metaYukle(); })
    .then(hepsiCiz);
}
function hepsiCiz() { agacCiz(); gorevCiz(); yorumCiz(); yorumSeritCiz(); pencereCiz(); }
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
  var a = KalemYol.yeniAdres(surumAdres(s));
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
    var a = document.createElement("a"); a.textContent = o.ad; a.href = KalemYol.editorYolu("harita.html", q, PROJE);
    kok.appendChild(a); KIRINTI_UST = a.href;
  });
}
function kirintiUst() { if (!KIRINTI_UST) return false; location.href = KIRINTI_UST; return true; }
function kirintiKur(surumAd) {
  return Promise.all([fetch("/projeler/katalog.json").then(function (r) { return r.json(); }),
    import("./harita-model.js")]).then(function (v) {
    var kat = v[0], M = v[1];
    YOLM = QS.get("yol") || M.projeYolu(kat, PROJE).join(",");
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
  GEN = v.z.genislik || 1920; YUK = v.z.yukseklik || 1080;
  TEMA = QS.get("tema") === "acik" ? "acik" : "koyu";
  panes = [paneOlustur(0, S, YOL)];
  sagKur(); gorevKur(); zamanCizgisiKur(); temaSec(TEMA); hizSec(1); olc();
  window.EDITOR = { git: git, durum: function () { return { t: t, calma: calma, yan: yan, slot: panes[0].slot.map(
    function (s) { return { no: s.no, hazir: s.hazir, goster: s.goster, op: s.op }; }),
    pencereler: panes.map(function (p) { var i = p.S.length ? sahneNo(p, t) : -1; return { kimlik: p.kimlik || HOSTK,
      tema: p.tema, sahne: i, hazir: !!(i >= 0 && C.slotBul(p, i, true)), gen: p.gen, yuk: p.yuk }; }) }; },
    oyna: oyna, dur: dur, zoom: zoomSec, yan: yanSec, pencere: pencereToggle, panel: panelToggle,
    odak: odakToggle };
  requestAnimationFrame(dongu);
  return haritaVeri;
}).then(function (a) {
  SU = a[0]; GO = a[1]; YO = a[2];
  return metaYukle();
}).then(function () {
  var ana = SU.filter(function (s) { return s.tur === "ana-yatay"; })[0] || SU[0];
  SK = QS.get("surum") || (ana ? ana.kimlik : "");
  var s = surumBul(SK); if (s) $("#ad small").textContent = (kitleYazi() || "YDT") + " · " + (s.ad || s.kimlik);
  kirintiKur(s ? (s.ad || s.kimlik) : SK);
  hepsiCiz(); yorumMetaYaz();
  if (QS.get("t")) git(+QS.get("t") || 0);
  return suaYukle();
}).then(function () {
  HOSTK = hostKimlik(); panes[0].kimlik = HOSTK;
  var pk = QS.get("pencere");
  if (pk) pencereAc(pk.split(",")); else if (QS.get("yan") === "1") yanSec(true); else pencereCiz();
}).catch(function (er) { $("#bekle").textContent = "Veri yüklenemedi: " + er; });

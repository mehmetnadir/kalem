// Kalem ders oynatıcısı — prototip 0.1 (08.11.2026). Görüş sürümü; PRD: dijital-anlatim
// .claude/docs/oynatici-prd-0811.md (K25, K33, K35, K36, K37). Tek saat: <audio>. Sahneler
// iframe'de ?canli=1&mesaj=1 ile yalnız {tip:"zaman", t} mesajıyla çizer (ortak/editor/onizle.js
// çekirdeğiyle aynı protokol, ortak/surucu.js). Oynatma sırasında sunucu ucu çağrılmaz.
// Kullanım: monte(kok, { paket: "/projeler/present-perfect-temel/", tema, baslik, alt, olay })
// Olaylar (olay(ad, detay)): hazir · oynuyor · durdu · bitti · zaman · bolum · tema · hata · dil
// Basılı tutma 2× (turbo.js): sahneye bas-tut → 2×, aşağı sürükle → halka dolar, kilit (09.11).
// Yön çifti (yon.js, 09.11): paketler [yatay, dikey] aynı ses saatinde; dokunmatik cihazda iki yön
// de sıcak tutulur (kendi iframe tamponları), cihaz dönünce yalnız görünen pane değişir: ses ve
// zaman kesilmez. Masaüstünde pasif yön tembel yüklenir (eski pane kalır, yenisi hazır olunca).
// dil: sözlük tr/en (madde 17)
"use strict";
import { turboKur, bas, sure, hareket, birak, kapat, hizli, TURBO_HIZ, BASILI_MS }
  from "./turbo.js";
import { yonAdi, yonIstek, ciftUyumlu } from "./yon.js";
import { sozlukSec, dilCoz, DILLER } from "./sozluk.js";
import "./cekirdek.js";                       // globalThis.KalemCekirdek (editörle ortak)
const C = globalThis.KalemCekirdek;
export const SURUM = "0.4.1";
const GIZLE_MS = 3000, SAR = 10, OK = 5;
const DEPO = "kalem.oynatici.", HIZLAR = [0.75, 1, 1.25, 1.5, 2];
const ZEMIN = { acik: "#f7f3ea", koyu: "#1b1a17" };
const IK = {
  oynat: "<path d='M7 4.5l12.5 7.5L7 19.5z'/>",                // dolu: CSS [data-ik] kuralı
  dur: "<path d='M6 5h4.5v14H6zM13.5 5H18v14h-4.5z'/>",
  cift: "<path d='M5 6l6 6-6 6M13 6l6 6-6 6'/>",
  kilit: "<rect x='5' y='11' width='14' height='10' rx='2'/><path d='M8 11V7a4 4 0 0 1 8 0v4'/>",
  geri: "<path d='M4 12a8 8 0 1 0 2.3-5.7M4 4v4.6h4.6'/><text x='12' y='15.5'>10</text>",
  ileri: "<path d='M20 12a8 8 0 1 1-2.3-5.7M20 4v4.6h-4.6'/><text x='12' y='15.5'>10</text>",
  ses: "<path d='M4 9v6h4l5 4V5L8 9zM16 9a4 4 0 0 1 0 6M18.5 6.5a7.5 7.5 0 0 1 0 11'/>",
  sesAz: "<path d='M4 9v6h4l5 4V5L8 9zM16 9a4 4 0 0 1 0 6'/>",
  sessiz: "<path d='M4 9v6h4l5 4V5L8 9zM17 9l4 6M21 9l-4 6'/>",
  altyazi: "<rect x='3' y='5' width='18' height='14' rx='2'/>" +
    "<path d='M7 12h3M12 12h5M7 15.5h5M14 15.5h3'/>",
  bolum: "<path d='M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01'/>",
  hiz: "<path d='M5 17a8 8 0 1 1 14 0M12 13l3.5-4'/>",
  gunes: "<circle cx='12' cy='12' r='4'/><path d='M12 2v2M12 20v2M4.9 4.9l1.4 1.4" +
    "M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4'/>",
  ay: "<path d='M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z'/>",
  tam: "<path d='M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5'/>",
  tamYon: "<path d='M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5'/>" +   // yön çifti: dönen telefon
    "<rect class='ko-tel' x='9.25' y='7' width='5.5' height='10' rx='1.2'/>",
  tamKapat: "<path d='M9 4v5H4M15 4v5h5M20 15h-5v5M4 15h5v5'/>",
  tekrar: "<path d='M3 12a9 9 0 1 0 3-6.7M3 4v5h5'/>",
  uyari: "<path d='M12 3l10 18H2zM12 10v5M12 18h.01'/>",
  ok: "<path d='M9 6l6 6-6 6'/>",
};

const pad = (n) => (n < 10 ? "0" : "") + n;
const sinirla = (x, a, b) => Math.max(a, Math.min(b, x));
function mmss(x) {
  x = Math.max(0, Math.floor(x + 1e-6)); return Math.floor(x / 60) + ":" + pad(x % 60);
}
function el(tag, cls, ust, html) {
  const n = document.createElement(tag); if (cls) n.className = cls;
  if (html != null) n.innerHTML = html; if (ust) ust.appendChild(n); return n;
}
const svg = (ad) =>
  "<svg viewBox='0 0 24 24' aria-hidden='true' focusable='false'>" + IK[ad] + "</svg>";
function dugme(ust, cls, etiket, ad) {
  const b = el("button", "ko-d " + cls, ust, svg(ad)); b.type = "button"; b.dataset.ik = ad;
  b.setAttribute("aria-label", etiket); b.title = etiket; return b;
}
function ikon(b, ad) { if (b.dataset.ik !== ad) { b.innerHTML = svg(ad); b.dataset.ik = ad; } }
function etiket(b, m) { if (b.getAttribute("aria-label") !== m) { b.setAttribute("aria-label", m);
  b.title = m; } }
function depoAl(k, v) {
  try { const x = localStorage.getItem(DEPO + k); return x == null ? v : JSON.parse(x); }
  catch (e) { return v; /* depo kapalı (özel pencere): varsayılan */ }
}
function depoYaz(k, v) {
  try { localStorage.setItem(DEPO + k, JSON.stringify(v)); }
  catch (e) { /* depo kapalı: tercih bu oturumda kalır */ }
}
// Ardışık aynı ad = tek bölüm; `bolum` alanı (K37) öncelikli, yoksa sahne `ad`.
function bolumListesi(S) {
  const B = [];
  S.forEach((s, i) => {
    const ad = s.bolum || s.ad || s.klasor.replace(/^\d+-[a-z]+-/, ""), son = B[B.length - 1];
    if (son && son.ad === ad) { son.t1 = s.t_son; son.sahneler.push(i); }
    else B.push({ ad, t0: s.t_bas, t1: s.t_son, sahneler: [i] });
  });
  return B;
}

export function monte(kok, sec) {
  sec = sec || {};
  const paketler = (sec.paketler || [sec.paket]).filter(Boolean)
    .map((p) => String(p).replace(/\/?$/, "/"));
  const d = {
    paketler, Y: {}, yon: "", bekleyenY: null, sicak: false,
    B: [], T: 0, FPS: 30, t: 0, oynuyor: false, bitti: false,
    hiz: depoAl("hiz", 1), ses: depoAl("ses", 1), sessiz: depoAl("sessiz", false),
    altyazi: depoAl("altyazi", true), tema: sec.tema || depoAl("tema", null) || "acik",
    dil: dilCoz(sec, kok),
    alt: [], slot: [], gosterilen: -1, hazir: false, basladi: false, gizleT: 0, gizliydi: false,
    surukle: false, menu: "", kontrolUstunde: false, sonSn: -1, sonBolum: -1, sonAlt: "",
    oynuyorduSurukle: false, turbo: turboKur(), turboZ: 0, turboTik: false,
    dokunma: matchMedia("(pointer: coarse)").matches,
    azHareket: matchMedia("(prefers-reduced-motion: reduce)").matches,
  };
  let M = sozlukSec(d.dil);
  kok.lang = d.dil;
  const konsol = (e) => {
    if (typeof console !== "undefined") console.error("[kalem-oynatici]", e);
  };
  const olay = (ad, detay) => { try { if (sec.olay) sec.olay(ad, detay || {}); }
    catch (e) { konsol(e); } };

  // ---------- Kurulum: DOM ----------
  kok.classList.add("ko"); kok.tabIndex = 0; kok.dataset.tema = d.tema;
  kok.setAttribute("role", "region"); kok.setAttribute("aria-label", sec.baslik || M.dersVideosu);
  kok.classList.toggle("ko-dokunma", d.dokunma); kok.innerHTML = "";
  const sahne = el("div", "ko-sahne", kok);
  // Yön başına pane + 2 iframe tamponu (çift tampon). Yön zaman.json yüklenince bilinir.
  function paneKur(ad, paket, z) {
    const pane = el("div", "ko-pane ko-pasif", sahne); pane.dataset.yon = ad;
    const Y = { ad, paket, S: z.sahneler, GEN: z.genislik || 1920, YUK: z.yukseklik || 1080, pane,
      tema: d.tema, gosterilen: -1 };
    Y.slot = [0, 1].map((m) => {
      const y = el("div", "ko-yaprak", pane), f = el("iframe", null, y);
      f.title = M.sahneTampon(ad, m + 1); f.setAttribute("aria-hidden", "true");
      f.tabIndex = -1;
      return { idx: m, y, f, no: -1, hazir: false, goster: false, sonT: null, sonF: -1, op: -1,
        z: -1, tr: null };
    });
    return Y;
  }
  const A = () => d.Y[d.yon];                                   // etkin yön
  const herY = (fn) => Object.values(d.Y).forEach(fn);
  const herSlot = (fn) => herY((Y) => Y.slot.forEach((s) => fn(s, Y)));
  const altyaziEl = el("div", "ko-altyazi", sahne); altyaziEl.setAttribute("aria-live", "off");
  const orta = el("div", "ko-orta", sahne);
  const oGeri = dugme(orta, "ko-geri", M.saniyeGeri(SAR), "geri");
  const oOynat = dugme(orta, "ko-oynat", M.oynat, "oynat");
  const oIleri = dugme(orta, "ko-ileri", M.saniyeIleri(SAR), "ileri");
  const poster = el("div", "ko-poster", sahne);
  const posterUst = el("div", "ko-poster-ust", poster, "<b></b><small></small>");
  posterUst.querySelector("b").textContent = sec.baslik || "";
  posterUst.querySelector("small").textContent = sec.alt || "";
  const buyuk = dugme(poster, "ko-buyuk", M.oynat, "oynat");
  const posterNot = el("div", "ko-poster-not", poster, M.yukleniyor);
  const hata = el("div", "ko-hata", sahne); hata.hidden = true; hata.setAttribute("role", "alert");
  const turboEl = el("button", "ko-turbo", sahne, "<span class='ko-halka'>" +
    "<svg viewBox='0 0 24 24'><circle class='iz' cx='12' cy='12' r='9'/>" +
    "<circle class='dolum' cx='12' cy='12' r='9'/></svg></span><b>" + TURBO_HIZ + "×</b>" +
    "<span class='ko-turbo-ik' data-ik='cift'>" + svg("cift") + "</span>");
  turboEl.type = "button"; turboEl.hidden = true; turboEl.tabIndex = -1;
  turboEl.setAttribute("aria-label", M.hizCarpan(TURBO_HIZ));
  el("div", "ko-golge", kok);
  const kontrol = el("div", "ko-kontrol", kok);
  const cubuk = el("div", "ko-cubuk", kontrol); cubuk.tabIndex = 0;
  cubuk.setAttribute("role", "slider"); cubuk.setAttribute("aria-label", M.ilerleme);
  cubuk.setAttribute("aria-valuemin", "0");
  const ray = el("div", "ko-ray", cubuk), tutamac = el("div", "ko-tutamac", cubuk);
  const ipucu = el("div", "ko-ipucu", cubuk, "<b></b><span></span>");
  const sira = el("div", "ko-sira", kontrol);
  const bOynat = dugme(sira, "ko-oynat", M.oynat, "oynat");
  const bGeri = dugme(sira, "ko-geri", M.saniyeGeri(SAR), "geri");
  const bIleri = dugme(sira, "ko-ileri", M.saniyeIleri(SAR), "ileri");
  const sesGrup = el("div", "ko-ses", sira);
  const bSes = dugme(sesGrup, "ko-sesd", M.sessiz, "ses");
  const sesKay = el("input", null, sesGrup); sesKay.type = "range"; sesKay.min = "0";
  sesKay.max = "1"; sesKay.step = "0.05"; sesKay.setAttribute("aria-label", M.sesDuzeyi);
  const zamanEl = el("div", "ko-zaman", sira, "<b>0:00</b><span> / 0:00</span>");
  const bBolum = el("button", "ko-bolum-ad", sira, "<i></i><b></b>" + svg("ok"));
  bBolum.type = "button"; bBolum.title = M.bolumler; bBolum.setAttribute("aria-haspopup", "menu");
  bBolum.setAttribute("aria-label", M.bolumler);
  el("span", "ko-bos", sira);
  const bAlt = dugme(sira, "ko-altd", M.altyazi, "altyazi");
  const bHiz = dugme(sira, "ko-hizd", M.oynatmaHizi, "hiz");
  const bBol = dugme(sira, "ko-bold", M.bolumler, "bolum");
  const bTema = dugme(sira, "ko-temad", M.tema, "gunes");
  const bTam = dugme(sira, "ko-tamd", M.tamEkran, "tam");
  const menu = el("div", "ko-menu", kok); menu.hidden = true; menu.setAttribute("role", "menu");
  const duyuru = el("div", "ko-duyuru", kok); duyuru.setAttribute("aria-live", "polite");
  const au = el("audio", null, kok); au.preload = "auto";

  // ---------- Sahne tamponları: ortak çekirdek cekirdek.js (editör onizle.js ile aynı) ----------
  function bolumNo(x) {
    for (let i = d.B.length - 1; i >= 0; i--) if (x >= d.B[i].t0) return i; return 0;
  }
  // aktif: görünen yön (her karede zaman mesajı, geçiş efekti). Pasif sıcak yön: tamponlar yüklü
  // kalır, saniyede 1 zaman mesajı alır; döndürünce ilk kare anında doğrudur.
  function sahneYonet(x, Y, aktif) {
    return C.sahneYonet(x, Y, { FPS: d.FPS, aktif, azHareket: d.azHareket });
  }
  addEventListener("message", (ev) => C.hazirMesaj(ev, Object.values(d.Y)));
  function olc() {
    const w = sahne.clientWidth, h = sahne.clientHeight; if (!w || !h) return;
    herY((Y) => {
      const k = Math.min(w / Y.GEN, h / Y.YUK);
      Y.pane.style.width = (Y.GEN * k) + "px"; Y.pane.style.height = (Y.YUK * k) + "px";
      Y.slot.forEach((s) => {
        s.f.style.width = Y.GEN + "px"; s.f.style.height = Y.YUK + "px";
        s.f.style.transform = "scale(" + k + ")";
      });
    });
  }
  if (typeof ResizeObserver !== "undefined") new ResizeObserver(olc).observe(sahne);
  addEventListener("resize", olc);

  // ---------- Yön (yatay ↔ dikey): ses saati ortak, yalnız görünen pane değişir ----------
  const portreMQ = matchMedia("(orientation: portrait)");
  function yonUygula(y) {
    const Y = d.Y[y]; if (!Y || y === d.yon) return;
    const eski = A(); d.yon = y; kok.dataset.yon = y;
    kok.style.setProperty("--ar", Y.GEN + " / " + Y.YUK); olc();
    const r = sahneYonet(d.t, Y, true);
    // Yeni yönün sahnesi henüz yoksa (tembel yükleme) eski pane kalır, yenisi hazır olunca geçer.
    d.bekleyenY = r.hazir || !eski ? null : eski;
    herY((Z) => Z.pane.classList.toggle("ko-pasif", Z !== Y && Z !== d.bekleyenY));
    if (eski) { duyur(y === "dikey" ? M.dikeyGorunum : M.yatayGorunum); goster(); }
    olay("yon", { yon: y, kesintisiz: r.hazir, t: d.t });
  }
  function yonGuncelle() {
    if (!d.yon) return;
    const y = yonIstek(portreMQ.matches, d.Y, sec.yon); if (y && y !== d.yon) yonUygula(y);
  }
  if (portreMQ.addEventListener) portreMQ.addEventListener("change", yonGuncelle);
  addEventListener("resize", yonGuncelle);

  // ---------- Oynatma ----------
  function git(x) {
    d.t = sinirla(x, 0, d.T - 1 / d.FPS); d.bitti = false;
    try { au.currentTime = d.t; }
    catch (e) { /* ses henüz yüklenmedi: t korunur, loadedmetadata eşitler */ }
    goster();
  }
  function oyna() {
    if (!d.hazir) return;
    if (d.bitti || d.t >= d.T - 0.1) git(0);
    hizUygula(); au.volume = d.ses; au.muted = d.sessiz;
    if (Math.abs(au.currentTime - d.t) > 0.05) {
      try { au.currentTime = d.t; } catch (e) { /* yüklenince eşitlenir */ }
    }
    au.play().then(() => {
      d.oynuyor = true; d.basladi = true; poster.classList.add("ko-yok");
      kok.classList.add("ko-oynuyor"); posterNot.textContent = ""; goster();
      duyur(M.oynatiliyor); olay("oynuyor", { t: d.t });
    }).catch(() => {
      d.oynuyor = false; poster.classList.remove("ko-yok");
      posterNot.textContent = M.sesIcinDokun; ikon(buyuk, "oynat");
    });
  }
  function dur(sessizce) {
    if (!d.oynuyor) return;
    au.pause(); d.t = au.currentTime; d.oynuyor = false; kok.classList.remove("ko-oynuyor");
    goster(); if (!sessizce) { duyur(M.duraklatildi); olay("durdu", { t: d.t }); }
  }
  function bitir() {                 // ses dosyası T'den kısa bitebilir: çubuk yine tam dolar
    au.pause(); d.oynuyor = false; d.bitti = true; d.t = d.T - 1 / d.FPS;
    kok.classList.remove("ko-oynuyor");
    poster.classList.remove("ko-yok"); poster.classList.add("ko-bitti"); ikon(buyuk, "tekrar");
    etiket(buyuk, M.tekrarIzle); posterNot.textContent = M.tekrarIzle; goster();
    turboKapat(true); olay("bitti", { t: d.T });
  }
  function oynatDur() { if (d.oynuyor) dur(); else oyna(); }
  function sar(k) { git(d.t + k); goster(); }
  function bolumGit(i) { i = sinirla(i, 0, d.B.length - 1); git(d.B[i].t0 + 0.001); menuKapat(); }
  const hizYazi = (h) => String(h).replace(".", ",") + "×";
  function hizSec(h) {
    d.hiz = h; depoYaz("hiz", h); menuKapat(); turboKapat(true); hizUygula();
    duyur(M.hiz(hizYazi(h)));
  }
  // Basılı tutma 2× (turbo.js): kalıcı hız d.hiz'e dokunmaz, depoya yazılmaz.
  function hizUygula() { au.playbackRate = hizli(d.turbo) ? TURBO_HIZ : d.hiz; }
  function turboCiz() {
    const s = d.turbo, kilit = s.evre === "kilit", ik = turboEl.querySelector(".ko-turbo-ik");
    turboEl.hidden = !hizli(s); turboEl.classList.toggle("ko-kilit", kilit);
    turboEl.style.setProperty("--u", String(kilit ? 1 : s.u));
    const ad = kilit ? "kilit" : "cift";
    if (ik.dataset.ik !== ad) { ik.innerHTML = svg(ad); ik.dataset.ik = ad; }
    etiket(turboEl, kilit ? M.hizKilitli(TURBO_HIZ) : M.hizCarpan(TURBO_HIZ));
  }
  function turboAc() {
    if (!d.oynuyor || !d.hazir) { kapat(d.turbo); return; }
    sure(d.turbo); if (!hizli(d.turbo)) return;
    hizUygula(); turboCiz(); duyur(M.hiz(TURBO_HIZ + "×")); goster();
  }
  function turboKapat(sessizce) {
    const vardi = hizli(d.turbo); clearTimeout(d.turboZ); kapat(d.turbo);
    if (!vardi) return;
    hizUygula(); turboCiz(); if (!sessizce) duyur(M.hiz(hizYazi(d.hiz))); goster();
  }
  function sesUygula() {
    au.volume = d.ses; au.muted = d.sessiz || d.ses === 0; sesKay.value = d.sessiz ? 0 : d.ses;
    ikon(bSes, au.muted ? "sessiz" : d.ses < 0.5 ? "sesAz" : "ses");
    etiket(bSes, au.muted ? M.sesiAc : M.sessiz);
    depoYaz("ses", d.ses); depoYaz("sessiz", d.sessiz);
  }
  function sessizSec(v) {
    d.sessiz = v == null ? !d.sessiz : v; if (!d.sessiz && d.ses === 0) d.ses = 0.5; sesUygula();
  }
  function sesAyar(v) { d.ses = sinirla(v, 0, 1); d.sessiz = d.ses === 0; sesUygula(); }
  function altyaziSec(v) {
    d.altyazi = v == null ? !d.altyazi : v; bAlt.setAttribute("aria-pressed", String(d.altyazi));
    altyaziEl.hidden = !d.altyazi; depoYaz("altyazi", d.altyazi); d.sonAlt = ""; altyaziYaz(d.t);
  }
  function temaSec(ad, sessizce) {
    d.tema = ad === "koyu" ? "koyu" : "acik"; kok.dataset.tema = d.tema;
    herY((Y) => { Y.tema = d.tema; });                       // sonraki sahne adresleri
    sahne.style.background = ZEMIN[d.tema]; ikon(bTema, d.tema === "acik" ? "gunes" : "ay");
    etiket(bTema, d.tema === "acik" ? M.koyuTema : M.acikTema);
    herSlot((s) => {
      try { s.f.contentWindow.postMessage({ tip: "tema", ad: d.tema }, "*"); }
      catch (e) { /* boş tampon */ }
    });
    if (!sessizce) { depoYaz("tema", d.tema); olay("tema", { tema: d.tema }); }
  }
  // Tam ekran: gerçek; yoksa (iPhone Safari) sayfa içi sahte tam ekran. Yatay pakette yön kilidi.
  function tamEkran() {
    if (document.fullscreenElement === kok) return document.exitFullscreen();
    if (kok.classList.contains("ko-tam-sahte")) return sahteKapat();
    if (!kok.requestFullscreen) return sahteAc();
    kok.requestFullscreen().then(() => {                 // yön çifti varsa kilit YOK: dönüş serbest
      const Y = A();
      if (!d.Y.dikey && Y && Y.GEN > Y.YUK && screen.orientation && screen.orientation.lock) {
        screen.orientation.lock("landscape").catch(() => { /* masaüstü: kilit yok */ });
      }
    }).catch(sahteAc);
  }
  function sahteAc() {
    kok.classList.add("ko-tam", "ko-tam-sahte"); document.documentElement.classList.add("ko-kilit");
    tamYaz(true); olc();
  }
  function sahteKapat() {
    kok.classList.remove("ko-tam", "ko-tam-sahte");
    document.documentElement.classList.remove("ko-kilit"); tamYaz(false); olc();
  }
  function tamYaz(acik) {                                // yön çifti: dönen telefon simgesi
    const cift = !!(d.Y.yatay && d.Y.dikey);
    ikon(bTam, acik ? "tamKapat" : cift ? "tamYon" : "tam");
    etiket(bTam, acik ? M.tamEkrandanCik : cift ? M.tamEkranCift : M.tamEkran);
  }
  document.addEventListener("fullscreenchange", () => {
    const acik = document.fullscreenElement === kok; kok.classList.toggle("ko-tam", acik);
    tamYaz(acik); olc();
  });
  function duyur(m) { duyuru.textContent = m; }
  function goster() { d.gizleT = performance.now() + GIZLE_MS; kok.classList.remove("ko-gizli"); }

  // ---------- Menü (bölümler, hız) ----------
  function menuKapat() {
    d.menu = ""; menu.hidden = true;
    [bBol, bHiz, bBolum].forEach((b) => b.setAttribute("aria-expanded", "false"));
  }
  function menuAc(tur, sag) {
    if (d.menu === tur) return menuKapat();
    d.menu = tur; menu.innerHTML = ""; menu.hidden = false; menu.classList.toggle("ko-sag", !!sag);
    if (tur === "bolum") {
      el("h4", null, menu, M.bolumler);
      const bi = bolumNo(d.t);
      d.B.forEach((b, i) => {
        const x = el("button", i === bi ? "on" : "", menu); x.type = "button";
        x.setAttribute("role", "menuitem");
        x.innerHTML = "<span class='no'>" + (i + 1) + "</span><span class='ad'></span>" +
          "<span class='zm'></span>";
        x.querySelector(".ad").textContent = b.ad; x.querySelector(".zm").textContent = mmss(b.t0);
        x.onclick = () => bolumGit(i);
      });
      bBol.setAttribute("aria-expanded", "true"); bBolum.setAttribute("aria-expanded", "true");
    } else {
      el("h4", null, menu, M.oynatmaHizi);
      HIZLAR.forEach((h) => {
        const x = el("button", h === d.hiz ? "on" : "", menu); x.type = "button";
        x.setAttribute("role", "menuitemradio");
        x.setAttribute("aria-checked", String(h === d.hiz));
        x.innerHTML = "<span class='ad'>" + (h === 1 ? M.normal : hizYazi(h)) + "</span>" +
          (h === d.hiz ? "<span class='zm'>✓</span>" : "");
        x.onclick = () => hizSec(h);
      });
      bHiz.setAttribute("aria-expanded", "true");
    }
    const ilk = menu.querySelector("button.on") || menu.querySelector("button");
    if (ilk) ilk.focus();
  }
  document.addEventListener("pointerdown", (ev) => {
    if (!d.menu || menu.contains(ev.target)) return;
    if (!ev.target.closest(".ko-bold, .ko-hizd, .ko-bolum-ad")) menuKapat();
  });

  // ---------- İlerleme çubuğu ----------
  const parcalar = [];
  function cubukKur() {
    ray.innerHTML = ""; parcalar.length = 0;
    d.B.forEach((b) => {
      const p = el("div", "ko-parca", ray); p.style.setProperty("--f", String(b.t1 - b.t0));
      parcalar.push({ b, p, tampon: el("div", "ko-tampon", p), oynanan: el("div", "ko-oynanan", p),
        sT: -1, sB: -1 });
    });
    cubuk.setAttribute("aria-valuemax", String(Math.round(d.T)));
  }
  function cubukZaman(ev) {
    const r = cubuk.getBoundingClientRect();
    return sinirla((ev.clientX - r.left) / r.width, 0, 1) * d.T;
  }
  function ipucuYaz(ev) {
    const x = cubukZaman(ev), r = cubuk.getBoundingClientRect(), b = d.B[bolumNo(x)];
    ipucu.querySelector("b").textContent = b ? b.ad : "";
    ipucu.querySelector("span").textContent = mmss(x);
    const w = ipucu.offsetWidth / 2;
    ipucu.style.left = sinirla(ev.clientX - r.left, w, r.width - w) + "px";
  }
  cubuk.addEventListener("pointerdown", (ev) => {
    if (!d.hazir) return;
    d.surukle = true; d.oynuyorduSurukle = d.oynuyor; cubuk.classList.add("ko-surukle");
    cubuk.setPointerCapture(ev.pointerId); if (d.oynuyor) dur(true);
    git(cubukZaman(ev)); ipucuYaz(ev);
  });
  cubuk.addEventListener("pointermove", (ev) => {
    if (d.hazir) ipucuYaz(ev); if (d.surukle) git(cubukZaman(ev));
  });
  const surukleBitir = () => {
    if (!d.surukle) return; d.surukle = false; cubuk.classList.remove("ko-surukle");
    if (d.oynuyorduSurukle) oyna();
  };
  cubuk.addEventListener("pointerup", surukleBitir);
  cubuk.addEventListener("pointercancel", surukleBitir);
  cubuk.addEventListener("keydown", (ev) => {
    if (ev.key === "ArrowLeft") { sar(-OK); ev.preventDefault(); }
    else if (ev.key === "ArrowRight") { sar(OK); ev.preventDefault(); }
  });

  // ---------- Altyazı ----------
  function altyaziYaz(x) {
    if (!d.altyazi) return;
    const a = d.alt.find((c) => x >= c.t0 && x < c.t1 + 0.35), m = a ? a.metin : "";
    if (m === d.sonAlt) return; d.sonAlt = m; altyaziEl.innerHTML = "";
    if (m) { const s = el("span", null, altyaziEl); s.lang = a.dil || "tr"; s.textContent = m; }
  }

  // ---------- Arayüz döngüsü (her karede yalnız değişen) ----------
  function arayuz(x, y) {
    if (!d.hazir && y.hazir) {
      d.hazir = true; poster.classList.add("ko-hazir");
      posterNot.textContent = d.dokunma ? M.izlemekIcinDokun : "";
      olay("hazir", { sure: d.T, bolumler: d.B.map((b) => ({ ad: b.ad, t0: b.t0, t1: b.t1 })) });
    }
    const sn = Math.floor(x);
    if (sn !== d.sonSn) {
      d.sonSn = sn; zamanEl.querySelector("b").textContent = mmss(x);
      cubuk.setAttribute("aria-valuenow", String(sn));
      cubuk.setAttribute("aria-valuetext", mmss(x) + " / " + mmss(d.T)); olay("zaman", { t: x });
    }
    const buf = au.buffered && au.buffered.length ? au.buffered.end(au.buffered.length - 1) : 0;
    parcalar.forEach((p) => {
      const n = p.b.t1 - p.b.t0, o = sinirla((x - p.b.t0) / n, 0, 1);
      const t = sinirla((buf - p.b.t0) / n, 0, 1);
      if (o !== p.sT) { p.oynanan.style.transform = "scaleX(" + o + ")"; p.sT = o; }
      if (t !== p.sB) { p.tampon.style.transform = "scaleX(" + t + ")"; p.sB = t; }
    });
    tutamac.style.left = (x / d.T * 100) + "%";
    const bi = bolumNo(x);
    if (bi !== d.sonBolum) {
      d.sonBolum = bi; bBolum.querySelector("b").textContent = d.B[bi] ? d.B[bi].ad : "";
      if (d.basladi) duyur(M.bolum(bi + 1) + ": " + d.B[bi].ad);
      olay("bolum", { no: bi, ad: d.B[bi] ? d.B[bi].ad : "", t0: d.B[bi] ? d.B[bi].t0 : 0 });
    }
    altyaziYaz(x);
    const ik = d.oynuyor ? "dur" : "oynat", et = d.oynuyor ? M.duraklat : M.oynat;
    [bOynat, oOynat].forEach((b) => { ikon(b, ik); etiket(b, et); });
    const gizli = d.oynuyor && !d.menu && !d.surukle && !d.kontrolUstunde &&
      performance.now() > d.gizleT;
    kok.classList.toggle("ko-gizli", gizli);
  }
  function dongu() {
    if (d.oynuyor) {
      d.t = au.currentTime; if (d.t >= d.T - 0.03) { d.t = d.T - 1 / d.FPS; bitir(); }
    }
    const Y = A();
    if (Y) {
      const r = sahneYonet(d.t, Y, true);
      herY((Z) => {                                        // sıcak pasif yön ve bekleyen eski yön
        if (Z !== Y && (d.sicak || Z === d.bekleyenY)) sahneYonet(d.t, Z, Z === d.bekleyenY);
      });
      if (d.bekleyenY && r.hazir) {
        d.bekleyenY.pane.classList.add("ko-pasif"); d.bekleyenY = null;
      }
      arayuz(d.t, r);
    }
    requestAnimationFrame(dongu);
  }

  // ---------- Olaylar ----------
  bOynat.onclick = oynatDur; oOynat.onclick = oynatDur; buyuk.onclick = oyna;
  bGeri.onclick = () => sar(-SAR); oGeri.onclick = () => sar(-SAR);
  bIleri.onclick = () => sar(SAR); oIleri.onclick = () => sar(SAR);
  bSes.onclick = () => sessizSec(); sesKay.oninput = () => sesAyar(+sesKay.value);
  bAlt.onclick = () => altyaziSec();
  bTema.onclick = () => temaSec(d.tema === "acik" ? "koyu" : "acik");
  bTam.onclick = tamEkran; bHiz.onclick = () => menuAc("hiz", true);
  bBol.onclick = () => menuAc("bolum", true); bBolum.onclick = () => menuAc("bolum", false);
  let sonTik = 0;
  // Basılı tutma: 500 ms sonra 2×; aşağı sürükleme halkayı doldurur (eşik = sahne boyu × 0,3,
  // 48–96 px); dolunca kilit. Etkinken touchmove engellenir: sayfa kaymaz (dinleyici pasif değil).
  sahne.addEventListener("pointerdown", (ev) => {
    d.turboTik = false;
    if (ev.button !== 0 || ev.target.closest("button") || !d.oynuyor || !d.hazir) return;
    bas(d.turbo, ev.clientX, ev.clientY, sinirla(sahne.clientHeight * 0.3, 48, 96));
    if (d.turbo.evre !== "bekliyor") return;                        // kilitli: sıradan dokunuş
    clearTimeout(d.turboZ); d.turboZ = setTimeout(turboAc, BASILI_MS);
    try { sahne.setPointerCapture(ev.pointerId); } catch (e) { /* yakalama yoksa da sürer */ }
  });
  sahne.addEventListener("pointermove", (ev) => {
    const s = d.turbo; if (s.evre === "bos") return;
    const once = s.evre; hareket(s, ev.clientX, ev.clientY);
    if (s.evre === "bos") clearTimeout(d.turboZ);                 // kaydırma niyeti: iptal
    else if (s.evre === "aktif" || once !== s.evre) {
      turboCiz(); if (s.evre === "kilit") duyur(M.hizKilitlendi(TURBO_HIZ));
    }
  });
  const turboBirak = () => {
    clearTimeout(d.turboZ); const s = d.turbo, vardi = hizli(s);
    if (birak(s)) d.turboTik = true;
    if (vardi && !hizli(s)) { hizUygula(); turboCiz(); duyur(M.hiz(hizYazi(d.hiz))); }
  };
  sahne.addEventListener("pointerup", turboBirak);
  sahne.addEventListener("pointercancel", turboBirak);
  sahne.addEventListener("touchmove", (ev) => { if (hizli(d.turbo)) ev.preventDefault(); },
    { passive: false });
  sahne.addEventListener("contextmenu", (ev) => {
    if (d.turbo.evre !== "bos") ev.preventDefault();
  });
  turboEl.onclick = () => turboKapat();
  sahne.addEventListener("click", (ev) => {
    if (d.turboTik) { d.turboTik = false; return; }               // basılı tutmanın tıkı sayılmaz
    if (ev.target.closest("button") || !d.hazir) return;
    if (d.dokunma) { if (!d.gizliydi) d.gizleT = 0; return; }   // dokunma: kontrolleri aç / kapat
    const simdi = performance.now();
    if (simdi - sonTik < 300) { tamEkran(); sonTik = 0; return; }
    sonTik = simdi; oynatDur();
  });
  kok.addEventListener("pointermove", goster);
  kok.addEventListener("pointerdown", () => {
    d.gizliydi = kok.classList.contains("ko-gizli"); goster();
  });
  kontrol.addEventListener("pointerenter", () => { d.kontrolUstunde = true; });
  kontrol.addEventListener("pointerleave", () => { d.kontrolUstunde = false; goster(); });
  document.addEventListener("keydown", (ev) => {
    if (ev.ctrlKey || ev.metaKey || ev.altKey || !d.hazir) return;
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(ev.target.tagName) && ev.target !== sesKay) return;
    if (!kok.contains(ev.target) && ev.target !== document.body) return;
    const k = ev.key; let ok = true;
    if (k === " " || k === "k" || k === "K") oynatDur();
    else if (k === "j" || k === "J") sar(-SAR);
    else if (k === "l" || k === "L") sar(SAR);
    else if (k === "ArrowLeft") sar(-OK);
    else if (k === "ArrowRight") sar(OK);
    else if (k === "ArrowUp") sesAyar(d.ses + 0.1);
    else if (k === "ArrowDown") sesAyar(d.ses - 0.1);
    else if (k === "m" || k === "M") sessizSec();
    else if (k === "c" || k === "C") altyaziSec();
    else if (k === "f" || k === "F") tamEkran();
    else if (k === "t" || k === "T") temaSec(d.tema === "acik" ? "koyu" : "acik");
    else if (k === "[") { const bi = bolumNo(d.t); bolumGit(d.t - d.B[bi].t0 > 1.5 ? bi : bi - 1); }
    else if (k === "]") bolumGit(bolumNo(d.t) + 1);
    else if (k === "Home") git(0);
    else if (k === "End") git(d.T);
    else if (k === "Escape") {
      if (d.menu) menuKapat(); else if (kok.classList.contains("ko-tam-sahte")) sahteKapat();
      else ok = false;
    }
    else ok = false;
    if (ok) { ev.preventDefault(); goster(); }
  });
  au.addEventListener("ended", () => { if (d.oynuyor) bitir(); });
  au.addEventListener("loadedmetadata", () => {
    if (Math.abs(au.currentTime - d.t) > 0.05) au.currentTime = d.t;
  });
  au.addEventListener("error", () => hataGoster(M.sesHatasi));
  au.addEventListener("waiting", () => kok.classList.add("ko-bekliyor"));
  au.addEventListener("playing", () => kok.classList.remove("ko-bekliyor"));
  au.addEventListener("canplay", () => kok.classList.remove("ko-bekliyor"));

  // ---------- Hata paneli ve veri yükleme ----------
  function hataGoster(m) {
    hata.hidden = false; hata.innerHTML = "";
    el("div", "ko-hata-ik", hata, svg("uyari")); el("p", null, hata).textContent = m;
    const b = el("button", "ko-tekrar", hata, svg("tekrar") + "<span>" + M.tekrarDene + "</span>");
    b.type = "button"; b.onclick = yukle; olay("hata", { mesaj: m });
  }
  function yukle() {
    hata.hidden = true; posterNot.textContent = M.yukleniyor; kok.classList.add("ko-bekliyor");
    herY((Y) => Y.pane.remove()); d.Y = {}; d.yon = ""; d.bekleyenY = null;   // "Tekrar dene"
    const zamanAl = (p) => fetch(p + "zaman.json").then((r) => {
      if (!r.ok) throw new Error("zaman.json " + r.status); return r.json();
    }).then((z) => ({ p, z }));
    Promise.all(d.paketler.map(zamanAl)).then((L) => {
      L.forEach(({ p, z }) => {                            // ilk paket ana; diğeri eş yön çifti
        if (!(z.sahneler || []).length) throw new Error("sahne yok: " + p);
        const ad = yonAdi(z.genislik || 1920, z.yukseklik || 1080), ilk = Object.values(d.Y)[0];
        if (d.Y[ad]) return;
        if (ilk && !ciftUyumlu(ilk.S, z.sahneler)) { konsol(M.yonUyumsuz(p)); return; }
        d.Y[ad] = paneKur(ad, p, z);
      });
      const ilk = Object.values(d.Y)[0], z0 = L[0].z;
      d.FPS = z0.fps || 30; d.T = ilk.S[ilk.S.length - 1].t_son; d.B = bolumListesi(ilk.S);
      const cift = !!(d.Y.yatay && d.Y.dikey);
      d.sicak = cift && (sec.sicak == null ? d.dokunma : !!sec.sicak);   // sicak: iki yön yüklü
      kok.dataset.cift = cift ? "1" : "0";
      if (!sec.tema && depoAl("tema", null) == null && z0.tema) d.tema = z0.tema;
      zamanEl.querySelector("span").textContent = " / " + mmss(d.T);
      au.src = ilk.paket + (z0.anlatim || "ortak/anlatim/anlatim.wav");
      temaSec(d.tema, true); cubukKur(); tamYaz(false);
      yonUygula(yonIstek(portreMQ.matches, d.Y, sec.yon)); kok.classList.remove("ko-bekliyor");
      return fetch(ilk.paket + "ortak/anlatim/altyazi.json").then((r) => (r.ok ? r.json() : []))
        .catch(() => []).then((a) => { d.alt = Array.isArray(a) ? a : []; });
    }).catch((e) => {
      kok.classList.remove("ko-bekliyor"); hataGoster(M.veriHatasi(e.message));
    });
  }

  // ---------- Dil ve etiket güncelleme ----------
  function etiketleriYaz() {
    kok.setAttribute("aria-label", sec.baslik || M.dersVideosu);
    etiket(oGeri, M.saniyeGeri(SAR));
    etiket(oOynat, d.oynuyor ? M.duraklat : M.oynat);
    etiket(oIleri, M.saniyeIleri(SAR));
    etiket(bOynat, d.oynuyor ? M.duraklat : M.oynat);
    etiket(bGeri, M.saniyeGeri(SAR));
    etiket(bIleri, M.saniyeIleri(SAR));
    if (d.bitti) {
      etiket(buyuk, M.tekrarIzle); posterNot.textContent = M.tekrarIzle;
    } else {
      etiket(buyuk, M.oynat);
      if (!d.hazir) posterNot.textContent = M.yukleniyor;
      else if (!d.basladi && d.dokunma) posterNot.textContent = M.izlemekIcinDokun;
    }
    cubuk.setAttribute("aria-label", M.ilerleme);
    sesKay.setAttribute("aria-label", M.sesDuzeyi);
    bBolum.title = M.bolumler; bBolum.setAttribute("aria-label", M.bolumler);
    etiket(bAlt, M.altyazi); etiket(bHiz, M.oynatmaHizi); etiket(bBol, M.bolumler);
    sesUygula(); temaSec(d.tema, true);
    tamYaz(document.fullscreenElement === kok || kok.classList.contains("ko-tam-sahte"));
    turboCiz();
    herSlot((s, Y) => { s.f.title = M.sahneTampon(Y.ad, s.idx + 1); });
    if (d.menu) {                                        // açık menüyü yeni dilde yeniden çiz
      const tur = d.menu, sag = menu.classList.contains("ko-sag"); d.menu = ""; menuAc(tur, sag);
    }
    const tk = hata.querySelector(".ko-tekrar span");
    if (tk) tk.textContent = M.tekrarDene;
  }
  function dilSec(yeni) {
    if (!DILLER.includes(yeni) || yeni === d.dil) return;
    d.dil = yeni; M = sozlukSec(yeni); kok.lang = yeni;
    etiketleriYaz();
    olay("dil", { dil: yeni });
  }

  // ---------- Açılış ----------
  sesUygula(); altyaziSec(d.altyazi); tamYaz(false);
  ikon(bTema, d.tema === "acik" ? "gunes" : "ay"); sahne.style.background = ZEMIN[d.tema];
  yukle(); requestAnimationFrame(dongu);

  return {
    oyna, dur, git, bolumGit, hiz: hizSec, tema: temaSec, tamEkran, altyazi: altyaziSec, kok,
    yon: yonUygula, dil: dilSec,
    durum: () => ({ t: d.t, sure: d.T, oynuyor: d.oynuyor, bolum: bolumNo(d.t), tema: d.tema,
      hazir: d.hazir, yon: d.yon, yonler: Object.keys(d.Y), sicak: d.sicak, dil: d.dil }),
    bolumler: () => d.B.map((b) => ({ ad: b.ad, t0: b.t0, t1: b.t1 })),
  };
}

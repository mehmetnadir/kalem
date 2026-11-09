// Oynatma çekirdeği — kalem editörü (ortak/editor/onizle.js, klasik betik) ve ders oynatıcısı
// (kalem-oynatici.js, modül) AYNI kodu kullanır (PRD P1, K36: editörde görülen = sitede görülen).
// yol.js kalıbı: globalThis.KalemCekirdek; modül `import "./cekirdek.js"` ile yükler, Node testi de.

// Pencere (Y): { S: zaman.json sahneler, paket: "/projeler/<ad>/", tema: "acik"|"koyu",
// slot: [2 tampon], gosterilen }. Tampon: { idx, f: iframe, y: sarmal div (yoksa stil iframe'e,
// kıvrım yok), no, hazir, goster, sonT, sonF, op, z, tr }. Sahne iframe'i ?canli=1&mesaj=1&tbas
// ile yalnız {tip:"zaman", t} mesajıyla çizer.
(function (kok) {
  "use strict";
  var GECIS = 0.4, KIVRIM = 0.6, ONYUKLE = 3;
  function sinirla(x, a, b) { return Math.max(a, Math.min(b, x)); }
  function yumusak(u) { return u * u * (3 - 2 * u); }
  function sahneNo(S, x) {
    for (var i = S.length - 1; i >= 0; i--) if (x >= S[i].t_bas) return i;
    return 0;
  }
  function sahneAdres(Y, i) {
    var s = Y.S[i], sayfa = s.motor === "HyperFrames" ? "/proje/index.html" : "/sayfa.html";
    return Y.paket + "sahneler/" + s.klasor + sayfa + "?canli=1&mesaj=1&tbas=" + s.t_bas +
      (Y.tema === "acik" ? "&tema=acik" : "");
  }
  function slotSifirla(s) {
    s.no = -1; s.hazir = false; s.goster = false; s.sonT = null; s.sonF = -1; s.op = -1; s.z = -1;
    s.tr = null;
  }
  function slotYukle(Y, s, i) {
    s.no = i; s.hazir = false; s.goster = false; s.sonT = null; s.sonF = -1;
    s.f.src = sahneAdres(Y, i);
  }
  function slotBul(Y, i, goster) {
    for (var k = 0; k < Y.slot.length; k++) {
      var s = Y.slot[k]; if (s.no === i && (!goster || s.goster)) return s;
    }
    return null;
  }
  // K37 + açık istisna: sahnenin kendi `gecis` alanı (i-1 → i) kuralı ezer ("fade" → fade;
  // BookFlip, YaprakKivrim… → kıvrım). Alan yoksa bölüm değişimi → kıvrım, bölüm içi → fade;
  // bölüm alanı yoksa kıvrım. Hareket azaltma ve ilk sahne → fade.
  // Veri kanıtı 09.11: 11 pakette tek açık istisna 5→6 fade ("Örnek 3" → "Soru + Form").
  function gecisTur(S, i, azHareket) {
    if (i <= 0 || azHareket) return "fade";
    var a = S[i - 1], b = S[i], g = String(a.gecis || "").toLowerCase();
    if (g === "fade") return "fade";
    if (g && g !== "none" && g !== "-") return "kivrim";
    if (a.bolum != null && b.bolum != null) return a.bolum === b.bolum ? "fade" : "kivrim";
    return "kivrim";
  }
  function stil(s, op, z, tr) {
    var el = s.y || s.f;
    if (s.op !== op) { el.style.opacity = op; s.op = op; }
    if (s.z !== z) { el.style.zIndex = z; s.z = z; }
    if (s.y && s.tr !== tr) {
      s.y.style.transform = tr; s.y.classList.toggle("ko-kivrim", !!tr); s.tr = tr;
    }
  }
  // sec: { FPS (30), aktif (true: görünen pencere — her karede mesaj ve geçiş efekti; false:
  // sıcak pasif yön — tamponlar yüklü, saniyede 1 mesaj), seyrek (ikincil pencere: çift
  // karelerde mesaj), azHareket }.
  // Dönüş: { i, hazir (bu anın sahnesi gösterilebilir), sonraki (hazır sonraki tampon) }.
  function sahneYonet(x, Y, sec) {
    sec = sec || {};
    var FPS = sec.FPS || 30, aktif = sec.aktif !== false, L = Y.S, i = sahneNo(L, x);
    var cur = slotBul(Y, i, true);
    if (cur) Y.gosterilen = cur.idx;
    else if (!slotBul(Y, i, false)) slotYukle(Y, Y.slot[Y.gosterilen === 0 ? 1 : 0], i);
    var tur = gecisTur(L, i, sec.azHareket);
    if (tur === "kivrim" && !Y.slot[0].y) tur = "fade";          // sarmal yoksa kıvrım çizilemez
    var sure = tur === "kivrim" ? KIVRIM : GECIS;
    var icinde = aktif && cur && i > 0 && x - L[i].t_bas < sure;
    var onceki = icinde ? slotBul(Y, i - 1, true) : null;
    // Önyükleme: ikinci tampon geçişteki eski sahneyi gösteriyorsa onu bitene kadar bekler.
    if (cur && !onceki && i + 1 < L.length && x >= L[i + 1].t_bas - ONYUKLE &&
        !slotBul(Y, i + 1, false)) {
      slotYukle(Y, Y.slot[1 - cur.idx], i + 1);
    }
    var u = onceki ? yumusak(sinirla((x - L[i].t_bas) / sure, 0, 1)) : 1;
    for (var k = 0; k < Y.slot.length; k++) {
      var s = Y.slot[k], op = 0, z = 0, tr = "";
      if (cur) {
        if (s === cur) { z = 2; op = onceki && tur === "fade" ? u : 1; }
        else if (s === onceki) {
          op = 1; z = tur === "kivrim" ? 3 : 1;
          if (tur === "kivrim") tr = "perspective(2400px) rotateY(" + (-90 * u).toFixed(2) + "deg)";
        }
      } else if (s.idx === Y.gosterilen) { z = 2; op = 1; }
      stil(s, op, z, tr);
      if (s.hazir && s.no >= 0) {
        var fr = Math.floor((x - L[s.no].t_bas) * FPS + 1e-4);
        var gorunur = s === cur || s === onceki || (!cur && s.idx === Y.gosterilen);
        var sira = !aktif ? fr - s.sonF >= FPS
          : sec.seyrek ? (fr !== s.sonF && (fr & 1) === 0) : fr !== s.sonF;
        if (s.sonT === null || (gorunur && sira)) {
          try { s.f.contentWindow.postMessage({ tip: "zaman", t: x }, "*"); }
          catch (e) { /* iframe henüz belge almadı: sonraki karede yeniden */ }
          s.sonT = x; s.sonF = fr;
        }
      }
    }
    return { i: i, hazir: !!cur, sonraki: i + 1 < L.length ? slotBul(Y, i + 1, true) : null };
  }
  // Sahneden gelen {tip:"hazir", tbas, zamanli}: gönderen tamponu işaretler, pencerenin temasını
  // yollar. Yler = pencere listesi. Dönüş: eşleşen tampon ya da null (başka kaynak).
  function hazirMesaj(ev, Yler) {
    var m = ev.data; if (!m || m.tip !== "hazir") return null;
    var bulunan = null;
    Yler.forEach(function (Y) {
      Y.slot.forEach(function (s) {
        if (s.f.contentWindow !== ev.source) return;
        s.hazir = true; s.sonT = null; if (m.zamanli) s.goster = true; bulunan = s;
        try { s.f.contentWindow.postMessage({ tip: "tema", ad: Y.tema }, "*"); }
        catch (e) { /* pencere kapandı */ }
      });
    });
    return bulunan;
  }
  kok.KalemCekirdek = { GECIS: GECIS, KIVRIM: KIVRIM, ONYUKLE: ONYUKLE, sahneNo: sahneNo,
    sahneAdres: sahneAdres, slotSifirla: slotSifirla, slotYukle: slotYukle, slotBul: slotBul,
    gecisTur: gecisTur, sahneYonet: sahneYonet, hazirMesaj: hazirMesaj };
})(globalThis);

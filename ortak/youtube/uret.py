"""YouTube sürümü ortak parçaları üreticisi (istem YT-1, 15.11.2026; standart D/.claude/docs/youtube-surumu-standart.md).
  /usr/bin/python3 -I uret.py [--tema acik|koyu]
Yazar: giris/proje/index.html · cikis/proje/index.html (HyperFrames, 1920x1080, 30 fps; lib/gsap + assets/logo-{acik,koyu})
       bildirim/kart.html (520x140, şeffaf zemin; kare.mjs PNG'ye çevirir).
Tema değişkenleri tek kaynaktan: emsal dersin ortak/hf_tema.py CSS'i. Ham renk yok; renkler style="fill:var(--…)".
Yazı tipleri gömülü (file:// önizlemede de yüklenir). Söz zamanları <parça>/ses/sureler.json'dan (sabit sn yok).
Sayfa sözleşmesi: ?tema=acik|koyu · ?zemin=1 (yalnız zemin, ölçüm kıyası) · message {tip:"zaman",t} / {tip:"tema",ad}
· window.__seek(t) · window.__hazir (yazı tipi + logo hazır)."""
from __future__ import annotations

import base64
import json
import shutil
import sys
from pathlib import Path

YT = Path(__file__).resolve().parent
K = YT.parent.parent
EMSAL = K / "projeler" / "02-04-ydt-temel" / "ortak"      # yeni kuşak emsal ders: tema, yazı tipi, logo
sys.path.insert(0, str(EMSAL))
import hf_tema  # noqa: E402  (#root koyu, #root.tema-acik açık: --zemin --murekkep --ikincil --vurgu --vurguDolgu …)

W, H, FPS = 1920, 1080, 30
LOGO_EN_BOY = 1920 / 476.3            # logo svg viewBox 1920 x 476,3
LOGO_KAYMA = 68 / 1920                # svg içeriği solda %3,5 boşlukla başlar (emsal yardim.py)
LOGO = {"acik": "yds-publishing-lacivert.svg", "koyu": "yds-publishing-seffaf.svg"}   # emsal ortak/tema.sh
KANAL = "@ydspublishing"
GSAP = K / "motorlar" / "hyperframes" / "node_modules" / "gsap" / "dist" / "gsap.min.js"
VURUS = 0.22                          # kinetik satır (stil §4: 0,18–0,22 sn, back.out(1.6))

# ---- giriş (standart §2: ≤ 3 sn, ilk söz ≤ 1 sn, logo + kanal adı, tek hareket) ----
GIRIS_SURE = 3.0
GIRIS_SES_BAS = 0.50                  # söz logo oturmaya başlarken girer
GIRIS_LOGO_H = 150                    # emsal giriş sahnesi logo damgasıyla aynı boy (LOGO_H u(150))
GIRIS_LOGO_Y = 420
GIRIS_KANAL_TABAN, GIRIS_KANAL_BOY = 668, 48
GIRIS_OTUR = 0.60                     # logo + kanal adı tek grup: 1,12 → 1 ölçek, 0 → 1 opaklık

# ---- çıkış (standart §2: 20 sn, sol yarı söz + logo, sağ yarı x ≥ 960 boş) ----
CIKIS_SURE = 20.0
CIKIS_SES_BAS = 0.50
SOL = 120                             # yazı sol kenarı (emsal AL.x)
SAG_SINIR = 900                       # sol yarı içerik sınırı (960 − 60 pay)
CIKIS_LOGO_H, CIKIS_LOGO_Y = 72, 290  # kanal satırı: logo + @ydspublishing yan yana (huni kanal katmanı düzeni)
LOGO_TABAN = 0.69                     # logo yazısının tabanı / logo boyu (piksel ölçümü, 15.11)
CIKIS_KANAL_BOY = 40                  # logo yazısından küçük (logo harf boyu 0,535 h ≈ 38 px)
SOZ_BOY, SOZ1_TABAN, SOZ2_TABAN = 92, 520, 628
SIRA_BOY, SIRA_TABAN = 42, 742
OK_X0, OK_X1 = 650, 860               # "Sıradaki ders ekranda." sonrası sağı gösteren el oku

# ---- bildirim kartı (standart §2: sessiz, "Beğen · Abone ol", SVG çizim, emoji ve YouTube logosu yok) ----
KART_W, KART_H, KART_R = 520, 140, 30
KART_BOY = 40                         # Fredoka 700
_LAT = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,"
        "U+2193,U+2212,U+2215,U+FEFF,U+FFFD")
_EXT = ("U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,"
        "U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")
FONTLAR = (("Fredoka", 700, "fredoka-%s-700-normal.woff2"), ("Lexend", 500, "lexend-%s-500-normal.woff2"),
           ("Lexend", 700, "lexend-%s-700-normal.woff2"))


def font_css() -> str:
    """@font-face, woff2 gömülü (unicode-range emsal yardim.font_css ile aynı)."""
    out = []
    for aile, agr, kalip in FONTLAR:
        for bolge, ar in (("latin", _LAT), ("latin-ext", _EXT)):
            b64 = base64.b64encode((EMSAL / "font" / (kalip % bolge)).read_bytes()).decode()
            out.append('@font-face{font-family:"%s";font-weight:%d;font-display:block;'
                       'src:url(data:font/woff2;base64,%s) format("woff2");unicode-range:%s;}' % (aile, agr, b64, ar))
    return "\n".join(out)


# Zemin: emsal HF sahneleriyle aynı katmanlar (zemin + gren + vinyet), renkler tema değişkeniyle.
ZEMIN_CSS = ("html,body{margin:0;background:transparent;}"
             "#root{position:relative;width:%dpx;height:%dpx;overflow:hidden;}"
             "#zemin{position:absolute;inset:0;background:var(--zemin);}"
             "#gren{position:absolute;left:0;top:0;opacity:var(--gren);mix-blend-mode:overlay;}"
             "#vinyet{position:absolute;inset:0;background:radial-gradient(circle 1026px at 50%% 50%%,"
             "rgba(0,0,0,0) 47.4%%,rgba(0,0,0,var(--vin)) 100%%);}"
             "#sahne{position:absolute;left:0;top:0;}"
             "#root.yalniz-zemin #icerik{visibility:hidden;}" % (W, H))
ZEMIN_HTML = ('<div id="zemin"></div>'
              '<svg id="gren" width="%d" height="%d" xmlns="http://www.w3.org/2000/svg">'
              '<filter id="grenf" x="0" y="0" width="100%%" height="100%%">'
              '<feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="11"/>'
              '<feColorMatrix type="saturate" values="0"/></filter>'
              '<rect width="%d" height="%d" filter="url(#grenf)"/></svg><div id="vinyet"></div>' % (W, H, W, H))

# Sayfa betiği: tema, zemin bayrağı, zaman ve tema mesajı, hazır bayrağı. Render mesaj almaz; tema dosyaya gömülü.
TEMA_JS = r"""(function () {
  var R = document.getElementById("root"), q = new URLSearchParams(location.search);
  function tema(ad) {
    if (ad !== "acik" && ad !== "koyu") return;
    R.classList.toggle("tema-acik", ad === "acik");
    document.querySelectorAll("image.logo").forEach(function (L) { L.setAttribute("href", L.dataset[ad]); });
  }
  if (q.get("tema")) tema(q.get("tema"));
  if (q.get("zemin") === "1") R.classList.add("yalniz-zemin");
  window.__seek = function (t) { var tl = window.__timelines && window.__timelines.main; if (tl) tl.seek(t, false); };
  addEventListener("message", function (e) {
    var d = e.data || {};
    if (d.tip === "zaman") window.__seek(+d.t || 0);
    else if (d.tip === "tema") tema(d.ad);
  });
  var yukle = function (s) { return new Promise(function (ok) { var i = new Image(); i.onload = i.onerror = ok; i.src = s; }); };
  var resim = Array.prototype.map.call(document.querySelectorAll("image.logo"), function (L) {
    return Promise.all([yukle(L.dataset.acik), yukle(L.dataset.koyu)]); });
  Promise.all([document.fonts.ready].concat(resim)).then(function () {
    if (window.__yerlesim) window.__yerlesim();
    window.__hazir = true; });
})();"""

# GSAP komut çalıştırıcısı (emsal yardim.html alt kümesi: to, set, fromTo, draw).
KOMUT_JS = r"""(function () {
  var tl = gsap.timeline({ paused: true }), $ = function (q) { return document.querySelector(q); };
  C.forEach(function (c) {
    var v;
    if (c.m === "draw") {
      var p = $("#" + c.id), L = p.getTotalLength();
      p.style.strokeDasharray = L + " " + (L + 2); p.style.strokeDashoffset = L;
      tl.set(p, { opacity: 1, immediateRender: false }, c.t);
      tl.to(p, { strokeDashoffset: 0, duration: c.d, ease: "power1.inOut", immediateRender: false }, c.t);
    } else if (c.m === "set") { v = Object.assign({ immediateRender: false }, c.v); tl.set(c.s, v, c.t); }
    else if (c.m === "to") { v = Object.assign({ immediateRender: false }, c.v); tl.to(c.s, v, c.t); }
    else if (c.m === "fromTo") { v = Object.assign({ immediateRender: false }, c.v); tl.fromTo(c.s, c.a, v, c.t); }
  });
  window.__timelines = window.__timelines || {};
  window.__timelines["main"] = tl;
  tl.seek(0, false);
})();"""


def logo_image(kimlik: str, x: float, y: float, yuk: float, tema: str) -> str:
    return ('<image id="%s" class="logo" href="assets/logo-%s.svg" data-acik="assets/logo-acik.svg" '
            'data-koyu="assets/logo-koyu.svg" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>'
            % (kimlik, tema, x, y, yuk * LOGO_EN_BOY, yuk))


def yazi(kimlik: str, x: float, y: float, aile: str, agr: int, boy: int, renk: str, metin: str, ek: str = "") -> str:
    return ('<text id="%s" x="%.1f" y="%.1f" font-family="%s" font-weight="%d" font-size="%d" style="fill:var(--%s)"%s>'
            '%s</text>' % (kimlik, x, y, aile, agr, boy, renk, ek, metin))


def sayfa(sure: float, govde: str, komut: list[dict], tema: str, baslik: str) -> str:
    sinif = ' class="tema-acik"' if tema == "acik" else ""
    veri = json.dumps(sorted(komut, key=lambda c: c["t"]), ensure_ascii=False)
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><title>{baslik}</title>
<style>
{font_css()}
{ZEMIN_CSS}
{hf_tema.CSS}</style></head><body>
<div id="root"{sinif} data-composition-id="main" data-start="0" data-duration="{sure}" data-fps="{FPS}" data-width="{W}" data-height="{H}">
{ZEMIN_HTML}
<svg id="sahne" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<g id="icerik">{govde}</g>
</svg></div>
<script src="lib/gsap.min.js"></script>
<script>var C = {veri};
{KOMUT_JS}</script>
<script>{TEMA_JS}</script>
</body></html>
"""


def varlik(proje: Path) -> None:
    (proje / "lib").mkdir(parents=True, exist_ok=True)
    (proje / "assets").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(GSAP, proje / "lib" / "gsap.min.js")
    for tema, ad in LOGO.items():
        shutil.copyfile(EMSAL / "logo" / ad, proje / "assets" / ("logo-%s.svg" % tema))


def ses(parca: str) -> dict:
    """<parça>/ses/sureler.json cümle 1: {"sure": sn, "sozcukler": [[sözcük, t0, t1], …]} (söz başına göre)."""
    return json.loads((YT / parca / "ses" / "sureler.json").read_text(encoding="utf-8"))[0]


def vur(kimlik: str, x: float, y: float, t: float) -> dict:
    """Kinetik satır: aşağıdan, küçükten vurarak gelir (stil §4); ölçek merkezi satırın sol tabanı."""
    return {"m": "fromTo", "s": "#" + kimlik, "t": round(t, 3),
            "a": {"opacity": 0, "y": 34, "scale": 0.86, "svgOrigin": "%.1f %.1f" % (x, y)},
            "v": {"opacity": 1, "y": 0, "scale": 1, "duration": VURUS, "ease": "back.out(1.6)"}}


def giris(tema: str) -> str:
    """Logo + kanal adı tek grup; tek hareket: 0,00–0,60 sn yerine oturur (1,12 → 1), sonra durgun."""
    s = ses("giris")
    son = GIRIS_SES_BAS + s["sure"]
    assert GIRIS_SES_BAS <= 1.0, "ilk söz 1,0 sn'den sonra"
    assert son <= GIRIS_SURE - 0.2, "söz %.2f sn'de bitiyor; sahne %.1f sn" % (son, GIRIS_SURE)
    lw = GIRIS_LOGO_H * LOGO_EN_BOY
    oy = (GIRIS_LOGO_Y + GIRIS_KANAL_TABAN) / 2
    govde = ('<g id="marka" style="opacity:0">%s%s</g>'
             % (logo_image("logoimg", (W - lw) / 2, GIRIS_LOGO_Y, GIRIS_LOGO_H, tema),
                yazi("kanal-yazi", W / 2, GIRIS_KANAL_TABAN, "Lexend", 700, GIRIS_KANAL_BOY, "ikincil", KANAL,
                     ' text-anchor="middle"')))
    komut = [{"m": "fromTo", "s": "#marka", "t": 0.0,
              "a": {"opacity": 0, "scale": 1.12, "svgOrigin": "%.1f %.1f" % (W / 2, oy)},
              "v": {"opacity": 1, "scale": 1, "duration": GIRIS_OTUR, "ease": "power3.out"}}]
    return sayfa(GIRIS_SURE, govde, komut, tema, "YouTube giriş")


def el_ok(x0: float, y0: float, x1: float, y1: float) -> str:
    """Hafif eğri el çizgisi + ok ucu (tek yol; emsal yardim.el_ok)."""
    k = 22
    return ("M%.1f %.1f Q%.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f"
            % (x0, y0, (x0 + x1) / 2, y0 + 6, x1, y1, x1 - k * 0.88, y1 - k * 0.48, x1, y1, x1 - k * 0.88, y1 + k * 0.48))


def cikis(tema: str) -> str:
    """Sol yarı: kanal satırı (logo + @ydspublishing) + söz satırları; sağ yarı (x ≥ 960) yalnız zemin.
    Satırlar söylendiği anda gelir (sureler.json sözcük başı + CIKIS_SES_BAS); söz bitince ekran durgun."""
    s = ses("cikis")
    soz = s["sozcukler"]
    assert [w[0] for w in soz] == ["Faydalı", "olduysa", "abone", "ol.", "Sıradaki", "ders", "ekranda."], soz

    def T(i: int) -> float:
        return CIKIS_SES_BAS + soz[i][1]

    lw = CIKIS_LOGO_H * LOGO_EN_BOY
    lx = SOL - lw * LOGO_KAYMA
    ky = CIKIS_LOGO_Y + LOGO_TABAN * CIKIS_LOGO_H     # kanal adı tabanı = logo yazısı tabanı
    oky = SIRA_TABAN - 0.34 * SIRA_BOY
    govde = ('<g id="marka" style="opacity:0">%s%s</g>' % (
        logo_image("logoimg", lx, CIKIS_LOGO_Y, CIKIS_LOGO_H, tema),
        yazi("kanal-yazi", lx + lw + CIKIS_LOGO_H * 0.34, ky, "Lexend", 700, CIKIS_KANAL_BOY, "murekkep", KANAL)))
    govde += yazi("soz1", SOL, SOZ1_TABAN, "Fredoka", 700, SOZ_BOY, "murekkep", "Faydalı olduysa", ' style="opacity:0"')
    govde += yazi("soz2", SOL, SOZ2_TABAN, "Fredoka", 700, SOZ_BOY, "vurgu", "abone ol.", ' style="opacity:0"')
    govde += yazi("sira", SOL, SIRA_TABAN, "Lexend", 700, SIRA_BOY, "ikincil", "Sıradaki ders ekranda.",
                  ' style="opacity:0"')
    govde += ('<path id="ok" d="%s" fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" '
              'style="stroke:var(--ikincil);opacity:0"/>' % el_ok(OK_X0, oky, OK_X1, oky))
    govde = govde.replace(' style="fill:var(--murekkep)" style="opacity:0"', ' style="fill:var(--murekkep);opacity:0"')
    govde = govde.replace(' style="fill:var(--vurgu)" style="opacity:0"', ' style="fill:var(--vurgu);opacity:0"')
    govde = govde.replace(' style="fill:var(--ikincil)" style="opacity:0"', ' style="fill:var(--ikincil);opacity:0"')
    assert 'style="opacity:0"' not in govde.split('id="marka"', 1)[1].split("</g>", 1)[1], "çift style"
    komut = [{"m": "fromTo", "s": "#marka", "t": 0.0, "a": {"opacity": 0},
              "v": {"opacity": 1, "duration": 0.30, "ease": "power1.out"}},
             vur("soz1", SOL, SOZ1_TABAN, T(0)), vur("soz2", SOL, SOZ2_TABAN, T(2)),
             vur("sira", SOL, SIRA_TABAN, T(4)),
             {"m": "draw", "id": "ok", "t": round(T(6), 3), "d": 0.35}]
    son = max(c["t"] + (c.get("d") or c.get("v", {}).get("duration", 0)) for c in komut)
    assert son <= CIKIS_SES_BAS + s["sure"] + 0.05, "hareket sözden sonra sürüyor: %.2f" % son
    assert OK_X1 + 6 <= SAG_SINIR, "ok sağ yarıya yakın"
    return sayfa(CIKIS_SURE, govde, komut, tema, "YouTube çıkış")


# Beğen işareti (64x64, elle çizim: bilek + el, başparmak yukarı) ve abone düğmesi biçimi (hap + artı).
BEGEN_YOL = ("M7 29 Q5 29 5 31 L5 56 Q5 58.5 7.5 58.5 L16.5 58.5 Q19 58.5 19 56 L19 31 Q19 28.5 16.5 28.5 Z "
             "M23.5 30 L31 13.5 Q33.2 8.4 38.2 9.6 Q43.4 11.2 42.2 17.4 L39.8 27.2 L52 27.2 Q58.2 27.6 57.4 33.6 "
             "L54.2 52.4 Q53.2 58.2 47 58.4 L23.5 58.4 Z")
ABONE_HAP = (66, 42)


def kart(tema: str) -> str:
    """Sessiz bildirim kartı 520x140 (şeffaf köşe). Yerleşim yazı tipi yüklenince ölçülür (getComputedTextLength):
    [beğen simgesi] Beğen · [abone hapı] Abone ol, yatay ortalı; yazı ve simgeler dikeyde kart ortasında."""
    sinif = ' class="tema-acik"' if tema == "acik" else ""
    hw, hh = ABONE_HAP
    t = 'font-family="Fredoka" font-weight="700" font-size="%d"' % KART_BOY
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><title>Bildirim kartı</title>
<style>
{font_css()}
html,body{{margin:0;background:transparent;}}
#root{{position:relative;width:{KART_W}px;height:{KART_H}px;overflow:hidden;}}
{hf_tema.CSS}</style></head><body>
<div id="root"{sinif}>
<svg id="kart-svg" width="{KART_W}" height="{KART_H}" viewBox="0 0 {KART_W} {KART_H}" xmlns="http://www.w3.org/2000/svg">
<rect id="kart" x="0" y="0" width="{KART_W}" height="{KART_H}" rx="{KART_R}" style="fill:var(--murekkep)"/>
<g id="begen-simge"><path d="{BEGEN_YOL}" stroke-width="4" stroke-linejoin="round"
 style="fill:var(--vurguDolgu);stroke:var(--zemin)"/></g>
<text id="begen" {t} style="fill:var(--zemin)">Beğen</text>
<text id="ayrac" {t} style="fill:var(--zemin);opacity:.55">·</text>
<g id="abone-simge"><rect x="2" y="2" width="{hw - 4}" height="{hh - 4}" rx="{(hh - 4) / 2}" stroke-width="4"
 style="fill:var(--vurguDolgu);stroke:var(--zemin)"/><path d="M{hw / 2} {hh / 2 - 10} L{hw / 2} {hh / 2 + 10} M{hw / 2 - 10} {hh / 2} L{hw / 2 + 10} {hh / 2}"
 stroke-width="5.5" stroke-linecap="round" style="fill:none;stroke:var(--pilMetin)"/></g>
<text id="abone" {t} style="fill:var(--zemin)">Abone ol</text>
</svg></div>
<script>
window.__yerlesim = function () {{
  var $ = function (q) {{ return document.getElementById(q); }}, ORTA = {KART_H / 2};
  var parca = [["begen-simge", 64, 14], ["begen", 0, 20], ["ayrac", 0, 20], ["abone-simge", {hw}, 14], ["abone", 0, 0]];
  var top = 0;
  parca.forEach(function (p) {{ if (!p[1]) p[1] = $(p[0]).getComputedTextLength(); top += p[1] + p[2]; }});
  var x = ({KART_W} - top) / 2;
  parca.forEach(function (p) {{
    var e = $(p[0]);
    if (e.tagName === "text") {{
      e.setAttribute("x", x.toFixed(1));
      e.setAttribute("y", (ORTA + {KART_BOY} * 0.36).toFixed(1));   /* taban: büyük harf ortası kart ortasında */
    }} else {{
      var h = p[0] === "begen-simge" ? 64 : {hh};
      e.setAttribute("transform", "translate(" + x.toFixed(1) + " " + (ORTA - h / 2 - (p[0] === "begen-simge" ? 2 : 0)).toFixed(1) + ")");
    }}
    x += p[1] + p[2];
  }});
}};
</script>
<script>{TEMA_JS}</script>
</body></html>
"""


def tema_arg(argv: list[str]) -> str:
    tema = "acik"
    for i, a in enumerate(argv):
        if a == "--tema" and i + 1 < len(argv):
            tema = argv[i + 1]
    if tema not in ("acik", "koyu"):
        raise SystemExit("tema acik ya da koyu olmalı: " + tema)
    return tema


ONIZLE_DERS = 6.0                     # önizlemede örnek ders karesi süresi (istem: 6 sn)
ONIZLE_KART = (2.0, 3.0, 0.3)         # kart: ders karesinin 2. sn'sinde belirir, 3 sn kalır; giriş/çıkış solma 0,3 sn


def onizle() -> str:
    """onizle.html: giriş (sesiyle) → 6 sn örnek ders karesi (2. sn'de kart, 3 sn) → çıkış (sesiyle).
    Tek dosya, göreli yollar, dış ağ isteği yok. Yer bildirim/yer.json'dan, ders karesi bildirim/ders/'ten."""
    yer = json.loads((YT / "bildirim" / "yer.json").read_text(encoding="utf-8"))
    ders = "02-04-ydt-temel"
    for tema in ("acik", "koyu"):
        assert (YT / "bildirim" / "ders" / ("%s-%s.png" % (ders, tema))).exists(), "önce olc.py yer"
    veri = json.dumps({"giris": GIRIS_SURE, "ders": ONIZLE_DERS, "cikis": CIKIS_SURE, "kart": ONIZLE_KART,
                       "dersKare": "./bildirim/ders/%s-" % ders})
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><title>YouTube sürümü önizleme · giriş, bildirim, çıkış</title>
<style>
{font_css()}
html,body{{margin:0;height:100%;}}
#root{{min-height:100%;background:var(--zemin);color:var(--murekkep);font-family:Lexend;font-weight:500;
  display:flex;flex-direction:column;align-items:center;gap:14px;padding:16px;box-sizing:border-box;}}
#ust{{display:flex;gap:12px;align-items:center;width:min(96vw,1280px);}}
button{{font:700 18px Lexend;padding:8px 18px;border-radius:12px;border:2px solid var(--murekkep);
  background:var(--zemin);color:var(--murekkep);cursor:pointer;}}
#durum{{margin-left:auto;font-size:16px;color:var(--ikincil);}}
#kap{{position:relative;width:min(96vw,1280px);aspect-ratio:16/9;overflow:hidden;border-radius:10px;
  outline:2px solid var(--ikincil);}}
#sahne{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:0 0;}}
#sahne iframe,#sahne img.kat{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;border:0;visibility:hidden;}}
#kart{{position:absolute;left:{yer["x"]}px;top:{yer["y"]}px;width:{yer["w"]}px;height:{yer["h"]}px;opacity:0;}}
#not{{font-size:15px;color:var(--ikincil);}}
{hf_tema.CSS}</style></head><body>
<div id="root" class="tema-acik">
<div id="ust"><button id="bastan">Baştan</button><button id="tema">Açık / Koyu</button><span id="durum"></span></div>
<div id="kap"><div id="sahne">
<iframe id="giris" class="kat" src="./giris/proje/index.html?tema=acik" scrolling="no"></iframe>
<img id="ders" class="kat" alt="örnek ders karesi" src="./bildirim/ders/{ders}-acik.png">
<img id="kart" alt="Beğen · Abone ol" src="./bildirim/bildirim-acik.png">
<iframe id="cikis" class="kat" src="./cikis/proje/index.html?tema=acik" scrolling="no"></iframe>
</div></div>
<div id="not">Giriş {GIRIS_SURE:.1f} sn → örnek ders karesi {ONIZLE_DERS:.0f} sn (kart {ONIZLE_KART[0]:.0f}.–{ONIZLE_KART[0] + ONIZLE_KART[1]:.0f}. sn,
sessiz) → çıkış {CIKIS_SURE:.0f} sn. Kart yeri: {yer["kose"]} x {yer["x"]} y {yer["y"]} ({yer["w"]}×{yer["h"]}).</div>
<audio id="a-giris" src="./giris/ses/giris.wav" preload="auto"></audio>
<audio id="a-cikis" src="./cikis/ses/cikis.wav" preload="auto"></audio>
</div>
<script>
(function () {{
  var S = {veri}, $ = function (q) {{ return document.getElementById(q); }};
  var TOPLAM = S.giris + S.ders + S.cikis, tema = "acik", oynuyor = false, t0 = 0, son = "", faz = "";
  var A = {{ giris: $("a-giris"), cikis: $("a-cikis") }};
  function olcekle() {{ $("sahne").style.transform = "scale(" + ($("kap").clientWidth / {W}) + ")"; }}
  function goster(ad) {{ ["giris", "ders", "cikis"].forEach(function (k) {{ $(k).style.visibility = k === ad ? "visible" : "hidden"; }});
    $("kart").style.visibility = ad === "ders" ? "visible" : "hidden"; }}
  function yolla(ad, t) {{ $(ad).contentWindow.postMessage({{ tip: "zaman", t: t }}, "*"); }}
  function kartOpak(u) {{ var b = S.kart[0], e = b + S.kart[1], g = S.kart[2];
    return Math.max(0, Math.min(1, (u - b) / g, (e - u) / g)); }}
  function ciz(t) {{
    var yeni;
    if (t < S.giris) {{ yeni = "giris"; yolla("giris", t); }}
    else if (t < S.giris + S.ders) {{ yeni = "ders"; $("kart").style.opacity = kartOpak(t - S.giris); }}
    else {{ yeni = "cikis"; yolla("cikis", Math.min(t - S.giris - S.ders, S.cikis - 1 / 30)); }}
    if (yeni !== faz) {{ goster(yeni); if (oynuyor) sesBaslat(yeni, t); faz = yeni; }}
    $("durum").textContent = {{ giris: "giriş", ders: "örnek ders karesi", cikis: "çıkış" }}[yeni] + " · " + t.toFixed(1) + " / " + TOPLAM.toFixed(1) + " sn" + son;
  }}
  function sesBaslat(ad, t) {{
    A.giris.pause(); A.cikis.pause();
    var a = A[ad], yerel = ad === "giris" ? t : t - S.giris - S.ders;
    if (!a) return;
    a.currentTime = Math.max(0, yerel);
    a.play().then(function () {{ son = ""; }}, function () {{ son = " · ses için Baştan'a bas"; }});
  }}
  function dongu() {{
    if (!oynuyor) return;
    var t = (performance.now() - t0) / 1000;
    if (t >= TOPLAM) {{ oynuyor = false; ciz(TOPLAM - 1 / 30); return; }}
    ciz(t); requestAnimationFrame(dongu);
  }}
  function bastan() {{ oynuyor = true; faz = ""; t0 = performance.now(); requestAnimationFrame(dongu); }}
  window.__seek = function (t) {{ oynuyor = false; A.giris.pause(); A.cikis.pause(); faz = ""; ciz(t); }};
  $("bastan").onclick = bastan;
  $("tema").onclick = function () {{
    tema = tema === "acik" ? "koyu" : "acik";
    $("root").classList.toggle("tema-acik", tema === "acik");
    ["giris", "cikis"].forEach(function (k) {{ $(k).contentWindow.postMessage({{ tip: "tema", ad: tema }}, "*"); }});
    $("ders").src = S.dersKare + tema + ".png"; $("kart").src = "./bildirim/bildirim-" + tema + ".png";
  }};
  addEventListener("resize", olcekle); olcekle();
  var yuklenen = 0;
  ["giris", "cikis"].forEach(function (k) {{ $(k).addEventListener("load", function () {{
    if (++yuklenen < 2) return;
    if (new URLSearchParams(location.search).get("tema") === "koyu") $("tema").onclick();   /* ?tema=koyu ile açılış */
    setTimeout(function () {{ window.__hazir = true; bastan(); }}, 400); }}); }});
}})();
</script>
</body></html>
"""


if __name__ == "__main__":
    if "--onizle" in sys.argv:
        (YT / "onizle.html").write_text(onizle(), encoding="utf-8")
        print("yazıldı: onizle.html")
        raise SystemExit(0)
    TEMA = tema_arg(sys.argv)
    for ad, fn in (("giris", giris), ("cikis", cikis)):
        proje = YT / ad / "proje"
        varlik(proje)
        (proje / "index.html").write_text(fn(TEMA), encoding="utf-8")
    (YT / "bildirim").mkdir(exist_ok=True)
    (YT / "bildirim" / "kart.html").write_text(kart(TEMA), encoding="utf-8")
    print("yazıldı: giris/proje/index.html · cikis/proje/index.html · bildirim/kart.html · tema", TEMA)

"""Ortak yardımcılar (İLERİ yatay sahne 06).
Yol verisi, yazı genişliği (fontTools, kerning yok), künye SVG'si, yazı tipi CSS'i."""
import json
import math
import re
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path

from fontTools.ttLib import TTFont

AD = Path(__file__).resolve().parent
ORTAK = AD.parent.parent / "ortak"
FONT = ORTAK / "font"
W, H = 1920, 1080
RENK = {"zemin": "#1b1a17", "murekkep": "#f3efe6", "ikincil": "#c9c2b3", "vurgu": "#f2a93b",
        "logoSari": "#fece00", "kirmizi": "#e0473b"}
LOGO_EN_BOY = 1920 / 476.3
LOGO_KAYMA = 68 / 1920  # logo svg'sinde içerik solda %3,5 boşlukla başlar

_FONT_DOSYA = {("Fredoka", 700): "fredoka-%s-700-normal.woff2", ("Fredoka", 600): "fredoka-%s-600-normal.woff2",
               ("Lexend", 500): "lexend-%s-500-normal.woff2", ("Lexend", 700): "lexend-%s-700-normal.woff2",
               ("Caveat", 700): "caveat-%s-700-normal.woff2"}


@lru_cache(None)
def _font(aile, agirlik, bolge):
    return TTFont(str(FONT / (_FONT_DOSYA[(aile, agirlik)] % bolge)))


def genislik(aile, agirlik, metin, boy):
    """Yazı genişliği px (kerning yok; ±1 px)."""
    toplam = 0.0
    for c in metin:
        for bolge in ("latin", "latin-ext"):
            f = _font(aile, agirlik, bolge)
            g = f.getBestCmap().get(ord(c))
            if g:
                toplam += f["hmtx"][g][0] / f["head"].unitsPerEm * boy
                break
    return toplam


def font_css():
    """@font-face (assets/fonts içindeki woff2'ler; unicode-range Google/fontsource ile aynı)."""
    lat = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
    ext = "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"
    out = []
    for (aile, agr), kalip in _FONT_DOSYA.items():
        for bolge, ar in (("latin", lat), ("latin-ext", ext)):
            out.append('@font-face{font-family:"%s";font-weight:%d;font-display:block;'
                       'src:url("assets/fonts/%s") format("woff2");unicode-range:%s;}'
                       % (aile, agr, kalip % bolge, ar))
    return "\n".join(out)


def font_kopyala(hedef):
    hedef = Path(hedef)
    hedef.mkdir(parents=True, exist_ok=True)
    for kalip in _FONT_DOSYA.values():
        for bolge in ("latin", "latin-ext"):
            ad = kalip % bolge
            (hedef / ad).write_bytes((FONT / ad).read_bytes())


# ---- yol verisi ----
def _sayilar(d):
    return re.findall(r"[MLCZHVmlczhv]|-?\d*\.?\d+(?:e-?\d+)?", d)


def yol_uzunluk(d):
    """M/L/C/Z (mutlak) yolun yaklaşık uzunluğu."""
    t = _sayilar(d)
    i, cx, cy, sx, sy, top = 0, 0.0, 0.0, 0.0, 0.0, 0.0
    cmd = None
    while i < len(t):
        if re.match(r"[A-Za-z]", t[i]):
            cmd = t[i]
            i += 1
            if cmd == "Z":
                top += math.hypot(sx - cx, sy - cy)
                cx, cy = sx, sy
            continue
        if cmd == "M":
            cx, cy = float(t[i]), float(t[i + 1]); sx, sy = cx, cy; i += 2; cmd = "L"
        elif cmd == "L":
            x, y = float(t[i]), float(t[i + 1]); top += math.hypot(x - cx, y - cy); cx, cy = x, y; i += 2
        elif cmd == "C":
            p = [float(v) for v in t[i:i + 6]]
            px, py = cx, cy
            for k in range(1, 9):
                u = k / 8
                a, b, c, e = (1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3
                x = a * cx + b * p[0] + c * p[2] + e * p[4]
                y = a * cy + b * p[1] + c * p[3] + e * p[5]
                top += math.hypot(x - px, y - py); px, py = x, y
            cx, cy = p[4], p[5]; i += 6
        else:
            raise ValueError("yol komutu desteklenmiyor: " + str(cmd))
    return top


def _etiket(e):
    return e.tag.split("}")[-1]


def peeps(ad, en_cok=60, esik=8.0):
    """Open Peeps SVG: beyaz dolguları at, alt yolları ayır, en uzun `en_cok` kadarını (yüz parçaları öncelikli)
    SVG sırasıyla döndür. Çıktı: (genislik, yukseklik, [ {tx,ty,d,uz,yuz} ])."""
    kok = ET.parse(str(ORTAK / "cizim" / "open-peeps" / (ad + ".svg"))).getroot()
    gen = float(re.sub(r"[^\d.]", "", kok.get("width"))); yuk = float(re.sub(r"[^\d.]", "", kok.get("height")))
    yollar = []

    def gez(e, tx, ty, dolgu, yuz):
        tr = e.get("transform")
        if tr:
            m = re.match(r"translate\(([-\d.e]+),\s*([-\d.e]+)\)", tr)
            if not m:
                raise ValueError("translate dışı dönüşüm: " + tr)
            tx += float(m.group(1)); ty += float(m.group(2))
        dolgu = e.get("fill", dolgu)
        yuz = yuz or (e.get("id", "").startswith(("face", "facial")))
        if _etiket(e) == "path" and e.get("d"):
            if dolgu not in ("#FFFFFF", "none"):
                for d in re.split(r"(?=M)", e.get("d")):
                    d = d.strip()
                    if len(d) > 8:
                        yollar.append({"tx": tx, "ty": ty, "d": d, "uz": yol_uzunluk(d), "yuz": yuz})
        for c in e:
            gez(c, tx, ty, dolgu, yuz)

    gez(kok, 0.0, 0.0, "none", False)
    yollar = [y for y in yollar if y["uz"] >= esik or y["yuz"] and y["uz"] >= 4]
    sec = sorted(range(len(yollar)), key=lambda i: (not yollar[i]["yuz"], -yollar[i]["uz"]))[:en_cok]
    return gen, yuk, [yollar[i] for i in sorted(sec)]


def tabler(ad):
    """Tabler ikon yolları (24x24, stroke-width 2): ['d', ...]."""
    s = (ORTAK / "cizim" / "tabler" / (ad + ".svg")).read_text()
    return [d for d in re.findall(r'<path d="([^"]+)"', s) if not d.startswith("M0 0h24v24")]


# ---- künye (SVG, tüm sahnelerde aynı px; BRIEF §3) ----
def ajanda_konumlari():
    """Sağdan sola: Form, Examples, Hook sol kenarları ve nokta merkezleri (Lexend 500 20)."""
    x, out = W - 56.0, {}
    for ad in ("Form", "Examples", "Hook"):
        w = genislik("Lexend", 500, ad, 20)
        out[ad] = {"x": x - w, "w": w}
        x -= w + 36
    return out


def _ajanda(etkin, kimlik):
    """Ajanda metni + etkin sözcüğün solunda nokta. etkin: 0 Hook, 1 Examples, 2 Form."""
    aj = ajanda_konumlari()
    sar, ikn = RENK["vurgu"], RENK["ikincil"]
    ad = ["Hook", "Examples", "Form"]
    tsp = ""
    for i, a in enumerate(ad):
        tsp += '<tspan fill="%s"%s>%s</tspan>' % (sar if i == etkin else ikn, ' dx="36"' if i else "", a)
    nk = aj[ad[etkin]]
    return ('<g id="%s"><text x="%d" y="1030" text-anchor="end" font-family="Lexend" font-weight="500" '
            'font-size="20">%s</text><circle cx="%.2f" cy="1023" r="4" fill="%s"/></g>'
            % (kimlik, W - 56, tsp, nk["x"] - 12, sar))


def kunye_svg(bolum, bolum2, etkin0=1, etkin1=2):
    """Künye: ders adı + seviye (sol üst), bölüm adı (sağ üst; bolum -> bolum2 geçişi), ajanda (sağ alt).
    İki ajanda kopyası üst üste: ku-ajA (etkin0) görünür, ku-ajB (etkin1) opaklık 0; sahne çapraz geçirir."""
    sar, kre, ikn = RENK["vurgu"], RENK["murekkep"], RENK["ikincil"]
    return ('<g id="kunye">'
            '<text id="ku-ders" x="56" y="72" font-family="Fredoka" font-weight="700" font-size="30" fill="%s">'
            'SIMPLE PAST<tspan id="ku-sev" dx="14" font-family="Lexend" font-weight="500" font-size="22" '
            'fill="%s">· YDT ADVANCED</tspan></text>'
            '<text id="ku-bolum" x="1864" y="72" text-anchor="end" font-family="Lexend" font-weight="700" '
            'font-size="24" fill="%s">%s</text>'
            '<text id="ku-bolum2" x="1864" y="72" text-anchor="end" font-family="Lexend" font-weight="700" '
            'font-size="24" fill="%s" style="opacity:0">%s</text>'
            '%s%s</g>' % (kre, ikn, sar, bolum, sar, bolum2, _ajanda(etkin0, "ku-ajA"),
                          _ajanda(etkin1, "ku-ajB").replace('<g id="ku-ajB">', '<g id="ku-ajB" style="opacity:0">')))


def zemin_html():
    return ('<div id="zemin"></div>'
            '<svg id="gren" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">'
            '<filter id="grenf" x="0" y="0" width="100%" height="100%">'
            '<feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="11"/>'
            '<feColorMatrix type="saturate" values="0"/></filter>'
            '<rect width="1920" height="1080" filter="url(#grenf)"/></svg><div id="vinyet"></div>')


ZEMIN_CSS = ("html,body{margin:0;background:#1b1a17;}"
             "#root{position:relative;width:1920px;height:1080px;overflow:hidden;background:#1b1a17;}"
             "#zemin{position:absolute;inset:0;background:#1b1a17;}"
             "#gren{position:absolute;left:0;top:0;opacity:.045;mix-blend-mode:overlay;}"
             "#vinyet{position:absolute;inset:0;background:radial-gradient(circle 1026px at 50% 50%,"
             "rgba(0,0,0,0) 47.4%,rgba(0,0,0,.38) 100%);}"
             ".abs{position:absolute;}")


def cizgi_zamanlari(uzunluklar, t0, t1, en_az=0.04):
    """Sıralı kalem darbeleri: uzunluğa orantılı süre, toplam [t0,t1]. -> [(bas, sure)]."""
    ham = [max(en_az, u) if False else u for u in uzunluklar]
    top = sum(ham) or 1.0
    sure = [max(en_az, (t1 - t0) * u / top) for u in ham]
    k = (t1 - t0) / sum(sure)
    sure = [s * k for s in sure]
    out, t = [], t0
    for s in sure:
        out.append((round(t, 4), round(s, 4))); t += s
    return out


# ---- sahne iskeleti (uret.py ve olay.py ortak kullanır) ----
class Sahne:
    """Komut listesi (GSAP), SVG parçaları ve ses olayları. Zaman yerel sn; tek kaynak uret.py."""

    def __init__(self, t_bas):
        self.defs, self.svg, self.cmd, self.ev, self.tb = [], [], [], [], t_bas

    def S(self, t):
        """Küresel sn -> yerel sn."""
        return round(t - self.tb, 4)

    def olay(self, t, tur, guc):
        self.ev.append({"kare": round(t * 30), "tur": tur, "guc": guc})

    def to(self, sel, t, v):
        self.cmd.append({"m": "to", "s": sel, "t": round(t, 4), "v": v})

    def set(self, sel, t, v):
        self.cmd.append({"m": "set", "s": sel, "t": round(t, 4), "v": v})

    def fromto(self, sel, t, a, v):
        self.cmd.append({"m": "fromTo", "s": sel, "t": round(t, 4), "a": a, "v": v})

    def goster(self, sel, t, d=0.35, dx=0, dy=0, sc=None):
        a = {"opacity": 0, "x": dx, "y": dy}
        v = {"opacity": 1, "x": 0, "y": 0, "duration": d, "ease": "power3.out"}
        if sc is not None:
            a["scale"], v["scale"] = sc, 1
        self.fromto(sel, t, a, v)

    def yol(self, id, d, t, sure, stroke, w=4.0, alfa=1.0, tur="cizgi", guc=0.55, ek=""):
        """Kendini çizen kalem yolu (stroke-dashoffset)."""
        self.svg.append('<path id="%s" d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
                        'stroke-linejoin="round" style="opacity:0" %s/>' % (id, d, stroke, w, ek))
        self.cmd.append({"m": "draw", "id": id, "t": round(t, 4), "d": round(sure, 4), "a": alfa})
        if tur:
            self.olay(t, tur, guc)

    def yazi(self, id, x, y, parcalar, aile, agr, boy, t, d=0.12, anchor="start", tur="tik", guc=0.5, sar_ek=""):
        """Parçalı yazı (soldan açılan kırpma). parcalar: [(metin, renk)]. Döner: (x0, genişlik)."""
        ws = [genislik(aile, agr, p[0], boy) for p in parcalar]
        Wt = sum(ws)
        x0 = x - Wt if anchor == "end" else x
        cx, tx = x0, ""
        for (m, fill), w in zip(parcalar, ws):
            tx += '<text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">%s</text>' % (cx, y, fill, m)
            cx += w
        self.defs.append('<clipPath id="c_%s"><rect id="r_%s" x="%.1f" y="%.1f" width="0" height="%.1f"/></clipPath>'
                         % (id, id, x0 - 8, y - boy * 1.05, boy * 1.5))
        self.svg.append('<g id="%s" font-family="%s" font-weight="%d" font-size="%s" clip-path="url(#c_%s)" %s>%s</g>'
                        % (id, aile, agr, boy, id, sar_ek, tx))
        self.cmd.append({"m": "rev", "id": "r_" + id, "t": round(t, 4), "d": d, "w": round(Wt + 20, 1)})
        if tur:
            self.olay(t, tur, guc)
        return x0, Wt

    def figur(self, ad, kimlik, x, y, yuk, t0, t1, w=3.4, en_cok=60, esik=8.0):
        """Open Peeps figürü kalemle: kutu sol-üst (x, y), yükseklik yuk. Döner: ölçek, genişlik px."""
        gen, yuks, yollar = peeps(ad, en_cok, esik)
        sc = yuk / yuks
        govde = "".join('<path id="%s%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                        % (kimlik, i, p["tx"], p["ty"], p["d"]) for i, p in enumerate(yollar))
        self.svg.append('<g id="%s" transform="translate(%.1f %.1f) scale(%.4f)" fill="none" stroke="%s" '
                        'stroke-width="%.3f" stroke-linecap="round" stroke-linejoin="round">%s</g>'
                        % (kimlik, x, y, sc, RENK["murekkep"], w / sc, govde))
        for i, (b, d) in enumerate(cizgi_zamanlari([p["uz"] for p in yollar], t0, t1)):
            self.cmd.append({"m": "draw", "id": "%s%d" % (kimlik, i), "t": b, "d": d, "a": 1})
            if i < 8:
                self.olay(b, "cizgi", 0.5)
        return sc, gen * sc


def el_daire(cx, cy, rx, ry, kayma=0.0):
    """Hafif eğik, kapanmayan el elipsi (yol d)."""
    pts = []
    for i in range(0, 38):
        a = -2.3 + i * (2 * math.pi * 1.04) / 37
        r = 1 + 0.025 * math.sin(a * 3 + kayma)
        pts.append((cx + rx * r * math.cos(a) - 6 * math.sin(a), cy + ry * r * math.sin(a) + 4 * math.cos(a)))
    return "M%.1f %.1f " % pts[0] + " ".join("L%.1f %.1f" % p for p in pts[1:])


def el_cizgi(x0, y0, x1, y1, egim=3.0):
    """Hafif eğri, hafif eğik el çizgisi."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    return "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x0, y0, mx, my + egim * 2, x1, y1 + egim * 0.4)


def el_kutu(x, y, w, h):
    """Dört kenarı hafif eğri el kutusu (tek yol)."""
    return ("M%.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f "
            "Q%.0f %.0f %.0f %.0f" % (x + 4, y + 3, x + w / 2, y - 3, x + w - 3, y + 1, x + w + 3, y + h / 2,
                                      x + w - 1, y + h - 2, x + w / 2, y + h + 4, x + 5, y + h + 1,
                                      x - 3, y + h / 2, x + 2, y + 6, x + 1, y + 2, x + 5, y + 2))


def el_ok(x0, y0, x1, y1, egim=2.0):
    """Çizgi + ok ucu (tek yol)."""
    a = math.atan2(y1 - y0, x1 - x0)
    k = 22
    return (el_cizgi(x0, y0, x1, y1, egim) + " M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        x1 - k * math.cos(a - 0.5), y1 - k * math.sin(a - 0.5), x1, y1, x1 - k * math.cos(a + 0.5),
        y1 - k * math.sin(a + 0.5)))


def tik_yolu(x, y, b):
    """Onay işareti (✓) yolu: sol-üst (x, y), boyut b."""
    return "M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (x, y + b * 0.5, x + b * 0.35, y + b * 0.85, x + b, y)


def html(s, sure, kunye, alan, logo, ek="", bal_ids=(), W=W, H=H, vin=1026, gruplar=(), dis=()):
    """index.html: zemin + SVG sahne (#icerik içinde #balg ve ek gruplar) + künye + logo + ek (altyazı).
    gruplar: [(grup_id, {eleman_id, ...})]: üyeler ilk üyenin yerinde <g id=grup_id> içine sarılır."""
    gr = [("balg", set(bal_ids))] + [(g, set(i)) for g, i in gruplar]
    kutu, govde, yerlesti, disar = {g: [] for g, _ in gr}, [], set(), []
    for e in s.svg:
        kim = e.split('id="', 1)[1].split('"', 1)[0]
        if kim in dis:       # #icerik dönüşümünden bağımsız öğeler (ör. kod bloğu)
            disar.append(e)
            continue
        for g, ids in gr:
            if kim in ids:
                kutu[g].append(e)
                if g not in yerlesti:
                    govde.append("@@" + g)
                    yerlesti.add(g)
                break
        else:
            govde.append(e)
    diger = [('<g id="%s">%s</g>' % (e[2:], "".join(kutu[e[2:]]))) if e.startswith("@@") else e for e in govde]
    veri = {"cmd": sorted(s.cmd, key=lambda c: c["t"])}
    lx, ly, lw, lh = logo
    zem = zemin_html().replace('width="1920" height="1080"', 'width="%d" height="%d"' % (W, H)).replace(
        'width="1920" height="1080"', 'width="%d" height="%d"' % (W, H))
    css = ZEMIN_CSS.replace("1920px;height:1080px", "%dpx;height:%dpx" % (W, H)).replace(
        "circle 1026px", "circle %dpx" % vin)
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{font_css()}
{css}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{sure}" data-fps="30" data-width="{W}" data-height="{H}">
{zem}
<svg id="sahne" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<defs>{''.join(s.defs)}</defs>
<g id="icerik">{''.join(diger)}</g>
{''.join(disar)}
{kunye}
<image id="logo" href="assets/logo.svg" x="{lx}" y="{ly}" width="{lw:.2f}" height="{lh}"/>
{ek}
</svg></div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var C = {json.dumps(veri, ensure_ascii=False)};
  var tl = gsap.timeline({{ paused: true }});
  var $ = function (q) {{ return document.querySelector(q); }};
  C.cmd.forEach(function (c) {{
    var t = c.t, v;
    if (c.m === "draw") {{
      var p = $("#" + c.id), L = p.getTotalLength();
      p.style.strokeDasharray = L + " " + (L + 2); p.style.strokeDashoffset = L;
      tl.set(p, {{ opacity: c.a, immediateRender: false }}, t);
      tl.to(p, {{ strokeDashoffset: 0, duration: c.d, ease: "power1.inOut", immediateRender: false }}, t);
    }} else if (c.m === "rev") {{
      tl.to("#" + c.id, {{ attr: {{ width: c.w }}, duration: c.d, ease: "power1.out", immediateRender: false }}, t);
    }} else if (c.m === "set") {{
      v = Object.assign({{ immediateRender: false }}, c.v); tl.set(c.s, v, t);
    }} else if (c.m === "to") {{
      v = Object.assign({{ immediateRender: false }}, c.v); tl.to(c.s, v, t);
    }} else if (c.m === "fromTo") {{
      v = Object.assign({{ immediateRender: false }}, c.v); tl.fromTo(c.s, c.a, v, t);
    }}
  }});
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""


def balon_sol(x0, y0, x1, y1, tx, ty):
    """El çizimi konuşma balonu; kuyruk sol kenardan (tx, ty) ucuna uzanır (konuşan solda)."""
    w, h = x1 - x0, y1 - y0
    return ("M%.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f "
            "C%.0f %.0f %.0f %.0f %.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f "
            "C%.0f %.0f %.0f %.0f %.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f L%.0f %.0f L%.0f %.0f "
            "C%.0f %.0f %.0f %.0f %.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f Z" % (
                x0 + 36, y0 + 2, x0 + w * .3, y0 - 6, x0 + w * .65, y0 + 6, x1 - 36, y0 - 2,
                x1 - 10, y0, x1 + 2, y0 + 16, x1, y0 + 38,
                x1 + 4, y0 + h * .4, x1 - 3, y0 + h * .65, x1 + 1, y1 - 38,
                x1 - 2, y1 - 14, x1 - 16, y1 + 2, x1 - 40, y1,
                x1 - w * .3, y1 + 6, x0 + w * .5, y1 - 4, x0 + 40, y1 + 1,
                x0 + 14, y1, x0 + 2, y1 - 10, x0 + 2, y1 - 34, tx, ty, x0 + 1, y1 - 92,
                x0 - 3, y0 + h * .5, x0 + 3, y0 + h * .3, x0 + 1, y0 + 40,
                x0 - 2, y0 + 14, x0 + 14, y0 + 4, x0 + 36, y0 + 2))

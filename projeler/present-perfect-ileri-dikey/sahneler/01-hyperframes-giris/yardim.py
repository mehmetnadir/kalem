"""Ortak yardımcılar (iki HyperFrames sahnesi aynı dosyayı kopya olarak taşır).
Yol verisi, yazı genişliği (fontTools, kerning yok), künye SVG'si, yazı tipi CSS'i."""
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
    """Sağdan sola: Exam, Rule, Hook sol kenarları ve nokta merkezleri (Lexend 500 20)."""
    x, out = W - 56.0, {}
    for ad in ("Exam", "Rule", "Hook"):
        w = genislik("Lexend", 500, ad, 20)
        out[ad] = {"x": x - w, "w": w}
        x -= w + 36
    return out


def kunye_svg(bolum, etkin, ders_class="", gizli=False):
    """Künyenin üç metin bloğu + ajanda + nokta. `gizli`: uçuş sahnesinde başta opaklık 0 (id'lerle yönetilir)."""
    aj = ajanda_konumlari()
    sar, kre, ikn = RENK["vurgu"], RENK["murekkep"], RENK["ikincil"]
    ad = ["Hook", "Rule", "Exam"]
    nokta = aj[ad[etkin]]
    tsp = ""
    for i, a in enumerate(ad):
        tsp += '<tspan id="ku-aj%d" fill="%s"%s>%s</tspan>' % (i, sar if i == etkin else ikn,
                                                              ' dx="36"' if i else "", a)
    s = ('<g id="kunye">'
         '<text id="ku-ders" x="56" y="72" font-family="Fredoka" font-weight="700" font-size="30" fill="%s">'
         'PRESENT PERFECT<tspan id="ku-sev" dx="14" font-family="Lexend" font-weight="500" font-size="22" '
         'fill="%s">· YDT ADVANCED</tspan></text>'
         '<text id="ku-bolum" x="1864" y="72" text-anchor="end" font-family="Lexend" font-weight="700" '
         'font-size="24" fill="%s">%s</text>'
         '<text id="ku-ajanda" x="1864" y="1030" text-anchor="end" font-family="Lexend" font-weight="500" '
         'font-size="20">%s</text>'
         '<circle id="ku-nokta" cx="%.2f" cy="1023" r="4" fill="%s"/></g>'
         % (kre, ikn, sar, bolum, tsp, nokta["x"] - 12, sar))
    return s


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


# ---- coco (Inkscape) SVG: kalem darbesi yolları ----
def _coco_alt_yollar(d):
    """m/M l/L h/H v/V c/C z/Z komutlu yolu alt yollara ayırır: [(noktalar, kapali)] (eğri 5 px'lik doğrulara bölünür)."""
    t = re.findall(r"[MmLlHhVvCcZz]|-?\d*\.?\d+(?:e-?\d+)?", d)
    i, cx, cy, sx, sy, cmd = 0, 0.0, 0.0, 0.0, 0.0, None
    cikti, nok = [], []

    def bitir(kapali):
        nonlocal nok
        if len(nok) > 1:
            cikti.append((nok, kapali))
        nok = []

    while i < len(t):
        if re.match(r"[A-Za-z]", t[i]):
            cmd = t[i]; i += 1
            if cmd in "Zz":
                bitir(True); cx, cy = sx, sy
            continue
        if cmd in "Mm":
            x, y = float(t[i]), float(t[i + 1]); i += 2
            if cmd == "m":
                x += cx; y += cy
            bitir(False); cx, cy, sx, sy = x, y, x, y; nok = [(x, y)]; cmd = "L" if cmd == "M" else "l"
        elif cmd in "Ll":
            x, y = float(t[i]), float(t[i + 1]); i += 2
            if cmd == "l":
                x += cx; y += cy
            nok.append((x, y)); cx, cy = x, y
        elif cmd in "Hh":
            x = float(t[i]); i += 1; x = x + cx if cmd == "h" else x
            nok.append((x, cy)); cx = x
        elif cmd in "Vv":
            y = float(t[i]); i += 1; y = y + cy if cmd == "v" else y
            nok.append((cx, y)); cy = y
        elif cmd in "Cc":
            p = [float(v) for v in t[i:i + 6]]; i += 6
            if cmd == "c":
                p = [p[0] + cx, p[1] + cy, p[2] + cx, p[3] + cy, p[4] + cx, p[5] + cy]
            n = max(6, int(math.hypot(p[4] - cx, p[5] - cy) / 3))
            for k in range(1, n + 1):
                u = k / n
                a, b, c, e = (1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3
                nok.append((a * cx + b * p[0] + c * p[2] + e * p[4], a * cy + b * p[1] + c * p[3] + e * p[5]))
            cx, cy = p[4], p[5]
        else:
            raise ValueError("coco yol komutu desteklenmiyor: " + str(cmd))
    bitir(False)
    return cikti


def _donusum(tr):
    """translate(...) ve matrix(...) zinciri -> (a,b,c,d,e,f)."""
    m = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)

    def carp(p, q):   # p ∘ q (önce q uygulanır)
        return (p[0] * q[0] + p[2] * q[1], p[1] * q[0] + p[3] * q[1], p[0] * q[2] + p[2] * q[3],
                p[1] * q[2] + p[3] * q[3], p[0] * q[4] + p[2] * q[5] + p[4], p[1] * q[4] + p[3] * q[5] + p[5])

    for ad, arg in re.findall(r"(translate|matrix)\(([^)]*)\)", tr or ""):
        v = [float(s) for s in re.split(r"[ ,]+", arg.strip())]
        k = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0) if ad == "translate" else tuple(v)
        m = carp(m, k)
    return m


def coco(ad, kutu, azami=25, kisa_atla=0.02):
    """coco/<ad>.svg -> kutuya sığdırılmış kalem darbesi yolları (svgCiz ile aynı seçim: en uzun `azami`).
    Çıktı: [{d, uz}] uzunluğa göre azalan."""
    s = (ORTAK / "cizim" / "coco" / (ad + ".svg")).read_text()
    alt = []
    for m in re.finditer(r"<path\b([^>]*)>", s, re.S):
        a = m.group(1)
        dm = re.search(r'\sd="([^"]+)"', a)
        if not dm:
            continue
        tm = re.search(r'transform="([^"]*)"', a)
        M = _donusum(tm.group(1) if tm else "")
        for nok, kapali in _coco_alt_yollar(dm.group(1)):
            p = [(M[0] * x + M[2] * y + M[4], M[1] * x + M[3] * y + M[5]) for x, y in nok]
            if kapali:
                p.append(p[0])
            alt.append(p)
    xs = [x for p in alt for x, _ in p]; ys = [y for p in alt for _, y in p]
    bx0, by0, bw, bh = min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)
    k = min(kutu[2] / bw, kutu[3] / bh)
    ox = kutu[0] + (kutu[2] - bw * k) / 2 - bx0 * k
    oy = kutu[1] + (kutu[3] - bh * k) / 2 - by0 * k
    liste = []
    for p in alt:
        q = [(x * k + ox, y * k + oy) for x, y in p]
        uz = sum(math.hypot(q[i + 1][0] - q[i][0], q[i + 1][1] - q[i][1]) for i in range(len(q) - 1))
        if uz > 0.5:
            liste.append({"d": "M " + " L ".join("%.1f %.1f" % c for c in q), "uz": uz})
    top = sum(y["uz"] for y in liste)
    uzun = sorted([y for y in liste if y["uz"] >= top * kisa_atla], key=lambda y: -y["uz"])[:azami]
    return uzun

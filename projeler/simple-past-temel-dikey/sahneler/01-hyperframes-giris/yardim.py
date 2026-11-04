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
W, H = 1080, 1920
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


# ---- künye (SVG, dikey HUD v2; BRIEF-DIKEY §2) ----
ROZET_X, ROZET_Y, ROZET_H = 48, 236, 72
DERS_TABAN = 212
LOGO_YUK = 96


def rozet_genislik(metin="YDT · BASIC"):
    return genislik("Lexend", 700, metin, 36) + 56


def kunye_svg(bolum, ders="SIMPLE PAST"):
    """HUD v2: ders adı Fredoka 700 56 (x 48, taban 212), rozet hapı (y 236, h 72, Lexend 700 36),
    sağ üst "şu an" çipi (y 48, h 80, Lexend 700 40). Logo sahnede ayrı <image> (387 x 96)."""
    sar, kre, zem = RENK["vurgu"], RENK["murekkep"], RENK["zemin"]
    rw = rozet_genislik()
    cw = genislik("Lexend", 700, bolum, 40) + 64
    return ('<g id="kunye">'
            '<text id="ku-ders" x="48" y="%d" font-family="Fredoka" font-weight="700" font-size="56" fill="%s">'
            '%s</text>'
            '<g id="ku-rz"><rect x="%d" y="%d" width="%.1f" height="%d" rx="%d" fill="%s"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" '
            'fill="%s">YDT · BASIC</text></g>'
            '<g id="ku-bolum"><rect x="%.1f" y="48" width="%.1f" height="80" rx="40" fill="none" stroke="%s" '
            'stroke-width="4"/><text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" '
            'font-weight="700" font-size="40" fill="%s">%s</text></g></g>'
            % (DERS_TABAN, kre, ders, ROZET_X, ROZET_Y, rw, ROZET_H, ROZET_H // 2, sar,
               ROZET_X + rw / 2, ROZET_Y + ROZET_H / 2 + 13, zem,
               1032 - cw, cw, sar, 1032 - cw / 2, 48 + 40 + 14, sar, bolum))


def altyazi_satirlari(metin):
    """Altyazı bandı (y 1400-1536): Lexend 500 44, en çok 2 satır, ortalı. -> [(satir, y)]."""
    sat, s = [], ""
    for w in metin.split(" "):
        d = s + " " + w if s else w
        if genislik("Lexend", 500, d, 44) > 984 and s:
            sat.append(s); s = w
        else:
            s = d
    if s:
        sat.append(s)
    while len(sat) > 2:
        son = sat.pop(); sat[1] += " " + son
    y0 = 1400 + (84 if len(sat) == 1 else 56)
    return [(t, y0 + i * 56) for i, t in enumerate(sat)]


def altyazi_svg(parcalar):
    """parcalar: altyazi.json satırları. Her parça <g id="ay<i>"> (opaklık 0; zaman çizelgesi açar)."""
    out = []
    for i, p in enumerate(parcalar):
        t = "".join('<text x="540" y="%d" text-anchor="middle" font-family="Lexend" font-weight="500" '
                    'font-size="44" fill="%s">%s</text>' % (y, RENK["murekkep"], s.replace("&", "&amp;"))
                    for s, y in altyazi_satirlari(p["metin"]))
        out.append('<g id="ay%d" style="opacity:0">%s</g>' % (i, t))
    return "".join(out)


def zemin_html():
    return ('<div id="zemin"></div>'
            '<svg id="gren" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">'
            '<filter id="grenf" x="0" y="0" width="100%" height="100%">'
            '<feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="11"/>'
            '<feColorMatrix type="saturate" values="0"/></filter>'
            '<rect width="1080" height="1920" filter="url(#grenf)"/></svg><div id="vinyet"></div>')


ZEMIN_CSS = ("html,body{margin:0;background:#1b1a17;}"
             "#root{position:relative;width:1080px;height:1920px;overflow:hidden;background:#1b1a17;}"
             "#zemin{position:absolute;inset:0;background:#1b1a17;}"
             "#gren{position:absolute;left:0;top:0;opacity:.045;mix-blend-mode:overlay;}"
             "#vinyet{position:absolute;inset:0;background:radial-gradient(circle 1150px at 50% 50%,"
             "rgba(0,0,0,0) 40%,rgba(0,0,0,.38) 100%);}"
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

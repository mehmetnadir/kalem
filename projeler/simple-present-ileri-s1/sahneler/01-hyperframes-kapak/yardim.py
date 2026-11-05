"""Ortak yardımcılar, DİKEY 1080x1920 (ileri S1 Shorts; iki HyperFrames sahnesi aynı dosyayı kopya olarak taşır).
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
            if not g and c == "\u0130":   # İ alt kümede yok: I genişliğiyle ölç
                g = f.getBestCmap().get(ord("I"))
            if g:
                toplam += f["hmtx"][g][0] / f["head"].unitsPerEm * boy
                break
    return toplam


def i_nokta(onek, boy):
    """Fredoka 700'de İ (U+0130) yok: büyük I + elle nokta. onek: I'dan önceki yazı. -> (merkez dx, nokta
    yarıçapı, nokta merkezi taban çizgisinin kaç px üstünde)."""
    f = _font("Fredoka", 700, "latin")
    g = f["glyf"][f.getBestCmap()[ord("I")]]
    upm = f["head"].unitsPerEm
    r = (g.xMax - g.xMin) / 2 / upm * boy * 1.12
    return (genislik("Fredoka", 700, onek, boy) + (g.xMin + g.xMax) / 2 / upm * boy, r,
            g.yMax / upm * boy + r + 0.07 * boy)


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


# ---- künye (SVG, dikey HUD v2, 05.11 telefon ölçeği; kunye.js ile aynı px) ----
HUD = {"kenar": 48, "logoY": 48, "logoYuk": 96, "dersTaban": 212, "dersYazi": 56, "rozetY": 236,
       "rozetH": 72, "rozetYazi": 36, "cipY": 48, "cipH": 80, "cipYazi": 40, "cipDolgu": 48,
       "altyaziBas": 1400, "altyaziYazi": 44, "altyaziSatir": 56}
ROZETLER = ("YDT · ADVANCED", "GRAMMAR")


def rozet_konumlari():
    """İki rozet hapı: (x, genislik) listesi."""
    x, out = HUD["kenar"], []
    for m in ROZETLER:
        w = genislik("Lexend", 700, m, HUD["rozetYazi"]) + 56
        out.append((x, w)); x += w + 12
    return out


def cip_olcu(metin):
    """Çip: (x, y, genislik, yukseklik) sağ kenar W-48."""
    w = genislik("Lexend", 700, metin, HUD["cipYazi"]) + HUD["cipDolgu"]
    return W - HUD["kenar"] - w, HUD["cipY"], w, HUD["cipH"]


def kunye_svg(cip):
    """Logo (#ku-logo) + ders adı + rozet (#rz0) + çip (#ku-cip). Hepsi kendi id'siyle yönetilir."""
    sar, kre, zem = RENK["vurgu"], RENK["murekkep"], RENK["zemin"]
    h = HUD
    roz = ""
    for i, ((x, w), m) in enumerate(zip(rozet_konumlari(), ROZETLER)):
        roz += ('<g id="rz%d"><rect x="%.1f" y="%d" width="%.1f" height="%d" rx="%d" fill="%s"/>'
                '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" font-weight="700" '
                'font-size="%d" fill="%s">%s</text></g>'
                % (i, x, h["rozetY"], w, h["rozetH"], h["rozetH"] // 2, sar if i == 0 else kre,
                   x + w / 2, h["rozetY"] + h["rozetH"] / 2 + 13, h["rozetYazi"], zem, m))
    cx, cy, cw, ch = cip_olcu(cip)
    chip = ('<g id="ku-cip"><rect id="ku-cipr" x="%.1f" y="%d" width="%.1f" height="%d" rx="%d" fill="none" stroke="%s" '
            'stroke-width="4"/><text id="ku-cipt" x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" '
            'font-weight="700" font-size="%d" fill="%s">%s</text></g>'
            % (cx, cy, cw, ch, ch // 2, sar, cx + cw / 2, cy + ch / 2 + 14, h["cipYazi"], sar, cip))
    ders = ('<text id="ku-ders" x="%d" y="%d" font-family="Fredoka" font-weight="700" font-size="%d" '
            'fill="%s">SIMPLE PRESENT</text>' % (h["kenar"], h["dersTaban"], h["dersYazi"], kre))
    logo = ('<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="%.2f" y="%d" width="%.2f" '
            'height="%d"/></g>' % (h["kenar"], h["logoY"], h["logoYuk"] * LOGO_EN_BOY, h["logoYuk"]))
    return '<g id="kunye">' + ders + roz + chip + logo + '</g>'


def altyazi_satirlari(metin):
    """Lexend 500 44, genişlik 984'e göre en çok 2 satır (kunye.js altyaziCiz ile aynı kural)."""
    sat, s = [], ""
    for w in metin.split(" "):
        d = s + " " + w if s else w
        if genislik("Lexend", 500, d, HUD["altyaziYazi"]) > W - 2 * HUD["kenar"] and s:
            sat.append(s); s = w
        else:
            s = d
    if s:
        sat.append(s)
    while len(sat) > 2:
        son = sat.pop(); sat[1] += " " + son
    return sat


def altyazi_cumleleri(liste):
    """Uzun altyazı parçasını (birden çok cümle) cümle cümle böler; sözcük sayısı tutmazsa parça olduğu gibi kalır.
    Paper.js sahnelerindeki `altyaziSec` (kalem-paper.js) ile aynı kural: cümle, ilk sözcüğünden sonraki cümleye kadar."""
    soz = json.loads((ORTAK / "anlatim" / "sozcukler.json").read_text())
    out = []
    for p in liste:
        cum = re.split(r"(?<=[.!?])\s+", p["metin"])
        kel = [w for w in soz if p["t0"] - 0.05 <= w["t0"] < p["t1"] + 0.05]
        sayi = [len(c.split()) for c in cum]
        if len(cum) < 2 or sum(sayi) != len(kel):
            out.append(p)
            continue
        i = 0
        for k, c in enumerate(cum):
            t0 = kel[i]["t0"]
            i += sayi[k]
            t1 = kel[i]["t0"] if k + 1 < len(cum) else p["t1"]
            out.append({**p, "t0": t0, "t1": t1, "metin": c})
    return out


def altyazi_svg(t_bas, sure, liste):
    """Altyazı bandı (y 1400-1536): her parça bir #al<i> grubu. -> (svg, [[id, aç, kapat], ...]) yerel sn."""
    svg, zaman = "", []
    liste = altyazi_cumleleri(liste)
    for i, a in enumerate(liste):
        ac = max(0.0, a["t0"] - 0.05 - t_bas)
        son = a["t1"] + 0.35
        if i + 1 < len(liste):
            son = min(son, liste[i + 1]["t0"] - 0.05)
        kapat = son - t_bas
        if kapat <= 0 or ac >= sure:
            continue
        sat = altyazi_satirlari(a["metin"])
        y0 = HUD["altyaziBas"] + (84 if len(sat) == 1 else 56)
        txt = "".join('<text x="540" y="%d" text-anchor="middle" font-family="Lexend" font-weight="500" '
                      'font-size="%d" fill="%s">%s</text>'
                      % (y0 + k * HUD["altyaziSatir"], HUD["altyaziYazi"], RENK["murekkep"], t)
                      for k, t in enumerate(sat))
        svg += '<g id="al%d" style="opacity:0">%s</g>' % (i, txt)
        zaman.append(["al%d" % i, round(ac, 3), round(min(kapat, sure), 3)])
    return svg, zaman


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

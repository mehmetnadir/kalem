"""Ortak yardımcılar, DİKEY 1080x1920 (02-04-ydt-temel-s1 sahne 04 hikâye v2 kopyası; simple-present-temel-s3 sahne 05
hikâye karesi A). Yol verisi, yazı genişliği (fontTools, kerning yok), künye SVG'si, yazı tipi CSS'i.
huni v2 (15.11): kanal katmanı (`#kanal`, logo `#logoimg`) + künye satırı (konu + `YDT · TEMEL`) + v2 bantları
(BRIEF-S3 "Kanal katmanı"); çip yok."""
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
def _font(aile: str, agirlik: int, bolge: str):
    return TTFont(str(FONT / (_FONT_DOSYA[(aile, agirlik)] % bolge)))


def genislik(aile: str, agirlik: int, metin: str, boy: float | int) -> float:
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


def font_css() -> str:
    """@font-face (assets/fonts içindeki woff2'ler; unicode-range Google/fontsource ile aynı)."""
    lat = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,"
           "U+2212,U+2215,U+FEFF,U+FFFD")
    ext = ("U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,"
           "U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")
    out = []
    for (aile, agr), kalip in _FONT_DOSYA.items():
        for bolge, ar in (("latin", lat), ("latin-ext", ext)):
            out.append('@font-face{font-family:"%s";font-weight:%d;font-display:block;'
                       'src:url("assets/fonts/%s") format("woff2");unicode-range:%s;}'
                       % (aile, agr, kalip % bolge, ar))
    return "\n".join(out)


def font_kopyala(hedef: str | Path) -> None:
    hedef = Path(hedef)
    hedef.mkdir(parents=True, exist_ok=True)
    for kalip in _FONT_DOSYA.values():
        for bolge in ("latin", "latin-ext"):
            ad = kalip % bolge
            (hedef / ad).write_bytes((FONT / ad).read_bytes())


# ---- yol verisi ----
def _sayilar(d: str) -> list[str]:
    return re.findall(r"[MLCZHVmlczhv]|-?\d*\.?\d+(?:e-?\d+)?", d)


def yol_uzunluk(d: str) -> float:
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


def _etiket(e: ET.Element) -> str:
    return e.tag.split("}")[-1]


def peeps(ad: str, en_cok: int = 60, esik: float = 8.0) -> tuple[float, float, list[dict]]:
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


def tabler(ad: str) -> list[str]:
    """Tabler ikon yolları (24x24, stroke-width 2): ['d', ...]."""
    s = (ORTAK / "cizim" / "tabler" / (ad + ".svg")).read_text()
    return [d for d in re.findall(r'<path d="([^"]+)"', s) if not d.startswith("M0 0h24v24")]


# ---- künye (SVG, dikey HUD v2, 15.11; BRIEF-S1 ile aynı px) ----
HUD = {"kenar": 60, "sagSinir": 960,
       "kanalLogoX": 53.2, "kanalLogoY": 291, "kanalLogoYuk": 48, "kanalLogoEn": 193.5,
       "kanalYaziX": 263, "kanalYaziTaban": 330, "kanalYazi": 42,
       "konuTaban": 420, "konuEnBuyuk": 34, "konuEnKucuk": 28,
       "rozetY": 386, "rozetH": 48, "rozetYazi": 26, "rozetAra": 20, "rozetDolgu": 20,
       "icerikBas": 460, "icerikSon": 1380,
       "altyaziBas": 1400, "altyaziSon": 1550, "altyaziYazi": 44, "altyaziSatir": 56,
       "altyaziMerkez": 510, "altyaziEn": 900}
KONU = "Simple Present"
ROZETLER = ("YDT · TEMEL",)
KANAL_YAZI = "@ydspublishing"


def rozet_hap_eni() -> float:
    return genislik("Lexend", 700, ROZETLER[0], HUD["rozetYazi"]) + 2 * HUD["rozetDolgu"]


def konu_boyu() -> int:
    hap_en = rozet_hap_eni()
    for boy in range(HUD["konuEnBuyuk"], HUD["konuEnKucuk"] - 1, -1):
        if HUD["kenar"] + genislik("Fredoka", 700, KONU, boy) + HUD["rozetAra"] + hap_en <= HUD["sagSinir"]:
            return boy
    return HUD["konuEnKucuk"]


def rozet_konumlari() -> list[tuple[float, float]]:
    x = HUD["kenar"] + genislik("Fredoka", 700, KONU, konu_boyu()) + HUD["rozetAra"]
    out: list[tuple[float, float]] = []
    for m in ROZETLER:
        w = genislik("Lexend", 700, m, HUD["rozetYazi"]) + 2 * HUD["rozetDolgu"]
        out.append((x, w))
        x += w + 12
    return out


def kunye_svg(cip: str | None = None) -> str:
    """Kanal katmanı + konu + rozet(ler). Çip çizilmez (cip geriye uyum için)."""
    h = HUD
    kanal = (
        '<g id="kanal">'
        '<image id="logoimg" href="assets/logo.svg" x="%.1f" y="%d" width="%.1f" height="%d"/>'
        '<text id="kanal-yazi" x="%d" y="%d" font-family="Lexend" font-weight="700" font-size="%d" '
        'fill="%s">%s</text>'
        '</g>'
        % (h["kanalLogoX"], h["kanalLogoY"], h["kanalLogoEn"], h["kanalLogoYuk"],
           h["kanalYaziX"], h["kanalYaziTaban"], h["kanalYazi"], RENK["murekkep"], KANAL_YAZI)
    )
    konu = (
        '<text id="ku-konu" x="%d" y="%d" font-family="Fredoka" font-weight="700" font-size="%d" '
        'fill="%s">%s</text>'
        % (h["kenar"], h["konuTaban"], konu_boyu(), RENK["murekkep"], KONU)
    )
    roz = ""
    rozet_taban = int(h["rozetY"] + h["rozetH"] / 2 + 9)
    for i, ((x, w), m) in enumerate(zip(rozet_konumlari(), ROZETLER)):
        roz += (
            '<g id="rz%d">'
            '<rect x="%.1f" y="%d" width="%.1f" height="%d" rx="%d" fill="%s"/>'
            '<text x="%.1f" y="%d" text-anchor="middle" font-family="Lexend" font-weight="700" '
            'font-size="%d" fill="%s">%s</text>'
            '</g>'
            % (i, x, h["rozetY"], w, h["rozetH"], h["rozetH"] // 2, RENK["vurgu"],
               x + w / 2, rozet_taban, h["rozetYazi"], RENK["zemin"], m)
        )
    return '<g id="kunye">' + kanal + konu + roz + '</g>'


def altyazi_satirlari(metin: str) -> list[str]:
    """Lexend 500 44, satır genişliği <= altyaziEn (900); sözcük sözcük sar; en çok 2 satır."""
    sat: list[str] = []
    s = ""
    for w in metin.split(" "):
        d = s + " " + w if s else w
        if genislik("Lexend", 500, d, HUD["altyaziYazi"]) > HUD["altyaziEn"] and s:
            sat.append(s)
            s = w
        else:
            s = d
    if s:
        sat.append(s)
    while len(sat) > 2:
        son = sat.pop()
        sat[1] += " " + son
    return sat


def altyazi_cumleleri(liste: list[dict]) -> list[dict]:
    """Uzun altyazı parçasını (birden çok cümle) cümle cümle böler; sözcük sayısı tutmazsa parça olduğu gibi kalır.
    Paper.js sahnelerindeki `altyaziSec` (kalem-paper.js) ile aynı kural:
    cümle, ilk sözcüğünden sonraki cümleye kadar."""
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


def altyazi_svg(t_bas: float, sure: float, liste: list[dict]) -> tuple[str, list[list], list[list]]:
    """Altyazı bandı (y 1400-1550, x 60-960) + karaoke altçizgisi.
    -> (svg, [["al<i>", ac, kapat], ...], [["ak<i>_<j>", ac, kapat, uzunluk], ...]) yerel sn."""
    svg_parcalar: list[str] = []
    zaman: list[list] = []
    karaoke: list[list] = []
    liste = altyazi_cumleleri(liste)

    soz_dosya = ORTAK / "anlatim" / "sozcukler.json"
    sozcukler = json.loads(soz_dosya.read_text()) if soz_dosya.exists() else []

    ayazi = HUD["altyaziYazi"]
    murekkep = RENK["murekkep"]
    vurgu = RENK["vurgu"]

    for i, a in enumerate(liste):
        t0 = a["t0"]
        t1 = a["t1"]
        ac = max(0.0, t0 - 0.05 - t_bas)
        son = t1 + 0.35
        if i + 1 < len(liste):
            son = min(son, liste[i + 1]["t0"] - 0.05)
        kapat = son - t_bas
        if kapat <= 0 or ac >= sure:
            continue
        parca_kapat = min(kapat, sure)
        zaman.append(["al%d" % i, round(ac, 3), round(parca_kapat, 3)])

        satirlar = altyazi_satirlari(a["metin"])
        y0 = HUD["altyaziBas"] + (84 if len(satirlar) == 1 else 56)

        satir_elemanlari: list[str] = []
        satir_bilgileri: list[dict] = []

        for k, sat in enumerate(satirlar):
            satir_y = y0 + k * HUD["altyaziSatir"]
            satir_eni = genislik("Lexend", 500, sat, ayazi)
            satir_x = HUD["altyaziMerkez"] - satir_eni / 2
            assert 60 <= satir_x and satir_x + satir_eni <= 960, (
                "Satır x aralığı 60-960 dışına çıktı: %.1f..%.1f" % (satir_x, satir_x + satir_eni)
            )
            satir_elemanlari.append(
                '<text x="%.1f" y="%d" text-anchor="start" font-family="Lexend" font-weight="500" '
                'font-size="%d" fill="%s" style="font-kerning:none">%s</text>'
                % (satir_x, satir_y, ayazi, murekkep, sat)
            )
            satir_bilgileri.append({"satir": sat, "x": satir_x, "y": satir_y})

        # Karaoke altçizgileri
        w_list = [w for w in sozcukler if t0 - 0.05 <= w["t0"] < t1 + 0.05]
        satir_sozcukleri = []
        for k, sb in enumerate(satir_bilgileri):
            sw_list = sb["satir"].split(" ")
            for s_idx, sw in enumerate(sw_list):
                satir_sozcukleri.append((k, s_idx, sw, sb))

        cizgi_elemanlari: list[str] = []
        if len(w_list) == len(satir_sozcukleri):
            for j, ((k, s_idx, sw, sb), w) in enumerate(zip(satir_sozcukleri, w_list)):
                sw_list = sb["satir"].split(" ")
                onceki = (" ".join(sw_list[:s_idx]) + " ") if s_idx > 0 else ""
                x1 = sb["x"] + (genislik("Lexend", 500, onceki, ayazi) if onceki else 0.0)
                sw_temiz = sw.rstrip(".,:;!?")
                x2 = x1 + genislik("Lexend", 500, sw_temiz, ayazi)
                y1 = sb["y"] + 12
                y2 = y1
                cizgi_ac = round(w["t0"] - t_bas, 3)
                if j + 1 < len(w_list):
                    cizgi_kapat = round(w_list[j + 1]["t0"] - t_bas, 3)
                else:
                    cizgi_kapat = round(min(w["t1"] - t_bas + 0.25, parca_kapat), 3)
                uzunluk = round(x2 - x1, 2)
                karaoke.append(["ak%d_%d" % (i, j), cizgi_ac, cizgi_kapat, uzunluk])
                cizgi_elemanlari.append(
                    '<line id="ak%d_%d" x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                    'stroke-width="6" stroke-linecap="round" style="opacity:0"/>'
                    % (i, j, x1, y1, x2, y2, vurgu)
                )

        svg_parcalar.append(
            '<g id="al%d" style="opacity:0">' % i + "".join(satir_elemanlari) + "".join(cizgi_elemanlari) + "</g>"
        )

    return "".join(svg_parcalar), zaman, karaoke


def zemin_html() -> str:
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


def cizgi_zamanlari(uzunluklar: list[float], t0: float, t1: float, en_az: float = 0.04) -> list[tuple[float, float]]:
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

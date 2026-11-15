"""02-04-ydt-temel-s2 huni v2: kanal katmanı (y 280–350) + künye (y 360–450); değerler BRIEF-S2.md Yerleşim tablosu."""
from __future__ import annotations

import json
import math
import re
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path
from typing import Any

from fontTools.ttLib import TTFont

AD = Path(__file__).resolve().parent
ORTAK = AD.parent.parent / "ortak"
FONT = ORTAK / "font"
W, H = 1080, 1920
RENK = {
    "zemin": "#1b1a17",
    "murekkep": "#f3efe6",
    "ikincil": "#c9c2b3",
    "vurgu": "#f2a93b",
    "logoSari": "#fece00",
    "kirmizi": "#e0473b",
}
LOGO_EN_BOY = 1920 / 476.3
LOGO_KAYMA = 68 / 1920  # logo svg'sinde içerik solda %3,5 boşlukla başlar

_FONT_DOSYA = {
    ("Fredoka", 700): "fredoka-%s-700-normal.woff2",
    ("Fredoka", 600): "fredoka-%s-600-normal.woff2",
    ("Lexend", 500): "lexend-%s-500-normal.woff2",
    ("Lexend", 700): "lexend-%s-700-normal.woff2",
    ("Caveat", 700): "caveat-%s-700-normal.woff2",
}


@lru_cache(None)
def _font(aile: str, agirlik: int, bolge: str) -> TTFont:
    return TTFont(str(FONT / (_FONT_DOSYA[(aile, agirlik)] % bolge)))


def genislik(aile: str, agirlik: int, metin: str, boy: float) -> float:
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
    lat = (
        "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,"
        "U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
    )
    ext = (
        "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+1EF2-1EFF,"
        "U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"
    )
    out: list[str] = []
    for (aile, agr), kalip in _FONT_DOSYA.items():
        for bolge, ar in (("latin", lat), ("latin-ext", ext)):
            out.append(
                '@font-face{font-family:"%s";font-weight:%d;font-display:block;'
                'src:url("assets/fonts/%s") format("woff2");unicode-range:%s;}'
                % (aile, agr, kalip % bolge, ar)
            )
    return "\n".join(out)


def font_kopyala(hedef: Path | str) -> None:
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
            cx, cy = float(t[i]), float(t[i + 1])
            sx, sy = cx, cy
            i += 2
            cmd = "L"
        elif cmd == "L":
            x, y = float(t[i]), float(t[i + 1])
            top += math.hypot(x - cx, y - cy)
            cx, cy = x, y
            i += 2
        elif cmd == "C":
            p = [float(v) for v in t[i : i + 6]]
            px, py = cx, cy
            for k in range(1, 9):
                u = k / 8
                a = (1 - u) ** 3
                b = 3 * u * (1 - u) ** 2
                c = 3 * u * u * (1 - u)
                e = u ** 3
                x = a * cx + b * p[0] + c * p[2] + e * p[4]
                y = a * cy + b * p[1] + c * p[3] + e * p[5]
                top += math.hypot(x - px, y - py)
                px, py = x, y
            cx, cy = p[4], p[5]
            i += 6
        else:
            raise ValueError("yol komutu desteklenmiyor: " + str(cmd))
    return top


def _etiket(e: ET.Element) -> str:
    return e.tag.split("}")[-1]


def peeps(ad: str, en_cok: int = 60, esik: float = 8.0) -> tuple[float, float, list[dict[str, Any]]]:
    """Open Peeps SVG: beyaz dolguları at, alt yolları ayır, en uzun `en_cok` kadarını (yüz parçaları öncelikli)
    SVG sırasıyla döndür. Çıktı: (genislik, yukseklik, [ {tx,ty,d,uz,yuz} ])."""
    kok = ET.parse(str(ORTAK / "cizim" / "open-peeps" / (ad + ".svg"))).getroot()
    gen = float(re.sub(r"[^\d.]", "", kok.get("width", "0")))
    yuk = float(re.sub(r"[^\d.]", "", kok.get("height", "0")))
    yollar: list[dict[str, Any]] = []

    def gez(e: ET.Element, tx: float, ty: float, dolgu: str, yuz: bool) -> None:
        tr = e.get("transform")
        if tr:
            m = re.match(r"translate\(([-\d.e]+),\s*([-\d.e]+)\)", tr)
            if not m:
                raise ValueError("translate dışı dönüşüm: " + tr)
            tx += float(m.group(1))
            ty += float(m.group(2))
        dolgu = e.get("fill", dolgu)
        yuz = yuz or (e.get("id", "").startswith(("face", "facial")))
        if _etiket(e) == "path" and e.get("d"):
            if dolgu not in ("#FFFFFF", "none"):
                for d in re.split(r"(?=M)", e.get("d", "")):
                    d = d.strip()
                    if len(d) > 8:
                        yollar.append({"tx": tx, "ty": ty, "d": d, "uz": yol_uzunluk(d), "yuz": yuz})
        for c in e:
            gez(c, tx, ty, dolgu, yuz)

    gez(kok, 0.0, 0.0, "none", False)
    yollar = [y for y in yollar if y["uz"] >= esik or (y["yuz"] and y["uz"] >= 4)]
    sec = sorted(range(len(yollar)), key=lambda i: (not yollar[i]["yuz"], -yollar[i]["uz"]))[:en_cok]
    return gen, yuk, [yollar[i] for i in sorted(sec)]


def tabler(ad: str) -> list[str]:
    """Tabler ikon yolları (24x24, stroke-width 2): ['d', ...]."""
    s = (ORTAK / "cizim" / "tabler" / (ad + ".svg")).read_text(encoding="utf-8")
    return [d for d in re.findall(r'<path d="([^"]+)"', s) if not d.startswith("M0 0h24v24")]


# ---- künye (SVG, dikey HUD v2; BRIEF-S2.md Yerleşim tablosu ile aynı px) ----
HUD = {
    "kenar": 48,
    "logoYuk": 48,
    "logoY": 291,
    "kanalX": 263,
    "kanalTaban": 330,
    "kanalYazi": 42,
    "konuX": 60,
    "konuTaban": 420,
    "konuUst": 34,
    "konuAlt": 28,
    "rozetY": 386,
    "rozetH": 48,
    "rozetAra": 20,
    "rozetYazi": 26,
    "rozetDolgu": 20,
    "sagSinir": 960,
    "altyaziBas": 1400,
    "altyaziYazi": 44,
    "altyaziSatir": 56,
}
KONU = "Simple Present vs Present Continuous"
ROZETLER = ("YDT · BASIC",)


def konu_boyu() -> int:
    """34'ten 28'e inerek rozetle birlikte sagSinir'a (960) sığan ilk tam sayı yazı boyu."""
    rozet_g = genislik("Lexend", 700, ROZETLER[0], HUD["rozetYazi"]) + 2 * HUD["rozetDolgu"]
    for boy in range(HUD["konuUst"], HUD["konuAlt"] - 1, -1):
        toplam_g = HUD["konuX"] + genislik("Fredoka", 700, KONU, boy) + HUD["rozetAra"] + rozet_g
        if toplam_g <= HUD["sagSinir"]:
            return boy
    raise AssertionError(f"Konu başlığı [{HUD['konuAlt']}, {HUD['konuUst']}] aralığında sağ sınıra sığmadı")


def rozet_konumlari() -> list[tuple[float, float]]:
    """Tek rozet hapı konumu: [(x, genişlik)]."""
    boy = konu_boyu()
    x = HUD["konuX"] + genislik("Fredoka", 700, KONU, boy) + HUD["rozetAra"]
    out: list[tuple[float, float]] = []
    for r in ROZETLER:
        w = genislik("Lexend", 700, r, HUD["rozetYazi"]) + 2 * HUD["rozetDolgu"]
        out.append((x, w))
        x += w + 12
    return out


def kunye_svg() -> str:
    """Kanal katmanı (#kanal) ve künye (#kunye) SVG grubu."""
    sar, kre, zem = RENK["vurgu"], RENK["murekkep"], RENK["zemin"]
    h = HUD
    lw = h["logoYuk"] * LOGO_EN_BOY
    lx = h["konuX"] - lw * LOGO_KAYMA
    logo = (
        f'<image id="logoimg" href="assets/logo.svg" x="{lx:.2f}" y="{h["logoY"]}" '
        f'width="{lw:.2f}" height="{h["logoYuk"]}"/>'
    )
    kanal_ad = (
        f'<text id="kanal-ad" x="{h["kanalX"]}" y="{h["kanalTaban"]}" '
        f'font-family="Lexend" font-weight="700" font-size="{h["kanalYazi"]}" fill="{kre}">@ydspublishing</text>'
    )
    kanal = f'<g id="kanal">{logo}{kanal_ad}</g>'
    k_boy = konu_boyu()
    konu_txt = (
        f'<text id="ku-konu" x="{h["konuX"]}" y="{h["konuTaban"]}" '
        f'font-family="Fredoka" font-weight="700" font-size="{k_boy}" fill="{kre}">{KONU}</text>'
    )
    roz = ""
    for i, ((x, w), m) in enumerate(zip(rozet_konumlari(), ROZETLER)):
        roz += (
            f'<g id="rz{i}">'
            f'<rect x="{x:.1f}" y="{h["rozetY"]}" width="{w:.1f}" height="{h["rozetH"]}" '
            f'rx="{h["rozetH"] // 2}" fill="{sar}"/>'
            f'<text x="{x + w / 2:.1f}" y="419" text-anchor="middle" '
            f'font-family="Lexend" font-weight="700" font-size="{h["rozetYazi"]}" fill="{zem}">{m}</text>'
            f'</g>'
        )
    return f'<g id="kunye">{kanal}{konu_txt}{roz}</g>'


def altyazi_satirlari(metin: str) -> list[str]:
    """Lexend 500 44, genişlik 984'e göre en çok 2 satır (kunye.js altyaziCiz ile aynı kural)."""
    sat: list[str] = []
    s = ""
    for w in metin.split(" "):
        d = s + " " + w if s else w
        if genislik("Lexend", 500, d, HUD["altyaziYazi"]) > W - 2 * HUD["kenar"] and s:
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


def altyazi_cumleleri(liste: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Uzun altyazı parçasını (birden çok cümle) cümle cümle böler; sözcük sayısı tutmazsa parça olduğu gibi kalır.
    Paper.js sahnelerindeki `altyaziSec` (kalem-paper.js) ile aynı kural:
    cümle, ilk sözcüğünden sonraki cümleye kadar."""
    soz = json.loads((ORTAK / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    out: list[dict[str, Any]] = []
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


def altyazi_svg(t_bas: float, sure: float, liste: list[dict[str, Any]]) -> tuple[str, list[list[Any]]]:
    """Altyazı bandı (y 1400-1536): her parça bir #al<i> grubu. -> (svg, [[id, aç, kapat], ...]) yerel sn."""
    svg = ""
    zaman: list[list[Any]] = []
    parcalar = altyazi_cumleleri(liste)
    for i, a in enumerate(parcalar):
        ac = max(0.0, a["t0"] - 0.05 - t_bas)
        son = a["t1"] + 0.35
        if i + 1 < len(parcalar):
            son = min(son, parcalar[i + 1]["t0"] - 0.05)
        kapat = son - t_bas
        if kapat <= 0 or ac >= sure:
            continue
        sat = altyazi_satirlari(a["metin"])
        y0 = HUD["altyaziBas"] + (84 if len(sat) == 1 else 56)
        txt = "".join(
            f'<text x="540" y="{y0 + k * HUD["altyaziSatir"]}" text-anchor="middle" '
            f'font-family="Lexend" font-weight="500" font-size="{HUD["altyaziYazi"]}" '
            f'fill="{RENK["murekkep"]}">{t}</text>'
            for k, t in enumerate(sat)
        )
        svg += f'<g id="al{i}" style="opacity:0">{txt}</g>'
        zaman.append([f"al{i}", round(ac, 3), round(min(kapat, sure), 3)])
    return svg, zaman


def zemin_html() -> str:
    return (
        '<div id="zemin"></div>'
        '<svg id="gren" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">'
        '<filter id="grenf" x="0" y="0" width="100%" height="100%">'
        '<feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="11"/>'
        '<feColorMatrix type="saturate" values="0"/></filter>'
        '<rect width="1080" height="1920" filter="url(#grenf)"/></svg><div id="vinyet"></div>'
    )


ZEMIN_CSS = (
    "html,body{margin:0;background:#1b1a17;}"
    "#root{position:relative;width:1080px;height:1920px;overflow:hidden;background:#1b1a17;}"
    "#zemin{position:absolute;inset:0;background:#1b1a17;}"
    "#gren{position:absolute;left:0;top:0;opacity:.045;mix-blend-mode:overlay;}"
    "#vinyet{position:absolute;inset:0;background:radial-gradient(circle 1026px at 50% 50%,"
    "rgba(0,0,0,0) 47.4%,rgba(0,0,0,.38) 100%);}"
    ".abs{position:absolute;}"
)


def cizgi_zamanlari(
    uzunluklar: list[float], t0: float, t1: float, en_az: float = 0.04
) -> list[tuple[float, float]]:
    """Sıralı kalem darbeleri: uzunluğa orantılı süre, toplam [t0,t1]. -> [(bas, sure)]."""
    ham = [max(en_az, u) if False else u for u in uzunluklar]
    top = sum(ham) or 1.0
    sure = [max(en_az, (t1 - t0) * u / top) for u in ham]
    k = (t1 - t0) / sum(sure)
    sure = [s * k for s in sure]
    out: list[tuple[float, float]] = []
    t = t0
    for s in sure:
        out.append((round(t, 4), round(s, 4)))
        t += s
    return out

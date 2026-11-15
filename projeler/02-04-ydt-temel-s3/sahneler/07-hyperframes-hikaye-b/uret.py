#!/usr/bin/python3
"""Sahne 07 hikâye karesi B (soru kartı) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: kanal (291-339) -> künye (386-434) -> soru (460-560) -> kart (580-760) -> şıklar (780-900) -> kural (920-1060) -> kaydet (1070-1140)."""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path
from typing import Any

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# zaman.json ve zamanlar.json okuma ve doğrulama
zaman_data = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlar = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlar) == 1, f"duragan listesinde {AD.name} olan tek kayıt olmalı, bulunan: {len(duragan_kayitlar)}"
kayit = duragan_kayitlar[0]
assert kayit["kare"] == 1, f"kare {kayit['kare']} != 1"
assert kayit["cikti"] == "hikaye-b.png", f"cikti {kayit['cikti']} != 'hikaye-b.png'"
assert AD.name not in [s["klasor"] for s in zaman_data.get("sahneler", [])], "AD.name sahneler içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}
assert R["zemin"] == "#1b1a17"
assert R["murekkep"] == "#f3efe6"
assert R["ikincil"] == "#c9c2b3"
assert R["vurgu"] == "#f2a93b"


def _kutu(x: float, y: float, w: float, h: float, ince: bool = False) -> dict[str, Any]:
    return {"n": [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], "kapali": True, "ince": ince}


TREN: list[dict[str, Any]] = [
    _kutu(200.0, 55.0, 170.0, 75.0),
    _kutu(200.0, 10.0, 75.0, 45.0),
    _kutu(320.0, 22.0, 26.0, 33.0, True),
    {"n": [(370.0, 95.0), (398.0, 130.0), (370.0, 130.0)]},
    _kutu(0.0, 45.0, 175.0, 85.0),
    {"n": [(175.0, 112.0), (200.0, 112.0)], "ince": True},
    _kutu(20.0, 60.0, 50.0, 30.0, True),
    _kutu(100.0, 60.0, 50.0, 30.0, True),
    _kutu(215.0, 20.0, 42.0, 25.0, True),
    {"daire": (40.0, 138.0, 17.0)},
    {"daire": (135.0, 138.0, 17.0)},
    {"daire": (240.0, 138.0, 17.0)},
    {"daire": (335.0, 138.0, 17.0)},
    {"n": [(-10.0, 158.0), (420.0, 158.0)], "ince": True},
]


def _kutusu(parcalar: list[dict[str, Any]]) -> tuple[float, float, float, float]:
    xs: list[float] = []
    ys: list[float] = []
    for p in parcalar:
        if "daire" in p:
            x, y, r = p["daire"]
            xs += [float(x - r), float(x + r)]
            ys += [float(y - r), float(y + r)]
        else:
            xs += [float(q[0]) for q in p["n"]]
            ys += [float(q[1]) for q in p["n"]]
    return min(xs), min(ys), max(xs), max(ys)


def _daire_yolu(cx: float, cy: float, r: float) -> str:
    k = 0.5523 * r
    return (
        "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f "
        "C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
        % (
            cx + r, cy, cx + r, cy + k, cx + k, cy + r, cx, cy + r,
            cx - k, cy + r, cx - r, cy + k, cx - r, cy,
            cx - r, cy - k, cx - k, cy - r, cx, cy - r,
            cx + k, cy - r, cx + r, cy - k, cx + r, cy,
        )
    )


def ikon_yollari(
    parcalar: list[dict[str, Any]], mx: float, my: float, en: float, boy: float
) -> list[tuple[str, float, bool]]:
    """Izgara parçalarını en x boy kutusuna (merkez mx, my) sığdırır. Döner: [(d, uzunluk, ince)]."""
    gx0, gy0, gx1, gy1 = _kutusu(parcalar)
    sc = min(boy / (gy1 - gy0), en / (gx1 - gx0))
    gmx, gmy = (gx0 + gx1) / 2.0, (gy0 + gy1) / 2.0

    def P(q: tuple[float, float]) -> tuple[float, float]:
        return (mx + (q[0] - gmx) * sc, my + (q[1] - gmy) * sc)

    out: list[tuple[str, float, bool]] = []
    for p in parcalar:
        if "daire" in p:
            x, y, r = p["daire"]
            c = P((x, y))
            out.append((_daire_yolu(c[0], c[1], r * sc), 2.0 * math.pi * r * sc, p.get("ince", False)))
            continue
        q = [P(v) for v in p["n"]]
        if p.get("kapali"):
            q = q + [q[0]]
        uz = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(q, q[1:]))
        if p.get("egri") and len(q) >= 3:
            d = "M%.1f %.1f" % q[0]
            for i in range(len(q) - 1):
                p0, p1, p2 = q[max(i - 1, 0)], q[i], q[i + 1]
                p3 = q[min(i + 2, len(q) - 1)]
                c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
                c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
                d += " C%.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p2)
            uz *= 1.05
        else:
            d = "M%.1f %.1f " % q[0] + " ".join("L%.1f %.1f" % v for v in q[1:])
        out.append((d, uz, p.get("ince", False)))
    return out


HUD = {
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
}
KONU = "Simple Present vs Present Continuous"
ROZET = "YDT · BASIC"


def konu_boyu() -> int:
    """34'ten 28'e inerek rozetle birlikte sagSinir'a (960) sığan ilk tam sayı yazı boyu."""
    rozet_g = Y.genislik("Lexend", 700, ROZET, HUD["rozetYazi"]) + 2 * HUD["rozetDolgu"]
    for boy in range(HUD["konuUst"], HUD["konuAlt"] - 1, -1):
        toplam_g = HUD["konuX"] + Y.genislik("Fredoka", 700, KONU, boy) + HUD["rozetAra"] + rozet_g
        if toplam_g <= HUD["sagSinir"]:
            return boy
    raise AssertionError(f"Konu başlığı [{HUD['konuAlt']}, {HUD['konuUst']}] aralığında sağ sınıra sığmadı")


def rozet_konumlari() -> list[tuple[float, float]]:
    """Tek rozet hapı konumu: [(x, genişlik)]."""
    x = HUD["konuX"] + Y.genislik("Fredoka", 700, KONU, konu_boyu()) + HUD["rozetAra"]
    w = Y.genislik("Lexend", 700, ROZET, HUD["rozetYazi"]) + 2 * HUD["rozetDolgu"]
    return [(x, w)]


def kunye_svg() -> str:
    """Kanal katmanı (#kanal) ve künye (#kunye) SVG grubu."""
    sar, kre, zem = R["vurgu"], R["murekkep"], R["zemin"]
    h = HUD
    lw = h["logoYuk"] * Y.LOGO_EN_BOY
    lx = h["konuX"] - lw * Y.LOGO_KAYMA
    logo = (
        f'<image id="logoimg" href="assets/logo.svg" x="{lx:.2f}" y="{h["logoY"]}" '
        f'width="{lw:.2f}" height="{h["logoYuk"]}"/>'
    )
    kanal_yazi = (
        f'<text id="kanal-yazi" x="{h["kanalX"]}" y="{h["kanalTaban"]}" '
        f'font-family="Lexend" font-weight="700" font-size="{h["kanalYazi"]}" fill="{kre}">@ydspublishing</text>'
    )
    kanal = f'<g id="kanal">{logo}{kanal_yazi}</g>'
    k_boy = konu_boyu()
    konu_txt = (
        f'<text id="ku-konu" x="{h["konuX"]}" y="{h["konuTaban"]}" '
        f'font-family="Fredoka" font-weight="700" font-size="{k_boy}" fill="{kre}" '
        f'style="font-kerning:none">{KONU}</text>'
    )
    x, w = rozet_konumlari()[0]
    rz = (
        f'<g id="rz0">'
        f'<rect x="{x:.1f}" y="{h["rozetY"]}" width="{w:.1f}" height="{h["rozetH"]}" '
        f'rx="{h["rozetH"] // 2}" fill="{sar}"/>'
        f'<text x="{x + w / 2.0:.1f}" y="419" text-anchor="middle" '
        f'font-family="Lexend" font-weight="700" font-size="{h["rozetYazi"]}" fill="{zem}">{ROZET}</text>'
        f'</g>'
    )
    return f'<g id="kunye">{kanal}{konu_txt}{rz}</g>'


SORU = "Tarife mi, plan mı?"


def hesapla_s_soru() -> int:
    """Soru başlığı için en büyük uygun yazı boyunu hesaplar (beklenen 96)."""
    w100 = Y.genislik("Fredoka", 700, SORU, 100) / 100.0
    return min(96, int(math.floor(900.0 / w100)))


def soru_svg(s_soru: int) -> str:
    """Soru başlığı SVG çıktısı (§5.1)."""
    return (
        f'<text id="soru" x="60" y="532" font-family="Fredoka" font-weight="700" '
        f'font-size="{s_soru}" fill="{R["murekkep"]}" xml:space="preserve">{SORU}</text>'
    )


def tren_svg() -> str:
    """Kart içi tren ikonu SVG grubu (§5.3)."""
    tren_yollar = ikon_yollari(TREN, mx=842.0, my=625.0, en=180.0, boy=64.0)
    tren_paths: list[str] = []
    for idx, (d, _, ince) in enumerate(tren_yollar):
        if idx == len(tren_yollar) - 1:
            renk = R["ikincil"]
            sw = 3
        elif ince:
            renk = R["murekkep"]
            sw = 3
        else:
            renk = R["murekkep"]
            sw = 4
        tren_paths.append(f'<path d="{d}" stroke="{renk}" stroke-width="{sw}"/>')
    return f'<g id="kart-tren" fill="none" stroke-linecap="round" stroke-linejoin="round">{"".join(tren_paths)}</g>'


def saat_svg() -> str:
    """Kart içi saat ikonu SVG grubu (§5.3)."""
    mur = R["murekkep"]
    cx, cy, r = 842.0, 712.0, 34.0
    parcalar = [
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{mur}" stroke-width="4"/>',
        f'<line x1="{cx:.1f}" y1="{cy - 0.80 * r:.2f}" x2="{cx:.1f}" y2="{cy - 0.66 * r:.2f}" stroke="{mur}" stroke-width="3"/>',
        f'<line x1="{cx + 0.66 * r:.2f}" y1="{cy:.1f}" x2="{cx + 0.80 * r:.2f}" y2="{cy:.1f}" stroke="{mur}" stroke-width="3"/>',
        f'<line x1="{cx:.1f}" y1="{cy + 0.66 * r:.2f}" x2="{cx:.1f}" y2="{cy + 0.80 * r:.2f}" stroke="{mur}" stroke-width="3"/>',
        f'<line x1="{cx - 0.80 * r:.2f}" y1="{cy:.1f}" x2="{cx - 0.66 * r:.2f}" y2="{cy:.1f}" stroke="{mur}" stroke-width="3"/>',
        f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx:.1f}" y2="{cy - 0.66 * r:.2f}" stroke="{mur}" stroke-width="4"/>',
        f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx + math.sin(math.radians(210)) * 0.5 * r:.2f}" y2="{cy - math.cos(math.radians(210)) * 0.5 * r:.2f}" stroke="{mur}" stroke-width="5"/>',
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="3.5" fill="{mur}"/>',
    ]
    return f'<g id="kart-saat" stroke-linecap="round">{"".join(parcalar)}</g>'


def kart_svg() -> str:
    """Cümle kartı grubu SVG çıktısı (§5.2–5.3)."""
    mur = R["murekkep"]
    crv = (
        f'<rect id="kart-crv" x="62" y="582" width="896" height="176" rx="28" '
        f'fill="none" stroke="{mur}" stroke-width="4"/>'
    )
    tren = tren_svg()
    saat = saat_svg()
    s1 = (
        f'<text id="kart-s1" x="88" y="655" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{mur}" xml:space="preserve">The train to İzmir</text>'
    )
    s2 = (
        f'<text id="kart-s2" x="88" y="730" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{mur}" xml:space="preserve">leaves at 7 pm today.</text>'
    )
    lw = Y.genislik("Fredoka", 700, "leaves", 64)
    alti = (
        f'<path id="alti" d="M{88 - 4} 741 Q{88 + lw / 2.0:.1f} 746 {88 + lw + 4:.1f} 738" '
        f'fill="none" stroke="{R["vurgu"]}" stroke-width="10" stroke-linecap="round"/>'
    )
    return f'<g id="kart">{crv}{tren}{saat}{s1}{s2}{alti}</g>'


def siklar_svg() -> tuple[str, str]:
    """Şık A (doğru, yeşil) ve Şık B (soluk) SVG çıktıları (§6)."""
    mur = R["murekkep"]
    sA = (
        f'<g id="sA">'
        f'<rect id="sA-crv" x="63" y="782" width="432" height="116" rx="24" '
        f'fill="none" class="dogru" stroke="#3a9a6a" stroke-width="6"/>'
        f'<circle id="sA-daire" cx="120" cy="840" r="38" fill="none" stroke="{mur}" stroke-width="4"/>'
        f'<text id="sA-harf" x="120" y="862" text-anchor="middle" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{mur}" xml:space="preserve">A</text>'
        f'<text id="sA-yazi" x="176" y="865" font-family="Fredoka" font-weight="700" font-size="72" '
        f'fill="{mur}" xml:space="preserve">TARİFE</text>'
        f'<path id="sA-tik" d="M437 842 L451 857 L476 826" fill="none" class="dogru" stroke="#3a9a6a" '
        f'stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
        f'</g>'
    )
    sB = (
        f'<g id="sB" opacity="0.4">'
        f'<rect id="sB-crv" x="524" y="782" width="434" height="116" rx="24" '
        f'fill="none" stroke="{mur}" stroke-width="4"/>'
        f'<circle id="sB-daire" cx="582" cy="840" r="38" fill="none" stroke="{mur}" stroke-width="4"/>'
        f'<text id="sB-harf" x="582" y="862" text-anchor="middle" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{mur}" xml:space="preserve">B</text>'
        f'<text id="sB-yazi" x="638" y="865" font-family="Fredoka" font-weight="700" font-size="72" '
        f'fill="{mur}" xml:space="preserve">PLAN</text>'
        f'</g>'
    )
    return sA, sB


def kural_svg() -> str:
    """Kural özeti SVG grubu (§7.1)."""
    mur = R["murekkep"]
    return (
        f'<g id="kural">'
        f'<text id="kural-s1" x="60" y="970" font-family="Lexend" font-weight="500" font-size="64" '
        f'fill="{mur}">Tren tarifeye uyar:</text>'
        f'<text id="kural-s2" x="60" y="1043" font-family="Lexend" font-weight="700" font-size="64" '
        f'fill="{mur}">geniş zaman.</text>'
        f'</g>'
    )


def kaydet_svg() -> str:
    """Kaydet grubu (#kaydet) SVG çıktısı (§7.2)."""
    mur = R["murekkep"]
    return (
        f'<g id="kaydet">'
        f'<path id="kaydet-imi" d="M63 1078 Q63 1074 67 1074 H103 Q107 1074 107 1078 V1134 L85 1118 L63 1134 Z" '
        f'fill="none" stroke="{mur}" stroke-width="5" stroke-linejoin="round"/>'
        f'<text id="kaydet-yazi" x="131" y="1122" font-family="Fredoka" font-weight="700" font-size="64" '
        f'fill="{mur}">Kaydet</text>'
        f'</g>'
    )


def blok_kutulari(s_soru: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Yerleşim bloklarının ve iç öğelerinin kutularını hesaplar."""
    # 1. kanal
    w_kanal = (263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42)) - 60.0
    kanal = {"ad": "kanal", "x": 60.0, "y": 291.0, "w": w_kanal, "h": 48.0}

    # 2. kunye
    rz_x, rz_w = rozet_konumlari()[0]
    w_kunye = (rz_x + rz_w) - 60.0
    kunye = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": w_kunye, "h": 48.0}

    # 3. soru
    w_soru = Y.genislik("Fredoka", 700, SORU, s_soru)
    soru = {
        "ad": "soru",
        "x": 60.0,
        "y": 532.0 - 0.73 * s_soru,
        "w": w_soru,
        "h": (0.73 + 0.221) * s_soru,
    }

    # 4. kart
    kart = {"ad": "kart", "x": 60.0, "y": 580.0, "w": 900.0, "h": 180.0}

    # 5. sA
    sA = {"ad": "sA", "x": 60.0, "y": 779.0, "w": 438.0, "h": 122.0}  # çizgi 6: dış kenar 60-498

    # 6. sB
    sB = {"ad": "sB", "x": 522.0, "y": 780.0, "w": 438.0, "h": 120.0}

    # 7. kural
    w_kural1 = Y.genislik("Lexend", 500, "Tren tarifeye uyar:", 64)
    w_kural2 = Y.genislik("Lexend", 700, "geniş zaman.", 64)
    w_kural = max(w_kural1, w_kural2)
    kural = {
        "ad": "kural",
        "x": 60.0,
        "y": 920.0,
        "w": w_kural,
        "h": 1058.7 - 920.0,
    }

    # 8. kaydet
    kaydet = {
        "ad": "kaydet",
        "x": 60.5,
        "y": 1071.5,
        "w": 338.9 - 60.5,
        "h": 1136.7 - 1071.5,
    }

    bloklar = [kanal, kunye, soru, kart, sA, sB, kural, kaydet]

    # İç öğeler: tren, saat, alti, tik
    tren = {"ad": "tren", "x": 752.0, "y": 594.0, "w": 180.0, "h": 62.0}
    saat = {"ad": "saat", "x": 805.6, "y": 675.6, "w": 72.8, "h": 72.8}
    alti = {"ad": "alti", "x": 79.0, "y": 733.0, "w": 208.2, "h": 18.0}
    tik = {"ad": "tik", "x": 433.0, "y": 822.0, "w": 47.0, "h": 39.0}

    ic_ogeler = [tren, saat, alti, tik]

    return bloklar, ic_ogeler


def kesisim(b1: dict[str, Any], b2: dict[str, Any]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(
    bloklar: list[dict[str, Any]], ic_ogeler: list[dict[str, Any]], s_soru: int, html: str
) -> None:
    """SPEC.md §9 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}
    ic_dict = {b["ad"]: b for b in ic_ogeler}

    # 1. Her blok: x >= 59 - 1e-4, x + w <= 960 + 1e-4, y >= 280, y + h <= 1140 + 1e-4
    for b in bloklar:
        assert b["x"] >= 60.0 - 1e-4, f"{b['ad']} sol {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{b['ad']} sağ {b['x'] + b['w']} > 960"
        assert b["y"] >= 280.0 - 1e-4, f"{b['ad']} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 1140.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1140"

    # 2. Bant içi: kanal ⊂ [280, 350], kunye ⊂ [360, 450], soru ⊂ [460, 560], kart ⊂ [580, 760], sA, sB ⊂ [778, 902], kural ⊂ [920, 1060], kaydet ⊂ [1070, 1140]
    assert b_dict["kanal"]["y"] >= 280.0 - 1e-4 and b_dict["kanal"]["y"] + b_dict["kanal"]["h"] <= 350.0 + 1e-4
    assert b_dict["kunye"]["y"] >= 360.0 - 1e-4 and b_dict["kunye"]["y"] + b_dict["kunye"]["h"] <= 450.0 + 1e-4
    assert b_dict["soru"]["y"] >= 460.0 - 1e-4 and b_dict["soru"]["y"] + b_dict["soru"]["h"] <= 560.0 + 1e-4
    assert b_dict["kart"]["y"] >= 580.0 - 1e-4 and b_dict["kart"]["y"] + b_dict["kart"]["h"] <= 760.0 + 1e-4
    assert b_dict["sA"]["y"] >= 778.0 - 1e-4 and b_dict["sA"]["y"] + b_dict["sA"]["h"] <= 902.0 + 1e-4
    assert b_dict["sB"]["y"] >= 778.0 - 1e-4 and b_dict["sB"]["y"] + b_dict["sB"]["h"] <= 902.0 + 1e-4
    assert b_dict["kural"]["y"] >= 920.0 - 1e-4 and b_dict["kural"]["y"] + b_dict["kural"]["h"] <= 1060.0 + 1e-4
    assert b_dict["kaydet"]["y"] >= 1070.0 - 1e-4 and b_dict["kaydet"]["y"] + b_dict["kaydet"]["h"] <= 1140.0 + 1e-4

    # 3. Ana bloklar kesişmez (alan 0); dikey komşu boşluğu >= 10; sA-sB yatay boşluk >= 20
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    dikey_ciftler = [
        ("kanal", "kunye"),
        ("kunye", "soru"),
        ("soru", "kart"),
        ("kart", "sA"),
        ("kart", "sB"),
        ("sA", "kural"),
        ("sB", "kural"),
        ("kural", "kaydet"),
    ]
    for b1_ad, b2_ad in dikey_ciftler:
        b1 = b_dict[b1_ad]
        b2 = b_dict[b2_ad]
        bosluk = b2["y"] - (b1["y"] + b1["h"])
        assert bosluk >= 10.0 - 1e-4, f"Dikey boşluk {b1_ad} -> {b2_ad}: {bosluk} < 10"

    yatay_bosluk = b_dict["sB"]["x"] - (b_dict["sA"]["x"] + b_dict["sA"]["w"])
    assert yatay_bosluk >= 20.0 - 1e-4, f"sA-sB yatay boşluk {yatay_bosluk} < 20"

    # 4. Kart içi (çerçeve iç alanı x 64-956, y 584-756): kart-s1, kart-s2, alti, tren, saat kutuları bu alanda;
    #    kart-s1 sağ <= tren sol - 24; kart-s2 sağ <= saat sol - 24; tren alt <= saat üst - 10;
    #    kart-s1 alt (taban + 0.02*64) <= kart-s2 üst (taban - 0.73*64) - 10; alti üst >= 730 + 2
    w_s1 = Y.genislik("Fredoka", 700, "The train to İzmir", 64)
    w_s2 = Y.genislik("Fredoka", 700, "leaves at 7 pm today.", 64)
    kart_ici_kutular = {
        "kart-s1": {"x": 88.0, "y": 655.0 - 0.921 * 64.0, "w": w_s1, "h": (0.921 + 0.02) * 64.0},
        "kart-s2": {"x": 88.0, "y": 730.0 - 0.73 * 64.0, "w": w_s2, "h": (0.73 + 0.229) * 64.0},
        "alti": ic_dict["alti"],
        "tren": ic_dict["tren"],
        "saat": ic_dict["saat"],
    }
    for k_ad, kb in kart_ici_kutular.items():
        assert kb["x"] >= 64.0 - 1e-4, f"{k_ad} sol {kb['x']} < 64"
        assert kb["x"] + kb["w"] <= 956.0 + 1e-4, f"{k_ad} sağ {kb['x'] + kb['w']} > 956"
        assert kb["y"] >= 584.0 - 1e-4, f"{k_ad} üst {kb['y']} < 584"
        assert kb["y"] + kb["h"] <= 756.0 + 1e-4, f"{k_ad} alt {kb['y'] + kb['h']} > 756"

    assert (88.0 + w_s1) <= ic_dict["tren"]["x"] - 24.0 + 1e-4, "kart-s1 sağ <= tren sol - 24 sağlanmadı"
    assert (88.0 + w_s2) <= ic_dict["saat"]["x"] - 24.0 + 1e-4, "kart-s2 sağ <= saat sol - 24 sağlanmadı"
    assert (ic_dict["tren"]["y"] + ic_dict["tren"]["h"]) <= ic_dict["saat"]["y"] - 10.0 + 1e-4, "tren alt <= saat üst - 10 sağlanmadı"
    s1_alt = 655.0 + 0.02 * 64.0
    s2_ust = 730.0 - 0.73 * 64.0
    assert s1_alt <= s2_ust - 10.0 + 1e-4, f"kart-s1 alt ({s1_alt}) <= kart-s2 üst ({s2_ust}) - 10 sağlanmadı"
    assert ic_dict["alti"]["y"] >= 730.0 + 2.0 - 1e-4, "alti üst >= 732 sağlanmadı"

    # 5. Şık içi: daire sağı + 12 <= yazı solu; A: yazı sağı + 10 <= ✓ sol, ✓ sağ <= 496 - 10; B: yazı sağı <= 958 - 24
    assert 120.0 + 38.0 + 12.0 <= 176.0 + 1e-4, "A: daire sağı + 12 <= yazı solu sağlanmadı"
    w_tarife = Y.genislik("Fredoka", 700, "TARİFE", 72)
    tik_sol = ic_dict["tik"]["x"]
    tik_sag = ic_dict["tik"]["x"] + ic_dict["tik"]["w"]
    assert 176.0 + w_tarife + 10.0 <= tik_sol + 1e-4, "A: yazı sağı + 10 <= ✓ sol sağlanmadı"
    assert tik_sag <= 496.0 - 10.0 + 1e-4, "A: ✓ sağ <= 496 - 10 sağlanmadı"

    assert 582.0 + 38.0 + 12.0 <= 638.0 + 1e-4, "B: daire sağı + 12 <= yazı solu sağlanmadı"
    w_plan = Y.genislik("Fredoka", 700, "PLAN", 72)
    assert 638.0 + w_plan <= 958.0 - 24.0 + 1e-4, "B: yazı sağı <= 958 - 24 sağlanmadı"

    # 6. İçerik yazı boyu >= 64: soru S >= 64, kart 64, harf 64, şık 72, kural 64, kaydet 64.
    assert s_soru >= 64, f"soru boyu {s_soru} < 64"

    # 7. Ekran satırları <= 24 karakter (künye standart ölçüsü muaf)
    satirlar = [
        "@ydspublishing",
        "YDT · BASIC",
        "Tarife mi, plan mı?",
        "The train to İzmir",
        "leaves at 7 pm today.",
        "TARİFE",
        "PLAN",
        "Tren tarifeye uyar:",
        "geniş zaman.",
        "Kaydet",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu > 24: '{s}' ({len(s)})"

    # 8. Üretilen HTML'de yasak dizgiler
    yasak_duyarsiz = [
        "tam ders",
        "dakika",
        "Full lesson",
        "profildeki",
        "Cevap",
        'font-family="Caveat"',
        "✓",
        'id="altyazi"',
        'id="rz1"',
        "kirmizi",
        "#e0473b",
    ]
    html_kucuk = html.lower()
    for y in yasak_duyarsiz:
        assert y.lower() not in html_kucuk, f"HTML içinde yasak dizgi bulundu: {y}"

    assert "Izmir" not in html, "HTML içinde noktasız 'Izmir' olmamalı"
    assert "İzmir" in html, "HTML içinde noktalı 'İzmir' olmalı"
    assert "7 pm" in html, "HTML içinde '7 pm' olmalı"

    for char in html:
        assert ord(char) < 0x1F000, f"HTML içinde emoji bulundu: {char} (U+{ord(char):04X})"

    # Kabul ölçütü 3: HTML'de #kanal içinde tam 1 image (#logoimg) + 1 text (@ydspublishing); #kunye içinde konu + rozet; altyazı öğesi yok
    kanal_match = re.search(r'<g id="kanal">(.*?)</g>', html)
    assert kanal_match, "HTML içinde #kanal bulunamadı"
    assert kanal_match.group(1).count("<image ") == 1, "#kanal içinde tam 1 image olmalı"
    assert kanal_match.group(1).count("<text ") == 1, "#kanal içinde tam 1 text olmalı"
    assert 'id="logoimg"' in kanal_match.group(1), "#kanal içinde #logoimg olmalı"
    assert "@ydspublishing" in kanal_match.group(1), "#kanal içinde @ydspublishing olmalı"

    kunye_match = re.search(r'<g id="kunye">([\s\S]*?)</g>\s*<text id="soru"', html)
    assert kunye_match, "HTML içinde #kunye bulunamadı"
    assert 'id="ku-konu"' in kunye_match.group(1), "#kunye içinde #ku-konu olmalı"
    assert 'id="rz0"' in kunye_match.group(1), "#kunye içinde #rz0 olmalı"
    assert 'id="altyazi"' not in html, "HTML içinde altyazı öğesi olmamalı"
    # hf_tema.py "#root.tema-acik" görürse dönüştürmeyi atlar (açık kare koyu çıkar)
    assert "#root.tema-acik" not in html, "uret.py CSS'i #root.tema-acik içermemeli"


def uret() -> tuple[str, int, list[dict[str, Any]], list[dict[str, Any]]]:
    """Sahne HTML'ini üretir ve doğrular."""
    s_soru = hesapla_s_soru()
    bloklar, ic_ogeler = blok_kutulari(s_soru)

    kunye = kunye_svg()
    soru = soru_svg(s_soru)
    kart = kart_svg()
    sA, sB = siklar_svg()
    kural = kural_svg()
    kaydet = kaydet_svg()

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
#sahne text{{font-kerning:none;}}
#root .dogru{{stroke:#3a9a6a}}
.tema-acik #sahne .dogru{{stroke:#167a4a}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{soru}
{kart}
{sA}
{sB}
{kural}
{kaydet}
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var tl = gsap.timeline({{ paused: true }});
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, 0);
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, {Z['sure']});
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""

    kurallari_dogrula(bloklar, ic_ogeler, s_soru, html)
    return html, s_soru, bloklar, ic_ogeler


if __name__ == "__main__":
    proje_dizini = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, S, bloklar, ic_ogeler = uret()
    (proje_dizini / "index.html").write_text(html, encoding="utf-8")

    tum_nesneler = bloklar + ic_ogeler
    nesneler = [
        {
            "ad": b["ad"],
            "x": int(round(b["x"])),
            "y": int(round(b["y"])),
            "w": int(round(b["w"])),
            "h": int(round(b["h"])),
        }
        for b in tum_nesneler
    ]
    (AD / "nesneler.json").write_text(json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"index.html yazıldı {len(html)}")
    print(f"S_SORU={S}")

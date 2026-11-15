#!/usr/bin/python3
"""Sahne 04 hikâye karesi index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: kanal (291-339) -> künye (386-434) -> üst (460-550) -> başlık (570-830) -> kart (850-1040) -> kaydet (1050-1140)."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# zaman.json ve zamanlar.json okuma ve doğrulama
zaman_data = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
hikaye = zaman_data["hikaye"]
assert hikaye["klasor"] == AD.name, f"klasor {hikaye['klasor']} != {AD.name}"
assert hikaye["kare"] == 1, f"kare {hikaye['kare']} != 1"
assert hikaye["cikti"] == "hikaye-a.png", f"cikti {hikaye['cikti']} != hikaye-a.png"
assert AD.name not in [s["klasor"] for s in zaman_data["sahneler"]], "AD.name sahneler içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}


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


def _bilet() -> list[dict[str, Any]]:
    def yay(x0: float, yon: float) -> list[tuple[float, float]]:
        return [
            (
                x0 - yon * 22.0 * math.cos(-math.pi / 2.0 + i / 12.0 * math.pi),
                yon * 22.0 * math.sin(-math.pi / 2.0 + i / 12.0 * math.pi),
            )
            for i in range(13)
        ]

    kenar = (
        [(-180.0, -70.0), (180.0, -70.0), (180.0, -22.0)]
        + yay(180.0, 1.0)
        + [(180.0, 70.0), (-180.0, 70.0), (-180.0, 22.0)]
        + yay(-180.0, -1.0)
    )
    p: list[dict[str, Any]] = [{"n": kenar + [(-180.0, -70.0)]}]
    p += [{"n": [(100.0, -58.0 + i * 20.0), (100.0, -47.0 + i * 20.0)], "ince": True} for i in range(6)]
    p += [{"n": [(-150.0, y), (x1, y)], "ince": True} for y, x1 in ((-30.0, 60.0), (0.0, 30.0), (30.0, 70.0))]
    return p


BILET: list[dict[str, Any]] = _bilet()


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
ROZET = "YDT · TEMEL"


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


BAS2_YAZI = "DÜZENLEME"  # DUZ2 A3: "plan -> am going" denkliği kapsamsız; seste "kesin düzenleme"
KART_KB = 64.0           # DUZ2: kart satırı 64 px, sol x 96 (satır 2 "kesin düzenleme -> am going." 826 px)
KART_TX = 96.0


def hesapla_s_ve_bas() -> tuple[
    int, int, float, float, float, float, float, float, float, float, float, float, float
]:
    """Başlık bloğu 'TARİFE' / '≠ DÜZENLEME' için S ve yerleşim değerlerini hesaplar (DUZ2: PLAN -> DÜZENLEME)."""
    w1 = Y.genislik("Fredoka", 700, "TARİFE", 100) / 100.0
    w_plan_100 = Y.genislik("Fredoka", 700, BAS2_YAZI, 100) / 100.0
    wh = 0.36 + 0.50 + 0.24 + w_plan_100 + 0.36
    S = min(120, int(math.floor(900.0 / max(w1, wh))))

    while S >= 64:
        taban1 = 570 + int(math.ceil(0.921 * S)) + 2
        hh = 1.02 * S
        hy = 828.0 - hh
        taban2 = hy + 0.86 * S
        if hy - (taban1 + 0.01 * S) >= 12:
            break
        S -= 1

    assert S >= 64, f"S={S} < 64"

    hw = wh * S
    hx = 60.0
    rx = hh / 2.0
    cx = hx + 0.36 * S + 0.25 * S

    w_tarife = Y.genislik("Fredoka", 700, "TARİFE", S)
    bas_x = 60.0
    bas_y = taban1 - 0.921 * S
    bas_w = max(w_tarife, hw)
    bas_h = 828.0 - bas_y

    return S, taban1, taban2, hy, hw, hh, rx, cx, wh, bas_x, bas_y, bas_w, bas_h


def bas_svg(
    S: int,
    taban1: int,
    taban2: float,
    hy: float,
    hw: float,
    hh: float,
    rx: float,
    cx: float,
) -> str:
    """Başlık bloğu 'TARİFE' / '≠ DÜZENLEME' SVG çıktısı."""
    bas1 = (
        f'<text id="bas1" x="60" y="{taban1}" '
        f'font-family="Fredoka" font-weight="700" font-size="{S}" '
        f'fill="{R["murekkep"]}" xml:space="preserve">TARİFE</text>'
    )
    hap_rect = (
        f'<rect id="bas2-hap" x="60" y="{hy:.1f}" width="{hw:.1f}" height="{hh:.1f}" '
        f'rx="{rx:.1f}" fill="{R["vurgu"]}"/>'
    )
    sw_esit = 0.12 * S
    esitdegil = (
        f'<g id="esitdegil" fill="none" stroke="{R["zemin"]}" stroke-width="{sw_esit:.1f}" stroke-linecap="round">'
        f'<path d="M{cx - 0.25 * S:.1f} {taban2 - 0.47 * S:.1f} L{cx + 0.25 * S:.1f} {taban2 - 0.47 * S:.1f}"/>'
        f'<path d="M{cx - 0.25 * S:.1f} {taban2 - 0.23 * S:.1f} L{cx + 0.25 * S:.1f} {taban2 - 0.23 * S:.1f}"/>'
        f'<path d="M{cx - 0.14 * S:.1f} {taban2 - 0.02 * S:.1f} L{cx + 0.14 * S:.1f} {taban2 - 0.68 * S:.1f}"/>'
        f'</g>'
    )
    plan_x = 60.0 + (0.36 + 0.50 + 0.24) * S
    plan_text = (
        f'<text id="bas2-yazi" x="{plan_x:.1f}" y="{taban2:.1f}" '
        f'font-family="Fredoka" font-weight="700" font-size="{S}" '
        f'fill="{R["zemin"]}" xml:space="preserve">{BAS2_YAZI}</text>'
    )
    bas2 = f'<g id="bas2">{hap_rect}{esitdegil}{plan_text}</g>'
    return f'<g id="bas">{bas1}{bas2}</g>'


def kart_svg() -> str:
    """Kural özeti kartı (#kart) SVG çıktısı."""
    crv = f'<rect id="kart-crv" x="62" y="852" width="896" height="186" rx="28" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    # İki satır: Tarife → leaves, / kesin düzenleme → am going. (DUZ2: simge sütunu kalktı)
    TX = KART_TX
    KB = KART_KB
    dx_ok = 18.0 * math.cos(0.5)
    dy_ok = 18.0 * math.sin(0.5)

    # Satır 1
    w_sol1 = Y.genislik("Fredoka", 700, "Tarife", KB)
    x_ok0_1 = TX + w_sol1 + 0.22 * KB
    x_ok1_1 = x_ok0_1 + 0.70 * KB
    x_sag1 = x_ok1_1 + 0.22 * KB
    y_ok1 = 922.0 - 0.28 * KB
    d_ok1 = (
        f"M{x_ok0_1:.1f} {y_ok1:.1f} L{x_ok1_1:.1f} {y_ok1:.1f} "
        f"M{x_ok1_1 - dx_ok:.1f} {y_ok1 - dy_ok:.1f} L{x_ok1_1:.1f} {y_ok1:.1f} L{x_ok1_1 - dx_ok:.1f} {y_ok1 + dy_ok:.1f}"
    )

    s1_sol = f'<text id="kart-s1-sol" x="{TX:.1f}" y="922" font-family="Fredoka" font-weight="700" font-size="{KB:g}" fill="{R["murekkep"]}" xml:space="preserve">Tarife</text>'
    s1_ok = f'<path id="kart-s1-ok" class="ok" d="{d_ok1}" fill="none" stroke="{R["murekkep"]}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    s1_sag = f'<text id="kart-s1-sag" x="{x_sag1:.1f}" y="922" font-family="Fredoka" font-weight="700" font-size="{KB:g}" fill="{R["murekkep"]}" xml:space="preserve">leaves,</text>'

    # Satır 2
    w_sol2 = Y.genislik("Fredoka", 700, "kesin düzenleme", KB)
    x_ok0_2 = TX + w_sol2 + 0.22 * KB
    x_ok1_2 = x_ok0_2 + 0.70 * KB
    x_sag2 = x_ok1_2 + 0.22 * KB
    y_ok2 = 1004.0 - 0.28 * KB
    d_ok2 = (
        f"M{x_ok0_2:.1f} {y_ok2:.1f} L{x_ok1_2:.1f} {y_ok2:.1f} "
        f"M{x_ok1_2 - dx_ok:.1f} {y_ok2 - dy_ok:.1f} L{x_ok1_2:.1f} {y_ok2:.1f} L{x_ok1_2 - dx_ok:.1f} {y_ok2 + dy_ok:.1f}"
    )

    s2_sol = f'<text id="kart-s2-sol" x="{TX:.1f}" y="1004" font-family="Fredoka" font-weight="700" font-size="{KB:g}" fill="{R["murekkep"]}" xml:space="preserve">kesin düzenleme</text>'
    s2_ok = f'<path id="kart-s2-ok" class="ok" d="{d_ok2}" fill="none" stroke="{R["murekkep"]}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    s2_sag = f'<text id="kart-s2-sag" x="{x_sag2:.1f}" y="1004" font-family="Fredoka" font-weight="700" font-size="{KB:g}" fill="{R["murekkep"]}" xml:space="preserve">am going.</text>'

    return f'<g id="kart">{crv}{s1_sol}{s1_ok}{s1_sag}{s2_sol}{s2_ok}{s2_sag}</g>'


def kaydet_svg() -> str:
    """Kaydet grubu (#kaydet) SVG çıktısı."""
    simge = (
        f'<path id="kaydet-imi" '
        f'd="M63 1062 Q63 1058 67 1058 H107 Q111 1058 111 1062 V1128 L87 1110 L63 1128 Z" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="5" stroke-linejoin="round"/>'
    )
    yazi = (
        f'<text id="kaydet-yazi" x="135" y="1110" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}">Kaydet</text>'
    )
    return f'<g id="kaydet">{simge}{yazi}</g>'


def blok_kutulari(
    bas_x: float, bas_y: float, bas_w: float, bas_h: float
) -> list[dict[str, Any]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    w_kanal = (263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42)) - 60.0
    kanal = {"ad": "kanal", "x": 60.0, "y": 291.0, "w": w_kanal, "h": 48.0}

    rz_x, rz_w = rozet_konumlari()[0]
    w_kunye = (rz_x + rz_w) - 60.0
    kunye = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": w_kunye, "h": 48.0}

    w_ust = Y.genislik("Lexend", 500, "İkisi geleceği anlatıyor", 64)
    ust = {"ad": "ust", "x": 60.0, "y": 530.0 - 0.901 * 64.0, "w": w_ust, "h": (0.901 + 0.23) * 64.0}

    bas = {"ad": "bas", "x": bas_x, "y": bas_y, "w": bas_w, "h": bas_h}

    kart = {"ad": "kart", "x": 60.0, "y": 850.0, "w": 900.0, "h": 190.0}

    kaydet = {"ad": "kaydet", "x": 60.5, "y": 1055.5, "w": 343.0 - 60.5, "h": 75.5}

    return [kanal, kunye, ust, bas, kart, kaydet]


def kesisim(b1: dict[str, Any], b2: dict[str, Any]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, Any]], S: int, html: str) -> None:
    """SPEC.md §8 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Her blok sınırları: x >= 60, x + w <= 960, y >= 280, y + h <= 1140
    for b in bloklar:
        assert b["x"] >= 60.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 960"
        assert b["y"] >= 280.0 - 1e-4, f"{b['ad']} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 1140.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1140"

    # 2. Bant içi kontroller
    assert b_dict["kanal"]["y"] >= 280.0 - 1e-4 and b_dict["kanal"]["y"] + b_dict["kanal"]["h"] <= 350.0 + 1e-4
    assert b_dict["kunye"]["y"] >= 360.0 - 1e-4 and b_dict["kunye"]["y"] + b_dict["kunye"]["h"] <= 450.0 + 1e-4
    assert b_dict["ust"]["y"] >= 460.0 - 1e-4 and b_dict["ust"]["y"] + b_dict["ust"]["h"] <= 550.0 + 1e-4
    assert b_dict["bas"]["y"] >= 570.0 - 1e-4 and b_dict["bas"]["y"] + b_dict["bas"]["h"] <= 830.0 + 1e-4
    assert b_dict["kart"]["y"] >= 850.0 - 1e-4 and b_dict["kart"]["y"] + b_dict["kart"]["h"] <= 1040.0 + 1e-4
    assert b_dict["kaydet"]["y"] >= 1050.0 - 1e-4 and b_dict["kaydet"]["y"] + b_dict["kaydet"]["h"] <= 1140.0 + 1e-4

    # 3. Blok kutuları kesişmez (alan 0); dikey komşu boşluğu >= 10
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    dikey_sirali = ["kanal", "kunye", "ust", "bas", "kart", "kaydet"]
    for i in range(len(dikey_sirali) - 1):
        b1 = b_dict[dikey_sirali[i]]
        b2 = b_dict[dikey_sirali[i + 1]]
        bosluk = b2["y"] - (b1["y"] + b1["h"])
        assert bosluk >= 10.0 - 1e-4, f"Dikey boşluk {b1['ad']} -> {b2['ad']}: {bosluk} < 10"

    # 4. İçerik yazı boyu >= 64
    assert S >= 64, f"bas boyutu {S} < 64"

    # 5. Ekran satırları <= 24 karakter (künye standart ölçüsü muaf)
    satirlar = [
        ("@ydspublishing", False),
        (KONU, True),  # muaf: standart künye satırı (36 karakter)
        (ROZET, False),
        ("İkisi geleceği anlatıyor", False),
        ("TARİFE", False),
        ("≠ DÜZENLEME", False),
        ("Tarife → leaves,", False),
        ("kesin düzenleme → am going.", True),  # muaf (DUZ2): 27 karakter; kısa kartında ölçü genişlik (<= 934 px)
        ("Kaydet", False),
    ]
    for metin, muaf in satirlar:
        if not muaf:
            assert len(metin) <= 24, f"Satır uzunluğu {len(metin)} > 24: {metin}"

    # 6. Kart içi kontroller (DUZ2: simge sütunu kalktı; satırlar 64 px, sol x 96)
    TX = KART_TX
    KB = KART_KB
    assert TX - 62.0 >= 28.0 - 1e-4, "satır sol ucu kart kenarına çok yakın"

    # Satır metinleri sağ ucu
    w_sol1 = Y.genislik("Fredoka", 700, "Tarife", KB)
    x_ok0_1 = TX + w_sol1 + 0.22 * KB
    x_ok1_1 = x_ok0_1 + 0.70 * KB
    x_sag1 = x_ok1_1 + 0.22 * KB
    w_sag1 = Y.genislik("Fredoka", 700, "leaves,", KB)
    s1_sag_uc = x_sag1 + w_sag1

    w_sol2 = Y.genislik("Fredoka", 700, "kesin düzenleme", KB)
    x_ok0_2 = TX + w_sol2 + 0.22 * KB
    x_ok1_2 = x_ok0_2 + 0.70 * KB
    x_sag2 = x_ok1_2 + 0.22 * KB
    w_sag2 = Y.genislik("Fredoka", 700, "am going.", KB)
    s2_sag_uc = x_sag2 + w_sag2

    assert s1_sag_uc <= 934.0 + 1e-4, f"satır 1 sağ uç {s1_sag_uc} > 934"
    assert s2_sag_uc <= 934.0 + 1e-4, f"satır 2 sağ uç {s2_sag_uc} > 934"

    # Ok gövdesi mesafeleri
    assert x_ok0_1 - (TX + w_sol1) >= 10.0 - 1e-4, "satır 1 ok sol mesafe < 10"
    assert x_sag1 - x_ok1_1 >= 10.0 - 1e-4, "satır 1 ok sağ mesafe < 10"
    assert x_ok0_2 - (TX + w_sol2) >= 10.0 - 1e-4, "satır 2 ok sol mesafe < 10"
    assert x_sag2 - x_ok1_2 >= 10.0 - 1e-4, "satır 2 ok sağ mesafe < 10"

    # 7. Yasak dizgi ve emoji kontrolleri
    yasak_dizgiler = [
        "tam ders",
        "dakika",
        "full lesson",
        "profildeki",
        'font-family="caveat"',
        "≠",
        "→",
        'id="altyazi"',
        'id="rz1"',
    ]
    html_lower = html.lower()
    for yd in yasak_dizgiler:
        assert yd not in html_lower, f"Yasak dizgi HTML içinde bulundu: {yd}"

    for ch in html:
        assert ord(ch) < 0x1F000, f"HTML içinde emoji / U+1F000 üstü karakter bulundu: {ch} (U+{ord(ch):04X})"

    # 8. Standart öğe sayıları kontrolü
    assert html.count('id="logoimg"') == 1, "logoimg tek olmalı"
    assert html.count('id="kanal-yazi"') == 1, "kanal-yazi tek olmalı"
    assert html.count('id="ku-konu"') == 1, "ku-konu tek olmalı"
    assert html.count('id="rz0"') == 1, "rz0 tek olmalı"
    assert 'id="altyazi"' not in html, "altyazi olmamalı"


def uret() -> tuple[str, int, list[dict[str, Any]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    (
        S,
        taban1,
        taban2,
        hy,
        hw,
        hh,
        rx,
        cx,
        wh,
        bas_x,
        bas_y,
        bas_w,
        bas_h,
    ) = hesapla_s_ve_bas()

    bloklar = blok_kutulari(bas_x, bas_y, bas_w, bas_h)

    kunye = kunye_svg()
    ust = f'<text id="ust" x="60" y="530" font-family="Lexend" font-weight="500" font-size="64" fill="{R["murekkep"]}">İkisi geleceği anlatıyor</text>'
    bas = bas_svg(S, taban1, taban2, hy, hw, hh, rx, cx)
    kart = kart_svg()
    kaydet = kaydet_svg()

    stil_esitdegil = '<style id="esitdegil-stil">#root #esitdegil path{stroke:var(--pilMetin)}</style>'

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
#sahne text{{font-kerning:none;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{stil_esitdegil}
{kunye}
{ust}
{bas}
{kart}
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

    kurallari_dogrula(bloklar, S, html)
    return html, S, bloklar


if __name__ == "__main__":
    proje_dizini = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, S, bloklar = uret()
    (proje_dizini / "index.html").write_text(html, encoding="utf-8")

    nesneler = [
        {
            "ad": b["ad"],
            "x": int(round(b["x"])),
            "y": int(round(b["y"])),
            "w": int(round(b["w"])),
            "h": int(round(b["h"])),
        }
        for b in bloklar
    ]
    (AD / "nesneler.json").write_text(json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"index.html yazıldı {len(html)}")
    print(f"S={S}")

#!/usr/bin/python3
"""Sahne 08 hikâye karesi B (soru kartı) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2: kanal katmanı + v2 bantları."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# zaman.json ve zamanlar.json okuma ve doğrulama (kalıp 2 satır 22–28)
zaman_data: dict[str, Any] = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlar = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlar) == 1, (
    f"duragan listesinde {AD.name} olan tek kayıt olmalı, bulunan: {len(duragan_kayitlar)}"
)
kayit = duragan_kayitlar[0]
assert kayit["kare"] == 1, f"kare {kayit['kare']} != 1"
assert kayit["cikti"] == "hikaye-b.png", f"cikti {kayit['cikti']} != 'hikaye-b.png'"
assert AD.name not in [s["klasor"] for s in zaman_data.get("sahneler", [])], "AD.name sahneler içinde olmamalı"

Z: dict[str, Any] = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

assert Y.KONU == "Simple Present"
R: dict[str, str] = Y.RENK
assert R["murekkep"] == "#f3efe6"
assert R["vurgu"] == "#f2a93b"

# Sabitler (SPEC §3)
BASLIK_BOY, BASLIK_TABAN = 88, 536
KOK_BOY, L1, L2 = 64, 634, 714
BOS_W, BOS_KAYMA = 180, 6
OTO_X, OTO_Y, OTO_W = 818, 668, 138
SIK_Y = (775, 895)
SIK_X0 = 65
SIK_X1 = 955
SIK_H = 90
DAIRE_X, DAIRE_R, HARF_KAYMA = 125, 36, 19
SIK_TX, SIK_BOY, METIN_KAYMA = 186, 64, 22
KURAL_BOY, ALT_TABAN = 64, 1094
KAYDET_BOY, YI_S, YI_SW = 72, 4, 1.5
BOS_UST = 1150
SIK_KAY = [1.4, -1.0, 1.8, -0.6, 0.8, -0.8, 0.6, 1.6, -1.2, 0.4, -0.8, 0.6]

# Tabler Icons bookmark (MIT License) - 24x24 viewBox, bounding box x: 6-18, y: 3-21
YERIMI_D = "M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"


def baslik_svg() -> str:
    """Başlık metni SVG çıktısı (SPEC §4)."""
    return (
        f'<text id="baslik" x="60" y="{BASLIK_TABAN}" font-family="Fredoka" font-weight="700" '
        f'font-size="{BASLIK_BOY}" fill="{R["murekkep"]}" xml:space="preserve">Hangisi doğru?</text>'
    )


def kok_svg() -> tuple[str, float]:
    """Kök grubu SVG çıktısı ve sağ sınır x1 (SPEC §4.1)."""
    bx0 = 60.0 + Y.genislik("Fredoka", 700, "My brother usually ", KOK_BOY)
    bx1 = bx0 + float(BOS_W)
    x0 = bx0 + 4.0
    x1 = bx1 - 4.0
    yb = float(L1 + BOS_KAYMA)
    xc = (x0 + x1) / 2.0
    yc = yb + 5.0
    y1 = yb + 1.0
    cizgi_d = f"M {x0:.1f} {yb:.1f} Q {xc:.1f} {yc:.1f} {x1:.1f} {y1:.1f}"
    svg = (
        '<g id="kok">\n'
        f'<text id="kok-s1" x="60" y="{L1}" font-family="Fredoka" font-weight="700" '
        f'font-size="{KOK_BOY}" fill="{R["murekkep"]}" xml:space="preserve">My brother usually</text>\n'
        f'<path id="kok-bos" d="{cizgi_d}" fill="none" stroke="{R["murekkep"]}" stroke-width="5" '
        'stroke-linecap="round"/>\n'
        f'<text id="kok-s2" x="60" y="{L2}" font-family="Fredoka" font-weight="700" '
        f'font-size="{KOK_BOY}" fill="{R["murekkep"]}" xml:space="preserve">to school by bus.</text>\n'
        '</g>'
    )
    return svg, x1


def otobus_svg() -> tuple[str, float]:
    """Otobüs SVG çıktısı ve kutu yüksekliği (SPEC §4.2)."""
    bus_path = Y.ORTAK / "cizim" / "coco" / "bus.svg"
    kok = ET.parse(str(bus_path)).getroot()
    vb = kok.get("viewBox", "")
    parts = [float(p) for p in vb.split()]
    vb_w, vb_h = parts[2], parts[3]
    oh = float(OTO_W) * vb_h / vb_w

    path_elem = None
    for elem in kok.iter():
        if elem.tag.endswith("path") and elem.get("fill") == "#030303":
            path_elem = elem
            break
    assert path_elem is not None, "Otobüs yol verisi (#030303) bulunamadı"

    d = path_elem.get("d", "")
    tr = path_elem.get("transform", "")
    svg = (
        f'<svg id="otobus" x="{OTO_X}" y="{OTO_Y}" width="{OTO_W}" height="{oh:.1f}" viewBox="{vb}">\n'
        f'<path d="{d}" transform="{tr}" fill="{R["murekkep"]}"/>\n'
        '</svg>'
    )
    return svg, oh


def kenar_yolu(x0: float, y0: float, x1: float, y1: float, kay: list[float]) -> str:
    """Şık kartı el çizimi kenar yolu (tek M + L dizisi, Z yok, SPEC §4.3)."""
    dx = x1 - x0
    dy = y1 - y0
    noktalar: list[tuple[float, float]] = [
        (x0 + 10.0, y0),
        (x0 + dx * 1.0 / 4.0, y0 + kay[0]),
        (x0 + dx * 2.0 / 4.0, y0 + kay[1]),
        (x0 + dx * 3.0 / 4.0, y0 + kay[2]),
        (x1, y0),
        (x1 + kay[3], y0 + dy * 1.0 / 4.0),
        (x1 + kay[4], y0 + dy * 2.0 / 4.0),
        (x1 + kay[5], y0 + dy * 3.0 / 4.0),
        (x1, y1),
        (x1 - dx * 1.0 / 4.0, y1 + kay[6]),
        (x1 - dx * 2.0 / 4.0, y1 + kay[7]),
        (x1 - dx * 3.0 / 4.0, y1 + kay[8]),
        (x0, y1),
        (x0 + kay[9], y1 - dy * 1.0 / 4.0),
        (x0 + kay[10], y1 - dy * 2.0 / 4.0),
        (x0 + kay[11], y1 - dy * 3.0 / 4.0),
        (x0, y0),
        (x0 + 24.0, y0),
    ]
    for p in noktalar:
        assert x0 - 2.5 <= p[0] <= x1 + 2.5, f"kenar x sınırı dışı: {p}"
        assert y0 - 2.5 <= p[1] <= y1 + 2.5, f"kenar y sınırı dışı: {p}"
    return "M " + f"{noktalar[0][0]:.1f} {noktalar[0][1]:.1f}" + " " + " ".join(
        f"L {p[0]:.1f} {p[1]:.1f}" for p in noktalar[1:]
    )


def secenek_karti_svg(grup_id: str, y0: int, harf: str, metin: str) -> str:
    """Şık kartı grubu SVG çıktısı (SPEC §4.3)."""
    cy = y0 + SIK_H // 2
    d = kenar_yolu(float(SIK_X0), float(y0), float(SIK_X1), float(y0 + SIK_H), SIK_KAY)
    return (
        f'<g id="{grup_id}">\n'
        f'<path id="{grup_id}-kenar" d="{d}" fill="none" stroke="{R["murekkep"]}" stroke-width="4" '
        'stroke-linecap="round" stroke-linejoin="round"/>\n'
        f'<circle id="{grup_id}-daire" cx="{DAIRE_X}" cy="{cy}" r="{DAIRE_R}" fill="none" '
        f'stroke="{R["murekkep"]}" stroke-width="4"/>\n'
        f'<text id="{grup_id}-harf" x="{DAIRE_X}" y="{cy + HARF_KAYMA}" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="{SIK_BOY}" fill="{R["murekkep"]}">{harf}</text>\n'
        f'<text id="{grup_id}-metin" x="{SIK_TX}" y="{cy + METIN_KAYMA}" font-family="Fredoka" '
        f'font-weight="700" font-size="{SIK_BOY}" fill="{R["murekkep"]}" xml:space="preserve">{metin}</text>\n'
        '</g>'
    )


def kural_svg() -> str:
    """Kural metni SVG çıktısı (SPEC §4)."""
    return (
        f'<text id="kural" x="60" y="{ALT_TABAN}" font-family="Caveat" font-weight="700" '
        f'font-size="{KURAL_BOY}" fill="{R["murekkep"]}" xml:space="preserve">usually = alışkanlık</text>'
    )


def kaydet_svg() -> str:
    """Kaydet grubu SVG çıktısı (SPEC §4.4)."""
    yazi_w = Y.genislik("Fredoka", 700, "Kaydet", KAYDET_BOY)
    yx0 = 958.0 - yazi_w
    hs = float(YI_SW) * float(YI_S) / 2.0
    tx = yx0 - 22.0 - hs - 18.0 * float(YI_S)
    ty = float(ALT_TABAN) - 25.0 - 12.0 * float(YI_S)
    return (
        '<g id="kaydet">\n'
        f'<g id="kaydet-ikon" transform="translate({tx:.1f} {ty:.1f}) scale({YI_S})" fill="none" '
        f'stroke="{R["murekkep"]}" stroke-width="{YI_SW}" stroke-linecap="round" stroke-linejoin="round">\n'
        f'<path id="kaydet-imi" d="{YERIMI_D}"/>\n'
        '</g>\n'
        f'<text id="kaydet-yazi" x="958" y="{ALT_TABAN}" text-anchor="end" font-family="Fredoka" '
        f'font-weight="700" font-size="{KAYDET_BOY}" fill="{R["murekkep"]}">Kaydet</text>\n'
        '</g>'
    )


def blok_kutulari(oh: float) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar (SPEC §5)."""
    w_kanal = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - 53.2
    kanal = {"ad": "kanal", "x": 53.2, "y": 291.0, "w": w_kanal, "h": 48.0}

    rz_x, rz_w = Y.rozet_konumlari()[0]
    kunye = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": rz_x + rz_w - 60.0, "h": 48.0}

    w_baslik = Y.genislik("Fredoka", 700, "Hangisi doğru?", BASLIK_BOY)
    baslik = {
        "ad": "baslik",
        "x": 60.0,
        "y": float(BASLIK_TABAN) - 0.74 * float(BASLIK_BOY),
        "w": w_baslik,
        "h": 0.98 * float(BASLIK_BOY),
    }

    bx0 = 60.0 + Y.genislik("Fredoka", 700, "My brother usually ", KOK_BOY)
    bx1 = bx0 + float(BOS_W)
    x1 = bx1 - 4.0
    w_s2 = Y.genislik("Fredoka", 700, "to school by bus.", KOK_BOY)
    kok_w = max(x1 + 2.5, 60.0 + w_s2) - 60.0
    kok_y = float(L1) - 0.74 * float(KOK_BOY)
    kok_h = (float(L2) + 0.24 * float(KOK_BOY)) - kok_y
    kok = {
        "ad": "kok",
        "x": 60.0,
        "y": kok_y,
        "w": kok_w,
        "h": kok_h,
    }

    otobus = {
        "ad": "otobus",
        "x": float(OTO_X),
        "y": float(OTO_Y),
        "w": float(OTO_W),
        "h": oh,
    }

    sikA = {
        "ad": "sikA",
        "x": float(SIK_X0) - 4.5,
        "y": float(SIK_Y[0]) - 4.5,
        "w": float(SIK_X1 - SIK_X0) + 9.0,
        "h": float(SIK_H) + 9.0,
    }

    sikB = {
        "ad": "sikB",
        "x": float(SIK_X0) - 4.5,
        "y": float(SIK_Y[1]) - 4.5,
        "w": float(SIK_X1 - SIK_X0) + 9.0,
        "h": float(SIK_H) + 9.0,
    }

    w_kural = Y.genislik("Caveat", 700, "usually = alışkanlık", KURAL_BOY)
    kural_y = float(ALT_TABAN) - 0.74 * float(KURAL_BOY)
    kural_h = 0.74 * float(KURAL_BOY) + 0.30 * float(KURAL_BOY)
    kural = {
        "ad": "kural",
        "x": 60.0,
        "y": kural_y,
        "w": w_kural,
        "h": kural_h,
    }

    yazi_w = Y.genislik("Fredoka", 700, "Kaydet", KAYDET_BOY)
    yx0 = 958.0 - yazi_w
    hs = float(YI_SW) * float(YI_S) / 2.0
    tx = yx0 - 22.0 - hs - 18.0 * float(YI_S)
    ty = float(ALT_TABAN) - 25.0 - 12.0 * float(YI_S)
    kx = tx + 6.0 * float(YI_S) - hs
    ky = min(ty + 3.0 * float(YI_S) - hs, float(ALT_TABAN) - 0.74 * float(KAYDET_BOY))
    kw = 958.0 - kx
    kh = max(ty + 21.0 * float(YI_S) + hs, float(ALT_TABAN) + 0.24 * float(KAYDET_BOY)) - ky
    kaydet = {
        "ad": "kaydet",
        "x": kx,
        "y": ky,
        "w": kw,
        "h": kh,
    }

    return [kanal, kunye, baslik, kok, otobus, sikA, sikB, kural, kaydet]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. İçerik blokları: x >= 60, x + w <= 960, y >= 460, y + h <= 1140
    for ad in ("baslik", "kok", "otobus", "sikA", "sikB", "kural", "kaydet"):
        b = b_dict[ad]
        assert b["x"] >= 60.0 - 1e-4, f"{ad} sol kenar {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ kenar {b['x'] + b['w']} > 960"
        assert b["y"] >= 460.0 - 1e-4, f"{ad} üst {b['y']} < 460"
        assert b["y"] + b["h"] <= 1140.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1140"

    # Bant denetimleri
    assert 460.0 - 1e-4 <= b_dict["baslik"]["y"] and b_dict["baslik"]["y"] + b_dict["baslik"]["h"] <= 560.0 + 1e-4
    assert 580.0 - 1e-4 <= b_dict["kok"]["y"] and b_dict["kok"]["y"] + b_dict["kok"]["h"] <= 740.0 + 1e-4
    assert 580.0 - 1e-4 <= b_dict["otobus"]["y"] and b_dict["otobus"]["y"] + b_dict["otobus"]["h"] <= 740.0 + 1e-4
    assert 770.0 - 1e-4 <= b_dict["sikA"]["y"] and b_dict["sikA"]["y"] + b_dict["sikA"]["h"] <= 870.0 + 1e-4
    assert 890.0 - 1e-4 <= b_dict["sikB"]["y"] and b_dict["sikB"]["y"] + b_dict["sikB"]["h"] <= 990.0 + 1e-4
    assert 1010.0 - 1e-4 <= b_dict["kural"]["y"] and b_dict["kural"]["y"] + b_dict["kural"]["h"] <= 1140.0 + 1e-4
    assert 1010.0 - 1e-4 <= b_dict["kaydet"]["y"] and b_dict["kaydet"]["y"] + b_dict["kaydet"]["h"] <= 1140.0 + 1e-4

    # 2. kanal ve kunye: y >= 280, y + h <= 450
    for ad in ("kanal", "kunye"):
        b = b_dict[ad]
        assert b["y"] >= 280.0 - 1e-4, f"{ad} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 450.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 450"

    # 3. Bütün blok çiftlerinin kesişim alanı 0
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    # 4. Dikey boşluk >= 12; Yatay boşluklar
    assert b_dict["baslik"]["y"] - (b_dict["kunye"]["y"] + b_dict["kunye"]["h"]) >= 12.0 - 1e-4
    assert b_dict["kok"]["y"] - (b_dict["baslik"]["y"] + b_dict["baslik"]["h"]) >= 12.0 - 1e-4
    assert b_dict["sikA"]["y"] - (b_dict["kok"]["y"] + b_dict["kok"]["h"]) >= 12.0 - 1e-4
    assert b_dict["sikA"]["y"] - (b_dict["otobus"]["y"] + b_dict["otobus"]["h"]) >= 12.0 - 1e-4
    assert b_dict["sikB"]["y"] - (b_dict["sikA"]["y"] + b_dict["sikA"]["h"]) >= 12.0 - 1e-4
    assert b_dict["kural"]["y"] - (b_dict["sikB"]["y"] + b_dict["sikB"]["h"]) >= 12.0 - 1e-4
    assert b_dict["kaydet"]["y"] - (b_dict["sikB"]["y"] + b_dict["sikB"]["h"]) >= 12.0 - 1e-4

    assert b_dict["kaydet"]["x"] - (b_dict["kural"]["x"] + b_dict["kural"]["w"]) >= 32.0 - 1e-4
    bx0 = 60.0 + Y.genislik("Fredoka", 700, "My brother usually ", KOK_BOY)
    bx1 = bx0 + float(BOS_W)
    x1 = bx1 - 4.0
    assert float(OTO_X) - (x1 + 2.5) >= 6.0 - 1e-4
    assert float(OTO_Y) - (float(L1) + 0.24 * float(KOK_BOY)) >= 12.0 - 1e-4

    # 5. Kök içi kuralları
    yb = float(L1 + BOS_KAYMA)
    assert (yb + 5.0 + 2.5) + 8.0 <= (float(L2) - 0.74 * float(KOK_BOY)) + 1e-4
    assert float(L1) - 0.74 * float(KOK_BOY) >= 580.0 - 1e-4

    # 6. Şık içi kuralları
    assert (float(DAIRE_X) + float(DAIRE_R) + 2.0) + 20.0 <= float(SIK_TX) + 1e-4
    for gid, y0, metin in [("sikA", SIK_Y[0], "goes"), ("sikB", SIK_Y[1], "is going")]:
        cy = float(y0) + float(SIK_H) / 2.0
        assert cy - (float(DAIRE_R) + 2.0) >= float(y0) + 4.0 - 1e-4
        assert cy + (float(DAIRE_R) + 2.0) <= float(y0 + SIK_H) - 4.0 + 1e-4
        h_taban = cy + float(HARF_KAYMA)
        assert h_taban - 0.74 * float(SIK_BOY) >= float(y0) + 4.0 - 1e-4
        assert h_taban + 0.24 * float(SIK_BOY) <= float(y0 + SIK_H) - 4.0 + 1e-4
        m_taban = cy + float(METIN_KAYMA)
        assert m_taban - 0.74 * float(SIK_BOY) >= float(y0) + 4.0 - 1e-4
        assert m_taban + 0.24 * float(SIK_BOY) <= float(y0 + SIK_H) - 4.0 + 1e-4
        w_m = Y.genislik("Fredoka", 700, metin, SIK_BOY)
        assert float(SIK_TX) + w_m <= float(SIK_X1) - 24.0 + 1e-4

    # 7. Kaydet kuralları
    yazi_w = Y.genislik("Fredoka", 700, "Kaydet", KAYDET_BOY)
    yx0 = 958.0 - yazi_w
    hs = float(YI_SW) * float(YI_S) / 2.0
    tx = yx0 - 22.0 - hs - 18.0 * float(YI_S)
    assert (tx + 18.0 * float(YI_S) + hs) + 20.0 <= yx0 + 1e-4
    assert 958.0 <= 960.0

    # 8. Ekran satırı <= 24 karakter (len)
    satirlar = [
        "Hangisi doğru?",
        "My brother usually ____",
        "to school by bus.",
        "A) goes",
        "B) is going",
        "usually = alışkanlık",
        "Kaydet",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 9. Yazı boyları >= 64 (künye ve kanal hariç)
    for boy in (BASLIK_BOY, KOK_BOY, SIK_BOY, KURAL_BOY, KAYDET_BOY):
        assert boy >= 64, f"Yazı boyu {boy} < 64"

    # 10. HTML id kontrolleri
    c_kanal = html.count('id="kanal"')
    assert c_kanal == 1, f"kanal id sayısı: {c_kanal}"
    c_logo = html.count('id="logoimg"')
    assert c_logo == 1, f"logoimg id sayısı: {c_logo}"
    yasak_tema = "#root" + ".tema-acik"
    assert yasak_tema not in html, f"{yasak_tema} HTML içinde olmamalı"
    assert 'id="rz1"' not in html, 'id="rz1" HTML içinde olmamalı'

    # 11. Beklenen kimlikler
    beklenen_kimlikler = [
        "baslik",
        "kok",
        "kok-s1",
        "kok-bos",
        "kok-s2",
        "otobus",
        "sikA",
        "sikA-kenar",
        "sikA-daire",
        "sikA-harf",
        "sikA-metin",
        "sikB",
        "sikB-kenar",
        "sikB-daire",
        "sikB-harf",
        "sikB-metin",
        "kural",
        "kaydet",
        "kaydet-ikon",
        "kaydet-imi",
        "kaydet-yazi",
    ]
    for kimlik in beklenen_kimlikler:
        assert f'id="{kimlik}"' in html, f'id="{kimlik}" HTML içinde bulunamadı'

    # 12. Tek sarı renk denetimi
    c_sari = html.lower().count("#f2a93b")
    assert c_sari == 1, f"sarı sayısı {c_sari} != 1"
    assert html.lower().count('stroke="#f2a93b"') == 0, "stroke=#f2a93b bulunmamalı"

    # 13. Cevap yok ve şık normalizasyonu
    def _norm_sik(s: str, gid: str, y0: int, h: str, m: str) -> str:
        r = s.replace(gid, "sikX")
        r = r.replace(f">{h}<", ">HARF<")
        r = r.replace(f">{m}<", ">METIN<")
        cy = y0 + SIK_H // 2
        r = r.replace(f'cy="{cy}"', 'cy="CY"')
        r = r.replace(f'y="{cy + HARF_KAYMA}"', 'y="HARF_Y"')
        r = r.replace(f'y="{cy + METIN_KAYMA}"', 'y="METIN_Y"')

        def _sub_d(m_obj: re.Match) -> str:
            d_str = m_obj.group(1)
            tokens = d_str.split()
            norm_tokens = []
            for i, tok in enumerate(tokens):
                if i % 3 == 2:
                    norm_tokens.append(f"{round(float(tok) - float(y0), 1):.1f}")
                else:
                    norm_tokens.append(tok)
            return f'd="{" ".join(norm_tokens)}"'

        r = re.sub(r'd="([^"]+)"', _sub_d, r)
        return r

    m_sikA = re.search(r'(<g id="sikA">.*?</g>)', html, re.DOTALL)
    m_sikB = re.search(r'(<g id="sikB">.*?</g>)', html, re.DOTALL)
    assert m_sikA, "sikA bulunamadı"
    assert m_sikB, "sikB bulunamadı"
    norm_A = _norm_sik(m_sikA.group(1), "sikA", SIK_Y[0], "A", "goes")
    norm_B = _norm_sik(m_sikB.group(1), "sikB", SIK_Y[1], "B", "is going")
    assert norm_A == norm_B, f"Normalleştirilmiş şıklar eşit değil:\n{norm_A}\n---\n{norm_B}"

    m_kok = re.search(r"<g id=\"kok\">(.*?)</g>", html, re.DOTALL)
    assert m_kok, "kok grubu bulunamadı"
    assert "goes" not in m_kok.group(1), "kok grubunda 'goes' bulundu"
    assert "is going" not in m_kok.group(1), "kok grubunda 'is going' bulundu"
    assert "#167a4a" not in html.lower(), "HTML'de #167a4a bulundu"

    # 14. Yasak içerikler
    for ch in html:
        o = ord(ch)
        assert not (o >= 0x1F000 or 0x2600 <= o <= 0x27BF), f"Yasak emoji karakteri: {ch} ({hex(o)})"
    assert "opacity:0" not in html, "HTML'de opacity:0 bulunmamalı"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    kunye_html = Y.kunye_svg()
    baslik_html = baslik_svg()
    kok_html, _ = kok_svg()
    otobus_html, oh = otobus_svg()
    sikA_html = secenek_karti_svg("sikA", SIK_Y[0], "A", "goes")
    sikB_html = secenek_karti_svg("sikB", SIK_Y[1], "B", "is going")
    kural_html = kural_svg()
    kaydet_html = kaydet_svg()

    bloklar = blok_kutulari(oh)

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}"
     data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye_html}
{baslik_html}
{kok_html}
{otobus_html}
{sikA_html}
{sikB_html}
{kural_html}
{kaydet_html}
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

    kurallari_dogrula(bloklar, html)
    return html, bloklar


if __name__ == "__main__":
    proje_dizini = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, bloklar = uret()
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
    (AD / "nesneler.json").write_text(
        json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"index.html yazıldı {len(html)}")
    b_dict = {b["ad"]: b for b in bloklar}
    satir2 = " ".join(
        f"{ad}={int(round(b_dict[ad]['y']))}-{int(round(b_dict[ad]['y'] + b_dict[ad]['h']))}"
        for ad in ["baslik", "kok", "otobus", "sikA", "sikB", "kural", "kaydet"]
    )
    print(satir2)

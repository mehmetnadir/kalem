#!/usr/bin/python3
"""02-04-ydt-temel-s3 sahne 05 kapak B (soru) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).

Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD / kanal katmanı (280-450) -> başlık (460-781) -> sahne (820-1380) -> alt bant (1380-1920 boş).
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# 1. zaman.json ve zamanlar.json okuma ve doğrulama (§3)
zaman_data: dict = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlari: list[dict] = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlari) == 1, f"duragan içinde {AD.name} kaydı tek olmalı"
duragan: dict = duragan_kayitlari[0]
assert duragan["kare"] == 1, f"kare {duragan['kare']} != 1"
assert duragan["cikti"] == "kapak-b.png", f"cikti {duragan['cikti']} != kapak-b.png"
assert AD.name not in [s["klasor"] for s in zaman_data.get("sahneler", [])], "AD.name sahneler içinde olmamalı"

Z: dict = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

# 2. Renk ve sabitler (§3)
R: dict[str, str] = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

ICERIK_SOL: float = 60.0
ICERIK_SAG: float = 960.0
ICERIK_UST: float = 460.0
ICERIK_ALT: float = 1380.0
UST_BOS: float = 280.0
MERKEZ_X: float = 510.0

K_TREN: float = 1.05
TX0: float = 64.0 + 10.0 * K_TREN + 2.0  # 76.5
TY0: float = 1010.0
RAY_Y: float = TY0 + 158.0 * K_TREN  # 1175.9

SC: tuple[float, float] = (TX0 + 87.5 * K_TREN, 934.0)
SR: float = 56.0

SH: float = 112.0
SY0: float = 880.0
SCX: float = TX0 + 237.5 * K_TREN
SX0: float = SCX - 0.31 * SH

KB: int = 72
kart_metin: str = "The train leaves \u2026"
metin_w: float = Y.genislik("Fredoka", 700, kart_metin, KB)
KW: float = metin_w + 80.0
LX: float = 102.0 + Y.genislik("Fredoka", 700, "The train ", KB)
LW: float = Y.genislik("Fredoka", 700, "leaves", KB)

LOGO_W: float = 48.0 * Y.LOGO_EN_BOY
LOGO_X: float = 60.0 - Y.LOGO_KAYMA * LOGO_W

KONU: str = "Simple Present vs Present Continuous"
ROZET: str = "YDT · TEMEL"
ROZET_W: float = Y.genislik("Lexend", 700, ROZET, 26) + 40.0

KB_K: int | None = None
for k in range(34, 27, -1):
    if 60.0 + Y.genislik("Fredoka", 700, KONU, k) + 20.0 + ROZET_W <= 960.0:
        KB_K = k
        break
assert KB_K is not None, "KB_K [28, 34] aralığında sığmadı"
ROZET_X: float = 60.0 + Y.genislik("Fredoka", 700, KONU, KB_K) + 20.0


def hesapla_s() -> tuple[int, float, float, float, float, float, float, float, float, float, float]:
    """Başlık font boyutu S ve yerleşim koordinatlarını hesaplar (§4.2)."""
    s0: float = 100.0
    g1_100: float = Y.genislik("Fredoka", 700, "NEDEN -ING", s0)
    g2_100: float = Y.genislik("Fredoka", 700, "YOK?", s0)
    S: int = math.floor(min(170.0, 900.0 * 100.0 / g1_100, 900.0 * 100.0 / (g2_100 + 60.0)))

    g1: float = Y.genislik("Fredoka", 700, "NEDEN -ING", S)
    g2: float = Y.genislik("Fredoka", 700, "YOK?", S)

    while (g1 > 900.0 or (g2 + 0.60 * S) > 900.0) and S > 1:
        S -= 1
        g1 = Y.genislik("Fredoka", 700, "NEDEN -ING", S)
        g2 = Y.genislik("Fredoka", 700, "YOK?", S)

    assert S == 164, f"Beklenen S=164 != {S}"
    T1: float = 476.0 + 0.70 * S
    x1: float = 510.0 - g1 / 2.0
    assert x1 >= 60.0, f"x1={x1} < 60"

    p: float = 0.30 * S
    hap_x: float = 510.0 - g2 / 2.0 - p
    hap_w: float = g2 + 2.0 * p
    hap_y: float = T1 + 0.16 * S
    hap_h: float = float(S)
    T2: float = hap_y + 0.85 * S
    x2: float = 510.0 - g2 / 2.0

    return S, g1, g2, T1, T2, x1, x2, hap_x, hap_w, hap_y, hap_h


def kutu_d(x: float, y: float, w: float, h: float, j: int = 0) -> str:
    """Yalnız M/L/Z komutlu el kutusu."""
    d0: float = 0.6 * math.sin(j * 1.7)
    d1: float = 0.6 * math.cos(j * 2.3)
    d2: float = 0.6 * math.sin(j * 3.1 + 1.0)
    d3: float = 0.6 * math.cos(j * 4.7 + 2.0)
    pts: list[tuple[float, float]] = [
        (x + d0, y + d1),
        (x + w * 0.5 + d2, y - 0.5 + d0),
        (x + w + d1, y + 0.3 + d3),
        (x + w + 0.5 + d3, y + h * 0.5 + d1),
        (x + w - 0.3 + d0, y + h + d2),
        (x + w * 0.5 + d1, y + h + 0.5 + d3),
        (x + 0.3 + d2, y + h + d0),
        (x - 0.4 + d3, y + h * 0.5 + d2),
    ]
    p_str: str = " ".join(f"L{px:.1f} {py:.1f}" for px, py in pts[1:])
    return f"M{pts[0][0]:.1f} {pts[0][1]:.1f} {p_str} Z"


def daire_d(cx: float, cy: float, r: float, ry: float | None = None) -> str:
    """29 noktalı, %4 kapanış paylı, yalnız M/L el dairesi."""
    if ry is None:
        ry = r
    pts: list[tuple[float, float]] = []
    for i in range(29):
        a: float = -math.pi / 2.0 + i * (2.0 * math.pi * 1.04) / 28.0
        wob: float = 1.0 + 0.02 * math.sin(a * 3.0)
        pts.append((cx + r * wob * math.cos(a), cy + ry * wob * math.sin(a)))
    return "M%.1f %.1f " % pts[0] + " ".join("L%.1f %.1f" % p for p in pts[1:])


def tren_svg(TX0: float, TY0: float, k: float) -> str:
    """Tren parçaları SVG çıktısı (§4.3)."""
    def P(x: float, y: float) -> tuple[float, float]:
        return TX0 + k * x, TY0 + k * y

    def K(x: float, y: float, w: float, h: float, j: int = 0) -> str:
        return kutu_d(TX0 + k * x, TY0 + k * y, k * w, k * h, j)

    def D(cx: float, cy: float, r: float, ry: float | None = None) -> str:
        return daire_d(TX0 + k * cx, TY0 + k * cy, k * r, k * ry if ry else None)

    parcalar: list[tuple[str, float, str]] = [
        (K(0, 45, 175, 85, 1), 4.5, ""),
        (K(200, 55, 170, 75, 2), 4.5, ""),
        (K(200, 10, 75, 45, 3), 4.5, ""),
        (K(320, 22, 26, 33, 4), 3.6, ""),
        (
            f"M{P(370, 95)[0]:.1f} {P(370, 95)[1]:.1f} L{P(398, 130)[0]:.1f} {P(398, 130)[1]:.1f} "
            f"L{P(370, 130)[0]:.1f} {P(370, 130)[1]:.1f}",
            4.5,
            "",
        ),
        (
            f"M{P(175, 112)[0]:.1f} {P(175, 112)[1]:.1f} L{P(200, 112)[0]:.1f} {P(200, 112)[1]:.1f}",
            3.6,
            "",
        ),
        (K(20, 60, 50, 30, 5), 3.6, ""),
        (K(100, 60, 50, 30, 6), 3.6, ""),
        (K(215, 20, 42, 25, 7), 3.6, ""),
        (D(40, 138, 17), 4.5, ""),
        (D(135, 138, 17), 4.5, ""),
        (D(240, 138, 17), 4.5, ""),
        (D(335, 138, 17), 4.5, ""),
        (
            f"M{P(-10, 158)[0]:.1f} {P(-10, 158)[1]:.1f} L{P(420, 158)[0]:.1f} {P(420, 158)[1]:.1f}",
            4.0,
            R["ikincil"],
        ),
        (D(345, 2, 11, 9), 3.4, R["ikincil"]),
        (D(372, -16, 8, 7), 3.4, R["ikincil"]),
    ]
    paths: list[str] = []
    for i, (d, w, renk) in enumerate(parcalar):
        renk_attr: str = f' stroke="{renk}"' if renk else ""
        paths.append(f'<path id="tr{i}" d="{d}" stroke-width="{w:.1f}"{renk_attr}/>')
    return f'<g id="tren">{"".join(paths)}</g>'


def saat_svg(SC: tuple[float, float], SR: float) -> str:
    """Saat SVG çıktısı (§4.3)."""
    cx, cy = SC
    kadran_d: str = daire_d(cx, cy, SR)
    centik_d: str = (
        f"M{cx:.1f} {cy - 0.80 * SR:.1f} L{cx:.1f} {cy - 0.66 * SR:.1f} "
        f"M{cx + 0.80 * SR:.1f} {cy:.1f} L{cx + 0.66 * SR:.1f} {cy:.1f} "
        f"M{cx:.1f} {cy + 0.80 * SR:.1f} L{cx:.1f} {cy + 0.66 * SR:.1f} "
        f"M{cx - 0.80 * SR:.1f} {cy:.1f} L{cx - 0.66 * SR:.1f} {cy:.1f}"
    )
    yelkovan_d: str = f"M{cx:.1f} {cy:.1f} L{cx:.1f} {cy - 0.66 * SR:.1f}"
    aci: float = 7.0 / 12.0 * 2.0 * math.pi
    akrep_d: str = (
        f"M{cx:.1f} {cy:.1f} L{cx + math.sin(aci) * 0.5 * SR:.1f} {cy - math.cos(aci) * 0.5 * SR:.1f}"
    )
    kadran: str = f'<path id="st-kadran" d="{kadran_d}" stroke-width="5"/>'
    centik: str = f'<path id="st-centik" d="{centik_d}" stroke-width="4"/>'
    yelkovan: str = f'<path id="st-yelkovan" d="{yelkovan_d}" stroke-width="5"/>'
    akrep: str = f'<path id="st-akrep" d="{akrep_d}" stroke-width="7"/>'
    return f'<g id="saat">{kadran}{centik}{yelkovan}{akrep}</g>'


def soru_svg(SX0: float, SY0: float, SH: float) -> str:
    """Soru işareti SVG çıktısı (§4.4)."""
    return (
        f'<g id="soru" transform="translate({SX0:.2f} {SY0:.2f}) scale({SH:.2f})" '
        f'fill="none" stroke="{R["vurgu"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'<path id="sr-govde" d="M0.05 0.27 C0.06 0.07 0.30 -0.01 0.47 0.05 C0.64 0.11 0.66 0.33 0.50 0.43 C0.36 0.52 0.31 0.56 0.31 0.72" stroke-width="{12.0 / SH:.4f}"/>'
        f'<path id="sr-nokta" d="M0.31 0.92 L0.311 0.92" stroke-width="{16.0 / SH:.4f}"/>'
        f'</g>'
    )


def kart_svg(KW: float, metin: str, LX: float, LW: float) -> str:
    """Kart SVG çıktısı (§4.5)."""
    kart_rect: str = (
        f'<rect id="kart" x="62" y="1256" width="{KW:.2f}" height="120" rx="28" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    kart_text: str = (
        f'<text id="kart-yazi" x="102" y="1341" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" style="font-kerning:none" xml:space="preserve">{metin}</text>'
    )
    alti_d: str = f"M{LX - 4.0:.1f} 1358 Q{LX + LW / 2.0:.1f} 1364 {LX + LW + 4.0:.1f} 1355"
    kart_alti: str = f'<path id="alti" d="{alti_d}" fill="none" stroke="{R["vurgu"]}" stroke-width="10" stroke-linecap="round"/>'
    return f"{kart_rect}{kart_text}{kart_alti}"


def kunye_svg(LOGO_X: float, LOGO_W: float, ROZET_X: float, ROZET_W: float) -> str:
    """Kanal katmanı ve rozet (<g id="kunye">) SVG çıktısı (§4.1)."""
    kanal = (
        f'<g id="kanal">'
        f'<image id="logoimg" href="assets/logo.svg" x="{LOGO_X:.2f}" y="291" width="{LOGO_W:.2f}" height="48"/>'
        f'<text id="kanal-ad" x="263" y="330" font-family="Lexend" font-weight="700" font-size="42" fill="{R["murekkep"]}">@ydspublishing</text>'
        f'</g>'
    )
    rz0 = (
        f'<g id="rz0">'
        f'<rect x="{ROZET_X:.2f}" y="386" width="{ROZET_W:.2f}" height="48" rx="24" fill="{R["vurgu"]}"/>'
        f'<text x="{ROZET_X + ROZET_W / 2.0:.2f}" y="419.4" text-anchor="middle" '
        f'font-family="Lexend" font-weight="700" font-size="26" fill="{R["zemin"]}">YDT · TEMEL</text>'
        f'</g>'
    )
    return f'<g id="kunye">{kanal}{rz0}</g>'


def baslik_svg(
    S: int,
    T1: float,
    T2: float,
    x1: float,
    x2: float,
    hap_x: float,
    hap_y: float,
    hap_w: float,
    hap_h: float,
) -> str:
    """Başlık (<g id="baslik">) SVG çıktısı (§4.2)."""
    rx_hap: float = S / 2.0
    bs_1: str = (
        f'<text id="bs-1" x="{x1:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">NEDEN -ING</text>'
    )
    bk_hap: str = (
        f'<rect id="bk-hap" x="{hap_x:.2f}" y="{hap_y:.2f}" width="{hap_w:.2f}" height="{hap_h:.2f}" '
        f'rx="{rx_hap:.2f}" fill="{R["vurgu"]}"/>'
    )
    bs_2: str = (
        f'<text id="bs-2" x="{x2:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["zemin"]}" style="font-kerning:none" xml:space="preserve">YOK?</text>'
    )
    return f'<g id="baslik">{bs_1}{bk_hap}{bs_2}</g>'


def eskiz_svg(TX0: float, TY0: float, K_TREN: float, SC: tuple[float, float], SR: float) -> str:
    """Sahne eskiz grubu (<g id="eskiz">) SVG çıktısı (§4.3)."""
    tren: str = tren_svg(TX0, TY0, K_TREN)
    saat: str = saat_svg(SC, SR)
    return (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{tren}{saat}</g>'
    )


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx: float = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy: float = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def karakter_hazirla(hedef: Path) -> tuple[int, int, int, int]:
    """Karakter görselini kırıntılardan temizleyip kırparak proje/assets'e kaydeder (§4.6)."""
    kaynak: Path = PAKET / "ortak" / "kapak" / "karakter.png"
    im: Image.Image = Image.open(kaynak)
    assert im.size == (896, 1200), f"karakter boyutu {im.size} != (896, 1200)"
    assert im.mode == "RGBA", f"karakter modu {im.mode} != RGBA"
    a = im.split()[-1]
    m = a.point(lambda v: 255 if v > 64 else 0).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    im.putalpha(ImageChops.multiply(a, m))
    bbox = im.split()[-1].getbbox()
    assert bbox is not None, "karakter alfasında getbbox None döndü"
    kirpilan = im.crop(bbox)
    hedef.parent.mkdir(parents=True, exist_ok=True)
    kirpilan.save(hedef)
    return bbox


def blok_kutulari(
    S: int,
    g1: float,
    T1: float,
    x1: float,
    hap_x: float,
    hap_y: float,
    hap_w: float,
    hap_h: float,
    SC: tuple[float, float],
    SR: float,
    SX0: float,
    SY0: float,
    SH: float,
    KW: float,
    metin_w: float,
    LX: float,
    LW: float,
    KX: float,
    KY: float,
    KW_K: float,
    KH_K: float,
    DX: float,
    DY: float,
    DR: float,
) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını döndürür (§5.1)."""
    kanal_w: float = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - LOGO_X
    b_kanal: dict[str, float] = {"ad": "kanal", "x": LOGO_X, "y": 291.0, "w": kanal_w, "h": 48.0}
    b_rozet: dict[str, float] = {"ad": "rozet", "x": ROZET_X, "y": 386.0, "w": ROZET_W, "h": 48.0}

    bas_x: float = min(x1 - 6.0, hap_x)
    bas_sag: float = max(x1 + g1 + 6.0, hap_x + hap_w)
    bas_y: float = T1 - 0.70 * S - 6.0
    bas_alt: float = hap_y + hap_h
    b_baslik: dict[str, float] = {
        "ad": "baslik",
        "x": bas_x,
        "y": bas_y,
        "w": bas_sag - bas_x,
        "h": bas_alt - bas_y,
    }

    b_bk_hap: dict[str, float] = {"ad": "bk-hap", "x": hap_x, "y": hap_y, "w": hap_w, "h": hap_h}

    r_box: float = 1.02 * SR + 2.5
    b_saat: dict[str, float] = {
        "ad": "saat",
        "x": SC[0] - r_box,
        "y": SC[1] - r_box,
        "w": 2.0 * r_box,
        "h": 2.0 * r_box,
    }

    b_soru: dict[str, float] = {
        "ad": "soru",
        "x": SX0 - 6.0,
        "y": SY0 - 6.0,
        "w": 0.62 * SH + 12.0,
        "h": 0.92 * SH + 14.0,
    }

    b_duman: dict[str, float] = {
        "ad": "duman",
        "x": TX0 + 334.0 * K_TREN - 2.0,
        "y": TY0 - 23.0 * K_TREN - 2.0,
        "w": (TX0 + 380.0 * K_TREN + 2.0) - (TX0 + 334.0 * K_TREN - 2.0),
        "h": (TY0 + 11.0 * K_TREN + 2.0) - (TY0 - 23.0 * K_TREN - 2.0),
    }

    b_tren: dict[str, float] = {
        "ad": "tren",
        "x": TX0 - 10.0 * K_TREN - 2.0,
        "y": TY0 + 10.0 * K_TREN - 3.0,
        "w": (TX0 + 420.0 * K_TREN + 2.0) - (TX0 - 10.0 * K_TREN - 2.0),
        "h": (RAY_Y + 2.0) - (TY0 + 10.0 * K_TREN - 3.0),
    }

    b_kart: dict[str, float] = {"ad": "kart", "x": 60.0, "y": 1254.0, "w": KW + 4.0, "h": 124.0}
    b_kart_yazi: dict[str, float] = {
        "ad": "kart-yazi",
        "x": 102.0,
        "y": 1341.0 - 0.75 * 72.0,
        "w": metin_w,
        "h": 72.0,
    }
    b_alti: dict[str, float] = {"ad": "alti", "x": LX - 9.0, "y": 1350.0, "w": LW + 18.0, "h": 19.0}
    b_karakter: dict[str, float] = {
        "ad": "karakter",
        "x": KX - 10.0,
        "y": KY - 10.0,
        "w": KW_K + 20.0,
        "h": KH_K + 20.0,
    }
    b_daire: dict[str, float] = {
        "ad": "daire",
        "x": DX - DR,
        "y": DY - DR,
        "w": 2.0 * DR,
        "h": 2.0 * DR,
    }

    return [
        b_kanal,
        b_rozet,
        b_baslik,
        b_bk_hap,
        b_saat,
        b_soru,
        b_duman,
        b_tren,
        b_kart,
        b_kart_yazi,
        b_alti,
        b_karakter,
        b_daire,
    ]


def kurallari_dogrula(
    bloklar: list[dict[str, float]],
    S: int,
    KB: int,
    html: str,
    x1: float,
    g1: float,
    DR: float,
) -> None:
    """SPEC.md §5.2 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict: dict[str, dict[str, float]] = {b["ad"]: b for b in bloklar}

    # 1. Bant: her blok y >= 280, alt <= 1380, sağ <= 960; kanal dışındaki her blok x >= 60
    for b in bloklar:
        assert b["y"] >= 280.0 - 1e-4, f"{b['ad']} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 1380.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1380"
        if b["ad"] == "kanal":
            assert b["x"] >= 53.0 - 1e-4, f"kanal sol {b['x']} < 53"
            assert b["x"] + b["w"] <= 960.0 + 1e-4, f"kanal sağ {b['x'] + b['w']} > 960"
        elif b["ad"] == "baslik":
            assert x1 >= 60.0 - 1e-4, f"baslik sol {x1} < 60"
            assert x1 + g1 <= 960.0 + 1e-4, f"baslik sağ {x1 + g1} > 960"
        else:
            assert b["x"] >= 60.0 - 1e-4, f"{b['ad']} sol {b['x']} < 60"
            assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{b['ad']} sağ {b['x'] + b['w']} > 960"

    # Başlık ve sahne blokları y >= 460
    for name in ["baslik", "saat", "soru", "duman", "tren", "kart", "karakter", "daire"]:
        assert b_dict[name]["y"] >= 460.0 - 1e-4, f"{name} üst {b_dict[name]['y']} < 460"

    # 2. Kesişim 0
    ciftler: list[str] = ["kanal", "rozet", "baslik", "saat", "soru", "duman", "tren", "kart", "karakter"]
    for i in range(len(ciftler)):
        for j in range(i + 1, len(ciftler)):
            n1, n2 = ciftler[i], ciftler[j]
            if {n1, n2} == {"duman", "tren"}:
                continue
            k: float = kesisim(b_dict[n1], b_dict[n2])
            assert k == 0.0, f"Kesişim {n1} - {n2}: {k}"

    for name in ["kanal", "rozet", "baslik", "saat", "soru", "duman", "tren", "kart"]:
        k = kesisim(b_dict["daire"], b_dict[name])
        assert k == 0.0, f"Kesişim daire - {name}: {k}"

    # Kapsama: bk-hap ⊂ baslik; kart-yazi ⊂ kart; alti ⊂ kart
    for child, parent in [("bk-hap", "baslik"), ("kart-yazi", "kart"), ("alti", "kart")]:
        assert b_dict[child]["x"] >= b_dict[parent]["x"] - 1e-4, f"{child} sol kenar {parent} dışında"
        assert (
            b_dict[child]["x"] + b_dict[child]["w"] <= b_dict[parent]["x"] + b_dict[parent]["w"] + 1e-4
        ), f"{child} sağ kenar {parent} dışında"
        assert b_dict[child]["y"] >= b_dict[parent]["y"] - 1e-4, f"{child} üst kenar {parent} dışında"
        assert (
            b_dict[child]["y"] + b_dict[child]["h"] <= b_dict[parent]["y"] + b_dict[parent]["h"] + 1e-4
        ), f"{child} alt kenar {parent} dışında"

    # 3. Boşluk
    assert b_dict["rozet"]["y"] - (b_dict["kanal"]["y"] + b_dict["kanal"]["h"]) >= 40.0 - 1e-4
    assert b_dict["baslik"]["y"] - (b_dict["rozet"]["y"] + b_dict["rozet"]["h"]) >= 24.0 - 1e-4
    assert b_dict["karakter"]["y"] - (b_dict["baslik"]["y"] + b_dict["baslik"]["h"]) >= 24.0 - 1e-4
    for n in ["saat", "soru", "duman"]:
        assert b_dict[n]["y"] - (b_dict["baslik"]["y"] + b_dict["baslik"]["h"]) >= 48.0 - 1e-4
    assert b_dict["tren"]["y"] - (b_dict["saat"]["y"] + b_dict["saat"]["h"]) >= 16.0 - 1e-4
    assert b_dict["tren"]["y"] - (b_dict["soru"]["y"] + b_dict["soru"]["h"]) >= 16.0 - 1e-4
    assert b_dict["kart"]["y"] - (b_dict["tren"]["y"] + b_dict["tren"]["h"]) >= 20.0 - 1e-4
    assert b_dict["kart"]["y"] - (b_dict["karakter"]["y"] + b_dict["karakter"]["h"]) >= 16.0 - 1e-4
    max_tren_duman_sag: float = max(
        b_dict["tren"]["x"] + b_dict["tren"]["w"], b_dict["duman"]["x"] + b_dict["duman"]["w"]
    )
    assert b_dict["karakter"]["x"] - max_tren_duman_sag >= 24.0 - 1e-4
    assert b_dict["duman"]["x"] - (b_dict["soru"]["x"] + b_dict["soru"]["w"]) >= 24.0 - 1e-4
    assert b_dict["soru"]["x"] - (b_dict["saat"]["x"] + b_dict["saat"]["w"]) >= 24.0 - 1e-4
    assert DR >= 100.0 - 1e-4

    # 4. Yazı boyu
    assert S >= 64, f"Başlık boyutu {S} < 64"
    assert KB == 72, f"Kart yazı boyutu {KB} != 72"

    satirlar: list[str] = ["@ydspublishing", "YDT · TEMEL", "NEDEN -ING", "YOK?", "The train leaves \u2026"]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    baslik_satirlari: list[str] = ["NEDEN -ING", "YOK?"]
    assert len(baslik_satirlari) == 2, f"Başlık satır sayısı {len(baslik_satirlari)} != 2"
    baslik_sozcukleri: list[str] = " ".join(baslik_satirlari).split()
    assert len(baslik_sozcukleri) == 3, f"Başlık sözcük sayısı {len(baslik_sozcukleri)} != 3"
    assert "İ" not in " ".join(baslik_satirlari), "Başlıkta Türkçe İ harfi yasak"
    assert "\u0049" in "NEDEN -ING", "-ING içinde U+0049 I harfi olmalı"

    # 5. Zorunlu
    zorunlu_ifadeler: list[str] = [
        'id="kunye"',
        'id="kanal"',
        "@ydspublishing",
        "assets/logo.svg",
        'id="karakter"',
        "assets/karakter.png",
        'id="daire"',
        "drop-shadow",
    ]
    for z in zorunlu_ifadeler:
        assert z in html, f"Zorunlu ifade eksik: {z}"

    kunye_m = re.search(r'<g id="kunye">(.*?)</g>', html, re.DOTALL)
    assert kunye_m is not None, "id kunye grubu bulunamadi"
    assert 'id="kanal"' in kunye_m.group(1), 'id="kanal" ogesi id="kunye" grubunun icinde olmali'

    # 6. Yasak
    html_lower: str = html.lower()
    yasak_kelimeler: list[str] = [
        "tam ders",
        "dakika",
        "qr",
        "izle",
        "tarife",
        "timetable",
        "6 dk",
        "simple present",
        "text-transform",
        "math.random",
        "date.now",
        "new date",
        "opacity:0",
        "<circle",
        "altyazi",
    ]
    for yk in yasak_kelimeler:
        assert yk not in html_lower, f"Yasak ifade bulundu: {yk}"

    assert 'id="t2"' not in html, "id t2 yasak"
    assert 'id="ku-nokta"' not in html, "id ku-nokta yasak"
    assert 'id="rz1"' not in html, "id rz1 yasak"
    # hf_tema bu dizgeyi "tema CSS'i var" sayar, açık tema koyu çıkar (sözleşme satır 75, 79)
    assert "#root.tema-acik" not in html, "#root.tema-acik dizgesi yasak"

    hex_kumesi: set[str] = set(re.findall(r"#[0-9a-f]{6}\b", html_lower))
    izin_verilen_hex: set[str] = {"#1b1a17", "#f3efe6", "#c9c2b3", "#f2a93b"}
    assert hex_kumesi.issubset(izin_verilen_hex), f"İzinsiz hex renk(ler): {hex_kumesi - izin_verilen_hex}"

    for ch in html:
        assert ord(ch) < 0x1F000, f"Emoji karakteri yasak: {ch}"


def uret() -> tuple[str, int, float, int, float, float, float, float, float, list[dict[str, float]]]:
    """Sahne HTML'i, font boyutları ve nesnelerini üretir."""
    S, g1, g2, T1, T2, x1, x2, hap_x, hap_w, hap_y, hap_h = hesapla_s()
    baslik_alt: float = hap_y + hap_h

    hedef_karakter: Path = AD / "proje" / "assets" / "karakter.png"
    bx0, by0, bx1, by1 = karakter_hazirla(hedef_karakter)

    SK: float = 520.0 / 1200.0
    KW_K: float = (bx1 - bx0) * SK
    KH_K: float = (by1 - by0) * SK
    KX: float = 948.0 - KW_K
    KY: float = 820.0

    DX: float = KX + (461.0 - bx0) * SK
    DY: float = KY + (470.0 - by0) * SK
    DR: float = min(0.36 * KH_K, DY - (baslik_alt + 16.0), 960.0 - DX)

    kunye: str = kunye_svg(LOGO_X, LOGO_W, ROZET_X, ROZET_W)
    baslik: str = baslik_svg(S, T1, T2, x1, x2, hap_x, hap_y, hap_w, hap_h)
    eskiz: str = eskiz_svg(TX0, TY0, K_TREN, SC, SR)
    soru: str = soru_svg(SX0, SY0, SH)
    kart: str = kart_svg(KW, kart_metin, LX, LW)

    adim: float = 10.0 / 3.0
    kenar_filter: str = " ".join(
        f"drop-shadow({dx:.2f}px {dy:.2f}px 0 {R['murekkep']})"
        for _ in range(3)
        for dx, dy in ((adim, 0), (-adim, 0), (0, adim), (0, -adim))
    )

    html: str = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
.kenar{{filter:{kenar_filter};}}
#daire{{display:none;border-radius:50%;background:#f3efe6;}}
.tema-acik #daire{{display:block;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<div id="daire" class="abs" style="left:{DX - DR:.1f}px;top:{DY - DR:.1f}px;width:{2.0 * DR:.1f}px;height:{2.0 * DR:.1f}px"></div>
<img id="karakter" class="abs kenar" src="assets/karakter.png" alt="" style="left:{KX:.1f}px;top:{KY:.1f}px;width:{KW_K:.1f}px;height:{KH_K:.1f}px">
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{baslik}
{eskiz}
{soru}
{kart}
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

    bloklar: list[dict[str, float]] = blok_kutulari(
        S,
        g1,
        T1,
        x1,
        hap_x,
        hap_y,
        hap_w,
        hap_h,
        SC,
        SR,
        SX0,
        SY0,
        SH,
        KW,
        metin_w,
        LX,
        LW,
        KX,
        KY,
        KW_K,
        KH_K,
        DX,
        DY,
        DR,
    )

    kurallari_dogrula(bloklar, S, KB, html, x1, g1, DR)
    return html, S, KW, KB_K, KX, KY, KW_K, KH_K, DR, bloklar


if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, S, KW, KB_K, KX, KY, KW_K, KH_K, DR, bloklar = uret()
    (proje_dizini / "index.html").write_text(html, encoding="utf-8")

    nesneler: list[dict[str, str | int]] = [
        {
            "ad": str(b["ad"]),
            "x": int(round(b["x"])),
            "y": int(round(b["y"])),
            "w": int(round(b["w"])),
            "h": int(round(b["h"])),
        }
        for b in bloklar
    ]
    (AD / "nesneler.json").write_text(json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"index.html yazıldı {len(html)}")
    print(f"S={S} KW={KW:.1f} KB_K={KB_K} karakter={KX:.1f},{KY:.1f},{KW_K:.1f},{KH_K:.1f} daire r={DR:.1f}")

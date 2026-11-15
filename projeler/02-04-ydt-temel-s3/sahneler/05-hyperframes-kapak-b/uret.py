#!/usr/bin/python3
"""02-04-ydt-temel-s3 sahne 05 kapak B (soru) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).

Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> başlık -> sahne (864-1344) -> platform (1536-1920 boş).
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

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

W: int = Y.W
H: int = Y.H
KENAR: int = 48
SAG: int = 1032
BASLIK_GEN: int = 952
BANT_UST: int = 864
BANT_ALT: int = 1344
PLATFORM: int = 1536

K_TREN: float = 1.1
TX0: float = 196.0
RAY_Y: float = 1172.0
TY0: float = RAY_Y - 158.0 * K_TREN

FIG: dict = json.loads((AD / "cizim" / "ogretmen.json").read_text(encoding="utf-8"))


def hesapla_s() -> tuple[int, float, float, float, float, float, float, float, float, float, float]:
    """Başlık font boyutu S ve yerleşim koordinatlarını hesaplar (§4.2)."""
    s0: float = 100.0
    g1_100: float = Y.genislik("Fredoka", 700, "NEDEN -ING", s0)
    g2_100: float = Y.genislik("Fredoka", 700, "YOK?", s0)
    S: int = math.floor(min(190.0, BASLIK_GEN * 100.0 / g1_100, BASLIK_GEN * 100.0 / (g2_100 + 60.0)))

    g1: float = Y.genislik("Fredoka", 700, "NEDEN -ING", S)
    g2: float = Y.genislik("Fredoka", 700, "YOK?", S)

    while (g1 > BASLIK_GEN or (g2 + 0.60 * S) > BASLIK_GEN) and S > 1:
        S -= 1
        g1 = Y.genislik("Fredoka", 700, "NEDEN -ING", S)
        g2 = Y.genislik("Fredoka", 700, "YOK?", S)

    assert g1 <= BASLIK_GEN, f"g1={g1} > {BASLIK_GEN}"
    assert g2 + 0.60 * S <= BASLIK_GEN, f"g2 + 0.60*S={g2 + 0.60 * S} > {BASLIK_GEN}"

    T1: float = 375.0 + 0.70 * S
    T2: float = T1 + 1.26 * S
    x1: float = 540.0 - g1 / 2.0
    p: float = 0.30 * S
    hap_x: float = 540.0 - g2 / 2.0 - p
    hap_w: float = g2 + 2.0 * p
    hap_y: float = T2 - 0.90 * S
    hap_h: float = 1.10 * S
    x2: float = 540.0 - g2 / 2.0

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


def figur_svg(FIG_SOL: float, FIG_UST: float, fs: float, x1: float, y0: float) -> str:
    """Figür SVG çıktısı (§4.3)."""
    fig_kalinlik: dict[str, float] = {"govde": 4.4, "sac": 3.6, "yuz": 2.6}
    fig_paths: str = "".join(
        f'<path id="f{i}" d="{p["d"]}" stroke-width="{fig_kalinlik.get(p["parca"], 4.4) / fs:.3f}"/>'
        for i, p in enumerate(FIG["yollar"])
    )
    return (
        f'<g id="fig" transform="translate({FIG_SOL + x1 * fs:.2f} {FIG_UST - y0 * fs:.2f}) '
        f'scale({-fs:.6f} {fs:.6f})">{fig_paths}</g>'
    )


def ok_svg(
    S_ok: tuple[float, float],
    E_ok: tuple[float, float],
    C_ok: tuple[float, float],
    uc1: tuple[float, float],
    uc2: tuple[float, float],
) -> str:
    """Kalem oku SVG çıktısı (§4.3)."""
    ok_g_d: str = f"M{S_ok[0]:.1f} {S_ok[1]:.1f} Q{C_ok[0]:.1f} {C_ok[1]:.1f} {E_ok[0]:.1f} {E_ok[1]:.1f}"
    ok_b_d: str = f"M{uc1[0]:.1f} {uc1[1]:.1f} L{E_ok[0]:.1f} {E_ok[1]:.1f} L{uc2[0]:.1f} {uc2[1]:.1f}"
    ok_g: str = f'<path id="ok-g" d="{ok_g_d}" stroke-width="6"/>'
    ok_b: str = f'<path id="ok-b" d="{ok_b_d}" stroke-width="6"/>'
    return f'<g id="ok">{ok_g}{ok_b}</g>'


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
    kart_rect: str = f'<rect id="kart" x="66" y="1202" width="{KW:.2f}" height="140" rx="28" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    kart_text: str = (
        f'<text id="kart-yazi" x="106" y="1294" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" style="font-kerning:none" xml:space="preserve">{metin}</text>'
    )
    alti_d: str = f"M{LX - 4.0:.1f} 1314 Q{LX + LW / 2.0:.1f} 1320 {LX + LW + 4.0:.1f} 1311"
    kart_alti: str = f'<path id="alti" d="{alti_d}" fill="none" stroke="{R["vurgu"]}" stroke-width="10" stroke-linecap="round"/>'
    return f"{kart_rect}{kart_text}{kart_alti}"


def kunye_svg() -> str:
    """HUD (<g id="kunye">) SVG çıktısı (§4.1)."""
    logo_w: float = 96.0 * Y.LOGO_EN_BOY
    logo: str = f'<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" width="{logo_w:.2f}" height="96"/></g>'
    rz_w: float = Y.genislik("Lexend", 700, "YDT · BASIC", 36.0) + 56.0
    rz_x: float = 48.0
    rz_ortax: float = rz_x + rz_w / 2.0
    rozet: str = (
        f'<g id="rz0">'
        f'<rect x="{rz_x:.1f}" y="216" width="{rz_w:.1f}" height="72" rx="36" fill="{R["vurgu"]}"/>'
        f'<text x="{rz_ortax:.1f}" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" fill="{R["zemin"]}">YDT · BASIC</text>'
        f'</g>'
    )
    return f'<g id="kunye">{logo}{rozet}</g>'


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
    rx_hap: float = hap_h / 2.0
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


def sahne_svg(
    FIG_SOL: float,
    FIG_UST: float,
    fs: float,
    x1: float,
    y0: float,
    SC: tuple[float, float],
    SR: float,
    S_ok: tuple[float, float],
    E_ok: tuple[float, float],
    C_ok: tuple[float, float],
    uc1: tuple[float, float],
    uc2: tuple[float, float],
) -> str:
    """Sahne grubu (<g id="eskiz">) SVG çıktısı (§4.3)."""
    zc: str = f'<path id="zc" d="M{FIG_SOL - 24.0:.1f} 1342 L1016 1342" stroke-width="4"/>'
    tren: str = tren_svg(TX0, TY0, K_TREN)
    saat: str = saat_svg(SC, SR)
    figur: str = figur_svg(FIG_SOL, FIG_UST, fs, x1, y0)
    ok: str = ok_svg(S_ok, E_ok, C_ok, uc1, uc2)
    return (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{zc}{tren}{saat}{figur}{ok}</g>'
    )


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx: float = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy: float = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def blok_kutulari(
    S: int,
    g1: float,
    T1: float,
    T2: float,
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
    FIG_SOL: float,
    FIG_UST: float,
    fs: float,
    x0: float,
    x1_fig: float,
    FIG_H: float,
    ok_box: dict[str, float],
) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını döndürür (§6.1, §6.4)."""
    hud: dict[str, float] = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}

    bas_x: float = min(x1, hap_x)
    bas_sag: float = max(x1 + g1, hap_x + hap_w)
    bas_y: float = T1 - 0.75 * S
    bas_h: float = (T2 + 0.20 * S) - bas_y
    baslik: dict[str, float] = {"ad": "baslik", "x": bas_x, "y": bas_y, "w": bas_sag - bas_x, "h": bas_h}

    bk_hap_kutu: dict[str, float] = {"ad": "bk-hap", "x": hap_x, "y": hap_y, "w": hap_w, "h": hap_h}

    r_box: float = 1.02 * SR + 2.5
    saat: dict[str, float] = {
        "ad": "saat",
        "x": SC[0] - r_box,
        "y": SC[1] - r_box,
        "w": 2.0 * r_box,
        "h": 2.0 * r_box,
    }

    soru: dict[str, float] = {
        "ad": "soru",
        "x": SX0 - 6.0,
        "y": SY0 - 6.0,
        "w": 0.62 * SH + 12.0,
        "h": 0.92 * SH + 14.0,
    }

    duman: dict[str, float] = {
        "ad": "duman",
        "x": TX0 + 334.0 * K_TREN - 2.0,
        "y": TY0 - 23.0 * K_TREN - 2.0,
        "w": (TX0 + 380.0 * K_TREN + 2.0) - (TX0 + 334.0 * K_TREN - 2.0),
        "h": (TY0 + 11.0 * K_TREN + 2.0) - (TY0 - 23.0 * K_TREN - 2.0),
    }

    tren: dict[str, float] = {
        "ad": "tren",
        "x": TX0 - 10.0 * K_TREN - 2.0,
        "y": TY0 + 10.0 * K_TREN - 3.0,
        "w": (TX0 + 420.0 * K_TREN + 2.0) - (TX0 - 10.0 * K_TREN - 2.0),
        "h": (RAY_Y + 2.0) - (TY0 + 10.0 * K_TREN - 3.0),
    }

    kart: dict[str, float] = {"ad": "kart", "x": 64.0, "y": 1200.0, "w": KW + 4.0, "h": 144.0}
    kart_yazi: dict[str, float] = {
        "ad": "kart-yazi",
        "x": 106.0,
        "y": 1294.0 - 0.75 * 72.0,
        "w": metin_w,
        "h": 72.0,
    }
    alti: dict[str, float] = {"ad": "alti", "x": LX - 9.0, "y": 1306.0, "w": LW + 18.0, "h": 19.0}
    fig: dict[str, float] = {"ad": "fig", "x": FIG_SOL, "y": FIG_UST, "w": (x1_fig - x0) * fs, "h": FIG_H}

    return [hud, baslik, bk_hap_kutu, saat, soru, duman, tren, kart, kart_yazi, alti, fig, ok_box]


def kurallari_dogrula(bloklar: list[dict[str, float]], S: int, KB: int, html: str) -> None:
    """SPEC.md §6 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict: dict[str, dict[str, float]] = {b["ad"]: b for b in bloklar}

    # 1. Bütün bloklar x in [48, 1032], y >= 0, alt <= 1344
    for b in bloklar:
        assert b["x"] >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0, f"{b['ad']} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1344.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1344"

    # Başlık ve sahne blokları x in [64, 1016]
    for name in ["baslik", "saat", "soru", "duman", "tren", "kart", "fig", "ok"]:
        b = b_dict[name]
        assert b["x"] >= 64.0 - 1e-4, f"{name} sol {b['x']} < 64"
        assert b["x"] + b["w"] <= 1016.0 + 1e-4, f"{name} sağ {b['x'] + b['w']} > 1016"

    # Sahne blokları y >= 864
    for name in ["saat", "soru", "duman", "tren", "kart", "fig", "ok"]:
        b = b_dict[name]
        assert b["y"] >= 864.0 - 1e-4, f"{name} üst {b['y']} < 864"

    # Kapsama kontrolleri
    assert b_dict["bk-hap"]["x"] >= b_dict["baslik"]["x"] - 1e-4, "bk-hap baslik icinde olmali (sol)"
    assert b_dict["bk-hap"]["x"] + b_dict["bk-hap"]["w"] <= b_dict["baslik"]["x"] + b_dict["baslik"]["w"] + 1e-4, "bk-hap baslik icinde olmali (sag)"
    assert b_dict["bk-hap"]["y"] >= b_dict["baslik"]["y"] - 1e-4, "bk-hap baslik icinde olmali (ust)"
    assert b_dict["bk-hap"]["y"] + b_dict["bk-hap"]["h"] <= b_dict["baslik"]["y"] + b_dict["baslik"]["h"] + 1e-4, "bk-hap baslik icinde olmali (alt)"

    assert b_dict["kart-yazi"]["x"] >= b_dict["kart"]["x"] - 1e-4, "kart-yazi kart icinde olmali (sol)"
    assert b_dict["kart-yazi"]["x"] + b_dict["kart-yazi"]["w"] <= b_dict["kart"]["x"] + b_dict["kart"]["w"] + 1e-4, "kart-yazi kart icinde olmali (sag)"
    assert b_dict["kart-yazi"]["y"] >= b_dict["kart"]["y"] - 1e-4, "kart-yazi kart icinde olmali (ust)"
    assert b_dict["kart-yazi"]["y"] + b_dict["kart-yazi"]["h"] <= b_dict["kart"]["y"] + b_dict["kart"]["h"] + 1e-4, "kart-yazi kart icinde olmali (alt)"

    assert b_dict["alti"]["x"] >= b_dict["kart"]["x"] - 1e-4, "alti kart icinde olmali (sol)"
    assert b_dict["alti"]["x"] + b_dict["alti"]["w"] <= b_dict["kart"]["x"] + b_dict["kart"]["w"] + 1e-4, "alti kart icinde olmali (sag)"
    assert b_dict["alti"]["y"] >= b_dict["kart"]["y"] - 1e-4, "alti kart icinde olmali (ust)"
    assert b_dict["alti"]["y"] + b_dict["alti"]["h"] <= b_dict["kart"]["y"] + b_dict["kart"]["h"] + 1e-4, "alti kart icinde olmali (alt)"

    # Kesisim 0: hud, baslik, saat, soru, duman, tren, kart, fig, ok çiftleri (duman-tren hariç)
    ciftler: list[str] = ["hud", "baslik", "saat", "soru", "duman", "tren", "kart", "fig", "ok"]
    for i in range(len(ciftler)):
        for j in range(i + 1, len(ciftler)):
            n1, n2 = ciftler[i], ciftler[j]
            if {n1, n2} == {"duman", "tren"}:
                continue
            k: float = kesisim(b_dict[n1], b_dict[n2])
            assert k == 0.0, f"Kesisim {n1} - {n2}: {k}"

    # Boşluklar
    bosluk_hud_baslik: float = b_dict["baslik"]["y"] - (b_dict["hud"]["y"] + b_dict["hud"]["h"])
    assert bosluk_hud_baslik >= 40.0 - 1e-4, f"hud alt -> baslik ust bosluk {bosluk_hud_baslik} < 40"

    en_ust_sahne: float = min(b_dict[n]["y"] for n in ["saat", "soru", "duman", "tren", "kart", "fig", "ok"])
    bosluk_baslik_sahne: float = en_ust_sahne - (b_dict["baslik"]["y"] + b_dict["baslik"]["h"])
    assert bosluk_baslik_sahne >= 48.0 - 1e-4, f"baslik alt -> sahne ust bosluk {bosluk_baslik_sahne} < 48"

    assert b_dict["tren"]["y"] - (b_dict["saat"]["y"] + b_dict["saat"]["h"]) >= 16.0 - 1e-4, "saat alt -> tren ust < 16"
    assert b_dict["tren"]["y"] - (b_dict["soru"]["y"] + b_dict["soru"]["h"]) >= 16.0 - 1e-4, "soru alt -> tren ust < 16"
    assert b_dict["kart"]["y"] - (b_dict["tren"]["y"] + b_dict["tren"]["h"]) >= 20.0 - 1e-4, "tren alt -> kart ust < 20"
    assert b_dict["fig"]["x"] - (b_dict["kart"]["x"] + b_dict["kart"]["w"]) >= 60.0 - 1e-4, "kart sag -> fig sol < 60"
    assert b_dict["ok"]["x"] - (b_dict["tren"]["x"] + b_dict["tren"]["w"]) >= 8.0 - 1e-4, "ok sol - tren sag < 8"
    assert b_dict["fig"]["x"] - (b_dict["ok"]["x"] + b_dict["ok"]["w"]) >= 4.0 - 1e-4, "fig sol - ok sag < 4"
    assert b_dict["duman"]["x"] - (b_dict["soru"]["x"] + b_dict["soru"]["w"]) >= 24.0 - 1e-4, "soru sag -> duman sol < 24"
    assert b_dict["soru"]["x"] - (b_dict["saat"]["x"] + b_dict["saat"]["w"]) >= 24.0 - 1e-4, "saat sag -> soru sol < 24"

    # 2. Yazı boyu >= 64 (rozet 36 hariç)
    assert S >= 64, f"Baslik boyutu {S} < 64"
    assert KB >= 64, f"Kart metin boyutu {KB} < 64"

    # Satır uzunlukları <= 24 karakter
    satirlar: list[str] = ["YDT · BASIC", "NEDEN -ING", "YOK?", "The train leaves \u2026"]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # Başlık 2 satır, 3 sözcük
    baslik_satirlari: list[str] = ["NEDEN -ING", "YOK?"]
    assert len(baslik_satirlari) == 2, f"Başlık satır sayısı {len(baslik_satirlari)} != 2"
    baslik_sozcukleri: list[str] = " ".join(baslik_satirlari).split()
    assert len(baslik_sozcukleri) == 3, f"Başlık sözcük sayısı {len(baslik_sozcukleri)} != 3"
    assert "İ" not in " ".join(baslik_satirlari), "Başlıkta Türkçe İ harfi yasak"
    assert "\u0049" in "NEDEN -ING", "-ING içinde U+0049 I harfi olmalı"

    # 5. Yasaklar ve ek kontroller
    html_lower: str = html.lower()
    yasak_kelimeler: list[str] = [
        "kanal",
        "qr",
        "tarife",
        "timetable",
        "6 dk",
        "text-transform",
        "math.random",
        "date.now",
        "new date",
        "opacity:0",
        "<circle",
    ]
    for yk in yasak_kelimeler:
        assert yk not in html_lower, f"Yasak ifade bulundu: {yk}"

    assert 'id="t2"' not in html, "id t2 yasak"
    assert 'id="ku-nokta"' not in html, "id ku-nokta yasak"
    assert 'id="rz1"' not in html, "id rz1 yasak"

    # 6 haneli hex renk kontrolü
    hex_kumesi: set[str] = set(re.findall(r"#[0-9a-f]{6}\b", html_lower))
    izin_verilen_hex: set[str] = {"#1b1a17", "#f3efe6", "#c9c2b3", "#f2a93b"}
    assert hex_kumesi.issubset(izin_verilen_hex), f"İzinsiz hex renk(ler): {hex_kumesi - izin_verilen_hex}"

    # Emoji kontrolü
    for ch in html:
        assert ord(ch) < 0x1F000, f"Emoji karakteri yasak: {ch}"


def uret() -> tuple[str, int, float, list[dict[str, float]]]:
    """Sahne HTML'i, font boyutları ve nesnelerini üretir."""
    S, g1, g2, T1, T2, x1, x2, hap_x, hap_w, hap_y, hap_h = hesapla_s()

    # Saat sabitleri
    SC: tuple[float, float] = (TX0 + 87.5 * K_TREN, 924.0)
    SR: float = 56.0

    # Soru sabitleri
    SH: float = 112.0
    SY0: float = 872.0
    SCX: float = TX0 + 237.5 * K_TREN
    SX0: float = SCX - 0.31 * SH

    # Figür koordinatları
    x0, y0, x1_fig, y1_fig = FIG["kutu"]
    FIG_H: float = 476.0
    FIG_ALT: float = 1341.0
    FIG_SAG: float = 1016.0
    fs: float = FIG_H / (y1_fig - y0)
    FIG_SOL: float = FIG_SAG - (x1_fig - x0) * fs
    FIG_UST: float = FIG_ALT - FIG_H

    el: list[float] = FIG["el"]
    EL: tuple[float, float] = (FIG_SOL + (x1_fig - el[0]) * fs, FIG_UST + (el[1] - y0) * fs)

    # Kalem oku koordinatları
    TREN_SAG: float = TX0 + 420.0 * K_TREN
    S_ok: tuple[float, float] = (FIG_SOL - 12.0, EL[1] - 10.0)
    E_ok: tuple[float, float] = (TREN_SAG + 16.0, 1086.0)
    C_ok: tuple[float, float] = ((S_ok[0] + E_ok[0]) / 2.0, min(S_ok[1], E_ok[1]) - 50.0)

    vx: float = E_ok[0] - C_ok[0]
    vy: float = E_ok[1] - C_ok[1]
    v_len: float = math.hypot(vx, vy)
    ux: float = -vx / v_len
    uy: float = -vy / v_len
    rx1: float = ux * math.cos(0.5) - uy * math.sin(0.5)
    ry1: float = ux * math.sin(0.5) + uy * math.cos(0.5)
    rx2: float = ux * math.cos(-0.5) - uy * math.sin(-0.5)
    ry2: float = ux * math.sin(-0.5) + uy * math.cos(-0.5)
    uc1: tuple[float, float] = (E_ok[0] + 26.0 * rx1, E_ok[1] + 26.0 * ry1)
    uc2: tuple[float, float] = (E_ok[0] + 26.0 * rx2, E_ok[1] + 26.0 * ry2)

    ok_noktalar: list[tuple[float, float]] = []
    for i in range(40):
        t: float = i / 39.0
        bx: float = (1.0 - t) ** 2 * S_ok[0] + 2.0 * (1.0 - t) * t * C_ok[0] + t**2 * E_ok[0]
        by: float = (1.0 - t) ** 2 * S_ok[1] + 2.0 * (1.0 - t) * t * C_ok[1] + t**2 * E_ok[1]
        ok_noktalar.append((bx, by))
    ok_noktalar.extend([uc1, E_ok, uc2])
    min_x: float = min(pt[0] for pt in ok_noktalar)
    max_x: float = max(pt[0] for pt in ok_noktalar)
    min_y: float = min(pt[1] for pt in ok_noktalar)
    max_y: float = max(pt[1] for pt in ok_noktalar)

    ok_box: dict[str, float] = {
        "ad": "ok",
        "x": min_x - 3.0,
        "y": min_y - 3.0,
        "w": (max_x + 3.0) - (min_x - 3.0),
        "h": (max_y + 3.0) - (min_y - 3.0),
    }

    # Kart metin ve altçizgi
    KB: int = 72
    kart_metin: str = "The train leaves \u2026"
    metin_w: float = Y.genislik("Fredoka", 700, kart_metin, KB)
    KW: float = metin_w + 80.0
    LX: float = 106.0 + Y.genislik("Fredoka", 700, "The train ", KB)
    LW: float = Y.genislik("Fredoka", 700, "leaves", KB)

    # SVG elemanları
    kunye: str = kunye_svg()
    baslik: str = baslik_svg(S, T1, T2, x1, x2, hap_x, hap_y, hap_w, hap_h)
    eskiz: str = sahne_svg(
        FIG_SOL, FIG_UST, fs, x1_fig, y0, SC, SR, S_ok, E_ok, C_ok, uc1, uc2
    )
    soru: str = soru_svg(SX0, SY0, SH)
    kart: str = kart_svg(KW, kart_metin, LX, LW)

    bloklar: list[dict[str, float]] = blok_kutulari(
        S,
        g1,
        T1,
        T2,
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
        FIG_SOL,
        FIG_UST,
        fs,
        x0,
        x1_fig,
        FIG_H,
        ok_box,
    )

    html: str = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
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

    kurallari_dogrula(bloklar, S, KB, html)
    return html, S, KW, bloklar


if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, S, KW, bloklar = uret()
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
    print(f"S={S} KW={KW:.1f}")

#!/usr/bin/python3
"""Sahne 04 hikâye karesi index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> içerik (352-1344) -> çağrı (1344-1536) -> platform (1536-1920 boş)."""
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

W, H = Y.W, Y.H
KENAR = 48
SAG = W - KENAR
GEN = W - 2 * KENAR
ICERIK = (352, 1392)
CAGRI = (1344, 1536)
PLATFORM = 1536

UST_Y = 404
BAS_BANT = (444, 724)
KART_Y = (748, 996)
KART_H = 228
ALT_Y = 1296
IKON_X = (664, 1000)


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


def hesapla_s_ve_bas() -> tuple[
    int, int, int, float, float, float, float, float, float, float, float, float, float, float
]:
    """Başlık bloğu 'TARİFE' / '≠ PLAN' için S ve yerleşim değerlerini hesaplar."""
    w1 = Y.genislik("Fredoka", 700, "TARİFE", 100) / 100.0
    w_plan_100 = Y.genislik("Fredoka", 700, "PLAN", 100) / 100.0
    wh = 0.36 + 0.50 + 0.24 + w_plan_100 + 0.36
    S = min(190, int(math.floor((724.0 - 444.0) / 2.25)), int(math.floor(952.0 / max(w1, wh))))
    assert S >= 64, f"S={S} < 64"

    taban1 = int(round(444.0 + 0.95 * S))
    taban2 = int(taban1 + round(1.14 * S))

    w_tarife = Y.genislik("Fredoka", 700, "TARİFE", S)
    bas1_x = 540.0 - w_tarife / 2.0
    bas1_sag = bas1_x + w_tarife

    hw = wh * S
    hx = 540.0 - hw / 2.0
    hh = 1.02 * S
    hy = taban2 - 0.86 * S
    rx = hh / 2.0
    cx = hx + 0.36 * S + 0.25 * S

    bas_x = min(bas1_x, hx)
    bas_y = taban1 - 0.95 * S
    bas_sag = max(bas1_sag, hx + hw)
    bas_w = bas_sag - bas_x
    bas_h = (hy + hh) - bas_y

    return S, taban1, taban2, bas1_x, hx, hy, hw, hh, rx, cx, bas_x, bas_y, bas_w, bas_h


def kunye_svg() -> str:
    """Künye (HUD) grubu SVG çıktısı."""
    logo_w = 96.0 * Y.LOGO_EN_BOY
    logo = f'<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" width="{logo_w:.2f}" height="96"/></g>'
    ders1 = f'<text id="ku-ders1" x="48" y="212" font-family="Fredoka" font-weight="700" font-size="56" fill="{R["murekkep"]}" xml:space="preserve">SIMPLE PRESENT vs</text>'
    ders2 = f'<text id="ku-ders2" x="48" y="276" font-family="Fredoka" font-weight="700" font-size="56" fill="{R["murekkep"]}" xml:space="preserve">PRESENT CONTINUOUS</text>'

    ders2_w = Y.genislik("Fredoka", 700, "PRESENT CONTINUOUS", 56)
    rz_w = Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56.0
    rz_x = 48.0 + ders2_w + 24.0
    rozet = (
        f'<g id="rz0">'
        f'<rect x="{rz_x:.1f}" y="216" width="{rz_w:.1f}" height="72" rx="36" fill="{R["vurgu"]}"/>'
        f'<text x="{rz_x + rz_w / 2.0:.1f}" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" fill="{R["zemin"]}">YDT · BASIC</text>'
        f'</g>'
    )

    cip_metin = "Full lesson"
    cip_w = Y.genislik("Lexend", 700, cip_metin, 40) + 64.0
    cip_x = 1032.0 - cip_w
    cip = (
        f'<g id="ku-cip">'
        f'<rect id="ku-cipr" x="{cip_x:.1f}" y="48" width="{cip_w:.1f}" height="80" rx="40" fill="none" stroke="{R["vurgu"]}" stroke-width="4"/>'
        f'<text id="ku-cipt" x="{cip_x + cip_w / 2.0:.1f}" y="102" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="40" fill="{R["vurgu"]}">{cip_metin}</text>'
        f'</g>'
    )
    return f'<g id="kunye">{logo}{ders1}{ders2}{rozet}{cip}</g>'


def bas_svg(
    S: int,
    taban1: int,
    taban2: int,
    bas1_x: float,
    hx: float,
    hy: float,
    hw: float,
    hh: float,
    rx: float,
    cx: float,
) -> str:
    """Başlık bloğu 'TARİFE' / '≠ PLAN' SVG çıktısı."""
    bas1 = (
        f'<text id="bas1" x="{bas1_x:.1f}" y="{taban1}" '
        f'font-family="Fredoka" font-weight="700" font-size="{S}" '
        f'fill="{R["murekkep"]}" xml:space="preserve">TARİFE</text>'
    )
    hap_rect = (
        f'<rect id="bas2-hap" x="{hx:.1f}" y="{hy:.1f}" width="{hw:.1f}" height="{hh:.1f}" '
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
    plan_x = hx + (0.36 + 0.50 + 0.24) * S
    plan_text = (
        f'<text id="bas2-yazi" x="{plan_x:.1f}" y="{taban2}" '
        f'font-family="Fredoka" font-weight="700" font-size="{S}" '
        f'fill="{R["zemin"]}" xml:space="preserve">PLAN</text>'
    )
    bas2 = f'<g id="bas2">{hap_rect}{esitdegil}{plan_text}</g>'
    return f'<g id="bas">{bas1}{bas2}</g>'


def kart1_svg(y0: int = 748) -> str:
    """Kart 1 (tren + saat, 'The train leaves …', 'train -> timetable') SVG çıktısı."""
    yc = y0 + 114
    crv = f'<rect id="kart1-crv" x="48" y="{y0}" width="984" height="228" rx="28" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'

    # Tren ikonu: ikon_yollari(TREN, 774, yc, 220, 100)
    tren_yollar = ikon_yollari(TREN, 774.0, float(yc), 220.0, 100.0)
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
    tren_svg = f'<g id="kart1-tren">{"".join(tren_paths)}</g>'

    # Saat ikonu: merkez (954, yc), r 46
    cx, cy, r = 954.0, float(yc), 46.0
    d_kadran = _daire_yolu(cx, cy, r)
    p_kadran = f'<path d="{d_kadran}" stroke="{R["murekkep"]}" stroke-width="4"/>'

    centik_paths: list[str] = []
    for dx_c, dy_c in [(0.0, -1.0), (1.0, 0.0), (0.0, 1.0), (-1.0, 0.0)]:
        x_bas = cx + dx_c * 0.80 * r
        y_bas = cy + dy_c * 0.80 * r
        x_bit = cx + dx_c * 0.64 * r
        y_bit = cy + dy_c * 0.64 * r
        centik_paths.append(f'<path d="M{x_bas:.1f} {y_bas:.1f} L{x_bit:.1f} {y_bit:.1f}" stroke="{R["murekkep"]}" stroke-width="3"/>')

    p_yelkovan = f'<path d="M{cx:.1f} {cy:.1f} L{cx:.1f} {cy - 0.66 * r:.1f}" stroke="{R["murekkep"]}" stroke-width="4"/>'

    aci_rad = math.radians(210)
    x_akrep = cx + math.sin(aci_rad) * 0.50 * r
    y_akrep = cy - math.cos(aci_rad) * 0.50 * r
    p_akrep = f'<path d="M{cx:.1f} {cy:.1f} L{x_akrep:.1f} {y_akrep:.1f}" stroke="{R["murekkep"]}" stroke-width="6"/>'

    saat_svg = f'<g id="kart1-saat">{p_kadran}{"".join(centik_paths)}{p_yelkovan}{p_akrep}</g>'

    ikon = f'<g id="kart1-ikon" fill="none" stroke-linecap="round" stroke-linejoin="round">{tren_svg}{saat_svg}</g>'

    # Cümle: The train leaves … (… = U+2026)
    cumle_taban = y0 + 84
    cumle = f'<text id="kart1-cumle" x="80" y="{cumle_taban}" font-family="Fredoka" font-weight="700" font-size="64" fill="{R["murekkep"]}" xml:space="preserve">The train leaves \u2026</text>'

    # Odak altçizgisi: önek 'The train ' / odak 'leaves'
    onek_w = Y.genislik("Fredoka", 700, "The train ", 64)
    odak_w = Y.genislik("Fredoka", 700, "leaves", 64)
    x0_c = 80.0 + onek_w - 4.0
    x1_c = 80.0 + onek_w + odak_w + 4.0
    y_c = cumle_taban + 0.48 * 64.0
    orta_c = (x0_c + x1_c) / 2.0
    d_c = f"M{x0_c:.1f} {y_c:.1f} Q{orta_c:.1f} {y_c + 3.0:.1f} {x1_c:.1f} {y_c + 1.0:.1f}"
    odak = f'<path id="kart1-odak" d="{d_c}" fill="none" stroke="{R["vurgu"]}" stroke-width="8" stroke-linecap="round"/>'

    # Etiket: train -> timetable
    etk_taban = y0 + 180
    etk1 = f'<text id="kart1-etk1" x="80" y="{etk_taban}" font-family="Caveat" font-weight="700" font-size="64" fill="{R["murekkep"]}">train</text>'

    w_s1 = Y.genislik("Caveat", 700, "train", 64)
    xa0 = 80.0 + w_s1 + 18.0
    xa1 = xa0 + 64.0
    ya = etk_taban - 14.0
    dx_ok = 18.0 * math.cos(0.5)
    dy_ok = 18.0 * math.sin(0.5)
    d_ok = (
        f"M{xa0:.1f} {ya:.1f} Q{(xa0 + xa1) / 2.0:.1f} {ya - 3.0:.1f} {xa1:.1f} {ya:.1f} "
        f"M{xa1 - dx_ok:.1f} {ya - dy_ok:.1f} L{xa1:.1f} {ya:.1f} L{xa1 - dx_ok:.1f} {ya + dy_ok:.1f}"
    )
    ok = f'<path id="kart1-ok" d="{d_ok}" fill="none" stroke="{R["murekkep"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'

    x_s2 = xa1 + 18.0
    etk2 = f'<text id="kart1-etk2" x="{x_s2:.1f}" y="{etk_taban}" font-family="Caveat" font-weight="700" font-size="64" fill="{R["murekkep"]}">timetable</text>'

    return f'<g id="kart1">{crv}{ikon}{cumle}{odak}{etk1}{etk2}{ok}</g>'


def kart2_svg(y0: int = 996) -> str:
    """Kart 2 (bilet, 'I am going …', 'person -> plan') SVG çıktısı."""
    yc = y0 + 114
    crv = f'<rect id="kart2-crv" x="48" y="{y0}" width="984" height="228" rx="28" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'

    # Bilet ikonu: ikon_yollari(BILET, 832, yc, 300, 140), transform="rotate(-3 832 yc)"
    bilet_yollar = ikon_yollari(BILET, 832.0, float(yc), 300.0, 140.0)
    bilet_paths: list[str] = []
    for d, _, ince in bilet_yollar:
        if ince:
            renk = R["ikincil"]
            sw = 3
        else:
            renk = R["murekkep"]
            sw = 4
        bilet_paths.append(f'<path d="{d}" stroke="{renk}" stroke-width="{sw}"/>')
    ikon = (
        f'<g id="kart2-ikon" transform="rotate(-3 832 {yc:.1f})" '
        f'fill="none" stroke-linecap="round" stroke-linejoin="round">'
        f'{"".join(bilet_paths)}'
        f'</g>'
    )

    # Cümle: I am going … (… = U+2026)
    cumle_taban = y0 + 84
    cumle = f'<text id="kart2-cumle" x="80" y="{cumle_taban}" font-family="Fredoka" font-weight="700" font-size="64" fill="{R["murekkep"]}" xml:space="preserve">I am going \u2026</text>'

    # Odak altçizgisi: önek 'I ' / odak 'am going'
    onek_w = Y.genislik("Fredoka", 700, "I ", 64)
    odak_w = Y.genislik("Fredoka", 700, "am going", 64)
    x0_c = 80.0 + onek_w - 4.0
    x1_c = 80.0 + onek_w + odak_w + 4.0
    y_c = cumle_taban + 0.48 * 64.0
    orta_c = (x0_c + x1_c) / 2.0
    d_c = f"M{x0_c:.1f} {y_c:.1f} Q{orta_c:.1f} {y_c + 3.0:.1f} {x1_c:.1f} {y_c + 1.0:.1f}"
    odak = f'<path id="kart2-odak" d="{d_c}" fill="none" stroke="{R["vurgu"]}" stroke-width="8" stroke-linecap="round"/>'

    # Etiket: person -> plan
    etk_taban = y0 + 180
    etk1 = f'<text id="kart2-etk1" x="80" y="{etk_taban}" font-family="Caveat" font-weight="700" font-size="64" fill="{R["murekkep"]}">person</text>'

    w_s1 = Y.genislik("Caveat", 700, "person", 64)
    xa0 = 80.0 + w_s1 + 18.0
    xa1 = xa0 + 64.0
    ya = etk_taban - 14.0
    dx_ok = 18.0 * math.cos(0.5)
    dy_ok = 18.0 * math.sin(0.5)
    d_ok = (
        f"M{xa0:.1f} {ya:.1f} Q{(xa0 + xa1) / 2.0:.1f} {ya - 3.0:.1f} {xa1:.1f} {ya:.1f} "
        f"M{xa1 - dx_ok:.1f} {ya - dy_ok:.1f} L{xa1:.1f} {ya:.1f} L{xa1 - dx_ok:.1f} {ya + dy_ok:.1f}"
    )
    ok = f'<path id="kart2-ok" d="{d_ok}" fill="none" stroke="{R["murekkep"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'

    x_s2 = xa1 + 18.0
    etk2 = f'<text id="kart2-etk2" x="{x_s2:.1f}" y="{etk_taban}" font-family="Caveat" font-weight="700" font-size="64" fill="{R["murekkep"]}">plan</text>'

    return f'<g id="kart2">{crv}{ikon}{cumle}{odak}{etk1}{etk2}{ok}</g>'


def blok_kutulari(
    bas_x: float, bas_y: float, bas_w: float, bas_h: float
) -> list[dict[str, Any]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    hud = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}
    w_ust = Y.genislik("Lexend", 500, "İkisi geleceği anlatıyor", 64)
    ust = {"ad": "ust", "x": 48.0, "y": UST_Y - 0.75 * 64.0, "w": w_ust, "h": (0.75 + 0.25) * 64.0}
    bas = {"ad": "bas", "x": bas_x, "y": bas_y, "w": bas_w, "h": bas_h}
    kart1 = {"ad": "kart1", "x": 48.0, "y": 748.0, "w": 984.0, "h": 228.0}
    kart2 = {"ad": "kart2", "x": 48.0, "y": 996.0, "w": 984.0, "h": 228.0}
    w_alt = Y.genislik("Lexend", 500, "Tren tarifeye uyar", 64)
    alt = {"ad": "alt", "x": 48.0, "y": ALT_Y - 0.75 * 64.0, "w": w_alt, "h": (0.75 + 0.25) * 64.0}
    w_cg1 = Y.genislik("Caveat", 700, "Tam ders:", 72)
    cg1 = {"ad": "cg1", "x": 48.0, "y": 1418.0 - 0.75 * 72.0, "w": w_cg1, "h": (0.75 + 0.30) * 72.0}
    w_cg2 = Y.genislik("Caveat", 700, "profildeki bağlantı", 72)
    cg2 = {"ad": "cg2", "x": 48.0, "y": 1498.0 - 0.75 * 72.0, "w": w_cg2, "h": (0.75 + 0.30) * 72.0}
    w_hap = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap = {"ad": "hap", "x": 1032.0 - w_hap, "y": 1398.0, "w": w_hap, "h": 84.0}
    return [hud, ust, bas, kart1, kart2, alt, cg1, cg2, hap]


def kesisim(b1: dict[str, Any], b2: dict[str, Any]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, Any]], S: int) -> None:
    """SPEC.md §7 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Bütün blok kutuları x ∈ [48, 1032]; hiçbir öğe y >= 1536 değil
    for b in bloklar:
        assert b["x"] >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0, f"{b['ad']} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1536.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1536"

    # Yazı alt sınırları kontrolü (taban + 0.30*boy <= 1536)
    assert 1498.0 + 0.30 * 72.0 <= 1536.0, "cg2 yazı alt sınırı > 1536"

    # 2. Yazı boyu >= 64 (HUD hariç)
    assert S >= 64, f"bas boyutu {S} < 64"

    # 3. Her ekran satırı <= 24 karakter (len), HUD dahil
    satirlar = [
        "SIMPLE PRESENT vs",
        "PRESENT CONTINUOUS",
        "YDT · BASIC",
        "Full lesson",
        "İkisi geleceği anlatıyor",
        "TARİFE",
        "≠ PLAN",
        "The train leaves \u2026",
        "train \u2192 timetable",
        "I am going \u2026",
        "person \u2192 plan",
        "Tren tarifeye uyar",
        "Tam ders:",
        "profildeki bağlantı",
        "@ydspublishing",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 4. Blok kutuları çakışmaz (kesişim alanı 0)
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    # Dikey komşular arası boşluk >= 16
    dikey_sirali = ["hud", "ust", "bas", "kart1", "kart2", "alt"]
    for i in range(len(dikey_sirali) - 1):
        b1 = b_dict[dikey_sirali[i]]
        b2 = b_dict[dikey_sirali[i + 1]]
        bosluk = b2["y"] - (b1["y"] + b1["h"])
        assert bosluk >= 16.0 - 1e-4, f"Dikey boşluk {b1['ad']} -> {b2['ad']}: {bosluk} < 16"

    assert b_dict["cg1"]["y"] - (b_dict["alt"]["y"] + b_dict["alt"]["h"]) >= 16.0 - 1e-4
    assert b_dict["hap"]["y"] - (b_dict["alt"]["y"] + b_dict["alt"]["h"]) >= 16.0 - 1e-4

    # cg1 ve cg2 sağ kenarı ile hap sol kenarı arası >= 24
    assert b_dict["hap"]["x"] - (b_dict["cg1"]["x"] + b_dict["cg1"]["w"]) >= 24.0 - 1e-4
    assert b_dict["hap"]["x"] - (b_dict["cg2"]["x"] + b_dict["cg2"]["w"]) >= 24.0 - 1e-4

    # 5. İçerik ilk bloğu ust üstü >= 352; alt altı <= 1344; hap, cg1, cg2 [1344, 1536] içinde
    assert b_dict["ust"]["y"] >= 352.0 - 1e-4, f"ust üstü {b_dict['ust']['y']} < 352"
    assert b_dict["alt"]["y"] + b_dict["alt"]["h"] <= 1344.0 + 1e-4, f"alt altı {b_dict['alt']['y'] + b_dict['alt']['h']} > 1344"
    for ad in ("hap", "cg1", "cg2"):
        assert b_dict[ad]["y"] >= 1344.0 - 1e-4, f"{ad} üstü {b_dict[ad]['y']} < 1344"
        assert b_dict[ad]["y"] + b_dict[ad]["h"] <= 1536.0 + 1e-4, f"{ad} altı {b_dict[ad]['y'] + b_dict[ad]['h']} > 1536"

    # 6. Kart içi doğrulamaları
    for simge, y0, cumle_metin, etk1_metin, etk2_metin, onek_metin, odak_metin in [
        ("kart1", 748, "The train leaves \u2026", "train", "timetable", "The train ", "leaves"),
        ("kart2", 996, "I am going \u2026", "person", "plan", "I ", "am going"),
    ]:
        w_c = Y.genislik("Fredoka", 700, cumle_metin, 64)
        c_sag = 80.0 + w_c
        assert c_sag <= 640.0 + 1e-4, f"{simge} cümle sağ {c_sag} > 640"

        w_s1 = Y.genislik("Caveat", 700, etk1_metin, 64)
        xa0 = 80.0 + w_s1 + 18.0
        xa1 = xa0 + 64.0
        w_s2 = Y.genislik("Caveat", 700, etk2_metin, 64)
        etk_sag = xa1 + 18.0 + w_s2
        assert etk_sag <= 640.0 + 1e-4, f"{simge} etiket sağ {etk_sag} > 640"

        taban1_k = y0 + 84
        y_c = taban1_k + 0.48 * 64.0
        taban2_k = y0 + 180
        assert (y_c + 1.0 + 4.0) < (taban2_k - 0.75 * 64.0), f"{simge} altçizgi alt kenar >= etiket üstü"
        assert (taban2_k + 0.30 * 64.0) <= y0 + 212.0 + 1e-4, f"{simge} etiket alt kenar > y0 + 212"

    # Kart 1 ikonları sınır kontrolü: tren ve saat
    y0_1 = 748
    yc_1 = y0_1 + 114
    gx0_t, gy0_t, gx1_t, gy1_t = _kutusu(TREN)
    sc_t = min(100.0 / (gy1_t - gy0_t), 220.0 / (gx1_t - gx0_t))
    gw_t = (gx1_t - gx0_t) * sc_t
    gh_t = (gy1_t - gy0_t) * sc_t
    tren_x1 = 774.0 + gw_t / 2.0
    tren_y0 = yc_1 - gh_t / 2.0
    tren_y1 = yc_1 + gh_t / 2.0
    assert tren_x1 <= 1000.0 + 1e-4, f"tren x1 {tren_x1} > 1000"
    assert tren_y0 >= y0_1 + 16.0 - 1e-4, f"tren y0 {tren_y0} < {y0_1 + 16}"
    assert tren_y1 <= y0_1 + 212.0 + 1e-4, f"tren y1 {tren_y1} > {y0_1 + 212}"

    cx_s, cy_s, r_s = 954.0, float(yc_1), 46.0
    assert cx_s + r_s <= 1000.0 + 1e-4, f"saat x1 {cx_s + r_s} > 1000"
    assert cy_s - r_s >= y0_1 + 16.0 - 1e-4, f"saat y0 {cy_s - r_s} < {y0_1 + 16}"
    assert cy_s + r_s <= y0_1 + 212.0 + 1e-4, f"saat y1 {cy_s + r_s} > {y0_1 + 212}"

    # Kart 2 ikonu sınır kontrolü: bilet (rotasyonlu)
    y0_2 = 996
    yc_2 = y0_2 + 114
    gx0_b, gy0_b, gx1_b, gy1_b = _kutusu(BILET)
    sc_b = min(140.0 / (gy1_b - gy0_b), 300.0 / (gx1_b - gx0_b))
    th = math.radians(-3)
    xs_rot: list[float] = []
    ys_rot: list[float] = []
    for p in BILET:
        for q in p["n"]:
            px = 832.0 + (q[0] - (gx0_b + gx1_b) / 2.0) * sc_b
            py = yc_2 + (q[1] - (gy0_b + gy1_b) / 2.0) * sc_b
            rx = 832.0 + (px - 832.0) * math.cos(th) - (py - yc_2) * math.sin(th)
            ry = yc_2 + (px - 832.0) * math.sin(th) + (py - yc_2) * math.cos(th)
            xs_rot.append(rx)
            ys_rot.append(ry)
    assert max(xs_rot) <= 1000.0 + 1e-4, f"bilet x1 {max(xs_rot)} > 1000"
    assert min(ys_rot) >= y0_2 + 16.0 - 1e-4, f"bilet y0 {min(ys_rot)} < {y0_2 + 16}"
    assert max(ys_rot) <= y0_2 + 212.0 + 1e-4, f"bilet y1 {max(ys_rot)} > {y0_2 + 212}"


def uret() -> tuple[str, int, list[dict[str, Any]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    (
        S,
        taban1,
        taban2,
        bas1_x,
        hx,
        hy,
        hw,
        hh,
        rx,
        cx,
        bas_x,
        bas_y,
        bas_w,
        bas_h,
    ) = hesapla_s_ve_bas()
    bloklar = blok_kutulari(bas_x, bas_y, bas_w, bas_h)
    kurallari_dogrula(bloklar, S)

    kunye = kunye_svg()
    ust = f'<text id="ust" x="48" y="{UST_Y}" font-family="Lexend" font-weight="500" font-size="64" fill="{R["murekkep"]}">İkisi geleceği anlatıyor</text>'
    bas = bas_svg(S, taban1, taban2, bas1_x, hx, hy, hw, hh, rx, cx)
    kart1 = kart1_svg(748)
    kart2 = kart2_svg(996)
    alt = f'<text id="alt" x="48" y="{ALT_Y}" font-family="Lexend" font-weight="500" font-size="64" fill="{R["murekkep"]}">Tren tarifeye uyar</text>'
    cg1 = f'<text id="cg1" x="48" y="1418" font-family="Caveat" font-weight="700" font-size="72" fill="{R["murekkep"]}">Tam ders:</text>'
    cg2 = f'<text id="cg2" x="48" y="1498" font-family="Caveat" font-weight="700" font-size="72" fill="{R["murekkep"]}">profildeki bağlantı</text>'

    hap_w = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap_x = 1032.0 - hap_w
    hap = (
        f'<g id="hap">'
        f'<rect id="hap-kutu" x="{hap_x:.1f}" y="1398" width="{hap_w:.1f}" height="84" rx="42" fill="{R["vurgu"]}"/>'
        f'<text id="hap-yazi" x="{hap_x + hap_w / 2.0:.1f}" y="1462" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="64" fill="{R["zemin"]}">@ydspublishing</text>'
        f'</g>'
    )

    stil_esitdegil = '<style id="esitdegil-stil">#root #esitdegil path{stroke:var(--pilMetin)}</style>'

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{stil_esitdegil}
{kunye}
{ust}
{bas}
{kart1}
{kart2}
{alt}
{cg1}
{cg2}
{hap}
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

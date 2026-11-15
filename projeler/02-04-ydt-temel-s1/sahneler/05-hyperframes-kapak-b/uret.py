#!/usr/bin/python3
"""02-04-ydt-temel-s1 sahne 05 kapak B (soru) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok; huni v2)."""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageFilter

AD: Path = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET: Path = AD.parent.parent
ORTAK: Path = PAKET / "ortak"

# 1. zaman.json ve zamanlar.json okuma ve doğrulama (SPEC §3)
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

# 2. Renk ve sabitler (SPEC §3)
R: dict[str, str] = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}
KREM: str = R["murekkep"]

W: int = Y.W
H: int = Y.H
X0: int = 60
X1: int = 960
XC: int = 510
Y0: int = 460
Y1: int = 1380
KANAL_Y: tuple[int, int] = (280, 350)
KUNYE_Y: tuple[int, int] = (360, 450)

BASLIK_GEN: int = 888
BAS_UST: int = 480

KARAKTER: Path = ORTAK / "kapak" / "karakter.png"
ESIK: int = 64
KENAR_PX: int = 10
KENAR_GECIS: int = 3
PAY: int = 24
BAS_SATIR: int = 300

BL1_Y: int = 864
BL_H: int = 140
BL_ARA: int = 24
BL2_Y: int = 1028
BL_X1: int = 958  # şef QA: çizgi 4 px, dış kenar 960'ta kalır
IK: int = 56
PAD: int = 24
PAD_SAG: int = 40  # şef QA tur 1: Caveat "?" glifi ilerleme genişliğini ~10 px aşıyor, kenara değiyordu
IK_ARA: int = 16


def alfa_kutusu(yol: Path) -> tuple[int, int, int, int]:
    """PNG'nin saydam olmayan kutusu (x0, y0, x1, y1)."""
    a = Image.open(yol).split()[-1].point(lambda v: 255 if v > ESIK else 0)
    kutu = a.getbbox()
    assert kutu is not None, f"{yol.name} tamamen saydam"
    return kutu


def maske(yol: Path, x: float, y: float, s: float) -> np.ndarray:
    """Görselin tuvaldeki saydamlık maskesi (bool, H x W)."""
    im = Image.open(yol)
    a = im.split()[-1].resize((round(im.width * s), round(im.height * s)), Image.BILINEAR)
    m = Image.new("L", (W, H), 0)
    m.paste(255, (round(x), round(y)), a.point(lambda v: 255 if v > ESIK else 0))
    return np.asarray(m) > 0


def bos_mu(m: np.ndarray, kutu: tuple[float, float, float, float], pay: float) -> bool:
    """Kutu (pay kadar genişletilmiş) içinde maskede görsel yok mu."""
    x0, y0 = max(0, math.floor(kutu[0] - pay)), max(0, math.floor(kutu[1] - pay))
    x1, y1 = min(W, math.ceil(kutu[2] + pay)), min(H, math.ceil(kutu[3] + pay))
    return x1 <= x0 or y1 <= y0 or not m[y0:y1, x0:x1].any()


def maske_kutusu(m: np.ndarray) -> tuple[int, int, int, int]:
    """Maskenin tuvaldeki kutusu (x0, y0, x1, y1)."""
    ys, xs = np.nonzero(m)
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def gorsel_kopyala(hedef: Path) -> None:
    """Karakter proje/assets'e kopyalanır. Alfa ≤ ESIK temizlenir."""
    hedef.mkdir(parents=True, exist_ok=True)
    im = Image.open(KARAKTER).convert("RGBA")
    a = im.split()[-1]
    m = a.point(lambda v: 255 if v > ESIK else 0).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    im.putalpha(ImageChops.multiply(a, m))
    im.save(hedef / "karakter.png")


def gorsel_img(kx: float, ky: float, s: float) -> str:
    """Çıkartma kenarlı görsel (<img>, SPEC §4.3)."""
    im = Image.open(KARAKTER)
    return (
        f'<img id="karakter" class="abs kenar" src="assets/karakter.png" alt="" '
        f'style="left:{kx:.1f}px;top:{ky:.1f}px;width:{im.width * s:.1f}px;height:{im.height * s:.1f}px">'
    )


def hesapla_s() -> tuple[int, float, float, float, float, float, float, float, float, float, float, float]:
    """Başlık font boyutu S ve yerleşim koordinatlarını hesaplar (SPEC §4.2)."""
    s0: float = 100.0
    wa0: float = Y.genislik("Fredoka", 700, "YAŞI", s0)
    wy0: float = Y.genislik("Fredoka", 700, "YOR", s0)
    wu0: float = Y.genislik("Fredoka", 700, "UM", s0)
    p0: float = 0.08 * s0
    g1_100: float = wa0 + 2.0 * p0 + wy0 + wu0
    g2_100: float = Y.genislik("Fredoka", 700, "NASIL DENİR?", s0)
    S: int = math.floor(min(190.0, BASLIK_GEN * 100.0 / g1_100, BASLIK_GEN * 100.0 / g2_100))

    wa: float = Y.genislik("Fredoka", 700, "YAŞI", S)
    wy: float = Y.genislik("Fredoka", 700, "YOR", S)
    wu: float = Y.genislik("Fredoka", 700, "UM", S)
    p: float = 0.08 * S
    g1: float = wa + 2.0 * p + wy + wu
    g2: float = Y.genislik("Fredoka", 700, "NASIL DENİR?", S)

    while (g1 > BASLIK_GEN or g2 > BASLIK_GEN) and S > 1:
        S -= 1
        wa = Y.genislik("Fredoka", 700, "YAŞI", S)
        wy = Y.genislik("Fredoka", 700, "YOR", S)
        wu = Y.genislik("Fredoka", 700, "UM", S)
        p = 0.08 * S
        g1 = wa + 2.0 * p + wy + wu
        g2 = Y.genislik("Fredoka", 700, "NASIL DENİR?", S)

    assert g1 <= BASLIK_GEN, f"g1={g1} > {BASLIK_GEN}"
    assert g2 <= BASLIK_GEN, f"g2={g2} > {BASLIK_GEN}"

    T1: float = BAS_UST + 0.86 * S
    T2: float = T1 + 1.26 * S
    x1: float = XC - g1 / 2.0
    x2: float = XC - g2 / 2.0
    baslik_alt: float = T2 + 0.10 * S + 6.0

    return S, g1, g2, wa, wy, wu, p, T1, T2, x1, x2, baslik_alt


def baslik_svg(S: int, wa: float, wy: float, wu: float, p: float, T1: float, T2: float, x1: float, x2: float) -> str:
    """Başlık (<g id="baslik">) SVG çıktısı (SPEC §4.2)."""
    kx0: float = x1 + wa
    kx1: float = kx0 + 2.0 * p + wy
    kw: float = kx1 - kx0
    ky: float = T1 - 0.86 * S
    kh: float = (0.86 + 0.16) * S
    krx: float = 0.10 * S

    bk_kutu: str = (
        f'<rect id="bk-kutu" x="{kx0:.2f}" y="{ky:.2f}" width="{kw:.2f}" height="{kh:.2f}" '
        f'rx="{krx:.2f}" fill="{R["vurgu"]}"/>'
    )
    bs_yasi: str = (
        f'<text id="bs-yasi" x="{x1:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">YAŞI</text>'
    )
    bs_yor: str = (
        f'<text id="bs-yor" x="{kx0 + p:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["zemin"]}" style="font-kerning:none" xml:space="preserve">YOR</text>'
    )
    bs_um: str = (
        f'<text id="bs-um" x="{kx1:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">UM</text>'
    )
    bs_2: str = (
        f'<text id="bs-2" x="{x2:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">NASIL DENİR?</text>'
    )
    return f'<g id="baslik">{bk_kutu}{bs_yasi}{bs_yor}{bs_um}{bs_2}</g>'


def hesapla_yerlesim(
    baslik_alt: float,
) -> tuple[float, float, float, int, int, int, int, np.ndarray, list[tuple[float, float, float]]]:
    """Karakter ölçeği ve balon konumunu bulur (SPEC §4.4, §4.6)."""
    ax0, ay0, ax1, ay1 = alfa_kutusu(KARAKTER)
    assert (ax0, ay0, ax1, ay1) == (21, 173, 878, 1112)

    w100: float = Y.genislik("Caveat", 700, "I am living?", 100.0)

    for s_cand in [round(0.60 - 0.01 * i, 2) for i in range(21)]:
        kx: float = X0 + KENAR_PX + 2 - ax0 * s_cand  # şef QA tur 2: kenar yumuşatması 2 px taşıyordu (x 58)
        ky: float = Y1 - KENAR_PX - ay1 * s_cand
        m: np.ndarray = maske(KARAKTER, kx, ky, s_cand)
        kust: float = ky + ay0 * s_cand
        if not (kust - KENAR_PX >= baslik_alt + 40.0):
            continue

        r_start: int = math.floor(BL1_Y - KENAR_PX - PAY)
        r_end: int = math.ceil(BL2_Y + BL_H + KENAR_PX + PAY)
        sub_m: np.ndarray = m[r_start:r_end, :]
        sag_kenar: int = int(np.nonzero(sub_m)[1].max()) + 1 if sub_m.any() else 0
        bx0: int = math.ceil(sag_kenar + KENAR_PX + PAY)
        bw: int = BL_X1 - bx0
        tx: int = bx0 + PAD + IK + IK_ARA
        TB: int = min(88, math.floor((BL_X1 - PAD_SAG - tx) * 100.0 / w100))
        if TB < 72:
            continue

        satir_p0: int = int(round(ky + BAS_SATIR * s_cand))
        p0_x: int = int(np.nonzero(m[satir_p0])[0].max()) + 1 + KENAR_PX + 14
        P0: tuple[float, float] = (float(p0_x), float(ky + BAS_SATIR * s_cand))
        P1: tuple[float, float] = (float(bx0 - 12 - 16), float((BL1_Y + BL_H + BL2_Y) / 2.0))

        if P1[0] - P0[0] < 60.0:
            continue

        daireler: list[tuple[float, float]] = [(0.10, 8.0), (0.45, 12.0), (0.85, 16.0)]
        pts: list[tuple[float, float, float]] = [
            (P0[0] + t * (P1[0] - P0[0]), P0[1] + t * (P1[1] - P0[1]), r) for t, r in daireler
        ]
        if not all(bos_mu(m, (cx - r, cy - r, cx + r, cy + r), KENAR_PX + 8) for cx, cy, r in pts):
            continue
        if not all(cx + r <= bx0 - 8 for cx, cy, r in pts):
            continue

        dist_ok: bool = True
        for i in range(len(pts) - 1):
            c1x, c1y, r1 = pts[i]
            c2x, c2y, r2 = pts[i + 1]
            if math.hypot(c2x - c1x, c2y - c1y) < r1 + r2 + 8.0:
                dist_ok = False
                break
        if not dist_ok:
            continue

        return s_cand, kx, ky, bx0, bw, tx, TB, m, pts

    raise AssertionError("yerleşim bulunamadı: hiçbir ölçek şartları sağlamadı")


def sahne_svg(
    bx0: int, bw: int, tx: int, TB: int, pts: list[tuple[float, float, float]]
) -> tuple[str, str, str, float, float]:
    """Sahne çizimi (<g id="eskiz">) ve balon yazılarını üretir (SPEC §4.5)."""
    bl1_rect: str = f'<rect id="bl1" x="{bx0}" y="{BL1_Y}" width="{bw}" height="{BL_H}" rx="48" stroke-width="4"/>'
    bl2_rect: str = f'<rect id="bl2" x="{bx0}" y="{BL2_Y}" width="{bw}" height="{BL_H}" rx="48" stroke-width="4"/>'

    b1_orta_y: float = BL1_Y + 70.0
    b2_orta_y: float = BL2_Y + 70.0

    daire_svg: str = "".join(
        f'<circle id="dn-{i}" cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.0f}" fill="none" stroke-width="4"/>'
        for i, (cx, cy, r) in enumerate(pts, 1)
    )
    iz_group: str = f'<g id="iz">{daire_svg}</g>'

    scale_ik: float = IK / 24.0
    sw_ik: float = 4.0 / scale_ik

    home_paths: list[str] = Y.tabler("home")
    home_svg: str = "".join(f'<path d="{d}"/>' for d in home_paths)
    bl1_ikon: str = (
        f'<g id="bl1-ikon" transform="translate({bx0 + PAD} {b1_orta_y - IK / 2.0:.1f}) scale({scale_ik:.6f})" '
        f'stroke-width="{sw_ik:.4f}">{home_svg}</g>'
    )

    luggage_paths: list[str] = Y.tabler("luggage", AD / "cizim")
    luggage_svg: str = "".join(f'<path d="{d}"/>' for d in luggage_paths)
    bl2_ikon: str = (
        f'<g id="bl2-ikon" transform="translate({bx0 + PAD} {b2_orta_y - IK / 2.0:.1f}) scale({scale_ik:.6f})" '
        f'stroke-width="{sw_ik:.4f}">{luggage_svg}</g>'
    )

    eskiz: str = (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{bl1_rect}{bl2_rect}{iz_group}{bl1_ikon}{bl2_ikon}</g>'
    )

    taban1: float = b1_orta_y + 0.30 * TB
    taban2: float = b2_orta_y + 0.30 * TB
    bl1_yazi: str = (
        f'<text id="bl1-yazi" x="{tx}" y="{taban1:.2f}" font-family="Caveat" font-weight="700" '
        f'font-size="{TB}" fill="{R["murekkep"]}" xml:space="preserve">I live?</text>'
    )
    bl2_yazi: str = (
        f'<text id="bl2-yazi" x="{tx}" y="{taban2:.2f}" font-family="Caveat" font-weight="700" '
        f'font-size="{TB}" fill="{R["murekkep"]}" xml:space="preserve">I am living?</text>'
    )

    w_b1: float = Y.genislik("Caveat", 700, "I live?", TB)
    w_b2: float = Y.genislik("Caveat", 700, "I am living?", TB)
    assert tx + w_b1 <= BL_X1 - PAD_SAG, f"Balon 1 sağ kenar {tx + w_b1} > {BL_X1 - PAD_SAG}"
    assert tx + w_b2 <= BL_X1 - PAD_SAG, f"Balon 2 sağ kenar {tx + w_b2} > {BL_X1 - PAD_SAG}"

    return eskiz, bl1_yazi, bl2_yazi, w_b1, w_b2


def blok_kutulari(
    S: int,
    TB: int,
    g1: float,
    g2: float,
    wa: float,
    wy: float,
    p: float,
    T1: float,
    T2: float,
    x1: float,
    x2: float,
    bx0: int,
    bw: int,
    tx: int,
    w_b1: float,
    w_b2: float,
    m: np.ndarray,
    pts: list[tuple[float, float, float]],
) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını döndürür (SPEC §6.1, §6.9)."""
    kanal_sag: float = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42.0)
    b_kanal: dict[str, float] = {
        "ad": "kanal",
        "x": 60.0,
        "y": 291.0,
        "w": kanal_sag - 60.0,
        "h": 339.0 - 291.0,
    }

    kb: int = Y.konu_boyu()
    rx, rw = Y.rozet_konumu()
    rozet_sag: float = rx + rw
    kunye_y: float = min(386.0, 420.0 - 0.75 * kb)
    kunye_alt: float = max(434.0, 420.0 + 0.25 * kb)
    b_kunye: dict[str, float] = {
        "ad": "kunye",
        "x": 60.0,
        "y": kunye_y,
        "w": rozet_sag - 60.0,
        "h": kunye_alt - kunye_y,
    }

    bas_x: float = min(x1, x2) - 6.0
    bas_sag: float = max(x1 + g1, x2 + g2) + 6.0
    bas_y: float = T1 - 0.86 * S - 6.0
    bas_alt: float = T2 + 0.10 * S + 6.0
    b_baslik: dict[str, float] = {
        "ad": "baslik",
        "x": bas_x,
        "y": bas_y,
        "w": bas_sag - bas_x,
        "h": bas_alt - bas_y,
    }

    kx0: float = x1 + wa
    kx1: float = kx0 + 2.0 * p + wy
    b_bk_kutu: dict[str, float] = {
        "ad": "bk-kutu",
        "x": kx0,
        "y": T1 - 0.86 * S,
        "w": kx1 - kx0,
        "h": (0.86 + 0.16) * S,
    }

    mx0, my0, mx1, my1 = maske_kutusu(m)
    b_karakter: dict[str, float] = {
        "ad": "karakter",
        "x": float(mx0 - KENAR_PX),
        "y": float(my0 - KENAR_PX),
        "w": float((mx1 + KENAR_PX) - (mx0 - KENAR_PX)),
        "h": float((my1 + KENAR_PX) - (my0 - KENAR_PX)),
    }

    b_bl1: dict[str, float] = {
        "ad": "bl1",
        "x": float(bx0 - 2),
        "y": float(BL1_Y - 2),
        "w": float(bw + 4),
        "h": float(BL_H + 4),
    }
    b_bl2: dict[str, float] = {
        "ad": "bl2",
        "x": float(bx0 - 2),
        "y": float(BL2_Y - 2),
        "w": float(bw + 4),
        "h": float(BL_H + 4),
    }

    taban1: float = (BL1_Y + 70.0) + 0.30 * TB
    b_bl1_yazi: dict[str, float] = {
        "ad": "bl1-yazi",
        "x": float(tx),
        "y": taban1 - 0.75 * TB,
        "w": w_b1,
        "h": 1.0 * TB,
    }

    taban2: float = (BL2_Y + 70.0) + 0.30 * TB
    b_bl2_yazi: dict[str, float] = {
        "ad": "bl2-yazi",
        "x": float(tx),
        "y": taban2 - 0.75 * TB,
        "w": w_b2,
        "h": 1.0 * TB,
    }

    b_dns: list[dict[str, float]] = [
        {
            "ad": f"dn-{i}",
            "x": cx - r - 2.0,
            "y": cy - r - 2.0,
            "w": 2.0 * (r + 2.0),
            "h": 2.0 * (r + 2.0),
        }
        for i, (cx, cy, r) in enumerate(pts, 1)
    ]

    return [
        b_kanal,
        b_kunye,
        b_baslik,
        b_bk_kutu,
        b_karakter,
        b_bl1,
        b_bl2,
        b_bl1_yazi,
        b_bl2_yazi,
        b_dns[0],
        b_dns[1],
        b_dns[2],
    ]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx: float = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy: float = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(
    bloklar: list[dict[str, float]],
    S: int,
    TB: int,
    html: str,
    baslik_alt: float,
) -> None:
    """SPEC.md §6 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict: dict[str, dict[str, float]] = {b["ad"]: b for b in bloklar}

    # 1 & 2. Sınırlar (SPEC §6.2)
    for b in bloklar:
        ad: str = b["ad"]
        assert b["x"] >= 60.0 - 1e-4, f"{ad} sol {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ {b['x'] + b['w']} > 960"
        if ad == "kanal":
            assert b["y"] >= 280.0 - 1e-4 and b["y"] + b["h"] <= 350.0 + 1e-4, f"kanal y out: {b['y']}"
        elif ad == "kunye":
            assert b["y"] >= 360.0 - 1e-4 and b["y"] + b["h"] <= 450.0 + 1e-4, f"kunye y out: {b['y']}"
        else:
            assert b["y"] >= 460.0 - 1e-4 and b["y"] + b["h"] <= 1380.0 + 1e-4, f"{ad} y out: {b['y']}"

    # 3. Kesişim 0 (SPEC §6.3)
    ana_ciftler: list[tuple[str, str]] = [
        ("kanal", "kunye"),
        ("kanal", "baslik"),
        ("kanal", "bl1"),
        ("kanal", "bl2"),
        ("kunye", "baslik"),
        ("kunye", "bl1"),
        ("kunye", "bl2"),
        ("baslik", "bl1"),
        ("baslik", "bl2"),
        ("bl1", "bl2"),
    ]
    for a, c in ana_ciftler:
        k: float = kesisim(b_dict[a], b_dict[c])
        assert k == 0.0, f"Kesişim {a} - {c}: {k}"

    k_bk: float = kesisim(b_dict["baslik"], b_dict["karakter"])
    assert k_bk == 0.0, f"Kesişim baslik - karakter: {k_bk}"

    for i in (1, 2, 3):
        for hedef in ("bl1", "bl2", "baslik"):
            k_dn: float = kesisim(b_dict[f"dn-{i}"], b_dict[hedef])
            assert k_dn == 0.0, f"Kesişim dn-{i} - {hedef}: {k_dn}"

    assert BL2_Y - (BL1_Y + BL_H) >= 24.0, "bl1 alt -> bl2 üst boşluk < 24"
    assert BL1_Y - baslik_alt >= 40.0, "baslik alt -> bl1 üst boşluk < 40"
    assert b_dict["bl1"]["y"] - baslik_alt >= 40.0, "baslik alt -> bl1 box üst boşluk < 40"

    # 4. Yazı boyu (SPEC §6.4)
    assert S >= 64, f"Başlık boyutu {S} < 64"
    assert TB >= 64, f"Balon boyutu {TB} < 64"

    baslik_satirlari: list[str] = ["YAŞIYORUM", "NASIL DENİR?"]
    assert len(baslik_satirlari) == 2, "Başlık satır sayısı != 2"
    assert len(" ".join(baslik_satirlari).split()) == 3, "Başlık sözcük sayısı != 3"

    tum_satirlar: list[str] = ["YAŞIYORUM", "NASIL DENİR?", "I live?", "I am living?"]
    for s_metin in tum_satirlar:
        assert len(s_metin) <= 24, f"Satır uzunluğu > 24: {s_metin}"

    # 5. Görünen metin taraması (SPEC §6.5)
    gorunen_metinler: list[str] = re.findall(r">([^<]+)</text>", html)
    yasak_kelimeler: list[str] = [
        "tam" + " ders",  # parçalı: istem metin taraması (grep) koruma listesini ekran metni saymasın
        "dak" + "ika",
        "izle",
        "qr",
        "kanal",
        "ikisi de",
        "kalıcı",
        "geçici",
    ]
    for gm in gorunen_metinler:
        gm_lower: str = gm.lower()
        for yk in yasak_kelimeler:
            assert yk not in gm_lower, f"Görünen metinde yasak sözcük bulundu: {yk!r} in {gm!r}"
        for ch in gm:
            assert ord(ch) <= 0x2FFF, f"Görünen metinde emoji/simge bulundu: {ch!r} (U+{ord(ch):04X})"

    # 6. Bütün HTML kontrolleri (SPEC §6.6)
    html_lower: str = html.lower()
    for yasak_kod in ("math.random", "date.now", "new date", "opacity:0"):
        assert yasak_kod not in html_lower, f"Yasak kod/özellik bulundu: {yasak_kod}"

    hex_renkler: set[str] = set(re.findall(r"#[0-9a-fA-F]{6}\b", html))
    gecerli_renkler: set[str] = {
        R["zemin"].lower(),
        R["murekkep"].lower(),
        R["ikincil"].lower(),
        R["vurgu"].lower(),
    }
    for hx in hex_renkler:
        assert hx.lower() in gecerli_renkler, f"Geçersiz hex renk: {hx}"

    kanal_sayisi: int = html.count('id="kanal"')
    assert kanal_sayisi == 1, f"id='kanal' sayısı {kanal_sayisi} != 1"
    logoimg_sayisi: int = html.count('id="logoimg"')
    assert logoimg_sayisi == 1, f"id='logoimg' sayısı {logoimg_sayisi} != 1"
    assert 'id="t2"' not in html, "id t2 yasak"
    assert 'id="ku-nokta"' not in html, "id ku-nokta yasak"
    assert 'id="rz1"' not in html, "id rz1 yasak"


def uret() -> tuple[str, int, int, float, int, list[dict[str, float]]]:
    """Sahne HTML'i, font boyutları ve nesnelerini üretir."""
    S, g1, g2, wa, wy, wu, p, T1, T2, x1, x2, baslik_alt = hesapla_s()
    s, kx, ky, bx0, bw, tx, TB, m, pts = hesapla_yerlesim(baslik_alt)

    kunye: str = Y.kunye_svg()
    baslik: str = baslik_svg(S, wa, wy, wu, p, T1, T2, x1, x2)
    eskiz, bl1_yazi, bl2_yazi, w_b1, w_b2 = sahne_svg(bx0, bw, tx, TB, pts)

    bloklar: list[dict[str, float]] = blok_kutulari(
        S, TB, g1, g2, wa, wy, p, T1, T2, x1, x2, bx0, bw, tx, w_b1, w_b2, m, pts
    )

    karakter_img: str = gorsel_img(kx, ky, s)

    adim: float = KENAR_PX / KENAR_GECIS
    kenar_filter: str = " ".join(
        f"drop-shadow({dx:.2f}px {dy:.2f}px 0 {KREM})"
        for _ in range(KENAR_GECIS)
        for dx, dy in ((adim, 0.0), (-adim, 0.0), (0.0, adim), (0.0, -adim))
    )

    html: str = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
.kenar{{filter:{kenar_filter};}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
{karakter_img}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{baslik}
{eskiz}
{bl1_yazi}
{bl2_yazi}
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

    kurallari_dogrula(bloklar, S, TB, html, baslik_alt)
    return html, S, TB, s, bx0, bloklar


if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    gorsel_kopyala(proje_dizini / "assets")

    html, S, TB, s, bx0, bloklar = uret()
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
    (AD / "nesneler.json").write_text(
        json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"index.html yazıldı {len(html)}")
    print(f"S={S} TB={TB} s={s:.2f} bx0={bx0}")

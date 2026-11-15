#!/usr/bin/python3
"""Sahne 06 kapak C (karşıt çift) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> başlık (358-786) -> kartlar ve figür (884-1344) -> alt platform (1344-1920 boş).
"""
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

# zaman.json ve zamanlar.json okuma ve doğrulama (SPEC §3)
zaman_data = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlar = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlar) == 1, "duragan içinde " + AD.name + " tek kayıt olmalı"
duragan_kayit = duragan_kayitlar[0]
kare_val = duragan_kayit["kare"]
cikti_val = duragan_kayit["cikti"]
assert kare_val == 1, f"kare {kare_val} != 1"
assert cikti_val == "kapak-c.png", f"cikti {cikti_val} != kapak-c.png"
assert AD.name not in [s["klasor"] for s in zaman_data["sahneler"]], f"{AD.name} sahneler[] içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

W, H = Y.W, Y.H
KENAR = 48
SAG = 1032
BASLIK_GEN = 952
BANT_UST = 864
BANT_ALT = 1344


def g(m: str, b: float) -> float:
    """Fredoka 700 metin genişliği px (kerning yok)."""
    return Y.genislik("Fredoka", 700, m, b)


def hesapla_s_ve_baslik() -> tuple[int, float, float, float, float, float, float, float, float, float, float]:
    """Başlık S boyutu ve yerleşim ölçülerini hesaplar (SPEC §4.2)."""
    s0 = 100.0
    p0 = 0.08 * s0
    w100 = g("İKİ ZAMAN", s0) + 2.0 * p0
    S = int(math.floor(min(190, 952.0 * 100.0 / w100)))

    p = 0.08 * S
    B = max(g("İKİ ÖRNEK", S), g("İKİ ZAMAN", S) + 2.0 * p)
    while B > 952.0 and S > 1:
        S -= 1
        p = 0.08 * S
        B = max(g("İKİ ÖRNEK", S), g("İKİ ZAMAN", S) + 2.0 * p)
    assert B <= 952.0, f"B={B} > 952"

    KX = 540.0 - B / 2.0
    x0 = KX + p
    kutu_w = g("İKİ ZAMAN", S) + 2.0 * p

    T1 = 358.0 + 0.93 * S  # İ noktası 358, kontur (12/2) 352 = içerik bandı üstü (BRIEF-DIKEY §2)
    KU = T1 + 0.12 * S
    T2 = KU + 1.00 * S
    KA = T2 + 0.20 * S
    kutu_h = KA - KU
    kutu_rx = 0.10 * S

    return S, B, KX, x0, T1, KU, T2, KA, kutu_w, kutu_h, kutu_rx


def kunye_svg() -> str:
    """Künye (HUD) grubu SVG çıktısı (SPEC §4.1)."""
    logo_w = 96.0 * Y.LOGO_EN_BOY
    logo = f'<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" width="{logo_w:.2f}" height="96"/></g>'
    rz_w = Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56.0
    rozet = (
        f'<g id="rz0">'
        f'<rect x="48" y="216" width="{rz_w:.2f}" height="72" rx="36" fill="{R["vurgu"]}"/>'
        f'<text x="{48.0 + rz_w / 2.0:.2f}" y="265" text-anchor="middle" '
        f'font-family="Lexend" font-weight="700" font-size="36" fill="{R["zemin"]}">YDT · BASIC</text>'
        f'</g>'
    )
    return f'<g id="kunye">{logo}{rozet}</g>'


def baslik_svg(
    S: int,
    x0: float,
    T1: float,
    T2: float,
    KX: float,
    KU: float,
    kutu_w: float,
    kutu_h: float,
    kutu_rx: float,
) -> str:
    """Başlık grubu SVG çıktısı (SPEC §4.2)."""
    bs_1 = (
        f'<text id="bs-1" x="{x0:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">İKİ ÖRNEK</text>'
    )
    bk_kutu = (
        f'<rect id="bk-kutu" x="{KX:.2f}" y="{KU:.2f}" width="{kutu_w:.2f}" '
        f'height="{kutu_h:.2f}" rx="{kutu_rx:.2f}" fill="{R["vurgu"]}"/>'
    )
    bs_2 = (
        f'<text id="bs-2" x="{x0:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["zemin"]}" style="font-kerning:none">İKİ ZAMAN</text>'
    )
    return f'<g id="baslik">{bs_1}{bk_kutu}{bs_2}</g>'


def _kutu(x: float, y: float, w: float, h: float, ince: bool = False) -> dict[str, Any]:
    """İkon parçası dikdörtgen yolu."""
    return {"n": [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], "kapali": True, "ince": ince}


TREN: list[dict[str, Any]] = [
    _kutu(200.0, 55.0, 170.0, 75.0),
    _kutu(200.0, 10.0, 75.0, 45.0),
    _kutu(320.0, 22.0, 26.0, 33.0, True),
    {"n": [(370.0, 95.0), (398.0, 130.0), (370.0, 130.0)]},
    _kutu(215.0, 20.0, 42.0, 25.0, True),
    {"daire": (240.0, 138.0, 17.0)},
    {"daire": (335.0, 138.0, 17.0)},
    {"n": [(190.0, 158.0), (410.0, 158.0)], "ince": True},
    {"daire": (345.0, 2.0, 10.0), "ince": True},
    {"daire": (372.0, -16.0, 7.5), "ince": True},
]


def _bilet() -> list[dict[str, Any]]:
    """Sinema bileti ikon parçaları."""
    def yay(x0: float, yon: float) -> list[tuple[float, float]]:
        return [
            (
                x0 - yon * 22.0 * math.cos(-math.pi / 2.0 + i / 12.0 * math.pi),
                yon * 22.0 * math.sin(-math.pi / 2.0 + i / 12.0 * math.pi),
            )
            for i in range(13)
        ]

    kenar = [(-180.0, -70.0), (180.0, -70.0), (180.0, -22.0)] + yay(180.0, 1.0) + [(180.0, 70.0), (-180.0, 70.0), (-180.0, 22.0)] + yay(-180.0, -1.0)
    p: list[dict[str, Any]] = [{"n": kenar + [(-180.0, -70.0)]}]
    p += [{"n": [(100.0, -58.0 + i * 20.0), (100.0, -47.0 + i * 20.0)], "ince": True} for i in range(6)]
    p += [{"n": [(-150.0, y), (x1, y)], "ince": True} for y, x1 in ((-30.0, 60.0), (0.0, 30.0), (30.0, 70.0))]
    return p


BILET: list[dict[str, Any]] = _bilet()


def _kutusu(parcalar: list[dict[str, Any]]) -> tuple[float, float, float, float]:
    """İkon parçalarının ızgara dış kutusunu hesaplar."""
    xs: list[float] = []
    ys: list[float] = []
    for p in parcalar:
        if "daire" in p:
            x, y, r = p["daire"]
            xs += [x - r, x + r]
            ys += [y - r, y + r]
        else:
            xs += [q[0] for q in p["n"]]
            ys += [q[1] for q in p["n"]]
    return min(xs), min(ys), max(xs), max(ys)


def _daire_yolu(cx: float, cy: float, r: float) -> str:
    """Çember Bezier yolu (4 kübik yay)."""
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
    parcalar: list[dict[str, Any]], mx0: float, my0: float, en: float, boy: float
) -> list[tuple[str, float, bool]]:
    """Izgara parçalarını en x boy kutusuna (merkez mx0, my0) sığdırır. Döner: [(d, uzunluk, ince)]."""
    gx0, gy0, gx1, gy1 = _kutusu(parcalar)
    sc = min(boy / (gy1 - gy0), en / (gx1 - gx0))
    gmx, gmy = (gx0 + gx1) / 2.0, (gy0 + gy1) / 2.0

    def P(q: tuple[float, float]) -> tuple[float, float]:
        return (mx0 + (q[0] - gmx) * sc, my0 + (q[1] - gmy) * sc)

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
        if p.get("egri") and len(q) >= 3:  # Catmull-Rom -> kübik
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


def ikon_kutusu(
    parcalar: list[dict[str, Any]], mx0: float, my0: float, en: float, boy: float, ad: str
) -> dict[str, Any]:
    """İkonun çizilen yollarının ekran dış kutusunu hesaplar."""
    gx0, gy0, gx1, gy1 = _kutusu(parcalar)
    gw = gx1 - gx0
    gh = gy1 - gy0
    sc = min(boy / gh, en / gw)
    w = gw * sc
    h = gh * sc
    x = mx0 - w / 2.0
    y = my0 - h / 2.0
    return {"ad": ad, "x": x, "y": y, "w": w, "h": h}


def ikon_svg(
    parcalar: list[dict[str, Any]], mx0: float, my0: float, en: float, boy: float, grup_id: str
) -> str:
    """İkon SVG çıktısı."""
    yollar = ikon_yollari(parcalar, mx0, my0, en, boy)
    icerik = "".join(
        f'<path d="{d}" stroke="{R["ikincil"] if ince else R["murekkep"]}" stroke-width="{3 if ince else 4}"/>'
        for d, _, ince in yollar
    )
    return f'<g id="{grup_id}" fill="none" stroke-linecap="round" stroke-linejoin="round">{icerik}</g>'


def el_kutu(x: float, y: float, w: float, h: float) -> str:
    """Dört kenarı hafif eğri el kutusu (tek yol)."""
    return (
        "M%.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f "
        "Q%.0f %.0f %.0f %.0f"
        % (
            x + 4,
            y + 3,
            x + w / 2,
            y - 3,
            x + w - 3,
            y + 1,
            x + w + 3,
            y + h / 2,
            x + w - 1,
            y + h - 2,
            x + w / 2,
            y + h + 4,
            x + 5,
            y + h + 1,
            x - 3,
            y + h / 2,
            x + 2,
            y + 6,
            x + 1,
            y + 2,
            x + 5,
            y + 2,
        )
    )


def kartlar_svg(
    metin_x: float,
    XL: float,
    xc: float,
    hap_x: float,
    hap_y: float,
    hap_w: float,
    hap_h: float,
    ik_tren_svg: str,
    ik_bilet_svg: str,
) -> str:
    """Kartlar grubu SVG çıktısı (SPEC §4.3)."""
    kc1 = (
        f'<path id="kc1" d="{el_kutu(64.0, 884.0, 816.0, 200.0)}" fill="none" '
        f'stroke="{R["murekkep"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    m1a = (
        f'<text id="m1a" x="{metin_x:.2f}" y="1010" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" style="font-kerning:none">The train</text>'
    )
    hap_leaves = (
        f'<rect id="hap-leaves" x="{hap_x:.2f}" y="{hap_y:.2f}" width="{hap_w:.2f}" '
        f'height="{hap_h:.2f}" rx="12" fill="{R["vurgu"]}"/>'
    )
    m1b = (
        f'<text id="m1b" x="{XL:.2f}" y="1010" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["zemin"]}" style="font-kerning:none">leaves</text>'
    )
    m1c = (
        f'<text id="m1c" x="{xc:.2f}" y="1010" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" style="font-kerning:none">…</text>'
    )
    kart1 = f'<g id="kart1">{kc1}{ik_tren_svg}{m1a}{hap_leaves}{m1b}{m1c}</g>'

    kc2 = (
        f'<path id="kc2" d="{el_kutu(64.0, 1124.0, 816.0, 200.0)}" fill="none" '
        f'stroke="{R["murekkep"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    m2 = (
        f'<text id="m2" x="{metin_x:.2f}" y="1250" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" style="font-kerning:none">I am going …</text>'
    )
    kart2 = f'<g id="kart2">{kc2}{ik_bilet_svg}{m2}</g>'

    return f'<g id="kartlar">{kart1}{kart2}</g>'


def eskiz_svg() -> tuple[str, float, float]:
    """Sahne figür ve zemin çizgisi SVG çıktısı (SPEC §4.4)."""
    FIG = json.loads((AD / "cizim" / "ogretmen.json").read_text(encoding="utf-8"))
    x0_f, y0_f, x1_f, y1_f = FIG["kutu"]
    FIG_H = 340.0
    FIG_ALT = 1324.0
    fs = FIG_H / (y1_f - y0_f)
    fw = (x1_f - x0_f) * fs
    FIG_X = 1016.0 - fw
    tx_fig = FIG_X - x0_f * fs
    ty_fig = (FIG_ALT - FIG_H) - y0_f * fs

    zc = f'<path id="zc" d="M{FIG_X - 16.0:.2f} 1324 L1016 1324" stroke-width="4"/>'

    fig_kalinlik: dict[str, float] = {"govde": 4.4, "sac": 3.6, "yuz": 2.6}
    fig_svg = "".join(
        f'<path id="f{i}" d="{p["d"]}" stroke-width="{fig_kalinlik.get(p.get("parca", ""), 4.4) / fs:.3f}"/>'
        for i, p in enumerate(FIG["yollar"])
    )
    fig_group = f'<g id="fig" transform="translate({tx_fig:.2f} {ty_fig:.2f}) scale({fs:.6f})">{fig_svg}</g>'

    eskiz = (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{zc}{fig_group}</g>'
    )
    return eskiz, fw, FIG_X


def blok_kutulari(
    S: int,
    B: float,
    KX: float,
    T1: float,
    KU: float,
    KA: float,
    kutu_w: float,
    kutu_h: float,
    fw: float,
    FIG_X: float,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Yerleşim bloklarının kutularını hesaplar.
    Döndürür: (kesisim_bloklari, nesneler_bloklari).
    kesisim_bloklari (5 adet): hud, baslik, kart-1, kart-2, fig.
    nesneler_bloklari (11 adet): hud, baslik, bk-kutu, kart-1, ik-tren, m-1, hap-leaves, kart-2, ik-bilet, m-2, fig.
    """
    hud = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}

    baslik_y_ust = T1 - 0.93 * S
    baslik = {
        "ad": "baslik",
        "x": KX,
        "y": baslik_y_ust,
        "w": B,
        "h": KA - baslik_y_ust,
    }

    bk_kutu = {
        "ad": "bk-kutu",
        "x": KX,
        "y": KU,
        "w": kutu_w,
        "h": kutu_h,
    }

    kart_1 = {
        "ad": "kart-1",
        "x": 64.0 - 4.0,
        "y": 884.0 - 4.0,
        "w": 816.0 + 8.0,
        "h": 200.0 + 8.0,
    }

    w_m1 = g("The train leaves …", 72.0)
    metin_x = 880.0 - 28.0 - w_m1
    ikon_en = (metin_x - 24.0) - 88.0
    ikon_boy = 112.0
    mx0_ik = 88.0 + ikon_en / 2.0

    ik_tren = ikon_kutusu(TREN, mx0_ik, 984.0, ikon_en, ikon_boy, "ik-tren")

    m_1 = {
        "ad": "m-1",
        "x": metin_x,
        "y": 1010.0 - 0.75 * 72.0,
        "w": w_m1,
        "h": 72.0,
    }

    XL = metin_x + g("The train ", 72.0)
    hap_leaves = {
        "ad": "hap-leaves",
        "x": XL - 0.12 * 72.0,
        "y": 1010.0 - 0.86 * 72.0,
        "w": g("leaves", 72.0) + 2.0 * 0.12 * 72.0,
        "h": (0.86 + 0.18) * 72.0,
    }

    kart_2 = {
        "ad": "kart-2",
        "x": 64.0 - 4.0,
        "y": 1124.0 - 4.0,
        "w": 816.0 + 8.0,
        "h": 200.0 + 8.0,
    }

    ik_bilet = ikon_kutusu(BILET, mx0_ik, 1224.0, ikon_en, ikon_boy, "ik-bilet")

    w_m2 = g("I am going …", 72.0)
    m_2 = {
        "ad": "m-2",
        "x": metin_x,
        "y": 1250.0 - 0.75 * 72.0,
        "w": w_m2,
        "h": 72.0,
    }

    fig = {
        "ad": "fig",
        "x": FIG_X,
        "y": 1324.0 - 340.0,
        "w": fw,
        "h": 340.0,
    }

    kesisim_bloklari = [hud, baslik, kart_1, kart_2, fig]
    nesneler_bloklari = [
        hud,
        baslik,
        bk_kutu,
        kart_1,
        ik_tren,
        m_1,
        hap_leaves,
        kart_2,
        ik_bilet,
        m_2,
        fig,
    ]
    return kesisim_bloklari, nesneler_bloklari


def kesisim(b1: dict[str, Any], b2: dict[str, Any]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(
    kesisim_bloklari: list[dict[str, Any]],
    nesneler_bloklari: list[dict[str, Any]],
    S: int,
    T2: float,
    html: str,
) -> None:
    """SPEC §6 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in nesneler_bloklari}

    # 1 & 2. Sınırlar: Bütün bloklar x ∈ [48, 1032]; hud dışı x ∈ [60, 1016]; alt kenar <= 1344
    for b in nesneler_bloklari:
        assert b["x"] >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0, f"{b['ad']} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1344.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1344"
        if b["ad"] != "hud":
            assert b["x"] >= 60.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 60"
            assert b["x"] + b["w"] <= 1016.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1016"

    # 3. Yazı boyu >= 64, satır uzunluğu <= 24
    assert S >= 64, f"Başlık boyutu S={S} < 64"
    satirlar = [
        "İKİ ÖRNEK",
        "İKİ ZAMAN",
        "The train leaves …",
        "I am going …",
        "YDT · BASIC",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 4. Kesişim 0: hud, baslik, kart-1, kart-2, fig
    for i in range(len(kesisim_bloklari)):
        for j in range(i + 1, len(kesisim_bloklari)):
            k = kesisim(kesisim_bloklari[i], kesisim_bloklari[j])
            ad1, ad2 = kesisim_bloklari[i]["ad"], kesisim_bloklari[j]["ad"]
            assert k == 0.0, f"Kesişim {ad1} - {ad2}: {k}"

    hud_alt = b_dict["hud"]["y"] + b_dict["hud"]["h"]
    baslik_ust = b_dict["baslik"]["y"]
    assert baslik_ust - hud_alt >= 40.0, f"hud alt -> başlık üst ara {baslik_ust - hud_alt} < 40"
    assert baslik_ust - 6.0 >= 352.0 - 1e-4, f"başlık üstü (kontur dahil) {baslik_ust - 6.0} < 352"

    baslik_alt = b_dict["baslik"]["y"] + b_dict["baslik"]["h"]
    assert 884.0 - baslik_alt >= 48.0, f"başlık alt -> kart 1 üst ara {884.0 - baslik_alt} < 48"

    assert 1124.0 - (884.0 + 200.0) >= 24.0, "kart 1 alt -> kart 2 üst ara < 24"
    assert b_dict["fig"]["x"] - 880.0 >= 24.0, f"kart sağı -> fig ara {b_dict['fig']['x'] - 880.0} < 24"

    # 5. Kart içi yerleşim
    ik_tren = b_dict["ik-tren"]
    m_1 = b_dict["m-1"]
    assert ik_tren["x"] >= 64.0 + 16.0, "ik-tren sol pay < 16"
    assert ik_tren["y"] >= 884.0 + 16.0, "ik-tren üst pay < 16"
    assert ik_tren["y"] + ik_tren["h"] <= 1084.0 - 16.0, "ik-tren alt pay < 16"
    assert m_1["x"] >= 64.0 + 16.0, "m-1 sol pay < 16"
    assert m_1["x"] + m_1["w"] <= 880.0 - 16.0, "m-1 sağ pay < 16"
    assert m_1["y"] >= 884.0 + 16.0, "m-1 üst pay < 16"
    assert m_1["y"] + m_1["h"] <= 1084.0 - 16.0, "m-1 alt pay < 16"

    ik_bilet = b_dict["ik-bilet"]
    m_2 = b_dict["m-2"]
    assert ik_bilet["x"] >= 64.0 + 16.0, "ik-bilet sol pay < 16"
    assert ik_bilet["y"] >= 1124.0 + 16.0, "ik-bilet üst pay < 16"
    assert ik_bilet["y"] + ik_bilet["h"] <= 1324.0 - 16.0, "ik-bilet alt pay < 16"
    assert m_2["x"] >= 64.0 + 16.0, "m-2 sol pay < 16"
    assert m_2["x"] + m_2["w"] <= 880.0 - 16.0, "m-2 sağ pay < 16"
    assert m_2["y"] >= 1124.0 + 16.0, "m-2 üst pay < 16"
    assert m_2["y"] + m_2["h"] <= 1324.0 - 16.0, "m-2 alt pay < 16"

    w_m1 = g("The train leaves …", 72.0)
    metin_x = 880.0 - 28.0 - w_m1
    assert metin_x - (ik_tren["x"] + ik_tren["w"]) >= 20.0, "tren sağı -> metin ara < 20"
    assert metin_x - (ik_bilet["x"] + ik_bilet["w"]) >= 20.0, "bilet sağı -> metin ara < 20"
    assert m_1["x"] + m_1["w"] <= 880.0 - 24.0, "m-1 sağ kenar > 880 - 24"

    XL = metin_x + g("The train ", 72.0)
    hap_leaves = b_dict["hap-leaves"]
    assert hap_leaves["x"] >= metin_x + g("The train", 72.0) + 4.0, "hap-leaves train kelimesine değiyor"
    assert hap_leaves["x"] + hap_leaves["w"] <= XL + g("leaves ", 72.0) - 4.0, "hap-leaves üç noktaya değiyor"

    # 6. Kart 1 ile kart 2 aynı ölçüde; başlık kutusu İ noktasını içerir
    kart_1 = b_dict["kart-1"]
    kart_2 = b_dict["kart-2"]
    assert kart_1["x"] == kart_2["x"], "kart-1 ve kart-2 x eşit olmalı"
    assert kart_1["w"] == kart_2["w"], "kart-1 ve kart-2 w eşit olmalı"
    assert kart_1["h"] == kart_2["h"], "kart-1 ve kart-2 h eşit olmalı"
    assert b_dict["bk-kutu"]["y"] <= T2 - 0.93 * S, "bk-kutu İ noktasını kapsamalı"

    # 7. HTML kontrolleri
    hex_kodlar = set(re.findall(r"#[0-9a-fA-F]{6}", html))
    izin_verilen = {R["zemin"], R["murekkep"], R["ikincil"], R["vurgu"]}
    assert hex_kodlar <= izin_verilen, f"Geçersiz renk: {hex_kodlar - izin_verilen}"
    for yasak_kelime in ("kanal", "QR", " dk"):
        assert yasak_kelime not in html, f"Yasak metin: {yasak_kelime}"

    # 8. Yasak API kontrolleri
    for yasak_api in ("Math.random", "Date", "try", "catch", "opacity:0", "opacity: 0"):
        assert yasak_api not in html, f"Yasak API / stil: {yasak_api}"


def uret() -> tuple[str, int, list[dict[str, Any]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    S, B, KX, x0, T1, KU, T2, KA, kutu_w, kutu_h, kutu_rx = hesapla_s_ve_baslik()
    kunye = kunye_svg()
    baslik = baslik_svg(S, x0, T1, T2, KX, KU, kutu_w, kutu_h, kutu_rx)

    w_m1 = g("The train leaves …", 72.0)
    metin_x = 880.0 - 28.0 - w_m1
    ikon_en = (metin_x - 24.0) - 88.0
    ikon_boy = 112.0
    mx0_ik = 88.0 + ikon_en / 2.0

    XL = metin_x + g("The train ", 72.0)
    hap_x = XL - 0.12 * 72.0
    hap_y = 1010.0 - 0.86 * 72.0
    hap_w = g("leaves", 72.0) + 2.0 * 0.12 * 72.0
    hap_h = (0.86 + 0.18) * 72.0
    xc = XL + g("leaves ", 72.0)

    ik_tren_svg = ikon_svg(TREN, mx0_ik, 984.0, ikon_en, ikon_boy, "ik-tren")
    ik_bilet_svg = ikon_svg(BILET, mx0_ik, 1224.0, ikon_en, ikon_boy, "ik-bilet")

    kartlar = kartlar_svg(
        metin_x, XL, xc, hap_x, hap_y, hap_w, hap_h, ik_tren_svg, ik_bilet_svg
    )

    eskiz, fw, FIG_X = eskiz_svg()

    kesisim_bloklari, nesneler_bloklari = blok_kutulari(
        S, B, KX, T1, KU, KA, kutu_w, kutu_h, fw, FIG_X
    )

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
{kunye}
{baslik}
{kartlar}
{eskiz}
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

    kurallari_dogrula(kesisim_bloklari, nesneler_bloklari, S, T2, html)

    return html, S, nesneler_bloklari


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

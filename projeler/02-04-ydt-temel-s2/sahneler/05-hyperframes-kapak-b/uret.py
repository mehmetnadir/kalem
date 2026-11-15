#!/usr/bin/python3
"""02-04-ydt-temel-s2 sahne 05 kapak B (soru) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).

Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> başlık -> sahne (757-1344) -> platform (1536-1920 boş).
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

AD: Path = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET: Path = AD.parent.parent

# 1. zaman.json ve zamanlar.json okuma ve doğrulama (§3)
zaman_data: dict = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlari: list[dict] = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlari) == 1, f"duragan içinde {AD.name} kaydı tek olmalı"
duragan: dict = duragan_kayitlari[0]
assert duragan["kare"] == 1, f"kare {duragan['kare']} != 1"
assert duragan["cikti"] == "kapak-b.png", f"cikti {duragan['cikti']} != kapak-b.png"
assert AD.name not in [s["klasor"] for s in zaman_data.get("sahneler", [])], "AD.name sahneler içinde olmamalı"

Z: dict = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
sure_sn: float = float(Z["sure"])
assert sure_sn == 1.0, f"sure {sure_sn} != 1.0"
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
ZEMIN_Y: int = 1344
PLATFORM: int = 1536

FIG: dict = json.loads((AD / "cizim" / "ogretmen-dusunen.json").read_text(encoding="utf-8"))


def hesapla_s() -> tuple[int, float, float, float, float, float, float]:
    """Başlık font boyutu S ve yerleşim koordinatlarını hesaplar (§4.2)."""
    s0: float = 100.0
    g1_100: float = Y.genislik("Fredoka", 700, "TODAY VARSA", s0)
    g2_100: float = Y.genislik("Fredoka", 700, "HANGİ ZAMAN?", s0)
    S: int = math.floor(min(190.0, BASLIK_GEN * 100.0 / g1_100, BASLIK_GEN * 100.0 / g2_100))

    g1: float = Y.genislik("Fredoka", 700, "TODAY VARSA", S)
    g2: float = Y.genislik("Fredoka", 700, "HANGİ ZAMAN?", S)

    while (g1 > BASLIK_GEN or g2 > BASLIK_GEN) and S > 1:
        S -= 1
        g1 = Y.genislik("Fredoka", 700, "TODAY VARSA", S)
        g2 = Y.genislik("Fredoka", 700, "HANGİ ZAMAN?", S)

    assert g1 <= BASLIK_GEN, f"g1={g1} > {BASLIK_GEN}"
    assert g2 <= BASLIK_GEN, f"g2={g2} > {BASLIK_GEN}"

    T1: float = 528.0 - 0.25 * S
    T2: float = T1 + 1.26 * S
    x1: float = 540.0 - g1 / 2.0
    x2: float = 540.0 - g2 / 2.0

    return S, g1, g2, T1, T2, x1, x2


def kunye_svg() -> str:
    """HUD (<g id="kunye">) SVG çıktısı (§4.1)."""
    logo_w: float = 96.0 * Y.LOGO_EN_BOY
    logo: str = f'<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" width="{logo_w:.2f}" height="96"/></g>'
    rz_w: float = Y.genislik("Lexend", 700, "YDT · BASIC", 36.0) + 56.0
    rz_x: float = 48.0
    rz_ortax: float = rz_x + rz_w / 2.0
    vurgu_c: str = R["vurgu"]
    zemin_c: str = R["zemin"]
    rozet: str = (
        f'<g id="rz0">'
        f'<rect x="{rz_x:.1f}" y="216" width="{rz_w:.1f}" height="72" rx="36" fill="{vurgu_c}"/>'
        f'<text x="{rz_ortax:.1f}" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" fill="{zemin_c}">YDT · BASIC</text>'
        f'</g>'
    )
    return f'<g id="kunye">{logo}{rozet}</g>'


def baslik_svg(S: int, T1: float, T2: float, x1: float, x2: float) -> str:
    """Başlık (<g id="baslik">) SVG çıktısı (§4.2)."""
    mur_c: str = R["murekkep"]
    zem_c: str = R["zemin"]
    bs_1: str = (
        f'<text id="bs-1" x="{x1:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{mur_c}" stroke="{zem_c}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">TODAY VARSA</text>'
    )
    bs_2: str = (
        f'<text id="bs-2" x="{x2:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{mur_c}" stroke="{zem_c}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">HANGİ ZAMAN?</text>'
    )
    return f'<g id="baslik">{bs_1}{bs_2}</g>'


def sahne_svg() -> tuple[
    str, str, str, str, str, int, float,
    dict[str, float], dict[str, float], dict[str, float], dict[str, float], dict[str, float], dict[str, float], dict[str, float]
]:
    """Sahne çizimi öğelerini (zc, takvim, tk-yazi, fig, soru) ve blok kutularını üretir (§4.3)."""
    mur_c: str = R["murekkep"]
    zem_c: str = R["zemin"]
    vur_c: str = R["vurgu"]

    # 1. Zemin çizgisi
    zc_svg: str = f'<path id="zc" d="M64 1344 L1016 1344" fill="none" stroke="{mur_c}" stroke-width="4" stroke-linecap="round"/>'

    # 2. Figür
    FIG_H: float = 480.0
    FIG_X: float = 64.0
    FIG_UST: float = ZEMIN_Y - FIG_H
    x0: float = FIG["kutu"][0]
    y0: float = FIG["kutu"][1]
    x1_k: float = FIG["kutu"][2]
    y1_k: float = FIG["kutu"][3]
    fs: float = FIG_H / (y1_k - y0)
    tx: float = FIG_X - x0 * fs
    ty: float = FIG_UST - y0 * fs

    def px(x: float, y: float) -> tuple[float, float]:
        return (FIG_X + (x - x0) * fs, FIG_UST + (y - y0) * fs)

    Gx, Gy = px(FIG["el"][0], FIG["el"][1])

    el_kutu: list[float] = FIG["el_kutu"]
    el_px_x: float = FIG_X + (el_kutu[0] - x0) * fs
    el_px_y: float = FIG_UST + (el_kutu[1] - y0) * fs
    el_px_w: float = (el_kutu[2] - el_kutu[0]) * fs
    el_px_h: float = (el_kutu[3] - el_kutu[1]) * fs
    el_px_sag: float = el_px_x + el_px_w

    bas: list[float] = FIG["bas"]
    bas_px_x: float = FIG_X + (bas[0] - x0) * fs
    bas_px_y: float = FIG_UST + (bas[1] - y0) * fs
    bas_px_w: float = (bas[2] - bas[0]) * fs
    bas_px_h: float = (bas[3] - bas[1]) * fs

    fig_paths: list[str] = []
    for p in FIG["yollar"]:
        d_val: str = p["d"]
        if p["dolgu"] == "beyaz":
            fig_paths.append(f'<path class="dz" fill="{zem_c}" d="{d_val}"/>')
        elif p["dolgu"] == "murekkep":
            fig_paths.append(f'<path fill="{mur_c}" fill-rule="evenodd" d="{d_val}"/>')
        else:
            raise ValueError(f"Bilinmeyen dolgu: {p['dolgu']}")

    fig_svg: str = f'<g id="fig" transform="translate({tx:.2f} {ty:.2f}) scale({fs:.6f})">' + "".join(fig_paths) + "</g>"

    # 3. Takvim yaprağı
    k: float = 300.0 / 16.0
    Cx: float = Gx - 14.0
    Cy: float = Gy + 16.0
    Ox: float = Cx - 4.0 * k
    Oy: float = Cy - 21.0 * k
    Hy: float = Oy + 11.0 * k

    cal_paths: list[str] = Y.tabler("calendar")
    assert len(cal_paths) >= 4, f"cal_paths uzunluğu {len(cal_paths)} < 4"
    assert cal_paths[0].startswith("M4 7a2"), f"cal_paths[0] beklenmeyen: {cal_paths[0][:20]}"
    assert cal_paths[1].startswith("M16 3v4"), f"cal_paths[1] beklenmeyen: {cal_paths[1][:20]}"
    assert cal_paths[2].startswith("M8 3v4"), f"cal_paths[2] beklenmeyen: {cal_paths[2][:20]}"
    assert cal_paths[3].startswith("M4 11h16"), f"cal_paths[3] beklenmeyen: {cal_paths[3][:20]}"

    takvim_paths_svg: str = "".join(f'<path d="{d}"/>' for d in cal_paths[:4])
    takvim_svg: str = (
        f'<g id="takvim" transform="rotate(4 {Gx:.2f} {Gy:.2f}) translate({Ox:.2f} {Oy:.2f}) scale({k:.4f})" '
        f'fill="none" stroke="{mur_c}" stroke-width="{6.0 / k:.4f}" '
        f'stroke-linecap="round" stroke-linejoin="round">{takvim_paths_svg}</g>'
    )

    noktalar: list[tuple[float, float]] = [
        (Ox + 4.0 * k, Oy + 5.0 * k),
        (Ox + 20.0 * k, Oy + 5.0 * k),
        (Ox + 20.0 * k, Oy + 21.0 * k),
        (Ox + 4.0 * k, Oy + 21.0 * k),
        (Ox + 8.0 * k, Oy + 3.0 * k),
        (Ox + 16.0 * k, Oy + 3.0 * k),
    ]
    rad: float = math.radians(4.0)
    cos_a: float = math.cos(rad)
    sin_a: float = math.sin(rad)
    rot_takvim: list[tuple[float, float]] = []
    for p_x, p_y in noktalar:
        dx: float = p_x - Gx
        dy: float = p_y - Gy
        rx: float = Gx + dx * cos_a - dy * sin_a
        ry: float = Gy + dx * sin_a + dy * cos_a
        rot_takvim.append((rx, ry))

    takvim_min_x: float = min(p[0] for p in rot_takvim) - 3.0
    takvim_max_x: float = max(p[0] for p in rot_takvim) + 3.0
    takvim_min_y: float = min(p[1] for p in rot_takvim) - 3.0
    takvim_max_y: float = max(p[1] for p in rot_takvim) + 3.0
    takvim_blok: dict[str, float] = {
        "ad": "takvim",
        "x": takvim_min_x,
        "y": takvim_min_y,
        "w": takvim_max_x - takvim_min_x,
        "h": takvim_max_y - takvim_min_y,
    }

    # 4. Takvim yazısı
    XL: float = el_px_sag + 16.0
    XR: float = Cx + 300.0 - 24.0
    w_today_100: float = Y.genislik("Caveat", 700, "today", 100.0)
    TT: int = min(100, math.floor((XR - XL) * 100.0 / w_today_100))
    assert TT >= 72, f"TT={TT} < 72"

    x_tk: float = (XL + XR) / 2.0
    taban_tk: float = (Hy + Cy) / 2.0 + 0.30 * TT
    tk_yazi_svg: str = (
        f'<g id="tk-yazi-g" transform="rotate(4 {Gx:.2f} {Gy:.2f})">'
        f'<text id="tk-yazi" x="{x_tk:.2f}" y="{taban_tk:.2f}" text-anchor="middle" '
        f'font-family="Caveat" font-weight="700" font-size="{TT}" fill="{mur_c}">today</text></g>'
    )

    w_today: float = Y.genislik("Caveat", 700, "today", TT)
    tk_yazi_kose: list[tuple[float, float]] = [
        (x_tk - w_today / 2.0, taban_tk - 0.75 * TT),
        (x_tk + w_today / 2.0, taban_tk - 0.75 * TT),
        (x_tk + w_today / 2.0, taban_tk + 0.30 * TT),
        (x_tk - w_today / 2.0, taban_tk + 0.30 * TT),
    ]
    rot_tk_yazi: list[tuple[float, float]] = []
    for p_x, p_y in tk_yazi_kose:
        dx_y: float = p_x - Gx
        dy_y: float = p_y - Gy
        rx_y: float = Gx + dx_y * cos_a - dy_y * sin_a
        ry_y: float = Gy + dx_y * sin_a + dy_y * cos_a
        rot_tk_yazi.append((rx_y, ry_y))

    tk_yazi_min_x: float = min(p[0] for p in rot_tk_yazi)
    tk_yazi_max_x: float = max(p[0] for p in rot_tk_yazi)
    tk_yazi_min_y: float = min(p[1] for p in rot_tk_yazi)
    tk_yazi_max_y: float = max(p[1] for p in rot_tk_yazi)
    takvim_yazi_blok: dict[str, float] = {
        "ad": "takvim-yazi",
        "x": tk_yazi_min_x,
        "y": tk_yazi_min_y,
        "w": tk_yazi_max_x - tk_yazi_min_x,
        "h": tk_yazi_max_y - tk_yazi_min_y,
    }

    # 5. Soru işareti
    q: float = 27.0
    QX: float = 987.0 - 16.0 * q
    QY: float = 903.0 - 5.0 * q
    qm_paths: list[str] = Y.tabler("question-mark", AD / "cizim")
    assert len(qm_paths) == 2, f"qm_paths uzunluğu {len(qm_paths)} != 2"
    assert qm_paths[0].startswith("M8 8a3.5"), f"qm_paths[0] beklenmeyen: {qm_paths[0][:20]}"
    assert qm_paths[1].startswith("M12 19l0"), f"qm_paths[1] beklenmeyen: {qm_paths[1][:20]}"

    soru_paths_svg: str = "".join(f'<path d="{d}"/>' for d in qm_paths)
    soru_svg: str = (
        f'<g id="soru" transform="translate({QX:.2f} {QY:.2f}) scale({q:.4f})" '
        f'fill="none" stroke="{vur_c}" stroke-width="{26.0 / q:.4f}" '
        f'stroke-linecap="round" stroke-linejoin="round">{soru_paths_svg}</g>'
    )

    soru_x0: float = 8.0 * q + QX - 13.0
    soru_x1: float = 16.0 * q + QX + 13.0
    soru_y0: float = 5.0 * q + QY - 13.0
    soru_y1: float = 19.0 * q + QY + 13.0
    soru_blok: dict[str, float] = {
        "ad": "soru",
        "x": soru_x0,
        "y": soru_y0,
        "w": soru_x1 - soru_x0,
        "h": soru_y1 - soru_y0,
    }

    fig_blok: dict[str, float] = {
        "ad": "fig",
        "x": FIG_X,
        "y": FIG_UST,
        "w": (x1_k - x0) * fs,
        "h": FIG_H,
    }
    bas_blok: dict[str, float] = {
        "ad": "bas",
        "x": bas_px_x,
        "y": bas_px_y,
        "w": bas_px_w,
        "h": bas_px_h,
    }
    el_blok: dict[str, float] = {
        "ad": "el",
        "x": el_px_x,
        "y": el_px_y,
        "w": el_px_w,
        "h": el_px_h,
    }
    zc_blok: dict[str, float] = {
        "ad": "zc",
        "x": 64.0,
        "y": 1342.0,
        "w": 952.0,
        "h": 4.0,
    }

    return (
        zc_svg, takvim_svg, tk_yazi_svg, fig_svg, soru_svg,
        TT, fs, fig_blok, bas_blok, el_blok, takvim_blok, takvim_yazi_blok, soru_blok, zc_blok
    )


def blok_kutulari(
    S: int,
    T1: float,
    T2: float,
    x1: float,
    x2: float,
    g1: float,
    g2: float,
    fig_blok: dict[str, float],
    bas_blok: dict[str, float],
    el_blok: dict[str, float],
    takvim_blok: dict[str, float],
    takvim_yazi_blok: dict[str, float],
    soru_blok: dict[str, float],
    zc_blok: dict[str, float],
) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını döndürür (§6.3, §6.4)."""
    hud: dict[str, float] = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}
    bas_x: float = min(x1, x2)
    bas_w: float = max(x1 + g1, x2 + g2) - bas_x
    bas_y: float = T1 - 0.86 * S
    bas_h: float = (T2 + 0.10 * S) - bas_y
    baslik: dict[str, float] = {"ad": "baslik", "x": bas_x, "y": bas_y, "w": bas_w, "h": bas_h}

    # §6.3 ve §6.4 sırası: hud, baslik, fig, bas, el, takvim, takvim-yazi, soru, zc
    return [hud, baslik, fig_blok, bas_blok, el_blok, takvim_blok, takvim_yazi_blok, soru_blok, zc_blok]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx: float = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy: float = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], S: int, TT: int, T1: float, T2: float, html: str) -> None:
    """SPEC.md §6 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict: dict[str, dict[str, float]] = {b["ad"]: b for b in bloklar}

    # 1. Bütün bloklar x in [48, 1032]; y+h <= 1536
    for b in bloklar:
        name: str = str(b["ad"])
        assert b["x"] >= 48.0 - 1e-4, f"{name} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{name} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0 - 1e-4, f"{name} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1536.0 + 1e-4, f"{name} alt {b['y'] + b['h']} > 1536"

    # baslik, fig, takvim, soru, zc x in [64, 1016]
    for name in ["baslik", "fig", "takvim", "soru", "zc"]:
        b = b_dict[name]
        assert b["x"] >= 64.0 - 1e-4, f"{name} sol {b['x']} < 64"
        assert b["x"] + b["w"] <= 1016.0 + 1e-4, f"{name} sağ {b['x'] + b['w']} > 1016"

    # fig, takvim, soru alt kenarı <= 1344 + 4
    for name in ["fig", "takvim", "soru"]:
        b = b_dict[name]
        assert b["y"] + b["h"] <= 1344.0 + 4.0 + 1e-4, f"{name} alt {b['y'] + b['h']} > 1348"

    # 2. Yazı boyu: S >= 64, TT >= 72
    assert S >= 64, f"Başlık boyutu {S} < 64"
    assert TT >= 72, f"Takvim yazı boyutu {TT} < 72"

    satirlar: list[str] = ["YDT · BASIC", "TODAY VARSA", "HANGİ ZAMAN?", "today"]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    baslik_satirlari: list[str] = ["TODAY VARSA", "HANGİ ZAMAN?"]
    assert len(baslik_satirlari) == 2, f"Başlık satır sayısı {len(baslik_satirlari)} != 2"
    baslik_sozcukleri: list[str] = " ".join(baslik_satirlari).split()
    assert len(baslik_sozcukleri) == 4, f"Başlık sözcük sayısı {len(baslik_sozcukleri)} != 4"
    assert "\u0130" in "HANGİ ZAMAN?", "HANGİ içinde U+0130 yok"

    # 3. Kesişim 0 olmalı:
    # [hud, baslik, takvim, soru] çiftlerinin hepsi
    dortlu: list[dict[str, float]] = [b_dict["hud"], b_dict["baslik"], b_dict["takvim"], b_dict["soru"]]
    for i in range(len(dortlu)):
        for j in range(i + 1, len(dortlu)):
            k_val: float = kesisim(dortlu[i], dortlu[j])
            assert k_val == 0.0, f"Kesişim {dortlu[i]['ad']} - {dortlu[j]['ad']}: {k_val}"

    assert kesisim(b_dict["baslik"], b_dict["fig"]) == 0.0, "Kesişim baslik - fig"
    assert kesisim(b_dict["fig"], b_dict["soru"]) == 0.0, "Kesişim fig - soru"
    assert kesisim(b_dict["bas"], b_dict["takvim"]) == 0.0, "Kesişim bas - takvim"
    assert kesisim(b_dict["el"], b_dict["takvim-yazi"]) == 0.0, "Kesişim el - takvim-yazi"

    # takvim-yazi tamamen takvim içinde
    ty: dict[str, float] = b_dict["takvim-yazi"]
    tk: dict[str, float] = b_dict["takvim"]
    assert ty["x"] >= tk["x"] - 1e-4, f"takvim-yazi sol {ty['x']} < takvim sol {tk['x']}"
    assert ty["x"] + ty["w"] <= tk["x"] + tk["w"] + 1e-4, "takvim-yazi sağ > takvim sağ"
    assert ty["y"] >= tk["y"] - 1e-4, "takvim-yazi üst < takvim üst"
    assert ty["y"] + ty["h"] <= tk["y"] + tk["h"] + 1e-4, "takvim-yazi alt > takvim alt"

    # Boşluklar
    assert b_dict["baslik"]["y"] - 288.0 >= 40.0, f"baslik.y - 288 = {b_dict['baslik']['y'] - 288.0} < 40"
    en_ust_sahne: float = min(b_dict["takvim"]["y"], b_dict["fig"]["y"], b_dict["soru"]["y"])
    baslik_alt: float = b_dict["baslik"]["y"] + b_dict["baslik"]["h"]
    assert en_ust_sahne - baslik_alt >= 48.0, f"sahne üst - baslik alt = {en_ust_sahne - baslik_alt} < 48"
    assert b_dict["soru"]["x"] - (b_dict["takvim"]["x"] + b_dict["takvim"]["w"]) >= 32.0, "soru.x - takvim.sağ < 32"
    assert b_dict["takvim"]["x"] - (b_dict["bas"]["x"] + b_dict["bas"]["w"]) >= 32.0, "takvim.x - bas.sağ < 32"

    satir1_alt: float = T1 + 0.25 * S
    satir2_i_ust: float = T2 - 0.94 * S
    assert satir1_alt < satir2_i_ust, f"satır 1 alt {satir1_alt} >= satır 2 İ noktası üstü {satir2_i_ust}"

    # 5. Hex beyaz listesi
    hex_kumesi: set[str] = set(re.findall(r"#[0-9a-fA-F]{6}\b", html))
    beyaz_liste: set[str] = {"#1b1a17", "#f3efe6", "#c9c2b3", "#f2a93b"}
    assert hex_kumesi.issubset(beyaz_liste), f"Beyaz liste dışı hex: {hex_kumesi - beyaz_liste}"

    # 6. Yasak kontrolleri
    html_lower: str = html.lower()
    yasaklar: list[str] = [
        "kanal", "qr", "6 dk", "wears", "is wearing", "ikisi de", "şimdiki", "geniş",
        "math.random", "date.now", "new date", "opacity:0"
    ]
    for yk in yasaklar:
        assert yk not in html_lower, f"Yasak ifade bulundu: {yk}"

    assert "<circle" not in html, "<circle> yasak"
    assert 'id="t2"' not in html, "id t2 yasak"
    assert 'id="ku-nokta"' not in html, "id ku-nokta yasak"
    assert 'id="rz1"' not in html, "id rz1 yasak"
    assert "try" not in html_lower, "try yasak"
    assert "catch" not in html_lower, "catch yasak"


def uret() -> tuple[str, int, int, float, list[dict[str, float]]]:
    """Sahne HTML'i, font boyutları ve nesnelerini üretir."""
    S, g1, g2, T1, T2, x1, x2 = hesapla_s()
    kunye: str = kunye_svg()
    baslik: str = baslik_svg(S, T1, T2, x1, x2)
    (
        zc, takvim, tk_yazi, fig, soru,
        TT, fs, fig_b, bas_b, el_b, takvim_b, tk_yazi_b, soru_b, zc_b
    ) = sahne_svg()

    bloklar: list[dict[str, float]] = blok_kutulari(
        S, T1, T2, x1, x2, g1, g2,
        fig_b, bas_b, el_b, takvim_b, tk_yazi_b, soru_b, zc_b
    )

    font_css_str: str = Y.font_css()
    zemin_css_str: str = Y.ZEMIN_CSS
    zemin_html_str: str = Y.zemin_html()

    html: str = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{font_css_str}
{zemin_css_str}
#sahne{{position:absolute;left:0;top:0;}}
#root .dz{{fill:var(--zemin,#1b1a17)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{sure_sn}" data-fps="30" data-width="1080" data-height="1920">
{zemin_html_str}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{baslik}
{zc}
{takvim}
{tk_yazi}
{fig}
{soru}
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var tl = gsap.timeline({{ paused: true }});
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, 0);
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, {sure_sn});
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""

    kurallari_dogrula(bloklar, S, TT, T1, T2, html)
    return html, S, TT, fs, bloklar


if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, S, TT, fs, bloklar = uret()
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
    print(f"S={S} TT={TT} fs={fs:.5f}")

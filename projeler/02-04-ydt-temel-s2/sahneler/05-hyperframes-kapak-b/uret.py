#!/usr/bin/python3
"""02-04-ydt-temel-s2 sahne 05 kapak B (soru) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).

Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Huni v2 (15.11, D-S2-V2): v1 HUD/figür/zemin çizgisi yerine kanal katmanı + künye (yardim.py) ve kapak görseli (karakter.png).
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

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
assert set(R.keys()) >= {"zemin", "murekkep", "vurgu"}

W: int = Y.W
H: int = Y.H
KENAR_X: float = 60.0
SAG: float = 960.0
ICERIK_UST: float = 460.0
ICERIK_ALT: float = 1380.0
BASLIK_ALT: float = 800.0
SAHNE_UST: float = 820.0
BASLIK_GEN: float = 900.0
S_UST: float = 190.0
KENAR_PX: float = 10.0
KENAR_GECIS: int = 3
ESIK: int = 64
PAY: float = 16.0
KS: float = 0.56
YUZ_PNG: tuple[float, float] = (461.0, 470.0)

KARAKTER: Path = PAKET / "ortak" / "kapak" / "karakter.png"


def alfa_kutusu(yol: Path) -> tuple[int, int, int, int]:
    """PNG'nin saydam olmayan kutusu (x0, y0, x1, y1)."""
    a = Image.open(yol).split()[-1].point(lambda v: 255 if v > ESIK else 0)
    kutu = a.getbbox()
    assert kutu is not None, f"{yol.name} tamamen saydam"
    return kutu


def maske(yol: Path, x: float, y: float, s: float) -> np.ndarray:
    """Görselin tuvaldeki saydamlık maskesi (bool, H x W). x, y = dosyanın sol üstü, s = ölçek."""
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


def daire_kutu_uzakligi(cx: float, cy: float, k: tuple[float, float, float, float]) -> float:
    """Daire merkezinin kutuya en kısa uzaklığı."""
    dx = max(k[0] - cx, 0.0, cx - k[2])
    dy = max(k[1] - cy, 0.0, cy - k[3])
    return math.hypot(dx, dy)


def to_kutu(b: dict[str, float]) -> tuple[float, float, float, float]:
    """Blok sözlüğünü (x0, y0, x1, y1) demetine çevirir."""
    return (b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"])


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx: float = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy: float = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def gorsel_img(ad: str, yol: Path, yer: tuple[float, float, float]) -> str:
    """Çıkartma kenarlı görsel (<img>, dosyanın tamamı ölçekli)."""
    x, yy, s = yer
    im = Image.open(yol)
    return (
        f'<img id="{ad}" class="abs kenar" src="assets/{yol.name}" alt="" '
        f'style="left:{x:.1f}px;top:{yy:.1f}px;width:{im.width * s:.1f}px;height:{im.height * s:.1f}px">'
    )


def hesapla_s() -> tuple[int, float, float, float, float]:
    """Başlık font boyutu S ve yerleşim tabanlarını hesaplar (§4.2)."""
    s0: float = 100.0
    g1_100: float = Y.genislik("Fredoka", 700, "TODAY VARSA", s0)
    g2_100: float = Y.genislik("Fredoka", 700, "HANGİ ZAMAN?", s0)
    S: int = math.floor(min(S_UST, BASLIK_GEN * 100.0 / g1_100, BASLIK_GEN * 100.0 / g2_100))

    g1: float = Y.genislik("Fredoka", 700, "TODAY VARSA", S)
    g2: float = Y.genislik("Fredoka", 700, "HANGİ ZAMAN?", S)

    while (g1 > BASLIK_GEN or g2 > BASLIK_GEN) and S > 1:
        S -= 1
        g1 = Y.genislik("Fredoka", 700, "TODAY VARSA", S)
        g2 = Y.genislik("Fredoka", 700, "HANGİ ZAMAN?", S)

    assert g1 <= BASLIK_GEN, f"g1={g1} > {BASLIK_GEN}"
    assert g2 <= BASLIK_GEN, f"g2={g2} > {BASLIK_GEN}"

    T1: float = 630.0 - 0.25 * S
    T2: float = T1 + 1.26 * S

    return S, g1, g2, T1, T2


def baslik_svg(S: int, T1: float, T2: float) -> str:
    """Başlık (<g id="baslik">) SVG çıktısı (§4.2)."""
    mur_c: str = R["murekkep"]
    zem_c: str = R["zemin"]
    bs_1: str = (
        f'<text id="bs-1" x="{KENAR_X:.0f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{mur_c}" stroke="{zem_c}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">TODAY VARSA</text>'
    )
    bs_2: str = (
        f'<text id="bs-2" x="{KENAR_X:.0f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{mur_c}" stroke="{zem_c}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">HANGİ ZAMAN?</text>'
    )
    return f'<g id="baslik">{bs_1}{bs_2}</g>'


def takvim_svg(Ox: float, Oy: float, k: float, TC: tuple[float, float]) -> tuple[str, dict[str, float]]:
    """Takvim yaprağı (<g id="takvim">) SVG çıktısı ve bloğunu üretir (§4.5)."""
    mur_c: str = R["murekkep"]
    cal_paths: list[str] = Y.tabler("calendar")
    assert len(cal_paths) >= 4, f"cal_paths uzunluğu {len(cal_paths)} < 4"
    assert cal_paths[0].startswith("M4 7a2"), f"cal_paths[0] beklenmeyen: {cal_paths[0][:20]}"
    assert cal_paths[1].startswith("M16 3v4"), f"cal_paths[1] beklenmeyen: {cal_paths[1][:20]}"
    assert cal_paths[2].startswith("M8 3v4"), f"cal_paths[2] beklenmeyen: {cal_paths[2][:20]}"
    assert cal_paths[3].startswith("M4 11h16"), f"cal_paths[3] beklenmeyen: {cal_paths[3][:20]}"

    takvim_paths_svg: str = "".join(f'<path d="{d}"/>' for d in cal_paths[:4])
    svg: str = (
        f'<g id="takvim" transform="rotate(4 {TC[0]:.2f} {TC[1]:.2f}) translate({Ox:.2f} {Oy:.2f}) scale({k:.4f})" '
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
    rot_tk: list[tuple[float, float]] = []
    for px, py in noktalar:
        dx: float = px - TC[0]
        dy: float = py - TC[1]
        rx: float = TC[0] + dx * cos_a - dy * sin_a
        ry: float = TC[1] + dx * sin_a + dy * cos_a
        rot_tk.append((rx, ry))

    tk_min_x: float = min(p[0] for p in rot_tk) - 3.0
    tk_max_x: float = max(p[0] for p in rot_tk) + 3.0
    tk_min_y: float = min(p[1] for p in rot_tk) - 3.0
    tk_max_y: float = max(p[1] for p in rot_tk) + 3.0
    blok: dict[str, float] = {
        "ad": "takvim",
        "x": tk_min_x,
        "y": tk_min_y,
        "w": tk_max_x - tk_min_x,
        "h": tk_max_y - tk_min_y,
    }
    return svg, blok


def takvim_yazi_svg(
    TK: float, Oy: float, k: float, TC: tuple[float, float]
) -> tuple[str, int, dict[str, float]]:
    """Takvim yazısı (<g id="tk-yazi-g">) SVG çıktısı ve bloğunu üretir (§4.6)."""
    mur_c: str = R["murekkep"]
    w_today_100: float = Y.genislik("Caveat", 700, "today", 100.0)
    TT: int = min(100, math.floor((TK - 56.0) * 100.0 / w_today_100))
    assert TT >= 64, f"TT={TT} < 64"

    # Caveat mürekkebi ilerleme kutusundan sağa kayar (y kuyruğu): 1. tur karesinde sol 30 / sağ 12 px -> merkez 0,09·TT sola
    x_tk: float = 590.0 - 0.09 * TT
    Hy: float = Oy + 11.0 * k
    taban_tk: float = (Hy + 1070.0) / 2.0 + 0.30 * TT
    svg: str = (
        f'<g id="tk-yazi-g" transform="rotate(4 {TC[0]:.2f} {TC[1]:.2f})">'
        f'<text id="tk-yazi" x="{x_tk:.2f}" y="{taban_tk:.2f}" text-anchor="middle" '
        f'font-family="Caveat" font-weight="700" font-size="{TT}" fill="{mur_c}">today</text></g>'
    )

    w_today: float = Y.genislik("Caveat", 700, "today", TT)
    corners: list[tuple[float, float]] = [
        (x_tk - w_today / 2.0, taban_tk - 0.75 * TT),
        (x_tk + w_today / 2.0, taban_tk - 0.75 * TT),
        (x_tk + w_today / 2.0, taban_tk + 0.30 * TT),
        (x_tk - w_today / 2.0, taban_tk + 0.30 * TT),
    ]
    rad: float = math.radians(4.0)
    cos_a: float = math.cos(rad)
    sin_a: float = math.sin(rad)
    rot_ty: list[tuple[float, float]] = []
    for px, py in corners:
        dx: float = px - TC[0]
        dy: float = py - TC[1]
        rx: float = TC[0] + dx * cos_a - dy * sin_a
        ry: float = TC[1] + dx * sin_a + dy * cos_a
        rot_ty.append((rx, ry))

    ty_min_x: float = min(p[0] for p in rot_ty)
    ty_max_x: float = max(p[0] for p in rot_ty)
    ty_min_y: float = min(p[1] for p in rot_ty)
    ty_max_y: float = max(p[1] for p in rot_ty)
    blok: dict[str, float] = {
        "ad": "takvim-yazi",
        "x": ty_min_x,
        "y": ty_min_y,
        "w": ty_max_x - ty_min_x,
        "h": ty_max_y - ty_min_y,
    }
    return svg, TT, blok


def soru_svg() -> tuple[str, dict[str, float]]:
    """Soru işareti (<g id="soru">) SVG çıktısı ve bloğunu üretir (§4.7)."""
    vur_c: str = R["vurgu"]
    q: float = 23.0
    QX: float = 950.0 - 13.0 - 16.0 * q
    QY: float = 900.0 + 13.0 - 5.0 * q
    qm_paths: list[str] = Y.tabler("question-mark", AD / "cizim")
    assert len(qm_paths) == 2, f"qm_paths uzunluğu {len(qm_paths)} != 2"
    assert qm_paths[0].startswith("M8 8a3.5"), f"qm_paths[0] beklenmeyen: {qm_paths[0][:20]}"
    assert qm_paths[1].startswith("M12 19l0"), f"qm_paths[1] beklenmeyen: {qm_paths[1][:20]}"

    soru_paths_svg: str = "".join(f'<path d="{d}"/>' for d in qm_paths)
    svg: str = (
        f'<g id="soru" transform="translate({QX:.2f} {QY:.2f}) scale({q:.4f})" '
        f'fill="none" stroke="{vur_c}" stroke-width="{26.0 / q:.4f}" '
        f'stroke-linecap="round" stroke-linejoin="round">{soru_paths_svg}</g>'
    )

    soru_x0: float = 8.0 * q + QX - 13.0
    soru_x1: float = 16.0 * q + QX + 13.0
    soru_y0: float = 5.0 * q + QY - 13.0
    soru_y1: float = 19.0 * q + QY + 13.0
    blok: dict[str, float] = {
        "ad": "soru",
        "x": soru_x0,
        "y": soru_y0,
        "w": soru_x1 - soru_x0,
        "h": soru_y1 - soru_y0,
    }
    return svg, blok


def kurallari_dogrula(
    bloklar: list[dict[str, float]],
    S: int,
    TT: int,
    T1: float,
    T2: float,
    html: str,
    km: np.ndarray,
    r: int,
    F: tuple[float, float],
) -> None:
    """SPEC.md §6 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict: dict[str, dict[str, float]] = {b["ad"]: b for b in bloklar}

    # 1. Bütün bloklar x in [53, 960]; y+h <= 1380
    for b in bloklar:
        name: str = str(b["ad"])
        if name != "kanal":
            assert b["x"] >= 60.0 - 1e-4, f"{name} sol kenar {b['x']} < 60"
        else:
            assert b["x"] >= 53.0 - 1e-4, f"kanal sol kenar {b['x']} < 53"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{name} sağ kenar {b['x'] + b['w']} > 960"
        assert b["y"] + b["h"] <= 1380.0 + 1e-4, f"{name} alt kenar {b['y'] + b['h']} > 1380"

    # Sınırlar (§6.2)
    assert 280.0 - 1e-4 <= b_dict["kanal"]["y"] and b_dict["kanal"]["y"] + b_dict["kanal"]["h"] <= 350.0 + 1e-4
    assert 360.0 - 1e-4 <= b_dict["kunye"]["y"] and b_dict["kunye"]["y"] + b_dict["kunye"]["h"] <= 450.0 + 1e-4
    assert b_dict["kunye"]["x"] + b_dict["kunye"]["w"] <= 960.0 + 1e-4
    assert 460.0 - 1e-4 <= b_dict["baslik"]["y"] and b_dict["baslik"]["y"] + b_dict["baslik"]["h"] <= 800.0 + 1e-4

    for name in ["karakter", "daire", "takvim", "soru"]:
        b = b_dict[name]
        assert b["y"] >= 820.0 - 1e-4, f"{name} üst {b['y']} < 820"
        assert b["y"] + b["h"] <= 1380.0 + 1e-4, f"{name} alt {b['y'] + b['h']} > 1380"

    # 2. Çakışma (§6.3)
    besli: list[dict[str, float]] = [b_dict["kanal"], b_dict["kunye"], b_dict["baslik"], b_dict["takvim"], b_dict["soru"]]
    for i in range(len(besli)):
        for j in range(i + 1, len(besli)):
            k_val: float = kesisim(besli[i], besli[j])
            assert k_val == 0.0, f"Kesişim {besli[i]['ad']} - {besli[j]['ad']}: {k_val}"

    assert kesisim(b_dict["karakter"], b_dict["baslik"]) == 0.0, "Kesişim karakter - baslik"
    assert kesisim(b_dict["karakter"], b_dict["soru"]) == 0.0, "Kesişim karakter - soru"

    assert bos_mu(km, to_kutu(b_dict["takvim"]), KENAR_PX + PAY), "takvim karakter maskesi ile çakışıyor"
    assert bos_mu(km, to_kutu(b_dict["soru"]), KENAR_PX + PAY), "soru karakter maskesi ile çakışıyor"
    assert bos_mu(km, to_kutu(b_dict["baslik"]), KENAR_PX + PAY), "baslik karakter maskesi ile çakışıyor"

    for name in ["takvim", "baslik", "soru"]:
        dist: float = daire_kutu_uzakligi(F[0], F[1], to_kutu(b_dict[name]))
        assert dist >= r + PAY - 1e-4, f"daire - {name} uzaklık {dist} < {r + PAY}"

    # takvim-yazi tamamen takvim içinde
    ty: dict[str, float] = b_dict["takvim-yazi"]
    tk: dict[str, float] = b_dict["takvim"]
    assert ty["x"] >= tk["x"] - 1e-4, f"takvim-yazi sol {ty['x']} < takvim sol {tk['x']}"
    assert ty["x"] + ty["w"] <= tk["x"] + tk["w"] + 1e-4, "takvim-yazi sağ > takvim sağ"
    assert ty["y"] >= tk["y"] - 1e-4, "takvim-yazi üst < takvim üst"
    assert ty["y"] + ty["h"] <= tk["y"] + tk["h"] + 1e-4, "takvim-yazi alt > takvim alt"

    # Boşluklar
    assert b_dict["soru"]["x"] - (b_dict["takvim"]["x"] + b_dict["takvim"]["w"]) >= 32.0, "soru.x - takvim.sağ < 32"
    en_ust_sahne: float = min(b_dict["takvim"]["y"], b_dict["soru"]["y"], b_dict["karakter"]["y"])
    baslik_alt: float = b_dict["baslik"]["y"] + b_dict["baslik"]["h"]
    assert en_ust_sahne - baslik_alt >= 48.0, f"sahne üst - baslik alt = {en_ust_sahne - baslik_alt} < 48"

    satir1_alt: float = T1 + 0.25 * S
    satir2_i_ust: float = T2 - 0.94 * S
    assert satir1_alt < satir2_i_ust, f"satır 1 alt {satir1_alt} >= satır 2 İ noktası üstü {satir2_i_ust}"

    # 3. Yazı boyu (§6.4)
    assert 64 <= S <= 190, f"Başlık boyutu {S} aralık dışı [64, 190]"
    assert TT >= 64, f"Takvim yazı boyutu {TT} < 64"

    satirlar: list[str] = ["TODAY VARSA", "HANGİ ZAMAN?", "today"]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    baslik_satirlari: list[str] = ["TODAY VARSA", "HANGİ ZAMAN?"]
    assert len(baslik_satirlari) == 2, f"Başlık satır sayısı {len(baslik_satirlari)} != 2"
    baslik_sozcukleri: list[str] = " ".join(baslik_satirlari).split()
    assert len(baslik_sozcukleri) == 4, f"Başlık sözcük sayısı {len(baslik_sozcukleri)} != 4"
    assert "\u0130" in "HANGİ ZAMAN?", "HANGİ içinde U+0130 yok"

    # 4. Yapı (§6.5)
    assert html.count('<g id="kanal">') == 1, '<g id="kanal"> tam 1 kez olmalı'
    kunye_match = re.search(r'<g id="kunye">[\s\S]*?</g>\s*</g>', html)
    assert kunye_match is not None and '<g id="kanal">' in kunye_match.group(0), '<g id="kanal"> <g id="kunye"> içinde olmalı'
    assert html.count('id="logoimg"') == 1, 'id="logoimg" tam 1 kez olmalı'
    assert html.count('@ydspublishing') == 1, '@ydspublishing tam 1 kez olmalı'
    assert 'tl.set("#sahne"' not in html, 'tl.set("#sahne" html içinde geçmemeli'
    assert '"#kanal"' not in html, '"#kanal" GSAP hedefi olmamalı'
    assert "#root.tema-acik" not in html, "#root.tema-acik dizesi geçmemeli"
    assert html.count("<circle") == 1, "<circle tam 1 kez olmalı"
    circle_match = re.search(r"<circle[^>]*>", html)
    assert circle_match is not None and "fill=" not in circle_match.group(0), "<circle üzerinde fill= olmamalı"
    assert html.count('src="assets/karakter.png"') == 1, 'src="assets/karakter.png" tam 1 kez olmalı'

    # 5. Hex beyaz listesi (§6.7)
    hex_kumesi: set[str] = set(re.findall(r"#[0-9a-fA-F]{6}\b", html))
    beyaz_liste: set[str] = {"#1b1a17", "#f3efe6", "#c9c2b3", "#f2a93b"}
    assert hex_kumesi.issubset(beyaz_liste), f"Beyaz liste dışı hex: {hex_kumesi - beyaz_liste}"

    # 6. Yasak kontrolleri (§6.8)
    html_lower: str = html.lower()
    # düzenli ifade: boşluk/ı-i çeşitlerini de yakalar (huni v2 §1 kural 4–5)
    yasaklar: list[str] = [
        r"tam\s+ders", r"dak[iı]ka", r"\sdk\b", "qr", "izle", "oynat", "wears", r"is\s+wearing",
        "şimdiki", "geniş", r"math\.random", r"date\.now", r"new\s+date", "opacity:0", "try", "catch"
    ]
    for yk in yasaklar:
        assert re.search(yk, html_lower) is None, f"Yasak ifade bulundu: {yk}"

    assert re.search(r"[\U0001F000-\U0001FAFF☀-➿]", html) is None, "Emoji bulundu"


def uret() -> tuple[str, int, int, float, int, float, float, list[dict[str, float]]]:
    """Sahne HTML'i, font boyutları ve nesnelerini üretir."""
    S, g1, g2, T1, T2 = hesapla_s()

    # Karakter ölçümü (§4.3)
    ax0, ay0, ax1, ay1 = alfa_kutusu(KARAKTER)
    assert abs(ax0 - 21) <= 2 and abs(ay0 - 173) <= 2 and abs(ax1 - 878) <= 2 and abs(ay1 - 1112) <= 2

    X0: float = 70.0 - ax0 * KS
    Y0: float = 1370.0 - ay1 * KS
    vis_x0: float = X0 + ax0 * KS
    vis_y0: float = Y0 + ay0 * KS
    vis_x1: float = X0 + ax1 * KS
    vis_y1: float = Y0 + ay1 * KS
    karakter_blok: dict[str, float] = {
        "ad": "karakter",
        "x": vis_x0 - KENAR_PX,
        "y": vis_y0 - KENAR_PX,
        "w": (vis_x1 - vis_x0) + 2.0 * KENAR_PX,
        "h": (vis_y1 - vis_y0) + 2.0 * KENAR_PX,
    }

    km: np.ndarray = maske(KARAKTER, X0, Y0, KS)
    F: tuple[float, float] = (X0 + YUZ_PNG[0] * KS, Y0 + YUZ_PNG[1] * KS)

    # Başlık bloğu (§4.2)
    bas_x: float = KENAR_X
    bas_y: float = T1 - 0.86 * S
    bas_w: float = max(g1, g2)
    bas_h: float = (T2 + 0.10 * S) - bas_y
    baslik_blok: dict[str, float] = {"ad": "baslik", "x": bas_x, "y": bas_y, "w": bas_w, "h": bas_h}

    # Takvim (§4.5)
    TK: float = 200.0
    k: float = TK / 16.0
    Ox: float = 490.0 - 4.0 * k
    Oy: float = 870.0 - 5.0 * k
    TC: tuple[float, float] = (590.0, 970.0)
    takvim_str, takvim_blok = takvim_svg(Ox, Oy, k, TC)

    # Takvim yazısı (§4.6)
    tk_yazi_str, TT, takvim_yazi_blok = takvim_yazi_svg(TK, Oy, k, TC)

    # Soru (§4.7)
    soru_str, soru_blok = soru_svg()

    # Daire yarıçapı (§4.4)
    r: int = math.floor(
        min(
            0.36 * (ay1 - ay0) * KS,
            daire_kutu_uzakligi(F[0], F[1], to_kutu(takvim_blok)) - PAY,
            F[1] - SAHNE_UST,
            daire_kutu_uzakligi(F[0], F[1], to_kutu(baslik_blok)) - PAY,
        )
    )
    daire_blok: dict[str, float] = {
        "ad": "daire",
        "x": F[0] - r,
        "y": F[1] - r,
        "w": 2.0 * r,
        "h": 2.0 * r,
    }

    # Kanal ve künye blokları (§6.1)
    kanal_w: float = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42.0) - 53.0
    kanal_blok: dict[str, float] = {"ad": "kanal", "x": 53.0, "y": 291.0, "w": kanal_w, "h": 50.0}

    rx, rw = Y.rozet_konumu()
    kunye_w: float = rx + rw - 60.0
    kunye_blok: dict[str, float] = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": kunye_w, "h": 48.0}

    bloklar: list[dict[str, float]] = [
        kanal_blok,
        kunye_blok,
        baslik_blok,
        karakter_blok,
        daire_blok,
        takvim_blok,
        takvim_yazi_blok,
        soru_blok,
    ]

    adim: float = KENAR_PX / KENAR_GECIS
    kenar: str = " ".join(
        f"drop-shadow({dx:.2f}px {dy:.2f}px 0 #f3efe6)"
        for _ in range(KENAR_GECIS)
        for dx, dy in ((adim, 0.0), (-adim, 0.0), (0.0, adim), (0.0, -adim))
    )

    kunye_str: str = Y.kunye_svg()
    baslik_str: str = baslik_svg(S, T1, T2)
    karakter_img_str: str = gorsel_img("karakter", KARAKTER, (X0, Y0, KS))

    font_css_str: str = Y.font_css()
    zemin_css_str: str = Y.ZEMIN_CSS
    zemin_html_str: str = Y.zemin_html()

    html: str = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{font_css_str}
{zemin_css_str}
#sahne,#alt{{position:absolute;left:0;top:0;}}
.kenar{{filter:{kenar};}}
#daire{{fill:#f3efe6;display:none;}}
.tema-acik #daire{{display:inline;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{sure_sn:.1f}" data-fps="30" data-width="1080" data-height="1920">
{zemin_html_str}
<svg id="alt" class="abs" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<circle id="daire" cx="{F[0]:.1f}" cy="{F[1]:.1f}" r="{r}"/>
</svg>
{karakter_img_str}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye_str}
{baslik_str}
{takvim_str}
{tk_yazi_str}
{soru_str}
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
var tl = gsap.timeline({{paused:true}});
tl.set("#baslik",{{opacity:1,immediateRender:false}},0);
tl.set("#baslik",{{opacity:1,immediateRender:false}},{sure_sn:.1f});
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
</script></body></html>"""

    kurallari_dogrula(bloklar, S, TT, T1, T2, html, km, r, F)
    return html, S, TT, KS, r, X0, Y0, bloklar


if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, S, TT, KS, r, X0, Y0, bloklar = uret()
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
    print(f"S={S} TT={TT} KS={KS} r={r} X0={X0:.1f} Y0={Y0:.1f}")

#!/usr/bin/python3
"""simple-present-temel-s2 sahne 06 kapak B (soru) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok; huni v2)."""
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

W: int = Y.W
H: int = Y.H
X0: int = 60
X1: int = 960
Y0: int = 460
Y1: int = 1380
KANAL_Y: tuple[int, int] = (280, 350)
KUNYE_Y: tuple[int, int] = (360, 450)
GORSEL_Y: tuple[int, int] = (820, 1380)

BAS_X: int = 60
BASLIK_GEN: int = 894  # 900 - 6 sağ kontur payı
S_UST: int = 190
BASLIK_SATIR1: str = "ALWAYS VARSA"
BASLIK_SATIR2: str = "HANGİ ZAMAN?"  # İ = U+0130

KIT: Path = ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg"
BS: float = 1.70
BAS_CIZGI: float = 4.0

BL_X: int = 524
BL_Y: int = 836
BL_W: int = 426
BL_H: int = 148
BL_R: int = 28
BL_CIZGI: int = 4
UC: tuple[int, int] = (472, 1040)
BL_YAZI: int = 72
BALON_METIN: str = "always?"

Q: int = 24
QX: int = 939 - 16 * Q  # = 555
QY: int = 1363 - 19 * Q  # = 907


def hesapla_s() -> tuple[int, float, float, float, float]:
    """Başlık font boyutu S ve yerleşim tabanlarını hesaplar (SPEC §4.2)."""
    s0: float = 100.0
    g1_100: float = Y.genislik("Fredoka", 700, BASLIK_SATIR1, s0)
    g2_100: float = Y.genislik("Fredoka", 700, BASLIK_SATIR2, s0)
    S: int = math.floor(min(float(S_UST), BASLIK_GEN * 100.0 / g1_100, BASLIK_GEN * 100.0 / g2_100))

    g1: float = Y.genislik("Fredoka", 700, BASLIK_SATIR1, S)
    g2: float = Y.genislik("Fredoka", 700, BASLIK_SATIR2, S)

    while (g1 > BASLIK_GEN or g2 > BASLIK_GEN) and S > 1:
        S -= 1
        g1 = Y.genislik("Fredoka", 700, BASLIK_SATIR1, S)
        g2 = Y.genislik("Fredoka", 700, BASLIK_SATIR2, S)

    assert g1 <= BASLIK_GEN, f"g1={g1} > {BASLIK_GEN}"
    assert g2 <= BASLIK_GEN, f"g2={g2} > {BASLIK_GEN}"
    assert S == 116, f"S={S} != 116"

    T1: float = 630.0 - 0.25 * S
    T2: float = T1 + 1.26 * S

    return S, g1, g2, T1, T2


def baslik_svg(S: int, T1: float, T2: float) -> str:
    """Başlık (<g id="baslik">) SVG çıktısı (SPEC §4.2)."""
    mur: str = R["murekkep"]
    zem: str = R["zemin"]
    bs_1: str = (
        f'<text id="bs-1" x="{BAS_X}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{mur}" stroke="{zem}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">{BASLIK_SATIR1}</text>'
    )
    bs_2: str = (
        f'<text id="bs-2" x="{BAS_X}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{mur}" stroke="{zem}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">{BASLIK_SATIR2}</text>'
    )
    return f'<g id="baslik">{bs_1}{bs_2}</g>'


def ogrenci_basi_oku() -> tuple[list[str], float, float, float, float, float, float]:
    """Öğrenci başı yollarını okur ve kutu/dönüşüm değerlerini hesaplar (SPEC §4.3)."""
    kit_metin: str = KIT.read_text(encoding="utf-8")
    yollar: list[str] = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit_metin)
    assert len(yollar) == 3, f"ogrenci-bas.svg 3 yol beklenir, {len(yollar)} bulundu"

    tum_noktalar: list[tuple[float, float]] = []
    for d in yollar:
        komutlar: list[str] = re.findall(r"[A-Za-z]", d)
        assert set(komutlar).issubset({"M", "C"}), f"Yalnız M ve C komutları beklenir: {set(komutlar)}"
        sayilar: list[float] = [float(v) for v in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", d)]
        assert len(sayilar) % 2 == 0, f"Sayı çiftleri bozuk: {len(sayilar)}"
        tum_noktalar.extend(zip(sayilar[0::2], sayilar[1::2]))

    xs: list[float] = [pt[0] for pt in tum_noktalar]
    ys: list[float] = [pt[1] for pt in tum_noktalar]
    kx0: float = min(xs)
    ky0: float = min(ys)
    kx1: float = max(xs)
    ky1: float = max(ys)

    assert abs(kx0 - (-41.907)) <= 0.01, f"kx0 {kx0} beklenen -41.907"
    assert abs(ky0 - 5.467) <= 0.01, f"ky0 {ky0} beklenen 5.467"
    assert abs(kx1 - 189.831) <= 0.01, f"kx1 {kx1} beklenen 189.831"
    assert abs(ky1 - 322.116) <= 0.01, f"ky1 {ky1} beklenen 322.116"

    BTX: float = 60.0 + BAS_CIZGI / 2.0 - kx0 * BS
    BTY: float = 1378.0 - BAS_CIZGI / 2.0 - ky1 * BS

    return yollar, kx0, ky0, kx1, ky1, BTX, BTY


def ogrenci_basi_svg(yollar: list[str], BTX: float, BTY: float) -> str:
    """Öğrenci başı (<g id="bas">) SVG çıktısı (SPEC §4.3)."""
    sw: float = BAS_CIZGI / BS
    mur: str = R["murekkep"]
    yollar_svg: str = "".join(f'<path id="bas-{i}" d="{d}"/>' for i, d in enumerate(yollar))
    return (
        f'<g id="bas" transform="translate({BTX:.2f} {BTY:.2f}) scale({BS:.2f})" fill="none" '
        f'stroke="{mur}" stroke-width="{sw:.4f}" stroke-linecap="round" stroke-linejoin="round">'
        f'{yollar_svg}</g>'
    )


def uc_ve_sac_denetimi(yol0: str, BTX: float, BTY: float) -> float:
    """Kuyruk ucunun öğrenci saçına değmediğini doğrular (SPEC §4.4)."""
    ux, uy = UC
    kyu: float = (uy - BTY) / BS
    sayilar: list[float] = [float(v) for v in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", yol0)]
    ciftler: list[tuple[float, float]] = list(zip(sayilar[0::2], sayilar[1::2]))
    cands: list[float] = [x for x, y in ciftler if abs(y - kyu) <= 12.0]
    assert len(cands) > 0, "kyu civarında saç noktası bulunamadı"
    max_kx: float = max(cands)
    sac_sag: float = BTX + max_kx * BS
    assert ux - sac_sag >= 16.0, f"ux - sac_sag = {ux - sac_sag:.2f} < 16"
    return sac_sag


def balon_yolu(x: int, y: int, w: int, h: int, ux: int, uy: int) -> str:
    """Sol alt kenarında kuyruğu olan el balonu yolu (SPEC §4.4)."""
    r: int = BL_R
    b1: int = y + h - r - 2
    b0: int = b1 - 58
    return (
        f"M{x + r} {y + 3} L{x + w - r} {y - 1} Q{x + w + 4} {y} {x + w + 2} {y + r} "
        f"L{x + w - 2} {y + h - r} Q{x + w} {y + h + 3} {x + w - r} {y + h + 1} "
        f"L{x + r} {y + h + 3} Q{x - 2} {y + h} {x} {y + h - r} "
        f"L{x} {b1} L{ux} {uy} L{x + 2} {b0} L{x - 1} {y + r} "
        f"Q{x + 1} {y + 1} {x + r} {y + 3} Z"
    )


def balon_svg() -> tuple[str, str]:
    """Konuşma balonu ve yazısı SVG çıktısı (SPEC §4.4)."""
    d: str = balon_yolu(BL_X, BL_Y, BL_W, BL_H, UC[0], UC[1])
    mur: str = R["murekkep"]
    balon_g: str = (
        f'<g id="balon" fill="none" stroke="{mur}" stroke-width="{BL_CIZGI}" '
        f'stroke-linecap="round" stroke-linejoin="round">'
        f'<path id="balon-yol" d="{d}"/></g>'
    )
    orta_x: float = BL_X + BL_W / 2.0
    taban_balon: float = BL_Y + BL_H / 2.0 + 0.28 * BL_YAZI
    balon_yazi: str = (
        f'<text id="balon-yazi" x="{orta_x:.0f}" y="{taban_balon:.2f}" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="{BL_YAZI}" fill="{mur}" '
        f'xml:space="preserve">{BALON_METIN}</text>'
    )
    return balon_g, balon_yazi


def soru_svg() -> str:
    """Soru işareti (<g id="soru">) SVG çıktısı (SPEC §4.5)."""
    qm_paths: list[str] = Y.tabler("question-mark", AD / "cizim")
    assert len(qm_paths) == 2, f"qm_paths uzunluğu {len(qm_paths)} != 2"
    assert qm_paths[0].startswith("M8 8a3.5"), f"qm_paths[0] beklenmeyen: {qm_paths[0][:20]}"
    assert qm_paths[1].startswith("M12 19l0"), f"qm_paths[1] beklenmeyen: {qm_paths[1][:20]}"

    sw: float = 26.0 / Q
    vur: str = R["vurgu"]
    soru_paths_svg: str = "".join(f'<path d="{d}"/>' for d in qm_paths)
    return (
        f'<g id="soru" transform="translate({QX} {QY}) scale({Q})" fill="none" '
        f'stroke="{vur}" stroke-width="{sw:.4f}" stroke-linecap="round" stroke-linejoin="round">'
        f'{soru_paths_svg}</g>'
    )


def blok_kutulari(
    S: int,
    g1: float,
    g2: float,
    T1: float,
    T2: float,
    kx0: float,
    ky0: float,
    kx1: float,
    ky1: float,
    BTX: float,
    BTY: float,
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

    bas_y: float = T1 - 0.86 * S - 6.0
    bas_alt: float = T2 + 0.10 * S + 6.0
    b_baslik: dict[str, float] = {
        "ad": "baslik",
        "x": 60.0,
        "y": bas_y,
        "w": max(g1, g2) + 6.0,
        "h": bas_alt - bas_y,
    }

    bas_x0: float = BTX + kx0 * BS - BAS_CIZGI / 2.0
    bas_x1: float = BTX + kx1 * BS + BAS_CIZGI / 2.0
    bas_y0: float = BTY + ky0 * BS - BAS_CIZGI / 2.0
    bas_y1: float = BTY + ky1 * BS + BAS_CIZGI / 2.0
    b_bas: dict[str, float] = {
        "ad": "bas",
        "x": bas_x0,
        "y": bas_y0,
        "w": bas_x1 - bas_x0,
        "h": bas_y1 - bas_y0,
    }

    b_balon: dict[str, float] = {
        "ad": "balon",
        "x": float(BL_X - 4),
        "y": float(BL_Y - 3),
        "w": float(BL_W + 10),
        "h": float(BL_H + 8),
    }

    b1: int = BL_Y + BL_H - BL_R - 2
    b0: int = b1 - 58
    ux, uy = UC
    kx_pts: list[float] = [float(BL_X), float(ux)]
    ky_pts: list[float] = [float(b0), float(b1), float(uy)]
    kuy_x0: float = min(kx_pts) - 2.0
    kuy_x1: float = max(kx_pts) + 2.0
    kuy_y0: float = min(ky_pts) - 2.0
    kuy_y1: float = max(ky_pts) + 2.0
    b_kuyruk: dict[str, float] = {
        "ad": "kuyruk",
        "x": kuy_x0,
        "y": kuy_y0,
        "w": kuy_x1 - kuy_x0,
        "h": kuy_y1 - kuy_y0,
    }

    w_by: float = Y.genislik("Fredoka", 700, BALON_METIN, BL_YAZI)
    taban_balon: float = BL_Y + BL_H / 2.0 + 0.28 * BL_YAZI
    b_balon_yazi: dict[str, float] = {
        "ad": "balon-yazi",
        "x": 737.0 - w_by / 2.0,
        "y": taban_balon - 0.75 * BL_YAZI,
        "w": w_by,
        "h": 1.0 * BL_YAZI,
    }

    soru_x0: float = 8.0 * Q + QX - 13.0
    soru_x1: float = 16.0 * Q + QX + 13.0
    soru_y0: float = 5.0 * Q + QY - 13.0
    soru_y1: float = 19.0 * Q + QY + 13.0
    b_soru: dict[str, float] = {
        "ad": "soru",
        "x": soru_x0,
        "y": soru_y0,
        "w": soru_x1 - soru_x0,
        "h": soru_y1 - soru_y0,
    }

    return [b_kanal, b_kunye, b_baslik, b_bas, b_balon, b_kuyruk, b_balon_yazi, b_soru]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx: float = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy: float = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], S: int, html: str, sac_sag: float) -> None:
    """SPEC.md §6 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict: dict[str, dict[str, float]] = {b["ad"]: b for b in bloklar}

    # 1 & 2. Sınırlar (SPEC §6.2)
    for b in bloklar:
        ad: str = b["ad"]
        bx: float = b["x"]
        by: float = b["y"]
        bw: float = b["w"]
        bh: float = b["h"]
        assert bx >= 60.0 - 1e-4, f"{ad} sol {bx} < 60"
        assert bx + bw <= 960.0 + 1e-4, f"{ad} sag {bx + bw} > 960"
        if ad == "kanal":
            assert by >= 280.0 - 1e-4 and by + bh <= 350.0 + 1e-4, f"kanal y out: {by}"
        elif ad == "kunye":
            assert by >= 360.0 - 1e-4 and by + bh <= 450.0 + 1e-4, f"kunye y out: {by}"
        else:
            assert by >= 460.0 - 1e-4 and by + bh <= 1380.0 + 1e-4, f"{ad} y out: {by}"

    assert b_dict["balon"]["x"] + b_dict["balon"]["w"] <= 958.0 + 1e-4, "balon sağ > 958"

    # 3. Kesişim 0 (SPEC §6.3)
    yedi_blok: list[str] = ["kanal", "kunye", "baslik", "bas", "balon", "kuyruk", "soru"]
    for i in range(len(yedi_blok)):
        for j in range(i + 1, len(yedi_blok)):
            a: str = yedi_blok[i]
            c: str = yedi_blok[j]
            if (a, c) == ("balon", "kuyruk") or (a, c) == ("kuyruk", "balon"):
                continue
            k: float = kesisim(b_dict[a], b_dict[c])
            assert k == 0.0, f"Kesisim {a} - {c}: {k}"

    by_box: dict[str, float] = b_dict["balon-yazi"]
    assert by_box["x"] >= BL_X + 24.0 - 1e-4, "balon-yazi sol dışta"
    assert by_box["x"] + by_box["w"] <= BL_X + BL_W - 24.0 + 1e-4, "balon-yazi sağ dışta"
    assert by_box["y"] >= BL_Y + 16.0 - 1e-4, "balon-yazi üst dışta"
    assert by_box["y"] + by_box["h"] <= BL_Y + BL_H - 16.0 + 1e-4, "balon-yazi alt dışta"

    baslik_alt: float = b_dict["baslik"]["y"] + b_dict["baslik"]["h"]
    assert b_dict["balon"]["y"] - baslik_alt >= 40.0 - 1e-4, "balon.y - baslik.alt < 40"
    assert b_dict["bas"]["y"] - baslik_alt >= 40.0 - 1e-4, "bas.y - baslik.alt < 40"
    assert b_dict["soru"]["y"] - (b_dict["balon"]["y"] + b_dict["balon"]["h"]) >= 20.0 - 1e-4, "soru.y - balon.alt < 20"
    assert b_dict["kuyruk"]["x"] - (b_dict["bas"]["x"] + b_dict["bas"]["w"]) >= 8.0 - 1e-4, "kuyruk.x - bas.sağ < 8"
    assert b_dict["soru"]["x"] - (b_dict["bas"]["x"] + b_dict["bas"]["w"]) >= 32.0 - 1e-4, "soru.x - bas.sağ < 32"
    assert UC[0] - sac_sag >= 16.0 - 1e-4, "ux - sac_sag < 16"

    # 4. Yazı boyu (SPEC §6.4)
    assert S >= 64, f"Başlık boyutu {S} < 64"
    assert BL_YAZI >= 64, f"Balon boyutu {BL_YAZI} < 64"

    baslik_satirlari: list[str] = [BASLIK_SATIR1, BASLIK_SATIR2]
    assert len(baslik_satirlari) == 2, "Başlık satır sayısı != 2"
    assert len(" ".join(baslik_satirlari).split()) == 4, "Başlık sözcük sayısı != 4"

    for s_metin in [BASLIK_SATIR1, BASLIK_SATIR2, BALON_METIN]:
        assert len(s_metin) <= 24, f"Satır uzunluğu > 24: {s_metin}"
    assert "\u0130" in BASLIK_SATIR2, "HANGİ içinde U+0130 yok"

    # 5. Görünen metin taraması (SPEC §6.5)
    gorunen_metinler: list[str] = re.findall(r">([^<]+)</text>", html)
    for gm in gorunen_metinler:
        gm_lower: str = gm.lower()
        assert "izle" not in gm_lower, f"Görünen metinde 'izle' var: {gm}"
        assert "qr" not in gm_lower, f"Görünen metinde 'qr' var: {gm}"
        for ch in gm:
            assert ord(ch) <= 0x2FFF, f"Görünen metinde emoji var: {ch}"

    # 6. Bütün HTML kontrolleri (SPEC §6.6)
    html_lower: str = html.lower()
    for yk in ("math.random", "date.now", "new date", "opacity:0"):
        assert yk not in html_lower, f"Yasak kod bulundu: {yk}"
    assert "#root.tema-acik" not in html, "#root.tema-acik geçmemeli"
    assert "<img" not in html_lower, "<img geçmemeli"

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


def uret() -> tuple[str, int, float, list[dict[str, float]]]:
    """Sahne HTML'i, font boyutu ve bloklarını üretir."""
    S, g1, g2, T1, T2 = hesapla_s()
    yollar, kx0, ky0, kx1, ky1, BTX, BTY = ogrenci_basi_oku()
    sac_sag: float = uc_ve_sac_denetimi(yollar[0], BTX, BTY)

    kunye: str = Y.kunye_svg()
    baslik: str = baslik_svg(S, T1, T2)
    bas: str = ogrenci_basi_svg(yollar, BTX, BTY)
    balon, balon_yazi = balon_svg()
    soru: str = soru_svg()

    bloklar: list[dict[str, float]] = blok_kutulari(S, g1, g2, T1, T2, kx0, ky0, kx1, ky1, BTX, BTY)

    sure_val: float = float(Z["sure"])
    html: str = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{sure_val}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{baslik}
{bas}
{balon}
{balon_yazi}
{soru}
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var tl = gsap.timeline({{ paused: true }});
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, 0);
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, {sure_val});
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""

    kurallari_dogrula(bloklar, S, html, sac_sag)
    return html, S, sac_sag, bloklar


if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")

    html, S, sac_sag, bloklar = uret()
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
    print(f"S={S} BS={BS:.2f} Q={Q} uc={UC[0]},{UC[1]} sac_sag={sac_sag:.1f}")

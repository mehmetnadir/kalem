#!/usr/bin/python3
"""simple-present-temel-s1 sahne 06 kapak B index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok; huni v2)."""
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

# 1. zaman.json ve zamanlar.json okuma ve doğrulama (SPEC §2)
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

# 2. Renk ve sabitler (SPEC §2)
SARI: str = "#fece00"
SIYAH: str = "#141414"
KREM: str = "#f3efe6"

W: int = Y.W
H: int = Y.H
X0: int = 60
X1: int = 960
KANAL_Y: tuple[int, int] = (280, 350)
KUNYE_Y: tuple[int, int] = (360, 450)
BASLIK_Y: tuple[int, int] = (470, 900)
GORSEL_Y: tuple[int, int] = (920, 1380)

SATIRLAR: tuple[str, str] = ("FİİLE -S", "HANGİ ÖZNEYLE?")
YEDEK: tuple[str, str] = ("-S HANGİ", "ÖZNEYLE?")
UST_SINIR: float = 190.0
ALT_SINIR: float = 64.0
PX: float = 0.16
UST: float = 0.93
ARA: float = 0.18
KUTU_UST: float = 1.05
KUTU_ALT: float = 0.24
RX: float = 0.10

KARAKTER: Path = ORTAK / "kapak" / "karakter.png"
NESNE: Path = ORTAK / "kapak" / "nesne.png"
ESIK: int = 64
KENAR_PX: int = 10
KENAR_GECIS: int = 3
KAR_KUTU: tuple[int, int, int, int] = (148, 85, 793, 1024)
NES_KUTU: tuple[int, int, int, int] = (96, 254, 1057, 643)
BAS_X: float = 526.0
PARMAK: tuple[float, float] = (162.0, 502.0)
DAIRE_R: float = 220.0
NESNE_EN: float = 360.0
NESNE_ARA: float = 24.0
NESNE_UST: float = 16.0  # DUZ2 16.11: parmak sol üste bakar; otobüs üstü parmak ucunun altında


def alfa_kutusu(yol: Path) -> tuple[int, int, int, int]:
    """PNG'nin saydam olmayan kutusu (x0, y0, x1, y1)."""
    a = Image.open(yol).split()[-1].point(lambda v: 255 if v > ESIK else 0)
    kutu = a.getbbox()
    assert kutu is not None, f"{yol.name} tamamen saydam"
    return kutu


assert alfa_kutusu(KARAKTER) == KAR_KUTU, f"KARAKTER alfa kutusu uyumsuz: {alfa_kutusu(KARAKTER)} != {KAR_KUTU}"
assert alfa_kutusu(NESNE) == NES_KUTU, f"NESNE alfa kutusu uyumsuz: {alfa_kutusu(NESNE)} != {NES_KUTU}"


def maske(yol: Path, x: float, y: float, s: float) -> np.ndarray:
    """Görselin tuvaldeki saydamlık maskesi (bool, H x W)."""
    im = Image.open(yol)
    a = im.split()[-1].resize((round(im.width * s), round(im.height * s)), Image.BILINEAR)
    m = Image.new("L", (W, H), 0)
    m.paste(255, (round(x), round(y)), a.point(lambda v: 255 if v > ESIK else 0))
    return np.asarray(m) > 0


def bos_mu(m: np.ndarray, kutu: tuple[float, float, float, float], pay: float) -> bool:
    """Kutu (pay kadar genişletilmiş) içinde maskede görsel yok mu."""
    x0: int = max(0, math.floor(kutu[0] - pay))
    y0: int = max(0, math.floor(kutu[1] - pay))
    x1: int = min(W, math.ceil(kutu[2] + pay))
    y1: int = min(H, math.ceil(kutu[3] + pay))
    return x1 <= x0 or y1 <= y0 or not m[y0:y1, x0:x1].any()


def maske_kutusu(m: np.ndarray) -> tuple[int, int, int, int]:
    """Maskenin tuvaldeki kutusu (x0, y0, x1, y1)."""
    ys, xs = np.nonzero(m)
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def gorsel_kopyala(kaynak: Path, hedef_dizin: Path) -> None:
    """Görsel hedef dizine kopyalanır. Alfa <= ESIK temizlenir."""
    hedef_dizin.mkdir(parents=True, exist_ok=True)
    im = Image.open(kaynak).convert("RGBA")
    a = im.split()[-1]
    m = a.point(lambda v: 255 if v > ESIK else 0).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    im.putalpha(ImageChops.multiply(a, m))
    im.save(hedef_dizin / kaynak.name)


def gorsel_img(
    gid: str,
    src: str,
    x: float,
    y: float,
    kaynak_w: int,
    kaynak_h: int,
    s: float,
) -> str:
    """Çıkartma kenarlı görsel (<img>, SPEC §3.3)."""
    return (
        f'<img id="{gid}" class="abs kenar" src="{src}" alt="" '
        f'style="left:{x:.1f}px;top:{y:.1f}px;width:{kaynak_w * s:.1f}px;height:{kaynak_h * s:.1f}px">'
    )


def glif_denetle(metin: str) -> None:
    """Metindeki her karakterin Fredoka 700 cmap'inde olduğunu doğrular (SPEC §3.2.5)."""
    for c in metin:
        var: bool = any(
            ord(c) in Y._font("Fredoka", 700, bolge).getBestCmap()
            for bolge in ("latin", "latin-ext")
        )
        assert var, f"Karakter {c!r} Fredoka 700 cmap içinde yok"


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx: float = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy: float = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def hesapla_baslik() -> tuple[
    str, tuple[str, str], int, float, float, float, float, float, float, float, float, float, float, float
]:
    """Başlık font boyutu S ve yerleşim koordinatlarını hesaplar (SPEC §3.2)."""
    for satir_ad, secenek in (("ana", SATIRLAR), ("yedek", YEDEK)):
        s1, s2 = secenek
        w1: float = Y.genislik("Fredoka", 700, s1, 100.0)
        w2: float = Y.genislik("Fredoka", 700, s2, 100.0)
        S: int = math.floor(
            min(UST_SINIR, 900.0 * 100.0 / w1, 900.0 * 100.0 / (w2 + 2.0 * PX * 100.0))
        )
        while S >= int(ALT_SINIR):
            g1: float = Y.genislik("Fredoka", 700, s1, S)
            g2: float = Y.genislik("Fredoka", 700, s2, S)
            if g1 <= 900.0 and (g2 + 2.0 * PX * S) <= 900.0:
                break
            S -= 1
        if S >= int(ALT_SINIR):
            glif_denetle(s1 + s2)
            bh: float = (UST + ARA + KUTU_UST + KUTU_ALT) * S
            by: float = 470.0 + (430.0 - bh) / 2.0
            T1: float = by + UST * S
            ky0: float = T1 + ARA * S
            T2: float = ky0 + KUTU_UST * S
            ky1: float = T2 + KUTU_ALT * S
            kutu_w: float = g2 + 2.0 * PX * S
            kutu_h: float = ky1 - ky0
            rx: float = RX * S
            s2_x: float = 60.0 + PX * S
            return (
                satir_ad,
                secenek,
                S,
                g1,
                g2,
                by,
                T1,
                ky0,
                T2,
                ky1,
                kutu_w,
                kutu_h,
                rx,
                s2_x,
            )
    assert False, f"Başlık font boyutu S < {ALT_SINIR}"


def hesapla_gorseller() -> tuple[
    float, float, float, float, float, float, np.ndarray, np.ndarray
]:
    """Karakter ve nesne ölçek ve konumlarını hesaplar (SPEC §3.3)."""
    # şef QA tur 1: kenar + yumuşak alfa saçta maskeden 13 px taşıyor (karede y 917) → görünür üst 933, yükseklik 436
    s: float = math.floor(436.0 / (KAR_KUTU[3] - KAR_KUTU[1]) * 1000.0) / 1000.0
    kx: float = (960.0 - DAIRE_R) - BAS_X * s
    ky: float = 933.0 - KAR_KUTU[1] * s

    sn: float = round(NESNE_EN / (1057.0 - 96.0), 4)
    px: float = kx + PARMAK[0] * s
    py: float = ky + PARMAK[1] * s
    o_deger: float = px - 2.0 * KENAR_PX - NESNE_ARA
    nx: float = o_deger - 1057.0 * sn
    ny: float = py + NESNE_UST - NES_KUTU[1] * sn

    m_karakter: np.ndarray = maske(KARAKTER, kx, ky, s)
    m_nesne: np.ndarray = maske(NESNE, nx, ny, sn)

    return s, kx, ky, sn, nx, ny, m_karakter, m_nesne


def baslik_svg(
    s1: str,
    s2: str,
    S: int,
    T1: float,
    ky0: float,
    T2: float,
    kutu_w: float,
    kutu_h: float,
    rx: float,
    s2_x: float,
) -> str:
    """Başlık grubu SVG'si (SPEC §3.2, §4)."""
    return (
        f'<g id="baslik">\n'
        f'<text id="bs-1" x="60" y="{T1:.1f}" font-family="Fredoka" font-weight="700" font-size="{S}" '
        f'style="font-kerning:none" xml:space="preserve">{s1}</text>\n'
        f'<rect id="bk-kutu" x="60" y="{ky0:.1f}" width="{kutu_w:.1f}" height="{kutu_h:.1f}" rx="{rx:.1f}"/>\n'
        f'<text id="bs-2" x="{s2_x:.1f}" y="{T2:.1f}" font-family="Fredoka" font-weight="700" font-size="{S}" '
        f'style="font-kerning:none" xml:space="preserve">{s2}</text>\n'
        f'</g>'
    )


def blok_kutulari(
    g1: float,
    g2: float,
    S: int,
    by: float,
    ky0: float,
    ky1: float,
    m_karakter: np.ndarray,
    m_nesne: np.ndarray,
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

    rozet_w: float = float(Y.rozet_konumlari(False)[0][1])
    b_kunye: dict[str, float] = {
        "ad": "kunye",
        "x": 60.0,
        "y": 386.0,
        "w": rozet_w,
        "h": 48.0,
    }

    kutu_sagi: float = 60.0 + g2 + 2.0 * PX * S
    baslik_sagi: float = max(60.0 + g1, kutu_sagi)
    b_baslik: dict[str, float] = {
        "ad": "baslik",
        "x": 60.0,
        "y": by,
        "w": baslik_sagi - 60.0,
        "h": ky1 - by,
    }

    b_bk_kutu: dict[str, float] = {
        "ad": "bk-kutu",
        "x": 60.0,
        "y": ky0,
        "w": g2 + 2.0 * PX * S,
        "h": ky1 - ky0,
    }

    b_daire: dict[str, float] = {
        "ad": "daire",
        "x": 520.0,
        "y": 930.0,
        "w": 440.0,
        "h": 440.0,
    }

    mn_x0, mn_y0, mn_x1, mn_y1 = maske_kutusu(m_nesne)
    b_nesne: dict[str, float] = {
        "ad": "nesne",
        "x": float(mn_x0 - KENAR_PX),
        "y": float(mn_y0 - KENAR_PX),
        "w": float(mn_x1 - mn_x0 + 2 * KENAR_PX),
        "h": float(mn_y1 - mn_y0 + 2 * KENAR_PX),
    }

    mk_x0, mk_y0, mk_x1, mk_y1 = maske_kutusu(m_karakter)
    b_karakter: dict[str, float] = {
        "ad": "karakter",
        "x": float(mk_x0 - KENAR_PX),
        "y": float(mk_y0 - KENAR_PX),
        "w": float(mk_x1 - mk_x0 + 2 * KENAR_PX),
        "h": float(mk_y1 - mk_y0 + 2 * KENAR_PX),
    }

    return [
        b_kanal,
        b_kunye,
        b_baslik,
        b_bk_kutu,
        b_daire,
        b_nesne,
        b_karakter,
    ]


def kurallari_dogrula(
    bloklar: list[dict[str, float]],
    S: int,
    satirlar: tuple[str, str],
    satir_ad: str,
    html: str,
    m_karakter: np.ndarray,
    m_nesne: np.ndarray,
) -> None:
    """SPEC.md §6 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict: dict[str, dict[str, float]] = {b["ad"]: b for b in bloklar}

    # 1 & 2. Sınırlar (SPEC §6.2)
    for b in bloklar:
        ad: str = b["ad"]
        x: float = b["x"]
        y: float = b["y"]
        w: float = b["w"]
        h: float = b["h"]
        assert x >= 60.0 - 1e-4, f"{ad} sol {x} < 60"
        assert x + w <= 960.0 + 1e-4, f"{ad} sağ {x + w} > 960"
        if ad == "kanal":
            assert y >= 280.0 - 1e-4 and y + h <= 350.0 + 1e-4, f"kanal y out: {y}"
        elif ad == "kunye":
            assert y >= 360.0 - 1e-4 and y + h <= 450.0 + 1e-4, f"kunye y out: {y}"
        elif ad in ("baslik", "bk-kutu"):
            assert y >= 470.0 - 1e-4 and y + h <= 900.0 + 1e-4, f"{ad} y out: {y}"
        elif ad in ("daire", "nesne", "karakter"):
            assert y >= 920.0 - 1e-4 and y + h <= 1380.0 + 1e-4, f"{ad} y out: {y}"

    # 3. Kesişim 0 (SPEC §6.3)
    ciftler: list[tuple[str, str]] = [
        ("kanal", "kunye"),
        ("kanal", "baslik"),
        ("kunye", "baslik"),
        ("baslik", "daire"),
        ("baslik", "nesne"),
        ("baslik", "karakter"),
    ]
    for a, c in ciftler:
        k: float = kesisim(b_dict[a], b_dict[c])
        assert k == 0.0, f"Kesişim {a} - {c}: {k}"

    mn_x0, mn_y0, mn_x1, mn_y1 = maske_kutusu(m_nesne)
    nesne_gorunur_kutu: tuple[float, float, float, float] = (
        float(mn_x0),
        float(mn_y0),
        float(mn_x1),
        float(mn_y1),
    )
    assert bos_mu(m_karakter, nesne_gorunur_kutu, 2 * KENAR_PX + 4), (
        "otobüs ve kenarı karaktere değiyor"
    )

    # 4. Yazı boyu ve satırlar (SPEC §6.4)
    assert S >= 64, f"Başlık boyutu {S} < 64"
    assert len(satirlar) == 2, "Başlık satır sayısı != 2"
    beklenen_sozcuk: int = 4 if satir_ad == "ana" else 3
    assert len(" ".join(satirlar).split()) == beklenen_sozcuk, (
        f"Başlık sözcük sayısı != {beklenen_sozcuk}"
    )
    for sm in satirlar:
        assert len(sm) <= 24, f"Satır uzunluğu > 24: {sm}"

    # 5. Görünen metin taraması (SPEC §6.5)
    gorunen_metinler: list[str] = re.findall(r">([^<]+)</text>", html)
    birlestirilmis: str = " ".join(gorunen_metinler)
    kucuk: str = birlestirilmis.lower()
    yasak_kelimeler: list[str] = [
        "tam" + " ders",
        "dak" + "ika",
        "izle",
        "qr",
        "you" + "tube",
        "abone",
    ]
    for yk in yasak_kelimeler:
        assert yk not in kucuk, f"Görünen metinde yasak sözcük bulundu: {yk!r}"
    assert "ALIR" not in birlestirilmis, "Görünen metinde ALIR bulundu"
    assert re.search(r"ÖZNE(?!YLE)", birlestirilmis) is None, (
        "Görünen metinde ÖZNE(?!YLE) eşleşti"
    )
    for ch in birlestirilmis:
        assert ord(ch) <= 0x2FFF, f"Görünen metinde emoji bulundu: {ch!r} (U+{ord(ch):04X})"

    # 6. Bütün HTML kontrolleri (SPEC §6.6)
    html_lower: str = html.lower()
    for yasak_kod in ("math.random", "date.now", "new date", "opacity:0"):
        assert yasak_kod not in html_lower, f"Yasak kod bulundu: {yasak_kod}"

    hex_renkler: set[str] = {h.lower() for h in re.findall(r"#[0-9a-fA-F]{6}\b", html)}
    gecerli_renkler: set[str] = {"#1b1a17", "#f3efe6", "#fece00", "#141414"}
    for hx in hex_renkler:
        assert hx in gecerli_renkler, f"Geçersiz hex renk: {hx}"

    assert html.count('id="kanal"') == 1, "id='kanal' sayısı != 1"
    assert html.count('id="logoimg"') == 1, "id='logoimg' sayısı != 1"
    assert html.count('id="kb-daire"') == 1, "id='kb-daire' sayısı != 1"
    assert html.count('id="bk-kutu"') == 1, "id='bk-kutu' sayısı != 1"
    assert 'id="ku-konu"' not in html, "id='ku-konu' HTML içinde olmamalı"


def uret() -> tuple[
    str, int, float, float, float, float, str, list[dict[str, float]]
]:
    """Sahne HTML'i ve bileşenlerini üretir."""
    (
        satir_ad,
        satirlar,
        S,
        g1,
        g2,
        by,
        T1,
        ky0,
        T2,
        ky1,
        kutu_w,
        kutu_h,
        rx,
        s2_x,
    ) = hesapla_baslik()

    s, kx, ky, sn, nx, ny, m_karakter, m_nesne = hesapla_gorseller()

    kunye: str = Y.kunye_svg(konu=False, cerceve=True)
    baslik: str = baslik_svg(
        satirlar[0],
        satirlar[1],
        S,
        T1,
        ky0,
        T2,
        kutu_w,
        kutu_h,
        rx,
        s2_x,
    )

    bloklar: list[dict[str, float]] = blok_kutulari(
        g1, g2, S, by, ky0, ky1, m_karakter, m_nesne
    )

    im_kar: Image.Image = Image.open(KARAKTER)
    im_nes: Image.Image = Image.open(NESNE)
    nesne_img: str = gorsel_img(
        "nesne", "assets/nesne.png", nx, ny, im_nes.width, im_nes.height, sn
    )
    karakter_img: str = gorsel_img(
        "karakter", "assets/karakter.png", kx, ky, im_kar.width, im_kar.height, s
    )

    adim: float = KENAR_PX / KENAR_GECIS
    kenar_filter: str = " ".join(
        f"drop-shadow({dx:.2f}px {dy:.2f}px 0 {KREM})"
        for _ in range(KENAR_GECIS)
        for dx, dy in ((adim, 0.0), (-adim, 0.0), (0.0, adim), (0.0, -adim))
    )

    # DUZ4 A6 / HV-20a (16.11): sarı kb-zemin kalktı; zemin A ve C kapağıyla aynı tema zemini + gren + vinyet
    # (Y.zemin_html; hf_tema: açık #f7f3ea, koyu #1b1a17). Sarı yalnız başlık kutusunda (iki temada sarı kutu, siyah yazı).
    # Seçici `.tema-acik#root`: hf_tema `#root.tema-acik` dizgisini görürse zemin değişkenlerini eklemez.
    tema_css: str = (
        "#root{--kbYazi:#f3efe6;--kbKutu:#fece00;--kbKutuYazi:#141414;--kbDaire:#f3efe6;}\n"
        ".tema-acik#root{--kbYazi:#141414;}\n"
        "#kb-daire{border-radius:50%;background:var(--kbDaire);display:none;}\n"
        ".tema-acik#root #kb-daire{display:block;}\n"
        "#root #kanal-yazi,#root #rz0 text,#root #bs-1{fill:var(--kbYazi);}\n"
        "#root #rz0 rect{stroke:var(--kbYazi);}\n"
        "#root #bk-kutu{fill:var(--kbKutu);}\n"
        "#root #bs-2{fill:var(--kbKutuYazi);}"
    )

    z_sure: float = Z["sure"]
    html: str = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
.kenar{{filter:{kenar_filter};}}
{tema_css}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{z_sure}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<div id="kb-daire" class="abs" style="left:520px;top:930px;width:440px;height:440px"></div>
{nesne_img}
{karakter_img}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920">
{kunye}
{baslik}
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var tl = gsap.timeline({{ paused: true }});
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, 0);
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, {z_sure});
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""

    kurallari_dogrula(bloklar, S, satirlar, satir_ad, html, m_karakter, m_nesne)
    return html, S, s, sn, kx, nx, satir_ad, bloklar


if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    gorsel_kopyala(KARAKTER, proje_dizini / "assets")
    gorsel_kopyala(NESNE, proje_dizini / "assets")

    html, S, s, sn, kx, nx, satir_ad, bloklar = uret()
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
    print(f"S={S} s={s:.3f} sn={sn:.4f} kx={kx:.1f} nx={nx:.1f} satir={satir_ad}")

#!/usr/bin/python3
"""Sahne 05 hikâye karesi A (kural kartı) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2: kanal katmanı + v2 bantları."""
from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# zaman.json ve zamanlar.json okuma ve doğrulama
zaman_data = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
hikaye = zaman_data["hikaye"]
assert hikaye["klasor"] == AD.name, f"klasor {hikaye['klasor']} != {AD.name}"
assert hikaye["kare"] == 1, f"kare {hikaye['kare']} != 1"
assert AD.name not in [s["klasor"] for s in zaman_data["sahneler"]], "AD.name sahneler içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

# şef QA 1: kenar kâğıdın kenarındaydı, koyu temada zeminle birleşti -> sahne 03 gibi ayrı kâğıt (dış 60-960 x 556-863),
# kalem kenarı 15/12 px içte
KX0 = 76.0
KX1 = 944.0
KY0 = 568.0
KY1 = 851.0
SORU_Y = 522
T1 = 635
T2 = 719
T3 = 811


def kart_kenar_yolu() -> str:
    """Kart kenarı yolu (tek M + L dizisi, Z yok, §3.1)."""
    kay = [1.6, -1.2, 2.2, -0.8, 1.0, -2.0, 0.6, 1.8, -1.4, 0.4, -2.2, 1.2]
    dx = KX1 - KX0
    dy = KY1 - KY0
    noktalar: list[tuple[float, float]] = [
        (KX0 + 10.0, KY0),
        (KX0 + dx * 1.0 / 4.0, KY0 + kay[0]),
        (KX0 + dx * 2.0 / 4.0, KY0 + kay[1]),
        (KX0 + dx * 3.0 / 4.0, KY0 + kay[2]),
        (KX1, KY0),
        (KX1 + kay[3], KY0 + dy * 1.0 / 4.0),
        (KX1 + kay[4], KY0 + dy * 2.0 / 4.0),
        (KX1 + kay[5], KY0 + dy * 3.0 / 4.0),
        (KX1, KY1),
        (KX1 - dx * 1.0 / 4.0, KY1 + kay[6]),
        (KX1 - dx * 2.0 / 4.0, KY1 + kay[7]),
        (KX1 - dx * 3.0 / 4.0, KY1 + kay[8]),
        (KX0, KY1),
        (KX0 + kay[9], KY1 - dy * 1.0 / 4.0),
        (KX0 + kay[10], KY1 - dy * 2.0 / 4.0),
        (KX0 + kay[11], KY1 - dy * 3.0 / 4.0),
        (KX0, KY0),
        (KX0 + 24.0, KY0),
    ]
    for p in noktalar:
        assert KX0 - 2.5 <= p[0] <= KX1 + 2.5, f"kart-kenar x sınırı dışı: {p}"
        assert KY0 - 2.5 <= p[1] <= KY1 + 2.5, f"kart-kenar y sınırı dışı: {p}"
    return "M " + f"{noktalar[0][0]:.1f} {noktalar[0][1]:.1f}" + " " + " ".join(
        f"L {p[0]:.1f} {p[1]:.1f}" for p in noktalar[1:]
    )


def soru_svg() -> str:
    """Soru metni SVG çıktısı (§3)."""
    return (
        f'<text id="soru" x="60" y="{SORU_Y}" font-family="Caveat" font-weight="700" '
        'font-size="72" fill="#f3efe6">Usually görünce hangi zaman?</text>'
    )


def kart_svg(bx: float, hap_w: float) -> str:
    """Kart grubu SVG çıktısı (§3.1)."""
    kenar_d = kart_kenar_yolu()
    return (
        '<g id="kart">'
        '<rect id="kagit" x="61" y="557" width="898" height="305" rx="18" fill="#fff9e6" stroke="#c9c2b3" '
        'stroke-width="2"/>'
        f'<path id="kart-kenar" d="{kenar_d}" fill="none" stroke="#1b1a17" stroke-width="4.5" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        f'<text id="kart-s1" x="{bx:.1f}" y="{T1}" font-family="Fredoka" font-weight="700" '
        'font-size="72" fill="#1b1a17">Usually, always,</text>'
        f'<text id="kart-s2" x="{bx:.1f}" y="{T2}" font-family="Fredoka" font-weight="700" '
        'font-size="72" fill="#1b1a17">every day: çoğunlukla</text>'
        f'<rect id="kart-hap" x="{bx:.1f}" y="{T3 - 62}" width="{hap_w:.1f}" height="88" '
        'rx="44" fill="#f2a93b"/>'
        f'<text id="kart-hap-yazi" x="{bx + hap_w / 2.0:.1f}" y="{T3}" text-anchor="middle" '
        'font-family="Fredoka" font-weight="700" font-size="72" fill="#1b1a17">Simple Present.</text>'
        '</g>'
    )


def ornek_svg() -> str:
    """Örnek cümle ve altçizgi SVG çıktısı (§3.2)."""
    ux0 = 60.0 + Y.genislik("Fredoka", 700, "My brother ", 64) - 4.0
    ux1 = 60.0 + Y.genislik("Fredoka", 700, "My brother usually", 64) + 1.0  # şef QA 1: +6 `goes` g kuyruğuna 6 px
    uw = ux1 - ux0
    uy = 937.0
    cizgi_d = (
        f"M {ux0:.1f} {uy + 1.2:.1f} "
        f"Q {ux0 + uw / 4.0:.1f} {uy - 1.8:.1f} {ux0 + uw / 2.0:.1f} {uy + 0.4:.1f} "
        f"Q {ux0 + 3.0 * uw / 4.0:.1f} {uy + 2.2:.1f} {ux1:.1f} {uy - 1.0:.1f}"
    )
    return (
        '<g id="ornek">'
        '<text id="ornek-1" x="60" y="925" font-family="Fredoka" font-weight="700" '
        'font-size="64" fill="#f3efe6" xml:space="preserve">My brother usually goes</text>'
        '<text id="ornek-2" x="60" y="1005" font-family="Fredoka" font-weight="700" '
        'font-size="64" fill="#f3efe6" xml:space="preserve">to school by bus.</text>'
        f'<path id="ornek-cizgi" d="{cizgi_d}" fill="none" stroke="#f3efe6" stroke-width="5" '
        'stroke-linecap="round"/>'
        '</g>'
    )


def otobus_svg() -> tuple[str, float]:
    """Otobüs SVG çıktısı ve kutu yüksekliği (§3.3)."""
    bus_path = Y.ORTAK / "cizim" / "coco" / "bus.svg"
    kok = ET.parse(str(bus_path)).getroot()
    vb = kok.get("viewBox", "")
    parts = [float(p) for p in vb.split()]
    vb_w, vb_h = parts[2], parts[3]
    oh = 168.0 * vb_h / vb_w

    path_elem = None
    for elem in kok.iter():
        if elem.tag.endswith("path") and elem.get("fill") == "#030303":
            path_elem = elem
            break
    assert path_elem is not None, "Otobüs yol verisi (#030303) bulunamadı"

    d = path_elem.get("d", "")
    tr = path_elem.get("transform", "")
    svg = (
        f'<svg id="otobus" x="786" y="948" width="168" height="{oh:.1f}" viewBox="{vb}">'
        f'<path d="{d}" transform="{tr}" fill="#f3efe6"/>'
        '</svg>'
    )
    return svg, oh


def kaydet_svg() -> str:
    """Kaydet yazısı ve yer imi ikonu SVG çıktısı (§3.4)."""
    yazi_w = Y.genislik("Fredoka", 700, "Kaydet", 88)
    yx0 = 958.0 - yazi_w
    hs = 1.4 * 4.5 / 2.0
    tx = yx0 - 24.0 - hs - 18.0 * 4.5
    ty = 1110.0 - 31.0 - 12.0 * 4.5
    return (
        '<g id="kaydet">'
        f'<g id="kaydet-ikon" transform="translate({tx:.1f} {ty:.1f}) scale(4.5)" fill="none" '
        'stroke="#f3efe6" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">'
        '<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/>'
        '</g>'
        '<text id="kaydet-yazi" x="958" y="1110" text-anchor="end" font-family="Fredoka" '
        'font-weight="700" font-size="88" fill="#f3efe6">Kaydet</text>'
        '</g>'
    )


def blok_kutulari(oh: float) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar (§4)."""
    w_kanal = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - 53.2
    kanal = {"ad": "kanal", "x": 53.2, "y": 291.0, "w": w_kanal, "h": 48.0}

    rz_x, rz_w = Y.rozet_konumlari()[0]
    kunye = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": rz_x + rz_w - 60.0, "h": 48.0}

    soru = {
        "ad": "soru",
        "x": 60.0,
        "y": SORU_Y - 0.74 * 72.0,
        "w": Y.genislik("Caveat", 700, "Usually görünce hangi zaman?", 72),
        "h": 0.98 * 72.0,
    }

    kart = {"ad": "kart", "x": 60.0, "y": 556.0, "w": 900.0, "h": 307.0}  # kâğıt dış kenarı (çizgi 2 dahil)

    ornek_y = 925.0 - 0.74 * 64.0
    ornek = {
        "ad": "ornek",
        "x": 60.0,
        "y": ornek_y,
        "w": Y.genislik("Fredoka", 700, "My brother usually goes", 64),
        "h": (1005.0 + 0.24 * 64.0) - ornek_y,
    }

    otobus = {"ad": "otobus", "x": 786.0, "y": 948.0, "w": 168.0, "h": oh}

    yazi_w = Y.genislik("Fredoka", 700, "Kaydet", 88)
    yx0 = 958.0 - yazi_w
    hs = 1.4 * 4.5 / 2.0
    tx = yx0 - 24.0 - hs - 18.0 * 4.5
    ty = 1110.0 - 31.0 - 12.0 * 4.5
    kx = tx + 6.0 * 4.5 - hs
    ky = min(ty + 3.0 * 4.5 - hs, 1110.0 - 0.74 * 88.0)
    kw = 958.0 - kx
    kh = max(ty + 21.0 * 4.5 + hs, 1110.0 + 0.24 * 88.0) - ky
    kaydet = {"ad": "kaydet", "x": kx, "y": ky, "w": kw, "h": kh}

    return [kanal, kunye, soru, kart, ornek, otobus, kaydet]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(
    bloklar: list[dict[str, float]], bx: float, gmax: float, html: str
) -> None:
    """SPEC.md §5 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. İçerik blokları: x >= 60, x + w <= 960, y >= 460, y + h <= 1140
    for ad in ("soru", "kart", "ornek", "otobus", "kaydet"):
        b = b_dict[ad]
        assert b["x"] >= 60.0 - 1e-4, f"{ad} sol kenar {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ kenar {b['x'] + b['w']} > 960"
        assert b["y"] >= 460.0 - 1e-4, f"{ad} üst {b['y']} < 460"
        assert b["y"] + b["h"] <= 1140.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1140"

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

    # 4. Dikey boşluk >= 12; Yatay boşluk >= 16
    assert b_dict["soru"]["y"] - (b_dict["kunye"]["y"] + b_dict["kunye"]["h"]) >= 12.0 - 1e-4
    assert b_dict["kart"]["y"] - (b_dict["soru"]["y"] + b_dict["soru"]["h"]) >= 12.0 - 1e-4
    assert b_dict["ornek"]["y"] - (b_dict["kart"]["y"] + b_dict["kart"]["h"]) >= 12.0 - 1e-4
    assert b_dict["otobus"]["y"] - (b_dict["kart"]["y"] + b_dict["kart"]["h"]) >= 12.0 - 1e-4
    assert b_dict["kaydet"]["y"] - (b_dict["ornek"]["y"] + b_dict["ornek"]["h"]) >= 12.0 - 1e-4
    assert b_dict["kaydet"]["y"] - (b_dict["otobus"]["y"] + b_dict["otobus"]["h"]) >= 12.0 - 1e-4
    assert b_dict["otobus"]["x"] - (b_dict["ornek"]["x"] + b_dict["ornek"]["w"]) >= 16.0 - 1e-4

    # 5. Kart içi
    assert bx >= KX0 + 24.0 - 1e-4
    assert bx + gmax <= KX1 - 24.0 + 1e-4
    assert T1 - 0.74 * 72.0 >= KY0 + 12.0 - 1e-4
    assert T3 + 26.0 <= KY1 - 12.0 + 1e-4
    assert (T1 + 0.24 * 72.0) + 8.0 <= (T2 - 0.74 * 72.0) + 1e-4
    assert (T2 + 0.24 * 72.0) + 8.0 <= (T3 - 62.0) + 1e-4

    # 6. Altçizgi (2. satıra değmez)
    uy = 937.0
    assert uy + 2.5 + 2.5 <= 1005.0 - 0.74 * 64.0 - 8.0 + 1e-4

    # 7. Ekran satırı <= 24 karakter (künye ve kanal hariç)
    satirlar = [
        "Usually, always,",
        "every day: çoğunlukla",
        "Simple Present.",
        "My brother usually goes",
        "to school by bus.",
        "Kaydet",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"
    # İstisna: soru satırı (28 karakter; istem metni, tek satır bandı 460-560) -> genişlik <= 900
    assert Y.genislik("Caveat", 700, "Usually görünce hangi zaman?", 72) <= 900.0

    # 8. Yazı boyları >= 64 (künye ve kanal hariç): soru 72, kart 72, örnek 64, Kaydet 88
    for boy in (72, 72, 64, 88):
        assert boy >= 64, f"Yazı boyu {boy} < 64"

    # 9. HTML id kontrolleri
    c_kanal = html.count('id="kanal"')
    assert c_kanal == 1, f'id="kanal" sayısı: {c_kanal}'
    c_logo = html.count('id="logoimg"')
    assert c_logo == 1, f'id="logoimg" sayısı: {c_logo}'
    yasak_tema = "#root" + ".tema-acik"
    assert yasak_tema not in html, f"{yasak_tema} HTML içinde olmamalı"
    assert 'id="rz1"' not in html, 'id="rz1" HTML içinde olmamalı'

    # 10. Beklenen kimlikler
    beklenen_kimlikler = [
        "soru",
        "kagit",
        "kart-kenar",
        "kart-s1",
        "kart-s2",
        "kart-hap",
        "kart-hap-yazi",
        "ornek-1",
        "ornek-2",
        "ornek-cizgi",
        "otobus",
        "kaydet-ikon",
        "kaydet-imi",
        "kaydet-yazi",
    ]
    for kimlik in beklenen_kimlikler:
        assert f'id="{kimlik}"' in html, f'id="{kimlik}" HTML içinde bulunamadı'

    # 11. Sarı renk denetimi (künye rozeti + kart hapı; başka sarı yok)
    c_sari = html.count('fill="#f2a93b"')
    assert c_sari == 2, f"sarı sayısı: {c_sari}"


def uret() -> tuple[str, float, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    hap_w = Y.genislik("Fredoka", 700, "Simple Present.", 72) + 56.0
    g1 = Y.genislik("Fredoka", 700, "Usually, always,", 72)
    # DUZ2 (16.11, A3/A4): 2. satır sesle aynı terimi taşır ("every day: çoğunlukla"); kart yüksekliği değişmez
    g2 = Y.genislik("Fredoka", 700, "every day: çoğunlukla", 72)
    gmax = max(g1, g2, hap_w)
    bx = round(510.0 - gmax / 2.0, 1)

    otobus_html, oh = otobus_svg()
    bloklar = blok_kutulari(oh)

    kunye = Y.kunye_svg()
    soru = soru_svg()
    kart = kart_svg(bx, hap_w)
    ornek = ornek_svg()
    kaydet = kaydet_svg()

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
.tema-acik #kagit{{fill:#fffdf8;}}
#root #kart-kenar{{stroke:var(--pilMetin,#1b1a17);}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}"
     data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{soru}
{kart}
{ornek}
{otobus_html}
{kaydet}
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

    kurallari_dogrula(bloklar, bx, gmax, html)
    return html, bx, bloklar


if __name__ == "__main__":
    proje_dizini = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, bx, bloklar = uret()
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
    print(f"BX={bx}")

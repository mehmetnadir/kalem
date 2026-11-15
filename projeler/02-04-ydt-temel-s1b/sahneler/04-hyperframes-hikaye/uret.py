#!/usr/bin/python3
"""Sahne 04 hikâye karesi index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2 (15.11): kanal katmanı + v2 bantları."""
from __future__ import annotations

import json
import math
import sys
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

W, H = Y.W, Y.H
EK_Y = 583.0

BAVUL: list[str] = [
    "M6 8a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v11a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2z",
    "M10 6v-3h4v3",
    "M10 9v9",
    "M14 9v9",
    "M8.5 21v1.8",
    "M15.5 21v1.8",
]


def hesapla_s_ve_ek() -> tuple[int, float, float, float, float, float, float, float]:
    """YAŞI-YOR-UM için S boyutu ve parça genişliklerini hesaplar."""
    s0 = 100
    wa0 = Y.genislik("Fredoka", 700, "YAŞI", s0)
    wt0 = Y.genislik("Fredoka", 700, "-", s0)
    wy0 = Y.genislik("Fredoka", 700, "YOR", s0)
    wu0 = Y.genislik("Fredoka", 700, "UM", s0)
    p0 = 0.14 * s0
    ara0 = 0.08 * s0
    top100 = wa0 + wt0 + ara0 + 2.0 * p0 + wy0 + ara0 + wt0 + ara0 + wu0
    S = min(124, int(math.floor(900.0 * 100.0 / top100)))

    wa = Y.genislik("Fredoka", 700, "YAŞI", S)
    wt = Y.genislik("Fredoka", 700, "-", S)
    wy = Y.genislik("Fredoka", 700, "YOR", S)
    wu = Y.genislik("Fredoka", 700, "UM", S)
    p = 0.14 * S
    ara = 0.08 * S
    top = wa + wt + ara + 2.0 * p + wy + ara + wt + ara + wu
    while top > 900.0 and S > 1:
        S -= 1
        wa = Y.genislik("Fredoka", 700, "YAŞI", S)
        wt = Y.genislik("Fredoka", 700, "-", S)
        wy = Y.genislik("Fredoka", 700, "YOR", S)
        wu = Y.genislik("Fredoka", 700, "UM", S)
        p = 0.14 * S
        ara = 0.08 * S
        top = wa + wt + ara + 2.0 * p + wy + ara + wt + ara + wu
    assert top <= 900.0, f"top={top} > 900"
    return S, top, wa, wt, wy, wu, p, ara


def ek_svg(S: int, top: float, wa: float, wt: float, wy: float, wu: float, p: float, ara: float) -> str:
    """YAŞI-YOR-UM grubu SVG çıktısı."""
    x0 = 510.0 - top / 2.0
    kx0 = x0 + wa + wt + ara
    kx1 = kx0 + 2.0 * p + wy
    kw = kx1 - kx0
    ky = EK_Y - 0.86 * S
    kh = (0.86 + 0.16) * S
    krx = 0.10 * S

    return (
        f'<g id="ek">'
        f'<rect id="ek-kutu" x="{kx0:.2f}" y="{ky:.2f}" width="{kw:.2f}" height="{kh:.2f}" '
        f'rx="{krx:.2f}" fill="{R["vurgu"]}"/>'
        f'<text id="ek-yasi" x="{x0:.2f}" y="{EK_Y:.0f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" xml:space="preserve">YAŞI</text>'
        f'<text id="ek-tire1" x="{x0 + wa:.2f}" y="{EK_Y:.0f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["ikincil"]}" xml:space="preserve">-</text>'
        f'<text id="ek-yor" x="{kx0 + p:.2f}" y="{EK_Y:.0f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["zemin"]}" xml:space="preserve">YOR</text>'
        f'<text id="ek-tire2" x="{kx1 + ara:.2f}" y="{EK_Y:.0f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["ikincil"]}" xml:space="preserve">-</text>'
        f'<text id="ek-um" x="{kx1 + 2.0 * ara + wt:.2f}" y="{EK_Y:.0f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" xml:space="preserve">UM</text>'
        f'</g>'
    )


def kart_svg(simge: str, x0: int, ikon_yollar: list[str], baslik: str, etiket: str) -> str:
    """Kart grubu SVG çıktısı."""
    crv = (
        f'<rect id="{simge}-crv" x="{x0 + 2}" y="638" width="434" height="200" rx="26" '  # QA 1: çizgi dış kenarı x0..x0+438
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    scale_str = f"{80 / 24:.6f}"
    paths = "".join(f'<path d="{d}"/>' for d in ikon_yollar)
    ikon = (
        f'<g id="{simge}-ikon" transform="translate({x0 + 24} 660) scale({scale_str})" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
        f'{paths}'
        f'</g>'
    )
    baslik_elem = (
        f'<text id="{simge}-baslik" x="{x0 + 116}" y="722" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}" xml:space="preserve">{baslik}</text>'
    )
    etiket_elem = (
        f'<text id="{simge}-etiket" x="{x0 + 24}" y="800" font-family="Caveat" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}">{etiket}</text>'
    )
    return f'<g id="{simge}">{crv}{ikon}{baslik_elem}{etiket_elem}</g>'


def ozet_svg() -> str:
    """Özet grubu SVG çıktısı."""
    t1 = (
        f'<text id="ozet1" x="60" y="924" font-family="Fredoka" font-weight="700" '
        f'font-size="68" fill="{R["murekkep"]}">Kalıcıysa geniş zaman,</text>'
    )
    t2 = (
        f'<text id="ozet2" x="60" y="1008" font-family="Fredoka" font-weight="700" '
        f'font-size="68" fill="{R["murekkep"]}">geçiciyse şimdiki zaman.</text>'
    )
    return f'<g id="ozet">{t1}{t2}</g>'


def kaydet_svg() -> str:
    """Kaydet grubu SVG çıktısı."""
    hap_w = Y.genislik("Fredoka", 700, "Kaydet", 64) + 80.0
    imi = (
        f'<g transform="translate(39 1044) scale(4)" fill="none" stroke="{R["murekkep"]}" '  # QA 1: çizgi x ≥ 60
        f'stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round">'
        f'<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/>'
        f'</g>'
    )
    hap = f'<rect id="kaydet-hap" x="128" y="1048" width="{hap_w:.1f}" height="88" rx="44" fill="{R["vurgu"]}"/>'
    yazi = (
        f'<text id="kaydet-yazi" x="{128.0 + hap_w / 2.0:.1f}" y="1114" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{R["zemin"]}">Kaydet</text>'
    )
    return f'<g id="kaydet">{imi}{hap}{yazi}</g>'


def blok_kutulari(S: int, top: float) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    w_kanal = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - 53.2
    kanal = {"ad": "kanal", "x": 53.2, "y": 291.0, "w": w_kanal, "h": 48.0}

    rz_x, rz_w = Y.rozet_konumlari()[0]
    kunye = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": rz_x + rz_w - 60.0, "h": 48.0}

    ek = {"ad": "ek", "x": 510.0 - top / 2.0, "y": EK_Y - 0.86 * S, "w": top, "h": 1.08 * S}

    kart1 = {"ad": "kart1", "x": 60.0, "y": 636.0, "w": 438.0, "h": 204.0}
    kart2 = {"ad": "kart2", "x": 522.0, "y": 636.0, "w": 438.0, "h": 204.0}

    w_ozet = max(
        Y.genislik("Fredoka", 700, "Kalıcıysa geniş zaman,", 68),
        Y.genislik("Fredoka", 700, "geçiciyse şimdiki zaman.", 68),
    )
    ozet_y = 924.0 - 0.75 * 68.0
    ozet_h = (1008.0 + 0.25 * 68.0) - ozet_y
    ozet = {"ad": "ozet", "x": 60.0, "y": ozet_y, "w": w_ozet, "h": ozet_h}

    hap_w = Y.genislik("Fredoka", 700, "Kaydet", 64) + 80.0
    kaydet = {"ad": "kaydet", "x": 60.0, "y": 1048.0, "w": 128.0 + hap_w - 60.0, "h": 88.0}

    return [kanal, kunye, ek, kart1, kart2, ozet, kaydet]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], S: int, html: str) -> None:
    """SPEC.md §5 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. İçerik blokları (ek, kart1, kart2, ozet, kaydet): x >= 60, x + w <= 960, y >= 460, y + h <= 1140
    for ad in ("ek", "kart1", "kart2", "ozet", "kaydet"):
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

    # 4. Dikey boşluk >= 16: kunye -> ek, ek -> kart1, ek -> kart2, kart1 -> ozet, ozet -> kaydet
    assert b_dict["ek"]["y"] - (b_dict["kunye"]["y"] + b_dict["kunye"]["h"]) >= 16.0
    assert b_dict["kart1"]["y"] - (b_dict["ek"]["y"] + b_dict["ek"]["h"]) >= 16.0
    assert b_dict["kart2"]["y"] - (b_dict["ek"]["y"] + b_dict["ek"]["h"]) >= 16.0
    assert b_dict["ozet"]["y"] - (b_dict["kart1"]["y"] + b_dict["kart1"]["h"]) >= 16.0
    assert b_dict["kaydet"]["y"] - (b_dict["ozet"]["y"] + b_dict["ozet"]["h"]) >= 16.0
    # Yatay: kart2.x - (kart1.x + kart1.w) >= 16
    assert b_dict["kart2"]["x"] - (b_dict["kart1"]["x"] + b_dict["kart1"]["w"]) >= 16.0

    # 5. Kart içi: 116 + genişlik(Fredoka 700 başlık 64) <= 438 - 24; genişlik(Caveat 700 etiket 64) <= 438 - 48
    for baslik, etiket in (("I live", "PERMANENT"), ("I am living", "TEMPORARY")):
        assert 116.0 + Y.genislik("Fredoka", 700, baslik, 64) <= 438.0 - 24.0
        assert Y.genislik("Caveat", 700, etiket, 64) <= 438.0 - 48.0

    # 6. Yazı boyları: S >= 64; kart başlığı, etiket, hap yazısı 64; özet 68
    assert S >= 64, f"ek boyutu {S} < 64"

    # 7. Ekran satırı <= 24 karakter (künye ve kanal satırı hariç)
    satirlar = [
        "YAŞI-YOR-UM",
        "I live",
        "PERMANENT",
        "I am living",
        "TEMPORARY",
        "Kalıcıysa geniş zaman,",
        "geçiciyse şimdiki zaman.",
        "Kaydet",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 8. Yasak söz denetimi kodda değil, dış metin taramasında (standart §7.3 grep; literal kodda grep'i kirletir).

    # 9. HTML'de id="kanal" ve id="logoimg" tam 1 kez geçer
    c_kanal = html.count('id="kanal"')
    assert c_kanal == 1, f'id="kanal" sayısı: {c_kanal}'
    c_logo = html.count('id="logoimg"')
    assert c_logo == 1, f'id="logoimg" sayısı: {c_logo}'

    # Kabul ölçütleri kontrolleri
    for var in (
        'id="kanal"',
        'id="ek-yor"',
        'id="kart1-baslik"',
        'id="kart2-etiket"',
        'id="ozet2"',
        'id="kaydet-imi"',
        'id="kaydet-hap"',
    ):
        assert var in html, f"{var} HTML içinde bulunamadı"
    for yok in ('id="ku-cip"', 'id="cg1"', 'id="hap-kutu"', 'id="ust"', 'id="alt"'):
        assert yok not in html, f"{yok} HTML içinde olmamalı"


def uret() -> tuple[str, int, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    S, top, wa, wt, wy, wu, p, ara = hesapla_s_ve_ek()
    bloklar = blok_kutulari(S, top)

    kunye = Y.kunye_svg()
    ek = ek_svg(S, top, wa, wt, wy, wu, p, ara)
    kart1 = kart_svg("kart1", 60, Y.tabler("home"), "I live", "PERMANENT")
    kart2 = kart_svg("kart2", 522, BAVUL, "I am living", "TEMPORARY")
    ozet = ozet_svg()
    kaydet = kaydet_svg()

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}"
     data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{ek}
{kart1}
{kart2}
{ozet}
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

    kurallari_dogrula(bloklar, S, html)
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

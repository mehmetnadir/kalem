#!/usr/bin/python3
"""Sahne 08 hikâye karesi B index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2 (15.11): kanal katmanı + v2 bantları (soru kartı düzeni)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# zaman.json ve zamanlar.json okuma ve doğrulama
zaman_data = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlar = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlar) == 1, (
    f"duragan listesinde {AD.name} olan tek kayıt olmalı, bulunan: {len(duragan_kayitlar)}"
)
kayit = duragan_kayitlar[0]
assert kayit["kare"] == 1, f"kare {kayit['kare']} != 1"
assert kayit["cikti"] == "hikaye-b.png", f"cikti {kayit['cikti']} != 'hikaye-b.png'"
assert AD.name not in [s["klasor"] for s in zaman_data.get("sahneler", [])], "AD.name sahneler içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

W, H = Y.W, Y.H

YESIL = "#167a4a"
YESIL_KOYU = "#4fbf85"

BOY_SORU = 80
BOY_KOK = 72
BOY_SIK = 72
BOY_OZET = 64
BOY_KAYDET = 64


def soru_svg() -> str:
    """Soru başlığı SVG çıktısı."""
    return (
        f'<text id="soru" x="60" y="535" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_SORU}" fill="{R["murekkep"]}" xml:space="preserve">Hangisi doğru?</text>'
    )


def kok_svg() -> str:
    """Kök cümle grubu SVG çıktısı."""
    w_parents = Y.genislik("Fredoka", 700, "My parents", BOY_KOK)
    w_space = Y.genislik("Fredoka", 700, " ", BOY_KOK)
    bos_x1 = round(60.0 + w_parents + w_space + 4.0, 1)
    bos_x2 = round(bos_x1 + 216.0, 1)
    d = f"M{bos_x1} 657 C{round(bos_x1 + 70.0, 1)} 652 {round(bos_x1 + 146.0, 1)} 662 {bos_x2} 655"
    kok1 = (
        f'<text id="kok1" x="60" y="650" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_KOK}" fill="{R["murekkep"]}" xml:space="preserve">My parents</text>'
    )
    bosluk = (
        f'<path id="kok-bosluk" d="{d}" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="7" stroke-linecap="round"/>'
    )
    kok2 = (
        f'<text id="kok2" x="60" y="740" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_KOK}" fill="{R["murekkep"]}" xml:space="preserve">to work by bus.</text>'
    )
    return f'<g id="kok">{kok1}{bosluk}{kok2}</g>'


def siklar_svg() -> str:
    """Şıklar grubu SVG çıktısı."""
    sik_a_crv = (
        f'<rect id="sik-a-crv" x="63" y="793" width="414" height="94" rx="26" '
        f'fill="none" stroke="{YESIL}" stroke-width="6"/>'
    )
    sik_a_yazi = (
        f'<text id="sik-a-yazi" x="96" y="862" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_SIK}" fill="{R["murekkep"]}" xml:space="preserve">A) go</text>'
    )
    sik_a_tik = (
        f'<g id="sik-a-tik" transform="translate(360 792) scale(4)" fill="none" stroke="{YESIL}" '
        f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
        f'<path d="M5 12l5 5l10 -10"/>'
        f'</g>'
    )
    sik_a = f'<g id="sik-a">{sik_a_crv}{sik_a_yazi}{sik_a_tik}</g>'

    sik_b_crv = (
        f'<rect id="sik-b-crv" x="542" y="792" width="416" height="96" rx="26" '
        f'fill="none" stroke="{R["ikincil"]}" stroke-width="4"/>'
    )
    sik_b_yazi = (
        f'<text id="sik-b-yazi" x="576" y="862" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_SIK}" fill="{R["murekkep"]}" xml:space="preserve">B) goes</text>'
    )
    sik_b = f'<g id="sik-b" opacity="0.45">{sik_b_crv}{sik_b_yazi}</g>'

    return f'<g id="siklar">{sik_a}{sik_b}</g>'


def ozet_svg() -> str:
    """Kural özeti grubu SVG çıktısı."""
    return (
        f'<g id="ozet">'
        f'<text id="ozet1" x="60" y="970" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_OZET}" fill="{R["murekkep"]}" xml:space="preserve">He, she, it: s gelir;</text>'
        f'<text id="ozet2" x="60" y="1050" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_OZET}" fill="{R["murekkep"]}" xml:space="preserve">I, you, we, they: s yok.</text>'
        f'</g>'
    )


def kaydet_svg() -> str:
    """Kaydet grubu SVG çıktısı."""
    hap_w = Y.genislik("Fredoka", 700, "Kaydet", BOY_KAYDET) + 80.0
    imi = (
        f'<g transform="translate(39 1412) scale(4)" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round">'
        f'<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/>'
        f'</g>'
    )
    hap = f'<rect id="kaydet-hap" x="128" y="1416" width="{hap_w:.1f}" height="88" rx="44" fill="{R["vurgu"]}"/>'
    yazi = (
        f'<text id="kaydet-yazi" x="{128.0 + hap_w / 2.0:.1f}" y="1482" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="{BOY_KAYDET}" fill="{R["zemin"]}" '
        f'xml:space="preserve">Kaydet</text>'
    )
    return f'<g id="kaydet">{imi}{hap}{yazi}</g>'


def blok_kutulari() -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    w_kanal = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - 53.2
    kanal = {"ad": "kanal", "x": 53.2, "y": 291.0, "w": w_kanal, "h": 48.0}

    rz_x, rz_w = Y.rozet_konumlari()[0]
    kunye = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": rz_x + rz_w - 60.0, "h": 48.0}

    w_soru = Y.genislik("Fredoka", 700, "Hangisi doğru?", BOY_SORU)
    soru_y = 535.0 - 0.75 * BOY_SORU
    soru = {"ad": "soru", "x": 60.0, "y": soru_y, "w": w_soru, "h": float(BOY_SORU)}

    w_parents = Y.genislik("Fredoka", 700, "My parents", BOY_KOK)
    w_space = Y.genislik("Fredoka", 700, " ", BOY_KOK)
    bos_x1 = round(60.0 + w_parents + w_space + 4.0, 1)
    bos_x2 = round(bos_x1 + 216.0, 1)
    w_kok = max(bos_x2 + 3.5 - 60.0, Y.genislik("Fredoka", 700, "to work by bus.", BOY_KOK))
    kok_y = 650.0 - 0.75 * BOY_KOK
    kok_h = (740.0 + 0.25 * BOY_KOK) - kok_y
    kok = {"ad": "kok", "x": 60.0, "y": kok_y, "w": w_kok, "h": kok_h}

    sik_a = {"ad": "sik-a", "x": 60.0, "y": 790.0, "w": 420.0, "h": 100.0}

    sik_b = {"ad": "sik-b", "x": 540.0, "y": 790.0, "w": 420.0, "h": 100.0}

    w_ozet = max(
        Y.genislik("Fredoka", 700, "He, she, it: s gelir;", BOY_OZET),
        Y.genislik("Fredoka", 700, "I, you, we, they: s yok.", BOY_OZET),
    )
    ozet_y = 970.0 - 0.75 * BOY_OZET
    ozet_h = (1050.0 + 0.25 * BOY_OZET) - ozet_y
    ozet = {"ad": "ozet", "x": 60.0, "y": ozet_y, "w": w_ozet, "h": ozet_h}

    hap_w = Y.genislik("Fredoka", 700, "Kaydet", BOY_KAYDET) + 80.0
    kaydet = {"ad": "kaydet", "x": 60.0, "y": 1416.0, "w": 128.0 + hap_w - 60.0, "h": 88.0}

    return [kanal, kunye, soru, kok, sik_a, sik_b, ozet, kaydet]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §5 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. soru, kok, sik-a, sik-b, ozet: x >= 60, x + w <= 960, y >= 460, y + h <= 1140
    for ad in ("soru", "kok", "sik-a", "sik-b", "ozet"):
        b = b_dict[ad]
        assert b["x"] >= 60.0 - 1e-4, f"{ad} sol kenar {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ kenar {b['x'] + b['w']} > 960"
        assert b["y"] >= 460.0 - 1e-4, f"{ad} üst {b['y']} < 460"
        assert b["y"] + b["h"] <= 1140.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1140"

    # 2. kaydet: x >= 60, x + w <= 960, y >= 1400, y + h <= 1520
    b_kaydet = b_dict["kaydet"]
    assert b_kaydet["x"] >= 60.0 - 1e-4, f"kaydet sol kenar {b_kaydet['x']} < 60"
    assert b_kaydet["x"] + b_kaydet["w"] <= 960.0 + 1e-4, f"kaydet sağ kenar {b_kaydet['x'] + b_kaydet['w']} > 960"
    assert b_kaydet["y"] >= 1400.0 - 1e-4, f"kaydet üst {b_kaydet['y']} < 1400"
    assert b_kaydet["y"] + b_kaydet["h"] <= 1520.0 + 1e-4, f"kaydet alt {b_kaydet['y'] + b_kaydet['h']} > 1520"

    # 3. kanal ve kunye: y >= 280, y + h <= 450
    for ad in ("kanal", "kunye"):
        b = b_dict[ad]
        assert b["y"] >= 280.0 - 1e-4, f"{ad} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 450.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 450"

    # 4. Bütün blok çiftlerinin kesişim alanı 0
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    # 5. Dikey boşluk >= 16: kunye -> soru, soru -> kok, kok -> sik-a, kok -> sik-b, sik-a -> ozet, sik-b -> ozet
    assert b_dict["soru"]["y"] - (b_dict["kunye"]["y"] + b_dict["kunye"]["h"]) >= 16.0 - 1e-4
    assert b_dict["kok"]["y"] - (b_dict["soru"]["y"] + b_dict["soru"]["h"]) >= 16.0 - 1e-4
    assert b_dict["sik-a"]["y"] - (b_dict["kok"]["y"] + b_dict["kok"]["h"]) >= 16.0 - 1e-4
    assert b_dict["sik-b"]["y"] - (b_dict["kok"]["y"] + b_dict["kok"]["h"]) >= 16.0 - 1e-4
    assert b_dict["ozet"]["y"] - (b_dict["sik-a"]["y"] + b_dict["sik-a"]["h"]) >= 16.0 - 1e-4
    assert b_dict["ozet"]["y"] - (b_dict["sik-b"]["y"] + b_dict["sik-b"]["h"]) >= 16.0 - 1e-4

    # 6. Kart içi: 96 + genişlik("A) go", 72) <= 380 - 24 · 576 + genişlik("B) goes", 72) <= 960 - 36
    w_a = Y.genislik("Fredoka", 700, "A) go", BOY_SIK)
    assert 96.0 + w_a <= 380.0 - 24.0, f"Kart A içi metin sağ sınırını aşıyor: {96.0 + w_a}"
    w_b = Y.genislik("Fredoka", 700, "B) goes", BOY_SIK)
    assert 576.0 + w_b <= 960.0 - 36.0, f"Kart B içi metin sağ sınırını aşıyor: {576.0 + w_b}"

    # 7. Yazı boyları >= 64: BOY_SORU, BOY_KOK, BOY_SIK, BOY_OZET, BOY_KAYDET
    for boy in (BOY_SORU, BOY_KOK, BOY_SIK, BOY_OZET, BOY_KAYDET):
        assert boy >= 64, f"Yazı boyu {boy} < 64"

    # 8. Ekran satırı <= 24 karakter (len)
    satirlar = [
        "Hangisi doğru?",
        "My parents ____",
        "to work by bus.",
        "A) go",
        "B) goes",
        "He, she, it: s gelir;",
        "I, you, we, they: s yok.",
        "Kaydet",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 9. HTML kontrolleri
    c_kanal = html.count('id="kanal"')
    assert c_kanal == 1, f'id="kanal" sayısı: {c_kanal}'
    c_logo = html.count('id="logoimg"')
    assert c_logo == 1, f'id="logoimg" sayısı: {c_logo}'
    assert "#root.tema-acik" not in html, "HTML içinde #root.tema-acik dizisi geçmemeli"

    kimlikler_var = (
        "soru", "kok1", "kok2", "kok-bosluk",
        "sik-a", "sik-a-crv", "sik-a-yazi", "sik-a-tik",
        "sik-b", "sik-b-crv", "sik-b-yazi",
        "ozet1", "ozet2",
        "kaydet-imi", "kaydet-hap", "kaydet-yazi",
    )
    for k in kimlikler_var:
        assert f'id="{k}"' in html, f'id="{k}" HTML içinde bulunamadı'

    kimlikler_yok = ("ku-cip", "cg1", "cg2", "hap-kutu", "soru-kutu", "kA", "kB")
    for k in kimlikler_yok:
        assert f'id="{k}"' not in html, f'id="{k}" HTML içinde olmamalı'

    # 10. svg içi kontroller
    svg = html.split('<svg id="sahne"', 1)[1]
    c_yesil = svg.count(f'stroke="{YESIL}"')
    assert c_yesil == 2, f'stroke="{YESIL}" sayısı {c_yesil} != 2'
    c_vurgu = svg.count(R["vurgu"])
    assert c_vurgu == 2, f'R["vurgu"] ({R["vurgu"]}) sayısı {c_vurgu} != 2'
    c_kirmizi = svg.count(R["kirmizi"])
    assert c_kirmizi == 0, f'R["kirmizi"] ({R["kirmizi"]}) sayısı {c_kirmizi} != 0'
    assert ">_" not in svg, "svg içinde >_ geçmemeli"
    assert "→" not in svg, "svg içinde → geçmemeli"

    c_yesil_koyu = html.count(YESIL_KOYU)
    assert c_yesil_koyu == 1, f"{YESIL_KOYU} sayısı {c_yesil_koyu} != 1"
    c_sik_b_op = html.count('id="sik-b" opacity="0.45"')
    assert c_sik_b_op == 1, f'id="sik-b" opacity="0.45" sayısı {c_sik_b_op} != 1'


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()

    kunye = Y.kunye_svg()
    soru = soru_svg()
    kok = kok_svg()
    siklar = siklar_svg()
    ozet = ozet_svg()
    kaydet = kaydet_svg()

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
#root:not(.tema-acik) [stroke="{YESIL}"]{{stroke:{YESIL_KOYU}}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}"
     data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{soru}
{kok}
{siklar}
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

    kurallari_dogrula(bloklar, html)
    return html, bloklar


if __name__ == "__main__":
    proje_dizini = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, bloklar = uret()
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

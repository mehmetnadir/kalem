#!/usr/bin/python3
"""Sahne 05 hikâye karesi A index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2 (15.11): kanal katmanı + v2 bantları."""
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
hikaye = zaman_data["hikaye"]
assert hikaye["klasor"] == AD.name, f"klasor {hikaye['klasor']} != {AD.name}"
assert hikaye["kare"] == 1, f"kare {hikaye['kare']} != 1"
assert AD.name not in [s["klasor"] for s in zaman_data["sahneler"]], "AD.name sahneler içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu", "kirmizi"}

W, H = Y.W, Y.H


def etiket_svg() -> str:
    """Etiket SVG çıktısı."""
    return (
        f'<text id="etiket" x="60" y="526" font-family="Caveat" font-weight="700" '
        f'font-size="64" fill="{R["ikincil"]}" style="font-kerning:none">Sınav tuzağı</text>'
    )


def kart_svg() -> str:
    """Kart grubu SVG çıktısı."""
    zemin = (
        f'<rect id="kart-zemin" x="60" y="560" width="900" height="200" rx="30" '
        f'fill="{R["murekkep"]}" fill-opacity="0.06"/>'
    )
    cerceve = (
        f'<rect id="kart-cerceve" x="62" y="562" width="896" height="196" rx="28" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )
    t1 = (
        f'<text id="kart1" x="510" y="639" text-anchor="middle" font-family="Fredoka" '
        f'font-weight="700" font-size="88" fill="{R["murekkep"]}" style="font-kerning:none">Does varsa</text>'
    )
    t2 = (
        f'<text id="kart2" x="510" y="723" text-anchor="middle" font-family="Fredoka" '
        f'font-weight="700" font-size="88" fill="{R["murekkep"]}" style="font-kerning:none">fiil yalın.</text>'
    )
    return f'<g id="kart">{zemin}{cerceve}{t1}{t2}</g>'


def yanlis_svg() -> str:
    """Yanlış grubu SVG çıktısı."""
    carpi = (
        f'<path id="yanlis-carpi" d="M64 799 Q85 819 107 842 M107 798 Q87 821 65 841" '
        f'fill="none" stroke="{R["kirmizi"]}" stroke-width="7" stroke-linecap="round"/>'
    )
    yazi = (
        f'<text id="yanlis-yazi" x="132" y="840" font-family="Fredoka" font-weight="700" '
        f'font-size="56" fill="{R["ikincil"]}" style="font-kerning:none">'
        f'He doesn\'t go<tspan id="yanlis-es">es</tspan>.</text>'
    )
    x_es = 132.0 + Y.genislik("Fredoka", 700, "He doesn't go", 56)
    w_es = Y.genislik("Fredoka", 700, "es", 56)
    cizik = (
        f'<path id="yanlis-cizik" d="M{x_es + 1.0:.1f} 827 L{x_es + w_es - 1.0:.1f} 821" '  # QA 1: uç `o`ya ve noktaya değmez
        f'fill="none" stroke="{R["kirmizi"]}" stroke-width="6" stroke-linecap="round"/>'
    )
    return f'<g id="yanlis">{carpi}{yazi}{cizik}</g>'


def dogru1_svg() -> str:
    """Doğru 1 grubu SVG çıktısı."""
    tik = (
        f'<path id="dogru1-tik" d="M64 909 L79 927 Q90 905 108 888" fill="none" '
        f'stroke="{R["murekkep"]}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    yazi = (
        f'<text id="dogru1-yazi" x="132" y="932" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}" style="font-kerning:none">He doesn\'t go.</text>'
    )
    return f'<g id="dogru1">{tik}{yazi}</g>'


def dogru2_svg() -> str:
    """Doğru 2 grubu SVG çıktısı."""
    tik = (
        f'<path id="dogru2-tik" d="M64 999 L79 1017 Q90 995 108 978" fill="none" '
        f'stroke="{R["murekkep"]}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    yazi = (
        f'<text id="dogru2-yazi" x="132" y="1022" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}" style="font-kerning:none">Does she go?</text>'
    )
    return f'<g id="dogru2">{tik}{yazi}</g>'


def kaydet_svg() -> str:
    """Kaydet grubu SVG çıktısı."""
    hap_w = Y.genislik("Lexend", 700, "Kaydet", 52) + 56.0
    imi = (
        f'<g transform="translate(39 1052) scale(4)" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round">'
        f'<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/>'
        f'</g>'
    )
    hap = f'<rect id="kaydet-hap" x="132" y="1060" width="{hap_w:.1f}" height="80" rx="40" fill="{R["vurgu"]}"/>'
    yazi = (
        f'<text id="kaydet-yazi" x="{132.0 + hap_w / 2.0:.1f}" y="1118" text-anchor="middle" '
        f'font-family="Lexend" font-weight="700" font-size="52" fill="{R["zemin"]}" '
        f'style="font-kerning:none">Kaydet</text>'
    )
    return f'<g id="kaydet">{imi}{hap}{yazi}</g>'


def blok_kutulari() -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    w_kanal = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - 53.2
    kanal = {"ad": "kanal", "x": 53.2, "y": 291.0, "w": w_kanal, "h": 48.0}

    rz_x, rz_w = Y.rozet_konumlari()[0]
    kunye = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": rz_x + rz_w - 60.0, "h": 48.0}

    w_etiket = Y.genislik("Caveat", 700, "Sınav tuzağı", 64)
    etiket = {"ad": "etiket", "x": 60.0, "y": 478.0, "w": w_etiket, "h": 64.0}

    kart = {"ad": "kart", "x": 60.0, "y": 560.0, "w": 900.0, "h": 200.0}

    w_yanlis = 132.0 + Y.genislik("Fredoka", 700, "He doesn't goes.", 56) - 60.0
    yanlis = {"ad": "yanlis", "x": 60.0, "y": 794.0, "w": w_yanlis, "h": 60.0}

    w_dogru1 = 132.0 + Y.genislik("Fredoka", 700, "He doesn't go.", 64) - 60.0
    dogru1 = {"ad": "dogru1", "x": 60.0, "y": 884.0, "w": w_dogru1, "h": 64.0}

    w_dogru2 = 132.0 + Y.genislik("Fredoka", 700, "Does she go?", 64) - 60.0
    dogru2 = {"ad": "dogru2", "x": 60.0, "y": 974.0, "w": w_dogru2, "h": 64.0}

    hap_w = Y.genislik("Lexend", 700, "Kaydet", 52) + 56.0
    kaydet = {"ad": "kaydet", "x": 60.0, "y": 1060.0, "w": 132.0 + hap_w - 60.0, "h": 80.0}

    return [kanal, kunye, etiket, kart, yanlis, dogru1, dogru2, kaydet]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §5 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. İçerik blokları (etiket, kart, yanlis, dogru1, dogru2, kaydet)
    for ad in ("etiket", "kart", "yanlis", "dogru1", "dogru2", "kaydet"):
        b = b_dict[ad]
        assert b["x"] >= 60.0 - 1e-4, f"{ad} sol kenar {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ kenar {b['x'] + b['w']} > 960"
        assert b["y"] >= 460.0 - 1e-4, f"{ad} üst {b['y']} < 460"
        assert b["y"] + b["h"] <= 1140.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1140"

    # 2. Her içerik bloğu kendi istem bandında (§3 tablo "Bant")
    bantlar = {
        "etiket": (470.0, 550.0),
        "kart": (560.0, 760.0),
        "yanlis": (780.0, 860.0),
        "dogru1": (870.0, 950.0),
        "dogru2": (960.0, 1040.0),
        "kaydet": (1060.0, 1140.0),
    }
    for ad, (bant_bas, bant_son) in bantlar.items():
        b = b_dict[ad]
        assert b["y"] >= bant_bas - 1e-4, f"{ad} üst {b['y']} < bant_bas {bant_bas}"
        assert b["y"] + b["h"] <= bant_son + 1e-4, f"{ad} alt {b['y'] + b['h']} > bant_son {bant_son}"

    # 3. kanal ve kunye: y >= 280, y + h <= 450
    for ad in ("kanal", "kunye"):
        b = b_dict[ad]
        assert b["y"] >= 280.0 - 1e-4, f"{ad} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 450.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 450"

    # 4. Bütün blok çiftlerinin kesişim alanı 0; ardışık bloklar arası dikey boşluk >= 16
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    ardisik = ["kunye", "etiket", "kart", "yanlis", "dogru1", "dogru2", "kaydet"]
    for i in range(len(ardisik) - 1):
        ust = b_dict[ardisik[i]]
        alt = b_dict[ardisik[i + 1]]
        bosluk = alt["y"] - (ust["y"] + ust["h"])
        assert bosluk >= 16.0 - 1e-4, f"{ardisik[i]} -> {ardisik[i + 1]} dikey boşluk {bosluk} < 16"

    # 5. Kart içi yerleşim sınırları
    w_kart1 = Y.genislik("Fredoka", 700, "Does varsa", 88)
    w_kart2 = Y.genislik("Fredoka", 700, "fiil yalın.", 88)
    assert max(w_kart1, w_kart2) <= 900.0 - 2.0 * 56.0, "kart içi metin genişliği sınırı aşıldı"
    # QA 1: ölçülen yazı 581–745 (üst pay 17, alt 11) -> tabanlar 3 px yukarı (pay 14 / 14)
    assert 639.0 - 0.75 * 88.0 >= 560.0 + 12.0, "kart1 üst boşluk yetersiz"
    assert 723.0 + 0.25 * 88.0 <= 760.0 - 8.0, "kart2 alt boşluk yetersiz"

    # 6. Yazı boyları (sabitler): etiket 64, kart 88, yanlış 56, doğru 64, hap 52
    boylar = {"etiket": 64, "kart": 88, "yanlis": 56, "dogru": 64, "hap": 52}
    assert all(b >= 50 for b in boylar.values()), f"yazı boyu < 50: {boylar}"
    assert boylar["kart"] >= 64 and boylar["dogru"] >= 64, f"ana yazı < 64: {boylar}"

    # 7. Ekran satırı <= 24 karakter
    satirlar = [
        "Sınav tuzağı",
        "Does varsa",
        "fiil yalın.",
        "He doesn't goes.",
        "He doesn't go.",
        "Does she go?",
        "Kaydet",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 8. Renk kuralları
    c_kirmizi = html.count(R["kirmizi"])
    assert c_kirmizi == 2, f"R['kirmizi'] sayısı {c_kirmizi} != 2"
    y_bas = html.find('<g id="yanlis">')
    y_son = html.find("</g>", y_bas) + 4
    yanlis_parca = html[y_bas:y_son]
    assert yanlis_parca.count(R["kirmizi"]) == 2, "Kırmızı yalnız yanlis grubunda olmalı"

    c_vurgu = html.count(R["vurgu"])
    assert c_vurgu == 2, f"R['vurgu'] sayısı {c_vurgu} != 2 (künye rozeti + kaydet-hap)"
    assert "#167a4a" not in html, "Yeşil (#167a4a) HTML içinde olmamalı"
    assert "✗" not in html, "✗ karakteri HTML içinde olmamalı"
    assert "✓" not in html, "✓ karakteri HTML içinde olmamalı"

    # 9. HTML'de id="kanal" ve id="logoimg" tam 1 kez
    c_kanal = html.count('id="kanal"')
    assert c_kanal == 1, f'id="kanal" sayısı: {c_kanal}'
    c_logo = html.count('id="logoimg"')
    assert c_logo == 1, f'id="logoimg" sayısı: {c_logo}'

    # 10. Kabul ölçütleri kontrolleri
    for var in (
        'id="etiket"',
        'id="kart-cerceve"',
        'id="kart1"',
        'id="kart2"',
        'id="yanlis-carpi"',
        'id="yanlis-es"',
        'id="yanlis-cizik"',
        'id="dogru1-tik"',
        'id="dogru2-tik"',
        'id="dogru1-yazi"',
        'id="dogru2-yazi"',
        'id="kaydet-imi"',
        'id="kaydet-hap"',
        'id="kaydet-yazi"',
    ):
        assert var in html, f"{var} HTML içinde bulunamadı"

    for yok in ('id="ku-cip"', 'id="cg1"', 'id="ek-yor"', 'id="ozet"'):
        assert yok not in html, f"{yok} HTML içinde olmamalı"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()

    kunye = Y.kunye_svg()
    etiket = etiket_svg()
    kart = kart_svg()
    yanlis = yanlis_svg()
    dogru1 = dogru1_svg()
    dogru2 = dogru2_svg()
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
{etiket}
{kart}
{yanlis}
{dogru1}
{dogru2}
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

#!/usr/bin/python3
"""Sahne 07 hikâye karesi B index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2 (15.11): kanal katmanı + v2 bantları (soru-cevap düzeni)."""
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

BOY_TR = 76
BOY_KART = 72
BOY_YANLIS = 64
BOY_OZET = 68
BOY_KAYDET = 64


def tr_svg() -> str:
    """Türkçe cümle grubu SVG çıktısı."""
    return (
        f'<g id="tr">'
        f'<text id="tr1" x="60" y="538" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_TR}" fill="{R["murekkep"]}" xml:space="preserve">Şimdilik amcamla</text>'
        f'<text id="tr2" x="60" y="622" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_TR}" fill="{R["murekkep"]}" xml:space="preserve">yaşıyorum.</text>'
        f'</g>'
    )


def dogru_svg() -> str:
    """Doğru şık kartı grubu SVG çıktısı."""
    crv = (
        f'<rect id="dogru-crv" x="63" y="667" width="894" height="194" rx="28" '
        f'fill="none" stroke="{YESIL}" stroke-width="6"/>'
    )
    s1 = (
        f'<text id="dogru-s1" x="100" y="742" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_KART}" fill="{R["murekkep"]}" xml:space="preserve">I am living</text>'
    )
    s2 = (
        f'<text id="dogru-s2" x="100" y="822" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_KART}" fill="{R["murekkep"]}" xml:space="preserve">with my uncle.</text>'
    )
    tik = (
        f'<g id="dogru-tik" transform="translate(812 716) scale(4)" fill="none" stroke="{YESIL}" '
        f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
        f'<path d="M5 12l5 5l10 -10"/>'
        f'</g>'
    )
    return f'<g id="dogru">{crv}{s1}{s2}{tik}</g>'


def yanlis_svg() -> str:
    """Yanlış şık grubu SVG çıktısı."""
    w_metin = Y.genislik("Fredoka", 700, "I live with my uncle.", BOY_YANLIS)
    x2 = 100.0 + w_metin + 8.0
    yazi = (
        f'<text id="yanlis-yazi" x="100" y="936" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_YANLIS}" fill="{R["murekkep"]}" opacity="0.45" xml:space="preserve">'
        f'I live with my uncle.</text>'
    )
    cizgi = (
        f'<path id="yanlis-cizgi" d="M92 918H{x2:.2f}" stroke="{R["ikincil"]}" '
        f'stroke-width="6" stroke-linecap="round" fill="none"/>'
    )
    return f'<g id="yanlis">{yazi}{cizgi}</g>'


def ozet_svg() -> str:
    """Kural özeti grubu SVG çıktısı."""
    return (
        f'<g id="ozet">'
        f'<text id="ozet1" x="60" y="1035" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_OZET}" fill="{R["murekkep"]}" xml:space="preserve">Kalıcıysa geniş zaman,</text>'
        f'<text id="ozet2" x="60" y="1117" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_OZET}" fill="{R["murekkep"]}" xml:space="preserve">geçiciyse şimdiki zaman.</text>'
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

    w_tr = max(
        Y.genislik("Fredoka", 700, "Şimdilik amcamla", BOY_TR),
        Y.genislik("Fredoka", 700, "yaşıyorum.", BOY_TR),
    )
    tr_y = 538.0 - 0.75 * BOY_TR
    tr_h = (622.0 + 0.25 * BOY_TR) - tr_y
    tr = {"ad": "tr", "x": 60.0, "y": tr_y, "w": w_tr, "h": tr_h}

    dogru = {"ad": "dogru", "x": 60.0, "y": 664.0, "w": 900.0, "h": 200.0}

    w_yanlis = Y.genislik("Fredoka", 700, "I live with my uncle.", BOY_YANLIS)
    x2 = 100.0 + w_yanlis + 8.0
    yanlis_y = 936.0 - 0.75 * BOY_YANLIS
    yanlis_h = 0.75 * BOY_YANLIS + 0.25 * BOY_YANLIS
    yanlis = {"ad": "yanlis", "x": 92.0, "y": yanlis_y, "w": x2 - 92.0, "h": yanlis_h}

    w_ozet = max(
        Y.genislik("Fredoka", 700, "Kalıcıysa geniş zaman,", BOY_OZET),
        Y.genislik("Fredoka", 700, "geçiciyse şimdiki zaman.", BOY_OZET),
    )
    ozet_y = 1035.0 - 0.75 * BOY_OZET
    ozet_h = (1117.0 + 0.25 * BOY_OZET) - ozet_y
    ozet = {"ad": "ozet", "x": 60.0, "y": ozet_y, "w": w_ozet, "h": ozet_h}

    hap_w = Y.genislik("Fredoka", 700, "Kaydet", BOY_KAYDET) + 80.0
    kaydet = {"ad": "kaydet", "x": 60.0, "y": 1416.0, "w": 128.0 + hap_w - 60.0, "h": 88.0}

    return [kanal, kunye, tr, dogru, yanlis, ozet, kaydet]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §5 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. tr, dogru, yanlis, ozet: x >= 60, x + w <= 960, y >= 460, y + h <= 1140
    for ad in ("tr", "dogru", "yanlis", "ozet"):
        b = b_dict[ad]
        assert b["x"] >= 60.0 - 1e-4, f"{ad} sol kenar {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ kenar {b['x'] + b['w']} > 960"
        assert b["y"] >= 460.0 - 1e-4, f"{ad} üst {b['y']} < 460"
        assert b["y"] + b["h"] <= 1140.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1140"

    # 2. kaydet: x >= 60, x + w <= 960, y >= 1400, y + h <= 1520 (1150-1380 boş, 1570-1920 boş)
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

    # 5. Dikey boşluk >= 16: kunye -> tr, tr -> dogru, dogru -> yanlis, yanlis -> ozet
    assert b_dict["tr"]["y"] - (b_dict["kunye"]["y"] + b_dict["kunye"]["h"]) >= 16.0 - 1e-4
    assert b_dict["dogru"]["y"] - (b_dict["tr"]["y"] + b_dict["tr"]["h"]) >= 16.0 - 1e-4
    assert b_dict["yanlis"]["y"] - (b_dict["dogru"]["y"] + b_dict["dogru"]["h"]) >= 16.0 - 1e-4
    assert b_dict["ozet"]["y"] - (b_dict["yanlis"]["y"] + b_dict["yanlis"]["h"]) >= 16.0 - 1e-4

    # 6. Kart içi: 100 + max(genişlik(Fredoka 700 "I am living" 72), genişlik(Fredoka 700 "with my uncle." 72)) <= 827 - 24
    w_kart_metin = max(
        Y.genislik("Fredoka", 700, "I am living", BOY_KART),
        Y.genislik("Fredoka", 700, "with my uncle.", BOY_KART),
    )
    assert 100.0 + w_kart_metin <= 827.0 - 24.0, f"Kart içi metin sağ sınırını aşıyor: {100.0 + w_kart_metin}"

    # 7. Yazı boyları (assert >= 64)
    for boy in (BOY_TR, BOY_KART, BOY_YANLIS, BOY_OZET, BOY_KAYDET):
        assert boy >= 64, f"Yazı boyu {boy} < 64"

    # 8. Ekran satırı <= 24 karakter (len)
    satirlar = [
        "Şimdilik amcamla",
        "yaşıyorum.",
        "I am living",
        "with my uncle.",
        "I live with my uncle.",
        "Kalıcıysa geniş zaman,",
        "geçiciyse şimdiki zaman.",
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
        "tr1", "tr2", "dogru-crv", "dogru-s1", "dogru-s2", "dogru-tik",
        "yanlis-yazi", "yanlis-cizgi", "ozet1", "ozet2",
        "kaydet-imi", "kaydet-hap", "kaydet-yazi",
    )
    for k in kimlikler_var:
        assert f'id="{k}"' in html, f'id="{k}" HTML içinde bulunamadı'

    kimlikler_yok = ("ku-cip", "cg1", "cg2", "hap-kutu", "soru-kutu", "kA", "kB")
    for k in kimlikler_yok:
        assert f'id="{k}"' not in html, f'id="{k}" HTML içinde olmamalı'

    # SVG içinde stroke="#167a4a" 2 kez (çerçeve + tik; CSS seçicisindeki geçiş sayılmaz), #4fbf85 1 kez
    c_yesil = html.split('<svg id="sahne"', 1)[1].count(f'stroke="{YESIL}"')
    assert c_yesil == 2, f'stroke="#167a4a" sayısı {c_yesil} != 2'
    c_yesil_koyu = html.count("#4fbf85")
    assert c_yesil_koyu == 1, f"#4fbf85 sayısı {c_yesil_koyu} != 1"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()

    kunye = Y.kunye_svg()
    tr = tr_svg()
    dogru = dogru_svg()
    yanlis = yanlis_svg()
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
{tr}
{dogru}
{yanlis}
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

#!/usr/bin/python3
"""Sahne 08 hikâye karesi B index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2 (15.11): kanal katmanı + v2 bantları (soru kartı)."""
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
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu", "kirmizi"}

W, H = Y.W, Y.H

BOY_BASLIK = 88
BOY_KOK = 64
BOY_SIK = 64
BOY_OZET = 56
BOY_KAYDET = 52
BASLIK_TABAN = 545
KOK_L1, KOK_L2 = 652, 732
BOS_W = 200
BOS_KAYMA = 6
SIK_Y = (772, 872)
SIK_H = 86
SIK_TABAN = (833, 933)
SIK_TX = 100
OZET_TABAN = 1027


def baslik_svg() -> str:
    """Başlık SVG çıktısı."""
    return (
        f'<text id="baslik" x="60" y="{BASLIK_TABAN}" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_BASLIK}" fill="{R["murekkep"]}" style="font-kerning:none">Hangisi doğru?</text>'
    )


def kok_svg() -> str:
    """Kök grubu SVG çıktısı."""
    bx0 = 60.0 + Y.genislik("Fredoka", 700, "Does she ", BOY_KOK)
    bx1 = bx0 + float(BOS_W)
    x0 = bx0 + 4.0
    x1 = bx1 - 4.0
    yb = float(KOK_L1 + BOS_KAYMA)
    xc = (x0 + x1) / 2.0
    yc = yb + 5.0
    y1 = yb + 1.0

    s1 = (
        f'<text id="kok-s1" x="60" y="{KOK_L1}" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_KOK}" fill="{R["murekkep"]}" style="font-kerning:none">Does she</text>'
    )
    bos = (
        f'<path id="kok-bos" d="M {x0:.1f} {yb:.1f} Q {xc:.1f} {yc:.1f} {x1:.1f} {y1:.1f}" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="5" stroke-linecap="round"/>'
    )
    s2 = (
        f'<text id="kok-s2" x="60" y="{KOK_L2}" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_KOK}" fill="{R["murekkep"]}" style="font-kerning:none">to school?</text>'
    )
    return f'<g id="kok">{s1}{bos}{s2}</g>'


def sik_svg(grup_id: str, y0: int, taban: int, metin: str) -> str:
    """Şık kartı SVG çıktısı."""
    crv = (
        f'<rect id="{grup_id}-crv" x="62" y="{y0 + 2}" width="896" height="{SIK_H - 4}" '
        f'rx="26" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    yazi = (
        f'<text id="{grup_id}-yazi" x="{SIK_TX}" y="{taban}" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_SIK}" fill="{R["murekkep"]}" style="font-kerning:none">{metin}</text>'
    )
    return f'<g id="{grup_id}">{crv}{yazi}</g>'


def ozet_svg() -> str:
    """Kural özeti SVG çıktısı."""
    return (
        f'<text id="ozet" x="60" y="{OZET_TABAN}" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_OZET}" fill="{R["murekkep"]}" style="font-kerning:none">Does varsa fiil yalın.</text>'
    )


def kaydet_svg() -> str:
    """Kaydet grubu SVG çıktısı."""
    hap_w = Y.genislik("Lexend", 700, "Kaydet", BOY_KAYDET) + 56.0
    imi = (
        f'<g transform="translate(39 1052) scale(4)" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round">'
        f'<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/>'
        f'</g>'
    )
    hap = f'<rect id="kaydet-hap" x="132" y="1060" width="{hap_w:.1f}" height="80" rx="40" fill="{R["vurgu"]}"/>'
    yazi = (
        f'<text id="kaydet-yazi" x="{132.0 + hap_w / 2.0:.1f}" y="1118" text-anchor="middle" '
        f'font-family="Lexend" font-weight="700" font-size="{BOY_KAYDET}" fill="{R["zemin"]}" '
        f'style="font-kerning:none">Kaydet</text>'
    )
    return f'<g id="kaydet">{imi}{hap}{yazi}</g>'


def blok_kutulari() -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    w_kanal = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - 53.2
    kanal = {"ad": "kanal", "x": 53.2, "y": 291.0, "w": w_kanal, "h": 48.0}

    rz_x, rz_w = Y.rozet_konumlari()[0]
    kunye = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": rz_x + rz_w - 60.0, "h": 48.0}

    w_baslik = Y.genislik("Fredoka", 700, "Hangisi doğru?", BOY_BASLIK)
    baslik = {"ad": "baslik", "x": 60.0, "y": 479.0, "w": w_baslik, "h": 88.0}

    bx0 = 60.0 + Y.genislik("Fredoka", 700, "Does she ", BOY_KOK)
    bx1 = bx0 + float(BOS_W)
    w_kok_s2 = Y.genislik("Fredoka", 700, "to school?", BOY_KOK)
    w_kok = max(bx1 - 60.0, w_kok_s2)
    kok = {"ad": "kok", "x": 60.0, "y": 604.0, "w": w_kok, "h": 144.0}

    sikA = {"ad": "sikA", "x": 60.0, "y": float(SIK_Y[0]), "w": 900.0, "h": float(SIK_H)}
    sikB = {"ad": "sikB", "x": 60.0, "y": float(SIK_Y[1]), "w": 900.0, "h": float(SIK_H)}

    w_ozet = Y.genislik("Fredoka", 700, "Does varsa fiil yalın.", BOY_OZET)
    ozet = {"ad": "ozet", "x": 60.0, "y": 985.0, "w": w_ozet, "h": 56.0}

    hap_w = Y.genislik("Lexend", 700, "Kaydet", BOY_KAYDET) + 56.0
    kaydet = {"ad": "kaydet", "x": 60.0, "y": 1060.0, "w": 132.0 + hap_w - 60.0, "h": 80.0}

    return [kanal, kunye, baslik, kok, sikA, sikB, ozet, kaydet]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. İçerik blokları (baslik, kok, sikA, sikB, ozet, kaydet)
    for ad in ("baslik", "kok", "sikA", "sikB", "ozet", "kaydet"):
        b = b_dict[ad]
        assert b["x"] >= 60.0 - 1e-4, f"{ad} sol kenar {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ kenar {b['x'] + b['w']} > 960"
        assert b["y"] >= 460.0 - 1e-4, f"{ad} üst {b['y']} < 460"
        assert b["y"] + b["h"] <= 1140.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1140"

    # 2. Her içerik bloğu kendi istem bandında
    bantlar = {
        "baslik": (470.0, 570.0),
        "kok": (590.0, 750.0),
        "sikA": (770.0, 860.0),
        "sikB": (870.0, 960.0),
        "ozet": (980.0, 1050.0),
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

    # 4. Bütün blok çiftlerinin kesişim alanı 0; ardışık bloklar arası dikey boşluk >= 16 (sikA -> sikB >= 12)
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    ardisik = ["kunye", "baslik", "kok", "sikA", "sikB", "ozet", "kaydet"]
    for i in range(len(ardisik) - 1):
        ust = b_dict[ardisik[i]]
        alt = b_dict[ardisik[i + 1]]
        bosluk = alt["y"] - (ust["y"] + ust["h"])
        esik = 12.0 if (ardisik[i], ardisik[i + 1]) == ("sikA", "sikB") else 16.0
        assert bosluk >= esik - 1e-4, f"{ardisik[i]} -> {ardisik[i + 1]} dikey boşluk {bosluk} < {esik}"

    # 5. Kök: boşluk çizgisinin en alt noktası < KOK_L2 - 0.75 * 64 - 12; bx1 <= 960
    bx0 = 60.0 + Y.genislik("Fredoka", 700, "Does she ", BOY_KOK)
    bx1 = bx0 + float(BOS_W)
    yb = float(KOK_L1 + BOS_KAYMA)
    cizgi_alt = yb + 5.0 + 2.5
    l2_ust = float(KOK_L2) - 0.75 * BOY_KOK
    assert cizgi_alt < l2_ust - 12.0, f"Boşluk çizgisi alt satıra fazla yakın: {cizgi_alt} >= {l2_ust - 12.0}"
    assert bx1 <= 960.0, f"bx1 {bx1} > 960"

    # 6. Şık içi: SIK_TX + genişlik <= 960 - 24; yazı kutusu kart sınırları içinde
    siklar = (("A) go", float(SIK_Y[0]), float(SIK_TABAN[0])), ("B) goes", float(SIK_Y[1]), float(SIK_TABAN[1])))
    for metin, y0, taban in siklar:
        w = Y.genislik("Fredoka", 700, metin, BOY_SIK)
        assert SIK_TX + w <= 960.0 - 24.0, f"Şık metin genişliği sınırı aşıldı: {metin}"
        assert y0 + 4.0 <= taban - 48.0, f"Şık üst boşluk yetersiz: {metin}"
        assert taban + 16.0 <= y0 + SIK_H - 4.0, f"Şık alt boşluk yetersiz: {metin}"

    # 7. Yazı boyları (sabitler)
    boylar = {
        "baslik": BOY_BASLIK,
        "kok": BOY_KOK,
        "sik": BOY_SIK,
        "ozet": BOY_OZET,
        "hap": BOY_KAYDET,
    }
    assert all(b >= 50 for b in boylar.values()), f"yazı boyu < 50: {boylar}"
    assert boylar["baslik"] >= 64 and boylar["kok"] >= 64 and boylar["sik"] >= 64, f"ana yazı < 64: {boylar}"

    # 8. Ekran satırı <= 24 karakter
    satirlar = [
        "Hangisi doğru?",
        "Does she ____",
        "to school?",
        "A) go",
        "B) goes",
        "Does varsa fiil yalın.",
        "Kaydet",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 9. Renk ve SVG karakter kontrolleri
    assert html.count(R["kirmizi"]) == 0, f"R['kirmizi'] sayısı {html.count(R['kirmizi'])} != 0"
    assert html.count(R["vurgu"]) == 2, f"R['vurgu'] sayısı {html.count(R['vurgu'])} != 2"
    assert "#167a4a" not in html, "Yeşil (#167a4a) HTML içinde olmamalı"

    svg_bas = html.find('<svg id="sahne"')
    svg_son = html.find("</svg>", svg_bas) + 6
    assert svg_bas != -1 and svg_son > svg_bas, "SVG sahne etiketi bulunamadı"
    svg_dize = html[svg_bas:svg_son]
    assert "✗" not in svg_dize, "✗ karakteri sahne SVG dizesinde olmamalı"
    assert "✓" not in svg_dize, "✓ karakteri sahne SVG dizesinde olmamalı"
    assert "_" not in svg_dize, "_ karakteri sahne SVG dizesinde olmamalı"

    # 10. HTML'de id="kanal" ve id="logoimg" tam 1 kez; #root.tema-acik 0 kez
    c_kanal = html.count('id="kanal"')
    assert c_kanal == 1, f'id="kanal" sayısı: {c_kanal}'
    c_logo = html.count('id="logoimg"')
    assert c_logo == 1, f'id="logoimg" sayısı: {c_logo}'
    assert "#root.tema-acik" not in html, "#root.tema-acik HTML içinde olmamalı"

    # 11. Var ve Yok id kontrolleri
    for var in (
        'id="baslik"',
        'id="kok-s1"',
        'id="kok-bos"',
        'id="kok-s2"',
        'id="sikA-crv"',
        'id="sikA-yazi"',
        'id="sikB-crv"',
        'id="sikB-yazi"',
        'id="ozet"',
        'id="kaydet-imi"',
        'id="kaydet-hap"',
        'id="kaydet-yazi"',
    ):
        assert var in html, f"{var} HTML içinde bulunamadı"

    for yok in (
        'id="ku-cip"',
        'id="cg1"',
        'id="cg2"',
        'id="ipucu"',
        'id="etiket"',
        'id="kart"',
        'id="dogru1"',
        'id="yanlis"',
        'id="kA"',
        'id="kB"',
    ):
        assert yok not in html, f"{yok} HTML içinde olmamalı"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()

    kunye = Y.kunye_svg()
    baslik = baslik_svg()
    kok = kok_svg()
    sikA = sik_svg("sikA", SIK_Y[0], SIK_TABAN[0], "A) go")
    sikB = sik_svg("sikB", SIK_Y[1], SIK_TABAN[1], "B) goes")
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
{baslik}
{kok}
{sikA}
{sikB}
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

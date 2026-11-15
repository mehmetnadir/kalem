#!/usr/bin/python3
"""Sahne 07 hikâye karesi B index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2 (15.11): kanal katmanı + v2 bantları (soru-cevap düzeni).
DUZ-1 (15.11): üstü çizgi kalktı (yanlış şık dilbilgisi olarak doğru); iki şık yan yana, altlarında bağlam etiketi."""
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
BOY_ETIKET = 48  # küçük etiket (Caveat 700; hikâye A kart etiketiyle aynı aile)

# İki şık yan yana (DUZ-1): sol doğru şık kartı, sağ soluk şık; satır tabanları ortak.
DOGRU_SATIR = ("I am living with", "my uncle.")
YANLIS_SATIR = ("I live with", "my uncle.")
KART_X = 100.0                      # kart içi yazı x
KART_B1, KART_B2 = 714, 794         # iki satırın tabanı (kart ve soluk şık)
KART_SAG = float(int(KART_X + max(Y.genislik("Fredoka", 700, s, BOY_KART) for s in DOGRU_SATIR) + 40.0) + 1)
YANLIS_X = KART_SAG + 28.0          # soluk şık x (kart dış kenarından 28 px)
ETIKET_B = 880                      # etiket satırı tabanı (iki etiket aynı satırda)
OZET_SATIR = ("Live, work fiillerinde:", "kalıcıysa geniş zaman,", "geçiciyse şimdiki zaman.")
OZET_B = (959, 1039, 1119)          # özet tabanları (DUZ2: 3 satır, aralık 80; alt kenar ≤ 1140)
# Tabler Icons "arrow-right" (MIT), 24x24; yol kutusu x 5-19, y 6-18. Yazı tiplerinde U+2192 yok, ok çizilir.
OK_D = "M5 12l14 0M13 18l6 -6M13 6l6 6"
OK_OLCEK = 2.0
OK_ARA = 18.0                       # ok ile yazı arası (Caveat eğik "k" ilerleme payını aşar)


def tr_svg() -> str:
    """Türkçe cümle grubu SVG çıktısı."""
    return (
        f'<g id="tr">'
        f'<text id="tr1" x="60" y="517" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_TR}" fill="{R["murekkep"]}" xml:space="preserve">Şimdilik amcamla</text>'
        f'<text id="tr2" x="60" y="601" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_TR}" fill="{R["murekkep"]}" xml:space="preserve">yaşıyorum.</text>'
        f'</g>'
    )


def dogru_svg() -> str:
    """Doğru şık kartı grubu SVG çıktısı."""
    crv = (
        f'<rect id="dogru-crv" x="63" y="639" width="{KART_SAG - 66.0:.0f}" height="194" rx="28" '
        f'fill="none" stroke="{YESIL}" stroke-width="6"/>'
    )
    s1, s2 = (
        f'<text id="dogru-s{i + 1}" x="{KART_X:.0f}" y="{b}" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_KART}" fill="{R["murekkep"]}" xml:space="preserve">{s}</text>'
        for i, (s, b) in enumerate(zip(DOGRU_SATIR, (KART_B1, KART_B2)))
    )
    tik = (
        # 2. satır hizasında, kartın sağında (görünür kutu x KART_SAG-100 .. KART_SAG-40, y 784-824)
        f'<g id="dogru-tik" transform="translate({KART_SAG - 120.0:.0f} 728) scale(4)" fill="none" stroke="{YESIL}" '
        f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
        f'<path d="M5 12l5 5l10 -10"/>'
        f'</g>'
    )
    return f'<g id="dogru">{crv}{s1}{s2}{tik}</g>'


def yanlis_svg() -> str:
    """Yanlış şık grubu SVG çıktısı."""
    s1, s2 = (
        f'<text id="yanlis-s{i + 1}" x="{YANLIS_X:.0f}" y="{b}" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_YANLIS}" fill="{R["murekkep"]}" opacity="0.45" xml:space="preserve">{s}</text>'
        for i, (s, b) in enumerate(zip(YANLIS_SATIR, (KART_B1, KART_B2)))
    )
    return f'<g id="yanlis">{s1}{s2}</g>'


def etiket_svg() -> str:
    """Şıkların altındaki bağlam etiketleri: doğru şık `şimdilik → geçici` (yeşil), soluk şık `kalıcıysa`."""
    w1 = Y.genislik("Caveat", 700, "şimdilik", BOY_ETIKET)
    ok_x = KART_X + w1 + OK_ARA - 5.0 * OK_OLCEK          # görünür ok başı = KART_X + w1 + OK_ARA
    ok_y = ETIKET_B - 0.2 * BOY_ETIKET - 12.0 * OK_OLCEK  # ok ortası x-yüksekliğinin ortasında (Caveat xh 0,4)
    x2 = KART_X + w1 + 2.0 * OK_ARA + 14.0 * OK_OLCEK
    yazi = f'font-family="Caveat" font-weight="700" font-size="{BOY_ETIKET}" xml:space="preserve"'
    dogru = (
        f'<g id="dogru-etiket" fill="{YESIL}">'
        f'<text id="dogru-et1" x="{KART_X:.0f}" y="{ETIKET_B}" {yazi}>şimdilik</text>'
        f'<path id="dogru-ok" d="{OK_D}" transform="translate({ok_x:.1f} {ok_y:.1f}) scale({OK_OLCEK:g})" '
        f'fill="none" stroke="{YESIL}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<text id="dogru-et2" x="{x2:.1f}" y="{ETIKET_B}" {yazi}>geçici</text></g>'
    )
    yanlis = (
        f'<text id="yanlis-etiket" x="{YANLIS_X:.0f}" y="{ETIKET_B}" fill="{R["ikincil"]}" {yazi}>kalıcıysa</text>'
    )
    return dogru + yanlis


def ozet_svg() -> str:
    """Kural özeti grubu SVG çıktısı."""
    # DUZ2 (15.11, J2 A3): kural fiil sınırı taşır; 3 satır (üst bloklar 28 px yukarı alındı)
    t = "".join(
        f'<text id="ozet{i}" x="60" y="{b}" font-family="Fredoka" font-weight="700" '
        f'font-size="{BOY_OZET}" fill="{R["murekkep"]}" xml:space="preserve">{s}</text>'
        for i, (s, b) in enumerate(zip(OZET_SATIR, OZET_B), 1)
    )
    return f'<g id="ozet">{t}</g>'


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
    tr_y = 517.0 - 0.75 * BOY_TR
    tr_h = (601.0 + 0.25 * BOY_TR) - tr_y
    tr = {"ad": "tr", "x": 60.0, "y": tr_y, "w": w_tr, "h": tr_h}

    dogru = {"ad": "dogru", "x": 60.0, "y": 636.0, "w": KART_SAG - 60.0, "h": 200.0}

    w_yanlis = max(Y.genislik("Fredoka", 700, s, BOY_YANLIS) for s in YANLIS_SATIR)
    yanlis_y = KART_B1 - 0.75 * BOY_YANLIS
    yanlis = {"ad": "yanlis", "x": YANLIS_X, "y": yanlis_y, "w": w_yanlis,
              "h": (KART_B2 + 0.25 * BOY_YANLIS) - yanlis_y}

    et_y, et_h = ETIKET_B - 0.75 * BOY_ETIKET, 1.0 * BOY_ETIKET
    w_et1 = Y.genislik("Caveat", 700, "şimdilik", BOY_ETIKET) + 2.0 * OK_ARA + 14.0 * OK_OLCEK \
        + Y.genislik("Caveat", 700, "geçici", BOY_ETIKET)
    dogru_et = {"ad": "dogru-etiket", "x": KART_X, "y": et_y, "w": w_et1, "h": et_h}
    yanlis_et = {"ad": "yanlis-etiket", "x": YANLIS_X, "y": et_y,
                 "w": Y.genislik("Caveat", 700, "kalıcıysa", BOY_ETIKET), "h": et_h}

    w_ozet = max(Y.genislik("Fredoka", 700, s, BOY_OZET) for s in OZET_SATIR)
    ozet_y = OZET_B[0] - 0.75 * BOY_OZET
    ozet_h = (OZET_B[-1] + 0.25 * BOY_OZET) - ozet_y
    ozet = {"ad": "ozet", "x": 60.0, "y": ozet_y, "w": w_ozet, "h": ozet_h}

    hap_w = Y.genislik("Fredoka", 700, "Kaydet", BOY_KAYDET) + 80.0
    kaydet = {"ad": "kaydet", "x": 60.0, "y": 1416.0, "w": 128.0 + hap_w - 60.0, "h": 88.0}

    return [kanal, kunye, tr, dogru, yanlis, dogru_et, yanlis_et, ozet, kaydet]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §5 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. tr, dogru, yanlis, etiketler, ozet: x >= 60, x + w <= 960, y >= 460, y + h <= 1140
    for ad in ("tr", "dogru", "yanlis", "dogru-etiket", "yanlis-etiket", "ozet"):
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

    # 5. Dikey boşluk >= 16: kunye -> tr, tr -> dogru, etiketler -> ozet; dogru -> etiket >= 8 (etiket karta ait);
    #    yatay: dogru -> yanlis >= 16; iki etiket aynı tabanda, her biri kendi şıkkının x'inden başlar
    assert b_dict["tr"]["y"] - (b_dict["kunye"]["y"] + b_dict["kunye"]["h"]) >= 16.0 - 1e-4
    assert b_dict["dogru"]["y"] - (b_dict["tr"]["y"] + b_dict["tr"]["h"]) >= 16.0 - 1e-4
    assert b_dict["dogru-etiket"]["y"] - (b_dict["dogru"]["y"] + b_dict["dogru"]["h"]) >= 8.0 - 1e-4
    assert b_dict["ozet"]["y"] - (b_dict["dogru-etiket"]["y"] + b_dict["dogru-etiket"]["h"]) >= 16.0 - 1e-4
    assert b_dict["yanlis"]["x"] - (b_dict["dogru"]["x"] + b_dict["dogru"]["w"]) >= 16.0 - 1e-4
    assert b_dict["yanlis-etiket"]["x"] == b_dict["yanlis"]["x"] and b_dict["dogru-etiket"]["x"] == KART_X

    # 6. Kart içi: yazı sağ kenarı kart dış kenarından >= 24 içeride; tik 2. satırın sağında, yazıdan >= 24 uzak
    w_kart_metin = max(Y.genislik("Fredoka", 700, s, BOY_KART) for s in DOGRU_SATIR)
    assert KART_X + w_kart_metin <= KART_SAG - 24.0, f"Kart içi metin sağ sınırını aşıyor: {KART_X + w_kart_metin}"
    w_s2 = Y.genislik("Fredoka", 700, DOGRU_SATIR[1], BOY_KART)
    assert KART_X + w_s2 <= KART_SAG - 100.0 - 24.0, "tik 2. satıra değiyor"

    # 7. Yazı boyları (assert >= 64; etiket küçük, >= 44)
    for boy in (BOY_TR, BOY_KART, BOY_YANLIS, BOY_OZET, BOY_KAYDET):
        assert boy >= 64, f"Yazı boyu {boy} < 64"
    assert BOY_ETIKET >= 44, f"Etiket boyu {BOY_ETIKET} < 44"

    # 8. Ekran satırı <= 24 karakter (len)
    satirlar = [
        "Şimdilik amcamla",
        "yaşıyorum.",
        *DOGRU_SATIR,
        *YANLIS_SATIR,
        "şimdilik",
        "geçici",
        "kalıcıysa",
        *OZET_SATIR,
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
        "yanlis-s1", "yanlis-s2", "dogru-etiket", "dogru-et1", "dogru-ok", "dogru-et2", "yanlis-etiket",
        "ozet1", "ozet2", "kaydet-imi", "kaydet-hap", "kaydet-yazi",
    )
    for k in kimlikler_var:
        assert f'id="{k}"' in html, f'id="{k}" HTML içinde bulunamadı'

    # DUZ-1: üstü çizgi yok (yanlış şık dilbilgisi olarak doğru; yalnız bağlama uymuyor)
    kimlikler_yok = ("ku-cip", "cg1", "cg2", "hap-kutu", "soru-kutu", "kA", "kB", "yanlis-yazi", "yanlis-cizgi")
    for k in kimlikler_yok:
        assert f'id="{k}"' not in html, f'id="{k}" HTML içinde olmamalı'

    # SVG içinde stroke="#167a4a" 3 kez (çerçeve + tik + ok), fill="#167a4a" 1 kez (etiket grubu);
    # CSS seçicilerindeki geçiş sayılmaz. #4fbf85 2 kez (stroke + fill kuralı)
    svg = html.split('<svg id="sahne"', 1)[1]
    c_yesil = svg.count(f'stroke="{YESIL}"')
    assert c_yesil == 3, f'stroke="#167a4a" sayısı {c_yesil} != 3'
    assert svg.count(f'fill="{YESIL}"') == 1, 'fill="#167a4a" sayısı != 1'
    c_yesil_koyu = html.count("#4fbf85")
    assert c_yesil_koyu == 2, f"#4fbf85 sayısı {c_yesil_koyu} != 2"
    assert "line-through" not in html, "üstü çizgi biçemi olmamalı"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()

    kunye = Y.kunye_svg()
    tr = tr_svg()
    dogru = dogru_svg()
    yanlis = yanlis_svg()
    etiket = etiket_svg()
    ozet = ozet_svg()
    kaydet = kaydet_svg()

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
#root:not(.tema-acik) [stroke="{YESIL}"]{{stroke:{YESIL_KOYU}}}
#root:not(.tema-acik) [fill="{YESIL}"]{{fill:{YESIL_KOYU}}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}"
     data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{tr}
{dogru}
{yanlis}
{etiket}
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

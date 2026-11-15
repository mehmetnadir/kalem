#!/usr/bin/python3
"""Sahne 07 hikâye karesi B (soru kartı) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> içerik (352-1392) -> çağrı (1344-1536) -> platform (1536-1920 boş)."""
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
assert len(duragan_kayitlar) == 1, f"duragan listesinde {AD.name} olan tek kayıt olmalı, bulunan: {len(duragan_kayitlar)}"
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
assert R["zemin"] == "#1b1a17"
assert R["murekkep"] == "#f3efe6"
assert R["ikincil"] == "#c9c2b3"
assert R["vurgu"] == "#f2a93b"

W, H = Y.W, Y.H
KENAR = 48
SAG = 1032
ICERIK = (352, 1392)
CAGRI = (1344, 1536)
PLATFORM = 1536
KART_H = 260


def kunye_svg() -> str:
    """Künye (HUD) grubu SVG çıktısı."""
    logo_w = 96.0 * Y.LOGO_EN_BOY
    logo = f'<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" width="{logo_w:.2f}" height="96"/></g>'
    ders1 = f'<text id="ku-ders1" x="48" y="212" font-family="Fredoka" font-weight="700" font-size="56" fill="{R["murekkep"]}" xml:space="preserve">SIMPLE PRESENT vs</text>'
    ders2 = f'<text id="ku-ders2" x="48" y="276" font-family="Fredoka" font-weight="700" font-size="56" fill="{R["murekkep"]}" xml:space="preserve">PRESENT CONTINUOUS</text>'

    ders2_w = Y.genislik("Fredoka", 700, "PRESENT CONTINUOUS", 56)
    rz_w = Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56.0
    rz_x = 48.0 + ders2_w + 24.0
    rozet = (
        f'<g id="rz0">'
        f'<rect x="{rz_x:.1f}" y="216" width="{rz_w:.1f}" height="72" rx="36" fill="{R["vurgu"]}"/>'
        f'<text x="{rz_x + rz_w / 2.0:.1f}" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" fill="{R["zemin"]}">YDT · BASIC</text>'
        f'</g>'
    )

    cip_metin = "Quiz"
    cip_w = Y.genislik("Lexend", 700, cip_metin, 40) + 64.0
    cip_x = 1032.0 - cip_w
    cip = (
        f'<g id="ku-cip">'
        f'<rect id="ku-cipr" x="{cip_x:.1f}" y="48" width="{cip_w:.1f}" height="80" rx="40" fill="none" stroke="{R["vurgu"]}" stroke-width="4"/>'
        f'<text id="ku-cipt" x="{cip_x + cip_w / 2.0:.1f}" y="102" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="40" fill="{R["vurgu"]}">{cip_metin}</text>'
        f'</g>'
    )
    return f'<g id="kunye">{logo}{ders1}{ders2}{rozet}{cip}</g>'


def soru_svg(soru_w: float) -> str:
    """Soru hapı grubu SVG çıktısı."""
    kutu = (
        f'<rect id="soru-kutu" x="48" y="596" width="{soru_w:.1f}" height="84" rx="42" '
        f'fill="{R["vurgu"]}"/>'
    )
    yazi = (
        f'<text id="soru-yazi" x="{48.0 + soru_w / 2.0:.1f}" y="660" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{R["zemin"]}" '
        f'xml:space="preserve">Hangisi doğru?</text>'
    )
    return f'<g id="soru">{kutu}{yazi}</g>'


def secenek_karti_svg(grup_id: str, y0: int, harf: str, satir1: str, satir2: str) -> str:
    """Seçenek kartı grubu SVG çıktısı (kA ya da kB)."""
    crv = (
        f'<rect id="{grup_id}-crv" x="48" y="{y0}" width="984" height="{KART_H}" rx="28" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    daire = (
        f'<circle id="{grup_id}-daire" cx="136" cy="{y0 + 130}" r="52" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    harf_yazi = (
        f'<text id="{grup_id}-harf" x="136" y="{y0 + 152}" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{R["murekkep"]}" '
        f'xml:space="preserve">{harf}</text>'
    )
    s1 = (
        f'<text id="{grup_id}-s1" x="228" y="{y0 + 112}" '
        f'font-family="Fredoka" font-weight="700" font-size="72" fill="{R["murekkep"]}" '
        f'xml:space="preserve">{satir1}</text>'
    )
    s2 = (
        f'<text id="{grup_id}-s2" x="228" y="{y0 + 202}" '
        f'font-family="Fredoka" font-weight="700" font-size="72" fill="{R["murekkep"]}" '
        f'xml:space="preserve">{satir2}</text>'
    )
    return f'<g id="{grup_id}">{crv}{daire}{harf_yazi}{s1}{s2}</g>'


def blok_kutulari() -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    hud = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}

    # tr: tr1 + tr2
    # Fredoka 700 88: y_üst = taban - 0.75 * boy, y_alt = taban + 0.25 * boy
    w_tr1 = Y.genislik("Fredoka", 700, "Şimdilik amcamla", 88)
    w_tr2 = Y.genislik("Fredoka", 700, "yaşıyorum.", 88)
    tr_y_ust = 440.0 - 0.75 * 88.0
    tr_y_alt = 540.0 + 0.25 * 88.0
    tr = {
        "ad": "tr",
        "x": 48.0,
        "y": tr_y_ust,
        "w": max(w_tr1, w_tr2),
        "h": tr_y_alt - tr_y_ust,
    }

    # soru: hap
    w_soru = Y.genislik("Fredoka", 700, "Hangisi doğru?", 64) + 56.0
    soru = {"ad": "soru", "x": 48.0, "y": 596.0, "w": w_soru, "h": 84.0}

    # kA ve kB kartları
    kA = {"ad": "kA", "x": 48.0, "y": 716.0, "w": 984.0, "h": float(KART_H)}
    kB = {"ad": "kB", "x": 48.0, "y": 1008.0, "w": 984.0, "h": float(KART_H)}

    # cg1 ve cg2: Caveat 700 72
    # y_üst = taban - 0.75 * boy, y_alt = taban + 0.30 * boy
    w_cg1 = Y.genislik("Caveat", 700, "Cevap tam derste:", 72)
    cg1 = {
        "ad": "cg1",
        "x": 48.0,
        "y": 1418.0 - 0.75 * 72.0,
        "w": w_cg1,
        "h": (0.75 + 0.30) * 72.0,
    }

    w_cg2 = Y.genislik("Caveat", 700, "profildeki bağlantı", 72)
    cg2 = {
        "ad": "cg2",
        "x": 48.0,
        "y": 1498.0 - 0.75 * 72.0,
        "w": w_cg2,
        "h": (0.75 + 0.30) * 72.0,
    }

    # hap: @ydspublishing
    w_hap = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap = {
        "ad": "hap",
        "x": 1032.0 - w_hap,
        "y": 1398.0,
        "w": w_hap,
        "h": 84.0,
    }

    return [hud, tr, soru, kA, kB, cg1, cg2, hap]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]]) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Bütün metin ve kutular x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil
    for b in bloklar:
        assert b["x"] >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0, f"{b['ad']} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1536.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1536"

    # Yazı alt sınırları kontrolü (taban + 0.30*boy <= 1536)
    yazilar: list[tuple[str, float, float]] = [
        ("tr1", 440.0, 88.0),
        ("tr2", 540.0, 88.0),
        ("soru", 660.0, 64.0),
        ("kA-harf", 868.0, 64.0),
        ("kA-s1", 828.0, 72.0),
        ("kA-s2", 918.0, 72.0),
        ("kB-harf", 1160.0, 64.0),
        ("kB-s1", 1120.0, 72.0),
        ("kB-s2", 1210.0, 72.0),
        ("cg1", 1418.0, 72.0),
        ("cg2", 1498.0, 72.0),
        ("hap", 1462.0, 64.0),
    ]
    for ad, taban, boy in yazilar:
        assert taban + 0.30 * boy <= 1536.0 + 1e-4, f"{ad} yazı alt sınırı > 1536"

    # 2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40)
    for ad, _, boy in yazilar:
        assert boy >= 64.0, f"{ad} yazı boyu {boy} < 64"

    # 3. Her ekran satırı ≤ 24 karakter (len), HUD dahil
    satirlar = [
        "SIMPLE PRESENT vs",
        "PRESENT CONTINUOUS",
        "YDT · BASIC",
        "Quiz",
        "Şimdilik amcamla",
        "yaşıyorum.",
        "Hangisi doğru?",
        "A",
        "B",
        "I live",
        "I am living",
        "with my uncle.",
        "Cevap tam derste:",
        "profildeki bağlantı",
        "@ydspublishing",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 4. Blok kutuları çakışmaz (kesişim alanı 0)
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    # Dikey komşular arası boşluk ≥ 16 (istisna: cg1–cg2, yalnız kesişim 0)
    dikey_sirali = ["hud", "tr", "soru", "kA", "kB"]
    for i in range(len(dikey_sirali) - 1):
        b1 = b_dict[dikey_sirali[i]]
        b2 = b_dict[dikey_sirali[i + 1]]
        bosluk = b2["y"] - (b1["y"] + b1["h"])
        assert bosluk >= 16.0, f"Dikey boşluk {b1['ad']} -> {b2['ad']}: {bosluk} < 16"

    assert b_dict["cg1"]["y"] - (b_dict["kB"]["y"] + b_dict["kB"]["h"]) >= 16.0
    assert b_dict["hap"]["y"] - (b_dict["kB"]["y"] + b_dict["kB"]["h"]) >= 16.0

    # cg1 ve cg2 dikey kesişimi 0
    assert kesisim(b_dict["cg1"], b_dict["cg2"]) == 0.0, "cg1 ve cg2 çakışıyor"

    # cg1 ve cg2 sağ kenarı ile hap sol kenarı arası ≥ 24
    assert b_dict["hap"]["x"] - (b_dict["cg1"]["x"] + b_dict["cg1"]["w"]) >= 24.0
    assert b_dict["hap"]["x"] - (b_dict["cg2"]["x"] + b_dict["cg2"]["w"]) >= 24.0

    # Kart içi: satır 1 ve satır 2 sağ kenarı ≤ 1000; harf dairesi sağı (188) ile yazı solu (228) arası ≥ 24
    assert 228.0 - 188.0 >= 24.0, "Harf dairesi sağı ile yazı solu arası < 24"
    for kart_s1 in ("I live", "I am living"):
        w = Y.genislik("Fredoka", 700, kart_s1, 72)
        assert 228.0 + w <= 1000.0, f"Kart satır 1 sağı {228.0 + w} > 1000: {kart_s1}"
    w_s2 = Y.genislik("Fredoka", 700, "with my uncle.", 72)
    assert 228.0 + w_s2 <= 1000.0, f"Kart satır 2 sağı {228.0 + w_s2} > 1000"

    # 5. tr üstü ≥ 352; kB altı ≤ 1344; hap, cg1, cg2 [1344, 1536] içinde
    assert b_dict["tr"]["y"] >= 352.0, f"tr üstü {b_dict['tr']['y']} < 352"
    assert b_dict["kB"]["y"] + b_dict["kB"]["h"] <= 1344.0, f"kB altı {b_dict['kB']['y'] + b_dict['kB']['h']} > 1344"
    for ad in ("hap", "cg1", "cg2"):
        assert b_dict[ad]["y"] >= 1344.0, f"{ad} üstü {b_dict[ad]['y']} < 1344"
        assert b_dict[ad]["y"] + b_dict[ad]["h"] <= 1536.0, f"{ad} altı {b_dict[ad]['y'] + b_dict[ad]['h']} > 1536"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()
    kurallari_dogrula(bloklar)

    kunye = kunye_svg()
    tr1 = f'<text id="tr1" x="48" y="440" font-family="Fredoka" font-weight="700" font-size="88" fill="{R["murekkep"]}" xml:space="preserve">Şimdilik amcamla</text>'
    tr2 = f'<text id="tr2" x="48" y="540" font-family="Fredoka" font-weight="700" font-size="88" fill="{R["murekkep"]}" xml:space="preserve">yaşıyorum.</text>'

    soru_w = Y.genislik("Fredoka", 700, "Hangisi doğru?", 64) + 56.0
    soru = soru_svg(soru_w)

    kA = secenek_karti_svg("kA", 716, "A", "I live", "with my uncle.")
    kB = secenek_karti_svg("kB", 1008, "B", "I am living", "with my uncle.")

    cg1 = f'<text id="cg1" x="48" y="1418" font-family="Caveat" font-weight="700" font-size="72" fill="{R["murekkep"]}" xml:space="preserve">Cevap tam derste:</text>'
    cg2 = f'<text id="cg2" x="48" y="1498" font-family="Caveat" font-weight="700" font-size="72" fill="{R["murekkep"]}" xml:space="preserve">profildeki bağlantı</text>'

    hap_w = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap_x = 1032.0 - hap_w
    hap = (
        f'<g id="hap">'
        f'<rect id="hap-kutu" x="{hap_x:.1f}" y="1398" width="{hap_w:.1f}" height="84" rx="42" fill="{R["vurgu"]}"/>'
        f'<text id="hap-yazi" x="{hap_x + hap_w / 2.0:.1f}" y="1462" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="64" fill="{R["zemin"]}" xml:space="preserve">@ydspublishing</text>'
        f'</g>'
    )

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{tr1}
{tr2}
{soru}
{kA}
{kB}
{cg1}
{cg2}
{hap}
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

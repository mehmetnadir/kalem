#!/usr/bin/python3
"""Sahne 04 hikâye karesi index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> içerik (352-1392) -> çağrı (1344-1536) -> platform (1536-1920 boş)."""
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
KENAR = 48
SAG = W - KENAR
GEN = W - 2 * KENAR
ICERIK = (352, 1392)
CAGRI = (1344, 1536)
PLATFORM = 1536

NOW_X = 540
KART_H = 236
EK_Y = 620

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
    top100 = wa0 + wt0 + ara0 + 2.0 * p0 + wy0 + ara0 + wt0 + ara0 + wu0   # QA tur 1: tire 2 UM'ye yapışıktı
    S = min(170, int(math.floor(952.0 * 100.0 / top100)))

    wa = Y.genislik("Fredoka", 700, "YAŞI", S)
    wt = Y.genislik("Fredoka", 700, "-", S)
    wy = Y.genislik("Fredoka", 700, "YOR", S)
    wu = Y.genislik("Fredoka", 700, "UM", S)
    p = 0.14 * S
    ara = 0.08 * S
    top = wa + wt + ara + 2.0 * p + wy + ara + wt + ara + wu
    while top > 952.0 and S > 1:
        S -= 1
        wa = Y.genislik("Fredoka", 700, "YAŞI", S)
        wt = Y.genislik("Fredoka", 700, "-", S)
        wy = Y.genislik("Fredoka", 700, "YOR", S)
        wu = Y.genislik("Fredoka", 700, "UM", S)
        p = 0.14 * S
        ara = 0.08 * S
        top = wa + wt + ara + 2.0 * p + wy + ara + wt + ara + wu
    assert top <= 952.0, f"top={top} > 952"
    return S, top, wa, wt, wy, wu, p, ara


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

    cip_metin = "Full lesson"
    cip_w = Y.genislik("Lexend", 700, cip_metin, 40) + 64.0
    cip_x = 1032.0 - cip_w
    cip = (
        f'<g id="ku-cip">'
        f'<rect id="ku-cipr" x="{cip_x:.1f}" y="48" width="{cip_w:.1f}" height="80" rx="40" fill="none" stroke="{R["vurgu"]}" stroke-width="4"/>'
        f'<text id="ku-cipt" x="{cip_x + cip_w / 2.0:.1f}" y="102" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="40" fill="{R["vurgu"]}">{cip_metin}</text>'
        f'</g>'
    )
    return f'<g id="kunye">{logo}{ders1}{ders2}{rozet}{cip}</g>'


def ek_svg(S: int, top: float, wa: float, wt: float, wy: float, wu: float, p: float, ara: float) -> str:
    """YAŞI-YOR-UM grubu SVG çıktısı."""
    x0 = 540.0 - top / 2.0
    kx0 = x0 + wa + wt + ara
    kx1 = kx0 + 2.0 * p + wy
    kw = kx1 - kx0
    ky = EK_Y - 0.86 * S
    kh = (0.86 + 0.16) * S
    krx = 0.10 * S

    return (
        f'<g id="ek">'
        f'<rect id="ek-kutu" x="{kx0:.2f}" y="{ky:.2f}" width="{kw:.2f}" height="{kh:.2f}" rx="{krx:.2f}" fill="{R["vurgu"]}"/>'
        f'<text id="ek-yasi" x="{x0:.2f}" y="{EK_Y}" font-family="Fredoka" font-weight="700" font-size="{S}" fill="{R["murekkep"]}" xml:space="preserve">YAŞI</text>'
        f'<text id="ek-tire1" x="{x0 + wa:.2f}" y="{EK_Y}" font-family="Fredoka" font-weight="700" font-size="{S}" fill="{R["ikincil"]}" xml:space="preserve">-</text>'
        f'<text id="ek-yor" x="{kx0 + p:.2f}" y="{EK_Y}" font-family="Fredoka" font-weight="700" font-size="{S}" fill="{R["zemin"]}" xml:space="preserve">YOR</text>'
        f'<text id="ek-tire2" x="{kx1 + ara:.2f}" y="{EK_Y}" font-family="Fredoka" font-weight="700" font-size="{S}" fill="{R["ikincil"]}" xml:space="preserve">-</text>'
        f'<text id="ek-um" x="{kx1 + 2.0 * ara + wt:.2f}" y="{EK_Y}" font-family="Fredoka" font-weight="700" font-size="{S}" fill="{R["murekkep"]}" xml:space="preserve">UM</text>'
        f'</g>'
    )


def kart_svg(simge: str, y0: int, ikon_yollar: list[str], baslik: str, odak_soz: str, etiket: str, bant_x: float, bant_w: float) -> str:
    """Kart grubu SVG çıktısı."""
    crv = f'<rect id="{simge}-crv" x="48" y="{y0}" width="984" height="{KART_H}" rx="28" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'

    scale_f = 128.0 / 24.0
    sw = 4.0 / scale_f
    paths = "".join(f'<path d="{d}"/>' for d in ikon_yollar)
    ikon = (
        f'<g id="{simge}-ikon" transform="translate(80 {y0 + 28}) scale({scale_f:.6f})" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="{sw:.4f}" stroke-linecap="round" stroke-linejoin="round">'
        f'{paths}'
        f'</g>'
    )

    y_yazi = y0 + 118
    txt = f'<text id="{simge}-baslik" x="240" y="{y_yazi}" font-family="Fredoka" font-weight="700" font-size="80" fill="{R["murekkep"]}" xml:space="preserve">{baslik}</text>'

    sol_odak = 240.0 + Y.genislik("Fredoka", 700, "I ", 80)
    w_odak = Y.genislik("Fredoka", 700, odak_soz, 80)
    x0_c = sol_odak - 4.0
    x1_c = sol_odak + w_odak + 4.0
    y_c = y_yazi + 0.48 * 80   # sözleşme 14.11: Fredoka altçizgi taban + 0,48 × boy (g kuyruğuna değmez)
    orta_c = (x0_c + x1_c) / 2.0
    d_c = f"M{x0_c:.1f} {y_c:.1f} Q{orta_c:.1f} {y_c + 3.0:.1f} {x1_c:.1f} {y_c + 1.0:.1f}"
    odak = f'<path id="{simge}-odak" d="{d_c}" fill="none" stroke="{R["vurgu"]}" stroke-width="8" stroke-linecap="round"/>'

    etk = f'<text id="{simge}-etiket" x="980" y="{y_yazi}" text-anchor="end" font-family="Caveat" font-weight="700" font-size="64" fill="{R["murekkep"]}">{etiket}</text>'

    y_eksen = y0 + 190
    dx = 20.0 * math.cos(0.5)
    dy = 20.0 * math.sin(0.5)
    d_eksen = f"M80 {y_eksen} L988 {y_eksen} M{988 - dx:.1f} {y_eksen - dy:.1f} L988 {y_eksen} L{988 - dx:.1f} {y_eksen + dy:.1f}"
    eksen = f'<path id="{simge}-eksen" d="{d_eksen}" fill="none" stroke="{R["ikincil"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'

    bant = f'<rect id="{simge}-bant" x="{bant_x}" y="{y0 + 176}" width="{bant_w}" height="28" rx="14" fill="{R["vurgu"]}" stroke="{R["vurgu"]}" stroke-width="4"/>'
    now = f'<circle id="{simge}-now" cx="{NOW_X}" cy="{y_eksen}" r="14" fill="{R["murekkep"]}"/>'

    return f'<g id="{simge}">{crv}{ikon}{txt}{odak}{etk}{eksen}{bant}{now}</g>'


def blok_kutulari(S: int, top: float) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    hud = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}
    w_ust = Y.genislik("Lexend", 500, "Türkçede tek sözcük", 64)
    ust = {"ad": "ust", "x": 48.0, "y": 424.0 - 0.75 * 64.0, "w": w_ust, "h": (0.75 + 0.25) * 64.0}

    ek_y_ust = min(620.0 - 0.86 * S, 620.0 - 0.75 * S)
    ek_y_alt = max(620.0 + 0.16 * S, 620.0 + 0.25 * S)
    ek = {"ad": "ek", "x": 540.0 - top / 2.0, "y": ek_y_ust, "w": top, "h": ek_y_alt - ek_y_ust}

    kart1 = {"ad": "kart1", "x": 48.0, "y": 690.0, "w": 984.0, "h": 236.0}
    kart2 = {"ad": "kart2", "x": 48.0, "y": 950.0, "w": 984.0, "h": 236.0}

    w_alt = Y.genislik("Lexend", 500, "İngilizcede iki zaman", 64)
    alt = {"ad": "alt", "x": 48.0, "y": 1280.0 - 0.75 * 64.0, "w": w_alt, "h": (0.75 + 0.25) * 64.0}

    w_cg1 = Y.genislik("Caveat", 700, "Tam ders:", 72)
    cg1 = {"ad": "cg1", "x": 48.0, "y": 1418.0 - 0.75 * 72.0, "w": w_cg1, "h": (0.75 + 0.30) * 72.0}

    w_cg2 = Y.genislik("Caveat", 700, "profildeki bağlantı", 72)
    cg2 = {"ad": "cg2", "x": 48.0, "y": 1498.0 - 0.75 * 72.0, "w": w_cg2, "h": (0.75 + 0.30) * 72.0}

    w_hap = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap = {"ad": "hap", "x": 1032.0 - w_hap, "y": 1398.0, "w": w_hap, "h": 84.0}

    return [hud, ust, ek, kart1, kart2, alt, cg1, cg2, hap]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], S: int) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Bütün metin ve kutular x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil
    for b in bloklar:
        assert b["x"] >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0, f"{b['ad']} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1536.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1536"

    # Yazı alt sınırları kontrolü (taban + 0.30*boy)
    assert 1498.0 + 0.30 * 72.0 <= 1536.0, "cg2 yazı alt sınırı > 1536"

    # 2. Yazı boyu ≥ 64 (HUD hariç)
    assert S >= 64, f"ek boyutu {S} < 64"

    # 3. Her ekran satırı ≤ 24 karakter (len), HUD dahil
    satirlar = [
        "SIMPLE PRESENT vs",
        "PRESENT CONTINUOUS",
        "YDT · BASIC",
        "Full lesson",
        "Türkçede tek sözcük",
        "YAŞI-YOR-UM",
        "I live",
        "PERMANENT",
        "I am living",
        "TEMPORARY",
        "İngilizcede iki zaman",
        "Tam ders:",
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

    # Dikey komşular arası boşluk ≥ 16
    dikey_sirali = ["hud", "ust", "ek", "kart1", "kart2", "alt"]
    for i in range(len(dikey_sirali) - 1):
        b1 = b_dict[dikey_sirali[i]]
        b2 = b_dict[dikey_sirali[i + 1]]
        bosluk = b2["y"] - (b1["y"] + b1["h"])
        assert bosluk >= 16.0, f"Dikey boşluk {b1['ad']} -> {b2['ad']}: {bosluk} < 16"

    assert b_dict["cg1"]["y"] - (b_dict["alt"]["y"] + b_dict["alt"]["h"]) >= 16.0
    assert b_dict["hap"]["y"] - (b_dict["alt"]["y"] + b_dict["alt"]["h"]) >= 16.0

    # cg1 ve cg2 sağ kenarı ile hap sol kenarı arası ≥ 24
    assert b_dict["hap"]["x"] - (b_dict["cg1"]["x"] + b_dict["cg1"]["w"]) >= 24.0
    assert b_dict["hap"]["x"] - (b_dict["cg2"]["x"] + b_dict["cg2"]["w"]) >= 24.0

    # 5. İçerik ilk bloğu ust üstü ≥ 352; alt altı ≤ 1344; hap, cg1, cg2 [1344, 1536] içinde
    assert b_dict["ust"]["y"] >= 352.0, f"ust üstü {b_dict['ust']['y']} < 352"
    assert b_dict["alt"]["y"] + b_dict["alt"]["h"] <= 1344.0, f"alt altı {b_dict['alt']['y'] + b_dict['alt']['h']} > 1344"
    for ad in ("hap", "cg1", "cg2"):
        assert b_dict[ad]["y"] >= 1344.0, f"{ad} üstü {b_dict[ad]['y']} < 1344"
        assert b_dict[ad]["y"] + b_dict[ad]["h"] <= 1536.0, f"{ad} altı {b_dict[ad]['y'] + b_dict[ad]['h']} > 1536"


def uret() -> tuple[str, int, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    S, top, wa, wt, wy, wu, p, ara = hesapla_s_ve_ek()
    bloklar = blok_kutulari(S, top)
    kurallari_dogrula(bloklar, S)

    kunye = kunye_svg()
    ek = ek_svg(S, top, wa, wt, wy, wu, p, ara)
    kart1 = kart_svg("kart1", 690, Y.tabler("home"), "I live", "live", "PERMANENT", 104.0, 824.0)
    kart2 = kart_svg("kart2", 950, BAVUL, "I am living", "am living", "TEMPORARY", 440.0, 200.0)

    ust = f'<text id="ust" x="48" y="424" font-family="Lexend" font-weight="500" font-size="64" fill="{R["murekkep"]}">Türkçede tek sözcük</text>'
    alt = f'<text id="alt" x="48" y="1280" font-family="Lexend" font-weight="500" font-size="64" fill="{R["murekkep"]}">İngilizcede iki zaman</text>'
    cg1 = f'<text id="cg1" x="48" y="1418" font-family="Caveat" font-weight="700" font-size="72" fill="{R["murekkep"]}">Tam ders:</text>'
    cg2 = f'<text id="cg2" x="48" y="1498" font-family="Caveat" font-weight="700" font-size="72" fill="{R["murekkep"]}">profildeki bağlantı</text>'

    hap_w = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap_x = 1032.0 - hap_w
    hap = (
        f'<g id="hap">'
        f'<rect id="hap-kutu" x="{hap_x:.1f}" y="1398" width="{hap_w:.1f}" height="84" rx="42" fill="{R["vurgu"]}"/>'
        f'<text id="hap-yazi" x="{hap_x + hap_w / 2.0:.1f}" y="1462" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="64" fill="{R["zemin"]}">@ydspublishing</text>'
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
{ust}
{ek}
{kart1}
{kart2}
{alt}
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

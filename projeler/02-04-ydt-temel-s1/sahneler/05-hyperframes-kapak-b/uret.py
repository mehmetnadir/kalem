#!/usr/bin/python3
"""02-04-ydt-temel-s1 sahne 05 kapak B (soru) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).

Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> başlık -> sahne (844-1344) -> platform (1536-1920 boş).
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# 1. zaman.json ve zamanlar.json okuma ve doğrulama (§3)
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

# 2. Renk ve sabitler (§3)
R: dict[str, str] = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

W: int = Y.W
H: int = Y.H
KENAR: int = 48
SAG: int = 1032
BASLIK_GEN: int = 952
ZEMIN_Y: int = 1344
PLATFORM: int = 1536

FIG: dict = json.loads((AD / "cizim" / "ogretmen.json").read_text(encoding="utf-8"))


def hesapla_s() -> tuple[int, float, float, float, float, float, float, float, float, float, float]:
    """Başlık font boyutu S ve yerleşim koordinatlarını hesaplar."""
    s0: float = 100.0
    wa0: float = Y.genislik("Fredoka", 700, "YAŞI", s0)
    wy0: float = Y.genislik("Fredoka", 700, "YOR", s0)
    wu0: float = Y.genislik("Fredoka", 700, "UM", s0)
    p0: float = 0.08 * s0
    g1_100: float = wa0 + 2.0 * p0 + wy0 + wu0
    g2_100: float = Y.genislik("Fredoka", 700, "NASIL DENİR?", s0)
    S: int = math.floor(min(190.0, BASLIK_GEN * 100.0 / g1_100, BASLIK_GEN * 100.0 / g2_100))

    wa: float = Y.genislik("Fredoka", 700, "YAŞI", S)
    wy: float = Y.genislik("Fredoka", 700, "YOR", S)
    wu: float = Y.genislik("Fredoka", 700, "UM", S)
    p: float = 0.08 * S
    g1: float = wa + 2.0 * p + wy + wu
    g2: float = Y.genislik("Fredoka", 700, "NASIL DENİR?", S)

    while (g1 > BASLIK_GEN or g2 > BASLIK_GEN) and S > 1:
        S -= 1
        wa = Y.genislik("Fredoka", 700, "YAŞI", S)
        wy = Y.genislik("Fredoka", 700, "YOR", S)
        wu = Y.genislik("Fredoka", 700, "UM", S)
        p = 0.08 * S
        g1 = wa + 2.0 * p + wy + wu
        g2 = Y.genislik("Fredoka", 700, "NASIL DENİR?", S)

    assert g1 <= BASLIK_GEN, f"g1={g1} > {BASLIK_GEN}"
    assert g2 <= BASLIK_GEN, f"g2={g2} > {BASLIK_GEN}"

    T1: float = 375.0 + 0.70 * S
    T2: float = T1 + 1.26 * S
    x1: float = 540.0 - g1 / 2.0
    x2: float = 540.0 - g2 / 2.0

    return S, g1, g2, wa, wy, wu, p, T1, T2, x1, x2


def hesapla_tb() -> tuple[int, float, float]:
    """Balon font boyutu TB ve metin genişliklerini hesaplar."""
    w100: float = Y.genislik("Caveat", 700, "I am living?", 100.0)
    TB: int = min(88, math.floor((SAG - 32.0 - 528.0) * 100.0 / w100))
    assert TB >= 72, f"TB={TB} < 72"
    w_b1: float = Y.genislik("Caveat", 700, "I live?", TB)
    w_b2: float = Y.genislik("Caveat", 700, "I am living?", TB)
    assert 528.0 + w_b1 <= 1000.0, f"Balon 1 sağ kenar {528.0 + w_b1} > 1000"
    assert 528.0 + w_b2 <= 1000.0, f"Balon 2 sağ kenar {528.0 + w_b2} > 1000"
    return TB, w_b1, w_b2


def kunye_svg() -> str:
    """HUD (<g id="kunye">) SVG çıktısı (§4.1)."""
    logo_w: float = 96.0 * Y.LOGO_EN_BOY
    logo: str = f'<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" width="{logo_w:.2f}" height="96"/></g>'
    rz_w: float = Y.genislik("Lexend", 700, "YDT · BASIC", 36.0) + 56.0
    rz_x: float = 48.0
    rz_ortax: float = rz_x + rz_w / 2.0
    rozet: str = (
        f'<g id="rz0">'
        f'<rect x="{rz_x:.1f}" y="216" width="{rz_w:.1f}" height="72" rx="36" fill="{R["vurgu"]}"/>'
        f'<text x="{rz_ortax:.1f}" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" fill="{R["zemin"]}">YDT · BASIC</text>'
        f'</g>'
    )
    return f'<g id="kunye">{logo}{rozet}</g>'


def baslik_svg(S: int, wa: float, wy: float, wu: float, p: float, T1: float, T2: float, x1: float, x2: float) -> str:
    """Başlık (<g id="baslik">) SVG çıktısı (§4.2)."""
    kx0: float = x1 + wa
    kx1: float = kx0 + 2.0 * p + wy
    kw: float = kx1 - kx0
    ky: float = T1 - 0.86 * S
    kh: float = (0.86 + 0.16) * S
    krx: float = 0.10 * S

    bk_kutu: str = (
        f'<rect id="bk-kutu" x="{kx0:.2f}" y="{ky:.2f}" width="{kw:.2f}" height="{kh:.2f}" '
        f'rx="{krx:.2f}" fill="{R["vurgu"]}"/>'
    )
    bs_yasi: str = (
        f'<text id="bs-yasi" x="{x1:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">YAŞI</text>'
    )
    bs_yor: str = (
        f'<text id="bs-yor" x="{kx0 + p:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["zemin"]}" style="font-kerning:none" xml:space="preserve">YOR</text>'
    )
    bs_um: str = (
        f'<text id="bs-um" x="{kx1:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">UM</text>'
    )
    bs_2: str = (
        f'<text id="bs-2" x="{x2:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">NASIL DENİR?</text>'
    )
    return f'<g id="baslik">{bk_kutu}{bs_yasi}{bs_yor}{bs_um}{bs_2}</g>'


def sahne_svg(TB: int) -> tuple[str, str, str, float, float]:
    """Sahne çizimi (<g id="eskiz">) ve balon yazılarını üretir (§4.3)."""
    zc: str = '<path id="zc" d="M64 1344 L1016 1344" stroke-width="4"/>'

    x0, y0, x1_fig, y1_fig = FIG["kutu"]
    FIG_H: float = 500.0
    FIG_X: float = 120.0
    fs: float = FIG_H / (y1_fig - y0)
    tx_fig: float = FIG_X - x0 * fs
    ty_fig: float = (ZEMIN_Y - FIG_H) - y0 * fs
    fig_kalinlik: dict[str, float] = {"govde": 4.4, "sac": 3.6, "yuz": 2.6}
    fig_svg: str = "".join(
        f'<path id="f{i}" d="{p["d"]}" stroke-width="{fig_kalinlik.get(p["parca"], 4.4) / fs:.3f}"/>'
        for i, p in enumerate(FIG["yollar"])
    )
    fig_group: str = f'<g id="fig" transform="translate({tx_fig:.2f} {ty_fig:.2f}) scale({fs:.6f})">{fig_svg}</g>'
    fig_sag: float = FIG_X + (x1_fig - x0) * fs
    fig_ust: float = ZEMIN_Y - FIG_H

    bl1_rect: str = '<rect id="bl1" x="360" y="860" width="672" height="200" rx="56" stroke-width="4"/>'
    bl2_rect: str = '<rect id="bl2" x="360" y="1100" width="672" height="200" rx="56" stroke-width="4"/>'

    b1_orta_y: float = 860.0 + 100.0
    b2_orta_y: float = 1100.0 + 100.0
    # Şef QA tur 1: balon başına iki iz dağınık okunuyordu -> tek iz, baştan iki balonun arasına (3 daire, büyüyerek).
    P0: tuple[float, float] = (fig_sag + 16.0, fig_ust + 60.0)
    P1: tuple[float, float] = (348.0, (860.0 + 200.0 + 1100.0) / 2.0)
    noktalar: str = ""
    for i, (t, r) in enumerate(((0.22, 8.0), (0.52, 12.0), (0.84, 16.0)), 1):
        cx: float = P0[0] + t * (P1[0] - P0[0])
        cy: float = P0[1] + t * (P1[1] - P0[1])
        assert cx - r >= fig_sag + 10.0, f"düşünce noktası d{i} figüre çok yakın"
        assert cx + r <= 360.0 - 4.0, f"düşünce noktası d{i} balona değiyor"
        noktalar += f'<circle id="dn-{i}" cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.0f}" stroke-width="4"/>'

    scale_f: float = 112.0 / 24.0
    sw: float = 4.0 / scale_f

    home_paths: list[str] = Y.tabler("home")
    home_svg: str = "".join(f'<path d="{d}"/>' for d in home_paths)
    bl1_ikon: str = (
        f'<g id="bl1-ikon" transform="translate(392 {b1_orta_y - 56.0:.1f}) scale({scale_f:.6f})" '
        f'stroke-width="{sw:.4f}">{home_svg}</g>'
    )

    luggage_paths: list[str] = Y.tabler("luggage", AD / "cizim")
    luggage_svg: str = "".join(f'<path d="{d}"/>' for d in luggage_paths)
    bl2_ikon: str = (
        f'<g id="bl2-ikon" transform="translate(392 {b2_orta_y - 56.0:.1f}) scale({scale_f:.6f})" '
        f'stroke-width="{sw:.4f}">{luggage_svg}</g>'
    )

    eskiz: str = (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{zc}{fig_group}{bl1_rect}{bl2_rect}{noktalar}{bl1_ikon}{bl2_ikon}</g>'
    )

    taban1: float = b1_orta_y + 0.30 * TB
    taban2: float = b2_orta_y + 0.30 * TB
    bl1_yazi: str = (
        f'<text id="bl1-yazi" x="528" y="{taban1:.2f}" font-family="Caveat" font-weight="700" '
        f'font-size="{TB}" fill="{R["murekkep"]}" xml:space="preserve">I live?</text>'
    )
    bl2_yazi: str = (
        f'<text id="bl2-yazi" x="528" y="{taban2:.2f}" font-family="Caveat" font-weight="700" '
        f'font-size="{TB}" fill="{R["murekkep"]}" xml:space="preserve">I am living?</text>'
    )

    return eskiz, bl1_yazi, bl2_yazi, fig_sag, fig_ust


def blok_kutulari(
    S: int,
    TB: int,
    g1: float,
    g2: float,
    wa: float,
    wy: float,
    p: float,
    T1: float,
    T2: float,
    x1: float,
    x2: float,
    w_b1: float,
    w_b2: float,
    fig_sag: float,
    fig_ust: float,
) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını döndürür (§6.3, §6.4)."""
    hud: dict[str, float] = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}

    bas_x: float = min(x1, x2)
    bas_w: float = max(x1 + g1, x2 + g2) - bas_x
    bas_y: float = T1 - 0.86 * S
    bas_h: float = (T2 + 0.10 * S) - bas_y
    baslik: dict[str, float] = {"ad": "baslik", "x": bas_x, "y": bas_y, "w": bas_w, "h": bas_h}

    kx0: float = x1 + wa
    kx1: float = kx0 + 2.0 * p + wy
    bk_kutu: dict[str, float] = {
        "ad": "bk-kutu",
        "x": kx0,
        "y": T1 - 0.86 * S,
        "w": kx1 - kx0,
        "h": (0.86 + 0.16) * S,
    }

    fig: dict[str, float] = {"ad": "fig", "x": 120.0, "y": fig_ust, "w": fig_sag - 120.0, "h": 500.0}

    bl1: dict[str, float] = {"ad": "bl1", "x": 360.0, "y": 860.0, "w": 672.0, "h": 200.0}
    bl2: dict[str, float] = {"ad": "bl2", "x": 360.0, "y": 1100.0, "w": 672.0, "h": 200.0}

    b1_orta_y: float = 860.0 + 100.0
    taban1: float = b1_orta_y + 0.30 * TB
    bl1_yazi: dict[str, float] = {
        "ad": "bl1-yazi",
        "x": 528.0,
        "y": taban1 - 0.75 * TB,
        "w": w_b1,
        "h": 1.0 * TB,
    }

    b2_orta_y: float = 1100.0 + 100.0
    taban2: float = b2_orta_y + 0.30 * TB
    bl2_yazi: dict[str, float] = {
        "ad": "bl2-yazi",
        "x": 528.0,
        "y": taban2 - 0.75 * TB,
        "w": w_b2,
        "h": 1.0 * TB,
    }

    return [hud, baslik, bk_kutu, fig, bl1, bl2, bl1_yazi, bl2_yazi]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx: float = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy: float = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], S: int, TB: int, html: str) -> None:
    """SPEC.md §6 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict: dict[str, dict[str, float]] = {b["ad"]: b for b in bloklar}

    # 1. Bütün öğeler x in [48, 1032]; hiçbir öğe y >= 1536 değil
    for b in bloklar:
        assert b["x"] >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0, f"{b['ad']} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1536.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1536"

    # başlık ve sahne x in [64, 1016] (zemin çizgisi dahil)
    assert b_dict["baslik"]["x"] >= 64.0 - 1e-4, f"baslik sol {b_dict['baslik']['x']} < 64"
    assert b_dict["baslik"]["x"] + b_dict["baslik"]["w"] <= 1016.0 + 1e-4, f"baslik sağ {b_dict['baslik']['x'] + b_dict['baslik']['w']} > 1016"
    assert b_dict["fig"]["x"] >= 64.0 - 1e-4, f"fig sol {b_dict['fig']['x']} < 64"
    assert b_dict["fig"]["x"] + b_dict["fig"]["w"] <= 1016.0 + 1e-4, f"fig sağ {b_dict['fig']['x'] + b_dict['fig']['w']} > 1016"

    # 2. Yazı boyu >= 64 (HUD rozeti 36 hariç)
    assert S >= 64, f"Başlık boyutu {S} < 64"
    assert TB >= 64, f"Balon boyutu {TB} < 64"

    # Başlık 2 satır, toplam 3 sözcük. Her satır <= 24 karakter.
    satirlar: list[str] = ["YDT · BASIC", "YAŞIYORUM", "NASIL DENİR?", "I live?", "I am living?"]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    baslik_satirlari: list[str] = ["YAŞIYORUM", "NASIL DENİR?"]
    assert len(baslik_satirlari) == 2, f"Başlık satır sayısı {len(baslik_satirlari)} != 2"
    baslik_sozcukleri: list[str] = " ".join(baslik_satirlari).split()
    assert len(baslik_sozcukleri) == 3, f"Başlık sözcük sayısı {len(baslik_sozcukleri)} != 3"

    # 3. Bloklar arası kesişim ve boşluklar
    ana_bloklar: list[dict[str, float]] = [b_dict["hud"], b_dict["baslik"], b_dict["fig"], b_dict["bl1"], b_dict["bl2"]]
    for i in range(len(ana_bloklar)):
        for j in range(i + 1, len(ana_bloklar)):
            k: float = kesisim(ana_bloklar[i], ana_bloklar[j])
            assert k == 0.0, f"Kesişim {ana_bloklar[i]['ad']} - {ana_bloklar[j]['ad']}: {k}"

    # baslik alt ile en üst sahne öğesi arası >= 48
    en_ust_sahne: float = min(b_dict["fig"]["y"], b_dict["bl1"]["y"])
    bosluk_baslik_sahne: float = en_ust_sahne - (b_dict["baslik"]["y"] + b_dict["baslik"]["h"])
    assert bosluk_baslik_sahne >= 48.0, f"baslik alt -> sahne üst boşluk {bosluk_baslik_sahne} < 48"

    # hud alt (288) ile başlık üstü arası >= 40
    bosluk_hud_baslik: float = b_dict["baslik"]["y"] - (b_dict["hud"]["y"] + b_dict["hud"]["h"])
    assert bosluk_hud_baslik >= 40.0, f"hud alt -> başlık üst boşluk {bosluk_hud_baslik} < 40"

    # fig sağ ile balon sol arası >= 60
    bosluk_fig_bl: float = b_dict["bl1"]["x"] - (b_dict["fig"]["x"] + b_dict["fig"]["w"])
    assert bosluk_fig_bl >= 60.0, f"fig sağ -> balon sol boşluk {bosluk_fig_bl} < 60"

    # bl1 alt ile bl2 üst arası >= 24
    bosluk_bl1_bl2: float = b_dict["bl2"]["y"] - (b_dict["bl1"]["y"] + b_dict["bl1"]["h"])
    assert bosluk_bl1_bl2 >= 24.0, f"bl1 alt -> bl2 üst boşluk {bosluk_bl1_bl2} < 24"

    # 5. Yasaklar ve ek kontroller
    yasak_kelimeler: list[str] = ["kanal", "qr", "ikisi de", "kalıcı", "geçici"]
    html_lower: str = html.lower()
    for yk in yasak_kelimeler:
        assert yk not in html_lower, f"Yasak ifade bulundu: {yk}"

    for yasak_kod in ["math.random", "date.now", "new date", "opacity:0"]:
        assert yasak_kod not in html_lower, f"Yasak kod/özellik bulundu: {yasak_kod}"

    assert 'id="t2"' not in html, "id t2 yasak"
    assert 'id="ku-nokta"' not in html, "id ku-nokta yasak"
    assert 'id="rz1"' not in html, "id rz1 yasak"


def uret() -> tuple[str, int, int, list[dict[str, float]]]:
    """Sahne HTML'i, font boyutları ve nesnelerini üretir."""
    S, g1, g2, wa, wy, wu, p, T1, T2, x1, x2 = hesapla_s()
    TB, w_b1, w_b2 = hesapla_tb()

    kunye: str = kunye_svg()
    baslik: str = baslik_svg(S, wa, wy, wu, p, T1, T2, x1, x2)
    eskiz, bl1_yazi, bl2_yazi, fig_sag, fig_ust = sahne_svg(TB)

    bloklar: list[dict[str, float]] = blok_kutulari(
        S, TB, g1, g2, wa, wy, p, T1, T2, x1, x2, w_b1, w_b2, fig_sag, fig_ust
    )

    html: str = f"""<!doctype html>
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
{baslik}
{eskiz}
{bl1_yazi}
{bl2_yazi}
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

    kurallari_dogrula(bloklar, S, TB, html)
    return html, S, TB, bloklar


if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, S, TB, bloklar = uret()
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
    (AD / "nesneler.json").write_text(json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"index.html yazıldı {len(html)}")
    print(f"S={S} TB={TB}")

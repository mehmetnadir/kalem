#!/usr/bin/python3
"""Sahne 07 kapak C (karşıt çift) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: kanal (280–350) → künye (360–450; yalnız rozet) → içerik (460–1380: başlık 470–873, otobüs ≈ 1053–1356, zemin çizgisi 1360) → alt boş (1570–1920).
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# zaman.json ve zamanlar.json okuma ve doğrulama (SPEC §2)
zaman_data = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlar = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlar) == 1, "duragan içinde " + AD.name + " tek kayıt olmalı"
duragan_kayit = duragan_kayitlar[0]
kare_val = duragan_kayit["kare"]
cikti_val = duragan_kayit["cikti"]
assert kare_val == 1, f"kare {kare_val} != 1"
assert cikti_val == "kapak-c.png", f"cikti {cikti_val} != kapak-c.png"
assert AD.name not in [s["klasor"] for s in zaman_data["sahneler"]], f"{AD.name} sahneler[] içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

W, H = Y.W, Y.H
KENAR = Y.HUD["kenar"]
SAG = Y.HUD["sagSinir"]
ICERIK_BAS = Y.HUD["icerikBas"]
ICERIK_SON = Y.HUD["icerikSon"]
ORTA = (KENAR + SAG) / 2.0
BASLIK_GEN = 900.0
BASLIK_UST = 470.0
ZEMIN_Y = 1360.0
BUS_W = 780.0
BUS_H = 303.0


def hesapla_s_ve_baslik() -> tuple[
    int,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
]:
    """Başlık S boyutu ve yerleşim ölçülerini hesaplar (SPEC §4.2)."""
    s0 = 100
    p0 = 0.08 * s0
    a0 = 0.14 * s0
    gb_100 = Y.genislik("Fredoka", 700, "HE GO", s0) + a0 + Y.genislik("Fredoka", 700, "ES", s0) + p0
    S = int(math.floor(min(190, BASLIK_GEN * 100.0 / gb_100)))

    p = 0.08 * S
    a = 0.14 * S  # GO–ES arası: hap O'dan ≈ 14 px uzak (0,10·S'de 6 px, sıkışık; şef düzeltmesi 15.11)
    g_hego = Y.genislik("Fredoka", 700, "HE GO", S)
    g_es = Y.genislik("Fredoka", 700, "ES", S)
    gb = g_hego + a + g_es + p
    while gb > BASLIK_GEN and S > 1:
        S -= 1
        p = 0.08 * S
        a = 0.14 * S
        g_hego = Y.genislik("Fredoka", 700, "HE GO", S)
        g_es = Y.genislik("Fredoka", 700, "ES", S)
        gb = g_hego + a + g_es + p
    assert gb <= BASLIK_GEN, f"gb={gb} > {BASLIK_GEN}"

    x0 = ORTA - gb / 2.0
    T1 = BASLIK_UST + 0.86 * S
    T2 = T1 + 1.10 * S

    ES_X = x0 + g_hego + a
    kutu_sol = ES_X - p
    kutu_sag = ES_X + g_es + p
    kutu_w = kutu_sag - kutu_sol
    kutu_ust = T1 - 0.86 * S
    kutu_alt = T1 + 0.16 * S
    kutu_h = kutu_alt - kutu_ust
    kutu_rx = 0.10 * S

    assert kutu_sol > x0 + g_hego + 0.01 * S, (
        f"kutu_sol={kutu_sol} <= x0 + g_hego + 0.01*S={x0 + g_hego + 0.01 * S}"
    )

    VX = x0 + Y.genislik("Fredoka", 700, "HE ", S)
    bs2_x = VX - Y.genislik("Fredoka", 700, "I ", S)

    return (
        S,
        gb,
        x0,
        T1,
        T2,
        ES_X,
        kutu_sol,
        kutu_sag,
        kutu_w,
        kutu_ust,
        kutu_alt,
        kutu_h,
        kutu_rx,
        bs2_x,
    )


def baslik_svg(
    S: int,
    x0: float,
    T1: float,
    T2: float,
    ES_X: float,
    kutu_sol: float,
    kutu_ust: float,
    kutu_w: float,
    kutu_h: float,
    kutu_rx: float,
    bs2_x: float,
) -> str:
    """Başlık grubu SVG çıktısı (SPEC §4.2)."""
    bs_1 = (
        f'<text id="bs-1" x="{x0:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" style="font-kerning:none">HE GO</text>'
    )
    es_hap = (
        f'<rect id="es-hap" x="{kutu_sol:.2f}" y="{kutu_ust:.2f}" width="{kutu_w:.2f}" '
        f'height="{kutu_h:.2f}" rx="{kutu_rx:.2f}" fill="{R["vurgu"]}"/>'
    )
    bs_1es = (
        f'<text id="bs-1es" x="{ES_X:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["zemin"]}" style="font-kerning:none">ES</text>'
    )
    bs_2 = (
        f'<text id="bs-2" x="{bs2_x:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" style="font-kerning:none">I GO</text>'
    )
    return f'<g id="baslik">{bs_1}{es_hap}{bs_1es}{bs_2}</g>'


def eskiz_svg() -> tuple[str, dict[str, float]]:
    """Otobüs ve zemin çizgisi SVG grubu ve otobüs kutusu (SPEC §4.3)."""
    BUS_KUTU = [ORTA - BUS_W / 2.0, ZEMIN_Y - 4.0 - BUS_H, BUS_W, BUS_H]
    BUS = Y.coco("bus", BUS_KUTU)

    bus_coords = [float(v) for p in BUS for v in re.findall(r"-?\d+(?:\.\d+)?", p["d"])]
    bus_xs = bus_coords[0::2]
    bus_ys = bus_coords[1::2]
    min_bx, max_bx = min(bus_xs), max(bus_xs)
    min_by, max_by = min(bus_ys), max(bus_ys)

    otobus_kutu = {
        "ad": "otobus",
        "x": min_bx,
        "y": min_by,
        "w": max_bx - min_bx,
        "h": max_by - min_by,
    }

    otobus_yollar = "".join(
        f'<path d="{p["d"]}" stroke-width="4.4" vector-effect="non-scaling-stroke"/>'
        for p in BUS
    )
    otobus_g = f'<g id="otobus">{otobus_yollar}</g>'
    zc_path = '<path id="zc" d="M70 1360 L950 1360" stroke-width="4" vector-effect="non-scaling-stroke"/>'

    eskiz = (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-linecap="round" stroke-linejoin="round">'
        f'{otobus_g}{zc_path}</g>'
    )
    return eskiz, otobus_kutu


def blok_kutulari(
    S: int,
    gb: float,
    x0: float,
    T2: float,
    kutu_sol: float,
    kutu_ust: float,
    kutu_w: float,
    kutu_h: float,
    otobus_kutu: dict[str, float],
) -> tuple[list[dict[str, float]], list[dict[str, float]]]:
    """Yerleşim bloklarının kutularını hesaplar (SPEC §6.3)."""
    w_kanal = Y.HUD["kanalYaziX"] + Y.genislik("Lexend", 700, Y.KANAL_YAZI, Y.HUD["kanalYaziBoy"]) - 60.0
    kanal = {"ad": "kanal", "x": 60.0, "y": 280.0, "w": w_kanal, "h": 70.0}

    rx, rw = Y.rozet_konumu()
    assert KENAR + rw <= 960.0, f"rozet sag {KENAR + rw} > 960"
    kunye = {"ad": "kunye", "x": 60.0, "y": 360.0, "w": rw, "h": 90.0}

    baslik_alt = T2 + 0.16 * S
    baslik = {
        "ad": "baslik",
        "x": x0,
        "y": float(BASLIK_UST),
        "w": gb,
        "h": baslik_alt - float(BASLIK_UST),
    }

    es_hap = {
        "ad": "es-hap",
        "x": kutu_sol,
        "y": kutu_ust,
        "w": kutu_w,
        "h": kutu_h,
    }

    otobus = dict(otobus_kutu)
    zc = {"ad": "zc", "x": 70.0, "y": 1358.0, "w": 880.0, "h": 4.0}

    kesisim_bloklari = [kanal, kunye, baslik, otobus, zc]
    nesneler_bloklari = [kanal, kunye, baslik, es_hap, otobus, zc]
    return kesisim_bloklari, nesneler_bloklari


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(
    kesisim_bloklari: list[dict[str, float]],
    nesneler_bloklari: list[dict[str, float]],
    S: int,
    x0: float,
    kutu_sol: float,
    kutu_sag: float,
) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    # 1. Hiçbir blok y < 280, y > 1380, x > 960 değil
    for b in nesneler_bloklari:
        ad = b["ad"]
        assert b["x"] >= 0.0, f"{ad} sol {b['x']} < 0"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ {b['x'] + b['w']} > 960"
        assert b["y"] >= 280.0 - 1e-4, f"{ad} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 1380.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1380"

    # İçerik blokları: x ∈ [KENAR, SAG], y ∈ [ICERIK_BAS, ICERIK_SON]
    icerik_ogeleri = [b for b in nesneler_bloklari if b["ad"] not in ("kanal", "kunye")]
    for b in icerik_ogeleri:
        ad = b["ad"]
        assert b["x"] >= KENAR - 1e-4, f"{ad} sol {b['x']} < {KENAR}"
        assert b["x"] + b["w"] <= SAG + 1e-4, f"{ad} sağ {b['x'] + b['w']} > {SAG}"
        assert b["y"] >= ICERIK_BAS - 1e-4, f"{ad} üst {b['y']} < {ICERIK_BAS}"
        assert b["y"] + b["h"] <= ICERIK_SON + 1e-4, f"{ad} alt {b['y'] + b['h']} > {ICERIK_SON}"

    # 2. Yazı boyu: başlık S ≥ 64. Başlık 2 satır. Her satır ≤ 24 karakter.
    assert S >= 64, f"Başlık boyutu S={S} < 64"
    satirlar = ["HE GOES", "I GO"]
    assert len(satirlar) == 2, f"Başlık 2 satır olmalı, {len(satirlar)} satır var"
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 3. Bloklar: Çiftler arası kesişim 0
    for i in range(len(kesisim_bloklari)):
        for j in range(i + 1, len(kesisim_bloklari)):
            k = kesisim(kesisim_bloklari[i], kesisim_bloklari[j])
            ad1, ad2 = kesisim_bloklari[i]["ad"], kesisim_bloklari[j]["ad"]
            assert k == 0.0, f"Kesişim {ad1} - {ad2}: {k}"

    b_dict = {b["ad"]: b for b in nesneler_bloklari}

    # baslik üstü ≥ ICERIK_BAS
    assert b_dict["baslik"]["y"] >= ICERIK_BAS - 1e-4, (
        f"baslik üstü {b_dict['baslik']['y']} < ICERIK_BAS {ICERIK_BAS}"
    )

    # otobus üstü - baslik altı ≥ 48
    baslik_alt = b_dict["baslik"]["y"] + b_dict["baslik"]["h"]
    assert b_dict["otobus"]["y"] - baslik_alt >= 48.0, (
        f"otobus üstü - baslik altı {b_dict['otobus']['y'] - baslik_alt} < 48"
    )

    # otobus üstü ≥ 1020
    assert b_dict["otobus"]["y"] >= 1020.0 - 1e-4, (
        f"otobus üstü {b_dict['otobus']['y']} < 1020"
    )

    # ZEMIN_Y - 8 ≤ otobus altı ≤ ZEMIN_Y - 2
    otobus_alt = b_dict["otobus"]["y"] + b_dict["otobus"]["h"]
    assert ZEMIN_Y - 8.0 - 1e-4 <= otobus_alt <= ZEMIN_Y - 2.0 + 1e-4, (
        f"otobus altı {otobus_alt} not in [{ZEMIN_Y - 8}, {ZEMIN_Y - 2}]"
    )

    # ZEMIN_Y + 2 ≤ ICERIK_SON
    assert ZEMIN_Y + 2.0 <= ICERIK_SON + 1e-4, (
        f"ZEMIN_Y + 2 = {ZEMIN_Y + 2} > ICERIK_SON {ICERIK_SON}"
    )

    # hap O'ya değmez (§4.2)
    g_hego = Y.genislik("Fredoka", 700, "HE GO", S)
    assert kutu_sol > x0 + g_hego + 0.01 * S, (
        f"hap sol={kutu_sol} <= x0 + g_hego + 0.01*S={x0 + g_hego + 0.01 * S}"
    )

    # es-hap sağı ≤ SAG
    assert kutu_sag <= SAG + 1e-4, f"es-hap sağı {kutu_sag} > SAG {SAG}"


def uret() -> tuple[str, int, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    (
        S,
        gb,
        x0,
        T1,
        T2,
        ES_X,
        kutu_sol,
        kutu_sag,
        kutu_w,
        kutu_ust,
        kutu_alt,
        kutu_h,
        kutu_rx,
        bs2_x,
    ) = hesapla_s_ve_baslik()

    kunye = Y.kunye_svg()
    baslik = baslik_svg(
        S,
        x0,
        T1,
        T2,
        ES_X,
        kutu_sol,
        kutu_ust,
        kutu_w,
        kutu_h,
        kutu_rx,
        bs2_x,
    )
    eskiz, otobus_kutu = eskiz_svg()

    kesisim_bloklari, nesneler_bloklari = blok_kutulari(
        S, gb, x0, T2, kutu_sol, kutu_ust, kutu_w, kutu_h, otobus_kutu
    )
    kurallari_dogrula(kesisim_bloklari, nesneler_bloklari, S, x0, kutu_sol, kutu_sag)

    rz_x, _ = Y.rozet_konumu()
    rz_kayma = KENAR - rz_x

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
{baslik}
{eskiz}
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  gsap.set("#ku-konu", {{ opacity: 0 }});
  gsap.set("#rz0", {{ x: {rz_kayma:.2f} }});
  var tl = gsap.timeline({{ paused: true }});
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, 0);
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, {Z['sure']});
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, S, nesneler_bloklari


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

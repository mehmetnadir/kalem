#!/usr/bin/python3
"""Sahne 06 kapak C (karşıt çift) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> başlık (375-700) -> sahne (864-1344) -> platform (1536-1920 boş).
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

# zaman.json ve zamanlar.json okuma ve doğrulama (SPEC §3)
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
KENAR = 48
SAG = 1032
BASLIK_GEN = 952
ZEMIN_Y = 1344
PLATFORM = 1536


def hesapla_s_ve_baslik() -> tuple[int, float, float, float, float, float, float, float, float, float, float]:
    """Başlık S boyutu ve yerleşim ölçülerini hesaplar (SPEC §4.2)."""
    s0 = 100
    p0 = 0.08 * s0
    gb_100 = Y.genislik("Fredoka", 700, "I AM LIVING", s0) + p0
    S = int(math.floor(min(190, 952.0 * 100.0 / gb_100)))

    p = 0.08 * S
    g_I = Y.genislik("Fredoka", 700, "I", S)
    g_Is = Y.genislik("Fredoka", 700, "I ", S)
    g_IAMLIVING = Y.genislik("Fredoka", 700, "I AM LIVING", S)
    gb = g_IAMLIVING + p
    while gb > 952.0 and S > 1:
        S -= 1
        p = 0.08 * S
        g_I = Y.genislik("Fredoka", 700, "I", S)
        g_Is = Y.genislik("Fredoka", 700, "I ", S)
        g_IAMLIVING = Y.genislik("Fredoka", 700, "I AM LIVING", S)
        gb = g_IAMLIVING + p
    assert gb <= 952.0, f"gb={gb} > 952"

    x0 = 540.0 - gb / 2.0
    kutu_sol = x0 + g_Is - p
    kutu_sag = x0 + g_IAMLIVING + p
    kutu_w = kutu_sag - kutu_sol
    T1 = 375.0 + 0.70 * S
    T2 = T1 + 1.02 * S
    kutu_ust = T2 - 0.86 * S
    kutu_alt = T2 + 0.16 * S
    kutu_h = kutu_alt - kutu_ust
    kutu_rx = 0.10 * S

    assert kutu_sol > x0 + g_I + 0.04 * S, f"kutu_sol={kutu_sol} <= x0 + g_I + 0.04*S={x0 + g_I + 0.04 * S}"
    return S, gb, x0, g_Is, T1, T2, kutu_sol, kutu_ust, kutu_w, kutu_h, kutu_rx


def kunye_svg() -> str:
    """Künye (HUD) grubu SVG çıktısı (SPEC §4.1)."""
    logo_w = 96.0 * Y.LOGO_EN_BOY
    logo = f'<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" width="{logo_w:.2f}" height="96"/></g>'
    rz_w = Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56.0
    rozet = (
        f'<g id="rz0">'
        f'<rect x="48" y="216" width="{rz_w:.2f}" height="72" rx="36" fill="{R["vurgu"]}"/>'
        f'<text x="{48.0 + rz_w / 2.0:.2f}" y="265" text-anchor="middle" '
        f'font-family="Lexend" font-weight="700" font-size="36" fill="{R["zemin"]}">YDT · BASIC</text>'
        f'</g>'
    )
    return f'<g id="kunye">{logo}{rozet}</g>'


def baslik_svg(
    S: int,
    x0: float,
    g_Is: float,
    T1: float,
    T2: float,
    kutu_sol: float,
    kutu_ust: float,
    kutu_w: float,
    kutu_h: float,
    kutu_rx: float,
) -> str:
    """Başlık grubu SVG çıktısı (SPEC §4.2)."""
    bs_1 = (
        f'<text id="bs-1" x="{x0:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">I LIVE</text>'
    )
    bs_2i = (
        f'<text id="bs-2i" x="{x0:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">I</text>'
    )
    bk_kutu = (
        f'<rect id="bk-kutu" x="{kutu_sol:.2f}" y="{kutu_ust:.2f}" width="{kutu_w:.2f}" '
        f'height="{kutu_h:.2f}" rx="{kutu_rx:.2f}" fill="{R["vurgu"]}"/>'
    )
    bs_2v = (
        f'<text id="bs-2v" x="{x0 + g_Is:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["zemin"]}" style="font-kerning:none">AM LIVING</text>'
    )
    return f'<g id="baslik">{bs_1}{bk_kutu}{bs_2i}{bs_2v}</g>'


def eskiz_svg() -> tuple[str, float, float]:
    """Sahne çizim grubu SVG çıktısı (SPEC §4.3)."""
    # 1. Zemin çizgisi
    zc = '<path id="zc" d="M64 1344 L1016 1344" stroke-width="4"/>'

    # 2. Ev (home)
    EV_S = 15
    tx_ev = 88 - 3 * EV_S
    ty_ev = 1344 - 21 * EV_S
    sw_ev = 4.0 / EV_S
    ev_yollar = Y.tabler("home")
    ev_svg = "".join(f'<path d="{d}"/>' for d in ev_yollar)
    ev_group = (
        f'<g id="ev" transform="translate({tx_ev} {ty_ev}) scale({EV_S})" '
        f'stroke-width="{sw_ev:.4f}">{ev_svg}</g>'
    )

    # 3. Figür
    FIG = json.loads((AD / "cizim" / "ogretmen.json").read_text(encoding="utf-8"))
    x0_f, y0_f, x1_f, y1_f = FIG["kutu"]
    FIG_H = 480
    fs = FIG_H / (y1_f - y0_f)
    fw = (x1_f - x0_f) * fs
    FIG_X = 540.0 - fw / 2.0
    tx_fig = FIG_X - x0_f * fs
    ty_fig = (ZEMIN_Y - FIG_H) - y0_f * fs
    fig_kalinlik = {"govde": 4.4, "sac": 3.6, "yuz": 2.6}
    fig_svg = "".join(
        f'<path id="f{i}" d="{p["d"]}" stroke-width="{fig_kalinlik.get(p.get("parca"), 4.4) / fs:.3f}"/>'
        for i, p in enumerate(FIG["yollar"])
    )
    fig_group = f'<g id="fig" transform="translate({tx_fig:.2f} {ty_fig:.2f}) scale({fs:.6f})">{fig_svg}</g>'

    # 4. Bavul (luggage)
    BV_S = 11
    tx_bv = 952 - 18 * BV_S
    ty_bv = 1344 - 21 * BV_S
    sw_bv = 4.0 / BV_S
    bavul_yollar = Y.tabler("luggage", AD / "cizim")
    bavul_svg = "".join(f'<path d="{d}"/>' for d in bavul_yollar)
    bavul_group = (
        f'<g id="bavul" transform="translate({tx_bv} {ty_bv}) scale({BV_S})" '
        f'stroke-width="{sw_bv:.4f}">{bavul_svg}</g>'
    )

    eskiz = (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{zc}{ev_group}{fig_group}{bavul_group}</g>'
    )
    return eskiz, fw, FIG_X


def etiketler_svg() -> str:
    """Etiketler SVG çıktısı (SPEC §4.3)."""
    et_kalici = (
        f'<text id="et-kalici" x="223" y="1038" text-anchor="middle" font-family="Caveat" '
        f'font-weight="700" font-size="88" fill="{R["murekkep"]}">kalıcı</text>'
    )
    et_gecici = (
        f'<text id="et-gecici" x="886" y="1110" text-anchor="middle" font-family="Caveat" '
        f'font-weight="700" font-size="88" fill="{R["murekkep"]}">geçici</text>'
    )
    return f"{et_kalici}\n{et_gecici}"


def blok_kutulari(
    S: int,
    gb: float,
    x0: float,
    T1: float,
    kutu_sol: float,
    kutu_ust: float,
    kutu_w: float,
    kutu_h: float,
    fw: float,
    FIG_X: float,
) -> tuple[list[dict[str, float]], list[dict[str, float]]]:
    """Yerleşim bloklarının kutularını hesaplar.
    Döndürür: (kesisim_bloklari, nesneler_bloklari).
    kesisim_bloklari (7 adet): hud, baslik, et-kalici, et-gecici, ev, fig, bavul.
    nesneler_bloklari (8 adet): hud, baslik, bk-kutu, et-kalici, et-gecici, ev, fig, bavul.
    """
    hud = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}

    baslik_y_ust = T1 - 0.75 * S
    kutu_alt = kutu_ust + kutu_h
    baslik = {
        "ad": "baslik",
        "x": x0,
        "y": baslik_y_ust,
        "w": gb,
        "h": kutu_alt - baslik_y_ust,
    }

    bk_kutu = {
        "ad": "bk-kutu",
        "x": kutu_sol,
        "y": kutu_ust,
        "w": kutu_w,
        "h": kutu_h,
    }

    w_kalici = Y.genislik("Caveat", 700, "kalıcı", 88)
    taban_kalici = 1074.0 - 36.0  # = 1038.0
    et_kalici = {
        "ad": "et-kalici",
        "x": 223.0 - w_kalici / 2.0,
        "y": taban_kalici - 0.75 * 88.0,
        "w": w_kalici,
        "h": (0.75 + 0.25) * 88.0,
    }

    w_gecici = Y.genislik("Caveat", 700, "geçici", 88)
    taban_gecici = 1146.0 - 36.0  # = 1110.0
    et_gecici = {
        "ad": "et-gecici",
        "x": 886.0 - w_gecici / 2.0,
        "y": taban_gecici - 0.75 * 88.0,
        "w": w_gecici,
        "h": (0.75 + 0.25) * 88.0,
    }

    ev = {"ad": "ev", "x": 88.0, "y": 1074.0, "w": 270.0, "h": 270.0}
    fig = {"ad": "fig", "x": FIG_X, "y": float(ZEMIN_Y - 480), "w": fw, "h": 480.0}
    bavul = {"ad": "bavul", "x": 820.0, "y": 1146.0, "w": 132.0, "h": 198.0}

    kesisim_bloklari = [hud, baslik, et_kalici, et_gecici, ev, fig, bavul]
    nesneler_bloklari = [hud, baslik, bk_kutu, et_kalici, et_gecici, ev, fig, bavul]
    return kesisim_bloklari, nesneler_bloklari


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(
    kesisim_bloklari: list[dict[str, float]], nesneler_bloklari: list[dict[str, float]], S: int
) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    # 1. Bütün öğeler x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil; başlık ve sahne x ∈ [64, 1016].
    for b in nesneler_bloklari:
        assert b["x"] >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0, f"{b['ad']} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1536.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1536"

    # Başlık ve sahne x ∈ [64, 1016] (zemin çizgisi dahil: M64 1344 L1016 1344)
    for b in nesneler_bloklari:
        if b["ad"] != "hud":
            ad_str = b["ad"]
            assert b["x"] >= 64.0 - 1e-4, f"{ad_str} sol {b['x']} < 64"
            assert b["x"] + b["w"] <= 1016.0 + 1e-4, f"{ad_str} sağ {b['x'] + b['w']} > 1016"

    # 2. Yazı boyu ≥ 64 (HUD rozeti 36 hariç). Başlık 2 satır. Her satır ≤ 24 karakter.
    assert S >= 64, f"Başlık boyutu S={S} < 64"
    satirlar = [
        "I LIVE",
        "I AM LIVING",
        "YDT · BASIC",
        "kalıcı",
        "geçici",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 3. Bloklar: hud (0–288), baslik, et-kalici, et-gecici, ev, fig, bavul.
    # Çiftler arası kesişim 0
    for i in range(len(kesisim_bloklari)):
        for j in range(i + 1, len(kesisim_bloklari)):
            k = kesisim(kesisim_bloklari[i], kesisim_bloklari[j])
            ad1, ad2 = kesisim_bloklari[i]["ad"], kesisim_bloklari[j]["ad"]
            assert k == 0.0, f"Kesişim {ad1} - {ad2}: {k}"

    b_dict = {b["ad"]: b for b in nesneler_bloklari}

    # baslik alt ile en üst sahne öğesi arası ≥ 48
    sahne_ogeleri = [b_dict["et-kalici"], b_dict["et-gecici"], b_dict["ev"], b_dict["fig"], b_dict["bavul"]]
    en_ust_sahne_y = min(b["y"] for b in sahne_ogeleri)
    baslik_alt = b_dict["baslik"]["y"] + b_dict["baslik"]["h"]
    assert en_ust_sahne_y - baslik_alt >= 48.0, f"baslik alt -> sahne ara {en_ust_sahne_y - baslik_alt} < 48"

    # hud alt ile başlık üstü arası ≥ 40
    hud_alt = b_dict["hud"]["y"] + b_dict["hud"]["h"]
    baslik_ust = b_dict["baslik"]["y"]
    assert baslik_ust - hud_alt >= 40.0, f"hud alt -> başlık üst ara {baslik_ust - hud_alt} < 40"

    # ev–fig ve fig–bavul yatay ara ≥ 60
    ev_fig_ara = b_dict["fig"]["x"] - (b_dict["ev"]["x"] + b_dict["ev"]["w"])
    assert ev_fig_ara >= 60.0, f"ev-fig yatay ara {ev_fig_ara} < 60"
    fig_bavul_ara = b_dict["bavul"]["x"] - (b_dict["fig"]["x"] + b_dict["fig"]["w"])
    assert fig_bavul_ara >= 60.0, f"fig-bavul yatay ara {fig_bavul_ara} < 60"

    # etiket alt ile kendi ikonu üstü arası ≥ 12
    et_kalici_alt = b_dict["et-kalici"]["y"] + b_dict["et-kalici"]["h"]
    assert b_dict["ev"]["y"] - et_kalici_alt >= 12.0, f"kalıcı -> ev ara {b_dict['ev']['y'] - et_kalici_alt} < 12"
    et_gecici_alt = b_dict["et-gecici"]["y"] + b_dict["et-gecici"]["h"]
    assert b_dict["bavul"]["y"] - et_gecici_alt >= 12.0, f"geçici -> bavul ara {b_dict['bavul']['y'] - et_gecici_alt} < 12"


def uret() -> tuple[str, int, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    S, gb, x0, g_Is, T1, T2, kutu_sol, kutu_ust, kutu_w, kutu_h, kutu_rx = hesapla_s_ve_baslik()
    kunye = kunye_svg()
    baslik = baslik_svg(S, x0, g_Is, T1, T2, kutu_sol, kutu_ust, kutu_w, kutu_h, kutu_rx)
    eskiz, fw, FIG_X = eskiz_svg()
    etiketler = etiketler_svg()

    kesisim_bloklari, nesneler_bloklari = blok_kutulari(
        S, gb, x0, T1, kutu_sol, kutu_ust, kutu_w, kutu_h, fw, FIG_X
    )
    kurallari_dogrula(kesisim_bloklari, nesneler_bloklari, S)

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
{etiketler}
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

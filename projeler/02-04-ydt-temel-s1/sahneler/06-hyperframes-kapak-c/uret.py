#!/usr/bin/python3
"""Sahne 06 kapak C (karşıt çift) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: kanal (280–350) → künye (360–450) → içerik (460–1380: başlık 470–779, sahne 880–1360) → alt boş (1570–1920).
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
ORTA = (KENAR + SAG) / 2
BASLIK_GEN = 880
BASLIK_UST = 470
ZEMIN_Y = 1360
NEQ_O, ARA_O = 0.50, 0.12   # ≠ genişliği, ≠–kutu arası (S oranı; ≠ çizimi 02-04-ydt-temel-s2 kapak A kalıbı)


def hesapla_s_ve_baslik() -> tuple[int, float, float, float, float, float, float, float, float, float, float]:
    """Başlık S boyutu ve yerleşim ölçülerini hesaplar (DUZ4 A2, 16.11: `LIVE` / `≠ LIVING`, 2 sözcük + ≠).
    Alt satır: çizili ≠ (NEQ_O·S) + ara (ARA_O·S) + kutu (p + LIVING + p); üst satır LIVE, LIVING yazısıyla aynı x."""
    S = int((ZEMIN_Y - 480 - 48 - BASLIK_UST) / 1.93)   # kutu altı 470 + 1,93·S, figür üstüne ≥ 48 (S = 187)
    p = 0.08 * S
    g_LIVING = Y.genislik("Fredoka", 700, "LIVING", S)
    gb = (NEQ_O + ARA_O) * S + g_LIVING + 2 * p
    while gb > BASLIK_GEN and S > 64:
        S -= 1
        p = 0.08 * S
        g_LIVING = Y.genislik("Fredoka", 700, "LIVING", S)
        gb = (NEQ_O + ARA_O) * S + g_LIVING + 2 * p
    assert gb <= BASLIK_GEN, f"gb={gb} > {BASLIK_GEN}"

    x0 = ORTA - gb / 2.0
    kutu_sol = x0 + (NEQ_O + ARA_O) * S
    g_Is = kutu_sol + p - x0                    # LIVE ve LIVING yazısının x0'dan uzaklığı
    kutu_w = gb - (NEQ_O + ARA_O) * S
    T1 = BASLIK_UST + 0.75 * S
    T2 = T1 + 1.02 * S
    kutu_ust = T2 - 0.86 * S
    kutu_alt = T2 + 0.16 * S
    kutu_h = kutu_alt - kutu_ust
    kutu_rx = 0.10 * S

    assert kutu_sol - (x0 + NEQ_O * S) >= 16, f"≠ ile kutu arası {kutu_sol - (x0 + NEQ_O * S):.1f} < 16"
    return S, gb, x0, g_Is, T1, T2, kutu_sol, kutu_ust, kutu_w, kutu_h, kutu_rx


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
        f'<text id="bs-1" x="{x0 + g_Is:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">LIVE</text>'
    )
    nw, xa, xb = NEQ_O * S, x0 + 0.06 * S, x0 + NEQ_O * S - 0.06 * S   # ≠: iki çubuk + eğik çizgi
    xm, yu, ya = (xa + xb) / 2, T2 - 0.46 * S, T2 - 0.24 * S
    bs_2i = (
        f'<g id="bs-2i" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round">'
        f'<path d="M {xa:.2f} {yu:.2f} Q {xm:.2f} {yu - 3:.2f} {xb:.2f} {yu:.2f}" stroke-width="{0.10 * S:.2f}"/>'
        f'<path d="M {xa:.2f} {ya:.2f} Q {xm:.2f} {ya + 3:.2f} {xb:.2f} {ya:.2f}" stroke-width="{0.10 * S:.2f}"/>'
        f'<path d="M {x0 + 0.74 * nw:.2f} {T2 - 0.70 * S:.2f} L {x0 + 0.26 * nw:.2f} {T2 + 0.02 * S:.2f}" '
        f'stroke-width="{0.09 * S:.2f}"/></g>'
    )
    bk_kutu = (
        f'<rect id="bk-kutu" x="{kutu_sol:.2f}" y="{kutu_ust:.2f}" width="{kutu_w:.2f}" '
        f'height="{kutu_h:.2f}" rx="{kutu_rx:.2f}" fill="{R["vurgu"]}"/>'
    )
    bs_2v = (
        f'<text id="bs-2v" x="{x0 + g_Is:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["zemin"]}" style="font-kerning:none">LIVING</text>'
    )
    return f'<g id="baslik">{bs_1}{bk_kutu}{bs_2i}{bs_2v}</g>'


def eskiz_svg() -> tuple[str, float, float, dict[str, float], dict[str, float]]:
    """Sahne çizim grubu SVG çıktısı (SPEC §4.3)."""
    # 1. Zemin çizgisi
    zc = f'<path id="zc" d="M70 {ZEMIN_Y} L950 {ZEMIN_Y}" stroke-width="4"/>'

    # 2. Ev (home)
    EV_S = 15
    tx_ev = 80 - 3 * EV_S
    ty_ev = ZEMIN_Y - 21 * EV_S
    sw_ev = 4.0 / EV_S
    ev_yollar = Y.tabler("home")
    ev_svg = "".join(f'<path d="{d}"/>' for d in ev_yollar)
    ev_group = (
        f'<g id="ev" transform="translate({tx_ev} {ty_ev}) scale({EV_S})" '
        f'stroke-width="{sw_ev:.4f}">{ev_svg}</g>'
    )
    ev_kutu = {"ad": "ev", "x": 80.0, "y": 1090.0, "w": 270.0, "h": 270.0}

    # 3. Figür
    FIG = json.loads((AD / "cizim" / "ogretmen.json").read_text(encoding="utf-8"))
    x0_f, y0_f, x1_f, y1_f = FIG["kutu"]
    FIG_H = 480
    fs = FIG_H / (y1_f - y0_f)
    fw = (x1_f - x0_f) * fs
    FIG_X = ORTA - fw / 2.0
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
    tx_bv = 876 - 18 * BV_S
    ty_bv = ZEMIN_Y - 21 * BV_S
    sw_bv = 4.0 / BV_S
    bavul_yollar = Y.tabler("luggage", AD / "cizim")
    bavul_svg = "".join(f'<path d="{d}"/>' for d in bavul_yollar)
    bavul_group = (
        f'<g id="bavul" transform="translate({tx_bv} {ty_bv}) scale({BV_S})" '
        f'stroke-width="{sw_bv:.4f}">{bavul_svg}</g>'
    )
    bavul_kutu = {"ad": "bavul", "x": 744.0, "y": 1162.0, "w": 132.0, "h": 198.0}

    eskiz = (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{zc}{ev_group}{fig_group}{bavul_group}</g>'
    )
    return eskiz, fw, FIG_X, ev_kutu, bavul_kutu


def etiketler_svg(ev_kutu: dict[str, float], bavul_kutu: dict[str, float]) -> str:
    """Etiketler SVG çıktısı (SPEC §4.3)."""
    ev_orta = int(round(ev_kutu["x"] + ev_kutu["w"] / 2.0))
    ev_taban = int(round(ev_kutu["y"] - 40.0))
    bv_orta = int(round(bavul_kutu["x"] + bavul_kutu["w"] / 2.0))
    bv_taban = int(round(bavul_kutu["y"] - 40.0))

    et_kalici = (
        f'<text id="et-kalici" x="{ev_orta}" y="{ev_taban}" text-anchor="middle" font-family="Caveat" '
        f'font-weight="700" font-size="88" fill="{R["murekkep"]}">kalıcı</text>'
    )
    et_gecici = (
        f'<text id="et-gecici" x="{bv_orta}" y="{bv_taban}" text-anchor="middle" font-family="Caveat" '
        f'font-weight="700" font-size="88" fill="{R["murekkep"]}">geçici</text>'
    )
    return f"{et_kalici}\n{et_gecici}"


def blok_kutulari(
    S: int,
    gb: float,
    x0: float,
    kutu_sol: float,
    kutu_ust: float,
    kutu_w: float,
    kutu_h: float,
    fw: float,
    FIG_X: float,
    ev_kutu: dict[str, float],
    bavul_kutu: dict[str, float],
) -> tuple[list[dict[str, float]], list[dict[str, float]]]:
    """Yerleşim bloklarının kutularını hesaplar.
    Döndürür: (kesisim_bloklari, nesneler_bloklari).
    kesisim_bloklari (8 adet): kanal, kunye, baslik, et-kalici, et-gecici, ev, fig, bavul.
    nesneler_bloklari (9 adet): kanal, kunye, baslik, bk-kutu, et-kalici, et-gecici, ev, fig, bavul.
    """
    w_kanal = Y.HUD["kanalYaziX"] + Y.genislik("Lexend", 700, Y.KANAL_YAZI, 42) - 60.0
    kanal = {"ad": "kanal", "x": 60.0, "y": 280.0, "w": w_kanal, "h": 70.0}

    rx, rw = Y.rozet_konumu()
    assert rx + rw <= 960.0, f"rozet sag {rx + rw} > 960"
    kunye = {"ad": "kunye", "x": 60.0, "y": 360.0, "w": rx + rw - 60.0, "h": 90.0}

    kutu_alt = kutu_ust + kutu_h
    baslik = {
        "ad": "baslik",
        "x": x0,
        "y": float(BASLIK_UST),
        "w": gb,
        "h": kutu_alt - float(BASLIK_UST),
    }

    bk_kutu = {
        "ad": "bk-kutu",
        "x": kutu_sol,
        "y": kutu_ust,
        "w": kutu_w,
        "h": kutu_h,
    }

    w_kalici = Y.genislik("Caveat", 700, "kalıcı", 88)
    ev_orta = ev_kutu["x"] + ev_kutu["w"] / 2.0
    taban_kalici = ev_kutu["y"] - 40.0
    et_kalici = {
        "ad": "et-kalici",
        "x": ev_orta - w_kalici / 2.0,
        "y": taban_kalici - 0.75 * 88.0,
        "w": w_kalici,
        "h": (0.75 + 0.30) * 88.0,
    }

    w_gecici = Y.genislik("Caveat", 700, "geçici", 88)
    bv_orta = bavul_kutu["x"] + bavul_kutu["w"] / 2.0
    taban_gecici = bavul_kutu["y"] - 40.0
    et_gecici = {
        "ad": "et-gecici",
        "x": bv_orta - w_gecici / 2.0,
        "y": taban_gecici - 0.75 * 88.0,
        "w": w_gecici,
        "h": (0.75 + 0.30) * 88.0,
    }

    ev = dict(ev_kutu)
    fig = {"ad": "fig", "x": FIG_X, "y": float(ZEMIN_Y - 480), "w": fw, "h": 480.0}
    bavul = dict(bavul_kutu)

    kesisim_bloklari = [kanal, kunye, baslik, et_kalici, et_gecici, ev, fig, bavul]
    nesneler_bloklari = [kanal, kunye, baslik, bk_kutu, et_kalici, et_gecici, ev, fig, bavul]
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
    # 1. Hiçbir blok y < 280, y > 1380, x > 960 değil
    for b in nesneler_bloklari:
        ad = b["ad"]
        assert b["x"] >= 0.0, f"{ad} sol {b['x']} < 0"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ {b['x'] + b['w']} > 960"
        assert b["y"] >= 280.0 - 1e-4, f"{ad} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 1380.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1380"

    # İçerik blokları: x ∈ [KENAR, SAG], y ∈ [ICERIK_BAS, ICERIK_SON]
    icerik_ogeleri = [b for b in nesneler_bloklari if b["ad"] not in ("kanal", "kunye")]
    zc = {"ad": "zc", "x": 70.0, "y": 1358.0, "w": 880.0, "h": 4.0}
    for b in icerik_ogeleri + [zc]:
        ad = b["ad"]
        assert b["x"] >= KENAR - 1e-4, f"{ad} sol {b['x']} < {KENAR}"
        assert b["x"] + b["w"] <= SAG + 1e-4, f"{ad} sağ {b['x'] + b['w']} > {SAG}"
        assert b["y"] >= ICERIK_BAS - 1e-4, f"{ad} üst {b['y']} < {ICERIK_BAS}"
        assert b["y"] + b["h"] <= ICERIK_SON + 1e-4, f"{ad} alt {b['y'] + b['h']} > {ICERIK_SON}"

    # 2. Yazı boyu: başlık S ≥ 64, etiket 88 ≥ 72. Başlık 2 satır. Her satır ≤ 24 karakter.
    assert S >= 64, f"Başlık boyutu S={S} < 64"
    assert 88 >= 72, "Etiket boyutu 88 < 72"
    satirlar = [
        "LIVE",
        "≠ LIVING",
        "kalıcı",
        "geçici",
    ]
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

    # baslik alt ile en üst sahne öğesi arası ≥ 48
    sahne_ogeleri = [b_dict["et-kalici"], b_dict["et-gecici"], b_dict["ev"], b_dict["fig"], b_dict["bavul"]]
    en_ust_sahne_y = min(b["y"] for b in sahne_ogeleri)
    baslik_alt = b_dict["baslik"]["y"] + b_dict["baslik"]["h"]
    assert en_ust_sahne_y - baslik_alt >= 48.0, (
        f"baslik alt -> sahne ara {en_ust_sahne_y - baslik_alt} < 48"
    )

    # ev–fig ve fig–bavul yatay ara ≥ 60
    ev_fig_ara = b_dict["fig"]["x"] - (b_dict["ev"]["x"] + b_dict["ev"]["w"])
    assert ev_fig_ara >= 60.0, f"ev-fig yatay ara {ev_fig_ara} < 60"
    fig_bavul_ara = b_dict["bavul"]["x"] - (b_dict["fig"]["x"] + b_dict["fig"]["w"])
    assert fig_bavul_ara >= 60.0, f"fig-bavul yatay ara {fig_bavul_ara} < 60"

    # etiket alt ile kendi ikonu üstü arası ≥ 12
    et_kalici_alt = b_dict["et-kalici"]["y"] + b_dict["et-kalici"]["h"]
    assert b_dict["ev"]["y"] - et_kalici_alt >= 12.0, (
        f"kalıcı -> ev ara {b_dict['ev']['y'] - et_kalici_alt} < 12"
    )
    et_gecici_alt = b_dict["et-gecici"]["y"] + b_dict["et-gecici"]["h"]
    assert b_dict["bavul"]["y"] - et_gecici_alt >= 12.0, (
        f"geçici -> bavul ara {b_dict['bavul']['y'] - et_gecici_alt} < 12"
    )

    # ZEMIN_Y + 2 ≤ ICERIK_SON
    assert ZEMIN_Y + 2 <= ICERIK_SON, f"ZEMIN_Y + 2 = {ZEMIN_Y + 2} > ICERIK_SON {ICERIK_SON}"


def uret() -> tuple[str, int, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    S, gb, x0, g_Is, T1, T2, kutu_sol, kutu_ust, kutu_w, kutu_h, kutu_rx = hesapla_s_ve_baslik()
    kunye = Y.kunye_svg()
    baslik = baslik_svg(S, x0, g_Is, T1, T2, kutu_sol, kutu_ust, kutu_w, kutu_h, kutu_rx)
    eskiz, fw, FIG_X, ev_kutu, bavul_kutu = eskiz_svg()
    etiketler = etiketler_svg(ev_kutu, bavul_kutu)

    kesisim_bloklari, nesneler_bloklari = blok_kutulari(
        S, gb, x0, kutu_sol, kutu_ust, kutu_w, kutu_h, fw, FIG_X, ev_kutu, bavul_kutu
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

#!/usr/bin/python3
"""Sahne 06 kapak C (karşıt çift) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> başlık (340-768) -> kart 1 (864-1096) -> kart 2 (1112-1344) -> platform (1536-1920 boş).
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
assert set(R.keys()) >= {"zemin", "murekkep", "vurgu"}

W, H = Y.W, Y.H
KENAR = 48
SAG = 1032
BASLIK_GEN = 952
SAHNE_UST = 864
SAHNE_ALT = 1344
PLATFORM = 1536
IKON = 140
IKON_X = 862

# Giysi çizimleri: birim ızgara (mont 100×120, tişört 100×90); n = darbe noktaları, egri = yumuşak.
# Kaynak: /home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/sahne-03.js satır 17–32
MONT: list[dict] = [
    {"n": [[40, 4], [20, 10], [6, 70], [17, 74], [26, 34], [23, 116], [50, 117]]},
    {"n": [[60, 4], [80, 10], [94, 70], [83, 74], [74, 34], [77, 116], [50, 117]]},
    {"n": [[40, 4], [50, 9], [60, 4]], "egri": True},
    {"n": [[40, 4], [44, 21], [50, 34]], "egri": True},
    {"n": [[60, 4], [56, 21], [50, 34]], "egri": True},
    {"n": [[50, 34], [50, 116]]},
    {"n": [[28, 96], [38, 95]]},
    {"n": [[62, 95], [72, 96]]},
    {"daire": [44, 48, 2.6]},
    {"daire": [44, 64, 2.6]},
    {"daire": [44, 80, 2.6]},
]

TISORT: list[dict] = [
    {
        "n": [
            [37, 4],
            [14, 12],
            [0, 36],
            [14, 46],
            [24, 37],
            [24, 88],
            [76, 88],
            [76, 37],
            [86, 46],
            [100, 36],
            [86, 12],
            [63, 4],
        ]
    },
    {"n": [[37, 4], [50, 14], [63, 4]], "egri": True},
    {"n": [[14, 12], [24, 37]]},
    {"n": [[86, 12], [76, 37]]},
]


def hesapla_baslik() -> tuple[int, float, float, float, float]:
    """Başlık S boyutu ve yerleşim ölçülerini hesaplar (SPEC §5.2)."""
    satir1 = "AYNI FİİL,"
    satir2 = "İKİ ZAMAN"
    gmax_100 = max(Y.genislik("Fredoka", 700, satir1, 100), Y.genislik("Fredoka", 700, satir2, 100))
    S = int(math.floor(min(190, 952.0 * 100.0 / gmax_100)))

    gmax_S = max(Y.genislik("Fredoka", 700, satir1, S), Y.genislik("Fredoka", 700, satir2, S))
    while gmax_S + 12.0 > 952.0 and S > 1:
        S -= 1
        gmax_S = max(Y.genislik("Fredoka", 700, satir1, S), Y.genislik("Fredoka", 700, satir2, S))
    assert gmax_S + 12.0 <= 952.0, f"gmax(S)+12={gmax_S + 12.0} > 952"
    assert S >= 64, f"S={S} < 64"

    x0 = 540.0 - gmax_S / 2.0
    T1 = 340.0 + 0.93 * S + 6.0
    T2 = T1 + 1.19 * S
    return S, gmax_S, x0, T1, T2


def baslik_svg(S: int, x0: float, T1: float, T2: float) -> str:
    """Başlık grubu SVG çıktısı (SPEC §5.2)."""
    bs_1 = (
        f'<text id="bs-1" x="{x0:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">AYNI FİİL,</text>'
    )
    bs_2 = (
        f'<text id="bs-2" x="{x0:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">İKİ ZAMAN</text>'
    )
    return f'<g id="baslik">{bs_1}{bs_2}</g>'


def kunye_svg() -> str:
    """Künye (HUD) grubu SVG çıktısı (SPEC §5.1)."""
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


def ikon_cizim_svg(
    ogeler: list[dict],
    uw: float,
    uh: float,
    dis_ust: float,
    simge: str,
) -> tuple[str, float, float, float, float]:
    """Köşe ikonu SVG çıktısını ve çizilen sınırlayıcı kutusunu (ox, oy, w, h) üretir (SPEC §5.5)."""
    k = min(140.0 / uw, 140.0 / uh)
    ox = 862.0 + (140.0 - uw * k) / 2.0
    oy = (dis_ust + 28.0) + (140.0 - uh * k) / 2.0
    parcalar: list[str] = []
    for item in ogeler:
        if "daire" in item:
            cx, cy, r = item["daire"]
            parcalar.append(f'<circle cx="{ox + cx * k:.2f}" cy="{oy + cy * k:.2f}" r="{r * k:.2f}"/>')
        elif item.get("egri"):
            p0, p1, p2 = item["n"]
            p0x, p0y = ox + p0[0] * k, oy + p0[1] * k
            p1x, p1y = ox + p1[0] * k, oy + p1[1] * k
            p2x, p2y = ox + p2[0] * k, oy + p2[1] * k
            cx = 2.0 * p1x - (p0x + p2x) / 2.0
            cy = 2.0 * p1y - (p0y + p2y) / 2.0
            parcalar.append(f'<path d="M {p0x:.2f} {p0y:.2f} Q {cx:.2f} {cy:.2f} {p2x:.2f} {p2y:.2f}"/>')
        else:
            pts = [f"{ox + pt[0] * k:.2f} {oy + pt[1] * k:.2f}" for pt in item["n"]]
            d = "M " + " L ".join(pts)
            parcalar.append(f'<path d="{d}"/>')
    ic = "".join(parcalar)
    svg = (
        f'<g id="{simge}" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{ic}</g>'
    )
    return svg, ox, oy, uw * k, uh * k


def hesapla_b() -> int:
    """Kart yazı boyutu B'yi hesaplar (SPEC §5.3)."""
    B = 72
    satirlar = [
        "She wears her coat",
        "in the winter.",
        "She is wearing her",
        "pink T-shirt today.",
    ]
    while any(88.0 + Y.genislik("Fredoka", 700, s, B) > IKON_X - 32.0 for s in satirlar) and B > 1:
        B -= 1
    assert B >= 64, f"B={B} < 64"
    return B


def kartlar_svg(
    B: int,
) -> tuple[
    str,
    str,
    dict[str, float],
    dict[str, float],
    dict[str, float],
    dict[str, float],
    dict[str, float],
    dict[str, float],
    dict[str, float],
    dict[str, float],
    dict[str, float],
]:
    """Kart 1 ve Kart 2 gruplarını ve nesne kutularını üretir (SPEC §5.3, §5.4, §5.5)."""
    # Kart 1
    k1_ust = 864.0
    k1_crv = f'<rect id="k1-crv" x="50" y="866" width="980" height="228" rx="24" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    k1_t1 = k1_ust + 84.0  # QA 1 (şef): satır aralığı 100; altçizgi alt satıra değmez
    k1_t2 = k1_ust + 184.0
    k1_s1_txt = "She wears her coat"
    k1_s2_txt = "in the winter."
    k1_s1_svg = (
        f'<text id="k1-s1" x="88" y="{k1_t1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" style="font-kerning:none">{k1_s1_txt}</text>'
    )
    k1_s2_svg = (
        f'<text id="k1-s2" x="88" y="{k1_t2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" style="font-kerning:none">{k1_s2_txt}</text>'
    )
    mont_svg, m_ox, m_oy, m_w, m_h = ikon_cizim_svg(MONT, 100.0, 120.0, k1_ust, "mont")
    kart1_svg_str = f'<g id="kart1">{k1_crv}{k1_s1_svg}{k1_s2_svg}{mont_svg}</g>'

    # Kart 2
    k2_ust = 1112.0
    k2_crv = f'<rect id="k2-crv" x="50" y="1114" width="980" height="228" rx="24" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    k2_t1 = k2_ust + 84.0
    k2_t2 = k2_ust + 184.0
    k2_s1_txt = "She is wearing her"
    k2_s2_txt = "pink T-shirt today."
    k2_s1_svg = (
        f'<text id="k2-s1" x="88" y="{k2_t1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" style="font-kerning:none">{k2_s1_txt}</text>'
    )
    k2_s2_svg = (
        f'<text id="k2-s2" x="88" y="{k2_t2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" style="font-kerning:none">{k2_s2_txt}</text>'
    )

    # Vurgu altçizgisi (k2-alti)
    x0_alti = 88.0 + Y.genislik("Fredoka", 700, "She ", B) - 4.0
    x1_alti = 88.0 + Y.genislik("Fredoka", 700, "She is wearing", B) + 4.0
    y_alti = k2_t1 + 0.40 * B  # QA 1: taban + max(0,28 em, g kuyruğu 0,22 em + 13) (sözleşme, 02-04-dikey s03)
    orta_alti = (x0_alti + x1_alti) / 2.0
    d_alti = f"M{x0_alti:.1f} {y_alti:.1f} Q{orta_alti:.1f} {y_alti + 3.0:.1f} {x1_alti:.1f} {y_alti + 1.0:.1f}"
    k2_alti_svg = f'<path id="k2-alti" d="{d_alti}" fill="none" stroke="{R["vurgu"]}" stroke-width="10" stroke-linecap="round"/>'

    tisort_svg, t_ox, t_oy, t_w, t_h = ikon_cizim_svg(TISORT, 100.0, 90.0, k2_ust, "tisort")
    kart2_svg_str = f'<g id="kart2">{k2_crv}{k2_s1_svg}{k2_s2_svg}{k2_alti_svg}{tisort_svg}</g>'

    # Kutular (§7.3, §7.4)
    kart1_kutu = {"ad": "kart1", "x": 48.0, "y": 864.0, "w": 984.0, "h": 232.0}
    k1_s1_w = Y.genislik("Fredoka", 700, k1_s1_txt, B)
    k1_s1_kutu = {"ad": "k1-s1", "x": 88.0, "y": k1_t1 - 0.75 * B, "w": k1_s1_w, "h": float(B)}
    k1_s2_w = Y.genislik("Fredoka", 700, k1_s2_txt, B)
    k1_s2_kutu = {"ad": "k1-s2", "x": 88.0, "y": k1_t2 - 0.75 * B, "w": k1_s2_w, "h": float(B)}
    mont_kutu = {"ad": "mont", "x": m_ox, "y": m_oy, "w": m_w, "h": m_h}

    kart2_kutu = {"ad": "kart2", "x": 48.0, "y": 1112.0, "w": 984.0, "h": 232.0}
    k2_s1_w = Y.genislik("Fredoka", 700, k2_s1_txt, B)
    k2_s1_kutu = {"ad": "k2-s1", "x": 88.0, "y": k2_t1 - 0.75 * B, "w": k2_s1_w, "h": float(B)}
    k2_s2_w = Y.genislik("Fredoka", 700, k2_s2_txt, B)
    k2_s2_kutu = {"ad": "k2-s2", "x": 88.0, "y": k2_t2 - 0.75 * B, "w": k2_s2_w, "h": float(B)}
    k2_alti_kutu = {"ad": "k2-alti", "x": x0_alti, "y": y_alti - 5.0, "w": x1_alti - x0_alti, "h": 12.0}
    tisort_kutu = {"ad": "tisort", "x": t_ox, "y": t_oy, "w": t_w, "h": t_h}

    return (
        kart1_svg_str,
        kart2_svg_str,
        kart1_kutu,
        k1_s1_kutu,
        k1_s2_kutu,
        mont_kutu,
        kart2_kutu,
        k2_s1_kutu,
        k2_s2_kutu,
        k2_alti_kutu,
        tisort_kutu,
    )


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(
    bloklar: list[dict[str, float]],
    S: int,
    B: int,
) -> None:
    """SPEC.md §7 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Bütün bloklar x ∈ [48, 1032]; hiçbir blok y + h > 1344 değil; hiçbir blok y ≥ 1536 değil.
    for b in bloklar:
        assert b["x"] >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0 - 1e-4, f"{b['ad']} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1344.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1344"
        assert b["y"] < 1536.0, f"{b['ad']} y {b['y']} >= 1536"

    # 2. Yazı boyu: başlık S ≥ 64, kart B ≥ 64 (HUD rozeti 36 hariç). Başlık 2 satır. Her satır ≤ 24 karakter.
    assert S >= 64, f"Başlık boyutu S={S} < 64"
    assert B >= 64, f"Kart yazı boyutu B={B} < 64"
    satirlar = [
        "AYNI FİİL,",
        "İKİ ZAMAN",
        "She wears her coat",
        "in the winter.",
        "She is wearing her",
        "pink T-shirt today.",
        "YDT · BASIC",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 3. Bloklar ve aralar:
    # Üst düzey hud (48, 0, 984, 288), baslik, kart1, kart2: çiftler arası kesişim 0.
    ust_duzey = [b_dict["hud"], b_dict["baslik"], b_dict["kart1"], b_dict["kart2"]]
    for i in range(len(ust_duzey)):
        for j in range(i + 1, len(ust_duzey)):
            k = kesisim(ust_duzey[i], ust_duzey[j])
            assert k == 0.0, f"Kesişim {ust_duzey[i]['ad']} - {ust_duzey[j]['ad']}: {k}"

    # baslik üstü − 288 ≥ 40 · kart1 üstü − baslik altı ≥ 48 · baslik altı ≤ 768.
    baslik_ust = b_dict["baslik"]["y"]
    baslik_alt = b_dict["baslik"]["y"] + b_dict["baslik"]["h"]
    assert baslik_ust - 288.0 >= 40.0, f"baslik üstü - 288 = {baslik_ust - 288.0} < 40"
    assert b_dict["kart1"]["y"] - baslik_alt >= 48.0, f"kart1 üstü - baslik altı = {b_dict['kart1']['y'] - baslik_alt} < 48"
    assert baslik_alt <= 768.0, f"baslik altı = {baslik_alt} > 768"

    # Kart içi (her kart): satır 1, satır 2, ikon çiftler arası kesişim 0; hepsi kart iç kutusunda (dış kutu her yandan 4 px içeri).
    # Kart 1:
    k1_ic = {"x": 48.0 + 4.0, "y": 864.0 + 4.0, "w": 984.0 - 8.0, "h": 232.0 - 8.0}
    k1_ogeler = [b_dict["k1-s1"], b_dict["k1-s2"], b_dict["mont"]]
    for og in k1_ogeler:
        assert og["x"] >= k1_ic["x"] - 1e-4, f"{og['ad']} x {og['x']} < {k1_ic['x']}"
        assert og["x"] + og["w"] <= k1_ic["x"] + k1_ic["w"] + 1e-4, f"{og['ad']} sag {og['x'] + og['w']} > {k1_ic['x'] + k1_ic['w']}"
        assert og["y"] >= k1_ic["y"] - 1e-4, f"{og['ad']} y {og['y']} < {k1_ic['y']}"
        assert og["y"] + og["h"] <= k1_ic["y"] + k1_ic["h"] + 1e-4, f"{og['ad']} alt {og['y'] + og['h']} > {k1_ic['y'] + k1_ic['h']}"
    for i in range(len(k1_ogeler)):
        for j in range(i + 1, len(k1_ogeler)):
            k = kesisim(k1_ogeler[i], k1_ogeler[j])
            assert k == 0.0, f"Kesişim {k1_ogeler[i]['ad']} - {k1_ogeler[j]['ad']}: {k}"

    # Kart 2:
    k2_ic = {"x": 48.0 + 4.0, "y": 1112.0 + 4.0, "w": 984.0 - 8.0, "h": 232.0 - 8.0}
    k2_ogeler = [b_dict["k2-s1"], b_dict["k2-s2"], b_dict["tisort"]]
    for og in k2_ogeler:
        assert og["x"] >= k2_ic["x"] - 1e-4, f"{og['ad']} x {og['x']} < {k2_ic['x']}"
        assert og["x"] + og["w"] <= k2_ic["x"] + k2_ic["w"] + 1e-4, f"{og['ad']} sag {og['x'] + og['w']} > {k2_ic['x'] + k2_ic['w']}"
        assert og["y"] >= k2_ic["y"] - 1e-4, f"{og['ad']} y {og['y']} < {k2_ic['y']}"
        assert og["y"] + og["h"] <= k2_ic["y"] + k2_ic["h"] + 1e-4, f"{og['ad']} alt {og['y'] + og['h']} > {k2_ic['y'] + k2_ic['h']}"
    for i in range(len(k2_ogeler)):
        for j in range(i + 1, len(k2_ogeler)):
            k = kesisim(k2_ogeler[i], k2_ogeler[j])
            assert k == 0.0, f"Kesişim {k2_ogeler[i]['ad']} - {k2_ogeler[j]['ad']}: {k}"

    # k2-alti kutusu: üstü ≥ k2-s1 alt · altı ≤ k2-s2 üst
    k2_alti = b_dict["k2-alti"]
    k2_s1_alt = b_dict["k2-s1"]["y"] + b_dict["k2-s1"]["h"]
    k2_s2_ust = b_dict["k2-s2"]["y"]
    assert k2_alti["y"] >= k2_s1_alt - 1e-4, f"k2-alti üst {k2_alti['y']} < k2-s1 alt {k2_s1_alt}"
    assert k2_alti["y"] + k2_alti["h"] <= k2_s2_ust + 1e-4, f"k2-alti alt {k2_alti['y'] + k2_alti['h']} > k2-s2 üst {k2_s2_ust}"

    # Her satır için 88 + g(satır, B) + 32 ≤ IKON_X
    for satir_ad in ["k1-s1", "k1-s2", "k2-s1", "k2-s2"]:
        assert 88.0 + b_dict[satir_ad]["w"] + 32.0 <= IKON_X, f"{satir_ad} sag pay > IKON_X"


def uret() -> tuple[str, int, int, list[dict[str, float]]]:
    """Sahne HTML'i, boyutları ve nesne kutularını üretir."""
    S, gmax_S, x0, T1, T2 = hesapla_baslik()
    B = hesapla_b()

    kunye = kunye_svg()
    baslik = baslik_svg(S, x0, T1, T2)
    (
        kart1,
        kart2,
        kart1_kutu,
        k1_s1_kutu,
        k1_s2_kutu,
        mont_kutu,
        kart2_kutu,
        k2_s1_kutu,
        k2_s2_kutu,
        k2_alti_kutu,
        tisort_kutu,
    ) = kartlar_svg(B)

    hud_kutu = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}
    baslik_kutu = {
        "ad": "baslik",
        "x": x0 - 6.0,
        "y": T1 - 0.93 * S - 6.0,
        "w": gmax_S + 12.0,
        "h": (T2 + 0.05 * S + 6.0) - (T1 - 0.93 * S - 6.0),
    }

    bloklar = [
        hud_kutu,
        baslik_kutu,
        kart1_kutu,
        k1_s1_kutu,
        k1_s2_kutu,
        mont_kutu,
        kart2_kutu,
        k2_s1_kutu,
        k2_s2_kutu,
        k2_alti_kutu,
        tisort_kutu,
    ]

    kurallari_dogrula(bloklar, S, B)

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
{kart1}
{kart2}
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
    return html, S, B, bloklar


if __name__ == "__main__":
    proje_dizini = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, S, B, bloklar = uret()
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
    (AD / "nesneler.json").write_text(
        json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"index.html yazıldı {len(html)}")
    print(f"S={S} B={B}")

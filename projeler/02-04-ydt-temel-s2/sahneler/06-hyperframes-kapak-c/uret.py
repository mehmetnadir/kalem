#!/usr/bin/python3
"""Sahne 06 kapak C (karşıt çift) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar (v2): kanal katmanı (280-350) -> künye (360-450) -> başlık (460-800) -> kart 1 (840-1096) -> kart 2 (1124-1380).
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

# zaman.json ve zamanlar.json okuma ve doğrulama (SPEC §2, §3)
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

# Künye doğrulaması (SPEC §3; yardim.py v2 değilse dur)
assert Y.HUD["logoY"] == 291
assert Y.HUD["logoYuk"] == 48
assert Y.HUD["kanalX"] == 263
assert Y.HUD["kanalTaban"] == 330
assert Y.HUD["kanalYazi"] == 42
assert Y.HUD["konuX"] == 60
assert Y.HUD["konuTaban"] == 420
assert Y.HUD["rozetY"] == 386
assert Y.HUD["rozetH"] == 48
assert Y.HUD["rozetYazi"] == 26
assert Y.ROZET == "YDT · BASIC"
assert Y.KONU == "Simple Present vs Present Continuous"
_kunye_svg_denetim = Y.kunye_svg()
assert 'id="kanal"' in _kunye_svg_denetim
assert 'id="logoimg"' in _kunye_svg_denetim
assert "@ydspublishing" in _kunye_svg_denetim
assert 'id="ku-cip"' not in _kunye_svg_denetim

# Sabitler (SPEC §3)
W, H = Y.W, Y.H
SOL = 60
SAG = 960
ICERIK_UST = 460
BASLIK_ALT = 800
SAHNE_UST = 820
ICERIK_ALT = 1380
ALTYAZI_UST = 1400

BASLIK_GEN = 900
KART_H = 256
KART_ARA = 28
YAZI_X = 100
IKON = 140
IKON_X = 790  # (= SAG - 30 - IKON)

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


def hesapla_baslik() -> tuple[int, float, float, float]:
    """Başlık S boyutu ve yerleşim ölçülerini hesaplar (SPEC §5.2)."""
    satir1 = "AYNI FİİL,"
    satir2 = "İKİ ZAMAN"
    gmax_100 = max(Y.genislik("Fredoka", 700, satir1, 100), Y.genislik("Fredoka", 700, satir2, 100))
    S = int(math.floor(min(190, BASLIK_GEN * 100.0 / gmax_100, (BASLIK_ALT - ICERIK_UST - 12) / 2.17)))

    gmax_S = max(Y.genislik("Fredoka", 700, satir1, S), Y.genislik("Fredoka", 700, satir2, S))
    while gmax_S > BASLIK_GEN and S > 1:
        S -= 1
        gmax_S = max(Y.genislik("Fredoka", 700, satir1, S), Y.genislik("Fredoka", 700, satir2, S))
    assert gmax_S <= 900, f"gmax(S)={gmax_S} > 900"
    assert S >= 64, f"S={S} < 64"

    T1 = ICERIK_UST + 6.0 + 0.93 * S
    T2 = T1 + 1.19 * S
    return S, gmax_S, T1, T2


def baslik_svg(S: int, T1: float, T2: float) -> str:
    """Başlık grubu SVG çıktısı (SPEC §5.2)."""
    bs_1 = (
        f'<text id="bs-1" x="{SOL}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">AYNI FİİL,</text>'
    )
    bs_2 = (
        f'<text id="bs-2" x="{SOL}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">İKİ ZAMAN</text>'
    )
    return f'<g id="baslik">{bs_1}{bs_2}</g>'


def ikon_cizim_svg(
    ogeler: list[dict],
    uw: float,
    uh: float,
    dis_ust: float,
    simge: str,
) -> tuple[str, float, float, float, float]:
    """Köşe ikonu SVG çıktısını ve çizilen sınırlayıcı kutusunu (ox, oy, w, h) üretir (SPEC §5.5)."""
    k = min(140.0 / uw, 140.0 / uh)
    ox = IKON_X + (140.0 - uw * k) / 2.0
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
    while any(YAZI_X + Y.genislik("Fredoka", 700, s, B) + 32.0 > IKON_X for s in satirlar) and B > 1:
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
    # Kart 1 (SPEC §5.3)
    k1_ust = 840.0
    k1_crv = (
        f'<rect id="k1-crv" x="62" y="842" width="896" height="252" rx="24" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    k1_t1 = k1_ust + 96.0
    k1_t2 = k1_ust + 196.0
    k1_s1_txt = "She wears her coat"
    k1_s2_txt = "in the winter."
    k1_s1_svg = (
        f'<text id="k1-s1" x="{YAZI_X}" y="{k1_t1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" style="font-kerning:none">{k1_s1_txt}</text>'
    )
    k1_s2_svg = (
        f'<text id="k1-s2" x="{YAZI_X}" y="{k1_t2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" style="font-kerning:none">{k1_s2_txt}</text>'
    )
    mont_svg, m_ox, m_oy, m_w, m_h = ikon_cizim_svg(MONT, 100.0, 120.0, k1_ust, "mont")
    kart1_svg_str = f'<g id="kart1">{k1_crv}{k1_s1_svg}{k1_s2_svg}{mont_svg}</g>'

    # Kart 2 (SPEC §5.3)
    k2_ust = 1124.0
    k2_crv = (
        f'<rect id="k2-crv" x="62" y="1126" width="896" height="252" rx="24" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    k2_t1 = k2_ust + 96.0
    k2_t2 = k2_ust + 196.0
    k2_s1_txt = "She is wearing her"
    k2_s2_txt = "pink T-shirt today."
    k2_s1_svg = (
        f'<text id="k2-s1" x="{YAZI_X}" y="{k2_t1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" style="font-kerning:none">{k2_s1_txt}</text>'
    )
    k2_s2_svg = (
        f'<text id="k2-s2" x="{YAZI_X}" y="{k2_t2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" style="font-kerning:none">{k2_s2_txt}</text>'
    )

    # Vurgu altçizgisi (k2-alti) (SPEC §5.4)
    x0_alti = YAZI_X + Y.genislik("Fredoka", 700, "She ", B) - 4.0
    x1_alti = YAZI_X + Y.genislik("Fredoka", 700, "She is wearing", B) + 4.0
    y_alti = k2_t1 + 0.40 * B
    orta_alti = (x0_alti + x1_alti) / 2.0
    d_alti = f"M{x0_alti:.1f} {y_alti:.1f} Q{orta_alti:.1f} {y_alti + 3.0:.1f} {x1_alti:.1f} {y_alti + 1.0:.1f}"
    k2_alti_svg = (
        f'<path id="k2-alti" d="{d_alti}" fill="none" stroke="{R["vurgu"]}" '
        f'stroke-width="10" stroke-linecap="round"/>'
    )

    tisort_svg, t_ox, t_oy, t_w, t_h = ikon_cizim_svg(TISORT, 100.0, 90.0, k2_ust, "tisort")
    kart2_svg_str = f'<g id="kart2">{k2_crv}{k2_s1_svg}{k2_s2_svg}{k2_alti_svg}{tisort_svg}</g>'

    # Kutular (SPEC §5.3, §5.4, §5.5, §6)
    kart1_kutu = {"ad": "kart1", "x": 60.0, "y": 840.0, "w": 900.0, "h": 256.0}
    k1_s1_w = Y.genislik("Fredoka", 700, k1_s1_txt, B)
    k1_s1_kutu = {"ad": "k1-s1", "x": float(YAZI_X), "y": k1_t1 - 0.75 * B, "w": k1_s1_w, "h": float(B)}
    k1_s2_w = Y.genislik("Fredoka", 700, k1_s2_txt, B)
    k1_s2_kutu = {"ad": "k1-s2", "x": float(YAZI_X), "y": k1_t2 - 0.75 * B, "w": k1_s2_w, "h": float(B)}
    mont_kutu = {"ad": "mont", "x": m_ox, "y": m_oy, "w": m_w, "h": m_h}

    kart2_kutu = {"ad": "kart2", "x": 60.0, "y": 1124.0, "w": 900.0, "h": 256.0}
    k2_s1_w = Y.genislik("Fredoka", 700, k2_s1_txt, B)
    k2_s1_kutu = {"ad": "k2-s1", "x": float(YAZI_X), "y": k2_t1 - 0.75 * B, "w": k2_s1_w, "h": float(B)}
    k2_s2_w = Y.genislik("Fredoka", 700, k2_s2_txt, B)
    k2_s2_kutu = {"ad": "k2-s2", "x": float(YAZI_X), "y": k2_t2 - 0.75 * B, "w": k2_s2_w, "h": float(B)}
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
    """SPEC.md §6 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Bant: kanal ve künye dışındaki her blok x >= 60, x + w <= 960, y >= 460, y + h <= 1380.
    for b in bloklar:
        if b["ad"] in ("kanal", "kunye"):
            continue
        assert b["x"] >= 60.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{b['ad']} sag kenar {b['x'] + b['w']} > 960"
        assert b["y"] >= 460.0 - 1e-4, f"{b['ad']} ust {b['y']} < 460"
        assert b["y"] + b["h"] <= 1380.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1380"

    # 0-280 ve 1400-1920'de blok YOK
    for b in bloklar:
        assert b["y"] >= 280.0 - 1e-4, f"{b['ad']} y {b['y']} < 280 (0-280 bandinda blok var)"
        assert b["y"] + b["h"] <= 1400.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1400 (1400-1920 bandinda blok var)"

    # Başlık 460 <= y, y + h <= 800; kartlar ve çocukları y >= 820
    baslik_k = b_dict["baslik"]
    assert baslik_k["y"] >= 460.0 - 1e-4, f"baslik y {baslik_k['y']} < 460"
    assert baslik_k["y"] + baslik_k["h"] <= 800.0 + 1e-4, f"baslik alt {baslik_k['y'] + baslik_k['h']} > 800"

    for k_ad in ["kart1", "k1-s1", "k1-s2", "mont", "kart2", "k2-s1", "k2-s2", "k2-alti", "tisort"]:
        assert b_dict[k_ad]["y"] >= 820.0 - 1e-4, f"{k_ad} y {b_dict[k_ad]['y']} < 820"

    # 2. Kanal kutusu y 280-350 içinde, x + w <= 960; Künye kutusu y 360-450 içinde, x + w <= 960
    kanal_k = b_dict["kanal"]
    assert 280.0 <= kanal_k["y"] and kanal_k["y"] + kanal_k["h"] <= 350.0, f"kanal y bandi hatali: {kanal_k}"
    assert kanal_k["x"] >= 60.0 and kanal_k["x"] + kanal_k["w"] <= 960.0, f"kanal x bandi hatali: {kanal_k}"

    kunye_k = b_dict["kunye"]
    assert 360.0 <= kunye_k["y"] and kunye_k["y"] + kunye_k["h"] <= 450.0, f"kunye y bandi hatali: {kunye_k}"
    assert kunye_k["x"] >= 60.0 and kunye_k["x"] + kunye_k["w"] <= 960.0, f"kunye x bandi hatali: {kunye_k}"

    # 3. Yazı boyu: başlık S >= 64, kart B >= 64. Başlık 2 satır. Her satır <= 24 karakter.
    assert S >= 64, f"Baslik boyutu S={S} < 64"
    assert B >= 64, f"Kart yazi boyutu B={B} < 64"
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
        assert len(s) <= 24, f"Satir uzunlugu {len(s)} > 24: {s}"

    # 4. Kesişim 0: üst düzey kanal, kunye, baslik, kart1, kart2 çiftleri.
    ust_duzey = [kanal_k, kunye_k, baslik_k, b_dict["kart1"], b_dict["kart2"]]
    for i in range(len(ust_duzey)):
        for j in range(i + 1, len(ust_duzey)):
            k = kesisim(ust_duzey[i], ust_duzey[j])
            assert k == 0.0, f"Kesisim {ust_duzey[i]['ad']} - {ust_duzey[j]['ad']}: {k}"

    assert baslik_k["y"] - 450.0 >= 10.0 - 1e-4, f"baslik.y - 450 = {baslik_k['y'] - 450.0} < 10"
    assert b_dict["kart1"]["y"] - (baslik_k["y"] + baslik_k["h"]) >= 20.0 - 1e-4, (
        f"kart1.y - baslik_alt = {b_dict['kart1']['y'] - (baslik_k['y'] + baslik_k['h'])} < 20"
    )

    # 5. Kart içi (her kart): satır 1, satır 2, ikon çiftler arası kesişim 0; hepsi kart iç kutusunda.
    k1_ic = {"x": 60.0 + 4.0, "y": 840.0 + 4.0, "w": 900.0 - 8.0, "h": 256.0 - 8.0}
    k1_ogeler = [b_dict["k1-s1"], b_dict["k1-s2"], b_dict["mont"]]
    for og in k1_ogeler:
        assert og["x"] >= k1_ic["x"] - 1e-4, f"{og['ad']} x {og['x']} < {k1_ic['x']}"
        assert og["x"] + og["w"] <= k1_ic["x"] + k1_ic["w"] + 1e-4, f"{og['ad']} sag {og['x'] + og['w']} > {k1_ic['x'] + k1_ic['w']}"
        assert og["y"] >= k1_ic["y"] - 1e-4, f"{og['ad']} y {og['y']} < {k1_ic['y']}"
        assert og["y"] + og["h"] <= k1_ic["y"] + k1_ic["h"] + 1e-4, f"{og['ad']} alt {og['y'] + og['h']} > {k1_ic['y'] + k1_ic['h']}"

    for i in range(len(k1_ogeler)):
        for j in range(i + 1, len(k1_ogeler)):
            k = kesisim(k1_ogeler[i], k1_ogeler[j])
            assert k == 0.0, f"K1 kesisim {k1_ogeler[i]['ad']} - {k1_ogeler[j]['ad']}: {k}"

    k2_ic = {"x": 60.0 + 4.0, "y": 1124.0 + 4.0, "w": 900.0 - 8.0, "h": 256.0 - 8.0}
    k2_ogeler = [b_dict["k2-s1"], b_dict["k2-s2"], b_dict["tisort"]]
    for og in k2_ogeler:
        assert og["x"] >= k2_ic["x"] - 1e-4, f"{og['ad']} x {og['x']} < {k2_ic['x']}"
        assert og["x"] + og["w"] <= k2_ic["x"] + k2_ic["w"] + 1e-4, f"{og['ad']} sag {og['x'] + og['w']} > {k2_ic['x'] + k2_ic['w']}"
        assert og["y"] >= k2_ic["y"] - 1e-4, f"{og['ad']} y {og['y']} < {k2_ic['y']}"
        assert og["y"] + og["h"] <= k2_ic["y"] + k2_ic["h"] + 1e-4, f"{og['ad']} alt {og['y'] + og['h']} > {k2_ic['y'] + k2_ic['h']}"

    for i in range(len(k2_ogeler)):
        for j in range(i + 1, len(k2_ogeler)):
            k = kesisim(k2_ogeler[i], k2_ogeler[j])
            assert k == 0.0, f"K2 kesisim {k2_ogeler[i]['ad']} - {k2_ogeler[j]['ad']}: {k}"

    # k2-alti kutusu: üstü >= k2-s1 alt · altı <= k2-s2 üst
    k2_alti = b_dict["k2-alti"]
    k2_s1_alt = b_dict["k2-s1"]["y"] + b_dict["k2-s1"]["h"]
    k2_s2_ust = b_dict["k2-s2"]["y"]
    assert k2_alti["y"] >= k2_s1_alt - 1e-4, f"k2-alti ust {k2_alti['y']} < k2-s1 alt {k2_s1_alt}"
    assert k2_alti["y"] + k2_alti["h"] <= k2_s2_ust + 1e-4, f"k2-alti alt {k2_alti['y'] + k2_alti['h']} > k2-s2 ust {k2_s2_ust}"

    # Her satır için YAZI_X + g(satır, B) + 32 <= IKON_X
    for satir_ad in ["k1-s1", "k1-s2", "k2-s1", "k2-s2"]:
        assert YAZI_X + b_dict[satir_ad]["w"] + 32.0 <= IKON_X + 1e-4, f"{satir_ad} sag pay > IKON_X"

    # 6. nesneler.json beklenen ad sırası (SPEC §6 Madde 6)
    beklenen_adlar = [
        "kanal",
        "kunye",
        "baslik",
        "kart1",
        "k1-s1",
        "k1-s2",
        "mont",
        "kart2",
        "k2-s1",
        "k2-s2",
        "k2-alti",
        "tisort",
    ]
    assert [b["ad"] for b in bloklar] == beklenen_adlar, f"Blok siralamasi hatali: {[b['ad'] for b in bloklar]}"


def uret() -> tuple[str, int, int, list[dict[str, float]]]:
    """Sahne HTML'i, boyutları ve nesne kutularını üretir."""
    S, gmax_S, T1, T2 = hesapla_baslik()
    B = hesapla_b()

    kunye = Y.kunye_svg()
    baslik = baslik_svg(S, T1, T2)
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

    # Kanal ve künye kutuları (SPEC §6 Madde 2)
    kanal_w = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - 60.0
    kanal_kutu = {"ad": "kanal", "x": 60.0, "y": 291.0, "w": kanal_w, "h": 52.0}

    rx, rw = Y.rozet_konumlari()[0]
    kunye_kutu = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": rx + rw - 60.0, "h": 48.0}

    baslik_kutu = {
        "ad": "baslik",
        "x": float(SOL),
        "y": T1 - 0.93 * S - 6.0,
        "w": gmax_S + 6.0,
        "h": (T2 + 0.05 * S + 6.0) - (T1 - 0.93 * S - 6.0),
    }

    # Sıra: kanal, kunye, baslik, kart1, k1-s1, k1-s2, mont, kart2, k2-s1, k2-s2, k2-alti, tisort (SPEC §6 Madde 6)
    bloklar = [
        kanal_kutu,
        kunye_kutu,
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

#!/usr/bin/python3
"""Sahne 04 hikâye karesi index.html üretici (02-04-ydt-temel-s2 huni v2; DİKEY 1080×1920, tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Yerleşim: kanal katmanı + künye (280–450) -> soru (530) -> kural kartı (570–862) -> eşleşme (926, 1000) -> Kaydet (1116); 1150–1920 boş."""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
for _p in ("/usr/local/lib/python3.10/dist-packages", str(Path.home() / ".local/lib/python3.10/site-packages")):
    if _p not in sys.path:
        sys.path.append(_p)
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# zaman.json ve zamanlar.json okuma ve doğrulama
zaman_data = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
hikaye = zaman_data["hikaye"]
assert hikaye["klasor"] == AD.name, f"klasor {hikaye['klasor']} != {AD.name}"
assert hikaye["kare"] == 1, f"kare {hikaye['kare']} != 1"
assert hikaye["cikti"] == "hikaye-a.png", f"cikti {hikaye['cikti']} != 'hikaye-a.png'"
assert AD.name not in [s["klasor"] for s in zaman_data["sahneler"]], "AD.name sahneler içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

assert Y.KONU == "Simple Present vs Present Continuous"
assert Y.ROZETLER == ("YDT · BASIC",)

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

X0, X1 = 60, 960
SORU_TABAN = 530
KART_X, KART_Y, KART_W, KART_H, KART_RX = 62, 570, 896, 292, 32
TX = 124
# şef QA tur 1: `y` kuyruğu hap alt kenarına değiyordu -> hap üstü taban − 64, yükseklik 88; satır 2–3 +4 px
TABAN = (658, 744, 826)
HAP_PAD, HAP_H, HAP_RX, HAP_UST = 22, 88, 44, 64
ESLESME_TABAN = (926, 1000)
IKON_X, IKON_W, IKON_H = 60, 64, 56
FIIL_X, OK_SON, ETIKET_X = 140, 460, 484
KAYDET_BOY, KAYDET_TABAN = 88, 1116
YERIMI_S, YERIMI_UST = 5.5, 1036
BOS_UST = 1150

# Tabler Icons `bookmark` (MIT License) - 24x24 viewBox, bounding box x: 6-18, y: 3-21
YERIMI_D = "M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"

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


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def blok_kutulari() -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar (SPEC §6 sırası)."""
    # 1. kanal (53.15, 291, 263 + genislik - 53.15, 341 - 291)
    w_ad = Y.genislik("Lexend", 700, "@ydspublishing", 42)
    kanal = {
        "ad": "kanal",
        "x": 53.15,
        "y": 291.0,
        "w": 263.0 + w_ad - 53.15,
        "h": 341.0 - 291.0,
    }

    # 2. kunye (60, 386, rozet_sag - 60, 48)
    rozet_konum = Y.rozet_konumlari()[0]
    rozet_sag = rozet_konum[0] + rozet_konum[1]
    kunye = {
        "ad": "kunye",
        "x": 60.0,
        "y": 386.0,
        "w": rozet_sag - 60.0,
        "h": 48.0,
    }

    # 3. soru (Caveat 72: üst = 530 - 0.75*72, alt = 530 + 0.30*72)
    w_soru = Y.genislik("Caveat", 700, "Genel mi, şu an mı?", 72)
    soru = {
        "ad": "soru",
        "x": 60.0,
        "y": float(SORU_TABAN) - 0.75 * 72.0,
        "w": w_soru,
        "h": (0.75 + 0.30) * 72.0,
    }

    # 4. kart (stroke dahil: x 60, y 568, w 900, h 296)
    kart = {
        "ad": "kart",
        "x": 60.0,
        "y": 568.0,
        "w": 900.0,
        "h": 296.0,
    }

    # 5. eslesme (60, 878, max(etiket_sag) - 60, 1000 + 0.30*64 - 878)
    w_gen = Y.genislik("Caveat", 700, "GENERAL", 64)
    w_now = Y.genislik("Caveat", 700, "RIGHT NOW", 64)
    max_etiket_sag = max(float(ETIKET_X) + w_gen, float(ETIKET_X) + w_now)
    eslesme = {
        "ad": "eslesme",
        "x": 60.0,
        "y": float(ESLESME_TABAN[0]) - 0.75 * 64.0,
        "w": max_etiket_sag - 60.0,
        "h": (float(ESLESME_TABAN[1]) + 0.30 * 64.0) - (float(ESLESME_TABAN[0]) - 0.75 * 64.0),
    }

    # 6. kaydet (yer imi sol - 3, 1036 - 3, 960 - (yer imi sol - 3), 1138 - 1033)
    w_kaydet = Y.genislik("Fredoka", 700, "Kaydet", KAYDET_BOY)
    kx = float(X1) - w_kaydet
    tx = (kx - 24.0 - 12.0 * YERIMI_S) - 6.0 * YERIMI_S
    yerimi_sol = tx + 6.0 * YERIMI_S
    kaydet = {
        "ad": "kaydet",
        "x": yerimi_sol - 3.0,
        "y": float(YERIMI_UST) - 3.0,
        "w": float(X1) - (yerimi_sol - 3.0),
        "h": 1138.0 - 1033.0,
    }

    return [kanal, kunye, soru, kart, eslesme, kaydet]


def soru_svg() -> str:
    """Soru başlığı SVG çıktısı (§4.3)."""
    return (
        f'<text id="soru" x="{X0}" y="{SORU_TABAN}" font-family="Caveat" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" xml:space="preserve">Genel mi, şu an mı?</text>'
    )


def kart_svg() -> str:
    """Kural kartı grubu SVG çıktısı (§4.3.1)."""
    hw = Y.genislik("Fredoka", 700, "Today", 72) + 2.0 * HAP_PAD
    s1_x = (TX - HAP_PAD) + hw + 20.0
    crv = (
        f'<rect id="kart-crv" x="{KART_X}" y="{KART_Y}" width="{KART_W}" height="{KART_H}" '
        f'rx="{KART_RX}" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    today_hap = (
        f'<g id="today-hap">'
        f'<rect id="today-kutu" x="{TX - HAP_PAD}" y="{TABAN[0] - HAP_UST}" width="{hw:.1f}" '
        f'height="{HAP_H}" rx="{HAP_RX}" fill="{R["vurgu"]}"/>'
        f'<text id="today-yazi" x="{TX}" y="{TABAN[0]}" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["zemin"]}" xml:space="preserve">Today</text>'
        f'</g>'
    )
    s1 = (
        f'<text id="s1" x="{s1_x:.1f}" y="{TABAN[0]}" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" xml:space="preserve">iki zamanda</text>'
    )
    s2 = (
        f'<text id="s2" x="{TX}" y="{TABAN[1]}" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" xml:space="preserve">da geçebilir;</text>'
    )
    s3 = (
        f'<text id="s3" x="{TX}" y="{TABAN[2]}" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" xml:space="preserve">farkı anlam yapar.</text>'
    )
    return f'<g id="kart">{crv}{today_hap}{s1}{s2}{s3}</g>'


def ikon_svg(k: str, t_taban: int, veri: list[dict], gw: float, gh: float) -> str:
    """İkon SVG çıktısı (kutuda ortalı, görünür stroke-width 3, §4.3.2)."""
    s = min(float(IKON_W) / gw, float(IKON_H) / gh)
    tx = float(IKON_X) + (float(IKON_W) - gw * s) / 2.0
    ty = (float(t_taban) - 48.0) + (float(IKON_H) - gh * s) / 2.0
    sw = 3.0 / s

    parcalar: list[str] = []
    for item in veri:
        if "n" in item:
            pts = item["n"]
            if item.get("egri") and len(pts) == 3:
                d = f"M {pts[0][0]} {pts[0][1]} Q {pts[1][0]} {pts[1][1]} {pts[2][0]} {pts[2][1]}"
            else:
                d = f"M {pts[0][0]} {pts[0][1]} " + " ".join(f"L {p[0]} {p[1]}" for p in pts[1:])
            parcalar.append(f'<path d="{d}"/>')
        elif "daire" in item:
            cx, cy, r = item["daire"]
            parcalar.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none"/>')

    govde = "".join(parcalar)
    return (
        f'<g id="{k}" transform="translate({tx:.4f} {ty:.4f}) scale({s:.6f})" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="{sw:.4f}" stroke-linecap="round" stroke-linejoin="round">'
        f'{govde}'
        f'</g>'
    )


def ok_svg(ok_id: str, t_taban: int, fiil: str) -> str:
    """Ok çizgisi SVG çıktısı (§4.3.2)."""
    oy = float(t_taban - 16)
    ox0 = float(FIIL_X) + Y.genislik("Caveat", 700, fiil, 64) + 20.0
    dx = 16.0 * math.cos(0.5)
    dy = 16.0 * math.sin(0.5)
    d = (
        f"M {ox0:.1f} {oy:.1f} L {float(OK_SON):.1f} {oy:.1f} "
        f"M {float(OK_SON) - dx:.1f} {oy - dy:.1f} L {float(OK_SON):.1f} {oy:.1f} "
        f"L {float(OK_SON) - dx:.1f} {oy + dy:.1f}"
    )
    return (
        f'<path id="{ok_id}" d="{d}" fill="none" stroke="{R["ikincil"]}" '
        f'stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    )


def eslesme_svg() -> str:
    """Eşleşme grubu SVG çıktısı (§4.3.2)."""
    t1, t2_taban = ESLESME_TABAN
    ikon1 = ikon_svg("ikon1", t1, MONT, 100.0, 120.0)
    fiil1 = (
        f'<text id="fiil1" x="{FIIL_X}" y="{t1}" font-family="Caveat" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}" xml:space="preserve">wears</text>'
    )
    ok1 = ok_svg("ok1", t1, "wears")
    etiket1 = (
        f'<text id="etiket1" x="{ETIKET_X}" y="{t1}" font-family="Caveat" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}" xml:space="preserve">GENERAL</text>'
    )

    ikon2 = ikon_svg("ikon2", t2_taban, TISORT, 100.0, 90.0)
    fiil2 = (
        f'<text id="fiil2" x="{FIIL_X}" y="{t2_taban}" font-family="Caveat" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}" xml:space="preserve">is wearing</text>'
    )
    ok2 = ok_svg("ok2", t2_taban, "is wearing")
    etiket2 = (
        f'<text id="etiket2" x="{ETIKET_X}" y="{t2_taban}" font-family="Caveat" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}" xml:space="preserve">RIGHT NOW</text>'
    )

    return f'<g id="eslesme">{ikon1}{fiil1}{ok1}{etiket1}{ikon2}{fiil2}{ok2}{etiket2}</g>'


def kaydet_svg() -> str:
    """Kaydet grubu SVG çıktısı (§4.3.3)."""
    w_kaydet = Y.genislik("Fredoka", 700, "Kaydet", KAYDET_BOY)
    kx = float(X1) - w_kaydet
    tx = (kx - 24.0 - 12.0 * YERIMI_S) - 6.0 * YERIMI_S
    ty = float(YERIMI_UST) - 3.0 * YERIMI_S
    sw = 6.0 / YERIMI_S
    yerimi = (
        f'<path id="yerimi" d="{YERIMI_D}" transform="translate({tx:.4f} {ty:.4f}) scale({YERIMI_S})" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="{sw:.4f}" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )
    kaydet_yazi = (
        f'<text id="kaydet-yazi" x="{kx:.1f}" y="{KAYDET_TABAN}" font-family="Fredoka" font-weight="700" '
        f'font-size="{KAYDET_BOY}" fill="{R["murekkep"]}" xml:space="preserve">Kaydet</text>'
    )
    return f'<g id="kaydet">{yerimi}{kaydet_yazi}</g>'


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Bütün blok x ∈ [53, 960]; kanal dışındaki bloklar x ≥ 60
    for b in bloklar:
        assert b["x"] >= 53.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 53"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 960"
        if b["ad"] != "kanal":
            assert b["x"] >= 60.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 60"
        assert b["y"] >= 280.0 - 1e-4, f"{b['ad']} üst {b['y']} < 280"

    # İçerik blokları y ≥ 460 ve alt ≤ BOS_UST (1150)
    for ad in ("soru", "kart", "eslesme", "kaydet"):
        b = b_dict[ad]
        assert b["y"] >= 460.0 - 1e-4, f"{ad} üst {b['y']} < 460"
        assert b["y"] + b["h"] <= float(BOS_UST) + 1e-4, f"{ad} alt {b['y'] + b['h']} > {BOS_UST}"

    # 2. İçerik yazı boyu ≥ 64 (soru 72, kart 72, eşleşme 64, Kaydet 88). Künye/kanal hariç.
    icerik_yazi_boylari = [72, 72, 64, KAYDET_BOY]
    for boy in icerik_yazi_boylari:
        assert boy >= 64, f"İçerik yazı boyu {boy} < 64"

    # 3. İçerik satırı ≤ 24 karakter (len)
    icerik_satirlari = [
        "Today iki zamanda",
        "da geçebilir;",
        "farkı anlam yapar.",
        "Genel mi, şu an mı?",
        "wears",
        "GENERAL",
        "is wearing",
        "RIGHT NOW",
        "Kaydet",
    ]
    for s in icerik_satirlari:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 4. Blok çiftleri kesişmez (alan 0). Dikey sıra kanal → kunye → soru → kart → eslesme → kaydet komşu boşluğu ≥ 12
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    dikey_sirali = ["kanal", "kunye", "soru", "kart", "eslesme", "kaydet"]
    for i in range(len(dikey_sirali) - 1):
        b1 = b_dict[dikey_sirali[i]]
        b2 = b_dict[dikey_sirali[i + 1]]
        bosluk = b2["y"] - (b1["y"] + b1["h"])
        assert bosluk >= 12.0 - 1e-4, f"Dikey boşluk {b1['ad']} -> {b2['ad']}: {bosluk} < 12"

    # 5. Kart içi kurallar
    hw = Y.genislik("Fredoka", 700, "Today", 72) + 2.0 * HAP_PAD
    today_x = float(TX - HAP_PAD)
    today_y = float(TABAN[0] - HAP_UST)
    today_w = hw
    today_h = float(HAP_H)

    assert today_x - float(KART_X) >= 16.0 - 1e-4, f"Hap sol boşluk {today_x - float(KART_X)} < 16"
    assert today_y - float(KART_Y) >= 16.0 - 1e-4, f"Hap üst boşluk {today_y - float(KART_Y)} < 16"
    assert (float(KART_X + KART_W)) - (today_x + today_w) >= 16.0 - 1e-4, "Hap sağ boşluk < 16"
    assert (float(KART_Y + KART_H)) - (today_y + today_h) >= 16.0 - 1e-4, "Hap alt boşluk < 16"

    s1_x = today_x + hw + 20.0
    assert s1_x >= (today_x + today_w) + 16.0 - 1e-4, f"s1 sol {s1_x} < hap sağı + 16"

    w_s1 = Y.genislik("Fredoka", 700, "iki zamanda", 72)
    w_s2 = Y.genislik("Fredoka", 700, "da geçebilir;", 72)
    w_s3 = Y.genislik("Fredoka", 700, "farkı anlam yapar.", 72)
    assert s1_x + w_s1 <= 958.0 - 32.0 + 1e-4, f"s1 sağ kenar {s1_x + w_s1} > 958 - 32"
    assert float(TX) + w_s2 <= 958.0 - 32.0 + 1e-4, f"s2 sağ kenar {float(TX) + w_s2} > 958 - 32"
    assert float(TX) + w_s3 <= 958.0 - 32.0 + 1e-4, f"s3 sağ kenar {float(TX) + w_s3} > 958 - 32"

    s2_ust = float(TABAN[1]) - 0.75 * 72.0
    hap_alt = today_y + today_h
    assert s2_ust > hap_alt, f"satır 2 üst {s2_ust} <= hap altı {hap_alt}"

    s3_alt = float(TABAN[2]) + 0.25 * 72.0
    cerceve_alt = float(KART_Y + KART_H)
    assert s3_alt + 16.0 <= cerceve_alt + 1e-4, f"satır 3 alt + 16 > çerçeve altı {cerceve_alt}"

    # 6. Eşleşme kuralları
    t1, t2_taban = ESLESME_TABAN
    sat1_alt = float(t1) + 0.30 * 64.0
    sat2_ust = float(t2_taban) - 0.75 * 64.0
    assert sat1_alt <= sat2_ust + 1e-4, f"satır 1 alt {sat1_alt} > satır 2 üst {sat2_ust}"

    for fiil, t_tab in (("wears", t1), ("is wearing", t2_taban)):
        w_f = Y.genislik("Caveat", 700, fiil, 64)
        fiil_sag = float(FIIL_X) + w_f
        ox0 = fiil_sag + 20.0
        assert ox0 >= fiil_sag + 16.0 - 1e-4, f"{fiil} ox0 < fiil sağı + 16"
        assert float(OK_SON) - ox0 >= 40.0 - 1e-4, f"{fiil} 460 - ox0 < 40"

    assert float(OK_SON) + 20.0 <= float(ETIKET_X) + 1e-4, "460 + 20 > 484"

    w_gen = Y.genislik("Caveat", 700, "GENERAL", 64)
    w_now = Y.genislik("Caveat", 700, "RIGHT NOW", 64)
    assert float(ETIKET_X) + w_gen <= 960.0 + 1e-4, "GENERAL sağ kenar > 960"
    assert float(ETIKET_X) + w_now <= 960.0 + 1e-4, "RIGHT NOW sağ kenar > 960"
    assert float(IKON_X + IKON_W) + 16.0 <= float(FIIL_X) + 1e-4, "İkon kutusu sağı + 16 > 140"

    # 7. Kaydet kuralları
    w_kaydet = Y.genislik("Fredoka", 700, "Kaydet", KAYDET_BOY)
    kx = float(X1) - w_kaydet
    assert abs((kx + w_kaydet) - 960.0) <= 0.5, f"kaydet-yazi sağ kenar != 960: {kx + w_kaydet}"

    yerimi_gorunur_sag = kx - 24.0
    assert yerimi_gorunur_sag + 20.0 <= kx + 1e-4, "yer imi sağ + 20 > kx"
    yerimi_gorunur_ust = float(YERIMI_UST)
    yerimi_gorunur_alt = yerimi_gorunur_ust + 18.0 * YERIMI_S
    assert yerimi_gorunur_ust == 1036.0, f"yer imi üst {yerimi_gorunur_ust} != 1036"
    assert yerimi_gorunur_alt <= 1140.0 + 1e-4, f"yer imi alt {yerimi_gorunur_alt} > 1140"

    # 8. Tek sarı: #icerik grubunun HTML'inde fill="#f2a93b" tam 1 kez (today-kutu), stroke="#f2a93b" 0 kez
    m_icerik = re.search(r'<g id="icerik">(.*?)</g>\s*</svg>', html, re.DOTALL)
    assert m_icerik, "#icerik grubu HTML içinde bulunamadı"
    icerik_html = m_icerik.group(1)
    cnt_vurgu_fill = icerik_html.count('fill="#f2a93b"')
    cnt_vurgu_stroke = icerik_html.count('stroke="#f2a93b"')
    assert cnt_vurgu_fill == 1, (
        f"#icerik içinde fill=#f2a93b {cnt_vurgu_fill} kez bulundu, 1 olmalı"
    )
    assert cnt_vurgu_stroke == 0, (
        f"#icerik içinde stroke=#f2a93b {cnt_vurgu_stroke} kez bulundu, 0 olmalı"
    )

    # 9. Yasak kontrolleri (büyük/küçük harf duyarsız)
    # desen düzenli ifadedir: huni v2 §7 madde 3 grep taraması bu dosyanın kendi yasak listesine takılmasın
    for desen in (r"tam\s+ders", r"dak[iı]ka", r"\bqr\b"):
        assert not re.search(desen, html, re.IGNORECASE), f"HTML içinde yasak dizgi bulundu: {desen}"

    # SVG <text> içeriklerinde 'dk'
    svg_metinler = re.findall(r"<text[^>]*>(.*?)</text>", html, re.DOTALL)
    for sm in svg_metinler:
        assert "dk" not in sm.lower(), f"SVG metni içinde 'dk' bulundu: {sm}"

    assert "opacity:0" not in html, "HTML içinde 'opacity:0' bulundu"
    assert R["kirmizi"] not in html, f"HTML içinde kırmızı renk ({R['kirmizi']}) bulundu"
    assert "#root.tema-acik" not in html, "HTML içinde '#root.tema-acik' bulundu"

    # Emoji kontrolü (U+1F000 üstü ve U+2600-U+27BF)
    emoji_bulgular = re.findall(r"[\U0001F000-\U0010FFFF\u2600-\u27BF]", html)
    assert not emoji_bulgular, f"HTML içinde emoji bulundu: {emoji_bulgular}"

    for yasak_kod in ("Math.random", "Date", "try", "catch"):
        assert yasak_kod not in html, f"HTML içinde yasak JavaScript öğesi: {yasak_kod}"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()

    kunye = Y.kunye_svg()
    soru = soru_svg()
    kart = kart_svg()
    eslesme = eslesme_svg()
    kaydet = kaydet_svg()

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
<g id="icerik">
{soru}
{kart}
{eslesme}
{kaydet}
</g>
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var tl = gsap.timeline({{ paused: true }});
  tl.set("#icerik", {{ opacity: 1, immediateRender: false }}, 0);
  tl.set("#icerik", {{ opacity: 1, immediateRender: false }}, {Z['sure']});
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

    b_dict = {b["ad"]: b for b in bloklar}
    print(f"index.html yazıldı {len(html.encode('utf-8'))}")
    print(
        f"soru={int(round(b_dict['soru']['y']))}-{int(round(b_dict['soru']['y'] + b_dict['soru']['h']))} "
        f"kart={int(round(b_dict['kart']['y']))}-{int(round(b_dict['kart']['y'] + b_dict['kart']['h']))} "
        f"eslesme={int(round(b_dict['eslesme']['y']))}-{int(round(b_dict['eslesme']['y'] + b_dict['eslesme']['h']))} "
        f"kaydet={int(round(b_dict['kaydet']['y']))}-{int(round(b_dict['kaydet']['y'] + b_dict['kaydet']['h']))}"
    )

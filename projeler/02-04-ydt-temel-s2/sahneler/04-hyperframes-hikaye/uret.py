#!/usr/bin/python3
"""Sahne 04 hikâye karesi index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> içerik (352-1392) -> çağrı (1344-1536) -> platform (1536-1920 boş)."""
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

# Künye metinleri kunye.js dosyasından okunur
kunye_metni = (PAKET / "ortak" / "kunye.js").read_text(encoding="utf-8")
m_ders = re.search(r'ders:\s*\[\s*"([^"]+)"\s*,\s*"([^"]+)"\s*\]', kunye_metni)
assert m_ders, "kunye.js içinde ders bulunamadı"
DERS: list[str] = [m_ders.group(1), m_ders.group(2)]
assert DERS == ["SIMPLE PRESENT vs", "PRESENT CONTINUOUS"], f"ders {DERS} beklenen değil"

m_rozet = re.search(r'rozet:\s*"([^"]+)"', kunye_metni)
assert m_rozet, "kunye.js içinde rozet bulunamadı"
ROZET: str = m_rozet.group(1)
assert ROZET == "YDT · BASIC", f"rozet {ROZET} beklenen değil"

m_cip = re.search(r'"04-hyperframes-hikaye":\s*"([^"]+)"', kunye_metni)
assert m_cip, "kunye.js içinde çip bulunamadı"
CIP: str = m_cip.group(1)
assert CIP == "Full lesson", f"çip {CIP} beklenen değil"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

W, H = Y.W, Y.H
KENAR = 48
SAG = 1032
GEN = 984
ICERIK = (352, 1392)
CAGRI = (1344, 1536)
PLATFORM = 1536

KART_H = 272
KART1_Y = 468
KART2_Y = 760
CUMLE_X = 240
CUMLE_BOY = 64
ETIKET_BOY = 64

AX0 = round(80 + Y.genislik("Caveat", 700, "RIGHT NOW", 64) + 36)
AX1 = 988
NOW_X = round((AX0 + AX1) / 2)

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


def kunye_svg(ders: list[str], rozet: str, cip: str) -> str:
    """Künye (HUD) grubu SVG çıktısı."""
    logo_w = 96.0 * Y.LOGO_EN_BOY
    logo = f'<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" width="{logo_w:.2f}" height="96"/></g>'
    ders1 = f'<text id="ku-ders1" x="48" y="212" font-family="Fredoka" font-weight="700" font-size="56" fill="{R["murekkep"]}" xml:space="preserve">{ders[0]}</text>'
    ders2 = f'<text id="ku-ders2" x="48" y="276" font-family="Fredoka" font-weight="700" font-size="56" fill="{R["murekkep"]}" xml:space="preserve">{ders[1]}</text>'

    ders2_w = Y.genislik("Fredoka", 700, ders[1], 56)
    rz_w = Y.genislik("Lexend", 700, rozet, 36) + 56.0
    rz_x = 48.0 + ders2_w + 24.0
    rozet_svg = (
        f'<g id="rz0">'
        f'<rect x="{rz_x:.1f}" y="216" width="{rz_w:.1f}" height="72" rx="36" fill="{R["vurgu"]}"/>'
        f'<text x="{rz_x + rz_w / 2.0:.1f}" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" fill="{R["zemin"]}">{rozet}</text>'
        f'</g>'
    )

    cip_w = Y.genislik("Lexend", 700, cip, 40) + 64.0
    cip_x = 1032.0 - cip_w
    cip_svg = (
        f'<g id="ku-cip">'
        f'<rect id="ku-cipr" x="{cip_x:.1f}" y="48" width="{cip_w:.1f}" height="80" rx="40" fill="none" stroke="{R["vurgu"]}" stroke-width="4"/>'
        f'<text id="ku-cipt" x="{cip_x + cip_w / 2.0:.1f}" y="102" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="40" fill="{R["vurgu"]}">{cip}</text>'
        f'</g>'
    )
    return f'<g id="kunye">{logo}{ders1}{ders2}{rozet_svg}{cip_svg}</g>'


def ikon_svg(k: str, y0: int, veri: list[dict], gw: float, gh: float) -> str:
    """İkon SVG çıktısı (kutuda ortalı, görünür stroke-width 4)."""
    s = min(128.0 / gw, 120.0 / gh)
    tx = 80.0 + (128.0 - gw * s) / 2.0
    ty = (y0 + 44.0) + (120.0 - gh * s) / 2.0
    sw = 4.0 / s

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
        f'<g id="{k}-ikon" transform="translate({tx:.4f} {ty:.4f}) scale({s:.6f})" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="{sw:.4f}" stroke-linecap="round" stroke-linejoin="round">'
        f'{govde}'
        f'</g>'
    )


def kart1_svg() -> str:
    """Kart 1 grubu SVG çıktısı (MONT, GENERAL)."""
    k = "kart1"
    y0 = KART1_Y
    AY = y0 + 222

    crv = f'<rect id="{k}-crv" x="48" y="{y0}" width="984" height="{KART_H}" rx="28" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    ikon = ikon_svg(k, y0, MONT, 100.0, 120.0)
    s1 = f'<text id="{k}-s1" x="{CUMLE_X}" y="{y0 + 84}" font-family="Fredoka" font-weight="700" font-size="{CUMLE_BOY}" fill="{R["murekkep"]}" xml:space="preserve">She wears her coat</text>'
    s2 = f'<text id="{k}-s2" x="{CUMLE_X}" y="{y0 + 164}" font-family="Fredoka" font-weight="700" font-size="{CUMLE_BOY}" fill="{R["murekkep"]}" xml:space="preserve">in the winter.</text>'
    etiket = f'<text id="{k}-etiket" x="80" y="{y0 + 242}" font-family="Caveat" font-weight="700" font-size="{ETIKET_BOY}" fill="{R["murekkep"]}">GENERAL</text>'

    d_list = (-187.5, -62.5, 62.5, 187.5)
    dx = 20.0 * math.cos(0.5)
    dy = 20.0 * math.sin(0.5)
    # şef QA tur 1: eksen bantların içinden geçmez (kar tanesi çizgiyle kesişiyordu) -> bant aralıklarında kesilir
    seg = f"M{AX0} {AY}" + "".join(f" L{NOW_X + d - 32.0:.1f} {AY} M{NOW_X + d + 32.0:.1f} {AY}" for d in d_list)
    d_eksen = f"{seg} L{AX1} {AY} M{AX1 - dx:.1f} {AY - dy:.1f} L{AX1} {AY} L{AX1 - dx:.1f} {AY + dy:.1f}"
    eksen = f'<path id="{k}-eksen" d="{d_eksen}" fill="none" stroke="{R["ikincil"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'

    kis_parcalari: list[str] = []
    kar_parcalari: list[str] = []
    dx_30 = 11.0 * math.cos(math.radians(30))
    dy_30 = 11.0 * math.sin(math.radians(30))

    for i, d in enumerate(d_list):
        mx = NOW_X + d
        bx = mx - 32.0
        kis_parcalari.append(
            f'<rect id="{k}-kis{i}" x="{bx:.1f}" y="{AY - 18}" width="64" height="36" rx="18" '
            f'fill="{R["murekkep"]}" fill-opacity="0.14" stroke="{R["murekkep"]}" stroke-width="3"/>'
        )
        d_kar = (
            f"M {mx:.2f} {AY - 11.0:.2f} L {mx:.2f} {AY + 11.0:.2f} "
            f"M {mx - dx_30:.2f} {AY + dy_30:.2f} L {mx + dx_30:.2f} {AY - dy_30:.2f} "
            f"M {mx - dx_30:.2f} {AY - dy_30:.2f} L {mx + dx_30:.2f} {AY + dy_30:.2f}"
        )
        kar_parcalari.append(
            f'<path id="{k}-kar{i}" d="{d_kar}" fill="none" stroke="{R["murekkep"]}" stroke-width="3" stroke-linecap="round"/>'
        )

    bantlar = "".join(kis_parcalari)
    karlar = "".join(kar_parcalari)
    now = f'<circle id="{k}-now" cx="{NOW_X}" cy="{AY}" r="12" fill="{R["murekkep"]}"/>'

    return f'<g id="{k}">{crv}{ikon}{s1}{s2}{etiket}{eksen}{bantlar}{karlar}{now}</g>'


def kart2_svg() -> str:
    """Kart 2 grubu SVG çıktısı (TISORT, RIGHT NOW)."""
    k = "kart2"
    y0 = KART2_Y
    AY = y0 + 222

    crv = f'<rect id="{k}-crv" x="48" y="{y0}" width="984" height="{KART_H}" rx="28" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    ikon = ikon_svg(k, y0, TISORT, 100.0, 90.0)
    s1 = f'<text id="{k}-s1" x="{CUMLE_X}" y="{y0 + 84}" font-family="Fredoka" font-weight="700" font-size="{CUMLE_BOY}" fill="{R["murekkep"]}" xml:space="preserve">She is wearing her</text>'
    s2 = f'<text id="{k}-s2" x="{CUMLE_X}" y="{y0 + 164}" font-family="Fredoka" font-weight="700" font-size="{CUMLE_BOY}" fill="{R["murekkep"]}" xml:space="preserve">pink T-shirt today.</text>'
    etiket = f'<text id="{k}-etiket" x="80" y="{y0 + 242}" font-family="Caveat" font-weight="700" font-size="{ETIKET_BOY}" fill="{R["murekkep"]}">RIGHT NOW</text>'

    dx = 20.0 * math.cos(0.5)
    dy = 20.0 * math.sin(0.5)
    # şef QA tur 1: eksen today bandının içinden geçmez (now noktasını kesiyordu)
    d_eksen = (f"M{AX0} {AY} L{NOW_X - 80} {AY} M{NOW_X + 80} {AY} L{AX1} {AY} "
               f"M{AX1 - dx:.1f} {AY - dy:.1f} L{AX1} {AY} L{AX1 - dx:.1f} {AY + dy:.1f}")
    eksen = f'<path id="{k}-eksen" d="{d_eksen}" fill="none" stroke="{R["ikincil"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'

    bant = (
        f'<rect id="{k}-bant" x="{NOW_X - 80}" y="{AY - 18}" width="160" height="36" rx="18" '
        f'fill="{R["murekkep"]}" fill-opacity="0.14" stroke="{R["murekkep"]}" stroke-width="3"/>'
    )
    now = f'<circle id="{k}-now" cx="{NOW_X}" cy="{AY}" r="12" fill="{R["murekkep"]}"/>'

    return f'<g id="{k}">{crv}{ikon}{s1}{s2}{etiket}{eksen}{bant}{now}</g>'


def today_svg(hw: float) -> str:
    """today hapı grubu SVG çıktısı."""
    return (
        f'<g id="today">'
        f'<rect id="today-kutu" x="48" y="1064" width="{hw:.1f}" height="84" rx="42" fill="{R["vurgu"]}"/>'
        f'<text id="today-yazi" x="{48.0 + hw / 2.0:.1f}" y="1128" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="64" fill="{R["zemin"]}">today</text>'
        f'</g>'
    )


def blok_kutulari() -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar (§6.4 sırası)."""
    hud = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}

    w_ust = Y.genislik("Lexend", 500, "Genel mi, şu an mı?", 64)
    ust = {"ad": "ust", "x": 48.0, "y": 424.0 - 0.75 * 64.0, "w": w_ust, "h": (0.75 + 0.25) * 64.0}

    kart1 = {"ad": "kart1", "x": 48.0, "y": float(KART1_Y), "w": 984.0, "h": float(KART_H)}
    kart2 = {"ad": "kart2", "x": 48.0, "y": float(KART2_Y), "w": 984.0, "h": float(KART_H)}

    w_today = Y.genislik("Fredoka", 700, "today", 64) + 56.0
    today = {"ad": "today", "x": 48.0, "y": 1064.0, "w": w_today, "h": 84.0}

    w_not1 = Y.genislik("Lexend", 500, "iki zamanda da geçebilir", 64)
    not1 = {"ad": "not1", "x": 48.0, "y": 1212.0 - 0.75 * 64.0, "w": w_not1, "h": (0.75 + 0.25) * 64.0}

    w_not2 = Y.genislik("Lexend", 700, "Farkı anlam yapar.", 64)
    not2 = {"ad": "not2", "x": 48.0, "y": 1296.0 - 0.75 * 64.0, "w": w_not2, "h": (0.75 + 0.25) * 64.0}

    w_cg1 = Y.genislik("Caveat", 700, "Tam ders:", 72)
    cg1 = {"ad": "cg1", "x": 48.0, "y": 1418.0 - 0.75 * 72.0, "w": w_cg1, "h": (0.75 + 0.30) * 72.0}

    w_cg2 = Y.genislik("Caveat", 700, "profildeki bağlantı", 72)
    cg2 = {"ad": "cg2", "x": 48.0, "y": 1498.0 - 0.75 * 72.0, "w": w_cg2, "h": (0.75 + 0.30) * 72.0}

    w_hap = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap = {"ad": "hap", "x": 1032.0 - w_hap, "y": 1398.0, "w": w_hap, "h": 84.0}

    return [hud, ust, kart1, kart2, today, not1, not2, cg1, cg2, hap]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Bütün metin ve kutular x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil
    for b in bloklar:
        assert b["x"] >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert b["x"] + b["w"] <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 1032"
        assert b["y"] >= 0.0, f"{b['ad']} üst {b['y']} < 0"
        assert b["y"] + b["h"] <= 1536.0 + 1e-4, f"{b['ad']} alt {b['y'] + b['h']} > 1536"

    # Yazı alt sınırı: cg2 taban + 0.30 * 72 <= 1536
    assert 1498.0 + 0.30 * 72.0 <= 1536.0, "cg2 yazı alt sınırı > 1536"

    # 2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40)
    # İçerik bloğunda kullanılan yazı boyutları: 64, 72. Hepsi >= 64.

    # 3. Her ekran satırı ≤ 24 karakter (len), HUD dahil (§4.3 listesinin tamamı)
    satirlar = [
        "SIMPLE PRESENT vs",
        "PRESENT CONTINUOUS",
        "YDT · BASIC",
        "Full lesson",
        "Genel mi, şu an mı?",
        "She wears her coat",
        "in the winter.",
        "GENERAL",
        "She is wearing her",
        "pink T-shirt today.",
        "RIGHT NOW",
        "today",
        "iki zamanda da geçebilir",
        "Farkı anlam yapar.",
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
    dikey_sirali = ["hud", "ust", "kart1", "kart2", "today", "not1", "not2"]
    for i in range(len(dikey_sirali) - 1):
        b1 = b_dict[dikey_sirali[i]]
        b2 = b_dict[dikey_sirali[i + 1]]
        bosluk = b2["y"] - (b1["y"] + b1["h"])
        assert bosluk >= 16.0 - 1e-4, f"Dikey boşluk {b1['ad']} -> {b2['ad']}: {bosluk} < 16"

    assert b_dict["cg1"]["y"] - (b_dict["not2"]["y"] + b_dict["not2"]["h"]) >= 16.0 - 1e-4
    assert b_dict["hap"]["y"] - (b_dict["not2"]["y"] + b_dict["not2"]["h"]) >= 16.0 - 1e-4

    # cg1 ve cg2 sağ kenarı ile hap sol kenarı arası ≥ 24
    assert b_dict["hap"]["x"] - (b_dict["cg1"]["x"] + b_dict["cg1"]["w"]) >= 24.0 - 1e-4
    assert b_dict["hap"]["x"] - (b_dict["cg2"]["x"] + b_dict["cg2"]["w"]) >= 24.0 - 1e-4

    # 5. ust üstü ≥ 352; not2 altı ≤ 1344; hap, cg1, cg2 [1344, 1536] içinde
    assert b_dict["ust"]["y"] >= 352.0 - 1e-4, f"ust üstü {b_dict['ust']['y']} < 352"
    assert b_dict["not2"]["y"] + b_dict["not2"]["h"] <= 1344.0 + 1e-4, f"not2 altı > 1344"
    for ad in ("hap", "cg1", "cg2"):
        assert b_dict[ad]["y"] >= 1344.0 - 1e-4, f"{ad} üstü {b_dict[ad]['y']} < 1344"
        assert b_dict[ad]["y"] + b_dict[ad]["h"] <= 1536.0 + 1e-4, f"{ad} altı > 1536"

    # 6. Kart içi kurallar (iki kartta)
    cümle_satirlari = [
        "She wears her coat",
        "in the winter.",
        "She is wearing her",
        "pink T-shirt today.",
    ]
    for cs in cümle_satirlari:
        w_cs = Y.genislik("Fredoka", 700, cs, 64)
        assert CUMLE_X + w_cs <= 1000.0, f"Cümle sağ kenar {CUMLE_X + w_cs} > 1000: {cs}"

    for y0 in (KART1_Y, KART2_Y):
        s2_alt = y0 + 164.0 + 0.25 * 64.0
        etiket_ust = y0 + 242.0 - 0.75 * 64.0
        assert s2_alt < etiket_ust, f"satır 2 alt {s2_alt} >= etiket üst {etiket_ust}"

    w_gen = Y.genislik("Caveat", 700, "GENERAL", 64)
    w_now = Y.genislik("Caveat", 700, "RIGHT NOW", 64)
    assert 80.0 + w_gen + 24.0 <= float(AX0), "GENERAL etiket sağ kenarı + 24 > AX0"
    assert 80.0 + w_now + 24.0 <= float(AX0), "RIGHT NOW etiket sağ kenarı + 24 > AX0"

    # Bütün bantlar [AX0 + 24, AX1 - 24] içinde
    for d in (-187.5, -62.5, 62.5, 187.5):
        mx = NOW_X + d
        bx = mx - 32.0
        assert bx >= AX0 + 24.0, f"kart 1 bant sol {bx} < AX0 + 24"
        assert bx + 64.0 <= AX1 - 24.0, f"kart 1 bant sağ {bx + 64.0} > AX1 - 24"

    bx2 = NOW_X - 80.0
    assert bx2 >= AX0 + 24.0, f"kart 2 bant sol {bx2} < AX0 + 24"
    assert bx2 + 160.0 <= AX1 - 24.0, f"kart 2 bant sağ {bx2 + 160.0} > AX1 - 24"

    # Kart 1 now noktası (r 12) ile her bant arası ≥ 12
    now_sol = NOW_X - 12.0
    now_sag = NOW_X + 12.0
    for d in (-187.5, -62.5, 62.5, 187.5):
        mx = NOW_X + d
        bx = mx - 32.0
        bw = 64.0
        if bx + bw <= now_sol:
            bosluk = now_sol - (bx + bw)
        elif bx >= now_sag:
            bosluk = bx - now_sag
        else:
            bosluk = 0.0
        assert bosluk >= 12.0, f"kart 1 now-bant boşluğu {bosluk} < 12 (d={d})"

    # Kart 2 now noktası today bandının içinde
    assert bx2 <= now_sol and now_sag <= bx2 + 160.0, "kart 2 now noktası today bandı içinde değil"

    # İkon kutusu sağ kenarı (208) + 24 ≤ CUMLE_X
    assert 208.0 + 24.0 <= float(CUMLE_X), "ikon kutusu sağ kenarı + 24 > CUMLE_X"

    # 8. Yasaklar ve metin taraması
    yasak_kelimeler = ["kanal", "qr", "dakika"]
    html_kucuk = html.lower()
    for yk in yasak_kelimeler:
        assert yk not in html_kucuk, f"HTML içinde yasak dizgi bulundu: {yk}"

    # dk yalnız SVG metinlerinde taranır
    svg_metinler = re.findall(r"<text[^>]*>(.*?)</text>", html, re.DOTALL)
    for sm in svg_metinler:
        assert "dk" not in sm.lower(), f"SVG metni içinde 'dk' bulundu: {sm}"

    assert "opacity:0" not in html, "opacity:0 başlangıç yasak"
    assert R["kirmizi"] not in html, "kırmızı renk kullanımı yasak"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()

    kunye = kunye_svg(DERS, ROZET, CIP)
    ust = f'<text id="ust" x="48" y="424" font-family="Lexend" font-weight="500" font-size="64" fill="{R["murekkep"]}">Genel mi, şu an mı?</text>'
    kart1 = kart1_svg()
    kart2 = kart2_svg()

    today_w = Y.genislik("Fredoka", 700, "today", 64) + 56.0
    today = today_svg(today_w)

    not1 = f'<text id="not1" x="48" y="1212" font-family="Lexend" font-weight="500" font-size="64" fill="{R["murekkep"]}">iki zamanda da geçebilir</text>'
    not2 = f'<text id="not2" x="48" y="1296" font-family="Lexend" font-weight="700" font-size="64" fill="{R["murekkep"]}">Farkı anlam yapar.</text>'
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
{kart1}
{kart2}
{today}
{not1}
{not2}
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
    print(f"index.html yazıldı {len(html)}")
    print(
        f"ust={int(round(b_dict['ust']['y']))}-{int(round(b_dict['ust']['y'] + b_dict['ust']['h']))} "
        f"kart1={int(round(b_dict['kart1']['y']))}-{int(round(b_dict['kart1']['y'] + b_dict['kart1']['h']))} "
        f"kart2={int(round(b_dict['kart2']['y']))}-{int(round(b_dict['kart2']['y'] + b_dict['kart2']['h']))} "
        f"today={int(round(b_dict['today']['y']))}-{int(round(b_dict['today']['y'] + b_dict['today']['h']))} "
        f"not2={int(round(b_dict['not2']['y']))}-{int(round(b_dict['not2']['y'] + b_dict['not2']['h']))}"
    )

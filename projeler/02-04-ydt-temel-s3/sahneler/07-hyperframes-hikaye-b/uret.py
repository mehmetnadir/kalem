#!/usr/bin/python3
"""Sahne 07 hikâye karesi B (soru kartı) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
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

# Çip metni: PAKET / "ortak" / "kunye.js" dosyasını oku; "07-hyperframes-hikaye-b": "<metin>" deseninden regex ile al
kunye_js = (PAKET / "ortak" / "kunye.js").read_text(encoding="utf-8")
cip_match = re.search(r'"07-hyperframes-hikaye-b":\s*"([^"]+)"', kunye_js)
assert cip_match, "kunye.js içinde 07-hyperframes-hikaye-b çip metni bulunamadı"
CIP_METIN = cip_match.group(1)
assert CIP_METIN == "Full lesson", f"Beklenen çip 'Full lesson', bulunan: '{CIP_METIN}'"

W, H = Y.W, Y.H
KENAR = 48
SAG = 1032
ICERIK = (352, 1392)
CAGRI = (1344, 1536)
PLATFORM = 1536


def soru_svg() -> str:
    """Soru başlığı SVG çıktısı (§4.1)."""
    return (
        f'<text id="soru" x="48" y="448" font-family="Fredoka" font-weight="700" '
        f'font-size="96" fill="{R["murekkep"]}" xml:space="preserve">Tarife mi, plan mı?</text>'
    )


def tren_svg() -> str:
    """Tren çizimi grubu SVG çıktısı (§4.2.1)."""
    mur = R["murekkep"]
    ikn = R["ikincil"]
    s = 1.2
    ox, oy = 100.0, 580.0

    def px(x: float) -> float:
        return ox + s * x

    def py(y: float) -> float:
        return oy + s * y

    parcalar = [
        # lokomotif gövdesi: rect 200, 55, 170, 75 | 4,8 | murekkep
        f'<rect x="{px(200):.1f}" y="{py(55):.1f}" width="{s * 170:.1f}" height="{s * 75:.1f}" rx="6" stroke="{mur}" stroke-width="4.8"/>',
        # kabin: rect 200, 10, 75, 45 | 4,8 | murekkep
        f'<rect x="{px(200):.1f}" y="{py(10):.1f}" width="{s * 75:.1f}" height="{s * 45:.1f}" rx="6" stroke="{mur}" stroke-width="4.8"/>',
        # baca: rect 320, 22, 26, 33 | 4,0 | murekkep
        f'<rect x="{px(320):.1f}" y="{py(22):.1f}" width="{s * 26:.1f}" height="{s * 33:.1f}" rx="6" stroke="{mur}" stroke-width="4"/>',
        # ön burun: polyline (370,95) → (398,130) → (370,130) | 4,8 | murekkep
        f'<polyline points="{px(370):.1f},{py(95):.1f} {px(398):.1f},{py(130):.1f} {px(370):.1f},{py(130):.1f}" stroke="{mur}" stroke-width="4.8"/>',
        # vagon: rect 0, 45, 175, 85 | 4,8 | murekkep
        f'<rect x="{px(0):.1f}" y="{py(45):.1f}" width="{s * 175:.1f}" height="{s * 85:.1f}" rx="6" stroke="{mur}" stroke-width="4.8"/>',
        # bağlantı: line (175,112) → (200,112) | 4,0 | murekkep
        f'<line x1="{px(175):.1f}" y1="{py(112):.1f}" x2="{px(200):.1f}" y2="{py(112):.1f}" stroke="{mur}" stroke-width="4"/>',
        # vagon camları: rect 20, 60, 50, 30 · rect 100, 60, 50, 30 | 4,0 | murekkep
        f'<rect x="{px(20):.1f}" y="{py(60):.1f}" width="{s * 50:.1f}" height="{s * 30:.1f}" rx="6" stroke="{mur}" stroke-width="4"/>',
        f'<rect x="{px(100):.1f}" y="{py(60):.1f}" width="{s * 50:.1f}" height="{s * 30:.1f}" rx="6" stroke="{mur}" stroke-width="4"/>',
        # kabin camı: rect 215, 20, 42, 25 | 4,0 | murekkep
        f'<rect x="{px(215):.1f}" y="{py(20):.1f}" width="{s * 42:.1f}" height="{s * 25:.1f}" rx="6" stroke="{mur}" stroke-width="4"/>',
        # tekerlekler: circle merkez (40,138) (135,138) (240,138) (335,138), r 17 | 4,8 | murekkep
        f'<circle cx="{px(40):.1f}" cy="{py(138):.1f}" r="{s * 17:.1f}" stroke="{mur}" stroke-width="4.8"/>',
        f'<circle cx="{px(135):.1f}" cy="{py(138):.1f}" r="{s * 17:.1f}" stroke="{mur}" stroke-width="4.8"/>',
        f'<circle cx="{px(240):.1f}" cy="{py(138):.1f}" r="{s * 17:.1f}" stroke="{mur}" stroke-width="4.8"/>',
        f'<circle cx="{px(335):.1f}" cy="{py(138):.1f}" r="{s * 17:.1f}" stroke="{mur}" stroke-width="4.8"/>',
        # ray: line (−10,158) → (420,158) | 4,0 | ikincil
        f'<line x1="{px(-10):.1f}" y1="{py(158):.1f}" x2="{px(420):.1f}" y2="{py(158):.1f}" stroke="{ikn}" stroke-width="4"/>',
        # duman: ellipse merkez (345,2) rx 11 ry 9 · ellipse merkez (372,−16) rx 8 ry 7 | 4,0 | ikincil
        f'<ellipse cx="{px(345):.1f}" cy="{py(2):.1f}" rx="{s * 11:.1f}" ry="{s * 9:.1f}" stroke="{ikn}" stroke-width="4"/>',
        f'<ellipse cx="{px(372):.1f}" cy="{py(-16):.1f}" rx="{s * 8:.1f}" ry="{s * 7:.1f}" stroke="{ikn}" stroke-width="4"/>',
    ]
    return f'<g id="tren" fill="none" stroke-linecap="round" stroke-linejoin="round">{"".join(parcalar)}</g>'


def saat_svg() -> str:
    """Saat çizimi grubu SVG çıktısı (§4.2.2)."""
    mur = R["murekkep"]
    cx, cy, r = 772.0, 661.0, 96.0
    parcalar = [
        # kadran: circle (cx, cy), r | 4,8 | stroke murekkep, fill="none"
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{mur}" stroke-width="4.8"/>',
        # 4 çentik: 12, 3, 6, 9 yönünde, merkezden 0,66·r → 0,80·r | 4,0 | murekkep
        f'<line x1="{cx:.1f}" y1="{cy - 0.80 * r:.2f}" x2="{cx:.1f}" y2="{cy - 0.66 * r:.2f}" stroke="{mur}" stroke-width="4"/>',
        f'<line x1="{cx:.1f}" y1="{cy + 0.66 * r:.2f}" x2="{cx:.1f}" y2="{cy + 0.80 * r:.2f}" stroke="{mur}" stroke-width="4"/>',
        f'<line x1="{cx + 0.66 * r:.2f}" y1="{cy:.1f}" x2="{cx + 0.80 * r:.2f}" y2="{cy:.1f}" stroke="{mur}" stroke-width="4"/>',
        f'<line x1="{cx - 0.80 * r:.2f}" y1="{cy:.1f}" x2="{cx - 0.66 * r:.2f}" y2="{cy:.1f}" stroke="{mur}" stroke-width="4"/>',
        # yelkovan: (cx, cy) → (cx, cy − 0,66·r) | 5 | murekkep
        f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx:.1f}" y2="{cy - 0.66 * r:.2f}" stroke="{mur}" stroke-width="5"/>',
        # akrep: (cx, cy) → (cx + sin(210°)·0,5·r, cy − cos(210°)·0,5·r) | 7 | murekkep (sarı DEĞİL)
        f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx + math.sin(math.radians(210)) * 0.5 * r:.2f}" y2="{cy - math.cos(math.radians(210)) * 0.5 * r:.2f}" stroke="{mur}" stroke-width="7"/>',
        # göbek: circle (cx, cy), r 7 | — | fill murekkep
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="7" fill="{mur}"/>',
    ]
    return f'<g id="saat" stroke-linecap="round">{"".join(parcalar)}</g>'


def kart_svg() -> str:
    """Cümle kartı grubu SVG çıktısı (§4.2)."""
    mur = R["murekkep"]
    crv = (
        f'<rect id="kart-crv" x="48" y="512" width="984" height="502" rx="28" '
        f'fill="none" stroke="{mur}" stroke-width="4"/>'
    )
    tren = tren_svg()
    saat = saat_svg()
    s1 = (
        f'<text id="kart-s1" x="88" y="870" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{mur}" '
        f'xml:space="preserve">The train to İzmir</text>'
    )
    s2 = (
        f'<text id="kart-s2" x="88" y="958" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{mur}" '
        f'xml:space="preserve">leaves at 7 pm today.</text>'
    )
    return f'<g id="kart">{crv}{tren}{saat}{s1}{s2}</g>'


def secenek_karti_svg(grup_id: str, x0: int, cx: int, x_yazi: int, harf: str, yazi: str) -> str:
    """Seçenek kartı grubu SVG çıktısı (sA ya da sB) (§4.3)."""
    mur = R["murekkep"]
    crv = (
        f'<rect id="{grup_id}-crv" x="{x0}" y="1054" width="476" height="220" rx="28" '
        f'fill="none" stroke="{mur}" stroke-width="4"/>'
    )
    daire = (
        f'<circle id="{grup_id}-daire" cx="{cx}" cy="1164" r="52" '
        f'fill="none" stroke="{mur}" stroke-width="4"/>'
    )
    harf_yazi = (
        f'<text id="{grup_id}-harf" x="{cx}" y="1186" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{mur}" '
        f'xml:space="preserve">{harf}</text>'
    )
    yazi_elem = (
        f'<text id="{grup_id}-yazi" x="{x_yazi}" y="1190" '
        f'font-family="Fredoka" font-weight="700" font-size="72" fill="{mur}" '
        f'xml:space="preserve">{yazi}</text>'
    )
    return f'<g id="{grup_id}">{crv}{daire}{harf_yazi}{yazi_elem}</g>'


def blok_kutulari() -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    hud = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}

    # soru: Fredoka 700 96, taban 448
    w_soru = Y.genislik("Fredoka", 700, "Tarife mi, plan mı?", 96)
    soru = {
        "ad": "soru",
        "x": 48.0,
        "y": 448.0 - 0.75 * 96.0,
        "w": w_soru,
        "h": (0.75 + 0.25) * 96.0,
    }

    # kart: çerçeve
    kart = {"ad": "kart", "x": 48.0, "y": 512.0, "w": 984.0, "h": 502.0}

    # sA ve sB
    sA = {"ad": "sA", "x": 48.0, "y": 1054.0, "w": 476.0, "h": 220.0}
    sB = {"ad": "sB", "x": 556.0, "y": 1054.0, "w": 476.0, "h": 220.0}

    # cg1 ve cg2: Caveat 700 72
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

    # tren ve saat (kart içi kutuları, nesneler.json için)
    tren = {"ad": "tren", "x": 88.0, "y": 552.0, "w": 516.0, "h": 218.0}
    saat = {"ad": "saat", "x": 676.0, "y": 565.0, "w": 192.0, "h": 192.0}

    return [hud, soru, kart, sA, sB, cg1, cg2, hap, tren, saat]


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
        ("soru", 448.0, 96.0),
        ("kart-s1", 870.0, 64.0),
        ("kart-s2", 958.0, 64.0),
        ("sA-harf", 1186.0, 64.0),
        ("sA-yazi", 1190.0, 72.0),
        ("sB-harf", 1186.0, 64.0),
        ("sB-yazi", 1190.0, 72.0),
        ("cg1", 1418.0, 72.0),
        ("cg2", 1498.0, 72.0),
        ("hap", 1462.0, 64.0),
    ]
    for ad, taban, boy in yazilar:
        assert taban + 0.30 * boy <= 1536.0 + 1e-4, f"{ad} yazı alt sınırı > 1536"

    # 2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40)
    for ad, _, boy in yazilar:
        assert boy >= 64.0, f"{ad} yazı boyu {boy} < 64"

    # 3. Her ekran satırı ≤ 24 karakter (len), HUD ve çip dahil
    satirlar = [
        "SIMPLE PRESENT vs",
        "PRESENT CONTINUOUS",
        "YDT · BASIC",
        CIP_METIN,
        "Tarife mi, plan mı?",
        "The train to İzmir",
        "leaves at 7 pm today.",
        "A",
        "TARİFE",
        "B",
        "PLAN",
        "Cevap tam derste:",
        "profildeki bağlantı",
        "@ydspublishing",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 4. Blok kutuları çakışmaz (kesişim alanı 0)
    ana_bloklar = [b for b in bloklar if b["ad"] not in ("tren", "saat")]
    for i in range(len(ana_bloklar)):
        for j in range(i + 1, len(ana_bloklar)):
            k = kesisim(ana_bloklar[i], ana_bloklar[j])
            assert k == 0.0, f"Kesişim {ana_bloklar[i]['ad']} - {ana_bloklar[j]['ad']}: {k}"

    # Dikey komşular (hud → soru → kart → sA/sB → cg1/hap) arası boşluk ≥ 16
    assert b_dict["soru"]["y"] - (b_dict["hud"]["y"] + b_dict["hud"]["h"]) >= 16.0
    assert b_dict["kart"]["y"] - (b_dict["soru"]["y"] + b_dict["soru"]["h"]) >= 16.0
    assert b_dict["sA"]["y"] - (b_dict["kart"]["y"] + b_dict["kart"]["h"]) >= 16.0
    assert b_dict["sB"]["y"] - (b_dict["kart"]["y"] + b_dict["kart"]["h"]) >= 16.0
    assert b_dict["cg1"]["y"] - (b_dict["sA"]["y"] + b_dict["sA"]["h"]) >= 16.0
    assert b_dict["hap"]["y"] - (b_dict["sA"]["y"] + b_dict["sA"]["h"]) >= 16.0

    # sA–sB yatay boşluk ≥ 24
    assert b_dict["sB"]["x"] - (b_dict["sA"]["x"] + b_dict["sA"]["w"]) >= 24.0

    # cg1 ve cg2 dikey kesişimi 0
    assert kesisim(b_dict["cg1"], b_dict["cg2"]) == 0.0, "cg1 ve cg2 çakışıyor"

    # cg1 ve cg2 sağ kenarı ile hap sol kenarı arası ≥ 24
    assert b_dict["hap"]["x"] - (b_dict["cg1"]["x"] + b_dict["cg1"]["w"]) >= 24.0
    assert b_dict["hap"]["x"] - (b_dict["cg2"]["x"] + b_dict["cg2"]["w"]) >= 24.0

    # Kart içi: tren, saat, kart-s1, kart-s2 kutuları çerçevenin iç alanında (her kenardan ≥ 32);
    kart = b_dict["kart"]
    w_s1 = Y.genislik("Fredoka", 700, "The train to İzmir", 64)
    kart_s1 = {
        "ad": "kart-s1",
        "x": 88.0,
        "y": 870.0 - 0.75 * 64.0,
        "w": w_s1,
        "h": (0.75 + 0.25) * 64.0,
    }
    w_s2 = Y.genislik("Fredoka", 700, "leaves at 7 pm today.", 64)
    kart_s2 = {
        "ad": "kart-s2",
        "x": 88.0,
        "y": 958.0 - 0.75 * 64.0,
        "w": w_s2,
        "h": (0.75 + 0.25) * 64.0,
    }

    kart_iciler = [b_dict["tren"], b_dict["saat"], kart_s1, kart_s2]
    for b in kart_iciler:
        assert b["x"] >= kart["x"] + 32.0 - 1e-4, f"Kart içi {b['ad']} sol kenar payı < 32"
        assert b["x"] + b["w"] <= kart["x"] + kart["w"] - 32.0 + 1e-4, f"Kart içi {b['ad']} sağ kenar payı < 32"
        assert b["y"] >= kart["y"] + 32.0 - 1e-4, f"Kart içi {b['ad']} üst kenar payı < 32"
        assert b["y"] + b["h"] <= kart["y"] + kart["h"] - 32.0 + 1e-4, f"Kart içi {b['ad']} alt kenar payı < 32"

    # tren–saat yatay boşluk ≥ 24
    assert b_dict["saat"]["x"] - (b_dict["tren"]["x"] + b_dict["tren"]["w"]) >= 24.0

    # ikon satırı altı (max(tren, saat) alt) ile kart-s1 üstü arası ≥ 32
    max_ikon_alt = max(b_dict["tren"]["y"] + b_dict["tren"]["h"], b_dict["saat"]["y"] + b_dict["saat"]["h"])
    assert kart_s1["y"] - max_ikon_alt >= 32.0, f"İkon satırı altı ile kart-s1 üstü arası {kart_s1['y'] - max_ikon_alt} < 32"

    # kart-s1–kart-s2 kesişim 0
    assert kesisim(kart_s1, kart_s2) == 0.0, "kart-s1 ve kart-s2 çakışıyor"

    # Şık içi: harf dairesi sağı ile şık yazısı solu arası ≥ 24; şık yazısı sağı ≤ çerçeve sağı − 32
    assert 224.0 - (140.0 + 52.0) >= 24.0, "sA harf dairesi sağı ile yazı solu arası < 24"
    assert 732.0 - (648.0 + 52.0) >= 24.0, "sB harf dairesi sağı ile yazı solu arası < 24"

    w_tarife = Y.genislik("Fredoka", 700, "TARİFE", 72)
    assert 224.0 + w_tarife <= b_dict["sA"]["x"] + b_dict["sA"]["w"] - 32.0, "sA şık yazısı çerçeve sağı - 32'yi aşıyor"

    w_plan = Y.genislik("Fredoka", 700, "PLAN", 72)
    assert 732.0 + w_plan <= b_dict["sB"]["x"] + b_dict["sB"]["w"] - 32.0, "sB şık yazısı çerçeve sağı - 32'yi aşıyor"

    # 5. soru üstü ≥ 352; sA ve sB altı ≤ 1344; hap, cg1, cg2 [1344, 1536] içinde
    assert b_dict["soru"]["y"] >= 352.0, f"soru üstü {b_dict['soru']['y']} < 352"
    assert b_dict["sA"]["y"] + b_dict["sA"]["h"] <= 1344.0, f"sA altı {b_dict['sA']['y'] + b_dict['sA']['h']} > 1344"
    assert b_dict["sB"]["y"] + b_dict["sB"]["h"] <= 1344.0, f"sB altı {b_dict['sB']['y'] + b_dict['sB']['h']} > 1344"
    for ad in ("hap", "cg1", "cg2"):
        assert b_dict[ad]["y"] >= 1344.0, f"{ad} üstü {b_dict[ad]['y']} < 1344"
        assert b_dict[ad]["y"] + b_dict[ad]["h"] <= 1536.0, f"{ad} altı {b_dict[ad]['y'] + b_dict[ad]['h']} > 1536"

    # İçerik bandı doluluğu: (max(sA, sB) alt − soru üst) / 1040 ≥ 0,85
    icerik_doluluk = (max(b_dict["sA"]["y"] + b_dict["sA"]["h"], b_dict["sB"]["y"] + b_dict["sB"]["h"]) - b_dict["soru"]["y"]) / 1040.0
    assert icerik_doluluk >= 0.85, f"İçerik bandı doluluğu {icerik_doluluk:.3f} < 0.85"


def metinleri_dogrula(html: str) -> None:
    """SPEC.md §6 madde 7 ekran metni denetimi."""
    metinler = re.findall(r'<text[^>]*>(.*?)</text>', html)
    yasak_listesi = ["kanal", "QR", "dk", "Hangisi doğru?", "I go to", "movie theater", "Izmir"]
    for m in metinler:
        for yasak in yasak_listesi:
            assert yasak not in m, f"Yasak metin '{yasak}' bulundu: {m}"
    birlesik = " ".join(metinler)
    assert "İzmir" in birlesik, "İzmir metni bulunamadı"
    assert "7 pm" in birlesik, "7 pm metni bulunamadı"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()
    kurallari_dogrula(bloklar)

    kunye = Y.kunye_svg(CIP_METIN)
    soru = soru_svg()
    kart = kart_svg()
    sA = secenek_karti_svg("sA", 48, 140, 224, "A", "TARİFE")
    sB = secenek_karti_svg("sB", 556, 648, 732, "B", "PLAN")

    cg1 = (
        f'<text id="cg1" x="48" y="1418" font-family="Caveat" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" xml:space="preserve">Cevap tam derste:</text>'
    )
    cg2 = (
        f'<text id="cg2" x="48" y="1498" font-family="Caveat" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" xml:space="preserve">profildeki bağlantı</text>'
    )

    hap_w = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap_x = 1032.0 - hap_w
    hap = (
        f'<g id="hap">'
        f'<rect id="hap-kutu" x="{hap_x:.1f}" y="1398" width="{hap_w:.1f}" height="84" rx="42" fill="{R["vurgu"]}"/>'
        f'<text id="hap-yazi" x="{hap_x + hap_w / 2.0:.1f}" y="1462" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{R["zemin"]}" xml:space="preserve">@ydspublishing</text>'
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
{soru}
{kart}
{sA}
{sB}
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

    metinleri_dogrula(html)
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

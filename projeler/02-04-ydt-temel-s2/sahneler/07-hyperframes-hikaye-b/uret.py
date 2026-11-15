#!/usr/bin/python3
"""Sahne 07 hikâye karesi B (soru kartı) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: HUD (0-288) -> içerik (352-1392) -> çağrı (1344-1536) -> platform (1536-1920 boş)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# zaman.json ve zamanlar.json okuma ve doğrulama
zaman_data: dict[str, Any] = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlar = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlar) == 1, f"duragan listesinde {AD.name} olan tek kayıt olmalı, bulunan: {len(duragan_kayitlar)}"
kayit = duragan_kayitlar[0]
assert kayit["kare"] == 1, f"kare {kayit['kare']} != 1"
assert kayit["cikti"] == "hikaye-b.png", f"cikti {kayit['cikti']} != 'hikaye-b.png'"
assert AD.name not in [s["klasor"] for s in zaman_data.get("sahneler", [])], "AD.name sahneler içinde olmamalı"

Z: dict[str, Any] = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R: dict[str, str] = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}
assert R["zemin"] == "#1b1a17"
assert R["murekkep"] == "#f3efe6"
assert R["ikincil"] == "#c9c2b3"
assert R["vurgu"] == "#f2a93b"

# P/ortak/kunye.js içinden çip metnini çekme (Full lesson)
kunye_js: str = (PAKET / "ortak" / "kunye.js").read_text(encoding="utf-8")
_cip_match = re.search(r'"07-hyperframes-hikaye-b":\s*"([^"]+)"', kunye_js)
assert _cip_match is not None, "kunye.js içinde 07-hyperframes-hikaye-b çipi bulunamadı"
CIP: str = _cip_match.group(1)

W, H = Y.W, Y.H
KENAR = 48
SAG = 1032
ICERIK = (352, 1392)
CAGRI = (1344, 1536)
PLATFORM = 1536
IC = 40
ARA = 40
KOK_H = 276
SIK_H = 160


def tisort_svg() -> str:
    """Küçük tişört grubu SVG çıktısı (#kok-tis)."""
    def tx(gx: float) -> float:
        return 876.0 + gx * 1.2

    def ty(gy: float) -> float:
        return 540.0 + (gy - 4.0) * 1.2

    dis_noktalar: list[tuple[float, float]] = [
        (37.0, 4.0), (14.0, 12.0), (0.0, 36.0), (14.0, 46.0),
        (24.0, 37.0), (24.0, 88.0), (76.0, 88.0), (76.0, 37.0),
        (86.0, 46.0), (100.0, 36.0), (86.0, 12.0), (63.0, 4.0),
    ]
    dis_d = "M " + " L ".join(f"{tx(gx):.1f} {ty(gy):.1f}" for gx, gy in dis_noktalar)
    p0 = (
        f'<path id="kok-tis-0" d="{dis_d}" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    p1 = (
        f'<path id="kok-tis-1" d="M {tx(37.0):.1f} {ty(4.0):.1f} Q {tx(50.0):.1f} {ty(24.0):.1f} {tx(63.0):.1f} {ty(4.0):.1f}" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    p2 = (
        f'<path id="kok-tis-2" d="M {tx(14.0):.1f} {ty(12.0):.1f} L {tx(24.0):.1f} {ty(37.0):.1f}" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    p3 = (
        f'<path id="kok-tis-3" d="M {tx(86.0):.1f} {ty(12.0):.1f} L {tx(76.0):.1f} {ty(37.0):.1f}" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    return f'<g id="kok-tis">{p0}{p1}{p2}{p3}</g>'


def kok_karti_svg() -> str:
    """Kök kartı grubu SVG çıktısı (#kok)."""
    crv = (
        f'<rect id="kok-crv" x="48" y="512" width="984" height="{KOK_H}" rx="28" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    s1a = (
        f'<text id="kok-s1a" x="88" y="620" '
        f'font-family="Fredoka" font-weight="700" font-size="72" fill="{R["murekkep"]}" '
        f'xml:space="preserve">Look! She</text>'
    )
    bx0 = 88.0 + Y.genislik("Fredoka", 700, "Look! She ", 72)
    bx1 = bx0 + 240.0
    x0 = bx0 + 4.0
    x1 = bx1 - 4.0
    yb = 620.0 + 14.0
    xc = (x0 + x1) / 2.0
    yc = yb + 6.0
    y1 = yb + 1.0
    bos = (
        f'<path id="kok-bos" d="M {x0:.1f} {yb:.1f} Q {xc:.1f} {yc:.1f} {x1:.1f} {y1:.1f}" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="5" stroke-linecap="round"/>'
    )
    x1b = bx1 + Y.genislik("Fredoka", 700, " ", 72)
    s1b = (
        f'<text id="kok-s1b" x="{x1b:.1f}" y="620" '
        f'font-family="Fredoka" font-weight="700" font-size="72" fill="{R["murekkep"]}" '
        f'xml:space="preserve">her</text>'
    )
    s2 = (
        f'<text id="kok-s2" x="88" y="716" '
        f'font-family="Fredoka" font-weight="700" font-size="72" fill="{R["murekkep"]}" '
        f'xml:space="preserve">pink T-shirt today.</text>'
    )
    tis = tisort_svg()
    return f'<g id="kok">{crv}{s1a}{bos}{s1b}{s2}{tis}</g>'


def secenek_karti_svg(grup_id: str, y0: int, harf: str, metin: str) -> str:
    """Şık kartı grubu SVG çıktısı (kA ya da kB)."""
    cy = y0 + 80
    crv = (
        f'<rect id="{grup_id}-crv" x="48" y="{y0}" width="984" height="{SIK_H}" rx="28" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    daire = (
        f'<circle id="{grup_id}-daire" cx="136" cy="{cy}" r="48" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    harf_yazi = (
        f'<text id="{grup_id}-harf" x="136" y="{cy + 22}" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{R["murekkep"]}" '
        f'xml:space="preserve">{harf}</text>'
    )
    metin_yazi = (
        f'<text id="{grup_id}-metin" x="220" y="{cy + 26}" '
        f'font-family="Fredoka" font-weight="700" font-size="72" fill="{R["murekkep"]}" '
        f'xml:space="preserve">{metin}</text>'
    )
    return f'<g id="{grup_id}">{crv}{daire}{harf_yazi}{metin_yazi}</g>'


def baslik_svg() -> str:
    """Soru başlığı SVG çıktısı (#baslik)."""
    return (
        f'<text id="baslik" x="48" y="448" '
        f'font-family="Fredoka" font-weight="700" font-size="96" fill="{R["murekkep"]}" '
        f'xml:space="preserve">Hangisi doğru?</text>'
    )


def ipucu_svg() -> str:
    """İpucu satırı SVG çıktısı (#ipucu)."""
    return (
        f'<text id="ipucu" x="48" y="1276" '
        f'font-family="Caveat" font-weight="700" font-size="64" fill="{R["murekkep"]}" '
        f'xml:space="preserve">Genel mi, şu an mı?</text>'
    )


def cagri_svg() -> tuple[str, str]:
    """Çağrı metinleri SVG çıktısı (#cg1 ve #cg2)."""
    cg1 = (
        f'<text id="cg1" x="48" y="1418" '
        f'font-family="Caveat" font-weight="700" font-size="72" fill="{R["murekkep"]}" '
        f'xml:space="preserve">Cevap ve neden:</text>'
    )
    cg2 = (
        f'<text id="cg2" x="48" y="1498" '
        f'font-family="Caveat" font-weight="700" font-size="72" fill="{R["murekkep"]}" '
        f'xml:space="preserve">tam derste</text>'
    )
    return cg1, cg2


def hap_svg() -> str:
    """@ydspublishing hapı grubu SVG çıktısı (#hap)."""
    hap_w = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap_x = 1032.0 - hap_w
    kutu = (
        f'<rect id="hap-kutu" x="{hap_x:.1f}" y="1398" width="{hap_w:.1f}" height="84" rx="42" '
        f'fill="{R["vurgu"]}"/>'
    )
    yazi = (
        f'<text id="hap-yazi" x="{hap_x + hap_w / 2.0:.1f}" y="1462" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{R["zemin"]}" '
        f'xml:space="preserve">@ydspublishing</text>'
    )
    return f'<g id="hap">{kutu}{yazi}</g>'


def blok_kutulari() -> list[dict[str, Any]]:
    """Yerleşim bloklarının kutularını hesaplar (bloklar §7.4 + tisort §7.10)."""
    hud = {"ad": "hud", "x": 48.0, "y": 0.0, "w": 984.0, "h": 288.0}

    w_baslik = Y.genislik("Fredoka", 700, "Hangisi doğru?", 96)
    baslik = {
        "ad": "baslik",
        "x": 48.0,
        "y": 448.0 - 0.75 * 96.0,
        "w": w_baslik,
        "h": (0.75 + 0.25) * 96.0,
    }

    kok = {"ad": "kok", "x": 48.0, "y": 512.0, "w": 984.0, "h": float(KOK_H)}
    kA = {"ad": "kA", "x": 48.0, "y": 828.0, "w": 984.0, "h": float(SIK_H)}
    kB = {"ad": "kB", "x": 48.0, "y": 1028.0, "w": 984.0, "h": float(SIK_H)}

    w_ipucu = Y.genislik("Caveat", 700, "Genel mi, şu an mı?", 64)
    ipucu = {
        "ad": "ipucu",
        "x": 48.0,
        "y": 1276.0 - 0.75 * 64.0,
        "w": w_ipucu,
        "h": (0.75 + 0.30) * 64.0,
    }

    w_cg1 = Y.genislik("Caveat", 700, "Cevap ve neden:", 72)
    cg1 = {
        "ad": "cg1",
        "x": 48.0,
        "y": 1418.0 - 0.75 * 72.0,
        "w": w_cg1,
        "h": (0.75 + 0.30) * 72.0,
    }

    w_cg2 = Y.genislik("Caveat", 700, "tam derste", 72)
    cg2 = {
        "ad": "cg2",
        "x": 48.0,
        "y": 1498.0 - 0.75 * 72.0,
        "w": w_cg2,
        "h": (0.75 + 0.30) * 72.0,
    }

    w_hap = Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56.0
    hap = {
        "ad": "hap",
        "x": 1032.0 - w_hap,
        "y": 1398.0,
        "w": w_hap,
        "h": 84.0,
    }

    # Tişört sınırlayıcı kutusu (§4.4: 876-996, 540-641)
    tisort = {
        "ad": "tisort",
        "x": 876.0,
        "y": 540.0,
        "w": 120.0,
        "h": 101.0,
    }

    return [hud, baslik, kok, kA, kB, ipucu, cg1, cg2, hap, tisort]


def kesisim(b1: dict[str, Any], b2: dict[str, Any]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(float(b1["x"]) + float(b1["w"]), float(b2["x"]) + float(b2["w"])) - max(float(b1["x"]), float(b2["x"])))
    dy = max(0.0, min(float(b1["y"]) + float(b1["h"]), float(b2["y"]) + float(b2["h"])) - max(float(b1["y"]), float(b2["y"])))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, Any]], svgler: dict[str, str], html: str) -> None:
    """SPEC.md §7 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Bütün metin ve kutular x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil
    for b in bloklar:
        assert float(b["x"]) >= 48.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 48"
        assert float(b["x"]) + float(b["w"]) <= 1032.0 + 1e-4, f"{b['ad']} sağ kenar {float(b['x']) + float(b['w'])} > 1032"
        assert float(b["y"]) >= 0.0, f"{b['ad']} üst {b['y']} < 0"
        assert float(b["y"]) + float(b["h"]) <= 1536.0 + 1e-4, f"{b['ad']} alt {float(b['y']) + float(b['h'])} > 1536"

    # Yazı alt sınırları kontrolü (taban + 0.30*boy Caveat / 0.25*boy diğer <= 1536)
    yazilar: list[tuple[str, float, float, str]] = [
        ("baslik", 448.0, 96.0, "Fredoka"),
        ("kok-s1a", 620.0, 72.0, "Fredoka"),
        ("kok-s1b", 620.0, 72.0, "Fredoka"),
        ("kok-s2", 716.0, 72.0, "Fredoka"),
        ("kA-harf", 930.0, 64.0, "Fredoka"),
        ("kA-metin", 934.0, 72.0, "Fredoka"),
        ("kB-harf", 1130.0, 64.0, "Fredoka"),
        ("kB-metin", 1134.0, 72.0, "Fredoka"),
        ("ipucu", 1276.0, 64.0, "Caveat"),
        ("cg1", 1418.0, 72.0, "Caveat"),
        ("cg2", 1498.0, 72.0, "Caveat"),
        ("hap-yazi", 1462.0, 64.0, "Fredoka"),
    ]
    for ad, taban, boy, aile in yazilar:
        carpan = 0.30 if aile == "Caveat" else 0.25
        alt = taban + carpan * boy
        assert alt <= 1536.0 + 1e-4, f"{ad} yazı alt sınırı {alt} > 1536"

    # 2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40)
    for ad, _, boy, _ in yazilar:
        assert boy >= 64.0, f"{ad} yazı boyu {boy} < 64"

    # 3. Her ekran satırı ≤ 24 karakter (len), HUD ve çip dahil
    satirlar = [
        "SIMPLE PRESENT vs",
        "PRESENT CONTINUOUS",
        "YDT · BASIC",
        CIP,
        "Hangisi doğru?",
        "Look! She ____ her",
        "pink T-shirt today.",
        "A",
        "B",
        "wears",
        "is wearing",
        "Genel mi, şu an mı?",
        "Cevap ve neden:",
        "tam derste",
        "@ydspublishing",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 4. Blok kutuları çakışmaz (kesişim alanı 0). §7.4 sırası: 9 blok (tisort hariç)
    ana_bloklar = [b for b in bloklar if b["ad"] != "tisort"]
    assert len(ana_bloklar) == 9, f"Ana blok sayısı 9 olmalı: {len(ana_bloklar)}"
    for i in range(len(ana_bloklar)):
        for j in range(i + 1, len(ana_bloklar)):
            k = kesisim(ana_bloklar[i], ana_bloklar[j])
            assert k == 0.0, f"Kesişim {ana_bloklar[i]['ad']} - {ana_bloklar[j]['ad']}: {k}"

    # Dikey komşular (hud→baslik→kok→kA→kB→ipucu→cg1, ipucu→hap) arası boşluk ≥ 16
    dikey_sirali = ["hud", "baslik", "kok", "kA", "kB", "ipucu", "cg1"]
    for i in range(len(dikey_sirali) - 1):
        b1 = b_dict[dikey_sirali[i]]
        b2 = b_dict[dikey_sirali[i + 1]]
        bosluk = float(b2["y"]) - (float(b1["y"]) + float(b1["h"]))
        assert bosluk >= 16.0 - 1e-4, f"Dikey boşluk {b1['ad']} -> {b2['ad']}: {bosluk} < 16"

    bosluk_ipucu_hap = float(b_dict["hap"]["y"]) - (float(b_dict["ipucu"]["y"]) + float(b_dict["ipucu"]["h"]))
    assert bosluk_ipucu_hap >= 16.0 - 1e-4, f"Dikey boşluk ipucu -> hap: {bosluk_ipucu_hap} < 16"

    # cg1 ve cg2 dikey kesişimi 0
    assert kesisim(b_dict["cg1"], b_dict["cg2"]) == 0.0, "cg1 ve cg2 çakışıyor"

    # cg1, cg2 sağ kenarı ile hap sol kenarı arası ≥ 24
    assert float(b_dict["hap"]["x"]) - (float(b_dict["cg1"]["x"]) + float(b_dict["cg1"]["w"])) >= 24.0 - 1e-4, "cg1 ile hap arası < 24"
    assert float(b_dict["hap"]["x"]) - (float(b_dict["cg2"]["x"]) + float(b_dict["cg2"]["w"])) >= 24.0 - 1e-4, "cg2 ile hap arası < 24"

    # 5. Kök kartı içi kuralları
    bx0 = 88.0 + Y.genislik("Fredoka", 700, "Look! She ", 72)
    bx1 = bx0 + 240.0
    x1b = bx1 + Y.genislik("Fredoka", 700, " ", 72)
    w_her = Y.genislik("Fredoka", 700, "her", 72)
    s1b_sag = x1b + w_her
    assert s1b_sag + 24.0 <= 876.0 + 1e-4, f"kok-s1b sağı + 24 ({s1b_sag + 24.0}) > 876"

    kok_s2_ust = 716.0 - 0.75 * 72.0
    tisort_alt = 540.0 + (88.0 - 4.0) * 1.2
    assert tisort_alt + 16.0 <= kok_s2_ust + 1e-4, f"tişört altı + 16 ({tisort_alt + 16.0}) > kok-s2 üstü ({kok_s2_ust})"

    # tişört kutusu kart içinde, kenarlara ≥ 16
    assert 876.0 >= 48.0 + 16.0 - 1e-4, "tişört sol boşluk < 16"
    assert 996.0 <= 1032.0 - 16.0 + 1e-4, "tişört sağ boşluk < 16"
    assert 540.0 >= 512.0 + 16.0 - 1e-4, "tişört üst boşluk < 16"
    assert tisort_alt <= 788.0 - 16.0 + 1e-4, "tişört alt boşluk < 16"

    # Bütün kök yazıları x ∈ [88, 1032 − IC] ve y ∈ [512 + 16, 788 − 16]
    kok_yazilar = [
        ("kok-s1a", 88.0, Y.genislik("Fredoka", 700, "Look! She", 72), 620.0, 72.0),
        ("kok-s1b", x1b, w_her, 620.0, 72.0),
        ("kok-s2", 88.0, Y.genislik("Fredoka", 700, "pink T-shirt today.", 72), 716.0, 72.0),
    ]
    for ad, x, w, taban, boy in kok_yazilar:
        assert x >= 88.0 - 1e-4, f"{ad} x ({x}) < 88"
        assert x + w <= 1032.0 - IC + 1e-4, f"{ad} sağ ({x + w}) > {1032 - IC}"
        y_ust = taban - 0.75 * boy
        y_alt = taban + 0.25 * boy
        assert y_ust >= 512.0 + 16.0 - 1e-4, f"{ad} üst ({y_ust}) < {512 + 16}"
        assert y_alt <= 788.0 - 16.0 + 1e-4, f"{ad} alt ({y_alt}) > {788 - 16}"

    # 6. Şık kartı içi: daire sağı (184) + 24 ≤ metin solu (220); metin sağı ≤ 1032 − IC; harf ve metin y kutusu kart içinde
    assert 184.0 + 24.0 <= 220.0 + 1e-4, "daire sağı + 24 > 220"
    for gid, y0, metin in [("kA", 828.0, "wears"), ("kB", 1028.0, "is wearing")]:
        w = Y.genislik("Fredoka", 700, metin, 72)
        assert 220.0 + w <= 1032.0 - IC + 1e-4, f"{gid} metin sağı {220.0 + w} > {1032 - IC}"
        cy = y0 + 80.0
        h_taban = cy + 22.0
        h_ust = h_taban - 0.75 * 64.0
        h_alt = h_taban + 0.25 * 64.0
        assert h_ust >= y0 - 1e-4, f"{gid} harf üst {h_ust} < {y0}"
        assert h_alt <= y0 + SIK_H + 1e-4, f"{gid} harf alt {h_alt} > {y0 + SIK_H}"
        m_taban = cy + 26.0
        m_ust = m_taban - 0.75 * 72.0
        m_alt = m_taban + 0.25 * 72.0
        assert m_ust >= y0 - 1e-4, f"{gid} metin üst {m_ust} < {y0}"
        assert m_alt <= y0 + SIK_H + 1e-4, f"{gid} metin alt {m_alt} > {y0 + SIK_H}"

    # 7. baslik üstü ≥ 352; ipucu altı ≤ 1344 − 16; hap, cg1, cg2 [1344, 1536] içinde; bant doluluğu ≥ 0.85
    assert float(b_dict["baslik"]["y"]) >= 352.0 - 1e-4, f"baslik üstü {b_dict['baslik']['y']} < 352"
    ipucu_alt = float(b_dict["ipucu"]["y"]) + float(b_dict["ipucu"]["h"])
    assert ipucu_alt <= 1344.0 - 16.0 + 1e-4, f"ipucu altı {ipucu_alt} > 1328"
    for ad in ("hap", "cg1", "cg2"):
        assert float(b_dict[ad]["y"]) >= 1344.0 - 1e-4, f"{ad} üstü {b_dict[ad]['y']} < 1344"
        assert float(b_dict[ad]["y"]) + float(b_dict[ad]["h"]) <= 1536.0 + 1e-4, f"{ad} altı {float(b_dict[ad]['y']) + float(b_dict[ad]['h'])} > 1536"

    doluluk = (ipucu_alt - float(b_dict["baslik"]["y"])) / (1392.0 - 352.0)
    assert doluluk >= 0.85, f"Bant doluluğu {doluluk:.4f} < 0.85"

    # 8. Cevap yok doğrulaması
    icerik_svg = (
        svgler["baslik"] + svgler["kok"] + svgler["kA"] +
        svgler["kB"] + svgler["ipucu"] + svgler["cg1"] + svgler["cg2"]
    )
    assert R["vurgu"] not in icerik_svg, f"İçerik SVG'sinde vurgu rengi bulundu: {R['vurgu']}"

    def _norm_sik(s: str, gid: str, y0: int, h: str, m: str) -> str:
        r = s.replace(gid, "kX")
        r = r.replace(str(y0), "Y0")
        r = r.replace(str(y0 + 80), "CY")
        r = r.replace(str(y0 + 80 + 22), "YH")
        r = r.replace(str(y0 + 80 + 26), "YM")
        r = r.replace(f">{h}<", ">H<")
        r = r.replace(f">{m}<", ">M<")
        return r

    kA_n = _norm_sik(svgler["kA"], "kA", 828, "A", "wears")
    kB_n = _norm_sik(svgler["kB"], "kB", 1028, "B", "is wearing")
    assert kA_n == kB_n, f"kA ve kB normalize edilince eşit değil:\nkA: {kA_n}\nkB: {kB_n}"

    assert "is wearing" not in svgler["kok"], "Kök içinde 'is wearing' bulundu"
    assert "wears" not in svgler["kok"], "Kök içinde 'wears' bulundu"

    # 9. Yasak kontrolleri
    for yasak_kelime in ("kanal", "QR", "dk"):
        assert yasak_kelime not in html, f"HTML içinde yasak metin bulundu: {yasak_kelime}"
    assert "#e0473b" not in icerik_svg, "Kırmızı renk bulundu"
    assert "opacity:0" not in html, "opacity:0 başlangıç bulundu"


def uret() -> tuple[str, list[dict[str, Any]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()
    kunye = Y.kunye_svg(CIP)
    baslik = baslik_svg()
    kok = kok_karti_svg()
    kA = secenek_karti_svg("kA", 828, "A", "wears")
    kB = secenek_karti_svg("kB", 1028, "B", "is wearing")
    ipucu = ipucu_svg()
    cg1, cg2 = cagri_svg()
    hap = hap_svg()

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
{kok}
{kA}
{kB}
{ipucu}
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
</script></body></html>
"""

    svgler = {
        "baslik": baslik,
        "kok": kok,
        "kA": kA,
        "kB": kB,
        "ipucu": ipucu,
        "cg1": cg1,
        "cg2": cg2,
        "hap": hap,
    }
    kurallari_dogrula(bloklar, svgler, html)
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
            "x": int(round(float(b["x"]))),
            "y": int(round(float(b["y"]))),
            "w": int(round(float(b["w"]))),
            "h": int(round(float(b["h"]))),
        }
        for b in bloklar
    ]
    (AD / "nesneler.json").write_text(json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"index.html yazıldı {len(html)}")

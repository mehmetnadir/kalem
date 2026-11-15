#!/usr/bin/python3
"""Sahne 07 hikâye karesi B (soru kartı) index.html üretici (02-04-ydt-temel-s2 huni v2; DİKEY 1080×1920, tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Yerleşim: kanal katmanı + künye (280–450) -> başlık (536) -> kök kartı (570–736) -> şık A (748–840) -> şık B (852–944) -> kural (956–1023) -> Kaydet (1036–1138); 1150–1920 boş.
DUZ2 (15.11, J2 A6): ipucu satırı ("Genel mi, şu an mı?") yerine kural özeti; terimler sesle aynı (cümle 1 "Genel mi, şu an mı?", cümle 2 "Genel durum: …")."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
for _p in ("/usr/local/lib/python3.10/dist-packages", str(Path.home() / ".local/lib/python3.10/site-packages")):
    if _p not in sys.path:
        sys.path.append(_p)
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

assert Y.KONU == "Simple Present vs Present Continuous"
assert Y.ROZETLER == ("YDT · TEMEL",)

R: dict[str, str] = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "vurgu"}
assert R["zemin"] == "#1b1a17"
assert R["murekkep"] == "#f3efe6"
assert R["vurgu"] == "#f2a93b"

# Tabler Icons `bookmark` (MIT License) - 24x24 viewBox, bounding box x: 6-18, y: 3-21
YERIMI_D = "M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"

# Sabitler (SPEC §3)
X0, X1 = 60, 960
BASLIK_BOY, BASLIK_TABAN = 88, 536
KOK_BOY, L1, L2 = 64, 634, 704
TX = 92
BOS_W = 200
TIS_X, TIS_Y, TIS_S = 844, 615, 0.9
SIK_Y = (750, 854)
DAIRE_X, DAIRE_R, SIK_TX, SIK_BOY = 122, 36, 184, 64  # r 34 → 36 (şef QA tur 1)
HARF_KAYMA = 19  # harf tabanı cy + 19 (şef QA tur 1: cy + 22'de "A" ayakları daire çizgisine değdi)
BOS_KAYMA = 6  # boşluk çizgisi L1 + 6 (şef QA tur 1: L1 + 12'de alt satır "today" harflerine 8 px kaldı)
KURAL_BOY, KURAL_TABAN = 64, 1004
KURAL_METIN = "Genel: wears · Şu an: is wearing"  # huni §6 hikâye kural özeti (A6); → glifi yazı tiplerinde yok
YERIMI_S, YERIMI_X, YERIMI_UST = 5, 63, 1039
KAYDET_BOY, KAYDET_TABAN = 88, 1116
BOS_UST = 1150


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def blok_kutulari() -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar (SPEC §6 sırası)."""
    w_ad = Y.genislik("Lexend", 700, "@ydspublishing", 42)
    kanal = {
        "ad": "kanal",
        "x": 53.15,
        "y": 291.0,
        "w": 263.0 + w_ad - 53.15,
        "h": 50.0,
    }

    rozet_konum = Y.rozet_konumlari()[0]
    rozet_sag = rozet_konum[0] + rozet_konum[1]
    kunye = {
        "ad": "kunye",
        "x": 60.0,
        "y": 386.0,
        "w": rozet_sag - 60.0,
        "h": 48.0,
    }

    w_baslik = Y.genislik("Fredoka", 700, "Hangisi doğru?", BASLIK_BOY)
    baslik = {
        "ad": "baslik",
        "x": float(X0),
        "y": float(BASLIK_TABAN) - 66.0,
        "w": w_baslik,
        "h": 88.0,
    }

    kok = {
        "ad": "kok",
        "x": 60.0,
        "y": 570.0,
        "w": 900.0,
        "h": 166.0,
    }

    kA = {
        "ad": "kA",
        "x": 60.0,
        "y": 748.0,
        "w": 900.0,
        "h": 92.0,
    }

    kB = {
        "ad": "kB",
        "x": 60.0,
        "y": 852.0,
        "w": 900.0,
        "h": 92.0,
    }

    w_kural = Y.genislik("Caveat", 700, KURAL_METIN, KURAL_BOY)
    kural = {
        "ad": "kural",
        "x": float(X0),
        "y": float(KURAL_TABAN) - 48.0,
        "w": w_kural,
        "h": 1.05 * 64.0,
    }

    w_kaydet = Y.genislik("Fredoka", 700, "Kaydet", KAYDET_BOY)
    kx = float((YERIMI_X + 12 * YERIMI_S + 3) + 22)
    kaydet = {
        "ad": "kaydet",
        "x": 60.0,
        "y": 1036.0,
        "w": (kx + w_kaydet) - 60.0,
        "h": (float(KAYDET_TABAN) + 22.0) - 1036.0,
    }

    tisort = {
        "ad": "tisort",
        "x": 844.0,
        "y": 615.0,
        "w": 90.0,
        "h": 75.6,
    }

    return [kanal, kunye, baslik, kok, kA, kB, kural, kaydet, tisort]


def defs_svg() -> str:
    """SVG defs çıktısı (yer imi kırpma yolu, §4.3.5)."""
    tx = YERIMI_X - 6 * YERIMI_S
    ty = YERIMI_UST - 3 * YERIMI_S
    return (
        f'<defs>\n'
        f'<clipPath id="yerimi-kirp">'
        f'<path d="{YERIMI_D}" transform="translate({tx} {ty}) scale({YERIMI_S})"/>'
        f'</clipPath>\n'
        f'</defs>'
    )


def baslik_svg() -> str:
    """Soru başlığı SVG çıktısı (#baslik, §4.3)."""
    return (
        f'<text id="baslik" x="{X0}" y="{BASLIK_TABAN}" '
        f'font-family="Fredoka" font-weight="700" font-size="{BASLIK_BOY}" '
        f'fill="{R["murekkep"]}" xml:space="preserve">Hangisi doğru?</text>'
    )


def tisort_svg() -> str:
    """Küçük tişört grubu SVG çıktısı (#kok-tis, §4.4)."""
    def tx(gx: float) -> float:
        return float(TIS_X) + gx * TIS_S

    def ty(gy: float) -> float:
        return float(TIS_Y) + (gy - 4.0) * TIS_S

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
    """Kök kartı grubu SVG çıktısı (#kok, §4.3.2)."""
    crv = (
        f'<rect id="kok-crv" x="62" y="572" width="896" height="162" rx="28" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    s1a = (
        f'<text id="kok-s1a" x="{TX}" y="{L1}" '
        f'font-family="Fredoka" font-weight="700" font-size="{KOK_BOY}" fill="{R["murekkep"]}" '
        f'xml:space="preserve">Look! She</text>'
    )
    bx0 = float(TX) + Y.genislik("Fredoka", 700, "Look! She ", KOK_BOY)
    bx1 = bx0 + float(BOS_W)
    x0 = bx0 + 4.0
    x1 = bx1 - 4.0
    yb = float(L1) + float(BOS_KAYMA)
    xc = (x0 + x1) / 2.0
    yc = yb + 5.0
    y1 = yb + 1.0
    bos = (
        f'<path id="kok-bos" d="M {x0:.1f} {yb:.1f} Q {xc:.1f} {yc:.1f} {x1:.1f} {y1:.1f}" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="5" stroke-linecap="round"/>'
    )
    x1b = bx1 + Y.genislik("Fredoka", 700, " ", KOK_BOY)
    s1b = (
        f'<text id="kok-s1b" x="{x1b:.1f}" y="{L1}" '
        f'font-family="Fredoka" font-weight="700" font-size="{KOK_BOY}" fill="{R["murekkep"]}" '
        f'xml:space="preserve">her</text>'
    )
    s2 = (
        f'<text id="kok-s2" x="{TX}" y="{L2}" '
        f'font-family="Fredoka" font-weight="700" font-size="{KOK_BOY}" fill="{R["murekkep"]}" '
        f'xml:space="preserve">pink T-shirt today.</text>'
    )
    tis = tisort_svg()
    return f'<g id="kok">{crv}{s1a}{bos}{s1b}{s2}{tis}</g>'


def secenek_karti_svg(grup_id: str, y0: int, harf: str, metin: str) -> str:
    """Şık kartı grubu SVG çıktısı (kA ya da kB, §4.3.3)."""
    cy = y0 + 44
    crv = (
        f'<rect id="{grup_id}-crv" x="62" y="{y0}" width="896" height="88" rx="28" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    daire = (
        f'<circle id="{grup_id}-daire" cx="{DAIRE_X}" cy="{cy}" r="{DAIRE_R}" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    harf_yazi = (
        f'<text id="{grup_id}-harf" x="{DAIRE_X}" y="{cy + HARF_KAYMA}" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="{SIK_BOY}" fill="{R["murekkep"]}" '
        f'xml:space="preserve">{harf}</text>'
    )
    metin_yazi = (
        f'<text id="{grup_id}-metin" x="{SIK_TX}" y="{cy + 22}" '
        f'font-family="Fredoka" font-weight="700" font-size="{SIK_BOY}" fill="{R["murekkep"]}" '
        f'xml:space="preserve">{metin}</text>'
    )
    return f'<g id="{grup_id}">{crv}{daire}{harf_yazi}{metin_yazi}</g>'


def kural_svg() -> str:
    """Kural özeti satırı SVG çıktısı (#kural; DUZ2 A6, eski #ipucu yerinde)."""
    return (
        f'<text id="kural" x="{X0}" y="{KURAL_TABAN}" '
        f'font-family="Caveat" font-weight="700" font-size="{KURAL_BOY}" '
        f'fill="{R["murekkep"]}" xml:space="preserve">{KURAL_METIN}</text>'
    )


def kaydet_svg() -> str:
    """Kaydet grubu SVG çıktısı (#kaydet, §4.3.5)."""
    tx = YERIMI_X - 6 * YERIMI_S
    ty = YERIMI_UST - 3 * YERIMI_S
    sw = 6.0 / YERIMI_S
    kx = (YERIMI_X + 12 * YERIMI_S + 3) + 22
    dolgu = (
        f'<rect id="yerimi-dolgu" x="{YERIMI_X}" y="{YERIMI_UST}" width="{12 * YERIMI_S}" height="{18 * YERIMI_S}" '
        f'fill="{R["vurgu"]}" clip-path="url(#yerimi-kirp)"/>'
    )
    yerimi = (
        f'<path id="yerimi" d="{YERIMI_D}" transform="translate({tx} {ty}) scale({YERIMI_S})" '
        f'fill="none" stroke="{R["murekkep"]}" stroke-width="{sw:.1f}" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )
    kaydet_yazi = (
        f'<text id="kaydet-yazi" x="{kx}" y="{KAYDET_TABAN}" '
        f'font-family="Fredoka" font-weight="700" font-size="{KAYDET_BOY}" '
        f'fill="{R["murekkep"]}" xml:space="preserve">Kaydet</text>'
    )
    return f'<g id="kaydet">{dolgu}{yerimi}{kaydet_yazi}</g>'


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. Bütün blok x ∈ [53, 960]; kanal dışındakiler x ≥ 60. Hiçbir blok y < 280; içerik blokları y ≥ 460 ve alt ≤ BOS_UST (1150)
    for b in bloklar:
        assert b["x"] >= 53.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 53"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{b['ad']} sağ kenar {b['x'] + b['w']} > 960"
        if b["ad"] != "kanal":
            assert b["x"] >= 60.0 - 1e-4, f"{b['ad']} sol kenar {b['x']} < 60"
        assert b["y"] >= 280.0 - 1e-4, f"{b['ad']} üst {b['y']} < 280"

    for ad in ("baslik", "kok", "kA", "kB", "kural", "kaydet"):
        b = b_dict[ad]
        assert b["y"] >= 460.0 - 1e-4, f"{ad} üst {b['y']} < 460"
        assert b["y"] + b["h"] <= float(BOS_UST) + 1e-4, f"{ad} alt {b['y'] + b['h']} > {BOS_UST}"

    # 2. İçerik yazı boyu ≥ 64 (başlık 88, kök 64, harf 64, şık 64, kural 64, Kaydet 88). Künye/kanal hariç
    for boy in (BASLIK_BOY, KOK_BOY, SIK_BOY, KURAL_BOY, KAYDET_BOY):
        assert boy >= 64, f"İçerik yazı boyu {boy} < 64"

    # 3. İçerik satırı ≤ 24 karakter (len)
    satirlar = [
        "Hangisi doğru?",
        "Look! She ____ her",
        "pink T-shirt today.",
        "A",
        "wears",
        "B",
        "is wearing",
        "Kaydet",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"
    # Kural satırı 32 karakter: ≤ 24 sınırı ders kalıbıdır (DK-2); kısa türevde ölçü genişliktir (x 60–960 içinde)
    assert X0 + Y.genislik("Caveat", 700, KURAL_METIN, KURAL_BOY) <= X1 + 1e-4, "kural satırı 960'ı aşıyor"

    # 4. Ana blok çiftleri (tisort hariç 8 blok) kesişmez (alan 0). Dikey sıra kanal → kunye → baslik → kok → kA → kB → kural → kaydet komşu boşluğu ≥ 12
    ana_bloklar = [b for b in bloklar if b["ad"] != "tisort"]
    assert len(ana_bloklar) == 8, f"Ana blok sayısı 8 olmalı, bulunan: {len(ana_bloklar)}"
    for i in range(len(ana_bloklar)):
        for j in range(i + 1, len(ana_bloklar)):
            k = kesisim(ana_bloklar[i], ana_bloklar[j])
            assert k == 0.0, f"Kesişim {ana_bloklar[i]['ad']} - {ana_bloklar[j]['ad']}: {k}"

    dikey_sirali = ["kanal", "kunye", "baslik", "kok", "kA", "kB", "kural", "kaydet"]
    for i in range(len(dikey_sirali) - 1):
        b1 = b_dict[dikey_sirali[i]]
        b2 = b_dict[dikey_sirali[i + 1]]
        bosluk = b2["y"] - (b1["y"] + b1["h"])
        assert bosluk >= 12.0 - 1e-4, f"Dikey boşluk {b1['ad']} -> {b2['ad']}: {bosluk} < 12"

    # 5. Kök içi kuralları
    bx0 = float(TX) + Y.genislik("Fredoka", 700, "Look! She ", KOK_BOY)
    bx1 = bx0 + float(BOS_W)
    x1b = bx1 + Y.genislik("Fredoka", 700, " ", KOK_BOY)
    w_her = Y.genislik("Fredoka", 700, "her", KOK_BOY)
    s1b_sag = x1b + w_her
    assert s1b_sag + 24.0 <= float(TIS_X) + 1e-4, f"kok-s1b sağı + 24 ({s1b_sag + 24.0}) > {TIS_X}"

    w_s2 = Y.genislik("Fredoka", 700, "pink T-shirt today.", KOK_BOY)
    s2_sag = float(TX) + w_s2
    assert s2_sag + 24.0 <= float(TIS_X) + 1e-4, f"kok-s2 sağı + 24 ({s2_sag + 24.0}) > {TIS_X}"

    tis = b_dict["tisort"]
    assert tis["x"] - 64.0 >= 16.0 - 1e-4, f"tişört sol boşluk {tis['x'] - 64.0} < 16"
    assert 956.0 - (tis["x"] + tis["w"]) >= 16.0 - 1e-4, f"tişört sağ boşluk {956.0 - (tis['x'] + tis['w'])} < 16"
    assert tis["y"] - 574.0 >= 16.0 - 1e-4, f"tişört üst boşluk {tis['y'] - 574.0} < 16"
    assert 732.0 - (tis["y"] + tis["h"]) >= 16.0 - 1e-4, f"tişört alt boşluk {732.0 - (tis['y'] + tis['h'])} < 16"

    w_s1a = Y.genislik("Fredoka", 700, "Look! She", KOK_BOY)
    kok_yazilar = [
        ("kok-s1a", float(TX), w_s1a, float(L1)),
        ("kok-s1b", x1b, w_her, float(L1)),
        ("kok-s2", float(TX), w_s2, float(L2)),
    ]
    for ad, x, w, taban in kok_yazilar:
        assert x >= 92.0 - 1e-4, f"{ad} x ({x}) < 92"
        assert x + w <= 956.0 - 24.0 + 1e-4, f"{ad} sağ ({x + w}) > 956 - 24"
        y_ust = taban - 0.75 * KOK_BOY
        y_alt = taban + 0.25 * KOK_BOY
        assert y_ust >= 574.0 + 12.0 - 1e-4, f"{ad} üst ({y_ust}) < 574 + 12"
        assert y_alt <= 732.0 - 8.0 + 1e-4, f"{ad} alt ({y_alt}) > 732 - 8"

    yb = float(L1) + float(BOS_KAYMA)
    kok_s2_ust = float(L2) - 0.75 * KOK_BOY
    assert yb + 3.0 < kok_s2_ust, f"boşluk çizgisi {yb + 3.0} >= kok-s2 üstü {kok_s2_ust}"

    # 6. Şık içi kuralları
    assert (float(DAIRE_X) + float(DAIRE_R)) + 24.0 <= float(SIK_TX) + 1e-4, "daire sağı + 24 > SIK_TX"
    for gid, y0, metin in [("kA", SIK_Y[0], "wears"), ("kB", SIK_Y[1], "is wearing")]:
        w_m = Y.genislik("Fredoka", 700, metin, SIK_BOY)
        assert float(SIK_TX) + w_m <= 956.0 - 24.0 + 1e-4, f"{gid} metin sağı {float(SIK_TX) + w_m} > 956 - 24"
        cy = float(y0) + 44.0
        taban = cy + 22.0
        y_ust = taban - 48.0
        y_alt = taban + 16.0
        assert y_ust >= float(y0) + 2.0 - 1e-4, f"{gid} yazı üst {y_ust} < y0 + 2"
        assert y_alt <= float(y0) + 86.0 + 1e-4, f"{gid} yazı alt {y_alt} > y0 + 86"
        d_dis = float(DAIRE_R) + 2.0
        assert cy - d_dis >= float(y0) + 2.0 - 1e-4, f"{gid} daire üst {cy - d_dis} < y0 + 2"
        assert cy + d_dis <= float(y0) + 86.0 + 1e-4, f"{gid} daire alt {cy + d_dis} > y0 + 86"
        # harf (Fredoka 700 64, büyük harf ≈ 0,71·boy) dairenin iç kenarına ≥ 4 px uzak: üst ve taban köşeleri
        h_taban = cy + float(HARF_KAYMA)
        w_h = Y.genislik("Fredoka", 700, harf_ad := ("A" if gid == "kA" else "B"), SIK_BOY)
        ic_r = float(DAIRE_R) - 2.0
        assert (cy - ic_r) + 4.0 <= h_taban - 0.71 * SIK_BOY + 1e-4, f"{gid} {harf_ad} üstü daireye yakın"
        dy = h_taban - cy
        assert (w_h / 2.0) ** 2 + dy ** 2 <= (ic_r - 4.0) ** 2 + 1e-4, f"{gid} {harf_ad} taban köşesi daireye yakın"

    # 7. Kaydet kuralları
    yerimi_gorunur_sag = 126.0
    kx = float((YERIMI_X + 12 * YERIMI_S + 3) + 22)
    assert kx - yerimi_gorunur_sag >= 20.0 - 1e-4, f"yer imi sağ ile kaydet-yazi arası {kx - yerimi_gorunur_sag} < 20"
    w_kaydet = Y.genislik("Fredoka", 700, "Kaydet", KAYDET_BOY)
    assert kx + w_kaydet <= 960.0 + 1e-4, f"kaydet-yazi sağ kenar {kx + w_kaydet} > 960"
    yerimi_gorunur_alt = 1132.0
    assert yerimi_gorunur_alt <= 1140.0 + 1e-4, f"yer imi alt {yerimi_gorunur_alt} > 1140"

    # 8. Tek sarı: #icerik HTML'inde fill="#f2a93b" tam 1 kez (yerimi-dolgu), stroke="#f2a93b" 0 kez; kok, kA, kB gruplarında yok
    m_icerik = re.search(r'<g id="icerik">(.*?)</g>\s*</svg>', html, re.DOTALL)
    assert m_icerik, "#icerik grubu HTML içinde bulunamadı"
    icerik_html = m_icerik.group(1)
    cnt_vurgu_fill = icerik_html.count('fill="#f2a93b"')
    cnt_vurgu_stroke = icerik_html.count('stroke="#f2a93b"')
    assert cnt_vurgu_fill == 1, f"#icerik içinde fill=#f2a93b {cnt_vurgu_fill} kez bulundu, 1 olmalı"
    assert cnt_vurgu_stroke == 0, f"#icerik içinde stroke=#f2a93b {cnt_vurgu_stroke} kez bulundu, 0 olmalı"

    for gid in ("kok", "kA", "kB"):
        m_g = re.search(rf'<g id="{gid}">(.*?)</g>', icerik_html, re.DOTALL)
        assert m_g, f"#{gid} grubu bulunamadı"
        assert "#f2a93b" not in m_g.group(1), f"#{gid} içinde #f2a93b bulundu"

    # 9. Cevap yok: kA ve kB grupları normalleştirince eşit dize; kok grubunda cevap kelimeleri yok; yeşil yok
    def _norm_sik(s: str, gid: str, y0: int, h: str, m: str) -> str:
        cy = y0 + 44
        taban = cy + 22
        r = s.replace(gid, "kX")
        r = r.replace(str(y0), "Y0")
        r = r.replace(str(cy), "CY")
        r = r.replace(str(taban), "TABAN")
        r = r.replace(str(cy + HARF_KAYMA), "HTABAN")
        r = r.replace(f">{h}<", ">H<")
        r = r.replace(f">{m}<", ">M<")
        return r

    m_kA = re.search(r'<g id="kA">(.*?)</g>', icerik_html, re.DOTALL)
    m_kB = re.search(r'<g id="kB">(.*?)</g>', icerik_html, re.DOTALL)
    assert m_kA and m_kB, "kA veya kB grubu bulunamadı"
    kA_n = _norm_sik(m_kA.group(0), "kA", SIK_Y[0], "A", "wears")
    kB_n = _norm_sik(m_kB.group(0), "kB", SIK_Y[1], "B", "is wearing")
    assert kA_n == kB_n, f"kA ve kB normalize edilince eşit değil:\nkA: {kA_n}\nkB: {kB_n}"

    m_kok = re.search(r'<g id="kok">(.*?)</g>', icerik_html, re.DOTALL)
    assert m_kok, "kok grubu bulunamadı"
    assert "wears" not in m_kok.group(1), "kok grubu içinde 'wears' bulundu"
    assert "is wearing" not in m_kok.group(1), "kok grubu içinde 'is wearing' bulundu"

    assert "#167a4a" not in html.lower(), "HTML içinde yeşil (#167a4a) bulundu"

    # 10. Yasak kontrolleri
    svg_metinler = re.findall(r"<text[^>]*>(.*?)</text>", html, re.DOTALL)
    yasak_desenler = [
        r"tam\s+ders",
        r"dak[iı]ka",
        r"\bdk\b",
        r"\bqr\b",
        r"\bizle\b",
        r"\boynat\b",
        r"\bcevap\b",
        r"full\s+lesson",
        r"\bkanal\b",
    ]
    for sm in svg_metinler:
        for yd in yasak_desenler:
            assert not re.search(yd, sm, re.IGNORECASE), f"SVG metni içinde yasak desen ({yd}) bulundu: {sm}"

    cnt_yds = html.count(">@ydspublishing<")
    assert cnt_yds == 1, f"HTML içinde '>@ydspublishing<' {cnt_yds} kez bulundu, 1 olmalı"

    assert "opacity:0" not in html, "HTML içinde 'opacity:0' bulundu"
    assert R["kirmizi"] not in html, f"HTML içinde kırmızı ({R['kirmizi']}) bulundu"
    assert "#root.tema-acik" not in html, "HTML içinde '#root.tema-acik' bulundu"

    emoji_bulgular = re.findall(r"[\U0001F000-\U0010FFFF\u2600-\u27BF]", html)
    assert not emoji_bulgular, f"HTML içinde emoji bulundu: {emoji_bulgular}"

    for yasak_kod in ("Math.random", "Date", "try", "catch"):
        assert yasak_kod not in html, f"HTML içinde yasak JavaScript öğesi: {yasak_kod}"


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()

    defs = defs_svg()
    kunye = Y.kunye_svg()
    baslik = baslik_svg()
    kok = kok_karti_svg()
    kA = secenek_karti_svg("kA", SIK_Y[0], "A", "wears")
    kB = secenek_karti_svg("kB", SIK_Y[1], "B", "is wearing")
    kural = kural_svg()
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
{defs}
{kunye}
<g id="icerik">
{baslik}
{kok}
{kA}
{kB}
{kural}
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
        f"baslik={int(round(b_dict['baslik']['y']))}-{int(round(b_dict['baslik']['y'] + b_dict['baslik']['h']))} "
        f"kok={int(round(b_dict['kok']['y']))}-{int(round(b_dict['kok']['y'] + b_dict['kok']['h']))} "
        f"kA={int(round(b_dict['kA']['y']))}-{int(round(b_dict['kA']['y'] + b_dict['kA']['h']))} "
        f"kB={int(round(b_dict['kB']['y']))}-{int(round(b_dict['kB']['y'] + b_dict['kB']['h']))} "
        f"kural={int(round(b_dict['kural']['y']))}-{int(round(b_dict['kural']['y'] + b_dict['kural']['h']))} "
        f"kaydet={int(round(b_dict['kaydet']['y']))}-{int(round(b_dict['kaydet']['y'] + b_dict['kaydet']['h']))}"
    )

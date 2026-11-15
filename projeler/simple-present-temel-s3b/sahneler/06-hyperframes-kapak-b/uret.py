#!/usr/bin/python3
"""simple-present-temel-s3 sahne 06 kapak B (soru) index.html üretici
(HyperFrames DİKEY 1080x1920; tek kare, ses yok; huni v2)."""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

AD: Path = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET: Path = AD.parent.parent

# 1. zaman.json ve zamanlar.json okuma ve doğrulama (kalıp satır 21–33 aynen)
zaman_data: dict = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlari: list[dict] = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlari) == 1, f"duragan içinde {AD.name} kaydı tek olmalı"
duragan: dict = duragan_kayitlari[0]
assert duragan["kare"] == 1, f"kare {duragan['kare']} != 1"
assert duragan["cikti"] == "kapak-b.png", f"cikti {duragan['cikti']} != kapak-b.png"
assert AD.name not in [s["klasor"] for s in zaman_data.get("sahneler", [])], "AD.name sahneler içinde olmamalı"

Z: dict = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

# 2. Renk ve sabitler (SPEC §2)
R: dict[str, str] = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

X0: int = 60
X1: int = 960
ORTA: int = 510
Y0: int = 460
Y1: int = 1380
BAS1: str = "GOES mu,"
BAS2: str = "GO mu?"
KONTUR: int = 10
CAP: float = 0.71
VIRGUL: float = 0.16
ALT: float = 0.02
SATIR: float = 1.12
BAS_UST: int = 470
BAS_SON: int = 800
BAS_TAVAN: int = 190
KB: int = 72
KPAD: int = 64
KY: int = 860
KH: int = 260
KRX: int = 18
KCIZGI: int = 4
KT1: int = 957
KT2: int = 1061
BOS_PAY: int = 16
BOS_SON_ARA: int = 6
BOS_ALT: int = 10
BOS_CIZGI: int = 5
HB: int = 80
HAP_PAY: int = 44
HAP_Y: int = 1170
HAP_H: int = 120
HAP_CIZGI: int = 5
HAP_ARA: int = 40
QS: float = 1.6
Q_ARA: int = 48


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx: float = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy: float = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def hesapla_baslik() -> tuple[int, float, float, float, float]:
    """Başlık boyutu B ve satır tabanları T1, T2 ile genişlikleri hesaplar."""
    g1_1: float = Y.genislik("Fredoka", 700, BAS1, 1.0)
    g2_1: float = Y.genislik("Fredoka", 700, BAS2, 1.0)
    b_limit: float = min(
        float(BAS_TAVAN),
        (900.0 - KONTUR) / max(g1_1, g2_1),
        (BAS_SON - BAS_UST - KONTUR) / (CAP + SATIR + ALT),
    )
    b_val: int = math.floor(b_limit)
    bh: float = KONTUR + (CAP + SATIR + ALT) * b_val
    ust: float = BAS_UST + (BAS_SON - BAS_UST - bh) / 2.0
    t1: float = ust + KONTUR / 2.0 + CAP * b_val
    t2: float = t1 + SATIR * b_val
    g1: float = Y.genislik("Fredoka", 700, BAS1, b_val)
    g2: float = Y.genislik("Fredoka", 700, BAS2, b_val)
    return b_val, g1, g2, t1, t2


def hesapla_kart() -> tuple[float, float, float, float, float, float, float, float, float, float]:
    """Kart boyutları, satır konumları ve boşluk çizgisi noktalarını hesaplar."""
    bas1_metin: str = "He doesn't"
    bas2_metin: str = "Does she"
    nokta1_metin: str = "."
    nokta2_metin: str = "?"

    bos_w: int = math.ceil(Y.genislik("Fredoka", 700, "goes", KB)) + 2 * BOS_PAY

    b0_1_rel: float = Y.genislik("Fredoka", 700, bas1_metin + " ", KB)
    b1_1_rel: float = b0_1_rel + bos_w
    n_1_rel: float = b1_1_rel + BOS_SON_ARA
    l_1: float = n_1_rel + Y.genislik("Fredoka", 700, nokta1_metin, KB)

    b0_2_rel: float = Y.genislik("Fredoka", 700, bas2_metin + " ", KB)
    b1_2_rel: float = b0_2_rel + bos_w
    n_2_rel: float = b1_2_rel + BOS_SON_ARA
    l_2: float = n_2_rel + Y.genislik("Fredoka", 700, nokta2_metin, KB)

    lw: float = max(l_1, l_2)
    kw: float = lw + 2.0 * KPAD
    kx: float = ORTA - kw / 2.0
    tx: float = kx + KPAD

    b0_1: float = tx + b0_1_rel
    b1_1: float = b0_1 + bos_w
    n_1: float = b1_1 + BOS_SON_ARA

    b0_2: float = tx + b0_2_rel
    b1_2: float = b0_2 + bos_w
    n_2: float = b1_2 + BOS_SON_ARA

    return lw, kw, kx, tx, b0_1, b1_1, n_1, b0_2, b1_2, n_2


def hesapla_haplar() -> tuple[int, float, float, float, float, float, float]:
    """İki eş hap ve soru işareti konumlarını hesaplar."""
    hap_w: int = math.ceil(Y.genislik("Fredoka", 700, "goes", HB)) + 2 * HAP_PAY
    rw: float = 2.0 * hap_w + HAP_ARA + Q_ARA + 57.0 * QS
    rx0: float = ORTA - rw / 2.0
    hap1_x: float = rx0
    hap2_x: float = rx0 + hap_w + HAP_ARA
    qx: float = hap2_x + hap_w + Q_ARA
    qy: float = HAP_Y + HAP_H / 2.0 - 50.0 * QS
    return hap_w, rw, rx0, hap1_x, hap2_x, qx, qy


def baslik_svg(b_val: int, t1: float, t2: float) -> str:
    """Başlık SVG grubunu üretir (iki satır ortalı text)."""
    r_mur: str = R["murekkep"]
    r_zem: str = R["zemin"]
    return (
        f'<g id="baslik">\n'
        f'<text id="bas1" x="{ORTA}" y="{t1:.2f}" text-anchor="middle" font-family="Fredoka" '
        f'font-weight="700" font-size="{b_val}" fill="{r_mur}" stroke="{r_zem}" '
        f'stroke-width="{KONTUR}" stroke-linejoin="round" '
        f'style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">{BAS1}</text>\n'
        f'<text id="bas2" x="{ORTA}" y="{t2:.2f}" text-anchor="middle" font-family="Fredoka" '
        f'font-weight="700" font-size="{b_val}" fill="{r_mur}" stroke="{r_zem}" '
        f'stroke-width="{KONTUR}" stroke-linejoin="round" '
        f'style="font-kerning:none;paint-order:stroke fill" xml:space="preserve">{BAS2}</text>\n'
        f'</g>'
    )


def kart_svg(
    kw: float,
    kx: float,
    tx: float,
    b0_1: float,
    b1_1: float,
    n_1: float,
    b0_2: float,
    b1_2: float,
    n_2: float,
) -> str:
    """Kâğıt kart SVG grubunu üretir (zemin, 2 satır metin, 2 boşluk çizgisi)."""
    y1: float = KT1 + BOS_ALT
    y2: float = KT2 + BOS_ALT
    return (
        f'<g id="kart">\n'
        f'<rect id="kart-zemin" x="{kx:.2f}" y="{KY}" width="{kw:.2f}" height="{KH}" rx="{KRX}" '
        f'fill="#fff9e6" stroke="#1b1a17" stroke-width="{KCIZGI}"/>\n'
        f'<text id="k1a" x="{tx:.2f}" y="{KT1}" font-family="Fredoka" font-weight="700" '
        f'font-size="{KB}" fill="#1b1a17" style="font-kerning:none" xml:space="preserve">He doesn\'t</text>\n'
        f'<text id="k1b" x="{n_1:.2f}" y="{KT1}" font-family="Fredoka" font-weight="700" '
        f'font-size="{KB}" fill="#1b1a17" style="font-kerning:none" xml:space="preserve">.</text>\n'
        f'<text id="k2a" x="{tx:.2f}" y="{KT2}" font-family="Fredoka" font-weight="700" '
        f'font-size="{KB}" fill="#1b1a17" style="font-kerning:none" xml:space="preserve">Does she</text>\n'
        f'<text id="k2b" x="{n_2:.2f}" y="{KT2}" font-family="Fredoka" font-weight="700" '
        f'font-size="{KB}" fill="#1b1a17" style="font-kerning:none" xml:space="preserve">?</text>\n'
        f'<g id="bosluk" fill="none" stroke="#1b1a17" stroke-width="{BOS_CIZGI}" stroke-linecap="round">\n'
        f'<path id="bos1" d="M{b0_1:.2f} {y1 + 1.5:.2f} Q{(b0_1 + b1_1) / 2.0:.2f} {y1 - 2.5:.2f} {b1_1:.2f} {y1 + 1.5:.2f}"/>\n'
        f'<path id="bos2" d="M{b0_2:.2f} {y2 + 1.5:.2f} Q{(b0_2 + b1_2) / 2.0:.2f} {y2 - 2.5:.2f} {b1_2:.2f} {y2 + 1.5:.2f}"/>\n'
        f'</g>\n'
        f'</g>'
    )


def haplar_svg(hap_w: int, hap1_x: float, hap2_x: float) -> str:
    """İki eş hap SVG grubu ve dışındaki metinleri üretir."""
    r_mur: str = R["murekkep"]
    taban: float = HAP_Y + HAP_H / 2.0 + 16.0
    return (
        f'<g id="haplar" fill="none" stroke="{r_mur}" stroke-width="{HAP_CIZGI}">\n'
        f'<rect id="hap-go" x="{hap1_x:.2f}" y="{HAP_Y}" width="{hap_w}" height="{HAP_H}" rx="{HAP_H / 2.0:.2f}"/>\n'
        f'<rect id="hap-goes" x="{hap2_x:.2f}" y="{HAP_Y}" width="{hap_w}" height="{HAP_H}" rx="{HAP_H / 2.0:.2f}"/>\n'
        f'</g>\n'
        f'<text id="hap-go-yazi" x="{hap1_x + hap_w / 2.0:.2f}" y="{taban:.2f}" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="{HB}" fill="{r_mur}" '
        f'style="font-kerning:none">go</text>\n'
        f'<text id="hap-goes-yazi" x="{hap2_x + hap_w / 2.0:.2f}" y="{taban:.2f}" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="{HB}" fill="{r_mur}" '
        f'style="font-kerning:none">goes</text>'
    )


def soru_svg(qx: float, qy: float) -> str:
    """Büyük sarı kalem ? SVG grubunu üretir."""
    r_vur: str = R["vurgu"]
    return (
        f'<g id="soru" transform="translate({qx:.2f} {qy:.2f}) scale({QS})" fill="none" stroke="{r_vur}" '
        f'stroke-linecap="round" stroke-linejoin="round">\n'
        f'<path id="soru-kanca" d="M3 27 C3 11 15 2 29 2 C44 2 54 12 54 27 C54 41 44 47 35 53 C29 57 28 63 28 72" '
        f'stroke-width="11"/>\n'
        f'<path id="soru-nokta" d="M28 92 L28 92.01" stroke-width="15"/>\n'
        f'</g>'
    )


def blok_kutulari(
    b_val: int,
    g1: float,
    g2: float,
    t1: float,
    t2: float,
    kx: float,
    kw: float,
    hap_w: int,
    hap1_x: float,
    hap2_x: float,
    qx: float,
    qy: float,
) -> list[dict[str, str | float]]:
    """SPEC §4'e göre 7 blok kutusunu hesaplar ve sırasıyla döndürür."""
    rozet_x: float
    rozet_w: float
    rozet_x, rozet_w = Y.rozet_konumu()
    konu_b: int = Y.konu_boyu()

    y_kunye: float = min(386.0, 420.0 - 0.75 * konu_b)
    y_baslik: float = t1 - CAP * b_val - KONTUR / 2.0
    w_baslik: float = max(g1, g2) + KONTUR
    h_baslik: float = t2 + ALT * b_val + KONTUR / 2.0 - y_baslik

    return [
        {
            "ad": "kanal",
            "x": 60.0,
            "y": 291.0,
            "w": 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - 60.0,
            "h": 48.0,
        },
        {
            "ad": "kunye",
            "x": 60.0,
            "y": y_kunye,
            "w": rozet_x + rozet_w - 60.0,
            "h": max(434.0, 420.0 + 0.25 * konu_b) - y_kunye,
        },
        {
            "ad": "baslik",
            "x": ORTA - max(g1, g2) / 2.0 - KONTUR / 2.0,
            "y": y_baslik,
            "w": w_baslik,
            "h": h_baslik,
        },
        {
            "ad": "kart",
            "x": kx - KCIZGI / 2.0,
            "y": KY - KCIZGI / 2.0,
            "w": kw + KCIZGI,
            "h": KH + KCIZGI,
        },
        {
            "ad": "hap-go",
            "x": hap1_x - HAP_CIZGI / 2.0,
            "y": HAP_Y - HAP_CIZGI / 2.0,
            "w": hap_w + HAP_CIZGI,
            "h": HAP_H + HAP_CIZGI,
        },
        {
            "ad": "hap-goes",
            "x": hap2_x - HAP_CIZGI / 2.0,
            "y": HAP_Y - HAP_CIZGI / 2.0,
            "w": hap_w + HAP_CIZGI,
            "h": HAP_H + HAP_CIZGI,
        },
        {
            "ad": "soru",
            "x": qx - 2.5 * QS,
            "y": qy - 3.5 * QS,
            "w": 62.0 * QS,
            "h": 103.0 * QS,
        },
    ]


def kurallari_dogrula(
    bloklar: list[dict[str, str | float]],
    b_val: int,
    g1: float,
    g2: float,
    kx: float,
    kw: float,
    tx: float,
    lw: float,
    html: str,
) -> None:
    """SPEC §6 kurallarını ve kabul ölçütlerini doğrular."""
    b_dict: dict[str, dict[str, float]] = {
        str(b["ad"]): {k: float(b[k]) for k in ("x", "y", "w", "h")} for b in bloklar
    }

    # 1. Sınır: kanal c x [60, 960] x y [280, 350]; kunye c x [60, 960] x y [360, 450]; ötekiler c [60, 960] x [460, 1320]
    for ad, b in b_dict.items():
        assert b["x"] >= 60.0 - 1e-4, f"{ad} sol {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ {b['x'] + b['w']} > 960"
        if ad == "kanal":
            assert b["y"] >= 280.0 - 1e-4 and b["y"] + b["h"] <= 350.0 + 1e-4, f"kanal y out: {b['y']}"
        elif ad == "kunye":
            assert b["y"] >= 360.0 - 1e-4 and b["y"] + b["h"] <= 450.0 + 1e-4, f"kunye y out: {b['y']}"
        else:
            assert b["y"] >= 460.0 - 1e-4 and b["y"] + b["h"] <= 1320.0 + 1e-4, f"{ad} y out: {b['y']}"

    # 2. Bant: baslik y >= 465 ve alt <= 805; kart üstü >= baslik altı + 40; hap-go, hap-goes, soru üstü >= kart altı + 20
    baslik_y: float = b_dict["baslik"]["y"]
    baslik_alt: float = baslik_y + b_dict["baslik"]["h"]
    assert baslik_y >= 465.0 - 1e-4, f"baslik y {baslik_y} < 465"
    assert baslik_alt <= 805.0 + 1e-4, f"baslik alt {baslik_alt} > 805"

    kart_y: float = b_dict["kart"]["y"]
    kart_alt: float = kart_y + b_dict["kart"]["h"]
    assert kart_y - baslik_alt >= 40.0 - 1e-4, f"kart üstü - baslik altı {kart_y - baslik_alt} < 40"

    for h_ad in ("hap-go", "hap-goes", "soru"):
        h_y: float = b_dict[h_ad]["y"]
        assert h_y - kart_alt >= 20.0 - 1e-4, f"{h_ad} üstü - kart altı {h_y - kart_alt} < 20"

    # 3. Kesişim 0 (7 blok -> 21 çift)
    blok_listesi: list[dict[str, float]] = list(b_dict.values())
    blok_adlari: list[str] = list(b_dict.keys())
    for i in range(len(blok_listesi)):
        for j in range(i + 1, len(blok_listesi)):
            k: float = kesisim(blok_listesi[i], blok_listesi[j])
            assert k == 0.0, f"Kesişim {blok_adlari[i]} - {blok_adlari[j]}: {k}"

    # 4. Yazı boyu: 64 <= B <= 190; KB == 72; HB == 80. Başlık satır genişliği + KONTUR <= 900.
    assert 64 <= b_val <= 190, f"Başlık boyutu B={b_val} sınır dışı"
    assert KB == 72, f"KB {KB} != 72"
    assert HB == 80, f"HB {HB} != 80"
    assert max(g1, g2) + KONTUR <= 900.0 + 1e-4, f"Başlık satır genişliği {max(g1, g2) + KONTUR} > 900"
    assert tx >= kx + 40.0 - 1e-4, f"TX {tx} < KX + 40"
    assert tx + lw <= kx + kw - 40.0 + 1e-4, f"TX + LW {tx + lw} > KX + KW - 40"
    assert KT1 - 0.73 * KB >= KY + 30.0 - 1e-4, "KT1 - 0.73*KB < KY + 30"
    assert KT2 + BOS_ALT + 4 <= KY + KH - 30.0 + 1e-4, "KT2 + BOS_ALT + 4 > KY + KH - 30"

    # 5. Başlık 2 satır, toplam 4 sözcük; her ekran satırı <= 24 karakter
    baslik_satirlari: list[str] = [BAS1, BAS2]
    assert len(baslik_satirlari) == 2, "Başlık satır sayısı != 2"
    assert len(" ".join(baslik_satirlari).split()) == 4, "Başlık sözcük sayısı != 4"
    tum_satirlar: list[str] = [BAS1, BAS2, "He doesn't ____.", "Does she ____?", "go", "goes"]
    for s_metin in tum_satirlar:
        assert len(s_metin) <= 24, f"Satır uzunluğu > 24: {s_metin}"

    # 6. Görünen metin taraması
    gorunen_metinler: set[str] = set(re.findall(r">([^<]+)</text>", html))
    beklenen_metinler: set[str] = {
        "@ydspublishing", "Simple Present", "YDT · TEMEL", "GOES mu,", "GO mu?",
        "He doesn't", ".", "Does she", "?", "go", "goes",
    }
    assert gorunen_metinler == beklenen_metinler, f"Görünen metinler eşleşmiyor: {gorunen_metinler ^ beklenen_metinler}"
    yasak_kelimeler: list[str] = [
        "tam" + " ders",
        "dak" + "ika",
        "izle",
        "qr",
        "kanal",
    ]
    for gm in gorunen_metinler:
        gm_lower: str = gm.lower()
        for yk in yasak_kelimeler:
            assert yk not in gm_lower, f"Görünen metinde yasak sözcük bulundu: {yk!r} in {gm!r}"
        for ch in gm:
            assert ord(ch) <= 0x2FFF, f"Görünen metinde emoji/simge bulundu: {ch!r} (U+{ord(ch):04X})"
            assert ch not in ("_", "✗", "✓"), f"Yasak karakter bulundu: {ch!r}"

    # 7. Bütün HTML kontrolleri
    html_lower: str = html.lower()
    for yasak_kod in ("math.random", "date.now", "new date", "opacity:0", "<circle", "<img", "#root.tema-acik"):
        assert yasak_kod not in html_lower, f"Yasak kod/özellik bulundu: {yasak_kod}"

    hex_renkler: set[str] = set(re.findall(r"#[0-9a-fA-F]{6}\b", html))
    gecerli_renkler: set[str] = {
        R["zemin"].lower(),
        R["murekkep"].lower(),
        R["ikincil"].lower(),
        R["vurgu"].lower(),
        "#fff9e6",
        "#fffdf8",
    }
    assert hex_renkler <= gecerli_renkler, f"Geçersiz hex renk: {hex_renkler - gecerli_renkler}"
    for yasak_renk in ("#e0473b", "#d6453a", "#167a4a", "#fece00"):
        assert yasak_renk not in html_lower, f"Yasak renk bulundu: {yasak_renk}"

    assert html.count(R["vurgu"]) == 2, f"R['vurgu'] sayısı {html.count(R['vurgu'])} != 2"
    assert html.count('id="kanal"') == 1, "id='kanal' sayısı != 1"
    assert html.count('id="logoimg"') == 1, "id='logoimg' sayısı != 1"
    assert html.count("<image") == 1, "<image sayısı != 1"

    # 8. Var olması ve olmaması gereken id'ler
    gerekli_idler: list[str] = [
        "baslik", "bas1", "bas2", "kart", "kart-zemin", "k1a", "k1b", "k2a", "k2b",
        "bosluk", "bos1", "bos2", "haplar", "hap-go", "hap-goes", "hap-go-yazi", "hap-goes-yazi",
        "soru", "soru-kanca", "soru-nokta",
    ]
    for gid in gerekli_idler:
        assert f'id="{gid}"' in html, f"Eksik id: {gid}"

    yasak_idler: list[str] = [
        "karakter", "daire", "bk-kutu", "t2", "ku-nokta", "rz1", "ku-cip",
    ]
    for yid in yasak_idler:
        assert f'id="{yid}"' not in html, f"Yasak id bulundu: {yid}"
    assert not re.search(r'\bid="hap"\b', html), "Yasak tek başına 'hap' id'si bulundu"

    # 9. Zaman çizelgesi kalıpla aynı
    assert 'tl.set("#sahne", { opacity: 1, immediateRender: false }, 0);' in html or \
           'tl.set("#sahne", {opacity: 1, immediateRender: false}, 0)' in html
    assert 'window.__timelines["main"]' in html


def uret() -> tuple[str, int, float, float, float, int, list[dict[str, str | float]]]:
    """Sahne HTML'i, yerleşim değişkenleri ve blok kutularını üretir."""
    b_val, g1, g2, t1, t2 = hesapla_baslik()
    lw, kw, kx, tx, b0_1, b1_1, n_1, b0_2, b1_2, n_2 = hesapla_kart()
    hap_w, rw, rx0, hap1_x, hap2_x, qx, qy = hesapla_haplar()

    kunye: str = Y.kunye_svg()
    baslik: str = baslik_svg(b_val, t1, t2)
    kart: str = kart_svg(kw, kx, tx, b0_1, b1_1, n_1, b0_2, b1_2, n_2)
    haplar: str = haplar_svg(hap_w, hap1_x, hap2_x)
    soru: str = soru_svg(qx, qy)

    bloklar: list[dict[str, str | float]] = blok_kutulari(
        b_val, g1, g2, t1, t2, kx, kw, hap_w, hap1_x, hap2_x, qx, qy
    )

    root_attrs: str = (
        f'data-composition-id="main" data-start="0" data-duration="{Z["sure"]}" '
        f'data-fps="30" data-width="1080" data-height="1920"'
    )

    html: str = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
.tema-acik #kart-zemin{{fill:#fffdf8;}}
#root #kart-zemin{{stroke:var(--pilMetin);}}
#root #bosluk{{stroke:var(--pilMetin);}}
</style></head><body>
<div id="root" {root_attrs}>
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{baslik}
{kart}
{haplar}
{soru}
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

    kurallari_dogrula(bloklar, b_val, g1, g2, kx, kw, tx, lw, html)
    return html, b_val, kx, kw, rx0, hap_w, bloklar


if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")

    html, b_val, kx, kw, rx0, hap_w, bloklar = uret()
    (proje_dizini / "index.html").write_text(html, encoding="utf-8")

    nesneler: list[dict[str, str | int]] = [
        {
            "ad": str(b["ad"]),
            "x": int(round(float(b["x"]))),
            "y": int(round(float(b["y"]))),
            "w": int(round(float(b["w"]))),
            "h": int(round(float(b["h"]))),
        }
        for b in bloklar
    ]
    (AD / "nesneler.json").write_text(
        json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"index.html yazıldı {len(html)}")
    print(f"B={b_val} KX={kx:.1f} KW={kw:.1f} RX0={rx0:.1f} HAP_W={hap_w}")

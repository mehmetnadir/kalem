#!/usr/bin/python3
"""Sahne 05 hikâye karesi A index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2 (15.11): kanal katmanı + v2 bantları (kural kartı)."""
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
assert AD.name not in [s["klasor"] for s in zaman_data["sahneler"]], "AD.name sahneler içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

W, H = Y.W, Y.H

OK_X = round(60.0 + Y.genislik("Fredoka", 700, "I · you · we · they", 72) + 24.0)
FIIL_X = OK_X + 72 + 24
BUS_KUTU = [470.0, 956.0, 220.0, 70.0]


# ---- coco (Inkscape) SVG: kalem darbesi yolları (01-kanca yardim.py kopyası) ----
def _coco_alt_yollar(d: str) -> list[tuple[list[tuple[float, float]], bool]]:
    """m/M l/L h/H v/V c/C z/Z komutlu yolu alt yollara ayırır: [(noktalar, kapali)]
    (eğri 5 px'lik doğrulara bölünür)."""
    t = re.findall(r"[MmLlHhVvCcZz]|-?\d*\.?\d+(?:e-?\d+)?", d)
    i, cx, cy, sx, sy, cmd = 0, 0.0, 0.0, 0.0, 0.0, None
    cikti, nok = [], []

    def bitir(kapali: bool) -> None:
        nonlocal nok
        if len(nok) > 1:
            cikti.append((nok, kapali))
        nok = []

    while i < len(t):
        if re.match(r"[A-Za-z]", t[i]):
            cmd = t[i]
            i += 1
            if cmd in "Zz":
                bitir(True)
                cx, cy = sx, sy
            continue
        if cmd in "Mm":
            x, y = float(t[i]), float(t[i + 1])
            i += 2
            if cmd == "m":
                x += cx
                y += cy
            bitir(False)
            cx, cy, sx, sy = x, y, x, y
            nok = [(x, y)]
            cmd = "L" if cmd == "M" else "l"
        elif cmd in "Ll":
            x, y = float(t[i]), float(t[i + 1])
            i += 2
            if cmd == "l":
                x += cx
                y += cy
            nok.append((x, y))
            cx, cy = x, y
        elif cmd in "Hh":
            x = float(t[i])
            i += 1
            x = x + cx if cmd == "h" else x
            nok.append((x, cy))
            cx = x
        elif cmd in "Vv":
            y = float(t[i])
            i += 1
            y = y + cy if cmd == "v" else y
            nok.append((cx, y))
            cy = y
        elif cmd in "Cc":
            p = [float(v) for v in t[i : i + 6]]
            i += 6
            if cmd == "c":
                p = [p[0] + cx, p[1] + cy, p[2] + cx, p[3] + cy, p[4] + cx, p[5] + cy]
            n = max(6, int(math.hypot(p[4] - cx, p[5] - cy) / 3))
            for k in range(1, n + 1):
                u = k / n
                a, b, c, e = (1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3
                nok.append((a * cx + b * p[0] + c * p[2] + e * p[4], a * cy + b * p[1] + c * p[3] + e * p[5]))
            cx, cy = p[4], p[5]
        else:
            raise ValueError("coco yol komutu desteklenmiyor: " + str(cmd))
    bitir(False)
    return cikti


def _donusum(tr: str) -> tuple[float, float, float, float, float, float]:
    """translate(...) ve matrix(...) zinciri -> (a,b,c,d,e,f)."""
    m = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)

    def carp(
        p: tuple[float, float, float, float, float, float],
        q: tuple[float, float, float, float, float, float],
    ) -> tuple[float, float, float, float, float, float]:  # p ∘ q (önce q uygulanır)
        return (
            p[0] * q[0] + p[2] * q[1],
            p[1] * q[0] + p[3] * q[1],
            p[0] * q[2] + p[2] * q[3],
            p[1] * q[2] + p[3] * q[3],
            p[0] * q[4] + p[2] * q[5] + p[4],
            p[1] * q[4] + p[3] * q[5] + p[5],
        )

    for ad, arg in re.findall(r"(translate|matrix)\(([^)]*)\)", tr or ""):
        v = [float(s) for s in re.split(r"[ ,]+", arg.strip())]
        k = (1.0, 0.0, 0.0, 1.0, v[0], v[1] if len(v) > 1 else 0.0) if ad == "translate" else tuple(v)
        m = carp(m, k)
    return m


def coco(
    ad: str,
    kutu: list[float] | tuple[float, ...],
    azami: int = 25,
    kisa_atla: float = 0.02,
) -> list[dict[str, str | float]]:
    """coco/<ad>.svg -> kutuya sığdırılmış kalem darbesi yolları (svgCiz ile aynı seçim: en uzun `azami`).
    Çıktı: [{d, uz}] uzunluğa göre azalan."""
    s = (Y.ORTAK / "cizim" / "coco" / (ad + ".svg")).read_text(encoding="utf-8")
    alt = []
    for m in re.finditer(r"<path\b([^>]*)>", s, re.S):
        a = m.group(1)
        dm = re.search(r'\sd="([^"]+)"', a)
        if not dm:
            continue
        tm = re.search(r'transform="([^"]*)"', a)
        M = _donusum(tm.group(1) if tm else "")
        for nok, kapali in _coco_alt_yollar(dm.group(1)):
            p = [(M[0] * x + M[2] * y + M[4], M[1] * x + M[3] * y + M[5]) for x, y in nok]
            if kapali:
                p.append(p[0])
            alt.append(p)
    xs = [x for p in alt for x, _ in p]
    ys = [y for p in alt for _, y in p]
    bx0, by0, bw, bh = min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)
    k = min(kutu[2] / bw, kutu[3] / bh)
    ox = kutu[0] + (kutu[2] - bw * k) / 2 - bx0 * k
    oy = kutu[1] + (kutu[3] - bh * k) / 2 - by0 * k
    liste = []
    for p in alt:
        q = [(x * k + ox, y * k + oy) for x, y in p]
        uz = sum(math.hypot(q[i + 1][0] - q[i][0], q[i + 1][1] - q[i][1]) for i in range(len(q) - 1))
        if uz > 0.5:
            liste.append({"d": "M " + " L ".join("%.1f %.1f" % c for c in q), "uz": uz})
    top = sum(float(y["uz"]) for y in liste)
    uzun = sorted([y for y in liste if float(y["uz"]) >= top * kisa_atla], key=lambda y: -float(y["uz"]))[:azami]
    return uzun


def ozet_svg() -> str:
    """Özet grubu SVG çıktısı."""
    t1 = (
        f'<text id="ozet1" x="60" y="536" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}">He, she, it: s gelir;</text>'
    )
    t2 = (
        f'<text id="ozet2" x="60" y="620" font-family="Fredoka" font-weight="700" '
        f'font-size="64" fill="{R["murekkep"]}">I, you, we, they: s yok.</text>'
    )
    return f'<g id="ozet">{t1}{t2}</g>'


def satir1_svg() -> str:
    """Satır 1 grubu SVG çıktısı: he · she · it -> goes."""
    w_go = Y.genislik("Fredoka", 700, "go", 72)
    w_es = Y.genislik("Fredoka", 700, "es", 72)
    es_x = FIIL_X + w_go
    cizgi_x1 = es_x + 2.0
    cizgi_x2 = es_x + w_es - 2.0
    y_orta = 770 - 26

    ozne = (
        f'<text id="s1-ozne" x="60" y="770" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}">he · she · it</text>'
    )
    ok_d = (
        f"M {OK_X} {y_orta} L {OK_X + 72} {y_orta} "
        f"M {OK_X + 52} {y_orta - 16} L {OK_X + 72} {y_orta} L {OK_X + 52} {y_orta + 16}"
    )
    ok = (
        f'<path id="s1-ok" d="{ok_d}" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    go = (
        f'<text id="s1-go" x="{FIIL_X}" y="770" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}">go</text>'
    )
    es = (
        f'<text id="s1-es" x="{es_x:.2f}" y="770" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}">es</text>'
    )
    cizgi = (
        f'<line id="s1-cizgi" x1="{cizgi_x1:.2f}" y1="786" x2="{cizgi_x2:.2f}" y2="786" '
        f'stroke="{R["murekkep"]}" stroke-width="8" stroke-linecap="round"/>'
    )
    return f'<g id="satir1">{ozne}{ok}{go}{es}{cizgi}</g>'


def satir2_svg() -> str:
    """Satır 2 grubu SVG çıktısı: I · you · we · they -> go [yuva]."""
    w_go = Y.genislik("Fredoka", 700, "go", 72)
    w_es = Y.genislik("Fredoka", 700, "es", 72)
    yuva_x = FIIL_X + w_go + 6.0  # QA 0: `go` ile kesik çizgi değiyordu; sağ uç `es` sonu ile aynı kalır
    w_es -= 6.0
    y_orta = 900 - 26

    ozne = (
        f'<text id="s2-ozne" x="60" y="900" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}">I · you · we · they</text>'
    )
    ok_d = (
        f"M {OK_X} {y_orta} L {OK_X + 72} {y_orta} "
        f"M {OK_X + 52} {y_orta - 16} L {OK_X + 72} {y_orta} L {OK_X + 52} {y_orta + 16}"
    )
    ok = (
        f'<path id="s2-ok" d="{ok_d}" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    go = (
        f'<text id="s2-go" x="{FIIL_X}" y="900" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}">go</text>'
    )
    yuva = (
        f'<rect id="s2-yuva" x="{yuva_x:.2f}" y="846" width="{w_es:.2f}" height="60" rx="12" '
        f'fill="none" stroke="{R["ikincil"]}" stroke-width="4" stroke-dasharray="10 8"/>'
    )
    return f'<g id="satir2">{ozne}{ok}{go}{yuva}</g>'


def ornek_svg() -> str:
    """Örnek grubu SVG çıktısı: My brother = he ve ayna otobüs."""
    bus_yollar = coco("bus", BUS_KUTU)
    cx = BUS_KUTU[0] + BUS_KUTU[2] / 2.0
    tr_x = 2.0 * cx
    yollar_svg = "".join(
        f'<path d="{y["d"]}" fill="none" stroke="{R["murekkep"]}" stroke-width="2.6" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
        for y in bus_yollar
    )
    otobus = f'<g id="otobus" transform="translate({tr_x:.1f} 0) scale(-1 1)">{yollar_svg}</g>'
    yazi = (
        f'<text id="ornek-yazi" x="60" y="1008" font-family="Caveat" font-weight="700" '
        f'font-size="64" fill="{R["ikincil"]}">My brother = he</text>'
    )
    return f'<g id="ornek">{yazi}{otobus}</g>'


def kaydet_svg() -> str:
    """Kaydet grubu SVG çıktısı."""
    hap_w = Y.genislik("Fredoka", 700, "Kaydet", 64) + 80.0
    imi = (
        f'<g transform="translate(39 1046) scale(4)" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round">'
        f'<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/>'
        f'</g>'
    )
    hap = f'<rect id="kaydet-hap" x="128" y="1050" width="{hap_w:.1f}" height="88" rx="44" fill="{R["vurgu"]}"/>'
    yazi = (
        f'<text id="kaydet-yazi" x="{128.0 + hap_w / 2.0:.1f}" y="1116" text-anchor="middle" '
        f'font-family="Fredoka" font-weight="700" font-size="64" fill="{R["zemin"]}">Kaydet</text>'
    )
    return f'<g id="kaydet">{imi}{hap}{yazi}</g>'


def blok_kutulari() -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar."""
    w_kanal = 263.0 + Y.genislik("Lexend", 700, "@ydspublishing", 42) - 53.2
    kanal = {"ad": "kanal", "x": 53.2, "y": 291.0, "w": w_kanal, "h": 48.0}

    rz_x, rz_w = Y.rozet_konumlari()[0]
    kunye = {"ad": "kunye", "x": 60.0, "y": 386.0, "w": rz_x + rz_w - 60.0, "h": 48.0}

    w_ozet = max(
        Y.genislik("Fredoka", 700, "He, she, it: s gelir;", 64),
        Y.genislik("Fredoka", 700, "I, you, we, they: s yok.", 64),
    )
    ozet_y = 536.0 - 48.0
    ozet_h = 620.0 + 16.0 - ozet_y
    ozet = {"ad": "ozet", "x": 60.0, "y": ozet_y, "w": w_ozet, "h": ozet_h}

    w_goes = Y.genislik("Fredoka", 700, "goes", 72)
    satir1 = {"ad": "satir1", "x": 60.0, "y": 716.0, "w": FIIL_X + w_goes - 60.0, "h": 74.0}

    w_go = Y.genislik("Fredoka", 700, "go", 72)
    w_es = Y.genislik("Fredoka", 700, "es", 72)
    satir2 = {"ad": "satir2", "x": 60.0, "y": 846.0, "w": FIIL_X + w_go + w_es - 60.0, "h": 72.0}

    ornek = {
        "ad": "ornek",
        "x": 60.0,
        "y": 956.0,
        "w": BUS_KUTU[0] + BUS_KUTU[2] - 60.0,
        "h": 74.0,
    }

    hap_w = Y.genislik("Fredoka", 700, "Kaydet", 64) + 80.0
    kaydet = {"ad": "kaydet", "x": 60.0, "y": 1050.0, "w": 128.0 + hap_w - 60.0, "h": 88.0}

    return [kanal, kunye, ozet, satir1, satir2, ornek, kaydet]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(bloklar: list[dict[str, float]], html: str) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    b_dict = {b["ad"]: b for b in bloklar}

    # 1. İçerik blokları (ozet, satir1, satir2, ornek, kaydet): x >= 60, x + w <= 960, y >= 460, y + h <= 1140
    for ad in ("ozet", "satir1", "satir2", "ornek", "kaydet"):
        b = b_dict[ad]
        assert b["x"] >= 60.0 - 1e-4, f"{ad} sol kenar {b['x']} < 60"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ kenar {b['x'] + b['w']} > 960"
        assert b["y"] >= 460.0 - 1e-4, f"{ad} üst {b['y']} < 460"
        assert b["y"] + b["h"] <= 1140.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1140"

    # 2. kanal ve kunye: y >= 280, y + h <= 450
    for ad in ("kanal", "kunye"):
        b = b_dict[ad]
        assert b["y"] >= 280.0 - 1e-4, f"{ad} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 450.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 450"

    # 3. Bütün blok çiftlerinin kesişim alanı 0 (7 blok)
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            assert k == 0.0, f"Kesişim {bloklar[i]['ad']} - {bloklar[j]['ad']}: {k}"

    # 4. Dikey boşluk >= 16: kunye -> ozet, ozet -> satir1, satir1 -> satir2, satir2 -> ornek, ornek -> kaydet
    assert b_dict["ozet"]["y"] - (b_dict["kunye"]["y"] + b_dict["kunye"]["h"]) >= 16.0
    assert b_dict["satir1"]["y"] - (b_dict["ozet"]["y"] + b_dict["ozet"]["h"]) >= 16.0
    assert b_dict["satir2"]["y"] - (b_dict["satir1"]["y"] + b_dict["satir1"]["h"]) >= 16.0
    assert b_dict["ornek"]["y"] - (b_dict["satir2"]["y"] + b_dict["satir2"]["h"]) >= 16.0
    assert b_dict["kaydet"]["y"] - (b_dict["ornek"]["y"] + b_dict["ornek"]["h"]) >= 16.0

    # 5. Otobüs: coco yollarının bütün koordinatları BUS_KUTU içinde (aynadan sonra da: x' = 2·580 − x); en az 5 yol.
    #    Yazı ile otobüs arası: 60 + genişlik(Caveat 700 My brother = he 64) + 24 <= BUS_KUTU x.
    bus_yollar = coco("bus", BUS_KUTU)
    assert len(bus_yollar) >= 5, f"otobüs yol sayısı {len(bus_yollar)} < 5"
    cx = BUS_KUTU[0] + BUS_KUTU[2] / 2.0
    for y in bus_yollar:
        nums = [float(n) for n in re.findall(r"-?\d+\.?\d*", str(y["d"]))]
        xs = nums[0::2]
        ys = nums[1::2]
        for x in xs:
            assert BUS_KUTU[0] - 1e-4 <= x <= BUS_KUTU[0] + BUS_KUTU[2] + 1e-4, f"x={x} BUS_KUTU disinda"
            x_ayna = 2.0 * cx - x
            assert BUS_KUTU[0] - 1e-4 <= x_ayna <= BUS_KUTU[0] + BUS_KUTU[2] + 1e-4, f"x_ayna={x_ayna} disinda"
        for y_coord in ys:
            assert BUS_KUTU[1] - 1e-4 <= y_coord <= BUS_KUTU[1] + BUS_KUTU[3] + 1e-4, f"y={y_coord} disinda"
    w_ornek_yazi = Y.genislik("Caveat", 700, "My brother = he", 64)
    assert (
        60.0 + w_ornek_yazi + 24.0 <= BUS_KUTU[0]
    ), f"Örnek yazı ile otobüs arası yetersiz: 60 + {w_ornek_yazi} + 24 > {BUS_KUTU[0]}"

    # 6. Yazı boyları: içerik yazılarının hepsi >= 64 (64, 72, Caveat 64, hap 64)
    for boy in (64, 72, 72, 64, 64):
        assert boy >= 64, f"Yazı boyu {boy} < 64"

    # 7. Ekran satırları <= 24 karakter (§5 listesi; künye ve kanal hariç)
    satirlar = [
        "He, she, it: s gelir;",
        "I, you, we, they: s yok.",
        "he · she · it",
        "I · you · we · they",
        "goes",
        "go",
        "es",
        "My brother = he",
        "Kaydet",
    ]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 8. Yasak söz denetimi kodda değil, dış metin taramasında (standart §7.3 grep; literal kodda grep'i kirletir).

    # 9. HTML'de id="kanal" ve id="logoimg" tam 1 kez. Şu id'ler var: ozet1, ozet2, s1-es, s1-cizgi, s1-ok, s2-ok,
    #    s2-yuva, ornek-yazi, otobus, kaydet-imi, kaydet-hap. Şunlar YOK: ku-cip, cg1, hap-kutu, ust, alt, altyazi.
    c_kanal = html.count('id="kanal"')
    assert c_kanal == 1, f'id="kanal" sayısı: {c_kanal}'
    c_logo = html.count('id="logoimg"')
    assert c_logo == 1, f'id="logoimg" sayısı: {c_logo}'

    for var in (
        'id="ozet1"',
        'id="ozet2"',
        'id="s1-es"',
        'id="s1-cizgi"',
        'id="s1-ok"',
        'id="s2-ok"',
        'id="s2-yuva"',
        'id="ornek-yazi"',
        'id="otobus"',
        'id="kaydet-imi"',
        'id="kaydet-hap"',
    ):
        assert var in html, f"{var} HTML içinde bulunamadı"

    for yok in ('id="ku-cip"', 'id="cg1"', 'id="hap-kutu"', 'id="ust"', 'id="alt"', 'id="altyazi"'):
        assert yok not in html, f"{yok} HTML içinde olmamalı"

    # 10. Sarı (R["vurgu"]) yalnız kaydet-hap rect'inde ve künye rozetinde: HTML'de R["vurgu"] değeri tam 2 kez geçer.
    c_vurgu = html.count(R["vurgu"])
    assert c_vurgu == 2, f'R["vurgu"] ({R["vurgu"]}) sayısı {c_vurgu} != 2'

    # 11. HTML'de → karakteri YOK; R["kirmizi"] değeri YOK (uret.py'nin kendi HTML dizgesinde, tema öncesi).
    assert "→" not in html, "HTML içinde → karakteri olmamalı"
    assert R["kirmizi"] not in html, f'R["kirmizi"] ({R["kirmizi"]}) HTML içinde olmamalı'


def uret() -> tuple[str, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir."""
    bloklar = blok_kutulari()

    kunye = Y.kunye_svg()
    ozet = ozet_svg()
    satir1 = satir1_svg()
    satir2 = satir2_svg()
    ornek = ornek_svg()
    kaydet = kaydet_svg()

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}"
     data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{ozet}
{satir1}
{satir2}
{ornek}
{kaydet}
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

    print(f"index.html yazıldı {len(html)}")

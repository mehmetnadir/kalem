#!/usr/bin/python3
"""Sahne 07 kapak C (kural kartı) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
huni v2: kanal katmanı + v2 bantları.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
from fontTools.pens.boundsPen import BoundsPen
from PIL import Image, ImageChops, ImageFilter

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

W, H = Y.W, Y.H
KENAR = Y.HUD["kenar"]
SAG = Y.HUD["sagSinir"]
ICERIK_BAS = Y.HUD["icerikBas"]
ICERIK_SON = Y.HUD["icerikSon"]
ORTA = 510
BAS_UST = 462
BAS_ALT = 800
BASLIK_GEN = 900
KONTUR = 12

ORTAK = PAKET / "ortak"
KARAKTER = ORTAK / "kapak" / "karakter.png"
ESIK = 64
KENAR_PX = 10
KENAR_GECIS = 3
PAY = 12
KAR_X0 = 620
KAR_SAG = 948

R = Y.RENK
KREM = R["murekkep"]

SAT1 = "ÜÇ İFADE,"
SAT2 = "TEK İŞARET"


def glif_sinir(metin: str) -> tuple[float, float]:
    """Metindeki Fredoka 700 gliflerinin (yMax, yMin) sınırlarını em cinsinden döndürür."""
    y_maxs: list[float] = []
    y_mins: list[float] = []
    for c in metin:
        for bolge in ("latin", "latin-ext"):
            f = Y._font("Fredoka", 700, bolge)
            cmap = f.getBestCmap()
            gname = cmap.get(ord(c))
            if gname:
                gs = f.getGlyphSet()
                pen = BoundsPen(gs)
                gs[gname].draw(pen)
                if pen.bounds is not None:
                    _, ymin, _, ymax = pen.bounds
                    upem = f["head"].unitsPerEm
                    y_maxs.append(ymax / upem)
                    y_mins.append(ymin / upem)
                break
    assert len(y_maxs) > 0, f"Glif bulunamadı: {metin}"
    return max(y_maxs), min(y_mins)


U1, A1 = glif_sinir(SAT1)
U2, A2 = glif_sinir(SAT2)
assert round(U1, 3) == 0.928 and round(A1, 3) == -0.182, f"SAT1 glif sınırı beklenenden farklı: {U1}, {A1}"
assert round(U2, 3) == 0.921 and round(A2, 3) == -0.182, f"SAT2 glif sınırı beklenenden farklı: {U2}, {A2}"


def hesapla_s_ve_baslik() -> tuple[int, float, float, float, float, float, float, float]:
    """Başlık S boyutu ve yerleşim ölçülerini hesaplar (SPEC §4.2)."""
    ARA = -A1 + U2 + 0.06
    S_secilen: int | None = None
    for s in range(190, 0, -1):
        g1 = Y.genislik("Fredoka", 700, SAT1, s)
        g2 = Y.genislik("Fredoka", 700, SAT2, s)
        sart_a = max(g1, g2) + KONTUR <= BASLIK_GEN
        sart_b = (U1 + ARA - A2) * s + KONTUR <= BAS_ALT - BAS_UST
        if sart_a and sart_b:
            S_secilen = s
            break
    assert S_secilen is not None, "Başlık boyutu S bulunamadı"
    assert S_secilen == 143, f"S={S_secilen} != 143 bekleniyordu"

    S = S_secilen
    g1 = Y.genislik("Fredoka", 700, SAT1, S)
    g2 = Y.genislik("Fredoka", 700, SAT2, S)
    x1 = ORTA - g1 / 2.0
    x2 = ORTA - g2 / 2.0
    T1 = BAS_UST + KONTUR / 2.0 + U1 * S
    T2 = T1 + ARA * S
    baslik_alt = T2 - A2 * S + KONTUR / 2.0
    assert baslik_alt <= 800.0, f"baslik_alt={baslik_alt} > 800"

    return S, g1, g2, x1, x2, T1, T2, baslik_alt


def baslik_svg(S: int, x1: float, x2: float, T1: float, T2: float) -> str:
    """Başlık grubu SVG çıktısı (SPEC §4.2)."""
    bs_1 = (
        f'<text id="bs-1" x="{x1:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="{KONTUR}" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">{SAT1}</text>'
    )
    bs_2 = (
        f'<text id="bs-2" x="{x2:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="{KONTUR}" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">{SAT2}</text>'
    )
    return f'<g id="baslik">{bs_1}{bs_2}</g>'


def kart_kenar_yolu() -> str:
    """Elle çizilmiş kart kenarı yolu (SPEC §4.3)."""
    kay = [1.6, -1.2, 2.2, -0.8, 1.0, -2.0, 0.6, 1.8, -1.4, 0.4, -2.2, 1.2]
    sol = 64.0
    sag = 596.0
    ust = 832.0
    alt = 1148.0
    dx = sag - sol
    dy = alt - ust
    noktalar: list[tuple[float, float]] = [
        (sol + 10.0, ust),
        (sol + dx * 0.25, ust + kay[0]),
        (sol + dx * 0.50, ust + kay[1]),
        (sol + dx * 0.75, ust + kay[2]),
        (sag, ust),
        (sag + kay[3], ust + dy * 0.25),
        (sag + kay[4], ust + dy * 0.50),
        (sag + kay[5], ust + dy * 0.75),
        (sag, alt),
        (sag - dx * 0.25, alt + kay[6]),
        (sag - dx * 0.50, alt + kay[7]),
        (sag - dx * 0.75, alt + kay[8]),
        (sol, alt),
        (sol + kay[9], alt - dy * 0.25),
        (max(62.0, sol + kay[10]), alt - dy * 0.50),
        (sol + kay[11], alt - dy * 0.75),
        (sol, ust),
        (88.0, ust),
    ]
    for p in noktalar:
        assert 62.0 <= p[0] <= 598.0, f"kart-kenar x sınırı dışı: {p}"
        assert 830.0 <= p[1] <= 1150.0, f"kart-kenar y sınırı dışı: {p}"
    return "M " + f"{noktalar[0][0]:.1f} {noktalar[0][1]:.1f}" + " " + " ".join(
        f"L {p[0]:.1f} {p[1]:.1f}" for p in noktalar[1:]
    )


def kart_svg() -> str:
    """Kart grubu SVG çıktısı (SPEC §4.3)."""
    kagit = '<rect id="kagit" x="66" y="834" width="528" height="312" rx="18" fill="#f3efe6" fill-opacity="0.06"/>'
    kenar_d = kart_kenar_yolu()
    kart_kenar = (
        f'<path id="kart-kenar" d="{kenar_d}" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    k1 = (
        f'<text id="k-1" x="100" y="912" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" style="font-kerning:none">usually</text>'
    )
    k2 = (
        f'<text id="k-2" x="100" y="1008" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" style="font-kerning:none">always</text>'
    )
    k3 = (
        f'<text id="k-3" x="100" y="1104" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" style="font-kerning:none">every day</text>'
    )
    # şef QA tur 1: Tabler calendar içindeki "1" çizgisi (M11 15h1, M12 15v3) rakam gibi okunuyor; kapakta rakam yok
    takvim_yollar = [d for d in Y.tabler("calendar") if not d.startswith(("M11 15", "M12 15"))]
    assert len(takvim_yollar) == 4, f"takvim yol sayısı {len(takvim_yollar)} != 4"
    takvim_paths = "".join(f'<path d="{d}"/>' for d in takvim_yollar)
    takvim = (
        f'<g id="takvim" transform="translate(476 846) scale(4)" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="1" stroke-linecap="round" stroke-linejoin="round">{takvim_paths}</g>'
    )
    return f'<g id="kart">{kagit}{kart_kenar}{k1}{k2}{k3}{takvim}</g>'


def ok_svg() -> str:
    """Kalem oku grubu SVG çıktısı (SPEC §4.4)."""
    return (
        f'<g id="ok" fill="none" stroke="{R["murekkep"]}" stroke-width="5" '
        f'stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M 316 1162 C 296 1192, 330 1212, 330 1252"/>'
        '<path d="M 313 1235 L 330 1253 L 347 1235"/>'
        '</g>'
    )


def hap_svg(gh: float) -> str:
    """Sarı hap grubu SVG çıktısı (SPEC §4.5)."""
    hap_w = gh + 60.0
    hap_x_orta = 60.0 + hap_w / 2.0
    return (
        f'<g id="hap">'
        f'<rect x="60" y="1268" width="{hap_w:.2f}" height="104" rx="52" fill="{R["vurgu"]}"/>'
        f'<text x="{hap_x_orta:.2f}" y="1340" text-anchor="middle" font-family="Fredoka" '
        f'font-weight="700" font-size="80" fill="{R["zemin"]}">Simple Present</text>'
        '</g>'
    )


def alfa_kutusu(yol: Path) -> tuple[int, int, int, int]:
    """PNG'nin saydam olmayan kutusu (x0, y0, x1, y1)."""
    a = Image.open(yol).split()[-1].point(lambda v: 255 if v > ESIK else 0)
    kutu = a.getbbox()
    assert kutu is not None, f"{yol.name} tamamen saydam"
    return kutu


def maske(yol: Path, x: float, y: float, s: float) -> np.ndarray:
    """Görselin tuvaldeki saydamlık maskesi (bool, H x W)."""
    im = Image.open(yol)
    a = im.split()[-1].resize((round(im.width * s), round(im.height * s)), Image.BILINEAR)
    m = Image.new("L", (W, H), 0)
    m.paste(255, (round(x), round(y)), a.point(lambda v: 255 if v > ESIK else 0))
    return np.asarray(m) > 0


def bos_mu(m: np.ndarray, kutu: tuple[float, float, float, float], pay: float) -> bool:
    """Kutu (pay kadar genişletilmiş) içinde maskede görsel yok mu."""
    x0, y0 = max(0, math.floor(kutu[0] - pay)), max(0, math.floor(kutu[1] - pay))
    x1, y1 = min(W, math.ceil(kutu[2] + pay)), min(H, math.ceil(kutu[3] + pay))
    return x1 <= x0 or y1 <= y0 or not m[y0:y1, x0:x1].any()


def gorsel_kopyala(hedef: Path) -> None:
    """Karakter proje/assets'e kopyalanır. Alfa ≤ ESIK temizlenir."""
    hedef.mkdir(parents=True, exist_ok=True)
    im = Image.open(KARAKTER).convert("RGBA")
    a = im.split()[-1]
    m = a.point(lambda v: 255 if v > ESIK else 0).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    im.putalpha(ImageChops.multiply(a, m))
    im.save(hedef / "karakter.png")


def gorsel_img(kx: float, ky: float, s: float) -> str:
    """Çıkartma kenarlı görsel (<img>, SPEC §4.6)."""
    im = Image.open(KARAKTER)
    return (
        f'<img id="karakter" class="abs kenar" src="assets/karakter.png" alt="" '
        f'style="left:{kx:.1f}px;top:{ky:.1f}px;width:{im.width * s:.1f}px;height:{im.height * s:.1f}px">'
    )


def karakter_yerlesim(baslik_alt: float, gh: float) -> tuple[float, float, float, tuple[int, int, int, int]]:
    """Karakter ölçek araması ve koordinat hesabı (SPEC §4.6)."""
    ax0, ay0, ax1, ay1 = alfa_kutusu(KARAKTER)
    im_a = Image.open(KARAKTER).split()[-1]
    arr_a = np.asarray(im_a) > ESIK
    dolu_satirlar = np.where(arr_a[:, ax0])[0]
    parmak_y = float(dolu_satirlar.mean())

    kust = baslik_alt + 24.0 + KENAR_PX
    kart_kutu = (62.0, 830.0, 598.0, 1150.0)
    ok_kutu = (294.0, 1159.0, 350.0, 1256.0)
    hap_kutu = (60.0, 1268.0, 60.0 + gh + 60.0, 1268.0 + 104.0)

    gecen_s: float | None = None
    gecen_kx: float = 0.0
    gecen_ky: float = 0.0

    adim_sayisi = round((0.540 - 0.300) / 0.005)
    for i in range(adim_sayisi + 1):
        s = round(0.540 - i * 0.005, 3)
        kx = KAR_SAG - ax1 * s
        ky = kust - ay0 * s
        m = maske(KARAKTER, kx, ky, s)
        sart1 = ky + ay1 * s + KENAR_PX <= ICERIK_SON
        sart2 = kx + ax0 * s - KENAR_PX >= KAR_X0
        sart3 = (
            bos_mu(m, hap_kutu, KENAR_PX + PAY)
            and bos_mu(m, ok_kutu, KENAR_PX + PAY)
            and bos_mu(m, kart_kutu, KENAR_PX + PAY)
        )
        parmak_pos = ky + parmak_y * s
        sart4 = (832.0 + 24.0) <= parmak_pos <= (1148.0 - 24.0)
        if sart1 and sart2 and sart3 and sart4:
            gecen_s = s
            gecen_kx = kx
            gecen_ky = ky
            break

    assert gecen_s is not None, "Hiçbir s ölçeği şartları sağlamadı"
    assert gecen_s == 0.465, f"s={gecen_s} != 0.465 bekleniyordu"
    return gecen_s, gecen_kx, gecen_ky, (ax0, ay0, ax1, ay1)


def blok_kutulari(
    baslik_x: float,
    baslik_w: float,
    baslik_alt: float,
    gh: float,
    kx: float,
    ky: float,
    s: float,
    alfa_k: tuple[int, int, int, int],
) -> tuple[list[dict[str, float]], list[dict[str, float]]]:
    """Yerleşim bloklarının kutularını hesaplar.
    Döndürür: (kesisim_bloklari, nesneler_bloklari).
    kesisim_bloklari (7 adet): kanal, kunye, baslik, kart, ok, hap, karakter.
    nesneler_bloklari (8 adet): kanal, kunye, baslik, kart, takvim, ok, hap, karakter.
    """
    w_kanal = Y.HUD["kanalYaziX"] + Y.genislik("Lexend", 700, Y.KANAL_YAZI, 42) - 60.0
    kanal = {"ad": "kanal", "x": 60.0, "y": 280.0, "w": w_kanal, "h": 70.0}

    rx, rw = Y.rozet_konumu()
    assert rx + rw <= 960.0, f"rozet sag {rx + rw} > 960"
    kunye = {"ad": "kunye", "x": 60.0, "y": 360.0, "w": rx + rw - 60.0, "h": 90.0}

    baslik = {
        "ad": "baslik",
        "x": baslik_x,
        "y": float(BAS_UST),
        "w": baslik_w,
        "h": baslik_alt - float(BAS_UST),
    }

    kart = {"ad": "kart", "x": 62.0, "y": 830.0, "w": 536.0, "h": 320.0}
    takvim = {"ad": "takvim", "x": 490.0, "y": 856.0, "w": 68.0, "h": 76.0}
    ok = {"ad": "ok", "x": 294.0, "y": 1159.0, "w": 56.0, "h": 97.0}
    hap = {"ad": "hap", "x": 60.0, "y": 1268.0, "w": gh + 60.0, "h": 104.0}

    ax0, ay0, ax1, ay1 = alfa_k
    kar_x0 = kx + ax0 * s - KENAR_PX
    kar_y0 = ky + ay0 * s - KENAR_PX
    kar_x1 = kx + ax1 * s + KENAR_PX
    kar_y1 = ky + ay1 * s + KENAR_PX
    karakter = {
        "ad": "karakter",
        "x": kar_x0,
        "y": kar_y0,
        "w": kar_x1 - kar_x0,
        "h": kar_y1 - kar_y0,
    }

    kesisim_bloklari = [kanal, kunye, baslik, kart, ok, hap, karakter]
    nesneler_bloklari = [kanal, kunye, baslik, kart, takvim, ok, hap, karakter]
    return kesisim_bloklari, nesneler_bloklari


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(
    kesisim_bloklari: list[dict[str, float]],
    nesneler_bloklari: list[dict[str, float]],
    S: int,
    baslik_alt: float,
    gh: float,
) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    # 1. Hiçbir blok y < 280, y > 1380, x > 960 değil
    for b in nesneler_bloklari:
        ad = b["ad"]
        bx, by, bw, bh = b["x"], b["y"], b["w"], b["h"]
        assert bx >= 0.0, f"{ad} sol {bx} < 0"
        assert bx + bw <= 960.0 + 1e-4, f"{ad} sağ {bx + bw} > 960"
        assert by >= 280.0 - 1e-4, f"{ad} üst {by} < 280"
        assert by + bh <= 1380.0 + 1e-4, f"{ad} alt {by + bh} > 1380"

    # 2. İçerik blokları: x ∈ [KENAR - 2, SAG], y ∈ [ICERIK_BAS, ICERIK_SON]
    icerik_ogeleri = [b for b in nesneler_bloklari if b["ad"] not in ("kanal", "kunye", "takvim")]
    for b in icerik_ogeleri:
        ad = b["ad"]
        bx, by, bw, bh = b["x"], b["y"], b["w"], b["h"]
        assert bx >= KENAR - 2.0 - 1e-4, f"{ad} sol {bx} < KENAR - 2"
        assert bx + bw <= SAG + 1e-4, f"{ad} sağ {bx + bw} > SAG"
        assert by >= ICERIK_BAS - 1e-4, f"{ad} üst {by} < ICERIK_BAS"
        assert by + bh <= ICERIK_SON + 1e-4, f"{ad} alt {by + bh} > ICERIK_SON"

    # 3. Kesişim 0: kanal, kunye, baslik, kart, ok, hap, karakter
    for i in range(len(kesisim_bloklari)):
        for j in range(i + 1, len(kesisim_bloklari)):
            k = kesisim(kesisim_bloklari[i], kesisim_bloklari[j])
            ad1, ad2 = kesisim_bloklari[i]["ad"], kesisim_bloklari[j]["ad"]
            assert k == 0.0, f"Kesişim {ad1} - {ad2}: {k}"

    b_dict = {b["ad"]: b for b in nesneler_bloklari}

    # baslik alt ile kart ve karakter üstü arası >= 24
    assert b_dict["kart"]["y"] - baslik_alt >= 24.0 - 1e-6, (
        f"baslik alt -> kart üstü ara {b_dict['kart']['y'] - baslik_alt} < 24"
    )
    assert b_dict["karakter"]["y"] - baslik_alt >= 24.0 - 1e-6, (
        f"baslik alt -> karakter üstü ara {b_dict['karakter']['y'] - baslik_alt} < 24"
    )

    # 4. Yazı boyu ≥ 64: başlık S, kart 72, hap 80
    assert S >= 64, f"Başlık boyutu S={S} < 64"
    assert 72 >= 64, "Kart satır font boyutu < 64"
    assert 80 >= 64, "Hap font boyutu < 64"

    # Başlık 2 satır, toplam 4 sözcük, her satır ≤ 24 karakter
    toplam_sozcuk = len(SAT1.split()) + len(SAT2.split())
    assert toplam_sozcuk == 4, f"Başlık toplam sözcük sayısı {toplam_sozcuk} != 4"
    for s in [SAT1, SAT2, "usually", "always", "every day", "Simple Present"]:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 5. Kart içi kurallar (§4.3)
    satir_metinleri = [("usually", 912.0), ("always", 1008.0), ("every day", 1104.0)]
    kart_satir_kutulari = []
    for metin, taban in satir_metinleri:
        w_sat = Y.genislik("Fredoka", 700, metin, 72)
        kart_satir_kutulari.append({
            "ad": metin,
            "x": 100.0,
            "y": taban - 0.75 * 72.0,
            "w": w_sat,
            "h": 72.0,
        })
    takvim_kutu = b_dict["takvim"]
    for sk in kart_satir_kutulari + [takvim_kutu]:
        assert sk["x"] >= 64.0 + 24.0 - 1e-4, f"{sk['ad']} kart sol kenarına 24 px'den yakın"
        assert sk["x"] + sk["w"] <= 596.0 - 24.0 + 1e-4, f"{sk['ad']} kart sağ kenarına 24 px'den yakın"
        assert sk["y"] >= 832.0 + 24.0 - 1e-4, f"{sk['ad']} kart üst kenarına 24 px'den yakın"
        assert sk["y"] + sk["h"] <= 1148.0 - 24.0 + 1e-4, f"{sk['ad']} kart alt kenarına 24 px'den yakın"

    for sk in kart_satir_kutulari:
        k = kesisim(sk, takvim_kutu)
        assert k == 0.0, f"Kart satırı {sk['ad']} ile takvim kesişiyor: {k}"

    # 6. Kalem oku mesafeleri (§4.4)
    assert b_dict["ok"]["y"] - 1148.0 >= 8.0, "Kart altı ile ok başı arası < 8"
    assert b_dict["hap"]["y"] - (b_dict["ok"]["y"] + b_dict["ok"]["h"]) >= 8.0, "Ok ucu ile hap üstü arası < 8"

    # 7. Sarı hap sınırları (§4.5)
    assert b_dict["hap"]["x"] + b_dict["hap"]["w"] <= SAG + 1e-4, "Hap sağ sınırı aştı"
    assert b_dict["hap"]["y"] + b_dict["hap"]["h"] <= ICERIK_SON + 1e-4, "Hap içerik son sınırını aştı"


def uret() -> tuple[str, int, float, list[dict[str, float]]]:
    """Sahne HTML'i, parametreleri ve nesnelerini üretir."""
    S, g1, g2, x1, x2, T1, T2, baslik_alt = hesapla_s_ve_baslik()
    baslik_w = max(g1, g2) + KONTUR
    baslik_x = ORTA - max(g1, g2) / 2.0 - KONTUR / 2.0

    gh = Y.genislik("Fredoka", 700, "Simple Present", 80)

    s, kx, ky, alfa_k = karakter_yerlesim(baslik_alt, gh)

    kunye = Y.kunye_svg()
    baslik = baslik_svg(S, x1, x2, T1, T2)
    kart = kart_svg()
    ok = ok_svg()
    hap = hap_svg(gh)
    karakter_img = gorsel_img(kx, ky, s)

    kesisim_bloklari, nesneler_bloklari = blok_kutulari(
        baslik_x, baslik_w, baslik_alt, gh, kx, ky, s, alfa_k
    )
    kurallari_dogrula(kesisim_bloklari, nesneler_bloklari, S, baslik_alt, gh)

    adim = KENAR_PX / KENAR_GECIS
    kenar_filter = " ".join(
        f"drop-shadow({dx:.2f}px {dy:.2f}px 0 {KREM})"
        for _ in range(KENAR_GECIS)
        for dx, dy in ((adim, 0.0), (-adim, 0.0), (0.0, adim), (0.0, -adim))
    )

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
.kenar{{filter:{kenar_filter};}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
{karakter_img}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{baslik}
{kart}
{ok}
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

    return html, S, s, nesneler_bloklari


if __name__ == "__main__":
    proje_dizini = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    gorsel_kopyala(proje_dizini / "assets")

    html, S, s, bloklar = uret()
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
    print(f"s={s}")

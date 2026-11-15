"""02-04-ydt-temel-s3 sahne 08 Kaydet (HyperFrames, DİKEY 1080x1920, huni v2).

Kural özeti kartı (Tarife -> leaves, / plan -> am going.), Gönder ve Kaydet satırları, altyazı üretimi.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(
    s for s in json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))["sahneler"]
    if s["klasor"] == AD.name
)
T_BAS: float = float(SAH["t_bas"])  # 15.99
KARE: int = int(SAH["kare"])        # 172
SURE: float = round(KARE / 30, 4)   # 5.7333
ICERIK: float = round(float(SAH["icerik_kare"]) / 30, 4)  # 5.3333
ALT_SON: float = round(float(SAH["t_son"]) - T_BAS, 3)    # 5.34

SOZ: list[dict[str, Any]] = [
    w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 4
]
ALT: list[dict[str, Any]] = [
    p for p in json.loads((PAKET / "ortak" / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
    if p.get("cumle") == 4
]


def yerel(t: float) -> float:
    """Küresel saniyeyi sahne yerel saniyesine çevirir."""
    return round(t - T_BAS, 3)


def T(i: int, bas: str = "") -> float:
    """Cümle 4, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = str(w["sozcuk"])
        assert val.lower().startswith(bas.lower()), f"sözcük {i}: {val!r}, beklenen {bas!r}"
    return float(w["t0"])


def E(i: int, bas: str = "") -> float:
    """Cümle 4, i. sözcüğün t1'i (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = str(w["sozcuk"])
        assert val.lower().startswith(bas.lower()), f"sözcük {i}: {val!r}, beklenen {bas!r}"
    return float(w["t1"])


# Sözcük sıralaması doğrulaması
BEKLENEN_SOZLER: list[tuple[int, str]] = [
    (0, "Bu"),
    (1, "üç"),
    (2, "farktan"),
    (3, "yalnız"),
    (4, "biri"),
    (5, "Bir"),
    (6, "arkadaşına"),
    (7, "gönder"),
    (8, "o"),
    (9, "da"),
    (10, "karıştırıyor"),
]
assert len(SOZ) == 11, f"Cümle 4 için 11 sözcük bekleniyor, {len(SOZ)} bulundu"
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)
assert len(ALT) == 2, f"Cümle 4 için 2 altyazı parçası bekleniyor, {len(ALT)} bulundu"


def _kutu(x: float, y: float, w: float, h: float, ince: bool = False) -> dict[str, Any]:
    return {"n": [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], "kapali": True, "ince": ince}


TREN: list[dict[str, Any]] = [
    _kutu(200.0, 55.0, 170.0, 75.0),
    _kutu(200.0, 10.0, 75.0, 45.0),
    _kutu(320.0, 22.0, 26.0, 33.0, True),
    {"n": [(370.0, 95.0), (398.0, 130.0), (370.0, 130.0)]},
    _kutu(0.0, 45.0, 175.0, 85.0),
    {"n": [(175.0, 112.0), (200.0, 112.0)], "ince": True},
    _kutu(20.0, 60.0, 50.0, 30.0, True),
    _kutu(100.0, 60.0, 50.0, 30.0, True),
    _kutu(215.0, 20.0, 42.0, 25.0, True),
    {"daire": (40.0, 138.0, 17.0)},
    {"daire": (135.0, 138.0, 17.0)},
    {"daire": (240.0, 138.0, 17.0)},
    {"daire": (335.0, 138.0, 17.0)},
    {"n": [(-10.0, 158.0), (420.0, 158.0)], "ince": True},
]


def _bilet() -> list[dict[str, Any]]:
    def yay(x0: float, yon: float) -> list[tuple[float, float]]:
        return [
            (
                x0 - yon * 22.0 * math.cos(-math.pi / 2.0 + i / 12.0 * math.pi),
                yon * 22.0 * math.sin(-math.pi / 2.0 + i / 12.0 * math.pi),
            )
            for i in range(13)
        ]

    kenar = (
        [(-180.0, -70.0), (180.0, -70.0), (180.0, -22.0)]
        + yay(180.0, 1.0)
        + [(180.0, 70.0), (-180.0, 70.0), (-180.0, 22.0)]
        + yay(-180.0, -1.0)
    )
    p: list[dict[str, Any]] = [{"n": kenar + [(-180.0, -70.0)]}]
    p += [{"n": [(100.0, -58.0 + i * 20.0), (100.0, -47.0 + i * 20.0)], "ince": True} for i in range(6)]
    p += [{"n": [(-150.0, y), (x1, y)], "ince": True} for y, x1 in ((-30.0, 60.0), (0.0, 30.0), (30.0, 70.0))]
    return p


BILET: list[dict[str, Any]] = _bilet()


def _kutusu(parcalar: list[dict[str, Any]]) -> tuple[float, float, float, float]:
    xs: list[float] = []
    ys: list[float] = []
    for p in parcalar:
        if "daire" in p:
            x, y, r = p["daire"]
            xs += [float(x - r), float(x + r)]
            ys += [float(y - r), float(y + r)]
        else:
            xs += [float(q[0]) for q in p["n"]]
            ys += [float(q[1]) for q in p["n"]]
    return min(xs), min(ys), max(xs), max(ys)


def _daire_yolu(cx: float, cy: float, r: float) -> str:
    k = 0.5523 * r
    return (
        "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f "
        "C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
        % (
            cx + r, cy, cx + r, cy + k, cx + k, cy + r, cx, cy + r,
            cx - k, cy + r, cx - r, cy + k, cx - r, cy,
            cx - r, cy - k, cx - k, cy - r, cx, cy - r,
            cx + k, cy - r, cx + r, cy - k, cx + r, cy,
        )
    )


def ikon_yollari(
    parcalar: list[dict[str, Any]], mx: float, my: float, en: float, boy: float
) -> list[tuple[str, float, bool]]:
    """Izgara parçalarını en x boy kutusuna (merkez mx, my) sığdırır. Döner: [(d, uzunluk, ince)]."""
    gx0, gy0, gx1, gy1 = _kutusu(parcalar)
    sc = min(boy / (gy1 - gy0), en / (gx1 - gx0))
    gmx, gmy = (gx0 + gx1) / 2.0, (gy0 + gy1) / 2.0

    def P(q: tuple[float, float]) -> tuple[float, float]:
        return (mx + (q[0] - gmx) * sc, my + (q[1] - gmy) * sc)

    out: list[tuple[str, float, bool]] = []
    for p in parcalar:
        if "daire" in p:
            x, y, r = p["daire"]
            c = P((x, y))
            out.append((_daire_yolu(c[0], c[1], r * sc), 2.0 * math.pi * r * sc, p.get("ince", False)))
            continue
        q = [P(v) for v in p["n"]]
        if p.get("kapali"):
            q = q + [q[0]]
        uz = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(q, q[1:]))
        if p.get("egri") and len(q) >= 3:
            d = "M%.1f %.1f" % q[0]
            for i in range(len(q) - 1):
                p0, p1, p2 = q[max(i - 1, 0)], q[i], q[i + 1]
                p3 = q[min(i + 2, len(q) - 1)]
                c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
                c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
                d += " C%.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p2)
            uz *= 1.05
        else:
            d = "M%.1f %.1f " % q[0] + " ".join("L%.1f %.1f" % v for v in q[1:])
        out.append((d, uz, p.get("ince", False)))
    return out


def uret() -> tuple[str, dict[str, Any]]:
    """Sahne 08 index.html ve zamanlar.json verisini üretir."""
    R = Y.RENK
    assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu"}

    # 1. Kural satırları ve metin uzunlukları (§8 kural 1)
    satir1_metin = "Tarife \u2192 leaves,"
    satir2_metin = "plan \u2192 am going."
    gonder_metin = "Arkadaşına gönder"
    kaydet_metin = "Kaydet"
    assert len(satir1_metin) <= 24, f"Satır 1 24 karakterden uzun: {len(satir1_metin)}"
    assert len(satir2_metin) <= 24, f"Satır 2 24 karakterden uzun: {len(satir2_metin)}"
    assert len(gonder_metin) <= 24, f"Gönder satırı 24 karakterden uzun: {len(gonder_metin)}"
    assert len(kaydet_metin) <= 24, f"Kaydet satırı 24 karakterden uzun: {len(kaydet_metin)}"

    # 2. Kart yerleşimi ve ölçüleri (§5)
    T1 = 705.0
    T2 = 801.0
    TX = 242.0
    dx_ok = 18.0 * math.cos(0.5)
    dy_ok = 18.0 * math.sin(0.5)

    # Tren ikonu
    tren_my = T1 - 0.30 * 72.0
    tren_yollar = ikon_yollari(TREN, 154.0, tren_my, 136.0, 64.0)
    tren_paths: list[str] = []
    for idx, (d, _, ince) in enumerate(tren_yollar):
        if idx == len(tren_yollar) - 1:
            renk = R["ikincil"]
            sw = 3
        elif ince:
            renk = R["murekkep"]
            sw = 3
        else:
            renk = R["murekkep"]
            sw = 4
        tren_paths.append(
            f'<path id="tren_{idx}" d="{d}" stroke="{renk}" stroke-width="{sw}" style="opacity:0"/>'
        )
    tren_svg = (
        f'<g id="kart-tren" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        f'{"".join(tren_paths)}</g>'
    )

    # Bilet ikonu
    bilet_my = T2 - 0.30 * 72.0
    bilet_yollar = ikon_yollari(BILET, 154.0, bilet_my, 132.0, 60.0)
    bilet_paths: list[str] = []
    for idx, (d, _, ince) in enumerate(bilet_yollar):
        if ince:
            renk = R["ikincil"]
            sw = 3
        else:
            renk = R["murekkep"]
            sw = 4
        bilet_paths.append(
            f'<path id="bilet_{idx}" d="{d}" stroke="{renk}" stroke-width="{sw}" style="opacity:0"/>'
        )
    bilet_svg = (
        f'<g id="kart-bilet" transform="rotate(-3 154 {bilet_my:.1f})" '
        f'fill="none" stroke-linecap="round" stroke-linejoin="round">'
        f'{"".join(bilet_paths)}</g>'
    )

    # Satır 1
    w_sol1 = Y.genislik("Fredoka", 700, "Tarife", 72)
    x_ok0_1 = TX + w_sol1 + 0.22 * 72.0
    x_ok1_1 = x_ok0_1 + 0.70 * 72.0
    LX = x_ok1_1 + 0.22 * 72.0 + 14.0
    w_leaves = Y.genislik("Fredoka", 700, "leaves", 72)
    x_virgul = LX + w_leaves + 16.0
    w_virgul = Y.genislik("Fredoka", 700, ",", 72)
    s1_sag_uc = x_virgul + w_virgul
    assert s1_sag_uc <= 934.0, f"Satır 1 sağ uç 934'ü aştı: {s1_sag_uc:.1f}"

    y_ok1 = T1 - 0.28 * 72.0
    d_ok1 = (
        f"M{x_ok0_1:.1f} {y_ok1:.1f} L{x_ok1_1:.1f} {y_ok1:.1f} "
        f"M{x_ok1_1 - dx_ok:.1f} {y_ok1 - dy_ok:.1f} L{x_ok1_1:.1f} {y_ok1:.1f} "
        f"L{x_ok1_1 - dx_ok:.1f} {y_ok1 + dy_ok:.1f}"
    )
    s1_ok = (
        f'<path id="kart-s1-ok" class="ok" d="{d_ok1}" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="6" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>'
    )

    leaves_hap = (
        f'<g id="leaves-hap">'
        f'<rect x="{LX - 14.0:.1f}" y="{T1 - 0.80 * 72.0:.1f}" width="{w_leaves + 28.0:.1f}" height="72" rx="36" '
        f'fill="{R["vurgu"]}"/>'
        f'<text x="{LX:.1f}" y="{T1:.1f}" font-family="Fredoka" font-weight="700" font-size="72" '
        f'fill="{R["zemin"]}" xml:space="preserve">leaves</text>'
        f'</g>'
    )
    s1_svg = (
        f'<g id="s1" style="opacity:0">'
        f'<text id="kart-s1-sol" x="{TX:.1f}" y="{T1:.1f}" font-family="Fredoka" font-weight="700" font-size="72" '
        f'fill="{R["murekkep"]}" xml:space="preserve">Tarife</text>'
        f'<text id="leaves-yazi" x="{LX:.1f}" y="{T1:.1f}" font-family="Fredoka" font-weight="700" font-size="72" '
        f'fill="{R["murekkep"]}" xml:space="preserve" style="opacity:0">leaves,</text>'
        f'{leaves_hap}'
        f'<text id="kart-s1-virgul" x="{x_virgul:.1f}" y="{T1:.1f}" font-family="Fredoka" font-weight="700" '
        f'font-size="72" fill="{R["murekkep"]}" xml:space="preserve">,</text>'
        f'</g>'
    )

    leaves_alti_d = (
        f"M{LX - 4.0:.1f} {T1 + 12:.1f} Q{LX + w_leaves / 2.0:.1f} {T1 + 15:.1f} "
        f"{LX + w_leaves + 4.0:.1f} {T1 + 11:.1f}"
    )
    leaves_alti = (
        f'<path id="leaves-alti" d="{leaves_alti_d}" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="6" stroke-linecap="round" style="opacity:0"/>'
    )

    # Satır 2
    w_sol2 = Y.genislik("Fredoka", 700, "plan", 72)
    x_ok0_2 = TX + w_sol2 + 0.22 * 72.0
    x_ok1_2 = x_ok0_2 + 0.70 * 72.0
    x_sag2 = x_ok1_2 + 0.22 * 72.0
    w_sag2 = Y.genislik("Fredoka", 700, "am going.", 72)
    s2_sag_uc = x_sag2 + w_sag2
    assert s2_sag_uc <= 934.0, f"Satır 2 sağ uç 934'ü aştı: {s2_sag_uc:.1f}"

    y_ok2 = T2 - 0.28 * 72.0
    d_ok2 = (
        f"M{x_ok0_2:.1f} {y_ok2:.1f} L{x_ok1_2:.1f} {y_ok2:.1f} "
        f"M{x_ok1_2 - dx_ok:.1f} {y_ok2 - dy_ok:.1f} L{x_ok1_2:.1f} {y_ok2:.1f} "
        f"L{x_ok1_2 - dx_ok:.1f} {y_ok2 + dy_ok:.1f}"
    )
    s2_ok = (
        f'<path id="kart-s2-ok" class="ok" d="{d_ok2}" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="6" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>'
    )
    s2_svg = (
        f'<g id="s2" style="opacity:0">'
        f'<text id="kart-s2-sol" x="{TX:.1f}" y="{T2:.1f}" font-family="Fredoka" font-weight="700" font-size="72" '
        f'fill="{R["murekkep"]}" xml:space="preserve">plan</text>'
        f'<text id="kart-s2-sag" x="{x_sag2:.1f}" y="{T2:.1f}" font-family="Fredoka" font-weight="700" font-size="72" '
        f'fill="{R["murekkep"]}" xml:space="preserve">am going.</text>'
        f'</g>'
    )

    # Ok mesafesi denetimi (§8 kural 4)
    assert x_ok0_1 - (TX + w_sol1) >= 10.0, "Satır 1 ok sol sözcüğe çok yakın"
    assert (LX - 14.0) - x_ok1_1 >= 10.0, "Satır 1 ok sağ hapa çok yakın"
    assert x_ok0_2 - (TX + w_sol2) >= 10.0, "Satır 2 ok sol sözcüğe çok yakın"
    assert x_sag2 - x_ok1_2 >= 10.0, "Satır 2 ok sağ sözcüğe çok yakın"

    # İkon kutusu sınır denetimi (§8 kural 3)
    tren_kutusu = (154.0 - 68.0, tren_my - 32.0, 154.0 + 68.0, tren_my + 32.0)
    assert 86.0 <= tren_kutusu[0] and tren_kutusu[2] <= TX - 16.0, "Tren x sınır dışı"
    assert 566.0 <= tren_kutusu[1] and tren_kutusu[3] <= 894.0, "Tren y sınır dışı"
    bilet_kutusu = (154.0 - 66.0, bilet_my - 30.0, 154.0 + 66.0, bilet_my + 30.0)
    assert 86.0 <= bilet_kutusu[0] and bilet_kutusu[2] <= TX - 16.0, "Bilet x sınır dışı"
    assert 566.0 <= bilet_kutusu[1] and bilet_kutusu[3] <= 894.0, "Bilet y sınır dışı"

    # Kart çerçevesi yolu (§5)
    kenar_d = (
        "M100 562 H930 A28 28 0 0 1 958 590 V870 A28 28 0 0 1 930 898 H90 A28 28 0 0 1 62 870 "
        "V590 A28 28 0 0 1 90 562 L114 562"
    )

    # 3. Gönder ve Kaydet satırları (§7)
    w_arkadasina_bosluk = Y.genislik("Fredoka", 700, "Arkadaşına ", 80)
    x_gonder_yazi2 = 156.0 + w_arkadasina_bosluk
    w_gonder_son = Y.genislik("Fredoka", 700, "gönder", 80)
    gonder_sag_uc = x_gonder_yazi2 + w_gonder_son
    assert gonder_sag_uc <= 960.0, f"Gönder sağ ucu 960'ı aştı: {gonder_sag_uc:.1f}"

    gonder_svg = (
        f'<g id="gonder">'
        f'<g id="gonder-ikon" transform="translate(48 962) scale(4)" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
        f'<path id="gonder-dolgu" d="M21 3l-6.5 18a.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a.55 .55 0 0 1 0 -1l18 -6.5" '
        f'fill="{R["vurgu"]}" fill-opacity="0" style="opacity:0"/>'
        f'<path id="gonder-cizgi" d="M10 14l11 -11" style="opacity:0"/>'
        f'</g>'
        f'<text id="gonder-yazi1" x="156" y="1038" font-family="Fredoka" font-weight="700" font-size="80" '
        f'fill="{R["murekkep"]}" style="opacity:0">Arkadaşına</text>'
        f'<text id="gonder-yazi2" x="{x_gonder_yazi2:.1f}" y="1038" font-family="Fredoka" font-weight="700" '
        f'font-size="80" fill="{R["murekkep"]}" style="opacity:0">gönder</text>'
        f'</g>'
    )

    w_kaydet = Y.genislik("Fredoka", 700, "Kaydet", 64)
    kaydet_sag_uc = 156.0 + w_kaydet
    assert kaydet_sag_uc <= 960.0, f"Kaydet sağ ucu 960'ı aştı: {kaydet_sag_uc:.1f}"

    kaydet_svg = (
        f'<g id="kaydet">'
        f'<g id="kaydet-ikon" transform="translate(57.6 1081.6) scale(3.2)" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
        f'<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z" style="opacity:0"/>'
        f'</g>'
        f'<text id="kaydet-yazi" x="156" y="1142" font-family="Fredoka" font-weight="700" font-size="64" '
        f'fill="{R["murekkep"]}" style="opacity:0">Kaydet</text>'
        f'</g>'
    )

    # 4. Zamanlamalar (§4)
    t_kart_ciz = yerel(T(0, "Bu"))            # 0.55
    t_satir1 = round(yerel(T(0)) + 0.06, 3)    # 0.61
    t_satir2 = round(yerel(T(0)) + 0.16, 3)    # 0.71
    t_gonder_ciz = yerel(T(5, "Bir"))          # 2.78
    t_imi_ciz = round(yerel(T(5)) + 0.10, 3)   # 2.88
    t_arkadasina = yerel(T(6, "arkadaşına"))   # 3.02
    t_gonder_yaz = yerel(T(7, "gönder"))       # 3.54
    t_sari_gecis = yerel(T(7, "gönder"))       # 3.54
    t_kuyruk = round(ICERIK, 3)                # 5.333

    assert max(t_sari_gecis + 0.30, t_gonder_yaz + 0.25) <= ICERIK, "Son tween bitişi ICERIK sonrasına sarktı"

    zamanlar: dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "kart_ciz": [t_kart_ciz, 0.40],
        "satir1": [t_satir1, 0.30],
        "satir2": [t_satir2, 0.30],
        "gonder_ciz": [t_gonder_ciz, 0.40],
        "imi_ciz": [t_imi_ciz, 0.40],
        "arkadasina": [t_arkadasina, 0.25],
        "gonder_yaz": [t_gonder_yaz, 0.25],
        "sari_gecis": [t_sari_gecis, 0.30],
        "kuyruk_durgun": [t_kuyruk, round(SURE - t_kuyruk, 3)],
        "olaylar": [
            [t_kart_ciz, "cizgi", 0.5],
            [t_gonder_ciz, "cizgi", 0.5],
            [t_gonder_yaz, "tik", 0.5],
        ],
        "olay_listesi": [
            {
                "olay": "kart_ciz",
                "kare": round(t_kart_ciz * 30),
                "yerel": t_kart_ciz,
                "kuresel": T(0, "Bu"),
                "sozcuk": "Bu,",
            },
            {
                "olay": "satir1",
                "kare": round(t_satir1 * 30),
                "yerel": t_satir1,
                "kuresel": round(T(0) + 0.06, 3),
                "sozcuk": "Bu,",
            },
            {
                "olay": "satir2",
                "kare": round(t_satir2 * 30),
                "yerel": t_satir2,
                "kuresel": round(T(0) + 0.16, 3),
                "sozcuk": "Bu,",
            },
            {
                "olay": "gonder_ciz",
                "kare": round(t_gonder_ciz * 30),
                "yerel": t_gonder_ciz,
                "kuresel": T(5, "Bir"),
                "sozcuk": "Bir",
            },
            {
                "olay": "imi_ciz",
                "kare": round(t_imi_ciz * 30),
                "yerel": t_imi_ciz,
                "kuresel": round(T(5) + 0.10, 3),
                "sozcuk": "Bir",
            },
            {
                "olay": "arkadasina",
                "kare": round(t_arkadasina * 30),
                "yerel": t_arkadasina,
                "kuresel": T(6, "arkadaşına"),
                "sozcuk": "arkadaşına",
            },
            {
                "olay": "gonder_yaz",
                "kare": round(t_gonder_yaz * 30),
                "yerel": t_gonder_yaz,
                "kuresel": T(7, "gönder"),
                "sozcuk": "gönder;",
            },
            {
                "olay": "sari_gecis",
                "kare": round(t_sari_gecis * 30),
                "yerel": t_sari_gecis,
                "kuresel": T(7, "gönder"),
                "sozcuk": "gönder;",
            },
            {
                "olay": "kuyruk_durgun",
                "kare": round(t_kuyruk * 30),
                "yerel": t_kuyruk,
                "kuresel": round(T_BAS + t_kuyruk, 3),
                "sozcuk": "sahne sonu",
            },
        ],
    }

    alt_svg, alt_zaman, karaoke_zaman = Y.altyazi_svg(T_BAS, ALT_SON, ALT)
    kunye_svg = Y.kunye_svg()

    veri = {
        "Z": {
            "kart_ciz": zamanlar["kart_ciz"],
            "satir1": zamanlar["satir1"],
            "satir2": zamanlar["satir2"],
            "gonder_ciz": zamanlar["gonder_ciz"],
            "imi_ciz": zamanlar["imi_ciz"],
            "arkadasina": zamanlar["arkadasina"],
            "gonder_yaz": zamanlar["gonder_yaz"],
            "sari_gecis": zamanlar["sari_gecis"],
            "kuyruk_durgun": zamanlar["kuyruk_durgun"],
        },
        "tren_sayisi": len(tren_yollar),
        "bilet_sayisi": len(bilet_yollar),
        "alt": alt_zaman,
        "karaoke": karaoke_zaman,
    }

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
#sahne text{{font-kerning:none;}}
#root #gonder-dolgu{{fill:var(--vurguDolgu,#f2a93b);}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{SURE}"
 data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">

<!-- Kart grubu -->
<g id="kart">
<path id="kart-kenar" d="{kenar_d}" fill="none" stroke="{R["murekkep"]}" stroke-width="4"
 stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>
{tren_svg}
{bilet_svg}
{s1_svg}
{s1_ok}
{leaves_alti}
{s2_svg}
{s2_ok}
</g>

<!-- Gönder grubu -->
{gonder_svg}

<!-- Kaydet grubu -->
{kaydet_svg}

<!-- Künye ve kanal katmanı -->
{kunye_svg}

<!-- Altyazı -->
<g id="altyazi">{alt_svg}</g>
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var V = {json.dumps(veri)};
  var Z = V.Z;
  var $ = function (s) {{ return document.querySelector(s); }};
  var tl = gsap.timeline({{ paused: true }});

  function ac(o) {{ o.immediateRender = false; return o; }}

  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});

  V.karaoke.forEach(function (k) {{
    var id = "#" + k[0], ac_t = k[1], kapat_t = k[2], uz = k[3];
    var el = $(id);
    if (el) {{
      el.style.strokeDasharray = uz + " " + (uz + 2);
      el.style.strokeDashoffset = uz;
      tl.set(id, ac({{ opacity: 1 }}), ac_t);
      tl.fromTo(id, {{ strokeDashoffset: uz }},
        {{ strokeDashoffset: 0, duration: 0.15, ease: "power2.out", immediateRender: false }}, ac_t);
      tl.set(id, ac({{ opacity: 0 }}), kapat_t);
    }}
  }});

  function darbe(id, t0, dur, ease) {{
    var el = $(id);
    if (!el) return;
    var L = el.getTotalLength();
    el.style.strokeDasharray = L + " " + (L + 2);
    el.style.strokeDashoffset = L;
    tl.set(el, ac({{ opacity: 1 }}), t0);
    tl.fromTo(el, {{ strokeDashoffset: L }},
      {{ strokeDashoffset: 0, duration: dur, ease: ease || "sine.inOut", immediateRender: false }}, t0);
  }}

  // 1. kart_ciz
  darbe("#kart-kenar", Z.kart_ciz[0], 0.40, "sine.inOut");

  // 2. satir1
  for (var i = 0; i < V.tren_sayisi; i++) {{
    darbe("#tren_" + i, Z.satir1[0], 0.30, "power1.out");
  }}
  tl.fromTo("#s1", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.25, ease: "power2.out", immediateRender: false }}, Z.satir1[0]);
  darbe("#kart-s1-ok", Z.satir1[0] + 0.05, 0.20, "power1.out");

  // 3. satir2
  for (var j = 0; j < V.bilet_sayisi; j++) {{
    darbe("#bilet_" + j, Z.satir2[0], 0.30, "power1.out");
  }}
  tl.fromTo("#s2", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.25, ease: "power2.out", immediateRender: false }}, Z.satir2[0]);
  darbe("#kart-s2-ok", Z.satir2[0] + 0.05, 0.20, "power1.out");

  // 4. gonder_ciz
  darbe("#gonder-dolgu", Z.gonder_ciz[0], 0.40, "sine.inOut");
  darbe("#gonder-cizgi", Z.gonder_ciz[0], 0.40, "sine.inOut");

  // 5. imi_ciz
  darbe("#kaydet-imi", Z.imi_ciz[0], 0.40, "sine.inOut");
  tl.fromTo("#kaydet-yazi", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.25, ease: "power2.out", immediateRender: false }}, Z.imi_ciz[0]);

  // 6. arkadasina
  tl.fromTo("#gonder-yazi1", {{ opacity: 0, y: 12 }},
    {{ opacity: 1, y: 0, duration: 0.25, ease: "power3.out", immediateRender: false }}, Z.arkadasina[0]);

  // 7. gonder_yaz
  tl.fromTo("#gonder-yazi2", {{ opacity: 0, y: 12 }},
    {{ opacity: 1, y: 0, duration: 0.25, ease: "power3.out", immediateRender: false }}, Z.gonder_yaz[0]);

  // 8. sari_gecis
  tl.fromTo("#gonder-dolgu", {{ fillOpacity: 0 }},
    {{ fillOpacity: 1, duration: 0.25, ease: "power2.out", immediateRender: false }}, Z.sari_gecis[0]);
  // hap + hap dönemi virgülü söner; mürekkep "leaves," 0,10 sn sonra gelir (yazı × yazı 0,5 eşiğini aşmaz)
  tl.fromTo(["#leaves-hap", "#kart-s1-virgul"], {{ opacity: 1 }},
    {{ opacity: 0, duration: 0.20, ease: "power2.out", immediateRender: false }}, Z.sari_gecis[0]);
  tl.fromTo("#leaves-yazi", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.20, ease: "power2.out", immediateRender: false }}, Z.sari_gecis[0] + 0.10);
  darbe("#leaves-alti", Z.sari_gecis[0], 0.30, "power1.out");

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""

    # HTML içerik denetimleri (§8 kural 5)
    yasaklar = ["\u2192", "\u2260", 'id="rz1"', 'id="t2"', 'id="ku-nokta"']
    for y in yasaklar:
        assert y.lower() not in html.lower(), f"HTML içinde yasak öğe bulundu: {y}"
    assert all(ord(c) <= 0x1F000 for c in html), "HTML içinde U+1F000 üstü karakter bulundu"

    return html, zamanlar


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_cikti, z_cikti = uret()
    (AD / "proje" / "index.html").write_text(html_cikti, encoding="utf-8")
    (AD / "zamanlar.json").write_text(json.dumps(z_cikti, ensure_ascii=False, indent=2), encoding="utf-8")
    print("proje/index.html yazıldı:", len(html_cikti), "karakter")
    print("zamanlar.json yazıldı:", len(z_cikti["olaylar"]), "ses olayı")

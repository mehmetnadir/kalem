"""Sahne 03 CTA index.html ve zamanlar.json üretici (02-04-ydt-temel-s3; DİKEY 1080x1920; 347 kare = 11,5667 sn).
Cümle 4 ses olayları ve kinetik sözcükler. HUD hazır; içerik bandı 352-1392; altyazı 1400-1536."""
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))["sahneler"]
           if s["klasor"] == AD.name)
T_BAS: float = SAH["t_bas"]  # 15.99
KARE: int = SAH["kare"]      # 347
SURE: float = round(KARE / 30, 4)  # 11.5667
SOZ: List[Dict[str, Any]] = [
    w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w["cumle"] == 4
]
ALT: List[Dict[str, Any]] = json.loads(
    (PAKET / "ortak" / "anlatim" / "altyazi.json").read_text(encoding="utf-8")
)
R = Y.RENK
CIP = "Full lesson"


def T(i: int, bas: str = "") -> float:
    """Cümle 4, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = w["sozcuk"]
        assert val.lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, val, bas)
    return float(w["t0"])


def E(i: int, bas: str = "") -> float:
    """Cümle 4, i. sözcüğün t1'i (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = w["sozcuk"]
        assert val.lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, val, bas)
    return float(w["t1"])


# Sözcük assert'leri ile 18 sözcüğün sırası baştan doğrulanır
BEKLENEN_SOZLER: List[Tuple[int, str]] = [
    (0, "Bu"), (1, "üç"), (2, "farktan"), (3, "yalnız"), (4, "biri"),
    (5, "Tam"), (6, "ders"), (7, "Simple"), (8, "Present"), (9, "ve"),
    (10, "Present"), (11, "Continuous"), (12, "Üç"), (13, "farkın"),
    (14, "hepsi"), (15, "dört"), (16, "buçuk"), (17, "dakikada")
]
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)


# Tren ve bilet ikonu (02-04-ydt-temel sahne 07; kaynak sahne 05 trenParcalari/biletParcalari)
def _kutu(x: float, y: float, w: float, h: float, ince: bool = False) -> Dict[str, Any]:
    return {"n": [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], "kapali": True, "ince": ince}


TREN: List[Dict[str, Any]] = [  # sahne 05 trenParcalari sadeleştirmesi (yandan, sağa bakar)
    _kutu(200, 55, 170, 75), _kutu(200, 10, 75, 45), _kutu(320, 22, 26, 33, True),
    {"n": [(370, 95), (398, 130), (370, 130)]}, _kutu(0, 45, 175, 85),
    {"n": [(175, 112), (200, 112)], "ince": True},
    _kutu(20, 60, 50, 30, True), _kutu(100, 60, 50, 30, True), _kutu(215, 20, 42, 25, True),
    {"daire": (40, 138, 17)}, {"daire": (135, 138, 17)}, {"daire": (240, 138, 17)}, {"daire": (335, 138, 17)},
    {"n": [(-10, 158), (420, 158)], "ince": True},
]


def _bilet() -> List[Dict[str, Any]]:
    """Sahne 05 biletParcalari: iki yanında çentik, delik çizgisi, 3 baskı satırı (merkez 0,0)."""
    def yay(x0: float, yon: int) -> List[Tuple[float, float]]:
        return [(x0 - yon * 22 * math.cos(-math.pi / 2 + i / 12 * math.pi),
                 yon * 22 * math.sin(-math.pi / 2 + i / 12 * math.pi)) for i in range(13)]
    kenar = [(-180, -70), (180, -70), (180, -22)] + yay(180, 1) + [(180, 70), (-180, 70), (-180, 22)] + yay(-180, -1)
    p: List[Dict[str, Any]] = [{"n": kenar + [(-180, -70)]}]
    p += [{"n": [(100, -58 + i * 20), (100, -47 + i * 20)], "ince": True} for i in range(6)]
    p += [{"n": [(-150, y), (x1, y)], "ince": True} for y, x1 in ((-30, 60), (0, 30), (30, 70))]
    return p


BILET: List[Dict[str, Any]] = _bilet()


def _kutusu(parcalar: List[Dict[str, Any]]) -> Tuple[float, float, float, float]:
    xs: List[float] = []
    ys: List[float] = []
    for p in parcalar:
        if "daire" in p:
            x, y, r = p["daire"]
            xs += [x - r, x + r]
            ys += [y - r, y + r]
        else:
            xs += [q[0] for q in p["n"]]
            ys += [q[1] for q in p["n"]]
    return min(xs), min(ys), max(xs), max(ys)


def _daire_yolu(cx: float, cy: float, r: float) -> str:
    k = 0.5523 * r
    return (
        "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f "
        "C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
            cx + r, cy, cx + r, cy + k, cx + k, cy + r, cx, cy + r,
            cx - k, cy + r, cx - r, cy + k, cx - r, cy,
            cx - r, cy - k, cx - k, cy - r, cx, cy - r,
            cx + k, cy - r, cx + r, cy - k, cx + r, cy
        )
    )


def ikon_yollari(
    parcalar: List[Dict[str, Any]], mx0: float, my0: float, en: float = 72.0, boy: float = 72.0
) -> List[Tuple[str, float, bool]]:
    """Izgara parçalarını en x boy kutusuna (merkez mx0, my0) sığdırır. Döner: [(d, uzunluk, ince)]."""
    gx0, gy0, gx1, gy1 = _kutusu(parcalar)
    sc = min(boy / (gy1 - gy0), en / (gx1 - gx0))
    gmx, gmy = (gx0 + gx1) / 2.0, (gy0 + gy1) / 2.0

    def P(q: Tuple[float, float]) -> Tuple[float, float]:
        return (mx0 + (q[0] - gmx) * sc, my0 + (q[1] - gmy) * sc)

    out: List[Tuple[str, float, bool]] = []
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
        d = "M%.1f %.1f " % q[0] + " ".join("L%.1f %.1f" % v for v in q[1:])
        out.append((d, uz, p.get("ince", False)))
    return out


# ---- Yerleşim Sabitleri (px) ----
CX: float = 540.0

# Satır A
A_Y: int = 452
A_BOY: int = 72

# Satır B
CAV_Y: int = 620
CAV_BOY: int = 96

# Ders Bandı
BANT_X: int = 132
BANT_Y: int = 660
BANT_W: int = 816
BANT_H: int = 236
BANT_RX: int = 48
BANT_CX: float = 540.0
BANT_CY: float = BANT_Y + BANT_H / 2.0  # 778.0
P1_Y: int = 758
P2_Y: int = 850

# İkonlar
TREN_CX: float = 84.0
BILET_CX: float = 996.0
IKON_EN: float = 72.0
IKON_KALIN: float = 3.2  # 72 px trende 4,0 pencere ve tekeri kapatıyordu (kare 26,4, tur 1)
IKON_INCE: float = 2.0

# Satır E
E_Y: int = 1066
E_BOY: int = 72

# Satır F (Hap)
F_BOY: int = 64
HAP_Y: int = 1200
HAP_H: int = 112
HAP_RX: int = 56
HAP_CX: float = 540.0
HAP_CY: float = HAP_Y + HAP_H / 2.0  # 1256.0
HAP_YAZI_Y: int = 1279


def uret() -> Tuple[str, Dict[str, Any]]:
    """index.html ve zamanlar verisini üretir."""
    # 1. Satır A ölçüleri
    w_a1 = Y.genislik("Lexend", 700, "üç farktan biri", A_BOY)
    w_a2 = Y.genislik("Lexend", 700, "üç farkın hepsi", A_BOY)
    a_x0 = CX - max(w_a1, w_a2) / 2.0

    w_uc = Y.genislik("Lexend", 700, "üç", A_BOY)
    w_uc_bos = Y.genislik("Lexend", 700, "üç ", A_BOY)
    w_farktan_bos = Y.genislik("Lexend", 700, "üç farktan ", A_BOY)
    w_farkin_bos = Y.genislik("Lexend", 700, "üç farkın ", A_BOY)

    x_uc = a_x0
    x_farktan = a_x0 + w_uc_bos
    x_biri = a_x0 + w_farktan_bos
    x_farkin = a_x0 + w_uc_bos
    x_hepsi = a_x0 + w_farkin_bos

    alt_y = A_Y + 0.42 * A_BOY
    alt_x0 = a_x0 - 4.0
    alt_x1 = a_x0 + w_uc + 4.0
    alt_xm = (alt_x0 + alt_x1) / 2.0
    d_alt = f"M{alt_x0:.1f} {alt_y:.1f} L{alt_xm:.1f} {alt_y - 2:.1f} L{alt_x1:.1f} {alt_y + 1:.1f}"

    # 2. Satır B (Tam ders:)
    cav_txt = "Tam ders:"
    cav_w = Y.genislik("Caveat", 700, cav_txt, CAV_BOY)
    cav_clip_w = cav_w + 24.0

    # 3. Bant & Bant Yazıları
    w_vs_birim = Y.genislik("Fredoka", 700, "vs Present Continuous", 1)
    bant_boy = min(96, math.floor((BANT_W - 2 * 28) / w_vs_birim))
    assert bant_boy == 74, f"beklenen 74, bulunan {bant_boy}"
    assert w_vs_birim * bant_boy <= 760, f"satır 2 banttan taşıyor: {w_vs_birim * bant_boy}"

    w_s1 = Y.genislik("Fredoka", 700, "Simple Present", bant_boy)
    s1_x0 = CX - w_s1 / 2.0
    x_simple = s1_x0
    x_present1 = s1_x0 + Y.genislik("Fredoka", 700, "Simple ", bant_boy)

    w_s2 = Y.genislik("Fredoka", 700, "vs Present Continuous", bant_boy)
    s2_x0 = CX - w_s2 / 2.0
    x_vs = s2_x0
    x_present2 = s2_x0 + Y.genislik("Fredoka", 700, "vs ", bant_boy)
    x_cont = s2_x0 + Y.genislik("Fredoka", 700, "vs Present ", bant_boy)

    # 4. İkonlar: Tren (sol, satır 1) ve Bilet (sağ, satır 2)
    tren_cy = P1_Y - 0.36 * bant_boy
    bilet_cy = P2_Y - 0.36 * bant_boy

    for parcalar, cx, cy, x_min, x_max in [
        (TREN, TREN_CX, tren_cy, 48.0, BANT_X - 8.0),
        (BILET, BILET_CX, bilet_cy, BANT_X + BANT_W + 8.0, 1032.0),
    ]:
        gx0, gy0, gx1, gy1 = _kutusu(parcalar)
        sc = min(IKON_EN / (gy1 - gy0), IKON_EN / (gx1 - gx0))
        gmx, gmy = (gx0 + gx1) / 2.0, (gy0 + gy1) / 2.0
        x0 = cx + (gx0 - gmx) * sc
        x1 = cx + (gx1 - gmx) * sc
        y0 = cy + (gy0 - gmy) * sc
        y1 = cy + (gy1 - gmy) * sc
        assert x_min <= x0 and x1 <= x_max, f"ikon x şeritten taşıyor: [{x0}, {x1}] not in [{x_min}, {x_max}]"
        assert BANT_Y <= y0 and y1 <= BANT_Y + BANT_H, f"ikon y banttan taşıyor: [{y0}, {y1}]"

    tren_yollar = ikon_yollari(TREN, TREN_CX, tren_cy, IKON_EN, IKON_EN)
    tren_ids = [f"tren_{i}" for i in range(len(tren_yollar))]
    tren_svg = "".join(
        f'<path id="tren_{i}" d="{d}" stroke-width="{IKON_INCE if ince else IKON_KALIN}" style="opacity:0"/>'
        for i, (d, _, ince) in enumerate(tren_yollar)
    )

    bilet_yollar = ikon_yollari(BILET, BILET_CX, bilet_cy, IKON_EN, IKON_EN)
    bilet_ids = [f"bilet_{i}" for i in range(len(bilet_yollar))]
    bilet_svg = "".join(
        f'<path id="bilet_{i}" d="{d}" stroke-width="{IKON_INCE if ince else IKON_KALIN}" style="opacity:0"/>'
        for i, (d, _, ince) in enumerate(bilet_yollar)
    )

    # 5. Satır E (Saat + dört buçuk dakikada)
    w_e_txt = Y.genislik("Lexend", 700, "dört buçuk dakikada", E_BOY)
    grp_w = 88.0 + 20.0 + w_e_txt
    grp_x0 = CX - grp_w / 2.0

    saat_s = 88.0 / 24.0
    saat_cy = E_Y - 0.36 * E_BOY
    saat_x = grp_x0
    saat_y = saat_cy - 44.0
    saat_yollar = Y.tabler("clock")
    saat_ids = [f"saat_{i}" for i in range(len(saat_yollar))]
    saat_svg = "".join(f'<path id="saat_{i}" d="{d}" style="opacity:0"/>' for i, d in enumerate(saat_yollar))

    e_txt_x0 = grp_x0 + 108.0
    x_dort = e_txt_x0
    x_bucuk = e_txt_x0 + Y.genislik("Lexend", 700, "dört ", E_BOY)
    x_dakikada = e_txt_x0 + Y.genislik("Lexend", 700, "dört buçuk ", E_BOY)

    # 6. Satır F (@ydspublishing)
    cta_txt = "@ydspublishing"
    w_cta = Y.genislik("Fredoka", 700, cta_txt, F_BOY)
    hap_w = w_cta + 112.0
    hap_rx = CX - hap_w / 2.0
    cta_x = CX - w_cta / 2.0
    cta_clip_w = w_cta + 24.0

    # 7. Zamanlar ve Olaylar
    def y_sn(t_kuresel: float) -> float:
        return round(t_kuresel - T_BAS, 4)

    t_tam = y_sn(T(5, "tam"))
    dur_tam = round(E(6, "ders") - T(5, "tam"), 4)

    t_hap_yazi = y_sn(T(17, "dakikada") + 0.10)
    dur_hap_yazi = round(E(17, "dakikada") - (T(17, "dakikada") + 0.10), 4)

    zamanlar: Dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "uc_giris": [y_sn(T(1, "üç")), 0.22],
        "farktan_giris": [y_sn(T(2, "farktan")), 0.22],
        "uc_altcizgi": [y_sn(T(1, "üç") + 0.22), 0.30],
        "biri_giris": [y_sn(T(4, "biri")), 0.22],
        "tam_ders": [t_tam, dur_tam],
        "bant_giris": [y_sn(T(7, "simple")), 0.35],
        "simple_giris": [y_sn(T(7, "simple")), 0.22],
        "present1_giris": [y_sn(T(8, "present")), 0.22],
        "vs_giris": [y_sn(T(9, "ve")), 0.22],
        "present2_giris": [y_sn(T(10, "present")), 0.22],
        "continuous_giris": [y_sn(T(11, "continuous")), 0.22],
        "farktan_biri_cikis": [y_sn(T(12, "üç")), 0.25],
        "farkin_giris": [y_sn(T(13, "farkın")), 0.22],
        "hepsi_giris": [y_sn(T(14, "hepsi")), 0.22],
        "saat_darbe": [y_sn(T(15, "dört")), 0.35],
        "dort_giris": [y_sn(T(15, "dört")), 0.22],
        "bucuk_giris": [y_sn(T(16, "buçuk")), 0.22],
        "dakikada_giris": [y_sn(T(17, "dakikada")), 0.22],
        "hap_giris": [y_sn(T(17, "dakikada")), 0.30],
        "hap_yazi": [t_hap_yazi, dur_hap_yazi],
        "tren_darbe": [y_sn(E(17, "dakikada")), 0.45],
        "bilet_darbe": [y_sn(E(17, "dakikada") + 0.10), 0.45],
        "olaylar": [
            [y_sn(T(1, "üç")), "tik", 0.4],
            [y_sn(T(1, "üç") + 0.22), "cizgi", 0.5],
            [y_sn(T(5, "tam")), "hisirti", 0.45],
            [y_sn(T(7, "simple")), "vurus", 0.9],
            [y_sn(T(9, "ve")), "tik", 0.5],
            [y_sn(T(12, "üç")), "tik", 0.4],
            [y_sn(T(15, "dört")), "cizgi", 0.5],
            [y_sn(T(17, "dakikada")), "tik", 0.6],
            [y_sn(T(17, "dakikada") + 0.10), "hisirti", 0.5],
            [y_sn(E(17, "dakikada")), "cizgi", 0.45],
            [y_sn(E(17, "dakikada") + 0.10), "cizgi", 0.45],
        ],
    }

    # 8. Altyazı ve Künye
    kunye_svg = Y.kunye_svg(CIP)
    alt_svg, alt_zaman = Y.altyazi_svg(T_BAS, SURE, ALT)

    # 9. ClipPath tanımları
    cp = lambda n, x, y, b: (  # noqa: E731
        f'<clipPath id="cp{n}"><rect id="cr{n}" x="{x:.1f}" y="{y - b}" width="0" height="{int(b * 1.5)}"/>'
        '</clipPath>'
    )
    clips = (
        cp("c", CX - cav_clip_w / 2.0, CAV_Y, CAV_BOY)
        + cp("l", CX - cta_clip_w / 2.0, HAP_YAZI_Y, F_BOY)
    )

    veri = {
        "Z": zamanlar,
        "cav_w": cav_clip_w,
        "cta_w": cta_clip_w,
        "bant_cx": BANT_CX,
        "bant_cy": BANT_CY,
        "hap_cx": HAP_CX,
        "hap_cy": HAP_CY,
        "saat_ids": saat_ids,
        "tren_ids": tren_ids,
        "bilet_ids": bilet_ids,
        "alt": alt_zaman,
    }

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{SURE}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>{clips}</defs>

<!-- Satır A: üç farktan biri / üç farkın hepsi -->
<text id="tx_uc" x="{x_uc:.1f}" y="{A_Y}" font-family="Lexend" font-weight="700" font-size="{A_BOY}" fill="{R['murekkep']}" style="opacity:0">üç</text>
<text id="tx_farktan" x="{x_farktan:.1f}" y="{A_Y}" font-family="Lexend" font-weight="700" font-size="{A_BOY}" fill="{R['murekkep']}" style="opacity:0">farktan</text>
<text id="tx_biri" x="{x_biri:.1f}" y="{A_Y}" font-family="Lexend" font-weight="700" font-size="{A_BOY}" fill="{R['murekkep']}" style="opacity:0">biri</text>
<text id="tx_farkin" x="{x_farkin:.1f}" y="{A_Y}" font-family="Lexend" font-weight="700" font-size="{A_BOY}" fill="{R['murekkep']}" style="opacity:0">farkın</text>
<text id="tx_hepsi" x="{x_hepsi:.1f}" y="{A_Y}" font-family="Lexend" font-weight="700" font-size="{A_BOY}" fill="{R['murekkep']}" style="opacity:0">hepsi</text>
<path id="uc_alt" d="{d_alt}" fill="none" stroke="{R['vurgu']}" stroke-width="10" stroke-linecap="round" style="opacity:0"/>

<!-- Satır B: Tam ders: -->
<text id="cav" x="540" y="{CAV_Y}" text-anchor="middle" font-family="Caveat" font-weight="700" font-size="{CAV_BOY}" fill="{R['murekkep']}" clip-path="url(#cpc)">{cav_txt}</text>

<!-- Ders Bandı -->
<g id="bantg" style="opacity:0">
<rect id="bant" x="{BANT_X}" y="{BANT_Y}" width="{BANT_W}" height="{BANT_H}" rx="{BANT_RX}" fill="{R['vurgu']}"/>
<text id="bp_simple" x="{x_simple:.1f}" y="{P1_Y}" font-family="Fredoka" font-weight="700" font-size="{bant_boy}" fill="{R['zemin']}" style="opacity:0">Simple</text>
<text id="bp_present1" x="{x_present1:.1f}" y="{P1_Y}" font-family="Fredoka" font-weight="700" font-size="{bant_boy}" fill="{R['zemin']}" style="opacity:0">Present</text>
<text id="bp_vs" x="{x_vs:.1f}" y="{P2_Y}" font-family="Fredoka" font-weight="700" font-size="{bant_boy}" fill="{R['zemin']}" style="opacity:0">vs</text>
<text id="bp_present2" x="{x_present2:.1f}" y="{P2_Y}" font-family="Fredoka" font-weight="700" font-size="{bant_boy}" fill="{R['zemin']}" style="opacity:0">Present</text>
<text id="bp_cont" x="{x_cont:.1f}" y="{P2_Y}" font-family="Fredoka" font-weight="700" font-size="{bant_boy}" fill="{R['zemin']}" style="opacity:0">Continuous</text>
</g>

<!-- İkon Sol: Tren (satır 1 hizası) -->
<g id="tren" fill="none" stroke="{R['murekkep']}" stroke-linecap="round" stroke-linejoin="round">
{tren_svg}
</g>

<!-- İkon Sağ: Bilet (satır 2 hizası) -->
<g id="bilet" fill="none" stroke="{R['murekkep']}" stroke-linecap="round" stroke-linejoin="round">
{bilet_svg}
</g>

<!-- Satır E: Saat + dört buçuk dakikada -->
<g id="saat" fill="none" stroke="{R['murekkep']}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{4.4 / saat_s:.4f}">
<g transform="translate({saat_x:.1f} {saat_y:.1f}) scale({saat_s:.6f})">
{saat_svg}
</g>
</g>
<text id="tx_dort" x="{x_dort:.1f}" y="{E_Y}" font-family="Lexend" font-weight="700" font-size="{E_BOY}" fill="{R['murekkep']}" style="opacity:0">dört</text>
<text id="tx_bucuk" x="{x_bucuk:.1f}" y="{E_Y}" font-family="Lexend" font-weight="700" font-size="{E_BOY}" fill="{R['murekkep']}" style="opacity:0">buçuk</text>
<text id="tx_dakikada" x="{x_dakikada:.1f}" y="{E_Y}" font-family="Lexend" font-weight="700" font-size="{E_BOY}" fill="{R['murekkep']}" style="opacity:0">dakikada</text>

<!-- Satır F: @ydspublishing hapı -->
<g id="pilg" style="opacity:0">
<rect id="pill" x="{hap_rx:.1f}" y="{HAP_Y}" width="{hap_w:.1f}" height="{HAP_H}" rx="{HAP_RX}" fill="{R['vurgu']}"/>
<text id="lin" x="{cta_x:.1f}" y="{HAP_YAZI_Y}" font-family="Fredoka" font-weight="700" font-size="{F_BOY}" fill="{R['zemin']}" clip-path="url(#cpl)">{cta_txt}</text>
</g>

{kunye_svg}<g id="altyazi">{alt_svg}</g>
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

  function darbe(id, bas, sure) {{
    var p = $("#" + id), L = p.getTotalLength();
    p.style.strokeDasharray = L + " " + (L + 2);
    p.style.strokeDashoffset = L;
    tl.set(p, ac({{ opacity: 1 }}), bas);
    tl.to(p, ac({{ strokeDashoffset: 0, duration: sure, ease: "none" }}), bas);
  }}

  function darbeCok(ids, bas, toplamSure) {{
    var elms = ids.map(function (id) {{ return $("#" + id); }});
    var lens = elms.map(function (p) {{ return p.getTotalLength(); }});
    var tot = lens.reduce(function (a, b) {{ return a + b; }}, 0) || 1;
    var t = bas;
    for (var i = 0; i < elms.length; i++) {{
      var p = elms[i], L = lens[i];
      var s = toplamSure * (L / tot);
      p.style.strokeDasharray = L + " " + (L + 2);
      p.style.strokeDashoffset = L;
      tl.set(p, ac({{ opacity: 1 }}), t);
      tl.to(p, ac({{ strokeDashoffset: 0, duration: s, ease: "none" }}), t);
      t += s;
    }}
  }}

  function kinetik(id, bas) {{
    tl.fromTo(id, {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.22, ease: "back.out(1.6)", immediateRender: false }}, bas);
  }}

  function yaz(id, z, w) {{
    tl.fromTo("#cr" + id, {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: w }}, duration: z[1], ease: "none", immediateRender: false }}, z[0]);
  }}

  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});

  kinetik("#tx_uc", Z.uc_giris[0]);
  kinetik("#tx_farktan", Z.farktan_giris[0]);
  darbe("uc_alt", Z.uc_altcizgi[0], Z.uc_altcizgi[1]);
  kinetik("#tx_biri", Z.biri_giris[0]);

  yaz("c", Z.tam_ders, V.cav_w);

  gsap.set("#bantg", {{ svgOrigin: V.bant_cx + " " + V.bant_cy }});
  tl.fromTo("#bantg", {{ opacity: 0, scale: 0.92 }}, {{ opacity: 1, scale: 1, duration: Z.bant_giris[1], ease: "power3.out", immediateRender: false }}, Z.bant_giris[0]);

  kinetik("#bp_simple", Z.simple_giris[0]);
  kinetik("#bp_present1", Z.present1_giris[0]);
  kinetik("#bp_vs", Z.vs_giris[0]);
  kinetik("#bp_present2", Z.present2_giris[0]);
  kinetik("#bp_cont", Z.continuous_giris[0]);

  tl.to(["#tx_farktan", "#tx_biri"], {{ opacity: 0, y: -16, duration: Z.farktan_biri_cikis[1], ease: "power2.in", immediateRender: false }}, Z.farktan_biri_cikis[0]);
  kinetik("#tx_farkin", Z.farkin_giris[0]);
  kinetik("#tx_hepsi", Z.hepsi_giris[0]);

  darbeCok(V.saat_ids, Z.saat_darbe[0], Z.saat_darbe[1]);
  kinetik("#tx_dort", Z.dort_giris[0]);
  kinetik("#tx_bucuk", Z.bucuk_giris[0]);
  kinetik("#tx_dakikada", Z.dakikada_giris[0]);

  gsap.set("#pilg", {{ svgOrigin: V.hap_cx + " " + V.hap_cy }});
  tl.fromTo("#pilg", {{ opacity: 0, scale: 0.9 }}, {{ opacity: 1, scale: 1, duration: Z.hap_giris[1], ease: "power3.out", immediateRender: false }}, Z.hap_giris[0]);
  yaz("l", Z.hap_yazi, V.cta_w);

  darbeCok(V.tren_ids, Z.tren_darbe[0], Z.tren_darbe[1]);
  darbeCok(V.bilet_ids, Z.bilet_darbe[0], Z.bilet_darbe[1]);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, zamanlar


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_cikti, z_cikti = uret()
    (AD / "proje" / "index.html").write_text(html_cikti, encoding="utf-8")
    (AD / "zamanlar.json").write_text(json.dumps(z_cikti, ensure_ascii=False, indent=2), encoding="utf-8")
    print("proje/index.html yazıldı:", len(html_cikti), "karakter")
    print("zamanlar.json yazıldı:", len(z_cikti["olaylar"]), "ses olayı")

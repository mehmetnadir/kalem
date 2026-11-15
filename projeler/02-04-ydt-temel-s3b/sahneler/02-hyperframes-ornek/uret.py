"""Sahne 02 — Örnek (02-04-ydt-temel-s3 shorts, HyperFrames DİKEY 1080x1920, huni v2).

Tasarım: SPEC.md (şef); kod agy-filo (15.11.2026).
DUZ2 (15.11): cümle 3 "Biletimi aldım, saat belli: kesin düzenleme, şimdiki zaman. Tren tarifeye uyar: geniş zaman.";
etiketler `kesin düzenleme` / `tarife` (TR, soluk); balonda TR soru yok (`-ing?`), TR soru yalnız altyazıda; altyazı karaoke
(sahne 03 düzeni: söylenmemiş sözcük ikincil, söylenen mürekkep); rozet `YDT · TEMEL`; kol b için kayma veriden (SOZ, TB).
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

# ---- 2. Zaman & Veri Okuma ----
PAKET = AD.parent.parent
SAH = next(
    s for s in json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))["sahneler"]
    if s["klasor"] == AD.name
)
SOZ_TUM = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
ALT_TUM = json.loads((PAKET / "ortak" / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
# A/B kol b (kanca değişkeni) başa cümle ekler. Kod iki kolda bayt aynı kalsın diye sözcük dizini ve zaman kol a
# ölçeğine indirgenir: kayma = örnek cümlesinin ilk sözcüğü ("The"; kol a'da cümle 1, t0 1,00). Yerel zaman değişmez.
_ILK = next(i for i, w in enumerate(SOZ_TUM) if w["sozcuk"] == "The")
C1 = int(SOZ_TUM[_ILK]["cumle"])
DT = round(float(SOZ_TUM[_ILK]["t0"]) - 1.00, 3)
SOZ = [{**w, "t0": round(w["t0"] - DT, 3), "t1": round(w["t1"] - DT, 3)} for w in SOZ_TUM[_ILK:]]
ALT = [{**a, "t0": round(a["t0"] - DT, 3), "t1": round(a["t1"] - DT, 3)} for a in ALT_TUM
       if C1 <= int(a["cumle"]) <= C1 + 2]
Z = {"t_bas": round(SAH["t_bas"] - DT, 3), "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
TB = Z["t_bas"]
assert TB == 3.0, f"sahne 02 t_bas (kol a ölçeği) {TB} != 3,0"

BEKLENEN_SOZ = {
    7: "p.m.",
    8: "today.",
    9: "I",
    10: "am",
    11: "going",
    12: "to",
    13: "the",
    14: "movie",
    15: "theater",
    16: "tonight.",
    17: "Hocam,",
    18: "tren",
    19: "de",
    20: "plana",
    21: "göre",
    22: "kalkmıyor",
    23: "mu?",
    24: "Neden",
    25: "-ing",
    26: "yok?",
    27: "Biletimi",
    28: "aldım,",
    29: "saat",
    30: "belli:",
    31: "kesin",
    32: "düzenleme,",
    33: "şimdiki",
    34: "zaman.",
    35: "Tren",
    36: "tarifeye",
    37: "uyar:",
    38: "geniş",
    39: "zaman.",
}
for idx, beklenen in BEKLENEN_SOZ.items():
    assert SOZ[idx]["sozcuk"] == beklenen, (
        f"SOZ[{idx}] beklenmeyen sozcuk: {SOZ[idx]['sozcuk']!r} != {beklenen!r}"
    )

assert SOZ[7]["t0"] == 3.00
assert SOZ[8]["t0"] == 3.40 and SOZ[8]["t1"] == 4.20
assert SOZ[9]["t0"] == 4.45
assert SOZ[10]["t0"] == 4.61
assert SOZ[11]["t0"] == 4.81
assert SOZ[12]["t0"] == 4.97
assert SOZ[13]["t0"] == 5.09
assert SOZ[14]["t0"] == 5.29
assert SOZ[15]["t0"] == 5.49
assert SOZ[16]["t0"] == 5.93 and SOZ[16]["t1"] == 6.53
assert SOZ[17]["t0"] == 7.00
assert SOZ[24]["t0"] == 9.72
assert SOZ[26]["t1"] == 10.84
assert SOZ[27]["t0"] == 11.51
assert SOZ[31]["t0"] == 13.87
assert SOZ[32]["t0"] == 14.15
assert SOZ[35]["t0"] == 16.06
assert SOZ[36]["t0"] == 16.46
assert SOZ[38]["t0"] == 17.90
assert SOZ[39]["t1"] == 18.86


def T(i: int, bas: str | None = None) -> float:
    if bas is not None:
        assert SOZ[i]["sozcuk"] == bas, f"SOZ[{i}] beklenmeyen sozcuk: {SOZ[i]['sozcuk']} != {bas}"
    return SOZ[i]["t0"]


def E(i: int, bas: str | None = None) -> float:
    if bas is not None:
        assert SOZ[i]["sozcuk"] == bas, f"SOZ[{i}] beklenmeyen sozcuk: {SOZ[i]['sozcuk']} != {bas}"
    return SOZ[i]["t1"]


EKRAN = {"Izmir": "İzmir", "seven": "7", "p.m.": "pm"}

R = Y.RENK
KRE = R["murekkep"]
IKN = R["ikincil"]
SAR = R["vurgu"]
ZEM = R["zemin"]

FIG = json.loads((AD / "cizim" / "ogretmen.json").read_text(encoding="utf-8"))

# ==============================================================================
# Huni v2 Geometri Sabitleri (SPEC §2.1)
# ==============================================================================
X_MIN = 60.0
X_MAX = 960.0
Y_MIN = 460.0
Y_MAX = 1380.0

K1_X = 71.0  # sahne 01 SPEC v2 KART kutu(71, 472, 878, 254, 71) ile aynı (kare 0 = 01 son karesi)
K1_Y = 472.0
K1_W = 878.0
K1_H = 254.0
K1_TOHUM = 71
K1_TX = 97.0
K1_Y1 = 568.0
K1_Y2 = 666.0

TRN_TX = 717.0  # sahne 01 SPEC v2 tren son kutusu [712, 494.5, 927, 585.5] (yerel kutu [-10, -24, 420, 158] × 0,5)
TRN_TY = 506.5
TRN_SC = 0.5
TRN_KUTU = (712.0, 494.5, 927.0, 585.5)
TRX = (TRN_KUTU[0] + TRN_KUTU[2]) / 2.0

TX_X0 = 72.0
TX_X1 = 948.0
AY = 848.0
XN = 120.0  # şef QA 6,4: 350/726'da iki alt etiket arası 28 px, tek satır gibi okunuyordu → 320/732 (≈ 65 px)
X7 = 320.0
XT = 732.0
LY = 808.0
GY = 924.0

K2_X = 70.0
K2_Y_A = 966.0
K2_W = 880.0
K2_H = 254.0
K2_TOHUM = 72
K2_TX = 97.0
K2_Y1_A = 1062.0
K2_Y2_A = 1160.0
K2_DY = -132.0

BS_BIL = 0.40
BCX_BIL = 859.0
BCY_BIL = 1017.0
E_BIL = -0.06

BS0 = 0.60
BTX = 64.0 + 45.0 * BS0
BTY = 1144.0

BAL_X0 = 256.0
BAL_Y0 = 1112.0
BAL_X1 = 954.0
BAL_Y1 = 1372.0
BAL_TX = 214.0
BAL_TY = 1300.0
BAL_WX = 296.0
BAL_TABANLAR = [1186.0, 1262.0, 1338.0]

CN_X = 767.0
CN_Y = 1112.0
BAG_Y = 704.0

FY0 = 1110.0
FIG_FS_H = 266.0
OK_FIG_BITIS_Y = 1102.0

KRM_Y = 961.0
KLM_Y = 684.0

LP_X = 300.0
LP_TABAN = 1172.0
LP_OK_Y = 1150.0

LT_X = 97.0
LT_TABAN = 792.0
LT_OK_Y = 770.0


# ---- 3.2 Kalem Geometrisi (kalem-canvas.js -> Python) ----
def _u32(x: int) -> int:
    return x & 0xFFFFFFFF


def _imul(a: int, b: int) -> int:
    return ((a & 0xFFFFFFFF) * (b & 0xFFFFFFFF)) & 0xFFFFFFFF


def hash_(a: int, b: int = 0, c: int = 0) -> float:
    a_u, b_u, c_u = _u32(a), _u32(b), _u32(c)
    h = (_imul(a_u, 374761393) + _imul(b_u, 668265263) + _imul(c_u, 1274126177)) & 0xFFFFFFFF
    h = _imul(h ^ (h >> 13), 1274126177)
    h = (h ^ (h >> 16)) & 0xFFFFFFFF
    return h / 4294967296.0


def _lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def gurul(x: float, s: int) -> float:
    i = math.floor(x)
    f = x - i
    u = f * f * (3.0 - 2.0 * f)
    return _lerp(hash_(i, s, 7), hash_(i + 1, s, 7), u) - 0.5


def elips(
    cx: float, cy: float, rx: float, ry: float, egim: float = 0.0, tohum: int = 1
) -> list[tuple[float, float]]:
    a0 = hash_(tohum, 1, 3) * math.pi * 2.0
    tur = 1.06 + 0.04 * hash_(tohum, 2, 3)
    n = max(24, math.ceil(math.pi * (rx + ry) * tur / 9.0))
    ce = math.cos(egim)
    se = math.sin(egim)
    cik = []
    for i in range(n + 1):
        u_val = i / n
        a = a0 + u_val * tur * math.pi * 2.0
        r = 1.0 + 0.06 * u_val + 0.025 * gurul(u_val * 5.0, tohum)
        x = rx * r * math.cos(a)
        y = ry * r * math.sin(a)
        cik.append((round(cx + x * ce - y * se, 2), round(cy + x * se + y * ce, 2)))
    return cik


def kutu(
    x: float, y: float, w: float, h: float, tohum: int = 1
) -> list[list[tuple[float, float]]]:
    def j(k: int) -> float:
        return (hash_(tohum, k, 9) - 0.5) * 5.0

    def e(k: int) -> float:
        return 3.0 + 6.0 * hash_(tohum, k, 11)

    def kenar(a: tuple[float, float], b: tuple[float, float], k: int) -> list[tuple[float, float]]:
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        L = math.hypot(dx, dy) or 1.0
        bos = (hash_(tohum, k, 13) - 0.5) * 5.0
        return [
            (round(a[0], 2), round(a[1], 2)),
            (round(a[0] + dx / 2.0 - dy / L * bos, 2), round(a[1] + dy / 2.0 + dx / L * bos, 2)),
            (round(b[0], 2), round(b[1], 2)),
        ]

    return [
        kenar((x - e(1), y + j(1)), (x + w + e(2), y + j(2)), 1),
        kenar((x + w + j(3), y - e(3)), (x + w + j(4), y + h + e(4)), 2),
        kenar((x + w + e(5), y + h + j(5)), (x - e(6), y + h + j(6)), 3),
        kenar((x + j(7), y + h + e(7)), (x + j(8), y - e(8)), 4),
    ]


def pts_to_d(pts: list[tuple[float, float]]) -> str:
    return f"M {pts[0][0]:.2f} {pts[0][1]:.2f} " + " ".join(f"L {p[0]:.2f} {p[1]:.2f}" for p in pts[1:])


def kutu_kenar_to_d(kenar: list[tuple[float, float]]) -> str:
    a, m, b = kenar
    return f"M {a[0]:.2f} {a[1]:.2f} Q {m[0]:.2f} {m[1]:.2f} {b[0]:.2f} {b[1]:.2f}"


def g_f700(m: str, boy: float = 64.0) -> float:
    return Y.genislik("Fredoka", 700, m, boy)


def g_f600(m: str, boy: float = 64.0) -> float:
    return Y.genislik("Fredoka", 600, m, boy)


def g_c700(m: str, boy: float = 64.0) -> float:
    return Y.genislik("Caveat", 700, m, boy)


def g_l700(m: str, boy: float = 40.0) -> float:
    return Y.genislik("Lexend", 700, m, boy)


def statik(kim: str, d: str, renk: str, w: float, alfa: float = 1.0) -> str:
    return (
        f'<path id="{kim}" d="{d}" fill="none" stroke="{renk}" stroke-width="{w:.1f}" '
        f'stroke-linecap="round" stroke-linejoin="round" opacity="{alfa:.2f}"/>'
    )


def metin(
    kim: str,
    x: float,
    y: float,
    m: str,
    aile: str = "Fredoka",
    agr: int = 700,
    boy: float = 64.0,
    renk: str = KRE,
    anchor: str = "start",
) -> str:
    anc = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return (
        f'<text id="{kim}" x="{x:.1f}" y="{y:.1f}" font-family="{aile}" font-weight="{agr}" '
        f'font-size="{boy:.1f}" fill="{renk}"{anc} xml:space="preserve">{m}</text>'
    )


def soldur(s: Y.Sahne, a: str, b: str, t: float, d: float = 0.25) -> None:
    sel_a = a if a.startswith("#") else f"#{a}"
    sel_b = b if b.startswith("#") else f"#{b}"
    s.to(sel_a, t, {"opacity": 0, "duration": d, "ease": "power1.inOut"})
    s.to(sel_b, t, {"opacity": 1, "duration": d, "ease": "power1.inOut"})


def kunye_v2() -> str:
    """SPEC §3.1 Künye v2: Simple Present vs Present Continuous + YDT · TEMEL rozeti."""
    konu = "Simple Present vs Present Continuous"
    rw = g_l700("YDT · TEMEL", 26) + 40.0
    kb = None
    for b in range(34, 27, -1):
        if 60.0 + g_f700(konu, b) + 20.0 + rw <= 960.0:
            kb = b
            break
    assert kb is not None, "Künye konusu sığmadı"
    rx = 60.0 + g_f700(konu, kb) + 20.0
    return (
        '<g id="kunye">'
        f'<text id="ku-konu" x="60" y="420" font-family="Fredoka" font-weight="700" font-size="{kb}" '
        f'fill="{KRE}" style="font-kerning:none" xml:space="preserve">{konu}</text>'
        f'<g id="ku-rz">'
        f'<rect x="{rx:.2f}" y="386" width="{rw:.2f}" height="48" rx="24" fill="{SAR}"/>'
        f'<text x="{rx + rw / 2.0:.2f}" y="419.4" text-anchor="middle" font-family="Lexend" font-weight="700" '
        f'font-size="26" fill="{ZEM}" xml:space="preserve">YDT · TEMEL</text>'
        '</g>'
        '</g>'
    )


def tren_svg() -> str:
    yollar: list[str] = []
    idx = 0

    def ekle_kutu(x: float, y: float, w: float, h: float, tohum: int, st_w: float, renk: str) -> None:
        nonlocal idx
        for kenar in kutu(x, y, w, h, tohum):
            d = kutu_kenar_to_d(kenar)
            yollar.append(
                f'<path id="trn_{idx}" d="{d}" stroke="{renk}" stroke-width="{st_w:.1f}" '
                f'vector-effect="non-scaling-stroke"/>'
            )
            idx += 1

    def ekle_duz(pts: list[tuple[float, float]], st_w: float, renk: str) -> None:
        nonlocal idx
        d = pts_to_d(pts)
        yollar.append(
            f'<path id="trn_{idx}" d="{d}" stroke="{renk}" stroke-width="{st_w:.1f}" '
            f'vector-effect="non-scaling-stroke"/>'
        )
        idx += 1

    def ekle_elips(
        cx: float, cy: float, rx: float, ry: float, egim: float, tohum: int, st_w: float, renk: str
    ) -> None:
        nonlocal idx
        d = pts_to_d(elips(cx, cy, rx, ry, egim, tohum))
        yollar.append(
            f'<path id="trn_{idx}" d="{d}" stroke="{renk}" stroke-width="{st_w:.1f}" '
            f'vector-effect="non-scaling-stroke"/>'
        )
        idx += 1

    # Lokomotif kutu(200, 55, 170, 75, 31) -> govde 4.5, KRE
    ekle_kutu(200, 55, 170, 75, 31, 4.5, KRE)
    # Kabin kutu(200, 10, 75, 45, 32) -> govde 4.5, KRE
    ekle_kutu(200, 10, 75, 45, 32, 4.5, KRE)
    # Baca kutu(320, 22, 26, 33, 33) -> ince 3.6, KRE
    ekle_kutu(320, 22, 26, 33, 33, 3.6, KRE)
    # Ön burun düz [(370, 95), (398, 130), (370, 130)] -> govde 4.5, KRE
    ekle_duz([(370.0, 95.0), (398.0, 130.0), (370.0, 130.0)], 4.5, KRE)
    # Vagon kutu(0, 45, 175, 85, 34) -> govde 4.5, KRE
    ekle_kutu(0, 45, 175, 85, 34, 4.5, KRE)
    # Bağlantı düz [(175, 112), (200, 112)] -> ince 3.6, KRE
    ekle_duz([(175.0, 112.0), (200.0, 112.0)], 3.6, KRE)
    # Vagon camları 1 kutu(20, 60, 50, 30, 35) -> ince 3.6, KRE
    ekle_kutu(20, 60, 50, 30, 35, 3.6, KRE)
    # Vagon camları 2 kutu(100, 60, 50, 30, 36) -> ince 3.6, KRE
    ekle_kutu(100, 60, 50, 30, 36, 3.6, KRE)
    # Kabin camı kutu(215, 20, 42, 25, 37) -> ince 3.6, KRE
    ekle_kutu(215, 20, 42, 25, 37, 3.6, KRE)
    # Tekerlekler
    for i, x in enumerate([40, 135, 240, 335]):
        ekle_elips(x, 138, 17, 17, 0, 50 + i, 4.5, KRE)
    # Ray düz [(-10, 158), (420, 158)] -> ray 4.0, IKN
    ekle_duz([(-10.0, 158.0), (420.0, 158.0)], 4.0, IKN)
    # Duman
    ekle_elips(345, 2, 11, 9, 0.2, 61, 3.4, IKN)
    ekle_elips(372, -16, 8, 7, 0.3, 62, 3.2, IKN)

    ic = "".join(yollar)
    return (
        f'<g id="tren" transform="translate({TRN_TX:g} {TRN_TY:g}) scale({TRN_SC})" fill="none" '
        f'stroke-linecap="round" stroke-linejoin="round">{ic}</g>'
    )


def bilet_verisi(
    bcx: float = BCX_BIL, bcy: float = BCY_BIL
) -> tuple[list[tuple[str, str, float]], list[tuple[float, float]]]:
    ce_bil = math.cos(E_BIL)
    se_bil = math.sin(E_BIL)

    def P(x: float, y: float) -> tuple[float, float]:
        return (
            round(bcx + BS_BIL * (x * ce_bil - y * se_bil), 2),
            round(bcy + BS_BIL * (x * se_bil + y * ce_bil), 2),
        )

    def yay(x0: float, yon: float) -> list[tuple[float, float]]:
        res = []
        for i in range(13):
            a = -math.pi / 2.0 + (i / 12.0) * math.pi
            res.append((x0 - yon * 22.0 * math.cos(a), yon * 22.0 * math.sin(a)))
        return res

    k1 = [P(-180, -70), P(180, -70)]
    k2 = [P(180, -70), P(180, -22)] + [P(x, y) for x, y in yay(180, 1)] + [P(180, 70)]
    k3 = [P(180, 70), P(-180, 70)]
    k4 = [P(-180, 70), P(-180, 22)] + [P(x, y) for x, y in yay(-180, -1)] + [P(-180, -70)]

    cikis: list[tuple[str, str, float]] = []
    for k in (k1, k2, k3, k4):
        cikis.append((pts_to_d(k), KRE, 4.5))

    for i in range(6):
        y0_delik = -58.0 + i * 20.0
        pts = [P(100.0, y0_delik), P(100.0, y0_delik + 11.0)]
        cikis.append((pts_to_d(pts), IKN, 3.4))

    satirlar = [
        [P(-150.0, -30.0), P(60.0, -30.0)],
        [P(-150.0, 0.0), P(30.0, 0.0)],
        [P(-150.0, 30.0), P(70.0, 30.0)],
    ]
    for pts in satirlar:
        cikis.append((pts_to_d(pts), IKN, 4.0))

    kenar_noktalari = [p for k in (k1, k2, k3, k4) for p in k]
    return cikis, kenar_noktalari


def bilet_yollari() -> list[tuple[str, str, float]]:
    cikis, _ = bilet_verisi(BCX_BIL, BCY_BIL)
    return cikis


def ok_tek(x0: float, y0: float, x1: float, y1: float, egim: float = 2.0) -> str:
    """Y.el_ok ile aynı ok, TEK kontur (Chrome kesik deseni her alt yolda baştan başlar; uç gövdeden önce görünür)."""
    a = math.atan2(y1 - y0, x1 - x0)
    b1 = (x1 - 22.0 * math.cos(a - 0.5), y1 - 22.0 * math.sin(a - 0.5))
    b2 = (x1 - 22.0 * math.cos(a + 0.5), y1 - 22.0 * math.sin(a + 0.5))
    uc = f" L {b1[0]:.1f} {b1[1]:.1f} L {x1:.1f} {y1:.1f} L {b2[0]:.1f} {b2[1]:.1f}"
    return Y.el_cizgi(x0, y0, x1, y1, egim) + uc


def cevir_ekran(m: str) -> str:
    return " ".join(EKRAN.get(w, w) for w in m.split(" "))


def altyazi_dilimleri_k() -> list[tuple[float, float, list[tuple[str, float]]]]:
    """altyazi.json parçalarını (örnek cümlesi + 2 cümle, kol a ölçeği) en çok 2 satıra sığan dilimlere böler.
    -> [(t0, t1, [(ekran sözcüğü, t0), ...])]; sözcük sayısı parça metniyle birebir (karaoke eşlemesi)."""

    def satir(m: str) -> int:
        n, cur = 1, ""
        for w in m.split(" "):
            d = (cur + " " + w) if cur else w
            if Y.genislik("Lexend", 500, d, 44) > 900.0 and cur:
                n += 1
                cur = w
            else:
                cur = d
        return n

    out: list[tuple[float, float, list[tuple[str, float]]]] = []
    for a in ALT:
        kel = [w for w in SOZ if w["cumle"] == a["cumle"] and a["t0"] - 0.05 <= w["t0"] < a["t1"]]
        assert len(kel) == len(a["metin"].split(" ")), f"altyazı/sözcük sayısı tutmuyor: {a['metin']}"
        soz = [(EKRAN.get(w["sozcuk"], w["sozcuk"]), float(w["t0"])) for w in kel]
        if satir(" ".join(x for x, _ in soz)) <= 2:
            out.append((a["t0"], a["t1"], soz))
            continue
        cur: list[tuple[str, float]] = []
        grup: list[list[tuple[str, float]]] = []
        for k in soz:
            if cur and satir(" ".join(x for x, _ in cur + [k])) > 2:
                grup.append(cur)
                cur = [k]
            else:
                cur.append(k)
        grup.append(cur)
        for i, g in enumerate(grup):
            out.append((a["t0"] if i == 0 else g[0][1], grup[i + 1][0][1] if i < len(grup) - 1 else a["t1"], g))
    return out


def altyazi_v2_svg(parcalar: list[dict]) -> str:
    """SPEC §5 Altyazı bandı v2: Lexend 500, satır genişliği <= 900, orta x 510.
    Boy sırası 44 -> 40 -> 36: 2 satıra sığan ilk boy. Satır aralığı round(boy * 1.27).
    Tek satır tabanı 1484; iki satır tabanları 1456 ve 1456 + aralık.
    DUZ2: her sözcük ayrı <tspan id="<pid>w<k>"> (karaoke); ilk dolgu `renk[k]`.
    """
    cikis: list[str] = []
    for p in parcalar:
        pid, met = p["id"], " ".join(p["sozler"])
        secilen_boy: int | None = None
        secilen_sat: list[str] = []

        for boy in (44, 40, 36):
            sat: list[str] = []
            cur = ""
            for w in met.split(" "):
                d = (cur + " " + w) if cur else w
                if Y.genislik("Lexend", 500, d, boy) > 900.0 and cur:
                    sat.append(cur)
                    cur = w
                else:
                    cur = d
            if cur:
                sat.append(cur)
            if len(sat) <= 2:
                secilen_boy = boy
                secilen_sat = sat
                break

        assert secilen_boy is not None, f"Altyazı metni 36 punto ile de 2 satıra sığmadı: {met}"
        assert len(secilen_sat) in (1, 2), f"Altyazı satır sayısı 1 veya 2 olmalı: {len(secilen_sat)}"
        for s_met in secilen_sat:
            assert Y.genislik("Lexend", 500, s_met, secilen_boy) <= 900.0, "Altyazı satır genişliği > 900"

        aralik = round(secilen_boy * 1.27)
        if len(secilen_sat) == 1:  # tabanlar sahne 01 SPEC v2 ile aynı (1490 · 1462/1518): kesmede altyazı kıpırdamaz
            tabanlar = [1490]
        else:
            tabanlar = [1462, 1462 + aralik]

        tsp_list: list[str] = []
        k = 0
        for y, t in zip(tabanlar, secilen_sat):
            parca: list[str] = []
            for w in t.split(" "):
                parca.append(f'<tspan id="{pid}w{k}" fill="{p["renk"][k]}">{w.replace("&", "&amp;")}</tspan>')
                k += 1
            tsp_list.append(
                f'<text x="510" y="{y}" text-anchor="middle" font-family="Lexend" font-weight="500" '
                f'font-size="{secilen_boy}" fill="{KRE}">' + " ".join(parca) + "</text>"
            )
        assert k == len(p["sozler"]), f"altyazı sözcük sayısı {k} != {len(p['sozler'])}"
        tsp = "".join(tsp_list)
        cikis.append(f'<g id="{pid}" style="opacity:0">{tsp}</g>')

    return "".join(cikis)


def uret() -> tuple[Y.Sahne, dict]:
    s = Y.Sahne(TB)
    zc_ids: set[str] = set()
    k2_ids: set[str] = set()
    bal_ids: list[str] = []

    # ----------------------------------------------------
    # Olay 0: Kare 0 = sahne 01 son karesi (statik)
    # ----------------------------------------------------
    kc_kenarlar = kutu(K1_X, K1_Y, K1_W, K1_H, K1_TOHUM)
    for i, kenar in enumerate(kc_kenarlar):
        s.svg.append(statik(f"kc{i}", kutu_kenar_to_d(kenar), KRE, 4.0))

    s.svg.append(tren_svg())

    s.svg.append(metin("r1", K1_TX, K1_Y1, "The train to İzmir", "Fredoka", 700, 64, KRE))
    s.svg.append(metin("r2", K1_TX, K1_Y2, "leaves at 7", "Fredoka", 700, 64, KRE))

    # ----------------------------------------------------
    # Olay 1: pm yazımı
    # ----------------------------------------------------
    t1 = max(0.40, s.S(T(7, "p.m.")))
    x_w7 = K1_TX + g_f700("leaves at 7 ")
    s.yazi("w7", x_w7, K1_Y2, [("pm", KRE)], "Fredoka", 700, 64, t1, 0.12, tur="tik", guc=0.4)

    # ----------------------------------------------------
    # Olay 2: today. yazımı
    # ----------------------------------------------------
    t2 = max(max(0.40, s.S(T(8, "today."))), t1 + 0.12)
    x_w8 = K1_TX + g_f700("leaves at 7 pm ")
    s.yazi("w8", x_w8, K1_Y2, [("today.", KRE)], "Fredoka", 700, 64, t2, 0.12, tur=None)

    # ----------------------------------------------------
    # Zaman Çizgisi Grubu (#zc) Öğeleri
    # ----------------------------------------------------
    # Olay 3: Zaman çizgisi ekseni
    t3 = t2
    s.yol("tx", ok_tek(TX_X0, AY, TX_X1, AY, 0.5), t3, 0.30, IKN, 4.5)
    zc_ids.add("tx")

    # Olay 4: now noktası + now
    t4 = t2 + 0.08
    s.svg.append(f'<circle id="tn_now" cx="{XN:.1f}" cy="{AY:.1f}" r="11" fill="{KRE}" style="opacity:0"/>')
    s.fromto("#tn_now", t4, {"opacity": 0}, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    zc_ids.add("tn_now")
    x_now = XN - g_c700("now") / 2.0
    s.yazi("tl_now", x_now, LY, [("now", KRE)], "Caveat", 700, 64, t4, 0.2)
    zc_ids.add("tl_now")

    # Olay 5: 7 pm çentiği + nokta + 7 pm
    t5 = t2 + 0.20
    s.yol("t7c", f"M {X7:.1f} {AY - 18.0:.1f} L {X7:.1f} {AY + 18.0:.1f}", t5, 0.12, KRE, 4.5)
    zc_ids.add("t7c")
    s.svg.append(f'<circle id="tn_7" cx="{X7:.1f}" cy="{AY:.1f}" r="9" fill="{KRE}" style="opacity:0"/>')
    s.fromto("#tn_7", t5, {"opacity": 0}, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    zc_ids.add("tn_7")
    x_7pm = X7 - g_c700("7 pm") / 2.0
    s.yazi("tl_7", x_7pm, LY, [("7 pm", KRE)], "Caveat", 700, 64, t5 + 0.04, 0.2)
    zc_ids.add("tl_7")

    # Olay 6: now -> 7 pm kalem oku (yay)
    t6 = t2 + 0.28
    p0_tok = (XN + 18.0, AY - 12.0)
    pc_tok = ((XN + X7) / 2.0 + 2.0, AY - 52.0)
    p1_tok = (X7 - 12.0, AY - 10.0)
    a_tok = math.atan2(p1_tok[1] - pc_tok[1], p1_tok[0] - pc_tok[0])
    k_tok = 18.0
    u1_x = p1_tok[0] - k_tok * math.cos(a_tok - 0.5)
    u1_y = p1_tok[1] - k_tok * math.sin(a_tok - 0.5)
    u2_x = p1_tok[0] - k_tok * math.cos(a_tok + 0.5)
    u2_y = p1_tok[1] - k_tok * math.sin(a_tok + 0.5)
    d_tok = (
        f"M {p0_tok[0]:.1f} {p0_tok[1]:.1f} Q {pc_tok[0]:.1f} {pc_tok[1]:.1f} {p1_tok[0]:.1f} {p1_tok[1]:.1f} "
        f"L {u1_x:.1f} {u1_y:.1f} L {p1_tok[0]:.1f} {p1_tok[1]:.1f} L {u2_x:.1f} {u2_y:.1f}"
    )
    s.yol("tok", d_tok, t6, 0.35, KRE, 4.5)
    zc_ids.add("tok")

    # Olay 7: 7 pm sarı daire
    t7 = t2 + 0.58
    s.yol("t7d", Y.el_daire(X7, LY - 20.0, 80, 38, 0.6), t7, 0.30, SAR, 6.0, tur="cizgi", guc=0.5)
    zc_ids.add("t7d")

    # Olay 8: gelecek · V-s
    t8 = t2 + 0.63
    m_tg1 = "gelecek · V-s"
    x_tg1 = X7 - g_c700(m_tg1) / 2.0
    s.yazi("tg1", x_tg1, GY, [(m_tg1, KRE)], "Caveat", 700, 64, t8, 0.30)
    zc_ids.add("tg1")

    # Olay 13: tonight noktası + tonight + gelecek · am + V-ing
    t13 = s.S(T(16, "tonight."))
    s.svg.append(f'<circle id="tn_t" cx="{XT:.1f}" cy="{AY:.1f}" r="11" fill="{KRE}" style="opacity:0"/>')
    s.fromto("#tn_t", t13, {"opacity": 0}, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    zc_ids.add("tn_t")
    x_tl_t = XT - g_c700("tonight") / 2.0
    s.yazi("tl_t", x_tl_t, LY, [("tonight", KRE)], "Caveat", 700, 64, t13 + 0.05, 0.2, tur=None)
    zc_ids.add("tl_t")
    m_tg2 = "gelecek · am + V-ing"
    x_tg2 = XT - g_c700(m_tg2) / 2.0
    s.yazi("tg2", x_tg2, GY, [(m_tg2, KRE)], "Caveat", 700, 64, t13 + 0.17, 0.30, tur="tik", guc=0.45)
    zc_ids.add("tg2")

    # Olay 14: Zaman çizgisi grubu söner
    t14 = s.S(T(17, "Hocam,")) - 0.50
    s.to("#zc", t14, {"opacity": 0, "duration": 0.25, "ease": "power2.in"})

    # ----------------------------------------------------
    # Kart 2 Grubu (#k2) Öğeleri (A konumu)
    # ----------------------------------------------------
    # Olay 9: Kart 2 çerçevesi
    t9 = s.S(T(9, "I")) - 0.30
    kd_kenarlar = kutu(K2_X, K2_Y_A, K2_W, K2_H, K2_TOHUM)
    kd_zamanlar = Y.cizgi_zamanlari([K2_W, K2_H, K2_W, K2_H], t9, t9 + 0.30)
    for i, (b, d_sure) in enumerate(kd_zamanlar):
        s.yol(
            f"kd{i}",
            kutu_kenar_to_d(kd_kenarlar[i]),
            b,
            d_sure,
            KRE,
            4.0,
            tur="cizgi" if i == 0 else None,
            guc=0.5,
        )
        k2_ids.add(f"kd{i}")

    # Olay 10: Kart 2 satır 1 sözcük sözcük
    k2_s1_sozcukler = ["I", "am", "going", "to", "the"]
    cur_prefix = ""
    for idx_offset, w_text in enumerate(k2_s1_sozcukler):
        i_soz = 9 + idx_offset
        t_w = s.S(T(i_soz, w_text))
        x_w = K2_TX + g_f700(cur_prefix)
        cur_prefix += w_text + " "
        s.yazi(
            f"w{i_soz}",
            x_w,
            K2_Y1_A,
            [(w_text, KRE)],
            "Fredoka",
            700,
            64,
            t_w,
            0.12,
            tur="tik" if i_soz == 9 else None,
            guc=0.35,
        )
        k2_ids.add(f"w{i_soz}")

    # Olay 11: Bilet kalemle
    t11 = s.S(T(14, "movie"))
    bilet_parcalar = bilet_yollari()
    bilet_uzunluklar = [Y.yol_uzunluk(p[0]) for p in bilet_parcalar]
    bilet_zamanlar = Y.cizgi_zamanlari(bilet_uzunluklar, t11, t11 + 0.45)
    for i, (b, d_sure) in enumerate(bilet_zamanlar):
        d_yol, r_yol, w_yol = bilet_parcalar[i]
        s.yol(f"bl{i}", d_yol, b, d_sure, r_yol, w_yol, tur="cizgi" if i == 0 else None, guc=0.45)
        k2_ids.add(f"bl{i}")

    # Olay 12: Kart 2 satır 2 sözcük sözcük
    k2_s2_sozcukler = ["movie", "theater", "tonight."]
    cur_prefix2 = ""
    for idx_offset, w_text in enumerate(k2_s2_sozcukler):
        i_soz = 14 + idx_offset
        t_w = s.S(T(i_soz, w_text))
        x_w = K2_TX + g_f700(cur_prefix2)
        cur_prefix2 += w_text + " "
        s.yazi(
            f"w{i_soz}",
            x_w,
            K2_Y2_A,
            [(w_text, KRE)],
            "Fredoka",
            700,
            64,
            t_w,
            0.12,
            tur="tik" if i_soz == 14 else None,
            guc=0.35,
        )
        k2_ids.add(f"w{i_soz}")

    # Olay 15: Kart 2 yukarı kayar
    t15 = s.S(T(17, "Hocam,")) - 0.42
    s.to("#k2", t15, {"y": K2_DY, "duration": 0.42, "ease": "power3.inOut"})

    # ----------------------------------------------------
    # Balon Grubu (#balg): Baş + Balon + Balon Sözcükleri + nk + cn
    # ----------------------------------------------------
    # Olay 16: Öğrenci başı
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text(encoding="utf-8")
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    bas_paths = "".join(f'<path id="bas{i}" d="{d}" style="opacity:0"/>' for i, d in enumerate(bd))
    s.svg.append(
        f'<g id="basm"><g id="basn"><g id="bas" transform="translate({BTX:.2f} {BTY:.2f}) scale({BS0:.4f})" '
        f'fill="none" stroke="{KRE}" stroke-width="{4.0 / BS0:.3f}" stroke-linecap="round" stroke-linejoin="round">'
        f'{bas_paths}</g></g></g>'
    )
    bal_ids.append("basm")

    t16 = s.S(T(17, "Hocam,")) - 0.10
    for i in range(3):
        t_b = t16 + 0.05 * i
        s.cmd.append({"m": "draw", "id": f"bas{i}", "t": round(t_b, 4), "d": 0.32, "a": 1})
        s.olay(t_b, "cizgi", 0.55)

    # Olay 17: Balon
    t17 = s.S(T(17, "Hocam,")) - 0.05
    s.yol(
        "bal",
        Y.balon_sol(BAL_X0, BAL_Y0, BAL_X1, BAL_Y1, BAL_TX, BAL_TY),
        t17,
        0.55,
        KRE,
        4.5,
        tur="cizgi",
        guc=0.7,
    )
    bal_ids.append("bal")

    # Olay 18 (DUZ2 A5): TR soru balonda yazılmaz (yalnız altyazıda, karaoke). Balonda EN anahtar `-ing?`:
    # `?` "mu?" sözüyle, `-ing` "-ing" sözüyle (ekran sesten önce gelmez).
    b_bal = 120.0
    g_ing = g_f700("-ing", b_bal)
    g_bal = g_f700("-ing?", b_bal)
    x_bal = (BAL_WX + BAL_X1 - 36.0) / 2.0 - g_bal / 2.0
    y_bal = (BAL_Y0 + BAL_Y1) / 2.0 + 0.36 * b_bal
    s.yazi("bw23", x_bal + g_ing, y_bal, [("?", KRE)], "Fredoka", 700, b_bal, s.S(T(23, "mu?")), 0.12, guc=0.4)
    s.yazi("bw25", x_bal, y_bal, [("-ing", KRE)], "Fredoka", 700, b_bal, s.S(T(25, "-ing")), 0.16, guc=0.45)
    bal_ids.extend(["bw23", "bw25"])
    assert x_bal >= BAL_WX and x_bal + g_bal <= BAL_X1 - 36.0, f"balon yazısı taştı: {x_bal}..{x_bal + g_bal}"

    # Olay 19: Sarı nokta nk
    t19 = s.S(T(24, "Neden"))
    s.yol("nk", f"M {CN_X:.1f} {CN_Y:.1f} L {CN_X + 0.1:.1f} {CN_Y:.1f}", t19, 0.12, SAR, 18.0, tur="tik", guc=0.45)
    bal_ids.append("nk")

    # Olay 20: Bağ cn
    t20 = t19 + 0.14
    w_leaves = g_f700("leaves")
    XU1 = round(K1_TX + 0.75 * w_leaves, 1)
    ok1 = f"L {XU1 + 19.0:.1f} {BAG_Y - 10.5:.1f} L {XU1:.1f} {BAG_Y:.1f} L {XU1 + 19.0:.1f} {BAG_Y + 10.5:.1f}"
    d_cn = (
        f"M {CN_X:.1f} {CN_Y:.1f} L {CN_X:.1f} 720 Q {CN_X:.1f} {BAG_Y:.1f} {CN_X - 16.0:.1f} {BAG_Y:.1f} "
        f"L {XU1:.1f} {BAG_Y:.1f} {ok1}"
    )
    s.yol("cn", d_cn, t20, 0.45, SAR, 6.0, alfa=0.9, tur="cizgi", guc=0.45)
    bal_ids.append("cn")

    # Olay 21: Balon grubu söner
    t21 = s.S(T(27, "Biletimi"))
    s.to("#balg", t21, {"opacity": 0, "duration": 0.35, "ease": "power2.in"})
    s.olay(t21, "vurus", 0.5)

    # ----------------------------------------------------
    # Öğretmen + Sonraki Öğeler (C konumu)
    # ----------------------------------------------------
    # Olay 22: Öğretmen
    x0, y0, x1, y1 = FIG["kutu"]
    fs = FIG_FS_H / (y1 - y0)
    tx_fig = 72.0 - x0 * fs
    ty_fig = FY0 - y0 * fs
    HX = 72.0 + (FIG["el"][0] - x0) * fs
    HY = FY0 + (FIG["el"][1] - y0) * fs
    fig_w_map = {"govde": 4.4, "sac": 3.6, "yuz": 2.6}
    fig_paths = "".join(
        f'<path id="fg{i}" d="{p["d"]}" stroke-width="{fig_w_map.get(p["parca"], 4.4) / fs:.3f}" style="opacity:0"/>'
        for i, p in enumerate(FIG["yollar"])
    )
    s.svg.append(
        f'<g id="fig" transform="translate({tx_fig:.2f} {ty_fig:.2f}) scale({fs:.6f})" fill="none" '
        f'stroke="{KRE}" stroke-linecap="round" stroke-linejoin="round">{fig_paths}</g>'
    )

    t22 = t21 + 0.04
    fig_uzunluklar = [Y.yol_uzunluk(p["d"]) for p in FIG["yollar"]]
    fig_zamanlar = Y.cizgi_zamanlari(fig_uzunluklar, t22, t22 + 0.50)
    for i, (b, d_sure) in enumerate(fig_zamanlar):
        s.cmd.append({"m": "draw", "id": f"fg{i}", "t": b, "d": d_sure, "a": 1})
        if i == 0:
            s.olay(b, "cizgi", 0.5)

    # Olay 23: Bağ öğretmenin eli -> am going (sarı ok) + ikiz ("kesin" çapası)
    t23 = s.S(T(31, "kesin"))
    XG = K2_TX + g_f700("I ")
    WG = g_f700("am going")
    d_ok_fig = ok_tek(HX + 10.0, HY - 14.0, XG + WG / 2.0, OK_FIG_BITIS_Y, 2.0)
    s.yol("ok_fig", d_ok_fig, t23, 0.40, SAR, 8.0, tur="cizgi", guc=0.55)
    s.yol("ok_fig_s", d_ok_fig, t23, 0.40, IKN, 8.0, alfa=0.0, tur=None)

    # Olay 24: am going odak (sarı altçizgi) + ikiz
    t24 = t23 + 0.40
    d_krm = Y.el_cizgi(XG - 2.0, KRM_Y, XG + WG + 2.0, KRM_Y, 1.0)
    s.yol("krm", d_krm, t24, 0.30, SAR, 10.0, tur="cizgi", guc=0.55)
    s.yol("krm_s", d_krm, t24, 0.30, IKN, 10.0, alfa=0.0, tur=None)

    # Olay 25 (DUZ2 A3): kart 2 etiketi `kesin düzenleme` (TR, soluk; seste aynı terim)
    t25 = s.S(T(32, "düzenleme,"))
    m_lp = "kesin düzenleme"
    s.yazi("lp0", LP_X, LP_TABAN, [(m_lp, IKN)], "Caveat", 700, 64, t25, 0.35, tur="tik", guc=0.4)

    # Olay 27: Önceki sarı griye döner
    t27 = s.S(T(35, "Tren"))
    soldur(s, "ok_fig", "ok_fig_s", t27, 0.25)
    soldur(s, "krm", "krm_s", t27, 0.25)

    # Olay 28: Bağ tren -> leaves (sarı) + ikiz
    t28 = t27
    d_ok_trn = (
        f"M {TRX:.1f} {TRN_KUTU[3] + 9.0:.1f} L {TRX:.1f} 688 Q {TRX:.1f} {BAG_Y:.1f} {TRX - 16.0:.1f} {BAG_Y:.1f} "
        f"L {XU1:.1f} {BAG_Y:.1f} {ok1}"
    )
    s.yol("ok_trn", d_ok_trn, t28, 0.60, SAR, 8.0, tur="cizgi", guc=0.55)
    s.yol("ok_trn_s", d_ok_trn, t28, 0.60, IKN, 8.0, alfa=0.0, tur=None)

    # Olay 29 (DUZ2 A3): kart 1 etiketi `tarife` (TR, soluk; seste "tarifeye")
    t29 = s.S(T(36, "tarifeye"))
    m_lt = "tarife"
    s.yazi("lt0", LT_X, LT_TABAN, [(m_lt, IKN)], "Caveat", 700, 64, t29, 0.25, tur="tik", guc=0.4)

    # Olay 31: Tren bağı griye döner + leaves odak (sarı)
    t31 = s.S(T(38, "geniş"))
    soldur(s, "ok_trn", "ok_trn_s", t31, 0.25)
    d_klm = Y.el_cizgi(95.0, KLM_Y, K1_TX + w_leaves + 2.0, KLM_Y, 1.0)
    s.yol("klm", d_klm, t31, 0.30, SAR, 10.0, tur="cizgi", guc=0.5)

    # ----------------------------------------------------
    # Altyazı aç/kapa
    # ----------------------------------------------------
    dilimler = altyazi_dilimleri_k()

    acik0: list[int] = []  # 0'da açık dilim: GSAP seek(0) 0. sn set'ini uygulamaz -> baştan görünür yazılır
    for i, (t0_alt, t1_alt, _) in enumerate(dilimler):
        t_ac = max(0.0, round(s.S(t0_alt) - 0.05, 4))
        if t_ac > 0:
            s.set(f"#alt{i}", t_ac, {"opacity": 1})
        else:
            acik0.append(i)
        if i < len(dilimler) - 1:
            sonraki_t0 = dilimler[i + 1][0]
            t_kapa = round(min(s.S(t1_alt) + 0.35, s.S(sonraki_t0) - 0.05), 4)
            if t_kapa <= 0:
                continue
            if t_kapa < Z["sure"]:
                s.set(f"#alt{i}", t_kapa, {"opacity": 0})

    # Karaoke (DUZ2 A5; sahne 03 düzeni): söylenmemiş sözcük ikincil, sözcük t0'ında mürekkep. 0'da açık dilim
    # sahne 01'in devamıdır (sahne 01 karaokesiz, mürekkep): kesmede renk sıçramasın diye baştan mürekkep.
    for i, (_, _, sozler) in enumerate(dilimler):
        for k, (_, w_t0) in enumerate(sozler):
            t_k = s.S(w_t0)
            if i not in acik0 and t_k > 0:
                s.set(f"#alt{i}w{k}", t_k, {"attr": {"fill": KRE}})
    alt_svg = altyazi_v2_svg([
        {"id": f"alt{i}", "sozler": [w for w, _ in sozler],
         "renk": [KRE if (i in acik0 or s.S(t) <= 0) else IKN for _, t in sozler]}
        for i, (_, _, sozler) in enumerate(dilimler)
    ])
    for i in acik0:
        assert f'<g id="alt{i}" style="opacity:0">' in alt_svg, "altyazı biçimi değişti"
        alt_svg = alt_svg.replace(f'<g id="alt{i}" style="opacity:0">', f'<g id="alt{i}">', 1)

    # ----------------------------------------------------
    # Denetimler (SPEC §6)
    # ----------------------------------------------------
    # 1. kart 1 satır 1 sağ ucu <= 719 - 24; satır 2 sağ ucu <= 950 - 40; kart 2 satır 1 sağ ucu <= bilet sol ucu - 24.
    s1_sag = K1_TX + g_f700("The train to İzmir")
    s2_sag = K1_TX + g_f700("leaves at 7 pm today.")
    k2_s1_sag = K2_TX + g_f700("I am going to the")
    _, kenar_noktalari_A = bilet_verisi(BCX_BIL, BCY_BIL)
    bilet_sol_A = min(p[0] for p in kenar_noktalari_A) - 2.25
    bilet_sag_A = max(p[0] for p in kenar_noktalari_A) + 2.25
    bilet_ust_A = min(p[1] for p in kenar_noktalari_A) - 2.25
    bilet_alt_A = max(p[1] for p in kenar_noktalari_A) + 2.25

    assert s1_sag <= TRN_KUTU[0] - 24.0, f"kart 1 satir 1 sağ ucu taştı: {s1_sag} > {TRN_KUTU[0] - 24.0}"
    assert s2_sag <= K1_X + K1_W - 40.0, f"kart 1 satir 2 sağ ucu taştı: {s2_sag} > {K1_X + K1_W - 40.0}"
    assert k2_s1_sag <= bilet_sol_A - 24.0, f"kart 2 satir 1 sağ ucu taştı: {k2_s1_sag} > {bilet_sol_A - 24.0}"

    # 2. üst etiketler arası (now <-> 7 pm, 7 pm <-> tonight) >= 24; tg1 sağ ucu ile tg2 sol ucu arası >= 24;
    #    tg2 sağ ucu <= 948; tl_now sol ucu >= 60.
    now_sag = x_now + g_c700("now")
    yedi_sol = x_7pm
    yedi_sag = x_7pm + g_c700("7 pm")
    tonight_sol = x_tl_t
    assert yedi_sol - now_sag >= 24.0, f"now ve 7 pm arası < 24: {yedi_sol - now_sag}"
    assert tonight_sol - yedi_sag >= 24.0, f"7 pm ve tonight arası < 24: {tonight_sol - yedi_sag}"

    tg1_sag = x_tg1 + g_c700(m_tg1)
    tg2_sol = x_tg2
    tg2_sag = x_tg2 + g_c700(m_tg2)
    assert tg2_sol - tg1_sag >= 24.0, f"tg1 ve tg2 arası < 24: {tg2_sol - tg1_sag}"
    assert tg2_sag <= 948.0, f"tg2 sağ ucu taştı: {tg2_sag} > 948.0"
    assert x_now >= 60.0, f"tl_now sol ucu taştı: {x_now} < 60.0"

    # 3. bağ koridoru: kart 2 satır 2 sağ ucu + 10 <= CN_X - 3;
    #    bilet sol ucu (kenar noktalarından hesapla, - 2,25 çizgi payı) >= CN_X + 3 + 10.
    k2_s2_sag = K2_TX + g_f700("movie theater tonight.")
    assert k2_s2_sag + 10.0 <= CN_X - 3.0, f"kart 2 satır 2 bağ koridoruna taştı: {k2_s2_sag + 10.0} > {CN_X - 3.0}"
    assert bilet_sol_A >= CN_X + 3.0 + 10.0, f"bilet sol ucu bağ koridoruna taştı: {bilet_sol_A} < {CN_X + 3.0 + 10.0}"

    # 4. balon satırı sağ ucu <= 954 - 36; baş sağ ucu (BTX + 195*BS0; viewBox x -45..195) < balon kuyruk ucu x 214.
    bas_sag = BTX + 195.0 * BS0
    assert bas_sag < BAL_TX, f"baş sağ ucu balon kuyruğuna taştı: {bas_sag} >= {BAL_TX}"

    # 5. kesin düzenleme ve tarife etiketi sağ ucu <= 760; öğretmen sağ ucu <= 290, altı <= 1380.
    assert LP_X + g_c700(m_lp) <= 760.0, "kesin düzenleme etiketi sağ ucu taştı"
    assert LT_X + g_c700(m_lt) <= 760.0, "tarife etiketi sağ ucu taştı"
    assert tx_fig + x1 * fs <= 290.0, f"öğretmen sağ ucu taştı: {tx_fig + x1 * fs} > 290.0"
    assert ty_fig + y1 * fs <= 1380.0, f"öğretmen altı taştı: {ty_fig + y1 * fs} > 1380.0"

    # 6. XU1 <= 97 + g("leaves").
    assert XU1 <= K1_TX + w_leaves, "XU1 leaves sağ ucu dışına taştı"

    # 7. içerik sınırı: her kart çerçevesi [x - 9, x + w + 9] x [y - 9, y + h + 9] (kutu taşması),
    #    tren kutusu, bilet (A ve B), balon [x0, x1 + 4] x [y0 - 6, y1 + 6], baş, öğretmen
    #    -> hepsi x 60–960 ve y 460–1380 içinde.
    def sinir_denetle(ad: str, x0: float, y0: float, x1: float, y1: float) -> None:
        assert x0 >= X_MIN, f"{ad} sol sınırı aştı: {x0} < {X_MIN}"
        assert x1 <= X_MAX, f"{ad} sağ sınırı aştı: {x1} > {X_MAX}"
        assert y0 >= Y_MIN, f"{ad} üst sınırı aştı: {y0} < {Y_MIN}"
        assert y1 <= Y_MAX, f"{ad} alt sınırı aştı: {y1} > {Y_MAX}"

    sinir_denetle("kart 1", K1_X - 9.0, K1_Y - 9.0, K1_X + K1_W + 9.0, K1_Y + K1_H + 9.0)
    sinir_denetle("kart 2 (A)", K2_X - 9.0, K2_Y_A - 9.0, K2_X + K2_W + 9.0, K2_Y_A + K2_H + 9.0)
    sinir_denetle("kart 2 (B)", K2_X - 9.0, K2_Y_A + K2_DY - 9.0, K2_X + K2_W + 9.0, K2_Y_A + K2_DY + K2_H + 9.0)
    sinir_denetle("tren kutusu", TRN_KUTU[0], TRN_KUTU[1], TRN_KUTU[2], TRN_KUTU[3])
    sinir_denetle("bilet (A)", bilet_sol_A, bilet_ust_A, bilet_sag_A, bilet_alt_A)

    _, kenar_noktalari_B = bilet_verisi(BCX_BIL, BCY_BIL + K2_DY)
    bilet_sol_B = min(p[0] for p in kenar_noktalari_B) - 2.25
    bilet_sag_B = max(p[0] for p in kenar_noktalari_B) + 2.25
    bilet_ust_B = min(p[1] for p in kenar_noktalari_B) - 2.25
    bilet_alt_B = max(p[1] for p in kenar_noktalari_B) + 2.25
    sinir_denetle("bilet (B)", bilet_sol_B, bilet_ust_B, bilet_sag_B, bilet_alt_B)

    sinir_denetle("balon", BAL_X0, BAL_Y0 - 6.0, BAL_X1 + 4.0, BAL_Y1 + 6.0)
    sinir_denetle("baş", BTX - 45.0 * BS0, BTY, BTX + 195.0 * BS0, BTY + 330.0 * BS0)
    sinir_denetle("öğretmen", tx_fig + x0 * fs, ty_fig + y0 * fs, tx_fig + x1 * fs, ty_fig + y1 * fs)

    return s, {
        "kun": kunye_v2(),
        "bal_ids": bal_ids,
        "gruplar": [("zc", zc_ids), ("k2", k2_ids)],
        "alt": alt_svg,
    }


if __name__ == "__main__":
    s, p = uret()
    Y.kontrol(s, Z["kare"])
    (AD / "proje").mkdir(exist_ok=True)
    logo = (53.2, 291, 193.5, 48)
    html_icerik = (
        Y.html(
            s,
            Z["sure"],
            p["kun"],
            None,
            logo,
            ek=p["alt"],
            bal_ids=p["bal_ids"],
            gruplar=p["gruplar"],
        ).replace("</style>", "#icerik text{font-kerning:none}\n</style>", 1)
    )

    eski_logo = (
        '<g id="logo"><image id="logoimg" href="assets/logo.svg" x="53.2" y="291" width="193.50" height="48"/></g>'
    )
    assert eski_logo in html_icerik, "logo deseni bulunamadı"
    yeni_logo = (
        '<g id="logo"><g id="kanal">'
        '<image id="logoimg" href="assets/logo.svg" x="53.2" y="291" width="193.50" height="48"/>'
        f'<text id="kanal-ad" x="263" y="330" font-family="Lexend" font-weight="700" font-size="42" '
        f'fill="{KRE}" xml:space="preserve">@ydspublishing</text>'
        '</g></g>'
    )
    html_icerik = html_icerik.replace(eski_logo, yeni_logo, 1)

    (AD / "proje" / "index.html").write_text(html_icerik, encoding="utf-8")
    print(f"index.html yazıldı; komut {len(s.cmd)} olay {len(s.ev)}")

"""Sahne 02 — Örnek (02-04-ydt-temel-s3 shorts, HyperFrames DİKEY 1080x1920, 402 kare, t_bas 3.00).

Tasarım: SPEC.md (şef); kod agy-filo (15.11.2026).
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
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
TB = Z["t_bas"]

SOZ = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))

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
    27: "Planı",
    28: "bir",
    29: "kişi",
    30: "yapar.",
    31: "Tren",
    32: "tarifeye",
    33: "uyar:",
    34: "geniş",
    35: "zaman.",
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
assert SOZ[28]["t0"] == 12.07
assert SOZ[29]["t0"] == 12.31
assert SOZ[30]["t0"] == 12.51
assert SOZ[31]["t0"] == 13.43
assert SOZ[32]["t0"] == 13.83
assert SOZ[34]["t0"] == 15.19
assert SOZ[35]["t1"] == 16.07


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


def kunye_tam() -> str:
    CIP = "Example"
    w_pc = g_f700("PRESENT CONTINUOUS", 56)
    rx = 48.0 + w_pc + 24.0
    rw = g_l700("YDT · BASIC", 36) + 56.0
    cw = g_l700(CIP, 40) + 64.0
    cx = 1032.0 - cw
    return (
        '<g id="kunye">'
        f'<text id="ku-ders1" x="48" y="212" font-family="Fredoka" font-weight="700" font-size="56" fill="{KRE}" '
        f'xml:space="preserve">SIMPLE PRESENT vs</text>'
        f'<text id="ku-ders2" x="48" y="276" font-family="Fredoka" font-weight="700" font-size="56" fill="{KRE}" '
        f'xml:space="preserve">PRESENT CONTINUOUS</text>'
        f'<g id="ku-rz"><rect x="{rx:.2f}" y="216" width="{rw:.2f}" height="72" rx="36" fill="{SAR}"/>'
        f'<text x="{rx + rw / 2.0:.2f}" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" '
        f'font-size="36" fill="{ZEM}" xml:space="preserve">YDT · BASIC</text></g>'
        f'<g id="ku-bolum"><rect x="{cx:.2f}" y="48" width="{cw:.2f}" height="80" rx="40" fill="none" stroke="{SAR}" '
        f'stroke-width="4"/>'
        f'<text x="{cx + cw / 2.0:.2f}" y="102" text-anchor="middle" font-family="Lexend" font-weight="700" '
        f'font-size="40" fill="{SAR}" xml:space="preserve">{CIP}</text></g>'
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
        f'<g id="tren" transform="translate(790 404) scale(0.5)" fill="none" '
        f'stroke-linecap="round" stroke-linejoin="round">{ic}</g>'
    )


def bilet_yollari() -> list[tuple[str, str, float]]:
    BS_BIL = 0.55
    E_BIL = -0.06
    BCX_BIL = 900.0
    BCY_BIL = 926.0
    ce_bil = math.cos(E_BIL)
    se_bil = math.sin(E_BIL)

    def P(x: float, y: float) -> tuple[float, float]:
        return (
            round(BCX_BIL + BS_BIL * (x * ce_bil - y * se_bil), 2),
            round(BCY_BIL + BS_BIL * (x * se_bil + y * ce_bil), 2),
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


def uret() -> tuple[Y.Sahne, dict]:
    s = Y.Sahne(TB)
    zc_ids: set[str] = set()
    k2_ids: set[str] = set()
    bal_ids: list[str] = []

    # ----------------------------------------------------
    # Olay 0: Kare 0 = sahne 01 son karesi (statik)
    # ----------------------------------------------------
    kc_kenarlar = kutu(57, 368, 966, 260, 71)
    for i, kenar in enumerate(kc_kenarlar):
        s.svg.append(statik(f"kc{i}", kutu_kenar_to_d(kenar), KRE, 4.0))

    s.svg.append(tren_svg())

    s.svg.append(metin("r1", 97, 468, "The train to İzmir", "Fredoka", 700, 64, KRE))
    s.svg.append(metin("r2", 97, 566, "leaves at 7", "Fredoka", 700, 64, KRE))

    # ----------------------------------------------------
    # Olay 1: pm yazımı
    # ----------------------------------------------------
    t1 = max(0.40, s.S(T(7, "p.m.")))
    x_w7 = 97.0 + g_f700("leaves at 7 ")
    s.yazi("w7", x_w7, 566, [("pm", KRE)], "Fredoka", 700, 64, t1, 0.12, tur="tik", guc=0.4)

    # ----------------------------------------------------
    # Olay 2: today. yazımı
    # ----------------------------------------------------
    t2 = max(max(0.40, s.S(T(8, "today."))), t1 + 0.12)
    x_w8 = 97.0 + g_f700("leaves at 7 pm ")
    s.yazi("w8", x_w8, 566, [("today.", KRE)], "Fredoka", 700, 64, t2, 0.12, tur=None)

    # ----------------------------------------------------
    # Zaman Çizgisi Grubu (#zc) Öğeleri
    # ----------------------------------------------------
    # Olay 3: Zaman çizgisi ekseni
    t3 = t2
    s.yol("tx", ok_tek(72, 748, 1008, 748, 0.5), t3, 0.30, IKN, 4.5)
    zc_ids.add("tx")

    # Olay 4: now noktası + now
    t4 = t2 + 0.08
    s.svg.append(f'<circle id="tn_now" cx="150" cy="748" r="11" fill="{KRE}" style="opacity:0"/>')
    s.fromto("#tn_now", t4, {"opacity": 0}, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    zc_ids.add("tn_now")
    x_now = 150.0 - g_c700("now") / 2.0
    s.yazi("tl_now", x_now, 708, [("now", KRE)], "Caveat", 700, 64, t4, 0.2)
    zc_ids.add("tl_now")

    # Olay 5: 7 pm çentiği + nokta + 7 pm
    t5 = t2 + 0.20
    s.yol("t7c", "M 400 730 L 400 766", t5, 0.12, KRE, 4.5)
    zc_ids.add("t7c")
    s.svg.append(f'<circle id="tn_7" cx="400" cy="748" r="9" fill="{KRE}" style="opacity:0"/>')
    s.fromto("#tn_7", t5, {"opacity": 0}, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    zc_ids.add("tn_7")
    x_7pm = 400.0 - g_c700("7 pm") / 2.0
    s.yazi("tl_7", x_7pm, 708, [("7 pm", KRE)], "Caveat", 700, 64, t5 + 0.04, 0.2)
    zc_ids.add("tl_7")

    # Olay 6: now -> 7 pm kalem oku (yay)
    t6 = t2 + 0.28
    a_tok = math.atan2(738.0 - 696.0, 388.0 - 277.0)
    k_tok = 18.0
    u1_x = 388.0 - k_tok * math.cos(a_tok - 0.5)
    u1_y = 738.0 - k_tok * math.sin(a_tok - 0.5)
    u2_x = 388.0 - k_tok * math.cos(a_tok + 0.5)
    u2_y = 738.0 - k_tok * math.sin(a_tok + 0.5)
    d_tok = f"M 168 736 Q 277 696 388 738 L {u1_x:.1f} {u1_y:.1f} L 388 738 L {u2_x:.1f} {u2_y:.1f}"
    s.yol("tok", d_tok, t6, 0.35, KRE, 4.5)
    zc_ids.add("tok")

    # Olay 7: 7 pm sarı daire
    t7 = t2 + 0.58
    s.yol("t7d", Y.el_daire(400, 688, 80, 38, 0.6), t7, 0.30, SAR, 6.0, tur="cizgi", guc=0.5)
    zc_ids.add("t7d")

    # Olay 8: gelecek · V-s
    t8 = t2 + 0.63
    m_tg1 = "gelecek · V-s"
    x_tg1 = 400.0 - g_c700(m_tg1) / 2.0
    s.yazi("tg1", x_tg1, 824, [(m_tg1, KRE)], "Caveat", 700, 64, t8, 0.30)
    zc_ids.add("tg1")

    # Olay 13: tonight noktası + tonight + gelecek · am + V-ing
    t13 = s.S(T(16, "tonight."))
    s.svg.append(f'<circle id="tn_t" cx="790" cy="748" r="11" fill="{KRE}" style="opacity:0"/>')
    s.fromto("#tn_t", t13, {"opacity": 0}, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    zc_ids.add("tn_t")
    x_tl_t = 790.0 - g_c700("tonight") / 2.0
    s.yazi("tl_t", x_tl_t, 708, [("tonight", KRE)], "Caveat", 700, 64, t13 + 0.05, 0.2, tur=None)
    zc_ids.add("tl_t")
    m_tg2 = "gelecek · am + V-ing"
    x_tg2 = 790.0 - g_c700(m_tg2) / 2.0
    s.yazi("tg2", x_tg2, 824, [(m_tg2, KRE)], "Caveat", 700, 64, t13 + 0.17, 0.30, tur="tik", guc=0.45)
    zc_ids.add("tg2")

    # Olay 14: Zaman çizgisi grubu söner
    t14 = s.S(T(17, "Hocam,")) - 0.50
    s.to("#zc", t14, {"opacity": 0, "duration": 0.25, "ease": "power2.in"})

    # ----------------------------------------------------
    # Kart 2 Grubu (#k2) Öğeleri (A konumu)
    # ----------------------------------------------------
    # Olay 9: Kart 2 çerçevesi
    t9 = s.S(T(9, "I")) - 0.30
    kd_kenarlar = kutu(57, 860, 966, 260, 72)
    kd_zamanlar = Y.cizgi_zamanlari([966, 260, 966, 260], t9, t9 + 0.30)
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
        x_w = 97.0 + g_f700(cur_prefix)
        cur_prefix += w_text + " "
        s.yazi(
            f"w{i_soz}",
            x_w,
            960,
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
        x_w = 97.0 + g_f700(cur_prefix2)
        cur_prefix2 += w_text + " "
        s.yazi(
            f"w{i_soz}",
            x_w,
            1058,
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
    s.to("#k2", t15, {"y": -124, "duration": 0.42, "ease": "power3.inOut"})

    # ----------------------------------------------------
    # Balon Grubu (#balg): Baş + Balon + Balon Sözcükleri + nk + cn
    # ----------------------------------------------------
    # Olay 16: Öğrenci başı
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text(encoding="utf-8")
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS0 = 240.0 / 330.0
    BTX = 72.0 + 45.0 * BS0
    BTY = 1090.0
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
    s.yol("bal", Y.balon_sol(300, 1040, 996, 1340, 252, 1290), t17, 0.55, KRE, 4.5, tur="cizgi", guc=0.7)
    bal_ids.append("bal")

    # Olay 18: Balon sözcükleri (bw17..bw26)
    balon_satirlar = [
        (17, 18, 19, 20),
        (21, 22, 23),
        (24, 25, 26),
    ]
    tabanlar_balon = [1124, 1208, 1292]
    sp_balon = g_f600(" ")
    for sat_indices, taban in zip(balon_satirlar, tabanlar_balon):
        cur_x = 340.0
        for idx in sat_indices:
            w_text = SOZ[idx]["sozcuk"]
            w_len = g_f600(w_text)
            t_bw = s.S(T(idx))
            s.yazi(
                f"bw{idx}",
                cur_x,
                taban,
                [(w_text, KRE)],
                "Fredoka",
                600,
                64,
                t_bw,
                0.12,
                tur="tik" if idx in (17, 21, 24) else None,
                guc=0.4,
            )
            bal_ids.append(f"bw{idx}")
            cur_x += w_len + sp_balon
        assert cur_x - sp_balon <= 956.0, f"Balon satırı sağ ucu taştı: {cur_x - sp_balon} > 956"

    # Olay 19: Sarı nokta nk
    t19 = s.S(T(24, "Neden"))
    s.yol("nk", "M 768 1036 L 768.1 1036", t19, 0.12, SAR, 18.0, tur="tik", guc=0.45)
    bal_ids.append("nk")

    # Olay 20: Bağ cn
    t20 = t19 + 0.14
    w_leaves = g_f700("leaves")
    XU1 = round(97.0 + 0.75 * w_leaves, 1)
    ok1 = f"L {XU1 + 19.0:.1f} 593.5 L {XU1:.1f} 604.0 L {XU1 + 19.0:.1f} 614.5"
    d_cn = f"M 768 1036 L 768 620 Q 768 604 752 604 L {XU1:.1f} 604.0 {ok1}"
    s.yol("cn", d_cn, t20, 0.45, SAR, 6.0, alfa=0.9, tur="cizgi", guc=0.45)
    bal_ids.append("cn")

    # Olay 21: Balon grubu söner
    t21 = s.S(T(27, "Planı"))
    s.to("#balg", t21, {"opacity": 0, "duration": 0.35, "ease": "power2.in"})
    s.olay(t21, "vurus", 0.5)

    # ----------------------------------------------------
    # Öğretmen + Sonraki Öğeler (C konumu)
    # ----------------------------------------------------
    # Olay 22: Öğretmen
    x0, y0, x1, y1 = FIG["kutu"]
    fs = 380.0 / (y1 - y0)
    tx_fig = 72.0 - x0 * fs
    ty_fig = 1010.0 - y0 * fs
    HX = 72.0 + (FIG["el"][0] - x0) * fs
    HY = 1010.0 + (FIG["el"][1] - y0) * fs
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

    # Olay 23: Bağ öğretmenin eli -> am going (sarı ok) + ikiz
    t23 = s.S(T(28, "bir"))
    XG = 97.0 + g_f700("I ")
    WG = g_f700("am going")
    d_ok_fig = ok_tek(HX + 10.0, HY - 14.0, XG + WG / 2.0, 1010.0, 2.0)
    s.yol("ok_fig", d_ok_fig, t23, 0.40, SAR, 8.0, tur="cizgi", guc=0.55)
    s.yol("ok_fig_s", d_ok_fig, t23, 0.40, IKN, 8.0, alfa=0.0, tur=None)

    # Olay 24: am going odak (sarı altçizgi) + ikiz
    t24 = t23 + 0.40
    d_krm = Y.el_cizgi(XG - 2.0, 867.0, XG + WG + 2.0, 867.0, 1.0)  # taban 836 + 0,48·64 (g kuyruğu; sözleşme)
    s.yol("krm", d_krm, t24, 0.30, SAR, 10.0, tur="cizgi", guc=0.55)
    s.yol("krm_s", d_krm, t24, 0.30, IKN, 10.0, alfa=0.0, tur=None)

    # Olay 25: person
    t25 = s.S(T(29, "kişi"))
    s.yazi("lp0", 300, 1080, [("person", KRE)], "Caveat", 700, 64, t25, 0.30, tur="tik", guc=0.4)

    # Olay 26: etiket oku + plan
    t26 = s.S(T(30, "yapar."))
    xa = 300.0 + g_c700("person") + 16.0
    s.yol("lpo", ok_tek(xa, 1058, xa + 56.0, 1058, 0.5), t26, 0.20, KRE, 4.5)
    s.yazi("lp1", xa + 72.0, 1080, [("plan", KRE)], "Caveat", 700, 64, t26 + 0.15, 0.30)

    # Olay 27: Önceki sarı griye döner
    t27 = s.S(T(31, "Tren"))
    soldur(s, "ok_fig", "ok_fig_s", t27, 0.25)
    soldur(s, "krm", "krm_s", t27, 0.25)

    # Olay 28: Bağ tren -> leaves (sarı) + ikiz
    t28 = t27
    d_ok_trn = f"M 892.5 492 L 892.5 588 Q 892.5 604 876.5 604 L {XU1:.1f} 604.0 {ok1}"
    s.yol("ok_trn", d_ok_trn, t28, 0.60, SAR, 8.0, tur="cizgi", guc=0.55)
    s.yol("ok_trn_s", d_ok_trn, t28, 0.60, IKN, 8.0, alfa=0.0, tur=None)

    # Olay 29: train
    t29 = t27 + 0.10
    s.yazi("lt0", 97, 694, [("train", KRE)], "Caveat", 700, 64, t29, 0.30, tur="tik", guc=0.4)

    # Olay 30: etiket oku + timetable
    t30 = s.S(T(32, "tarifeye"))
    xb = 97.0 + g_c700("train") + 16.0
    s.yol("lto", ok_tek(xb, 672, xb + 56.0, 672, 0.5), t30, 0.20, KRE, 4.5)
    s.yazi("lt1", xb + 72.0, 694, [("timetable", KRE)], "Caveat", 700, 64, t30 + 0.15, 0.30)

    # Olay 31: Tren bağı griye döner + leaves odak (sarı)
    t31 = s.S(T(34, "geniş"))
    soldur(s, "ok_trn", "ok_trn_s", t31, 0.25)
    d_klm = Y.el_cizgi(95.0, 584.0, 97.0 + w_leaves + 2.0, 584.0, 1.0)
    s.yol("klm", d_klm, t31, 0.30, SAR, 10.0, tur="cizgi", guc=0.5)

    # ----------------------------------------------------
    # Altyazı aç/kapa
    # ----------------------------------------------------
    dilimler = []
    for t0_alt, t1_alt, m_alt in Y.altyazi_dilimleri([1, 2, 3]):
        dilimler.append((t0_alt, t1_alt, cevir_ekran(m_alt)))

    acik0: list[int] = []  # 0'da açık dilim: GSAP seek(0) 0. sn set'ini uygulamaz → baştan görünür yazılır
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

    alt_svg = Y.altyazi_svg([{"id": f"alt{i}", "metin": m} for i, (_, _, m) in enumerate(dilimler)])
    for i in acik0:
        assert f'<g id="alt{i}" style="opacity:0">' in alt_svg, "altyazı biçimi değişti"
        alt_svg = alt_svg.replace(f'<g id="alt{i}" style="opacity:0">', f'<g id="alt{i}">', 1)

    # ----------------------------------------------------
    # Denetimler (SPEC §7)
    # ----------------------------------------------------
    assert 97.0 + g_f700("The train to İzmir") <= 785.0 - 24.0, "satir 1 sağ ucu taştı"
    assert 97.0 + g_f700("leaves at 7 pm today.") <= 1023.0 - 40.0, "satir 2 sağ ucu taştı"
    assert 790.0 + g_c700("gelecek · am + V-ing") / 2.0 <= 1032.0, "gelecek am+v-ing sağ ucu taştı"
    assert (400.0 - g_c700("7 pm") / 2.0) - (150.0 + g_c700("now") / 2.0) >= 24.0, "now ve 7 pm arası < 24"
    assert (790.0 - g_c700("tonight") / 2.0) - (400.0 + g_c700("7 pm") / 2.0) >= 24.0, "7 pm ve tonight arası < 24"
    assert xa + 72.0 + g_c700("plan") <= 760.0, "person -> plan sağ ucu taştı"
    assert xb + 72.0 + g_c700("timetable") <= 760.0, "train -> timetable sağ ucu taştı"
    assert tx_fig + x1 * fs <= 290.0, "ogretmen sağ ucu taştı"
    assert ty_fig + y1 * fs <= 1392.0, "ogretmen altı taştı"
    assert XU1 <= 97.0 + w_leaves, "XU1 leaves altı dışına taştı"

    return s, {
        "kun": kunye_tam(),
        "bal_ids": bal_ids,
        "gruplar": [("zc", zc_ids), ("k2", k2_ids)],
        "alt": alt_svg,
    }


if __name__ == "__main__":
    s, p = uret()
    Y.kontrol(s, Z["kare"])
    (AD / "proje").mkdir(exist_ok=True)
    logo = (48, 48, round(96 * Y.LOGO_EN_BOY, 2), 96)
    (AD / "proje" / "index.html").write_text(
        Y.html(
            s,
            Z["sure"],
            p["kun"],
            None,
            logo,
            ek=p["alt"],
            bal_ids=p["bal_ids"],
            gruplar=p["gruplar"],
        ).replace("</style>", "#icerik text{font-kerning:none}\n</style>", 1),  # sahne 01 ile aynı (devir.json)
        encoding="utf-8",
    )
    print(f"index.html yazıldı; komut {len(s.cmd)} olay {len(s.ev)}")

"""02-04-ydt-temel-s3 sahne 01 kapak index.html üretici (HyperFrames DİKEY 1080x1920, 102 kare).

SPEC.md §3 uygulaması: kapak düzeni, tren/saat/bilet/figür çizimleri, Fredoka cümle yazımı, başlık uçuşu,
kart çerçevesi çizimi ve devir.json çıktısı.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

# ---- 3.1 Okuma ----
Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
ORTAK = AD.parent.parent / "ortak"
SOZ = [
    w for w in json.loads((ORTAK / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 1
]
assert [w["sozcuk"] for w in SOZ[:7]] == ["The", "train", "to", "Izmir", "leaves", "at", "seven"], (
    f"Beklenen ilk 7 sözcük bulunamadı: {[w['sozcuk'] for w in SOZ[:7]]}"
)

EKRAN = {"Izmir": "İzmir", "seven p.m.": "7 pm"}
_raw_alt = json.loads((ORTAK / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
ALT = []
for _item in _raw_alt:
    _c = dict(_item)
    _m = _c["metin"]
    for _k, _v in EKRAN.items():
        _m = _m.replace(_k, _v)
    _c["metin"] = _m
    ALT.append(_c)

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
        u = i / n
        a = a0 + u * tur * math.pi * 2.0
        r = 1.0 + 0.06 * u + 0.025 * gurul(u * 5.0, tohum)
        x = rx * r * math.cos(a)
        y = ry * r * math.sin(a)
        cik.append((cx + x * ce - y * se, cy + x * se + y * ce))
    return cik


def kutu(x: float, y: float, w: float, h: float, tohum: int = 1) -> list[list[tuple[float, float]]]:
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
            a,
            (a[0] + dx / 2.0 - dy / L * bos, a[1] + dy / 2.0 + dx / L * bos),
            b,
        ]

    return [
        kenar((x - e(1), y + j(1)), (x + w + e(2), y + j(2)), 1),
        kenar((x + w + j(3), y - e(3)), (x + w + j(4), y + h + e(4)), 2),
        kenar((x + w + e(5), y + h + j(5)), (x - e(6), y + h + j(6)), 3),
        kenar((x + j(7), y + h + e(7)), (x + j(8), y - e(8)), 4),
    ]


def pts_to_d(pts: list[tuple[float, float]]) -> str:
    return f"M{pts[0][0]:.2f} {pts[0][1]:.2f} " + " ".join(f"L{p[0]:.2f} {p[1]:.2f}" for p in pts[1:])


def kutu_kenar_to_d(kenar: list[tuple[float, float]]) -> str:
    a, m, b = kenar
    return f"M{a[0]:.2f} {a[1]:.2f} Q{m[0]:.2f} {m[1]:.2f} {b[0]:.2f} {b[1]:.2f}"


# ---- 3.4 Sabitler ve Türetilen Ölçüler ----
W, H = Y.W, Y.H
KENAR = Y.HUD.get("kenar", 48) if hasattr(Y, "HUD") else 48
BAS1 = "TARİFE"
BAS2_METIN = "= PLAN"
PAD = 0.20  # em

B = math.floor(min(
    190,
    952 / Y.genislik("Fredoka", 700, BAS1, 1),
    952 / (Y.genislik("Fredoka", 700, BAS2_METIN, 1) + 2 * PAD),
))
g1 = Y.genislik("Fredoka", 700, BAS1, B)
t1x = (W - g1) / 2
T1 = 354 + 0.921 * B
ALTI_Y = T1 + 0.16 * B
HAP_UST = ALTI_Y + 29
T2 = HAP_UST + 0.88 * B
HAP_ALT = T2 + 0.18 * B

hap_w = Y.genislik("Fredoka", 700, BAS2_METIN, B) + 2 * PAD * B
hap_x = (W - hap_w) / 2
hap_h = HAP_ALT - HAP_UST
hap_rx = hap_h / 2

GX = hap_x + PAD * B
PX = GX + Y.genislik("Fredoka", 700, "= ", B)

SOL = 97
KB = 64
SATIR_ARA = 98
R1_K = 876
R2_K = R1_K + SATIR_ARA
R1_SON = 468
R2_SON = 566
DY = R1_SON - R1_K

ZEMIN_Y = 1384
TX = 58
TY = ZEMIN_Y - 158

SAAT_X, SAAT_Y, SAAT_R = 160, 1100, 72

FIG_H, FIG_X = 460, 600
x0, y0, x1, y1 = FIG["kutu"]
fs = FIG_H / (y1 - y0)
EX = FIG_X + (FIG["el"][0] - x0) * fs
EY = (ZEMIN_Y - FIG_H) + (FIG["el"][1] - y0) * fs

BS = 0.42
egim = -0.18
BCX = EX + BS * 150
BCY = EY - 6

E1_X = 380
E1_Y = 1080
E2_X = W - KENAR
E2_Y = 1080

SATIR1 = "The train to İzmir"
SATIR2_TAM = "leaves at 7 pm today."
SATIR2_KAPAK = "leaves at 7"

g_sat1 = Y.genislik("Fredoka", 700, SATIR1, KB)
g_sat2_tam = Y.genislik("Fredoka", 700, SATIR2_TAM, KB)
g_sat2_kapak = Y.genislik("Fredoka", 700, SATIR2_KAPAK, KB)

# Künye ve Uçuş Parametreleri
DERS = getattr(Y, "DERS", ("SIMPLE PRESENT vs", "PRESENT CONTINUOUS"))
ROZET = getattr(Y, "ROZET", "YDT · BASIC")

if hasattr(Y, "rozet_konumu"):
    rz_x, rz_w = Y.rozet_konumu()
else:
    rz_x = KENAR + Y.genislik("Fredoka", 700, DERS[-1], 56) + 24
    rz_w = Y.genislik("Lexend", 700, ROZET, 36) + 56

UK = 0.85
gd1 = Y.genislik("Fredoka", 700, DERS[0], 56)
gd2 = Y.genislik("Fredoka", 700, DERS[1], 56)
dersTaban = Y.HUD.get("dersTaban", 212) if hasattr(Y, "HUD") else 212
dersSatir = Y.HUD.get("dersSatir", 64) if hasattr(Y, "HUD") else 64

o1 = (t1x + g1 / 2, T1 - 0.35 * B)
h1 = (KENAR + UK * gd1 / 2, dersTaban - 0.35 * 56 - Z["ucus_ayrik"])
hs1 = UK * gd1 / g1

o2 = (540, (HAP_UST + HAP_ALT) / 2)
h2 = (KENAR + UK * gd2 / 2, dersTaban + dersSatir - 0.35 * 56 + Z["ucus_ayrik"])
hs2 = UK * gd2 / hap_w

o3 = (263.0, 1293.0)
h3 = (892.5, 437.5)
hs3 = Z["tren_olcek"]

# Tren uçuş sonu kutusu
tren_son_kutu = [
    h3[0] + hs3 * (48.0 - o3[0]),
    h3[1] + hs3 * (1202.0 - o3[1]),
    h3[0] + hs3 * (478.0 - o3[0]),
    h3[1] + hs3 * (1384.0 - o3[1]),
]


# ---- 3.9 Denetimler ----
def _denetimler() -> None:
    # 1. B, hap ve başlık 1
    assert 150 <= B <= 190, f"B={B} aralık [150, 190] dışı"
    assert hap_x >= 63 and hap_x + hap_w <= 1017, f"hap x={hap_x:.2f}..{hap_x + hap_w:.2f} aralık [63, 1017] dışı"
    assert t1x >= 63 and t1x + g1 <= 1017, f"baslik 1 x={t1x:.2f}..{t1x + g1:.2f} aralık [63, 1017] dışı"
    assert (T1 - 0.921 * B) >= 352, f"baslik 1 üstü {T1 - 0.921 * B:.2f} < 352"

    # 2. Satır metinleri
    assert len(SATIR1) <= 24, f"satir 1 {len(SATIR1)} > 24 karakter"
    assert len(SATIR2_TAM) <= 24, f"satir 2 tam {len(SATIR2_TAM)} > 24 karakter"
    assert SOL + g_sat2_tam <= 57 + 966 - 40, f"satir 2 tam {SOL + g_sat2_tam:.2f} > 983"

    # 3. Kapak dikey sıra (>= 24 px ara)
    r1_ust = R1_K - 0.921 * KB
    assert r1_ust - HAP_ALT >= 24, f"HAP_ALT -> satır 1 üstü ara {r1_ust - HAP_ALT:.2f} < 24"

    r1_alt = R1_K + 0.212 * KB
    fig_ust = ZEMIN_Y - FIG_H
    etk_ust = 1080 - 0.70 * 72
    saat_ust = SAAT_Y - 1.09 * SAAT_R
    assert min(fig_ust, etk_ust, saat_ust) - r1_alt >= 24, "satır 1 altı nesnelere < 24 px"

    etk_alt = 1080 + 0.25 * 72
    ce, se = math.cos(egim), math.sin(egim)
    bilet_kose_y = [BCY + BS * (kx * se + ky * ce) for kx, ky in [(-180, -70), (180, -70), (180, 70), (-180, 70)]]
    bilet_ust = min(bilet_kose_y)
    assert etk_alt + 12 <= bilet_ust, f"etiket altı + 12 = {etk_alt + 12:.2f} > bilet_ust = {bilet_ust:.2f}"
    tren_ust = 1202
    assert etk_alt + 24 <= tren_ust, f"leaves altı + 24 = {etk_alt + 24:.2f} > tren_ust = {tren_ust}"

    # 4. Yatay sıra (>= 20 px)
    g_am_going = Y.genislik("Caveat", 700, "am going", 72)
    g_leaves = Y.genislik("Caveat", 700, "leaves", 72)
    am_going_sol = 1032 - g_am_going
    fig_sag = FIG_X + (x1 - x0) * fs
    assert am_going_sol >= fig_sag + 20, f"am_going_sol {am_going_sol:.2f} < fig_sag + 20 ({fig_sag + 20:.2f})"
    leaves_sag = 380 + g_leaves / 2
    assert leaves_sag + 20 <= FIG_X, f"leaves_sag + 20 {leaves_sag + 20:.2f} > FIG_X ({FIG_X})"
    saat_sag = SAAT_X + 1.09 * SAAT_R
    leaves_sol = 380 - g_leaves / 2
    assert saat_sag + 20 <= leaves_sol, f"saat_sag + 20 {saat_sag + 20:.2f} > leaves_sol ({leaves_sol:.2f})"
    bilet_kose_x = [BCX + BS * (kx * ce - ky * se) for kx, ky in [(-180, -70), (180, -70), (180, 70), (-180, 70)]]
    bilet_sag = max(bilet_kose_x)
    assert bilet_sag <= W - KENAR, f"bilet_sag {bilet_sag:.2f} > {W - KENAR}"
    assert 478 + 20 <= FIG_X, f"tren sağı + 20 {498} > FIG_X {FIG_X}"

    # 5. Son hal
    assert R1_SON - 0.921 * KB >= 368 + 40, f"R1_SON üstü {R1_SON - 0.921 * KB:.2f} < 408"
    assert R2_SON + 0.48 * KB + 24 <= 368 + 260, f"R2_SON altı {R2_SON + 0.48 * KB + 24:.2f} > 628"
    assert tren_son_kutu[2] <= 1023 - 20, f"tren sağ {tren_son_kutu[2]} > 1003"
    assert tren_son_kutu[1] >= 368 + 20, f"tren üst {tren_son_kutu[1]} < 388"
    assert tren_son_kutu[3] + 24 <= R2_SON - 0.75 * KB, f"tren altı {tren_son_kutu[3] + 24} > {R2_SON - 0.75 * KB}"
    assert tren_son_kutu[0] >= SOL + g_sat1 + 40, f"tren solu {tren_son_kutu[0]} < {SOL + g_sat1 + 40}"

    # 6. Zaman
    satir1_bitis = SOZ[3]["t0"] + min(SOZ[3]["t1"] - SOZ[3]["t0"], Z["yazi_cap"])
    assert satir1_bitis <= Z["kapak_kare"] / 30.0 - 1.0 / 30.0, f"satır 1 bitiş {satir1_bitis:.3f} > kapak_kare sınırı"
    satir2_bitis = SOZ[6]["t0"] + min(SOZ[6]["t1"] - SOZ[6]["t0"], Z["yazi_cap"])
    assert satir2_bitis <= 2.93, f"satır 2 bitiş {satir2_bitis:.3f} > 2.93"
    u1 = Z["ucus"][0] + Z["ucus"][1]
    hareket_bitis_sinir = (Z["kare"] - 12) / 30.0
    assert u1 <= hareket_bitis_sinir, f"u1 {u1:.3f} > {hareket_bitis_sinir:.3f}"
    assert Z["kart_ciz"][0] + Z["kart_ciz"][1] <= 2.97, "kart_ciz bitişi > 2.97"

    # 7. Uçuş çakışma örneklemesi
    def _p3_in_out(p: float) -> float:
        p = max(0.0, min(1.0, p))
        return 8.0 * (p ** 4) if p < 0.5 else 1.0 - 8.0 * ((1.0 - p) ** 4)

    def _p3_out(p: float) -> float:
        p = max(0.0, min(1.0, p))
        return 1.0 - ((1.0 - p) ** 4)

    def _kesisir(b1: list[float], b2: list[float], pay: float = 6.0) -> bool:
        return not (b1[1] + pay <= b2[0] or b2[1] + pay <= b1[0] or b1[3] + pay <= b2[2] or b2[3] + pay <= b1[2])

    u0, ud = Z["ucus"]
    rk0, rkd = Z["rozet_kay"]
    t_baslik_opak = Z["baslik_sol"][0] + 0.71 * Z["baslik_sol"][1]

    curr_t = u0
    while curr_t <= u1 + 1e-6:
        pt = (curr_t - u0) / ud
        et = _p3_in_out(pt)
        es = _p3_out((curr_t - u0) / Z["ucus_olcek"])

        prz = (curr_t - rk0) / rkd
        erz = _p3_in_out(prz)
        curr_rz_x = KENAR + (rz_x - KENAR) * erz
        box_rz0 = [curr_rz_x, curr_rz_x + rz_w, 216.0, 288.0]

        box_r1 = [
            float(SOL),
            float(SOL + g_sat1),
            R1_K - 0.921 * KB + DY * et,
            R1_K + 0.212 * KB + DY * et,
        ]

        dx3 = (h3[0] - o3[0]) * et
        dy3 = (h3[1] - o3[1]) * et
        s3 = 1.0 + (hs3 - 1.0) * es
        box_tren = [
            o3[0] + dx3 + s3 * (48.0 - o3[0]),
            o3[0] + dx3 + s3 * (478.0 - o3[0]),
            o3[1] + dy3 + s3 * (1202.0 - o3[1]),
            o3[1] + dy3 + s3 * (1384.0 - o3[1]),
        ]

        c_tren_r1 = _kesisir(box_tren, box_r1, 6.0)
        assert not c_tren_r1, f"Uçuş çakışması t={curr_t:.3f}: tren x r1"

        c_tren_rz0 = _kesisir(box_tren, box_rz0, 6.0)
        assert not c_tren_rz0, f"Uçuş çakışması t={curr_t:.3f}: tren x rz0"

        if curr_t >= 2.20:
            if curr_t >= 2.80:
                g_r2_curr = Y.genislik("Fredoka", 700, "leaves at 7", KB)
            elif curr_t >= 2.56:
                g_r2_curr = Y.genislik("Fredoka", 700, "leaves at", KB)
            else:
                g_r2_curr = Y.genislik("Fredoka", 700, "leaves", KB)
            box_r2 = [
                float(SOL),
                float(SOL + g_r2_curr),
                R2_K - 0.75 * KB + DY * et,
                R2_K + 0.212 * KB + DY * et,
            ]
            c_tren_r2 = _kesisir(box_tren, box_r2, 6.0)
            assert not c_tren_r2, f"Uçuş çakışması t={curr_t:.3f}: tren x r2"

        if curr_t <= t_baslik_opak + 1e-6:
            dx1 = (h1[0] - o1[0]) * et
            dy1 = (h1[1] - o1[1]) * et
            s1 = 1.0 + (hs1 - 1.0) * es
            box_bas1 = [
                o1[0] + dx1 + s1 * (t1x - o1[0]),
                o1[0] + dx1 + s1 * (t1x + g1 - o1[0]),
                o1[1] + dy1 + s1 * (T1 - 0.921 * B - o1[1]),
                o1[1] + dy1 + s1 * (ALTI_Y + 5 - o1[1]),
            ]

            dx2 = (h2[0] - o2[0]) * et
            dy2 = (h2[1] - o2[1]) * et
            s2 = 1.0 + (hs2 - 1.0) * es
            box_bas2 = [
                o2[0] + dx2 + s2 * (hap_x - o2[0]),
                o2[0] + dx2 + s2 * (hap_x + hap_w - o2[0]),
                o2[1] + dy2 + s2 * (HAP_UST - o2[1]),
                o2[1] + dy2 + s2 * (HAP_ALT - o2[1]),
            ]

            c_bas1_rz0 = _kesisir(box_bas1, box_rz0, 6.0)
            c_bas2_rz0 = _kesisir(box_bas2, box_rz0, 6.0)
            c_bas2_r1 = _kesisir(box_bas2, box_r1, 6.0)
            b1_alt = o1[1] + dy1 + s1 * (T1 + 0.01 * B - o1[1])
            b2_ust = o2[1] + dy2 + s2 * (T2 - 0.69 * B - o2[1])
            c_bas1_bas2 = (b2_ust - b1_alt) < 6.0
            c_tren_bas1 = _kesisir(box_tren, box_bas1, 6.0)
            c_tren_bas2 = _kesisir(box_tren, box_bas2, 6.0)

            assert not c_bas1_rz0, f"Uçuş çakışması t={curr_t:.3f}: bas1 x rz0"
            assert not c_bas2_rz0, f"Uçuş çakışması t={curr_t:.3f}: bas2 x rz0"
            assert not c_bas2_r1, f"Uçuş çakışması t={curr_t:.3f}: bas2 x r1"
            assert not c_bas1_bas2, f"Uçuş çakışması t={curr_t:.3f}: bas1 x bas2"
            assert not c_tren_bas1, f"Uçuş çakışması t={curr_t:.3f}: tren x bas1"
            assert not c_tren_bas2, f"Uçuş çakışması t={curr_t:.3f}: tren x bas2"

        curr_t += 1.0 / 30.0


_denetimler()


# ---- 3.10 zamanlar() ----
def zamanlar() -> dict:
    """olay.py tarafından okunan olay zamanları."""
    return {
        "alti": [Z["alti"][0], Z["alti"][1]],
        "r1": [
            [SOZ[k]["t0"], round(min(SOZ[k]["t1"] - SOZ[k]["t0"], Z["yazi_cap"]), 4)]
            for k in range(4)
        ],
        "r2": [
            [SOZ[4 + k]["t0"], round(min(SOZ[4 + k]["t1"] - SOZ[4 + k]["t0"], Z["yazi_cap"]), 4)]
            for k in range(3)
        ],
        "ucus": [Z["ucus"][0], Z["ucus"][1]],
        "kart": [Z["kart_ciz"][0], Z["kart_ciz"][1]],
    }


# ---- Çizim Üreticileri ----
def _tren_parcalari_svg() -> str:
    yollar = []

    def _ekle_kutu(x: float, y: float, w: float, h: float, tohum: int, kalinlik: float, renk: str) -> None:
        for k in kutu(x, y, w, h, tohum):
            d = kutu_kenar_to_d(k)
            yollar.append(
                f'<path d="{d}" stroke="{renk}" stroke-width="{kalinlik}" vector-effect="non-scaling-stroke"/>'
            )

    def _ekle_elips(
        cx: float, cy: float, rx: float, ry: float, egim: float, tohum: int, kalinlik: float, renk: str
    ) -> None:
        pts = elips(cx, cy, rx, ry, egim, tohum)
        d = pts_to_d(pts)
        yollar.append(
            f'<path d="{d}" stroke="{renk}" stroke-width="{kalinlik}" vector-effect="non-scaling-stroke"/>'
        )

    def _ekle_duz(pts: list[tuple[float, float]], kalinlik: float, renk: str) -> None:
        d = pts_to_d(pts)
        yollar.append(
            f'<path d="{d}" stroke="{renk}" stroke-width="{kalinlik}" vector-effect="non-scaling-stroke"/>'
        )

    _ekle_kutu(200, 55, 170, 75, 31, 4.5, "#f3efe6")
    _ekle_kutu(200, 10, 75, 45, 32, 4.5, "#f3efe6")
    _ekle_kutu(320, 22, 26, 33, 33, 3.6, "#f3efe6")
    _ekle_duz([(370, 95), (398, 130), (370, 130)], 4.5, "#f3efe6")
    _ekle_kutu(0, 45, 175, 85, 34, 4.5, "#f3efe6")
    _ekle_duz([(175, 112), (200, 112)], 3.6, "#f3efe6")
    _ekle_kutu(20, 60, 50, 30, 35, 3.6, "#f3efe6")
    _ekle_kutu(100, 60, 50, 30, 36, 3.6, "#f3efe6")
    _ekle_kutu(215, 20, 42, 25, 37, 3.6, "#f3efe6")
    for i, x in enumerate([40, 135, 240, 335]):
        _ekle_elips(x, 138, 17, 17, 0, 50 + i, 4.5, "#f3efe6")
    _ekle_duz([(-10, 158), (420, 158)], 4.0, "#c9c2b3")
    _ekle_elips(345, 2, 11, 9, 0.2, 61, 3.4, "#c9c2b3")
    _ekle_elips(372, -16, 8, 7, 0.3, 62, 3.2, "#c9c2b3")

    ic = "".join(yollar)
    return (
        f'<g id="tren"><g id="tren-ic" transform="translate({TX} {TY})" fill="none" '
        f'stroke-linecap="round" stroke-linejoin="round">{ic}</g></g>'
    )


def _saat_svg() -> str:
    cx, cy, r = SAAT_X, SAAT_Y, SAAT_R
    yollar = []
    d_kadran = pts_to_d(elips(cx, cy, r, r * 0.97, 0.05, 41))
    yollar.append(f'<path d="{d_kadran}" stroke="#f3efe6" stroke-width="5"/>')
    for a, b in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
        pts = [(cx + a * r * 0.8, cy + b * r * 0.8), (cx + a * r * 0.66, cy + b * r * 0.66)]
        yollar.append(f'<path d="{pts_to_d(pts)}" stroke="#f3efe6" stroke-width="4"/>')
    pts_yel = [(cx, cy), (cx, cy - r * 0.66)]
    yollar.append(f'<path d="{pts_to_d(pts_yel)}" stroke="#f3efe6" stroke-width="5"/>')
    aci = (7.0 / 12.0) * math.pi * 2.0
    pts_akr = [(cx, cy), (cx + math.sin(aci) * r * 0.5, cy - math.cos(aci) * r * 0.5)]
    yollar.append(f'<path d="{pts_to_d(pts_akr)}" stroke="#f3efe6" stroke-width="6"/>')
    return f'<g id="saat">{"".join(yollar)}</g>'


def _bilet_svg() -> str:
    ce = math.cos(egim)
    se = math.sin(egim)

    def P(x: float, y: float) -> tuple[float, float]:
        return (BCX + BS * (x * ce - y * se), BCY + BS * (x * se + y * ce))

    yollar = []
    ortu_pts = [P(-180, -70), P(180, -70), P(180, 70), P(-180, 70)]
    d_ortu = pts_to_d(ortu_pts) + " Z"
    yollar.append(f'<path d="{d_ortu}" stroke="none" style="fill:var(--zemin)"/>')

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

    for k in [k1, k2, k3, k4]:
        yollar.append(f'<path d="{pts_to_d(k)}" stroke="#f3efe6" stroke-width="4.5"/>')

    for i in range(6):
        y0_delik = -58.0 + i * 20.0
        pts = [P(100, y0_delik), P(100, y0_delik + 11)]
        yollar.append(f'<path d="{pts_to_d(pts)}" stroke="#c9c2b3" stroke-width="3.4"/>')

    satirlar_baski = [
        [P(-150, -30), P(60, -30)],
        [P(-150, 0), P(30, 0)],
        [P(-150, 30), P(70, 30)],
    ]
    for pts in satirlar_baski:
        yollar.append(f'<path d="{pts_to_d(pts)}" stroke="#c9c2b3" stroke-width="4"/>')

    return f'<g id="bilet">{"".join(yollar)}</g>'


def _fig_svg() -> str:
    fig_kalinlik = {"govde": 4.4, "sac": 3.6, "yuz": 2.6}
    yollar = "".join(
        f'<path id="f{i}" d="{p["d"]}" stroke-width="{fig_kalinlik.get(p["parca"], 4.4) / fs:.3f}"/>'
        for i, p in enumerate(FIG["yollar"])
    )
    tx_fig = FIG_X - x0 * fs
    ty_fig = (ZEMIN_Y - FIG_H) - y0 * fs
    return f'<g id="fig" transform="translate({tx_fig:.2f} {ty_fig:.2f}) scale({fs:.6f})">{yollar}</g>'


# ---- 3.8 uret() ----
def uret() -> str:
    # Kırpma kutuları
    clips = (
        f'<clipPath id="cp1"><rect id="cr1" x="{SOL - 12}" y="{R1_K - KB}" width="0" '
        f'height="{int(KB * 1.35)}"/></clipPath>'
        f'<clipPath id="cp2"><rect id="cr2" x="{SOL - 12}" y="{R2_K - KB}" width="0" '
        f'height="{int(KB * 1.35)}"/></clipPath>'
    )

    # 1. Kapak sahne: eskiz (saat, bilet, figür) + etk1 + etk2
    eskiz = (
        f'<g id="eskiz" fill="none" stroke="#f3efe6" stroke-linecap="round" stroke-linejoin="round">'
        f'{_saat_svg()}{_bilet_svg()}{_fig_svg()}</g>'
    )
    etk1 = (
        f'<text id="etk1" x="{E1_X}" y="{E1_Y}" text-anchor="middle" font-family="Caveat" '
        f'font-weight="700" font-size="72" stroke="none" fill="#f3efe6">leaves</text>'
    )
    etk2 = (
        f'<text id="etk2" x="{E2_X}" y="{E2_Y}" text-anchor="end" font-family="Caveat" '
        f'font-weight="700" font-size="72" stroke="none" fill="#f3efe6">am going</text>'
    )
    kapak_sahne = f'<g id="kapak-sahne">{eskiz}{etk1}{etk2}</g>'

    # 2. Tren
    tren = _tren_parcalari_svg()

    # 3. Kart çerçevesi
    kart_kenarlar = kutu(57, 368, 966, 260, 71)
    kart_yollar = "".join(
        f'<path id="kc{i}" d="{kutu_kenar_to_d(k)}" stroke="#f3efe6" stroke-width="4" '
        f'stroke-linecap="round" fill="none" style="opacity:0"/>'
        for i, k in enumerate(kart_kenarlar)
    )
    kart = f'<g id="kart">{kart_yollar}</g>'

    # 4. Satırlar
    r1 = (
        f'<g id="r1"><text x="{SOL}" y="{R1_K}" font-family="Fredoka" font-weight="700" font-size="{KB}" '
        f'fill="#f3efe6" clip-path="url(#cp1)" style="font-kerning:none">{SATIR1}</text></g>'
    )
    r2 = (
        f'<g id="r2"><text x="{SOL}" y="{R2_K}" font-family="Fredoka" font-weight="700" font-size="{KB}" '
        f'fill="#f3efe6" clip-path="url(#cp2)" style="font-kerning:none">{SATIR2_KAPAK}</text></g>'
    )

    # 5. Başlık 2 (hap + neq + PLAN)
    # ≠ çizgileri (em -> px: x = GX + a*B, y = T2 - b*B)
    neq_c1 = f"M{GX + 0.093 * B:.2f} {T2 - 0.159 * B:.2f} L{GX + 0.352 * B:.2f} {T2 - 0.159 * B:.2f}"
    neq_c2 = f"M{GX + 0.093 * B:.2f} {T2 - 0.356 * B:.2f} L{GX + 0.352 * B:.2f} {T2 - 0.356 * B:.2f}"
    # QA tur 1: alt uç (0,115; −0,045) hapın sol alt kavisinden taşıyordu; uçlar içeri çekildi (kavise ≥ 11 px)
    neq_eg = f"M{GX + 0.322 * B:.2f} {T2 - 0.555 * B:.2f} L{GX + 0.150 * B:.2f} {T2 + 0.005 * B:.2f}"
    neq_paths = (
        f'<path d="{neq_c1}" stroke-width="{0.158 * B:.2f}"/>'
        f'<path d="{neq_c2}" stroke-width="{0.158 * B:.2f}"/>'
        f'<path d="{neq_eg}" stroke-width="{0.140 * B:.2f}"/>'
    )
    bas2 = (
        f'<g id="bas2">'
        f'<rect id="hap" x="{hap_x:.2f}" y="{HAP_UST:.2f}" width="{hap_w:.2f}" height="{hap_h:.2f}" '
        f'rx="{hap_rx:.2f}" fill="#f2a93b"/>'
        f'<g id="neq" fill="none" stroke-linecap="round" style="stroke:var(--pilMetin)">{neq_paths}</g>'
        f'<text id="bas2t" x="{PX:.2f}" y="{T2:.2f}" text-anchor="start" font-family="Fredoka" '
        f'font-weight="700" font-size="{B}" fill="#1b1a17" style="font-kerning:none">PLAN</text>'
        f'</g>'
    )

    # 6. Başlık 1 (TARİFE + altçizgi)
    x_bas = t1x - 6
    x_son = t1x + g1 + 6
    dx_al = x_son - x_bas
    alti_d = (
        f"M{x_bas:.2f} {ALTI_Y:.2f} "
        f"C{x_bas + dx_al / 3:.2f} {ALTI_Y - 5:.2f}, "
        f"{x_bas + 2 * dx_al / 3:.2f} {ALTI_Y + 5:.2f}, "
        f"{x_son:.2f} {ALTI_Y:.2f}"
    )
    bas1 = (
        f'<g id="bas1">'
        f'<text id="bas1t" x="{t1x:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="#f3efe6" stroke="#1b1a17" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">{BAS1}</text>'
        f'<path id="alti" d="{alti_d}" fill="none" stroke="#f2a93b" stroke-width="10" '
        f'stroke-linecap="round" style="opacity:0"/>'
        f'</g>'
    )

    # 7. Künye ve altyazı
    kunye_svg = Y.kunye_svg("Hook")
    alt_svg, alt_zaman = Y.altyazi_svg(0.0, Z["sure"], ALT)

    # Kırpma genişlikleri
    r1_prefixes = ["The", "The train", "The train to"]
    r1_w = [12 + Y.genislik("Fredoka", 700, p, KB) + 8 for p in r1_prefixes]
    r1_w.append(12 + Y.genislik("Fredoka", 700, SATIR1, KB) + 12)

    r2_prefixes = ["leaves", "leaves at"]
    r2_w = [12 + Y.genislik("Fredoka", 700, p, KB) + 8 for p in r2_prefixes]
    r2_w.append(12 + Y.genislik("Fredoka", 700, SATIR2_KAPAK, KB) + 12)

    veri = {
        "Z": Z,
        "alt": alt_zaman,
        "rz_kayma": KENAR - rz_x,
        "r1_t": [SOZ[k]["t0"] for k in range(4)],
        "r1_dur": [round(min(SOZ[k]["t1"] - SOZ[k]["t0"], Z["yazi_cap"]), 4) for k in range(4)],
        "r1_w": [round(w, 2) for w in r1_w],
        "r2_t": [SOZ[4 + k]["t0"] for k in range(3)],
        "r2_dur": [round(min(SOZ[4 + k]["t1"] - SOZ[4 + k]["t0"], Z["yazi_cap"]), 4) for k in range(3)],
        "r2_w": [round(w, 2) for w in r2_w],
        "o1": [round(o1[0], 2), round(o1[1], 2)],
        "h1": [round(h1[0], 2), round(h1[1], 2)],
        "hs1": round(hs1, 4),
        "o2": [round(o2[0], 2), round(o2[1], 2)],
        "h2": [round(h2[0], 2), round(h2[1], 2)],
        "hs2": round(hs2, 4),
        "o3": [round(o3[0], 2), round(o3[1], 2)],
        "h3": [round(h3[0], 2), round(h3[1], 2)],
        "hs3": round(hs3, 4),
        "dy": DY,
    }

    sure_val = Z["sure"]
    root_attrs = (
        f'data-composition-id="main" data-start="0" data-duration="{sure_val}" '
        'data-fps="30" data-width="1080" data-height="1920"'
    )

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" {root_attrs}>
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>{clips}</defs>
{kapak_sahne}
{tren}
{kart}
{r1}
{r2}
{bas2}
{bas1}
{kunye_svg}<g id="altyazi">{alt_svg}</g>
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var V = {json.dumps(veri)};
  var Z = V.Z, $ = function (s) {{ return document.querySelector(s); }};
  var tl = gsap.timeline({{ paused: true }});
  function ac(o) {{ o.immediateRender = false; return o; }}

  // 0. kare durumu
  gsap.set("#ku-ders", {{ opacity: 0 }});
  gsap.set("#ku-cip", {{ opacity: 0 }});
  gsap.set("#rz0", {{ x: V.rz_kayma }});

  // Altçizgi hazırla
  var alti = $("#alti");
  if (alti) {{
    var L = alti.getTotalLength();
    alti.style.strokeDasharray = L + " " + (L + 2);
    alti.style.strokeDashoffset = L;
  }}

  // Kart çerçevesi hazırla
  for (var k = 0; k < 4; k++) {{
    var pk = $("#kc" + k);
    if (pk) {{
      var Lk = pk.getTotalLength();
      pk.style.strokeDasharray = Lk + " " + (Lk + 2);
      pk.style.strokeDashoffset = Lk;
    }}
  }}

  // 1. Altçizgi darbesi (sine.inOut)
  tl.set("#alti", ac({{ opacity: 1 }}), Z.alti[0]);
  tl.to("#alti", ac({{ strokeDashoffset: 0, duration: Z.alti[1], ease: "sine.inOut" }}), Z.alti[0]);

  // 2. Altyazı
  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});

  // 3. Satır 1 kırpma ile kademeli yazım (4 adım)
  var prevW1 = 0;
  for (var i = 0; i < 4; i++) {{
    tl.fromTo("#cr1", {{ attr: {{ width: prevW1 }} }},
      ac({{ attr: {{ width: V.r1_w[i] }}, duration: V.r1_dur[i], ease: "none" }}), V.r1_t[i]);
    prevW1 = V.r1_w[i];
  }}

  // 4. Rozet sağa kayar
  tl.to("#rz0", ac({{ x: 0, duration: Z.rozet_kay[1], ease: "power3.inOut" }}), Z.rozet_kay[0]);

  // 5. Sahne grubu solar
  tl.to("#kapak-sahne", ac({{ opacity: 0, duration: Z.sahne_sol[1], ease: "power1.in" }}), Z.sahne_sol[0]);

  // 6. Uçuş: başlık 1, başlık 2 ve tren
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud;
  function uc2(id, o, h, hs, sol) {{
    gsap.set(id, {{ svgOrigin: o[0] + " " + o[1], smoothOrigin: false }});
    tl.to(id, ac({{ x: h[0] - o[0], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ y: h[1] - o[1], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ scale: hs, duration: Z.ucus_olcek, ease: "power3.out" }}), u0);
    if (sol) {{
      tl.to(id, ac({{ opacity: 0, duration: Z.baslik_sol[1], ease: "power1.in" }}), Z.baslik_sol[0]);
    }}
  }}
  uc2("#bas1", V.o1, V.h1, V.hs1, true);
  uc2("#bas2", V.o2, V.h2, V.hs2, true);
  uc2("#tren", V.o3, V.h3, V.hs3, false);

  // 7. Cümle satırları yukarı kayar
  tl.to("#r1", ac({{ y: V.dy, duration: ud, ease: "power3.inOut" }}), u0);
  tl.to("#r2", ac({{ y: V.dy, duration: ud, ease: "power3.inOut" }}), u0);

  // 8. Satır 2 kırpma ile kademeli yazım (3 adım)
  var prevW2 = 0;
  for (var j = 0; j < 3; j++) {{
    tl.fromTo("#cr2", {{ attr: {{ width: prevW2 }} }},
      ac({{ attr: {{ width: V.r2_w[j] }}, duration: V.r2_dur[j], ease: "none" }}), V.r2_t[j]);
    prevW2 = V.r2_w[j];
  }}

  // 9. Künye açılır
  tl.to("#ku-ders", ac({{ opacity: 1, duration: Z.kunye_ac[1], ease: "power1.out" }}), Z.kunye_ac[0]);

  // 10. Çip açılır
  tl.to("#ku-cip", ac({{ opacity: 1, duration: 0.2, ease: "power1.out" }}), u1 - 0.22);

  // 11. Kart çerçevesi (4 kenar sırayla)
  var kc = [$("#kc0"), $("#kc1"), $("#kc2"), $("#kc3")];
  var kcL = kc.map(function (p) {{ return p ? p.getTotalLength() : 0; }});
  var kcTop = kcL.reduce(function (a, b) {{ return a + b; }}, 0) || 1;
  var kcT = Z.kart_ciz[0];
  var kcD = Z.kart_ciz[1];
  kc.forEach(function (p, idx) {{
    if (!p) return;
    var dur = kcD * (kcL[idx] / kcTop);
    tl.set(p, ac({{ opacity: 1 }}), kcT);
    tl.to(p, ac({{ strokeDashoffset: 0, duration: dur, ease: "none" }}), kcT);
    kcT += dur;
  }});

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html


# ---- 3.10 __main__ ----
if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_icerik = uret()
    (AD / "proje" / "index.html").write_text(html_icerik, encoding="utf-8")

    satirlar = [
        "The train to İzmir",
        "leaves at 7 pm today.",
    ]
    sozcukler_list = []
    for sat_idx, sat_str in enumerate(satirlar):
        kelimeler = sat_str.split(" ")
        for k_idx, kelime in enumerate(kelimeler):
            prev = " ".join(kelimeler[:k_idx]) + (" " if k_idx > 0 else "")
            x0_s = SOL + Y.genislik("Fredoka", 700, prev, KB)
            x1_s = x0_s + Y.genislik("Fredoka", 700, kelime, KB)
            sozcukler_list.append([kelime, sat_idx, round(x0_s, 2), round(x1_s, 2)])

    devir = {
        "font": "Fredoka",
        "agirlik": 700,
        "boy": 64,
        "kerning": "none",
        "sol": 97,
        "taban": [468, 566],
        "satir": ["The train to İzmir", "leaves at 7 pm today."],
        "gorunen": ["The train to İzmir", "leaves at 7"],
        "sozcuk": sozcukler_list,
        "kart": {
            "x": 57,
            "y": 368,
            "w": 966,
            "h": 260,
            "tohum": 71,
            "cizgi": 4,
            "bicim": "kutu (ortak/kalem-canvas.js)",
        },
        "tren": {
            "kutu": [int(round(v)) for v in tren_son_kutu],
            "olcek": 0.5,
            "yerel_kutu": [-10, -24, 420, 158],
            "tx": 58,
            "ty": 1226,
            "kaynak": "trenParcalari",
        },
        "altyazi_ekran": EKRAN,
        "t": 3.0,
    }
    (AD / "devir.json").write_text(json.dumps(devir, ensure_ascii=False, indent=2), encoding="utf-8")
    print("devir:", json.dumps(devir, ensure_ascii=False))

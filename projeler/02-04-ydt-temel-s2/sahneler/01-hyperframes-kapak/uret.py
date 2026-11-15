"""02-04-ydt-temel-s2 sahne 01 kapak index.html üretici (HyperFrames DİKEY 1080x1920, 97 kare) · huni v2.

SPEC.md §3 uygulaması: kapak düzeni, çizimler, Caveat soru yazımı, başlık uçuşu ve devir.json çıktısı.
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

# ---- 3.1 Okuma ----
Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
ORTAK = AD.parent.parent / "ortak"
SOZ = [
    w for w in json.loads((ORTAK / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 1
]
assert [w["sozcuk"] for w in SOZ] == ["Genel", "mi,", "şu", "an", "mı?"], (
    f"Beklenen sözcükler bulunamadı: {[w['sozcuk'] for w in SOZ]}"
)
ALT = json.loads((ORTAK / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
assert ALT[0]["metin"] == "Genel mi, şu an mı?" and ALT[0]["cumle"] == 1, (
    f"Beklenen ilk altyazı bulunamadı: {ALT[0]}"
)
FIG = json.loads((AD / "cizim" / "ogretmen.json").read_text(encoding="utf-8"))
GY = json.loads((AD / "cizim" / "giysi.json").read_text(encoding="utf-8"))


# ---- 3.2 Darbe -> SVG ----
def darbe_svg(d: dict) -> str:
    """Izgara biriminde darbe verisini SVG öğesine çevirir."""
    if "daire" in d:
        cx, cy, r = d["daire"]
        return f'<circle cx="{cx}" cy="{cy}" r="{r}"/>'
    pts = d.get("n", [])
    if not pts:
        return ""
    if not d.get("egri", False) or len(pts) <= 2:
        d_str = f"M {pts[0][0]} {pts[0][1]} " + " ".join(f"L {p[0]} {p[1]}" for p in pts[1:])
        return f'<path d="{d_str}"/>'
    if len(pts) == 3:
        p0, p1, p2 = pts
        return f'<path d="M {p0[0]} {p0[1]} Q {p1[0]} {p1[1]} {p2[0]} {p2[1]}"/>'
    elif len(pts) == 4:
        p0, p1, p2, p3 = pts
        return f'<path d="M {p0[0]} {p0[1]} C {p1[0]} {p1[1]} {p2[0]} {p2[1]} {p3[0]} {p3[1]}"/>'
    else:
        parts = [f"M {pts[0][0]} {pts[0][1]}"]
        for i in range(1, len(pts) - 1):
            mx = (pts[i][0] + pts[i + 1][0]) / 2.0
            my = (pts[i][1] + pts[i + 1][1]) / 2.0
            parts.append(f"Q {pts[i][0]} {pts[i][1]} {mx:.2f} {my:.2f}")
        parts.append(f"L {pts[-1][0]} {pts[-1][1]}")
        return f'<path d="{" ".join(parts)}"/>'


# ---- 3.2 Sabitler ve türetilen ölçüler ----
W, H = Y.W, Y.H
SOL = 60
SAG = Y.HUD["sagSinir"]
UST = Y.HUD["icerikUst"]
ALT_SINIR = Y.HUD["icerikAlt"]

BAS1, BAS2 = "GENEL", "ŞU AN"
g_bas1_1 = Y.genislik("Fredoka", 700, BAS1, 1)
g_bas2_1 = Y.genislik("Fredoka", 700, BAS2, 1)
B = math.floor(min(
    190,
    900 / g_bas1_1,
    900 / (g_bas2_1 + 0.50 + 0.20 + 0.40),
))

PAD = 0.20 * B
NEQ_W = 0.50 * B
GAP = 0.20 * B

g1 = Y.genislik("Fredoka", 700, BAS1, B)
t1x = SOL
T1 = UST + 6 + 0.70 * B

HAP_UST = T1 + 0.18 * B
T2 = HAP_UST + 0.92 * B
HAP_ALT = T2 + 0.28 * B

hap_w = NEQ_W + GAP + Y.genislik("Fredoka", 700, BAS2, B) + 2 * PAD
hap_x = SOL
hap_rx = (HAP_ALT - HAP_UST) / 2
hap_h = HAP_ALT - HAP_UST

NX = hap_x + PAD
BX2 = NX + NEQ_W + GAP

ZEMIN_Y = 1372
FIG_H = 440
x0, y0, x1, y1 = FIG["kutu"]
fs = FIG_H / (y1 - y0)
govde_sag = FIG["govde_sag"]
FIG_X = 400
parmak_x, parmak_y = FIG["parmak"]
PX = FIG_X + (parmak_x - x0) * fs
PY = (ZEMIN_Y - FIG_H) + (parmak_y - y0) * fs

GT = 944
KM = 2.1
MX = SOL + 50 * KM
KT = 2.4
TX = 830
LB = 1280

SORU = "Genel mi, şu an mı?"
SORU_B = 72
SORU_T = 530
g_soru = Y.genislik("Caveat", 700, SORU, SORU_B)

ALT_Y = Y.HUD["altyaziBas"] + 84
KS = Y.konu_boyu()
hs = KS / B

rz_x, rz_w = Y.rozet_konumlari()[0]

SP = Y.genislik("Fredoka", 700, "Simple Present", KS)
SPV = Y.genislik("Fredoka", 700, "Simple Present vs ", KS)
PC = Y.genislik("Fredoka", 700, "Present Continuous", KS)

o1 = (t1x + g1 / 2, T1 - 0.35 * B)
h1 = (SOL + SP / 2, 420 - 0.35 * KS)

o2 = (hap_x + hap_w / 2, (HAP_UST + HAP_ALT) / 2)
h2 = (SOL + SPV + PC / 2, 420 - 0.35 * KS + (o2[1] - (T2 - 0.35 * B)) * hs)


# ---- 3.7 Denetimler ----
def _denetimler() -> None:
    # 1. B, baslik 1, hap
    assert 150 <= B <= 190, f"B={B} aralık [150, 190] dışı (§3.7 madde 1)"
    assert t1x + g1 <= SAG, f"baslik 1 sağı {t1x + g1:.2f} > SAG {SAG} (§3.7 madde 1)"
    assert hap_x + hap_w <= SAG, f"hap sağı {hap_x + hap_w:.2f} > SAG {SAG} (§3.7 madde 1)"
    assert max(g1, hap_w) <= 900, f"max(g1, hap_w) {max(g1, hap_w):.2f} > 900 (§3.7 madde 1)"
    assert T1 - 0.70 * B >= UST, f"baslik 1 üstü {T1 - 0.70 * B:.2f} < UST {UST} (§3.7 madde 1)"

    # 2. Hap içi
    assert NX + NEQ_W + 16 <= BX2, f"Hap içi ≠ ile yazı arası yetersiz (§3.7 madde 2)"
    g_bas2_b = Y.genislik("Fredoka", 700, BAS2, B)
    assert BX2 + g_bas2_b + 0.15 * B <= hap_x + hap_w, f"Hap içi yazı sağ taşma (§3.7 madde 2)"
    y0_egik = T2 - 0.70 * B
    y1_egik = T2 + 0.02 * B
    assert min(y0_egik, y1_egik) >= HAP_UST + 8 and max(y0_egik, y1_egik) <= HAP_ALT - 8, (
        f"Eğik çizgi y aralığı hap dışı (§3.7 madde 2)"
    )

    # 3. Soru
    assert len(SORU) <= 24, f"SORU {len(SORU)} > 24 karakter (§3.7 madde 3)"
    assert SOL + g_soru <= SAG, f"SORU sağı {SOL + g_soru:.2f} > SAG {SAG} (§3.7 madde 3)"
    assert SORU_T - 0.864 * SORU_B >= UST, f"SORU üstü {SORU_T - 0.864 * SORU_B:.2f} < UST {UST} (§3.7 madde 3)"
    assert SORU_T + 0.212 * SORU_B <= ALT_SINIR, (
        f"SORU altı {SORU_T + 0.212 * SORU_B:.2f} > ALT_SINIR {ALT_SINIR} (§3.7 madde 3)"
    )

    # 4. Kapak dikey (>= 24 px ara)
    kanca_m = GT - 22 * KM
    kanca_t = GT - 22 * KT
    fig_ust = ZEMIN_Y - FIG_H
    assert kanca_m - HAP_ALT >= 24, f"HAP_ALT -> mont askı ara {kanca_m - HAP_ALT:.2f} < 24 (§3.7 madde 4)"
    assert kanca_t - HAP_ALT >= 24, f"HAP_ALT -> tişört askı ara {kanca_t - HAP_ALT:.2f} < 24 (§3.7 madde 4)"
    assert fig_ust - HAP_ALT >= 24, f"HAP_ALT -> figür üst ara {fig_ust - HAP_ALT:.2f} < 24 (§3.7 madde 4)"
    mont_alt = GT + 117 * KM
    tisort_alt = GT + 88 * KT
    etk_ust = LB - 0.70 * 72
    assert etk_ust - mont_alt >= 24, f"mont alt -> etiket 1 üst ara {etk_ust - mont_alt:.2f} < 24 (§3.7 madde 4)"
    assert etk_ust - tisort_alt >= 24, f"tişört alt -> etiket 2 üst ara {etk_ust - tisort_alt:.2f} < 24 (§3.7 madde 4)"
    etk_alt = LB + 0.25 * 72
    assert ZEMIN_Y - etk_alt >= 24, f"etiket alt -> yer çizgisi ara {ZEMIN_Y - etk_alt:.2f} < 24 (§3.7 madde 4)"
    assert ZEMIN_Y <= ALT_SINIR, f"ZEMIN_Y {ZEMIN_Y} > ALT_SINIR {ALT_SINIR} (§3.7 madde 4)"

    # 5. Yatay
    assert MX - 50 * KM >= SOL, f"mont sol {MX - 50 * KM:.2f} < SOL {SOL} (§3.7 madde 5)"
    assert TX + 50 * KT <= SAG, f"tişört sağ {TX + 50 * KT:.2f} > SAG {SAG} (§3.7 madde 5)"
    assert MX + 50 * KM + 24 <= FIG_X, f"mont sağ + 24 {MX + 50 * KM + 24:.2f} > FIG_X {FIG_X:.2f} (§3.7 madde 5)"
    assert PX + 24 <= TX - 50 * KT, f"parmak X + 24 {PX + 24:.2f} > tişört sol {TX - 50 * KT:.2f} (§3.7 madde 5)"
    g_wears = Y.genislik("Caveat", 700, "wears", 72)
    assert MX - g_wears / 2 >= SOL and MX + g_wears / 2 <= FIG_X - 24, (
        f"wears aralığı sınırlar dışı (§3.7 madde 5)"
    )
    g_is_wearing = Y.genislik("Caveat", 700, "is wearing", 72)
    govde_sag_ekran = FIG_X + (govde_sag - x0) * fs
    assert TX - g_is_wearing / 2 >= govde_sag_ekran + 24 and TX + g_is_wearing / 2 <= SAG, (
        f"is wearing aralığı sınırlar dışı (§3.7 madde 5)"
    )

    # 6. Künye
    assert 28 <= KS <= 34, f"KS={KS} aralık [28, 34] dışı (§3.7 madde 6)"
    assert rz_x + rz_w <= SAG, f"rozet sağı {rz_x + rz_w:.2f} > SAG {SAG} (§3.7 madde 6)"
    assert SOL == 60, f"kapakta rozet x = SOL beklenen 60 (§3.7 madde 6)"

    # 7. Altyazı
    satirlar = Y.altyazi_satirlari(ALT[0]["metin"])
    assert len(satirlar) == 1, f"Altyazı tek satır değil: {satirlar} (§3.7 madde 7)"
    g_alt = Y.genislik("Lexend", 500, ALT[0]["metin"], 44)
    assert g_alt <= W - 2 * Y.HUD["kenar"], f"Altyazı genişliği {g_alt:.2f} > W - 2*kenar (§3.7 madde 7)"
    assert " ".join(w["sozcuk"] for w in SOZ) == ALT[0]["metin"], f"Sözcükler birleşimi metne eşit değil (§3.7 madde 7)"

    # 8. Zaman
    neq_bitis = Z["neq"][0] + Z["neq"][1]
    assert neq_bitis <= Z["kapak_kare"] / 30.0 - 1.0 / 30.0, (
        f"neq bitiş {neq_bitis:.3f} > kapak_kare sınırı (§3.7 madde 8)"
    )
    ilk_alt_acilis = SOZ[0]["t0"] - 0.05
    assert ilk_alt_acilis > Z["kapak_kare"] / 30.0, (
        f"ilk altyazı açılış {ilk_alt_acilis:.3f} <= kapak_kare (§3.7 madde 8)"
    )
    u1 = Z["ucus"][0] + Z["ucus"][1]
    hareket_bitis_sinir = (Z["kare"] - 12) / 30.0
    assert u1 <= hareket_bitis_sinir, f"u1 {u1:.3f} > hareket sınırı {hareket_bitis_sinir:.3f} (§3.7 madde 8)"
    assert Z["soru"][0] + Z["soru"][1] <= hareket_bitis_sinir, f"soru bitiş > sınır (§3.7 madde 8)"
    assert Z["kunye_ac"][0] + Z["kunye_ac"][1] <= hareket_bitis_sinir, f"kunye_ac bitiş > sınır (§3.7 madde 8)"
    assert Z["kunye_ac"][0] >= Z["baslik_sol"][0] + 0.71 * Z["baslik_sol"][1], (
        f"kunye_ac başlık solmadan önce açılıyor (§3.7 madde 8)"
    )

    # 9. Uçuş çakışma örneklemesi
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
    s0_soru, sd_soru = Z["soru"]
    curr_t = u0
    max_t = Z["baslik_sol"][0] + 0.71 * Z["baslik_sol"][1]

    while curr_t <= max_t + 1e-6:
        pt = (curr_t - u0) / ud
        et = _p3_in_out(pt)
        es = _p3_out((curr_t - u0) / Z["ucus_olcek"])

        dx1 = (h1[0] - o1[0]) * et
        dy1 = (h1[1] - o1[1]) * et
        s1 = 1.0 + (hs - 1.0) * es
        box_bas1 = [
            o1[0] + dx1 + s1 * (t1x - 6.0 - o1[0]),
            o1[0] + dx1 + s1 * (t1x + g1 + 6.0 - o1[0]),
            o1[1] + dy1 + s1 * (T1 - 0.70 * B - 6.0 - o1[1]),
            o1[1] + dy1 + s1 * (T1 + 0.02 * B + 6.0 - o1[1]),
        ]

        dx2 = (h2[0] - o2[0]) * et
        dy2 = (h2[1] - o2[1]) * et
        s2 = 1.0 + (hs - 1.0) * es
        box_bas2 = [
            o2[0] + dx2 + s2 * (hap_x - o2[0]),
            o2[0] + dx2 + s2 * (hap_x + hap_w - o2[0]),
            o2[1] + dy2 + s2 * (HAP_UST - o2[1]),
            o2[1] + dy2 + s2 * (HAP_ALT - o2[1]),
        ]

        prz = (curr_t - rk0) / rkd
        erz = _p3_in_out(prz)
        curr_rz_x = SOL + (rz_x - SOL) * erz
        box_rz0 = [curr_rz_x, curr_rz_x + rz_w, 386.0, 434.0]

        if curr_t < s0_soru:
            box_soru = None
        else:
            p_soru = min(1.0, (curr_t - s0_soru) / sd_soru)
            e_soru = p_soru ** 2
            w_soru_t = (g_soru + 24) * e_soru
            if SOL - 12 + w_soru_t <= SOL:
                box_soru = None
            else:
                box_soru = [
                    float(SOL),
                    min(float(SOL + g_soru), float(SOL - 12 + w_soru_t)),
                    float(SORU_T - 0.864 * SORU_B),
                    float(SORU_T + 0.212 * SORU_B),
                ]

        c1 = _kesisir(box_bas1, box_rz0, 6.0)
        c2 = _kesisir(box_bas2, box_rz0, 6.0)
        c3 = _kesisir(box_bas1, box_bas2, 6.0)
        c4 = _kesisir(box_bas1, box_soru, 6.0) if box_soru else False
        c5 = _kesisir(box_bas2, box_soru, 6.0) if box_soru else False

        if c1 or c2 or c3 or c4 or c5:
            assert False, (
                f"Uçuş çakışması t={curr_t:.3f}: bas1xrz0={c1}, bas2xrz0={c2}, "
                f"bas1xbas2={c3}, bas1xsoru={c4}, bas2xsoru={c5} (§3.7 madde 9)"
            )

        curr_t += 1.0 / 30.0


_denetimler()


# ---- 3.8 zamanlar() fonksiyonu ----
def zamanlar() -> dict:
    """olay.py tarafından okunan olay zamanları."""
    return {
        "neq": [Z["neq"][0], Z["neq"][1]],
        "ucus": [Z["ucus"][0], Z["ucus"][1]],
        "soru": [Z["soru"][0], Z["soru"][1]],
    }


# ---- 3.8 uret() fonksiyonu ----
def uret() -> str:
    R = Y.RENK

    # Kırpma kutusu: soru satırı
    clips = (
        f'<clipPath id="cps">'
        f'<rect id="crs" x="{SOL - 12}" y="{SORU_T - SORU_B}" width="0" height="{1.35 * SORU_B:.1f}"/>'
        f'</clipPath>'
    )

    # 1. Çizimler: yer çizgisi
    zc_path = f'<path id="zc" d="M{SOL} {ZEMIN_Y} L{SAG} {ZEMIN_Y}" stroke-width="4"/>'

    # 2. Mont (darbeler ve askı)
    mont_darbeler = "".join(darbe_svg(d) for d in GY["mont"]["darbeler"])
    mont_aski = "".join(darbe_svg(d) for d in GY["mont"]["aski"])
    mont_group = (
        f'<g id="mont" transform="translate({MX - 50 * KM:.2f} {GT}) scale({KM})">'
        f'<g stroke-width="{4.0 / KM:.3f}">{mont_darbeler}</g>'
        f'<g stroke-width="{3.4 / KM:.3f}">{mont_aski}</g>'
        f'</g>'
    )

    # 3. Tişört (darbeler ve askı)
    tisort_darbeler = "".join(darbe_svg(d) for d in GY["tisort"]["darbeler"])
    tisort_aski = "".join(darbe_svg(d) for d in GY["tisort"]["aski"])
    tisort_group = (
        f'<g id="tisort" transform="translate({TX - 50 * KT:.2f} {GT}) scale({KT})">'
        f'<g stroke-width="{4.0 / KT:.3f}">{tisort_darbeler}</g>'
        f'<g stroke-width="{3.4 / KT:.3f}">{tisort_aski}</g>'
        f'</g>'
    )

    # 4. Figür (öğretmen)
    fig_kalinlik = {"govde": 4.4, "sac": 3.6, "yuz": 2.6}
    fig_svg = "".join(
        f'<path id="f{i}" d="{p["d"]}" stroke-width="{fig_kalinlik.get(p["parca"], 4.4) / fs:.3f}"/>'
        for i, p in enumerate(FIG["yollar"])
    )
    tx_fig = FIG_X - x0 * fs
    ty_fig = (ZEMIN_Y - FIG_H) - y0 * fs
    fig_group = f'<g id="fig" transform="translate({tx_fig:.2f} {ty_fig:.2f}) scale({fs:.6f})">{fig_svg}</g>'

    # Eskiz grubu
    eskiz = (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{zc_path}{mont_group}{tisort_group}{fig_group}</g>'
    )

    # Etiketler: wears, is wearing
    etk1 = (
        f'<text id="etk1" x="{MX}" y="{LB}" text-anchor="middle" font-family="Caveat" font-weight="700" '
        f'font-size="72" stroke="none" fill="{R["murekkep"]}">wears</text>'
    )
    etk2 = (
        f'<text id="etk2" x="{TX}" y="{LB}" text-anchor="middle" font-family="Caveat" font-weight="700" '
        f'font-size="72" stroke="none" fill="{R["murekkep"]}">is wearing</text>'
    )

    kapak_sahne = f'<g id="kapak-sahne">{eskiz}{etk1}{etk2}</g>'

    # Soru satırı
    soru_svg = (
        f'<g id="soru">'
        f'<text x="{SOL}" y="{SORU_T}" font-family="Caveat" font-weight="700" font-size="{SORU_B}" '
        f'fill="{R["murekkep"]}" clip-path="url(#cps)" style="font-kerning:none">{SORU}</text>'
        f'</g>'
    )

    # Başlık 2 (hap + neq + ŞU AN)
    x0_cubuk = NX + 0.06 * B
    x1_cubuk = NX + NEQ_W - 0.06 * B
    xc_cubuk = (x0_cubuk + x1_cubuk) / 2
    y_ust = T2 - 0.46 * B
    y_alt = T2 - 0.24 * B

    neq_c1 = f"M {x0_cubuk:.2f} {y_ust:.2f} Q {xc_cubuk:.2f} {y_ust - 3:.2f} {x1_cubuk:.2f} {y_ust:.2f}"
    neq_c2 = f"M {x0_cubuk:.2f} {y_alt:.2f} Q {xc_cubuk:.2f} {y_alt + 3:.2f} {x1_cubuk:.2f} {y_alt:.2f}"

    x0_egik = NX + 0.74 * NEQ_W
    y0_egik = T2 - 0.70 * B
    x1_egik = NX + 0.26 * NEQ_W
    y1_egik = T2 + 0.02 * B
    neq_eg = f"M {x0_egik:.2f} {y0_egik:.2f} L {x1_egik:.2f} {y1_egik:.2f}"

    neq_paths = (
        f'<path d="{neq_c1}" stroke-width="{0.10 * B:.2f}"/>'
        f'<path d="{neq_c2}" stroke-width="{0.10 * B:.2f}"/>'
        f'<path d="{neq_eg}" stroke-width="{0.09 * B:.2f}"/>'
    )

    bas2 = (
        f'<g id="bas2">'
        f'<rect id="hap" x="{hap_x:.2f}" y="{HAP_UST:.2f}" width="{hap_w:.2f}" height="{hap_h:.2f}" '
        f'rx="{hap_rx:.2f}" fill="{R["vurgu"]}"/>'
        f'<g id="neq" fill="none" stroke-linecap="round" style="stroke:var(--pilMetin)">{neq_paths}</g>'
        f'<text id="bas2t" x="{BX2:.2f}" y="{T2:.2f}" text-anchor="start" font-family="Fredoka" '
        f'font-weight="700" font-size="{B}" fill="#1b1a17" style="font-kerning:none">{BAS2}</text>'
        f'</g>'
    )

    # Başlık 1 (GENEL)
    bas1 = (
        f'<g id="bas1">'
        f'<text id="bas1t" x="{t1x:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" stroke="#1b1a17" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">{BAS1}</text>'
        f'</g>'
    )

    # Künye
    kunye_svg = Y.kunye_svg()

    # Altyazı ve karaoke
    metin = ALT[0]["metin"]
    g_metin = Y.genislik("Lexend", 500, metin, 44)
    x0_alt = 540.0 - g_metin / 2.0

    alt_elements = []
    prefix = ""
    karaoke_bilgi = []
    soz_bilgi = []

    for i, w in enumerate(SOZ):
        w_metin = w["sozcuk"]
        x_i = x0_alt + Y.genislik("Lexend", 500, prefix, 44)
        prefix += w_metin + " "

        temiz = re.sub(r"[.,?!:]+$", "", w_metin)
        g_temiz = Y.genislik("Lexend", 500, temiz, 44)

        ak_x0 = x_i - 2.0
        ak_x1 = x_i + g_temiz + 2.0
        ak_y = ALT_Y + 10.0

        alt_elements.append(
            f'<path id="ak{i}" d="M{ak_x0:.2f} {ak_y:.2f} L{ak_x1:.2f} {ak_y:.2f}" '
            f'stroke="{R["vurgu"]}" stroke-width="5" stroke-linecap="round" style="opacity:0"/>'
        )
        alt_elements.append(
            f'<text id="aw{i}" x="{x_i:.2f}" y="{ALT_Y:.2f}" text-anchor="start" font-family="Lexend" '
            f'font-weight="500" font-size="44" fill="{R["murekkep"]}" style="opacity:0;font-kerning:none">'
            f'{w_metin}</text>'
        )

        t_aw_ac = max(0.0, w["t0"] - 0.05)
        t_aw_kapat = min(ALT[0]["t1"] + 0.35, Z["sure"])
        soz_bilgi.append([f"aw{i}", round(t_aw_ac, 3), round(t_aw_kapat, 3)])

        if i < len(SOZ) - 1:
            bitis_i = min(w["t1"], SOZ[i + 1]["t0"] - 0.04, Z["karaoke_son"])
        else:
            bitis_i = min(w["t1"], Z["karaoke_son"])

        karaoke_bilgi.append([f"ak{i}", round(w["t0"], 3), round(bitis_i, 3)])

    altyazi_svg = "".join(alt_elements)

    # ≠ zamanları
    L_ust = math.hypot(x1_cubuk - x0_cubuk, 0)
    L_alt = math.hypot(x1_cubuk - x0_cubuk, 0)
    L_egik = math.hypot(x1_egik - x0_egik, y1_egik - y0_egik)
    neq_zamanlar = Y.cizgi_zamanlari([L_ust, L_alt, L_egik], Z["neq"][0], Z["neq"][0] + Z["neq"][1])

    veri = {
        "Z": Z,
        "rz_kayma": SOL - rz_x,
        "neq_zaman": neq_zamanlar,
        "aw": soz_bilgi,
        "ak": karaoke_bilgi,
        "o1": [round(o1[0], 2), round(o1[1], 2)],
        "h1": [round(h1[0], 2), round(h1[1], 2)],
        "o2": [round(o2[0], 2), round(o2[1], 2)],
        "h2": [round(h2[0], 2), round(h2[1], 2)],
        "hs": round(hs, 6),
        "soru_w": round(g_soru + 24, 2),
    }

    sure_val = Z["sure"]
    fps_val = Z["fps"]
    root_attrs = (
        f'data-composition-id="main" data-start="0" data-duration="{sure_val}" '
        f'data-fps="{fps_val}" data-width="1080" data-height="1920"'
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
{soru_svg}
{bas2}
{bas1}
{kunye_svg}<g id="altyazi">{altyazi_svg}</g>
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
  gsap.set("#ku-konu", {{ opacity: 0 }});
  gsap.set("#rz0", {{ x: V.rz_kayma }});

  // ≠ yolları hazırla
  var neqYollar = document.querySelectorAll("#neq path");
  neqYollar.forEach(function (p, i) {{
    var L = p.getTotalLength();
    p.style.strokeDasharray = L + " " + (L + 2);
    p.style.strokeDashoffset = L;
    gsap.set(p, {{ opacity: 0 }});
  }});

  // 1. ≠ çizimi (üst çubuk -> alt çubuk -> eğik çizgi)
  neqYollar.forEach(function (p, i) {{
    var z = V.neq_zaman[i];
    tl.set(p, ac({{ opacity: 1 }}), z[0]);
    tl.to(p, ac({{ strokeDashoffset: 0, duration: z[1], ease: "sine.inOut" }}), z[0]);
  }});

  // 2. Altyazı sözcük zamanlı açılış
  V.aw.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});

  // 3. Altyazı karaoke çizgileri
  V.ak.forEach(function (k) {{
    tl.set("#" + k[0], ac({{ opacity: 1 }}), k[1]);
    tl.set("#" + k[0], ac({{ opacity: 0 }}), k[2]);
  }});

  // 4. Rozet sağa kayar
  tl.to("#rz0", ac({{ x: 0, duration: Z.rozet_kay[1], ease: "power3.inOut" }}), Z.rozet_kay[0]);

  // 5. Sahne grubu solar
  tl.to("#kapak-sahne", ac({{ opacity: 0, duration: Z.sahne_sol[1], ease: "power1.in" }}), Z.sahne_sol[0]);

  // 6. Uçuş: başlık 1 ve başlık 2
  var u0 = Z.ucus[0], ud = Z.ucus[1];
  function uc2(id, o, h, hs) {{
    gsap.set(id, {{ svgOrigin: o[0] + " " + o[1], smoothOrigin: false }});
    tl.to(id, ac({{ x: h[0] - o[0], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ y: h[1] - o[1], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ scale: hs, duration: Z.ucus_olcek, ease: "power3.out" }}), u0);
    tl.to(id, ac({{ opacity: 0, duration: Z.baslik_sol[1], ease: "power1.in" }}), Z.baslik_sol[0]);
  }}
  uc2("#bas1", V.o1, V.h1, V.hs);
  uc2("#bas2", V.o2, V.h2, V.hs);

  // 7. Soru satırı kırpmayla yazılır
  tl.fromTo("#crs", {{ attr: {{ width: 0 }} }},
    ac({{ attr: {{ width: V.soru_w }}, duration: Z.soru[1], ease: "power1.in" }}), Z.soru[0]);

  // 8. Konu açılır
  tl.to("#ku-konu", ac({{ opacity: 1, duration: Z.kunye_ac[1], ease: "power1.out" }}), Z.kunye_ac[0]);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html


# ---- 3.8 __main__ bloğu ----
if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_icerik = uret()
    (AD / "proje" / "index.html").write_text(html_icerik, encoding="utf-8")

    devir = {
        "font": "Caveat",
        "agirlik": 700,
        "boy": 72,
        "kerning": "none",
        "sol": 60,
        "taban": 530,
        "satir": SORU,
        "sag": round(SOL + g_soru, 2),
        "ust": round(SORU_T - 0.864 * 72, 2),
        "alt": round(SORU_T + 0.212 * 72, 2),
        "t": 2.84,
        "altyazi": "cümle 1 tek satır, Lexend 500 44, taban 1484, ortalı",
    }
    (AD / "devir.json").write_text(json.dumps(devir, ensure_ascii=False, indent=2), encoding="utf-8")
    print("devir:", json.dumps(devir, ensure_ascii=False))

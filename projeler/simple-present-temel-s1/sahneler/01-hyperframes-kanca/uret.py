"""simple-present-temel-s1 sahne 01 kanca index.html üretici (HyperFrames DİKEY 1080x1920, 102 kare).

SPEC v2 §4 uygulaması (huni v2): kanal katmanı, künye, kapak düzeni, soru işareti kalem çizimi,
uçuş, grup küçülmesi, satır yazımı, kart girişi ve devir.json.
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

# ---- 4.1 Okuma ----
Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
ORTAK = AD.parent.parent / "ortak"
SOZ = [
    w for w in json.loads((ORTAK / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 1
]
assert [w["sozcuk"] for w in SOZ[:3]] == ["Kardeşim", "gider:", "go"], (
    f"Beklenen ilk 3 sözcük bulunamadı: {[w['sozcuk'] for w in SOZ[:3]]}"
)
ALT = json.loads((ORTAK / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
gw, gh, FIG = Y.peeps("standing-2", 60)

# ---- 4.2 Sabitler ve türetilen ölçüler (§4.2) ----
W, H = Y.W, Y.H
KENAR = Y.HUD["kenar"]
SAG = Y.HUD["sagSinir"]
ORTA = (KENAR + SAG) / 2
BAS1 = "GO mu,"
BAS2 = "GOES mu"
BAS2_TAM = BAS2 + "?"
PAD = 0.20  # em

B = math.floor(min(
    190,
    (SAG - KENAR) / Y.genislik("Fredoka", 700, BAS1, 1),
    (SAG - KENAR) / (Y.genislik("Fredoka", 700, BAS2_TAM, 1) + 2 * PAD),
))
g1 = Y.genislik("Fredoka", 700, BAS1, B)
t1x = ORTA - g1 / 2
TOP1 = 472
T1 = TOP1 + 0.70 * B
HAP_UST = T1 + 0.34 * B
T2 = HAP_UST + 0.98 * B
HAP_ALT = T2 + 0.26 * B

g2 = Y.genislik("Fredoka", 700, BAS2_TAM, B)
hap_w = g2 + 2 * PAD * B
hap_x = ORTA - hap_w / 2
hap_rx = (HAP_ALT - HAP_UST) / 2
hap_h = HAP_ALT - HAP_UST

t2x = ORTA - g2 / 2
QX = t2x + Y.genislik("Fredoka", 700, BAS2, B)
QB = B / 1000

ZEMIN_Y = 1372
FIG_H = 440
FIG_S = FIG_H / gh
FIG_X = 120
FIG_Y = ZEMIN_Y - FIG_H

BUS_KUTU = [340, 1135, 600, 233]
BUS = Y.coco("bus", BUS_KUTU)

G = (80, 932, 870, 442)
GK = min(256 / 870, 140 / 442)
GT = (700, 465)

SATIR = "Kardeşim gider:"
SAT_BOY = 72
SAT_X = 60
SAT_TABAN = 560
SATIR_BAS = Z["ucus"][0] + Z["ucus"][1]

KART = {"x": 62, "y": 622, "w": 376, "h": 196, "rx": 28, "cizgi": 4}
KART_YAZI = "go"
KART_BAS = SOZ[2]["t0"]

boy = Y.konu_boyu()
rz_x, rz_w = Y.rozet_konumu()

gk1 = Y.genislik("Fredoka", 700, Y.KONU_PARCA[0], boy)
gk2 = Y.genislik("Fredoka", 700, Y.KONU_PARCA[1], boy)
KONU_SON = KENAR + Y.genislik("Fredoka", 700, Y.KONU, boy)
YK = Y.HUD["konuTaban"] - 0.35 * boy
UK = 0.85

o1 = (t1x + g1 / 2, T1 - 0.35 * B)
h1 = (KENAR + UK * gk1 / 2, YK - Z["ucus_ayrik"])
hs1 = UK * gk1 / g1

o2 = (ORTA, (HAP_UST + HAP_ALT) / 2)
h2 = (KONU_SON - UK * gk2 / 2, YK + Z["ucus_ayrik"])
hs2 = UK * gk2 / hap_w

# ---- 4.3 Soru işareti yolu ----
KANCA_D = (
    f"M {QX + 85 * QB:.2f} {T2 - 520 * QB:.2f} "
    f"C {QX + 85 * QB:.2f} {T2 - 610 * QB:.2f} {QX + 160 * QB:.2f} {T2 - 638 * QB:.2f} "
    f"{QX + 235 * QB:.2f} {T2 - 638 * QB:.2f} "
    f"C {QX + 320 * QB:.2f} {T2 - 638 * QB:.2f} {QX + 385 * QB:.2f} {T2 - 590 * QB:.2f} "
    f"{QX + 385 * QB:.2f} {T2 - 515 * QB:.2f} "
    f"C {QX + 385 * QB:.2f} {T2 - 430 * QB:.2f} {QX + 235 * QB:.2f} {T2 - 415 * QB:.2f} "
    f"{QX + 235 * QB:.2f} {T2 - 300 * QB:.2f} "
    f"L {QX + 235 * QB:.2f} {T2 - 250 * QB:.2f}"
)
NOKTA_D = (
    f"M {QX + 235 * QB:.2f} {T2 - 62 * QB:.2f} "
    f"L {QX + 235 * QB:.2f} {T2 - 64 * QB:.2f}"
)
SORU_SW = round(140 * QB, 2)


# ---- 4.8 Denetimler ----
def _denetimler() -> None:
    # 1. B, hap, baslik 1
    assert 140 <= B <= 190, f"B={B} aralık [140, 190] dışı"
    assert hap_x >= KENAR - 0.5 and hap_x + hap_w <= SAG + 0.5, (
        f"hap x={hap_x:.2f}..{hap_x + hap_w:.2f} aralık [{KENAR - 0.5}, {SAG + 0.5}] dışı"
    )
    assert t1x >= KENAR and t1x + g1 <= SAG, (
        f"baslik 1 x={t1x:.2f}..{t1x + g1:.2f} aralık [{KENAR}, {SAG}] dışı"
    )
    assert (T1 - 0.70 * B) >= Y.HUD["icerikBas"], (
        f"baslik 1 üstü {T1 - 0.70 * B:.2f} < icerikBas {Y.HUD['icerikBas']}"
    )
    assert HAP_ALT <= 900, f"HAP_ALT {HAP_ALT:.2f} > 900"

    # 2. ? kutusu
    pts = [
        (85, 520), (85, 610), (160, 638), (235, 638), (320, 638), (385, 590),
        (385, 515), (385, 430), (235, 415), (235, 300), (235, 250),
        (235, 62), (235, 64)
    ]
    sw = 140 * QB
    xs = [QX + ux * QB for ux, _ in pts]
    ys = [T2 - uy * QB for _, uy in pts]
    q_sol = min(xs) - sw / 2
    q_sag = max(xs) + sw / 2
    q_ust = min(ys) - sw / 2
    q_alt = max(ys) + sw / 2
    assert q_sol >= QX, f"q_sol {q_sol:.2f} < QX {QX:.2f}"
    assert q_sag <= hap_x + hap_w - 8, f"q_sag {q_sag:.2f} > hap_x + hap_w - 8 {hap_x + hap_w - 8:.2f}"
    assert q_ust >= HAP_UST + 8, f"q_ust {q_ust:.2f} < HAP_UST + 8 {HAP_UST + 8:.2f}"
    assert q_alt <= HAP_ALT - 8, f"q_alt {q_alt:.2f} > HAP_ALT - 8 {HAP_ALT - 8:.2f}"

    # 3. Karakter sayısı ve satır sağ sınır
    assert len(BAS1) <= 24, f"BAS1 {len(BAS1)} > 24 karakter"
    assert len(BAS2_TAM) <= 24, f"BAS2_TAM {len(BAS2_TAM)} > 24 karakter"
    assert len(SATIR) <= 24, f"SATIR {len(SATIR)} > 24 karakter"
    g_sat = Y.genislik("Caveat", 700, SATIR, SAT_BOY)
    assert SAT_X + g_sat + 24 <= GT[0], f"SAT_X + g_sat + 24 = {SAT_X + g_sat + 24:.2f} > GT[0] {GT[0]}"

    # 4. Kapak dikey ve yatay
    assert HAP_ALT + 24 <= FIG_Y, f"HAP_ALT + 24 = {HAP_ALT + 24:.2f} > FIG_Y {FIG_Y}"
    assert ZEMIN_Y + 2 <= Y.HUD["icerikSon"], f"ZEMIN_Y + 2 = {ZEMIN_Y + 2} > icerikSon {Y.HUD['icerikSon']}"
    assert FIG_X + gw * FIG_S + 24 <= BUS_KUTU[0], (
        f"FIG_X + gw*FIG_S + 24 = {FIG_X + gw * FIG_S + 24:.2f} > BUS_KUTU[0] {BUS_KUTU[0]}"
    )
    assert BUS_KUTU[0] + BUS_KUTU[2] <= SAG - 16, (
        f"BUS sağı {BUS_KUTU[0] + BUS_KUTU[2]} > SAG - 16 {SAG - 16}"
    )
    bus_coords = [float(v) for p in BUS for v in re.findall(r"-?\d+(?:\.\d+)?", p["d"])]
    bus_xs = bus_coords[0::2]
    bus_ys = bus_coords[1::2]
    assert min(bus_xs) >= BUS_KUTU[0] - 1.0, f"min bus x {min(bus_xs):.2f} < {BUS_KUTU[0] - 1.0}"
    assert max(bus_xs) <= BUS_KUTU[0] + BUS_KUTU[2] + 1.0, (
        f"max bus x {max(bus_xs):.2f} > {BUS_KUTU[0] + BUS_KUTU[2] + 1.0}"
    )
    assert min(bus_ys) >= BUS_KUTU[1] - 1.0, f"min bus y {min(bus_ys):.2f} < {BUS_KUTU[1] - 1.0}"
    assert max(bus_ys) <= BUS_KUTU[1] + BUS_KUTU[3] + 1.0, (
        f"max bus y {max(bus_ys):.2f} > {BUS_KUTU[1] + BUS_KUTU[3] + 1.0}"
    )

    # 5. Son hal
    assert GT[1] >= Y.HUD["icerikBas"], f"GT[1] {GT[1]} < icerikBas {Y.HUD['icerikBas']}"
    assert GT[1] + G[3] * GK <= 600, f"GT[1] + G[3]*GK = {GT[1] + G[3] * GK:.2f} > 600"
    assert GT[0] >= 700, f"GT[0] {GT[0]} < 700"
    assert GT[0] + G[2] * GK <= SAG, f"GT[0] + G[2]*GK = {GT[0] + G[2] * GK:.2f} > SAG {SAG}"
    sat_ust = SAT_TABAN - 0.864 * SAT_BOY
    assert sat_ust >= Y.HUD["icerikBas"], f"satır üstü {sat_ust:.2f} < icerikBas {Y.HUD['icerikBas']}"
    sat_alt = SAT_TABAN + 0.212 * SAT_BOY
    assert sat_alt + 24 <= 620, f"satır altı + 24 = {sat_alt + 24:.2f} > 620"
    assert 60 >= KENAR and 440 <= SAG, "KART yatay içerik bandı dışı"
    assert 620 >= Y.HUD["icerikBas"] and 820 <= Y.HUD["icerikSon"], "KART dikey içerik bandı dışı"
    assert 440 + 24 <= GT[0], f"440 + 24 = {440 + 24} > GT[0] {GT[0]}"

    # 6. Zaman
    soru_nokta_son = Z["soru_nokta"][0] + Z["soru_nokta"][1]
    assert soru_nokta_son <= Z["kapak_kare"] / 30.0 - 1.0 / 30.0, (
        f"soru_nokta sonu {soru_nokta_son:.3f} > kapak_kare sınırı {Z['kapak_kare']/30.0 - 1.0/30.0:.3f}"
    )
    assert Z["soru"][0] >= 0.25, f"soru başı {Z['soru'][0]} < 0.25"
    assert soru_nokta_son < SOZ[0]["t0"], f"soru_nokta sonu {soru_nokta_son:.3f} >= SOZ[0].t0 {SOZ[0]['t0']}"
    assert SATIR_BAS >= SOZ[1]["t1"], f"SATIR_BAS {SATIR_BAS:.3f} < SOZ[1].t1 {SOZ[1]['t1']}"
    assert KART_BAS == SOZ[2]["t0"], f"KART_BAS {KART_BAS:.3f} != SOZ[2].t0 {SOZ[2]['t0']}"

    hareket_bitis_sinir = (Z["kare"] - 12) / 30.0
    ucus_son = Z["ucus"][0] + Z["ucus"][1]
    grup_son = Z["grup_ucus"][0] + Z["grup_ucus"][1]
    satir_son = SATIR_BAS + Z["satir_sure"]
    kart_son = KART_BAS + Z["kart_sure"]
    kunye_ac_son = Z["kunye_ac"][0] + Z["kunye_ac"][1]
    assert ucus_son <= hareket_bitis_sinir, f"ucus_son {ucus_son:.3f} > {hareket_bitis_sinir:.3f}"
    assert grup_son <= hareket_bitis_sinir, f"grup_son {grup_son:.3f} > {hareket_bitis_sinir:.3f}"
    assert satir_son <= hareket_bitis_sinir, f"satir_son {satir_son:.3f} > {hareket_bitis_sinir:.3f}"
    assert kart_son <= hareket_bitis_sinir, f"kart_son {kart_son:.3f} > {hareket_bitis_sinir:.3f}"
    assert kunye_ac_son <= hareket_bitis_sinir, f"kunye_ac_son {kunye_ac_son:.3f} > {hareket_bitis_sinir:.3f}"

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
    gu0, gud = Z["grup_ucus"]
    box_kanal = [60.0, 602.0, 291.0, 341.0]
    box_kunye_bandi = [60.0, 960.0, 360.0, 450.0]

    curr_t = u0
    while curr_t <= u0 + ud + 1e-6:
        pt = (curr_t - u0) / ud
        et = _p3_in_out(pt)
        es = _p3_out((curr_t - u0) / Z["ucus_olcek"])

        dx1 = (h1[0] - o1[0]) * et
        dy1 = (h1[1] - o1[1]) * et
        s1 = 1.0 + (hs1 - 1.0) * es
        box_bas1 = [
            o1[0] + dx1 + s1 * (t1x - o1[0]),
            o1[0] + dx1 + s1 * (t1x + g1 - o1[0]),
            o1[1] + dy1 + s1 * (T1 - 0.70 * B - o1[1]),
            o1[1] + dy1 + s1 * (T1 + 0.182 * B - o1[1]),
        ]

        dx2 = (h2[0] - o2[0]) * et
        dy2 = (h2[1] - o2[1]) * et
        s2 = 1.0 + (hs2 - 1.0) * es
        box_hap = [
            o2[0] + dx2 + s2 * (hap_x - o2[0]),
            o2[0] + dx2 + s2 * (hap_x + hap_w - o2[0]),
            o2[1] + dy2 + s2 * (HAP_UST - o2[1]),
            o2[1] + dy2 + s2 * (HAP_ALT - o2[1]),
        ]

        prz = (curr_t - rk0) / rkd
        erz = _p3_in_out(prz)
        curr_rz_x = KENAR + (rz_x - KENAR) * erz
        box_rz0 = [curr_rz_x, curr_rz_x + rz_w, 386.0, 434.0]

        pg = (curr_t - gu0) / gud
        eg = _p3_in_out(pg)
        dx_g = (GT[0] - 80) * eg
        dy_g = (GT[1] - 932) * eg
        sg = 1.0 + (GK - 1.0) * eg
        box_grup = [
            80.0 + dx_g,
            80.0 + dx_g + sg * G[2],
            932.0 + dy_g,
            932.0 + dy_g + sg * G[3],
        ]

        # Bütün uçuş boyunca denetimler:
        if _kesisir(box_grup, box_rz0, 6.0):
            assert False, f"Uçuş çakışması t={curr_t:.3f}: grup x rz0"
        if _kesisir(box_grup, box_kanal, 6.0):
            assert False, f"Uçuş çakışması t={curr_t:.3f}: grup x kanal"
        if _kesisir(box_grup, box_kunye_bandi, 6.0):
            assert False, f"Uçuş çakışması t={curr_t:.3f}: grup x künye bandı"

        # Başlıklar opaklık >= 0.5 iken:
        if curr_t <= Z["baslik_sol"][0] + 0.71 * Z["baslik_sol"][1] + 1e-6:
            c_bas1_hap = _kesisir(box_bas1, box_hap, 6.0)
            c_bas1_rz0 = _kesisir(box_bas1, box_rz0, 6.0)
            c_hap_rz0 = _kesisir(box_hap, box_rz0, 6.0)
            c_grup_bas1 = _kesisir(box_grup, box_bas1, 6.0)
            c_grup_hap = _kesisir(box_grup, box_hap, 6.0)
            c_bas1_kanal = _kesisir(box_bas1, box_kanal, 6.0)
            c_hap_kanal = _kesisir(box_hap, box_kanal, 6.0)
            if any([c_bas1_hap, c_bas1_rz0, c_hap_rz0, c_grup_bas1, c_grup_hap, c_bas1_kanal, c_hap_kanal]):
                assert False, (
                    f"Uçuş çakışması t={curr_t:.3f}: bas1xhap={c_bas1_hap}, bas1xrz0={c_bas1_rz0}, "
                    f"hapxrz0={c_hap_rz0}, grupxbas1={c_grup_bas1}, grupxhap={c_grup_hap}, "
                    f"bas1xkanal={c_bas1_kanal}, hapxkanal={c_hap_kanal}"
                )

        curr_t += 1.0 / 30.0


_denetimler()


# ---- 4.9 zamanlar() fonksiyonu ----
def zamanlar() -> dict:
    """olay.py tarafından okunan olay zamanları."""
    return {
        "soru": Z["soru"],
        "ucus": Z["ucus"],
        "satir": [SATIR_BAS, Z["satir_sure"]],
        "kart": [KART_BAS, Z["kart_sure"]],
    }


# ---- 4.9 uret() fonksiyonu ----
def uret() -> str:
    R = Y.RENK
    g_sat = Y.genislik("Caveat", 700, SATIR, SAT_BOY)

    # Kırpma kutusu
    clips = (
        '<clipPath id="cps">'
        '<rect id="crs" x="48" y="488" width="0" height="97"/>'
        '</clipPath>'
    )

    # Kapak sahne: figür + otobüs + zemin çizgisi
    fig_svg = "".join(
        f'<path transform="translate({p["tx"]:.2f} {p["ty"]:.2f})" d="{p["d"]}" '
        f'stroke-width="4" vector-effect="non-scaling-stroke"/>'
        for p in FIG
    )
    fig_g = f'<g id="fig" transform="translate({FIG_X} {FIG_Y}) scale({FIG_S:.6f})">{fig_svg}</g>'

    otobus_svg = "".join(
        f'<path d="{p["d"]}" stroke-width="4.4" vector-effect="non-scaling-stroke"/>'
        for p in BUS
    )
    otobus_g = f'<g id="otobus" transform="translate(1280 0) scale(-1 1)">{otobus_svg}</g>'

    zc_path = '<path id="zc" d="M80 1372 L950 1372" stroke-width="4" vector-effect="non-scaling-stroke"/>'

    kapak_sahne = (
        f'<g id="kapak-sahne" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-linecap="round" stroke-linejoin="round">'
        f'{fig_g}{otobus_g}{zc_path}</g>'
    )

    # Satır
    satir_svg = (
        f'<text id="satir" x="{SAT_X}" y="{SAT_TABAN}" font-family="Caveat" font-weight="700" '
        f'font-size="{SAT_BOY}" fill="{R["murekkep"]}" clip-path="url(#cps)" '
        f'style="font-kerning:none">{SATIR}</text>'
    )

    # Kart go
    kart_svg = (
        f'<g id="kart-go">'
        f'<rect x="{KART["x"]}" y="{KART["y"]}" width="{KART["w"]}" height="{KART["h"]}" '
        f'rx="{KART["rx"]}" fill="none" stroke="{R["murekkep"]}" stroke-width="{KART["cizgi"]}"/>'
        f'<text x="250" y="750" text-anchor="middle" font-family="Fredoka" font-weight="700" '
        f'font-size="120" fill="{R["murekkep"]}" style="font-kerning:none">{KART_YAZI}</text>'
        f'</g>'
    )

    # Başlık 2 (hap)
    bas2_svg = (
        f'<g id="bas2">'
        f'<rect id="hap" x="{hap_x:.2f}" y="{HAP_UST:.2f}" width="{hap_w:.2f}" height="{hap_h:.2f}" '
        f'rx="{hap_rx:.2f}" fill="{R["vurgu"]}"/>'
        f'<text id="bas2t" x="{t2x:.2f}" y="{T2:.2f}" text-anchor="start" font-family="Fredoka" '
        f'font-weight="700" font-size="{B}" fill="{R["zemin"]}" style="font-kerning:none">{BAS2}</text>'
        f'<path id="soru-kanca" d="{KANCA_D}" fill="none" stroke-width="{SORU_SW:.2f}" '
        f'stroke-linecap="round" stroke-linejoin="round" style="stroke:var(--pilMetin);opacity:0"/>'
        f'<path id="soru-nokta" d="{NOKTA_D}" fill="none" stroke-width="{SORU_SW:.2f}" '
        f'stroke-linecap="round" stroke-linejoin="round" style="stroke:var(--pilMetin);opacity:0"/>'
        f'</g>'
    )

    # Başlık 1
    bas1_svg = (
        f'<g id="bas1">'
        f'<text id="bas1t" x="{t1x:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">{BAS1}</text>'
        f'</g>'
    )

    # Künye ve altyazı
    kunye_svg = Y.kunye_svg()
    alt_svg, alt_zaman, karaoke_zaman = Y.altyazi_svg(0.0, Z["sure"], ALT)

    # GSAP veri sözlüğü (§4.7)
    veri = {
        "Z": Z,
        "alt": alt_zaman,
        "karaoke": karaoke_zaman,
        "rz_kayma": round(KENAR - rz_x, 2),
        "o1": [round(o1[0], 2), round(o1[1], 2)],
        "h1": [round(h1[0], 2), round(h1[1], 2)],
        "hs1": round(hs1, 4),
        "o2": [round(o2[0], 2), round(o2[1], 2)],
        "h2": [round(h2[0], 2), round(h2[1], 2)],
        "hs2": round(hs2, 4),
        "gk": round(GK, 5),
        "gt": [round(GT[0], 2), round(GT[1], 2)],
        "satir_bas": SATIR_BAS,
        "satir_w": round(g_sat + 24, 2),
        "kart_bas": KART_BAS,
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
{satir_svg}
{kart_svg}
{bas2_svg}
{bas1_svg}
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
  gsap.set("#ku-konu", {{ opacity: 0 }});
  gsap.set("#rz0", {{ x: V.rz_kayma }});
  gsap.set("#kart-go", {{ opacity: 0 }});

  // ? hazırlığı (dasharray / dashoffset)
  var sk = $("#soru-kanca");
  if (sk) {{
    var L1 = sk.getTotalLength();
    sk.style.strokeDasharray = L1 + " " + (L1 + 2);
    sk.style.strokeDashoffset = L1;
  }}
  var sn = $("#soru-nokta");
  if (sn) {{
    var L2 = sn.getTotalLength();
    sn.style.strokeDasharray = L2 + " " + (L2 + 2);
    sn.style.strokeDashoffset = L2;
  }}

  // 1. ? kanca ve nokta kalemle çizim (sine.inOut)
  tl.set("#soru-kanca", ac({{ opacity: 1 }}), Z.soru[0]);
  tl.to("#soru-kanca", ac({{ strokeDashoffset: 0, duration: Z.soru[1], ease: "sine.inOut" }}), Z.soru[0]);
  tl.set("#soru-nokta", ac({{ opacity: 1 }}), Z.soru_nokta[0]);
  tl.to("#soru-nokta", ac({{ strokeDashoffset: 0, duration: Z.soru_nokta[1], ease: "sine.inOut" }}), Z.soru_nokta[0]);

  // 2. Altyazı
  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});
  // 2b. Karaoke altçizgisi (03-hyperframes-kaydet kalıbı; okunan sözcük, sözcük çapasıyla)
  V.karaoke.forEach(function (k) {{
    var id = "#" + k[0], uz = k[3], el = $(id);
    if (!el || k[1] >= Z.sure) return;
    el.style.strokeDasharray = uz + " " + (uz + 2);
    el.style.strokeDashoffset = uz;
    tl.set(id, ac({{ opacity: 1 }}), k[1]);
    tl.fromTo(id, {{ strokeDashoffset: uz }},
      ac({{ strokeDashoffset: 0, duration: 0.15, ease: "power2.out" }}), k[1]);
    tl.set(id, ac({{ opacity: 0 }}), k[2]);
  }});

  // 3. Rozet sağa kayar
  tl.to("#rz0", ac({{ x: 0, duration: Z.rozet_kay[1], ease: "power3.inOut" }}), Z.rozet_kay[0]);

  // 4. Uçuş: başlık 1 ve başlık 2 (hap)
  var u0 = Z.ucus[0], ud = Z.ucus[1];
  function uc2(id, o, h, hs) {{
    gsap.set(id, {{ svgOrigin: o[0] + " " + o[1], smoothOrigin: false }});
    tl.to(id, ac({{ x: h[0] - o[0], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ y: h[1] - o[1], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ scale: hs, duration: Z.ucus_olcek, ease: "power3.out" }}), u0);
    tl.to(id, ac({{ opacity: 0, duration: Z.baslik_sol[1], ease: "power1.in" }}), Z.baslik_sol[0]);
  }}
  uc2("#bas1", V.o1, V.h1, V.hs1);
  uc2("#bas2", V.o2, V.h2, V.hs2);

  // 5. Figür + otobüs + zemin grubu küçülüp sağ üste iner
  var gu0 = Z.grup_ucus[0], gud = Z.grup_ucus[1];
  gsap.set("#kapak-sahne", {{ svgOrigin: "80 932", smoothOrigin: false }});
  tl.to("#kapak-sahne", ac({{ x: V.gt[0] - 80, duration: gud, ease: "power3.inOut" }}), gu0);
  tl.to("#kapak-sahne", ac({{ y: V.gt[1] - 932, duration: gud, ease: "power3.inOut" }}), gu0);
  tl.to("#kapak-sahne", ac({{ scale: V.gk, duration: gud, ease: "power3.inOut" }}), gu0);

  // 6. Konu adı açılır
  tl.to("#ku-konu", ac({{ opacity: 1, duration: Z.kunye_ac[1], ease: "power1.out" }}), Z.kunye_ac[0]);

  // 7. Satır kırpmayla soldan yazılır
  tl.fromTo("#crs", {{ attr: {{ width: 0 }} }},
    ac({{ attr: {{ width: V.satir_w }}, duration: Z.satir_sure, ease: "none" }}), V.satir_bas);

  // 8. Kart go girer
  tl.fromTo("#kart-go", {{ y: 24, opacity: 0 }},
    ac({{ y: 0, opacity: 1, duration: Z.kart_sure, ease: "power3.out" }}), V.kart_bas);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html


# ---- 4.9 __main__ bloğu ----
if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_icerik = uret()
    (AD / "proje" / "index.html").write_text(html_icerik, encoding="utf-8")

    g_sat = Y.genislik("Caveat", 700, SATIR, SAT_BOY)

    devir = {
        "satir": {
            "metin": SATIR,
            "font": "Caveat",
            "agirlik": 700,
            "boy": 72,
            "x": 60,
            "taban": 560,
            "sag": round(SAT_X + g_sat, 2),
        },
        "kart_go": {
            "x": 60,
            "y": 620,
            "w": 380,
            "h": 200,
            "rx": 28,
            "cizgi": 4,
            "metin": "go",
            "font": "Fredoka",
            "agirlik": 700,
            "boy": 120,
            "orta_x": 250,
            "taban": 750,
        },
        "grup": {
            "kutu": [
                round(GT[0], 2),
                round(GT[1], 2),
                round(G[2] * GK, 2),
                round(G[3] * GK, 2),
            ],
            "olcek": round(GK, 5),
            "kaynak": [80, 932, 870, 442],
            "figur_kutu": [
                round(GT[0] + (FIG_X - G[0]) * GK, 2),
                round(GT[1] + (FIG_Y - G[1]) * GK, 2),
                round(gw * FIG_S * GK, 2),
                round(FIG_H * GK, 2),
            ],
            "otobus_kutu": [
                round(GT[0] + (BUS_KUTU[0] - G[0]) * GK, 2),
                round(GT[1] + (BUS_KUTU[1] - G[1]) * GK, 2),
                round(BUS_KUTU[2] * GK, 2),
                round(BUS_KUTU[3] * GK, 2),
            ],
            "cizgi_px": {"figur": 4, "otobus": 4.4, "zemin": 4},
            "otobus_ayna": True,
            "figur": "open-peeps/standing-2",
            "otobus": "coco/bus",
        },
        "konu": {
            "metin": Y.KONU,
            "boy": boy,
            "x": 60,
            "taban": 420,
        },
        "rozet": {
            "x": round(rz_x, 2),
            "w": round(rz_w, 2),
        },
        "t": 3.0,
        "not": "huni v2 (15.11): sahne 02 kare 0 = bu son hal",
    }
    (AD / "devir.json").write_text(json.dumps(devir, ensure_ascii=False, indent=2), encoding="utf-8")
    print("devir:", json.dumps(devir, ensure_ascii=False))

"""simple-present-temel-s1b sahne 01 kanca index.html üretici (HyperFrames DİKEY 1080x1920, 102 kare).

SPEC v2 §4 uygulaması (huni v2): kanal katmanı, künye, kapak düzeni, ✗ kalem çizimi,
uçuş, grup küçülmesi, satır yazımı, kart girişi ve devir.json.
Kol b (KBC-0202S1, A/B değişkeni kanca = yanlis-cumle): başlık `MY BROTHER` / `GO.` (hap yok) + kırmızı kalem ✗;
`Kardeşim gider:` satırı ve `go` kartı yerine yanlış cümle kartı `My brother go` / `to school by bus.` (kanca satırı).
Kapak düzeni, figür, otobüs, uçuş, grup küçülmesi, künye ve altyazı kol a ile aynı.
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
assert [w["sozcuk"] for w in SOZ[:7]] == ["My", "brother", "go", "to", "school", "by", "bus."], (
    f"Beklenen ilk 7 sözcük bulunamadı: {[w['sozcuk'] for w in SOZ[:7]]}"
)
ALT = json.loads((ORTAK / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
gw, gh, FIG = Y.peeps("standing-2", 60)

# ---- 4.2 Sabitler ve türetilen ölçüler (§4.2) ----
W, H = Y.W, Y.H
KENAR = Y.HUD["kenar"]
SAG = Y.HUD["sagSinir"]
ORTA = (KENAR + SAG) / 2
BAS1 = "MY BROTHER"
BAS2 = "GO."

B = math.floor(min(190, (SAG - KENAR) / Y.genislik("Fredoka", 700, BAS1, 1)))
g1 = Y.genislik("Fredoka", 700, BAS1, B)
t1x = ORTA - g1 / 2
TOP1 = 472
T1 = TOP1 + 0.70 * B
T2 = T1 + 1.15 * B
g2 = Y.genislik("Fredoka", 700, BAS2, B)
t2x = t1x  # satır 2 sola hizalı (satır 1 ile aynı sol kenar); sağında ✗ (kapak-taslak §2)
# ✗ (kırmızı kalem, iki darbe): satır 2'nin sağ ucunda, büyük harf orta çizgisinde
X_SW = round(0.13 * B, 2)
X_YARI = 0.34 * B
X_CX, X_CY = 870.0, T2 - 0.35 * B
# satır 2 kutusu (GO. + ✗): uçuş merkezi ve ölçeği
S2_SOL = t2x
S2_SAG = X_CX + X_YARI + X_SW / 2
S2_UST = min(T2 - 0.70 * B, X_CY - X_YARI - X_SW / 2)
S2_ALT = max(T2 + 0.182 * B, X_CY + X_YARI + X_SW / 2)
s2_w = S2_SAG - S2_SOL

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

# yanlış cümle kartı (kanca satırı): sahne 02 kare 0'da kalem-paper kutuHazir(70, 630, 880, 220) ile aynı yer
KX, KY, KW, KH = 70, 630, 880, 220
IC, YB1, YB2, EN_BOY = KX + 40, KY + 82, KY + 82 + 92, 72
SATIR1, SATIR2 = "My brother go", "to school by bus."
KART_BAS = Z["ucus"][0] + Z["ucus"][1]  # 2,45: uçuş sonu; satırlar söylendikten sonra
KIRP_X = IC - 12
KIRP_W = max(Y.genislik("Fredoka", 700, s, EN_BOY) for s in (SATIR1, SATIR2)) + 24
BUS_X = IC + Y.genislik("Fredoka", 700, "to school by ", EN_BOY)
BUS_GORUNUR = KART_BAS + Z["satir_sure"] * (BUS_X - KIRP_X) / KIRP_W  # `bus.` kırpmadan bu anda çıkar

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

o2 = ((S2_SOL + S2_SAG) / 2, (S2_UST + S2_ALT) / 2)
h2 = (KONU_SON - UK * gk2 / 2, YK + Z["ucus_ayrik"])
hs2 = UK * gk2 / s2_w

# ---- 4.3 ✗ yolları (kol b; kol a'daki `?` yerine) ----
X1_D = (
    f"M {X_CX - X_YARI:.2f} {X_CY - 0.90 * X_YARI:.2f} "
    f"Q {X_CX + 0.06 * X_YARI:.2f} {X_CY - 0.04 * X_YARI:.2f} {X_CX + X_YARI:.2f} {X_CY + X_YARI:.2f}"
)
X2_D = (
    f"M {X_CX + 0.92 * X_YARI:.2f} {X_CY - X_YARI:.2f} "
    f"Q {X_CX - 0.02 * X_YARI:.2f} {X_CY + 0.10 * X_YARI:.2f} {X_CX - 0.96 * X_YARI:.2f} {X_CY + 0.94 * X_YARI:.2f}"
)


def _kutu_d(x: float, y: float, w: float, h: float) -> list[str]:
    """kalem-paper kutuHazir ile aynı 4 kenar (köşeler hafif taşar); sahne 02 kare 0 ile eş."""
    k = [((x - 6, y + 2), (x + w + 8, y - 2)), ((x + w + 2, y - 8), (x + w - 2, y + h + 9)),
         ((x + w + 7, y + h + 2), (x - 8, y + h - 2)), ((x + 2, y + h + 8), (x - 2, y - 10))]
    return [f"M {a[0]} {a[1]} L {(a[0] + b[0]) / 2 + (1.5 if i % 2 else -1.5):.1f} {(a[1] + b[1]) / 2 + 1.2:.1f} "
            f"L {b[0]} {b[1]}" for i, (a, b) in enumerate(k)]


# ---- 4.8 Denetimler ----
def _denetimler() -> None:
    # 1. B, hap, baslik 1
    assert 140 <= B <= 190, f"B={B} aralık [140, 190] dışı"
    assert S2_SOL >= KENAR - 0.5 and S2_SAG <= SAG - 20, (
        f"satır 2 x={S2_SOL:.2f}..{S2_SAG:.2f} aralık [{KENAR - 0.5}, {SAG - 20}] dışı"
    )
    assert t2x + g2 + 40 <= X_CX - X_YARI - X_SW / 2, f"✗ GO. yazısına yakın: {t2x + g2:.2f}"
    assert t1x >= KENAR and t1x + g1 <= SAG, (
        f"baslik 1 x={t1x:.2f}..{t1x + g1:.2f} aralık [{KENAR}, {SAG}] dışı"
    )
    assert (T1 - 0.70 * B) >= Y.HUD["icerikBas"], (
        f"baslik 1 üstü {T1 - 0.70 * B:.2f} < icerikBas {Y.HUD['icerikBas']}"
    )
    assert S2_ALT <= 900, f"satır 2 altı {S2_ALT:.2f} > 900"
    assert S2_UST >= T1 + 0.20 * B, f"satır 2 üstü {S2_UST:.2f} satır 1 tabanına yakın ({T1:.2f})"

    # 2-3. Karakter sayısı (≤ 24) ve kart yazısının kart içinde kalması
    for s in (BAS1, BAS2, SATIR1, SATIR2):
        assert len(s) <= 24, f"{s!r} {len(s)} > 24 karakter"
    assert KIRP_X + KIRP_W <= KX + KW - 20, f"kart yazısı sağ {KIRP_X + KIRP_W:.2f} > {KX + KW - 20}"

    # 4. Kapak dikey ve yatay
    assert S2_ALT + 24 <= FIG_Y, f"S2_ALT + 24 = {S2_ALT + 24:.2f} > FIG_Y {FIG_Y}"
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
    assert KX - 8 >= KENAR and KX + KW + 8 <= SAG, "KART yatay içerik bandı dışı"
    assert KY - 10 >= Y.HUD["icerikBas"] and KY + KH + 9 <= Y.HUD["icerikSon"], "KART dikey içerik bandı dışı"
    assert KY - 10 >= GT[1] + G[3] * GK + 20, f"KART üstü {KY - 10} küçük gruba yakın ({GT[1] + G[3] * GK:.2f})"

    # 6. Zaman
    carpi_son = Z["carpi2"][0] + Z["carpi2"][1]
    assert carpi_son <= Z["kapak_kare"] / 30.0 - 1.0 / 30.0, (
        f"✗ sonu {carpi_son:.3f} > kapak_kare sınırı {Z['kapak_kare']/30.0 - 1.0/30.0:.3f}"
    )
    assert Z["carpi"][0] >= 0.25, f"✗ başı {Z['carpi'][0]} < 0.25"
    assert carpi_son < SOZ[0]["t0"], f"✗ sonu {carpi_son:.3f} >= SOZ[0].t0 {SOZ[0]['t0']}"
    # ekran metni sesten önce gelmez: kart yazısı `by` bittikten sonra açılır, `bus.` kendi çapasından önce görünmez
    assert KART_BAS >= SOZ[5]["t1"], f"KART_BAS {KART_BAS:.3f} < `by` sonu {SOZ[5]['t1']}"
    assert BUS_GORUNUR >= SOZ[6]["t0"], f"`bus.` {BUS_GORUNUR:.3f}'te görünür < çapa {SOZ[6]['t0']}"

    hareket_bitis_sinir = (Z["kare"] - 12) / 30.0
    ucus_son = Z["ucus"][0] + Z["ucus"][1]
    grup_son = Z["grup_ucus"][0] + Z["grup_ucus"][1]
    satir_son = KART_BAS + Z["satir_sure"]
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
        box_hap = [  # kol b: satır 2 kutusu (GO. + ✗); ad kol a'dan
            o2[0] + dx2 + s2 * (S2_SOL - o2[0]),
            o2[0] + dx2 + s2 * (S2_SAG - o2[0]),
            o2[1] + dy2 + s2 * (S2_UST - o2[1]),
            o2[1] + dy2 + s2 * (S2_ALT - o2[1]),
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
        "carpi": Z["carpi"],
        "ucus": Z["ucus"],
        "satir": [KART_BAS, Z["satir_sure"]],
        "kart": [KART_BAS, Z["kart_sure"]],
    }


# ---- 4.9 uret() fonksiyonu ----
def uret() -> str:
    R = Y.RENK
    k_ust, k_alt = YB1 - 0.95 * EN_BOY, YB2 + 0.30 * EN_BOY

    # Kırpma kutusu (kart yazısı soldan açılır)
    clips = (
        '<clipPath id="cps">'
        f'<rect id="crs" x="{KIRP_X}" y="{k_ust:.1f}" width="0" height="{k_alt - k_ust:.1f}"/>'
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

    # Yanlış cümle kartı: 4 kalem kenarı (ikincil, 4 px) + 2 satır (Fredoka 700 72, kırpmayla)
    kenar = "".join(f'<path id="kk{i}" d="{d}" stroke-width="4"/>' for i, d in enumerate(_kutu_d(KX, KY, KW, KH)))
    yazi = "".join(
        f'<text x="{IC}" y="{y}" font-family="Fredoka" font-weight="700" font-size="{EN_BOY}" '
        f'fill="{R["murekkep"]}" style="font-kerning:none">{s}</text>' for s, y in ((SATIR1, YB1), (SATIR2, YB2))
    )
    kart_svg = (
        f'<g id="kart-yanlis"><g fill="none" stroke="{R["ikincil"]}" stroke-linecap="round" '
        f'stroke-linejoin="round">{kenar}</g><g clip-path="url(#cps)">{yazi}</g></g>'
    )

    # Başlık 2 (kol b: hapsız `GO.` + kalem ✗; ✗ hf_tema ile temaya göre --murekkep)
    # DUZ4 A5 / ST-1 (16.11): ✗ kırmızı → mürekkep (s3b kalıbı; tek vurgu rengi)
    carpi = "".join(
        f'<path id="carpi-{i}" d="{d}" fill="none" stroke="{R["murekkep"]}" stroke-width="{X_SW:.2f}" '
        f'stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>' for i, d in ((1, X1_D), (2, X2_D))
    )
    bas2_svg = (
        f'<g id="bas2">'
        f'<text id="bas2t" x="{t2x:.2f}" y="{T2:.2f}" text-anchor="start" font-family="Fredoka" '
        f'font-weight="700" font-size="{B}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">{BAS2}</text>{carpi}</g>'
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
        "satir_bas": KART_BAS,
        "satir_w": round(KIRP_W, 2),
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
  gsap.set("#kart-yanlis", {{ opacity: 0 }});

  // ✗ hazırlığı (dasharray / dashoffset)
  ["#carpi-1", "#carpi-2"].forEach(function (id) {{
    var el = $(id), L = el.getTotalLength();
    el.style.strokeDasharray = L + " " + (L + 2);
    el.style.strokeDashoffset = L;
  }});

  // 1. ✗ iki darbe kalemle çizim (sine.inOut)
  tl.set("#carpi-1", ac({{ opacity: 1 }}), Z.carpi[0]);
  tl.to("#carpi-1", ac({{ strokeDashoffset: 0, duration: Z.carpi[1], ease: "sine.inOut" }}), Z.carpi[0]);
  tl.set("#carpi-2", ac({{ opacity: 1 }}), Z.carpi2[0]);
  tl.to("#carpi-2", ac({{ strokeDashoffset: 0, duration: Z.carpi2[1], ease: "sine.inOut" }}), Z.carpi2[0]);

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

  // 7. Kart yazısı kırpmayla soldan açılır (iki satır birlikte)
  tl.fromTo("#crs", {{ attr: {{ width: 0 }} }},
    ac({{ attr: {{ width: V.satir_w }}, duration: Z.satir_sure, ease: "none" }}), V.satir_bas);

  // 8. Yanlış cümle kartı girer
  tl.fromTo("#kart-yanlis", {{ y: 24, opacity: 0 }},
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

    devir = {
        "kart_yanlis": {
            "kutu": [KX, KY, KW, KH], "kenar": "kutuHazir", "cizgi": 4, "renk": "ikincil",
            "satirlar": [SATIR1, SATIR2], "font": "Fredoka", "agirlik": 700, "boy": EN_BOY,
            "x": IC, "tabanlar": [YB1, YB2],
            "go_x": round(IC + Y.genislik("Fredoka", 700, "My brother ", EN_BOY), 2),
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
        "not": "huni v2 (15.11) kol b: sahne 02 kare 0 = bu son hal",
    }
    (AD / "devir.json").write_text(json.dumps(devir, ensure_ascii=False, indent=2), encoding="utf-8")
    print("devir:", json.dumps(devir, ensure_ascii=False))

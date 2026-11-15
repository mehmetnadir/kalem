"""simple-present-temel-s3b sahne 01 kanca — A/B kol b, değişken `kanca`, değer `soru` (HyperFrames 1080x1920).

Kol a (`simple-present-temel-s3`) uret.py'sinden türedi (istem KBC-0202S3, 15.11.2026). Kol b farkı yalnız bu sahnededir:
söz `Olumsuzda s nereye gider?` (tek TR parça), başlık `S NEREYE` / `GİDER?`, kapak kartı doğru cümle `He goes.`.
"Olumsuzda" sözüyle karta `doesn't` girer (şapka işareti, sözcükler ayrılır, kırpmayla açılır); kart kol a kartına
(`He doesn't goes.`) yakınsar. `s` sözünde `es` altına sarı kalem, `nereye` sözünde mürekkep `?` (DUZ2 A7: kırmızı ikinci vurgu rengiydi); çıkış kol a kuralıyla.
Son kare = kol a son karesi (altyazı hariç); `devir.json` kol a ile aynı (`t` hariç).
Taslak: `uretim-tutanagi/senaryo-taslak.md` §2, `kapak-taslak.md`.
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

AD: Path = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

P: Path = AD.parent.parent
ORTAK: Path = P / "ortak"
KARAKTER_PNG: Path = ORTAK / "kapak" / "karakter.png"

# ---- 2. Girdi Okuma ----
Z: dict = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
SAH: dict = next(
    s for s in json.loads((P / "zaman.json").read_text(encoding="utf-8"))["sahneler"] if s["klasor"] == AD.name
)
assert SAH["kare"] == Z["kare"], f"zamanlar.json kare {Z['kare']} != zaman.json kare {SAH['kare']}"

_soz_hepsi: list[dict] = json.loads((ORTAK / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
SOZ: list[dict] = [s for s in _soz_hepsi if s.get("cumle") == 1]

_alt_hepsi: list[dict] = json.loads((ORTAK / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
_alt_c1: list[dict] = [a for a in _alt_hepsi if a.get("cumle") == 1]
assert len(_alt_c1) == 1 and _alt_c1[0].get("dil") == "tr", f"cümle 1 altyazısı tek TR parça değil: {_alt_c1}"
ALT_TR: dict = _alt_c1[0]

KART0: str = "He goes."  # kapak kartı (doğru cümle; söylenmez)
KART: str = "He doesn't goes."  # son kart = kol a kartı (sahne 02 kare 0)

assert [s["sozcuk"] for s in SOZ] == ["Olumsuzda", "s", "nereye", "gider?"], (
    f"SOZ sözcük sırası beklenmeyen: {[s['sozcuk'] for s in SOZ]}"
)
assert " ".join(s["sozcuk"] for s in SOZ) == ALT_TR["metin"], (
    f"SOZ ({' '.join(s['sozcuk'] for s in SOZ)!r}) != ALT_TR ({ALT_TR['metin']!r})"
)
S_OLUMSUZ, S_S, S_NEREYE, S_GIDER = SOZ

# ---- 3. Sabitler ve Türetilen Ölçüler (§3) ----
W: int = Y.W
H: int = Y.H
RENK: dict[str, str] = Y.RENK
KENAR: float = float(Y.HUD["kenar"])
SAG: float = float(Y.HUD["sagSinir"])
ORTA: float = (KENAR + SAG) / 2.0

BAS1: str = "S NEREYE"
BAS2: str = "GİDER?"
PAD: float = 0.20
PADY: float = 0.10
ACC: float = 0.93
CED: float = 0.19
CAP: float = 0.70
KONTUR: float = 10.0
G1: float = 18.0
CW: float = 5.0
BAS_UST: float = 468.0
BAS_SON: float = 796.0
B_KOLA: int = 133  # kol a başlık boyu (kol a RAPOR: B = 133, bant sınırı); iki kolda başlığın görsel ağırlığı eşit


def glif_sinir(metin: str) -> tuple[float, float]:
    """Metnin Fredoka 700 glif sınırları (yMin, yMax; em oranı, fontTools glyf)."""
    alt, ust = 0.0, 0.0
    for c in metin:
        for bolge in ("latin", "latin-ext"):
            f = Y._font("Fredoka", 700, bolge)
            g = f.getBestCmap().get(ord(c))
            if g:
                gl = f["glyf"][g]
                gl.recalcBounds(f["glyf"])
                alt, ust = min(alt, gl.yMin / f["head"].unitsPerEm), max(ust, gl.yMax / f["head"].unitsPerEm)
                break
    return alt, ust


B: int = math.floor(min(
    float(B_KOLA),
    (SAG - KENAR - KONTUR) / Y.genislik("Fredoka", 700, BAS1, 1.0),
    (SAG - KENAR) / (Y.genislik("Fredoka", 700, BAS2, 1.0) + 2.0 * PAD),
))

g1: float = Y.genislik("Fredoka", 700, BAS1, B)
t1x: float = ORTA - g1 / 2.0
# Tabanlar kol a formülüyle (iki kolda aynı y). Kol b satır 1'de nokta/çengel yok; satır 2'de İ noktası hap içinde.
T1: float = BAS_UST + KONTUR / 2.0 + ACC * B
T2: float = T1 + (CED + PADY + CAP) * B + KONTUR / 2.0 + G1 + CW / 2.0
HAP_PAY: float = (CED + PADY) * B  # alt pay kol a ile aynı; üst pay eşit (büyük harf hapta ortalı)
HAP_UST: float = T2 - CAP * B - HAP_PAY
HAP_ALT: float = T2 + HAP_PAY
B1_ALT, B1_UST = glif_sinir(BAS1)
B2_ALT, B2_UST = glif_sinir(BAS2)

g2: float = Y.genislik("Fredoka", 700, BAS2, B)
hap_w: float = g2 + 2.0 * PAD * B
hap_x: float = ORTA - hap_w / 2.0
hap_h: float = HAP_ALT - HAP_UST
hap_rx: float = hap_h / 2.0

KB: int = 80
KX: float = 60.0
KY: float = 840.0
KH: float = 160.0
KRX: float = 18.0
KPS: float = 40.0
KPD: float = 56.0
g_kart: float = Y.genislik("Fredoka", 700, KART, KB)
KW: float = KPS + g_kart + KPD
KSON: float = KX + KW
KYX: float = KX + KPS
KTABAN: float = KY + 108.0
KY_SON: float = 480.0
DY: float = KY_SON - KY
KK_Y: float = KTABAN + 24.0


def gk(metin: str) -> float:
    """Kart yazısı (Fredoka 700, KB) ilerleme genişliği."""
    return Y.genislik("Fredoka", 700, metin, KB)


# Kart sözcükleri: son konum kol a'nın tek yazısıyla aynı (kerning yok, ilerleme genişliği toplamı).
X_HE1: float = KYX
X_DOESNT: float = KYX + gk("He ")
X_GOES1: float = KYX + gk("He doesn't ")
G_HE, G_DOESNT, G_GOES = gk("He"), gk("doesn't"), gk("goes.")
# Kapak kartı `He goes.` kartta ortalı.
X_HE0: float = KX + KW / 2.0 - gk(KART0) / 2.0
X_GOES0: float = X_HE0 + gk("He ")
# `es` (goes içindeki ek) altı sarı kalem çizgisi.
X_ES0: float = KYX + gk("He doesn't go")
X_ES1: float = X_ES0 + gk("es")
# Şapka işareti `‸`: ilk boşluğun ortasında, tabanın altında (mürekkep kalem).
SAPKA_X: float = (X_HE0 + G_HE + X_GOES0) / 2.0
SAPKA_UST, SAPKA_ALT, SAPKA_YARI = KTABAN + 10.0, KTABAN + 40.0, 16.0
# `doesn't` kırpma kutusu (soldan sağa açılır).
KIRP_X, KIRP_Y, KIRP_W, KIRP_H = X_DOESNT - 4.0, KY + 6.0, G_DOESNT + 8.0, KH - 12.0

QW: float = 56.0
QH: float = 100.0
QX: float = KSON - 4.0 - QW / 2.0
QY: float = KY - 24.0

KENAR_PX: float = 10.0
KENAR_GECIS: int = 3
ESIK: int = 64
KAR_SOL: float = KSON + 20.0 + KENAR_PX

ALT_Y: float = float(Y.HUD["altyaziBas"]) + 84.0
ALT_ORTA: float = float(Y.HUD["altyaziOrta"])
ICERIK_SON: float = (float(Z["kare"]) - 12.0) / 30.0
# Çıkış kol a kuralıyla: son söz sonu − cikis_sure; son söz sesin bitişini (cümle sonu) aşarsa içerik sonu sınırdır.
C0: float = round(min(S_GIDER["t1"], ICERIK_SON) - float(Z["cikis_sure"]), 4)

# Ekleme zamanları ("Olumsuzda" sözüne bağlı; ofset, süre)
T_OL0, T_OL1 = S_OLUMSUZ["t0"], S_OLUMSUZ["t1"]
SAPKA_T: float = round(T_OL0 + float(Z["sapka"][0]), 4)
KAY_T: float = round(T_OL0 + float(Z["kay"][0]), 4)
AC_T: float = round(T_OL0 + float(Z["doesnt_ac"][0]), 4)
SAPKA_SOL_T: float = round(T_OL1 - float(Z["sapka_sol"]), 4)
ES_T0: float = S_S["t0"]
ES_T1: float = round(min(S_S["t1"], S_NEREYE["t0"] - float(Z["karaoke_ara"])), 4)


# ---- Karakter ve Maske İşlevleri (§7) ----
def alfa_kutusu(yol: Path) -> tuple[int, int, int, int]:
    """PNG'nin saydam olmayan kutusu (x0, y0, x1, y1)."""
    a = Image.open(yol).split()[-1].point(lambda v: 255 if v > ESIK else 0)
    kutu = a.getbbox()
    assert kutu is not None, f"{yol.name} tamamen saydam"
    return kutu


ax0, ay0, ax1, ay1 = alfa_kutusu(KARAKTER_PNG)
KS: float = (SAG - KENAR_PX - 2.0 - KAR_SOL) / float(ax1 - ax0)
KAR_X0: float = KAR_SOL - ax0 * KS
DAIRE_CX: float = (KSON + 20.0 + SAG) / 2.0
DAIRE_R: float = (SAG - (KSON + 20.0)) / 2.0 - 2.0


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


def maske_kutusu(m: np.ndarray) -> tuple[int, int, int, int]:
    """Maskenin tuvaldeki kutusu (x0, y0, x1, y1)."""
    ys, xs = np.nonzero(m)
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


KART_KUTU: tuple[float, float, float, float] = (KX, KY, KX + KW, KY + KH)
SORU_KUTU: tuple[float, float, float, float] = (QX - 5.0, QY - 5.0, QX + QW + 5.0, QY + 99.0)


def karakter_ustu() -> float:
    """Alfa üstü 880'den 2 px adımla iner; kart ve ? kutusuna KENAR_PX + 16 pay kalan ilk y (şef QA tur 1).
    DUZ2 (16.11): daire merkezi de ? kutusuna DAIRE_R + 16 uzak olmalı (denetim 5 aramaya alındı; kadın karakter
    eski görselden kısa, 880'de sığıyor ama daire ? kutusuna yaklaşıyordu)."""
    for ust in range(880, 1001, 2):
        m = maske(KARAKTER_PNG, KAR_X0, ust - ay0 * KS, KS)
        cy = ust + 0.372 * (ay1 - ay0) * KS
        dx = max(SORU_KUTU[0] - DAIRE_CX, 0.0, DAIRE_CX - SORU_KUTU[2])
        dy = max(SORU_KUTU[1] - cy, 0.0, cy - SORU_KUTU[3])
        if (bos_mu(m, KART_KUTU, KENAR_PX + 16.0) and bos_mu(m, SORU_KUTU, KENAR_PX + 16.0)
                and math.hypot(dx, dy) >= DAIRE_R + 16.0):
            return float(ust)
    raise ValueError(f"karakter 880–1000 arasında ? ve kartla çakışmadan yer bulamadı (KS={KS:.4f})")


KAR_UST: float = karakter_ustu()
KAR_Y0: float = KAR_UST - ay0 * KS
KAR_W, KAR_H = Image.open(KARAKTER_PNG).size  # DUZ2 (16.11): görsel boyu dosyadan (kadın karakter 1024×1024; eskisi 896×1200)
# Daire merkezi alfa kutusunun üst %37,2 noktası (eski görselde 470 px = 89 + 0,372 × 1024; oran korunur).
DAIRE_CY: float = KAR_Y0 + (ay0 + 0.372 * (ay1 - ay0)) * KS


def daire_kutu_uzakligi(cx: float, cy: float, k: tuple[float, float, float, float]) -> float:
    """Daire merkezinin kutuya en kısa uzaklığı."""
    dx = max(k[0] - cx, 0.0, cx - k[2])
    dy = max(k[1] - cy, 0.0, cy - k[3])
    return math.hypot(dx, dy)


def _p3_in_out(p: float) -> float:
    """power3.inOut Python karşılığı (4. derece S-eğrisi)."""
    p = max(0.0, min(1.0, p))
    return 8.0 * (p ** 4) if p < 0.5 else 1.0 - 8.0 * ((1.0 - p) ** 4)


def _p2_in_out(p: float) -> float:
    """power2.inOut Python karşılığı (kübik S-eğrisi)."""
    p = max(0.0, min(1.0, p))
    return 4.0 * (p ** 3) if p < 0.5 else 1.0 - 4.0 * ((1.0 - p) ** 3)


def _kesisir(
    b1: list[float] | tuple[float, ...],
    b2: list[float] | tuple[float, ...],
    pay: float = 6.0,
) -> bool:
    """İki kutunun pay ile kesişip kesişmediği (b = [x0, x1, y0, y1])."""
    return not (
        b1[1] + pay <= b2[0]
        or b2[1] + pay <= b1[0]
        or b1[3] + pay <= b2[2]
        or b2[3] + pay <= b1[2]
    )


# ---- 4. Denetimler (§7) ----
def _denetimler() -> None:
    # 1. Başlık
    assert 100 <= B <= 190, f"B={B} aralık [100, 190] dışı"
    assert t1x - KONTUR / 2.0 >= KENAR, f"t1x - KONTUR/2={t1x - KONTUR / 2.0:.2f} < KENAR {KENAR}"
    assert t1x + g1 + KONTUR / 2.0 <= SAG, f"t1x + g1 + KONTUR/2={t1x + g1 + KONTUR / 2.0:.2f} > SAG {SAG}"
    assert hap_x >= KENAR, f"hap_x={hap_x:.2f} < KENAR {KENAR}"
    assert hap_x + hap_w <= SAG, f"hap_x + hap_w={hap_x + hap_w:.2f} > SAG {SAG}"
    b1_ust = T1 - B1_UST * B - KONTUR / 2.0
    assert b1_ust >= BAS_UST - 0.5, f"satır 1 üstü {b1_ust:.2f} < BAS_UST {BAS_UST}"
    assert HAP_ALT + CW / 2.0 <= BAS_SON + 0.5, (
        f"HAP_ALT + CW/2={HAP_ALT + CW / 2.0:.2f} > BAS_SON {BAS_SON}"
    )
    b1_alt = T1 - B1_ALT * B + KONTUR / 2.0
    assert b1_alt + 12.0 <= HAP_UST - CW / 2.0, (
        f"satır 1 altı + 12={b1_alt + 12.0:.2f} > HAP_UST - CW/2 {HAP_UST - CW / 2.0:.2f}"
    )
    i_nokta = T2 - B2_UST * B
    assert i_nokta >= HAP_UST + CW / 2.0 + 4.0, (
        f"İ noktası üstü {i_nokta:.2f} hap iç kenarına 4 px'ten yakın (HAP_UST + CW/2 = {HAP_UST + CW / 2.0:.2f})"
    )
    assert T2 - B2_ALT * B <= HAP_ALT - CW / 2.0 - 4.0, "satır 2 alt taşması hap iç kenarına 4 px'ten yakın"

    # 2. Kart
    assert len(KART) <= 24, f"len(KART)={len(KART)} > 24"
    assert KB >= 72, f"KB={KB} < 72"
    assert KSON <= SAG, f"KSON={KSON:.2f} > SAG {SAG}"
    assert KY - (HAP_ALT + CW / 2.0) >= 24.0, (
        f"KY - (HAP_ALT + CW/2)={KY - (HAP_ALT + CW / 2.0):.2f} < 24"
    )
    assert KYX >= KX + 8.0, f"KYX={KYX:.2f} < KX + 8 {KX + 8.0}"
    assert KYX + g_kart <= KX + KW - 8.0, f"KYX + g_kart={KYX + g_kart:.2f} > KX + KW - 8 {KX + KW - 8.0:.2f}"
    assert KTABAN - CAP * KB >= KY + 8.0, f"KTABAN - CAP*KB={KTABAN - CAP * KB:.2f} < KY + 8 {KY + 8.0}"
    assert KTABAN + 0.22 * KB <= KY + KH - 8.0, (
        f"KTABAN + 0.22*KB={KTABAN + 0.22 * KB:.2f} > KY + KH - 8 {KY + KH - 8.0}"
    )
    assert KK_Y + 3.0 <= KY + KH - 8.0, f"KK_Y + 3={KK_Y + 3.0:.2f} > KY + KH - 8 {KY + KH - 8.0}"
    assert abs(X_GOES1 + G_GOES - (KYX + g_kart)) < 1e-6, "kart sözcük toplamı tek yazı genişliğine eşit değil"
    assert X_HE0 >= KX + 8.0 and X_GOES0 + G_GOES <= KX + KW - 8.0, "kapak kartı yazısı kartın içinde değil"
    assert SAPKA_ALT + 3.0 <= KY + KH - 8.0, f"şapka altı {SAPKA_ALT + 3.0:.2f} > KY + KH - 8"
    assert KIRP_X >= X_HE1 + G_HE and KIRP_X + KIRP_W <= X_GOES1, "doesn't kırpması son konumda komşulara taşıyor"
    assert KY_SON >= float(Y.HUD["icerikBas"]) + 20.0, (
        f"KY_SON={KY_SON} < icerikBas + 20 {float(Y.HUD['icerikBas']) + 20.0}"
    )
    assert KY_SON + KH <= float(Y.HUD["icerikSon"]), (
        f"KY_SON + KH={KY_SON + KH} > icerikSon {float(Y.HUD['icerikSon'])}"
    )

    # 3. ?
    assert QY - 5.0 >= HAP_ALT + CW / 2.0 + 12.0, (
        f"QY - 5={QY - 5.0:.2f} < HAP_ALT + CW/2 + 12 {HAP_ALT + CW / 2.0 + 12.0:.2f}"
    )
    assert QX >= KYX + g_kart + 16.0, f"QX={QX:.2f} < KYX + g_kart + 16 {KYX + g_kart + 16.0:.2f}"
    assert QX + QW + 5.0 <= SAG, f"QX + QW + 5={QX + QW + 5.0:.2f} > SAG {SAG}"

    # 4. Karakter
    if KS < 0.25:
        raise ValueError(f"KS={KS:.4f} < 0.25 (KSON={KSON:.2f})")
    m = maske(KARAKTER_PNG, KAR_X0, KAR_Y0, KS)
    mx0, my0, mx1, my1 = maske_kutusu(m)
    assert mx0 >= KSON + 20.0 + KENAR_PX - 1.0, (
        f"mx0={mx0} < KSON + 20 + KENAR_PX - 1 {KSON + 20.0 + KENAR_PX - 1.0:.2f}"
    )
    assert mx1 + KENAR_PX <= SAG, f"mx1 + KENAR_PX={mx1 + KENAR_PX} > SAG {SAG}"
    assert my0 >= KY + 20.0, f"my0={my0} < KY + 20 {KY + 20.0}"
    assert my1 + KENAR_PX <= float(Y.HUD["icerikSon"]), (
        f"my1 + KENAR_PX={my1 + KENAR_PX} > icerikSon {float(Y.HUD['icerikSon'])}"
    )

    kart_kutu = (float(KX), float(KY), float(KX + KW), float(KY + KH))
    soru_kutu = (float(QX - 5.0), float(QY - 5.0), float(QX + QW + 5.0), float(QY + 99.0))
    assert bos_mu(m, kart_kutu, KENAR_PX + 16.0), "karakter kart kutusu ile çakışıyor"
    assert bos_mu(m, soru_kutu, KENAR_PX + 16.0), "karakter soru kutusu ile çakışıyor"

    # 5. Daire
    assert DAIRE_CX - DAIRE_R >= KSON + 20.0, (
        f"DAIRE_CX - DAIRE_R={DAIRE_CX - DAIRE_R:.2f} < KSON + 20 {KSON + 20.0:.2f}"
    )
    assert DAIRE_CX + DAIRE_R <= SAG, f"DAIRE_CX + DAIRE_R={DAIRE_CX + DAIRE_R:.2f} > SAG {SAG}"
    assert DAIRE_CY - DAIRE_R >= HAP_ALT + 24.0, (
        f"DAIRE_CY - DAIRE_R={DAIRE_CY - DAIRE_R:.2f} < HAP_ALT + 24 {HAP_ALT + 24.0:.2f}"
    )
    assert DAIRE_CY + DAIRE_R <= float(Y.HUD["icerikSon"]), (
        f"DAIRE_CY + DAIRE_R={DAIRE_CY + DAIRE_R:.2f} > icerikSon {float(Y.HUD['icerikSon'])}"
    )
    assert daire_kutu_uzakligi(DAIRE_CX, DAIRE_CY, soru_kutu) >= DAIRE_R + 16.0, (
        f"daire merkezinin soru kutusuna uzaklığı < DAIRE_R + 16 ({DAIRE_R + 16.0:.2f})"
    )

    # 6. Altyazı
    g_alt_tr = Y.genislik("Lexend", 500, ALT_TR["metin"], 44.0)
    assert g_alt_tr <= float(Y.HUD["altyaziGen"]), (
        f"g_alt_tr={g_alt_tr:.2f} > altyaziGen {float(Y.HUD['altyaziGen'])}"
    )
    assert ALT_Y + 0.25 * 44.0 <= float(Y.HUD["altyaziSon"]), (
        f"ALT_Y + 0.25*44={ALT_Y + 0.25 * 44.0:.2f} > altyaziSon {float(Y.HUD['altyaziSon'])}"
    )
    assert ALT_Y - 0.75 * 44.0 >= float(Y.HUD["altyaziBas"]), (
        f"ALT_Y - 0.75*44={ALT_Y - 0.75 * 44.0:.2f} < altyaziBas {float(Y.HUD['altyaziBas'])}"
    )

    # 7. Zaman
    cerceve_bitis = float(Z["cerceve"][0]) + float(Z["cerceve"][1])
    assert cerceve_bitis < SOZ[0]["t0"] - 0.1, (
        f"cerceve_bitis {cerceve_bitis:.3f} >= SOZ[0].t0 - 0.1 ({SOZ[0]['t0'] - 0.1:.3f})"
    )
    assert cerceve_bitis <= float(Z["kapak_t"]) - 1.0 / 30.0, (
        f"cerceve_bitis {cerceve_bitis:.3f} > kapak_t - 1/30 ({float(Z['kapak_t']) - 1.0 / 30.0:.3f})"
    )
    assert float(Z["kapak_t"]) < min(SAPKA_T, KAY_T, AC_T), "kapak karesinde ekleme başlamış"
    # Ekran metni sesten önce gelmez: doesn't "Olumsuzda" başladıktan sonra açılır ve söz bitmeden tamdır.
    assert AC_T >= T_OL0, f"doesn't açılışı {AC_T:.3f} < Olumsuzda t0 {T_OL0:.3f}"
    assert KAY_T + float(Z["kay"][1]) <= AC_T + 1e-6, "doesn't açılmadan önce sözcük kayması bitmeli (kırpma × He)"
    assert AC_T + float(Z["doesnt_ac"][1]) <= SAPKA_SOL_T + 1e-6, "doesn't açılışı şapka sönmeden bitmeli"
    assert SAPKA_T + float(Z["sapka"][1]) <= SAPKA_SOL_T, "şapka çizimi sönmeden önce bitmeli"
    assert T_OL1 <= S_S["t0"], "şapka `s` sözünden önce sönmeli"
    assert ES_T0 + float(Z["es_ciz"]) <= ES_T1, f"es çizgisi {ES_T0:.3f}+{Z['es_ciz']} > kapanış {ES_T1:.3f}"
    soru_toplam = round(float(Z["soru_kanca"]) + float(Z["soru_ara"]) + float(Z["soru_nokta"]), 4)
    assert soru_toplam <= float(Z["soru_en_cok"]), (
        f"soru_toplam {soru_toplam:.3f} > soru_en_cok {float(Z['soru_en_cok']):.3f}"
    )
    soru_bitis = round(S_NEREYE["t0"] + soru_toplam, 4)
    assert soru_bitis <= S_GIDER["t1"], f"soru_bitis {soru_bitis:.3f} > gider?.t1 {S_GIDER['t1']:.3f}"
    assert soru_bitis <= C0 + 1e-6, f"soru_bitis {soru_bitis:.3f} > çıkış başı {C0:.3f}"
    assert C0 + float(Z["cikis_sure"]) <= ICERIK_SON + 1e-6, (
        f"C0 + cikis_sure {C0 + float(Z['cikis_sure']):.3f} > (kare-12)/30 {ICERIK_SON:.4f}"
    )
    assert C0 >= S_GIDER["t0"], f"C0 {C0:.3f} < gider?.t0 {S_GIDER['t0']:.3f}"
    assert abs(float(Z["sure"]) - float(Z["kare"]) / 30.0) < 1e-4, "abs(Z.sure - Z.kare / 30) >= 1e-4 (4 ondalık)"

    # 8. Ekleme örneklemesi: kayan He ve goes. kırpılmış doesn't ile kesişmez (kayma açılmadan önce biter).
    t = KAY_T
    while t <= AC_T + float(Z["doesnt_ac"][1]) + 1e-6:
        p = _p2_in_out((t - KAY_T) / float(Z["kay"][1]))
        he, go = X_HE0 + (X_HE1 - X_HE0) * p, X_GOES0 + (X_GOES1 - X_GOES0) * p
        pa = max(0.0, min(1.0, (t - AC_T) / float(Z["doesnt_ac"][1])))
        if pa > 0.0:
            assert he + G_HE <= KIRP_X, f"t={t:.3f}: He kırpılmış doesn't ile kesişiyor"
            assert KIRP_X + KIRP_W * pa <= go, f"t={t:.3f}: goes. kırpılmış doesn't ile kesişiyor"
        t += 1.0 / 30.0

    # 9. Çıkış örneklemesi
    box_bas1 = [t1x, t1x + g1, T1 - B1_UST * B, T1 - B1_ALT * B]
    box_hap = [hap_x, hap_x + hap_w, HAP_UST - CW / 2.0, HAP_ALT + CW / 2.0]
    box_kunye_bandi = [60.0, 960.0, 360.0, 450.0]
    box_kanal = [60.0, 602.0, 291.0, 341.0]

    curr_t = C0
    cikis_sure_val = float(Z["cikis_sure"])
    while curr_t <= C0 + cikis_sure_val + 1e-6:
        p = max(0.0, min(1.0, (curr_t - C0) / cikis_sure_val))
        dy = DY * _p3_in_out(p)
        pb = max(0.0, min(1.0, (curr_t - C0) / float(Z["baslik_sol"])))
        ps = max(0.0, min(1.0, (curr_t - C0) / float(Z["soru_sol"])))
        op_bas = 1.0 - pb ** 2  # power1.in sönme (#baslik)
        op_soru = 1.0 - ps ** 2  # power1.in sönme (#soru)

        box_kart_yazi = [KYX, KYX + g_kart, KTABAN - CAP * KB + dy, KTABAN + 0.22 * KB + dy]
        box_kart = [float(KX), float(KSON), KY + dy, KY + KH + dy]
        box_soru_ornek = [QX - 5.0, QX + QW + 5.0, QY - 5.0 + dy, QY + 99.0 + dy]

        if op_bas >= 0.5:
            assert not _kesisir(box_kart_yazi, box_bas1, 6.0), (
                f"Çıkış çakışması t={curr_t:.3f}: kart_yazi x baslik1"
            )
            assert not _kesisir(box_kart_yazi, box_hap, 6.0), (
                f"Çıkış çakışması t={curr_t:.3f}: kart_yazi x hap"
            )
        if op_bas >= 0.5 and op_soru >= 0.5:
            assert not _kesisir(box_soru_ornek, box_bas1, 6.0), (
                f"Çıkış çakışması t={curr_t:.3f}: soru x baslik1"
            )
            assert not _kesisir(box_soru_ornek, box_hap, 6.0), (
                f"Çıkış çakışması t={curr_t:.3f}: soru x hap"
            )

        assert not _kesisir(box_kart, box_kunye_bandi, 6.0), (
            f"Çıkış çakışması t={curr_t:.3f}: kart x künye bandı"
        )
        assert not _kesisir(box_kart, box_kanal, 6.0), (
            f"Çıkış çakışması t={curr_t:.3f}: kart x kanal"
        )

        curr_t += 1.0 / 30.0


_denetimler()


# ---- 5. Çıktı İşlevleri (§8) ----
def zamanlar() -> dict:
    """olay.py tarafından okunan olay zamanları."""
    soru_toplam = round(float(Z["soru_kanca"]) + float(Z["soru_ara"]) + float(Z["soru_nokta"]), 4)
    return {
        "cerceve": [float(Z["cerceve"][0]), float(Z["cerceve"][1])],
        "soru": [S_NEREYE["t0"], soru_toplam],
        "cikis": [C0, float(Z["cikis_sure"])],
        "sapka": [SAPKA_T, float(Z["sapka"][1])],
        "es": [ES_T0, ES_T1],
    }


def uret() -> str:
    """Tam index.html çıktısını üretir."""
    # 1. Hap çerçevesi yolu
    k = 0.5523
    cx_sag = hap_x + hap_w - hap_rx
    cy_hap = HAP_UST + hap_rx
    cx_sol = hap_x + hap_rx

    cerceve_d = (
        f"M{hap_x + hap_rx:.2f} {HAP_UST:.2f} "
        f"L{hap_x + hap_w - hap_rx:.2f} {HAP_UST:.2f} "
        f"C{cx_sag + k * hap_rx:.2f} {HAP_UST:.2f}, "
        f"{cx_sag + hap_rx:.2f} {cy_hap - k * hap_rx:.2f}, "
        f"{cx_sag + hap_rx:.2f} {cy_hap:.2f} "
        f"C{cx_sag + hap_rx:.2f} {cy_hap + k * hap_rx:.2f}, "
        f"{cx_sag + k * hap_rx:.2f} {HAP_ALT:.2f}, "
        f"{cx_sag:.2f} {HAP_ALT:.2f} "
        f"L{hap_x + hap_rx:.2f} {HAP_ALT:.2f} "
        f"C{cx_sol - k * hap_rx:.2f} {HAP_ALT:.2f}, "
        f"{cx_sol - hap_rx:.2f} {cy_hap + k * hap_rx:.2f}, "
        f"{cx_sol - hap_rx:.2f} {cy_hap:.2f} "
        f"C{cx_sol - hap_rx:.2f} {cy_hap - k * hap_rx:.2f}, "
        f"{cx_sol - k * hap_rx:.2f} {HAP_UST:.2f}, "
        f"{cx_sol:.2f} {HAP_UST:.2f} "
        f"L{hap_x + hap_rx + 36.0:.2f} {HAP_UST:.2f}"
    )

    baslik_svg = (
        f'<g id="baslik">'
        f'<text id="bas1t" x="{t1x:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" font-size="{B}" '
        f'fill="{RENK["murekkep"]}" stroke="#1b1a17" stroke-width="{KONTUR}" stroke-linejoin="round" '
        f'style="font-kerning:none;paint-order:stroke fill">{BAS1}</text>'
        f'<rect id="hap" x="{hap_x:.2f}" y="{HAP_UST:.2f}" width="{hap_w:.2f}" height="{hap_h:.2f}" '
        f'rx="{hap_rx:.2f}" fill="{RENK["vurgu"]}"/>'
        # GİDER? iki parça (Gİ + DER?), konum tek yazıyla aynı (kerning yok): İ noktası tek kutuyu köşeye dek yükseltir,
        # yarım çerçevenin köşe yayı o kutu köşesini keser (kapı 0,50 sn); mürekkepte kesişme yok.
        f'<text id="bas2t" x="{ORTA - g2 / 2.0:.2f}" y="{T2:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="#1b1a17" style="font-kerning:none">{BAS2[:2]}</text>'
        f'<text id="bas2u" x="{ORTA - g2 / 2.0 + Y.genislik("Fredoka", 700, BAS2[:2], B):.2f}" y="{T2:.2f}" '
        f'font-family="Fredoka" font-weight="700" font-size="{B}" fill="#1b1a17" style="font-kerning:none">{BAS2[2:]}</text>'
        f'<path id="cerceve" d="{cerceve_d}" fill="none" stroke="{RENK["murekkep"]}" stroke-width="{CW}" '
        f'stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>'
        f'</g>'
    )

    # 2. Kart: sözcükler (He, doesn't, goes.), doesn't kırpması, şapka, es çizgisi
    yo = f'font-family="Fredoka" font-weight="700" font-size="{KB}" fill="#1b1a17" style="font-kerning:none"'
    kart_yazi = (
        f'<text id="kw-he" x="{X_HE0:.2f}" y="{KTABAN:.1f}" {yo}>He</text>'
        f'<text id="kw-doesnt" x="{X_DOESNT:.2f}" y="{KTABAN:.1f}" clip-path="url(#doesnt-kirp)" {yo}>doesn&apos;t</text>'
        f'<text id="kw-goes" x="{X_GOES0:.2f}" y="{KTABAN:.1f}" {yo}>goes.</text>'
    )
    kirp_svg = (
        f'<defs><clipPath id="doesnt-kirp" clipPathUnits="userSpaceOnUse"><rect id="doesnt-kirp-r" '
        f'x="{KIRP_X:.2f}" y="{KIRP_Y:.1f}" width="0" height="{KIRP_H:.1f}"/></clipPath></defs>'
    )
    sapka_d = f"M{SAPKA_X - SAPKA_YARI:.2f} {SAPKA_ALT:.1f} L{SAPKA_X:.2f} {SAPKA_UST:.1f} L{SAPKA_X + SAPKA_YARI:.2f} {SAPKA_ALT:.1f}"
    sapka_svg = (
        f'<path id="sapka" d="{sapka_d}" fill="none" stroke="#1b1a17" stroke-width="6" '
        f'stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>'
    )
    es_svg = (
        f'<path id="es-cizgi" d="M{X_ES0 - 2.0:.2f} {KK_Y:.2f} L{X_ES1 + 2.0:.2f} {KK_Y:.2f}" '
        f'stroke="{RENK["vurgu"]}" stroke-width="6" stroke-linecap="round" style="opacity:0"/>'
    )
    karaoke_ara = float(Z["karaoke_ara"])

    # 3. Soru SVG
    soru_svg = (
        f'<g id="soru" transform="translate({QX:.2f} {QY:.2f})">'
        f'<path id="soru-kanca" d="M3 27 C3 11 15 2 29 2 C44 2 54 12 54 27 C54 41 44 47 35 53 C29 57 28 63 28 72" '
        f'fill="none" stroke="{RENK["murekkep"]}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" '
        f'style="opacity:0"/>'
        f'<circle id="soru-nokta" cx="28" cy="92" r="6.5" fill="{RENK["murekkep"]}" style="opacity:0"/>'
        f'</g>'
    )

    kart_g_svg = (
        f'<g id="kart-g">'
        f'{kirp_svg}'
        f'<rect id="kart-zemin" x="{KX:.1f}" y="{KY:.1f}" width="{KW:.2f}" height="{KH:.1f}" rx="{KRX:.1f}" '
        f'stroke="#1b1a17" stroke-width="4"/>'
        f'{kart_yazi}{sapka_svg}{es_svg}'
        f'{soru_svg}'
        f'</g>'
    )

    # 4. Altyazı ve Karaoke
    alt_elements: list[str] = []
    aw_bilgi: list[list] = []
    ak_bilgi: list[list] = []
    altyazi_sozcukler = SOZ

    g_tr_toplam = Y.genislik("Lexend", 500, ALT_TR["metin"], 44.0)
    x0_alt = ALT_ORTA - g_tr_toplam / 2.0
    altyazi_on = float(Z["altyazi_on"])
    t_kapat = min(float(ALT_TR["t1"]) + float(Z["altyazi_kuyruk"]), float(Z["sure"]))
    oneki_alt = ""

    for i, s in enumerate(altyazi_sozcukler):
        w_metin = s["sozcuk"]
        x_i = x0_alt + Y.genislik("Lexend", 500, oneki_alt, 44.0)
        oneki_alt += w_metin + " "

        temiz = re.sub(r"[.,?!]+$", "", w_metin)
        g_temiz = Y.genislik("Lexend", 500, temiz, 44.0)

        ak_x0 = x_i - 2.0
        ak_x1 = x_i + g_temiz + 2.0
        ak_y = ALT_Y + 10.0

        alt_elements.append(
            f'<path id="ak{i}" d="M{ak_x0:.2f} {ak_y:.2f} L{ak_x1:.2f} {ak_y:.2f}" stroke="{RENK["vurgu"]}" '
            f'stroke-width="5" stroke-linecap="round" style="opacity:0"/>'
        )
        alt_elements.append(
            f'<text id="aw{i}" x="{x_i:.2f}" y="{ALT_Y:.2f}" text-anchor="start" font-family="Lexend" '
            f'font-weight="500" font-size="44" fill="{RENK["murekkep"]}" '
            f'style="opacity:0;font-kerning:none">{w_metin}</text>'
        )

        t_aw_ac = max(0.0, s["t0"] - altyazi_on)
        aw_bilgi.append([f"aw{i}", round(t_aw_ac, 3), round(t_kapat, 3)])

        if i < len(altyazi_sozcukler) - 1:
            bitis_k = min(s["t1"], altyazi_sozcukler[i + 1]["t0"] - karaoke_ara)
        else:
            bitis_k = s["t1"]
        ak_bilgi.append([f"ak{i}", round(s["t0"], 3), round(bitis_k, 3)])

    altyazi_svg = "".join(alt_elements)

    # 5. Kenar drop-shadow CSS
    adim: float = KENAR_PX / KENAR_GECIS
    kenar_filter: str = " ".join(
        f"drop-shadow({dx:.2f}px {dy:.2f}px 0 #f3efe6)"
        for _ in range(KENAR_GECIS)
        for dx, dy in ((adim, 0.0), (-adim, 0.0), (0.0, adim), (0.0, -adim))
    )

    # 6. Künye
    kunye_svg = Y.kunye_svg()

    # 7. Veri
    t_soru = S_NEREYE["t0"]
    t_nokta = round(t_soru + float(Z["soru_kanca"]) + float(Z["soru_ara"]), 4)

    veri = {
        "Z": Z, "C0": round(C0, 4), "dy": DY,
        "soru_t": round(t_soru, 4), "nokta_t": round(t_nokta, 4),
        "aw": aw_bilgi, "ak": ak_bilgi, "t_kapat": round(t_kapat, 4),
        "sapka_t": SAPKA_T, "sapka_sol_t": SAPKA_SOL_T, "kay_t": KAY_T, "ac_t": AC_T, "es": [ES_T0, ES_T1],
        "he": [round(X_HE0, 2), round(X_HE1, 2)], "goes": [round(X_GOES0, 2), round(X_GOES1, 2)],
        "kirp_w": round(KIRP_W, 2),
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
#sahne,#alt{{position:absolute;left:0;top:0;}}
.kenar{{filter:{kenar_filter};}}
#kart-zemin{{fill:#fff9e6;}}
.tema-acik #kart-zemin{{fill:#fffdf8;}}
#root #kart-zemin{{stroke:var(--pilMetin);}}
#root #sapka{{stroke:var(--pilMetin);}}
</style></head><body>
<div id="root" {root_attrs}>
{Y.zemin_html()}
<div id="kgrup" class="abs" style="left:0;top:0;width:1080px;height:1920px">
<svg id="alt" class="abs" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<circle id="daire" cx="{DAIRE_CX:.2f}" cy="{DAIRE_CY:.2f}" r="{DAIRE_R:.2f}" fill="#fece00"/>
</svg>
<img id="karakter" class="abs kenar" src="assets/karakter.png" alt="" style="left:{KAR_X0:.1f}px;top:{KAR_Y0:.1f}px;width:{KAR_W * KS:.1f}px;height:{KAR_H * KS:.1f}px">
</div>
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{baslik_svg}
{kart_g_svg}
{kunye_svg}
<g id="altyazi">{altyazi_svg}</g>
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var V = {json.dumps(veri)};
  var Z = V.Z, $ = function (s) {{ return document.querySelector(s); }};
  var tl = gsap.timeline({{ paused: true }});
  function ac(o) {{ o.immediateRender = false; return o; }}

  // dash hazırlığı: hap çerçevesi, şapka, es çizgisi, mürekkep ?
  ["#cerceve", "#sapka", "#es-cizgi", "#soru-kanca"].forEach(function (s) {{
    var e = $(s);
    if (e) {{ var L = e.getTotalLength(); e.style.strokeDasharray = L + " " + (L + 2); e.style.strokeDashoffset = L; }}
  }});

  // 1. #cerceve hap çerçevesi (sine.inOut)
  tl.set("#cerceve", ac({{ opacity: 1 }}), Z.cerceve[0]);
  tl.to("#cerceve", ac({{ strokeDashoffset: 0, duration: Z.cerceve[1], ease: "sine.inOut" }}), Z.cerceve[0]);

  // 2. doesn't girişi ("Olumsuzda"): şapka kalemle, sözcükler ayrılır, doesn't soldan sağa açılır, şapka söner
  tl.set("#sapka", ac({{ opacity: 1 }}), V.sapka_t);
  tl.to("#sapka", ac({{ strokeDashoffset: 0, duration: Z.sapka[1], ease: "sine.inOut" }}), V.sapka_t);
  tl.fromTo("#kw-he", {{ attr: {{ x: V.he[0] }} }}, ac({{ attr: {{ x: V.he[1] }}, duration: Z.kay[1], ease: "power2.inOut" }}), V.kay_t);
  tl.fromTo("#kw-goes", {{ attr: {{ x: V.goes[0] }} }}, ac({{ attr: {{ x: V.goes[1] }}, duration: Z.kay[1], ease: "power2.inOut" }}), V.kay_t);
  tl.fromTo("#doesnt-kirp-r", {{ attr: {{ width: 0 }} }}, ac({{ attr: {{ width: V.kirp_w }}, duration: Z.doesnt_ac[1], ease: "none" }}), V.ac_t);
  tl.to("#sapka", ac({{ opacity: 0, duration: Z.sapka_sol, ease: "power1.in" }}), V.sapka_sol_t);

  // 2b. "s": goes içindeki es altına sarı kalem (karaoke gibi, sözcük sonunda kapanır)
  tl.set("#es-cizgi", ac({{ opacity: 1 }}), V.es[0]);
  tl.to("#es-cizgi", ac({{ strokeDashoffset: 0, duration: Z.es_ciz, ease: "sine.inOut" }}), V.es[0]);
  tl.set("#es-cizgi", ac({{ opacity: 0 }}), V.es[1]);

  // 3. Altyazı sözcükleri
  V.aw.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});

  // 4. Altyazı karaoke çizgileri
  V.ak.forEach(function (k) {{
    tl.set("#" + k[0], ac({{ opacity: 1 }}), k[1]);
    tl.set("#" + k[0], ac({{ opacity: 0 }}), k[2]);
  }});

  // 5. Kırmızı ?
  tl.set("#soru-kanca", ac({{ opacity: 1 }}), V.soru_t);
  tl.to("#soru-kanca", ac({{ strokeDashoffset: 0, duration: Z.soru_kanca, ease: "sine.inOut" }}), V.soru_t);
  tl.to("#soru-nokta", ac({{ opacity: 1, duration: Z.soru_nokta, ease: "power1.out" }}), V.nokta_t);

  // 6. Çıkış geçişi (C0)
  var C0 = V.C0;
  tl.to("#baslik", ac({{ opacity: 0, duration: Z.baslik_sol, ease: "power1.in" }}), C0);
  tl.to("#soru", ac({{ opacity: 0, duration: Z.soru_sol, ease: "power1.in" }}), C0);
  tl.to("#kart-g", ac({{ y: V.dy, duration: Z.cikis_sure, ease: "power3.inOut" }}), C0);
  tl.to("#kgrup", ac({{ x: Z.karakter_dx, opacity: 0, duration: Z.karakter_cik, ease: "power2.in" }}), C0);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html


# ---- 6. __main__ Bloğu (§8) ----
if __name__ == "__main__":
    proje_dizini: Path = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html_icerik = uret()
    assert "#root.tema-acik" not in html_icerik, "hf_tema dosyayı çevrilmiş sayar (sözleşme 15.11)"
    (proje_dizini / "index.html").write_text(html_icerik, encoding="utf-8")

    # devir.json sözcük x koordinatları
    x_he_0 = KYX + Y.genislik("Fredoka", 700, "", KB)
    x_he_1 = x_he_0 + Y.genislik("Fredoka", 700, "He", KB)

    x_doesnt_0 = KYX + Y.genislik("Fredoka", 700, "He ", KB)
    x_doesnt_1 = x_doesnt_0 + Y.genislik("Fredoka", 700, "doesn't", KB)

    x_goes_0 = KYX + Y.genislik("Fredoka", 700, "He doesn't ", KB)
    x_goes_1 = x_goes_0 + Y.genislik("Fredoka", 700, "goes.", KB)

    x_does_0 = KYX + Y.genislik("Fredoka", 700, "He ", KB)
    x_does_1 = x_does_0 + Y.genislik("Fredoka", 700, "does", KB)

    x_go_0 = KYX + Y.genislik("Fredoka", 700, "He doesn't ", KB)
    x_go_1 = x_go_0 + Y.genislik("Fredoka", 700, "go", KB)

    x_es_0 = KYX + Y.genislik("Fredoka", 700, "He doesn't go", KB)
    x_es_1 = x_es_0 + Y.genislik("Fredoka", 700, "es", KB)

    devir = {
        "kart": {
            "x": 60,
            "y": KY_SON,
            "w": round(KW, 2),
            "h": KH,
            "rx": KRX,
            "kenar": 4,
            "kenarRenk": "pilMetin",
            "dolgu": {"koyu": "#fff9e6", "acik": "#fffdf8"},
        },
        "yazi": {
            "metin": KART,
            "font": "Fredoka",
            "agirlik": 700,
            "boy": KB,
            "kerning": "none",
            "x": KYX,
            "taban": KY_SON + 108,
            "renk": "pilMetin",
        },
        "sozcuk": {
            "He": [round(x_he_0, 2), round(x_he_1, 2)],
            "doesn't": [round(x_doesnt_0, 2), round(x_doesnt_1, 2)],
            "goes.": [round(x_goes_0, 2), round(x_goes_1, 2)],
            "does": [round(x_does_0, 2), round(x_does_1, 2)],
            "go": [round(x_go_0, 2), round(x_go_1, 2)],
            "es": [round(x_es_0, 2), round(x_es_1, 2)],
        },
        "t": float(SAH["t_son"]),  # kol b: sahne 01 sonu (zaman.json); kol a'da son sözün sonuydu (aynı değer)
        "not": (
            "huni v2 (15.11): sahne 02 kare 0 kartı; x değerleri mürekkep değil "
            "ilerleme genişliği (kerning yok)"
        ),
    }

    (AD / "devir.json").write_text(json.dumps(devir, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("devir:", json.dumps(devir, ensure_ascii=False))
    print(
        f"B={B} T1={T1:.2f} T2={T2:.2f} hap y {HAP_UST:.2f}–{HAP_ALT:.2f} x {hap_x:.2f}–{hap_x + hap_w:.2f} "
        f"İ üstü {T2 - B2_UST * B:.2f} · kart0 He {X_HE0:.2f} goes {X_GOES0:.2f} · şapka x {SAPKA_X:.2f} · "
        f"C0 {C0} · içerik sonu {ICERIK_SON:.4f}",
        file=sys.stderr,
    )

"""simple-present-temel-s2 sahne 01 kanca index.html üretici (HyperFrames DİKEY 1080x1920, 102 kare).

SPEC huni v2 uygulaması: kanal katmanı, künye, kapak düzeni, takvim yaprağı (4 tik + 1 boş kutu),
öğrenci figürü, başlık uçuşu, karaoke altyazı ve devir.json.
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

# ---- Girdiler ----
Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
ORTAK = AD.parent.parent / "ortak"
SOZ = [
    w for w in json.loads((ORTAK / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 1
]
assert [w["sozcuk"] for w in SOZ[:4]] == ["Usually", "görünce", "hangi", "zaman?"], (
    f"Beklenen ilk 4 sözcük bulunamadı: {[w['sozcuk'] for w in SOZ[:4]]}"
)
ALT = json.loads((ORTAK / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
FIG = json.loads((AD / "cizim" / "ogrenci.json").read_text(encoding="utf-8"))

# ---- Sabitler ve türetilen ölçüler (§3) ----
W, H = Y.W, Y.H
KENAR = Y.HUD["kenar"]
SAG = Y.HUD["sagSinir"]
ORTA = (KENAR + SAG) / 2
BAS1 = "USUALLY"
BAS2 = "= ALIŞKANLIK"
PAD = 0.20  # em

B = math.floor(min(
    190,
    (SAG - KENAR) / Y.genislik("Fredoka", 700, BAS1, 1),
    (SAG - KENAR) / (Y.genislik("Fredoka", 700, BAS2, 1) + 2 * PAD),
))
g1 = Y.genislik("Fredoka", 700, BAS1, B)
t1x = ORTA - g1 / 2
TOP1 = 472
T1 = TOP1 + 0.70 * B
HAP_UST = T1 + 0.20 * B + 29
T2 = HAP_UST + 0.98 * B
HAP_ALT = T2 + 0.26 * B

hap_w = Y.genislik("Fredoka", 700, BAS2, B) + 2 * PAD * B
hap_x = ORTA - hap_w / 2
hap_rx = (HAP_ALT - HAP_UST) / 2
hap_h = HAP_ALT - HAP_UST

w0 = hap_w
h0 = HAP_ALT - (T1 - 0.70 * B)
O = (ORTA, ((T1 - 0.70 * B) + HAP_ALT) / 2)

boy = Y.konu_boyu()
rz_x, rz_w = Y.rozet_konumu()
KONU_SON = KENAR + Y.genislik("Fredoka", 700, Y.KONU, boy)

HEDEF_X0 = rz_x + rz_w + 24
HEDEF_X1 = 940.0
HEDEF_Y0 = 372.0
HEDEF_Y1 = 438.0
H = ((HEDEF_X0 + HEDEF_X1) / 2, 405.0)
HS = Z["ucus_hs"]

TK_X0, TK_X1, TK_Y0, TK_Y1, TK_R = 60, 440, 918, 1310, 28
HALKA_X, HALKA_Y = (155, 345), (876, 960)
BASLIK_Y = 1018
KUTU = 100
KUTULAR = [(80, 1044), (200, 1044), (320, 1044), (80, 1164), (200, 1164)]
TIK = [(24, 54), (44, 74), (78, 28)]
TIK_KAY = [(0, 0), (2, -2), (-2, 2), (1, -1)]

FIG_S = 0.37
FIG_R = 954
FIG_ALT = 1376
kx0, ky0, kx1, ky1 = FIG["kutu"]
px, py = FIG["parmak"]
FIG_UST = FIG_ALT - (ky1 - ky0) * FIG_S
FIG_SOL = FIG_R - (kx1 - kx0) * FIG_S
PARMAK = (FIG_R - (px - kx0) * FIG_S, FIG_UST + (py - ky0) * FIG_S)
FIG_KAL = {"govde": 4.4, "sac": 3.6, "yuz": 2.6, "aks": 2.6}

TABLO_KAYMA = (1.5, -2.0, 1.8, -1.2, -1.6, 2.1, -1.9, 1.4)


def _p3_in_out(p: float) -> float:
    p = max(0.0, min(1.0, p))
    return 8.0 * (p ** 4) if p < 0.5 else 1.0 - 8.0 * ((1.0 - p) ** 4)


def _p3_out(p: float) -> float:
    p = max(0.0, min(1.0, p))
    return 1.0 - ((1.0 - p) ** 4)


def _kesisir(b1: list[float] | tuple[float, ...], b2: list[float] | tuple[float, ...], pay: float = 6.0) -> bool:
    return not (b1[1] + pay <= b2[0] or b2[1] + pay <= b1[0] or b1[3] + pay <= b2[2] or b2[3] + pay <= b1[2])


def el_kutu(x: float, y: float, w: float, h: float, i: int) -> str:
    """El çizimi kare: 4 kenar tek kübik C, kontrol noktaları ±2.5 px kayma, 6 px bindirme."""
    k = [TABLO_KAYMA[(j + 2 * i) % len(TABLO_KAYMA)] for j in range(8)]
    cp1_1 = (x + w / 3, y + k[0])
    cp2_1 = (x + 2 * w / 3, y + k[1])
    p1 = (x + w, y)
    cp1_2 = (x + w + k[2], y + h / 3)
    cp2_2 = (x + w + k[3], y + 2 * h / 3)
    p2 = (x + w, y + h)
    cp1_3 = (x + 2 * w / 3, y + h + k[4])
    cp2_3 = (x + w / 3, y + h + k[5])
    p3 = (x, y + h)
    cp1_4 = (x + k[6], y + 2 * h / 3)
    cp2_4 = (x + k[7], y + h / 3)
    p4 = (x, y)
    p_son = (x + 6, y)
    return (
        f"M {x:.1f} {y:.1f} "
        f"C {cp1_1[0]:.1f} {cp1_1[1]:.1f}, {cp2_1[0]:.1f} {cp2_1[1]:.1f}, {p1[0]:.1f} {p1[1]:.1f} "
        f"C {cp1_2[0]:.1f} {cp1_2[1]:.1f}, {cp2_2[0]:.1f} {cp2_2[1]:.1f}, {p2[0]:.1f} {p2[1]:.1f} "
        f"C {cp1_3[0]:.1f} {cp1_3[1]:.1f}, {cp2_3[0]:.1f} {cp2_3[1]:.1f}, {p3[0]:.1f} {p3[1]:.1f} "
        f"C {cp1_4[0]:.1f} {cp1_4[1]:.1f}, {cp2_4[0]:.1f} {cp2_4[1]:.1f}, {p4[0]:.1f} {p4[1]:.1f} "
        f"L {p_son[0]:.1f} {p_son[1]:.1f}"
    )


def altyazi_karaoke(t_bas: float, sure: float, liste: list[dict]) -> tuple[str, list[list], list[list]]:
    """Altyazı bandı + karaoke altçizgileri."""
    svg_parcalar: list[str] = []
    zaman: list[list] = []
    karaoke: list[list] = []
    liste = Y.altyazi_dilimle(liste)

    soz_dosya = ORTAK / "anlatim" / "sozcukler.json"
    sozcukler = json.loads(soz_dosya.read_text(encoding="utf-8")) if soz_dosya.exists() else []

    ayazi = Y.HUD["altyaziYazi"]
    asatir = Y.HUD["altyaziSatir"]
    abas = Y.HUD["altyaziBas"]
    ason = Y.HUD["altyaziSon"]
    aorta = Y.HUD["altyaziOrta"]
    murekkep = Y.RENK["murekkep"]
    vurgu = Y.RENK["vurgu"]

    for i, a in enumerate(liste):
        t0 = a["t0"]
        t1 = a["t1"]
        ac = max(0.0, t0 - 0.05 - t_bas)
        son = t1 + 0.35
        if i + 1 < len(liste):
            son = min(son, liste[i + 1]["t0"] - 0.05)
        kapat = son - t_bas
        if kapat <= 0 or ac >= sure:
            continue
        parca_kapat = min(kapat, sure)
        zaman.append(["al%d" % i, round(ac, 3), round(parca_kapat, 3)])

        satirlar = Y.altyazi_satirlari(a["metin"])
        y0 = abas + (84 if len(satirlar) == 1 else 56)
        son_taban = y0 + (len(satirlar) - 1) * asatir
        assert son_taban + 0.25 * ayazi <= ason, f"Altyazı sınırı aşıldı: {son_taban + 0.25 * ayazi} > {ason}"

        satir_elemanlari: list[str] = []
        satir_bilgileri: list[dict] = []

        for k, sat in enumerate(satirlar):
            satir_y = y0 + k * asatir
            satir_eni = Y.genislik("Lexend", 500, sat, ayazi)
            satir_x = aorta - satir_eni / 2
            assert 60 <= satir_x and satir_x + satir_eni <= 960, (
                f"Satır x aralığı 60-960 dışına çıktı: {satir_x:.1f}..{satir_x + satir_eni:.1f}"
            )
            satir_elemanlari.append(
                f'<text x="{satir_x:.1f}" y="{satir_y}" text-anchor="start" font-family="Lexend" '
                f'font-weight="500" font-size="{ayazi}" fill="{murekkep}" style="font-kerning:none">{sat}</text>'
            )
            satir_bilgileri.append({"satir": sat, "x": satir_x, "y": satir_y})

        # Karaoke altçizgileri
        w_list = [w for w in sozcukler if w.get("cumle") == a.get("cumle") and (t0 - 0.06 <= w["t0"] < t1)]
        satir_sozcukleri = []
        for k, sb in enumerate(satir_bilgileri):
            sw_list = sb["satir"].split(" ")
            for s_idx, sw in enumerate(sw_list):
                satir_sozcukleri.append((k, s_idx, sw, sb))

        if a.get("cumle") == 1:
            assert len(w_list) == 4 and len(satir_sozcukleri) == 4, (
                f"Cümle 1 eşleşme hatası: w_list={len(w_list)}, satir_sozcukleri={len(satir_sozcukleri)}"
            )

        cizgi_elemanlari: list[str] = []
        if len(w_list) == len(satir_sozcukleri):
            for j, ((k, s_idx, sw, sb), w) in enumerate(zip(satir_sozcukleri, w_list)):
                sw_list = sb["satir"].split(" ")
                onceki = (" ".join(sw_list[:s_idx]) + " ") if s_idx > 0 else ""
                x1 = sb["x"] + (Y.genislik("Lexend", 500, onceki, ayazi) if onceki else 0.0)
                sw_temiz = sw.rstrip(".,:;!?")
                x2 = x1 + Y.genislik("Lexend", 500, sw_temiz, ayazi)
                y1 = sb["y"] + 12
                y2 = y1
                cizgi_ac = round(w["t0"] - t_bas, 3)
                if j + 1 < len(w_list):
                    cizgi_kapat = round(w_list[j + 1]["t0"] - t_bas, 3)
                else:
                    cizgi_kapat = round(min(w["t1"] - t_bas + 0.25, parca_kapat), 3)
                uzunluk = round(x2 - x1, 2)
                karaoke.append(["ak%d_%d" % (i, j), cizgi_ac, cizgi_kapat, uzunluk])
                cizgi_elemanlari.append(
                    f'<line id="ak{i}_{j}" x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" '
                    f'stroke="{vurgu}" stroke-width="6" stroke-linecap="round" style="opacity:0"/>'
                )

        svg_parcalar.append(
            f'<g id="al{i}" style="opacity:0">' + "".join(satir_elemanlari) + "".join(cizgi_elemanlari) + "</g>"
        )

    return "".join(svg_parcalar), zaman, karaoke


def _denetimler() -> None:
    # 1. Başlık
    assert 120 <= B <= 190, f"B={B} aralık [120, 190] dışı"
    assert t1x >= KENAR and t1x + g1 <= SAG, f"baslik 1 x={t1x:.2f}..{t1x + g1:.2f} [{KENAR}, {SAG}] dışı"
    assert hap_x >= KENAR and hap_x + hap_w <= SAG, f"hap x={hap_x:.2f}..{hap_x + hap_w:.2f} [{KENAR}, {SAG}] dışı"
    assert (T1 - 0.70 * B) >= Y.HUD["icerikBas"], f"T1 - 0.70*B={T1 - 0.70*B:.2f} < icerikBas {Y.HUD['icerikBas']}"
    assert HAP_ALT <= 800, f"HAP_ALT={HAP_ALT:.2f} > 800"
    assert len(BAS1) <= 24 and len(BAS2) <= 24, f"len(BAS1)={len(BAS1)}, len(BAS2)={len(BAS2)} > 24"

    # 2. Takvim
    assert TK_X0 >= KENAR and TK_X1 <= SAG, f"takvim yaprak x [{TK_X0}, {TK_X1}] dışı"
    assert TK_Y0 >= 820 and TK_Y1 <= Y.HUD["icerikSon"], f"takvim yaprak y [{TK_Y0}, {TK_Y1}] dışı"
    assert all(KENAR <= x <= SAG for x in HALKA_X), f"halka x dışı: {HALKA_X}"
    assert HALKA_Y[0] >= 820 and HALKA_Y[1] <= Y.HUD["icerikSon"], f"halka y dışı: {HALKA_Y}"
    for i, (kx, ky) in enumerate(KUTULAR):
        assert kx >= TK_X0 + 20 and kx + KUTU <= TK_X1 - 20, (
            f"kutu {i} x={kx}..{kx + KUTU} yaprak içinden < 20 px"
        )
        assert ky >= BASLIK_Y + 24 and ky + KUTU <= TK_Y1 - 20, (
            f"kutu {i} y={ky}..{ky + KUTU} BASLIK_Y/alt kenar dışı"
        )
    for i in range(4):
        pts = [(KUTULAR[i][0] + p[0] + TIK_KAY[i][0], KUTULAR[i][1] + p[1] + TIK_KAY[i][1]) for p in TIK]
        for px_val, py_val in pts:
            assert KUTULAR[i][0] + 4 <= px_val <= KUTULAR[i][0] + KUTU - 4, (
                f"tik {i} px {px_val} kutu {i} içi 4 px dışı"
            )
            assert KUTULAR[i][1] + 4 <= py_val <= KUTULAR[i][1] + KUTU - 4, (
                f"tik {i} py {py_val} kutu {i} içi 4 px dışı"
            )
    for i, (kx, ky) in enumerate(KUTULAR):
        d = el_kutu(kx, ky, KUTU, KUTU, i)
        nums = [float(v) for v in re.findall(r"-?\d+\.?\d*", d)]
        for px_val, py_val in zip(nums[0::2], nums[1::2]):
            assert kx - 4 <= px_val <= kx + KUTU + 4, f"kutu {i} el_kutu px {px_val} çevresi 4 px dışı"
            assert ky - 4 <= py_val <= ky + KUTU + 4, f"kutu {i} el_kutu py {py_val} çevresi 4 px dışı"

    # 3. Figür
    assert FIG_SOL >= TK_X1 + 20, f"FIG_SOL={FIG_SOL:.2f} < TK_X1 + 20 ({TK_X1 + 20})"
    assert FIG_R <= SAG - 4, f"FIG_R={FIG_R:.2f} > SAG - 4 ({SAG - 4})"
    assert FIG_UST >= HAP_ALT + 24, f"FIG_UST={FIG_UST:.2f} < HAP_ALT + 24 ({HAP_ALT + 24:.2f})"
    assert FIG_ALT <= Y.HUD["icerikSon"] - 2, f"FIG_ALT={FIG_ALT:.2f} > icerikSon - 2 ({Y.HUD['icerikSon'] - 2})"
    assert PARMAK[0] > TK_X1 + 20, f"PARMAK x={PARMAK[0]:.2f} <= TK_X1 + 20 ({TK_X1 + 20})"
    assert TK_Y0 <= PARMAK[1] <= TK_Y1, f"PARMAK y={PARMAK[1]:.2f} [{TK_Y0}, {TK_Y1}] dışı"

    # 4. Dikey sıra
    assert HAP_ALT + 24 <= min(HALKA_Y[0], FIG_UST), (
        f"HAP_ALT + 24 = {HAP_ALT + 24:.2f} > min({HALKA_Y[0]}, {FIG_UST:.2f})"
    )

    # 5. Uçuş örneklemesi
    u0, ud = Z["ucus"]
    curr_t = u0
    while curr_t <= u0 + ud + 1e-6:
        e_konum = _p3_in_out((curr_t - u0) / ud)
        e_olcek = _p3_out((curr_t - u0) / Z["ucus_olcek"])
        merkez_x = O[0] + (H[0] - O[0]) * e_konum
        merkez_y = O[1] + (H[1] - O[1]) * e_konum
        s = 1.0 + (HS - 1.0) * e_olcek
        kutu = [
            merkez_x - s * (w0 / 2),
            merkez_x + s * (w0 / 2),
            merkez_y - s * (h0 / 2),
            merkez_y + s * (h0 / 2),
        ]
        rozet_kutu = [rz_x, rz_x + rz_w, 386.0, 434.0]
        konu_kutu = [float(KENAR), float(KONU_SON), 420.0 - 0.75 * boy, 420.0 + 0.25 * boy]
        kanal_kutu = [60.0, 602.0, 291.0, 341.0]

        assert not _kesisir(kutu, rozet_kutu, 6.0), f"Uçuş çakışması t={curr_t:.3f}: kutu x rozet"
        assert not _kesisir(kutu, konu_kutu, 6.0), f"Uçuş çakışması t={curr_t:.3f}: kutu x konu"
        assert not _kesisir(kutu, kanal_kutu, 6.0), f"Uçuş çakışması t={curr_t:.3f}: kutu x kanal"
        assert KENAR <= kutu[0] and kutu[1] <= SAG, (
            f"Uçuş t={curr_t:.3f}: kutu x [{KENAR}, {SAG}] dışı: {kutu[0]:.2f}..{kutu[1]:.2f}"
        )
        assert kutu[3] <= min(HALKA_Y[0], FIG_UST) - 6.0, (
            f"Uçuş t={curr_t:.3f}: kutu altı {kutu[3]:.2f} > {min(HALKA_Y[0], FIG_UST) - 6.0:.2f}"
        )
        curr_t += 1.0 / 30.0

    assert HEDEF_X0 - 1.0 <= kutu[0] and kutu[1] <= HEDEF_X1 + 1.0, (
        f"Son t kutu x {kutu[:2]} hedef [{HEDEF_X0}, {HEDEF_X1}] dışı"
    )
    assert HEDEF_Y0 - 1.0 <= kutu[2] and kutu[3] <= HEDEF_Y1 + 1.0, (
        f"Son t kutu y {kutu[2:]} hedef [{HEDEF_Y0}, {HEDEF_Y1}] dışı"
    )

    # 6. Zaman
    tik_son = Z["tik_bas"] + 3 * Z["tik_ara"] + Z["tik_sure"]
    assert tik_son <= 0.80 + 1e-6, f"son tik {tik_son:.3f} > 0.80"
    assert tik_son <= Z["kapak_kare"] / 30.0 - 1.0 / 30.0, f"son tik {tik_son:.3f} > kapak_kare sınırı"
    assert SOZ[0]["t0"] >= Z["kapak_kare"] / 30.0 + 1.0 / 30.0, f"SOZ[0].t0 {SOZ[0]['t0']} < kapak_kare sınırı"
    assert abs(Z["ucus"][0] + Z["ucus"][1] - 3.00) < 1e-6, f"ucus toplam != 3.00"
    assert abs(Z["baslik_sol"][0] + Z["baslik_sol"][1] - 3.00) < 1e-6, f"baslik_sol toplam != 3.00"
    assert abs(Z["sahne_sol"][0] + Z["sahne_sol"][1] - 3.00) < 1e-6, f"sahne_sol toplam != 3.00"
    assert abs(3.00 - (Z["kare"] - 12) / 30.0) < 1e-6, f"3.00 != (kare - 12)/30"


_denetimler()


def zamanlar() -> dict:
    """olay.py tarafından okunan olay zamanları."""
    return {
        "tikler": [
            [round(Z["tik_bas"] + i * Z["tik_ara"], 4), Z["tik_sure"]]
            for i in range(4)
        ],
        "altyazi_ac": round(SOZ[0]["t0"] - 0.05, 4),
        "ucus": [Z["ucus"][0], Z["ucus"][1]],
    }


def uret() -> str:
    """Tam HTML belgesi üretir."""
    R = Y.RENK

    # 1. Takvim öğeleri
    tk_yaprak = (
        f'<rect id="tk-yaprak" x="{TK_X0}" y="{TK_Y0}" width="{TK_X1 - TK_X0}" '
        f'height="{TK_Y1 - TK_Y0}" rx="{TK_R}" stroke-width="7"/>'
    )
    halka1 = f'<path d="M{HALKA_X[0]} {HALKA_Y[0]} L{HALKA_X[0]} {HALKA_Y[1]}" stroke-width="7"/>'
    halka2 = f'<path d="M{HALKA_X[1]} {HALKA_Y[0]} L{HALKA_X[1]} {HALKA_Y[1]}" stroke-width="7"/>'
    baslik_cizgi = f'<path d="M{TK_X0} {BASLIK_Y} L{TK_X1} {BASLIK_Y}" stroke-width="7"/>'

    kutular_svg = "".join(
        f'<path id="gk{i}" d="{el_kutu(kx, ky, KUTU, KUTU, i)}" stroke-width="5"/>'
        for i, (kx, ky) in enumerate(KUTULAR)
    )

    tikler_svg_list = []
    for i in range(4):
        p0 = (KUTULAR[i][0] + TIK[0][0] + TIK_KAY[i][0], KUTULAR[i][1] + TIK[0][1] + TIK_KAY[i][1])
        p1 = (KUTULAR[i][0] + TIK[1][0] + TIK_KAY[i][0], KUTULAR[i][1] + TIK[1][1] + TIK_KAY[i][1])
        p2 = (KUTULAR[i][0] + TIK[2][0] + TIK_KAY[i][0], KUTULAR[i][1] + TIK[2][1] + TIK_KAY[i][1])
        tikler_svg_list.append(
            f'<path id="tk{i}" d="M{p0[0]} {p0[1]} L{p1[0]} {p1[1]} L{p2[0]} {p2[1]}" '
            f'stroke-width="10" style="opacity:0"/>'
        )
    tikler_svg = "".join(tikler_svg_list)

    takvim_svg = (
        f'<g id="takvim" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{tk_yaprak}{halka1}{halka2}{baslik_cizgi}{kutular_svg}{tikler_svg}'
        f'</g>'
    )

    # 2. Figür
    fig_paths = "".join(
        f'<path d="{p["d"]}" stroke-width="{FIG_KAL.get(p["parca"], 4.4) / FIG_S:.3f}"/>'
        for p in FIG["yollar"]
    )
    tx_fig = FIG_R + kx0 * FIG_S
    ty_fig = FIG_UST - ky0 * FIG_S
    figur_svg = (
        f'<g id="figur" clip-path="url(#figkl)" fill="none" stroke="{R["murekkep"]}" '
        f'stroke-linecap="round" stroke-linejoin="round">'
        f'<g id="fig-ic" transform="translate({tx_fig:.2f} {ty_fig:.2f}) scale({-FIG_S}, {FIG_S})">'
        f'{fig_paths}'
        f'</g>'
        f'</g>'
    )

    # 3. Başlık
    bas2 = (
        f'<g id="bas2">'
        f'<rect id="hap" x="{hap_x:.2f}" y="{HAP_UST:.2f}" width="{hap_w:.2f}" height="{hap_h:.2f}" '
        f'rx="{hap_rx:.2f}" fill="{R["vurgu"]}"/>'
        f'<text id="bas2t" x="{ORTA:.2f}" y="{T2:.2f}" text-anchor="middle" font-family="Fredoka" '
        f'font-weight="700" font-size="{B}" fill="{R["zemin"]}" style="font-kerning:none">{BAS2}</text>'
        f'</g>'
    )
    bas1 = (
        f'<g id="bas1">'
        f'<text id="bas1t" x="{t1x:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">{BAS1}</text>'
        f'</g>'
    )
    baslik_svg = f'<g id="baslik">{bas2}{bas1}</g>'

    # 4. Künye ve altyazı
    kunye_svg = Y.kunye_svg()
    alt_svg, alt_zaman, karaoke = altyazi_karaoke(0.0, Z["sure"], ALT)

    # GSAP parametreleri
    tikler_js = [
        ["#tk%d" % i, round(Z["tik_bas"] + i * Z["tik_ara"], 4), Z["tik_sure"]]
        for i in range(4)
    ]
    veri = {
        "Z": Z,
        "alt": alt_zaman,
        "karaoke": karaoke,
        "tikler": tikler_js,
        "O": [round(O[0], 2), round(O[1], 2)],
        "H": [round(H[0], 2), round(H[1], 2)],
        "HS": round(HS, 4),
    }

    sure_val = Z["sure"]
    root_attrs = (
        f'data-composition-id="main" data-start="0" data-duration="{sure_val}" '
        f'data-fps="30" data-width="1080" data-height="1920"'
    )
    defs_svg = '<defs><clipPath id="figkl"><rect x="440" y="900" width="520" height="476"/></clipPath></defs>'

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
{defs_svg}
{takvim_svg}
{figur_svg}
{baslik_svg}
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

  // 1. Altyazı
  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});

  // 2. Karaoke
  V.karaoke.forEach(function (k) {{
    var id = "#" + k[0], ac_t = k[1], kapat_t = k[2], uz = k[3];
    var el = $(id);
    if (el) {{
      el.style.strokeDasharray = uz + " " + (uz + 2);
      el.style.strokeDashoffset = uz;
      tl.set(id, ac({{ opacity: 1 }}), ac_t);
      tl.fromTo(id, {{ strokeDashoffset: uz }},
        ac({{ strokeDashoffset: 0, duration: 0.15, ease: "power2.out" }}), ac_t);
      tl.set(id, ac({{ opacity: 0 }}), kapat_t);
    }}
  }});

  // 3. Tikler
  V.tikler.forEach(function (tk) {{
    var id = tk[0], t0 = tk[1], sure = tk[2];
    var el = $(id);
    if (el) {{
      var L = el.getTotalLength();
      el.style.strokeDasharray = L + " " + (L + 2);
      el.style.strokeDashoffset = L;
      tl.set(id, ac({{ opacity: 1 }}), t0);
      tl.to(id, ac({{ strokeDashoffset: 0, duration: sure, ease: "sine.inOut" }}), t0);
    }}
  }});

  // 4. Sahne grubu solar (takvim + figür)
  tl.to(["#takvim", "#figur"], ac({{ opacity: 0, duration: Z.sahne_sol[1], ease: "power2.in" }}), Z.sahne_sol[0]);

  // 5. Uçuş: #baslik
  gsap.set("#baslik", {{ svgOrigin: V.O[0] + " " + V.O[1], smoothOrigin: false }});
  tl.to("#baslik", ac({{ x: V.H[0] - V.O[0], duration: Z.ucus[1], ease: "power3.inOut" }}), Z.ucus[0]);
  tl.to("#baslik", ac({{ y: V.H[1] - V.O[1], duration: Z.ucus[1], ease: "power3.inOut" }}), Z.ucus[0]);
  tl.to("#baslik", ac({{ scale: V.HS, duration: Z.ucus_olcek, ease: "power3.out" }}), Z.ucus[0]);

  // 6. Başlık solar
  tl.to("#baslik", ac({{ opacity: 0, duration: Z.baslik_sol[1], ease: "power2.in" }}), Z.baslik_sol[0]);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""

    # Yasak söz taraması (standart §7 kapı 3) bu dosyada değil, istemdeki grep ile üretilen HTML üzerinde koşar.
    return html


if __name__ == "__main__":
    proje_dir = AD / "proje"
    proje_dir.mkdir(parents=True, exist_ok=True)
    Y.font_kopyala(proje_dir / "assets" / "fonts")
    html_icerik = uret()
    (proje_dir / "index.html").write_text(html_icerik, encoding="utf-8")

    devir = {
        "icerik_bandi": "bos",
        "t": 3.0,
        "kunye": {
            "konu": Y.KONU,
            "boy": boy,
            "rozet": [round(rz_x, 2), round(rz_w, 2)],
            "rozet_y": [386, 434],
        },
        "altyazi": "cümle 1 sahne sonuna dek (3,40)",
        "not": "huni v2 (15.11): sahne 02 kare 0 içerik bandı boş; kanal + künye 0. kareden aynı",
    }
    (AD / "devir.json").write_text(json.dumps(devir, ensure_ascii=False, indent=2), encoding="utf-8")
    print("devir:", json.dumps(devir, ensure_ascii=False))

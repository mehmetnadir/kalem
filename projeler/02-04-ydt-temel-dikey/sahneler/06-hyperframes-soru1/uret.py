"""Sahne 06 — Soru anı 1 (02-04 YDT temel dikey; 1080x1920; cümle 6 öğrenci, cümle 7 öğretmen).
yanılgı: tarifeli gelecek planlanmış gelecekle karışır (tren de plana göre kalkar → -ing). Soru 10 sözcük (≤ 12).
Tasarım: SPEC.md (şef); kod agy-filo (rol kod) 15.11.
"""
import json
import math
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
TB = Z["t_bas"]

_ham = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
S6 = [w for w in _ham if w["cumle"] == 6]
S7 = [w for w in _ham if w["cumle"] == 7]

assert [w["sozcuk"] for w in S6] == [
    "Hocam,",
    "tren",
    "de",
    "plana",
    "göre",
    "kalkmıyor",
    "mu?",
    "Neden",
    "-ing",
    "yok?",
], f"S6 sözcükleri beklenenden farklı: {[w['sozcuk'] for w in S6]}"

R = Y.RENK
KRE, IKN, SAR, ZEM = R["murekkep"], R["ikincil"], R["vurgu"], R["zemin"]


def T6(i: int) -> float:
    return S6[i]["t0"]


def T7(sozcuk: str, n: int = 0) -> float:
    matches = [w["t0"] for w in S7 if w["sozcuk"] == sozcuk]
    assert len(matches) > n, f"S7 içinde {sozcuk!r} sözcüğünün {n}. geçişi bulunamadı"
    return matches[n]


def g(m: str, boy: float, agr: int = 700, aile: str = "Fredoka") -> float:
    return Y.genislik(aile, agr, m, boy)


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
    boy: float = 48.0,
    renk: str = KRE,
    anchor: str = "start",
) -> str:
    anc = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return (
        f'<text id="{kim}" x="{x:.1f}" y="{y:.1f}" font-family="{aile}" font-weight="{agr}" '
        f'font-size="{boy:.1f}" fill="{renk}"{anc} xml:space="preserve">{m}</text>'
    )


def kutu_d(x: float, y: float, w: float, h: float, j: int = 0) -> str:
    """Yalnız M/L/Z komutlu el kutusu."""
    d0 = 0.6 * math.sin(j * 1.7)
    d1 = 0.6 * math.cos(j * 2.3)
    d2 = 0.6 * math.sin(j * 3.1 + 1.0)
    d3 = 0.6 * math.cos(j * 4.7 + 2.0)
    pts = [
        (x + d0, y + d1),
        (x + w * 0.5 + d2, y - 0.5 + d0),
        (x + w + d1, y + 0.3 + d3),
        (x + w + 0.5 + d3, y + h * 0.5 + d1),
        (x + w - 0.3 + d0, y + h + d2),
        (x + w * 0.5 + d1, y + h + 0.5 + d3),
        (x + 0.3 + d2, y + h + d0),
        (x - 0.4 + d3, y + h * 0.5 + d2),
    ]
    p_str = " ".join(f"L{px:.1f} {py:.1f}" for px, py in pts[1:])
    return f"M{pts[0][0]:.1f} {pts[0][1]:.1f} {p_str} Z"


def daire_d(cx: float, cy: float, r: float, ry: float | None = None) -> str:
    """29 noktalı, %4 kapanış paylı, yalnız M/L el dairesi."""
    if ry is None:
        ry = r
    pts = []
    for i in range(29):
        a = -math.pi / 2 + i * (2 * math.pi * 1.04) / 28
        wob = 1.0 + 0.02 * math.sin(a * 3)
        pts.append((cx + r * wob * math.cos(a), cy + ry * wob * math.sin(a)))
    return "M%.1f %.1f " % pts[0] + " ".join("L%.1f %.1f" % p for p in pts[1:])


def bukum_ok(x: float, y0: float, y1: float, x1: float) -> str:
    """Basamak oku: x'te y0 -> y1 aşağı, yuvarlak köşe Q (yarıçap 12), sağa x1, ok başı (13)."""
    r = 12.0
    k = 13.0
    cos5 = math.cos(0.5)
    sin5 = math.sin(0.5)
    return (
        f"M{x:.1f} {y0:.1f} "
        f"L{x:.1f} {y1 - r:.1f} "
        f"Q{x:.1f} {y1:.1f} {x + r:.1f} {y1:.1f} "
        f"L{x1:.1f} {y1:.1f} "
        f"M{x1 - k * cos5:.1f} {y1 - k * sin5:.1f} "
        f"L{x1:.1f} {y1:.1f} "
        f"L{x1 - k * cos5:.1f} {y1 + k * sin5:.1f}"
    )


def tren_parcalari(TX0: float, TY0: float, k: float) -> tuple[list[tuple[str, str, float, float]], list[str]]:
    """Tren parçaları: [(d, renk, kalınlık, uzunluk)], kimlikler tr0.."""
    def P(x: float, y: float) -> tuple[float, float]:
        return TX0 + k * x, TY0 + k * y

    def K(x: float, y: float, w: float, h: float, j: int = 0) -> str:
        return kutu_d(TX0 + k * x, TY0 + k * y, k * w, k * h, j)

    def D(cx: float, cy: float, r: float, ry: float | None = None) -> str:
        return daire_d(TX0 + k * cx, TY0 + k * cy, k * r, (k * ry) if ry else None)

    parcalar = [
        (K(0, 45, 175, 85, 1), KRE, 4.5, 2 * (175 + 85) * k),
        (K(200, 55, 170, 75, 2), KRE, 4.5, 2 * (170 + 75) * k),
        (K(200, 10, 75, 45, 3), KRE, 4.5, 2 * (75 + 45) * k),
        (K(320, 22, 26, 33, 4), KRE, 3.6, 2 * (26 + 33) * k),
        (
            f"M{P(370, 95)[0]:.1f} {P(370, 95)[1]:.1f} L{P(398, 130)[0]:.1f} {P(398, 130)[1]:.1f} "
            f"L{P(370, 130)[0]:.1f} {P(370, 130)[1]:.1f}",
            KRE,
            4.5,
            (math.hypot(28, 35) + 28) * k,
        ),
        (
            f"M{P(175, 112)[0]:.1f} {P(175, 112)[1]:.1f} L{P(200, 112)[0]:.1f} {P(200, 112)[1]:.1f}",
            KRE,
            3.6,
            25 * k,
        ),
        (K(20, 60, 50, 30, 5), KRE, 3.6, 2 * (50 + 30) * k),
        (K(100, 60, 50, 30, 6), KRE, 3.6, 2 * (50 + 30) * k),
        (K(215, 20, 42, 25, 7), KRE, 3.6, 2 * (42 + 25) * k),
        (D(40, 138, 17), KRE, 4.5, 2 * math.pi * 17 * k),
        (D(135, 138, 17), KRE, 4.5, 2 * math.pi * 17 * k),
        (D(240, 138, 17), KRE, 4.5, 2 * math.pi * 17 * k),
        (D(335, 138, 17), KRE, 4.5, 2 * math.pi * 17 * k),
        (
            f"M{P(-10, 158)[0]:.1f} {P(-10, 158)[1]:.1f} L{P(420, 158)[0]:.1f} {P(420, 158)[1]:.1f}",
            IKN,
            4.0,
            430 * k,
        ),
        (D(345, 2, 11, 9), IKN, 3.4, 2 * math.pi * math.sqrt((11 * 11 + 9 * 9) / 2) * k),
        (D(372, -16, 8, 7), IKN, 3.4, 2 * math.pi * math.sqrt((8 * 8 + 7 * 7) / 2) * k),
    ]
    ids = [f"tr{i}" for i in range(len(parcalar))]
    return parcalar, ids


def ikon(
    s: Y.Sahne, kim: str, ad: str, x: float, y: float, boy: float, t: float, sure: float
) -> list[str]:
    """Tabler ikon yolları kalemle çizilir."""
    yollar = Y.tabler(ad)
    n = len(yollar)
    olcek = boy / 24.0
    w_line = 4.6 / olcek
    d_part = sure / max(1, n)
    ids = []
    for i, d in enumerate(yollar):
        cid = f"{kim}_{i}" if n > 1 else kim
        ids.append(cid)
        t_i = t + i * d_part
        ek = f'transform="translate({x:.1f} {y:.1f}) scale({olcek:.4f})"'
        s.yol(cid, d, t_i, d_part, KRE, w_line, 1.0, tur="cizgi" if i == 0 else None, guc=0.5, ek=ek)
    return ids


def nabiz(
    s: Y.Sahne,
    sec: str,
    t: float,
    ox: float,
    oy: float,
    olcek: float = 1.06,
    d_up: float = 0.2,
    d_down: float = 0.25,
) -> None:
    """Merkezden ölçek nabzı."""
    origin = f"{ox:.1f} {oy:.1f}"
    s.to(sec, t, {"scale": olcek, "svgOrigin": origin, "duration": d_up, "ease": "power2.out"})
    s.to(sec, t + d_up, {"scale": 1.0, "svgOrigin": origin, "duration": d_down, "ease": "power2.in"})


def kalinlik(
    s: Y.Sahne,
    sec: str,
    t: float,
    w0: float,
    w1: float,
    d_up: float = 0.15,
    d_down: float = 0.2,
) -> None:
    """Çizgi kalınlığı nabzı (GSAP attr: stroke-width)."""
    s.to(sec, t, {"attr": {"stroke-width": w1}, "duration": d_up, "ease": "power1.out"})
    s.to(sec, t + d_up, {"attr": {"stroke-width": w0}, "duration": d_down, "ease": "power1.in"})


def soldur(s: Y.Sahne, a: str, b: str, t: float, d: float = 0.25) -> None:
    """#a opaklık 0'a, #b opaklık 1'e."""
    sel_a = a if a.startswith("#") else f"#{a}"
    sel_b = b if b.startswith("#") else f"#{b}"
    s.to(sel_a, t, {"opacity": 0, "duration": d, "ease": "power1.inOut"})
    s.to(sel_b, t, {"opacity": 1, "duration": d, "ease": "power1.inOut"})


def hap(kim: str, x: float, taban: float, metin_icerik: str) -> str:
    """Vurgulanan kalıp hapı."""
    w = g(metin_icerik, 64, 700, "Caveat") + 20
    return (
        f'<g id="{kim}" style="opacity:0">'
        f'<rect x="{x - 10:.1f}" y="{taban - 52:.1f}" width="{w:.1f}" height="74" rx="16" fill="{SAR}"/>'
        f'<text x="{x:.1f}" y="{taban:.1f}" font-family="Caveat" font-weight="700" font-size="64" fill="{ZEM}" '
        f'xml:space="preserve">{metin_icerik}</text>'
        '</g>'
    )


def kunye_tam() -> str:
    """Dikey HUD künyesi (kare 0'dan sabit)."""
    w_pc = g("PRESENT CONTINUOUS", 56, 700, "Fredoka")
    rx = 48 + w_pc + 24
    rw = g("YDT · TEMEL", 36, 700, "Lexend") + 56
    cw = g("Question", 40, 700, "Lexend") + 64
    cx = 1032 - cw
    return (
        '<g id="kunye">'
        f'<text id="ku-ders1" x="48" y="212" font-family="Fredoka" font-weight="700" font-size="56" fill="{KRE}" '
        f'xml:space="preserve">SIMPLE PRESENT vs</text>'
        f'<text id="ku-ders2" x="48" y="276" font-family="Fredoka" font-weight="700" font-size="56" fill="{KRE}" '
        f'xml:space="preserve">PRESENT CONTINUOUS</text>'
        f'<g id="ku-rz"><rect x="{rx:.2f}" y="216" width="{rw:.2f}" height="72" rx="36" fill="{SAR}"/>'
        f'<text x="{rx + rw / 2:.2f}" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" '
        f'font-size="36" fill="{ZEM}" xml:space="preserve">YDT · TEMEL</text></g>'
        f'<g id="ku-bolum"><rect x="{cx:.2f}" y="48" width="{cw:.2f}" height="80" rx="40" fill="none" stroke="{SAR}" '
        f'stroke-width="4"/>'
        f'<text x="{cx + cw / 2:.2f}" y="102" text-anchor="middle" font-family="Lexend" font-weight="700" '
        f'font-size="40" fill="{SAR}" xml:space="preserve">Question</text></g>'
        '</g>'
    )


def zincir(
    s: Y.Sahne,
    ad: str,
    satirlar: list[list[tuple[str, str]] | None],
    zamanlar: list[float],
    x0: float,
    ZB: tuple[float, ...],
) -> dict[str, tuple[float, float, float]]:
    """Kavram zinciri: satır 0 düz yazı, sonraki satırlar büküm oku + yazı."""
    ret: dict[str, tuple[float, float, float]] = {}
    xp = x0
    if satirlar[0]:
        x_ret, w_ret = s.yazi(f"{ad}y0", xp, ZB[0], satirlar[0], "Caveat", 700, 64, zamanlar[0], 0.3)
        ret[f"{ad}y0"] = (x_ret, w_ret, ZB[0])

    for i in range(1, len(zamanlar)):
        t_arr = zamanlar[i]
        d_ok = bukum_ok(xp + 14, ZB[i - 1] + 28, ZB[i] - 16, xp + 50)
        s.yol(f"{ad}z{i}", d_ok, t_arr, 0.3, IKN, 4.5, 1.0, "cizgi", 0.45)
        xp = xp + 64
        if i < len(satirlar) and satirlar[i]:
            x_ret, w_ret = s.yazi(f"{ad}y{i}", xp, ZB[i], satirlar[i], "Caveat", 700, 64, t_arr + 0.15, 0.3)
            ret[f"{ad}y{i}"] = (x_ret, w_ret, ZB[i])
        else:
            ret[f"{ad}y{i}"] = (xp, 0.0, ZB[i])

    return ret


def uret() -> tuple[Y.Sahne, dict]:
    s = Y.Sahne(TB)
    S = s.S
    bal_ids: list[str] = []

    # ================= 1. Üst Şerit (kare 0'dan sabit) =================
    s1_metin = "The train … leaves at 7 pm today."
    s2_metin = "I am going … tonight."
    assert 48 + g(s1_metin, 64, 700, "Fredoka") <= 1032
    assert 48 + g(s2_metin, 64, 700, "Fredoka") <= 1032

    XL = 48 + g("The train … ", 64, 700, "Fredoka")
    WL = g("leaves", 64, 700, "Fredoka")
    XG = 48 + g("I ", 64, 700, "Fredoka")
    WG = g("am going", 64, 700, "Fredoka")
    L2SON = 48 + g(s2_metin, 64, 700, "Fredoka")
    XU = XL + 0.75 * WL

    # Altçizgiler klm, klm_s, krm, krm_s
    d_klm = Y.el_cizgi(XL - 2, 418, XL + WL + 2, 418, 1)
    s.svg.append(statik("klm", d_klm, SAR, 10.0, 1.0))
    s.svg.append(statik("klm_s", d_klm, IKN, 10.0, 0.0))

    d_krm = Y.el_cizgi(XG - 2, 531, XG + WG + 2, 531, 1)
    s.svg.append(statik("krm", d_krm, SAR, 10.0, 1.0))
    s.svg.append(statik("krm_s", d_krm, IKN, 10.0, 0.0))

    # Şerit metinleri
    s.svg.append(metin("st1", 48, 400, s1_metin, "Fredoka", 700, 64, KRE))
    s.svg.append(metin("st2", 48, 500, s2_metin, "Fredoka", 700, 64, KRE))

    # ================= 2. Soru anı: Öğrenci başı + Balon =================
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS0 = 240.0 / 330.0
    BTX = 96.0 + 45.0 * BS0
    BTY = 680.0
    bas_paths = "".join(f'<path id="bas{i}" d="{d}" style="opacity:0"/>' for i, d in enumerate(bd))
    s.svg.append(
        f'<g id="basm"><g id="basn"><g id="bas" transform="translate({BTX:.2f} {BTY:.2f}) scale({BS0:.4f})" '
        f'fill="none" stroke="{KRE}" stroke-width="{4.0 / BS0:.3f}" stroke-linecap="round" stroke-linejoin="round">'
        f'{bas_paths}</g></g></g>'
    )

    # Olay 1: Baş 3 yolu kalemle
    t0_bas = 0.43
    for i in range(3):
        t_b = t0_bas + 0.05 * i
        s.cmd.append({"m": "draw", "id": f"bas{i}", "t": round(t_b, 4), "d": 0.32, "a": 1})
        s.olay(t_b, "cizgi", 0.55)

    # Olay 2: Balon çizimi
    t_bal = S(T6(0)) - 0.05
    s.yol("bal", Y.balon_sol(410, 565, 1010, 905, 290, 845), t_bal, 0.55, KRE, 4.5, tur="cizgi", guc=0.7)
    bal_ids.append("bal")

    # Olay 3: Soru sözcükleri
    words_s6 = [w["sozcuk"] for w in S6]
    sp = g(" ", 64, 700, "Caveat")
    satir_duzeni = [
        (0, 1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
    ]
    base_ys = [665, 749, 833]
    pos: dict[int, tuple[float, float, float]] = {}

    for sat, by in zip(satir_duzeni, base_ys):
        cur_x = 450.0
        for idx in sat:
            m = words_s6[idx]
            w = g(m, 64, 700, "Caveat")
            s.yazi(f"bw{idx}", cur_x, by, [(m, KRE)], "Caveat", 700, 64, S(T6(idx)), 0.12, tur="tik", guc=0.5)
            bal_ids.append(f"bw{idx}")
            pos[idx] = (cur_x, w, by)
            cur_x += w + sp
        assert cur_x - sp <= 980, f"Soru satırı sağ ucu taştı: {cur_x - sp:.1f} > 980"

    # Olay 4: Sarı nokta nk + bağ cn
    x1, w1, _ = pos[1]
    NX = x1 + w1 / 2
    NY = 548.0
    assert NX >= L2SON + 20, f"NX çok solda: {NX:.1f} < {L2SON + 20:.1f}"

    t_nk = S(T6(1))
    s.yol("nk", f"M {NX:.1f} {NY:.1f} L {NX + 0.1:.1f} {NY:.1f}", t_nk, 0.12, SAR, 18.0, tur="tik", guc=0.45)
    bal_ids.append("nk")

    ok_basi = f"M {XU + 19:.1f} 427.5 L {XU:.1f} 438.0 L {XU + 19:.1f} 448.5"
    d_cn = f"M {NX:.1f} 548.0 L {NX:.1f} 454.0 Q {NX:.1f} 438.0 {NX - 16:.1f} 438.0 L {XU:.1f} 438.0 {ok_basi}"
    t_cn = t_nk + 0.14
    s.yol("cn", d_cn, t_cn, 0.45, SAR, 6.0, alfa=0.9, tur="cizgi", guc=0.45)
    bal_ids.append("cn")

    # Olay 5: bm8 (-ing altı) + soldur(krm -> krm_s)
    x8, w8, _ = pos[8]
    t_bm8 = S(T6(8))
    d_bm8 = Y.el_cizgi(x8 - 2, 866, x8 + w8 + 2, 864, 1.0)
    s.yol("bm8", d_bm8, t_bm8, 0.28, SAR, 10.0, tur="cizgi", guc=0.5)
    bal_ids.append("bm8")
    soldur(s, "krm", "krm_s", t_bm8)

    # ================= 3. Öğretmen Cevabı =================
    # Olay 6: #balg söner, #basm taşınır
    t6 = S(T7("Planı"))
    s.to("#balg", t6, {"opacity": 0, "duration": 0.4, "ease": "power2.in"})
    s.olay(t6, "vurus", 0.5)
    s.to(
        "#basm",
        t6,
        {
            "x": 796,
            "y": 550,
            "scale": round(160 / 240, 4),
            "svgOrigin": "96 680",
            "duration": 0.6,
            "ease": "power3.inOut",
        },
    )

    # Olay 7: Figür kalemle, soldur(klm -> klm_s), Zincir 1
    t7 = S(T7("insanlar"))
    _, FW = s.figur("standing-3", "fig", 72, 556, 420, t7, t7 + 1.0, w=4.4)
    assert 72 + FW + 40 <= 268, f"Figür çok sağa taştı: {72 + FW + 40:.1f} > 268"

    soldur(s, "klm", "klm_s", t7 + 0.1)

    # Zincir 1 (zs)
    ZB1 = (690.0, 800.0, 910.0)
    zamanlar_sag = [
        t7 + 0.1,             # Olay 7: person
        S(T7("yapar:")),      # Olay 8: plan
        S(T7("arkadaşım.")),  # Olay 10: am / is / are +
    ]
    satirlar_sag = [
        [("person", KRE)],
        [("plan", KRE)],
        [("am / is / are + ", KRE)],
    ]
    pos_zs = zincir(s, "zs", satirlar_sag, zamanlar_sag, x0=268.0, ZB=ZB1)

    # Olay 10: Hap zsy2v (V-ing) + Yazı ikizi zsy2s
    x_zs2, w_zs2, _ = pos_zs["zsy2"]
    x_hap_zs = x_zs2 + w_zs2 + 12
    w_ving = g("V-ing", 64, 700, "Caveat")
    assert x_hap_zs - 10 + (w_ving + 20) <= 960, f"zsy2v sağ kenara taştı: {x_hap_zs - 10 + w_ving + 20:.1f} > 960"

    s.svg.append(hap("zsy2v", x_hap_zs, ZB1[2], "V-ing"))
    s.svg.append(
        f'<text id="zsy2s" x="{x_hap_zs:.1f}" y="{ZB1[2]:.1f}" font-family="Caveat" font-weight="700" '
        f'font-size="64" fill="{KRE}" opacity="0" xml:space="preserve">V-ing</text>'
    )
    t10 = S(T7("arkadaşım."))
    s.goster("#zsy2v", t10 + 0.35, d=0.3)

    # Olay 9: ok_fig + ok_fig_s (t9), soldur(krm_s -> krm) +0.45
    t9 = S(T7("ben,"))
    d_ok_fig = Y.el_ok(72 + FW + 14, 710, XG + WG / 2 + 10, 552, 2.0)
    s.yol("ok_fig", d_ok_fig, t9, 0.45, SAR, 8.0, alfa=1.0, tur="cizgi", guc=0.55)
    s.yol("ok_fig_s", d_ok_fig, t9, 0.45, IKN, 8.0, alfa=0.0, tur=None)
    soldur(s, "krm_s", "krm", t9 + 0.45)

    # Olay 11: Tren çizimi, soldur(ok_fig -> ok_fig_s), soldur(krm -> krm_s), Zincir 2
    t11 = S(T7("Tren"))
    TX0, TY0, k = 548.0, 1035.0, 1.1
    assert TX0 + 420 * k <= 1032, f"Tren sağ kenara taştı: {TX0 + 420 * k:.1f} > 1032"

    parcalar_tr, tren_ids = tren_parcalari(TX0, TY0, k)
    zamanlar_tr = Y.cizgi_zamanlari([p[3] for p in parcalar_tr], t11, t11 + 1.0)
    for i, (d, renk, w_tr, _) in enumerate(parcalar_tr):
        b, dur = zamanlar_tr[i]
        s.yol(f"tr{i}", d, b, dur, renk, w_tr, 1.0, tur="cizgi" if i < 4 else None, guc=0.5)

    soldur(s, "ok_fig", "ok_fig_s", t11)
    soldur(s, "krm", "krm_s", t11)

    # Zincir 2 (zt)
    ZB2 = (1065.0, 1175.0, 1285.0)
    zamanlar_sol = [
        t11 + 0.1,            # Olay 11: train
        S(T7("tarifeye")),    # Olay 12: timetable
        S(T7("geniş")),       # Olay 16: büküm oku
    ]
    satirlar_sol = [
        [("train", KRE)],
        [("timetable", KRE)],
        None,
    ]
    pos_zt = zincir(s, "zt", satirlar_sol, zamanlar_sol, x0=72.0, ZB=ZB2)

    # Olay 13: ok_trn + ok_trn_s (0.6 sn), soldur(klm_s -> klm) +0.6
    t13 = S(T7("uyar."))
    d_ok_trn = f"M 1000 {TY0 + 60:.1f} L 1000 454.0 Q 1000 438.0 984.0 438.0 L {XU:.1f} 438.0 {ok_basi}"
    s.yol("ok_trn", d_ok_trn, t13, 0.6, SAR, 8.0, alfa=1.0, tur="cizgi", guc=0.55)
    s.yol("ok_trn_s", d_ok_trn, t13, 0.6, IKN, 8.0, alfa=0.0, tur=None)
    soldur(s, "klm_s", "klm", t13 + 0.6)

    # Olay 14: Öğrenci baş sallar
    tb_bas = t13 + 0.46
    orig_bas = f"{BTX + 75 * BS0:.1f} {BTY + 300 * BS0:.1f}"
    s.to(
        "#basn",
        tb_bas,
        {"y": 12, "rotation": 4, "duration": 0.22, "ease": "sine.inOut", "svgOrigin": orig_bas},
    )
    s.to(
        "#basn",
        tb_bas + 0.22,
        {"y": 0, "rotation": 0, "duration": 0.26, "ease": "sine.inOut", "svgOrigin": orig_bas},
    )
    s.to(
        "#basn",
        tb_bas + 0.48,
        {"y": 12, "rotation": 4, "duration": 0.22, "ease": "sine.inOut", "svgOrigin": orig_bas},
    )
    s.to(
        "#basn",
        tb_bas + 0.70,
        {"y": 0, "rotation": 0, "duration": 0.30, "ease": "sine.inOut", "svgOrigin": orig_bas},
    )

    # Olay 15: TIMETABLE nabzı
    t15 = S(T7("Tarife"))
    kalinlik(s, "#klm", t15, 10.0, 16.0)
    x_zt1, w_zt1, b_zt1 = pos_zt["zty1"]
    nabiz(s, "#zty1", t15, x_zt1 + w_zt1 / 2, b_zt1 - 24, 1.08)

    # Olay 16: Hap zty2v (V1 / V-s) + soldur(ok_trn -> ok_trn_s)
    x_hap_zt = x_zt1 + 74.0
    s.svg.append(hap("zty2v", x_hap_zt, ZB2[2], "V1 / V-s"))
    t16 = S(T7("geniş"))
    s.goster("#zty2v", t16 + 0.15, d=0.3)
    soldur(s, "ok_trn", "ok_trn_s", t16)

    # Olay 17: ktm (*The train* altı), zsy2v söner, zsy2s görünür
    t17 = S(T7("özne"))
    w_train = g("The train", 64, 700, "Fredoka")
    d_ktm = Y.el_cizgi(46, 418, 48 + w_train + 2, 418, 1.0)
    s.yol("ktm", d_ktm, t17, 0.4, SAR, 10.0, tur="cizgi", guc=0.5)
    s.set("#zsy2v", t17, {"opacity": 0})
    s.set("#zsy2s", t17, {"opacity": 1})

    # Olay 18: Tren nabzı
    t18 = S(T7("tren,"))
    nabiz(s, "#trn", t18, TX0 + 205 * k, TY0 + 80 * k, 1.06)

    # Olay 19: Uçak simgesi
    t19 = S(T7("uçak,"))
    ikon(s, "ik_ucak", "plane", 540, 1240, 140, t19, 0.35)

    # Olay 20: Kitap simgesi
    t20 = S(T7("ders."))
    ikon(s, "ik_kitap", "book", 700, 1240, 140, t20, 0.35)

    # ================= 4. Altyazı aç/kapa =================
    dilimler = Y.altyazi_dilimleri([6, 7])
    for i, (t0, t1, _) in enumerate(dilimler):
        t_ac = max(0.0, round(S(t0) - 0.05, 4))
        s.set(f"#alt{i}", t_ac, {"opacity": 1})
        if i < len(dilimler) - 1:
            sonraki_t0 = dilimler[i + 1][0]
            t_kapa = round(min(S(t1) + 0.35, S(sonraki_t0) - 0.05), 4)
            if t_kapa < Z["sure"]:
                s.set(f"#alt{i}", t_kapa, {"opacity": 0})

    alt_svg = Y.altyazi_svg([{"id": f"alt{i}", "metin": m} for i, (_, _, m) in enumerate(dilimler)])

    return s, {
        "kun": kunye_tam(),
        "bal_ids": bal_ids,
        "tren_ids": set(tren_ids),
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
            gruplar=[("trn", p["tren_ids"])],
        )
    )
    print(f"index.html yazıldı; komut {len(s.cmd)} olay {len(s.ev)}")

"""Sahne 06 — Soru anı 1 (02-04 YDT temel, HyperFrames, 1920x1080; cümle 6 öğrenci, cümle 7 öğretmen).
Öğrenci sorusu: «Hocam, tren de plana göre kalkmıyor mu? Neden -ing yok?»
Öğretmen cevabı: «Planı bir kişi yapar: ben, biz, arkadaşım. Tren plan yapmaz, tarifeye uyar...»
Yerleşim: İki kart (sol TIMETABLE, sağ ARRANGEMENT) üstte statik; sol altta tren ve simgeler,
sağ altta konuşan kişi; ortada basamaklı kavram zincirleri.
yanılgı: tarifeli gelecek planlanmış gelecekle karışır (tren de plana göre kalkar → -ing). Soru 10 sözcük (≤ 12).
Tasarım ve olay tablosu: SPEC.md (şef); kod agy-filo (rol kod) 14.11.
"""
import json
import math
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402
from yardim import u  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_ham = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
S6 = [w for w in _ham if w["cumle"] == 6]
S7 = [w for w in _ham if w["cumle"] == 7]

SORU = ["Hocam,", "tren", "de", "plana", "göre", "kalkmıyor", "mu?", "Neden", "-ing", "yok?"]
assert [w["sozcuk"] for w in S6] == SORU, f"S6 sözcükleri beklenenden farklı: {[w['sozcuk'] for w in S6]}"

R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]


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
    r = u(12)
    k = u(13)
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
        return TX0 + u(k * x), TY0 + u(k * y)

    def K(x: float, y: float, w: float, h: float, j: int = 0) -> str:
        return kutu_d(TX0 + u(k * x), TY0 + u(k * y), u(k * w), u(k * h), j)

    def D(cx: float, cy: float, r: float, ry: float | None = None) -> str:
        return daire_d(TX0 + u(k * cx), TY0 + u(k * cy), u(k * r), u(k * ry) if ry else None)

    parcalar = [
        (K(0, 45, 175, 85, 1), KRE, u(4.5), 2 * (175 + 85) * k),
        (K(200, 55, 170, 75, 2), KRE, u(4.5), 2 * (170 + 75) * k),
        (K(200, 10, 75, 45, 3), KRE, u(4.5), 2 * (75 + 45) * k),
        (K(320, 22, 26, 33, 4), KRE, u(3.6), 2 * (26 + 33) * k),
        (
            f"M{P(370, 95)[0]:.1f} {P(370, 95)[1]:.1f} L{P(398, 130)[0]:.1f} {P(398, 130)[1]:.1f} "
            f"L{P(370, 130)[0]:.1f} {P(370, 130)[1]:.1f}",
            KRE,
            u(4.5),
            (math.hypot(28, 35) + 28) * k,
        ),
        (
            f"M{P(175, 112)[0]:.1f} {P(175, 112)[1]:.1f} L{P(200, 112)[0]:.1f} {P(200, 112)[1]:.1f}",
            KRE,
            u(3.6),
            25 * k,
        ),
        (K(20, 60, 50, 30, 5), KRE, u(3.6), 2 * (50 + 30) * k),
        (K(100, 60, 50, 30, 6), KRE, u(3.6), 2 * (50 + 30) * k),
        (K(215, 20, 42, 25, 7), KRE, u(3.6), 2 * (42 + 25) * k),
        (D(40, 138, 17), KRE, u(4.5), 2 * math.pi * 17 * k),
        (D(135, 138, 17), KRE, u(4.5), 2 * math.pi * 17 * k),
        (D(240, 138, 17), KRE, u(4.5), 2 * math.pi * 17 * k),
        (D(335, 138, 17), KRE, u(4.5), 2 * math.pi * 17 * k),
        (
            f"M{P(-10, 158)[0]:.1f} {P(-10, 158)[1]:.1f} L{P(420, 158)[0]:.1f} {P(420, 158)[1]:.1f}",
            IKN,
            u(4.0),
            430 * k,
        ),
        (D(345, 2, 11, 9), IKN, u(3.4), 2 * math.pi * math.sqrt((11 * 11 + 9 * 9) / 2) * k),
        (D(372, -16, 8, 7), IKN, u(3.4), 2 * math.pi * math.sqrt((8 * 8 + 7 * 7) / 2) * k),
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
    w_line = u(4.6) / olcek
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


def zincir(s: Y.Sahne, ad: str, satirlar: list, zamanlar: list[float], x0: float) -> None:
    """Kavram zinciri: satır 0 düz yazı, sonraki satırlar büküm oku + yazı."""
    ZB = (u(560), u(650), u(740))
    xp = x0
    s.yazi(f"{ad}y0", xp, ZB[0], satirlar[0], "Fredoka", 700, u(44), zamanlar[0], 0.3)
    for i in range(1, len(satirlar)):
        t_arr = zamanlar[i]
        d_ok = bukum_ok(xp + u(14), ZB[i - 1] + u(22), ZB[i] - u(14), xp + u(50))
        s.yol(f"{ad}z{i}", d_ok, t_arr, 0.3, IKN, u(4.5), 1.0, "cizgi", 0.45)
        xp = xp + u(64)
        s.yazi(f"{ad}y{i}", xp, ZB[i], satirlar[i], "Fredoka", 700, u(44), t_arr + 0.15, 0.3)


def uret() -> tuple[Y.Sahne, dict]:
    s = Y.Sahne(TB)
    S = s.S
    bal_ids: list[str] = []

    # ================= 1. Kartlar (ilk kareden statik) =================
    w_kart, h_kart = u(810), u(300)
    x_sol, x_sag, y_kart = u(100), u(1010), u(118)
    pad = u(40)
    s.svg.append(statik("klk", Y.el_kutu(x_sol, y_kart, w_kart, h_kart), KRE, u(4.5)))
    s.svg.append(statik("krk", Y.el_kutu(x_sag, y_kart, w_kart, h_kart), KRE, u(4.5)))

    # Kart satırları (Fredoka 700, 48)
    b1, b2 = u(200), u(268)
    x_sol_ic = x_sol + pad
    x_sag_ic = x_sag + pad
    satirlar_kart = [
        ("The train to İzmir", "klt1", x_sol_ic, b1),
        ("leaves at 7 pm today.", "klt2", x_sol_ic, b2),
        ("I am going to the", "krt1", x_sag_ic, b1),
        ("movie theater tonight.", "krt2", x_sag_ic, b2),
    ]
    for text, kid, kx, ky in satirlar_kart:
        assert g(text, 48) <= 730, f"Kart satırı taştı: {text}"
        s.svg.append(metin(kid, kx, ky, text, "Fredoka", 700, u(48), KRE, "start"))

    # Etiketler (Caveat 700, 54)
    x_sol_end = x_sol + w_kart - pad
    x_sag_end = x_sag + w_kart - pad
    y_etiket = u(372)
    s.svg.append(metin("klt_e", x_sol_end, y_etiket, "TIMETABLE", "Caveat", 700, u(54), KRE, "end"))
    s.svg.append(metin("krt_e", x_sag_end, y_etiket, "ARRANGEMENT", "Caveat", 700, u(54), KRE, "end"))
    w_klu = g("TIMETABLE", 54, 700, "Caveat")
    w_kru = g("ARRANGEMENT", 54, 700, "Caveat")
    s.svg.append(
        statik(
            "klu",
            Y.el_cizgi(x_sol_end - w_klu - u(4), y_etiket + u(16), x_sol_end + u(4), y_etiket + u(16), 1),
            SAR,
            u(7),
            0.9,
        )
    )
    s.svg.append(
        statik(
            "kru",
            Y.el_cizgi(x_sag_end - w_kru - u(4), y_etiket + u(16), x_sag_end + u(4), y_etiket + u(16), 1),
            SAR,
            u(7),
            0.9,
        )
    )

    # Sahne 05 odakları (statik)
    w_leaves = g("leaves", 48)
    s.svg.append(
        statik(
            "klm",
            Y.el_cizgi(x_sol_ic - u(2), b2 + u(14), x_sol_ic + w_leaves + u(2), b2 + u(14), 1),
            SAR,
            u(9),
            0.85,
        )
    )
    w_I = g("I ", 48)
    w_am_going = g("am going", 48)
    x_ag = x_sag_ic + w_I
    s.svg.append(statik("krm", Y.el_cizgi(x_ag - u(2), b1 + u(14), x_ag + w_am_going + u(2), b1 + u(14), 1),
                        SAR, u(9), 0.85))

    # ================= 2. Soru anı: Öğrenci başı + Balon =================
    # Öğrenci başı (0,43 sn, ilk 12 kare durgun; baş gruptan bağımsız kalır)
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.55, u(118), u(790)
    bas_paths = "".join(f'<path id="bas{i}" d="{d}" style="opacity:0"/>' for i, d in enumerate(bd))
    s.svg.append(
        f'<g id="basn"><g id="bas" transform="translate({BTX:.1f} {BTY:.1f}) scale({BS:.2f})" '
        f'fill="none" stroke="{KRE}" stroke-width="{u(2.8) / BS:.2f}" '
        f'stroke-linecap="round" stroke-linejoin="round">{bas_paths}</g></g>'
    )
    t0_bas = 0.43
    for i in range(3):
        s.cmd.append({"m": "draw", "id": f"bas{i}", "t": round(t0_bas + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0_bas + 0.05 * i, "cizgi", 0.55)

    # Balon ve soru sözcükleri (T6(0) - 0.05)
    BF, BX0, BY0 = u(44), u(300), u(660)
    sp = g(" ", 44, 600)
    satir = ((0, 1, 2, 3, 4, 5, 6), (7, 8, 9))
    gens = [sum(g(S6[i]["sozcuk"], 44, 600) for i in sat) + sp * (len(sat) - 1) for sat in satir]
    x1b = BX0 + max(gens) + u(70)
    assert x1b < u(1880), f"Balon taştı: {x1b}"
    BASE = (BY0 + u(72), BY0 + u(136))
    s.yol("bal", Y.balon_sol(BX0, BY0, x1b, BY0 + u(190), BX0 - u(62), BY0 + u(212)),
          S(T6(0)) - 0.05, 0.55, KRE, u(4.2), 1.0, "cizgi", 0.7)
    bal_ids.append("bal")

    pos: dict[int, tuple[float, float, float]] = {}
    for sat, bs in zip(satir, BASE):
        x = BX0 + u(35)
        for i in sat:
            m = S6[i]["sozcuk"]
            w = g(m, 44, 600)
            s.yazi(f"bw{i}", x, bs, [(m, KRE)], "Fredoka", 600, BF, S(S6[i]["t0"]), 0.12, tur="tik", guc=0.5)
            bal_ids.append(f"bw{i}")
            pos[i] = (x, w, bs)
            x += w + sp

    # -ing altı SAR (Event 5)
    x8, w8, b8 = pos[8]
    s.yol("bm8", Y.el_cizgi(x8 - u(2), b8 + u(12), x8 + w8 + u(2), b8 + u(9), 1.0),
          S(T6(8)), 0.28, SAR, u(8), 0.85, "cizgi", 0.5)
    bal_ids.append("bm8")

    # Sarı nokta + bağ çizgisi (Event 4)
    x_nk = BX0 + u(110)
    y_nk = BY0 - u(22)
    td = S(T6(1))
    s.yol("nk", f"M{x_nk:.1f} {y_nk:.1f} L{x_nk + 0.1:.1f} {y_nk:.1f}", td, 0.12, SAR, u(18), 1.0, "tik", 0.45)
    x_lv_mid = x_sol_ic + w_leaves / 2
    s.yol("cn", Y.el_cizgi(x_nk, y_nk, x_lv_mid, b2 + u(34), -2.0),
          td + 0.14, 0.45, SAR, u(4.5), 0.9, "cizgi", 0.45)
    bal_ids.extend(["nk", "cn"])

    # ================= 3. Öğretmen cevabı olayları =================
    # Event 6: #balg söner (baş KALIR)
    th = S(T7("Planı"))
    s.to("#balg", th, {"opacity": 0, "duration": 0.4, "ease": "power2.in"})
    s.olay(th, "vurus", 0.5)

    # Event 7: kru kalınlık nabzı
    kalinlik(s, "#kru", th + 0.1, u(7), u(12))

    # Event 8: figür kalemle
    t_fig = S(T7("kişi"))
    _, gen_fig = s.figur("standing-1", "fig", u(1640), u(470), u(470), t_fig, t_fig + 1.0, w=u(3.4))
    assert u(1640) + gen_fig <= u(1864), f"Figür taştı: {u(1640) + gen_fig}"

    # Events 9, 10, 12: Sağ zincir
    zamanlar_sag = [S(T7("kişi")) + 0.1, S(T7("yapar:")), S(T7("arkadaşım."))]
    satirlar_sag = [
        [("person", KRE)],
        [("plan", KRE)],
        [("am / is / are + ", KRE), ("V-ing", SAR)],
    ]
    zincir(s, "zs", satirlar_sag, zamanlar_sag, x0=u(1040))

    # Event 11: figür oku -> am going; ardından krm kalınlık nabzı
    t_ok1 = S(T7("ben,"))
    x_ag_mid = x_ag + w_am_going / 2
    s.yol("ok_fig", Y.el_ok(u(1640 - 14), u(470 + 70), x_ag_mid, u(118 + 300 + 16), 2.0),
          t_ok1, 0.45, SAR, u(7), 0.9, "cizgi", 0.55)
    kalinlik(s, "#krm", t_ok1 + 0.45, u(9), u(14))

    # Event 13: tren çizimi (1.0 sn, orantılı süreler)
    TX0, TY0, k = u(515), u(500), 0.85
    parcalar_tr, tren_ids = tren_parcalari(TX0, TY0, k)
    t0_tr = S(T7("Tren"))
    zamanlar_tr = Y.cizgi_zamanlari([p[3] for p in parcalar_tr], t0_tr, t0_tr + 1.0)
    for i, (d, renk, w_tr, _) in enumerate(parcalar_tr):
        b, dur = zamanlar_tr[i]
        s.yol(f"tr{i}", d, b, dur, renk, w_tr, 1.0, tur="cizgi" if i < 4 else None, guc=0.5)

    # Events 14, 15, 19: Sol zincir
    zamanlar_sol = [S(T7("Tren")) + 0.1, S(T7("tarifeye")), S(T7("geniş"))]
    satirlar_sol = [
        [("train", KRE)],
        [("timetable", KRE)],
        [("V1 / V-s", SAR)],
    ]
    zincir(s, "zt", satirlar_sol, zamanlar_sol, x0=u(140))

    # Event 16: tren oku -> leaves; ardından klm kalınlık nabzı
    t_ok2 = S(T7("uyar."))
    s.yol("ok_trn", Y.el_ok(TX0 - u(10), TY0 + u(22), x_lv_mid + u(14), b2 + u(36), -3.0),
          t_ok2, 0.45, SAR, u(7), 0.9, "cizgi", 0.55)
    kalinlik(s, "#klm", t_ok2 + 0.45, u(9), u(14))

    # Event 17: öğrenci 1 sn baş sallar
    tb_bas = S(T7("uyar.")) + 0.46
    orig = f"{u(118) + u(75 * 0.55):.1f} {u(790) + u(300 * 0.55):.1f}"
    s.to(
        "#basn", tb_bas,
        {"y": u(9), "rotation": 4, "duration": 0.22, "ease": "sine.inOut", "svgOrigin": orig},
    )
    s.to(
        "#basn", tb_bas + 0.22,
        {"y": 0, "rotation": 0, "duration": 0.26, "ease": "sine.inOut", "svgOrigin": orig},
    )
    s.to(
        "#basn", tb_bas + 0.48,
        {"y": u(9), "rotation": 4, "duration": 0.22, "ease": "sine.inOut", "svgOrigin": orig},
    )
    s.to(
        "#basn", tb_bas + 0.70,
        {"y": 0, "rotation": 0, "duration": 0.30, "ease": "sine.inOut", "svgOrigin": orig},
    )

    # Event 18: klu kalınlık nabzı
    kalinlik(s, "#klu", S(T7("Tarife")), u(7), u(12))

    # Event 20: The train altı SAR
    w_ttrain = g("The train", 48)
    s.yol("ktm", Y.el_cizgi(x_sol_ic - u(2), b1 + u(14), x_sol_ic + w_ttrain + u(2), b1 + u(14), 1.0),
          S(T7("özne")), 0.4, SAR, u(8), 0.85, "cizgi", 0.5)

    # Event 21: #trn tek nabız
    t_trn_nb = S(T7("tren,"))
    nabiz(s, "#trn", t_trn_nb, TX0 + u(205 * k), TY0 + u(80 * k), 1.06)

    # Event 22: Uçak simgesi
    ikon(s, "ik_ucak", "plane", u(555), u(660), u(84), S(T7("uçak,")), 0.35)

    # Event 23: Kitap simgesi
    ikon(s, "ik_kitap", "book", u(685), u(660), u(84), S(T7("ders.")), 0.35)

    kun = Y.kunye_svg("Question", Y.AJANDA.index("Examples"))
    return s, {"kun": kun, "bal_ids": bal_ids, "tren_ids": set(tren_ids)}


if __name__ == "__main__":
    s, parca = uret()
    Y.kontrol(s, Z["kare"])
    (AD / "proje").mkdir(exist_ok=True)
    logo = (u(56), u(1002), u(34) * Y.LOGO_EN_BOY, u(34))
    (AD / "proje" / "index.html").write_text(
        Y.html(
            s,
            Z["sure"],
            parca["kun"],
            None,
            logo,
            bal_ids=parca["bal_ids"],
            gruplar=[("trn", parca["tren_ids"])],
        )
    )
    print(f"index.html yazıldı; komut {len(s.cmd)} olay {len(s.ev)}")

"""Sahne 12 Ara özet DİKEY (02-04 YDT temel, HyperFrames, 1080x1920, 497 kare; cümle 14).
16.11 DUZ3: cümle 14 «Zaman sözcüğü ipucu verir. Türkçe ek yanıltabilir.»; blok 3 satır a «time word → clue»,
satır b «-yor → trap» (eski «Turkish -yor → clue» dersin tuzak bölümüyle çelişiyordu); «MEANING → decision»
satırı kalktı, aynı iddiayı alttaki MEANING FIRST taşır.
SPEC: projeler/02-04-ydt-temel-dikey/sahneler/12-hyperframes-ozet/SPEC.md
Yerleşim: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform 1536-1920 BOŞ."""
import json
import math
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402
from yardim import u  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text()) if w["cumle"] == 14]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
HAP_YAZI = R["zemin"]

# ---- yerleşim ve sabitler (mantıksal px) ----
KX, KW = u(48), u(984)
IX = u(88)
SAG = u(992)
BLOK = ((u(360), u(330)), (u(702), u(330)), (u(1044), u(210)))
TB, TF = u(64), u(64)
R1, R2, R3 = u(70), u(180), u(288)
R3A, R3B = u(74), u(170)
IKON_EN, IKON_BOY, IKON_ARA = u(150), u(110), u(20)
IKON_UST = u(116)
BEL_DY, BEL_W = round(max(0.28 * TB, 0.234 * TB + u(13)), 2), u(10)   # sözleşme: max(0,28 em, kuyruk + 13); Caveat p 0,234 em
AU, BO, HP, HY = u(84), u(24), u(14), 1.06
MF_X, MF_Y, MF_B = u(88), u(1340), u(96)
MF_BEL_DY, MF_BEL_W = round(0.28 * MF_B, 2), u(12)
GECIS_Y = u(1390)

# ---- ikon ızgara verisi (sahne 07 ile aynı) ----
MONT = [
    {"n": [(40, 4), (20, 10), (6, 70), (17, 74), (26, 34), (23, 116), (50, 117)]},
    {"n": [(60, 4), (80, 10), (94, 70), (83, 74), (74, 34), (77, 116), (50, 117)]},
    {"n": [(40, 4), (50, 9), (60, 4)], "egri": True},
    {"n": [(40, 4), (44, 21), (50, 34)], "egri": True}, {"n": [(60, 4), (56, 21), (50, 34)], "egri": True},
    {"n": [(50, 34), (50, 116)], "ince": True},
    {"n": [(29, 88), (41, 87)], "ince": True}, {"n": [(59, 87), (71, 88)], "ince": True},
]
TISORT = [
    {"n": [(37, 4), (14, 12), (0, 36), (14, 46), (24, 37), (24, 88), (76, 88), (76, 37), (86, 46), (100, 36),
           (86, 12), (63, 4)]},
    {"n": [(37, 4), (50, 14), (63, 4)], "egri": True},
    {"n": [(14, 12), (24, 37)], "ince": True}, {"n": [(86, 12), (76, 37)], "ince": True},
]
EV = [
    {"n": [(5, 12), (3, 12), (12, 3), (21, 12), (19, 12)]},
    {"n": [(5, 12), (5, 19), (5.6, 20.4), (7, 21), (17, 21), (18.4, 20.4), (19, 19), (19, 12)]},
    {"n": [(9, 21), (9, 15), (9.6, 13.6), (11, 13), (13, 13), (14.4, 13.6), (15, 15), (15, 21)], "ince": True},
]
BAVUL = [
    {"n": [(14, 30), (86, 30), (92, 36), (92, 86), (86, 92), (14, 92), (8, 86), (8, 36)], "kapali": True},
    {"n": [(38, 30), (38, 18), (42, 13), (58, 13), (62, 18), (62, 30)]},
    {"n": [(30, 34), (30, 88)], "ince": True}, {"n": [(70, 34), (70, 88)], "ince": True},
    {"daire": (22, 97, 4), "ince": True}, {"daire": (78, 97, 4), "ince": True},
]


def _kutu(x, y, w, h, ince=False):
    return {"n": [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], "kapali": True, "ince": ince}


TREN = [
    _kutu(200, 55, 170, 75), _kutu(200, 10, 75, 45), _kutu(320, 22, 26, 33, True),
    {"n": [(370, 95), (398, 130), (370, 130)]}, _kutu(0, 45, 175, 85),
    {"n": [(175, 112), (200, 112)], "ince": True},
    _kutu(20, 60, 50, 30, True), _kutu(100, 60, 50, 30, True), _kutu(215, 20, 42, 25, True),
    {"daire": (40, 138, 17)}, {"daire": (135, 138, 17)}, {"daire": (240, 138, 17)}, {"daire": (335, 138, 17)},
    {"n": [(-10, 158), (420, 158)], "ince": True},
]


def _bilet():
    def yay(x0, yon):
        return [(x0 - yon * 22 * math.cos(-math.pi / 2 + i / 12 * math.pi),
                 yon * 22 * math.sin(-math.pi / 2 + i / 12 * math.pi)) for i in range(13)]
    kenar = [(-180, -70), (180, -70), (180, -22)] + yay(180, 1) + [(180, 70), (-180, 70), (-180, 22)] + yay(-180, -1)
    p = [{"n": kenar + [(-180, -70)]}]
    p += [{"n": [(100, -58 + i * 20), (100, -47 + i * 20)], "ince": True} for i in range(6)]
    p += [{"n": [(-150, y), (x1, y)], "ince": True} for y, x1 in ((-30, 60), (0, 30), (30, 70))]
    return p


BILET = _bilet()


def _kutusu(parcalar):
    xs, ys = [], []
    for p in parcalar:
        if "daire" in p:
            x, y, r = p["daire"]
            xs += [x - r, x + r]
            ys += [y - r, y + r]
        else:
            xs += [q[0] for q in p["n"]]
            ys += [q[1] for q in p["n"]]
    return min(xs), min(ys), max(xs), max(ys)


def _daire_yolu(cx, cy, r):
    k = 0.5523 * r
    return ("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f "
            "C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
                cx + r, cy, cx + r, cy + k, cx + k, cy + r, cx, cy + r,
                cx - k, cy + r, cx - r, cy + k, cx - r, cy,
                cx - r, cy - k, cx - k, cy - r, cx, cy - r,
                cx + k, cy - r, cx + r, cy - k, cx + r, cy))


def ikon_yollari(parcalar, mx0, my0):
    """Izgara parçalarını IKON_EN x IKON_BOY kutusuna (merkez mx0, my0) sığdırır. Döner: [(d, uzunluk, ince)]."""
    gx0, gy0, gx1, gy1 = _kutusu(parcalar)
    sc = min(IKON_BOY / (gy1 - gy0), IKON_EN / (gx1 - gx0))
    gmx, gmy = (gx0 + gx1) / 2, (gy0 + gy1) / 2

    def P(q):
        return (mx0 + (q[0] - gmx) * sc, my0 + (q[1] - gmy) * sc)

    out = []
    for p in parcalar:
        if "daire" in p:
            x, y, r = p["daire"]
            c = P((x, y))
            out.append((_daire_yolu(c[0], c[1], r * sc), 2 * math.pi * r * sc, p.get("ince", False)))
            continue
        q = [P(v) for v in p["n"]]
        if p.get("kapali"):
            q = q + [q[0]]
        uz = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(q, q[1:]))
        if p.get("egri") and len(q) >= 3:
            d = "M%.1f %.1f" % q[0]
            for i in range(len(q) - 1):
                p0, p1, p2 = q[max(i - 1, 0)], q[i], q[i + 1]
                p3 = q[min(i + 2, len(q) - 1)]
                c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
                c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
                d += " C%.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p2)
            uz *= 1.05
        else:
            d = "M%.1f %.1f " % q[0] + " ".join("L%.1f %.1f" % v for v in q[1:])
        out.append((d, uz, p.get("ince", False)))
    return out


def T(i, bas):
    """Cümle 14, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    assert w["sozcuk"].lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, w["sozcuk"], bas)
    return w["t0"]


def gen_c(m):
    return Y.genislik("Caveat", 700, m, TB)


def gen_f(m):
    return Y.genislik("Fredoka", 700, m, TF)


def gen_mf(m):
    return Y.genislik("Fredoka", 700, m, MF_B)


def uret():
    s = Y.Sahne(Z["t_bas"])
    L = s.S
    olaylar = []

    def kayit(ad, t, soz):
        olaylar.append((ad, round(t, 2), soz))

    def parca(kim, x, y, m, t, d=0.35, tur="tik"):
        s.yazi(kim, x, y, [(m, KRE)], "Caveat", 700, TB, L(t), d, tur=tur, guc=0.5)
        return x + gen_c(m)

    def belirtec(kim, x0, x1, y, t, d=0.40):
        by = y + BEL_DY
        s.yol(kim, Y.el_cizgi(x0 - u(4), by, x1 + u(4), by - u(1), 1), L(t), d, SAR, BEL_W, 0.85, "cizgi", 0.5)

    def ok(kim, x, y, t, d=0.30):
        s.yol(kim, Y.el_ok(x, y - u(15), x + AU, y - u(15), 2.0), L(t), d, KRE, u(5), 0.9, "cizgi", 0.5)

    def hap(kim, x, y, m, t, d=0.35):
        w = gen_f(m)
        rx, ry, rw, rh = x - HP, y - TF * 0.80, w + 2 * HP, TF * HY
        s.defs.append('<clipPath id="c_%s"><rect id="r_%s" x="%.1f" y="%.1f" width="0" height="%.1f"/></clipPath>'
                      % (kim, kim, rx - u(4), ry - u(4), rh + u(8)))
        s.svg.append('<g id="%s" clip-path="url(#c_%s)"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" '
                     'rx="%.1f" fill="%s"/><text x="%.2f" y="%.2f" fill="%s" font-family="Fredoka" font-weight="700" '
                     'font-size="%s" xml:space="preserve">%s</text></g>'
                     % (kim, kim, rx, ry, rw, rh, u(12), SAR, x, y, HAP_YAZI, TF, m))
        s.cmd.append({"m": "rev", "id": "r_" + kim, "t": round(L(t), 4), "d": d, "w": round(rw + u(8), 1)})
        s.olay(L(t), "tik", 0.55)
        return rx + rw

    def ikon_ciz(blok_i, n, parcalar, ti, y0):
        alan = 3 * IKON_EN + 2 * IKON_ARA
        mx = (SAG - alan) + n * (IKON_EN + IKON_ARA) + IKON_EN / 2
        my = y0 + IKON_UST + IKON_BOY / 2
        yollar = ikon_yollari(parcalar, mx, my)
        t0 = L(ti)
        t1 = t0 + min(0.6, 0.25 + 0.05 * len(yollar))
        for j, ((d, _uz, ince), (b, du)) in enumerate(zip(yollar, Y.cizgi_zamanlari([q[1] for q in yollar], t0, t1))):
            s.yol("ki%d_%d_%d" % (blok_i, n, j), d, b, du, IKN if ince else KRE, u(3.0) if ince else u(4.0), 1.0,
                  "cizgi" if j < 2 else None, 0.4)

    sp, dot = gen_c(" "), gen_c("· ")

    # ---- Olay 1: Altyazı dilimleri (cümle 13 sonu + cümle 14) ----
    dil = Y.altyazi_dilimleri([13, 14])
    dilimler = []
    for i, (t0_dilim, t1_dilim, m_dilim) in enumerate(dil):
        goster = round(t0_dilim - 0.05, 3)
        sonraki_goster = round(dil[i + 1][0] - 0.05, 3) if i + 1 < len(dil) else None
        gizle = round(min(t1_dilim + 0.35, sonraki_goster) if sonraki_goster is not None else t1_dilim + 0.35, 3)
        if gizle > Z["t_bas"] and goster < Z["t_bas"] + Z["sure"]:
            dilimler.append((goster, gizle, m_dilim))

    for i, (goster, gizle, m_dilim) in enumerate(dilimler):
        s.set("#alt%d" % i, max(0.0, L(goster)), {"opacity": 1})
        if L(gizle) < Z["sure"]:
            s.set("#alt%d" % i, L(gizle), {"opacity": 0})
    s.dilimler = dilimler

    # ---- Olay 2: Çip Recap nabzı ----
    t0 = T(0, "Özet")
    cw = Y.genislik("Lexend", 700, "Recap", 40) + 64
    cx = 1032 - cw
    s.set("#ku-bolum", L(t0), {"svgOrigin": "%.2f %.2f" % (cx + cw / 2, 48 + 40)})
    s.to("#ku-bolum", L(t0), {"scale": 1.08, "duration": 0.18, "ease": "power2.out"})
    s.to("#ku-bolum", L(t0) + 0.18, {"scale": 1.0, "duration": 0.22, "ease": "power2.inOut"})
    s.olay(L(t0), "tik", 0.4)
    kayit("çip Recap nabzı", t0, "Özet. (0)")

    # ---- Blok 1: general · permanent · timetable -> V1 / V-s ----
    y0_b1, h_b1 = BLOK[0]
    tg = T(1, "Genel")
    s.yol("kf0", Y.el_kutu(KX, y0_b1, KW, h_b1), L(tg - 0.30), 0.50, IKN, u(4), 0.85, "cizgi", 0.45)
    kayit("blok 1 çerçevesi (el kutusu)", tg - 0.30, "Genel (1)")

    ya_b1 = y0_b1 + R1
    xe1_a = parca("m1a", IX, ya_b1, "general", tg)
    belirtec("b1a", IX, xe1_a, ya_b1, tg + 0.10)
    kayit("general + belirteç", tg, "Genel (1)")

    td = T(2, "durum")
    ikon_ciz(0, 0, MONT, td, y0_b1)
    kayit("mont ikonu (hücre 1)", td, "durum, (2)")

    tk = T(3, "kalıcı")
    x1_b = xe1_a + sp
    xe1_b = parca("m1b", x1_b, ya_b1, "· permanent ·", tk, d=0.40)   # BRIEF: satır sonu "·" liste sürer
    belirtec("b1b", x1_b + dot, xe1_b - gen_c(" ·"), ya_b1, tk + 0.10)
    kayit("· permanent + belirteç; ev ikonu", tk, "kalıcı (3)")
    ikon_ciz(0, 1, EV, tk + 0.20, y0_b1)

    tt = T(6, "tarifeli")
    yb_b1 = y0_b1 + R2
    xe1_c = parca("m1c", IX, yb_b1, "timetable", tt, d=0.40)
    belirtec("b1c", IX, xe1_c, yb_b1, tt + 0.10)
    kayit("timetable + belirteç; tren ikonu", tt, "tarifeli (6)")
    ikon_ciz(0, 2, TREN, tt + 0.20, y0_b1)

    tz = T(8, "geniş")
    yc_b1 = y0_b1 + R3
    ok("o1", IX, yc_b1, tz, d=0.30)
    w1b = hap("h1", IX + AU + BO, yc_b1, "V1 / V-s", tz + 0.14, d=0.35)
    kayit("kalem oku + hap V1 / V-s", tz, "geniş (8)")

    # ---- Blok 2: right now · temporary · arrangement -> am / is / are + V-ing ----
    y0_b2, h_b2 = BLOK[1]
    tc = T(10, "Konuşma")
    s.yol("kf1", Y.el_kutu(KX, y0_b2, KW, h_b2), L(tc - 0.30), 0.50, IKN, u(4), 0.85, "cizgi", 0.45)
    kayit("blok 2 çerçevesi", tc - 0.30, "Konuşma (10)")

    t_son1 = tc + 0.10
    for bid in ("b1a", "b1b", "b1c"):
        s.set("#" + bid, L(t_son1), {"attr": {"stroke": IKN}, "opacity": 0.6})
    kayit("blok 1 belirteçleri söner", t_son1, "—")

    ya_b2 = y0_b2 + R1
    xe2_a = parca("m2a", IX, ya_b2, "right now", tc, d=0.40)
    belirtec("b2a", IX, xe2_a, ya_b2, tc + 0.10)
    kayit("right now + belirteç", tc, "Konuşma (10)")

    ta1 = T(11, "anı")
    ikon_ciz(1, 0, TISORT, ta1, y0_b2)
    kayit("tişört ikonu", ta1, "anı, (11)")

    tg2 = T(12, "geçici")
    x2_b = xe2_a + sp
    xe2_b = parca("m2b", x2_b, ya_b2, "· temporary ·", tg2, d=0.40)
    belirtec("b2b", x2_b + dot, xe2_b - gen_c(" ·"), ya_b2, tg2 + 0.10)
    kayit("· temporary + belirteç; bavul ikonu", tg2, "geçici (12)")
    ikon_ciz(1, 1, BAVUL, tg2 + 0.20, y0_b2)

    tp = T(15, "planlanmış")
    yb_b2 = y0_b2 + R2
    xe2_c = parca("m2c", IX, yb_b2, "arrangement", tp, d=0.45)
    belirtec("b2c", IX, xe2_c, yb_b2, tp + 0.10)
    kayit("arrangement + belirteç; bilet ikonu", tp, "planlanmış (15)")
    ikon_ciz(1, 2, BILET, tp + 0.20, y0_b2)

    ts = T(17, "şimdiki")
    yc_b2 = y0_b2 + R3
    ok("o2", IX, yc_b2, ts, d=0.30)
    w2b = hap("h2", IX + AU + BO, yc_b2, "am / is / are + V-ing", ts + 0.14, d=0.50)
    kayit("kalem oku + hap am / is / are + V-ing", ts, "şimdiki (17)")

    # ---- Blok 3: time word -> clue / -yor -> trap (16.11 DUZ3) ----
    y0_b3, h_b3 = BLOK[2]
    tw = T(19, "Zaman")
    s.yol("kf2", Y.el_kutu(KX, y0_b3, KW, h_b3), L(tw - 0.30), 0.45, IKN, u(4), 0.85, "cizgi", 0.45)
    kayit("blok 3 çerçevesi", tw - 0.30, "Zaman (19)")

    t_son2 = tw + 0.10
    for bid in ("b2a", "b2b", "b2c"):
        s.set("#" + bid, L(t_son2), {"attr": {"stroke": IKN}, "opacity": 0.6})
    kayit("blok 2 belirteçleri söner", t_son2, "—")

    ya_b3 = y0_b3 + R3A
    xe3_a = parca("m3a", IX, ya_b3, "time word", tw, d=0.40)
    belirtec("b3a", IX, xe3_a, ya_b3, tw + 0.10)
    kayit("time word + belirteç", tw, "Zaman (19)")

    ti = T(21, "ipucu")
    ok("o3", xe3_a + BO, ya_b3, ti, d=0.25)
    w3a = hap("h3", xe3_a + BO + AU + BO, ya_b3, "clue", ti + 0.12, d=0.30)
    kayit("kalem oku + hap clue", ti, "ipucu (21)")

    yb_b3 = y0_b3 + R3B
    tr = T(23, "Türkçe")
    xe3_b = parca("m3b", IX, yb_b3, "-yor", tr, d=0.35)
    belirtec("b3b", IX, xe3_b, yb_b3, tr + 0.10)
    kayit("-yor + belirteç", tr, "Türkçe (23)")

    ty = T(25, "yanıltabilir")
    ok("o4", xe3_b + BO, yb_b3, ty, d=0.25)
    w3b = hap("h4", xe3_b + BO + AU + BO, yb_b3, "trap", ty + 0.12, d=0.30)
    kayit("kalem oku + hap trap", ty, "yanıltabilir (25)")

    # ---- Alt: MEANING FIRST + sarı belirteç ----
    tkr = T(26, "Kararı")
    s.yazi("mf", MF_X, MF_Y, [("MEANING FIRST", KRE)], "Fredoka", 700, MF_B, L(tkr), 0.40, tur="tik", guc=0.55)
    kayit("MEANING FIRST (alt)", tkr, "Kararı (26)")

    ta = T(27, "anlam")
    t_bmf = tkr + 0.10
    d_bmf = round(ta - t_bmf, 4)
    w_mf = gen_mf("MEANING FIRST")
    by_mf = MF_Y + MF_BEL_DY
    s.yol("bmf", Y.el_cizgi(MF_X - u(4), by_mf, MF_X + w_mf + u(4), by_mf - u(1), 1), L(t_bmf), d_bmf, SAR,
          MF_BEL_W, 0.85, "cizgi", 0.5)
    kayit("MEANING FIRST belirteci", t_bmf, "anlam (27)")

    tv = T(28, "verir")

    # ---- Geçiş çizgisi ----
    t_gc = tv + 0.02
    s.yol("gc", Y.el_cizgi(u(88), GECIS_Y, SAG, GECIS_Y - u(2), 1), L(t_gc), 0.42, IKN, u(4), 0.80, "cizgi", 0.4)
    kayit("geçiş çizgisi", t_gc, "verir. (28)")

    # ---- Assert'ler (SPEC §4.7) ----
    # 1. Her terim/hap/ikon sağ ucu <= SAG (992)
    assert xe1_b <= SAG, "blok 1 satır a taştı: %.1f > %.1f" % (xe1_b, SAG)
    assert xe1_c <= SAG, "blok 1 satır b terim taştı"
    assert w1b <= SAG, "blok 1 hap taştı: %.1f > %.1f" % (w1b, SAG)
    assert xe2_b <= SAG, "blok 2 satır a taştı: %.1f > %.1f" % (xe2_b, SAG)
    assert xe2_c <= SAG, "blok 2 satır b terim taştı"
    assert w2b <= SAG, "blok 2 hap taştı: %.1f > %.1f" % (w2b, SAG)
    assert w3a <= SAG, "blok 3 satır a hap taştı: %.1f > %.1f" % (w3a, SAG)
    assert w3b <= SAG, "blok 3 satır b hap taştı: %.1f > %.1f" % (w3b, SAG)
    assert MF_X + w_mf <= SAG, "MEANING FIRST taştı: %.1f > %.1f" % (MF_X + w_mf, SAG)

    # 2. Her satır metni <= 24 karakter
    metinler = [
        "general · permanent ·", "timetable", "V1 / V-s",
        "right now · temporary ·", "arrangement", "am / is / are + V-ing",
        "time word", "clue", "-yor", "trap", "MEANING FIRST"
    ]
    for m in metinler:
        assert len(m) <= 24, "metin 24 karakteri aştı: %r" % m

    # 3. blok 1-2 satır a belirteç alt kenarı + u(10) <= ikon hücresi üstü
    b1_alt = ya_b1 + BEL_DY + BEL_W / 2
    assert b1_alt + u(10) <= y0_b1 + IKON_UST, "blok 1 belirteç ikon hücresine yakın"
    b2_alt = ya_b2 + BEL_DY + BEL_W / 2
    assert b2_alt + u(10) <= y0_b2 + IKON_UST, "blok 2 belirteç ikon hücresine yakın"

    # 4. blok 1-2 hap rect üstü − ikon hücresi altı >= u(10)
    h1_ust = yc_b1 - TF * 0.80
    assert h1_ust - (y0_b1 + IKON_UST + IKON_BOY) >= u(10), "blok 1 hap ikon hücresine yakın"
    h2_ust = yc_b2 - TF * 0.80
    assert h2_ust - (y0_b2 + IKON_UST + IKON_BOY) >= u(10), "blok 2 hap ikon hücresine yakın"

    # 5. blok 3 satır b hap rect üstü − satır a belirteç alt kenarı >= u(10) (satır b hap = trap)
    b3a_alt = ya_b3 + BEL_DY + BEL_W / 2
    h4_ust = yb_b3 - TF * 0.80
    assert h4_ust - b3a_alt >= u(10), "blok 3 hap satır a belirtecine yakın"

    # 6. her blok çerçevesi 352 <= y0 ve y0 + h <= alt öğenin üstü
    mf_ust = MF_Y - 0.69 * MF_B
    assert y0_b1 >= 352 and y0_b1 + h_b1 <= y0_b2, "blok 1 dikey sınır ihlali"
    assert y0_b2 >= 352 and y0_b2 + h_b2 <= y0_b3, "blok 2 dikey sınır ihlali"
    assert y0_b3 >= 352 and y0_b3 + h_b3 <= mf_ust, "blok 3 dikey sınır ihlali"

    # 7. MEANING FIRST üstü (taban − 0,69·96) >= blok 3 altı + u(12)
    assert mf_ust >= y0_b3 + h_b3 + u(12), "MF blok 3'e yakın"

    # 8. MF belirteç alt kenarı + u(10) <= GECIS_Y − u(2)
    mf_bel_alt = MF_Y + MF_BEL_DY + MF_BEL_W / 2
    assert mf_bel_alt + u(10) <= GECIS_Y - u(2), "MF belirteç geçiş çizgisine yakın"

    # 9. GECIS_Y + u(2) <= 1392
    assert GECIS_Y + u(2) <= 1392, "geçiş çizgisi içerik bandına taştı"

    # Durgunluk kontrolü (ilk=True: ilk hareket >= 0.4 sn, son bitiş <= (kare-12)/30)
    bas, son = Y.kontrol(s, Z["kare"], ilk=True)
    s.olaylar = olaylar
    s.hareket = (bas, son)
    return s, Y.kunye_svg("Recap")


if __name__ == "__main__":
    s, kun = uret()
    (AD / "proje").mkdir(exist_ok=True)
    ek_altyazi = Y.altyazi_svg([{"id": "alt%d" % i, "metin": m} for i, (_, _, m) in enumerate(s.dilimler)])
    html_icerik = Y.html(s, Z["sure"], kun, None, (48, 48, round(96 * Y.LOGO_EN_BOY, 2), 96), ek=ek_altyazi)
    (AD / "proje" / "index.html").write_text(html_icerik)
    bas, son = s.hareket
    print("index.html yazıldı; komut %d olay %d hareket %.2f-%.2f sn (yerel)" % (len(s.cmd), len(s.ev), bas, son))
    for ad, t, soz in s.olaylar:
        yer = t - Z["t_bas"]
        print("  %7.2f sn  yerel %5.2f  kare %3d  %-16s %s" % (t, yer, round(yer * 30), soz, ad))

"""Sahne 07 Kural kartı (02-04 YDT temel dikey, HyperFrames 1080x1920, 523 kare; cümle 8).
Yerleşim BRIEF-DIKEY §2-§3 satır 7 + SPEC.md: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform boş.
Zaman: ../../zaman.json (t_bas, kare) + ortak/anlatim/sozcukler.json (cümle 8; t_bas 113.37)."""
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
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text()) if w["cumle"] == 8]
R = Y.RENK
KRE, IKN, SAR, ZEM = R["murekkep"], R["ikincil"], R["vurgu"], R["zemin"]

# ---- HUD okuma ve assert ----
KUNYE_JS = (PAKET / "ortak" / "kunye.js").read_text(encoding="utf-8")
DERS = json.loads(re.search(r'ders:\s*(\[[^\]]+\])', KUNYE_JS).group(1))
ROZET = re.search(r'rozet:\s*"([^"]+)"', KUNYE_JS).group(1)
CIP = re.search(r'"07-hyperframes-kural":\s*"([^"]+)"', KUNYE_JS).group(1)
assert DERS == ["SIMPLE PRESENT vs", "PRESENT CONTINUOUS"], f"ders adı uyuşmuyor: {DERS}"
assert ROZET == "YDT · TEMEL", f"rozet uyuşmuyor: {ROZET}"
assert CIP == "Rule", f"çip uyuşmuyor: {CIP}"

# ---- İkon verileri ve yardımcıları (SPEC §2 yatay kalıp) ----
IKON_BOY, IKON_EN = u(120), u(120)

MONT = [  # sahne 03 (mont 100x120)
    {"n": [(40, 4), (20, 10), (6, 70), (17, 74), (26, 34), (23, 116), (50, 117)]},
    {"n": [(60, 4), (80, 10), (94, 70), (83, 74), (74, 34), (77, 116), (50, 117)]},
    {"n": [(40, 4), (50, 9), (60, 4)], "egri": True},
    {"n": [(40, 4), (44, 21), (50, 34)], "egri": True}, {"n": [(60, 4), (56, 21), (50, 34)], "egri": True},
    {"n": [(50, 34), (50, 116)], "ince": True},
    {"n": [(29, 88), (41, 87)], "ince": True}, {"n": [(59, 87), (71, 88)], "ince": True},
]
TISORT = [  # sahne 03 (tişört 100x90)
    {"n": [(37, 4), (14, 12), (0, 36), (14, 46), (24, 37), (24, 88), (76, 88), (76, 37), (86, 46), (100, 36),
           (86, 12), (63, 4)]},
    {"n": [(37, 4), (50, 14), (63, 4)], "egri": True},
    {"n": [(14, 12), (24, 37)], "ince": True}, {"n": [(86, 12), (76, 37)], "ince": True},
]
EV = [  # sahne 04 ile aynı kaynak: Tabler home (24x24), köşe yayları nokta dizisine çevrildi
    {"n": [(5, 12), (3, 12), (12, 3), (21, 12), (19, 12)]},
    {"n": [(5, 12), (5, 19), (5.6, 20.4), (7, 21), (17, 21), (18.4, 20.4), (19, 19), (19, 12)]},
    {"n": [(9, 21), (9, 15), (9.6, 13.6), (11, 13), (13, 13), (14.4, 13.6), (15, 15), (15, 21)], "ince": True},
]
BAVUL = [  # kendi çizimimiz (100x100): gövde, sap, iki kayış, iki teker
    {"n": [(14, 30), (86, 30), (92, 36), (92, 86), (86, 92), (14, 92), (8, 86), (8, 36)], "kapali": True},
    {"n": [(38, 30), (38, 18), (42, 13), (58, 13), (62, 18), (62, 30)]},
    {"n": [(30, 34), (30, 88)], "ince": True}, {"n": [(70, 34), (70, 88)], "ince": True},
    {"daire": (22, 97, 4), "ince": True}, {"daire": (78, 97, 4), "ince": True},
]


def _kutu(x, y, w, h, ince=False):
    return {"n": [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], "kapali": True, "ince": ince}


TREN_D = [  # SPEC §4.4 sade lokomotif
    _kutu(200, 55, 170, 75), _kutu(200, 10, 75, 45), _kutu(320, 22, 26, 33, True),
    {"n": [(370, 95), (398, 130), (370, 130)]}, _kutu(215, 20, 42, 25, True),
    {"daire": (240, 138, 17)}, {"daire": (335, 138, 17)},
    {"n": [(190, 158), (410, 158)], "ince": True},
]


def _bilet_d():
    """SPEC §4.4 bilet sadeleştirmesi (merkez 0,0, yarı genişlik 110)."""
    def yay(x0, yon):
        return [(x0 - yon * 22 * math.cos(-math.pi / 2 + i / 12 * math.pi),
                 yon * 22 * math.sin(-math.pi / 2 + i / 12 * math.pi)) for i in range(13)]
    kenar = [(-110, -70), (110, -70), (110, -22)] + yay(110, 1) + [(110, 70), (-110, 70), (-110, 22)] + yay(-110, -1)
    p = [{"n": kenar + [(-110, -70)]}]
    p += [{"n": [(50, -58 + i * 20), (50, -47 + i * 20)], "ince": True} for i in range(6)]
    p += [{"n": [(-85, y), (x1, y)], "ince": True} for y, x1 in ((-30, 20), (0, 0), (30, 30))]
    return p


BILET_D = _bilet_d()


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


def ikon_yollari(parcalar, kenar_x, cy, sag_kenar, egim=0.0):
    """Izgara parçalarını sahne yoluna çevirir. sag_kenar True: ikon sağ kenarı kenar_x'te (sol sütun), False: sol
    kenarı kenar_x'te (sağ sütun); dikey merkez cy. Döner: [(d, uzunluk, ince)], (x0, x1)."""
    gx0, gy0, gx1, gy1 = _kutusu(parcalar)
    sc = min(IKON_BOY / (gy1 - gy0), IKON_EN / (gx1 - gx0))
    w = (gx1 - gx0) * sc
    x0 = kenar_x - w if sag_kenar else kenar_x
    ce, se = math.cos(egim), math.sin(egim)
    mx, my = (gx0 + gx1) / 2, (gy0 + gy1) / 2

    def P(q):
        dx, dy = (q[0] - mx) * sc, (q[1] - my) * sc
        return (x0 + w / 2 + dx * ce - dy * se, cy + dx * se + dy * ce)

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
    return out, (x0, x0 + w)


def T(i, bas):
    """Cümle 8, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    assert w["sozcuk"].lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, w["sozcuk"], bas)
    return w["t0"]


def kunye_tam_svg():
    """SPEC §4.2: Dikey HUD (ders 2 satır, rozet, çip)."""
    t1 = ('<text x="48" y="212" font-family="Fredoka" font-weight="700" font-size="56" fill="%s">%s</text>'
          % (KRE, DERS[0]))
    t2 = ('<text x="48" y="276" font-family="Fredoka" font-weight="700" font-size="56" fill="%s">%s</text>'
          % (KRE, DERS[1]))
    ku_ders = '<g id="ku-ders">%s%s</g>' % (t1, t2)

    w_ders1 = Y.genislik("Fredoka", 700, DERS[1], 56)
    rx = 48 + w_ders1 + 24
    rw = Y.genislik("Lexend", 700, ROZET, 36) + 56
    rt = ('<text x="%.2f" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" '
          'fill="%s">%s</text>' % (rx + rw / 2, ZEM, ROZET))
    ku_rozet = '<g id="ku-rz"><rect x="%.2f" y="216" width="%.2f" height="72" rx="36" fill="%s"/>%s</g>' % (
        rx, rw, SAR, rt)

    bolum_svg = Y.kunye_svg(CIP)
    m = re.search(r'(<g id="ku-bolum".*</g>)</g>', bolum_svg, re.DOTALL)
    ku_bolum = m.group(1)

    return '<g id="kunye">%s%s%s</g>' % (ku_ders, ku_rozet, ku_bolum)


def uret():
    s = Y.Sahne(Z["t_bas"])
    S = s.S
    olaylar = []

    def kayit(ad, t, soz):
        olaylar.append((ad, round(t, 2), soz))

    # ---------------- 1. Satır 1: 380-560, cy=470 ----------------
    t_s1_sol = S(T(7, "Genel"))
    s.yol("ayr1", Y.el_cizgi(u(540), u(394), u(542), u(546), 1.0), t_s1_sol, 0.3, IKN, u(4), 0.9, "cizgi", 0.4)
    s.yazi("y_gen", u(228), u(488), [("general", KRE)], "Caveat", 700, u(64), t_s1_sol, 0.35,
           anchor="start", tur="tik", guc=0.5)
    tb_s1_sol = t_s1_sol + 0.30
    s.yol("bag1_sol", Y.el_cizgi(u(214), u(470), u(190), u(471), 0.6), tb_s1_sol, 0.2, IKN, u(3), 0.9,
          "cizgi", 0.35)
    mont_yollar, mont_box = ikon_yollari(MONT, u(176), u(470), True, 0.0)
    ti0_mont = tb_s1_sol + 0.15
    ti1_mont = ti0_mont + min(0.75, 0.25 + 0.06 * len(mont_yollar))
    mont_zam = Y.cizgi_zamanlari([y[1] for y in mont_yollar], ti0_mont, ti1_mont)
    for n, ((d, _uz, ince), (b, du)) in enumerate(zip(mont_yollar, mont_zam)):
        s.yol("mont%d" % n, d, b, du, IKN if ince else KRE, u(3) if ince else u(4), 1.0,
              "cizgi" if n < 2 else None, 0.4)
    kayit("satır 1 sol: ayraç + general + bağ + mont", t_s1_sol, "Genel (7)")

    t_s1_sag = S(T(10, "konuşma"))
    s.yazi("y_rnow", u(852), u(488), [("right now", KRE)], "Caveat", 700, u(64), t_s1_sag, 0.4,
           anchor="end", tur="tik", guc=0.5)
    tb_s1_sag = t_s1_sag + 0.30
    s.yol("bag1_sag", Y.el_cizgi(u(866), u(470), u(890), u(471), 0.6), tb_s1_sag, 0.2, IKN, u(3), 0.9,
          "cizgi", 0.35)
    tisort_yollar, tisort_box = ikon_yollari(TISORT, u(904), u(470), False, 0.0)
    ti0_tis = tb_s1_sag + 0.15
    ti1_tis = ti0_tis + min(0.75, 0.25 + 0.06 * len(tisort_yollar))
    tis_zam = Y.cizgi_zamanlari([y[1] for y in tisort_yollar], ti0_tis, ti1_tis)
    for n, ((d, _uz, ince), (b, du)) in enumerate(zip(tisort_yollar, tis_zam)):
        s.yol("tis%d" % n, d, b, du, IKN if ince else KRE, u(3) if ince else u(4), 1.0,
              "cizgi" if n < 2 else None, 0.4)
    kayit("satır 1 sağ: right now + bağ + tişört", t_s1_sag, "konuşma (10)")

    # ---------------- 2. Satır 2: 570-750, cy=660 ----------------
    t_s2_sol = S(T(12, "Kalıcı"))
    s.yol("sayr2", Y.el_cizgi(u(64), u(565), u(1016), u(565), 1.2), t_s2_sol, 0.35, IKN, u(3), 0.9,
          "cizgi", 0.4)
    s.yol("ayr2", Y.el_cizgi(u(540), u(584), u(542), u(736), 1.0), t_s2_sol, 0.3, IKN, u(4), 0.9, None)
    s.yazi("y_perm", u(228), u(678), [("permanent", KRE)], "Caveat", 700, u(64), t_s2_sol, 0.4,
           anchor="start", tur="tik", guc=0.5)
    tb_s2_sol = t_s2_sol + 0.30
    s.yol("bag2_sol", Y.el_cizgi(u(214), u(660), u(190), u(661), 0.6), tb_s2_sol, 0.2, IKN, u(3), 0.9,
          "cizgi", 0.35)
    ev_yollar, ev_box = ikon_yollari(EV, u(176), u(660), True, 0.0)
    ti0_ev = tb_s2_sol + 0.15
    ti1_ev = ti0_ev + min(0.75, 0.25 + 0.06 * len(ev_yollar))
    ev_zam = Y.cizgi_zamanlari([y[1] for y in ev_yollar], ti0_ev, ti1_ev)
    for n, ((d, _uz, ince), (b, du)) in enumerate(zip(ev_yollar, ev_zam)):
        s.yol("ev%d" % n, d, b, du, IKN if ince else KRE, u(3) if ince else u(4), 1.0,
              "cizgi" if n < 2 else None, 0.4)
    kayit("satır 2 sol: ayırıcı + ayraç + permanent + bağ + ev", t_s2_sol, "Kalıcı (12)")

    t_s2_sag = S(T(15, "geçici"))
    s.yazi("y_temp", u(852), u(678), [("temporary", KRE)], "Caveat", 700, u(64), t_s2_sag, 0.4,
           anchor="end", tur="tik", guc=0.5)
    tb_s2_sag = t_s2_sag + 0.30
    s.yol("bag2_sag", Y.el_cizgi(u(866), u(660), u(890), u(661), 0.6), tb_s2_sag, 0.2, IKN, u(3), 0.9,
          "cizgi", 0.35)
    bavul_yollar, bavul_box = ikon_yollari(BAVUL, u(904), u(660), False, 0.0)
    ti0_bav = tb_s2_sag + 0.15
    ti1_bav = ti0_bav + min(0.75, 0.25 + 0.06 * len(bavul_yollar))
    bav_zam = Y.cizgi_zamanlari([y[1] for y in bavul_yollar], ti0_bav, ti1_bav)
    for n, ((d, _uz, ince), (b, du)) in enumerate(zip(bavul_yollar, bav_zam)):
        s.yol("bav%d" % n, d, b, du, IKN if ince else KRE, u(3) if ince else u(4), 1.0,
              "cizgi" if n < 2 else None, 0.4)
    kayit("satır 2 sağ: temporary + bağ + bavul", t_s2_sag, "geçici (15)")

    # ---------------- 3. Satır 3: 760-940, cy=850 (iki satırlı) ----------------
    t_s3_sol = S(T(17, "Tarifeli"))
    s.yol("sayr3", Y.el_cizgi(u(64), u(755), u(1016), u(755), 1.2), t_s3_sol, 0.35, IKN, u(3), 0.9,
          "cizgi", 0.4)
    s.yol("ayr3", Y.el_cizgi(u(540), u(774), u(542), u(926), 1.0), t_s3_sol, 0.3, IKN, u(4), 0.9, None)
    s.yazi("y_tt", u(228), u(834), [("timetable", KRE)], "Caveat", 700, u(64), t_s3_sol, 0.4,
           anchor="start", tur="tik", guc=0.5)
    tb_s3_sol = t_s3_sol + 0.30
    s.yol("bag3_sol", Y.el_cizgi(u(214), u(850), u(190), u(851), 0.6), tb_s3_sol, 0.2, IKN, u(3), 0.9,
          "cizgi", 0.35)
    tren_yollar, tren_box = ikon_yollari(TREN_D, u(176), u(850), True, 0.0)
    ti0_tren = tb_s3_sol + 0.15
    ti1_tren = ti0_tren + min(0.75, 0.25 + 0.06 * len(tren_yollar))
    tren_zam = Y.cizgi_zamanlari([y[1] for y in tren_yollar], ti0_tren, ti1_tren)
    for n, ((d, _uz, ince), (b, du)) in enumerate(zip(tren_yollar, tren_zam)):
        s.yol("trn%d" % n, d, b, du, IKN if ince else KRE, u(3) if ince else u(4), 1.0,
              "cizgi" if n < 2 else None, 0.4)
    kayit("satır 3 sol: ayırıcı + ayraç + timetable + bağ + tren", t_s3_sol, "Tarifeli (17)")

    t_s3_sol_fut = S(T(18, "gelecek"))
    s.yazi("y_fut_sol", u(228), u(902), [("(future)", KRE)], "Caveat", 700, u(64), t_s3_sol_fut, 0.35,
           anchor="start", tur="tik", guc=0.5)
    kayit("(future) sol", t_s3_sol_fut, "gelecek (18)")

    t_s3_sag = S(T(20, "planlanmış"))
    s.yazi("y_arr", u(852), u(834), [("arrangement", KRE)], "Caveat", 700, u(64), t_s3_sag, 0.45,
           anchor="end", tur="tik", guc=0.5)
    tb_s3_sag = t_s3_sag + 0.30
    s.yol("bag3_sag", Y.el_cizgi(u(866), u(850), u(890), u(851), 0.6), tb_s3_sag, 0.2, IKN, u(3), 0.9,
          "cizgi", 0.35)
    bilet_yollar, bilet_box = ikon_yollari(BILET_D, u(904), u(850), False, -0.06)
    ti0_bil = tb_s3_sag + 0.15
    ti1_bil = ti0_bil + min(0.75, 0.25 + 0.06 * len(bilet_yollar))
    bil_zam = Y.cizgi_zamanlari([y[1] for y in bilet_yollar], ti0_bil, ti1_bil)
    for n, ((d, _uz, ince), (b, du)) in enumerate(zip(bilet_yollar, bil_zam)):
        s.yol("bil%d" % n, d, b, du, IKN if ince else KRE, u(3) if ince else u(4), 1.0,
              "cizgi" if n < 2 else None, 0.4)
    kayit("satır 3 sağ: arrangement + bağ + bilet", t_s3_sag, "planlanmış (20)")

    t_s3_sag_fut = S(T(21, "gelecek"))
    s.yazi("y_fut_sag", u(852), u(902), [("(future)", KRE)], "Caveat", 700, u(64), t_s3_sag_fut, 0.35,
           anchor="end", tur="tik", guc=0.5)
    kayit("(future) sağ", t_s3_sag_fut, "gelecek (21)")

    # ---------------- 4. Ad satırı (y 960-1250) ----------------
    t_ad_sol = S(T(22, "Soldakiler"))
    s.yol("sayr_ad", Y.el_cizgi(u(64), u(950), u(1016), u(950), 1.2), t_ad_sol, 0.35, KRE, u(4), 0.9,
          "cizgi", 0.4)
    s.yol("ayr_ad", Y.el_cizgi(u(540), u(964), u(542), u(1246), 1.0), t_ad_sol, 0.3, IKN, u(4), 0.9, None)

    w_sim = Y.genislik("Fredoka", 700, "SIMPLE", u(64))
    s.yazi("ad_sim", u(294) - w_sim / 2, u(1018), [("SIMPLE", KRE)], "Fredoka", 700, u(64),
           t_ad_sol, 0.3, anchor="start", tur="tik", guc=0.5)

    t_pres_sol = t_ad_sol + 0.22
    w_pres_sol = Y.genislik("Fredoka", 700, "PRESENT", u(64))
    s.yazi("ad_pres_sol", u(294) - w_pres_sol / 2, u(1088), [("PRESENT", KRE)], "Fredoka", 700, u(64),
           t_pres_sol, 0.3, anchor="start", tur="tik", guc=0.5)
    kayit("ad ayırıcı + ayraç + SIMPLE / PRESENT", t_ad_sol, "Soldakiler (22)")

    t_v1 = S(T(23, "geniş"))
    w_v1 = Y.genislik("Caveat", 700, "V1 / V-s", u(72))
    s.yazi("ad_v1", u(294) - w_v1 / 2, u(1166), [("V1 / V-s", IKN)], "Caveat", 700, u(72),
           t_v1, 0.3, anchor="start", tur="tik", guc=0.5)
    kayit("V1 / V-s", t_v1, "geniş (23)")

    t_ad_sag = S(T(25, "sağdakiler"))
    w_pres_sag = Y.genislik("Fredoka", 700, "PRESENT", u(64))
    s.yazi("ad_pres_sag", u(786) - w_pres_sag / 2, u(1018), [("PRESENT", KRE)], "Fredoka", 700, u(64),
           t_ad_sag, 0.3, anchor="start", tur="tik", guc=0.5)

    t_cont = t_ad_sag + 0.22
    w_cont = Y.genislik("Fredoka", 700, "CONTINUOUS", u(64))
    s.yazi("ad_cont", u(786) - w_cont / 2, u(1088), [("CONTINUOUS", KRE)], "Fredoka", 700, u(64),
           t_cont, 0.3, anchor="start", tur="tik", guc=0.5)
    kayit("PRESENT / CONTINUOUS", t_ad_sag, "sağdakiler (25)")

    t_am = S(T(26, "şimdiki"))
    w_am = Y.genislik("Caveat", 700, "am / is / are", u(72))
    s.yazi("ad_am", u(786) - w_am / 2, u(1166), [("am / is / are", IKN)], "Caveat", 700, u(72),
           t_am, 0.3, anchor="start", tur="tik", guc=0.5)

    t_ving = S(T(27, "zaman"))
    w_ving = Y.genislik("Caveat", 700, "+ V-ing", u(72))
    s.yazi("ad_ving", u(786) - w_ving / 2, u(1232), [("+ V-ing", IKN)], "Caveat", 700, u(72),
           t_ving, 0.3, anchor="start", tur="tik", guc=0.5)
    kayit("am / is / are · + V-ing", t_am, "şimdiki (26) · zaman (27)")

    # ---------------- 5. Alt: MEANING FIRST (y 1270-1390) ----------------
    MF_BOY, MF_Y = u(110), u(1364)
    VURUS = 0.22
    wm = Y.genislik("Fredoka", 700, "MEANING ", MF_BOY)
    wf = Y.genislik("Fredoka", 700, "FIRST", MF_BOY)
    mf_toplam = wm + wf
    x0_mf = u(540) - mf_toplam / 2

    s.svg.append('<g id="mfa" style="opacity:0"><text x="%.2f" y="%.2f" font-family="Fredoka" font-weight="700" '
                 'font-size="%.1f" fill="%s" xml:space="preserve">%s</text></g>'
                 % (x0_mf, MF_Y, MF_BOY, KRE, "MEANING"))
    t_mf_a = S(T(28, "Seçmeden"))
    s.fromto("#mfa", t_mf_a, {"opacity": 0, "y": u(34), "scale": 0.86,
                              "svgOrigin": "%.1f %.1f" % (x0_mf + wm / 2, MF_Y)},
             {"opacity": 1, "y": 0, "scale": 1, "duration": VURUS, "ease": "back.out(1.6)"})
    s.olay(t_mf_a, "tik", 0.55)

    x_first = x0_mf + wm
    s.svg.append('<g id="mfb" style="opacity:0"><text x="%.2f" y="%.2f" font-family="Fredoka" font-weight="700" '
                 'font-size="%.1f" fill="%s" xml:space="preserve">%s</text></g>'
                 % (x_first, MF_Y, MF_BOY, KRE, "FIRST"))
    t_mf_b = S(T(29, "önce"))
    s.fromto("#mfb", t_mf_b, {"opacity": 0, "y": u(34), "scale": 0.86,
                              "svgOrigin": "%.1f %.1f" % (x_first + wf / 2, MF_Y)},
             {"opacity": 1, "y": 0, "scale": 1, "duration": VURUS, "ease": "back.out(1.6)"})
    s.olay(t_mf_b, "tik", 0.55)
    kayit("MEANING · FIRST kinetik", t_mf_a, "Seçmeden (28) · önce (29)")

    ta = S(T(31, "anlamına"))
    s.yol("mfc", Y.el_cizgi(x0_mf - u(6), u(1380), x0_mf + mf_toplam + u(6), u(1379), 1.0),
          ta, 0.45, SAR, u(11), 0.9, "vurus", 0.7)
    kayit("sarı belirteç", ta, "anlamına (31)")

    # ---------------- 6. Altyazı dilimleri ve görünürlük ----------------
    dil = Y.altyazi_dilimleri([8])
    parcalar = [{"id": "alt%d" % i, "metin": d[2]} for i, d in enumerate(dil)]
    s.altyazi_svg = Y.altyazi_svg(parcalar)

    def aktif(tg):
        k = -1
        for i, (t0, t1, _m) in enumerate(dil):
            if t0 - 0.05 <= tg < t1 + 0.35:
                k = i
        return k

    onc = -1
    for f in range(Z["kare"]):
        tg = Z["t_bas"] + f / 30.0
        k = aktif(tg)
        if k != onc:
            t_yerel = round(f / 30.0, 4)
            if onc >= 0:
                s.set("#alt%d" % onc, t_yerel, {"opacity": 0})
            if k >= 0:
                s.set("#alt%d" % k, t_yerel, {"opacity": 1})
            onc = k

    # ---------------- Asserts ----------------
    sol_sonlar = [
        u(228) + Y.genislik("Caveat", 700, "general", u(64)),
        u(228) + Y.genislik("Caveat", 700, "permanent", u(64)),
        u(228) + Y.genislik("Caveat", 700, "timetable", u(64)),
        u(228) + Y.genislik("Caveat", 700, "(future)", u(64)),
        u(294) + w_sim / 2,
        u(294) + w_pres_sol / 2,
        u(294) + w_v1 / 2,
    ]
    sag_baslar = [
        u(852) - Y.genislik("Caveat", 700, "right now", u(64)),
        u(852) - Y.genislik("Caveat", 700, "temporary", u(64)),
        u(852) - Y.genislik("Caveat", 700, "arrangement", u(64)),
        u(852) - Y.genislik("Caveat", 700, "(future)", u(64)),
        u(786) - w_pres_sag / 2,
        u(786) - w_cont / 2,
        u(786) - w_am / 2,
        u(786) - w_ving / 2,
    ]
    assert max(sol_sonlar) <= 516, f"sol yazı sonu 516'yı aştı: {max(sol_sonlar):.1f}"
    assert min(sag_baslar) >= 564, f"sağ yazı başı 564'ten küçük: {min(sag_baslar):.1f}"
    assert mf_toplam <= 984, f"MEANING FIRST genişliği 984'ten büyük: {mf_toplam:.1f}"
    assert x0_mf >= 48 and x0_mf + mf_toplam <= 1032, "MEANING FIRST x sınırları dışında"

    for n_box, (bx0, bx1) in [("MONT", mont_box), ("TISORT", tisort_box), ("EV", ev_box),
                              ("BAVUL", bavul_box), ("TREN_D", tren_box), ("BILET_D", bilet_box)]:
        assert bx0 >= 48 and bx1 <= 1032, f"{n_box} x sınırları dışında: {bx0:.1f}-{bx1:.1f}"

    bas, son = Y.kontrol(s, Z["kare"], ilk=True)
    s.bas, s.son = bas, son
    s.rapor = olaylar
    kun = kunye_tam_svg()
    return s, kun


if __name__ == "__main__":
    s, kun = uret()
    logo = (u(48), u(48), u(96) * Y.LOGO_EN_BOY, u(96))
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, logo, ek=s.altyazi_svg))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev),
          "hareket %.2f-%.2f sn" % (s.bas, s.son))
    for ad, t, soz in s.rapor:
        print("  %6.2f sn  kare %3d  %-30s %s" % (t, round(t * 30), soz, ad))

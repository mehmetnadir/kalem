"""Sahne 07 Kural kartı (02-04 YDT temel, HyperFrames, 1920x1080; cümle 8).
BRIEF §3 No 7: `tanim` iki sütun (slayt 3 düzeni), 3 satır ses sırasıyla kademeli; her satır hücresi kalem çizgisiyle
örneğin küçük ikonuna bağlanır (mont/tişört, ev/bavul, tren/bilet); "anlamına bak" derken MEANING FIRST sarı belirteç.
Sütun başlıkları (SIMPLE PRESENT / PRESENT CONTINUOUS + kalıp) söylendiği anda gelir: "Soldakiler geniş zaman,
sağdakiler şimdiki zaman" satırlardan sonradır (önce anlam, sonra ad).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn; i = cümle içi sıra).
Yerel sn = küresel - t_bas. Ölçüler mantıksal px (yatay 1920 tabanı) -> u(); sabit px yok."""
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
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text()) if w["cumle"] == 8]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]

# ---- yerleşim (mantıksal px) ----
CER = (u(160), u(150), u(1600), u(680))     # tablo çerçevesi x, y, w, h (alt kenar 830)
ORTA = u(960)                               # sütun ayracı
SOL_X, SAG_X = u(416), u(1504)              # sol sütun yazı başı, sağ sütun yazı sonu (960 ± 544, ayna)
BAS_Y, KAL_Y = u(224), u(280)               # başlık ve kalıp tabanı
AYRAC_Y = u(316)                            # başlık satırı alt çizgisi
SATIR_H = (CER[1] + CER[3] - AYRAC_Y) / 3   # 3 satır
BF, KF, SF, GF = u(46), u(36), u(54), u(40)  # başlık (Fredoka), kalıp (Lexend), satır (Fredoka), "(future)" (Caveat)
CIZ_BOSLUK, CIZ_UZ = u(22), u(48)           # yazı ile bağ çizgisi arası, bağ çizgisi uzunluğu
IKON_ARA = u(16)                            # bağ çizgisi ile ikon arası
IKON_BOY, IKON_EN = u(92), u(140)           # ikon kutusu en çok yükseklik / genişlik
MF_BOY, MF_Y = u(68), u(925)                # MEANING FIRST (Fredoka 700), taban
VURUS = 0.22                                # kinetik sözcük (stil §4: 0,18-0,22 sn, back.out(1.6))


def T(i, bas):
    """Cümle 8, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    assert w["sozcuk"].lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, w["sozcuk"], bas)
    return w["t0"]


def satir_orta(k):
    return AYRAC_Y + SATIR_H * (k + 0.5)


# ---- ikonlar (örnek sahnelerinin çizimleri; ızgara birimi, parça: n = nokta dizisi, egri, kapali, ince) ----
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


TREN = [  # sahne 05 trenParcalari sadeleştirmesi (yandan, sağa bakar)
    _kutu(200, 55, 170, 75), _kutu(200, 10, 75, 45), _kutu(320, 22, 26, 33, True),
    {"n": [(370, 95), (398, 130), (370, 130)]}, _kutu(0, 45, 175, 85),
    {"n": [(175, 112), (200, 112)], "ince": True},
    _kutu(20, 60, 50, 30, True), _kutu(100, 60, 50, 30, True), _kutu(215, 20, 42, 25, True),
    {"daire": (40, 138, 17)}, {"daire": (135, 138, 17)}, {"daire": (240, 138, 17)}, {"daire": (335, 138, 17)},
    {"n": [(-10, 158), (420, 158)], "ince": True},
]


def _bilet():
    """Sahne 05 biletParcalari: iki yanında çentik, delik çizgisi, 3 baskı satırı (merkez 0,0)."""
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
        if p.get("egri") and len(q) >= 3:            # Catmull-Rom -> kübik
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


def uret():
    s = Y.Sahne(Z["t_bas"])
    S = s.S
    olaylar = []   # RAPOR için (olay, yerel sn, sözcük)

    def kayit(ad, t, soz):
        olaylar.append((ad, round(t, 2), soz))

    # ---------------- "Kural kartı" (0): çerçeve, sütun ayracı, başlık satırı çizgisi ----------------
    t0 = S(T(0, "Kural"))
    cx, cy, cw, ch = CER
    s.yol("cer", Y.el_kutu(cx, cy, cw, ch), t0, 0.7, KRE, u(4), 0.9, "cizgi", 0.6)
    s.yol("ayr", Y.el_cizgi(ORTA, cy + u(18), ORTA + u(2), cy + ch - u(18), 1.0), t0 + 0.3, 0.45, IKN, u(3), 0.9,
          "cizgi", 0.4)
    s.yol("bsc", Y.el_cizgi(cx + u(20), AYRAC_Y, cx + cw - u(20), AYRAC_Y, 1.5), t0 + 0.45, 0.45, IKN, u(3), 0.9,
          "cizgi", 0.4)
    kayit("çerçeve + ayraç + başlık çizgisi", t0, "Kural kartı (0)")
    # ---------------- "üç fark" (4, 5): iki satır çizgisi -> 3 boş satır ----------------
    for k, (i, bas) in enumerate(((4, "üç"), (5, "fark"))):
        y = AYRAC_Y + SATIR_H * (k + 1)
        s.yol("sc%d" % k, Y.el_cizgi(cx + u(20), y, cx + cw - u(20), y, 1.2), S(T(i, bas)), 0.3, IKN, u(2.5), 0.7,
              "cizgi", 0.35)
    kayit("2 satır çizgisi (3 satır)", S(T(4, "üç")), "üç fark (4, 5)")

    # ---------------- satırlar: hücre yazısı + bağ çizgisi + örnek ikonu ----------------
    def hucre(kim, k, sol, parcalar, ikon, egim=0.0):
        """parcalar: [(metin, aile, ağırlık, boy, renk, yerel t, süre)] tek taban çizgisi üstünde art arda.
        sol: sol sütun (yazı SOL_X'ten başlar) ya da sağ sütun (yazı SAG_X'te biter). Döner: ikon bitiş sn."""
        cyr = satir_orta(k)
        taban = cyr + SF * 0.35
        gen = [Y.genislik(a, g, m, b) for m, a, g, b, _, _, _ in parcalar]
        x = SOL_X if sol else SAG_X - sum(gen)
        assert (x + sum(gen) <= ORTA - u(30)) if sol else (x >= ORTA + u(30)), "%s ayraca değiyor" % kim
        for j, ((m, a, g, b, renk, t, d), w) in enumerate(zip(parcalar, gen)):
            s.yazi("%s%d" % (kim, j), x, taban, [(m, renk)], a, g, b, t, d, tur="tik" if j == 0 else None)
            x += w
        tb = parcalar[0][5] + 0.3                         # bağ çizgisi: ilk parça açılınca
        if sol:
            x1 = SOL_X - CIZ_BOSLUK
            x0 = x1 - CIZ_UZ
            yollar, _ = ikon_yollari(ikon, x0 - IKON_ARA, cyr, True, egim)
            bag = Y.el_cizgi(x1, cyr, x0, cyr + u(1), 0.6)
        else:
            x0 = SAG_X + CIZ_BOSLUK
            x1 = x0 + CIZ_UZ
            yollar, _ = ikon_yollari(ikon, x1 + IKON_ARA, cyr, False, egim)
            bag = Y.el_cizgi(x0, cyr, x1, cyr + u(1), 0.6)
        s.yol(kim + "b", bag, tb, 0.2, IKN, u(3), 0.9, "cizgi", 0.35)
        ti0 = tb + 0.15
        ti1 = ti0 + min(0.75, 0.25 + 0.06 * len(yollar))
        zam = Y.cizgi_zamanlari([y[1] for y in yollar], ti0, ti1)
        for n, ((d, _uz, ince), (b, du)) in enumerate(zip(yollar, zam)):
            s.yol("%si%d" % (kim, n), d, b, du, IKN if ince else KRE, u(3) if ince else u(4), 1.0,
                  "cizgi" if n < 2 else None, 0.4)
        return ti1

    F = ("Fredoka", 700, SF, KRE)
    G = ("Caveat", 700, GF, IKN)

    def p(m, stil, t, d):
        return (m,) + stil + (t, d)

    satirlar = (
        # (kimlik, satır, sol mu, parçalar, ikon, eğim, sözcük notu)
        ("ag", 0, True, [p("general", F, S(T(7, "Genel")), 0.35)], MONT, 0.0, "Genel (7)"),
        ("an", 0, False, [p("right now", F, S(T(10, "konuşma")), 0.4)], TISORT, 0.0, "konuşma anı (10)"),
        ("bk", 1, True, [p("permanent", F, S(T(12, "Kalıcı")), 0.4)], EV, 0.0, "Kalıcı (12)"),
        ("bg", 1, False, [p("temporary", F, S(T(15, "geçici")), 0.4)], BAVUL, 0.0, "geçici (15)"),
        ("ct", 2, True, [p("timetable", F, S(T(17, "Tarifeli")), 0.4),
                         p(" (future)", G, S(T(18, "gelecek")), 0.35)], TREN, 0.0, "Tarifeli (17) · gelecek (18)"),
        ("cp", 2, False, [p("arrangement", F, S(T(20, "planlanmış")), 0.45),
                          p(" (future)", G, S(T(21, "gelecek")), 0.35)], BILET, -0.06,
         "planlanmış (20) · gelecek (21)"),
    )
    for kim, k, sol, parcalar, ikon, egim, notu in satirlar:
        bit = hucre(kim, k, sol, parcalar, ikon, egim)
        ad = "satır %d %s: %s + bağ + ikon (ikon biter %.2f)" % (
            k + 1, "sol" if sol else "sağ", "".join(q[0] for q in parcalar), bit)
        kayit(ad, parcalar[0][5], notu)

    # ---------------- sütun başlıkları: "Soldakiler geniş zaman, sağdakiler şimdiki zaman" ----------------
    def baslik(kim, sol, metin, aile, agr, boy, renk, y, t, d):
        x = SOL_X if sol else SAG_X
        w = Y.genislik(aile, agr, metin, boy)
        assert (x + w <= ORTA - u(30)) if sol else (x - w >= ORTA + u(30)), "%s ayraca değiyor" % kim
        s.yazi(kim, x, y, [(metin, renk)], aile, agr, boy, t, d, anchor="start" if sol else "end", tur="tik", guc=0.5)

    basliklar = (
        ("hs", True, "SIMPLE PRESENT", "Fredoka", 700, BF, KRE, BAS_Y, 22, "Soldakiler", 0.45),
        ("ks", True, "V1 / V-s", "Lexend", 500, KF, IKN, KAL_Y, 23, "geniş", 0.3),
        ("hc", False, "PRESENT CONTINUOUS", "Fredoka", 700, BF, KRE, BAS_Y, 25, "sağdakiler", 0.5),
        ("kc", False, "am / is / are + V-ing", "Lexend", 500, KF, IKN, KAL_Y, 26, "şimdiki", 0.45),
    )
    for kim, sol, metin, aile, agr, boy, renk, y, i, bas, d in basliklar:
        t = S(T(i, bas))
        baslik(kim, sol, metin, aile, agr, boy, renk, y, t, d)
        kayit(metin, t, "%s (%d)" % (SOZ[i]["sozcuk"], i))

    # ---------------- MEANING FIRST: "Seçmeden önce cümlenin anlamına bak." ----------------
    wm = Y.genislik("Fredoka", 700, "MEANING ", MF_BOY)
    wf = Y.genislik("Fredoka", 700, "FIRST", MF_BOY)
    x0 = ORTA - (wm + wf) / 2
    for kim, m, x, w, i, bas in (("mfa", "MEANING", x0, wm, 28, "Seçmeden"), ("mfb", "FIRST", x0 + wm, wf, 29, "önce")):
        s.svg.append('<g id="%s" style="opacity:0"><text x="%.2f" y="%.2f" font-family="Fredoka" font-weight="700" '
                     'font-size="%.1f" fill="%s" xml:space="preserve">%s</text></g>' % (kim, x, MF_Y, MF_BOY, KRE, m))
        t = S(T(i, bas))
        s.fromto("#" + kim, t, {"opacity": 0, "y": u(34), "scale": 0.86,
                                "svgOrigin": "%.1f %.1f" % (x + w / 2, MF_Y)},
                 {"opacity": 1, "y": 0, "scale": 1, "duration": VURUS, "ease": "back.out(1.6)"})
        s.olay(t, "tik", 0.55)
        kayit(m + " (kinetik)", t, "%s (%d)" % (SOZ[i]["sozcuk"], i))
    ta = S(T(31, "anlamına"))
    s.yol("mfc", Y.el_cizgi(x0 - u(6), MF_Y + u(16), x0 + wm + wf + u(6), MF_Y + u(15), 1.0), ta, 0.45, SAR, u(10),
          0.9, "cizgi", 0.6)
    s.olay(ta, "vurus", 0.7)
    kayit("sarı belirteç (altı çizgi) MEANING FIRST", ta, "anlamına (31)")
    bas, son = Y.kontrol(s, Z["kare"])
    return s, Y.kunye_svg("Rule", 2), olaylar, (bas, son)


if __name__ == "__main__":
    s, kun, olaylar, (bas, son) = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (u(56), u(1002), u(34) * Y.LOGO_EN_BOY, u(34))))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "hareket %.2f-%.2f sn" % (bas, son))
    for ad, t, soz in olaylar:
        print("  %6.2f sn  kare %3d  %-30s %s" % (t, round(t * 30), soz, ad))

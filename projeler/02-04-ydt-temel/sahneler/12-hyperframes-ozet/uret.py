"""Sahne 12 Ara özet (02-04 YDT temel, HyperFrames, 1920x1080; cümle 14).
BRIEF §3 No 12: `ozet` 3 madde kademeli, her madde kural kartının (sahne 07) karşılığına ince kalem çizgisiyle bağlanır;
bölüm perdesi yok, sonda geçiş çizgisi. Ekran metni (senaryo-taslak §cümle 14):
  1. general · permanent · timetable → V1 / V-s
  2. right now · temporary · arrangement → am / is / are + V-ing
  3. time word · Turkish -yor → clue · MEANING → decision
Sol: madde bantları (sahne 02-03/12 dili: kalemle bant, sarı belirteç, kalem oku). Sağ: kural kartının küçük kartları
(1: SIMPLE PRESENT sütunu, 2: PRESENT CONTINUOUS sütunu, 3: MEANING FIRST satırı); sütun kartında sahne 07'nin satır
ikonları (mont/ev/tren, tişört/bavul/bilet) ilgili sözcük söylenince çizilir. Kalıp hapı: vurgu dolgusu + zemin
renginde yazı (açık temada okunur kontrast). Zaman tek kaynak: ../../zaman.json + ../../ortak/anlatim/sozcukler.json
(küresel sn). Ölçüler mantıksal px (yatay 1920 tabanı) -> u(); sabit px yok."""
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
HAP_YAZI = R["zemin"]          # hap üstü yazı: hf_tema text[fill=zemin] -> --pilMetin (iki temada koyu)

# ---- yerleşim (mantıksal px) ----
BX, BW = u(96), u(880)                       # madde bandı sol kenar, genişlik (sağ kenar 976)
IX = u(140)                                  # bant içi yazı başı
IT = u(48)                                   # madde yazısı (Fredoka 700)
AU, BO = u(84), u(24)                        # kalem oku uzunluğu, ok çevresi boşluk
BANT = ((u(180), u(200)), (u(420), u(200)), (u(660), u(200)))   # (y, yükseklik): madde 1, 2, 3
SA, SB = u(82), u(160)                       # bant içi satır a / b tabanı (bant üstünden)
HP, HY = u(14), 1.06                         # hap yatay iç boşluğu, hap yüksekliği (× yazı boyu)
CX, CW = u(1150), u(680)                     # küçük kart sol kenar, genişlik (sağ kenar 1830)
KH = (u(190), u(190), u(110))                # küçük kart yükseklikleri (merkez = bant merkezi)
KF, KF3 = u(34), u(40)                       # kart başlığı (Fredoka 700): sütun kartı, MEANING FIRST
IKON_EN, IKON_BOY, IKON_ARA = u(150), u(80), u(60)
GECIS_Y = u(924)                             # geçiş çizgisi

# ---- ikonlar: sahne 07 (kural kartı) ile aynı ızgara verisi ----
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
    return out


def T(i, bas):
    """Cümle 14, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    assert w["sozcuk"].lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, w["sozcuk"], bas)
    return w["t0"]


def gen(m, b=IT):
    return Y.genislik("Fredoka", 700, m, b)


def bant_orta(k):
    return BANT[k][0] + BANT[k][1] / 2


def uret():
    s = Y.Sahne(Z["t_bas"])
    L = s.S
    olaylar = []   # RAPOR: (olay, küresel sn, sözcük)

    def kayit(ad, t, soz):
        olaylar.append((ad, round(t, 2), soz))

    def parca(kim, x, y, m, t, renk=KRE, d=0.35, tur="tik"):
        s.yazi(kim, x, y, [(m, renk)], "Fredoka", 700, IT, L(t), d, tur=tur, guc=0.5)
        return x + gen(m)

    def belirtec(kim, x0, x1, y, t):
        s.yol(kim, Y.el_cizgi(x0 - u(4), y + u(16), x1 + u(4), y + u(15), 1), L(t), 0.4, SAR, u(9), 0.85,
              "cizgi", 0.5)

    def ok(kim, x, y, t, d=0.3):
        s.yol(kim, Y.el_ok(x, y - u(15), x + AU, y - u(15), 2.0), L(t), d, KRE, u(6), 0.9, "cizgi", 0.5)

    def hap(kim, x, y, m, t, d=0.35):
        """Kalıp hapı: vurgu dolgulu yuvarlak kutu + zemin renginde yazı; soldan açılan kırpma. Döner: sağ kenar."""
        w = gen(m)
        rx, ry, rw, rh = x - HP, y - IT * 0.80, w + 2 * HP, IT * HY
        s.defs.append('<clipPath id="c_%s"><rect id="r_%s" x="%.1f" y="%.1f" width="0" height="%.1f"/></clipPath>'
                      % (kim, kim, rx - u(4), ry - u(4), rh + u(8)))
        s.svg.append('<g id="%s" clip-path="url(#c_%s)"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" '
                     'rx="%.1f" fill="%s"/><text x="%.2f" y="%.2f" fill="%s" font-family="Fredoka" font-weight="700" '
                     'font-size="%s" xml:space="preserve">%s</text></g>'
                     % (kim, kim, rx, ry, rw, rh, u(12), SAR, x, y, HAP_YAZI, IT, m))
        s.cmd.append({"m": "rev", "id": "r_" + kim, "t": round(L(t), 4), "d": d, "w": round(rw + u(8), 1)})
        s.olay(L(t), "tik", 0.55)
        return rx + rw

    def kart(k, t, baslik, ikonlar=()):
        """Bant -> küçük kart ince kalem çizgisi, kart çerçevesi, başlık; ikonlar: [(parcalar, t)]."""
        cy, h = bant_orta(k), KH[k]
        y0 = cy - h / 2
        s.yol("kb%d" % k, Y.el_ok(BX + BW + u(8), cy, CX - u(14), cy + u(1), 1.5), L(t), 0.35, SAR, u(4), 0.9,
              "cizgi", 0.45)
        s.yol("kc%d" % k, Y.el_kutu(CX, y0, CW, h), L(t) + 0.2, 0.5, IKN, u(3.2), 0.85, "cizgi", 0.4)
        boy = KF3 if k == 2 else KF
        taban = y0 + (u(68) if k == 2 else u(52))
        assert gen(baslik, boy) <= CW - u(56), (baslik, gen(baslik, boy))
        s.yazi("kt%d" % k, CX + u(28), taban, [(baslik, KRE)], "Fredoka", 700, boy, L(t) + 0.3, 0.4, tur="tik",
               guc=0.4)
        alan = len(ikonlar) * IKON_EN + (len(ikonlar) - 1) * IKON_ARA
        for n, (parcalar, ti) in enumerate(ikonlar):
            mx = CX + (CW - alan) / 2 + IKON_EN / 2 + n * (IKON_EN + IKON_ARA)
            yollar = ikon_yollari(parcalar, mx, y0 + u(128))
            t0 = L(ti)
            t1 = t0 + min(0.6, 0.25 + 0.05 * len(yollar))
            for j, ((d, _uz, ince), (b, du)) in enumerate(zip(yollar, Y.cizgi_zamanlari([q[1] for q in yollar],
                                                                                        t0, t1))):
                s.yol("ki%d_%d_%d" % (k, n, j), d, b, du, IKN if ince else KRE, u(2.6) if ince else u(3.4), 1.0,
                      "cizgi" if j < 2 else None, 0.4)
        return taban, boy

    sp, dot = gen(" "), gen("· ")
    sinir = BX + BW - u(30)

    # ---- "Özet." (0): üç madde bandı (soluk) ----
    t0 = T(0, "Özet")
    for i, (y, h) in enumerate(BANT):
        s.yol("bn%d" % i, Y.el_kutu(BX, y, BW, h), L(t0) + 0.2 * i, 0.55, IKN, u(3.6), 0.8, "cizgi",
              0.5 if i == 0 else 0.4)
    kayit("3 madde bandı (soluk)", t0, "Özet. (0)")

    # ---- madde 1: general · permanent · timetable -> V1 / V-s ----
    ya, yb = BANT[0][0] + SA, BANT[0][0] + SB
    tg, tk, tt, tz = T(1, "Genel"), T(3, "kalıcı"), T(6, "tarifeli"), T(8, "geniş")
    kart(0, tg, "SIMPLE PRESENT", ((MONT, T(2, "durum")), (EV, tk + 0.2), (TREN, tt + 0.2)))
    kayit("ince çizgi -> SIMPLE PRESENT kartı (çerçeve + başlık)", tg, "Genel (1)")
    xe = parca("m1a", IX, ya, "general", tg)
    belirtec("b1a", IX, xe, ya, tg + 0.1)
    kayit("general + belirteç", tg, "Genel (1)")
    kayit("mont ikonu (kartta)", T(2, "durum"), "durum, (2)")
    x = xe + sp
    xe = parca("m1b", x, ya, "· permanent", tk, d=0.4)
    belirtec("b1b", x + dot, xe, ya, tk + 0.1)
    kayit("· permanent + belirteç; ev ikonu", tk, "kalıcı (3)")
    x = xe + sp
    xe = parca("m1c", x, ya, "· timetable", tt, d=0.4)
    belirtec("b1c", x + dot, xe, ya, tt + 0.1)
    kayit("· timetable + belirteç; tren ikonu", tt, "tarifeli (6)")
    w1a = xe
    ok("o1", IX, yb, tz)
    w1b = hap("h1", IX + AU + BO, yb, "V1 / V-s", tz + 0.14)
    kayit("kalem oku + hap V1 / V-s", tz, "geniş (8)")

    # ---- madde 2: right now · temporary · arrangement -> am / is / are + V-ing ----
    ya, yb = BANT[1][0] + SA, BANT[1][0] + SB
    tc, tg2, tp, ts = T(10, "Konuşma"), T(12, "geçici"), T(15, "planlanmış"), T(17, "şimdiki")
    kart(1, tc, "PRESENT CONTINUOUS", ((TISORT, T(11, "anı")), (BAVUL, tg2 + 0.2), (BILET, tp + 0.2)))
    kayit("ince çizgi -> PRESENT CONTINUOUS kartı (çerçeve + başlık)", tc, "Konuşma (10)")
    xe = parca("m2a", IX, ya, "right now", tc, d=0.4)
    belirtec("b2a", IX, xe, ya, tc + 0.1)
    kayit("right now + belirteç", tc, "Konuşma (10)")
    kayit("tişört ikonu (kartta)", T(11, "anı"), "anı, (11)")
    x = xe + sp
    xe = parca("m2b", x, ya, "· temporary", tg2, d=0.4)
    belirtec("b2b", x + dot, xe, ya, tg2 + 0.1)
    kayit("· temporary + belirteç; bavul ikonu", tg2, "geçici (12)")
    x = xe + sp
    xe = parca("m2c", x, ya, "· arrangement", tp, d=0.45)
    belirtec("b2c", x + dot, xe, ya, tp + 0.1)
    kayit("· arrangement + belirteç; bilet ikonu", tp, "planlanmış (15)")
    w2a = xe
    ok("o2", IX, yb, ts)
    w2b = hap("h2", IX + AU + BO, yb, "am / is / are + V-ing", ts + 0.14, d=0.5)
    kayit("kalem oku + hap am / is / are + V-ing", ts, "şimdiki (17)")

    # ---- madde 3: time word · Turkish -yor -> clue · MEANING -> decision ----
    ya, yb = BANT[2][0] + SA, BANT[2][0] + SB
    tw, tr, ti, tkr, ta, tv = (T(19, "Zaman"), T(22, "Türkçe"), T(24, "ipucu"), T(26, "Kararı"), T(27, "anlam"),
                               T(28, "verir"))
    xe = parca("m3a", IX, ya, "time word", tw, d=0.4)
    belirtec("b3a", IX, xe, ya, tw + 0.1)
    kayit("time word + belirteç", tw, "Zaman (19)")
    x = xe + sp
    xe = parca("m3b", x, ya, "· Turkish -yor", tr, d=0.45)
    belirtec("b3b", x + dot, xe, ya, tr + 0.1)
    kayit("· Turkish -yor + belirteç", tr, "Türkçe (22)")
    ok("o3", xe + BO, ya, ti, d=0.25)
    w3a = hap("h3", xe + BO + AU + BO, ya, "clue", ti + 0.12, d=0.3)
    kayit("kalem oku + hap clue", ti, "ipucu (24)")
    kt, kb = kart(2, tkr, "MEANING FIRST")
    kayit("ince çizgi -> MEANING FIRST kartı (çerçeve + başlık)", tkr, "Kararı (26)")
    xm = CX + u(28)
    s.yol("kmf", Y.el_cizgi(xm - u(4), kt + u(14), xm + gen("MEANING FIRST", kb) + u(4), kt + u(13), 1),
          L(ta) + 0.05, 0.4, SAR, u(8), 0.85, "cizgi", 0.5)
    xe = parca("m3c", IX, yb, "MEANING", ta, d=0.35)
    kayit("MEANING (bantta); kartta MEANING FIRST sarı belirteç", ta, "anlam (27)")
    ok("o4", xe + BO, yb, tv, d=0.25)
    w3b = hap("h4", xe + BO + AU + BO, yb, "decision", tv + 0.1, d=0.3)
    kayit("kalem oku + hap decision", tv, "verir. (28)")
    for n, ex in (("1a", w1a), ("1b", w1b), ("2a", w2a), ("2b", w2b), ("3a", w3a), ("3b", w3b)):
        assert ex <= sinir, "madde %s banda taştı: %.0f > %.0f" % (n, ex, sinir)

    # ---- geçiş çizgisi (perde yok): son sözcük 'verir.' ----
    s.yol("gc", Y.el_cizgi(u(140), GECIS_Y, u(1780), GECIS_Y - u(2), 1), L(tv) + 0.02, 0.42, IKN, u(4), 0.8,
          "cizgi", 0.4)
    kayit("geçiş çizgisi", tv + 0.02, "verir. (28)")
    bas, son = Y.kontrol(s, Z["kare"])
    return s, Y.kunye_svg("Recap", -1), olaylar, (bas, son)


if __name__ == "__main__":
    s, kun, olaylar, (bas, son) = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (u(56), u(1002), u(34) * Y.LOGO_EN_BOY, u(34))))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "hareket %.2f-%.2f sn (yerel)" % (bas, son))
    for ad, t, soz in olaylar:
        yer = t - Z["t_bas"]
        print("  %7.2f sn  yerel %5.2f  kare %3d  %-16s %s" % (t, yer, round(yer * 30), soz, ad))

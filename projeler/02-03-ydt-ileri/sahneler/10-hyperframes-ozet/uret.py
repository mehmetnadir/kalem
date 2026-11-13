"""Sahne 10 Ara özet (02-03 YDT ileri, HyperFrames, 724 kare, t_bas 263,48; cümle 14).
`ozet`: 3 madde kademeli; her madde sağdaki küçük anahtar kartının (sahne 03 ile aynı görsel dil: anahtar, çerçeve,
sarı belirteç, kalem oku) kendi grubuna okla bağlanır. Zaman: ortak/anlatim/sozcukler.json (küresel sn) +
zamanlar.json. Yerel sn = t - t_bas."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
SOZ = [w for w in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == 14]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
LX = 140.0
BASLIK = 76
IT = 44                       # madde yazı boyu (Fredoka 700)
YI = (504, 680, 860)          # madde taban çizgileri
KX, KW = 1270.0, 560.0        # mini kart sol kenar, genişlik
KF = 32                       # mini kart yazı boyu
# mini kart grupları: (çerçeve y, yükseklik, satır taban çizgileri)
GRUP = ((372, 232, (428, 484, 580)), (640, 138, (690, 750)), (800, 76, (850,)))
OK_X0 = 1110                  # madde -> kart oku başlangıcı (maddeler bunun solunda biter)
ETK = (("NOW", 0, 0, 6), ("THESE DAYS / NOWADAYS", 0, 1, 13), ("USUALLY", 0, 2, 9),
       ("ARRANGEMENT", 1, 0, 26), ("TIMETABLE", 1, 1, 29), ("believe · have · recommend", 2, 0, 32))


def T(i):
    return SOZ[i]["t0"]


def uret():
    s = Y.Sahne(Z["t_bas"])
    L = s.S
    gen = lambda m, b=IT: Y.genislik("Fredoka", 700, m, b)  # noqa: E731
    kgen = lambda m: Y.genislik("Fredoka", 700, m, KF)  # noqa: E731

    # ---- mini anahtar kartı (264,40 "Özet."): anahtar + 3 soluk çerçeve + soluk satırlar ----
    t = T(0)
    s.yol("ka1", "M1362 270 A30 30 0 1 0 1302 270 A30 30 0 1 0 1362 270", L(t), 0.35, KRE, 4, 1, "cizgi", 0.5)
    s.yol("ka2", "M1362 270 L1470 270", L(t + 0.35), 0.2, KRE, 4, 1, "cizgi", 0.4)
    s.yol("ka3", "M1432 270 L1432 296 M1456 270 L1456 291", L(t + 0.55), 0.2, KRE, 4, 1, "cizgi", 0.4)
    for i, (gy, gh, _) in enumerate(GRUP):
        s.yol("gk%d" % i, Y.el_kutu(KX, gy, KW, gh), L(t + 0.3 + 0.18 * i), 0.5, IKN, 3.2, 0.75, "cizgi", 0.4)
    for k, (m, g, r, ti) in enumerate(ETK):
        assert kgen(m) <= KW - 48, (m, kgen(m))
        s.yazi("mk%d" % k, KX + 24, GRUP[g][2][r], [(m, IKN)], "Fredoka", 700, KF, L(t + 0.5 + 0.1 * k), 0.3,
               tur=None)
    # mini kartta söylenen satır sarı belirteç alır; "geçici ya da değişen" notu
    for k, (m, g, r, ti) in enumerate(ETK):
        y = GRUP[g][2][r]
        s.yol("mb%d" % k, Y.el_cizgi(KX + 18, y + 10, KX + 30 + kgen(m), y + 8, 1.5), L(T(ti)), 0.35, SAR, 9, 0.65,
              "cizgi", 0.4)
    s.yazi("mn1", KX + 24, 524, [("(temporary,", IKN)], "Caveat", 700, 34, L(T(18)), 0.45, tur="tik", guc=0.35)
    s.yazi("mn2", KX + 24 + Y.genislik("Caveat", 700, "(temporary, ", 34), 524, [("changing)", IKN)], "Caveat", 700,
           34, L(T(21)), 0.4, tur=None)
    # ---- başlık (265,29 "Signal first." / 266,73 "Then the verb.") ----
    for kim, m, pre, ti, d, y, renk in (("b1", "SIGNAL", "", 1, 0.4, 250, KRE), ("b2", "FIRST.", "SIGNAL ", 2, 0.5,
                                                                                 250, KRE),
                                        ("b3", "THEN", "", 3, 0.2, 340, KRE), ("b4", "THE", "THEN ", 4, 0.15, 340, KRE),
                                        ("b5", "VERB.", "THEN THE ", 5, 0.5, 340, SAR)):
        s.yazi(kim, LX + Y.genislik("Fredoka", 700, pre, BASLIK), y, [(m, renk)], "Fredoka", 700, BASLIK, L(T(ti)), d,
               tur="tik", guc=0.55)

    def ok(kim, x, y, t, uz):
        s.yol(kim, Y.el_ok(x, y - 16, x + uz, y - 16, 2.0), L(t), 0.3, KRE, 6, 0.9, "cizgi", 0.5)

    def parca(kim, x, y, m, t, d=0.3):
        s.yazi(kim, x, y, [(m, KRE)], "Fredoka", 700, IT, L(t), d, tur="tik", guc=0.5)
        return x + gen(m)

    def bagla(kim, i, t):
        """madde -> kart grubu oku (madde başlarken); grup çerçevesi sarıya döner."""
        gy, gh, _ = GRUP[i]
        s.yol(kim, Y.el_ok(OK_X0, YI[i] - 16, KX - 24, gy + gh / 2 - 6, 3.0), L(t), 0.45, SAR, 6, 0.9, "cizgi", 0.55)
        s.yol(kim + "k", Y.el_kutu(KX, gy, KW, gh), L(t + 0.3), 0.5, SAR, 4.5, 0.9, "cizgi", 0.4)

    AU, BO = 70, 20               # ok uzunluğu, ok çevresi boşluğu
    bit = []
    # ---- madde 1: NOW -> V-ing · USUALLY -> V1 / V-s ----
    bagla("bg0", 0, T(6))
    x = parca("i1a", LX, YI[0], "NOW", T(6))
    ok("i1o", x + BO, YI[0], T(7), AU)
    x = parca("i1b", x + BO + AU + BO, YI[0], "V-ing", T(8))
    x = parca("i1c", x + 40, YI[0], "USUALLY", T(9))
    ok("i1p", x + BO, YI[0], T(10), AU)
    x = parca("i1d", x + BO + AU + BO, YI[0], "V1 / V-s", T(11))
    bit.append(x)
    # ---- madde 2: ARRANGEMENT -> V-ing · TIMETABLE -> V1 / V-s ----
    bagla("bg1", 1, T(24))
    x = parca("i2a", LX, YI[1], "ARRANGEMENT", T(26))
    ok("i2o", x + BO, YI[1], T(27), AU)
    x = parca("i2b", x + BO + AU + BO, YI[1], "V-ing", T(27) + 0.3)
    bit.append(x)
    x = parca("i2c", LX, YI[1] + 62, "TIMETABLE", T(29))
    ok("i2p", x + BO, YI[1] + 62, T(30), AU)
    x = parca("i2d", x + BO + AU + BO, YI[1] + 62, "V1 / V-s", T(31))
    bit.append(x)
    # ---- madde 3: believe · have · recommend -> no -ing ----
    bagla("bg2", 2, T(32))
    x = parca("i3a", LX, YI[2], "believe", T(32))
    x = parca("i3b", x + gen(" "), YI[2], "· have", T(33))
    x = parca("i3c", x + gen(" "), YI[2], "· recommend", T(34))
    ok("i3o", x + BO, YI[2], T(35), AU)
    x = parca("i3d", x + BO + AU + BO, YI[2], "no -ing", T(35) + 0.2)
    bit.append(x)
    assert max(bit) <= OK_X0 - 10, bit
    kun = Y.kunye_svg("Recap", -1)
    return s, kun


if __name__ == "__main__":
    s, kun = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), kun, None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34)))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

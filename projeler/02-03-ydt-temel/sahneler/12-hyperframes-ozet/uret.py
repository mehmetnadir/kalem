"""Sahne 12 Ara özet (02-03 YDT temel, HyperFrames, 1920x1080; cümle 15).
`ozet` 3 madde kademeli: NOW · THESE DAYS / NOWADAYS → usually -ing (temporary, changing) · USUALLY / GENERAL → V1 ·
believe, have: no -ing. Sahne 07 (kural) ile aynı görsel dil: kalemle bant, sarı belirteç, kalem oku, soluk küçük kart.
Her madde sağdaki küçük kartına (kural kartı 07, tuzak kartı 10) okla bağlanır; kart çerçevesi söylenince sarıya döner.
Bölüm perdesi yok; sonda ince geçiş çizgisi. Zaman tek kaynak: ../../zaman.json + ../../ortak/anlatim/sozcukler.json."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text()) if w["cumle"] == 15]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]

# ---- yerleşim (px) ----
BX, BW = 96, 1060                 # madde bandı (sol kenar, genişlik; sağ kenar 1156)
IX = 140                          # bant içi yazı başı
IT = 48                           # madde yazısı (Fredoka 700)
AU, BO = 84, 24                   # ok uzunluğu, ok çevresi boşluğu
BANT = ((250, 200), (500, 120), (680, 120))     # (y, yükseklik): madde 1, 2, 3
BASE = {"1a": 330, "1b": 408, "2": 578, "3": 758}
CX, CW = 1260, 564                # küçük kart sol kenar, genişlik
CF, CL = 30, 40                   # kart yazı boyu, satır adımı
KC = (350, 560, 740)              # kart merkez y
KART = ((("NOW", "THESE DAYS · NOWADAYS · PLAN"), 128),
        (("USUALLY · GENERAL",), 88),
        (("TRAP", "We believe this situation", "is temporary."), 168))


def T(i):
    return SOZ[i]["t0"]


def gen(m, b=IT):
    return Y.genislik("Fredoka", 700, m, b)


def uret():
    s = Y.Sahne(Z["t_bas"])
    L = s.S

    def parca(kim, x, y, m, t, renk, boy=IT, d=0.35, tur="tik"):
        s.yazi(kim, x, y, [(m, renk)], "Fredoka", 700, boy, L(t), d, tur=tur, guc=0.5)
        return x + gen(m, boy)

    def belirtec(kim, x0, x1, y, t):
        s.yol(kim, Y.el_cizgi(x0 - 4, y + 13, x1 + 4, y + 12, 1), L(t), 0.4, SAR, 9, 0.85, "cizgi", 0.5)

    def ok(kim, x, y, t, uz=AU):
        s.yol(kim, Y.el_ok(x, y - 15, x + uz, y - 15, 2.0), L(t), 0.3, KRE, 6, 0.9, "cizgi", 0.5)

    t0 = T(0)
    # ---- madde bantları (soluk) + küçük kartlar (soluk) ----
    for i, (y, h) in enumerate(BANT):
        s.yol("bn%d" % i, Y.el_kutu(BX, y, BW, h), L(t0) + 0.2 * i, 0.55, IKN, 3.6, 0.8, "cizgi", 0.5 if i == 0 else 0.4)
    for k, (satirlar, h) in enumerate(KART):
        y0 = KC[k] - h / 2
        s.yol("gk%d" % k, Y.el_kutu(CX, y0, CW, h), L(t0) + 0.15 + 0.18 * k, 0.5, IKN, 3.2, 0.75, "cizgi", 0.35)
        for li, m in enumerate(satirlar):
            renk = SAR if (k == 2 and li == 0) else IKN
            assert gen(m, CF) <= CW - 40, (m, gen(m, CF))
            s.yazi("gt%d_%d" % (k, li), CX + 20, y0 + 28 + li * CL + 26, [(m, renk)], "Fredoka", 700, CF,
                   L(t0) + 0.45 + 0.1 * k, 0.35, tur=None)

    def bagla(k, t):
        """madde bandı -> küçük kart oku (madde başlarken); kart çerçevesi sarıya döner."""
        by = BANT[k][0] + BANT[k][1] / 2
        h = KART[k][1]
        s.yol("bg%d" % k, Y.el_ok(BX + BW + 6, by, CX - 14, KC[k], 3.0), L(t), 0.35, SAR, 6, 0.9, "cizgi", 0.5)
        s.yol("gh%d" % k, Y.el_kutu(CX, KC[k] - h / 2, CW, h), L(t) + 0.3, 0.5, SAR, 4.5, 0.9, "cizgi", 0.4)

    sp = gen(" ")
    dot = gen("· ")
    # ---- madde 1: NOW · THESE DAYS / NOWADAYS → usually -ing (temporary, changing) ----
    bagla(0, T(1))
    ya, yb = BASE["1a"], BASE["1b"]
    xe = parca("i1a", IX, ya, "NOW", T(1), KRE)
    belirtec("m1", IX, xe, ya, T(1) + 0.1)
    x2 = xe + sp
    xe = parca("i1b", x2, ya, "· THESE DAYS", T(2), KRE, IT, 0.4)
    belirtec("m2", x2 + dot, xe, ya, T(2) + 0.1)
    x3 = xe + sp
    xe = parca("i1c", x3, ya, "/ NOWADAYS", T(5), KRE, IT, 0.45)
    belirtec("m3", x3 + gen("/ "), xe, ya, T(5) + 0.1)
    w1 = xe
    ok("o1", IX, yb, T(6))
    xu = IX + AU + BO
    xe = parca("i1d", xu, yb, "usually -ing", T(6) + 0.14, SAR, IT, 0.5)
    s.yazi("n1", xe + 36, yb, [("(temporary,", IKN)], "Caveat", 700, 40, L(T(9)), 0.45, tur="tik", guc=0.35)
    wt = Y.genislik("Caveat", 700, "(temporary, ", 40)
    s.yazi("n2", xe + 36 + wt, yb, [("changing)", IKN)], "Caveat", 700, 40, L(T(12)), 0.4, tur=None)
    w1b = xe + 36 + wt + Y.genislik("Caveat", 700, "changing)", 40)
    # ---- madde 2: USUALLY / GENERAL → V1 ----
    bagla(1, T(14))
    y2 = BASE["2"]
    xe = parca("i2a", IX, y2, "USUALLY", T(14), KRE)
    belirtec("m4", IX, xe, y2, T(14) + 0.1)
    xg = xe + sp
    xe = parca("i2b", xg, y2, "/ GENERAL", T(16), KRE, IT, 0.4)
    belirtec("m5", xg + gen("/ "), xe, y2, T(16) + 0.1)
    ok("o2", xe + BO, y2, T(18))
    xe = parca("i2c", xe + BO + AU + BO, y2, "V1", T(18) + 0.14, SAR, IT, 0.3)
    w2 = xe
    # ---- madde 3: believe, have: no -ing ----
    bagla(2, T(20))
    y3 = BASE["3"]
    xe = parca("i3a", IX, y3, "believe,", T(20), KRE, IT, 0.45)
    xe = parca("i3b", xe + sp, y3, "have:", T(22), KRE, IT, 0.35)
    xe = parca("i3c", xe + sp + 8, y3, "no -ing", T(28), SAR, IT, 0.4)
    w3 = xe
    # küçük kartta believe sarı daire (söylendiği anda)
    bw0 = CX + 20 + gen("We ", CF)
    bw1 = gen("believe", CF)
    cy3 = KC[2] - KART[2][1] / 2 + 28 + 1 * CL + 26
    s.yol("gd", Y.el_cizgi(bw0 - 1, cy3 + 14, bw0 + bw1 + 1, cy3 + 13, 1), L(T(20)) + 0.3, 0.45, SAR, 5, 0.85,
          "cizgi", 0.45)   # halka yerine el altçizgisi (13.11 QA)
    for n, ex in (("1a", w1), ("1b", w1b), ("2", w2), ("3", w3)):
        assert ex <= BX + BW - 30, "madde %s banda taştı: %.0f" % (n, ex)
    # ---- geçiş çizgisi (perde yok): 'yok.' 241,84 ----
    s.yol("gc", Y.el_cizgi(140, 910, 1780, 908, 1), L(T(29)), 0.38, IKN, 4, 0.8, "cizgi", 0.4)
    Y.kontrol(s, Z["kare"])
    return s, Y.kunye_svg("Recap", -1)


if __name__ == "__main__":
    s, kun = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34)))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

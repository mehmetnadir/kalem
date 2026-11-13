"""Sahne 03 Karar anahtarı (02-03 YDT ileri, HyperFrames, 1008 kare, t_bas 15,39; cümle 3).
`tanim` kartı: 3 grup, ses sırasıyla kademeli. Zaman: ortak/anlatim/sozcukler.json (küresel sn) + zamanlar.json
(t_bas, kare). Yerel sn = t - t_bas. olay.py bu modülün Sahne nesnesini içe alır (tek kaynak)."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
SOZ = [w for w in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == 3]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
LX = 140.0                    # sol kenar
F = 60                        # etiket Fredoka boyu
HF = 56                       # hint Fredoka boyu
Y1A, Y1B, Y1C = 330, 440, 600  # sinyal satırları (taban çizgisi)
YOL2 = 660
Y2A, Y2B = 750, 850
KUTU3 = (LX, 888, 1130, 76)   # tuzak çerçevesi


def T(i):
    return SOZ[i]["t0"]


def uret():
    s = Y.Sahne(Z["t_bas"])
    L = s.S
    gen = lambda m, b=F: Y.genislik("Fredoka", 700, m, b)  # noqa: E731
    lab_max = gen("THESE DAYS / NOWADAYS")
    AX = LX + lab_max + 50        # ok başlangıcı (sinyal grubu)
    AX2 = LX + gen("ARRANGEMENT") + 50   # gelecek grubu oku
    HX = AX + 150                 # hint x

    def etiket(kim, x, y, m, t, d, renk=KRE):
        s.yazi(kim, x, y, [(m, renk)], "Fredoka", 700, F, L(t), d, tur="tik", guc=0.55)
        return gen(m)

    def belirtec(kim, x, y, w, t, d=0.35):
        s.yol(kim, Y.el_cizgi(x - 6, y + 16, x + w + 6, y + 12, 2.0), L(t), d, SAR, 13, 0.6, "cizgi", 0.5)

    def ok(kim, x, y, t, uz=110, d=0.3):
        s.yol(kim, Y.el_ok(x, y - 20, x + uz, y - 20, 2.0), L(t), d, KRE, 6, 0.9, "cizgi", 0.5)

    def hint(kim, x, y, deger, t, t2, boy=HF):
        a = s.yazi(kim + "a", x, y, [("hint: ", IKN)], "Fredoka", 700, boy, L(t), 0.25, tur=None)
        wa = Y.genislik("Fredoka", 700, "hint: ", boy)
        s.yazi(kim + "b", x + wa, y, [(deger, KRE)], "Fredoka", 700, boy, L(t2), 0.35, tur="tik", guc=0.5)
        return a

    # ---- anahtar çizimi (16,31 "Karar anahtarı"): kalemle, sol üst ----
    t = T(0)
    s.yol("ka1", "M232 200 A42 42 0 1 0 148 200 A42 42 0 1 0 232 200", L(t), 0.5, KRE, 5, 1, "cizgi", 0.6)
    s.yol("ka2", "M232 200 L372 200", L(t + 0.5), 0.3, KRE, 5, 1, "cizgi", 0.5)
    s.yol("ka3", "M330 200 L330 238 M360 200 L360 232", L(t + 0.8), 0.3, KRE, 5, 1, "cizgi", 0.5)
    s.yol("ka4", Y.el_daire(190, 200, 18, 18, 0.5), L(t + 1.05), 0.25, SAR, 5, 0.85, "parilti", 0.5)
    # ---- grup 1: sinyaller ----
    # NOW (17,68) -> V-ing (continuous 18,80)
    w = etiket("nw", LX, Y1A, "NOW", T(2), 0.3)
    belirtec("m_nw", LX, Y1A, w, T(2) + 0.05)
    ok("o_nw", AX, Y1A, T(6))
    hint("h_nw", HX, Y1A, "V-ing", T(6) + 0.1, T(6) + 0.4)
    # THESE DAYS / NOWADAYS (19,80 / 20,68) + (temporary, changing) -> V-ing (25,52)
    pa = "THESE DAYS / "
    etiket("td", LX, Y1B, "THESE DAYS /", T(7), 0.45)
    etiket("nd", LX + gen(pa), Y1B, "NOWADAYS", T(10), 0.5)
    belirtec("m_td", LX, Y1B, lab_max, T(10) + 0.05, 0.55)
    s.yazi("tc1", LX, Y1B + 68, [("(temporary,", IKN)], "Caveat", 700, 46, L(T(15)), 0.5, tur="tik", guc=0.4)
    s.yazi("tc2", LX + Y.genislik("Caveat", 700, "(temporary, ", 46), Y1B + 68, [("changing)", IKN)], "Caveat", 700, 46,
           L(T(17)), 0.45, tur=None)
    ok("o_td", AX, Y1B, T(25))
    hint("h_td", HX, Y1B, "V-ing", T(25) + 0.1, T(25) + 0.4)
    # USUALLY (26,64) -> V1 / V-s (27,60)
    w = etiket("us", LX, Y1C, "USUALLY", T(26), 0.4)
    belirtec("m_us", LX, Y1C, w, T(26) + 0.05)
    ok("o_us", AX, Y1C, T(30))
    hint("h_us", HX, Y1C, "V1 / V-s", T(30) + 0.1, T(31))
    # ---- ayraç (28,97 "Gelecekte") ----
    s.yol("ayr", Y.el_cizgi(LX, YOL2, 1500, YOL2 - 4, 3.0), L(T(32)), 0.55, IKN, 4, 0.8, "cizgi", 0.5)
    # ---- grup 2: gelecek ----
    w = etiket("ar", LX, Y2A, "ARRANGEMENT", T(37), 0.55)
    belirtec("m_ar", LX, Y2A, w, T(37) + 0.05, 0.5)
    ok("o_ar", AX2, Y2A, T(40))
    s.yazi("v_ar", AX2 + 140, Y2A, [("V-ing", KRE)], "Fredoka", 700, HF, L(T(40) + 0.3), 0.35, tur="tik", guc=0.5)
    w = etiket("tt", LX, Y2B, "TIMETABLE", T(43), 0.5)
    belirtec("m_tt", LX, Y2B, w, T(43) + 0.05, 0.45)
    ok("o_tt", AX2, Y2B, T(46))
    s.yazi("v_tt", AX2 + 140, Y2B, [("V1 / V-s", KRE)], "Fredoka", 700, HF, L(T(47)), 0.4, tur="tik", guc=0.5)
    # kişi (37,38) ve nesne (39,22): kalemle çizilir
    s.figur("standing-3", "kz", 1250, 698, 186, L(T(50)), L(T(50)) + 1.5, 3.4)
    for i, d in enumerate(Y.tabler("clock")):
        s.yol("sa%d" % i, d, L(T(56)) + 0.12 * i, 0.6, KRE, 0.35, 1, "cizgi", 0.5,
              'transform="translate(1560 700) scale(7.5)"')
    # ---- grup 3: tuzak (soluk çerçeve; 41,31 -> 47,03) ----
    bx, by, bw, bh = KUTU3
    s.yol("tz_k", Y.el_kutu(bx, by, bw, bh), L(T(60)), 0.9, IKN, 3.2, 0.8, "cizgi", 0.45)
    pw = lambda m: Y.genislik("Fredoka", 700, m, 44)  # noqa: E731
    x = bx + 30
    yy = by + 55
    for i, (m, ti) in enumerate((("believe", 64), ("have", 65), ("recommend", 67))):
        pre = "· " if i else ""
        s.yazi("tz%d" % i, x, yy, [(pre + m, IKN)], "Fredoka", 700, 44, L(T(ti)), 0.3, tur="tik", guc=0.35)
        x += pw(pre + m + " ")
    s.yol("tz_o", Y.el_ok(x + 10, yy - 16, x + 100, yy - 16, 2.0), L(T(68)), 0.3, IKN, 5, 0.9, "cizgi", 0.4)
    s.yazi("tz_n", x + 120, yy, [("no -ing", IKN)], "Fredoka", 700, 44, L(T(68)) + 0.3, 0.35, tur="tik", guc=0.35)
    s.yazi("tz_e", bx + bw + 40, by + 60, [("trap — later", IKN)], "Caveat", 700, 42, L(T(71)), 0.5, tur="tik",
           guc=0.35)
    kun = Y.kunye_svg("Key", 1)
    return s, kun


if __name__ == "__main__":
    s, kun = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), kun, None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34)))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

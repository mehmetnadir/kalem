"""Sahne 09 ara özet (HyperFrames, 1920x1080): `ozet` beş madde kademeli + sıklık ölçeği (always 100 % -> never 0 %)
+ `every` ve tekrar sayısı kalıpları ayrı etiket + kapanış notu.
Zaman tek kaynak: ../../zaman.json + ../../ortak/anlatim/sozcukler.json (küresel sn; cümle 51–53). Yerel sn = küresel − t_bas."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_ALL = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
SOZ = {c: [w for w in _ALL if w["cumle"] == c] for c in (51, 52, 53)}
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]
FS = 56
RB = (222, 304, 386, 468, 550)       # madde tabanları
TX = 156                             # madde yazısı x
AX_Y = 740


def T(c, i):
    return SOZ[c][i]["t0"]


def uret():
    s = Y.Sahne(TB)
    S = s.S
    tt = lambda c, i: S(T(c, i))  # noqa: E731
    dizi = Y.dizi

    # ---------------- ozet: beş madde ----------------
    s.yazi("oz", 96, 150, [("Özetle.", SAR)], "Caveat", 700, 72, tt(51, 0), 0.6, tur="tik", guc=0.55)

    def madde(n, t):
        s.yol("mb%d" % n, Y.el_daire(116, RB[n] - 20, 15, 15, n * 0.7), t - 0.05, 0.3, SAR, 6, 0.9, "cizgi", 0.4)

    for n, (m, i) in enumerate((("rutin", 3), ("kalıcı durum", 4), ("genel gerçek", 7))):
        t = tt(51, i)
        madde(n, t)
        s.yazi("m%d" % n, TX, RB[n], [(m, KRE)], "Fredoka", 700, FS, t, 0.3, tur="tik", guc=0.5)
    madde(3, tt(52, 0))
    e3, _ = dizi(s, "r3", TX, RB[3], [
        {"m": "he", "t": tt(52, 0)}, {"m": " · she", "t": tt(52, 1)}, {"m": " · it", "t": tt(52, 2), "bos": 18},
        {"ok": 84, "t": tt(52, 3), "bos": 18}, {"kutu": True, "m": "s", "t": tt(52, 4)}], boy=FS)
    madde(4, tt(52, 6))
    e4, yer4 = dizi(s, "r4", TX, RB[4], [
        {"m": "don't / doesn't", "t": tt(52, 6)}, {"m": " · ", "t": tt(52, 7), "r": IKN},
        {"m": "Do / Does", "t": tt(52, 8)}], boy=FS)
    assert e4 < 1060, "madde 5 taştı %.0f" % e4
    s.yol("r4u", Y.el_cizgi(TX - 4, RB[4] + 18, e4 + 4, RB[4] + 15, 2), tt(52, 9), 0.7, SAR, 8, 0.9, "cizgi", 0.55)

    # ---------------- sıklık ölçeği (C53) ----------------
    s.yazi("st", 96, 640, [("sinyal sözcükler", IKN)], "Caveat", 700, 60, tt(53, 0), 1.2, tur="tik", guc=0.45)
    s.yol("ek", Y.el_kutu(96, 690, 250, 100), tt(53, 2) - 0.05, 0.4, IKN, 4, 1, "cizgi", 0.5)
    s.yazi("ev", 96 + 38, 762, [("every", KRE)], "Fredoka", 700, 56, tt(53, 2), 0.3, tur="tik", guc=0.55)
    s.yol("ax", Y.el_ok(420, AX_Y, 1800, AX_Y, 1), tt(53, 1), 0.9, KRE, 5, 1, "cizgi", 0.6)
    s.yazi("p1", 420, 702, [("100 %", IKN)], "Lexend", 500, 30, tt(53, 3), 0.3, tur=None)
    wp = Y.genislik("Lexend", 500, "0 %", 30)
    s.yazi("p0", 1800 - wp, 702, [("0 %", IKN)], "Lexend", 500, 30, tt(53, 7), 0.3, tur=None)
    for n, (m, i) in enumerate((("always", 3), ("usually", 4), ("often", 5), ("sometimes", 6), ("never", 7))):
        cx = (470, 790, 1110, 1430, 1750)[n]
        t = tt(53, i)
        w = Y.genislik("Fredoka", 700, m, 46)
        s.yol("dt%d" % n, Y.el_daire(cx, AX_Y, 13, 13, n * 0.9), t, 0.3, SAR, 7, 0.95, "tik", 0.5)
        s.yazi("sl%d" % n, cx - w / 2, 830, [(m, KRE)], "Fredoka", 700, 46, t, 0.3, tur=None)
    # tekrar sayısı kalıpları: ayrı etiket
    s.yazi("tl", 96, 925, [("tekrar sayısı:", IKN)], "Caveat", 700, 56, tt(53, 8), 1.4, tur="tik", guc=0.45)
    x = 96 + Y.genislik("Caveat", 700, "tekrar sayısı:", 56) + 36
    for n, (m, i) in enumerate((("once a week", 14), ("on Mondays", 17), ("in the mornings", 19))):
        w = Y.genislik("Fredoka", 700, m, 40)
        t = tt(53, i)
        s.yol("tkk%d" % n, Y.el_kutu(x, 880, w + 52, 70), t - 0.05, 0.35, IKN, 4, 1, "cizgi", 0.45)
        s.yazi("tkt%d" % n, x + 26, 927, [(m, KRE)], "Fredoka", 700, 40, t, 0.4, tur="tik", guc=0.45)
        x += w + 52 + 30
    assert x - 30 <= 1824, "kalıp çipleri taştı %.0f" % x
    # kapanış notu (sağ bölge)
    RXn = 1100
    s.yazi("n1", RXn, 262, [("önce geniş zamanı düşün", KRE)], "Caveat", 700, 64, tt(53, 24), 1.3, tur="tik", guc=0.5)
    wn = Y.genislik("Caveat", 700, "önce geniş zamanı düşün", 64)
    s.yol("n1u", Y.el_cizgi(RXn, 282, RXn + wn, 279, 2), tt(53, 27), 0.45, SAR, 7, 0.9, "cizgi", 0.5)
    s.yazi("n2", RXn, 382, [("kesin kural değil,", IKN)], "Caveat", 700, 64, tt(53, 28), 0.9, tur="tik", guc=0.45)
    s.yazi("n3", RXn, 470, [("ilk akla gelen zaman bu.", KRE)], "Caveat", 700, 64, tt(53, 31), 0.9, tur="tik", guc=0.5)
    assert RXn + Y.genislik("Caveat", 700, "ilk akla gelen zaman bu.", 64) < 1860
    return s, {"kun": Y.kunye_svg("Summary", "Summary", 3, 3)}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34)))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

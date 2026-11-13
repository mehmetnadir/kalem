"""Sahne 03 formül İLERİ (HyperFrames, 1920x1080): `tanim` FORM kartı iki aşamada.
Aşama 1 (cümle 5): iki geniş kart: `S + V` (özne, yalın fiil) ve `he · she · it → V + s` (s sarı kutu).
Aşama 2 (cümle 6): olumsuz / soru kartı, yardımcı fiiller sarı kutu (don't, doesn't, Do, Does) + sağda el notları.
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn). Yerel sn = küresel − t_bas.
Olay zamanı = ilgili sözcüğün t0'ı."""
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
SOZ = {c: [w for w in _ALL if w["cumle"] == c] for c in (5, 6)}
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]
SON = (Z["kare"] - 12) / 30          # içerik sonu (yerel sn); son 12 kare durgun

KX = 96
Y1, Y2, KH = 200, 560, 300           # iki kart: üst y, alt y, yükseklik


def kimlikler(s, bas):
    """s.svg[bas:] elemanlarının üst düzey id kümesi."""
    return {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}


def uret():
    s = Y.Sahne(TB)
    S = s.S
    tt = lambda c, i: S(SOZ[c][i]["t0"])  # noqa: E731
    dizi = Y.dizi
    gruplar = []

    def grup(ad, bas):
        gruplar.append((ad, kimlikler(s, bas)))

    def sol(ad, t, d=0.3):
        s.to("#" + ad, t, {"opacity": 0, "duration": d, "ease": "power1.in"})
        assert t + d <= SON + 1e-6, "solma içerik sonunu aştı " + ad

    # ================= aşama 1 (cümle 5): iki geniş kart =================
    g0 = len(s.svg)
    KW, KX5 = 1260, 330                        # iki kart ortalı (soldan 330 px)
    for n, y, t in ((0, Y1, tt(5, 0)), (1, Y2, tt(5, 7) - 0.1)):
        s.yol("a%d" % n, Y.el_kutu(KX5, y, KW, KH), t, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
    s.yazi("al0", KX5 + 40, Y1 + 56, [("FORM", IKN)], "Lexend", 500, 30, tt(5, 0) + 0.25, 0.3, tur="tik", guc=0.4)
    s.yazi("al1", KX5 + 40, Y2 + 56, [("EK", IKN)], "Lexend", 500, 30, tt(5, 7) + 0.1, 0.3, tur="tik", guc=0.4)
    B1 = 168
    e1, y1 = dizi(s, "f", KX5 + 60, Y1 + 222, [
        {"m": "S", "t": tt(5, 3), "tik": True}, {"m": " + ", "t": tt(5, 4)}, {"m": "V", "t": tt(5, 5), "tik": True}],
        boy=B1)
    assert e1 < KX5 + KW - 40, "kart 1 taştı %.0f" % e1
    s.yazi("fc0", y1[0][1], Y1 + 276, [("özne", IKN)], "Caveat", 700, 56, tt(5, 3) + 0.1, 0.4, tur=None)
    s.yazi("fc1", y1[2][1], Y1 + 276, [("yalın fiil", IKN)], "Caveat", 700, 56, tt(5, 5) + 0.1, 0.5, tur=None)
    B2 = 118
    e2, y2 = dizi(s, "h", KX5 + 60, Y2 + 205, [
        {"m": "he", "t": tt(5, 7), "tik": True}, {"m": " · she", "t": tt(5, 8)}, {"m": " · it", "t": tt(5, 9), "bos": 30},
        {"ok": 120, "t": tt(5, 10), "bos": 30}, {"m": "V", "t": tt(5, 11)}, {"m": " + ", "t": tt(5, 11) + 0.22},
        {"kutu": True, "m": "s", "t": tt(5, 12)}], boy=B2)
    assert e2 < KX5 + KW - 40, "kart 2 taştı %.0f" % e2
    grup("gA", g0)
    sol("gA", tt(6, 0) - 0.4)                  # "gelir." biter, 0,45 sn sonra cümle 6 başlar

    # ================= aşama 2 (cümle 6): olumsuz ve soru kartları =================
    g0 = len(s.svg)
    KW = 960
    FS = 92
    for n, (y, ad, t) in enumerate(((Y1, "OLUMSUZ", tt(6, 0)), (Y2, "SORU", tt(6, 2)))):
        s.yol("b%d" % n, Y.el_kutu(KX, y, KW, KH), t, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
        s.yazi("bl%d" % n, KX + 40, y + 56, [(ad, IKN)], "Lexend", 500, 30, t + 0.25, 0.3, tur="tik", guc=0.4)
    eA, _ = dizi(s, "p", KX + 50, Y1 + 215, [
        {"kutu": True, "m": "don't", "t": tt(6, 6), "bos": 16}, {"m": "/", "t": tt(6, 7) - 0.15, "bos": 16},
        {"kutu": True, "m": "doesn't", "t": tt(6, 7), "bos": 12}, {"m": " + ", "t": tt(6, 13)},
        {"m": "V", "t": tt(6, 14), "tik": True}], boy=FS)
    assert eA < KX + KW - 30, "olumsuz satırı taştı %.0f" % eA
    eB, _ = dizi(s, "q", KX + 50, Y2 + 215, [
        {"kutu": True, "m": "Do", "t": tt(6, 8), "bos": 16}, {"m": "/", "t": tt(6, 9) - 0.15, "bos": 16},
        {"kutu": True, "m": "Does", "t": tt(6, 9), "bos": 12}, {"m": " + ", "t": tt(6, 10)},
        {"m": "S", "t": tt(6, 10) + 0.1}, {"m": " + ", "t": tt(6, 13)}, {"m": "V", "t": tt(6, 14), "tik": True},
        {"m": " ?", "t": tt(6, 15), "r": SAR}], boy=FS)
    assert eB < KX + KW - 30, "soru satırı taştı %.0f" % eB
    # sağ bölge: el notları (söylenen sözcükler)
    RX, NB = 1130, 64
    e, _ = dizi(s, "n1", RX, 300, [{"m": "yük ", "t": tt(6, 3)}, {"m": "yardımcı ", "t": tt(6, 4)},
                                   {"m": "fiilde", "t": tt(6, 5), "r": SAR}], aile="Caveat", boy=NB)
    assert e < 1860, "not 1 taştı %.0f" % e
    e, _ = dizi(s, "n2", RX, 470, [{"m": "özneye ", "t": tt(6, 10), "r": SAR}, {"m": "göre", "t": tt(6, 11), "r": SAR}],
                aile="Caveat", boy=NB)
    assert e < 1860, "not 2 taştı %.0f" % e
    e, _ = dizi(s, "n3", RX, 640, [{"m": "asıl ", "t": tt(6, 13)}, {"m": "fiil", "t": tt(6, 14)}], aile="Caveat", boy=NB)
    e, yn = dizi(s, "n4", RX, 720, [{"m": "yalın ", "t": tt(6, 15)}, {"m": "kalır", "t": tt(6, 16)}], aile="Caveat", boy=NB)
    assert e < 1860, "not 4 taştı %.0f" % e
    s.yol("n4u", Y.el_cizgi(RX, 742, e, 739, 2), tt(6, 16), 0.45, SAR, 7, 0.9, "cizgi", 0.55)
    assert tt(6, 16) + 0.45 <= SON, "son çizgi içerik sonunu aştı"
    grup("gB", g0)
    return s, {"kun": Y.kunye_svg("Rule", "Rule", 1, 1), "gruplar": gruplar}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

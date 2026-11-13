"""Sahne 13 ara özet İLERİ (HyperFrames, 1920x1080): `ozet` satırları kademeli, dört kutu yanar, üç kutu ok ile
bağlanır, `kinetik_baslik` "Türkçeye değil, çerçeveye bak." (çerçeve sarı).
Cümle 47: tekrar · kalıcı · genel gerçek. Cümle 48: Özet · Tabela · Tören · Tarife (dört kutu yanar).
Cümle 49: çerçeve → özne → yardımcı fiil. Cümle 50: kinetik kod başlığı.
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn; cümle 47–50).
Olay zamanı = ilgili sözcüğün t0'ı. Yerel sn = küresel − t_bas."""
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
SOZ = {c: [w for w in _ALL if w["cumle"] == c] for c in (47, 48, 49, 50)}
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]
SON = (Z["kare"] - 12) / 30          # içerik sonu (yerel sn); son 12 kare durgun
SX, SW, SG = 136, 380, 40            # dört kutu: x, genişlik, aralık
BY, BH = 450, 230                    # kutu satırı: y, yükseklik


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

    # ================= C47–C48: özet + dört kutu =================
    g0 = len(s.svg)
    s.yazi("oz", 96, 160, [("Özet", SAR)], "Caveat", 700, 76, tt(47, 0), 0.6, tur="tik", guc=0.55)
    s.yol("mb", Y.el_daire(120, 244, 16, 16, 0.4), tt(47, 3) - 0.05, 0.3, SAR, 6, 0.9, "cizgi", 0.4)
    e, _ = dizi(s, "r", 156, 266, [
        {"m": "tekrar", "t": tt(47, 3), "tik": True}, {"m": " · ", "t": tt(47, 4) - 0.12, "r": IKN},
        {"m": "kalıcı", "t": tt(47, 4)}, {"m": " · ", "t": tt(47, 7) - 0.12, "r": IKN},
        {"m": "genel ", "t": tt(47, 7)}, {"m": "gerçek", "t": tt(47, 8)}], boy=64)
    assert e < 1700, "madde satırı taştı %.0f" % e
    e, _ = dizi(s, "d", 96, 390, [
        {"m": "dört ", "t": tt(48, 0)}, {"m": "çerçeve ", "t": tt(48, 1), "bos": 14},
        {"ok": 90, "t": tt(48, 2), "bos": 22}, {"m": "geniş ", "t": tt(48, 3), "r": SAR},
        {"m": "zaman", "t": tt(48, 4), "r": SAR}], aile="Caveat", boy=70)
    assert e < 1700, "dört çerçeve notu taştı %.0f" % e
    for i, (ad, th) in enumerate((("Özet", tt(48, 6)), ("Tabela", tt(48, 7)), ("Tören", tt(48, 8)),
                                  ("Tarife", tt(48, 9)))):
        x = SX + i * (SW + SG)
        s.yol("bo%d" % i, Y.el_kutu(x, BY, SW, BH), tt(48, 1) + i * 0.15, 0.45, IKN, 4, 1, "cizgi", 0.45)
        s.yol("by%d" % i, Y.el_kutu(x, BY, SW, BH), th, 0.5, SAR, 7, 0.95, "cizgi", 0.6)
        w = Y.genislik("Fredoka", 700, ad, 64)
        assert w < SW - 40, "kutu başlığı taştı " + ad
        s.yazi("bh%d" % i, x + (SW - w) / 2, BY + 138, [(ad, KRE)], "Fredoka", 700, 64, th + 0.1, 0.3, tur="tik", guc=0.5)
    e, _ = dizi(s, "t", 96, 800, [
        {"m": "Türkçesi ", "t": tt(48, 10), "r": IKN}, {"m": "şimdiki", "t": tt(48, 11)},
        {"m": " · geçmiş", "t": tt(48, 12)}, {"m": " · gelecek", "t": tt(48, 15)}], aile="Caveat", boy=70)
    assert e < 1700, "Türkçesi notu taştı %.0f" % e
    grup("gP", g0)
    sol("gP", tt(49, 0) - 0.4)

    # ================= C49: çerçeve → özne → yardımcı fiil =================
    g0 = len(s.svg)
    dizi(s, "sl", 96, 330, [{"m": "Sınavda ", "t": tt(49, 0)}, {"m": "sırayla ", "t": tt(49, 1)},
                            {"m": "bak", "t": tt(49, 2), "r": SAR}], aile="Caveat", boy=76)
    ADIM = (("çerçeve", tt(49, 3), 6), ("özne", tt(49, 4), 6), ("yardımcı fiil", tt(49, 5), 7))
    GAP, CY, CH, FB = 150, 440, 200, 64
    gen = [Y.genislik("Fredoka", 700, m, FB) + 100 for m, _, _ in ADIM]
    x = 136.0
    for n, ((m, t, _), w) in enumerate(zip(ADIM, gen)):
        s.yol("cb%d" % n, Y.el_kutu(x, CY, w, CH), t - 0.05, 0.45, KRE, 4.5, 1, "cizgi", 0.65)
        s.yazi("cn%d" % n, x + 24, CY + 52, [(str(n + 1), SAR)], "Lexend", 700, 30, t + 0.1, 0.2, tur=None)
        s.yazi("ct%d" % n, x + 50, CY + 128, [(m, KRE)], "Fredoka", 700, FB, t + 0.1, 0.35, tur="tik", guc=0.5)
        if n < 2:
            s.yol("ca%d" % n, Y.el_ok(x + w + 22, CY + CH / 2, x + w + GAP - 22, CY + CH / 2, 1),
                  ADIM[n + 1][1] - 0.3, 0.3, SAR, 6, 1, "cizgi", 0.5)
        x += w + GAP
    assert x - GAP < 1824, "adım zinciri taştı %.0f" % (x - GAP)
    grup("gC", g0)
    sol("gC", tt(50, 0) - 0.35)

    # ================= C50: kinetik kod başlığı =================
    s.yazi("kd", 96, 290, [("Kod:", SAR)], "Caveat", 700, 80, tt(50, 0), 0.5, tur="tik", guc=0.55)
    e, y1 = dizi(s, "k1", 96, 520, [{"m": "Türkçeye ", "t": tt(50, 1), "r": IKN}, {"m": "değil,", "t": tt(50, 2), "r": IKN}],
                 boy=124)
    assert e < 1700, "kod satırı 1 taştı %.0f" % e
    wt = Y.genislik("Fredoka", 700, "Türkçeye", 124)
    s.yol("kx", Y.el_cizgi(y1[0][1] - 8, 478, y1[0][1] + wt + 8, 470, 2), tt(50, 2), 0.4, KRE, 8, 0.9, "cizgi", 0.6)
    e, y2 = dizi(s, "k2", 96, 730, [{"m": "çerçeveye ", "t": tt(50, 3), "r": SAR}, {"m": "bak.", "t": tt(50, 4)}],
                 boy=156)
    assert e < 1700, "kod satırı 2 taştı %.0f" % e
    assert tt(50, 4) + 0.12 <= SON
    return s, {"kun": Y.kunye_svg("Recap", "Recap", 2, 2), "gruplar": gruplar}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

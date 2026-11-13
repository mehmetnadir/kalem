"""Sahne 04 dört çerçeve İLERİ (HyperFrames, 1920x1080): `panel` `kavram_karti` iki kutu.
Kutu 1 (cümle 7): `1) tekrar · kalıcı · genel gerçek`. Kutu 2 (cümle 8): `2) dört çerçeve`; Türkçe yanıltır notları,
sonra kutu dörde bölünür. Cümle 9: dört kutu sırayla yanar (Özet film · Tabela sign · Tören promise · Tarife flight).
Cümle 10: üç kutu dolgu (kök), dördüncü kutuya kalemle ünlem (kırmızı yalnız burada), `3 kök + 1 tuzak`.
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn; cümle 7–10).
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
SOZ = {c: [w for w in _ALL if w["cumle"] == c] for c in (7, 8, 9, 10)}
R = Y.RENK
KRE, IKN, SAR, KIR = R["murekkep"], R["ikincil"], R["vurgu"], R["kirmizi"]
TB = Z["t_bas"]
SON = (Z["kare"] - 12) / 30          # içerik sonu (yerel sn); son 12 kare durgun

KX, KW = 96, 1728
B1Y, B1H = 140, 170                  # kutu 1
B2Y, B2H = 350, 500                  # kutu 2 (dış)
SX, SW, SG, SY, SH = 136, 380, 40, 480, 340   # dört alt kutu: x, genişlik, aralık, y, yükseklik


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

    # dolgu dikdörtgenleri önce (z sırası: yazının arkasında); C10'da açılır
    for i in range(3):
        x = SX + i * (SW + SG)
        s.svg.append('<rect id="sf%d" x="%d" y="%d" width="%d" height="%d" rx="14" fill="%s" fill-opacity="0.35" '
                     'style="opacity:0"/>' % (i, x, SY, SW, SH, SAR))

    # ================= C7: kutu 1 =================
    s.yol("k1", Y.el_kutu(KX, B1Y, KW, B1H), tt(7, 0), 0.6, KRE, 4.5, 1, "cizgi", 0.7)
    e, _ = dizi(s, "r", 136, B1Y + 112, [
        {"m": "1) ", "t": tt(7, 3), "r": SAR}, {"m": "tekrar", "t": tt(7, 7), "tik": True},
        {"m": " · ", "t": tt(7, 8) - 0.12, "r": IKN}, {"m": "kalıcı", "t": tt(7, 8)},
        {"m": " · ", "t": tt(7, 10) - 0.12, "r": IKN}, {"m": "genel ", "t": tt(7, 10)},
        {"m": "gerçek", "t": tt(7, 11)}], boy=68)
    e2, _ = dizi(s, "rb", 1440, B1Y + 108, [{"m": "bildiğin ", "t": tt(7, 5)}, {"m": "kullanımlar", "t": tt(7, 6)}],
                 aile="Caveat", boy=52)
    assert e < 1400, "kutu 1 yazısı notla çakışır %.0f" % e
    assert e2 < KX + KW - 20, "kutu 1 notu taştı %.0f" % e2

    # ================= C8: kutu 2 =================
    s.yol("k2", Y.el_kutu(KX, B2Y, KW, B2H), tt(8, 0), 0.7, KRE, 4.5, 1, "cizgi", 0.7)
    s.yazi("t2n", 136, B2Y + 80, [("2) ", SAR)], "Fredoka", 700, 60, tt(8, 0) + 0.2, 0.3, tur="tik", guc=0.5)
    wn = Y.genislik("Fredoka", 700, "2) ", 60)
    s.yazi("t2", 136 + wn, B2Y + 80, [("dört çerçeve", KRE)], "Fredoka", 700, 60, tt(8, 11), 0.5, tur="tik", guc=0.55)
    g0 = len(s.svg)
    e, _ = dizi(s, "y", 156, 620, [{"m": "Türkçe ", "t": tt(8, 2)}, {"m": "yanıltır", "t": tt(8, 3), "r": SAR}],
                aile="Caveat", boy=84)
    e1, _ = dizi(s, "z", 156, 740, [{"m": "şimdiki", "t": tt(8, 5)}, {"m": " · geçmiş", "t": tt(8, 6)},
                                    {"m": " · gelecek", "t": tt(8, 9)}], aile="Caveat", boy=76)
    assert e1 < KX + KW - 40, "notlar taştı %.0f" % e1
    grup("gN", g0)
    sol("gN", tt(8, 11) - 0.15)
    # dörde bölünür: dört boş alt kutu
    for i in range(4):
        x = SX + i * (SW + SG)
        s.yol("so%d" % i, Y.el_kutu(x, SY, SW, SH), tt(8, 11) + i * 0.22, 0.45, IKN, 4, 1, "cizgi", 0.5)

    # ================= C9: dört kutu sırayla yanar =================
    DUR = (("Özet", "film", tt(9, 0), tt(9, 3)), ("Tabela", "sign", tt(9, 7), tt(9, 7) + 0.12),
           ("Tören", "promise", tt(9, 10), tt(9, 14)), ("Tarife", "flight", tt(9, 16), tt(9, 16) + 0.12))
    for i, (ad, kel, th, tk) in enumerate(DUR):
        x = SX + i * (SW + SG)
        s.yol("sy%d" % i, Y.el_kutu(x, SY, SW, SH), th, 0.5, SAR, 7, 0.95, "cizgi", 0.6)
        s.yazi("sh%d" % i, x + 36, SY + 86, [(ad, KRE)], "Fredoka", 700, 56, th + 0.1, 0.3, tur="tik", guc=0.5)
        s.yazi("sk%d" % i, x + 36, SY + 250, [(kel, SAR)], "Caveat", 700, 100, tk, 0.4, tur="tik", guc=0.5)
        assert Y.genislik("Caveat", 700, kel, 100) < SW - 50, "anahtar sözcük taştı " + kel
        assert Y.genislik("Fredoka", 700, ad, 56) < SW - 50, "kutu başlığı taştı " + ad

    # ================= C10: 3 kök + 1 tuzak =================
    g0 = len(s.svg)
    e, _ = dizi(s, "w", 136, 950, [{"m": "Türkçe ", "t": tt(10, 5)}, {"m": "seni ", "t": tt(10, 6)},
                                   {"m": "başka ", "t": tt(10, 7)}, {"m": "zamana ", "t": tt(10, 8)},
                                   {"m": "çeker", "t": tt(10, 9), "r": SAR}], aile="Caveat", boy=72)
    assert e < KX + KW - 40
    grup("gW", g0)
    sol("gW", tt(10, 9) + 0.55)
    for i in range(3):    # üç kutu dolgu: kök
        t = tt(10, 11) + i * 0.3
        s.to("#sf%d" % i, t, {"opacity": 1, "duration": 0.4, "ease": "power2.out"})
        s.olay(t, "tik", 0.45)
    e, _ = dizi(s, "v", 136, 950, [
        {"m": "3 ", "t": tt(10, 10), "r": SAR, "tik": True}, {"m": "kök", "t": tt(10, 12)},
        {"m": " + ", "t": tt(10, 14) - 0.1, "r": IKN}, {"m": "1 ", "t": tt(10, 15), "r": SAR},
        {"m": "tuzak", "t": tt(10, 16), "r": KIR, "tik": True}], boy=64)
    assert e < KX + KW - 40
    # dördüncü kutu: kırmızı kenar + kalemle ünlem (kırmızı yalnız burada)
    x4 = SX + 3 * (SW + SG)
    tz = tt(10, 15)
    s.yol("sr", Y.el_kutu(x4, SY, SW, SH), tz, 0.5, KIR, 7, 1, "cizgi", 0.6)
    ux = x4 + SW - 36
    s.yol("un1", "M%d %d Q%d %d %d %d" % (ux, SY - 70, ux + 3, SY - 34, ux - 2, SY + 12), tz + 0.3, 0.28, KIR, 12, 1,
          "cizgi", 0.7)
    s.yol("un2", "M%d %d l0.1 0" % (ux - 4, SY + 54), tz + 0.58, 0.1, KIR, 17, 1, "tik", 0.6)
    assert tz + 0.7 <= SON, "ünlem içerik sonunu aştı"
    assert tt(10, 16) + 0.12 <= SON
    return s, {"kun": Y.kunye_svg("Rule", "Rule", 1, 1), "gruplar": gruplar}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

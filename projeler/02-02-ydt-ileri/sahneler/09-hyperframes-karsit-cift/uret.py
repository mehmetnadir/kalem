"""Sahne 09 — Karşıt çift Mike (HyperFrames, 1920x1080, 844 kare, cümle 28–33).
Bölüm perdesi (KARŞIT ÇİFT) → sol kart «Mike lives and works in Birmingham.» (live|s, work|s; uzun kalıcı bant; home)
→ sağ kart «Mike is staying in a hotel this week.» (this week sarı köşeli ayraç; kısa bant; bed) → Türkçe çeviriler
(soluk italik; yor altı çizili) → fark tablosu (kalıcı → geniş zaman · geçici → şimdiki zaman).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (cümle içi sıra numarası). Yerel sn = küresel − t_bas.
Renk yalnız Y.RENK (kunye.js TEMALAR eşleniği); kırmızı yok (kırmızı yalnız sahne 04 ünlemi)."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_HAM = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
SOZ = {c: [w for w in _HAM if w["cumle"] == c] for c in range(28, 34)}
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]

# ---- yerleşim (px) ----
LX, RX, CW = 96, 984, 840            # sol/sağ kart x, kart genişliği
CY, CH = 170, 236                    # kart y, yüksekliği
B1, B2 = CY + 88, CY + 88 + 78       # kart içi satır tabanları
FS = 54                              # kart yazısı
AX = 470                             # zaman çizgisi y
IKY = 520                            # ikon üst
TRY = 700                            # çeviri taban
TLY, TLH = 770, 214                  # fark tablosu y, yükseklik


def T(c, i):
    """Cümle c içindeki i. sözcüğün t0'ı (küresel sn)."""
    return SOZ[c][i]["t0"]


def ikon(s, ad, kimlik, x, y, boy, t0, t1, w=4.0, renk=KRE):
    """Tabler ikonu kalemle çizilir (24x24 kutu -> boy px); yollar sırayla."""
    yollar = Y.tabler(ad)
    sc = boy / 24.0
    govde = "".join('<path id="%s%d" d="%s" style="opacity:0"/>' % (kimlik, i, d) for i, d in enumerate(yollar))
    s.svg.append('<g id="%s" transform="translate(%.1f %.1f) scale(%.4f)" fill="none" stroke="%s" '
                 'stroke-width="%.3f" stroke-linecap="round" stroke-linejoin="round">%s</g>'
                 % (kimlik, x, y, sc, renk, w / sc, govde))
    for i, (b, d) in enumerate(Y.cizgi_zamanlari([1.0] * len(yollar), t0, t1)):
        s.cmd.append({"m": "draw", "id": "%s%d" % (kimlik, i), "t": b, "d": d, "a": 1})
        s.olay(b, "cizgi", 0.5)


def tr_satir(s, kid, x, y, kelimeler, idler, cumle, boy=34):
    """Türkçe çeviri: soluk italik, kelime kelime (sözcüğün t0'ında). Döner: [(x, genişlik)] her kelime için."""
    sp = Y.genislik("Lexend", 500, " ", boy)
    yer = []
    for k, (m, i) in enumerate(zip(kelimeler, idler)):
        w = Y.genislik("Lexend", 500, m, boy)
        s.yazi("%s%d" % (kid, k), x, y, [(m, IKN)], "Lexend", 500, boy, s.S(T(cumle, i)), 0.14,
               tur="tik" if k == 0 else None, guc=0.35, sar_ek='font-style="italic" opacity=".85"')
        yer.append((x, w))
        x += w + sp
    return yer


def uret():
    s = Y.Sahne(TB)
    S = s.S
    tt = lambda c, i: S(T(c, i))  # noqa: E731
    gruplar = []

    def kimlikler(bas):
        return {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}

    # ================= C28 (196,99): bölüm perdesi KARŞIT ÇİFT =================
    g0 = len(s.svg)
    e, _ = Y.dizi(s, "pd", 96, 560, [{"m": "KARŞIT", "t": tt(28, 2), "tik": True}, {"m": " ÇİFT", "t": tt(28, 3)}], boy=170)
    wz = Y.genislik("Fredoka", 700, "KARŞIT ÇİFT", 170)
    s.yol("pdu", Y.el_cizgi(90, 594, 96 + wz + 10, 590, 3), tt(28, 3) + 0.35, 0.45, SAR, 10, 0.9, "cizgi", 0.6)
    gruplar.append(("gP", kimlikler(g0)))
    s.to("#gP", tt(29, 0) - 0.4, {"opacity": 0, "duration": 0.3, "ease": "power1.in"})

    # ================= C29 (199,38): sol kart — live|s, work|s; uzun kalıcı bant =================
    s.yol("kl", Y.el_kutu(LX, CY, CW, CH), tt(29, 0) - 0.05, 0.45, IKN, 4, 1, "cizgi", 0.5)
    tx = LX + 34
    e1, yer1 = Y.dizi(s, "l1", tx, B1, [
        {"m": "Mike ", "t": tt(29, 0), "tik": True}, {"m": "live", "t": tt(29, 1)},
        {"kutu": True, "m": "s", "t": tt(29, 1) + 0.18, "bos": 6}, {"m": " and ", "t": tt(29, 2)},
        {"m": "work", "t": tt(29, 3)}, {"kutu": True, "m": "s", "t": tt(29, 3) + 0.18}], boy=FS)
    e2, _ = Y.dizi(s, "l2", tx, B2, [{"m": "in ", "t": tt(29, 4)}, {"m": "Birmingham.", "t": tt(29, 5)}], boy=FS)
    assert max(e1, e2) < LX + CW - 20, "sol kart taştı: %.0f" % max(e1, e2)
    # zaman çizgisi + uzun kalıcı bant (Birmingham söylenirken)
    s.yol("al", Y.el_ok(LX + 14, AX, LX + CW - 14, AX, 1), tt(29, 5) + 0.05, 0.7, IKN, 4, 1, "cizgi", 0.45)
    s.yol("bl", Y.el_cizgi(LX + 44, AX, LX + 690, AX - 1, 0.3), tt(29, 5) + 0.45, 0.9, KRE, 20, 0.9, "cizgi", 0.55)

    # ================= C30 (202,49): kalıcı — home, TR çeviri, live/work, süreklilik =================
    ikon(s, "home", "ev", LX + 10, IKY, 110, tt(30, 0), tt(30, 0) + 1.0)
    tr_satir(s, "t1", LX + 4, TRY, ["Mike", "Birmingham'da", "yaşıyor", "ve", "çalışıyor."], [0, 1, 2, 3, 4], 30)
    sw1 = Y.genislik("Caveat", 700, "kalıcı", 76)
    s.yazi("ka", LX + 170, IKY + 84, [("kalıcı", KRE)], "Caveat", 700, 76, tt(30, 5), 0.5, tur="tik", guc=0.55)
    s.yol("kau", Y.el_cizgi(LX + 166, IKY + 100, LX + 176 + sw1, IKY + 99, 2), tt(30, 6), 0.4, SAR, 8, 0.9, "cizgi", 0.5)
    (_, xl, wl), (_, xw, ww) = yer1[1], yer1[4]
    s.yol("ul", Y.el_cizgi(xl - 2, B1 + 18, xl + wl + 2, B1 + 17, 1), tt(30, 8), 0.35, SAR, 8, 0.9, "cizgi", 0.5)
    s.yol("uw", Y.el_cizgi(xw - 2, B1 + 18, xw + ww + 2, B1 + 17, 1), tt(30, 10), 0.35, SAR, 8, 0.9, "cizgi", 0.5)
    s.yol("bok", Y.el_ok(LX + 690, AX - 1, LX + 806, AX, 1), tt(30, 11), 0.5, KRE, 8, 0.9, "cizgi", 0.5)   # süreklilik

    # ================= C31 (210,04): sağ kart — this week sarı köşeli ayraç; kısa bant =================
    s.yol("kr", Y.el_kutu(RX, CY, CW, CH), tt(31, 0) - 0.05, 0.45, IKN, 4, 1, "cizgi", 0.5)
    rx = RX + 34
    e3, _ = Y.dizi(s, "r1", rx, B1, [
        {"m": "Mike ", "t": tt(31, 0), "tik": True}, {"m": "is ", "t": tt(31, 1)},
        {"m": "staying ", "t": tt(31, 2)}, {"m": "in", "t": tt(31, 3)}], boy=FS)
    e4, yer4 = Y.dizi(s, "r2", rx, B2, [
        {"m": "a ", "t": tt(31, 4)}, {"m": "hotel ", "t": tt(31, 5), "bos": 16}, {"m": "this ", "t": tt(31, 6)},
        {"m": "week.", "t": tt(31, 7)}], boy=FS)
    assert max(e3, e4) < RX + CW - 20, "sağ kart taştı: %.0f" % max(e3, e4)
    bx0, bx1 = yer4[2][1] - 14, yer4[3][1] + yer4[3][2] + 14
    by0, by1 = B2 - 56, B2 + 20
    s.yol("sb1", "M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f" % (bx0 + 14, by0, bx0, by0 + 1, bx0 - 1, by1, bx0 + 14, by1 + 1),
          tt(31, 6), 0.3, SAR, 7, 1, "cizgi", 0.55)
    s.yol("sb2", "M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f" % (bx1 - 14, by0, bx1, by0 + 1, bx1 + 1, by1, bx1 - 14, by1 + 1),
          tt(31, 7), 0.3, SAR, 7, 1, "cizgi", 0.55)
    s.yol("ar", Y.el_ok(RX + 14, AX, RX + CW - 14, AX, 1), tt(31, 3), 0.6, IKN, 4, 1, "cizgi", 0.45)
    s.yol("br", Y.el_cizgi(RX + 330, AX, RX + 520, AX - 1, 0.3), tt(31, 7) + 0.1, 0.4, SAR, 20, 0.95, "cizgi", 0.55)

    # ================= C32 (212,83): geçici — bed, TR çeviri =================
    ikon(s, "bed", "yatak", RX + 10, IKY, 110, tt(32, 0), tt(32, 0) + 1.0)
    yer_t2 = tr_satir(s, "t2", RX + 4, TRY, ["Mike", "bu", "hafta", "otelde", "kalıyor."], [0, 1, 2, 3, 4], 32)
    sw2 = Y.genislik("Caveat", 700, "geçici", 76)
    s.yazi("ge", RX + 170, IKY + 84, [("geçici", KRE)], "Caveat", 700, 76, tt(32, 5), 0.5, tur="tik", guc=0.55)
    s.yol("geu", Y.el_cizgi(RX + 166, IKY + 100, RX + 176 + sw2, IKY + 99, 2), tt(32, 6), 0.4, SAR, 8, 0.9, "cizgi", 0.5)

    # ================= C33 (216,42): yor alır → fark tablosu =================
    # «yor» (217,70): çevirilerde yaşıyor, çalışıyor, kalıyor sözcüklerinin yor eki altı çizilir
    wy = Y.genislik("Lexend", 500, "yor", 34)
    t1y = {k: None for k in range(5)}
    sp = Y.genislik("Lexend", 500, " ", 34)
    xs, x = [], LX + 4
    for m in ["Mike", "Birmingham'da", "yaşıyor", "ve", "çalışıyor."]:
        xs.append((x, Y.genislik("Lexend", 500, m, 34)))
        x += xs[-1][1] + sp
    hedef = [(xs[2][0] + xs[2][1] - wy, "y1", 0.0), (xs[4][0] + xs[4][1] - Y.genislik("Lexend", 500, ".", 34) - wy, "y2", 0.12),
             (yer_t2[4][0] + yer_t2[4][1] - Y.genislik("Lexend", 500, ".", 32) - Y.genislik("Lexend", 500, "yor", 32), "y3", 0.24)]
    for xx, kid, gec in hedef:
        gw = wy if kid != "y3" else Y.genislik("Lexend", 500, "yor", 32)
        s.yol(kid, Y.el_cizgi(xx - 2, TRY + 12, xx + gw + 2, TRY + 11, 1), tt(33, 3) + gec, 0.3, SAR, 6, 0.95, "cizgi", 0.5)
    # tablo çerçevesi: «Fark» (218,74)
    s.yol("tl", Y.el_kutu(96, TLY, 1728, TLH), tt(33, 5) - 0.05, 0.5, KRE, 4.5, 1, "cizgi", 0.6)
    FT = 62
    w1 = max(Y.genislik("Fredoka", 700, "kalıcı", FT), Y.genislik("Fredoka", 700, "geçici", FT))
    for no, (ad1, i1, io, ad3a, i3a, ad3b, i3b, yb) in enumerate((
            ("kalıcı", 7, 7, "geniş", 8, " zaman", 9, TLY + 92),
            ("geçici", 10, 10, "şimdiki", 11, " zaman", 12, TLY + 180))):
        bos = w1 - Y.genislik("Fredoka", 700, ad1, FT) + 40
        e5, _ = Y.dizi(s, "f%d" % no, 150, yb, [
            {"m": ad1, "t": tt(33, i1), "tik": True, "bos": bos},
            {"ok": 120, "t": tt(33, i3a) - 0.3, "bos": 40},
            {"m": ad3a, "t": tt(33, i3a), "r": SAR}, {"m": ad3b, "t": tt(33, i3b), "r": SAR}], boy=FT)
        assert e5 < 1824 - 40, "tablo satırı taştı: %.0f" % e5
    return s, {"kun": Y.kunye_svg("Contrast", "Contrast", 2, 2), "gruplar": gruplar}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

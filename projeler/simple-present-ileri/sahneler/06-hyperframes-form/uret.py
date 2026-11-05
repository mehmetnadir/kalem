"""Sahne 06 (SIMPLE PRESENT İLERİ, yatay 1920x1080): öğrenci sorusu + tarife/will + durum fiilleri + kod.
Tek kaynak: ortak/anlatim/sozcukler.json (küresel sn) + zamanlar.json (t_bas, kare). Yerel sn = t - t_bas.
Komut listesi veri olarak JS'e gömülür; olaylar aynı çağrılardan toplanır (olay.py bu modülü içe alır).
Akış: soru (balon + will take off ?) -> Hayır: ✗ will, tarife/program/takvim -> Simple Present, takes off ✓
-> will = predictions · sudden decisions -> durum fiilleri (know own cost, -ing ✗, I know ✓ / I am knowing ✗)
-> Kod: tarife → Simple Present / tahmin → will."""
import json
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
SOZ = {c: [w for w in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
           if w["cumle"] == c] for c in (6, 7)}
R = Y.RENK
KRE, IKN, SAR, KIR = R["murekkep"], R["ikincil"], R["vurgu"], R["kirmizi"]
TB = Z["t_bas"]


def T(c, i, beklenen=None):
    """Sözcük başlangıcı (küresel sn); beklenen verilirse sözcük sırası doğrulanır."""
    if beklenen:
        assert SOZ[c][i]["sozcuk"].lower().startswith(beklenen.lower()), (c, i, SOZ[c][i]["sozcuk"], beklenen)
    return SOZ[c][i]["t0"]


def T1(c, i):
    return SOZ[c][i]["t1"]


def kimlikler(s, bas):
    """s.svg[bas:] elemanlarının üst düzey id kümesi."""
    return {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}


def sivri(x, y0, y1, k=34):
    """Sağa bakan küme ayracı }; uç x+k+34'te."""
    ym = (y0 + y1) / 2
    return ("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f L%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f "
            "C%.1f %.1f %.1f %.1f %.1f %.1f L%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
                x, y0, x + k * .7, y0, x + k * .9, y0 + 14, x + k, y0 + 44, x + k, ym - 34,
                x + k, ym - 12, x + k + 14, ym - 4, x + k + 34, ym,
                x + k + 14, ym + 4, x + k, ym + 12, x + k, ym + 34, x + k, y1 - 44,
                x + k * .9, y1 - 14, x + k * .7, y1, x, y1))


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


def etiket(s, kimlik, x, yb, metin, t, boy=56, kutu_renk=IKN):
    """El kutulu etiket: kutu çizilir, sonra yazı. Döner: sağ kenar x."""
    w = Y.genislik("Fredoka", 700, metin, boy)
    s.yol(kimlik + "k", Y.el_kutu(x, yb - boy * 0.95, w + 56, boy * 1.35), t - 0.05, 0.3, kutu_renk, 4, 1, "cizgi", 0.5)
    s.yazi(kimlik, x + 28, yb, [(metin, KRE)], "Fredoka", 700, boy, t + 0.12, 0.3, tur="tik", guc=0.55)
    return x + w + 56


def uret():
    s = Y.Sahne(TB)
    S = s.S
    bal_ids = []
    # ---------------- öğrenci başı (peeps-kit) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.59, 104.0, 176.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, 2.8 / BS, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = max(S(T(6, 0)) - 0.14, 0.42)          # soğuk açılış: ilk 12 kare (0,40 sn) boş
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu + sözcükler (Caveat 700 58, iki satır; Fredoka ğ ş İ taşımaz) ----------------
    BF, BX, BASE = 58, 384.0, (240, 316)
    sp = Y.genislik("Caveat", 700, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6, 7, 8))
    gens = [sum(Y.genislik("Caveat", 700, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = BX + max(gens) + 44
    s.yol("bal", Y.balon_sol(340, 176, x1b, 342, 262, 292), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    pos = {}
    for sat, base in zip(satir, BASE):
        x = BX
        for i in sat:
            m = SOZ[6][i]["sozcuk"]
            w = Y.genislik("Caveat", 700, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Caveat", 700, BF, S(T(6, i)), 0.12,
                   tur="tik" if i in (0, 4) else None)
            bal_ids.append("bw%d" % i)
            pos[i] = (x, w, base)
            x += w + sp
    # fosforlu belirteç: will take off altı (balonda)
    xa, xb = pos[4][0], pos[6][0] + pos[6][1]
    s.yol("bm", Y.el_cizgi(xa - 2, BASE[1] + 12, xb + 2, BASE[1] + 9), S(T(6, 6, "off")), 0.4, SAR, 8, 0.85,
          "cizgi", 0.5)
    bal_ids.append("bm")

    # soru anı: takvim (yarın) solda; Hayır'dan sonra söner
    tcal = S(T(6, 1, "yar"))
    ikon(s, "calendar", "cal", 230, 470, 230, tcal, tcal + 0.8, 4.4, KRE)
    cw_ = Y.genislik("Caveat", 700, "yarın", 80)
    s.yazi("caln", 230 + 115 - cw_ / 2, 790, [("yarın", KRE)], "Caveat", 700, 80, tcal + 0.5, 0.4, tur="tik",
           guc=0.5)
    for kim in ("cal", "caln"):
        s.to("#" + kim, S(66.95), {"opacity": 0, "duration": 0.4, "ease": "power1.in"})
    # ---------------- bölüm A: will take off ? (sağ) -> Hayır: ✗ will (66,43) -> takes off ✓ ----------------
    iA = len(s.svg)
    PF, PY = 110, 560.0
    sp2 = Y.genislik("Fredoka", 700, " ", PF)
    gw = [Y.genislik("Fredoka", 700, SOZ[6][i]["sozcuk"], PF) for i in (4, 5, 6)]
    px0 = 1700 - sum(gw) - 2 * sp2
    cx, pp = px0, []
    for n, i in enumerate((4, 5, 6)):
        m = SOZ[6][i]["sozcuk"]
        s.yazi("pw%d" % n, cx, PY, [(m, KRE)], "Fredoka", 700, PF, S(T(6, i)), 0.15, tur="tik" if n == 0 else None)
        pp.append((cx, gw[n]))
        cx += gw[n] + sp2
    s.yazi("pq", cx - sp2 + 16, PY + 6, [("? ", SAR)], "Caveat", 700, 150, S(T(6, 7, "olmaz")), 0.3, tur="tik",
           guc=0.6)
    # 66,43 Hayır.: will üstüne büyük kırmızı kalem çarpısı
    tx = S(T(7, 0, "Hay"))
    wx, ww = pp[0]
    s.yol("xk1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (wx - 16, PY - 104, wx + ww / 2, PY - 40, wx + ww + 16, PY + 18),
          tx, 0.3, KIR, 10, 1, "cizgi", 0.7)
    s.yol("xk2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (wx + ww + 16, PY - 104, wx + ww / 2, PY - 46, wx - 16, PY + 18),
          tx + 0.3, 0.3, KIR, 10, 1, "cizgi", 0.7)
    s.olay(tx + 0.3, "vurus", 0.85)
    s.to("#ku-bolum", tx, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tx, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    s.to("#ku-ajA", tx, {"opacity": 0, "duration": 0.2})
    s.to("#ku-ajB", tx, {"opacity": 1, "duration": 0.2})
    # balon + baş köşeye toplanır
    s.to("#balg", S(66.95), {"svgOrigin": "90 150", "scale": 0.62, "opacity": 0.85, "duration": 0.7,
                             "ease": "power3.inOut"})
    # 70,40 takes off ✓ (mürekkep)
    tkk = S(70.4)
    s.yazi("to1", px0, PY + 150, [("takes off", KRE)], "Fredoka", 700, PF, tkk, 0.3, tur="tik", guc=0.6)
    tw_ = Y.genislik("Fredoka", 700, "takes off", PF)
    s.yol("tot", Y.tik_yolu(px0 + tw_ + 36, PY + 150 - 88, 80), tkk + 0.35, 0.3, KRE, 11, 1, "cizgi", 0.55)
    s.olay(tkk + 0.4, "vurus", 0.8)

    # ---------------- sol: tarife · program · takvim -> Simple Present kutusu (67,31–70,99) ----------------
    LF, LX = 80, 140.0
    RY = (470, 560, 650)
    adlar = [SOZ[7][i]["sozcuk"].rstrip(",").lower() for i in (1, 2, 3)]
    gen = max(Y.genislik("Fredoka", 700, a, LF) for a in adlar)
    for n, i in enumerate((1, 2, 3)):
        s.yazi("lf%d" % n, LX, RY[n], [(adlar[n], KRE)], "Fredoka", 700, LF, S(T(7, i)), 0.3, tur="tik", guc=0.55)
    bxx = LX + gen + 30
    tkes = S(T(7, 4, "kesinse"))
    s.yol("lsiv", sivri(bxx, 400, 690), tkes, 0.5, IKN, 5, 1, "cizgi", 0.55)
    kx, ky = bxx + 68 + 22, 496.0
    bt = "Simple Present"
    bw_ = Y.genislik("Fredoka", 700, bt, 64)
    tsp = S(T(7, 5, "Simple"))
    s.yol("lbox", Y.el_kutu(kx, ky, bw_ + 60, 104), tsp, 0.5, SAR, 5, 1, "cizgi", 0.6)
    s.yazi("ltxt", kx + 30, ky + 72, [(bt, KRE)], "Fredoka", 700, 64, tsp + 0.25, 0.5, tur="tik", guc=0.55)
    # ---------------- sol alt: will = predictions · sudden decisions (71,24–75,01) ----------------
    WY = 860.0
    tw0 = S(T(7, 7, "Will"))
    s.yazi("wl", LX, WY, [("will", KRE)], "Fredoka", 700, 80, tw0, 0.3, tur="tik", guc=0.6)
    ww_ = Y.genislik("Fredoka", 700, "will", 80)
    s.yazi("we", LX + ww_ + 28, WY, [("=", IKN)], "Fredoka", 700, 80, S(T(7, 8, "is")), 0.2, tur=None)
    ex = LX + ww_ + 28 + Y.genislik("Fredoka", 700, "=", 80) + 36
    ex = etiket(s, "e1", ex, WY, "predictions", S(T(7, 10, "predictions")))
    etiket(s, "e2", ex + 30, WY, "sudden decisions", S(T(7, 12, "sudden")))
    gA = kimlikler(s, iA)
    # s2 -> sağ üst çipe toplanır (74,55)
    s.to("#s2", S(74.55), {"svgOrigin": "140 380", "scale": 0.5, "x": 890, "y": -250, "duration": 0.6,
                           "ease": "power3.inOut"})

    # ---------------- bölüm B: durum fiilleri (75,01–84,87) ----------------
    iB = len(s.svg)
    t_d = S(T(7, 14, "Durum"))
    s.yazi("dh", 140, 400, [("durum fiilleri", SAR)], "Caveat", 700, 64, t_d, 0.7, tur="tik", guc=0.55)
    FF_, FX = 88, 140.0
    FY = (500, 600, 700)
    nm = [SOZ[7][i]["sozcuk"].rstrip(",:").lower() for i in (16, 17, 18)]
    gen2 = max(Y.genislik("Fredoka", 700, a, FF_) for a in nm)
    for n, i in enumerate((16, 17, 18)):
        s.yazi("fl%d" % n, FX, FY[n], [(nm[n], KRE)], "Fredoka", 700, FF_, S(T(7, i)), 0.3, tur="tik", guc=0.55)
    bx3 = FX + gen2 + 30
    tnow = S(T(7, 19, "now"))
    s.yol("fsiv", sivri(bx3, 430, 730), tnow - 0.25, 0.5, IKN, 5, 1, "cizgi", 0.55)
    xn = bx3 + 68 + 40
    s.yazi("fnow", xn, 520, [("now", KRE)], "Fredoka", 700, 88, tnow, 0.3, tur="tik", guc=0.6)
    nw_ = Y.genislik("Fredoka", 700, "now", 88)
    ikon(s, "clock", "fclk", xn + nw_ + 36, 440, 110, tnow + 0.3, tnow + 0.9, 4.0, SAR)
    ting = S(T(7, 22, "ing"))
    s.yazi("fing", xn, 700, [("-ing", SAR)], "Fredoka", 700, 130, ting, 0.3, tur="tik", guc=0.6)
    iw = Y.genislik("Fredoka", 700, "-ing", 130)
    ta = S(T(7, 23, "almaz"))
    s.yol("fx1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xn - 16, 700 - 100, xn + iw / 2, 700 - 44, xn + iw + 16, 700 + 14),
          ta, 0.28, KRE, 10, 1, "cizgi", 0.7)
    s.yol("fx2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xn + iw + 16, 700 - 100, xn + iw / 2, 700 - 50, xn - 16, 700 + 14),
          ta + 0.26, 0.28, KRE, 10, 1, "cizgi", 0.7)
    s.yazi("falm", xn + iw + 60, 700, [("almaz", IKN)], "Caveat", 700, 64, ta + 0.5, 0.4, tur="tik", guc=0.45)
    # sağ: I know the answer. ✓ / Not: I am knowing. ✗ (kırmızı çizgi 83,70)
    RX, RA, RB = 1110.0, 520.0, 700.0
    ya = []
    cx = RX
    sp3 = Y.genislik("Fredoka", 700, " ", 72)
    for n, i in enumerate((24, 25, 26, 27)):
        m = SOZ[7][i]["sozcuk"]
        w = Y.genislik("Fredoka", 700, m, 72)
        s.yazi("ra%d" % n, cx, RA, [(m, KRE)], "Fredoka", 700, 72, S(T(7, i)), 0.12, tur="tik" if n == 0 else None)
        ya.append((cx, w))
        cx += w + sp3
    s.yol("rah", Y.el_daire(ya[1][0] + ya[1][1] / 2, RA - 26, ya[1][1] / 2 + 12, 52, 2.0), S(T(7, 25, "know")) + 0.1,
          0.4, SAR, 7, 0.85, "parilti", 0.5)
    s.yol("rat", Y.tik_yolu(RX - 70, RA - 50, 56), S(T(7, 27, "answer")) + 0.5, 0.3, KRE, 9, 1, "cizgi", 0.55)
    s.yazi("rnot", RX, 610, [("Not:", IKN)], "Caveat", 700, 56, S(T(7, 28, "Not")), 0.3, tur="tik", guc=0.45)
    cx, yb = RX, []
    for n, i in enumerate((29, 30, 31)):
        m = SOZ[7][i]["sozcuk"]
        w = Y.genislik("Fredoka", 700, m, 72)
        s.yazi("rb%d" % n, cx, RB, [(m, KRE)], "Fredoka", 700, 72, S(T(7, i)), 0.12, tur="tik" if n == 0 else None)
        yb.append((cx, w))
        cx += w + sp3
    xe = yb[2][0] + yb[2][1]
    tr = S(T(7, 31, "knowing"))
    s.yol("rbl", Y.el_cizgi(RX - 8, RB - 26, xe + 8, RB - 30, 1), tr + 0.1, 0.4, KIR, 9, 1, "cizgi", 0.65)
    s.yol("rbx1", "M%.1f %.1f L%.1f %.1f" % (RX - 70, RB - 56, RX - 14, RB), tr + 0.55, 0.15, KIR, 9, 1, "cizgi", 0.7)
    s.yol("rbx2", "M%.1f %.1f L%.1f %.1f" % (RX - 14, RB - 56, RX - 70, RB), tr + 0.7, 0.15, KIR, 9, 1, "cizgi", 0.5)
    s.olay(tr + 0.7, "vurus", 0.85)
    gB = kimlikler(s, iB)
    s.to("#s3", S(84.45), {"svgOrigin": "140 340", "scale": 0.5, "x": 0, "y": -10, "duration": 0.55,
                           "ease": "power3.inOut"})

    # ---------------- bölüm C: Kod: tarife → Simple Present / tahmin → will (84,87–89,43) ----------------
    tk = S(T(7, 32, "Kod"))
    s.yazi("kod", 140, 650, [("Kod:", IKN)], "Caveat", 700, 64, tk, 0.4, tur="tik")
    KF, K1, K2 = 110, 790.0, 930.0
    a1 = Y.genislik("Fredoka", 700, "tarife", KF)
    ok_ = 170.0   # el çizimi ok için boşluk (Fredoka → taşımaz)
    s.yazi("k1a", 140, K1, [("tarife", KRE)], "Fredoka", 700, KF, S(T(7, 33, "tarife")), 0.35, tur="tik", guc=0.6)
    s.yol("k1o", Y.el_ok(140 + a1 + 28, K1 - 40, 140 + a1 + 146, K1 - 40), S(T(7, 34, "varsa")), 0.3, IKN, 9, 1, "cizgi", 0.5)
    s.yazi("k1b", 140 + a1 + ok_, K1, [("Simple Present", SAR)], "Fredoka", 700, KF, S(T(7, 35, "Simple")), 0.5,
           tur="tik", guc=0.6)
    b1 = Y.genislik("Fredoka", 700, "tahmin", KF)
    s.yazi("k2a", 140, K2, [("tahmin", KRE)], "Fredoka", 700, KF, S(T(7, 37, "tahmin")), 0.35, tur="tik", guc=0.6)
    s.yol("k2o", Y.el_ok(140 + b1 + 28, K2 - 40, 140 + b1 + 146, K2 - 40), S(T(7, 38, "varsa")), 0.3, IKN, 9, 1, "cizgi", 0.5)
    s.yazi("k2b", 140 + b1 + ok_, K2, [("will", SAR)], "Fredoka", 700, KF, S(T(7, 39, "will")), 0.35, tur="tik",
           guc=0.7)
    tn2 = S(89.0)
    nw = Y.genislik("Lexend", 500, "Next lesson", 24)
    s.yazi("nx", 1864 - nw - 44, 984, [("Next lesson", IKN)], "Lexend", 500, 24, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M%.1f 976 L%.1f 976 M%.1f 969 L%.1f 976 L%.1f 983" % (1864 - 38, 1864 - 4, 1864 - 12, 1864 - 4,
                                                                          1864 - 12), tn2 + 0.3, 0.25, IKN, 3, 1,
          "cizgi", 0.4)
    kun = Y.kunye_svg("Question", "Form")
    return s, {"kun": kun, "bal_ids": bal_ids, "gruplar": [("s2", gA), ("s3", gB)]}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34),
               bal_ids=parca["bal_ids"], gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

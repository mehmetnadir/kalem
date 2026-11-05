"""Sahne 06 (SIMPLE PAST İLERİ yatay, 1920x1080): öğrenci sorusu + kural + form + kod.
Tek kaynak: ortak/anlatim/sozcukler.json (küresel sn) + zamanlar.json (t_bas, kare). Yerel sn = t - t_bas.
Komut listesi veri olarak JS'e gömülür; olaylar aynı çağrılardan toplanır (olay.py bu modülü içe alır)."""
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


def T(c, i):
    return SOZ[c][i]["t0"]


def T1(c, i):
    return SOZ[c][i]["t1"]


def kimlikler(s, bas):
    """s.svg[bas:] elemanlarının üst düzey id kümesi."""
    return {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}


def kelimeler(s, kimlik, x, y, idx, c, aile, agr, boy, renk=KRE, bosluk=None, tur0="tik"):
    """Sözcükleri konuşma zamanında tek tek açar. idx: sözcük sırası listesi (cümle c). Döner: [(x, w)]."""
    sp = Y.genislik(aile, agr, " ", boy) if bosluk is None else bosluk
    yer, cx = [], x
    for n, i in enumerate(idx):
        m = SOZ[c][i]["sozcuk"]
        w = Y.genislik(aile, agr, m, boy)
        s.yazi("%s%d" % (kimlik, n), cx, y, [(m, renk)], aile, agr, boy, s.S(T(c, i)), 0.12,
               tur=tur0 if n == 0 else None)
        yer.append((cx, w))
        cx += w + sp
    return yer


def sivri(x, y0, y1, k=34):
    """Sağa bakan küme ayracı }; uç x+k+34'te."""
    ym = (y0 + y1) / 2
    return ("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f L%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f "
            "C%.1f %.1f %.1f %.1f %.1f %.1f L%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
                x, y0, x + k * .7, y0, x + k * .9, y0 + 14, x + k, y0 + 44, x + k, ym - 34,
                x + k, ym - 12, x + k + 14, ym - 4, x + k + 34, ym,
                x + k + 14, ym + 4, x + k, ym + 12, x + k, ym + 34, x + k, y1 - 44,
                x + k * .9, y1 - 14, x + k * .7, y1, x, y1))


def uret():
    s = Y.Sahne(TB)
    S = s.S
    bal_ids = []
    # ---------------- öğrenci başı (peeps-kit) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.59, 104.0, 176.0
    sw = 2.8 / BS
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, sw, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = max(S(T(6, 0)) - 0.14, 0.42)   # soğuk açılış: ilk 12 kare (0,40 sn) boş
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu + sözcükler (Caveat: ğ ş İ Fredoka alt kümesinde yok) ----------------
    BF, BX, BASE = 56, 384.0, (252, 330)
    sp = Y.genislik("Caveat", 700, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6, 7))
    gens = [sum(Y.genislik("Caveat", 700, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = BX + max(gens) + 44
    s.yol("bal", Y.balon_sol(340, 176, x1b, 366, 262, 296), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
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
    # fosforlu belirteç: has resigned altı
    xa, xb = pos[3][0], pos[4][0] + pos[4][1]
    s.yol("bm", Y.el_cizgi(pos[4][0] - 2, BASE[1] + 12, xb + 2, BASE[1] + 9), S(T(6, 4)), 0.4, SAR, 8, 0.85,
          "cizgi", 0.5)
    bal_ids.append("bm")
    # sağ: yanlış öneri `has resigned + ago` (68,43), üstüne kırmızı çarpı (69,47)
    YX, YY, YF = 1050.0, 300.0, 76
    yp = [("has resigned", KRE), (" + ", IKN), ("ago", KRE)]
    yw = sum(Y.genislik("Fredoka", 700, p[0], YF) for p in yp)
    s.yazi("yan", YX, YY, yp, "Fredoka", 700, YF, S(T(6, 4)), 0.35, tur="tik", guc=0.55)
    bal_ids.append("yan")
    tc = S(T(6, 6))
    s.yol("xk1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (YX - 20, YY - 74, YX + yw / 2, YY - 22, YX + yw + 20,
                                                      YY + 24), tc, 0.3, KIR, 9, 1, "cizgi", 0.7)
    s.yol("xk2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (YX + yw + 20, YY - 74, YX + yw / 2, YY - 28, YX - 20,
                                                      YY + 24), tc + 0.3, 0.3, KIR, 9, 1, "cizgi", 0.7)
    s.olay(tc + 0.3, "vurus", 0.85)
    bal_ids += ["xk1", "xk2"]
    # künye: Question -> Form (71,06)
    tx = S(T(7, 0))
    s.to("#ku-bolum", tx, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tx, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    s.to("#ku-ajA", tx, {"opacity": 0, "duration": 0.2})
    s.to("#ku-ajB", tx, {"opacity": 1, "duration": 0.2})
    # balon + baş küçülüp yukarı kayar, alfa 0,45
    s.to("#balg", tx + 0.3, {"svgOrigin": "90 150", "scale": 0.62, "opacity": 0.45, "duration": 0.7,
                             "ease": "power3.inOut"})

    # ---------------- Olmaz. (71,06, vuruş) ----------------
    OZ = 160
    s.fromto("#olm", tx, {"opacity": 0, "scale": 0.7, "svgOrigin": "140 500"},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "back.out(1.6)", "svgOrigin": "140 500"})
    s.svg.append('<g id="olm" font-family="Fredoka" font-weight="700" font-size="%d" style="opacity:0">'
                 '<text x="140" y="500" fill="%s">Olmaz.</text></g>' % (OZ, KIR))
    s.olay(tx, "vurus", 0.9)

    # ---------------- kart: kural cümlesi (72,11–75,15) ----------------
    CXk, CYk, CWk, CHk = 730, 372, 1100, 176
    s.yol("kart1", Y.el_kutu(CXk, CYk, CWk, CHk), S(T(7, 1)) - 0.1, 0.6, KRE, 4.2, 1, "cizgi", 0.6)
    k1 = kelimeler(s, "kw", CXk + 40, 452, (1, 2, 3, 4, 5), 7, "Fredoka", 700, 60, tur0="tik")
    k2 = kelimeler(s, "kv", CXk + 40, 526, (6, 7, 8), 7, "Fredoka", 700, 60, tur0=None)
    s.yol("blk", Y.el_cizgi(k1[4][0] - 4, 452 + 16, k1[4][0] + k1[4][1] + 4, 452 + 14), S(T(7, 5)), 0.4, SAR, 8,
          0.9, "cizgi", 0.5)

    # ---------------- sol sütun: belirli zaman (75,56–79,88) ----------------
    LF, LX = 60, 140.0
    RY = (665, 745, 825)
    sol = ((9, "ago"), (10, "last year"), (12, "in 1911"))
    gmax = max(Y.genislik("Fredoka", 700, m, LF) for _, m in sol)
    for n, (i, m) in enumerate(sol):
        s.yazi("sl%d" % n, LX, RY[n], [(m, KRE)], "Fredoka", 700, LF, S(T(7, i)), 0.3, tur="tik", guc=0.55)
        w = Y.genislik("Fredoka", 700, m, LF)
        s.yol("st%d" % n, Y.tik_yolu(LX + w + 24, RY[n] - 40, 38), S(T(7, i)) + 0.3, 0.28, SAR, 7, 0.9, "cizgi", 0.5)
    bxx = LX + gmax + 24 + 38 + 22
    tb_ = S(T(7, 14))
    s.yol("sivri", sivri(bxx, 610, 850), tb_ - 0.1, 0.5, IKN, 5, 1, "cizgi", 0.55)
    s.yazi("bz", bxx + 34 + 34 + 22, 765, [("belirli zaman", SAR)], "Caveat", 700, 64, tb_, 0.6, tur="tik",
           guc=0.5)

    # ---------------- sağ sütun: Present Perfect isteyenler (80,44–83,12) ----------------
    RX = 1090.0
    tp = S(T(7, 16))
    s.yol("pk", Y.el_kutu(RX - 20, 572, 560, 84), tp, 0.5, KRE, 4.2, 1, "cizgi", 0.6)
    s.yazi("pt", RX + 10, 632, [("Present Perfect", SAR)], "Fredoka", 700, 56, tp + 0.2, 0.4, tur="tik", guc=0.55)
    for n, (i, m) in enumerate(((18, "for"), (19, "since"), (20, "yet"))):
        s.yazi("sr%d" % n, RX + 40, (735, 800, 865)[n], [(m, KRE)], "Fredoka", 700, LF,
               S(T(7, i)), 0.3, tur="tik", guc=0.55)

    # ---------------- Did not resign. (83,97–85,2) ----------------
    s.yazi("dd0", 140, 955, [("Did", SAR)], "Fredoka", 700, 72, S(T(7, 22)), 0.3, tur="tik", guc=0.6)
    dw = Y.genislik("Fredoka", 700, "Did ", 72)
    s.yazi("dd1", 140 + dw, 955, [("not", KRE)], "Fredoka", 700, 72, S(T(7, 23)), 0.25, tur=None)
    nw_ = Y.genislik("Fredoka", 700, "not ", 72)
    s.yazi("dd2", 140 + dw + nw_, 955, [("resign.", KRE)], "Fredoka", 700, 72, S(T(7, 24)), 0.3, tur="tik", guc=0.55)

    # ---------------- Kod: ago → Past, since → Perfect (85,90–90,54) ----------------
    tk = S(T(7, 25))
    s.to("#icerik", tk - 0.5, {"svgOrigin": "90 110", "scale": 0.6, "duration": 0.8, "ease": "power3.inOut"})
    i_kod = len(s.svg)
    s.yazi("kod", 140, 712, [("Kod:", KRE)], "Caveat", 700, 64, tk, 0.4, tur="tik")
    s.yol("kutu", Y.el_kutu(110, 736, 1190, 258), tk + 0.3, 0.7, IKN, 4.2, 1, "cizgi", 0.55)
    KF, K1, K2 = 112, 846, 960
    for n, (a, ai, b, bi, y) in enumerate((("ago", 26, "Past", 28, K1), ("since", 29, "Perfect", 31, K2))):
        aw = Y.genislik("Fredoka", 700, a, KF)
        ta = S(T(7, ai))
        s.yazi("ka%d" % n, 150, y, [(a, KRE)], "Fredoka", 700, KF, ta, 0.35, tur="tik", guc=0.6)
        ox = 150 + aw + 36
        s.yol("ko%d" % n, Y.el_ok(ox, y - 44, ox + 190, y - 44, 2.0 + n), ta + 0.45, 0.35, SAR, 9, 0.95, "cizgi", 0.55)
        s.yazi("kb%d" % n, ox + 190 + 40, y, [(b, SAR)], "Fredoka", 700, KF, S(T(7, bi)), 0.35, tur="tik", guc=0.6)
    # formül kartı toplanır (90,54)
    tf = S(T1(7, 31))
    CX, CY, CW, CH = 1350, 760, 480, 130
    s.yol("fk", Y.el_kutu(CX, CY, CW, CH), tf, 0.5, KRE, 4.5, 1, "cizgi", 0.7)
    parc = [("V2", SAR), (" · ", IKN), ("did + V1", KRE)]
    tw = sum(Y.genislik("Fredoka", 700, p[0], 52) for p in parc)
    cx0 = CX + (CW - tw - 70) / 2
    s.yazi("f1", cx0, CY + 82, parc, "Fredoka", 700, 52, tf + 0.1, 0.4, tur="tik", guc=0.6)
    s.yol("ftk", Y.tik_yolu(CX + CW - 74, CY + 40, 44), tf + 0.7, 0.3, SAR, 8, 0.9, "cizgi", 0.55)
    s.olay(tf + 0.7, "vurus", 0.8)
    nw = Y.genislik("Lexend", 500, "Next lesson", 24)
    tn2 = tf + 0.6
    s.yazi("nx", 1864 - nw - 44, 984, [("Next lesson", IKN)], "Lexend", 500, 24, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M%.1f 976 L%.1f 976 M%.1f 969 L%.1f 976 L%.1f 983" % (1864 - 38, 1864 - 4, 1864 - 12, 1864 - 4,
                                                                          1864 - 12), tn2 + 0.3, 0.25, IKN, 3, 1,
          "cizgi", 0.4)
    kod_ids = kimlikler(s, i_kod)
    kun = Y.kunye_svg("Question", "Form")
    return s, {"kun": kun, "bal_ids": bal_ids, "dis": kod_ids}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34),
               bal_ids=parca["bal_ids"], dis=parca["dis"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

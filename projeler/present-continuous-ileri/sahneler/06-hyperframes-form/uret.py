"""Sahne 06 (İLERİ yatay, 1920x1080): öğrenci sorusu + durum fiilleri + always şikâyeti + kod.
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


def kelimeler(s, kimlik, x, y, idx, c, aile, agr, boy, renk=KRE, bosluk=None):
    """Sözcükleri konuşma zamanında tek tek açar. idx: sözcük sırası listesi (cümle c). Döner: [(x, w)]."""
    sp = Y.genislik(aile, agr, " ", boy) if bosluk is None else bosluk
    yer, cx = [], x
    for n, i in enumerate(idx):
        m = SOZ[c][i]["sozcuk"]
        w = Y.genislik(aile, agr, m, boy)
        s.yazi("%s%d" % (kimlik, n), cx, y, [(m, renk)], aile, agr, boy, s.S(T(c, i)), 0.12,
               tur="tik" if n == 0 else None)
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


def balon(x0, y0, x1, y1, tx, ty):
    """El çizimi konuşma balonu; kuyruk alt kenardan (tx, ty) ucuna uzanır."""
    w, h = x1 - x0, y1 - y0
    return ("M%.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f "
            "C%.0f %.0f %.0f %.0f %.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f "
            "C%.0f %.0f %.0f %.0f %.0f %.0f L%.0f %.0f L%.0f %.0f "
            "C%.0f %.0f %.0f %.0f %.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f C%.0f %.0f %.0f %.0f %.0f %.0f Z" % (
                x0 + 36, y0 + 2, x0 + w * .3, y0 - 6, x0 + w * .65, y0 + 6, x1 - 36, y0 - 2,
                x1 - 10, y0, x1 + 2, y0 + 16, x1, y0 + 38,
                x1 + 4, y0 + h * .4, x1 - 3, y0 + h * .65, x1 + 1, y1 - 38,
                x1 - 2, y1 - 14, x1 - 16, y1 + 2, x1 - 40, y1,
                x1 - w * .3, y1 + 6, x0 + w * .5, y1 - 4, x0 + 150, y1 + 2, tx, ty, x0 + 70, y1 - 2,
                x0 + 30, y1, x0 + 4, y1 - 10, x0, y1 - 36,
                x0 - 4, y0 + h * .6, x0 + 4, y0 + h * .3, x0 + 1, y0 + 36,
                x0 - 2, y0 + 14, x0 + 14, y0 + 4, x0 + 36, y0 + 2))


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
    t0 = S(T(6, 0)) - 0.14          # soğuk açılış: ilk 12 kare (0,40 sn) boş; baş 0,42'de başlar
    t0 = max(t0, 0.42)
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu + sözcükler ----------------
    BF, BX, BASE = 44, 384.0, (234, 310)
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6, 7, 8, 9, 10))
    gens = [sum(Y.genislik("Fredoka", 600, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = BX + max(gens) + 44
    s.yol("bal", Y.balon_sol(340, 176, x1b, 342, 262, 292), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    pos = {}
    for sat, base in zip(satir, BASE):
        x = BX
        for i in sat:
            m = SOZ[6][i]["sozcuk"]
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(T(6, i)), 0.12,
                   tur="tik" if i in (0, 4, 9) else None)
            bal_ids.append("bw%d" % i)
            pos[i] = (x, w, base)
            x += w + sp
    # fosforlu belirteç: I am knowing altı
    xa, xb = pos[4][0], pos[6][0] + pos[6][1]
    s.yol("bm", el_cizgi_(xa - 2, BASE[1] + 12, xb + 2, BASE[1] + 9), S(T(6, 6)), 0.4, SAR, 8, 0.85, "cizgi", 0.5)
    bal_ids.append("bm")
    # 60,40 Olmaz.: yanlış cümle (I am knowing the answer) üstüne kırmızı kalem çarpısı
    xe = pos[8][0] + pos[8][1]
    tx = S(T(7, 0))
    s.yol("xk1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xa - 14, BASE[1] - 44, (xa + xe) / 2, BASE[1] - 8, xe + 14,
                                                       BASE[1] + 18), tx, 0.3, KIR, 8, 1, "cizgi", 0.7)
    s.yol("xk2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xe + 14, BASE[1] - 44, (xa + xe) / 2, BASE[1] - 14, xa - 14,
                                                       BASE[1] + 18), tx + 0.3, 0.3, KIR, 8, 1, "cizgi", 0.7)
    s.olay(tx + 0.3, "vurus", 0.85)
    bal_ids += ["xk1", "xk2"]
    # künye: Question -> Form (60,40)
    s.to("#ku-bolum", tx, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tx, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    s.to("#ku-ajA", tx, {"opacity": 0, "duration": 0.2})
    s.to("#ku-ajB", tx, {"opacity": 1, "duration": 0.2})
    # balon + baş köşeye toplanır
    s.to("#balg", S(61.25), {"svgOrigin": "90 150", "scale": 0.62, "opacity": 0.85, "duration": 0.7,
                             "ease": "power3.inOut"})

    # ---------------- sol sütun: durum fiilleri listesi (61,60–66,04) ----------------
    LF, LX = 88, 140.0
    RY = (480, 580, 680, 780)
    gen = max(Y.genislik("Fredoka", 700, SOZ[7][i]["sozcuk"].rstrip(",").lower(), LF) for i in (1, 2, 3, 4))
    for n, i in enumerate((1, 2, 3, 4)):
        m = SOZ[7][i]["sozcuk"].rstrip(",").lower()
        s.yazi("fiil%d" % n, LX, RY[n], [(m, KRE)], "Fredoka", 700, LF, S(T(7, i)), 0.3, tur="tik", guc=0.55)
    bxx = LX + gen + 36
    tdf = S(T(7, 5))
    s.yol("sivri", sivri(bxx, 420, 800), tdf - 0.1, 0.5, IKN, 5, 1, "cizgi", 0.55)
    kx, ky, kw, kh = bxx + 34 + 34 + 22, 560, 310, 96
    s.yol("dk", el_kutu_(kx, ky, kw, kh), tdf, 0.5, KRE, 4.2, 1, "cizgi", 0.6)
    tw_ = Y.genislik("Caveat", 700, "durum fiili", 60)
    s.yazi("dtext", kx + (kw - tw_) / 2, ky + 66, [("durum fiili", KRE)], "Caveat", 700, 60, tdf + 0.25, 0.45)
    ing_x, ing_y, ing_f = kx + 10, 850.0, 130
    tg = S(T(7, 7))
    s.yazi("ing", ing_x, ing_y, [("-ing", SAR)], "Fredoka", 700, ing_f, tg, 0.3, tur="tik", guc=0.6)
    iw = Y.genislik("Fredoka", 700, "-ing", ing_f)
    ta = S(T(7, 8))
    s.yol("ikx1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (ing_x - 14, ing_y - 96, ing_x + iw / 2, ing_y - 40,
                                                      ing_x + iw + 14, ing_y + 12), ta, 0.28, KRE, 9, 1, "cizgi", 0.7)
    s.yol("ikx2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (ing_x + iw + 14, ing_y - 96, ing_x + iw / 2, ing_y - 46,
                                                      ing_x - 14, ing_y + 12), ta + 0.26, 0.28, KRE, 9, 1, "cizgi", 0.7)
    s.yazi("almaz", ing_x + 20, ing_y + 72, [("almaz", IKN)], "Caveat", 700, 56, ta + 0.5, 0.4, tur="tik",
           guc=0.45)

    # ---------------- sağ sütun ----------------
    RX = 960.0
    # R1: I know the answer. (66,81–68,33)
    yer = kelimeler(s, "ik", RX, 215, (9, 10, 11, 12), 7, "Fredoka", 700, 72)
    s.yol("kh", el_daire(yer[1][0] + yer[1][1] / 2, 215 - 26, yer[1][1] / 2 + 9, 52, 2.0), S(T(7, 10)), 0.4, SAR,
          7, 0.85, "parilti", 0.5)
    # R2: köprü (68,58–73,14)
    A_Y, B_Y, C_Y = 330, 420, 520
    ta = S(T(7, 14))
    ax, aw = s.yazi("br", RX, A_Y, [("bili", KRE), ("yor", SAR), ("-um", KRE)], "Caveat", 700, 64, ta, 0.5)
    s.yol("brok", el_ok(ax + aw + 40, A_Y - 22, ax + aw + 190, A_Y - 22), S(T1(7, 15)), 0.3, SAR, 7, 0.9, "cizgi", 0.5)
    ix = ax + aw + 214
    s.yazi("brik", ix, A_Y, [("I know", KRE)], "Fredoka", 700, 64, S(T(7, 16)), 0.3, tur="tik")
    s.yol("brk", el_daire(ix + Y.genislik("Fredoka", 700, "I know", 64) / 2, A_Y - 22, 112, 50, 1.4), S(T(7, 16)) + 0.3,
          0.4, SAR, 6, 0.85, "parilti", 0.5)
    pa = [("Türkçede ", KRE), ("-yor", SAR), (" var,", KRE)]
    pb = [(" İngilizcede ", KRE), ("-ing", SAR), (" yok", KRE)]
    nx, nw = s.yazi("nota", RX, B_Y, pa, "Caveat", 700, 52, S(T(7, 15)), 0.5, tur="tik")
    s.yazi("notb", nx + nw, B_Y, pb, "Caveat", 700, 52, S(T(7, 17)), 0.7, tur="tik")
    kxx = RX
    s.yazi("kn1", kxx, C_Y, [("know", KRE)], "Fredoka", 700, 64, S(T(7, 17)) + 0.2, 0.25, tur="tik")
    kw1 = Y.genislik("Fredoka", 700, "know", 64)
    s.yazi("kn2", kxx + kw1, C_Y, [("-ing", SAR)], "Fredoka", 700, 64, S(T(7, 18)), 0.25, tur="tik")
    kw2 = Y.genislik("Fredoka", 700, "-ing", 64)
    s.yol("kst", el_cizgi_(kxx - 10, C_Y - 22, kxx + kw1 + kw2 + 12, C_Y - 24), S(T(7, 19)), 0.35, KRE, 8, 1,
          "cizgi", 0.65)
    # R3: He is always losing his keys. (73,39–75,87)
    h1 = kelimeler(s, "he", RX, 650, (20, 21, 22), 7, "Fredoka", 700, 60)
    h2 = kelimeler(s, "hf", RX, 722, (23, 24, 25), 7, "Fredoka", 700, 60)
    s.yol("alw", el_cizgi_(h1[2][0] - 4, 650 + 16, h1[2][0] + h1[2][1] + 4, 650 + 14), S(T(7, 22)) + 0.1, 0.35, SAR,
          8, 0.9, "cizgi", 0.5)
    s.yol("los", el_daire(h2[0][0] + h2[0][1] / 2, 722 - 22, h2[0][1] / 2 + 22, 46, 0.8), S(T(7, 23)), 0.35, SAR, 6,
          0.85, "parilti", 0.5)
    s.figur("standing-5", "kz", 1640, 540, 440, S(T(7, 20)) + 0.05, S(T(7, 20)) + 1.6, 3.4)
    tun = S(T1(7, 25)) - 0.55
    s.yol("un1", "M1604 582 Q1598 612 1600 640", tun, 0.25, KRE, 9, 1, "cizgi", 0.6)
    s.yol("un2", "M1600 662 L1601 664", tun + 0.22, 0.08, KRE, 11, 1, "cizgi", 0.5)
    for k, (dx, dy, ex, ey) in enumerate(((1632, 570, 1618, 552), (1636, 604, 1616, 604), (1632, 636, 1618, 654))):
        s.yol("un%d" % (3 + k), "M%d %d L%d %d" % (dx, dy, ex, ey), tun + 0.3 + 0.05 * k, 0.15, SAR, 5, 0.9,
              "cizgi", 0.4)
    # R4: always + V-ing = şikâyet (76,12–79,92)
    Q_Y = 830
    qx = RX
    parc = [("always", KRE, 76.12), (" + ", IKN, T(7, 27)), ("V", KRE, T(7, 28)), ("-ing", SAR, T(7, 28)),
            (" = ", IKN, T(7, 29) - 0.3), ("şikâyet", KRE, T(7, 29))]
    for n, (m, f, t) in enumerate(parc):
        w = Y.genislik("Caveat", 700, m, 60)
        s.yazi("al%d" % n, qx, Q_Y, [(m, f)], "Caveat", 700, 60, S(t), 0.3, tur="tik" if n in (0, 5) else None)
        if n == 5:
            s.yol("alu", el_cizgi_(qx - 4, Q_Y + 16, qx + w + 6, Q_Y + 12), S(t) + 0.25, 0.4, KRE, 6, 1, "cizgi", 0.5)
        qx += w
    # Sınavda ikisi de çıkar (78,96): iki küçük kutu
    for n, (txt, ww, tt, yy) in enumerate((("know / believe / own / belong", 590, T(7, 30), 872),
                                           ("always + V-ing", 340, T(7, 31), 946))):
        s.yol("sk%d" % n, el_kutu_(RX, yy, ww, 62), S(tt), 0.35, IKN, 4, 1, "cizgi", 0.5)
        s.yazi("st%d" % n, RX + 24, yy + 44, [(txt, KRE)], "Fredoka", 700, 34, S(tt) + 0.25, 0.4, tur="tik")
    tc = S(T(7, 33))
    s.yol("sc1", Y.tik_yolu(RX + 620, 876, 44), tc, 0.3, SAR, 8, 0.9, "cizgi", 0.55)
    s.yol("sc2", Y.tik_yolu(RX + 370, 950, 44), tc + 0.2, 0.3, SAR, 8, 0.9, "cizgi", 0.55)

    # ---------------- Kod: olay = -ing / durum ≠ -ing (80,72–83,96) ----------------
    tk = S(T(7, 34))
    s.to("#icerik", tk - 0.5, {"svgOrigin": "90 110", "scale": 0.55, "duration": 0.8, "ease": "power3.inOut"})
    i_kod = len(s.svg)
    s.yazi("kod", 140, 690, [("Kod:", KRE)], "Caveat", 700, 64, tk, 0.4, tur="tik")
    KF, K1, K2 = 150, 840, 990
    ow = Y.genislik("Fredoka", 700, "olay", KF)
    s.yazi("k1a", 140, K1, [("olay", KRE)], "Fredoka", 700, KF, S(T(7, 35)), 0.35, tur="tik", guc=0.6)
    ex = 140 + ow + 34
    te = S(T(7, 35)) + 0.35
    s.yol("e1", el_cizgi_(ex, K1 - 84, ex + 92, K1 - 86, 1), te, 0.2, KRE, 11, 1, "cizgi", 0.6)
    s.yol("e2", el_cizgi_(ex + 2, K1 - 44, ex + 94, K1 - 46, -1), te + 0.2, 0.2, KRE, 11, 1, "cizgi", 0.6)
    s.yazi("k1b", ex + 126, K1, [("-ing", SAR)], "Fredoka", 700, KF, S(T(7, 36)), 0.35, tur="tik", guc=0.6)
    dw = Y.genislik("Fredoka", 700, "durum", KF)
    s.yazi("k2a", 140, K2, [("durum", KRE)], "Fredoka", 700, KF, S(T(7, 38)), 0.35, tur="tik", guc=0.6)
    nx2 = 140 + dw + 34
    tn = S(T(7, 39))
    s.yol("n1", el_cizgi_(nx2, K2 - 84, nx2 + 92, K2 - 86, 1), tn, 0.2, KRE, 11, 1, "cizgi", 0.6)
    s.yol("n2", el_cizgi_(nx2 + 2, K2 - 44, nx2 + 94, K2 - 46, -1), tn + 0.2, 0.2, KRE, 11, 1, "cizgi", 0.6)
    s.yol("n3", "M%.1f %.1f L%.1f %.1f" % (nx2 + 72, K2 - 118, nx2 + 22, K2 + 6), tn + 0.4, 0.2, KRE, 11, 1, "cizgi",
          0.7)
    s.yazi("k2b", nx2 + 126, K2, [("-ing", SAR)], "Fredoka", 700, KF, tn + 0.55, 0.3, tur="tik", guc=0.6)
    # formül kartı el kutusunda toplanır (83,96)
    tf = S(T1(7, 39))
    CX, CY, CW, CH = 1180, 716, 650, 120
    s.yol("kart", el_kutu_(CX, CY, CW, CH), tf, 0.5, KRE, 4.5, 1, "cizgi", 0.7)
    parc = [("am / is / are", KRE), ("  +  ", IKN), ("V", KRE), ("-ing", SAR)]
    tw = sum(Y.genislik("Fredoka", 700, p[0], 52) for p in parc)
    cx0 = CX + (CW - tw - 70) / 2
    pa_ = Y.genislik("Fredoka", 700, parc[0][0], 52)
    pp_ = Y.genislik("Fredoka", 700, parc[1][0], 52)
    s.yazi("c1", cx0, CY + 76, [parc[0]], "Fredoka", 700, 52, tf + 0.1, 0.3, tur="tik", guc=0.5)
    s.yazi("c2", cx0 + pa_, CY + 76, [parc[1]], "Fredoka", 700, 52, tf + 0.3, 0.15, tur=None)
    s.yazi("c3", cx0 + pa_ + pp_, CY + 76, [parc[2], parc[3]], "Fredoka", 700, 52, tf + 0.4, 0.3, tur="tik", guc=0.6)
    s.yol("ctk", Y.tik_yolu(CX + CW - 74, CY + 36, 44), tf + 0.7, 0.3, SAR, 8, 0.9, "cizgi", 0.55)
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


def el_cizgi_(x0, y0, x1, y1, egim=3.0):
    return Y.el_cizgi(x0, y0, x1, y1, egim)


def el_kutu_(x, y, w, h):
    return Y.el_kutu(x, y, w, h)


def el_daire(cx, cy, rx, ry, kayma=0.0):
    return Y.el_daire(cx, cy, rx, ry, kayma)


def el_ok(x0, y0, x1, y1, egim=2.0):
    return Y.el_ok(x0, y0, x1, y1, egim)


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34),
               bal_ids=parca["bal_ids"], dis=parca["dis"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

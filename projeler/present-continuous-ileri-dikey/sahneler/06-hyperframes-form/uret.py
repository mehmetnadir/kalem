"""Sahne 06 DİKEY (İLERİ, 1080x1920): öğrenci sorusu + durum fiilleri + always şikâyeti + kod.
Yerleşim BRIEF-DIKEY §2-§4: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform bandı boş.
Bölümler sırayla çalışır; biten bölüm yer açmak için tek satırlık özete (çip, Fredoka 48) toplanır:
  balon (üst, ölçek 0,75) -> bölüm 1 liste -> çip 1 -> bölüm 2 köprü -> çip 2 -> bölüm 3 şikâyet -> çip 3 -> kod.
Tek kaynak: ortak/anlatim/{sozcukler,altyazi}.json (küresel sn) + zamanlar.json. Yerel sn = t - t_bas."""
import json
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
ANL = AD / ".." / ".." / "ortak" / "anlatim"
SOZ = {c: [w for w in json.loads((ANL / "sozcukler.json").read_text()) if w["cumle"] == c] for c in (6, 7)}
ALT = [a for a in json.loads((ANL / "altyazi.json").read_text()) if a["cumle"] in (6, 7)]
R = Y.RENK
KRE, IKN, SAR, KIR = R["murekkep"], R["ikincil"], R["vurgu"], R["kirmizi"]
TB = Z["t_bas"]
X0 = 48.0


def T(c, i):
    return SOZ[c][i]["t0"]


def T1(c, i):
    return SOZ[c][i]["t1"]


def kimlikler(s, bas):
    """s.svg[bas:] elemanlarının üst düzey id listesi (bölüm grubu için)."""
    return {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}


def kelimeler(s, kimlik, x, y, idx, c, aile, agr, boy, renk=KRE):
    """Sözcükleri konuşma zamanında tek tek açar. Döner: [(x, w)]."""
    sp = Y.genislik(aile, agr, " ", boy)
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


def topla(s, grup, t, cx, cy, hx, hy, sure=0.5):
    """Bölüm grubunu çip konumuna (hx, hy) küçülterek toplar (merkez cx, cy)."""
    s.to("#" + grup, t, {"svgOrigin": "%.0f %.0f" % (cx, cy), "x": round(hx - cx, 1), "y": round(hy - cy, 1),
                         "scale": 0.3, "opacity": 0, "duration": sure, "ease": "power3.in"})


def uret():
    s = Y.Sahne(TB)
    S = s.S
    bal_ids = []
    # ---------------- öğrenci başı (peeps-kit, 160 px) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.484, 63.0, 535.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.3f)" fill="none" stroke="%s" '
                 'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (
                     BTX, BTY, BS, KRE, 3.6 / BS, "".join(
                         '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = max(S(T(6, 0)) - 0.14, 0.42)
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu: 3 satır Caveat 64 ----------------
    BF, BX, BASE = 64, 280.0, (456, 536, 616)
    sp = Y.genislik("Caveat", 700, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6, 7, 8), (9, 10))
    gens = [sum(Y.genislik("Caveat", 700, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = min(1032.0, BX + max(gens) + 40)
    s.yol("bal", Y.balon_sol(240, 372, x1b, 652, 176, 590), t0 + 0.1, 0.55, KRE, 4.6, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    pos = {}
    for sat, base in zip(satir, BASE):
        x = BX
        for i in sat:
            m = SOZ[6][i]["sozcuk"]
            w = Y.genislik("Caveat", 700, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Caveat", 700, BF, S(T(6, i)), 0.12,
                   tur="tik" if i in (0, 4, 9) else None)
            bal_ids.append("bw%d" % i)
            pos[i] = (x, w, base)
            x += w + sp
    xa, xb = pos[4][0], pos[6][0] + pos[6][1]
    s.yol("bm", Y.el_cizgi(xa - 2, BASE[1] + 14, xb + 2, BASE[1] + 11), S(T(6, 6)), 0.4, SAR, 10, 0.85, "cizgi", 0.5)
    bal_ids.append("bm")
    # 60,40 Olmaz.: yanlış cümle (I am knowing the answer) üstüne kırmızı kalem çarpısı
    xe = pos[8][0] + pos[8][1]
    tx = S(T(7, 0))
    s.yol("xk1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xa - 14, BASE[1] - 50, (xa + xe) / 2, BASE[1] - 8, xe + 14,
                                                       BASE[1] + 22), tx, 0.3, KIR, 11, 1, "cizgi", 0.7)
    s.yol("xk2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xe + 14, BASE[1] - 50, (xa + xe) / 2, BASE[1] - 14, xa - 14,
                                                       BASE[1] + 22), tx + 0.3, 0.3, KIR, 11, 1, "cizgi", 0.7)
    s.olay(tx + 0.3, "vurus", 0.85)
    bal_ids += ["xk1", "xk2"]
    s.to("#ku-bolum", tx, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tx, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    # balon + baş yukarı toplanır (ölçek 0,75: metin 48 px)
    s.to("#balg", S(61.25), {"svgOrigin": "48 372", "scale": 0.75, "duration": 0.7, "ease": "power3.inOut"})

    # ---------------- bölüm 1: durum fiilleri listesi (61,60–66,56) ----------------
    i0 = len(s.svg)
    LF = 96
    RY = (790, 890, 990, 1090)
    gen = max(Y.genislik("Fredoka", 700, SOZ[7][i]["sozcuk"].rstrip(",").lower(), LF) for i in (1, 2, 3, 4))
    for n, i in enumerate((1, 2, 3, 4)):
        m = SOZ[7][i]["sozcuk"].rstrip(",").lower()
        s.yazi("fiil%d" % n, X0, RY[n], [(m, KRE)], "Fredoka", 700, LF, S(T(7, i)), 0.3, tur="tik", guc=0.55)
    bxx = X0 + gen + 30
    tdf = S(T(7, 5))
    s.yol("sivri", sivri(bxx, 718, 1112), tdf - 0.1, 0.5, IKN, 6, 1, "cizgi", 0.55)
    kx = bxx + 68 + 22
    kw, kh, ky = 1032 - kx, 100, 865
    s.yol("dk", Y.el_kutu(kx, ky, kw, kh), tdf, 0.5, KRE, 4.6, 1, "cizgi", 0.6)
    tw_ = Y.genislik("Caveat", 700, "durum fiili", 64)
    s.yazi("dtext", kx + (kw - tw_) / 2, ky + 70, [("durum fiili", KRE)], "Caveat", 700, 64, tdf + 0.25, 0.45)
    ing_f = 150
    iw = Y.genislik("Fredoka", 700, "-ing", ing_f)
    ing_x, ing_y = kx + (kw - iw) / 2, 1115.0
    s.yazi("ing", ing_x, ing_y, [("-ing", SAR)], "Fredoka", 700, ing_f, S(T(7, 7)), 0.3, tur="tik", guc=0.6)
    ta = S(T(7, 8))
    s.yol("ikx1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (ing_x - 16, ing_y - 110, ing_x + iw / 2, ing_y - 46,
                                                      ing_x + iw + 16, ing_y + 14), ta, 0.28, KRE, 11, 1, "cizgi", 0.7)
    s.yol("ikx2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (ing_x + iw + 16, ing_y - 110, ing_x + iw / 2, ing_y - 52,
                                                      ing_x - 16, ing_y + 14), ta + 0.26, 0.28, KRE, 11, 1, "cizgi",
          0.7)
    aw = Y.genislik("Caveat", 700, "almaz", 72)
    s.yazi("almaz", ing_x + (iw - aw) / 2, ing_y + 90, [("almaz", KRE)], "Caveat", 700, 72, ta + 0.08, 0.3, tur="tik",
           guc=0.45)
    g1 = kimlikler(s, i0)
    # çip 1 (66,62): know · believe · own · belong  -ing (çizili)
    C1, C2, C3 = 676, 748, 820
    tc1 = S(66.5)
    topla(s, "s1", tc1, 540, 930, 360, C1 - 16, 0.35)
    c1 = [("know · believe · own · belong ", KRE), ("-ing", SAR)]
    c1x, c1w = s.yazi("c1", X0, C1, c1, "Fredoka", 700, 48, tc1 + 0.2, 0.4, tur="tik", guc=0.5)
    wl = Y.genislik("Fredoka", 700, c1[0][0], 48)
    wi = Y.genislik("Fredoka", 700, "-ing", 48)
    s.yol("c1k", Y.el_cizgi(X0 + wl - 6, C1 - 14, X0 + wl + wi + 6, C1 - 16, 1), tc1 + 0.6, 0.25, KRE, 6, 1,
          "cizgi", 0.5)

    # ---------------- bölüm 2: I know the answer + köprü (66,81–73,14) ----------------
    i0 = len(s.svg)
    yer = kelimeler(s, "ik", X0, 860, (9, 10, 11, 12), 7, "Fredoka", 700, 80)
    s.yol("kh", Y.el_daire(yer[1][0] + yer[1][1] / 2, 860 - 28, yer[1][1] / 2 + 9, 58, 2.0), S(T(7, 10)), 0.4, SAR,
          9, 0.85, "parilti", 0.5)
    A_Y = 990
    ax, aw2 = s.yazi("br", X0, A_Y, [("bili", KRE), ("yor", SAR), ("-um", KRE)], "Caveat", 700, 72,
                     S(T(7, 14)), 0.5)
    s.yol("brok", Y.el_ok(ax + aw2 + 36, A_Y - 26, ax + aw2 + 170, A_Y - 26), S(T1(7, 15)), 0.3, SAR, 9, 0.9, "cizgi",
          0.5)
    ix = ax + aw2 + 200
    s.yazi("brik", ix, A_Y, [("I know", KRE)], "Fredoka", 700, 72, S(T(7, 16)), 0.3, tur="tik")
    iwk = Y.genislik("Fredoka", 700, "I know", 72)
    s.yol("brk", Y.el_daire(ix + iwk / 2, A_Y - 26, iwk / 2 + 26, 56, 1.4), S(T(7, 16)) + 0.3, 0.4, SAR, 8, 0.85,
          "parilti", 0.5)
    pa = [("Türkçede ", KRE), ("-yor", SAR), (" var,", KRE)]
    pb = [("İngilizcede ", KRE), ("-ing", SAR), (" yok", KRE)]
    s.yazi("nota", X0, 1100, pa, "Caveat", 700, 64, S(T(7, 15)), 0.5, tur="tik")
    s.yazi("notb", X0, 1180, pb, "Caveat", 700, 64, S(T(7, 17)), 0.6, tur="tik")
    s.yazi("kn1", X0, 1290, [("know", KRE)], "Fredoka", 700, 80, S(T(7, 17)) + 0.25, 0.25, tur="tik")
    kw1 = Y.genislik("Fredoka", 700, "know", 80)
    s.yazi("kn2", X0 + kw1, 1290, [("-ing", SAR)], "Fredoka", 700, 80, S(T(7, 18)), 0.25, tur="tik")
    kw2 = Y.genislik("Fredoka", 700, "-ing", 80)
    s.yol("kst", Y.el_cizgi(X0 - 10, 1290 - 28, X0 + kw1 + kw2 + 12, 1290 - 32), S(T(7, 19)), 0.35, KRE, 10, 1,
          "cizgi", 0.65)
    g2 = kimlikler(s, i0)
    tc2 = S(72.55)
    topla(s, "s2", tc2, 540, 1075, 300, C2 - 16, 0.4)
    c2 = [("bili", KRE), ("yor", SAR), ("-um = I know   ", KRE), ("know", KRE), ("-ing", SAR)]
    s.yazi("c2", X0, C2, c2, "Fredoka", 700, 48, tc2 + 0.2, 0.4, tur="tik", guc=0.5)
    wk = sum(Y.genislik("Fredoka", 700, p[0], 48) for p in c2[:4])
    wi2 = Y.genislik("Fredoka", 700, "-ing", 48)
    s.yol("c2k", Y.el_cizgi(X0 + wk - 6, C2 - 14, X0 + wk + wi2 + 6, C2 - 16, 1), tc2 + 0.6, 0.25, KRE, 6, 1,
          "cizgi", 0.5)

    # ---------------- bölüm 3: He is always losing his keys + always + V-ing = şikâyet ----------------
    i0 = len(s.svg)
    h1 = kelimeler(s, "he", X0, 930, (20, 21, 22), 7, "Fredoka", 700, 72)
    h2 = kelimeler(s, "hf", X0, 1020, (23, 24, 25), 7, "Fredoka", 700, 72)
    s.yol("alw", Y.el_cizgi(h1[2][0] - 4, 930 + 18, h1[2][0] + h1[2][1] + 4, 930 + 16), S(T(7, 22)) + 0.1, 0.35, SAR,
          10, 0.9, "cizgi", 0.5)
    s.yol("los", Y.el_daire(h2[0][0] + h2[0][1] / 2, 1020 - 26, h2[0][1] / 2 + 8, 52, 0.8), S(T(7, 23)), 0.35, SAR,
          8, 0.85, "parilti", 0.5)
    sc, fw = s.figur("standing-5", "kz", 1032 - 190, 850, 410, S(T(7, 20)) + 0.05, S(T(7, 20)) + 1.6, 4.4)
    fx = 1032 - fw - 12
    tun = S(T1(7, 25)) - 0.55
    s.yol("un1", "M%.0f 880 Q%.0f 920 %.0f 962" % (fx - 30, fx - 36, fx - 34), tun, 0.25, KRE, 10, 1, "cizgi", 0.6)
    s.yol("un2", "M%.0f 992 L%.0f 994" % (fx - 33, fx - 33), tun + 0.22, 0.08, KRE, 13, 1, "cizgi", 0.5)
    for k, (dx, dy, ex, ey) in enumerate(((fx - 8, 886, fx - 22, 866), (fx - 4, 922, fx - 24, 922),
                                          (fx - 8, 958, fx - 22, 978))):
        s.yol("un%d" % (3 + k), "M%d %d L%d %d" % (dx, dy, ex, ey), tun + 0.3 + 0.05 * k, 0.15, SAR, 6, 0.9, "cizgi",
              0.4)
    Q_Y = 1180
    qx = X0
    parc = [("always", KRE, T(7, 26)), (" + ", IKN, T(7, 27)), ("V", KRE, T(7, 28)), ("-ing", SAR, T(7, 28)),
            (" = ", IKN, T(7, 29) - 0.3), ("şikâyet", KRE, T(7, 29))]
    ust = []
    for n, (m, f, t) in enumerate(parc):
        w = Y.genislik("Caveat", 700, m, 72)
        s.yazi("al%d" % n, qx, Q_Y, [(m, f)], "Caveat", 700, 72, S(t), 0.3, tur="tik" if n in (0, 5) else None)
        ust.append((qx, w))
        if n == 5:
            s.yol("alu", Y.el_cizgi(qx - 4, Q_Y + 18, qx + w + 6, Q_Y + 14), S(t) + 0.25, 0.4, KRE, 7, 1, "cizgi", 0.5)
        qx += w
    # 78,96 Sınavda ikisi de çıkar: iki kutu (çip 1 ve always + V-ing) + onay
    tb = S(T(7, 30))
    s.yol("bkA", Y.el_kutu(X0 - 14, C1 - 52, c1w + 28, 70), tb, 0.4, SAR, 5, 0.95, "cizgi", 0.5)
    bkx0, bkx1 = ust[0][0] - 12, ust[3][0] + ust[3][1] + 12
    s.yol("bkB", Y.el_kutu(bkx0, Q_Y - 62, bkx1 - bkx0, 96), S(T(7, 31)), 0.4, SAR, 5, 0.95, "cizgi", 0.5)
    tc = S(T(7, 33))
    s.yol("sc1", Y.tik_yolu(X0 + c1w + 24, C1 - 60, 44), tc, 0.3, SAR, 9, 0.9, "cizgi", 0.55)
    s.yol("sc2", Y.tik_yolu(bkx1 + 16, Q_Y - 58, 44), tc + 0.2, 0.3, SAR, 9, 0.9, "cizgi", 0.55)
    g3 = kimlikler(s, i0) - {"bkA", "sc1"}
    tk = S(T(7, 34))
    tc3 = tk - 0.55
    topla(s, "s3", tc3, 540, 1050, 300, C3 - 16)
    c3 = [("always + V", KRE), ("-ing", SAR), (" = şikâyet", KRE)]
    s.yazi("c3", X0, C3, c3, "Fredoka", 700, 48, tc3 + 0.2, 0.4, tur="tik", guc=0.5)

    # ---------------- bölüm 4: Kod: olay = -ing / durum ≠ -ing (80,72–83,96) ----------------
    s.yazi("kod", X0, 915, [("Kod:", KRE)], "Caveat", 700, 72, tk, 0.4, tur="tik")
    KF, K1, K2 = 150, 1060, 1210
    ow = Y.genislik("Fredoka", 700, "olay", KF)
    s.yazi("k1a", X0, K1, [("olay", KRE)], "Fredoka", 700, KF, S(T(7, 35)), 0.35, tur="tik", guc=0.6)
    ex = X0 + ow + 30
    te = S(T(7, 35)) + 0.35
    s.yol("e1", Y.el_cizgi(ex, K1 - 84, ex + 88, K1 - 86, 1), te, 0.2, KRE, 12, 1, "cizgi", 0.6)
    s.yol("e2", Y.el_cizgi(ex + 2, K1 - 44, ex + 90, K1 - 46, -1), te + 0.2, 0.2, KRE, 12, 1, "cizgi", 0.6)
    s.yazi("k1b", ex + 120, K1, [("-ing", SAR)], "Fredoka", 700, KF, S(T(7, 36)), 0.35, tur="tik", guc=0.6)
    dw = Y.genislik("Fredoka", 700, "durum", KF)
    s.yazi("k2a", X0, K2, [("durum", KRE)], "Fredoka", 700, KF, S(T(7, 38)), 0.35, tur="tik", guc=0.6)
    nx2 = X0 + dw + 30
    tn = S(T(7, 39))
    s.yol("n1", Y.el_cizgi(nx2, K2 - 84, nx2 + 88, K2 - 86, 1), tn, 0.2, KRE, 12, 1, "cizgi", 0.6)
    s.yol("n2", Y.el_cizgi(nx2 + 2, K2 - 44, nx2 + 90, K2 - 46, -1), tn + 0.2, 0.2, KRE, 12, 1, "cizgi", 0.6)
    s.yol("n3", "M%.1f %.1f L%.1f %.1f" % (nx2 + 70, K2 - 118, nx2 + 20, K2 + 6), tn + 0.4, 0.2, KRE, 12, 1, "cizgi",
          0.7)
    s.yazi("k2b", nx2 + 120, K2, [("-ing", SAR)], "Fredoka", 700, KF, tn + 0.55, 0.3, tur="tik", guc=0.6)
    # formül kartı el kutusunda toplanır (83,96) + Next lesson
    tf = S(T1(7, 39))
    CW, CH, CY = 860, 104, 1250
    CX = (1080 - CW) / 2
    s.yol("kart", Y.el_kutu(CX, CY, CW, CH), tf, 0.5, KRE, 5, 1, "cizgi", 0.7)
    parc = [("am / is / are", KRE), ("  +  ", IKN), ("V", KRE), ("-ing", SAR)]
    tw = sum(Y.genislik("Fredoka", 700, p[0], 56) for p in parc)
    cx0 = CX + (CW - tw - 70) / 2
    pa_ = Y.genislik("Fredoka", 700, parc[0][0], 56)
    pp_ = Y.genislik("Fredoka", 700, parc[1][0], 56)
    s.yazi("cf1", cx0, CY + 74, [parc[0]], "Fredoka", 700, 56, tf + 0.1, 0.3, tur="tik", guc=0.5)
    s.yazi("cf2", cx0 + pa_, CY + 74, [parc[1]], "Fredoka", 700, 56, tf + 0.3, 0.15, tur=None)
    s.yazi("cf3", cx0 + pa_ + pp_, CY + 74, [parc[2], parc[3]], "Fredoka", 700, 56, tf + 0.4, 0.3, tur="tik",
           guc=0.6)
    s.yol("ctk", Y.tik_yolu(CX + CW - 76, CY + 28, 44), tf + 0.7, 0.3, SAR, 9, 0.9, "cizgi", 0.55)
    s.olay(tf + 0.7, "vurus", 0.8)
    nw = Y.genislik("Lexend", 700, "Next lesson", 36)
    tn2 = tf + 0.6
    s.yazi("nx", 1032 - nw - 56, 1384, [("Next lesson", KRE)], "Lexend", 700, 36, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M%.1f 1372 L%.1f 1372 M%.1f 1362 L%.1f 1372 L%.1f 1382" % (1032 - 46, 1032 - 6, 1032 - 18,
                                                                                1032 - 6, 1032 - 18), tn2 + 0.3,
          0.25, KRE, 4, 1, "cizgi", 0.4)
    # ---------------- altyazı: konuşulan parça (kunye.js altyaziMetin ile aynı pencere) ----------------
    parcalar = [{"id": "alt%d" % i, "metin": a["metin"]} for i, a in enumerate(ALT)]
    for i, a in enumerate(ALT):
        ac = S(a["t0"]) - 0.05
        kapa = S(a["t1"]) + 0.35
        if i + 1 < len(ALT):
            kapa = min(kapa, S(ALT[i + 1]["t0"]) - 0.05)
        s.set("#alt%d" % i, max(0.0, ac), {"opacity": 1})
        if i + 1 < len(ALT):
            s.set("#alt%d" % i, kapa, {"opacity": 0})
    kun = Y.kunye_svg("Question", "Form")
    return s, {"kun": kun, "bal_ids": bal_ids, "gruplar": [("s1", g1), ("s2", g2), ("s3", g3)],
               "altyazi": Y.altyazi_svg(parcalar)}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    logo = (48, 48, 96 * Y.LOGO_EN_BOY, 96)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), parca["kun"], None, logo, ek=parca["altyazi"],
               bal_ids=parca["bal_ids"], vin=1150, gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

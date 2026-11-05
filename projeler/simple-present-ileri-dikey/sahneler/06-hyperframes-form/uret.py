"""Sahne 06 DİKEY (SIMPLE PRESENT İLERİ, 1080x1920): öğrenci sorusu + tarife/will + durum fiilleri + kod.
Yerleşim BRIEF-DIKEY §2-§4: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform bandı boş.
Bölümler sırayla çalışır; biten bölüm yer açmak için tek satırlık özete (çip, Fredoka 48) toplanır:
  balon + baş (üst, ölçek 0,75) -> bölüm A/B1 (soru, tarife) -> çip 1 -> bölüm B2 (will) -> çip 2
  -> bölüm B3 (durum fiilleri) -> çip 3 -> bölüm C (kod: iki büyük satır çifti).
Tek kaynak: ortak/anlatim/{sozcukler,altyazi}.json (küresel sn) + zamanlar.json. Yerel sn = t - t_bas.
Fredoka ğ ş İ taşımaz: Türkçe özel harfli metin Caveat ile yazılır; oklar el çizimidir (Fredoka -> yok)."""
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


def T(c, i, beklenen=None):
    """Sözcük başlangıcı (küresel sn); beklenen verilirse sözcük sırası doğrulanır."""
    if beklenen:
        assert SOZ[c][i]["sozcuk"].lower().startswith(beklenen.lower()), (c, i, SOZ[c][i]["sozcuk"], beklenen)
    return SOZ[c][i]["t0"]


def kimlikler(s, bas):
    """s.svg[bas:] elemanlarının üst düzey id kümesi (bölüm grubu için)."""
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


def topla(s, grup, t, cx, cy, hx, hy, sure=0.4):
    """Bölüm grubunu çip konumuna (hx, hy) küçülterek toplar (merkez cx, cy)."""
    s.to("#" + grup, t, {"svgOrigin": "%.0f %.0f" % (cx, cy), "x": round(hx - cx, 1), "y": round(hy - cy, 1),
                         "scale": 0.3, "opacity": 0, "duration": sure, "ease": "power3.in"})


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


def etiket(s, kimlik, x, yb, metin, t, boy=80, kutu_renk=IKN):
    """El kutulu etiket: kutu çizilir, sonra yazı. Döner: sağ kenar x."""
    w = Y.genislik("Fredoka", 700, metin, boy)
    s.yol(kimlik + "k", Y.el_kutu(x, yb - boy * 0.95, w + 56, boy * 1.35), t - 0.05, 0.3, kutu_renk, 5, 1,
          "cizgi", 0.5)
    s.yazi(kimlik, x + 28, yb, [(metin, KRE)], "Fredoka", 700, boy, t + 0.12, 0.3, tur="tik", guc=0.55)
    return x + w + 56


def uret():
    s = Y.Sahne(TB)
    S = s.S
    bal_ids = []
    # ---------------- öğrenci başı (peeps-kit, 270 px) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.82, 85.0, 372.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.3f)" fill="none" stroke="%s" '
                 'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (
                     BTX, BTY, BS, KRE, 4.2 / BS, "".join(
                         '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = max(S(T(6, 0)) - 0.14, 0.42)          # soğuk açılış: ilk 12 kare (0,40 sn) boş
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu: 2 satır Caveat 64 ----------------
    BF, BX, BASE = 64, 330.0, (462, 548)
    sp = Y.genislik("Caveat", 700, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6, 7, 8))
    gens = [sum(Y.genislik("Caveat", 700, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = min(1032.0, BX + max(gens) + 40)
    s.yol("bal", Y.balon_sol(290, 372, x1b, 596, 250, 545), t0 + 0.1, 0.55, KRE, 4.6, 1, "cizgi", 0.7)
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
    xa, xb = pos[4][0], pos[6][0] + pos[6][1]
    s.yol("bm", Y.el_cizgi(xa - 2, BASE[1] + 14, xb + 2, BASE[1] + 11), S(T(6, 6, "off")), 0.4, SAR, 10, 0.85,
          "cizgi", 0.5)
    bal_ids.append("bm")
    # soru anı: takvim (yarın) ve sözü; Hayır'dan sonra söner
    tcal = S(T(6, 1, "yar"))
    ikon(s, "calendar", "cal", 110, 690, 270, tcal, tcal + 0.8, 5.0, KRE)
    s.yazi("caln", 440, 880, [("yarın", KRE)], "Caveat", 700, 120, tcal + 0.5, 0.4, tur="tik", guc=0.5)
    for kim in ("cal", "caln"):
        s.to("#" + kim, S(66.95), {"opacity": 0, "duration": 0.4, "ease": "power1.in"})
    # balon + baş yukarı toplanır (ölçek 0,75)
    s.to("#balg", S(66.95), {"svgOrigin": "48 372", "scale": 0.75, "duration": 0.7, "ease": "power3.inOut"})

    # ---------------- bölüm A+B1: will take off ? -> Hayır: ✗ will -> tarife -> Simple Present, takes off ✓ ----
    i1 = len(s.svg)
    PF, PY = 150, 1180.0
    sp2 = Y.genislik("Fredoka", 700, " ", PF)
    gw = [Y.genislik("Fredoka", 700, SOZ[6][i]["sozcuk"], PF) for i in (4, 5, 6)]
    cx, pp = X0, []
    for n, i in enumerate((4, 5, 6)):
        m = SOZ[6][i]["sozcuk"]
        s.yazi("pw%d" % n, cx, PY, [(m, KRE)], "Fredoka", 700, PF, S(T(6, i)), 0.15, tur="tik" if n == 0 else None)
        pp.append((cx, gw[n]))
        cx += gw[n] + sp2
    s.yazi("pq", cx - sp2 + 12, PY + 10, [("? ", SAR)], "Caveat", 700, 200, S(T(6, 7, "olmaz")), 0.3, tur="tik",
           guc=0.6)
    tx = S(T(7, 0, "Hay"))
    wx, ww = pp[0]
    s.yol("xk1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (wx - 18, PY - 140, wx + ww / 2, PY - 56, wx + ww + 18, PY + 22),
          tx, 0.3, KIR, 13, 1, "cizgi", 0.7)
    s.yol("xk2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (wx + ww + 18, PY - 140, wx + ww / 2, PY - 62, wx - 18, PY + 22),
          tx + 0.3, 0.3, KIR, 13, 1, "cizgi", 0.7)
    s.olay(tx + 0.3, "vurus", 0.85)
    s.to("#ku-bolum", tx, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tx, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    # tarife · program · takvim -> Simple Present kutusu (67,31–70,99)
    LF = 96
    RY = (760, 860, 960)
    adlar = [SOZ[7][i]["sozcuk"].rstrip(",").lower() for i in (1, 2, 3)]
    gen = max(Y.genislik("Fredoka", 700, a, LF) for a in adlar)
    for n, i in enumerate((1, 2, 3)):
        s.yazi("lf%d" % n, X0, RY[n], [(adlar[n], KRE)], "Fredoka", 700, LF, S(T(7, i)), 0.3, tur="tik", guc=0.55)
    bxx = X0 + gen + 30
    tkes = S(T(7, 4, "kesinse"))
    s.yol("lsiv", sivri(bxx, 680, 985), tkes, 0.5, IKN, 6, 1, "cizgi", 0.55)
    kx, ky = bxx + 68 + 22, 788.0
    bt = "Simple Present"
    bw_ = Y.genislik("Fredoka", 700, bt, 64)
    tsp = S(T(7, 5, "Simple"))
    s.yol("lbox", Y.el_kutu(kx, ky, min(bw_ + 60, 1030 - kx), 104), tsp, 0.5, SAR, 6, 1, "cizgi", 0.6)
    s.yazi("ltxt", kx + 30, ky + 72, [(bt, KRE)], "Fredoka", 700, 64, tsp + 0.25, 0.5, tur="tik", guc=0.55)
    # 70,40 takes off ✓ (mürekkep)
    tkk = S(70.4)
    s.yazi("to1", X0, PY + 150, [("takes off", KRE)], "Fredoka", 700, PF, tkk, 0.3, tur="tik", guc=0.6)
    tw_ = Y.genislik("Fredoka", 700, "takes off", PF)
    s.yol("tot", Y.tik_yolu(X0 + tw_ + 40, PY + 150 - 120, 100), tkk + 0.35, 0.3, KRE, 14, 1, "cizgi", 0.55)
    s.olay(tkk + 0.4, "vurus", 0.8)
    g1 = kimlikler(s, i1)
    C1, C2, C3 = 660, 732, 804
    tc1 = S(70.95)
    topla(s, "s1", tc1, 540, 1000, 360, C1 - 18, 0.35)
    c1 = [("tarife = ", KRE), ("Simple Present", SAR)]
    s.yazi("c1", X0, C1, c1, "Fredoka", 700, 56, tc1 + 0.2, 0.4, tur="tik", guc=0.5)

    # ---------------- bölüm B2: will = predictions · sudden decisions (71,24–74,55) ----------------
    i2 = len(s.svg)
    tw0 = S(T(7, 7, "Will"))
    s.yazi("wl", X0, 930, [("will", KRE)], "Fredoka", 700, 150, tw0, 0.3, tur="tik", guc=0.6)
    ww_ = Y.genislik("Fredoka", 700, "will", 150)
    s.yazi("we", X0 + ww_ + 30, 930, [("=", IKN)], "Fredoka", 700, 150, S(T(7, 8, "is")), 0.2, tur=None)
    etiket(s, "e1", X0, 1075, "predictions", S(T(7, 10, "predictions")))
    etiket(s, "e2", X0, 1225, "sudden decisions", S(T(7, 12, "sudden")))
    g2 = kimlikler(s, i2)
    tc2 = S(74.55)
    topla(s, "s2", tc2, 540, 1080, 360, C2 - 18, 0.35)
    c2 = [("will = ", KRE), ("predictions", SAR), (" · sudden decisions", KRE)]
    s.yazi("c2", X0, C2, c2, "Fredoka", 700, 56, tc2 + 0.2, 0.4, tur="tik", guc=0.5)

    # ---------------- bölüm B3: durum fiilleri (75,01–84,40) ----------------
    i3 = len(s.svg)
    t_d = S(T(7, 14, "Durum"))
    s.yazi("dh", X0, 855, [("durum fiilleri", SAR)], "Caveat", 700, 72, t_d, 0.7, tur="tik", guc=0.55)
    FF_ = 96
    FY = (960, 1055, 1150)
    nm = [SOZ[7][i]["sozcuk"].rstrip(",:").lower() for i in (16, 17, 18)]
    gen2 = max(Y.genislik("Fredoka", 700, a, FF_) for a in nm)
    for n, i in enumerate((16, 17, 18)):
        s.yazi("fl%d" % n, X0, FY[n], [(nm[n], KRE)], "Fredoka", 700, FF_, S(T(7, i)), 0.3, tur="tik", guc=0.55)
    bx3 = X0 + gen2 + 30
    tnow = S(T(7, 19, "now"))
    s.yol("fsiv", sivri(bx3, 890, 1180), tnow - 0.25, 0.5, IKN, 6, 1, "cizgi", 0.55)
    xn = bx3 + 68 + 40
    s.yazi("fnow", xn, 960, [("now", KRE)], "Fredoka", 700, FF_, tnow, 0.3, tur="tik", guc=0.6)
    nw_ = Y.genislik("Fredoka", 700, "now", FF_)
    ikon(s, "clock", "fclk", xn + nw_ + 40, 880, 120, tnow + 0.3, tnow + 0.9, 5.0, SAR)
    ting = S(T(7, 22, "ing"))
    s.yazi("fing", xn, 1150, [("-ing", SAR)], "Fredoka", 700, 130, ting, 0.3, tur="tik", guc=0.6)
    iw = Y.genislik("Fredoka", 700, "-ing", 130)
    ta = S(T(7, 23, "almaz"))
    s.yol("fx1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xn - 16, 1150 - 100, xn + iw / 2, 1150 - 44, xn + iw + 16,
                                                      1150 + 14), ta, 0.28, KRE, 12, 1, "cizgi", 0.7)
    s.yol("fx2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xn + iw + 16, 1150 - 100, xn + iw / 2, 1150 - 50, xn - 16,
                                                      1150 + 14), ta + 0.26, 0.28, KRE, 12, 1, "cizgi", 0.7)
    s.yazi("falm", xn + iw + 46, 1150, [("almaz", KRE)], "Caveat", 700, 72, ta + 0.5, 0.4, tur="tik", guc=0.45)
    # I know the answer. ✓ / I am knowing. ✗ (kırmızı çizgi 83,70)
    RA, RB, RX = 1280.0, 1366.0, 140.0
    sp3 = Y.genislik("Fredoka", 700, " ", 72)
    cx, ya = RX, []
    for n, i in enumerate((24, 25, 26, 27)):
        m = SOZ[7][i]["sozcuk"]
        w = Y.genislik("Fredoka", 700, m, 72)
        s.yazi("ra%d" % n, cx, RA, [(m, KRE)], "Fredoka", 700, 72, S(T(7, i)), 0.12, tur="tik" if n == 0 else None)
        ya.append((cx, w))
        cx += w + sp3
    s.yol("rah", Y.el_daire(ya[1][0] + ya[1][1] / 2, RA - 26, ya[1][1] / 2 + 12, 52, 2.0), S(T(7, 25, "know")) + 0.1,
          0.4, SAR, 9, 0.85, "parilti", 0.5)
    s.yol("rat", Y.tik_yolu(X0, RA - 50, 56), S(T(7, 27, "answer")) + 0.5, 0.3, KRE, 10, 1, "cizgi", 0.55)
    cx, yb = RX, []
    for n, i in enumerate((29, 30, 31)):
        m = SOZ[7][i]["sozcuk"]
        w = Y.genislik("Fredoka", 700, m, 72)
        s.yazi("rb%d" % n, cx, RB, [(m, KRE)], "Fredoka", 700, 72, S(T(7, i)), 0.12, tur="tik" if n == 0 else None)
        yb.append((cx, w))
        cx += w + sp3
    xe = yb[2][0] + yb[2][1]
    tr = S(T(7, 31, "knowing"))
    s.yol("rbl", Y.el_cizgi(RX - 8, RB - 26, xe + 8, RB - 30, 1), tr + 0.1, 0.4, KIR, 10, 1, "cizgi", 0.65)
    s.yol("rbx1", "M%.1f %.1f L%.1f %.1f" % (X0, RB - 54, X0 + 54, RB + 2), tr + 0.55, 0.15, KIR, 10, 1, "cizgi", 0.7)
    s.yol("rbx2", "M%.1f %.1f L%.1f %.1f" % (X0 + 54, RB - 54, X0, RB + 2), tr + 0.7, 0.15, KIR, 10, 1, "cizgi", 0.5)
    s.olay(tr + 0.7, "vurus", 0.85)
    g3 = kimlikler(s, i3)
    tc3 = S(84.4)
    topla(s, "s3", tc3, 540, 1100, 360, C3 - 18, 0.35)
    c3 = [("know · own · cost = no ", KRE), ("-ing", SAR)]
    s.yazi("c3", X0, C3, c3, "Fredoka", 700, 56, tc3 + 0.2, 0.4, tur="tik", guc=0.5)

    # ---------------- bölüm C: Kod: tarife → Simple Present / tahmin → will (84,87–89,43) ----------------
    tk = S(T(7, 32, "Kod"))
    s.yazi("kod", X0, 890, [("Kod:", IKN)], "Caveat", 700, 72, tk, 0.4, tur="tik")
    KF = 110
    A1, A2, B1, B2 = 995.0, 1110.0, 1255.0, 1370.0
    a1 = Y.genislik("Fredoka", 700, "tarife", KF)
    s.yazi("k1a", X0, A1, [("tarife", KRE)], "Fredoka", 700, KF, S(T(7, 33, "tarife")), 0.35, tur="tik", guc=0.6)
    s.yol("k1o", Y.el_ok(X0 + a1 + 36, A1 - 40, X0 + a1 + 170, A1 - 40), S(T(7, 34, "varsa")), 0.3, IKN, 10, 1,
          "cizgi", 0.5)
    s.yazi("k1b", X0, A2, [("Simple Present", SAR)], "Fredoka", 700, KF, S(T(7, 35, "Simple")), 0.5, tur="tik",
           guc=0.6)
    b1 = Y.genislik("Fredoka", 700, "tahmin", KF)
    s.yazi("k2a", X0, B1, [("tahmin", KRE)], "Fredoka", 700, KF, S(T(7, 37, "tahmin")), 0.35, tur="tik", guc=0.6)
    s.yol("k2o", Y.el_ok(X0 + b1 + 36, B1 - 40, X0 + b1 + 170, B1 - 40), S(T(7, 38, "varsa")), 0.3, IKN, 10, 1,
          "cizgi", 0.5)
    s.yazi("k2b", X0, B2, [("will", SAR)], "Fredoka", 700, KF, S(T(7, 39, "will")), 0.35, tur="tik", guc=0.7)
    tn2 = S(89.0)
    nw = Y.genislik("Lexend", 700, "Next lesson", 56)
    s.yazi("nx", 1032 - nw - 62, 1376, [("Next lesson", KRE)], "Lexend", 700, 56, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M%.1f 1356 L%.1f 1356 M%.1f 1344 L%.1f 1356 L%.1f 1368" % (
        1032 - 48, 1032 - 6, 1032 - 20, 1032 - 6, 1032 - 20), tn2 + 0.3,
          0.25, KRE, 4.5, 1, "cizgi", 0.4)
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

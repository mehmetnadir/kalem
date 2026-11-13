"""Sahne 08 tuzak (HyperFrames, 1920x1080): "doesn't eats" / "Does she eats" yanlış kartları (kırmızı YALNIZ burada),
öğrenci sorusu (soru anı 2), s harfinin does'a kayması, fark tablosu, doğru kartlar, kanca fiiliyle sınama, kod.
Zaman tek kaynak: ../../zaman.json + ../../ortak/anlatim/sozcukler.json (küresel sn; cümle 39–50). Yerel sn = küresel − t_bas."""
import json
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_ALL = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
SOZ = {c: [w for w in _ALL if w["cumle"] == c] for c in range(39, 51)}
R = Y.RENK
KRE, IKN, SAR, KIR = R["murekkep"], R["ikincil"], R["vurgu"], R["kirmizi"]
YESIL = R["vurgu"]   # yeşil token yok → vurgu (QA 13.11)
TB = Z["t_bas"]
KX, KW, KH = 96, 940, 130     # sol kartlar
RX, RW = 1100, 724            # sağ bölge
FS = 60


def T(c, i):
    return SOZ[c][i]["t0"]


def kimlikler(s, bas):
    return {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}


def uret():
    s = Y.Sahne(TB)
    S = s.S
    tt = lambda c, i: S(T(c, i))  # noqa: E731
    gruplar = []
    dizi = Y.dizi

    def grup(ad, bas):
        gruplar.append((ad, kimlikler(s, bas)))

    def sol(ad, t, d=0.3):
        s.to("#" + ad, t, {"opacity": 0, "duration": d, "ease": "power1.in"})

    def kart(kid, y, t, parc, boy=FS, genis=KW):
        s.yol("k" + kid, Y.el_kutu(KX, y, genis, KH), t, 0.4, IKN, 4, 1, "cizgi", 0.5)
        e, yer = dizi(s, kid, KX + 34, y + 88, parc, boy=boy)
        assert e <= KX + genis - 110, "kart taştı %s: %.0f" % (kid, e)
        return yer

    def carp(kid, x, y, b, t, renk=KIR, w=9):
        d1, d2 = Y.carpi(x, y, b)
        s.yol(kid + "a", d1, t, 0.22, renk, w, 1, "cizgi", 0.7)
        s.yol(kid + "b", d2, t + 0.22, 0.22, renk, w, 1, None)
        s.olay(t + 0.22, "vurus", 0.8)

    def tik(kid, x, y, b, t, renk=YESIL, w=10):
        s.yol(kid, Y.tik_yolu(x, y, b), t, 0.3, renk, w, 1, "cizgi", 0.55)

    # ================= C39: perde =================
    g0 = len(s.svg)
    s.yazi("tz", 96, 330, [("TUZAK", KRE)], "Fredoka", 700, 170, tt(39, 0), 0.8, tur="tik", guc=0.6)
    wz = Y.genislik("Fredoka", 700, "TUZAK", 170)
    s.yol("tzu", Y.el_cizgi(90, 362, 96 + wz + 10, 358, 3), tt(39, 2), 0.5, SAR, 10, 0.9, "cizgi", 0.6)
    s.yazi("hi", 96, 450, [("hata iki yerde çıkar:", IKN)], "Caveat", 700, 64, tt(39, 3), 1.4, tur="tik", guc=0.45)
    x = 96.0
    for n, (m, i) in enumerate((("olumsuz", 7), ("soru", 9))):
        w = Y.genislik("Fredoka", 700, m, 80)
        s.yol("pk%d" % n, Y.el_kutu(x, 520, w + 60, 120), tt(39, i), 0.4, SAR, 5, 1, "cizgi", 0.55)
        s.yazi("pt%d" % n, x + 30, 606, [(m, KRE)], "Fredoka", 700, 80, tt(39, i) + 0.1, 0.3, tur="tik", guc=0.5)
        x += w + 60 + 50
    grup("gP", g0)
    sol("gP", tt(40, 0) - 0.3)

    # ================= C40–C41: yanlış kartlar =================
    g0 = len(s.svg)
    y1, y2 = 330, 500
    yer1 = kart("w1", y1, tt(40, 0) - 0.05, [
        {"m": "She ", "t": tt(40, 0), "tik": True}, {"m": "doe", "t": tt(40, 1), "bos": 18}, {"m": "s", "t": tt(40, 1), "bos": 18},
        {"m": "n't", "t": tt(40, 1)}, {"m": " eat", "t": tt(40, 2)},
        {"m": "s", "t": tt(40, 2) + 0.12}, {"m": " fish.", "t": tt(40, 3)}])
    carp("x1", KX + KW - 96, y1 + 36, 56, tt(40, 3) + 0.15)
    yer2 = kart("w2", y2, tt(41, 0) - 0.05, [
        {"m": "Does", "t": tt(41, 0), "tik": True}, {"m": " she", "t": tt(41, 1)}, {"m": " eat", "t": tt(41, 2)},
        {"m": "s", "t": tt(41, 2) + 0.12}, {"m": " fish?", "t": tt(41, 3)}])
    carp("x2", KX + KW - 96, y2 + 36, 56, tt(41, 3) + 0.15)
    grup("gW", g0)
    sol("gW", tt(45, 0) - 0.3)

    # ================= C42: öğrenci sorusu (soru anı 2) =================
    g0 = len(s.svg)
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.72, 1080.0, 300.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" '
                 'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (
                     BTX, BTY, BS, KRE, 3.0 / BS, "".join(
                         '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    t0 = tt(42, 0) - 0.14
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    BF, BX, BASE = 40, 1340.0, (360, 414, 468)
    sp = Y.genislik("Fredoka", 600, " ", BF)
    GOR = {3: "Doesn't"}
    satir = ((0, 1, 2), (3, 4), (5, 6))
    gens = [sum(Y.genislik("Fredoka", 600, GOR.get(i, SOZ[42][i]["sozcuk"]), BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = BX + max(gens) + 44
    assert x1b < 1850, "balon taştı %.0f" % x1b
    s.yol("bal", Y.balon_sol(1296, 296, x1b, 500, 1226, 440), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    pos = {}
    for sat, base in zip(satir, BASE):
        x = BX
        for i in sat:
            m = GOR.get(i, SOZ[42][i]["sozcuk"])
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, tt(42, i), 0.12,
                   tur="tik" if i in (0, 3, 5) else None)
            pos[i] = (x, w, base)
            x += w + sp
    ex, ew, eb = pos[4]
    # QA 13.11: halkalar harflere değiyordu → vurgu el altçizgisi (sözcük göründükten sonra)
    s.yol("bd", Y.el_cizgi(ex - 2, eb + 11, ex + ew + 2, eb + 10, 6), tt(42, 4) + 0.15, 0.35, SAR, 7, 0.9, "parilti", 0.55)
    grup("gOgr", g0)
    sol("gOgr", tt(43, 0) - 0.1, 0.3)

    # ================= C43: does = do + s; s eats'ten does'a kayar =================
    g0 = len(s.svg)
    DB = 520
    e, _ = dizi(s, "dd", RX, DB, [
        {"m": "does", "t": tt(43, 1)}, {"m": " = ", "t": tt(43, 2), "r": IKN}, {"m": "do", "t": tt(43, 3)},
        {"m": " + ", "t": tt(43, 4), "r": IKN}, {"kutu": True, "m": "s", "t": tt(43, 5)}], boy=104)
    assert e < RX + RW, "does=do+s taştı %.0f" % e
    s.yazi("tk", RX, 640, [("takı yardımcı fiilde zaten var", KRE)], "Caveat", 700, 56, tt(43, 7), 1.5, tur="tik",
           guc=0.45)
    grup("gD", g0)
    sol("gD", tt(44, 0) - 0.15)
    # kart 1: eats'in s'si (yer1: She , doesn't, eat, s, fish.) ve doesn't içindeki s
    xs_e = yer1[5][1]                                     # "s" parçasının x'i (eats)
    xs_d = yer1[2][1]                                     # "doesn't" içinde s'nin x'i (iki yanı 18 px açık: kutu komşu harfe değmez, QA 13.11)
    ws = Y.genislik("Fredoka", 700, "s", FS)
    pad = 14
    tf = tt(43, 7)
    s.kutulu("sk", xs_e - pad, y1 + 88, "s", "Fredoka", 700, FS, tf, 0.25, pad)
    s.to("#" + yer1[5][0], tf, {"opacity": 0, "duration": 0.05})
    dx = xs_d - xs_e
    s.to("#sk", tf + 0.4, {"x": dx, "duration": 0.8, "ease": "power2.inOut"})
    s.to("#sk", tf + 0.4, {"y": -64, "duration": 0.4, "ease": "power2.out"})
    s.to("#sk", tf + 0.8, {"y": 0, "duration": 0.4, "ease": "power2.in"})
    s.to("#" + yer1[2][0], tf + 1.15, {"opacity": 0, "duration": 0.05})   # kutu inince alttaki düz s gizlenir (üst üste yok)
    s.olay(tf + 0.4, "cizgi", 0.5)
    s.olay(tf + 1.2, "tik", 0.55)
    sol("sk", tt(45, 0) - 0.3)

    # ================= C44: she -> s; yeri yanlış =================
    g0 = len(s.svg)
    e, _ = dizi(s, "sh", RX, 480, [
        {"m": "she", "t": tt(44, 3)}, {"ok": 90, "t": tt(44, 5), "bos": 20},
        {"kutu": True, "m": "s", "t": tt(44, 6)}], boy=104)
    # QA 13.11: not oklarla kesişiyordu → notu s kutusunun sağına al (oklar 530'dan aşağı çıkar)
    wnot = Y.genislik("Caveat", 700, "zihin se ister", 56)
    assert e + 40 + wnot < RX + RW + 80, "not sığmadı %.0f" % (e + 40 + wnot)
    s.yazi("is", e + 40, 480, [("zihin se ister", IKN)], "Caveat", 700, 56, tt(44, 6), 0.8, tur="tik", guc=0.45)
    s.yazi("ew", RX, 760, [("eats", KRE)], "Fredoka", 700, 92, tt(44, 8), 0.3, tur="tik", guc=0.5)
    s.yazi("dw", RX + 400, 760, [("does", KRE)], "Fredoka", 700, 92, tt(44, 8), 0.3, tur="tik", guc=0.5)
    wew = Y.genislik("Fredoka", 700, "eats", 92)
    wdw = Y.genislik("Fredoka", 700, "does", 92)
    sx = e - 60                                            # s kutusunun orta x'i
    s.yol("a1", Y.el_ok(sx - 20, 530, RX + 90, 660, 1), tt(44, 10), 0.4, SAR, 7, 0.95, "cizgi", 0.55)
    carp("x3", RX + wew + 24, 690, 64, tt(44, 11))
    s.yol("a2", Y.el_ok(sx + 20, 530, RX + 500, 660, 1), tt(44, 11) + 0.25, 0.4, SAR, 7, 0.95, "cizgi", 0.55)
    tik("t3", RX + 400 + wdw + 24, 690, 66, tt(44, 11) + 0.4)
    grup("gS", g0)
    sol("gS", tt(45, 0) - 0.25)

    # ================= C45: fark tablosu =================
    g0 = len(s.svg)
    s.yazi("bh", 96, 290, [("be dışındaki fiillerde", IKN)], "Caveat", 700, 60, tt(45, 0), 1.2, tur="tik", guc=0.45)
    s.yol("tl", Y.el_kutu(96, 330, 840, 500), tt(45, 3) - 0.1, 0.5, KRE, 4.5, 1, "cizgi", 0.6)
    dizi(s, "h1", 136, 400, [{"m": "olumlu", "t": tt(45, 3), "r": SAR}], aile="Lexend", agr=700, boy=36)
    s.yazi("n1", 136, 490, [("yardımcı fiil yok", IKN)], "Caveat", 700, 60, tt(45, 5), 1.1, tur="tik", guc=0.45)
    e, _ = dizi(s, "e1", 136, 690, [{"m": "eat", "t": tt(45, 9), "bos": 2}, {"kutu": True, "m": "s", "t": tt(45, 12)}],
                boy=140)
    s.yol("tr", Y.el_kutu(984, 330, 840, 500), tt(45, 13) - 0.1, 0.5, KRE, 4.5, 1, "cizgi", 0.6)
    dizi(s, "h2", 1024, 400, [{"m": "olumsuz", "t": tt(45, 13), "r": SAR}, {"m": ", soru", "t": tt(45, 15), "r": SAR}],
         aile="Lexend", agr=700, boy=36)
    s.yazi("n2", 1024, 490, [("yardımcı fiil var", IKN)], "Caveat", 700, 60, tt(45, 16), 1.2, tur="tik", guc=0.45)
    e, yer3 = dizi(s, "e2", 1024, 690, [
        {"m": "doe", "t": tt(45, 18)}, {"kutu": True, "m": "s", "t": tt(45, 20), "bos": 4},
        {"m": " + ", "t": tt(45, 21), "r": IKN}, {"m": "eat", "t": tt(45, 22), "r": IKN}], boy=120)
    assert e < 1824 - 30, "tablo taştı %.0f" % e
    ex3, ew3 = yer3[3][1], yer3[3][2]
    s.yol("e2u", Y.el_cizgi(ex3 - 4, 712, ex3 + ew3 + 4, 709, 1), tt(45, 24), 0.4, SAR, 8, 0.9, "cizgi", 0.55)
    grup("gT", g0)
    sol("gT", tt(46, 0) - 0.3)

    # ================= C46: doğru kartlar =================
    g0 = len(s.svg)
    kart("c1", 330, tt(46, 0) - 0.05, [
        {"m": "She ", "t": tt(46, 0), "tik": True}, {"m": "doesn't", "t": tt(46, 1)},
        {"m": " eat", "t": tt(46, 2), "r": IKN}, {"m": " fish.", "t": tt(46, 3)}])
    tik("tc1", KX + KW - 100, 330 + 34, 60, tt(46, 3) + 0.15)
    kart("c2", 500, tt(46, 4) - 0.05, [
        {"m": "Does", "t": tt(46, 4), "tik": True}, {"m": " she", "t": tt(46, 5)},
        {"m": " eat", "t": tt(46, 6), "r": IKN}, {"m": " fish?", "t": tt(46, 7)}])
    tik("tc2", KX + KW - 100, 500 + 34, 60, tt(46, 7) + 0.15)
    grup("gC", g0)
    sol("gC", tt(47, 0) - 0.1)

    # ================= C47: kanca kartı geri gelir =================
    g0 = len(s.svg)
    s.yol("hk", Y.el_kutu(KX, 150, KW, 100), tt(47, 1) - 0.05, 0.45, IKN, 4, 1, "cizgi", 0.5)
    e, _ = dizi(s, "hz", KX + 34, 218, [{"m": "I get up at seven every morning.", "t": tt(47, 1), "tik": True}], boy=48)
    assert e < KX + KW - 20
    grup("gH", g0)

    # ================= C48–C49: kanca fiiliyle sınama =================
    g0 = len(s.svg)
    z1, z2 = 330, 500
    yer5 = kart("d1", z1, tt(48, 0) - 0.05, [
        {"m": "He ", "t": tt(48, 0), "tik": True}, {"m": "doesn't ", "t": tt(48, 1)}, {"m": "get", "t": tt(48, 2), "r": IKN},
        {"m": " up at seven.", "t": tt(48, 3), "bos": 0}], boy=52)
    tik("td1", KX + KW - 100, z1 + 34, 60, tt(48, 5) + 0.15)
    yer6 = kart("d2", z2, tt(48, 6) - 0.05, [
        {"m": "Does ", "t": tt(48, 6), "tik": True}, {"m": "he ", "t": tt(48, 7)}, {"m": "get", "t": tt(48, 8), "r": IKN},
        {"m": " up at seven?", "t": tt(48, 9), "bos": 0}], boy=52)
    tik("td2", KX + KW - 100, z2 + 34, 60, tt(48, 11) + 0.15)
    for kid, yer, yy in (("g1", yer5, z1), ("g2", yer6, z2)):
        gx, gw = yer[2][1], yer[2][2]
        s.yol(kid, Y.el_cizgi(gx - 2, yy + 92, gx + gw + 2, yy + 91, 5), tt(49, 0), 0.35, SAR, 7, 0.9, "parilti", 0.5)
    s.yazi("gt", RX + 20, 470, [("get", KRE)], "Fredoka", 700, 120, tt(49, 0), 0.3, tur="tik", guc=0.5)
    wg = Y.genislik("Fredoka", 700, "get", 120)
    tik("tg", RX + 20 + wg + 40, 400, 80, tt(49, 2))
    s.yazi("gs", RX + 20, 650, [("gets", KRE)], "Fredoka", 700, 120, tt(49, 3), 0.3, tur="tik", guc=0.5)
    wgs = Y.genislik("Fredoka", 700, "gets", 120)
    carp("xg", RX + 20 + wgs + 40, 570, 80, tt(49, 4))
    grup("gK", g0)
    sol("gK", tt(50, 0) - 0.15)
    sol("gH", tt(50, 0) - 0.15)

    # ================= C50: kod =================
    s.yazi("kd", 96, 330, [("Kod:", SAR)], "Caveat", 700, 110, tt(50, 0), 0.5, tur="tik", guc=0.55)
    dizi(s, "k", 96, 530, [{"m": "takı", "t": tt(50, 1)}, {"m": " bir", "t": tt(50, 2)}, {"m": " kez", "t": tt(50, 3)},
                           {"m": " gelir.", "t": tt(50, 4)}], boy=104)
    e, yer7 = dizi(s, "ky", 96, 780, [
        {"kutu": True, "m": "s", "t": tt(50, 1) + 0.2, "bos": 40}, {"ok": 120, "t": tt(50, 8), "bos": 30},
        {"m": "yardımcı fiil", "t": tt(50, 5)}], boy=104)
    assert e < 1824, "kod satırı taştı %.0f" % e

    kun = Y.kunye_svg("Trap", "Trap", 3, 3)
    return s, {"kun": kun, "gruplar": gruplar}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

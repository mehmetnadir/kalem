"""Sahne 06 (İLERİ yatay, 1920x1080): öğrenci sorusu + durum fiili tuzağı + süreç/sonuç kartı + kod.
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
    # ---------------- konuşma balonu: Hocam, have been knowing, / olmaz mıydı? ----------------
    BF, BX, BASE = 44, 384.0, (244, 306)
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5))
    gens = [sum(Y.genislik("Fredoka", 600, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = BX + max(gens) + 44
    s.yol("bal", Y.balon_sol(340, 176, x1b, 330, 262, 292), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    pos = {}
    for sat, base in zip(satir, BASE):
        x = BX
        for i in sat:
            m = SOZ[6][i]["sozcuk"]
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(T(6, i)), 0.12,
                   tur="tik" if i in (0, 4) else None)
            bal_ids.append("bw%d" % i)
            pos[i] = (x, w, base)
            x += w + sp
    # fosforlu belirteç: have been knowing altı
    xa, xb = pos[1][0], pos[3][0] + pos[3][1]
    s.yol("bm", Y.el_cizgi(xa - 2, BASE[0] + 12, xb + 2, BASE[0] + 9), S(T(6, 3)), 0.4, SAR, 8, 0.85, "cizgi", 0.5)
    bal_ids.append("bm")
    # künye: Question -> Form (66,75)
    tx = S(T(7, 0))
    s.to("#ku-bolum", tx, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tx, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    s.to("#ku-ajA", tx, {"opacity": 0, "duration": 0.2})
    s.to("#ku-ajB", tx, {"opacity": 1, "duration": 0.2})
    # ---------------- sağ üst: yanlış kalıp + düzeltme ----------------
    RX, FB = 1070.0, 80
    wb = 0.0
    sp2 = Y.genislik("Fredoka", 700, " ", FB)
    x = RX
    for n, i in enumerate((1, 2, 3)):
        m = SOZ[6][i]["sozcuk"].rstrip(",")
        w = Y.genislik("Fredoka", 700, m, FB)
        s.yazi("hb%d" % n, x, 280, [(m, KRE)], "Fredoka", 700, FB, S(T(6, i)), 0.15, tur="tik" if n == 0 else None)
        x += w + sp2
    xe = x - sp2
    s.yol("hbx", Y.el_cizgi(RX - 14, 248, xe + 14, 240, -2), S(T(7, 0)), 0.35, KIR, 10, 1, "cizgi", 0.7)
    s.olay(S(T(7, 0)) + 0.3, "vurus", 0.85)
    s.yazi("hk", RX, 410, [("have known", KRE)], "Fredoka", 700, FB, S(T(7, 0)) + 0.5, 0.35, tur="tik", guc=0.6)
    wk = Y.genislik("Fredoka", 700, "have known", FB)
    s.yol("hkt", Y.tik_yolu(RX + wk + 40, 330, 70), S(T(7, 0)) + 0.95, 0.3, SAR, 11, 0.9, "cizgi", 0.55)
    s.yazi("dn", RX, 500, [("durum fiilleri ", KRE), ("-ing", SAR), (" almaz", KRE)], "Caveat", 700, 64,
           S(T(7, 1)), 0.9, tur="tik", guc=0.5)
    # balon + baş köşeye toplanır
    s.to("#balg", S(69.4), {"svgOrigin": "90 150", "scale": 0.62, "opacity": 0.85, "duration": 0.7,
                            "ease": "power3.inOut"})
    # ---------------- iki sütunlu kart: iskelet erken, hücreler konuşma anında ----------------
    CY, CH, CW = 600, 220, 780
    LX, RXC = 140, 980
    s.yol("kL", Y.el_kutu(LX, CY, CW, CH), S(T(7, 4)) + 0.2, 0.5, KRE, 4.2, 1, "cizgi", 0.6)
    s.yol("kR", Y.el_kutu(RXC, CY, CW, CH), S(T(7, 4)) + 0.55, 0.5, KRE, 4.2, 1, "cizgi", 0.6)
    s.yazi("pl", LX + 40, CY + 56, [("PROCESS", SAR)], "Lexend", 700, 30, S(T(7, 5)), 0.3, tur="tik", guc=0.5)
    FZ = 56
    p1 = Y.genislik("Fredoka", 700, "have / has", FZ)
    p2 = Y.genislik("Fredoka", 700, " been", FZ)
    p3 = Y.genislik("Fredoka", 700, " + ", FZ)
    fx = LX + 40
    s.yazi("pf1", fx, CY + 150, [("have / has", KRE)], "Fredoka", 700, FZ, S(T(7, 6)), 0.3, tur="tik", guc=0.55)
    s.yazi("pf2", fx + p1, CY + 150, [(" been", KRE)], "Fredoka", 700, FZ, S(T(7, 7)), 0.25, tur="tik", guc=0.5)
    s.yazi("pf3", fx + p1 + p2, CY + 150, [(" + ", IKN)], "Fredoka", 700, FZ, S(T(7, 8)), 0.2, tur=None)
    s.yazi("pf4", fx + p1 + p2 + p3, CY + 150, [("V", KRE), ("-ing", SAR)], "Fredoka", 700, FZ, S(T(7, 9)), 0.3,
           tur="tik", guc=0.6)
    s.yazi("rl", RXC + 40, CY + 56, [("RESULT", SAR)], "Lexend", 700, 30, S(T(7, 10)), 0.3, tur="tik", guc=0.5)
    r1 = Y.genislik("Fredoka", 700, "have / has", FZ)
    r3 = Y.genislik("Fredoka", 700, " + ", FZ)
    gx = RXC + 40
    s.yazi("rf1", gx, CY + 150, [("have / has", KRE)], "Fredoka", 700, FZ, S(T(7, 11)), 0.3, tur="tik", guc=0.55)
    s.yazi("rf2", gx + r1, CY + 150, [(" + ", IKN)], "Fredoka", 700, FZ, S(T(7, 12)), 0.2, tur=None)
    s.yazi("rf3", gx + r1 + r3, CY + 150, [("V3", SAR)], "Fredoka", 700, FZ, S(T(7, 14)), 0.3, tur="tik", guc=0.6)
    s.yazi("rf4", gx + r1 + r3 + Y.genislik("Fredoka", 700, "V3", FZ) + 24, CY + 150, [("(third form)", IKN)],
           "Caveat", 700, 44, S(T(7, 15)), 0.5, tur=None)
    # ---------------- oklar: -yor → süreç, -di → sonuç (76,70–79,82) ----------------
    AY = 900
    ta = S(T(7, 17))
    for k, (px, ya, tt, sol, sag) in enumerate(((LX + 40, "-yor", S(T(7, 17)), "o1", "süreç"),
                                                (RXC + 40, "-di", S(T(7, 19)), "o2", "sonuç"))):
        wy = Y.genislik("Caveat", 700, ya, 60)
        s.yazi(sol, px, AY, [(ya, SAR)], "Caveat", 700, 60, tt, 0.3, tur="tik", guc=0.5)
        s.yol(sol + "o", Y.el_ok(px + wy + 18, AY - 22, px + wy + 98, AY - 22, 1), tt + 0.25, 0.3, SAR, 6, 0.9,
              "cizgi", 0.5)
        s.yazi(sol + "s", px + wy + 118, AY, [(sag, KRE)], "Caveat", 700, 60, tt + 0.45, 0.4, tur="tik", guc=0.5)
        s.yol(sol + "k", Y.el_ok(px + 50, AY - 50, px + 50, CY + CH + 14, 1), tt, 0.3, SAR, 7, 0.9, "cizgi", 0.5)
    # ---------------- Kod: süreç varsa been var / sonuç varsa been yok (79,97–85,01) ----------------
    tk = S(T(7, 22))
    s.to("#icerik", tk - 0.5, {"svgOrigin": "90 110", "scale": 0.55, "duration": 0.8, "ease": "power3.inOut"})
    i_kod = len(s.svg)
    s.yazi("kod", 140, 640, [("Kod:", KRE)], "Caveat", 700, 64, tk, 0.4, tur="tik")
    KF, K1, K2 = 100, 780, 920
    w1 = Y.genislik("Fredoka", 700, "süreç varsa", KF)
    s.yazi("k1a", 140, K1, [("süreç varsa", KRE)], "Fredoka", 700, KF, S(T(7, 24)), 0.4, tur="tik", guc=0.6)
    s.yazi("k1b", 140 + w1 + 50, K1, [("been", SAR), (" var", KRE)], "Fredoka", 700, KF, S(T(7, 26)), 0.4, tur="tik",
           guc=0.6)
    w1b = Y.genislik("Fredoka", 700, "been var", KF)
    s.yol("k1t", Y.tik_yolu(140 + w1 + 50 + w1b + 40, K1 - 70, 60), S(T1(7, 27)), 0.3, SAR, 10, 0.9, "cizgi", 0.55)
    w2 = Y.genislik("Fredoka", 700, "sonuç varsa", KF)
    s.yazi("k2a", 140, K2, [("sonuç varsa", KRE)], "Fredoka", 700, KF, S(T(7, 28)), 0.4, tur="tik", guc=0.6)
    s.yazi("k2b", 140 + w2 + 50, K2, [("been", SAR), (" yok", KRE)], "Fredoka", 700, KF, S(T(7, 30)), 0.4,
           tur="tik", guc=0.6)
    w2b = Y.genislik("Fredoka", 700, "been yok", KF)
    s.yol("k2t", Y.tik_yolu(140 + w2 + 50 + w2b + 40, K2 - 70, 60), S(T1(7, 31)), 0.3, SAR, 10, 0.9, "cizgi", 0.55)
    s.olay(S(T1(7, 31)), "vurus", 0.8)
    nw = Y.genislik("Lexend", 500, "Next lesson", 24)
    tn2 = S(T1(7, 31)) - 0.3
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

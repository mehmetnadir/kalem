"""Sahne 06 DİKEY (İLERİ, 1080x1920): öğrenci sorusu + durum fiili tuzağı + süreç/sonuç tablosu + kod.
Yerleşim BRIEF-DIKEY §2-§4: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform bandı boş.
Üst yarı: balon (372-620) + yanlış/doğru kalıp (700-960); alt yarı: tablo iskeleti erken çizilir (1010-1392),
hücreler konuşma anında dolar. 79,4'te üst yarı tek satırlık çipe toplanır, yerine kod kartı gelir.
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
    """s.svg[bas:] elemanlarının üst düzey id kümesi (bölüm grubu için)."""
    return {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}


def topla(s, grup, t, cx, cy, hx, hy, sure=0.5):
    """Grubu çip konumuna (hx, hy) küçülterek toplar (merkez cx, cy)."""
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
    BS, BTX, BTY = 0.484, 63.0, 450.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.3f)" fill="none" stroke="%s" '
                 'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (
                     BTX, BTY, BS, KRE, 3.6 / BS, "".join(
                         '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = max(S(T(6, 0)) - 0.14, 0.42)
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu: Fredoka 600 56, 2 satır ----------------
    BF, BX, BASE = 56, 280.0, (466, 552)
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5))
    gens = [sum(Y.genislik("Fredoka", 600, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = min(1020.0, BX + max(gens) + 40)
    s.yol("bal", Y.balon_sol(240, 380, x1b, 606, 176, 560), t0 + 0.1, 0.55, KRE, 4.6, 1, "cizgi", 0.7)
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
    xa, xb = pos[1][0], pos[3][0] + pos[3][1]
    s.yol("bm", Y.el_cizgi(xa - 2, BASE[0] + 14, xb + 2, BASE[0] + 11), S(T(6, 3)), 0.4, SAR, 10, 0.85, "cizgi", 0.5)
    bal_ids.append("bm")
    tx = S(T(7, 0))
    s.to("#ku-bolum", tx, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tx, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})

    # ---------------- orta: yanlış kalıp + düzeltme + durum fiili notu (700-960) ----------------
    i0 = len(s.svg)
    FB = 96
    sp2 = Y.genislik("Fredoka", 700, " ", FB)
    x = X0
    for n, i in enumerate((1, 2, 3)):
        m = SOZ[6][i]["sozcuk"].rstrip(",")
        w = Y.genislik("Fredoka", 700, m, FB)
        s.yazi("hb%d" % n, x, 740, [(m, KRE)], "Fredoka", 700, FB, S(T(6, i)), 0.15, tur="tik" if n == 0 else None)
        x += w + sp2
    xe = x - sp2
    s.yol("hbx", Y.el_cizgi(X0 - 14, 706, xe + 14, 698, -2), tx, 0.35, KIR, 12, 1, "cizgi", 0.7)
    s.olay(tx + 0.3, "vurus", 0.85)
    s.yazi("hk", X0, 860, [("have known", KRE)], "Fredoka", 700, FB, tx + 0.5, 0.35, tur="tik", guc=0.6)
    wk = Y.genislik("Fredoka", 700, "have known", FB)
    s.yol("hkt", Y.tik_yolu(X0 + wk + 40, 780, 76), tx + 0.95, 0.3, SAR, 12, 0.9, "cizgi", 0.55)
    s.yazi("dn", X0, 950, [("durum fiilleri ", KRE), ("-ing", SAR), (" almaz", KRE)], "Caveat", 700, 72,
           S(T(7, 1)), 0.9, tur="tik", guc=0.5)
    g1 = kimlikler(s, i0)

    # ---------------- alt: tablo iskeleti erken (1010-1392), hücreler konuşma anında ----------------
    s.yol("kA", Y.el_kutu(X0, 1010, 984, 176), 63.5 - TB, 0.5, KRE, 4.6, 1, "cizgi", 0.6)
    s.yol("kB", Y.el_kutu(X0, 1210, 984, 176), 63.9 - TB, 0.5, KRE, 4.6, 1, "cizgi", 0.6)
    FZ = 72
    s.yazi("pl", X0 + 36, 1062, [("PROCESS", SAR)], "Lexend", 700, 36, S(T(7, 5)), 0.3, tur="tik", guc=0.5)
    p1 = Y.genislik("Fredoka", 700, "have / has", FZ)
    p2 = Y.genislik("Fredoka", 700, " been", FZ)
    p3 = Y.genislik("Fredoka", 700, " + ", FZ)
    fx = X0 + 36
    s.yazi("pf1", fx, 1160, [("have / has", KRE)], "Fredoka", 700, FZ, S(T(7, 6)), 0.3, tur="tik", guc=0.55)
    s.yazi("pf2", fx + p1, 1160, [(" been", KRE)], "Fredoka", 700, FZ, S(T(7, 7)), 0.25, tur="tik", guc=0.5)
    s.yazi("pf3", fx + p1 + p2, 1160, [(" + ", IKN)], "Fredoka", 700, FZ, S(T(7, 8)), 0.2, tur=None)
    s.yazi("pf4", fx + p1 + p2 + p3, 1160, [("V", KRE), ("-ing", SAR)], "Fredoka", 700, FZ, S(T(7, 9)), 0.3,
           tur="tik", guc=0.6)
    s.yazi("rl", X0 + 36, 1262, [("RESULT", SAR)], "Lexend", 700, 36, S(T(7, 10)), 0.3, tur="tik", guc=0.5)
    r1 = Y.genislik("Fredoka", 700, "have / has", FZ)
    r3 = Y.genislik("Fredoka", 700, " + ", FZ)
    s.yazi("rf1", fx, 1360, [("have / has", KRE)], "Fredoka", 700, FZ, S(T(7, 11)), 0.3, tur="tik", guc=0.55)
    s.yazi("rf2", fx + r1, 1360, [(" + ", IKN)], "Fredoka", 700, FZ, S(T(7, 12)), 0.2, tur=None)
    s.yazi("rf3", fx + r1 + r3, 1360, [("V3", SAR)], "Fredoka", 700, FZ, S(T(7, 14)), 0.3, tur="tik", guc=0.6)
    # -yor -> süreç, -di -> sonuç (etiket satırının sağı, Caveat 64)
    for sol, ya, sag, yy, tt in (("o1", "-yor", "süreç", 1066, S(T(7, 17))),
                                 ("o2", "-di", "sonuç", 1266, S(T(7, 19)))):
        wy = Y.genislik("Caveat", 700, ya, 64)
        ws = Y.genislik("Caveat", 700, sag, 64)
        px = 1032 - 36 - (wy + 16 + 74 + 16 + ws) - 12
        s.yazi(sol, px, yy, [(ya, SAR)], "Caveat", 700, 64, tt, 0.3, tur="tik", guc=0.5)
        s.yol(sol + "o", Y.el_ok(px + wy + 16, yy - 24, px + wy + 90, yy - 24, 1), tt + 0.25, 0.3, SAR, 8, 0.9,
              "cizgi", 0.5)
        s.yazi(sol + "s", px + wy + 106, yy, [(sag, KRE)], "Caveat", 700, 64, tt + 0.45, 0.4, tur="tik", guc=0.5)

    # ---------------- üst yarı çipe toplanır, kod kartı (79,97–85,01) ----------------
    tk = S(T(7, 22))
    tc = tk - 0.6
    topla(s, "s1", tc, 540, 830, 240, 420, 0.45)
    topla(s, "balg", tc, 540, 496, 240, 420, 0.45)
    s.yazi("chip", X0, 436, [("have known", KRE)], "Fredoka", 700, 56, tc + 0.3, 0.35, tur="tik", guc=0.5)
    wc = Y.genislik("Fredoka", 700, "have known", 56)
    s.yol("chipt", Y.tik_yolu(X0 + wc + 30, 392, 48), tc + 0.6, 0.25, SAR, 9, 0.9, "cizgi", 0.5)
    s.yol("kk", Y.el_kutu(X0, 500, 984, 470), tk - 0.1, 0.5, KRE, 4.6, 1, "cizgi", 0.6)
    s.yazi("kod", X0 + 40, 590, [("Kod:", KRE)], "Caveat", 700, 72, tk, 0.4, tur="tik")
    KF, K1, K2 = 80, 730, 870
    w1 = Y.genislik("Fredoka", 700, "süreç varsa", KF)
    s.yazi("k1a", X0 + 40, K1, [("süreç varsa", KRE)], "Fredoka", 700, KF, S(T(7, 24)), 0.4, tur="tik", guc=0.6)
    s.yazi("k1b", X0 + 40 + w1 + 36, K1, [("been", SAR), (" var", KRE)], "Fredoka", 700, KF, S(T(7, 26)), 0.4,
           tur="tik", guc=0.6)
    w1b = Y.genislik("Fredoka", 700, "been var", KF)
    s.yol("k1t", Y.tik_yolu(X0 + 40 + w1 + 36 + w1b + 24, K1 - 60, 52), S(T1(7, 27)), 0.3, SAR, 10, 0.9, "cizgi",
          0.55)
    w2 = Y.genislik("Fredoka", 700, "sonuç varsa", KF)
    s.yazi("k2a", X0 + 40, K2, [("sonuç varsa", KRE)], "Fredoka", 700, KF, S(T(7, 28)), 0.4, tur="tik", guc=0.6)
    s.yazi("k2b", X0 + 40 + w2 + 36, K2, [("been", SAR), (" yok", KRE)], "Fredoka", 700, KF, S(T(7, 30)), 0.4,
           tur="tik", guc=0.6)
    w2b = Y.genislik("Fredoka", 700, "been yok", KF)
    s.yol("k2t", Y.tik_yolu(X0 + 40 + w2 + 36 + w2b + 24, K2 - 60, 52), S(T1(7, 31)), 0.3, SAR, 10, 0.9, "cizgi",
          0.55)
    s.olay(S(T1(7, 31)), "vurus", 0.8)
    nw = Y.genislik("Lexend", 700, "Next lesson", 36)
    tn2 = S(T1(7, 31)) - 0.3
    s.yazi("nx", 1032 - nw - 76, 944, [("Next lesson", KRE)], "Lexend", 700, 36, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M%.1f 932 L%.1f 932 M%.1f 922 L%.1f 932 L%.1f 942" % (1032 - 66, 1032 - 30, 1032 - 42,
                                                                          1032 - 30, 1032 - 42), tn2 + 0.3,
          0.25, KRE, 4, 1, "cizgi", 0.4)
    # ---------------- altyazı: konuşulan parça ----------------
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
    return s, {"kun": kun, "bal_ids": bal_ids, "gruplar": [("s1", g1)], "altyazi": Y.altyazi_svg(parcalar)}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    logo = (48, 48, 96 * Y.LOGO_EN_BOY, 96)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), parca["kun"], None, logo, ek=parca["altyazi"],
               bal_ids=parca["bal_ids"], vin=1150, gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

"""Sahne 06 (İLERİ yatay, 1920x1080, 785 kare, t_bas 68,60): öğrenci sorusu (cümle 6) + kural (cümle 7).
Present Perfect: "ago varken has landed olmaz" -> bitmiş zaman sözcükleri -> Finished/Unfinished -> kod.
Tek kaynak: ortak/anlatim/sozcukler.json (küresel sn) + zamanlar.json (t_bas, kare). Yerel sn = t - t_bas.
Komut listesi veri olarak JS'e gömülür; olaylar aynı çağrılardan toplanır (olay.py bu modülü içe alır).
Ok işareti metin değil kalem yoludur (yazı tipi alt kümesinde U+2192 yok)."""
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


def kelimeler(s, kimlik, x, y, idx, c, aile, agr, boy, renk=KRE, metin=None):
    """Sözcükleri konuşma zamanında tek tek açar. metin: sözcük yerine gösterilecek yazı (ör. kesme işareti
    atılmış). Döner: [(x, w)]."""
    sp = Y.genislik(aile, agr, " ", boy)
    yer, cx = [], x
    for n, i in enumerate(idx):
        m = metin[n] if metin else SOZ[c][i]["sozcuk"]
        w = Y.genislik(aile, agr, m, boy)
        s.yazi("%s%d" % (kimlik, n), cx, y, [(m, renk)], aile, agr, boy, s.S(T(c, i)), 0.12,
               tur="tik" if n == 0 else None)
        yer.append((cx, w))
        cx += w + sp
    return yer


def yasak(s, kimlik, cx, cy, r, t):
    """Yasak işareti: kırmızı daire + çapraz çizgi (iki darbe)."""
    s.yol(kimlik + "c", Y.el_daire(cx, cy, r, r, 0.6), t, 0.3, KIR, 7, 0.95, "cizgi", 0.5)
    s.yol(kimlik + "s", "M%.1f %.1f L%.1f %.1f" % (cx - r * 0.72, cy + r * 0.72, cx + r * 0.72, cy - r * 0.72),
          t + 0.28, 0.2, KIR, 7, 0.95, "cizgi", 0.6)


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
    t0 = max(S(T(6, 0)) - 0.14, 0.42)          # soğuk açılış: ilk 12 kare (0,40 sn) boş
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu + sözcükler (Fredoka 600 44) ----------------
    BF, BX, BASE = 44, 384.0, (234, 310)
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6, 7))
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
                   tur="tik" if i in (0, 4) else None)
            bal_ids.append("bw%d" % i)
            pos[i] = (x, w, base)
            x += w + sp
    # fosforlu belirteç: ago altı (69,95)
    xa, wa, ya = pos[1]
    s.yol("bm", Y.el_cizgi(xa - 2, ya + 12, xa + wa + 2, ya + 9), S(T(6, 1)), 0.3, SAR, 8, 0.85, "cizgi", 0.5)
    bal_ids.append("bm")
    # 71,15–71,99 has landed üstüne kırmızı kalem çarpısı
    xs, xe = pos[4][0], pos[5][0] + pos[5][1]
    yb = pos[4][2]
    tx = S(71.15)
    s.yol("xk1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xs - 12, yb - 44, (xs + xe) / 2, yb - 8, xe + 12, yb + 18),
          tx, 0.4, KIR, 8, 1, "cizgi", 0.7)
    s.yol("xk2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xe + 12, yb - 44, (xs + xe) / 2, yb - 14, xs - 12, yb + 18),
          tx + 0.42, 0.4, KIR, 8, 1, "cizgi", 0.7)
    s.olay(tx + 0.42, "vurus", 0.85)
    bal_ids += ["xk1", "xk2"]
    # künye: Question -> Rule (73,62); balon + baş köşeye toplanır (73,30)
    tr = S(73.62)
    s.to("#ku-bolum", tr, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tr, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    s.to("#ku-ajA", tr, {"opacity": 0, "duration": 0.2})
    s.to("#ku-ajB", tr, {"opacity": 1, "duration": 0.2})
    s.to("#balg", S(73.3), {"svgOrigin": "90 150", "scale": 0.62, "opacity": 0.9, "duration": 0.7,
                            "ease": "power3.inOut"})

    # ---------------- A (sol): Hayır. + Bitmiş zaman (sarı bant) + Present Perfect yasaklı (73,62–78,10) ----------------
    AX, A1, A2 = 140.0, 470.0, 590.0
    hw = Y.genislik("Caveat", 700, "Hayır.", 120)
    s.yazi("hay", AX, A1, [("Hayır.", KRE)], "Caveat", 700, 120, S(T(7, 0)), 0.4, tur="tik", guc=0.6)
    bx = AX + hw + 50
    bw = Y.genislik("Caveat", 700, "Bitmiş zaman", 104)
    s.yol("band", Y.el_cizgi(bx - 14, A1 - 24, bx + bw + 14, A1 - 28, 1), S(T(7, 1)), 0.55, SAR, 70, 0.42, "cizgi",
          0.4)
    kelimeler(s, "bz", bx, A1, (1, 2), 7, "Caveat", 700, 104)
    pp = kelimeler(s, "pp", AX, A2, (5, 6), 7, "Fredoka", 700, 80, metin=("Present", "Perfect"))
    pe = pp[1][0] + pp[1][1]
    ty_ = S(T(7, 7))
    s.yol("pst", Y.el_cizgi(AX - 10, A2 - 30, pe + 10, A2 - 36, 2), ty_, 0.4, KIR, 10, 0.95, "cizgi", 0.7)
    s.olay(ty_ + 0.3, "vurus", 0.8)
    s.yazi("yas", pe + 50, A2, [("yasak", KIR)], "Caveat", 700, 76, ty_ + 0.3, 0.4, tur="tik", guc=0.5)

    # ---------------- B (sağ): kırmızı etiketler el kutusunda (78,35–81,47) ----------------
    BXX, BY0, BW, BH = 1080.0, 330.0, 700.0, 290.0
    s.yol("bk", Y.el_kutu(BXX, BY0, BW, BH), S(70.2), 0.5, IKN, 4.4, 1, "cizgi", 0.6)
    LF = 68
    for n, (i, m, yy) in enumerate(((8, "ago", 420.0), (9, "yesterday", 505.0), (10, "last year", 590.0))):
        t = S(T(7, i))
        s.yazi("e%d" % n, BXX + 56, yy, [(m, KIR)], "Fredoka", 700, LF, t, 0.3, tur="tik", guc=0.55)
        w = Y.genislik("Fredoka", 700, m, LF)
        yasak(s, "ey%d" % n, BXX + 56 + w + 70, yy - 24, 32, t + 0.45)

    # ---------------- C: iki sütun Finished -> Simple Past / Unfinished -> Present Perfect (81,72–86,84) ----------------
    CY, CH = 660.0, 170.0
    s.yol("ca", Y.el_kutu(140, CY, 760, CH), S(70.5), 0.5, IKN, 4.4, 1, "cizgi", 0.6)
    s.yazi("cf", 180, CY + 66, [("Finished", KRE)], "Fredoka", 700, 60, S(T(7, 12)), 0.3, tur="tik", guc=0.55)
    s.yol("cfo", Y.el_ok(180, CY + 132, 260, CY + 130), S(T(7, 13)) + 0.1, 0.3, KRE, 7, 0.95, "cizgi", 0.5)
    s.yazi("cs", 290, CY + 146, [("Simple Past", KRE)], "Fredoka", 700, 72, S(T(7, 14)), 0.35, tur="tik", guc=0.6)
    s.yol("cb", Y.el_kutu(1000, CY, 820, CH), S(70.8), 0.5, IKN, 4.4, 1, "cizgi", 0.6)
    s.yazi("cu", 1040, CY + 66, [("Unfinished", KRE)], "Fredoka", 700, 60, S(T(7, 16)), 0.3, tur="tik", guc=0.55)
    s.yol("cuo", Y.el_ok(1040, CY + 132, 1120, CY + 130), S(T(7, 17)) + 0.1, 0.3, SAR, 7, 0.95, "cizgi", 0.5)
    s.yazi("cp", 1150, CY + 146, [("Present Perfect", SAR)], "Fredoka", 700, 72, S(T(7, 18)), 0.4, tur="tik", guc=0.6)

    # ---------------- D: kod kartı el kutusunda (87,09–92,77) ----------------
    DX, DY, DW, DH = 140.0, 856.0, 1100.0, 140.0
    tf = S(71.1)
    s.yol("kart", Y.el_kutu(DX, DY, DW, DH), tf, 0.5, KRE, 4.5, 1, "cizgi", 0.7)
    KFZ = 52
    aw = Y.genislik("Fredoka", 700, "ago", KFZ)
    s.yazi("k1a", DX + 40, DY + 60, [("ago", KIR)], "Fredoka", 700, KFZ, S(T(7, 23)), 0.3, tur="tik", guc=0.6)
    s.yol("k1o", Y.el_ok(DX + 40 + aw + 24, DY + 44, DX + 40 + aw + 100, DY + 42), S(T(7, 24)), 0.3, KIR, 7, 0.95,
          "cizgi", 0.55)
    s.yazi("k1b", DX + 40 + aw + 124, DY + 60, [("Simple Past", KRE)], "Fredoka", 700, KFZ, S(T(7, 25)), 0.35,
           tur="tik", guc=0.6)
    yw = Y.genislik("Fredoka", 700, "yet", KFZ)
    s.yazi("k2a", DX + 40, DY + 122, [("yet", SAR)], "Fredoka", 700, KFZ, S(T(7, 27)), 0.3, tur="tik", guc=0.6)
    s.yol("k2o", Y.el_ok(DX + 40 + yw + 24, DY + 106, DX + 40 + yw + 100, DY + 104), S(T(7, 28)), 0.3, SAR, 7, 0.95,
          "cizgi", 0.55)
    s.yazi("k2b", DX + 40 + yw + 124, DY + 122, [("Present Perfect", KRE)], "Fredoka", 700, KFZ, S(T(7, 29)), 0.4,
           tur="tik", guc=0.6)
    tc = S(T1(7, 30)) - 0.35
    s.yol("ctk", Y.tik_yolu(DX + DW - 90, DY + 44, 46), tc, 0.3, SAR, 8, 0.9, "cizgi", 0.55)
    s.olay(tc, "vurus", 0.8)
    nw = Y.genislik("Lexend", 500, "Next lesson", 24)
    tn2 = tc + 0.1
    s.yazi("nx", 1864 - nw - 44, 984, [("Next lesson", IKN)], "Lexend", 500, 24, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M%.1f 976 L%.1f 976 M%.1f 969 L%.1f 976 L%.1f 983" % (1864 - 38, 1864 - 4, 1864 - 12, 1864 - 4,
                                                                          1864 - 12), tn2 + 0.3, 0.25, IKN, 3, 1,
          "cizgi", 0.4)
    kun = Y.kunye_svg("Question", "Rule", etkin0=2, etkin1=1)
    return s, {"kun": kun, "bal_ids": bal_ids}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34),
               bal_ids=parca["bal_ids"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

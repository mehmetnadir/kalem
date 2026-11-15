"""Sahne 06 DİKEY (İLERİ, 1080x1920, 873 kare, t_bas 70,20): öğrenci sorusu + kural. Present Perfect.
16.11 DUZ3-0206I: soru "took off yerine has taken off", kural "fiili Simple Past'a çeker", kod yet satırı "çoğu zaman";
sabit saniyeler sözcüğe bağlandı (I()); yasak çizgileri kalktı.
Yerleşim BRIEF-DIKEY §2-§4: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform bandı boş.
Tablo iskeleti erken çizilir (70,0–71,0: etiket kutusu, tablo satırları, kod kartı); hücreler konuşma anında dolar.
Tek kaynak: ortak/anlatim/{sozcukler,altyazi}.json (küresel sn) + zamanlar.json. Yerel sn = t - t_bas.
Ok işareti metin değil kalem yoludur (yazı tipi alt kümesinde U+2192 yok)."""
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


def I(c, sozcuk, sira=0):
    """Cümle c'de sozcuk'un (noktalama atılmış) sira'ncı geçişinin dizini."""
    bul = [i for i, w in enumerate(SOZ[c]) if w["sozcuk"].strip(".,:;?!") == sozcuk]
    assert len(bul) > sira, (c, sozcuk, sira)
    return bul[sira]


def kelimeler(s, kimlik, x, y, idx, c, aile, agr, boy, renk=KRE, metin=None):
    """Sözcükleri konuşma zamanında tek tek açar. Döner: [(x, w)]."""
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


def uret():
    s = Y.Sahne(TB)
    S = s.S
    bal_ids = []
    # ---------------- öğrenci başı (peeps-kit) ----------------
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
    # ---------------- konuşma balonu: 2 satır Caveat 76 (küçülünce 61 px ≥ 56; 84 px'te 2. satır 809 > 741) ----------------
    BF, BX, BASE = 76, 255.0, (482, 574)
    sp = Y.genislik("Caveat", 700, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6, 7, 8))   # "Hocam, took off yerine" / "has taken off diyemez miyiz?"
    gens = [sum(Y.genislik("Caveat", 700, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = min(1032.0, BX + max(gens) + 36)
    s.yol("bal", Y.balon_sol(235, 396, x1b, 620, 176, 590), t0 + 0.1, 0.55, KRE, 4.6, 1, "cizgi", 0.7)
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
    xa, ya = pos[1][0], pos[1][2]             # took off altı sarı belirteç (öğrencinin değiştirmek istediği fiil)
    xb = pos[2][0] + pos[2][1]
    s.yol("bm", Y.el_cizgi(xa - 2, ya + 14, xb + 2, ya + 11), S(T(6, 1)), 0.3, SAR, 10, 0.85, "cizgi", 0.5)
    bal_ids.append("bm")
    xs, xe = pos[4][0], pos[6][0] + pos[6][1]  # has taken off üstüne kırmızı çarpı (tuzak çarpısı), "has" anında
    yb = pos[4][2]
    tx = S(T(6, 4))
    s.yol("xk1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xs - 14, yb - 52, (xs + xe) / 2, yb - 8, xe + 14, yb + 22),
          tx, 0.4, KIR, 11, 1, "cizgi", 0.7)
    s.yol("xk2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xe + 14, yb - 52, (xs + xe) / 2, yb - 14, xs - 14, yb + 22),
          tx + 0.42, 0.4, KIR, 11, 1, "cizgi", 0.7)
    s.olay(tx + 0.42, "vurus", 0.85)
    bal_ids += ["xk1", "xk2"]
    tr = S(T(7, 0))                            # çip Question -> Rule; balon + baş yukarı toplanır (ölçek 0,80)
    s.to("#ku-bolum", tr, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tr, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    # 16.11 DUZ3-0206I: toplanma tr − 0,5 (c6 bitişi tr − 0,59); "Hayır." başlarken baş yukarıda
    s.to("#balg", tr - 0.5, {"svgOrigin": "48 372", "scale": 0.80, "duration": 0.7, "ease": "power3.inOut"})

    # ---------------- tablo iskeleti (cümle 6 başı + 0,85–1,70 sn): etiket kutusu, tablo satırları, kod kartı ----------------
    t6 = T(6, 0)
    BY0, BH = 828.0, 92.0
    s.yol("bk", Y.el_kutu(X0, BY0, 984, BH), S(t6 + 0.85), 0.5, IKN, 4.6, 1, "cizgi", 0.5)
    TY1, TY2, TH = 952.0, 1058.0, 92.0
    TF = 68
    s.yol("tbl1", Y.el_kutu(X0, TY1, 984, TH), S(t6 + 1.2), 0.5, IKN, 4.6, 1, "cizgi", 0.5)
    s.yol("tbl2", Y.el_kutu(X0, TY2, 984, TH), S(t6 + 1.45), 0.5, IKN, 4.6, 1, "cizgi", 0.5)
    DX, DY, DW, DH = X0, 1170.0, 984.0, 160.0
    s.yol("kart", Y.el_kutu(DX, DY, DW, DH), S(t6 + 1.7), 0.6, KRE, 5, 1, "cizgi", 0.6)

    # ---------------- A: Hayır. + Bitmiş zaman (sarı bant) + fiil -> Simple Past (cümle 7 parça 1) ----------------
    A1, A2 = 704.0, 800.0
    hw = Y.genislik("Caveat", 700, "Hayır.", 100)
    s.yazi("hay", X0, A1, [("Hayır.", KRE)], "Caveat", 700, 100, S(T(7, 0)), 0.4, tur="tik", guc=0.6)
    bx = X0 + hw + 44
    bw = Y.genislik("Caveat", 700, "Bitmiş zaman", 100)
    s.yol("band", Y.el_cizgi(bx - 14, A1 - 24, bx + bw + 14, A1 - 28, 1), S(T(7, 1)), 0.55, SAR, 68, 0.42, "cizgi",
          0.4)
    kelimeler(s, "bz", bx, A1, (1, 2), 7, "Caveat", 700, 100)
    # "bağlandıkları fiili Simple Past'a çeker": fiil (soluk) -> Simple Past (eski: Present Perfect üstü çizili + yasak)
    fw = Y.genislik("Caveat", 700, "fiil", 88)
    tf_ = S(T(7, I(7, "fiili")))
    s.yazi("af", X0, A2, [("fiil", IKN)], "Caveat", 700, 88, tf_, 0.3, tur="tik", guc=0.5)
    s.yol("afo", Y.el_ok(X0 + fw + 26, A2 - 26, X0 + fw + 110, A2 - 28), tf_ + 0.25, 0.3, IKN, 9, 0.95, "cizgi",
          0.5)
    s.yazi("asp", X0 + fw + 134, A2, [("Simple Past", KRE)], "Fredoka", 700, 76, S(T(7, I(7, "Simple"))), 0.35,
           tur="tik", guc=0.6)

    # ---------------- B: üç bitmiş zaman sözcüğü el kutusunda (cümle 7 parça 2; 16.11: yasak çizgileri kalktı) ----------------
    LF = 64
    x = X0 + 40
    for n, m in enumerate(("ago", "yesterday", "last year")):
        t = S(T(7, I(7, m.split()[0])))
        w = Y.genislik("Fredoka", 700, m, LF)
        s.yazi("e%d" % n, x, BY0 + 68, [(m, IKN)], "Fredoka", 700, LF, t, 0.3, tur="tik", guc=0.55)
        x += w + 70

    # ---------------- C: tablo hücreleri (81,72–86,84): Finished → Simple Past / Unfinished → Present Perfect ----------------
    gA = max(Y.genislik("Fredoka", 700, "Finished", TF), Y.genislik("Fredoka", 700, "Unfinished", TF))
    ax0, ax1 = X0 + 32 + gA + 22, X0 + 32 + gA + 86
    cx2 = ax1 + 20
    iF, iU = I(7, "Finished"), I(7, "Unfinished")
    for kim, yy, c1, c2, i1, i2, renk in (("a", TY1, "Finished", "Simple Past", iF, iF + 2, KRE),
                                          ("b", TY2, "Unfinished", "Present Perfect", iU, iU + 2, SAR)):
        s.yazi("c1" + kim, X0 + 32, yy + 66, [(c1, KRE)], "Fredoka", 700, TF, S(T(7, i1)), 0.3, tur="tik", guc=0.55)
        s.yol("co" + kim, Y.el_ok(ax0, yy + 46, ax1, yy + 44), S(T(7, i1 + 1)) + 0.1, 0.3, renk, 8, 0.95, "cizgi",
              0.5)
        s.yazi("c2" + kim, cx2, yy + 66, [(c2, renk)], "Fredoka", 700, TF, S(T(7, i2)), 0.35, tur="tik", guc=0.6)

    # ---------------- D: kod kartı (cümle 7 parça 4): ago -> Simple Past / yet -> Present Perfect + çoğu zaman ----------------
    KF = 64                                    # 16.11: 72 -> 64, yet satırına "çoğu zaman" sığsın (dikey taban 50)
    iA, iY, iP = I(7, "ago'nun"), I(7, "yet'in"), I(7, "Present")
    ag = Y.genislik("Fredoka", 700, "ago", KF)
    yt = Y.genislik("Fredoka", 700, "yet", KF)
    s.yazi("k1a", DX + 44, DY + 74, [("ago", IKN)], "Fredoka", 700, KF, S(T(7, iA)), 0.3, tur="tik", guc=0.6)
    s.yol("k1o", Y.el_ok(DX + 44 + ag + 24, DY + 50, DX + 44 + ag + 104, DY + 48), S(T(7, iA + 1)), 0.3, IKN, 9,
          0.95, "cizgi", 0.55)
    s.yazi("k1b", DX + 44 + ag + 128, DY + 74, [("Simple Past", KRE)], "Fredoka", 700, KF, S(T(7, iA + 2)), 0.35,
           tur="tik", guc=0.6)
    s.yazi("k2a", DX + 44, DY + 142, [("yet", SAR)], "Fredoka", 700, KF, S(T(7, iY)), 0.3, tur="tik", guc=0.6)
    s.yol("k2o", Y.el_ok(DX + 44 + yt + 24, DY + 118, DX + 44 + yt + 104, DY + 116), S(T(7, iY + 1)), 0.3, SAR, 9,
          0.95, "cizgi", 0.55)
    s.yazi("k2b", DX + 44 + yt + 128, DY + 142, [("Present Perfect", KRE)], "Fredoka", 700, KF, S(T(7, iP)), 0.4,
           tur="tik", guc=0.6)
    # "çoğu zaman" (kural kapsamı, EK-5b): soluk el yazısı Present Perfect'in sağında, yazıldıktan sonra
    czx = DX + 44 + yt + 128 + Y.genislik("Fredoka", 700, "Present Perfect", KF) + 22
    assert czx + Y.genislik("Caveat", 700, "çoğu zaman", 52) <= DX + DW - 14, "çoğu zaman kart dışına taşar"
    s.yazi("k2c", czx, DY + 142, [("çoğu zaman", IKN)], "Caveat", 700, 52, S(T(7, iP)) + 0.35, 0.3, tur="tik",
           guc=0.4)
    tc = S(T1(7, len(SOZ[7]) - 1)) - 0.35
    s.yol("ctk", Y.tik_yolu(DX + DW - 96, DY + 16, 46), tc, 0.3, SAR, 9, 0.9, "cizgi", 0.55)
    s.olay(tc, "vurus", 0.8)
    LNF = 56
    nw = Y.genislik("Lexend", 700, "Next lesson", LNF)
    tn2 = tc + 0.1
    s.yazi("nx", 1032 - nw - 70, 1388, [("Next lesson", KRE)], "Lexend", 700, LNF, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M%.1f 1372 L%.1f 1372 M%.1f 1360 L%.1f 1372 L%.1f 1384" % (1032 - 56, 1032 - 10, 1032 - 24,
                                                                                1032 - 10, 1032 - 24), tn2 + 0.3,
          0.25, KRE, 5, 1, "cizgi", 0.4)
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
    kun = Y.kunye_svg("Question", "Rule")
    return s, {"kun": kun, "bal_ids": bal_ids, "altyazi": Y.altyazi_svg(parcalar)}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    logo = (48, 48, 96 * Y.LOGO_EN_BOY, 96)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), parca["kun"], None, logo, ek=parca["altyazi"],
               bal_ids=parca["bal_ids"], vin=1150))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

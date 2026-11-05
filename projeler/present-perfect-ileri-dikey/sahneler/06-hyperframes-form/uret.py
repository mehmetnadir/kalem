"""Sahne 06 DİKEY (İLERİ, 1080x1920, 785 kare, t_bas 68,60): öğrenci sorusu + kural. Present Perfect.
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
    # ---------------- konuşma balonu: 2 satır Caveat 76 (küçülünce 57 px) ----------------
    BF, BX, BASE = 76, 280.0, (484, 574)
    sp = Y.genislik("Caveat", 700, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6, 7))
    gens = [sum(Y.genislik("Caveat", 700, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = min(1032.0, BX + max(gens) + 40)
    s.yol("bal", Y.balon_sol(240, 396, x1b, 618, 176, 590), t0 + 0.1, 0.55, KRE, 4.6, 1, "cizgi", 0.7)
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
    xa, wa, ya = pos[1]                       # 69,95 ago altı sarı belirteç
    s.yol("bm", Y.el_cizgi(xa - 2, ya + 14, xa + wa + 2, ya + 11), S(T(6, 1)), 0.3, SAR, 10, 0.85, "cizgi", 0.5)
    bal_ids.append("bm")
    xs, xe = pos[4][0], pos[5][0] + pos[5][1]  # 71,15–71,99 has landed üstüne kırmızı çarpı
    yb = pos[4][2]
    tx = S(71.15)
    s.yol("xk1", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xs - 14, yb - 52, (xs + xe) / 2, yb - 8, xe + 14, yb + 22),
          tx, 0.4, KIR, 11, 1, "cizgi", 0.7)
    s.yol("xk2", "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (xe + 14, yb - 52, (xs + xe) / 2, yb - 14, xs - 14, yb + 22),
          tx + 0.42, 0.4, KIR, 11, 1, "cizgi", 0.7)
    s.olay(tx + 0.42, "vurus", 0.85)
    bal_ids += ["xk1", "xk2"]
    tr = S(73.62)                              # çip Question -> Rule; balon + baş yukarı toplanır (ölçek 0,75)
    s.to("#ku-bolum", tr, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tr, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    s.to("#balg", S(73.3), {"svgOrigin": "48 372", "scale": 0.75, "duration": 0.7, "ease": "power3.inOut"})

    # ---------------- tablo iskeleti (70,0–71,0): etiket kutusu, tablo satırları, kod kartı ----------------
    BY0, BH = 828.0, 92.0
    s.yol("bk", Y.el_kutu(X0, BY0, 984, BH), S(70.0), 0.5, IKN, 4.6, 1, "cizgi", 0.5)
    TY1, TY2, TH = 952.0, 1058.0, 92.0
    TF = 68
    s.yol("tbl1", Y.el_kutu(X0, TY1, 984, TH), S(70.35), 0.5, IKN, 4.6, 1, "cizgi", 0.5)
    s.yol("tbl2", Y.el_kutu(X0, TY2, 984, TH), S(70.6), 0.5, IKN, 4.6, 1, "cizgi", 0.5)
    DX, DY, DW, DH = X0, 1180.0, 984.0, 168.0
    s.yol("kart", Y.el_kutu(DX, DY, DW, DH), S(70.85), 0.6, KRE, 5, 1, "cizgi", 0.6)

    # ---------------- A: Hayır. + Bitmiş zaman (sarı bant) + Present Perfect yasaklı (73,62–78,10) ----------------
    A1, A2 = 704.0, 800.0
    hw = Y.genislik("Caveat", 700, "Hayır.", 100)
    s.yazi("hay", X0, A1, [("Hayır.", KRE)], "Caveat", 700, 100, S(T(7, 0)), 0.4, tur="tik", guc=0.6)
    bx = X0 + hw + 44
    bw = Y.genislik("Caveat", 700, "Bitmiş zaman", 100)
    s.yol("band", Y.el_cizgi(bx - 14, A1 - 24, bx + bw + 14, A1 - 28, 1), S(T(7, 1)), 0.55, SAR, 68, 0.42, "cizgi",
          0.4)
    kelimeler(s, "bz", bx, A1, (1, 2), 7, "Caveat", 700, 100)
    pp = kelimeler(s, "pp", X0, A2, (5, 6), 7, "Fredoka", 700, 76, metin=("Present", "Perfect"))
    pe = pp[1][0] + pp[1][1]
    ty_ = S(T(7, 7))
    s.yol("pst", Y.el_cizgi(X0 - 10, A2 - 28, pe + 10, A2 - 34, 2), ty_, 0.4, KIR, 11, 0.95, "cizgi", 0.7)
    s.olay(ty_ + 0.3, "vurus", 0.8)
    s.yazi("yas", pe + 50, A2, [("yasak", KIR)], "Caveat", 700, 88, ty_ + 0.3, 0.4, tur="tik", guc=0.5)

    # ---------------- B: üç kırmızı etiket el kutusunda, yasak çizgili (78,35–81,47) ----------------
    LF = 64
    x = X0 + 40
    for n, (i, m) in enumerate(((8, "ago"), (9, "yesterday"), (10, "last year"))):
        t = S(T(7, i))
        w = Y.genislik("Fredoka", 700, m, LF)
        s.yazi("e%d" % n, x, BY0 + 68, [(m, KIR)], "Fredoka", 700, LF, t, 0.3, tur="tik", guc=0.55)
        s.yol("es%d" % n, "M%.1f %.1f L%.1f %.1f" % (x - 10, BY0 + 78, x + w + 10, BY0 + 12), t + 0.4, 0.22, KRE, 8,
              0.95, "cizgi", 0.55)
        x += w + 70

    # ---------------- C: tablo hücreleri (81,72–86,84): Finished → Simple Past / Unfinished → Present Perfect ----------------
    gA = max(Y.genislik("Fredoka", 700, "Finished", TF), Y.genislik("Fredoka", 700, "Unfinished", TF))
    ax0, ax1 = X0 + 32 + gA + 22, X0 + 32 + gA + 86
    cx2 = ax1 + 20
    for kim, yy, c1, c2, i1, i2, renk in (("a", TY1, "Finished", "Simple Past", 12, 14, KRE),
                                          ("b", TY2, "Unfinished", "Present Perfect", 16, 18, SAR)):
        s.yazi("c1" + kim, X0 + 32, yy + 66, [(c1, KRE)], "Fredoka", 700, TF, S(T(7, i1)), 0.3, tur="tik", guc=0.55)
        s.yol("co" + kim, Y.el_ok(ax0, yy + 46, ax1, yy + 44), S(T(7, i1 + 1)) + 0.1, 0.3, renk, 8, 0.95, "cizgi",
              0.5)
        s.yazi("c2" + kim, cx2, yy + 66, [(c2, renk)], "Fredoka", 700, TF, S(T(7, i2)), 0.35, tur="tik", guc=0.6)

    # ---------------- D: kod kartı (87,09–92,77): ago → Simple Past (kırmızı) / yet → Present Perfect (sarı) ----------------
    KF = 72
    ag = Y.genislik("Fredoka", 700, "ago", KF)
    yt = Y.genislik("Fredoka", 700, "yet", KF)
    s.yazi("k1a", DX + 44, DY + 78, [("ago", KIR)], "Fredoka", 700, KF, S(T(7, 23)), 0.3, tur="tik", guc=0.6)
    s.yol("k1o", Y.el_ok(DX + 44 + ag + 24, DY + 54, DX + 44 + ag + 104, DY + 52), S(T(7, 24)), 0.3, KIR, 9, 0.95,
          "cizgi", 0.55)
    s.yazi("k1b", DX + 44 + ag + 128, DY + 78, [("Simple Past", KRE)], "Fredoka", 700, KF, S(T(7, 25)), 0.35,
           tur="tik", guc=0.6)
    s.yazi("k2a", DX + 44, DY + 150, [("yet", SAR)], "Fredoka", 700, KF, S(T(7, 27)), 0.3, tur="tik", guc=0.6)
    s.yol("k2o", Y.el_ok(DX + 44 + yt + 24, DY + 126, DX + 44 + yt + 104, DY + 124), S(T(7, 28)), 0.3, SAR, 9, 0.95,
          "cizgi", 0.55)
    s.yazi("k2b", DX + 44 + yt + 128, DY + 150, [("Present Perfect", KRE)], "Fredoka", 700, KF, S(T(7, 29)), 0.4,
           tur="tik", guc=0.6)
    tc = S(T1(7, 30)) - 0.35
    s.yol("ctk", Y.tik_yolu(DX + DW - 96, DY + 16, 46), tc, 0.3, SAR, 9, 0.9, "cizgi", 0.55)
    s.olay(tc, "vurus", 0.8)
    nw = Y.genislik("Lexend", 700, "Next lesson", 36)
    tn2 = tc + 0.1
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

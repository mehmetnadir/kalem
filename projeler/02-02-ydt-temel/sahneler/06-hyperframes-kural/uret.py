"""Sahne 06 kural kartı (HyperFrames, 1920x1080): öğrenci sorusu (soru anı 1) + üç bloklu `tanim` kartı
(olumlu / olumsuz / soru) + sağ bölgede destek görselleri (ek_ayir, örnek kartları, eşleşme çipleri).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn; cümle 20–27).
Olay zamanı = ilgili sözcüğün t0'ı. Yerel sn = küresel − t_bas."""
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
SOZ = {c: [w for w in _ALL if w["cumle"] == c] for c in range(20, 28)}
R = Y.RENK
KRE, IKN, SAR, KIR = R["murekkep"], R["ikincil"], R["vurgu"], R["kirmizi"]
TB = Z["t_bas"]

KX, KW = 96, 940                              # sol kart (tanım)
BLOK = ((350, 220), (590, 160), (770, 160))   # A olumlu, B olumsuz, C soru: (y, yükseklik)
RX, RW = 1100, 724                            # sağ bölge
FS = 54                                       # kart formül yazısı


def T(c, i):
    return SOZ[c][i]["t0"]


def kimlikler(s, bas):
    """s.svg[bas:] elemanlarının üst düzey id kümesi."""
    return {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}


def uret():
    s = Y.Sahne(TB)
    S = s.S
    tt = lambda c, i: S(T(c, i))  # noqa: E731
    gruplar = []

    def grup(ad, bas):
        gruplar.append((ad, kimlikler(s, bas)))

    def sol(ad, t, d=0.3):
        s.to("#" + ad, t, {"opacity": 0, "duration": d, "ease": "power1.in"})

    # ================= C20: öğrenci balonu (soru anı 1) =================
    b0 = len(s.svg)
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.72, 126.0, 150.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" '
                 'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (
                     BTX, BTY, BS, KRE, 3.0 / BS, "".join(
                         '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    t0 = max(tt(20, 0) - 0.14, 0.42)         # soğuk açılış değil: ilk 12 kare (0,40 sn) durgun
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    BF, BX, BASE = 44, 400.0, (236, 312)
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6))
    gens = [sum(Y.genislik("Fredoka", 600, SOZ[20][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = BX + max(gens) + 44
    s.yol("bal", Y.balon_sol(356, 178, x1b, 344, 282, 296), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    pos = {}
    for sat, base in zip(satir, BASE):
        x = BX
        for i in sat:
            m = SOZ[20][i]["sozcuk"]
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, tt(20, i), 0.12,
                   tur="tik" if i in (0, 4) else None)
            pos[i] = (x, w, base)
            x += w + sp
    # üç fiil çipi: söylendiği anda kutu + metin; fiil sarı daire; balonda fiil altı sarı çizgi
    CHIP = ((1, "I ", "go"), (2, "He ", "gets"), (3, "It ", "completes"))
    cx = 356.0
    CY, CH, CBASE = 430, 92, 494
    for i, on, fiil in CHIP:
        wo, wf = Y.genislik("Fredoka", 700, on, 52), Y.genislik("Fredoka", 700, fiil, 52)
        cw = wo + wf + 56
        t = tt(20, i)
        s.yol("cb%d" % i, Y.el_kutu(cx, CY, cw, CH), t, 0.4, IKN, 4, 1, "cizgi", 0.5)
        s.yazi("ct%d" % i, cx + 28, CBASE, [(on, KRE), (fiil, KRE)], "Fredoka", 700, 52, t + 0.12, 0.25,
               tur="tik", guc=0.5)
        # QA 13.11: fiil halkası harflere değiyordu → fiil altına vurgu el altçizgisi (fiil yazıldıktan sonra)
        s.yol("cd%d" % i, Y.el_cizgi(cx + 28 + wo - 2, CBASE + 12, cx + 28 + wo + wf + 2, CBASE + 10, i), t + 0.3,
              0.3, SAR, 7, 0.9, "parilti", 0.5)
        x, w, base = pos[i]
        s.yol("bm%d" % i, Y.el_cizgi(x - 2, base + 12, x + w + 2, base + 10), t, 0.3, SAR, 7, 0.85, None)
        cx += cw + 40
    ts = tt(20, 5)   # "neden"
    s.yazi("soru", cx + 10, CBASE + 16, [("?", SAR)], "Caveat", 700, 150, ts, 0.35, tur="tik", guc=0.55)
    grup("gOgr", b0)
    sol("gOgr", tt(21, 0) - 0.15, 0.4)       # soru anı biter, 0,5 sn duraklama, öğretmen cevabı başlar

    # ================= sol kart: üç blok =================
    t_k = tt(21, 0)
    etk = (("OLUMLU", tt(21, 0)), ("OLUMSUZ", tt(24, 0)), ("SORU", tt(26, 0)))
    for n, ((y, h), (ad, t)) in enumerate(zip(BLOK, etk)):
        s.yol("kb%d" % n, Y.el_kutu(KX, y, KW, h), t, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
        s.yazi("kt%d" % n, KX + 36, y + 48, [(ad, IKN)], "Lexend", 500, 30, t + 0.25, 0.3, tur="tik", guc=0.4)
    s.yazi("oz", KX, 336, [("özneye bağlı", SAR)], "Caveat", 700, 54, tt(21, 1), 0.5, tur="tik", guc=0.5)
    # blok A (C21): iki satır
    A1, A2 = BLOK[0][0] + 118, BLOK[0][0] + 196
    dizi = Y.dizi
    e1, _ = dizi(s, "a1", KX + 36, A1, [
        {"m": "I", "t": tt(21, 2)}, {"m": " · you", "t": tt(21, 3)}, {"m": " · we", "t": tt(21, 4)},
        {"m": " · they", "t": tt(21, 5), "bos": 18}, {"ok": 84, "t": tt(21, 6), "bos": 18},
        {"m": "V", "t": tt(21, 7), "r": KRE}], boy=FS)
    e2, _ = dizi(s, "a2", KX + 36, A2, [
        {"m": "he", "t": tt(21, 10)}, {"m": " · she", "t": tt(21, 11)}, {"m": " · it", "t": tt(21, 12), "bos": 18},
        {"ok": 84, "t": tt(21, 13), "bos": 18}, {"m": "V", "t": tt(21, 14)}, {"m": " + ", "t": tt(21, 15)},
        {"kutu": True, "m": "s", "t": tt(21, 16)}], boy=FS)
    # blok B (C24)
    B1 = BLOK[1][0] + 122
    eB, _ = dizi(s, "b1", KX + 36, B1, [
        {"m": "özne", "t": tt(24, 5)}, {"m": " + ", "t": tt(24, 9)},
        {"kutu": True, "m": "don't", "t": tt(24, 10), "bos": 4}, {"m": " / ", "t": tt(24, 11)},
        {"kutu": True, "m": "doesn't", "t": tt(24, 15), "bos": 4}, {"m": " + ", "t": tt(24, 16)},
        {"m": "V", "t": tt(24, 18)}], boy=FS)
    # blok C (C26)
    C1 = BLOK[2][0] + 122
    eC, _ = dizi(s, "c1", KX + 36, C1, [
        {"kutu": True, "m": "Do", "t": tt(26, 5), "bos": 4}, {"m": " / ", "t": tt(26, 6)},
        {"kutu": True, "m": "Does", "t": tt(26, 8), "bos": 4}, {"m": " + özne", "t": tt(26, 9)},
        {"m": " + V", "t": tt(26, 11)}, {"m": " ?", "t": tt(26, 11) + 0.25, "r": SAR}], boy=FS)
    for ad, e in (("A1", e1), ("A2", e2), ("B", eB), ("C", eC)):
        assert e <= KX + KW - 20, "kart satırı taştı %s: %.0f" % (ad, e)

    # ================= sağ bölge =================
    # --- C22: ek_ayir get|s, go|es, stud|ies ---
    g0 = len(s.svg)
    s.yazi("eh", RX, 450, [("he · she · it", IKN)], "Lexend", 500, 30, tt(22, 1), 0.3, tur="tik", guc=0.4)
    EY = (540, 660, 780)
    for n, (kok, ek, t1, t2) in enumerate((("get", "s", tt(22, 2), tt(22, 3)), ("go", "es", tt(22, 18), tt(22, 18) + 0.2),
                                           ("stud", "ies", tt(22, 19), tt(22, 19) + 0.2))):
        e, _ = dizi(s, "ea%d" % n, RX, EY[n], [{"m": kok, "t": t1, "bos": 2}, {"kutu": True, "m": ek, "t": t2}],
                    boy=80)
        assert e < RX + RW
    s.yazi("en1", RX, 870, [("ayrıntı önemli değil", IKN)], "Caveat", 700, 56, tt(22, 22), 0.6, tur="tik", guc=0.45)
    s.yazi("en2", RX, 940, [("takıyı tanımak yeter", KRE)], "Caveat", 700, 56, tt(22, 24), 0.6, tur="tik", guc=0.45)
    wn2 = Y.genislik("Caveat", 700, "takıyı tanımak yeter", 56)
    s.yol("en3", Y.el_cizgi(RX, 956, RX + wn2, 953, 2), tt(22, 26), 0.35, SAR, 6, 0.9, "cizgi", 0.5)
    grup("gEk", g0)
    sol("gEk", tt(23, 0) - 0.3)

    # --- C23: I eat fish. / She eats fish. + balık ---
    g0 = len(s.svg)
    s.yol("fk1", Y.el_kutu(RX, 400, 560, 118), tt(23, 0) - 0.05, 0.4, IKN, 4, 1, "cizgi", 0.5)
    dizi(s, "f1", RX + 30, 484, [{"m": "I", "t": tt(23, 0), "tik": True}, {"m": " eat", "t": tt(23, 1)},
                                 {"m": " fish.", "t": tt(23, 2)}], boy=64)
    s.yol("fk2", Y.el_kutu(RX, 560, 640, 118), tt(23, 3) - 0.05, 0.4, IKN, 4, 1, "cizgi", 0.5)
    e, _ = dizi(s, "f2", RX + 30, 644, [{"m": "She", "t": tt(23, 3), "tik": True}, {"m": " eat", "t": tt(23, 4)},
                                        {"kutu": True, "m": "s", "t": tt(23, 4) + 0.2},
                                        {"m": " fish.", "t": tt(23, 5), "bos": 0}], boy=64)
    assert e < RX + 640 - 10
    fb = Y.balik(RX + 170, 740, 300)
    for n, (d, st, du, w) in enumerate(zip(fb, (tt(23, 2), tt(23, 2) + 0.75, tt(23, 2) + 1.0, tt(23, 2) + 1.1),
                                           (0.7, 0.25, 0.1, 0.2), (5, 5, 9, 5))):
        s.yol("fb%d" % n, d, st, du, KRE, w, 1, "cizgi" if n == 0 else None, 0.45)
    grup("gF", g0)
    sol("gF", tt(24, 0) - 0.2)

    # --- C24: eşleşme çipleri (don't / doesn't) ---
    g0 = len(s.svg)
    s.yazi("yf", RX, 420, [("yardımcı fiil", SAR)], "Caveat", 700, 64, tt(24, 2), 0.5, tur="tik", guc=0.5)
    for n, (yb, kutu_t, parc) in enumerate((
            (450, tt(24, 5) - 0.1, [{"m": "I", "t": tt(24, 5)}, {"m": " · you", "t": tt(24, 6)},
                                    {"m": " · we", "t": tt(24, 7)}, {"m": " · they", "t": tt(24, 8), "bos": 16},
                                    {"ok": 50, "t": tt(24, 9), "bos": 12},
                                    {"kutu": True, "m": "don't", "t": tt(24, 10)}]),
            (590, tt(24, 11) - 0.1, [{"m": "he", "t": tt(24, 11)}, {"m": " · she", "t": tt(24, 12)},
                                     {"m": " · it", "t": tt(24, 13), "bos": 16},
                                     {"ok": 50, "t": tt(24, 14), "bos": 12},
                                     {"kutu": True, "m": "doesn't", "t": tt(24, 15)}]))):
        s.yol("ck%d" % n, Y.el_kutu(RX, yb, RW, 110), kutu_t, 0.4, IKN, 4, 1, "cizgi", 0.5)
        e, _ = dizi(s, "cp%d" % n, RX + 30, yb + 74, parc, boy=40)
        assert e < RX + RW - 16, "çip taştı %d: %.0f" % (n, e)
    grup("gC24", g0)
    sol("gC24", tt(25, 0) - 0.25)

    # --- C25: They don't eat fish. ---
    g0 = len(s.svg)
    s.yol("tk", Y.el_kutu(RX, 450, 650, 120), tt(25, 0) - 0.05, 0.4, IKN, 4, 1, "cizgi", 0.5)
    e, _ = dizi(s, "t", RX + 30, 532, [{"m": "They ", "t": tt(25, 0), "tik": True},
                                       {"kutu": True, "m": "don't", "t": tt(25, 1)},
                                       {"m": " eat", "t": tt(25, 2), "r": IKN}, {"m": " fish.", "t": tt(25, 3)}],
                boy=56)
    assert e < RX + 650 - 10, "C25 taştı %.0f" % e
    grup("gC25", g0)
    sol("gC25", tt(26, 9) - 0.25)

    # --- C26: eşleşme çipleri (Do / Does) + bilgi sorusu notu ---
    g0 = len(s.svg)
    for n, (yb, kutu_t, parc) in enumerate((
            (380, tt(26, 9) - 0.05, [{"m": "I · you · we · they", "t": tt(26, 9), "bos": 14},
                                     {"ok": 50, "t": tt(26, 10), "bos": 12},
                                     {"kutu": True, "m": "Do", "t": tt(26, 10) + 0.1}]),
            (520, tt(26, 10) - 0.05, [{"m": "he · she · it", "t": tt(26, 10), "bos": 14},
                                      {"ok": 50, "t": tt(26, 11), "bos": 12},
                                      {"kutu": True, "m": "Does", "t": tt(26, 11) + 0.1}]))):
        s.yol("dk%d" % n, Y.el_kutu(RX, yb, RW, 110), kutu_t, 0.4, IKN, 4, 1, "cizgi", 0.5)
        e, _ = dizi(s, "dp%d" % n, RX + 30, yb + 74, parc, boy=40)
        assert e < RX + RW - 16, "çip taştı %d: %.0f" % (n, e)
    s.yazi("bs1", RX, 740, [("bilgi sorusu:", SAR)], "Caveat", 700, 60, tt(26, 12), 0.5, tur="tik", guc=0.5)
    s.yazi("bs2", RX, 820, [("en başa soru sözcüğü", KRE)], "Caveat", 700, 60, tt(26, 15), 0.7, tur="tik", guc=0.5)
    grup("gC26", g0)
    sol("gC26", tt(27, 0) - 0.25)

    # --- C27: Do you eat fish? ---
    s.yol("qk", Y.el_kutu(RX, 450, 650, 120), tt(27, 0) - 0.05, 0.4, IKN, 4, 1, "cizgi", 0.5)
    e, _ = dizi(s, "q", RX + 30, 532, [{"kutu": True, "m": "Do", "t": tt(27, 0)}, {"m": " you", "t": tt(27, 1)},
                                       {"m": " eat", "t": tt(27, 2)}, {"m": " fish?", "t": tt(27, 3)}], boy=64)
    assert e < RX + 650 - 10, "C27 taştı %.0f" % e

    kun = Y.kunye_svg("Rule", "Rule", 2, 2)
    return s, {"kun": kun, "gruplar": gruplar}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

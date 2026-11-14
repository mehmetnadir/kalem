"""Sahne 14 Kapanış (02-04 YDT temel, HyperFrames, 1920x1080; cümle 18).
Son sahne: geçişsiz, +0,5 sn kuyruk. BRIEF §3 No 14: MEANING FIRST + üç soru satırı ses sırasıyla
kalemle yazılır (general or now? · permanent or temporary? · timetable or plan?); sonraki ders
kartı (02-05: Next lesson · Stative Verbs).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn;
i = cümle içi sıra). Yerel sn = küresel - t_bas. Ölçüler mantıksal px (yatay 1920) -> u()."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402
from yardim import u  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"]
           if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == 18]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]

# ---- yerleşim (mantıksal px) ----
SOL = u(220)                                 # sol blok hizası (başlık, numara halkaları)
BAS_Y, BAS_BOY = u(330), u(112)              # MEANING FIRST tabanı, boy (Fredoka 700)
SORU_Y = (u(500), u(628), u(756))            # üç soru satırının tabanı
SORU_X, SORU_BOY = u(332), u(88)             # soru satırı yazı başı, boy (Caveat 700)
SORU_ARA = Y.genislik("Caveat", 700, " ", SORU_BOY) + u(8)  # parça arası (boşluk + pay)
HALKA_R, NUM_BOY = u(36), u(46)              # numara halkası yarıçapı, numara boyu (Fredoka 700)
KART = (u(1220), u(492), u(560), u(236))     # sonraki ders kartı x, y, w, h
KART_IC, KART_BOY = u(48), u(72)             # kart iç boşluğu, kart başlığı boyu (Fredoka 700)
VURUS = 0.22                                 # kinetik sözcük (stil §4: 0,18-0,22 sn, back.out(1.6))
SORULAR = (  # satır başına parçalar: (metin, renk, sözcük sırası, sözcük başı)
    (("general", KRE, 7, "Genel"), ("or", IKN, 8, "mi"), ("now?", KRE, 9, "şu")),
    (("permanent", KRE, 12, "Kalıcı"), ("or", IKN, 13, "mı"), ("temporary?", KRE, 14, "geçici")),
    (("timetable", KRE, 16, "Tarife"), ("or", IKN, 17, "mi"), ("plan?", KRE, 18, "plan")),
)


def T(i, bas):
    """Cümle 18, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    assert w["sozcuk"].lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (
        i, w["sozcuk"], bas)
    return w["t0"]


def g(m, boy, aile="Fredoka", agr=700):
    return Y.genislik(aile, agr, m, boy)


def uret():
    s = Y.Sahne(Z["t_bas"])
    S = s.S
    olaylar = []

    def kayit(ad, t, i):
        olaylar.append((ad, t, "%s (%d)" % (SOZ[i]["sozcuk"], i)))

    # ---- "Dil sınavında": MEANING FIRST kinetik (sahne 07 belirtecinin geri dönüşü) ----
    wm, wf = g("MEANING ", BAS_BOY), g("FIRST", BAS_BOY)
    for kim, m, x, w, i, bas in (("mfa", "MEANING", SOL, wm, 0, "Dil"),
                                 ("mfb", "FIRST", SOL + wm, wf, 1, "sınav")):
        s.svg.append('<g id="%s" style="opacity:0"><text x="%.2f" y="%.2f" '
                     'font-family="Fredoka" font-weight="700" font-size="%.1f" fill="%s" '
                     'xml:space="preserve">%s</text></g>' % (kim, x, BAS_Y, BAS_BOY, KRE, m))
        t = S(T(i, bas))
        s.fromto("#" + kim, t, {"opacity": 0, "y": u(34), "scale": 0.86,
                                "svgOrigin": "%.1f %.1f" % (x + w / 2, BAS_Y)},
                 {"opacity": 1, "y": 0, "scale": 1, "duration": VURUS, "ease": "back.out(1.6)"})
        s.olay(t, "tik", 0.55)
        kayit(m + " (kinetik)", t, i)
    # ---- "boşluğu": sarı alt çizgi ----
    t = S(T(2, "boşluğu"))
    s.yol("mfc", Y.el_cizgi(SOL - u(6), BAS_Y + u(22), SOL + wm + wf + u(6), BAS_Y + u(21), 1.0),
          t, 0.45, SAR, u(10), 0.9, "cizgi", 0.6)
    kayit("sarı alt çizgi MEANING FIRST", t, 2)
    # ---- "üç soru": üç numara halkası kalemle (0,12 sn ara), numara halkanın içinde ----
    t3 = S(T(4, "üç"))
    for k, y in enumerate(SORU_Y):
        cx, cy, tk = SOL + HALKA_R, y - u(30), t3 + 0.12 * k
        s.yol("nh%d" % k, Y.el_daire(cx, cy, HALKA_R, HALKA_R, 0.7 * k), tk, 0.32, IKN, u(3.6),
              0.95, "cizgi", 0.4)
        n = str(k + 1)
        s.yazi("nn%d" % k, cx - g(n, NUM_BOY) / 2, cy + u(16), [(n, KRE)], "Fredoka", 700, NUM_BOY,
               tk + 0.12, 0.15, tur=None)
    kayit("numara halkaları 1-2-3", t3, 4)
    # ---- üç soru satırı: her parça söylendiği anda kalemle yazılır (Caveat) ----
    for k, (satir, y) in enumerate(zip(SORULAR, SORU_Y)):
        x = SORU_X
        for j, (m, renk, i, bas) in enumerate(satir):
            t = S(T(i, bas))
            w = g(m, SORU_BOY, "Caveat")
            s.yazi("q%d%d" % (k, j), x, y, [(m, renk)], "Caveat", 700, SORU_BOY, t,
                   round(0.12 + w / 1100, 2), tur=None if j == 1 else "tik", guc=0.45)
            kayit("soru %d: %s" % (k + 1, m.strip()), t, i)
            x += w + SORU_ARA
    # ---- "Sonraki derste -ing almayan fiilleri görüyoruz.": sonraki ders kartı (02-05) ----
    kx, ky, kw, kh = KART
    assert KART_IC + g("Stative Verbs", KART_BOY) <= kw - KART_IC, "kart başlığı taştı"
    t = S(T(20, "Sonraki"))
    s.yol("kk", Y.el_kutu(kx, ky, kw, kh), t, 0.55, IKN, u(3.6), 0.95, "cizgi", 0.55)
    kayit("kart çerçevesi", t, 20)
    t = S(T(21, "derste"))
    s.yazi("k1", kx + KART_IC, ky + u(76), [("Next lesson", IKN)], "Lexend", 500, u(36), t, 0.3,
           tur=None)
    kayit("Next lesson", t, 21)
    ws = g("Stative ", KART_BOY)
    for kim, m, x, i, bas in (("k2", "Stative", kx + KART_IC, 22, "-ing"),
                              ("k3", "Verbs", kx + KART_IC + ws, 24, "fiil")):
        t = S(T(i, bas))
        s.yazi(kim, x, ky + u(172), [(m, KRE)], "Fredoka", 700, KART_BOY, t, 0.3, tur="tik",
               guc=0.5)
        kayit(m, t, i)
    t = S(T(25, "görüyoruz"))
    s.yol("kok", Y.el_ok(kx + kw - u(190), ky + u(64), kx + kw - u(56), ky + u(64), 2), t, 0.3, SAR,
          u(7), 0.95, "cizgi", 0.5)
    kayit("sarı ok (ileri)", t, 25)
    bas, son = Y.kontrol(s, Z["kare"])
    return s, Y.kunye_svg("Next lesson", 3), olaylar, (bas, son)


if __name__ == "__main__":
    s, kun, olaylar, (bas, son) = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (u(56), u(1002), u(34) * Y.LOGO_EN_BOY, u(34))))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev),
          "hareket %.2f-%.2f sn" % (bas, son))
    for ad, t, soz in olaylar:
        print("  %6.2f sn  kare %3d  %-30s %s" % (t, round(t * 30), soz, ad))

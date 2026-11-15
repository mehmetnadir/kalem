"""Sahne 14 Kapanış (02-04 YDT temel dikey; HyperFrames 1080×1920, 434 kare; cümle 18).
Son sahne: geçişsiz, +0,5 sn kuyruk. MEANING FIRST + üç soru satırı ses sırasıyla yazılır;
sonraki ders kartı (02-05: Next lesson · Stative Verbs).
Yerleşim BRIEF-DIKEY §2-§3 satır 14 + SPEC.md: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform boş.
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (cümle 18, 27 sözcük). Yerel sn = küresel - t_bas."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402
from yardim import u  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text()) if w["cumle"] == 18]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]

# ---- yerleşim (mantıksal px) ----
SOL = u(96)                                                   # sol hiza: başlık + numara halkaları
BAS_Y, BAS_BOY = u(505), u(120)                               # MEANING FIRST tabanı, Fredoka 700 (bant y ≈ 422–545)
ALT_Y, ALT_W = BAS_Y + u(34), u(11)                           # sarı alt çizgi: taban + 0,28 em; kalınlık (belirteç 9–12)
SORU_Y = (u(690), u(840), u(990))                             # üç soru satırı tabanı (satır 150; bant 600–1060)
SORU_BOY = u(88)                                              # Caveat 700
HALKA_R, NUM_BOY = u(46), u(64)                               # numara halkası yarıçapı; numara Fredoka 700 64
HALKA_CX, HALKA_DY = SOL + HALKA_R, u(30)                     # halka merkezi x; merkez y = satır tabanı − HALKA_DY
SORU_X = SOL + 2 * HALKA_R + u(36)                            # soru yazı başı (≈ 224)
SORU_ARA = Y.genislik("Caveat", 700, " ", SORU_BOY) + u(8)     # parça arası; parçalar boşluksuz
KART = (u(48), u(1100), u(984), u(280))                       # sonraki ders kartı x, y, w, h (BRIEF §2.6: 984, x 48–1032)
KART_IC = u(40)                                               # kart iç boşluğu
NL_Y, NL_BOY = KART[1] + u(96), u(56)                         # Next lesson tabanı (≈ 1196), Lexend 500
SV_Y, SV_BOY = KART[1] + u(216), u(96)                        # Stative Verbs tabanı (≈ 1316), Fredoka 700
OK = (KART[0] + KART[2] - u(262), KART[0] + KART[2] - u(64), SV_Y - u(34))  # sarı ok (≈ 770 → 968, y ≈ 1282); kalınlık u(10)
VURUS = 0.22                                                  # kinetik sözcük (stil §4: back.out(1.6))
SORULAR = (  # satır başına parçalar: (metin, renk, sözcük sırası, sözcük başı)
    (("general", KRE, 7, "Genel"), ("or", IKN, 8, "mi"), ("now?", KRE, 9, "şu")),
    (("permanent", KRE, 12, "Kalıcı"), ("or", IKN, 13, "mı"), ("temporary?", KRE, 14, "geçici")),
    (("timetable", KRE, 16, "Tarife"), ("or", IKN, 17, "mi"), ("plan?", KRE, 18, "plan")),
)


def T(i, bas):
    """Cümle 18, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    assert w["sozcuk"].lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, w["sozcuk"], bas)
    return w["t0"]


def g(m, boy, aile="Fredoka", agr=700):
    return Y.genislik(aile, agr, m, boy)


def uret():
    s = Y.Sahne(Z["t_bas"])
    S = s.S
    olaylar = []

    def kayit(ad, t, i):
        olaylar.append((ad, t, "%s (%d)" % (SOZ[i]["sozcuk"], i)))

    # ---- Geometri doğrulamaları (SPEC §4.7) ----
    wm, wf = g("MEANING ", BAS_BOY), g("FIRST", BAS_BOY)
    kx, ky, kw, kh = KART
    ok_x0, ok_x1, ok_y = OK

    assert SOL + wm + wf <= Y.W - 48, "başlık sağ kenara taşıyor"
    assert BAS_Y - 0.72 * BAS_BOY >= 352, "başlık üstü içerik bandı dışında"
    for k, (satir, _) in enumerate(zip(SORULAR, SORU_Y)):
        w_top = sum(g(m, SORU_BOY, "Caveat") for m, _, _, _ in satir) + 2 * SORU_ARA
        assert SORU_X + w_top <= Y.W - 48, f"soru satırı {k+1} sağ kenara taşıyor: {SORU_X + w_top:.1f}"
    assert (SORU_Y[0] - HALKA_DY - HALKA_R) - ALT_Y >= u(40), "alt çizgi ile halka arası yakın"
    assert (SORU_Y[2] + 0.3 * SORU_BOY) + u(40) <= ky, "soru 3 ile kart arası yakın"
    assert kx + KART_IC + g("Next lesson", NL_BOY, "Lexend", 500) <= kx + kw - KART_IC, "Next lesson taştı"
    assert kx + KART_IC + g("Stative Verbs", SV_BOY) <= kx + kw - KART_IC, "Stative Verbs taştı"
    assert ok_x0 - (kx + KART_IC + g("Stative Verbs", SV_BOY)) >= u(48), "ok ile Stative Verbs arası yakın"
    assert ky + kh <= 1392, "kart içerik bandının altına taştı"
    for k, (satir, _) in enumerate(zip(SORULAR, SORU_Y)):
        for j in range(len(satir) - 1):
            m1, _, i1, b1 = satir[j]
            m2, _, i2, b2 = satir[j + 1]
            t1, t2 = S(T(i1, b1)), S(T(i2, b2))
            d1 = round(0.12 + g(m1, SORU_BOY, "Caveat") / 1100, 2)
            assert t1 + d1 < t2, f"soru {k+1} parça {m1} ({t1+d1:.2f}) sonraki parça {m2} ({t2:.2f}) başlangıcından önce değil"

    # ---- 1) MEANING FIRST kinetik (x SOL, taban BAS_Y; "Dil", "sınav") ----
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

    # ---- 2) "boşluğu": sarı alt çizgi MEANING FIRST ----
    t = S(T(2, "boşluğu"))
    s.yol("mfc", Y.el_cizgi(SOL - u(6), ALT_Y, SOL + wm + wf + u(6), ALT_Y - u(1), 1.0),
          t, 0.45, SAR, ALT_W, 0.9, "cizgi", 0.6)
    kayit("sarı alt çizgi MEANING FIRST", t, 2)

    # ---- 3) "üç": numara halkaları 1 · 2 · 3 (0,12 sn ara), numara Fredoka 700 64 ----
    t3 = S(T(4, "üç"))
    for k, y in enumerate(SORU_Y):
        cx, cy, tk = HALKA_CX, y - HALKA_DY, t3 + 0.12 * k
        s.yol("nh%d" % k, Y.el_daire(cx, cy, HALKA_R, HALKA_R, 0.7 * k), tk, 0.32, IKN, u(4), 0.95, "cizgi", 0.4)
        n = str(k + 1)
        s.yazi("nn%d" % k, cx - g(n, NUM_BOY) / 2, cy + u(22), [(n, KRE)], "Fredoka", 700, NUM_BOY, tk + 0.12, 0.15, tur=None)
    kayit("numara halkaları 1 · 2 · 3", t3, 4)

    # ---- 4) Üç soru satırı: her parça söylendiği anda kalemle yazılır (Caveat 700 88) ----
    for k, (satir, y) in enumerate(zip(SORULAR, SORU_Y)):
        x = SORU_X
        for j, (m, renk, i, bas) in enumerate(satir):
            t = S(T(i, bas))
            w = g(m, SORU_BOY, "Caveat")
            s.yazi("q%d%d" % (k, j), x, y, [(m, renk)], "Caveat", 700, SORU_BOY, t,
                   round(0.12 + w / 1100, 2), tur=None if j == 1 else "tik", guc=0.45)
            kayit("soru %d: %s" % (k + 1, m.strip()), t, i)
            x += w + SORU_ARA

    # ---- 5) "Sonraki derste durum bildiren fiilleri görüyoruz.": sonraki ders kartı (02-05) ----
    # 16.11 DUZ3: eski cümle «-ing almayan fiiller» mutlak kuraldı (durum fiilleri de -ing alabilir); Stative = «durum»
    t = S(T(20, "Sonraki"))
    s.yol("kk", Y.el_kutu(kx, ky, kw, kh), t, 0.55, IKN, u(4), 0.95, "cizgi", 0.55)
    kayit("kart çerçevesi", t, 20)

    t = S(T(21, "derste"))
    s.yazi("k1", kx + KART_IC, NL_Y, [("Next lesson", IKN)], "Lexend", 500, NL_BOY, t, 0.3, tur=None)
    kayit("Next lesson", t, 21)

    ws = g("Stative ", SV_BOY)
    for kim, m, x, i, bas in (("k2", "Stative", kx + KART_IC, 22, "durum"),
                              ("k3", "Verbs", kx + KART_IC + ws, 24, "fiil")):
        t = S(T(i, bas))
        s.yazi(kim, x, SV_Y, [(m, KRE)], "Fredoka", 700, SV_BOY, t, 0.3, tur="tik", guc=0.5)
        kayit(m, t, i)

    t = S(T(25, "görüyoruz"))
    # çizgi önce, uç sonra: Chrome dash desenini her alt yolda yeniden başlatır (uç çizgiyle aynı anda belirmesin)
    cizgi, uc = Y.el_ok(ok_x0, ok_y, ok_x1, ok_y, 2).split(" M", 1)
    s.yol("kok", cizgi, t, 0.22, SAR, u(10), 0.95, "cizgi", 0.5)
    s.yol("kok2", "M" + uc, t + 0.2, 0.1, SAR, u(10), 0.95, None)
    kayit("sarı ok (ileri)", t, 25)

    # ---- 6) Altyazı dilimleri (opaklık anahtarları, 06 kalıbı) ----
    dil = Y.altyazi_dilimleri([18])

    def aktif(t_an):
        k_sec = -1
        for i_dil, (t0, t1, _m) in enumerate(dil):
            if t0 - 0.05 <= t_an < t1 + 0.35:
                k_sec = i_dil
        return k_sec

    onc = -1
    for f in range(Z["kare"]):
        k_sec = aktif(Z["t_bas"] + f / 30)
        if k_sec != onc:
            if onc >= 0:
                s.set("#alt%d" % onc, round(f / 30, 4), {"opacity": 0})
            if k_sec >= 0:
                s.set("#alt%d" % k_sec, round(f / 30, 4), {"opacity": 1})
            onc = k_sec

    Y.kontrol(s, Z["kare"])
    s.olaylar = olaylar
    return s, Y.kunye_svg("Next lesson")


if __name__ == "__main__":
    s, kun = uret()
    dilimler = Y.altyazi_dilimleri([18])
    altyazi = Y.altyazi_svg([{"id": "alt%d" % i, "metin": m} for i, (_, _, m) in enumerate(dilimler)])
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (48, 48, round(96 * Y.LOGO_EN_BOY, 2), 96), ek=altyazi)
    )
    bas, son = Y.kontrol(s, Z["kare"])
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "hareket %.2f-%.2f sn" % (bas, son))
    for ad, t, soz in s.olaylar:
        print("  %6.2f sn  kare %3d  %-30s %s" % (t, round(t * 30), soz, ad))

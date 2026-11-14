"""Sahne 10 Tuzak + soru anı 2 (02-04 YDT temel, HyperFrames, 1920x1080; cümle 11 ve 12).
BRIEF §3 No 10. Cümle 11: `yaklas` ("Tuzak.") TRAP etiketi + tam genişlik kart (0,93 -> 1 ölçekle öne gelir);
"Türkçe" derken kartta TR etiketi; EN cümle "I live in İstanbul with my family." sözcük sözcük; "Türkçesi yaşıyorum"
derken TR satırı "Ailemle İstanbul'da yaşıyorum."; "yor" derken `ek_ayir` (yaşı-yor-um., *yor* sarı kutuda kayar);
"Yor eki" derken `bag` (*yor* -> *live* kalem çizgisi), "akla" derken ortada sarı soru işareti; "-ing" derken *live*
fosfor (V1, -ing yok).
Cümle 12: SORU ANI 2 (yanılgı: Türkçe "yaşıyorum" ile kalıcı durumda -ing kurulur): öğrenci başı (ogrenci-bas.svg, kadın,
K22) + el çizimi balon, soru sözcük sözcük (Fredoka 600, 44); "yaşıyorum" derken sarı nokta balonu *yor* kutusuna bağlar;
"living" sarı el altçizgisi. Duraklama (0,75 sn) ve cevap sahne 11'de.
Zaman tek kaynak: ../../zaman.json + ../../ortak/anlatim/sozcukler.json. Ölçüler u() ile (sabit px yok)."""
import json
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402
from yardim import u  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_ham = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
S11 = [w for w in _ham if w["cumle"] == 11]
S12 = [w for w in _ham if w["cumle"] == 12]
R = Y.RENK
KRE, IKN, SAR, ZEM = R["murekkep"], R["ikincil"], R["vurgu"], R["zemin"]
# Vurgu dolgusu üstündeki yazı ZEM ile yazılır: hf_tema text[fill=#1b1a17] -> --pilMetin (iki temada koyu, okunur).

# ---- yerleşim (mantıksal px, u() oranı) ----
KX, KY, KW, KH = u(96), u(228), u(1728), u(410)   # TRAP kartı
SX = u(150)                                       # kart içi yazı başı
FS = u(96)                                        # EN cümle (Fredoka 700)
B1 = KY + u(150)                                  # EN taban
TRB = u(72)                                       # TR cümle (Fredoka 600, ikincil)
TRL = u(30)                                       # "TR" etiketi (Lexend 700; taban 30)
B2 = KY + u(350)                                  # TR taban
KUTU_UST, KUTU_ALT = 0.64, 0.36                   # yor kutusu: taban üstü / altı (em; sahne 01 ile aynı)
TIRE_PAY, TIRE_ARA = 0.14, 0.08                   # kutu iç boşluğu, tire-kutu arası (em; sahne 01 QA)
QB = u(64)                                        # bag ortasındaki soru işareti (Fredoka 700)
BF = u(44)                                        # öğrenci sorusu (soru-ani.md: Fredoka 600, 44)
BTX, BTY, BS = u(150), u(690), 0.6 * u(1)         # öğrenci başı: çeviri, ölçek
BX0, BY0, BH = u(330), u(700), u(190)             # balon sol-üst, yükseklik


def T(i):
    return S11[i]["t0"]


def Q(i):
    return S12[i]["t0"]


def gen(m, b=FS, agr=700):
    return Y.genislik("Fredoka", agr, m, b)


def metin(m, x, y, renk, boy=TRB, agr=600):
    return ('<text x="%.2f" y="%.2f" font-family="Fredoka" font-weight="%d" font-size="%.1f" fill="%s" '
            'xml:space="preserve">%s</text>' % (x, y, agr, boy, renk, m))


def uret():
    assert [w["sozcuk"] for w in S11[5:12]] == ["I", "live", "in", "Istanbul", "with", "my", "family."], S11[5:12]
    assert [S11[i]["sozcuk"] for i in (0, 1, 12, 13, 15, 18, 22, 27)] == [
        "Tuzak.", "Türkçe", "Türkçesi", "yaşıyorum.", "yor", "Yor", "akla", "-ing"]
    assert len(S12) == 10 and S12[0]["sozcuk"] == "Hocam," and S12[5]["sozcuk"] == "living"
    s = Y.Sahne(Z["t_bas"])
    L = s.S
    kart = set()                          # yaklaş grubu: çerçeve + iki satır + işaretler
    bal_ids = []

    # ---------------- EN satırı konumları (fosfor yazının altında kalsın diye önce hesaplanır) ----------------
    sp = gen(" ")
    en = [(5, "I")] + [(6 + k, m) for k, m in enumerate(("live", "in", "İstanbul", "with", "my", "family."))]
    xs, x = {}, SX
    for i, m in en:
        xs[i] = x
        x += gen(m) + sp
    en_son = x - sp
    assert en_son <= KX + KW - u(60), "EN satırı karta taştı: %.0f" % en_son
    lw = gen("live")
    lx = xs[6] + lw / 2                                    # live ortası

    # fosfor (*live*, "-ing" 176,26): dolgu yazının altında; yazı dolgu %85 iken pilMetin kopyasına geçer
    fp = 0.10 * FS
    s.svg.append('<rect id="fos" x="%.2f" y="%.2f" width="0" height="%.2f" rx="%.1f" fill="%s" style="opacity:0"/>'
                 % (xs[6] - fp, B1 - 0.78 * FS, 0.90 * FS, u(10), SAR))
    kart.add("fos")
    tf = L(T(27))
    s.set("#fos", tf, {"opacity": 1})
    s.to("#fos", tf, {"attr": {"width": round(lw + 2 * fp, 2)}, "duration": 0.35, "ease": "power2.out"})
    s.olay(tf, "cizgi", 0.5)

    # ---------------- TRAP etiketi + kart (Tuzak. 162,88) ----------------
    t0 = L(T(0))
    s.yazi("etiket", KX, KY - u(26), [("TRAP", SAR)], "Lexend", 700, u(36), t0, 0.3, tur="tik", guc=0.45)
    s.yol("kr", Y.el_kutu(KX, KY, KW, KH), t0 + 0.1, 0.7, KRE, u(4.5), 1, "cizgi", 0.7)
    kart.add("kr")
    org = "%.1f %.1f" % (KX + KW / 2, KY + KH / 2)
    s.fromto("#kartg", t0, {"scale": 0.93, "svgOrigin": org},
             {"scale": 1, "svgOrigin": org, "duration": 0.9, "ease": "power3.out"})

    # ---------------- "TR" etiketi ("Türkçe ek seni yanıltabilir." 163,84) ----------------
    s.yazi("trl", SX, B2, [("TR", IKN)], "Lexend", 700, TRL, L(T(1)), 0.2, tur="tik", guc=0.35)
    kart.add("trl")
    TX = SX + Y.genislik("Lexend", 700, "TR", TRL) + u(22)

    # ---------------- EN cümle: I(5) live(6) in(7) İstanbul(8) with(9) my(10) family.(11) ----------------
    for i, m in en:
        s.yazi("w%d" % i, xs[i], B1, [(m, KRE)], "Fredoka", 700, FS, L(T(i)), 0.18 if i != 11 else 0.3,
               tur="tik" if i in (5, 8, 11) else None, guc=0.5)
        kart.add("w%d" % i)
    # live'ın fosfor üstü kopyası (pilMetin): aynı kırpmayı kullanır, fosfor %85 dolunca açılır
    s.svg.append('<g id="w6z" font-family="Fredoka" font-weight="700" font-size="%s" clip-path="url(#c_w6)" '
                 'style="opacity:0"><text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">live</text></g>'
                 % (FS, xs[6], B1, ZEM))
    kart.add("w6z")
    s.set("#w6z", tf + 0.3, {"opacity": 1})
    s.set("#w6", tf + 0.3, {"opacity": 0})

    # ---------------- TR cümle: "Ailemle İstanbul'da" (Türkçesi 168,66) + "yaşıyorum." (169,54) ----------------
    on = "Ailemle İstanbul'da "
    s.yazi("tra", TX, B2, [(on.rstrip(), IKN)], "Fredoka", 600, TRB, L(T(12)), 0.45, tur="tik", guc=0.45)
    kart.add("tra")
    xa = TX + gen(on, TRB, 600)
    wa, wy, wu, wt = (gen(m, TRB, 600) for m in ("yaşı", "yor", "um.", "-"))
    p = TIRE_PAY * TRB
    xy0, xu0 = xa + wa, xa + wa + wy                       # bitişik (ayrılmadan önce)
    ara = TIRE_ARA * TRB
    dy, du = wt + ara + p, 2 * (wt + ara + p)               # kayma: yor bir tire + ara + iç boşluk, um iki katı
    kx0, kx1 = xy0 + dy - p, xy0 + dy + wy + p              # kutunun son yeri
    ky, kh, sag = B2 - KUTU_UST * TRB, (KUTU_UST + KUTU_ALT) * TRB, xu0 + du + wu
    assert sag <= KX + KW - u(60), "TR satırı karta taştı: %.0f" % sag
    s.defs.append('<clipPath id="c_trw"><rect id="r_trw" x="%.1f" y="%.1f" width="0" height="%.1f"/></clipPath>'
                  % (xa - u(8), B2 - TRB * 1.05, TRB * 1.5))
    s.svg.append('<g id="trw" clip-path="url(#c_trw)"><rect id="ekk" x="%.2f" y="%.2f" width="0" height="%.2f" '
                 'rx="%.1f" fill="%s"/><g id="eka">%s</g><g id="eky"><g id="eky1">%s</g><g id="eky2" style="opacity:0">'
                 '%s</g></g><g id="eku">%s</g><g id="ekt" style="opacity:0">%s%s</g></g>'
                 % (xy0 + wy / 2, ky, kh, u(12), SAR, metin("yaşı", xa, B2, IKN), metin("yor", xy0, B2, IKN),
                    metin("yor", xy0, B2, ZEM), metin("um.", xu0, B2, IKN), metin("-", xa + wa, B2, IKN),
                    metin("-", kx1 + ara, B2, IKN)))
    kart.add("trw")
    s.cmd.append({"m": "rev", "id": "r_trw", "t": L(T(13)), "d": 0.4, "w": round(sag - xa + u(24), 1)})
    s.olay(L(T(13)), "tik", 0.45)
    # ek_ayir ("yor" 171,30): yor kutuyla kayar, um iki katı; kutu %90 dolunca yazı pilMetin'e döner (sahne 01 QA 2);
    # tireler kayma %99 bitince belirir (sahne 01 QA 3)
    te = L(T(15))
    kay = {"duration": 0.36, "ease": "power3.out"}
    s.to("#eky", te, dict(kay, x=round(dy, 2)))
    s.to("#eku", te, dict(kay, x=round(du, 2)))
    s.to("#ekk", te, dict(kay, attr={"x": round(kx0, 2), "width": round(kx1 - kx0, 2)}))
    s.set("#eky1", te + 0.20, {"opacity": 0})
    s.set("#eky2", te + 0.20, {"opacity": 1})
    s.to("#ekt", te + 0.28, {"opacity": 1, "duration": 0.15, "ease": "power1.out"})
    s.olay(te, "cizgi", 0.55)

    # ---------------- bag: yor -> live ("Yor eki" 172,74), ortada "?" ("akla" 174,26) ----------------
    yx = (kx0 + kx1) / 2
    en_alt = B1 + 0.24 * FS                                # EN satırı inişli harf altı (my, family)
    hy = (en_alt + ky) / 2                                 # yatay kol: iki satırın tam ortası
    assert ky - en_alt >= u(110), "satır arası bag için dar: %.0f" % (ky - en_alt)
    qw = Y.genislik("Fredoka", 700, "?", QB)
    qx = (lx + yx) / 2 - qw / 2                            # soru işareti sol kenarı
    bos = u(18)                                            # soru işareti ile çizgi arası
    ly_uc = B1 + u(20)                                     # ok ucu: live tabanının altında
    r1 = u(40)
    d1 = ("M%.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f"
          % (yx, ky - u(12), yx, hy + r1, yx, hy, yx - r1, hy + u(1), qx + qw + bos, hy - u(2)))
    d2 = ("M%.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f"
          % (qx - bos, hy - u(1), lx + r1, hy + u(1), lx, hy, lx, hy - r1, lx, ly_uc,
             lx - u(13), ly_uc + u(20), lx, ly_uc, lx + u(13), ly_uc + u(20)))
    tb = L(T(18))
    s.yol("bag1", d1, tb, 0.45, KRE, u(4), 1, "cizgi", 0.55)
    s.yol("bag2", d2, tb + 0.45, 0.5, KRE, u(4), 1, None)
    kart.update(("bag1", "bag2"))
    qbas = hy + 0.36 * QB                                  # "?" görsel ortası yatay kolda
    s.svg.append('<g id="qm" style="opacity:0">%s</g>' % metin("?", qx, qbas, SAR, QB, 700))
    kart.add("qm")
    tq = L(T(22))
    qo = "%.1f %.1f" % (qx + qw / 2, hy)
    s.fromto("#qm", tq, {"opacity": 0, "scale": 0.4, "svgOrigin": qo},
             {"opacity": 1, "scale": 1, "svgOrigin": qo, "duration": 0.3, "ease": "back.out(2)"})
    s.olay(tq, "tik", 0.55)
    assert qbas - 0.74 * QB - en_alt >= u(20) and ky - qbas >= u(20), "soru işareti satırlara yakın"
    assert qx - bos > lx + r1 and qx + qw + bos < yx - r1, "soru işareti bag köşesine biniyor"

    # ---------------- SORU ANI 2: öğrenci başı + balon ("Hocam," 177,85) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.3f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, u(2.8) / BS, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    tb = L(Q(0)) - 0.2
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(tb + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(tb + 0.05 * i, "cizgi", 0.55)
    # ekran metni (senaryo §4 satır 12): "Hocam, Türkçesi yaşıyorum. / I am living in İstanbul olmaz mı?"
    ekran = ["Hocam,", "Türkçesi", "yaşıyorum.", "I", "am", "living", "in", "İstanbul", "olmaz", "mı?"]
    spb = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2), (3, 4, 5, 6, 7, 8, 9))
    gens = [sum(Y.genislik("Fredoka", 600, ekran[i], BF) for i in sat) + spb * (len(sat) - 1) for sat in satir]
    x1b = BX0 + max(gens) + u(70)
    BASE = (BY0 + u(74), BY0 + u(138))
    s.yol("bal", Y.balon_sol(BX0, BY0, x1b, BY0 + BH, BTX + u(130), BY0 + u(110)), tb + 0.1, 0.55, KRE, u(4.2), 1,
          "cizgi", 0.7)
    bal_ids.append("bal")
    pos = {}
    for sat, base in zip(satir, BASE):
        x = BX0 + u(35)
        for i in sat:
            m = ekran[i]
            w = Y.genislik("Fredoka", 600, m, BF)
            pos[i] = (x, base, w)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, L(Q(i)), 0.12 if i != 9 else 0.25,
                   tur="tik" if i in (0, 3) else None)
            bal_ids.append("bw%d" % i)
            x += w + spb
    assert x1b < KX + KW and BY0 + BH < u(960), "balon sınır dışı"
    assert BY0 - (KY + KH) >= u(50), "balon karta yakın"
    # sarı nokta: balon üst kenarından *yor* kutusuna ("yaşıyorum." 179,37)
    dx0 = min(yx, x1b - u(70))
    dy0 = BY0 - u(2)
    s.yol("bg", Y.el_cizgi(dx0, dy0, yx, ky + kh + u(10), 2.0), L(Q(2)), 0.4, SAR, u(4.5), 0.9, "cizgi", 0.45)
    s.svg.append('<circle id="bgd" cx="%.1f" cy="%.1f" r="%.1f" fill="%s" style="opacity:0"/>' % (dx0, dy0, u(10), SAR))
    do = "%.1f %.1f" % (dx0, dy0)
    s.fromto("#bgd", L(Q(2)), {"opacity": 0, "scale": 0.3, "svgOrigin": do},
             {"opacity": 1, "scale": 1, "svgOrigin": do, "duration": 0.25, "ease": "back.out(2)"})
    bal_ids.extend(("bg", "bgd"))
    # "living" sarı el altçizgisi: sözcük göründükten 0,3 sn sonra (13.11 QA işaret kuralı)
    lxb, lbb, lwb = pos[5]
    s.yol("ml", Y.el_cizgi(lxb - u(3), lbb + u(13), lxb + lwb + u(3), lbb + u(12), 1), L(Q(5)) + 0.3, 0.35, SAR, u(8),
          0.85, "cizgi", 0.45)
    bal_ids.append("ml")
    Y.kontrol(s, Z["kare"])
    return s, Y.kunye_svg("Trap", 3), bal_ids, kart


if __name__ == "__main__":
    s, kun, bal_ids, kart = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (u(56), u(1002), u(34) * Y.LOGO_EN_BOY, u(34)), bal_ids=bal_ids,
               gruplar=[("kartg", kart)]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

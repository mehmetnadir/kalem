"""Sahne 10 Tuzak + soru anı 2 (02-03 YDT temel, HyperFrames, 1920x1080; cümle 12 ve 13).
Cümle 12: `yaklas` (kart öne gelir, Tuzak. 168,15 sn) tek tam genişlik kart "We believe this situation is temporary." +
TRAP etiketi; cümle sözcük sözcük konuşmayla; `believe` sarı daire; `temporary` sarı belirteç; köşede kalemle `-ing`
yazılır, soru işareti konur.
Cümle 13: SORU ANI 2 (yanılgı: Türkçe "şu anda" duygusuyla durum fiiline -ing eklenir): öğrenci başı (ogrenci-bas.svg) +
el çizimi balon, soru sözcük sözcük; "şu anda" sarı belirteç; sarı nokta balonu karttaki `-ing ?` notuna bağlar.
Duraklama (0,75 sn) ve cevap sahne 11'de. Zaman tek kaynak: ../../zaman.json + ../../ortak/anlatim/sozcukler.json."""
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
_ham = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
S12 = [w for w in _ham if w["cumle"] == 12]
S13 = [w for w in _ham if w["cumle"] == 13]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]

# ---- yerleşim (px) ----
KX, KY, KW, KH = 96, 230, 1728, 330       # TRAP kartı
FS = 96                                   # kart yazısı (Fredoka 700)
SX = 150                                  # yazı başı
B1, B2 = 400, 520                         # yazı taban çizgileri
BF = 48                                   # öğrenci sorusu (Fredoka 600)
BTX, BTY, BS = 170.0, 640.0, 0.7          # öğrenci başı: çeviri, ölçek
BX0, BY0 = 360.0, 640.0                   # balon sol-üst
BH = 210


def T(i):
    return S12[i]["t0"]


def Q(i):
    return S13[i]["t0"]


def gen(m, b=FS):
    return Y.genislik("Fredoka", 700, m, b)


def uret():
    s = Y.Sahne(Z["t_bas"])
    L = s.S
    kart = set()                          # yaklaş grubu: çerçeve + cümle + işaretler
    bal_ids = []

    # ---------------- TRAP etiketi + kart (Tuzak. 168,15) ----------------
    t0 = L(S12[0]["t0"])
    s.yazi("etiket", KX, 205, [("TRAP", SAR)], "Lexend", 700, 36, t0, 0.3, tur="tik", guc=0.45)
    s.yol("kr", Y.el_kutu(KX, KY, KW, KH), t0 + 0.1, 0.7, KRE, 4.5, 1, "cizgi", 0.7)
    kart.add("kr")
    s.fromto("#kartg", t0, {"scale": 0.93, "svgOrigin": "960 395"},
             {"scale": 1, "svgOrigin": "960 395", "duration": 0.9, "ease": "power3.out"})
    # ---------------- cümle: We(9) believe(10) this(11) situation(12) is(13) temporary.(14) ----------------
    sp = gen(" ")
    xs = {}
    x = SX
    for i, m in ((9, "We"), (10, "believe"), (11, "this"), (12, "situation")):
        xs[i] = x
        s.yazi("w%d" % i, x, B1, [(m, KRE)], "Fredoka", 700, FS, L(T(i)), 0.18, tur="tik" if i == 9 else None, guc=0.5)
        kart.add("w%d" % i)
        x += gen(m) + sp
    line1_end = x - sp
    xs[13] = SX
    s.yazi("w13", SX, B2, [("is", KRE)], "Fredoka", 700, FS, L(T(13)), 0.15, tur=None)
    kart.add("w13")
    xs[14] = SX + gen("is") + sp
    s.yazi("w14", xs[14], B2, [("temporary.", KRE)], "Fredoka", 700, FS, L(T(14)), 0.5, tur="tik", guc=0.5)
    kart.add("w14")
    line2_end = xs[14] + gen("temporary.")
    assert line1_end <= KX + KW - 60, "satır 1 karta taştı: %.0f" % line1_end
    # believe: sarı daire (173,84)
    bw = gen("believe")
    s.yol("dr", Y.el_cizgi(xs[10] - 2, B1 + 16, xs[10] + bw + 2, B1 + 15, 1), L(T(10)) + 0.12, 0.5, SAR, 10, 0.9,
          "cizgi", 0.5)   # halka yerine el altçizgisi (13.11 QA)
    kart.add("dr")
    # temporary: sarı belirteç ("geçici" 177,29)
    tw = gen("temporary")
    s.yol("mt", Y.el_cizgi(xs[14] - 4, B2 + 16, xs[14] + tw + 4, B2 + 15, 1), L(T(17)), 0.45, SAR, 10, 0.85, "cizgi", 0.5)
    kart.add("mt")
    # köşede -ing (181,45) ve soru işareti (182,09)
    IF, IX_, IY = 120, 1260, 520
    s.yazi("ing", IX_, IY, [("-ing", SAR)], "Caveat", 700, IF, L(T(23)), 0.5, tur="tik", guc=0.55)
    kart.add("ing")
    iw = Y.genislik("Caveat", 700, "-ing", IF)
    s.yazi("soru", IX_ + iw + 24, IY, [("?", IKN)], "Fredoka", 700, IF, L(T(25)), 0.25, tur="tik", guc=0.55)
    kart.add("soru")
    assert IX_ > line2_end + 60, "-ing notu cümleye değiyor"
    assert IX_ + iw + 24 + gen("?", IF) <= KX + KW - 40, "-ing notu karttan taştı"

    # ---------------- SORU ANI 2: öğrenci başı + balon (183,36) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, 2.8 / BS, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    tb = L(Q(0)) - 0.2
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(tb + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(tb + 0.05 * i, "cizgi", 0.55)
    spb = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2, 3), (4, 5, 6, 7, 8))   # Hocam, şu anda inanıyoruz. / We are believing. Olmaz mı?
    gens = [sum(Y.genislik("Fredoka", 600, S13[i]["sozcuk"], BF) for i in sat) + spb * (len(sat) - 1) for sat in satir]
    x1b = BX0 + max(gens) + 70
    BASE = (BY0 + 78, BY0 + 150)
    s.yol("bal", Y.balon_sol(BX0, BY0, x1b, BY0 + BH, BTX + 148, BY0 + 120), tb + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    pos = {}
    for sat, base in zip(satir, BASE):
        x = BX0 + 35
        for i in sat:
            m = S13[i]["sozcuk"]
            w = Y.genislik("Fredoka", 600, m, BF)
            pos[i] = (x, base, w)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, L(Q(i)), 0.12 if i != 8 else 0.25,
                   tur="tik" if i in (0, 4) else None)
            bal_ids.append("bw%d" % i)
            x += w + spb
    assert x1b < 1800 and BY0 + BH < 960
    # "şu anda" sarı belirteç (184,24-184,64)
    xa, xb = pos[1][0], pos[2][0] + pos[2][2]
    s.yol("ms", Y.el_cizgi(xa - 4, BASE[0] + 12, xb + 4, BASE[0] + 11, 1), L(Q(1)), 0.35, SAR, 8, 0.85, "cizgi", 0.45)
    bal_ids.append("ms")
    # sarı nokta: balon üstünden karttaki `-ing ?` notuna ("believing." 186,25)
    nx, ny = IX_ + iw / 2, IY + 26                       # -ing altı
    dx0 = x1b - 70                                       # balon üst kenarında nokta
    s.yol("bg", Y.el_cizgi(dx0, BY0 - 2, nx, ny, 3.0), L(Q(6)), 0.4, SAR, 4.5, 0.9, "cizgi", 0.45)
    s.svg.append('<circle id="bgd" cx="%.1f" cy="%.1f" r="10" fill="%s" style="opacity:0"/>' % (dx0, BY0 - 2, SAR))
    s.fromto("#bgd", L(Q(6)), {"opacity": 0, "scale": 0.3, "svgOrigin": "%.1f %.1f" % (dx0, BY0 - 2)},
             {"opacity": 1, "scale": 1, "svgOrigin": "%.1f %.1f" % (dx0, BY0 - 2), "duration": 0.25, "ease": "back.out(2)"})
    Y.kontrol(s, Z["kare"])
    return s, Y.kunye_svg("Trap", 3), bal_ids, kart


if __name__ == "__main__":
    s, kun, bal_ids, kart = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), bal_ids=bal_ids,
               gruplar=[("kartg", kart)]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

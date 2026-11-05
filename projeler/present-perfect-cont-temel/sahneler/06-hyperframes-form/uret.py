"""Sahne 06 (PPC temel: öğrenci sorusu + form) index.html + olay listesi üretici; 681 kare, t_bas 61,51.
Tek kaynak: zamanlar.json (küresel sn) -> yerel sn = t - t_bas. Komut listesi veri olarak JS'e gömülür,
olaylar aynı çağrılardan toplanır (olay.py yalnız bu modülü içe alır)."""
import json
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
R = Y.RENK
KRE, IKN, SAR, KIR, ZEM = R["murekkep"], R["ikincil"], R["vurgu"], R["kirmizi"], R["zemin"]
TB = Z["t_bas"]


def S(t):
    return round(t - TB, 4)


class Sahne:
    def __init__(self):
        self.defs, self.svg, self.cmd, self.ev = [], [], [], []

    # -- olay ve komut --
    def olay(self, t, tur, guc):
        self.ev.append({"kare": round(t * 30), "tur": tur, "guc": guc})

    def to(self, sel, t, v, olay=None):
        self.cmd.append({"m": "to", "s": sel, "t": round(t, 4), "v": v})

    def fromto(self, sel, t, a, v):
        self.cmd.append({"m": "fromTo", "s": sel, "t": round(t, 4), "a": a, "v": v})

    def goster(self, sel, t, d=0.35, dx=0, dy=0, sc=None):
        a = {"opacity": 0, "x": dx, "y": dy}
        v = {"opacity": 1, "x": 0, "y": 0, "duration": d, "ease": "power3.out"}
        if sc is not None:
            a["scale"], v["scale"] = sc, 1
        self.fromto(sel, t, a, v)

    # -- yol (kendini çizen kalem) --
    def yol(self, id, d, t, sure, stroke=KRE, w=4.0, alfa=1.0, tur="cizgi", guc=0.55, ek=""):
        self.svg.append('<path id="%s" d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
                        'stroke-linejoin="round" style="opacity:0" %s/>' % (id, d, stroke, w, ek))
        self.cmd.append({"m": "draw", "id": id, "t": round(t, 4), "d": round(sure, 4), "a": alfa})
        if tur:
            self.olay(t, tur, guc)

    # -- yazı (soldan maske) --
    def yazi(self, id, x, y, parcalar, aile, agr, boy, t, d=0.12, anchor="start", tur="tik", guc=0.5,
             sar_ek=""):
        ws = [Y.genislik(aile, agr, p[0], boy) for p in parcalar]
        W = sum(ws)
        x0 = x - W if anchor == "end" else x
        cx, tx = x0, ""
        for (m, fill), w in zip(parcalar, ws):
            tx += ('<text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">%s</text>' % (cx, y, fill, m))
            cx += w
        self.defs.append('<clipPath id="c_%s"><rect id="r_%s" x="%.1f" y="%.1f" width="0" height="%.1f"/></clipPath>'
                         % (id, id, x0 - 8, y - boy * 1.05, boy * 1.5))
        self.svg.append('<g id="%s" font-family="%s" font-weight="%d" font-size="%s" clip-path="url(#c_%s)" %s>%s</g>'
                        % (id, aile, agr, boy, id, sar_ek, tx))
        self.cmd.append({"m": "rev", "id": "r_" + id, "t": round(t, 4), "d": d, "w": round(W + 20, 1)})
        if tur:
            self.olay(t, tur, guc)
        return x0, W


def el_daire(cx, cy, rx, ry, kayma=0.0):
    """Hafif eğik, kapanmayan el elipsi (yol d)."""
    import math
    pts = []
    for i in range(0, 38):
        a = -2.3 + i * (2 * math.pi * 1.04) / 37
        r = 1 + 0.025 * math.sin(a * 3 + kayma)
        pts.append((cx + rx * r * math.cos(a) - 6 * math.sin(a), cy + ry * r * math.sin(a) + 4 * math.cos(a)))
    return "M%.1f %.1f " % pts[0] + " ".join("L%.1f %.1f" % p for p in pts[1:])


def el_cizgi(x0, y0, x1, y1, egim=3.0):
    """Hafif eğri, hafif eğik el çizgisi."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    return "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x0, y0, mx, my + egim * 2, x1, y1 + egim * 0.4)


def el_kutu(x, y, w, h):
    """Dört kenarı hafif eğri el kutusu (tek yol)."""
    return ("M%.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f "
            "Q%.0f %.0f %.0f %.0f" % (x + 4, y + 3, x + w / 2, y - 3, x + w - 3, y + 1, x + w + 3, y + h / 2,
                                      x + w - 1, y + h - 2, x + w / 2, y + h + 4, x + 5, y + h + 1,
                                      x - 3, y + h / 2, x + 2, y + 6, x + 1, y + 2, x + 5, y + 2))


def el_cift_ok(x0, y0, x1, y1, bas=16):
    """Çift yönlü el oku: gövde + iki ucunda ok başı (tek yol)."""
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2 + 3
    p = "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x0, y0, mx, my, x1, y1)
    for (x, y, d) in ((x1, y1, a), (x0, y0, a + math.pi)):
        for s_ in (-0.5, 0.5):
            p += " M%.1f %.1f L%.1f %.1f" % (x - bas * math.cos(d + s_), y - bas * math.sin(d + s_), x, y)
    return p


def el_ok(x0, y0, x1, y1, bas=16):
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2 + 3
    k1 = (x1 - bas * math.cos(a - 0.5), y1 - bas * math.sin(a - 0.5))
    k2 = (x1 - bas * math.cos(a + 0.5), y1 - bas * math.sin(a + 0.5))
    return "M%.1f %.1f Q%.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        x0, y0, mx, my, x1, y1, k1[0], k1[1], x1, y1, k2[0], k2[1])


def uret():
    s = Sahne()
    FF = "Fredoka"
    # ---------------- öğrenci başı + konuşma balonu (ilk 12 kare boş: çizim 0,40 sn'de başlar) ----------------
    B0 = 0.40
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.59, 128.0, 206.0
    sw = 2.8 / BS
    bas = '<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" ' \
          'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, sw, "".join(
              '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd)))
    s.svg.append(bas)
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(B0 + 0.04 * i, 4), "d": 0.32, "a": 1})
        s.olay(B0 + 0.04 * i, "cizgi", 0.55)
    bal = ("M402 196 C520 182 700 190 880 184 C960 181 1030 186 1052 190 C1076 196 1082 222 1080 262 "
           "C1078 300 1082 332 1078 352 C1074 378 1056 386 1030 386 C900 392 760 384 640 388 "
           "C560 390 500 386 470 388 L330 470 L408 392 C384 388 366 380 364 352 C360 300 366 250 362 224 "
           "C360 204 380 198 402 196 Z")
    s.yol("bal", bal, B0, 0.5, KRE, 4.2, 1, "cizgi", 0.7)
    BF, BX = 44, 412
    sp = Y.genislik("Fredoka", 600, " ", BF)
    pos = {}
    for idx, base in ((range(0, 5), 258), (range(5, 8), 328)):
        x = BX
        for i in idx:
            m, t = Z["balon_kelime"][i]
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(t), 0.12, tur="tik" if i in (3, 7) else None)
            pos[i] = (x, w, base)
            x += w + sp
    for i in (3, 7):   # fosforlu belirteç: been altı
        x, w, base = pos[i]
        s.yol("bm%d" % i, el_cizgi(x - 2, base + 12, x + w + 2, base + 9), S(Z["balon_kelime"][i][1]), 0.28,
              SAR, 8, 0.85, "cizgi", 0.5)
    # ---------------- sağ sütun: have been waiting / has been playing / has been raining ----------------
    RF, RY = 72, [330, 450, 570]
    satir = [("have ", "waiting"), ("has ", "playing"), ("has ", "raining")]
    gen = [Y.genislik(FF, 700, a + "been" + b, RF) for a, b in satir]
    RX = min(1130.0, 1840 - max(gen))
    BIG = 160
    bigw = Y.genislik(FF, 700, "been", BIG)
    ingw = Y.genislik(FF, 700, "-ing", BIG)
    BXB, BYB = 1120.0, 440.0
    for i, (a, b) in enumerate(satir):
        wa = Y.genislik(FF, 700, a, RF)
        wb = Y.genislik(FF, 700, "been", RF)
        t = S(Z["satir_been"][i])
        s.svg.append('<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
                     '<text id="pre%d" x="%.1f" y="%d" fill="%s" xml:space="preserve">%s</text>'
                     '<text id="rb%d" x="%.1f" y="%d" fill="%s">been</text>'
                     '<text id="po%d" x="%.1f" y="%d" fill="%s" xml:space="preserve"> %s</text></g>'
                     % (i, RF, i, RX, RY[i], KRE, a, i, RX + wa, RY[i], SAR, i, RX + wa + wb, RY[i], KRE, b))
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
    # ---------------- 65,97: Form — been'ler tek büyük been'e toplanır ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    for i, (a, b) in enumerate(satir):
        ox, oy = RX + Y.genislik(FF, 700, a, RF), RY[i]
        ta = tf + 0.35 + 0.08 * i
        s.to("#rb%d" % i, ta, {"svgOrigin": "%.1f %d" % (ox, oy), "x": round(BXB - ox, 1), "y": round(BYB - oy, 1),
                               "scale": round(BIG / RF, 3), "duration": 0.55, "ease": "power3.inOut"})
        s.to("#rb%d" % i, ta + 0.5, {"opacity": 0, "duration": 0.08})
        s.to("#pre%d" % i, ta, {"opacity": 0, "duration": 0.3})
        s.to("#po%d" % i, ta, {"opacity": 0, "duration": 0.3})
    tp = tf + 0.9
    s.svg.append('<g id="bigw"><text id="big" x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" font-weight="700" '
                 'font-size="%d" style="opacity:0">been</text></g>' % (BXB, BYB, SAR, BIG))
    s.fromto("#big", tp, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 56)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(tp, "vurus", 0.85)
    # have etiketi + past → now oku (have geçmişi bugüne bağlar)
    PY, PX = 650, BXB + 70
    hw = Y.genislik("Caveat", 700, "have", 52)
    s.yazi("hv", PX + 175 - hw / 2 + 20, PY - 52, [("have", SAR)], "Caveat", 700, 52, S(Z["have_etiket"]) + 0.2, 0.3,
           tur="tik", guc=0.4)
    s.yazi("pst", PX, PY, [("past", IKN)], "Caveat", 700, 56, S(Z["past"]), 0.35, tur="tik", guc=0.45)
    pw = Y.genislik("Caveat", 700, "past", 56)
    s.yol("pnok", el_ok(PX + pw + 22, PY - 18, PX + pw + 262, PY - 20, 16), S(Z["now"]) - 0.1, 0.4, IKN, 4.5, 1,
          "cizgi", 0.5)
    s.yazi("nw", PX + pw + 290, PY, [("now", SAR)], "Caveat", 700, 56, S(Z["now"]) + 0.2, 0.35, tur="tik", guc=0.45)
    # balon ve baş küçülür, yukarı kayar, soluklaşır
    s.to("#balg", tf + 0.5, {"svgOrigin": "362 182", "x": 300, "y": -40, "scale": 0.55, "opacity": 0.45,
                             "duration": 0.8, "ease": "power3.inOut"})
    # ---------------- 68,61: been kutusu + -ing (sarı) + in progress bandı ----------------
    tk = S(Z["been_kutu"])
    s.yol("bkut", el_kutu(BXB - 18, BYB - 128, bigw + 36, 168), tk, 0.5, IKN, 4.5, 1, "cizgi", 0.6)
    ex = BXB + bigw + 26
    s.svg.append('<g id="ingg" style="opacity:0"><text x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" '
                 'font-weight="700" font-size="%d">-ing</text></g>' % (ex, BYB, SAR, BIG))
    s.fromto("#ingg", S(Z["ing"]), {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (ex + ingw / 2, BYB - 56)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(S(Z["ing"]), "vurus", 0.85)
    s.yol("band", el_cizgi(BXB, BYB + 50, ex + ingw, BYB + 46), S(Z["band"]), 0.45, SAR, 9, 0.85, "cizgi", 0.55)
    ipx, ipw = s.yazi("ip", BXB, BYB + 116, [("in progress", IKN)], "Caveat", 700, 52, S(Z["in_progress"]), 0.45,
                      tur="tik", guc=0.5)
    s.yol("ipok", "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        ipx + ipw + 14, BYB + 104, ipx + ipw + 50, BYB + 96, ipx + ipw + 74, BYB + 106, ipx + ipw + 98, BYB + 100,
        ipx + ipw + 84, BYB + 88, ipx + ipw + 98, BYB + 100, ipx + ipw + 82, BYB + 114),
        S(Z["in_progress"]) + 0.55, 0.4, IKN, 4, 1, "cizgi", 0.5)
    s.to("#bigw", tp + 0.5, {"svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 56), "scale": 1.025, "duration": 2.6,
                             "ease": "sine.inOut", "repeat": 5, "yoyo": True})
    # ---------------- sol sütun: -dir … -yor ⇄ have been … -ing ----------------
    AF, AX, AY, BY2 = 96, 110.0, 360, 540
    wd = Y.genislik(FF, 700, "-dir", AF)
    wm = Y.genislik(FF, 700, " … ", AF)
    s.yazi("a1", AX, AY, [("-dir", SAR)], FF, 700, AF, S(Z["dir"]), 0.3, tur="tik", guc=0.55)
    s.yazi("a2", AX + wd, AY, [(" … ", IKN)], FF, 700, AF, S(Z["dir"]) + 0.35, 0.2, tur=None)
    s.yazi("a3", AX + wd + wm, AY, [("-yor", SAR)], FF, 700, AF, S(Z["yor"]), 0.3, tur="tik", guc=0.55)
    s.yazi("b1", AX, BY2, [("have been", SAR), (" … ", IKN), ("-ing", SAR)], FF, 700, AF, S(Z["satir_b"]), 0.7,
           tur="tik", guc=0.55)
    s.yol("cok", el_cift_ok(AX + 200, AY + 34, AX + 200, BY2 - 110, 16), S(Z["cift_ok"]), 0.4, SAR, 6, 0.9, "cizgi",
          0.5)
    # ---------------- cümle: I have been working for two hours. (Fredoka 64) ----------------
    SF, SX, SY = 64, 110.0, 690
    sps = Y.genislik(FF, 700, " ", SF)
    xs, x = {}, SX
    for m, t in Z["cumle"]:
        w = Y.genislik(FF, 700, m, SF)
        renk = SAR if m in ("have", "been") else KRE
        s.yazi("cw_" + m.strip("."), x, SY, [(m, renk)], FF, 700, SF, S(t), 0.12, tur="tik" if m == "I" else None)
        xs[m] = (x, w)
        x += w + sps
    # ---------------- Türkçe köprü: saat-tir  çalış-ıyor-um (Caveat 56) ve kalem bağları ----------------
    TY = 806
    ta_ = [("saat-", KRE), ("tir", SAR)]
    tb_ = [("çalış-", KRE), ("ıyor", SAR), ("-um", KRE)]
    tx1, tw1 = s.yazi("tr1", SX, TY, ta_, "Caveat", 700, 56, S(Z["tr_saat"]), 0.4, tur="tik", guc=0.45)
    tx2, tw2 = s.yazi("tr2", SX + tw1 + 50, TY, tb_, "Caveat", 700, 56, S(Z["tr_calis"]), 0.5, tur="tik", guc=0.45)
    fx0 = xs["for"][0]
    fx1 = xs["hours."][0] + xs["hours."][1]
    s.yol("uf", el_cizgi(fx0, SY + 14, fx1, SY + 11), S(Z["alt_for"]), 0.4, SAR, 8, 0.85, "cizgi", 0.5)
    hx0, hx1 = xs["have"][0], xs["been"][0] + xs["been"][1]
    s.yol("uh", el_cizgi(hx0, SY + 14, hx1, SY + 11), S(Z["alt_havebeen"]), 0.3, SAR, 8, 0.85, "cizgi", 0.5)
    wk0, wkw = xs["working"]
    k_ = Y.genislik(FF, 700, "work", SF)
    s.yol("ui", el_cizgi(wk0 + k_, SY + 14, wk0 + wkw, SY + 11), S(Z["alt_ing"]), 0.25, SAR, 8, 0.85, "cizgi", 0.45)
    # kalem bağları: -tir <-> for two hours ; -ıyor <-> have been … -ing
    tirx = tx1 + Y.genislik("Caveat", 700, "saat-", 56) + Y.genislik("Caveat", 700, "tir", 56) / 2
    iyx = tx2 + Y.genislik("Caveat", 700, "çalış-", 56) + Y.genislik("Caveat", 700, "ıyor", 56) / 2
    s.yol("bg1", "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (tirx, TY - 48, tirx + 60, TY - 70, fx0 + 80, SY + 40,
                                                                 (fx0 + fx1) / 2, SY + 20),
          S(Z["alt_for"]) + 0.3, 0.45, SAR, 4.5, 0.9, "cizgi", 0.45)
    s.yol("bg2", "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (iyx, TY - 48, iyx - 30, TY - 70, (hx0 + hx1) / 2 + 10,
                                                                 SY + 40, (hx0 + hx1) / 2, SY + 20),
          S(Z["alt_havebeen"]) + 0.3, 0.45, SAR, 4.5, 0.9, "cizgi", 0.45)
    # ---------------- formül kartı el kutusunda: have / has been + V-ing ----------------
    KX, KY, KW, KH = 110.0, 850, 880, 124
    s.yol("kart", el_kutu(KX, KY, KW, KH), S(Z["kart"]), 0.55, KRE, 4.5, 1, "cizgi", 0.7)
    KF = 60
    p1 = Y.genislik(FF, 700, "have / has been", KF)
    p2 = Y.genislik(FF, 700, "  +  ", KF)
    p3 = Y.genislik(FF, 700, "V-ing", KF)
    cx0 = KX + (KW - (p1 + p2 + p3)) / 2 - 30
    s.yazi("k1", cx0, KY + 82, [("have / has been", KRE)], FF, 700, KF, S(Z["kart_have"]), 0.45, tur="tik", guc=0.5)
    s.yazi("k2", cx0 + p1, KY + 82, [("  +  ", IKN)], FF, 700, KF, S(Z["kart_arti"]), 0.15, tur=None)
    s.yazi("k3", cx0 + p1 + p2, KY + 82, [("V", KRE), ("-ing", SAR)], FF, 700, KF, S(Z["kart_ing"]), 0.3, tur="tik",
           guc=0.6)
    s.olay(S(Z["kart_ing"]) + 0.3, "vurus", 0.8)
    s.yol("ktik", "M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (KX + KW - 74, KY + 66, KX + KW - 60, KY + 82, KX + KW - 30,
                                                       KY + 42), S(Z["kart_ing"]) + 0.55, 0.25, SAR, 8, 0.95, "cizgi",
          0.5)
    # Next lesson →
    tn2 = S(Z["sonraki"])
    nw = Y.genislik("Lexend", 500, "Next lesson", 24)
    s.yazi("nx", 1864 - nw - 44, 984, [("Next lesson", IKN)], "Lexend", 500, 24, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M%.1f 976 L%.1f 976 M%.1f 969 L%.1f 976 L%.1f 983" % (1864 - 38, 1864 - 4, 1864 - 12, 1864 - 4,
                                                                          1864 - 12), tn2 + 0.3, 0.25, IKN, 3, 1,
          "cizgi", 0.4)
    # ---------------- derleme ----------------
    kun = Y.kunye_svg("Question", 2).replace(
        '<circle id="ku-nokta"', '<text id="ku-bolum2" x="1864" y="72" text-anchor="end" font-family="Lexend" '
        'font-weight="700" font-size="24" fill="%s" style="opacity:0">Form</text><circle id="ku-nokta"' % SAR)
    govde = "".join(s.svg)
    bal_ids = ["bal", "bas", "bm3", "bm7"] + ["bw%d" % i for i in range(8)]
    return s, {"kun": kun, "bal_ids": bal_ids, "govde": govde}


def html(s, parca):
    ayr = {}
    # grupla: balon elemanlarını #balg altında topla (svg sırası korunur: balg figürden sonra)
    govde_parcalar = s.svg
    bal_ids = set(parca["bal_ids"])
    bal_html, diger = [], []
    for e in govde_parcalar:
        idn = e.split('id="', 1)[1].split('"', 1)[0]
        (bal_html if idn in bal_ids else diger).append(e)
    sec = "".join(bal_html)
    veri = {"cmd": sorted(s.cmd, key=lambda c: c["t"])}
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1920" data-height="1080">
{Y.zemin_html()}
<svg id="sahne" width="1920" height="1080" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
<defs>{''.join(s.defs)}</defs>
<g id="balg">{sec}</g>
{''.join(diger)}
{parca['kun']}
<image id="logo" href="assets/logo.svg" x="56" y="1002" width="{34 * Y.LOGO_EN_BOY:.2f}" height="34"/>
</svg></div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var C = {json.dumps(veri, ensure_ascii=False)};
  var tl = gsap.timeline({{ paused: true }});
  var $ = function (q) {{ return document.querySelector(q); }};
  C.cmd.forEach(function (c) {{
    var t = c.t, v;
    if (c.m === "draw") {{
      var p = $("#" + c.id), L = p.getTotalLength();
      p.style.strokeDasharray = L + " " + (L + 2); p.style.strokeDashoffset = L;
      tl.set(p, {{ opacity: c.a, immediateRender: false }}, t);
      tl.to(p, {{ strokeDashoffset: 0, duration: c.d, ease: "power1.inOut", immediateRender: false }}, t);
    }} else if (c.m === "rev") {{
      tl.to("#" + c.id, {{ attr: {{ width: c.w }}, duration: c.d, ease: "power1.out", immediateRender: false }}, t);
    }} else if (c.m === "to") {{
      v = Object.assign({{ immediateRender: false }}, c.v); tl.to(c.s, v, t);
    }} else if (c.m === "fromTo") {{
      v = Object.assign({{ immediateRender: false }}, c.v); tl.fromTo(c.s, c.a, v, t);
    }}
  }});
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(html(s, parca))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

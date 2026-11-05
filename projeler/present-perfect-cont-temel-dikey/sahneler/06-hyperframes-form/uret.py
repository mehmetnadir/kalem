"""Sahne 06 (PPC temel: öğrenci sorusu + form) DİKEY 1080x1920, HyperFrames (PPC temel), 681 kare, t_bas 61,51.
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
        self.grp = {"bal": [], "rows": [], "recap": []}

    def _hedef(self, g):
        return self.grp[g] if g else self.svg

    def olay(self, t, tur, guc):
        self.ev.append({"kare": round(t * 30), "tur": tur, "guc": guc})

    def to(self, sel, t, v):
        self.cmd.append({"m": "to", "s": sel, "t": round(t, 4), "v": v})

    def fromto(self, sel, t, a, v):
        self.cmd.append({"m": "fromTo", "s": sel, "t": round(t, 4), "a": a, "v": v})

    def goster(self, sel, t, d=0.35, dx=0, dy=0, sc=None):
        a = {"opacity": 0, "x": dx, "y": dy}
        v = {"opacity": 1, "x": 0, "y": 0, "duration": d, "ease": "power3.out"}
        if sc is not None:
            a["scale"], v["scale"] = sc, 1
        self.fromto(sel, t, a, v)

    def yol(self, id, d, t, sure, stroke=KRE, w=4.0, alfa=1.0, tur="cizgi", guc=0.55, g=None):
        self._hedef(g).append('<path id="%s" d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
                              'stroke-linejoin="round" style="opacity:0"/>' % (id, d, stroke, w))
        self.cmd.append({"m": "draw", "id": id, "t": round(t, 4), "d": round(sure, 4), "a": alfa})
        if tur:
            self.olay(t, tur, guc)

    def yazi(self, id, x, y, parcalar, aile, agr, boy, t, d=0.12, anchor="start", tur="tik", guc=0.5, g=None):
        """Soldan maske ile yazılan metin; parcalar [(metin, renk)]. -> (x0, genişlik)."""
        ws = [Y.genislik(aile, agr, p[0], boy) for p in parcalar]
        W = sum(ws)
        x0 = x - W if anchor == "end" else (x - W / 2 if anchor == "middle" else x)
        cx, tx = x0, ""
        for (m, fill), w in zip(parcalar, ws):
            tx += '<text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">%s</text>' % (cx, y, fill, m)
            cx += w
        self.defs.append('<clipPath id="c_%s"><rect id="r_%s" x="%.1f" y="%.1f" width="0" height="%.1f"/></clipPath>'
                         % (id, id, x0 - 8, y - boy * 1.05, boy * 1.5))
        self._hedef(g).append('<g id="%s" font-family="%s" font-weight="%d" font-size="%s" clip-path="url(#c_%s)">%s</g>'
                              % (id, aile, agr, boy, id, tx))
        self.cmd.append({"m": "rev", "id": "r_" + id, "t": round(t, 4), "d": d, "w": round(W + 20, 1)})
        if tur:
            self.olay(t, tur, guc)
        return x0, W

    def pop(self, id, x, y, parcalar, aile, agr, boy, t, d=0.35, tur="vurus", guc=0.85, anchor="start", g=None):
        """Ölçek 0,92 -> 1 + alfa (formül / anahtar sözcük). -> (x0, genişlik)."""
        ws = [Y.genislik(aile, agr, p[0], boy) for p in parcalar]
        W = sum(ws)
        x0 = x - W / 2 if anchor == "middle" else x
        cx, tx = x0, ""
        for (m, fill), w in zip(parcalar, ws):
            tx += '<text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">%s</text>' % (cx, y, fill, m)
            cx += w
        self._hedef(g).append('<g id="%s" font-family="%s" font-weight="%d" font-size="%s" style="opacity:0">%s</g>'
                              % (id, aile, agr, boy, tx))
        self.fromto("#" + id, t, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (x0 + W / 2, y - boy * 0.35)},
                    {"opacity": 1, "scale": 1, "duration": d, "ease": "power3.out"})
        if tur:
            self.olay(t, tur, guc)
        return x0, W


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


def el_ok(x0, y0, x1, y1, bas=16):
    """El oku: hafif eğri gövde + iki uçlu ok başı (tek yol; dikey oka da uyar)."""
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2 + 3
    k1 = (x1 - bas * math.cos(a - 0.5), y1 - bas * math.sin(a - 0.5))
    k2 = (x1 - bas * math.cos(a + 0.5), y1 - bas * math.sin(a + 0.5))
    return "M%.1f %.1f Q%.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        x0, y0, mx, my, x1, y1, k1[0], k1[1], x1, y1, k2[0], k2[1])


def tik_yolu(x, y, b=1.0):
    """Küçük onay işareti (sol alt başlangıç)."""
    return "M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (x, y, x + 12 * b, y + 14 * b, x + 38 * b, y - 20 * b)


def parca_x(parcalar, aile, agr, boy, x0):
    """Her parçanın sol x'i ve genişliği."""
    out, x = [], x0
    for m, _ in parcalar:
        w = Y.genislik(aile, agr, m, boy)
        out.append((x, w))
        x += w
    return out


def altyazi_parcalar():
    """altyazi.json: cümle 6 ve 7 parçaları -> [(t0, t1, [satır, ...])]; Lexend 500 44, en çok 2 satır, 984 px."""
    liste = json.loads((Y.ORTAK / "anlatim" / "altyazi.json").read_text())
    out = []
    for p in liste:
        if p["cumle"] not in (6, 7):
            continue
        satir, cur = [], ""
        for w in p["metin"].split(" "):
            dene = (cur + " " + w).strip()
            if cur and Y.genislik("Lexend", 500, dene, 44) > 984:
                satir.append(cur)
                cur = w
            else:
                cur = dene
        satir.append(cur)
        while len(satir) > 2:
            son = satir.pop()
            satir[-1] += " " + son
        out.append((p["t0"], p["t1"], satir))
    return out


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


def uret():
    s = Sahne()
    FF = "Fredoka"
    B0 = 0.40   # ilk 12 kare boş: baş ve balon 0,40 sn'de başlar
    # ---------------- öğrenci başı 160 px (peeps-kit) + konuşma balonu: grup "bal" ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS = 0.5
    BTX, BTY = 128.0 - 118 * BS, 470.0 - 126 * BS    # yüz merkezi (118,126) -> (128, 470)
    sw = 4.2 / BS
    s.grp["bal"].append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" '
                        'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (
                            BTX, BTY, BS, KRE, sw, "".join(
                                '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(B0 + 0.04 * i, 4), "d": 0.32, "a": 1})
        s.olay(B0 + 0.04 * i, "cizgi", 0.55)
    bal = ("M262 384 C400 372 700 386 1000 380 C1026 380 1036 396 1036 420 C1038 480 1034 540 1036 580 "
           "C1036 604 1020 618 996 618 C800 626 520 616 296 620 C268 620 256 612 240 598 C234 590 234 578 234 572 "
           "L204 546 L234 520 C232 470 230 420 240 400 C246 390 252 386 262 384 Z")
    s.yol("bal", bal, B0, 0.5, KRE, 5.0, 1, "cizgi", 0.7, g="bal")
    BF, BX = 68, 276
    sp = Y.genislik("Caveat", 700, " ", BF)
    pos = {}
    for idx, base in ((range(0, 5), 472), (range(5, 8), 568)):
        x = BX
        for i in idx:
            m, t = Z["balon_kelime"][i]
            w = Y.genislik("Caveat", 700, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Caveat", 700, BF, S(t), 0.14,
                   tur="tik" if i in (3, 7) else None, g="bal")
            pos[i] = (x, w, base)
            x += w + sp
    for i in (3, 7):   # fosforlu belirteç: been altı (w 10)
        x, w, base = pos[i]
        s.yol("bm%d" % i, el_cizgi(x - 2, base + 14, x + w + 2, base + 10), S(Z["balon_kelime"][i][1]), 0.28, SAR, 10,
              0.85, "cizgi", 0.5, g="bal")
    # ---------------- ORTA: have been waiting / has been playing / has been raining (Fredoka 100) ----------------
    RF, RY = 100, [800, 960, 1120]
    satir = [("have ", "waiting"), ("has ", "playing"), ("has ", "raining")]
    gen = [Y.genislik(FF, 700, a + "been" + b, RF) for a, b in satir]
    RX = (1080 - max(gen)) / 2
    BIG, BXB, BYB = 150, 230.0, 720.0
    bigw = Y.genislik(FF, 700, "been", BIG)
    ingw = Y.genislik(FF, 700, "-ing", BIG)
    for i, (a, b) in enumerate(satir):
        wa = Y.genislik(FF, 700, a, RF)
        wb = Y.genislik(FF, 700, "been", RF)
        s.grp["rows"].append(
            '<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
            '<text id="pre%d" x="%.1f" y="%d" fill="%s" xml:space="preserve">%s</text>'
            '<text id="rb%d" x="%.1f" y="%d" fill="%s">been</text>'
            '<text id="po%d" x="%.1f" y="%d" fill="%s" xml:space="preserve"> %s</text></g>'
            % (i, RF, i, RX, RY[i], KRE, a, i, RX + wa, RY[i], SAR, i, RX + wa + wb, RY[i], KRE, b))
        t = S(Z["satir_been"][i])
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
    # ---------------- 65,97: Form — balon+baş küçülür, been'ler tek büyük been'e toplanır ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    s.to("#balg", tf + 0.1, {"svgOrigin": "48 352", "scale": 0.72, "opacity": 0.5, "duration": 0.8,
                             "ease": "power3.inOut"})
    for i, (a, b) in enumerate(satir):
        ox, oy = RX + Y.genislik(FF, 700, a, RF), RY[i]
        ta = tf + 0.35 + 0.08 * i
        s.to("#rb%d" % i, ta, {"svgOrigin": "%.1f %d" % (ox, oy), "x": round(BXB - ox, 1), "y": round(BYB - oy, 1),
                               "scale": round(BIG / RF, 3), "duration": 0.55, "ease": "power3.inOut"})
        s.to("#rb%d" % i, ta + 0.5, {"opacity": 0, "duration": 0.08})
        s.to("#pre%d" % i, ta, {"opacity": 0, "duration": 0.3})
        s.to("#po%d" % i, ta, {"opacity": 0, "duration": 0.3})
    tp = tf + 0.9
    s.grp["recap"].append('<g id="bigw"><text id="big" x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" '
                          'font-weight="700" font-size="%d" style="opacity:0">been</text></g>' % (BXB, BYB, SAR, BIG))
    s.fromto("#big", tp, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 52)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(tp, "vurus", 0.85)
    # past → now oku (have geçmişi bugüne bağlar): sağ, taban 860
    PY = 860
    pw = Y.genislik("Caveat", 700, "past", 64)
    nw = Y.genislik("Caveat", 700, "now", 64)
    PX = 1032 - (pw + 24 + 200 + 24 + nw)
    s.yazi("pst", PX, PY, [("past", IKN)], "Caveat", 700, 64, S(Z["past"]), 0.35, tur="tik", guc=0.45, g="recap")
    s.yol("pnok", el_ok(PX + pw + 24, PY - 20, PX + pw + 224, PY - 22, 18), S(Z["now"]) - 0.1, 0.4, IKN, 5, 1,
          "cizgi", 0.5, g="recap")
    s.yazi("nw", PX + pw + 248, PY, [("now", SAR)], "Caveat", 700, 64, S(Z["now"]) + 0.2, 0.35, tur="tik", guc=0.45,
           g="recap")
    # ---------------- 68,61: been kutusu + -ing (sarı) + in progress bandı ----------------
    ex = BXB + bigw + 26
    s.yol("bkut", el_kutu(BXB - 20, BYB - 124, bigw + 40, 160), S(Z["been_kutu"]), 0.5, IKN, 5, 1, "cizgi", 0.6,
          g="recap")
    s.pop("ingg", ex, BYB, [("-ing", SAR)], FF, 700, BIG, S(Z["ing"]), 0.35, "vurus", 0.85, g="recap")
    s.yol("band", el_cizgi(BXB, BYB + 50, ex + ingw, BYB + 46), S(Z["band"]), 0.45, SAR, 10, 0.85, "cizgi", 0.55,
          g="recap")
    ipx, ipw = s.yazi("ip", 48, PY, [("in progress", IKN)], "Caveat", 700, 64, S(Z["in_progress"]), 0.45, tur="tik",
                      guc=0.5, g="recap")
    s.yol("ipok", el_ok(ipx + ipw + 20, PY - 20, ipx + ipw + 110, PY - 22, 16), S(Z["in_progress"]) + 0.55, 0.35, IKN,
          5, 1, "cizgi", 0.45, g="recap")
    s.to("#bigw", tp + 0.5, {"svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 52), "scale": 1.025, "duration": 2.6,
                             "ease": "sine.inOut", "repeat": 5, "yoyo": True})
    # ---------------- -dir … -yor ⇄ have been … -ing (Fredoka 96): grup "recap" ----------------
    AF, AX, AY, BY2 = 96, 80.0, 1030, 1190
    wd = Y.genislik(FF, 700, "-dir", AF)
    wm = Y.genislik(FF, 700, " … ", AF)
    s.yazi("a1", AX, AY, [("-dir", SAR)], FF, 700, AF, S(Z["dir"]), 0.3, tur="tik", guc=0.55, g="recap")
    s.yazi("a2", AX + wd, AY, [(" … ", IKN)], FF, 700, AF, S(Z["dir"]) + 0.35, 0.2, tur=None, g="recap")
    s.yazi("a3", AX + wd + wm, AY, [("-yor", SAR)], FF, 700, AF, S(Z["yor"]), 0.3, tur="tik", guc=0.55, g="recap")
    s.yazi("b1", AX, BY2, [("have been", SAR), (" … ", IKN), ("-ing", SAR)], FF, 700, AF, S(Z["satir_b"]), 0.7,
           tur="tik", guc=0.55, g="recap")
    s.yol("cok", el_cift_ok(AX + 230, AY + 34, AX + 230, BY2 - 110, 18), S(Z["cift_ok"]), 0.4, SAR, 8, 0.9, "cizgi",
          0.5, g="recap")
    # ---------------- 74,20: üst blok toplanır (ölçek 0,6), alta cümle + Türkçe köprü + kart ----------------
    s.to("#recapg", S(Z["toplan"]), {"svgOrigin": "48 600", "scale": 0.6, "y": -40, "duration": 0.6,
                                     "ease": "power3.inOut"})
    s.olay(S(Z["toplan"]), "parilti", 0.5)
    SF, SX = 72, 60.0
    sps = Y.genislik(FF, 700, " ", SF)
    satir1 = ["I", "have", "been", "working"]
    satir2 = ["for", "two", "hours."]
    SY1, SY2 = 1000, 1080
    xs = {}
    for lst, yy in ((satir1, SY1), (satir2, SY2)):
        x = SX
        for m in lst:
            t = [tt for mm, tt in Z["cumle"] if mm == m][0]
            w = Y.genislik(FF, 700, m, SF)
            s.yazi("cw_" + m.strip("."), x, yy, [(m, SAR if m in ("have", "been") else KRE)], FF, 700, SF, S(t), 0.12,
                   tur="tik" if m == "I" else None)
            xs[m] = (x, w, yy)
            x += w + sps
    # Türkçe köprü: Caveat 72 mürekkep, -tir / -ıyor sarı; alt çizgiler ve bağ
    TY = 1200
    ta_ = [("saat-", KRE), ("tir", SAR)]
    tb_ = [("çalış-", KRE), ("ıyor", SAR), ("-um", KRE)]
    tx1, tw1 = s.yazi("tr1", SX, TY, ta_, "Caveat", 700, 72, S(Z["tr_saat"]), 0.4, tur="tik", guc=0.45)
    tx2, tw2 = s.yazi("tr2", SX + tw1 + 60, TY, tb_, "Caveat", 700, 72, S(Z["tr_calis"]), 0.5, tur="tik", guc=0.45)
    fx0, fw0, _ = xs["for"]
    fx1 = xs["hours."][0] + xs["hours."][1]
    s.yol("uf", el_cizgi(fx0, SY2 + 16, fx1, SY2 + 12), S(Z["alt_for"]), 0.4, SAR, 10, 0.85, "cizgi", 0.5)
    hx0, hx1 = xs["have"][0], xs["been"][0] + xs["been"][1]
    s.yol("uh", el_cizgi(hx0, SY1 + 16, hx1, SY1 + 12), S(Z["alt_havebeen"]), 0.3, SAR, 10, 0.85, "cizgi", 0.5)
    wk0, wkw, _ = xs["working"]
    k_ = Y.genislik(FF, 700, "work", SF)
    s.yol("ui", el_cizgi(wk0 + k_, SY1 + 16, wk0 + wkw, SY1 + 12), S(Z["alt_ing"]), 0.25, SAR, 10, 0.85, "cizgi", 0.45)
    tirx = tx1 + Y.genislik("Caveat", 700, "saat-", 72) + Y.genislik("Caveat", 700, "tir", 72) / 2
    s.yol("bg1", "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (tirx, TY - 62, tirx + 40, TY - 90, fx0 + 120,
                                                                 SY2 + 60, fx0 + 100, SY2 + 22),
          S(Z["alt_for"]) + 0.3, 0.45, SAR, 5, 0.9, "cizgi", 0.45)
    # ---------------- kod kartı: have / has been + V-ing ----------------
    KX, KY, KW, KH = 48.0, 1252, 984.0, 124
    s.yol("kart", el_kutu(KX, KY, KW, KH), S(Z["kart"]), 0.55, KRE, 5.0, 1, "cizgi", 0.7)
    KF = 72
    p1 = Y.genislik(FF, 700, "have / has been", KF)
    p2 = Y.genislik(FF, 700, "  +  ", KF)
    p3 = Y.genislik(FF, 700, "V-ing", KF)
    cx0 = KX + (KW - (p1 + p2 + p3)) / 2 - 36
    s.yazi("k1", cx0, KY + 88, [("have / has been", KRE)], FF, 700, KF, S(Z["kart_have"]), 0.45, tur="tik", guc=0.5)
    s.yazi("k2", cx0 + p1, KY + 88, [("  +  ", IKN)], FF, 700, KF, S(Z["kart_arti"]), 0.15, tur=None)
    s.yazi("k3", cx0 + p1 + p2, KY + 88, [("V", KRE), ("-ing", SAR)], FF, 700, KF, S(Z["kart_ing"]), 0.3, tur="tik",
           guc=0.6)
    s.olay(S(Z["kart_ing"]) + 0.3, "vurus", 0.8)
    s.yol("ktik", tik_yolu(KX + KW - 96, KY + 70, 1.1), S(Z["kart_ing"]) + 0.55, 0.25, SAR, 9, 0.95, "cizgi", 0.5)
    # ---------------- altyazı bandı (1400–1536): konuşulan parça ----------------
    par = altyazi_parcalar()
    for i, (t0, t1, satirlar) in enumerate(par):
        y0 = 1400 + (84 if len(satirlar) == 1 else 56)
        tx = "".join('<text x="540" y="%d" text-anchor="middle" fill="%s">%s</text>' % (y0 + 56 * k, KRE, m)
                     for k, m in enumerate(satirlar))
        s.svg.append('<g id="alt%d" style="opacity:0" font-family="Lexend" font-weight="500" font-size="44">%s</g>'
                     % (i, tx))
        bas = max(0.0, S(t0) - 0.05)
        bit = S(par[i + 1][0]) - 0.05 if i + 1 < len(par) else S(t1) + 0.35
        s.cmd.append({"m": "set", "s": "#alt%d" % i, "t": round(bas, 4), "v": {"opacity": 1}})
        s.cmd.append({"m": "set", "s": "#alt%d" % i, "t": round(max(bas + 0.1, min(bit, S(t1) + 0.35)), 4),
                      "v": {"opacity": 0}})
    # ---------------- künye (dikey HUD v2): Question -> Form çipi ----------------
    kun = Y.kunye_svg("Question") + Y.kunye_cip("Form", "ku-bolum2")
    return s, {"kun": kun}


def html(s, parca):
    veri = {"cmd": sorted(s.cmd, key=lambda c: c["t"])}
    bal = "".join(s.grp["bal"])
    rows = "".join(s.grp["rows"])
    recap = "".join(s.grp["recap"])
    lw = 96 * Y.LOGO_EN_BOY
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>{''.join(s.defs)}</defs>
<g id="balg">{bal}</g>
<g id="rowsg">{rows}</g>
<g id="recapg">{recap}</g>
{''.join(s.svg)}
{parca['kun']}
<image id="logo" href="assets/logo.svg" x="48" y="48" width="{lw:.2f}" height="96"/>
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
    }} else if (c.m === "set") {{
      v = Object.assign({{ immediateRender: false }}, c.v); tl.set(c.s, v, t);
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

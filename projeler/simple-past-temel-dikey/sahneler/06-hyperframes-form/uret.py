"""Sahne 06 (öğrenci sorusu + form) DİKEY 1080x1920, HyperFrames, 901 kare, t_bas 64,78.
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


def uret():
    s = Sahne()
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
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(0.04 * i, 4), "d": 0.32, "a": 1})
        s.olay(0.04 * i, "cizgi", 0.55)
    bal = ("M262 384 C400 372 700 386 1000 380 C1026 380 1036 396 1036 420 C1038 480 1034 540 1036 580 "
           "C1036 604 1020 618 996 618 C800 626 520 616 296 620 C268 620 256 612 240 598 C234 590 234 578 234 572 "
           "L204 546 L234 520 C232 470 230 420 240 400 C246 390 252 386 262 384 Z")
    s.yol("bal", bal, 0.0, 0.5, KRE, 5.0, 1, "cizgi", 0.7, g="bal")
    BF, BX = 68, 276
    sp = Y.genislik("Caveat", 700, " ", BF)
    pos = {}
    for idx, base in ((range(0, 4), 472), (range(4, 7), 568)):
        x = BX
        for i in idx:
            m, t = Z["balon_kelime"][i]
            w = Y.genislik("Caveat", 700, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Caveat", 700, BF, S(t), 0.14,
                   tur="tik" if i in (2, 6) else None, g="bal")
            pos[i] = (x, w, base)
            x += w + sp
    x, w, base = pos[2]   # fosforlu belirteç: -ed altı (w 10)
    s.yol("bm2", el_cizgi(x - 2, base + 14, x + w + 2, base + 10), S(Z["balon_kelime"][2][1]), 0.28, SAR, 10, 0.85,
          "cizgi", 0.5, g="bal")
    # ---------------- ORTA: watch-ed / went / didn't play (Fredoka 110, tek tek toplanır) ----------------
    RF, RX, RY = 110, 90.0, [800, 960, 1120]
    satir = [[("watch", KRE), ("-ed", SAR)], [("went", KRE)], [("didn't play", KRE)]]
    genrow = []
    for i in range(3):
        tx, cx = "", RX
        for m, fill in satir[i]:
            tx += '<text x="%.1f" y="%d" fill="%s">%s</text>' % (cx, RY[i], fill, m)
            cx += Y.genislik("Fredoka", 700, m, RF)
        genrow.append(cx - RX)
        s.grp["rows"].append('<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" '
                             'font-size="%d">%s</g>' % (i, RF, tx))
        t = S(Z["satir"][i])
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
    # ---------------- 69,33: Form — balon+baş küçülür, satırlar şeride toplanır ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    s.to("#balg", tf + 0.1, {"svgOrigin": "48 352", "scale": 0.83, "y": -16, "opacity": 0.5,
                             "duration": 0.8,
                             "ease": "power3.inOut"})
    cx = 48.0
    for i in range(3):   # satır -> şerit çipi: ölçek 0,52 (110 -> 57,2 px), taban y 618
        wi = genrow[i] * 0.52
        s.to("#row%d" % i, tf + 0.1 + 0.06 * i, {"svgOrigin": "%.1f %d" % (RX, RY[i]), "x": round(cx - RX, 1),
                                                "y": 618 - RY[i], "scale": 0.52, "opacity": 0.6, "duration": 0.8,
                                                "ease": "power3.inOut"})
        cx += wi + 44
    s.olay(tf + 0.1, "parilti", 0.5)
    # ---------------- S1: iki kutucuk (düzenli | düzensiz), grup "recap" ----------------
    TY, TH, TW = 652, 360, 480
    s.yol("tile1", el_kutu(48, TY, TW, TH), S(Z["iki_yol"]), 0.4, IKN, 4.0, 1, "cizgi", 0.6, g="recap")
    s.yol("tile2", el_kutu(552, TY, TW, TH), S(Z["iki_yol"]) + 0.18, 0.4, IKN, 4.0, 1, "cizgi", 0.5, g="recap")
    # düzenli
    s.yazi("dz", 84, TY + 92, [("düzenli", KRE)], "Fredoka", 700, 72, S(Z["duzenli"]), 0.4, tur="tik", guc=0.55,
           g="recap")
    ex, ew = s.pop("ed", 84, TY + 232, [("+ ", KRE), ("-ed", SAR)], "Fredoka", 700, 120, S(Z["ed"]), 0.35, g="recap")
    s.yol("edal", el_cizgi(ex + Y.genislik("Fredoka", 700, "+ ", 120) - 4, TY + 256, ex + ew + 6, TY + 252),
          S(Z["ed"]) + 0.3, 0.3, SAR, 10, 0.85, "cizgi", 0.45, g="recap")
    ya = TY + 330
    w1 = Y.genislik("Caveat", 700, "watch", 64)
    s.yazi("o1a", 80, ya, [("watch", IKN)], "Caveat", 700, 64, S(Z["ornek1"]), 0.25, tur="tik", guc=0.5, g="recap")
    s.yol("o1k", el_ok(80 + w1 + 14, ya - 20, 80 + w1 + 78, ya - 22, 14), S(Z["ornek1"]) + 0.25, 0.25, SAR, 8, 0.9,
          "cizgi", 0.4, g="recap")
    s.yazi("o1b", 80 + w1 + 92, ya, [("watch", KRE), ("ed", SAR)], "Caveat", 700, 64, S(Z["ornek1"]) + 0.45, 0.35,
           tur="tik", guc=0.5, g="recap")
    # düzensiz
    s.yazi("dsz", 588, TY + 92, [("düzensiz", KRE)], "Fredoka", 700, 72, S(Z["duzensiz"]), 0.4, tur="tik", guc=0.55,
           g="recap")
    vx, vw = s.pop("v2", 588, TY + 232, [("V2", SAR)], "Fredoka", 700, 120, S(Z["v2"]), 0.35, g="recap")
    s.yol("v2al", el_cizgi(vx - 4, TY + 256, vx + vw + 6, TY + 252), S(Z["v2"]) + 0.8, 0.3, SAR, 10, 0.85, "cizgi", 0.45,
          g="recap")
    w2 = Y.genislik("Caveat", 700, "go", 64)
    s.yazi("o2a", 584, ya, [("go", IKN)], "Caveat", 700, 64, S(Z["ornek2"]), 0.2, tur="tik", guc=0.5, g="recap")
    s.yol("o2k", el_ok(584 + w2 + 14, ya - 20, 584 + w2 + 78, ya - 22, 14), S(Z["ornek2"]) + 0.2, 0.25, SAR, 8, 0.9,
          "cizgi", 0.4, g="recap")
    s.yazi("o2b", 584 + w2 + 92, ya, [("went", SAR)], "Caveat", 700, 64, S(Z["ornek2"]) + 0.4, 0.35, tur="tik",
           guc=0.5, g="recap")
    # ---------------- S2: didn't + V1 / Did + özne + V1? ----------------
    KX, KY, KW, KH = 48.0, 1034, 984.0, 206
    s.yol("kutu", el_kutu(KX, KY, KW, KH), S(Z["kutu"]), 0.55, KRE, 5.0, 1, "cizgi", 0.7, g="recap")
    FS = 76
    l1 = [("didn't", KRE), (" + ", IKN), ("V1", SAR)]
    l2 = [("Did", KRE), (" + ", IKN), ("özne", KRE), (" + ", IKN), ("V1", SAR), ("?", KRE)]
    s.pop("l1", KX + 48, KY + 84, l1, "Fredoka", 700, FS, S(Z["didnt"]), 0.35, "vurus", 0.8, g="recap")
    s.pop("l2", KX + 48, KY + 178, l2, "Fredoka", 700, FS, S(Z["soru"]), 0.35, "tik", 0.6, g="recap")
    for k, (lin, yy) in enumerate(((l1, KY + 84), (l2, KY + 178))):
        px = parca_x(lin, "Fredoka", 700, FS, KX + 48)
        i = [j for j, p in enumerate(lin) if p[0] == "V1"][0]
        s.yol("v1al%d" % k, el_cizgi(px[i][0] - 3, yy + 20, px[i][0] + px[i][1] + 5, yy + 16),
              S(Z["v1"]) + 0.12 * k, 0.28, SAR, 9, 0.85, "cizgi", 0.5, g="recap")
    # ---------------- Türkçe köprüsü: izle-di = watch-ed ----------------
    s.yazi("tr", 56, 1296, [("Türkçedeki -di gibi:", IKN)], "Caveat", 700, 56, S(Z["turkce"]), 0.9, tur="tik", guc=0.4,
           g="recap")
    YY, CF = 1382, 88
    a = [("izle", KRE), ("-di", SAR)]
    b = [("watch", KRE), ("-ed", SAR)]
    wa = sum(Y.genislik("Fredoka", 700, p[0], CF) for p in a)
    s.yazi("iz", 56, YY, a, "Fredoka", 700, CF, S(Z["izledi"]), 0.6, tur="tik", guc=0.5, g="recap")
    eq = 56 + wa + 40
    s.yol("es1", el_cizgi(eq, YY - 50, eq + 64, YY - 53, 1), S(Z["esit"]), 0.2, KRE, 8, 1, "cizgi", 0.5, g="recap")
    s.yol("es2", el_cizgi(eq + 2, YY - 24, eq + 66, YY - 27, -1), S(Z["esit"]) + 0.2, 0.2, KRE, 8, 1, "cizgi", 0.5,
          g="recap")
    s.yazi("wa", eq + 104, YY, b, "Fredoka", 700, CF, S(Z["watched"]), 0.6, tur="tik", guc=0.5, g="recap")
    # ---------------- 84,20: S1+S2+köprü toplanır (sol blok), sağda zaman ifadeleri ----------------
    s.to("#recapg", S(Z["yesterday"]) - 0.15, {"svgOrigin": "48 640", "scale": 0.62, "duration": 0.7,
                                              "ease": "power3.inOut"})
    s.olay(S(Z["yesterday"]) - 0.15, "parilti", 0.5)
    TF2, BX0 = 46, 700.0
    for i, (m, t) in enumerate((("yesterday", Z["yesterday"]), ("ago", Z["ago"]), ("last year", Z["lastyear"]))):
        y = 652 + 110 * i
        w = Y.genislik("Fredoka", 700, m, TF2) + 96
        s.yol("tk%d" % i, el_kutu(BX0, y, w, 80), S(t), 0.3, KRE, 4.5, 1, "cizgi", 0.55)
        s.yazi("tt%d" % i, BX0 + 24, y + 56, [(m, KRE)], "Fredoka", 700, TF2, S(t) + 0.22, 0.25, tur="tik", guc=0.5)
        s.yol("ti%d" % i, tik_yolu(BX0 + w - 62, y + 44, 0.9), S(t) + 0.5, 0.22, SAR, 8, 0.95, "cizgi", 0.4)
    ax = 868.0
    s.yol("ok", el_ok(ax, 972, ax + 4, 1092, 20), S(Z["ok"]), 0.4, SAR, 10, 0.9, "cizgi", 0.55)
    # ---------------- alt: Simple Past, formül kartı, kural cümlesi ----------------
    s.pop("sp", 540, 1214, [("Simple Past", KRE)], "Fredoka", 700, 124, S(Z["simplepast"]), 0.4, "vurus", 0.9,
          anchor="middle")
    s.yazi("bi", 540, 1384, [("Biten iş, belli zaman", IKN)], "Caveat", 700, 64, S(Z["biten"]), 0.7, tur="tik",
           guc=0.5, anchor="middle")
    CX, CY, CW, CH = 48.0, 1240, 984.0, 92
    s.yol("kart", el_kutu(CX, CY, CW, CH), S(Z["kart"]), 0.5, KRE, 5.0, 1, "cizgi", 0.7)
    fp = [("V-ed / V2", KRE), ("  ·  ", IKN), ("did + V1", SAR)]
    fw = sum(Y.genislik("Fredoka", 700, p[0], 72) for p in fp)
    s.pop("kf", CX + (CW - fw) / 2 - 30, CY + 68, fp, "Fredoka", 700, 72, S(Z["kart"]) + 0.3, 0.35, "tik", 0.6)
    s.yol("kt", tik_yolu(CX + CW - 90, CY + 56, 1.2), S(Z["kart"]) + 0.9, 0.25, SAR, 8, 0.95, "cizgi", 0.5)
    s.olay(S(Z["kart"]) + 0.75, "vurus", 0.8)
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

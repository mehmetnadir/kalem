"""Sahne 06 (öğrenci sorusu + form) YATAY 1920x1080, HyperFrames, 901 kare, t_bas 64,78.
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
        self.grp = {"bal": [], "rows": []}

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


def uret():
    s = Sahne()
    # ---------------- öğrenci başı (peeps-kit) + konuşma balonu: grup "bal" ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.59, 128.0, 206.0   # saç dahil boy ≈ 190 px; yüz merkezi (118,126) -> (198, 280)
    sw = 2.8 / BS
    s.grp["bal"].append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" '
                        'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (
                            BTX, BTY, BS, KRE, sw, "".join(
                                '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(0.04 * i, 4), "d": 0.32, "a": 1})
        s.olay(0.04 * i, "cizgi", 0.55)
    bal = ("M402 196 C520 182 700 190 880 184 C960 181 1030 186 1052 190 C1076 196 1082 222 1080 262 "
           "C1078 300 1082 332 1078 352 C1074 378 1056 386 1030 386 C900 392 760 384 640 388 "
           "C560 390 500 386 470 388 L330 470 L408 392 C384 388 366 380 364 352 C360 300 366 250 362 224 "
           "C360 204 380 198 402 196 Z")
    s.yol("bal", bal, 0.0, 0.5, KRE, 4.2, 1, "cizgi", 0.7, g="bal")
    BF, BX = 44, 412
    sp = Y.genislik("Fredoka", 600, " ", BF)
    pos = {}
    for idx, base in ((range(0, 4), 258), (range(4, 7), 328)):
        x = BX
        for i in idx:
            m, t = Z["balon_kelime"][i]
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(t), 0.12,
                   tur="tik" if i in (2, 6) else None, g="bal")
            pos[i] = (x, w, base)
            x += w + sp
    x, w, base = pos[2]   # fosforlu belirteç: -ed altı
    s.yol("bm2", el_cizgi(x - 2, base + 12, x + w + 2, base + 9), S(Z["balon_kelime"][2][1]), 0.28, SAR, 8, 0.85,
          "cizgi", 0.5, g="bal")
    # ---------------- sağ sütun: watch-ed / went / didn't play (grup "rows") ----------------
    RF, RX, RY = 72, 1130.0, [330, 450, 570]
    satir = [[("watch", KRE), ("-ed", SAR)], [("went", KRE)], [("didn't play", KRE)]]
    for i in range(3):
        tx, cx = "", RX
        for m, fill in satir[i]:
            tx += '<text x="%.1f" y="%d" fill="%s">%s</text>' % (cx, RY[i], fill, m)
            cx += Y.genislik("Fredoka", 700, m, RF)
        s.grp["rows"].append('<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" '
                             'font-size="%d">%s</g>' % (i, RF, tx))
        t = S(Z["satir"][i])
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
    # ---------------- 69,33: Form — balon, baş ve satırlar toplanır ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    s.to("#ku-ajanda", tf, {"opacity": 0, "duration": 0.2})
    s.to("#ku-nokta", tf, {"opacity": 0, "duration": 0.2})
    s.to("#ku-ajanda2", tf, {"opacity": 1, "duration": 0.2})
    s.to("#ku-nokta2", tf, {"opacity": 1, "duration": 0.2})
    s.to("#balg", tf + 0.1, {"svgOrigin": "56 110", "scale": 0.5, "opacity": 0.45, "duration": 0.8,
                             "ease": "power3.inOut"})
    s.to("#rowsg", tf + 0.1, {"svgOrigin": "1130 300", "x": 120, "y": -190, "scale": 0.55, "opacity": 0.6,
                              "duration": 0.8, "ease": "power3.inOut"})
    s.olay(tf + 0.1, "parilti", 0.5)
    s.yazi("ikiyol", 640, 282, [("iki yol var", SAR)], "Caveat", 700, 56, S(Z["iki_yol"]), 0.5, tur="tik", guc=0.5)
    # ---------------- sol kolon: düzenli -> + -ed ----------------
    LX, RXC, BAS = 140.0, 1000.0, 372
    x, w = s.yazi("dz", LX, BAS, [("düzenli", KRE)], "Fredoka", 700, 84, S(Z["duzenli"]), 0.4, tur="tik", guc=0.55)
    s.yol("dza", el_ok(x + w + 22, BAS - 30, x + w + 124, BAS - 32), S(Z["duzenli"]) + 0.6, 0.3, SAR, 6.5, 0.9,
          "cizgi", 0.5)
    ex, ew = s.pop("ed", x + w + 150, BAS + 8, [("+ ", KRE), ("-ed", SAR)], "Fredoka", 700, 96, S(Z["ed"]), 0.35)
    s.yol("edal", el_cizgi(ex + Y.genislik("Fredoka", 700, "+ ", 96) - 4, BAS + 28, ex + ew + 6, BAS + 24), S(Z["ed"]) + 0.3,
          0.3, SAR, 8, 0.85, "cizgi", 0.45)
    ya = BAS + 100
    w1 = Y.genislik("Fredoka", 700, "watch", 56)
    s.yazi("o1a", LX, ya, [("watch", IKN)], "Fredoka", 700, 56, S(Z["ornek1"]), 0.25, tur="tik", guc=0.5)
    s.yol("o1k", el_ok(LX + w1 + 18, ya - 20, LX + w1 + 88, ya - 22, 14), S(Z["ornek1"]) + 0.25, 0.25, SAR, 5.5, 0.9,
          "cizgi", 0.4)
    s.yazi("o1b", LX + w1 + 110, ya, [("watch", KRE), ("ed", SAR)], "Fredoka", 700, 56, S(Z["ornek1"]) + 0.45, 0.35,
           tur="tik", guc=0.5)
    # ---------------- ayraç + sağ kolon: düzensiz -> V2 ----------------
    s.yol("ayr", el_cizgi(960, 318, 962, 500, 1.5), S(Z["duzensiz"]) - 0.2, 0.35, IKN, 3.5, 1, "cizgi", 0.4)
    x, w = s.yazi("dsz", RXC, BAS, [("düzensiz", KRE)], "Fredoka", 700, 84, S(Z["duzensiz"]), 0.4, tur="tik", guc=0.55)
    s.yol("dsza", el_ok(x + w + 22, BAS - 30, x + w + 124, BAS - 32), S(Z["duzensiz"]) + 0.6, 0.3, SAR, 6.5, 0.9,
          "cizgi", 0.5)
    vx, vw = s.pop("v2", x + w + 150, BAS + 8, [("V2", SAR)], "Fredoka", 700, 96, S(Z["v2"]), 0.35)
    s.yol("v2al", el_cizgi(vx - 4, BAS + 28, vx + vw + 6, BAS + 24), S(Z["v2"]) + 0.8, 0.3, SAR, 8, 0.85, "cizgi", 0.45)
    w2 = Y.genislik("Fredoka", 700, "go", 56)
    s.yazi("o2a", RXC, ya, [("go", IKN)], "Fredoka", 700, 56, S(Z["ornek2"]), 0.2, tur="tik", guc=0.5)
    s.yol("o2k", el_ok(RXC + w2 + 18, ya - 20, RXC + w2 + 88, ya - 22, 14), S(Z["ornek2"]) + 0.2, 0.25, SAR, 5.5, 0.9,
          "cizgi", 0.4)
    s.yazi("o2b", RXC + w2 + 110, ya, [("went", SAR)], "Fredoka", 700, 56, S(Z["ornek2"]) + 0.4, 0.35, tur="tik",
           guc=0.5)
    # ---------------- kutu: didn't + V1 / Did + özne + V1? ----------------
    KX, KY, KW, KH = 140.0, 560, 960.0, 250
    s.yol("kutu", el_kutu(KX, KY, KW, KH), S(Z["kutu"]), 0.55, KRE, 4.5, 1, "cizgi", 0.7)
    FS = 72
    l1 = [("didn't", KRE), (" + ", IKN), ("V1", SAR)]
    l2 = [("Did", KRE), (" + ", IKN), ("özne", KRE), (" + ", IKN), ("V1", SAR), ("?", KRE)]
    s.pop("l1", KX + 50, KY + 100, l1, "Fredoka", 700, FS, S(Z["didnt"]), 0.35, "vurus", 0.8)
    s.pop("l2", KX + 50, KY + 205, l2, "Fredoka", 700, FS, S(Z["soru"]), 0.35, "tik", 0.6)
    for k, (lin, yy) in enumerate(((l1, KY + 100), (l2, KY + 205))):
        px = parca_x(lin, "Fredoka", 700, FS, KX + 50)
        i = [j for j, p in enumerate(lin) if p[0] == "V1"][0]
        s.yol("v1al%d" % k, el_cizgi(px[i][0] - 3, yy + 20, px[i][0] + px[i][1] + 5, yy + 16),
              S(Z["v1"]) + 0.12 * k, 0.28, SAR, 8, 0.85, "cizgi", 0.5)
    # ---------------- Türkçe köprüsü: izle-di = watch-ed ----------------
    s.yazi("tr", LX, 872, [("Türkçedeki -di gibi:", IKN)], "Caveat", 700, 48, S(Z["turkce"]), 0.9, tur="tik", guc=0.4)
    YY, CF = 948, 72
    a = [("izle", KRE), ("-di", SAR)]
    b = [("watch", KRE), ("-ed", SAR)]
    wa = sum(Y.genislik("Caveat", 700, p[0], CF) for p in a)
    s.yazi("iz", LX, YY, a, "Caveat", 700, CF, S(Z["izledi"]), 0.6, tur="tik", guc=0.5)
    eq = LX + wa + 34
    s.yol("es1", el_cizgi(eq, YY - 40, eq + 60, YY - 43, 1), S(Z["esit"]), 0.2, KRE, 5.5, 1, "cizgi", 0.5)
    s.yol("es2", el_cizgi(eq + 2, YY - 18, eq + 62, YY - 21, -1), S(Z["esit"]) + 0.2, 0.2, KRE, 5.5, 1, "cizgi", 0.5)
    s.yazi("wa", eq + 94, YY, b, "Caveat", 700, CF, S(Z["watched"]), 0.6, tur="tik", guc=0.5)
    # ---------------- zaman ifadeleri (sağ bölge) ----------------
    TF, TY, TH = 40, 548, 64
    kutular = [("yesterday", Z["yesterday"], 1170.0), ("ago", Z["ago"], None), ("last year", Z["lastyear"], None)]
    x = 1170.0
    bx = []
    for i, (m, t, _) in enumerate(kutular):
        w = Y.genislik("Fredoka", 700, m, TF) + 56
        bx.append((x, w))
        s.yol("tk%d" % i, el_kutu(x, TY, w, TH), S(t), 0.3, KRE, 3.8, 1, "cizgi", 0.55)
        s.yazi("tt%d" % i, x + 28, TY + 45, [(m, KRE)], "Fredoka", 700, TF, S(t) + 0.22, 0.25, tur="tik", guc=0.5)
        s.yol("ti%d" % i, tik_yolu(x + w - 40, TY - 14, 0.8), S(t) + 0.5, 0.22, SAR, 6, 0.95, "cizgi", 0.4)
        x += w + 22
    ax = 1170 + (x - 22 - 1170) / 2
    s.yol("ok", el_ok(ax, TY + TH + 22, ax + 4, TY + TH + 100, 18), S(Z["ok"]), 0.4, SAR, 7, 0.9, "cizgi", 0.55)
    s.pop("sp", ax, TY + TH + 190, [("Simple Past", KRE)], "Fredoka", 700, 88, S(Z["simplepast"]), 0.4, "vurus", 0.9,
          anchor="middle")
    # ---------------- formül kartı, kural cümlesi, Next lesson ----------------
    CX, CY, CW, CH = 1150.0, 840, 700.0, 96
    s.yol("kart", el_kutu(CX, CY, CW, CH), S(Z["kart"]), 0.5, KRE, 4.5, 1, "cizgi", 0.7)
    fp = [("V-ed / V2", KRE), ("  ·  ", IKN), ("did + V1", SAR)]
    fw = sum(Y.genislik("Fredoka", 700, p[0], 50) for p in fp)
    s.pop("kf", CX + (CW - fw) / 2 - 20, CY + 66, fp, "Fredoka", 700, 50, S(Z["kart"]) + 0.3, 0.35, "tik", 0.6)
    s.yol("kt", tik_yolu(CX + CW - 64, CY + 56, 1.0), S(Z["kart"]) + 0.9, 0.25, SAR, 6.5, 0.95, "cizgi", 0.5)
    s.olay(S(Z["kart"]) + 0.75, "vurus", 0.8)
    s.yazi("bi", 1150, 996, [("Biten iş, belli zaman", IKN)], "Caveat", 700, 56, S(Z["biten"]), 0.7, tur="tik", guc=0.5)
    nw = Y.genislik("Lexend", 500, "Next lesson", 24)
    tn2 = S(Z["sonraki"])
    s.yazi("nx", 1864 - nw - 44, 984, [("Next lesson", IKN)], "Lexend", 500, 24, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M%.1f 976 L%.1f 976 M%.1f 969 L%.1f 976 L%.1f 983" % (1864 - 38, 1864 - 4, 1864 - 12, 1864 - 4,
                                                                          1864 - 12), tn2 + 0.3, 0.25, IKN, 3, 1,
          "cizgi", 0.4)
    # ---------------- künye: Question -> Form (ajanda etkin Examples -> Form) ----------------
    kun = Y.kunye_svg("Question", 1)
    k2 = Y.kunye_svg("Form", 2)
    m2 = re.search(r'<text id="ku-ajanda".*?</text><circle id="ku-nokta"[^>]*/>', k2, re.S).group(0)
    m2 = m2.replace('id="ku-aj', 'id="ku-b').replace('id="ku-banda"', 'id="ku-ajanda2" style="opacity:0"').replace(
        'id="ku-nokta"', 'id="ku-nokta2" style="opacity:0;fill:var(--vurgu)"')
    kun = kun.replace('<circle id="ku-nokta"', '<text id="ku-bolum2" x="1864" y="72" text-anchor="end" '
                      'font-family="Lexend" font-weight="700" font-size="24" fill="%s" style="opacity:0">Form</text>'
                      '<circle id="ku-nokta"' % SAR)
    kun = kun.replace("</g>", m2 + "</g>") if kun.endswith("</g>") else kun + m2
    return s, {"kun": kun}


def html(s, parca):
    veri = {"cmd": sorted(s.cmd, key=lambda c: c["t"])}
    bal = "".join(s.grp["bal"])
    rows = "".join(s.grp["rows"])
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
<g id="balg">{bal}</g>
<g id="rowsg">{rows}</g>
{''.join(s.svg)}
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

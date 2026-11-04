"""Sahne 06 DİKEY (HyperFrames 1080x1920, 1020 kare, t_bas 60,47): cümle 6 (öğrenci balonu) + cümle 7 (form).
Simple Present. Yerleşim BRIEF-DIKEY §4: içerik bandı 352–1392, altyazı bandı 1400–1536 (div), platform boş.
Tek kaynak: zamanlar.json (küresel sn) -> yerel sn = t - t_bas. Komut listesi veri olarak JS'e gömülür;
olaylar aynı çağrılardan toplanır (olay.py yalnız bu modülü içe alır).
Tablo iskeleti (kutular + etiketler) form başında çizilir: hücreler konuşmadan önce görünür, alt bant boş kalmaz."""
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
FPS = 30


def S(t):
    return round(t - TB, 4)


def gen(aile, agr, m, boy):
    return Y.genislik(aile, agr, m, boy)


class Sahne:
    def __init__(self):
        self.defs, self.svg, self.cmd, self.ev = [], [], [], []

    def olay(self, t, tur, guc):
        self.ev.append({"kare": round(t * FPS), "tur": tur, "guc": guc})

    def to(self, sel, t, v):
        self.cmd.append({"m": "to", "s": sel, "t": round(t, 4), "v": v})

    def fromto(self, sel, t, a, v):
        self.cmd.append({"m": "fromTo", "s": sel, "t": round(t, 4), "a": a, "v": v})

    def goster(self, sel, t, d=0.35, dx=0, dy=0, sc=None, son=1):
        a = {"opacity": 0, "x": dx, "y": dy}
        v = {"opacity": son, "x": 0, "y": 0, "duration": d, "ease": "power3.out"}
        if sc is not None:
            a["scale"], v["scale"] = sc, 1
        self.fromto(sel, t, a, v)

    def yol(self, id, d, t, sure, stroke=KRE, w=4.0, alfa=1.0, tur="cizgi", guc=0.55):
        self.svg.append('<path id="%s" d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
                        'stroke-linejoin="round" style="opacity:0"/>' % (id, d, stroke, w))
        self.cmd.append({"m": "draw", "id": id, "t": round(t, 4), "d": round(sure, 4), "a": alfa})
        if tur:
            self.olay(t, tur, guc)

    def yazi(self, id, x, y, parcalar, aile, agr, boy, t, d=0.12, anchor="start", tur="tik", guc=0.5, ek=""):
        """Soldan maske ile yazılan metin. Döner: (x0, genişlik)."""
        ws = [gen(aile, agr, p[0], boy) for p in parcalar]
        W = sum(ws)
        x0 = x - W / 2 if anchor == "middle" else (x - W if anchor == "end" else x)
        cx, tx = x0, ""
        for (m, fill), w in zip(parcalar, ws):
            tx += '<text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">%s</text>' % (cx, y, fill, m)
            cx += w
        self.defs.append('<clipPath id="c_%s"><rect id="r_%s" x="%.1f" y="%.1f" width="0" height="%.1f"/></clipPath>'
                         % (id, id, x0 - 8, y - boy * 1.05, boy * 1.5))
        self.svg.append('<g id="%s" font-family="%s" font-weight="%d" font-size="%s" clip-path="url(#c_%s)" %s>%s</g>'
                        % (id, aile, agr, boy, id, ek, tx))
        self.cmd.append({"m": "rev", "id": "r_" + id, "t": round(t, 4), "d": d, "w": round(W + 20, 1)})
        if tur:
            self.olay(t, tur, guc)
        return x0, W

    def duz(self, id, x, y, parcalar, aile, agr, boy, ek=""):
        """Maskesiz metin (opaklık komutlarıyla yönetilir; hayalet etiketler için)."""
        ws = [gen(aile, agr, p[0], boy) for p in parcalar]
        cx, tx = x, ""
        for (m, fill), w in zip(parcalar, ws):
            tx += '<text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">%s</text>' % (cx, y, fill, m)
            cx += w
        self.svg.append('<g id="%s" style="opacity:0" font-family="%s" font-weight="%d" font-size="%s" %s>%s</g>'
                        % (id, aile, agr, boy, ek, tx))
        return x, sum(ws)


def el_daire(cx, cy, rx, ry, kayma=0.0):
    import math
    pts = []
    for i in range(0, 38):
        a = -2.3 + i * (2 * math.pi * 1.04) / 37
        r = 1 + 0.025 * math.sin(a * 3 + kayma)
        pts.append((cx + rx * r * math.cos(a) - 6 * math.sin(a), cy + ry * r * math.sin(a) + 4 * math.cos(a)))
    return "M%.1f %.1f " % pts[0] + " ".join("L%.1f %.1f" % p for p in pts[1:])


def el_cizgi(x0, y0, x1, y1, egim=3.0):
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    return "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x0, y0, mx, my + egim * 2, x1, y1 + egim * 0.4)


def el_kutu(x, y, w, h):
    """Dört kenarı hafif eğri el kutusu (tek yol)."""
    return ("M%.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f "
            "Q%.0f %.0f %.0f %.0f" % (x + 4, y + 3, x + w / 2, y - 3, x + w - 3, y + 1, x + w + 3, y + h / 2,
                                      x + w - 1, y + h - 2, x + w / 2, y + h + 4, x + 5, y + h + 1,
                                      x - 3, y + h / 2, x + 2, y + 6, x + 1, y + 2, x + 5, y + 2))


def el_tik(x, y, boy=26):
    return "M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (x, y, x + boy * 0.4, y + boy * 0.5, x + boy, y - boy * 0.6)


def konusma_balonu(x, y, w, h, ty):
    """Sol kenarında kuyruğu olan, hafif eğri el balonu (yol d). ty: kuyruk ucu y."""
    r = 30
    return ("M%d %d L%d %d Q%d %d %d %d L%d %d Q%d %d %d %d L%d %d Q%d %d %d %d L%d %d L%d %d L%d %d L%d %d "
            "Q%d %d %d %d Z" % (x + r, y + 3, x + w - r, y - 1, x + w + 4, y, x + w + 2, y + r,
                                x + w - 2, y + h - r, x + w, y + h + 3, x + w - r, y + h + 1,
                                x + r, y + h + 3, x - 2, y + h, x, y + h - r,
                                x, ty + 40, x - 56, ty, x + 2, ty - 30, x - 1, y + r,
                                x + 1, y + 1, x + r, y + 3))


def altyazi_dilimleri():
    """altyazi.json parçalarını (cümle 6-7) en çok 2 satıra sığan dilimlere böler -> [(t0, t1, metin)].
    Çok uzun parça (2 satıra sığmayan): küçük yazı kuralı JS/CSS'te (en çok 3 satır, bant içinde)."""
    kok = AD.parent.parent / "ortak" / "anlatim"
    parca = [p for p in json.loads((kok / "altyazi.json").read_text()) if p["cumle"] in (6, 7)]
    soz = json.loads((kok / "sozcukler.json").read_text())
    genis = 1080 - 96

    def satir(m):
        n, cur = 1, ""
        for w in m.split(" "):
            d = (cur + " " + w) if cur else w
            if gen("Lexend", 500, d, 44) > genis and cur:
                n += 1
                cur = w
            else:
                cur = d
        return n
    out = []
    for p in parca:
        if satir(p["metin"]) <= 2:
            out.append((p["t0"], p["t1"], p["metin"]))
            continue
        kel = [s for s in soz if s["cumle"] == p["cumle"] and p["t0"] - 0.05 <= s["t0"] < p["t1"]]
        cur, grup = [], []
        for k in kel:
            if cur and satir(" ".join(x["sozcuk"] for x in cur + [k])) > 2:
                grup.append(cur)
                cur = [k]
            else:
                cur.append(k)
        grup.append(cur)
        for i, g in enumerate(grup):
            out.append((p["t0"] if i == 0 else g[0]["t0"], grup[i + 1][0]["t0"] if i < len(grup) - 1 else p["t1"],
                        " ".join(x["sozcuk"] for x in g)))
    return out


def sigdir(aile, agr, m, boy_ust, genislik_max):
    """metni genislik_max'a sığdıran en büyük boy (boy_ust'u aşmaz)."""
    w = gen(aile, agr, m, boy_ust)
    return boy_ust if w <= genislik_max else int(boy_ust * genislik_max / w)


def uret():
    s = Sahne()
    # ---------------- öğrenci başı (peeps-kit; 160 px) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.5, 91.0, 440.0
    sw = 3.4 / BS
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, sw, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(0.04 * i, 4), "d": 0.32, "a": 1})
        s.olay(0.04 * i, "cizgi", 0.55)
    bal_ids = ["bas"]
    # ---------------- konuşma balonu (Caveat 68; en çok 660 px satır) ----------------
    BF, BXL, BY0, MAXW = 68, 340, 380, 660
    sp = gen("Caveat", 700, " ", BF)
    satirlar, cur, curw = [], [], 0.0
    for i, (m, t) in enumerate(Z["balon_kelime"]):
        w = gen("Caveat", 700, m, BF)
        if cur and curw + sp + w > MAXW:
            satirlar.append(cur)
            cur, curw = [], 0.0
        cur.append((i, m, t, w))
        curw += (sp if len(cur) > 1 else 0) + w
    satirlar.append(cur)
    SH = 82
    bh = len(satirlar) * SH + 34
    bw = max(sum(k[3] for k in sat) + sp * (len(sat) - 1) for sat in satirlar) + 76
    s.yol("bal", konusma_balonu(296, BY0, bw, bh, 520), 0.0, 0.5, KRE, 4.4, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    pos = {}
    for si, sat in enumerate(satirlar):
        x, base = BXL, BY0 + 78 + si * SH
        for i, m, t, w in sat:
            fill = SAR if i in (5, 9) else KRE
            s.yazi("bw%d" % i, x, base, [(m, fill)], "Caveat", 700, BF, S(t), 0.12, tur="tik" if i in (5, 9) else None)
            bal_ids.append("bw%d" % i)
            pos[i] = (x, w, base)
            x += w + sp
    for i in (5, 9):
        x, w, base = pos[i]
        s.yol("bm%d" % i, el_cizgi(x - 2, base + 14, x + w + 2, base + 10), S(Z["balon_kelime"][i][1]), 0.28,
              SAR, 9, 0.85, "cizgi", 0.5)
        bal_ids.append("bm%d" % i)
    # ---------------- 3 satır: rise-s / go-es / take-s (Fredoka 120) ----------------
    RF, RX, RY = 120, 100.0, [900, 1060, 1220]
    govde = [("rise-", "s"), ("go-e", "s"), ("take-", "s")]
    swd = [gen("Fredoka", 700, g[0], RF) for g in govde]
    ssw = gen("Fredoka", 700, "s", RF)
    BIG = 200
    bigw = gen("Fredoka", 700, "s", BIG)
    BXB, BYB = 720.0, 1070.0
    for i in range(3):
        t = S(Z["satir_s"][i])
        s.svg.append('<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
                     '<text id="stem%d" x="%.1f" y="%d" fill="%s">%s</text>'
                     '<text id="ri%d" x="%.1f" y="%d" fill="%s">s</text></g>'
                     % (i, RF, i, RX, RY[i], KRE, govde[i][0], i, RX + swd[i], RY[i], SAR))
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
    # ---------------- 65,73: toplanma -> büyük s ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    for i in range(3):
        x0, y0 = RX + swd[i] + ssw + 16, RY[i] - 40
        x1, y1 = BXB - 16, BYB - 80 + 26 * i
        s.yol("ok%d" % i, "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
            x0, y0, x0 + (x1 - x0) * 0.5, y0, x1 - 60, y1 - 4 * (i - 1), x1, y1),
            tf + 0.04 * i, 0.45, IKN, 4, 1, "cizgi", 0.45)
    for i in range(3):
        ox, oy = RX + swd[i], RY[i]
        ta = tf + 0.35 + 0.08 * i
        s.to("#ri%d" % i, ta, {"svgOrigin": "%.1f %d" % (ox, oy), "x": round(BXB - ox, 1), "y": round(BYB - oy, 1),
                               "scale": round(BIG / RF, 3), "duration": 0.55, "ease": "power3.inOut"})
        s.to("#ri%d" % i, ta + 0.5, {"opacity": 0, "duration": 0.08})
    tp = tf + 0.9
    s.svg.append('<g id="bigw"><text id="big" x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" font-weight="700" '
                 'font-size="%d" style="opacity:0">s</text></g>' % (BXB, BYB, SAR, BIG))
    s.fromto("#big", tp, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 70)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(tp, "vurus", 0.85)
    s.yol("band", el_cizgi(BXB - 8, BYB + 34, BXB + bigw + 10, BYB + 30), tp + 0.4, 0.4, SAR, 11, 0.85, "cizgi", 0.55)
    ipx, ipw = s.yazi("ip", 560, BYB + 150, [("3. tekil kişi", IKN)], "Caveat", 700, 76, S(Z["uc_tekil"]), 0.6)
    solacak = ["#band", "#ip"] + ["#ok%d" % i for i in range(3)] + ["#row%d" % i for i in range(3)]
    # balon ve baş: 0.75 ölçek (yazı ≥ 48 px) üstte toplanır
    s.to("#balg", tf + 0.5, {"svgOrigin": "48 352", "scale": 0.75, "opacity": 0.6, "duration": 0.8,
                             "ease": "power3.inOut"})
    # ---------------- 68,2: sütunlar söner, tablo iskeleti çizilir ----------------
    tb = S(Z["he"])
    for sel in solacak:
        s.to(sel, tb - 0.25, {"opacity": 0, "duration": 0.25, "ease": "power1.in"})
    KX, KW = 48.0, 984.0
    # R1 / R2 kutuları + kart kutusu (hücreler konuşmadan önce görünür)
    R1Y, R1H, R2Y, R2H = 600, 108, 720, 98
    CY0, CH = 828, 316
    s.yol("fr1", el_kutu(KX, R1Y, KW, R1H), tb - 0.05, 0.4, IKN, 3.6, 0.8, "cizgi", 0.45)
    s.yol("fr2", el_kutu(KX, R2Y, KW, R2H), tb + 0.3, 0.4, IKN, 3.6, 0.8, "cizgi", 0.4)
    s.yol("kart", el_kutu(KX, CY0, KW, CH), tb + 0.65, 0.6, KRE, 4.2, 1, "cizgi", 0.6)
    s.yol("kd1", el_cizgi(KX + 30, CY0 + 112, KX + KW - 30, CY0 + 109, 1), tb + 1.1, 0.4, IKN, 3.2, 0.6, "cizgi", 0.3)
    s.yol("kd2", el_cizgi(KX + 30, CY0 + 206, KX + KW - 30, CY0 + 203, -1), tb + 1.4, 0.4, IKN, 3.2, 0.6, "cizgi", 0.3)
    # hayalet etiketler: olumsuz / soru (konuşma anında tam görünür)
    TF = 72
    tw_n = gen("Caveat", 700, "olumsuz", TF)
    tw_s = gen("Caveat", 700, "soru", TF)
    s.duz("tn", KX + KW - 36 - tw_n, CY0 + 190, [("olumsuz", IKN)], "Caveat", 700, TF)
    s.duz("ts", KX + KW - 36 - tw_s, CY0 + 284, [("soru", IKN)], "Caveat", 700, TF)
    s.goster("#tn", tb + 1.5, 0.4, son=0.4)
    s.goster("#ts", tb + 1.7, 0.4, son=0.4)
    s.to("#tn", S(Z["olumsuz"]), {"opacity": 1, "duration": 0.25})
    s.to("#ts", S(Z["soru"]), {"opacity": 1, "duration": 0.25})
    s.olay(S(Z["olumsuz"]), "tik", 0.45)
    s.olay(S(Z["soru"]), "tik", 0.45)
    # ---------------- 68,46: R1 he · she · it + V-s ----------------
    base1 = R1Y + 82
    F1 = sigdir("Fredoka", 700, "he · she · it  +  V-s", 88, KW - 70)
    x = KX + 34
    for k, (ad, t) in enumerate((("he", Z["he"]), ("she", Z["she"]), ("it", Z["it"]))):
        pc = ([(" · ", IKN)] if k else []) + [(ad, KRE)]
        x0, W = s.yazi("g_%s" % ad, x, base1, pc, "Fredoka", 700, F1, S(t), 0.25, tur="tik", guc=0.55)
        x += W
    pw = gen("Fredoka", 700, "  +  ", F1)
    vw = gen("Fredoka", 700, "V-", F1)
    s.yazi("pls", x, base1, [("  +  ", IKN), ("V-", KRE)], "Fredoka", 700, F1, S(Z["vs"]), 0.3, tur="tik", guc=0.5)
    sx = x + pw + vw
    # büyük s, V- yanındaki yuvasına yerleşir (form başında, s sözcüğüne kadar bekler: 71,43 vurgu)
    s.to("#big", tb + 0.0, {"svgOrigin": "%.1f %.1f" % (BXB, BYB), "x": round(sx - BXB, 1), "y": round(base1 - BYB, 1),
                            "scale": round(F1 / BIG, 3), "duration": 0.6, "ease": "power3.inOut"})
    s.to("#big", S(Z["vs_s"]), {"svgOrigin": "%.1f %.1f" % (sx, base1 - 30), "scale": round(F1 / BIG * 1.3, 3),
                                "duration": 0.18, "ease": "power2.out"})
    s.to("#big", S(Z["vs_s"]) + 0.18, {"svgOrigin": "%.1f %.1f" % (sx, base1 - 30), "scale": round(F1 / BIG, 3),
                                       "duration": 0.25, "ease": "power2.inOut"})
    s.olay(S(Z["vs_s"]), "vurus", 0.8)
    sw1 = gen("Fredoka", 700, "s", F1)
    s.yol("vsal", el_cizgi(sx - 4, base1 + 18, sx + sw1 + 8, base1 + 15), S(Z["vs_s"]) + 0.2, 0.3, SAR, 9, 0.85,
          "cizgi", 0.45)
    # ---------------- 72,55: R2 I · you · we · they + V (s yok) ----------------
    base2 = R2Y + 72
    F2 = sigdir("Fredoka", 700, "I · you · we · they  +  V", 76, KW - 70)
    x = KX + 34
    for k, (ad, t) in enumerate((("I", Z["diger"][0]), ("you", Z["diger"][1]), ("we", Z["diger"][2]),
                                 ("they", Z["diger"][3]))):
        pc = ([(" · ", IKN)] if k else []) + [(ad, IKN)]
        x0, W = s.yazi("d_%s" % ad, x, base2, pc, "Fredoka", 700, F2, S(t), 0.25, tur="tik", guc=0.45,
                       ek='opacity="0.85"')
        x += W
    s.yazi("d_v", x, base2, [("  +  ", IKN), ("V", IKN)], "Fredoka", 700, F2, S(Z["go"]), 0.25, tur="tik", guc=0.4,
           ek='opacity="0.85"')
    gx = x + gen("Fredoka", 700, "  +  V", F2)
    s.yazi("d_s", gx + 4, base2, [("-s", SAR)], "Fredoka", 700, F2, S(Z["kirmizi"]) - 0.1, 0.15, tur=None,
           ek='opacity="0.55"')
    sw2 = gen("Fredoka", 700, "-s", F2)
    s.yol("kir", el_cizgi(gx - 6, base2 - 4, gx + sw2 + 16, base2 - 44, 2), S(Z["kirmizi"]), 0.45, KIR, 9, 1, "cizgi", 0.7)
    s.yol("kir2", el_cizgi(gx + 2, base2 - 46, gx + sw2 + 10, base2 + 6, -2), S(Z["kirmizi"]) + 0.25, 0.3, KIR, 9, 1,
          "cizgi", 0.5)
    # ---------------- 77,74: kart: does ; 78,70: s ona geçer ----------------
    tk = S(Z["kart"])
    HF = 110
    dw = gen("Fredoka", 700, "does", HF)
    hx0, hbase = KX + 40, CY0 + 92
    s.yazi("does", hx0, hbase, [("does", SAR)], "Fredoka", 700, HF, tk, 0.35, tur="tik", guc=0.6)
    s.yazi("dnot", hx0 + dw + 36, hbase - 8, [("= yardımcı fiil", IKN)], "Caveat", 700, 72, tk + 0.4, 0.5, tur=None)
    ts = S(Z["s_gec"])
    s.svg.append('<g id="sdup"><text id="sd" x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" font-weight="700" '
                 'font-size="%d" style="opacity:0">s</text></g>' % (sx, base1, SAR, F1))
    hx, hy = hx0 + dw - 20, hbase
    s.fromto("#sd", ts, {"opacity": 0, "scale": 1, "svgOrigin": "%.1f %.1f" % (sx, base1)}, {"opacity": 1, "duration": 0.05})
    s.to("#sd", ts + 0.05, {"svgOrigin": "%.1f %.1f" % (sx, base1), "x": round(hx - sx, 1), "y": round(hy - base1, 1),
                            "scale": round(HF / F1, 3), "duration": 0.55, "ease": "power3.inOut"})
    s.to("#sd", ts + 0.62, {"opacity": 0, "duration": 0.1})
    s.to("#does", ts + 0.6, {"svgOrigin": "%.1f %.1f" % (hx0 + dw / 2, hbase - 40), "scale": 1.1, "duration": 0.18,
                             "ease": "power2.out"})
    s.to("#does", ts + 0.78, {"svgOrigin": "%.1f %.1f" % (hx0 + dw / 2, hbase - 40), "scale": 1.0, "duration": 0.25,
                              "ease": "power2.inOut"})
    s.olay(ts + 0.6, "vurus", 0.8)
    # ---------------- 80,47 / 82,23: He does not go. / Does he go? ----------------
    LF2 = 76
    t1 = Z["he_does"]
    x = KX + 40
    b3, b4 = CY0 + 190, CY0 + 284
    for k, (m, fill, t) in enumerate((("He", KRE, t1[0]), (" does", SAR, t1[1]), (" not", KRE, t1[2]),
                                      (" go.", KRE, t1[3]))):
        x0, W = s.yazi("hd%d" % k, x, b3, [(m, fill)], "Fredoka", 700, LF2, S(t), 0.2,
                       tur="tik" if k == 1 else None, guc=0.5)
        x += W
    t2 = Z["does_he"]
    x = KX + 40
    for k, (m, fill, t) in enumerate((("Does", SAR, t2[0]), (" he", KRE, t2[1]), (" go?", KRE, t2[2]))):
        x0, W = s.yazi("dh%d" % k, x, b4, [(m, fill)], "Fredoka", 700, LF2, S(t), 0.2,
                       tur="tik" if k == 0 else None, guc=0.5)
        x += W
    # ---------------- 83,68: Türkçe: -er eki ; 85,60: git-er = go-es ----------------
    LY = 1222
    EF = 84
    trw = gen("Caveat", 700, "Türkçe: ", 72)
    gw1 = gen("Fredoka", 700, "git-er", EF)
    eqw = gen("Fredoka", 700, " = ", EF)
    gw2 = gen("Fredoka", 700, "go-es", EF)
    toplam = trw + gw1 + eqw + gw2
    lx = 540 - toplam / 2
    s.yazi("tr", lx, LY, [("Türkçe: ", IKN)], "Caveat", 700, 72, S(Z["turkce"]), 0.4, tur="tik", guc=0.4)
    s.yazi("gter", lx + trw, LY, [("git", KRE), ("-er", SAR)], "Fredoka", 700, EF, S(Z["git_er"]), 0.4, tur="tik",
           guc=0.5)
    ex = lx + trw + gw1
    te = S(Z["esit"])
    s.yol("es1", el_cizgi(ex + 14, LY - 40, ex + eqw - 14, LY - 43, 1), te, 0.2, KRE, 6, 1, "cizgi", 0.5)
    s.yol("es2", el_cizgi(ex + 16, LY - 18, ex + eqw - 12, LY - 21, -1), te + 0.2, 0.2, KRE, 6, 1, "cizgi", 0.5)
    s.yazi("goes", ex + eqw, LY, [("go", KRE), ("-es", SAR)], "Fredoka", 700, EF, S(Z["go_es"]), 0.4, tur="tik", guc=0.5)
    # ---------------- 87,75: always · usually · every day -> Simple Present ----------------
    CF = 72
    x = 60.0
    CYL = 1298
    sepw = gen("Caveat", 700, " · ", CF)
    toplam = sum(gen("Caveat", 700, m, CF) for m in ("always", "usually", "every day")) + 2 * sepw
    x = 540 - toplam / 2
    for k, (m, t) in enumerate((("always", Z["always"]), ("usually", Z["usually"]), ("every day", Z["every_day"]))):
        pc = ([(" · ", IKN)] if k else []) + [(m, KRE)]
        x0, W = s.yazi("f%d" % k, x, CYL, pc, "Caveat", 700, CF, S(t), 0.3, tur="tik", guc=0.55)
        wm = gen("Caveat", 700, m, CF)
        xm = x0 + (sepw if k else 0)
        s.yol("fu%d" % k, el_cizgi(xm, CYL + 12, xm + wm, CYL + 9), S(t) + 0.25, 0.25, SAR, 9, 0.85, "cizgi", 0.45)
        x += W
    SF = 80
    spw = gen("Fredoka", 700, "Simple Present", SF)
    sx0 = 540 - spw / 2 + 40
    SYL = 1386
    s.yol("fok", "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        sx0 - 150, SYL - 30, sx0 - 110, SYL - 40, sx0 - 80, SYL - 24, sx0 - 36, SYL - 28,
        sx0 - 54, SYL - 42, sx0 - 36, SYL - 28, sx0 - 56, SYL - 14), S(Z["simple"]) - 0.45, 0.4, IKN, 5, 1, "cizgi", 0.5)
    s.yazi("fsp", sx0, SYL, [("Simple Present", SAR)], "Fredoka", 700, SF, S(Z["simple"]), 0.6, tur="tik", guc=0.6)
    s.olay(S(Z["present"]), "vurus", 0.8)
    # ---------------- altyazı dilimleri (opaklık anahtarları) ----------------
    dil = altyazi_dilimleri()
    s.altyazi = ["%s" % d[2] for d in dil]

    def aktif(t):
        k = -1
        for i, (t0, t1_, _m) in enumerate(dil):
            if t0 - 0.05 <= t < t1_ + 0.35:
                k = i
        return k
    onc = -1
    for f in range(Z["kare"]):
        k = aktif(TB + f / FPS)
        if k != onc:
            if onc >= 0:
                s.cmd.append({"m": "set", "s": "#alt%d" % onc, "t": round(f / FPS, 4), "v": {"opacity": 0}})
            if k >= 0:
                s.cmd.append({"m": "set", "s": "#alt%d" % k, "t": round(f / FPS, 4), "v": {"opacity": 1}})
            onc = k
    kun = Y.kunye_svg("Question", "Form")
    return s, {"kun": kun, "bal_ids": bal_ids}


def html(s, parca):
    bal_ids = set(parca["bal_ids"])
    bal_html, diger = [], []
    for e in s.svg:
        idn = e.split('id="', 1)[1].split('"', 1)[0]
        (bal_html if idn in bal_ids else diger).append(e)
    veri = {"cmd": sorted(s.cmd, key=lambda c: c["t"])}
    alt = "".join('<div id="alt%d" class="alt"><span class="at">%s</span></div>' % (
        i, " ".join('<span style="white-space:nowrap">%s</span>' % w for w in m.split(" ")))
        for i, m in enumerate(s.altyazi))
    lw = 96 * Y.LOGO_EN_BOY
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
.alt{{position:absolute;left:48px;top:1400px;width:984px;height:136px;display:flex;align-items:center;
justify-content:center;text-align:center;font:500 44px/56px Lexend,sans-serif;color:var(--murekkep,#f3efe6);opacity:0;
overflow:hidden;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>{''.join(s.defs)}</defs>
<g id="balg">{''.join(bal_html)}</g>
{''.join(diger)}
{parca['kun']}
<image id="logo" href="assets/logo.svg" x="48" y="48" width="{lw:.2f}" height="96"/>
</svg>
{alt}</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var C = {json.dumps(veri, ensure_ascii=False)};
  var tl = gsap.timeline({{ paused: true }});
  var $ = function (q) {{ return document.querySelector(q); }};
  // Altyazı: bant içinde kal. 2 satıra sığmazsa yazı 44→40→36 küçülür, en çok 3 satır, taşma yok.
  function sigdir() {{
    document.querySelectorAll(".alt").forEach(function (a) {{
      var at = a.querySelector(".at"), boy = [[44, 56], [40, 50], [36, 46]];
      for (var i = 0; i < boy.length; i++) {{
        a.style.fontSize = boy[i][0] + "px"; a.style.lineHeight = boy[i][1] + "px";
        var max = i < boy.length - 1 ? 2 : 3;
        if (Math.round(at.getBoundingClientRect().height / boy[i][1]) <= max) break;
      }}
    }});
  }}
  sigdir();
  if (document.fonts && document.fonts.load) document.fonts.load("500 44px Lexend", "İşğçö").then(sigdir);
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
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "altyazı", len(s.altyazi))

"""Sahne 06 DİKEY (HyperFrames 1080x1920, 766 kare, t_bas 62,81): cümle 6 (öğrenci balonu) + cümle 7 (form).
Yerleşim BRIEF-DIKEY §4 + 05.11 kararları. Tek kaynak: zamanlar.json (küresel sn) -> yerel sn = t - t_bas.
Komut listesi veri olarak JS'e gömülür; olaylar aynı çağrılardan toplanır (olay.py yalnız bu modülü içe alır).
- t≈66 s -ing örtüşmesi düzeltildi (satır ve toplanma yerleşimi ayrıldı).
- t 71–74 s içerik bandı boş kalması düzeltildi (tablo satırları erken getirildi, boşluk kapatıldı).
- Bu pakette Next lesson öğesi yok (anlatım 85,09 s'de biter).
- Tüm Caveat etiketleri ≥ 56 px.
"""
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


class Sahne:
    def __init__(self):
        self.defs, self.svg, self.cmd, self.ev = [], [], [], []

    def olay(self, t, tur, guc):
        self.ev.append({"kare": round(t * FPS), "tur": tur, "guc": guc})

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

    def yol(self, id, d, t, sure, stroke=KRE, w=4.0, alfa=1.0, tur="cizgi", guc=0.55):
        self.svg.append('<path id="%s" d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
                        'stroke-linejoin="round" style="opacity:0"/>' % (id, d, stroke, w))
        self.cmd.append({"m": "draw", "id": id, "t": round(t, 4), "d": round(sure, 4), "a": alfa})
        if tur:
            self.olay(t, tur, guc)

    def yazi(self, id, x, y, parcalar, aile, agr, boy, t, d=0.12, anchor="start", tur="tik", guc=0.5, ek=""):
        """Soldan maske ile yazılan metin. Döner: (x0, genişlik)."""
        ws = [Y.genislik(aile, agr, p[0], boy) for p in parcalar]
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


def altyazi_dilimleri():
    """altyazi.json parçalarını (cümle 6-7) en çok 2 satıra sığan dilimlere böler -> [(t0, t1, metin)]."""
    kok = AD.parent.parent / "ortak" / "anlatim"
    parca = [p for p in json.loads((kok / "altyazi.json").read_text()) if p["cumle"] in (6, 7)]
    soz = json.loads((kok / "sozcukler.json").read_text())
    gen = 1080 - 96

    def satir(m):
        n, cur = 1, ""
        for w in m.split(" "):
            d = (cur + " " + w) if cur else w
            if Y.genislik("Lexend", 500, d, 44) > gen and cur:
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


def uret():
    s = Sahne()
    # ---------------- öğrenci başı (peeps-kit; 160 px) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.5, 91.0, 477.0
    sw = 3.4 / BS
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, sw, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(0.04 * i, 4), "d": 0.32, "a": 1})
        s.olay(0.04 * i, "cizgi", 0.55)

    # ---------------- konuşma balonu (y 416-650) ----------------
    bal = ("M300 424 C420 414 700 422 1000 416 C1032 415 1048 428 1048 458 C1046 520 1050 580 1046 610 "
           "C1044 638 1026 648 998 648 C800 652 560 646 330 650 C304 651 288 638 288 610 L288 590 L232 562 "
           "L288 546 C286 502 290 466 288 454 C286 436 296 425 300 424 Z")
    s.yol("bal", bal, 0.0, 0.5, KRE, 4.4, 1, "cizgi", 0.7)
    BF, BX = 72, 330
    sp = Y.genislik("Caveat", 700, " ", BF)
    pos = {}
    for idx, base in ((range(0, 5), 506), (range(5, 8), 600)):
        x = BX
        for i in idx:
            m, t = Z["balon_kelime"][i]
            w = Y.genislik("Caveat", 700, m, BF)
            fill = SAR if i in (3, 7) else KRE
            s.yazi("bw%d" % i, x, base, [(m, fill)], "Caveat", 700, BF, S(t), 0.12, tur="tik" if i in (3, 7) else None)
            pos[i] = (x, w, base)
            x += w + sp
    for i in (3, 7):
        x, w, base = pos[i]
        s.yol("bm%d" % i, el_cizgi(x - 2, base + 14, x + w + 2, base + 10), S(Z["balon_kelime"][i][1]), 0.28,
              SAR, 9, 0.85, "cizgi", 0.5)

    # ---------------- 3 satır: sitt-ing / tak-ing / climb-ing ----------------
    # y hiza: 880, 990, 1100
    RF, RX, RY = 96, 90.0, [880, 990, 1100]
    stems = ["sitt", "tak", "climb"]
    swd = [Y.genislik("Fredoka", 700, m, RF) for m in stems]
    ingw = Y.genislik("Fredoka", 700, "-ing", RF)
    BIG = 150
    bigw = Y.genislik("Fredoka", 700, "-ing", BIG)
    BXB, BYB = 620.0, 990.0
    solacak = []
    for i in range(3):
        t = S(Z["satir_ing"][i])
        s.svg.append('<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
                     '<text id="stem%d" x="%.1f" y="%d" fill="%s">%s</text>'
                     '<text id="ri%d" x="%.1f" y="%d" fill="%s">-ing</text></g>'
                     % (i, RF, i, RX, RY[i], KRE, stems[i], i, RX + swd[i], RY[i], SAR))
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
        solacak.append("#row%d" % i)

    # ---------------- 66,72: toplanma (form) ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    for i in range(3):
        x0, y0 = RX + swd[i] + ingw + 14, RY[i] - 30
        x1, y1 = BXB - 16, BYB - 60 + 24 * i
        s.yol("ok%d" % i, "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
            x0, y0, x0 + (x1 - x0) * 0.5, y0, x1 - 60, y1 - 4 * (i - 1), x1, y1),
            tf + 0.04 * i, 0.45, IKN, 4, 1, "cizgi", 0.45)
        solacak.append("#ok%d" % i)

    for i in range(3):
        ox, oy = RX + swd[i], RY[i]
        ta = tf + 0.35 + 0.08 * i
        s.to("#ri%d" % i, ta, {"svgOrigin": "%.1f %d" % (ox, oy), "x": round(BXB - ox, 1), "y": round(BYB - oy, 1),
                               "scale": round(BIG / RF, 3), "duration": 0.45, "ease": "power3.inOut"})
        s.to("#ri%d" % i, ta + 0.45, {"opacity": 0, "duration": 0.08})

    tp = tf + 0.8
    s.svg.append('<g id="bigw"><text id="big" x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" font-weight="700" '
                 'font-size="%d" style="opacity:0">-ing</text></g>' % (BXB, BYB, SAR, BIG))
    s.fromto("#big", tp, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 50)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(tp, "vurus", 0.85)
    s.yol("band", el_cizgi(BXB - 6, BYB + 28, BXB + bigw + 8, BYB + 24), tp + 0.35, 0.4, SAR, 11, 0.85, "cizgi", 0.55)
    ipx, ipw = s.yazi("ip", BXB - 10, BYB + 105, [("in progress", IKN)], "Caveat", 700, 72, tp + 0.7, 0.45)
    s.yol("ipok", "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        ipx + ipw + 14, BYB + 90, ipx + ipw + 44, BYB + 82, ipx + ipw + 62, BYB + 92, ipx + ipw + 86, BYB + 86,
        ipx + ipw + 72, BYB + 74, ipx + ipw + 86, BYB + 86, ipx + ipw + 70, BYB + 100),
        tp + 1.15, 0.4, IKN, 4.5, 1, "cizgi", 0.5)
    solacak += ["#band", "#ip", "#ipok"]
    s.to("#balg", tf + 0.5, {"opacity": 0.4, "duration": 0.8, "ease": "power3.inOut"})

    # ---------------- 71,43: be tablosu + V-ing ----------------
    # BULGU DÜZELTMESİ (t 71-74 s boşluk):
    # solacak elemanları tb anında silinir; tablo satırları (I am, He is, We are) erken gelir!
    tb = S(Z["be"])
    for sel in solacak:
        s.to(sel, tb, {"opacity": 0, "duration": 0.35, "ease": "power1.in"})

    CF = 96
    bx, bw = s.yazi("belb", 100, 730, [("be", IKN)], "Fredoka", 700, CF, tb, 0.3)
    s.yol("beal", el_cizgi(bx - 4, 750, bx + bw + 10, 747), tb + 0.2, 0.35, SAR, 9, 0.85, "cizgi", 0.45)

    VF, VX, VY = 110, 580.0, 960.0
    vw = Y.genislik("Fredoka", 700, "V", VF)
    s.svg.append('<g id="vv" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
                 '<text x="%.1f" y="%.1f" fill="%s">V</text></g>' % (VF, VX, VY, KRE))
    ta = tb + 0.1
    s.to("#big", ta, {"svgOrigin": "%.1f %.1f" % (BXB, BYB), "x": round(VX + vw - BXB, 1), "y": round(VY - BYB, 1),
                      "scale": round(VF / BIG, 3), "duration": 0.55, "ease": "power3.inOut"})
    s.fromto("#vv", ta + 0.4, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (VX + vw / 2, VY - 40)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(ta + 0.4, "vurus", 0.85)

    # Satırlar: erken getirilir (tb + 0.35, tb + 0.85, tb + 1.35) -> t≈71.8, 72.3, 72.8'de ekranda hazır!
    rows = [("I ", "am", "am", 830, tb + 0.35),
            ("He ", "is", "is", 960, tb + 0.85),
            ("We ", "are", "are", 1090, tb + 1.35)]
    for i, (sb, fi, k, y, t_yazi) in enumerate(rows):
        wsb = Y.genislik("Fredoka", 700, sb, CF)
        wf = Y.genislik("Fredoka", 700, fi, CF)
        s.yazi("c_%s" % k, 100, y, [(sb, IKN), (fi, KRE)], "Fredoka", 700, CF, t_yazi, 0.3, tur="tik", guc=0.45)
        # Alt çizgi ses zamanında parlar (am 73.83, is 74.55, are 75.19)
        s.yol("ua%d" % i, el_cizgi(100 + wsb - 4, y + 20, 100 + wsb + wf + 8, y + 17), S(Z[k]), 0.3, SAR, 9,
              0.85, "cizgi", 0.55)

    tn = S(Z["now"])
    bx0, top, bot = 520, 770, 1110
    mid = (top + bot) // 2
    s.yol("kuma", "M%d %d C%d %d %d %d %d %d C%d %d %d %d %d %d C%d %d %d %d %d %d C%d %d %d %d %d %d" % (
        bx0, top, bx0 + 26, top + 10, bx0 + 14, top + 40, bx0 + 14, top + 90,
        bx0 + 14, mid - 40, bx0 + 26, mid - 14, bx0 + 46, mid,
        bx0 + 26, mid + 14, bx0 + 14, mid + 40, bx0 + 14, bot - 90,
        bx0 + 14, bot - 40, bx0 + 26, bot - 10, bx0, bot), tn, 0.5, IKN, 4.5, 1, "cizgi", 0.45)
    s.yazi("now", VX - 4, 1056, [("now", SAR)], "Caveat", 700, 80, tn + 0.25, 0.4, tur="tik", guc=0.5)

    # ---------------- was · were -> past ----------------
    WF, WX, WY = 72, 100.0, 1185
    ww = Y.genislik("Fredoka", 700, "was", WF)
    dot = Y.genislik("Fredoka", 700, " · ", WF)
    wew = Y.genislik("Fredoka", 700, "were", WF)
    s.yazi("was", WX, WY, [("was", IKN)], "Fredoka", 700, WF, S(Z["was"]), 0.2, tur="tik", guc=0.4, ek='opacity="0.6"')
    s.yazi("dotw", WX + ww, WY, [(" · ", IKN)], "Fredoka", 700, WF, S(Z["was"]) + 0.2, 0.1, tur=None, ek='opacity="0.6"')
    s.yazi("were", WX + ww + dot, WY, [("were", IKN)], "Fredoka", 700, WF, S(Z["were"]), 0.2, tur="tik", guc=0.4,
           ek='opacity="0.6"')
    xe = WX + ww + dot + wew
    s.yazi("past", xe + 50, WY - 4, [("past", IKN)], "Caveat", 700, 72, S(Z["past"]), 0.4, tur="tik", guc=0.45)
    s.yol("kir", el_cizgi(WX - 12, WY - 26, xe + 14, WY - 40, 2), S(Z["cizgi_kirmizi"]), 0.45, KIR, 8, 1, "cizgi", 0.7)

    # ---------------- 81,25: -ing = -yor ----------------
    th = S(Z["ing_halka"])
    ingv = Y.genislik("Fredoka", 700, "-ing", VF)
    s.yol("halka", el_daire(VX + vw + ingv / 2, VY - 38, ingv / 2 + 16, 74, 1.0), th, 0.55, SAR, 8, 0.85, "parilti", 0.5)
    EF, EY = 110, 1285
    w1, w2, w3 = (Y.genislik("Fredoka", 700, m, EF) for m in ("-ing", " = ", "-yor"))
    ex0 = 540 - (w1 + w2 + w3) / 2
    s.svg.append('<g id="eqf" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
                 '<text x="%.1f" y="%d" fill="%s">-ing</text><text x="%.1f" y="%d" fill="%s" xml:space="preserve"> = </text>'
                 '<text x="%.1f" y="%d" fill="%s">-yor</text></g>' % (EF, ex0, EY, SAR, ex0 + w1, EY, KRE,
                                                                      ex0 + w1 + w2, EY, SAR))
    s.fromto("#eqf", th, {"opacity": 0, "scale": 0.92, "svgOrigin": "540 %d" % (EY - 40)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(th, "vurus", 0.85)

    # ---------------- koşu-yor = runn-ing (Caveat 72) ----------------
    LF, LY = 72, 1362
    wk = Y.genislik("Caveat", 700, "koşu-yor", LF)
    wr = Y.genislik("Caveat", 700, "runn-ing", LF)
    gap, eqw = 36, 56
    lx = 540 - (wk + gap + eqw + gap + wr) / 2
    s.yazi("kosu", lx, LY, [("koşu", KRE), ("-yor", SAR)], "Caveat", 700, LF, S(Z["yor"]), 0.45)
    ex = lx + wk + gap
    te = S(Z["esit"])
    s.yol("es1", el_cizgi(ex, LY - 34, ex + eqw, LY - 37, 1), te, 0.2, KRE, 6, 1, "cizgi", 0.5)
    s.yol("es2", el_cizgi(ex + 2, LY - 14, ex + eqw + 2, LY - 17, -1), te + 0.2, 0.2, KRE, 6, 1, "cizgi", 0.5)
    s.yazi("runn", ex + eqw + gap, LY, [("runn", KRE), ("-ing", SAR)], "Caveat", 700, LF, S(Z["runn"]), 0.45)

    # ---------------- altyazı dilimleri (opaklık anahtarları) ----------------
    dil = altyazi_dilimleri()
    s.altyazi = ["%s" % d[2] for d in dil]

    def aktif(t):
        k = -1
        for i, (t0, t1, _m) in enumerate(dil):
            if t0 - 0.05 <= t < t1 + 0.35:
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
    bal_ids = ["bal", "bas", "bm3", "bm7"] + ["bw%d" % i for i in range(8)]
    return s, {"kun": kun, "bal_ids": bal_ids}


def html(s, parca):
    bal_ids = set(parca["bal_ids"])
    bal_html, diger = [], []
    for e in s.svg:
        idn = e.split('id="', 1)[1].split('"', 1)[0]
        (bal_html if idn in bal_ids else diger).append(e)
    veri = {"cmd": sorted(s.cmd, key=lambda c: c["t"])}
    alt = "".join('<div id="alt%d" class="alt"><span>%s</span></div>' % (
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
justify-content:center;text-align:center;font:500 44px/56px Lexend,sans-serif;color:var(--murekkep,#f3efe6);opacity:0;}}
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

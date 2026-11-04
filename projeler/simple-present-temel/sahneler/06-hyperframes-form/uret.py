"""Sahne 06 (öğrenci sorusu + form) index.html + olay listesi üretici — Simple Present, YATAY 1920x1080.
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
        x0 = x - W if anchor == "end" else (x - W / 2 if anchor == "middle" else x)
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


def el_tik(x, y, boy=26):
    """Küçük el tiki (yol d): sol-alt kısa kol, sağ-üst uzun kol."""
    return "M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (x, y, x + boy * 0.4, y + boy * 0.5, x + boy, y - boy * 0.6)


def konusma_balonu(x, y, w, h, ty):
    """Sol kenarında kuyruğu olan, hafif eğri el balonu (yol d). ty: kuyruk ucu y."""
    r = 28
    return ("M%d %d L%d %d Q%d %d %d %d L%d %d Q%d %d %d %d L%d %d Q%d %d %d %d L%d %d L%d %d L%d %d L%d %d "
            "Q%d %d %d %d Z" % (x + r, y + 3, x + w - r, y - 1, x + w + 4, y, x + w + 2, y + r,
                                x + w - 2, y + h - r, x + w, y + h + 3, x + w - r, y + h + 1,
                                x + r, y + h + 3, x - 2, y + h, x, y + h - r,
                                x, ty + 46, x - 58, ty, x + 2, ty - 34, x - 1, y + r,
                                x + 1, y + 1, x + r, y + 3))


def uret():
    s = Sahne()
    # ---------------- öğrenci başı (peeps-kit: LongBangs + Smile + GlassRound) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.59, 128.0, 206.0   # saç dahil boy ≈ 190 px; yüz merkezi (118,126) -> (198, 280)
    sw = 2.8 / BS
    bas = '<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" ' \
          'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, sw, "".join(
              '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd)))
    s.svg.append(bas)
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(0.04 * i, 4), "d": 0.32, "a": 1})
        s.olay(0.04 * i, "cizgi", 0.55)
    bal_ids = ["bas"]
    # ---------------- konuşma balonu: kelimeler 44 px, en çok 640 px satır ----------------
    BF, BX0, BY, MAXW = 44, 406, 170, 640
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satirlar, cur, curw = [], [], 0.0
    for i, (m, t) in enumerate(Z["balon_kelime"]):
        w = Y.genislik("Fredoka", 600, m, BF)
        if cur and curw + sp + w > MAXW:
            satirlar.append(cur)
            cur, curw = [], 0.0
        cur.append((i, m, t, w))
        curw += (sp if len(cur) > 1 else 0) + w
    satirlar.append(cur)
    bh = len(satirlar) * 66 + 36
    bw = max(sum(k[3] for k in sat) + sp * (len(sat) - 1) for sat in satirlar) + 88
    s.yol("bal", konusma_balonu(362, BY, bw, bh, 300), 0.0, 0.5, KRE, 4.2, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    pos = {}
    for si, sat in enumerate(satirlar):
        x, base = BX0, BY + 70 + si * 66
        for i, m, t, w in sat:
            fill = SAR if i in (5, 9) else KRE
            s.yazi("bw%d" % i, x, base, [(m, fill)], "Fredoka", 600, BF, S(t), 0.12,
                   tur="tik" if i in (5, 9) else None)
            bal_ids.append("bw%d" % i)
            pos[i] = (x, w, base)
            x += w + sp
    for i in (5, 9):   # fosforlu belirteç: s altı
        x, w, base = pos[i]
        s.yol("bm%d" % i, el_cizgi(x - 2, base + 12, x + w + 2, base + 9), S(Z["balon_kelime"][i][1]), 0.28,
              SAR, 8, 0.85, "cizgi", 0.5)
        bal_ids.append("bm%d" % i)
    # ---------------- sağ sütun: rise-s / go-es / take-s ----------------
    RF, RX, RY = 96, 1190.0, [330, 470, 610]
    govde = [("rise-", "s"), ("go-e", "s"), ("take-", "s")]
    sw_ = [Y.genislik("Fredoka", 700, g[0], RF) for g in govde]
    BIG = 200
    bigw = Y.genislik("Fredoka", 700, "s", BIG)
    BXB, BYB = 1640.0, 520.0
    for i in range(3):
        t = S(Z["satir_s"][i])
        s.svg.append('<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
                     '<text id="stem%d" x="%.1f" y="%d" fill="%s">%s</text>'
                     '<text id="ri%d" x="%.1f" y="%d" fill="%s">s</text></g>'
                     % (i, RF, i, RX, RY[i], KRE, govde[i][0], i, RX + sw_[i], RY[i], SAR))
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
    # ---------------- 65,73: toplanma ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    sws = Y.genislik("Fredoka", 700, "s", RF)
    for i in range(3):   # kalemle oklar: satır sonundan büyük s'ye
        x0, y0 = RX + sw_[i] + sws + 18, RY[i] - 30
        x1, y1 = BXB - 18, BYB - 70 + 18 * i
        s.yol("ok%d" % i, "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
            x0, y0, x0 + (x1 - x0) * 0.5, y0, x1 - 40, y1 - 4 * (i - 1), x1, y1),
            tf + 0.04 * i, 0.45, IKN, 3.6, 1, "cizgi", 0.45)
    for i in range(3):   # s harfleri büyük s'ye uçar
        ox, oy = RX + sw_[i], RY[i]
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
    s.yol("band", el_cizgi(BXB - 10, BYB + 36, BXB + bigw + 12, BYB + 32), tp + 0.4, 0.4, SAR, 9, 0.85, "cizgi", 0.55)
    ipx, ipw = s.yazi("ip", 1560, BYB + 100, [("3. tekil kişi", IKN)], "Caveat", 700, 52, S(Z["uc_tekil"]), 0.7,
                      tur="tik", guc=0.5)
    # balon ve baş küçülür, sol üste toplanır, soluklaşır
    s.to("#balg", tf + 0.5, {"svgOrigin": "140 120", "scale": 0.5, "opacity": 0.45, "duration": 0.8,
                             "ease": "power3.inOut"})
    kalan = max(1, int((S(Z["bitis_icerik"]) - (tp + 0.5)) / 2.6) - 1)
    s.to("#bigw", tp + 0.5, {"svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 70), "scale": 1.025, "duration": 2.6,
                             "ease": "sine.inOut", "repeat": kalan, "yoyo": True})
    # ---------------- 68,46: he · she · it + V-s ----------------
    # sağ sütun satırları yer açmak için söner
    tb = S(Z["he"])
    for i in range(3):
        s.to("#row%d" % i, tb - 0.2, {"opacity": 0, "duration": 0.3, "ease": "power1.in"})
        s.to("#ok%d" % i, tb - 0.2, {"opacity": 0, "duration": 0.3, "ease": "power1.in"})
    CF, CX, CY = 120, 150.0, 400
    x = CX
    sepw = Y.genislik("Fredoka", 700, " · ", CF)
    for k, (ad, t) in enumerate((("he", Z["he"]), ("she", Z["she"]), ("it", Z["it"]))):
        pc = ([(" · ", IKN)] if k else []) + [(ad, KRE)]
        x0, W = s.yazi("g_%s" % ad, x, CY, pc, "Fredoka", 700, CF, S(t), 0.25, tur="tik", guc=0.55)
        x += W
    # + V-s
    tv = S(Z["vs"])
    pw = Y.genislik("Fredoka", 700, "  +  ", CF)
    vw = Y.genislik("Fredoka", 700, "V", CF)
    s.yazi("pls", x, CY, [("  +  ", IKN), ("V", KRE)], "Fredoka", 700, CF, tv, 0.3, tur="tik", guc=0.5)
    sx = x + pw + vw
    s.yazi("vss", sx, CY, [("-s", SAR)], "Fredoka", 700, CF, S(Z["vs_s"]), 0.2, tur="tik", guc=0.6)
    swd = Y.genislik("Fredoka", 700, "-s", CF)
    s.olay(S(Z["vs_s"]), "vurus", 0.8)
    s.yol("vsal", el_cizgi(sx - 4, CY + 22, sx + swd + 8, CY + 19), S(Z["vs_s"]) + 0.15, 0.3, SAR, 9, 0.85, "cizgi", 0.45)
    # ---------------- 72,55: I · you · we · they + go (s yok) ----------------
    DF, DY = 80, 540
    x = CX
    for k, (ad, t) in enumerate((("I", Z["diger"][0]), ("you", Z["diger"][1]), ("we", Z["diger"][2]),
                                 ("they", Z["diger"][3]))):
        pc = ([(" · ", IKN)] if k else []) + [(ad, IKN)]
        x0, W = s.yazi("d_%s" % ad, x, DY, pc, "Fredoka", 700, DF, S(t), 0.25, tur="tik", guc=0.45,
                       sar_ek='opacity="0.8"')
        x += W
    pw2 = Y.genislik("Fredoka", 700, "  +  ", DF)
    gw = Y.genislik("Fredoka", 700, "go", DF)
    s.yazi("d_go", x, DY, [("  +  ", IKN), ("go", IKN)], "Fredoka", 700, DF, S(Z["go"]), 0.25, tur="tik", guc=0.4,
           sar_ek='opacity="0.8"')
    gx = x + pw2 + gw
    s.yazi("d_s", gx + 4, DY, [("-s", SAR)], "Fredoka", 700, DF, S(Z["kirmizi"]) - 0.1, 0.15, tur=None,
           sar_ek='opacity="0.55"')
    sw2 = Y.genislik("Fredoka", 700, "-s", DF)
    s.yol("kir", el_cizgi(gx - 6, DY - 8, gx + sw2 + 18, DY - 40, 2), S(Z["kirmizi"]), 0.45, KIR, 8, 1, "cizgi", 0.7)
    s.yol("kir2", el_cizgi(gx + 2, DY - 42, gx + sw2 + 12, DY + 8, -2), S(Z["kirmizi"]) + 0.25, 0.3, KIR, 8, 1,
          "cizgi", 0.5)
    # ---------------- 76,38 / 77,74: olumsuz ve soru kartı (does) ----------------
    KX, KY, KW, KH = 140.0, 610, 860, 380
    tk = S(Z["kart"])
    s.yol("kart", el_kutu(KX, KY, KW, KH), S(69.4), 0.7, KRE, 4.2, 1, "cizgi", 0.6)   # iskelet erken: alt yarı boş kalmaz
    s.yazi("does", KX + 50, KY + 110, [("does", SAR)], "Fredoka", 700, 110, tk + 0.3, 0.35, tur="tik", guc=0.6)
    dw = Y.genislik("Fredoka", 700, "does", 110)
    s.yazi("dnot", KX + 50 + dw + 40, KY + 100, [("= yardımcı fiil", IKN)], "Caveat", 700, 56, tk + 0.6, 0.5,
           tur=None)
    # s ona geçer: büyük s'in kopyası does'a uçar
    ts = S(Z["s_gec"])
    s.svg.append('<g id="sdup"><text id="sd" x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" font-weight="700" '
                 'font-size="%d" style="opacity:0">s</text></g>' % (BXB, BYB, SAR, BIG))
    hx, hy = KX + 50 + dw - 24, KY + 110
    s.fromto("#sd", ts, {"opacity": 0, "scale": 1, "svgOrigin": "%.1f %.1f" % (BXB, BYB)},
             {"opacity": 1, "duration": 0.05})
    s.to("#sd", ts + 0.05, {"svgOrigin": "%.1f %.1f" % (BXB, BYB), "x": round(hx - BXB, 1), "y": round(hy - BYB, 1),
                            "scale": round(110 / BIG, 3), "duration": 0.55, "ease": "power3.inOut"})
    s.to("#sd", ts + 0.62, {"opacity": 0, "duration": 0.1})
    s.to("#does", ts + 0.6, {"svgOrigin": "%.1f %.1f" % (KX + 50 + dw / 2, KY + 70), "scale": 1.1, "duration": 0.18,
                             "ease": "power2.out"})
    s.to("#does", ts + 0.78, {"svgOrigin": "%.1f %.1f" % (KX + 50 + dw / 2, KY + 70), "scale": 1.0, "duration": 0.25,
                              "ease": "power2.inOut"})
    s.olay(ts + 0.6, "vurus", 0.8)
    s.to("#big", ts + 0.6, {"opacity": 0.4, "duration": 0.4})
    s.yol("sok", "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (BXB - 20, BYB - 20, BXB - 160, BYB + 20, hx + 260,
                                                                  hy - 70, hx + 90, hy - 40),
          ts + 0.05, 0.5, IKN, 3.6, 1, "cizgi", 0.45)
    s.to("#sok", ts + 0.75, {"opacity": 0, "duration": 0.25})
    # olumsuz / soru etiketleri (kutu içinde, satırın sağında)
    TF = 52
    s.yazi("tn", 840, KY + 232, [("olumsuz", IKN)], "Caveat", 700, TF, S(Z["olumsuz"]), 0.4, tur="tik", guc=0.45)
    s.yazi("ts", 840, KY + 332, [("soru", IKN)], "Caveat", 700, TF, S(Z["soru"]), 0.3, tur="tik", guc=0.45)
    # He does not go. / Does he go?
    LF2 = 72
    t1 = Z["he_does"]
    x = KX + 50
    kel1 = (("He", KRE, t1[0]), (" does", SAR, t1[1]), (" not", KRE, t1[2]), (" go.", KRE, t1[3]))
    for k, (m, fill, t) in enumerate(kel1):
        x0, W = s.yazi("hd%d" % k, x, KY + 232, [(m, fill)], "Fredoka", 700, LF2, S(t), 0.2,
                       tur="tik" if k == 1 else None, guc=0.5)
        x += W
    t2 = Z["does_he"]
    x = KX + 50
    for k, (m, fill, t) in enumerate((("Does", SAR, t2[0]), (" he", KRE, t2[1]), (" go?", KRE, t2[2]))):
        x0, W = s.yazi("dh%d" % k, x, KY + 332, [(m, fill)], "Fredoka", 700, LF2, S(t), 0.2,
                       tur="tik" if k == 0 else None, guc=0.5)
        x += W
    # ---------------- 83,68: Türkçe -er eki ; 85,60: git-er = go-es ----------------
    GX, GY = 1090.0, 640
    s.yazi("tr", GX, GY - 70, [("Türkçe: ", IKN)], "Caveat", 700, 56, S(Z["turkce"]), 0.4, tur="tik", guc=0.4)
    trw = Y.genislik("Caveat", 700, "Türkçe: ", 56)
    s.yazi("ter", GX + trw, GY - 70, [("-er eki", SAR)], "Caveat", 700, 56, S(Z["er"]), 0.35, tur="tik", guc=0.5)
    LF = 72
    gw1 = Y.genislik("Caveat", 700, "git-er", LF)
    s.yazi("gter", GX, GY + 10, [("git", KRE), ("-er", SAR)], "Caveat", 700, LF, S(Z["git_er"]), 0.5, tur="tik", guc=0.5)
    ex = GX + gw1 + 30
    te = S(Z["esit"])
    s.yol("es1", el_cizgi(ex, GY - 28, ex + 60, GY - 31, 1), te, 0.2, KRE, 5, 1, "cizgi", 0.5)
    s.yol("es2", el_cizgi(ex + 2, GY - 6, ex + 62, GY - 9, -1), te + 0.2, 0.2, KRE, 5, 1, "cizgi", 0.5)
    s.yazi("goes", ex + 96, GY + 10, [("go", KRE), ("-es", SAR)], "Caveat", 700, LF, S(Z["go_es"]), 0.5, tur="tik",
           guc=0.5)
    # ---------------- 87,75: formül kartı: always · usually · every day -> Simple Present ----------------
    FX, FY, FW, FH = 1090.0, 745, 740, 190
    tk2 = S(Z["kod"])
    s.yol("fkart", el_kutu(FX, FY, FW, FH), tk2, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    CF2 = 44
    x = FX + 36
    for k, (m, t) in enumerate((("always", Z["always"]), ("usually", Z["usually"]), ("every day", Z["every_day"]))):
        w = Y.genislik("Fredoka", 700, m, CF2)
        s.yazi("f%d" % k, x, FY + 82, [(m, KRE)], "Fredoka", 700, CF2, S(t), 0.25, tur="tik", guc=0.55)
        s.yol("ft%d" % k, el_tik(x + w + 10, FY + 70, 24), S(t) + 0.3, 0.2, SAR, 6, 0.9, "cizgi", 0.4)
        x += w + 10 + 24 + 36
    s.yol("fok", "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        FX + 80, FY + 108, FX + 120, FY + 110, FX + 150, FY + 112, FX + 200, FY + 110,
        FX + 184, FY + 98, FX + 200, FY + 110, FX + 184, FY + 124), S(Z["simple"]) - 0.5, 0.4, IKN, 4, 1, "cizgi", 0.5)
    s.yazi("fsp", FX + 224, FY + 148, [("Simple Present", SAR)], "Fredoka", 700, 62, S(Z["simple"]), 0.6, tur="tik",
           guc=0.6)
    s.olay(S(Z["present"]), "vurus", 0.8)
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
    return s, {"kun": kun, "bal_ids": bal_ids}


def html(s, parca):
    bal_ids = set(parca["bal_ids"])
    bal_html, diger = [], []
    for e in s.svg:
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

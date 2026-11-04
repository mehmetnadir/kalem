"""Sahne 06 (öğrenci sorusu + form) index.html + olay listesi üretici.
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
    # ---------------- konuşma balonu ----------------
    bal = ("M402 196 C520 182 700 190 880 184 C960 181 1030 186 1052 190 C1076 196 1082 222 1080 262 "
           "C1078 300 1082 332 1078 352 C1074 378 1056 386 1030 386 C900 392 760 384 640 388 "
           "C560 390 500 386 470 388 L330 470 L408 392 C384 388 366 380 364 352 C360 300 366 250 362 224 "
           "C360 204 380 198 402 196 Z")
    s.yol("bal", bal, 0.0, 0.5, KRE, 4.2, 1, "cizgi", 0.7)
    BF, BX = 44, 412
    sp = Y.genislik("Fredoka", 600, " ", BF)
    pos = {}
    for satir, (idx, base) in (("1", (range(0, 5), 258)), ("2", (range(5, 8), 328))):
        x = BX
        for i in idx:
            m, t = Z["balon_kelime"][i]
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(t), 0.12, tur="tik" if i in (3, 7) else None)
            pos[i] = (x, w, base)
            x += w + sp
    for i in (3, 7):   # fosforlu belirteç: -ing altı
        x, w, base = pos[i]
        s.yol("bm%d" % i, el_cizgi(x - 2, base + 12, x + w + 2, base + 9), S(Z["balon_kelime"][i][1]), 0.28,
              SAR, 8, 0.85, "cizgi", 0.5)
    # ---------------- sağ sütun: sitt-ing / tak-ing / climb-ing ----------------
    RF, RX, RY = 72, 1130.0, [330, 450, 570]
    stems = ["sitt", "tak", "climb"]
    sw = [Y.genislik("Fredoka", 700, m, RF) for m in stems]
    ingw = Y.genislik("Fredoka", 700, "-ing", RF)
    BIG = 180
    bigw = Y.genislik("Fredoka", 700, "-ing", BIG)
    BXB, BYB = 1500.0, 470.0
    for i in range(3):
        t = S(Z["satir_ing"][i])
        s.svg.append('<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
                     '<text id="stem%d" x="%.1f" y="%d" fill="%s">%s</text>'
                     '<text id="ri%d" x="%.1f" y="%d" fill="%s">-ing</text></g>'
                     % (i, RF, i, RX, RY[i], KRE, stems[i], i, RX + sw[i], RY[i], SAR))
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
    # ---------------- 72,72: toplanma ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    for i in range(3):   # kalemle oklar: kök sonundan büyük -ing'e
        x0, y0 = RX + sw[i] + 16, RY[i] - 24
        x1, y1 = BXB - 14, BYB - 62 + 6 * i
        s.yol("ok%d" % i, "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
            x0, y0, x0 + (x1 - x0) * 0.5, y0, x1 - 70, y1 - 4 * (i - 1), x1, y1),
            tf + 0.04 * i, 0.45, IKN, 3.5, 1, "cizgi", 0.45)
    for i in range(3):   # -ing parçaları büyük -ing'e uçar
        ox, oy = RX + sw[i], RY[i]
        ta = tf + 0.35 + 0.08 * i
        s.to("#ri%d" % i, ta, {"svgOrigin": "%.1f %d" % (ox, oy), "x": round(BXB - ox, 1), "y": round(BYB - oy, 1),
                               "scale": round(BIG / RF, 3), "duration": 0.55, "ease": "power3.inOut"})
        s.to("#ri%d" % i, ta + 0.5, {"opacity": 0, "duration": 0.08})
    tp = tf + 0.9
    s.svg.append('<g id="bigw"><text id="big" x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" font-weight="700" '
                 'font-size="%d" style="opacity:0">-ing</text></g>' % (BXB, BYB, SAR, BIG))
    s.fromto("#big", tp, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 62)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(tp, "vurus", 0.85)
    # in progress bandı
    s.yol("band", el_cizgi(BXB - 6, BYB + 58, BXB + bigw + 8, BYB + 54), tp + 0.4, 0.4, SAR, 9, 0.85, "cizgi", 0.55)
    ipx, ipw = s.yazi("ip", BXB - 30, BYB + 130, [("in progress", IKN)], "Caveat", 700, 52, tp + 0.9, 0.45,
                      tur="tik", guc=0.5)
    s.yol("ipok", "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        ipx + ipw + 14, BYB + 118, ipx + ipw + 50, BYB + 110, ipx + ipw + 74, BYB + 120, ipx + ipw + 98, BYB + 114,
        ipx + ipw + 84, BYB + 102, ipx + ipw + 98, BYB + 114, ipx + ipw + 82, BYB + 128),
        tp + 1.45, 0.4, IKN, 4, 1, "cizgi", 0.5)
    # balon ve baş birlikte küçülür, yukarı kayar, soluklaşır
    s.to("#balg", tf + 0.5, {"svgOrigin": "362 182", "x": 300, "y": -40, "scale": 0.55, "opacity": 0.45,
                             "duration": 0.8, "ease": "power3.inOut"})
    s.to("#bigw", tp + 0.5, {"svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 62), "scale": 1.025, "duration": 2.6,
                             "ease": "sine.inOut", "repeat": 6, "yoyo": True})
    # ---------------- be kolonu ----------------
    CF, CX = 96, 300.0
    tb = S(Z["be"])
    YB = {"be": 232, "am": 350, "is": 468, "are": 586, "was": 704}
    bx, bw = s.yazi("belb", CX, YB["be"], [("be", IKN)], "Fredoka", 700, CF, tb, 0.3)
    s.yol("beal", el_cizgi(CX - 4, YB["be"] + 18, CX + bw + 10, YB["be"] + 16), tb + 0.2, 0.35, SAR, 8, 0.85, "cizgi",
          0.45)
    for k in ("am", "is", "are"):
        s.yazi("c_" + k, CX, YB[k], [(k, KRE)], "Fredoka", 700, CF, S(Z[k]), 0.3, tur="tik", guc=0.55)
    tn = S(Z["now"])
    bx0, top, bot = CX + 230, 290, 600
    mid = (top + bot) // 2
    s.yol("kuma", "M%d %d C%d %d %d %d %d %d C%d %d %d %d %d %d C%d %d %d %d %d %d C%d %d %d %d %d %d" % (
        bx0, top, bx0 + 30, top + 10, bx0 + 16, top + 40, bx0 + 16, top + 90,
        bx0 + 16, mid - 40, bx0 + 30, mid - 14, bx0 + 50, mid,
        bx0 + 30, mid + 14, bx0 + 16, mid + 40, bx0 + 16, bot - 90,
        bx0 + 16, bot - 40, bx0 + 30, bot - 10, bx0, bot), tn, 0.5, IKN, 4, 1, "cizgi", 0.45)
    s.yazi("now", bx0 + 78, mid + 18, [("now", SAR)], "Caveat", 700, 56, tn + 0.25, 0.4, tur="tik", guc=0.5)
    # ---------------- was · were ----------------
    ww = Y.genislik("Fredoka", 700, "was", CF)
    dot = Y.genislik("Fredoka", 700, " · ", CF)
    wew = Y.genislik("Fredoka", 700, "were", CF)
    s.yazi("was", CX, YB["was"], [("was", IKN)], "Fredoka", 700, CF, S(Z["was"]), 0.2, tur="tik", guc=0.4,
           sar_ek='opacity="0.55"')
    s.yazi("dotw", CX + ww, YB["was"], [(" · ", IKN)], "Fredoka", 700, CF, S(Z["was"]) + 0.2, 0.1, tur=None,
           sar_ek='opacity="0.55"')
    s.yazi("were", CX + ww + dot, YB["was"], [("were", IKN)], "Fredoka", 700, CF, S(Z["were"]), 0.2, tur="tik",
           guc=0.4, sar_ek='opacity="0.55"')
    xe = CX + ww + dot + wew
    s.yazi("past", xe + 40, YB["was"] - 6, [("past", IKN)], "Caveat", 700, 56, S(Z["past"]), 0.4, tur="tik", guc=0.45)
    s.yol("kir", el_cizgi(CX - 14, YB["was"] - 24, xe + 14, YB["was"] - 40, 2), S(Z["cizgi_kirmizi"]), 0.45, KIR, 7,
          1, "cizgi", 0.7)
    # ---------------- -ing halka, koşu-yor = runn-ing ----------------
    th = S(Z["ing_halka"])
    s.yol("halka", el_daire(BXB + bigw / 2, BYB - 62, bigw / 2 + 34, 92, 1.0), th, 0.55, SAR, 7, 0.85, "parilti", 0.5)
    LX, LY, LF = 760.0, 860, 72
    ty = S(Z["yor"])
    kx, kw = s.yazi("kosu", LX, LY, [("koşu", KRE), ("-yor", SAR)], "Caveat", 700, LF, ty, 0.45)
    ex = LX + kw + 40
    te = S(Z["esit"])
    s.yol("es1", el_cizgi(ex, LY - 38, ex + 60, LY - 41, 1), te, 0.2, KRE, 5, 1, "cizgi", 0.5)
    s.yol("es2", el_cizgi(ex + 2, LY - 16, ex + 62, LY - 19, -1), te + 0.2, 0.2, KRE, 5, 1, "cizgi", 0.5)
    s.yazi("runn", ex + 100, LY, [("runn", KRE), ("-ing", SAR)], "Caveat", 700, LF, S(Z["runn"]), 0.45)
    # ---------------- formül kartı ----------------
    tk = S(Z["kart"])
    KX, KY, KW, KH = 950.0, 650, 900, 132
    s.yol("kart", el_kutu(KX, KY, KW, KH), tk, 0.55, KRE, 4.5, 1, "cizgi", 0.7)
    parc = [("am / is / are", KRE), ("  +  ", IKN), ("V", KRE), ("-ing", SAR)]
    tw = sum(Y.genislik("Fredoka", 700, p[0], 56) for p in parc)
    cx0 = KX + (KW - tw) / 2
    pa = Y.genislik("Fredoka", 700, parc[0][0], 56)
    pp = Y.genislik("Fredoka", 700, parc[1][0], 56)
    s.yazi("k1", cx0, KY + 82, [parc[0]], "Fredoka", 700, 56, tk + 0.1, 0.3, tur="tik", guc=0.5)
    s.yazi("k2", cx0 + pa, KY + 82, [parc[1]], "Fredoka", 700, 56, tk + 0.35, 0.15, tur=None)
    s.yazi("k3", cx0 + pa + pp, KY + 82, [parc[2], parc[3]], "Fredoka", 700, 56, tk + 0.5, 0.3, tur="tik", guc=0.6)
    s.olay(tk + 0.85, "vurus", 0.8)
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
    # figür ve balon grupları: balon parçaları balg içine taşınır
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

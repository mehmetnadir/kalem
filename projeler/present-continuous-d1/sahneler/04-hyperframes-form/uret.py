"""Sahne 04 D1 (dikey 1080x1920, HyperFrames, 582 kare, t_bas 34,94): cümle 6 (be kolonu, formül) + cümle 7 (kapanış).
Tek kaynak: zamanlar.json + sözcük zamanları (küresel sn) -> yerel sn = t - t_bas. Komut listesi veri olarak JS'e gömülür."""
import json
import math
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
R = Y.RENK
KRE, IKN, SAR, ZEM = R["murekkep"], R["ikincil"], R["vurgu"], R["zemin"]
TB = Z["t_bas"]
S_ = lambda t: round(t - TB, 4)  # noqa: E731


class Sahne:
    def __init__(self):
        self.defs, self.svg, self.cmd, self.ev = [], [], [], []

    def olay(self, t, tur, guc):
        self.ev.append({"kare": round(t * 30), "tur": tur, "guc": guc})

    def to(self, sel, t, v):
        self.cmd.append({"m": "to", "s": sel, "t": round(t, 4), "v": v})

    def fromto(self, sel, t, a, v):
        self.cmd.append({"m": "fromTo", "s": sel, "t": round(t, 4), "a": a, "v": v})

    def yol(self, id, d, t, sure, stroke=KRE, w=4.0, alfa=1.0, tur="cizgi", guc=0.55):
        self.svg.append('<path id="%s" d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
                        'stroke-linejoin="round" style="opacity:0"/>' % (id, d, stroke, w))
        self.cmd.append({"m": "draw", "id": id, "t": round(t, 4), "d": round(sure, 4), "a": alfa})
        if tur:
            self.olay(t, tur, guc)

    def yazi(self, id, x, y, parcalar, aile, agr, boy, t, d=0.12, tur="tik", guc=0.5, anchor="start"):
        ws = [Y.genislik(aile, agr, p[0], boy) for p in parcalar]
        W = sum(ws)
        x0 = x - W / 2 if anchor == "middle" else x
        cx, tx = x0, ""
        for (m, fill), w in zip(parcalar, ws):
            tx += '<text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">%s</text>' % (cx, y, fill, m)
            cx += w
        self.defs.append('<clipPath id="c_%s"><rect id="r_%s" x="%.1f" y="%.1f" width="0" height="%.1f"/></clipPath>'
                         % (id, id, x0 - 8, y - boy * 1.05, boy * 1.5))
        self.svg.append('<g id="%s" font-family="%s" font-weight="%d" font-size="%s" clip-path="url(#c_%s)">%s</g>'
                        % (id, aile, agr, boy, id, tx))
        self.cmd.append({"m": "rev", "id": "r_" + id, "t": round(t, 4), "d": d, "w": round(W + 20, 1)})
        if tur:
            self.olay(t, tur, guc)
        return x0, W

    def pop(self, id, x, y, parcalar, aile, agr, boy, t, d=0.35, tur="vurus", guc=0.85, anchor="middle"):
        """Ölçek 0,92->1 + alfa (formül / anahtar sözcük)."""
        ws = [Y.genislik(aile, agr, p[0], boy) for p in parcalar]
        W = sum(ws)
        x0 = x - W / 2 if anchor == "middle" else x
        cx, tx = x0, ""
        for (m, fill), w in zip(parcalar, ws):
            tx += '<text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">%s</text>' % (cx, y, fill, m)
            cx += w
        self.svg.append('<g id="%s" font-family="%s" font-weight="%d" font-size="%s" style="opacity:0">%s</g>'
                        % (id, aile, agr, boy, tx))
        self.fromto("#" + id, t, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (x0 + W / 2, y - boy * 0.35)},
                    {"opacity": 1, "scale": 1, "duration": d, "ease": "power3.out"})
        if tur:
            self.olay(t, tur, guc)
        return x0, W


def el_cizgi(x0, y0, x1, y1, egim=3.0):
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    return "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x0, y0, mx, my + egim * 2, x1, y1 + egim * 0.4)


def el_kutu(x, y, w, h):
    return ("M%.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f "
            "Q%.0f %.0f %.0f %.0f" % (x + 4, y + 3, x + w / 2, y - 3, x + w - 3, y + 1, x + w + 3, y + h / 2,
                                      x + w - 1, y + h - 2, x + w / 2, y + h + 4, x + 5, y + h + 1,
                                      x - 3, y + h / 2, x + 2, y + 6, x + 1, y + 2, x + 5, y + 2))


def uret():
    s = Sahne()
    # ---------- cümle 6 ----------
    # 35,50 "be": büyük anahtar sözcük + sarı alt çizgi
    bx, bw = s.yazi("belb", 90, 470, [("be", KRE)], "Fredoka", 700, 140, S_(35.5), 0.3, guc=0.55)
    s.yol("beal", el_cizgi(bx - 4, 492, bx + bw + 10, 488), S_(35.75), 0.35, SAR, 9, 0.85, "cizgi", 0.45)
    # 36,87 / 38,11 / 39,11 özne + am / is / are
    satir = [("I", "am", 36.87, 37.19, 650), ("He", "is", 38.11, 38.31, 800), ("We", "are", 39.11, 39.35, 950)]
    for i, (sb, fi, ts, tv, y) in enumerate(satir):
        s.yazi("sb%d" % i, 90, y, [(sb, IKN)], "Fredoka", 700, 76, S_(ts), 0.2, tur="tik", guc=0.4)
        vx, vw = s.yazi("fi%d" % i, 300, y, [(fi, KRE)], "Fredoka", 700, 116, S_(tv), 0.3, tur="tik", guc=0.55)
        s.yol("ua%d" % i, el_cizgi(vx - 4, y + 20, vx + vw + 8, y + 16), S_(tv) + 0.2, 0.3, SAR, 8, 0.85, "cizgi", 0.45)
    # 40,56 süslü ayraç + 41,36 now
    bx0, top, bot = 640, 560, 990
    mid = (top + bot) // 2
    s.yol("kuma", "M%d %d C%d %d %d %d %d %d C%d %d %d %d %d %d C%d %d %d %d %d %d C%d %d %d %d %d %d" % (
        bx0, top, bx0 + 30, top + 10, bx0 + 16, top + 40, bx0 + 16, top + 90,
        bx0 + 16, mid - 40, bx0 + 30, mid - 14, bx0 + 50, mid,
        bx0 + 30, mid + 14, bx0 + 16, mid + 40, bx0 + 16, bot - 90,
        bx0 + 16, bot - 40, bx0 + 30, bot - 10, bx0, bot), S_(40.56), 0.5, IKN, 4.5, 1, "cizgi", 0.45)
    s.yazi("now", bx0 + 90, mid + 28, [("now", SAR)], "Caveat", 700, 104, S_(41.36), 0.4, tur="tik", guc=0.5)
    # 42,79 formül kutusu: be + V-ing
    KX, KY, KW, KH = 90.0, 1040, 900.0, 150
    tk = S_(42.79)
    s.yol("kart", el_kutu(KX, KY, KW, KH), tk, 0.55, KRE, 4.5, 1, "cizgi", 0.7)
    parc = [("be", KRE), ("  +  ", IKN), ("V", KRE), ("-ing", SAR)]
    FS = 96
    ws = [Y.genislik("Fredoka", 700, p[0], FS) for p in parc]
    cx0 = KX + (KW - sum(ws)) / 2
    s.yazi("k1", cx0, KY + 103, [parc[0]], "Fredoka", 700, FS, tk + 0.1, 0.3, tur="tik", guc=0.5)
    s.yazi("k2", cx0 + ws[0], KY + 103, [parc[1]], "Fredoka", 700, FS, tk + 0.35, 0.15, tur=None)
    s.yazi("k3", cx0 + ws[0] + ws[1], KY + 103, [parc[2], parc[3]], "Fredoka", 700, FS, tk + 0.5, 0.3, tur="tik", guc=0.6)
    s.olay(tk + 0.85, "vurus", 0.8)
    # 44,15 in progress -> (-ing işin sürdüğünü gösterir)
    ipx, ipw = s.yazi("ip", 130, 1268, [("in progress", IKN)], "Caveat", 700, 70, S_(44.15), 0.5, tur="tik", guc=0.5)
    s.yol("ipok", "M%.1f 1250 C%.1f 1242 %.1f 1252 %.1f 1246 M%.1f 1234 L%.1f 1246 L%.1f 1260" % (
        ipx + ipw + 18, ipx + ipw + 56, ipx + ipw + 82, ipx + ipw + 106, ipx + ipw + 90, ipx + ipw + 106,
        ipx + ipw + 88), S_(44.9), 0.4, IKN, 4.5, 1, "cizgi", 0.5)
    g1_son = len(s.svg)
    # ---------- cümle 7: kapanış ----------
    # 45,55-46,15 önceki içerik küçülüp sol üste toplanır
    s.to("#g1", S_(45.5), {"svgOrigin": "90 360", "x": -30, "y": -60, "scale": 0.46, "duration": 0.6,
                          "ease": "power3.inOut"})
    s.olay(S_(45.5), "parilti", 0.5)
    # 47,17 -yor  = (iki kalem çizgisi, 47,65)  -ing (48,21): Fredoka 140, bant merkezi
    KF, KY2 = 140, 862
    wy = Y.genislik("Fredoka", 700, "-yor", KF)
    wi = Y.genislik("Fredoka", 700, "-ing", KF)
    gap, eqw = 44, 96
    tot = wy + gap + eqw + gap + wi
    x0 = 540 - tot / 2
    s.pop("ky", x0, KY2, [("-yor", SAR)], "Fredoka", 700, KF, S_(47.17), 0.35, "vurus", 0.85, anchor="start")
    ex = x0 + wy + gap
    s.yol("es1", el_cizgi(ex, KY2 - 66, ex + eqw, KY2 - 70, 1), S_(47.65), 0.22, KRE, 13, 1, "cizgi", 0.6)
    s.yol("es2", el_cizgi(ex + 2, KY2 - 30, ex + eqw + 2, KY2 - 34, -1), S_(47.65) + 0.22, 0.22, KRE, 13, 1, "cizgi", 0.6)
    s.pop("ki", ex + eqw + gap, KY2, [("-ing", SAR)], "Fredoka", 700, KF, S_(48.21), 0.35, "vurus", 0.9, anchor="start")
    s.yol("kal", el_cizgi(x0 - 6, KY2 + 34, x0 + tot + 8, KY2 + 28, 2), S_(48.75), 0.5, SAR, 10, 0.85, "cizgi", 0.55)
    # 49,48 Gidiyorum. / 50,77 I am going.
    s.yazi("gd", 540, 1010, [("Gidiyorum.", KRE)], "Caveat", 700, 104, S_(49.48), 0.55, tur="tik", guc=0.5, anchor="middle")
    s.yazi("ia", 540, 1130, [("I am go", KRE), ("ing", SAR), (".", KRE)], "Fredoka", 700, 84, S_(50.77), 0.8,
           tur="tik", guc=0.5, anchor="middle")
    s.olay(S_(51.8), "parilti", 0.5)
    return s, g1_son


def html(s, g1_son):
    kun = Y.kunye_svg("Form")
    govde = s.svg
    g1 = '<g id="g1">' + "".join(govde[:g1_son]) + "</g>"
    g2 = "".join(govde[g1_son:])
    lw = 48 * Y.LOGO_EN_BOY
    veri = {"cmd": sorted(s.cmd, key=lambda c: c["t"])}
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
{g1}
{g2}
{kun}
<image id="logo" href="assets/logo.svg" x="{48 - Y.LOGO_KAYMA * lw:.2f}" y="1464" width="{lw:.2f}" height="48"/>
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
    s, g = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(html(s, g))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

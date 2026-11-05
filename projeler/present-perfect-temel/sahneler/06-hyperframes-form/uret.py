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


def ok_yol(s, id, x0, y, uz, t, w=4.0, stroke=IKN, sure=0.3):
    """Sağa bakan kalem oku (gövde + iki kanat) tek yol."""
    x1 = x0 + uz
    s.yol(id, "M%.1f %.1f Q%.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        x0, y + 2, (x0 + x1) / 2, y - 3, x1, y, x1 - 14, y - 11, x1, y, x1 - 14, y + 11), t, sure, stroke, w, 1,
        "cizgi", 0.45)


def uret():
    s = Sahne()
    t0 = 0.42   # ilk 12 kare (0,4 sn) geçiş altında durgun: çizim 0,42'den başlar
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
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.04 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.04 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu ----------------
    bal = ("M402 196 C520 182 700 190 880 184 C960 181 1030 186 1052 190 C1076 196 1082 222 1080 262 "
           "C1078 300 1082 332 1078 352 C1074 378 1056 386 1030 386 C900 392 760 384 640 388 "
           "C560 390 500 386 470 388 L330 470 L408 392 C384 388 366 380 364 352 C360 300 366 250 362 224 "
           "C360 204 380 198 402 196 Z")
    s.yol("bal", bal, t0, 0.5, KRE, 4.2, 1, "cizgi", 0.7)
    BF, BX = 44, 412
    sp = Y.genislik("Fredoka", 600, " ", BF)
    pos = {}
    for idx, base in ((range(0, 5), 258), (range(5, 9), 328)):
        x = BX
        for i in idx:
            m, t = Z["balon_kelime"][i]
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(t), 0.12, tur="tik" if i in (3, 7) else None)
            pos[i] = (x, w, base)
            x += w + sp
    for i in (3, 7):   # fosforlu belirteç: have ve üçüncü altı
        x, w, base = pos[i]
        s.yol("bm%d" % i, el_cizgi(x - 2, base + 12, x + w + 2, base + 9), S(Z["balon_kelime"][i][1]), 0.28,
              SAR, 8, 0.85, "cizgi", 0.5)
    # ---------------- sağ sütun: broken / played / flown (V3 sarı) ----------------
    RF, RX, RY = 72, 1130.0, [330, 450, 570]
    fiil = ["broken", "played", "flown"]
    fw = [Y.genislik("Fredoka", 700, m, RF) for m in fiil]
    BIG = 180
    bigw = Y.genislik("Fredoka", 700, "V3", BIG)
    BXB, BYB = 1560.0, 440.0
    for i in range(3):
        t = S(Z["fiil_v3"][i])
        s.svg.append('<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
                     '<text x="%.1f" y="%d" fill="%s">%s</text></g>' % (i, RF, RX, RY[i], SAR, fiil[i]))
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
    # ---------------- 72,13: fiiller tek V3'e toplanır ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    for i in range(3):   # kalemle oklar: fiil sonundan büyük V3'e
        x0, y0 = RX + fw[i] + 16, RY[i] - 24
        x1, y1 = BXB - 14, BYB - 62 + 6 * i
        s.yol("ok%d" % i, "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
            x0, y0, x0 + (x1 - x0) * 0.5, y0, x1 - 70, y1 - 4 * (i - 1), x1, y1),
            tf + 0.04 * i, 0.45, IKN, 3.5, 1, "cizgi", 0.45)
    for i in range(3):   # fiiller V3'e uçar ve söner; oklar da söner
        ta = tf + 0.5 + 0.08 * i
        s.to("#row%d" % i, ta, {"x": round(BXB - RX, 1), "y": round(BYB - RY[i] - 40, 1), "scale": 0.5,
                                "svgOrigin": "%.1f %d" % (RX, RY[i]), "opacity": 0, "duration": 0.5,
                                "ease": "power3.inOut"})
        s.to("#ok%d" % i, ta + 0.1, {"opacity": 0, "duration": 0.25})
    tp = S(Z["v3"])
    s.svg.append('<g id="bigw"><text id="big" x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" font-weight="700" '
                 'font-size="%d" style="opacity:0">V3</text></g>' % (BXB, BYB, SAR, BIG))
    s.fromto("#big", tp, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 62)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(tp, "vurus", 0.85)
    s.yol("band", el_cizgi(BXB - 6, BYB + 40, BXB + bigw + 8, BYB + 36), tp + 0.4, 0.4, SAR, 9, 0.85, "cizgi", 0.55)
    NX = 1230.0
    s.yazi("n1", NX, BYB + 130, [("geçmişte bitti", IKN)], "Caveat", 700, 52, S(Z["bitti"]), 0.45, tur="tik",
           guc=0.5)
    ok_yol(s, "n2ok", NX, BYB + 188, 56, S(Z["etkisi"]) - 0.1, 4.0, IKN)
    s.yazi("n2", NX + 74, BYB + 200, [("etkisi şimdiye uzanıyor", SAR)], "Caveat", 700, 52, S(Z["etkisi"]), 0.5,
           tur="tik", guc=0.5)
    # balon ve baş birlikte küçülür, yukarı kayar, soluklaşır
    s.to("#balg", tf + 0.5, {"svgOrigin": "362 182", "x": 300, "y": -40, "scale": 0.55, "opacity": 0.45,
                             "duration": 0.8, "ease": "power3.inOut"})
    s.to("#bigw", tp + 0.5, {"svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 62), "scale": 1.025, "duration": 2.4,
                             "ease": "sine.inOut", "repeat": 7, "yoyo": True})
    # ---------------- sol sütun: kişi -> have / has ----------------
    HF, HX = 72, 140.0
    for k, (gen, kelime, y, t, id) in enumerate([
            ("I · you · we · they", "have", 410, Z["have_satir"], "ha"),
            ("he · she · it", "has", 520, Z["has_satir"], "hb")]):
        gw = Y.genislik("Fredoka", 700, gen, HF)
        ts = S(t)
        s.yazi(id + "g", HX, y, [(gen, KRE)], "Fredoka", 700, HF, ts, 0.4, tur="tik", guc=0.5)
        ok_yol(s, id + "o", HX + gw + 18, y - 26, 70, ts + 0.3, 5.0, IKN)
        s.yazi(id + "k", HX + gw + 18 + 70 + 18, y, [(kelime, SAR)], "Fredoka", 700, HF, ts + 0.45, 0.3, tur="tik",
               guc=0.55)
    s.yazi("sy", HX, 598, [("şimdiyi taşır", SAR)], "Caveat", 700, 56, S(Z["simdiyi"]), 0.5, tur="tik", guc=0.5)
    # ---------------- sinyal tablosu (el kutusu, 3 satır) ----------------
    tt = S(Z["tablo"])
    TX, TY, TW, TH = 140.0, 660, 1000, 270
    s.yol("tablo", el_kutu(TX, TY, TW, TH), tt, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    SF = 44
    satirlar = [("for · since", "süre", 82.0), ("never · ever", "deneyim", 84.6),
                ("just · already · yet", "yeni biten iş", 86.4)]
    L = max(Y.genislik("Fredoka", 700, a, SF) for a, _b, _t in satirlar)
    for i, (a, b, t) in enumerate(satirlar):
        y = TY + 78 + 78 * i
        ts = S(t)
        s.yazi("sg%d" % i, TX + 40, y, [(a, KRE)], "Fredoka", 700, SF, ts, 0.35, tur="tik", guc=0.55)
        ok_yol(s, "so%d" % i, TX + 40 + L + 20, y - 16, 64, ts + 0.3, 4.0, IKN)
        s.yazi("sb%d" % i, TX + 40 + L + 20 + 64 + 18, y, [(b, SAR)], "Fredoka", 700, SF, ts + 0.45, 0.35, tur=None)
    # ---------------- kod kartı: have / has + V3 ----------------
    tk = S(Z["kod"])
    KX, KY, KW, KH = 1270.0, 690, 580, 240
    s.yol("kart", el_kutu(KX, KY, KW, KH), tk, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
    CF = 52
    a1, a2, a3 = "have / has", "  +  ", "V3"
    w1, w2, w3 = (Y.genislik("Fredoka", 700, m, CF) for m in (a1, a2, a3))
    cx0 = KX + (KW - (w1 + w2 + w3)) / 2
    s.yazi("k1", cx0, KY + 92, [(a1, KRE)], "Fredoka", 700, CF, S(Z["k_have"]), 0.4, tur="tik", guc=0.5)
    s.yazi("k2", cx0 + w1, KY + 92, [(a2, IKN)], "Fredoka", 700, CF, S(Z["k_arti"]), 0.15, tur=None)
    s.yazi("k3", cx0 + w1 + w2, KY + 92, [(a3, SAR)], "Fredoka", 700, CF, S(Z["k_v3"]), 0.3, tur="tik", guc=0.6)
    s.olay(S(Z["k_v3"]) + 0.3, "vurus", 0.8)
    GF = 48
    g1, g3 = "geçmiş iş", "şimdiki etki"
    gw1, gw3 = (Y.genislik("Caveat", 700, m, GF + 4) for m in (g1, g3))
    gx = KX + (KW - (gw1 + gw3 + 70)) / 2
    s.yazi("g1", gx, KY + 190, [(g1, IKN)], "Caveat", 700, GF + 4, S(Z["k_gecmis"]), 0.4, tur="tik", guc=0.45)
    ok_yol(s, "gok", gx + gw1 + 8, KY + 176, 54, S(Z["k_ok"]), 4.0, IKN)
    s.yazi("g3", gx + gw1 + 70, KY + 190, [(g3, SAR)], "Caveat", 700, GF + 4, S(Z["k_etki"]), 0.45, tur="tik",
           guc=0.5)
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
    bal_ids = ["bal", "bas", "bm3", "bm7"] + ["bw%d" % i for i in range(9)]
    return s, {"kun": kun, "bal_ids": bal_ids}


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

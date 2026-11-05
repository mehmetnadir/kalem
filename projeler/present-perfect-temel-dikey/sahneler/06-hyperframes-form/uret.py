"""Sahne 06 DİKEY PRESENT PERFECT (HyperFrames 1080x1920, 860 kare, t_bas 67,19): cümle 6 (öğrenci balonu) + cümle 7 (form).
Yerleşim BRIEF-DIKEY §4. Tek kaynak: zamanlar.json (küresel sn) -> yerel sn = t - t_bas.
Komut listesi veri olarak JS'e gömülür; olaylar aynı çağrılardan toplanır (olay.py yalnız bu modülü içe alır)."""
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


def el_kutu(x, y, w, h):
    return ("M%.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f "
            "Q%.0f %.0f %.0f %.0f" % (x + 4, y + 3, x + w / 2, y - 3, x + w - 3, y + 1, x + w + 3, y + h / 2,
                                      x + w - 1, y + h - 2, x + w / 2, y + h + 4, x + 5, y + h + 1,
                                      x - 3, y + h / 2, x + 2, y + 6, x + 1, y + 2, x + 5, y + 2))


def ok_yol(s, id, x0, y, uz, t, w=5.0, stroke=IKN, sure=0.3):
    """Sağa bakan kalem oku (gövde + iki kanat) tek yol."""
    x1 = x0 + uz
    s.yol(id, "M%.1f %.1f Q%.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
        x0, y + 2, (x0 + x1) / 2, y - 4, x1, y, x1 - 18, y - 14, x1, y, x1 - 18, y + 14), t, sure, stroke, w, 1,
        "cizgi", 0.45)


def altyazi_parcalari():
    """altyazi.json (cümle 6-7): her parça için (t0, t1, satırlar, yazı boyu, satır aralığı).
    Kural (kunye.js altyaziCiz): yazı 44 -> 40 -> 36 küçülür, 2 satıra sığmazsa 3 satır (36 px, satır 44)."""
    kok = AD.parent.parent / "ortak" / "anlatim"
    parca = [p for p in json.loads((kok / "altyazi.json").read_text()) if p["cumle"] in (6, 7)]
    gen = 1080 - 96 - 12   # ölçüm payı (kerning yok)

    def sar(m, boy):
        out, cur = [], ""
        for w in m.split(" "):
            d = (cur + " " + w) if cur else w
            if Y.genislik("Lexend", 500, d, boy) > gen and cur:
                out.append(cur)
                cur = w
            else:
                cur = d
        out.append(cur)
        return out
    sonuc = []
    for p in parca:
        for boy in (44, 40, 36):
            sat = sar(p["metin"], boy)
            if len(sat) <= 2:
                break
        while len(sat) > 3:
            son = sat.pop()
            sat[2] += " " + son
        sonuc.append((p["t0"], p["t1"], sat, boy, 44 if len(sat) == 3 else 56))
    return sonuc


def uret():
    s = Sahne()
    t0 = 0.42   # ilk 12 kare geçiş altında durgun
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
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.04 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.04 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu (y 416-650) ----------------
    bal = ("M300 424 C420 414 700 422 1000 416 C1032 415 1048 428 1048 458 C1046 520 1050 580 1046 610 "
           "C1044 638 1026 648 998 648 C800 652 560 646 330 650 C304 651 288 638 288 610 L288 590 L232 562 "
           "L288 546 C286 502 290 466 288 454 C286 436 296 425 300 424 Z")
    s.yol("bal", bal, t0, 0.5, KRE, 4.4, 1, "cizgi", 0.7)
    BF, BX = 72, 330
    sp = Y.genislik("Caveat", 700, " ", BF)
    pos = {}
    for idx, base in ((range(0, 5), 506), (range(5, 9), 600)):
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
    # ---------------- evre 1: broken / played / flown (V3 sarı) ----------------
    RF, RX, RY = 120, 100.0, [850, 1010, 1170]
    fiil = ["broken", "played", "flown"]
    fw = [Y.genislik("Fredoka", 700, m, RF) for m in fiil]
    BIG = 210
    bigw = Y.genislik("Fredoka", 700, "V3", BIG)
    BXB, BYB = 650.0, 1040.0
    for i in range(3):
        t = S(Z["fiil_v3"][i])
        s.svg.append('<g id="row%d" style="opacity:0" font-family="Fredoka" font-weight="700" font-size="%d">'
                     '<text x="%.1f" y="%d" fill="%s">%s</text></g>' % (i, RF, RX, RY[i], SAR, fiil[i]))
        s.goster("#row%d" % i, t, 0.3, dx=30)
        s.olay(t, "tik", 0.5)
    # ---------------- evre 2 (72,13): fiiller tek V3'e toplanır ----------------
    tf = S(Z["form"])
    s.to("#ku-bolum", tf, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    for i in range(3):
        x0, y0 = RX + fw[i] + 16, RY[i] - 40
        x1, y1 = BXB - 16, BYB - 80 + 20 * i
        s.yol("ok%d" % i, "M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" % (
            x0, y0, x0 + (x1 - x0) * 0.5, y0, x1 - 40, y1 - 4 * (i - 1), x1, y1),
            tf + 0.04 * i, 0.45, IKN, 4.5, 1, "cizgi", 0.45)
    for i in range(3):
        ta = tf + 0.5 + 0.08 * i
        s.to("#row%d" % i, ta, {"x": round(BXB - RX, 1), "y": round(BYB - RY[i] - 60, 1), "scale": 0.5,
                                "svgOrigin": "%.1f %d" % (RX, RY[i]), "opacity": 0, "duration": 0.5,
                                "ease": "power3.inOut"})
        s.to("#ok%d" % i, ta + 0.1, {"opacity": 0, "duration": 0.25})
    tp = S(Z["v3"])
    s.svg.append('<g id="bigw"><text id="big" x="%.1f" y="%.1f" fill="%s" font-family="Fredoka" font-weight="700" '
                 'font-size="%d" style="opacity:0">V3</text></g>' % (BXB, BYB, SAR, BIG))
    s.fromto("#big", tp, {"opacity": 0, "scale": 0.92, "svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 80)},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "power3.out"})
    s.olay(tp, "vurus", 0.85)
    s.yol("band", el_cizgi(BXB - 6, BYB + 36, BXB + bigw + 8, BYB + 32), tp + 0.4, 0.4, SAR, 12, 0.85, "cizgi", 0.55)
    n1x, n1w = s.yazi("n1", 540, 1270, [("geçmişte bitti", KRE)], "Caveat", 700, 80, S(Z["bitti"]), 0.45,
                      anchor="middle", tur="tik", guc=0.5)
    n2w = Y.genislik("Caveat", 700, "etkisi şimdiye uzanıyor", 80)
    n2x = 540 - (n2w + 96) / 2
    ok_yol(s, "n2ok", n2x, 1346, 70, S(Z["etkisi"]) - 0.1, 6.0, IKN)
    s.yazi("n2", n2x + 96, 1360, [("etkisi şimdiye uzanıyor", SAR)], "Caveat", 700, 80, S(Z["etkisi"]), 0.5,
           tur="tik", guc=0.5)
    s.to("#balg", tf + 0.5, {"opacity": 0.55, "duration": 0.8, "ease": "power3.inOut"})
    s.to("#bigw", tp + 0.5, {"svgOrigin": "%.1f %.1f" % (BXB + bigw / 2, BYB - 80), "scale": 1.025, "duration": 1.3,
                             "ease": "sine.inOut", "repeat": 1, "yoyo": True})
    # ---------------- evre 3 (76,52): kişi -> have / has ----------------
    t3 = S(Z["have_satir"])
    for sel in ("#bigw", "#band", "#n1", "#n2", "#n2ok"):
        s.to(sel, t3 - 0.2, {"opacity": 0, "duration": 0.25, "ease": "power1.in"})
    ev3 = []
    for gen, kelime, yg, yk, t, id in (("I · you · we · they", "have", 780, 910, Z["have_satir"], "ha"),
                                       ("he · she · it", "has", 1010, 1140, Z["has_satir"], "hb")):
        ts = S(t)
        s.yazi(id + "g", 100, yg, [(gen, KRE)], "Fredoka", 700, 88, ts, 0.4, tur="tik", guc=0.5)
        ok_yol(s, id + "o", 100, yk - 40, 90, ts + 0.3, 7.0, IKN)
        s.yazi(id + "k", 230, yk, [(kelime, SAR)], "Fredoka", 700, 140, ts + 0.45, 0.3, tur="tik", guc=0.55)
        ev3 += ["#" + id + "g", "#" + id + "o", "#" + id + "k"]
    s.yazi("sy", 540, 1290, [("şimdiyi taşır", SAR)], "Caveat", 700, 88, S(Z["simdiyi"]), 0.5, anchor="middle",
           tur="tik", guc=0.5)
    ev3.append("#sy")
    # ---------------- evre 4 (81,63): sinyal tablosu, çerçeve ve ayraçlar baştan çizilir ----------------
    tt = S(Z["tablo"])
    for sel in ev3:
        s.to(sel, tt - 0.2, {"opacity": 0, "duration": 0.25, "ease": "power1.in"})
    TY, RH = 700, 215
    ev4 = ["#tablo", "#ay1", "#ay2"]
    s.yol("tablo", el_kutu(48, TY, 984, RH * 3), tt, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
    s.yol("ay1", el_cizgi(60, TY + RH, 1020, TY + RH, 2), tt + 0.45, 0.35, IKN, 3.5, 1, "cizgi", 0.4)
    s.yol("ay2", el_cizgi(60, TY + 2 * RH, 1020, TY + 2 * RH, 2), tt + 0.6, 0.35, IKN, 3.5, 1, "cizgi", 0.4)
    SF = 80
    for i, (a, b, t) in enumerate((("for · since", "süre", Z["satir1"]), ("never · ever", "deneyim", Z["satir2"]),
                                   ("just · already · yet", "yeni biten iş", Z["satir3"]))):
        top = TY + RH * i
        ts = S(t)
        s.yazi("sg%d" % i, 90, top + 90, [(a, KRE)], "Fredoka", 700, SF, ts, 0.4, tur="tik", guc=0.55)
        ok_yol(s, "so%d" % i, 90, top + 150, 90, ts + 0.3, 7.0, IKN)
        s.yazi("sb%d" % i, 210, top + 184, [(b, SAR)], "Fredoka", 700, SF, ts + 0.45, 0.35, tur=None)
        ev4 += ["#sg%d" % i, "#so%d" % i, "#sb%d" % i]
    # ---------------- evre 5 (88,98): kod kartı ----------------
    tk = S(Z["kod"])
    for sel in ev4:
        s.to(sel, tk - 0.2, {"opacity": 0, "duration": 0.25, "ease": "power1.in"})
    s.yol("kart", el_kutu(48, 700, 984, 540), tk, 0.6, KRE, 5, 1, "cizgi", 0.7)
    CF = 140
    s.yazi("k1", 540, 880, [("have / has", KRE)], "Fredoka", 700, CF, S(Z["k_have"]), 0.4, anchor="middle",
           tur="tik", guc=0.5)
    w2 = Y.genislik("Fredoka", 700, "+  V3", 150)
    s.yazi("k2", 540, 1050, [("+  ", IKN), ("V3", SAR)], "Fredoka", 700, 150, S(Z["k_arti"]), 0.4, anchor="middle",
           tur="tik", guc=0.6)
    s.olay(S(Z["k_v3"]) + 0.2, "vurus", 0.8)
    g1w = Y.genislik("Caveat", 700, "geçmiş iş", 72)
    g3w = Y.genislik("Caveat", 700, "şimdiki etki", 72)
    gx = 540 - (g1w + g3w + 96) / 2
    s.yazi("g1", gx, 1170, [("geçmiş iş", KRE)], "Caveat", 700, 72, S(Z["k_gecmis"]), 0.4, tur="tik", guc=0.45)
    ok_yol(s, "gok", gx + g1w + 12, 1152, 70, S(Z["k_ok"]), 6.0, IKN)
    s.yazi("g3", gx + g1w + 96, 1170, [("şimdiki etki", SAR)], "Caveat", 700, 72, S(Z["k_etki"]), 0.45, tur="tik",
           guc=0.5)
    nw = Y.genislik("Caveat", 700, "Next lesson", 72)
    nx = 980 - nw - 86
    s.yazi("nx", nx, 1350, [("Next lesson", IKN)], "Caveat", 700, 72, S(Z["sonraki"]), 0.4, tur="tik", guc=0.4)
    ok_yol(s, "nxok", 980 - 70, 1334, 70, S(Z["sonraki"]) + 0.35, 6.0, IKN, 0.25)
    # ---------------- altyazı parçaları (opaklık anahtarları) ----------------
    dil = altyazi_parcalari()
    s.altyazi = dil

    def aktif(t):
        k = -1
        for i, (t0_, t1, _sat, _b, _a) in enumerate(dil):
            if t0_ - 0.05 <= t < t1 + 0.35:
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
    bal_ids = ["bal", "bas", "bm3", "bm7"] + ["bw%d" % i for i in range(9)]
    return s, {"kun": kun, "bal_ids": bal_ids}


def html(s, parca):
    bal_ids = set(parca["bal_ids"])
    bal_html, diger = [], []
    for e in s.svg:
        idn = e.split('id="', 1)[1].split('"', 1)[0]
        (bal_html if idn in bal_ids else diger).append(e)
    veri = {"cmd": sorted(s.cmd, key=lambda c: c["t"])}
    alt = "".join('<div id="alt%d" class="alt" style="font-size:%dpx;line-height:%dpx"><div>%s</div></div>' % (
        i, boy, ara, "<br>".join('<span style="white-space:nowrap">%s</span>' % sa for sa in sat))
        for i, (_a, _b, sat, boy, ara) in enumerate(s.altyazi))
    lw = 96 * Y.LOGO_EN_BOY
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
.alt{{position:absolute;left:48px;top:1400px;width:984px;height:136px;display:flex;align-items:center;
justify-content:center;text-align:center;font-family:Lexend,sans-serif;font-weight:500;color:var(--murekkep,#f3efe6);opacity:0;}}
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

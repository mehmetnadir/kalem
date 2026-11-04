"""Sahne 01 (dikey 1080x1920) index.html üretici: soğuk açılış kapağı, 3 sn içerik + 12 kare geçiş payı = 102 kare.
HUD v2 (BRIEF-DIKEY §2): logo sol üst 387x96, ders adı 56, rozet hapı 72, çip 80, altyazı bandı 1400-1536.
Başlık `SIMPLE` / `PAST` kalemle çizilir (210 px); 2,0-3,0 sn'de künye ders adına küçülür, cümle yukarı kayar."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
R = Y.RENK
BASLIK_BOY = 210
SOL = 48
T1_Y, T2_Y = 540, 750
CUMLE_BOY, CUMLE_X = 80, 56
CUMLE_Y = (850, 940)          # iki satır (taban); sahne 02'de y 450 / 540'a oturur
CUMLE_HEDEF_DY = -400
LOGO_H = Y.LOGO_YUK
LOGO_W = LOGO_H * Y.LOGO_EN_BOY
LOGO_BX, LOGO_BY = 48 - Y.LOGO_KAYMA * LOGO_W, 48.0
FIG_S, FIG_X, FIG_Y = 0.6, 240.0, 960.0
TV_S, TV_X, TV_Y = 14.0, 500.0, 1040.0
_SOZ = json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
SOZ = [w for w in _SOZ if w["cumle"] == 1]
ALT = [a for a in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "altyazi.json").read_text())
       if a["cumle"] == 1]


def yapi():
    gf, hf, fig = Y.peeps("standing-3", 60)
    tv = Y.tabler("device-tv")
    t0, t1 = Z["figur"][0], Z["figur"][0] + Z["figur"][1]
    fz = Y.cizgi_zamanlari([s["uz"] for s in fig], t0, t1)
    tz = Y.cizgi_zamanlari([70.0, 25.0], Z["tv"][0], Z["tv"][0] + Z["tv"][1])
    return fig, tv, fz, tz


def uret():
    fig, tv, fz, tz = yapi()
    sw = 4.4
    figs = "".join('<path id="f%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                   % (i, s["tx"], s["ty"], s["d"]) for i, s in enumerate(fig))
    tvs = "".join('<path id="k%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(tv))
    rw0 = Y.rozet_genislik("YDT · BASIC")
    gw = Y.rozet_genislik("GRAMMAR")
    gx = Y.ROZET_X + rw0 + 16
    roz = ('<g id="rz1" style="opacity:0"><rect x="%.1f" y="%d" width="%.1f" height="%d" rx="36" fill="%s"/>'
           '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" '
           'fill="%s">GRAMMAR</text></g>'
           % (gx, Y.ROZET_Y, gw, Y.ROZET_H, R["murekkep"], gx + gw / 2, Y.ROZET_Y + Y.ROZET_H / 2 + 13,
              R["zemin"]))
    bs = ('font-family="Fredoka" font-weight="700" font-size="%d" stroke="%s" stroke-width="12" '
          'stroke-linejoin="round" style="paint-order:stroke fill"' % (BASLIK_BOY, R["zemin"]))
    tit = ('<text id="t1" x="%d" y="%d" fill="%s" clip-path="url(#cp1)" %s>SIMPLE</text>'
           '<text id="t2" x="%d" y="%d" fill="%s" clip-path="url(#cp2)" %s>PAST</text>'
           % (SOL, T1_Y, R["murekkep"], bs, SOL, T2_Y, R["logoSari"], bs))
    tw1 = Y.genislik("Fredoka", 700, "SIMPLE", BASLIK_BOY) + 24
    tw2 = Y.genislik("Fredoka", 700, "PAST", BASLIK_BOY) + 24
    # cümle 1: iki satır ("Dün akşam amcamlara" / "gittim."), her satırın kırpması konuşmayla açılır
    sat = [SOZ[:3], SOZ[3:]]
    cw = []
    for si, ws in enumerate(sat):
        for i, w in enumerate(ws):
            metin = " ".join(x["sozcuk"] for x in ws[:i + 1])
            cw.append([si, w["t0"], min(w["t1"], w["t0"] + 0.5),
                       Y.genislik("Caveat", 700, metin, CUMLE_BOY) + 8])
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                    % (n, n, SOL - 12, y - BASLIK_BOY + 8, int(BASLIK_BOY * 1.35))
                    for n, y in ((1, T1_Y), (2, T2_Y)))
    cum = ""
    for si, ws in enumerate(sat):
        clips += ('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                  % (3 + si, 3 + si, CUMLE_X - 12, CUMLE_Y[si] - CUMLE_BOY, int(CUMLE_BOY * 1.5)))
        cum += ('<text id="cm%d" x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" '
                'fill="%s" clip-path="url(#cp%d)">%s</text>'
                % (si, CUMLE_X, CUMLE_Y[si], CUMLE_BOY, R["murekkep"], 3 + si,
                   " ".join(x["sozcuk"] for x in ws)))
    cum = '<g id="cum">%s</g>' % cum
    ders_w = Y.genislik("Fredoka", 700, "SIMPLE ", 56)
    hedef = {"t1": [48, Y.DERS_TABAN, 56 / BASLIK_BOY],
             "t2": [48 + ders_w, Y.DERS_TABAN, 56 / BASLIK_BOY]}
    kunye = Y.kunye_svg("Hook")
    alt = Y.altyazi_svg(ALT)
    veri = {"Z": Z, "fz": fz, "tz": tz, "nF": len(fig), "nK": len(tv), "hedef": hedef,
            "sol": SOL, "t1y": T1_Y, "t2y": T2_Y, "tw": [tw1, tw2], "cw": cw, "cx": CUMLE_X,
            "logo": [LOGO_BX, LOGO_BY, LOGO_W, LOGO_H], "cdy": CUMLE_HEDEF_DY,
            "alt": [[a["t0"] - 0.05, a["t1"] + 0.35] for a in ALT]}
    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>{clips}<filter id="el" x="-5%" y="-5%" width="110%" height="110%">
<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="5" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="3.2"/></filter></defs>
<g id="eskiz" fill="none" stroke="{R['murekkep']}" stroke-linecap="round" stroke-linejoin="round">
<g id="fig" transform="translate({FIG_X} {FIG_Y}) scale({FIG_S})" stroke-width="{sw / FIG_S:.3f}">{figs}</g>
<g id="tv" filter="url(#el)"><g transform="translate({TV_X} {TV_Y}) rotate(-4 168 168) scale({TV_S})" stroke-width="{4.4 / TV_S:.3f}">{tvs}</g></g>
</g>
{roz}{tit}{cum}
<g id="logo"><g id="lgs" style="opacity:0"><image id="logoimg" href="assets/logo.svg" x="{LOGO_BX:.2f}" y="{LOGO_BY}" width="{LOGO_W:.2f}" height="{LOGO_H}"/></g></g>
{kunye}{alt}
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var V = {json.dumps(veri)};
  var Z = V.Z, $ = function (s) {{ return document.querySelector(s); }};
  var tl = gsap.timeline({{ paused: true }});
  function ac(o) {{ o.immediateRender = false; return o; }}
  function darbe(id, bas, sure) {{
    var p = $("#" + id), L = p.getTotalLength();
    p.style.strokeDasharray = L + " " + (L + 2); p.style.strokeDashoffset = L;
    tl.set(p, ac({{ opacity: 1 }}), bas);
    tl.to(p, ac({{ strokeDashoffset: 0, duration: sure, ease: "none" }}), bas);
  }}
  for (var i = 0; i < V.nF; i++) darbe("f" + i, V.fz[i][0], V.fz[i][1]);
  for (var j = 0; j < V.nK; j++) darbe("k" + j, V.tz[j][0], V.tz[j][1]);
  gsap.set("#ku-ders,#ku-bolum,#ku-rz", {{ opacity: 0 }});

  // altyazı bandı: konuşulan parça (cümle 1) süresince görünür
  V.alt.forEach(function (a, i) {{ tl.set("#ay" + i, ac({{ opacity: 1 }}), a[0]); }});

  // 0,0-0,4 logo damgası HUD'da (sol üst): ölçek 1,18->1,0 + dönme -2 -> 0, alfa 0->1
  var lg = V.logo, bx = lg[0], by = lg[1], bw = lg[2], bh = lg[3];
  gsap.set("#lgs", {{ svgOrigin: (bx + bw / 2) + " " + (by + bh / 2) }});
  tl.fromTo("#lgs", {{ opacity: 0, scale: 1.18, rotation: -2 }},
    {{ opacity: 1, scale: 1, rotation: 0, duration: Z.logo_damga[1], ease: "power3.out", immediateRender: false }}, Z.logo_damga[0]);

  // 0,3-0,9 rozetler: künye hapı + GRAMMAR
  tl.fromTo("#ku-rz", {{ y: 26, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.rozet[0]);
  tl.fromTo("#rz1", {{ y: 26, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.rozet[0] + Z.rozet[1]);
  // 0,65-1,45 başlık kalemle çizilir (kırpma soldan açılır)
  [0, 1].forEach(function (i) {{
    tl.fromTo("#cr" + (i + 1), {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.tw[i] }}, duration: Z.baslik[i][1], ease: "none", immediateRender: false }}, Z.baslik[i][0]);
  }});
  // 1,0- cümle 1 konuşmayla yazılır (iki satır, sözcük sözcük)
  var onceki = [0, 0];
  V.cw.forEach(function (w) {{
    var s = w[0], hedef = w[3] + 4;
    tl.fromTo("#cr" + (3 + s), {{ attr: {{ width: onceki[s] }} }}, {{ attr: {{ width: hedef }}, duration: w[2] - w[1], ease: "none", immediateRender: false }}, w[1]);
    onceki[s] = hedef;
  }});

  gsap.set("#eskiz", {{ svgOrigin: "540 1200" }});
  // 2,0-3,0 uçuş: başlık künye ders adına küçülür, cümle yukarı kayar (sahne 02'deki yerine), eskiz + GRAMMAR söner
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud, H = V.hedef;
  function uc2(id, ox, oy, h, ex) {{
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, x: h[0] - ox, duration: ud, ease: ex }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, y: h[1] - oy, duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, scale: h[2], duration: ud * 0.8, ease: "power3.out" }}), u0);
  }}
  uc2("#t1", V.sol, V.t1y, H.t1, "power3.inOut"); uc2("#t2", V.sol, V.t2y, H.t2, "power2.out");
  tl.to("#t2", ac({{ fill: "{R['murekkep']}", duration: ud * 0.6, ease: "power1.inOut" }}), u0);
  tl.to("#rz1", ac({{ opacity: 0, duration: 0.3, ease: "power1.in" }}), u0);
  tl.to("#cum", ac({{ y: V.cdy, duration: ud, ease: "power3.inOut" }}), u0);
  tl.to("#eskiz", ac({{ opacity: 0, scale: 1.06, duration: 0.45, ease: "power1.in" }}), u0 + 0.1);
  var son = u1 - 0.25;
  ["#t1", "#t2"].forEach(function (s) {{ tl.to(s, ac({{ opacity: 0, duration: 0.25, ease: "power1.in" }}), son); }});
  tl.to("#ku-ders,#ku-bolum", ac({{ opacity: 1, duration: 0.25, ease: "power1.out" }}), son);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, fig, tv, fz, tz


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    html, *_ = uret()
    (AD / "proje" / "index.html").write_text(html)
    print("index.html yazıldı", len(html))

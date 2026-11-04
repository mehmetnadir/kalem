"""Sahne 01 kapak index.html üretici (DİKEY 1080x1920; soğuk açılış, 3 sn içerik + 12 kare geçiş = 102 kare).
Zamanlar: zamanlar.json (olay.py ile ortak); cümle 1 sözcük zamanları: ortak/anlatim/sozcukler.json.
Kapak kalıbı: başlık `BU AKŞAM` / `= I AM GOING` kalemle çizilir, figür + ev eskizi, Caveat cümle konuşmayla
yazılır, 2,0-3,0 sn'de başlık HUD çipine uçar, cümleler içerik bandının üstüne çıkar, eskiz solar."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
SOZ = [w for w in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == 1]
TR = SOZ[:3]            # Bu akşam gidiyorum.
R = Y.RENK
CIP = "BU AKŞAM = I AM GOING"
SOL = 72
BASLIK_BOY = 150
T1_Y = 466
T2_Y = T1_Y + 165
CUMLE1_Y, CUMLE2_Y, CUMLE_BOY = 745, 820, 64
KAYMA_Y = -315                      # uçuşta cümleler: 745/820 -> 430/505
FIG_S, FIG_X, FIG_Y = 0.67, 150.0, 874.0
EV_S, EV_X, EV_Y = 15.0, 560.0, 984.0
CAP = 0.36                          # cümle yazımı sözcük başına en çok 0,36 sn (kapak karesi 1,95 tam olsun)


def yapi():
    gf, hf, fig = Y.peeps("standing-3", 60)
    ev = Y.tabler("home")
    fz = Y.cizgi_zamanlari([s["uz"] for s in fig], Z["figur"][0], Z["figur"][0] + Z["figur"][1])
    ez = Y.cizgi_zamanlari([40.0, 30.0, 20.0], Z["ev"][0], Z["ev"][0] + Z["ev"][1])
    return fig, ev, fz, ez


def uret():
    fig, ev, fz, ez = yapi()
    sw = 3.5
    figs = "".join('<path id="f%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                   % (i, s["tx"], s["ty"], s["d"]) for i, s in enumerate(fig))
    evs = "".join('<path id="k%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(ev))
    bs = 'font-family="Fredoka" font-weight="700" font-size="%d" stroke="%s" stroke-width="10" ' \
         'stroke-linejoin="round" style="paint-order:stroke fill"' % (BASLIK_BOY, R["zemin"])
    tit = ('<text id="t1" x="%d" y="%d" fill="%s" clip-path="url(#cp1)" %s>BU AKŞAM</text>'
           '<text id="t2" x="%d" y="%d" fill="%s" clip-path="url(#cp2)" %s>= I AM GOING</text>'
           % (SOL, T1_Y, R["murekkep"], bs, SOL, T2_Y, R["logoSari"], bs))
    tw1 = Y.genislik("Fredoka", 700, "BU AKŞAM", BASLIK_BOY) * 1.15 + 40   # ölçüm kerning/Ş farkı payı
    tw2 = Y.genislik("Fredoka", 700, "= I AM GOING", BASLIK_BOY) * 1.15 + 40
    tr_metin = " ".join(w["sozcuk"] for w in TR)
    cum_x = [SOL + Y.genislik("Caveat", 700, " ".join(w["sozcuk"] for w in TR[:i + 1]), CUMLE_BOY) + 8
             for i in range(len(TR))]
    en_w = Y.genislik("Caveat", 700, "I am going tonight.", CUMLE_BOY) + 24
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                    % (n, n, SOL - 12, y - BASLIK_BOY + 8, int(BASLIK_BOY * 1.35))
                    for n, y in ((1, T1_Y), (2, T2_Y)))
    for n, y in ((3, CUMLE1_Y), (4, CUMLE2_Y)):
        clips += ('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                  % (n, n, SOL - 12, y - CUMLE_BOY, int(CUMLE_BOY * 1.5)))
    cum = ('<g id="cum"><text id="cm1" x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" '
           'fill="%s" clip-path="url(#cp3)">%s</text>'
           '<text id="cm2" x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" '
           'fill="%s" clip-path="url(#cp4)">I am going tonight.</text></g>'
           % (SOL, CUMLE1_Y, CUMLE_BOY, R["murekkep"], tr_metin, SOL, CUMLE2_Y, CUMLE_BOY, R["murekkep"]))
    # uçuş hedefleri: çip metninin iki parçası (Lexend 26)
    cx, cy, cw, ch = Y.cip_olcu(CIP)
    base = cy + ch / 2 + 9.3
    x0 = cx + 22
    w_bu = Y.genislik("Lexend", 700, "BU AKŞAM ", Y.HUD["cipYazi"])
    k = Y.HUD["cipYazi"] / BASLIK_BOY
    hedef = {"t1": [x0, base, k], "t2": [x0 + w_bu, base, k]}
    kunye = Y.kunye_svg(CIP)
    veri = {"Z": Z, "fz": fz, "ez": ez, "nF": len(fig), "nE": len(ev), "hedef": hedef,
            "sol": SOL, "t1y": T1_Y, "t2y": T2_Y, "tw": [tw1, tw2], "enw": en_w, "kayma": KAYMA_Y,
            "logoc": "%.2f %.2f" % (Y.HUD["kenar"] + Y.HUD["logoYuk"] * Y.LOGO_EN_BOY / 2, Y.HUD["logoY"] + Y.HUD["logoYuk"] / 2),
            "cw": [[w["t0"], min(w["t1"], w["t0"] + CAP), cum_x[i]] for i, w in enumerate(TR)]}
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
<g id="evg" filter="url(#el)"><g transform="translate({EV_X} {EV_Y}) scale({EV_S})" stroke-width="{sw / EV_S:.3f}">{evs}</g></g>
<g id="par" stroke="{R['vurgu']}" stroke-width="5" style="opacity:0">
<path d="M470 1010 l0 -40 M450 990 l40 0 M458 978 l24 24 M482 978 l-24 24"/>
<path d="M980 1090 l0 -34 M963 1073 l34 0"/><path d="M520 1300 l0 -30 M505 1285 l30 0"/></g>
</g>
{tit}{cum}
{kunye}
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
  for (var j = 0; j < V.nE; j++) darbe("k" + j, V.ez[j][0], V.ez[j][1]);
  gsap.set("#ku-cip", {{ opacity: 0 }});
  gsap.set("#ku-cipt", {{ opacity: 0 }});

  // ders adı + logo damgası + rozetler
  tl.fromTo("#ku-ders", {{ opacity: 0 }}, {{ opacity: 1, duration: Z.ders[1], ease: "power1.out", immediateRender: false }}, Z.ders[0]);
  gsap.set("#ku-logo", {{ svgOrigin: V.logoc }});
  tl.fromTo("#ku-logo", {{ opacity: 0, scale: 1.18, rotation: -2 }},
    {{ opacity: 1, scale: 1, rotation: 0, duration: Z.logo_damga[1], ease: "power3.out", immediateRender: false }}, Z.logo_damga[0]);
  [0, 1].forEach(function (i) {{
    tl.fromTo("#rz" + i, {{ y: 26, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.rozet[0] + i * Z.rozet[1]);
  }});
  // başlık kalemle çizilir (kırpma soldan sağa)
  [0, 1].forEach(function (i) {{
    tl.fromTo("#cr" + (i + 1), {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.tw[i] }}, duration: Z.baslik[i][1], ease: "none", immediateRender: false }}, Z.baslik[i][0]);
  }});
  // Türkçe cümle konuşmayla yazılır
  var onceki = 0;
  V.cw.forEach(function (w) {{
    tl.fromTo("#cr3", {{ attr: {{ width: onceki }} }}, {{ attr: {{ width: w[2] - V.sol + 12 }}, duration: w[1] - w[0], ease: "none", immediateRender: false }}, w[0]);
    onceki = w[2] - V.sol + 12;
  }});
  // İngilizce cümle altında
  tl.fromTo("#cr4", {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.enw }}, duration: Z.en_cumle[1], ease: "none", immediateRender: false }}, Z.en_cumle[0]);

  gsap.set("#eskiz", {{ svgOrigin: "540 1100" }});

  // uçuş 2,0-3,0: başlık -> çip, cümleler yukarı, eskiz solar
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud, H = V.hedef;
  function uc2(id, ox, oy, h, ex) {{
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, x: h[0] - ox, duration: ud, ease: ex }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, y: h[1] - oy, duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, scale: h[2], duration: ud * 0.8, ease: "power3.out" }}), u0);
  }}
  uc2("#t1", V.sol, V.t1y, H.t1, "power3.inOut"); uc2("#t2", V.sol, V.t2y, H.t2, "power2.out");
  tl.to("#t2", ac({{ fill: "{R['murekkep']}", duration: ud * 0.6, ease: "power1.inOut" }}), u0);
  tl.to("#cum", ac({{ y: V.kayma, duration: ud, ease: "power3.inOut" }}), u0);
  tl.to("#eskiz", ac({{ opacity: 0, scale: 1.06, duration: 0.4, ease: "power1.in" }}), u0 + 0.1);
  tl.fromTo("#par", {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.2, ease: "power3.out", immediateRender: false, svgOrigin: "540 1100" }}, u0);
  tl.to("#par", ac({{ opacity: 0, duration: 0.3, ease: "power1.in" }}), u0 + 0.25);
  tl.to("#ku-cip", ac({{ opacity: 1, duration: 0.35, ease: "power1.out" }}), u0 + 0.35);
  var son = u1 - 0.3;   // çip metni son 0,25 sn'de belirir, başlık satırları söner
  ["#t1", "#t2"].forEach(function (s) {{ tl.to(s, ac({{ opacity: 0, duration: 0.15, ease: "power1.in" }}), son); }});
  tl.to("#ku-cipt", ac({{ opacity: 1, duration: 0.2, ease: "power1.out" }}), son + 0.1);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, fig, ev, fz, ez


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    html, *_ = uret()
    (AD / "proje" / "index.html").write_text(html)
    print("index.html yazıldı", len(html))

"""Sahne 01 D1 (dikey 1080x1920) index.html üretici: soğuk açılış kapağı, 3 sn içerik + 12 kare geçiş payı = 102 kare.
Zamanlar: zamanlar.json (olay.py ile ortak). Rozet HUD'da, başlık y 346-768, figür + ev y 880-1340, logo alt sol.
Başlık `-YOR` / `= -ING` kalemle çizilir; 2,0-3,0 sn'de künyeye uçar."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
R = Y.RENK
BASLIK_BOY = 230
SOL = 64
T1_Y, T2_Y = 530, 730
CUMLE_Y, CUMLE_BOY = 850, 110
LOGO_H = 48
LOGO_W = LOGO_H * Y.LOGO_EN_BOY
LOGO_BX, LOGO_BY = 48 - Y.LOGO_KAYMA * LOGO_W, 1464.0
FIG_S, FIG_X, FIG_Y = 0.66, 130.0, 880.0
EV_S, EV_X, EV_Y = 11.0, 560.0, 1020.0
SOZ = [w for w in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == 1]


def yapi():
    gf, hf, fig = Y.peeps("standing-3", 60)
    ev = Y.tabler("home")
    fz = Y.cizgi_zamanlari([s["uz"] for s in fig], Z["figur"][0], Z["figur"][0] + Z["figur"][1])
    ez = Y.cizgi_zamanlari([40.0] * len(ev), Z["ev"][0], Z["ev"][0] + Z["ev"][1])
    return fig, ev, fz, ez


def uret():
    fig, ev, fz, ez = yapi()
    sw = 3.5
    figs = "".join('<path id="f%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                   % (i, s["tx"], s["ty"], s["d"]) for i, s in enumerate(fig))
    evs = "".join('<path id="k%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(ev))
    # rozet: künye hapı (ku-rz) + GRAMMAR hapı (rz1, uçuşta söner)
    rw0 = Y.genislik("Lexend", 700, "YDT · BASIC", 24) + 44
    gw = Y.genislik("Lexend", 700, "GRAMMAR", 24) + 44
    gx = 48 + rw0 + 12
    roz = ('<g id="rz1" style="opacity:0"><rect x="%.1f" y="136" width="%.1f" height="46" rx="23" fill="%s"/>'
           '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="24" '
           'fill="%s">GRAMMAR</text></g>' % (gx, gw, R["murekkep"], gx + gw / 2, 136 + 23 + 8.5, R["zemin"]))
    bs = ('font-family="Fredoka" font-weight="700" font-size="%d" stroke="%s" stroke-width="10" '
          'stroke-linejoin="round" style="paint-order:stroke fill"' % (BASLIK_BOY, R["zemin"]))
    tit = ('<text id="t1" x="%d" y="%d" fill="%s" clip-path="url(#cp1)" %s>-YOR</text>'
           '<text id="t2" x="%d" y="%d" fill="%s" clip-path="url(#cp2)" %s>= -ING</text>'
           % (SOL, T1_Y, R["murekkep"], bs, SOL, T2_Y, R["logoSari"], bs))
    tw1 = Y.genislik("Fredoka", 700, "-YOR", BASLIK_BOY) + 24
    tw2 = Y.genislik("Fredoka", 700, "= -ING", BASLIK_BOY) + 24
    cw = Y.genislik("Caveat", 700, SOZ[0]["sozcuk"], CUMLE_BOY) + 16
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                    % (n, n, SOL - 12, y - BASLIK_BOY + 8, int(BASLIK_BOY * 1.35))
                    for n, y in ((1, T1_Y), (2, T2_Y)))
    clips += ('<clipPath id="cp3"><rect id="cr3" x="%d" y="%d" width="0" height="%d"/></clipPath>'
              % (SOL - 12, CUMLE_Y - CUMLE_BOY, int(CUMLE_BOY * 1.5)))
    cum = ('<text id="cm" x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" fill="%s" '
           'clip-path="url(#cp3)">%s</text>' % (SOL, CUMLE_Y, CUMLE_BOY, R["murekkep"], SOZ[0]["sozcuk"]))
    w1s = Y.genislik("Fredoka", 700, "-YOR", 36)
    hedef = {"t1": [48, 104, 36 / BASLIK_BOY], "t2": [48 + w1s + 14, 104, 36 / BASLIK_BOY]}
    kunye = Y.kunye_svg("Hook")
    veri = {"Z": Z, "fz": fz, "ez": ez, "nF": len(fig), "nE": len(ev), "hedef": hedef,
            "sol": SOL, "t1y": T1_Y, "t2y": T2_Y, "tw": [tw1, tw2], "cw": [cw, SOZ[0]["t0"], SOZ[0]["t1"]],
            "logo": [LOGO_BX, LOGO_BY, LOGO_W, LOGO_H]}
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
<g id="ev" filter="url(#el)"><g transform="translate({EV_X} {EV_Y}) rotate(-5 132 132) scale({EV_S})" stroke-width="{sw / EV_S:.3f}">{evs}</g></g>
</g>
{roz}{tit}{cum}
<g id="logo"><g id="lgs" style="opacity:0"><image id="logoimg" href="assets/logo.svg" x="{LOGO_BX:.2f}" y="{LOGO_BY}" width="{LOGO_W:.2f}" height="{LOGO_H}"/></g></g>
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
  gsap.set("#ku-ders,#ku-bolum,#ku-rz", {{ opacity: 0 }});

  // 0,0-0,4 logo damgası alt solda (HUD'daki yeri): ölçek 1,18->1,0 + dönme -2 -> 0, alfa 0->1
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
  // 1,0-1,65 cümle 1 "Gidiyorum." konuşmayla yazılır
  tl.fromTo("#cr3", {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.cw[0] }}, duration: Z.cumle[1], ease: "none", immediateRender: false }}, Z.cumle[0]);

  gsap.set("#eskiz", {{ svgOrigin: "540 1100" }});
  // 2,0-3,0 uçuş: başlık künyeye küçülür, eskiz + cümle + GRAMMAR söner, künye metinleri son 0,25 sn'de belirir
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud, H = V.hedef;
  function uc2(id, ox, oy, h, ex) {{
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, x: h[0] - ox, duration: ud, ease: ex }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, y: h[1] - oy, duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, scale: h[2], duration: ud * 0.8, ease: "power3.out" }}), u0);
  }}
  uc2("#t1", V.sol, V.t1y, H.t1, "power3.inOut"); uc2("#t2", V.sol, V.t2y, H.t2, "power2.out");
  tl.to("#t2", ac({{ fill: "{R['murekkep']}", duration: ud * 0.6, ease: "power1.inOut" }}), u0);
  tl.to("#rz1", ac({{ opacity: 0, duration: 0.3, ease: "power1.in" }}), u0);
  tl.to("#cm", ac({{ opacity: 0, duration: 0.4, ease: "power1.in" }}), u0 + 0.05);
  tl.to("#eskiz", ac({{ opacity: 0, scale: 1.06, duration: 0.45, ease: "power1.in" }}), u0 + 0.1);
  var son = u1 - 0.25;
  ["#t1", "#t2"].forEach(function (s) {{ tl.to(s, ac({{ opacity: 0, duration: 0.25, ease: "power1.in" }}), son); }});
  tl.to("#ku-ders,#ku-bolum", ac({{ opacity: 1, duration: 0.25, ease: "power1.out" }}), son);

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

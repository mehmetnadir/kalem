"""Sahne 01 DİKEY (1080x1920) index.html üretici: kapak kalıbı, 3 sn içerik + 12 kare geçiş payı = 102 kare.
Yerleşim BRIEF-DIKEY §2-§4: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform bandı boş.
Zamanlar: zamanlar.json (olay.py ile ortak); cümle 1 sözcük zamanları: ortak/anlatim/sozcukler.json."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
ANL = AD / ".." / ".." / "ortak" / "anlatim"
SOZ = [w for w in json.loads((ANL / "sozcukler.json").read_text()) if w["cumle"] == 1]
ALT = [a for a in json.loads((ANL / "altyazi.json").read_text()) if a["cumle"] == 1]
R = Y.RENK
SOL = 48
# başlık: PRESENT 210 px = 894 px, PERFECT 210 px = 900 px (984 px güvenli genişliğe sığar)
B1, B2 = 210, 210
T1_Y, T2_Y = 545, 745
CUMLE_BOY, CUMLE_Y = 96, (900,)             # tek satır, Caveat 96 (842 px)
CUMLE_HEDEF_Y = (450,)                       # sahne 02'deki yer (uçuş sonu)
FIG_S, FIG_X, FIG_Y = 0.64, 140.0, 955.0     # standing-4 681 px -> 436 px (alt kenar 1391)
EV_S, EV_X, EV_Y = 20.0, 540.0, 960.0        # home 18 birim -> 360 px (alt kenar 1380)
LOGO_X, LOGO_Y, LOGO_H = 48, 48, 96
LOGO_W = LOGO_H * Y.LOGO_EN_BOY


def yapi():
    gf, hf, fig = Y.peeps("standing-4", 60)
    ev = Y.tabler("home")
    fz = Y.cizgi_zamanlari([s["uz"] for s in fig], Z["figur"][0], Z["figur"][0] + Z["figur"][1])
    ez = Y.cizgi_zamanlari([40.0] * len(ev), Z["ev"][0], Z["ev"][0] + Z["ev"][1])
    return fig, ev, fz, ez


def sozcuk_yerleri():
    """Sözcük başına (satır, x0, genişlik). Cümle tek satır."""
    font = ("Caveat", 700)
    bosluk = Y.genislik(*font, " ", CUMLE_BOY)
    x, yer = SOL, []
    for i, w in enumerate(SOZ):
        sat = 0
        if sat == 1:
            x = SOL
        gw = Y.genislik(*font, w["sozcuk"], CUMLE_BOY)
        yer.append((sat, x, gw))
        x += gw + bosluk
    return yer


def uret():
    fig, ev, fz, ez = yapi()
    figs = "".join('<path id="f%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                   % (i, s["tx"], s["ty"], s["d"]) for i, s in enumerate(fig))
    evs = "".join('<path id="k%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(ev))
    # GRAMMAR hapı: YDT · BASIC hapının yanında (kapakta); uçuşta söner
    rw0 = Y.genislik("Lexend", 700, Y.ROZET, 36) + 56
    gw = Y.genislik("Lexend", 700, "GRAMMAR", 36) + 56
    gx = 48 + rw0 + 16
    roz = ('<g id="rz1" style="opacity:0"><rect x="%.1f" y="236" width="%.1f" height="72" rx="36" fill="%s"/>'
           '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" '
           'fill="%s">GRAMMAR</text></g>' % (gx, gw, R["murekkep"], gx + gw / 2, 236 + 36 + 13, R["zemin"]))
    bs = ('font-family="Fredoka" font-weight="700" font-size="%d" stroke="%s" stroke-width="12" '
          'stroke-linejoin="round" style="paint-order:stroke fill"')
    tit = ('<text id="t1" x="%d" y="%d" fill="%s" clip-path="url(#cp1)" %s>PRESENT</text>'
           '<text id="t2" x="%d" y="%d" fill="%s" clip-path="url(#cp2)" %s>PERFECT</text>'
           % (SOL, T1_Y, R["murekkep"], bs % (B1, R["zemin"]),
              SOL, T2_Y, R["logoSari"], bs % (B2, R["zemin"])))
    tw1 = Y.genislik("Fredoka", 700, "PRESENT", B1) + 28
    tw2 = Y.genislik("Fredoka", 700, "PERFECT", B2) + 28
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                    % (n, n, SOL - 14, y - b + 8, int(b * 1.35))
                    for n, y, b in ((1, T1_Y, B1), (2, T2_Y, B2)))
    # cümle 1: her sözcük ayrı <text>, kendi kırpması konuşma süresinde açılır
    yer = sozcuk_yerleri()
    cum, cw = [], []
    for i, (w, (sat, x, gw_)) in enumerate(zip(SOZ, yer)):
        y = CUMLE_Y[sat]
        clips += ('<clipPath id="cpw%d"><rect id="crw%d" x="%.1f" y="%d" width="0" height="%d"/></clipPath>'
                  % (i, i, x - 8, y - CUMLE_BOY, int(CUMLE_BOY * 1.5)))
        cum.append('<text x="%.1f" y="%d" font-family="Caveat" font-weight="700" font-size="%d" fill="%s" '
                   'clip-path="url(#cpw%d)">%s</text>' % (x, y, CUMLE_BOY, R["murekkep"], i, w["sozcuk"]))
        cw.append([w["t0"], min(w["t1"], w["t0"] + 0.5, 2.85), gw_ + 16])
    cum = '<g id="cm">' + "".join(cum) + "</g>"
    ders_w = Y.genislik("Fredoka", 700, "PRESENT ", 56)
    hedef = {"t1": [48, 212, 56 / B1], "t2": [48 + ders_w, 212, 56 / B2]}
    kunye = Y.kunye_svg("Hook")
    altyazi = Y.altyazi_svg([{"id": "alt0", "metin": ALT[0]["metin"]}])
    veri = {"Z": Z, "fz": fz, "ez": ez, "nF": len(fig), "nE": len(ev), "hedef": hedef,
            "sol": SOL, "t1y": T1_Y, "t2y": T2_Y, "tw": [tw1, tw2], "cw": cw,
            "cdy": CUMLE_HEDEF_Y[0] - CUMLE_Y[0], "logo": [LOGO_X, LOGO_Y, LOGO_W, LOGO_H]}
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
<g id="fig" transform="translate({FIG_X} {FIG_Y}) scale({FIG_S})" stroke-width="{4.4 / FIG_S:.3f}">{figs}</g>
<g id="ev" filter="url(#el)"><g transform="translate({EV_X} {EV_Y}) rotate(-5 12 12) scale({EV_S})" stroke-width="{4.0 / EV_S:.3f}">{evs}</g></g>
</g>
{roz}{tit}{cum}
<g id="logo" style="opacity:0"><image id="logoimg" href="assets/logo.svg" x="{LOGO_X}" y="{LOGO_Y}" width="{LOGO_W:.2f}" height="{LOGO_H}"/></g>
{kunye}{altyazi}
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

  // 0,0-0,4 logo damgası HUD'daki yerinde (sol üst 387x96): ölçek 1,18->1,0 + dönme -2 -> 0, alfa 0->1
  var lg = V.logo;
  gsap.set("#logo", {{ svgOrigin: (lg[0] + lg[2] / 2) + " " + (lg[1] + lg[3] / 2) }});
  tl.fromTo("#logo", {{ opacity: 0, scale: 1.18, rotation: -2 }},
    {{ opacity: 1, scale: 1, rotation: 0, duration: Z.logo_damga[1], ease: "power3.out", immediateRender: false }}, Z.logo_damga[0]);

  // 0,3-0,9 rozetler: künye hapı (kalır) + GRAMMAR (uçuşta söner)
  tl.fromTo("#ku-rz", {{ y: 26, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.rozet[0]);
  tl.fromTo("#rz1", {{ y: 26, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.rozet[0] + Z.rozet[1]);
  // 0,65-1,45 başlık kalemle çizilir (kırpma soldan açılır)
  [0, 1].forEach(function (i) {{
    tl.fromTo("#cr" + (i + 1), {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.tw[i] }}, duration: Z.baslik[i][1], ease: "none", immediateRender: false }}, Z.baslik[i][0]);
  }});
  // 1,0-2,92 cümle 1: her sözcük konuşma zamanında açılır
  V.cw.forEach(function (w, i) {{
    tl.fromTo("#crw" + i, {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: w[2] }}, duration: Math.max(0.1, w[1] - w[0]), ease: "none", immediateRender: false }}, w[0]);
  }});
  // altyazı: cümle 1 parçası konuşmayla gelir, sahne sonuna kadar kalır
  tl.set("#alt0", ac({{ opacity: 1 }}), Z.altyazi);

  gsap.set("#eskiz", {{ svgOrigin: "540 1170" }});
  // 2,0-3,0 uçuş: başlık HUD ders adına küçülür, cümle sahne 02'deki yerine kayar, GRAMMAR söner (eskiz kalır: alt yarı boş kalmasın)
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud, H = V.hedef;
  function uc2(id, ox, oy, h, ex) {{
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, x: h[0] - ox, duration: ud, ease: ex }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, y: h[1] - oy, duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, scale: h[2], duration: ud * 0.8, ease: "power3.out" }}), u0);
  }}
  uc2("#t1", V.sol, V.t1y, H.t1, "power3.inOut"); uc2("#t2", V.sol, V.t2y, H.t2, "power2.out");
  tl.to("#t2", ac({{ fill: "{R['murekkep']}", duration: ud * 0.6, ease: "power1.inOut" }}), u0);
  tl.to("#rz1", ac({{ opacity: 0, duration: 0.3, ease: "power1.in" }}), u0);
  tl.to("#cm", ac({{ y: V.cdy, duration: ud, ease: "power3.inOut" }}), u0);
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

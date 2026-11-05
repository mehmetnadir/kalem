"""Sahne 03 CTA index.html üretici (PPC ileri S1 Shorts; DİKEY 1080x1920; 247 kare = 8,23 sn).
Küresel t = 16,69 + yerel sn. HUD hazır (ilk 12 kare geçiş altında durgun); içerik bandı 352-1392:
`Tam ders:` (Caveat 88) -> `Present / Perfect / Continuous` bandı (Fredoka 150, 3 satır) ->
saat + `6 dakika` (120) -> `Tam ders kanalda · 6 dk` hapı (64). Altyazı bandı 1400-1536."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
ALT = json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "altyazi.json").read_text())
R = Y.RENK
CIP = "Full lesson"
T_BAS = 16.69
CX = 540
CAV_Y, CAV_BOY = 450, 88
BANT = (60, 490, 960, 510)          # x, y, w, h
BOY = 150
P1_Y, P2_Y, P3_Y = 655, 805, 955
SAAT_S, SAAT_X, SAAT_Y = 9.0, 192.0, 1008.0     # görünür daire: x 219-381, y 1035-1197
DK_BOY = 120
DK_X, DK_Y = 417, 1156
PILL = (120, 1235, 840, 120)
L_BOY, L_Y = 64, 1317


def yapi():
    saat = Y.tabler("clock")
    sz = Y.cizgi_zamanlari([57.0, 8.0], Z["saat"][0], Z["saat"][0] + Z["saat"][1])
    return saat, sz


def uret():
    saat, sz = yapi()
    cav = "Tam ders:"
    cav_w = Y.genislik("Caveat", 700, cav, CAV_BOY) + 24
    dk = "6 dakika"
    dk_w = Y.genislik("Fredoka", 700, dk, DK_BOY) + 24
    t_a, t_b = "Tam ders kanalda · ", "6 dk"
    wa = Y.genislik("Fredoka", 700, t_a, L_BOY)
    wb = Y.genislik("Fredoka", 700, t_b, L_BOY)
    lx = CX - (wa + wb) / 2
    cy_mid = BANT[1] + BANT[3] / 2
    saats = "".join('<path id="s%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(saat))
    bx, by, bw, bh = BANT
    bk_d = ("M%d %d H%d a44 44 0 0 1 44 44 V%d a44 44 0 0 1 -44 44 H%d a44 44 0 0 1 -44 -44 V%d a44 44 0 0 1 44 -44 Z"
            % (bx + 44, by, bx + bw - 44, by + bh - 44, bx + 44, by + 44))
    kunye = Y.kunye_svg(CIP)
    alt_svg, alt_zaman = Y.altyazi_svg(T_BAS, Z["sure"], ALT)
    veri = {"Z": Z, "sz": sz, "nS": len(saat), "cav": cav_w, "dk": dk_w,
            "lw": wa + wb + 24, "cx": CX, "cy": cy_mid, "pcx": PILL[0] + PILL[2] / 2,
            "pcy": PILL[1] + PILL[3] / 2, "alt": alt_zaman}
    cp = lambda n, x, y, b: ('<clipPath id="cp%s"><rect id="cr%s" x="%.1f" y="%d" width="0" height="%d"/>'  # noqa: E731
                             '</clipPath>' % (n, n, x, y - b, int(b * 1.5)))
    clips = (cp("c", CX - cav_w / 2, CAV_Y, CAV_BOY)
             + cp("d", DK_X - 12, DK_Y, DK_BOY) + cp("l", lx - 12, L_Y, L_BOY))
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
<defs>{clips}</defs>
<text id="cav" x="{CX}" y="{CAV_Y}" text-anchor="middle" font-family="Caveat" font-weight="700" font-size="{CAV_BOY}" fill="{R['murekkep']}" clip-path="url(#cpc)">{cav}</text>
<path id="bk" d="{bk_d}" fill="none" stroke="{R['vurgu']}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>
<g id="bantg" style="opacity:0">
<rect id="bant" x="{BANT[0]}" y="{BANT[1]}" width="{BANT[2]}" height="{BANT[3]}" rx="44" fill="{R['vurgu']}"/>
<text id="p1" x="{CX}" y="{P1_Y}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="{BOY}" fill="{R['zemin']}" style="opacity:0">Present</text>
<text id="p2" x="{CX}" y="{P2_Y}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="{BOY}" fill="{R['zemin']}" style="opacity:0">Perfect</text>
<text id="p3" x="{CX}" y="{P3_Y}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="{BOY}" fill="{R['zemin']}" style="opacity:0">Continuous</text>
</g>
<g id="saat" fill="none" stroke="{R['vurgu']}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{4 / SAAT_S:.3f}"><g transform="translate({SAAT_X} {SAAT_Y}) scale({SAAT_S})">{saats}</g></g>
<text id="dk" x="{DK_X}" y="{DK_Y}" font-family="Fredoka" font-weight="700" font-size="{DK_BOY}" fill="{R['murekkep']}" clip-path="url(#cpd)">{dk}</text>
<g id="pilg" style="opacity:0">
<rect id="pill" x="{PILL[0]}" y="{PILL[1]}" width="{PILL[2]}" height="{PILL[3]}" rx="60" fill="{R['vurgu']}"/>
<text id="lin" x="{lx:.1f}" y="{L_Y}" font-family="Fredoka" font-weight="700" font-size="{L_BOY}" fill="{R['zemin']}" clip-path="url(#cpl)">{t_a}{t_b}</text>
</g>
{kunye}<g id="altyazi">{alt_svg}</g>
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
  function yaz(id, z, w) {{
    tl.fromTo("#cr" + id, {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: w }}, duration: z[1], ease: "none", immediateRender: false }}, z[0]);
  }}
  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]); tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});
  for (var i = 0; i < V.nS; i++) darbe("s" + i, V.sz[i][0], V.sz[i][1]);
  darbe("bk", Z.bant_kontur[0], Z.bant_kontur[1]);   // boş bant konturu: içerik bandı konuşma beklerken boş kalmaz
  yaz("c", Z.tam_ders, V.cav);
  gsap.set("#bantg", {{ svgOrigin: V.cx + " " + V.cy }});
  tl.fromTo("#bantg", {{ opacity: 0, scale: 0.92 }}, {{ opacity: 1, scale: 1, duration: Z.bant[1], ease: "power3.out", immediateRender: false }}, Z.bant[0]);
  tl.fromTo("#p1", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3, ease: "power2.out", immediateRender: false }}, Z.bant[0] + 0.04);
  tl.fromTo("#p2", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: Z.satir2[1], ease: "power3.out", immediateRender: false }}, Z.satir2[0]);
  tl.fromTo("#p3", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: Z.satir3[1], ease: "power3.out", immediateRender: false }}, Z.satir3[0]);
  yaz("d", Z.dakika, V.dk);
  gsap.set("#pilg", {{ svgOrigin: V.pcx + " " + V.pcy }});
  tl.fromTo("#pilg", {{ opacity: 0, scale: 0.9 }}, {{ opacity: 1, scale: 1, duration: Z.pill[1], ease: "power3.out", immediateRender: false }}, Z.pill[0]);
  yaz("l", Z.cta, V.lw);
  // durgun kuyruk: bant ve hap hafif nabız (1,5 sn)
  tl.to("#bantg", ac({{ scale: 1.015, duration: 0.8, ease: "sine.inOut", yoyo: true, repeat: 1 }}), 6.0);
  tl.to("#pilg", ac({{ scale: 1.03, duration: 0.8, ease: "sine.inOut", yoyo: true, repeat: 1 }}), 6.0);
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, saat, sz


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html, *_ = uret()
    (AD / "proje" / "index.html").write_text(html)
    print("index.html yazıldı", len(html))

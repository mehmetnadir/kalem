"""Sahne 03 CTA index.html üretici (DİKEY 1080x1920; 7,22 sn içerik + 1 sn durgun kuyruk = 247 kare).
Küresel t = 16,75 + yerel sn. Künye hazır (ilk 12 kare geçiş altında durgun), içerik 0,45 sn'den başlar."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
R = Y.RENK
CIP = "FULL LESSON"
T_BAS = 16.75                       # sahnenin küresel başlangıcı (altyazı zamanı için)
ALT = json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "altyazi.json").read_text())
# 05.11 düzeltme (telefon ölçeği): içerik bandı 352-1392 dolu; Caveat 72, bant Fredoka 150, alt satır 64
BANT = (48, 510, 984, 560)          # x, y, w, h  (y 510-1070)
CAV_Y, CAV_BOY = 460, 72
BOY = 150
L_BOY, L_Y = 64, 1263               # satır merkezi y 1240
SAAT_S, SAAT_MERKEZ_Y = 6.0, 1240   # saat simgesi: görünür çap 108 px


def yapi():
    saat = Y.tabler("clock")
    sz = Y.cizgi_zamanlari([70.0, 8.0], Z["saat"][0], Z["saat"][0] + Z["saat"][1])
    return saat, sz


def uret():
    saat, sz = yapi()
    w1 = Y.genislik("Fredoka", 700, "Present", BOY)
    w2 = Y.genislik("Fredoka", 700, "Perfect", BOY)
    w3 = Y.genislik("Fredoka", 700, "Continuous", BOY)
    boy = int(min(BOY, BOY * 900 / max(w1, w2, w3)))
    cx = BANT[0] + BANT[2] / 2
    cy_mid = BANT[1] + BANT[3] / 2
    adim = boy * 0.95                # üç satır: blok merkezi bant merkezinde (kapak yüksekliği 0,35 boy)
    y2 = cy_mid + boy * 0.35
    y1 = y2 - adim
    y3 = y2 + adim
    cav = "Tam ders:"
    cav_w = Y.genislik("Caveat", 700, cav, CAV_BOY) + 24
    # alt satır: saat simgesi + "@ydspublishing · 6 dk"
    t_a, t_b = "@ydspublishing", " · 6 dk"   # karar A 05.11: tek kimlik
    wa = Y.genislik("Lexend", 700, t_a, L_BOY)
    wb = Y.genislik("Lexend", 700, t_b, L_BOY)
    ic = 108 + 28                   # saat çapı + boşluk
    top = ic + wa + wb
    x0 = (1080 - top) / 2
    tx = x0 + ic
    saat_cx = x0 + 54
    kunye = Y.kunye_svg(CIP)
    alt_svg, alt_zaman = Y.altyazi_svg(T_BAS, Z["sure"], ALT)
    saats = "".join('<path id="s%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(saat))
    veri = {"Z": Z, "sz": sz, "nS": len(saat), "cav": cav_w, "lw": wa + wb + 40, "lx": tx - 12,
            "cx": cx, "cy": cy_mid, "bw": BANT[2], "alt": alt_zaman}
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
<defs><clipPath id="cpc"><rect id="crc" x="{cx - cav_w / 2:.1f}" y="{CAV_Y - CAV_BOY}" width="0" height="{int(CAV_BOY * 1.5)}"/></clipPath>
<clipPath id="cpl"><rect id="crl" x="{tx - 12:.1f}" y="{L_Y - L_BOY - 10}" width="0" height="{int(L_BOY * 1.6)}"/></clipPath></defs>
<text id="cav" x="{cx}" y="{CAV_Y}" text-anchor="middle" font-family="Caveat" font-weight="700" font-size="{CAV_BOY}" fill="{R['murekkep']}" clip-path="url(#cpc)">Tam ders:</text>
<g id="bantg" style="opacity:0">
<rect id="bant" x="{BANT[0]}" y="{BANT[1]}" width="{BANT[2]}" height="{BANT[3]}" rx="44" fill="{R['vurgu']}"/>
<text id="p1" x="{cx}" y="{y1:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="{boy}" fill="{R['zemin']}" style="opacity:0">Present</text>
<text id="p2" x="{cx}" y="{y2:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="{boy}" fill="{R['zemin']}" style="opacity:0">Perfect</text>
<text id="p3" x="{cx}" y="{y3:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="{boy}" fill="{R['zemin']}" style="opacity:0">Continuous</text>
</g>
<g id="saat" fill="none" stroke="{R['vurgu']}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{6 / SAAT_S:.2f}"><g transform="translate({saat_cx - 12 * SAAT_S:.1f} {SAAT_MERKEZ_Y - 12 * SAAT_S:.1f}) scale({SAAT_S})">{saats}</g></g>
<text id="lin" x="{tx:.1f}" y="{L_Y}" font-family="Lexend" font-weight="700" font-size="{L_BOY}" fill="{R['murekkep']}" clip-path="url(#cpl)"><tspan fill="{R['vurgu']}">{t_a}</tspan>{t_b}</text>
<g id="par" stroke="{R['vurgu']}" stroke-width="5" style="opacity:0">
<path d="M1000 590 l0 -44 M978 568 l44 0 M986 552 l28 32 M1014 552 l-28 32"/>
<path d="M84 1150 l0 -34 M67 1133 l34 0"/></g>
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
  for (var i = 0; i < V.nS; i++) darbe("s" + i, V.sz[i][0], V.sz[i][1]);
  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]); tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});
  gsap.set("#bantg", {{ svgOrigin: V.cx + " " + V.cy }});
  tl.fromTo("#crc", {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.cav }}, duration: Z.tam_ders[1], ease: "none", immediateRender: false }}, Z.tam_ders[0]);
  tl.fromTo("#bantg", {{ opacity: 0, scale: 0.92 }}, {{ opacity: 1, scale: 1, duration: Z.bant[1], ease: "power3.out", immediateRender: false }}, Z.bant[0]);
  tl.fromTo("#p1", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3, ease: "power2.out", immediateRender: false }}, Z.bant[0] + 0.04);
  tl.fromTo("#p2", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: Z.satir2[1], ease: "power3.out", immediateRender: false }}, Z.satir2[0]);
  tl.fromTo("#p3", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: Z.satir3[1], ease: "power3.out", immediateRender: false }}, Z.satir3[0]);
  tl.fromTo("#crl", {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.lw }}, duration: Z.satir[1], ease: "none", immediateRender: false }}, Z.satir[0]);
  // sarı tarafa nabız + parıltı
  tl.fromTo("#par", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, ease: "power3.out", immediateRender: false }}, Z.parilti);
  tl.to("#par", ac({{ opacity: 0, duration: 0.3, ease: "power1.in" }}), Z.parilti + 0.3);
  tl.to("#bantg", ac({{ scale: 1.015, duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 1 }}), 5.0);
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, saat, sz


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    html, *_ = uret()
    (AD / "proje" / "index.html").write_text(html)
    print("index.html yazıldı", len(html))

"""Sahne 01 giriş İLERİ (soğuk açılış kapağı, HyperFrames, 3,00 sn içerik + 12 kare geçiş payı = 102 kare).
Zamanlar: zamanlar.json (olay.py ile ortak); cümle 1 sözcük zamanları: ortak/anlatim/sozcukler.json (küresel = yerel sn).
Kapak kalıbı: başlık kalemle çizilir, Caveat cümle konuşmayla yazılır, sonda künyeye uçuş.
Künye metni ortak/kunye.js KUNYE ile aynı: SIMPLE PRESENT · YDT ADVANCED · Hook / Rule / Roots (etkin Hook)."""
import json
import math
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
SOZ = [w for w in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == 1]
R = Y.RENK
BASLIK_BOY = 140
# ---- yerleşim (px) ----
SOL = 96
HEDEF_CUMLE = (140, 300)   # sahne 02 cümle 1 yeri (kanca sahnesi aynı yerde başlar)
ROZET_Y, ROZET_H = 150, 48
T1_Y, T2_Y = 360, 510
CUMLE_Y, CUMLE_BOY = 650, 64
LOGO_H = 110
LOGO_W = LOGO_H * Y.LOGO_EN_BOY
LOGO_BX, LOGO_BY = SOL - Y.LOGO_KAYMA * LOGO_W, 880.0
# çizim: saat, takvim, kalem (Tabler çizgi ikonları, 24 birimlik kutu; rutin = geniş zaman)
OBJ = (("saat", "clock", 11.0, 1340.0, 190.0, (57.0, 11.0)),
       ("takvim", "calendar", 9.0, 1390.0, 560.0, (62.0, 4.0, 4.0, 16.0, 1.0, 3.0)),
       ("kalem", "pencil", 6.0, 1660.0, 130.0, (46.0, 6.0)))


def yapi():
    cikti = []
    for ad, ikon, olcek, x, y, uz in OBJ:
        yollar = Y.tabler(ikon)
        assert len(yollar) == len(uz), ikon
        cikti.append((ad, olcek, x, y, yollar, Y.cizgi_zamanlari(list(uz), *Z[ad])))
    return cikti


def uret():
    obj = yapi()
    sw = 3.5
    ciz = ""
    for ad, olcek, x, y, yollar, zam in obj:
        rot = ' rotate(-5 12 12)' if ad == "saat" else ""
        ciz += ('<g id="%s" filter="url(#el)"><g transform="translate(%.1f %.1f) scale(%.2f)%s" '
                'stroke-width="%.3f">%s</g></g>' % (ad, x, y, olcek, rot, sw / olcek, "".join(
                    '<path id="%s_%d" d="%s" style="opacity:0"/>' % (ad, i, d) for i, d in enumerate(yollar))))
    # rozetler
    roz = []
    x = SOL
    for i, (m, dolgu) in enumerate((("YDT · ADVANCED", R["vurgu"]), ("GRAMMAR", R["murekkep"]))):
        w = Y.genislik("Lexend", 700, m, 26) + 44
        roz.append('<g id="rz%d" style="opacity:0"><rect x="%.1f" y="%d" width="%.1f" height="%d" rx="24" fill="%s"/>'
                   '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" font-weight="700" '
                   'font-size="26" fill="%s">%s</text></g>'
                   % (i, x, ROZET_Y, w, ROZET_H, dolgu, x + w / 2, ROZET_Y + ROZET_H / 2 + 9.1, R["zemin"], m))
        x += w + 12
    bs = 'font-family="Fredoka" font-weight="700" font-size="%d" stroke="%s" stroke-width="10" ' \
         'stroke-linejoin="round" style="paint-order:stroke fill"' % (BASLIK_BOY, R["zemin"])
    tit = ('<text id="t1" x="%d" y="%d" fill="%s" clip-path="url(#cp1)" %s>SIMPLE</text>'
           '<text id="t2" x="%d" y="%d" fill="%s" clip-path="url(#cp2)" %s>PRESENT</text>'
           % (SOL, T1_Y, R["murekkep"], bs, SOL, T2_Y, R["logoSari"], bs))
    tw1 = Y.genislik("Fredoka", 700, "SIMPLE", BASLIK_BOY) + 24
    tw2 = Y.genislik("Fredoka", 700, "PRESENT", BASLIK_BOY) + 24
    cum_metin = " ".join(w["sozcuk"] for w in SOZ)
    cum_x = [SOL + Y.genislik("Caveat", 700, " ".join(w["sozcuk"] for w in SOZ[:i + 1]), CUMLE_BOY) + 8
             for i in range(len(SOZ))]
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                    % (n, n, SOL - 12, y - BASLIK_BOY + 8, int(BASLIK_BOY * 1.35))
                    for n, y in ((1, T1_Y), (2, T2_Y)))
    clips += ('<clipPath id="cp3"><rect id="cr3" x="%d" y="%d" width="0" height="%d"/></clipPath>'
              % (SOL - 12, CUMLE_Y - CUMLE_BOY, int(CUMLE_BOY * 1.5)))
    cum = ('<g id="cg"><text id="cm" x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" fill="%s" '
           'clip-path="url(#cp3)">%s</text></g>' % (SOL, CUMLE_Y, CUMLE_BOY, R["murekkep"], cum_metin))
    ders_w = Y.genislik("Fredoka", 700, "SIMPLE ", 30)
    hedef = {"t1": [56, 72, 30 / BASLIK_BOY], "t2": [56 + ders_w, 72, 30 / BASLIK_BOY],
             "logo": [56, 1002, 34 / LOGO_H]}
    kunye = Y.kunye_svg("Hook", "Hook", 0, 0)
    veri = {"Z": Z, "obj": [[a[0], [[b, d] for b, d in a[5]]] for a in obj], "hedef": hedef,
            "sol": SOL, "t1y": T1_Y, "t2y": T2_Y, "tw": [tw1, tw2],
            "cw": [[w["t0"], min(w["t1"], w["t0"] + 0.5, 2.96), cum_x[i]] for i, w in enumerate(SOZ)],
            "logo": [LOGO_BX, LOGO_BY, LOGO_W, LOGO_H], "hc": [HEDEF_CUMLE[0] - SOL, HEDEF_CUMLE[1] - CUMLE_Y]}
    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{Z['sure']}" data-fps="30" data-width="1920" data-height="1080">
{Y.zemin_html()}
<svg id="sahne" width="1920" height="1080" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
<defs>{clips}<filter id="el" x="-5%" y="-5%" width="110%" height="110%">
<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="5" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="3.2"/></filter></defs>
<g id="eskiz" fill="none" stroke="{R['murekkep']}" stroke-linecap="round" stroke-linejoin="round">{ciz}
<g id="par" stroke="{R['vurgu']}" stroke-width="5" style="opacity:0">
<path d="M1730 380 l0 -46 M1707 357 l46 0 M1716 341 l28 32 M1744 341 l-28 32"/>
<path d="M1830 560 l0 -34 M1813 543 l34 0"/><path d="M1290 520 l0 -30 M1275 505 l30 0"/></g>
</g>
{''.join(roz)}{tit}{cum}
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
  // kalem darbesi: dash uzunluğu çalışma anında ölçülür
  function darbe(id, bas, sure) {{
    var p = $("#" + id), L = p.getTotalLength();
    p.style.strokeDasharray = L + " " + (L + 2); p.style.strokeDashoffset = L;
    tl.set(p, ac({{ opacity: 1 }}), bas);
    tl.to(p, ac({{ strokeDashoffset: 0, duration: sure, ease: "none" }}), bas);
  }}
  V.obj.forEach(function (o) {{ o[1].forEach(function (z, i) {{ darbe(o[0] + "_" + i, z[0], z[1]); }}); }});
  gsap.set("#ku-ders,#ku-bolum,#ku-ajA", {{ opacity: 0 }});

  // 0,0-0,4 logo damgası sol sütun altında (ölçek 1,18->1,0 + dönme -2 -> 0, alfa 0->1)
  var lg = V.logo, bx = lg[0], by = lg[1], bw = lg[2], bh = lg[3];
  gsap.set("#lgs", {{ svgOrigin: (bx + bw / 2) + " " + (by + bh / 2) }});
  gsap.set("#logo", {{ svgOrigin: bx + " " + by }});
  tl.fromTo("#lgs", {{ opacity: 0, scale: 1.18, rotation: -2 }},
    {{ opacity: 1, scale: 1, rotation: 0, duration: Z.logo_damga[1], ease: "power3.out", immediateRender: false }}, Z.logo_damga[0]);

  // 0,3-0,5 rozetler
  [0, 1].forEach(function (i) {{
    tl.fromTo("#rz" + i, {{ y: 26, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.rozet[0] + i * Z.rozet[1]);
  }});
  // 0,0-2,2 başlık kalemle çizilir: kırpma dikdörtgeni soldan sağa açılır (satır 1, sonra satır 2)
  [0, 1].forEach(function (i) {{
    tl.fromTo("#cr" + (i + 1), {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.tw[i] }}, duration: Z.baslik[i][1], ease: "none", immediateRender: false }}, Z.baslik[i][0]);
  }});
  // 1,00-2,58 Caveat cümlesi konuşmayla yazılır: her sözcük kendi süresinde açılır
  var onceki = 0;
  V.cw.forEach(function (w) {{
    tl.fromTo("#cr3", {{ attr: {{ width: onceki }} }}, {{ attr: {{ width: w[2] - V.sol + 12 }}, duration: w[1] - w[0], ease: "none", immediateRender: false }}, w[0]);
    onceki = w[2] - V.sol + 12;
  }});

  gsap.set("#eskiz", {{ svgOrigin: "1500 540" }});
  // cümle grubu sahne 02 yerine (140,300) kayar; yazım 2,96 sn'de biter, 3,00 sn'de yerinde
  tl.to("#cg", ac({{ x: V.hc[0], y: V.hc[1], duration: Z.cumle_ucus[1], ease: "power3.inOut" }}), Z.cumle_ucus[0]);

  // 2,2-3,0 uçuş
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud, H = V.hedef;
  function uc2(id, ox, oy, h, ex) {{
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, x: h[0] - ox, duration: ud, ease: ex }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, y: h[1] - oy, duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, scale: h[2], duration: ud * 0.8, ease: "power3.out" }}), u0);
  }}
  uc2("#t1", V.sol, V.t1y, H.t1, "power3.inOut"); uc2("#t2", V.sol, V.t2y, H.t2, "power2.out");
  tl.to("#logo", ac({{ x: H.logo[0] - bx, y: H.logo[1] - by, scale: H.logo[2], duration: ud, ease: "power3.inOut" }}), u0);
  tl.to("#t2", ac({{ fill: "{R['murekkep']}", duration: ud * 0.6, ease: "power1.inOut" }}), u0);
  ["#rz0", "#rz1"].forEach(function (s, k) {{
    tl.to(s, ac({{ opacity: 0, duration: 0.3, ease: "power1.in" }}), u0 + k * 0.04);
  }});
  tl.to("#eskiz", ac({{ opacity: 0, scale: 1.06, duration: 0.4, ease: "power1.in" }}), u0 + 0.1);
  tl.fromTo("#par", {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.2, ease: "power3.out", immediateRender: false, svgOrigin: "1500 540" }}, u0);
  tl.to("#par", ac({{ opacity: 0, duration: 0.3, ease: "power1.in" }}), u0 + 0.25);
  var son = u1 - 0.25;   // künye gerçek metinleri son 0,25 sn'de belirir
  ["#t1", "#t2"].forEach(function (s) {{ tl.to(s, ac({{ opacity: 0, duration: 0.25, ease: "power1.in" }}), son); }});
  tl.to("#ku-ders,#ku-bolum,#ku-ajA", ac({{ opacity: 1, duration: 0.25, ease: "power1.out" }}), son);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, obj


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    html, *_ = uret()
    (AD / "proje" / "index.html").write_text(html)
    print("index.html yazıldı", len(html))

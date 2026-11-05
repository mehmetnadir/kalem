"""Sahne 01 index.html üretici (soğuk açılış, 3 sn içerik + 12 kare geçiş payı = 102 kare).
Zamanlar: zamanlar.json (olay.py ile ortak); cümle 1 sözcük zamanları: ortak/anlatim/sozcukler.json.
Giriş kapak kalıbı: başlık kalemle çizilir, Caveat cümle konuşmayla yazılır, sonda künyeye uçuş."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
SOZ = [w for w in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == 1]
R = Y.RENK
BASLIK_BOY = 112
# ---- yerleşim (px) ----
SOL = 96
HEDEF_CUMLE = (140, 300)   # sahne 02 cümle 1 yeri (BRIEF §4)
ROZET_Y, ROZET_H = 150, 48
T1_Y, T2_Y = 340, 470
CUMLE_Y, CUMLE_BOY = 640, 64
LOGO_H = 110
LOGO_W = LOGO_H * Y.LOGO_EN_BOY
LOGO_BX, LOGO_BY = SOL - Y.LOGO_KAYMA * LOGO_W, 880.0
FIG_S, FIG_X, FIG_Y = 18.0, 1200.0, 120.0
KAM_S, KAM_X, KAM_Y = 14.0, 1450.0, 520.0


def yapi():
    fig = [{"tx": 0.0, "ty": 0.0, "d": d, "uz": 40.0} for d in Y.tabler("book")]   # yarım okunmuş kitap
    kam = Y.tabler("clock")                                                       # saat
    fz = Y.cizgi_zamanlari([s["uz"] for s in fig], *Z["figur"])
    kz = Y.cizgi_zamanlari([60.0, 25.0][:len(kam)], *Z["kamera"])
    return fig, kam, fz, kz


def uret():
    fig, kam, fz, kz = yapi()
    sw = 3.5
    figs = "".join('<path id="f%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                   % (i, s["tx"], s["ty"], s["d"]) for i, s in enumerate(fig))
    kams = "".join('<path id="k%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(kam))
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
    tit = ('<text id="t1" x="%d" y="%d" fill="%s" clip-path="url(#cp1)" %s>PRESENT PERFECT</text>'
           '<text id="t2" x="%d" y="%d" fill="%s" clip-path="url(#cp2)" %s>CONTINUOUS</text>'
           % (SOL, T1_Y, R["murekkep"], bs, SOL, T2_Y, R["logoSari"], bs))
    # kırpma dikdörtgenleri: genişlik 0'dan yazı genişliğine büyür (kalem ilerlemesi)
    tw1 = Y.genislik("Fredoka", 700, "PRESENT PERFECT", BASLIK_BOY) + 24
    tw2 = Y.genislik("Fredoka", 700, "CONTINUOUS", BASLIK_BOY) + 24
    cum_metin = " ".join(w["sozcuk"] for w in SOZ)
    cum_x = [SOL + Y.genislik("Caveat", 700, " ".join(w["sozcuk"] for w in SOZ[:i + 1]), CUMLE_BOY) + 8
             for i in range(len(SOZ))]
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                    % (n, n, SOL - 12, y - BASLIK_BOY + 8, int(BASLIK_BOY * 1.35))
                    for n, y in ((1, T1_Y), (2, T2_Y)))
    clips += ('<clipPath id="cp3"><rect id="cr3" x="%d" y="%d" width="0" height="%d"/></clipPath>'
              % (SOL - 12, CUMLE_Y - CUMLE_BOY, int(CUMLE_BOY * 1.5)))
    ing = SOZ[2]   # "sonuç" üstüne sarı halka
    ing_x0 = SOL + Y.genislik("Caveat", 700, " ".join(w["sozcuk"] for w in SOZ[:2]) + " ", CUMLE_BOY)
    ing_w = Y.genislik("Caveat", 700, ing["sozcuk"], CUMLE_BOY)
    hcx, hcy, hrx, hry = ing_x0 + ing_w / 2, CUMLE_Y - 22, ing_w / 2 + 16, 36
    import math
    nok = []
    for k in range(49):   # el halkası: 1,06 tur, hafif titrek, yarıçap yavaş büyür
        u = k / 48
        aa = -2.4 + u * 1.06 * 2 * math.pi
        kk = 1 + 0.04 * math.sin(u * 9) + 0.06 * (u - 0.5)
        nok.append("%.1f %.1f" % (hcx + math.cos(aa) * hrx * kk, hcy + math.sin(aa) * hry * kk))
    halka = ('<path id="halka" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round" '
             'stroke-linejoin="round" transform="rotate(-3 %.1f %.1f)" d="M %s" style="opacity:0"/>'
             % (R["vurgu"], hcx, hcy, " L ".join(nok)))
    cum = ('<g id="cg"><text id="cm" x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" fill="%s" '
           'clip-path="url(#cp3)">%s</text>%s</g>' % (SOL, CUMLE_Y, CUMLE_BOY, R["murekkep"], cum_metin, halka))
    ders_w = Y.genislik("Fredoka", 700, "PRESENT PERFECT ", 30)
    hedef = {"t1": [56, 72, 30 / BASLIK_BOY], "t2": [56 + ders_w, 72, 30 / BASLIK_BOY],
             "logo": [56, 1002, 34 / LOGO_H]}
    kunye = Y.kunye_svg("Hook", 0)
    veri = {"Z": Z, "fz": fz, "kz": kz, "nF": len(fig), "nK": len(kam), "hedef": hedef,
            "sol": SOL, "t1y": T1_Y, "t2y": T2_Y, "tw": [tw1, tw2],
            "cw": [[w["t0"], min(w["t1"], w["t0"] + 0.5, 2.96), cum_x[i]] for i, w in enumerate(SOZ)],
            "logo": [LOGO_BX, LOGO_BY, LOGO_W, LOGO_H], "hc": [HEDEF_CUMLE[0] - SOL, HEDEF_CUMLE[1] - CUMLE_Y], "figs": FIG_S, "sw": sw, "kams": KAM_S}
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
<g id="eskiz" fill="none" stroke="{R['murekkep']}" stroke-linecap="round" stroke-linejoin="round">
<g id="fig" filter="url(#el)"><g transform="translate({FIG_X} {FIG_Y}) scale({FIG_S})" stroke-width="{sw / FIG_S:.3f}">{figs}</g></g>
<g id="kam" filter="url(#el)"><g transform="translate({KAM_X} {KAM_Y}) rotate(-4 168 168) scale({KAM_S})" stroke-width="{sw / KAM_S:.3f}">{kams}</g></g>
<g id="par" stroke="{R['vurgu']}" stroke-width="5" style="opacity:0">
<path d="M1690 330 l0 -46 M1667 307 l46 0 M1676 291 l28 32 M1704 291 l-28 32"/>
<path d="M1800 600 l0 -34 M1783 583 l34 0"/><path d="M1400 480 l0 -30 M1385 465 l30 0"/></g>
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
  var IR = {{ immediateRender: false }};
  function ac(o) {{ o.immediateRender = false; return o; }}
  // kalem darbesi: dash uzunluğu çalışma anında ölçülür
  function darbe(id, bas, sure) {{
    var p = $("#" + id), L = p.getTotalLength();
    p.style.strokeDasharray = L + " " + (L + 2); p.style.strokeDashoffset = L;
    tl.set(p, ac({{ opacity: 1 }}), bas);
    tl.to(p, ac({{ strokeDashoffset: 0, duration: sure, ease: "none" }}), bas);
  }}
  for (var i = 0; i < V.nF; i++) darbe("f" + i, V.fz[i][0], V.fz[i][1]);
  for (var j = 0; j < V.nK; j++) darbe("k" + j, V.kz[j][0], V.kz[j][1]);
  gsap.set("#ku-ders,#ku-bolum,#ku-ajanda,#ku-nokta", {{ opacity: 0 }});

  // 0,0-0,4 logo damgası sol sütun altında (ölçek 1,18->1,0 + dönme -2 -> 0, alfa 0->1)
  var lg = V.logo, bx = lg[0], by = lg[1], bw = lg[2], bh = lg[3];
  gsap.set("#lgs", {{ svgOrigin: (bx + bw / 2) + " " + (by + bh / 2) }});
  gsap.set("#logo", {{ svgOrigin: bx + " " + by }});
  tl.fromTo("#lgs", {{ opacity: 0, scale: 1.18, rotation: -2 }},
    {{ opacity: 1, scale: 1, rotation: 0, duration: Z.logo_damga[1], ease: "power3.out", immediateRender: false }}, Z.logo_damga[0]);

  // 0,3-0,9 rozetler
  [0, 1].forEach(function (i) {{
    tl.fromTo("#rz" + i, {{ y: 26, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.rozet[0] + i * Z.rozet[1]);
  }});
  // 0,0-2,2 başlık kalemle çizilir: kırpma dikdörtgeni soldan sağa açılır (satır 1, sonra satır 2)
  [0, 1].forEach(function (i) {{
    tl.fromTo("#cr" + (i + 1), {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.tw[i] }}, duration: Z.baslik[i][1], ease: "none", immediateRender: false }}, Z.baslik[i][0]);
  }});
  // 1,0-2,9 Caveat cümlesi konuşmayla yazılır: her sözcük kendi süresinde açılır
  var onceki = 0;
  V.cw.forEach(function (w) {{
    tl.fromTo("#cr3", {{ attr: {{ width: onceki }} }}, {{ attr: {{ width: w[2] - V.sol + 12 }}, duration: w[1] - w[0], ease: "none", immediateRender: false }}, w[0]);
    onceki = w[2] - V.sol + 12;
  }});

  gsap.set("#eskiz", {{ svgOrigin: "1500 540" }});
  // 1,80 sarı halka -ing üstünde (kalem darbesi); cümle grubu sahne 02 yerine (140,300) kayar
  darbe("halka", Z.halka[0], Z.halka[1]);
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
  tl.to("#ku-ders,#ku-bolum,#ku-ajanda,#ku-nokta", ac({{ opacity: 1, duration: 0.25, ease: "power1.out" }}), son);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, fig, kam, fz, kz


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "assets" / "cizim").mkdir(parents=True, exist_ok=True)
    html, *_ = uret()
    (AD / "proje" / "index.html").write_text(html)
    print("index.html yazıldı", len(html))

"""Sahne 01 İLERİ DİKEY index.html üretici (1080x1920, 3 sn içerik + 12 kare geçiş payı = 102 kare).
BRIEF-DIKEY §2–§4: HUD sol üst (logo 387x96, ders adı 56, rozet 72, çip 80), içerik bandı 352–1392,
altyazı bandı 1400–1536 (Lexend 500 44), platform bandı 1536–1920 boş. Yatay yerleşim döndürülmez."""
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
# ---- yerleşim (px, 1080x1920) ----
KENAR = 48
BASLIK_BOY = 150                     # CONTINUOUS 150 px'te ~930 px (984 px'e sığar)
TS = 56                              # başlık x (kontur payı)
T1_Y, T2_Y, T3_Y = 572, 727, 882
ROZET_Y, ROZET_H, ROZET_YAZI = 354, 72, 36
HUD_ROZET_Y = 236
CUMLE_BOY, CUMLE_X = 80, 64
CUMLE_Y = (1000,)                    # tek satır taban
HEDEF_CUMLE_Y = (470,)                # sahne 02 yeri
FIG_S, FIG_X, FIG_Y = 20.0, 10.0, 1000.0
KAM_S, KAM_X, KAM_Y = 18.0, 610.0, 1030.0
LOGO_W, LOGO_H = 96 * Y.LOGO_EN_BOY, 96
ALT_Y = 1484                         # altyazı taban (tek satır: 1400 + 84)
SATIRLAR = [[0, 1, 2, 3]]          # sözcük indisleri / satır


def yapi():
    fig = [{"tx": 0.0, "ty": 0.0, "d": d, "uz": 40.0} for d in Y.tabler("book")]   # yarım okunmuş kitap
    kam = Y.tabler("clock")                                                       # saat
    fz = Y.cizgi_zamanlari([s["uz"] for s in fig], *Z["figur"])
    kz = Y.cizgi_zamanlari([60.0, 25.0][:len(kam)], *Z["kamera"])
    return fig, kam, fz, kz


def uret():
    fig, kam, fz, kz = yapi()
    sw = 4.4
    figs = "".join('<path id="f%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                   % (i, s["tx"], s["ty"], s["d"]) for i, s in enumerate(fig))
    kams = "".join('<path id="k%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(kam))
    # rozetler (cover): y 372 h 72; 1. hap HUD rozetine uçar
    roz, x = [], KENAR
    for i, (m, dolgu) in enumerate((("YDT · ADVANCED", R["vurgu"]), ("GRAMMAR", R["murekkep"]))):
        w = Y.genislik("Lexend", 700, m, ROZET_YAZI) + 56
        roz.append('<g id="rz%d" style="opacity:0"><rect x="%.1f" y="%d" width="%.1f" height="%d" rx="36" fill="%s"/>'
                   '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" font-weight="700" '
                   'font-size="%d" fill="%s">%s</text></g>'
                   % (i, x, ROZET_Y, w, ROZET_H, dolgu, x + w / 2, ROZET_Y + ROZET_H / 2 + 13, ROZET_YAZI,
                      R["zemin"], m))
        x += w + 16
    bs = ('font-family="Fredoka" font-weight="700" font-size="%d" stroke="%s" stroke-width="12" '
          'stroke-linejoin="round" style="paint-order:stroke fill"' % (BASLIK_BOY, R["zemin"]))
    tit = ('<text id="t1" x="%d" y="%d" fill="%s" clip-path="url(#cp1)" %s>PRESENT</text>'
           '<text id="t3" x="%d" y="%d" fill="%s" clip-path="url(#cp2)" %s>PERFECT</text>'
           '<text id="t2" x="%d" y="%d" fill="%s" clip-path="url(#cp3)" %s>CONTINUOUS</text>'
           % (TS, T1_Y, R["murekkep"], bs, TS, T2_Y, R["murekkep"], bs, TS, T3_Y, R["logoSari"], bs))
    tw = [Y.genislik("Fredoka", 700, m, BASLIK_BOY) + 28 for m in ("PRESENT", "PERFECT", "CONTINUOUS")]
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                    % (n, n, TS - 14, y - BASLIK_BOY + 8, int(BASLIK_BOY * 1.35))
                    for n, y in ((1, T1_Y), (2, T2_Y), (3, T3_Y)))
    # cümle: iki satır, her satırın kendi kırpması; sözcük zamanlı açılır
    satir_metin, cw = [], []
    for k, idx in enumerate(SATIRLAR):
        satir_metin.append(" ".join(SOZ[i]["sozcuk"] for i in idx))
        clips += ('<clipPath id="cpc%d"><rect id="crc%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                  % (k, k, CUMLE_X - 12, CUMLE_Y[k] - CUMLE_BOY, int(CUMLE_BOY * 1.5)))
        for n, i in enumerate(idx):
            gen = Y.genislik("Caveat", 700, " ".join(SOZ[j]["sozcuk"] for j in idx[:n + 1]), CUMLE_BOY) + 8
            cw.append([k, SOZ[i]["t0"], min(SOZ[i]["t1"], SOZ[i]["t0"] + 0.5, 2.96), gen])
    cum = "".join('<text id="cm%d" x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" '
                  'fill="%s" clip-path="url(#cpc%d)">%s</text>'
                  % (k, CUMLE_X, CUMLE_Y[k], CUMLE_BOY, R["murekkep"], k, satir_metin[k]) for k in range(len(SATIRLAR)))
    # -ing halkası (satır 1, 2. sözcük)
    ing_x0 = CUMLE_X + Y.genislik("Caveat", 700, " ".join(w["sozcuk"] for w in SOZ[:2]) + " ", CUMLE_BOY)
    ing_w = Y.genislik("Caveat", 700, SOZ[2]["sozcuk"], CUMLE_BOY)
    hcx, hcy, hrx, hry = ing_x0 + ing_w / 2 + 12, CUMLE_Y[0] - 28, ing_w / 2 + 20, 46
    nok = []
    for k in range(49):
        u = k / 48
        aa = -2.4 + u * 1.06 * 2 * math.pi
        kk = 1 + 0.04 * math.sin(u * 9) + 0.06 * (u - 0.5)
        nok.append("%.1f %.1f" % (hcx + math.cos(aa) * hrx * kk, hcy + math.sin(aa) * hry * kk))
    halka = ('<path id="halka" fill="none" stroke="%s" stroke-width="10" stroke-linecap="round" '
             'stroke-linejoin="round" transform="rotate(-3 %.1f %.1f)" d="M %s" style="opacity:0"/>'
             % (R["vurgu"], hcx, hcy, " L ".join(nok)))
    w1 = Y.genislik("Fredoka", 700, "PRESENT ", 56)
    w2 = Y.genislik("Fredoka", 700, "PRESENT PERFECT ", 56)
    hedef = {"t1": [KENAR, 212, 56 / BASLIK_BOY], "t2": [KENAR + w1, 212, 56 / BASLIK_BOY],
             "t3": [KENAR + w2, 212, 56 / BASLIK_BOY],
             "roz": [0, HUD_ROZET_Y - ROZET_Y]}
    cipw = Y.genislik("Lexend", 700, "Hook", 40) + 64
    cip = ('<g id="ku-cip" style="opacity:0"><rect x="%.1f" y="48" width="%.1f" height="80" rx="40" fill="none" '
           'stroke="%s" stroke-width="4"/><text x="%.1f" y="102" text-anchor="middle" font-family="Lexend" '
           'font-weight="700" font-size="40" fill="%s">Hook</text></g>'
           % (1080 - KENAR - cipw, cipw, R["vurgu"], 1080 - KENAR - cipw / 2, R["vurgu"]))
    ders = ('<text id="ku-ders" x="%d" y="212" font-family="Fredoka" font-weight="700" font-size="56" '
            'fill="%s" style="opacity:0">PRESENT PERFECT CONTINUOUS</text>' % (KENAR, R["murekkep"]))
    alt = ('<text id="alt" x="540" y="%d" text-anchor="middle" font-family="Lexend" font-weight="500" '
           'font-size="44" fill="%s" style="opacity:0">Süreç mi, sonuç mu?</text>' % (ALT_Y, R["murekkep"]))
    veri = {"Z": Z, "fz": fz, "kz": kz, "nF": len(fig), "nK": len(kam), "hedef": hedef,
            "ts": TS, "t1y": T1_Y, "t2y": T2_Y, "t3y": T3_Y, "tw": tw, "cw": cw, "sw": sw,
            "hc": [0, HEDEF_CUMLE_Y[0] - CUMLE_Y[0]], "cx": CUMLE_X,
            "logo": [KENAR, 48, LOGO_W, LOGO_H]}
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
<g id="eskiz" fill="none" stroke="{R['murekkep']}" stroke-linecap="round" stroke-linejoin="round">
<g id="fig" transform="translate({FIG_X} {FIG_Y}) scale({FIG_S})" stroke-width="{sw / FIG_S:.3f}">{figs}</g>
<g id="kam"><g transform="translate({KAM_X} {KAM_Y}) rotate(-5 162 162) scale({KAM_S})" stroke-width="{4.0 / KAM_S:.3f}">{kams}</g></g>
</g>
{''.join(roz)}{tit}<g id="cg">{cum}{halka}</g>
<g id="lgs" style="opacity:0"><image id="logoimg" href="assets/logo.svg" x="{KENAR}" y="48" width="{LOGO_W:.2f}" height="{LOGO_H}"/></g>
{ders}{cip}{alt}
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
  for (var j = 0; j < V.nK; j++) darbe("k" + j, V.kz[j][0], V.kz[j][1]);
  darbe("halka", Z.halka[0], Z.halka[1]);

  // 0,0-0,4 logo damgası sol üstte (HUD yeri): ölçek 1,18->1,0, dönme -2 -> 0, alfa 0->1
  var lg = V.logo;
  gsap.set("#lgs", {{ svgOrigin: (lg[0] + lg[2] / 2) + " " + (lg[1] + lg[3] / 2) }});
  tl.fromTo("#lgs", {{ opacity: 0, scale: 1.18, rotation: -2 }},
    {{ opacity: 1, scale: 1, rotation: 0, duration: Z.logo_damga[1], ease: "power3.out", immediateRender: false }}, Z.logo_damga[0]);
  // 0,3-0,9 rozetler
  [0, 1].forEach(function (i) {{
    tl.fromTo("#rz" + i, {{ y: 26, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.rozet[0] + i * Z.rozet[1]);
  }});
  // 0,65-1,45 başlık kalemle: kırpma soldan sağa açılır
  [0, 1, 2].forEach(function (i) {{
    tl.fromTo("#cr" + (i + 1), {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.tw[i] }}, duration: Z.baslik[i][1], ease: "none", immediateRender: false }}, Z.baslik[i][0]);
  }});
  // 1,0-3,0 cümle konuşmayla yazılır (satır başına kırpma)
  var onceki = {{ 0: 0 }};
  V.cw.forEach(function (w) {{
    var hedef = w[3] + 12;
    tl.fromTo("#crc" + w[0], {{ attr: {{ width: onceki[w[0]] }} }}, {{ attr: {{ width: hedef }}, duration: w[2] - w[1], ease: "none", immediateRender: false }}, w[1]);
    onceki[w[0]] = hedef;
  }});
  // altyazı bandı: cümle 1 parçası (altyazi.json: 1,00 - 3,16)
  tl.set("#alt", ac({{ opacity: 1 }}), 0.95);
  gsap.set("#eskiz", {{ svgOrigin: "540 1200" }});

  // 2,1-3,0 uçuş: başlık -> ders adı, 1. rozet -> HUD rozeti, cümle -> sahne 02 yeri
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud, H = V.hedef;
  function uc2(id, ox, oy, h) {{
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, x: h[0] - ox, duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, y: h[1] - oy, duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, scale: h[2], duration: ud * 0.8, ease: "power3.out" }}), u0);
  }}
  uc2("#t1", V.ts, V.t1y, H.t1); uc2("#t3", V.ts, V.t2y, H.t2); uc2("#t2", V.ts, V.t3y, H.t3);
  tl.to("#t2", ac({{ fill: "{R['murekkep']}", duration: ud * 0.6, ease: "power1.inOut" }}), u0);
  tl.to("#rz0", ac({{ y: H.roz[1], duration: ud, ease: "power3.inOut" }}), u0);
  tl.to("#rz1", ac({{ opacity: 0, duration: 0.3, ease: "power1.in" }}), u0);
  tl.to("#cg", ac({{ y: V.hc[1], duration: Z.cumle_ucus[1], ease: "power3.inOut" }}), Z.cumle_ucus[0]);
  tl.to("#eskiz", ac({{ opacity: 0, scale: 1.06, duration: 0.4, ease: "power1.in" }}), u0 + 0.1);
  var son = u1 - 0.25;   // gerçek HUD metinleri son 0,25 sn'de belirir
  ["#t1", "#t2", "#t3"].forEach(function (s) {{ tl.to(s, ac({{ opacity: 0, duration: 0.25, ease: "power1.in" }}), son); }});
  tl.to("#ku-ders,#ku-cip", ac({{ opacity: 1, duration: 0.25, ease: "power1.out" }}), son);

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

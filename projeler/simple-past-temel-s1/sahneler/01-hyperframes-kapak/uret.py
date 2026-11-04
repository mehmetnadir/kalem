"""Sahne 01 kapak index.html üretici (DİKEY 1080x1920; 3 sn içerik + 12 kare geçiş = 102 kare).
Zamanlar: zamanlar.json (olay.py ile ortak); cümle 1 sözcük zamanları: ortak/anlatim/sozcukler.json.
Kapak kalıbı: başlık `-Dİ` / `= -ED` kalemle çizilir (230 px), figür + ev eskizi, Caveat cümle
konuşmayla yazılır, 2,0-3,0 sn'de başlık HUD çipine uçar, cümle yukarı çıkar, eskiz yerinde kalır."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
ALT = json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "altyazi.json").read_text())
SOZ = [w for w in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == 1]
TR = SOZ[:4]            # Dün akşam amcamlara gittim.
R = Y.RENK
CIP = "-Dİ = -ED"
SOL = 72
# BRIEF-DIKEY §3: kapak başlığı 190-230 px, 2 satır, kontur 12. Kısa başlık: ikisi de 230.
BASLIK = 230
T1_Y, T2_Y = 570, 790
BAS1, BAS2 = "-Dİ", "= -ED"
CUMLE_Y, CUMLE_BOY = 885, 80
KAYMA_Y = 440 - CUMLE_Y             # uçuşta cümle 885 -> 440 (sahne 02 kare 0 ile aynı)
# eskiz bandı y 950-1384: figür 430 px, ev kutusu 440 (görünür 330), zemin çizgisi y 1384
FIG_YUK = 430.0
FIG_X, FIG_Y = 230.0, 950.0
EV_KUTU = 440.0
EV_S, EV_X, EV_Y = EV_KUTU / 24, 480.0, 1384 - 21 * EV_KUTU / 24
ZEMIN_Y = 1384
# Kapak karesi t = 1,97 sn: cümlenin tamamı o ana kadar yazılmış olmalı. "gittim." sesten 0,34 sn
# önce yazılır (ses 2,20); kasıtlı sapma, RAPOR.md'de açıklı.
CW_T = [(1.00, 1.16), (1.24, 1.56), (1.64, 1.84), (1.84, 1.95)]


def yapi():
    gf, hf, fig = Y.peeps("standing-3", 60)
    ev = Y.tabler("home")
    fz = Y.cizgi_zamanlari([s["uz"] for s in fig], Z["figur"][0], Z["figur"][0] + Z["figur"][1])
    ez = Y.cizgi_zamanlari([40.0, 30.0, 20.0], Z["ev"][0], Z["ev"][0] + Z["ev"][1])
    return fig, ev, fz, ez


def uret():
    fig, ev, fz, ez = yapi()
    fig_s = FIG_YUK / 701.0
    sw = 4.4
    figs = "".join('<path id="f%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                   % (i, s["tx"], s["ty"], s["d"]) for i, s in enumerate(fig))
    evs = "".join('<path id="k%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(ev))
    bs = ('font-family="Fredoka" font-weight="700" font-size="%d" stroke="%s" stroke-width="12" '
          'stroke-linejoin="round" style="paint-order:stroke fill"')
    w1 = Y.genislik("Fredoka", 700, BAS1, BASLIK)
    w2 = Y.genislik("Fredoka", 700, BAS2, BASLIK)
    tit = ('<text id="t1" x="540" y="%d" text-anchor="middle" fill="%s" clip-path="url(#cp1)" %s>%s</text>'
           '<text id="t2" x="540" y="%d" text-anchor="middle" fill="%s" clip-path="url(#cp2)" %s>%s</text>'
           % (T1_Y, R["murekkep"], bs % (BASLIK, R["zemin"]), BAS1,
              T2_Y, R["logoSari"], bs % (BASLIK, R["zemin"]), BAS2))
    tw = [w1 + 80, w2 + 80]
    tx0 = [540 - w1 / 2 - 40, 540 - w2 / 2 - 40]
    tr_metin = " ".join(w["sozcuk"] for w in TR)
    cum_x = [SOL + Y.genislik("Caveat", 700, " ".join(w["sozcuk"] for w in TR[:i + 1]), CUMLE_BOY) + 8
             for i in range(len(TR))]
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%.1f" y="%d" width="0" height="%d"/>'
                    '</clipPath>' % (n, n, tx0[n - 1], y - BASLIK, int(BASLIK * 1.25))
                    for n, y in ((1, T1_Y), (2, T2_Y)))
    clips += ('<clipPath id="cp3"><rect id="cr3" x="%d" y="%d" width="0" height="%d"/></clipPath>'
              % (SOL - 12, CUMLE_Y - CUMLE_BOY, int(CUMLE_BOY * 1.5)))
    cum = ('<g id="cum"><text id="cm1" x="%d" y="%d" font-family="Caveat" font-weight="700" '
           'font-size="%d" fill="%s" clip-path="url(#cp3)">%s</text></g>'
           % (SOL, CUMLE_Y, CUMLE_BOY, R["murekkep"], tr_metin))
    # uçuş hedefleri: çip metninin iki parçasının merkezi (Lexend 40); başlık merkezden küçülür
    cx, cy, cw, ch = Y.cip_olcu(CIP)
    base = cy + ch / 2 + 14
    x0 = cx + Y.HUD["cipDolgu"] / 2
    p1 = Y.genislik("Lexend", 700, BAS1, Y.HUD["cipYazi"])
    sp = Y.genislik("Lexend", 700, " ", Y.HUD["cipYazi"])
    p2 = Y.genislik("Lexend", 700, BAS2, Y.HUD["cipYazi"])
    olcek = Y.HUD["cipYazi"] / BASLIK
    hedef = {"t1": [x0 + p1 / 2, base, olcek], "t2": [x0 + p1 + sp + p2 / 2, base, olcek]}
    kunye = Y.kunye_svg(CIP)
    alt_svg, alt_zaman = Y.altyazi_svg(0.0, Z["sure"], ALT)
    veri = {"Z": Z, "fz": fz, "ez": ez, "nF": len(fig), "nE": len(ev), "hedef": hedef,
            "sol": SOL, "t1y": T1_Y, "t2y": T2_Y, "tw": tw, "alt": alt_zaman, "zc": Z["zemin"],
            "kayma": KAYMA_Y,
            "logoc": "%.2f %.2f" % (Y.HUD["kenar"] + Y.HUD["logoYuk"] * Y.LOGO_EN_BOY / 2,
                                    Y.HUD["logoY"] + Y.HUD["logoYuk"] / 2),
            "cw": [[a, b, cum_x[i]] for i, (a, b) in enumerate(CW_T)]}
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
<g id="fig" transform="translate({FIG_X} {FIG_Y}) scale({fig_s:.5f})" stroke-width="{sw / fig_s:.3f}">{figs}</g>
<g id="evg" filter="url(#el)"><g transform="translate({EV_X} {EV_Y:.1f}) scale({EV_S:.4f})" stroke-width="{sw / EV_S:.3f}">{evs}</g></g>
<path id="zc" d="M96 {ZEMIN_Y} L560 {ZEMIN_Y - 2} L1000 {ZEMIN_Y}" stroke="{R['ikincil']}" stroke-opacity="0.75" stroke-width="4" style="opacity:0"/>
<g id="par" stroke="{R['vurgu']}" stroke-width="6" style="opacity:0">
<path d="M440 1010 l0 -44 M418 988 l44 0 M426 972 l28 32 M454 972 l-28 32"/>
<path d="M960 1040 l0 -36 M942 1022 l36 0"/><path d="M420 1290 l0 -34 M403 1273 l34 0"/></g>
</g>
{tit}{cum}
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
  for (var i = 0; i < V.nF; i++) darbe("f" + i, V.fz[i][0], V.fz[i][1]);
  for (var j = 0; j < V.nE; j++) darbe("k" + j, V.ez[j][0], V.ez[j][1]);
  darbe("zc", V.zc[0], V.zc[1]);
  // altyazı bandı: parça başında açılır, bitince (ya da sonraki parça başlarken) kapanır
  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]); tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});
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

  // uçuş 2,0-3,0: başlık -> çip, cümle yukarı
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud, H = V.hedef;
  function uc2(id, oy, h, ex) {{
    tl.to(id, ac({{ svgOrigin: "540 " + oy, x: h[0] - 540, duration: ud, ease: ex }}), u0);
    tl.to(id, ac({{ svgOrigin: "540 " + oy, y: h[1] - oy, duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: "540 " + oy, scale: h[2], duration: ud * 0.8, ease: "power3.out" }}), u0);
  }}
  uc2("#t1", V.t1y, H.t1, "power3.inOut"); uc2("#t2", V.t2y, H.t2, "power2.out");
  tl.to("#t2", ac({{ fill: "{R['murekkep']}", duration: ud * 0.6, ease: "power1.inOut" }}), u0);
  tl.to("#cum", ac({{ y: V.kayma, duration: ud, ease: "power3.inOut" }}), u0);
  // eskiz (figür + ev + zemin) yerinde kalır: sahne 02 aynı kareyi hazır çizili açar
  tl.fromTo("#par", {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.2, ease: "power3.out", immediateRender: false, svgOrigin: "540 1150" }}, u0);
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

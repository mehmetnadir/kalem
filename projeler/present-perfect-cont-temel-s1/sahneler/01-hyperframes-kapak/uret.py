"""Sahne 01 kapak index.html üretici (DİKEY 1080x1920; soğuk açılış, 3 sn içerik + 12 kare geçiş = 102 kare).
Present Perfect Continuous: İKİ SAATTİR / = HAVE BEEN; figür + dizüstü + saat eskizi.
Zamanlar: zamanlar.json (olay.py ile ortak); cümle 1 sözcük zamanları: ortak/anlatim/sozcukler.json.
Kapak kalıbı: başlık `İKİ SAATTİR` / `= HAVE BEEN` kalemle çizilir, figür + dizüstü + saat eskizi, Caveat cümle konuşmayla
yazılır (3 sn'e kadar ilk 3 sözcük; kalanı sahne 02'de), 2,0-3,0 sn'de başlık HUD çipine uçar, cümle içerik
bandının üstüne çıkar, eskiz (figür + otobüs) yerinde kalır."""
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
TR = SOZ[:3]            # İki saattir çalışıyorum. (kalan sahne 02)
R = Y.RENK
CIP = "= HAVE BEEN"          # logo 387 px: tam başlık çipe sığmaz (607 px); çip yalnız kalıp
SOL = 72
# Telefon ölçeği (BRIEF-DIKEY §3): başlık 2 satır, 984 px içine sığar (en az 150).
# Fredoka'da İ (U+0130) yok: tarayıcı yedek yazı tipine düşer; başlık "Fredoka, Lexend" yazılır, genişlik
# İ için Lexend ile ölçülür. Her satır 984 px içine sığacak boyda (en çok 190, en az 150).
GEN1, GEN2 = 1.0, 1.0               # ölçülen render genişliği / fontTools genişliği


def baslik_gen(metin, boy):
    """Başlık genişliği: İ harfleri Lexend, kalan Fredoka."""
    ni = metin.count("İ")
    return (Y.genislik("Fredoka", 700, metin.replace("İ", ""), boy)
            + ni * Y.genislik("Lexend", 700, "İ", boy))


BASLIK1 = max(150, min(190, int(970 * 100 / baslik_gen("İKİ SAATTİR", 100))))
BASLIK2 = max(150, min(190, int(970 * 100 / baslik_gen("= HAVE BEEN", 100))))
T1_Y = 560
T2_Y = 745
CUMLE1_Y, CUMLE_BOY = 850, 80
KAYMA_Y = -410                      # uçuşta cümle: 850 -> 440 (sahne 02 kare 0 ile aynı)
# eskiz bandı y 900-1380 (bant ortası): figür 480 px, ev 460 kutu (görünür 345 px), zemin çizgisi y 1384
FIG_S = 0.685
FIG_X, FIG_Y = 100.0, 900.0
EV_S, EV_X, EV_Y = 460 / 24, 300.0, 1000.0      # dizüstü (tabler/device-laptop), görünür x 357-703, y 1115-1364
SA_S, SA_X, SA_Y = 330 / 24, 690.0, 960.0        # saat (tabler/clock), görünür x 731-979, y 1001-1249
ZEMIN_Y = 1384
CAP = 0.36                          # cümle yazımı sözcük başına en çok 0,36 sn (kapak karesi 1,95 tam olsun)


def yapi():
    gf, hf, fig = Y.peeps("standing-2", 60)
    ev = Y.tabler("device-laptop")
    sa = Y.tabler("clock")
    fz = Y.cizgi_zamanlari([s["uz"] for s in fig], Z["figur"][0], Z["figur"][0] + Z["figur"][1])
    ez = Y.cizgi_zamanlari([18.0, 62.0], Z["ev"][0], Z["ev"][0] + Z["ev"][1])
    sz = Y.cizgi_zamanlari([57.0, 9.0], Z["saat"][0], Z["saat"][0] + Z["saat"][1])
    return fig, ev, sa, fz, ez, sz


def uret():
    fig, ev, sa, fz, ez, sz = yapi()
    sw = 4.4
    figs = "".join('<path id="f%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                   % (i, s["tx"], s["ty"], s["d"]) for i, s in enumerate(fig))
    evs = "".join('<path id="k%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(ev))
    sas = "".join('<path id="h%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(sa))
    bs = 'font-family="Fredoka, Lexend" font-weight="700" font-size="%d" stroke="%s" stroke-width="12" ' \
         'stroke-linejoin="round" style="paint-order:stroke fill"'
    w1 = baslik_gen("İKİ SAATTİR", BASLIK1) * GEN1     # gerçek render genişliği
    w2 = baslik_gen("= HAVE BEEN", BASLIK2) * GEN2
    t1x, t2x = (1080 - w1) / 2, (1080 - w2) / 2
    tit = ('<text id="t1" x="%.1f" y="%d" fill="%s" clip-path="url(#cp1)" %s>İKİ SAATTİR</text>'
           '<text id="t2" x="%.1f" y="%d" fill="%s" clip-path="url(#cp2)" %s>= HAVE BEEN</text>'
           % (t1x, T1_Y, R["murekkep"], bs % (BASLIK1, R["zemin"]),
              t2x, T2_Y, R["logoSari"], bs % (BASLIK2, R["zemin"])))
    tw1, tw2 = w1 * 1.1 + 40, w2 * 1.1 + 40   # ölçüm kerning/Ş farkı payı
    tr_metin = " ".join(w["sozcuk"] for w in TR)
    cum_x = [SOL + Y.genislik("Caveat", 700, " ".join(w["sozcuk"] for w in TR[:i + 1]), CUMLE_BOY) + 8
             for i in range(len(TR))]
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%.1f" y="%d" width="0" height="%d"/></clipPath>'
                    % (n, n, x - 12, y - b + 8, int(b * 1.35))
                    for n, y, x, b in ((1, T1_Y, t1x, BASLIK1), (2, T2_Y, t2x, BASLIK2)))
    for n, y in ((3, CUMLE1_Y),):
        clips += ('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                  % (n, n, SOL - 12, y - CUMLE_BOY, int(CUMLE_BOY * 1.5)))
    cum = ('<g id="cum"><text id="cm1" x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" '
           'fill="%s" clip-path="url(#cp3)">%s</text>'
           '</g>'
           % (SOL, CUMLE1_Y, CUMLE_BOY, R["murekkep"], tr_metin))
    # uçuş hedefleri: çip metninin iki parçası (Lexend 40); başlık satırları kendi boylarından küçülür
    cx, cy, cw, ch = Y.cip_olcu(CIP)
    base = cy + ch / 2 + 14
    x0 = cx + Y.HUD["cipDolgu"] / 2
    hedef = {"t1": [x0, base, Y.HUD["cipYazi"] / BASLIK1], "t2": [x0, base, Y.HUD["cipYazi"] / BASLIK2]}
    kunye = Y.kunye_svg(CIP)
    alt_svg, alt_zaman = Y.altyazi_svg(0.0, Z["sure"], ALT)
    veri = {"Z": Z, "fz": fz, "ez": ez, "nF": len(fig), "nE": len(ev), "nH": len(sa), "sz": sz, "hedef": hedef,
            "sol": SOL, "t1y": T1_Y, "t2y": T2_Y, "tw": [tw1, tw2],
            "t1x": t1x, "t2x": t2x, "alt": alt_zaman, "zc": Z["zemin"], "kayma": KAYMA_Y,
            "logoc": "%.2f %.2f" % (Y.HUD["kenar"] + Y.HUD["logoYuk"] * Y.LOGO_EN_BOY / 2, Y.HUD["logoY"] + Y.HUD["logoYuk"] / 2),
            "cw": [[w["t0"], min(w["t1"], w["t0"] + (0.2 if i == 2 else CAP), 2.98), cum_x[i]] for i, w in enumerate(TR)]}
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
<g id="evg" filter="url(#el)"><g transform="translate({EV_X} {EV_Y}) scale({EV_S})" stroke-width="{sw / EV_S:.3f}">{evs}</g>
<g transform="translate({SA_X} {SA_Y}) scale({SA_S})" stroke-width="{sw / SA_S:.3f}">{sas}</g></g>
<path id="zc" d="M96 {ZEMIN_Y} L560 {ZEMIN_Y - 2} L1000 {ZEMIN_Y}" stroke="{R['ikincil']}" stroke-opacity="0.75" stroke-width="4" style="opacity:0"/>
<g id="par" stroke="{R['vurgu']}" stroke-width="6" style="opacity:0">
<path d="M440 960 l0 -44 M418 938 l44 0 M426 922 l28 32 M454 922 l-28 32"/>
<path d="M1004 940 l0 -36 M986 922 l36 0"/><path d="M290 1060 l0 -34 M273 1043 l34 0"/></g>
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
  for (var h = 0; h < V.nH; h++) darbe("h" + h, V.sz[h][0], V.sz[h][1]);
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

  
  // uçuş 2,0-3,0: başlık -> çip, cümleler yukarı
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud, H = V.hedef;
  function uc2(id, ox, oy, h, ex) {{
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, x: h[0] - ox, duration: ud, ease: ex }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, y: h[1] - oy, duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: ox + " " + oy, scale: h[2], duration: ud * 0.8, ease: "power3.out" }}), u0);
  }}
  uc2("#t1", V.t1x, V.t1y, H.t1, "power3.inOut"); uc2("#t2", V.t2x, V.t2y, H.t2, "power2.out");
  tl.to("#t2", ac({{ fill: "{R['murekkep']}", duration: ud * 0.6, ease: "power1.inOut" }}), u0);
  tl.to("#t1", ac({{ opacity: 0, duration: ud * 0.45, ease: "power1.in" }}), u0 + ud * 0.35);
  tl.to("#cum", ac({{ y: V.kayma, duration: ud, ease: "power3.inOut" }}), u0);
  // eskiz (figür + dizüstü + saat + zemin) yerinde kalır: sahne 02 aynı kareyi hazır çizili açar
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

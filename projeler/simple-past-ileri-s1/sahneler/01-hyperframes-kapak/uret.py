"""Sahne 01 kapak index.html üretici (simple-past-ileri-s1; DİKEY 1080x1920; 3 sn içerik + 12 kare geçiş = 102 kare).
Zamanlar: zamanlar.json (olay.py ile ortak); cümle 1 sözcük zamanları: ortak/anlatim/sozcukler.json.
Kapak: başlık `AGO` / `= PAST` kalemle çizilir, altında cümle 1 yazılır (Ago görürsen / Present Perfect /
yazma.), alt bantta figür + saat. 2,0-2,65 sn uçuş: başlık sağ üst çipe (Trap) uçar, cümle satırları yukarı
çıkar; 3,04-3,28 `Perfect` üstüne kırmızı çizgi, 3,04-3,40 `yazma.` yazılır (son 12 kare geçiş altında).
Çip kapak bitene kadar gizlidir (kapak karesi t 1,97)."""
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
R = Y.RENK
CIP = "Trap"
SOL = 72
# başlık: "AGO" ~350 px, "= PAST" ~560 px (190 px yazıda; 984 px bandına sığar)
BASLIK1, BASLIK2 = 190, 190
T1_Y, T2_Y = 514, 724
# cümle satırları: kapak konumu -> uçuş sonrası konum (sahne 02 kare 0 ile aynı)
R1_BOY, R2_BOY = 88, 88
R1_Y, R2_Y = 830, 920
R1_SON, R2_SON, R3_Y = 500, 650, 800
CAP = 0.36                          # cümle yazımı sözcük başına en çok 0,36 sn
# alt bant (940-1392): figür 440 px (standing-3) + saat (tabler/clock; daire 360 px); zemin çizgisi y 1388
FIG_S = 0.628
FIG_X, FIG_Y = 150.0, 950.0
KT_S, KT_X, KT_Y = 20.0, 500.0, 950.0       # tabler/clock: görünür daire x 560-920, y 1010-1370
ZEMIN_Y = 1388
CAPRAZ_PAY = 12


def yapi():
    gf, hf, fig = Y.peeps("standing-3", 60)
    kt = Y.tabler("clock")
    fz = Y.cizgi_zamanlari([s["uz"] for s in fig], Z["figur"][0], Z["figur"][0] + Z["figur"][1])
    kz = Y.cizgi_zamanlari([float(len(d)) for d in kt], Z["kitap"][0], Z["kitap"][0] + Z["kitap"][1])
    return fig, kt, fz, kz


def capraz_yollari():
    """Kırmızı çizgi: `Perfect` sözcüğünün (uçuş sonrası konum) üstünde tek, hafif eğik çizgi."""
    a = Y.genislik("Fredoka", 700, "Present ", R2_BOY)
    b = Y.genislik("Fredoka", 700, "Present Perfect", R2_BOY)
    x0, x1 = SOL + a - CAPRAZ_PAY, SOL + b + CAPRAZ_PAY
    return ["M%.1f %d L%.1f %d" % (x0, R2_SON - 20, x1, R2_SON - 42)]


def uret():
    fig, kt, fz, kz = yapi()
    sw, sk = 4.4, 4.0                  # kalınlık: figür 4,4 · nesne 4,0 (BRIEF-DIKEY §3)
    figs = "".join('<path id="f%d" transform="translate(%.2f %.2f)" d="%s" style="opacity:0"/>'
                   % (i, s["tx"], s["ty"], s["d"]) for i, s in enumerate(fig))
    kts = "".join('<path id="k%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(kt))
    cr = capraz_yollari()
    capr = "".join('<path id="x%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(cr))
    bs = 'font-family="Fredoka" font-weight="700" font-size="%d" stroke="%s" stroke-width="12" ' \
         'stroke-linejoin="round" style="paint-order:stroke fill"'
    w1 = Y.genislik("Fredoka", 700, "AGO", BASLIK1)
    w2 = Y.genislik("Fredoka", 700, "= PAST", BASLIK2)
    t1x, t2x = (1080 - w1) / 2, (1080 - w2) / 2
    tit = ('<g id="t1" clip-path="url(#cp1)"><text x="%.1f" y="%d" fill="%s" %s>AGO</text></g>'
           '<text id="t2" x="%.1f" y="%d" fill="%s" clip-path="url(#cp2)" %s>= PAST</text>'
           % (t1x, T1_Y, R["murekkep"], bs % (BASLIK1, R["zemin"]),
              t2x, T2_Y, R["vurgu"], bs % (BASLIK2, R["zemin"])))
    tw1, tw2 = w1 * 1.15 + 40, w2 * 1.15 + 40   # ölçüm kerning/Ş farkı payı
    # satır 1: Ago görürsen (Caveat); satır 2: Present Perfect (Fredoka); satır 3: yazma. (Caveat)
    s_tr, s_pp, s_deme = SOZ[:2], SOZ[2:4], SOZ[4]
    r1_x = [SOL + Y.genislik("Caveat", 700, " ".join(w["sozcuk"] for w in s_tr[:i + 1]), R1_BOY) + 8
            for i in range(len(s_tr))]
    r1_x[-1] += 16
    r2_x = [SOL + Y.genislik("Fredoka", 700, " ".join(w["sozcuk"] for w in s_pp[:i + 1]), R2_BOY) + 8
            for i in range(len(s_pp))]
    r2_x[-1] += 16
    clips = "".join('<clipPath id="cp%d"><rect id="cr%d" x="%.1f" y="%d" width="0" height="%d"/></clipPath>'
                    % (n, n, x - 12, y - b + 8, int(b * 1.35))
                    for n, y, x, b in ((1, T1_Y, t1x, BASLIK1), (2, T2_Y, t2x, BASLIK2)))
    for n, y, b in ((3, R1_Y, R1_BOY), (4, R2_Y, R2_BOY), (5, R3_Y, R1_BOY)):
        clips += ('<clipPath id="cp%d"><rect id="cr%d" x="%d" y="%d" width="0" height="%d"/></clipPath>'
                  % (n, n, SOL - 12, y - b, int(b * 1.5)))
    satirlar = ('<g id="r1"><text x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" '
                'fill="%s" clip-path="url(#cp3)">%s</text></g>'
                '<g id="r2"><text x="%d" y="%d" font-family="Fredoka" font-weight="700" font-size="%d" '
                'fill="%s" clip-path="url(#cp4)">%s</text></g>'
                '<text id="r3" x="%d" y="%d" font-family="Caveat" font-weight="700" font-size="%d" '
                'fill="%s" clip-path="url(#cp5)">%s</text>'
                % (SOL, R1_Y, R1_BOY, R["murekkep"], " ".join(w["sozcuk"] for w in s_tr),
                   SOL, R2_Y, R2_BOY, R["murekkep"], " ".join(w["sozcuk"] for w in s_pp),
                   SOL, R3_Y, R1_BOY, R["murekkep"], s_deme["sozcuk"]))
    r3w = Y.genislik("Caveat", 700, s_deme["sozcuk"], R1_BOY) + 24
    # uçuş hedefi: çip merkezi (başlık satırları küçülüp çipe girer)
    cx, cy, cw, ch = Y.cip_olcu(CIP)
    hedef = [cx + cw / 2, cy + ch / 2]
    kunye = Y.kunye_svg(CIP)
    alt_svg, alt_zaman = Y.altyazi_svg(0.0, Z["sure"], ALT)
    veri = {"Z": Z, "fz": fz, "kz": kz, "nF": len(fig), "nK": len(kt), "hedef": hedef,
            "sol": SOL, "t1y": T1_Y, "t2y": T2_Y, "tw": [tw1, tw2], "t1x": t1x, "t2x": t2x,
            "t1c": [t1x + w1 / 2, T1_Y - BASLIK1 * 0.35], "t2c": [t2x + w2 / 2, T2_Y - BASLIK2 * 0.35],
            "alt": alt_zaman, "r3w": r3w, "r1k": R1_SON - R1_Y, "r2k": R2_SON - R2_Y,
            "logoc": "%.2f %.2f" % (Y.HUD["kenar"] + Y.HUD["logoYuk"] * Y.LOGO_EN_BOY / 2,
                                    Y.HUD["logoY"] + Y.HUD["logoYuk"] / 2),
            "cw": [[w["t0"], min(w["t1"], w["t0"] + CAP), r1_x[i]] for i, w in enumerate(s_tr)],
            "cw2": [[w["t0"], min(w["t1"], w["t0"] + CAP), r2_x[i]] for i, w in enumerate(s_pp)],
            "zc": Z["zemin"]}
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
<g id="ktg"><g transform="translate({KT_X} {KT_Y}) scale({KT_S})" stroke-width="{sk / KT_S:.3f}">{kts}</g></g>
<path id="zc" d="M96 {ZEMIN_Y} L560 {ZEMIN_Y - 2} L1000 {ZEMIN_Y}" stroke-width="4" style="opacity:0"/>
</g>
{satirlar}
<g id="capraz" fill="none" stroke="{R['kirmizi']}" stroke-width="12" stroke-linecap="round">{capr}</g>
{tit}
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
  for (var j = 0; j < V.nK; j++) darbe("k" + j, V.kz[j][0], V.kz[j][1]);
  darbe("zc", V.zc[0], V.zc[1]);
  // altyazı bandı: parça başında açılır, bitince (ya da sonraki parça başlarken) kapanır
  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]); tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});
  gsap.set("#ku-cip", {{ opacity: 0 }});
  gsap.set("#ku-cipt", {{ opacity: 0 }});

  // ders adı + logo damgası + rozet
  tl.fromTo("#ku-ders", {{ opacity: 0 }}, {{ opacity: 1, duration: Z.ders[1], ease: "power1.out", immediateRender: false }}, Z.ders[0]);
  gsap.set("#ku-logo", {{ svgOrigin: V.logoc }});
  tl.fromTo("#ku-logo", {{ opacity: 0, scale: 1.18, rotation: -2 }},
    {{ opacity: 1, scale: 1, rotation: 0, duration: Z.logo_damga[1], ease: "power3.out", immediateRender: false }}, Z.logo_damga[0]);
  ["#rz0", "#rz1"].forEach(function (id, i) {{
    tl.fromTo(id, {{ y: 26, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.rozet[0] + i * Z.rozet[1]);
  }});
  // başlık kalemle çizilir (kırpma soldan sağa)
  [0, 1].forEach(function (i) {{
    tl.fromTo("#cr" + (i + 1), {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.tw[i] }}, duration: Z.baslik[i][1], ease: "none", immediateRender: false }}, Z.baslik[i][0]);
  }});
  // cümle 1: Ago görürsen, Present Perfect (sözcük zamanlı), yazma.
  var onceki = 0;
  V.cw.forEach(function (w) {{
    tl.fromTo("#cr3", {{ attr: {{ width: onceki }} }}, {{ attr: {{ width: w[2] - V.sol + 12 }}, duration: w[1] - w[0], ease: "none", immediateRender: false }}, w[0]);
    onceki = w[2] - V.sol + 12;
  }});
  var onceki2 = 0;
  V.cw2.forEach(function (w) {{
    tl.fromTo("#cr4", {{ attr: {{ width: onceki2 }} }}, {{ attr: {{ width: w[2] - V.sol + 12 }}, duration: w[1] - w[0], ease: "none", immediateRender: false }}, w[0]);
    onceki2 = w[2] - V.sol + 12;
  }});
  tl.fromTo("#cr5", {{ attr: {{ width: 0 }} }}, {{ attr: {{ width: V.r3w }}, duration: Z.deme[1], ease: "none", immediateRender: false }}, Z.deme[0]);

  // uçuş 2,0-2,65: başlık satırları çipe uçar ve küçülür, cümle satırları yukarı çıkar
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud, H = V.hedef;
  function uc2(id, o, hs) {{
    tl.to(id, ac({{ svgOrigin: o[0] + " " + o[1], x: H[0] - o[0], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: o[0] + " " + o[1], y: H[1] - o[1], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ svgOrigin: o[0] + " " + o[1], scale: hs, duration: ud * 0.85, ease: "power3.out" }}), u0);
    tl.to(id, ac({{ opacity: 0, duration: 0.18, ease: "power1.in" }}), u1 - 0.2);
  }}
  uc2("#t1", V.t1c, 0.1); uc2("#t2", V.t2c, 0.1);
  tl.to("#r1", ac({{ y: V.r1k, duration: ud, ease: "power3.inOut" }}), u0);
  tl.to("#r2", ac({{ y: V.r2k, duration: ud, ease: "power3.inOut" }}), u0);
  tl.to("#ku-cip", ac({{ opacity: 1, duration: 0.2, ease: "power1.out" }}), u1 - 0.22);
  tl.to("#ku-cipt", ac({{ opacity: 1, duration: 0.2, ease: "power1.out" }}), u1 - 0.18);
  // kırmızı çizgi: Perfect üstünde tek hızlı çizgi (3,04-3,28)
  darbe("x0", Z.capraz[0], Z.capraz[1]);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, fig, kt, fz, kz


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html, *_ = uret()
    (AD / "proje" / "index.html").write_text(html)
    print("index.html yazıldı", len(html))

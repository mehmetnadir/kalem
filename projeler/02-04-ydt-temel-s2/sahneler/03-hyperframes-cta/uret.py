"""Sahne 03 CTA index.html ve zamanlar.json üretici (02-04-ydt-temel-s2 huni v2; DİKEY 1080×1920).
Cümle 4 ses olayları ve kinetik sözcükler. Kanal katmanı ve künye; içerik bandı 460–1380; altyazı 1400–1550.
DUZ4 (16.11, J3 A1 + A9): altyazı karaokesi (sahne 08 `altyazi_svg` üç değer + `V.karaoke` kalıbı); altyazı x 60–960."""
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(
    s for s in json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))["sahneler"]
    if s["klasor"] == AD.name
)
T_BAS: float = SAH["t_bas"]  # 22.75
KARE: int = SAH["kare"]      # 230
SURE: float = round(KARE / 30, 4)  # 7.6667
SOZ: List[Dict[str, Any]] = [
    w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w["cumle"] == 4
]
ALT: List[Dict[str, Any]] = [
    a for a in json.loads((PAKET / "ortak" / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
    if a.get("cumle") == 4
]
R = Y.RENK


def T(i: int, bas: str = "") -> float:
    """Cümle 4, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = w["sozcuk"]
        assert val.lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, val, bas)
    return float(w["t0"])


def E(i: int, bas: str = "") -> float:
    """Cümle 4, i. sözcüğün t1'i (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = w["sozcuk"]
        assert val.lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, val, bas)
    return float(w["t1"])


# Sözcük assert'leri ile 8 sözcüğün sırası baştan doğrulanır
BEKLENEN_SOZLER: List[Tuple[int, str]] = [
    (0, "Bitmedi"), (1, "gel"), (2, "Dersin"), (3, "tamamı"),
    (4, "YDS"), (5, "Publishing"), (6, "YouTube"), (7, "kanalında")
]
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)


def uret() -> Tuple[str, Dict[str, Any]]:
    """index.html ve zamanlar verisini üretir."""
    # 1. Giriş sözleri ölçüleri
    w_bitmedi_bos = Y.genislik("Fredoka", 700, "Bitmedi, ", 96)
    x_gel = 60.0 + w_bitmedi_bos
    w_gel = Y.genislik("Fredoka", 700, "gel.", 96)
    assert 60.0 + w_bitmedi_bos + w_gel <= 960, "Bitmedi, gel. sağ ucu 960'ı aşıyor"

    # 2. Hap ve YouTube satırı ölçüleri
    hw = Y.genislik("Lexend", 700, "@ydspublishing", 64) + 2 * 20
    yt_x = 60.0 + hw + 14.0
    w_yt = Y.genislik("Lexend", 700, "· YouTube", 64)
    assert yt_x + w_yt <= 958, f"YouTube satırının sağ ucu 958'i aşıyor: {yt_x + w_yt}"

    # 3. Zamanlar ve Olaylar
    def y_sn(t_kuresel: float) -> float:
        return round(t_kuresel - T_BAS, 4)

    zamanlar: Dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "bitmedi_giris": [y_sn(T(0, "Bitmedi")), 0.22],
        "gel_giris": [y_sn(T(1, "gel")), 0.22],
        "kapak_giris": [y_sn(T(2, "Dersin")), 0.4],
        "hap_giris": [y_sn(T(4, "YDS")), 0.3],
        "youtube_giris": [y_sn(T(6, "YouTube")), 0.22],
        "olaylar": [
            [y_sn(T(0, "Bitmedi")), "tik", 0.4],
            [y_sn(T(1, "gel")), "tik", 0.45],
            [y_sn(T(2, "Dersin")), "vurus", 0.7],
            [y_sn(T(4, "YDS")), "tik", 0.6],
            [y_sn(T(6, "YouTube")), "tik", 0.4],
        ],
    }

    # 4. Altyazı ve Künye
    kunye_svg = Y.kunye_svg()
    alt_svg, alt_zaman, karaoke_zaman = Y.altyazi_svg(T_BAS, SURE, ALT)   # DUZ4 A1: sahne 08 biçimi

    hap_cx = round(60.0 + hw / 2.0, 2)
    hap_cy = 1210.0

    veri: Dict[str, Any] = {
        "Z": zamanlar,
        "hap_cx": hap_cx,
        "hap_cy": hap_cy,
        "alt": alt_zaman,
        "karaoke": karaoke_zaman,
    }

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
/* kapak teması: "#root" + ".tema-acik" bitişik yazılmaz; hf_tema.py o dizgiyi "çevrildi" sayıp tema CSS'ini atlar */
#kapak-acik{{display:none}}
.tema-acik #kapak-acik{{display:inline}}.tema-acik #kapak-koyu{{display:none}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{SURE}"
  data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>
<clipPath id="cpkapak"><rect x="60" y="627" width="900" height="506" rx="24"/></clipPath>
</defs>

<!-- Giriş sözü -->
<text id="tx_bitmedi" x="60" y="572" font-family="Fredoka" font-weight="700"
  font-size="96" fill="#f3efe6" style="opacity:0">Bitmedi,</text>
<text id="tx_gel" x="{x_gel:.1f}" y="572" font-family="Fredoka" font-weight="700"
  font-size="96" fill="#f3efe6" style="opacity:0">gel.</text>

<!-- Kapak kartı grubu -->
<g id="kapakg" style="opacity:0">
<g clip-path="url(#cpkapak)">
<image id="kapak-acik" href="assets/ana-kapak.png" x="60" y="627" width="900" height="506"
  preserveAspectRatio="xMidYMid slice"/>
<image id="kapak-koyu" href="assets/ana-kapak-koyu.png" x="60" y="627" width="900" height="506"
  preserveAspectRatio="xMidYMid slice"/>
</g>
<rect id="kapak-cerceve" x="60" y="627" width="900" height="506" rx="24"
  fill="none" stroke="#f3efe6" stroke-width="3"/>
</g>

<!-- Hap grubu -->
<g id="hapg" style="opacity:0">
<rect id="hap" x="60" y="1170" width="{hw:.1f}" height="80" rx="40" fill="#f2a93b"/>
<text id="tx_hap" x="80" y="1232" font-family="Lexend" font-weight="700"
  font-size="64" fill="#1b1a17">@ydspublishing</text>
</g>

<!-- YouTube satırı -->
<text id="tx_youtube" x="{yt_x:.1f}" y="1232" font-family="Lexend" font-weight="700"
  font-size="64" fill="#f3efe6" style="opacity:0">· YouTube</text>

{kunye_svg}<g id="altyazi">{alt_svg}</g>
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var V = {json.dumps(veri)};
  var Z = V.Z;
  var $ = function (s) {{ return document.querySelector(s); }};
  var tl = gsap.timeline({{ paused: true }});

  function ac(o) {{ o.immediateRender = false; return o; }}

  function kinetik(id, bas) {{
    tl.fromTo(id, {{ opacity: 0, y: 24 }},
      {{ opacity: 1, y: 0, duration: 0.22, ease: "back.out(1.6)", immediateRender: false }}, bas);
  }}

  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});

  V.karaoke.forEach(function (k) {{
    var id = "#" + k[0], ac_t = k[1], kapat_t = k[2], uz = k[3];
    var el = $(id);
    if (el) {{
      el.style.strokeDasharray = uz + " " + (uz + 2);
      el.style.strokeDashoffset = uz;
      tl.set(id, ac({{ opacity: 1 }}), ac_t);
      tl.fromTo(id, {{ strokeDashoffset: uz }},
        {{ strokeDashoffset: 0, duration: 0.15, ease: "power2.out", immediateRender: false }}, ac_t);
      tl.set(id, ac({{ opacity: 0 }}), kapat_t);
    }}
  }});

  kinetik("#tx_bitmedi", Z.bitmedi_giris[0]);
  kinetik("#tx_gel", Z.gel_giris[0]);

  gsap.set("#kapakg", {{ svgOrigin: "510 880" }});
  tl.fromTo("#kapakg", {{ opacity: 0, scale: 0.96 }},
    {{ opacity: 1, scale: 1, duration: 0.4, ease: "power3.out", immediateRender: false }}, Z.kapak_giris[0]);

  gsap.set("#hapg", {{ svgOrigin: V.hap_cx + " " + V.hap_cy }});
  tl.fromTo("#hapg", {{ opacity: 0, scale: 0.9 }},
    {{ opacity: 1, scale: 1, duration: 0.3, ease: "power3.out", immediateRender: false }}, Z.hap_giris[0]);

  kinetik("#tx_youtube", Z.youtube_giris[0]);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html, zamanlar


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_cikti, z_cikti = uret()
    (AD / "proje" / "index.html").write_text(html_cikti, encoding="utf-8")
    (AD / "zamanlar.json").write_text(json.dumps(z_cikti, ensure_ascii=False, indent=2), encoding="utf-8")
    print("proje/index.html yazıldı:", len(html_cikti), "karakter")
    print("zamanlar.json yazıldı:", len(z_cikti["olaylar"]), "ses olayı")

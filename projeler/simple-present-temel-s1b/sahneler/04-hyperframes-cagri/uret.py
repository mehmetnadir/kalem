"""simple-present-temel-s1 sahne 04 Çağrı (HyperFrames, DİKEY 1080x1920, huni v2).

Kapak kartı, kinetik giriş, çağrı hapı, YouTube ve altyazı üretimi.
Kaynak: 02-04-ydt-temel-s1 sahne 03-hyperframes-cta (v2) kopyası; zaman zaman.json + sozcukler.json çapasından.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(
    s for s in json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))["sahneler"]
    if s["klasor"] == AD.name
)
T_BAS: float = float(SAH["t_bas"])  # 17.74
KARE: int = int(SAH["kare"])        # 218
SURE: float = round(KARE / 30, 4)   # 7.2667

# Kapak dosyaları kontrolü
KAPAK_ACIK = PAKET / "ortak" / "kapak" / "ana-kapak.png"
KAPAK_KOYU = PAKET / "ortak" / "kapak" / "ana-kapak-koyu.png"
if not KAPAK_ACIK.exists():
    raise SystemExit(f"ana kapak bekliyor: {KAPAK_ACIK}")
if not KAPAK_KOYU.exists():
    raise SystemExit(f"ana kapak bekliyor: {KAPAK_KOYU}")

SOZ: list[dict[str, Any]] = [
    w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 4
]
ALT: list[dict[str, Any]] = [
    p for p in json.loads((PAKET / "ortak" / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
    if p.get("cumle") == 4
]
R = Y.RENK


def yerel(t: float) -> float:
    """Küresel saniyeyi sahne yerel saniyesine çevirir."""
    return round(t - T_BAS, 3)


def T(i: int, bas: str = "") -> float:
    """Cümle 4, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = str(w["sozcuk"])
        assert val.lower().startswith(bas.lower()), f"sözcük {i}: {val!r}, beklenen {bas!r}"
    return float(w["t0"])


def E(i: int, bas: str = "") -> float:
    """Cümle 4, i. sözcüğün t1'i (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = str(w["sozcuk"])
        assert val.lower().startswith(bas.lower()), f"sözcük {i}: {val!r}, beklenen {bas!r}"
    return float(w["t1"])


# Sözcük sıralaması doğrulaması
BEKLENEN_SOZLER: list[tuple[int, str]] = [
    (0, "Gerisi"),
    (1, "bizde"),
    (2, "Dersin"),
    (3, "tamamı"),
    (4, "YDS"),
    (5, "Publishing"),
    (6, "YouTube"),
    (7, "kanalında"),
]
assert len(SOZ) == 8, f"Cümle 4 için 8 sözcük bekleniyor, {len(SOZ)} bulundu"
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)
assert len(ALT) == 2, f"Cümle 4 için 2 altyazı parçası bekleniyor, {len(ALT)} bulundu"


def uret() -> tuple[str, dict[str, Any]]:
    """Sahne 03 index.html ve zamanlar.json verisini üretir."""
    # Kinetik yazı boyutu
    g_boy = 96
    while g_boy >= 64:
        w_toplam = Y.genislik("Fredoka", 700, "Gerisi bizde.", g_boy)
        if 60.0 + w_toplam <= 960.0:
            break
        g_boy -= 1
    assert g_boy >= 64, f"G_BOY 64'ten küçük olamaz: {g_boy}"

    bizde_x = 60.0 + Y.genislik("Fredoka", 700, "Gerisi ", g_boy)

    # Hap ölçüleri: @ydspublishing (Lexend 700, 56)
    hap_metin = "@ydspublishing"
    w_hap_metin = Y.genislik("Lexend", 700, hap_metin, 56)
    hap_w = w_hap_metin + 2.0 * 28.0
    hap_cx = 60.0 + hap_w / 2.0

    # YouTube: · YouTube (Lexend 700, 56)
    yt_x = 60.0 + hap_w + 18.0
    yt_w = Y.genislik("Lexend", 700, "· YouTube", 56)
    assert yt_x + yt_w <= 960.0, f"YouTube sağ sınırı aştı: {yt_x + yt_w:.1f} > 960"

    t_kart = 0.0
    t_gerisi = yerel(T(0, "Gerisi"))
    t_bizde = yerel(T(1, "bizde"))
    t_hap = yerel(T(4, "YDS"))
    t_yt = yerel(T(6, "YouTube"))
    t_kuyruk = yerel(E(7, "kanalında"))

    zamanlar: dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "kart_giris": [t_kart, 0.50],
        "gerisi_giris": [t_gerisi, 0.22],
        "bizde_giris": [t_bizde, 0.22],
        "hap_giris": [t_hap, 0.30],
        "youtube_giris": [t_yt, 0.30],
        "kuyruk_durgun": [t_kuyruk, round(SURE - t_kuyruk, 3)],
        "olaylar": [
            [0.40, "vurus", 0.6],
            [t_gerisi, "tik", 0.4],
            [t_hap, "tik", 0.6],
            [t_yt, "tik", 0.4],
        ],
        "olay_listesi": [
            {
                "olay": "kart_giris",
                "kare": round(t_kart * 30),
                "yerel": t_kart,
                "kuresel": round(T_BAS, 3),
                "sozcuk": "sahne başı",
            },
            {
                "olay": "gerisi_giris",
                "kare": round(t_gerisi * 30),
                "yerel": t_gerisi,
                "kuresel": T(0, "Gerisi"),
                "sozcuk": "Gerisi",
            },
            {
                "olay": "bizde_giris",
                "kare": round(t_bizde * 30),
                "yerel": t_bizde,
                "kuresel": T(1, "bizde"),
                "sozcuk": "bizde.",
            },
            {
                "olay": "hap_giris",
                "kare": round(t_hap * 30),
                "yerel": t_hap,
                "kuresel": T(4, "YDS"),
                "sozcuk": "YDS",
            },
            {
                "olay": "youtube_giris",
                "kare": round(t_yt * 30),
                "yerel": t_yt,
                "kuresel": T(6, "YouTube"),
                "sozcuk": "YouTube",
            },
            {
                "olay": "kuyruk_durgun",
                "kare": round(t_kuyruk * 30),
                "yerel": t_kuyruk,
                "kuresel": E(7, "kanalında"),
                "sozcuk": "kanalında.",
            },
        ],
    }

    alt_svg, alt_zaman, karaoke_zaman = Y.altyazi_svg(T_BAS, SURE, ALT)
    kunye_svg = Y.kunye_svg()

    veri = {
        "Z": {
            "kart_giris": zamanlar["kart_giris"],
            "gerisi_giris": zamanlar["gerisi_giris"],
            "bizde_giris": zamanlar["bizde_giris"],
            "hap_giris": zamanlar["hap_giris"],
            "youtube_giris": zamanlar["youtube_giris"],
        },
        "alt": alt_zaman,
        "karaoke": karaoke_zaman,
    }

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{SURE}"
 data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>
<clipPath id="kart-kirp"><rect x="60" y="620" width="900" height="506" rx="24"/></clipPath>
</defs>

<!-- Kapak kartı (16:9) -->
<g id="kart" style="opacity:0">
<image id="kapakimg" href="assets/ana-kapak.png" x="60" y="620" width="900" height="506"
 preserveAspectRatio="xMidYMid slice" clip-path="url(#kart-kirp)"/>
<rect x="62" y="622" width="896" height="502" rx="22" fill="none" stroke="{R['murekkep']}" stroke-width="4"/>
</g>

<!-- Kinetik metinler -->
<text id="gerisi" x="60" y="560" font-family="Fredoka" font-weight="700"
 font-size="{g_boy}" fill="{R['murekkep']}" style="opacity:0">Gerisi</text>
<text id="bizde" x="{bizde_x:.1f}" y="560" font-family="Fredoka" font-weight="700"
 font-size="{g_boy}" fill="{R['murekkep']}" style="opacity:0">bizde.</text>

<!-- Çağrı hapı ve YouTube -->
<g id="hap" style="opacity:0">
<rect x="60" y="1160" width="{hap_w:.1f}" height="80" rx="40" fill="{R['vurgu']}"/>
<text x="{hap_cx:.1f}" y="1220" text-anchor="middle" font-family="Lexend" font-weight="700"
 font-size="56" fill="{R['zemin']}">@ydspublishing</text>
</g>
<text id="yt" x="{yt_x:.1f}" y="1220" font-family="Lexend" font-weight="700"
 font-size="56" fill="{R['murekkep']}" style="opacity:0">· YouTube</text>

<!-- Künye ve kanal katmanı -->
{kunye_svg}

<!-- Altyazı -->
<g id="altyazi">{alt_svg}</g>
</svg>
</div>
<script>
(function () {{
  var root = document.getElementById("root");
  var img = document.getElementById("kapakimg");
  var p1 = new Image(); p1.src = "assets/ana-kapak.png";
  var p2 = new Image(); p2.src = "assets/ana-kapak-koyu.png";
  function k() {{
    if (!img || !root) return;
    var acik = root.classList.contains("tema-acik");
    img.setAttribute("href", acik ? "assets/ana-kapak.png" : "assets/ana-kapak-koyu.png");
  }}
  k();
  if (root && window.MutationObserver) {{
    new MutationObserver(k).observe(root, {{ attributes: true, attributeFilter: ["class"] }});
  }}
}})();
</script>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var V = {json.dumps(veri)};
  var Z = V.Z;
  var $ = function (s) {{ return document.querySelector(s); }};
  var tl = gsap.timeline({{ paused: true }});

  function ac(o) {{ o.immediateRender = false; return o; }}

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

  gsap.set("#kart", {{ svgOrigin: "510 873" }});
  tl.fromTo("#kart", {{ scale: 0.94 }},
    {{ scale: 1, duration: 0.50, ease: "power3.out", immediateRender: false }}, 0.0);
  tl.fromTo("#kart", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.25, ease: "power2.out", immediateRender: false }}, 0.0);

  tl.fromTo("#gerisi", {{ opacity: 0, y: 24 }},
    {{ opacity: 1, y: 0, duration: 0.22, ease: "back.out(1.6)", immediateRender: false }}, Z.gerisi_giris[0]);
  tl.fromTo("#bizde", {{ opacity: 0, y: 24 }},
    {{ opacity: 1, y: 0, duration: 0.22, ease: "back.out(1.6)", immediateRender: false }}, Z.bizde_giris[0]);

  gsap.set("#hap", {{ svgOrigin: "60 1200" }});
  tl.fromTo("#hap", {{ opacity: 0, scale: 0.9 }},
    {{ opacity: 1, scale: 1, duration: 0.30, ease: "back.out(1.6)", immediateRender: false }}, Z.hap_giris[0]);

  tl.fromTo("#yt", {{ opacity: 0, x: -12 }},
    {{ opacity: 1, x: 0, duration: 0.30, ease: "power3.out", immediateRender: false }}, Z.youtube_giris[0]);

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

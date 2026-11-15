"""simple-present-temel-s2b (A/B kol b, değişken kapanis) sahne 04 Çağrı (HyperFrames, DİKEY 1080x1920, huni v2).

Kapak kartı, kinetik giriş, çağrı hapı, YouTube ve altyazı üretimi.
Kaynak: 02-04-ydt-temel-s1 sahne 03-hyperframes-cta (v2) kopyası; ana kapak iki <image> + tema CSS'i.
Kol a'dan fark (KBC-0202S2): giriş `Konu burada bitmiyor.` (kol a `Bitmedi, gel.`), 3 kinetik adım, yazı boyu 900 px'e sığan.
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
T_BAS: float = float(SAH["t_bas"])  # 19.07
KARE: int = int(SAH["kare"])        # 230
SURE: float = round(KARE / 30, 4)   # 7.6667

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
    (0, "Konu"),
    (1, "burada"),
    (2, "bitmiyor"),
    (3, "Dersin"),
    (4, "tamamı"),
    (5, "YDS"),
    (6, "Publishing"),
    (7, "YouTube"),
    (8, "kanalında"),
]
assert len(SOZ) == 9, f"Cümle 4 için 9 sözcük bekleniyor, {len(SOZ)} bulundu"
GIRIS: list[str] = ["Konu", "burada", "bitmiyor."]  # kinetik adımlar = sözcük 0-2
GIRIS_ID: list[str] = ["konu", "burada", "bitmiyor"]  # öğe kimlikleri ve zamanlar anahtarı (<id>_giris)
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)
assert len(ALT) == 2, f"Cümle 4 için 2 altyazı parçası bekleniyor, {len(ALT)} bulundu"


def uret() -> tuple[str, dict[str, Any]]:
    """Sahne 03 index.html ve zamanlar.json verisini üretir."""
    # Kinetik yazı boyutu
    g_boy = 96
    while g_boy >= 64:
        w_toplam = Y.genislik("Fredoka", 700, " ".join(GIRIS), g_boy)
        if 60.0 + w_toplam <= 960.0:
            break
        g_boy -= 1
    assert g_boy >= 64, f"G_BOY 64'ten küçük olamaz: {g_boy}"

    # sözcük x'leri: önceki sözcükler + boşluk ölçüsü (tek satır, sol 60)
    giris_x = [60.0 + Y.genislik("Fredoka", 700, " ".join(GIRIS[:k]) + " ", g_boy) if k else 60.0
               for k in range(len(GIRIS))]
    giris_svg = "\n".join(
        f'<text id="{GIRIS_ID[k]}" x="{giris_x[k]:.1f}" y="560" font-family="Fredoka" font-weight="700"\n'
        f' font-size="{g_boy}" fill="{R["murekkep"]}" style="opacity:0">{GIRIS[k]}</text>'
        for k in range(len(GIRIS))
    )

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
    t_giris = [yerel(T(k, GIRIS[k].rstrip("."))) for k in range(len(GIRIS))]
    t_hap = yerel(T(5, "YDS"))
    t_yt = yerel(T(7, "YouTube"))
    t_kuyruk = yerel(E(8, "kanalında"))

    zamanlar: dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "kart_giris": [t_kart, 0.50],
        **{f"{GIRIS_ID[k]}_giris": [t_giris[k], 0.22] for k in range(len(GIRIS))},
        "hap_giris": [t_hap, 0.30],
        "youtube_giris": [t_yt, 0.30],
        "kuyruk_durgun": [t_kuyruk, round(SURE - t_kuyruk, 3)],
        "olaylar": [
            [0.40, "vurus", 0.6],
            [t_giris[0], "tik", 0.4],
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
            *[
                {
                    "olay": f"{GIRIS_ID[k]}_giris",
                    "kare": round(t_giris[k] * 30),
                    "yerel": t_giris[k],
                    "kuresel": T(k, GIRIS[k].rstrip(".")),
                    "sozcuk": GIRIS[k],
                }
                for k in range(len(GIRIS))
            ],
            {
                "olay": "hap_giris",
                "kare": round(t_hap * 30),
                "yerel": t_hap,
                "kuresel": T(5, "YDS"),
                "sozcuk": "YDS",
            },
            {
                "olay": "youtube_giris",
                "kare": round(t_yt * 30),
                "yerel": t_yt,
                "kuresel": T(7, "YouTube"),
                "sozcuk": "YouTube",
            },
            {
                "olay": "kuyruk_durgun",
                "kare": round(t_kuyruk * 30),
                "yerel": t_kuyruk,
                "kuresel": E(8, "kanalında"),
                "sozcuk": "kanalında.",
            },
        ],
    }

    alt_svg, alt_zaman, karaoke_zaman = Y.altyazi_svg(T_BAS, SURE, ALT)
    kunye_svg = Y.kunye_svg()

    veri = {
        "Z": {
            "kart_giris": zamanlar["kart_giris"],
            **{f"{g}_giris": zamanlar[f"{g}_giris"] for g in GIRIS_ID},
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
/* ana kapak teması: "#root" + ".tema-acik" bitişik yazılmaz (hf_tema.py o dizgiyi "çevrildi" sayar) */
#kapakA{{display:none}}
.tema-acik #kapakA{{display:inline}}.tema-acik #kapakK{{display:none}}
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
<image id="kapakA" href="assets/ana-kapak.png" x="60" y="620" width="900" height="506"
 preserveAspectRatio="xMidYMid slice" clip-path="url(#kart-kirp)"/>
<image id="kapakK" href="assets/ana-kapak-koyu.png" x="60" y="620" width="900" height="506"
 preserveAspectRatio="xMidYMid slice" clip-path="url(#kart-kirp)"/>
<rect x="62" y="622" width="896" height="502" rx="22" fill="none" stroke="{R['murekkep']}" stroke-width="4"/>
</g>

<!-- Kinetik metinler -->
{giris_svg}

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

  {json.dumps(GIRIS_ID)}.forEach(function (g) {{
    tl.fromTo("#" + g, {{ opacity: 0, y: 24 }},
      {{ opacity: 1, y: 0, duration: 0.22, ease: "back.out(1.6)", immediateRender: false }}, Z[g + "_giris"][0]);
  }});

  gsap.set("#hap", {{ svgOrigin: "60 1200" }});
  tl.fromTo("#hap", {{ opacity: 0, scale: 0.9 }},
    {{ opacity: 1, scale: 1, duration: 0.30, ease: "back.out(1.6)", immediateRender: false }}, Z.hap_giris[0]);

  tl.fromTo("#yt", {{ opacity: 0, x: -12 }},
    {{ opacity: 1, x: 0, duration: 0.30, ease: "power3.out", immediateRender: false }}, Z.youtube_giris[0]);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    assert "#root.tema-acik" not in html, "hf_tema.py tema CSS'ini atlar (sözleşme 15.11)"
    return html, zamanlar


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_cikti, z_cikti = uret()
    (AD / "proje" / "index.html").write_text(html_cikti, encoding="utf-8")
    (AD / "zamanlar.json").write_text(json.dumps(z_cikti, ensure_ascii=False, indent=2), encoding="utf-8")
    print("proje/index.html yazıldı:", len(html_cikti), "karakter")
    print("zamanlar.json yazıldı:", len(z_cikti["olaylar"]), "ses olayı")

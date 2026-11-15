"""02-04-ydt-temel-s1 sahne 08 Kaydet (HyperFrames, DİKEY 1080x1920, huni v2).

Kural özeti kartı, yer imi çizimi, Kaydet hapı ve altyazı üretimi.
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
T_BAS: float = float(SAH["t_bas"])  # 19.99
KARE: int = int(SAH["kare"])        # 177
SURE: float = round(KARE / 30, 4)   # 5.9

SOZ: list[dict[str, Any]] = [
    w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 3
]
ALT: list[dict[str, Any]] = [
    p for p in json.loads((PAKET / "ortak" / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
    if p.get("cumle") == 3
]


def yerel(t: float) -> float:
    """Küresel saniyeyi sahne yerel saniyesine çevirir."""
    return round(t - T_BAS, 3)


def T(i: int, bas: str = "") -> float:
    """Cümle 3, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = str(w["sozcuk"])
        assert val.lower().startswith(bas.lower()), f"sözcük {i}: {val!r}, beklenen {bas!r}"
    return float(w["t0"])


def E(i: int, bas: str = "") -> float:
    """Cümle 3, i. sözcüğün t1'i (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = str(w["sozcuk"])
        assert val.lower().startswith(bas.lower()), f"sözcük {i}: {val!r}, beklenen {bas!r}"
    return float(w["t1"])


# Sözcük sıralaması doğrulaması
BEKLENEN_SOZLER: list[tuple[int, str]] = [
    (0, "Bu"),
    (1, "üç"),
    (2, "farktan"),
    (3, "yalnız"),
    (4, "biri"),
    (5, "Sınavdan"),
    (6, "önce"),
    (7, "lazım"),
    (8, "olacak"),
    (9, "Kaydet"),
]
assert len(SOZ) == 10, f"Cümle 3 için 10 sözcük bekleniyor, {len(SOZ)} bulundu"
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)
assert len(ALT) == 2, f"Cümle 3 için 2 altyazı parçası bekleniyor, {len(ALT)} bulundu"


def kart_kenar_yolu() -> str:
    """Elle çizilmiş kart kenarı yolu (tek M, 3 ara noktalı kenarlar, sol üstte bindirme)."""
    kay = [1.6, -1.2, 2.2, -0.8, 1.0, -2.0, 0.6, 1.8, -1.4, 0.4, -2.2, 1.2]
    noktalar: list[tuple[float, float]] = [
        (86.0, 616.0),
        (293.0, 616.0 + kay[0]),
        (510.0, 616.0 + kay[1]),
        (727.0, 616.0 + kay[2]),
        (944.0, 616.0),
        (944.0 + kay[3], 703.0),
        (944.0 + kay[4], 790.0),
        (944.0 + kay[5], 877.0),
        (944.0, 964.0),
        (727.0, 964.0 + kay[6]),
        (510.0, 964.0 + kay[7]),
        (293.0, 964.0 + kay[8]),
        (76.0, 964.0),
        (76.0 + kay[9], 877.0),
        (max(74.0, 76.0 + kay[10]), 790.0),
        (76.0 + kay[11], 703.0),
        (76.0, 616.0),
        (100.0, 616.0),
    ]
    for p in noktalar:
        assert 74.0 <= p[0] <= 946.0, f"kart-kenar x sınırı dışı: {p}"
        assert 614.0 <= p[1] <= 966.0, f"kart-kenar y sınırı dışı: {p}"
    return "M " + f"{noktalar[0][0]:.1f} {noktalar[0][1]:.1f}" + " " + " ".join(
        f"L {p[0]:.1f} {p[1]:.1f}" for p in noktalar[1:]
    )


def uret() -> tuple[str, dict[str, Any]]:
    """Sahne 08 index.html ve zamanlar.json verisini üretir."""
    # Kural satırları ölçüsü: B = 76'dan 64'e inerek üç satırın en büyüğü <= 800 olan ilk boy
    # DUZ2 (15.11, J2 A3): kural fiil sınırı taşır (durum fiilinde genelleme yanlış: I have a cold this week).
    satir0 = "Live, work fiillerinde:"
    satir1 = "kalıcıysa geniş zaman,"
    satir2 = "geçiciyse şimdiki zaman."
    for _s in (satir0, satir1, satir2):
        assert len(_s) <= 24, f"Satır 24 karakterden uzun: {len(_s)} {_s!r}"
    assert len("üç farktan biri") <= 24
    assert len("Kaydet") <= 24

    b_boy = 76
    w_satir_max = 0.0
    while b_boy >= 64:
        w_satir_max = max(Y.genislik("Fredoka", 700, s, b_boy) for s in (satir0, satir1, satir2))
        if w_satir_max <= 800.0:
            break
        b_boy -= 1
    assert b_boy >= 64, f"B boyutu 64'ten küçük olamaz: {b_boy}"
    assert 110.0 + w_satir_max <= 910.0, f"Satır sonu 910'u aştı: {110.0 + w_satir_max:.1f}"

    a_aralik = round(1.32 * b_boy)
    t0 = round(790 - a_aralik + 0.32 * b_boy)
    t1 = t0 + a_aralik
    t2 = t1 + a_aralik
    # Kart iç kenarı (kalem yolu) y 616–964: üst satır tepesi ve alt satır kuyruğu en az 32 px içeride
    assert t0 - 0.75 * b_boy >= 616 + 32, f"Satır 0 kart üst kenarına yakın: {t0}"
    assert t2 + 0.25 * b_boy <= 964 - 32, f"Satır 2 kart alt kenarına yakın: {t2}"

    # Kalem kenarı yolu
    kenar_d = kart_kenar_yolu()

    # Kaydet grubu ölçüleri (§7)
    hap_w = Y.genislik("Fredoka", 700, "Kaydet", 64) + 80.0
    ikon_en = 67.0
    ara = 24.0
    grup_en = ikon_en + ara + hap_w
    gx = 510.0 - grup_en / 2.0
    tx = gx + 3.5 - 30.0
    hap_x = gx + ikon_en + ara
    hap_cx = hap_x + hap_w / 2.0
    assert gx >= 60.0 and gx + grup_en <= 960.0, f"Kaydet grubu sınır dışı: {gx:.1f}..{gx+grup_en:.1f}"

    # Zamanlamalar (§4)
    t_kart = yerel(T(0, "Bu"))
    t_uc = yerel(T(1, "üç"))
    t_imi = yerel(T(9, "Kaydet"))
    t_hap = round(yerel(T(9, "Kaydet")) + 0.10, 3)
    t_kuyruk = 5.50
    assert t_hap + 0.30 <= 5.50, f"Hap girişi son 12 kareye sarktı: {t_hap + 0.30}"

    zamanlar: dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "kart_giris": [t_kart, 0.45],
        "uc_giris": [t_uc, 0.30],
        "imi_ciz": [t_imi, 0.30],
        "hap_giris": [t_hap, 0.30],
        "kuyruk_durgun": [t_kuyruk, round(SURE - t_kuyruk, 3)],
        "olaylar": [
            [t_kart, "vurus", 0.5],
            [t_imi, "cizgi", 0.6],
            [t_hap, "tik", 0.5],
        ],
        "olay_listesi": [
            {
                "olay": "kart_giris",
                "kare": round(t_kart * 30),
                "yerel": t_kart,
                "kuresel": T(0, "Bu"),
                "sozcuk": "Bu,",
            },
            {
                "olay": "uc_giris",
                "kare": round(t_uc * 30),
                "yerel": t_uc,
                "kuresel": T(1, "üç"),
                "sozcuk": "üç",
            },
            {
                "olay": "imi_ciz",
                "kare": round(t_imi * 30),
                "yerel": t_imi,
                "kuresel": T(9, "Kaydet"),
                "sozcuk": "Kaydet.",
            },
            {
                "olay": "hap_giris",
                "kare": round(t_hap * 30),
                "yerel": t_hap,
                "kuresel": round(T(9, "Kaydet") + 0.10, 3),
                "sozcuk": "Kaydet.",
            },
            {
                "olay": "kuyruk_durgun",
                "kare": round(t_kuyruk * 30),
                "yerel": t_kuyruk,
                "kuresel": round(T_BAS + t_kuyruk, 3),
                "sozcuk": "sahne sonu",
            },
        ],
    }

    alt_svg, alt_zaman, karaoke_zaman = Y.altyazi_svg(T_BAS, SURE, ALT)
    kunye_svg = Y.kunye_svg()

    veri = {
        "Z": {
            "kart_giris": zamanlar["kart_giris"],
            "uc_giris": zamanlar["uc_giris"],
            "imi_ciz": zamanlar["imi_ciz"],
            "hap_giris": zamanlar["hap_giris"],
            "kuyruk_durgun": zamanlar["kuyruk_durgun"],
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
.tema-acik #kagit{{fill:#fffdf8;}}
#root #kart-kenar{{stroke:var(--pilMetin,#1b1a17);}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{SURE}"
 data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">

<!-- Üst yazı -->
<text id="uc" x="60" y="528" font-family="Lexend" font-weight="700" font-size="48"
 fill="#f3efe6" fill-opacity="0.7" style="opacity:0">üç farktan biri</text>

<!-- Kart grubu -->
<g id="kart" style="opacity:0">
<rect id="kagit" x="61" y="601" width="898" height="378" rx="22"
 fill="#fff9e6" stroke="#c9c2b3" stroke-width="2"/>
<path id="kart-kenar" d="{kenar_d}" fill="none" stroke="#1b1a17" stroke-width="4.5"
 stroke-linecap="round" stroke-linejoin="round"/>
<text id="kural0" x="110" y="{t0}" font-family="Fredoka" font-weight="700"
 font-size="{b_boy}" fill="#1b1a17">{satir0}</text>
<text id="kural1" x="110" y="{t1}" font-family="Fredoka" font-weight="700"
 font-size="{b_boy}" fill="#1b1a17">{satir1}</text>
<text id="kural2" x="110" y="{t2}" font-family="Fredoka" font-weight="700"
 font-size="{b_boy}" fill="#1b1a17">{satir2}</text>
</g>

<!-- Kaydet grubu -->
<g id="kaydet">
<g id="kaydet-ikon" transform="translate({tx:.1f} 1020) scale(5)" fill="none" stroke="#f3efe6"
 stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">
<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z" style="opacity:0"/>
</g>
<g id="kaydet-hap" style="opacity:0">
<rect x="{hap_x:.1f}" y="1036" width="{hap_w:.1f}" height="88" rx="44" fill="#f2a93b"/>
<text x="{hap_cx:.1f}" y="1102" text-anchor="middle" font-family="Fredoka" font-weight="700"
 font-size="64" fill="#1b1a17">Kaydet</text>
</g>
</g>

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

  gsap.set("#kart", {{ svgOrigin: "510 790" }});
  tl.fromTo("#kart", {{ scale: 0.96 }},
    {{ scale: 1, duration: 0.45, ease: "power3.out", immediateRender: false }}, Z.kart_giris[0]);
  tl.fromTo("#kart", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.45, ease: "power3.out", immediateRender: false }}, Z.kart_giris[0]);

  tl.fromTo("#uc", {{ opacity: 0, y: 16 }},
    {{ opacity: 1, y: 0, duration: 0.30, ease: "power3.out", immediateRender: false }}, Z.uc_giris[0]);

  var el = $("#kaydet-imi");
  if (el) {{
    var L = el.getTotalLength();
    el.style.strokeDasharray = L + " " + (L + 2);
    el.style.strokeDashoffset = L;
    tl.set(el, ac({{ opacity: 1 }}), Z.imi_ciz[0]);
    tl.fromTo(el, {{ strokeDashoffset: L }},
      {{ strokeDashoffset: 0, duration: 0.30, ease: "sine.inOut", immediateRender: false }}, Z.imi_ciz[0]);
  }}

  gsap.set("#kaydet-hap", {{ svgOrigin: "{hap_cx:.1f} 1080" }});
  tl.fromTo("#kaydet-hap", {{ opacity: 0, scale: 0.9 }},
    {{ opacity: 1, scale: 1, duration: 0.30, ease: "back.out(1.6)", immediateRender: false }}, Z.hap_giris[0]);

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

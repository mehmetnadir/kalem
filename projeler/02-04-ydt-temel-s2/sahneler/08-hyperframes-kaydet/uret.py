"""02-04-ydt-temel-s2 sahne 08 Kaydet (HyperFrames, DİKEY 1080x1920, huni v2).

Kural kartı, Today hapı dönüşümü, yer imi çizimi ve Kaydet metni.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
for _p in ("/usr/local/lib/python3.10/dist-packages", str(Path.home() / ".local/lib/python3.10/site-packages")):
    if _p not in sys.path:
        sys.path.append(_p)
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(
    s for s in json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))["sahneler"]
    if s["klasor"] == AD.name
)
T_BAS: float = float(SAH["t_bas"])  # 17.41
KARE: int = int(SAH["kare"])        # 172
SURE: float = round(KARE / 30, 4)   # 5.7333

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


# Sözcük çapaları (§3)
BEKLENEN_SOZLER: list[tuple[int, str]] = [
    (0, "Bu"),
    (1, "üç"),
    (2, "farktan"),
    (3, "yalnız"),
    (4, "biri"),
    (5, "Bu"),
    (6, "kuralı"),
    (7, "kaybetme"),
    (8, "Kaydet"),
]
assert len(SOZ) == 9, f"Cümle 3 için 9 sözcük bekleniyor, {len(SOZ)} bulundu"
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)
assert len(ALT) == 2, f"Cümle 3 için 2 altyazı parçası bekleniyor, {len(ALT)} bulundu"


def uret() -> tuple[str, dict[str, Any]]:
    """Sahne 08 index.html ve zamanlar.json verisini üretir."""
    satir_today = "Today"
    satir1 = "iki zamanda"
    satir2 = "da geçebilir;"
    satir3 = "farkı anlam yapar."
    satir_kaydet = "Kaydet"

    assert len(f"{satir_today} {satir1}") <= 24, "Satır 1 24 karakterden uzun"
    assert len(satir2) <= 24, f"Satır 2 24 karakterden uzun: {len(satir2)}"
    assert len(satir3) <= 24, f"Satır 3 24 karakterden uzun: {len(satir3)}"
    assert len(satir_kaydet) <= 24, f"Kaydet 24 karakterden uzun: {len(satir_kaydet)}"

    # Ölçüler (§5)
    hw = Y.genislik("Fredoka", 700, satir_today, 72) + 44.0
    s1x = 102.0 + hw + 20.0
    b1, b2, b3 = 703, 803, 903

    bookmark_svg = (AD / "cizim" / "bookmark.svg").read_text(encoding="utf-8")
    yollar = re.findall(r'<path d="([^"]+)"', bookmark_svg)
    assert yollar, "bookmark.svg içinde path bulunamadı"
    yerimi_d = yollar[0]
    assert yerimi_d.startswith("M18 7v14"), f"Yer imi yolu beklenmeyen biçimde: {yerimi_d}"

    s_oran = 140.0 / 18.0
    ix = 102.0 - 6.0 * s_oran
    iy = 1120.0 - 3.0 * s_oran
    ir = 102.0 + 12.0 * s_oran
    kx = round(ir + 3.0 + 36.0, 1)
    sw_imi = round(6.0 / s_oran, 4)

    # Sınır denetimleri (§7 kural 6, 8)
    w_s1 = Y.genislik("Fredoka", 700, satir1, 72)
    w_s3 = Y.genislik("Fredoka", 700, satir3, 72)
    w_kaydet = Y.genislik("Fredoka", 700, satir_kaydet, 96)

    assert 102.0 + hw + 20.0 + w_s1 <= 920.0, f"s1 sağ sınır taştı: {102.0 + hw + 20.0 + w_s1}"
    assert 124.0 + w_s3 <= 920.0, f"s3 sağ sınır taştı: {124.0 + w_s3}"
    assert kx + w_kaydet <= 960.0, f"Kaydet sağ sınır taştı: {kx + w_kaydet}"
    assert b1 - 64 >= 562 + 16, f"B1 - 64 kart çerçevesine çok yakın: {b1 - 64}"
    assert b3 + 20 <= 998 - 16, f"B3 + 20 kart çerçevesine çok yakın: {b3 + 20}"
    assert 1120.0 <= iy + 3.0 * s_oran and iy + 21.0 * s_oran <= 1260.0 + 1e-4, "Yer imi y aralığı dışı"
    assert 1224 < 1380, "Kaydet tabanı 1380 altında olmalı"

    # Zamanlamalar (§4)
    t_kart = yerel(T(0, "Bu"))
    t_nokta = yerel(T(1, "üç"))
    t_imi = yerel(T(6, "kuralı"))
    t_kaydet = yerel(T(8, "Kaydet"))
    t_kuyruk = round((KARE - 12) / 30, 4)

    assert t_kaydet + 0.30 <= (KARE - 12) / 30, f"Kaydet girişi son 12 kareye sarktı: {t_kaydet + 0.30}"

    zamanlar: dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "kart_giris": [t_kart, 0.40],
        "nokta_giris": [t_nokta, 0.46],
        "imi_ciz": [t_imi, 0.50],
        "kaydet_giris": [t_kaydet, 0.30],
        "kuyruk_durgun": [t_kuyruk, round(SURE - t_kuyruk, 4)],
        "olaylar": [
            [t_kart, "vurus", 0.5],
            [t_nokta, "tik", 0.4],
            [t_imi, "cizgi", 0.6],
            [t_kaydet, "tik", 0.6],
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
                "olay": "nokta_giris",
                "kare": round(t_nokta * 30),
                "yerel": t_nokta,
                "kuresel": T(1, "üç"),
                "sozcuk": "üç",
            },
            {
                "olay": "imi_ciz",
                "kare": round(t_imi * 30),
                "yerel": t_imi,
                "kuresel": T(6, "kuralı"),
                "sozcuk": "kuralı",
            },
            {
                "olay": "kaydet_giris",
                "kare": round(t_kaydet * 30),
                "yerel": t_kaydet,
                "kuresel": T(8, "Kaydet"),
                "sozcuk": "Kaydet.",
            },
            {
                "olay": "kuyruk_durgun",
                "kare": round(t_kuyruk * 30),
                "yerel": t_kuyruk,
                "kuresel": round(T_BAS + t_kuyruk, 3),
                "sozcuk": "geçiş",
            },
        ],
    }

    alt_svg, alt_zaman, karaoke_zaman = Y.altyazi_svg(T_BAS, SURE, ALT)
    kunye_svg = Y.kunye_svg()

    veri = {
        "Z": {
            "kart_giris": zamanlar["kart_giris"],
            "nokta_giris": zamanlar["nokta_giris"],
            "imi_ciz": zamanlar["imi_ciz"],
            "kaydet_giris": zamanlar["kaydet_giris"],
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
#root #imi-dolgu{{fill:var(--vurguDolgu,#f2a93b);}}
/* açık temada pilMetin = mürekkep (#1b2440): Today yazısı geçişsiz kalır (karşılıklı solma kaplamayı %75'e indiriyordu) */
.tema-acik #today-yazi{{opacity:1 !important;}}.tema-acik #today-yazi2{{display:none;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{SURE}"
 data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">

<!-- Kart grubu -->
<g id="kart" style="opacity:0">
<rect id="kart-crv" x="62" y="562" width="896" height="436" rx="32"
 fill="none" stroke="#f3efe6" stroke-width="4"/>
<g id="today-hap">
<rect id="today-kutu" x="102" y="{b1 - 64}" width="{hw:.1f}" height="88" rx="44"
 fill="#f2a93b"/>
<rect id="today-cerceve" x="102" y="{b1 - 64}" width="{hw:.1f}" height="88" rx="44"
 fill="none" stroke="#f3efe6" stroke-width="3" style="opacity:0"/>
<text id="today-yazi" x="124" y="{b1}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#1b1a17">{satir_today}</text>
<text id="today-yazi2" x="124" y="{b1}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#f3efe6" style="opacity:0">{satir_today}</text>
</g>
<text id="s1" x="{s1x:.1f}" y="{b1}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#f3efe6">{satir1}</text>
<text id="s2" x="124" y="{b2}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#f3efe6">{satir2}</text>
<text id="s3" x="124" y="{b3}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#f3efe6">{satir3}</text>
</g>

<!-- Noktalar -->
<g id="noktalar">
<circle id="nokta0" cx="115" cy="1040" r="13" fill="#f3efe6" style="opacity:0"/>
<circle id="nokta1" cx="159" cy="1040" r="11" fill="none" stroke="#f3efe6" stroke-width="4" style="opacity:0"/>
<circle id="nokta2" cx="203" cy="1040" r="11" fill="none" stroke="#f3efe6" stroke-width="4" style="opacity:0"/>
</g>

<!-- Yer imi grubu -->
<g id="yerimi" transform="translate({ix:.4f} {iy:.4f}) scale({s_oran:.6f})">
<path id="imi-dolgu" d="{yerimi_d}" fill="#f2a93b" stroke="none" style="opacity:0"/>
<path id="imi-cizgi" d="{yerimi_d}" fill="none" stroke="#f3efe6" stroke-width="{sw_imi:.4f}"
 stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>
</g>

<!-- Kaydet yazısı -->
<text id="kaydet-yazi" x="{kx:.1f}" y="1224" font-family="Fredoka" font-weight="700"
 font-size="96" fill="#f3efe6" style="opacity:0">{satir_kaydet}</text>

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

  gsap.set("#kart", {{ svgOrigin: "510 780" }});
  tl.fromTo("#kart", {{ scale: 0.96 }},
    {{ scale: 1, duration: 0.40, ease: "power3.out", immediateRender: false }}, Z.kart_giris[0]);
  tl.fromTo("#kart", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.40, ease: "power3.out", immediateRender: false }}, Z.kart_giris[0]);

  ["#nokta0", "#nokta1", "#nokta2"].forEach(function (id, idx) {{
    var t = Z.nokta_giris[0] + idx * 0.08;
    tl.fromTo(id, {{ opacity: 0, y: 12 }},
      {{ opacity: 1, y: 0, duration: 0.30, ease: "power3.out", immediateRender: false }}, t);
  }});

  var el = $("#imi-cizgi");
  if (el) {{
    var L = el.getTotalLength();
    el.style.strokeDasharray = L + " " + (L + 2);
    el.style.strokeDashoffset = L;
    tl.set(el, ac({{ opacity: 1 }}), Z.imi_ciz[0]);
    tl.fromTo(el, {{ strokeDashoffset: L }},
      {{ strokeDashoffset: 0, duration: 0.50, ease: "sine.inOut", immediateRender: false }}, Z.imi_ciz[0]);
  }}

  tl.fromTo("#kaydet-yazi", {{ opacity: 0, y: 24 }},
    {{ opacity: 1, y: 0, duration: 0.30, ease: "power3.out", immediateRender: false }}, Z.kaydet_giris[0]);
  tl.fromTo("#imi-dolgu", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.kaydet_giris[0]);
  tl.fromTo("#today-kutu", {{ opacity: 1 }},
    {{ opacity: 0, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.kaydet_giris[0]);
  tl.fromTo("#today-yazi", {{ opacity: 1 }},
    {{ opacity: 0, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.kaydet_giris[0]);
  tl.fromTo("#today-cerceve", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.kaydet_giris[0]);
  tl.fromTo("#today-yazi2", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.kaydet_giris[0]);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    assert "#root" + ".tema-acik" not in html, "hf_tema bu dizgeyi 'çevrildi' sayar; açık tema koyu çıkar"
    return html, zamanlar


if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_cikti, z_cikti = uret()
    (AD / "proje" / "index.html").write_text(html_cikti, encoding="utf-8")
    (AD / "zamanlar.json").write_text(json.dumps(z_cikti, ensure_ascii=False, indent=2), encoding="utf-8")
    print("proje/index.html yazıldı:", len(html_cikti), "karakter")
    print("zamanlar.json yazıldı:", len(z_cikti["olaylar"]), "ses olayı")

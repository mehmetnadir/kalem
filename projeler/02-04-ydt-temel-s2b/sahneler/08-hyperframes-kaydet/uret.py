"""02-04-ydt-temel-s2b sahne 08 Kaydet, kol b (HyperFrames, DİKEY 1080x1920, huni v2; A/B değişkeni `kapanis`).

Kol a (02-04-ydt-temel-s2) kopyası. Kart, üç nokta, kanal katmanı, künye kol a ile aynı. Kol b farkı (KBC-0204S2, 15.11):
kaydet kalıbı `Ekran görüntüsü al, sınav günü bak.`; yer imi yerine vizör (cizim/vizor.svg), `Kaydet` yerine üç parça yazı.
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
    (5, "Ekran"),
    (6, "görüntüsü"),
    (7, "al"),
    (8, "sınav"),
    (9, "günü"),
    (10, "bak"),
]
assert len(SOZ) == 11, f"Cümle 3 için 11 sözcük bekleniyor, {len(SOZ)} bulundu"
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)
assert len(ALT) == 2, f"Cümle 3 için 2 altyazı parçası bekleniyor, {len(ALT)} bulundu"


def uret() -> tuple[str, dict[str, Any]]:
    """Sahne 08 index.html ve zamanlar.json verisini üretir."""
    satir_today = "Today"
    satir1 = "iki zamanda"
    satir2 = "da geçebilir;"
    satir3 = "farkı anlam yapar."
    # Kol b kalıbı: satır 1 = parça 1 + parça 2, satır 2 = parça 3; her parça kendi sözcük çapasında gelir
    parca1, parca2, parca3 = "Ekran görüntüsü", "al,", "sınav günü bak."

    assert len(f"{satir_today} {satir1}") <= 24, "Satır 1 24 karakterden uzun"
    assert len(satir2) <= 24, f"Satır 2 24 karakterden uzun: {len(satir2)}"
    assert len(satir3) <= 24, f"Satır 3 24 karakterden uzun: {len(satir3)}"
    assert len(f"{parca1} {parca2}") <= 24, f"Kalıp satır 1 24 karakterden uzun: {parca1} {parca2}"
    assert len(parca3) <= 24, f"Kalıp satır 2 24 karakterden uzun: {parca3}"

    # Ölçüler (§5)
    hw = Y.genislik("Fredoka", 700, satir_today, 72) + 44.0
    s1x = 102.0 + hw + 20.0
    b1, b2, b3 = 703, 803, 903

    # Vizör (cizim/vizor.svg, 140×140, elle yazılan yol): kutu x 102–242, y 1120–1260 (kol a yer imi bandı)
    vizor_svg = (AD / "cizim" / "vizor.svg").read_text(encoding="utf-8")
    kose_d = re.findall(r'<path d="([^"]+)"', vizor_svg)
    assert len(kose_d) == 4, f"vizor.svg içinde 4 köşe yolu bekleniyor, {len(kose_d)} bulundu"
    assert '<rect x="24" y="24" width="92" height="92" rx="12"' in vizor_svg, "vizor.svg deklanşör karesi yok"
    vx, vy, vk = 102.0, 1120.0, 140.0
    kx = round(vx + vk + 39.0, 1)  # 281,0
    kb1, kb2 = 1176, 1256
    x_parca2 = round(kx + Y.genislik("Fredoka", 700, f"{parca1} ", 72), 1)

    # Sınır denetimleri (§7 kural 6, 8)
    w_s1 = Y.genislik("Fredoka", 700, satir1, 72)
    w_s3 = Y.genislik("Fredoka", 700, satir3, 72)
    w_k1 = x_parca2 - kx + Y.genislik("Fredoka", 700, parca2, 72)
    w_k2 = Y.genislik("Fredoka", 700, parca3, 72)

    assert 102.0 + hw + 20.0 + w_s1 <= 920.0, f"s1 sağ sınır taştı: {102.0 + hw + 20.0 + w_s1}"
    assert 124.0 + w_s3 <= 920.0, f"s3 sağ sınır taştı: {124.0 + w_s3}"
    assert kx + w_k1 <= 960.0, f"Kalıp satır 1 sağ sınır taştı: {kx + w_k1}"
    assert kx + w_k2 <= 960.0, f"Kalıp satır 2 sağ sınır taştı: {kx + w_k2}"
    assert b1 - 64 >= 562 + 16, f"B1 - 64 kart çerçevesine çok yakın: {b1 - 64}"
    assert b3 + 20 <= 998 - 16, f"B3 + 20 kart çerçevesine çok yakın: {b3 + 20}"
    assert 1120.0 <= vy and vy + vk <= 1260.0, "Vizör y aralığı dışı"
    assert kb2 + 20 < 1380, "Kalıp satır 2 tabanı 1380 altında olmalı"

    # Zamanlamalar (§4)
    t_kart = yerel(T(0, "Bu"))
    t_nokta = yerel(T(1, "üç"))
    t_vizor = yerel(T(5, "Ekran"))
    t_deklansor = yerel(T(7, "al"))
    t_parca3 = yerel(T(8, "sınav"))
    t_kuyruk = round((KARE - 12) / 30, 4)

    assert t_vizor + 0.50 <= t_deklansor, f"Vizör çizimi deklanşörden önce bitmeli: {t_vizor + 0.50}"
    assert t_parca3 + 0.30 <= (KARE - 12) / 30, f"Kalıp girişi son 12 kareye sarktı: {t_parca3 + 0.30}"

    zamanlar: dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "kart_giris": [t_kart, 0.40],
        "nokta_giris": [t_nokta, 0.46],
        "vizor_ciz": [t_vizor, 0.50],
        "parca1_giris": [t_vizor, 0.30],
        "deklansor": [t_deklansor, 0.30],
        "parca2_giris": [t_deklansor, 0.30],
        "parca3_giris": [t_parca3, 0.30],
        "kuyruk_durgun": [t_kuyruk, round(SURE - t_kuyruk, 4)],
        "olaylar": [
            [t_kart, "vurus", 0.5],
            [t_nokta, "tik", 0.4],
            [t_vizor, "cizgi", 0.6],
            [t_deklansor, "tik", 0.6],
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
                "olay": "vizor_ciz",
                "kare": round(t_vizor * 30),
                "yerel": t_vizor,
                "kuresel": T(5, "Ekran"),
                "sozcuk": "Ekran",
            },
            {"olay": "deklansor", "kare": round(t_deklansor * 30), "yerel": t_deklansor,
             "kuresel": T(7, "al"), "sozcuk": "al,"},
            {"olay": "parca3_giris", "kare": round(t_parca3 * 30), "yerel": t_parca3,
             "kuresel": T(8, "sınav"), "sozcuk": "sınav"},
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
            "vizor_ciz": zamanlar["vizor_ciz"],
            "parca1_giris": zamanlar["parca1_giris"],
            "deklansor": zamanlar["deklansor"],
            "parca2_giris": zamanlar["parca2_giris"],
            "parca3_giris": zamanlar["parca3_giris"],
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
#root #vizor-dolgu{{fill:var(--vurguDolgu,#f2a93b);}}
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

<!-- Vizör grubu (kol b; cizim/vizor.svg) -->
<g id="vizor" transform="translate({vx:.1f} {vy:.1f})">
<rect id="vizor-dolgu" x="24" y="24" width="92" height="92" rx="12" fill="#f2a93b" style="opacity:0"/>
{"".join(f'<path id="vizor-kose{i}" class="vizor-kose" d="{d}" fill="none" stroke="#f3efe6" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>' for i, d in enumerate(kose_d))}
</g>

<!-- Kalıp yazısı: satır 1 parça 1 + 2, satır 2 parça 3 -->
<text id="kalip-p1" x="{kx:.1f}" y="{kb1}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#f3efe6" style="opacity:0">{parca1}</text>
<text id="kalip-p2" x="{x_parca2:.1f}" y="{kb1}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#f3efe6" style="opacity:0">{parca2}</text>
<text id="kalip-p3" x="{kx:.1f}" y="{kb2}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#f3efe6" style="opacity:0">{parca3}</text>

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

  // vizör köşeleri kalemle, sırayla (her biri 0,2 sn, 0,1 sn aralık; toplam 0,5 sn)
  document.querySelectorAll(".vizor-kose").forEach(function (el, idx) {{
    var L = el.getTotalLength(), t = Z.vizor_ciz[0] + idx * 0.10;
    el.style.strokeDasharray = L + " " + (L + 2);
    el.style.strokeDashoffset = L;
    tl.set(el, ac({{ opacity: 1 }}), t);
    tl.fromTo(el, {{ strokeDashoffset: L }},
      {{ strokeDashoffset: 0, duration: 0.20, ease: "sine.inOut", immediateRender: false }}, t);
  }});

  ["#kalip-p1", "#kalip-p2", "#kalip-p3"].forEach(function (id, idx) {{
    tl.fromTo(id, {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.30, ease: "power3.out",
      immediateRender: false }}, [Z.parca1_giris, Z.parca2_giris, Z.parca3_giris][idx][0]);
  }});
  // deklanşör: vizör içine sarı kare (ölçek 1,08 → 1); aynı anda Today hapı mürekkep çerçeveye döner (tek sarı)
  tl.fromTo("#vizor-dolgu", {{ opacity: 0, scale: 1.08, transformOrigin: "50% 50%" }},
    {{ opacity: 1, scale: 1, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.deklansor[0]);
  tl.fromTo("#today-kutu", {{ opacity: 1 }},
    {{ opacity: 0, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.deklansor[0]);
  tl.fromTo("#today-yazi", {{ opacity: 1 }},
    {{ opacity: 0, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.deklansor[0]);
  tl.fromTo("#today-cerceve", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.deklansor[0]);
  tl.fromTo("#today-yazi2", {{ opacity: 0 }},
    {{ opacity: 1, duration: 0.30, ease: "power2.out", immediateRender: false }}, Z.deklansor[0]);

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

"""simple-present-temel-s3 sahne 03 Kaydet (HyperFrames, DİKEY 1080x1920, huni v2).

Kural özeti kartı, yer imi ve kâğıt uçak simgeleri, Kaydet hapı, Gönder metni ve altyazı üretimi.
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
T_BAS: float = float(SAH["t_bas"])
KARE: int = int(SAH["kare"])
SURE: float = round(KARE / 30, 4)

SOZ: list[dict[str, Any]] = [
    w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 3
]
ALT: list[dict[str, Any]] = [
    p for p in json.loads((PAKET / "ortak" / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
    if p.get("cumle") == 3
]
R: dict[str, str] = Y.RENK


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
    (0, "Does"),
    (1, "varsa"),
    (2, "fiil"),
    (3, "yalın"),
    (4, "Bir"),
    (5, "arkadaşına"),
    (6, "gönder"),
    (7, "o"),
    (8, "da"),
    (9, "karıştırıyor"),
]
assert len(SOZ) == 10, f"Cümle 3 için 10 sözcük bekleniyor, {len(SOZ)} bulundu"
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)
assert len(ALT) == 2, f"Cümle 3 için 2 altyazı parçası bekleniyor, {len(ALT)} bulundu"

# Simge yolları (Tabler Icons biçimi, 24x24)
YERIMI: list[str] = ["M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"]
UCAK: list[str] = [
    "M21 3l-6.5 18a.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a.55 .55 0 0 1 0 -1l18 -6.5",
    "M10 14l11 -11",
]


def uret() -> tuple[str, dict[str, Any]]:
    """Sahne 03 index.html ve zamanlar.json verisini üretir."""
    # Kart metni boyutu ve yerleşimi
    satir1 = "Does varsa"
    satir2 = "fiil yalın."
    k_boy = 88
    while k_boy >= 64:
        w1 = Y.genislik("Fredoka", 700, satir1, k_boy)
        w2 = Y.genislik("Fredoka", 700, satir2, k_boy)
        if max(w1, w2) <= 900.0 - 2.0 * 56.0:
            break
        k_boy -= 1
    assert k_boy >= 64, f"K_BOY 64'ten küçük olamaz: {k_boy}"

    x1 = 510.0 - w1 / 2.0
    x2 = 510.0 - w2 / 2.0
    y1 = 700
    y2 = 700 + round(1.18 * k_boy)

    ks0_x = x1
    ks1_x = x1 + Y.genislik("Fredoka", 700, "Does ", k_boy)
    ks2_x = x2
    ks3_x = x2 + Y.genislik("Fredoka", 700, "fiil ", k_boy)

    assert x1 + w1 <= 960.0 - 56.0, f"Kart satır 1 sağ sınırı aştı: {x1 + w1:.1f}"
    assert x2 + w2 <= 960.0 - 56.0, f"Kart satır 2 sağ sınırı aştı: {x2 + w2:.1f}"

    # Kaydet grubu ölçüleri (sol yarı, 60–510, merkez 285)
    hap_en = Y.genislik("Fredoka", 700, "Kaydet", 64) + 2.0 * 28.0
    g1 = 96.0 + 16.0 + hap_en
    g1x = 285.0 - g1 / 2.0
    hap_x = g1x + 96.0 + 16.0
    hap_cx = hap_x + hap_en / 2.0
    assert g1x >= 60.0, f"g1x sol sınırı aştı: {g1x:.1f} < 60"
    assert g1x + g1 <= 510.0, f"g1x + G1 orta çizgiyi aştı: {g1x + g1:.1f} > 510"

    # Gönder grubu ölçüleri (sağ yarı, 510–960, merkez 735)
    w_gonder = Y.genislik("Lexend", 700, "Gönder", 56)
    g2 = 96.0 + 16.0 + w_gonder
    g2x = 735.0 - g2 / 2.0
    gonder_x = g2x + 96.0 + 16.0
    assert g2x >= 510.0, f"g2x orta çizginin soluna taştı: {g2x:.1f} < 510"
    assert g2x + g2 <= 960.0, f"g2x + G2 sağ sınırı aştı: {g2x + g2:.1f} > 960"

    # Zamanlamalar
    t_cerceve = 0.0
    t_does = yerel(T(0, "Does"))
    t_varsa = yerel(T(1, "varsa"))
    t_fiil = yerel(T(2, "fiil"))
    t_yalin = yerel(T(3, "yalın"))
    t_kart_tam = yerel(E(3, "yalın"))
    t_yerimi = yerel(T(4, "Bir"))
    t_hap = round(yerel(T(4, "Bir")) + 0.10, 3)
    t_ucak = yerel(T(6, "gönder"))
    t_gonder = round(yerel(T(6, "gönder")) + 0.08, 3)
    t_kuyruk = yerel(E(9, "karıştırıyor"))

    zamanlar: dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "kart_cerceve": [t_cerceve, 0.40],
        "soz_does": [t_does, 0.18],
        "soz_varsa": [t_varsa, 0.18],
        "soz_fiil": [t_fiil, 0.18],
        "soz_yalin": [t_yalin, 0.18],
        "kart_tam": [t_kart_tam, round(SURE - t_kart_tam, 3)],
        "yerimi_ciz": [t_yerimi, 0.30],
        "kaydet_hap": [t_hap, 0.30],
        "ucak_ciz": [t_ucak, 0.30],
        "gonder_yazi": [t_gonder, 0.20],
        "kuyruk_durgun": [t_kuyruk, round(SURE - t_kuyruk, 3)],
        "olaylar": [
            [0.40, "cizgi", 0.4],
            [t_yerimi, "cizgi", 0.5],
            [t_hap, "tik", 0.6],
            [t_ucak, "cizgi", 0.5],
        ],
        "olay_listesi": [
            {
                "olay": "kart_cerceve",
                "kare": round(t_cerceve * 30),
                "yerel": t_cerceve,
                "kuresel": round(T_BAS, 3),
                "sozcuk": "sahne başı",
            },
            {
                "olay": "soz_does",
                "kare": round(t_does * 30),
                "yerel": t_does,
                "kuresel": T(0, "Does"),
                "sozcuk": "Does",
            },
            {
                "olay": "soz_varsa",
                "kare": round(t_varsa * 30),
                "yerel": t_varsa,
                "kuresel": T(1, "varsa"),
                "sozcuk": "varsa",
            },
            {
                "olay": "soz_fiil",
                "kare": round(t_fiil * 30),
                "yerel": t_fiil,
                "kuresel": T(2, "fiil"),
                "sozcuk": "fiil",
            },
            {
                "olay": "soz_yalin",
                "kare": round(t_yalin * 30),
                "yerel": t_yalin,
                "kuresel": T(3, "yalın"),
                "sozcuk": "yalın.",
            },
            {
                "olay": "kart_tam",
                "kare": round(t_kart_tam * 30),
                "yerel": t_kart_tam,
                "kuresel": E(3, "yalın"),
                "sozcuk": "kart tam",
            },
            {
                "olay": "yerimi_ciz",
                "kare": round(t_yerimi * 30),
                "yerel": t_yerimi,
                "kuresel": T(4, "Bir"),
                "sozcuk": "Bir",
            },
            {
                "olay": "kaydet_hap",
                "kare": round(t_hap * 30),
                "yerel": t_hap,
                "kuresel": round(T(4, "Bir") + 0.10, 3),
                "sozcuk": "Kaydet",
            },
            {
                "olay": "ucak_ciz",
                "kare": round(t_ucak * 30),
                "yerel": t_ucak,
                "kuresel": T(6, "gönder"),
                "sozcuk": "gönder;",
            },
            {
                "olay": "gonder_yazi",
                "kare": round(t_gonder * 30),
                "yerel": t_gonder,
                "kuresel": round(T(6, "gönder") + 0.08, 3),
                "sozcuk": "Gönder",
            },
            {
                "olay": "kuyruk_durgun",
                "kare": round(t_kuyruk * 30),
                "yerel": t_kuyruk,
                "kuresel": E(9, "karıştırıyor"),
                "sozcuk": "sahne sonu",
            },
        ],
    }

    alt_svg, alt_zaman, karaoke_zaman = Y.altyazi_svg(T_BAS, SURE, ALT)
    kunye_svg = Y.kunye_svg()

    veri = {
        "Z": {
            "kart_cerceve": zamanlar["kart_cerceve"],
            "soz_does": zamanlar["soz_does"],
            "soz_varsa": zamanlar["soz_varsa"],
            "soz_fiil": zamanlar["soz_fiil"],
            "soz_yalin": zamanlar["soz_yalin"],
            "yerimi_ciz": zamanlar["yerimi_ciz"],
            "kaydet_hap": zamanlar["kaydet_hap"],
            "ucak_ciz": zamanlar["ucak_ciz"],
            "gonder_yazi": zamanlar["gonder_yazi"],
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
</defs>

<!-- Kart zemin ve çerçeve -->
<rect id="kart-zemin" x="60" y="560" width="900" height="340" rx="30"
 fill="{R['murekkep']}" fill-opacity="0.06" style="opacity:0"/>
<rect id="kart-cerceve" x="62" y="562" width="896" height="336" rx="28"
 fill="none" stroke="{R['murekkep']}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>

<!-- Kart sözcükleri -->
<text id="ks0" x="{ks0_x:.1f}" y="{y1}" font-family="Fredoka" font-weight="700"
 font-size="{k_boy}" fill="{R['murekkep']}" text-anchor="start" style="font-kerning:none;opacity:0">Does</text>
<text id="ks1" x="{ks1_x:.1f}" y="{y1}" font-family="Fredoka" font-weight="700"
 font-size="{k_boy}" fill="{R['murekkep']}" text-anchor="start" style="font-kerning:none;opacity:0">varsa</text>
<text id="ks2" x="{ks2_x:.1f}" y="{y2}" font-family="Fredoka" font-weight="700"
 font-size="{k_boy}" fill="{R['murekkep']}" text-anchor="start" style="font-kerning:none;opacity:0">fiil</text>
<text id="ks3" x="{ks3_x:.1f}" y="{y2}" font-family="Fredoka" font-weight="700"
 font-size="{k_boy}" fill="{R['murekkep']}" text-anchor="start" style="font-kerning:none;opacity:0">yalın.</text>

<!-- Yer imi simgesi -->
<g id="yerimi" transform="translate({g1x:.1f} 1022) scale(4)" fill="none" stroke="{R['murekkep']}"
 stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="opacity:0">
<path d="{YERIMI[0]}"/>
</g>

<!-- Kaydet hapı -->
<g id="kaydet" style="opacity:0">
<rect x="{hap_x:.1f}" y="1022" width="{hap_en:.1f}" height="96" rx="48" fill="{R['vurgu']}"/>
<text x="{hap_cx:.1f}" y="1092" text-anchor="middle" font-family="Fredoka" font-weight="700"
 font-size="64" fill="{R['zemin']}">Kaydet</text>
</g>

<!-- Kâğıt uçak simgesi -->
<g id="ucak" transform="translate({g2x:.1f} 1022) scale(4)" fill="none" stroke="{R['murekkep']}"
 stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="opacity:0">
<path d="{UCAK[0]}"/>
<path d="{UCAK[1]}"/>
</g>

<!-- Gönder metni -->
<text id="gonder" x="{gonder_x:.1f}" y="1090" font-family="Lexend" font-weight="700"
 font-size="56" fill="{R['murekkep']}" style="opacity:0">Gönder</text>

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

  var cerceve = $("#kart-cerceve");
  if (cerceve) {{
    var L = cerceve.getTotalLength();
    cerceve.style.strokeDasharray = L + " " + (L + 2);
    cerceve.style.strokeDashoffset = L;
    tl.fromTo(cerceve, {{ strokeDashoffset: L }},
      {{ strokeDashoffset: 0, duration: Z.kart_cerceve[1], ease: "sine.inOut",
         immediateRender: false }}, Z.kart_cerceve[0]);
  }}

  tl.fromTo("#kart-zemin", {{ opacity: 0 }},
    {{ opacity: 1, duration: Z.kart_cerceve[1], ease: "power2.out", immediateRender: false }}, Z.kart_cerceve[0]);

  tl.fromTo("#ks0", {{ opacity: 0 }},
    {{ opacity: 1, duration: Z.soz_does[1], ease: "power2.out", immediateRender: false }}, Z.soz_does[0]);
  tl.fromTo("#ks1", {{ opacity: 0 }},
    {{ opacity: 1, duration: Z.soz_varsa[1], ease: "power2.out", immediateRender: false }}, Z.soz_varsa[0]);
  tl.fromTo("#ks2", {{ opacity: 0 }},
    {{ opacity: 1, duration: Z.soz_fiil[1], ease: "power2.out", immediateRender: false }}, Z.soz_fiil[0]);
  tl.fromTo("#ks3", {{ opacity: 0 }},
    {{ opacity: 1, duration: Z.soz_yalin[1], ease: "power2.out", immediateRender: false }}, Z.soz_yalin[0]);

  var yerimiYol = $("#yerimi path");
  if (yerimiYol) {{
    var L1 = yerimiYol.getTotalLength();
    yerimiYol.style.strokeDasharray = L1 + " " + (L1 + 2);
    yerimiYol.style.strokeDashoffset = L1;
    tl.set("#yerimi", ac({{ opacity: 1 }}), Z.yerimi_ciz[0]);
    tl.fromTo(yerimiYol, {{ strokeDashoffset: L1 }},
      {{ strokeDashoffset: 0, duration: Z.yerimi_ciz[1], ease: "sine.inOut",
         immediateRender: false }}, Z.yerimi_ciz[0]);
  }}

  gsap.set("#kaydet", {{ svgOrigin: "{hap_x:.1f} 1070" }});
  tl.fromTo("#kaydet", {{ opacity: 0, scale: 0.9 }},
    {{ opacity: 1, scale: 1, duration: Z.kaydet_hap[1], ease: "back.out(1.6)",
       immediateRender: false }}, Z.kaydet_hap[0]);

  var ucakYollar = document.querySelectorAll("#ucak path");
  if (ucakYollar.length > 0) {{
    var L2_toplam = 0;
    var L2_dizi = [];
    ucakYollar.forEach(function (p) {{
      var l = p.getTotalLength();
      L2_dizi.push(l);
      L2_toplam += l;
      p.style.strokeDasharray = l + " " + (l + 2);
      p.style.strokeDashoffset = l;
    }});
    tl.set("#ucak", ac({{ opacity: 1 }}), Z.ucak_ciz[0]);
    var t_ucak_an = Z.ucak_ciz[0];
    var ucak_toplam_sure = Z.ucak_ciz[1];
    ucakYollar.forEach(function (p, idx) {{
      var d = ucak_toplam_sure * (L2_dizi[idx] / (L2_toplam || 1));
      tl.fromTo(p, {{ strokeDashoffset: L2_dizi[idx] }},
        {{ strokeDashoffset: 0, duration: d, ease: "sine.inOut", immediateRender: false }}, t_ucak_an);
      t_ucak_an += d;
    }});
  }}

  tl.fromTo("#gonder", {{ opacity: 0, x: -12 }},
    {{ opacity: 1, x: 0, duration: Z.gonder_yazi[1], ease: "power3.out", immediateRender: false }}, Z.gonder_yazi[0]);

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

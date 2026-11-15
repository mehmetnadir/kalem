"""simple-present-temel-s2b (A/B kol b, değişken kapanis) sahne 03 Kaydet (HyperFrames, DİKEY 1080x1920, huni v2).

Kural özeti kartı, kinetik giriş, sarı hap, ekran görüntüsü çerçevesi ve altyazı üretimi.
Kol a'dan fark (KBC-0202S2): kaydet kalıbı `Ekran görüntüsü al, sınav günü bak.`; yer imi yerine 4 köşe parantezi
(vizör köşeleri), `Kaydet` yerine `Ekran görüntüsü al`; ikisi de `al,` çapasında. Kart kol a ile aynı.
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
T_BAS: float = float(SAH["t_bas"])  # 11.87
KARE: int = int(SAH["kare"])        # 228
SURE: float = round(KARE / 30, 4)   # 7.6

SOZ: list[dict[str, Any]] = [
    w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 3
]
ALT: list[dict[str, Any]] = [
    p for p in json.loads((PAKET / "ortak" / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
    if p.get("cumle") == 3 or (p.get("cumle") == 2 and float(p.get("t1", 0)) > T_BAS)
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


# Sözcük ve altyazı doğrulamaları (§2 ve §3)
BEKLENEN_SOZLER: list[tuple[int, str]] = [
    (0, "Usually"),
    (1, "always"),
    (2, "every"),
    (3, "day"),
    (4, "Simple"),
    (5, "Present"),
    (6, "Ekran"),
    (7, "görüntüsü"),
    (8, "al"),
    (9, "sınav"),
    (10, "günü"),
    (11, "bak"),
]
assert len(SOZ) == 12, f"Cümle 3 için 12 sözcük bekleniyor, {len(SOZ)} bulundu"
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)

assert len([p for p in ALT if p.get("cumle") == 3]) == 2, "Cümle 3 için 2 altyazı parçası bekleniyor"
assert len([p for p in ALT if p.get("cumle") == 2]) == 1, "Cümle 2 için 1 altyazı parçası bekleniyor"
assert len(ALT) == 3, f"Toplam 3 altyazı parçası bekleniyor, {len(ALT)} bulundu"

# Kol b kaydet öğesi: ekrandaki yazı + ekran görüntüsü çerçevesi (4 köşe parantezi; 24 birimlik kutu, x 5-19, y 3-21).
# Her köşe ayrı yol: Chrome kesik desenini her M'de baştan başlatır (taslak açık nokta 7); köşeler saat yönünde sırayla çizilir.
KAYDET_YAZI: str = "Ekran görüntüsü al"
CERCEVE_YOLLARI: list[str] = [
    "M5 8v-3a2 2 0 0 1 2 -2h3",
    "M14 3h3a2 2 0 0 1 2 2v3",
    "M19 16v3a2 2 0 0 1 -2 2h-3",
    "M10 21h-3a2 2 0 0 1 -2 -2v-3",
]


def kart_kenar_yolu() -> str:
    """Elle çizilmiş kart kenarı yolu (tek M, 3 ara noktalı kenarlar, sol üstte bindirme, §6)."""
    kay = [1.6, -1.2, 2.2, -0.8, 1.0, -2.0, 0.6, 1.8, -1.4, 0.4, -2.2, 1.2]
    noktalar: list[tuple[float, float]] = [
        (86.0, 564.0),
        (293.0, 564.0 + kay[0]),
        (510.0, 564.0 + kay[1]),
        (727.0, 564.0 + kay[2]),
        (944.0, 564.0),
        (944.0 + kay[3], 647.0),
        (944.0 + kay[4], 730.0),
        (944.0 + kay[5], 813.0),
        (944.0, 896.0),
        (727.0, 896.0 + kay[6]),
        (510.0, 896.0 + kay[7]),
        (293.0, 896.0 + kay[8]),
        (76.0, 896.0),
        (76.0 + kay[9], 813.0),
        (max(74.0, 76.0 + kay[10]), 730.0),
        (76.0 + kay[11], 647.0),
        (76.0, 564.0),
        (100.0, 564.0),
    ]
    for p in noktalar:
        assert 74.0 <= p[0] <= 946.0, f"kart-kenar x sınırı dışı: {p}"
        assert 562.0 <= p[1] <= 898.0, f"kart-kenar y sınırı dışı: {p}"
    return "M " + f"{noktalar[0][0]:.1f} {noktalar[0][1]:.1f}" + " " + " ".join(
        f"L {p[0]:.1f} {p[1]:.1f}" for p in noktalar[1:]
    )


def uret() -> tuple[str, dict[str, Any]]:
    """Sahne 03 index.html ve zamanlar.json verisini üretir."""
    # Karakter sayısı denetimleri (§9 kural 7)
    assert len("Usually,") <= 24
    assert len("always,") <= 24
    assert len("Usually, always,") <= 24
    assert len("every day:") <= 24
    assert len("Simple Present.") <= 24
    assert len(KAYDET_YAZI) <= 24

    # Hap ve satır genişlikleri (§5); nokta hapın içinde (hap dışında kopuk görünüyordu, QA 15.11)
    hap_w = Y.genislik("Fredoka", 700, "Simple Present.", 72) + 56.0
    g1 = Y.genislik("Fredoka", 700, "Usually, always,", 72)
    g2 = Y.genislik("Fredoka", 700, "every day:", 72)
    g3 = hap_w
    gmax = max(g1, g2, g3)

    bx = round(510.0 - gmax / 2.0, 1)
    s2_x = bx + Y.genislik("Fredoka", 700, "Usually, ", 72)
    hap_cx = bx + hap_w / 2.0

    t1 = 646
    t2 = t1 + 96
    t3 = t2 + 96

    # Yerleşim doğrulamaları (§5 ve §9)
    assert bx >= 110.0, f"BX 110'dan küçük: {bx}"
    assert bx + gmax <= 910.0, f"Sağ sınır 910'u aştı: {bx + gmax}"
    assert t1 - 52 >= 564 + 24, f"Yazı üst boşluğu yetersiz: {t1 - 52}"
    assert t3 + 28 <= 896 - 24, f"Yazı alt boşluğu yetersiz: {t3 + 28}"
    assert (t3 - 64) - (t2 + 17) >= 12, f"Hap ile üst satır arası yetersiz: {(t3 - 64) - (t2 + 17)}"

    # Kart kenar yolu (§6)
    kenar_d = kart_kenar_yolu()

    # Kaydet grubu ölçüleri (§7; kol b: çerçeve yolu x 5-19, y 3-21 birim, ölçek 5 → 70 + çizgi 7 = 77 px)
    yazi_w = Y.genislik("Fredoka", 700, KAYDET_YAZI, 72)
    ikon_en = 77.0
    ara = 28.0
    grup_en = ikon_en + ara + yazi_w
    gx = 510.0 - grup_en / 2.0
    tx = gx + 3.5 - 25.0
    yazi_x = gx + ikon_en + ara
    assert gx >= 60.0 and gx + grup_en <= 960.0, f"Kaydet grubu sınır dışı: {gx:.1f}..{gx + grup_en:.1f}"
    assert grup_en <= 900.0, f"Kaydet grubu 900 px'i aştı: {grup_en:.1f}"

    # Bütün içerik y 460-1380 ve x 60-960 sınır denetimi (§9 kural 8)
    # Kart dış kenar 60-960 x 548-912 (kâğıt rect 61/549 + 898x362); Kaydet ikonu çizgi dahil y 960-1060
    assert 60 <= 61 - 1 and 61 + 898 + 1 <= 960 and 549 - 1 >= 460 and 549 + 362 + 1 <= 1380
    assert 951 + 3 * 5 - 3.5 >= 960 and 951 + 21 * 5 + 3.5 <= 1060, "Kaydet ikonu 960-1060 dışında"
    cerceve_svg = "\n".join(
        f'<path id="kaydet-imi-{k + 1}" class="kaydet-imi" d="{d}" style="opacity:0"/>'
        for k, d in enumerate(CERCEVE_YOLLARI)
    )

    # Zamanlamalar (§4)
    t_kart = yerel(T(0, "Usually"))
    t_s1 = yerel(T(0, "Usually"))
    t_s2 = yerel(T(1, "always"))
    t_s3 = yerel(T(2, "every"))
    t_hap = yerel(T(4, "Simple"))
    t_sabit = yerel(T(5, "Present"))
    t_imi = yerel(T(8, "al"))
    t_yazi = round(yerel(T(8, "al")) + 0.10, 3)
    t_kuyruk = round((KARE - 12) / 30, 3)

    # Kart içindeki son tween kart_sabit'ten önce biter (§4)
    assert t_hap + 0.30 <= t_sabit, f"Hap girişi kart sabitlenmeden bitmedi: {t_hap + 0.30} > {t_sabit}"
    # Son 12 karede tween yok (§4, §9 kural 6)
    assert t_yazi + 0.25 <= t_kuyruk, f"Yazı girişi son 12 kareye sarktı: {t_yazi + 0.25} > {t_kuyruk}"

    zamanlar: dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "kart_giris": [t_kart, 0.45],
        "s1_giris": [t_s1, 0.25],
        "s2_giris": [t_s2, 0.25],
        "s3_giris": [t_s3, 0.25],
        "hap_giris": [t_hap, 0.30],
        "kart_sabit": [t_sabit, round(t_kuyruk - t_sabit, 3)],
        "imi_ciz": [t_imi, 0.30],
        "yazi_giris": [t_yazi, 0.25],
        "kuyruk_durgun": [t_kuyruk, round(SURE - t_kuyruk, 3)],
        "olaylar": [
            [t_kart, "vurus", 0.5],
            [t_hap, "tik", 0.5],
            [t_imi, "cizgi", 0.6],
            [t_yazi, "tik", 0.4],
        ],
        "olay_listesi": [
            {
                "olay": "kart_giris",
                "kare": round(t_kart * 30),
                "yerel": t_kart,
                "kuresel": T(0, "Usually"),
                "sozcuk": "Usually,",
            },
            {
                "olay": "s1_giris",
                "kare": round(t_s1 * 30),
                "yerel": t_s1,
                "kuresel": T(0, "Usually"),
                "sozcuk": "Usually,",
            },
            {
                "olay": "s2_giris",
                "kare": round(t_s2 * 30),
                "yerel": t_s2,
                "kuresel": T(1, "always"),
                "sozcuk": "always,",
            },
            {
                "olay": "s3_giris",
                "kare": round(t_s3 * 30),
                "yerel": t_s3,
                "kuresel": T(2, "every"),
                "sozcuk": "every day:",
            },
            {
                "olay": "hap_giris",
                "kare": round(t_hap * 30),
                "yerel": t_hap,
                "kuresel": T(4, "Simple"),
                "sozcuk": "Simple Present.",
            },
            {
                "olay": "kart_sabit",
                "kare": round(t_sabit * 30),
                "yerel": t_sabit,
                "kuresel": T(5, "Present"),
                "sozcuk": "Present.",
            },
            {
                "olay": "imi_ciz",
                "kare": round(t_imi * 30),
                "yerel": t_imi,
                "kuresel": T(8, "al"),
                "sozcuk": "al,",
            },
            {
                "olay": "yazi_giris",
                "kare": round(t_yazi * 30),
                "yerel": t_yazi,
                "kuresel": round(T(8, "al") + 0.10, 3),
                "sozcuk": "al,",
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

    alt_svg, alt_zaman, ham_karaoke = Y.altyazi_svg(T_BAS, SURE, ALT)
    karaoke_zaman: list[list[Any]] = []
    for k in ham_karaoke:
        cid, ac_t, kapat_t, uz = k
        if kapat_t <= 0:
            continue
        if ac_t < 0:
            ac_t = 0.0
        karaoke_zaman.append([cid, ac_t, kapat_t, uz])

    kunye_svg = Y.kunye_svg()

    veri = {
        "Z": {
            "kart_giris": zamanlar["kart_giris"],
            "s1_giris": zamanlar["s1_giris"],
            "s2_giris": zamanlar["s2_giris"],
            "s3_giris": zamanlar["s3_giris"],
            "hap_giris": zamanlar["hap_giris"],
            "imi_ciz": zamanlar["imi_ciz"],
            "yazi_giris": zamanlar["yazi_giris"],
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

<!-- Kart grubu -->
<g id="kart" style="opacity:0">
<rect id="kagit" x="61" y="549" width="898" height="362" rx="22"
 fill="#fff9e6" stroke="#c9c2b3" stroke-width="2"/>
<path id="kart-kenar" d="{kenar_d}" fill="none" stroke="#1b1a17" stroke-width="4.5"
 stroke-linecap="round" stroke-linejoin="round"/>
<text id="s1" x="{bx:.1f}" y="{t1}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#1b1a17" style="opacity:0">Usually,</text>
<text id="s2" x="{s2_x:.1f}" y="{t1}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#1b1a17" style="opacity:0">always,</text>
<text id="s3" x="{bx:.1f}" y="{t2}" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#1b1a17" style="opacity:0">every day:</text>
<g id="satir3" style="opacity:0">
<rect x="{bx:.1f}" y="{t3 - 64}" width="{hap_w:.1f}" height="92" rx="46" fill="#f2a93b"/>
<text x="{hap_cx:.1f}" y="{t3}" text-anchor="middle" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#1b1a17">Simple Present.</text>
</g>
</g>

<!-- Kaydet grubu -->
<g id="kaydet">
<g id="kaydet-ikon" transform="translate({tx:.1f} 951) scale(5)" fill="none" stroke="#f3efe6"
 stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">
{cerceve_svg}
</g>
<text id="kaydet-yazi" x="{yazi_x:.1f}" y="1036" font-family="Fredoka" font-weight="700"
 font-size="72" fill="#f3efe6" style="opacity:0">{KAYDET_YAZI}</text>
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

  gsap.set("#kart", {{ svgOrigin: "510 730" }});
  tl.fromTo("#kart", {{ scale: 0.96, opacity: 0 }},
    {{ scale: 1, opacity: 1, duration: 0.45, ease: "power3.out", immediateRender: false }}, Z.kart_giris[0]);

  tl.fromTo("#s1", {{ opacity: 0, y: 16 }},
    {{ opacity: 1, y: 0, duration: 0.25, ease: "power3.out", immediateRender: false }}, Z.s1_giris[0]);

  tl.fromTo("#s2", {{ opacity: 0, y: 16 }},
    {{ opacity: 1, y: 0, duration: 0.25, ease: "power3.out", immediateRender: false }}, Z.s2_giris[0]);

  tl.fromTo("#s3", {{ opacity: 0, y: 16 }},
    {{ opacity: 1, y: 0, duration: 0.25, ease: "power3.out", immediateRender: false }}, Z.s3_giris[0]);

  gsap.set("#satir3", {{ svgOrigin: "{hap_cx:.1f} {t3 - 18}" }});
  tl.fromTo("#satir3", {{ opacity: 0, scale: 0.9 }},
    {{ opacity: 1, scale: 1, duration: 0.30, ease: "back.out(1.6)", immediateRender: false }}, Z.hap_giris[0]);

  // 4 köşe saat yönünde sırayla: köşe başına 0,12 sn, aralık 0,06 sn → toplam 0,30 sn (kol a yer imi süresi)
  document.querySelectorAll(".kaydet-imi").forEach(function (el, k) {{
    var L = el.getTotalLength(), t = Z.imi_ciz[0] + 0.06 * k;
    el.style.strokeDasharray = L + " " + (L + 2);
    el.style.strokeDashoffset = L;
    tl.set(el, ac({{ opacity: 1 }}), t);
    tl.fromTo(el, {{ strokeDashoffset: L }},
      {{ strokeDashoffset: 0, duration: 0.12, ease: "sine.inOut", immediateRender: false }}, t);
  }});

  tl.fromTo("#kaydet-yazi", {{ opacity: 0, y: 12 }},
    {{ opacity: 1, y: 0, duration: 0.25, ease: "power3.out", immediateRender: false }}, Z.yazi_giris[0]);

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

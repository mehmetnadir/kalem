"""simple-present-temel-s3 sahne 04 Çağrı (HyperFrames, DİKEY 1080x1920, huni v2).

Kapak kartı, kinetik giriş, çağrı hapı, YouTube ve konuşma balonu altyazı üretimi.
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
T_BAS: float = float(SAH["t_bas"])  # 18.10
KARE: int = int(SAH["kare"])        # 239
SURE: float = round(KARE / 30, 4)   # 7.9667

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

BALON: dict[str, Any] = {
    "x": 122,
    "y": 1404,
    "h": 142,
    "ty": 1470,
    "pay": 40,
    "satirEn": 760,
    "yazi": 44,
    "satirAra": 56,
    "taban1": 1490,
    "taban2": (1461, 1517),
}


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
    (0, "Bu"),
    (1, "sadece"),
    (2, "başlangıç"),
    (3, "Dersin"),
    (4, "tamamı"),
    (5, "YDS"),
    (6, "Publishing"),
    (7, "YouTube"),
    (8, "kanalında"),
]
assert len(SOZ) == 9, f"Cümle 4 için 9 sözcük bekleniyor, {len(SOZ)} bulundu"
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)
assert len(ALT) == 2, f"Cümle 4 için 2 altyazı parçası bekleniyor, {len(ALT)} bulundu"


def konusma_balonu(x: float | int, y: float | int, w: float | int, h: float | int, ty: float | int) -> str:
    """Sol kenarında kuyruğu olan, hafif eğri el balonu (yol d). ty: kuyruk ucu y."""
    r = 28
    return (
        "M%d %d L%d %d Q%d %d %d %d L%d %d Q%d %d %d %d L%d %d Q%d %d %d %d L%d %d L%d %d L%d %d L%d %d "
        "Q%d %d %d %d Z"
        % (
            x + r, y + 3, x + w - r, y - 1, x + w + 4, y, x + w + 2, y + r,
            x + w - 2, y + h - r, x + w, y + h + 3, x + w - r, y + h + 1,
            x + r, y + h + 3, x - 2, y + h, x, y + h - r,
            x, ty + 46, x - 58, ty, x + 2, ty - 34, x - 1, y + r,
            x + 1, y + 1, x + r, y + 3,
        )
    )


def altyazi_balon_satirlari(metin: str) -> list[str]:
    """Lexend 500 44, satır eni <= satirEn (760), sözcük sözcük; en çok 2 satır."""
    sat: list[str] = []
    s = ""
    for w in metin.split(" "):
        d = s + " " + w if s else w
        if Y.genislik("Lexend", 500, d, BALON["yazi"]) > BALON["satirEn"] and s:
            sat.append(s)
            s = w
        else:
            s = d
    if s:
        sat.append(s)
    assert len(sat) <= 2, f"En çok 2 satır beklenir: {sat}"
    return sat


def balon_altyazi(
    t_bas: float, sure: float, liste: list[dict[str, Any]]
) -> tuple[str, list[list[Any]], list[list[Any]]]:
    """Konuşma balonu altyazısı (y 1400-1550) + karaoke altçizgisi.

    -> (svg, [["al<i>", ac, kapat], ...], [["ak<i>_<j>", ac, kapat, uzunluk], ...]) yerel sn.
    """
    svg_parcalar: list[str] = []
    zaman: list[list[Any]] = []
    karaoke: list[list[Any]] = []
    liste = Y.altyazi_cumleleri(liste)
    sozcukler = SOZ

    ayazi = BALON["yazi"]
    murekkep = R["murekkep"]
    vurgu = R["vurgu"]

    for i, a in enumerate(liste):
        t0 = float(a["t0"])
        t1 = float(a["t1"])
        ac = max(0.0, t0 - 0.05 - t_bas)
        son = t1 + 0.35
        if i + 1 < len(liste):
            son = min(son, float(liste[i + 1]["t0"]) - 0.05)
        kapat = son - t_bas
        if kapat <= 0 or ac >= sure:
            continue
        parca_kapat = min(kapat, sure)
        zaman.append(["al%d" % i, round(ac, 3), round(parca_kapat, 3)])

        satirlar = altyazi_balon_satirlari(a["metin"])
        satir_enleri = [Y.genislik("Lexend", 500, s, ayazi) for s in satirlar]
        bw = max(satir_enleri) + 2 * BALON["pay"]

        bx = BALON["x"]
        by = BALON["y"]
        bh = BALON["h"]
        bty = BALON["ty"]

        assert bx - 58 >= 60, f"kuyruk ucu < 60: {bx - 58}"
        assert bx + bw + 4 <= 960, f"gövde sağ ucu > 960: {bx + bw + 4}"
        assert by - 1 >= 1400, f"üst < 1400: {by - 1}"
        assert by + bh + 3 <= 1550, f"alt > 1550: {by + bh + 3}"

        d_balon = konusma_balonu(bx, by, bw, bh, bty)
        balon_el = (
            f'<path id="ab{i}" d="{d_balon}" fill="none" stroke="{murekkep}" '
            'stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
        )

        tabanlar = [BALON["taban1"]] if len(satirlar) == 1 else list(BALON["taban2"])
        satir_elemanlari: list[str] = []
        satir_bilgileri: list[dict[str, Any]] = []

        for k, sat in enumerate(satirlar):
            satir_y = tabanlar[k]
            satir_eni = satir_enleri[k]
            satir_x = bx + (bw - satir_eni) / 2
            satir_elemanlari.append(
                f'<text x="{satir_x:.1f}" y="{satir_y}" text-anchor="start" font-family="Lexend" '
                f'font-weight="500" font-size="{ayazi}" fill="{murekkep}" style="font-kerning:none">{sat}</text>'
            )
            satir_bilgileri.append({"satir": sat, "x": satir_x, "y": satir_y})

        # Karaoke altçizgileri
        w_list = [w for w in sozcukler if t0 - 0.05 <= w["t0"] < t1 + 0.05]
        satir_sozcukleri: list[tuple[int, int, str, dict[str, Any]]] = []
        for k, sb in enumerate(satir_bilgileri):
            sw_list = sb["satir"].split(" ")
            for s_idx, sw in enumerate(sw_list):
                satir_sozcukleri.append((k, s_idx, sw, sb))

        cizgi_elemanlari: list[str] = []
        if len(w_list) == len(satir_sozcukleri):
            for j, ((k, s_idx, sw, sb), w) in enumerate(zip(satir_sozcukleri, w_list)):
                sw_list = sb["satir"].split(" ")
                onceki = (" ".join(sw_list[:s_idx]) + " ") if s_idx > 0 else ""
                x1 = sb["x"] + (Y.genislik("Lexend", 500, onceki, ayazi) if onceki else 0.0)
                sw_temiz = sw.rstrip(".,:;!?")
                x2 = x1 + Y.genislik("Lexend", 500, sw_temiz, ayazi)
                y1 = sb["y"] + 12
                y2 = y1
                cizgi_ac = round(w["t0"] - t_bas, 3)
                if j + 1 < len(w_list):
                    cizgi_kapat = round(w_list[j + 1]["t0"] - t_bas, 3)
                else:
                    cizgi_kapat = round(min(w["t1"] - t_bas + 0.25, parca_kapat), 3)
                uzunluk = round(x2 - x1, 2)
                karaoke.append([f"ak{i}_{j}", cizgi_ac, cizgi_kapat, uzunluk])
                cizgi_elemanlari.append(
                    f'<line id="ak{i}_{j}" x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" '
                    f'stroke="{vurgu}" stroke-width="6" stroke-linecap="round" style="opacity:0"/>'
                )

        ic_govde = balon_el + "".join(satir_elemanlari) + "".join(cizgi_elemanlari)
        svg_parcalar.append(f'<g id="al{i}" style="opacity:0">{ic_govde}</g>')

    return "".join(svg_parcalar), zaman, karaoke


def uret() -> tuple[str, dict[str, Any]]:
    """Sahne 04 index.html ve zamanlar.json verisini üretir."""
    # Kinetik metin boyutu
    g_boy = 96
    while g_boy >= 64:
        w_toplam = Y.genislik("Fredoka", 700, "Bu sadece başlangıç.", g_boy)
        if 60.0 + w_toplam <= 960.0:
            break
        g_boy -= 1
    assert g_boy >= 64, f"G_BOY 64'ten küçük olamaz: {g_boy}"

    x_bs1 = 60.0 + Y.genislik("Fredoka", 700, "Bu ", g_boy)
    x_bs2 = 60.0 + Y.genislik("Fredoka", 700, "Bu sadece ", g_boy)

    # Hap ölçüleri: @ydspublishing (Lexend 700, 56)
    hap_metin = "@ydspublishing"
    w_hap_metin = Y.genislik("Lexend", 700, hap_metin, 56)
    hap_w = w_hap_metin + 2.0 * 28.0
    hap_cx = 60.0 + hap_w / 2.0

    # YouTube: · YouTube (Lexend 700, 56)
    yt_x = 60.0 + hap_w + 18.0
    yt_w = Y.genislik("Lexend", 700, "· YouTube", 56)
    assert yt_x + yt_w <= 960.0, f"YouTube sağ sınırı aştı: {yt_x + yt_w:.1f} > 960"

    t_bu = yerel(T(0, "Bu"))
    t_sadece = yerel(T(1, "sadece"))
    t_baslangic = yerel(T(2, "başlangıç"))
    t_dersin = yerel(T(3, "Dersin"))
    t_hap = yerel(T(5, "YDS"))
    t_yt = yerel(T(7, "YouTube"))
    t_kuyruk = yerel(E(8, "kanalında"))

    zamanlar: dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "bu_giris": [t_bu, 0.22],
        "sadece_giris": [t_sadece, 0.22],
        "baslangic_giris": [t_baslangic, 0.22],
        "kart_cerceve": [t_dersin, 0.40],
        "kapak_belir": [t_dersin, 0.30],
        "hap_giris": [t_hap, 0.30],
        "youtube_giris": [t_yt, 0.30],
        "kuyruk_durgun": [t_kuyruk, round(SURE - t_kuyruk, 3)],
        "olaylar": [
            [t_bu, "tik", 0.4],
            [t_dersin, "cizgi", 0.5],
            [t_hap, "tik", 0.6],
            [t_yt, "tik", 0.4],
        ],
        "olay_listesi": [
            {
                "olay": "bu_giris",
                "kare": round(t_bu * 30),
                "yerel": t_bu,
                "kuresel": T(0, "Bu"),
                "sozcuk": "Bu",
            },
            {
                "olay": "sadece_giris",
                "kare": round(t_sadece * 30),
                "yerel": t_sadece,
                "kuresel": T(1, "sadece"),
                "sozcuk": "sadece",
            },
            {
                "olay": "baslangic_giris",
                "kare": round(t_baslangic * 30),
                "yerel": t_baslangic,
                "kuresel": T(2, "başlangıç"),
                "sozcuk": "başlangıç.",
            },
            {
                "olay": "kart_cerceve",
                "kare": round(t_dersin * 30),
                "yerel": t_dersin,
                "kuresel": T(3, "Dersin"),
                "sozcuk": "Dersin",
            },
            {
                "olay": "kapak_belir",
                "kare": round(t_dersin * 30),
                "yerel": t_dersin,
                "kuresel": T(3, "Dersin"),
                "sozcuk": "Dersin",
            },
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

    alt_svg, alt_zaman, karaoke_zaman = balon_altyazi(T_BAS, SURE, ALT)
    kunye_svg = Y.kunye_svg()

    veri = {
        "Z": {
            "bu_giris": zamanlar["bu_giris"],
            "sadece_giris": zamanlar["sadece_giris"],
            "baslangic_giris": zamanlar["baslangic_giris"],
            "kart_cerceve": zamanlar["kart_cerceve"],
            "kapak_belir": zamanlar["kapak_belir"],
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
<g id="kart">
<image id="kapakimg" href="assets/ana-kapak.png" x="60" y="620" width="900" height="506"
 preserveAspectRatio="xMidYMid slice" clip-path="url(#kart-kirp)" style="opacity:0"/>
<rect id="kart-cerceve" x="62" y="622" width="896" height="502" rx="22" fill="none"
 stroke="{R['murekkep']}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
</g>

<!-- Kinetik metinler -->
<text id="bs0" x="60" y="560" font-family="Fredoka" font-weight="700"
 font-size="{g_boy}" fill="{R['murekkep']}" style="font-kerning:none;opacity:0">Bu</text>
<text id="bs1" x="{x_bs1:.1f}" y="560" font-family="Fredoka" font-weight="700"
 font-size="{g_boy}" fill="{R['murekkep']}" style="font-kerning:none;opacity:0">sadece</text>
<text id="bs2" x="{x_bs2:.1f}" y="560" font-family="Fredoka" font-weight="700"
 font-size="{g_boy}" fill="{R['murekkep']}" style="font-kerning:none;opacity:0">başlangıç.</text>

<!-- Çağrı hapı ve YouTube -->
<g id="hap" style="opacity:0">
<rect x="60" y="1180" width="{hap_w:.1f}" height="80" rx="40" fill="{R['vurgu']}"/>
<text x="{hap_cx:.1f}" y="1240" text-anchor="middle" font-family="Lexend" font-weight="700"
 font-size="56" fill="{R['zemin']}">@ydspublishing</text>
</g>
<text id="yt" x="{yt_x:.1f}" y="1240" font-family="Lexend" font-weight="700"
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

  var cerceve = $("#kart-cerceve");
  if (cerceve) {{
    var L = cerceve.getTotalLength();
    cerceve.style.strokeDasharray = L + " " + (L + 2);
    cerceve.style.strokeDashoffset = L;
    tl.fromTo(cerceve, {{ strokeDashoffset: L }},
      {{ strokeDashoffset: 0, duration: Z.kart_cerceve[1], ease: "sine.inOut", immediateRender: false }},
      Z.kart_cerceve[0]);
  }}

  tl.fromTo("#kapakimg", {{ opacity: 0 }},
    {{ opacity: 1, duration: Z.kapak_belir[1], ease: "power2.out", immediateRender: false }},
    Z.kapak_belir[0]);

  tl.fromTo("#bs0", {{ opacity: 0, y: 24 }},
    {{ opacity: 1, y: 0, duration: Z.bu_giris[1], ease: "back.out(1.6)", immediateRender: false }},
    Z.bu_giris[0]);
  tl.fromTo("#bs1", {{ opacity: 0, y: 24 }},
    {{ opacity: 1, y: 0, duration: Z.sadece_giris[1], ease: "back.out(1.6)", immediateRender: false }},
    Z.sadece_giris[0]);
  tl.fromTo("#bs2", {{ opacity: 0, y: 24 }},
    {{ opacity: 1, y: 0, duration: Z.baslangic_giris[1], ease: "back.out(1.6)", immediateRender: false }},
    Z.baslangic_giris[0]);

  gsap.set("#hap", {{ svgOrigin: "60 1220" }});
  tl.fromTo("#hap", {{ opacity: 0, scale: 0.9 }},
    {{ opacity: 1, scale: 1, duration: Z.hap_giris[1], ease: "back.out(1.6)", immediateRender: false }},
    Z.hap_giris[0]);

  tl.fromTo("#yt", {{ opacity: 0, x: -12 }},
    {{ opacity: 1, x: 0, duration: Z.youtube_giris[1], ease: "power3.out", immediateRender: false }},
    Z.youtube_giris[0]);

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

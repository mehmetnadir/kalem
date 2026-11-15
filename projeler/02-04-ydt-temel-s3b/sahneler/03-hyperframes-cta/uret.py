"""Sahne 03 Çağrı index.html ve zamanlar.json üretici (02-04-ydt-temel-s3; DİKEY 1080x1920; 239 kare = 7.9667 sn).
Cümle 5 ses olayları, kapak kartı, giriş sözü ve @ydspublishing YouTube çağrısı. Huni v2."""
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))["sahneler"]
           if s["klasor"] == AD.name)
T_BAS: float = SAH["t_bas"]  # 21.33
KARE: int = SAH["kare"]      # 239
SURE: float = round(KARE / 30, 4)  # 7.9667
_SOZ_TUM: List[Dict[str, Any]] = json.loads(
    (PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
# DUZ2 (15.11): A/B kol b (kanca değişkeni) başa cümle ekler; kayma = örnek cümlesinin ("The ...") sırası - 1.
KAYMA: int = int(next(w["cumle"] for w in _SOZ_TUM if w["sozcuk"] == "The")) - 1
CUMLE: int = 5 + KAYMA
SOZ: List[Dict[str, Any]] = [w for w in _SOZ_TUM if w["cumle"] == CUMLE]
ALT: List[Dict[str, Any]] = [
    a for a in json.loads((PAKET / "ortak" / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
    if a.get("cumle") == CUMLE
]


def T(i: int, bas: str = "") -> float:
    """Cümle 5, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = w["sozcuk"]
        assert val.lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, val, bas)
    return float(w["t0"])


def E(i: int, bas: str = "") -> float:
    """Cümle 5, i. sözcüğün t1'i (küresel sn); sözcük kayarsa durur."""
    w = SOZ[i]
    if bas:
        val = w["sozcuk"]
        assert val.lower().startswith(bas.lower()), "sözcük %d: %r, beklenen %r" % (i, val, bas)
    return float(w["t1"])


def y_sn(t_kuresel: float) -> float:
    """Küresel saniyeyi yerel sahne saniyesine çevirir (4 basamak yuvarlar)."""
    return round(t_kuresel - T_BAS, 4)


# Sözcük assert'leri ile 9 sözcüğün sırası baştan doğrulanır
BEKLENEN_SOZLER: List[Tuple[int, str]] = [
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
for _idx, _bas in BEKLENEN_SOZLER:
    T(_idx, _bas)

# ---- Yerleşim Sabitleri (px, DİKEY 1080x1920) ----
W: int = 1080
H: int = 1920

# Renkler (tema CSS'i bu sabitleri değişkene çevirir; başka renk yazma)
RENK_MUREKKEP: str = "#f3efe6"
RENK_IKINCIL: str = "#c9c2b3"
RENK_VURGU: str = "#f2a93b"
RENK_PIL_METIN: str = "#1b1a17"

# 3.1 Kanal ve Künye
KANAL_LOGO_X: float = 53.2
KANAL_LOGO_Y: int = 291
KANAL_LOGO_W: float = 193.5  # 48 * 1920 / 476.3
KANAL_LOGO_H: int = 48
KANAL_METIN_X: int = 263
KANAL_METIN_Y: int = 330
KANAL_METIN_BOY: int = 42

KUNYE_X: int = 60
KUNYE_Y: int = 420
KUNYE_KONU: str = "Simple Present vs Present Continuous"

ROZET_METIN: str = "YDT · TEMEL"
ROZET_BOY: int = 26
ROZET_Y: int = 386
ROZET_H: int = 48
ROZET_RX: int = 24
ROZET_DOLGU_EK: int = 40
ROZET_ARA: int = 20

# 3.2 Giriş Sözü
GS_X: int = 60
GS_Y: int = 560
GS_METIN: str = "Bu sadece başlangıç."

# 3.3 Ana Ders Kapağı Kartı
KAPAK_X: int = 60
KAPAK_Y: int = 620
KAPAK_W: int = 900
KAPAK_H: int = 506
KAPAK_RX: int = 24
KAPAK_CX: float = KAPAK_X + KAPAK_W / 2.0  # 510.0
KAPAK_CY: float = KAPAK_Y + KAPAK_H / 2.0  # 873.0

# 3.4 @ydspublishing / YouTube
HAP_X: int = 60
HAP_Y: int = 1160
HAP_H: int = 104
HAP_RX: int = 52
HAP_METIN: str = "@ydspublishing"
HAP_YAZI_X: int = 92
HAP_YAZI_Y: int = 1234
HAP_YAZI_BOY: int = 64

YT_METIN: str = "YouTube"
YT_X: int = 60
YT_Y: int = 1346
YT_BOY: int = 64

# 3.5 Altyazı
ALTYAZI_X: int = 510
ALTYAZI_Y_TEK: int = 1490
ALTYAZI_Y_CIFT1: int = 1462
ALTYAZI_Y_CIFT2: int = 1518
ALTYAZI_EN_SINIR: int = 900


def hap_yolu(x: float, y: float, w: float, h: float, rx: float) -> str:
    """Yuvarlak dikdörtgenin çevresi (sol orta noktadan başlar, saat yönünde tek kapalı yol)."""
    return (
        f"M{x:.1f} {y + rx:.1f} "
        f"A{rx:.1f} {rx:.1f} 0 0 1 {x + rx:.1f} {y:.1f} "
        f"L{x + w - rx:.1f} {y:.1f} "
        f"A{rx:.1f} {rx:.1f} 0 0 1 {x + w:.1f} {y + rx:.1f} "
        f"A{rx:.1f} {rx:.1f} 0 0 1 {x + w - rx:.1f} {y + h:.1f} "
        f"L{x + rx:.1f} {y + h:.1f} "
        f"A{rx:.1f} {rx:.1f} 0 0 1 {x:.1f} {y + rx:.1f} Z"
    )


def uret_altyazi() -> Tuple[str, List[List[Any]], List[List[Any]]]:
    """Altyazı parçalarını ve karaoke zamanlarını üretir (Lexend 500 en çok 2 satır; tspan sözcükleri)."""
    svg_parcalar: List[str] = []
    alt_zaman: List[List[Any]] = []
    karaoke_zaman: List[List[Any]] = []

    for i, p in enumerate(ALT):
        metin_sozcukler = p["metin"].split()
        soz_eslesen = [w for w in SOZ if p["t0"] - 0.05 <= w["t0"] < p["t1"] + 0.05]
        assert len(soz_eslesen) == len(metin_sozcukler), (
            f"parça {i}: sözcük sayısı {len(soz_eslesen)} != {len(metin_sozcukler)}"
        )

        # Satır kırma: Lexend 500, en çok 2 satır; boy 44 -> 40 -> 36
        secilen_boy: int = 0
        secilen_satirlar: List[List[str]] = []
        for boy in (44, 40, 36):
            satirlar: List[List[str]] = []
            cur: List[str] = []
            ok = True
            for w in metin_sozcukler:
                cand = " ".join(cur + [w])
                if Y.genislik("Lexend", 500, cand, boy) <= ALTYAZI_EN_SINIR:
                    cur.append(w)
                else:
                    if not cur:
                        ok = False
                        break
                    satirlar.append(cur)
                    cur = [w]
                    if Y.genislik("Lexend", 500, w, boy) > ALTYAZI_EN_SINIR:
                        ok = False
                        break
            if cur:
                satirlar.append(cur)
            if ok and len(satirlar) <= 2:
                secilen_boy = boy
                secilen_satirlar = satirlar
                break

        assert secilen_satirlar, f"parça {i} 2 satıra sığmadı"

        tabanlar = [ALTYAZI_Y_TEK] if len(secilen_satirlar) == 1 else [ALTYAZI_Y_CIFT1, ALTYAZI_Y_CIFT2]

        satir_svglari: List[str] = []
        w_idx = 0
        for sat_words, y_tab in zip(secilen_satirlar, tabanlar):
            tspans: List[str] = []
            for w in sat_words:
                tspans.append(f'<tspan id="al{i}w{w_idx}" fill="{RENK_IKINCIL}">{w}</tspan>')
                w_idx += 1
            satir_svglari.append(
                f'<text x="{ALTYAZI_X}" y="{y_tab}" text-anchor="middle" font-family="Lexend" '
                f'font-weight="500" font-size="{secilen_boy}">' + " ".join(tspans) + "</text>"
            )

        svg_parcalar.append(f'<g id="al{i}" style="opacity:0">\n' + "\n".join(satir_svglari) + "\n</g>")

        ac_sn = round(max(0.0, p["t0"] - 0.05 - T_BAS), 4)
        son_sn = p["t1"] + 0.35
        if i + 1 < len(ALT):
            son_sn = min(son_sn, ALT[i + 1]["t0"] - 0.05)
        kapat_sn = round(min(son_sn - T_BAS, SURE), 4)
        alt_zaman.append([f"al{i}", ac_sn, kapat_sn])

        for k, w_soz in enumerate(soz_eslesen):
            t0_yerel = round(w_soz["t0"] - T_BAS, 4)
            karaoke_zaman.append([f"al{i}w{k}", t0_yerel])

    return "\n".join(svg_parcalar), alt_zaman, karaoke_zaman


def uret() -> Tuple[str, Dict[str, Any]]:
    """index.html ve zamanlar verisini üretir."""
    # 1. Künye konu boyu ve rozet konumu
    w_rozet = Y.genislik("Lexend", 700, ROZET_METIN, ROZET_BOY) + ROZET_DOLGU_EK
    konu_boy: int = 34
    for boy in range(34, 27, -1):
        w_k = Y.genislik("Fredoka", 700, KUNYE_KONU, boy)
        if KUNYE_X + w_k + ROZET_ARA + w_rozet <= 960:
            konu_boy = boy
            break

    w_konu = Y.genislik("Fredoka", 700, KUNYE_KONU, konu_boy)
    rz_x = KUNYE_X + w_konu + ROZET_ARA
    rz_cx = rz_x + w_rozet / 2.0

    # 2. Giriş sözü (Bu sadece başlangıç.)
    gs_birim = Y.genislik("Fredoka", 700, GS_METIN, 1)
    gs_boy = min(96, math.floor(900 / gs_birim))
    w_gs = Y.genislik("Fredoka", 700, GS_METIN, gs_boy)
    assert gs_boy >= 64, f"giriş sözü boyu {gs_boy} < 64"
    assert w_gs <= 900, f"giriş sözü genişliği {w_gs} > 900"

    x_gs0 = float(GS_X)
    x_gs1 = GS_X + Y.genislik("Fredoka", 700, "Bu ", gs_boy)
    x_gs2 = GS_X + Y.genislik("Fredoka", 700, "Bu sadece ", gs_boy)

    # 3. @ydspublishing / YouTube (Tek veya İki Satır)
    w_cta = Y.genislik("Lexend", 700, HAP_METIN, HAP_YAZI_BOY)
    w_hap = w_cta + 64.0
    w_yt_tek = Y.genislik("Lexend", 700, "· YouTube", HAP_YAZI_BOY)
    tek_satir_toplam = w_hap + 20.0 + w_yt_tek

    if tek_satir_toplam <= 900.0:
        cagri_satir = 1
        yt_metin = "· YouTube"
        yt_x = HAP_X + w_hap + 20.0
        yt_y = 1234
    else:
        cagri_satir = 2
        yt_metin = "YouTube"
        yt_x = float(YT_X)
        yt_y = YT_Y

    d_hap = hap_yolu(float(HAP_X), float(HAP_Y), w_hap, float(HAP_H), float(HAP_RX))
    hap_clip_w = w_cta + 24.0

    hap_svg = (
        f'<g id="hapg">\n'
        f'  <rect id="hapdolgu" x="{HAP_X}" y="{HAP_Y}" width="{w_hap:.1f}" height="{HAP_H}" '
        f'rx="{HAP_RX}" fill="{RENK_VURGU}" style="opacity:0"/>\n'
        f'  <path id="hapcizgi" d="{d_hap}" fill="none" stroke="{RENK_VURGU}" stroke-width="4" '
        f'stroke-linecap="round" style="opacity:0"/>\n'
        f'  <text id="hapyazi" x="{HAP_YAZI_X}" y="{HAP_YAZI_Y}" font-family="Lexend" font-weight="700" '
        f'font-size="{HAP_YAZI_BOY}" fill="{RENK_PIL_METIN}" clip-path="url(#cph)">{HAP_METIN}</text>\n'
        f'</g>\n'
        f'<text id="yt" x="{yt_x:.1f}" y="{yt_y}" font-family="Lexend" font-weight="700" '
        f'font-size="{YT_BOY}" fill="{RENK_MUREKKEP}" style="opacity:0">{yt_metin}</text>'
    )

    # 4. Altyazı ve Karaoke
    altyazi_svg, alt_zaman, karaoke_zaman = uret_altyazi()

    # 5. Zamanlar ve Olaylar
    t_hap_yazi = y_sn(T(5, "YDS") + 0.10)
    dur_hap_yazi = round(E(6, "Publishing") - (T(5, "YDS") + 0.10), 4)

    zamanlar: Dict[str, Any] = {
        "fps": 30,
        "kare": KARE,
        "sure": SURE,
        "t_bas": T_BAS,
        "cagri_satir": cagri_satir,
        "kapak_giris": [0.0, 0.40],
        "gs0_giris": [y_sn(T(0, "Bu")), 0.30],
        "gs1_giris": [y_sn(T(1, "sadece")), 0.30],
        "gs2_giris": [y_sn(T(2, "başlangıç")), 0.30],
        "hap_cizgi": [y_sn(T(5, "YDS")), 0.30],
        "hap_dolgu": [y_sn(T(5, "YDS") + 0.20), 0.15],
        "hap_yazi": [t_hap_yazi, dur_hap_yazi],
        "yt_giris": [y_sn(T(7, "YouTube")), 0.30],
        "olaylar": [
            [y_sn(T(0, "Bu")), "tik", 0.40],
            [y_sn(T(2, "başlangıç")), "tik", 0.45],
            [y_sn(T(5, "YDS")), "cizgi", 0.50],
            [y_sn(T(5, "YDS") + 0.10), "hisirti", 0.45],
            [y_sn(T(7, "YouTube")), "tik", 0.50],
        ],
    }

    # ClipPath tanımları
    cp = lambda n, x, y, b: (  # noqa: E731
        f'<clipPath id="cp{n}"><rect id="cr{n}" x="{x:.1f}" y="{y - b}" width="0" height="{int(b * 1.5)}"/>'
        '</clipPath>'
    )
    clips = (
        f'<clipPath id="kapakkirp"><rect x="{KAPAK_X}" y="{KAPAK_Y}" width="{KAPAK_W}" '
        f'height="{KAPAK_H}" rx="{KAPAK_RX}"/></clipPath>\n'
        + cp("h", HAP_YAZI_X, HAP_YAZI_Y, HAP_YAZI_BOY)
    )

    veri: Dict[str, Any] = {
        "Z": zamanlar,
        "kapak_cx": KAPAK_CX,
        "kapak_cy": KAPAK_CY,
        "hap_clip_w": hap_clip_w,
        "alt": alt_zaman,
        "karaoke": karaoke_zaman,
    }

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
#kapakA{{display:none}}.tema-acik #kapakA{{display:inline}}.tema-acik #kapakK{{display:none}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{SURE}" data-fps="30"
     data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>
{clips}
</defs>

<!-- 3.1 Kanal Katmanı + Künye -->
<g id="kunye">
  <g id="kanal">
    <image id="logoimg" href="assets/logo.svg" x="{KANAL_LOGO_X}" y="{KANAL_LOGO_Y}"
           width="{KANAL_LOGO_W}" height="{KANAL_LOGO_H}"/>
    <text x="{KANAL_METIN_X}" y="{KANAL_METIN_Y}" font-family="Lexend" font-weight="700"
          font-size="{KANAL_METIN_BOY}" fill="{RENK_MUREKKEP}">@ydspublishing</text>
  </g>
  <text id="ku-konu" x="{KUNYE_X}" y="{KUNYE_Y}" font-family="Fredoka" font-weight="700"
        font-size="{konu_boy}" fill="{RENK_MUREKKEP}">{KUNYE_KONU}</text>
  <g id="rz0">
    <rect x="{rz_x:.1f}" y="{ROZET_Y}" width="{w_rozet:.1f}" height="{ROZET_H}" rx="{ROZET_RX}" fill="{RENK_VURGU}"/>
    <text x="{rz_cx:.1f}" y="419" text-anchor="middle" font-family="Lexend" font-weight="700"
          font-size="{ROZET_BOY}" fill="{RENK_PIL_METIN}">{ROZET_METIN}</text>
  </g>
</g>

<!-- 3.2 Giriş Sözü -->
<text id="gs0" x="{x_gs0:.1f}" y="{GS_Y}" font-family="Fredoka" font-weight="700" font-size="{gs_boy}"
      fill="{RENK_MUREKKEP}" style="opacity:0">Bu</text>
<text id="gs1" x="{x_gs1:.1f}" y="{GS_Y}" font-family="Fredoka" font-weight="700" font-size="{gs_boy}"
      fill="{RENK_MUREKKEP}" style="opacity:0">sadece</text>
<text id="gs2" x="{x_gs2:.1f}" y="{GS_Y}" font-family="Fredoka" font-weight="700" font-size="{gs_boy}"
      fill="{RENK_MUREKKEP}" style="opacity:0">başlangıç.</text>

<!-- 3.3 Ana Ders Kapağı Kartı -->
<g id="kapakg" style="opacity:0">
  <image id="kapakA" href="assets/ana-kapak.png" x="{KAPAK_X}" y="{KAPAK_Y}" width="{KAPAK_W}" height="{KAPAK_H}"
         preserveAspectRatio="xMidYMid slice" clip-path="url(#kapakkirp)"/>
  <image id="kapakK" href="assets/ana-kapak-koyu.png" x="{KAPAK_X}" y="{KAPAK_Y}" width="{KAPAK_W}" height="{KAPAK_H}"
         preserveAspectRatio="xMidYMid slice" clip-path="url(#kapakkirp)"/>
  <rect id="kapakcer" x="{KAPAK_X}" y="{KAPAK_Y}" width="{KAPAK_W}" height="{KAPAK_H}" rx="{KAPAK_RX}"
        fill="none" stroke="{RENK_MUREKKEP}" stroke-width="3"/>
</g>

<!-- 3.4 @ydspublishing / YouTube -->
{hap_svg}

<!-- 3.5 Altyazı + Karaoke -->
<g id="altyazi">
{altyazi_svg}
</g>

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

  function darbe(id, bas, sure) {{
    var p = $("#" + id), L = p.getTotalLength();
    p.style.strokeDasharray = L + " " + (L + 2);
    p.style.strokeDashoffset = L;
    tl.set(p, ac({{ opacity: 1 }}), bas);
    tl.to(p, ac({{ strokeDashoffset: 0, duration: sure, ease: "none" }}), bas);
  }}

  function kinetik(id, bas) {{
    tl.fromTo(id, {{ opacity: 0, y: 24 }},
      {{ opacity: 1, y: 0, duration: 0.30, ease: "power3.out", immediateRender: false }}, bas);
  }}

  function yaz(id, z, w) {{
    tl.fromTo("#cr" + id, {{ attr: {{ width: 0 }} }},
      {{ attr: {{ width: w }}, duration: z[1], ease: "none", immediateRender: false }}, z[0]);
  }}

  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});

  V.karaoke.forEach(function (k) {{
    tl.set("#" + k[0], ac({{ attr: {{ fill: "{RENK_MUREKKEP}" }} }}), k[1]);
  }});

  gsap.set("#kapakg", {{ svgOrigin: V.kapak_cx + " " + V.kapak_cy }});
  tl.fromTo("#kapakg", {{ opacity: 0, scale: 0.96 }},
    {{ opacity: 1, scale: 1, duration: Z.kapak_giris[1], ease: "power3.out", immediateRender: false }},
    Z.kapak_giris[0]);

  kinetik("#gs0", Z.gs0_giris[0]);
  kinetik("#gs1", Z.gs1_giris[0]);
  kinetik("#gs2", Z.gs2_giris[0]);

  darbe("hapcizgi", Z.hap_cizgi[0], Z.hap_cizgi[1]);
  tl.fromTo("#hapdolgu", {{ opacity: 0 }},
    {{ opacity: 1, duration: Z.hap_dolgu[1], ease: "power3.out", immediateRender: false }}, Z.hap_dolgu[0]);
  yaz("h", Z.hap_yazi, V.hap_clip_w);

  kinetik("#yt", Z.yt_giris[0]);

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

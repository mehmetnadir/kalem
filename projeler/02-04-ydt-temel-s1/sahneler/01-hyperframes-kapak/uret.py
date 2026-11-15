"""02-04-ydt-temel-s1 sahne 01 kapak index.html üretici (HyperFrames DİKEY 1080x1920, 102 kare).

SPEC.md §4 uygulaması: kapak düzeni, çizimler, Caveat cümle yazımı, başlık uçuşu ve devir.json çıktısı.
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

# ---- 4.1 Okuma ----
Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
ORTAK = AD.parent.parent / "ortak"
SOZ = [
    w for w in json.loads((ORTAK / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 1
]
assert [w["sozcuk"] for w in SOZ[:4]] == ["İstanbul'da", "yaşıyorum.", "Amcamla", "yaşıyorum."], (
    f"Beklenen ilk 4 sözcük bulunamadı: {[w['sozcuk'] for w in SOZ[:4]]}"
)
ALT = json.loads((ORTAK / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
FIG = json.loads((AD / "cizim" / "ogretmen.json").read_text(encoding="utf-8"))

try:
    BAVUL_YOLLAR = Y.tabler("luggage", AD / "cizim")
except TypeError:
    _lug_svg = (AD / "cizim" / "luggage.svg").read_text(encoding="utf-8")
    BAVUL_YOLLAR = [d for d in re.findall(r'<path d="([^"]+)"', _lug_svg) if not d.startswith("M0 0h24v24")]
EV_YOLLAR = Y.tabler("home")

# ---- 4.2 Sabitler ve türetilen ölçüler ----
W, H = Y.W, Y.H
KENAR = Y.HUD.get("kenar", 48) if hasattr(Y, "HUD") else 48
BAS1 = "YAŞIYORUM"
BAS2 = "= İKİ ZAMAN"
PAD = 0.20  # em

B = math.floor(min(
    190,
    952 / Y.genislik("Fredoka", 700, BAS1, 1),
    952 / (Y.genislik("Fredoka", 700, BAS2, 1) + 2 * PAD)
))
g1 = Y.genislik("Fredoka", 700, BAS1, B)
t1x = (W - g1) / 2
T1 = 375 + 0.70 * B
ALTI_Y = T1 + 0.20 * B
HAP_UST = ALTI_Y + 29
T2 = HAP_UST + 0.98 * B
HAP_ALT = T2 + 0.26 * B

hap_w = Y.genislik("Fredoka", 700, BAS2, B) + 2 * PAD * B
hap_x = (W - hap_w) / 2
hap_rx = (HAP_ALT - HAP_UST) / 2
hap_h = HAP_ALT - HAP_UST

SOL = 48
SAT_BOY = 80
R1_K, R2_K = 856, 1004
R1_SON, R2_SON = 452, 600
DY = R1_SON - R1_K

ZEMIN_Y = 1384
EV_S, EV_X = 16, 48
EV_Y = ZEMIN_Y - 21 * EV_S

FIG_H, FIG_X = 460, 600
x0, y0, x1, y1 = FIG["kutu"]
fs = FIG_H / (y1 - y0)
EX = FIG_X + (FIG["el"][0] - x0) * fs
EY = (ZEMIN_Y - FIG_H) + (FIG["el"][1] - y0) * fs

BV_S = 9
BX = EX + 6 - 12 * BV_S
BY = EY - 3 * BV_S

E1_X = EV_X + 12 * EV_S
E1_Y = EV_Y + 3 * EV_S - 36
E2_X = W - KENAR
E2_Y = EY - 48

SATIR1 = "İstanbul'da yaşı-yor-um."
SATIR2 = "Amcamla yaşı-yor-um."
g_sat1 = Y.genislik("Caveat", 700, SATIR1, SAT_BOY)
g_sat2 = Y.genislik("Caveat", 700, SATIR2, SAT_BOY)

# Künye bilgileri (kunye.js / yardim.py arayüzü)
DERS = getattr(Y, "DERS", ("SIMPLE PRESENT vs", "PRESENT CONTINUOUS"))
ROZET = getattr(Y, "ROZET", "YDT · BASIC")

if hasattr(Y, "rozet_konumu"):
    rz_x, rz_w = Y.rozet_konumu()
else:
    rz_x = KENAR + Y.genislik("Fredoka", 700, DERS[-1], 56) + 24
    rz_w = Y.genislik("Lexend", 700, ROZET, 36) + 56
rz_h = 72
rz_y = 216

UK = 0.85
gd1 = Y.genislik("Fredoka", 700, DERS[0], 56)
gd2 = Y.genislik("Fredoka", 700, DERS[1], 56)
dersTaban = Y.HUD.get("dersTaban", 212) if hasattr(Y, "HUD") else 212
dersSatir = Y.HUD.get("dersSatir", 64) if hasattr(Y, "HUD") else 64

o1 = (t1x + g1 / 2, T1 - 0.35 * B)
h1 = (KENAR + UK * gd1 / 2, dersTaban - 0.35 * 56 - Z["ucus_ayrik"])   # QA tur 1: bas1 × bas2 26 px
hs1 = UK * gd1 / g1

o2 = (540, (HAP_UST + HAP_ALT) / 2)
h2 = (KENAR + UK * gd2 / 2, dersTaban + dersSatir - 0.35 * 56 + Z["ucus_ayrik"])
hs2 = UK * gd2 / hap_w


# ---- 4.7 Denetimler ----
def _denetimler() -> None:
    # 1. B, hap, baslik 1
    assert 150 <= B <= 190, f"B={B} aralık [150, 190] dışı"
    assert hap_x >= 63 and hap_x + hap_w <= 1017, f"hap x={hap_x:.2f}..{hap_x + hap_w:.2f} aralık [63, 1017] dışı"
    assert t1x >= 63 and t1x + g1 <= 1017, f"baslik 1 x={t1x:.2f}..{t1x + g1:.2f} aralık [63, 1017] dışı"
    assert (T1 - 0.70 * B) >= 352, f"baslik 1 üstü {T1 - 0.70 * B:.2f} < 352"

    # 2. Satır metinleri
    assert len(SATIR1) <= 24, f"satir 1 {len(SATIR1)} > 24 karakter"
    assert len(SATIR2) <= 24, f"satir 2 {len(SATIR2)} > 24 karakter"
    assert SOL + g_sat1 <= W - KENAR, f"satir 1 {SOL + g_sat1:.2f} > {W - KENAR}"
    assert SOL + g_sat2 <= W - KENAR, f"satir 2 {SOL + g_sat2:.2f} > {W - KENAR}"

    # 3. Kapak dikey sıra (>= 24 px ara)
    r1_ust = R1_K - 0.864 * SAT_BOY
    r1_alt = R1_K + 0.212 * SAT_BOY
    fig_ust = ZEMIN_Y - FIG_H
    e1_ust = E1_Y - 0.70 * 72
    ev_ust = EV_Y + 3 * EV_S
    e2_alt = E2_Y + 0.25 * 72

    assert r1_ust - HAP_ALT >= 24, f"HAP_ALT -> satır 1 üstü ara {r1_ust - HAP_ALT:.2f} < 24"
    assert fig_ust - r1_alt >= 24, f"satır 1 altı -> figür üstü ara {fig_ust - r1_alt:.2f} < 24"
    assert e1_ust - r1_alt >= 24, f"satır 1 altı -> E1 üstü ara {e1_ust - r1_alt:.2f} < 24"
    assert ev_ust - E1_Y >= 24, f"E1 tabanı -> ev üstü ara {ev_ust - E1_Y:.2f} < 24"
    assert e2_alt + 12 <= EY, f"E2 altı + 12 = {e2_alt + 12:.2f} > EY = {EY:.2f}"

    # 4. Yatay
    g_e2 = Y.genislik("Caveat", 700, "I am living", 72)
    g_e1 = Y.genislik("Caveat", 700, "I live", 72)
    e2_sol = W - KENAR - g_e2
    fig_sag = FIG_X + (x1 - x0) * fs
    assert e2_sol >= fig_sag + 20, f"E2 sol {e2_sol:.2f} < figür sağı + 20 ({fig_sag + 20:.2f})"
    assert BX + 18 * BV_S <= W - KENAR, f"bavul sağı {BX + 18 * BV_S:.2f} > {W - KENAR}"
    e1_sag = E1_X + g_e1 / 2
    assert e1_sag < FIG_X, f"E1 sağı {e1_sag:.2f} >= FIG_X {FIG_X}"

    # 5. Son hal
    assert R1_SON - 0.864 * SAT_BOY >= 352, f"R1_SON üstü {R1_SON - 0.864 * SAT_BOY:.2f} < 352"
    assert R2_SON + 0.212 * SAT_BOY <= 1392, f"R2_SON altı {R2_SON + 0.212 * SAT_BOY:.2f} > 1392"
    assert R2_SON - R1_SON >= 1.85 * SAT_BOY, f"satır aralığı {R2_SON - R1_SON} < {1.85 * SAT_BOY}"

    # 6. Zaman
    satir1_bitis = SOZ[1]["t0"] + Z["yazi_cap"]
    assert satir1_bitis <= Z["kapak_kare"] / 30.0 - 1.0 / 30.0, f"satır 1 bitiş {satir1_bitis:.3f} > kapak_kare sınırı"
    u1 = Z["ucus"][0] + Z["ucus"][1]
    hareket_bitis_sinir = (Z["kare"] - 12) / 30.0
    assert u1 <= hareket_bitis_sinir, f"u1 {u1:.3f} > {hareket_bitis_sinir:.3f}"
    assert Z["satir2_son"] <= hareket_bitis_sinir, f"satir2_son {Z['satir2_son']:.3f} > {hareket_bitis_sinir:.3f}"

    # 7. Uçuş çakışma örneklemesi
    def _p3_in_out(p: float) -> float:
        p = max(0.0, min(1.0, p))
        return 8.0 * (p ** 4) if p < 0.5 else 1.0 - 8.0 * ((1.0 - p) ** 4)

    def _p3_out(p: float) -> float:
        p = max(0.0, min(1.0, p))
        return 1.0 - ((1.0 - p) ** 4)

    def _kesisir(b1: list[float], b2: list[float], pay: float = 6.0) -> bool:
        return not (b1[1] + pay <= b2[0] or b2[1] + pay <= b1[0] or b1[3] + pay <= b2[2] or b2[3] + pay <= b1[2])

    u0, ud = Z["ucus"]
    rk0, rkd = Z["rozet_kay"]
    curr_t = u0
    # başlıklar opaklık ≥ 0,5 iken (power1.in: süre × 0,71); QA tur 1'de kapı 2,75'te çapraz solmayı yakaladı
    while curr_t <= Z["baslik_sol"][0] + 0.71 * Z["baslik_sol"][1] + 1e-6:
        pt = (curr_t - u0) / ud
        et = _p3_in_out(pt)
        es = _p3_out((curr_t - u0) / Z["ucus_olcek"])

        dx1 = (h1[0] - o1[0]) * et
        dy1 = (h1[1] - o1[1]) * et
        s1 = 1.0 + (hs1 - 1.0) * es
        box_bas1 = [
            o1[0] + dx1 + s1 * (t1x - o1[0]),
            o1[0] + dx1 + s1 * (t1x + g1 - o1[0]),
            o1[1] + dy1 + s1 * (T1 - 0.70 * B - o1[1]),
            o1[1] + dy1 + s1 * (ALTI_Y + 5 - o1[1]),
        ]

        dx2 = (h2[0] - o2[0]) * et
        dy2 = (h2[1] - o2[1]) * et
        s2 = 1.0 + (hs2 - 1.0) * es
        box_bas2 = [
            o2[0] + dx2 + s2 * (hap_x - o2[0]),
            o2[0] + dx2 + s2 * (hap_x + hap_w - o2[0]),
            o2[1] + dy2 + s2 * (HAP_UST - o2[1]),
            o2[1] + dy2 + s2 * (HAP_ALT - o2[1]),
        ]

        prz = (curr_t - rk0) / rkd
        erz = _p3_in_out(prz)
        curr_rz_x = KENAR + (rz_x - KENAR) * erz
        box_rz0 = [curr_rz_x, curr_rz_x + rz_w, 216.0, 288.0]

        box_r1 = [
            float(SOL),
            float(SOL + g_sat1),
            R1_K - 0.864 * SAT_BOY + DY * et,
            R1_K + 0.212 * SAT_BOY + DY * et,
        ]

        c1 = _kesisir(box_bas1, box_rz0, 6.0)
        c2 = _kesisir(box_bas2, box_rz0, 6.0)
        c3 = _kesisir(box_bas2, box_r1, 6.0)
        # bas1 × bas2 yazı mürekkebi (kapı ölçüsü): Ş çengeli 0,182 em, İ noktası 0,921 em
        b1_alt = o1[1] + dy1 + s1 * (T1 + 0.182 * B - o1[1])
        b2_ust = o2[1] + dy2 + s2 * (T2 - 0.921 * B - o2[1])
        c4 = b2_ust - b1_alt < 6.0
        if c1 or c2 or c3 or c4:
            assert False, f"Uçuş çakışması t={curr_t:.3f}: bas1xrz0={c1}, bas2xrz0={c2}, bas2xr1={c3}, bas1xbas2={c4}"
        curr_t += 1.0 / 30.0


_denetimler()


# ---- 4.8 Zamanlar fonksiyonu ----
def zamanlar() -> dict:
    """olay.py tarafından okunan olay zamanları."""
    return {
        "alti": [Z["alti"][0], Z["alti"][1]],
        "r1": [
            [SOZ[0]["t0"], round(min(SOZ[0]["t1"] - SOZ[0]["t0"], Z["yazi_cap"]), 4)],
            [SOZ[1]["t0"], Z["yazi_cap"]],
        ],
        "r2": [SOZ[2]["t0"], round(Z["satir2_son"] - SOZ[2]["t0"], 4)],
        "ucus": [Z["ucus"][0], Z["ucus"][1]],
    }


# ---- 4.8 uret() fonksiyonu ----
def uret() -> str:
    R = Y.RENK

    # Kırpma kutuları
    clips = (
        f'<clipPath id="cp1"><rect id="cr1" x="{SOL - 12}" y="{R1_K - SAT_BOY}" width="0" '
        f'height="{int(SAT_BOY * 1.35)}"/></clipPath>'
        f'<clipPath id="cp2"><rect id="cr2" x="{SOL - 12}" y="{R2_K - SAT_BOY}" width="0" '
        f'height="{int(SAT_BOY * 1.35)}"/></clipPath>'
    )

    # Çizimler
    # 1. Yer
    zc_path = '<path id="zc" d="M64 1384 L1016 1384" stroke-width="4"/>'

    # 2. Ev (home)
    ev_svg = "".join(f'<path d="{d}"/>' for d in EV_YOLLAR)
    ev_group = (
        f'<g id="ev" transform="translate({EV_X} {EV_Y}) scale({EV_S})" '
        f'stroke-width="{4.0 / EV_S:.3f}">{ev_svg}</g>'
    )

    # 3. Figür
    fig_kalinlik = {"govde": 4.4, "sac": 3.6, "yuz": 2.6}
    fig_svg = "".join(
        f'<path id="f{i}" d="{p["d"]}" stroke-width="{fig_kalinlik.get(p["parca"], 4.4) / fs:.3f}"/>'
        for i, p in enumerate(FIG["yollar"])
    )
    tx_fig = FIG_X - x0 * fs
    ty_fig = (ZEMIN_Y - FIG_H) - y0 * fs
    fig_group = (
        f'<g id="fig" transform="translate({tx_fig:.2f} {ty_fig:.2f}) scale({fs:.6f})">{fig_svg}</g>'
    )

    # 4. Bavul (luggage)
    bavul_svg = "".join(f'<path d="{d}"/>' for d in BAVUL_YOLLAR)
    bavul_group = (
        f'<g id="bavul" transform="translate({BX:.2f} {BY:.2f}) scale({BV_S})" stroke-width="{4.0 / BV_S:.3f}">'
        f'<rect id="bvd" x="6" y="6" width="12" height="14" rx="2" stroke="none" style="fill:var(--zemin)"/>'
        f'{bavul_svg}</g>'
    )

    eskiz = (
        f'<g id="eskiz" fill="none" stroke="{R["murekkep"]}" stroke-linecap="round" stroke-linejoin="round">'
        f'{zc_path}{ev_group}{fig_group}{bavul_group}</g>'
    )

    # Etiketler
    etk1 = (
        f'<text id="etk1" x="{E1_X}" y="{E1_Y}" text-anchor="middle" font-family="Caveat" '
        f'font-weight="700" font-size="72" stroke="none" fill="{R["murekkep"]}">I live</text>'
    )
    etk2 = (
        f'<text id="etk2" x="{E2_X}" y="{E2_Y:.2f}" text-anchor="end" font-family="Caveat" '
        f'font-weight="700" font-size="72" stroke="none" fill="{R["murekkep"]}">I am living</text>'
    )

    kapak_sahne = f'<g id="kapak-sahne">{eskiz}{etk1}{etk2}</g>'

    # Cümle satırları
    r1 = (
        f'<g id="r1"><text x="{SOL}" y="{R1_K}" font-family="Caveat" font-weight="700" font-size="{SAT_BOY}" '
        f'fill="{R["murekkep"]}" clip-path="url(#cp1)" style="font-kerning:none">{SATIR1}</text></g>'
    )
    r2 = (
        f'<g id="r2"><text x="{SOL}" y="{R2_K}" font-family="Caveat" font-weight="700" font-size="{SAT_BOY}" '
        f'fill="{R["murekkep"]}" clip-path="url(#cp2)" style="font-kerning:none">{SATIR2}</text></g>'
    )

    # Başlık 2 (hap)
    bas2 = (
        f'<g id="bas2">'
        f'<rect id="hap" x="{hap_x:.2f}" y="{HAP_UST:.2f}" width="{hap_w:.2f}" height="{hap_h:.2f}" '
        f'rx="{hap_rx:.2f}" fill="{R["vurgu"]}"/>'
        f'<text id="bas2t" x="540" y="{T2:.2f}" text-anchor="middle" font-family="Fredoka" '
        f'font-weight="700" font-size="{B}" fill="{R["zemin"]}" style="font-kerning:none">{BAS2}</text>'
        f'</g>'
    )

    # Başlık 1 (ve altçizgi)
    x_bas = t1x + Y.genislik("Fredoka", 700, "YAŞI", B) - 6
    x_son = t1x + Y.genislik("Fredoka", 700, "YAŞIYOR", B) + 6
    dx_al = x_son - x_bas
    alti_d = (
        f"M{x_bas:.2f} {ALTI_Y:.2f} "
        f"C{x_bas + dx_al / 3:.2f} {ALTI_Y - 5:.2f}, "
        f"{x_bas + 2 * dx_al / 3:.2f} {ALTI_Y + 5:.2f}, "
        f"{x_son:.2f} {ALTI_Y:.2f}"
    )
    bas1 = (
        f'<g id="bas1">'
        f'<text id="bas1t" x="{t1x:.2f}" y="{T1:.2f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{B}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" stroke-width="12" '
        f'stroke-linejoin="round" style="font-kerning:none;paint-order:stroke fill">{BAS1}</text>'
        f'<path id="alti" d="{alti_d}" fill="none" stroke="{R["vurgu"]}" stroke-width="10" '
        f'stroke-linecap="round" style="opacity:0"/>'
        f'</g>'
    )

    # Künye ve altyazı
    kunye_svg = Y.kunye_svg("Hook")
    alt_svg, alt_zaman = Y.altyazi_svg(0.0, Z["sure"], ALT)

    # GSAP parametreleri
    r1_w1 = round(Y.genislik("Caveat", 700, "İstanbul'da", SAT_BOY) + 20, 2)
    r1_w2 = round(g_sat1 + 24, 2)
    r2_w = round(g_sat2 + 24, 2)

    veri = {
        "Z": Z,
        "alt": alt_zaman,
        "rz_kayma": KENAR - rz_x,
        "r1_t0": SOZ[0]["t0"],
        "r1_dur1": round(min(SOZ[0]["t1"] - SOZ[0]["t0"], Z["yazi_cap"]), 4),
        "r1_w1": r1_w1,
        "r1_t1": SOZ[1]["t0"],
        "r1_dur2": Z["yazi_cap"],
        "r1_w2": r1_w2,
        "r2_t0": SOZ[2]["t0"],
        "r2_dur": round(Z["satir2_son"] - SOZ[2]["t0"], 4),
        "r2_w": r2_w,
        "o1": [round(o1[0], 2), round(o1[1], 2)],
        "h1": [round(h1[0], 2), round(h1[1], 2)],
        "hs1": round(hs1, 4),
        "o2": [round(o2[0], 2), round(o2[1], 2)],
        "h2": [round(h2[0], 2), round(h2[1], 2)],
        "hs2": round(hs2, 4),
        "dy": DY,
    }

    sure_val = Z["sure"]
    root_attrs = (
        f'data-composition-id="main" data-start="0" data-duration="{sure_val}" '
        'data-fps="30" data-width="1080" data-height="1920"'
    )

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" {root_attrs}>
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>{clips}</defs>
{kapak_sahne}
{r1}
{r2}
{bas2}
{bas1}
{kunye_svg}<g id="altyazi">{alt_svg}</g>
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var V = {json.dumps(veri)};
  var Z = V.Z, $ = function (s) {{ return document.querySelector(s); }};
  var tl = gsap.timeline({{ paused: true }});
  function ac(o) {{ o.immediateRender = false; return o; }}

  // 0. kare durumu
  gsap.set("#ku-ders", {{ opacity: 0 }});
  gsap.set("#ku-cip", {{ opacity: 0 }});
  gsap.set("#rz0", {{ x: V.rz_kayma }});

  // Altçizgi hazırla
  var alti = $("#alti");
  if (alti) {{
    var L = alti.getTotalLength();
    alti.style.strokeDasharray = L + " " + (L + 2);
    alti.style.strokeDashoffset = L;
  }}

  // 1. Altçizgi darbesi (sine.inOut)
  tl.set("#alti", ac({{ opacity: 1 }}), Z.alti[0]);
  tl.to("#alti", ac({{ strokeDashoffset: 0, duration: Z.alti[1], ease: "sine.inOut" }}), Z.alti[0]);

  // 2. Altyazı
  V.alt.forEach(function (a) {{
    tl.set("#" + a[0], ac({{ opacity: 1 }}), a[1]);
    tl.set("#" + a[0], ac({{ opacity: 0 }}), a[2]);
  }});

  // 3. Satır 1 kırpma ile kademeli yazım
  tl.fromTo("#cr1", {{ attr: {{ width: 0 }} }},
    ac({{ attr: {{ width: V.r1_w1 }}, duration: V.r1_dur1, ease: "none" }}), V.r1_t0);
  tl.fromTo("#cr1", {{ attr: {{ width: V.r1_w1 }} }},
    ac({{ attr: {{ width: V.r1_w2 }}, duration: V.r1_dur2, ease: "none" }}), V.r1_t1);

  // 4. Rozet sağa kayar
  tl.to("#rz0", ac({{ x: 0, duration: Z.rozet_kay[1], ease: "power3.inOut" }}), Z.rozet_kay[0]);

  // 5. Sahne grubu solar
  tl.to("#kapak-sahne", ac({{ opacity: 0, duration: Z.sahne_sol[1], ease: "power1.in" }}), Z.sahne_sol[0]);

  // 6. Uçuş: başlık 1 ve başlık 2
  var u0 = Z.ucus[0], ud = Z.ucus[1], u1 = u0 + ud;
  function uc2(id, o, h, hs) {{
    // QA tur 3: her tween'de svgOrigin verilince doğrudan aramada (0 → 2,62) GSAP orijin dengelemesi x/y'yi
    // kaydırıyordu (sıralı aramada doğru). Orijin bir kez, dönüşüm yokken verilir; tween'ler yalnız x/y/scale sürer.
    gsap.set(id, {{ svgOrigin: o[0] + " " + o[1], smoothOrigin: false }});
    tl.to(id, ac({{ x: h[0] - o[0], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ y: h[1] - o[1], duration: ud, ease: "power3.inOut" }}), u0);
    tl.to(id, ac({{ scale: hs, duration: Z.ucus_olcek, ease: "power3.out" }}), u0);
    tl.to(id, ac({{ opacity: 0, duration: Z.baslik_sol[1], ease: "power1.in" }}), Z.baslik_sol[0]);
  }}
  uc2("#bas1", V.o1, V.h1, V.hs1);
  uc2("#bas2", V.o2, V.h2, V.hs2);

  // 7. Cümle satırları yukarı kayar
  tl.to("#r1", ac({{ y: V.dy, duration: ud, ease: "power3.inOut" }}), u0);
  tl.to("#r2", ac({{ y: V.dy, duration: ud, ease: "power3.inOut" }}), u0);

  // 8. Satır 2 tek süpürmeyle yazılır
  tl.fromTo("#cr2", {{ attr: {{ width: 0 }} }},
    ac({{ attr: {{ width: V.r2_w }}, duration: V.r2_dur, ease: "none" }}), V.r2_t0);

  // 9. Künye açılır
  tl.to("#ku-ders", ac({{ opacity: 1, duration: Z.kunye_ac[1], ease: "power1.out" }}), Z.kunye_ac[0]);

  // 10. Çip açılır
  tl.to("#ku-cip", ac({{ opacity: 1, duration: 0.2, ease: "power1.out" }}), u1 - 0.22);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html


# ---- 4.8 __main__ bloğu ----
if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_icerik = uret()
    (AD / "proje" / "index.html").write_text(html_icerik, encoding="utf-8")

    x0_1 = SOL + Y.genislik("Caveat", 700, "İstanbul'da yaşı-", SAT_BOY)
    x1_1 = x0_1 + Y.genislik("Caveat", 700, "yor", SAT_BOY)
    x0_2 = SOL + Y.genislik("Caveat", 700, "Amcamla yaşı-", SAT_BOY)
    x1_2 = x0_2 + Y.genislik("Caveat", 700, "yor", SAT_BOY)

    devir = {
        "font": "Caveat",
        "agirlik": 700,
        "boy": 80,
        "kerning": "none",
        "sol": 48,
        "taban": [452, 600],
        "satir": [SATIR1, SATIR2],
        "yor": [[round(x0_1, 2), round(x1_1, 2)], [round(x0_2, 2), round(x1_2, 2)]],
        "sag": [round(SOL + g_sat1, 2), round(SOL + g_sat2, 2)],
        "t": 3.0,
    }
    (AD / "devir.json").write_text(json.dumps(devir, ensure_ascii=False, indent=2), encoding="utf-8")
    print("devir:", json.dumps(devir, ensure_ascii=False))

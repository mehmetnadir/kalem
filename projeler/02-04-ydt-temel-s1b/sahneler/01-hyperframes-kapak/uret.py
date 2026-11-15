"""02-04-ydt-temel-s1b sahne 01 kanca (kol b, değişken kanca = soru) index.html üretici (HyperFrames DİKEY 1080x1920).

Kol a (02-04-ydt-temel-s1) uret.py kopyası; KBC-0204S1 (15.11) değişiklikleri, senaryo-taslak §3: başlık 2 `AYNI MI?` ·
iki Türkçe satır `Bu` / `iki` çapasında (seslendirilmez) · `yaşıyorum` çapasında iki `yor` kutusu (kol a sahne 02 kare 101
görünümü) · İngilizce etiket yok · figür 280 · uçuş yok: `aynı` çapasında başlık ve çizim solar, rozet kayar, konu adı
açılır, satırlar sahne 02 konumuna (560 / 680) kayar. Zamanlar sözcük çapasından (sozcukler.json).
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
PAKET = AD.parent.parent
ORTAK = PAKET / "ortak"
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))["sahneler"]
           if s["klasor"] == AD.name)
assert SAH["kare"] == Z["kare"] and SAH["t_bas"] == 0.0, f"zaman.json kare {SAH['kare']} != {Z['kare']}"
SOZ = [
    w for w in json.loads((ORTAK / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
    if w.get("cumle") == 1
]
assert [w["sozcuk"] for w in SOZ] == ["Bu", "iki", "yaşıyorum", "aynı", "mı?"], (
    f"Beklenen kanca sözcükleri bulunamadı: {[w['sozcuk'] for w in SOZ]}"
)
W_BU, W_IKI, W_YAS, W_AYNI = (float(SOZ[i]["t0"]) for i in range(4))
ALT = json.loads((ORTAK / "anlatim" / "altyazi.json").read_text(encoding="utf-8"))
FIG = json.loads((AD / "cizim" / "ogretmen.json").read_text(encoding="utf-8"))

try:
    BAVUL_YOLLAR = Y.tabler("luggage", AD / "cizim")
except TypeError:
    _lug_svg = (AD / "cizim" / "luggage.svg").read_text(encoding="utf-8")
    BAVUL_YOLLAR = [d for d in re.findall(r'<path d="([^"]+)"', _lug_svg) if not d.startswith("M0 0h24v24")]
EV_YOLLAR = Y.tabler("home")

# ---- 4.1 Sabitler ve türetilen ölçüler (§4.1) ----
W, H = Y.W, Y.H
KENAR = Y.HUD["kenar"]
SAG = Y.HUD["sagSinir"]
ORTA = (KENAR + SAG) / 2
BAS1 = "YAŞIYORUM"
BAS2 = "AYNI MI?"
PAD = 0.20  # em

B = math.floor(min(
    152,  # kol b: kol a başlık boyu (kapak-taslak §2); dar `AYNI MI?` ile formül 161 verir, satır 1'e 5 px kalır
    190,
    (SAG - KENAR) / Y.genislik("Fredoka", 700, BAS1, 1),
    (SAG - KENAR) / (Y.genislik("Fredoka", 700, BAS2, 1) + 2 * PAD),
))
g1 = Y.genislik("Fredoka", 700, BAS1, B)
t1x = ORTA - g1 / 2
TOP1 = 472
T1 = TOP1 + 0.70 * B
ALTI_Y = T1 + 0.20 * B
HAP_UST = ALTI_Y + 29
T2 = HAP_UST + 0.98 * B
HAP_ALT = T2 + 0.26 * B

hap_w = Y.genislik("Fredoka", 700, BAS2, B) + 2 * PAD * B
hap_x = ORTA - hap_w / 2
hap_rx = (HAP_ALT - HAP_UST) / 2
hap_h = HAP_ALT - HAP_UST

SOL = 84
SAT_BOY = 80
R1_K, R2_K = 920, 1040
R1_SON, R2_SON = 560, 680
DY = R1_SON - R1_K

ZEMIN_Y = 1372
EV_S, EV_X = 16, KENAR
EV_Y = ZEMIN_Y - 21 * EV_S

FIG_H, FIG_X = 280, 540  # kol b: 400 → 280 (satır 2 ile figür arası ≥ 24 px; taslak §3 olay 1)
x0, y0, x1, y1 = FIG["kutu"]
fs = FIG_H / (y1 - y0)
EX = FIG_X + (FIG["el"][0] - x0) * fs
EY = (ZEMIN_Y - FIG_H) + (FIG["el"][1] - y0) * fs

BV_S = round(9 * FIG_H / 400, 3)  # bavul figürle aynı oranda küçülür (kol a 9)
BX = EX + 6 - 12 * BV_S
BY = EY - 3 * BV_S
# kol b: İngilizce etiketler (I live / I am living) kalktı; cevap değer sahnesinde

SATIR1 = "İstanbul'da yaşı-yor-um."
SATIR2 = "Amcamla yaşı-yor-um."
g_sat1 = Y.genislik("Caveat", 700, SATIR1, SAT_BOY)
g_sat2 = Y.genislik("Caveat", 700, SATIR2, SAT_BOY)

# yor kutuları: kol a sahne 02 ek_ayir görünümü (x yor −5 … yor +6; taban −42 … +8; vurguDolgu %60)
YOR = []
for _on, _taban in (("İstanbul'da yaşı-", R1_K), ("Amcamla yaşı-", R2_K)):
    _x0 = SOL + Y.genislik("Caveat", 700, _on, SAT_BOY)
    YOR.append((_x0, _x0 + Y.genislik("Caveat", 700, "yor", SAT_BOY), _taban))
KUTU_UST, KUTU_ALT = 42, 8

# Künye (kol b: uçuş yok, rozet kayar, konu adı açılır)
boy = Y.konu_boyu()
rz_x, rz_w = Y.rozet_konumu()
KONU_SON = KENAR + Y.genislik("Fredoka", 700, Y.KONU, boy)

# Zamanlar (küresel sn = yerel sn): sözcük çapası + zamanlar.json payları
T_R1, T_R2 = [W_BU, Z["yazi_sure"]], [W_IKI, Z["yazi_sure"]]
T_K1, T_K2 = [W_YAS, Z["kutu_sure"]], [round(W_YAS + Z["kutu_ara"], 3), Z["kutu_sure"]]
T_BSOL, T_SSOL = [W_AYNI, Z["baslik_sol_sure"]], [W_AYNI, Z["sahne_sol_sure"]]
T_RZ = [W_AYNI, Z["rozet_kay_sure"]]
T_KAY = [round(W_AYNI + Z["satir_kay"][0], 3), Z["satir_kay"][1]]
T_KONU = [round(W_AYNI + Z["kunye_ac"][0], 3), Z["kunye_ac"][1]]


# ---- 4.6 Denetimler ----
def _p_in(p: float) -> float:
    """GSAP power1.in."""
    p = max(0.0, min(1.0, p))
    return p * p


def _p3_in_out(p: float) -> float:
    """GSAP power3.inOut."""
    p = max(0.0, min(1.0, p))
    return 4.0 * p ** 3 if p < 0.5 else 1.0 - ((-2.0 * p + 2.0) ** 3) / 2.0


def _denetimler() -> None:
    # 1. B, hap, baslik 1
    assert 140 <= B <= 190, f"B={B} aralık [140, 190] dışı"
    assert hap_x >= KENAR and hap_x + hap_w <= SAG, (
        f"hap x={hap_x:.2f}..{hap_x + hap_w:.2f} aralık [{KENAR}, {SAG}] dışı"
    )
    assert t1x >= KENAR and t1x + g1 <= SAG, (
        f"baslik 1 x={t1x:.2f}..{t1x + g1:.2f} aralık [{KENAR}, {SAG}] dışı"
    )
    assert (T1 - 0.70 * B) >= Y.HUD["icerikBas"], (
        f"baslik 1 üstü {T1 - 0.70 * B:.2f} < icerikBas {Y.HUD['icerikBas']}"
    )

    # 2. Satır metinleri
    assert len(SATIR1) <= 24, f"satir 1 {len(SATIR1)} > 24 karakter"
    assert len(SATIR2) <= 24, f"satir 2 {len(SATIR2)} > 24 karakter"
    assert SOL + g_sat1 <= SAG, f"satir 1 {SOL + g_sat1:.2f} > SAG {SAG}"
    assert SOL + g_sat2 <= SAG, f"satir 2 {SOL + g_sat2:.2f} > SAG {SAG}"

    # 3. Kapak dikey sıra (>= 24 px ara)
    r1_ust = R1_K - 0.864 * SAT_BOY
    r2_alt = R2_K + 0.212 * SAT_BOY  # kol b: kapak karesinde iki satır var
    fig_ust = ZEMIN_Y - FIG_H
    ev_ust = EV_Y + 3 * EV_S

    assert r1_ust - HAP_ALT >= 24, f"HAP_ALT -> satır 1 üstü ara {r1_ust - HAP_ALT:.2f} < 24"
    assert fig_ust - r2_alt >= 24, f"satır 2 altı -> figür üstü ara {fig_ust - r2_alt:.2f} < 24"
    assert ev_ust - r2_alt >= 24, f"satır 2 altı -> ev üstü ara {ev_ust - r2_alt:.2f} < 24"
    assert all(kt + KUTU_ALT < r2_alt and kt - KUTU_UST > HAP_ALT for (_a, _b, kt) in YOR), "yor kutusu bant dışı"
    assert BY + 21 * BV_S <= ZEMIN_Y, f"bavul altı {BY + 21 * BV_S:.2f} > ZEMIN_Y {ZEMIN_Y}"
    assert ZEMIN_Y + 2 <= Y.HUD["icerikSon"], f"ZEMIN_Y + 2 = {ZEMIN_Y + 2} > icerikSon {Y.HUD['icerikSon']}"

    # 4. Yatay
    assert BX + 18 * BV_S <= SAG, f"bavul sağı {BX + 18 * BV_S:.2f} > SAG {SAG}"
    assert EV_X + 21 * EV_S + 20 <= FIG_X, f"ev sağı + 20 = {EV_X + 21 * EV_S + 20} > FIG_X {FIG_X}"
    assert EV_X + 3 * EV_S >= KENAR, f"ev solu {EV_X + 3 * EV_S:.2f} < KENAR {KENAR}"

    # 5. Son hal
    assert R1_SON - 0.864 * SAT_BOY >= Y.HUD["icerikBas"], (
        f"R1_SON üstü {R1_SON - 0.864 * SAT_BOY:.2f} < icerikBas {Y.HUD['icerikBas']}"
    )
    assert R2_SON + 0.212 * SAT_BOY <= Y.HUD["icerikSon"], (
        f"R2_SON altı {R2_SON + 0.212 * SAT_BOY:.2f} > icerikSon {Y.HUD['icerikSon']}"
    )
    assert R2_SON - R1_SON == 120, f"R2_SON - R1_SON = {R2_SON - R1_SON} != 120"

    # 6. Zaman: kapak karesi kutulardan sonra, "aynı"dan önce; hareket son 12 kareden önce biter
    son = (Z["kare"] - 12) / 30.0
    assert T_R2[0] + T_R2[1] < T_K1[0], "satır 2 yazımı kutudan önce bitmeli"
    assert T_K2[0] + T_K2[1] < Z["kapak_t"] < W_AYNI, f"kapak_t {Z['kapak_t']} sırası bozuk"
    for ad, (t0, d) in (("rozet", T_RZ), ("satır kayması", T_KAY), ("konu", T_KONU), ("çizim", T_SSOL)):
        assert t0 + d <= son + 1e-6, f"{ad} bitişi {t0 + d:.3f} > {son:.3f}"

    # 7. Kayma çakışma örneklemesi (kare kare): başlık görünürken (opaklık >= 0,05) satır 1 hapın altında kalır;
    #    konu adı görünürken rozet konu adının sağında kalır.
    t = W_AYNI
    while t <= son + 1e-6:
        dy = DY * _p3_in_out((t - T_KAY[0]) / T_KAY[1])
        if 1.0 - _p_in((t - T_BSOL[0]) / T_BSOL[1]) >= 0.05:
            assert R1_K - 0.864 * SAT_BOY + dy >= HAP_ALT + 6, f"t={t:.3f}: satır 1 başlık hapına girdi"
        rzx = KENAR + (rz_x - KENAR) * _p3_in_out((t - T_RZ[0]) / T_RZ[1])
        if (t - T_KONU[0]) / T_KONU[1] >= 0.05:
            assert rzx >= KONU_SON + 6, f"t={t:.3f}: rozet ({rzx:.1f}) konu adına ({KONU_SON:.1f}) değdi"
        t += 1.0 / 30.0


_denetimler()


# ---- 4.7 Zamanlar fonksiyonu ----
def zamanlar() -> dict:
    """olay.py tarafından okunan olay zamanları."""
    return {
        "alti": [Z["alti"][0], Z["alti"][1]],
        "r1": T_R1,
        "r2": T_R2,
        "yk1": T_K1,
        "yk2": T_K2,
        "kay": T_KAY,
        "konu": T_KONU,
    }


# ---- 4.7 uret() fonksiyonu ----
def uret() -> str:
    R = Y.RENK

    # Kırpma kutuları
    clips = (
        f'<clipPath id="cp1"><rect id="cr1" x="{SOL - 12}" y="{R1_K - SAT_BOY}" width="0" '
        f'height="{int(SAT_BOY * 1.35)}"/></clipPath>'
        f'<clipPath id="cp2"><rect id="cr2" x="{SOL - 12}" y="{R2_K - SAT_BOY}" width="0" '
        f'height="{int(SAT_BOY * 1.35)}"/></clipPath>'
    ) + "".join(  # kol b: yor kutuları soldan sağa açılır
        f'<clipPath id="ck{i + 1}"><rect id="kr{i + 1}" x="{kx0 - 7:.2f}" y="{kt - KUTU_UST - 2}" width="0" '
        f'height="{KUTU_UST + KUTU_ALT + 4}"/></clipPath>'
        for i, (kx0, _kx1, kt) in enumerate(YOR)
    )

    # Çizimler
    # 1. Yer
    zc_path = f'<path id="zc" d="M{KENAR + 4} {ZEMIN_Y} L{SAG - 4} {ZEMIN_Y}" stroke-width="4"/>'

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

    # kol b: İngilizce etiket yok
    kapak_sahne = f'<g id="kapak-sahne">{eskiz}</g>'

    def kutu(i: int) -> str:
        """yor kutusu: yazının altında, satırla aynı grupta (satırla birlikte kayar)."""
        kx0, kx1, kt = YOR[i]
        a, b, ust, alt = kx0 - 5, kx1 + 6, kt - KUTU_UST, kt + KUTU_ALT
        d = f"M{a + 4:.2f} {ust + 1} L{b:.2f} {ust} L{b - 4:.2f} {alt} L{a:.2f} {alt + 1} Z"
        return (f'<path id="yk{i + 1}" d="{d}" stroke="none" fill-opacity="0.6" '
                f'style="fill:var(--vurguDolgu,#f2a93b)" clip-path="url(#ck{i + 1})"/>')

    # Cümle satırları
    r1 = (
        f'<g id="r1">{kutu(0)}<text x="{SOL}" y="{R1_K}" font-family="Caveat" font-weight="700" font-size="{SAT_BOY}" '
        f'fill="{R["murekkep"]}" clip-path="url(#cp1)" style="font-kerning:none">{SATIR1}</text></g>'
    )
    r2 = (
        f'<g id="r2">{kutu(1)}<text x="{SOL}" y="{R2_K}" font-family="Caveat" font-weight="700" font-size="{SAT_BOY}" '
        f'fill="{R["murekkep"]}" clip-path="url(#cp2)" style="font-kerning:none">{SATIR2}</text></g>'
    )

    # Başlık 2 (hap)
    bas2 = (
        f'<g id="bas2">'
        f'<rect id="hap" x="{hap_x:.2f}" y="{HAP_UST:.2f}" width="{hap_w:.2f}" height="{hap_h:.2f}" '
        f'rx="{hap_rx:.2f}" fill="{R["vurgu"]}"/>'
        f'<text id="bas2t" x="{ORTA}" y="{T2:.2f}" text-anchor="middle" font-family="Fredoka" '
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
    kunye_svg = Y.kunye_svg()
    alt_svg, alt_zaman = Y.altyazi_svg(0.0, Z["sure"], ALT)

    # GSAP parametreleri (kol b)
    veri = {
        "Z": Z,
        "alt": alt_zaman,
        "rz_kayma": KENAR - rz_x,
        "r1": T_R1, "r1_w": round(g_sat1 + 24, 2),
        "r2": T_R2, "r2_w": round(g_sat2 + 24, 2),
        "k1": T_K1, "k2": T_K2,
        "kw": [round(kx1 - kx0 + 25, 2) for (kx0, kx1, _kt) in YOR],
        "bsol": T_BSOL, "ssol": T_SSOL, "rz": T_RZ, "kay": T_KAY, "konu": T_KONU,
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
  gsap.set("#ku-konu", {{ opacity: 0 }});
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

  // 3. Satır 1 ("Bu") ve satır 2 ("iki") kırpma ile yazılır (kol b; satırlar seslendirilmez)
  tl.fromTo("#cr1", {{ attr: {{ width: 0 }} }}, ac({{ attr: {{ width: V.r1_w }}, duration: V.r1[1], ease: "none" }}), V.r1[0]);
  tl.fromTo("#cr2", {{ attr: {{ width: 0 }} }}, ac({{ attr: {{ width: V.r2_w }}, duration: V.r2[1], ease: "none" }}), V.r2[0]);

  // 4. ek_ayir ("yaşıyorum"): iki yor kutusu soldan sağa çizilir
  tl.fromTo("#kr1", {{ attr: {{ width: 0 }} }}, ac({{ attr: {{ width: V.kw[0] }}, duration: V.k1[1], ease: "power1.out" }}), V.k1[0]);
  tl.fromTo("#kr2", {{ attr: {{ width: 0 }} }}, ac({{ attr: {{ width: V.kw[1] }}, duration: V.k2[1], ease: "power1.out" }}), V.k2[0]);

  // 5. "aynı": başlık ve çizim solar (uçuş yok), rozet sağa kayar
  tl.to(["#bas1", "#bas2"], ac({{ opacity: 0, duration: V.bsol[1], ease: "power1.in" }}), V.bsol[0]);
  tl.to("#kapak-sahne", ac({{ opacity: 0, duration: V.ssol[1], ease: "power1.in" }}), V.ssol[0]);
  tl.to("#rz0", ac({{ x: 0, duration: V.rz[1], ease: "power3.inOut" }}), V.rz[0]);

  // 6. Satırlar yor kutularıyla sahne 02 konumuna kayar; 7. konu adı açılır
  tl.to(["#r1", "#r2"], ac({{ y: V.dy, duration: V.kay[1], ease: "power3.inOut" }}), V.kay[0]);
  tl.to("#ku-konu", ac({{ opacity: 1, duration: V.konu[1], ease: "power1.out" }}), V.konu[0]);

  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    return html


# ---- 4.7 __main__ bloğu ----
if __name__ == "__main__":
    (AD / "proje").mkdir(exist_ok=True)
    Y.font_kopyala(AD / "proje" / "assets" / "fonts")
    html_icerik = uret()
    (AD / "proje" / "index.html").write_text(html_icerik, encoding="utf-8")

    (x0_1, x1_1, _t1), (x0_2, x1_2, _t2) = YOR

    devir = {
        "font": "Caveat",
        "agirlik": 700,
        "boy": 80,
        "kerning": "none",
        "sol": SOL,
        "taban": [R1_SON, R2_SON],
        "satir": [SATIR1, SATIR2],
        "yor": [[round(x0_1, 2), round(x1_1, 2)], [round(x0_2, 2), round(x1_2, 2)]],
        "sag": [round(SOL + g_sat1, 2), round(SOL + g_sat2, 2)],
        "yor_kutusu": "kol b: sahne 01'de çizilir; sahne 02 kare 0'da hazır",
        "t": SAH["t_son"],
        "not": "kol b (KBC-0204S1, 15.11): sahne 02 Y_L1/Y_L2 560/680, SOL = kenar 60 + 24",
    }
    (AD / "devir.json").write_text(json.dumps(devir, ensure_ascii=False, indent=2), encoding="utf-8")
    print("devir:", json.dumps(devir, ensure_ascii=False))

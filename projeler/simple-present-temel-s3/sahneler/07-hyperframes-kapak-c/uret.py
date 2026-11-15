#!/usr/bin/python3
"""Sahne 07 kapak C (kural + karşıt çift) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
Durağan PNG üretimi için tek kare zaman çizelgesi (1,0 sn).
Bantlar: kanal (280–350) → künye (360–450) → içerik (460–1380: başlık 470–748, kart 1 840–1040, kart 2 1100–1300) → alt boş.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent

# zaman.json ve zamanlar.json okuma ve doğrulama (SPEC §2)
zaman_data = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
duragan_kayitlar = [d for d in zaman_data.get("duragan", []) if d.get("klasor") == AD.name]
assert len(duragan_kayitlar) == 1, "duragan içinde " + AD.name + " tek kayıt olmalı"
duragan_kayit = duragan_kayitlar[0]
kare_val = duragan_kayit["kare"]
cikti_val = duragan_kayit["cikti"]
assert kare_val == 1, f"kare {kare_val} != 1"
assert cikti_val == "kapak-c.png", f"cikti {cikti_val} != kapak-c.png"
assert AD.name not in [s["klasor"] for s in zaman_data["sahneler"]], f"{AD.name} sahneler[] içinde olmamalı"

Z = json.loads((AD / "zamanlar.json").read_text(encoding="utf-8"))
assert Z["sure"] == 1.0, f"sure {Z['sure']} != 1.0"
assert Z["kare"] == 1, f"kare {Z['kare']} != 1"
assert Z["fps"] == 30, f"fps {Z['fps']} != 30"

R = Y.RENK
assert set(R.keys()) >= {"zemin", "murekkep", "ikincil", "vurgu", "kirmizi"}

W, H = Y.W, Y.H
KENAR = Y.HUD["kenar"]
SAG = Y.HUD["sagSinir"]
ICERIK_BAS = Y.HUD["icerikBas"]
ICERIK_SON = Y.HUD["icerikSon"]
ORTA = (KENAR + SAG) / 2.0
BASLIK_GEN = 900
BASLIK_UST = 470
KONTUR = 10
SAT1 = "DOES VARSA"
SAT2 = "FİİL YALIN"
KB = 72
KX = 60
KW = 900
KH = 200
KRX = 24
K1_Y = 840
K2_Y = 1100
KYX = 108
IM = 72
IM_X = 848
CAP = 0.691
NOKTA = 0.921
ALT = 0.22


def hesapla_baslik() -> tuple[int, float, float, float]:
    """Başlık S boyutu ve yerleşim ölçülerini hesaplar (SPEC §4.2)."""
    def gm(s: float) -> float:
        return max(Y.genislik("Fredoka", 700, SAT1, s), Y.genislik("Fredoka", 700, SAT2, s))

    S = int(math.floor(min(190.0, (BASLIK_GEN - KONTUR) * 100.0 / gm(100.0))))
    while gm(float(S)) + KONTUR > BASLIK_GEN and S > 1:
        S -= 1

    T1 = BASLIK_UST + CAP * S + KONTUR / 2.0
    T2 = T1 + 1.12 * S
    baslik_alt = T2 + 0.009 * S + KONTUR / 2.0
    return S, T1, T2, baslik_alt


def baslik_svg(S: int, T1: float, T2: float) -> str:
    """Başlık grubu SVG çıktısı (SPEC §4.2)."""
    bs_1 = (
        f'<text id="bs-1" x="{ORTA:.0f}" y="{T1:.2f}" text-anchor="middle" font-family="Fredoka" '
        f'font-weight="700" font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" '
        f'stroke-width="{KONTUR}" stroke-linejoin="round" '
        f'style="font-kerning:none;paint-order:stroke fill">{SAT1}</text>'
    )
    bs_2 = (
        f'<text id="bs-2" x="{ORTA:.0f}" y="{T2:.2f}" text-anchor="middle" font-family="Fredoka" '
        f'font-weight="700" font-size="{S}" fill="{R["murekkep"]}" stroke="{R["zemin"]}" '
        f'stroke-width="{KONTUR}" stroke-linejoin="round" '
        f'style="font-kerning:none;paint-order:stroke fill">{SAT2}</text>'
    )
    return f'<g id="baslik">{bs_1}{bs_2}</g>'


def kart1_svg() -> str:
    """Kart 1 (soluk, yanlış) SVG çıktısı (SPEC §4.3)."""
    zemin = (
        f'<rect id="k1-zemin" x="{KX}" y="{K1_Y}" width="{KW}" height="{KH}" rx="{KRX}" '
        f'fill="{R["ikincil"]}" fill-opacity="0.08"/>'
    )
    cerceve = (
        f'<rect id="k1-cerceve" x="{KX + 2}" y="{K1_Y + 2}" width="{KW - 4}" height="{KH - 4}" '
        f'rx="{KRX - 2}" fill="none" stroke="{R["ikincil"]}" stroke-width="4"/>'
    )
    t1 = K1_Y + KH / 2.0 + 0.35 * KB
    yazi = (
        f'<text id="k1-yazi" x="{KYX}" y="{t1:.1f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{KB}" fill="{R["ikincil"]}" style="font-kerning:none">'
        f'He doesn\'t go<tspan id="k1-es">es</tspan>.</text>'
    )
    x_es = KYX + Y.genislik("Fredoka", 700, "He doesn't go", KB)
    w_es = Y.genislik("Fredoka", 700, "es", KB)
    cizik = (
        f'<path id="k1-cizik" d="M{x_es + 4.0:.1f} {t1 - 17.0:.1f} L{x_es + w_es - 2.0:.1f} {t1 - 24.0:.1f}" '
        f'fill="none" stroke="{R["kirmizi"]}" stroke-width="7" stroke-linecap="round"/>'
    )
    oy = K1_Y + KH // 2
    carpi = (
        f'<path id="k1-carpi" d="M{IM_X + 4} {oy - 32} Q{IM_X + 38} {oy + 2} {IM_X + 68} {oy + 34} '
        f'M{IM_X + 68} {oy - 34} Q{IM_X + 36} {oy + 2} {IM_X + 6} {oy + 32}" '
        f'fill="none" stroke="{R["kirmizi"]}" stroke-width="9" stroke-linecap="round"/>'
    )
    return f'<g id="kart1">{zemin}{cerceve}{yazi}{cizik}{carpi}</g>'


def kart2_svg() -> str:
    """Kart 2 (doğru) SVG çıktısı (SPEC §4.4)."""
    zemin = (
        f'<rect id="k2-zemin" x="{KX}" y="{K2_Y}" width="{KW}" height="{KH}" rx="{KRX}" '
        f'fill="{R["murekkep"]}" fill-opacity="0.06"/>'
    )
    cerceve = (
        f'<rect id="k2-cerceve" x="{KX + 2}" y="{K2_Y + 2}" width="{KW - 4}" height="{KH - 4}" '
        f'rx="{KRX - 2}" fill="none" stroke="{R["murekkep"]}" stroke-width="4"/>'
    )
    t2 = K2_Y + KH / 2.0 + 0.35 * KB
    x_go = KYX + Y.genislik("Fredoka", 700, "He doesn't ", KB)
    w_go = Y.genislik("Fredoka", 700, "go", KB)
    alt = (
        f'<path id="k2-alt" d="M{x_go - 6.0:.1f} {t2 + 30.0:.1f} Q{x_go + w_go / 2.0:.1f} {t2 + 24.0:.1f} '
        f'{x_go + w_go + 8.0:.1f} {t2 + 27.0:.1f}" fill="none" stroke="{R["vurgu"]}" '
        f'stroke-width="9" stroke-linecap="round"/>'
    )
    yazi = (
        f'<text id="k2-yazi" x="{KYX}" y="{t2:.1f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{KB}" fill="{R["murekkep"]}" style="font-kerning:none">He doesn\'t go.</text>'
    )
    oy2 = K2_Y + KH // 2
    tik = (
        f'<path id="k2-tik" d="M{IM_X + 4} {oy2 + 2} L{IM_X + 28} {oy2 + 30} Q{IM_X + 42} {oy2 - 4} '
        f'{IM_X + 70} {oy2 - 34}" fill="none" stroke="{R["murekkep"]}" stroke-width="9" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )
    return f'<g id="kart2">{zemin}{cerceve}{alt}{yazi}{tik}</g>'


def blok_kutulari(S: int, T1: float, baslik_alt: float) -> list[dict[str, float]]:
    """Yerleşim bloklarının kutularını hesaplar (SPEC §6)."""
    w_kanal = Y.HUD["kanalYaziX"] + Y.genislik("Lexend", 700, Y.KANAL_YAZI, 42) - 60.0
    kanal = {"ad": "kanal", "x": 60.0, "y": 280.0, "w": w_kanal, "h": 70.0}

    rx, rw = Y.rozet_konumu()
    assert rx + rw <= 960.0, f"rozet sag {rx + rw} > 960"
    kunye = {"ad": "kunye", "x": 60.0, "y": 360.0, "w": rx + rw - 60.0, "h": 90.0}

    gm_S = max(Y.genislik("Fredoka", 700, SAT1, S), Y.genislik("Fredoka", 700, SAT2, S))
    baslik_x = ORTA - gm_S / 2.0 - KONTUR / 2.0
    baslik_y = T1 - CAP * S - KONTUR / 2.0
    baslik = {
        "ad": "baslik",
        "x": baslik_x,
        "y": baslik_y,
        "w": gm_S + KONTUR,
        "h": baslik_alt - baslik_y,
    }

    kart1 = {"ad": "kart1", "x": float(KX), "y": float(K1_Y), "w": float(KW), "h": float(KH)}
    kart2 = {"ad": "kart2", "x": float(KX), "y": float(K2_Y), "w": float(KW), "h": float(KH)}

    return [kanal, kunye, baslik, kart1, kart2]


def kesisim(b1: dict[str, float], b2: dict[str, float]) -> float:
    """İki kutu arasındaki kesişim alanını döndürür."""
    dx = max(0.0, min(b1["x"] + b1["w"], b2["x"] + b2["w"]) - max(b1["x"], b2["x"]))
    dy = max(0.0, min(b1["y"] + b1["h"], b2["y"] + b2["h"]) - max(b1["y"], b2["y"]))
    return dx * dy


def kurallari_dogrula(
    bloklar: list[dict[str, float]],
    S: int,
    T1: float,
    T2: float,
    baslik_alt: float,
    html: str,
) -> None:
    """SPEC.md §6 kurallarını doğrular."""
    # 1. Her blok sınır kontrolü
    for b in bloklar:
        ad = b["ad"]
        assert b["x"] >= 0.0, f"{ad} sol {b['x']} < 0"
        assert b["x"] + b["w"] <= 960.0 + 1e-4, f"{ad} sağ {b['x'] + b['w']} > 960"
        assert b["y"] >= 280.0 - 1e-4, f"{ad} üst {b['y']} < 280"
        assert b["y"] + b["h"] <= 1380.0 + 1e-4, f"{ad} alt {b['y'] + b['h']} > 1380"

    icerik_ogeleri = [b for b in bloklar if b["ad"] in ("baslik", "kart1", "kart2")]
    for b in icerik_ogeleri:
        ad = b["ad"]
        assert b["x"] >= KENAR - 1e-4, f"{ad} sol {b['x']} < {KENAR}"
        assert b["x"] + b["w"] <= SAG + 1e-4, f"{ad} sağ {b['x'] + b['w']} > {SAG}"
        assert b["y"] >= ICERIK_BAS - 1e-4, f"{ad} üst {b['y']} < {ICERIK_BAS}"
        assert b["y"] + b["h"] <= ICERIK_SON + 1e-4, f"{ad} alt {b['y'] + b['h']} > {ICERIK_SON}"

    # 2. Rozet sağ ve çiftler arası kesişim 0
    rx, rw = Y.rozet_konumu()
    assert rx + rw <= 960.0, f"rozet sağ {rx + rw} > 960"
    for i in range(len(bloklar)):
        for j in range(i + 1, len(bloklar)):
            k = kesisim(bloklar[i], bloklar[j])
            ad1, ad2 = bloklar[i]["ad"], bloklar[j]["ad"]
            assert k == 0.0, f"Kesişim {ad1} - {ad2}: {k}"

    # 3. Dikey aralar
    b_dict = {b["ad"]: b for b in bloklar}
    assert b_dict["kart1"]["y"] - baslik_alt >= 48.0, (
        f"baslik alt -> kart1 ara {b_dict['kart1']['y'] - baslik_alt} < 48"
    )
    kart1_alt = b_dict["kart1"]["y"] + b_dict["kart1"]["h"]
    assert b_dict["kart2"]["y"] - kart1_alt >= 40.0, (
        f"kart1 alt -> kart2 ara {b_dict['kart2']['y'] - kart1_alt} < 40"
    )

    # 4. Başlık
    gm_S = max(Y.genislik("Fredoka", 700, SAT1, S), Y.genislik("Fredoka", 700, SAT2, S))
    assert S >= 64, f"Başlık boyutu S={S} < 64"
    assert S <= 190, f"Başlık boyutu S={S} > 190"
    assert gm_S + KONTUR <= BASLIK_GEN + 1e-4, f"gm(S) + KONTUR = {gm_S + KONTUR} > {BASLIK_GEN}"
    assert T2 - NOKTA * S - KONTUR / 2.0 > T1 + KONTUR / 2.0, "İ noktası T1 + KONTUR/2 den yukarıda olmalı"
    assert baslik_alt <= 800.0, f"baslik_alt {baslik_alt} > 800"

    # 5. Kart içi
    t1_val = K1_Y + KH / 2.0 + 0.35 * KB
    t2_val = K2_Y + KH / 2.0 + 0.35 * KB
    oy = K1_Y + KH // 2
    oy2 = K2_Y + KH // 2
    g_goes = Y.genislik("Fredoka", 700, "He doesn't goes.", KB)
    assert KYX + g_goes + 40.0 <= IM_X, f"yazı ile işaret arası < 40: {KYX + g_goes + 40.0} > {IM_X}"
    assert IM_X + IM <= KX + KW - 24, f"işaret kutusu sağ {IM_X + IM} > {KX + KW - 24}"
    assert oy - IM / 2.0 >= K1_Y and oy + IM / 2.0 <= K1_Y + KH, "oy +/- IM/2 kart1 içinde değil"
    assert oy2 - IM / 2.0 >= K2_Y and oy2 + IM / 2.0 <= K2_Y + KH, "oy2 +/- IM/2 kart2 içinde değil"
    assert t1_val - CAP * KB >= K1_Y + 24, "kart1 yazı üstü payı < 24"
    assert t2_val + ALT * KB <= K2_Y + KH - 24, "kart2 yazı altı payı < 24"
    assert t2_val + 30.0 + 4.5 <= K2_Y + KH - 12, "altçizgi kart2 alt sınırını aşıyor"
    assert t2_val + 24.0 - 4.5 > t2_val + ALT * KB, "altçizgi g kuyruğuna değiyor"

    # 6. Yazı boyu ve satırlar
    assert KB >= 64, f"KB={KB} < 64"
    satirlar = [SAT1, SAT2, "He doesn't goes.", "He doesn't go."]
    for s in satirlar:
        assert len(s) <= 24, f"Satır uzunluğu {len(s)} > 24: {s}"

    # 7. Renk sayımı
    assert html.count(R["kirmizi"]) == 2, f"kirmizi sayisi {html.count(R['kirmizi'])} != 2"
    assert html.count(R["vurgu"]) == 2, f"vurgu sayisi {html.count(R['vurgu'])} != 2"
    assert "#167a4a" not in html and "green" not in html, "Yeşil renk bulunmamalı"
    assert "✗" not in html and "✓" not in html, "✗ ve ✓ karakterleri bulunmamalı"
    assert not any(0x1F300 <= ord(c) <= 0x1FAFF for c in html), "Emoji bulunmamalı"

    # 8. HTML id kontrolleri
    assert html.count('id="kanal"') == 1, "id=kanal 1 kez olmalı"
    assert html.count('id="logoimg"') == 1, "id=logoimg 1 kez olmalı"
    assert html.count("<image") == 1, "<image 1 kez olmalı"
    for req_id in (
        "bs-1", "bs-2", "k1-zemin", "k1-cerceve", "k1-yazi", "k1-es",
        "k1-cizik", "k1-carpi", "k2-zemin", "k2-cerceve", "k2-yazi", "k2-alt", "k2-tik"
    ):
        assert f'id="{req_id}"' in html, f"id={req_id} bulunamadı"
    for banned_id in ("bk-kutu", "eskiz", "fig", "ku-cip"):
        assert f'id="{banned_id}"' not in html, f"id={banned_id} bulunmamalı"


def uret() -> tuple[str, int, list[dict[str, float]]]:
    """Sahne HTML'i ve nesnelerini üretir (SPEC §7)."""
    S, T1, T2, baslik_alt = hesapla_baslik()
    kunye = Y.kunye_svg()
    baslik = baslik_svg(S, T1, T2)
    kart1 = kart1_svg()
    kart2 = kart2_svg()

    bloklar = blok_kutulari(S, T1, baslik_alt)

    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
{Y.ZEMIN_CSS}
#sahne{{position:absolute;left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0"
     data-duration="{Z['sure']}" data-fps="30" data-width="1080" data-height="1920">
{Y.zemin_html()}
<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
{kunye}
{baslik}
{kart1}
{kart2}
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var tl = gsap.timeline({{ paused: true }});
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, 0);
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, {Z['sure']});
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""

    kurallari_dogrula(bloklar, S, T1, T2, baslik_alt, html)
    return html, S, bloklar


if __name__ == "__main__":
    proje_dizini = AD / "proje"
    proje_dizini.mkdir(exist_ok=True)
    Y.font_kopyala(proje_dizini / "assets" / "fonts")
    html, S, bloklar = uret()
    (proje_dizini / "index.html").write_text(html, encoding="utf-8")

    nesneler = [
        {
            "ad": b["ad"],
            "x": int(round(b["x"])),
            "y": int(round(b["y"])),
            "w": int(round(b["w"])),
            "h": int(round(b["h"])),
        }
        for b in bloklar
    ]
    (AD / "nesneler.json").write_text(json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"index.html yazıldı {len(html)}")
    print(f"S={S}")

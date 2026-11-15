#!/usr/bin/python3
"""simple-present-temel ana ders kapağı: HyperFrames durağan kare (kapak standardı v1, §2).

  /usr/bin/python3 uret.py --tema acik|koyu --duzen yatay|dikey [--cikti <proje dizini>]

yatay = 1920x1080 (ana paket), dikey = 1080x1920 (-dikey paketinin uret.py'si bu dosyayı çağırır).
İki düzen ayrı dizilir (kırpma yok). Yazı SVG ile dizilir; görseller hazır şeffaf PNG (ortak/kapak/).
Kurallar assert ile denetlenir: yazı ile görsel çakışmaz, boş bölgeler boş, kenar payı.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from PIL import Image

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

# Görsel ve logo, çıktının paketinden okunur (main() çıktı dizinine göre değiştirir; -dikey paketinde ortak/kapak göreli bağ).
KAPAK = AD.parent.parent / "ortak" / "kapak"
LOGO = AD.parent.parent / "ortak" / "logo"

# Kapak metni (şef kararı; değiştirme)
SATIR1 = "GİDER"
SATIR2 = "= GOES"
KUCUK_SOL = "he · she · it"
KUCUK_SAG = "-s"
ROZET = "YDT · TEMEL"

KREM = "#f3efe6"
SARI = "#fece00"
SIYAH = "#141414"
KENAR_PX = 10  # çıkartma kenarı (standart §2)

TEMA: dict[str, dict[str, str | None]] = {
    "acik": {"zemin": SARI, "yazi": SIYAH, "kutu": SIYAH, "kutuYazi": KREM, "daire": KREM},
    "koyu": {"zemin": SIYAH, "yazi": KREM, "kutu": SARI, "kutuYazi": SIYAH, "daire": None},
}


@dataclass
class Kutu:
    ad: str
    x0: float
    y0: float
    x1: float
    y1: float

    def genis(self, e: float) -> "Kutu":
        return Kutu(self.ad, self.x0 - e, self.y0 - e, self.x1 + e, self.y1 + e)


@dataclass
class Gorsel:
    ad: str
    dosya: str
    sol: float
    ust: float
    olcek: float
    kirp: int = 0  # >0: görsel bu piksel satırında düz kesilir (çıkartma kenarı kesik boyunca da çizilir)


@dataclass
class Duzen:
    W: int
    H: int
    S: float          # ana yazı boyu (Fredoka 700)
    L: float          # küçük satır boyu (Lexend 700)
    R: float          # rozet yazı boyu (Lexend 700)
    X0: float         # sol hiza (görünür mürekkep)
    LOGO_UST: float   # logo görünür üst
    LOGO_H: float     # logo kutu yüksekliği (svg viewBox 1920x476,3)
    T1: float         # satır 1 taban
    ROZET_ALT: float
    karakter: Gorsel
    nesne: Gorsel
    daire: tuple[float, float, float]
    serbest: Kutu     # yazı ve görsel bu kutunun içinde kalır (alt_kesik ise karakter alttan taşabilir)
    alt_kesik: bool   # karakter kapağın alt kenarından taşar (bel üstü)
    bos: list[Kutu]   # yalnız zemin olacak bölgeler


def sinir(aile: str, agirlik: int, ch: str) -> tuple[float, float, float, float, float]:
    """Glifin (xMin, yMin, xMax, yMax, ilerleme) değerleri, em biriminde; glif yoksa hata (yedek yazı tipine düşer)."""
    for bolge in ("latin", "latin-ext"):
        f = Y._font(aile, agirlik, bolge)
        g = f.getBestCmap().get(ord(ch))
        if g:
            u = f["head"].unitsPerEm
            p = BoundsPen(f.getGlyphSet())
            f.getGlyphSet()[g].draw(p)
            b = p.bounds or (0, 0, 0, 0)
            return b[0] / u, b[1] / u, b[2] / u, b[3] / u, f["hmtx"][g][0] / u
    raise AssertionError(f"glif yok: {aile} {agirlik} {ch!r}")


def gorunur(aile: str, agirlik: int, metin: str, boy: float) -> tuple[float, float]:
    """(sol yan boşluk px, mürekkep genişliği px). Her harf glif denetiminden geçer."""
    for ch in metin:
        if ch != " ":
            sinir(aile, agirlik, ch)
    sol = sinir(aile, agirlik, metin[0])[0] * boy
    son = sinir(aile, agirlik, metin[-1])
    return sol, Y.genislik(aile, agirlik, metin, boy) - sol - (son[4] - son[2]) * boy


ALFA: dict[tuple[str, int], Image.Image] = {}


def alfa(dosya: str, kirp: int = 0) -> Image.Image:
    if (dosya, kirp) not in ALFA:
        a = Image.open(KAPAK / dosya).getchannel("A").point(lambda v: 255 if v > 32 else 0)
        ALFA[(dosya, kirp)] = a.crop((0, 0, a.width, kirp)) if kirp else a
    return ALFA[(dosya, kirp)]


def gorsel_kutusu(g: Gorsel) -> Kutu:
    """Görselin mürekkep (alfa) sınır kutusu, kapak koordinatında."""
    b = alfa(g.dosya, g.kirp).getbbox()
    assert b is not None
    o = g.olcek
    return Kutu(g.ad, g.sol + b[0] * o, g.ust + b[1] * o, g.sol + b[2] * o, g.ust + b[3] * o)


def degiyor(g: Gorsel, k: Kutu) -> bool:
    """Görselin opak pikseli k kutusuna düşüyor mu (kutuyu çağıran kenar + pay kadar genişletir)."""
    a = alfa(g.dosya, g.kirp)
    x0 = max(0, int((k.x0 - g.sol) / g.olcek))
    y0 = max(0, int((k.y0 - g.ust) / g.olcek))
    x1 = min(a.width, int((k.x1 - g.sol) / g.olcek) + 1)
    y1 = min(a.height, int((k.y1 - g.ust) / g.olcek) + 1)
    return x1 > x0 and y1 > y0 and a.crop((x0, y0, x1, y1)).getbbox() is not None


def daire_arasi(cx: float, cy: float, r: float, k: Kutu) -> float:
    """Daire kenarı ile kutu arası en kısa uzaklık (negatif = kesişim)."""
    dx = max(k.x0 - cx, 0.0, cx - k.x1)
    dy = max(k.y0 - cy, 0.0, cy - k.y1)
    return (dx * dx + dy * dy) ** 0.5 - r


def kesisir(a: Kutu, b: Kutu) -> bool:
    return min(a.x1, b.x1) > max(a.x0, b.x0) and min(a.y1, b.y1) > max(a.y0, b.y0)


def yatay() -> Duzen:
    W, H = 1920, 1080
    s, n = 1.05, 0.42
    return Duzen(
        W=W, H=H, S=240.0, L=64.0, R=40.0, X0=96.0, LOGO_UST=54.0, LOGO_H=84.0,
        T1=459.0, ROZET_ALT=1026.0,
        karakter=Gorsel("karakter", "karakter.png", 880.0, 66.0 - 89 * s, s),
        nesne=Gorsel("nesne", "nesne.png", 640.0 - 96 * n, 822.0 - 254 * n, n),
        daire=(1375.0, 480.0, 390.0),
        serbest=Kutu("serbest", 96.0, 54.0, W - 96.0, H - 54.0),
        alt_kesik=True,
        bos=[Kutu("sure-rozeti", W * 0.85, H * 0.92, W, H)],
    )


def dikey() -> Duzen:
    W, H = 1080, 1920
    s, n, kirp = 0.64, 0.31, 1000  # karakter göğüs altında (el dahil) düz kesilir: yüz büyür, alt %20 boş kalır
    return Duzen(
        W=W, H=H, S=190.0, L=48.0, R=36.0, X0=72.0, LOGO_UST=400.0, LOGO_H=72.0,
        T1=492.0 + 0.921 * 190.0, ROZET_ALT=1500.0,
        karakter=Gorsel("karakter", "karakter.png", 610.0 - 448 * s, 930.0 - 89 * s, s, kirp),
        nesne=Gorsel("nesne", "nesne.png", 84.0 - 96 * n, 1190.0 - 254 * n, n),
        daire=(625.0, 1220.0, 295.0),
        serbest=Kutu("serbest", 54.0, H * 0.20, W - 54.0, H * 0.80),
        alt_kesik=False,
        bos=[Kutu("ust-20", 0, 0, W, H * 0.20), Kutu("alt-20", 0, H * 0.80, W, H)],
    )


def denetle(d: Duzen, yazilar: list[Kutu], gk: list[Kutu], daire_var: bool) -> None:
    """Çakışma, kenar payı ve boş bölge kuralları (standart §2, §5.4)."""
    PAY = 24.0
    gorseller = [d.karakter, d.nesne]
    sb = d.serbest
    for y in yazilar:
        assert sb.x0 - 0.5 <= y.x0 and y.x1 <= sb.x1 and sb.y0 <= y.y0 and y.y1 <= sb.y1, f"{y.ad} serbest alan dışında: {y}"
        for g in gorseller:
            assert not degiyor(g, y.genis(KENAR_PX + PAY)), f"{g.ad} ile {y.ad} çakışıyor"
        for b in d.bos:
            assert not kesisir(y, b), f"{y.ad} boş bölgede: {b.ad}"
    for i, a in enumerate(yazilar):
        for b in yazilar[i + 1:]:
            assert not kesisir(a.genis(PAY / 2), b.genis(PAY / 2)), f"{a.ad} ile {b.ad} çakışıyor"
    for g, k in zip(gorseller, gk):
        assert sb.x0 <= k.x0 - KENAR_PX and k.x1 + KENAR_PX <= sb.x1, f"{g.ad} yan kenar payı: {k}"
        assert sb.y0 <= k.y0 - KENAR_PX, f"{g.ad} üst sınır: {k}"
        assert k.y1 + KENAR_PX <= sb.y1 or (g.ad == "karakter" and d.alt_kesik), f"{g.ad} alt sınır: {k}"
        for b in d.bos:
            assert not degiyor(g, b.genis(KENAR_PX + 8)), f"{g.ad} boş bölgede: {b.ad}"
    assert not degiyor(d.karakter, gk[1].genis(KENAR_PX + 12)), "nesne karaktere değiyor"
    if daire_var:
        cx, cy, r = d.daire
        for y in yazilar:
            assert daire_arasi(cx, cy, r, y) >= PAY, f"daire {y.ad} yazısına değiyor"
        for b in d.bos:
            assert daire_arasi(cx, cy, r, b) >= 8, f"daire boş bölgede: {b.ad}"
        assert sb.x0 <= cx - r and cx + r <= sb.x1 and sb.y0 <= cy - r and cy + r <= sb.y1, "daire serbest alan dışında"


def ciz(d: Duzen, tema: str) -> tuple[str, list[Kutu]]:
    """index.html metni ve blok kutuları."""
    R = TEMA[tema]
    S, L = d.S, d.L

    # Satır 1 (İ noktası satırın üst sınırı)
    g_sol, g_gen = gorunur("Fredoka", 700, SATIR1, S)
    s1 = Kutu("satir1", d.X0, d.T1 - sinir("Fredoka", 700, "İ")[3] * S, d.X0 + g_gen, d.T1 + 0.02 * S)

    # Satır 2: vurgu kutusu
    k_sol, k_gen = gorunur("Fredoka", 700, SATIR2, S)
    ph, pv = 0.17 * S, 0.15 * S
    k_ust = d.T1 + 0.15 * S
    T2 = k_ust + pv + 0.70 * S
    kutu = Kutu("vurgu", d.X0, k_ust, d.X0 + k_gen + 2 * ph, T2 + pv)

    # Küçük satır: "he · she · it" + ok (SVG; Lexend'de → glifi yok) + "-s"
    ks_sol, _ = gorunur("Lexend", 700, KUCUK_SOL, L)
    gorunur("Lexend", 700, KUCUK_SAG, L)
    bosluk = Y.genislik("Lexend", 700, " ", L)
    ok_x0 = d.X0 - ks_sol + Y.genislik("Lexend", 700, KUCUK_SOL, L) + bosluk
    ok_x1 = ok_x0 + 0.78 * L
    sag_x = ok_x1 + bosluk
    T3 = kutu.y1 + 0.62 * L + 0.74 * L
    _, h_alt, _, h_ust, _ = sinir("Lexend", 700, "-")
    ok_y = T3 - (h_alt + h_ust) / 2 * L
    ok_k = (h_ust - h_alt) * L
    ok_u = 0.30 * L
    s_g = sinir("Lexend", 700, "s")
    kucuk = Kutu("kucuk", d.X0, T3 - 0.74 * L, sag_x + Y.genislik("Lexend", 700, KUCUK_SAG, L) - (s_g[4] - s_g[2]) * L,
                 T3 + 0.02 * L)

    # Logo (svg kutusu 1920x476,3; mürekkep yaklaşık x 68-1850, y 73-400)
    lw = d.LOGO_H * Y.LOGO_EN_BOY
    lx = d.X0 - Y.LOGO_KAYMA * lw
    ly = d.LOGO_UST - 73.2 / 476.3 * d.LOGO_H
    logo = Kutu("logo", d.X0, d.LOGO_UST, lx + lw * 0.965, ly + 400 / 476.3 * d.LOGO_H)

    # Rozet (çerçeveli hap)
    rh = 1.8 * d.R
    rw = Y.genislik("Lexend", 700, ROZET, d.R) + 1.6 * d.R
    gorunur("Lexend", 700, ROZET, d.R)
    rozet = Kutu("rozet", d.X0, d.ROZET_ALT - rh, d.X0 + rw, d.ROZET_ALT)

    yazilar = [s1, kutu, kucuk, logo, rozet]
    gk = [gorsel_kutusu(d.karakter), gorsel_kutusu(d.nesne)]
    denetle(d, yazilar, gk, R["daire"] is not None)

    cx, cy, cr = d.daire
    fr = 'font-family="Fredoka" font-weight="700" style="font-kerning:none" xml:space="preserve"'
    lx_ = 'font-family="Lexend" font-weight="700" style="font-kerning:none" xml:space="preserve"'
    daire = f'<circle id="daire" cx="{cx:.1f}" cy="{cy:.1f}" r="{cr:.1f}" fill="{R["daire"]}"/>' if R["daire"] else ""
    yazi_svg = (
        f'<text id="s1" x="{d.X0 - g_sol:.2f}" y="{d.T1:.2f}" font-size="{S:.0f}" {fr} fill="{R["yazi"]}">{SATIR1}</text>'
        f'<rect id="vurgu" x="{kutu.x0:.2f}" y="{kutu.y0:.2f}" width="{kutu.x1 - kutu.x0:.2f}" '
        f'height="{kutu.y1 - kutu.y0:.2f}" rx="{0.10 * S:.1f}" fill="{R["kutu"]}"/>'
        f'<text id="s2" x="{kutu.x0 + ph - k_sol:.2f}" y="{T2:.2f}" font-size="{S:.0f}" {fr} fill="{R["kutuYazi"]}">{SATIR2}</text>'
        f'<text id="k1" x="{d.X0 - ks_sol:.2f}" y="{T3:.2f}" font-size="{L:.0f}" {lx_} fill="{R["yazi"]}">{KUCUK_SOL}</text>'
        f'<path id="ok" d="M{ok_x0:.1f} {ok_y:.1f} H{ok_x1:.1f} M{ok_x1 - ok_u:.1f} {ok_y - ok_u:.1f} L{ok_x1:.1f} {ok_y:.1f} '
        f'L{ok_x1 - ok_u:.1f} {ok_y + ok_u:.1f}" fill="none" stroke="{R["yazi"]}" stroke-width="{ok_k:.1f}" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
        f'<text id="k2" x="{sag_x:.2f}" y="{T3:.2f}" font-size="{L:.0f}" {lx_} fill="{R["yazi"]}">{KUCUK_SAG}</text>'
        f'<rect id="rozet" x="{rozet.x0 + 2.5:.1f}" y="{rozet.y0 + 2.5:.1f}" width="{rw - 5:.1f}" height="{rh - 5:.1f}" '
        f'rx="{(rh - 5) / 2:.1f}" fill="none" stroke="{R["yazi"]}" stroke-width="5"/>'
        f'<text id="rozet-yazi" x="{rozet.x0 + rw / 2:.1f}" y="{d.ROZET_ALT - rh / 2 + 0.35 * d.R:.1f}" '
        f'text-anchor="middle" font-size="{d.R:.0f}" {lx_} fill="{R["yazi"]}">{ROZET}</text>'
    )

    def img(g: Gorsel) -> str:
        a = alfa(g.dosya)
        w, h = a.width * g.olcek, a.height * g.olcek
        if not g.kirp:
            return (f'<img id="{g.ad}" class="abs cikartma" src="assets/{g.dosya}" alt="" '
                    f'style="left:{g.sol:.1f}px;top:{g.ust:.1f}px;width:{w:.1f}px;height:{h:.1f}px">')
        return (f'<div id="{g.ad}" class="abs cikartma" style="left:{g.sol:.1f}px;top:{g.ust:.1f}px;width:{w:.1f}px;'
                f'height:{g.kirp * g.olcek:.1f}px;overflow:hidden"><img class="abs" src="assets/{g.dosya}" alt="" '
                f'style="left:0;top:0;width:{w:.1f}px;height:{h:.1f}px"></div>')

    # Dört yön drop-shadow, 3 geçiş x KENAR_PX/3 adım: kenar yine 10 px, ince çizgide (hız çizgisi) kopya arası boşluk kalmaz.
    a = KENAR_PX / 3
    golge = " ".join(f"drop-shadow({x:.2f}px {y:.2f}px 0 {KREM})"
                     for _ in range(3) for x, y in ((a, 0), (-a, 0), (0, a), (0, -a)))
    html = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
html,body{{margin:0;background:{R["zemin"]};}}
#root{{position:relative;width:{d.W}px;height:{d.H}px;overflow:hidden;background:{R["zemin"]};}}
.abs{{position:absolute;}}
svg.kat{{position:absolute;left:0;top:0;}}
.cikartma{{filter:{golge};}}
</style></head><body>
<div id="root" class="tema-{tema}" data-composition-id="main" data-start="0" data-duration="1" data-fps="30" data-width="{d.W}" data-height="{d.H}">
<svg class="kat" id="alt" width="{d.W}" height="{d.H}" viewBox="0 0 {d.W} {d.H}" xmlns="http://www.w3.org/2000/svg">{daire}</svg>
{img(d.karakter)}
{img(d.nesne)}
<img id="logo" class="abs" src="assets/logo.svg" alt="" style="left:{lx:.1f}px;top:{ly:.1f}px;width:{lw:.1f}px;height:{d.LOGO_H:.1f}px">
<svg class="kat" id="yazi" width="{d.W}" height="{d.H}" viewBox="0 0 {d.W} {d.H}" xmlns="http://www.w3.org/2000/svg">{yazi_svg}</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var tl = gsap.timeline({{ paused: true }});
  tl.set("#root", {{ opacity: 1, immediateRender: false }}, 0);
  tl.set("#root", {{ opacity: 1, immediateRender: false }}, 1);
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""
    for yasak in ("math.random", "date.now", "new date", "opacity:0"):
        assert yasak not in html.lower(), f"yasak: {yasak}"
    return html, yazilar + gk


def logo_svg(tema: str) -> str:
    """Açık tema: sarı zeminde 'yds' sarısı kaybolur -> tek renk siyah logo. Koyu tema: şeffaf (sarı + beyaz) logo."""
    if tema == "koyu":
        return (LOGO / "yds-publishing-seffaf.svg").read_text(encoding="utf-8")
    s = (LOGO / "yds-publishing-lacivert.svg").read_text(encoding="utf-8")
    assert "#fece00" in s and "#13204D" in s
    return s.replace("#fece00", SIYAH).replace("#13204D", SIYAH)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tema", choices=("acik", "koyu"), default="acik")
    ap.add_argument("--duzen", choices=("yatay", "dikey"), default="yatay")
    ap.add_argument("--cikti", type=Path, default=AD / "proje")
    a = ap.parse_args()
    global KAPAK, LOGO
    proje: Path = a.cikti.resolve()
    KAPAK = proje.parent.parent.parent / "ortak" / "kapak"
    LOGO = proje.parent.parent.parent / "ortak" / "logo"
    d = yatay() if a.duzen == "yatay" else dikey()
    html, bloklar = ciz(d, a.tema)
    (proje / "assets").mkdir(parents=True, exist_ok=True)
    Y.font_kopyala(proje / "assets" / "fonts")
    for ad in ("karakter.png", "nesne.png"):
        shutil.copyfile(KAPAK / ad, proje / "assets" / ad)
    (proje / "assets" / "logo.svg").write_text(logo_svg(a.tema), encoding="utf-8")
    (proje / "index.html").write_text(html, encoding="utf-8")
    nesneler = [{"ad": b.ad, "x": round(b.x0), "y": round(b.y0), "w": round(b.x1 - b.x0), "h": round(b.y1 - b.y0)}
                for b in bloklar]
    (proje.parent / "nesneler.json").write_text(json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"index.html yazıldı {len(html)} · {a.duzen} {d.W}x{d.H} · tema {a.tema} · S={d.S:.0f}")


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""02-04-ydt-temel ana ders kapağı (kapak standardı v1, dijital-anlatim/.claude/docs/kapak-standardi.md).

Durağan tek kare (HyperFrames, ses yok, zaman.json sahneler[] dışı). Biçim paket adından: '-dikey' ile biten paket
1080x1920, öteki 1920x1080. Aynı dosya iki pakette birebir durur. Tema CSS değişkeniyle: varsayılan koyu,
'#root.tema-acik' açık (sınıfı ortak/hf_tema.py ekler). Çıktı: proje/index.html, proje/assets/logo-{acik,koyu}.svg,
nesneler.json. Kalıp: 02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/uret.py.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageFilter

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
ORTAK = PAKET / "ortak"
DIKEY: bool = PAKET.name.endswith("-dikey")
W, H = (1080, 1920) if DIKEY else (1920, 1080)

# Kapak metni (şef kararı; değiştirme)
# 16.11 DUZ3 (KS-4 + EK-5c): «HER ZAMAN mı ŞİMDİ mi?» 5 sözcüktü ve geniş zamanı «her zaman» diye çerçeveliyordu;
# yeni yazı dersin kilit sorusu (cümle 13, 18: «Kalıcı mı, geçici mi?»), 4 sözcük.
SATIR1 = "KALICI mı"
SATIR2 = "GEÇİCİ mi?"
KUCUK = "I live · I am living"
ROZET = "YDT · TEMEL"

SARI, SIYAH, KREM = "#fece00", "#141414", "#f3efe6"
KENAR_PX = 10      # çıkartma kenarı (standart §2)
PAY = 24           # kenar dışında ek güvenlik payı (çarpışma denetimi)
ESIK = 64          # saydamlık eşiği: altı kopyada sıfırlanır (arka plan temizleyici kırıntısı), üstü görsel
KENAR_GECIS = 3    # 4 yönlü drop-shadow kaç geçişte (10 px tek adım ince uçta basamak/şerit bırakır)

KARAKTER = ORTAK / "kapak" / "karakter.png"
NESNE = ORTAK / "kapak" / "nesne.png"
YUZ_PNG = (461.0, 470.0)   # karakter.png içinde yüz ortası (göz ölçümü, 896x1200 dosya)
ELLER_PNG = 640            # karakter.png içinde avuçların başladığı satır (üstü yalnız baş)
NESNE_YAN = "sol" if DIKEY else "sag"   # tabela başın hangi yanında (dikeyde sol boşluk, yatayda sağ)


def murekkep(aile: str, agirlik: int, metin: str) -> tuple[float, float]:
    """Metnin mürekkep alt ve üst sınırı (em; taban 0, yukarı artı). Glif latin ya da latin-ext dosyasından."""
    alt, ust = 0.0, 0.0
    for c in metin:
        for bolge in ("latin", "latin-ext"):
            f = Y._font(aile, agirlik, bolge)
            g = f.getBestCmap().get(ord(c))
            if g:
                gl = f["glyf"][g]
                if gl.numberOfContours != 0:
                    upm = f["head"].unitsPerEm
                    alt, ust = min(alt, gl.yMin / upm), max(ust, gl.yMax / upm)
                break
        else:
            raise AssertionError(f"glif yok: {c!r} ({aile} {agirlik})")
    return alt, ust


def alfa_kutusu(yol: Path) -> tuple[int, int, int, int]:
    """PNG'nin saydam olmayan kutusu (x0, y0, x1, y1)."""
    a = Image.open(yol).split()[-1].point(lambda v: 255 if v > ESIK else 0)
    kutu = a.getbbox()
    assert kutu is not None, f"{yol.name} tamamen saydam"
    return kutu


def maske(yol: Path, x: float, y: float, s: float) -> np.ndarray:
    """Görselin tuvaldeki saydamlık maskesi (bool, H x W). x, y = dosyanın sol üstü, s = ölçek."""
    im = Image.open(yol)
    a = im.split()[-1].resize((round(im.width * s), round(im.height * s)), Image.BILINEAR)
    m = Image.new("L", (W, H), 0)
    m.paste(255, (round(x), round(y)), a.point(lambda v: 255 if v > ESIK else 0))
    return np.asarray(m) > 0


def bos_mu(m: np.ndarray, kutu: tuple[float, float, float, float], pay: float) -> bool:
    """Kutu (pay kadar genişletilmiş) içinde maskede görsel yok mu."""
    x0, y0 = max(0, math.floor(kutu[0] - pay)), max(0, math.floor(kutu[1] - pay))
    x1, y1 = min(W, math.ceil(kutu[2] + pay)), min(H, math.ceil(kutu[3] + pay))
    return x1 <= x0 or y1 <= y0 or not m[y0:y1, x0:x1].any()


def maske_kutusu(m: np.ndarray) -> tuple[int, int, int, int]:
    """Maskenin tuvaldeki kutusu (x0, y0, x1, y1)."""
    ys, xs = np.nonzero(m)
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def daire_kutu_uzakligi(cx: float, cy: float, k: tuple[float, float, float, float]) -> float:
    """Daire merkezinin kutuya en kısa uzaklığı."""
    dx = max(k[0] - cx, 0.0, cx - k[2])
    dy = max(k[1] - cy, 0.0, cy - k[3])
    return math.hypot(dx, dy)


def yerlesim(ks: float, oynat: float) -> dict:
    """Bütün öğelerin konumu (px). Kutular (x0, y0, x1, y1). ks: karakter ölçeği. oynat: yatayda yazı bloğunu
    ortadan yukarı alma, dikeyde karakteri ortadan sağa kaydırma (px)."""
    if DIKEY:
        M, LOGO_Y, LOGO_H, SUTUN, SK, RZ = 72.0, 408.0, 64.0, W - 72.0, 54.0, 34.0
    else:
        M, LOGO_Y, LOGO_H, SUTUN, SK, RZ = 96.0, 60.0, 76.0, round(0.55 * W), 64.0, 40.0
    PADX, PADY = 0.14, 0.08
    ORAN2, ARA = (1.2, 0.24) if DIKEY else (1.35, 0.30)   # vurgu satırı boy oranı, satır arası (S1 katı)

    # Ana yazı boyu: satır 1 sütuna sığar; vurgu satırı (kutulu) satır 1'in 1,35 katı, kutu sütuna sığar.
    w1_100 = Y.genislik("Fredoka", 700, SATIR1, 100.0)
    w2_100 = Y.genislik("Fredoka", 700, SATIR2, 100.0)
    # 16.11 DUZ3: dikeyde kısa satır 1 yazıyı 170 px'e büyütüp karakteri küçültüyordu (ölçek 0,61); tavan 140
    # (eski «HER ZAMAN mı» genişlikten 136 px idi), yatay tavan 170 aynı.
    S1 = math.floor(min(140.0 if DIKEY else 170.0, (SUTUN - M) * 100.0 / w1_100))
    S2 = min(round(ORAN2 * S1), math.floor((SUTUN - M) * 100.0 / (w2_100 + 2 * PADX * 100.0)))
    w1 = Y.genislik("Fredoka", 700, SATIR1, S1)
    w2 = Y.genislik("Fredoka", 700, SATIR2, S2)
    wk = Y.genislik("Lexend", 700, KUCUK, SK)
    a1, u1 = murekkep("Fredoka", 700, SATIR1)
    a2, u2 = murekkep("Fredoka", 700, SATIR2)
    ak, uk = murekkep("Lexend", 700, KUCUK)

    ara = round(ARA * S1)
    h1 = (u1 - a1) * S1
    kutu_h = (u2 - a2) * S2 + 2 * PADY * S2
    hk = (uk - ak) * SK
    blok_h = h1 + ara + kutu_h + ara + hk

    rz_h = round(1.9 * RZ)
    rz_w = Y.genislik("Lexend", 700, ROZET, RZ) + 1.6 * RZ
    if DIKEY:
        blok_ust = LOGO_Y + LOGO_H + 44.0
        rz_y = 0.80 * H - 24.0 - rz_h          # orta bandın sol altı (alt %20 sınırının üstü)
    else:
        rz_y = H - 60.0 - rz_h                  # sol alt
        bos = rz_y - (LOGO_Y + LOGO_H)
        blok_ust = max(LOGO_Y + LOGO_H + 40.0, LOGO_Y + LOGO_H + (bos - blok_h) / 2.0 - oynat)
    T1 = blok_ust + u1 * S1
    kutu_ust = blok_ust + h1 + ara
    T2 = kutu_ust + PADY * S2 + u2 * S2
    kutu_alt = kutu_ust + kutu_h
    TK = kutu_alt + ara + uk * SK

    y: dict = {
        "M": M, "S1": S1, "S2": S2, "SK": SK, "RZ": RZ, "T1": T1, "T2": T2, "TK": TK, "PADX": PADX,
        "logo": (M, LOGO_Y, M + LOGO_H * Y.LOGO_EN_BOY, LOGO_Y + LOGO_H),
        "satir1": (M, T1 - u1 * S1, M + w1, T1 - a1 * S1),
        "kutu2": (M, kutu_ust, M + w2 + 2 * PADX * S2, kutu_alt),
        "kucuk": (M, TK - uk * SK, M + wk, TK - ak * SK),
        "rozet": (M, rz_y, M + rz_w, rz_y + rz_h),
    }

    # Karakter: bel üstü. Dosyanın saydam olmayan kutusu kx0..kx1, ky0..ky1.
    kx0, ky0, kx1, ky1 = alfa_kutusu(KARAKTER)
    if DIKEY:
        alt = 0.80 * H - KENAR_PX - 6.0                       # alt %20'ye kenar dahil girmez
        kx = W / 2.0 + oynat - (kx0 + kx1) / 2.0 * ks          # ortalı; rozete yer için sağa kayabilir
        ky = alt - ky1 * ks
    else:
        ky = H - ky1 * ks                                       # bel kesiti alt kenarda
        bos_x, bos_y = 0.85 * W, 0.92 * H                      # sağ alt %15 x %8 (süre rozeti)
        a = np.asarray(Image.open(KARAKTER).split()[-1]) > ESIK
        satir0 = max(0, math.floor((bos_y - KENAR_PX - PAY - ky) / ks))
        sag = np.nonzero(a[satir0:, :].any(axis=0))[0].max() + 1
        kx = bos_x - KENAR_PX - PAY - sag * ks                 # sağa yaslı, boş bölgeye girmez
    y["karakter"] = (kx, ky, ks)
    km = maske(KARAKTER, kx, ky, ks)
    y["karakter_kutu"] = maske_kutusu(km)

    # Krem daire (açık tema): yüz ortasında; yazıya ve boş bölgeye değmez.
    hk_ = (ky1 - ky0) * ks
    yazi_kutulari = [y["logo"], y["satir1"], y["kutu2"], y["kucuk"], y["rozet"]]
    secenek = []
    for dx in (0.0, 0.03, 0.06, 0.09):
        cx, cy = kx + YUZ_PNG[0] * ks + dx * hk_, ky + YUZ_PNG[1] * ks
        r = min(0.36 * hk_, min(daire_kutu_uzakligi(cx, cy, k) for k in yazi_kutulari) - PAY)
        secenek.append((r, -dx, cx, cy))
        if r >= 0.32 * hk_:
            break
    r, _, cx, cy = max(secenek)
    y["daire"] = (cx, cy, r)

    # Nesne (iki ok tabelası): küçük, karakterin yanında, avucun üstünde. Yatay: başın sağı, sağ kenara yaslı.
    # Dikey: başın solu, başa iki kenar + 16 px uzaklıkta; üstü küçük satırın altında.
    nx0, ny0, nx1, ny1 = alfa_kutusu(NESNE)
    nh = (0.40 if DIKEY else 0.34) * (ky1 - ky0) * ks
    if NESNE_YAN == "sag":
        ns = nh / (ny1 - ny0)
        nx = (W - M) - nx1 * ns
        ust = max(cy - 0.62 * nh, 0.05 * H)
    else:
        a = np.asarray(Image.open(KARAKTER).split()[-1]) > ESIK
        ust = max(y["kucuk"][3] + KENAR_PX + PAY + 2.0, ky + ky0 * ks)
        nh_hedef = nh
        nh = min(nh, ky + ELLER_PNG * ks - 2 * KENAR_PX - 16.0 - ust)    # avucun üstünde kalır
        # 16.11 DUZ3: yazı bloğu uzayınca avuç sınırı nesneyi sıfıra indirebilir (istisna); aday reddedilir, arama sürer
        y["_nesne_kucuk"] = nh < 0.6 * nh_hedef
        nh = max(nh, 0.6 * nh_hedef)
        ns = nh / (ny1 - ny0)
        bas_sol = kx + np.nonzero(a[ky0:ELLER_PNG].any(axis=0))[0].min() * ks
        nx = bas_sol - 2 * KENAR_PX - 16.0 - nx1 * ns
    ny = ust - ny0 * ns
    y["nesne"] = (nx, ny, ns)
    nm = maske(NESNE, nx, ny, ns)
    y["nesne_kutu"] = maske_kutusu(nm)
    y["_maske"] = (km, nm)
    return y


def dogrula(y: dict) -> list[str]:
    """Kapı (standart §2, §5) — çizimden önce sayısal denetim. Dönen liste: bozulan kurallar."""
    hata: list[str] = []

    def kural(kosul: bool, mesaj: str) -> None:
        if not kosul:
            hata.append(mesaj)

    km, nm = y["_maske"]
    gorsel = km | nm
    yazi = {k: y[k] for k in ("logo", "satir1", "kutu2", "kucuk", "rozet")}
    for ad, k in yazi.items():
        kural(k[0] >= y["M"] - 0.5 and k[2] <= W - y["M"] + 0.5, f"{ad} yatay kenar payı dışında: {k}")
        kural(bos_mu(gorsel, k, KENAR_PX + PAY), f"{ad} görselle üst üste: {k}")
    kural(yazi["satir1"][3] < yazi["kutu2"][1] and yazi["kutu2"][3] < yazi["kucuk"][1], "yazı satırları üst üste")
    kural(not (km & nm).any(), "karakter ile nesne üst üste")
    kural(not y.get("_nesne_kucuk"), "nesne avuç üstüne sığmıyor (hedef boyun %60'ından küçük)")
    nk = y["nesne_kutu"]                    # nesne ile karakter arasında iki kenar + 4 px hava
    for satir in range(nk[1], nk[3]):
        nxs = np.nonzero(nm[satir])[0]
        if nxs.size == 0:
            continue
        lo, hi = max(0, satir - 2 * KENAR_PX), min(H, satir + 2 * KENAR_PX)
        kxs = np.nonzero(km[lo:hi].any(axis=0))[0]
        sol, sag = kxs[kxs < nxs.min()], kxs[kxs > nxs.max()]
        ic = kxs.size - sol.size - sag.size
        if ic or (sol.size and nxs.min() - sol.max() < 2 * KENAR_PX + 4) or \
                (sag.size and sag.min() - nxs.max() < 2 * KENAR_PX + 4):
            hata.append(f"nesne karaktere çok yakın (satır {satir})")
            break
    cx, cy, r = y["daire"]
    for ad, k in yazi.items():
        kural(daire_kutu_uzakligi(cx, cy, k) >= r + PAY - 0.01, f"daire {ad} yazısına değiyor")
    if DIKEY:
        for ad, k in {"ust20": (0, 0, W, 0.20 * H), "alt20": (0, 0.80 * H, W, H)}.items():
            kural(bos_mu(gorsel, k, KENAR_PX), f"{ad} bölgesinde görsel")
            for yad, yk in yazi.items():
                kural(yk[3] <= k[1] or yk[1] >= k[3], f"{yad} {ad} bölgesinde")
        kural(cy + r <= 0.80 * H and cy - r >= 0.20 * H, "daire üst/alt %20 bölgesinde")
    else:
        bos = (0.85 * W, 0.92 * H, W, H)
        kural(bos_mu(gorsel, bos, KENAR_PX), "sağ alt boş bölgede görsel")
        for yad, yk in yazi.items():
            kural(yk[2] <= bos[0] or yk[3] <= bos[1], f"{yad} sağ alt boş bölgede")
        kural(max(y["kutu2"][2], y["satir1"][2]) <= 0.55 * W + 0.5, "ana yazı sol %55 dışında")
        kural(cy < H / 2, "yüz kapağın üst yarısında değil")
    for ad, k in {"karakter": y["karakter_kutu"], "nesne": y["nesne_kutu"]}.items():
        kural(k[0] >= y["M"] / 2 and k[2] <= W - y["M"] / 2 and k[1] > 0, f"{ad} kenar payı dışında: {k}")
    kural(y["S1"] >= (110 if DIKEY else 120), f"ana yazı küçük: {y['S1']}")
    return hata


def logo_yaz(hedef: Path) -> None:
    """Koyu tema: saydam logo (sarı yds + beyaz publishing). Açık tema (sarı zemin): aynı logo tek renk siyah."""
    kaynak = (ORTAK / "logo" / "yds-publishing-seffaf.svg").read_text(encoding="utf-8")
    acik = kaynak
    for renk in ("#fece00", "#fff;", "#231f20"):
        assert renk in acik, f"logo rengi yok: {renk}"
        acik = acik.replace(renk, SIYAH + (";" if renk.endswith(";") else ""))
    hedef.mkdir(parents=True, exist_ok=True)
    (hedef / "logo-koyu.svg").write_text(kaynak, encoding="utf-8")
    (hedef / "logo-acik.svg").write_text(acik, encoding="utf-8")


def gorsel_kopyala(hedef: Path) -> None:
    """Karakter ve nesneyi proje/assets'e kopyalar. Alfa ≤ ESIK ve 3x3 açılışta düşen tek piksel kırıntılar sıfırlanır
    (arka plan temizleyici artığı; kenar gölgesi onları büyütüp kenarı pürüzlü gösterir). Kaynak dosya değişmez."""
    hedef.mkdir(parents=True, exist_ok=True)
    for yol in (KARAKTER, NESNE):
        im = Image.open(yol).convert("RGBA")
        a = im.split()[-1]
        m = a.point(lambda v: 255 if v > ESIK else 0).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
        im.putalpha(ImageChops.multiply(a, m))
        im.save(hedef / yol.name)


def gorsel_img(ad: str, yol: Path, yer: tuple[float, float, float]) -> str:
    """Çıkartma kenarlı görsel (<img>, dosyanın tamamı ölçekli)."""
    x, yy, s = yer
    im = Image.open(yol)
    return (f'<img id="{ad}" class="abs kenar" src="assets/{yol.name}" alt="" '
            f'style="left:{x:.1f}px;top:{yy:.1f}px;width:{im.width * s:.1f}px;height:{im.height * s:.1f}px">')


def html_yaz(y: dict) -> str:
    """index.html metni."""
    M, S1, S2, SK, RZ = y["M"], y["S1"], y["S2"], y["SK"], y["RZ"]
    k2, rz, lg = y["kutu2"], y["rozet"], y["logo"]
    cx, cy, r = y["daire"]
    ys = 'style="font-kerning:none" xml:space="preserve"'
    adim = KENAR_PX / KENAR_GECIS
    kenar = " ".join(f"drop-shadow({dx:.2f}px {dy:.2f}px 0 {KREM})" for _ in range(KENAR_GECIS)
                     for dx, dy in ((adim, 0), (-adim, 0), (0, adim), (0, -adim)))
    logo = "".join(
        f'<image id="logo-{t}" href="assets/logo-{t}.svg" x="{lg[0]:.1f}" y="{lg[1]:.1f}" '
        f'width="{lg[2] - lg[0]:.1f}" height="{lg[3] - lg[1]:.1f}"/>' for t in ("koyu", "acik"))
    rh = rz[3] - rz[1] - 4
    sahne = (
        f'<g id="kunye">{logo}'
        f'<g id="rozet"><rect class="cizgi" x="{rz[0] + 2:.1f}" y="{rz[1] + 2:.1f}" width="{rz[2] - rz[0] - 4:.1f}" '
        f'height="{rh:.1f}" rx="{rh / 2:.1f}" fill="none" stroke-width="4"/>'
        f'<text class="yazi" x="{(rz[0] + rz[2]) / 2:.1f}" y="{(rz[1] + rz[3]) / 2 + 0.35 * RZ:.1f}" '
        f'text-anchor="middle" font-family="Lexend" font-weight="700" font-size="{RZ:.0f}" {ys}>{ROZET}</text></g></g>'
        f'<g id="baslik">'
        f'<text id="bs-1" class="yazi" x="{M:.1f}" y="{y["T1"]:.1f}" font-family="Fredoka" font-weight="700" '
        f'font-size="{S1}" {ys}>{SATIR1}</text>'
        f'<rect id="bk-kutu" class="kutu" x="{k2[0]:.1f}" y="{k2[1]:.1f}" width="{k2[2] - k2[0]:.1f}" '
        f'height="{k2[3] - k2[1]:.1f}" rx="{0.12 * S2:.1f}"/>'
        f'<text id="bs-2" class="kutuYazi" x="{M + y["PADX"] * S2:.1f}" y="{y["T2"]:.1f}" font-family="Fredoka" '
        f'font-weight="700" font-size="{S2}" {ys}>{SATIR2}</text>'
        f'<text id="bs-k" class="yazi" x="{M:.1f}" y="{y["TK"]:.1f}" font-family="Lexend" font-weight="700" '
        f'font-size="{SK:.0f}" {ys}>{KUCUK}</text></g>'
    )
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
{Y.font_css()}
html,body{{margin:0;background:{SIYAH};}}
#root{{--zemin:{SIYAH};--yazi:{KREM};--kutu:{SARI};--kutuYazi:{SIYAH};position:relative;width:{W}px;height:{H}px;overflow:hidden;background:var(--zemin);}}
#root.tema-acik{{--zemin:{SARI};--yazi:{SIYAH};--kutu:{SIYAH};--kutuYazi:{KREM};}}
#daire,#logo-acik{{display:none;}}
#root.tema-acik #daire,#root.tema-acik #logo-acik{{display:inline;}}
#root.tema-acik #logo-koyu{{display:none;}}
.abs{{position:absolute;}}
.kenar{{filter:{kenar};}}
.yazi{{fill:var(--yazi);}} .kutu{{fill:var(--kutu);}} .kutuYazi{{fill:var(--kutuYazi);}} .cizgi{{stroke:var(--yazi);}}
#alt,#sahne{{left:0;top:0;}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="1" data-fps="30" data-width="{W}" data-height="{H}">
<svg id="alt" class="abs" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<circle id="daire" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{KREM}"/>
</svg>
{gorsel_img("nesne", NESNE, y["nesne"])}
{gorsel_img("karakter", KARAKTER, y["karakter"])}
<svg id="sahne" class="abs" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
{sahne}
</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script>
(function () {{
  var tl = gsap.timeline({{ paused: true }});
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, 0);
  tl.set("#sahne", {{ opacity: 1, immediateRender: false }}, 1);
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
}})();
</script></body></html>"""


def main() -> None:
    zaman: dict = json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))
    assert AD.name not in [s.get("klasor") for s in zaman.get("sahneler", [])], "kapak sahnesi sahneler[] içinde olmamalı"
    for satir in (SATIR1, SATIR2, KUCUK, ROZET):
        assert not any(ord(c) > 0x2FFF for c in satir), f"emoji/simge: {satir}"
    y: dict = {}
    hata: list[str] = []
    for ks in [round(1.0 - 0.01 * i, 2) for i in range(61)]:      # önce büyük karakter, sonra en az oynatma
        for oynat in range(0, 200, 8):
            y = yerlesim(ks, float(oynat))
            hata = dogrula(y)
            if not hata:
                break
        if not hata:
            break
    assert not hata, "yerleşim bulunamadı: " + "; ".join(hata)
    proje = AD / "proje"
    Y.font_kopyala(proje / "assets" / "fonts")
    logo_yaz(proje / "assets")
    gorsel_kopyala(proje / "assets")
    html = html_yaz(y)
    (proje / "index.html").write_text(html, encoding="utf-8")
    adlar = ("logo", "satir1", "kutu2", "kucuk", "rozet", "karakter_kutu", "nesne_kutu")
    nesneler = [{"ad": a, "x": round(y[a][0]), "y": round(y[a][1]), "w": round(y[a][2] - y[a][0]),
                 "h": round(y[a][3] - y[a][1])} for a in adlar]
    cx, cy, r = y["daire"]
    nesneler.append({"ad": "daire", "x": round(cx - r), "y": round(cy - r), "w": round(2 * r), "h": round(2 * r)})
    (AD / "nesneler.json").write_text(json.dumps(nesneler, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"index.html yazıldı {len(html)} · {W}x{H} · S1={y['S1']} S2={y['S2']} karakter ölçek={y['karakter'][2]:.3f}"
          f" · oynat {oynat}"
          f" · daire r={r:.0f}")


if __name__ == "__main__":
    main()

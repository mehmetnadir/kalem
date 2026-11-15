"""Sahne 01 index.html üretici (02-04 YDT temel dikey; soğuk açılış K23, 102 kare, 1080x1920).
Yerleşim BRIEF-DIKEY §2-§3 satır 1 + SPEC.md: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform boş.
Zaman: ../../zaman.json (t_bas, kare) + ortak/anlatim/sozcukler.json (cümle 1; t_bas 0)."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402
from yardim import u  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text()) if w["cumle"] == 1]
R = Y.RENK
KRE, IKN, SAR, ZEM = R["murekkep"], R["ikincil"], R["vurgu"], R["zemin"]

SOL = u(96)                         # yazı sol kenarı, sola hizalı
BOY = u(128)                        # Fredoka 700, kinetik satır
Y1, Y2, Y3 = u(560), u(740), u(960) # satır tabanları: İstanbul'da / yaşıyorum. / Amcamla
Y4 = u(1140)                        # 4. satır yuvası: BOŞ (sahne 02 çizer)
TIRE_PAY = 0.14                     # yor kutusu yatay iç boşluğu (em)
TIRE_ARA = 0.08                     # tire ile kutu kenarı arası (em)
KUTU_UST, KUTU_ALT = 0.64, 0.36     # kutu: taban üstü / altı (em)
LOGO_H = u(192)                     # logo damgası yükseklik
LOGO_W = LOGO_H * Y.LOGO_EN_BOY     # logo damgası genişlik (≈ 774)
LOGO_BX = (Y.W - LOGO_W) / 2        # damga orta x (≈ 153)
LOGO_BY = (352 + 1392) / 2 - LOGO_H / 2  # damga orta y (≈ 776)
HUD_LOGO = (u(48), u(48), u(96))    # sol üst HUD hedefi (48, 48), h 96 (kunye.js ile birebir)
UCUS = (0.50, 0.45)                 # logo HUD'a uçar (0,50-0,95)
VURUS = 0.22                        # kinetik sözcük gelişi (back.out(1.6))


def T(i):
    """Cümle 1, i. sözcüğün t0'ı (küresel = yerel sn)."""
    return SOZ[i]["t0"]


def g(m):
    return Y.genislik("Fredoka", 700, m, BOY)


def metin(m, x, y, renk):
    return ('<text x="%.2f" y="%.2f" font-family="Fredoka" font-weight="700" font-size="%.1f" fill="%s" '
            'xml:space="preserve">%s</text>' % (x, y, BOY, renk, m))


def vur(s, kim, x, w, y, t):
    """Kinetik sözcük: aşağıdan, küçükten vurarak gelir (stil §4)."""
    s.fromto("#" + kim, t, {"opacity": 0, "y": u(34), "scale": 0.86, "svgOrigin": "%.1f %.1f" % (x + w / 2, y)},
             {"opacity": 1, "y": 0, "scale": 1, "duration": VURUS, "ease": "back.out(1.6)"})
    s.olay(t, "tik", 0.55)


# ---- Geometri ve devir değerleri ----
xa = SOL
wa, wy, wu, wt, p = g("yaşı"), g("yor"), g("um."), g("-"), TIRE_PAY * BOY
xy0, xu0 = xa + wa, xa + wa + wy                    # bitişik (ayrılmadan önce)
ara = TIRE_ARA * BOY
dy, du = wt + ara + p, 2 * (wt + ara + p)            # kayma miktarları
kx0, kx1 = xy0 + dy - p, xy0 + dy + wy + p           # kutunun son yeri
ky, kh, sag = Y2 - KUTU_UST * BOY, (KUTU_UST + KUTU_ALT) * BOY, xu0 + du + wu

DEVIR = {
    "sol": SOL,
    "taban": [Y1, Y2, Y3, Y4],
    "boy": BOY,
    "yasi_x": xa,
    "kutu": {"x": round(kx0, 2), "y": round(ky, 2), "w": round(kx1 - kx0, 2), "h": round(kh, 2), "rx": round(u(14), 2)},
    "tire_x": [round(xa + wa, 2), round(kx1 + ara, 2)],
    "sag": round(sag, 2),
}

# Asserts
assert [w["sozcuk"] for w in SOZ[:4]] == ["İstanbul'da", "yaşıyorum.", "Amcamla", "yaşıyorum."], SOZ[:4]
assert sag <= Y.W - 48, f"satır 2 sağ kenara taşıyor: {sag:.0f}"
assert SOL + g("İstanbul'da") <= Y.W - 48, "satır 1 sağ kenara taşıyor"
assert SOL + g("Amcamla") <= Y.W - 48, "satır 3 sağ kenara taşıyor"
assert Y1 - 0.95 * BOY >= 352, f"satır 1 üstü içerik bandına taştı: {Y1 - 0.95 * BOY:.1f}"
assert ky - Y1 >= u(40), f"kutu üstü ile satır 1 arası yakın: {ky - Y1:.1f}"
assert (Y3 - 0.691 * BOY) - (ky + kh) >= u(40), f"kutu altı ile satır 3 arası yakın: {(Y3 - 0.691 * BOY) - (ky + kh):.1f}"
assert LOGO_BY >= 352 and LOGO_BY + LOGO_H <= 1392, "logo damga kutusu içerik bandı dışında"
assert LOGO_BX >= 48 and LOGO_BX + LOGO_W <= 1032, "logo damga kutusu x sınırları dışında"
assert Y3 + KUTU_ALT * BOY < Y4 - 0.691 * BOY, "Amcamla 4. satır yuvasına taşıyor"


def uret():
    s = Y.Sahne(Z["t_bas"])
    assert [w["sozcuk"] for w in SOZ[:4]] == ["İstanbul'da", "yaşıyorum.", "Amcamla", "yaşıyorum."], SOZ[:4]

    # ---- logo damgası 0,00-0,40 (orta) · 0,50-0,95 HUD sol üste; çip Hook açılır ----
    s.set("#logoimg", 0.0, {"svgOrigin": "%.1f %.1f" % (LOGO_BX + LOGO_W / 2, LOGO_BY + LOGO_H / 2)})
    s.fromto("#logoimg", 0.0, {"opacity": 0, "scale": 1.18, "rotation": -2},
             {"opacity": 1, "scale": 1, "rotation": 0, "duration": 0.4, "ease": "power3.out"})
    s.olay(0.05, "vurus", 0.9)

    (u0, ud), (hx, hy, hh) = UCUS, HUD_LOGO
    s.set("#logo", 0.0, {"svgOrigin": "%.1f %.1f" % (LOGO_BX, LOGO_BY)})
    s.to("#logo", u0, {"x": round(hx - LOGO_BX, 2), "y": round(hy - LOGO_BY, 2), "scale": round(hh / LOGO_H, 4),
                       "duration": ud, "ease": "power3.inOut"})
    s.olay(u0, "parilti", 0.5)

    s.to("#ku-bolum", u0 + ud - 0.25, {"opacity": 1, "duration": 0.25, "ease": "power1.out"})
    s.olay(round(u0 + ud - 1 / 30, 4), "tik", 0.4)

    # ---- altyazı görünürlüğü (cümle 1 tek dilim) ----
    dilimler = Y.altyazi_dilimleri([1])
    for i, (t0, t1, _) in enumerate(dilimler):
        s.set("#alt%d" % i, max(0.0, round(t0 - 0.05, 3)), {"opacity": 1})
        if t1 + 0.35 < Z["sure"]:
            s.set("#alt%d" % i, round(t1 + 0.35, 3), {"opacity": 0})

    # ---- satır 1, sözcük 1: İstanbul'da (1,00) ----
    s.svg.append('<g id="w1" style="opacity:0">%s</g>' % metin("İstanbul'da", SOL, Y1, KRE))
    vur(s, "w1", SOL, g("İstanbul'da"), Y1, T(0))

    # ---- satır 2, sözcük 2: yaşıyorum. (1,64) üç parça bitişik gelir; ek_ayir ile yaşı-yor-um. olur ----
    s.svg.append('<g id="w2" style="opacity:0"><rect id="ek1k" x="%.2f" y="%.2f" width="0" height="%.2f" rx="%.1f" '
                 'fill="%s"/><g id="ek1a">%s</g><g id="ek1y"><g id="ek1y1">%s</g><g id="ek1y2" style="opacity:0">%s</g>'
                 '</g><g id="ek1u">%s</g><g id="ek1t" style="opacity:0">%s%s</g></g>'
                 % (xy0 + wy / 2, ky, kh, u(14), SAR, metin("yaşı", xa, Y2, KRE), metin("yor", xy0, Y2, KRE),
                    metin("yor", xy0, Y2, ZEM), metin("um.", xu0, Y2, KRE), metin("-", xa + wa, Y2, IKN),
                    metin("-", kx1 + ara, Y2, IKN)))
    vur(s, "w2", xa, sag - xa, Y2, T(1))

    # ek_ayir: "yor" hecesinde (sözcük başı + 0,30 sn; vuruş 0,22'de biter) ek kutuyla kayar, tireler belirir.
    te = round(T(1) + 0.30, 3)
    kay = {"duration": 0.36, "ease": "power3.out"}
    s.to("#ek1y", te, dict(kay, x=round(dy, 2)))
    s.to("#ek1u", te, dict(kay, x=round(du, 2)))
    s.to("#ek1k", te, dict(kay, attr={"x": round(kx0, 2), "width": round(kx1 - kx0, 2)}))
    s.set("#ek1y1", te + 0.20, {"opacity": 0})
    s.set("#ek1y2", te + 0.20, {"opacity": 1})
    s.to("#ek1t", te + 0.28, {"opacity": 1, "duration": 0.15, "ease": "power1.out"})
    s.olay(te, "cizgi", 0.55)

    # ---- satır 3, sözcük 3: Amcamla (2,52); arkasındaki "yaşıyorum" (3,08) sahne 02'de ----
    s.svg.append('<g id="w3" style="opacity:0">%s</g>' % metin("Amcamla", SOL, Y3, KRE))
    vur(s, "w3", SOL, g("Amcamla"), Y3, T(2))

    # Doğrulamalar
    Y.kontrol(s, Z["kare"], ilk=False)
    return s, Y.kunye_svg("Hook", gizli=True)


if __name__ == "__main__":
    s, kun = uret()
    dilimler = Y.altyazi_dilimleri([1])
    altyazi = Y.altyazi_svg([{"id": "alt%d" % i, "metin": m} for i, (_, _, m) in enumerate(dilimler)])
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (round(LOGO_BX, 2), round(LOGO_BY, 2), round(LOGO_W, 2), round(LOGO_H, 2)), ek=altyazi)
    )
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))
    print("devir:", json.dumps(DEVIR, ensure_ascii=False))

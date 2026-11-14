"""Sahne 01 index.html üretici (02-04 YDT temel; soğuk açılış K23, 3 sn içerik + 12 kare geçiş payı = 102 kare).
Zaman: ../../zaman.json (t_bas, kare) + ortak/anlatim/sozcukler.json (cümle 1; küresel sn = yerel sn, t_bas 0).
BRIEF §3 No 1: iki Türkçe satır sözcük sözcük (`kinetik_baslik`); "yaşıyorum" söylenirken `ek_ayir`
(yaşı-yor-um., *yor* sarı kutuda kayar). İlk söz 1,00 sn, geri sayım yok.
Sahne sınırı: 2. satırın "yaşıyorum" sözcüğü 3,08 sn'de söylenir, sahne 3,00'te biter. Söylenmeden gelmesin
diye o kısım burada YOK; sahne 02 (cümle 1 sonu) tamamlar.
Künye: logo damgası 0,00 sn (orta), 0,50-0,95 künye köşesine uçar; bölüm + ajanda açılır. Ders adı cümle 2'de
söylenir (başlık sahne 02'de künyeye uçar): ku-ders bu sahnede gizli."""
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
SOL = u(120)                       # yazı alanı sol kenarı (AL.x)
BOY = u(128)                       # Fredoka 700, kinetik satır
Y1, Y2 = u(505), u(685)            # satır tabanları
TIRE_PAY = 0.14                    # yor kutusu yatay iç boşluğu (em)
TIRE_ARA = 0.08                    # tire ile kutu kenarı arası (em; QA tur 1: tire kutuya değiyordu)
KUTU_UST, KUTU_ALT = 0.64, 0.36    # kutu: taban üstü / altı (em); y-o-r mürekkebi -0,229..0,511 em
LOGO_H = u(150)
LOGO_W = LOGO_H * Y.LOGO_EN_BOY
LOGO_BX, LOGO_BY = (Y.W - LOGO_W) / 2, (Y.H - LOGO_H) / 2
KUNYE_LOGO = (u(56), u(1002), u(34))   # ortak/kunye.js: kenar 56, H - 44 - logoYuk, logoYuk 34
UCUS = (0.50, 0.45)                # logo künyeye uçar (bitiş 0,95 sn; ilk söz 1,00)
VURUS = 0.22                       # kinetik sözcük (stil §4: 0,18-0,22 sn, back.out(1.6))


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


def uret():
    s = Y.Sahne(Z["t_bas"])
    assert [w["sozcuk"] for w in SOZ[:4]] == ["İstanbul'da", "yaşıyorum.", "Amcamla", "yaşıyorum."], SOZ[:4]
    # ---- satır 1, sözcük 1: İstanbul'da (1,00) ----
    s.svg.append('<g id="w1" style="opacity:0">%s</g>' % metin("İstanbul'da", SOL, Y1, KRE))
    vur(s, "w1", SOL, g("İstanbul'da"), Y1, T(0))
    # ---- satır 1, sözcük 2: yaşıyorum. (1,64) üç parça bitişik gelir; ek_ayir ile yaşı-yor-um. olur ----
    xa = SOL + g("İstanbul'da ")
    wa, wy, wu, wt, p = g("yaşı"), g("yor"), g("um."), g("-"), TIRE_PAY * BOY
    xy0, xu0 = xa + wa, xa + wa + wy                    # bitişik (ayrılmadan önce)
    ara = TIRE_ARA * BOY
    dy, du = wt + ara + p, 2 * (wt + ara + p)            # kayma: yor bir tire + ara + iç boşluk, um iki katı
    kx0, kx1 = xy0 + dy - p, xy0 + dy + wy + p           # kutunun son yeri
    ky, kh, sag = Y1 - KUTU_UST * BOY, (KUTU_UST + KUTU_ALT) * BOY, xu0 + du + wu
    assert sag <= Y.W - u(120), "satır 1 sağ kenara taşıyor: %.0f" % sag
    s.svg.append('<g id="w2" style="opacity:0"><rect id="ek1k" x="%.2f" y="%.2f" width="0" height="%.2f" rx="%.1f" '
                 'fill="%s"/><g id="ek1a">%s</g><g id="ek1y"><g id="ek1y1">%s</g><g id="ek1y2" style="opacity:0">%s</g>'
                 '</g><g id="ek1u">%s</g><g id="ek1t" style="opacity:0">%s%s</g></g>'
                 % (xy0 + wy / 2, ky, kh, u(14), SAR, metin("yaşı", xa, Y1, KRE), metin("yor", xy0, Y1, KRE),
                    metin("yor", xy0, Y1, ZEM), metin("um.", xu0, Y1, KRE), metin("-", xa + wa, Y1, IKN), metin("-", kx1 + ara, Y1, IKN)))
    vur(s, "w2", xa, sag - xa, Y1, T(1))
    # ek_ayir: "yor" hecesinde (sözcük başı + 0,30 sn; vuruş 0,22'de biter) ek kutuyla kayar, tireler belirir.
    # Kutu üstünde yazı zemin rengine döner (koyu temada krem yazı sarı dolguda okunmaz). QA tur 2: soluyarak
    # geçiş yazıyı yarı saydam gösteriyordu; kutu %90 dolunca (te + 0,20) tek karede değişir, iki yazı örtüşmez.
    te = round(T(1) + 0.30, 3)
    kay = {"duration": 0.36, "ease": "power3.out"}
    s.to("#ek1y", te, dict(kay, x=round(dy, 2)))
    s.to("#ek1u", te, dict(kay, x=round(du, 2)))
    s.to("#ek1k", te, dict(kay, attr={"x": round(kx0, 2), "width": round(kx1 - kx0, 2)}))
    s.set("#ek1y1", te + 0.20, {"opacity": 0})
    s.set("#ek1y2", te + 0.20, {"opacity": 1})
    # QA tur 3: tire erken (te + 0,10) belirince kayan "um." ile üst üste biniyordu; kayma %99 bitince belirir
    s.to("#ek1t", te + 0.28, {"opacity": 1, "duration": 0.15, "ease": "power1.out"})
    s.olay(te, "cizgi", 0.55)
    # ---- satır 2, sözcük 3: Amcamla (2,52); arkasındaki "yaşıyorum" (3,08) sahne 02'de ----
    s.svg.append('<g id="w3" style="opacity:0">%s</g>' % metin("Amcamla", SOL, Y2, KRE))
    vur(s, "w3", SOL, g("Amcamla"), Y2, T(2))
    assert Y2 - 0.691 * BOY - (ky + kh) >= u(40), "yor kutusu 2. satıra yakın"
    # ---- logo damgası 0,00-0,40 (orta) · 0,50-0,95 künye köşesine; künye çerçevesi (bölüm + ajanda) açılır ----
    s.set("#logoimg", 0.0, {"svgOrigin": "%.1f %.1f" % (LOGO_BX + LOGO_W / 2, LOGO_BY + LOGO_H / 2)})
    s.fromto("#logoimg", 0.0, {"opacity": 0, "scale": 1.18, "rotation": -2},
             {"opacity": 1, "scale": 1, "rotation": 0, "duration": 0.4, "ease": "power3.out"})
    s.olay(0.05, "vurus", 0.9)
    (u0, ud), (hx, hy, hh) = UCUS, KUNYE_LOGO
    s.set("#logo", 0.0, {"svgOrigin": "%.1f %.1f" % (LOGO_BX, LOGO_BY)})
    s.to("#logo", u0, {"x": round(hx - LOGO_BX, 2), "y": round(hy - LOGO_BY, 2), "scale": round(hh / LOGO_H, 4),
                       "duration": ud, "ease": "power3.inOut"})
    s.olay(u0, "parilti", 0.5)
    s.to("#ku-bolum,#ku-ajanda,#ku-nokta", u0 + ud - 0.25, {"opacity": 1, "duration": 0.25, "ease": "power1.out"})
    s.olay(u0 + ud - 1 / 30, "tik", 0.4)
    Y.kontrol(s, Z["kare"], ilk=False)
    return s, Y.kunye_svg("Hook", 0, gizli=True)


if __name__ == "__main__":
    s, kun = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (round(LOGO_BX, 2), round(LOGO_BY, 2), LOGO_W, round(LOGO_H, 2))))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

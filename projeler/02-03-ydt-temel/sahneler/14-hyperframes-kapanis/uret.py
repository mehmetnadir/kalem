"""Sahne 14 — Kapanış (02-03 YDT temel, HyperFrames, 1920x1080; cümle 19, son sahne, geçişsiz).
SIGNAL → VERB kalemle ok; «believe → no -ing» notu; sonraki ders kartı (GR-02-04). Anlatım bitişi + 0,5 sn.
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (sapma ≤ 0,15 sn). Yerel sn = küresel - t_bas. İlk ve son 12 kare durgun."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_ham = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
S19 = [w for w in _ham if w["cumle"] == 19]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]


def T(i: int) -> float:
    return S19[i]["t0"]


def g(m: str, boy: int, agr: int = 700, aile: str = "Fredoka") -> float:
    return Y.genislik(aile, agr, m, boy)


def kunye(bolum: str, etkin: int) -> str:
    """Künye (ortak/kunye.js KUNYE ile aynı): ders + seviye (sol üst), bölüm (sağ üst), ajanda (sağ alt)."""
    ad = ["Hook", "Examples", "Rule", "Trap"]
    x, yer = Y.W - 56.0, {}
    for a in reversed(ad):
        w = g(a, 20, 500, "Lexend")
        yer[a] = {"x": x - w, "w": w}
        x -= w + 36
    tsp = "".join('<tspan fill="%s"%s>%s</tspan>' % (SAR if i == etkin else IKN, ' dx="36"' if i else "", a)
                  for i, a in enumerate(ad))
    nk = yer[ad[etkin]]
    return ('<g id="kunye">'
            '<text id="ku-ders" x="56" y="72" font-family="Fredoka" font-weight="700" font-size="30" fill="%s">'
            'PRESENT CONTINUOUS vs SIMPLE PRESENT<tspan id="ku-sev" dx="14" font-family="Lexend" font-weight="500" '
            'font-size="22" fill="%s">· YDT BASIC</tspan></text>'
            '<text id="ku-bolum" x="1864" y="72" text-anchor="end" font-family="Lexend" font-weight="700" '
            'font-size="24" fill="%s">%s</text>'
            '<g id="ku-ajA"><text x="%d" y="1030" text-anchor="end" font-family="Lexend" font-weight="500" '
            'font-size="20">%s</text><circle id="ku-nokta" cx="%.2f" cy="1023" r="4" fill="%s"/></g></g>'
            % (KRE, IKN, SAR, bolum, Y.W - 56, tsp, nk["x"] - 12, SAR))


def uret() -> tuple:
    s = Y.Sahne(TB)
    S = s.S
    # ---- 274,17 «sinyal» SIGNAL (Fredoka 150), 275,13 «altını» sarı alt çizgi ----
    FB, YB = 150, 380
    wS, wV, ara = g("SIGNAL", FB), g("VERB", FB), 230
    x0 = (1920 - (wS + ara + wV)) / 2
    s.yazi("sig", x0, YB, [("SIGNAL", KRE)], "Fredoka", 700, FB, S(T(3)), 0.35, tur="tik", guc=0.6)
    s.yol("sigm", Y.el_cizgi(x0 - 6, YB + 28, x0 + wS + 6, YB + 27, 1), S(T(5)), 0.4, SAR, 9, 0.85, "cizgi", 0.5)
    # ---- 276,17 «Sonra»: kalem oku SIGNAL → VERB ----
    s.yol("sok", Y.el_ok(x0 + wS + 40, YB - 56, x0 + wS + ara - 40, YB - 56, 2), S(T(7)), 0.35, SAR, 9, 0.95, "cizgi",
          0.6)
    # ---- 276,57 «fiile» VERB, 276,93 «bak:» sarı halka ----
    xv = x0 + wS + ara
    s.yazi("vrb", xv, YB, [("VERB", SAR)], "Fredoka", 700, FB, S(T(8)), 0.35, tur="tik", guc=0.6)
    s.yol("vrc", Y.el_daire(xv + wV / 2, YB - 54, wV / 2 + 34, 106, 0.4), S(T(9)), 0.5, SAR, 7, 0.85, "parilti", 0.55)
    # ---- 277,53 «believe» · 278,25 «fiiller» ok · 278,89 «-ing» no -ing ----
    BF, YN = 64, 560
    wb, wn = g("believe", BF), g("no -ing", BF)
    oku = 90
    xb = (1920 - (wb + 40 + oku + 40 + wn)) / 2
    s.yazi("bel", xb, YN, [("believe", KRE)], "Fredoka", 700, BF, S(T(10)), 0.35, tur="tik", guc=0.5)
    s.yol("bok", Y.el_ok(xb + wb + 40, YN - 22, xb + wb + 40 + oku, YN - 22, 2), S(T(12)), 0.3, SAR, 8, 0.95,
          "cizgi", 0.5)
    xn = xb + wb + 40 + oku + 40
    s.yazi("no", xn, YN, [("no -ing", SAR)], "Fredoka", 700, BF, S(T(13)), 0.35, tur="tik", guc=0.6)
    s.yol("nom", Y.el_cizgi(xn - 4, YN + 16, xn + wn + 4, YN + 15, 1), S(T(14)), 0.35, SAR, 9, 0.85, "cizgi", 0.5)
    # ---- 280,25 «Sonraki derste görüşürüz»: sonraki ders kartı (GR-02-04) ----
    kx, ky, kw, kh = 440, 660, 1040, 270
    tS, tD, tG = S(T(15)), S(T(16)), S(T(17))
    s.yol("kk", Y.el_kutu(kx, ky, kw, kh), tS, 0.55, IKN, 3.6, 0.95, "cizgi", 0.55)
    s.yazi("k1", kx + 56, ky + 70, [("Next lesson", IKN)], "Lexend", 500, 36, tS + 0.15, 0.3, tur=None)
    s.yazi("k2", kx + 56, ky + 166, [("GR-02-04", KRE)], "Fredoka", 700, 84, tD, 0.3, tur="tik", guc=0.5)
    baslik = "Simple Present vs Present Continuous"
    assert g(baslik, 44, 600) <= kw - 112, "kart başlığı taştı"
    s.yazi("k3", kx + 56, ky + 232, [(baslik, SAR)], "Fredoka", 600, 44, tG, 0.35, tur=None)
    s.yol("kok", Y.el_ok(kx + kw - 190, ky + 66, kx + kw - 60, ky + 66, 2), tG + 0.1, 0.25, SAR, 7, 0.95, "cizgi", 0.4)
    return s, {"kun": kunye("Next lesson", 3)}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34)))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

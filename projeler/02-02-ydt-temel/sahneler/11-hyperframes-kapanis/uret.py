"""Sahne 11 — Kapanış (HyperFrames, 1920x1080): başlık SIMPLE PRESENT + üç söz etiketi (form · 2 kullanım · tuzak),
formül kartı (özne + V · he/she/it + V-s · sinyal sözcükleri), sonraki ders kartı (GR-02-03). Son kare durgun.
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (cümle içi sıra numarası). Yerel sn = küresel - t_bas.
Anlatım bitimi 387,63; sahne 388,05'te biter (anlatım sonu + 0,4 sn)."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_HAM = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
C60, C61 = [[w for w in _HAM if w["cumle"] == n] for n in (60, 61)]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]
CX = Y.W / 2


def T(c, i):
    """Cümle listesi c içindeki i. sözcüğün t0'ı (küresel sn)."""
    return c[i]["t0"]


def kunye():
    """Künye (kunye.js ile aynı): ders + seviye (sol üst), bölüm (sağ üst), ajanda (sağ alt, etkin Trap)."""
    ad = ["Hook", "Examples", "Rule", "Trap"]
    etkin = 3
    x, yer = Y.W - 56.0, {}
    for a in reversed(ad):
        w = Y.genislik("Lexend", 500, a, 20)
        yer[a] = {"x": x - w, "w": w}
        x -= w + 36
    tsp = "".join('<tspan fill="%s"%s>%s</tspan>' % (SAR if i == etkin else IKN, ' dx="36"' if i else "", a)
                  for i, a in enumerate(ad))
    nk = yer[ad[etkin]]
    return ('<g id="kunye">'
            '<text id="ku-ders" x="56" y="72" font-family="Fredoka" font-weight="700" font-size="30" fill="%s">'
            'SIMPLE PRESENT<tspan id="ku-sev" dx="14" font-family="Lexend" font-weight="500" '
            'font-size="22" fill="%s">· YDT BASIC</tspan></text>'
            '<text id="ku-bolum" x="1864" y="72" text-anchor="end" font-family="Lexend" font-weight="700" '
            'font-size="24" fill="%s">Next lesson</text>'
            '<g id="ku-ajA"><text x="%d" y="1030" text-anchor="end" font-family="Lexend" font-weight="500" '
            'font-size="20">%s</text><circle cx="%.2f" cy="1023" r="4" fill="%s"/></g></g>'
            % (KRE, IKN, SAR, Y.W - 56, tsp, nk["x"] - 12, SAR))


def parcala(s, ad, x, y, parcalar, aile, agr, boy, sozcuk_t):
    """Satırı sözcük zamanlı parçalara böler: parcalar [(metin, renk)], sozcuk_t her parçanın küresel t0'ı.
    Parçalar yan yana (soldan) dizilir; döner: satırın toplam genişliği."""
    for n, ((m, renk), t) in enumerate(zip(parcalar, sozcuk_t)):
        s.yazi("%s%d" % (ad, n), x, y, [(m, renk)], aile, agr, boy, s.S(t), 0.2,
               tur="tik" if n == 0 else None, guc=0.5)
        x += Y.genislik(aile, agr, m, boy)
    return x


def uret():
    s = Y.Sahne(TB)
    S = s.S

    # ---------------- başlık: SIMPLE PRESENT (369,04 «Bu derste»), sarı çizgi «geniş» 369,92 ----------------
    TBF = 112
    tw = Y.genislik("Fredoka", 700, "SIMPLE PRESENT", TBF)
    tx = CX - tw / 2
    s.yazi("baslik", tx, 200, [("SIMPLE PRESENT", KRE)], "Fredoka", 700, TBF, S(T(C60, 0)), 0.55, tur="tik", guc=0.6)
    s.yol("alt", Y.el_cizgi(tx - 6, 232, tx + tw + 6, 231, 2), S(T(C60, 2)), 0.45, SAR, 9, 0.9, "cizgi", 0.55)

    # ---------------- üç söz etiketi: form 370,72 · iki kullanım 371,60 · tuzak 373,04 ----------------
    etiket = [("form", 4), ("2 kullanım", 5), ("tuzak", 9)]
    PH, PY0, GAP = 58, 268, 40
    gen = [Y.genislik("Lexend", 500, m, 34) + 56 for m, _ in etiket]
    x = CX - (sum(gen) + GAP * (len(gen) - 1)) / 2
    for k, ((m, i), w) in enumerate(zip(etiket, gen)):
        t = S(T(C60, i))
        s.yol("pk%d" % k, Y.el_kutu(x, PY0, w, PH), t, 0.3, IKN, 3.6, 1, "cizgi", 0.5)
        s.yazi("pm%d" % k, x + 28, PY0 + 40, [(m, KRE)], "Lexend", 500, 34, t + 0.1, 0.2, tur="tik", guc=0.45)
        x += w + GAP

    # ---------------- formül kartı (374,63 «Formül»): özne + V · he/she/it + V-s · sinyal sözcükleri ----------------
    FX, FY, FW, FH = 360, 380, 1200, 340
    s.yol("fk", Y.el_kutu(FX, FY, FW, FH), S(T(C61, 0)), 0.5, KRE, 4.5, 1, "cizgi", 0.65)
    LX = FX + 90
    # satır 1: özne (375,59) + V (376,31 «yalın»)
    F1 = 76
    w_oz = Y.genislik("Fredoka", 700, "özne", F1)
    s.yazi("f1a", LX, 484, [("özne", KRE)], "Fredoka", 700, F1, S(T(C61, 1)), 0.25, tur="tik", guc=0.55)
    s.yazi("f1b", LX + w_oz, 484, [(" + ", IKN), ("V", SAR)], "Fredoka", 700, F1, S(T(C61, 2)), 0.25, tur="tik",
           guc=0.5)
    # satır 2: he (377,44) /she (378,00) /it (378,56) + V (378,97 «ile») -s (379,53 «se»)
    F2 = 76
    parca2 = [("he", KRE), ("/she", KRE), ("/it", KRE), (" + ", IKN), ("V", KRE), ("-s", SAR)]
    t2 = [T(C61, 4), T(C61, 5), T(C61, 6), T(C61, 7), T(C61, 7), T(C61, 8)]
    parcala(s, "f2", LX, 590, parca2, "Fredoka", 700, F2, t2)
    # satır 3: sinyal sözcükleri every (382,50) · always (383,38) · usually (384,42)
    F3 = 54
    sinyal = [("every", T(C61, 11)), ("always", T(C61, 12)), ("usually", T(C61, 13))]
    x = LX
    sep = Y.genislik("Fredoka", 600, "  ·  ", F3)
    for k, (m, t) in enumerate(sinyal):
        if k:
            s.yazi("f3p%d" % k, x, 684, [("  ·  ", IKN)], "Fredoka", 600, F3, S(t), 0.15, tur=None)
            x += sep
        s.yazi("f3w%d" % k, x, 684, [(m, SAR)], "Fredoka", 600, F3, S(t), 0.25, tur="tik", guc=0.5)
        x += Y.genislik("Fredoka", 600, m, F3)
    assert x < FX + FW - 60, "sinyal satırı karta sığmadı"

    # ---------------- sonraki ders kartı (385,95 «Sıradaki derste görüşürüz») ----------------
    NX, NY, NW, NH = 360, 760, 1200, 210
    s.yol("nk", Y.el_kutu(NX, NY, NW, NH), S(T(C61, 14)), 0.5, IKN, 3.6, 1, "cizgi", 0.55)
    s.yazi("nl", NX + 56, NY + 56, [("Next lesson", IKN)], "Lexend", 500, 32, S(T(C61, 14)) + 0.2, 0.25,
           tur=None)
    s.yazi("nn", NX + 56, NY + 128, [("GR-02-03", KRE)], "Fredoka", 700, 64, S(T(C61, 15)), 0.25, tur="tik",
           guc=0.5)
    ad = "Present Continuous vs Simple Present"
    aw = Y.genislik("Fredoka", 600, ad, 40)
    assert NX + 56 + aw < NX + NW - 220, "ders adı karta sığmadı"
    s.yazi("na", NX + 56, NY + 184, [(ad, SAR)], "Fredoka", 600, 40, S(T(C61, 16)), 0.3, tur=None)
    s.yol("no", Y.el_ok(NX + NW - 190, NY + 100, NX + NW - 70, NY + 100, 2), S(T(C61, 16)) + 0.1, 0.25, SAR, 7, 1,
          "cizgi", 0.5)
    return s, {"kun": kunye()}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34)))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

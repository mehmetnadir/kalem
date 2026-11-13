"""Sahne 16 — Kapanış (HyperFrames, 1920x1080, 453 kare = içerik 423 + 30 durgun kuyruk).
Başlık SIMPLE PRESENT · YDT ADVANCED + üç söz etiketi (form · dört çerçeve · tuzak) + formül kartı
(S + V · he/she/it + V-s). Formül kartı son değişiklikten sonra durgun kalır.
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (cümle içi sıra numarası). Yerel sn = küresel - t_bas."""
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
C58, C59 = [[w for w in _HAM if w["cumle"] == n] for n in (58, 59)]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]
CX = Y.W / 2


def T(c, i):
    """Cümle listesi c içindeki i. sözcüğün t0'ı (küresel sn)."""
    return c[i]["t0"]


def parcala(s, ad, x, y, parcalar, aile, agr, boy, sozcuk_t):
    """Satırı sözcük zamanlı parçalara böler: parcalar [(metin, renk)], sozcuk_t her parçanın küresel t0'ı.
    Döner: [(parça x, genişlik)]."""
    yer = []
    for n, ((m, renk), t) in enumerate(zip(parcalar, sozcuk_t)):
        w = Y.genislik(aile, agr, m, boy)
        s.yazi("%s%d" % (ad, n), x, y, [(m, renk)], aile, agr, boy, s.S(t), 0.2, tur="tik" if n == 0 else None, guc=0.5)
        yer.append((x, w))
        x += w
    return yer


def uret():
    s = Y.Sahne(TB)
    S = s.S

    # ---------------- başlık: «Bu» 405,19 yazılır; sarı çizgi «geniş» 406,07 ----------------
    TBF = 112
    w1 = Y.genislik("Fredoka", 700, "SIMPLE PRESENT", TBF)
    w2 = Y.genislik("Lexend", 500, "· YDT ADVANCED", 44)
    gap = 28
    x0 = CX - (w1 + gap + w2) / 2
    s.yazi("baslik", x0, 210, [("SIMPLE PRESENT", KRE)], "Fredoka", 700, TBF, S(T(C58, 0)), 0.55, tur="tik", guc=0.6)
    s.yazi("sev", x0 + w1 + gap, 210, [("· YDT ADVANCED", IKN)], "Lexend", 500, 44, S(T(C58, 1)), 0.35, tur=None)
    s.yol("alt", Y.el_cizgi(x0 - 6, 242, x0 + w1 + 6, 241, 2), S(T(C58, 2)), 0.45, SAR, 9, 0.9, "cizgi", 0.55)

    # ---------------- üç söz etiketi: form 406,87 · dört çerçeve 407,75 · tuzak 409,11 ----------------
    etiket = [("form", 4), ("dört çerçeve", 5), ("tuzak", 8)]
    PH, PY0, GAP = 62, 290, 40
    gen = [Y.genislik("Lexend", 500, m, 34) + 56 for m, _ in etiket]
    x = CX - (sum(gen) + GAP * (len(gen) - 1)) / 2
    for k, ((m, i), w) in enumerate(zip(etiket, gen)):
        t = S(T(C58, i))
        s.yol("pk%d" % k, Y.el_kutu(x, PY0, w, PH), t, 0.3, IKN, 3.6, 1, "cizgi", 0.5)
        s.yazi("pm%d" % k, x + 28, PY0 + 42, [(m, KRE)], "Lexend", 500, 34, t + 0.1, 0.2, tur="tik", guc=0.45)
        x += w + GAP

    # ---------------- formül kartı: «Formül:» 410,70 ----------------
    FX, FY, FW, FH = 360, 420, 1200, 480
    s.yol("fk", Y.el_kutu(FX, FY, FW, FH), S(T(C59, 0)), 0.5, KRE, 4.5, 1, "cizgi", 0.65)
    F = 104
    # satır 1: S + V   (özne, 411,66 · yalın 412,46); altında küçük açıklamalar
    p1 = [("S", KRE), (" + ", IKN), ("V", SAR)]
    w1p = [Y.genislik("Fredoka", 700, m, F) for m, _ in p1]
    l1x = CX - sum(w1p) / 2
    yer1 = parcala(s, "f1", l1x, 600, p1, "Fredoka", 700, F, [T(C59, 1), T(C59, 2), T(C59, 2)])
    for ad, (px, pw), i, metin in (("c1", yer1[0], 1, "özne"), ("c2", yer1[2], 2, "yalın fiil")):
        cw = Y.genislik("Lexend", 500, metin, 32)
        s.yazi(ad, px + pw / 2 - cw / 2, 660, [(metin, IKN)], "Lexend", 500, 32, S(T(C59, i)) + 0.18, 0.25, tur=None)
    # satır 2: he/she/it + V-s   (he 413,51 · she 414,15 · it 414,79 · ile 415,20 · se 415,68)
    p2 = [("he", KRE), ("/she", KRE), ("/it", KRE), (" + ", IKN), ("V", KRE), ("-s", SAR)]
    w2p = [Y.genislik("Fredoka", 700, m, F) for m, _ in p2]
    l2x = CX - sum(w2p) / 2
    assert l2x > FX + 80 and l2x + sum(w2p) < FX + FW - 80, "formül satırı karta sığmadı"
    parcala(s, "f2", l2x, 820, p2, "Fredoka", 700, F,
            [T(C59, 4), T(C59, 5), T(C59, 6), T(C59, 7), T(C59, 7), T(C59, 8)])
    return s, {"kun": Y.kunye_svg("Wrap-up", "Wrap-up", 2, 2)}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34)))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

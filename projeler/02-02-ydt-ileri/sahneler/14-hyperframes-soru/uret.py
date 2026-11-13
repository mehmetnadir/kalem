"""Sahne 14 — Mini soru (HyperFrames, 1920x1080, 555 kare, cümle 51–53): soru kartı (tek boşluk) + 5 şık,
sayaç halkası (3 → 1; «Üç» sözcüğünden), öğrenci yanlış cevabı C (balon + sarı çerçeve).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (cümle içi sıra numarası). Yerel sn = küresel − t_bas.
Yerleşim sahne 15 ile BİREBİR aynı (kart, şık satırları, harf daireleri): 15'te yalnız doğru şık vurgulanır.
Renk yalnız Y.RENK (kunye.js TEMALAR eşleniği): yeşil token yok → doğru/yanlış işareti `vurgu`; kırmızı yok."""
import json
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_HAM = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
C51, C52, C53 = [[w for w in _HAM if w["cumle"] == n] for n in (51, 52, 53)]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]

# ---- yerleşim (px) — sahne 15 ile aynı ----
FS, LH = 56, 76                      # kök yazısı, satır aralığı
KX, KY, KW, KH = 96, 164, 1728, 278  # soru kartı
IX, IW = 140, 1480                   # kart içi yazı alanı (sağda sayaç için pay)
PY, RH, RHH = 470, 96, 84            # şık paneli başı, satır adımı, satır yüksekliği
RWD = 900                            # şık satırı çerçeve genişliği (x 96–996; sağ bölge notlara/balona kalır)
CHX, OPX = 146, 212                  # harf dairesi merkezi, şık metni x

# ---- içerik (taslak §4 satır 7.1–7.3; ekran metni değişmez) ----
# (tür, metin | boşluk no, cümle içi sözcük sırası): cümle 51 = "Mini soru. Look at the notice ..."
KOK = [("w", "Look", 2), ("w", "at", 3), ("w", "the", 4), ("w", "notice", 5), ("w", "on", 6), ("w", "the", 7),
       ("w", "library", 8), ("w", "door:", 9), ("w", "it", 10), ("b", 0, 11), ("w", "that", 12), ("w", "the", 13),
       ("w", "library", 14), ("w", "closes", 15), ("w", "at", 16), ("w", "six", 17), ("w", "on", 18),
       ("w", "Fridays.", 19)]
DOLGU = ["says"]                     # sahne 15'te boşluğa yazılır; yerleşim için genişliği ayrılır
SIK = {"A": "say", "B": "says", "C": "is saying", "D": "said", "E": "has said"}


def T(c, i):
    """Cümle listesi c içindeki i. sözcüğün t0'ı (küresel sn)."""
    return c[i]["t0"]


def yerlestir():
    """Kök simgelerini satırlara dizer. Döner: (pos listesi, satır sayısı)."""
    sp = Y.genislik("Fredoka", 700, " ", FS)
    gen = [Y.genislik("Fredoka", 700, t[1], FS) if t[0] == "w"
           else Y.genislik("Fredoka", 700, DOLGU[t[1]], FS) + 48 for t in KOK]
    satirlar, cur, cw = [], [], 0.0
    for n, w in enumerate(gen):
        if cur and cw + sp + w > IW:
            satirlar.append(cur)
            cur, cw = [], 0.0
        cw += (sp if cur else 0) + w
        cur.append(n)
    if cur:
        satirlar.append(cur)
    assert len(satirlar) <= 3, "soru 3 satırdan uzun"
    top = KY + (KH - len(satirlar) * LH) / 2
    pos = [None] * len(gen)
    for li, sat in enumerate(satirlar):
        x = IX
        for n in sat:
            pos[n] = {"x": x, "w": gen[n], "satir": li, "base": top + li * LH + 54}
            x += gen[n] + sp
        assert x - sp <= IX + IW + 1, "satır taştı: %d" % li
    return pos, len(satirlar)


def kunye():
    """Künye (kunye.js ile aynı): SIMPLE PRESENT · YDT ADVANCED, bölüm Question, ajanda Hook Rule Roots (etkin Roots)."""
    return Y.kunye_svg("Question", "Question", 2, 2)


def uret():
    s = Y.Sahne(TB)
    S = s.S
    pos, nsat = yerlestir()
    bpos = {KOK[i][1]: pos[i] for i, t in enumerate(KOK) if t[0] == "b"}
    bal_ids = []
    t_kart = S(T(C51, 0))

    # ---------------- soru kartı (340,28 «Mini») ----------------
    s.yol("kart", Y.el_kutu(KX, KY, KW, KH), t_kart, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
    s.yazi("etiket", KX, 148, [("MINI QUESTION", SAR)], "Lexend", 700, 32, t_kart + 0.15, 0.3, tur="tik", guc=0.45)
    for n, t in enumerate(KOK):
        if t[0] == "w":
            p = pos[n]
            s.yazi("w%d" % n, p["x"], p["base"], [(t[1], KRE)], "Fredoka", 700, FS, S(T(C51, t[2])), 0.14,
                   tur="tik" if n == 0 else None, guc=0.5)
    # boşluk çizgisi: «boşluk» sözcüğü söylenince (344,22)
    p = bpos[0]
    s.yol("bl0", Y.el_cizgi(p["x"] + 4, p["base"] + 12, p["x"] + p["w"] - 4, p["base"] + 12, 2),
          S(T(C51, 11)), 0.3, IKN, 5, 1, "cizgi", 0.5)

    # ---------------- şık paneli («Şıklara» 348,46: satırlar sırayla gelir; şıklar sese yok) ----------------
    harfler = "ABCDE"
    for k, h in enumerate(harfler):
        y0 = PY + k * RH
        cy = y0 + RHH / 2
        metin = SIK[h]
        lw = Y.genislik("Fredoka", 700, h, 40)
        s.svg.append(
            '<g id="row%s" style="opacity:0">'
            '<circle class="chip" cx="%d" cy="%.1f" r="32" fill="none" stroke="%s" stroke-width="4"/>'
            '<text x="%.1f" y="%.1f" font-family="Fredoka" font-weight="700" font-size="40" fill="%s">%s</text>'
            '<text x="%d" y="%.1f" font-family="Fredoka" font-weight="700" font-size="46" fill="%s" '
            'xml:space="preserve">%s</text></g>'
            % (h, CHX, cy, KRE, CHX - lw / 2, cy + 14, KRE, h, OPX, cy + 16, KRE, metin))
    tp = S(T(C52, 0))
    for k, h in enumerate(harfler):
        s.goster("#row" + h, tp + 0.09 * k, 0.35, 0, 24)
    s.olay(tp, "tik", 0.5)
    s.olay(tp + 0.2, "tik", 0.4)

    # ---------------- sayaç halkası: «Üç» 349,50 → 3 · 2 · 1 (halka 3 sn dolar; sonra 2,0 sn sessizlik) ----------------
    tsay = S(T(C52, 2))
    sx, sy, sr = 1700, 303, 46
    s.yol("say", "M%.1f %.1f A%d %d 0 1 1 %.2f %.1f" % (sx, sy - sr, sr, sr, sx - 0.01, sy - sr), tsay, 3.0,
          SAR, 8, 1, "cizgi", 0.55)
    for n, rakam in enumerate("321"):
        nw = Y.genislik("Fredoka", 700, rakam, 60)
        tn = tsay + 0.04 + n * 1.0
        s.yazi("say" + rakam, sx - nw / 2, sy + 22, [(rakam, KRE)], "Fredoka", 700, 60, tn, 0.2, tur="tik", guc=0.5)
        if n < 2:
            s.to("#say" + rakam, tn + 0.96, {"opacity": 0, "duration": 0.12})
    tson = tsay + 3.04
    s.to("#say", tson, {"opacity": 0, "duration": 0.25})
    s.to("#say1", tson, {"opacity": 0, "duration": 0.25})

    # ---------------- öğrenci başı + balon: yanlış cevap C (352,93–357,19) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.6, 1056.0, 480.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, 2.8 / BS, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = S(T(C53, 0)) - 0.18
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    BF, BX0, BY0 = 42, 1236.0, 494.0
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2, 3, 4), (5, 6, 7, 8))            # «Bence C şıkkı: is saying.» / «Tabela şu an diyor.»
    gens = [sum(Y.genislik("Fredoka", 600, C53[i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1) for sat in satir]
    x1b = BX0 + max(gens) + 70
    assert x1b <= 1830, "balon taştı: %.0f" % x1b
    BASE = (BY0 + 76, BY0 + 76 + 62)
    s.yol("bal", Y.balon_sol(BX0, BY0, x1b, BY0 + 62 + 112, 1180, BY0 + 90), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    for sat, base in zip(satir, BASE):
        x = BX0 + 35
        for i in sat:
            m = C53[i]["sozcuk"]
            w = Y.genislik("Fredoka", 600, m, BF) - (9 if m.startswith("Ta") else 0)  # QA 13.11: "Ta" kerning
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(C53[i]["t0"]), 0.12,
                   tur="tik" if i in (0, 5) else None)
            bal_ids.append("bw%d" % i)
            x += w + sp
    # C şıkkı: sarı işaret («C» 353,65) — yanlış cevap; sahne sonuna kadar kalır, 15'te söner
    kc = harfler.index("C")
    s.yol("cfr", Y.el_kutu(KX, PY + kc * RH, RWD, RHH), S(T(C53, 1)), 0.45, SAR, 5, 0.9, "tik", 0.5)
    return s, {"kun": kunye(), "pos": pos, "nsat": nsat, "bal_ids": bal_ids}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), bal_ids=parca["bal_ids"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "satır", parca["nsat"])

"""Sahne 10 — Mini soru (HyperFrames, 1920x1080): soru kartı (tek boşluk) + 5 şık, sayaç halkası (3 → 1),
öğrenci yanlış cevabı (A), doğru B yeşil, üç adım yöntemi, çeldirici notları (sik_not pilleri).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (cümle içi sıra numarası). Yerel sn = küresel - t_bas.
Yerleşim 02-03 ileri mini soru sahnesiyle aynı: kart (96,164,1728x278) + panel (y 470, adım 96) + pil (x 1010).
Kırmızı yok (kırmızı yalnız tuzak sahnesinde): yanlış işareti ikincil renkli çarpı."""
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
C54, C55, C56, C57, C58, C59 = [[w for w in _HAM if w["cumle"] == n] for n in range(54, 60)]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
YESIL, BEYAZ = SAR, KRE   # yeşil token yok → vurgu; sarı üstünde mürekkep (QA 13.11)
TB = Z["t_bas"]

# ---- yerleşim (px) ----
FS, LH = 56, 76                      # kök yazısı, satır aralığı
KX, KY, KW, KH = 96, 164, 1728, 278  # soru kartı
IX, IW = 140, 1480                   # kart içi yazı alanı (sağda sayaç için pay)
PY, RH, RHH = 470, 96, 84            # panel başı, satır adımı, satır yüksekliği
CHX, OPX = 146, 212                  # harf dairesi merkezi, şık metni x
PIX = 1010                           # çeldirici notu (pil) x
PIL_H = 56

# ---- içerik (taslak §4 satır 7.1–7.6; ekran metni değişmez) ----
# (tür, metin | boşluk no, cümle içi sözcük sırası): cümle 54 = "Mini soru. Every morning, my brother boşluk ..."
KOK = [("w", "Every", 2), ("w", "morning,", 3), ("w", "my", 4), ("w", "brother", 5), ("b", 0, 6),
       ("w", "the", 7), ("w", "dog", 8), ("w", "for", 9), ("w", "a", 10), ("w", "walk", 11),
       ("w", "before", 12), ("w", "school.", 13)]
DOLGU = ["takes"]
SIK = {"A": "take", "B": "takes", "C": "taking", "D": "is taking", "E": "to take"}


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
    top = KY + (KH - len(satirlar) * LH) / 2
    pos = [None] * len(gen)
    for li, sat in enumerate(satirlar):
        x = IX
        for n in sat:
            pos[n] = {"x": x, "w": gen[n], "satir": li, "base": top + li * LH + 54}
            x += gen[n] + sp
        assert x - sp <= IX + IW + 1, "satır taştı: %d" % li
    return pos, len(satirlar)


def pil_olc(parcalar):
    """Çeldirici notu parçalarının genişliği: metin Lexend 500 30; <> ve -> 44 px; x 28 px."""
    w = 0.0
    for n, p in enumerate(parcalar):
        w += (14 if n else 0)
        w += {"t": Y.genislik("Lexend", 500, p[1], 30) if p[0] == "t" else 0}.get(p[0], 0)
        w += {"<>": 44, "->": 44, "x": 28}.get(p[0], 0)
    return w + 44


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
            'font-size="24" fill="%s">Mini question</text>'
            '<g id="ku-ajA"><text x="%d" y="1030" text-anchor="end" font-family="Lexend" font-weight="500" '
            'font-size="20">%s</text><circle cx="%.2f" cy="1023" r="4" fill="%s"/></g></g>'
            % (KRE, IKN, SAR, Y.W - 56, tsp, nk["x"] - 12, SAR))


def uret():
    s = Y.Sahne(TB)
    S = s.S
    pos, nsat = yerlestir()
    bpos = {KOK[i][1]: pos[i] for i, t in enumerate(KOK) if t[0] == "b"}
    tok = {t[2]: i for i, t in enumerate(KOK) if t[0] == "w"}   # cümle sözcük sırası -> simge sırası
    t_kart = S(T(C54, 0))
    bal_ids = []
    panel_ids = []                                               # 342,12–358,85 arası sönen grup

    # ---------------- soru kartı (316,96 «Mini soru») ----------------
    s.yol("kart", Y.el_kutu(KX, KY, KW, KH), t_kart, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
    s.yazi("etiket", KX, 148, [("MINI QUESTION", SAR)], "Lexend", 700, 32, t_kart + 0.15, 0.3, tur="tik", guc=0.45)
    for n, t in enumerate(KOK):
        if t[0] == "w":
            p = pos[n]
            s.yazi("w%d" % n, p["x"], p["base"], [(t[1], KRE)], "Fredoka", 700, FS, S(T(C54, t[2])), 0.14,
                   tur="tik" if n == 0 else None, guc=0.5)
    # boşluk çizgisi: «boşluk» sözcüğü söylenince (319,86)
    p = bpos[0]
    s.yol("bl0", Y.el_cizgi(p["x"] + 4, p["base"] + 12, p["x"] + p["w"] - 4, p["base"] + 12, 2),
          S(T(C54, 6)), 0.3, IKN, 5, 1, "cizgi", 0.5)

    # ---------------- şık paneli («Şıklara bak» 323,46: satırlar sırayla gelir) ----------------
    harfler = "ABCDE"
    for k, h in enumerate(harfler):
        y0 = PY + k * RH
        cy = y0 + RHH / 2
        metin = SIK[h]
        lw = Y.genislik("Fredoka", 700, h, 40)
        ow = Y.genislik("Fredoka", 700, metin, 46)
        assert OPX + ow < PIX - 24, "şık metni nota değiyor: " + metin
        s.svg.append(
            '<g id="row%s" style="opacity:0">'
            '<rect id="gr%s" x="%d" y="%d" width="%d" height="%d" rx="24" fill="%s" style="opacity:0"/>'
            '<circle class="chip" cx="%d" cy="%.1f" r="32" fill="none" stroke="%s" stroke-width="4"/>'
            '<text x="%.1f" y="%.1f" font-family="Fredoka" font-weight="700" font-size="40" fill="%s">%s</text>'
            '<text x="%d" y="%.1f" font-family="Fredoka" font-weight="700" font-size="46" fill="%s" '
            'xml:space="preserve">%s</text></g>'
            % (h, h, KX, y0, KW, RHH, YESIL, CHX, cy, KRE, CHX - lw / 2, cy + 14, KRE, h, OPX, cy + 16, KRE, metin))
        panel_ids.append("row" + h)
    tp = S(T(C55, 0))
    for k, h in enumerate(harfler):
        s.goster("#row" + h, tp + 0.09 * k, 0.35, 0, 24)
    s.olay(tp, "tik", 0.5)
    s.olay(tp + 0.2, "tik", 0.4)

    # ---------------- sayaç halkası: «Üç saniye» 324,50 → 327,50 (3 · 2 · 1), halka dolar ----------------
    tsay = S(T(C55, 2))
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

    # ---------------- öğrenci başı + balon: yanlış cevap A (327,93–330,66) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.6, 1040.0, 470.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, 2.8 / BS, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = S(T(C56, 0)) - 0.18
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    BF, BX0, BY0 = 44, 1250.0, 500.0
    sp = Y.genislik("Fredoka", 600, " ", BF)
    sat = (0, 1, 2, 3)                                 # Bence A şıkkı: take.  (tek satır)
    gen = sum(Y.genislik("Fredoka", 600, C56[i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
    x1b = BX0 + gen + 70
    assert x1b <= 1830, "balon taştı: %.0f" % x1b
    BASE = BY0 + 88
    s.yol("bal", Y.balon_sol(BX0, BY0, x1b, BY0 + 140, 1172, BY0 + 78), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    x = BX0 + 35
    for i in sat:
        m = C56[i]["sozcuk"]
        w = Y.genislik("Fredoka", 600, m, BF)
        s.yazi("bw%d" % i, x, BASE, [(m, KRE)], "Fredoka", 600, BF, S(C56[i]["t0"]), 0.12,
               tur="tik" if i == 0 else None)
        bal_ids.append("bw%d" % i)
        x += w + sp
    # A şıkkı: soluk sarı çerçeve («A» 328,65)
    ka = harfler.index("A")
    y0a = PY + ka * RH
    tA = S(T(C56, 1))
    s.svg.append('<rect id="dfr" x="%d" y="%d" width="%d" height="%d" rx="24" fill="none" stroke="%s" '
                 'stroke-width="4" style="opacity:0"/>' % (KX, y0a, KW, RHH, SAR))
    s.to("#dfr", tA, {"opacity": 0.55, "duration": 0.3, "ease": "power2.out"})
    s.olay(tA, "tik", 0.5)

    # ---------------- öğretmen cevabı (331,36): balon söner, A çerçevesi söner ----------------
    th = S(T(C57, 0))
    s.to("#balg", th, {"opacity": 0, "duration": 0.4, "ease": "power2.in"})
    s.to("#dfr", th, {"opacity": 0, "duration": 0.3})
    s.olay(th, "vurus", 0.6)

    # ---------------- işaret yardımcıları ----------------
    def belirtec(idler, t, kimlik, renk=SAR, w=9):
        grup = {}
        for n in idler:
            grup.setdefault(pos[n]["satir"], []).append(n)
        for li, ns in grup.items():
            x0 = pos[ns[0]]["x"] - 4
            x1 = pos[ns[-1]]["x"] + pos[ns[-1]]["w"] + 4
            s.yol("%s_%d" % (kimlik, li), Y.el_cizgi(x0, pos[ns[0]]["base"] + 14, x1, pos[ns[0]]["base"] + 13, 1),
                  t, 0.4, renk, w, 0.85, "cizgi", 0.5)

    def cevre(idler, t, kimlik, tohum):
        """Yan yana simgelere tek sarı daire (satır ayrıysa belirteç)."""
        belirtec(idler, t, kimlik)   # QA 13.11: halka harflere değiyordu → vurgu el altçizgisi

    # ---------------- 333,93 «My brother»: özne belirteci ----------------
    belirtec([tok[4], tok[5]], S(T(C57, 4)), "ozne")

    # ---------------- A notu: «he» 335,79 imleç, «se» 337,40 pil (he için s yok) ----------------
    imlec_ve_pil("A", S(T(C57, 7)), S(T(C57, 9)), [["t", "he için s yok"], ["x"]], s, S, harfler, panel_ids, None)

    # ---------------- doğru şık B (339,08): yeşil satır + onay; «takes» 340,61 boşluğa yazılır ----------------
    tdg = S(T(C57, 13))
    kb = harfler.index("B")
    s.to("#grB", tdg, {"opacity": 1, "duration": 0.3, "ease": "power2.out"})
    s.to("#rowB text", tdg, {"fill": "var(--pilMetin)", "duration": 0.01})   # vurgu dolgusu üstünde zemin rengi (QA 13.11)
    s.to("#rowB .chip", tdg, {"stroke": "var(--pilMetin)", "duration": 0.01})
    s.yol("ck", Y.tik_yolu(KX + KW - 110, PY + kb * RH + 20, 44), tdg + 0.2, 0.3, BEYAZ, 9, 1, "cizgi", 0.55)
    s.to("#ck", tdg + 0.2, {"stroke": "var(--pilMetin)", "duration": 0.01})
    panel_ids.append("ck")
    s.olay(tdg, "vurus", 0.85)
    p = bpos[0]
    fw = Y.genislik("Fredoka", 700, DOLGU[0], FS)
    td = S(T(C57, 16))
    s.yazi("fl0", p["x"] + (p["w"] - fw) / 2, p["base"], [(DOLGU[0], KRE)], "Fredoka", 700, FS, td, 0.3,
           tur="tik", guc=0.55)
    s.yol("gb0", Y.el_cizgi(p["x"] + 2, p["base"] + 12, p["x"] + p["w"] - 2, p["base"] + 11, 1),
          tdg + 0.35, 0.35, YESIL, 8, 1, "cizgi", 0.5)

    # ---------------- 342,12–358,60 üç adım yöntemi: panel söner, adımlar + kartta işaretler ----------------
    t_y = S(T(C58, 0))
    s.to("#panel", t_y, {"opacity": 0, "duration": 0.4, "ease": "power2.inOut"})
    adim = [("1", "zaman sözcüğü", 3, 4), ("2", "özne", 11, 12), ("3", "yardımcı fiil?", 18, 19)]
    SX, SY, SADIM = 190, 640, 120
    adim_ids = []
    for k, (no, metin, i_no, i_metin) in enumerate(adim):
        cy = SY + k * SADIM
        tn = S(T(C58, i_no))
        nw = Y.genislik("Fredoka", 700, no, 44)
        s.yol("an%d" % k, Y.el_daire(SX, cy - 14, 40, 40, k * 0.8), tn, 0.4, SAR, 6, 0.9, "parilti", 0.5)
        s.yazi("ano%d" % k, SX - nw / 2, cy + 2, [(no, KRE)], "Fredoka", 700, 44, tn + 0.1, 0.2, tur="tik", guc=0.5)
        s.yazi("am%d" % k, SX + 80, cy + 6, [(metin, KRE)], "Fredoka", 700, 64, S(T(C58, i_metin)), 0.3,
               tur="tik", guc=0.55)
        adim_ids += ["an%d" % k, "ano%d" % k, "am%d" % k]
    # adım 3 cevabı: «yok» 356,50
    w3 = Y.genislik("Fredoka", 700, adim[2][1], 64)
    s.yazi("yok", SX + 80 + w3 + 40, SY + 2 * SADIM + 8, [("yok", SAR)], "Caveat", 700, 72, S(T(C58, 25)), 0.25,
           tur="tik", guc=0.5)
    adim_ids.append("yok")
    # kartta ilgili sözcükler sırayla sarı: every morning (345,81) · my brother (350,87) · boşluk (357,18)
    belirtec([tok[2], tok[3]], S(T(C58, 7)), "z1")
    cevre([tok[4], tok[5]], S(T(C58, 15)), "z2", 0.6)
    s.yol("z3", Y.el_cizgi(p["x"] + 2, p["base"] + 12, p["x"] + p["w"] - 2, p["base"] + 11, 1),
          S(T(C58, 26)), 0.35, SAR, 9, 0.9, "cizgi", 0.5)
    # adımlar söner, panel geri gelir (358,89 «Çeldiricilere»)
    t_son = S(T(C59, 0))
    for i in adim_ids:
        s.to("#" + i, t_son - 0.3, {"opacity": 0, "duration": 0.25})
    s.to("#panel", t_son - 0.05, {"opacity": 1, "duration": 0.35, "ease": "power2.out"})

    # ---------------- çeldirici notları (D · C · E): imleç + sik_not pili ----------------
    onceki = "A"
    for h, i_isaret, i_not, parcalar in (
            ("D", 5, 7, [["t", "rutin anlamına uymaz"], ["x"]]),
            ("C", 17, 18, [["t", "yardımcı fiil yok"], ["x"]]),
            ("E", 20, 21, [["t", "yardımcı fiil yok"], ["x"]])):
        imlec_ve_pil(h, S(T(C59, i_isaret)), S(T(C59, i_not)), parcalar, s, S, harfler, panel_ids, onceki)
        onceki = h
    return s, {"kun": kunye(), "pos": pos, "nsat": nsat, "bal_ids": bal_ids, "panel_ids": panel_ids}


def imlec_ve_pil(h, ti, tn, parcalar, s, S, harfler, panel_ids, onceki):
    """Şık satırına sarı imleç okunu çizer (öncekini söndürür), tn anında sik_not pilini getirir.
    İlk not (A, panel ile sönen) panel grubuna girer; sonraki notlar panel geri geldikten sonra gelir."""
    k = harfler.index(h)
    cy = PY + k * RH + RHH / 2
    s.yol("pt" + h, Y.el_ok(30, cy, 84, cy, 1), ti, 0.25, SAR, 7, 0.95, "tik", 0.45)
    if onceki:
        s.to("#pt" + onceki, ti, {"opacity": 0, "duration": 0.15})
    pw = pil_olc(parcalar)
    assert PIX + pw <= KX + KW, "pil taştı: " + h
    g = ['<rect x="%d" y="%.1f" width="%.1f" height="%d" rx="28" fill="none" stroke="%s" stroke-width="3"/>'
         % (PIX, cy - PIL_H / 2, pw, PIL_H, IKN)]
    x = PIX + 22
    xx = None
    for n, p in enumerate(parcalar):
        x += 14 if n else 0
        if p[0] == "t":
            g.append('<text x="%.1f" y="%.1f" font-family="Lexend" font-weight="500" font-size="30" '
                     'fill="%s" xml:space="preserve">%s</text>' % (x, cy + 10.5, IKN, p[1]))
            x += Y.genislik("Lexend", 500, p[1], 30)
        elif p[0] == "x":
            xx = x
            x += 28
    s.svg.append('<g id="pil%s" style="opacity:0">%s</g>' % (h, "".join(g)))
    s.goster("#pil" + h, tn, 0.3, -24, 0)
    s.olay(tn, "tik", 0.4)
    if h == "A":
        panel_ids += ["pt" + h, "pil" + h, "px1" + h, "px2" + h]
    if xx is not None:
        s.yol("px1" + h, "M%.1f %.1f L%.1f %.1f" % (xx, cy - 12, xx + 28, cy + 12), tn + 0.15, 0.12, IKN, 6, 1,
              "cizgi", 0.4)
        s.yol("px2" + h, "M%.1f %.1f L%.1f %.1f" % (xx + 28, cy - 12, xx, cy + 12), tn + 0.28, 0.12, IKN, 6, 1,
              None)


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), bal_ids=parca["bal_ids"],
               gruplar=[("panel", parca["panel_ids"])]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "satır", parca["nsat"])

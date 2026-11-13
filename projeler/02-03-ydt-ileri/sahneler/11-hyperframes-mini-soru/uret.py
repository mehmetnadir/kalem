"""Sahne 11 — Mini soru (HyperFrames, 1920x1080): soru kartı (iki boşluk) + 5 şık, sayaç «Beş şık var»,
öğrenci yanlış cevabı (D), doğru B yeşil, çeldirici notları (sik_not pilleri).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (cümle içi sıra numarası). Yerel sn = küresel - t_bas.
Yerleşim sınav-kökü sahneleriyle (05–08) aynı: kart (96,164,1728x278) + panel (y 470, adım 96) + pil (x 1010)."""
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
_ham = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
S15 = [w for w in _ham if w["cumle"] == 15]
S16 = [w for w in _ham if w["cumle"] == 16]
S17 = [w for w in _ham if w["cumle"] == 17]
R = Y.RENK
KRE, IKN, SAR, KIR = R["murekkep"], R["ikincil"], R["vurgu"], R["kirmizi"]
YESIL, BEYAZ = SAR, "#1b1a17"   # yeşil token yok: doğru = vurgu; üstündeki yazı koyu (13.11 QA)
TB = Z["t_bas"]

# ---- yerleşim (px) ----
FS, LH = 56, 76                      # kök yazısı, satır aralığı
KX, KY, KW, KH = 96, 164, 1728, 278  # soru kartı
IX, IW = 140, 1480                   # kart içi yazı alanı (sağda sayaç için pay)
PY, RH, RHH = 470, 96, 84            # panel başı, satır adımı, satır yüksekliği
CHX, OPX = 146, 212                  # harf dairesi merkezi, şık metni x
PIX = 1010                           # çeldirici notu (pil) x
PIL_H = 56

# ---- içerik (taslak §4 satır 15–17; ekran metni değişmez) ----
KOK = [("w", "I", 5), ("b", 0), ("w", "here", 6), ("w", "this", 7), ("w", "week,", 8), ("w", "and", 9),
       ("w", "I", 10), ("w", "definitely", 11), ("b", 1), ("w", "a", 12), ("w", "holiday", 13), ("w", "in", 14),
       ("w", "this", 15), ("w", "lovely", 16), ("w", "city.", 17)]
DOLGU = ["am staying", "recommend"]
SIK = {"A": ["stay", "am recommending"], "B": ["am staying", "recommend"],
       "C": ["am staying", "am recommending"], "D": ["stay", "recommend"], "E": ["stays", "recommend"]}


def T15(i):
    return S15[i]["t0"]


def T17(i):
    return S17[i]["t0"]


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
    """Künye: ders adı + seviye (sol üst), bölüm adı (sağ üst), ajanda Hook · Key · Items · Trap (etkin Items)."""
    ad = ["Hook", "Key", "Items", "Trap"]
    etkin = 2
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
            'PRESENT CONTINUOUS vs SIMPLE PRESENT<tspan id="ku-sev" dx="14" font-family="Lexend" font-weight="500" '
            'font-size="22" fill="%s">· YDT ADVANCED</tspan></text>'
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
    t_kart = S(T15(0))
    bal_ids = []

    # ---------------- soru kartı (288,14 «Mini soru») ----------------
    s.yol("kart", Y.el_kutu(KX, KY, KW, KH), t_kart, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
    s.yazi("etiket", KX, 148, [("MINI QUESTION", SAR)], "Lexend", 700, 32, t_kart + 0.15, 0.3, tur="tik", guc=0.45)
    for n, t in enumerate(KOK):
        if t[0] == "w":
            p = pos[n]
            s.yazi("w%d" % n, p["x"], p["base"], [(t[1], KRE)], "Fredoka", 700, FS, S(T15(t[2])), 0.14,
                   tur="tik" if n == 0 else None, guc=0.5)
    # boşluk çizgileri: sessiz parçada çizilir (I → 291,27 · definitely → 293,9)
    tb0, tb1 = S(S15[5]["t1"]) + 0.06, S(S15[11]["t1"]) + 0.06
    for b, tb in ((0, tb0), (1, tb1)):
        p = bpos[b]
        s.yol("bl%d" % b, Y.el_cizgi(p["x"] + 4, p["base"] + 12, p["x"] + p["w"] - 4, p["base"] + 12, 2),
              tb, 0.3, IKN, 5, 1, "cizgi", 0.5)

    # ---------------- sayaç «Beş şık var» (297,74–298,78): halka dolar, ortada 5 ----------------
    tsay = S(T15(18))
    sx, sy, sr = 1700, 303, 46
    s.yol("say", "M%.1f %.1f A%d %d 0 1 1 %.2f %.1f" % (sx, sy - sr, sr, sr, sx - 0.01, sy - sr), tsay, 0.96,
          SAR, 8, 1, "cizgi", 0.55)
    nw = Y.genislik("Fredoka", 700, "5", 60)
    s.yazi("say5", sx - nw / 2, sy + 22, [("5", KRE)], "Fredoka", 700, 60, tsay + 0.04, 0.2, tur="tik", guc=0.5)
    tsf = tsay + 1.12
    s.to("#say", tsf, {"opacity": 0, "duration": 0.25})
    s.to("#say5", tsf, {"opacity": 0, "duration": 0.25})

    # ---------------- şık paneli (Beş → rows sırayla gelir) ----------------
    harfler = "ABCDE"
    for k, h in enumerate(harfler):
        y0 = PY + k * RH
        cy = y0 + RHH / 2
        metin = " / ".join(SIK[h])
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
    for k, h in enumerate(harfler):
        s.goster("#row" + h, tsay + 0.18 * k, 0.35, 0, 24)
    s.olay(tsay, "tik", 0.5)
    s.olay(tsay + 0.4, "tik", 0.4)

    # ---------------- öğrenci başı + balon: yanlış cevap D (299,33–302,53) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.6, 1040.0, 470.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, 2.8 / BS, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = S(S16[0]["t0"]) - 0.18
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    BF, BX0, BY0 = 44, 1250.0, 500.0
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2), (3, 4, 5, 6))                  # Bence D şıkkı. / İkisi de geniş zaman.
    gens = [sum(Y.genislik("Fredoka", 600, S16[i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1) for sat in satir]
    x1b = BX0 + max(gens) + 70
    BASE = (BY0 + 72, BY0 + 136)
    s.yol("bal", Y.balon_sol(BX0, BY0, x1b, BY0 + 190, 1172, BY0 + 118), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    for sat, base in zip(satir, BASE):
        x = BX0 + 35
        for i in sat:
            m = S16[i]["sozcuk"]
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(S16[i]["t0"]), 0.12,
                   tur="tik" if i in (0, 3) else None)
            bal_ids.append("bw%d" % i)
            x += w + sp
    # D şıkkı: soluk sarı çerçeve (299,97 «D»)
    kd = harfler.index("D")
    y0d = PY + kd * RH
    tD = S(S16[1]["t0"])
    s.svg.append('<rect id="dfr" x="%d" y="%d" width="%d" height="%d" rx="24" fill="none" stroke="%s" '
                 'stroke-width="4" style="opacity:0"/>' % (KX, y0d, KW, RHH, SAR))
    s.to("#dfr", tD, {"opacity": 0.55, "duration": 0.3, "ease": "power2.out"})
    s.olay(tD, "tik", 0.5)

    # ---------------- öğretmen cevabı (303,20–): «Hayır.» balon söner, D çerçevesi kırmızı ----------------
    th = S(T17(0))
    s.to("#balg", th, {"opacity": 0, "duration": 0.4, "ease": "power2.in"})
    s.svg.append('<rect id="dfk" x="%d" y="%d" width="%d" height="%d" rx="24" fill="none" stroke="%s" '
                 'stroke-width="5" style="opacity:0"/>' % (KX, y0d, KW, RHH, KIR))
    s.to("#dfr", th, {"opacity": 0, "duration": 0.25})
    s.to("#dfk", th, {"opacity": 0.9, "duration": 0.3, "ease": "power2.out"})
    s.olay(th, "vurus", 0.7)
    # D satırında: ikinci boşluk doğru (sarı tik), ilk boşluk yanlış (kırmızı çarpı)
    w1 = Y.genislik("Fredoka", 700, "stay", 46)
    wsep = Y.genislik("Fredoka", 700, " / ", 46)
    wrec = Y.genislik("Fredoka", 700, "recommend", 46)
    cyd = y0d + RHH / 2
    s.yol("dtk", Y.tik_yolu(OPX + w1 + wsep + wrec + 22, cyd - 26, 44), S(T17(3)), 0.3, SAR, 8, 0.95, "cizgi", 0.55)
    tx_ = S(T17(5))
    cxd = OPX + w1 / 2
    s.yol("dx1", "M%.1f %.1f L%.1f %.1f" % (cxd - w1 / 2 - 6, cyd - 26, cxd + w1 / 2 + 6, cyd + 20), tx_, 0.15, KIR, 7,
          1, "cizgi", 0.5)
    s.yol("dx2", "M%.1f %.1f L%.1f %.1f" % (cxd + w1 / 2 + 6, cyd - 26, cxd - w1 / 2 - 6, cyd + 20), tx_ + 0.17, 0.15,
          KIR, 7, 1, "cizgi", 0.5)
    s.olay(tx_ + 0.17, "vurus", 0.6)

    # ---------------- işaretler: this week belirteci, boşluk dolgusu (am staying · recommend) ----------------
    def satir_belirtec(idler, t, kimlik, renk=SAR, w=9):
        grup = {}
        for n in idler:
            grup.setdefault(pos[n]["satir"], []).append(n)
        for li, ns in grup.items():
            x0 = pos[ns[0]]["x"] - 4
            x1 = pos[ns[-1]]["x"] + pos[ns[-1]]["w"] + 4
            s.yol("%s_%d" % (kimlik, li), Y.el_cizgi(x0, pos[ns[0]]["base"] + 14, x1, pos[ns[0]]["base"] + 13, 1),
                  t, 0.4, renk, w, 0.85, "cizgi", 0.5)

    satir_belirtec([3, 4], S(T17(7)), "mw")                               # 307,36 «This week»
    for b in range(2):
        p = bpos[b]
        fw = Y.genislik("Fredoka", 700, DOLGU[b], FS)
        td = S(T17(13)) if b == 0 else S(T17(15))                        # am (309,88) · Recommend (311,20)
        s.yazi("fl%d" % b, p["x"] + (p["w"] - fw) / 2, p["base"], [(DOLGU[b], KRE)], "Fredoka", 700, FS, td, 0.3,
               tur="tik", guc=0.55)
        if b == 0:
            s.yol("fm0", Y.el_cizgi(p["x"] + 6, p["base"] + 16, p["x"] + p["w"] - 6, p["base"] + 15, 1), td + 0.25,
                  0.35, SAR, 9, 0.85, "cizgi", 0.5)
        else:
            s.yol("fm1", Y.el_cizgi(p["x"] + 6, p["base"] + 16, p["x"] + p["w"] - 6, p["base"] + 15, 1.3), td + 0.25,
                  0.35, SAR, 9, 0.85, "cizgi", 0.5)

    # ---------------- doğru şık B (315,44 «B»): yeşil satır + onay + boşlukta yeşil çizgi ----------------
    tdg = S(T17(22))
    kb = harfler.index("B")
    s.to("#grB", tdg, {"opacity": 1, "duration": 0.3, "ease": "power2.out"})
    s.to("#rowB text", tdg, {"fill": BEYAZ, "duration": 0.3})
    s.to("#rowB .chip", tdg, {"stroke": BEYAZ, "duration": 0.3})
    s.yol("ck", Y.tik_yolu(KX + KW - 110, PY + kb * RH + 20, 44), tdg + 0.2, 0.3, KRE, 9, 1, "cizgi", 0.55)
    s.olay(tdg, "vurus", 0.85)
    for b in range(2):
        p = bpos[b]
        s.yol("gb%d" % b, Y.el_cizgi(p["x"] + 2, p["base"] + 12, p["x"] + p["w"] - 2, p["base"] + 11, 1),
              tdg + 0.35 + 0.25 * b, 0.35, YESIL, 8, 1, "cizgi", 0.5)

    # ---------------- çeldirici notları: imleç + sik_not pili (A · C · D · E) ----------------
    NOT = [("A", 25, 27, 0.0, [["t", "this week"], ["<>"], ["t", "stay"], ["x"]]),
           ("C", 33, 37, 0.0, [["t", "recommend"], ["->"], ["t", "no -ing"], ["x"]]),
           ("D", 41, 43, 0.0, [["t", "1. boşluk"], ["x"]]),
           ("E", 48, 50, 0.0, [["t", "I"], ["<>"], ["t", "stays"], ["x"]])]
    onceki = None
    for h, i_isaret, i_not, gecikme, parcalar in NOT:
        k = harfler.index(h)
        cy = PY + k * RH + RHH / 2
        ti = S(T17(i_isaret))
        s.yol("pt" + h, Y.el_ok(30, cy, 84, cy, 1), ti, 0.25, SAR, 7, 0.95, "tik", 0.45)
        if onceki:
            s.to("#pt" + onceki, ti, {"opacity": 0, "duration": 0.15})
        onceki = h
        tn = S(T17(i_not)) + gecikme
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
            elif p[0] in ("<>", "->"):
                g.append('<path d="M%.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f%s" fill="none" '
                         'stroke="%s" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
                         % (x + 2, cy, x + 42, cy, x + 32, cy - 9, x + 42, cy, x + 32, cy + 9,
                            (" M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (x + 12, cy - 9, x + 2, cy, x + 12, cy + 9))
                            if p[0] == "<>" else "", IKN))
                x += 44
            elif p[0] == "x":
                xx = x
                x += 28
        s.svg.append('<g id="pil%s" style="opacity:0">%s</g>' % (h, "".join(g)))
        s.goster("#pil" + h, tn, 0.3, -24, 0)
        s.olay(tn, "tik", 0.4)
        if xx is not None:
            s.yol("px1" + h, "M%.1f %.1f L%.1f %.1f" % (xx, cy - 12, xx + 28, cy + 12), tn + 0.25, 0.15, KIR, 6, 1,
                  "cizgi", 0.4)
            s.yol("px2" + h, "M%.1f %.1f L%.1f %.1f" % (xx + 28, cy - 12, xx, cy + 12), tn + 0.4, 0.15, KIR, 6, 1,
                  None)
    # son imleç söner (E satırı notundan sonra)
    s.to("#pt" + onceki, S(T17(52)), {"opacity": 0, "duration": 0.2})

    # ---------------- 332,97 «Check the signal first, then check the verb.» ----------------
    # önce sinyal (this week: sarı çift altçizgi), sonra fiil (am staying: çift altçizgi) — halka yok (13.11 QA: sıkışık satır)
    def cift_alti(idler, t0, kimlik, tohum):
        grup = {}
        for n in idler:
            grup.setdefault(pos[n]["satir"], []).append(n)
        for li, ns in grup.items():
            x0 = pos[ns[0]]["x"] - 4
            x1 = pos[ns[-1]]["x"] + pos[ns[-1]]["w"] + 4
            yb = pos[ns[0]]["base"] + 25
            s.yol("%s_%d" % (kimlik, li), Y.el_cizgi(x0 + 8, yb, x1 - 8, yb - 1, tohum), t0, 0.4, SAR, 6, 0.9, "cizgi", 0.5)

    cift_alti([3, 4], S(T17(56)), "sg", 0.6)
    p0 = bpos[0]
    s.yol("vb", Y.el_cizgi(p0["x"] + 14, p0["base"] + 28, p0["x"] + p0["w"] - 14, p0["base"] + 27, 2.1), S(T17(59)), 0.4,
          SAR, 6, 0.9, "cizgi", 0.5)
    return s, {"kun": kunye(), "pos": pos, "nsat": nsat, "bal_ids": bal_ids}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), bal_ids=parca["bal_ids"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "satır", parca["nsat"])

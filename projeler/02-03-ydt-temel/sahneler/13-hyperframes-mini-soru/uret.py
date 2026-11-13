"""Sahne 13 — Mini soru (02-03 YDT temel, HyperFrames, 1920x1080): soru kartı (tek boşluk) + 5 şık,
sayaç «Beş şık var», öğrenci yanlış cevabı (A), doğru B yeşil, çeldirici notları (sik_not pilleri).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (cümle içi sıra numarası). Yerel sn = küresel - t_bas.
Yerleşim ileri mini soru (11) ile aynı: kart (96,164,1728x278) + panel (y 470, adım 96) + pil (x 1010).
Renkler yalnız kalem paleti (ince tema çevirisi hf_tema.py): sarı vurgu, doğru şık yeşil #167A4A, kırmızı YOK."""
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
S16 = [w for w in _ham if w["cumle"] == 16]   # öğretmen: soru
S17 = [w for w in _ham if w["cumle"] == 17]   # öğrenci: yanlış cevap
S18 = [w for w in _ham if w["cumle"] == 18]   # öğretmen: cevap
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
YESIL, BEYAZ = SAR, KRE   # yeşil token yok: doğru cevap = vurgu (13.11 QA)
TB = Z["t_bas"]

# ---- yerleşim (px) ----
FS, LH, TAB = 72, 96, 69             # kök yazısı, satır aralığı, taban çizgisi payı
KX, KY, KW, KH = 96, 164, 1728, 278  # soru kartı
IX, IW = 140, 1480                   # kart içi yazı alanı (sağda sayaç için pay)
PY, RH, RHH = 470, 96, 84            # panel başı, satır adımı, satır yüksekliği
CHX, OPX = 146, 212                  # harf dairesi merkezi, şık metni x
PIX = 1010                           # çeldirici notu (pil) x
PIL_H = 56
ALT = 14                             # boşluk çizgisi: taban çizgisinin altı

# ---- içerik (taslak §4 satır 16–18; ekran metni değişmez) ----
KOK = [("w", "I", 5), ("b", 0), ("w", "this", 6), ("w", "postcard", 7), ("w", "now.", 8)]
DOLGU = ["am writing"]
SIK = {"A": ["write"], "B": ["am writing"], "C": ["writes"], "D": ["wrote"], "E": ["is writing"]}


def T16(i: int) -> float:
    return S16[i]["t0"]


def T17(i: int) -> float:
    return S17[i]["t0"]


def T18(i: int) -> float:
    return S18[i]["t0"]


def yerlestir() -> tuple[list, int]:
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
            pos[n] = {"x": x, "w": gen[n], "satir": li, "base": top + li * LH + TAB}
            x += gen[n] + sp
        assert x - sp <= IX + IW + 1, "satır taştı: %d" % li
    return pos, len(satirlar)


def pil_olc(parcalar: list) -> float:
    """Çeldirici notu parçalarının genişliği: metin Lexend 500 30; <> ve -> 44 px; x 28 px."""
    w = 0.0
    for n, p in enumerate(parcalar):
        w += (14 if n else 0)
        w += {"t": Y.genislik("Lexend", 500, p[1], 30) if p[0] == "t" else 0}.get(p[0], 0)
        w += {"<>": 44, "->": 44, "x": 28}.get(p[0], 0)
    return w + 44


def kunye(bolum: str, etkin: int) -> str:
    """Künye (ortak/kunye.js KUNYE ile aynı): ders + seviye (sol üst), bölüm (sağ üst), ajanda (sağ alt)."""
    ad = ["Hook", "Examples", "Rule", "Trap"]
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
            'font-size="22" fill="%s">· YDT BASIC</tspan></text>'
            '<text id="ku-bolum" x="1864" y="72" text-anchor="end" font-family="Lexend" font-weight="700" '
            'font-size="24" fill="%s">%s</text>'
            '<g id="ku-ajA"><text x="%d" y="1030" text-anchor="end" font-family="Lexend" font-weight="500" '
            'font-size="20">%s</text><circle id="ku-nokta" cx="%.2f" cy="1023" r="4" fill="%s"/></g></g>'
            % (KRE, IKN, SAR, bolum, Y.W - 56, tsp, nk["x"] - 12, SAR))


def uret() -> tuple:
    s = Y.Sahne(TB)
    S = s.S
    pos, nsat = yerlestir()
    bpos = {KOK[i][1]: pos[i] for i, t in enumerate(KOK) if t[0] == "b"}
    t_kart = S(T16(0))
    bal_ids = []

    # ---------------- soru kartı (242,83 «Mini soru») ----------------
    s.yol("kart", Y.el_kutu(KX, KY, KW, KH), t_kart, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
    s.yazi("etiket", KX, 148, [("MINI QUESTION", SAR)], "Lexend", 700, 32, t_kart + 0.15, 0.3, tur="tik", guc=0.45)
    for n, t in enumerate(KOK):
        if t[0] == "w":
            p = pos[n]
            s.yazi("w%d" % n, p["x"], p["base"], [(t[1], KRE)], "Fredoka", 700, FS, S(T16(t[2])), 0.14,
                   tur="tik" if n == 0 else None, guc=0.5)
    # boşluk çizgisi: sessiz parçada çizilir (I biter → this başlar; ~0,75 sn)
    p = bpos[0]
    s.yol("bl0", Y.el_cizgi(p["x"] + 4, p["base"] + ALT, p["x"] + p["w"] - 4, p["base"] + ALT, 2),
          S(S16[5]["t1"]) + 0.06, 0.3, IKN, 5, 1, "cizgi", 0.5)

    # ---------------- sayaç «Beş şık var» (250,32–251,28): halka dolar, ortada 5 ----------------
    tsay = S(T16(11))
    sx, sy, sr = 1700, 303, 46
    s.yol("say", "M%.1f %.1f A%d %d 0 1 1 %.2f %.1f" % (sx, sy - sr, sr, sr, sx - 0.01, sy - sr), tsay, 0.96,
          SAR, 8, 1, "cizgi", 0.55)
    nw = Y.genislik("Fredoka", 700, "5", 60)
    s.yazi("say5", sx - nw / 2, sy + 22, [("5", KRE)], "Fredoka", 700, 60, tsay + 0.04, 0.2, tur="tik", guc=0.5)
    tsf = tsay + 1.12
    s.to("#say", tsf, {"opacity": 0, "duration": 0.25})
    s.to("#say5", tsf, {"opacity": 0, "duration": 0.25})

    # ---------------- şık paneli (Beş → satırlar sırayla gelir) ----------------
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
            '<rect id="gr%s" x="%d" y="%d" width="%d" height="%d" rx="24" fill="%s" fill-opacity="0.22" stroke="%s" stroke-width="4" style="opacity:0"/>'
            '<circle class="chip" cx="%d" cy="%.1f" r="32" fill="none" stroke="%s" stroke-width="4"/>'
            '<text x="%.1f" y="%.1f" font-family="Fredoka" font-weight="700" font-size="40" fill="%s">%s</text>'
            '<text x="%d" y="%.1f" font-family="Fredoka" font-weight="700" font-size="46" fill="%s" '
            'xml:space="preserve">%s</text></g>'
            % (h, h, KX, y0, KW, RHH, SAR, SAR, CHX, cy, KRE, CHX - lw / 2, cy + 14, KRE, h, OPX, cy + 16, KRE, metin))
    for k, h in enumerate(harfler):
        s.goster("#row" + h, tsay + 0.18 * k, 0.35, 0, 24)
    s.olay(tsay, "tik", 0.5)
    s.olay(tsay + 0.4, "tik", 0.4)

    # ---------------- öğrenci başı + balon: yanlış cevap A (251,75–255,75) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.6, 1040.0, 470.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, 2.8 / BS, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = S(S17[0]["t0"]) - 0.18
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    BF, BX0, BY0 = 44, 1250.0, 500.0
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2), (3, 4), (5, 6))      # Bence A şıkkı. / Kartpostal yazmak / bir alışkanlık.
    gens = [sum(Y.genislik("Fredoka", 600, S17[i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1) for sat in satir]
    x1b = BX0 + max(gens) + 70
    assert x1b < 1880, "balon taştı: %.0f" % x1b
    BASE = (BY0 + 72, BY0 + 136, BY0 + 200)
    s.yol("bal", Y.balon_sol(BX0, BY0, x1b, BY0 + 254, BX0 - 78, BY0 + 118), t0 + 0.1, 0.55, KRE, 4.2, 1, "cizgi",
          0.7)
    bal_ids.append("bal")
    for sat, base in zip(satir, BASE):
        x = BX0 + 35
        for i in sat:
            m = S17[i]["sozcuk"]
            w = Y.genislik("Fredoka", 600, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(S17[i]["t0"]), 0.12,
                   tur="tik" if i in (0, 3) else None)
            bal_ids.append("bw%d" % i)
            x += w + sp
    # A şıkkı: soluk sarı çerçeve (252,31 «A»), «Hayır.» ile söner
    ka = harfler.index("A")
    y0a = PY + ka * RH
    tA = S(S17[1]["t0"])
    s.svg.append('<rect id="afr" x="%d" y="%d" width="%d" height="%d" rx="24" fill="none" stroke="%s" '
                 'stroke-width="4" style="opacity:0"/>' % (KX, y0a, KW, RHH, SAR))
    s.to("#afr", tA, {"opacity": 0.55, "duration": 0.3, "ease": "power2.out"})
    s.olay(tA, "tik", 0.5)

    # ---------------- öğretmen cevabı (256,42 «Hayır.»): balon söner, A çerçevesi söner ----------------
    th = S(T18(0))
    s.to("#balg", th, {"opacity": 0, "duration": 0.4, "ease": "power2.in"})
    s.to("#afr", th, {"opacity": 0, "duration": 0.25})
    s.olay(th, "vurus", 0.6)
    # «Now» (256,98): now. sarı belirteç (sinyal sözcüğü)
    pn = pos[4]
    s.yol("mnow", Y.el_cizgi(pn["x"] - 4, pn["base"] + ALT + 2, pn["x"] + pn["w"] + 4, pn["base"] + ALT + 1, 1),
          S(T18(1)), 0.4, SAR, 9, 0.85, "cizgi", 0.5)

    # ---------------- doğru şık B (261,46 «B»): yeşil satır + onay + boşlukta yeşil çizgi ----------------
    tdg = S(T18(9))
    kb = harfler.index("B")
    s.to("#grB", tdg, {"opacity": 1, "duration": 0.3, "ease": "power2.out"})
    #     s.to("#rowB text", tdg, {"fill": BEYAZ, "duration": 0.3})
    #     s.to("#rowB .chip", tdg, {"stroke": BEYAZ, "duration": 0.3})
    s.yol("ck", Y.tik_yolu(KX + KW - 110, PY + kb * RH + 20, 44), tdg + 0.2, 0.3, SAR, 9, 1, "cizgi", 0.55)
    s.olay(tdg, "vurus", 0.85)
    p = bpos[0]
    s.yol("gb0", Y.el_cizgi(p["x"] + 2, p["base"] + ALT, p["x"] + p["w"] - 2, p["base"] + ALT - 1, 1), tdg + 0.35,
          0.35, YESIL, 8, 1, "cizgi", 0.5)
    # «am writing» (262,98 / 263,22): boşluğa dolgu + sarı daire
    fw = Y.genislik("Fredoka", 700, DOLGU[0], FS)
    tf = S(T18(12))
    s.yazi("fl0", p["x"] + (p["w"] - fw) / 2, p["base"], [(DOLGU[0], KRE)], "Fredoka", 700, FS, tf, 0.3, tur="tik",
           guc=0.55)
    # fm0 vurgu altçizgisi kaldırıldı (13.11 QA): boşluk çizgisi (gb0) zaten vurgu renginde

    # ---------------- çeldirici notları: imleç + sik_not pili ----------------
    # (harf, imleç sözcüğü, pil sözcüğü, imleç kalır mı, parçalar)
    NOT = [("A", 1, 5, False, [["t", "now"], ["<>"], ["t", "write"], ["x"]]),          # Now … alışkanlığı
           ("D", 15, 17, False, [["t", "now"], ["<>"], ["t", "wrote"], ["x"]]),         # D şıkkı: now
           ("C", 22, 27, True, [["t", "I"], ["<>"], ["t", "writes"], ["x"]]),           # C şıkkı … özne
           ("E", 25, 28, True, [["t", "I"], ["<>"], ["t", "is"], ["x"]])]               # E şıkkı … I
    onceki = None
    kal = []
    for h, i_isaret, i_not, tut, parcalar in NOT:
        k = harfler.index(h)
        cy = PY + k * RH + RHH / 2
        ti = S(T18(i_isaret))
        s.yol("pt" + h, Y.el_ok(30, cy, 84, cy, 1), ti, 0.25, SAR, 7, 0.95, "tik", 0.45)
        if onceki:
            s.to("#pt" + onceki, ti, {"opacity": 0, "duration": 0.15})
        onceki = None if tut else h
        if tut:
            kal.append(h)
        tn = S(T18(i_not))
        pw = pil_olc(parcalar)
        assert PIX + pw <= KX + KW, "pil taştı: " + h
        g = ['<rect x="%d" y="%.1f" width="%.1f" height="%d" rx="28" fill="none" stroke="%s" stroke-width="3"/>'
             % (PIX, cy - PIL_H / 2, pw, PIL_H, IKN)]
        x = PIX + 22
        xx = None
        for n, q in enumerate(parcalar):
            x += 14 if n else 0
            if q[0] == "t":
                g.append('<text x="%.1f" y="%.1f" font-family="Lexend" font-weight="500" font-size="30" '
                         'fill="%s" xml:space="preserve">%s</text>' % (x, cy + 10.5, IKN, q[1]))
                x += Y.genislik("Lexend", 500, q[1], 30)
            elif q[0] in ("<>", "->"):
                g.append('<path d="M%.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f%s" fill="none" '
                         'stroke="%s" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
                         % (x + 2, cy, x + 42, cy, x + 32, cy - 9, x + 42, cy, x + 32, cy + 9,
                            (" M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (x + 12, cy - 9, x + 2, cy, x + 12, cy + 9))
                            if q[0] == "<>" else "", IKN))
                x += 44
            elif q[0] == "x":
                xx = x
                x += 28
        s.svg.append('<g id="pil%s" style="opacity:0">%s</g>' % (h, "".join(g)))
        s.goster("#pil" + h, tn, 0.3, -24, 0)
        s.olay(tn, "tik", 0.4)
        if xx is not None:   # çarpı sarı (kırmızı yok)
            s.yol("px1" + h, "M%.1f %.1f L%.1f %.1f" % (xx, cy - 12, xx + 28, cy + 12), tn + 0.25, 0.15, SAR, 6, 1,
                  "cizgi", 0.4)
            s.yol("px2" + h, "M%.1f %.1f L%.1f %.1f" % (xx + 28, cy - 12, xx, cy + 12), tn + 0.4, 0.15, SAR, 6, 1,
                  None)
        if h == "A":   # A elenir: satır soluklaşır
            s.to("#rowA", tn + 0.2, {"opacity": 0.4, "duration": 0.35})
    # C ve E imleçleri birlikte söner (son 12 kareden önce: global 272,00 → yerel 29,72)
    for h in kal:
        s.to("#pt" + h, S(271.70), {"opacity": 0, "duration": 0.2})
    return s, {"kun": kunye("Mini question", 3), "pos": pos, "nsat": nsat, "bal_ids": bal_ids}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), bal_ids=parca["bal_ids"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "satır", parca["nsat"])

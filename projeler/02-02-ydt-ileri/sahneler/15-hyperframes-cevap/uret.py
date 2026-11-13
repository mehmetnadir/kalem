"""Sahne 15 — Cevap ve çeldiriciler (HyperFrames, 1920x1080, 1416 kare, cümle 54–57).
Soru kartı ve 5 şık sahne 14 ile BİREBİR aynı yerde (kare 0'dan hazır; geçiş fade). Cevapta yalnız doğru şık (B)
vurgulanır: yöntem 3 adım (sağ bölge) → kartta notice ve it → «tabela · it → says» → B şıkkı sarı + onay →
çeldirici notları (C soluk, A, D, E).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (cümle içi sıra numarası). Yerel sn = küresel − t_bas.
Renk yalnız Y.RENK (kunye.js TEMALAR eşleniği): yeşil token yok → doğru şık `vurgu`; kırmızı yok (işaretler ikincil)."""
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
C54, C55, C56, C57 = [[w for w in _HAM if w["cumle"] == n] for n in range(54, 58)]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]

# ---- yerleşim (px) — sahne 14 ile aynı ----
FS, LH = 56, 76
KX, KY, KW, KH = 96, 164, 1728, 278
IX, IW = 140, 1480
PY, RH, RHH = 470, 96, 84
RWD = 900
CHX, OPX = 146, 212
PIX = 1010                           # çeldirici notu (pil) x
PIL_H = 56

# ---- içerik (taslak §4 satır 7.4–7.7; ekran metni değişmez) ----
KOK = [("w", "Look", 2), ("w", "at", 3), ("w", "the", 4), ("w", "notice", 5), ("w", "on", 6), ("w", "the", 7),
       ("w", "library", 8), ("w", "door:", 9), ("w", "it", 10), ("b", 0, 11), ("w", "that", 12), ("w", "the", 13),
       ("w", "library", 14), ("w", "closes", 15), ("w", "at", 16), ("w", "six", 17), ("w", "on", 18),
       ("w", "Fridays.", 19)]
DOLGU = ["says"]
SIK = {"A": "say", "B": "says", "C": "is saying", "D": "said", "E": "has said"}
HARF = "ABCDE"


def T(c, i):
    """Cümle listesi c içindeki i. sözcüğün t0'ı (küresel sn)."""
    return c[i]["t0"]


def yerlestir():
    """Kök simgelerini satırlara dizer (sahne 14 ile aynı algoritma). Döner: (pos listesi, satır sayısı)."""
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
    """Künye (kunye.js ile aynı): bölüm Question, ajanda Hook Rule Roots (etkin Roots)."""
    return Y.kunye_svg("Question", "Question", 2, 2)


def statik_yazi(s, kid, x, y, metin, renk, aile, agr, boy):
    """Kare 0'dan görünen yazı (animasyonsuz)."""
    s.svg.append('<g id="%s" font-family="%s" font-weight="%d" font-size="%s"><text x="%.2f" y="%.2f" fill="%s" '
                 'xml:space="preserve">%s</text></g>' % (kid, aile, agr, boy, x, y, renk, metin))


def uret():
    s = Y.Sahne(TB)
    S = s.S
    tt = lambda c, i: S(T(c, i))  # noqa: E731
    pos, nsat = yerlestir()
    bpos = {KOK[i][1]: pos[i] for i, t in enumerate(KOK) if t[0] == "b"}
    tok = {t[2]: i for i, t in enumerate(KOK) if t[0] == "w"}   # cümle 51 sözcük sırası -> simge sırası
    kimlik = lambda bas: {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}  # noqa: E731
    gruplar = []

    # ================= kare 0: sahne 14'ün bitiş durumu (kart, boşluk, 5 şık, C çerçevesi) =================
    s.svg.append('<path id="kart" d="%s" fill="none" stroke="%s" stroke-width="4.5" stroke-linecap="round" '
                 'stroke-linejoin="round"/>' % (Y.el_kutu(KX, KY, KW, KH), KRE))
    statik_yazi(s, "etiket", KX, 148, "MINI QUESTION", SAR, "Lexend", 700, 32)
    for n, t in enumerate(KOK):
        if t[0] == "w":
            statik_yazi(s, "w%d" % n, pos[n]["x"], pos[n]["base"], t[1], KRE, "Fredoka", 700, FS)
    p = bpos[0]
    s.svg.append('<path id="bl0" d="%s" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round"/>'
                 % (Y.el_cizgi(p["x"] + 4, p["base"] + 12, p["x"] + p["w"] - 4, p["base"] + 12, 2), IKN))
    # doğru şık B için vurgu dolgusu (satırların ARKASINDA; sonradan açılır)
    kb = HARF.index("B")
    s.svg.append('<rect id="hlB" x="%d" y="%d" width="%d" height="%d" rx="24" fill="%s" style="opacity:0"/>'
                 % (KX, PY + kb * RH, RWD, RHH, SAR))
    g0 = len(s.svg)
    for k, h in enumerate(HARF):
        y0 = PY + k * RH
        cy = y0 + RHH / 2
        lw = Y.genislik("Fredoka", 700, h, 40)
        s.svg.append(
            '<g id="row%s">'
            '<circle class="chip" cx="%d" cy="%.1f" r="32" fill="none" stroke="%s" stroke-width="4"/>'
            '<text x="%.1f" y="%.1f" font-family="Fredoka" font-weight="700" font-size="40" fill="%s">%s</text>'
            '<text x="%d" y="%.1f" font-family="Fredoka" font-weight="700" font-size="46" fill="%s" '
            'xml:space="preserve">%s</text></g>' % (h, CHX, cy, KRE, CHX - lw / 2, cy + 14, KRE, h, OPX, cy + 16, KRE, SIK[h]))
    kc = HARF.index("C")
    s.svg.append('<path id="cfr" d="%s" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round" '
                 'stroke-linejoin="round" style="opacity:0.9"/>' % (Y.el_kutu(KX, PY + kc * RH, RWD, RHH), SAR))
    gruplar.append(("panel", kimlik(g0)))

    # ================= C54 (358,53): yöntem — panel söner, C işareti kalkar, 3 adım sağ bölgede =================
    t_y = tt(C54, 0)
    s.to("#panel", t_y, {"opacity": 0.35, "duration": 0.4, "ease": "power2.inOut"})
    s.to("#cfr", t_y, {"opacity": 0, "duration": 0.4})
    s.olay(t_y, "vurus", 0.5)
    g0 = len(s.svg)
    adim = [("1", "çerçeve", 1, 2), ("2", "özne", 4, 5), ("3", "çerçeveyi", 7, 11)]
    SX, SY, SADIM = 1096, 570, 130
    for k, (no, metin, i_no, i_metin) in enumerate(adim):
        cy = SY + k * SADIM
        tn = tt(C54, i_no)
        nw = Y.genislik("Fredoka", 700, no, 48)
        s.yol("an%d" % k, Y.el_daire(SX, cy - 15, 42, 42, k * 0.8), tn, 0.4, SAR, 6, 0.9, "parilti", 0.5)
        s.yazi("ano%d" % k, SX - nw / 2, cy + 3, [(no, KRE)], "Fredoka", 700, 48, tn + 0.1, 0.2, tur="tik", guc=0.5)
        s.yazi("am%d" % k, SX + 84, cy + 8, [(metin, KRE)], "Fredoka", 700, 66, tt(C54, i_metin), 0.3,
               tur="tik", guc=0.55)
    w3 = Y.genislik("Fredoka", 700, adim[2][1], 66)
    assert SX + 84 + w3 + 16 + Y.genislik("Fredoka", 700, "izle", 66) < 1824, "adım 3 taştı"
    s.yazi("am3b", SX + 84 + w3 + 16, SY + 2 * SADIM + 8, [("izle", KRE)], "Fredoka", 700, 66, tt(C54, 12), 0.25,
           tur="tik", guc=0.5)
    gruplar.append(("gAdim", kimlik(g0)))
    s.to("#gAdim", tt(C55, 0) - 0.3, {"opacity": 0, "duration": 0.25})

    # ================= C55 (366,60): çerçeve tabela · özne it → says =================
    def belirtec(idler, t, kid, renk=SAR, w=9):
        a, b = pos[idler[0]], pos[idler[-1]]
        s.yol(kid, Y.el_cizgi(a["x"] - 4, a["base"] + 14, b["x"] + b["w"] + 4, a["base"] + 13, 1),
              t, 0.4, renk, w, 0.85, "cizgi", 0.5)

    belirtec([tok[5]], tt(C55, 3), "z1")           # notice  — «tabela.» 368,00
    belirtec([tok[10]], tt(C55, 5), "z2")          # it      — «it,» 369,57
    g0 = len(s.svg)
    SB, STX = 700, 1090
    e, yer = Y.dizi(s, "st", STX, SB, [
        {"m": "tabela", "t": tt(C55, 3), "tik": True}, {"m": " · ", "t": tt(C55, 5), "r": IKN},
        {"m": "it", "t": tt(C55, 5), "r": SAR}, {"ok": 100, "t": tt(C55, 8), "bos": 24},
        {"m": "says", "t": tt(C55, 9), "r": SAR}], boy=84)
    assert e < 1824 - 20, "şerit taştı: %.0f" % e
    # C56: «tabela sabit: says» — şeritte tabela (378,30) ve says (379,59) altı çizilir
    (_, tx_, tw_), (_, sx_, sw_) = yer[0], yer[4]
    s.yol("su1", Y.el_cizgi(tx_ - 4, SB + 16, tx_ + tw_ + 4, SB + 15, 1), tt(C56, 8), 0.4, SAR, 10, 0.9, "cizgi", 0.55)
    s.yol("su2", Y.el_cizgi(sx_ - 4, SB + 16, sx_ + sw_ + 4, SB + 15, 1), tt(C56, 10), 0.4, SAR, 10, 0.9, "cizgi", 0.55)
    gruplar.append(("gSerit", kimlik(g0)))

    # ================= C56 (374,46): tuzak = C; Türkçe şimdiki gibi → ikincil çarpı; B doğru =================
    cy_c = PY + kc * RH + RHH / 2
    s.yol("ctz", Y.el_kutu(KX, PY + kc * RH, RWD, RHH), tt(C56, 0), 0.45, IKN, 4, 0.85, "cizgi", 0.5)    # «Tuzak» 374,46
    d1, d2 = Y.carpi(KX + RWD - 96, cy_c - 24, 48)
    s.yol("cx1", d1, tt(C56, 4), 0.2, IKN, 7, 1, "cizgi", 0.6)                                          # «şimdiki» 376,54
    s.yol("cx2", d2, tt(C56, 4) + 0.2, 0.2, IKN, 7, 1, None)
    s.olay(tt(C56, 4) + 0.2, "vurus", 0.6)
    t_b = tt(C56, 13)                                # «B» 381,76
    s.to("#gSerit", t_b - 1.2, {"opacity": 0, "duration": 0.3})
    s.to("#panel", t_b - 1.2, {"opacity": 1, "duration": 0.35, "ease": "power2.out"})
    s.to("#hlB", t_b, {"opacity": 0.3, "duration": 0.3, "ease": "power2.out"})
    s.yol("bfr", Y.el_kutu(KX, PY + kb * RH, RWD, RHH), t_b, 0.45, SAR, 5, 1, "cizgi", 0.7)
    s.yol("ck", Y.tik_yolu(KX + RWD - 110, PY + kb * RH + 20, 44), t_b + 0.25, 0.3, SAR, 9, 1, "cizgi", 0.55)
    s.olay(t_b, "vurus", 0.85)
    fw = Y.genislik("Fredoka", 700, DOLGU[0], FS)
    td = tt(C56, 16)                                 # «says.» 383,37 boşluğa yazılır
    s.yazi("fl0", p["x"] + (p["w"] - fw) / 2, p["base"], [(DOLGU[0], KRE)], "Fredoka", 700, FS, td, 0.3,
           tur="tik", guc=0.55)
    s.yol("gb0", Y.el_cizgi(p["x"] + 2, p["base"] + 12, p["x"] + p["w"] - 2, p["base"] + 11, 1),
          t_b + 0.5, 0.35, SAR, 8, 1, "cizgi", 0.5)

    # ================= C57 (384,96): çeldirici notları =================
    onceki = []

    def not_pili(h, parcalar, t_imlec, soluk=False):
        """Şık satırına sarı imleç (öncekini söndürür) + sik_not pili. parcalar: {"t": metin | "ok" | "x", "ts": küresel sn}."""
        k = HARF.index(h)
        cy = PY + k * RH + RHH / 2
        s.yol("pt" + h, Y.el_ok(58, cy, 106, cy, 1), S(t_imlec), 0.25, SAR, 7, 0.95, "tik", 0.45)
        for o in onceki:
            s.to("#pt" + o, S(t_imlec), {"opacity": 0, "duration": 0.15})
        onceki.append(h)
        gen, x = [], PIX + 22.0
        for n, pr in enumerate(parcalar):
            # QA 13.11: metin-metin bitişiminde kerning payı ölçülmüyor → aralık 14 yerine 8 px
            x += (8 if parcalar[n - 1]["t"] not in ("ok", "x") and pr["t"] not in ("ok", "x") else 14) if n else 0
            w = Y.genislik("Lexend", 500, pr["t"], 30) if pr["t"] not in ("ok", "x") else {"ok": 44, "x": 28}[pr["t"]]
            gen.append((x, w))
            x += w
        pw = x + 22 - PIX
        assert PIX + pw <= KX + KW, "pil taştı: " + h
        t0 = S(parcalar[0]["ts"])
        s.svg.append('<rect id="pf%s" x="%d" y="%.1f" width="%.1f" height="%d" rx="28" fill="none" stroke="%s" '
                     'stroke-width="3" style="opacity:0"/>' % (h, PIX, cy - PIL_H / 2, pw, PIL_H, IKN))
        s.fromto("#pf" + h, t0, {"opacity": 0, "x": -24}, {"opacity": 0.6 if soluk else 1, "x": 0, "duration": 0.3,
                                                          "ease": "power3.out"})
        for n, (pr, (px, pw_)) in enumerate(zip(parcalar, gen)):
            ts = S(pr["ts"])
            if pr["t"] == "ok":
                s.yol("po%s%d" % (h, n), Y.el_ok(px, cy, px + 40, cy, 1), ts, 0.25, IKN, 5, 0.6 if soluk else 1, "tik", 0.4)
            elif pr["t"] == "x":
                a, b = Y.carpi(px, cy - 13, 26)
                s.yol("px%s%da" % (h, n), a, ts, 0.12, IKN, 6, 0.6 if soluk else 1, "cizgi", 0.4)
                s.yol("px%s%db" % (h, n), b, ts + 0.13, 0.12, IKN, 6, 0.6 if soluk else 1, None)
            else:
                s.yazi("pm%s%d" % (h, n), px, cy + 10.5, [(pr["t"], IKN)], "Lexend", 500, 30, ts, 0.25,
                       tur="tik", guc=0.4, sar_ek='opacity=".6"' if soluk else "")

    not_pili("C", [{"t": "Türkçe şimdiki gibi, tabela sabit", "ts": T(C57, 1)}, {"t": "x", "ts": T(C57, 1) + 0.5}],
             T(C57, 1), soluk=True)                                                          # «bakalım.» 385,76
    not_pili("A", [{"t": "it için", "ts": T(C57, 5)}, {"t": "s yok", "ts": T(C57, 7)}, {"t": "x", "ts": T(C57, 8)}],
             T(C57, 3))                                                                      # A 387,44 · it · se · yok
    not_pili("D", [{"t": "Look at", "ts": T(C57, 13)}, {"t": "ok", "ts": T(C57, 19)},
                   {"t": "sabit içerik: says", "ts": T(C57, 20)}, {"t": "x", "ts": T(C57, 22)}],
             T(C57, 10))                                                                     # D 391,22 · Look · sabit · ile
    not_pili("E", [{"t": "sürekli duran tabela", "ts": T(C57, 27)}, {"t": "x", "ts": T(C57, 31)}],
             T(C57, 25))                                                                     # E 400,38 · tabela · yeter.
    return s, {"kun": kunye(), "gruplar": gruplar}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

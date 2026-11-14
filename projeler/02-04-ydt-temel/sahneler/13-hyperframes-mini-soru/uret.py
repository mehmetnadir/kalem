"""Sahne 13 Mini soru (02-04 YDT temel, HyperFrames, 1920x1080; cümle 15 soru + 16 öğrenci + 17 öğretmen).
BRIEF §3 No 13: `soru` kök + 5 şık + sayaç («Beş şık var»), yanlış cevap A balonu + soluk sarı çerçeve,
`odak` (lives in Ankara, this month; ses sırasıyla), `dogru` (B vurgu dolgusu + koyu tik), `sik_not` pilleri;
çıkış fade geçiş katmanında. Ses şıkları okumaz (D-0205); ekran metni senaryo-taslak satır 15-17.
Kalıp 02-03 sahne 13 (kart + 5 şıklı panel + sayaç + pil). Doğru şık: ham yeşil yok (13.11 QA); dolgu vurgu,
üstündeki yazı ve tik koyu (#1b1a17 satır içi stil: iki temada da dolgu üstünde okunur).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn; i = cümle içi sıra).
Yerel sn = küresel - t_bas. Ölçüler mantıksal px (yatay 1920 tabanı) -> u(); sabit px yok."""
import json
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402
from yardim import u  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_ham = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
SOZ = {c: [w for w in _ham if w["cumle"] == c] for c in (15, 16, 17)}   # 15 soru · 16 öğrenci · 17 cevap
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
KOYU = R["zemin"]   # doğru şık dolgusu üstündeki yazı + tik (GSAP satır içi stil; tema eşlemesine girmez)
TB = Z["t_bas"]

# ---- yerleşim (mantıksal px; 02-03 sahne 13 ile aynı ızgara) ----
FS, LH, TAB = u(72), u(96), u(69)                 # kök yazısı, satır aralığı, taban payı
KX, KY, KW, KH = u(96), u(164), u(1728), u(278)   # soru kartı
IX, IW = u(140), u(1480)                          # kart içi yazı alanı (sağda sayaç payı)
PY, RH, RHH = u(470), u(96), u(84)                # şık paneli başı, satır adımı, satır yüksekliği
CHX, OPX = u(146), u(212)                         # harf dairesi merkezi, şık metni x
PIX, PIL_H, PF = u(1010), u(56), u(30)            # çeldirici notu (pil) x, yükseklik, yazı boyu
ALT = u(14)                                       # boşluk çizgisi: taban çizgisinin altı
AFR_W = PIX - u(24) - KX                          # A çerçevesi: harf + şık metni (öğrenci başına değmez)
SAY_X, SAY_Y, SAY_R = u(1700), u(303), u(46)      # sayaç halkası
BAS_X, BAS_Y, BS = u(1040), u(470), u(0.6)        # öğrenci başı (ogrenci-bas.svg) konum ve ölçek
BF, BX0, BY0 = u(44), u(1250), u(500)             # balon yazısı, balon sol-üst

# ---- içerik (senaryo-taslak satır 15-17; ekran metni değişmez) ----
# Kök iki satır (anlam öbeği bölünmez): ("w", metin, cümle-15 sözcük sırası) · ("b",) boşluk
KOK = [[("w", "My", 2), ("w", "brother", 3), ("w", "lives", 4), ("w", "in", 5), ("w", "Ankara,", 6)],
       [("w", "but", 7), ("w", "this", 8), ("w", "month", 9), ("w", "he", 10), ("b",), ("w", "with", 11),
        ("w", "us.", 12)]]
DOLGU = "is living"
SIK = {"A": "lives", "B": "is living", "C": "live", "D": "to live", "E": "are living"}
# çeldirici notları: (harf, imleç sözcüğü | None, pil sözcüğü, parçalar); A imleçsiz (soluk çerçeve gösterir)
NOT = [("A", None, (13, "geçici"), [["t", "this month"], ["->"], ["t", "temporary"], ["x"]]),
       ("C", (22, "C"), (27, "özne"), [["t", "he"], ["<>"], ["t", "live"], ["x"]]),
       ("E", (25, "E"), (28, "uyum"), [["t", "he"], ["<>"], ["t", "are"], ["x"]]),
       ("D", (29, "D"), (31, "tek"), [["t", "to live: no tense"], ["x"]])]


def T(c: int, i: int, bas: str) -> float:
    """Cümle c, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[c][i]
    assert w["sozcuk"].lower().startswith(bas.lower()), "cümle %d sözcük %d: %r, beklenen %r" % (
        c, i, w["sozcuk"], bas)
    return w["t0"]


def yerlestir() -> list:
    """Kök simgelerini iki satıra dizer. Döner: [{x, w, base, t}] (KOK düzleştirilmiş sırayla)."""
    sp = Y.genislik("Fredoka", 700, " ", FS)
    top = KY + (KH - len(KOK) * LH) / 2
    pos = []
    for li, sat in enumerate(KOK):
        x = IX
        for t in sat:
            w = (Y.genislik("Fredoka", 700, t[1], FS) if t[0] == "w"
                 else Y.genislik("Fredoka", 700, DOLGU, FS) + u(48))
            pos.append({"x": x, "w": w, "base": top + li * LH + TAB, "t": t})
            x += w + sp
        assert x - sp <= IX + IW + 1, "satır taştı: %d" % li
    return pos


def pil_olc(parcalar: list) -> float:
    """Çeldirici notu genişliği: metin Lexend 500 PF; <> ve -> u(44); x u(28); parça arası u(14); iç pay u(44)."""
    w = 0.0
    for n, p in enumerate(parcalar):
        w += u(14) if n else 0
        if p[0] == "t":
            w += Y.genislik("Lexend", 500, p[1], PF)
        else:
            w += {"<>": u(44), "->": u(44), "x": u(28)}[p[0]]
    return w + u(44)


def pil(s: Y.Sahne, h: str, cy: float, parcalar: list, tn: float) -> None:
    """sik_not pili: ince çerçeve + parçalar; çarpı vurgu renginde (kırmızı yok); tn'de soldan kayarak gelir."""
    pw = pil_olc(parcalar)
    assert PIX + pw <= KX + KW, "pil taştı: " + h
    g = ['<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="none" stroke="%s" '
         'stroke-width="%.1f"/>' % (PIX, cy - PIL_H / 2, pw, PIL_H, u(28), IKN, u(3))]
    x, xx = PIX + u(22), None
    for n, q in enumerate(parcalar):
        x += u(14) if n else 0
        if q[0] == "t":
            g.append('<text x="%.1f" y="%.1f" font-family="Lexend" font-weight="500" font-size="%.1f" '
                     'fill="%s" xml:space="preserve">%s</text>' % (x, cy + u(10.5), PF, IKN, q[1]))
            x += Y.genislik("Lexend", 500, q[1], PF)
        elif q[0] in ("<>", "->"):
            ok = "M%.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (
                x + u(2), cy, x + u(42), cy, x + u(32), cy - u(9), x + u(42), cy, x + u(32), cy + u(9))
            if q[0] == "<>":
                ok += " M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (x + u(12), cy - u(9), x + u(2), cy, x + u(12),
                                                             cy + u(9))
            g.append('<path d="%s" fill="none" stroke="%s" stroke-width="%.1f" stroke-linecap="round" '
                     'stroke-linejoin="round"/>' % (ok, IKN, u(3.5)))
            x += u(44)
        else:
            xx = x
            x += u(28)
    s.svg.append('<g id="pil%s" style="opacity:0">%s</g>' % (h, "".join(g)))
    s.goster("#pil" + h, tn, 0.3, -u(24), 0)
    s.olay(tn, "tik", 0.4)
    if xx is not None:
        s.yol("px1" + h, "M%.1f %.1f L%.1f %.1f" % (xx, cy - u(12), xx + u(28), cy + u(12)), tn + 0.25, 0.15,
              SAR, u(6), 1, "cizgi", 0.4)
        s.yol("px2" + h, "M%.1f %.1f L%.1f %.1f" % (xx + u(28), cy - u(12), xx, cy + u(12)), tn + 0.4, 0.15,
              SAR, u(6), 1, None)


def uret() -> tuple:
    s = Y.Sahne(TB)
    S = s.S
    pos = yerlestir()
    bos = next(p for p in pos if p["t"][0] == "b")
    harfler = "ABCDE"
    bal_ids = []

    # ---------------- soru kartı (220,88 «Mini soru») + kök sözcük sözcük ----------------
    t_kart = S(T(15, 0, "Mini"))
    s.yol("kart", Y.el_kutu(KX, KY, KW, KH), t_kart, 0.6, KRE, u(4.5), 1, "cizgi", 0.7)
    s.yazi("etiket", KX, u(148), [("MINI QUESTION", SAR)], "Lexend", 700, u(32), t_kart + 0.15, 0.3,
           tur="tik", guc=0.45)
    for n, p in enumerate(pos):
        t = p["t"]
        if t[0] == "w":
            s.yazi("w%d" % n, p["x"], p["base"], [(t[1], KRE)], "Fredoka", 700, FS, S(T(15, t[2], t[1][:2])),
                   0.14, tur="tik" if n == 0 else None, guc=0.5)
    # boşluk çizgisi: «he» ile «with» arasındaki susmada (0,5 sn) çizilir
    s.yol("bl0", Y.el_cizgi(bos["x"] + u(4), bos["base"] + ALT, bos["x"] + bos["w"] - u(4), bos["base"] + ALT, 2),
          S(SOZ[15][10]["t1"]) + 0.06, 0.3, IKN, u(5), 1, "cizgi", 0.5)
    # «Boşluğa» (227,25): soluk çizgi söner, aynı yere vurgu çizgisi çizilir (ikisi aynı anda görünmez)
    tbo = S(T(15, 13, "Boş"))
    s.to("#bl0", tbo, {"opacity": 0, "duration": 0.15})
    s.yol("gb0", Y.el_cizgi(bos["x"] + u(2), bos["base"] + ALT, bos["x"] + bos["w"] - u(2), bos["base"] + ALT - 1,
                            1), tbo + 0.15, 0.35, SAR, u(8), 1, "cizgi", 0.5)

    # ---------------- sayaç «Beş şık var» (229,33-230,29): halka dolar, ortada 5 ----------------
    tsay = S(T(15, 17, "Beş"))
    s.yol("say", "M%.1f %.1f A%.1f %.1f 0 1 1 %.2f %.1f" % (SAY_X, SAY_Y - SAY_R, SAY_R, SAY_R, SAY_X - 0.01,
                                                           SAY_Y - SAY_R), tsay, 0.96, SAR, u(8), 1, "cizgi", 0.55)
    nw = Y.genislik("Fredoka", 700, "5", u(60))
    s.yazi("say5", SAY_X - nw / 2, SAY_Y + u(22), [("5", KRE)], "Fredoka", 700, u(60), tsay + 0.04, 0.2,
           tur="tik", guc=0.5)
    s.to("#say", tsay + 1.12, {"opacity": 0, "duration": 0.25})
    s.to("#say5", tsay + 1.12, {"opacity": 0, "duration": 0.25})

    # ---------------- şık paneli («Beş»: satırlar 0,18 sn arayla gelir) ----------------
    for k, h in enumerate(harfler):
        y0 = PY + k * RH
        cy = y0 + RHH / 2
        lw = Y.genislik("Fredoka", 700, h, u(40))
        ow = Y.genislik("Fredoka", 700, SIK[h], u(46))
        assert OPX + ow < PIX - u(24), "şık metni nota değiyor: " + SIK[h]
        s.svg.append(
            '<g id="row%s" style="opacity:0">'
            '<rect id="gr%s" x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" '
            'stroke-width="%.1f" style="opacity:0"/>'
            '<circle class="chip" cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%.1f"/>'
            '<text x="%.1f" y="%.1f" font-family="Fredoka" font-weight="700" font-size="%.1f" fill="%s">%s</text>'
            '<text x="%.1f" y="%.1f" font-family="Fredoka" font-weight="700" font-size="%.1f" fill="%s" '
            'xml:space="preserve">%s</text></g>'
            % (h, h, KX, y0, KW, RHH, u(24), SAR, SAR, u(4), CHX, cy, u(32), SAR, u(4),
               CHX - lw / 2, cy + u(14), u(40), KRE, h, OPX, cy + u(16), u(46), KRE, SIK[h]))
        s.goster("#row" + h, tsay + 0.18 * k, 0.35, 0, u(24))
    s.olay(tsay, "tik", 0.5)
    s.olay(tsay + 0.4, "tik", 0.4)

    # ---------------- öğrenci başı + balon: yanlış cevap A (230,76-234,36) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.3f)" fill="none" stroke="%s" '
                 'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>'
                 % (BAS_X, BAS_Y, BS, KRE, u(2.8) / BS,
                    "".join('<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = S(T(16, 0, "Bence")) - 0.18
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    sp = Y.genislik("Fredoka", 600, " ", BF)
    satir = ((0, 1, 2), (3, 4), (5, 6))      # Bence A şıkkı. / Yaşamak kalıcı / bir durum.
    gens = [sum(Y.genislik("Fredoka", 600, SOZ[16][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = BX0 + max(gens) + u(70)
    assert x1b < u(1880), "balon taştı: %.0f" % x1b
    s.yol("bal", Y.balon_sol(BX0, BY0, x1b, BY0 + u(254), BX0 - u(78), BY0 + u(118)), t0 + 0.1, 0.55, KRE,
          u(4.2), 1, "cizgi", 0.7)
    bal_ids.append("bal")
    for sat, base in zip(satir, (BY0 + u(72), BY0 + u(136), BY0 + u(200))):
        x = BX0 + u(35)
        for i in sat:
            m = SOZ[16][i]["sozcuk"]
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Fredoka", 600, BF, S(SOZ[16][i]["t0"]), 0.12,
                   tur="tik" if i in (0, 3) else None)
            bal_ids.append("bw%d" % i)
            x += Y.genislik("Fredoka", 600, m, BF) + sp
    # A şıkkı: soluk sarı çerçeve (231,40 «A»); A notu gelince söner
    tA = S(T(16, 1, "A"))
    s.svg.append('<rect id="afr" x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="none" stroke="%s" '
                 'stroke-width="%.1f" style="opacity:0"/>'
                 % (KX, PY + harfler.index("A") * RH, AFR_W, RHH, u(24), SAR, u(4)))
    s.to("#afr", tA, {"opacity": 0.55, "duration": 0.3, "ease": "power2.out"})
    s.olay(tA, "tik", 0.5)

    # ---------------- öğretmen cevabı (235,03 «Ankara'da»): balon söner; kökte odak ses sırasıyla ----------------
    th = S(T(17, 0, "Ankara"))
    s.to("#balg", th, {"opacity": 0, "duration": 0.4, "ease": "power2.in"})
    s.olay(th, "vurus", 0.6)
    p0, p1 = pos[2], pos[4]                         # lives … Ankara (virgül dışarıda)
    x1 = p1["x"] + Y.genislik("Fredoka", 700, "Ankara", FS)
    s.yol("odak1", Y.el_cizgi(p0["x"] - u(4), p0["base"] + ALT + u(2), x1 + u(4), p0["base"] + ALT + u(1), 1),
          th + 0.1, 0.45, SAR, u(9), 0.85, "cizgi", 0.5)
    q0, q1 = pos[6], pos[7]                         # this month («bu ayı»)
    s.yol("odak2", Y.el_cizgi(q0["x"] - u(4), q0["base"] + ALT + u(2), q1["x"] + q1["w"] + u(4),
                              q0["base"] + ALT + u(1), 1), S(T(17, 6, "bu")), 0.4, SAR, u(9), 0.85, "cizgi", 0.5)

    # ---------------- doğru şık B (243,43 «B»): vurgu dolgusu + koyu yazı + koyu tik ----------------
    tdg = S(T(17, 17, "B"))
    kb = harfler.index("B")
    s.to("#grB", tdg, {"opacity": 1, "duration": 0.3, "ease": "power2.out"})
    s.to("#rowB text", tdg, {"fill": KOYU, "duration": 0.3})
    s.to("#rowB .chip", tdg, {"stroke": KOYU, "duration": 0.3})
    s.yol("ck", Y.tik_yolu(KX + KW - u(110), PY + kb * RH + u(20), u(44)), tdg + 0.2, 0.3, KOYU, u(9), 1, "cizgi",
          0.55)
    s.set("#ck", tdg, {"stroke": KOYU})   # satır içi: tema eşlemesi (zemin) açık temada tiki açık renge çevirmez
    s.olay(tdg, "vurus", 0.85)
    # «is» (244,95): boşluğa «is living» yazılır (vurgu çizgisi gb0 altında kalır)
    fw = Y.genislik("Fredoka", 700, DOLGU, FS)
    s.yazi("fl0", bos["x"] + (bos["w"] - fw) / 2, bos["base"], [(DOLGU, KRE)], "Fredoka", 700, FS,
           S(T(17, 20, "is")), 0.3, tur="tik", guc=0.55)

    # ---------------- çeldirici notları: imleç + pil; elenen satır soluklaşır ----------------
    imlec = []
    for h, isaret, notu, parcalar in NOT:
        cy = PY + harfler.index(h) * RH + RHH / 2
        if isaret:
            ti = S(T(17, *isaret))
            if h == "D":   # D'ye geçince C ve E imleçleri söner
                for e in imlec:
                    s.to("#pt" + e, ti, {"opacity": 0, "duration": 0.15})
            s.yol("pt" + h, Y.el_ok(u(30), cy, u(84), cy, 1), ti, 0.25, SAR, u(7), 0.95, "tik", 0.45)
            imlec.append(h)
        tn = S(T(17, *notu))
        pil(s, h, cy, parcalar, tn)
        s.to("#row" + h, tn + 0.2, {"opacity": 0.4, "duration": 0.35})
        if h == "A":
            s.to("#afr", tn, {"opacity": 0, "duration": 0.25})
    bas, son = Y.kontrol(s, Z["kare"])
    return s, {"kun": Y.kunye_svg("Mini question", 3), "bal_ids": bal_ids, "aralik": (bas, son)}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (u(56), u(1002), u(34) * Y.LOGO_EN_BOY, u(34)),
               bal_ids=parca["bal_ids"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "hareket", parca["aralik"])

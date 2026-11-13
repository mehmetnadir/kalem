"""Sahne 07 Kural kartı (02-03 YDT temel, HyperFrames, 1920x1080; cümle 8).
`tanim` 3 satır (3 bant) söylendiği anda kademeli gelir: NOW → am / is / are + V-ing (sarı) · THESE DAYS · NOWADAYS ·
PLAN → usually V-ing (temporary / changing) · USUALLY · GENERAL → V1 / V-s. Sağda üç örnek kartı küçük hâlde (sahne
03–05); satır 2'nin sinyal sözcükleri kendi örnek kartına ince çizgiyle bağlanır. Sahne 12 (özet) aynı görsel dili kullanır.
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn; i = cümle içi sıra).
Yerel sn = küresel - t_bas."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text()) if w["cumle"] == 8]
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]

# ---- yerleşim (px) ----
BX, BW = 96, 1060                 # bant sol kenar, genişlik (sağ kenar 1156)
IX = 140                          # bant içi yazı başı
SF, RF = 56, 52                   # sinyal yazısı, sonuç yazısı (Fredoka 700)
BANT = ((150, 180), (360, 330), (720, 170))     # (y, yükseklik)
BASE = {"r1": 262, "a": 452, "b": 552, "c": 630, "r3": 826}   # taban çizgileri
AU, BO = 84, 24                   # ok uzunluğu, ok çevresi boşluğu
CX, CW = 1260, 564                # örnek kartı sol kenar, genişlik
CF, CL = 30, 40                   # kart yazı boyu, satır adımı
KC = (330, 560, 790)              # kart merkez y (örnek 1, 2, 3)
ORNEK = ("We are leaving for the airport at 9.",
         "Our company is going through a hard period these days.",
         "It is getting harder and harder to find a good job nowadays.")
# kart içi işaretlenecek sözcük sıraları: ex1 "at 9", ex2 "these days", ex3 "nowadays" (cümle sonu noktası dışarıda)
ISARET = ((6, 7), (8, 9), (11,))


def T(i):
    return SOZ[i]["t0"]


def gen(m, b):
    return Y.genislik("Fredoka", 700, m, b)


def kart_yerlesim(metin):
    """Metni CW-40 genişliğe sarar. Döner: (sözcükler, satırlar [sözcük sıraları], kart yüksekliği)."""
    sp = gen(" ", CF)
    kel = metin.split(" ")
    satirlar, cur, cw = [], [], 0.0
    for k, w in enumerate(kel):
        gw = gen(w, CF)
        if cur and cw + sp + gw > CW - 40:
            satirlar.append(cur)
            cur, cw = [], 0.0
        cw += (sp if cur else 0) + gw
        cur.append(k)
    satirlar.append(cur)
    return kel, satirlar, 28 + len(satirlar) * CL + 20


def uret():
    s = Y.Sahne(Z["t_bas"])
    S = s.S
    # ---------------- bantlar (söylenen "Karar kartı": 88,33) ----------------
    for i, ((y, h), renk, w) in enumerate(zip(BANT, (SAR, IKN, IKN), (5.0, 4.0, 4.0))):
        s.yol("bn%d" % i, Y.el_kutu(BX, y, BW, h), S(T(0)) + 0.2 * i, 0.55, renk, w, 0.95 if i == 0 else 0.8,
              "cizgi", 0.6 if i == 0 else 0.4)
    isr = []                                # sinyal belirteçleri (son vurgu için)

    def parca(kim, x, y, m, t, renk, boy=SF, d=0.35, tur="tik"):
        s.yazi(kim, x, y, [(m, renk)], "Fredoka", 700, boy, S(t), d, tur=tur, guc=0.5)
        return x + gen(m, boy)

    def belirtec(kim, x0, x1, y, t):
        s.yol(kim, Y.el_cizgi(x0 - 4, y + 14, x1 + 4, y + 13, 1), S(t), 0.4, SAR, 9, 0.85, "cizgi", 0.5)
        isr.append(kim)

    def ok(kim, x, y, t, uz=AU):
        s.yol(kim, Y.el_ok(x, y - 16, x + uz, y - 16, 2.0), S(t), 0.3, KRE, 6, 0.9, "cizgi", 0.5)

    # ---------------- satır 1: NOW → am / is / are + V-ing (sarı) ----------------
    b1 = BASE["r1"]
    xe = parca("r1a", IX, b1, "NOW", T(4), KRE)
    belirtec("m1", IX, xe, b1, T(4) + 0.1)
    ok("o1", xe + BO, b1, T(8))
    xs = xe + BO + AU + BO
    xe = parca("r1b", xs, b1, "am / is / are + V-ing", T(8) + 0.14, SAR, RF, 0.5)
    sat1 = xe
    # ---------------- satır 2: THESE DAYS · NOWADAYS · PLAN → usually V-ing (temporary / changing) ----------------
    ba, bb, bc = BASE["a"], BASE["b"], BASE["c"]
    sp = gen(" ", SF)
    x_th = IX
    xe = parca("r2a", x_th, ba, "THESE DAYS", T(10), KRE, SF, 0.4)
    belirtec("m2", x_th, xe, ba, T(10) + 0.1)
    x_nw = xe + sp
    dot = gen("· ", SF)
    xe = parca("r2b", x_nw, ba, "· NOWADAYS", T(13), KRE, SF, 0.45)
    belirtec("m3", x_nw + dot, xe, ba, T(13) + 0.1)
    x_pl = xe + sp
    xe = parca("r2c", x_pl, ba, "· PLAN", T(23), KRE, SF, 0.35)
    belirtec("m4", x_pl + dot, xe, ba, T(23) + 0.1)
    sat2 = xe
    ok("o2", IX, bb, T(14))
    xu = IX + AU + BO
    xe = parca("r2d", xu, bb, "usually V-ing", T(14) + 0.12, IKN, RF, 0.5)
    sat2 = max(sat2, xe)
    s.yazi("r2e", xu, bc, [("(temporary", IKN)], "Caveat", 700, 44, S(T(18)), 0.45, tur="tik", guc=0.35)
    wt = Y.genislik("Caveat", 700, "(temporary ", 44)
    s.yazi("r2f", xu + wt, bc, [("/ changing)", IKN)], "Caveat", 700, 44, S(T(21)), 0.45, tur=None)
    sat2 = max(sat2, xu + wt + Y.genislik("Caveat", 700, "/ changing)", 44))
    # ---------------- satır 3: USUALLY · GENERAL → V1 / V-s ----------------
    b3 = BASE["r3"]
    xe = parca("r3a", IX, b3, "USUALLY", T(29), KRE, SF, 0.4)
    belirtec("m5", IX, xe, b3, T(29) + 0.1)
    x_gn = xe + sp
    xe = parca("r3b", x_gn, b3, "· GENERAL", T(34), KRE, SF, 0.4)
    belirtec("m6", x_gn + dot, xe, b3, T(34) + 0.1)
    ok("o3", xe + BO, b3, T(36))
    xe = parca("r3c", xe + BO + AU + BO, b3, "V1 / V-s", T(36) + 0.14, IKN, RF, 0.4)
    sat3 = xe
    for n, ex in (("1", sat1), ("2", sat2), ("3", sat3)):
        assert ex <= BX + BW - 30, "satır %s banda taştı: %.0f" % (n, ex)

    # ---------------- örnek kartları (sahne 03-05'in küçük hâli; yazı soluk, sinyal sarı) ----------------
    kart_t = S(T(0)) - 0.1                   # 88,23 sn: "Karar kartı" öncesi hafif, ilk 12 kare durgun
    bag_t = (T(23) + 0.1, T(10) + 0.1, T(13) + 0.1)   # örnek 1 (PLAN), 2 (THESE DAYS), 3 (NOWADAYS)
    for k, metin in enumerate(ORNEK):
        kel, satirlar, h = kart_yerlesim(metin)
        y0 = KC[k] - h / 2
        s.yol("ec%d" % k, Y.el_kutu(CX, y0, CW, h), max(kart_t, 0.5) + 0.12 * k, 0.5, IKN, 3.2, 0.75, "cizgi", 0.35)
        pos = {}
        for li, sat in enumerate(satirlar):
            x = CX + 20
            base = y0 + 28 + li * CL + 26
            for kk in sat:
                pos[kk] = (x, base, gen(kel[kk], CF))
                x += gen(kel[kk], CF) + gen(" ", CF)
            m = " ".join(kel[kk] for kk in sat)
            s.yazi("ex%d_%d" % (k, li), CX + 20, base, [(m, IKN)], "Fredoka", 700, CF, 0.65 + 0.12 * k, 0.4, tur=None)
        # kart sinyal belirteci (satır başına bir parça); söylenen sinyalle aynı anda
        sat_idx = {}
        for kk in ISARET[k]:
            for li, sat in enumerate(satirlar):
                if kk in sat:
                    sat_idx.setdefault(li, []).append(kk)
        for li, ks in sat_idx.items():
            x0 = pos[ks[0]][0]
            x1 = pos[ks[-1]][0] + pos[ks[-1]][2]
            if ks[-1] == len(kel) - 1:      # cümle sonu noktası işarete girmez
                x1 -= gen(".", CF)
            s.yol("em%d_%d" % (k, li), Y.el_cizgi(x0 - 3, pos[ks[0]][1] + 10, x1 + 3, pos[ks[0]][1] + 9, 1),
                  S(bag_t[k]) + 0.25, 0.35, SAR, 8, 0.9, "cizgi", 0.4)
        # satır 2 bandından karta ince bağ çizgisi
        s.yol("bg%d" % k, Y.el_cizgi(BX + BW + 2, 525, CX - 8, KC[k], 3.0), S(bag_t[k]), 0.4, IKN, 3.0, 0.85,
              "cizgi", 0.4)

    # ---------------- son: "Önce sinyal sözcüğünü ara." (107,85; sinyal 108,25) ----------------
    for kim in isr:
        s.to("#" + kim, S(T(40)), {"attr": {"stroke-width": 15}, "opacity": 1, "duration": 0.3, "ease": "power2.out"})
    s.olay(S(T(40)), "vurus", 0.7)
    Y.kontrol(s, Z["kare"])
    return s, Y.kunye_svg("Rule", 2)


if __name__ == "__main__":
    s, kun = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34)))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

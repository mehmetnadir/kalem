"""Sahne 06 DİKEY (SIMPLE PAST İLERİ, 1080x1920): öğrenci sorusu + kural + form + kod.
Yerleşim BRIEF-DIKEY §2-§4: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform bandı boş.
Soru evresi bandı doldurur (balon üstte, yanlış öneri `has resigned + ago` alt-orta büyük). 71,06'dan sonra:
  üst blok = balon+baş (ölçek 0,80 → 57,6 px) · `Olmaz.` + öneri özeti · çipler (Fredoka 56):
  kart -> çip 1 · sütunlar -> çip 2, 3 · Did not resign -> çip 4 · kod (alt bölge) + formül kartı.
Tek kaynak: ortak/anlatim/{sozcukler,altyazi}.json (küresel sn) + zamanlar.json. Yerel sn = t - t_bas."""
import json
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
ANL = AD / ".." / ".." / "ortak" / "anlatim"
SOZ = {c: [w for w in json.loads((ANL / "sozcukler.json").read_text()) if w["cumle"] == c] for c in (6, 7)}
ALT = [a for a in json.loads((ANL / "altyazi.json").read_text()) if a["cumle"] in (6, 7)]
R = Y.RENK
KRE, IKN, SAR, KIR = R["murekkep"], R["ikincil"], R["vurgu"], R["kirmizi"]
TB = Z["t_bas"]
X0 = 48.0


def T(c, i):
    return SOZ[c][i]["t0"]


def T1(c, i):
    return SOZ[c][i]["t1"]


def kimlikler(s, bas):
    """s.svg[bas:] elemanlarının üst düzey id kümesi (bölüm grubu için)."""
    return {e.split('id="', 1)[1].split('"', 1)[0] for e in s.svg[bas:]}


def kelimeler(s, kimlik, x, y, idx, c, aile, agr, boy, renk=KRE, tur0="tik"):
    """Sözcükleri konuşma zamanında tek tek açar. Döner: [(x, w)]."""
    sp = Y.genislik(aile, agr, " ", boy)
    yer, cx = [], x
    for n, i in enumerate(idx):
        m = SOZ[c][i]["sozcuk"]
        w = Y.genislik(aile, agr, m, boy)
        s.yazi("%s%d" % (kimlik, n), cx, y, [(m, renk)], aile, agr, boy, s.S(T(c, i)), 0.12,
               tur=tur0 if n == 0 else None)
        yer.append((cx, w))
        cx += w + sp
    return yer


def topla(s, grup, t, cx, cy, hx, hy, sure=0.4):
    """Bölüm grubunu çip konumuna (hx, hy) küçülterek toplar ve söndürür (merkez cx, cy)."""
    s.to("#" + grup, t, {"svgOrigin": "%.0f %.0f" % (cx, cy), "x": round(hx - cx, 1), "y": round(hy - cy, 1),
                         "scale": 0.3, "opacity": 0, "duration": sure, "ease": "power3.in"})


def uret():
    s = Y.Sahne(TB)
    S = s.S
    bal_ids = []
    # ---------------- öğrenci başı (peeps-kit, 160 px) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.484, 63.0, 535.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.3f)" fill="none" stroke="%s" '
                 'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (
                     BTX, BTY, BS, KRE, 3.6 / BS, "".join(
                         '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = max(S(T(6, 0)) - 0.14, 0.42)    # soğuk açılış: ilk 12 kare (0,40 sn) boş
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    # ---------------- konuşma balonu: 3 satır Caveat 72 ----------------
    BF, BX, BASE = 72, 280.0, (456, 540, 624)
    sp = Y.genislik("Caveat", 700, " ", BF)
    satir = ((0, 1, 2), (3, 4, 5), (6, 7))
    gens = [sum(Y.genislik("Caveat", 700, SOZ[6][i]["sozcuk"], BF) for i in sat) + sp * (len(sat) - 1)
            for sat in satir]
    x1b = min(1032.0, BX + max(gens) + 40)
    s.yol("bal", Y.balon_sol(240, 372, x1b, 658, 176, 590), t0 + 0.1, 0.55, KRE, 4.6, 1, "cizgi", 0.7)
    bal_ids.append("bal")
    pos = {}
    for sat, base in zip(satir, BASE):
        x = BX
        for i in sat:
            m = SOZ[6][i]["sozcuk"]
            w = Y.genislik("Caveat", 700, m, BF)
            s.yazi("bw%d" % i, x, base, [(m, KRE)], "Caveat", 700, BF, S(T(6, i)), 0.12,
                   tur="tik" if i in (0, 3, 6) else None)
            bal_ids.append("bw%d" % i)
            pos[i] = (x, w, base)
            x += w + sp
    xa, xb = pos[3][0], pos[4][0] + pos[4][1]
    s.yol("bm", Y.el_cizgi(xa - 2, BASE[1] + 14, xb + 2, BASE[1] + 11), S(T(6, 4)), 0.4, SAR, 10, 0.85, "cizgi", 0.5)
    bal_ids.append("bm")
    # ---------------- öneri: `has resigned + ago` (68,43), üstüne kırmızı çarpı (69,47) ----------------
    i0 = len(s.svg)
    tcl = S(T(6, 4))
    YF = 110
    s.yazi("cl1", 540 - Y.genislik("Fredoka", 700, "has resigned", YF) / 2, 980, [("has resigned", KRE)],
           "Fredoka", 700, YF, tcl, 0.4, tur="tik", guc=0.55)
    pw = Y.genislik("Fredoka", 700, "+ ago", YF)
    s.yazi("cl2", 540 - pw / 2, 1120, [("+ ", IKN), ("ago", KRE)], "Fredoka", 700, YF, tcl + 0.25, 0.3, tur=None)
    tx = S(T(6, 6))
    s.yol("xk1", "M260 830 Q540 980 830 1160", tx, 0.3, KIR, 14, 1, "cizgi", 0.7)
    s.yol("xk2", "M830 830 Q540 990 260 1160", tx + 0.3, 0.3, KIR, 14, 1, "cizgi", 0.7)
    s.olay(tx + 0.3, "vurus", 0.85)
    gcl = kimlikler(s, i0)
    # ---------------- künye: Question -> Form (71,06) ----------------
    tf0 = S(T(7, 0))
    s.to("#ku-bolum", tf0, {"opacity": 0, "duration": 0.2, "ease": "power1.in"})
    s.to("#ku-bolum2", tf0, {"opacity": 1, "duration": 0.2, "ease": "power1.out"})
    # balon + baş yukarı toplanır (ölçek 0,80: Caveat 57,6 px >= 56)
    s.to("#balg", tf0 + 0.25, {"svgOrigin": "48 372", "scale": 0.80, "opacity": 0.65, "duration": 0.7,
                               "ease": "power3.inOut"})
    # öneri bloğu ölçek 0,51 (Fredoka 56) ile Olmaz.'ın sağına taşınır; çarpı onunla gider
    s.to("#cl", tf0 + 0.3, {"svgOrigin": "540 980", "x": 250, "y": -310, "scale": 0.51, "duration": 0.7,
                            "ease": "power3.inOut"})
    # ---------------- Olmaz. (71,06, vuruş) ----------------
    s.svg.append('<g id="olm" font-family="Fredoka" font-weight="700" font-size="140" style="opacity:0">'
                 '<text x="48" y="738" fill="%s">Olmaz.</text></g>' % KIR)
    s.fromto("#olm", tf0, {"opacity": 0, "scale": 0.7, "svgOrigin": "48 738"},
             {"opacity": 1, "scale": 1, "duration": 0.35, "ease": "back.out(1.6)", "svgOrigin": "48 738"})
    s.olay(tf0, "vurus", 0.9)

    # ---------------- bölüm 1: kart (72,11–75,15) ----------------
    i0 = len(s.svg)
    s.yol("kart1", Y.el_kutu(48, 810, 984, 310), S(T(7, 1)) - 0.1, 0.6, KRE, 4.6, 1, "cizgi", 0.6)
    k1 = kelimeler(s, "kw", 88, 910, (1, 2, 3, 4), 7, "Fredoka", 700, 72)
    k2 = kelimeler(s, "kv", 88, 1005, (5, 6, 7), 7, "Fredoka", 700, 72, tur0=None)
    k3 = kelimeler(s, "kx", 88, 1100, (8,), 7, "Fredoka", 700, 72, tur0=None)
    s.yol("blk", Y.el_cizgi(k2[0][0] - 4, 1005 + 20, k2[0][0] + k2[0][1] + 4, 1005 + 18), S(T(7, 5)), 0.4, SAR, 10,
          0.9, "cizgi", 0.5)
    g1 = kimlikler(s, i0)
    C = (820, 880, 940, 1000)    # çip taban çizgileri (Fredoka 56)
    tc1 = S(T(7, 8)) + 0.45
    topla(s, "s1", tc1, 540, 965, 400, C[0] - 16, 0.35)
    s.yazi("c1", X0, C[0], [("definite time: ", KRE), ("no", KIR), (" Present Perfect", KRE)], "Fredoka", 700, 56,
           tc1 + 0.2, 0.4, tur="tik", guc=0.5)

    # ---------------- bölüm 2: sütunlar (75,56–83,12) ----------------
    i0 = len(s.svg)
    LF, LX = 80, X0
    RY = (980, 1080, 1180)
    sol = ((9, "ago"), (10, "last year"), (12, "in 1911"))
    for n, (i, m) in enumerate(sol):
        s.yazi("sl%d" % n, LX, RY[n], [(m, KRE)], "Fredoka", 700, LF, S(T(7, i)), 0.3, tur="tik", guc=0.55)
        w = Y.genislik("Fredoka", 700, m, LF)
        s.yol("st%d" % n, Y.tik_yolu(LX + w + 22, RY[n] - 52, 44), S(T(7, i)) + 0.3, 0.28, SAR, 9, 0.9, "cizgi", 0.5)
    tb_ = S(T(7, 14))
    nw_ = Y.genislik("Caveat", 700, "belirli zaman", 72)
    s.yazi("bz", LX, 1300, [("belirli zaman", SAR)], "Caveat", 700, 72, tb_, 0.6, tur="tik", guc=0.5)
    s.yol("bzu", Y.el_cizgi(LX - 4, 1318, LX + nw_ + 6, 1314), tb_ + 0.55, 0.35, SAR, 8, 0.9, "cizgi", 0.5)
    RX = 570.0
    tp = S(T(7, 16))
    s.yol("pk", Y.el_kutu(RX - 20, 900, 482, 92), tp, 0.5, KRE, 4.6, 1, "cizgi", 0.6)
    s.yazi("pt", RX, 962, [("Present Perfect", SAR)], "Fredoka", 700, 56, tp + 0.2, 0.4, tur="tik", guc=0.55)
    for n, (i, m) in enumerate(((18, "for"), (19, "since"), (20, "yet"))):
        s.yazi("sr%d" % n, RX, (1100, 1200, 1300)[n], [(m, KRE)], "Fredoka", 700, LF, S(T(7, i)), 0.3, tur="tik",
               guc=0.55)
        w = Y.genislik("Fredoka", 700, m, LF)
        s.yol("sq%d" % n, Y.tik_yolu(RX + w + 22, (1100, 1200, 1300)[n] - 52, 44), S(T(7, i)) + 0.3, 0.28, SAR, 9,
              0.9, "cizgi", 0.5)
    g2 = kimlikler(s, i0)
    tc2 = S(83.62)
    topla(s, "s2", tc2, 540, 1140, 400, C[1] - 16, 0.3)
    s.yazi("c2", X0, C[1], [("ago · last year · in 1911 = ", KRE), ("Past", SAR)], "Fredoka", 700, 56, tc2 + 0.2,
           0.3, tur="tik", guc=0.5)
    s.yazi("c3", X0, C[2], [("for · since · yet = ", KRE), ("Perfect", SAR)], "Fredoka", 700, 56, tc2 + 0.3, 0.3,
           tur=None)

    # ---------------- bölüm 3: Did not resign. (83,97–85,2) ----------------
    i0 = len(s.svg)
    DF = 110
    dw = Y.genislik("Fredoka", 700, "Did ", DF)
    nw2 = Y.genislik("Fredoka", 700, "not ", DF)
    tw3 = Y.genislik("Fredoka", 700, "Did not resign.", DF)
    dx0 = 540 - tw3 / 2
    s.yazi("dd0", dx0, 1150, [("Did", SAR)], "Fredoka", 700, DF, S(T(7, 22)), 0.3, tur="tik", guc=0.6)
    s.yazi("dd1", dx0 + dw, 1150, [("not", KRE)], "Fredoka", 700, DF, S(T(7, 23)), 0.25, tur=None)
    s.yazi("dd2", dx0 + dw + nw2, 1150, [("resign.", KRE)], "Fredoka", 700, DF, S(T(7, 24)), 0.3, tur="tik", guc=0.55)
    g3 = kimlikler(s, i0)
    tc3 = S(85.45)
    topla(s, "s3", tc3, 540, 1120, 300, C[3] - 16, 0.3)
    s.yazi("c4", X0, C[3], [("Did", SAR), (" not resign.", KRE)], "Fredoka", 700, 56, tc3 + 0.2, 0.3, tur="tik",
           guc=0.5)

    # ---------------- bölüm 4: Kod: ago → Past, since → Perfect (85,90–90,54) ----------------
    tk = S(T(7, 25))
    s.yazi("kod", X0, 1078, [("Kod:", KRE)], "Caveat", 700, 72, tk, 0.4, tur="tik")
    KF = 110
    for n, (a, ai, b, bi, y) in enumerate((("ago", 26, "Past", 28, 1178), ("since", 29, "Perfect", 31, 1280))):
        aw = Y.genislik("Fredoka", 700, a, KF)
        ta = S(T(7, ai))
        s.yazi("ka%d" % n, X0, y, [(a, KRE)], "Fredoka", 700, KF, ta, 0.35, tur="tik", guc=0.6)
        ox = X0 + aw + 30
        s.yol("ko%d" % n, Y.el_ok(ox, y - 40, ox + 150, y - 40, 2.0 + n), ta + 0.45, 0.35, SAR, 10, 0.95, "cizgi", 0.55)
        s.yazi("kb%d" % n, ox + 150 + 34, y, [(b, SAR)], "Fredoka", 700, KF, S(T(7, bi)), 0.35, tur="tik", guc=0.6)
    # formül kartı toplanır (90,54) + Next lesson
    tf = S(T1(7, 31))
    CX, CY, CW, CH = X0, 1308, 520, 80
    s.yol("kart", Y.el_kutu(CX, CY, CW, CH), tf, 0.5, KRE, 5, 1, "cizgi", 0.7)
    parc = [("V2", SAR), (" · ", IKN), ("did + V1", KRE)]
    tw = sum(Y.genislik("Fredoka", 700, p[0], 56) for p in parc)
    cx0 = CX + (CW - tw - 56) / 2
    s.yazi("cf1", cx0, CY + 58, parc, "Fredoka", 700, 56, tf + 0.1, 0.4, tur="tik", guc=0.6)
    s.yol("ctk", Y.tik_yolu(CX + CW - 62, CY + 20, 38), tf + 0.7, 0.3, SAR, 9, 0.9, "cizgi", 0.55)
    s.olay(tf + 0.7, "vurus", 0.8)
    nw = Y.genislik("Lexend", 700, "Next lesson", 56)
    tn2 = tf + 0.6
    s.yazi("nx", 962 - nw, 1366, [("Next lesson", KRE)], "Lexend", 700, 56, tn2, 0.3, tur="tik", guc=0.4)
    s.yol("nxok", "M980 1348 L1024 1348 M1010 1336 L1024 1348 L1010 1360", tn2 + 0.3,
          0.25, KRE, 4.6, 1, "cizgi", 0.4)
    # ---------------- altyazı: konuşulan parça ----------------
    parcalar = [{"id": "alt%d" % i, "metin": a["metin"]} for i, a in enumerate(ALT)]
    for i, a in enumerate(ALT):
        ac = S(a["t0"]) - 0.05
        kapa = S(a["t1"]) + 0.35
        if i + 1 < len(ALT):
            kapa = min(kapa, S(ALT[i + 1]["t0"]) - 0.05)
        s.set("#alt%d" % i, max(0.0, ac), {"opacity": 1})
        if i + 1 < len(ALT):
            s.set("#alt%d" % i, kapa, {"opacity": 0})
    kun = Y.kunye_svg("Question", "Form")
    return s, {"kun": kun, "bal_ids": bal_ids, "gruplar": [("cl", gcl), ("s1", g1), ("s2", g2), ("s3", g3)],
               "altyazi": Y.altyazi_svg(parcalar)}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    logo = (48, 48, 96 * Y.LOGO_EN_BOY, 96)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, round(Z["kare"] / 30, 4), parca["kun"], None, logo, ek=parca["altyazi"],
               bal_ids=parca["bal_ids"], vin=1150, gruplar=parca["gruplar"]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

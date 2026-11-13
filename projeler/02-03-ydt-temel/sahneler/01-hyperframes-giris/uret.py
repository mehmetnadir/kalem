"""Sahne 01 index.html üretici (02-03 YDT temel; soğuk açılış, 3 sn içerik + 12 kare geçiş payı = 102 kare).
Zaman: ../../zaman.json (t_bas, kare) + ortak/anlatim/sozcukler.json (cümle 1; küresel sn = yerel sn, t_bas 0).
Kapak kalıbı (02-03-ydt-ileri/01 ile aynı): logo damgası, rozet hapları, iki satır başlık sözcük sözcük (ONE VERB /
TWO TENSES), sağda `goes` ve `is going` iki kart kalemle, sonda başlık ve logo künyeye uçar.
`SIGNAL WORD` ("sinyal" 3,72 sn) sahne 02'de söylenir; bu sahnede yok (söylenmeden önce gelmez)."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text()) if w["cumle"] == 1]
R = Y.RENK
KRE, IKN, SAR, ZEM = R["murekkep"], R["ikincil"], R["vurgu"], R["zemin"]
SOL = 96
BOY = 140
T1_Y, T2_Y = 380, 530
ROZET_Y, ROZET_H = 150, 48
LOGO_H = 110
LOGO_W = LOGO_H * Y.LOGO_EN_BOY
LOGO_BX, LOGO_BY = SOL - Y.LOGO_KAYMA * LOGO_W, 880.0
UCUS = (2.5, 0.5)          # başlık + logo künyeye uçar (bitiş 3,00 sn)
CX, CW, CH = 1160, 620, 200            # kart x, genişlik, yükseklik
CY = (310, 570)                        # kart üst kenarları (goes, is going)
CFS = 100                              # kart yazı boyu
STIL = 'stroke="%s" stroke-width="10" stroke-linejoin="round" style="paint-order:stroke fill"' % ZEM


def T(i):
    """Cümle 1, i. sözcüğün t0'ı (küresel = yerel sn)."""
    return SOZ[i]["t0"]


def uret():
    s = Y.Sahne(Z["t_bas"])
    ids = {"eskiz": set(), "t1": set(), "t2": set()}
    # ---- rozetler (0,30 / 0,40) ----
    x = SOL
    for i, (m, dolgu) in enumerate((("YDT · BASIC", SAR), ("GRAMMAR", KRE))):
        w = Y.genislik("Lexend", 700, m, 26) + 44
        s.svg.append('<g id="rz%d" style="opacity:0"><rect x="%.1f" y="%d" width="%.1f" height="%d" rx="24" fill="%s"/>'
                     '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" font-weight="700" '
                     'font-size="26" fill="%s">%s</text></g>'
                     % (i, x, ROZET_Y, w, ROZET_H, dolgu, x + w / 2, ROZET_Y + ROZET_H / 2 + 9.1, ZEM, m))
        s.fromto("#rz%d" % i, 0.30 + 0.10 * i, {"y": 26, "opacity": 0},
                 {"y": 0, "opacity": 1, "duration": 0.4, "ease": "power3.out"})
        s.olay(0.30 + 0.10 * i, "tik", 0.4)
        x += w + 12
    # ---- eskiz: iki kart (goes / is going), kalemle; kart yazısı söylenen sözcükle gelir ----
    for k, (ad, m, ti, renk) in enumerate((("A", "goes", T(1), KRE), ("B", "is going", T(2), KRE))):
        bt = 0.20 + 0.65 * k
        s.yol("c" + ad, Y.el_kutu(CX, CY[k], CW, CH), bt, 0.6, KRE, 4.5, 1, "cizgi", 0.6)
        ids["eskiz"].add("c" + ad)
        fw = Y.genislik("Fredoka", 700, m, CFS)
        assert fw <= CW - 80, (m, fw)
        s.yazi("t" + ad, CX + (CW - fw) / 2, CY[k] + CH / 2 + CFS * 0.36, [(m, renk)], "Fredoka", 700, CFS, ti, 0.3,
               tur="tik", guc=0.55)
        ids["eskiz"].add("t" + ad)
    # sarı belirteç: ikinci kartta "going" söylenen "zaman" sözcüğünde (2,28 sn)
    gw0 = Y.genislik("Fredoka", 700, "is ", CFS)
    gw1 = Y.genislik("Fredoka", 700, "is going", CFS)
    bx0 = CX + (CW - gw1) / 2 + gw0
    s.yol("mk", Y.el_cizgi(bx0, CY[1] + CH / 2 + CFS * 0.36 + 16, CX + (CW + gw1) / 2, CY[1] + CH / 2 + CFS * 0.36 + 15,
                           1), T(3), 0.35, SAR, 10, 0.85, "cizgi", 0.5)
    ids["eskiz"].add("mk")
    # ---- başlık: satır 1 sözcükler konuşmayla (Aynı 1,00 · fiil 1,40), satır 2 (iki 2,04 · zaman 2,28) ----
    w_one = Y.genislik("Fredoka", 700, "ONE ", BOY)
    w_two = Y.genislik("Fredoka", 700, "TWO ", BOY)
    plan = (("w1a", "t1", "ONE", SOL, T1_Y, KRE, T(0), 0.30),
            ("w1b", "t1", "VERB", SOL + w_one, T1_Y, SAR, T(1), 0.45),
            ("w2a", "t2", "TWO", SOL, T2_Y, KRE, T(2), 0.25),
            ("w2b", "t2", "TENSES", SOL + w_two, T2_Y, SAR, T(3), 0.45))
    for kim, grup, m, px, py, renk, t, d in plan:
        s.yazi(kim, px, py, [(m, renk)], "Fredoka", 700, BOY, t, d, tur="tik", guc=0.55, sar_ek=STIL)
        ids[grup].add(kim)
    assert SOL + w_two + Y.genislik("Fredoka", 700, "TENSES", BOY) < CX - 40, "başlık karta değiyor"
    # ---- logo damgası 0,00-0,40 ----
    s.set("#logoimg", 0.0, {"svgOrigin": "%.1f %.1f" % (LOGO_BX + LOGO_W / 2, LOGO_BY + LOGO_H / 2)})
    s.fromto("#logoimg", 0.0, {"opacity": 0, "scale": 1.18, "rotation": -2},
             {"opacity": 1, "scale": 1, "rotation": 0, "duration": 0.4, "ease": "power3.out"})
    s.olay(0.05, "vurus", 0.9)
    # ---- uçuş 2,50-3,00: başlık, logo künyeye; eskiz ve rozet söner; künye açılır ----
    u0, ud = UCUS
    ders_w = Y.genislik("Fredoka", 700, "ONE VERB ", 30)
    hedef = {"t1": (56, 72, 30 / BOY, SOL, T1_Y), "t2": (56 + ders_w, 72, 30 / BOY, SOL, T2_Y)}
    for g, (hx, hy, hs, ox, oy) in hedef.items():
        s.to("#" + g, u0, {"svgOrigin": "%d %d" % (ox, oy), "x": hx - ox, "duration": ud, "ease": "power3.inOut"})
        s.to("#" + g, u0, {"svgOrigin": "%d %d" % (ox, oy), "y": hy - oy, "duration": ud, "ease": "power3.inOut"})
        s.to("#" + g, u0, {"svgOrigin": "%d %d" % (ox, oy), "scale": hs, "duration": ud * 0.8, "ease": "power3.out"})
        s.to("#" + g, u0 + ud - 0.25, {"opacity": 0, "duration": 0.25, "ease": "power1.in"})
    s.set("#logo", 0.0, {"svgOrigin": "%.1f %.1f" % (LOGO_BX, LOGO_BY)})
    s.to("#logo", u0, {"x": 56 - LOGO_BX, "y": 1002 - LOGO_BY, "scale": 34 / LOGO_H, "duration": ud,
                       "ease": "power3.inOut"})
    s.to("#eskiz", u0, {"opacity": 0, "scale": 1.06, "svgOrigin": "1470 540", "duration": 0.4, "ease": "power1.in"})
    for i in (0, 1):
        s.to("#rz%d" % i, u0 + 0.04 * i, {"opacity": 0, "duration": 0.3, "ease": "power1.in"})
    s.to("#ku-ders,#ku-bolum,#ku-ajanda,#ku-nokta", u0 + ud - 0.25, {"opacity": 1, "duration": 0.25,
                                                                     "ease": "power1.out"})
    s.olay(u0, "parilti", 0.5)
    s.olay(u0 + ud - 1 / 30, "tik", 0.5)
    gruplar = [("eskiz", ids["eskiz"]), ("t1", ids["t1"]), ("t2", ids["t2"])]
    kun = Y.kunye_svg("Hook", 0, gizli=True)
    Y.kontrol(s, Z["kare"], ilk=False)
    return s, kun, gruplar


if __name__ == "__main__":
    s, kun, gruplar = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (LOGO_BX, LOGO_BY, LOGO_W, LOGO_H), gruplar=gruplar))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

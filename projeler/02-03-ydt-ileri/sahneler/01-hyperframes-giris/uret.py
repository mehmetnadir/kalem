"""Sahne 01 index.html üretici (02-03 YDT ileri; soğuk açılış, 3 sn içerik + 12 kare geçiş payı = 102 kare).
Zaman: sozcukler.json (cümle 1, küresel sn = yerel sn çünkü t_bas 0) + aşağıdaki sabitler. olay.py aynı Sahne nesnesini kullanır.
Kapak kalıbı: logo damgası, rozet hapları, iki satır başlık kalemle açılır, çizim eskizi (bavul + uçak) sağda, sonda künyeye uçuş."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

Z = json.loads((AD / "zamanlar.json").read_text())
SOZ = [w for w in json.loads((AD / ".." / ".." / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == 1]
R = Y.RENK
KRE, IKN, SAR, ZEM = R["murekkep"], R["ikincil"], R["vurgu"], R["zemin"]
SOL = 96
BOY = 140
T1_Y, T2_Y = 380, 530
ROZET_Y, ROZET_H = 150, 48
LOGO_H = 110
LOGO_W = LOGO_H * Y.LOGO_EN_BOY
LOGO_BX, LOGO_BY = SOL - Y.LOGO_KAYMA * LOGO_W, 880.0
BAVUL = ("M12 34 Q12 26 20 26 L80 26 Q88 26 88 34 L88 82 Q88 90 80 90 L20 90 Q12 90 12 82 Z",
         "M38 26 L38 14 Q38 8 44 8 L56 8 Q62 8 62 14 L62 26",
         "M30 32 L30 84 M70 32 L70 84 M44 58 L56 58")
STIL = 'stroke="%s" stroke-width="10" stroke-linejoin="round" style="paint-order:stroke fill"' % ZEM


def uret():
    s = Y.Sahne(Z["t_bas"])
    ids = {"eskiz": set(), "t1": set(), "t2": set()}
    # ---- rozetler (0,30 / 0,40) ----
    x = SOL
    for i, (m, dolgu) in enumerate((("YDT · ADVANCED", SAR), ("GRAMMAR", KRE))):
        w = Y.genislik("Lexend", 700, m, 26) + 44
        s.svg.append('<g id="rz%d" style="opacity:0"><rect x="%.1f" y="%d" width="%.1f" height="%d" rx="24" fill="%s"/>'
                     '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Lexend" font-weight="700" '
                     'font-size="26" fill="%s">%s</text></g>'
                     % (i, x, ROZET_Y, w, ROZET_H, dolgu, x + w / 2, ROZET_Y + ROZET_H / 2 + 9.1, ZEM, m))
        s.fromto("#rz%d" % i, 0.30 + 0.10 * i, {"y": 26, "opacity": 0},
                 {"y": 0, "opacity": 1, "duration": 0.4, "ease": "power3.out"})
        s.olay(0.30 + 0.10 * i, "tik", 0.4)
        x += w + 12
    # ---- eskiz: bavul (kişisel plan) + uçak (tarife), kalemle ----
    bt = 0.20
    for i, (d, sure) in enumerate(zip(BAVUL, (0.5, 0.2, 0.25))):
        s.yol("bv%d" % i, d, bt, sure, KRE, 1.2, 1, "cizgi", 0.6,
              'transform="translate(1130 400) scale(3)"')
        ids["eskiz"].add("bv%d" % i)
        bt += sure
    ucak = Y.tabler("plane")
    ut = 1.10
    for i, d in enumerate(ucak):
        s.yol("uc%d" % i, d, ut, 0.7 / len(ucak), KRE, 0.3, 1, "cizgi", 0.6,
              'transform="translate(1480 400) scale(12)"')
        ids["eskiz"].add("uc%d" % i)
        ut += 0.7 / len(ucak)
    # ---- başlık: satır 1 sözcükler konuşmayla (İki 1,00 · gelecek 1,80), satır 2 hemen ardından ----
    w_two = Y.genislik("Fredoka", 700, "TWO ", BOY)
    plan = (("w1a", "t1", "TWO", SOL, T1_Y, KRE, SOZ[0]["t0"], 0.30),
            ("w1b", "t1", "FUTURES", SOL + w_two, T1_Y, SAR, SOZ[1]["t0"], 0.60),
            ("w2a", "t2", "TWO", SOL, T2_Y, KRE, SOZ[2]["t0"] - 0.10, 0.14),
            ("w2b", "t2", "TENSES", SOL + w_two, T2_Y, SAR, SOZ[2]["t0"] + 0.02, 0.12))
    for kim, grup, m, px, py, renk, t, d in plan:
        s.yazi(kim, px, py, [(m, renk)], "Fredoka", 700, BOY, t, d, tur="tik", guc=0.55, sar_ek=STIL)
        ids[grup].add(kim)
    # ---- logo damgası 0,00-0,40 ----
    s.set("#logoimg", 0.0, {"svgOrigin": "%.1f %.1f" % (LOGO_BX + LOGO_W / 2, LOGO_BY + LOGO_H / 2)})
    s.fromto("#logoimg", 0.0, {"opacity": 0, "scale": 1.18, "rotation": -2},
             {"opacity": 1, "scale": 1, "rotation": 0, "duration": 0.4, "ease": "power3.out"})
    s.olay(0.05, "vurus", 0.9)
    # ---- 2,50-3,00: uçuş yok (BRIEF "künyeye uçuş" 3,00 sn tavanına sığmaz: cümle 1'in ikinci yarısı 2,84'te
    # başlar, sahne 3,00'da biter). Eskiz ve rozet 2,70-3,00 arası yumuşakça söner; başlık ve logo yerinde kalır. ----
    s.to("#eskiz", 2.60, {"opacity": 0, "duration": 0.3, "ease": "power1.in"})
    for i in (0, 1):
        s.to("#rz%d" % i, 2.60 + 0.04 * i, {"opacity": 0, "duration": 0.26, "ease": "power1.in"})
    s.olay(2.60, "parilti", 0.5)
    gruplar = [("eskiz", ids["eskiz"]), ("t1", ids["t1"]), ("t2", ids["t2"])]
    kun = ""   # künye sahne 02'de başlar
    return s, kun, gruplar


if __name__ == "__main__":
    s, kun, gruplar = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (LOGO_BX, LOGO_BY, LOGO_W, LOGO_H), gruplar=gruplar))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

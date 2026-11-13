"""Sahne 06 — Soru anı 1 (02-03 YDT temel, HyperFrames, 1920x1080; cümle 6 öğrenci, cümle 7 öğretmen).
yanılgı: değişen durum (harder and harder) genel gerçek sanılır → «Neden -ing?».
Akış (soru-ani.md): öğrenci sorusu (balon + ogrenci-bas.svg, sözcük sözcük) → 0,75 sn duraklama (ses dosyasında)
→ öğretmen cevabı + görsel karşılık: «CHANGING → mostly -ing»; üç örnek kartı sağ köşede küçülüp üst üste durur.
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (sapma ≤ 0,15 sn). Yerel sn = küresel - t_bas. İlk ve son 12 kare durgun.
Renkler yalnız kalem paleti (tema çevirisi hf_tema.py); kırmızı YOK."""
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
S6 = [w for w in _ham if w["cumle"] == 6]    # öğrenci sorusu
S7 = [w for w in _ham if w["cumle"] == 7]    # öğretmen cevabı
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]

# ---- büyük kart (örnek 3; sahne 05'in son hâliyle aynı cümle) ----
CX, CY, CW, CH = 96, 170, 1728, 250
SATIR = "It is getting harder and harder to find a good job nowadays."
ON, FRAZ, ORTA, SON = "It is getting ", "harder and harder", " to find a good job ", "nowadays."
# ---- sağ köşe yığını: üç mini kart ----
MX, MW, MH = 1204, 620, 160
MY = (220, 408, 596)                  # örnek 1, 2, 3
MINI = [("PLAN", [("are ", KRE), ("leaving", KRE), (" · at 9", IKN)], 1),
        ("PERIOD", [("is ", KRE), ("going", KRE), (" · these days", IKN)], 1),
        ("CHANGING", [("is ", KRE), ("getting", KRE), (" · harder and harder", IKN)], 1)]
MF = 36                               # mini kart yazı boyu
# ---- cevap kartı (sol) ----
AX, AY, AW, AH = 96, 440, 1000, 250


def T6(i: int) -> float:
    return S6[i]["t0"]


def T7(i: int) -> float:
    return S7[i]["t0"]


def g(m: str, boy: int, agr: int = 700, aile: str = "Fredoka") -> float:
    return Y.genislik(aile, agr, m, boy)


def kunye(bolum: str, etkin: int) -> str:
    """Künye (ortak/kunye.js KUNYE ile aynı): ders + seviye (sol üst), bölüm (sağ üst), ajanda (sağ alt)."""
    ad = ["Hook", "Examples", "Rule", "Trap"]
    x, yer = Y.W - 56.0, {}
    for a in reversed(ad):
        w = g(a, 20, 500, "Lexend")
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


def statik(kim: str, d: str, renk: str, w: float, alfa: float = 1.0) -> str:
    return ('<path id="%s" d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
            'stroke-linejoin="round" opacity="%s"/>' % (kim, d, renk, w, alfa))


def uret() -> tuple:
    s = Y.Sahne(TB)
    S = s.S
    bal_ids: list[str] = []
    big_ids: set[str] = set()

    # ================= büyük kart: statik (sahne 05'ten gelen son görünüm), ilk kareden görünür =================
    FB = 56
    while g(SATIR, FB) > CW - 120:
        FB -= 2
    base = CY + 170
    x0 = CX + 44
    xf = x0 + g(ON, FB)                              # «harder and harder» başı
    wf = g(FRAZ, FB)
    xs = x0 + g(ON + FRAZ + ORTA, FB)                # «nowadays.» başı
    ws = g(SON, FB)
    s.svg.append(statik("bigk", Y.el_kutu(CX, CY, CW, CH), KRE, 4.5))
    s.svg.append('<g id="bigt" font-family="Fredoka" font-weight="700" font-size="%d" fill="%s">'
                 '<text x="%.1f" y="%d" xml:space="preserve">%s</text></g>' % (FB, KRE, x0, base, SATIR))
    s.svg.append(statik("bigm", Y.el_cizgi(xf - 4, base + 14, xf + wf + 4, base + 13, 1), SAR, 9, 0.85))
    s.svg.append(statik("bigc", Y.el_cizgi(xs - 2, base + 14, xs + ws + 2, base + 13, 1), SAR, 9, 0.85))
    big_ids |= {"bigk", "bigt", "bigm", "bigc"}

    # ================= soru anı: öğrenci başı + balon (069,11 «Hocam,») =================
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    BS, BTX, BTY = 0.6, 128.0, 540.0
    s.svg.append('<g id="bas" transform="translate(%.1f %.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="%.2f" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (BTX, BTY, BS, KRE, 2.8 / BS, "".join(
                     '<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    t0 = 0.43                                        # ilk 12 kare (0,4 sn) durgun
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(t0 + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t0 + 0.05 * i, "cizgi", 0.55)
    BF, BX0, BY0 = 44, 340.0, 540.0
    sp = g(" ", BF, 600)
    satir = ((0, 1, 2, 3, 4), (5, 6, 7, 8))          # Hocam, zorlaşmak genel bir durum / değil mi? Neden -ing?
    gens = [sum(g(S6[i]["sozcuk"], BF, 600) for i in sat) + sp * (len(sat) - 1) for sat in satir]
    x1b = BX0 + max(gens) + 70
    assert x1b < 1880, "balon taştı: %.0f" % x1b
    BASE = (BY0 + 72, BY0 + 136)
    s.yol("bal", Y.balon_sol(BX0, BY0, x1b, BY0 + 190, BX0 - 78, BY0 + 118), S(T6(0)) - 0.05, 0.55, KRE, 4.2, 1,
          "cizgi", 0.7)
    bal_ids.append("bal")
    pos: dict[int, tuple[float, float, float]] = {}
    for sat, bs in zip(satir, BASE):
        x = BX0 + 35
        for i in sat:
            m = S6[i]["sozcuk"]
            w = g(m, BF, 600)
            s.yazi("bw%d" % i, x, bs, [(m, KRE)], "Fredoka", 600, BF, S(S6[i]["t0"]), 0.12,
                   tur="tik" if i in (0, 5) else None)
            bal_ids.append("bw%d" % i)
            pos[i] = (x, w, bs)
            x += w + sp
    x8, w8, b8 = pos[8]                              # «-ing?» sarı belirteç (yanılgının odağı)
    s.yol("bm8", Y.el_cizgi(x8 - 2, b8 + 12, x8 + w8 + 2, b8 + 9, 1), S(T6(8)), 0.28, SAR, 8, 0.85, "cizgi", 0.5)
    bal_ids.append("bm8")
    # sarı nokta (069,91 «zorlaşmak»): balondan kartın «harder and harder» satırına bağlanır
    xd = xf + wf / 2
    td = S(T6(1))
    s.yol("nk", "M%.1f %.1f L%.1f %.1f" % (xd, BY0 - 8, xd + 0.1, BY0 - 8), td, 0.12, SAR, 18, 1, "tik", 0.45)
    s.yol("cn", Y.el_cizgi(xd, BY0 - 20, xd, base + 30, 2), td + 0.14, 0.45, SAR, 5, 0.9, "cizgi", 0.45)
    bal_ids += ["nk", "cn"]

    # ================= öğretmen cevabı (074,02): balon + baş söner =================
    th = S(T7(0))
    s.to("#balg", th, {"opacity": 0, "duration": 0.4, "ease": "power2.in"})
    s.olay(th, "vurus", 0.5)
    # 074,90 «değişiyor.»: «harder and harder» üstünde kalemle yükselen ok
    s.yol("bok", Y.el_ok(xf + 20, base - 62, xf + wf - 10, base - 112, 1), S(T7(2)), 0.5, SAR, 8, 0.9, "cizgi", 0.55)
    big_ids.add("bok")
    # 077,14 «değişimde.»: «süren değişim» — fraz üstüne sarı halka
    # (13.11 QA: ikinci altçizgi kaldırıldı, fraz zaten altı çizili) s.yol("bdr", Y.el_cizgi(xf - 4, base + 30, xf + wf + 4, base + 29, 1), S(T7(5)), 0.5, SAR, 7, 0.85, "cizgi", 0.5)   # halka yerine altçizgi (13.11 QA)
    big_ids.add("bdr")

    # ================= cevap kartı: CHANGING → mostly -ing =================
    AF = 64
    bs = AY + 150
    w1, w2, w3 = g("CHANGING", AF), g("mostly ", AF), g("-ing", AF)
    ok_u = 100
    tx0 = AX + (AW - (w1 + 40 + ok_u + 40 + w2 + w3)) / 2
    s.yol("ak", Y.el_kutu(AX, AY, AW, AH), S(T7(5)) + 0.3, 0.55, KRE, 4.5, 1, "cizgi", 0.7)
    s.yazi("a1", tx0, bs, [("CHANGING", KRE)], "Fredoka", 700, AF, S(T7(6)), 0.35, tur="tik", guc=0.55)
    xo = tx0 + w1 + 40
    s.yol("aok", Y.el_ok(xo, bs - 22, xo + ok_u, bs - 22, 2), S(T7(8)), 0.3, SAR, 8, 0.95, "cizgi", 0.55)
    x2 = xo + ok_u + 40
    s.yazi("a2", x2, bs, [("mostly ", KRE)], "Fredoka", 700, AF, S(T7(8)) + 0.12, 0.35, tur="tik", guc=0.5)
    x3 = x2 + w2
    s.yazi("a3", x3, bs, [("-ing", SAR)], "Fredoka", 700, AF, S(T7(9)), 0.3, tur="tik", guc=0.6)
    s.yol("am", Y.el_cizgi(x3 - 4, bs + 16, x3 + w3 + 4, bs + 15, 1), S(T7(10)), 0.35, SAR, 9, 0.85, "cizgi", 0.5)
    s.olay(S(T7(10)) + 0.3, "vurus", 0.7)

    # ================= 081,30 «Üç örnekte…»: büyük kart sağ köşede küçülür, üç mini kart üst üste =================
    t_kuc = S(T7(12))
    s.to("#big", t_kuc, {"scale": 0.34, "svgOrigin": "%d %d" % (CX + CW, CY), "duration": 0.4, "ease": "power3.inOut"})
    s.to("#big", t_kuc + 0.45, {"y": MY[2] - CY, "duration": 0.4, "ease": "power3.inOut"})
    s.olay(t_kuc, "vurus", 0.5)
    s.to("#big", t_kuc + 0.85, {"opacity": 0, "duration": 0.15})
    gelis = (t_kuc + 0.85, t_kuc + 1.05, t_kuc + 1.3)   # C önce (küçülen kart yerini alır), sonra A, B
    sira = (2, 0, 1)
    chip_t = (S(T7(18)), S(T7(19)), S(T7(20)))          # plan, dönem, değişim
    mini_pos = {}
    for k in sira:
        etiket, parcalar, _ = MINI[k]
        y = MY[k]
        tg = gelis[sira.index(k)]
        genis = sum(g(m, MF) for m, _r in parcalar)
        assert genis <= MW - 56, "mini kart taştı: %s %.0f" % (etiket, genis)
        s.yol("mk%d" % k, Y.el_kutu(MX, y, MW, MH), tg, 0.45, IKN, 3.6, 0.95, "cizgi", 0.5)
        s.yazi("mt%d" % k, MX + 28, y + 70, parcalar, "Fredoka", 700, MF, tg + 0.15, 0.4, tur="tik", guc=0.45)
        s.yazi("mc%d" % k, MX + 28, y + 128, [(etiket, SAR)], "Lexend", 700, 30, chip_t[k], 0.3, tur="tik", guc=0.55)
        pre = g(parcalar[0][0], MF)
        mini_pos[k] = (MX + 28 + pre, g(parcalar[1][0], MF), y + 70)
    # 086,26 «şimdiki zamanı çağırıyor»: üç fiilde sarı halka (ipucu → -ing)
    for n, k in enumerate(range(3)):
        xv, wv, bv = mini_pos[k]
        s.yol("mh%d" % k, Y.el_cizgi(xv - 2, bv + 11, xv + wv + 2, bv + 10, 1), S(T7(22)) + 0.14 * n, 0.4, SAR,
              8, 0.9, "cizgi", 0.5)   # halka yerine el altçizgisi (13.11 QA: halka are/is'e değiyordu)

    return s, {"kun": kunye("Question", 1), "bal_ids": bal_ids, "big_ids": big_ids}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34), bal_ids=parca["bal_ids"],
               gruplar=[("big", parca["big_ids"])]))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

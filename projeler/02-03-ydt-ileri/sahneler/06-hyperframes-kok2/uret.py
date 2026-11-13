"""Sınav kökü sahnesi (HyperFrames, 1920x1080): kök kartı + 5 şıklı panel (sayaçsız).
Şablon: sahne başına veri = kok.json (kök simgeleri, boşluklar, işaretler, şıklar, çeldirici notları).
Zaman tek kaynak: ../../zaman.json (t_bas, kare) + ../../ortak/anlatim/sozcukler.json (küresel sn).
Olay zamanı = ilgili sözcüğün t0'ı (cümle içi sıra numarası `i`). Yerel sn = küresel - t_bas."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(s for s in json.loads((PAKET / "zaman.json").read_text())["sahneler"] if s["klasor"] == AD.name)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
K = json.loads((AD / "kok.json").read_text())
SOZ = [w for w in json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text())
       if w["cumle"] == K["cumle"]]
R = Y.RENK
KRE, IKN, SAR, KIR = R["murekkep"], R["ikincil"], R["vurgu"], R["kirmizi"]
YESIL, BEYAZ = SAR, "#1b1a17"   # yeşil token yok: doğru = vurgu; üstündeki yazı koyu (13.11 QA)
TB = Z["t_bas"]

# ---- yerleşim (px) ----
FS, LH = 56, 76                      # kök yazısı, satır aralığı
KX, KY, KW, KH = 96, 164, 1728, 278  # kök kartı
IX, IW = 140, 1640                   # kart içi yazı alanı
PY, RH, RHH = 470, 96, 84            # panel başı, satır adımı, satır yüksekliği
CHX, OPX = 146, 212                  # harf dairesi merkezi, şık metni x
PIX = 1010                           # çeldirici notu (pil) x
PIL_H = 56


def T(i):
    """Cümle içi i. sözcüğün t0'ı (küresel sn)."""
    return SOZ[i]["t0"]


def yerlestir():
    """Kök simgelerini satırlara dizer. Döner: (pos listesi, satır sayısı)."""
    sp = Y.genislik("Fredoka", 700, " ", FS)
    gen = []
    for t in K["kok"]:
        if "w" in t:
            gen.append(Y.genislik("Fredoka", 700, t["w"], FS))
        else:
            gen.append(Y.genislik("Fredoka", 700, K["bosluklar"][t["b"]]["dolgu"], FS) + 48)
    satirlar, cur, cw = [], [], 0.0
    for n, w in enumerate(gen):
        yeni = bool(cur) and cw + sp + w > IW
        if yeni:
            satirlar.append(cur)
            cur, cw = [], 0.0
        cw += (sp if cur else 0) + w
        cur.append(n)
        if n == K.get("kir_sonra"):
            satirlar.append(cur)
            cur, cw = [], 0.0
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
            'font-size="24" fill="%s">Items</text>'
            '<g id="ku-ajA"><text x="%d" y="1030" text-anchor="end" font-family="Lexend" font-weight="500" '
            'font-size="20">%s</text><circle cx="%.2f" cy="1023" r="4" fill="%s"/></g></g>'
            % (KRE, IKN, SAR, Y.W - 56, tsp, nk["x"] - 12, SAR))


def uret():
    s = Y.Sahne(TB)
    S = s.S
    pos, nsat = yerlestir()
    bos = [i for i, t in enumerate(K["kok"]) if "b" in t]   # boşluk -> simge sırası
    bpos = {K["kok"][i]["b"]: pos[i] for i in bos}
    t_kart = S(T(0))

    # ---------------- kök kartı ----------------
    s.yol("kart", Y.el_kutu(KX, KY, KW, KH), t_kart, 0.6, KRE, 4.5, 1, "cizgi", 0.7)
    et = "ROOT %d / 4" % K["no"]
    s.yazi("etiket", KX, 148, [(et, SAR)], "Lexend", 700, 32, t_kart + 0.15, 0.3, tur="tik", guc=0.45)
    for n, t in enumerate(K["kok"]):
        p = pos[n]
        if "w" in t:
            s.yazi("w%d" % n, p["x"], p["base"], [(t["w"], KRE)], "Fredoka", 700, FS, S(T(t["i"])), 0.14,
                   tur="tik" if n == 0 else None, guc=0.5)
    # boşluk çizgileri (söylendiği anda) + dolgu (açıklandığı anda)
    for b, bd in enumerate(K["bosluklar"]):
        p = bpos[b]
        s.yol("bl%d" % b, Y.el_cizgi(p["x"] + 4, p["base"] + 12, p["x"] + p["w"] - 4, p["base"] + 12, 2),
              S(T(bd["i_ciz"])), 0.3, IKN, 5, 1, "cizgi", 0.5)
    # ---------------- işaretler (belirteç, daire, boşluk vurgusu, yükselen ok) ----------------
    for m, isr in enumerate(K["isaretler"]):
        t = S(T(isr["i"]))
        if isr["tur"] == "belirtec":
            satir = {}
            for n in isr["tok"]:
                satir.setdefault(pos[n]["satir"], []).append(n)
            for li, ns in satir.items():
                x0 = pos[ns[0]]["x"] - 4
                x1 = pos[ns[-1]]["x"] + pos[ns[-1]]["w"] + 4
                s.yol("m%d_%d" % (m, li), Y.el_cizgi(x0, pos[ns[0]]["base"] + 14, x1, pos[ns[0]]["base"] + 13, 1),
                      t, 0.4, SAR, 9, 0.85, "cizgi", 0.5)
        elif isr["tur"] == "bosluk":
            p = bpos[isr["b"]]
            s.yol("m%d" % m, Y.el_cizgi(p["x"] + 2, p["base"] + 12, p["x"] + p["w"] - 2, p["base"] + 11, 1),
                  t, 0.35, SAR, 8, 0.9, "cizgi", 0.5)
        elif isr["tur"] == "daire":
            p = bpos[isr["b"]] if "b" in isr else pos[isr["tok"]]
            s.yol("m%d" % m, Y.el_daire(p["x"] + p["w"] / 2, p["base"] - 20, p["w"] / 2 - 6, 46, m * 0.7),
                  t, 0.45, SAR, 7, 0.85, "parilti", 0.5)
        elif isr["tur"] == "ok_yukari":
            p = pos[isr["tok"]]
            x0 = p["x"] + p["w"] + 48
            s.yol("m%d" % m, Y.el_ok(x0, p["base"] + 4, x0 + 160, p["base"] - 64, 1), t, 0.5, SAR, 9, 0.9,
                  "cizgi", 0.6)
    for b, bd in enumerate(K["bosluklar"]):
        p = bpos[b]
        fw = Y.genislik("Fredoka", 700, bd["dolgu"], FS)
        td = S(T(bd["i_doldur"]))
        s.yazi("fl%d" % b, p["x"] + (p["w"] - fw) / 2, p["base"], [(bd["dolgu"], KRE)], "Fredoka", 700, FS, td,
               0.3, tur="tik", guc=0.55)
        if bd.get("isaret") == "belirtec":
            s.yol("fm%d" % b, Y.el_cizgi(p["x"] + 6, p["base"] + 16, p["x"] + p["w"] - 6, p["base"] + 15, 1),
                  td + 0.2, 0.35, SAR, 9, 0.85, "cizgi", 0.5)
        elif bd.get("isaret") == "daire":
            s.yol("fm%d" % b, Y.el_daire(p["x"] + p["w"] / 2, p["base"] - 20, p["w"] / 2 - 6, 46, b * 0.9 + 0.4),
                  td + 0.2, 0.45, SAR, 7, 0.85, "parilti", 0.5)

    # ---------------- şık paneli ----------------
    harfler = "ABCDE"
    for k, h in enumerate(harfler):
        y0 = PY + k * RH
        cy = y0 + RHH / 2
        a, *b2 = K["sik"][h]
        metin = " / ".join([a] + b2)
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
    tp = S(T(K["panel_i"]))
    for k, h in enumerate(harfler):
        s.goster("#row" + h, tp + 0.09 * k, 0.35, 0, 24)
    s.olay(tp, "tik", 0.5)
    s.olay(tp + 0.2, "tik", 0.4)

    # ---------------- doğru şık: yeşil satır + onay işareti + boşlukta yeşil çizgi ----------------
    d = K["dogru"]
    td = S(T(d["i"]))
    kd = harfler.index(d["harf"])
    s.to("#gr" + d["harf"], td, {"opacity": 1, "duration": 0.3, "ease": "power2.out"})
    s.to("#row%s text" % d["harf"], td, {"fill": BEYAZ, "duration": 0.3})
    s.to("#row%s .chip" % d["harf"], td, {"stroke": BEYAZ, "duration": 0.3})
    s.yol("ck", Y.tik_yolu(KX + KW - 110, PY + kd * RH + 20, 44), td + 0.2, 0.3, KRE, 9, 1, "cizgi", 0.55)
    s.olay(td, "vurus", 0.85)
    for b in range(len(K["bosluklar"])):
        p = bpos[b]
        s.yol("gb%d" % b, Y.el_cizgi(p["x"] + 2, p["base"] + 12, p["x"] + p["w"] - 2, p["base"] + 11, 1),
              td + 0.35 + 0.25 * b, 0.35, YESIL, 8, 1, "cizgi", 0.5)

    # ---------------- çeldirici notları: imleç + sik_not pili ----------------
    onceki = None
    for nt in sorted(K["notlar"], key=lambda n: T(n["i_isaret"])):
        h = nt["harf"]
        k = harfler.index(h)
        y0 = PY + k * RH
        cy = y0 + RHH / 2
        ti = S(T(nt["i_isaret"]))
        s.yol("pt" + h, Y.el_ok(30, cy, 84, cy, 1), ti, 0.25, SAR, 7, 0.95, "tik", 0.45)
        if onceki:
            s.to("#pt" + onceki, ti, {"opacity": 0, "duration": 0.15})
        onceki = h
        tn = S(T(nt["i_not"])) + nt.get("gecikme", 0.0)
        pw = pil_olc(nt["parcalar"])
        assert PIX + pw <= KX + KW, "pil taştı: " + h
        g = ['<rect x="%d" y="%.1f" width="%.1f" height="%d" rx="28" fill="none" stroke="%s" stroke-width="3"/>'
             % (PIX, cy - PIL_H / 2, pw, PIL_H, IKN)]
        x = PIX + 22
        xx = None
        for n, p in enumerate(nt["parcalar"]):
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
    return s, {"kun": kunye(), "pos": pos, "nsat": nsat}


if __name__ == "__main__":
    s, parca = uret()
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], parca["kun"], None, (56, 1002, 34 * Y.LOGO_EN_BOY, 34)))
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "satır", parca["nsat"])

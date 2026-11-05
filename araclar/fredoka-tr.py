"""Fredoka latin-ext alt kümesine Türkçe harfleri ekler: Ş ş Ğ ğ İ.
Kaynak: fredoka-latin-<w>-normal.woff2 (S s G g I i ve uni0327 cedilla). Breve sentezlenir (yuvarlak uçlu yay).
Kullanım: uv run --no-project --with "fonttools[woff]" --python 3.12 araclar/fredoka-tr.py <font dizini> <çıktı dizini>
  → <çıktı>/fredoka-latin-ext-<w>-normal.woff2; sonra ortak/font ve her HyperFrames proje/assets/fonts/ kopyasına yazılır.
Gerekçe (05.11): Google Fredoka Türkçe Ş ş Ğ ğ İ içermez; S1 kapağında AKŞAM yedek fonta düşüyordu.
import math
import sys
from pathlib import Path

from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

KAYNAK, CIKTI = Path(sys.argv[1]), Path(sys.argv[2])
CIKTI.mkdir(parents=True, exist_ok=True)


def konturlar(gs, ad):
    rp = RecordingPen(); gs[ad].draw(rp)
    out, cur = [], []
    for op, a in rp.value:
        cur.append((op, a))
        if op in ("closePath", "endPath"): out.append(cur); cur = []
    return out


def bbox(konts):
    pts = [p for k in konts for op, a in k for p in a if p is not None]
    return min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts)


def ciz(pen, konts, dx=0, dy=0):
    tp = TransformPen(pen, (1, 0, 0, 1, dx, dy))
    for k in konts:
        for op, a in k: getattr(tp, op)(*a)


def yay(pen, cx, cy, r, a0, a1, adim=math.radians(30), ilk=True):
    """Merkez (cx,cy), yarıçap r, a0→a1 (radyan) çember yayı; quadratic parçalarla. ilk=True ise moveTo."""
    n = max(1, int(math.ceil(abs(a1 - a0) / adim - 1e-9)))
    for i in range(n):
        b0 = a0 + (a1 - a0) * i / n; b1 = a0 + (a1 - a0) * (i + 1) / n; bm = (b0 + b1) / 2
        p0 = (cx + r * math.cos(b0), cy + r * math.sin(b0))
        p1 = (cx + r / math.cos((b1 - b0) / 2) * math.cos(bm), cy + r / math.cos((b1 - b0) / 2) * math.sin(bm))
        p2 = (cx + r * math.cos(b1), cy + r * math.sin(b1))
        if ilk and i == 0: pen.moveTo(p0)
        pen.qCurveTo(p1, p2)


def breve(pen, cx, taban, genislik, kalinlik, alfa=math.radians(60)):
    """Alt kenarı 'taban' olan, 'genislik' geniş, yuvarlak uçlu yay (U). Merkez çizgisi yarıçapı Rc."""
    t2 = kalinlik / 2
    rc = (genislik - kalinlik) / (2 * math.sin(alfa))
    cy = taban + t2 + rc                              # merkez çizgisinin en alt noktası taban + t2
    tl, tr = -math.pi / 2 - alfa, -math.pi / 2 + alfa  # sol ve sağ uç açıları
    # dış yay sağdan sola (saat yönü), sol kapak, iç yay soldan sağa, sağ kapak
    yay(pen, cx, cy, rc + t2, tr, tl, ilk=True)
    el = (cx + rc * math.cos(tl), cy + rc * math.sin(tl))
    yay(pen, el[0], el[1], t2, tl, tl - math.pi, ilk=False)
    yay(pen, cx, cy, rc - t2, tl, tr, ilk=False)
    er = (cx + rc * math.cos(tr), cy + rc * math.sin(tr))
    yay(pen, er[0], er[1], t2, tr + math.pi, tr, ilk=False)
    pen.closePath()


for w in (600, 700):
    kay = TTFont(KAYNAK / f"fredoka-latin-{w}-normal.woff2")
    hedef = TTFont(KAYNAK / f"fredoka-latin-ext-{w}-normal.woff2")
    gs, hm = kay.getGlyphSet(), kay["hmtx"]
    K = {ad: konturlar(gs, ad) for ad in ("S", "s", "G", "g", "I", "i", "uni0327", "uni0304")}
    ced = bbox(K["uni0327"]); cedW = (ced[0] + ced[2]) / 2; cedTop = ced[3]
    mak = bbox(K["uni0304"]); kal = mak[3] - mak[1]; gen = (mak[2] - mak[0]) + kal * 0.3
    i_dot = [k for k in K["i"] if bbox([k])[1] > 520]; i_gov = [k for k in K["i"] if bbox([k])[1] <= 520]
    dotB = bbox(i_dot); govB = bbox(i_gov); bosluk = dotB[1] - govB[3]
    yeni = {}
    def ekle(ad, cp, taban, parca, dx=0, dy=0, ek=None):
        pen = TTGlyphPen(None)
        ciz(pen, K[taban])
        if parca: ciz(pen, parca, dx, dy)
        if ek: ek(pen)
        g = pen.glyph(); g.recalcBounds(kay["glyf"])
        yeni[ad] = (cp, g, hm[taban][0])
    S, s, G, g_, I = bbox(K["S"]), bbox(K["s"]), bbox(K["G"]), bbox(K["g"]), bbox(K["I"])
    ekle("Scedilla", 0x15E, "S", K["uni0327"], round((S[0] + S[2]) / 2 - cedW), S[1] + 59 - cedTop)
    ekle("scedilla", 0x15F, "s", K["uni0327"], round((s[0] + s[2]) / 2 - cedW), s[1] + 48 - cedTop)
    ekle("Idotaccent", 0x130, "I", i_dot, round((I[0] + I[2]) / 2 - (dotB[0] + dotB[2]) / 2), I[3] + bosluk - dotB[1])
    ekle("Gbreve", 0x11E, "G", None, ek=lambda p: breve(p, (G[0] + G[2]) / 2, G[3] + 44, gen, kal))
    ekle("gbreve", 0x11F, "g", None, ek=lambda p: breve(p, (g_[0] + g_[2]) / 2, g_[3] + 44, gen, kal))
    # hedefe yaz
    sira = hedef.getGlyphOrder()
    for ad, (cp, g, adv) in yeni.items():
        if ad in sira: continue
        sira.append(ad)
    hedef.setGlyphOrder(sira)
    for ad, (cp, g, adv) in yeni.items():
        hedef["glyf"][ad] = g; hedef["hmtx"][ad] = (adv, g.xMin)
        for st in hedef["cmap"].tables:
            if st.isUnicode(): st.cmap[cp] = ad
    hedef["maxp"].numGlyphs = len(sira)
    out = CIKTI / f"fredoka-latin-ext-{w}-normal.woff2"
    hedef.flavor = "woff2"; hedef.save(out)
    print(w, "kal", kal, "gen", round(gen), "dot boşluk", bosluk, "→", out.name, out.stat().st_size, "bayt")

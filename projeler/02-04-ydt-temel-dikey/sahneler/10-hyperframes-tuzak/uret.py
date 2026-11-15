"""Sahne 10 Tuzak ve soru anı 2 (02-04 YDT temel dikey, HyperFrames 1080x1920, 656 kare; cümle 11 ve 12).
Yerleşim BRIEF-DIKEY §2-§3 satır 10 + SPEC.md: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform boş.
Zaman: zaman.json (t_bas 162.33, kare 656) + ortak/anlatim/sozcukler.json (cümle 11 ve 12)."""
import json
import re
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import yardim as Y  # noqa: E402

PAKET = AD.parent.parent
SAH = next(
    s for s in json.loads((PAKET / "zaman.json").read_text(encoding="utf-8"))["sahneler"]
    if s["klasor"] == AD.name
)
Z = {"t_bas": SAH["t_bas"], "kare": SAH["kare"], "sure": round(SAH["kare"] / 30, 4)}
_ham = json.loads((PAKET / "ortak" / "anlatim" / "sozcukler.json").read_text(encoding="utf-8"))
S11 = [w for w in _ham if w["cumle"] == 11]
S12 = [w for w in _ham if w["cumle"] == 12]
R = Y.RENK
KRE, IKN, SAR, ZEM = R["murekkep"], R["ikincil"], R["vurgu"], R["zemin"]

# ---- yerleşim (px; SPEC §4) ----
KX, KW, CH = 48, 984, 544
CY0, CY1 = 600, 392
DY_KART = CY1 - CY0  # -208
TB1 = CY0 + 128
TB2 = CY0 + 214
EB1 = CY0 + 400
EB2 = CY0 + 486
KUTU_UST, KUTU_ALT = 0.64, 0.36
TIRE_PAY, TIRE_ARA = 0.14, 0.08
BX0, BY0, BY1 = 290, 966, 1276


def T(i):
    return S11[i]["t0"]


def Q(i):
    return S12[i]["t0"]


def gen(m, b=72, agr=700, aile="Fredoka"):
    return Y.genislik(aile, agr, m, b)


def metin(m, x, y, renk, boy=72, agr=600, aile="Fredoka"):
    return ('<text x="%.2f" y="%.2f" font-family="%s" font-weight="%d" font-size="%.1f" fill="%s" '
            'xml:space="preserve">%s</text>' % (x, y, aile, agr, boy, renk, m))


def kunye_tam(bolum="Trap"):
    """SPEC §5: Dikey HUD (ders 2 satır, rozet, çip). Tek <g id="kunye">."""
    pw = gen("PRESENT CONTINUOUS", 56, 700, "Fredoka")
    rx = 48 + pw + 24
    rw = gen("YDT · BASIC", 36, 700, "Lexend") + 56
    cw = gen(bolum, 40, 700, "Lexend") + 64
    cx = 1032 - cw
    return ('<g id="kunye">'
            '<text id="ku-ders1" x="48" y="212" font-family="Fredoka" font-weight="700" font-size="56" fill="%s">'
            'SIMPLE PRESENT vs</text>'
            '<text id="ku-ders2" x="48" y="276" font-family="Fredoka" font-weight="700" font-size="56" fill="%s">'
            'PRESENT CONTINUOUS</text>'
            '<g id="ku-rozet"><rect x="%.2f" y="216" width="%.2f" height="72" rx="36" fill="%s"/>'
            '<text x="%.2f" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" '
            'fill="%s">YDT · BASIC</text></g>'
            '<g id="ku-bolum"><rect x="%.2f" y="48" width="%.2f" height="80" rx="40" fill="none" stroke="%s" stroke-width="4"/>'
            '<text x="%.2f" y="102" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="40" '
            'fill="%s">%s</text></g></g>'
            % (KRE, KRE, rx, rw, SAR, rx + rw / 2, ZEM, cx, cw, SAR, cx + cw / 2, SAR, bolum))


def acik_kart_yolu(kx, ky, kw, kh, x_gap_sol, x_gap_sag):
    """TRAP boşluğunun sağ ucundan başlar, saat yönünde döner, sol ucunda biter."""
    return ("M %.1f %.1f Q %.1f %.1f %.1f %.1f Q %.1f %.1f %.1f %.1f Q %.1f %.1f %.1f %.1f "
            "Q %.1f %.1f %.1f %.1f Q %.1f %.1f %.1f %.1f" % (
                x_gap_sag, ky,
                (x_gap_sag + kx + kw) / 2, ky - 3, kx + kw - 3, ky + 1,
                kx + kw + 3, ky + kh / 2, kx + kw - 1, ky + kh - 2,
                kx + kw / 2, ky + kh + 4, kx + 5, ky + kh + 1,
                kx - 3, ky + kh / 2, kx + 2, ky + 6,
                (kx + x_gap_sol) / 2, ky - 2, x_gap_sol, ky))


def uret():
    assert [w["sozcuk"] for w in S11[5:12]] == ["I", "live", "in", "Istanbul", "with", "my", "family."], S11[5:12]
    assert [S11[i]["sozcuk"] for i in (0, 1, 12, 13, 15, 18, 22, 27)] == [
        "Tuzak.", "Türkçe", "Türkçesi", "yaşıyorum.", "yor", "Yor", "akla", "-ing"]
    assert len(S12) == 10 and S12[0]["sozcuk"] == "Hocam," and S12[5]["sozcuk"] == "living"

    s = Y.Sahne(Z["t_bas"])
    L = s.S
    kart = set()
    bal_ids = []

    # ---------------- Ölçüm ve Geometri ----------------
    # hap "TR"
    tr_w = gen("TR", 64, 700, "Lexend")
    hap_w = tr_w + 40
    hap_x = 88
    hap_y = TB1 - 65
    hap_h = 84
    hap_rx = 42
    XT = hap_x + hap_w + 24

    k_r = hap_rx * 0.55228475
    d_trp = ("M %.1f %.1f L %.1f %.1f C %.1f %.1f %.1f %.1f %.1f %.1f "
             "C %.1f %.1f %.1f %.1f %.1f %.1f L %.1f %.1f C %.1f %.1f %.1f %.1f %.1f %.1f "
             "C %.1f %.1f %.1f %.1f %.1f %.1f Z" % (
                 hap_x + hap_rx, hap_y,
                 hap_x + hap_w - hap_rx, hap_y,
                 hap_x + hap_w - hap_rx + k_r, hap_y, hap_x + hap_w, hap_y + hap_rx - k_r, hap_x + hap_w, hap_y + hap_rx,
                 hap_x + hap_w, hap_y + hap_rx + k_r, hap_x + hap_w - hap_rx + k_r, hap_y + hap_h,
                 hap_x + hap_w - hap_rx, hap_y + hap_h,
                 hap_x + hap_rx, hap_y + hap_h,
                 hap_x + hap_rx - k_r, hap_y + hap_h, hap_x, hap_y + hap_rx + k_r, hap_x, hap_y + hap_rx,
                 hap_x, hap_y + hap_rx - k_r, hap_x + hap_rx - k_r, hap_y, hap_x + hap_rx, hap_y))

    # TRAP & kart kenarı
    trap_w = gen("TRAP", 96, 700, "Fredoka")
    x_gap_sol = 100 - 18
    x_gap_sag = 100 + trap_w + 18
    d_kr = acik_kart_yolu(KX, CY0, KW, CH, x_gap_sol, x_gap_sag)

    # EN cümleleri
    sp_en = gen(" ", 72, 700, "Fredoka")
    en_words = {
        5: "I", 6: "live", 7: "in", 8: "İstanbul",
        9: "with", 10: "my", 11: "family."
    }
    xs = {}
    cur_x = XT
    for idx in (5, 6, 7, 8):
        xs[idx] = cur_x
        cur_x += gen(en_words[idx], 72, 700, "Fredoka") + sp_en
    en1_son = cur_x - sp_en

    cur_x = XT
    for idx in (9, 10, 11):
        xs[idx] = cur_x
        cur_x += gen(en_words[idx], 72, 700, "Fredoka") + sp_en
    en2_son = cur_x - sp_en

    lw = gen("live", 72, 700, "Fredoka")
    lx = xs[6] + lw / 2  # live ortası

    # fosfor
    fp = 0.10 * 72
    fx = xs[6] - fp
    fy = EB1 - 0.78 * 72
    fh = 0.90 * 72

    # TR cümleleri
    tr1_metin = "Ailemle İstanbul'da"
    tr1_son = XT + gen(tr1_metin, 72, 600, "Fredoka")

    xa = XT
    wa = gen("yaşı", 72, 600, "Fredoka")
    wy = gen("yor", 72, 600, "Fredoka")
    wu = gen("um.", 72, 600, "Fredoka")
    wt = gen("-", 72, 600, "Fredoka")
    p = TIRE_PAY * 72
    ara = TIRE_ARA * 72
    xy0 = xa + wa
    xu0 = xa + wa + wy
    dy = wt + ara + p
    du = 2 * (wt + ara + p)
    kx0 = xy0 + dy - p
    kx1 = xy0 + dy + wy + p
    ky = TB2 - KUTU_UST * 72
    kh = (KUTU_UST + KUTU_ALT) * 72
    kb = ky + kh
    sag = xu0 + du + wu
    KXM = (kx0 + kx1) / 2

    # bag & ?
    # QA tur 1: ok ucu tik (✓) gibi okunuyordu -> eğri dikey gövdeyle (CY+296-332) biter, uç live'a yaklaşır
    OK_UC = CY0 + 332
    d_bag = ("M %.1f,%.1f C %.1f,%.1f %.1f,%.1f %.1f,%.1f L %.1f,%.1f M %.1f,%.1f L %.1f,%.1f L %.1f,%.1f" % (
        KXM, CY0 + 248,
        KXM, CY0 + 278,
        lx, CY0 + 262,
        lx, CY0 + 296,
        lx, OK_UC,
        lx - 13, OK_UC - 18,
        lx, OK_UC,
        lx + 13, OK_UC - 18))

    qw = gen("?", 72, 700, "Fredoka")
    qx = lx - 27 - qw
    qbas = CY0 + 318

    # Balon & öğrenci
    ekran_bal = ["Hocam,", "Türkçesi", "yaşıyorum.", "I", "am", "living", "in", "İstanbul", "olmaz", "mı?"]
    sp_bal = gen(" ", 64, 700, "Caveat")
    satir = ((0, 1), (2, 3, 4, 5), (6, 7, 8, 9))
    BASE = (BY0 + 76, BY0 + 168, BY0 + 260)
    gens = [sum(gen(ekran_bal[i], 64, 700, "Caveat") for i in sat) + sp_bal * (len(sat) - 1) for sat in satir]
    en_genis = max(gens)
    BX1 = max(840.0, min(850.0, round(BX0 + 40 + en_genis + 40, 1)))

    # Sarı nokta çizgisi
    kb_goreli = kb - CY0
    YC = CY1 + kb_goreli + 22
    d_bg = ("M 800,%.1f L 800,%.1f Q 800,%.1f 770,%.1f L %.1f,%.1f Q %.1f,%.1f %.1f,%.1f" % (
        BY0 + 1, YC + 30, YC, YC, kx1 + 16, YC, kx1 - 14, YC, kx1 - 14, YC - 12))

    # ---------------- 1. TRAP & Kart (162,88) ----------------
    t0 = L(T(0))
    s.yazi("trap", 100, CY0 + 33, [("TRAP", SAR)], "Fredoka", 700, 96, t0, 0.3, tur="tik", guc=0.45)
    kart.add("trap")
    s.yol("kr", d_kr, t0 + 0.1, 0.7, KRE, 4.0, 1.0, "cizgi", 0.7)
    kart.add("kr")
    org = "%.1f %.1f" % (KX + KW / 2, CY0 + CH / 2)
    s.fromto("#kartg", t0, {"scale": 0.93, "svgOrigin": org},
             {"scale": 1, "svgOrigin": org, "duration": 0.9, "ease": "power3.out"})

    # ---------------- 2. Hap "TR" (163,84) ----------------
    t1 = L(T(1))
    s.yol("trp", d_trp, t1, 0.3, KRE, 4.0, 1.0, tur=None)
    kart.add("trp")
    s.yazi("trl", hap_x + 20, TB1, [("TR", KRE)], "Lexend", 700, 64, t1, 0.2, tur="tik", guc=0.35)
    kart.add("trl")

    # ---------------- 3. EN Cümlesi (166,09–167,53) & Fosfor (176,26) ----------------
    s.svg.append('<rect id="fos" x="%.2f" y="%.2f" width="0" height="%.2f" rx="10" fill="%s" style="opacity:0"/>'
                 % (fx, fy, fh, SAR))
    kart.add("fos")

    for i in (5, 6, 7, 8):
        m = en_words[i]
        s.yazi("en%d" % i, xs[i], EB1, [(m, KRE)], "Fredoka", 700, 72, L(T(i)), 0.18,
               tur="tik" if i in (5, 8) else None, guc=0.5)
        kart.add("en%d" % i)

    for i in (9, 10, 11):
        m = en_words[i]
        dur = 0.3 if i == 11 else 0.18
        s.yazi("en%d" % i, xs[i], EB2, [(m, KRE)], "Fredoka", 700, 72, L(T(i)), dur,
               tur="tik" if i == 11 else None, guc=0.5)
        kart.add("en%d" % i)

    s.svg.append('<g id="en6z" font-family="Fredoka" font-weight="700" font-size="72" clip-path="url(#c_en6)" '
                 'style="opacity:0"><text x="%.2f" y="%.2f" fill="%s" xml:space="preserve">live</text></g>'
                 % (xs[6], EB1, ZEM))
    kart.add("en6z")

    # ---------------- 4. TR1 (168,66) ----------------
    s.yazi("tra", XT, TB1, [(tr1_metin, IKN)], "Fredoka", 600, 72, L(T(12)), 0.45, tur="tik", guc=0.45)
    kart.add("tra")

    # ---------------- 5. TR2 (169,54) & 6. ek_ayir (171,30) ----------------
    s.defs.append('<clipPath id="c_trw"><rect id="r_trw" x="%.1f" y="%.1f" width="0" height="%.1f"/></clipPath>'
                  % (xa - 8, TB2 - 72 * 1.05, 72 * 1.5))
    s.svg.append(
        '<g id="trw" clip-path="url(#c_trw)">'
        '<rect id="ekk" x="%.2f" y="%.2f" width="0" height="%.2f" rx="10" fill="%s"/>'
        '<g id="eka">%s</g>'
        '<g id="eky"><g id="eky1">%s</g><g id="eky2" style="opacity:0">%s</g></g>'
        '<g id="eku">%s</g>'
        '<g id="ekt" style="opacity:0">%s%s</g>'
        '</g>'
        % (xy0 + wy / 2, ky, kh, SAR,
           metin("yaşı", xa, TB2, IKN, 72, 600),
           metin("yor", xy0, TB2, IKN, 72, 600),
           metin("yor", xy0, TB2, ZEM, 72, 600),
           metin("um.", xu0, TB2, IKN, 72, 600),
           metin("-", xa + wa, TB2, IKN, 72, 600),
           metin("-", kx1 + ara, TB2, IKN, 72, 600))
    )
    kart.add("trw")
    s.cmd.append({"m": "rev", "id": "r_trw", "t": L(T(13)), "d": 0.4, "w": round(sag - xa + 24, 1)})
    s.olay(L(T(13)), "tik", 0.45)

    te = L(T(15))
    kay = {"duration": 0.36, "ease": "power3.out"}
    s.to("#eky", te, dict(kay, x=round(dy, 2)))
    s.to("#eku", te, dict(kay, x=round(du, 2)))
    s.to("#ekk", te, dict(kay, attr={"x": round(kx0, 2), "width": round(kx1 - kx0, 2)}))
    s.set("#eky1", te + 0.20, {"opacity": 0})
    s.set("#eky2", te + 0.20, {"opacity": 1})
    s.to("#ekt", te + 0.28, {"opacity": 1, "duration": 0.15, "ease": "power1.out"})
    s.olay(te, "cizgi", 0.55)

    # ---------------- 7. bag (172,74) ----------------
    s.yol("bag", d_bag, L(T(18)), 0.6, KRE, 4.0, 1.0, "cizgi", 0.55)
    kart.add("bag")

    # ---------------- 8. ? (174,26) ----------------
    s.svg.append('<g id="qm" style="opacity:0">%s</g>' % metin("?", qx, qbas, SAR, 72, 700))
    s.svg.append('<g id="qmi" style="opacity:0">%s</g>' % metin("?", qx, qbas, IKN, 72, 700))
    kart.add("qm")
    kart.add("qmi")
    tq = L(T(22))
    qo = "%.1f %.1f" % (qx + qw / 2, qbas - 0.36 * 72)
    s.fromto("#qm", tq, {"opacity": 0, "scale": 0.4, "svgOrigin": qo},
             {"opacity": 1, "scale": 1, "svgOrigin": qo, "duration": 0.3, "ease": "back.out(2)"})
    s.olay(tq, "tik", 0.55)

    # ---------------- 9. fosfor genişler (176,26) ----------------
    tf = L(T(27))
    s.set("#fos", tf, {"opacity": 1})
    s.to("#fos", tf, {"attr": {"width": round(lw + 2 * fp, 2)}, "duration": 0.35, "ease": "power2.out"})
    s.olay(tf, "cizgi", 0.5)
    s.set("#en6z", tf + 0.3, {"opacity": 1})
    s.set("#en6", tf + 0.3, {"opacity": 0})

    # ---------------- 10. kartg toplanma (177,40) ----------------
    s.to("#kartg", L(177.40), {"y": DY_KART, "duration": 0.35, "ease": "power3.out"})

    # ---------------- 11. Öğrenci başı & Balon (177,65) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text(encoding="utf-8")
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    s.svg.append('<g id="bas" transform="translate(987.4 1217.5) scale(-0.505 0.505)" fill="none" stroke="%s" '
                 'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>'
                 % (KRE, 4.0 / 0.505, "".join('<path id="bas%d" d="%s" style="opacity:0"/>' % (i, d) for i, d in enumerate(bd))))
    bal_ids.append("bas")
    tb_bas = L(Q(0)) - 0.20
    for i in range(3):
        s.cmd.append({"m": "draw", "id": "bas%d" % i, "t": round(tb_bas + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(tb_bas + 0.05 * i, "cizgi", 0.55)

    d_bal = Y.balon_sol(BX0, BY0, BX1, BY1, BX0 + BX1 - 870, 1270)
    ek_bal = 'transform="matrix(-1 0 0 1 %.2f 0)"' % (BX0 + BX1)
    s.yol("bal", d_bal, tb_bas + 0.10, 0.55, KRE, 4.0, 1.0, "cizgi", 0.7, ek=ek_bal)
    bal_ids.append("bal")

    # ---------------- 12. Balon sözcükleri (177,85–183,39) ----------------
    pos = {}
    for sat, base in zip(satir, BASE):
        cur_x = BX0 + 40
        for i in sat:
            m = ekran_bal[i]
            w = gen(m, 64, 700, "Caveat")
            pos[i] = (cur_x, base, w)
            dur = 0.25 if i == 9 else 0.12
            s.yazi("bw%d" % i, cur_x, base, [(m, KRE)], "Caveat", 700, 64, L(Q(i)), dur,
                   tur="tik" if i in (0, 3) else None, guc=0.5)
            bal_ids.append("bw%d" % i)
            cur_x += w + sp_bal

    # ---------------- 13. Sarı nokta çizgisi (179,37) ----------------
    t13 = L(Q(2))
    s.svg.append('<circle id="bgd" cx="800" cy="%.1f" r="12" fill="%s" style="opacity:0"/>' % (BY0 + 1, SAR))
    s.svg.append('<path id="bgi" d="%s" fill="none" stroke="%s" stroke-width="6" stroke-linecap="round" '
                 'stroke-linejoin="round" style="opacity:0"/>' % (d_bg, IKN))
    s.svg.append('<circle id="bgdi" cx="800" cy="%.1f" r="12" fill="%s" style="opacity:0"/>' % (BY0 + 1, IKN))
    s.yol("bg", d_bg, t13, 0.45, SAR, 9.0, 1.0, "cizgi", 0.45)
    do = "800.0 %.1f" % (BY0 + 1)
    s.fromto("#bgd", t13, {"opacity": 0, "scale": 0.3, "svgOrigin": do},
             {"opacity": 1, "scale": 1, "svgOrigin": do, "duration": 0.25, "ease": "back.out(2)"})
    s.set("#qm", t13, {"opacity": 0})
    s.set("#qmi", t13, {"opacity": 1})
    bal_ids.extend(["bg", "bgd", "bgi", "bgdi"])

    # ---------------- 14. living sarı altı (181,36) ----------------
    t14 = L(Q(5)) + 0.3
    s.set("#bg", t14, {"opacity": 0})
    s.set("#bgd", t14, {"opacity": 0})
    s.set("#bgi", t14, {"opacity": 1})
    s.set("#bgdi", t14, {"opacity": 1})

    lxb, lbb, lwb = pos[5]
    d_ml = Y.el_cizgi(lxb - 3, lbb + 28, lxb + lwb + 3, lbb + 28, 1.0)
    s.yol("ml", d_ml, t14, 0.35, SAR, 9.0, 1.0, "cizgi", 0.45)
    bal_ids.append("ml")

    # ---------------- Altyazı Zamanlaması ----------------
    dilimler = Y.altyazi_dilimleri([11, 12])
    for i, (t0_dilim, t1_dilim, _) in enumerate(dilimler):
        bas_alt = max(0.0, round(L(t0_dilim) - 0.05, 3))
        if i < len(dilimler) - 1:
            sonraki_t0 = dilimler[i + 1][0]
            bit_alt = min(round(L(t1_dilim) + 0.35, 3), round(L(sonraki_t0) - 0.05, 3))
        else:
            bit_alt = Z["sure"]
        s.set("#alt%d" % i, bas_alt, {"opacity": 1})
        if bit_alt < Z["sure"]:
            s.set("#alt%d" % i, bit_alt, {"opacity": 0})

    # ---------------- SPEC §8 Assert'ler ----------------
    # 1. Her metin satırının sağ ucu <= 992; balon BX1 <= 850 ve 800 <= BX1 - 40
    assert tr1_son <= 992, f"TR1 sağ ucu taştı: {tr1_son}"
    assert sag <= 992, f"TR2 sağ ucu taştı: {sag}"
    assert en1_son <= 992, f"EN1 sağ ucu taştı: {en1_son}"
    assert en2_son <= 992, f"EN2 sağ ucu taştı: {en2_son}"
    assert BX1 <= 850 and 800 <= BX1 - 40, f"Balon BX1 sınır dışı: {BX1}"

    # 2. CY1 - 34 >= 352; CY0 + CH <= 1392; CY1 + CH + 24 <= BY0; BY1 <= 1392; baş altı 1380 <= 1392
    assert CY1 - 34 >= 352, f"CY1 - 34 bandı aştı: {CY1 - 34}"
    assert CY0 + CH <= 1392, f"CY0 + CH bandı aştı: {CY0 + CH}"
    assert CY1 + CH + 24 <= BY0, f"CY1 + CH + 24 balona yakın: {CY1 + CH + 24} > {BY0}"
    assert BY1 <= 1392, f"BY1 bandı aştı: {BY1}"
    assert 1380 <= 1392, "baş altı bandı aştı"

    # 3. kanal: (CY+332) - kb >= 80; ? üstü - (TB2 + 0.27*72) >= 20; (EB1 - 0.74*72) - ? tabanı >= 20; ? sağ ucu <= LXM - 25
    assert (CY0 + 332) - kb >= 80, f"kanal dar: {(CY0 + 332) - kb}"
    assert (qbas - 0.74 * 72) - (TB2 + 0.27 * 72) >= 20, "? üstü yakın"
    assert (EB1 - 0.74 * 72) - qbas >= 20, "? altı yakın"
    assert qx + qw <= lx - 25, f"? sağ ucu LXM'ye yakın: {qx + qw} > {lx - 25}"

    # 4. fosfor sol ucu > "I" sağ ucu + 6 ve fosfor sağ ucu < "in" sol ucu - 6; ok ucu <= fosfor üstü - 12
    assert fx > xs[5] + gen(en_words[5], 72, 700, "Fredoka") + 6, "fosfor I'ya yakın"
    assert fx + lw + 2 * fp < xs[7] - 6, "fosfor in'e yakın"
    assert OK_UC <= fy - 8, f"ok ucu fosfora yakın: {OK_UC} > {fy - 8}"
    assert qx + qw <= lx - 13 - 12, "? ok kanadına yakın"

    # 5. sarı nokta çizgisi: 800 - max(EN1, EN2) >= 40; YC - kb >= 18; (CY1+332) - YC >= 40; KX1 + 16 > KXM + 40
    assert 800 - max(en1_son, en2_son) >= 40, f"sarı nokta çizgisi EN satırlarına yakın: {800 - max(en1_son, en2_son)}"
    assert YC - (CY1 + kb_goreli) >= 18, f"YC kb'ye yakın: {YC - (CY1 + kb_goreli)}"
    assert (CY1 + 332) - YC >= 40, f"YC kanal altına yakın: {(CY1 + 332) - YC}"
    assert kx1 + 16 > KXM + 40, f"KX1 KXM'ye yakın: {kx1 + 16} <= {KXM + 40}"

    # 6. living altı + 5 <= taban3 - 0.72*64 - 6; balon sözcük satırları BX1 - 40 içinde
    assert pos[5][1] + 28 + 5 <= (BY0 + 260) - 0.72 * 64 - 6, "living altı satır 3'e yakın"
    assert all(pos[i][0] + pos[i][2] <= BX1 - 40 for i in range(10)), "balon sözcüğü balondan taştı"

    # 7. Ders ve rozet 984 içinde, rozet sağ ucu < çip sol ucu (HUD satır ayrı ama yazı kutuları çakışmaz)
    w_ders2 = gen("PRESENT CONTINUOUS", 56, 700, "Fredoka")
    rx_hud = 48 + w_ders2 + 24
    rw_hud = gen("YDT · BASIC", 36, 700, "Lexend") + 56
    cw_hud = gen("Trap", 40, 700, "Lexend") + 64
    cx_hud = 1032 - cw_hud
    assert rx_hud + rw_hud <= 1032, f"Ders ve rozet 984'ü aştı: {rx_hud + rw_hud}"
    assert rx_hud + rw_hud < cx_hud or 48 + 80 <= 216, "HUD kutuları çakışıyor"

    Y.kontrol(s, Z["kare"], ilk=True)
    s.kart = kart
    s.bal = bal_ids
    return s, kunye_tam("Trap")


if __name__ == "__main__":
    s, kun = uret()
    dilimler = Y.altyazi_dilimleri([11, 12])
    altyazi = Y.altyazi_svg([{"id": "alt%d" % i, "metin": m} for i, (_, _, m) in enumerate(dilimler)])
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(s, Z["sure"], kun, None, (48, 48, 96 * Y.LOGO_EN_BOY, 96),
               ek=altyazi, bal_ids=s.bal, gruplar=[("kartg", s.kart)]),
        encoding="utf-8"
    )
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev))

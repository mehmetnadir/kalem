"""Sahne 13 Mini soru (02-04 YDT temel dikey, HyperFrames, 1080x1920, 940 kare).
Kök + 5 şık + sayaç («Beş şık var»), yanlış cevap A balonu + soluk sarı çerçeve,
odak (lives in Ankara, this month), doğru (B vurgu dolgusu + koyu tik + is living),
çeldirici pilleri (A, C, E, D).
Yerleşim BRIEF-DIKEY §2 + SPEC.md: HUD 0-320, içerik 352-1392, altyazı 1400-1536, platform boş.
Zaman: ../../zaman.json + ../../ortak/anlatim/sozcukler.json (cümle 15, 16, 17)."""
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
SOZ = {c: [w for w in _ham if w["cumle"] == c] for c in (15, 16, 17)}
R = Y.RENK
KRE, IKN, SAR = R["murekkep"], R["ikincil"], R["vurgu"]
TB = Z["t_bas"]
FPS = 30

SIK = {"A": "lives", "B": "is living", "C": "live", "D": "to live", "E": "are living"}

# çeldirici notları: (harf, imleç bilgisi | None, pil bilgisi, parçalar)
NOT = [
    ("A", None, (13, "geçici"), [("t", "this month"), ("->",), ("t", "temporary")]),
    ("C", (22, "C"), (27, "özneyle"), [("t", "he"), ("<>",), ("t", "live")]),
    ("E", (25, "E"), (28, "uyumsuz."), [("t", "he"), ("<>",), ("t", "are")]),
    ("D", (29, "D"), (31, "tek"), [("t", "to live: no tense")]),
]


def T(c: int, i: int, bas: str) -> float:
    """Cümle c, i. sözcüğün t0'ı (küresel sn); sözcük kayarsa durur."""
    w = SOZ[c][i]
    assert w["sozcuk"].lower().startswith(bas.lower()), "cümle %d sözcük %d: %r, beklenen %r" % (
        c, i, w["sozcuk"], bas
    )
    return w["t0"]


def alt_y(taban: float, sozcuk: str) -> float:
    """Karaoke ve odak altçizgisi y konumu (g j p q y veya virgül varsa taban + 25, yoksa taban + 21)."""
    return taban + (25.0 if any(c in sozcuk for c in "gjpqy,") else 21.0)


def lejant_kart_yolu(g0: float, g1: float) -> str:
    """Kart çerçevesi tek açık yol: başlangıç (g1, 380) -> sağ üst -> sağ kenar -> alt -> sol -> sol üst -> bitiş (g0, 380)."""
    return (
        f"M{g1:.1f} 380.0 "
        f"Q{(g1 + 1032) / 2:.1f} 377.0 1029.0 381.0 "
        f"Q1035.0 {380 + 332 / 2:.1f} 1031.0 710.0 "
        f"Q{48 + 984 / 2:.1f} 716.0 53.0 713.0 "
        f"Q45.0 {380 + 332 / 2:.1f} 50.0 384.0 "
        f"Q{(48 + g0) / 2:.1f} 378.0 {g0:.1f} 380.0"
    )


def pil_genislik(parcalar: list) -> float:
    """Çeldirici notu genişliği: iç pay 24x2=48, parça arası 14, metin Caveat 700 64, ok 56 px."""
    w = 0.0
    for n, p in enumerate(parcalar):
        if n > 0:
            w += 18.0
        if p[0] == "t":
            w += Y.genislik("Caveat", 700, p[1], 64)
        else:
            w += 52.0
    return w + 58.0   # iç pay sol 24 + sağ 34 (Caveat y/p kuyruğu sağ alt köşe eğrisine değmesin)


def pil(s: Y.Sahne, h: str, cy: float, parcalar: list, tn: float) -> None:
    """sik_not pili: çerçeve rect + parça text'leri + ok yolları; satır grubunun dışında kalır."""
    sik_w = Y.genislik("Fredoka", 700, f"{h}) {SIK[h]}", 64)
    sik_sag = 128.0 + sik_w
    pw = pil_genislik(parcalar)
    px = max(420.0, sik_sag + 40.0)

    assert px >= 420.0, f"pil x 420 altında: {h}"
    assert sik_sag + 40.0 <= px + 1e-6, f"şık yazısı sağ ucu ile pil arası yakın: {h}"
    assert px + pw <= 1032.0, f"pil {h} taştı: {px + pw}"

    g = [
        f'<rect x="{px:.1f}" y="{cy - 40:.1f}" width="{pw:.1f}" height="80" rx="40" '
        f'fill="none" stroke="{IKN}" stroke-width="4"/>'
    ]
    x_cur = px + 24.0
    y_base = cy + 14.0
    y_ok = cy + 1.0

    for n, p in enumerate(parcalar):
        if n > 0:
            x_cur += 18.0
        if p[0] == "t":
            g.append(
                f'<text x="{x_cur:.1f}" y="{y_base:.1f}" font-family="Caveat" font-weight="700" '
                f'font-size="64" fill="{KRE}" xml:space="preserve">{p[1]}</text>'
            )
            x_cur += Y.genislik("Caveat", 700, p[1], 64)
        elif p[0] in ("->", "<>"):
            d_ok = (
                f"M{x_cur + 3:.1f} {y_ok:.1f} L{x_cur + 49:.1f} {y_ok:.1f} "
                f"M{x_cur + 37:.1f} {y_ok - 11:.1f} L{x_cur + 49:.1f} {y_ok:.1f} L{x_cur + 37:.1f} {y_ok + 11:.1f}"
            )
            if p[0] == "<>":
                d_ok += (
                    f" M{x_cur + 15:.1f} {y_ok - 11:.1f} L{x_cur + 3:.1f} {y_ok:.1f} L{x_cur + 15:.1f} {y_ok + 11:.1f}"
                )
            g.append(
                f'<path d="{d_ok}" fill="none" stroke="{KRE}" stroke-width="5" '
                f'stroke-linecap="round" stroke-linejoin="round"/>'
            )
            x_cur += 52.0

    s.svg.append(f'<g id="pil{h}" style="opacity:0">{"".join(g)}</g>')
    s.goster(f"#pil{h}", tn, 0.3, -24, 0)
    s.olay(tn, "tik", 0.4)


def ikincile_don(s: Y.Sahne, ids: list[str], t: float) -> None:
    """Sarı belirteci ikincil ikizine dönüştürür (0,3 sn)."""
    for kim in ids:
        s.to("#" + kim, t, {"opacity": 0, "duration": 0.3})
        s.to("#" + kim + "_i", t, {"opacity": 1, "duration": 0.3})


def uret() -> tuple[Y.Sahne, dict]:
    s = Y.Sahne(TB)
    S = s.S
    bal_ids: list[str] = []

    # ---------------- HUD (kare 0 sabit) ----------------
    kun = Y.kunye_svg("Mini question")
    gw_pc = Y.genislik("Fredoka", 700, "PRESENT CONTINUOUS", 56)
    gw_rz = Y.genislik("Lexend", 700, "YDT · BASIC", 36)
    rx = 48.0 + gw_pc + 24.0
    rw = gw_rz + 56.0
    tx = rx + rw / 2.0
    ku_ders = (
        '<g id="ku-ders">'
        '<text x="48" y="212" font-family="Fredoka" font-weight="700" font-size="56" fill="#f3efe6">SIMPLE PRESENT vs</text>'
        '<text x="48" y="276" font-family="Fredoka" font-weight="700" font-size="56" fill="#f3efe6">PRESENT CONTINUOUS</text>'
        '</g>'
    )
    ku_rozet = (
        f'<g id="ku-rozet">'
        f'<rect x="{rx:.2f}" y="216" width="{rw:.2f}" height="72" rx="36" fill="#f2a93b"/>'
        f'<text x="{tx:.2f}" y="265" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="36" '
        f'fill="#1b1a17">YDT · BASIC</text>'
        f'</g>'
    )
    kun = kun.replace('<g id="kunye">', f'<g id="kunye">{ku_ders}{ku_rozet}')

    # ---------------- Soru kartı ve etiket ----------------
    etiket_w = Y.genislik("Lexend", 700, "MINI QUESTION", 56)
    g0 = 72.0
    g1 = 88.0 + etiket_w + 16.0
    t_kart = S(T(15, 0, "Mini"))
    s.yol("kart", lejant_kart_yolu(g0, g1), t_kart, 0.6, KRE, 4.0, 1.0, "cizgi", 0.7)
    s.yazi("etiket", 88.0, 400.0, [("MINI QUESTION", KRE)], "Lexend", 700, 56, t_kart + 0.15, d=0.3, tur="tik", guc=0.45)

    # ---------------- Kök yerleşimi (3 satır, KX=88, KB=[472, 558, 644]) ----------------
    sp = Y.genislik("Fredoka", 700, " ", 72)
    KB = [480.0, 566.0, 652.0]   # şef: +8 px, MINI QUESTION etiketi ile satır 1 arası açılır

    # Satır 1
    w_list: list[dict] = []
    x = 88.0
    for soz_i, m in [(2, "My"), (3, "brother"), (4, "lives"), (5, "in")]:
        gw = Y.genislik("Fredoka", 700, m, 72)
        w_list.append({"m": m, "x": x, "w": gw, "base": KB[0], "soz_i": soz_i, "li": 0})
        x += gw + sp
    assert x - sp <= 1032 - 40, "satır 1 sağ kenara taştı"
    assert 932.0 - (x - sp) >= 16.0, "sayaç sol kenarı satır 1 sağ ucuna çok yakın"

    # Satır 2
    x = 88.0
    for soz_i, m in [(6, "Ankara,"), (7, "but"), (8, "this"), (9, "month")]:
        gw = Y.genislik("Fredoka", 700, m, 72)
        w_list.append({"m": m, "x": x, "w": gw, "base": KB[1], "soz_i": soz_i, "li": 1})
        x += gw + sp
    assert x - sp <= 1032 - 40, "satır 2 sağ kenara taştı"

    # Satır 3: "he", boşluk, "with", "us."
    x = 88.0
    gw = Y.genislik("Fredoka", 700, "he", 72)
    w_list.append({"m": "he", "x": x, "w": gw, "base": KB[2], "soz_i": 10, "li": 2})
    x += gw + sp

    bos_w = Y.genislik("Fredoka", 700, "is living", 72) + 48.0
    bos_x = x
    x += bos_w + sp

    for soz_i, m in [(11, "with"), (12, "us.")]:
        gw = Y.genislik("Fredoka", 700, m, 72)
        w_list.append({"m": m, "x": x, "w": gw, "base": KB[2], "soz_i": soz_i, "li": 2})
        x += gw + sp
    assert x - sp <= 1032 - 40, "satır 3 sağ kenara taştı"
    assert bos_x + bos_w <= 1032 - 40, "boşluk sağ kenara taştı"

    # Kök sözcükler (w0..w10) ve karaoke (ka0..ka10)
    for n, p in enumerate(w_list):
        m = p["m"]
        t_w = S(T(15, p["soz_i"], m[:2]))
        s.yazi(f"w{n}", p["x"], p["base"], [(m, KRE)], "Fredoka", 700, 72, t_w, d=0.14, tur="tik" if n == 0 else None, guc=0.5)
        alt = alt_y(p["base"], m)
        s.yol(f"ka{n}", Y.el_cizgi(p["x"] - 2, alt, p["x"] + p["w"] + 2, alt, 1), t_w, 0.12, SAR, 6.0, 1.0, tur=None)
        s.to(f"#ka{n}", t_w + 0.30, {"opacity": 0, "duration": 0.15})

    # Boşluk soluk çizgisi (bl0)
    y_bos = KB[2] + 0.48 * 72   # sözleşme: kalıcı altçizgi taban + 0,48 × boy (g kuyruğu değmez)
    t_bl0 = S(SOZ[15][10]["t1"]) + 0.06
    s.yol("bl0", Y.el_cizgi(bos_x + 4, y_bos, bos_x + bos_w - 4, y_bos, 2), t_bl0, 0.3, IKN, 5.0, 1.0, "cizgi", 0.5)

    # Boşluk vurgu çizgisi (gb0) + ikiz (gb0_i)
    tbo = S(T(15, 13, "Boş"))
    s.to("#bl0", tbo, {"opacity": 0, "duration": 0.15})
    d_gb0 = Y.el_cizgi(bos_x + 2, y_bos, bos_x + bos_w - 2, y_bos - 1, 1)
    s.yol("gb0", d_gb0, tbo + 0.15, 0.35, SAR, 10.0, 1.0, "cizgi", 0.5)
    s.svg.append(f'<path id="gb0_i" d="{d_gb0}" stroke="{IKN}" stroke-width="6" fill="none" '
                 f'stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>')

    # ---------------- Sayaç «Beş şık var» (229,33): halka dolar, ortada 5 ----------------
    tsay = S(T(15, 17, "Beş"))
    d_say = "M%.1f %.1f A%.1f %.1f 0 1 1 %.2f %.1f" % (972.0, 440.0 - 40.0, 40.0, 40.0, 972.0 - 0.01, 440.0 - 40.0)
    s.yol("say", d_say, tsay, 0.96, SAR, 8.0, 1.0, "cizgi", 0.55)
    nw5 = Y.genislik("Fredoka", 700, "5", 56)
    s.yazi("say5", 972.0 - nw5 / 2.0, 440.0 + 20.0, [("5", KRE)], "Fredoka", 700, 56, tsay + 0.04, 0.2, tur="tik", guc=0.5)
    s.to("#say", tsay + 1.12, {"opacity": 0, "duration": 0.25})
    s.to("#say5", tsay + 1.12, {"opacity": 0, "duration": 0.25})

    # ---------------- 5 Şık satırı ----------------
    harfler = "ABCDE"
    for k, h in enumerate(harfler):
        y0 = 730.0 + 88.0 * k
        cy = y0 + 40.0
        taban = cy + 22.0
        if h == "B":
            s.svg.append(
                f'<g id="rowB" style="opacity:0">'
                f'<rect id="grB" x="48" y="{y0:.1f}" width="984" height="80" rx="24" fill="{SAR}" style="opacity:0"/>'
                f'<text class="m" x="128" y="{taban:.1f}" font-family="Fredoka" font-weight="700" font-size="64" '
                f'fill="{KRE}" xml:space="preserve">B) is living</text>'
                f'<text class="p" x="128" y="{taban:.1f}" font-family="Fredoka" font-weight="700" font-size="64" '
                f'fill="#1b1a17" style="opacity:0" xml:space="preserve">B) is living</text>'
                f'</g>'
            )
        else:
            s.svg.append(
                f'<g id="row{h}" style="opacity:0">'
                f'<text class="m" x="128" y="{taban:.1f}" font-family="Fredoka" font-weight="700" font-size="64" '
                f'fill="{KRE}" xml:space="preserve">{h}) {SIK[h]}</text>'
                f'</g>'
            )
        s.goster(f"#row{h}", tsay + 0.18 * k, 0.35, 0, 24)
    s.olay(tsay, "tik", 0.5)
    s.olay(tsay + 0.4, "tik", 0.4)

    # ---------------- Öğrenci başı + Balon (yanlış cevap A) ----------------
    kit = (Y.ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg").read_text()
    bd = re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', kit)
    assert len(bd) == 3, "ogrenci-bas.svg: 3 path beklenir"
    sc_bas = 160.0 / 330.0
    tx_bas = 48.0 + 45.0 * sc_bas
    ty_bas = 1210.0
    sw_bas = 4.4 / sc_bas
    paths_bas = "".join(f'<path id="bas{i}" d="{d}" style="opacity:0"/>' for i, d in enumerate(bd))
    s.svg.append(
        f'<g id="bas" transform="translate({tx_bas:.3f} {ty_bas:.3f}) scale({sc_bas:.5f})" '
        f'fill="none" stroke="{KRE}" stroke-width="{sw_bas:.2f}" stroke-linecap="round" stroke-linejoin="round">'
        f'{paths_bas}</g>'
    )
    t_bas_draw = S(T(16, 0, "Bence")) - 0.18
    for i in range(3):
        s.cmd.append({"m": "draw", "id": f"bas{i}", "t": round(t_bas_draw + 0.05 * i, 4), "d": 0.32, "a": 1})
        s.olay(t_bas_draw + 0.05 * i, "cizgi", 0.55)

    # Balon ölçüsü ve çizimi
    sp_c = Y.genislik("Caveat", 700, " ", 64)
    satir_idx = ((0, 1, 2), (3, 4, 5, 6))
    gens = [
        sum(Y.genislik("Caveat", 700, SOZ[16][i]["sozcuk"], 64) for i in sat) + sp_c * (len(sat) - 1)
        for sat in satir_idx
    ]
    max_satir_w = max(gens)
    x1b = 220.0 + 36.0 + max_satir_w + 44.0
    assert x1b <= 1032.0 - 8.0, f"balon taştı: {x1b}"
    assert 256.0 + max_satir_w <= x1b - 36.0, "balon satır sağ ucu taştı"
    assert 1384.0 <= 1392.0, "balon y1 taştı"
    assert 1162.0 + 24.0 <= 1198.0, "balon şık satırına çok yakın"

    t_bal = t_bas_draw + 0.1
    s.yol("bal", Y.balon_sol(220, 1198, x1b, 1384, 176, 1318), t_bal, 0.55, KRE, 4.2, 1.0, "cizgi", 0.7)
    bal_ids.append("bal")

    for sat, base in zip(satir_idx, (1272.0, 1346.0)):
        xw = 256.0
        for i in sat:
            m = SOZ[16][i]["sozcuk"]
            s.yazi(f"bw{i}", xw, base, [(m, KRE)], "Caveat", 700, 64, S(SOZ[16][i]["t0"]), 0.12,
                   tur="tik" if i in (0, 3) else None, guc=0.5)
            bal_ids.append(f"bw{i}")
            xw += Y.genislik("Caveat", 700, m, 64) + sp_c

    # A şıkkı: soluk sarı çerçeve (afr)
    tA = S(T(16, 1, "A"))
    s.svg.append(f'<rect id="afr" x="48" y="730" width="984" height="80" rx="24" fill="none" '
                 f'stroke="{SAR}" stroke-width="4" style="opacity:0"/>')
    s.to("#afr", tA, {"opacity": 0.55, "duration": 0.3, "ease": "power2.out"})
    s.olay(tA, "tik", 0.5)

    # ---------------- Öğretmen cevabı: balon söner (baş kalır), odak çizgileri ----------------
    th = S(T(17, 0, "Ankara"))
    s.to("#balg", th, {"opacity": 0, "duration": 0.4, "ease": "power2.in"})
    s.olay(th, "vurus", 0.6)

    # odak1a: lives in (satır 1)
    w_lives, w_in = w_list[2], w_list[3]
    x_odak1a_0 = w_lives["x"] - 4.0
    x_odak1a_1 = w_in["x"] + w_in["w"] + 4.0
    y_odak1a = alt_y(KB[0], "lives in")
    d_odak1a = Y.el_cizgi(x_odak1a_0, y_odak1a, x_odak1a_1, y_odak1a, 1)
    s.yol("odak1a", d_odak1a, th + 0.1, 0.35, SAR, 10.0, 0.85, "cizgi", 0.5)
    s.svg.append(f'<path id="odak1a_i" d="{d_odak1a}" stroke="{IKN}" stroke-width="6" fill="none" '
                 f'stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>')

    # odak1b: Ankara (satır 2, virgül dışarıda)
    w_ank = w_list[4]
    x_odak1b_0 = w_ank["x"] - 4.0
    x_odak1b_1 = w_ank["x"] + Y.genislik("Fredoka", 700, "Ankara", 72) + 4.0
    y_odak1b = alt_y(KB[1], "Ankara")
    d_odak1b = Y.el_cizgi(x_odak1b_0, y_odak1b, x_odak1b_1, y_odak1b, 1)
    s.yol("odak1b", d_odak1b, th + 0.1 + 0.35, 0.3, SAR, 10.0, 0.85, tur=None)
    s.svg.append(f'<path id="odak1b_i" d="{d_odak1b}" stroke="{IKN}" stroke-width="6" fill="none" '
                 f'stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>')

    # odak2: this month (satır 2); odak1a ve odak1b ikincile döner
    w_this, w_month = w_list[6], w_list[7]
    t_bu = S(T(17, 6, "bu"))
    x_odak2_0 = w_this["x"] - 4.0
    x_odak2_1 = w_month["x"] + w_month["w"] + 4.0
    y_odak2 = alt_y(KB[1], "this month")
    d_odak2 = Y.el_cizgi(x_odak2_0, y_odak2, x_odak2_1, y_odak2, 1)
    s.yol("odak2", d_odak2, t_bu, 0.4, SAR, 10.0, 0.85, "cizgi", 0.5)
    s.svg.append(f'<path id="odak2_i" d="{d_odak2}" stroke="{IKN}" stroke-width="6" fill="none" '
                 f'stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>')
    ikincile_don(s, ["odak1a", "odak1b"], t_bu)

    # ---------------- A pili, A çerçevesi söner, A satırı soluklaşır ----------------
    cy_A = 730.0 + 40.0
    tnA = S(T(17, 13, "geçici"))
    pil(s, "A", cy_A, [("t", "this month"), ("->",), ("t", "temporary")], tnA)
    s.to("#afr", tnA, {"opacity": 0, "duration": 0.25})
    s.to("#rowA", tnA + 0.2, {"opacity": 0.4, "duration": 0.35})

    # ---------------- Doğru şık B: dolgu + koyu yazı + koyu tik ----------------
    tdg = S(T(17, 17, "B"))
    s.to("#grB", tdg, {"opacity": 1, "duration": 0.3, "ease": "power2.out"})
    s.to("#rowB .m", tdg, {"opacity": 0, "duration": 0.3})
    s.to("#rowB .p", tdg, {"opacity": 1, "duration": 0.3})
    s.olay(tdg, "vurus", 0.85)

    cy_B = 818.0 + 40.0
    wB = Y.genislik("Fredoka", 700, "B) is living", 64)
    assert 944.0 - (128.0 + wB) >= 32.0, "B tiki B yazısına çok yakın"
    s.yol("ck", Y.tik_yolu(944.0, cy_B - 24.0, 48.0), tdg + 0.2, 0.3, "#1b1a17", 9.0, 1.0, "cizgi", 0.55)
    s.svg.append('<style id="pm13">#root #ck{stroke:var(--pilMetin)}</style>')

    # Boşluğa "is living" yazılır, odak2 ikincile döner
    t_is = S(T(17, 20, "is"))
    fw = Y.genislik("Fredoka", 700, "is living", 72)
    fl_x = bos_x + (bos_w - fw) / 2.0
    s.yazi("fl0", fl_x, KB[2], [("is living", KRE)], "Fredoka", 700, 72, t_is, d=0.3, tur="tik", guc=0.55)
    ikincile_don(s, ["odak2"], t_is)

    # ---------------- Çeldirici pilleri (C, E, D) ve imleçler ----------------
    cy_C = 906.0 + 40.0
    cy_D = 994.0 + 40.0
    cy_E = 1082.0 + 40.0

    # C imleci + gb0 ikincile döner
    tC = S(T(17, 22, "C"))
    s.yol("ptC", Y.el_ok(58, cy_C, 112, cy_C, 1), tC, 0.25, SAR, 9.0, 1.0, "tik", 0.45)
    ikincile_don(s, ["gb0"], tC)

    # E imleci
    tE = S(T(17, 25, "E"))
    s.yol("ptE", Y.el_ok(58, cy_E, 112, cy_E, 1), tE, 0.25, SAR, 9.0, 1.0, "tik", 0.45)

    # C pili + C soluklaşır
    tnC = S(T(17, 27, "özneyle"))
    pil(s, "C", cy_C, [("t", "he"), ("<>",), ("t", "live")], tnC)
    s.to("#rowC", tnC + 0.2, {"opacity": 0.4, "duration": 0.35})

    # E pili + E soluklaşır
    tnE = S(T(17, 28, "uyumsuz."))
    pil(s, "E", cy_E, [("t", "he"), ("<>",), ("t", "are")], tnE)
    s.to("#rowE", tnE + 0.2, {"opacity": 0.4, "duration": 0.35})

    # D imleci (C ve E söner)
    tD = S(T(17, 29, "D"))
    s.to("#ptC", tD, {"opacity": 0, "duration": 0.15})
    s.to("#ptE", tD, {"opacity": 0, "duration": 0.15})
    s.yol("ptD", Y.el_ok(58, cy_D, 112, cy_D, 1), tD, 0.25, SAR, 9.0, 1.0, "tik", 0.45)

    # D pili + D soluklaşır
    tnD = S(T(17, 31, "tek"))
    pil(s, "D", cy_D, [("t", "to live: no tense")], tnD)
    s.to("#rowD", tnD + 0.2, {"opacity": 0.4, "duration": 0.35})

    # ---------------- Altyazı aç/kapa (tek dilim görünür) ----------------
    dil = Y.altyazi_dilimleri([15, 16, 17])

    def aktif(t: float) -> int:
        k = -1
        for i, (t0, t1, _m) in enumerate(dil):
            if t0 - 0.05 <= t < t1 + 0.35:
                k = i
        return k

    onc = -1
    for f in range(Z["kare"]):
        k = aktif(TB + f / FPS)
        if k != onc:
            if onc >= 0:
                s.cmd.append({"m": "set", "s": f"#alt{onc}", "t": round(f / FPS, 4), "v": {"opacity": 0}})
            if k >= 0:
                s.cmd.append({"m": "set", "s": f"#alt{k}", "t": round(f / FPS, 4), "v": {"opacity": 1}})
            onc = k

    # ---------------- Genel Asserts ----------------
    assert 380 >= 352 and 380 + 332 <= 1392, "kart içerik bandı dışında"
    assert 400.0 - 0.7 * 56.0 >= 352.0, "etiket üstü içerik bandı dışında"
    assert len("My brother lives in") <= 24
    assert len("Ankara, but this month") <= 24
    assert len("he is living with us.") <= 24
    for h, m in SIK.items():
        assert len(f"{h}) {m}") <= 24, f"şık satırı karakter sayısı fazla: {h}"
    for h, _, _, parcalar in NOT:
        t_chars = "".join(p[1] for p in parcalar if p[0] == "t")
        assert len(t_chars) <= 24, f"pil karakter sayısı fazla: {h}"

    bas, son = Y.kontrol(s, Z["kare"], ilk=True)
    return s, {"kun": kun, "bal_ids": bal_ids, "aralik": (bas, son)}


if __name__ == "__main__":
    s, parca = uret()
    dil = Y.altyazi_dilimleri([15, 16, 17])
    altyazi = Y.altyazi_svg([{"id": f"alt{i}", "metin": m} for i, (_, _, m) in enumerate(dil)])
    (AD / "proje").mkdir(exist_ok=True)
    (AD / "proje" / "index.html").write_text(
        Y.html(
            s,
            Z["sure"],
            parca["kun"],
            None,
            (48, 48, 96 * Y.LOGO_EN_BOY, 96),
            ek=altyazi,
            bal_ids=parca["bal_ids"],
        )
    )
    print("index.html yazıldı; komut", len(s.cmd), "olay", len(s.ev), "hareket", parca["aralik"])

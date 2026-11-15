"""YouTube sürümü DİKEY parçaları (istem YT-2, 15.11.2026; standart D/.claude/docs/youtube-surumu-standart.md).
  /usr/bin/python3 -I uret.py [--tema acik|koyu]      giris/ · cikis/ · cikis-kisa/ proje/index.html (1080x1920, 30 fps)
  /usr/bin/python3 -I uret.py --onizle                 onizle.html (dikey çerçeve; yer bildirim/yer.json'dan)
Yatay üretici (../uret.py) tek kaynaktır: yazı tipi, tema CSS'i, sayfa betiği, GSAP komutları, söz zamanları, süreler.
Bu dosya yalnız dikey yerleşimi ve dikey zemini (vinyet: dikey HF sahneleriyle aynı, circle 1150px 40 %) taşır.
Ses dosyaları burada üretilmez: giriş ve uzun çıkış yatayın kopyasıdır, kısa çıkış önbellek parçasıdır (olc.py ses)."""
from __future__ import annotations

import importlib.util
import json
import sys
import wave
from pathlib import Path

DY = Path(__file__).resolve().parent
# yatay YT-1 üreticisi (font_css, TEMA_JS, KOMUT_JS, hf_tema, logo, vur, ses, süreler); ad çakışmasın diye yoldan yüklenir
_spec = importlib.util.spec_from_file_location("uret_yatay", DY.parent / "uret.py")
Y = importlib.util.module_from_spec(_spec)
sys.modules["uret_yatay"] = Y
_spec.loader.exec_module(Y)

W, H, FPS = 1080, 1920, 30
ICERIK = (288, 1344)                  # içerik bölgesi y %15–70 (istem; dikey ders güvenli alanı)
YARI = 960                            # uzun çıkış: y ≥ 960 yalnız zemin (bitiş ekranı ögeleri)
SAG_SERIT = (900, 864, 1536)          # Shorts düğmeleri: x ≥ 900, y %45–80 (kısa çıkışta hiçbir öğe girmez)
SOL = 96                              # yazı sol kenarı (dikey ders kinetik satırları x 96)

# ---- giriş: yatayla aynı sahne (logo + kanal adı, tek hareket), dikey ders logo damgası boyunda ----
GIRIS_LOGO_H = 192                    # dikey ders 01 sahnesi logo damgası (LOGO_H u(192), ≈ 774 px)
GIRIS_LOGO_Y = 658
GIRIS_KANAL_TABAN, GIRIS_KANAL_BOY = 975, 60   # yatay 48 px × 192/150 ≈ 61

# ---- çıkış (uzun, > 180 sn ders): üst yarı söz + logo + kanal, alt yarı boş; ok aşağıyı (bitiş ekranını) gösterir ----
KANAL_LOGO_H = 88
KANAL_BOY = 48
SOZ_BOY = 112                         # Fredoka 700 ("Faydalı olduysa" ≈ 7,06 px/boy → 791 px; x 96–887)
SIRA_BOY = 56
CIKIS = {"logo_y": 300, "soz1": 560, "soz2": 690, "sira": 810}
OK = (776, 925, 850)                  # ok: (başlangıç x, uç y, uç x); başlangıç y = sıra satırı ortası

# ---- kısa çıkış (≤ 180 sn ders, YouTube Shorts): söz + logo + kanal içerik bölgesinde, ≤ 4 sn ----
KISA_SURE = 3.0
KISA_SOZ = 0.30                       # ilk söz (ölçülen enerji başı) 0,30 sn
KISA = {"logo_y": 600, "soz1": 870, "soz2": 1000}
KISA_METIN = "Faydalı olduysa abone ol."

ZEMIN_CSS = ("html,body{margin:0;background:transparent;}"
             "#root{position:relative;width:%dpx;height:%dpx;overflow:hidden;}"
             "#zemin{position:absolute;inset:0;background:var(--zemin);}"
             "#gren{position:absolute;left:0;top:0;opacity:var(--gren);mix-blend-mode:overlay;}"
             "#vinyet{position:absolute;inset:0;background:radial-gradient(circle 1150px at 50%% 50%%,"
             "rgba(0,0,0,0) 40%%,rgba(0,0,0,var(--vin)) 100%%);}"
             "#sahne{position:absolute;left:0;top:0;}"
             "#root.yalniz-zemin #icerik{visibility:hidden;}" % (W, H))
ZEMIN_HTML = Y.ZEMIN_HTML.replace('width="%d" height="%d"' % (Y.W, Y.H), 'width="%d" height="%d"' % (W, H))


def sayfa(sure: float, govde: str, komut: list[dict], tema: str, baslik: str) -> str:
    sinif = ' class="tema-acik"' if tema == "acik" else ""
    veri = json.dumps(sorted(komut, key=lambda c: c["t"]), ensure_ascii=False)
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><title>{baslik}</title>
<style>
{Y.font_css()}
{ZEMIN_CSS}
{Y.hf_tema.CSS}</style></head><body>
<div id="root"{sinif} data-composition-id="main" data-start="0" data-duration="{sure}" data-fps="{FPS}" data-width="{W}" data-height="{H}">
{ZEMIN_HTML}
<svg id="sahne" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<g id="icerik">{govde}</g>
</svg></div>
<script src="lib/gsap.min.js"></script>
<script>var C = {veri};
{Y.KOMUT_JS}</script>
<script>{Y.TEMA_JS}</script>
</body></html>
"""


def gizli(svg: str) -> str:
    """Satır öğesi opaklık 0 ile başlar (tek style özniteliği)."""
    return svg.replace(')"', ');opacity:0"', 1)


def kanal_satiri(y: float, tema: str) -> str:
    """Logo + @ydspublishing yan yana; kanal adı tabanı logo yazısının tabanında (yatay çıkış düzeni)."""
    lw = KANAL_LOGO_H * Y.LOGO_EN_BOY
    lx = SOL - lw * Y.LOGO_KAYMA
    return ('<g id="marka" style="opacity:0">%s%s</g>' % (
        Y.logo_image("logoimg", lx, y, KANAL_LOGO_H, tema),
        Y.yazi("kanal-yazi", lx + lw + KANAL_LOGO_H * 0.34, y + Y.LOGO_TABAN * KANAL_LOGO_H, "Lexend", 700, KANAL_BOY,
               "murekkep", Y.KANAL)))


def giris(tema: str) -> str:
    """Yatay giriş sahnesi (aynı süre, aynı tek hareket, aynı ses zamanı), dikey çerçevede ortalı."""
    s = Y.ses("giris")
    assert Y.GIRIS_SES_BAS <= 1.0 and Y.GIRIS_SES_BAS + s["sure"] <= Y.GIRIS_SURE - 0.2
    lw = GIRIS_LOGO_H * Y.LOGO_EN_BOY
    oy = (GIRIS_LOGO_Y + GIRIS_KANAL_TABAN) / 2
    assert ICERIK[0] <= GIRIS_LOGO_Y and GIRIS_KANAL_TABAN + 0.3 * GIRIS_KANAL_BOY <= ICERIK[1]
    govde = ('<g id="marka" style="opacity:0">%s%s</g>'
             % (Y.logo_image("logoimg", (W - lw) / 2, GIRIS_LOGO_Y, GIRIS_LOGO_H, tema),
                Y.yazi("kanal-yazi", W / 2, GIRIS_KANAL_TABAN, "Lexend", 700, GIRIS_KANAL_BOY, "ikincil", Y.KANAL,
                       ' text-anchor="middle"')))
    komut = [{"m": "fromTo", "s": "#marka", "t": 0.0,
              "a": {"opacity": 0, "scale": 1.12, "svgOrigin": "%.1f %.1f" % (W / 2, oy)},
              "v": {"opacity": 1, "scale": 1, "duration": Y.GIRIS_OTUR, "ease": "power3.out"}}]
    return sayfa(Y.GIRIS_SURE, govde, komut, tema, "YouTube giriş (dikey)")


def ok_asagi(x0: float, y0: float, x1: float, y1: float) -> str:
    """El çizgisi: sağa çıkıp aşağı kıvrılır, ok ucu aşağı bakar (uçta teğet dikey)."""
    k = 22
    return ("M%.1f %.1f Q%.1f %.1f %.1f %.1f M%.1f %.1f L%.1f %.1f L%.1f %.1f"
            % (x0, y0, x1, y0 + 6, x1, y1, x1 - k * 0.48, y1 - k * 0.88, x1, y1, x1 + k * 0.48, y1 - k * 0.88))


def cikis(tema: str) -> str:
    """Uzun çıkış: üst yarı kanal satırı + söz satırları + aşağı ok; y ≥ 960 yalnız zemin. Zamanlar yatay çıkışla aynı."""
    s = Y.ses("cikis")
    soz = s["sozcukler"]
    assert [w[0] for w in soz] == ["Faydalı", "olduysa", "abone", "ol.", "Sıradaki", "ders", "ekranda."], soz

    def T(i: int) -> float:
        return Y.CIKIS_SES_BAS + soz[i][1]

    oky = CIKIS["sira"] - 0.34 * SIRA_BOY
    govde = kanal_satiri(CIKIS["logo_y"], tema)
    govde += gizli(Y.yazi("soz1", SOL, CIKIS["soz1"], "Fredoka", 700, SOZ_BOY, "murekkep", "Faydalı olduysa"))
    govde += gizli(Y.yazi("soz2", SOL, CIKIS["soz2"], "Fredoka", 700, SOZ_BOY, "vurgu", "abone ol."))
    govde += gizli(Y.yazi("sira", SOL, CIKIS["sira"], "Lexend", 700, SIRA_BOY, "ikincil", "Sıradaki ders ekranda."))
    govde += ('<path id="ok" d="%s" fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" '
              'style="stroke:var(--ikincil);opacity:0"/>' % ok_asagi(OK[0], oky, OK[2], OK[1]))
    komut = [{"m": "fromTo", "s": "#marka", "t": 0.0, "a": {"opacity": 0},
              "v": {"opacity": 1, "duration": 0.30, "ease": "power1.out"}},
             Y.vur("soz1", SOL, CIKIS["soz1"], T(0)), Y.vur("soz2", SOL, CIKIS["soz2"], T(2)),
             Y.vur("sira", SOL, CIKIS["sira"], T(4)),
             {"m": "draw", "id": "ok", "t": round(T(6), 3), "d": 0.35}]
    son = max(c["t"] + (c.get("d") or c.get("v", {}).get("duration", 0)) for c in komut)
    assert son <= Y.CIKIS_SES_BAS + s["sure"] + 0.05, "hareket sözden sonra sürüyor: %.2f" % son
    assert OK[1] + 6 < YARI - 20, "ok alt yarıya yakın"
    return sayfa(Y.CIKIS_SURE, govde, komut, tema, "YouTube çıkış (dikey, uzun)")


def kisa_kayma() -> float:
    """Kısa çıkış sesinin yerleşimi: parça yatay cumle-1.wav'ın ilk parçası; enerji başı (−40 dBFS, 10 ms) KISA_SOZ'a gelir.
    Dönen değer: parçanın 0 noktasının kısa çıkıştaki zamanı (sn)."""
    import numpy as np
    with wave.open(str(Y.YT / "cikis" / "ses" / "cumle-1.wav")) as w:
        sr = w.getframerate()
        a = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float32) / 32768.0
    n = sr // 100
    p = a[: len(a) // n * n].reshape(-1, n)
    i = np.nonzero(20 * np.log10(np.sqrt((p ** 2).mean(1)) + 1e-9) > -40.0)[0][0]
    return round(KISA_SOZ - i * n / sr, 3)


def cikis_kisa(tema: str) -> str:
    """Kısa çıkış (Shorts): kanal satırı + "Faydalı olduysa / abone ol." içerik bölgesinde; satırlar söylendiği anda vurur."""
    s = Y.ses("cikis")
    soz, parca = s["sozcukler"][:4], s["parcalar"][0]
    assert " ".join(w[0] for w in soz) == KISA_METIN, soz
    p = kisa_kayma()
    t1, t2 = KISA_SOZ, p + soz[2][1]
    assert abs(p + soz[0][1] - KISA_SOZ) < 0.12, "ilk sözcük hizası %.2f" % (p + soz[0][1])
    assert p + parca[1] <= KISA_SURE - 0.5, "söz %.2f sn'de bitiyor" % (p + parca[1])
    govde = kanal_satiri(KISA["logo_y"], tema)
    govde += gizli(Y.yazi("soz1", SOL, KISA["soz1"], "Fredoka", 700, SOZ_BOY, "murekkep", "Faydalı olduysa"))
    govde += gizli(Y.yazi("soz2", SOL, KISA["soz2"], "Fredoka", 700, SOZ_BOY, "vurgu", "abone ol."))
    komut = [{"m": "fromTo", "s": "#marka", "t": 0.0, "a": {"opacity": 0},
              "v": {"opacity": 1, "duration": 0.25, "ease": "power1.out"}},
             Y.vur("soz1", SOL, KISA["soz1"], t1), Y.vur("soz2", SOL, KISA["soz2"], t2)]
    return sayfa(KISA_SURE, govde, komut, tema, "YouTube kısa çıkış (dikey, Shorts)")


ONIZLE_DERS = 6.0
ONIZLE_KART = (2.0, 3.0, 0.3)         # ders karesinin 2. sn'sinde, 3 sn; solma 0,3 sn
ORNEK = {"uzun": "02-04-ydt-temel-dikey", "kisa": "simple-present-temel-dikey"}   # uzun: 265,7 sn · kısa: 93,5 sn


def onizle() -> str:
    """onizle.html: giriş → 6 sn örnek dikey ders karesi (2. sn'de kart, 3 sn) → çıkış (uzun ya da kısa).
    Tek dosya, göreli yollar, dış ağ isteği yok. Kart görseli yatayın dosyası (../bildirim/), yeri bildirim/yer.json."""
    yer = json.loads((DY / "bildirim" / "yer.json").read_text(encoding="utf-8"))
    for ders in ORNEK.values():
        for tema in ("acik", "koyu"):
            assert (DY / "bildirim" / "ders" / ("%s-%s.png" % (ders, tema))).exists(), "önce olc.py yer"
    veri = json.dumps({"giris": Y.GIRIS_SURE, "ders": ONIZLE_DERS, "kart": ONIZLE_KART,
                       "cikis": {"uzun": Y.CIKIS_SURE, "kisa": KISA_SURE}, "ornek": ORNEK})
    kw, kh = round(yer["w"]), round(yer["h"])
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><title>YouTube sürümü önizleme (dikey) · giriş, bildirim, çıkış</title>
<style>
{Y.font_css()}
html,body{{margin:0;height:100%;}}
#root{{height:100%;background:var(--zemin);color:var(--murekkep);font-family:Lexend;font-weight:500;
  display:flex;flex-direction:column;align-items:center;gap:10px;padding:10px;box-sizing:border-box;}}
#ust{{display:flex;gap:10px;align-items:center;flex-wrap:wrap;justify-content:center;}}
button{{font:700 16px Lexend;padding:7px 14px;border-radius:12px;border:2px solid var(--murekkep);
  background:var(--zemin);color:var(--murekkep);cursor:pointer;}}
#durum{{font-size:14px;color:var(--ikincil);min-width:16em;text-align:center;}}
#kap{{position:relative;height:calc(100vh - 130px);max-width:96vw;aspect-ratio:9/16;overflow:hidden;border-radius:10px;
  outline:2px solid var(--ikincil);}}
#sahne{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:0 0;}}
#sahne iframe,#sahne img.kat{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;border:0;visibility:hidden;}}
#kart{{position:absolute;left:{yer["x"]}px;top:{yer["y"]}px;width:{kw}px;height:{kh}px;opacity:0;}}
#not{{font-size:13px;color:var(--ikincil);text-align:center;}}
{Y.hf_tema.CSS}</style></head><body>
<div id="root" class="tema-acik">
<div id="ust"><button id="bastan">Baştan</button><button id="tema">Açık / Koyu</button>
<button id="cikisd">Uzun çıkış / Kısa çıkış</button><span id="durum"></span></div>
<div id="kap"><div id="sahne">
<iframe id="giris" class="kat" src="./giris/proje/index.html?tema=acik" scrolling="no"></iframe>
<img id="ders" class="kat" alt="örnek dikey ders karesi" src="./bildirim/ders/{ORNEK["uzun"]}-acik.png">
<img id="kart" alt="Beğen · Abone ol" src="../bildirim/bildirim-acik.png">
<iframe id="cikis" class="kat" src="./cikis/proje/index.html?tema=acik" scrolling="no"></iframe>
<iframe id="kisa" class="kat" src="./cikis-kisa/proje/index.html?tema=acik" scrolling="no"></iframe>
</div></div>
<div id="not">Giriş {Y.GIRIS_SURE:.1f} sn → örnek ders karesi {ONIZLE_DERS:.0f} sn (kart {ONIZLE_KART[0]:.0f}.–{ONIZLE_KART[0] + ONIZLE_KART[1]:.0f}. sn,
sessiz) → çıkış: uzun {Y.CIKIS_SURE:.0f} sn (ders &gt; 180 sn) ya da kısa {KISA_SURE:.1f} sn (ders ≤ 180 sn, Shorts).
Kart yeri: {yer["kose"]} x {yer["x"]} y {yer["y"]} ({kw}×{kh}, ölçek {yer["olcek"]}).</div>
<audio id="a-giris" src="./giris/ses/giris.wav" preload="auto"></audio>
<audio id="a-cikis" src="./cikis/ses/cikis.wav" preload="auto"></audio>
<audio id="a-kisa" src="./cikis-kisa/ses/cikis-kisa.wav" preload="auto"></audio>
</div>
<script>
(function () {{
  var S = {veri}, $ = function (q) {{ return document.getElementById(q); }};
  var tema = "acik", tur = "uzun", oynuyor = false, t0 = 0, son = "", faz = "";
  var A = {{ giris: $("a-giris"), cikis: $("a-cikis"), kisa: $("a-kisa") }};
  function cik() {{ return tur === "uzun" ? "cikis" : "kisa"; }}
  function toplam() {{ return S.giris + S.ders + S.cikis[tur]; }}
  function olcekle() {{ $("sahne").style.transform = "scale(" + ($("kap").clientWidth / {W}) + ")"; }}
  function goster(ad) {{ ["giris", "ders", "cikis", "kisa"].forEach(function (k) {{
      $(k).style.visibility = k === ad ? "visible" : "hidden"; }});
    $("kart").style.visibility = ad === "ders" ? "visible" : "hidden"; }}
  function yolla(ad, t) {{ $(ad).contentWindow.postMessage({{ tip: "zaman", t: t }}, "*"); }}
  function kartOpak(u) {{ var b = S.kart[0], e = b + S.kart[1], g = S.kart[2];
    return Math.max(0, Math.min(1, (u - b) / g, (e - u) / g)); }}
  function ciz(t) {{
    var yeni;
    if (t < S.giris) {{ yeni = "giris"; yolla("giris", t); }}
    else if (t < S.giris + S.ders) {{ yeni = "ders"; $("kart").style.opacity = kartOpak(t - S.giris); }}
    else {{ yeni = cik(); yolla(yeni, Math.min(t - S.giris - S.ders, S.cikis[tur] - 1 / 30)); }}
    if (yeni !== faz) {{ goster(yeni); if (oynuyor) sesBaslat(yeni, t); faz = yeni; }}
    $("durum").textContent = {{ giris: "giriş", ders: "örnek ders karesi", cikis: "uzun çıkış", kisa: "kısa çıkış" }}[yeni]
      + " · " + t.toFixed(1) + " / " + toplam().toFixed(1) + " sn" + son;
  }}
  function sesDur() {{ Object.keys(A).forEach(function (k) {{ A[k].pause(); }}); }}
  function sesBaslat(ad, t) {{
    sesDur();
    var a = A[ad], yerel = ad === "giris" ? t : t - S.giris - S.ders;
    if (!a) return;
    a.currentTime = Math.max(0, yerel);
    a.play().then(function () {{ son = ""; }}, function () {{ son = " · ses için Baştan'a bas"; }});
  }}
  function dongu() {{
    if (!oynuyor) return;
    var t = (performance.now() - t0) / 1000;
    if (t >= toplam()) {{ oynuyor = false; ciz(toplam() - 1 / 30); return; }}
    ciz(t); requestAnimationFrame(dongu);
  }}
  function bastan() {{ oynuyor = true; faz = ""; t0 = performance.now(); requestAnimationFrame(dongu); }}
  function dersKare() {{ $("ders").src = "./bildirim/ders/" + S.ornek[tur] + "-" + tema + ".png"; }}
  window.__seek = function (t) {{ oynuyor = false; sesDur(); faz = ""; ciz(t); }};
  window.__tur = function (ad) {{ tur = ad; dersKare(); faz = ""; }};
  $("bastan").onclick = bastan;
  $("tema").onclick = function () {{
    tema = tema === "acik" ? "koyu" : "acik";
    $("root").classList.toggle("tema-acik", tema === "acik");
    ["giris", "cikis", "kisa"].forEach(function (k) {{ $(k).contentWindow.postMessage({{ tip: "tema", ad: tema }}, "*"); }});
    dersKare(); $("kart").src = "../bildirim/bildirim-" + tema + ".png";
  }};
  $("cikisd").onclick = function () {{ window.__tur(tur === "uzun" ? "kisa" : "uzun"); bastan(); }};
  addEventListener("resize", olcekle); olcekle();
  var yuklenen = 0, q = new URLSearchParams(location.search);
  ["giris", "cikis", "kisa"].forEach(function (k) {{ $(k).addEventListener("load", function () {{
    if (++yuklenen < 3) return;
    if (q.get("tema") === "koyu") $("tema").onclick();
    if (q.get("cikis") === "kisa") window.__tur("kisa");
    setTimeout(function () {{ window.__hazir = true; if (q.get("oynat") !== "0") bastan(); }}, 400); }}); }});
}})();
</script>
</body></html>
"""


if __name__ == "__main__":
    if "--onizle" in sys.argv:
        (DY / "onizle.html").write_text(onizle(), encoding="utf-8")
        print("yazıldı: dikey/onizle.html")
        raise SystemExit(0)
    TEMA = Y.tema_arg(sys.argv)
    for ad, fn in (("giris", giris), ("cikis", cikis), ("cikis-kisa", cikis_kisa)):
        proje = DY / ad / "proje"
        Y.varlik(proje)
        (proje / "index.html").write_text(fn(TEMA), encoding="utf-8")
    print("yazıldı: dikey/{giris,cikis,cikis-kisa}/proje/index.html · tema", TEMA, "· kısa söz kayması", kisa_kayma())

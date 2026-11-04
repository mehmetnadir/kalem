#!/usr/bin/python3
"""HyperFrames sahnesinin proje/index.html dosyasını temaya çevirir (yerinde, tekrar çalıştırılabilir).
  /usr/bin/python3 -I hf_tema.py <index.html> acik|koyu
uret.py koyu renkleri sabit yazar; bu betik renk değişkenlerini (CSS), 'tema-acik' sınıfını ve canlı önizleme
düğmesini ekler. Palet ortak/kunye.js TEMALAR ile aynıdır (K19: zemin #f7f3ea, mürekkep #1b2440, vurgu #d9900f)."""
from __future__ import annotations
import re, sys

ZEMIN_DEGISIM = [
    ("overflow:hidden;background:#1b1a17;}", "overflow:hidden;background:var(--zemin);}"),
    ("#zemin{position:absolute;inset:0;background:#1b1a17;}", "#zemin{position:absolute;inset:0;background:var(--zemin);}"),
    ("opacity:.045;mix-blend-mode:overlay;}", "opacity:var(--gren);mix-blend-mode:overlay;}"),
    ("rgba(0,0,0,.38) 100%)", "rgba(0,0,0,var(--vin)) 100%)"),
]
CSS = (
    '#root{--zemin:#1b1a17;--murekkep:#f3efe6;--ikincil:#c9c2b3;--vurgu:#f2a93b;--vurguDolgu:#f2a93b;'
    '--logoSari:#fece00;--logoMetin:#ffffff;--kirmizi:#e0473b;--pilMetin:#1b1a17;--gren:.045;--vin:.38;}\n'
    '#root.tema-acik{--zemin:#f7f3ea;--murekkep:#1b2440;--ikincil:#5a6275;--vurgu:#d9900f;--vurguDolgu:#ffe066;'
    '--logoMetin:#13204D;--kirmizi:#d6453a;--pilMetin:#1b2440;--gren:.03;--vin:.10;}\n'
    '#root [fill="#f3efe6"]{fill:var(--murekkep)}#root [stroke="#f3efe6"]{stroke:var(--murekkep)}\n'
    '#root [fill="#c9c2b3"]{fill:var(--ikincil)}#root [stroke="#c9c2b3"]{stroke:var(--ikincil)}\n'
    '#root [fill="#f2a93b"]{fill:var(--vurgu)}#root [stroke="#f2a93b"]{stroke:var(--vurgu)}\n'
    '#root rect[fill="#f2a93b"],#root circle[fill="#f2a93b"]:not(#ku-nokta){fill:var(--vurguDolgu)}\n'
    '#root [fill="#e0473b"]{fill:var(--kirmizi)}#root [stroke="#e0473b"]{stroke:var(--kirmizi)}\n'
    '#root [stroke="#1b1a17"]{stroke:var(--zemin)}#root text[fill="#1b1a17"]{fill:var(--pilMetin)}'
    '#root #rz1 text{fill:var(--zemin)}\n'
    '#root.tema-acik #t2{fill:var(--vurgu)}\n')
LOGO = "/projeler/present-continuous-s1/ortak/logo/"
JS = ('<script>/* kalem-tema */(function () {  /* canlı önizleme (?canli=1): ?tema=acik ya da message {tip:"tema", ad}; '
      'sorgu yoksa koyu. Render sırasında çalışmaz, tema dosyaya gömülüdür */\n'
      '  if (!/[?&]canli=1/.test(location.search)) return;\n'
      '  var R = document.getElementById("root"), L = document.getElementById("logoimg") || document.getElementById("logo");\n'
      '  function t(a) { R.classList.toggle("tema-acik", a === "acik");\n'
      '    if (L) L.setAttribute("href", "' + LOGO + '" + (a === "acik" ? "yds-publishing-lacivert.svg" : "yds-publishing-seffaf.svg")); }\n'
      '  t(new URLSearchParams(location.search).get("tema") || "koyu");\n'
      '  addEventListener("message", function (e) { if (e.data && e.data.tip === "tema") t(e.data.ad); });\n'
      '})();</script>')
ESKI_JS = re.compile(r"<script>(?:/\* kalem-tema \*/)?\(function \(\) \{  /\* canlı önizleme (?:\(\?canli=1\): )?"
                     r"(?:teması: )?.*?\}\)\(\);</script>", re.S)


def donustur(html: str, tema: str) -> str:
    if "#root.tema-acik" not in html:
        for eski, yeni in ZEMIN_DEGISIM:
            if eski not in html: raise SystemExit(f"hf_tema: beklenen CSS yok: {eski!r}")
            html = html.replace(eski, yeni, 1)
        html = html.replace("</style>", CSS + "</style>", 1)
    html = ESKI_JS.sub("", html)
    html = html.replace("</body>", JS + "\n</body>", 1)
    sinif = re.search(r'<div id="root"([^>]*)>', html)
    if not sinif: raise SystemExit("hf_tema: #root yok")
    govde = re.sub(r'\s+class="[^"]*"', "", sinif.group(1))
    yeni = '<div id="root"' + (' class="tema-acik"' if tema == "acik" else "") + govde + ">"
    return html.replace(sinif.group(0), yeni, 1)


if __name__ == "__main__":
    yol, tema = sys.argv[1], sys.argv[2]
    if tema not in ("acik", "koyu"): sys.exit("tema acik|koyu")
    s = open(yol, encoding="utf-8").read(); open(yol, "w", encoding="utf-8").write(donustur(s, tema))

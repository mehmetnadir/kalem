#!/usr/bin/env python3
"""Matris galerisi: projeler/*/cikti*.mp4 dosyalarını konu × seviye × biçim × tema ızgarasında listeler.
Kullanım: /usr/bin/python3 -I araclar/matris-sayfa.py   (çıktı: projeler/matris.html; 3012'de /projeler/matris.html)"""
import json
import re
from pathlib import Path

K = Path(__file__).resolve().parent.parent
P = K / "projeler"
KONULAR = [
  ("present-continuous", "Present Continuous"), ("simple-present", "Simple Present"),
  ("present-perfect", "Present Perfect"), ("present-perfect-cont", "Present Perfect Continuous"),
  ("simple-past", "Simple Past"),
]
BICIMLER = [("", "Yatay 16:9", "ana-yatay"), ("-dikey", "Dikey 9:16", "dikey-tam"), ("-s1", "Shorts", "shorts")]


def kok(konu: str, seviye: str) -> str:
  if konu == "present-continuous" and seviye == "temel":
    return "present-continuous"
  return f"{konu}-{seviye}"


def kare(proje: Path) -> str:
  z = proje / "zaman.json"
  if not z.exists():
    return "-"
  s = json.loads(z.read_text())["sahneler"]
  return str(sum(x["kare"] for x in s) - 12 * (len(s) - 1))


def hucre(proje: str, tema: str) -> str:
  ad = "cikti.mp4" if tema == "acik" else "cikti-koyu.mp4"
  if not (P / proje / ad).exists():
    return "<td class='yok'>yok</td>"
  return (f"<td><video controls preload='none' src='/projeler/{proje}/{ad}'></video>"
          f"<div class='alt'>{tema}</div></td>")


satirlar = []
for konu, baslik in KONULAR:
  for seviye in ("temel", "ileri"):
    k = kok(konu, seviye)
    ana = k if seviye == "temel" and konu == "present-continuous" else k
    for ek, bicim_ad, surum in BICIMLER:
      proje = f"{ana}{ek}"
      if konu == "present-continuous" and seviye == "temel":
        proje = "present-continuous" + ek
      dur = "var" if (P / proje / "cikti.mp4").exists() else "yok"
      editor = f"/p/{proje}/onizle.html?surum={surum}&tema=acik"
      satirlar.append(
        f"<tr class='{dur}'><th>{baslik}<br><small>{seviye}</small></th>"
        f"<td>{bicim_ad}<br><small>{kare(P / proje)} kare · <a href='{editor}'>editör</a></small></td>"
        + hucre(proje, "acik") + hucre(proje, "koyu") + "</tr>")

html = f"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<title>Grammar matrisi — 5 konu × 2 seviye × 3 biçim × 2 tema</title>
<style>
body{{font-family:-apple-system,Helvetica,sans-serif;margin:24px;background:#f7f5ef;color:#1d2340}}
table{{border-collapse:collapse;width:100%}} th,td{{border:1px solid #cfcabc;padding:8px;vertical-align:top}}
th{{text-align:left;background:#efe9d8;width:180px}} video{{width:100%;max-width:420px;background:#111}}
tr.yok td{{color:#a33}} .yok{{color:#a33}} .alt{{font-size:12px;color:#666}} small{{color:#666}}
</style></head><body>
<h1>Grammar matrisi (05.11)</h1>
<p>5 konu × 2 seviye × 3 biçim × 2 tema = 60 video. Her kutu bir mp4; "editör" bağlantısı canlı önizlemeyi açar.</p>
<table><tr><th>Konu / seviye</th><td>Biçim</td><td>Açık</td><td>Koyu</td></tr>
{''.join(satirlar)}
</table></body></html>
"""
(P / "matris.html").write_text(html)
print(len(satirlar), "satır →", P / "matris.html")

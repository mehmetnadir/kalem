#!/usr/bin/python3 -I
"""buda-<öğe>.json: bir öğenin kaynaktaki sürüm kimlikleri (DB'de sürüm adı = kimlik).
Kullanım: buda-oge.py <öğe> <paket>[=kimlik,kimlik] …   (kimlik listesi verilmezse paketin bütün sürümleri)"""
import json
import sys
from pathlib import Path

K = Path.home() / "01dev/_worktrees/kalem-0204/projeler"
oge = sys.argv[1]
kimlikler: list[str] = []
for arg in sys.argv[2:]:
    paket, _, sec = arg.partition("=")
    secili = set(sec.split(",")) if sec else None
    for s in json.loads((K / paket / "surumler.json").read_text(encoding="utf-8"))["surumler"]:
        if secili is None or s["kimlik"] in secili:
            kimlikler.append(s["kimlik"])
cikti = Path.home() / f"is/uretim-0204/buda-{oge}.json"
cikti.write_text(json.dumps({"ogeler": [{"kimlik": oge, "surumler": kimlikler}]}), encoding="utf-8")
print(cikti.name, len(kimlikler), kimlikler)

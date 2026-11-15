#!/usr/bin/python3 -I
"""buda-0204.json: 02-04-ydt-temel öğesinin kaynaktaki sürüm kimlikleri (DB'de sürüm adı = kimlik)."""
import json
from pathlib import Path

K = Path.home() / "01dev/_worktrees/kalem-0204/projeler"
kimlikler: list[str] = []
for paket, sec in (("02-04-ydt-temel", {"ana-yatay"}), ("02-04-ydt-temel-dikey", None), ("02-04-ydt-temel-s1", None),
                   ("02-04-ydt-temel-s2", None), ("02-04-ydt-temel-s3", None)):
    for s in json.loads((K / paket / "surumler.json").read_text(encoding="utf-8"))["surumler"]:
        if sec is None or s["kimlik"] in sec:
            kimlikler.append(s["kimlik"])
(Path.home() / "is/uretim-0204/buda-0204.json").write_text(
    json.dumps({"ogeler": [{"kimlik": "02-04-ydt-temel", "surumler": kimlikler}]}), encoding="utf-8")
print(len(kimlikler), kimlikler)

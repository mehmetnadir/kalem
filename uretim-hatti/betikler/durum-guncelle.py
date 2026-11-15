#!/usr/bin/python3 -I
"""02-04-ydt-temel sürüm durumları: üretimi biten dikey ve kısa satırları 'inceleme' olur (15.11)."""
import json
from pathlib import Path

K = Path.home() / "01dev/_worktrees/kalem-0204/projeler"
HEDEF = {"02-04-ydt-temel": {"dikey-tam", "shorts"}, "02-04-ydt-temel-dikey": {"dikey-tam"},
         "02-04-ydt-temel-s1": {"s1"}, "02-04-ydt-temel-s2": {"s2"}, "02-04-ydt-temel-s3": {"s3"}}
for paket, kimlikler in HEDEF.items():
    yol = K / paket / "surumler.json"
    veri = json.loads(yol.read_text(encoding="utf-8"))
    degisen = []
    for s in veri.get("surumler", []):
        if s.get("kimlik") in kimlikler and s.get("durum") != "inceleme":
            degisen.append(f"{s['kimlik']}: {s.get('durum')} → inceleme")
            s["durum"] = "inceleme"
    if degisen:
        yol.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(paket, "·", "; ".join(degisen) or "değişmedi", "· satırlar:",
          [(s.get("kimlik"), s.get("tur"), s.get("durum")) for s in veri.get("surumler", [])])

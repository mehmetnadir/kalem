"""Sunucu işi sonucu: oku.py <ad> [karakter]"""
import json, sys
from pathlib import Path
D = Path.home() / "is" / "uretim-0204"
ad = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 2500
b = D / f"{ad}.bitti"
print("bitti:", b.read_text().strip() if b.exists() else "YOK")
e = D / f"{ad}.err"
if e.exists() and e.stat().st_size: print("err:", e.read_text()[:400])
try:
  d = json.loads((D / f"{ad}.json").read_text())
except Exception as x:
  print("json okunamadı:", x); sys.exit(0)
print(d.get("subtype"), "tur", d.get("num_turns"), "maliyet", round(d.get("total_cost_usd", 0), 2), "sn", d.get("duration_ms", 0) // 1000)
print(d.get("result", "")[:n])

"""Sahne 03 olaylar.json: uret.py'nin yazdığı zamanlar.json "olaylar" listesinden ({kare, tur, guc})."""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
Z = json.loads((AD / "zamanlar.json").read_text())
ol = sorted(({"kare": round(t * Z["fps"]), "tur": tur, "guc": guc} for t, tur, guc in Z["olaylar"]),
            key=lambda o: o["kare"])
assert all(12 <= o["kare"] < Z["kare"] - 12 for o in ol), "olay ilk/son 12 kare içinde"
(AD / "olaylar.json").write_text(json.dumps(ol, ensure_ascii=False))
print("olay", len(ol))

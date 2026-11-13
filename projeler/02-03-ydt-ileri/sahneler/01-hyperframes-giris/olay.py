"""Sahne 01 olaylar.json: uret.py'nin ses olayları (tek kaynak)."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import uret as U  # noqa: E402

s, _, _ = U.uret()
ol = sorted(s.ev, key=lambda o: o["kare"])
sayac = {}
for o in ol:   # aynı karede en çok 3 olay: fazlası sonraki kareye kayar
    k = o["kare"]
    while sayac.get(k, 0) >= 3:
        k += 1
    sayac[k] = sayac.get(k, 0) + 1
    o["kare"] = k
ol.sort(key=lambda o: o["kare"])
assert all(0 <= o["kare"] < U.Z["kare"] - 12 for o in ol), "olay son 12 karede"
(AD / "olaylar.json").write_text(json.dumps(ol, ensure_ascii=False))
print("olay", len(ol), "cizgi", sum(1 for o in ol if o["tur"] == "cizgi"))

"""Sahne 01 kanca olaylar.json: uret.py zamanlar() çıktısından darbe ve ses efekt zamanları (✗ · uçuş · satır · kart)."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import uret as U  # noqa: E402


def f(t: float) -> int:
    return round(t * 30)


zz = U.zamanlar()

ol = [
    {"kare": f(zz["carpi"][0]), "tur": "cizgi", "guc": 0.6},
    {"kare": f(zz["ucus"][0]), "tur": "parilti", "guc": 0.5},
    {"kare": f(zz["satir"][0]), "tur": "hisirti", "guc": 0.45},
    {"kare": f(zz["kart"][0]), "tur": "tik", "guc": 0.5},
]

ol.sort(key=lambda o: o["kare"])
sayac = {}
for o in ol:
    k = o["kare"]
    while sayac.get(k, 0) >= 3:
        k += 1
    sayac[k] = sayac.get(k, 0) + 1
    o["kare"] = k
ol.sort(key=lambda o: o["kare"])

assert all(0 <= o["kare"] < U.Z["kare"] - 12 for o in ol)
(AD / "olaylar.json").write_text(json.dumps(ol, ensure_ascii=False))
print("olay", len(ol))

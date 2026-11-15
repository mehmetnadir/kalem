"""Sahne 01 olaylar.json (kol b): uret.py zamanlar() çıktısından darbe ve ses efekt zamanları."""
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
    # kol b (KBC-0204S1): satır 1 ve 2 tek süpürme; yor kutuları "tik" (kol a sahne 02'deki gibi); uçuş yerine kayma
    {"kare": f(zz["alti"][0]), "tur": "cizgi", "guc": 0.6},
    {"kare": f(zz["r1"][0]), "tur": "hisirti", "guc": 0.45},
    {"kare": f(zz["r2"][0]), "tur": "hisirti", "guc": 0.45},
    {"kare": f(zz["yk1"][0]), "tur": "tik", "guc": 0.5},
    {"kare": f(zz["yk2"][0]), "tur": "tik", "guc": 0.5},
    {"kare": f(zz["kay"][0]), "tur": "parilti", "guc": 0.5},
    {"kare": f(zz["konu"][0] + zz["konu"][1]) - 1, "tur": "tik", "guc": 0.5},
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

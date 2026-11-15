"""Sahne 01 kanca (simple-present-temel-s3) olaylar.json: uret.py zamanlar() çıktısından darbe ve ses efekt zamanları."""
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
    {"kare": f(zz["cerceve"][0]), "tur": "cizgi", "guc": 0.6},  # YANLIŞ hap çerçevesi (0,30)
    {"kare": f(zz["soru"][0]), "tur": "cizgi", "guc": 0.6},  # kırmızı ? (Hata 2,69)
    {"kare": f(zz["cikis"][0]), "tur": "parilti", "guc": 0.5},  # çıkış başı
    {"kare": f(zz["cikis"][0] + zz["cikis"][1]) - 1, "tur": "tik", "guc": 0.5},  # kart yerine oturur
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

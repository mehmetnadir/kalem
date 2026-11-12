"""Sahne 03 olaylar.json: zamanlar.json ile aynı zamanlar."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import uret as U  # noqa: E402

Z = U.Z
saat, sz = U.yapi()
f = lambda t: round(t * 30)  # noqa: E731
ol = [{"kare": f(Z["bant_kontur"][0]), "tur": "cizgi", "guc": 0.6},
      {"kare": f(Z["tam_ders"][0]), "tur": "hisirti", "guc": 0.45},
      {"kare": f(Z["bant"][0]), "tur": "vurus", "guc": 0.9},
      {"kare": f(Z["satir2"][0]), "tur": "tik", "guc": 0.5},
      {"kare": f(Z["satir3"][0]), "tur": "tik", "guc": 0.5},
      {"kare": f(Z["pill"][0]), "tur": "tik", "guc": 0.6},
      {"kare": f(Z["cta"][0]), "tur": "hisirti", "guc": 0.5},
      {"kare": f(Z["parilti"]), "tur": "parilti", "guc": 0.5}]
for (b, d), g in zip(sz, (0.6, 0.45)):
    ol.append({"kare": f(b), "tur": "cizgi", "guc": g})
ol.sort(key=lambda o: o["kare"])
assert all(0 <= o["kare"] < Z["kare"] for o in ol)
(AD / "olaylar.json").write_text(json.dumps(ol, ensure_ascii=False))
print("olay", len(ol))

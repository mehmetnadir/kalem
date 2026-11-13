"""Sahne 01 olaylar.json: zamanlar.json + uret.py ile aynı darbe zamanları (tek kaynak)."""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import uret as U  # noqa: E402

Z = U.Z
obj = U.yapi()
f = lambda t: round(t * 30)  # noqa: E731
ol = [{"kare": Z["vurus_kare"], "tur": "vurus", "guc": 0.9}]
# kalem sesleri 0. kareden: başlık satır 1 (cizgi + hışırtı), satır 2 + cümle yazımı (hışırtı)
ol.append({"kare": f(Z["baslik"][0][0]), "tur": "cizgi", "guc": 0.7})
ol.append({"kare": f(Z["baslik"][0][0]), "tur": "hisirti", "guc": 0.6})
ol.append({"kare": f(Z["baslik"][1][0]), "tur": "hisirti", "guc": 0.5})
ol.append({"kare": f(U.SOZ[0]["t0"]), "tur": "hisirti", "guc": 0.45})
ol.append({"kare": f(U.SOZ[-1]["t0"]), "tur": "tik", "guc": 0.5})   # ediyorum. yazılmaya başlar
for ad, olcek, x, y, yollar, zam in obj:
    mx = max(d for b, d in zam)
    for b, d in zam:
        ol.append({"kare": f(b), "tur": "cizgi", "guc": 0.7 if d >= 0.5 * mx else round(0.4 + 0.3 * d / (0.5 * mx), 2)})
for i in range(2):
    ol.append({"kare": f(Z["rozet"][0] + i * Z["rozet"][1]), "tur": "tik", "guc": 0.4})
ol.append({"kare": f(Z["ucus"][0]), "tur": "parilti", "guc": 0.5})
ol.append({"kare": f(Z["ucus"][0] + Z["ucus"][1]) - 1, "tur": "tik", "guc": 0.5})  # künye yerine oturur
# aynı karede en çok 3 olay: fazlası sonraki kareye kayar
ol.sort(key=lambda o: o["kare"])
sayac = {}
for o in ol:
    k = o["kare"]
    while sayac.get(k, 0) >= 3:
        k += 1
    sayac[k] = sayac.get(k, 0) + 1
    o["kare"] = k
ol.sort(key=lambda o: o["kare"])
assert all(0 <= o["kare"] < Z["kare"] for o in ol)
(AD / "olaylar.json").write_text(json.dumps(ol, ensure_ascii=False))
print("olay", len(ol), "cizgi", sum(1 for o in ol if o["tur"] == "cizgi"))

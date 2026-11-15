"""sozcukler.json üretici: sureler.json (cümle içi sözcük zamanları) + cümle başları (sn).
Cümle başları sabit dizi DEĞİL, hesaplanır: ilk cümle 1,00 sn (K23 soğuk açılış); sonraki cümle başı =
önceki cümlenin bitişi (başı + sure) + cümle arası sessizlik. Sessizlik: GAP 0,55 sn; öğrenci cümlesinden sonra
GAP_OGRENCI 0,75 sn (soru anı duraklaması, taslak §6). Cümle rolü senaryo.json'daki `ses` alanından gelir.
Whisper yok: sözcük payları sentez raporundan (sureler.json). Çıktı: sozcukler.json [{cumle, sozcuk, t0, t1}]
küresel sn + baslar.json {cümle no: [başı, bitişi]}. Kullanım: /usr/bin/python3 -I sozcuk_uret.py"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
ILK = 1.00
GAP = 0.55
GAP_OGRENCI = 0.75

sen = json.loads((AD / "senaryo.json").read_text())
sure = json.loads((AD / "sureler.json").read_text())
assert len(sure) == len(sen["cumleler"]), (len(sure), len(sen["cumleler"]))

out = []
baslar: dict[str, list[float]] = {}
t = ILK
for e, c in zip(sure, sen["cumleler"]):
    for s, a, z in e["sozcukler"]:
        out.append({"cumle": e["i"], "sozcuk": s, "t0": round(t + a, 3), "t1": round(t + z, 3)})
    bit = t + e["sure"]
    baslar[str(e["i"])] = [round(t, 3), round(bit, 3)]
    t = bit + (GAP_OGRENCI if c["ses"] == "ogrenci" else GAP)
(AD / "sozcukler.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
(AD / "baslar.json").write_text(json.dumps(baslar, indent=0))
print(len(out), "sözcük ·", len(baslar), "cümle · son cümle bitişi", baslar[str(len(baslar))][1])

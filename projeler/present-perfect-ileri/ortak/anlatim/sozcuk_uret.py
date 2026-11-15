"""sozcukler.json üretici: sureler.json (cümle içi sözcük zamanları) + cümle başları (sn).
Whisper yok: sureler.json'daki sözcük payları el.py sentez raporundan gelir.
Çıktı biçimi ana projeyle aynı: [{cumle, sozcuk, t0, t1}] küresel sn. Kullanım: /usr/bin/python3 -I sozcuk_uret.py"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
# 16.11 DUZ3-0206I: c1 +0,4 · c3 +1,2 · c6 +0,2 sn kayma (0,1 sn ızgarası)
BASLAR = [1.0, 4.43, 18.92, 36.04, 53.4, 70.75, 75.42]
sure = json.loads((AD / "sureler.json").read_text())
out = []
for e, b in zip(sure, BASLAR):
    for s, a, z in e["sozcukler"]:
        out.append({"cumle": e["i"], "sozcuk": s, "t0": round(b + a, 3), "t1": round(b + z, 3)})
(AD / "sozcukler.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
print(len(out), "sözcük")

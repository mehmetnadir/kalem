"""sozcukler.json üretici: sureler.json (cümle içi sözcük zamanları) + cümle başları (sn).
Whisper yok: sureler.json'daki sözcük payları sentez raporundan gelir (ses yeniden sentezlenmedi).
Çıktı biçimi ana projeyle aynı: [{cumle, sozcuk, t0, t1}] küresel sn. Kullanım: /usr/bin/python3 -I sozcuk_uret.py"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
BASLAR = [1.0, 3.39, 17.8, 35.83, 51.35, 65.22, 69.55]  # 16.11 DUZ3-0209I: c3 +1,52 → c4–c5 +1,60; c5 +1,12 → c6–c7 +2,80
sure = json.loads((AD / "sureler.json").read_text())
out = []
for e, b in zip(sure, BASLAR):
    for s, a, z in e["sozcukler"]:
        out.append({"cumle": e["i"], "sozcuk": s, "t0": round(b + a, 3), "t1": round(b + z, 3)})
(AD / "sozcukler.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
print(len(out), "sözcük")

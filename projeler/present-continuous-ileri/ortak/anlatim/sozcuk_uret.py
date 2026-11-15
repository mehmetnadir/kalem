"""sozcukler.json üretici: sureler.json (cümle içi sözcük zamanları) + cümle başları (sn).
Whisper yok: sureler.json'daki sözcük payları sentez raporundan gelir (ses yeniden sentezlenmedi).
Çıktı biçimi ana projeyle aynı: [{cumle, sozcuk, t0, t1}] küresel sn. Kullanım: /usr/bin/python3 -I sozcuk_uret.py"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
BASLAR = [0.64, 3.71, 15.80, 31.13, 43.62, 55.63, 61.40]  # 16.11 DUZ3: c3 +0,96 sn → c4–c7 +1,00 sn (3 kare katı)
sure = json.loads((AD / "sureler.json").read_text())
out = []
for e, b in zip(sure, BASLAR):
    for s, a, z in e["sozcukler"]:
        out.append({"cumle": e["i"], "sozcuk": s, "t0": round(b + a, 3), "t1": round(b + z, 3)})
(AD / "sozcukler.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
print(len(out), "sözcük")

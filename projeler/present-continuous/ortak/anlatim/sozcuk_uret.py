"""sozcukler.json üretici: sureler.json (cümle içi sözcük zamanları) + cümle başları (sn).
Whisper yok: sureler.json'daki sözcük payları el.py sentez raporundan gelir.
Çıktı biçimi ana projeyle aynı: [{cumle, sozcuk, t0, t1}] küresel sn. Kullanım: /usr/bin/python3 -I sozcuk_uret.py"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
# 16.11 DUZ3-0201T: cümle 2 (12,54 sn) ve 7 (25,25 sn) yeniden sentezlendi; cümle 3–7 başı +1,04 (zincir: önceki bitiş + 0,55)
BASLAR = [1.0, 3.39, 16.48, 31.19, 47.02, 63.85, 67.76]
sure = json.loads((AD / "sureler.json").read_text())
out = []
for e, b in zip(sure, BASLAR):
    for s, a, z in e["sozcukler"]:
        out.append({"cumle": e["i"], "sozcuk": s, "t0": round(b + a, 3), "t1": round(b + z, 3)})
(AD / "sozcukler.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
print(len(out), "sözcük")

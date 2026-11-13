"""sozcukler.json üretici: sureler.json (cümle içi sözcük zamanları) + kur.baslar() (cümle başları, sn).
Whisper yok: sureler.json'daki sözcük payları sentez raporundan gelir (el.py with-timestamps hizalaması).
Çıktı biçimi ana projeyle aynı: [{cumle, sozcuk, t0, t1}] küresel sn. Kullanım: /usr/bin/python3 -I sozcuk_uret.py"""
import json
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
sys.path.insert(0, str(AD))
import kur  # noqa: E402

BASLAR = kur.baslar()
sure = json.loads((AD / "sureler.json").read_text())
out = []
for e in sure:
    b = BASLAR[e["i"]]
    for s, a, z in e["sozcukler"]:
        out.append({"cumle": e["i"], "sozcuk": s, "t0": round(b + a, 3), "t1": round(b + z, 3)})
(AD / "sozcukler.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
print(len(out), "sözcük")

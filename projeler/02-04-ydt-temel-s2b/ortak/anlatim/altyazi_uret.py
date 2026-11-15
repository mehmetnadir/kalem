#!/usr/bin/env python3
"""altyazi.json üretici (parça düzeyi): ortak/anlatim/senaryo.json (cümle parçaları) + sureler.json (sözcük zamanları)
+ sozcukler.json (küresel cümle başları) → [{cumle, dil, t0, t1, metin, konusan}].
S2-C (15.11): araclar/altyazi_uret.py kopyası. Parça sınırı sözcük sayısıyla DEĞİL, sureler.json `parcalar` alanından okunur.
Neden: `T-shirt` parçası sese `T shirt` gider, el.py o parçaya sözcük zamanı yazmaz; sayıyla bölme sonraki parçanın sözcüklerini
ona verir (ana ders cümle 3 ve 9'da altyazı ≈ 3 sn kaydı). Kullanım: /usr/bin/python3 -I projeler/<proje>/ortak/anlatim/altyazi_uret.py projeler/<proje>"""
import json
import re
import sys
from pathlib import Path

P = Path(sys.argv[1]).resolve()
A = P / "ortak" / "anlatim"
sen = json.loads((A / "senaryo.json").read_text())
sure = {s["i"]: s for s in json.loads((A / "sureler.json").read_text())}
soz = json.loads((A / "sozcukler.json").read_text())


def baslar() -> dict[int, float]:
    out: dict[int, float] = {}
    for no, s in sure.items():
        ilk = min(w["t0"] for w in soz if w["cumle"] == no)
        out[no] = round(ilk - s["sozcukler"][0][1], 3)
    return out


def sozcuk_sayisi(metin: str) -> int:
    return len([w for w in re.split(r"\s+", metin.strip()) if w])


B = baslar()
out = []
for i, c in enumerate(sen["cumleler"], 1):
    pz = sure[i]["parcalar"]  # S2-C: parça sınırı el.py sentez raporundan (sus dışı parça başına [baş, son])
    j = 0
    for dil, metin in c["parcalar"]:
        if dil == "sus":  # sessizlik parçası (metin = saniye): sözcüğü yok, altyazıya girmez
            continue
        a, z = pz[j]
        j += 1
        out.append({"cumle": i, "dil": dil, "t0": round(B[i] + a, 3), "t1": round(B[i] + z, 3), "metin": metin,
                    "konusan": c.get("ses", "ogretmen")})
(A / "altyazi.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
print(len(out), "parça →", A / "altyazi.json")

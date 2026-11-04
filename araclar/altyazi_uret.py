#!/usr/bin/env python3
"""altyazi.json üretici (parça düzeyi): ortak/anlatim/senaryo.json (cümle parçaları) + sureler.json (sözcük zamanları)
+ sozcukler.json (küresel cümle başları) → [{cumle, dil, t0, t1, metin, konusan}].
Parça sınırı sözcük sayısıyla bulunur: el.py parçaları sırayla sentezler, sözcük listesi aynı sırayı korur.
Kullanım: /usr/bin/python3 -I araclar/altyazi_uret.py projeler/<proje>   (çıktı: <proje>/ortak/anlatim/altyazi.json)"""
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
    sl = sure[i]["sozcukler"]
    k = 0
    for dil, metin in c["parcalar"]:
        n = sozcuk_sayisi(metin)
        dilim = sl[k:k + n]
        if not dilim:
            print(f"uyarı: cümle {i} parça '{metin[:30]}' için sözcük zamanı yok", file=sys.stderr)
            continue
        t0 = round(B[i] + dilim[0][1], 3)
        t1 = round(B[i] + dilim[-1][2], 3)
        out.append({"cumle": i, "dil": dil, "t0": t0, "t1": t1, "metin": metin, "konusan": c.get("ses", "ogretmen")})
        k += n
    if k != len(sl):
        print(f"uyarı: cümle {i} sözcük sayısı {len(sl)}, parçalardan {k} (parça sınırları kaymış olabilir)", file=sys.stderr)
(A / "altyazi.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
print(len(out), "parça →", A / "altyazi.json")

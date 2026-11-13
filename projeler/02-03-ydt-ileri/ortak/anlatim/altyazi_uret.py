"""altyazi.json üretici (parça düzeyi) — araclar/altyazi_uret.py'nin bu paket kopyası; fark: `sus` parçalarını atlar
(ortak sürüm sus değerinde çöker: float.strip). senaryo.json + sureler.json + sozcukler.json → [{cumle, dil, t0, t1, metin, konusan}].
Kullanım: /usr/bin/python3 -I altyazi_uret.py"""
import json
import re
from pathlib import Path

A = Path(__file__).resolve().parent
sen = json.loads((A / "senaryo.json").read_text())
sure = {s["i"]: s for s in json.loads((A / "sureler.json").read_text())}
soz = json.loads((A / "sozcukler.json").read_text())
B = {no: round(min(w["t0"] for w in soz if w["cumle"] == no) - s["sozcukler"][0][1], 3) for no, s in sure.items()}
out = []
for i, c in enumerate(sen["cumleler"], 1):
    sl = sure[i]["sozcukler"]
    k = 0
    for dil, metin in c["parcalar"]:
        if dil == "sus":
            continue
        n = len([w for w in re.split(r"\s+", metin.strip()) if w])
        dilim = sl[k:k + n]
        if not dilim:
            print(f"uyarı: cümle {i} parça '{metin[:30]}' için sözcük zamanı yok")
            continue
        out.append({"cumle": i, "dil": dil, "t0": round(B[i] + dilim[0][1], 3), "t1": round(B[i] + dilim[-1][2], 3),
                    "metin": metin, "konusan": c.get("ses", "ogretmen")})
        k += n
    if k != len(sl):
        print(f"uyarı: cümle {i} sözcük sayısı {len(sl)}, parçalardan {k}")
(A / "altyazi.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
print(len(out), "parça →", A / "altyazi.json")

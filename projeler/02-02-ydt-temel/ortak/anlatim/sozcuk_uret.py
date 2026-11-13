"""sozcukler.json üretici: sureler.json (cümle içi sözcük zamanları) + cümle arası sessizlik → küresel sn.
Cümle başları sabit dizi değil, hesaptır (K23 soğuk açılış):
  başlar[1] = 1.00 − (cümle 1'in ilk sözcük payı)            # ilk söz tam 1,00 sn'de
  başlar[i+1] = başlar[i] + sure[i] + ARA (+ SORU_EK, cümle i öğrenci sorusuysa)
ARA 0,55 sn; öğrenci cümlesinden sonra +0,15 (toplam 0,7 sn, taslak süre ölçüsü).
Çıktılar: sozcukler.json [{cumle, sozcuk, t0, t1}] · cumle-baslar.json [{i, baslar, biter, ilk_soz, ses}].
Whisper yok: sözcük payları sentez raporundan gelir. Kullanım: /usr/bin/python3 -I sozcuk_uret.py"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
ILK_SOZ = 1.00
ARA = 0.55
OGRENCI_EK = 0.15

sure = json.loads((AD / "sureler.json").read_text())
sen = json.loads((AD / "senaryo.json").read_text())["cumleler"]
assert len(sure) == len(sen), (len(sure), len(sen))


def ilk_pay(e: dict) -> float:
    return e["sozcukler"][0][1] if e["sozcukler"] else 0.0


baslar: dict[int, float] = {}
t = ILK_SOZ - ilk_pay(sure[0])
for e, c in zip(sure, sen):
    baslar[e["i"]] = round(t, 3)
    t += e["sure"] + ARA + (OGRENCI_EK if c["ses"] == "ogrenci" else 0.0)

out = []
bas_json = []
for e, c in zip(sure, sen):
    b = baslar[e["i"]]
    for s, a, z in e["sozcukler"]:
        out.append({"cumle": e["i"], "sozcuk": s, "t0": round(b + a, 3), "t1": round(b + z, 3)})
    bas_json.append({"i": e["i"], "baslar": b, "biter": round(b + e["sure"], 3),
                     "ilk_soz": round(b + ilk_pay(e), 3), "ses": c["ses"]})
(AD / "sozcukler.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
(AD / "cumle-baslar.json").write_text(json.dumps(bas_json, ensure_ascii=False, indent=0))
print(len(out), "sözcük ·", len(bas_json), "cümle · anlatım biter", bas_json[-1]["biter"], "sn")

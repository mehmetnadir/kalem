"""sozcukler.json üretici: sureler.json (cümle içi sözcük zamanları) + senaryo.json (konuşan, bölüm) → küresel sn.
Cümle başları sabit dizi değil, hesaplanır: ilk söz 1,00 sn (K23 soğuk açılış); cümleler arası sessizlik
ARA 0,55 sn; öğrenci cümlesinden sonra 0,75 sn (soru anı duraklaması); bölüm değişiminde 1,00 sn (perde).
Whisper yok: sözcük payları el.py sentez raporundan (sureler.json) gelir. Çıktı: [{cumle, sozcuk, t0, t1}] küresel sn.
Kullanım: /usr/bin/python3 -I sozcuk_uret.py"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
ILK_SOZ = 1.00
ARA, OGRENCI, BOLUM = 0.55, 0.75, 1.00


def baslar() -> list[float]:
    sure = json.loads((AD / "sureler.json").read_text())
    sen = json.loads((AD / "senaryo.json").read_text())["cumleler"]
    assert len(sure) == len(sen), "sureler.json ile senaryo.json cümle sayısı farklı"
    out = [round(ILK_SOZ - sure[0]["sozcukler"][0][1], 3)]
    for i in range(1, len(sure)):
        bitis = out[-1] + sure[i - 1]["sure"]
        ara = ARA
        if sen[i - 1]["ses"] == "ogrenci":
            ara = max(ara, OGRENCI)
        if sen[i]["bolum"] != sen[i - 1]["bolum"]:
            ara = max(ara, BOLUM)
        out.append(round(bitis + ara, 3))
    return out


if __name__ == "__main__":
    sure = json.loads((AD / "sureler.json").read_text())
    out = []
    for e, b in zip(sure, baslar()):
        for s, a, z in e["sozcukler"]:
            out.append({"cumle": e["i"], "sozcuk": s, "t0": round(b + a, 3), "t1": round(b + z, 3)})
    (AD / "sozcukler.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
    print(len(out), "sözcük")

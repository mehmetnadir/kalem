"""altyazi.json üretici (S1 Shorts): senaryo parçaları + sözcük zamanlarından parça başı/sonu.
Her parça (senaryo `cumleler[i].parcalar` öğesi) için sozcukler.json'daki ardışık sözcükler eşleştirilir:
t0 = ilk sözcüğün t0'ı, t1 = son sözcüğün t1'i. Sözcük sayısı tutmazsa cümle düzeyine düşer
(sureler.json parça aralığı + cümle başlangıcı).
Kullanım: /usr/bin/python3 -I altyazi_uret.py   (çıktı: altyazi.json, bu dizinde)"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent


def uret() -> list[dict]:
    sen = json.loads((AD / "senaryo.json").read_text())
    soz = json.loads((AD / "sozcukler.json").read_text())
    sure = {s["i"]: s for s in json.loads((AD / "sureler.json").read_text())}
    cikti: list[dict] = []
    for no, c in enumerate(sen["cumleler"], start=1):
        kel = [w for w in soz if w["cumle"] == no]
        toplam = sum(len(m.split()) for _, m in c["parcalar"])
        bas = kel[0]["t0"] - sure[no]["sozcukler"][0][1]      # cümle başlangıcı (küresel sn)
        k = 0
        for j, (dil, metin) in enumerate(c["parcalar"]):
            n = len(metin.split())
            if toplam == len(kel):
                t0, t1 = kel[k]["t0"], kel[k + n - 1]["t1"]
            else:
                a, b = sure[no]["parcalar"][j]
                t0, t1 = bas + a, bas + b
            k += n
            cikti.append({"cumle": no, "dil": dil, "t0": round(t0, 3), "t1": round(t1, 3),
                          "metin": metin, "konusan": c["ses"]})
    return cikti


if __name__ == "__main__":
    liste = uret()
    (AD / "altyazi.json").write_text(json.dumps(liste, ensure_ascii=False, indent=1) + "\n")
    for a in liste:
        print(a["cumle"], a["dil"], a["t0"], a["t1"], a["metin"])

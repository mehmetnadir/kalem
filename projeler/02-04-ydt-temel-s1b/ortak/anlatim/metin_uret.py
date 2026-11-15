"""METIN.md üretici: senaryo.json + sozcukler.json + baslar.json + sureler.json -> METIN.md (örnek paket biçimi).
Kullanım: /usr/bin/python3 -I metin_uret.py"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
sen = json.loads((AD / "senaryo.json").read_text())
soz = json.loads((AD / "sozcukler.json").read_text())
sure = {s["i"]: s for s in json.loads((AD / "sureler.json").read_text())}
baslar = {int(k): v for k, v in json.loads((AD / "baslar.json").read_text()).items()}
ROL = {"ogretmen": "öğretmen", "ogrenci": "öğrenci"}

L = ["# Anlatım metni ve zamanlar (küresel saniye; video 0 = anlatim.wav 0; soğuk açılış: sahne 01 3 sn, ilk söz 1 sn)", "",
     "| # | başlar | biter | konuşan | metin |", "|---|---|---|---|---|"]
for i, c in enumerate(sen["cumleler"], 1):
    b, e = baslar[i]
    L.append(f"| {i} | {b:.2f} | {e:.2f} | {ROL[c['ses']]} | {c['metin']} |")
L += ["", "## Parçalar (cümle içi dil/duraklama parçaları, küresel sn)", ""]
for i in sorted(baslar):
    b = baslar[i][0]
    pz = ", ".join(f"[{b + a:.2f}–{b + z:.2f}]" for a, z in sure[i]["parcalar"])
    L.append(f"- cümle {i}: {pz}")
L += ["", "## Sözcükler (küresel sn): `ortak/anlatim/sozcukler.json` — {cumle, sozcuk, t0, t1}; yerel kare = round((t − t_bas) × 30)"]
for i in sorted(baslar):
    L += ["", f"### cümle {i}", " ".join(f"{w['sozcuk']}({w['t0']:.2f})" for w in soz if w["cumle"] == i)]
(AD / "METIN.md").write_text("\n".join(L) + "\n")
print("METIN.md", len(L), "satır")

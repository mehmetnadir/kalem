"""METIN.md üretici: senaryo.json + sureler.json + sozcukler.json → METIN.md (başlar/biter, parçalar, bölümler, sözcükler).
Kullanım: /usr/bin/python3 -I metin_uret.py"""
import json
from pathlib import Path

A = Path(__file__).resolve().parent
sen = json.loads((A / "senaryo.json").read_text())["cumleler"]
sure = json.loads((A / "sureler.json").read_text())
soz = json.loads((A / "sozcukler.json").read_text())
ad = {"ogretmen": "öğretmen", "ogrenci": "öğrenci"}
BOL = {1: "1 Kanca", 2: "2 Karar anahtarı", 3: "3 Karşıt çift", 4: "4 Dört sınav kökü", 5: "5 Tuzak", 6: "6 Ara özet",
       7: "7 Mini soru", 8: "8 Kapanış"}
by = {}
for w in soz:
    by.setdefault(w["cumle"], []).append(w)
bas = {n: round(by[n][0]["t0"] - sure[n - 1]["sozcukler"][0][1], 3) for n in by}
bit = {n: by[n][-1]["t1"] for n in by}
L = ["# Anlatım metni ve zamanlar (küresel saniye; video 0 = anlatim.wav 0; soğuk açılış: ilk söz 1 sn; sahne 01 = cümle 1)", "",
     "| # | bölüm | başlar | biter | konuşan | metin |", "|---|---|---|---|---|---|"]
for i, c in enumerate(sen, 1):
    L.append(f"| {i} | {BOL[c['bolum']]} | {bas[i]:.2f} | {bit[i]:.2f} | {ad[c['ses']]} | {c['metin']} |")
L += ["", "## Bölümler (gerçekleşen süre = ilk cümle başı → son cümle sonu)", "", "| bölüm | cümleler | başlar | biter | süre (sn) |", "|---|---|---|---|---|"]
for b, adb in BOL.items():
    ks = [i for i, c in enumerate(sen, 1) if c["bolum"] == b]
    L.append(f"| {adb} | {ks[0]}–{ks[-1]} | {bas[ks[0]]:.2f} | {bit[ks[-1]]:.2f} | {bit[ks[-1]] - bas[ks[0]]:.1f} |")
L += ["", "## Parçalar (cümle içi dil parçaları, küresel sn; `sus` parçaları dışarıda)", ""]
for i in sorted(by):
    L.append(f"- cümle {i}: " + ", ".join(f"[{bas[i] + a:.2f}–{bas[i] + z:.2f}]" for a, z in sure[i - 1]["parcalar"]))
L += ["", "## Sözcükler (küresel sn): `ortak/anlatim/sozcukler.json` — {cumle, sozcuk, t0, t1}; yerel kare = round((t − t_bas) × 30)", ""]
for i in sorted(by):
    L += [f"### cümle {i}", " ".join(f"{w['sozcuk']}({w['t0']:.2f})" for w in by[i]), ""]
(A / "METIN.md").write_text("\n".join(L))
print("METIN.md", len(sen), "cümle")

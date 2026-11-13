"""zaman.json üretici: BRIEF.md "Sahne planı" (SAHNELER) + sozcukler.json (sözcük zamanları) → ../../zaman.json.
Sahne sınırı = sahnenin son cümlesinin son sözcük sonu (sahne 01 = cümle 1: 4,12 sn; ilk söz 1,00 sn, K23 ≤3 sn giriş ölçüsü cümle 3,1 sn sürdüğü için aşıldı, rapora yazıldı).
Son sahne t_son = anlatım sonu + 0,5 sn. kare = icerik_kare + 12 (gecis_kare); son sahne icerik_kare + 30 (örnek paket biçimi).
Sahne dizinleri OLUŞTURULMAZ (P2). Kullanım: /usr/bin/python3 -I zaman_uret.py"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
PROJE = AD.parent.parent
FPS, N = 30, 12
# (klasör, motor, ad, bölüm, ilk cümle, son cümle)
SAHNELER = [
    ("01-hyperframes-giris", "HyperFrames", "Giriş", "1 Kanca", 1, 1),
    ("02-paperjs-kanca", "Paper.js", "Kanca", "1 Kanca", 2, 2),
    ("03-hyperframes-anahtar", "HyperFrames", "Karar anahtarı", "2 Karar anahtarı", 3, 3),
    ("04-canvas-gelecek", "Düz canvas", "Gelecek ayrımı", "3 Karşıt çift", 4, 6),
    ("05-hyperframes-kok1", "HyperFrames", "Kök 1", "4 Dört sınav kökü", 7, 7),
    ("06-hyperframes-kok2", "HyperFrames", "Kök 2", "4 Dört sınav kökü", 8, 8),
    ("07-hyperframes-kok3", "HyperFrames", "Kök 3", "4 Dört sınav kökü", 9, 9),
    ("08-hyperframes-kok4", "HyperFrames", "Kök 4", "4 Dört sınav kökü", 10, 10),
    ("09-paperjs-tuzak", "Paper.js", "Tuzak", "5 Tuzak", 11, 13),
    ("10-hyperframes-ozet", "HyperFrames", "Ara özet", "6 Ara özet", 14, 14),
    ("11-hyperframes-mini-soru", "HyperFrames", "Mini soru", "7 Mini soru", 15, 17),
    ("12-canvas-kapanis", "Düz canvas", "Kapanış", "8 Kapanış", 18, 18),
]
KOK_ARASI_FADE = {5, 6, 7}  # kök 1→2, 2→3, 3→4 aynı bölüm: fade; diğerleri BookFlip

soz = json.loads((AD / "sozcukler.json").read_text())
bit = {}
for w in soz:
    bit[w["cumle"]] = max(bit.get(w["cumle"], 0), w["t1"])
sahneler = []
t_bas = 0.0
for k, (klasor, motor, ad, bolum, c0, c1) in enumerate(SAHNELER, 1):
    son = k == len(SAHNELER)
    t_son = (round(bit[c1] + 0.5, 2) if son else round(bit[c1], 2))
    icerik = round((t_son - t_bas) * FPS)
    s = {"no": k, "klasor": klasor, "motor": motor, "kare": icerik + (30 if son else N), "t_bas": round(t_bas, 2),
         "t_son": t_son, "icerik_kare": icerik}
    if not son:
        s["gecis"] = "fade" if k in KOK_ARASI_FADE else "BookFlip"
    s["ad"] = ad
    s["bolum"] = bolum
    s["cumleler"] = [c0, c1] if c0 != c1 else [c0]
    sahneler.append(s)
    t_bas = t_son
z = {"fps": FPS, "genislik": 1920, "yukseklik": 1080, "gecis_kare": N, "tema": "acik",
     "anlatim": "ortak/anlatim/anlatim.m4a", "sahneler": sahneler}
(PROJE / "zaman.json").write_text(json.dumps(z, ensure_ascii=False, indent=2) + "\n")
print(len(sahneler), "sahne, son t_son", sahneler[-1]["t_son"])

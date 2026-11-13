"""zaman.json üretici: sahne planı (BRIEF "Sahne planı") + baslar.json (cümle başı/bitişi, sozcuk_uret.py).
Kural: sahne t_son = sahnenin son cümlesinin bitişi; sahne t_bas = önceki sahnenin t_son'u (ilk sahne 0,0).
Giriş sahnesi (K23, giriş ≤ 3 sn): t_son 3,0 (cümle 1'in kalanı sahne 02'de konuşulur).
Son sahne t_son = son cümle bitişi + 0,5. icerik_kare = round((t_son − t_bas) × 30); kare = icerik_kare + 12
(giriş geçişi, gecis_kare); son sahne kare = icerik_kare + 30 (örnek paketlerle aynı kuyruk).
Kullanım: /usr/bin/python3 -I zaman_uret.py   (kur.py zaman.json'un son t_son'unu toplam süre sayar)"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
PROJE = AD.parent.parent
FPS, N = 30, 12

# (klasör, motor, ad, bölüm, son cümle no, geçiş) — sahne planı BRIEF.md ile aynı
SAHNE = [
    ("01-hyperframes-giris", "HyperFrames", "Giriş", "Giriş", 1, "BookFlip"),
    ("02-paperjs-kanca", "Paper.js", "Kanca", "Kanca", 2, "BookFlip"),
    ("03-paperjs-ornek1", "Paper.js", "Örnek 1", "Örnek 1", 3, "BookFlip"),
    ("04-canvas-ornek2", "Düz canvas", "Örnek 2", "Örnek 2", 4, "BookFlip"),
    ("05-canvas-ornek3", "Düz canvas", "Örnek 3", "Örnek 3", 5, "BookFlip"),
    ("06-hyperframes-soru1", "HyperFrames", "Soru anı 1", "Soru 1", 7, "BookFlip"),
    ("07-hyperframes-kural", "HyperFrames", "Kural kartı", "Kural", 8, "BookFlip"),
    ("08-canvas-karsit1", "Düz canvas", "Karşıt çift 1", "Karşıt çift 1", 9, "BookFlip"),
    ("09-canvas-karsit2", "Düz canvas", "Karşıt çift 2-3", "Karşıt çift 2", 11, "BookFlip"),
    ("10-hyperframes-tuzak", "HyperFrames", "Tuzak ve soru anı 2", "Tuzak", 13, "BookFlip"),
    ("11-canvas-tuzak-fiiller", "Düz canvas", "Tuzak fiilleri", "Tuzak fiilleri", 14, "BookFlip"),
    ("12-hyperframes-ozet", "HyperFrames", "Ara özet", "Özet", 15, "BookFlip"),
    ("13-hyperframes-mini-soru", "HyperFrames", "Mini soru", "Mini soru", 18, "fade"),
    ("14-hyperframes-kapanis", "HyperFrames", "Kapanış", "Kapanış", 19, None),
]
GIRIS_SN = 3.0

baslar = json.loads((AD / "baslar.json").read_text())
bit = {int(k): v[1] for k, v in baslar.items()}
sahneler = []
t_bas = 0.0
for no, (klasor, motor, ad, bolum, son_c, gecis) in enumerate(SAHNE, 1):
    t_son = bit[son_c]
    if no == 1:
        t_son = min(t_son, GIRIS_SN)
    if no == len(SAHNE):
        t_son = bit[son_c] + 0.5
    t_son = round(t_son, 2)
    icerik = int((t_son - t_bas) * FPS + 0.5)
    kare = icerik + (30 if no == len(SAHNE) else N)
    s = {"no": no, "klasor": klasor, "motor": motor, "kare": kare, "t_bas": round(t_bas, 2), "t_son": t_son,
         "icerik_kare": icerik}
    if gecis:
        s["gecis"] = gecis
    s.update({"ad": ad, "bolum": bolum})
    sahneler.append(s)
    t_bas = t_son
z = {"fps": FPS, "genislik": 1920, "yukseklik": 1080, "gecis_kare": N, "tema": "acik",
     "anlatim": "ortak/anlatim/anlatim.m4a", "sahneler": sahneler}
(PROJE / "zaman.json").write_text(json.dumps(z, ensure_ascii=False, indent=2) + "\n")
for s in sahneler:
    print(s["no"], s["klasor"], s["t_bas"], s["t_son"], s["kare"])
print("toplam sn", sahneler[-1]["t_son"])

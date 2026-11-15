"""zaman.json üretici: sahne planı (BRIEF "Sahne planı") + baslar.json (cümle başı/bitişi, sozcuk_uret.py).
Kural: sahne t_son = sahnenin son cümlesinin bitişi; sahne t_bas = önceki sahnenin t_son'u (ilk sahne 0,0).
Giriş sahnesi (K23, giriş ≤ 3 sn): t_son 3,0 (cümle 1'in kalanı sahne 02'de konuşulur).
Son sahne t_son = son cümle bitişi + 1,0 (S1 kuralı, present-continuous-ileri-s1). icerik_kare = round((t_son − t_bas) × 30);
kare = icerik_kare + 12 (giriş geçişi, gecis_kare); son sahne kare = icerik_kare + 30 (örnek paketlerle aynı kuyruk).
S1 (15.11, S1-C): 3 sahne, 1080×1920; geçiş birlestir --gecis ile (örnekteki gibi sahnede yok). Hikâye karesi `hikaye`
alanında, sahneler[] dışında: birlestir.py ve kur.py yalnız sahneler[] okur, hikâye zaman çizelgesine girmez.
S3 (15.11, S3-C): S1 kopyası; sahne 02 HyperFrames (cümle 1 sonu + 2 + 3), sahne 03 cümle 4. Çok sürüm: hikâye A `hikaye`
alanında, kapak B/C ve hikâye B `duragan` listesinde (ikisi de sahneler[] dışında, S1 zaman.json biçimi).
Huni v2 (15.11, V2-S3-C): 4 sahne — 01 kanca → 02 değer → 08 kaydet (cümle 4, öğretmen) → 03 çağrı (cümle 5, öğrenci).
Kullanım: /usr/bin/python3 -I zaman_uret.py   (kur.py zaman.json'un son t_son'unu toplam süre sayar)"""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
PROJE = AD.parent.parent
FPS, N = 30, 12

# (klasör, motor, ad, bölüm, son cümle no, geçiş) — sahne planı BRIEF.md ile aynı
SAHNE = [
    ("01-hyperframes-kapak", "HyperFrames", "Kapak", "Kapak", 1, None),
    ("02-hyperframes-ornek", "HyperFrames", "Örnek", "Örnek", 3, None),
    ("08-hyperframes-kaydet", "HyperFrames", "Kaydet", "Kaydet", 4, None),
    ("03-hyperframes-cta", "HyperFrames", "Çağrı", "Çağrı", 5, None),
]
NOT = "durağan kare; zaman çizelgesine girmez"
HIKAYE = {"klasor": "04-hyperframes-hikaye", "motor": "HyperFrames", "kare": 1, "cikti": "hikaye-a.png",
          "ad": "Hikâye karesi A (kural kartı + Kaydet)", "not": "anlatımdan bağımsız " + NOT + "; hikaye.png = aynı dosyanın kopyası"}
DURAGAN = [{"klasor": k, "motor": "HyperFrames", "kare": 1, "cikti": c, "ad": a, "not": NOT} for k, c, a in [
    ("05-hyperframes-kapak-b", "kapak-b.png", "Kapak B (soru)"),
    ("06-hyperframes-kapak-c", "kapak-c.png", "Kapak C (karşıt çift)"),
    ("07-hyperframes-hikaye-b", "hikaye-b.png", "Hikâye karesi B (soru + cevap + Kaydet)")]]
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
        t_son = bit[son_c] + 1.0
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
z = {"fps": FPS, "genislik": 1080, "yukseklik": 1920, "gecis_kare": N, "tema": "acik",
     "anlatim": "ortak/anlatim/anlatim.m4a", "sahneler": sahneler, "hikaye": HIKAYE, "duragan": DURAGAN}
(PROJE / "zaman.json").write_text(json.dumps(z, ensure_ascii=False, indent=2) + "\n")
for s in sahneler:
    print(s["no"], s["klasor"], s["t_bas"], s["t_son"], s["kare"])
print("toplam sn", sahneler[-1]["t_son"])

#!/usr/bin/env python3
"""Sürüm durumlarını çıktıdan türetir: projenin cikti.mp4 + cikti-koyu.mp4 varsa o sürüm 'hazir' olur.
Proje = sürümün `proje` alanı; yoksa `onizleme` yolundaki /p/<proje>/. Yalnız planli/uretimde → hazir yazar.
Kullanım: /usr/bin/python3 -I araclar/surum-durum.py [--yaz]   (yazmadan rapor; --yaz dosyaları günceller)"""
import json
import re
import sys
from pathlib import Path

K = Path(__file__).resolve().parent.parent
YAZ = "--yaz" in sys.argv
for sf in sorted((K / "projeler").glob("*/surumler.json")):
    v = json.loads(sf.read_text(encoding="utf-8"))
    degisti = False
    for s in v.get("surumler", []):
        proje = s.get("proje")
        if not proje:
            m = re.match(r"/p/([^/]+)/", s.get("onizleme") or "")
            proje = m.group(1) if m else None
        if not proje:
            continue
        d = K / "projeler" / proje
        hazir = (d / "cikti.mp4").exists() and (d / "cikti-koyu.mp4").exists()
        if hazir and s.get("durum") in ("planli", "uretimde"):
            print(f"{sf.parent.name:32s} {s['kimlik']:18s} {s['durum']} → hazir  ({proje})")
            s["durum"] = "hazir"
            degisti = True
        elif not hazir and s.get("durum") not in ("hazir", "iptal", "kapali", "onay"):
            print(f"{sf.parent.name:32s} {s['kimlik']:18s} {s['durum']} (çıktı yok: {proje})")
    if degisti and YAZ:
        sf.write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("yazıldı" if YAZ else "kuru koşu (--yaz ile uygula)")

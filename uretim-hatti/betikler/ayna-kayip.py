#!/usr/bin/python3 -I
"""Ayna yüklemesinde kaybolan dosyalar: en yeni .eski ağacında olup güncel aynada olmayan dosyaları listeler.
--kopyala verilirse kayıp dosyayı worktree paketine (yoksa) kopyalar; var olanın üstüne yazmaz.
Kullanım: ayna-kayip.py [--kopyala] <paket>…"""
import os
import shutil
import sys
from pathlib import Path

AYNA = Path("/var/www/videokayit/storage/kontrol-ayna")
K = Path("/home/sef/01dev/_worktrees/kalem-0204/projeler")
kopyala = "--kopyala" in sys.argv


def dosyalar(kok: Path) -> set[str]:
    cikti: set[str] = set()
    for dizin, _alt, adlar in os.walk(kok):
        for ad in adlar:
            cikti.add(str((Path(dizin) / ad).relative_to(kok)))
    return cikti


for paket in [a for a in sys.argv[1:] if not a.startswith("--")]:
    guncel = AYNA / "projeler" / paket
    eskiler = sorted((AYNA / ".eski").glob(f"projeler__{paket}.eski-*"), key=lambda p: p.name, reverse=True)
    if not guncel.is_dir() or not eskiler:
        print(f"{paket}: güncel {'var' if guncel.is_dir() else 'YOK'} · eski {len(eskiler)}")
        continue
    eski = eskiler[0]
    kayip = sorted(dosyalar(eski) - dosyalar(guncel))
    ozet: dict[str, int] = {}
    kopya = 0
    for yol in kayip:
        uz = yol.rsplit(".", 1)[-1]
        ozet[uz] = ozet.get(uz, 0) + 1
        hedef = K / paket / yol
        if kopyala and not hedef.exists():
            hedef.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(eski / yol, hedef)
            kopya += 1
    onemli = [y for y in kayip if not ("/k/" in y and y.endswith(".png"))]
    print(f"{paket}: kayıp {len(kayip)} {ozet} · kopyalanan {kopya} · k/ dışı: {onemli[:6]}")

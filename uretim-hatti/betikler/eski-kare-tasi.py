#!/usr/bin/env python3
"""Huni v2 paketlerinde k/ altında kalan v1 QA karelerini bulur (üst 0–250 bandı boş değilse v1) ve Silinecekler'e taşır."""
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageStat

K = Path("/home/sef/01dev/_worktrees/kalem-0204/projeler")
HEDEF = Path("/home/sef/Silinecekler/2026-11-15-huni-v2/k-eski")
kuru = "--kuru" in sys.argv
for paket in [a for a in sys.argv[1:] if not a.startswith("--")]:
    sahneler = K / paket / "sahneler"
    kareler = sorted(list(sahneler.glob("*/k/*.png")) + list(sahneler.glob("*/k/*/*.png")))
    for png in kareler:
        g = Image.open(png)
        if g.size != (1080, 1920):
            continue
        bant = g.convert("L").crop((40, 10, 1040, 250))
        sapma = ImageStat.Stat(bant).stddev[0]
        if sapma > 12:
            goreli = png.relative_to(K)
            print(f"v1 {sapma:5.1f} {goreli}")
            if not kuru:
                h = HEDEF / goreli
                h.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(png), str(h))

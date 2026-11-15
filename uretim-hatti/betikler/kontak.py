#!/usr/bin/env python3
"""Kontak sayfası: kip 'film' (kısa paket sahne kareleri + türevler) ya da 'kapak' (ders kapakları)."""
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw

K = Path("/home/sef/01dev/_worktrees/kalem-0204/projeler")


def sayi(p: Path) -> float:
    m = re.search(r"-([0-9.]+)\.png$", p.name)
    return float(m.group(1)) if m else 0.0


def diz(yollar: list[Path], w: int, h: int, sutun: int, cikti: str) -> None:
    satir = (len(yollar) + sutun - 1) // sutun
    sayfa = Image.new("RGB", (sutun * (w + 6) + 6, satir * (h + 22) + 6), "#808080")
    ciz = ImageDraw.Draw(sayfa)
    for i, y in enumerate(yollar):
        x0 = 6 + (i % sutun) * (w + 6)
        y0 = 6 + (i // sutun) * (h + 22)
        if y.exists():
            g = Image.open(y).convert("RGB")
            g.thumbnail((w, h))
            sayfa.paste(g, (x0, y0))
        ciz.text((x0, y0 + h + 4), y.name if y.exists() else f"YOK {y.name}", fill="white")
    sayfa.save(cikti)
    print(cikti, sayfa.size, len(yollar))


def film(paket: str, cikti: str) -> None:
    kok = K / paket
    z = json.loads((kok / "zaman.json").read_text())
    sahneler = [s.get("klasor") for s in z.get("sahneler", [])]
    yollar: list[Path] = []
    for s in sahneler:
        kareler = sorted((kok / "sahneler" / str(s) / "k").glob("*.png"), key=sayi)
        kareler = [k for k in kareler if re.search(r"-[0-9.]+\.png$", k.name)]
        if len(kareler) > 3:
            kareler = [kareler[0], kareler[len(kareler) // 2], kareler[-1]]
        yollar += kareler
    yollar += [kok / n for n in ("kapak-a.png", "kapak-b.png", "kapak-c.png", "hikaye-a.png", "hikaye-b.png")]
    diz(yollar, 270, 480, 9, cikti)


def kapak(cikti: str, dersler: list[str]) -> None:
    yatay: list[Path] = []
    dikey: list[Path] = []
    for d in dersler:
        yatay += [K / d / "kapak.png", K / d / "kapak-koyu.png"]
        dikey += [K / f"{d}-dikey" / "kapak.png", K / f"{d}-dikey" / "kapak-koyu.png"]
    diz(yatay, 480, 270, 4, cikti + "-yatay.png")
    diz(dikey, 216, 384, 10, cikti + "-dikey.png")


if sys.argv[1] == "film":
    film(sys.argv[2], sys.argv[3])
else:
    kapak(sys.argv[2], sys.argv[3:])

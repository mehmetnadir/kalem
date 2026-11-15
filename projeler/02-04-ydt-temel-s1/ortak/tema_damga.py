#!/usr/bin/python3
"""Sahne çıktısına tema adını yazar: kontrol.png üstüne tema şeridi, RAPOR.md'ye 'Tema:' satırı.
  /usr/bin/python3 tema_damga.py <sahne_dizini> acik|koyu
PIL gerekir (kullanıcı site-packages; -I ile çalışmaz). PIL yoksa yalnız RAPOR.md yazılır."""
from __future__ import annotations
import os, re, sys

FONTLAR = ("/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Menlo.ttc")


def rapor_satiri(metin: str, tema: str) -> str:
    """RAPOR.md metninde 'Tema:' satırı varsa değiştirir, yoksa başlığın (1. satır) altına ekler."""
    satir = f"Tema: {tema}"
    if re.search(r"^Tema: .*$", metin, flags=re.M):
        return re.sub(r"^Tema: .*$", satir, metin, count=1, flags=re.M)
    ilk, _, geri = metin.partition("\n")
    return f"{ilk}\n\n{satir}\n{geri}" if ilk else satir + "\n"


def damgala(yol: str, tema: str) -> bool:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return False
    f = next((ImageFont.truetype(p, 20) for p in FONTLAR if os.path.exists(p)), ImageFont.load_default())
    src = Image.open(yol).convert("RGB")   # künyeyi örtmesin: üste 30 px'lik siyah şerit eklenir
    im = Image.new("RGB", (src.size[0], src.size[1] + 30), (0, 0, 0)); im.paste(src, (0, 30))
    ImageDraw.Draw(im).text((7, 4), f"tema: {tema}", font=f, fill=(255, 255, 255))
    im.save(yol); return True


def main(argv: list[str]) -> None:
    d, tema = argv[1], argv[2]
    k = os.path.join(d, "kontrol.png")
    if os.path.exists(k) and not damgala(k, tema): print("uyarı: PIL yok, kontrol.png damgasız")
    r = os.path.join(d, "RAPOR.md")
    if os.path.exists(r):
        m = open(r, encoding="utf-8").read(); open(r, "w", encoding="utf-8").write(rapor_satiri(m, tema))


if __name__ == "__main__":
    main(sys.argv)

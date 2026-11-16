#!/usr/bin/python3 -I
"""duz-istem-uret.py <kod> <paket> --hukum <yol> [--kapsam hepsi] [--cikti <yol>]

DUZ şablonunu (istemler/sablon/DUZ.md) doldurur. Hükümdeki `hayır` satırlarını (kalın dahil) "İş listesi" olarak yazar.
Sayım mantığı ders-sonraki.sh ile aynıdır: `| hayır` ile başlayan hücre, aynı satırda `| evet |` hücresi yok.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SABLON = Path(__file__).resolve().parent.parent / "istemler" / "sablon" / "DUZ.md"
KAPSAMLAR = ("cumle-ses", "sahne-kare", "kapak-yayin", "hepsi")
HAYIR = re.compile(r"^\|.*\| *(\*\*)?hayır(\*\*)?( |\||\()")
EVET = re.compile(r"\| *(\*\*)?evet(\*\*)? *\|")


def hayir_satirlari(metin: str) -> list[tuple[str, str]]:
  """(kimlik, satır) listesi; kimlik = ilk hücre."""
  sonuc: list[tuple[str, str]] = []
  for satir in metin.splitlines():
    if not HAYIR.search(satir) or EVET.search(satir):
      continue
    hucreler = [h.strip() for h in satir.strip().strip("|").split("|")]
    kimlik = hucreler[0].replace("**", "").strip() if hucreler else "?"
    sonuc.append((kimlik or "?", satir.strip()))
  return sonuc


def is_listesi(satirlar: list[tuple[str, str]]) -> str:
  if not satirlar:
    return "Hükümde `hayır` satırı yok. İş yok; raporda bunu yaz."
  cikti = [f"Hükümde {len(satirlar)} `hayır` satırı var. Her biri için rapor tablosunda bir satır yaz.", ""]
  for i, (kimlik, satir) in enumerate(satirlar, 1):
    cikti.append(f"{i}. **{kimlik}** — {satir}")
  return "\n".join(cikti)


def uret(kod: str, paket: str, hukum: Path, kapsam: str) -> str:
  if kapsam not in KAPSAMLAR:
    raise ValueError(f"kapsam geçersiz: {kapsam} (olası: {', '.join(KAPSAMLAR)})")
  if not hukum.is_file():
    raise FileNotFoundError(f"hüküm dosyası yok: {hukum}")
  if not SABLON.is_file():
    raise FileNotFoundError(f"şablon yok: {SABLON}")
  govde = SABLON.read_text(encoding="utf-8")
  yer = {
    "{IS_LISTESI}": is_listesi(hayir_satirlari(hukum.read_text(encoding="utf-8"))),
    "{HUKUM_YOLU}": str(hukum),
    "{KAPSAM}": kapsam,
    "{PAKET}": paket,
    "{KOD}": kod,
  }
  for anahtar, deger in yer.items():
    govde = govde.replace(anahtar, deger)
  return govde


def main(argv: list[str]) -> int:
  ap = argparse.ArgumentParser(description=__doc__)
  ap.add_argument("kod")
  ap.add_argument("paket")
  ap.add_argument("--hukum", required=True)
  ap.add_argument("--kapsam", default="hepsi")
  ap.add_argument("--cikti")
  a = ap.parse_args(argv)
  try:
    metin = uret(a.kod, a.paket, Path(a.hukum), a.kapsam)
  except (ValueError, FileNotFoundError) as e:
    print(f"duz-istem-uret: {e}", file=sys.stderr)
    return 2
  if a.cikti:
    Path(a.cikti).write_text(metin, encoding="utf-8")
  else:
    sys.stdout.write(metin)
  return 0


if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))

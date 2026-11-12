#!/usr/bin/env python3
"""Paket başına tema çıktılarını uretim-tutanagi/ciktilar.json'a yazar (12.11, hat G-3).

birlestir.py her paketi iki temada üretir: açık → cikti.mp4, koyu → cikti-koyu.mp4. Kayıt evi
(kayit.ndr.ist) mp4 dosyalarını görmez; içe alma bu dosyayı okur ve konu sayfası açık/koyu kartlarını
bundan doldurur. Türetilmiş dosyadır (git dışı); içe almadan hemen önce koşulur.

Kullanım: /usr/bin/python3 -I araclar/cikti-yaz.py [--paket AD]...
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent / "projeler"
SEMA = "ut-ciktilar/v1"
TEMA_DOSYA = (("acik", "cikti.mp4"), ("koyu", "cikti-koyu.mp4"))


def zaman_iso(sn: float) -> str:
  return datetime.fromtimestamp(sn, timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def ciktilar(paket: Path) -> list[dict[str, object]]:
  sonuc: list[dict[str, object]] = []
  for tema, ad in TEMA_DOSYA:
    yol = paket / ad
    if yol.is_file():
      st = yol.stat()
      sonuc.append({"tema": tema, "dosya": ad, "bayt": st.st_size, "zaman": zaman_iso(st.st_mtime)})
  return sonuc


def yaz(yol: Path, veri: dict[str, object]) -> None:
  yol.parent.mkdir(parents=True, exist_ok=True)
  gecici = yol.with_name(f"{yol.name}.{os.getpid()}.tmp")
  gecici.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
  gecici.replace(yol)


def main() -> int:
  ap = argparse.ArgumentParser()
  ap.add_argument("--paket", action="append", default=[])
  a = ap.parse_args()
  adlar = a.paket or sorted(p.name for p in KOK.iterdir() if p.is_dir() and (p / "zaman.json").is_file())
  sayac = 0
  for ad in adlar:
    paket = KOK / ad
    if not paket.is_dir():
      print(f"{ad}: paket yok, atlandı")
      continue
    c = ciktilar(paket)
    yaz(paket / "uretim-tutanagi" / "ciktilar.json", {"sema": SEMA, "paket": ad, "ciktilar": c})
    sayac += 1
    print(f"{ad}: {', '.join(str(x['tema']) for x in c) or 'çıktı yok'}")
  print(f"TOPLAM: {sayac} paket")
  return 0


if __name__ == "__main__":
  sys.exit(main())

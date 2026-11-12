#!/usr/bin/env python3
"""Paket başına KAPI-ÖN sonucunu uretim-tutanagi/kapi.json'a yazar (12.11, pp g-6, D-0147).

Kayıt evi (kayit.ndr.ist) kapıyı kendisi koşamaz: kaynak dosyaları ve sesler bu Mac'tedir. Bu betik
dijital-anlatim tutanak_on.kapi() sonucunu dosyaya yazar; kontrol-ice-al betiği on.json ile birlikte
okur. kapi.json türetilmiş dosyadır (git dışı); içe almadan hemen önce koşulur.

Kullanım: /usr/bin/python3 -I araclar/kapi-yaz.py [--paket AD]...
Çıktı: paket başına sonuç satırı; tutanağı olmayan paket atlanır.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent / "projeler"
DA_KOK = Path(os.environ.get("DIJITAL_ANLATIM_KOK", Path.home() / "01dev" / "dijital-anlatim"))
SEMA = "ut-kapi/v1"


def tutanak_on_yukle():  # type: ignore[no-untyped-def]
  dizin = DA_KOK / "araclar" / "sema"
  sys.path.insert(0, str(dizin))  # tutanak_on, sema_ortak'ı aynı dizinden alır
  spec = importlib.util.spec_from_file_location("tutanak_on", dizin / "tutanak_on.py")
  assert spec and spec.loader
  modul = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(modul)
  return modul


def kapi_kaydi(paket: Path, kod: int, ileti: str, sonuc: str, kimlik: str | None) -> dict[str, object]:
  return {
    "sema": SEMA,
    "tutanak": kimlik,
    "kod": kod,
    "sonuc": sonuc,
    "mesaj": ileti,
    "zaman": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
    "paket": paket.name,
  }


def yaz(yol: Path, veri: dict[str, object]) -> None:
  gecici = yol.with_name(f"{yol.name}.{os.getpid()}.tmp")
  gecici.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
  gecici.replace(yol)


def main() -> int:
  ap = argparse.ArgumentParser()
  ap.add_argument("--paket", action="append", default=[])
  a = ap.parse_args()
  to = tutanak_on_yukle()
  adlar = a.paket or sorted(p.name for p in KOK.iterdir() if (p / "uretim-tutanagi" / "on.json").is_file())
  sayac: dict[str, int] = {}
  for ad in adlar:
    paket = KOK / ad
    on = paket / "uretim-tutanagi" / "on.json"
    if not on.is_file():
      print(f"{ad}: on.json yok, atlandı")
      continue
    kimlik = json.loads(on.read_text(encoding="utf-8")).get("kimlik")
    kod, ileti = to.kapi(paket, DA_KOK)
    sonuc = to.KAPI_KODLARI[kod]
    yaz(paket / "uretim-tutanagi" / "kapi.json", kapi_kaydi(paket, kod, ileti, sonuc, kimlik))
    sayac[sonuc] = sayac.get(sonuc, 0) + 1
    print(f"{ad}: {ileti}")
  print("TOPLAM:", ", ".join(f"{k} {v}" for k, v in sorted(sayac.items())) or "0")
  return 0


if __name__ == "__main__":
  sys.exit(main())

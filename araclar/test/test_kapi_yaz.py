"""araclar/kapi-yaz.py birim testleri (12.11, pp g-6). Koş: /usr/bin/python3 -I -m unittest discover araclar/test -p 'test_kapi_yaz.py'"""
from __future__ import annotations

import importlib.util
import json
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

YOL = Path(__file__).resolve().parent.parent / "kapi-yaz.py"
_spec = importlib.util.spec_from_file_location("kapi_yaz", YOL)
assert _spec and _spec.loader
ky = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ky)


class KapiYazTest(unittest.TestCase):
  def test_paket_basina_kapi_json_yazar_ve_tutanagi_olmayani_atlar(self) -> None:
    with tempfile.TemporaryDirectory() as d:
      kok = Path(d)
      for ad, kimlik in (("ders-a", "UT-1"), ("ders-b", "UT-2")):
        (kok / ad / "uretim-tutanagi").mkdir(parents=True)
        (kok / ad / "uretim-tutanagi" / "on.json").write_text(json.dumps({"kimlik": kimlik}))
      (kok / "ders-c").mkdir()
      sonuclar = {"ders-a": (0, "KAPI-ÖN GEÇTİ: UT-1"), "ders-b": (5, "KAPI-ÖN BAYAT: değişen girdi")}
      sahte = types.SimpleNamespace(
        KAPI_KODLARI={0: "GEÇTİ", 5: "BAYAT"},
        kapi=lambda paket, kok_: sonuclar[Path(paket).name],
      )
      with mock.patch.object(ky, "KOK", kok), mock.patch.object(ky, "tutanak_on_yukle", return_value=sahte), \
          mock.patch("sys.argv", ["kapi-yaz.py"]):
        self.assertEqual(ky.main(), 0)
      a = json.loads((kok / "ders-a" / "uretim-tutanagi" / "kapi.json").read_text())
      b = json.loads((kok / "ders-b" / "uretim-tutanagi" / "kapi.json").read_text())
      self.assertEqual((a["sema"], a["tutanak"], a["kod"], a["sonuc"]), ("ut-kapi/v1", "UT-1", 0, "GEÇTİ"))
      self.assertEqual((b["tutanak"], b["kod"], b["sonuc"]), ("UT-2", 5, "BAYAT"))
      self.assertTrue(a["zaman"].endswith("Z"))
      self.assertFalse((kok / "ders-c" / "uretim-tutanagi").exists())
      self.assertEqual(list((kok / "ders-a" / "uretim-tutanagi").glob("*.tmp")), [])


if __name__ == "__main__":
  unittest.main()

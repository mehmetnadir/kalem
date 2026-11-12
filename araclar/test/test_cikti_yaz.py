"""araclar/cikti-yaz.py birim testleri (12.11, hat G-3). Koş: /usr/bin/python3 -I -m unittest discover araclar/test -p 'test_cikti_yaz.py'"""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

YOL = Path(__file__).resolve().parent.parent / "cikti-yaz.py"
_spec = importlib.util.spec_from_file_location("cikti_yaz", YOL)
assert _spec and _spec.loader
cy = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cy)


class CiktiYazTest(unittest.TestCase):
  def test_iki_tema_tek_tema_ve_ciktisiz_paket(self) -> None:
    with tempfile.TemporaryDirectory() as d:
      kok = Path(d)
      for ad in ("iki", "tek", "yok"):
        (kok / ad).mkdir()
        (kok / ad / "zaman.json").write_text("{}")
      (kok / "iki" / "cikti.mp4").write_bytes(b"a" * 3)
      (kok / "iki" / "cikti-koyu.mp4").write_bytes(b"b" * 5)
      (kok / "tek" / "cikti-koyu.mp4").write_bytes(b"c")
      (kok / "zamansiz").mkdir()
      with mock.patch.object(cy, "KOK", kok), mock.patch("sys.argv", ["cikti-yaz.py"]):
        self.assertEqual(cy.main(), 0)
      oku = lambda ad: json.loads((kok / ad / "uretim-tutanagi" / "ciktilar.json").read_text())
      iki, tek, yok = oku("iki"), oku("tek"), oku("yok")
      self.assertEqual(iki["sema"], "ut-ciktilar/v1")
      self.assertEqual([(c["tema"], c["dosya"], c["bayt"]) for c in iki["ciktilar"]],
                       [("acik", "cikti.mp4", 3), ("koyu", "cikti-koyu.mp4", 5)])
      self.assertEqual([c["tema"] for c in tek["ciktilar"]], ["koyu"])
      self.assertEqual(yok["ciktilar"], [])
      self.assertTrue(str(iki["ciktilar"][0]["zaman"]).endswith("Z"))
      self.assertFalse((kok / "zamansiz" / "uretim-tutanagi").exists())


if __name__ == "__main__":
  unittest.main()

"""araclar/duzeltme-tasi.py birim testleri (12.11, pp g-11). Koş: /usr/bin/python3 -I -m unittest discover araclar/test -p 'test_*.py'"""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

YOL = Path(__file__).resolve().parent.parent / "duzeltme-tasi.py"
_spec = importlib.util.spec_from_file_location("duzeltme_tasi", YOL)
assert _spec and _spec.loader
dt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dt)


class GunlukTest(unittest.TestCase):
  def test_tek_satir_cagri_ve_tanim_importtan_sonra(self) -> None:
    kaynak = ('import { a } from "/x.js";\nimport { b } from "/y.js";\n\nconst W = 1;\n'
              'await fetch("/log", { method: "POST", body: "OLAYLAR " + s });\n')
    yeni, n = dt.gunluk_donustur(kaynak)
    self.assertEqual(n, 1)
    self.assertNotIn('fetch("/log", {', yeni)
    self.assertIn('await logGonder({ method: "POST", body: "OLAYLAR " + s });', yeni)
    satirlar = yeni.split("\n")
    self.assertEqual(satirlar[2], dt.TANIM.split("\n")[0])          # son import'tan hemen sonra
    self.assertEqual(yeni.count("const logGonder"), 1)

  def test_cok_satirli_import(self) -> None:
    kaynak = ('import {\n  a,\n  b,\n} from "/x.js";\nfetch("/log", {\n  method: "POST",\n  body: m\n});\n')
    yeni, n = dt.gunluk_donustur(kaynak)
    self.assertEqual(n, 1)
    satirlar = yeni.split("\n")
    self.assertEqual(satirlar[3], '} from "/x.js";')
    self.assertTrue(satirlar[4].startswith("// Geliştirme günlüğü"))

  def test_yerel_sarmalayici_o_secenegi(self) -> None:
    kaynak = ('import { a } from "/x.js";\nconst gunluk = (o) => (c ? Promise.resolve() : fetch("/log", o));\n')
    yeni, n = dt.gunluk_donustur(kaynak)
    self.assertEqual(n, 1)
    self.assertIn("Promise.resolve() : logGonder(o));", yeni)

  def test_ikinci_kosu_degistirmez(self) -> None:
    kaynak = 'import { a } from "/x.js";\nfetch("/log", o);\n'
    bir, _ = dt.gunluk_donustur(kaynak)
    iki, n = dt.gunluk_donustur(bir)
    self.assertEqual((iki, n), (bir, 0))

  def test_cagri_yoksa_dokunmaz(self) -> None:
    kaynak = 'import { a } from "/x.js";\nconst x = 1;\n'
    self.assertEqual(dt.gunluk_donustur(kaynak), (kaynak, 0))

  def test_tanim_yalniz_yerel_sunucuda_gonderir(self) -> None:
    self.assertIn("YEREL_SUNUCU ? fetch(\"/log\", o)", dt.TANIM)
    self.assertIn("192\\.168", dt.TANIM)


class ZeminTest(unittest.TestCase):
  def test_kaynak_pakette_yeni_blok_ve_eski_blok_tutarli(self) -> None:
    kaynak = (dt.KOK / dt.KAYNAK / "ortak" / "kunye.js").read_text(encoding="utf-8")
    yeni, eski = dt.zemin_bloklari(kaynak)
    for ad in ("export function zeminCiz", "function zeminKaroAl", "function vinyetAl"):
      self.assertIn(ad, yeni)
    self.assertNotIn(eski, kaynak)                      # kaynak paket zaten yeni sürümde
    self.assertTrue(yeni.rstrip().endswith("}"))

  def test_eski_govde_en_az_bir_pakette_birebir(self) -> None:
    sayi = sum(1 for k in dt.KOK.glob("*/ortak/kunye.js")
               if not k.is_symlink() and k.read_text(encoding="utf-8").count(dt.ESKI_ZEMIN) == 1)
    tasinmis = sum(1 for k in dt.KOK.glob("*/ortak/kunye.js")
                   if not k.is_symlink() and "zeminKaroAl" in k.read_text(encoding="utf-8"))
    self.assertGreaterEqual(sayi + tasinmis, 3)


if __name__ == "__main__":
  unittest.main()

#!/usr/bin/python3 -I
"""kisa-istem-uret.py testleri (model yok, ağ yok). Koşu: /usr/bin/python3 -I test_kisa_istem_uret.py"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

BU = Path(__file__).resolve().parent
HAT = BU.parent
URET = BU / "kisa-istem-uret.py"
ISTEM = HAT / "istemler"
KONU_0202T = ISTEM / "sablon" / "konu-0202T.json"
# 0202T altın testi: emsalden beklenen farklar. Satır 1: dosya adı öneki (P0202 → P0202T).
# 30-31: karakter tarifi artık ana paketin ortak/kapak/KAYNAK.json dosyasından gelir
# (emsaldeki "kıvırcık saçlı…" elle yazılmıştı, güncel görselle uyuşmuyor).
BEKLENEN_FARK = {1, 30, 31}


def kos(*arg: str) -> subprocess.CompletedProcess[str]:
  return subprocess.run(["/usr/bin/python3", "-I", str(URET), *arg],
                        capture_output=True, text=True, check=False)


def farkli_satirlar(a: str, b: str) -> set[int]:
  x, y = a.splitlines(), b.splitlines()
  n = max(len(x), len(y))
  return {i + 1 for i in range(n) if (x[i] if i < len(x) else None) != (y[i] if i < len(y) else None)}


class AltinTest(unittest.TestCase):
  def altin(self, n: int) -> None:
    with tempfile.TemporaryDirectory() as t:
      r = kos("0202T", "simple-present-temel", str(n), "--cikti", t,
              "--konu-json", str(KONU_0202T), "--tarih", "15.11.2026")
      self.assertEqual(r.returncode, 0, r.stderr)
      uretilen = (Path(t) / f"P0202T-S{n}-A.md").read_text(encoding="utf-8")
      emsal = (ISTEM / f"P0202-S{n}-A.md").read_text(encoding="utf-8")
      self.assertEqual(farkli_satirlar(uretilen, emsal) - BEKLENEN_FARK, set(),
                       f"S{n}: beklenmeyen fark")
      self.assertEqual(uretilen.splitlines()[0].replace("P0202T-", "P0202-"),
                       emsal.splitlines()[0])

  def test_s2(self) -> None:
    self.altin(2)

  def test_s3(self) -> None:
    self.altin(3)

  def test_s1_eski_icerik_cumlesi(self) -> None:
    """S1: paket kökünde eski kısa içeriği var → A'daki 'ESKİ' cümlesi emsalle aynı."""
    self.altin(1)


class DavranisTest(unittest.TestCase):
  def test_0201t_s2_dort_dosya(self) -> None:
    with tempfile.TemporaryDirectory() as t:
      r = kos("0201T", "present-continuous", "2", "--cikti", t, "--tarih", "16.11.2026")
      self.assertEqual(r.returncode, 0, r.stderr)
      for d in ("A", "B-dil", "B-kural", "C"):
        s = (Path(t) / f"P0201T-S2-{d}.md").read_text(encoding="utf-8")
        self.assertNotIn("{{", s, d)
        self.assertNotIn("simple-present", s, d)
        self.assertIn("present-continuous-s2", s, d)
      a = (Path(t) / "P0201T-S2-A.md").read_text(encoding="utf-8")
      self.assertIn("öğe `02-01-ydt-temel`", a)
      self.assertIn("Look!, Listen! ve now", a)
      self.assertIn("`sesler`", a)  # present-continuous senaryo.json'da kadro yok
      self.assertIn("BU AKŞAM = I AM GOING", a)

  def test_eksik_alan_cikis_2(self) -> None:
    with tempfile.TemporaryDirectory() as t:
      pr = Path(t) / "projeler" / "p1"
      (pr / "ortak" / "anlatim").mkdir(parents=True)
      (pr / "surumler.json").write_text(json.dumps({"video": {"konu": "K", "seviye": "temel", "kitle": "YDT"}, "surumler": []}))
      (pr / "ortak" / "anlatim" / "senaryo.json").write_text(json.dumps({"cumleler": []}))
      cik = Path(t) / "cikti"
      r = kos("0201T", "p1", "2", "--projeler", str(Path(t) / "projeler"), "--cikti", str(cik))
      self.assertEqual(r.returncode, 2)
      self.assertIn("EKSİK", r.stderr)
      for alan in ("kapak metni", "huni-konu.json", "KAYNAK.json"):
        self.assertIn(alan, r.stderr)
      self.assertFalse(cik.exists())  # hiçbir dosya yazılmadı

  def test_var_olan_dosya_cikis_3(self) -> None:
    with tempfile.TemporaryDirectory() as t:
      arg = ("0202T", "simple-present-temel", "2", "--cikti", t, "--konu-json", str(KONU_0202T))
      self.assertEqual(kos(*arg).returncode, 0)
      ilk = (Path(t) / "P0202T-S2-C.md").read_text(encoding="utf-8")
      (Path(t) / "P0202T-S2-C.md").write_text("elle düzenlendi")
      r = kos(*arg)
      self.assertEqual(r.returncode, 3)
      self.assertEqual((Path(t) / "P0202T-S2-C.md").read_text(), "elle düzenlendi")
      self.assertEqual(kos(*arg, "--zorla").returncode, 0)
      self.assertEqual((Path(t) / "P0202T-S2-C.md").read_text(encoding="utf-8"), ilk)

  def test_kuru_yazmaz(self) -> None:
    with tempfile.TemporaryDirectory() as t:
      r = kos("0201T", "present-continuous", "2", "--cikti", str(Path(t) / "yok"), "--kuru")
      self.assertEqual(r.returncode, 0)
      self.assertFalse((Path(t) / "yok").exists())

  def test_kaydet_kalibi_olmayan_n(self) -> None:
    with tempfile.TemporaryDirectory() as t:
      r = kos("0201T", "present-continuous", "4", "--cikti", t)
      self.assertEqual(r.returncode, 2)
      self.assertIn("kaydet/çağrı", r.stderr)
      r = kos("0201T", "present-continuous", "4", "--cikti", t,
              "--kaydet", "Kaydet.", "--cagri", "Gel.")
      self.assertEqual(r.returncode, 0, r.stderr)

  def test_sablon_tek_kaynak(self) -> None:
    for d in ("A", "B-dil", "B-kural", "C"):
      self.assertTrue((ISTEM / "sablon" / f"{d}.md").is_file(), d)
    shutil.which("true")


if __name__ == "__main__":
  unittest.main(argv=[sys.argv[0], "-v"])

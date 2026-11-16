#!/usr/bin/python3 -I
"""duz-istem-uret.py testleri (model yok, ağ yok). Koşu: /usr/bin/python3 -I test_duz_istem_uret.py"""
from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

URET = Path(__file__).resolve().parent / "duz-istem-uret.py"

HUKUM = """# DJ-0206T
| Bölüm | evet | hayır | kanıt yok |
|---|---|---|---|
| DK-1 | **hayır** | `06/yardim.py:170` | dolgu |
| EK-3 | hayır | kare yok | koyu kare |
| EK-5b | hayır (kısmi) | tablo | ekle |
| EK-6 | evet | — | — |
| EK-7 | **evet** | — | — |
| EK-8 | kanıt yok | — | — |
"""


def kos(*arg: str) -> subprocess.CompletedProcess[str]:
  return subprocess.run(["/usr/bin/python3", "-I", str(URET), *arg],
                        capture_output=True, text=True, check=False)


class DuzIstemUret(unittest.TestCase):
  def setUp(self) -> None:
    self.t = tempfile.TemporaryDirectory()
    self.h = Path(self.t.name) / "DJ-hukum.md"
    self.h.write_text(HUKUM, encoding="utf-8")

  def tearDown(self) -> None:
    self.t.cleanup()

  def test_kalin_ve_duz_hayir_sayilir(self) -> None:
    c = kos("0206T", "present-perfect-temel", "--hukum", str(self.h))
    self.assertEqual(c.returncode, 0, c.stderr)
    self.assertIn("3 `hayır` satırı", c.stdout)
    for kimlik in ("**DK-1**", "**EK-3**", "**EK-5b**"):
      self.assertIn(kimlik, c.stdout)

  def test_baslik_satiri_sayilmaz(self) -> None:
    c = kos("X", "p", "--hukum", str(self.h))
    self.assertNotIn("**Bölüm**", c.stdout)

  def test_evet_ve_kanit_yok_sayilmaz(self) -> None:
    c = kos("X", "p", "--hukum", str(self.h))
    for kimlik in ("**EK-6**", "**EK-7**", "**EK-8**"):
      self.assertNotIn(kimlik, c.stdout)

  def test_kapsam_yer_tutucusu_dolar(self) -> None:
    c = kos("X", "ders-a", "--hukum", str(self.h), "--kapsam", "sahne-kare")
    self.assertIn("kapsam `sahne-kare`", c.stdout)
    self.assertIn("K/projeler/ders-a-dikey", c.stdout)
    for yer in ("{KAPSAM}", "{PAKET}", "{KOD}", "{HUKUM_YOLU}", "{IS_LISTESI}"):
      self.assertNotIn(yer, c.stdout)

  def test_durum_tablosu_basligi_var(self) -> None:
    c = kos("X", "p", "--hukum", str(self.h))
    self.assertIn("| kimlik | kapandı / kapanmadı | sınıf a–e | sahip | kanıt", c.stdout)
    self.assertIn("uretici_model", c.stdout)

  def test_eksik_hukum_anlamli_hata(self) -> None:
    c = kos("X", "p", "--hukum", "/yok/DJ.md")
    self.assertEqual(c.returncode, 2)
    self.assertIn("hüküm dosyası yok", c.stderr)

  def test_gecersiz_kapsam(self) -> None:
    c = kos("X", "p", "--hukum", str(self.h), "--kapsam", "xyz")
    self.assertEqual(c.returncode, 2)
    self.assertIn("kapsam geçersiz", c.stderr)

  def test_cikti_dosyasi(self) -> None:
    o = Path(self.t.name) / "istem.md"
    c = kos("X", "p", "--hukum", str(self.h), "--cikti", str(o))
    self.assertEqual(c.returncode, 0)
    self.assertEqual(c.stdout, "")
    self.assertIn("DUZ-X", o.read_text(encoding="utf-8"))


if __name__ == "__main__":
  unittest.main()

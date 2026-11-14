"""araclar/qa-yerel.sh: sunucu-yerel sahne QA sarmalayıcısının giriş kapıları (14.11).

Chrome ve önizleme sunucusu gerekmez: yalnız ortam ve argüman kapıları sınanır.
"""
from __future__ import annotations

import getpass
import platform
import subprocess
import unittest
from pathlib import Path

BETIK = Path(__file__).resolve().parent.parent / "araclar" / "qa-yerel.sh"
SUNUCU = platform.system() == "Linux" and getpass.getuser() == "sef"


def kos(*arg: str) -> subprocess.CompletedProcess[str]:
  return subprocess.run(["bash", str(BETIK), *arg], capture_output=True, text=True, timeout=30)


class QaYerelTest(unittest.TestCase):
  def test_sozdizimi(self) -> None:
    self.assertEqual(subprocess.run(["bash", "-n", str(BETIK)]).returncode, 0)

  @unittest.skipIf(SUNUCU, "sunucuda koşar")
  def test_sunucu_disinda_reddeder(self) -> None:
    r = kos("02-04-ydt-temel", "01-hyperframes-giris", "1", "1")
    self.assertEqual(r.returncode, 1)
    self.assertIn("yalnız Linux/sef", r.stderr)

  @unittest.skipUnless(SUNUCU, "yalnız sunucu (Linux/sef)")
  def test_argumansiz_kullanim(self) -> None:
    r = kos()
    self.assertEqual(r.returncode, 1)
    self.assertIn("kullanım", r.stderr)

  @unittest.skipUnless(SUNUCU, "yalnız sunucu (Linux/sef)")
  def test_kural_disi_sahne(self) -> None:
    r = kos("02-04-ydt-temel", "giris", "1", "1")
    self.assertEqual(r.returncode, 1)
    self.assertIn("sahne adı kural dışı", r.stderr)

  @unittest.skipUnless(SUNUCU, "yalnız sunucu (Linux/sef)")
  def test_olmayan_sahne(self) -> None:
    r = kos("02-99-ydt-temel", "01-hyperframes-giris", "1,2", "1")
    self.assertEqual(r.returncode, 1)
    self.assertIn("sahne yok", r.stderr)


if __name__ == "__main__":
  unittest.main()

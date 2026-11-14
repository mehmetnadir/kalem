"""araclar/ayna-sunucu.sh: sunucu üretiminden ayna eşitleme sarmalayıcısının giriş kapıları (14.11).

Ağ ve kayit gerekmez: hata dallarını ve jetonun ortam dosyasından okunduğunu sınar.
"""
from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

BETIK = Path(__file__).resolve().parent.parent / "araclar" / "ayna-sunucu.sh"


def kos(*arg: str, env_ek: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
  env = dict(os.environ)
  env.update(env_ek or {})
  return subprocess.run(["bash", str(BETIK), *arg], capture_output=True, text=True, env=env, timeout=30)


class AynaSunucuTest(unittest.TestCase):
  def setUp(self) -> None:
    self.td = tempfile.TemporaryDirectory()
    self.kok = Path(self.td.name) / "kalem"
    (self.kok / "projeler" / "02-04-ydt-temel").mkdir(parents=True)
    self.ortam = Path(self.td.name) / "kontrol.env"

  def tearDown(self) -> None:
    self.td.cleanup()

  def test_sozdizimi(self) -> None:
    self.assertEqual(subprocess.run(["bash", "-n", str(BETIK)]).returncode, 0)

  def test_argumansiz_kullanim(self) -> None:
    r = kos()
    self.assertEqual(r.returncode, 1)
    self.assertIn("kullanım", r.stderr)

  def test_kural_disi_paket_adi(self) -> None:
    r = kos("--kok", str(self.kok), "Kotu_Ad")
    self.assertEqual(r.returncode, 1)
    self.assertIn("kural dışı", r.stderr)

  def test_olmayan_paket(self) -> None:
    r = kos("--kok", str(self.kok), "02-05-ydt-temel")
    self.assertEqual(r.returncode, 1)
    self.assertIn("paket yok", r.stderr)

  def test_ortam_dosyasi_yok(self) -> None:
    r = kos("--kok", str(self.kok), "02-04-ydt-temel", env_ek={"KONTROL_ORTAM": str(self.ortam)})
    self.assertEqual(r.returncode, 1)
    self.assertIn("ortam dosyası okunamıyor", r.stderr)

  def test_ortamda_jeton_yok(self) -> None:
    self.ortam.write_text("KONTROL_URL=http://127.0.0.1:3810\n")
    r = kos("--kok", str(self.kok), "02-04-ydt-temel", env_ek={"KONTROL_ORTAM": str(self.ortam)})
    self.assertEqual(r.returncode, 1)
    self.assertIn("KONTROL_ISCI_JETON yok", r.stderr)

  def test_jeton_varsa_kayit_dizinine_gecer(self) -> None:
    self.ortam.write_text("KONTROL_ISCI_JETON=deneme\n")
    olmayan = Path(self.td.name) / "kayit-yok"
    r = kos("--kok", str(self.kok), "02-04-ydt-temel",
            env_ek={"KONTROL_ORTAM": str(self.ortam), "KAYIT_KOK": str(olmayan)})
    # Jeton okundu, eşitleme için kayit dizinine geçmeye çalıştı; dizin yok → cd hatası.
    self.assertNotEqual(r.returncode, 0)
    self.assertIn(str(olmayan), r.stderr)
    self.assertNotIn("deneme", r.stdout + r.stderr)


if __name__ == "__main__":
  unittest.main()

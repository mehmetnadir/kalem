"""araclar/ses-sunucu.sh: sunucu ses sentezi sarmalayıcısının giriş kapıları (14.11).

ElevenLabs, vekil ve model gerekmez: hata dalları ve ortamın el.py'ye nasıl geçtiği sahte python ile sınanır.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

BETIK = Path(__file__).resolve().parent.parent / "araclar" / "ses-sunucu.sh"


class SesSunucuTest(unittest.TestCase):
  def setUp(self) -> None:
    self.td = tempfile.TemporaryDirectory()
    t = Path(self.td.name)
    self.kok = t / "kalem"
    self.anlatim = self.kok / "projeler" / "02-04-ydt-temel" / "ortak" / "anlatim"
    self.anlatim.mkdir(parents=True)
    (self.anlatim / "senaryo.json").write_text("{}")
    self.da = t / "dijital-anlatim"
    (self.da / "araclar" / "iki-dilli").mkdir(parents=True)
    (self.da / "araclar" / "iki-dilli" / "el.py").write_text("# sahte\n")
    self.ortam = t / "kontrol.env"
    self.ortam.write_text("KONTROL_ISCI_JETON=gizli-deneme\n")
    # Sahte python: aldığı argümanları ve ortamı yazar, jetonu yazmaz.
    self.py = t / "py"
    self.py.write_text(
      "#!/bin/bash\n"
      'echo "ARG $*"\n'
      'echo "VEKIL $ELEVEN_VEKIL_URL"\n'
      'echo "HIZ $HIZ_EN"\n'
      'echo "OFFLINE $HF_HUB_OFFLINE"\n'
      '[ -n "$KONTROL_ISCI_JETON" ] && echo "JETON var"\n'
    )
    self.py.chmod(0o755)

  def tearDown(self) -> None:
    self.td.cleanup()

  def kos(self, *arg: str, **env_ek: str) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env.update({"DA_KOK": str(self.da), "SES_PY": str(self.py), "KONTROL_ORTAM": str(self.ortam),
                "TMPDIR": self.td.name})
    env.pop("ELEVEN_VEKIL_URL", None)
    env.update(env_ek)
    return subprocess.run(["bash", str(BETIK), *arg], capture_output=True, text=True, env=env, timeout=30)

  def test_sozdizimi(self) -> None:
    self.assertEqual(subprocess.run(["bash", "-n", str(BETIK)]).returncode, 0)

  def test_argumansiz(self) -> None:
    r = self.kos()
    self.assertEqual(r.returncode, 1)
    self.assertIn("kullanım", r.stderr)

  def test_senaryo_yok(self) -> None:
    r = self.kos("--kok", str(self.kok), "02-05-ydt-temel")
    self.assertEqual(r.returncode, 1)
    self.assertIn("senaryo yok", r.stderr)

  def test_jeton_yok(self) -> None:
    self.ortam.write_text("KONTROL_URL=x\n")
    r = self.kos("--kok", str(self.kok), "02-04-ydt-temel")
    self.assertEqual(r.returncode, 1)
    self.assertIn("KONTROL_ISCI_JETON yok", r.stderr)

  @unittest.skipUnless(shutil.which("flock"), "flock yalnız Linux'ta (sunucu)")
  def test_el_py_ortami(self) -> None:
    r = self.kos("--kok", str(self.kok), "02-04-ydt-temel")
    self.assertEqual(r.returncode, 0, r.stderr)
    self.assertIn(f"ARG -I {self.da}/araclar/iki-dilli/el.py {self.anlatim}/senaryo.json "
                  f"{self.anlatim}/sentez.wav {self.anlatim} gsJ9nrlXYbPztJxC4fwc eleven_v4", r.stdout)
    self.assertIn("VEKIL http://127.0.0.1:3810/api/kontrol/saglayici/elevenlabs", r.stdout)
    self.assertIn("HIZ 0.9", r.stdout)
    self.assertIn("OFFLINE 1", r.stdout)
    self.assertIn("JETON var", r.stdout)
    self.assertNotIn("gizli-deneme", r.stdout + r.stderr)


if __name__ == "__main__":
  unittest.main()

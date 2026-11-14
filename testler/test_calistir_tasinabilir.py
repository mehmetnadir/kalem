"""calistir.sh taşınabilirliği: koşulsuz /opt/homebrew PATH'i ve ham uptime ayrıştırması yok; yuk1() tam sayı verir."""
import glob, os, re, subprocess, unittest

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJE = os.path.join(KOK, "projeler/02-02-ydt-temel")
BETIKLER = sorted(glob.glob(os.path.join(PROJE, "sahneler/*/calistir.sh")))


class Tasinabilir(unittest.TestCase):
  def test_betik_sayisi(self):
    self.assertEqual(len(BETIKLER), 11)

  def test_homebrew_path_kosullu(self):
    for b in BETIKLER:
      for s in open(b, encoding="utf-8"):
        if "/opt/homebrew/bin" in s and not s.lstrip().startswith("#"):
          self.assertTrue(s.startswith("[ -d /opt/homebrew/bin ] &&"), f"{b}: {s}")

  def test_yuk_yardimcisi_kullaniliyor(self):
    for b in BETIKLER:
      t = open(b, encoding="utf-8").read()
      self.assertNotIn("uptime", t, b)
      self.assertIn("Y=$(yuk1)", t, b)

  def test_yuk1_tam_sayi(self):
    c = subprocess.run(["bash", "-c", f'. "{PROJE}/ortak/tema.sh" >/dev/null 2>&1; yuk1'],
                       capture_output=True, text=True)
    self.assertRegex(c.stdout.strip(), r"^\d+$")

  def test_yuk1_uptime_biçimleri(self):
    for cikti in ("load averages: 3.10 3.40 3.50", "load average: 12.34, 3.40, 3.50"):
      c = subprocess.run(["bash", "-c", f'echo "{cikti}" | sed \'s/.*averages*: *//\' | awk \'{{gsub(",","",$1); print int($1)}}\''],
                         capture_output=True, text=True)
      self.assertEqual(c.stdout.strip(), re.search(r"(\d+)\.", cikti.split(":")[1]).group(1))


if __name__ == "__main__":
  unittest.main()

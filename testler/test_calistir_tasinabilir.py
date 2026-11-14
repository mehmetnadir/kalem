"""calistir.sh taşınabilirliği: koşulsuz /opt/homebrew PATH'i ve ham uptime ayrıştırması yok; yuk1() tam sayı verir."""
import glob, os, re, subprocess, unittest

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJE = os.path.join(KOK, "projeler/02-02-ydt-temel")
BETIKLER = sorted(glob.glob(os.path.join(PROJE, "sahneler/*/calistir.sh")))
TUM = sorted(glob.glob(os.path.join(KOK, "projeler/*/sahneler/*/calistir.sh")))
TEMALAR = sorted(glob.glob(os.path.join(KOK, "projeler/*/ortak/tema.sh")))


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

  # --- bütün paketler (14.11, K-0063) ---
  def test_tum_betikler_bulundu(self):
    self.assertGreater(len(TUM), 0)
    self.assertGreaterEqual(len(TUM), len(BETIKLER))

  def test_tum_homebrew_path_kosullu(self):
    for b in TUM + [os.path.join(KOK, "araclar/matris-uret.sh")]:
      for s in open(b, encoding="utf-8"):
        if "/opt/homebrew/bin" in s and not s.lstrip().startswith("#"):
          self.assertTrue(s.startswith("[ -d /opt/homebrew/bin ] &&"), f"{b}: {s}")

  def test_tum_ham_uptime_yok(self):
    for b in TUM:
      for s in open(b, encoding="utf-8"):
        if s.lstrip().startswith("#"):
          continue
        self.assertNotIn("uptime", s, b)

  def test_yuk1_kullanan_betik_tema_okur(self):
    for b in TUM:
      t = open(b, encoding="utf-8").read()
      if "$(yuk1)" in t:
        self.assertIn("ortak/tema.sh", t, b)
        self.assertLess(t.index("ortak/tema.sh"), t.index("$(yuk1)"), b)

  def test_tum_tema_yuk1_tanimli(self):
    self.assertGreater(len(TEMALAR), 0)
    for tm in TEMALAR:
      self.assertIn("yuk1()", open(tm, encoding="utf-8").read(), tm)
      c = subprocess.run(["bash", "-c", f'. "{tm}" >/dev/null 2>&1; yuk1'], capture_output=True, text=True)
      self.assertRegex(c.stdout.strip(), r"^\d+$", tm)

  def test_kur_ffmpeg_yolu_tasinabilir(self):
    # 14.11: kur.py sabit /opt/homebrew/bin/ffmpeg yazıyordu; sunucuda (Linux) PATH'teki ffmpeg önce gelir.
    kurlar = sorted(glob.glob(os.path.join(KOK, "projeler", "*", "ortak", "anlatim", "kur.py")))
    self.assertGreater(len(kurlar), 0)
    for k in kurlar:
      with open(k, encoding="utf-8") as f:
        s = f.read()
      self.assertNotRegex(s, r'(?m)^FFMPEG = "/opt/homebrew/bin/ffmpeg"\s*$', k)
      if "FFMPEG =" in s:
        self.assertIn('shutil.which("ffmpeg")', s, k)


if __name__ == "__main__":
  unittest.main()

"""yakala.py platform seçimi: Mac dalı eski gömülü değerlerle birebir, Linux dalı ayrı (saf işlevler)."""
import os, sys, unittest

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(KOK, "ortak"))
import yakala_platform as yp


class Platform(unittest.TestCase):
  def test_mac_chrome_eski_deger(self):
    self.assertEqual(yp.chrome_yolu("Darwin", {}),
                     "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

  def test_mac_bayraklari_eski_deger(self):
    self.assertEqual(yp.gpu_bayraklari("Darwin"),
                     ["--use-angle=metal", "--enable-gpu", "--ignore-gpu-blocklist"])

  def test_env_kazanir(self):
    self.assertEqual(yp.chrome_yolu("Darwin", {"CHROME": "/x/c"}), "/x/c")
    self.assertEqual(yp.chrome_yolu("Linux", {"CHROME": "/x/c"}), "/x/c")

  def test_linux_which(self):
    self.assertEqual(yp.chrome_yolu("Linux", {}, which=lambda a: "/usr/bin/" + a if a == "chromium" else None),
                     "/usr/bin/chromium")

  def test_linux_bayrak_metal_yok(self):
    b = yp.gpu_bayraklari("Linux")
    self.assertNotIn("--use-angle=metal", b)
    self.assertIn("--no-sandbox", b)
    self.assertIn("--use-angle=swiftshader", b)


if __name__ == "__main__":
  unittest.main()

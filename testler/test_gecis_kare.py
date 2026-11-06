"""Geçiş kare sayısı seçimi ve B'nin ilk n karesine bindirme hesabı (saf işlevler; ağ/ffmpeg yok)."""
import io, os, sys, unittest
from contextlib import redirect_stdout

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
import birlestir as b


def sahneler(*kareler, **ek):
  return [{"no": i + 1, "klasor": f"s{i + 1}", "kare": k, **ek.get(f"s{i + 1}", {})}
          for i, k in enumerate(kareler)]


class GecisKareSecimi(unittest.TestCase):
  def test_tablo(self):
    self.assertEqual(b.GECIS_KARE, {"YaprakKivrim": 32, "Silgi": 42, "BookFlip": 12})

  def test_ad_basina_kare(self):
    S = sahneler(200, 200, 200, 200, s1={"gecis": "YaprakKivrim"}, s2={"gecis": "Silgi"},
                 s3={"gecis": "fade"})
    g = b.gecis_kareleri(S, 12)
    self.assertEqual([x and (x["ad"], x["n"]) for x in g],
                     [("YaprakKivrim", 32), ("Silgi", 42), ("fade", 12), None])

  def test_gecis_yok_ya_da_bookflip_yaprak_kivrim(self):
    S = sahneler(200, 200, 200, s2={"gecis": "BookFlip"})
    g = b.gecis_kareleri(S, 12)
    self.assertEqual([x["ad"] for x in g[:2]], ["YaprakKivrim", "YaprakKivrim"])
    self.assertEqual([x["n"] for x in g[:2]], [32, 32])

  def test_sahnedeki_acik_gecis_kare_kazanir(self):
    S = sahneler(200, 200, s1={"gecis": "Silgi", "gecis_kare": 20})
    self.assertEqual(b.gecis_kareleri(S, 12)[0]["n"], 20)

  def test_bilinmeyen_ad_varsayilan_ve_uyari(self):
    cikti = io.StringIO()
    with redirect_stdout(cikti):
      g = b.gecis_kareleri(sahneler(200, 200, s1={"gecis": "Yokboyle"}), 12)
    self.assertEqual((g[0]["ad"], g[0]["n"]), ("YaprakKivrim", 32))
    self.assertIn("uyarı", cikti.getvalue())


class Bindirme(unittest.TestCase):
  def plan(self, N=12):
    S = sahneler(102, 484, 475, 521, s1={"gecis": "YaprakKivrim"}, s2={"gecis": "Silgi"},
                 s3={"gecis": "BookFlip"})
    return S, b.planla(S, N, "YaprakKivrim", b.gecis_kareleri(S, N))

  def test_b_govdesi_gecis_karesinden_baslar(self):
    _, p = self.plan()
    self.assertEqual([x["bas"] for x in p], [0, 32, 42, 32])

  def test_a_govdesi_k_eksi_n_biter_a_pencereleri_kesilmez(self):
    _, p = self.plan()
    self.assertEqual([x["son"] for x in p], [90, 472, 463, 521])

  def test_toplam_kare_ve_ofsetler_degismez(self):
    S, p = self.plan()
    eski = b.planla(S, 12)
    self.assertEqual([x["ofs"] for x in p], [x["ofs"] for x in eski])
    self.assertEqual(b.toplam_kare(p, 12), sum(s["kare"] for s in S) - 12 * (len(S) - 1))

  def test_parca_kareleri_toplami_toplama_esit(self):
    S, p = self.plan()
    govde = sum(x["son"] - x["bas"] for x in p)
    gecis = sum(x["n"] for x in p[:-1])
    self.assertEqual(govde + gecis, b.toplam_kare(p, 12))

  def test_gecissiz_cagri_eski_davranis(self):
    p = b.planla(sahneler(100, 100, 100), 10)
    self.assertEqual([(x["bas"], x["son"]) for x in p], [(0, 90), (10, 90), (10, 100)])


if __name__ == "__main__":
  unittest.main()

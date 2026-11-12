"""birlestir.py saf işlev testleri (ağ/ffmpeg yok)."""
import json, os, sys, unittest

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
import birlestir as b

GL = {"BookFlip", "Fade", "Cube"}


def sahneler(*kareler, **gecisler):
    return [{"no": i + 1, "klasor": f"s{i + 1}", "kare": k, **({"gecis": gecisler[f"g{i + 1}"]} if f"g{i + 1}" in gecisler else {})}
            for i, k in enumerate(kareler)]


class Planla(unittest.TestCase):
    def test_ofsetler_toplam_kare_eksi_n(self):
        N, S = 15, sahneler(240, 300, 250, 240)
        p = b.planla(S, N)
        self.assertEqual([x["ofs"] for x in p], [0, 225, 510, 745])
        self.assertEqual(p[-1]["ofs"], sum(s["kare"] - N for s in S[:-1]))

    def test_toplam_ofs_arti_n(self):
        N, S = 12, sahneler(222, 445, 453)
        p = b.planla(S, N)
        son_ofs_sonrasi = sum(s["kare"] - N for s in S)   # döngü sonu ofs
        self.assertEqual(b.toplam_kare(p, N), son_ofs_sonrasi + N)
        self.assertEqual(b.toplam_kare(p, N), sum(s["kare"] for s in S) - N * (len(S) - 1))

    def test_govde_araligi(self):
        p = b.planla(sahneler(100, 100, 100), 10)
        self.assertEqual([(x["bas"], x["son"]) for x in p], [(0, 90), (10, 90), (10, 100)])

    def test_tek_sahne(self):
        p = b.planla(sahneler(50), 10)
        self.assertEqual((p[0]["bas"], p[0]["son"], p[0]["gecis"], b.toplam_kare(p, 10)), (0, 50, None, 50))

    def test_gercek_kare_k_oncelikli(self):
        S = sahneler(100, 100); S[0]["_k"] = 98
        p = b.planla(S, 10)
        self.assertEqual((p[0]["kare"], p[1]["ofs"]), (98, 88))

    def test_sahne_basina_gecis(self):
        p = b.planla(sahneler(60, 60, 60, g1="fade", g2="Cube", g3="fade"), 10, "BookFlip")
        self.assertEqual([x["gecis"] for x in p], ["fade", "Cube", None])   # son sahnenin geçişi yok sayılır

    def test_varsayilan_gecis(self):
        p = b.planla(sahneler(60, 60, 60), 10)
        self.assertEqual([x["gecis"] for x in p], ["BookFlip", "BookFlip", None])
        p = b.planla(sahneler(60, 60, 60, g2="x"), 10, "Cube")
        self.assertEqual([x["gecis"] for x in p], ["Cube", "x", None])


class Gecis(unittest.TestCase):
    def test_tur(self):
        self.assertEqual(b.gecis_turu("BookFlip", GL), "gl")
        self.assertEqual(b.gecis_turu("fade", GL), "xfade")   # gl'de yalnız "Fade" var, küçük harf değil
        self.assertEqual(b.gecis_turu("BookFlip", set()), "xfade")

    def test_gercek_gl_listesi_fade_kucuk_yok(self):
        ad = b.gl_adlari_oku()
        if ad:
            self.assertIn("BookFlip", ad); self.assertNotIn("fade", ad)

    def test_xfade_filtre_tam_n_kare(self):
        f = b.xfade_filtre("fade", 40, 12, 30)
        self.assertIn("trim=start_frame=28:end_frame=40", f)
        self.assertIn("trim=start_frame=0:end_frame=12", f)
        self.assertIn("xfade=transition=fade:duration=0.400000:offset=0", f)


class Karisim(unittest.TestCase):
    def test_anlatimsiz(self):
        self.assertEqual(b.karisim_filtre(False), ["[1:a]loudnorm=I=-16:TP=-1.5:LRA=11[s]"])

    def test_anlatimli(self):
        f = ";".join(b.karisim_filtre(True, 94.333))
        self.assertIn("[1:a]volume=0.35[e]", f)
        self.assertIn("[2:a]apad[an]", f)
        self.assertIn("amix=inputs=2:duration=longest:normalize=0", f)
        self.assertIn("atrim=duration=94.333", f)
        self.assertTrue(f.endswith("loudnorm=I=-16:TP=-1.5:LRA=11[s]"))


class Kontrol(unittest.TestCase):
    def test_on_iki_karo_zaman(self):
        e = b.kontrol_etiketleri(1200, 30)
        self.assertEqual(len(e), 12)
        self.assertEqual(e[0], (0, "k=0  t=0.00 sn")); self.assertEqual(e[1][0], 100)

    def test_kisa_video(self):
        self.assertEqual(len(b.kontrol_etiketleri(5, 30)), 5)


class Plan(unittest.TestCase):
    def test_zaman_json_tablosu(self):
        with open(os.path.join(KOK, "projeler/present-continuous/zaman.json")) as f: z = json.load(f)
        N = z["gecis_kare"]
        p = b.planla(z["sahneler"], N)
        gercek = {s["klasor"]: None for s in z["sahneler"]}
        t = b.plan_tablosu(p, N, z["fps"], gercek, GL, "x.wav", 93.33)
        self.assertIn("yok", t); self.assertIn("fade (xfade)", t); self.assertIn("BookFlip (gl)", t)
        self.assertIn("TOPLAM 2650 kare = 88.33 sn", t); self.assertIn("x.wav  93.33 sn", t)
        self.assertEqual(len(t.splitlines()), 1 + 6 + 3)

    def test_gercek_kare_farki_isaretlenir(self):
        S = sahneler(100, 100); p = b.planla(S, 10)
        t = b.plan_tablosu(p, 10, 30, {"s1": 100, "s2": 99}, GL)
        self.assertIn("99!", t); self.assertIn("anlatım: yok", t)


class Tema(unittest.TestCase):
    def test_varsayilan_acik(self):
        self.assertEqual(b.tema_oku({}), "acik")
        self.assertEqual(b.tema_oku({"tema": None}), "acik")

    def test_zaman_json_ve_ezme(self):
        self.assertEqual(b.tema_oku({"tema": "koyu"}), "koyu")
        self.assertEqual(b.tema_oku({"tema": "koyu"}, "acik"), "acik")

    def test_gecersiz_tema(self):
        with self.assertRaises(ValueError): b.tema_oku({"tema": "mavi"})

    def test_cikti_adi(self):
        self.assertEqual(b.cikti_adi("acik"), "cikti.mp4")
        self.assertEqual(b.cikti_adi("koyu"), "cikti-koyu.mp4")
        self.assertEqual(b.cikti_adi("koyu", "kontrol"), "kontrol-koyu.mp4")

    def test_plan_tablosu_tema_satiri(self):
        p = b.planla(sahneler(100, 100), 10)
        t = b.plan_tablosu(p, 10, 30, {}, GL)
        self.assertIn("tema: acik  (çıktı: cikti.mp4)", t)
        t = b.plan_tablosu(p, 10, 30, {}, GL, None, None, "koyu")
        self.assertIn("tema: koyu  (çıktı: cikti-koyu.mp4)", t)

    def test_zaman_json_temasi_acik(self):
        with open(os.path.join(KOK, "projeler/present-continuous/zaman.json")) as f: z = json.load(f)
        self.assertEqual(b.tema_oku(z), "acik")


OLAYLAR = [{"kare": 1, "tur": "cizgi"}, {"kare": 2, "tur": "tik"}, {"kare": 3, "tur": "vurus"},
           {"kare": 4, "tur": "cizgi"}, {"kare": 5, "tur": "sayfa"}]


class Efekt(unittest.TestCase):
    def test_hisirti_yalniz_cizgi(self):
        r = b.olaylari_suz(OLAYLAR, "hisirti")
        self.assertEqual([o["kare"] for o in r], [1, 4])
        self.assertTrue(all(o["tur"] == "cizgi" for o in r))

    def test_tam_hepsi(self):
        self.assertEqual(b.olaylari_suz(OLAYLAR, "tam"), OLAYLAR)

    def test_sayfa_hisirti_kipinde_eklenmez(self):
        self.assertEqual(b.olaylari_suz([{"kare": 9, "tur": "sayfa", "guc": 0.8}], "hisirti"), [])

    def test_efekt_oku_oncelik(self):
        self.assertEqual(b.efekt_oku({}), "hisirti")
        self.assertEqual(b.efekt_oku({"efekt": "tam"}), "tam")
        self.assertEqual(b.efekt_oku({"efekt": "tam"}, "hisirti"), "hisirti")


class Yol(unittest.TestCase):
    def test_mutlak_ve_goreli(self):
        self.assertEqual(b.yol_coz("/a/b.wav", "/x"), "/a/b.wav")
        self.assertEqual(b.yol_coz("zaman.json", KOK + "/projeler/present-continuous", KOK),
                         KOK + "/projeler/present-continuous/zaman.json")
        self.assertEqual(b.yol_coz("yok.wav", "/p", "/k"), "/p/yok.wav")



class KapiOnTesti(unittest.TestCase):
    """KAPI-ÖN (12.11, D-0146): grammar paketi tutanak kapısından geçmeden birleştirilmez."""

    def setUp(self):
        import tempfile
        self.d = tempfile.TemporaryDirectory(); self.addCleanup(self.d.cleanup)
        self.da = os.path.join(self.d.name, "da", "araclar", "sema"); os.makedirs(self.da)
        self.paket = os.path.join(self.d.name, "projeler", "ders-temel"); os.makedirs(self.paket)
        open(os.path.join(self.paket, "surumler.json"), "w").write("{}")
        self.eski = b.DA_KOK; b.DA_KOK = os.path.join(self.d.name, "da")
        self.addCleanup(setattr, b, "DA_KOK", self.eski)

    def _sahte(self, kod):
        open(os.path.join(self.da, "tutanak_on.py"), "w").write(
            "import sys\nprint('KAPI-ÖN SAHTE ' + sys.argv[2])\nsys.exit(%d)\n" % kod)

    def test_paket_disi_kapsam_disi(self):
        self.assertIsNone(b.kapi_on(os.path.join(self.d.name, "ornek", "ucan-makine")))

    def test_surumler_yoksa_kapsam_disi(self):
        yol = os.path.join(self.d.name, "projeler", "taslak"); os.makedirs(yol)
        self.assertIsNone(b.kapi_on(yol))

    def test_bayat_kod_doner(self):
        self._sahte(5)
        kod, ileti = b.kapi_on(self.paket)
        self.assertEqual(kod, 5)
        self.assertIn("KAPI-ÖN SAHTE", ileti)

    def test_gecti(self):
        self._sahte(0)
        self.assertEqual(b.kapi_on(self.paket)[0], 0)

if __name__ == "__main__":
    unittest.main()


class HisirtiHacim(unittest.TestCase):
    def test_hisirti_kipinde_hacim_yuksek(self):
        import birlestir as b
        h = b.karisim_filtre(True, 10.0, "hisirti")[0]
        self.assertIn(f"volume={b.EFEKT_VOLUME_HISIRTI}", h)
        self.assertIn(f"volume={b.EFEKT_VOLUME}", b.karisim_filtre(True, 10.0, "tam")[0])

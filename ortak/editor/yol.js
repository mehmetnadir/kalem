// Editör yol yardımcıları: proje adı adres çubuğundan okunur, mutlak yol tek yerde kurulur.
// Klasik betik (onizle.js) ve modül (harita.js) globalThis.KalemYol'u kullanır; Node testi require eder.
(function (kok) {
  var Y = {
    // /p/<proje>/... ya da eski /projeler/<proje>/... adresinden proje adı; yoksa null
    projeAdi: function (yol) {
      var y = yol === undefined ? kok.location.pathname : yol;
      var m = /^\/(?:p|projeler)\/([^/]+)\//.exec(y);
      return m ? decodeURIComponent(m[1]) : null;
    },
    // proje veri dizini (zaman.json, sahneler/, ortak/, cikti.mp4)
    projeYolu: function (ad) { return '/projeler/' + encodeURIComponent(ad) + '/'; },
    // editör sayfası: /p/<proje>/<sayfa>?<sorgu>
    editorYolu: function (sayfa, sorgu, ad) {
      var proje = ad || Y.projeAdi();
      var q = sorgu ? (typeof sorgu === 'string' ? sorgu : new URLSearchParams(sorgu).toString()) : '';
      return '/p/' + encodeURIComponent(proje) + '/' + sayfa + (q ? '?' + q : '');
    },
    // sürümün üretilmiş videosu: önizleme adresindeki projenin cikti.mp4 (koyu: cikti-koyu.mp4); yoksa null
    ciktiYolu: function (onizleme, koyu) {
      var ad = onizleme ? Y.projeAdi(String(onizleme).split('?')[0]) : null;
      return ad ? Y.projeYolu(ad) + (koyu ? 'cikti-koyu.mp4' : 'cikti.mp4') : null;
    },
    // veri dosyalarında kalan eski /projeler/<proje>/(harita|onizle).html adresini yeniye çevirir
    yeniAdres: function (a) {
      var m = /^\/projeler\/([^/]+)\/((?:harita|onizle)\.html)(.*)$/.exec(a || '');
      return m ? '/p/' + m[1] + '/' + m[2] + m[3] : a;
    },
  };
  kok.KalemYol = Y;
  if (typeof module !== 'undefined' && module.exports) module.exports = Y;
})(typeof globalThis !== 'undefined' ? globalThis : this);

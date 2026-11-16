// sahne-kare hata mesajı ve toplayıcı testleri — node --test araclar/test/
import { test } from "node:test";
import assert from "node:assert/strict";
import { hazirOlmadiMesaji } from "../sahne-kare.mjs";

test("hazirOlmadiMesaji boş listelerde eski metni aynen korur", () => {
  const url = "http://127.0.0.1:3012/projeler/demo/sahneler/s1/proje/index.html?canli=1";
  const sonuc = hazirOlmadiMesaji(url);
  assert.equal(sonuc, `sahne hazır olmadı (sayaç yok): ${url}`);

  const sonucBosDiziler = hazirOlmadiMesaji(url, [], []);
  assert.equal(sonucBosDiziler, `sahne hazır olmadı (sayaç yok): ${url}`);
});

test("hazirOlmadiMesaji gsap 404 ve referenceError durumunu içerir", () => {
  const url = "http://127.0.0.1:3012/projeler/demo/sahneler/s1/proje/index.html?canli=1";
  const istisnalar = ["ReferenceError: gsap is not defined"];
  const basarisizlar = [{ yol: "/lib/gsap.min.js", durum: 404 }];

  const sonuc = hazirOlmadiMesaji(url, istisnalar, basarisizlar);
  assert.ok(sonuc.includes("sahne hazır olmadı (sayaç yok): " + url));
  assert.ok(sonuc.includes(" · sayfa hatası: ReferenceError: gsap is not defined"));
  assert.ok(sonuc.includes(" · başarısız istek: /lib/gsap.min.js 404"));
  assert.ok(sonuc.includes("gsap is not defined"));
  assert.ok(sonuc.includes("/lib/gsap.min.js 404"));
});

test("hazirOlmadiMesaji yalnızca ilk istisna ve ilk başarısız isteği ekler", () => {
  const url = "http://127.0.0.1:3012/test";
  const istisnalar = ["IlkHata: birinci", "IkinciHata: ikinci", "UcuncuHata: ucuncu", "Dorduncu: dort"];
  const basarisizlar = [
    { yol: "/a.js", durum: 404 },
    { yol: "/b.js", durum: 500 },
    { yol: "/c.js", durum: "net::ERR_FAILED" },
    { yol: "/d.js", durum: 403 },
    { yol: "/e.js", durum: 404 },
    { yol: "/f.js", durum: 400 },
  ];

  const sonuc = hazirOlmadiMesaji(url, istisnalar, basarisizlar);
  assert.equal(
    sonuc,
    "sahne hazır olmadı (sayaç yok): http://127.0.0.1:3012/test · sayfa hatası: IlkHata: birinci" +
      " · başarısız istek: /a.js 404"
  );
  assert.ok(!sonuc.includes("IkinciHata"));
  assert.ok(!sonuc.includes("/b.js"));
});

test("hazirOlmadiMesaji yalnızca istisna varken başarısız istek eklemez", () => {
  const url = "http://127.0.0.1:3012/test";
  const sonuc = hazirOlmadiMesaji(url, ["TypeError: fail"], []);
  assert.equal(sonuc, "sahne hazır olmadı (sayaç yok): http://127.0.0.1:3012/test · sayfa hatası: TypeError: fail");
});

test("hazirOlmadiMesaji yalnızca başarısız istek varken istisna eklemez", () => {
  const url = "http://127.0.0.1:3012/test";
  const sonuc = hazirOlmadiMesaji(url, [], [{ yol: "/stil.css", durum: 404 }]);
  assert.equal(
    sonuc,
    "sahne hazır olmadı (sayaç yok): http://127.0.0.1:3012/test · başarısız istek: /stil.css 404"
  );
});

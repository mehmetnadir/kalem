// testler/test_cakisma_olcer.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { kesisim, icinde, carpisma, olaylariBirlestir } from "../araclar/cakisma-olcer.mjs";

test("kesisim ve icinde fonksiyonları doğru çalışır", () => {
  const k1 = { x: 10, y: 10, w: 50, h: 50 };
  const k2 = { x: 30, y: 30, w: 50, h: 50 };
  const k3 = { x: 100, y: 100, w: 20, h: 20 };
  const k4 = { x: 15, y: 15, w: 20, h: 20 };

  // kesisim
  const ks12 = kesisim(k1, k2);
  assert.deepEqual(ks12, { x: 30, y: 30, w: 30, h: 30 });

  const ks13 = kesisim(k1, k3);
  assert.equal(ks13, null);

  // icinde (k4 k1'in içinde)
  assert.equal(icinde(k4, k1), true);
  assert.equal(icinde(k1, k4), false);
  assert.equal(icinde(k1, k2), false);
});

test("yazi × cizim, yazi × kunye, cizim × kunye hata üretir", () => {
  const yazi = { tur: "yazi", ad: "metin1", x: 10, y: 10, w: 60, h: 30 };
  const cizim = { tur: "cizim", ad: "agac", x: 40, y: 20, w: 100, h: 100 };
  const kunye = { tur: "kunye", ad: "kunye:ders", x: 20, y: 15, w: 80, h: 40 };

  const c1 = carpisma([yazi, cizim]);
  assert.equal(c1.length, 1);
  assert.equal(c1[0].tip, "hata");

  const c2 = carpisma([yazi, kunye]);
  assert.equal(c2.length, 1);
  assert.equal(c2[0].tip, "hata");

  const c3 = carpisma([cizim, kunye]);
  assert.equal(c3.length, 1);
  assert.equal(c3[0].tip, "hata");
});

test("kart içi yazı muaftır (çakışma sayılmaz)", () => {
  const kart = { tur: "kart", ad: "formulKarti", x: 100, y: 100, w: 200, h: 150 };
  const yaziIceride = { tur: "yazi", ad: "formulMetin", x: 120, y: 120, w: 80, h: 30 };

  const c1 = carpisma([kart, yaziIceride]);
  assert.equal(c1.length, 0);

  // Kart dışına taşmış yazı (yazi × kart kuralı yok, sayılmaz)
  const yaziDisarida = { tur: "yazi", ad: "tasanMetin", x: 50, y: 50, w: 80, h: 80 };
  const c2 = carpisma([kart, yaziDisarida]);
  assert.equal(c2.length, 0);
});

test("isaret türü muaftır (çakışma sayılmaz)", () => {
  const yazi = { tur: "yazi", ad: "ornekSozcuk", x: 50, y: 50, w: 60, h: 30 };
  const cizim = { tur: "cizim", ad: "kedi", x: 50, y: 50, w: 60, h: 30 };
  const halka = { tur: "isaret", ad: "halka:ornek", x: 45, y: 45, w: 70, h: 40 };

  const c1 = carpisma([yazi, halka]);
  assert.equal(c1.length, 0);

  const c2 = carpisma([cizim, halka]);
  assert.equal(c2.length, 0);
});

test("pay altı kesişim sayılmaz (tolerans)", () => {
  const yazi = { tur: "yazi", ad: "yazi1", x: 0, y: 0, w: 20, h: 20 };
  // Kesişim genişliği 3 px, yüksekliği 20 px (genişlik <= pay: 4)
  const cizim1 = { tur: "cizim", ad: "cizim1", x: 17, y: 0, w: 20, h: 20 };
  const c1 = carpisma([yazi, cizim1], { pay: 4 });
  assert.equal(c1.length, 0);

  // Kesişim 5x5 px (her iki boyutta > 4 px)
  const cizim2 = { tur: "cizim", ad: "cizim2", x: 15, y: 15, w: 20, h: 20 };
  const c2 = carpisma([yazi, cizim2], { pay: 4 });
  assert.equal(c2.length, 1);
  assert.equal(c2[0].tip, "hata");
});

test("yazi × yazi (farklı ad) uyari üretir", () => {
  const yazi1 = { tur: "yazi", ad: "satir1", x: 10, y: 10, w: 80, h: 40 };
  const yazi2 = { tur: "yazi", ad: "satir2", x: 40, y: 20, w: 80, h: 40 };

  const c = carpisma([yazi1, yazi2]);
  assert.equal(c.length, 1);
  assert.equal(c[0].tip, "uyari");
});

test("aynı ada sahip öğeler muaftır", () => {
  const yazi1 = { tur: "yazi", ad: "ayniMetin", x: 10, y: 10, w: 80, h: 40 };
  const yazi2 = { tur: "yazi", ad: "ayniMetin", x: 20, y: 15, w: 80, h: 40 };

  const c = carpisma([yazi1, yazi2]);
  assert.equal(c.length, 0);
});

test("ardışık örnek birleştirme doğru çalışır", () => {
  const ogeYazi = { tur: "yazi", ad: "metinA", x: 10, y: 10, w: 50, h: 30 };
  const ogeCizim = { tur: "cizim", ad: "cizimB", x: 20, y: 15, w: 50, h: 50 };

  const c = carpisma([ogeYazi, ogeCizim])[0];

  const ornekler = [
    { t: 1.0, carpismalar: [c], png: "kare-1.0.png" },
    { t: 1.25, carpismalar: [c], png: "kare-1.25.png" },
    { t: 1.5, carpismalar: [c], png: "kare-1.5.png" },
    // 1.75 boş
    { t: 1.75, carpismalar: [] },
    // 2.0 yeniden başlıyor
    { t: 2.0, carpismalar: [c], png: "kare-2.0.png" },
  ];

  const olaylar = olaylariBirlestir(ornekler, { tolerans: 0.3 });
  assert.equal(olaylar.length, 2);

  assert.equal(olaylar[0].t0, 1.0);
  assert.equal(olaylar[0].t1, 1.5);
  assert.equal(olaylar[0].tip, "hata");
  assert.equal(olaylar[0].png, "kare-1.0.png");

  assert.equal(olaylar[1].t0, 2.0);
  assert.equal(olaylar[1].t1, 2.0);
  assert.equal(olaylar[1].tip, "hata");
  assert.equal(olaylar[1].png, "kare-2.0.png");
});

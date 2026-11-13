// HyperFrames çakışma ölçümü: ham öğe → kutu şeması ve kasıtlı örtüşme kuralları.
// node --test araclar/test/hf-kutu.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { HF_TOPLA_JS, hfKutular, cizgiTuru, parcala, adlandir, noktaKutusu, yayOrani } from "../hf-kutu.mjs";
import { carpisma } from "../cakisma-olcer.mjs";

const yazi = (grp, x, y, w, h, ek = {}) => ({ k: "t", tag: "text", grp, kn: false, op: 1, x, y, w, h, ...ek });
const cizgi = (grp, p, sw = 6, ek = {}) => ({ k: "s", tag: "path", grp, kn: false, op: 1, sw, p, ...ek });
// düz yatay çizgi: x0→x1, y sabit (3 px eğim)
const yatay = (x0, x1, y) => [x0, y, (x0 + x1) / 2, y + 3, x1, y];
// elips halka (1.04 tur, kapanmayan): merkez cx,cy
const halkaYolu = (cx, cy, rx, ry) => {
  const p = [];
  for (let i = 0; i < 38; i++) {
    const a = -2.3 + i * (2 * Math.PI * 1.04) / 37;
    p.push(cx + rx * Math.cos(a), cy + ry * Math.sin(a));
  }
  return p;
};
const hatalar = (ham) => carpisma(hfKutular({ og: ham })).filter((c) => c.tip === "hata");
// parçalı çizgi aynı çifti birden çok kez bildirir; olaylariBirlestir ad çiftine göre tek olay yapar
const cift = (h) => new Set(h.map((c) => [c.a.ad, c.b.ad].sort().join(" × ")));

test("HF_TOPLA_JS geçerli bir ifade ve JSON döndürür", () => {
  const f = new Function("return " + HF_TOPLA_JS);
  assert.equal(typeof f, "function");
});

test("cizgiTuru: yassı açık çizgi altcizgi, küçük kapalı halka, uzun köşegen cizim", () => {
  assert.equal(cizgiTuru(yatay(100, 400, 300), 9), "altcizgi");
  assert.equal(cizgiTuru(halkaYolu(300, 300, 80, 44), 7), "halka");
  assert.equal(cizgiTuru([100, 100, 300, 260, 500, 420], 9), "cizim");
  // büyük kapalı çerçeve (kart kenarı) halka sayılmaz
  assert.equal(cizgiTuru(halkaYolu(900, 300, 800, 130), 4.5), "cizim");
});

test("parcala: köşegen çizgi tek büyük AABB yerine küçük parçalara bölünür", () => {
  const p = [];
  for (let i = 0; i <= 20; i++) p.push(100 + i * 20, 100 + i * 20);
  const kutular = parcala(p, 6, 36);
  assert.ok(kutular.length >= 8);
  for (const k of kutular) assert.ok(k.w < 70 && k.h < 70);
});

test("adlandir: grupta tek öğe grup adını, çok öğe grup:tagN adını alır; künye öneki", () => {
  const og = adlandir([
    yazi("w1", 0, 0, 10, 10), yazi("satir", 0, 0, 10, 10), yazi("satir", 20, 0, 10, 10),
    yazi("ku-ders", 0, 0, 10, 10, { kn: true }),
  ]);
  assert.deepEqual(og.map((o) => o.ad), ["w1", "satir:text0", "satir:text1", "kunye:ku-ders"]);
});

test("görünmeyen (opaklık < 0,5) öğe kutu üretmez", () => {
  const k = hfKutular({ og: [yazi("a", 0, 0, 50, 20, { op: 0.3 }), yazi("b", 0, 0, 50, 20)] });
  assert.equal(k.length, 1);
  assert.equal(k[0].ad, "b");
});

test("gerçek kusur: halka komşu sözcüğün harfini keser", () => {
  // hedef sözcük halkanın içinde, komşu sözcük halkanın sağ kenarını geçer
  const hedef = yazi("w1", 260, 280, 80, 40);
  const komsu = yazi("w2", 340, 280, 90, 40);
  const hata = hatalar([hedef, komsu, cizgi("m0", halkaYolu(320, 300, 70, 36), 7)]);
  assert.ok(hata.length > 0);
  assert.ok(hata.every((h) => [h.a.ad, h.b.ad].includes("w2")));
});

test("kasıtlı: halkanın içindeki hedef sözcük hata sayılmaz", () => {
  const hedef = yazi("w1", 270, 285, 100, 30);
  assert.equal(hatalar([hedef, cizgi("m0", halkaYolu(320, 300, 70, 36), 7)]).length, 0);
});

test("kasıtlı: harf dairesinin içindeki harf hata sayılmaz", () => {
  const harf = yazi("A", 134, 485, 24, 30);
  assert.equal(hatalar([harf, cizgi("chip", halkaYolu(146, 500, 32, 32), 4)]).length, 0);
});

test("kasıtlı: altçizgi kendi sözcüğünün altında, hata değil", () => {
  const soz = yazi("w9", 200, 300, 120, 62);
  assert.equal(hatalar([soz, cizgi("bl0", yatay(196, 324, 352), 9)]).length, 0);
});

test("gerçek kusur: altçizgi başka satırın sözcüğüne biner", () => {
  const ust = yazi("w1", 200, 300, 120, 62);
  const alt = yazi("w2", 200, 360, 120, 62);
  // çizgi üst sözcüğün altında ama alt satırın sözcüğüne 20 px giriyor
  const hata = hatalar([ust, alt, cizgi("m1", yatay(196, 324, 380), 9)]);
  assert.ok(hata.some((h) => [h.a.ad, h.b.ad].includes("w2")));
});

test("gerçek kusur: iki altçizgi üst üste", () => {
  const hata = hatalar([cizgi("m0", yatay(100, 400, 500), 9), cizgi("m1", yatay(150, 420, 507), 9)]);
  assert.equal(cift(hata).size, 1);
  assert.deepEqual([hata[0].a.tur, hata[0].b.tur], ["altcizgi", "altcizgi"]);
});

test("gerçek kusur: çip/etiket metni çizime biner", () => {
  const metin = yazi("fl0", 400, 250, 200, 56);
  const ok = cizgi("m1", [300, 330, 420, 280, 560, 240, 700, 200], 9);
  assert.ok(hatalar([metin, ok]).length > 0);
});

test("kasıtlı: kart (dolgulu rozet) üstündeki yazı hata değil", () => {
  const kart = { k: "f", tag: "rect", grp: "rz0", kn: false, op: 1, x: 96, y: 150, w: 273, h: 48 };
  const metin = yazi("rz0", 130, 160, 200, 28);
  const k = hfKutular({ og: [kart, metin] });
  assert.equal(k.find((b) => b.tur === "kart").tur, "kart");
  assert.equal(carpisma(k).length, 0);
});

test("künye ile çizim çakışması hata", () => {
  const kunye = yazi("ku-ders", 56, 40, 400, 40, { kn: true });
  const hata = hatalar([kunye, cizgi("m0", yatay(100, 300, 60), 9)]);
  assert.equal(cift(hata).size, 1);
  assert.equal(hata[0].a.tur === "kunye" || hata[0].b.tur === "kunye", true);
});

test("kutu üretmeyen sahne boş dizi döner (kapı 'ölçülmedi' der, sessiz geçmez)", () => {
  assert.deepEqual(hfKutular({ og: [] }), []);
  assert.deepEqual(hfKutular({}), []);
  assert.deepEqual(hfKutular(undefined), []);
});

test("noktaKutusu: pay iki yana eklenir", () => {
  assert.deepEqual(noktaKutusu([10, 20, 30, 50], 2), { x: 8, y: 18, w: 24, h: 34 });
});

test("altçizgi muafiyeti yakınlıkla sınırlı: iki satır yukarıdaki sözcük muaf değil", () => {
  const cokUst = yazi("w0", 200, 100, 120, 62);       // çizgiden 200+ px yukarıda
  const k = hfKutular({ og: [cokUst, cizgi("bl0", yatay(196, 324, 352), 9)] });
  assert.equal(k.find((b) => b.tur === "altcizgi").muaf, undefined);
});

test("kasıtlı: aynı çizginin üst üste yeniden çizimi (boşluk çizgisi + vurgu) hata değil", () => {
  const alt = cizgi("bl0", yatay(518, 732, 293), 5), vurgu = cizgi("m2", yatay(516, 734, 293), 8);
  assert.equal(hatalar([alt, vurgu]).length, 0);
  assert.equal(hatalar([vurgu, cizgi("gb0", yatay(516, 734, 293), 8)]).length, 0);
});

test("gerçek kusur: halkanın kenarına yapışan komşu harf (uçtaki 'I') hedef sayılmaz", () => {
  // halka merkez 320, yarıçap 70: sol kenar 250; "I" kutusu 252-262 halkanın bbox'ının içinde ama elips dışında
  const kenar = yazi("w0", 252, 285, 10, 30);
  const hata = hatalar([kenar, cizgi("m0", halkaYolu(320, 300, 70, 36), 7)]);
  assert.ok(hata.length > 0);
});

test("kasıtlı: sözcüğün üstündeki çarpı (iki düz köşegen) hata değil; dışarıdan geçen ok hata", () => {
  const soz = yazi("rowD", 212, 780, 88, 46);
  const x1 = cizgi("dx1", [202, 772, 258, 798, 314, 824], 8), x2 = cizgi("dx2", [314, 772, 258, 798, 202, 824], 8);
  assert.equal(hatalar([soz, x1, x2]).length, 0);
  const ok = cizgi("gS", [150, 900, 260, 840, 330, 700], 9);   // sözcüğün içinden kıvrımla dışarı çıkıyor
  assert.ok(hatalar([soz, ok]).length > 0);
});

test("kasıtlı: sözcüğün orta bandındaki yatay çizgi (üstü çizili) hata değil", () => {
  const soz = yazi("k10", 96, 430, 548, 120);
  assert.equal(hatalar([soz, cizgi("kx", yatay(84, 418, 477), 10)]).length, 0);
});

test("kasıtlı: çizgi + ok ucu uç uca temas (altçizgi × altçizgi, kısa örtüşme) hata değil", () => {
  assert.equal(hatalar([cizgi("bl", yatay(130, 796, 468), 21), cizgi("bok", yatay(782, 925, 468), 4)]).length, 0);
});

test("gerçek kusur: tamamlanmamış halka yayı komşu sözcüğü keser; içindeki hedef muaf kalır", () => {
  // yay: ~270 derece (kapanmamış), hedef içeride, komşu sağ kenarda
  const p = [];
  for (let i = 0; i < 28; i++) { const a = -2.3 + i * 0.17; p.push(320 + 70 * Math.cos(a), 300 + 36 * Math.sin(a)); }
  const hedef = yazi("w1", 270, 285, 100, 30), komsu = yazi("w2", 372, 280, 60, 40);
  const hata = hatalar([hedef, komsu, cizgi("m0", p, 7)]);
  assert.ok(hata.some((h) => [h.a.ad, h.b.ad].includes("w2")));
  assert.ok(!hata.some((h) => [h.a.ad, h.b.ad].includes("w1")));
});

test("yayOrani: düz çizgi 1, kapalı halka 0'a yakın", () => {
  assert.ok(yayOrani([0, 0, 50, 0, 100, 0]) > 0.99);
  assert.ok(yayOrani(halkaYolu(300, 300, 80, 44)) < 0.2);
});

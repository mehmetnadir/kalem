// Oynatma çekirdeği (ortak/oynatici/cekirdek.js) — editör ve oynatıcının ortak kodu.
// node --test araclar/test/ · Sahte tampon: iframe yerine { style, src, contentWindow.postMessage }
// kaydı; sarmal div `y` ile kıvrım.
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const KOK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
await import(path.join(KOK, "ortak", "oynatici", "cekirdek.js"));
const C = globalThis.KalemCekirdek;
const Z = JSON.parse(fs.readFileSync(
  path.join(KOK, "projeler", "present-perfect-temel", "zaman.json")));

function tampon(idx, sarmal = true) {
  const mesaj = [];
  const s = { idx, no: -1, hazir: false, goster: false, sonT: null, sonF: -1, op: -1, z: -1,
    tr: null, mesaj,
    f: { style: {}, src: "", contentWindow: { postMessage: (m) => mesaj.push(m) } } };
  if (sarmal) s.y = { style: {}, sinif: new Set(),
    classList: { toggle(ad, v) { v ? s.y.sinif.add(ad) : s.y.sinif.delete(ad); } } };
  return s;
}
function pencere(S, sarmal = true) {
  return { S, paket: "/projeler/p/", tema: "acik", gosterilen: -1,
    slot: [tampon(0, sarmal), tampon(1, sarmal)] };
}
const hazirla = (s) => { s.hazir = true; s.goster = true; };
const yakin = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, `${a} ≈ ${b} değil`);
const uc = (S) => [{ klasor: "01-a", motor: "Paper.js", t_bas: 0, t_son: 3, ad: "A" },
  { klasor: "02-b", motor: "Paper.js", t_bas: 3, t_son: 6, ad: "B", ...S },
  { klasor: "03-c", motor: "Paper.js", t_bas: 6, t_son: 9, ad: "C" }];

test("gecisTur: açık gecis kazanır; yoksa bölüm kuralı; yoksa kıvrım; ilk sahne/az hareket fade",
  () => {
    const S = [{ t_bas: 0, gecis: "BookFlip", bolum: "a" }, { t_bas: 3, gecis: "fade", bolum: "b" },
      { t_bas: 6, bolum: "b" }, { t_bas: 9, bolum: "b" }, { t_bas: 12, bolum: "c" }, { t_bas: 15 }];
    assert.equal(C.gecisTur(S, 0), "fade");
    assert.equal(C.gecisTur(S, 1), "kivrim");          // BookFlip açık
    assert.equal(C.gecisTur(S, 2), "fade");            // gecis: fade açık (bölüm farklı olsa da)
    assert.equal(C.gecisTur(S, 3), "fade");            // aynı bölüm
    assert.equal(C.gecisTur(S, 4), "kivrim");          // bölüm değişti
    assert.equal(C.gecisTur(S, 5), "kivrim");          // bölüm alanı yok
    assert.equal(C.gecisTur(S, 4, true), "fade");      // prefers-reduced-motion
  });

test("present-perfect-temel: 1→2…4→5 kıvrım, 5→6 fade (açık istisna); bolum eklenince aynı", () => {
  const S = Z.sahneler;
  assert.deepEqual([1, 2, 3, 4, 5].map((i) => C.gecisTur(S, i)),
    ["kivrim", "kivrim", "kivrim", "kivrim", "fade"]);
  const S2 = S.map((s) => ({ ...s, bolum: s.ad }));
  assert.deepEqual([1, 2, 3, 4, 5].map((i) => C.gecisTur(S2, i)),
    ["kivrim", "kivrim", "kivrim", "kivrim", "fade"]);
});

test("sahneYonet: boş pencere sahneyi yükler, hazır olunca gösterir, 3 sn kala önyükler", () => {
  const Y = pencere(Z.sahneler);
  let r = C.sahneYonet(0.5, Y, { FPS: 30 });
  assert.equal(r.hazir, false); assert.equal(Y.slot[0].no, 0);
  assert.match(Y.slot[0].f.src,
    /01-hyperframes-giris\/proje\/index\.html\?canli=1&mesaj=1&tbas=0&tema=acik$/);
  assert.equal(Y.slot[1].no, -1);                    // hazır değilken önyükleme yok
  hazirla(Y.slot[0]);
  r = C.sahneYonet(0.6, Y, { FPS: 30 });
  assert.equal(r.hazir, true); assert.equal(Y.slot[0].op, 1); assert.equal(Y.slot[0].z, 2);
  assert.equal(Y.slot[1].no, 1);                     // t_bas 3 − 3 ≤ 0,6 → 02 önyüklendi
  assert.match(Y.slot[1].f.src, /02-paperjs-kanca\/sayfa\.html/);
  assert.deepEqual(Y.slot[0].mesaj.at(-1), { tip: "zaman", t: 0.6 });
  assert.equal(r.sonraki, null);                     // önyüklenen henüz hazır değil
  hazirla(Y.slot[1]);
  assert.equal(C.sahneYonet(0.7, Y, { FPS: 30 }).sonraki, Y.slot[1]);
});

test("kıvrım: eski tampon döner (z 3, rotateY), yeni tam görünür; bitince önyükleme; fade", () => {
  const Y = pencere(uc({ gecis: "fade" }));
  Y.slot[0].no = 0; Y.slot[1].no = 1; hazirla(Y.slot[0]); hazirla(Y.slot[1]);
  C.sahneYonet(3.3, Y, { FPS: 30 });                  // 1 → 2 kıvrım (0,6 sn): u = yumusak(0,5)
  assert.equal(Y.slot[1].op, 1); assert.equal(Y.slot[0].z, 3);
  assert.equal(Y.slot[0].y.style.transform, "perspective(2400px) rotateY(-45.00deg)");
  assert.ok(Y.slot[0].y.sinif.has("ko-kivrim"));
  assert.equal(Y.slot[0].no, 0);                     // geçiş sürerken eski tampon korunur
  C.sahneYonet(4, Y, { FPS: 30 });                    // geçiş bitti: eski gizli, 03 önyüklendi
  assert.equal(Y.slot[0].op, 0); assert.equal(Y.slot[0].y.style.transform, "");
  assert.equal(Y.slot[0].no, 2);
  hazirla(Y.slot[0]);
  C.sahneYonet(6.2, Y, { FPS: 30 });                  // 2 → 3 fade (0,4 sn): u = yumusak(0,5)
  yakin(Y.slot[0].op, 0.5); assert.equal(Y.slot[1].op, 1); assert.equal(Y.slot[1].z, 1);
});

test("sarmal yoksa (eski editör tamponu) kıvrım fade'e düşer, stil iframe'e uygulanır", () => {
  const Y = pencere(uc({}), false);
  Y.slot[0].no = 0; Y.slot[1].no = 1; hazirla(Y.slot[0]); hazirla(Y.slot[1]);
  C.sahneYonet(3.2, Y, { FPS: 30 });
  yakin(Y.slot[1].f.style.opacity, 0.5); assert.equal(Y.slot[0].f.style.zIndex, 1);
});

test("pasif pencerede geçiş efekti yok: yeni tampon anında tam, eski gizli", () => {
  const Y = pencere(uc({}));
  Y.slot[0].no = 0; Y.slot[1].no = 1; hazirla(Y.slot[0]); hazirla(Y.slot[1]);
  C.sahneYonet(3.1, Y, { FPS: 30, aktif: false });
  assert.equal(Y.slot[1].op, 1); assert.equal(Y.slot[0].op, 0);
  assert.equal(Y.slot[0].y.style.transform, "");
});

test("zaman mesajı bütçesi: etkin her karede, seyrek çift karelerde, pasif saniyede bir", () => {
  const S = [{ klasor: "01-a", motor: "Paper.js", t_bas: 0, t_son: 10, ad: "A" }];
  const say = (sec, anlar) => {
    const Y = pencere(S); Y.slot[0].no = 0; hazirla(Y.slot[0]);
    anlar.forEach((t) => C.sahneYonet(t, Y, { FPS: 30, ...sec }));
    return Y.slot[0].mesaj.length;
  };
  const kareler = Array.from({ length: 60 }, (_, k) => k / 30);          // 2 sn, 60 kare
  assert.equal(say({}, kareler), 60);
  assert.equal(say({ seyrek: true }, kareler), 30);
  assert.equal(say({ aktif: false }, kareler), 2);                       // ilk + 1 sn sonra
  assert.equal(say({}, [1, 1, 1]), 1);                                   // aynı kare: tek mesaj
});

test("hazirMesaj: gönderen tamponu işaretler, temayı yollar; yabancı kaynak null", () => {
  const Y = pencere(Z.sahneler); Y.tema = "koyu"; Y.slot[0].no = 0;
  const s = C.hazirMesaj({ data: { tip: "hazir", tbas: 0, zamanli: true },
    source: Y.slot[0].f.contentWindow }, [Y]);
  assert.equal(s, Y.slot[0]); assert.equal(s.hazir, true); assert.equal(s.goster, true);
  assert.deepEqual(s.mesaj.at(-1), { tip: "tema", ad: "koyu" });
  assert.equal(C.hazirMesaj({ data: { tip: "hazir" }, source: {} }, [Y]), null);
  assert.equal(C.hazirMesaj({ data: { tip: "zaman" }, source: Y.slot[0].f.contentWindow }, [Y]),
    null);
});

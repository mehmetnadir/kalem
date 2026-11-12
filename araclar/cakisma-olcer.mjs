// araclar/cakisma-olcer.mjs
// Saf AABB çakışma ve tolerans ölçer (DOM yok, bağımlılık yok).

/**
 * İki kutunun kesişim dikdörtgenini döner.
 * Kesişim yoksa null döner.
 */
export function kesisim(a, b) {
  if (!a || !b) return null;
  const x0 = Math.max(a.x, b.x);
  const y0 = Math.max(a.y, b.y);
  const x1 = Math.min(a.x + a.w, b.x + b.w);
  const y1 = Math.min(a.y + a.h, b.y + b.h);
  const w = x1 - x0;
  const h = y1 - y0;
  if (w > 0 && h > 0) return { x: x0, y: y0, w, h };
  return null;
}

/**
 * a kutusu tamamen b kutusunun içinde mi? (A ⊆ B)
 */
export function icinde(a, b) {
  if (!a || !b) return false;
  return a.x >= b.x && a.y >= b.y && (a.x + a.w) <= (b.x + b.w) && (a.y + a.h) <= (b.y + b.h);
}

/**
 * Maskeli bir öğenin görünür kutusunu hesaplar.
 * İçerik ile maskenin AABB kesişimini döner. Kesişim yoksa null döner.
 *
 * @param {Object} icerik { x, y, w, h } veya bounds { x, y, width, height }
 * @param {Object} maske  { x, y, w, h } veya bounds { x, y, width, height }
 * @returns {Object|null} { x, y, w, h }
 */
export function gorunurKutu(icerik, maske) {
  if (!icerik || !maske) return null;
  const iw = icerik.w ?? icerik.width ?? 0;
  const ih = icerik.h ?? icerik.height ?? 0;
  const mw = maske.w ?? maske.width ?? 0;
  const mh = maske.h ?? maske.height ?? 0;
  if (iw <= 0 || ih <= 0 || mw <= 0 || mh <= 0) return null;

  const x0 = Math.max(icerik.x, maske.x);
  const y0 = Math.max(icerik.y, maske.y);
  const x1 = Math.min(icerik.x + iw, maske.x + mw);
  const y1 = Math.min(icerik.y + ih, maske.y + mh);
  const w = x1 - x0;
  const h = y1 - y0;
  if (w > 0 && h > 0) {
    return { x: x0, y: y0, w, h };
  }
  return null;
}

/**
 * Kutular listesindeki çakışmaları kurallara göre bulur.
 * Kurallar:
 *  - yazi × cizim, yazi × kunye, cizim × kunye -> 'hata'
 *  - yazi × yazi (farklı ad) -> 'uyari'
 *  - yazi tamamen kart içindeyse ya da öğelerden biri 'isaret' ise sayılmaz
 *  - aynı ad sayılmaz
 *  - kesişim iki boyutta da > pay değilse sayılmaz
 *
 * @param {Array} kutular [{tur, ad, x, y, w, h}]
 * @param {Object} secenekler { pay = 4 }
 * @returns {Array} [{ a, b, tip, kesisim }]
 */
export function carpisma(kutular = [], { pay = 4 } = {}) {
  const sonuclar = [];
  const kartlar = kutular.filter((k) => k.tur === "kart");

  // Bir yazının herhangi bir kart içinde olup olmadığını kontrol et
  const kartIcindeYazi = (yazi) => kartlar.some((kart) => icinde(yazi, kart));

  for (let i = 0; i < kutular.length; i++) {
    const a = kutular[i];
    for (let j = i + 1; j < kutular.length; j++) {
      const b = kutular[j];

      // Aynı ad sayılmaz
      if (a.ad && b.ad && a.ad === b.ad) continue;

      // Öğelerden biri 'isaret' ise sayılmaz
      if (a.tur === "isaret" || b.tur === "isaret") continue;

      // Yazı tamamen kart içindeyse sayılmaz (a veya b kart ise ya da sahnedeki bir kartın içindeyse)
      if (a.tur === "yazi" && b.tur === "kart" && icinde(a, b)) continue;
      if (b.tur === "yazi" && a.tur === "kart" && icinde(b, a)) continue;

      // Tip belirle
      let tip = null;
      if ((a.tur === "yazi" && b.tur === "cizim") || (a.tur === "cizim" && b.tur === "yazi")) {
        // Eğer yazı sahnedeki bir kartın içindeyse ve çizim de o kart ise sayılmaz
        if (a.tur === "yazi" && kartIcindeYazi(a) && b.tur === "cizim" && b.ad === "kart") continue;
        if (b.tur === "yazi" && kartIcindeYazi(b) && a.tur === "cizim" && a.ad === "kart") continue;
        tip = "hata";
      } else if ((a.tur === "yazi" && b.tur === "kunye") || (a.tur === "kunye" && b.tur === "yazi")) {
        tip = "hata";
      } else if ((a.tur === "cizim" && b.tur === "kunye") || (a.tur === "kunye" && b.tur === "cizim")) {
        tip = "hata";
      } else if (a.tur === "yazi" && b.tur === "yazi") {
        tip = "uyari";
      }

      if (!tip) continue;

      const k = kesisim(a, b);
      if (!k) continue;

      // Kesişim iki boyutta da > pay değilse sayılmaz
      if (k.w <= pay || k.h <= pay) continue;

      sonuclar.push({ a, b, tip, kesisim: k });
    }
  }

  return sonuclar;
}

/**
 * Zamanda ardışık örneklerde devam eden aynı çifti tek bir olaya birleştirir.
 *
 * @param {Array} ornekler [{ t, carpismalar: [{ a, b, tip, kesisim }], png }]
 * @param {number} tolerans ardışık sayılma azami zaman farkı (örn. 1.25 / sikilik)
 * @returns {Array} [{ t0, t1, a: adA, b: adB, tip, kesisim, png }]
 */
export function olaylariBirlestir(ornekler = [], { tolerans = 0.3 } = {}) {
  const olaylar = [];
  const aktifOlaylar = new Map(); // kimlik -> olay nesnesi

  for (const ornek of ornekler) {
    const { t, carpismalar = [], png } = ornek;
    const buOrnekKimlikler = new Set();

    for (const c of carpismalar) {
      const adA = c.a?.ad || "";
      const adB = c.b?.ad || "";
      const isimler = [adA, adB].sort();
      const kimlik = `${c.tip}::${isimler[0]}::${isimler[1]}`;
      buOrnekKimlikler.add(kimlik);

      if (aktifOlaylar.has(kimlik)) {
        const olay = aktifOlaylar.get(kimlik);
        olay.t1 = t;
        // Kesişim alanı daha büyükse güncelle
        if (c.kesisim.w * c.kesisim.h > olay.kesisim.w * olay.kesisim.h) {
          olay.kesisim = c.kesisim;
        }
      } else {
        const yeniOlay = {
          t0: t,
          t1: t,
          a: isimler[0],
          b: isimler[1],
          tip: c.tip,
          kesisim: c.kesisim,
          png: png || null,
        };
        aktifOlaylar.set(kimlik, yeniOlay);
        olaylar.push(yeniOlay);
      }
    }

    // Bu örnekte kesilenleri aktif listesinden çıkar
    for (const [kimlik, olay] of aktifOlaylar.entries()) {
      if (!buOrnekKimlikler.has(kimlik)) {
        aktifOlaylar.delete(kimlik);
      }
    }
  }

  return olaylar;
}

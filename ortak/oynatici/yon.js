// Yön çifti (09.11, Nadir: "ekranı dikeye çevirdiğimizde hiç kesinti olmadan yön değişmeli").
// Aynı videonun yatay (16:9) ve dikey (9:16) paketleri aynı ses saatini ve aynı sahne zamanlarını
// paylaşır; oynatıcı ikisini de yükler, görünür pane'i cihaz yönüne göre seçer. Saf mantık, DOM yok
// (node --test araclar/test/oynatici-yon.test.mjs).
"use strict";
export const ZAMAN_TOLERANS = 0.05;                           // sn; sahne başlangıç farkı sınırı

// Paket ölçüsünden yön adı.
export const yonAdi = (genislik, yukseklik) => (genislik >= yukseklik ? "yatay" : "dikey");

// Hangi yön gösterilsin? portre = ekran dikey mi; Y = yüklü yönler {yatay?, dikey?}; zorla = istek.
export function yonIstek(portre, Y, zorla) {
  if (zorla && Y[zorla]) return zorla;
  const iste = portre ? "dikey" : "yatay";
  if (Y[iste]) return iste;
  return Y.yatay ? "yatay" : Y.dikey ? "dikey" : "";
}

// İki paketin sahne listesi kesintisiz geçişe uygun mu: aynı sayı, klasör sırası ve zamanlar.
export function ciftUyumlu(S1, S2) {
  if (!Array.isArray(S1) || !Array.isArray(S2) || !S1.length) return false;
  if (S1.length !== S2.length) return false;
  return S1.every((a, i) => {
    const b = S2[i];
    return a.klasor === b.klasor && Math.abs(a.t_bas - b.t_bas) <= ZAMAN_TOLERANS &&
      Math.abs(a.t_son - b.t_son) <= ZAMAN_TOLERANS;
  });
}

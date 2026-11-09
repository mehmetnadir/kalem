// Basılı tutma hızlandırması (2×) — durum makinesi. YouTube/Instagram davranışı (Nadir 09.11):
// sahneye basılı tut → 2×; basılıyken aşağı sürükle → tepedeki halka dolar, dolunca 2× kilitlenir
// ve parmak kalkınca da sürer; kilit kapsüle dokununca ya da hız menüsünden seçince çözülür.
// Saf mantık; DOM yok (node --test araclar/test/oynatici-turbo.test.mjs). Evreler:
//   bos → bas → bekliyor → sure → aktif → hareket(u ≥ 1) → kilit
//   bekliyor + sapma > SAPMA_PX → bos (kaydırma niyeti) · aktif + birak → bos (tık bastırılır)
"use strict";
export const TURBO_HIZ = 2, BASILI_MS = 500, SAPMA_PX = 12;

export function turboKur() {
  return { evre: "bos", x0: 0, y0: 0, u: 0, esik: 80, tutuyor: false };
}
// Parmak / fare indi. esik = kilit için gereken aşağı sürükleme (px).
// Kilitliyken yeni basış sıradan dokunuştur: kilit bozulmaz, tık geçer (duraklat / kontroller).
export function bas(s, x, y, esik) {
  if (s.evre === "kilit") return s;
  s.evre = "bekliyor"; s.x0 = x; s.y0 = y; s.u = 0; s.esik = Math.max(24, esik || 80);
  s.tutuyor = true;
  return s;
}
// Zamanlayıcı doldu (BASILI_MS). Yalnız hâlâ bekliyorsa etkinleşir.
export function sure(s) {
  if (s.evre === "bekliyor") { s.evre = "aktif"; s.u = 0; }
  return s;
}
// Hareket: bekliyorken sapma iptal eder; aktifken aşağı mesafe halkayı doldurur.
export function hareket(s, x, y) {
  if (s.evre === "bekliyor") {
    if (Math.hypot(x - s.x0, y - s.y0) > SAPMA_PX) s.evre = "bos";
  } else if (s.evre === "aktif") {
    s.u = Math.max(0, Math.min(1, (y - s.y0) / s.esik));
    if (s.u >= 1) s.evre = "kilit";
  }
  return s;
}
// Parmak kalktı. Dönüş: bu basışın ardından gelen tık bastırılsın mı?
export function birak(s) {
  const bastir = s.tutuyor && (s.evre === "aktif" || s.evre === "kilit");
  if (s.evre !== "kilit") { s.evre = "bos"; s.u = 0; }
  s.tutuyor = false;
  return bastir;
}
export function kapat(s) { s.evre = "bos"; s.u = 0; s.tutuyor = false; return s; }
export const hizli = (s) => s.evre === "aktif" || s.evre === "kilit";

// Canlı kontrol API'sini sunucunun içinden yoklar (jeton değeri yazdırılmaz; yalnız ortam değişkeninden okunur).
// Kullanım (srv21, root): cd /var/www/videokayit && node --env-file=.env <bu dosya> <yol?sorgu> [jq benzeri anahtar yolu]
// Örnek: node --env-file=.env api-yokla.mjs "/api/kontrol/youtube?oge=02-04-ydt-temel" eksikler
const [yol, anahtar] = process.argv.slice(2);
if (!yol) {
  console.error("kullanım: api-yokla.mjs <yol?sorgu> [anahtar.yolu]");
  process.exit(2);
}
const jeton = process.env.KONTROL_ISCI_JETON ?? "";
if (!jeton) {
  console.error("KONTROL_ISCI_JETON tanımlı değil");
  process.exit(2);
}
const taban = `http://127.0.0.1:${process.env.YOKLA_PORT ?? "3810"}`;
const y = await fetch(taban + yol, { headers: { "x-kontrol-jeton": jeton, "x-kontrol-isci": "sef" } });
const metin = await y.text();
let veri;
try {
  veri = JSON.parse(metin);
} catch {
  console.log(y.status, metin.slice(0, 400));
  process.exit(0);
}
let secim = veri;
for (const p of (anahtar ?? "").split(".").filter(Boolean)) secim = secim?.[p];
const cikti = JSON.stringify(secim, null, 1);
console.log(y.status, cikti.length > 6000 ? cikti.slice(0, 6000) + "\n…(kırpıldı)" : cikti);

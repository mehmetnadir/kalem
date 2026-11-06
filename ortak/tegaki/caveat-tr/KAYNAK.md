# Caveat Türkçe el yazısı verisi (tegaki glif verisi)

- Font: Caveat 400 + 700 (Google Fonts, SIL Open Font License 1.1; telif Caveat Project Authors).
  Font dosyası depoda değil (`ortak/font/caveat-*.woff2` ile aynı aile); burada yalnız darbe verisi var.
- Üretici: tegaki (MIT, github.com/gkurt/tegaki) `bun start generate Caveat --weights 400,700 -c "<karakterler>"`,
  pipeline geometry; 05.11.2026, klon `~/01dev/_deneme/tegaki` (commit 32654a4 + PR #80 Latin Extended).
- Karakter kümesi: ASCII + Türkçe harfler (ç ğ ı İ ö ş ü ve büyükleri) + noktalama ve tırnaklar
  (`'` `"` `“ ” ‘ ’ « »` `– —` `…`); `→` fontta yok (ok işareti kalem yolu olarak çizilir).
- Biçim: `glyphData[ch] = {w, t, s: [{p: [[x, y, kalınlık]…], d, a, n?}]}` — font birimi (1000/em),
  y AŞAĞI pozitif, 0 = taban çizgisi; t/d/a saniye; `n` nib damgaları `[noktaIdx, dx, dy, çapA, çapB, açı]`
  (noktalar ve i/ö/ü noktaları yalnız burada). Tarif: `~/.claude/skills/el-yazisi-efekti/SKILL.md` §4-B.
- Kullanım: `kalem-canvas.js` `yaziDarbeleri()` + `yaziCiz()`; sahne öğesi `S.elYazisi()`.
- 06.11: â Â eklendi (üretici aynı; komut: bun start generate Caveat -c "<anahtarlar>âÂ").

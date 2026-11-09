# Teslim kapısı — oynatıcı v3 (prototip 0.3, 09.11.2026) — KISMEN (tarayıcı doğrulaması bekliyor)

Nadir 09.11: "yatay ekrandayız, ekranı dikeye çevirdik; hiç kesinti olmadan video yönü değişmeli" +
"tam ekran düğmesine yatay/dikey desteğini gösteren minik animasyon".

Yapılan: `yon.js` (yön adı, yön isteği, çift uyumu) + `kalem-oynatici.js` 0.3.0: yön başına pane + 2 iframe
tamponu; tek `<audio>` saati ortak; `(orientation: portrait)` değişince yalnız görünen pane değişir (0,15 sn
saydamlık geçişi). Dokunmatik cihazda iki yön SICAK (pasif yön sahneleri yüklü, saniyede 1 zaman mesajı; dönüşte
ilk kare anında doğru). Masaüstünde pasif yön tembel: eski pane yeni kutuda kalır, yeni yön hazır olunca geçer.
Yön çifti varken tam ekranda yön kilidi YOK. Tam ekran simgesi: köşeler + küçük telefon, 7 sn'de bir 0 → 90° → 0
(`ko-tel`), üstüne gelince hızlı; `prefers-reduced-motion` durdurur. Sayfa (`index.html`) `surumler.json`'dan
`ana-yatay` + `dikey-tam` çiftini verir, `yon` olayıyla düzeni izler; `?yon=` ve `?sicak=1` deneme anahtarları.

| # | Madde | Sonuç | Kanıt |
|---|---|---|---|
| 1 | Görüntüye bakıldı | BEKLİYOR | `oynatici-kare.mjs --dondur GxY` (yeni yön kaç ms'de göründü, ses saati kesildi mi) hazır; koşu bu Mac'in yükü (load 225–300, başka oturum) düşünce arka planda koşar: yatay→dikey ve dikey→yatay dokunmatik sıcak, masaüstü tembel, simge karesi |
| 2 | Emoji taraması | GEÇTİ | temiz (5 dosya) |
| 3 | Yapay görünüm | GEÇTİ | yeni görsel yalnız simge içi telefon dikdörtgeni; palet değişmedi |
| 4 | Hareket | GEÇTİ | pane geçişi 150 ms, telefon dönüşü 7 sn döngü (hareket bütçesi: süreklilik ipucu); reduced-motion genel kuralı |
| 5 | Erişilebilirlik | GEÇTİ (kod) | canlı bölge "Dikey görünüm / Yatay görünüm"; düğme etiketi "Tam ekran (yatay ve dikey)" |
| 6 | Metin | GEÇTİ | sayfa notu: "cihazı döndür: yatay ↔ dikey kesintisiz" |
| 7 | Algılanan hız / yük | ÖLÇÜLECEK | sıcak kipte sahne yüklemesi ikiye katlanır (2 yön × 2 tampon); telefon ölçümü `oynatici-olcum.mjs --dokunma 1` ile (aynı bekleyen koşu) |
| 8 | Uygulama kipi | GEÇTİ | krom değişmedi |

Testler: `araclar/test/oynatici-yon.test.mjs` (4 test; present-perfect-temel yatay/dikey çifti uyumlu: aynı 6 sahne,
aynı t_bas/t_son, aynı ses) + turbo 5 + yazı darbeleri 8 = 17 GEÇTİ.

# Sahne 04 — Dört çerçeve (HyperFrames, 1089 kare = 1077 içerik + 12 geçiş; t_bas 38,99)

Tema: acik

Durum: önizleme hazır (koyu, sonra açık; son koşu AÇIK). Render, kapı ve kare görüntüsü bu turda YOK (şef EK 13.11 12:40).

## İçerik
- `panel` `kavram_karti`: kutu 1 `1) tekrar · kalıcı · genel gerçek` (+ Caveat `bildiğin kullanımlar`). Kutu 2 `2) dört çerçeve`; önce Caveat notları (`Türkçe yanıltır`, `şimdiki · geçmiş · gelecek`), sonra kutu dört alt kutuya bölünür.
- Dört kutu sırayla yanar (sarı kenar): Özet `film` · Tabela `sign` · Tören `promise` · Tarife `flight` (Caveat sarı anahtar sözcük).
- Cümle 10: Caveat `Türkçe seni başka zamana çeker`; sonra üç kutu dolgu (`vurguDolgu`, kök), dördüncü kutu kırmızı kenar + kalemle ünlem (kırmızı yalnız burada), alt satır `3 kök + 1 tuzak` (`tuzak` kırmızı).
- Künye: `Rule`, ajanda etkin Rule. Çizim yok (anahtar sözcükler yazı; hazır ikon yalnız `ortak/cizim` listesinden olabilir).

## Olay ↔ sözcük t0 (sozcukler.json; yerel = küresel − 38,99)
| Olay | Cümle / sözcük | Sözcük t0 | Olay küresel | Yerel | Sapma |
|---|---|---|---|---|---|
| kutu 1 kenarı | 7 Kullanım | 39,54 | 39,54 | 0,55 | 0,00 |
| `1)` | 7 Birinci | 41,22 | 41,22 | 2,23 | 0,00 |
| `tekrar` | 7 tekrar, | 43,70 | 43,70 | 4,71 | 0,00 |
| `kalıcı` | 7 kalıcı | 44,50 | 44,50 | 5,51 | 0,00 |
| `genel gerçek` | 7 genel | 45,46 | 45,46 | 6,47 | 0,00 |
| kutu 2 kenarı + `2)` | 8 İkinci | 47,05 | 47,05 | 8,06 | 0,00 |
| `Türkçe yanıltır` notu | 8 Türkçe | 48,25 | 48,25 | 9,26 | 0,00 |
| `şimdiki` notu | 8 şimdiki, | 50,57 | 50,57 | 11,58 | 0,00 |
| `dört çerçeve` + dört boş alt kutu | 8 dört | 53,13 | 53,13 (+0,22 adım) | 14,14 | 0,00 |
| Özet kutusu yanar | 9 Özet: | 54,80 | 54,80 | 15,81 | 0,00 |
| `film` | 9 film, | 56,96 | 56,96 | 17,97 | 0,00 |
| Tabela kutusu yanar | 9 Tabela | 59,44 | 59,44 | 20,45 | 0,00 |
| `sign` | 9 Tabela | 59,44 | 59,56 | 20,57 | 0,12 |
| Tören kutusu yanar | 9 Tören | 61,04 | 61,04 | 22,05 | 0,00 |
| `promise` | 9 promise | 62,81 | 62,81 | 23,82 | 0,00 |
| Tarife kutusu yanar | 9 Tarife. | 64,70 | 64,70 | 25,71 | 0,00 |
| `3` (alt satır) | 10 Üç | 70,97 | 70,97 | 31,98 | 0,00 |
| üç kutu dolgu (0,30 sn adım) | 10 çerçeveyi | 71,17 | 71,17 | 32,18 | 0,00 |
| `kök` | 10 kök | 71,77 | 71,77 | 32,78 | 0,00 |
| 4. kutu kırmızı kenar + `1` | 10 Dördüncüsü | 73,33 | 73,33 | 34,34 | 0,00 |
| ünlem (kalem) | 10 Dördüncüsü | 73,33 | 73,63 / 73,91 | 34,64 / 34,92 | 0,30 / 0,58 |
| `tuzak` (kırmızı) | 10 tuzak. | 74,25 | 74,25 | 35,26 | 0,00 |
Not: `Tarife` anahtarı `flight` 64,82'de (+0,12). Ünlem çizimi cümle bitimine kadar sürer; `Dördüncüsü` ile başlar, sapma tasarım gereği (önce kenar, sonra ünlem). olaylar.json 29 olay (kare 16–1058).

## Kontroller (kapı/görüntü yok)
- Üretimde taşma sınamaları (assert): kutu 1 metni/notu, notlar, anahtar sözcük ve başlık genişlikleri kutuya sığıyor.
- `node --check` 2 blok OK · yinelenen id yok · `Math.random`/`Date` yok · negatif zaman yok.
- İlk hareket 0,55 sn (kare 16), son olay 35,26 sn (kare ≈ 1058 < 1077); son 12 kare durgun.

## Açık
- Ünlem sapması (0,30 sn / 0,58 sn) tasarım gereği; şef itiraz ederse ünlem `Dördüncüsü` anına çekilir.
- Dolgu `vurguDolgu` ile 0,35 şeffaflık; açık temada soluk sarı (kapı/göz kontrolü QA şeridinde).


## QA 13.11
Kapı: ölçülmedi (HyperFrames). Kareler: k/04-hyperframes-dort-cerceve-{42.6,52.6,62.7,74.4}.png (açık), -57.7.png (koyu). Göz: şef maddesi 5 (vurguDolgu 0,35) açıkta okunur, koyu yazı koyu dolguda kaybolmuyor; dördüncü kart kırmızı yalnız tuzakta. Düzeltme yok. Kalan: yok.

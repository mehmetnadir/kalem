# Sahne 06 — Kural kartı (HyperFrames, 1849 kare = 1837 içerik + 12 geçiş; t_bas 96,65)

Tema: acik

Durum: önizleme hazır (koyu, sonra açık). Render, kapı ve kare görüntüsü bu turda YOK (şef EK 13.11 12:40).

## İçerik
- Soru anı 1 (cümle 20, `yanılgı:` fiil her özneyle aynı kalır): öğrenci başı + el balonu sözcük sözcük, üç çip (I go / He gets / It completes) fiil sarı daire, `?`; 0,5 sn duraklama, sonra grup solar.
- Sol `tanim` kartı, üç blok kademeli: OLUMLU (`I · you · we · they → V`, `he · she · it → V + s`, s sarı kutu) · OLUMSUZ (`özne + don't / doesn't + V`, yardımcı fiiller sarı kutu) · SORU (`Do / Does + özne + V ?`).
- Sağ bölge destek: `ek_ayir` get|s go|es stud|ies (+ "ayrıntı önemli değil", "takıyı tanımak yeter") → `I eat fish.` / `She eat|s fish.` + elle balık → eşleşme çipleri I·you·we·they→don't, he·she·it→doesn't → `They don't eat fish.` (eat soluk) → çipler →Do / →Does + "bilgi sorusu: en başa soru sözcüğü" → `Do you eat fish?`.
- Künye: `Rule` (ajanda etkin 3. sözcük Rule). Kırmızı yok.

## Olay ↔ sözcük t0 (sapma ≤ 0,15; küresel sn, yerel = küresel − 96,65)
| Olay | Cümle / sözcük | Sözcük t0 | Olay küresel | Yerel | Sapma |
|---|---|---|---|---|---|
| `I go` çipi + daire | 20 go, | 98,09 | 98,09 | 1,44 | 0,00 |
| `He gets` çipi | 20 gets, | 98,97 | 98,97 | 2,32 | 0,00 |
| `It completes` çipi | 20 completes. | 99,77 | 99,77 | 3,12 | 0,00 |
| `I` (blok A satır 1) | 21 I, | 105,13 | 105,13 | 8,48 | 0,00 |
| `he` (satır 2) | 21 He, | 109,55 | 109,55 | 12,90 | 0,00 |
| s sarı kutu | 21 se | 112,44 | 112,44 | 15,79 | 0,00 |
| `go|es` | 22 goes, | 121,88 | 121,88 | 25,23 | 0,00 |
| `don't` kutusu (blok B) | 24 /doʊnt/. | 137,73 | 137,73 | 41,08 | 0,00 |
| `doesn't` kutusu | 24 /ˈdʌzənt/. | 141,11 | 141,11 | 44,46 | 0,00 |
| `They don't` kutusu | 25 don't | 144,94 | 144,94 | 48,29 | 0,00 |
| `Do` kutusu (blok C) | 26 do | 149,41 | 149,41 | 52,76 | 0,00 |
| `Do you eat fish?` | 27 Do | 156,60 | 156,60 | 59,95 | 0,00 |

## Kontroller (kapı/görüntü yok)
- Uret sırasında taşma sınaması (assert): kart satırları, çipler, örnek kartları sığıyor. `node --check` 2 blok OK · yinelenen id yok · negatif zaman yok.
- İlk hareket 0,42 sn (kare 13), son hareket 60,71 sn (içerik 61,23 sn): ilk/son 12 kare durgun. olaylar.json 63 olay (kare 13–1798).
- Yazı tabanı ≥ 30 px (en küçük: blok etiketi 30, çip 40). Ok, ✓, ≠ gibi harf dışı simge yazıyla yok (el çizimi yol).

## Açık
- Taslak satır 2 metni `+ don't / doesn't + V` çıplak; `özne +` önüne eklendi (kartın 3. bloğu `özne` kullanıyor). Şef onayı.
- Öğrenci grubu 103,6 sn'de tümüyle solar (küçültme yok; küçültünce yazı 30 px altına inerdi).

## QA 13.11
- Kapı/kare: ALINAMADI (Mac'te CDP zaman aşımı, yük 450; sunucu yolu da takıldı). Düzeltme yok. Sonraki şerit: `sunucu-qa.sh 02-02-ydt-temel 06-hyperframes-kural 100,113,138,156.5 125`.
- 2. tur (sunucu): kapı "ölçülmedi (HyperFrames)". Kareler k/06-…-100, -113, -138, -156.5 (açık), k/koyu/…-125. Göz: üç blok, çipler, s/es/ies, Do/Does kartları, sarı kutular okunur; taşma/binme yok. Düzeltme yok, kalan yok.

- Halka kuralı: DEĞİŞTİ: balondaki üç fiil halkası (go/gets/completes) → fiil altına altçizgi (uret.py `cd%d`, fiilden 0,3 sn sonra). BIRAKILDI: yok. Kare k/…-100.3 (üçüncü çizgi çizim ortasında). Kapı HyperFrames: ölçülmedi.

- zaman eşitleme 13.11: KARE 1849 aynı; sunucuda --hazirla ile yeniden kuruldu (uret.py sözcükten okuyor). Kareler k/…-98.3…156 alındı.

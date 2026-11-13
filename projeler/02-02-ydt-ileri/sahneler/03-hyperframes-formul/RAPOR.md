# Sahne 03 — Formül (HyperFrames, 584 kare = 572 içerik + 12 geçiş; t_bas 19,93)

Tema: acik

Durum: önizleme hazır (koyu, sonra açık; son koşu AÇIK). Render, kapı ve kare görüntüsü bu turda YOK (şef EK 13.11 12:40).

## İçerik
- Aşama 1 (cümle 5): iki ortalı kart, etiket `FORM` / `EK`. Kart 1 `S + V` (altında Caveat `özne`, `yalın fiil`). Kart 2 `he · she · it → V + s`; `s` sarı kutu.
- Aşama 2 (cümle 6): sol iki kart `OLUMSUZ` (`don't` / `doesn't` + V) ve `SORU` (`Do` / `Does` + S + V ?); yardımcı fiiller sarı kutu, `?` sarı. Sağda Caveat el notları: yük yardımcı fiilde · özneye göre · asıl fiil · yalın kalır (altı sarı çizgi).
- Künye: `Rule`, ajanda etkin Rule (ders `SIMPLE PRESENT · YDT ADVANCED`, `ortak/kunye.js` ile aynı). Renk yalnız `RENK` (yeşil yok, kırmızı yok).

## Olay ↔ sözcük t0 (sozcukler.json; yerel = küresel − 19,93)
| Olay | Cümle / sözcük | Sözcük t0 | Olay küresel | Yerel | Sapma |
|---|---|---|---|---|---|
| kart 1 kenarı + `FORM` | 5 Formül | 20,48 | 20,48 | 0,55 | 0,00 |
| `S` + `özne` notu | 5 Özne, | 22,16 | 22,16 | 2,23 | 0,00 |
| `V` + `yalın fiil` notu | 5 yalın | 23,36 | 23,36 | 3,43 | 0,00 |
| kart 2 kenarı + `he` | 5 He, | 24,49 | 24,49 | 4,56 | 0,00 |
| ok `→` | 5 ile | 26,02 | 26,02 | 6,09 | 0,00 |
| `s` sarı kutu | 5 se | 26,90 | 26,90 | 6,97 | 0,00 |
| `don't` sarı kutu | 6 don't, | 31,70 | 31,70 | 11,77 | 0,00 |
| `doesn't` sarı kutu | 6 doesn't, | 32,50 | 32,50 | 12,57 | 0,00 |
| `Do` sarı kutu | 6 do, | 33,58 | 33,58 | 13,65 | 0,00 |
| `Does` sarı kutu | 6 does. | 34,18 | 34,18 | 14,25 | 0,00 |
| `S` (soru kartı) + `özneye göre` | 6 Özneye | 35,47 | 35,47 / 35,57 (S) | 15,54 / 15,64 | 0,00 / 0,10 |
| `V` (iki kart) | 6 fiil | 37,55 | 37,55 | 17,62 | 0,00 |
| `yalın kalır` notu + çizgi | 6 yalın / kalır. | 38,11 / 38,43 | 38,11 / 38,43 | 18,18 / 18,50 | 0,00 |
Aşama 1 → 2 geçişi: aşama 1 grubu 27,85'te solar (cümle 5 biter 27,78; cümle 6 başlar 28,25). olaylar.json 20 olay (kare 16–555).

## Kontroller (kapı/görüntü yok)
- Üretimde taşma sınamaları (assert): kart 1/2 satırı, olumsuz/soru satırı, sağ not satırları sığıyor.
- `node --check` 2 blok OK · yinelenen id yok · `Math.random`/`Date` yok · negatif zaman yok.
- İlk hareket 0,55 sn (kare 16), son hareket 18,95 sn (kare ≈ 568 < 572); son 12 kare durgun.

## Açık
- `?` sarı (söz yok); sözcük t0 olarak `yalın` (38,11) kullanıldı.


## QA 13.11
Kapı: ölçülmedi (HyperFrames). Kareler: k/03-hyperframes-formul-{21.8,27.2,32.5,38.5}.png (açık), -29.8.png (koyu, aşama geçişi). Göz: iki aşama okunur, sarı kutular kontrastlı, el notları sağda taşmıyor. Düzeltme yok. Kalan: yok.

QA 13.11 ek: Koyu kare: k/koyu/03-hyperframes-formul-29.8.png bakıldı (aşama geçişi, kutular), renk hatası yok.

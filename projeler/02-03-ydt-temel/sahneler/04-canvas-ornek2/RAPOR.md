# 04-canvas-ornek2 — RAPOR (13.11, P2; render yok)

Motor: Düz canvas · 1920×1080 · 30 fps · 569 kare · t_bas 33. Tema: açık/koyu hazırlık koştu (son koşu açık).

## Olay ↔ sözcük t0 (yerel kare = round((t − t_bas) × 30); sapma 0)

| Cümle:sözcük | t0 (sn) | Kare | Olay |
|---|---|---|---|
| 4:0 İkinci | 33.55 | 16 | daire içinde 2 |
| 4:1 örnek. | 34.03 | 31 | tek kart |
| 4:2 Our | 34.84 | 55 | kök sözcük sözcük (Our) |
| 4:4 is | 35.56 | 77 | `is going` sarı daire |
| 4:8 hard | 36.28 | 98 | yağmur bulutu |
| 4:10 these | 37.12 | 124 | takvim + `these days.` sarı belirteç |
| 4:12 Şirketimiz | 38.53 | 166 | Türkçe çeviri |
| 4:18 These | 42.21 | 276 | ok → takvim |
| 4:21 dönemi | 43.41 | 312 | takvim altında ayraç |
| 4:24 geçici. | 45.09 | 363 | `geçici` etiketi |
| 4:27 şimdiki | 46.93 | 418 | ok |
| 4:28 zaman | 47.33 | 430 | `-ing` |
| 4:30 Yapı | 48.45 | 464 | formül kartı |
| 4:32 aynı: | 49.09 | 483 | be + V-ing |
| 4:33 is | 49.73 | 502 | is |
| 4:35 going. | 50.93 | 538 | go-ing |

## Kapı ve göz

- Çakışma kapısı ve sahne-kare: ŞEF NOTU (13.11 12:40) gereği KOŞULMADI; QA şeridi koşar. Kare görüntüsü yok (`k/` boş).
- `node --check` JS: geçti. `ONIZLE_YALNIZ=1 bash calistir.sh` (koyu, sonra açık): "önizleme hazır".
- Kapı notu: dekoratif çizgiler `isaret`; yazı kartın içinde; simgeler yazıyla örtüşmeyecek konumda (elle hesap).

## QA 13.11
- Kapı: çakışma yok (76 örnek, 1353 kutu). Kareler `k/04-canvas-ornek2-{34.1,37.5,44,51}.png`, koyu `kk/04-canvas-ornek2-47.png`.
- Göz: taşma yok, bulut/takvim simgeleri anlamlı (hard period, these days), formül kartı ve çeviri sığıyor, koyu tema doğru. Düzeltme yok. Kalan sorun yok.
- QA 13.11 ek (halka/kutu taraması): is going halkası altçizgi oldu. Kapı: çakışma yok (76 örnek, 1353 kutu).

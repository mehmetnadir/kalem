# Sahne 01 — Giriş (HyperFrames, 102 kare = 90 içerik + 12 geçiş; t_bas 0,00)

Tema: acik

Durum: önizleme hazır (`ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu`, sonra açık; son koşu AÇIK). Render, kapı ve kare görüntüsü bu turda YOK (şef EK 13.11 12:40).

## İçerik
- Soğuk açılış kapağı (K23): 0. karede logo damgası + başlık kalemle (SIMPLE / PRESENT), rozetler `YDT · ADVANCED` ve `GRAMMAR`. Kalem sesi 0. kareden (kare 0 çizgi + hışırtı).
- Sağ sütun el çizimi (Tabler, `ortak/cizim/tabler`): saat, takvim, kalem (rutin = geniş zaman); kalemle çizilir, filtre `el`.
- 1,00–2,96 sn Caveat cümlesi 1 konuşmayla yazılır: "Sizi karı koca ilan ediyorum." (ses 3,08 sn'de biter; yazım 2,96'da tamam, sahne 02 başında yerinde).
- 2,20–3,00 sn uçuş: SIMPLE + PRESENT künye sol üste (30 px), logo sol alta (34 px), cümle sahne 02 yerine (x 140, y 300, Caveat 64) kayar (2,45–3,00); çizimler solar; künye metni son 0,25 sn belirir.
- Künye (`ortak/kunye.js` ile aynı): `SIMPLE PRESENT · YDT ADVANCED`, ajanda Hook · Rule · Roots (etkin Hook), sağ üst `Hook`.

## Olay ↔ sözcük t0 (sozcukler.json, cümle 1; t_bas 0,00 → yerel = küresel)
| Olay | Sözcük | Sözcük t0 | Olay sn | Sapma |
|---|---|---|---|---|
| cümle yazımı başlar (kalem hışırtısı) | Sizi | 1,00 | 1,00 | 0,00 |
| `karı` açılır | karı | 1,56 | 1,56 | 0,00 |
| `koca` açılır | koca | 1,80 | 1,80 | 0,00 |
| `ilan` açılır | ilan | 2,12 | 2,12 | 0,00 |
| `ediyorum.` açılır + tık | ediyorum. | 2,48 | 2,48 | 0,00 |
Yazı olmayan olaylar: logo damgası 0,00 · başlık satır 1 0,00, satır 2 1,00 · rozetler 0,30/0,40 · uçuş 2,20–3,00 · olaylar.json 20 olay (kare 0–89).

## Kontroller (kapı/görüntü yok)
- `node --check` 2 inline blok OK · yinelenen id yok · `Math.random`/`Date` yok · ilk hareket kare 0 (soğuk açılış), son olay kare 89, 90–102. kare durgun.
- Renkler yalnız `RENK` paletinden (hf_tema ile açık/koyu çift). Emoji yok. Yazı tabanı: başlık 140, cümle 64, rozet 26 (HUD ölçüsü).

## Açık
- Sahne 02 (Paper.js kanca) cümleyi aynı yerde (x 140, y 300, Caveat 64, `murekkep`) 0. karede başlatmalı.
- Sahne 01'de halka yok (BRIEF'te yok); `ediyorum` vurgusu sahne 02'de.


## QA 13.11
Kapı: ölçülmedi (HyperFrames, kapı bu motoru ölçmez). Kareler: k/01-hyperframes-giris-{0.4,1.3,2.2,2.5}.png (açık), -1.8.png (koyu). Göz: taşma/binme yok, koyu tema doğru, yazı ≥ 64 px, uçuş 2,5 sn'de künye yerine iniyor. Düzeltme yok. Kalan: yok.

QA 13.11 ek 3: simge–etiket/cümle taraması: çizimler cümleyle uyumlu (kod ve kareler üzerinden); uyuşmazlık yok.

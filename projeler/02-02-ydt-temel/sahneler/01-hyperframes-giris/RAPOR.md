# Sahne 01 — Giriş (HyperFrames, 102 kare = 90 içerik + 12 geçiş)

Tema: acik

Durum: önizleme hazır (`ONIZLE_YALNIZ=1 bash calistir.sh` koyu, sonra açık; son koşu AÇIK). Render, kapı ve kare görüntüsü bu turda YOK (şef EK 13.11 12:40).

## İçerik
- Soğuk açılış kapağı: 0. karede logo damgası + başlık kalemle (SIMPLE / PRESENT), rozetler `YDT · BASIC` ve `GRAMMAR`.
- Sağ sütun el çizimi (Tabler): saat (07:00 kalkış), yatak, güneş; sürücü hareketsiz, kalemle çizilir (filtre `el`).
- 1,00–2,58 sn Caveat cümlesi 1 konuşmayla yazılır: "Her sabah yedide kalkıyorum." Sarı halka `kalkıyorum` üstünde.
- 2,20–3,00 sn uçuş: SIMPLE + PRESENT künye sol üste (30 px), logo sol alta (34 px), cümle sahne 02 yerine (x 140, y 300, Caveat 64) kayar; çizimler solar; künye metni son 0,25 sn belirir.
- Künye = `ortak/kunye.js` KUNYE: `SIMPLE PRESENT · YDT BASIC`, ajanda Hook · Examples · Rule · Trap (etkin Hook), sağ üst `Hook`.

## Olay ↔ sözcük t0 (sozcukler.json, cümle 1; sahne t_bas 0,00 → yerel = küresel)
| Olay | Sözcük | Sözcük t0 | Olay sn | Sapma |
|---|---|---|---|---|
| cümle yazımı başlar | Her | 1,00 | 1,00 | 0,00 |
| `sabah` açılır | sabah | 1,32 | 1,32 | 0,00 |
| `yedide` açılır | yedide | 1,72 | 1,72 | 0,00 |
| `kalkıyorum.` açılır | kalkıyorum. | 2,08 | 2,08 | 0,00 |
| sarı halka (kalem darbesi) | kalkıyorum. | 2,08 | 2,20 | +0,12 |
Yazı olmayan olaylar: logo damgası 0,00 · başlık satır 1 0,00, satır 2 1,00 · rozetler 0,30/0,40 · uçuş 2,20–3,00 · olaylar.json 19 olay (kare 0–89).

## Kontroller (kapı/görüntü yok)
- `node --check`: 2 inline blok OK · yinelenen id yok · `Math.random`/`Date` yok · ilk hareket kare 0 (soğuk açılış, K23), içerik 3,00 sn'de biter, 90–102. kare durgun.
- Renkler yalnız RENK paletinden (hf_tema ile açık/koyu çift). Emoji yok. Yazı tabanı: başlık 140, cümle 64, rozet 26 (künye/rozet HUD ölçüsü, örnekle aynı).

## Açık
- Cümle son yeri (140, 300) örnek paketle aynı; sahne 02 kanca (Paper.js) cümleyi aynı yerde 0. karede başlatmalı.
- BRIEF ajanda "Hook · Examples · Form" diyor; `ortak/kunye.js` Rule/Trap — kunye.js esas alındı.

## QA 13.11
- Kapı: "ölçülmedi (HyperFrames)" (kapı bu motoru ölçmüyor).
- Kareler (açık): k/01-hyperframes-giris-0.5, -1.5, -2.2, -2.5, -2.95 · koyu: k/01-hyperframes-giris-1.9.
- Göz: kapak, rozetler, çizimler, halka, künye uçuşu temiz; koyu tema renkleri doğru; taşma yok.
- Düzeltme: yok.
- Kalan: 2,95 sn karesinde SIMPLE/PRESENT hayalet yazısı solarken cümlenin "Her" kelimesinin altından geçiyor (yaklaşık 0,3 sn, soluk). Kabul edilebilir, dokunulmadı.

- Halka kuralı (QA 13.11): DEĞİŞTİ: `kalkıyorum` halkası → vurgu el altçizgisi (uret.py, zamanlar.json halka [2.3,0.3]). Kare k/…-2.7 temiz. Kapı HyperFrames: ölçülmedi.

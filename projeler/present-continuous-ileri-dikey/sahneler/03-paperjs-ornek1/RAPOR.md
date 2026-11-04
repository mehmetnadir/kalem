# Sahne 03 İLERİ Örnek 1 (DİKEY) — RAPOR (05.11)

Motor: Paper.js · 1080×1920 · 30 fps · 442 kare (zaman.json ile birebir) · t_bas 15.25

## Dosyalar

| Dosya | Durum |
|---|---|
| video-acik.mp4, video-koyu.mp4, video.mp4 | ffprobe: 1080,1920 yuv420p 30/1, 442 kare (üçü de) |
| olaylar.json | 25 olay, son olay kare 422, aynı karede en çok 2, son 12 kare olaysız |
| kontrol.png, k/*.png | 0128.png, 0278.png, 0428.png, 0429.png, telefon-01.png, telefon-02.png, telefon-03.png |
| sayfa.html, calistir.sh, sahne-03.js, kalem-paper.js, altyazi-bol.js | kod |

## Zamanlama (yerel kare = round((t − t_bas) × 30); ±3 kare kabul)

| Olay | Küresel sn | Kare |
|---|---|---|
| kart çerçevesi | 15.8 | 17 |
| cümle başı Please | 16.93 | 50 |
| while kutusu | 20.13 | 146 |
| is sleeping daire | 18.75 | 105 |
| am talking daire | 20.4 | 154 |
| duvar | 16.9 | 49 |
| uyuyan figür | 17.3 | 62 |
| konuşan figür | 17.6 | 71 |
| telefon | 19.3 | 122 |
| Türkçe çeviri (Bebek) | 22.3 | 212 |
| iki iş de sürüyor | 25.14 | 297 |
| While vurgusu + toplanma | 27.66 | 372 |
| formül kutusu | 28.3 | 392 |
| is sleep-ing | 28.9 | 409 |
| am talk-ing | 29.2 | 418 |

Paper.js sahnelerinde kareler `zamanlar.json` gerçek ölçümüdür; canvas sahnelerinde motor zaman logu üretmez, tablo kodda verilen başlangıç saniyesinin kareye çevrilmiş hâlidir (sözcük zamanları `sozcukler.json`'dan).

## Bakılan kareler (Read ile açıldı, kendi gözümle)

- k/0128.png, k/0278.png (24,5 sn): kart 4 satır, 3 belirteç, TR 2 satır, sahne 940–1370 (iki figür 420 px, duvar, telefon, z z z), altyazı bandı dolu
- k/0428.png, k/0429.png: sahne 0,42'ye toplandı; formül `is sleep-ing / am talk-ing` Fredoka 110 kartta; altyazı `While, tam anı gösterir.`
- k/telefon-01..03.png (360×640, 6 kare/sayfa): HUD okunuyor, yazı ≥ 64 px (formül 110), platform bandı boş
- Editör kapısı t=20 ve t=36 (dikey-tam): konsol hata 0; slot no:2 ve no:3 hazir/goster true

## Neden yeniden (koşu sırası)

- 1. koşu açık: altyazı bandında 3 tümceli parça 2. satıra yapıştı, satır 15–1065 px (48 px kenar dışı) → `altyazi-bol.js` ile tümce sınırından bölündü.
- 1. koşu: while kutusu 'I' harfine değiyordu → sağ pay 14→6 px.
- Koyu tema aynı kodla koştu (105 sn); telefon kontağı koyu temadan.

## Açık sorular

- Ortak `kunye.js` `altyaziCiz` 3 satıra taşan parçayı (cümle 3 TR: 3 tümce) 2. satıra ekler; satır 48 px güvenli alanın dışına taşar. Dikey sahnelerim parçayı tümce sınırından böler (`altyazi-bol.js`, yerel). Ortak dosya DEĞİŞTİRİLMEDİ; 01/02/05/06 aynı kusuru taşırsa şef karar versin.


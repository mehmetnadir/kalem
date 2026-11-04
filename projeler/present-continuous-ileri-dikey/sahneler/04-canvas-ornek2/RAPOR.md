# Sahne 04 İLERİ Örnek 2 (DİKEY) — RAPOR (05.11)

Motor: Düz canvas · 1080×1920 · 30 fps · 387 kare (zaman.json ile birebir) · t_bas 29.58

## Dosyalar

| Dosya | Durum |
|---|---|
| video-acik.mp4, video-koyu.mp4, video.mp4 | ffprobe: 1080,1920 yuv420p 30/1, 387 kare (üçü de) |
| olaylar.json | 31 olay, son olay kare 361, aynı karede en çok 1, son 12 kare olaysız |
| kontrol.png, k/*.png | 0118.png, 0268.png, 0358.png, 0374.png, telefon-01.png, telefon-02.png, telefon-03.png |
| sayfa.html, calistir.sh, sahne.js, sahne-ortak.js, altyazi-bol.js | kod |

## Zamanlama (yerel kare = round((t − t_bas) × 30); ±3 kare kabul)

| Olay | Küresel sn | Kare |
|---|---|---|
| kart çerçevesi | 30.13 | 17 |
| Because | 31.34 | 53 |
| is leaking daire | 32.14 | 77 |
| are staying daire | 33.02 | 103 |
| this week ayracı | 34.38 | 144 |
| büyük ev | 31.4 | 55 |
| 3 damla | 31.95 | 71 |
| ok | 33.3 | 112 |
| uncle's | 33.82 | 127 |
| figür | 34.0 | 133 |
| Türkçe çeviri | 35.75 | 185 |
| toplanma | 38.5 | 268 |
| geçici → this week | 38.87 | 279 |
| takvim şeridi | 39.1 | 286 |
| this week daire | 40.47 | 327 |
| is leak-ing | 41.0 | 343 |
| are stay-ing | 41.4 | 355 |

Paper.js sahnelerinde kareler `zamanlar.json` gerçek ölçümüdür; canvas sahnelerinde motor zaman logu üretmez, tablo kodda verilen başlangıç saniyesinin kareye çevrilmiş hâlidir (sözcük zamanları `sozcukler.json`'dan).

## Bakılan kareler (Read ile açıldı, kendi gözümle)

- k/0268.png (açık, 38,5 sn): kart + TR + ev–ok–ev–figür tam boy; altyazı 2 satır
- k/0374.png (koyu, 41,5 sn): toplanmış sahne, geçici → this week, 7 kutu takvim, formül 108 px, `This week bunu söyler.` altyazısı; içerik bandı 372–1380 dolu
- k/telefon-02.png (koyu, 6–11 sn): HUD + kart + sahne + altyazı telefon ölçeğinde okunuyor; 6–9 sn arası alt kısım (1240–1392) geçici boş
- Editör kapısı t=36: konsol hata 0 (düzeltmeden sonra), slot no:3 hazir/goster true

## Neden yeniden (koşu sırası)

- 1. koşu: kart 4 kısa satır, sağı boş; formül takvime değiyordu; takvim günleri 28 px; uncle's etiketi toplanınca 24 px'e küçüldü
-  → kart 5/6/3 sözcük 3 satır, formül y 1268/1370, gün yazıları kaldırıldı, etiket küçülmeden taşınır, sahne 830'dan başlar 0,42.
- 2. koşu: etiket küçük evin yanında figürün saçına değdi → toplanırken 48 px sola kayar.
- Editörde t=36 konsolda 2× `405 Method Not Allowed` (canvas `cizim` canlı kipte POST /log atıyordu) → 4 motor kopyasında `gunluk()` yardımcısı: `?canli=1` ise POST yok; kapı yeniden: hata 0.
- Koyu tema son kodla koştu (346 sn, yük bekleme dahil).

## Açık sorular

- Ortak `kunye.js` `altyaziCiz` 3 satıra taşan parçayı (cümle 3 TR: 3 tümce) 2. satıra ekler; satır 48 px güvenli alanın dışına taşar. Dikey sahnelerim parçayı tümce sınırından böler (`altyazi-bol.js`, yerel). Ortak dosya DEĞİŞTİRİLMEDİ; 01/02/05/06 aynı kusuru taşırsa şef karar versin.


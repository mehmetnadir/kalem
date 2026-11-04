# Sahne 04 İLERİ Örnek 2 (yatay) — RAPOR (05.11)

Motor: Düz canvas · 1920×1080 · 30 fps · 387 kare (zaman.json ile birebir) · t_bas 29.58

## Dosyalar

| Dosya | Durum |
|---|---|
| video-acik.mp4, video-koyu.mp4, video.mp4 | ffprobe: 1920,1080 yuv420p 30/1, 387 kare (üçü de) |
| olaylar.json | 34 olay, son olay kare 365, aynı karede en çok 1, son 12 kare olaysız |
| kontrol.png, k/*.png | 0118.png, 0268.png, 0358.png, 0374.png |
| sayfa.html, calistir.sh, sahne.js, sahne-ortak.js | kod |

## Zamanlama (yerel kare = round((t − t_bas) × 30); ±3 kare kabul)

| Olay | Küresel sn | Kare |
|---|---|---|
| daire 2 | 30.13 | 17 |
| Because | 31.34 | 53 |
| is leaking daire | 32.14 | 77 |
| are staying daire | 33.02 | 103 |
| this week ayracı | 34.38 | 144 |
| büyük ev | 31.4 | 55 |
| 3 damla | 31.95 | 71 |
| ok → küçük ev | 33.3 | 112 |
| uncle's | 33.82 | 127 |
| figür | 34.0 | 133 |
| Türkçe çeviri | 35.75 | 185 |
| takvim şeridi | 38.87 | 279 |
| geçici | 39.3 | 292 |
| this week yazısı | 39.5 | 298 |
| eve dönüş | 40.0 | 313 |
| this week daire | 40.47 | 327 |
| formül kutusu | 40.75 | 335 |
| is leak-ing | 41.35 | 353 |
| are stay-ing | 41.6 | 361 |

Paper.js sahnelerinde kareler `zamanlar.json` gerçek ölçümüdür; canvas sahnelerinde motor zaman logu üretmez, tablo kodda verilen başlangıç saniyesinin kareye çevrilmiş hâlidir (sözcük zamanları `sozcukler.json`'dan).

## Bakılan kareler (Read ile açıldı, kendi gözümle)

- k/0118.png (33,5 sn): kök yazılıyor, 2 sarı daire, ev + 3 damla + ok, küçük ev çiziliyor
- k/0268.png (38,5 sn): kök + çeviri; sağda ev–ok–ev–figür; alt yarı boş (takvim 38,87'de)
- k/0358.png, k/0374.png (41,5 sn): takvim şeridi + this week ayracı + geçici → eve dönüş + formül kartı; figür kutuya değmiyor
- Editör kapısı t=36: konsol hata 0, `slot {no:3,hazir:true,goster:true}`

## Neden yeniden (koşu sırası)

- 1. koşu: otomatik satır sonu 'are/staying' ve 'this/week' ayırdı + geniş sözcük aralığı → `satirSay` ile sabit 5/6/3 satır, boşluk 4.
- 1. koşu: figür küçük evin kapısına biniyordu, 3 damla birbirine ve kapıya geçiyordu → ev/figür/damla konumları değişti.
- 2. koşu: figür formül kutusunun üst çizgisine değiyordu → figür kutusu y 445→435, boy 230→210.
- Koyu tema 3. kodla koştu.

## Açık sorular

- Ortak `kunye.js` `altyaziCiz` 3 satıra taşan parçayı (cümle 3 TR: 3 tümce) 2. satıra ekler; satır 48 px güvenli alanın dışına taşar. Dikey sahnelerim parçayı tümce sınırından böler (`altyazi-bol.js`, yerel). Ortak dosya DEĞİŞTİRİLMEDİ; 01/02/05/06 aynı kusuru taşırsa şef karar versin.


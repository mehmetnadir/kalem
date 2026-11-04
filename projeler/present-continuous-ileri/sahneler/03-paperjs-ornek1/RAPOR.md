# Sahne 03 İLERİ Örnek 1 (yatay) — RAPOR (05.11)

Motor: Paper.js · 1920×1080 · 30 fps · 442 kare (zaman.json ile birebir) · t_bas 15.25

## Dosyalar

| Dosya | Durum |
|---|---|
| video-acik.mp4, video-koyu.mp4, video.mp4 | ffprobe: 1920,1080 yuv420p 30/1, 442 kare (üçü de) |
| olaylar.json | 37 olay, son olay kare 422, aynı karede en çok 2, son 12 kare olaysız |
| kontrol.png, k/*.png | 0128.png, 0278.png, 0413.png, 0429.png |
| sayfa.html, calistir.sh, sahne-03.js, kalem-paper.js | kod |

## Zamanlama (yerel kare = round((t − t_bas) × 30); ±3 kare kabul)

| Olay | Küresel sn | Kare |
|---|---|---|
| daire 1 | 15.8 | 17 |
| cümle başı Please | 16.93 | 50 |
| while kutusu | 20.13 | 146 |
| is sleeping daire | 18.75 | 105 |
| am talking daire | 20.4 | 154 |
| duvar çizgisi | 16.9 | 49 |
| Türkçe çeviri (Bebek) | 22.3 | 212 |
| zaman çizgisi | 25.14 | 297 |
| now noktası | 25.9 | 319 |
| While → NOW | 27.66 | 372 |
| formül kutusu | 28.05 | 384 |
| be + V-ing | 28.42 | 395 |
| is sleep-ing | 28.95 | 411 |
| am talk-ing | 29.18 | 418 |

Paper.js sahnelerinde kareler `zamanlar.json` gerçek ölçümüdür; canvas sahnelerinde motor zaman logu üretmez, tablo kodda verilen başlangıç saniyesinin kareye çevrilmiş hâlidir (sözcük zamanları `sozcukler.json`'dan).

## Bakılan kareler (Read ile açıldı, kendi gözümle)

- k/0128.png (19,5 sn): kök yazılıyor, is sleeping dairesi, iki figür + duvar + z z z, telefon yok henüz (ilk koşu karesi)
- k/0278.png (24,5 sn): kök + 3 sarı belirteç + Türkçe çeviri; alt yarı boş (zaman çizgisi 25,14'te başlıyor)
- k/0413.png (29,0 sn, açık+koyu): NOW oku, zaman çizgisi + iki dalgalı bant, formül kartı yazılıyor
- k/0429.png (son−13): her şey yerinde, çakışma 0, künye tam; kontrol.png 6 kare
- Editör kapısı t=20 ve t=36: konsol hata 0; durum `slot[0] {no:2,hazir:true,goster:true}` ve `{no:3,hazir:true,goster:true}`

## Neden yeniden (koşu sırası)

- 1. koşu açık: daire/kutu 'I' ve 'in' sözcüğüne değiyordu → daire payı 12→4 px, kutu sağ pay 24→13 px.
- 2. koşu koyu: başsız Chrome 60 sn sessiz kaldı (makine yükü 50–157, ZAMAN AŞIMI 347. karede) → aynı kodla yeniden koşuldu, 158 sn.
- Açık tema 2. koşusu pay düzeltmesiyle aynı zincirde koştu (86 sn).

## Açık sorular

- Ortak `kunye.js` `altyaziCiz` 3 satıra taşan parçayı (cümle 3 TR: 3 tümce) 2. satıra ekler; satır 48 px güvenli alanın dışına taşar. Dikey sahnelerim parçayı tümce sınırından böler (`altyazi-bol.js`, yerel). Ortak dosya DEĞİŞTİRİLMEDİ; 01/02/05/06 aynı kusuru taşırsa şef karar versin.


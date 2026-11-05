# Sahne 04 — Kök 2 (DİKEY, present-perfect-ileri-dikey) — RAPOR (05.11)

Motor: düz canvas · 1080×1920 · 30 fps · 533 kare (zaman.json ile birebir) · t_bas 33,89 · içerik kare 521 · çip `Exam Q 2 / 3`.

## Dosyalar

| Dosya | Durum |
|---|---|
| video-acik.mp4, video-koyu.mp4, video.mp4 (son koşu = açık) | ffprobe: 1080×1920 yuv420p 30/1, 533 kare (acik, koyu) |
| olaylar.json | 30 olay, son olay kare 510, son 12 kare olaysız |
| kontrol.png, k/*.png | 0123.png, 0273.png, 0423.png, 0520.png, telefon-01..03.png (açık temadan) |
| sayfa.html, calistir.sh, sahne.js, sahne-ortak.js | kod; altyazı ortak `altyaziMetin` + yamalı `altyaziCiz` |

## Yerleşim (bantlar)

kart 372–708 (Fredoka 64, 4 satır 4/4/4/2, sağ üstte daire 2) · TR Caveat 64 3 satır 740–920 · ORTA: figür (sitting-5, 425 px) + dizüstü (coco/laptop, 360 px) 935–1360; 40,4'te 0,6'ya sola toplanır · takvim şeridi 1170–1392 (`30 years` / `1995` / `now` Caveat 96) · 46,4'te sahne + takvim birlikte 0,48'e toplanır · formül kartı 1170–1392 (`for + süre` / `since + başlangıç` Fredoka 96) · altyazı 1400–1536 · platform boş.

## Zamanlama (kod tablosu; kare = round((t − 33,89) × 30))

| Olay | Küresel sn | Kare |
|---|---|---|
| kart / daire 2 | 34,44 / 34,7 | 17 / 24 |
| cümle başı Selim | 35,57 | 50 |
| `for thirty` / `years,` halka | 37,13 / 37,55 | 97 / 110 |
| figür / dizüstü çizimi | 36,0 / 37,8 | 63 / 117 |
| TR 3 satır | 40,70 / 42,34 / 43,82 | 204 / 253 / 298 |
| takvim (çizgi 41,3; ayraç 42,4; `30 years` 43,0; `now` 44,2) | 41,3–44,2 | 222–309 |
| `has worked` halka | 46,3 | 372 |
| kart kutusu / `for + süre` | 46,75 / 47,17 | 386 / 398 |
| `since + başlangıç` | 50,29 | 492 |

## Bakılan kareler (Read ile, kendi gözümle)

- k/0273.png, k/0520.png (açık, 2. koşu): kart + TR + takvim/kart; `for thirty` ve `years,` halkaları ayrı satırlarda; altyazı bandı dolu.
- k/0123.png (açık, son koşu): figür 425 px + dizüstü ORTA'da çiziliyor, altyazı bandı tam cümle.
- telefon-01.png / telefon-02.png (360×640): HUD okunuyor, yazı ≥ 64, platform bandı boş; telefon-02'de takvim şeridi ve kart okunuyor.
- Editör kapısı t=42 (`dikey-tam`, açık): konsol boş (hata 0); `slot[0] {no:3,hazir:true,goster:true,op:1}`.

## Neden yeniden (koşu sırası)

- 1. koşu: 0,42'ye toplanan sahne ≈ 180 px, 40,4–51 sn boyunca küçük; takvim sağda küçük (yazı 52 px < 64); `for thirty years` halkası 3 satıra bölününce `thirty` halkasız kaldı → takvim alt banda 96 px yazıyla alındı, sahne 0,6, ikinci toplanma 0,48; halka `for thirty` + `years,` olarak ikiye bölündü, dikey yarıçap 48→39.
- 2. koşu: laptop `tabler/device-laptop.svg` boş kutu çiziyordu → `coco/laptop.svg`; açık tema yeniden koşuldu (03:59).

## Açık sorular / uyarı

- Figür ≥ 420 yalnız 36,0–40,4 sn'de (ve çizim sırasında); sonra 0,6 → 0,48 ölçekle ≈ 110 px. Brief "figürü yarıya küçültme yerine formülü yanına/altına koy" diyor, ama kart 222 px yer istedi; şef karar versin (örn. kart tek satır `for + süre` sonra değişir).
- Takvim ve `now` / `1995` yazıları 0,48'de ≈ 46 px (< 64 ama ≥ 48 kuralı içinde).

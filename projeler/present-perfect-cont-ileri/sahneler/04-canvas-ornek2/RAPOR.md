# Sahne 04 — Örnek 2 (düz canvas, yatay, ileri)

Tema: acik + koyu (ikisi de koşuldu; `video-acik.mp4`, `video-koyu.mp4`, `video.mp4` = son koşu koyu).

| Kalem | Değer |
|---|---|
| Kare sayısı | 478 (zaman.json ile birebir; ffprobe acik ve koyu: 478 kare, yuv420p, 30 fps, 1920x1080) |
| Olay sayısı | 29 (`olaylar.json`, en büyük kare 457, son 12 kare durgun) |
| Editör kapısı | t=24 ve t=40: konsol boş (hata 0); eval slot {no:2|3, hazir:true, goster:true} |
| Denetim kareleri | k/0100, 0220, 0370, 0465 |

Neden yeniden: 1. koşuda ikinci daire satır 3'ün alt çizgi 'all week' ile çakışıyordu → satır aralığı 76→84, daire ry 42→37. Açık soru yok.

# Sahne 04 — Örnek 2 (düz canvas, dikey 1080x1920, ileri)

Tema: acik + koyu (ikisi de koşuldu; `video-acik.mp4`, `video-koyu.mp4`, `video.mp4` = son koşu koyu).

| Kalem | Değer |
|---|---|
| Kare sayısı | 478 (zaman.json ile birebir; ffprobe acik ve koyu: 478 kare, yuv420p, 30 fps, 1080x1920) |
| Olay sayısı | 28 (`olaylar.json`, en büyük kare 457, son 12 kare durgun) |
| Editör kapısı | dikey-tam t=24 ve t=40: konsol boş (hata 0); eval slot {no:2|3, hazir:true, goster:true} |
| Denetim kareleri | k/0100, 0220, 0370, 0465 + k/telefon-01..03 (bakıldı) |

Neden yeniden: ilk düzende sahne 0,45'e toplanıyordu (figür ≈190 px) → iki sütun düzeni, figür 430 px; ilk koşuda 'have only finished two chapters' dairesi yanlış sözcüklere düşüyordu (kel 10..14 iki satıra bölünmüştü) → cevre(10,11) + cevre(12,14). Roman çizimi ≈180×230 px (nesne; figür değil).

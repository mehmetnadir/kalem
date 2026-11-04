# Sahne 01 — Giriş (HyperFrames, yatay 1920x1080, 102 kare)

Tema: açık + koyu (ikisi de koşuldu; `video-acik.mp4`, `video-koyu.mp4`; `video.mp4` = son koşu = koyu).

## Yapılan
- Present Continuous sahne 01 kodu kopyalandı (`uret.py`, `olay.py`, `yardim.py`, `calistir.sh`); başlık `SIMPLE` / `PAST`, künye ders adı `SIMPLE PAST`, kamera eskizi yerine `device-tv` (2 yol), figür `standing-3`.
- `zamanlar.json`: BRIEF §4 (başlık 0,0–1,1 / 1,0–2,2; figür 0,2–2,0; TV 1,6–2,2; uçuş 2,2–3,0). Cümle 1 sözcükleri `sozcukler.json`'dan.
- `ortak/kunye.js` kontrol edildi: ders `SIMPLE PAST`, seviye `YDT BASIC`, KOK `simple-past-temel`; düzeltme gerekmedi.

## Sayılar
ffprobe: h264 yuv420p 1920x1080 30 fps, 102 kare (iki tema). Olay 51 (son kare 89, geçiş altı olaysız).

## Kare denetimi
`k/36.png`, `k/60.png`, `k/87.png`, `kontrol.png` (6 kare) Read ile açıldı: başlık kalemle çizilir, cümle sözcük sözcük, TV + figür sağ sütunda, son karede künye tam (SIMPLE PAST · YDT BASIC, Hook, logo sol alt, ajanda sağ alt). Çakışma yok.

## Açık
- BRIEF TV'yi "device-tv" ister; küçük döndürme (-5°) PC kamerasından devralındı.

# RAPOR — simple-present-temel-s1 (05.11)

| Çıktı | Değer |
|---|---|
| cikti.mp4, cikti-koyu.mp4 | 1080x1920, 30 fps, 713 kare (23,77 sn) = 102 + 403 + 232 - 24 geçiş payı |
| Sahne kareleri (açık + koyu) | 01: 102 · 02: 403 · 03: 232 (zaman.json ile birebir) |
| kapak.png | sahne 01 kare 59 (t 1,97) |

## Yeniden yakalama (neden)
- Sahne 01 açık, 1. koşu: "GİDER" satırı ortada değil, +48 px sağda (fontTools genişliği render genişliğinin
  %89'u). `GEN1 = 1.12` ile düzeltildi; sahne 01 açık + koyu yeniden koştu.
- Sahne 02 ve 03: tek koşu (açık, koyu).

## Sapmalar
- Otobüs ve okul `tabler/bus.svg` + `tabler/school.svg`: HyperFrames kapak eskizi yalnız Tabler (24x24, mutlak
  yol) çizer; coco SVG'leri (mm, göreli komut) kapakla sahne 02 arasında aynı çizimi vermez. Kapakta figür +
  otobüs hazır; okul sahne 02'de 7,2 sn'de çizilir.
- Altyazı "gelir." yetim satırı: `kunye.js` ve HyperFrames `yardim.py` aynı sarma kuralını kullanır; yerel çözüm
  yazılmadı.

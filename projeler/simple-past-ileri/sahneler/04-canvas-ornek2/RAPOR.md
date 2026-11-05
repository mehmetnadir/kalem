# Sahne 04 Örnek 2 — Yatay (05.11)

Motor: Düz canvas · 1920×1080 · 30 fps · 487 kare (zaman.json ile birebir) · t_bas 33.15

| Kapı | Sonuç |
|---|---|
| video-acik.mp4, video-koyu.mp4 | ffprobe: 487 kare, ikisi de |
| olaylar.json | 37 olay, son olay kare 443 (son 12 kare olaysız) |
| Editör (3012, başsız) t=20 ve t=40 | slot no 2 / no 3 `hazir:true, goster:true`; konsolda yalnız başka ajanların eksik sahnelerinden 404 |
| Bakılan kareler (Read ile açıldı) | kontrol.png, 0131.png, 0251.png, 0428.png, 0474.png |

## Neden yeniden (koşu öncesi canlı önizleme turları)
- Yürüyen figür okula girip çizimi örtüyordu: yürüyüş 270→190 px, başlangıç sola alındı.

## Açık sorular
- Kod satırları şablon gibi 100 karakteri aşan yerler içerir (şablonun biçimi korundu).

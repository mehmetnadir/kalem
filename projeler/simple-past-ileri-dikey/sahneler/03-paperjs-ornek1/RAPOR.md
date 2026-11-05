# Sahne 03 Örnek 1 — Dikey (05.11)

Motor: Paper.js · 1080×1920 · 30 fps · 602 kare (zaman.json ile birebir) · t_bas 13.47

| Kapı | Sonuç |
|---|---|
| video-acik.mp4, video-koyu.mp4 | ffprobe: 602 kare, ikisi de |
| olaylar.json | 42 olay, son olay kare 553 (son 12 kare olaysız) |
| Editör (3012, başsız) t=20 ve t=40 | slot no 2 / no 3 `hazir:true, goster:true`; konsolda yalnız başka ajanların eksik sahnelerinden 404 |
| Bakılan kareler (Read ile açıldı) | kontrol.png, 0202.png, 0391.png, 0547.png, 0589.png, telefon-01.png, telefon-02.png, telefon-03.png, telefon-04.png |

## Neden yeniden (koşu öncesi canlı önizleme turları)
- Figür 430 px kaldı: alt bölgeye iner (küçülmez); kitap+kalem figürün kucağına küçülür (k 0,4→0,5, çizgi kalınlığı 6,6).
- Tuzak satırı sağ kenardan taşıyordu: X 410→442, nokta boşluğu 10→6.
- Zaman çizgisi M bölgesinde (690–950), figür bant altında.

## Açık sorular
- Kod satırları şablon gibi 100 karakteri aşan yerler içerir (şablonun biçimi korundu).

# Sahne 04 Örnek 2 — Dikey (05.11)

Motor: Düz canvas · 1080×1920 · 30 fps · 487 kare (zaman.json ile birebir) · t_bas 33.15

| Kapı | Sonuç |
|---|---|
| video-acik.mp4, video-koyu.mp4 | ffprobe: 487 kare, ikisi de |
| olaylar.json | 36 olay, son olay kare 443 (son 12 kare olaysız) |
| Editör (3012, başsız) t=20 ve t=40 | slot no 2 / no 3 `hazir:true, goster:true`; konsolda yalnız başka ajanların eksik sahnelerinden 404 |
| Bakılan kareler (Read ile açıldı) | kontrol.png, 0131.png, 0251.png, 0428.png, 0474.png, telefon-01.png, telefon-02.png, telefon-03.png |

## Neden yeniden (koşu öncesi canlı önizleme turları)
- Sahne inişi 150→110 px, yol çizgileri 1392 altına alındı.
- used to grubu 38,5'te sabit yer açmak için M bölgesinden yukarı kayar (kırpılır); `artık yok` descender'ı kenarda iz bırakıyordu: kayma 260→330 px.
- Sapma: used to grubu `would` grubuna yer açarken görünmez olur (figür 430 px korunduğu için başka yer yok).

## Açık sorular
- Kod satırları şablon gibi 100 karakteri aşan yerler içerir (şablonun biçimi korundu).

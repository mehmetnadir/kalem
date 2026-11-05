# simple-present-ileri-s1 — S1 Shorts üretim raporu (05.11)

| Çıktı | Kare | Süre |
|---|---|---|
| cikti.mp4 (acik) | 607 | 20,23 sn |
| cikti-koyu.mp4 (koyu) | 607 | 20,23 sn |
| sahne 01 / 02 / 03 | 102 / 297 / 232 | zaman.json ile birebir (iki tema) |

102 + 297 + 232 − 2 × 12 (geçiş payı) = 607 (birlestir.py aynı sayıyı yazdı).

- Sahneler: `sahneler/01-hyperframes-kapak` (TARİFE / = SIMPLE, İ = I + elle nokta, Tarife varsa / will + kırmızı çarpı / deme.,
  figür + otobüs) · `02-paperjs-ornek` (EN kart, takes off altı çizgi, uçak + saat 9:00 + takvim, TR çeviri,
  tomorrow ≠ will, Simple Present) · `03-hyperframes-cta` (Tam ders: · Simple Present bandı · saat + 6 dakika · hap).
- kalem-paper.js: yerel `altyaziSec` kaldırıldı; `ortak/kunye.js` `altyaziMetin/altyaziCiz` (yamalı) kullanılır.
- Editör kapısı (`onizle.html?surum=shorts&tema=acik`): konsol hatası 0. `EDITOR.durum()`:
  t 1,9 → slot 0 `hazir:true, goster:true` · t 8 → slot 1 `hazir:true, goster:true` · t 16 → slot 2 `hazir:true, goster:true`.
  Ekran: `k/editor-t1.9.png`, `k/editor-t8.png`, `k/editor-t16.png`.
- Telefon kontak: `k/telefon-01..04.png` (acik), `k/telefon-koyu-01..04.png` (koyu).
- Baktığım kareler: 01 `k/59.png` (kapak, çip yok), `k/93.png` · 02 `k/0048.png`, `0102.png`, `0189.png`, `0284.png` ·
  03 `k/90.png`, `k/147.png`.
- Açık soru: editör saati toplam kareyi 578 gösterir (zaman.json `icerik_kare` toplamı 90+285+202+1); paket 607.

## Neden yeniden
| Koşu | Sebep |
|---|---|
| 01 (1. deneme) | Makine yükü: HyperFrames alarmı 480 sn'de kesti; alarm 1200'e çıkarıldı, yeniden koşuldu |
| 01 (2.) | İ noktasının tepesi HUD sınırına (320) değiyordu: başlık 14 px aşağı (T1_Y 514, T2_Y 724) |
| 02 (2.) | `coco/plane.svg` çift çizgili ve sol kenara 20 px kala yapışıktı → `tabler/plane.svg`; `tabler/clock` elleri 4:30 gösterdi, etiket 9:00 → kadran + eller elle çizildi (9:00) |

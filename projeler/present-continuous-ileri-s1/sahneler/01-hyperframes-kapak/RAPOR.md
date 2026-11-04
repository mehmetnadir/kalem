# Sahne 01 Kapak (HyperFrames, 102 kare)

Tema: acik + koyu (ikisi de `video-acik.mp4` / `video-koyu.mp4`)

- Kare: 102 (ffprobe nb_read_frames, iki tema). Olay: 58.
- Kapı: kapak karesi t 1,97 (kare 59): çip yok, başlık 2 satır, figür 440 px + kitap, altyazı bandında `I am knowing`.
- Baktığım kareler: `k/36.png` (1,2 sn) · `k/59.png` · `k/74.png` (2,45 sn uçuş) · `k/93.png` (3,1 sn son hal) · `kontrol.png`.
- Sapma: `I AM KNOWING` 190 px'te 1290 px olur (984'e sığmaz) → 138 px (938 px). `= YANLIŞ` 230 px.
- Sapma: uçuş 2,0–2,65 (brief 2,0–3,0); çarpı 2,74–2,94; `diyemezsin.` 2,86–2,96. Sebep: sahne 02 kare 0 son hali taşımalı.

## Neden yeniden
| Koşu | Sebep |
|---|---|
| 2 | `diyemezsin.` ve çarpı sahne sonuna alındı (2,86 sn sahne 01 içinde); alt bantta 300 px boşluk vardı |
| 3 | `diyemezsin.` yazımı 0,14 → 0,10 sn (kare 89'da yarımdı); figür 3,5 → 4,4, kitap 4,0 (BRIEF-DIKEY §3 kalınlık) |
| 4 | altyazı cümle cümle bölündü (`altyazi_cumleleri`, Paper sahnelerindeki `altyaziSec` ile aynı kural) |
| 5 | `tema.sh` `video-<tema>.mp4` yazmıyordu; acik yeniden koşuldu (cikti.mp4 koyu videodan çıkmıştı) |

# S1 Shorts — "TARİFE = SIMPLE" (simple-present-ileri-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 19.2 sn, anlatım 19.25 sn hazır) + `kapak.png` + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../simple-present-ileri/BRIEF.md` ile aynı.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1.00 · 3.55 · 13.06; toplam 19.25), kalıp `dikey-senaryo-kalibi.md` §4–5.
HUD sayıları dikey v2 (`../present-continuous-dikey/BRIEF-DIKEY.md` §2–3) ile aynı; `ortak/kunye.js` iki rozetli (`YDT · ADVANCED` + `GRAMMAR`).

## Dikey yerleşim (px)
Yerleşim ve ölçek: ../present-continuous-s1/BRIEF-S1.md '05.11 düzeltme' bölümü +
../present-continuous-dikey/BRIEF-DIKEY.md §2–§3
(tek kaynak, 05.11 karar 6b); 04.11 tablosu geçersiz.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0,00–3,00 | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3,00–12,51 | 297 |
| 03 | 03-hyperframes-cta | HyperFrames | 12,51–19,25 | 232 |

Kapak: başlık `TARİFE` / `= SIMPLE` 0,65–1,45; Türkçe cümle 1 (`Tarife varsa will deme.`) 1,00'dan sözcük zamanlı; uçuş 2,0–3,0.
Örnek: `takes off` altı çizgi (4,15), uçak `coco/plane.svg` + saat `coco/clock.svg` `9:00` + takvim `tabler/calendar.svg` (3,55'dan), `tomorrow ≠ will` kırmızı çizgi, `tarife kesin` (8,75).
CTA: `Tam ders:` 13,06 · `Simple Present` bant 14,10 · saat + `Tam ders kanalda · 6 dk` 16,49 · 1 sn durgun kuyruk.

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/simple-present-ileri-s1 --tema acik --gecis BookFlip --efekt hisirti`.

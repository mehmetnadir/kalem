# S1 Shorts — "GİDER = GOES" (simple-present-temel-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 22.8 sn, anlatım 22.77 sn hazır) + `kapak.png` + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../simple-present-temel/BRIEF.md` ile aynı.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1.00 · 6.35 · 16.58; toplam 22.77), kalıp `dikey-senaryo-kalibi.md` §4–5.
HUD sayıları dikey v2 (`../present-continuous-dikey/BRIEF-DIKEY.md` §2–3) ile aynı; `ortak/kunye.js` iki rozetli (`YDT · BASIC` + `GRAMMAR`).

## Dikey yerleşim (px)
Yerleşim ve ölçek: ../present-continuous-s1/BRIEF-S1.md '05.11 düzeltme' bölümü +
../present-continuous-dikey/BRIEF-DIKEY.md §2–§3
(tek kaynak, 05.11 karar 6b); 04.11 tablosu geçersiz.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0,00–3,00 | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3,00–16,03 | 403 |
| 03 | 03-hyperframes-cta | HyperFrames | 16,03–22,77 | 232 |

Kapak: başlık `GİDER` / `= GOES` 0,65–1,45; Türkçe cümle 1 (`Gider, İngilizcede goes olur: fiilin sonuna s gelir.`) 1,00'dan sözcük zamanlı; uçuş 2,0–3,0.
Örnek: `goes` altı çizgi (6,99), figür `open-peeps/standing-2.svg` + otobüs `coco/bus.svg` + okul `coco/school.svg` (6,35'den), `go + es` formülü (10,39 civarı), `he · she · it` etiketi (12,11).
CTA: `Tam ders:` 16,58 · `Simple Present` bant 17,62 · saat + `Tam ders kanalda · 6 dk` 20,01 · 1 sn durgun kuyruk.

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/simple-present-temel-s1 --tema acik --gecis BookFlip --efekt hisirti`.

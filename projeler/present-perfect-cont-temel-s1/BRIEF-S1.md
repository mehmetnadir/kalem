# S1 Shorts — İKİ SAATTİR = HAVE BEEN (present-perfect-cont-temel-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 24,97 sn, anlatım 23,97 sn hazır; konuşma 22,97'de biter) + `kapak.png` (t = 1,97 sn karesi) + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../present-continuous/BRIEF.md` ile aynı.
HUD sayıları dikey v2 (`ortak/kunye.js`, BRIEF-DIKEY.md §2–3). Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 7,86 · 17,30;
toplam 23,97 = konuşma sonu + 1,0), kalıp `dikey-senaryo-kalibi.md` §4–5. Kapak başlığı: `İKİ SAATTİR` / `= HAVE BEEN`. Rozetler `YDT · BASIC` + `GRAMMAR`.

## Dikey yerleşim (px)
Yerleşim ve ölçek: ../present-continuous-s1/BRIEF-S1.md '05.11 düzeltme' bölümü +
../present-continuous-dikey/BRIEF-DIKEY.md §2–§3
(tek kaynak, 05.11 karar 6b); 04.11 tablosu geçersiz.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0,00–3,00 (+12 geçiş) | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3,00–16,75 (+12) | 424 |
| 03 | 03-hyperframes-cta | HyperFrames | 16,75–23,97 (+1 sn kuyruk) | 247 |

Kapak: başlık 0,65–1,45; cümle 1 1,00'den sözcük zamanlı; uçuş 2,0–3,0 (başlık → çip, cümleler yukarı, eskiz solar).
Örnek: figür + dizüstü + saat 1,3'ten; `have been` + `-ing` kartı 3,55'ten; örnek kartı 7,86'ten; `since this morning` yayı 9,78; `has been + -ing` 13,91.
CTA: `Tam ders:` 17,30 · `Present Perfect Continuous` bant 18,34 · saat + `Tam ders kanalda · 6 dk` 20,42 · 1 sn durgun kuyruk.

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/present-perfect-cont-temel-s1 --tema acik --gecis BookFlip --efekt hisirti`.

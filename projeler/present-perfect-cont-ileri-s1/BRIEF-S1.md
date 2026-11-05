# S1 Shorts — SÜREÇ Mİ? SONUÇ MU? (present-perfect-cont-ileri-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 24,93 sn, anlatım 23,91 sn hazır; konuşma 22,91'de biter) + `kapak.png` (t = 1,97 sn karesi) + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../present-continuous/BRIEF.md` ile aynı.
HUD sayıları dikey v2 (`ortak/kunye.js`, BRIEF-DIKEY.md §2–3). Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 7,80 · 17,24;
toplam 23,91 = konuşma sonu + 1,0), kalıp `dikey-senaryo-kalibi.md` §4–5. Kapak başlığı: `SÜREÇ Mİ?` / `SONUÇ MU?`. Rozetler `YDT · ADVANCED` + `GRAMMAR`.

## Dikey yerleşim (px)
Yerleşim ve ölçek: ../present-continuous-s1/BRIEF-S1.md '05.11 düzeltme' bölümü +
../present-continuous-dikey/BRIEF-DIKEY.md §2–§3
(tek kaynak, 05.11 karar 6b); 04.11 tablosu geçersiz.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0,00–3,00 (+12 geçiş) | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3,00–16,69 (+12) | 423 |
| 03 | 03-hyperframes-cta | HyperFrames | 16,69–23,91 (+1 sn kuyruk) | 247 |

Kapak: başlık 0,65–1,45; cümle 1 1,00'den sözcük zamanlı; uçuş 2,0–3,0 (başlık → çip, cümleler yukarı, eskiz solar).
Örnek: `been reading` sarı daire 8,20; `have finished` ikinci daire 11,00; `PROCESS / RESULT` iki sütun kartı 12,69.
CTA: `Tam ders:` 17,24 · `Present Perfect Continuous` bant 18,28 · saat + `Tam ders kanalda · 6 dk` 20,36 · 1 sn durgun kuyruk.

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/present-perfect-cont-ileri-s1 --tema acik --gecis BookFlip --efekt hisirti`.

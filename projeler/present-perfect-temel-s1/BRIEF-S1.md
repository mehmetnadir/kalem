# S1 Shorts — "KAYBETTİM = I HAVE LOST" (present-perfect-temel-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 22.52 sn anlatım hazır) + `kapak.png` + `kontrol.png`. Kod `ING-YDT-GR-02-06-T-S1`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../present-continuous/BRIEF.md` ile aynı; yerleşim
`../present-continuous-s1/BRIEF-S1.md` gibi (HUD sayıları dikey v2: `ortak/kunye.js`).
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 7,70 · 16,33; toplam 22.52), kalıp `dikey-senaryo-kalibi.md` §4–5.
Cümleler: 3 (kanca · tek örnek EN + TR · "Tam ders kanalda · 6 dk" çağrısı). `ortak/anlatim/altyazi.json` veri olarak var; bu sürümde altyazı bandı YOK (cümleler ekranda yazılı).

## Dikey yerleşim (px)
Yerleşim ve ölçek: ../present-continuous-s1/BRIEF-S1.md '05.11 düzeltme' bölümü +
../present-continuous-dikey/BRIEF-DIKEY.md §2–§3
(tek kaynak, 05.11 karar 6b); 04.11 tablosu geçersiz.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0.00–3.00 | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3.00–15.78 | 395 |
| 03 | 03-hyperframes-cta | HyperFrames | 15.78–22.52 | 232 |

Kapak: başlık `KAYBETTİM` / `= I HAVE LOST` 0,65–1,45; Türkçe cümle 1 (`Anahtarımı kaybettim, kapıda kaldım.`, 1,00–4,12 → 3,00'dan sonrası sahne 02'de) sözcük zamanlı; ikinci parça `Türkçede geçmiş gibi durur, ama etkisi şimdi sürer.` (3,63–7,15) örnek sahnesinde Caveat 64; uçuş 2,0–3,0.
Örnek: `I have lost my keys.` (EN 7,70–9,46), TR `Anahtarlarımı kaybettim, hâlâ bulamadım.` (9,71–12,91), `Have, artı fiilin üçüncü hâli.` (13,06–15,78). `have` 8,02 ve `lost` 8,18 sarı daire; ev + kapıda figür (standing-4) 480 px; kapıda 3 çizgilik anahtar işareti; formül `have + V3` 13,06–15,22.
CTA: `Tam ders:` · `Present Perfect` bant · saat + `Tam ders kanalda · 6 dk` · 1 sn durgun kuyruk (sözcük zamanları `sozcukler.json` cümle 3).
Çizimler yalnız `ortak/cizim/` içinde VAR olanlar (home, plane, clock, calendar, standing-*, sitting-*; anahtar simgesi yok → el çizgisi).

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/present-perfect-temel-s1 --tema acik --gecis BookFlip --efekt hisirti`.

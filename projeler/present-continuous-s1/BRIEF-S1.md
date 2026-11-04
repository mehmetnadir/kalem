# S1 Shorts — "BU AKŞAM = I AM GOING" (present-continuous-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 26,4 sn, anlatım 25,39 sn hazır) + `kapak.png` (t = 1,97 sn karesi) + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../present-continuous/BRIEF.md` ile aynı.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 8,21 · 18,52; toplam 25,39), kalıp `dikey-senaryo-kalibi.md` §4–5.

## Dikey yerleşim (px)
| Bant | y | İçerik |
|---|---|---|
| HUD | 0–288 | ders adı sol üst, rozetler `YDT · BASIC` + `GRAMMAR`, çip sağ üst |
| İçerik | 288–1344 | kapak / örnek / CTA |
| Altyazı | 1344–1536 | boş (bu sürümde altyazı bandı yok; cümleler ekranda yazılı) |
| Logo | 1440–1536 sol | y 1464, yükseklik 48 |
| Platform | 1536–1920 | BOŞ |

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0,00–3,00 (+12 geçiş) | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3,00–18,52 (+12) | 478 |
| 03 | 03-hyperframes-cta | HyperFrames | 18,52–25,39 (+1 sn kuyruk) | 236 |

Kapak: başlık 0,65–1,45; Türkçe cümle 1,00'dan sözcük zamanlı; uçuş 2,0–3,0 (başlık → çip, cümleler yukarı, eskiz solar).
Örnek: `going` altı çizgi, `şimdiki` / `gelecek` belirteç, figür + ev + hilal 8,3'ten, kart 8,0'dan, `go + -ing` 12,77–13,73, `am · is · are` 15,41 / 16,05 / 17,09.
CTA: `Tam ders:` 0,45 · `Present Continuous` bant 1,0 / 1,44 · saat + `Tam ders kanalda · 6 dk` 2,4 / 3,51 · 1 sn durgun kuyruk.

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/present-continuous-s1 --tema acik --gecis BookFlip --efekt hisirti`.

# S1 Shorts — "AGO = PAST" (simple-past-ileri-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 21,08 sn anlatım hazır + 1 sn kuyruk) + `kapak.png` (t = 1,97 sn karesi) + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../simple-past-ileri/BRIEF.md` ile aynı.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 6,02 · 14,65; toplam 21,08), kalıp `dikey-senaryo-kalibi.md` §4–5, senaryo `pilot/grammar-tenses-05-simple-past-ileri-s1/senaryo.json`.
Kod `ING-YDT-GR-02-10-I-S1`; HUD sayıları dikey v2 (`ortak/kunye.js`).

## Dikey yerleşim (px)
| Bant | y | İçerik |
|---|---|---|
| HUD | 0–288 | ders adı sol üst (`SIMPLE PAST`), rozetler `YDT · ADVANCED` + `GRAMMAR`, çip sağ üst |
| İçerik | 288–1344 | kapak / örnek / CTA |
| Altyazı | 1344–1536 | boş (bu sürümde altyazı bandı yok; cümleler ekranda yazılı) |
| Logo | 1440–1536 sol | y 1464, yükseklik 48 |
| Platform | 1536–1920 | BOŞ |

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0,00–3,00 (+12 geçiş) | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3,00–14,65 (+12) | 362 |
| 03 | 03-hyperframes-cta | HyperFrames | 14,65–21,08 (+1 sn kuyruk) | 223 |

Kapak: başlık `AGO` / `= PAST` 0,65–1,45; Türkçe cümle `Ago görürsen Present Perfect yazma.` 1,00'dan sözcük zamanlı (Ago 1,00 · görürsen 1,40 · Present 2,20 · Perfect 2,60 · yazma 3,04); `Perfect` üstüne kırmızı çizgi 3,04'te; uçuş 2,0–3,0.
Örnek: `Sınav bu tuzağı sever` (3,71'den); kart `The manager resigned two weeks ago.` 6,02'den sözcük zamanlı (resigned 6,66 · two 7,30 · weeks 7,54 · ago 7,94); `ago` sarı daire; figür + takvim 6,2'den; TR `Müdür iki hafta önce istifa etti.` 8,59; `Ago belirli zaman, yani Simple Past` (10,98–13,70): `ago → Simple Past` kartı 13,14'te.
CTA: `Tam ders:` 14,65 (Tam 14,65 · ders 14,97) · `Simple Past` bant 15,77 / 16,17 · saat + `Tam ders kanalda · 6 dk` (6 17,05 · kanalda 19,04) · 1 sn durgun kuyruk.

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/simple-past-ileri-s1 --tema acik --gecis BookFlip --efekt hisirti`.

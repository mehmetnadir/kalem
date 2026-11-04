# S1 Shorts — "AGO VARSA SIMPLE PAST" (present-perfect-ileri-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 22.12 sn anlatım hazır) + `kapak.png` + `kontrol.png`. Kod `ING-YDT-GR-02-06-I-S1`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../present-continuous/BRIEF.md` ile aynı; yerleşim
`../present-continuous-s1/BRIEF-S1.md` gibi (HUD sayıları dikey v2: `ortak/kunye.js`).
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 6,34 · 15,93; toplam 22.12), kalıp `dikey-senaryo-kalibi.md` §4–5.
Cümleler: 3 (kanca · tek örnek EN + TR · "Tam ders kanalda · 6 dk" çağrısı). `ortak/anlatim/altyazi.json` veri olarak var; bu sürümde altyazı bandı YOK (cümleler ekranda yazılı).

## Dikey yerleşim (px)
| Bant | y | İçerik |
|---|---|---|
| HUD | 0–288 | ders adı sol üst, rozetler `YDT · ADVANCED` + `GRAMMAR`, çip sağ üst |
| İçerik | 288–1344 | kapak / örnek / CTA |
| Altyazı | 1344–1536 | boş |
| Logo | 1440–1536 sol | y 1464, yükseklik 48 |
| Platform | 1536–1920 | BOŞ |

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0.00–3.00 | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3.00–15.38 | 383 |
| 03 | 03-hyperframes-cta | HyperFrames | 15.38–22.12 | 232 |

Kapak: başlık `AGO VARSA` / `SIMPLE PAST` 0,65–1,45; Türkçe cümle 1 (`Ago gördün mü, Present Perfect elenir.` 1,00–4,12 ve `Bu sınav tuzağına düşme.` 4,27–5,79) sözcük zamanlı; uçuş 2,0–3,0 (cümle 1'in sonu örnek sahnesine taşar, yazı hazır belirir).
Örnek: `She moved to Berlin two years ago.` (EN 6,34–8,50), TR `İki yıl önce Berlin'e taşındı.` (8,75–10,91), `Ago var, yani Simple Past. Has moved yanlış olurdu.` (11,06–15,38). `ago` (8,02) kırmızı alt çizgi; ev (home) + yürüyen figür (standing-2) 480 px, takvim (calendar); `Has moved` (13,62) üstüne kırmızı çarpı; `Simple Past` (12,34) sarı daire.
CTA: `Tam ders:` · `Present Perfect` bant · saat + `Tam ders kanalda · 6 dk` · 1 sn durgun kuyruk (sözcük zamanları `sozcukler.json` cümle 3).
Çizimler yalnız `ortak/cizim/` içinde VAR olanlar (home, plane, clock, calendar, standing-*, sitting-*; anahtar simgesi yok → el çizgisi).

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/present-perfect-ileri-s1 --tema acik --gecis BookFlip --efekt hisirti`.

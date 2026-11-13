# 06-canvas-kok1-film-spor — P2 (önizleme hazır, render yok)
Düz canvas, 1144 kare, t_bas 91,66, cümle 14–19, çip `Root 1 / 3`, ajanda etkin Roots (etkin 2). Künye `ortak/kunye.js`.
İçerik: film kartı (acts, keeps halkası, tv çizimi) · Türkçe çeviri · öğrenci balonu (soru anı 1, `yanılgı:` olay bitmiş → geçmiş) · özet → geniş zaman + film/kitap/öykü etiketleri (öğrenci baş sallar) · spor kartı (runs halkası, futbol topu) · çeviri · spor yorumu → runs, spor etiketi.

| Olay | Sözcük | t0 (sn) | Sapma |
|---|---|---|---|
| acts halkası | acts | 93,25 | 0,00 |
| tv çizimi | movie | 94,53 | 0,00 |
| keeps halkası | keeps | 97,01 | 0,00 |
| balon karşılığı: acts? halkası + karttaki acts parıltısı | acts? | 109,16 | 0,00 (parıltı +0,05) |
| özet | Özetin | 110,58 | 0,00 |
| ok (özet → geniş zaman) | olay | 112,10 | 0,00 |
| film etiketi | bitmiş | 112,42 | 0,00 |
| geniş zaman | geniş | 113,54 | 0,00 |
| kitap / öykü etiketi | Kitap / öykü | 114,66 / 115,62 | 0,00 |
| runs halkası | runs | 117,61 | 0,00 |
| futbol topu | ball | 118,17 | 0,00 |
| spor yorumu | Spor | 126,08 | 0,00 |
| spor etiketi | yorumunda | 126,40 | 0,00 |
| runs (sarı) + parıltı | runs | 127,93 | 0,00 (parıltı +0,05) |
| runs halkası (son) | gelir. | 128,66 | 0,00 |

Kontroller: `ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu`, sonra açık tema (son koşu AÇIK): "önizleme hazır". `node --check` sahne.js ve sahne-ortak.js temiz. Betikle doğrulandı: sahnedeki 24 sözcük araması sozcukler.json'da var, sapma ≤ 0,02 sn.
Kapı (cakisma-kapisi) ve sahne-kare KOŞULMADI (şef EK 12:40); `k/` boş. QA şeridi koşar.
Not: yerleşim ölçülerle (fontTools genişlikleri) hesaplandı, gözle doğrulanmadı. Riskli yerler: tv/futbol topu çizimi kutusu, balon–kart arası boşluk (kart alt 490, balon üst 520).

## QA 13.11
Kapı (sunucu): çakışma yok (152 örnek, 3489 kutu). Kareler: k/06-canvas-kok1-film-spor-{93.3,108.5,121.5,128.5}.png (açık), k/koyu/…-113.9.png (koyu). Göz: kart alt 490 – balon üst 520 boşluğu görsel olarak yeterli, binme yok; öğrenci başı 116,75'te sönüyor, cevap bitiminden sonra (soru-ani.md ile uyumlu). Koyu tema doğru. Düzeltme yok. Kalan: yok.

QA 13.11 ek: Koyu kare: k/koyu/06-canvas-kok1-film-spor-113.9.png bakıldı, renk hatası yok.

QA 13.11 ek 2: Halka kuralı: acts, keeps, runs halkaları altçizgiye çevrildi (sahne-ortak.js halka(..., alt=true), başlangıç tb+0,2 sn). Balondaki 'acts?' ve özet 'runs' halkalarına bakılmadı; komşuya değmiyordu (k/…-121.5, -128.5). Kapı: çakışma yok (152 örnek, 3486 kutu); k/06-canvas-kok1-film-spor-98.5.png temiz.

QA 13.11 ek 3: simge–etiket/cümle taraması: çizimler cümleyle uyumlu (kod ve kareler üzerinden); uyuşmazlık yok.

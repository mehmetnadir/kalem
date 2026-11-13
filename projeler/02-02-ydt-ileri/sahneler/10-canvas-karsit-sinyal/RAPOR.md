# 10-canvas-karsit-sinyal — P2 (önizleme hazır, render yok)
Düz canvas, 1075 kare, t_bas 224,18, cümle 34–37, çip `Contrast`, ajanda etkin Roots (etkin 2). Öğrenci sesi yok.
İçerik: sinyal sütunları (geçici | kalıcı, söner) · kalıcı uzun bant, geçici kısa bant · yarın işaretçisi, sürer / sürmez, "bu durum yarın da sürer mi?" · Farmers kartı (grow halkası, kalıcı oku) · çeviri · Bu da kalıcı · zaman sözcüğü yok · anlama bak · sürekli mi, geçici mi? (iki banda ok + soru işareti).

| Olay | Sözcük | t0 (sn) | Sapma |
|---|---|---|---|
| geçici başlığı + ayraç | Geçici | 224,73 | 0,00 |
| this week / this semester / these days | this / this / these | 226,26 / 227,38 / 228,58 | 0,00 |
| kalıcı başlığı | Kalıcı | 230,19 | 0,00 |
| every / always | every, / always. | 232,04 / 233,08 | 0,00 |
| uzun bant | kimliğin | 235,71 | 0,00 |
| kısa bant | haftalık | 239,63 | 0,00 |
| yarın işaretçisi | yarın | 242,83 | 0,00 |
| sürer oku ve etiketi | sürer | 243,23 | 0,00 |
| sürmez etiketi | mi? | 243,63 | 0,00 |
| grow halkası | grow | 245,06 | 0,00 |
| kalıcı oku | sunflowers | 246,42 | 0,00 |
| kalıcı etiketi | Thrace. | 247,30 | 0,00 |
| kalıcı halkası | kalıcı. | 252,97 | 0,00 |
| anlama bak | anlama | 256,65 | 0,00 |
| sürekli: ok, soru işareti | sürekli | 258,09 | 0,00 |
| geçici: ok, soru işareti | geçici | 258,97 | 0,00 |

Kontroller: önizleme hazırlığı koyu, sonra AÇIK tema koştu ("önizleme hazır"); `node --check` temiz; 23 sözcük araması doğrulandı.
Kapı ve sahne-kare KOŞULMADI (şef EK). `k/` boş.
Not: yerleşim gözle doğrulanmadı. Riskli yerler: "yarın" çizgisi uzun bandı keser (bilinçli); son soru işareti 259,0 + 0,45 sn, sahne sonu 259,61'e yakın (son 12 kare durgun olmalı: QA kontrol etsin).

## QA 13.11
Kapı (sunucu): çakışma yok (143 örnek, 1499 kutu). Kareler: k/10-canvas-karsit-sinyal-{227.7,237.6,247.6,259.1}.png + 244.6 (açık), k/koyu/…-242.6.png (koyu). Düzeltme: şef (a) son geçici ok + "?" t_son − 0,45 sn öncesine alındı (ok tG−0,2'de başlar, "?" tG−0,1, süre 0,2 → bitiş ≈ 259,07 ≤ 259,16); 259,1 karesinde ikisi de tam çizilmiş. "yarın" çizgisi (244,6 karesi): açık sarı bant üstünden geçiyor ama okunur, yazıyı kesmiyor → kısaltılmadı. Koyu tema doğru. Kalan: son 12 kare durgunluğunu olaylar.json ile doğrulamadım (görsel olarak 259,1'de tamam).

QA 13.11 ek 2: Halka kuralı: 'grow' halkası (Farmers'a değiyordu) altçizgiye çevrildi; 'Thrace.' sarı altçizgisi kaldı. Kapı: çakışma yok (143 örnek, 1498 kutu); k/10-canvas-karsit-sinyal-247.6.png temiz.

zaman eşitleme 13.11: cümle 30 +0,38 sn. Mutlak zamanlar (T() yakınları, SON, tb) +0,38 sn, TBAS 224,18→224,56 (36 sabit). Kapı: çakışma yok (143 örnek, 1498 kutu). Kareler 238,0 / 244,9 / 248,0 / 259,5 temiz; son ok ve '?' tam çizili.

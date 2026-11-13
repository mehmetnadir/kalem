# 07-canvas-kok2-tabela — P2 (önizleme hazır, render yok)
Düz canvas, 858 kare, t_bas 129,38, cümle 20–23, çip `Root 2 / 3`, ajanda etkin Roots (etkin 2).
İçerik: daire 2 · Kök · Tabela · kök cümlesi kartı (says, keep halkası, kafesteki köpek) · Türkçe çeviri (söner) · tabela, mektup, kitap çizimleri · sabit mesaj etiketi · sabit içerik → says · the sign / letter / book says (says sarı, altı çizili).

| Olay | Sözcük | t0 (sn) | Sapma |
|---|---|---|---|
| daire 2 | İkinci | 129,93 | 0,00 |
| Kök | kök: | 130,41 | 0,00 |
| Tabela (el yazısı) | tabela. | 131,13 | 0,00 |
| says halkası | says | 133,36 | 0,00 |
| köpek çizimi | animals | 134,96 | 0,00 |
| kafes çubukları | cages, | 135,60 | 0,00 |
| keep halkası | keep | 137,04 | 0,00 |
| tabela çizimi | Tabelanın | 146,86 | 0,00 |
| sabit mesaj etiketi | değişmez. | 147,90 | 0,00 |
| zarf çizimi | Mektup | 148,94 | 0,00 |
| kitap çizimi | kitap | 149,50 | 0,00 |
| sabit içerik | sabit | 149,98 | 0,00 |
| ok | geniş | 152,14 | 0,00 |
| says (sarı) + parıltı | gelir: | 152,94 | 0,00 |
| the sign / letter / book says | the | 153,67 / 155,11 / 156,47 | 0,00 |
| says altı çizgisi | says, / says, / says. | 154,23 / 155,59 / 156,87 | 0,00 |

Kontroller: önizleme hazırlığı koyu, sonra AÇIK tema koştu ("önizleme hazır"); `node --check` temiz; 19 sözcük araması sozcukler.json ile doğrulandı.
Kapı ve sahne-kare KOŞULMADI (şef EK). `k/` boş.
Not: yerleşim gözle doğrulanmadı. Riskli yerler: kafes (1470–1770) ile kart sağ kenarı (1410) arası 60 px; sol alt tabela/zarf çizimleri tek "çizim" kutusu olarak elle bildirildi (çakışma kapısı için).

## QA 13.11
Kapı (sunucu): ilk koşu "sabit mesaj × tabela kesişim 223x9 px" (gerçek: etiket tabela direk tabanına değiyordu; tabela/zarf tek çizim kutusu uyarısı çıkmadı). Düzeltme: "sabit mesaj" etiketi (x 150, y 905) → (x 400, y 850), tabela ile mektup arası altı. Yeniden koşu: çakışma yok (114 örnek, 3326 kutu). Kareler: k/07-canvas-kok2-tabela-{132.2,140.1,148,157.1}.png (açık), k/07-canvas-kok2-tabela-144.png (koyu; görmedim, dosya k/ altında). Göz: kafes kart sağ kenarına 60 px boşluk var, taşma/binme yok, yazı ≥ 56 px. Kalan: kafes çizimindeki hayvan kafası belirsiz (köpek/tavşan); anlam kaybı yok, değiştirilmedi.

QA 13.11 ek: Şef kararı 4: kafesteki hayvan (dog.svg, belirsiz görünüyordu) cat.svg ile değiştirildi, ad 'kedi', kutu 220x190, enCok 20 (cümle 'animals' dediği için belirli tür yok; kedi kafes çubuklarının arkasında tanınıyor). Sunucuda kapı: çakışma yok (114 örnek, 3326 kutu); k/07-canvas-kok2-tabela-157.1.png temiz.

QA 13.11 ek 2: Halka kuralı: says ve keep halkaları altçizgiye çevrildi (children'a değen 'keep' dahil). Kapı: çakışma yok (114 örnek, 3325 kutu); k/07-canvas-kok2-tabela-157.1.png temiz.

QA 13.11 ek 3: simge–etiket/cümle taraması: çizimler cümleyle uyumlu (kod ve kareler üzerinden); uyuşmazlık yok.

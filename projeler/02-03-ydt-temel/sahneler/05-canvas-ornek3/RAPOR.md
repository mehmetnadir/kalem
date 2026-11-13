# 05-canvas-ornek3 — RAPOR (13.11, P2; render yok)

Motor: Düz canvas · 1920×1080 · 30 fps · 522 kare · t_bas 51.57. Tema: açık/koyu hazırlık koştu (son koşu açık).

## Olay ↔ sözcük t0 (yerel kare = round((t − t_bas) × 30); sapma 0)

| Cümle:sözcük | t0 (sn) | Kare | Olay |
|---|---|---|---|
| 5:0 Üçüncü | 52.12 | 16 | daire içinde 3 |
| 5:1 örnek. | 52.6 | 31 | tek kart |
| 5:2 It | 53.41 | 55 | kök sözcük sözcük (It) |
| 5:4 getting | 53.81 | 67 | basamak 1 |
| 5:5 harder | 54.05 | 74 | basamak 2 + `harder and harder` belirteç |
| 5:7 harder | 54.73 | 95 | basamak 4 + yükselen ok |
| 5:9 find | 55.25 | 110 | laptop |
| 5:13 nowadays. | 56.13 | 137 | `nowadays.` sarı daire |
| 5:14 Bugünlerde | 57.34 | 173 | Türkçe çeviri |
| 5:19 Nowadays | 60.54 | 269 | ok Bugünlerde → nowadays |
| 5:24 harder | 63.83 | 368 | `harder and harder` sarı daire |
| 5:26 harder | 64.79 | 397 | parıltı |
| 5:28 Bu | 66.2 | 439 | ok → etiket |
| 5:31 değiştiğini | 67.44 | 476 | CHANGING |
| 5:32 söyler. | 68 | 493 | parıltı |

## Kapı ve göz

- Çakışma kapısı ve sahne-kare: ŞEF NOTU (13.11 12:40) gereği KOŞULMADI; QA şeridi koşar. Kare görüntüsü yok (`k/` boş).
- `node --check` JS: geçti. `ONIZLE_YALNIZ=1 bash calistir.sh` (koyu, sonra açık): "önizleme hazır".
- Kapı notu: dekoratif çizgiler `isaret`; yazı kartın içinde; simgeler yazıyla örtüşmeyecek konumda (elle hesap).

## QA 13.11
- Kapı: çakışma yok (69 örnek, 1191 kutu). Kareler `k/05-canvas-ornek3-{52.5,57,63,68}.png`, koyu `kk/05-canvas-ornek3-62.png`.
- Göz: taşma yok, tema renkleri doğru, "CHANGING" kalemle yazılırken (68 sn karede yarım; sahne sonunda tamam). Zayıf nokta: sağdaki boş dizüstü ikonu amaçsız sayılabilir (grafik + ok yeterli). Düzeltilmedi (şef kararı).
- Güncelleme (şef isteği): boş dizüstü simgesi kaldırıldı (`sahne.js`), önizleme yenilendi, kapı temiz, kare `k/05-canvas-ornek3-63.png` doğrulandı (simge yok, grafik + ok kaldı).
- QA 13.11 ek (halka/kutu taraması): nowadays ve harder and harder halkaları altçizgi oldu. Kapı: çakışma yok (69 örnek, 1137 kutu).
- QA 13.11 ek: alt çerçeveyi kesen ikinci ok (Türkçe → nowadays, `sahne.js`) kaldırıldı; sağdaki grafik oku kaldı. Kapı: çakışma yok (69 örnek, 1137 kutu). Kare `k/05-canvas-ornek3-64.3.png` doğrulandı (alt ok yok, çerçeve temiz).

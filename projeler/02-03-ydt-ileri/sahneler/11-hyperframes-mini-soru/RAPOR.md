# Sahne 11-hyperframes-mini-soru — RAPOR (13.11, P2 canlı önizleme; render yok)

Tema: açık (koyu kontrol karesi var)

## İçerik

HyperFrames · 1478 kare · t_bas 287,22 · cümle 15–17. Soru kartı (iki boşluk) + 5 şık, sayaç «Beş şık var», öğrenci yanlış cevabı D (soluk sarı çerçeve, balon), Hayır ile D kırmızıya döner, doğru B yeşil + 4 sik_not pili (A, C, D, E), this week belirteci, am staying / recommend dolgusu, kapanışta signal ve verb halkası.

## Dosyalar

| Dosya | Durum |
|---|---|
| calistir.sh | `ONIZLE_YALNIZ=1 bash calistir.sh` ve `--tema koyu` koşar ("önizleme hazır"); render yalnız bayrak olmadan |
| olaylar.json | 44 olay, son olay karesi 1435, aynı karede en çok 3, son 12 kare olaysız |
| k/ | k/11-hyperframes-mini-soru-298.5.png, k/11-hyperframes-mini-soru-300.5.png, k/11-hyperframes-mini-soru-312.png, k/11-hyperframes-mini-soru-316.png, k/11-hyperframes-mini-soru-320.5.png, k/11-hyperframes-mini-soru-333.png · koyu: k/koyu/11-hyperframes-mini-soru-333.png |

## Olay zamanı ↔ sözcük t0 (kare = round((t0 − t_bas) × 30); Δ = en yakın ölçülen olay)

| Olay | Sözcük | t0 (sn) | kare | ölçülen kare | Δ sn |
|---|---|---|---|---|---|
| kart + MINI QUESTION | Mini | 288.14 | 28 | 28 (cizgi) | 0.00 |
| I (kök başlar) | I | 291.11 | 117 | 117 (tik) | 0.00 |
| sayaç Beş (halka + 5) | Beş | 297.74 | 316 | 316 (cizgi) | 0.00 |
| öğrenci başı / Bence | Bence | 299.33 | 363 | 363 (tik) | 0.00 |
| D şıkkı çerçeve (D) | D | 299.97 | 382 | 382 (tik) | 0.00 |
| Hayır: D çerçevesi kırmızı | Hayır. | 303.20 | 479 | 479 (vurus) | 0.00 |
| this week belirteci | This | 307.36 | 604 | 604 (cizgi) | 0.00 |
| am staying dolgusu | am | 309.88 | 680 | 680 (tik) | 0.00 |
| recommend dolgusu + daire | Recommend | 311.20 | 719 | 719 (tik) | 0.00 |
| doğru B yeşil | B | 315.44 | 847 | 847 (vurus) | 0.00 |
| A notu (stay) | stay, | 318.40 | 935 | 935 (tik) | 0.00 |
| C notu (tavsiyede) | tavsiyede | 323.76 | 1096 | 1096 (tik) | 0.00 |
| D notu (yalnız) | yalnız | 327.36 | 1204 | 1204 (tik) | 0.00 |
| E notu (özne) | özne | 330.88 | 1310 | 1310 (tik) | 0.00 |
| signal halkası | signal | 333.45 | 1387 | 1387 (parilti) | 0.00 |
| verb halkası (check) | check | 335.05 | 1435 | 1435 (parilti) | 0.00 |

## Kapı

`node araclar/cakisma-kapisi.mjs 02-03-ydt-ileri --sahne 11-hyperframes-mini-soru` → 11-hyperframes-mini-soru | ölçülmedi (HyperFrames; kapı kapsamı dışı), kareler gözle denetlendi

## Not

Gözle bakıldı: recommend dairesi ilk koşuda `a` sözcüğüne değiyordu → daire genişliği yazıya indi. D kırmızı çerçeve yalnız yanlış cevap işareti; yeşil yalnız B.

## QA 13.11

- Kapı: HyperFrames, kapı kapsamı dışı (sunucuda 'ölçülmedi'), kareler gözle denetlendi.
- Kareler: k/11-hyperframes-mini-soru-324.png (C notu anı, 'tavsiyede'), -324 koyu k/koyu/…-324.png
- Düzeltme: Ham yeşil kalktı (vurgu + mürekkep tik); C şıkkı notu 'recommend → no -ing' karesi yeniden alındı, not yerinde ve okunuyor.
- Kalan sorun: Yok.

# Sahne 09-paperjs-tuzak — RAPOR (13.11, P2 canlı önizleme; render yok)

Tema: açık (koyu kontrol karesi var)

## İçerik

Paper.js · 1277 kare · t_bas 221,32 · cümle 11–13. TRAP etiketi, kart 1 (has sarı kutu), deniz çizgisi, Türkçe çeviri, soru anı 2 (öğrenci balonu, having ↔ has oku), has + -ing yazılıp kırmızı çarpıyla silinir, köşe listesi have (own) · believe · recommend → NO -ing, performative yalnız recommend'de, kart 2 (recommend sarı daire).

## Dosyalar

| Dosya | Durum |
|---|---|
| calistir.sh | `ONIZLE_YALNIZ=1 bash calistir.sh` ve `--tema koyu` koşar ("önizleme hazır"); render yalnız bayrak olmadan |
| olaylar.json | 35 olay, son olay karesi 1236, aynı karede en çok 3, son 12 kare olaysız |
| k/ | k/09-paperjs-tuzak-223.5.png, k/09-paperjs-tuzak-227.7.png, k/09-paperjs-tuzak-234.5.png, k/09-paperjs-tuzak-240.png, k/09-paperjs-tuzak-249.png, k/09-paperjs-tuzak-258.5.png, k/09-paperjs-tuzak-262.9.png, k/09-paperjs-tuzak-264.png · koyu: k/koyu/09-paperjs-tuzak-262.9.png |

## Olay zamanı ↔ sözcük t0 (kare = round((t0 − t_bas) × 30); Δ = en yakın ölçülen olay)

| Olay | Sözcük | t0 (sn) | kare | ölçülen kare | Δ sn |
|---|---|---|---|---|---|
| TRAP etiketi | Tuzak. | 222.24 | 28 | 28 (tik) | 0.00 |
| kart 1: It | It | 225.77 | 134 | 134 (cizgi) | 0.00 |
| has sarı kutu | has | 225.93 | 138 | 140 (cizgi) | 0.07 |
| deniz çizgisi | sea. | 227.29 | 179 | 179 (cizgi) | 0.00 |
| Manzara çok güzel (çeviri) | Manzara | 228.26 | 208 | 208 (cizgi) | 0.00 |
| öğrenci balonu (soru anı 2): Manzarası | manzarası | 231.49 | 290 | 305 (tik) | 0.00 |
| balon: having | having? | 234.18 | 386 | 386 (cizgi) | 0.00 |
| -ing yazılır (has yanında) | -ing | 239.66 | 550 | 550 (cizgi) | 0.00 |
| believe satırı | Believe | 241.02 | 591 | 591 (tik) | 0.00 |
| recommend satırı | Recommend | 247.52 | 786 | 786 (tik) | 0.00 |
| performative etiketi | performative | 248.56 | 817 | 817 (cizgi) | 0.00 |
| kart 2: I definitely recommend… | I | 256.91 | 1068 | 1068 (cizgi) | 0.00 |
| → NO -ing | Sinyal | 261.24 | 1198 | 1198 (tik) | 0.00 |

## Kapı

`node araclar/cakisma-kapisi.mjs 02-03-ydt-ileri --sahne 09-paperjs-tuzak` → 09-paperjs-tuzak | çakışma yok (170 örnek, 7660 kutu; baş düzeltmesinden sonra yeniden koşuldu)

## Not

Gözle bakıldı: öğrenci başı ilk koşuda eksikti (peeps-kit SVG'de stroke kökte yok → svgCiz `cizgi` seçeneği eklendi), düzeltildi; ok cümlenin altından geçer.

## QA 13.11

- Kapı: P2 koşusu geçerli, yeniden koşulmadı (13.11 sunucu karesi: --kapisiz).
- Kareler: k/09-paperjs-tuzak-240.png, -258.5.png; koyu k/koyu/…-240.png
- Düzeltme: KUNYE ezmesi kaldırıldı; künye ve ajanda doğru.
- Kalan sorun: Yok.
- Ek (13.11 son tur): künye değişikliğinden sonra kapı (sunucu): çakışma yok (170 örnek, 7660 kutu); kareler k/09-paperjs-tuzak-240.png, -258.5.png.

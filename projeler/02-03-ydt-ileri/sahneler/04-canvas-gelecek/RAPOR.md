# Sahne 04-canvas-gelecek — RAPOR (13.11, P2 canlı önizleme; render yok)

Tema: açık (koyu kontrol karesi var)

## İçerik

Düz canvas · 1053 kare · t_bas 48,59 · cümle 4–6. İki fiilli tek cümle kartı (are leaving / takes off sarı halka), zaman çizgisi 9 → 11, Türkçe çeviri, öğrenci balonu (soru anı 1, 9 sözcük, balon ↔ cümle numaralı sarı noktalar), fark tablosu (We + bavul → ARRANGEMENT → V-ing · uçak + saat → TIMETABLE → V1 / V-s, eşittir işareti), halkalar, öğrenci baş sallar.

## Dosyalar

| Dosya | Durum |
|---|---|
| calistir.sh | `ONIZLE_YALNIZ=1 bash calistir.sh` ve `--tema koyu` koşar ("önizleme hazır"); render yalnız bayrak olmadan |
| olaylar.json | 47 olay, son olay karesi 1025, aynı karede en çok 3, son 12 kare olaysız |
| k/ | k/04-canvas-gelecek-52.5.png, k/04-canvas-gelecek-54.4.png, k/04-canvas-gelecek-62.7.png, k/04-canvas-gelecek-64.5.png, k/04-canvas-gelecek-70.png, k/04-canvas-gelecek-76.5.png, k/04-canvas-gelecek-83.png · koyu: k/koyu/04-canvas-gelecek-83.png |

## Olay zamanı ↔ sözcük t0 (kare = round((t0 − t_bas) × 30); Δ = en yakın ölçülen olay)

| Olay | Sözcük | t0 (sn) | kare | ölçülen kare | Δ sn |
|---|---|---|---|---|---|
| are leaving halkası (sarı) | are | 51.24 | 79 | 79 (cizgi) | 0.00 |
| takes off halkası | takes | 53.72 | 154 | 154 (cizgi) | 0.00 |
| zaman çizgisi: 9 noktası | nine, | 52.48 | 117 | 117 (cizgi) | 0.00 |
| zaman çizgisi: 11 noktası | eleven. | 54.24 | 169 | 169 (cizgi) | 0.00 |
| Türkçe çeviri 1. satır (el yazısı) | Dokuzda | 55.45 | 206 | 206 (cizgi) | 0.00 |
| öğrenci balonu ilk sözcük (soru anı 1) | ikisi | 60.48 | 357 | 357 (tik) | 0.00 |
| balon sözcüğü -ing ↔ nokta 1 | -ing, | 62.56 | 419 | 419 (tik) | 0.00 |
| fark tablosu: We figürü | We | 66.20 | 528 | 528 (cizgi) | 0.00 |
| ARRANGEMENT | Kişisel | 68.13 | 586 | 586 (tik) | 0.00 |
| uçak çizimi | Our | 71.02 | 673 | 673 (cizgi) | 0.00 |
| TIMETABLE | Sabit | 73.27 | 740 | 740 (tik) | 0.00 |
| eşittir işareti (Both mean the future) | Both | 76.24 | 834 | 830 (cizgi) | 0.03 |
| arrangement halkası | arrangement | 80.32 | 952 | 952 (cizgi) | 0.00 |
| timetable halkası | timetable. | 82.32 | 1011 | 1011 (cizgi) | 0.03 |

## Kapı

`node araclar/cakisma-kapisi.mjs 02-03-ydt-ileri --sahne 04-canvas-gelecek` → 04-canvas-gelecek | çakışma yok (140 örnek, 3337 kutu)

## Not

Gözle bakıldı: taşma yok; balon sağa kaydırıldı, öğrenci başı kenara taşmıyor; numaralı noktalar tema renginde (vurgu).

## QA 13.11

- Kapı: P2 koşusu geçerli, yeniden koşulmadı (13.11 sunucu karesi: --kapisiz).
- Kareler: k/04-canvas-gelecek-60.png, -70.png; koyu k/koyu/…-60.png
- Düzeltme: KUNYE ezmesi (Object.assign) kaldırıldı; künye 'PRESENT CONTINUOUS vs SIMPLE PRESENT · YDT ADVANCED', ajanda Hook·Key·Items·Trap doğru göründü.
- Kalan sorun: 'are leaving' dairesi 'We'ye, 'takes off' dairesi 'flight'a değiyor (düz canvas el dairesi); küçük, değiştirilmedi.
- Ek (13.11 son tur): "are leaving" ve "takes off" daireleri sahne.js 69. satırda `+8` → `+3` (denenen `-6` kendi harflerini kesti). Yeni kare k/04-canvas-gelecek-60.png ve -53.9.png: daireler "We" ve "flight" sözcüklerine değmiyor. Kapı (sunucu): çakışma yok (140 örnek, 3337 kutu).
- Ek 2 (13.11 son tur): "are leaving" ve "takes off" halkaları kaldırıldı (dar sözcük aralığında harfleri kesiyordu); yerine vurgu renginde (`SARI`) el altçizgisi (`altCizgi`, w 7,5), öbeğin SON sözcüğü yazıldıktan 0,3 sn sonra başlar (sahne.js `cevre(a, b, tohum)`, tb = son sözcük t0 + 0,3). Kareler: k/04-canvas-gelecek-53.9.png ("takes" yazılmış, "off" yok, takes-off çizgisi YOK), -54.2.png ("off" yazıldı, çizgi henüz yok), -54.5.png (çizgi çiziliyor), -56.png (iki çizgi tam), -60.png, koyu k/koyu/…-60.png (renk doğru). Öğrenci figürü tamamlanmış kare: k/04-canvas-gelecek-62.7.png (baş, gözlük, balon). Kapı (sunucu): çakışma yok (140 örnek, 3337 kutu). Not: karelerdeki soluk sarı çizgi cümle yazıcısının konuşulan-sözcük izleyicisidir, işaret değil.

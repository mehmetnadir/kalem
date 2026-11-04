# Sahne 05 — Örnek 3 (düz canvas) — RAPOR

Tema: acik

04.11.2026 · 517 kare · t_bas 51,98 · cümle 5 · çıkış geçişi fade. Ortak kod `../04-canvas-ornek2/sahne-ortak.js`.

## Yapılan
- Künye `Example 3 / 3`, etkin 1; kare 0'dan sabit; ilk 12 kare boş, son 12 kare durgun (salınım `icerik_kare`'de donar).
- `Look!`: Fredoka 110 kırmızı pop (ölçek 0,6→1 taşmalı, vurus 0,9) + kalem ile çizilen ünlem.
- Kedi dolgusu (zemin renginde) kediyi gövde çizgisinin önüne alır; tırmanış yol + salınım + hafif eğim.

## Zamanlama (BRIEF satırı → gerçek kare)
| BRIEF | Beklenen kare | Gerçek kare |
|---|---|---|
| Daire içinde 3 | 0–31 | 12–28 daire, pop 21–32 |
| Look! pop + vurus | 39 | 39 (vurus 0,9); ünlem 46 ve 54 |
| Cümle sözcükleri | 60 – 108 | 60 – 108 (sozcukler.json t0) |
| Ağaç | 40–79 | 40–79 (1,3 sn, 4 darbe); parıltı 80 |
| Kedi çizimi / tırmanış | 73 / 96–136 | 73–95 çizim; 96–136 tırmanış; 3 toz çizgisi 96–100 |
| Türkçe çeviri | 130–… | 130–147 |
| Etiketler Look! / Listen! / Watch out! | 207 / 229 / 256 | kutu 207 / 229 / 256; yazı + tik 214 / 235 / 263 |
| Sarı ok → NOW noktası | 325–358 | ok 325; nokta 346; NOW yazısı 349; nabız 355 |
| is / climbing daire | 402 / 411 | 402 / 411 |
| Formül kartı | 455–465 | kutu 455; be 455; + 456; V-ing 456; is 460; climb-ing 462 |

## Kontrol anları
Kontrol.png: 0, 103, 206, 310, 413, 503. Tam boy `k/`: 0106 (55,5 sn), 0271 (61,0 sn), 0475 (67,8 sn).

## Sayılar
- video.mp4: 517 kare, 1920×1080, yuv420p, 30 fps.
- Darbe: 42 (daire 1, ünlem 2, ağaç 4, kedi 4, toz 3, etiket kutusu 12, ok 3, NOW noktası 1, halka 2, kart 4, alt çizgi 6). Olay: 22 (cizgi 13, tik 6, vurus 2, parilti 1); aynı karede en çok 2.
- En uzun sakin aralık ≈ 2,0 sn (56,8–58,8 sn; kedi salınımı ve nabız dışında hareket yok).

## Görsel denetim bulguları ve düzeltmeler
1. Tur 1: halkalar komşu harflere değiyordu → sözcük aralığı +10 px, halka payı 6 px.
2. Tur 1: kedi ağaç tacının içinde bitiyor; Tabler ağacında gövde yalnız ≈115 px görünür. "Aşağıdan ortaya" okunuyor; kedi dolgusu tacın alt çizgisini örtüyor.
3. Çakışma yok, güvenli alan içinde, künye tam. Cümle tek satıra sığdı (en ≈ 850 px).

## Açık sorular
- Tabler `cat.svg` yalnız kedi başı (gövdesiz). Tırmanış baş simgesiyle gösteriliyor; tam gövdeli kedi için Open Doodles ya da Peeps dışı bir çizim gerekir.
- Toz çizgileri sahne sonuna kadar kalıyor ("hiçbir öğe kaybolmaz" kuralı); isterseniz solabilir.
- `NOW` noktası kalın tek darbe ile çiziliyor (el çizimi); nabız halkası süs efekti.

## Çalışmayan / eksik
Eksik madde yok.

## Tur 3 (şef göz denetimi: Coco ağaç + gövdeli kedi, alt yarı)
- `svgYollari` beyaz dolgulu örtü yolunu (`#fff`/`#ffffff`/white) atlıyor; `transform` zinciri DOMMatrix ile uygulanıyor.
- Ağaç `coco/tree.svg`, kutu x 1200–1840, taban y ≈ 900, 53,3–54,6 sn, 9 darbe. Kedi `coco/cat.svg` 170 px, 54,4–55,0 çizilir, 55,15–56,5 y ≈ 860 → 520 tırmanır (±4 px, ±3°); kedi gövde dolgusu ağaç çizgilerini örter; 3 toz çizgisi 55,95'te solar.
- Cümle y 460. Ok etiketlerden NOW noktasına (830, 802) + Caveat NOW; kart x 140, y 820–980.
- Kontrol: 517 kare; k/0106, 0271, 0475 ve kontrol.png yenilendi.
- Açık: Coco ağacı sık çizgili, kedi hâlâ kolay seçilmiyor (kalın kontur w 4,2). Cümle y 460'ta `is` halkasının tepesi `Look!` ünleminin noktasına yaklaşıyor.
- Tur 4: Look! tabanı y 350 (40 px yukarı), kedi kontur w 4,6 (dolgu zemin rengi).

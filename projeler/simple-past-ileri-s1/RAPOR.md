# simple-past-ileri-s1 — S1 Shorts üretim raporu (05.11)

| Çıktı | Kare | Süre |
|---|---|---|
| cikti.mp4 (acik) | 663 | 22,1 sn |
| cikti-koyu.mp4 (koyu) | 663 | 22,1 sn |
| sahne 01 / 02 / 03 | 102 / 362 / 223 | zaman.json ile birebir (iki tema, ffprobe) |

102 + 362 + 223 − 2 × 12 = 663 (birlestir.py aynı sayıyı yazdı). `kapak.png` = sahne 01 kare 59 (t 1,97).

- Sahneler: `sahneler/01-hyperframes-kapak` (AGO / = PAST, Ago görürsen / Present Perfect / yazma., figür + saat),
  `02-paperjs-ornek` (Sınav bu tuzağı sever, EN kart + ago dairesi, TR çeviri, figür + takvim + geri ok,
  ago → Simple Past), `03-hyperframes-cta` (Tam ders: · Simple Past bandı · saat + 6 dakika · hap).
- Şablon: simple-present-ileri-s1. kalem-paper.js: yerel `altyaziSec` yok (yamalı kunye.js); `?canli=1` iken `POST /log` atılmaz.
- Kırmızı yalnız Perfect üstündeki tek çizgi (3,04); sahne 01 bu sesleri yazmaz (kare ≥ 90), sahne 02 yazar.
- Editör kapısı: konsol hatası 0. `EDITOR.durum()`: t 1,9 slot 0 · t 8 slot 1 · t 18 slot 2, hepsi `hazir:true, goster:true`.
  Ekran: `sahneler/02-paperjs-ornek/k/editor-t1.9.png`, `editor-t8.png`, `editor-t18.png`.
- Telefon kontak: her sahnenin `k/telefon-01.png` (acik), `k/telefon-koyu-01.png` (koyu); tüm video kontağı baktım.
- Baktığım kareler: 01 `k/59.png`, kontrol.png · 02 `k/0006.png`, `0048.png`, `0216.png`, `0349.png`, kontrol.png · 03 kontrol.png.
- `ortak/kunye.js` satırı doğru: ders `SIMPLE PAST`, rozet `YDT · ADVANCED` + `GRAMMAR`.

## Neden yeniden
| Koşu | Sebep |
|---|---|
| 01, 03 (acik, 2.) | yardim.py künyesi `SIMPLE PRESENT` yazıyordu (şablondan kalma) → `SIMPLE PAST`; koyu koşu düzeltmeden sonra |

## Sapmalar / açık sorular
- BRIEF-S1 §Dikey "altyazı bandı boş" diyor; görev gereği altyazi.json bandı dolu (1400–1536).
- `ago → Simple Past` iki satır (ago + ok üstte, Simple Past altta); tek satıra 984 px sığmadı.
- Sahne 01 saat çizimi tabler/clock (eller 4:30; etiket yok). Şablonun 3. denetimi: HF sahnelerinin 02 ile arka plan tonu farkı şablondaki gibi.

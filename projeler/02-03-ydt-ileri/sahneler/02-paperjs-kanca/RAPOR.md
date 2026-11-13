# Sahne 02 — Kanca (Paper.js, 384 kare, t_bas 3,00, 02-03 YDT ileri)

Tema: acik

## İçerik
Faz A (3,40–9,5): iki kart `are leaving` / `takes off` (el kutusu + Fredoka 80), ortada kalemle sarı `?`, etiketler `PRESENT CONTINUOUS` (6,03) / `SIMPLE PRESENT` (7,39), `leaving` halkası, `takes` belirteci, `vs`, `?` üstüne halka; faz A 9,20–9,53'te söner. Faz B (10,19–15,2): `bu derste` planı: 4 kutu KEY · PAIR · ITEMS · TRAP, rakamlar 2 · 4 · 1; `karar anahtarını` derken kalemle anahtar çizimi (10,25); `görüyoruz.` anında dört tik. Künye: bölüm `Hook`, ajanda Hook · Key · Items · Trap (etkin Hook). Kod: kalem-paper.js ileri kopyası + `sondur` (yazı sönmesi) + `window.__kalemOlaylar` (olaylar.json kaynağı).

## Olay zamanları ↔ sözcük t0 (ortak/anlatim/sozcukler.json)
| olay | sözcük | t0 (küresel sn) | olay (küresel sn) | sapma | yerel kare |
|---|---|---|---|---|---|
| are leaving kutusu+yazı | zaman. | 3.48 | 3.40 | -0.08 | 12 |
| PRESENT CONTINUOUS etiketi | şimdiki | 6.03 | 6.03 | +0.00 | 91 |
| leaving daire | zamanı | 6.47 | 6.47 | +0.00 | 104 |
| SIMPLE PRESENT etiketi | geniş | 7.39 | 7.39 | +0.00 | 132 |
| takes belirteç | zamanı | 7.71 | 7.71 | +0.00 | 141 |
| vs (kalemle) | yan | 8.23 | 8.23 | +0.00 | 157 |
| ? daire | koyar. | 8.59 | 8.59 | +0.00 | 168 |
| KEY kutu | karar | 10.19 | 10.19 | +0.00 | 216 |
| KEY etiket | anahtarını, | 10.51 | 10.51 | +0.00 | 225 |
| PAIR kutu | iki | 11.47 | 11.47 | +0.00 | 254 |
| ITEMS kutu+4 | dört | 12.99 | 12.99 | +0.00 | 300 |
| TRAP kutu+1 | bir | 13.95 | 13.95 | +0.00 | 328 |
| dört tik | görüyoruz. | 14.59 | 14.59 | +0.00 | 348 |

## Kapı ve kontrol
- Kapı: `cakisma-kapisi.mjs 02-03-ydt-ileri --sahne 02-paperjs-kanca` → `02-paperjs-kanca | çakışma yok (51 örnek, 760 kutu)` (çıkış 0). Kapı kilidi alındı ve bırakıldı. İlk sürümde `vs` yazısı faz A grubunu `oge:` ile paylaşıyordu (bilinen sınıf): ayrı grup (`fazVs`) verildi, yanlış alarm değil önlem.
- olaylar.json: 32 olay (kare 12–360).
- Render yok: `video.mp4` üretilmedi; `ONIZLE_YALNIZ=1 bash calistir.sh` hazırlık yolu ve canlı önizleme (`?canli=1&mesaj=1&tbas=…`, sahne-kare.mjs ile) kullanıldı. `kontrol.png` = k/ karelerinden ffmpeg kontak sayfası (video değil).

## Kare yolları
`k/` altında; kontak: `kontrol.png`.

## Notlar
- `are leaving` kartı sözden (`ayrı` 3,16 / `zaman.` 3,48) sonra 3,40'ta başlar: ilk 12 kare geçiş altında durgun olmalı; `zaman.` t0'a göre −0,08 sn. `takes off` 4,00 (söz yok, cümle 4,12'de biter).
- 14,19–15,39 TRAP kutusu cümle 2 sonunda; kare 384, içerik 372'de biter (zaman.json uyumlu).
- Kareler k/: 5 görüntü (4,3 · 6,7 · 8,8 · 11,0 · 14,9); 14,9'da TRAP son tik'i çiziliyor (kalem darbesi sürüyor).

## QA 13.11

- Kapı: P2 koşusu geçerli, yeniden koşulmadı (13.11 sunucu karesi: --kapisiz).
- Kareler: k/02-paperjs-kanca-8.8.png, -14.9.png; koyu k/koyu/…-8.8.png
- Düzeltme: Yok.
- Kalan sorun: Son karede ITEMS tiki henüz çizilmemiş (14,9 sn); sahne 15,39'da bitiyor, kabul.
- Ek (13.11 son tur): k/02-paperjs-kanca-15.3.png alındı; dört tikin hepsi sahne bitmeden çizilmiş (ITEMS dahil), düzeltme gerekmedi. Kapı (sunucu): çakışma yok (51 örnek, 760 kutu).

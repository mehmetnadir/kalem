# Sahne 03 — Karar anahtarı (HyperFrames, 1008 kare, t_bas 15,39, 02-03 YDT ileri)

Tema: acik

## İçerik
`tanim` kartı, 3 grup ses sırasıyla: (1) sinyaller NOW → hint: V-ing · THESE DAYS / NOWADAYS (+ Caveat `(temporary, changing)`) → hint: V-ing · USUALLY → hint: V1 / V-s; sarı belirteç söz anında; `hint:` soluk (ikincil renk), değer mürekkep. (2) ayraç + ARRANGEMENT → V-ing · TIMETABLE → V1 / V-s; kişi (standing-3) `a person` söylenince, saat (tabler clock) `thing` söylenince kalemle. (3) `believe · have · recommend → no -ing` soluk çerçevede + `trap — later`; kırmızı yok. Anahtar çizimi `Karar anahtarı.` (16,31) ile. Künye: bölüm `Key`.

## Olay zamanları ↔ sözcük t0 (ortak/anlatim/sozcukler.json)
| olay | sözcük | t0 (küresel sn) | olay (küresel sn) | sapma | yerel kare |
|---|---|---|---|---|---|
| anahtar çizimi | Karar | 16.31 | 16.31 | +0.00 | 28 |
| NOW + belirteç | Now | 17.68 | 17.68 | +0.00 | 69 |
| hint: V-ing (now) | continuous. | 18.80 | 18.80 | +0.00 | 102 |
| THESE DAYS / NOWADAYS | These | 19.80 | 19.80 | +0.00 | 132 |
| (temporary, changing) | temporary | 22.16 | 22.16 | +0.00 | 203 |
| USUALLY | Usually | 26.64 | 26.64 | +0.00 | 338 |
| hint: V1 / V-s | simple | 27.60 | 27.60 | +0.00 | 366 |
| ayraç | Gelecekte | 28.97 | 28.97 | +0.00 | 407 |
| ARRANGEMENT | arrangement | 31.78 | 31.78 | +0.00 | 492 |
| TIMETABLE | timetable | 34.42 | 34.42 | +0.00 | 571 |
| kişi figürü | person | 37.38 | 37.38 | +0.00 | 660 |
| tuzak çerçevesi | Fiil | 41.31 | 41.31 | +0.00 | 778 |
| believe | Believe, | 43.11 | 43.11 | +0.00 | 832 |
| no -ing | -ing | 45.47 | 45.47 | +0.00 | 902 |

## Kapı ve kontrol
- Kare: HyperFrames (kapı ölçmez). Göz kontrolü 8 kare (18 · 23,5 · 28 · 33 · 36,9 · 41,5 · 46 · 48,1): taşma yok; ilk sürümde kişi figürü ayraç çizgisini ve tuzak çerçevesini kesiyordu → figür 186 px, y 698'e alındı (son kare 48,1 yeniden alındı, temiz).
- olaylar.json: 44 olay.
- Render yok: `video.mp4` üretilmedi; `ONIZLE_YALNIZ=1 bash calistir.sh` hazırlık yolu ve canlı önizleme (`?canli=1&mesaj=1&tbas=…`, sahne-kare.mjs ile) kullanıldı. `kontrol.png` = k/ karelerinden ffmpeg kontak sayfası (video değil).

## Kare yolları
`k/` altında; kontak: `kontrol.png`.

## Notlar
- `hint:` değeri `V-ing` söz t0 + 0,10/0,40 sn'de gelir (sapma ≤ 0,40: önce ok, sonra hint, sonra değer). Satır 1–3 üst üste aynı kalıp.
- Süre 33,2 sn tek kartta; her ~3–4 sn'de bir yeni öğe var, en uzun boşluk 36,26–36,82 (3 sn içinde).
- Ayraç altındaki satırlar 2. grup (ARRANGEMENT / TIMETABLE) `hint:` taşımaz (BRIEF: yalnız sinyal satırlarında).

## QA 13.11

- Kapı: P2 koşusu geçerli, yeniden koşulmadı (13.11 sunucu karesi: --kapisiz).
- Kareler: k/03-hyperframes-anahtar-33.png, -48.1.png; koyu k/koyu/…-33.png
- Düzeltme: Yok.
- Kalan sorun: 'THESE DAYS' altçizgisi alt yazı '(temporary, changing)' ile bitişik; okunuyor, değiştirilmedi.

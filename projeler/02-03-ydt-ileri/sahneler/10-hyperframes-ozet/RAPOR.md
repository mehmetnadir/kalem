# Sahne 10 — Ara özet (HyperFrames, 724 kare, t_bas 263,48, 02-03 YDT ileri)

Tema: acik

## İçerik
`SIGNAL FIRST. THEN THE VERB.` başlığı (Fredoka 76), 3 madde söylendikçe kademeli (`NOW → V-ing · USUALLY → V1 / V-s`; `ARRANGEMENT → V-ing`, `TIMETABLE → V1 / V-s`; `believe · have · recommend → no -ing`). Sağda sahne 03 ile aynı görsel dilde küçük anahtar kartı (anahtar + 3 soluk çerçeve + soluk satırlar + Caveat `(temporary, changing)`); her madde söylenirken sarı ok kendi gruba bağlanır, grup çerçevesi sarıya döner ve söylenen satırlar sarı belirteç alır. Künye: bölüm `Recap`, ajanda noktası yok.

## Olay zamanları ↔ sözcük t0 (ortak/anlatim/sozcukler.json)
| olay | sözcük | t0 (küresel sn) | olay (küresel sn) | sapma | yerel kare |
|---|---|---|---|---|---|
| SIGNAL | Signal | 265.29 | 265.29 | +0.00 | 54 |
| THEN | Then | 266.73 | 266.73 | +0.00 | 98 |
| NOW → V-ing + kart oku | Now | 268.34 | 268.34 | +0.00 | 146 |
| USUALLY → V1 / V-s | usually | 270.18 | 270.18 | +0.00 | 201 |
| ARRANGEMENT + kart oku | düzenleme | 279.06 | 279.06 | +0.00 | 467 |
| TIMETABLE | tarife | 281.18 | 281.18 | +0.00 | 531 |
| believe · have · recommend | Believe, | 283.22 | 283.22 | +0.00 | 592 |
| no -ing | -ing | 285.78 | 285.78 | +0.00 | 669 |

## Kapı ve kontrol
- Kare: HyperFrames (kapı ölçmez). Göz kontrolü 5 kare (267 · 273,5 · 277 · 283 · 286,8): taşma yok; ilk koşuda `believe · have · recommend` arası çok sıkıydı → sözcük boşluğu `gen(" ")` ile ölçüldü, tekrar alındı.
- olaylar.json: 41 olay.
- Render yok: `video.mp4` üretilmedi; `ONIZLE_YALNIZ=1 bash calistir.sh` hazırlık yolu ve canlı önizleme (`?canli=1&mesaj=1&tbas=…`, sahne-kare.mjs ile) kullanıldı. `kontrol.png` = k/ karelerinden ffmpeg kontak sayfası (video değil).

## Kare yolları
`k/` altında; kontak: `kontrol.png`.

## Notlar
- Madde 3 sözden sonra: `Believe,` 283,22–`recommend` 284,82: maddeler `ozet` kademesi (her 3–4 sn'de yeni öğe).
- Mini kart satır etiketleri `THESE DAYS / NOWADAYS` (272,70) söylenince belirteç alır; `(temporary, changing)` `geçici`/`değişen` (275,22/276,02) söylenince açılır.

## QA 13.11

- Kapı: P2 koşusu geçerli, yeniden koşulmadı (13.11 sunucu karesi: --kapisiz).
- Kareler: k/10-hyperframes-ozet-277.png, -286.8.png; koyu k/koyu/…-277.png
- Düzeltme: Yok.
- Kalan sorun: Yok.

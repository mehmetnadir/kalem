# Sahne 01 — Giriş (HyperFrames, 102 kare, 0–3,00 sn, 02-03 YDT ileri)

Tema: acik

## İçerik
Kapak kalıbı (şablon: present-continuous-ileri 01): logo damgası 0,00–0,40; rozet hapları `YDT · ADVANCED` + `GRAMMAR` 0,30/0,40; bavul (kişisel plan) 0,20'den ve uçak (tarife) 1,10'dan kalemle çizilir; başlık `TWO FUTURES` / `TWO TENSES` söz zamanında açılır (3 hareket türü ilk 3 sn'de: damga, kalem çizimi, kinetik yazı). Eskiz ve rozet 2,60–3,00 söner; başlık + logo 3,00'da yerinde (son 12 kare durgun).

## Olay zamanları ↔ sözcük t0 (ortak/anlatim/sozcukler.json)
| olay | sözcük | t0 (küresel sn) | olay (küresel sn) | sapma | yerel kare |
|---|---|---|---|---|---|
| TWO (satır 1) | İki | 1.00 | 1.00 | +0.00 | 30 |
| FUTURES (satır 1) | gelecek. | 1.80 | 1.80 | +0.00 | 54 |
| TWO (satır 2) | İki | 2.84 | 2.74 | -0.10 | 82 |
| TENSES (satır 2) | İki | 2.84 | 2.86 | +0.02 | 86 |

## Kapı ve kontrol
- Kare: kapı HyperFrames sahnesini ölçmez ("ölçülmedi (HyperFrames)" kuralı). Göz kontrolü 5 kare (0,6 · 1,5 · 2,4 · 2,8 · 2,97): taşma yok, üst üste binme yok, tema renkleri kunye.js açık paletle uyumlu.
- olaylar.json: 12 olay (kare 3–86; son 12 kare boş).
- Render yok: `video.mp4` üretilmedi; `ONIZLE_YALNIZ=1 bash calistir.sh` hazırlık yolu ve canlı önizleme (`?canli=1&mesaj=1&tbas=…`, sahne-kare.mjs ile) kullanıldı. `kontrol.png` = k/ karelerinden ffmpeg kontak sayfası (video değil).

## Kare yolları
`k/` altında; kontak: `kontrol.png`.

## Notlar
- BRIEF "başlık künyeye uçar" yapılmadı: cümle 1'in ikinci yarısı (`İki ayrı zaman`) 2,84'te başlıyor, sahne 3,00'da bitiyor; uçuşa 0,16 sn kalır. İlk uçuş denemesi (2,50–3,00) satır 2'yi sözden 0,8 sn önce açmaya zorluyordu, bu yüzden kaldırıldı. Künye sahne 02'nin ilk karesinden başlar. Şef karar versin (açık soru 1).
- `TWO` (satır 2) sözden 0,10 sn önce (2,74), `TENSES` 2,86; `ayrı zaman` sahne 02'de söylenir.

## QA 13.11

- Kapı: P2 koşusu geçerli, yeniden koşulmadı (13.11 sunucu karesi: --kapisiz).
- Kareler: k/01-hyperframes-giris-1.5.png, -2.8.png, -2.97.png
- Düzeltme: Yok.
- Kalan sorun: 2,8 sn karesinde 2. satır yazılıyor (TW), son kare 2,97 sn tam; sorun değil.

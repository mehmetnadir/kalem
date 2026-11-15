# Sahne 03 Kaydet — huni v2 (simple-present-temel-s3, HyperFrames DİKEY 1080×1920, 170 kare, t_bas 12,84; cümle 3 öğretmen)

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh simple-present-temel-s3 03-hyperframes-kaydet 12.90,16.60,18.00 16.60 --hazirla` | çıkış 0 · `kapı çıkış kodu: 0` |
| `cakisma-kapisi.mjs --sahne 03-hyperframes-kaydet --port 41333 --sunucu 41022` | çıkış 0 · `03-hyperframes-kaydet \| çakışma yok (22 örnek, 3125 kutu)` · 0 uyarı |
| `grep -rniE 'tam ders\|dakika'` (html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, 4 kare) | 4 karede aynı: logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 264–595, y 296–339 (taban 330) |
| Boş bölgeler (piksel ölçümü, 4 kare) | 0–280 boş · 1570–1920 boş · sağ 963–1080 (y 280–1570) içerik yok · içerik x 60–959, y 560–1117 · altyazı y 1448–1498 |

Durum: yazıldı, önizleme hazır (`ONIZLE_YALNIZ=1`, son hazırlık AÇIK tema). Render yok. Commit yok.
Tema: acik (koyu kare canlı tema geçişiyle çekildi).

## Dosyalar
- `SPEC.md` (şef) → `uret.py` (agy, tek koşu; şef okudu, düzeltme gerekmedi).
- `calistir.sh`, `olay.py`, `yardim.py`, `nesneler.json`: emsal `02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/` kopyası
  (`nesneler.json` emsal `03-hyperframes-cta`'dan). Şef Edit: `calistir.sh` başlık, `KARE=170`, denetim kareleri (yerel 0,06 / 3,76 / 5,16);
  `uret.py` ile `olay.py` ayrı satırda (sözleşme: `a && b` zincirinde `set -e` uret.py hatasını yutar). `yardim.py`: docstring + `KONU = "Simple Present"`.
  `olay.py`: docstring.
- Üretilen: `proje/index.html`, `zamanlar.json`, `olaylar.json` (4 ses olayı), `k/*.png`, `k/koyu/*.png`.

## Yerleşim
| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal | logo + `@ydspublishing` Lexend 700 42 | BRIEF tablosu; `#kunye > #kanal`, opaklık 1, animasyon yok |
| Künye | konu `Simple Present` Fredoka 700 34 + rozet `YDT · BASIC` Lexend 700 26 | taban 420; hap 386–434, x 309,7–513,2 |
| Kural kartı | kâğıt tonu (`murekkep` %6 dolgu) + kalem çerçeve 4 px | x 60–960, y 560–900, köşe 30 |
| `Does varsa` / `fiil yalın.` | Fredoka 700 88 (sığdı; küçültme yok) | kart içinde ortalı; taban 700 / 804; sözcük başına ayrı `<text>` |
| Yer imi simgesi + `Kaydet` hapı | simge 96 px (Tabler `bookmark` biçimi, 6 px çizgi) · hap Fredoka 700 64 | sol yarı ortalı, y 1022–1118; tek sarı |
| Kâğıt uçak simgesi + `Gönder` | simge 96 px (Tabler `send` biçimi) · Lexend 700 56, hapsız | sağ yarı ortalı, y 1022–1118 |
| Altyazı + karaoke | Lexend 500 44 | 1400–1550, orta x 510; iki parça da tek satır |

## Olay listesi (yerel sn = küresel − 12,84; zaman `sozcukler.json` çapasından, `T(i, bas)` assert'li)
| Olay | Kare · yerel (küresel) | Cümle 3 sözcüğü |
|---|---|---|
| kart çerçevesi kalemle çizilir (0,40 sn, `sine.inOut`) + kâğıt tonu belirir | 0 · 0,00 (12,84) | sahne başı |
| `Does` belirir (0,18 sn) | 17 · 0,55 (13,39) | Does |
| `varsa` | 26 · 0,87 (13,71) | varsa |
| `fiil` | 45 · 1,51 (14,35) | fiil |
| `yalın.` | 57 · 1,91 (14,75) | yalın. |
| kart tam; sahne sonuna kadar hareketsiz (3,20 sn) | 74 · 2,47 (15,31) | yalın. sonu |
| yer imi kalemle çizilir (0,30 sn) | 79 · 2,62 (15,46) | Bir |
| `Kaydet` hapı girer (ölçek 0,9→1, `back.out(1.6)`, 0,30 sn) | 82 · 2,72 (15,56) | Bir + 0,10 |
| kâğıt uçak çizilir (2 yol sırayla, 0,30 sn) | 103 · 3,42 (16,26) | gönder; |
| `Gönder` girer (x −12→0, 0,20 sn) | 105 · 3,50 (16,34) | gönder; + 0,08 |
| durgun kuyruk | 160 · 5,34 (18,18) → 170 | karıştırıyor. sonu |
Ses olayları (`olaylar.json`): kare 12 cizgi 0,4 · 79 cizgi 0,5 · 82 tik 0,6 · 103 cizgi 0,5.
Altyazı: yalnız cümle 3 (2 parça); karaoke çizgisi her sözcüğün t0'ında 0,15 sn'de çizilir, sonraki sözcükte söner.

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `k/03-hyperframes-kaydet-12.9.png` (kare 2) | kanal + künye tam; kalem çerçeveyi sol üstten çizmeye başlamış (≈ 45 px), kâğıt tonu soluk. İçerik henüz yok: geçiş payı (`gecis_kare` 12). Taşma yok. |
| `k/03-hyperframes-kaydet-16.6.png` (kare 113) | kart tam; yer imi + `Kaydet` hapı + uçak + `Gönder` tam; altyazı tek satır x 79–941, `gönder;` altında karaoke çizgisi. Üst üste binme yok. |
| `k/03-hyperframes-kaydet-18.png` (kare 155) | aynı düzen, hareketsiz; karaoke `karıştırıyor.` altında. Kesik yazı yok. |
| `k/koyu/03-hyperframes-kaydet-16.6.png` | koyu zemin; kart tonu ve çerçeve açık mürekkep; hap ve rozet koyu vurgu dolgusu (`#f2a93b`), hap yazısı koyu; kontrast okunur. |

## agy koşu özeti
- uret.py: `/home/sef/.claude/canavar/agy-filo/20261115-192137` (gemini-3.8-flash-high, başarılı, 326 sn, 1 tur).
- Not: özetin "değişen" listesinde başka sahne/paket dosyaları var (`.claude/docs/sozlesme.md`, `02-04-ydt-temel-s1/…/08-…`, `02-04-ydt-temel-s2/…`);
  o dosyalar aynı çalışma ağacındaki paralel oturumlarındır, bu koşu yalnız `uret.py` yazdı.

## Açık noktalar
- Kart sözcükleri yalnız opaklıkla belirir (karaoke sarısı kartta yok, istem gereği). Okunan sözcük vurgusu altyazı bandında kalır.
- İlk kare (12,90) geçiş payında neredeyse boş: çerçeve kare 0'da başlar, 12. karede kapanır. mp4 birleştirmede BookFlip geçişiyle bakılmalı.
- `karıştırıyor.` 18,18'de biter; sahne sınırı 18,10 (zaman.json). Altyazı parça 2 sahne sonuna (yerel 5,67) kadar açık; sahne 04 başında cümle 3 altyazısı yok.
- Simge yolları (Tabler `bookmark`, `send`; MIT) yerel `ortak/cizim/tabler/` kümesinde yok; `uret.py` içinde sabit dize. Kalıcı küme için `ortak/` sahibine öneri.

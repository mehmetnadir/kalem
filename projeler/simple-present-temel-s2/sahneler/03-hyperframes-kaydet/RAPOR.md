# Sahne 03 Kaydet — huni v2 (simple-present-temel-s2, HyperFrames DİKEY 1080×1920, 228 kare, t_bas 11,87; cümle 3 öğretmen)

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh … 11.95,15.45,19.00 19.00 --hazirla` | çıkış 0 · `kapı çıkış kodu: 0` |
| `cakisma-kapisi.mjs --sahne 03-hyperframes-kaydet --port 41333 --sunucu 41022` | çıkış 0 · `03-hyperframes-kaydet \| çakışma yok (30 örnek, 3777 kutu)` · 0 uyarı |
| `grep -rniE 'tam ders\|dakika'` (html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, 4 kare) | 4 karede aynı: logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 264/265–595, y 296–339 (taban 330) |
| Boş bölgeler (piksel ölçümü, 4 kare; sol kenar x 0–40 satır medyanı, eşik 60) | 0–280 boş · 1570–1920 boş · sağ 963–1080 (y 280–1570) içerik yok |

Durum: yazıldı, önizleme hazır (`ONIZLE_YALNIZ=1`, son hazırlık AÇIK tema). Render yok. Commit yok.

## Dosyalar
- `calistir.sh`, `olay.py`, `yardim.py`: emsal `02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/` kopyası (`cp -p`) + şef Edit
  (başlık, `KARE=228`, denetim kareleri 0,08 / 3,58 / 7,13; `KONU = "Simple Present"`; belge satırları).
- `SPEC.md` (şef) → `uret.py` (agy). Şef düzeltmesi 2: (1) anlamsız iki sınır assert'i gerçek sınır denetimiyle değişti;
  (2) QA karesinde hap dışındaki nokta kopuk göründü → nokta hapın içinde (`Simple Present.`), SPEC de güncellendi.
- Üretilen: `proje/index.html`, `zamanlar.json`, `olaylar.json` (4 ses olayı), `k/*.png`, `k/koyu/*.png`.

## Yerleşim
| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal + künye | logo + `@ydspublishing` Lexend 700 42 · `Simple Present` Fredoka 700 34 + `YDT · BASIC` | `Y.kunye_svg()`; rozet hap x 309,7–513,2, y 386–434 |
| Kural kartı | kâğıt `#fff9e6` (açık `#fffdf8`) + kalem kenarı 4,5 px | x 60–960, y 548–912; kenar yolu x 74–946, y 562–898 |
| `Usually, always,` / `every day:` / `Simple Present.` | Fredoka 700 72 | blok ortalı, satırlar sola hizalı x 230,9; taban 646 / 742 / 838; hap x 230,9–789,1, y 774–866 (tek sarı) |
| Yer imi + `Kaydet` | Tabler `bookmark` yolu × 5, çizgi 7 px · Fredoka 700 72, mürekkep, hapsız | grup 510'a ortalı (x ≈ 345–675); ikon y 966–1056, yazı tabanı 1036 |
| Altyazı + karaoke | Lexend 500 44 | 1400–1550, orta x 510, en çok 2 satır |

## Olay listesi (yerel sn = küresel − 11,87; zaman `sozcukler.json` çapasından, `T(i, bas)` assert'li)
| Olay | Kare · yerel (küresel) | Cümle 3 sözcüğü | Hareket |
|---|---|---|---|
| kart girer | 16 · 0,55 (12,42) | `Usually,` | ölçek 0,96→1 + opaklık, 0,45 sn `power3.out` |
| `Usually,` | 16 · 0,55 (12,42) | `Usually,` | opaklık + y 16→0, 0,25 sn |
| `always,` | 55 · 1,83 (13,70) | `always,` | aynı |
| `every day:` | 79 · 2,63 (14,50) | `every` | aynı |
| `Simple Present.` hapı | 110 · 3,67 (15,54) | `Simple` | opaklık + ölçek 0,9→1, 0,30 sn `back.out(1.6)`; 15,84'te biter |
| kart sabit | 120 · 3,99 (15,86) → 216 | `Present.` | hareket yok, 3,21 sn |
| yer imi çizilir | 198 · 6,60 (18,47) | `Kaydet.` | `strokeDashoffset` L→0, 0,30 sn `sine.inOut` |
| `Kaydet` yazısı | 201 · 6,70 (18,57) | `Kaydet.` | opaklık + y 12→0, 0,25 sn |
| durgun kuyruk | 216 · 7,20 (19,07) → 228 | sahne sonu | son 12 kare (geçiş payı) |

Ses olayları (`olaylar.json`): kare 16 vurus 0,5 · 110 tik 0,5 · 198 cizgi 0,6 · 201 tik 0,4.
Altyazı: cümle 2 kuyruğu (`Şu an değil, her sabah yedide kalkarım` / `gibi.`, yerel 0–0,43; yalnız `gibi.` karaoke çizgisi) + cümle 3
(`Usually, always, every day: Simple Present.` 0,50–4,83 · `Bu kuralı kaybetme.` 4,83–6,55 · `Kaydet.` 6,55–7,60).

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `k/03-hyperframes-kaydet-11.95.png` | kanal + künye tam; kart yok (12,42'de girer); altyazı cümle 2 kuyruğu 2 satır, `gibi.` altında karaoke. Taşma yok. |
| `k/03-hyperframes-kaydet-15.45.png` | kart + `Usually, always,` / `every day:`; 3. satır henüz yok (15,54); altyazı 2 satır, `day` altında karaoke. |
| `k/03-hyperframes-kaydet-19.png` | son kare: kart tam, `Simple Present.` sarı hap (`#ffe066`, yazı `#1b2440`), yer imi + `Kaydet` ortalı; altyazı `Kaydet.`. Üst üste binme yok. |
| `k/koyu/03-hyperframes-kaydet-19.png` | koyu zemin; kart krem, hap `#f2a93b`, yer imi ve `Kaydet` krem mürekkep; kontrast okunur. |
İlk tur bulgusu (düzeltildi): hap dışındaki `.` hap kenarından 34 px uzakta kopuk duruyordu ("Present ."). İkinci turda temiz.

## agy koşu özeti
- uret.py: `/home/sef/.claude/canavar/agy-filo/20261115-192216` (gemini-3.8-flash-high, başarılı, 218 sn).
- Not: özetin "değişen" listesinde başka paket/sahne dosyaları var (`02-04-ydt-temel-s2/…`, `02-04-ydt-temel-s3/…`, `sozlesme.md`);
  bunlar aynı çalışma ağacındaki paralel oturumlarındır. Bu sahnede agy yalnız `uret.py` yazdı (mtime 19:25).

## Açık noktalar
- Kare 0'da cümle 2 kuyruk altyazısı görünmez (GSAP `seek(0)` 0'daki `set`'i uygulamaz); kare 1–12 görünür. `gibi.` karaoke çizgisi
  sahne 02'de zaten çizili, burada 0–0,15 sn yeniden çizilir. İkisi de geçiş payının (BookFlip) içinde; mp4 birleştirmede bakılmalı.
- Nokta hapın içinde: BRIEF "`Simple Present` sarı hapta" der; hap metni `Simple Present.` oldu (görsel karar, şef onayı bekler).
  Hikâye A (05) aynı kartı taşıyorsa aynı biçim önerilir.
- Kart yazı bloğu 558 px; kalem kenarının iki yanında ≈ 155 px boş kâğıt kalır (blok ortalı). Fredoka 72 istem değeridir; büyütme kararı şefte.

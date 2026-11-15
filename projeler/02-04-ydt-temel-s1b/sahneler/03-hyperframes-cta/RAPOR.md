# Sahne 03 Çağrı — huni v2 (02-04-ydt-temel-s1, HyperFrames DİKEY 1080×1920, 218 kare, t_bas 25,49; cümle 4 öğrenci)

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh … 25.55,28.60,31.70 31.70 --hazirla` | çıkış 0 · `kapı çıkış kodu: 0` |
| `cakisma-kapisi.mjs --sahne 03-hyperframes-cta` | çıkış 0 · `03-hyperframes-cta \| çakışma yok (26 örnek, 3880 kutu)` · 0 uyarı |
| `grep -rniE 'tam ders\|dakika'` (html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, 4 kare) | 4 karede aynı: logo mürekkebi x 61–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 264–595, y 296–339 (taban 330) |
| Boş bölgeler (piksel ölçümü, 4 kare) | 0–280 boş · 1570–1920 boş · sağ 963–1080 (y 280–1570) içerik yok |

Durum: yazıldı, önizleme hazır (`ONIZLE_YALNIZ=1`, son hazırlık AÇIK tema). Render yok. Commit yok.
Tema: acik (koyu kare canlı tema geçişiyle çekildi).

## Dosyalar
- `SPEC.md` (şef) → `yardim.py` (agy, bölüm A) + `uret.py` (agy, bölüm B; şef 2 savunma dalını sadeleştirdi).
- `calistir.sh` (şef Edit): başlık, `KARE=218`, ana kapak iki tema kopyası `proje/assets/`, denetim kareleri.
- `ortak/kapak/ana-kapak.png`, `ana-kapak-koyu.png`: `projeler/02-04-ydt-temel/kapak*.png` kopyası (`cp -p`, 1920×1080).
- v1 yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/v1/`; eski v1 kareleri `…/k-v1-tasindi/`.
- Üretilen: `proje/index.html`, `zamanlar.json`, `olaylar.json` (4 ses olayı).

## Yerleşim
| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal | logo + `@ydspublishing` Lexend 700 42 | BRIEF tablosu; `#kunye > #kanal`, opaklık 1, animasyon yok |
| Künye | konu Fredoka 700 34 + rozet `YDT · BASIC` Lexend 700 26 | taban 420; hap 386–434, x 665–868 |
| `Gerisi bizde.` | Fredoka 700 96 | x 60, taban 560 (≈ 489–560) |
| Kapak kartı | ana kapak 16:9 | x 60–960, y 620–1126, köşe 24, mürekkep kenar 4 px |
| `@ydspublishing` hapı + `· YouTube` | Lexend 700 56 | hap x 60–568, y 1160–1240 (tek vurgu); `· YouTube` x 586–874, taban 1220 |
| Altyazı + karaoke | Lexend 500 44 | 1400–1550, orta x 510, en çok 2 satır; okunan sözcük altında vurgu çizgisi |

## Olay listesi (yerel sn = küresel − 25,49; zaman `sozcukler.json` çapasından, `T(i, bas)` assert'li)
| Olay | Kare · yerel (küresel) | Cümle 4 sözcüğü |
|---|---|---|
| kapak kartı girer (ölçek 0,94→1 0,50 sn + opaklık 0,25 sn) | 0 · 0,00 (25,49) | sahne başı |
| `Gerisi` kinetik | 16 · 0,55 (26,04) | Gerisi |
| `bizde.` kinetik | 31 · 1,03 (26,52) | bizde. |
| `@ydspublishing` hapı girer | 91 · 3,02 (28,51) | YDS |
| `· YouTube` girer | 124 · 4,14 (29,63) | YouTube |
| durgun kuyruk | 160 · 5,34 (30,83) → 218 | kanalında. sonu |
Ses olayları (`olaylar.json`): kare 12 vurus 0,6 · 16 tik 0,4 · 91 tik 0,6 · 124 tik 0,4.
Altyazı: yalnız cümle 4 (2 parça); karaoke çizgisi her sözcüğün t0'ında 0,15 sn'de çizilir, sonraki sözcükte söner.

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `k/03-hyperframes-cta-25.55.png` | kanal + künye tam; kart girişte (yarı saydam, %94 ölçek). Taşma yok. |
| `k/03-hyperframes-cta-28.6.png` | `Gerisi bizde.`, kart, hap girişte; altyazı 2 satır x 81–936, `YDS` altında karaoke çizgisi. |
| `k/03-hyperframes-cta-31.7.png` | son kare: bütün öğeler tam; altyazı kapalı (kuyruk). Üst üste binme yok. |
| `k/koyu/03-hyperframes-cta-31.7.png` | koyu zemin, koyu kapak (`ana-kapak-koyu.png`) yüklendi; hap ve rozet koyu vurgu dolgusu; kontrast okunur. |

## Tema geçişi
`hf_tema.py` yalnız `#logoimg` href'ini değiştirir. Kapak için `uret.py` küçük bir betik ekler: `#root` sınıfını `MutationObserver`
ile izler, `tema-acik` → `assets/ana-kapak.png`, yoksa `assets/ana-kapak-koyu.png`; iki dosya önceden yüklenir. Koyu kare bunu doğruladı.

## agy koşu özeti
- yardim.py: `/home/sef/.claude/canavar/agy-filo/20261115-184951` (gemini-3.8-flash-high, başarılı, 207 sn).
- uret.py: `/home/sef/.claude/canavar/agy-filo/20261115-184954` (gemini-3.8-flash-high, başarılı, 219 sn).
- Not: iki özetin "değişen" listesinde başka sahne/paket dosyaları var; o dosyalar aynı çalışma ağacındaki paralel oturumlarındır, bu koşular yazmadı.

## Açık noktalar
- Rozet iç boşluğu BRIEF'te yok: 20 px seçildi (canvas `ortak/kunye.js` `rozetPay: 20` ile aynı).
- Ana kapakta rozet `YDT · TEMEL`, künyede `YDT · BASIC` (BRIEF değeri). Aynı karede iki farklı seviye adı görünür; karar şefte.
- Sahne başında (kare 0–7) kart henüz saydam; geçiş (`gecis_kare` 12) bu aralığı örter. mp4 birleştirmede bakılmalı.
- Ses: cümle 3 `Kaydet.` sözcüğü 25,57'de biter (sahne başından 0,08 sn sonra); bu sahne cümle 3 altyazısını göstermez (istem: yalnız cümle 4).

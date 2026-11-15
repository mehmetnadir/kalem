# RAPOR — 02-04-ydt-temel-s3 · 05-hyperframes-kapak-b (kapak B, soru) · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Çıktı (açık) | `P/kapak-b.png` 1080×1920 (md5 `755908ec2d09…`, `k/at-0.5s.png` ile aynı) |
| Çıktı (koyu) | `k/koyu/kapak-b-koyu.png` 1080×1920 (md5 `83a1eb2dea0f…`) |
| `calistir.sh --tema acik` / `--tema koyu` | çıkış 0 / çıkış 0 (`hyperframes snapshot --at 0.5`) |
| `ONIZLE_YALNIZ=1 bash calistir.sh` | çıkış 0, "önizleme hazır" (index.html son durumda açık tema) |
| `uret.py` | `index.html yazıldı 27817` · `S=174 KW=688.6`; SPEC §6 assert'lerinin tamamı geçti |
| Başlık boyu | S = 174 (`NEDEN -ING` 951,3 px ≤ 952; üst sınır 190'a ulaşmadı) |
| Kod yolu | şef `SPEC.md` → `agy-filo tek --rol kod` (gemini-3.8-flash-high, 180 sn, başarılı) → şef okudu, düzeltme gerekmedi |
| agy koşu özeti | `/home/sef/.claude/canavar/agy-filo/20261115-124814/ozet.md` |

## Olay listesi (durağan kare, ses yok, zaman çizelgesi dışı)
| Olay | Kare / sn | Cümle · sözcük |
|---|---|---|
| bütün öğeler tam görünür (tek `set`) | kare 0; yakalama 0,5 sn | yok (`olaylar.json` = `[]`) |

Ekran metni: `YDT · BASIC` · `NEDEN -ING` (Latin I) · `YOK?` (sarı hap) · `The train leaves …` (Fredoka 700 72, `leaves` altında sarı el
altçizgisi). Cevap karede yok (`tarife`, `timetable` html'de yok, assert). Can alıcı `canAlici[1]`, kısa kod `leaves`.

## Yerleşim (nesneler.json, px)
`hud` 0–288 · `baslik` 366–751 (hap 559–751) · `saat` 864–983 · `soru` 866–983 · `duman` 971–1012 · `tren` 1006–1174 ·
`kart` 1200–1344 (x 64–757) · `fig` 865–1341 (x 868–1016, aynalı, trene bakar) · `ok` 1061–1110 (x 671–859, elden lokomotife).
1344–1920 boş. İçerik bandı 352–1392'nin 366–1344 aralığı dolu (≈ %94).

## Bakılan kareler ve bulgu
| Kare | Bulgu |
|---|---|
| `k/at-0.5s.png` (açık) | taşma yok, kesik yazı yok, üst üste binme yok; `-ING` Latin I; hap `#ffe066` + yazı `#1b2440`; `?` ve altçizgi `#d9900f`; saat kolları yedide, rakamsız; figür sola (trene) bakar; 1344 altı boş |
| `k/koyu/kapak-b-koyu.png` (koyu) | aynı yerleşim; hap ve rozet `#f2a93b` + yazı `#1b1a17`; mürekkep `#f3efe6`; okunur kontrast; altyazı/karaoke yok (kapak) |

Düzeltme turu: 0 (ilk koşu kabul ölçütünü sağladı).

## Kararlar (şef)
- Logo HUD sol üst (y 48, h 96). İstem "Logo sol alt; 1344–1920 boş" diyor; iki koşul birlikte sağlanmaz. BRIEF-DIKEY §0 (Nadir 04.11:
  "alt bantta logo yok") ve S1 kapak A/B bitmiş kareleri sol üst. "Sol alt y ≈ 1478" kapak kalıbının eski satırı sayıldı.
- Tek vurgu disiplini: sarı yalnız hap, `?` ve `leaves` altçizgisi (+ rozet). Saat akrebi ana derste sarıydı; burada mürekkep.
- İşaret pozu: peeps-kit figüründe işaret eden kol yok (sözleşme satır 42); figür yatay aynalandı, mürekkep kalem oku elden lokomotife.
- Kısa zemin çizgisi yalnız figür altında; tren kendi rayında.

## Açık noktalar
1. Logo konumu (yukarıdaki karar): Nadir "sol alt" isterse yalnız `kunye_svg()` logo y'si değişir; o zaman 1344–1536 bandı boş kalmaz.
2. `?` 112 px yüksek; kapakta daha baskın istenirse `SH` büyütülür (üst sınır başlık–sahne boşluğu 113 px).
3. `zaman.json` ve `BRIEF-S3.md` değişmedi; `duragan` kaydı uret.py assert'iyle doğrulandı.

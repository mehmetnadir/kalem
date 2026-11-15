# RAPOR v2 — 02-04-ydt-temel-s3 · 04-hyperframes-hikaye (hikâye A, kural kartı) · huni v2 · 15.11.2026

Tema: acik + koyu (iki tema çekildi)

| Kalem | Sonuç |
|---|---|
| Çıktı | `P/hikaye-a.png` + `P/hikaye.png` (`cmp` aynı) · `D/k/hikaye-a-koyu.png` · üçü `png 1080×1920` (ffprobe) |
| Kod | `uret.py` agy yazdı (SPEC v2); şef 1 küçük düzeltme (bilet merkezi 868 → 866, katı assert) · `calistir.sh` `cmp` satırı (şef) |
| İç kurallar | `uret.py` assert'leri geçti: bantlar, kesişim 0, boşluk ≥ 10, yazı ≥ 64, satır ≤ 24, yasak dizgi, emoji yok · `S=120` |
| Çakışma kapısı | çıkış 2 (ölçülemedi; araç sınırı, sahne `sahneler[]` dışında) |
| Metin taraması | `grep -rniE "tam ders\|dakika" …/proje` → sonuç yok |
| Kanal katmanı | açık + koyu: logo ve `@ydspublishing` görünür, sol kenar x 60, y 291–339 içinde |

## Öğe listesi

| Öğe | Kimlik | y bandı | Yazı boyu |
|---|---|---|---|
| Kanal: logo (tema logosu) | `#kunye > #kanal > #logoimg` | 291–339 (resim x 53,15, w 193,49) | — |
| Kanal: `@ydspublishing` | `#kanal-yazi` | taban 330 | Lexend 700 42 |
| Künye konu `Simple Present vs Present Continuous` | `#ku-konu` | taban 420 | Fredoka 700 34 |
| Rozet `YDT · BASIC` (sarı hap) | `#rz0` | 386–434 (x 664,6, w 203,6) | Lexend 700 26 |
| Üst satır `İkisi geleceği anlatıyor` | `#ust` | 472–545 (taban 530) | Lexend 500 64 |
| Başlık `TARİFE` | `#bas1` | 572–683 (taban 683) | Fredoka 700 120 |
| Başlık `≠ PLAN` (sarı hap, `≠` kalem çizgisi) | `#bas2` | hap 705,6–828 (taban 808,8) | Fredoka 700 120 |
| Kural kartı çerçevesi | `#kart-crv` | 850–1040, x 60–960 | — |
| Satır 1 tren + `Tarife → leaves,` (ok çizgi) | `#kart-tren`, `#kart-s1-*` | taban 922 | Fredoka 700 72 |
| Satır 2 `plan → am going.` + bilet (−3°) | `#kart-s2-*`, `#kart-bilet` | taban 1004 | Fredoka 700 72 |
| Yer imi simgesi (SVG yol) + `Kaydet` | `#kaydet-imi`, `#kaydet-yazi` | 1056–1131 (taban 1110) | Fredoka 700 64 |
| Bağ çıkartması yeri | — | 1150–1380 boş zemin | — |
| Alt boş | — | 1400–1920 boş; altyazı yok | — |

## Kanal katmanı ölçümü (PNG piksel taraması, mürekkep/doygun piksel kutusu)

| Tema | Logo görünür kutu (x0, y0, x1, y1) | Yazı görünür kutu | 0–280 | x 962+ | y 1146+ |
|---|---|---|---|---|---|
| açık | 60, 298, 239, 330 | 265, 296, 596, 339 | boş | boş | boş |
| koyu | 60, 298, 239, 330 | 265, 296, 596, 339 | boş | boş | boş |

İçerik görünür kutusu iki temada: x 60–959, y 472–1130.

## Kapı (son satırlar, aynen)

```
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --sahne 04-hyperframes-hikaye --port 41333 --sunucu 41022
HATA sahne bulunamadı: 04-hyperframes-hikaye
çıkış=2
```

## Bakılan kareler ve bulgu

Tek kare (ilk = orta = son): `P/hikaye-a.png` (açık), `D/k/hikaye-a-koyu.png` (koyu). Read ile açıldı.
- Taşma, kesik yazı, üst üste binme yok. `İ` noktalı (`TARİFE`, `İkisi`).
- Tek sarı: başlık hapı (+ künye rozeti, standart parça). Kartta ve `Kaydet`'te sarı yok. Kırmızı, emoji yok.
- `≠` ve `→` fontta yok; ikisi de kalem çizgisi. Kontrast iki temada yeterli (hap yazısı `pilMetin`).
- v1 öğeleri (üst logo, 2 satır ders adı, `Full lesson` çipi, `Tren tarifeye uyar`, Caveat çağrı, alt `@ydspublishing` hapı) yok.
- Düzeltme turu: 1 (bilet sağ ucu 935,25 → ≤ 934, kod içi).

## agy koşusu

`~/.claude/canavar/agy-filo/20261115-190348/ozet.md` — rol `kod`, gemini-3.8-flash-high, 250 sn, başarılı, tek dosya `uret.py`.

## Açık noktalar

- agy özetinin "değişen" listesinde S1/S2 dosyaları da görünür. agy dökümünde bu yollar yok; S2 `04/proje/index.html`
  agy bittikten sonra (19:09) değişti → eş zamanlı başka oturumun işi. Bu sahne onlara dokunmadı.
- Sahne 08 (`08-hyperframes-kaydet`) bu koşuda yoktu; kart cümlesi BRIEF metninden alındı. 08 bitince iki kartın görünümü karşılaştırılmalı
  (08'de `leaves` sarı hap; burada istem gereği vurgu yok).
- Çakışma kapısı bu sahneyi ölçmez (çıkış 2); yerine `uret.py` iç kuralları + piksel taraması.

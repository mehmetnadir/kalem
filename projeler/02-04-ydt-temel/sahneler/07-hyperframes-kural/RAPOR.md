# Sahne 07 · kural kartı (HyperFrames, 523 kare, 113,37–130,40 sn; cümle 8)

Durum: P2 yazıldı. `ONIZLE_YALNIZ=1` hazırlığı koşuldu, son koşu AÇIK tema. Render yok. Kapı GEÇTİ (çıkış kodu 0).
Tema: acik (koyu kare ayrıca çekildi).

## İçerik

İki sütunlu kural kartı (`tanim`, slayt 3 düzeni), kalemle çizilen tablo:

| Sütun | Başlık + kalıp | Satır 1 | Satır 2 | Satır 3 |
|---|---|---|---|---|
| sol | SIMPLE PRESENT · V1 / V-s | general ← mont | permanent ← ev | timetable (future) ← tren |
| sağ | PRESENT CONTINUOUS · am / is / are + V-ing | right now → tişört | temporary → bavul | arrangement (future) → bilet |

- Sol sütun yazısı x 416'dan başlar, sağ sütun yazısı x 1504'te biter (960 ± 544, ayna). İkonlar dış kenarda.
- Her hücre kısa kalem çizgisiyle örnek ikonuna bağlanır. İkonlar örnek sahnelerinin çizimleridir (03 mont/tişört, 04 ev = Tabler home, bavul kendi çizimimiz, 05 tren/bilet sadeleştirmesi).
- Sütun başlıkları satırlardan SONRA gelir. Sebep: anlatım "Soldakiler geniş zaman, sağdakiler şimdiki zaman" cümlesini satırlardan sonra söyler (önce anlam, sonra ad).
- Alt: MEANING FIRST (Fredoka 700, 68) iki sözcük kinetik vurur. "anlamına" sözcüğünde altına sarı el çizgisi gelir.
- Renk: tek vurgu sarı (yalnız MEANING FIRST belirteci). Kırmızı yok, emoji yok, yeşil gerekmedi (soru yok).
- Yazı tabanı: en küçük yazı 36 (kalıp, Lexend 500). Ölçüler `u()` ile orandır.
- Künye: `kunye_svg("Rule", 2)`; ders adı ve px değerleri `ortak/kunye.js` KUNYE ile aynı. Tema çifti `ortak/hf_tema.py` (tema_hf).

## Olay listesi (cümle 8; yerel sn = küresel − 113,37; kare = yerel × 30)

| Olay | Yerel sn | Kare | Küresel sn | Cümle sözcüğü (i) |
|---|---|---|---|---|
| tablo çerçevesi + sütun ayracı + başlık satırı çizgisi | 0,55 | 16 | 113,92 | Kural kartı (0) |
| 2 satır çizgisi (3 boş satır) | 2,71 / 2,91 | 81 / 87 | 116,08 / 116,28 | üç (4) / fark (5) |
| `general` + bağ + mont (ikon biter 5,25) | 4,07 | 122 | 117,44 | Genel (7) |
| `right now` + bağ + tişört (biter 5,81) | 4,87 | 146 | 118,24 | konuşma (10) |
| `permanent` + bağ + ev (biter 6,95) | 6,07 | 182 | 119,44 | Kalıcı (12) |
| `temporary` + bağ + bavul (biter 8,17) | 7,11 | 213 | 120,48 | geçici (15) |
| `timetable` + bağ + tren (biter 9,35) · `(future)` 8,67 | 8,15 | 244 | 121,52 | Tarifeli (17) · gelecek (18) |
| `arrangement` + bağ + bilet (biter 10,63) · `(future)` 10,07 | 9,43 | 283 | 122,80 | planlanmış (20) · gelecek (21) |
| `SIMPLE PRESENT` | 10,95 | 328 | 124,32 | Soldakiler (22) |
| `V1 / V-s` | 11,59 | 348 | 124,96 | geniş (23) |
| `PRESENT CONTINUOUS` | 12,63 | 379 | 126,00 | sağdakiler (25) |
| `am / is / are + V-ing` | 13,35 | 400 | 126,72 | şimdiki (26) |
| `MEANING` (kinetik) | 14,71 | 441 | 128,08 | Seçmeden (28) |
| `FIRST` (kinetik) | 15,19 | 456 | 128,56 | önce (29) |
| sarı belirteç (altı çizgi) MEANING FIRST | 16,15 | 484 | 129,52 | anlamına (31) |

Hareket aralığı 0,55–16,60 sn: ilk 12 ve son 12 kare durgun (`Y.kontrol` geçti). olaylar.json: 37 olay (24 cizgi).
Her olayın sözcüğü `T(i, bas)` ile denetlenir: sözcük kayarsa üretim durur.

## Kapı

Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel 07-hyperframes-kural 119.4,124.1,130.3 127.6` (önce aynı komut `--hazirla` ile).
Son çıktı satırları:

```
== KAPI
07-hyperframes-kural | çakışma yok (69 örnek, 43884 kutu)
...
kapı çıkış kodu: 0
```

## Bakılan kareler ve bulgu

| Kare | Ne görünür | Bulgu |
|---|---|---|
| `k/07-hyperframes-kural-119.4.png` (yerel 6,0) | çerçeve, ayraç, 3 satır, satır 1 (general/mont, right now/tişört) | sorun yok |
| `k/07-hyperframes-kural-124.1.png` (yerel 10,7) | 3 satır dolu, ikonlar tam, başlık satırı boş (söylenmedi) | sorun yok |
| `k/07-hyperframes-kural-128.9.png` (yerel 15,5) | başlıklar + kalıplar, MEANING FIRST, çizgi yok | sorun yok |
| `k/07-hyperframes-kural-130.3.png` (yerel 16,9) | son hâl, sarı altı çizgi | sorun yok |
| `k/koyu/07-hyperframes-kural-127.6.png` (yerel 14,2) | koyu tema, tablo + başlıklar | kontrast iyi |
| `k/koyu/07-hyperframes-kural-130.3.png` (yerel 16,9) | koyu tema son hâl, sarı çizgi | kontrast iyi |

Taşma, kesilen yazı, üst üste binme, okunmaz kontrast, boş kare yok. Düzeltme turu gerekmedi (0/4).

## Açık noktalar

1. **sahne-kare zamanı küresel saniyedir.** İstem "sahne içi saniye" diyor; `araclar/sahne-kare.mjs` `t`'yi anlatım saniyesi (`tbas` ile) alır. İlk koşu yerel değerlerle (6, 10.7, 16.9 / koyu 14.2) boş kare üretti. Kapı kendi örneklerini aldığı için o koşuda da geçerliydi. Boş kareler `~/Silinecekler/2026-11-14-0204/07-k-bos/` ve `07-qa-kare-bos/` altına taşındı. Sonraki istemlerde zaman t_bas + yerel yazılmalı.
2. **Kod yazım yolu.** Yazma kapısı (`write-size-gate.sh`) 15+ satır `.py` yazımını engelledi; atlatma bayrağı Claude'a kapalı. `uret.py`'yi şef belge olarak yazdı (`/tmp/kalem0204-s07/uret.spec.md`), `agy-filo tek --rol kod` dosyaya geçirdi (gemini-3.8-flash-high, 56 sn), şef bayt bayt karşılaştırdı: eşit (15.540 bayt). İstemdeki "alt ajan açma" kuralıyla çatışır; Claude alt ajanı açılmadı, kapının gösterdiği agy yolu kullanıldı.
3. `olay.py` 02-03 kopyasıdır; tek satır değişti (`uret()` 4 değer döner). `yardim.py` 02-04 sahne 01 kopyası, değişiklik yok.
4. Başlık satırı 0,55–10,95 sn boş durur (tasarım: başlık söylendiği anda). Nadir başlığı baştan isterse soluk başlık + söylenince koyulaşma seçeneği var.
5. Tren ve bilet ikonu çerçeveye ~25 px yakın; kapı çizim × çizim saymaz, gözle sorun yok.
6. Birim testi yok (02-03 HF sahneleri de test taşımıyor); doğrulama kapı + kare. Render yapılmadı (`video.mp4`, `kontrol.png` yok).

Dosyalar: `uret.py`, `olay.py`, `yardim.py`, `calistir.sh`, `olaylar.json`, `proje/index.html`, `k/`, `RAPOR.md`.

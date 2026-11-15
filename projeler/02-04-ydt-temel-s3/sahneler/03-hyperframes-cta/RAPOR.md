# Sahne 03 CTA (02-04-ydt-temel-s3, HyperFrames DİKEY 1080×1920, 347 kare, t_bas 15,99; cümle 4)

Durum: yazıldı. `ONIZLE_YALNIZ=1` hazırlığı koşuldu, son koşu AÇIK tema. Render yok. Kapı GEÇTİ (çıkış kodu 0, çakışma yok).
Tema: acik

| Dosya | Kaynak | Değişiklik |
|---|---|---|
| `uret.py` | S1 s03 kopyası → agy | cümle 3 → 4; ev/bavul → tren/bilet (ana ders sahne 07 `TREN`, `_bilet()`); şef: çizgi 4,0/2,6 → 3,2/2,0 |
| `SPEC.md` | şef | değişiklik tarifi, olay listesi, kabul ölçütü |
| `calistir.sh` | S1 kopyası | başlık (paket, t_bas 15,99) ve denetim karesi yorumu; `ONIZLE_YALNIZ` satırı örnekte vardı |
| `yardim.py`, `olay.py`, `nesneler.json` | S1 kopyası | yalnız `yardim.py` docstring'ine S3 notu |
| üretilen | `uret.py` + `olay.py` | `proje/index.html`, `zamanlar.json`, `olaylar.json` (11 ses olayı) |

## İçerik ve yerleşim (S1 s03 düzeni; aynı ses dosyası, md5 `80e56127…`)

| Satır | Öğe | Yazı · boy | Konum (y) |
|---|---|---|---|
| A | `üç farktan biri` → `üç farkın hepsi` (`üç` yerinde kalır, sarı altçizgi) | Lexend 700 · 72 | taban 452 |
| B | `Tam ders:` (soldan yazılır) | Caveat 700 · 96 | taban 620 |
| Bant | `Simple Present` / `vs Present Continuous`, dolgu `vurgu` | Fredoka 700 · 74 | 660–896 (x 132–948) |
| İkon sol | tren (yandan), 72×25, satır 1 hizası (merkez y ≈ 731) | çizgi 3,2 / ince 2,0 | x 48–120 |
| İkon sağ | sinema bileti, 72×28, satır 2 hizası (merkez y ≈ 823) | çizgi 3,2 / ince 2,0 | x 960–1032 |
| E | saat + `dört buçuk dakikada` | Lexend 700 · 72 | taban 1066 |
| F | `@ydspublishing` hapı (açık: `#ffe066` / `#1b2440`) | Fredoka 700 · 64 | 1200–1312 |

İkon hizası bilinçli: tren (tarife) `Simple Present` satırının, bilet (plan) `Present Continuous` satırının yanında.
İkon çizimi S3 kapak A ile aynı kaynak (ana ders sahne 05 `trenParcalari` / `biletParcalari` → sahne 07 sadeleştirmesi): döngü tutarlı.
Künye: logo, ders adı 2 satır, rozet `YDT · BASIC`, çip `Full lesson` (`KUNYE.cipler["03-hyperframes-cta"]`). Altyazı 1400–1536, 1536 altı boş.
Renk: tek vurgu (bant, hap, `üç` altçizgisi). Vurgu renginde yazı yok. Yeşil, kırmızı, emoji yok. "kanal", QR, "6 dk" yok.

## Olay listesi (yerel sn = küresel − 15,99; zaman `sozcukler.json` cümle 4 çapasından, `T(i, bas)` assert'li)

| Olay | Kare · yerel (küresel) | Cümle 4 sözcüğü (sıra) | Ses olayı |
|---|---|---|---|
| `üç` kinetik + altçizgi (+0,22) | 31 · 1,03 (17,02) | üç (1) | tik 0,4 · cizgi 0,5 |
| `farktan` kinetik | 36 · 1,19 (17,18) | farktan (2) | — |
| `biri` kinetik | 67 · 2,23 (18,22) | biri. (4) | — |
| `Tam ders:` yazımı (1,04 sn) | 83 · 2,78 (18,77) | Tam (5) → ders: t1 (6) | hisirti 0,45 |
| bant girişi + `Simple` | 119 · 3,98 (19,97) | Simple (7) | vurus 0,9 |
| `Present` (satır 1) | 127 · 4,22 (20,21) | Present (8) | — |
| `vs` | 143 · 4,78 (20,77) | ve (9) | tik 0,5 |
| `Present` · `Continuous` (satır 2) | 158 · 5,26 (21,25) · 178 · 5,94 (21,93) | Present (10) · Continuous. (11) | — |
| `farktan biri` çıkışı → `farkın` · `hepsi` | 210 · 7,01 (23,00) → 218 · 232 | Üç (12) · farkın (13) · hepsi (14) | tik 0,4 |
| saat darbesi + `dört` · `buçuk` | 251 · 8,37 (24,36) · 258 | dört (15) · buçuk (16) | cizgi 0,5 |
| `dakikada` + hap girişi | 266 · 8,85 (24,84) | dakikada. (17) | tik 0,6 |
| `@ydspublishing` yazımı (0,70 sn) | 268 · 8,95 (24,94) | dakikada. → t1 25,64 | hisirti 0,5 |
| tren darbesi (sol) | 290 · 9,65 (25,64) | dakikada. t1 | cizgi 0,45 |
| bilet darbesi (sağ) | 293 · 9,75 (25,74) | dakikada. t1 + 0,10 | cizgi 0,45 |

Yerel zamanların hepsi S1 `zamanlar.json` ile birebir eşit (betikle karşılaştırıldı; yalnız anahtar adı `tren_darbe` / `bilet_darbe`).
Hareket yerel 10,20'de (kare 306) biter. Kare 306–346 durgun son düzen. En uzun boş alan: y 660–1392, sahne başı 15,99'dan bant girişi 19,97'ye kadar (≈ 4,0 sn, 9 sn sınırının altında).

## Kapı

Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 03-hyperframes-cta 18.7,23.0,26.4 25.8 --hazirla`

```
== KAPI
03-hyperframes-cta | çakışma yok (44 örnek, 1196 kutu)
== KARE (açık)  18.7 · 23 · 26.4
== KARE (koyu)  25.8
kapı çıkış kodu: 0
```

Düzeltme turu: 1 (tren çizgisi inceltildi; iki koşu da kapı 0).

## Bakılan kareler ve bulgu

| Kare | Ne görünür | Bulgu |
|---|---|---|
| `k/03-hyperframes-cta-18.7.png` | künye, `üç farktan biri` + altçizgi, altyazı `Bu, üç farktan yalnız biri.` | sorun yok; `Tam ders:` 18,77'de başlar |
| `k/03-hyperframes-cta-23.png` | satır A (çıkış 23,00'te başlar), `Tam ders:`, bant 2 satır, altyazı cümle 4/3 | sorun yok |
| `k/03-hyperframes-cta-26.4.png` | son düzen: satır A, `Tam ders:`, bant + tren + bilet, saat satırı, hap | tur 0: tren 72 px'te çizgi 4,0 ile pencere/teker kapanmıştı → 3,2/2,0; tur 1: tren ve bilet okunur. Taşma, kesik yazı, üst üste binme yok; altyazı kapanmış; 1536 altı boş |
| `k/koyu/03-hyperframes-cta-25.8.png` | koyu, ikonlar çizim ortasında | beklenen (25,64'ten çizilir); kontrast yeterli |
| ek: koyu 26,4 (yalnız şef bakışı, `/tmp`) | koyu son düzen | tren ve bilet açık renkte tam; sorun yok |

## agy koşusu

`agy-filo tek --rol kod` · gemini-3.8-flash-high · 120 sn · başarılı. Özet: `~/.claude/canavar/agy-filo/20261115-124456`.
Şef okuması: `diff` S1 ↔ S3 `uret.py` yalnız SPEC'teki satırları gösterir (cümle 4, `TREN`/`BILET` verisi, ikon sabitleri, şerit `assert`'i,
SVG grupları, `veri` anahtarları, 2 `darbeCok` satırı). Özet "değişen" listesi worktree geneli: `02-04-ydt-temel-s2/…` ve S3 sahne 01
dosyaları eş oturumların işidir; bu sahne dışında agy değişikliği yok.

## Açık noktalar

1. **Tren küçük (72×25 px).** Şerit 72 px; yandan tren oranı ≈ 2,9 : 1. Büyütmek için bant daraltılmalı (yazı 74 → ≈ 69) ya da ikonlar hap
   yanına alınmalı (≈ 160 px). BRIEF "küçük" dediği için S1 düzeni korundu.
2. **İkonlar kuyrukta çizilir** (25,64–26,19). BRIEF "25,56–26,56 durgun kuyruk" der; S1 açık nokta 2 ile aynı (S1 göreli çapası korundu).
   Alternatif: tren `Simple` (19,97), bilet `vs` (20,77) çapasında çizilir; kuyruk tam durgun olur.
3. **İkon hizası S1'den farklı** (S1: ikisi bant ortası 778; S3: satır hizası 731 / 823). Gerekçe: tarife ↔ Simple Present, plan ↔ Present
   Continuous. İstenirse iki sabit 778'e döner.
4. Birim testi yok (HF sahneleri test taşımıyor); doğrulama kapı + kare. Render yapılmadı (`video.mp4`, `kontrol.png` yok).
5. Sözleşmeye 1 satır eklendi (`.claude/docs/sozlesme.md`: aynı sesli kısa sahne kopyası + 72 px tren çizgi kalınlığı).

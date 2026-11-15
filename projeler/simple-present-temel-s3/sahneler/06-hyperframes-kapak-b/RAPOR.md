# RAPOR — simple-present-temel-s3 · sahne 06-hyperframes-kapak-b (kapak B, huni v2) · 15.11.2026

İstem: `uretim-tutanagi/istem/sahne/D-06-hyperframes-kapak-b.md` (P0202-S3-C). Tasarım: `SPEC.md` (şef). Kod: agy (`uret.py`).
Durum: BİTTİ. İki tema üretildi. Kapılar geçti; çakışma kapısı durağan kareyi ölçmez (beklenen çıkış 2).

| Çıktı | Yol | Ölçü |
|---|---|---|
| Açık kare | `projeler/simple-present-temel-s3/kapak-b.png` | PNG 1080×1920, RGB |
| Koyu kare | `sahneler/06-hyperframes-kapak-b/k/koyu/kapak-b-koyu.png` | PNG 1080×1920, RGB |
| Ham yakalama | `k/at-0.5s.png` (açık), `k/koyu/at-0.5s.png` (koyu) | 0,5 sn |
| Önizleme | `proje/index.html` (açık temada hazır, `ONIZLE_YALNIZ=1`) | — |

## 1. Dosyalar

| Dosya | Kaynak | Değişiklik |
|---|---|---|
| `calistir.sh` | emsal `02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/` kopyası | başlık yorumu, paket adı; `uret.py` ve `olay.py` ayrı satır (`a && b` zincirinde `set -e` `uret.py` hatasını yutar) |
| `olay.py` | emsal kopyası | docstring |
| `yardim.py` | emsal kopyası | docstring, `KONU = "Simple Present"`, `KONU_PARCA` |
| `zamanlar.json` | emsal kopyası | yok (sure 1,0 · kare 1 · yakala 0,5) |
| `SPEC.md` | şef | yeni |
| `uret.py` | agy (SPEC'ten) | yeni, 520 satır; şef okudu, düzeltme gerekmedi |
| `nesneler.json`, `olaylar.json`, `proje/` | `uret.py`, `olay.py`, `calistir.sh` çıktısı | — |

## 2. Olay listesi

| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| Bütün öğeler görünür: kanal katmanı, künye, başlık `GOES mu,` / `GO mu?`, kâğıt kart (`He doesn't ____.` / `Does she ____?`, boşluk kalem çizgisi), iki eş hap `go` · `goes`, sarı kalem `?` | kare 0 (çizelge 1,0 sn; yakalama 0,5 sn) | — (anlatım yok; zaman çizelgesi dışı; `olaylar.json` = `[]`) |

## 3. Yerleşim (`nesneler.json`, px)

| Blok | x | y | w | h | Not |
|---|---|---|---|---|---|
| kanal | 60 | 291 | 542 | 48 | `Y.kunye_svg()` |
| kunye | 60 | 386 | 453 | 48 | `Simple Present` 34 + `YDT · BASIC` |
| baslik | 126 | 471 | 767 | 328 | Fredoka 700 B = 172, kontur 10 (zemin), ortalı x 510 |
| kart | 163 | 858 | 693 | 264 | Fredoka 72; boşluk 183 px (iki satırda aynı) |
| hap-go | 162 | 1168 | 261 | 125 | dolgusuz, mürekkep çerçeve, Fredoka 80 |
| hap-goes | 458 | 1168 | 261 | 125 | `hap-go` ile aynı boy |
| soru | 760 | 1144 | 99 | 165 | sarı kalem `?` (tek sarı öğe) |

## 4. Kapı sonuçları

| # | Kapı | Sonuç |
|---|---|---|
| 1 | `calistir.sh --tema acik` | rc 0; `index.html yazıldı 7735` · `B=172 KX=165.5 KW=689.0 RX0=164.4 HAP_W=256` · `png,1080,1920` |
| 1 | `calistir.sh --tema koyu` | rc 0; `png,1080,1920` |
| 1 | `file` | iki dosya `PNG image data, 1080 x 1920, 8-bit/color RGB` |
| 1 | `uret.py` iç kuralları | geçti: sınırlar, 21 blok çiftinde kesişim 0, yazı boyu, satır ≤ 24 karakter, görünen metin kümesi, renk kümesi, id'ler |
| 2 | çakışma kapısı | `HATA sahne bulunamadı: 06-hyperframes-kapak-b` · çıkış 2 (beklenen: araç yalnız `zaman.json → sahneler[]` okur; emsal S1-VAR-RAPOR §5). Çakışma karede gözle ve piksel ölçümüyle denetlendi (§5) |
| 3 | `grep -rniE 'tam ders\|dakika' … --include=*.html --include=*.js --include=*.py` | boş (rc 1) |
| 4 | kanal katmanı (piksel) | açık ve koyu karede görünür; logo mürekkebi x 60–239, y 298–330 (resim kutusu 291–339); `@ydspublishing` x 264–596, y 296–339 (taban 330, alt uzantı 339). Kanal ve künye bandı kapak A (`kapak-a.png`) ile piksel piksel aynı: en büyük fark 0 |

QA kareleri: açık tek kare (ilk = orta = son, durağan) + koyu tek kare.

## 5. Bakılan kareler ve bulgu

Ölçüm: satır başına sol kenar (x 0–40) medyanı zemin sayılır; kanal toplamı farkı > 60 olan piksel içeriktir.

| Bölge | Açık | Koyu | Beklenen |
|---|---|---|---|
| üst 0–280 | boş | boş | boş |
| kanal 280–352 | x 60–596, y 296–339 | aynı | kanal katmanı |
| künye 352–456 | x 60–512, y 386–433 | x 60–513 | künye satırı |
| başlık 456–840 | x 137–885, y 477–794 | aynı | 470–800 |
| kart 840–1135 | x 163–856, y 858–1121 | x 167–852, y 862–1117 | 860–1120 |
| hap + `?` 1135–1320 | x 162–859, y 1144–1308 | x 161–859, y 1144–1309 | 1160–1300 (≈) |
| 1320–1400 | boş | boş | boş |
| alt 1400–1920 | boş | boş | boş (altyazı yok) |
| sağ x 960–1080 (bütün y) | boş | boş | boş |

Göz denetimi (Read ile iki kare): taşma yok, kesik yazı yok, üst üste binme yok, boş kare yok. Başlık iki satır aynı boy; virgül
alt uzantısı ile 2. satır arasında boşluk var. Kart iki temada açık kâğıt, yazı koyu mürekkep; boşluk çizgileri aynı boyda.
Haplar aynı biçim; hiçbiri vurgulanmamış. Kırmızı yok, yeşil yok, emoji yok, figür ve karakter görseli yok. y 1150–1380 arasında
boş kutu ya da yer tutucu yok; bu bantta yalnız istemin istediği hap sırası ve `?` var (bkz. açık nokta 2).

## 6. agy koşusu

`agy-filo tek --rol kod --zaman 25m` · gemini-3.8-flash-high · başarılı · 242 sn · özet `/home/sef/.claude/canavar/agy-filo/20261115-194844`.
agy yalnız `uret.py` yazdı. Özetteki "değişen" listesi (`simple-present-temel-s1/…`, `.claude/docs/sozlesme.md`) aynı worktree'de
koşan paralel oturumların işidir (huni v2 taşıması); bu sahne onlara dokunmadı. Düzeltme turu: 0.

## 7. Açık noktalar

1. **Sarı `?` tonu.** `?` kalem çizgisidir (`stroke` = `vurgu`): açık temada `--vurgu` `#d9900f` (koyu sarı), koyu temada `#f2a93b`.
   Hap sarısı (`#ffe066`) krem zeminde çizgi olarak okunmaz (sözleşme: vurgu/zemin ≈ 2,3:1, `#ffe066` daha düşük). Büyük boy
   (165 px, çizgi ≈ 18 px) karede açık seçik okunur. Nadir dolgu sarısı isterse yol: `<clipPath>` + `rect` dolgu (S2 s07 kalıbı).
2. **İstem doğrulama satırı "y 1150–1380 boş zemin mi".** Bu satır hikâye karelerinin bağ çıkartması kuralıdır (standart §6). Kapak B
   istemi aynı bantta hap sırasını ve `?`'yi ister (1160–1300); kare istemin "Bu sahneye özel" maddesine göre üretildi. Kutu yok.
3. **Koyu temada kart kenarı.** Kâğıt kart kalem kenarı `--pilMetin` (koyuda `#1b1a17`) zeminle aynı tondadır; kenar görünmez, kart
   açık kâğıt olarak durur. Kapak A kartı (sahne 01) aynı CSS ile aynı görünür; tutarlılık için değiştirilmedi.
4. **Çakışma kapısı** durağan kareyi ölçmez (çıkış 2). Yerine `uret.py` iç kuralları ve §5 piksel ölçümü kullanıldı.
5. Commit yok (istem). Çıktı PNG'leri ve `proje/` git durumu şefte.

# DUZ2-RAPOR — 02-04-ydt-temel-s3b (A/B kol b, değişken `kanca` = `yanlis-cumle`) · J2 A sınıfı + KBJ gerçek hataları · 15–16.11.2026

İstem: `uretim-hatti/istemler/DUZ2-0204S3.md`. Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` §3A, §4.1, §4.2 satır T3 (b kolu satırı);
`uretim-tutanagi/juri/KBJ-hukum.md`; `uretim-tutanagi/KBC-RAPOR.md`. Kol a raporu: `../02-04-ydt-temel-s3/uretim-tutanagi/DUZ2-RAPOR.md`.
Not: iş 16.11'de makine bellek arızasıyla kesildi. Yarım iş yinelenmedi. Kol b'nin bütün düzeltmeleri arızadan önce bitmişti; bu rapor
ve §3–§4'teki yeniden doğrulama arızadan sonra yazıldı (kapı r2 16.11 00:44).

| Kalem | Sonuç |
|---|---|
| Düzeltilen kusur | HV-24/TD-1 rozet · EK-5b/A3 (c4 sesi, kart, etiket, açıklama başlığı) · DK-1/A5 · EK-7 · EK-6 · AB-8 · kol a'dan kopya kareler · ST-2 ve HV-13 kanıtı |
| Yeniden sentezlenen cümle | **0** (c4 = kol a c3 kopyası, sha256 `74cb0c729581`; AB-9 5/5 eşit) |
| Süre | 29,31 → **32,10 sn** (≤ 35; hedef 22–26 aşıldı, §5) |
| İlk söz · kanca | 0,41 sn (`Hata`) · kanca sahnesi 0,00–4,00 sn (HV-12 sınırda, ≤ 4) · bilgi: kanca cümlesi bitişi 1,45 sn |
| Whisper en düşük | 0,98 (c3 öğrenci sorusu; kol a c2 ile aynı ses); öteki 9 parça 1,00 |
| Çakışma kapısı | çıkış **0** (r2 16.11 00:44; ilk koşu 00:17, 133 örnek) |
| `hyperframes check` | 4 sahne çıkış 0, 0 hata (`hf-check-duz2.txt`) |
| `huni-kapi.mjs --kol-a` | çıkış 1: JR-1b (jüri dosyası düzeltmeden eski) + AB-2 (3 dosya küresel zaman üst verisi; §4) · 21 GEÇTİ |
| AB-8 grep | **boş** (çıkış 1; `surumler.json` `varyant` da yolu taşımıyor) |
| diff beklenmeyen | **0** (196 satır; sınıflama `siniflama-duz2-r2.txt`) |
| mp4 | yok (istem) |

## 1. Düzeltmeler (kusur başına satır)

| Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|
| HV-24 / TD-1 rozet (KBJ HV-24) | `ortak/anlatim/senaryo.json` `giris.rozetler`, `ortak/kunye.js` `KUNYE.rozet`, sahne 01 `yardim.py` `ROZET`, `BRIEF-S3.md`; 02/08/03 kol a ile aynı kod | `YDT · BASIC` → `YDT · TEMEL`; kare 28,28'deki çift rozet (künye `BASIC` + kapak kartı `TEMEL`) kalktı | kod ve çıktıda `grep -rln BASIC` (js, html, json, py, sh) = 0; `huni-kapi` HV-24 GEÇTİ (34 dosya); bütün kareler rozet `YDT · TEMEL` |
| EK-5b / A3 ses c4 | `ortak/anlatim/cumle-4.wav`, `senaryo.json` c4 | "Planı bir kişi yapar. Tren tarifeye uyar: geniş zaman." → "Biletimi aldım, saat belli: kesin düzenleme, şimdiki zaman." + "Tren tarifeye uyar: geniş zaman." | `cumle-4.wav` sha256 `74cb0c729581` = kol a `cumle-3.wav` (kopya, sentez yok); Whisper 1,00 / 1,00 |
| EK-5b / A3 kaydet kartı | `sahneler/08-hyperframes-kaydet/uret.py`, `yardim.py` (kol a ile bayt aynı) | "Tarife → leaves, plan → am going." → "Tarife → leaves," / "kesin düzenleme → am going." (64 px, sol x 96, simge yok) | `k/08-…-20.88.png`, `-22.88.png`, `k/koyu/08-…-20.88.png` |
| EK-5b / A3 sahne 02 etiketleri | `sahneler/02-hyperframes-ornek/uret.py` (kol a ile bayt aynı) | `person → plan`, `train → timetable` → `kesin düzenleme`, `tarife` | `k/02-…-15.6.png`, `-19.6.png` |
| EK-5b / A3 açıklama başlığı | `aciklama-a.md` (= `aciklama.md`), `aciklama-b.md` gövdesi | "Tarife geniş zaman, plan şimdiki zaman" → "Tarife geniş zaman, kesin düzenleme şimdiki zaman" | `diff` kol a ↔ kol b: başlık ve gövde aynı, fark yalnız üst bilgi ve `utm_content` |
| DK-1 / A5 karaoke (KBJ DK-1) | `sahneler/02-hyperframes-ornek/uret.py`, `proje/index.html` (kol a ile bayt aynı, `cmp` eşit) | tek `fill` düz altyazı → sözcük başına `tspan`, ikincil → mürekkep; TR soru yalnız altyazıda, balonda `?` sonra `-ing?` | `k/02-…-10.5.png` (balonda `?`, altyazıda "Neden -ing yok?" ikincil), `-14.png`, `-15.6.png` |
| EK-7 koyu hap geçişi (KBJ EK-7) | `sahneler/08-hyperframes-kaydet/uret.py` (kol a ile bayt aynı) | 0,20 sn çapraz geçiş (koyu temada yazı / hap 2,1:1) → hap yazısı anında söner, mürekkep `leaves,` anında gelir, hap zemini 0,10 sn'de söner | `k/koyu/08-…-23.35.png` (geçiş karesi) ve `-23.38.png`: `leaves,` açık mürekkeple okunur |
| EK-6 açıklama üst bilgisi (KBJ EK-6) | `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` | başlık `02-04-ydt-temel-s3` → `02-04-ydt-temel-s3b … (A/B kol b, grup s3)`; `s3-aciklama-a` → `s3b-aciklama-a`; "Shorts: …-S3, 28,31 sn" → "kol b `s3b` (grup …-S3, değişken kanca), 32,10 sn"; `hikaye-a.png`, `kapak-b.png`, `hikaye-b.png` → "grup türevi … (kol a paketinde; AB §4)" | `head -8 aciklama*.md`; `huni-kapi` HV-18, HV-19 (15 bağ `utm_content=s3b-<set>`) GEÇTİ |
| AB-8 bağımsız kopya (KBJ AB-8) | `ortak/kunye.js:8`; `sahneler/*/proje*/.hyperframes` | `KOK = "/projeler/02-04-ydt-temel-s3/ortak"` → `"/projeler/02-04-ydt-temel-s3b/ortak"`; kol a mutlak yollu snapshot durumları Silinecekler'e (LISTE satır 20) | §3 grep çıktısı boş; `huni-kapi` AB-8 GEÇTİ |
| Kol a'dan kopya kareler (KBJ kare notu) | `sahneler/*/k/` | 02/08/03 kareleri kol a üretiminden geliyordu → bütün sahne kareleri kol b paketinden çekildi; eski kopyalar Silinecekler'e | §3 kare tablosu; 02/08/03 kareleri kol a ile içerikte 27 / 27 piksel eşit (AB-3) |
| KBC açık nokta 7 (sabit cümle no) | sahne 02, 08, 03 `uret.py` (iki kolda bayt aynı) | sabit cümle numarası (4, 5) ve `t_bas` → ilk `The` sözcüğünden türeyen kayma (`KAYMA`, `DT`) | `cmp` kol a ↔ kol b `uret.py` ×3 eşit; 08 ve 02 `index.html` eşit |
| ST-2 kanıt (KBJ ST-2, kanıt yok) | `uretim-tutanagi/hf-check-duz2.txt` | tutanakta `hyperframes check` yoktu → 4 sahne çıkış 0, 0 hata | `hf-check-duz2.txt` |
| HV-13 kanıt (KBJ HV-13, kanıt yok) | `sahneler/08-…/k/` | 2 sn aralıklı kare çifti yoktu → 20,88 ↔ 22,88 çifti | kart bölgesi x 60–960, y 558–902 piksel farkı **0** (PIL `getbbox` = None); fark kutusu yalnız y 971–1495 (Gönder/Kaydet satırları) |

Kapak A (kol b kanca karesi) `HATA` / `NEREDE?` kural terimi taşımaz; yalnız rozet değişti.

## 2. Ses, süre, Whisper

| Cümle | Metin | sha256 (12) | Kaynak | Whisper |
|---|---|---|---|---|
| c1 (öğretmen, değişken) | Hata nerede? | `142d55e5bbd0` | KBC sentezi, değişmedi | 1,00 |
| c2 (EN) | The train to İzmir leaves at 7 pm today. · I am going to the movie theater tonight. | `af9343e6d690` | = kol a c1 | 1,00 · 1,00 |
| c3 (öğrenci) | Hocam, tren de plana göre kalkmıyor mu? Neden -ing yok? | `a65bb1e43a13` | = kol a c2 | 0,98 |
| c4 (öğretmen) | Biletimi aldım, saat belli: kesin düzenleme, şimdiki zaman. · Tren tarifeye uyar: geniş zaman. | `74cb0c729581` | = kol a c3 (**yeni metin, kopya**) | 1,00 · 1,00 |
| c5 | Bu, üç farktan yalnız biri. · Bir arkadaşına gönder; o da karıştırıyor. | `9b7e70ce36dc` | = kol a c4 | 1,00 · 1,00 |
| c6 (öğrenci, çağrı) | Bu sadece başlangıç. · Dersin tamamı YDS Publishing YouTube kanalında. | `6a9927c66d00` | = kol a c5 | 1,00 · 1,00 |

AB-9: kol a `cumle-1…5` = kol b `cumle-2…6`, 5 / 5 sha256 eşit (`sha256sum` ve `huni-kapi` AB-9). Zincir kol a ile aynı:
`sozcuk_uret.py` → `zaman_uret.py` → `kur.py` → `ses-paketle.py --yaz` → `altyazi_uret.py` → `metin_uret.py`.

| Ölçü (sn) | Önce (KBC) | Sonra | Kol a (sonra) |
|---|---|---|---|
| Süre (`zaman.json` son sahne `t_son`) | 29,31 | 32,10 | 31,10 |
| İlk söz | 0,41 (`Hata`) | 0,41 | 1,00 (`The`) |
| Kanca sahnesi (HV-12) | 0,00–4,00 | 0,00–4,00 | 0,00–3,00 |
| Kanca cümlesi bitişi (bilgi) | 1,45 | 1,45 | 6,45 |
| Sahne 02 (değer) | 4,00–16,99 | 4,00–19,78 | 3,00–18,78 |
| Sahne 08 (kaydet) | 16,99–22,33 | 19,78–25,12 | 18,78–24,12 |
| Sahne 03 (çağrı) | 22,33–29,31 | 25,12–32,10 | 24,12–31,10 |

AB-3 göreli an: ilk EN sözcüğü (`The`) kol a 1,00, kol b 2,00 sn. Değişken dışı sahneler bu ana göre iki kolda aynı yerde başlar
(02: +2,00 · 08: +17,78 · 03: +23,12 sn). Sözcükler kol a + 1,000 sn (60 / 60, en büyük sapma 2e-15); altyazı parçaları da +1,000 sn (9 / 9; kol b ayrıca kanca parçasını taşır).

## 3. Kareler, kapılar, yeniden doğrulama

Kareleri arızadan önce ben çektim (`ONIZLE_YALNIZ=1 calistir.sh` + `hyperframes snapshot`); arızadan sonra hepsine yeniden baktım
(PIL kontak sayfası, gerekli yerde tam çözünürlük kırpımı).

| Sahne | Açık kareler (küresel sn) | Koyu kareler |
|---|---|---|
| 01 kanca (değişken) | 0 · 0,6 · 1,2 · 1,8 · 2,8 · 3,45 · 3,97 | 0 · 1,8 · `kapak-a-koyu.png` |
| 02 değer | 4 · 5,2 · 7,6 · 10,5 · 12,2 · 14 · 15,6 · 17,6 · 19,6 | 10,5 · 17,6 |
| 08 kaydet | 19,78 · 20,88 · 22,88 · 24,6 · 25,1 | 20,88 · 23,35 · 23,38 · 24,6 |
| 03 çağrı | 25,12 · 26,5 · 28 · 29,6 · 32,07 | 28 · 32,07 |
| Türev | `kapak-a.png` (= `kapak.png`, sha256 `29394e05c0af`) | `sahneler/01-…/k/koyu/kapak-a-koyu.png` |

Kol b'de kapak B/C ve hikâye yok (AB §4: grup türevi, kol a'da). Açık kareler `proje/index.html`'den yeni; koyu kareler tema betiğinin
koyu geçişinde çekildi, sonra açık `index.html` geri yazıldı (zaman sırası bu yüzden ters).

Bakış sonucu: taşma yok; yazı × çizim çakışması yok; rozet her karede `YDT · TEMEL`; karakter (öğretmen figürü, çağrıdaki ana ders
kapağı) değişmedi; altyazı en çok 2 satır, karaoke sesle aynı anda; koyu temada okunmayan yazı yok (08 geçiş karesi dahil).

| Kapı / ölçüm | Komut | Çıkış |
|---|---|---|
| Çakışma (r2, arıza sonrası) | `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3b --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s3b/uretim-tutanagi/kapi-duz2-r2.json` | **0** (`kapi-duz2-r2.txt`; 4 sahne, 133 örnek) |
| Çakışma (ilk) | aynı komut, `kapi-duz2.json` | 0 (`kapi-duz2.txt`, 00:17) |
| HyperFrames | `hyperframes check sahneler/<01\|02\|08\|03>/proje` | 0 (×4), 0 hata |
| Huni kapısı | (D) `node araclar/huni-kapi.mjs K/projeler/02-04-ydt-temel-s3b --kol-a K/projeler/02-04-ydt-temel-s3` | 1 (`huni-kapi-duz2.txt`; JR-1b, AB-2: §4–§5) |
| AB-3 piksel | kol a 02/08/03 karesi ↔ kol b aynı yerel an (+1,00 sn) | 27 / 27 çift piksel eşit |
| HV-13 | 08 çifti 20,88 ↔ 22,88, kart bölgesi | 0 px |
| AB-9 | `sha256sum` kol a c1…c5 ↔ kol b c2…c6 | 5 / 5 eşit |

AB-8 taraması (istem komutu, kök `K`):

```
$ grep -rn "02-04-ydt-temel-s3/" K/projeler/02-04-ydt-temel-s3b --include=*.js --include=*.html --include=*.json --include=*.py
(çıktı yok; çıkış 1)
```

Geniş tarama (`ydt-temel-s3([^b]|$)`, `.sh` dahil): yalnız yorum satırları ve docstring (02, 03, 08 `uret.py` / `calistir.sh`; 04–07
`calistir.sh`), `senaryo.json` `meta.kimlik` ve `uretim-tutanagi/kol-b.json` `kol_a`. AB-8 bunları saymaz (yorum, `kimlik`, tutanak).

## 4. diff sınıflaması (kol a ↔ kol b)

`diff -rq K/projeler/02-04-ydt-temel-s3 K/projeler/02-04-ydt-temel-s3b`: 196 satır (`diff-rq-duz2-r2.txt`). Satır başına sınıf
`siniflama-duz2-r2.txt`. Arıza öncesi çıktı (`diff-rq-duz2.txt`, 190 satır) ile fark yalnız yeni tutanak dosyaları (6 satır).

| Sınıf | Satır | Beklenen mi |
|---|---|---|
| QA karesi: küresel zaman adı +1,00 (02/08/03; içerik 27 / 27 piksel eşit) | 54 | beklenen |
| Değişken sahne 01 (kanca) | 37 | beklenen (değişken) |
| Üretim tutanağı (paket başına) | 33 | beklenen |
| hyperframes durum dosyası (snapshot/check geçmişi) | 16 | beklenen |
| Türev karesi yalnız kol a (04–07 `k/`; huni-ab §4) | 12 | beklenen |
| Ses: kanca cümlesi + numara kayması (c2–c6 = kol a c1–c5 bayt aynı) | 11 | beklenen |
| Zaman ve söz türevleri (+1,00 sn) | 9 | beklenen |
| Python derleme önbelleği (`__pycache__`, kaynak yolu gömülü) | 7 | beklenen |
| Grup türevi yalnız kol a (kök `kapak-b/c`, `hikaye*`; huni-ab §4) | 5 | beklenen |
| Açıklama üst bilgisi + `utm_content` (EK-6, AB-6) | 3 | beklenen |
| Kapak A (kanca karesi; `kapak-a.png`, `kapak.png`) | 2 | beklenen (değişken) |
| Sahne zaman üst verisi (03, 08 `zamanlar.json` `t_bas` / `kuresel` +1,00) | 2 | beklenen (kapı notu aşağıda) |
| Sahne 03 `index.html` `V.Z.t_bas` (+1,00; kalan V eşit) | 1 | beklenen (kapı notu aşağıda) |
| `BRIEF-S3.md` kol b notu | 1 | beklenen |
| `senaryo.json` (değişken cümle 1 + kol b üst bilgisi) | 1 | beklenen |
| `ortak/kunye.js` `KOK` kol b yolu (AB-8) | 1 | beklenen |
| `surumler.json` (kol b kimliği, süre, revizyon) | 1 | beklenen |
| **BEKLENMEYEN** | **0** | — |

Bu iki r2 dosyası `diff` koşusundan sonra pakete kondu; sonraki bir `diff -rq` 2 tutanak satırı daha verir.

Kapı notu: `huni-kapi` AB-2 şu 3 dosyayı "beklenmeyen" sayar: sahne 03 `proje/index.html`, sahne 03 `zamanlar.json`, sahne 08
`zamanlar.json`. Üçünün farkı yalnız küresel zaman üst verisidir (`t_bas`, `kuresel` +1,00 sn; kanca kol b'de 1 sn uzun).
Sahne 03 `index.html` farkı tek satırdır: `V.Z.t_bas` 24,12 ↔ 25,12. Sahne betiği bu alanı okumaz (`index.html`'de `t_bas` tek
geçiş); 03 kareleri 7 / 7 piksel eşit. Sınıf: beklenen (zaman üst verisi). Kapının beklenen sınıf listesinde bu sınıf yok:
`D/araclar/huni-kapi.mjs` düzeltmesi şefin işi (yazma kapsamım dışında).

## 5. Ölçüt, kapsam dışı ve düzeltilmeyen maddeler

| Madde | Durum | Sebep |
|---|---|---|
| HV-13 kapanış değişkeni bölümü | ölçüt | kol b kapanışı `kaydet` (taban); kanca değişkeni kapanışa dokunmaz. Kart çifti yine de ölçüldü (§3, 0 px) |
| HV-17 | ölçüt | J2 B1; söyleniş `YeDeSe` (D-0340) |
| HV-20, HV-21 (kol b) | ölçüt | AB §4: kapak B/C ve hikâye kol a'da; kol b yalnız `s3b-kapak-a` taşır |
| AB-4, AB-5, AB-7 | ölçüt | yayın sonrası denetim (juri-olcutleri §2d) |
| EK-8 kanca karesi "5 satır" | **düzeltilmedi, şef kararı** | KBJ altyazıyı dizgi satırı saydı. Klişe 16 eşiği "5+ satır dizgi"; kol b kanca karesinde 4 dizgi satırı var (başlık 2 + yanlış cümle 2), altyazı huni §2 zorunlu katmanı. Kol a kancası aynı yoğunlukta (başlık 2 + cümle 1 + 2 etiket + altyazı); J2 kol a EK-8'i C5 (kontak yok) saydı. Altyazıyı yalnız kol b'de gizlemek kanca değişkenine ikinci bir fark ekler (altyazı var/yok). "≤ 3 satır" hedefi iki kolda ortak kanca kuralı ister |
| EK-11 dinleme | kapsam dışı | Nadir dinler, şef yazar ("Hata nerede?" parçası; Whisper 1,00) |
| EK-4 adres gidiş zamanı | kapsam dışı | şefin işi |
| JR-1b (`huni-kapi`) | beklenen | KBJ hükmü 15.11 23:33, son içerik 16.11 00:19; düzeltme sonrası kol b jürisi yeniden koşar (J2-OZET §4 Sıra 6) |
| AB-2 kapı sınıf listesi | kapı eksiği | §4: 3 zaman üst verisi dosyası; kapı betiği D'de |
| Süre 32,10 sn > hedef 22–26 | sınır içinde | ≤ 35 tutar; yeni c4 eski cümleden 2,79 sn uzun (kol a ile aynı ses). Kısaltma yeni ses ister: şef kararı |
| Rozet 26 px < 28 px (`hyperframes check` uyarısı) | şef kararı | huni §2 değeri; ST-2 kural çakışması (KBJ ST-2 notu) |
| Yorum satırlarında kol a `t_bas` (18,78 / 24,12) | dokunulmadı | 02/03/08 kaynakları iki kolda bayt aynı kalmalı (AB-3); kod değeri veriden türer (`KAYMA`) |
| `senaryo.json` `meta.kimlik` = `02-04-ydt-temel-s3` | dokunulmadı | ders grubu kimliği; AB-8 `kimlik` alanını saymaz (KBC açık nokta 8) |
| `BRIEF-S3.md` kol a planı | dokunulmadı | KBC açık nokta 8; DUZ2 notu ve kart metni güncel |

## 6. Değişen dosyalar

Kol b paketi git'te izsiz (`??`, şef commit atar). DUZ2'de değişen: `senaryo.json`, `sureler.json`, `sozcukler.json`, `baslar.json`,
`altyazi.json`, `METIN.md`, `sentez.wav.rapor.json`, ses türevleri (`cumle-4.wav`, `anlatim.*`, `sentez.wav`), `ortak/kunye.js`, `BRIEF-S3.md`,
3 açıklama, `zaman.json`, `surumler.json` (`ad` "S3b Shorts (32,10 sn)", `revizyonlar` r1), 8 sahnenin `uret.py` / `yardim.py` / `SPEC.md` /
`index.html` / `zamanlar.json` (kol a ile aynı kaynak; 01 kol b'ye özgü), bütün `sahneler/*/k/` kareleri, kök `kapak-a.png` / `kapak.png`.
Yeni tutanak: `kapi-duz2.{txt,json}`, `kapi-duz2-r2.{txt,json}`, `hf-check-duz2.txt`, `huni-kapi-duz2.txt`, `diff-rq-duz2.txt`,
`siniflama-duz2.txt`, `diff-rq-duz2-r2.txt`, `siniflama-duz2-r2.txt`, bu dosya.

Silinecekler: `~/Silinecekler/2026-11-15-duz2-0204S3/02-04-ydt-temel-s3b/` (kol a kopya kareleri, eski kol b kareleri, kol a mutlak yollu
`.hyperframes` durumları; LISTE satır 20).

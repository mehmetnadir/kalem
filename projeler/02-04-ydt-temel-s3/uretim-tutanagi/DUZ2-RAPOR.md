# DUZ2-RAPOR — 02-04-ydt-temel-s3 (kol a) · J2 özeti A sınıfı düzeltmeleri · 15–16.11.2026

İstem: `uretim-hatti/istemler/DUZ2-0204S3.md`. Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` §3A, §4.1, §4.2 satır T3;
`uretim-tutanagi/juri/J2-hukum.md`. Kol b raporu: `../02-04-ydt-temel-s3b/uretim-tutanagi/DUZ2-RAPOR.md`.

| Kalem | Sonuç |
|---|---|
| Düzeltilen kusur | A1/TD-1 (J2 EK-6 rozet) · A3 (J2 EK-5b) · A5 (J2 DK-1 + DK-2 TR kısmı) · KBJ EK-7 (sahne 08, iki kolda ortak) |
| Yeniden sentezlenen cümle | 1 (c3, iki parça; kol b c4 bu sesin kopyası) |
| Süre (anlatım) | 28,31 → **31,10 sn** (≤ 35; hedef 22–26 aşıldı, §6) |
| İlk söz · kanca | 1,00 sn (`The`) · kanca sahnesi 0,00–3,00 sn (değişmedi) · bilgi: kanca cümlesi bitişi 6,45 sn (`baslar.json`, değişmedi) |
| Whisper en düşük | 0,98 (c2 öğrenci sorusu, değişmedi); yeni c3 parçaları 1,00 / 1,00 |
| Çakışma kapısı | çıkış **0** (4 sahne, 129 örnek; arıza sonrası r2 16.11 00:43 yine 0) |
| `huni-kapi.mjs` | çıkış 1 yalnız JR-1b (jüri dosyası düzeltmeden eski; J2 yeniden koşacak) · 16 GEÇTİ (§7) |
| `hyperframes check` | 4 sahne çıkış 0, 0 hata (uyarılar §3) |
| diff beklenmeyen | **0** (sınıflama kol b `uretim-tutanagi/siniflama-duz2-r2.txt`) |
| mp4 | yok (istem) |

## 1. Düzeltmeler (kusur başına satır)

| Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|
| A1/TD-1 rozet (EK-6) | `ortak/anlatim/senaryo.json` `giris.rozetler`, `BRIEF-S3.md`, `ortak/kunye.js`, sahne 01–08 `uret.py` / `yardim.py` | `YDT · BASIC` → `YDT · TEMEL` | kod dosyalarında `grep -rln BASIC` (py, js, json, html, sh) = 0; bütün kareler rozet `YDT · TEMEL` |
| A3 ses c3 (öğretmen) | `ortak/anlatim/senaryo.json` c3 | "Planı bir kişi yapar. Tren tarifeye uyar: geniş zaman." → "Biletimi aldım, saat belli: kesin düzenleme, şimdiki zaman." + "Tren tarifeye uyar: geniş zaman." | `cumle-3.wav` sha256 `74cb0c729581…`; Whisper 1,00 / 1,00 (`sentez.wav.rapor.json`) |
| A3 kaydet kartı | `sahneler/08-hyperframes-kaydet/uret.py`, `yardim.py` | "Tarife → leaves, plan → am going." → 2 satır "Tarife → leaves," / "kesin düzenleme → am going." (64 px, sol x 96; karttaki tren/bilet simgesi kalktı, satır 2 sığsın diye) | `k/08-…-19.88.png`, `-23.6.png`, `k/koyu/…` |
| A3 kapak A | `sahneler/01-hyperframes-kapak/uret.py` (+ `proje-ka`, `proje-ka-koyu`) | başlık 2 `≠ PLAN` → `≠ DÜZENLEME` (hap kendi boyuna sığar, B2 131 px) | `kapak-a.png` = `kapak.png`; `sahneler/01-…/k/koyu/kapak-a-koyu.png` |
| A3 hikâye A | `sahneler/04-hyperframes-hikaye/uret.py` | başlık `≠ PLAN`, kart "plan → am going." → `≠ DÜZENLEME`, kart "kesin düzenleme → am going." (64 px, simge kalktı) | `hikaye-a.png` = `hikaye.png`; `sahneler/04-…/k/hikaye-a-koyu.png` |
| A3 hikâye B (terim aynılığı) | `sahneler/07-hyperframes-hikaye-b/uret.py` | soru "Tarife mi, plan mı?", şık `PLAN` → "Tarife mi, düzenleme mi?", şık `DÜZENLEME` (şıklar 64 px, yeniden orantılı) | `hikaye-b.png`; `sahneler/07-…/k/koyu/hikaye-b-koyu.png`. İlk çekim (şık `plan`) Silinecekler'de |
| A3 sahne 02 etiketleri | `sahneler/02-hyperframes-ornek/uret.py` | `person → plan`, `train → timetable` → tek etiket `kesin düzenleme`, `tarife` (seste geçen terim, ikincil renk) | `k/02-…-14.6.png`, `-18.6.png` |
| A3 açıklama | `aciklama-a.md` (= `aciklama.md`), `aciklama-b.md` | başlık A "Tarife geniş zaman, plan şimdiki zaman" → "Tarife geniş zaman, kesin düzenleme şimdiki zaman"; gövde cümleleri "kesin düzenleme" | `grep -n düzenleme aciklama*.md` |
| A3 senaryo üst bilgisi | `senaryo.json` `giris.satir2`, `meta.kapak.satir2`, `meta.kapak.canAlici`, `amaclar[2]`, `canAlici[0]`, `canAlici[2]` | `≠ PLAN`, "plan", "planlanmış gelecek" → `≠ DÜZENLEME`, "kesin düzenleme" | `git diff` |
| A3 BRIEF | `BRIEF-S3.md` | DUZ2 notu, cümle 3, kapak A başlığı, sahne tablosu, süre 31,10 | `git diff` |
| A5 karaoke (DK-1) | `sahneler/02-hyperframes-ornek/uret.py` | tek `fill` düz altyazı → sözcük başına `tspan`, ikincil → mürekkep, sözcüğün `t0` anında (sahne 03 ile aynı mekanizma) | `k/02-…-13.png`, `-14.6.png`, `-16.6.png`: sözcük dolgusu sesle |
| A5 TR soru tek yerde (DK-2 TR kısmı) | `sahneler/02-hyperframes-ornek/uret.py` | TR soru balonda + altyazıda (EN boyunda) → TR soru yalnız altyazıda (karaoke, ikincil renkten başlar); balonda yalnız `?`, sonra EN `-ing?` | `k/02-…-9.5.png`, `-11.2.png` |
| Aynı mekanizma | `sahneler/08-hyperframes-kaydet/uret.py`, `yardim.py` | 08 altyazı karaokesi 03/02 ile aynı `tspan` + `tl.set(fill)` koduna alındı | `k/08-…-19.88.png`, `-21.88.png` |
| KBJ EK-7 (kol b hükmü; sahne iki kolda bayt aynı) | `sahneler/08-hyperframes-kaydet/uret.py` | `leaves` hapı 0,20 sn çapraz geçiş, koyu temada hap yazısı soluk hap üstünde 2,1:1 → hap yazısı ve hap virgülü anında söner, mürekkep `leaves,` anında gelir, yalnız hap zemini 0,10 sn'de söner; hap mürekkebin altında | `k/koyu/08-…-22.35.png` geçiş karesi: açık mürekkep / sönen hap 7,1:1; `-22.38.png` 13,4:1 |
| AB-3 için kod kayması | sahne 02, 08, 03 `uret.py` | sabit cümle numarası ve `t_bas` → ilk `The` sözcüğünden türeyen kayma (`KAYMA`, `DT`); iki kolda kod bayt aynı | `cmp` kol a ↔ kol b: 02, 08 `uret.py` + `index.html` eşit |
| Yan etki onarımı | `sahneler/04-…`, `06-…`, `07-…/RAPOR.md` satır 3 | türev koşusu (`ortak/tema.sh`) satırı `Tema: acik` yaptı → HEAD değeri geri yazıldı | `git diff --stat` bu üç dosyada 0 |

Cümle 3 dil denetimi (şef kararı "kendin denetle"): özetin örneği "Biletini aldın, saati belli: şimdiki zaman." kart terimini taşımıyordu. Seçilen cümle:

- Birinci tekil şahıs ("Biletimi aldım") ekrandaki "I am going…" cümlesiyle aynı kişidir.
- "saat belli" yüklemli kısa yargıdır; "saati belli" tamlama ister ve özne belirsiz kalır.
- "kesin düzenleme" kartla, kapak A ile, hikâye A ile ve açıklamayla aynı terimdir (A3 "kartla aynı terim").
- İkinci yarı ("Tren tarifeye uyar: geniş zaman.") değişmedi. Ses iki parçaya ayrıldı; iki parça da Whisper 1,00.

## 2. Ses, süre, Whisper

| Cümle | Metin | sha256 (12) | Whisper | Durum |
|---|---|---|---|---|
| c1 (EN) | The train to İzmir leaves at 7 pm today. · I am going to the movie theater tonight. | `af9343e6d690` | 1,00 · 1,00 | değişmedi |
| c2 (öğrenci) | Hocam, tren de plana göre kalkmıyor mu? Neden -ing yok? | `a65bb1e43a13` | 0,98 | değişmedi |
| c3 (öğretmen) | Biletimi aldım, saat belli: kesin düzenleme, şimdiki zaman. · Tren tarifeye uyar: geniş zaman. | `74cb0c729581` | 1,00 · 1,00 | **yeni** |
| c4 | Bu, üç farktan yalnız biri. · Bir arkadaşına gönder; o da karıştırıyor. | `9b7e70ce36dc` | 1,00 · 1,00 | değişmedi |
| c5 | Bu sadece başlangıç. · Dersin tamamı YDS Publishing YouTube kanalında. | `6a9927c66d00` | 1,00 · 1,00 | değişmedi |

Zincir: `araclar/ses-sunucu.sh --kok K 02-04-ydt-temel-s3` (el.py, değişmeyen parça önbellekten) → `sozcuk_uret.py` → `zaman_uret.py` →
`kur.py` → `araclar/ses-paketle.py --yaz` → `araclar/altyazi_uret.py` → `metin_uret.py`.

| Ölçü (sn) | Önce (HEAD) | Sonra |
|---|---|---|
| Anlatım | 28,31 | 31,10 |
| İlk söz | 1,00 | 1,00 |
| Kanca (sahne 01) | 0,00–3,00 | 0,00–3,00 |
| Sahne 02 (değer) | 3,00–15,99 (12,99) | 3,00–18,78 (15,78) |
| Sahne 08 (kaydet) `t_bas` | 15,99 | 18,78 |
| Sahne 03 (çağrı) `t_bas` | 21,33 | 24,12 |
| Son kare (03 bitişi) | 29,30 | 32,09 |

## 3. Kareler ve kapı

Kareleri ben çektim ve baktım (mp4 yok; `ONIZLE_YALNIZ=1 calistir.sh` + `hyperframes snapshot`). Eski v2 kareleri Silinecekler'de (LISTE satır 19).

| Sahne | Açık kareler (küresel sn) | Koyu kareler |
|---|---|---|
| 01 kanca | 0 · 0,6 · 1,2 · 1,97 · 2,45 · 2,97 | 0 · 1,97 · `kapak-a-koyu.png` |
| 02 değer | 3 · 4,2 · 6,6 · 9,5 · 11,2 · 13 · 14,6 · 16,6 · 18,6 | 9,5 · 16,6 |
| 08 kaydet | 18,78 · 19,88 · 21,88 · 23,6 · 24,1 | 19,88 · 22,35 · 22,38 · 23,6 |
| 03 çağrı | 24,12 · 25,5 · 27 · 28,6 · 31,07 | 27 · 31,07 |
| Türevler | `kapak-a/b/c.png`, `hikaye-a/b.png` (+ `kapak.png`, `hikaye.png` kopya) | `kapak-a-koyu`, `kapak-b-koyu`, `kapak-c-koyu`, `hikaye-a-koyu`, `hikaye-b-koyu` |

Bakış sonucu: taşma yok, yazı × çizim çakışması yok, rozet her karede `YDT · TEMEL`, karakter değişmedi, altyazı karaokesi sesle aynı anda,
kart satır 2 çerçevenin içinde, koyu temada okunmayan yazı yok (08 geçiş karesi dahil).

| Kapı | Komut | Çıkış |
|---|---|---|
| Çakışma | `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s3/uretim-tutanagi/kapi-duz2.json` | **0** (`kapi-duz2.txt`) |
| HyperFrames | `hyperframes check sahneler/<01|02|08|03>/proje` | 0 (×4), 0 hata (`hf-check-duz2.txt`) |
| HV-13 kart sabitliği | 08 kare çifti 19,88 ↔ 21,88; kart bölgesi x 60–960, y 558–902 | piksel farkı 0 (fark kutusu yalnız y 971–1495: Gönder/Kaydet satırları) |
| AB-3 | kol a ↔ kol b 02/08/03 kareleri (+1,00 sn) | 27 / 27 çift piksel eşit |

`hyperframes check` uyarıları: rozet `YDT · TEMEL` 26 px < 28 px taban (huni §2 değeri; KBJ ST-2 kural çakışması, şef kararı);
`line_unread` uyarıları tek sahne koşusunun sahne sınırı uyarılarıdır (sonraki sahne aynı satırı sürdürür). Türev sahneleri (04–07)
`zaman.json` dışındadır; çakışma kapısı onları ölçmez, ben kareye baktım.

## 4. diff sınıflaması (kol a ↔ kol b)

`diff -rq 02-04-ydt-temel-s3 02-04-ydt-temel-s3b`: çıktı ve sınıflama kol b `uretim-tutanagi/diff-rq-duz2-r2.txt`, `siniflama-duz2-r2.txt` (arıza sonrası, 196 satır; ilk koşu `diff-rq-duz2.txt`, 190 satır).
Beklenmeyen 0. Sınıf sayıları kol b raporu §3'te.

## 5. Değişen dosyalar

`git diff --name-only` 60 izli dosya (BRIEF, 3 açıklama, `ortak/anlatim` 7 dosya, `ortak/kunye.js`, 8 sahnenin `uret.py` / `yardim.py` /
`SPEC.md` / `index.html` / `nesneler.json` / `zamanlar.json` / `calistir.sh`, `surumler.json`, `zaman.json`). Git dışı türev: `*.wav`, `*.m4a`,
kök `*.png`, `sahneler/*/k/` (`.gitignore` 27, 32, 36, 38). Yeni tutanak: `kapi-duz2.{txt,json}`, `kapi-duz2-r2.{txt,json}` (arıza sonrası), `hf-check-duz2.txt`, `huni-kapi-duz2.txt`, bu dosya.
`surumler.json`: `ad` "S3 Shorts (31,10 sn)", `revizyonlar` r1 (s2 paketiyle aynı alan düzeni).

## 6. Düzeltilmeyen maddeler ve sebebi

| Madde | Sebep |
|---|---|
| B2 HV-19, B3 KS-3, B4 KS-4, B5 KS-5, B6 DK-2 satır uzunluğu, B7 ST-1 vinyet | J2 B sınıfı (ölçüt hatası); istem "B sınıfına dokunma" |
| C1 HV-22, C2 HV-13 | C sınıfı; bu turda kanıt yine de çıktı: kapı çıktısı `kapi-duz2.txt` (künye kapıdan önce değişti), HV-13 piksel çifti §3 |
| C3 KS-6 (168 px), C5 EK-8 (v2 kontak) | C sınıfı, istem kapsamı A. Not: `magick` bu makinede bozuk (`libwebp.so.6` yok); montajı PIL ile yaptım |
| C4 EK-4 | şefin işi (adresin gidiş zamanı) |
| c2 "tren de plana göre kalkmıyor mu?" | öğrencinin yanlış anlaması; soru bilerek "plan" der. Ses değişmedi |
| Süre 31,10 sn > hedef 22–26; sahne 02 15,78 sn > huni §3 rehberi 15 sn | yeni c3 eski cümleden 2,79 sn uzun; ≤ 35 sınırı tutar. Kısaltma yeni ses ister: şef kararı |
| `surumler.json` `video.amaclar[2]` "planlanmış gelecek" | ana ders tanımı; J2 §4.2 ana paket satırı "şef kararı". Ana ders 02-04 aynı genellemeyi taşır (geri besleme) |
| Sahne `RAPOR.md`, `uretim-tutanagi/istem/*`, taslak belgelerinde `BASIC` / "plan" anışı | tarihli belge; değiştirmedim. Güncel durum SPEC DUZ2 notlarında |

Silinecekler: `~/Silinecekler/2026-11-15-duz2-0204S3/02-04-ydt-temel-s3/` (eski kareler, hikâye B ilk çekimi; LISTE satır 19 ve son satır).

## 7. Arıza sonrası yeniden doğrulama (16.11.2026)

İş 16.11'de makine bellek arızasıyla kesildi. Kol a'nın bütün düzeltmeleri ve bu raporun §1–§6'sı arızadan önce bitmişti; yarım iş
yinelenmedi. Arızadan sonra şunları yeniden ölçtüm:

| Ölçüm | Komut / yöntem | Sonuç |
|---|---|---|
| Kapıdan sonra değişen içerik | `find <paket> -newer uretim-tutanagi/kapi-duz2.txt` | yalnız `.hyperframes` check durumu, 08 `SPEC.md`, `surumler.json` (içerik değil) |
| Kare tazeliği | kare ↔ `proje/index.html` zaman karşılaştırması | açık kareler `index.html`'den yeni; koyu kareler tema betiğinin koyu geçişinde çekildi |
| Çakışma kapısı (r2) | `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s3/uretim-tutanagi/kapi-duz2-r2.json` | **çıkış 0** (`kapi-duz2-r2.txt`; 4 sahne, 129 örnek) |
| Huni kapısı | (D) `node araclar/huni-kapi.mjs K/projeler/02-04-ydt-temel-s3` | çıkış 1: yalnız JR-1b (J2 hükmü 15.11 22:56, son içerik 16.11 00:19; J2-OZET §4 Sıra 6). HV-11 31,1 sn · HV-12 ilk söz 1 sn, kanca sahnesi 3 sn · HV-20 teslim tam · HV-24 `BASIC` yok (34 dosya) GEÇTİ (`huni-kapi-duz2.txt`) |
| Rozet | `grep -rln BASIC` (js, html, json, py, sh; `.hyperframes` hariç) | 0 dosya |
| Ses | `sha256sum cumle-*.wav`; `sentez.wav.rapor.json` | c3 `74cb0c729581`; Whisper en düşük 0,98 (c2), öteki 8 parça 1,00 |
| HV-13 | 08 çifti 19,88 ↔ 21,88, kart bölgesi x 60–960, y 558–902 | 0 px |
| AB-3 | kol a 02/08/03 kareleri ↔ kol b +1,00 sn | 27 / 27 piksel eşit |
| Kareler | PIL kontak sayfası: 01 (6 + 3 koyu), türevler (kapak A/B/C, hikâye A/B, 5 koyu), `≠ DÜZENLEME` tam çözünürlük kırpımı; 02/08/03 kol b kareleriyle piksel eşit, onlara baktım | taşma, çakışma, okunmayan yazı yok; rozet `YDT · TEMEL`; karakter değişmedi |

A3 terim gerekçesi (öneriden sapma): J2 önerisi açıklama başlığında "Tarife geniş zaman, düzenleme şimdiki zaman" der. Başlıkta
"kesin düzenleme" kullandım. Sebep: şef kararı kart, kapak, hikâye ve açıklamanın sesle aynı terimi taşımasını ister; seste ve kartta terim
"kesin düzenleme"dir. Yalın "düzenleme" kapsamı yeniden genişletir (her düzenleme şimdiki zaman almaz; A3'ün kusuru buydu). Kapak A ve
hikâye A başlığı `TARİFE` / `≠ DÜZENLEME` 2–4 sözcük sınırı (HV-20b) için kısa kaldı; aynı karede kart "kesin düzenleme → am going."
terimi tamamlar. Hikâye B şıkkı `DÜZENLEME` aynı sebeple kısadır; soru "Tarife mi, düzenleme mi?" ve altındaki kural satırı tarifeyi verir.

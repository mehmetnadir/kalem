# S3 Shorts — "TARİFE ≠ PLAN" (02-04-ydt-temel-s3, YDT TEMEL)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 26.56 sn, anlatım 26.56 sn hazır) + `kontrol.png` + kapak 3 sürüm (`kapak-a.png` = `kapak.png`,
`kapak-b.png`, `kapak-c.png`) + hikâye karesi 2 sürüm (`hikaye-a.png` = `hikaye.png`, `hikaye-b.png`). Açıklama 2 set: `aciklama-a.md`
(= `aciklama.md`), `aciklama-b.md`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../02-04-ydt-temel/BRIEF.md` ile aynı; dikey v2 ölçekleri
`../present-continuous-dikey/BRIEF-DIKEY.md` §2–§3 (HUD, ders adı 56, rozet 36, ≥ 64 px yazı). Kaynaklar: ses `ortak/anlatim/`
(cümle başları 1,00 · 7,00 · 11,51 · 16,54; toplam 26.56), senaryo `ortak/anlatim/senaryo.json`
(kaynak: `uretim-tutanagi/senaryo-taslak.md`, jüri düzeltmeleri `uretim-tutanagi/S3-duzeltme.md`). `ortak/kunye.js` = S1 kopyası
(ders adı 2 satır `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`, tek rozet `YDT · BASIC`); çip sağ üst `KUNYE.cipler[<klasör>]`.
Biçim emsali (aynı dersin bitmiş kısası, 7 sahnesi yazılı): `../02-04-ydt-temel-s1/`.

Kapak A başlığı (2 satır, 2 sözcük): `TARİFE` / `≠ PLAN`. Can alıcı: `canAlici[1]` + `[2]` kısa kodu `tarife → leaves · plan → am going`.
Sesler: öğretmen Atakan (`gsJ9nrlXYbPztJxC4fwc`), öğrenci Gökçe Deniz (`oPC5I9GKjMReiaM29gjY`). Figür sesle eşleşir (K22):
öğretmen erkek (`kadro.ogretmen`: ShirtPantsWB / Smile / Short), öğrenci kadın genç (`kadro.ogrenci`: Sitting / Smile / LongBangs /
GlassRound; `ogrenci-bas.svg`). Soru anı 1 (cümle 2, öğrenci); sonra 0,75 sn duraklama, cevap 0,75 sn sonra.

## Dikey yerleşim (px) — dikey v2 bantları
Yerleşim ve ölçek: ../present-continuous-s1/BRIEF-S1.md '05.11 düzeltme' bölümü +
../present-continuous-dikey/BRIEF-DIKEY.md §2–§3
(tek kaynak, 05.11 karar 6b). HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 · platform 1536–1920 BOŞ.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0.00–3.00 | 102 |
| 02 | 02-hyperframes-ornek | HyperFrames | 3.00–15.99 | 402 |
| 03 | 03-hyperframes-cta | HyperFrames | 15.99–26.56 | 347 |
| — | 04-hyperframes-hikaye | HyperFrames | zaman çizelgesi dışı | 1 (`hikaye-a.png` + kopya `hikaye.png`) |
| — | 05-hyperframes-kapak-b | HyperFrames | zaman çizelgesi dışı | 1 (`kapak-b.png`) |
| — | 06-hyperframes-kapak-c | HyperFrames | zaman çizelgesi dışı | 1 (`kapak-c.png`) |
| — | 07-hyperframes-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 (`hikaye-b.png`) |

Sahne sınırı = bir sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn. Sahne 01 → 02 sınırı 3,00 (K23 giriş ≤ 3 sn).
Durağan kareler `zaman.json` → `hikaye` (A) ve `duragan` (kapak B, kapak C, hikâye B) alanlarındadır, `sahneler[]` dışında:
`birlestir.py` ve `kur.py` yalnız `sahneler[]` okur, `cikti.mp4`'e girmez (S1 biçimi).

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
Zaman sözcük çapasından okunur (`ortak/anlatim/sozcukler.json`), sabit saniyeden değil.

| sn | Hareket |
|---|---|
| 0,00 | Kapak A tam görünür (ilk kare = kapak): rozet `YDT · BASIC`; başlık `TARİFE` (952 px'e sığan en büyük boy, üst sınır 190 px) / `≠ PLAN` sarı hapta (dolgu `#ffe066`, yazı `#1b2440`); solda tren + saat (kollar yedide, rakamsız), etiket `leaves`; sağda elinde sinema bileti tutan öğretmen figürü, etiket `am going` (Caveat ≥ 72). `≠` glifi Fredoka'da yoksa kalemle çizilir |
| 0,30–0,80 | `TARİFE` altına sarı el altçizgisi (`alti`) |
| 1,00–2,12 | Kart 1 satır 1 `The train to İzmir` sözcük zamanlı (`The` 1,00 · `train` 1,28 · `to` 1,48 · `Izmir` 1,64) |
| 2,0–3,0 | Uçuş: başlık üst bant ders adına, figür solar; tren ikonu küçülüp kart 1 köşesine iner |
| 2,20–2,92 | Kart 1 satır 2 `leaves at 7` (`leaves` 2,20 · `at` 2,56 · `7` = *seven* 2,80–2,92); 3,00'ten önce duyulan her sözcük sahne 01'de görünür |
| 3,00–4,20 | Sahne 02: kart 1 sürer; `pm` (= *p.m.* 3,00) · `today.` (3,40). `today.` çapasında zaman çizgisi: now noktası → `7 pm` çentiğine kalem oku; `7 pm` sarı daire (`isaret`); nokta altına etiket `gelecek · V-s` |
| 4,45–6,53 | Kart 2 `I am going to the` / `movie theater tonight.` sözcük zamanlı (`I` 4,45 · `am` 4,61 · `going` 4,81 · `movie` 5,29 · `tonight.` 5,93); `tonight.` çapasında çizgide now'ın sağına `tonight` noktası, etiket `gelecek · am + V-ing`; bilet ikonu kart 2 köşesinde küçük. `leaves` ve `am going` henüz vurgusuz |
| 7,00–10,84 | Soru anı: balon (`ogrenci-bas.svg`, `hw-text-cloud`) kart sütununun altına girer, kartlar üstte küçülür. Balon `Hocam, tren de plana` / `göre kalkmıyor mu?` / `Neden -ing yok?` sözcük zamanlı (`Hocam,` 7,00 · `kalkmıyor` 8,72 · `Neden` 9,72 · `-ing` 10,08 · `yok?` 10,33). `Neden` çapasında sarı nokta: balon → kart 1 `leaves` |
| 10,76–11,51 | Duraklama 0,75 sn (öğrenciden sonra); balon durur |
| 11,51–13,19 | Balon solar, öğretmen figürü girer (ayakta, işaret pozu). `Planı` (11,51) çapasında `bag`: figür → `am going`, `am going` `odak`; kart 2 altında etiket `person → plan` |
| 13,43–15,99 | `Tren` (13,43) çapasında `bag`: tren ikonu → `leaves`; kart 1 altında etiket `train → timetable` (`tarifeye` 13,83); `geniş` (15,19) çapasında `leaves` `odak` (sarı). `zaman.` 15,47 |
| 15,99–18,62 | Sahne 03 (CTA, S1 sahne 03 düzeni; aynı ses dosyası, S1'e göre −4,00 sn): `üç farktan biri` Lexend (`üç` 17,02) |
| 18,77–22,85 | `Tam ders:` Caveat (`Tam` 18,77) · ders bandı Fredoka `Simple Present` (`Simple` 19,97) / `vs Present Continuous` (`vs` = `ve` çapası 20,77; `Present` 21,25) |
| 23,00–25,64 | `üç farkın hepsi` Lexend (`Üç` 23,00) · saat (clock) + `dört buçuk dakikada` (`dört` 24,36 · `dakikada.` 24,84) · `@ydspublishing` sarı hap (dolgu `#ffe066`, yazı `#1b2440`) son sözle (`dakikada.` 24,84–25,64) |
| 25,56–26,56 | Durgun kuyruk; son karede tren ve bilet ikonu bandın iki yanında küçük → kapak A karesine döngü (kalıp §1 kural 5) |

Ekranda "İzmir" noktalı, seste "Izmir" (EN parça). Ekran `7 pm`, ses *seven p.m.* (rakam kuralı yalnız sesteki metinde; S3-B dil jürisi).
`@ydspublishing` sesle okunmaz. "kanal" sözü yok, QR yok, emoji yok. Satır ≤ 24 karakter (en uzun `movie theater tonight.` = 22).

## Kapak A (`kapak-a.png` + kopya `kapak.png`, 1080×1920)
Sahne 01'in uçuş öncesi karesi: t 1,97 (kare 59), tema açık, çip yok. `calistir.sh` render dalı `video.mp4`'ten `select=eq(n\,59)` ile
paket köküne `kapak-a.png` yazar ve aynı dosyayı `kapak.png` olarak kopyalar (S1 `01-hyperframes-kapak/calistir.sh` satır 38 kalıbı).
Karede: rozet, 2 satır başlık (`TARİFE` altçizgisi bitmiş), tren + saat, bilet tutan figür, etiketler `leaves` / `am going`, kart 1 satır 1
`The train to İzmir`, altyazı bandında cümle 1'in ilk dilimi. Logo sol alt y ≈ 1478. Tarif: `uretim-tutanagi/kapak-taslak.md` §2 (A).

## Kapak B ve C (durağan, videoya girmez)
Tarif: `uretim-tutanagi/kapak-taslak.md` §1–§3. Ortak: zemin açık, rozet `YDT · BASIC`, 2 satır başlık (952 px'e sığan en büyük boy, üst
sınır 190 px), logo sol alt, 1344–1536 boş, 1536–1920 boş. Kart yazısı Fredoka 72.

| Sürüm | Klasör → çıktı | Başlık | Sahne (864–1344) | Can alıcı |
|---|---|---|---|---|
| B (soru) | `05-hyperframes-kapak-b` → `kapak-b.png` | `NEDEN -ING` / `YOK?` (sarı hap) | ortada tren + saat; üstünde el çizimi sarı `?`; altında kart `The train leaves …`, `leaves` altında sarı altçizgi; sağda öğretmen figürü trene işaret eder | `canAlici[1]`, kısa kod `leaves` |
| C (karşıt çift) | `06-hyperframes-kapak-c` → `kapak-c.png` | `İKİ ÖRNEK` / `İKİ ZAMAN` (sarı hap) | iki kart üst üste, aynı boy: `The train leaves …` (solda tren ikonu) / `I am going …` (solda bilet ikonu); tek vurgu `leaves` sarı hapta; sağ altta küçük öğretmen figürü | `canAlici[1]` + `[2]` |

`-ING` Latin büyük I; `İKİ`, `TARİFE` Türkçe İ. Başlık elle büyük harf yazılır; `text-transform` yok.

## Hikâye karesi A (`hikaye-a.png` + kopya `hikaye.png`, 1080×1920)
Anlatımdan bağımsız durağan kare; ses yok; süre yazmaz. Sahne `04-hyperframes-hikaye` tek kare üretir, paket köküne `hikaye-a.png`
(açık) yazar ve `hikaye.png` olarak kopyalar. Tarif: `uretim-tutanagi/hikaye-taslak.md` §2.

| Bant (y px) | Metin |
|---|---|
| 0–288 HUD | rozet `YDT · BASIC` · ders adı `Simple Present vs Present Continuous` (2 satır, 56 px) |
| 300–420 | `İkisi geleceği anlatıyor` (Lexend 64) |
| 440–700 | `TARİFE` / `≠ PLAN` (Fredoka; `≠ PLAN` sarı hapta; 952 px'e sığan en büyük boy) |
| 720–1180 | kart 1 `The train leaves …` · etiket `train → timetable` · tren + saat ikonu · kart 2 `I am going …` · etiket `person → plan` · bilet ikonu; `leaves` ve `am going` sarı altçizgi |
| 1190–1300 | `Tren tarifeye uyar` (Lexend 64) |
| 1344–1536 | `Tam ders:` / `profildeki bağlantı` (Caveat 72) · `@ydspublishing` sarı hap · logo sol alt y ≈ 1478 |
| 1536–1920 | boş (platform arayüzü) |

## Hikâye karesi B (`hikaye-b.png`, 1080×1920)
Sahne `07-hyperframes-hikaye-b` tek kare. Tarif: `uretim-tutanagi/hikaye-taslak.md` §3. Cevap (karede yazmaz): A — TARİFE.

| Bant (y px) | Metin |
|---|---|
| 0–288 HUD | A ile aynı |
| 300–420 | `Tarife mi, plan mı?` (Fredoka 96) |
| 440–800 | cümle kartı `The train to İzmir` / `leaves at 7 pm today.` (Fredoka 64) · tren + saat ikonu; vurgu yok |
| 820–1180 | şıklar yan yana: `A` `TARİFE` · `B` `PLAN` (harf rozeti mürekkep çerçeve, sarı değil; Fredoka 72; iki şık aynı biçim) |
| 1190–1300 | boş |
| 1344–1536 | `Cevap tam derste:` / `profildeki bağlantı` (Caveat 72) · `@ydspublishing` sarı hap · logo sol alt |
| 1536–1920 | boş |

## Çalıştırma
Her zaman çizelgesi sahnesi `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/02-04-ydt-temel-s3 --tema acik --gecis BookFlip --efekt hisirti`.
Durağan kareler ayrı (birleştirmeye girmez): `sahneler/04-hyperframes-hikaye/calistir.sh --tema acik` → `hikaye-a.png` + `hikaye.png` ·
`05-hyperframes-kapak-b` → `kapak-b.png` · `06-hyperframes-kapak-c` → `kapak-c.png` · `07-hyperframes-hikaye-b` → `hikaye-b.png`.
Ses yeniden kurulumu (sentez yok): `ortak/anlatim/` içinde `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`araclar/ses-paketle.py --yaz --paket 02-04-ydt-temel-s3` → `araclar/altyazi_uret.py projeler/02-04-ydt-temel-s3` → `metin_uret.py`.
Sahne istemleri: `uretim-tutanagi/istem/sahne/D-<klasör>.md` (şablon `D-s3-sablon.md`).

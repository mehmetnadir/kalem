# S3 Shorts — "TARİFE ≠ DÜZENLEME" (02-04-ydt-temel-s3, YDT TEMEL) · huni v2

> DUZ2 (15.11, J2-OZET §4.2 T3): cümle 3 → "Biletimi aldım, saat belli: kesin düzenleme, şimdiki zaman. Tren tarifeye uyar:
> geniş zaman." (2 parça; eski "Planı bir kişi yapar." kapsamsızdı, A3). Kart `Tarife → leaves,` / `kesin düzenleme → am going.`
> (64 px, simgesiz), kapak A ve hikâye A başlığı `TARİFE` / `≠ DÜZENLEME`, sahne 02 etiketleri `kesin düzenleme` / `tarife`,
> sahne 02 karaoke + TR soru yalnız altyazıda (A5), rozet `YDT · TEMEL` (TD-1). Süre 28,31 → 31,10 sn. Aşağıdaki tablolarda
> eski zaman kalan satırlar için kaynak `zaman.json` + `ortak/anlatim/sozcukler.json`; rapor `uretim-tutanagi/DUZ2-RAPOR.md`.

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 31.10 sn, anlatım 31.10 sn hazır; mp4 şimdi üretilmez, standart §1 kural 9) + kapak 3 sürüm
(`kapak-a.png` = `kapak.png`, `kapak-b.png`, `kapak-c.png`) + hikâye karesi 2 sürüm (`hikaye-a.png` = `hikaye.png`, `hikaye-b.png`).
Açıklama 2 set: `aciklama-a.md` (= `aciklama.md`), `aciklama-b.md`.
BAĞLAYICI: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` (15.11). Bu belge yerleşimi ve yapıyı oradan alır; stil,
kalem darbesi, olay sesi kuralları `../02-04-ydt-temel/BRIEF.md` ile aynı. Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 7,00 ·
11,51 · 19,33 · 24,67; toplam 31.10), senaryo `ortak/anlatim/senaryo.json` (kaynak: `uretim-tutanagi/senaryo-taslak.md`, jüri düzeltmeleri
`uretim-tutanagi/S3-duzeltme.md`; v2 çevirisi `uretim-tutanagi/V2-C-RAPOR.md`). `ortak/kunye.js` ve sahnelerin `yardim.py` künyesi
v1 HUD'dur (logo 48–144, ders adı 212, çip); v2 kanal katmanını taşımaz → değerler aşağıdaki tablodan, her sahnede aynı.

Kapak A başlığı (2 satır, 2 sözcük): `TARİFE` / `≠ DÜZENLEME`. Can alıcı: `canAlici[1]` + `[2]` kısa kodu `tarife → leaves · kesin düzenleme → am going`.
Sesler: öğretmen Atakan (`gsJ9nrlXYbPztJxC4fwc`), öğrenci Gökçe Deniz (`oPC5I9GKjMReiaM29gjY`). Figür sesle eşleşir (K22):
öğretmen erkek (`kadro.ogretmen`: ShirtPantsWB / Smile / Short), öğrenci kadın genç (`kadro.ogrenci`: Sitting / Smile / LongBangs /
GlassRound; `ogrenci-bas.svg`). Öğrenci iki kez konuşur: soru anı (cümle 2) ve çağrı (cümle 5, standart §1 kural 2).

## Yerleşim (px) — huni v2 (standart §2), bütün sahnelerde aynı
| Bölge | y | Değer |
|---|---|---|
| Üst boş | 0–280 | yalnız zemin; v1 HUD (logo, 2 satır ders adı, çip) kalkar |
| Kanal katmanı (kimlik `kanal`) | 280–350 | tema logosu yükseklik 48, genişlik 193,5 (48 × 1920 / 476,3), resim x 53,2 (görünür sol kenar x 60), y 291–339 · `@ydspublishing` Lexend 700 42 px, `murekkep`, x 263, taban y 330 · ilk kareden son kareye opaklık 1, giriş/çıkış yok · `__kalemKutu` `kunye:kanal`. S1 ve S2 ile aynı piksel (`../02-04-ydt-temel-s1/BRIEF-S1.md`) |
| Künye | 360–450 | tek satır: `Simple Present vs Present Continuous` Fredoka 700, x 60, taban y 420, boy ≤ 34 (rozetle x 960'a sığan en büyük, alt sınır 28) · rozet hapı `YDT · TEMEL` Lexend 700 26 px, y 386–434, konu sonu + 20 (dolgu `vurguDolgu`, yazı `pilMetin`); çip yok |
| İçerik | 460–1380 | x 60–960; yazı ≥ 64 px (kanal ve künye hariç) |
| Altyazı + karaoke | 1400–1550 | x 60–960 (orta 510), en çok 2 satır, Lexend 500 44 (uzunda 40 → 36) |
| Alt boş | 1570–1920 | yalnız zemin; sağ şerit x 960–1080 içerik taşımaz |

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare | Ses |
|---|---|---|---|---|---|
| 1 Kanca | 01-hyperframes-kapak | HyperFrames | 0.00–3.00 | 102 | öğretmen |
| 2 Değer | 02-hyperframes-ornek | HyperFrames | 3.00–18.78 | 485 | öğretmen + öğrenci sorusu |
| 3 Kaydet | 08-hyperframes-kaydet (YENİ) | HyperFrames | 18.78–24.12 | 172 | öğretmen |
| 4 Çağrı | 03-hyperframes-cta | HyperFrames | 24.12–31.10 | 239 | öğrenci |
| — | 04-hyperframes-hikaye | HyperFrames | zaman çizelgesi dışı | 1 (`hikaye-a.png` + kopya `hikaye.png`) | — |
| — | 05-hyperframes-kapak-b | HyperFrames | zaman çizelgesi dışı | 1 (`kapak-b.png`) | — |
| — | 06-hyperframes-kapak-c | HyperFrames | zaman çizelgesi dışı | 1 (`kapak-c.png`) | — |
| — | 07-hyperframes-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 (`hikaye-b.png`) | — |

Sahne sınırı = bir sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn. Sahne 01 → 02 sınırı 3,00 (K23 giriş ≤ 3 sn).
Klasör adı sırayı belirlemez: `birlestir.py` sırayı `zaman.json` → `sahneler[]`'den okur (08, 03'ten önce çalar).
Durağan kareler `zaman.json` → `hikaye` (A) ve `duragan` (kapak B, kapak C, hikâye B) alanlarındadır, `sahneler[]` dışında.

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
Zaman sözcük çapasından okunur (`ortak/anlatim/sozcukler.json`), sabit saniyeden değil. Kanal katmanı her satırda ekranda.

| sn | Hareket |
|---|---|
| 0,00 | Kapak A tam görünür (ilk kare = kapak): künye bandında yalnız rozet (son konumunda); başlık `TARİFE` (900 px'e sığan en büyük boy, üst sınır 190 px) / `≠ DÜZENLEME` sarı hapta (DUZ2: kendi boyu B2 = 900 px'e sığan, 131 px; dolgu `#ffe066`, yazı `#1b2440`); solda tren + saat (kollar yedide, rakamsız), etiket `leaves`; sağda elinde sinema bileti tutan öğretmen figürü, etiket `am going` (Caveat ≥ 72). `≠` glifi Fredoka'da yoksa kalemle çizilir |
| 0,30–0,80 | `TARİFE` altına sarı el altçizgisi (`alti`) |
| 1,00–2,12 | Kart 1 satır 1 `The train to İzmir` sözcük zamanlı (`The` 1,00 · `train` 1,28 · `to` 1,48 · `Izmir` 1,64) |
| 2,0–3,0 | Uçuş: başlık künye bandına (360–450) ders adı olur, figür solar; tren ikonu küçülüp kart 1 köşesine iner |
| 2,20–2,92 | Kart 1 satır 2 `leaves at 7` (`leaves` 2,20 · `at` 2,56 · `7` = *seven* 2,80–2,92); 3,00'ten önce duyulan her sözcük sahne 01'de görünür |
| 3,00–4,20 | Sahne 02: kart 1 sürer; `pm` (= *p.m.* 3,00) · `today.` (3,40). `today.` çapasında zaman çizgisi: now noktası → `7 pm` çentiğine kalem oku; `7 pm` sarı daire (`isaret`); nokta altına etiket `gelecek · V-s` |
| 4,45–6,53 | Kart 2 `I am going to the` / `movie theater tonight.` sözcük zamanlı (`I` 4,45 · `am` 4,61 · `going` 4,81 · `movie` 5,29 · `tonight.` 5,93); `tonight.` çapasında çizgide now'ın sağına `tonight` noktası, etiket `gelecek · am + V-ing`; bilet ikonu kart 2 köşesinde küçük |
| 7,00–10,84 | Soru anı: balon (`ogrenci-bas.svg`, `hw-text-cloud`) kart sütununun altına girer, kartlar üstte küçülür. DUZ2: balonda yalnız EN `-ing?` (`?` "mu?" sözüyle, `-ing` "-ing" sözüyle); TR soru yalnız altyazıda, karaoke (eski: balon `Hocam, tren de plana` / `göre kalkmıyor mu?` / `Neden -ing yok?` sözcük zamanlı) (`Hocam,` 7,00 · `kalkmıyor` 8,72 · `Neden` 9,72 · `-ing` 10,08 · `yok?` 10,33). `Neden` çapasında sarı nokta: balon → kart 1 `leaves` |
| 10,76–11,51 | Duraklama 0,75 sn (öğrenciden sonra); balon durur |
| 11,51–15,91 | Balon solar, öğretmen figürü girer (ayakta, işaret pozu) `Biletimi` (11,51) çapasında. `kesin` (13,87) çapasında `bag`: figür → `am going`, `am going` `odak`; `düzenleme,` (14,15) çapasında kart 2 altında etiket `kesin düzenleme` (Caveat, ikincil) |
| 16,06–18,78 | `Tren` (16,06) çapasında `bag`: tren ikonu → `leaves`; `tarifeye` (16,46) çapasında kart 1 altında etiket `tarife` (Caveat, ikincil); `geniş` (17,90) çapasında `leaves` `odak` (sarı). `zaman.` 18,22 |
| 18,78–21,41 | Sahne 08 (kaydet): `Bu,` (19,33) çapasında kural özeti kartı kalemle çizilir, içinde tek cümle `Tarife → leaves,` / `kesin düzenleme → am going.` (Fredoka 64, sol x 96; `leaves` ve `am going` EN, tek sarı vurgu `leaves`); DUZ2: karttaki tren/bilet simgesi kalktı (satır 2 826 px). Kart `gönder;` (22,32) öncesi en az 2 sn sabit |
| 21,56–24,12 | `Bir` (21,56) çapasında kartın altında yer imi simgesi (SVG, kalemle çizilir, emoji değil) + `Kaydet` (Fredoka 72); `gönder;` (22,32) çapasında yer imi sarıyla dolar, `leaves` hapı mürekkep altçizgiye döner (aynı anda tek sarı). Kart kımıldamaz |
| 24,12–26,43 | Sahne 03 (çağrı, öğrenci sesi): ana dersin kapağı 16:9 kart (900×506, x 60–960, y 620–1126; `ortak/kapak/ana-kapak.png` / `ana-kapak-koyu.png`, temaya göre) sahne başında yumuşak girer; giriş sözü `Bu sadece başlangıç.` Fredoka 700 kartın üstünde (y 470–600), sözcük zamanlı (`Bu` 24,67 · `sadece` 24,91 · `başlangıç.` 25,47) |
| 26,58–30,10 | `@ydspublishing · YouTube` kartın altında (y 1160–1260; `@ydspublishing` sarı hap, `YouTube` mürekkep) `YDS` (27,86) çapasında gelir; `kanalında.` 29,38 |
| 30,10–31,10 | Durgun kuyruk; kapak kartı ve satırlar yerinde |

Ekranda "İzmir" noktalı, seste "Izmir" (EN parça). Ekran `7 pm`, ses *seven p.m.* (rakam kuralı yalnız sesteki metinde; S3-B dil jürisi).
`@ydspublishing` ekranda yazar; seste "YDS Publishing YouTube kanalında" (söyleniş `ses-sozluk.json` "YeDeSe"). Hiçbir yerde standart §1 kural 4–5 sözü
(eski çağrı kalıbı, süre sözü), QR, emoji, "izle" düğmesi taklidi yok. Satır ≤ 24 karakter.

## Kapak A (`kapak-a.png` + kopya `kapak.png`, 1080×1920)
Sahne 01'in uçuş öncesi kanca karesi: t 1,97 (kare 59), altyazı katmanı GİZLİ, kanal katmanı görünür. Yöntem S3-SON (`uretim-tutanagi/
S3-SON-RAPOR.md` "Kapak A yöntemi"): proje kopyasında yalnız CSS `#altyazi{display:none !important}` + `hyperframes snapshot --at 1.97`;
açık → paket kökü `kapak-a.png` + `kapak.png`; koyu → `sahneler/01-hyperframes-kapak/k/koyu/kapak-a-koyu.png`.

## Kapak B ve C (durağan, videoya girmez)
Ortak: kanal katmanı + künye bandında yalnız rozet; altyazı yok; 1400–1920 boş; başlık 2 satır (900 px'e sığan en büyük boy, üst sınır
170 px). Tarif temeli: `uretim-tutanagi/kapak-taslak.md` §1–§3.

| Sürüm | Klasör → çıktı | Başlık | Sahne (≈ 820–1380) | Can alıcı |
|---|---|---|---|---|
| B (soru) | `05-hyperframes-kapak-b` → `kapak-b.png` | `NEDEN -ING` / `YOK?` (sarı hap) | solda tren + saat, üstünde el çizimi sarı `?`; altında kart `The train leaves …`, `leaves` altında sarı altçizgi; sağda KARAKTER GÖRSELİ `ortak/kapak/karakter.png` (ana ders kopyası; öğrenci, "hangisi?" pozu), 10 px krem çıkartma kenarı, açık temada arkasında krem daire (`kapak-standardi.md`) | `canAlici[1]`, kısa kod `leaves` |
| C (karşıt çift) | `06-hyperframes-kapak-c` → `kapak-c.png` | `İKİ ÖRNEK` / `İKİ ZAMAN` (sarı hap) | iki kart üst üste, aynı boy: `The train leaves …` (solda tren ikonu) / `I am going …` (solda bilet ikonu); tek vurgu `leaves` sarı hapta; sağ altta küçük öğretmen figürü | `canAlici[1]` + `[2]` |

`-ING` Latin büyük I; `İKİ`, `TARİFE` Türkçe İ. Başlık elle büyük harf yazılır; `text-transform` yok.

## Hikâye karesi A (`hikaye-a.png` + kopya `hikaye.png`) — kural kartı düzeni
Durağan, ses yok, altyazı yok. Standart §6: kanal katmanı + kural özeti + "Kaydet"; y 1150–1380 yalnız boş zemin (bağ çıkartması; boş kutu çizilmez).

| Bant (y px) | İçerik |
|---|---|
| 280–450 | kanal katmanı + künye (tablo yukarıda) |
| 460–550 | `İkisi geleceği anlatıyor` (Lexend 64) |
| 570–830 | `TARİFE` / `≠ DÜZENLEME` (Fredoka; `≠ DÜZENLEME` sarı hapta; 900 px'e sığan, üst sınır 120 px) |
| 850–1040 | kural özeti kartı (sahne 08 ile aynı tek cümle): `Tarife → leaves,` / `kesin düzenleme → am going.` (64 px, sol x 96; DUZ2: simgeler kalktı) |
| 1050–1140 | yer imi simgesi (SVG) + `Kaydet` (Fredoka 64), x 60'tan |
| 1150–1380 | boş zemin |
| 1400–1920 | boş |

## Hikâye karesi B (`hikaye-b.png`) — soru + cevap düzeni
A'dan farklı düzen: soru sorulur, cevap karede açıktır (v1 çağrı satırı kalktı).

| Bant (y px) | İçerik |
|---|---|
| 280–450 | kanal katmanı + künye |
| 460–560 | `Tarife mi, düzenleme mi?` (Fredoka; 900 px'e sığan, üst sınır 96 → 79; DUZ2) |
| 580–760 | cümle kartı `The train to İzmir` / `leaves at 7 pm today.` (Fredoka 64) · tren + saat ikonu; `leaves` sarı altçizgi |
| 780–900 | şıklar yan yana: `A` `TARİFE` (doğru şık: yeşil çerçeve + kalem ✓) · `B` `DÜZENLEME` (soluk) · DUZ2: şık yazısı 64 px, daire r 32; A kutusu 371 px, B kutusu 497 px |
| 920–1060 | kural özeti: `Tren tarifeye uyar:` / `geniş zaman.` (Lexend 64; seste cümle 3) |
| 1070–1140 | yer imi simgesi (SVG) + `Kaydet` (Fredoka 64) |
| 1150–1380 | boş zemin |
| 1400–1920 | boş |

## Çalıştırma
Her zaman çizelgesi sahnesi `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` (mp4 yok). Birleştirme (mp4 takvimi gelince):
`python3 birlestir.py projeler/02-04-ydt-temel-s3 --tema acik --gecis BookFlip --efekt hisirti`.
Durağan kareler ayrı (birleştirmeye girmez): `04-hyperframes-hikaye` → `hikaye-a.png` + `hikaye.png` · `05` → `kapak-b.png` ·
`06` → `kapak-c.png` · `07` → `hikaye-b.png`.
Ses yeniden kurulumu (sentez yok): `ortak/anlatim/` içinde `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`araclar/ses-paketle.py --yaz --paket 02-04-ydt-temel-s3` → `araclar/altyazi_uret.py projeler/02-04-ydt-temel-s3` → `metin_uret.py`.
Sahne istemleri: `uretim-tutanagi/istem/sahne-v2/D-<klasör>.md` (8 dosya; v1 istemleri `istem/sahne/` yerinde, yalnız tarih için).

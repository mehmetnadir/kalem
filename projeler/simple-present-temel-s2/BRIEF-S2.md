# S2 Shorts — "USUALLY = ALIŞKANLIK" (simple-present-temel-s2, YDT TEMEL) · huni v2

> DUZ2 (16.11, J2-OZET A1–A4): rozet `YDT · TEMEL`; ses c3 `Usually, always, every day: çoğunlukla Simple Present. …` (3 parça); süre 26,68 sn (cümle başları 1,00 · 3,95 · 12,42 · 20,57; sahne 03 11,87–20,02, 04 20,02–26,68; güncel değer `zaman.json`); kart 2. satır `every day: çoğunlukla`; kapak B `ALWAYS` / `NEYİN İŞARETİ?`; kapak C `ÜÇ İFADE,` / `GÜÇLÜ İPUCU`; karakter ana paketin kadın öğrencisi. Rapor `uretim-tutanagi/DUZ2-RAPOR.md`.

Çıktı: önizleme (mp4 yok, standart §1 kural 9; 1080×1920, 30 fps, 25,73 sn, anlatım 25,73 sn hazır) + `kapak-a|b|c.png` (`kapak.png` = A)
+ `hikaye-a|b.png` (`hikaye.png` = A). Bağlayıcı standart: `D/.claude/docs/huni-v2-standart.md` (15.11; bu belge onunla çelişirse standart geçer).
Biçim emsali: `../02-04-ydt-temel-s1/BRIEF-S1.md` (v2). Stil, kalem darbesi, olay sesi kuralları `../simple-present-temel/BRIEF.md` ile aynı;
≥ 64 px içerik yazısı `../present-continuous-dikey/BRIEF-DIKEY.md` §3. Öğe `02-02-ydt-temel`, kod `ING-YDT-GR-02-02-T-S2`, biçim "sinyal sözcük" (standart §5).
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 3,95 · 12,42 · 19,62; toplam 25,73), senaryo `ortak/anlatim/senaryo.json`
(kaynak: `uretim-tutanagi/senaryo-taslak.md`, jüri `uretim-tutanagi/juri/`, düzeltme `uretim-tutanagi/S2-duzeltme.md`, rapor `uretim-tutanagi/S2-C-RAPOR.md`).

Kapak başlığı (2 satır, 2 sözcük + simge): `USUALLY` / `= ALIŞKANLIK`. Can alıcı: "usually, always, every day çoğu zaman alışkanlığı işaret eder" (DUZ2 16.11; ana ders canAlici[2])
(`canAlici[2]`; üç kapakta tek kaynak). Ses: cümle 1–3 öğretmen (`gsJ9nrlXYbPztJxC4fwc`, ana ders `sesler.ogretmen`), cümle 4 (çağrı)
öğrenci (`kadro.ogrenci`, `oPC5I9GKjMReiaM29gjY`; ana dersten). Kalem figürü `kadro.ogrenci` (kadın, genç, LongBangs, GlassRound; peeps-kit).
Kural özeti (kaydet kartı ve hikâye A, tek cümle, cümle 3 ile birebir): `Usually, always,` / `every day: çoğunlukla` / `Simple Present.` (DUZ2 16.11, A3)

## Yerleşim (px) — huni v2 §2
| Bölge | y | İçerik |
|---|---|---|
| Üst boş | 0–280 | yalnız zemin; çip YOK |
| Kanal katmanı | 280–350 | aşağıdaki tablo; kalıcı |
| Künye | 360–450 | konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · TEMEL` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20); 0. kareden son kareye aynı |
| İçerik | 460–1380 | x 60–960 |
| Altyazı + karaoke | 1400–1550 | en çok 2 satır (kapak ve hikâye karelerinde yok) |
| Alt boş | 1570–1920 | yalnız zemin |

Kanal katmanı (bütün sahnelerde AYNI piksel; değerler emsal `02-04-ydt-temel-s1/BRIEF-S1.md` tablosundan AYNEN; tek kaynak bu tablo — ortak modül
yok: canvas `ortak/kunye.js` `KANAL`, HyperFrames sahne başına `yardim.py`):

| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5 (48 × 1920 / 476,3); resim x 53,2 (SVG iç boşluğu 68/1920 düşülür, görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş ve geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare | Ses |
|---|---|---|---|---|---|
| 1 Kanca | 01-hyperframes-kanca | HyperFrames | 0,00–3,00 | 102 | öğretmen |
| 2 Değer | 02-paperjs-deger | Paper.js | 3,00–11,87 | 278 | öğretmen |
| 3 Kaydet | 03-hyperframes-kaydet | HyperFrames | 11,87–19,07 | 228 | öğretmen |
| 4 Çağrı | 04-hyperframes-cagri | HyperFrames | 19,07–25,73 | 230 | öğrenci |
| — | 05-hyperframes-hikaye-a · 06-…-kapak-b · 07-…-kapak-c · 08-…-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 | — |

Sahne sınırı = sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn (`zaman_uret.py`). Sahne 01 → 02 sınırı 3,00 (giriş ≤ 3 sn; cümle 1 3,40'ta
biter, `zaman?` 2,92–3,48 sözcüğünün sonu sahne 02'de duyulur). Her sahnenin ilk 12 karesi geçiş payıdır (son sahne + 30 kuyruk).
Durağan kareler `zaman.json` → `hikaye` (05) ve `duragan[]` (06–08) alanındadır, `sahneler[]` dışında: `birlestir.py` ve `kur.py` yalnız `sahneler[]` okur.

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
Zaman sözcük çapasından okunur (`ortak/anlatim/sozcukler.json`), sabit saniyeden değil. Ekran metni sesten önce gelmez; tek istisna kapak başlığı
(0. kare) ve sahne 04 başındaki ana ders kapağı (görsel).

| sn | Hareket |
|---|---|
| 0,00 | Kapak tam görünür (ilk kare = kapak A; kanal katmanı + künye dahil): başlık `USUALLY` / `= ALIŞKANLIK` (900 px'e sığan en büyük boy, üst sınır 190; iki satır aynı boy; satır 2 sarı hapta: dolgu `#ffe066`, yazı `#1b2440`) · solda takvim yaprağı (`tabler/calendar.svg` biçimi, 5 gün kutusu) · sağda kalem çizgisi figür (`kadro.ogrenci`, peeps-kit) takvime işaret eder; başlık y 460–800, görsel y 820–1380 |
| 0,30–0,80 | Takvimde 5 kutudan 4'üne kalemle tik (5. kutu boş: `usually` ≠ her gün; jüri dil 1) |
| 1,00–3,48 | Cümle 1 yalnız altyazıda, sözcük zamanlı: `Usually` 1,00 · `görünce` 1,80 · `hangi` 2,60 · `zaman?` 2,92 |
| 2,40–3,00 | Uçuş: başlık küçülerek künye satırının sağ boş bölümüne (konu + rozet sonrası, x ≈ 500–940, y ≈ 370–440) gider ve 3,00'te saydamlığı 0 olur; künye metni değişmez, son metin `Simple Present` + `YDT · TEMEL`. Figür ve takvim solar. Kanal katmanı yerinde |
| 3,00–3,40 | Sahne 02: boş kart çerçevesi girer (yazısız, tek hareket); kart x 60–960, y ≈ 480–660 |
| 3,95–6,59 | Kart karaoke, Fredoka 64: `My brother usually` / `goes to school by bus.` (`My` 3,95 · `usually` 4,59 · `goes` 4,99 · `bus.` 5,95). `usually` çapasında (4,59) sarı el dairesi: sahnenin tek sarısı. Alt bölgede oturan figür (`open-peeps/sitting-4.svg`) + otobüs (`coco/bus.svg`) kalemle çizilir (3,95–6,59; ana ders sahne 04 dizisi) |
| 6,59 | Kartın altında soluk TR (Caveat 64, `ikincil`, 2 satır, seslendirilmez): `Kardeşim genellikle` / `okula otobüsle gider.`; y ≈ 690–830 |
| 6,84–8,52 | `alışkanlık` (Caveat 64) `Alışkanlık` çapasında, sarı daireden ince kalem okuyla, kartın sağ altında; ikinci ince ok `usually` dairesinden TR satırdaki `genellikle`ye (köprü; çizgi) |
| 8,67 | Figür ve otobüs solar (alt bölge boşalır); `şu an` (Caveat 64, `ikincil`) yazılır, y ≈ 960–1030 |
| 9,07 | `değil,` çapasında `şu an` üstüne kalem çizgisi |
| 9,79–11,39 | `Her sabah yedide` / `kalkarım.` (Caveat 64) sözcük zamanlı (`her` 9,79 · `sabah` 9,95 · `yedide` 10,31 · `kalkarım` 10,67), y ≈ 1060–1220; `her sabah` altına mürekkep altçizgi (sarı değil); altta 5 küçük gün kutusu sırayla tik alır (5/5: her sabah; y ≈ 1250–1350) |
| 11,87–12,27 | Sahne 03 geçiş payı; sahne 02 öğeleri sahne sınırında solar |
| 12,42–15,86 | Kural özeti kartı (kâğıt kart + kalem kenarı, x 60–960, y ≈ 560–900) girer (tek hareket ≤ 0,45 sn: ölçek 0,96 → 1 + saydamlık); yazı Fredoka 700 72 sözcük zamanlı: `Usually,` 12,42 · `always,` 13,70 · `every day:` 14,50 · `Simple Present.` 15,54 (sarı hap, tek vurgu) |
| 15,86–19,07 | Kart sabit (3,21 sn ≥ 2 sn; standart §3 "2 sn sabit"); kımıldamaz |
| 18,47 | `Kaydet.` çapası: yer imi simgesi (SVG yol; Tabler `bookmark` biçimi, yerel `tabler/` içinde YOK → yol sahnede; emoji değil) kalem darbesiyle ≤ 0,3 sn + `Kaydet` (Fredoka 700 72), kartın altında ortalı, y ≈ 960–1060 |
| 19,07–19,62 | Sahne 04: ana dersin kapağı 16:9 kart (900×506, x 60–960, y 620–1126; standart ≈ 920×518, x 960 sınırı için 900; köşe 24, `murekkep` kenar 4) girer (ölçek 0,94 → 1 + saydamlık), sonra sabit; açık `ortak/kapak/ana-kapak.png`, koyu `ana-kapak-koyu.png` |
| 19,62–21,06 | `Bitmedi, gel.` Fredoka 700 (≈ 96 px, 900 px'e sığan), kartın üstünde (y ≈ 470–590), sözcük zamanlı (`Bitmedi,` 19,62 · `gel.` 20,58); öğrenci sesi |
| 22,49–24,81 | `@ydspublishing · YouTube` Lexend 700 ≈ 56 (`YDS` 22,49), kartın altında (y ≈ 1160–1240); `@ydspublishing` sarı hapta (tek vurgu), `YouTube` mürekkep |
| 24,73–25,73 | Durgun kuyruk (son söz + 1,0 sn) |

Ekranda `@ydspublishing`; seste "YDS Publishing" (`ses-sozluk.json` → "YeDeSe"). Yasak sözler (seste, ekranda, açıklamada): standart §1 kural 4–5
(eski çağrı kalıbı ve süre sözü; tarama komutu sahne istemlerinde, kapı 3). QR yok, emoji yok, "izle" düğmesi taklidi yok, YouTube logosu taklidi yok. Sözcük `t1` değeri cümle sonunu ≤ 0,08 sn aşabilir
(`gibi.` 11,95 > sahne sınırı 11,87; ElevenLabs hizalaması); altyazı bunu taşır, sahne sınırı değişmez.

## Kapak (`kapak-a.png` = `kapak.png`, 1080×1920)
A: sahne 01'in kanca karesi t 0,90 (kare 27: başlık tam, 4 tik bitmiş, ses başlamamış), altyazı katmanı gizli (S1-KAPAK-A yöntemi: `proje` kopyasında
CSS `#altyazi{display:none}`, `hyperframes snapshot --at 0.90`), açık + koyu. B (`06`, `kapak-b.png`): `ALWAYS` / `NEYİN İŞARETİ?` (DUZ2 16.11)
(mürekkep, hapsız) · solda öğrenci başı (`peeps-kit/ogrenci-bas.svg`, kalem çizgisi) + el çizimi balon `always?` (Fredoka 72) · sağda büyük sarı `?`.
C (`07`, `kapak-c.png`): `ÜÇ İFADE,` / `GÜÇLÜ İPUCU` (DUZ2 16.11) (mürekkep, hapsız; jüri dil 3 + kaynak 1a) · el çizimi kart: `usually` · `always` · `every day`
alt alta (Fredoka 72) → kalem oku → `Simple Present` sarı hap (Fredoka 80) · kartın sağında karakter görseli (`ortak/kapak/karakter.png`: genç erkek,
gözlüklü, sola işaret eden "buldum" duruşu; 10 px krem `#f3efe6` çıkartma kenarı, kapak-standardi.md) karta işaret eder; kart x 60–600,
karakter x 620–960; sığmazsa köşedeki küçük takvim çıkar. Üçünde kanal katmanı + künye var, altyazı yok; başlık 2 satır, rakam ve emoji yok.
Tarif: `uretim-tutanagi/kapak-taslak.md` (S2-C notu: karakter A'dan C'ye geçti, istem Huni v2).

## Hikâye kareleri (`hikaye-a.png` = `hikaye.png`, `hikaye-b.png`; 1080×1920)
Durağan; ses yok; altyazı yok; kanal katmanı + künye + kural özeti + `Kaydet` (yer imi simgesi). İçerik y 460–1140; y 1150–1380 boş zemin
(bağ çıkartması elle konur; boş kutu çizilmez); 1400–1920 boş.

| Bölge (y) | A (`05`, kural kartı) | B (`08`, soru kartı "Hangisi doğru?") |
|---|---|---|
| 460–560 | `Usually görünce hangi zaman?` (Caveat 72, mürekkep) | `Hangisi doğru?` (Fredoka 88) |
| 570–820 / 580–740 | kural kartı `Usually, always,` / `every day: çoğunlukla` / `Simple Present.` (DUZ2 16.11, A3) (Fredoka 72; `Simple Present` sarı hap, tek vurgu) | kök `My brother usually ____` / `to school by bus.` (Fredoka 64; boşluk kalem çizgisi; köşede küçük otobüs) |
| 840–1000 / 770–990 | örnek `My brother usually goes` / `to school by bus.` (Fredoka 64; `usually` altında mürekkep altçizgi; köşede küçük otobüs) | şıklar `A) goes` (770–870) · `B) is going` (890–990), el çizimi kart, Fredoka 64; ikisi aynı biçim, sarı yok |
| 1010–1140 | yer imi + `Kaydet` (Fredoka 88, sağa yaslı) | kural özeti `usually = alışkanlık` (Caveat 64, sola yaslı; jüri kaynak 2 b) · yer imi + `Kaydet` (Fredoka 72, sağa yaslı) |

B'de cevap karede yok (doğru şık A; not yalnız `aciklama-b.md`'de); karenin sarısı yok. Satır ≤ 24 karakter. Tarif: `uretim-tutanagi/hikaye-taslak.md`.

## Çalıştırma
Her sahne `calistir.sh --tema acik` (önizleme: `ONIZLE_YALNIZ=1`); birleştirme `python3 birlestir.py projeler/simple-present-temel-s2 --tema acik
--gecis BookFlip --efekt hisirti` (mp4 takvimi gelince). Durağan kareler ayrı: `sahneler/<klasör>/calistir.sh --tema acik|koyu` → paket kökü PNG.
Ses yeniden kurulumu (sentez yok): `ortak/anlatim/` içinde `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`araclar/ses-paketle.py --yaz --paket simple-present-temel-s2` → `araclar/altyazi_uret.py projeler/simple-present-temel-s2` → `metin_uret.py`.
Sahne istemleri: `uretim-tutanagi/istem/sahne/D-<klasör>.md` (8 dosya; emsal `../02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/`).
Sahne kodu tabanı (yalnız okunur): emsal `../02-04-ydt-temel-s1/sahneler/` aynı rol: 01 ↔ `01-hyperframes-kapak`, 02 ↔ `02-paperjs-ornek`,
03 ↔ `08-hyperframes-kaydet`, 04 ↔ `03-hyperframes-cta`, 05 ↔ `04-hyperframes-hikaye`, 06 ↔ `05-…-kapak-b`, 07 ↔ `06-…-kapak-c`, 08 ↔ `07-…-hikaye-b`.

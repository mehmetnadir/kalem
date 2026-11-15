# simple-present-temel-s2 · Shorts senaryo taslağı (huni v2, 9:16, hedef 22–26 sn)

Durum: TASLAK (istem P0202-S2-A, 15.11.2026). Ses sentezi, sahne kodu ve render YOK.
Bağlayıcı standart: `dijital-anlatim/.claude/docs/huni-v2-standart.md` (4 sahne: kanca → değer → kaydet → çağrı).
Kaynak ders: `../../simple-present-temel/` (`ortak/anlatim/senaryo.json`, `sureler.json`, `surumler.json`, `BRIEF.md`).
Biçim emsali: `../../02-04-ydt-temel-s2/uretim-tutanagi/` (yalnız dosya biçimi ve yazım kuralı; 3 sahneli yapı ve "Tam ders" kalıbı ESKİ).
Ölçülmüş ikizler: `../../02-04-ydt-temel-s2/ortak/anlatim/sureler.json` (v2 pilot; aynı öğretmen ve öğrenci sesi).
**S2-C (15.11) klasör adları (istem Huni v2, bağlayıcı):** `01-hyperframes-kanca` · `02-paperjs-deger` · `03-hyperframes-kaydet` · `04-hyperframes-cagri`;
durağan `05-hyperframes-hikaye-a` · `06-hyperframes-kapak-b` · `07-hyperframes-kapak-c` · `08-hyperframes-hikaye-b`. Aşağıdaki eski adlar
(`01-hyperframes-kapak`, `02-paperjs-ornek`, `08-hyperframes-kaydet`, `03-hyperframes-cta`, `04-…-hikaye`, `05-…-kapak-b`, `06-…-kapak-c`,
`07-…-hikaye-b`) sırayla bunlara karşılık gelir. Ölçülen süreler: `../BRIEF-S2.md`, `../zaman.json`, `S2-C-RAPOR.md` (§5 tahmindir).

## 1. Künye

| Alan | Değer |
|---|---|
| Kimlik | `02-02-ydt-temel-s2` (paket `simple-present-temel-s2`; ders başına 3 kısa, S2 = sinyal sözcük) |
| Kod | `ING-YDT-GR-02-02-T-S2` (ana ders `surumler.json` → `video.kod` + `-S2`) |
| Konu | Simple Present · YDT · temel |
| Biçim | sinyal sözcük (standart §5): zaman sözcüğü → zaman |
| Taşınan bilgi | `usually`, `always`, `every day` alışkanlık işaretidir; alışkanlık Simple Present ile söylenir; şu an olan iş değildir |
| Ana ders kaynağı | cümle 1 (`Her sabah yedide kalkarım.`) ve cümle 4 (EN örnek + `Usually, always, every day: alışkanlık işareti.`); sahne `01-hyperframes-giris`, `04-canvas-ornek2` |
| Can alıcı | `canAlici[2]` "usually, always, every day = tekrar eden iş sinyali" + `canAlici[1]` "'Her sabah yedide kalkarım' — alışkanlık iki dilde aynı zamanla" |
| Format | dikey 1080×1920, 30 fps, tema açık (K19); mp4 yok, sayfada önizleme (standart §1 kural 9) |
| Ses | cümle 1–3 öğretmen `gsJ9nrlXYbPztJxC4fwc` (ana ders `sesler.ogretmen`); cümle 4 öğrenci `oPC5I9GKjMReiaM29gjY` (ana ders `kadro.ogrenci`, `sesler.ogrenci`); eleven_v4, tohum 0 |
| Kanal katmanı | `ydspublishing` yazı logosu + `@ydspublishing`, y 280–350, ilk kareden son kareye, giriş/çıkış yok (standart §1 kural 1, §2) |
| Künye | `Simple Present` + rozet `YDT · BASIC`, y 360–450 (v2 pilot `02-04-ydt-temel-s2/BRIEF-S2.md` ile aynı) |
| Yasak söz | "Tam ders" ve süre sözü ("dakika") seste, ekranda, açıklamada yok (standart §1 kural 4–5); QR yok, emoji yok |

## 2. Senaryo

**TR** / **EN** = ses parçasının dili. Ses metninde rakam ve okunan kısaltma yok. Sözcük zamanları tahmindir (§5); gerçek çapa sentezden sonra
`ortak/anlatim/sozcukler.json`'dan okunur. Ekranda her konuşulan satır altyazı bandında (y 1400–1550) sözcük zamanlı akar; aşağıdaki "Ekran metni"
içerik bandındaki (y 460–1380) yazıdır.
İşaret: **[YENİ]** = ana derste yok, jüri bakacak · **[ANA]** = ana derste aynı tümce var · **[S2-04]** = `02-04-ydt-temel-s2` ile birebir.

| Sahne | Konuşan | Ses metni (söylenen) | Ekran metni | Görsel fikir |
|---|---|---|---|---|
| 1 Kanca · `01-hyperframes-kapak` · 0,00–2,73 | öğretmen | **TR** `Usually görünce hangi zaman?` **[YENİ]** · ilk söz 1,00 (`Usually` 1,00 · `görünce` 1,63 · `hangi` 2,10 · `zaman?` 2,42) | 0. kare = kapak A (`kapak-taslak.md` §3): başlık `USUALLY` / `= ALIŞKANLIK` (hap) 0. karede tam (kapak istisnası, kalıp §4–§5). Başka içerik yazısı yok | İlk kare kapak. 0,30–0,80 takvim yaprağında 5 gün kutusundan 4'üne kalemle tik (S2-C, jüri dil 1: `usually` ≠ her gün; kapak PNG karesi t 0,90). 2,10–2,73 uçuş: başlık künye satırına (y 360–450), karakter ve takvim solar. Kanal katmanı yerinde |
| 2 Değer · `02-paperjs-ornek` · 2,73–11,10 | öğretmen | **EN** `My brother usually goes to school by bus.` **[ANA]** cümle 4 parça 2 (`My` 3,28 · `usually` 3,92 · `goes` 4,36 · `bus.` 5,76) | Kart: `My brother usually` / `goes to school by bus.` (Fredoka 64, karaoke, y ≈ 480–640). 6,24'ten sonra altında soluk TR: `Kardeşim genellikle okula otobüsle gider.` (Caveat 48, ikincil renk; seslendirilmez, standart §3 "TR soluk") | `usually` çapasında (3,92) sarı daire: sahnenin tek sarısı. Sağ altta kalemle oturan figür + otobüs (ana ders sahne 04 dizisi: `open-peeps/sitting-4.svg`, `coco/bus.svg`), 3,28–6,24 |
| | | **TR** `Alışkanlık işareti.` **[YENİ]** ana ders cümle 4 parça 4'ün son iki sözcüğü (`Alışkanlık` 6,49) | `alışkanlık` (Caveat 56) daireden ince kalem okuyla, kartın sağ altında (6,49) | `usually` dairesinden TR satırdaki `genellikle`ye ikinci ince ok (köprü; yazı değil, çizgi) |
| | | **TR** `Şu an değil, her sabah yedide kalkarım gibi.` **[YENİ]** ana ders cümle 1 + `gibi`; `Şu an değil` ana derste yok (`Şu` 7,85 · `her` 9,15 · `kalkarım` 10,29) | 7,85: `şu an` (Caveat 56, ikincil) yazılır, `değil,` (8,18) çapasında üstüne kalem çizgisi · 9,15: `Her sabah yedide kalkarım.` (Caveat 56, y ≈ 1040) sözcük zamanlı | 9,15'ten 5 küçük gün kutusu (el çizimi, ana ders sahne 04 görseli) altta sırayla tik alır: her gün tekrar eden iş. `her sabah` altına mürekkep altçizgi (sarı değil) |
| 3 Kaydet · `08-hyperframes-kaydet` · 11,10–18,31 | öğretmen | **EN** `Usually, always, every day: Simple Present.` **[YENİ]** (S2-C, jüri dil 2: Türkçe sözcük yok → `en` parça) içerik ana ders cümle 4 parça 4 ve cümle 7 son parça (`Kod: always, usually, every day, Simple Present.`) ile aynı; sıra ve biçim yeni (`Usually,` 11,65 · `always,` 12,82 · `every` 13,86 · `Simple` 15,16) | Kural özeti kartı (tek cümle, Fredoka 72, x 60–960, y ≈ 560–900): `Usually, always,` / `every day:` / `Simple Present.` sözcük zamanlı; 15,68'den sahne sonuna sabit (2,63 sn ≥ 2 sn) | Kart tek hareketle girer (≤ 0,45 sn, 11,10–11,55). Tek sarı: `Simple Present` hapı (15,16). Sahne 02'nin daire, ok ve kutuları sahne sınırında solar |
| | | **TR** `Bu kuralı kaybetme. Kaydet.` (standart §4 kaydet kalıbı; metin `02-04-ydt-temel-s2` cümle 3 parça 2 ile aynı, komşu farklı) (`Bu` 15,83 · `Kaydet.` 17,71) | `Kaydet` (Fredoka 72) kartın altında (y ≈ 960–1040), `Kaydet.` çapasında (17,71) | Yer imi simgesi (SVG yol, emoji değil) `Kaydet.` çapasında kalemle çizilir, mürekkep. Kart kımıldamaz |
| 4 Çağrı · `03-hyperframes-cta` · 18,31–24,97 | **öğrenci** | **TR** `Bitmedi, gel.` · **TR** `Dersin tamamı YDS Publishing YouTube kanalında.` **[S2-04]** cümle 4 birebir (`Bitmedi,` 18,86 · `gel.` 19,82 · `YDS` 21,73 · `kanalında.` 23,25) | `Bitmedi, gel.` Fredoka 700, kartın üstünde (y ≈ 470–600), sözcük zamanlı · `@ydspublishing · YouTube` kartın altında (y ≈ 1160–1260; `@ydspublishing` sarı hap, `YouTube` mürekkep), `YDS` çapasında (21,73) | 18,31–18,86: ana dersin kapağı 16:9 kart girer (`../../simple-present-temel/kapak.png` / `kapak-koyu.png`, 1920×1080 → 900×506, x 60–960, y 620–1126; standart ≈ 920×518, x 960 sınırı için 900; pilot ile aynı). 23,97–24,97 durgun kuyruk |

Sahne sınırı = sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn (v2 pilot kuralı). Ekran metni sesten önce gelmez; tek istisna kapak başlığı
(0. kare) ve sahne 04 başındaki ana ders kapağı (görsel; pilot emsali). TR çeviri satırı seslendirilmez: EN cümle bittikten sonra soluk belirir.
Hikâye kareleri ve kapak B/C zaman çizelgesi dışında (`hikaye-taslak.md`, `kapak-taslak.md`).

## 3. Kaynak eşlemesi ve ses önbelleği

| Parça | Ana derste | Ses önbelleği |
|---|---|---|
| C1 `Usually görünce hangi zaman?` | yok | yok (yeni) |
| C2 EN `My brother usually goes to school by bus.` | cümle 4 parça 2, birebir | yok: komşu parçalar değişir |
| C2 `Alışkanlık işareti.` | cümle 4 parça 4 içinde (`… every day: alışkanlık işareti.`) | yok |
| C2 `Şu an değil, her sabah yedide kalkarım gibi.` | `Her sabah yedide kalkarım` = cümle 1; `Şu an değil` ve `gibi` yok | yok |
| C3 `Usually, always, every day: Simple Present.` | içerik cümle 4 parça 4 + cümle 7 son parça; tümce yok | yok |
| C3 `Bu kuralı kaybetme. Kaydet.` | yok (standart §4 kalıbı) | yok: `02-04-ydt-temel-s2` cümle 3'te önceki parça `Bu, üç farktan yalnız biri.`; burada önceki parça farklı |
| C4 `Bitmedi, gel.` + `Dersin tamamı YDS Publishing YouTube kanalında.` | yok (standart §4 kalıbı) | **VAR**: `02-04-ydt-temel-s2` cümle 4 ile birebir (2 parça, aynı sıra, aynı ses `oPC5I9GKjMReiaM29gjY`, eleven_v4, tohum 0). Whisper 1,00 · 1,00 (`02-04-ydt-temel-s2/ortak/anlatim/sentez.wav.rapor.json`) |

**Ana dersin bir cümlesiyle birebir aynı cümle yok.** EN parça ana dersle aynıdır, ama önbellek anahtarı aynı cümlenin önceki ve sonraki
parçalarını da içerir (`dijital-anlatim/araclar/iki-dilli/el.py` satır 88 ve 138–142: `[metin, dil, onceki, sonraki, ses, model, tohum]`).
Cümle 4 kardeş kısa `02-04-ydt-temel-s2` cümle 4 ile birebir aynıdır → srv21 önbelleğinden gelir, ücretsiz.
Standart §4 "aynı derste yinelenmez" kuralı ders içindir: `Bitmedi, gel.` 02-04'te de S2'dedir; 02-02 dersinin S1 ve S3'ü bu girişi kullanmaz.

## 4. Ses metni notları

- TR parça İngilizce sözcükle başlar (`Usually görünce …`). Emsal: `02-04-ydt-temel-s2` `Today iki zamanda da geçebilir; …` duyulan "Today, …", benzerlik 1,00.
- C3 parça 1 `en` parçadır (S2-C, jüri dil 2): Türkçe sözcük taşımaz; parça düzeni kuralı bağımsız İngilizceyi `en` sentezler. Eski not
  ("ana ders cümle 4 parça 4 ve cümle 7 son parça aynı biçimde") yanlıştı: o parçalarda Türkçe çapa var. Emsal: `02-02-ydt-temel`
  `Every day, always, usually:` `en` parçası, Whisper 1,00. Sentezde kulak + Whisper kapısı zorunlu.
- EN parça tam cümledir; tek sözcüklük EN parça yok (13.11 KULAK).
- TR parçada rakam (`yedide` sözcük), kısaltma, `-ing` yok. "Dil sınavı" sözü gerekmedi; YDT seste geçmez.
- Hitap: yalnız standart kalıplarda (`kaybetme`, `Kaydet`, `gel`). Yeni cümlelerde sen/siz yok (`görünce` ulaç).
- `@ydspublishing` sesle okunmaz; seste "YDS Publishing" (`ses-sozluk.json` → "YeDeSe"; önbellekteki ses bu söyleyişle).
- Maliyet (tahmin): yeni parçalar 202 karakter (cümle 1–3). 02-04 S1 oranıyla (257 karakter ≈ 1,26 TL) ≈ 0,99 TL. Cümle 4 ücretsiz.

## 5. Süre (tahmin; gerçek süre sentez sonrası `zaman.json`)

Yöntem: ölçülmüş ikizi olan parça ikizin süresini alır. İkizi olmayan TR parça ana dersin ölçülmüş öğretmen hızından hesaplanır:
süre = 0,1731 sn × hece + 0,649 sn × iç duraklama (virgül, iki nokta, cümle içi nokta). Model ana ders `sureler.json` 20 TR öğretmen parçasına
en küçük kareler uyumudur (5,78 hece/sn; ortalama mutlak hata %10,9, en büyük %29,3). Parça arası: EN'li geçiş 0,25 sn, TR → TR 0,15 sn
(`el.py`); cümle arası 0,55 sn; ilk söz 1,00 sn; kuyruk 1,00 sn.

| Cümle / parça | Hece · duraklama | Kaynak | sn | Başlar | Biter |
|---|---|---|---|---|---|
| 1 `Usually görünce hangi zaman?` | 10 · 0 | model | 1,73 | 1,00 | 2,73 |
| 2 EN `My brother usually goes …` | — | ana ders cümle 4 parça 2: 29,53–32,49 | 2,96 | 3,28 | 6,24 |
| 2 `Alışkanlık işareti.` | 7 · 0 | model | 1,21 | 6,49 | 7,70 |
| 2 `Şu an değil, her sabah yedide kalkarım gibi.` | 15 · 1 | model | 3,25 | 7,85 | 11,10 |
| 3 `Usually, always, every day: Simple Present.` | 12 · 3 | model (ana dersin aynı biçimli iki parçası: ölçülen 4,64 ve 4,72, model 4,72 ve 4,85; bu biçimde model %2–3 uzun) | 4,03 | 11,65 | 15,68 |
| 3 `Bu kuralı kaybetme. Kaydet.` | — | `02-04-ydt-temel-s2` cümle 3 parça 2: 2,31–4,79 | 2,48 | 15,83 | 18,31 |
| 4 `Bitmedi, gel.` | — | `02-04-ydt-temel-s2` cümle 4 parça 1 (önbellek) | 1,44 | 18,86 | 20,30 |
| 4 `Dersin tamamı YDS Publishing …` | — | `02-04-ydt-temel-s2` cümle 4 parça 2 (önbellek) | 3,52 | 20,45 | 23,97 |
| kuyruk | | | 1,00 | 23,97 | 24,97 |

**Toplam tahmin 24,97 sn** (hedef 22–26). Sahneler: 01 0,00–2,73 · 02 2,73–11,10 · 03 11,10–18,31 · 04 18,31–24,97.
Standart §3 ile: kanca 0–4 sn → 0–2,73 · değer 4–15 sn → 2,73–11,10 · kaydet 15–18 sn → 11,10–18,31 · çağrı 18–25 sn → 18,31–24,97.
Kaydet sahnesi tablodan uzun (7,21 sn): kural özeti seslendirilir (istem). İlk 10 sn'de 3 hareket türü: uçuş (01), kalem çizimi (figür, otobüs, gün
kutuları), karaoke (02).

Sapma payı: modelli parçalar 10,22 sn, komşusu değişen ikizler 5,44 sn, önbellek parçaları 4,96 sn (sapmaz).
Olağan sapma (modelli +%10,9, ikiz +%10): **26,63 sn**. En kötü (modelli +%29,3, ikiz +%10): **28,51 sn** → 28 sn'yi aşar; B planı gerekir.

**B planı (yalnız ölçülen toplam 28 sn'yi aşarsa; metin değişmez, jüri gerekmez):** 1) ilk söz 1,00 → 0,50 (kalıp §5 "ilk söz 0. sn"
izin verir) = −0,50 sn · 2) kuyruk 1,00 → 0,44 = −0,56 sn. En kötü durum 27,45 sn olur.
**C planı (yalnız B planı yetmezse; metin değişir, jüri gerekir):** C2 parça 3'ten `yedide` çıkar (`Şu an değil, her sabah kalkarım gibi.`) ≈ −0,5 sn.

### 5b. Ölçülen (S2-C, 15.11 sentez sonrası; jüri dil 2 "§5 yeniden hesaplanır")

Kaynak: `../ortak/anlatim/sureler.json`, `baslar.json`, `sentez.wav.rapor.json`; `../zaman.json`. C3 parça 1 `en` (HIZ_EN 0,9) sentezlendi.

| Cümle / parça | Tahmin sn | Ölçülen sn | Başlar | Biter |
|---|---|---|---|---|
| 1 `Usually görünce hangi zaman?` | 1,73 | 2,40 | 1,00 | 3,40 |
| 2 EN `My brother usually goes …` | 2,96 | 2,64 | 3,95 | 6,59 |
| 2 `Alışkanlık işareti.` | 1,21 | 1,68 | 6,84 | 8,52 |
| 2 `Şu an değil, her sabah yedide kalkarım gibi.` | 3,25 | 3,20 | 8,67 | 11,87 |
| 3 EN `Usually, always, every day: Simple Present.` | 4,03 (`tr` modeli) | 4,08 | 12,42 | 16,50 |
| 3 `Bu kuralı kaybetme. Kaydet.` | 2,48 | 2,32 | 16,75 | 19,07 |
| 4 `Bitmedi, gel.` (önbellek) | 1,44 | 1,44 | 19,62 | 21,06 |
| 4 `Dersin tamamı YDS Publishing …` (önbellek) | 3,52 | 3,52 | 21,21 | 24,73 |
| kuyruk | 1,00 | 1,00 | 24,73 | 25,73 |

**Ölçülen toplam 25,73 sn** (tahmin 24,97; hedef 22–28; B planı gerekmedi). Sahneler: 01 0,00–3,00 · 02 3,00–11,87 · 03 11,87–19,07 ·
04 19,07–25,73. Sahne 01 giriş tavanı 3,00 (cümle 1 3,40'ta biter). Parça süreleri el.py parça sınırıdır (sessizlik payı dahil); sözcük
zamanları `../ortak/anlatim/METIN.md`.

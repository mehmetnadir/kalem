# DUZ2-0202S2 raporu — `simple-present-temel-s2` (A/B kol a, değişken `kapanis`) · J2 özeti A sınıfı düzeltmeleri · 16.11.2026

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 / TD-1 (rozet), A2 / TD-2 (karakter + ana kapak), A3 + A4 (EK-5b, EK-5c: kural cümlesi kapsamı), TD-3 (`canAlici` yanlış denklik), KS-4 / HV-20b (kapak B başlığı) |
| A6 (hikâye B kural özeti) | düzeltme gerekmedi: hikâye B `usually = alışkanlık` kural satırını ve "Kaydet"i taşır (J2 HV-21 evet) |
| TD-4 (bayat UTM notu) | uygulanmaz: bu pakette not yok (`grep "küçük harf" aciklama*.md` → 0) |
| Yeniden sentez | 1 cümle (c3; 3 parça, 80 karakter ≈ 0,39 TL); c1, c2, c4 önbellekten, sha256 değişmedi |
| Süre (`ffprobe anlatim.m4a`) | 25,73 → **26,68 sn** (kabul ≤ 35 sağlandı; hedef 22–26 0,68 sn aşıldı) |
| İlk söz · kanca cümlesi bitişi | 1,00 sn (≤ 1, sınırda) · 3,48 sn (`zaman?` t1; kanca ≤ 4 sağlandı) |
| Whisper en düşük | 0,94 (c3 parça 2, duyulan `Çoğunlukla Simple Crescent.`); eşik 0,90 |
| Kareler | 4 sahne (20 açık + 6 koyu) + 5 kök türev + 5 koyu türev, hepsi yeniden çekildi; mp4 yok |
| Çakışma kapısı | çıkış **0** (4 sahne, çakışma yok) |
| Üretici model | Claude Opus 5.5 (`claude-opus-5-5`); jüri başka modelle koşmalı (juri-olcutleri §1e) |

Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` (§3A, A3 ayrıntısı, §4.1, §4.2 P2, Sıra), `juri/J2-hukum.md`, `D/.claude/docs/huni-v2-standart.md`,
`huni-ab-sozlesme.md`, `kapak-standardi.md`, `juri-olcutleri.md` (15.11 akşam). Kol b raporu: `../../simple-present-temel-s2b/uretim-tutanagi/DUZ2-RAPOR.md`.
Not: iş 15.11 gecesi başladı, makine bellek arızasında kesildi (kol b `el.py` 00:24 koşusu `Killed`). Bu oturum kol a sesini önceki koşudan aldı
(`ses-sentez-DUZ2.log` 00:20–00:23, rc 0), ötekileri tamamladı ve hepsini yeniden doğruladı.

## 1. Düzeltmeler

| # | Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| 1 | A1 / TD-1 (HV-24) | `ortak/anlatim/senaryo.json` `giris.rozetler`, `BRIEF-S2.md`, `ortak/kunye.js`, 7 `yardim.py` (01, 03–08), SPEC 01, 06, 07, 08 | `YDT · BASIC` → `YDT · TEMEL` | `grep -rn BASIC --include=*.py/js/json/html` (tutanak dışı): 0 satır. Her karede tek rozet metni; 04 son karede künye ve ana kapak kartı ikisi de `YDT · TEMEL` (`04-…-26.6.png`) |
| 2 | A2 / TD-2 (K22, KS-10) | `ortak/kapak/karakter.png` | erkek, iri kıvırcık saç (`a4198903…`) → ana paketin kadın öğrencisi (`5a902b40…`, sha256 ana paketle eş) | eski dosya `~/Silinecekler/2026-11-15-duz2-0202S2/simple-present-temel-s2/ortak/kapak/` |
| 3 | A2 (çağrı son kartı) | `ortak/kapak/ana-kapak.png`, `ana-kapak-koyu.png` | eski ana kapak (`e2bbf46d…` / `df33df75…`, erkek) → ana paketin yeni `kapak.png` / `kapak-koyu.png` (`7f714514…` / `7e948a3b…`) | huni §1 kural 7: son sahnede ana dersin kapağı. `04-…-26.6.png`, koyu `k/koyu/04-…-26.6.png` |
| 4 | A2 (yerleşim) | `sahneler/07-hyperframes-kapak-c/uret.py` | ölçek 0,465 → 0,455; aramaya `sart5` (karakter kutusu hap kutusuna binmez) eklendi | ilk koşu `Kesişim hap - karakter: 269` ile düştü (§5). Yeni karakter sol eliyle yukarı-sola, karta ve başlığa işaret eder; kutu (10 px kenar dahil) x 645–958, y 817–1264 (`nesneler.json`); kart ve hapla kesişim 0 (`kurallari_dogrula`) |
| 5 | A3 + A4 (ses) | `senaryo.json` c3 | `Usually, always, every day: Simple Present. Bu kuralı kaybetme. Kaydet.` → `Usually, always, every day: çoğunlukla Simple Present. Bu kuralı kaybetme. Kaydet.` (parça `en` + `tr` + `tr`) | `sentez.wav.rapor.json`; §2 |
| 6 | A3 + A4 (kart) | `sahneler/03-hyperframes-kaydet/uret.py` | 2. satır `every day:` → `every day:` + `çoğunlukla` (`#s4`, T(4) `çoğunlukla` 15,39'da girer); hap T(5) `Simple`; kart sabit = max(T(6) `Present`, hap + 0,30); yer imi T(10) `Kaydet` | `03-…-19.95.png`: 2. satır x 149–870 (sınır 910), kart yüksekliği değişmedi |
| 7 | A3 + A4 (hikâye A) | `sahneler/05-hyperframes-hikaye-a/uret.py` | kart 2. satırı `every day:` → `every day: çoğunlukla` | `hikaye-a.png`, `k/koyu/hikaye-a-koyu.png` |
| 8 | A4 (kapak C) | `sahneler/07-hyperframes-kapak-c/uret.py` `SAT2` | `ÜÇ İFADE, / TEK İŞARET` → `ÜÇ İFADE, / GÜÇLÜ İPUCU` (S 143 → 140) | `kapak-c.png`, `k/koyu/kapak-c-koyu.png` |
| 9 | A4 + KS-4 / HV-20b (kapak B) | `sahneler/06-hyperframes-kapak-b/uret.py` | `ALWAYS VARSA / HANGİ ZAMAN?` → `ALWAYS / NEYİN İŞARETİ?` (S 116 → 125; 3 sözcük) | `kapak-b.png`, `k/koyu/kapak-b-koyu.png`; öneriden sapma gerekçesi §1.1 |
| 10 | TD-3 | `surumler.json` `video.canAlici` (senaryo `meta.canAlici` önceki oturumda düzelmişti) | `Türkçedeki geniş zaman eki = İngilizcedeki s: gider = goes` ve `usually, always, every day = tekrar eden iş sinyali` → ana paketin `surumler.json` `canAlici` dizisi birebir | `grep "= İngilizcedeki\|tekrar eden iş" surumler.json`: 0 |
| 11 | KS-4 notu | `aciklama-b.md` satır 4 ve 35 | `(kapak B ile aynı soru)` → kapak B'nin yeni metni, "başlıktan ayrı" | dosya |
| 12 | kaynak belge | `BRIEF-S2.md` (DUZ2 satırı + 5 metin), SPEC 03, 05, 06, 07 (DUZ2 satırı) | eski metinler yeni metinle | yeniden üretim aynı sonucu verir |
| 13 | eski QA kareleri | `01/k/ara/`, `05/k/qa/`, `08/k/qa/`, `03/k/*`, `04/k/*` (eski zamanlı) | `~/Silinecekler/2026-11-15-duz2-0202S2/simple-present-temel-s2/sahneler/` | `LISTE.md` satırı; içlerinde `BASIC` rozetli ve eski kartlı kareler vardı |

### 1.1 Önerilen metnin denetimi (istem: "öneriyi kendin de denetle")

| Yer | Önerilen (J2-OZET A3) | Uygulanan | Gerekçe |
|---|---|---|---|
| ses c3, kart, hikâye A | `Usually, always, every day: çoğunlukla Simple Present.` | aynı | Doğru ve kapsamlı: üç ifade çoğu zaman Simple Present ister; `always` Present Continuous ile (`He is always complaining.`), `every day` geçmişle (`I walked every day.`) de gelir. "çoğunlukla" bu istisnayı açık bırakır |
| kapak C satır 2 | `GÜÇLÜ İPUCU` | aynı | 4 sözcük (HV-20b 2–4); "tek" mutlaklığı kalktı |
| kapak B | `ALWAYS = ?` | `ALWAYS / NEYİN İŞARETİ?` | (1) `ALWAYS = ?` tek sözcüktür; HV-20b 2–4 sözcük ister. (2) `=` işareti tek denklik ima eder; A4'ün kaldırdığı mutlak sunumu geri getirir. Yeni metin 3 sözcük, B başlığını (`Always varsa hangi zaman?`) yinelemez, kuralı vermez, sesin terimini taşır (c2 `Alışkanlık işareti.`) |

Terim birliği (sesle aynı terim):

| Yüzey | Metin |
|---|---|
| ses c3 | `… every day: çoğunlukla Simple Present.` |
| kaydet kartı (sahne 03), hikâye A | `Usually, always, / every day: çoğunlukla / Simple Present.` |
| açıklama A (YouTube metni) | `Usually, always, every day: çoğunlukla Simple Present.` (bce68bd'den) |
| açıklama B | `Çoğunlukla alışkanlık işareti: Simple Present.` |
| kapak B · kapak C | `ALWAYS / NEYİN İŞARETİ?` (ses c2 `işareti`) · `ÜÇ İFADE, / GÜÇLÜ İPUCU` |

## 2. Ses, süre ve Whisper

Komut: `timeout 1500 bash araclar/ses-sunucu.sh simple-present-temel-s2` (00:20, rc 0) → `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`ses-paketle.py --yaz --paket …` → `altyazi_uret.py` → `metin_uret.py` (günlük `ses-sentez-DUZ2.log`, rc 0). `el.py` çıktısı: "kapı önbelleği 6 / 9
parça · 80 karakter · 9 / 9 parça kapıdan geçti". c3'ün 3 parçası yeniden sentezlendi: `el.py` anahtarı komşu parçayı içerir; 3·3 metni aynı kaldı ama
önceki parçası değişti.

| Parça | Konuşan | Metin | Duyulan (Whisper) | Benzerlik |
|---|---|---|---|---|
| 1·1 | öğretmen | Usually görünce hangi zaman? | aynı | 1,00 |
| 2·1 | öğretmen | My brother usually goes to school by bus. | aynı | 1,00 |
| 2·2 | öğretmen | Alışkanlık işareti. | Alışkanlık işareti | 1,00 |
| 2·3 | öğretmen | Şu an değil, her sabah yedide kalkarım gibi. | … 7'de … | 1,00 |
| 3·1 | öğretmen (`en`) | Usually, always, every day: | Usually, always, every day. | 1,00 |
| 3·2 | öğretmen (`tr`) | çoğunlukla Simple Present. | Çoğunlukla Simple Crescent. | **0,94** |
| 3·3 | öğretmen | Bu kuralı kaybetme. Kaydet. | aynı | 1,00 |
| 4·1 | öğrenci | Bitmedi, gel. | aynı | 1,00 |
| 4·2 | öğrenci | Dersin tamamı YDS Publishing YouTube kanalında. (ses metni `YeDeSe`) | … YEDESE Publishing … | 1,00 |

3·2 notu: Türkçe Whisper İngilizce terimi `Crescent` yazdı; eşik geçti. Kol b'de aynı metin 1,00 duyuldu. Dinleme kaydı (EK-11) Nadir'in işidir.

| Ölçü | Önce | Sonra |
|---|---|---|
| Toplam | 25,73 | 26,68 |
| Cümle başları | 1,00 · 3,95 · 12,42 · 19,62 | 1,00 · 3,95 · 12,42 · 20,57 |
| Sahne 03 kaydet | 11,87–19,07 (228 kare) | 11,87–20,02 (257 kare) |
| Sahne 04 çağrı | 19,07–25,73 | 20,02–26,68 (230 kare) |
| Kart sabit (03) | 15,86–19,07 (3,21) | 16,65–20,04 (3,39) |
| Yer imi · "Kaydet" yazısı | 18,47 · 18,57 | 19,42 · 19,52 |

| Cümle wav | sha256 (ilk 12) | Durum |
|---|---|---|
| `cumle-1.wav` | `3128f4881413` | değişmedi (kol b ile eş) |
| `cumle-2.wav` | `c102637639ac` | değişmedi (kol b ile eş) |
| `cumle-3.wav` | `3a7e07035c51` | yeni (A3/A4) |
| `cumle-4.wav` | `b192db36b66b` | değişmedi |

## 3. Kareler (hepsi bu oturumda, kol a'dan)

Yöntem: 01, 03, 04 `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik`; sonra `node araclar/sahne-kare.mjs simple-present-temel-s2 <sahne> <t…> <k dizini>
--tema acik|koyu --port 41333 --sunucu 41022` (02 çalışma anında kurulur). Kapak A: RAPOR 01 "Kapak A" yöntemi (`proje-ka`, `#altyazi{display:none}`,
`hyperframes snapshot --at 0.90`, koyu önce). 05–08: `bash calistir.sh --tema koyu`, sonra `--tema acik` (kök PNG). Hepsi sırayla, tek tarayıcı.

| Sahne / türev | Açık | Koyu |
|---|---|---|
| 01 kanca | 0 · 1,5 · 2,95; `kapak-a.png` = `kapak.png` | 1,5; `k/koyu/kapak-a-koyu.png` |
| 02 değer | 3,05 · 7,45 · 11,8 | 7,45 |
| 03 kaydet | 11,95 · 15,6 · 16,9 · 18,9 · 19,95 | 19,95 |
| 04 çağrı | 20,1 · 21,6 · 23 · 24,7 · 26,6 | 23 · 26,6 |
| 05–08 | `hikaye-a.png` (= `hikaye.png`), `kapak-b.png`, `kapak-c.png`, `hikaye-b.png`; `k/at-0.5s.png` ile piksel farkı 0 | `k/koyu/<türev>-koyu.png` × 4 |

Kontak: `uretim-tutanagi/kontak/DUZ2-acik.png` (16 kare), `DUZ2-koyu.png` (10 kare). Açtığım kareler (Read): `kapak-a`, `kapak-b`, `kapak-c` (ilk ve
son), `hikaye-a`, `03-…-19.95`, `04-…-26.6` tam boy; ötekiler kontakta. Bulgu: taşma yok, çakışma yok, okunmayan yazı yok; her karede rozet
`YDT · TEMEL`; karakter yalnız kapak C ve ana kapak kartında, ikisi de kadın öğrenci; altyazı 1400–1550 bandında, en çok 2 satır; kanal katmanı her karede.

HV-13 (kart 2 sn sabit, kart bölgesi x 60–960, y 548–912): `03-…-16.9.png` ↔ `03-…-18.9.png` **0 px** (kanal farkı > 16; en büyük 0).
16,9 ↔ 19,95: 193 px (en büyük 32), yalnız kart alt kenar çizgisinde (y 894–900, x 591–709) 1 px yarı-piksel kayması; yer imi kartın dışında çizilir.

## 4. Çakışma kapısı

Komut: `node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --port 41333 --sunucu 41022 --json projeler/simple-present-temel-s2/uretim-tutanagi/cakisma-DUZ2.json`
Çıkış kodu: **0**. 01 13 örnek · 02 37 · 03 34 · 04 28; çakışma yok (`cakisma-DUZ2.txt`).

## 5. Bu işte bulunan arıza

| Arıza | Etki | Ne yaptım |
|---|---|---|
| `calistir.sh` satırı `/usr/bin/python3 uret.py >&2 && /usr/bin/python3 olay.py >&2` `set -e` altında `&&` zinciri olduğu için `uret.py` düşünce durmaz | kapak C ilk koşuda eski HTML'le (eski başlık, `BASIC`) ama yeni karakterle çekildi; çıkış 0 | kareye bakınca gördüm; `uret.py`'yi doğrudan koşup hatayı buldum (§1 #4), sonra yeniden çektim. Şablon düzeltmesi (`&&` yerine ayrı satır) bu istemin yazma alanında değil; şefe açık nokta |
| `uret.py`'yi `calistir.sh` dışında koşmak `tema_hf` işlemesini siler | ilk denemede kol b açık durağan kareleri temasız çıktı | iki kolda `ONIZLE_YALNIZ=1 … --tema acik` ile HTML'i geri kurdum; kol a ↔ kol b `proje/index.html` 05–08 bayt aynı, kareler piksel aynı |

## 6. Düzeltilmeyen maddeler

| Madde | Sınıf | Sebep |
|---|---|---|
| HV-17 "YEDESE" | ölçüt | güncel HV-17 bu dökümü beklenen davranış sayar |
| HV-19 küçük harf UTM | ölçüt | J2-OZET B2: bu paketin yayın bağları büyük harf |
| KS-1, KS-2 (düzen), KS-3 | ölçüt | güncel ölçüt: kısa kapakta geçersiz; HV-20a geçerli |
| DK-2 (altyazı 38 karakter) | ölçüt | kısada HV-25 (satır sayısı); karakter sınırı Nadir kararı |
| HV-22, KS-6, EK-8 | kanıt (C) | HV-22: kapı koştu, çıkış 0 (§4). `kapak-*-168.png` ve 18 maddelik klişe kontak bu istemin A listesinde yok (J2-OZET Sıra 5) |
| EK-4, EK-11 | kanıt (C) | önizleme adresinin gidiş zamanı şefin, dinleme kaydı Nadir'in işi. Dinlenecek yeni söz: c3 `çoğunlukla Simple Present` (Whisper 0,94) |
| EK-5b düşük not: kapak A `USUALLY = ALIŞKANLIK`, hikâye B `usually = alışkanlık` | şef kararı | J2-OZET A listesinde yok; ses "Alışkanlık işareti" der, kapak bir işaret sözcüğünü anlamına bağlar |
| Süre 26,68 > hedef 22–26 | açık nokta | "çoğunlukla" sözcüğü 0,95 sn ekledi; kabul sınırı 35 sn sağlandı |
| `calistir.sh` `&&` zinciri | açık nokta | §5 |

## 7. Değişen dosyalar

Kaynak: `BRIEF-S2.md`, `aciklama-b.md`, `ortak/kunye.js`, `ortak/kapak/{karakter,ana-kapak,ana-kapak-koyu}.png`, `ortak/anlatim/senaryo.json` (önceki oturum),
`sahneler/0{1,3,4,5,6,7,8}-*/yardim.py`, `sahneler/0{3,5,6,7}-*/uret.py`, SPEC 01, 03, 05, 06, 07, 08, `surumler.json` (`canAlici`, `ad`, `revizyonlar` r1).
Türetilmiş: `ortak/anlatim/{sureler,sozcukler,baslar,altyazi,sentez.wav.rapor}.json`, `METIN.md`, ses dosyaları (git dışı), `zaman.json`, sahne `proje/index.html`,
`zamanlar.json`, `olaylar.json`, `nesneler.json`, `devir.json`, `RAPOR.md` "Tema:" satırı (05–08), `k/` kareleri, kök `kapak*.png`, `hikaye*.png`.
Silinecekler: `~/Silinecekler/2026-11-15-duz2-0202S2/simple-present-temel-s2/` (`LISTE.md` satırları).

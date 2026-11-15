# J2 hükmü — simple-present-temel-s2 (kol a) · ÇIKTI jürisi · 15.11.2026 22:5x

**Jüri modeli: Claude Sonnet 5.5** (oturum kimliği 447a0910). Üretici oturum modeli: bilinmiyor (`S2-A-RAPOR.md`, `S2-C-RAPOR.md`
ve eski jüri dosyaları model yazmıyor; §1e tutanağa yazılmamış). Aynı model ailesi olup olmadığı **doğrulanamadı**.

**HÜKÜM: KALDI.** Kaldı 10 madde, kanıt yok 5 madde (47 maddenin 32'si geçti), ek bulgu 1.

## 1. Yöntem ve zaman (§1a, §1b)

| Konu | Ölçüm |
|---|---|
| Bakılan | son `senaryo.json`, `sentez.wav.rapor.json` (Whisper), `sozcukler.json`, `METIN.md`, `zaman.json`, `surumler.json`, `aciklama-a|b.md`, 27 kare Read ile açıldı: 5 kök PNG (kapak A/B/C, hikâye A/B), 5 koyu kapak/hikâye, 12 açık + 5 koyu sahne karesi (her sahneden en az 1 açık ve 1 koyu). Açılmayan sahne kareleri (sahne 04 için 20,2 ve 23 sn; `ara/`, `qa/`, `ka-*`) hükme girmedi |
| Paketin son içerik değişikliği | `git log`: 2026-11-15T22:38:38+03:00 (`bce68bd`, yalnız `aciklama-a|b|aciklama.md`); önceki içerik commit'i 20:06:16 |
| Eski jüri dosyaları | `juri/s2.dil.md` 18:56:21 · `juri/s2.kaynak-kural.md` 18:58:00 → son değişiklikten **3 sa 40 dk eski** (§1b ihlali, 22 kurala hiç bakmamış) |
| Bu jüri | 22:5x → son içerik değişikliğinden yeni. Düzeltmeden sonra yeniden koşmalı |
| Kareler | en yeni sahne karesi 20:01; sahne HTML'leri karelerden eski. Açıklama dosyalarının görsel karesi yok (metin olarak okundu) |

## 2. §2a — Kısa video (HV-1 … HV-23)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | `01-…-0.png`, `03-…-15.45.png`, `04-…-25.68.png`; koyu `kapak-a-koyu.png` | `ydspublishing` + `@ydspublishing` y 295–335, x 60; üç karede de var; giriş/çıkış animasyonu yok |
| HV-2 | evet | `senaryo.json` cümle 4 `ses: ogrenci` (`oPC5I9…`) | çağrı öğrenci sesi |
| HV-3 | evet | `senaryo.json` cümle 4; `sentez.wav.rapor.json` parça 8 | birebir "Dersin tamamı YDS Publishing YouTube kanalında." |
| HV-4 | evet | metin taraması (senaryo, altyazı, açıklamalar, sahne HTML, `ortak/*.js`) | "Tam ders" yok. Yalnız `RAPOR/SPEC` dosyaları yasağı anar (yüzey değil) |
| HV-5 | evet | aynı tarama | "dakika", "dk" yok |
| HV-6 | evet | sahne 03; `aciklama-a.md` satır 1 | kaydet ayrı sahnede ve ilk satırda |
| HV-7 | evet | `04-…-25.68.png` | kart x 60–960, y 622–1125 (≈ 900×503; hedef ≈ 920×518, kabul) |
| HV-8 | evet | `senaryo.json` | 6 sorunun 6'sı evet (sınavda çıkar, yanılgı, tek cümle, TR köprü, bağımsız anlaşılır, yeniden bakılır) |
| HV-9 | evet | `find … -name '*.mp4'` boş | |
| HV-10 | evet | 27 açılan kare | içerik y 295–1520; 0–280 ve 1570–1920 boş. Biçimsel kutu ölçümü koşmadı (bkz. HV-22) |
| HV-11 | evet | `zaman.json` | 4 sahne, 25,73 sn (hedef 22–26) |
| HV-12 | evet | `baslar.json` 1,00 sn; `zaman.json` sahne 1 = 3,0 sn | ilk söz tam 1,00 sn (sınırda); kanca ≤ 4 |
| HV-13 | evet | `zamanlar.json` `kart_sabit` 3,21 sn; `03-…-15.45.png`, `-19.png` | yer imi SVG, "Kaydet" yazısı var. 2 sn'lik piksel karşılaştırması için ara kare yok; çizelgeyle kabul edildi |
| HV-14 | evet | `04-…-22.7.png`, `-25.68.png` | "Bitmedi, gel." Fredoka 700; `@ydspublishing · YouTube` son karede |
| HV-15 | evet | `METIN.md` | "Bitmedi, gel." listede, bir kez |
| HV-16 | evet | `METIN.md` | "Bu kuralı kaybetme. Kaydet." listede, bir kez |
| HV-17 | **hayır** | `sentez.wav.rapor.json` parça 8: duyulan "YEDESE Publishing"; `ses-sozluk.json` `YDS → YeDeSe` | Söyleniş sözlükten (evet). Ama madde "Whisper 'YDS Publishing' duyuyor mu?" der; duyduğu "YEDESE". Standart §9 bunu bilinen sapma yazıyor; ölçüt ile gerçek çelişiyor |
| HV-18 | evet | `aciklama-a.md`, `aciklama-b.md` | ilk satır sabit; Reels açıklamasında bağ yok |
| HV-19 | **hayır** | `grep utm_campaign` (tüm paketler) | s2: `ING-YDT-GR-02-02-T` büyük harf, `utm_content=s2-a` doğru. Ama `02-04-ydt-temel-s2` ve `-s2b` (`aciklama.md`, `-a`, `-b`) 13 yerde küçük harf `ing-ydt-gr-02-04-t` |
| HV-20 | evet | `kapak-a|b|c.png`, `hikaye-a|b.png`, `aciklama-a|b.md` | kapak 3, hikâye 2, açıklama 2; altyazı yok; kanal katmanı var; üçünde karakter |
| HV-21 | evet | `hikaye-a.png`, `hikaye-b.png` + koyu | katman + kural özeti (`Usually, always, every day: Simple Present.` / `usually = alışkanlık`) + Kaydet; y 1150–1380 boş |
| HV-22 | **kanıt yok** | yalnız üretici `RAPOR.md` ("çakışma yok, 0 uyarı") | `cakisma-kapisi.mjs` jüri tarafından koşmadı (tarayıcı/port gerekir); sahne 05–08 statik kapıda ölçülemiyor. G gözü: kapak/hikâye karelerinde çakışma yok |
| HV-23 | evet | `sentez.wav.rapor.json` | benzerlik 1,00 (ses metniyle; §9'a göre ekran metniyle 0,97, yeniden hesaplanmadı) |

## 3. §2c — Kapak ve hikâye karesi (KS-1 … KS-10)

Ölçüt kapsamı: KS-1/2/3 ana ders kapağı için yazılmış (1920×1080 yatay, sarı zemin). Kısa kapağının ölçütü `huni-v2` §6'dır ve bu üç maddeyi
tanımlamaz. Madde metni uygulandı, hüküm "hayır"; kaldı sayılıp sayılmayacağı şefe: ölçüt belgesi kısa kapağı için ayrı madde istemeli.

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| KS-1 | hayır | `file`: 1080×1920 ×5 PNG | Kökte yalnız açık PNG. Koyu karşılıkları `sahneler/*/k/koyu/kapak-a|b|c-koyu.png` içinde, kökte `-koyu` dosyası yok |
| KS-2 | hayır | `kapak-a|b|c.png` | Kısa kapağı ana yazıyı sol %55'e değil ortaya (A, C) ya da sola (B) koyar. Rozet `YDT · BASIC`; kapak standardı `YDT · TEMEL` ister |
| KS-3 | hayır | kareler | Açık zemin krem, `#fece00` değil; koyu zemin siyaha yakın. C'deki karakterde 10 px krem çıkartma kenarı var (evet) |
| KS-4 | **hayır** | `aciklama-b.md` satır 3 ve 25: "Kapak: `kapak-b.png` (başlık ile aynı soru)" | Kapak B "ALWAYS VARSA HANGİ ZAMAN?" = B başlığı "Always varsa hangi zaman?". Kapak A ve C başlığı yinelemez (A, C: 2 ve 4 sözcük) |
| KS-5 | evet | `ortak/kapak/karakter.png` sha = ana ders; ana ders `KAYNAK.json` | model `nano-banana-2`; görselde yazı yok. s2 paketinde kendi `KAYNAK.json` yok (ana dersten). A ve B imagen değil, kalem çizimi |
| KS-6 | **kanıt yok** | `kapak-168.png` yok (yalnız ana derste var) | 168 px küçük görünüm dosyası üretilmedi; jüri yazma alanı dışı dosya üretmedi |
| KS-7 | evet | A "ALIŞKANLIK", B "HANGİ", C "İFADE / İŞARET" | İ ve Ş doğru çiziliyor. Not (düşük): C satır 1'de F–A aralığı hafif açık |
| KS-8 | evet | kareler | taşma ve binme yok (C'de chip ile karakter arasında ≈ 25 px boşluk) |
| KS-9 | evet | kareler | emoji yok |
| KS-10 | **hayır** | `KAYNAK.json`: "genç erkek, iri kıvırcık saç"; `senaryo.json` `kadro.ogrenci`: `cinsiyet: kadin` | Kapak C ve sahne 04'ün son kartı (`ana-kapak`) erkek karakter taşır. Çağrıyı söyleyen öğrenci kadın. A ve B'deki kalem figürü kadın (uyumlu) |

## 4. Ek maddeler (§2b, §1)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| EK-1 | evet | `METIN.md`, `ses_metni` | YDT ve BASIC seslendirilmiyor; YDS "YeDeSe" |
| EK-2 | evet | 27 açılan kare | emoji yok; yer imi ve otobüs çizim |
| EK-3 | evet | kapsam matrisi aşağıda | boş hücre yok (yön yalnız dikey: kısa videonun yatay sürümü yok) |
| EK-4 | kanıt yok | eski jüri DÜZELT dedi; "GEÇTİ" kaydı yok | önizleme adresinin Nadir'e gidip gitmediği tutanakta yok |
| EK-5a | evet | `02-…-11.8.png` | üstü çizili yalnız "şu an" (olumsuzlanan zarf); cümle yanlış gösterilmiyor. Hikâye B'de çizili öğe yok |
| EK-5b | **hayır** | sahne 03, hikâye A, kapak C (`Usually, always, every day: Simple Present.`) | Bağımsız doğrulama: `always` Present Continuous ile ("He is always losing keys"), `every day` Past Simple ile ("I walked every day") gelir; "üçü = Simple Present" istisnasız doğru değil. Düşük not: kapak A ve hikâye B `usually = alışkanlık` sözcüğü kavramla eşitler; videonun kendisi doğru söylüyor ("Alışkanlık işareti") |
| EK-5c | **hayır** | `senaryo.json` cümle 3 (ses + kart), hikâye A, kapak B ("ALWAYS VARSA HANGİ ZAMAN?"), kapak C ("TEK İŞARET") | Mutlak sunum. `bce68bd` yalnız açıklamalara "çoğunlukla" ekledi; video, kart ve kapaklar aynı kaldı → açıklama ile video çelişiyor |
| EK-6 | **hayır** | `senaryo.json` `giris.rozetler`; her karede rozet | `YDT · BASIC`; standart `YDT · TEMEL` (huni §9 açık iş). `04-…-22.7.png`'de aynı karede künye "BASIC", kart içi "TEMEL". Metin hatası yok: açıklamalarda tamlama, İ/I ve noktalama temiz |
| EK-7 | evet | 10 koyu kare | hepsi okunuyor (krem kart koyu zeminde kalıyor) |
| EK-8 | kanıt yok | yalnız `k/ara/kontak-ucus.png` (uçuş) | 18 maddelik klişe kontak sayfası yok |
| EK-9 | evet | `senaryo.json` | 1 soru, 4 sözcük |
| EK-10 | evet | `ses_metni` | tire, IPA, şık harfi, `ve,` yok |
| EK-11 | kanıt yok | dinleme kaydı yok | marka söylenişi D-0340'ta dinlendi; "Usually/goes" gibi yeni sözcükler için kayıt yok |
| EK-12 | evet | `zamanlar.json`; `sozcukler.json` | kart satırları söz başlangıcıyla aynı an (12,42 / 13,70); "Kaydet" yazısı 18,57, ses 18,47 |
| DK-2 (ek) | hayır | `02-…-11.8.png` | altyazı satırı 38 karakter ("Şu an değil, her sabah yedide kalkarım"), sınır 24. Dikey kalıp kısaya uygulanıyorsa kaldı |

Kapsam matrisi (dikey 1080×1920):

| Öğe | Açık | Koyu |
|---|---|---|
| Sahne 01 | 0 · 1,5 · 2,95 | 1,5 |
| Sahne 02 | 3,05 · 7,45 · 11,8 | 7,45 |
| Sahne 03 | 11,95 · 15,45 · 19 | 19 |
| Sahne 04 | 19,15 · 22,7 · 25,68 | 22,7 · 25,68 |
| Kapak A / B / C | kök PNG | `k/koyu/…-koyu.png` |
| Hikâye A / B | kök PNG | `k/koyu/…-koyu.png` |

## 5. Kaldı maddeleri — düzeltme önerisi (tek cümle)

| Kimlik | Öneri |
|---|---|
| HV-17 | Whisper beklentisini "YEDESE Publishing" olarak ölçüt belgesine yaz ya da kapıya `YDS → YeDeSe` eşlemesi ekle. |
| HV-19 | `02-04-ydt-temel-s2` ve `-s2b` açıklamalarında `utm_campaign` değerini `ING-YDT-GR-02-04-T` yap (13 yer). |
| KS-1…3 | Şef karar: kısa kapağı için ayrı ölçüt yaz ya da kökte `kapak-a|b|c-koyu.png` üret. |
| KS-4 | Kapak B'yi başlıktan ayır (ör. kapakta `ALWAYS = ?`), tam soru yalnız başlıkta kalsın. |
| KS-10 | Kapak C ve son kart için kadın karakterle yeni görsel üret ya da `kadro.ogrenci` ile ana kapağı birlikte yeniden kararlaştır. |
| EK-5b / EK-5c | Cümle 3 ve karta "çoğunlukla" ekle (`Usually, always, every day: çoğunlukla Simple Present.`), kapak C satır 2'yi `GÜÇLÜ İPUCU`, kapak B'yi `ALWAYS = ?` yap; ses yeniden sentezlenir, süre yeniden ölçülür. |
| EK-6 | `senaryo.json` rozetini ve 8 sahnenin rozetini `YDT · TEMEL` yap, kareleri yeniden çek. |
| HV-22, KS-6, EK-8 | Çakışma kapısını s2 için koştur; `kapak-168.png` ve klişe kontak sayfasını üret. |
| EK-4, EK-11, §1e | Tutanağa üretici modeli, görsel jüri GEÇTİ zamanını ve yeni sözcüklerin dinleme kaydını yaz. |

## 6. Ana derse geri besleme (`simple-present-temel`)

| Bulgu | Yer | Not |
|---|---|---|
| Karakter erkek, `kadro.ogrenci` kadın | `ortak/kapak/KAYNAK.json`, `ana-kapak*.png` | K22 ihlali ana kapakta |
| Rozet `YDT · BASIC` | `senaryo.json` satır 205 | huni §9 açık iş |
| "Türkçedeki er eki gibi: git-er, go-es" yanıltıcı | `senaryo.json` cümle 7 | Türkçe `-(e)r` her kişide zaman ekidir; İngilizce `-s` yalnız 3. tekil kişi. EK-5b |
| "Usually, always, every day: alışkanlık işareti." | cümle 4 | doğru, işaret olarak sunuyor (kısa video bunu "işaret"ten "kural"a çevirdi) |

Not: `bce68bd` "mutlak kural" düzeltmesi yalnız metin dosyalarını kapsadı; ses, kart ve kapaklar bu hükümde hâlâ kaldı.

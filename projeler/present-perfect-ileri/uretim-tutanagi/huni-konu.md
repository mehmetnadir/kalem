# present-perfect-ileri · huni v2 konu seçimi (istem HK-0206I, 15.11.2026)

Durum: TASLAK. Yalnız konu; senaryo, ses, sahne kodu yok. Makine biçimi: `huni-konu.json`.
Bağlayıcı standart: `dijital-anlatim/.claude/docs/huni-v2-standart.md` §5 (altı ölçüt, biçim tablosu), §9 (pilot).
Kaynak ders: `../ortak/anlatim/METIN.md` (7 cümle; cümle numaraları aşağıda bu tablodan), `../surumler.json` (`canAlici`, `amaclar`),
`../BRIEF.md` §4. Ana kapak metni: "AGO VARSA PERFECT YOK". Emsal: 02-02 temel S1 köprü · S2 sinyal sözcük · S3 yanlış–doğru.
Kardeş tarama (sözleşme huni konu satırları): var olan kısalar `present-perfect-temel-s1`, `present-perfect-cont-temel-s1`,
`present-perfect-cont-ileri-s1`, `simple-past-temel-s1`, `simple-past-ileri-s1`; 15.11 aday taslakları (`uretim-tutanagi/huni-konu.json`)
`present-perfect-temel`, `present-perfect-cont-temel`, `present-perfect-cont-ileri`, `simple-past-temel`, `simple-past-ileri`.

Ölçütler (standart §5): Ö1 sınavda çıkar · Ö2 öğrenci en çok burada yanılır · Ö3 kural tek cümleye sığar · Ö4 Türkçe köprüyle gösterilir ·
Ö5 dersi izlemeden anlaşılır · Ö6 sınav günü yeniden bakılır. Eşik: en az 4 evet.

**Sonuç: 5 aday. Boş biçim: sinyal sözcük.** Dersin sinyal sözcük konusu (yesterday, last year, ago → Simple Past) var olan
`simple-past-ileri-s1` kısasıyla çakışır (§4); yet / since sinyali s1 ve s2'nin içindedir. Ölçütleri geçen ve var olan kardeş kısayla
çakışmayan 6. konu bulunmadı; uydurulmadı.

## 1. Aday tablosu — içerik

| Sıra | Kimlik | Biçim | Taşıdığı bilgi | Kural özeti kartı | Kanca (ilk 1 sn) | Örnek EN | Örnek TR | Ana derste kaynak |
|---|---|---|---|---|---|---|---|---|
| 1 | s1 | tuzak | Aynı cümlede ago'lu yan Simple Past, yet'li yan Present Perfect alır; ago bütün cümleyi geçmişe çekmez. | Ago'lu cümlecik Simple Past, yet'li cümlecik Present Perfect. | Bir cümlede iki zaman olur mu? | The plane took off two hours ago, but it hasn't landed yet. | Uçak iki saat önce kalktı, ama henüz inmedi. | cümle 5 (örnek + kod), cümle 6 (öğrenci sorusu), cümle 7 son parça; `canAlici[0]` birebir |
| 2 | s2 | kural kartı | Since cümleciği geçmişteki başlangıç anını Simple Past ile söyler, ana cümle Present Perfect olur. | Since cümleciği Simple Past, ana cümle Present Perfect. | Since'ten sonra hangi zaman gelir? | Ever since the company launched its new app, the number of users has doubled. | Şirket yeni uygulamasını çıkardığından beri kullanıcı sayısı ikiye katlandı. | cümle 3 (örnek + kural birebir); `canAlici[2]` |
| 3 | s3 | köprü cümle | For tek başına Present Perfect işareti değildir: süre bugün sürüyorsa Present Perfect, bittiyse Simple Past gelir; Türkçe "otuz yıldır" ile "otuz yıl" bu ayrımı gösterir. | Süre bittiyse for olsa da Simple Past gelir. | For varsa hep Present Perfect mi? | Selim worked at this bank for thirty years, then he retired. | Selim bu bankada otuz yıl çalıştı, sonra emekli oldu. | cümle 4 (`has worked … for thirty years` = "otuz yıldır çalışıyor") + cümle 7 parça 3 (`Finished time: simple past`); `canAlici[4]`, amaç 4. Simple Past'lı for örneği ana derste yok |
| 4 | s4 | mini test | Süre bildiren sözden önce for, başlangıç noktasından önce since gelir; ago Present Perfect ile gelmez. | Süre ise for, başlangıç noktası ise since. | Üç saniyen var: for mu, since mi? | Selim has worked at this bank since 1995. | Selim 1995'ten beri bu bankada çalışıyor. | cümle 4 parça 4 ("Yıl adı verseydin since gelirdi"); `since 1995` BRIEF §4 sahne 04 görseli; `canAlici[3]` |
| 5 | s5 | yanlış–doğru | Have ya da has varsa fiilin ikinci hâli değil üçüncü hâli gelir: has taken, has took değil. | Have ya da has varsa fiilin üçüncü hâli gelir. | The plane has took off. Doğru mu? | The plane has taken off. | Uçak kalktı. | cümle 2 parça 2 (formül: have or has plus past participle); `took` cümle 5; `canAlici[1]` |

## 2. Aday tablosu — ölçütler ve sınav değeri

| Sıra | Ö1 | Ö2 | Ö3 | Ö4 | Ö5 | Ö6 | Evet | Sınavdaki değeri |
|---|---|---|---|---|---|---|---|---|
| 1 | evet | evet | evet | evet | evet | evet | 6 | YDT dilbilgisi boşluk doldurmada iki boşluklu zaman sorusu (bir yanda ago, öbür yanda yet); ders bunu "Üçüncü kök. Tuzak burada." diye verir (cümle 5). |
| 2 | evet | evet | evet | evet | evet | evet | 6 | YDT cümle tamamlama ve boşluk doldurmada "since + geçmiş an" kökü ana cümleyi Present Perfect'e bağlar; ders bunu ilk sınav kökü yapar (cümle 3). |
| 3 | evet | evet | evet | evet | evet | evet | 6 | YDT boşluk doldurmada "for + süre" kökü bitmiş bağlamla (then, before, emekli oldu) gelince şık Simple Past'tır; for'u Present Perfect işareti sanan öğrenci çeldiriciye düşer (ders cümle 4 for'u Present Perfect içinde öğretir, cümle 7 bitmiş zamanı ayırır). |
| 4 | evet | hayır | evet | evet | evet | evet | 5 | YDT dilbilgisi sorusunda for / since / ago boşluğu; ders "For süreyi söyler … Yıl adı verseydin since gelirdi" der (cümle 4). |
| 5 | hayır | evet | evet | hayır | evet | evet | 4 | Düşük: YDT şıkları çoğunlukla biçimce doğrudur; değer okuma ve şık tanımada düzensiz üçüncü hâli bilmektedir (cümle 2 formülü). |

## 3. Açıklamalar

- **s1 tuzak.** Dersin doruk noktası (çip `Trap 3 / 3`). Kapak yalnız "ago varsa Perfect yok" der; s1 aynı cümlenin öbür yanının
  Present Perfect kalacağını ekler. Öğrencinin sorusu (cümle 6, "ago varken de has landed diyemez miyiz?") bu karışıklığı gösterir.
  Ö4 köprü: Türkçede iki yan da "-dı" (kalktı, inmedi); İngilizce ikiye ayırır. Kart kapak satırının bir parçasını ("ago varsa") yinelemez.
- **s2 kural kartı.** Kural özeti ders cümle 3'ün kendisidir ("Since cümleciği Simple Past alır, ana cümle Present Perfect").
  Ö4 köprü: "-dığından beri" = since + Simple Past. Örnek cümle uzun (14 sözcük); senaryo yazarı dikeyde 3 satıra bölmeyi ölçer.
- **s3 köprü cümle.** Bir İngilizce söz, iki Türkçe karşılık: `for thirty years` = "otuz yıldır" (süren iş, `has worked`) ya da
  "otuz yıl" (biten iş, `worked`). Ders for'u yalnız Present Perfect içinde öğretir (cümle 4); öğrenci "for = Present Perfect" diye
  ezberler (kardeş `simple-past-ileri` `canAlici[4]` de "for, since, yet, already = Present Perfect tarafı" der). Bilgi dersin amacı 4
  ("bitmiş ve bitmemiş zaman ayrımını yapmak") ve `canAlici[4]` içindedir; ana derste geçmeyen yalnız Simple Past'lı örnek. Bu yüzden
  sözleşmenin "ana derste geçmeyen bilgi alt sıraya iner" kuralına girmez: çağrıdaki ders ilkeyi anlatır.
- **s4 mini test.** Üç şık: `for` · `since` · `ago` (doğru: `since`); `ago` çeldiricisi kapağa bağlanır. Ö2 hayır: ileri düzeyde
  for / since en çok yanılınan yer değildir.
- **s5 yanlış–doğru.** Formül (cümle 2) + dersin uçağı: `took` ikinci hâl, `has` sonrası `taken`. Ö1 ve Ö4 hayır; eşikte (4).

## 4. Eski kısa ve elenenler (var olan kardeş kısayla çakışan)

| Konu | Ölçüt | Durum | Gerekçe |
|---|---|---|---|
| Eski kısa `present-perfect-ileri-s1`: ago → Simple Past ("Ago gördün mü, Present Perfect elenir." · `She moved to Berlin two years ago.`) | 6 evet | elendi | Kapak metnini yineler (kapak "AGO VARSA PERFECT YOK", eski kısa kapağı "AGO VARSA SIMPLE PAST"). Standart §1 kural 7 ile son sahnede ana kapak görünür: bilgi bir kısada iki kez gelir. Aynı bilgi `simple-past-ileri-s1` ("AGO = PAST") kısasında da var. Bilginin ago'yu aşan parçası (yet'li yan) s1'e girdi. v1 çağrısı ("Tam ders kanalda · 6 dk") biçim sorunudur, konu sorunu değil. |
| Sinyal sözcük: yesterday, last year, ago → Simple Past (cümle 7 listesi; eski kısanın genişletilmiş hâli) | 6 evet | elendi | `simple-past-ileri-s1` ("AGO = PAST") var olan kısa; `simple-past-temel` s3 ve `simple-past-ileri` s5 taslakları aynı kural. Bilginin evi simple-past dersleridir. |
| Köprü: "otuz yıldır çalışıyor" = `has worked`, `is working` değil (cümle 4 TR–EN çifti) | 6 evet | elendi | `present-perfect-cont-temel-s1` ("İKİ SAATTİR = HAVE BEEN") aynı köprüyü ("-yor + süre") taşır; `present-perfect-temel` s1 taslağı ("Beş yıldır çalıyor: is playing değil, has played.") konunun evi olarak aldı. |
| Köprü: Türkçe "-dı" → Present Perfect ("ikiye katlandı" = `has doubled`) | 6 evet | elendi | `present-perfect-temel-s1` ("KAYBETTİM = I HAVE LOST") var olan kısa, aynı köprü. |

## 5. Kardeş taslak örtüşmesi (yalnız taslak; sözleşme kuralı: aday elenmez, burada yazılır)

| Aday | Kardeş taslak | Örtüşme | Not (şef kararı) |
|---|---|---|---|
| s1 | `simple-past-ileri` s1 yanlış–doğru ("Ago varsa Present Perfect değil, Simple Past.") · s3 sinyal sözcük ("Yet görürsen Simple Past değil, Present Perfect.") | s1 iki taslağı tek cümlede birleştirir; ikisi de orada ilk 3'te | `canAlici[0]` ("Ago varsa Simple Past, yet varsa Present Perfect") ve cümle 5 bu dersin; yet → Present Perfect bilgisinin evi bu derstir. `simple-past-ileri` s3 başka adaya geçebilir; s1 (ago) onun eski kısasıyla aynıdır. |
| s2 | `present-perfect-cont-ileri` s3 sinyal sözcük ("Since'li yan cümle geçmiş, ana cümle have been -ing.") | aynı yan cümle kuralı, ana cümle zamanı farklı; ikisi de ilk 3'te | Since cümleciği bu dersin ilk sınav kökü (cümle 3, amaç 2). İki kısa aynı haftaya konmaz ya da biri başka adaya geçer. |
| s3 | `simple-past-ileri` `canAlici[4]` ("for … = Present Perfect tarafı"; aday değil) | s3 bu ezberi düzeltir | Çelişki değil, ayrıntı: s3 yayınlanırsa simple-past-ileri kısaları for'u kesin Present Perfect işareti diye göstermez. |
| s4 | `present-perfect-temel` s2 tuzak ("Süre varsa for, başlangıç noktası varsa since.") · `present-perfect-cont-temel` s2 tuzak | aynı kural; ikisi de orada ilk 3'te | Temel ders for / since'i amaç 2 olarak taşır; evi temel derstir. s4 yalnız yedek kalır. |
| s5 | `present-perfect-temel` s4 yanlış–doğru ("Have ya da has'tan sonra fiilin üçüncü hâli gelir.") · `simple-past-ileri` s6 tuzak (began / begun) | aynı kural, aynı biçim; hepsi yayma sırasında | Biri yeter; evi formülü amaç 1 olarak taşıyan temel derstir. |

## 6. Koşul denetimi

| Koşul | Sonuç |
|---|---|
| İlk 3 adayın biçimi farklı | tuzak · kural kartı · köprü cümle (5 adayda 5 biçim, her biri bir kez) |
| Kapak metni aynen yinelenmez | 5 kural özetinden hiçbiri "AGO VARSA PERFECT YOK" ya da onun bir parçası değil |
| Kural özeti ≤ 9 sözcük, kısaltma yok | 8 · 8 · 8 · 7 · 9 sözcük; `V3`, `PP` yok |
| Her aday ≥ 4 evet | 6 · 6 · 6 · 5 · 4 |
| Ana dersle çelişki | yok; s3 ve s5 örnekleri yeni (yukarıda) |

## 7. Jüri bakacak

- **s1:** `It didn't land yet` Amerikan İngilizcesi konuşmasında geçer. Kısa bu cümleyi "yanlış" diye göstermemeli; sınav İngiliz normunu
  (yet → Present Perfect) bekler. Kanca bu yüzden yanlış cümle değil, sorudur.
- **s2:** Since cümleciğindeki fiil süren durum ise Present Perfect de alabilir (`since I have known him`). Kart kuralı geçmişteki
  başlangıç anıyla sınırlamalı (`launched`).
- **s3:** Kural kesin (bitmiş dönem + for → Simple Past). Jüri yeni EN örneğini ve "otuz yıl çalıştı" çevirisini okur; kart for'u
  "Present Perfect'e yasak" diye değil, "tek başına işaret değil" diye sunmalı.
- **s4:** Türkçe "-den beri" süreyle de kullanılır ("iki saatten beri" = `for two hours`). Kart Türkçe eke değil anlama (süre / başlangıç
  noktası) dayanır; "-den beri = since" eşlemesi yazılmamalı.
- **s5:** Kural kesin (take → took → taken).

# simple-present-ileri · huni v2 konu seçimi (ders başına 6 aday, ilk 3 üretilir)

Durum: TASLAK (istem HK-0202I, 15.11.2026). Senaryo, ses, sahne kodu ve render YOK; bu belge yalnız KONU seçer.
Bağlayıcı standart: `dijital-anlatim/.claude/docs/huni-v2-standart.md` §5 (altı ölçüt, biçim tablosu), §9 (pilot sonucu).
Ana ders: `../ortak/anlatim/senaryo.json` (7 cümle; numaralar aşağıda bu sırayla), `METIN.md`, `surumler.json`, `BRIEF.md`.
Ana dersin kapak metni: `YARIN ama WILL YOK` (`KAPAK-RAPOR.md`). Hiçbir aday bu metni aynen yinelemez.
Makine biçimi: `huni-konu.json` (aynı bilgi).

**Not:** `projeler/02-02-ydt-ileri/` aynı kimliği (`02-02-ydt-ileri`) taşıyan ayrı bir pakettir, senaryosu farklıdır. Bu seçim istemin
bağladığı `simple-present-ileri` senaryosuna dayanır.

Ana dersin cümleleri (kısa):

| # | Konuşan | Özü |
|---|---|---|
| 1 | öğretmen | `Uçak yarın dokuzda kalkıyor.` (kanca) |
| 2 | öğretmen | kural: he, she, it → `-s`; olumsuz ve soru: `does` + yalın fiil |
| 3 | öğretmen | `Although the sun looks small from here, it gives plants the energy they need.` → `Bağlaç var, zaman değişmez: gives.` |
| 4 | öğretmen | `Mike owns two cars, but he usually takes the bus …` → `Owns ve costs durum fiilidir: ing almaz.` |
| 5 | öğretmen | `Our flight takes off at eleven tomorrow morning …` → `Tarife kesin, Simple Present. Tomorrow tuzaktır.` |
| 6 | öğrenci | `Hocam, yarın dediği için will take off olmaz mıydı?` |
| 7 | öğretmen | tarife, program, takvim → Simple Present · `Will is for predictions and sudden decisions.` · `I know the answer. Not: I am knowing.` · `Kod: tarife varsa Simple Present, tahmin varsa will.` |

Ölçüt kısaltması (standart §5): Ö1 sınavda çıkar mı · Ö2 öğrenci en çok burada mı yanılır · Ö3 kural tek cümleye sığar mı ·
Ö4 Türkçe köprüyle gösterilir mi · Ö5 dersi izlemeden anlaşılır mı · Ö6 sınav günü yeniden bakılır mı. E = evet, H = hayır.

## 1. Adaylar (değer sırasıyla)

| Sıra | Kimlik | Biçim | Kural özeti kartı (TR, ≤ 9 sözcük) | Kanca (ilk 1 sn) | Kaynak (cümle) | Ö1 | Ö2 | Ö3 | Ö4 | Ö5 | Ö6 | Evet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | s1 | tuzak | Tarife kesinse yarın da olsa Simple Present. | `Tomorrow gördün, will mi yazacaksın?` | 1, 5, 6, 7 | E | E | E | E | E | E | 6 |
| 2 | s2 | yanlış–doğru | Durum fiili şu an olsa bile -ing almaz. | `I am knowing the answer.` (kırmızı) | 4, 7 | E | E | E | E | E | E | 6 |
| 3 | s3 | kural kartı | Tahmin ve ani kararda will kullan. | `Yarın var, will doğru. Neden?` | 7 | E | H | E | E | E | E | 5 |
| 4 | s4 | köprü cümle | Türkçedeki -yor eki her zaman -ing değildir. | `Kalkıyor: is taking off mu, takes off mu?` | 1, 5 | E | E | E | E | E | E | 6 |
| 5 | s5 | mini test | Now gelse bile own, know -ing almaz. | `Mike ___ two cars now.` + `Üç saniye!` | 2, 4, 7 | E | E | E | H | E | H | 4 |
| 6 | s6 | kural kartı | Although gelse de genel gerçek Simple Present kalır. | `Although gelince zaman değişir mi?` | 3 | E | H | E | E | E | H | 4 |

İlk 3 adayın biçimi farklıdır: tuzak · yanlış–doğru · kural kartı. Sıra yalnız "evet" sayısından gelmez. Sırayı 3 etken belirler:
ölçüt sayısı, ana dersteki ağırlık (`canAlici` sırası) ve öteki adaylarla örtüşme. s4 6 "evet" alır, ama örneği s1 ile aynı uçak
cümlesidir; s3 yeni bilgi taşır. Bu yüzden s3 üretilecek üçlüdedir.

## 2. Aday ayrıntısı

### s1 · tuzak — tarife varsa `tomorrow` will istemez

- Bilgi: Tarife, program ya da takvim kesinse gelecek de Simple Present ile söylenir; `tomorrow` sözcüğü will gerektirmez.
- Örnek: EN `Our flight takes off at nine tomorrow.` · TR `Uçuşumuz yarın dokuzda kalkıyor.`
- Kaynak: cümle 5 (kısaltılmış; saat cümle 1'den) · cümle 6 (öğrencinin yanılgısı) · cümle 7 (`Tarife, program, takvim kesinse Simple Present.`).
- Tuzak + işaret: tuzak `tomorrow`; işaret sözcüğü tarife (`flight`, saat `at nine`).
- Sınavdaki değeri: `canAlici[0]` ve `[1]` bu bilgidir. Kanıt: cümle 6'da öğrenci tam bu yanılgıyı yapar. Soru tipi: zaman seçimi boşluk
  doldurma (şıklarda will çeldiricisi).
- Eski kısa: `simple-present-ileri-s1` aynı konuyu taşır (bkz. §3).

### s2 · yanlış–doğru — `I am knowing` yok

- Bilgi: `know` ve `own` gibi durum fiilleri şu anı anlatsa bile -ing almaz.
- Yanlış → doğru: `I am knowing the answer.` → `I know the answer.` · Neden: `know` durum fiilidir.
- Örnek: EN `I know the answer.` · TR `Cevabı biliyorum.`
- Türkçe köprü: Türkçe `biliyorum` `-yor` eki taşır; öğrenci bu yüzden `-ing` yazar.
- Kaynak: cümle 4 (`Owns ve costs durum fiilidir: ing almaz.`) · cümle 7 (`I know the answer. Not: I am knowing.`).
- Sınavdaki değeri: `canAlici[2]`. Kanıt: cümle 7 aynı yanlış–doğru çiftini verir. Soru tipi: boşluk doldurma, -ing şıkkı çeldiricidir.

### s3 · kural kartı — will'in işi: tahmin ve ani karar

- Bilgi: will gelecekteki tahmin ve konuşma anında verilen karar için kullanılır; kesin tarife için Simple Present kullanılır.
- Örnek: EN `I think it will rain tomorrow.` · TR `Bence yarın yağmur yağacak.` **[YENİ: ana derste will örnek cümlesi yok]**
- Türkçe köprü: `yağacak` (`-acak`) ↔ `will rain`; s1'deki `kalkıyor` ↔ `takes off` ile karşıtlık.
- Kaynak: cümle 7 (`Will is for predictions and sudden decisions.` · `Kod: tarife varsa Simple Present, tahmin varsa will.`).
- Ö2 hayır: öğrencinin asıl yanılgısı will'i fazla kullanmaktır (s1); bu kısa doğru kullanımı öğretir.
- Sınavdaki değeri: dersin kapanış kodu bu karşıtlıktır. Kanıt: cümle 7. Soru tipi: gelecek anlamında will ile Simple Present arasında seçim.

### s4 · köprü cümle — bir `kalkıyor`, iki İngilizce zaman

- Bilgi: Türkçe `kalkıyor` iki İngilizce zamana karşılık gelir: şu an olan iş Present Continuous, tarifeli gelecek Simple Present.
- Köprü: `Uçak şu an kalkıyor.` → `The plane is taking off now.` **[YENİ]** · `Uçak yarın dokuzda kalkıyor.` → `The plane takes off at nine tomorrow.`
- Örnek (ana): EN `The plane takes off at nine tomorrow.` · TR `Uçak yarın dokuzda kalkıyor.`
- Kaynak: cümle 1 (dersin kancası: Türkçe cümle → `İngilizcede hangi zamanla kurarsın?`) · cümle 5. `şu an` tarafı ana derste yok.
- Örtüşme: örnek s1 ile aynı aileden; s1 ile aynı haftada yayınlanmaz.
- Sınavdaki değeri: Türkçe `-yor` eki öğrenciyi `-ing`'e çeker. Kanıt: cümle 1. Soru tipi: Türkçeden İngilizceye çeviri.

### s5 · mini test — `now` görünce -ing yazma

- Bilgi: `now` sinyali durum fiilini -ing'e çevirmez; he, she, it öznesi fiile `-s` ekler.
- Test: `Mike ___ two cars now.` · a) `owns` · b) `is owning` · c) `own` · Cevap: a. Sayaç 3 sn.
- Örnek: EN `Mike owns two cars now.` · TR `Mike'ın şu an iki arabası var.`
- Kaynak: cümle 2 (`he, she, it takes s`) · cümle 4 (`Mike owns two cars`) · cümle 7 (`now gelse bile ing almaz`).
- Ö4 hayır: Türkçe karşılık (`arabası var`) `-yor` taşımaz; köprü öğretici değil. Ö6 hayır: test biçimi tek seferlik meydan okumadır.
- Örtüşme: s2 ile aynı kural; s5 `now` tuzağını ve `-s` uyumunu ekler.
- Sınavdaki değeri: boşluk doldurma soru tipinin 3 şıklı kısaltmasıdır. Kanıt: cümle 7 `now gelse bile`.

### s6 · kural kartı — although zamanı değiştirmez

- Bilgi: although cümleyi uzatır, ama genel gerçeğin zamanını değiştirmez; ana cümle Simple Present kalır.
- Örnek: EN `Although the sun looks small from here, it gives plants the energy they need.` · TR `Güneş küçük görünse de bitkilere gereken enerjiyi verir.`
- Türkçe köprü: `görünse de` ↔ `although`; `verir` (geniş zaman) ↔ `gives`.
- Kaynak: cümle 3 (`Bağlaç var, zaman değişmez: gives.`). `genel gerçek` adı ana derste yok **[YENİ]**.
- Ö2 hayır: öğrenci bağlaçtan sonra zamanı seyrek değiştirir. Ö6 hayır: sınav günü bakılacak kural değil.
- Sınavdaki değeri: ana dersin amacı 4. Kanıt: cümle 3. Soru tipi: bağlaçlı uzun kök ve bilimsel olgu anlatan okuma parçası.

## 3. Eski kısa — `simple-present-ileri-s1`

| Alan | Değer |
|---|---|
| Konu | tarifeli gelecek: `Tarife varsa will deme.` · `Our flight takes off at nine tomorrow.` · `Tarife kesin: gelecek anlamı olsa da Simple Present.` |
| Biçim | v1, 3 sahne (kapak-kanca → örnek → çağrı), 19,25 sn ses, mp4 20,23 sn |
| Ölçüt | 6/6 geçer → listede **s1** |
| v2 eksiği | kaydet sahnesi yok; çağrı öğretmen sesiyle; seste `Tam ders`, ekranda `6 dk` var (standart §1 kural 4, 5 ihlali) |

v2 çeviriminde konu korunur, biçim tuzak olur, kaydet sahnesi eklenir. Eski kısanın cümle 2 içeriği s1 değer sahnesine uyar; sesin yeniden
kullanılıp kullanılmayacağı senaryo adımında ölçülür (hesaplamadan önce 3 soru).

## 4. Elenen konular

| Konu | Neden |
|---|---|
| Olumsuz ve soru: `does` + yalın fiil (cümle 2) | 3 evet (Ö1 H: dil sınavı bu temel biçimi doğrudan sormaz · Ö4 H: Türkçede `does` karşılığı yok · Ö6 H). Ayrıca 02-02 temel S3 aynı konu |
| `usually` → Simple Present sinyali (cümle 4) | 02-02 temel S2 ile aynı konu; ileri derste kural olarak söylenmez, yalnız örnekte geçer |
| `when`, `if`, `until` + gelecek → Simple Present | ölçütleri geçer, ama **ana derste yok**. Kısa izleyiciyi derse çağırır; derste bulunmayan bilgi huni vaadini bozar |

## 5. Jüri bakacak (dilbilgisi)

| Aday | Konu | Not |
|---|---|---|
| s1 | `will take off` sertliği | Tarife için `will take off` dilbilgisi olarak yanlış değildir; sınavın beklediği doğal biçim Simple Present'tir. Kanca soru sorar, "yanlış" demez. Ana ders cümle 7'deki `Hayır.` sertliği kısada yinelenmez |
| s2 | `cost` | `cost` süreç anlamında -ing alabilir (`The delays are costing us money.`). Kartta yalnız `know` ve `own` yer alır |
| s3 | will'in kapsamı | will söz, teklif ve gelecek olgu için de kullanılır; kart "yalnız" demez. Kanıtlı tahminde `be going to` da kullanılır (ana derste yok, kısa söylemez) |
| s4 | `is taking off at nine tomorrow` | Present Continuous kişisel düzenleme için gelecek bildirebilir. Kısa iki cümleyi `now` ve `at nine tomorrow` ile açıkça ayırır |
| s6 | bağlaç genellemesi | Ana dersin `Bağlaç var, zaman değişmez` sözü `when`, `if`, `until`, `as soon as` için geçerli değildir: bu bağlaçlarla gelecek Simple Present ile verilir. Kart yalnız although cümlesini anlatır |

s5'te jüri notu yok: tek doğru şık var; b) durum fiili hatası, c) özne uyumu hatası.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (istem HK-0202I).

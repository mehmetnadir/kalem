# present-perfect-cont-ileri · huni v2 konu seçimi (6 aday)

Durum: TASLAK (istem HK-0209I, 15.11.2026). Bu belge yalnız KONU seçer; senaryo, ses ve sahne yok.
Bağlayıcı standart: `dijital-anlatim/.claude/docs/huni-v2-standart.md` §5 (altı ölçüt, biçim tablosu), §9 (pilot).
Ana ders: `../ortak/anlatim/senaryo.json` (7 cümle; numaralar `../ortak/anlatim/METIN.md` tablosuyla aynı), `../surumler.json`,
`../BRIEF.md`. Ana kapak metni: "SÜREÇ mi SONUÇ mu?" (hiçbir aday bu metni aynen yinelemez).
Üretim sırası: s1–s3 bu tur (üç biçim ayrı); s4–s6 yayma adımında. Makine biçimi: `huni-konu.json`.

Ana dersin 7 cümlesi (kaynak sütunu bu numaraları kullanır; `canAlici` ve amaç numaraları `senaryo.json` `meta` listesinde 1'den sayılır):

| # | Konuşan | Özü |
|---|---|---|
| 1 | öğretmen | kanca: `Süreç mi, sonuç mu?` |
| 2 | öğretmen | form: `Have or has, plus been, plus the -ing form.` · süre ipuçları ve iki tuzak duyurusu |
| 3 | öğretmen | `Since the school changed the timetable, students have been complaining.` · `Since, plus a simple past clause.` |
| 4 | öğretmen | `I have been reading this novel all week, but I have only finished two chapters.` · `Sonuç ve sayı, have finished.` |
| 5 | öğretmen | `We have known each other since we were at primary school.` · `Know is a state verb.` |
| 6 | öğrenci | `Hocam, have been knowing, olmaz mıydı?` |
| 7 | öğretmen | `Durum fiilleri -ing almaz.` · `Türkçede -yor süreci, -di sonucu söyler.` · `süreç varsa been var, sonuç varsa been yok` |

## 1. Adaylar (değer sırasıyla, 1 = en değerli)

| Sıra | Kimlik | Biçim | Taşıdığı bilgi | Kural özeti kartı (sözcük) | Kanca (ilk 1 sn) | Örnek EN | Örnek TR | Kaynak |
|---|---|---|---|---|---|---|---|---|
| 1 | s1 | köprü cümle | Süreyle söylenen Türkçe `-yor` süreçtir ve `have been -ing` olur; `-di` sonuçtur ve `been` almaz. | -yor süreçtir: been -ing; -di sonuçtur: been yok. (8) | "Bütün hafta okuyorum" İngilizcede nasıl? | I have been reading this novel all week, but I have only finished two chapters. | Bütün hafta bu romanı okuyorum, ama yalnızca iki bölümü bitirdim. | cümle 4, 7 |
| 2 | s2 | yanlış–doğru | `know` gibi durum fiilleri Present Perfect Continuous'a girmez; doğrusu `have known`. | Durum fiilleri -ing almaz: know, like, belong. (7) | Ekranda kırmızı: `We have been knowing each other.` Ses: "Have been knowing, doğru mu?" | We have known each other since we were at primary school. | İlkokuldan beri birbirimizi tanıyoruz. | cümle 5, 6, 7 |
| 3 | s3 | sinyal sözcük | `since` ile başlayan yan cümle geçmiş zamanda kalır; ana cümle `have been -ing` alır. | Since'li yan cümle geçmiş, ana cümle have been -ing. (9) | Since görünce ana cümle hangi zaman? | Since the school changed the timetable, students have been complaining. | Program değişeli beri öğrenciler yakınıyor. | cümle 3 |
| 4 | s4 | tuzak | Bitmiş iş sayıyla verilirse (`two chapters`) cümle sonuçtur; `been` düşer, `have` + fiilin üçüncü hâli gelir. | Sayı varsa been yok: have ve fiilin üçüncü hâli. (9) | "İki bölüm bitirdim": have been finishing mi? | I have only finished two chapters. | Yalnızca iki bölümü bitirdim. | cümle 4 |
| 5 | s5 | mini test | İki boşluklu sınav kökü: `since` yan cümlesi geçmiş zaman, `know` ana cümlede `have known`. | Since'li yan cümle geçmiş; know -ing almaz. (7) | Üç saniye: `We ___ each other since we ___ at primary school.` | We have known each other since we were at primary school. | İlkokuldan beri birbirimizi tanıyoruz. | cümle 3, 5 |
| 6 | s6 | kural kartı | Present Perfect Continuous üç parçadan kurulur: `have/has` + `been` + `-ing`; bir parça eksikse cümle yanlıştır. | Üç parça şart: have ya da has, been, -ing. (9) | Ekranda kırmızı: `Students have complaining.` Ses: "Eksik ne?" | Students have been complaining. | Öğrenciler yakınıyor. | cümle 2, 3 |

## 2. Altı ölçüt (standart §5; en az 4 "evet")

| Sıra | Sınavda çıkar mı | En çok burada mı yanılır | Tek cümleye sığar mı | Türkçe köprü | İzlemeden anlaşılır mı | Sınav günü bakılır mı | Evet | Sınavdaki değeri (kanıt) |
|---|---|---|---|---|---|---|---|---|
| 1 | evet | evet | evet | evet | evet | evet | 6 | Dilbilgisi boşluk doldurma ve çeviri sorularında süreç–sonuç ayrımı belirleyicidir; ana ders bu ayrımı kapanış kuralı yapar (cümle 7, `canAlici` 1 ve 5, amaç 3). |
| 2 | evet | evet | evet | evet | evet | evet | 6 | Durum fiili + `-ing` şıkkı tipik çeldiricidir; ana dersin tek tuzağı ve öğrenci sorusu budur (cümle 5–7, `canAlici` 4, amaç 4). |
| 3 | evet | evet | evet | evet | evet | evet | 6 | `Since` yan cümleli boşluk doldurma kökü sınavın sık kalıbıdır; ana ders bir örneğin tamamını buna ayırır (cümle 3, `canAlici` 2, amaç 2). |
| 4 | evet | hayır | evet | evet | evet | evet | 5 | Sayı içeren kökte (`two chapters`) `have been -ing` çeldiricisini eler; ana ders bunu yarım cümleyle söyler (cümle 4: `Sonuç ve sayı, have finished.`). |
| 5 | evet | evet | hayır | hayır | evet | evet | 4 | İki boşluklu dilbilgisi sorusunun biçimini birebir taşır; iki çeldirici öğrencinin iki yanlışıdır (cümle 3 ve 5). |
| 6 | evet | hayır | evet | hayır | evet | evet | 4 | Biçim ve özne uyumu (`have`/`has`) her kökte geçer; ileri seviyede ayırt edici değildir (cümle 2, amaç 1). |

## 3. Açıklama

**s1 · köprü cümle.** Türkçe söz `okuyorum` (süreyle) ve `bitirdim` iki İngilizce karşılığa ayrılır: `have been reading` ve `have finished`.
Ana dersin öz kuralını (cümle 7) Türkçe köprüyle gösterir; kapak metnini yinelemez. Eski kısanın konusu budur (§4).
Kanca alternatifi: "Bütün hafta okuyorum: I am reading mi?" (yaygın yanlış; `I am reading` ana derste yok, jüri bakacak).

**s2 · yanlış–doğru.** Yanlış cümle `We have been knowing each other.` → doğrusu `We have known each other …` → neden: `know` durum fiilidir.
Ana dersteki öğrenci sorusunun (cümle 6) cevabıdır. Türkçe köprü: `tanıyoruz` `-yor` taşır ama İngilizcede `-ing` yoktur.

**s3 · sinyal sözcük.** İşaret sözcüğü `since`; Türkçe köprü `-eli beri` (`değişeli beri`). Yan cümle geçmiş zaman (`changed`), ana cümle
`have been complaining`. Kural ana derste aynen var (cümle 3: `Since, plus a simple past clause. Ana cümlede have been ve -ing gelir.`).

**s4 · tuzak.** Tuzak: `been` görünce bütün cümleyi süreç sanmak. İşaret: bitmiş sayı (`two chapters`). Ana ders aynı cümlede süreci ve
sayıyı yan yana koyar (cümle 4). s1 ile aynı örneği paylaşır; s1 `-yor`/`-di` köprüsünü, s4 sayı işaretini öğretir.

**s5 · mini test.** Kök: `We ___ each other since we ___ at primary school.` Şıklar: A) `have known / were` (doğru) · B) `have been knowing /
have been` · C) `know / are`. 3 sn sayaç, sonra cevap ve iki satır neden. s2 ile s3'ü tek soruda birleştirir.

**s6 · kural kartı.** Kart: `have / has` + `been` + `-ing`; tek örnek `Students have been complaining.` Kanca yanlışı ana derste yoktur
(öğretim amaçlı eksik parça). İleri seviyede değeri en düşük aday; listeyi dolduran son seçenektir.

## 4. Eski kısa: `present-perfect-cont-ileri-s1`

| Alan | Değer |
|---|---|
| Konu | süreç–sonuç: `been reading` ↔ `have finished` (ana ders cümle 4 örneği) |
| Biçim | v1, 3 sahne (kapak-kanca → `PROCESS / RESULT` iki sütun kartı → çağrı), 24,93 sn |
| Ölçütler | konu ölçütleri geçer (s1 ile aynı 6 evet) → listede **s1** olarak var |
| Olduğu gibi kullanılamaz | kanca `Sınav tek şey sorar: süreç mi, sonuç mu?` kapak metnini yineler · çağrı yasak çağrı sözünü ve süre sözünü söyler (standart §1 kural 4–5) · kaydet sahnesi ve kanal katmanı yok |
| Yeni biçim | köprü cümle (`-yor` / `-di`); kanca kapak sorusu yerine Türkçe cümle sorusu |

## 5. Jüri bakacak (emin olunmayan kurallar)

1. s1: `-di` her zaman Present Perfect değildir; geçmiş zaman sözcüğü varsa (`dün`, `geçen hafta`) Simple Past olur. `-yor` de durum fiilinde
   (`tanıyoruz`) `been -ing` olmaz. Kısa bu iki istisnayı söylemezse aşırı genelleme riski vardır.
2. s2: `like`, `belong` ana derste seslendirilmez (yalnız `meta.canAlici` 4). `think`, `have` gibi fiiller eylem anlamında `-ing` alabilir
   (`I have been thinking`); kısa örneği `know` ile sınırlı tutmalı.
3. s3, s5: `since` + Present Perfect yan cümle de dilbilgiseldir (`since I have known her`). "Yan cümle geçmiş zaman" kuralı sınav kökü
   kalıbı olarak doğrudur, mutlak kural değildir.
4. s4: `I have been reading three books` eşzamanlı okuma anlamında kabul görebilir. Kısa yalnız bitmiş sayıyla (`finished two chapters`)
   kalmalı.

## 6. Koşul denetimi

| Koşul | Durum |
|---|---|
| İlk 3 adayın biçimi farklı | köprü cümle · yanlış–doğru · sinyal sözcük |
| Kapak metni aynen yinelenmez | hiçbir kanca ve kural özeti `Süreç mi, sonuç mu?` demez |
| Kural özeti ≤ 9 sözcük, Türkçe, kısaltma yok | 8 · 7 · 9 · 9 · 7 · 9 sözcük; `V3` yerine "fiilin üçüncü hâli" |
| Her aday ≥ 4 evet | 6 · 6 · 6 · 5 · 4 · 4 |
| Ana dersle çelişki | yok; istisnalar §5'te jüriye |

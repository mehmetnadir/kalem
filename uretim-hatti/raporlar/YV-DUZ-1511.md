# YV-DUZ — 12 dersin YouTube yayın verisi: jüri bulguları + dersler arası tutarlılık · 15–16.11.2026

İstem: `uretim-hatti/istemler/YV-DUZ.md`. Üretici: Claude Opus 5.5 (`claude-opus-5-5`). Commit yok (şef atar).

| Ölçü | Değer |
|---|---|
| Hüküm maddesi (hayır + öneri taşıyan uyarı/not) | 65 |
| Sınıf a / b / c / d | 15 / 3 / 13 / 34 |
| Düzeltilen ders | 9 (+ 8 dikey eş) |
| Düzeltilen kapak | 1 ders (`simple-present-ileri`): 4 PNG + 168 px |
| Tutarlılık betiği, eski durum | 18 sorun (çıkış 1) |
| Tutarlılık betiği, son durum | 0 sorun, kilitli pakette 2 (çıkış 0, `--kilitli` ile) |
| Dokunulmayan | `simple-present-temel{,-dikey}`, `02-04-ydt-temel-dikey`, bütün kısalar |

**UYARI:** `uretim-hatti/betikler/yv-tutarlilik.py` DOSYASI YAZILMADI. Yazma kapısı (`write-size-gate.sh`, 15+ satır `.py`) engelledi;
istem alt ajanı, agy-filo'yu ve kapı bayrağını yasaklıyor. Betik metni hazır: `~/.cache/yv-duz/yv-tutarlilik.py.taslak` (stdin ile koşuldu;
aşağıdaki çıktılar bu metindendir). Şef onayıyla tek `Write` ile yerine konur.

**UYARI:** İçerik değişen 9 pakette YVJ jürisi yeniden koşmalı (`juri-olcutleri.md` §1b). `simple-present-ileri` kapağı için kapak jürisi de.

## 1. Hüküm dökümü (madde 1)

Sınıf: a = yayın verisi metni · b = kapak görselindeki yazı · c = dersin kendisi (ses/sahne) · d = ölçüt ya da kanıt.
Durum: ✔ düzeltildi · ✖ düzeltilmedi (gerekçe) · → rapor (kilitli paket) · açık (c/d).

| # | Ders | Madde | Bulgu | Öneri (jüri) | Sınıf | Durum |
|---|---|---|---|---|---|---|
| 1 | 02-04 temel | YV-8 | srt türetici yok, json/srt karşılaştırılamadı | türetici + test ya da ölçütü daralt | d | açık |
| 2 | 02-04 temel | §3 Yer | sağ üst değil sol alt | standardı güncelle | d | standart §3 artık sol alt (yer.json); hüküm eski metne dayanır |
| 3 | 02-04 temel | §3 Ses | mp4 yok | mp4 sonrası enerji ölçümü | d | açık |
| 4 | 02-04 temel | Ek | giriş kayması açıklamaya yansımamış | damgaları +3 sn kaydır | d | sözleşme §3: API yeniden yazar; veri ders zamanı kalır |
| 5 | 02-04 temel | Ek | dikey bildirim yeri ölçülmemiş | dikey ölçüm | d | açık |
| 6 | 02-04 temel | Ek | `ortak/youtube/kanal.json` yok | — | d | açık |
| 7 | simple-present-temel | YV-8 | srt kanıtı yok | panel türetici + test | d | açık |
| 8 | simple-present-temel | §3 Yer | sağ üst değil | standart güncellensin | d | standart güncel (sol alt) |
| 9 | simple-present-temel | §3 Zaman | %30 ile "ilk 30 sn yok" çakışır | standarda cümle | d | açık (standart) |
| 10 | simple-present-temel | YV-1 not | `02-02-ydt-ileri` ile aynı başlık | ileri alt başlık alsın | a | ✔ (ileri başlığı değişti) |
| 11 | simple-present-temel | YV-6 not | "üç örnekle" ama dört öğe sayılır | — | a | → rapor (§7) |
| 12 | simple-present-temel | not | "er eki gibi", canAlici "geniş zaman eki = s", always kodu | ders jürisine | c | → rapor (§7) |
| 13 | present-continuous | YV-6 hayır | gönderi görseli "GİDİYORUM = AM GOING", "-yor → -ing" | kapakta "-yor → -ing" kaldır, "= I AM GOING" | c | ders c7 aynı denkliği söyler → kapağa dokunulmadı (§4) |
| 14 | present-continuous | §3 Yer | kare yok, BookFlip çakışması ölçülmedi | 3 kare; gerekirse t 31,44 | d | açık |
| 15 | present-continuous | şef 1 | dikey Shorts; sabit yorum damga vaadi | şef kararı | d | açık |
| 16 | present-continuous | şef 2 | ileri ile aynı başlık | ileri alt başlık | a | ✔ |
| 17 | present-continuous | şef 3 | c7 "-yor gibi", canAlici, c2 "aynısını yapar" | ders jürisine | c | açık (§4) |
| 18 | present-continuous | şef 4 | `surumler.json` kodu `ING-YDT-GR-01-PC` | — | d | yazma alanı dışı |
| 19 | present-continuous-ileri | YV-6 hayır | "Present Continuous'u" (ek okunuşa aykırı, temelle tutarsız) | "'ı" | a | ✔ |
| 20 | present-continuous-ileri | YV-1 not | temel ile aynı başlık | alt başlık | a | ✔ |
| 21 | present-continuous-ileri | YV-6 not | gönderide tırnaksız örnekler | tırnak | a | ✔ |
| 22 | present-continuous-ileri | YV-9 not | `karakter.png` kol–gövde arası beyaz üçgen | — | b | ✖ görsel (yazı değil); "görsel değişmez" kuralı |
| 23 | present-continuous-ileri | §1c | c3 "while tam anı", c7 "-ing almaz", "always + -ing şikâyettir" | ders jürisine | c | açık (§4) |
| 24 | present-continuous-ileri | B-4 | yer kanıtı yok | mp4 sonrası | d | açık |
| 25 | present-continuous-ileri | B-5 | ses kanıtı yok | mp4 sonrası | d | açık |
| 26 | simple-present-ileri | YV-9 hayır | kapak "YARIN ama WILL YOK" mutlak | kapak metnini yenile | b | ✔ "YARIN / WILL mi?" (§3) |
| 27 | simple-present-ileri | N-1 | temel ile aynı başlık | "Simple Present: tarife ve durum fiilleri" | a | ✔ (farklı sözle, §2 gerekçe) |
| 28 | simple-present-ileri | N-2 | katalog `proje: 02-02-ydt-ileri` | şef kararı | d | açık |
| 29 | simple-present-ileri | N-4 | dikey Shorts sayılır | — | d | açık |
| 30 | simple-present-ileri | YV-9 | c6–c7 "Hayır." kapsam (EK-5c) | — | c | açık (§4) |
| 31 | 02-03 temel | YV-6 hayır | bölüm "Believe, recommend, have" ("have -ing almaz" okunur) | "have (sahip olmak)" | a | ✔ |
| 32 | 02-03 temel | YV-6 not | gönderide "çoğunlukla" kapsamı belirsiz | "usually ise çoğunlukla" | a | ✔ |
| 33 | 02-03 temel | §3 | çakışmama kanıtı yok | birleştirme sonrası kare | d | açık |
| 34 | 02-03 temel | bilgi | `METIN.md` zamanları bayat | — | d | açık |
| 35 | 02-03 temel | bilgi | ders sayfası 404 | yayından önce aç | d | açık |
| 36 | 02-03 temel | bilgi | dikey paket yok | — | d | açık |
| 37 | 02-03 temel | YV-6 bağlam | c15 özet "Believe ve have gibi fiiller" (sınırsız have) | — | c | açık (§4) |
| 38 | present-perfect-temel | Not 1 | dikey Shorts | şef kararı | d | açık |
| 39 | present-perfect-temel | Not 2 | %30 / ilk 30 sn çakışması | standarda cümle | d | açık |
| 40 | present-perfect-temel | Not 3 | kapak "KAYBETTİM = HAVE LOST" -dı ↔ PP denkliği | kapak jürisi bakar | b | ✖ (§3 gerekçe) |
| 41 | present-perfect-temel | §1c | c7 "for ve since süre", "just ve already yeni biten iş" | senaryo jürisine | c | açık (§4) |
| 42 | present-perfect-temel | §3 Yer | jüri `yer.json`ı bulamadı | G bakar | d | açık |
| 43 | present-perfect-ileri | YV-6 hayır | "ago içeren cümlede PP kullanılmaz" dersin c5 örneğiyle çelişir | yeni satır 1 | a | ✔ |
| 44 | present-perfect-ileri | Ek 1 | kanca c1 + kapak "AGO VARSA / PERFECT YOK" mutlak | "Ago varsa Simple Past." | c | ses c1 aynı → kapağa dokunulmadı (§4) |
| 45 | present-perfect-ileri | Ek 2 | c3 "Since cümleciği Simple Past alır", c7 | Ş kararı | c | açık (§4) |
| 46 | present-perfect-ileri | Ek 3 | dikey Shorts | Ş | d | açık |
| 47 | present-perfect-ileri | Ek 4 | sıradaki ders (since/for) içeriği tekrarlar | — | d | açık (içerik planı) |
| 48 | present-perfect-cont-temel | N-1 | kapak "İKİ SAATTİR = HAVE BEEN" | kapak jürisi | c | ders c2/c7 aynı eşlemeyi kurar → kapağa dokunulmadı (§4) |
| 49 | present-perfect-cont-temel | N-1 | gönderi "-dir ve -yor ile … have been ve -ing ile" denklik çağrıştırır | yeni gönderi cümlesi | a | ✔ |
| 50 | present-perfect-cont-temel | N-2 | damga yuvarlaması önceki sözün kuyruğuna iner | araçta aşağı yuvarlama | d | açık (araç) |
| 51 | present-perfect-cont-temel | N-3 | açıklama ilk satırı 182 karakter | kısalt | a | ✔ (114) |
| 52 | present-perfect-cont-ileri | YV-6 not | sabit yorum "süreç ile sonuç farkına" yerleşik değil | yeni cümle | a | ✔ |
| 53 | present-perfect-cont-ileri | YV-9 not | dikeyde `kapak.png` dikey kapağı gösterir | panel kararı | d | açık |
| 54 | present-perfect-cont-ileri | §1c | c5, c7 "durum fiili -ing almaz"; c3 | ders senaryosuna | c | açık (§4) |
| 55 | present-perfect-cont-ileri | YT-3 | yer kare yok | mp4 sonrası | d | açık |
| 56 | simple-past-temel | §3 hayır | t 47,82 = %51 (≈%30 değil) | 29,35 + standart cümlesi ya da istisna | d | açık: öteki 11 ders ders zamanıyla "30 sn sonrası ilk cümle başı" kuralını uygular; karar şefte |
| 57 | simple-past-temel | Not 1 | c7 "olumsuzda ve soruda did" (be hariç), c2 "-ed ekler", canAlici "-di = -ed" | yeni cümleler | c | açık (§4) |
| 58 | simple-past-temel | Not 2 | sıradaki ders `planli` | yükleme sırası | d | açık |
| 59 | simple-past-temel | Not 3 | bağlantı canlılığı, dikey Shorts | — | d | açık |
| 60 | simple-past-ileri | YT-3 | yatay yer çakışması kanıtı yok | 3 kare | d | açık |
| 61 | simple-past-ileri | YT-3 | dikey yer ölçümü yok | ölçüm koş | d | açık |
| 62 | simple-past-ileri | Ö-1 | temel ile aynı başlık | "Simple Past: Ago, Used to, Would" | a | ✔ (farklı sözle, §2 gerekçe) |
| 63 | simple-past-ileri | Ö-2 | gönderi ago ile, kapak used to/would ile açılıyor | gönderiyi kapakla eşle | a | ✔ |
| 64 | simple-past-ileri | Ö-3 | damga kayması panel testinde doğrulanmalı | — | d | açık |
| 65 | simple-past-ileri | D-1…3 | c1 "Ago varsa Perfect yok", c7 "PP for, since, yet ister", "since varsa Perfect" | yeni cümleler | c | açık (§4) |

Kendi denetimimden çıkan (jüri listesinde yok): `present-perfect-ileri` gönderisi "Ago varken has landed diyebilir miyiz?" dersin kendi
cümlesiyle (ago + hasn't landed) çelişen bir "hayır" cevabı çağırıyordu → (a) ✔. `simple-past-ileri` gönderisindeki "ago … Present Perfect
ile kullanılmaz" mutlak cümlesi aynı sebeple kalktı (madde 63 ile birlikte).

## 2. Uygulanan metin düzeltmeleri (a) — önce → sonra

Her değişiklik dikey eşine de aynı uygulandı (`02-03` dikeyi yok). Özgün dosyalar: `~/Silinecekler/2026-11-15-yv-duz/<paket>/`.

| Ders | Alan | Önce | Sonra |
|---|---|---|---|
| present-continuous-ileri | baslik | Present Continuous \| YDT İngilizce | Present Continuous: durum fiilleri ve always \| YDT İngilizce İleri |
| present-continuous-ileri | açıklama s1 | Present Continuous'u üç sınav köküyle … | Present Continuous'ı üç sınav köküyle … |
| present-continuous-ileri | gönderi | Biliyorum için I am knowing denir mi? … doğrusu I know the answer. | "Biliyorum" için "I am knowing" denir mi? … doğrusu "I know the answer". |
| present-continuous-ileri | sabitYorum | Sınavdan önce tekrar etmek için bu dersi kaydet; … | Sınav öncesi hızlı tekrar için bu dersi kaydet; … |
| simple-present-ileri | baslik | Simple Present \| YDT İngilizce | Simple Present: bağlaç ve durum fiilleri \| YDT İngilizce İleri |
| simple-present-ileri | sabitYorum | Sınavdan önce tekrar etmek için bu dersi kaydet; … | Sınava bir gün kala dönmek için bu dersi kaydet; … |
| 02-03 temel | bolumler[9] + açıklama 03:08 | Believe, recommend, have: -ing tuzağı | Believe, recommend, have (sahip olmak): -ing tuzağı |
| 02-03 temel | gönderi | now ve these days çoğunlukla şimdiki zamanı, usually ise geniş zamanı çağırır. | now ve these days çoğu zaman şimdiki zamanı, usually de çoğu zaman geniş zamanı çağırır. |
| present-perfect-ileri | baslik | Present Perfect: since, for ve ago tuzağı \| YDT İngilizce | Present Perfect: since, for ve ago \| YDT İngilizce İleri |
| present-perfect-ileri | açıklama s1 | … ve ago içeren cümlede Present Perfect'in neden kullanılmadığını … | … ve ago ile söylenen bitmiş zamanın neden Simple Past istediğini … |
| present-perfect-ileri | açıklama | (başlık yok) | "Bölümler:" satırı eklendi (9 dersle aynı biçim) |
| present-perfect-ileri | gönderi | Ago varken has landed diyebilir miyiz? … Sınavdan önce bakmak için videoyu kaydet. | The plane took off two hours ago, but it hasn't landed yet: aynı cümlede neden iki ayrı zaman var? … Sınavdan önce dönüp bakmak için bu dersi kaydet. |
| present-perfect-cont-temel | etiket | for ve since | since for (ötekilerle aynı yazım) |
| present-perfect-cont-temel | gönderi | Türkçede -dir ve -yor ile kurduğumuz bu cümleyi İngilizce have been ve -ing ile kurar: … | Süreyi for two hours taşır, süren işi have been + -ing kurar: … |
| present-perfect-cont-temel | açıklama s1 | Bu derste … kurarsın; süre için for, başlangıç noktası için since kullanmayı ve izi şimdi görünen eylemi tanırsın. (182 kr) | Present Perfect Continuous kalıbını (have/has been + -ing) üç örnekle kur; for, since ve izi görünen eylemi tanı. (114 kr) |
| present-perfect-cont-ileri | baslik | Present Perfect Continuous \| YDT İngilizce | Present Perfect Continuous: since ve durum fiilleri \| YDT İngilizce İleri |
| present-perfect-cont-ileri | sabitYorum | Sınavdan önce tekrar etmek için bu dersi kaydet; süreç ile sonuç farkına açıklamadaki bölüm damgalarıyla doğrudan geç. | Deneme sınavından önce dönmek için bu dersi kaydet; süreç ile sonucun farkını anlatan bölümlere açıklamadaki damgalarla doğrudan geç. |
| simple-past-ileri | baslik | Simple Past \| YDT İngilizce | Simple Past: ago ve düzensiz fiiller \| YDT İngilizce İleri |
| simple-past-ileri | gönderi | Two weeks ago varken has resigned yazılır mı? Yazılmaz: ago … Present Perfect ile kullanılmaz; … | Used to mu, would mu? We used to live in a village doğru; would live yanlış, çünkü geçmişteki durumu would anlatmaz. Derste two weeks ago varken neden resigned geldiğini ve begin, began, begun tuzağını da görüyoruz. |
| simple-past-ileri | sabitYorum | Sınavdan önce tekrar etmek için bu dersi kaydet; … | Sınav öncesi göz atmak için bu dersi kaydet; … |
| present-perfect-temel | gönderi son cümle | Sınavdan önce bakmak için videoyu kaydet. | Sınav öncesi tekrar için videoyu kaydet. |
| simple-past-temel | gönderi son cümle | Sınavdan önce bakmak için videoyu kaydet. | Sınav haftasında yeniden izlemek için videoyu kaydet. |
| simple-past-temel | sabitYorum | (simple-present-temel ile birebir aynı) | Sınavdan önce hızlıca dönmek için videoyu kaydet; düzensiz fiillere ve did yapısına açıklamadaki bölüm damgalarıyla doğrudan geç. |
| simple-past-temel | açıklama | (başlık yok) | "Bölümler:" satırı eklendi |

Değişmeyen: `02-04-ydt-temel` (dikeyi kilitli; düzeltme gerekmedi), `present-continuous` (gönderi son cümlesi artık yalnız 2 derste).

Başlık kararları (ileri kalıbı `<Konu>: <2–4 sözcük> | YDT İngilizce İleri`):
- Ayırt edici içerik, dersin temelde olmayan bölümlerinden seçildi (bölüm adları ve senaryo).
- Kapak metni başlığı yinelemesin diye (kapak standardı §3, KS-4) `simple-past-ileri` "used to, would", `present-perfect-cont-ileri`
  "süreç / sonuç", `simple-present-ileri` "tarife" sözcüklerini almadı: kapakları zaten bunları söyler. Başlık + kapak birlikte dersin
  bütün içeriğini verir.
- Hedef ≤ 60: 4 başlık aşar (62, 66, 71, 73); hepsi ≤ 100. Ek " | YDT İngilizce İleri" tek başına 22 karakterdir.

## 3. Kapak düzeltmeleri (b)

| Ders | Önce | Sonra | Kareler |
|---|---|---|---|
| simple-present-ileri | YARIN ama / WILL YOK | YARIN / WILL mi? (küçük satır aynı: "The flight takes off at nine.") | `projeler/simple-present-ileri/kapak.png`, `kapak-koyu.png`; `projeler/simple-present-ileri-dikey/kapak.png`, `kapak-koyu.png`; `projeler/simple-present-ileri/uretim-tutanagi/kapak-168.png` |

1. Ders karşılaştırması: ders c7 "tarife varsa Simple Present, tahmin varsa will" der. Kapak "yarında will yok" diyerek dersin koduyla çelişir.
   Ders doğru, kapak yanlış → kapak düzeltildi.
2. Yeni metin dersin c6 sorusudur ("yarın dediği için will take off olmaz mıydı?"); soru biçimi kapak §3'te izinlidir; iddia kurmaz.
3. Üretici: `sahneler/90-hyperframes-kapak/uret.py` yalnız SATIR1/SATIR2 değişti; dikey paket aynı üreticiyi çağırır. Karakter, nesne,
   yerleşim aynı. "YARIN DİYE" dikeyde "İ" noktasıyla logoya, "YARIN diye" "y" kuyruğuyla vurgu kutusuna değdi (üretici `assert`).
4. Kareye baktım: 4 kare + 168 px. Taşma yok, yazı karaktere binmiyor, sağ alt boş, 168 px'te "YARIN WILL mi?" okunur.

Dokunulmayan kapaklar ve gerekçesi:
- `present-continuous` ("GİDİYORUM = AM GOING", "-yor → -ing"), `present-perfect-ileri` ("AGO VARSA / PERFECT YOK"),
  `present-perfect-cont-temel` ("İKİ SAATTİR = HAVE BEEN"): aynı iddia dersin sesinde var → kural gereği (c), §4.
- `present-perfect-temel` ("KAYBETTİM = HAVE LOST" · "have / has + V3"): ders c1–c2 aynı köprüyü "sonucu şimdi" şartıyla kurar; kapak,
  standardın köprü biçimidir ("GİDER = GOES" de kısmi denkliktir). Jüri "hayır" demedi, kapak jürisine bıraktı. Jüri önerisi
  ("KAYBETTİM, KAPIDA KALDIM = HAVE LOST") satır 1'e sığmaz (S1 170 px). Kapak jürisi isterse ikinci sıra.
- `present-continuous-ileri`: kusur görselde (beyaz üçgen), yazıda değil; görsel bu işte değişmez.

## 4. (c) Dersin kendisi — açık işler

| Ders | Cümle (ses) | Sorun | Önerilen cümle | Ses yeniden | Kapak |
|---|---|---|---|---|---|
| present-continuous | c7 "-ing ekini Türkçedeki -yor gibi düşün: koşu-yor, runn-ing." | yanlış denklik (biliyorum ≠ I am knowing) | "-ing çoğu zaman Türkçedeki -yor'a denk gelir: koşuyor, running. Ama know gibi durum fiillerinde -yor olsa da -ing gelmez: biliyorum, I know." | evet (c7) | ses düzelince "GİDİYORUM / = I AM GOING", küçük satırdaki "-yor → -ing" kalkar |
| present-continuous | c2 "İngilizce de aynısını yapar." | kısmi denklik | "İngilizce de planlanmış gelecek için aynısını yapar." | evet (c2) | — |
| present-continuous-ileri | c3 "While, tam anı gösterir." | belirsiz terim | "While, aynı anda süren iki işi bağlar." | evet | — |
| present-continuous-ileri | c7 "… durum fiilidir, -ing almaz." · "Always artı -ing şikâyettir." | mutlak (I am thinking, She is always helping) | "… durum anlamında -ing almaz." · "Always artı -ing çoğu zaman şikâyet bildirir." | evet (c7) | — |
| simple-present-ileri | c6–c7 "Hayır. Tarife … kesinse Simple Present." | "Hayır" will take off'u yanlış sayar (EK-5c) | "Tarife kesinse Simple Present seçilir; will tahmin ve ani karar içindir." | evet (c7) | kapak düzeltildi (§3) |
| simple-present-ileri | c4 "Owns ve costs durum fiilidir: ing almaz." | mutlak | "Owns ve costs burada durum anlatır: -ing almaz." | evet (c4) | — |
| 02-03 temel | c15 "Believe ve have gibi fiiller …" | have sınırsız (c14 sınırı çizer) | "Believe ve sahip olmak anlamındaki have gibi fiiller …" | evet (c15) | — |
| present-perfect-temel | c7 "For ve since süre … just ve already yeni biten iş." | since başlangıç noktasıdır; already "çoktan" | "For süreyi, since başlangıç noktasını söyler; just yeni biten işi, already beklenenden önce biten işi." | evet (c7) | — |
| present-perfect-ileri | c1 "Ago varsa Present Perfect yok." | mutlak; dersin c5 örneği (ago + hasn't landed) çürütür | "Ago varsa Simple Past." (`meta.kapak` zaten böyle) | evet (c1) | ses düzelince kapak "AGO VARSA / SIMPLE PAST" (`meta.kapak`) |
| present-perfect-ileri | c3 "Since cümleciği Simple Past alır" · c7 "… Present Perfect'i yasaklar" | mutlak | "Since cümleciği çoğu zaman Simple Past alır" · "… aynı yan cümlede Present Perfect'i dışlar" | evet (c3, c7) | — |
| present-perfect-cont-temel | c2/c7 "Türkçedeki -dir ve -yor gibi düşün" | -dir ↔ have been eşlemesi; süreyi for taşır | "Süreyi for ve since söyler; süren işi have been artı -ing." | evet (c7) | ses düzelince kapak "İKİ SAATTİR = HAVE BEEN" yerine dersin c1'i ile soru ya da "I have been working" |
| present-perfect-cont-ileri | c5, c7 "Durum fiili -ing almaz" · c3 "Ana cümlede have been ve -ing gelir" | mutlak (I have been thinking) | "Durum anlamındaki fiil -ing almaz" · "Burada ana cümlede …" | evet | — |
| simple-past-temel | c7 "Olumsuzda ve soruda did gelir, fiil yalın kalır." · c2 "İngilizce de -ed ekler." | be fiilinde yanlış; her fiile -ed çağrışımı | "Düzenli ve düzensiz fiillerde olumsuzda ve soruda did gelir (be hariç: wasn't, were)." · "İngilizce düzenli fiile -ed ekler." | evet (c2, c7) | — |
| simple-past-ileri | c1 "Ago varsa Perfect yok." · c7 "Present Perfect for, since, yet ister." · "since varsa Perfect" | mutlak / belirsiz | "Ago varsa Simple Past." · "… for, since, yet ile sık gelir." · "since + zaman noktası varsa ana cümle Perfect" | evet (c1, c7) | — |

Yazma alanı dışında kalan aynı sınıf: `present-continuous` ve `simple-past-temel` `surumler.json` `canAlici` ("-yor = -ing", "-di = -ed").

## 5. (d) Ölçüt ve kanıt notları

- YV-8: srt pakette tutulmaz, panel türetir; json yarısı 12 derste geçer. Ölçüt "`altyazi.json` son t1 ≤ ders süresi" biçimine daraltılmalı.
- Bildirim yeri: `youtube-surumu-standart.md` §3 artık "sol alt (yer.json)" der. 02-04 ve simple-present-temel jürilerinin "sağ üst" hükmü eski metne dayanır.
- Bildirim zamanı: 11 ders "ilk 30 sn sonrası ilk cümle başı" kuralını ders zamanıyla uygular; `simple-past-temel` (%51) bu kuralla tutarlıdır.
  Standarda tek cümle gerekir ("≈ %30 ilk 30 sn'ye düşüyorsa 30 sn sonrası ilk cümle başı") ya da "YouTube zamanı" kararı. Karar şefte.
- Giriş kayması: `youtube.json` ders zamanını tutar; API damgaları yeniden yazar (sözleşme §3). Panel testi doğrulamalı.
- mp4 yok: ses ve kare çakışma ölçümleri (YT-3) mp4 sonrası jüride.
- Dikey ≈ 100 sn → Shorts: bölüm damgası, bildirim, sabit yorumdaki "damgalarla geç" vaadi işlemeyebilir. Dikey `youtube.json` yatayla aynı kalır (istem kuralı). Karar şefte.
- Katalog: `02-02-ydt-ileri` öğesi `proje: 02-02-ydt-ileri` gösterir; veri `simple-present-ileri`de. Betik eşlemeyi `utm_campaign` kodundan yapar.
- "Kanal etiketi" tanımlı değil. Betik sözleşme §2'nin kanal sabitlerini aradı: "İngilizce", "gramer", "YDT" (12/12 var). `@ydspublishing`
  ya da "YDT İngilizce" seçilirse kilitli 02-04 dikeyi ve simple-present-temel değişmeden geçemez.
- Ek bilgi (aynı süreçte görüldü): `simple-present-temel` ders süresi 93,47 → 96,47 sn (başka oturum c7'yi yeniden sentezledi). Bölüm başları
  sahne başlarıyla hâlâ eşleşir; son bölüm 36 sn.

## 6. Tutarlılık betiği

Metin: `~/.cache/yv-duz/yv-tutarlilik.py.taslak` (hedef yol `uretim-hatti/betikler/yv-tutarlilik.py`; yazma kapısı bekliyor). Yalnız standart
kitaplık, salt okuma, çıkış 1 = sorun. Ölçtüğü: sınırlar, bölüm/bildirim zamanı (`zaman.json`, sahne başı, ilk 30 / son 20 sn), açıklama
damga bloğu = `bolumler`, kanal etiketi, emoji, başlık kalıbı ve tekliği (temel / ileri), liste adı + sıra + önceki/sonraki (katalogdan),
etiket ve hashtag yazımı (eş ad ve konu adı istisnası), sabit yorum + gönderi kopyası (birebir metin; cümle ve yan cümle > 2 derste), dikey = yatay.
`--kilitli`: yalnız kilitli pakete düşen sorun çıkış koduna sayılmaz.

Eski durum (yedeklerden kurulan ağaç): 18 sorun, çıkış 1 — damga başlığı 4, başlık 9 (3 çift aynı + 5 ileri kalıp dışı), etiket yazımı 1, kopya 4.

Son koşu (`--kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey`), çıkış 0:

```
yv-tutarlilik: 12 ders, 11 dikey eş
[TAMAM] sinir: 0
[TAMAM] zaman: 0
[TAMAM] damga: 0
[TAMAM] kanal-etiketi: 0
[TAMAM] emoji: 0
[TAMAM] baslik: 0
[TAMAM] liste: 0
[TAMAM] etiket-yazim: 0
[TAMAM] kopya: 0
[TAMAM] dikey: 0
[kilitli] damga: simple-present-temel: açıklamada 'Bölümler:' başlığı yok
[kilitli] damga: simple-present-temel-dikey: açıklamada 'Bölümler:' başlığı yok
[bilgi] 02-03-ydt-temel: başlık 71 karakter (hedef ≤ 60)
[bilgi] present-continuous-ileri: başlık 66 karakter (hedef ≤ 60)
[bilgi] present-perfect-cont-ileri: başlık 73 karakter (hedef ≤ 60)
[bilgi] simple-present-ileri: başlık 62 karakter (hedef ≤ 60)
toplam sorun: 0 · kilitli pakette: 2
```

`--kilitli` olmadan: 2 sorun, çıkış 1 (yalnız yukarıdaki iki `simple-present-temel` satırı).

Yeni başlık listesi (değişenler):

| Ders | Başlık | kr |
|---|---|---|
| present-continuous-ileri | Present Continuous: durum fiilleri ve always \| YDT İngilizce İleri | 66 |
| simple-present-ileri | Simple Present: bağlaç ve durum fiilleri \| YDT İngilizce İleri | 62 |
| present-perfect-ileri | Present Perfect: since, for ve ago \| YDT İngilizce İleri | 56 |
| present-perfect-cont-ileri | Present Perfect Continuous: since ve durum fiilleri \| YDT İngilizce İleri | 73 |
| simple-past-ileri | Simple Past: ago ve düzensiz fiiller \| YDT İngilizce İleri | 58 |

## 7. `simple-present-temel` için bekleyen düzeltmeler (kilitli paket; uygulanmadı)

1. `youtube-aciklama.md` (+ dikey): damga bloğunun üstüne "Bölümler:" satırı (öteki 11 dersle aynı biçim; betik kilitsiz koşuda bunu sorar).
2. Açıklama satır 1: "Simple Present'ı üç örnekle öğren: doğa kanunu, alışkanlık, tarife ve fiile gelen s" dört öğe sayar →
   "Simple Present'ı üç örnekle öğren: doğa kanunu, alışkanlık ve tarife; fiile gelen s (he, she, it) de derste."
3. Ders iddiaları (c, jüri notu): "Türkçedeki er eki gibi: git-er, go-es" (LISTE.md: DUZ2-SPANA c7'yi yeniden sentezledi; doğrulanmadı),
   `canAlici` "geniş zaman eki = s", "Kod: always, usually, every day" (always öteki zamanlarla da gelir).
4. Ders süresi 96,47 sn oldu: bildirim (43,91) ve bölüm damgaları sahne başlarıyla tutarlı; YVJ jürisi yeni ses üzerinde yeniden koşmalı.
5. Kopya sınırı: gönderi son cümlesi "Sınavdan önce bakmak için videoyu kaydet." artık yalnız bu ders + present-continuous'ta (2); sabit
   yorum yan cümlesi "açıklamadaki bölüm damgalarıyla istediğin bölüme doğrudan geç" bu ders + present-perfect-temel'de (2). Değişiklik gerekmez.

## 8. Sözleşmeye önerilen satırlar (`.claude/docs/sozlesme.md`; yazılmadı)

Gerekçe: dosya istemin yazma alanı dışında; başka oturumun commit'lenmemiş 5 satırı var; kapı bayrağı istemle yasak. Şef ekler:
- YV başlık kalıbı (YV-DUZ): temel `<Konu> | YDT İngilizce`; ileri `<Konu>: <2–4 sözcük> | YDT İngilizce İleri`; alt başlık kapak metnini yinelemez (KS-4).
- YV açıklama: damga bloğu "Bölümler:" satırıyla başlar. Sabit yorum ve gönderide aynı cümle ya da yan cümle en çok 2 derste.
- YV tutarlılık kapısı: `uretim-hatti/betikler/yv-tutarlilik.py [--kilitli …]` (çıkış 0 = geçti; yazma kapısı onayı bekliyor).

---
Son Güncelleme: 16.11.2026 — ilk sürüm; §8 sözleşme önerisi.

# 02-04-ydt-temel · İstem A girdisi (kaynak dökümü)

Tarih: 14.11.2026 · Hazırlayan: Claude oturumu (srv21, istem A) · Amaç: senaryo taslağının kaynak tabanı.
Senaryo taslağı: `../senaryo-taslak.md`. Jüri (kaynak, kural, dil) bu dosyadaki ham metni kanıt olarak kullanır.

## 1. Künye

| Alan | Değer |
|---|---|
| Kimlik / kod | `02-04-ydt-temel` · `ING-YDT-GR-02-04-T` |
| Ders | GR-02-04 · Tenses (02) · katalog adı "02 - tenses - 04" |
| Konu adı (katalog) | Simple Present vs Present Continuous (`konu-adlari.json`, güven yüksek; kanıt: döküm [00:02]) |
| Kitle · seviye · format | YDT · temel · yatay 16:9 |
| Sesler | öğretmen Atakan `gsJ9nrlXYbPztJxC4fwc` · öğrenci Gökçe Deniz `oPC5I9GKjMReiaM29gjY` · eleven_v4 |
| Süre | iddia yok (12.11 kararı) |
| Eski LMS video | Vimeo 863572960 · 1.158 sn · 375 izlenme · tamamlama 52 · ortalama izleme %41 (`katalog.json`) |
| pptx (katalog) | `YEDEK/Tenses/unit-1_sunum-3 uygun.pptx` + `YEDEK/Tenses/unit-1_sunum-3-NADIR-MSI.pptx` |
| pptx (okunan) | `/home/sef/01dev/dijital-anlatim/varlik/grammar/kaynak-pptx/YEDEK/Tenses/unit-1_sunum-3 uygun.pptx` (14 slayt, gizli slayt yok). `-NADIR-MSI` sürümü sunucuda yok; okunmadı. |
| Çıkarma yöntemi | python `zipfile`: `ppt/presentation.xml` `sldIdLst` sırası + `ppt/_rels/presentation.xml.rels` → `ppt/slides/slideN.xml` içindeki `a:t` metinleri, paragraf başına bir satır |
| Döküm | `/home/sef/01dev/dijital-anlatim/varlik/grammar/transkript-whisper/863572960.md` (Whisper, 444 satır, son damga 19:15) · 02-04 kapsamı 00:00–03:14; 03:14–04:30 (slayt 3 S4, *smell*) 02-05'e (kaynak jürisi tur 1 madde 1) |
| Aynı pptx'i kullanan komşu | GR-02-05 "Simple Present vs Present Continuous: Stative Verbs" (katalog: aynı iki pptx) |

**DİKKAT:** Sunucudaki `grammar-defter.md` 10.11 21:10 kaydında biter (1.550 satır). D-0204 ve D-0205 satırları bu kopyada yok.
Kovan `kararlar.jsonl` da sunucuda D-0096'da biter. İki kararın içeriği şu kaynaklardan alındı:
SKILL.md adım 2 (D-0204: jüri 3 denetçi), `projeler/02-03-ydt-temel/BRIEF.md` §1 ve `projeler/02-03-ydt-ileri/BRIEF.md`
"Karar notları (D-0205)": believe/think için kategori etiketi yok; "performative" yalnız recommend/promise/agree;
these days / nowadays mutlak kural değil; köklerde şıklar ekranda tam görünür; öğrenci cümlesinden sonra 0,75 sn duraklama.

## 2. Seçilen slaytlar

### Slayt 2 — bölüm kapağı (taslakta: kanca sonu başlık, kapanış künyesi)

```
SIMPLE PRESENT
TENSE 
& 
PRESENT CONTINUOUS TENSE
```

Gerekçe: dersin başlığı. Katalog konu adıyla aynı.

### Slayt 3 — iki sütunlu fark tablosu (taslakta: örnekler, kural kartı, karşıt çift, tuzak)

Ham metin (çıkarıldığı gibi; etiket ile örnek arasında boşluk yok, "olun" kaynakta yazım hatası):

```
SIMPLE PRESENT TENSE
Genel durumlarShe wears her coat in the winter.
Kalıcı, sürekli durumI live in İstanbul with my family.
Gelecekte yer alacak programlı, tarifeli olaylarThe train to İzmir leaves at 7 pm today.
Durum bildirmeThe roses smell nice.
PRESENT CONTINUOUS TENSE
Konuşma esnasında olun durumlarShe is wearing her pink T-shirt today.
Geçici durumMy parents are out of town,so I am living with my uncle.
Gelecekte yer alacak planlanmış, ayarlanmış olaylarI  am going to the movie theater tonight.
Eylem bildirmeShe is smelling the roses.
DIFFERENCES
SIMPLE PRESENT TENSE & PRESENT CONTINUOUS TENSE  
```

Ayrıştırılmış hâli (satır = karşıtlık):

| Satır | SIMPLE PRESENT | PRESENT CONTINUOUS | Taslakta |
|---|---|---|---|
| S1 | Genel durumlar · *She wears her coat in the winter.* | Konuşma esnasında olan durumlar · *She is wearing her pink T-shirt today.* | kullanıldı |
| S2 | Kalıcı, sürekli durum · *I live in İstanbul with my family.* | Geçici durum · *My parents are out of town, so I am living with my uncle.* | kullanıldı |
| S3 | Gelecekte yer alacak programlı, tarifeli olaylar · *The train to İzmir leaves at 7 pm today.* | Gelecekte yer alacak planlanmış, ayarlanmış olaylar · *I am going to the movie theater tonight.* | kullanıldı |
| S4 | Durum bildirme · *The roses smell nice.* | Eylem bildirme · *She is smelling the roses.* | kullanılmadı; kapanışta 02-05'e tek cümle işaret |

Gerekçe: slayt 3 bu dersin çekirdeği. Döküm 00:17–04:30 aralığı bu slaytı satır satır işler ve "Bunlar genel farklılıklardı" (04:30) ile kapatır.
S4 (durum ↔ eylem, *smell*) ile slayt 4–9 aynı konuyu taşır: anlamına göre -ing alan ya da almayan fiiller. Katalog bu konuyu 02-05'e verir.

## 3. Seçilmeyen slaytlar

| Slayt | İçerik (özet) | Neden seçilmedi |
|---|---|---|
| 1 | PRESENT FORMS: Present Continuous · Simple Present · Present Perfect · Present Perfect Continuous | Ünite içindekisi; ders konusu değil (02-03 emsali). |
| 4 | Non-progressive Verbs (-ing takısı almayan fiiller): duyular, duygular, zihinsel faaliyet, sahiplik, diğer fiiller listesi (yıldızlı fiiller) | 02-05 konusu (katalog başlığı "Stative Verbs"). |
| 5 | think (fikir beyanı / düşünmek), see (görmek / buluşmak) | 02-05 konusu: yıldızlı fiillerin iki anlamı. |
| 6 | smell (kokmak / koklamak), taste (tat vermek / tatmak) | 02-05 konusu. |
| 7 | feel (dokunma hissi, sezinlemek / dokunarak hissetmek, hissetmek), appear (gibi görünmek / sahneye çıkmak) | 02-05 konusu. |
| 8 | look (görünmek / bakmak), weigh (ağırlığında olmak / tartmak) | 02-05 konusu. |
| 9 | be (genel / bir süreliğine: *is being*), have (sahip olmak / diğer anlamlar) | 02-05 konusu. |
| 10–12 | EXERCISE 01 (9 diyalog: have lunch, tastes bitter, smell nice, see the director, have a lot of work, remember, know, look worried / think, feel energetic / want) | Eski 02-05 videosunun alıştırması (döküm 863573110, 00:18–). Maddelerin çoğu durum fiili sorusu. |
| 13 | EXERCISE 02 (8 cümle: eagle reaches, sounds impossible, use / am using, smells / think, realize / get worse, have classes outdoors, hear, consists) | Eski 02-05 videosunda çözüldü (döküm 863573110, son madde *consist* 06:51). Durum fiili ağırlıklı; 02-05'e kalır. |
| 14 | Kapanış başlığı (slayt 2 ile aynı) | Yinelenen başlık. |

## 4. Dökümden alınan kapsam maddeleri (Vimeo 863572960)

| # | Damga | Madde | Taslakta |
|---|---|---|---|
| 1 | 00:03–00:09 | Amaç: "Present Continuous Tense yani şimdiki zaman ve Simple Present Tense yani geniş zaman arasındaki farkları inceleyeceğiz." | kanca 2 |
| 2 | 00:22–00:26 | İki tablo: Simple Present ↔ Present Continuous (slayt 3). | kural kartı 8 |
| 3 | 00:28–00:31 | Geniş zaman genel durumları anlatır. | örnek 3 |
| 4 | 00:36–00:43 | *She wears her coat in the winter.* "Her kış ayında giyer anlamına geliyor." | örnek 3 |
| 5 | 00:46–00:50 | Şimdiki zaman: konuşma esnasında olan, "tam şu anda gerçekleşen" durum. | örnek 3 |
| 6 | 00:55–01:01 | *She is wearing her pink T-shirt today.* "Konuşma esnasında bugün gerçekleşen olaya vurgu yapıyor." | örnek 3, karşıt çift 9 |
| 7 | 01:05–01:09 | *wears* genel; *is wearing* "sadece bugüne ait … şu zamana ait olduğu için". | örnek 3, karşıt çift 9 |
| 8 | 01:18–01:30 | Kalıcı sürekli durum: *I live in Istanbul with my family.* "Bu her zaman yaşıyorum anlamına gelir." | kanca 1–2, örnek 4, tuzak 11 |
| 9 | 01:34–01:46 | Geçici durum: *My parents are out of town. So I am living with my uncle.* | kanca 2, örnek 4 |
| 10 | 01:46–02:03 | "İstanbul'da yaşamam genel bir durumdu … sadece şu zamana has olarak amcamla yaşıyorum derken I am living." | örnek 4, tuzak 13 |
| 11 | 02:05–02:10 | Gelecekte de fark var: programlı, tarifeli olaylar. | örnek 5 |
| 12 | 02:10–02:19 | "Timetable dediğimiz olaylar … öznenin cansız olduğu olaylarda geniş zamanı kullanıyorduk." | soru anı 1 cevabı 7 |
| 13 | 02:21–02:24 | *The train to İzmir leaves at 7 p.m. today.* "İzmir treni bugün saat 7'de kalkacak." | örnek 5, karşıt çift 10 |
| 14 | 02:26–02:39 | "Gelecek zamana yönelik bir tarife, bir program, bir schedule varsa biz geniş zaman kurallarını uyguluyoruz. Ama öznemizin genelde cansız olduğuna dikkat edelim." | örnek 5, cevap 7 |
| 15 | 02:39–02:46 | Planlanmış, ayarlanmış gelecek olaylar; "aynı be going to gibi". | örnek 5 (be going to anılmadı: 02-04'te gelecek kalıpları kıyaslanmıyor) |
| 16 | 02:46–03:03 | "Ben bu akşam amcamlara gidiyorum … Türkçe olarak direkt karşılığı var … söyleyebiliyorsanız şimdiki zamanı gelecek zaman anlamında kullanabilirsiniz." | örnek 5 (Türkçe çeviri kartı) |
| 17 | 03:03–03:14 | *I am going to the movie theater tonight.* "Çok net bir şekilde plan yapmış … aslında gideceğim demiş oluyor." | örnek 5, cevap 7 |
| 18 | 03:14–03:24 | Durum bildirme ↔ eylem bildirme; "biraz sonra bunlara tek tek odaklanacağız". | kapanış 18 (02-05 işareti) |
| 19 | 03:28–04:26 | *smell*: kokmak (durum, *The roses smell nice*, -ing yok) ↔ koklamak (eylem, *She is smelling the roses*). | kullanılmadı → 02-05 |
| 20 | 04:30 | "Peki devam edelim. Bunlar genel farklılıklardı." — 02-04 kapsamının sonu. | sınır |
| 21 | 04:33–07:38 | Non-progressive verbs tablosu (slayt 4): duyular, duygular, zihinsel, sahiplik, diğer fiiller; "I am liking diye bir şey duymak istemiyoruz". | kullanılmadı → 02-05 |
| 22 | 07:38–18:50 | Yıldızlı fiiller: think, see, smell, taste, feel, appear, look, weigh, be, have (slayt 5–9). | kullanılmadı → 02-05 |
| 23 | 18:50–19:15 | Kapanış: iki zamanın farkları + -ing alan/almayan fiiller anlatıldı; "bir sonraki videomuzda görüşmek dileğiyle". | kapanış 18 |

Döküm notu: Whisper döküm, yazım hataları kaynakta (örn. "inkeki" = -ing eki, "özlem" = özne). Alıntılar dökümdeki gibidir.

## 5. Komşu ders sınırı

| Ders | Konusu (katalog / üretim) | Kullandığı içerik | 02-04 bunu yinelemez |
|---|---|---|---|
| 02-01 Present Continuous (`present-continuous`) | PC formu, zaman ifadeleri, 6 kullanım | *I am sitting … now*, *piano lessons this semester*, *Look! The cat is climbing*, *The world is becoming smaller*, *For the time being I am staying …*, ***I am going to the movie theater tonight***, *barbecue this Saturday* | PC formu ve tek başına kullanımları. Ortak cümle: *movie theater tonight* (slayt 3'te de var; açık nokta). |
| 02-02 Simple Present (`02-02-ydt-temel`) | SP formu (+s, don't/doesn't, do/does), rutin, kalıcı durum, genel gerçek; tarife yalnız ileri | *I go to Kaş every summer*, *He gets up at seven*, *The Moon completes its orbit*, *She eats fish every day / is eating fish now*; "Türkçe ekine değil, anlama bak" (rutin) | SP formu, sıklık zarfları, rutin. Türkçe "-yor" tuzağı 02-02'de rutin içindi; 02-04'te kalıcı ↔ geçici için (açık nokta). |
| 02-03 ayrım alıştırması (`02-03-ydt-temel`, slayt 2b) | Sinyal sözcüğüyle ayırma: now, these days, nowadays, usually, plan | *are leaving at 9*, *is going through … these days*, *harder and harder nowadays*, *Nancy usually … now*, *staying for a week ≠ includes*, *offers ≠ are enjoying*, tuzak *believe / have / recommend*, mini soru *I am writing now*. İleri: *takes off* (tarife) | Sinyal sözcüğü listesi ve karar kartı, kartpostal cümleleri, believe/have/recommend tuzağı. 02-04'ün açısı: kullanım tablosu (anlam). |
| 02-05 Stative Verbs (aynı pptx) | -ing almayan fiiller, yıldızlı fiillerin iki anlamı, alıştırmalar | slayt 3 S4 (*smell*), slayt 4–13 | Hiçbiri işlenmez. Kapanışta tek cümle: "Sonraki derste ing almayan fiilleri görüyoruz." |

**02-04'ün kendi kapsamı (örtüşmeyen):**
1. Slayt 3 S1: genel durum ↔ konuşma anı (*wears her coat in the winter* ↔ *is wearing her pink T-shirt today*).
2. Slayt 3 S2: kalıcı ↔ geçici (*live in İstanbul with my family* ↔ *am living with my uncle*).
3. Slayt 3 S3: tarifeli gelecek ↔ planlanmış gelecek (*train to İzmir leaves at 7 pm* ↔ *am going to the movie theater tonight*). Temel hatta tarife ilk kez burada (02-02 temel ve 02-03 temel tarifeyi ileriye bıraktı).
4. Aynı zaman sözcüğü iki zamanda: *today* hem S1 PC hem S3 SP cümlesinde (kaynakta iki cümle ayrı satırda).
5. Türkçe "yaşıyorum" iki İngilizce zamana karşılık gelir (döküm 01:18–02:03).

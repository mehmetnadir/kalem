# YV-RAPOR — simple-past-ileri YouTube yayın verisi · 15.11.2026 (istem YV-0210I)

| Dosya | Durum |
|---|---|
| `simple-past-ileri/youtube.json` | yazıldı, JSON ayrıştırıldı |
| `simple-past-ileri/youtube-aciklama.md` | yazıldı, 699 bayt, `utm_content=ana-yatay` |
| `simple-past-ileri-dikey/youtube.json` | yazıldı; ana paketle bayt bayt aynı (`cmp` farksız) |
| `simple-past-ileri-dikey/youtube-aciklama.md` | yazıldı, 699 bayt; tek fark `utm_content=dikey-tam` (`diff` 1 satır) |

Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`), sunucu oturumu. Jüri (YVJ-0210I) farklı modelle koşmalı (`juri-olcutleri.md` §1e).
Dikey paket: VAR (`simple-past-ileri-dikey`, `surumler.json` `dikey-tam.proje`). Dikey `zaman.json` yalnız genişlik/yükseklikte farklı;
sahne sınırları aynı. Dikey `ortak/anlatim` ana pakete bağdır (aynı `sozcukler.json`). `bolumler` ve `bildirimler` dikeyin kendi
dosyalarından hesaplandı; değerler ana paketle aynı çıktı.

**Kaynak notu:** bu paket eski kuşaktandır (05.11). Pakette `senaryo.json` ve `baslar.json` YOK. Cümle başları için
`ortak/anlatim/METIN.md` "başlar" sütunu ve `ortak/anlatim/sozcukler.json` (sözcük `t0`/`t1`) okundu. Konu adı `surumler.json`
`video.konu` ("Simple Past"), kitle `video.kitle` ("YDT"); künye `ortak/kunye.js` `ders: "SIMPLE PAST"`.

## 1. Ölçüm çıktısı (betik, iki paket için aynı)

```
== simple-past-ileri JSON OK; ders süresi 91.54
YV-1 baslik 27 kr True
YV-5 etiket 7 ham kr 61 YouTube sayımı 73 yineleme False
YV-3 bölüm 5 ilk 0.0 süreler [13.47, 19.68, 15.84, 17.2, 25.35] min 13.47 hepsi sahne başı True max ad kr 40
iç ad []
damga birebir True 5
YV-2 açıklama bayt 699 hashtag 5 ['#YDT', '#İngilizce', '#gramer', '#SimplePast', '#PresentPerfect'] utm [('ING-YDT-GR-02-10-I', 'ana-yatay')]
sıra: ['Bu derste Simple Past ', 'Sınav günü bakmak için', 'Bölümler:'] … ['Sıradaki ders: Past Co', 'Ders sayfası: https://', '#YDT #İngilizce #grame']
bildirim 33.15 %36.2 cümle başı [4] önceki cümle biter 32.68 ilk30 dışı True son20 dışı True söz ortası değil True
emoji []
gorsel var [True]
sabitYorum cümle 1 gönderi cümle 3 gönderi soru ile başlar True
yasak söz []
YV-8 altyazı 21 ilk t0 1.0 son t1 90.62 ≤ süre True
== simple-past-ileri-dikey … (aynı değerler; utm dikey-tam)
katalog Tenses 2 GR-02-09 sira 9 02-09-ydt-ileri uretimde present-perfect-cont-ileri
katalog Tenses 2 GR-02-10 sira 10 02-10-ydt-ileri uretimde simple-past-ileri
katalog Tenses 2 GR-02-11 sira 11 02-11-ydt-ileri planli None
```

Ders süresi = `zaman.json` son `t_son` = 91,54 sn. Pakette `cikti.mp4` yok; mp4 süresiyle karşılaştırma yapılmadı.
"YouTube sayımı" = ham karakter + virgüller + boşluklu etikete 2 tırnak.

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 27 karakter; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu = `surumler.json` `video.konu` "Simple Past" (katalog `konu-adlari.json` GR-02-10 "Simple Past", güven yüksek); kitle `video.kitle` "YDT" |
| YV-2 | evet | 699 bayt (≤ 5.000). Sıra: değer cümlesi → kaydet → "Bölümler:" + 5 damga → "Sıradaki ders" → "Ders sayfası" (utm) → 5 etiket. Dil kısmına jüri (D) bakacak |
| YV-3 | evet | ilk damga 00:00; 5 bölüm; en kısa bölüm 13,47 sn (Giriş + Kanca). Yuvarlanmış damgalarla en kısa aralık 00:00 → 00:13 = 13 sn. Her `t` bir sahne `t_bas` değeri |
| YV-4 | evet (D bakacak) | iç ad kalmadı ("Giriş", "Kanca", "Örnek 1–3", "Soru + Form" yok); en uzun ad 40 karakter (≤ 40). Tablo §3 |
| YV-5 | evet | 7 etiket, ham 61 karakter; YouTube sayımı 73 (≤ 500); yineleme yok. Konu adı ("Simple Past"), zaman adları ("Simple Past", "Present Perfect", "geçmiş zaman"), kitle ("YDT") var |
| YV-6 | evet (D bakacak) | mutlak kural sözü ("her zaman", "asla", always) yok (betik: `yasak söz []`); iddialar §5 tablosunda. Yazım elle denetlendi; İngilizce sözcük ardından Türkçe soru eki kullanılmadı (ünlü uyumu belirsizliği yok) |
| YV-7 | evet | katalog ünite 02 "Tenses" (`sira` 2); konu GR-02-10 `sira` 10 → `liste.sira` 10; seviye adı katalog `seviyeler.ileri` "İleri" → "Tenses · YDT İleri"; önceki `02-09-ydt-ileri` (uretimde), sonraki `02-11-ydt-ileri` (planli) |
| YV-8 | evet (pakette srt yok) | `altyazi.srt` paneldedir. `altyazi.json` 21 satır, ilk `t0` 1,00, son `t1` 90,62 ≤ 91,54 (iki pakette aynı dosya) |
| YV-9 | evet | `gorsel` = `kapak.png`; dosya iki pakette var (`file`: ana 1920×1080, dikey 1080×1920; açık tema: `KAPAK-RAPOR.md`). Gönderi, sabit yorum ve açıklamada emoji yok (betik) |

## 3. Bölüm tablosu

| Sahne (iç ad) | İzleyici adı | `t` (sn) | Damga | Süre (sn) |
|---|---|---|---|---|
| 1 Giriş + 2 Kanca (birleşti; Giriş 3 sn < 10 sn) | Simple Past: bitmiş eylem, belli zaman | 0,00 | 00:00 | 13,47 |
| 3 Örnek 1 | In 1911 ve begin, began, begun tuzağı | 13,47 | 00:13 | 19,68 |
| 4 Örnek 2 | Used to ve would: hangisi durum anlatır? | 33,15 | 00:33 | 15,84 |
| 5 Örnek 3 | Asıl tuzak: ago ve yet aynı cümlede | 48,99 | 00:49 | 17,20 |
| 6 Soru + Form | Ago varken has resigned olur mu? | 66,19 | 01:06 | 25,35 |

- Damga kuralı: `t` en yakın saniyeye yuvarlanır (02-04 pilotuyla aynı kural). 48,99 → 00:49; aşağı yuvarlama (00:48) cümle 4'ün
  son sözcüğüne ("yanlış." 47,72–48,44) düşer.
- Bölüm 1 içeriği: cümle 1 "Ago varsa Perfect yok." (Giriş sahnesi) + cümle 2 tanım "A finished action at a definite time in the past."
  (Kanca sahnesi; sahne raporu: tanım iki satır, `finished` daire, `definite time` alt çizgi). Ad tanımı özetler.
- Bölüm 3 adı soru biçimindedir. Sebep: "durum ve alışkanlık" biçimi "used to = durum, would = alışkanlık" diye yanlış eşleşme
  okunabilir; ders "used to ikisini de, would yalnız tekrarlanan eylemi" der (cümle 4).

## 4. Bildirim anları

| # | `t` (sn) | Ders payı | Cümle sınırı | Ekranda |
|---|---|---|---|---|
| 1 | 33,15 | %36,2 | cümle 4 başı ("İkinci" 33,15); cümle 3 biter 32,68 ("yanlış."), ara 0,47 sn | sahne 4 "Örnek 2" başı; söz: "İkinci kök. We used to live in a village, …" |

- Ders < 4 dk (91,54 sn) → 1 bildirim. Kart 33,15–36,15; son 20 sn sınırı 71,54'ün çok önünde.
- **Sapma:** %30 hedefi 27,46 sn'dir; bu an "ilk 30 sn içinde bildirim yok" kuralına takılır. 30 sn'den sonraki ilk cümle başı
  33,15'tir (%36,2). Sonraki aday 48,99 (%53,5) hedefe daha uzak. Cümle 3 içindeki "Burada" (30,84) bir söz cümlesinin başıdır ama
  `METIN.md` cümle sınırı değildir ve tuzağın cevabının üstüne düşer; seçilmedi.
- "İlk bilgi verildikten sonra" şartı sağlanır: 33,15'e kadar tanım ve ilk örnek (in 1911, begin–began–begun) bitmiştir.

## 5. Dilbilgisi iddiaları

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama 1. satır | ders üç ayrımı örneklerle gösterir (Simple Past ↔ Present Perfect, used to ↔ would, düzensiz fiil hâlleri) | kesin (`surumler.json` amaçlar; cümle 3, 4, 5) |
| Bölüm "Simple Past: bitmiş eylem, belli zaman" | Simple Past geçmişte bitmiş ve zamanı belli eylemi anlatır | jüri bakacak (cümle 2 tanımının özeti; Simple Past zaman bağlamdan anlaşılınca da kullanılır, ad "her zaman" demez) |
| Bölüm "In 1911 ve begin, began, begun tuzağı" | in 1911 belirli zaman; begin fiilinin hâlleri begin–began–begun | kesin (cümle 3) |
| Bölüm "Used to ve would: hangisi durum anlatır?" | soru; iddia yok (cevap derste: used to) | kesin |
| Bölüm "Asıl tuzak: ago ve yet aynı cümlede" | cümle 5'te ago ve yet aynı cümlede | kesin (cümle 5) |
| Bölüm "Ago varken has resigned olur mu?" | soru; iddia yok | kesin (cümle 6) |
| Gönderi 1. cümle | soru; iddia yok | kesin |
| Gönderi 2. cümle | ago geçmişte belli bir zamanı gösterir ve Present Perfect ile kullanılmaz; doğrusu resigned | kesin (standart İngilizcede Present Perfect, bitmiş zaman sözüyle (ago) kullanılmaz); jüri bağımsız doğrulasın |
| Gönderi 3. cümle | derste used to / would farkı ve begin, began, begun tuzağı var | kesin (cümle 3, 4) |
| Sabit yorum | iddia yok | kesin |
| "Sıradaki ders: Past Continuous" | 02-11'in konusu | jüri bakacak (kaynak `varlik/grammar/konu-adlari.json` GR-02-11, güven yüksek, transkript 863571351 [00:08]; katalog adı "02 - tenses - 11", durum planli) |

## 6. Açık noktalar

- **Ders içeriği (bu dosyaların dışında; dil jürisi ana derse de baksın, §1c):** (a) cümle 1 "Ago varsa Perfect yok." ve cümle 7
  "since varsa Perfect" "Present" demeden "Perfect" der; Past Perfect, aktarılan sözde ago ile kullanılabilir ("She said she had left
  two years ago"). (b) Cümle 7 "Present Perfect for, since, yet ister." zorunluluk gibi okunur; Present Perfect bu sözcükler olmadan
  da kurulur ("I have lost my keys"). (c) "since varsa Perfect": since yan cümlesinin kendisi çoğunlukla Simple Past alır ("since I
  moved here"). Bu metinlerin hiçbiri yayın verisine alınmadı.
- Kanca sahnesi raporunda takvimde `6 min` yazısı var (sahne 02 RAPOR: "takvim + saat (`6 min` 4,03)"). Süre sözü kuralı
  (skill `motion-grafik-ders`, 12.11) için görsel jüri bakmalı; kapsam dışı, dokunulmadı.
- Başlık "Simple Past | YDT İngilizce" 02-10 temel dersinde de aynı çıkabilir (kalıpta seviye yok). Kanalda iki aynı başlık riski:
  şef/panel kararı (ör. liste adı seviyeyi taşır; başlığa seviye eklenmesi kalıp değişikliği ister).
- `surumler.json` `ana-yatay.kapak` = `null`, `dikey-tam.kapak` = "SIMPLE PAST" (dosya adı değil, metin). Gönderi görseli paket
  kökündeki `kapak.png` (açık tema). Dikey pakette aynı ad dikey kapağı gösterir; topluluk gönderisinde hangisi kullanılacağı panel kararı.
- Bağlantı tabanı: bu dersin kısasında (`simple-past-ileri-s1`) `aciklama-a/b.md` YOK; emsal alınacak kısa açıklaması yoktur. Taban,
  site kuralından türetildi: `ydspublishing.com/grammar/<katalog kimliği>` (sözleşme K35; emsal `02-06-ydt-temel`, `02-04-ydt-temel`).
  Kimlik `02-10-ydt-ileri` (paket adı `simple-past-ileri` değil). `utm_campaign` büyük harf (HV-19). Adresin canlılığı ölçülmedi.
- Bildirim 33,15 sahne 3 → 4 geçişine (BookFlip, 12 kare) denk gelir. Kartın sayfa çevirme anında okunurluğuna görsel jüri bakmalı.
- Giriş klibi (≤ 3 sn) eklenirse damgalar ve bölüm `t` değerleri kayar; araç düzeltir (sözleşme §2). Açıklamaya bu not yazılmadı.
- Liste bağı: `sonraki` = `02-11-ydt-ileri` katalogda `planli`; yüklenene kadar bitiş ekranı ve "sıradaki ders" bağı boş kalır.
- Etiket "ileri" (`surumler.json`'dan) genel bir sözcük; arama değeri düşük. Kaynak etiket olduğu için kaldırılmadı.
- Künye `seviye: "YDT ADVANCED"` (İngilizce); kapak rozeti `YDT · İLERİ` (KAPAK-RAPOR). Başlıkta kitle "YDT" kullanıldı, çakışma yok.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0210I).

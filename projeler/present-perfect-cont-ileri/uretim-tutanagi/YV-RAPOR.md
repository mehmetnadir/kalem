# YV-RAPOR — present-perfect-cont-ileri YouTube yayın verisi · 15.11.2026 (istem YV-0209I)

| Dosya | Durum |
|---|---|
| `present-perfect-cont-ileri/youtube.json` | yazıldı, JSON ayrıştırıldı |
| `present-perfect-cont-ileri/youtube-aciklama.md` | yazıldı, 712 bayt, `utm_content=ana-yatay` |
| `present-perfect-cont-ileri-dikey/youtube.json` | yazıldı; ana paketle bayt bayt aynı (`cmp` farksız) |
| `present-perfect-cont-ileri-dikey/youtube-aciklama.md` | yazıldı, 712 bayt; tek fark `utm_content=dikey-tam` (`diff` 1 satır) |

Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`), sunucu oturumu (srv21). Jüri (YVJ) farklı modelle koşmalı (`juri-olcutleri.md` §1e).
Dikey paket: VAR (`present-perfect-cont-ileri-dikey`, `surumler.json` `dikey-tam` satırı). Dikey `zaman.json` ana paketten yalnız
`genislik`/`yukseklik` satırında ayrılır (`diff` 2 satır); sahne sınırları aynı. Dikeyin `ortak/anlatim` dizini ana paketin anlatımına bağdır
(sembolik bağ) → `bolumler` ve `bildirimler` dikeyin kendi dosyalarından hesaplandı, değerler aynı çıktı.

## 1. Ölçüm çıktısı

Betik `/tmp/yv_olc_0209i.py` (geçici, repo dışı; `/usr/bin/python3 -I`). İki paketin çıktısı `boyut` ve `utm` dışında aynı:

```
== present-perfect-cont-ileri JSON OK; ders süresi 85.93 boyut 1920 1080
YV-1 baslik 42 kr True
YV-5 etiket 7 ham kr 78 YouTube sayımı 90 yineleme False
YV-3 bölüm 5 ilk 0.0 süreler [17.25, 16.43, 15.52, 12.67, 24.06] min 12.67 hepsi sahne başı True ad kr [36, 36, 33, 28, 31]
YV-2 açıklama bayt 712 satır 15 damga birebir True 5 hashtag 5 utm ['ana-yatay']
bildirim 34.23 %39.8 cümle başı [4] önceki cümle sonu 33.68 ilk30 True son20 True sahne ['Örnek 2'] kart sonu 37.23
emoji [] görsel var [True]
sabitYorum cümle 1 gönderi cümle 3 soru ile başlar True
yasak söz []
YV-8 altyazı 26 ilk t0 1.0 son t1 85.01 <= süre True
== present-perfect-cont-ileri-dikey JSON OK; ders süresi 85.93 boyut 1080 1920
… (aynı değerler; utm ['dikey-tam'])
JSON-AYNI
```

Ders süresi = `zaman.json` son `t_son` = 85,93 sn. Pakette mp4 yok (`cikti*.mp4` bulunamadı); süre mp4 ile karşılaştırılamadı.

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 42 karakter; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu = `senaryo.json` `baslik` ve `surumler.json` `konu` ("Present Perfect Continuous"); kitle `surumler.json` `kitle` "YDT" |
| YV-2 | evet | 712 bayt (≤ 5.000). Sıra: değer cümlesi → kaydet → "Bölümler:" + 5 damga → "Sıradaki ders" → "Ders sayfası" (utm) → 5 etiket. Dil kısmına jüri (D) bakacak |
| YV-3 | evet | ilk damga 00:00; 5 bölüm; en kısa bölüm 12,67 sn (Durum fiili know). Yuvarlanmış damgalarla en kısa aralık 00:49 → 01:02 = 13 sn. Her `t` bir sahne `t_bas` değeri |
| YV-4 | evet (D bakacak) | iç ad kalmadı ("Giriş", "Kanca", "Örnek 1–3", "Soru + Form" yok); en uzun ad 36 karakter (≤ 40). Tablo §3 |
| YV-5 | evet | 7 etiket, ham 78 karakter; YouTube sayımı (boşluklu etikete 2 tırnak + virgüller) 90 (≤ 500); yineleme yok. Konu adı, zaman adları (Present Perfect Continuous, Present Perfect), kitle (YDT), "İngilizce", "gramer" var |
| YV-6 | evet (D bakacak) | mutlak kural sözü ("her zaman", "asla", "-ing almaz") yok; iddialar §5 tablosunda. Yazım denetimi elle yapıldı; kısaltma yalnız kalıbın istediği "YDT" |
| YV-7 | evet | katalog ünite 02 "Tenses" (`sira` 2), seviye adı "İleri"; konu GR-02-09 `sira` 9 → `liste.sira` 9; önceki `02-08-ydt-ileri` (`planli`), sonraki `02-10-ydt-ileri` (`uretimde`, proje `simple-past-ileri`; `katalog-durum.json`) |
| YV-8 | evet (pakette srt yok) | `altyazi.srt` paneldedir. `altyazi.json` 26 satır, ilk `t0` 1,00, son `t1` 85,01 ≤ 85,93 (dikeyde aynı dosya, bağ) |
| YV-9 | evet | `gorsel` = `kapak.png`; dosya iki pakette var (ana 1920 × 1080, dikey 1080 × 1920, açık tema; `KAPAK-RAPOR.md`). Gönderi, sabit yorum ve açıklamada emoji yok |

## 3. Bölüm tablosu

| Sahne (iç ad) | İzleyici adı | `t` (sn) | Damga | Süre (sn) |
|---|---|---|---|---|
| 1 Giriş + 2 Kanca (birleşti; Giriş 3 sn) | Süreç mi, sonuç mu? have been + -ing | 0,00 | 00:00 | 17,25 |
| 3 Örnek 1 | Since cümlesi: have been complaining | 17,25 | 00:17 | 16,43 |
| 4 Örnek 2 | Süreç ve sonuç: reading, finished | 33,68 | 00:34 | 15,52 |
| 5 Örnek 3 | Durum fiili know: have known | 49,20 | 00:49 | 12,67 |
| 6 Soru + Form | Have been knowing olur mu? Özet | 61,87 | 01:02 | 24,06 |

Damga kuralı (02-04 emsali): `t` en yakın saniyeye yuvarlanır. 33,68 → 00:34: cümle 3 biter 33,68, cümle 4 başlar 34,23 (aşağı yuvarlama
00:33 cümle 3'ün son sözüne düşerdi). 61,87 → 01:02: cümle 5 biter 61,95, cümle 6 başlar 62,42. 49,20 → 00:49: cümle 4'ün son sözü
"finished." 49,28'de biter; damga sözün son 0,28 sn'sine düşer. Yukarı yuvarlama (00:50) cümle 5'in ilk sözüne ("Üçüncü", 49,75'te başlar)
0,25 sn girerdi. Kural tutarlılığı için 00:49 kaldı.

## 4. Bildirim anları

| # | `t` (sn) | Ders payı | Cümle sınırı | Ekranda |
|---|---|---|---|---|
| 1 | 34,23 | %39,8 | cümle 4 başı (cümle 3 biter 33,68; ara 0,55 sn) | sahne 4 "Örnek 2", söz: "İkinci örnek." (34,23–35,27), ardından İngilizce örnek (35,52) |

- Ders < 4 dk (85,93 sn) → 1 bildirim. Kart 34,23–37,23; ilk 30 sn ve son 20 sn (65,93 sonrası) dışında; kart tek sahne içinde kalır.
- Cümle başları dosyası: pakette `baslar.json` YOK. Cümle başları `ortak/anlatim/kur.py` içindeki `baslar()` formülüyle salt okuma hesaplandı
  (`sozcukler.json` ilk sözcük `t0` − `sureler.json` ilk sözcük payı): 1,00 · 3,39 · 17,80 · 34,23 · 49,75 · 62,42 · 66,75. Değerler
  `altyazi.json` cümle ilk satırı `t0` ile birebir.
- %30 hedefi (25,78 sn) ilk 30 sn yasağının içinde kalır; iki kural bu kısa derste çatışır. 30 sn sonrası ilk cümle sınırı 34,23'tür
  (%39,8). Öteki adaylar: 49,75 (%57,9) daha uzak; 62,42 (%72,6) kartı 65,42'de biter, son 20 sn sınırına 0,51 sn kalır. 30,32
  ("Ana cümlede have been ve -ing gelir.") bir altyazı satırı başıdır, cümle başı değil; seçilmedi.
- Kart, İngilizce örnek cümle (35,52–40,24) ekrana gelirken görünür. Kart yeri (yatay sol alt; dikey ayrıca ölçülecek) ile örnek kartı
  çakışıyor mu: görsel jüri bakacak (`youtube-surumu-standart.md` §5.2).

## 5. Dilbilgisi iddiaları

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama 1. satır | Present Perfect Continuous kalıbı have/has been + -ing | kesin (cümle 2 "Have or has, plus been, plus the -ing form.") |
| Açıklama 1. satır | since bir ipucudur; been -ing süreci, have + fiilin üçüncü hâli sonucu anlatır | kesin (cümle 3, 4, 7; ders amaçları 2–3). Ayrım dersin kendi çerçevesidir, kural mutlak yazılmadı |
| Bölüm "Süreç mi, sonuç mu? have been + -ing" | kalıp have been + -ing | kesin (cümle 1–2) |
| Bölüm "Since cümlesi: have been complaining" | since'li cümlede have been complaining geçer | kesin (cümle 3 örneği; genelleme yok) |
| Bölüm "Süreç ve sonuç: reading, finished" | been reading süreç, have finished sonuç | kesin (cümle 4 "Süreç, been reading. Sonuç ve sayı, have finished.") |
| Bölüm "Durum fiili know: have known" | know bir durum fiilidir; örnekte have known geçer | kesin (cümle 5) |
| Bölüm "Have been knowing olur mu? Özet" | soru; iddia yok | kesin |
| Gönderi 1. cümle | Türkçe çift "okuyorum / bitirdim" ve soru | jüri bakacak (biçem: "hangisi been alır" konuşma dili) |
| Gönderi 2. cümle | süreç have been reading, sayıyla verilen sonuç have finished ile söylenir | kesin (cümle 4); ders bağlamından ayrı okunduğu için jüri bakacak |
| Gönderi 3. cümle | derste since ipucu ve durum fiili tuzağı var | kesin (cümle 2 "süre ipuçlarını ve iki tuzağı", cümle 3, 5–7) |
| Sabit yorum | dilbilgisi iddiası yok | kesin |
| "Sıradaki ders: Simple Past" | katalog sıra 10 = `02-10-ydt-ileri` = Simple Past | kesin (`katalog-durum.json` proje `simple-past-ileri`, onun `surumler.json` `konu` "Simple Past") |
| Etiket "Present Perfect" | have + üçüncü hâl = Present Perfect | kesin; ders bu adı söylemez ("Result: have plus the third form"), jüri bakacak |

## 6. Açık noktalar

- Bildirim %39,8: %30 hedefi ilk 30 sn yasağıyla çatışıyor (§4). Kısa dersler (< 100 sn) için standarda bir cümle gerekir; karar şefte.
- Ders süresi 85,93 sn; skill künyesindeki yatay ders hedefi 5–7 dk. Bölüm sayısı (5) en az 3 sınırını geçer; kapsam dışı gözlem.
- Kısa `present-perfect-cont-ileri-s1` paketinde açıklama dosyası yok (`aciklama*.md` bulunamadı; kısa henüz v2'ye çevrilmedi). Taban
  adres ve utm biçimi 02-04 ve 02-02 kısalarından alındı: `https://ydspublishing.com/grammar/<video kimlik>`, `utm_campaign` = ders kodu
  büyük harfle (`ING-YDT-GR-02-09-I`). Ders sayfası adresinin canlılığı ölçülmedi.
- Damga 00:49 sözün son 0,28 sn'sine düşer (§3). Damga yuvarlama kuralı sözleşmede yazılı değil; betik kapısı `int(t)` kullanırsa
  00:34 ve 01:02 damgaları "birebir değil" görünür.
- Giriş klibi (≤ 3 sn) eklenirse açıklama damgaları ve bölüm `t` değerleri kayar; araç düzeltir (sözleşme §2–3). Açıklamaya bu not yazılmadı.
- Liste bağı: `onceki` = `02-08-ydt-ileri` katalogda `planli`; YouTube'a yüklenene kadar bu bağ boş kalır.
- `surumler.json` `kapak` alanı: ana-yatay `null`, dikey-tam bir metin ("PRESENT PERFECT CONTINUOUS"), dosya adı değil. Gönderi görseli
  paket kökündeki `kapak.png` (açık tema). Dikey pakette aynı ad 1080 × 1920 kapağı gösterir; topluluk gönderisinde hangisinin
  kullanılacağı panel ya da şef kararı.
- Etiket "ileri" (`surumler.json`'dan) genel bir sözcük; arama değeri düşük. Kaynak etiket olduğu için kaldırılmadı. Eklenen 2 etiket:
  "Present Perfect", "durum fiilleri".
- Ana dersteki dilbilgisi iddiaları (dil jürisine, §1c; bu paketin metinlerine alınmadı):
  (a) cümle 5 ve 7 "Durum fiili -ing almaz" genellemedir; durum fiillerinin hareket anlamlı kullanımı -ing alabilir (ör. "I have been
  thinking about it"). (b) cümle 3 "Since, plus a simple past clause. Ana cümlede have been ve -ing gelir." since + geçmiş zamanlı yan
  cümleden sonra ana cümle Present Perfect de olabilir; dersin kendi 3. örneği ("We have known each other since …") bunu gösterir.
  (c) cümle 7 "Türkçede -yor süreci, -di sonucu söyler" yaklaşık bir köprüdür.
- Kapsam dışı gözlem: senaryo giriş rozeti "YDT · ADVANCED" ve künye `seviye: "YDT ADVANCED"` İngilizce; kapak rozeti "YDT · İLERİ"
  (huni v2 Ç4 kararı). Başlıkta kitle "YDT" kullanıldı, çakışma yok.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0209I).

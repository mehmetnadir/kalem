# YV-RAPOR — 02-04-ydt-temel YouTube yayın verisi · 15.11.2026 (istem YV-0204T)

| Dosya | Durum |
|---|---|
| `02-04-ydt-temel/youtube.json` | yazıldı, JSON ayrıştırıldı |
| `02-04-ydt-temel/youtube-aciklama.md` | yazıldı, 972 bayt, `utm_content=ana-yatay` |
| `02-04-ydt-temel-dikey/youtube.json` | yazıldı; ana paketle bayt bayt aynı (`cmp` farksız) |
| `02-04-ydt-temel-dikey/youtube-aciklama.md` | yazıldı, 972 bayt; tek fark `utm_content=dikey-tam` (`diff` 1 satır) |

Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`), sunucu oturumu. Jüri (YVJ) farklı modelle koşmalı (`juri-olcutleri.md` §1e).
Dikey paket: VAR (`02-04-ydt-temel-dikey`). Dikey `zaman.json` sahne sınırları ve `baslar.json` ana paketle aynı (`cmp` AYNI) →
`bolumler` ve `bildirimler` dikeyin kendi dosyalarından hesaplandı, değerler aynı çıktı.

## 1. Ölçüm çıktısı (betik, iki paket için aynı)

```
== 02-04-ydt-temel JSON OK; ders süresi 264.64
YV-1 baslik 52 kr True
YV-5 etiket sayısı 9 ham kr 115 YouTube sayımı (tırnak+virgül) 133 yineleme False
YV-3 bölüm 13 ilk 0.0 min süre 13.37 hepsi sahne başı True max ad kr 37
damga birebir True 13
YV-2 açıklama bayt 972 hashtag 5 utm ana-yatay
bildirim 69.39 %26.2 cümle başı ['5'] ilk30 True son20 True
bildirim 184.54 %69.7 cümle başı ['13'] ilk30 True son20 True
emoji False
gorsel var [True]
sabitYorum cümle 1 gönderi cümle 3
yasak söz []
== 02-04-ydt-temel-dikey … (aynı değerler; utm dikey-tam)
JSON-AYNI
```

Ders süresi `zaman.json` son `t_son` = 264,64 sn. `ffprobe cikti.mp4` = 265,676 sn (iki pakette); 1,04 sn fark kapanış kuyruğudur.
mp4 süresine göre de bildirimler %26,1 ve %69,5'tir; son 20 sn sınırı (245,68) aşılmaz.

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 52 karakter; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu = `senaryo.json` `baslik` ("Simple Present ve Present Continuous"); kitle künye/`surumler.json` "YDT" |
| YV-2 | evet | 972 bayt (≤ 5.000). Sıra: değer cümlesi → kaydet → "Bölümler:" + 13 damga → "Sıradaki ders" → "Ders sayfası" (utm) → 5 etiket. Dil kısmı jüri (D) bakacak |
| YV-3 | evet | ilk damga 00:00; 13 bölüm; en kısa bölüm 13,37 sn (Kapanış). Yuvarlanmış damgalarla en kısa aralık 04:11 → 264,64 = 13,6 sn. Her `t` bir sahne `t_bas` değeri |
| YV-4 | evet (D bakacak) | iç ad kalmadı ("Örnek 1", "Karşıt çift 1", "Kural kartı" yok); en uzun ad 37 karakter (≤ 40). Tablo §3 |
| YV-5 | evet | 9 etiket, ham 115 karakter; YouTube sayımı (boşluklu etikete 2 tırnak + virgüller) 133 (≤ 500); yineleme yok. Konu adı, zaman adları (EN + TR), kitle var |
| YV-6 | evet (D bakacak) | mutlak kural sözü ("her zaman", "asla") yok; iddialar §5 tablosunda. Yazım denetimi elle yapıldı; ünlü uyumu notu §6 |
| YV-7 | evet | katalog ünite 02 "Tenses" (`sira` 2); konu GR-02-04 `sira` 4 → `liste.sira` 4; önceki `02-03-ydt-temel` (uretimde), sonraki `02-05-ydt-temel` (planli) |
| YV-8 | evet (pakette srt yok) | `altyazi.srt` paneldedir. `altyazi.json` 47 satır, ilk `t0` 1,00, son `t1` 264,22 ≤ 264,64 (iki pakette aynı) |
| YV-9 | evet | `gorsel` = `kapak.png`; dosya iki pakette var (ana 1920×1080, dikey 1080×1920, açık tema; `KAPAK-RAPOR.md`). Gönderi, sabit yorum ve açıklamada emoji yok |

## 3. Bölüm tablosu

| Sahne (iç ad) | İzleyici adı | `t` (sn) | Damga | Süre (sn) |
|---|---|---|---|---|
| 1 Giriş + 2 Kanca (birleşti; Giriş 3 sn) | Yaşıyorum: I live mi, I am living mi? | 0,00 | 00:00 | 20,22 |
| 3 Örnek 1 | Genel durum ve konuşma anı: wear | 20,22 | 00:20 | 23,63 |
| 4 Örnek 2 | Kalıcı ve geçici durum: live | 43,85 | 00:44 | 24,99 |
| 5 Örnek 3 | Tarifeli ve planlanmış gelecek | 68,84 | 01:09 | 24,51 |
| 6 Soru anı 1 | Tren örneği: tarife mi, plan mı? | 93,35 | 01:33 | 20,02 |
| 7 Kural kartı | Üç fark tek kartta | 113,37 | 01:53 | 17,03 |
| 8 Karşıt çift 1 | Aynı sözcük today: konuşma anı | 130,40 | 02:10 | 14,89 |
| 9 Karşıt çift 2 | Saatle gelen today: tarife | 145,29 | 02:25 | 17,04 |
| 10 Tuzak ve soru anı 2 | Tuzak: Türkçedeki -yor eki | 162,33 | 02:42 | 21,46 |
| 11 Tuzak cevabı | I live ve I am living: anlam farkı | 183,79 | 03:04 | 21,51 |
| 12 Ara özet | Özet: hangi durumda hangi zaman? | 205,30 | 03:25 | 15,03 |
| 13 Mini soru | Mini soru: boşluğa hangi şık? | 220,33 | 03:40 | 30,94 |
| 14 Kapanış | Sınavda soracağın üç soru | 251,27 | 04:11 | 13,37 |

Damga kuralı: `t` en yakın saniyeye yuvarlanır. Gerekçe: aşağı yuvarlama 00:43 ve 01:08 damgalarında önceki cümlenin son sözüne düşer
(cümle 3 biter 43,85; cümle 4 biter 68,84). Yuvarlama ile her damga sahne başından en çok 0,5 sn sapar; ilk söz sahne başından 0,55 sn sonra gelir.

## 4. Bildirim anları

| # | `t` (sn) | Ders payı | Cümle sınırı (`baslar.json`) | Ekranda |
|---|---|---|---|---|
| 1 | 69,39 | %26,2 | cümle 5 başı (cümle 4 biter 68,84; ara 0,55 sn) | sahne 5 "Örnek 3", söz: "Üçüncü örnek. İki cümle de geleceği anlatıyor." |
| 2 | 184,54 | %69,7 | cümle 13 başı (cümle 12 biter 183,79; ara 0,75 sn) | sahne 11 "Tuzak cevabı", söz: "Olur, ama anlam değişir." |

- Ders ≥ 4 dk (264,64 sn) → 2 bildirim. İlk 30 sn ve son 20 sn (244,64 sonrası) dışında; her kart (3 sn) tek sahne içinde kalır.
- %30 hedefine en yakın `baslar.json` sınırı 69,39'dur (−3,8 puan). Öteki aday 93,90 (%35,5; öğrenci sorusu başı). 69,39 seçildi: daha yakın,
  ilk iki fark anlatılmış ("ilk bilgi verildikten sonra"), söz düşük yoğunluklu bir geçiş cümlesi.

## 5. Dilbilgisi iddiaları

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama 1. satır | iki zaman arasında üç kullanım farkı var; zaman cümlenin anlamına bakılarak seçilir | kesin (ders amaçları ve cümle 2, 8 ile aynı) |
| Bölüm "Genel durum ve konuşma anı: wear" | wears = genel durum, is wearing = konuşma anı | kesin (cümle 3) |
| Bölüm "Kalıcı ve geçici durum: live" | live = kalıcı, am living = geçici | kesin (cümle 4) |
| Bölüm "Tarifeli ve planlanmış gelecek" | iki gelecek kullanımı | kesin (cümle 5) |
| Bölüm "Tren örneği: tarife mi, plan mı?" | soru; iddia yok | kesin |
| Bölüm "Aynı sözcük today: konuşma anı" | "She is wearing … today" cümlesinde today konuşma anını gösterir | kesin (cümle 9) |
| Bölüm "Saatle gelen today: tarife" | "leaves at seven p.m. today" tarife cümlesi | kesin (cümle 10) |
| Bölüm "Tuzak: Türkçedeki -yor eki" | -yor eki yanıltabilir | kesin (cümle 11) |
| Bölüm "I live ve I am living: anlam farkı" | ikisi de dilbilgisi olarak doğru, anlam farklı | kesin (cümle 13 "Olur, ama anlam değişir") |
| Gönderi 2. cümle | "I live in Istanbul" kalıcı, "I am living with my uncle" geçici durumu anlatır | jüri bakacak (cümleler ders bağlamından ayrı okunur; "with my uncle" bağlamı derste "Ailem şehir dışında" ile kurulur) |
| Gönderi 1. cümle | Türkçede ikisi de "yaşıyorum" | kesin (cümle 1) |
| "Sıradaki ders: Stative Verbs" | 02-05'in konusu | jüri bakacak (kaynak: kısa açıklamaları + cümle 18 "-ing almayan fiiller"; katalogda 02-05 adı "02 - tenses - 05", durum planli) |

## 6. Açık noktalar

- `surumler.json` `kapak` alanı `null` (ana-yatay ve dikey-tam). Gönderi görseli paket kökündeki `kapak.png` (açık tema). Dikey pakette
  aynı ad dikeyin 1080×1920 kapağını gösterir; topluluk gönderisinde yatay mı dikey mi kullanılacağı panel/şef kararı.
- Damga yuvarlama kuralı sözleşmede yazılı değil (§3). Betik kapısı `int(t)` kullanırsa 00:44 / 01:09 / 03:04 damgaları "birebir değil" görünür.
- Giriş klibi (≤ 3 sn) eklenirse açıklama damgaları ve bölüm `t` değerleri kayar; araç düzeltir (sözleşme §2). Açıklamaya bu not yazılmadı.
- Ders sayfası adresi `https://ydspublishing.com/grammar/02-04-ydt-temel` kısaların açıklamasındaki tabandan alındı; canlılığı ölçülmedi
  (kısa açıklamasındaki UYARI aynen geçerli).
- Paketler arası tutarsızlık: kısa S1 başlığı ve açıklaması "I live **mı**" yazar; ünlü uyumuna göre "live" (/lɪv/) ardından "mi" gelir.
  Bu paket "I live mi" yazdı. S1 dosyasına dokunulmadı (yazma alanı dışı).
- Liste bağı: `sonraki` = `02-05-ydt-temel` katalogda `planli`; YouTube'a yüklenene kadar bitiş ekranı/sıradaki ders bağı boş kalır.
- Etiket "temel" (`surumler.json`'dan) genel bir sözcük; arama değeri düşük. Kaldırılmadı (kaynak etiket).
- Kapsam dışı gözlem: `ortak/youtube/bildirim/yer.json` köşe değeri `sol_alt` (x 240, y 900); `youtube-surumu-standart.md` §3 "sağ üst" der.
- Künye `seviye: "YDT BASIC"` (İngilizce); huni v2 rozet kararı `YDT · TEMEL`. Başlıkta kitle "YDT" kullanıldı, çakışma yok.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0204T).

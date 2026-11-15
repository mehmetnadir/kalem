# YV-RAPOR — simple-present-ileri YouTube yayın verisi · 15.11.2026 (istem YV-0202I)

| Dosya | Durum |
|---|---|
| `simple-present-ileri/youtube.json` | yazıldı, JSON ayrıştırıldı |
| `simple-present-ileri/youtube-aciklama.md` | yazıldı, 675 bayt, `utm_content=ana-yatay` |
| `simple-present-ileri-dikey/youtube.json` | yazıldı; ana paketle bayt bayt aynı (`filecmp` AYNI) |
| `simple-present-ileri-dikey/youtube-aciklama.md` | yazıldı, 675 bayt; tek fark `utm_content=dikey-tam` (`diff` 1 satır) |

Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`), sunucu oturumu (srv21). Jüri (YVJ-0202I) farklı modelle koşmalı (`juri-olcutleri.md` §1e).
Dikey paket: VAR (`simple-present-ileri-dikey`, `surumler.json` `dikey-tam` satırı). Dikey `zaman.json` sahne sınırları ana paketle aynı;
dikey `altyazi.json` ve `sureler.json` ana paketle bayt aynı (`cmp`). Dikeyin `bolumler` ve `bildirimler` değerleri dikeyin kendi
`zaman.json` ve `METIN.md` dosyasından hesaplandı; değerler ana paketle aynı çıktı.

## 1. Ölçüm çıktısı (betik, iki paket)

```
== simple-present-ileri JSON OK; ders süresi 90.43
YV-1 baslik 30 kr kalıp True
YV-5 etiket 12 ham kr 134 YouTube sayımı 161 yineleme False
YV-3 bölüm 5 ilk 0.0 süreler [17.65, 14.8, 15.84, 13.12, 29.02] min 13.12 hepsi sahne başı True max ad kr 36
damga birebir (round) True 5
YV-2 açıklama bayt 675 hashtag 5 utm_content ['ana-yatay'] campaign ['ING-YDT-GR-02-02-I']
sıra: ['Bu derste Simple P', 'Sınav günü bakmak ', 'Bölümler:', '00:00 Hangi zaman?', '00:18 Although cüm', '00:32 Durum fiille',
       '00:48 Tarifeli gel', '01:01 Will mi, Sim', 'Sıradaki ders: Pre', 'Ders sayfası: http', '#YDT #İngilizce #g']
bildirim 33.0 %36.5 ilk30 True son20 True
emoji False
gorsel var [True]
gönderi soru ile başlar True cümle 3
sabitYorum cümle 1
YV-8 altyazı son t1 89.51 <= 90.43 True
yasak söz []
== simple-present-ileri-dikey … (aynı değerler; utm_content ['dikey-tam'])
JSON-AYNI True
$ wc -c simple-present-ileri/youtube-aciklama.md simple-present-ileri-dikey/youtube-aciklama.md
 675 simple-present-ileri/youtube-aciklama.md
 675 simple-present-ileri-dikey/youtube-aciklama.md
```

Ders süresi `zaman.json` son `t_son` = 90,43 sn (iki pakette). Yasak söz taraması: "Tam ders", "dakika", " dk", "her zaman", "asla",
"always", "never", "Örnek 1", "Karşıt çift" (başlık, bölüm adları, açıklama, sabit yorum, gönderi).

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 30 karakter; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu = `senaryo.json` `baslik` ve `surumler.json` `konu` ("Simple Present"); kitle `surumler.json` "YDT". Başlık çakışması §6.1 |
| YV-2 | evet | 675 bayt (≤ 5.000). Sıra: değer cümlesi → kaydet → "Bölümler:" + 5 damga → "Sıradaki ders" → "Ders sayfası" (utm) → 5 etiket. Dil kısmına jüri (D) bakacak |
| YV-3 | evet | ilk damga 00:00; 5 bölüm; en kısa bölüm 13,12 sn ("Tarifeli gelecek", 48,29–61,41). Yuvarlanmış damgalarla en kısa aralık 00:48 → 01:01 = 13 sn. Her `t` bir sahne `t_bas` değeri |
| YV-4 | evet (D bakacak) | iç ad kalmadı ("Giriş", "Kanca", "Örnek 1–3", "Soru + Form" yok); en uzun ad 36 karakter (≤ 40). Tablo §3 |
| YV-5 | evet | 12 etiket, ham 134 karakter; YouTube sayımı (boşluklu etikete 2 tırnak + virgüller) 161 (≤ 500); yineleme yok. Konu adı (Simple Present), zaman adları (Simple Present, Present Simple, geniş zaman), kitle (YDT) var |
| YV-6 | evet (D bakacak) | mutlak kural sözü yok (tarama §1). İddialar §5 tablosunda. Yazım elle denetlendi: İngilizce sözcüğe kesme ekli Türkçe ek yazılmadı (ünlü uyumu tartışması yok) |
| YV-7 | evet | katalog ünite 02 "Tenses"; konu GR-02-02 `sira` 2 → `liste.sira` 2; seviye adı katalog `seviyeler.ileri` = "İleri". Önceki `02-01-ydt-ileri` (uretimde), sonraki `02-03-ydt-ileri` (uretimde) |
| YV-8 | evet (pakette srt yok) | `altyazi.srt` paneldedir. `altyazi.json` 22 satır, ilk `t0` 1,00, son `t1` 89,51 ≤ 90,43 (iki pakette aynı) |
| YV-9 | evet | `gorsel` = `kapak.png`; dosya iki pakette var (ana 1920×1080, dikey 1080×1920, açık tema; `KAPAK-RAPOR.md` satır 4–5, PNG başlığı okundu). Gönderi, sabit yorum ve açıklamada emoji yok |

## 3. Bölüm tablosu

| Sahne (iç ad) | İzleyici adı | `t` (sn) | Damga | Süre (sn) |
|---|---|---|---|---|
| 1 Giriş + 2 Kanca (birleşti; Giriş 3 sn) | Hangi zaman? Önce kural: s ve does | 0,00 | 00:00 | 17,65 |
| 3 Örnek 1 | Although cümlesinde zaman: it gives | 17,65 | 00:18 | 14,80 |
| 4 Örnek 2 | Durum fiilleri: owns ve costs | 32,45 | 00:32 | 15,84 |
| 5 Örnek 3 | Tarifeli gelecek: takes off tomorrow | 48,29 | 00:48 | 13,12 |
| 6 Soru + Form | Will mi, Simple Present mi? Özet | 61,41 | 01:01 | 29,02 |

Damga kuralı: `t` en yakın saniyeye yuvarlanır (sözleşme satırı "43,85 → 00:44"; kardeş paketler aynı). Damganın düştüğü söz:

| Damga | Söz |
|---|---|
| 00:18 | sessizlik (cümle 2 biter 17,65; "Birinci kök." başlar 18,20) |
| 00:32 | önceki bölümün son sözcüğü "gives." (31,65–32,45), sahne başından 0,45 sn önce |
| 00:48 | önceki bölümün son sözcüğü "almaz." (47,65–48,29), 0,29 sn önce |
| 01:01 | önceki bölümün son sözcüğü "tuzaktır." (60,61–61,41), 0,41 sn önce |

## 4. Bildirim anları

| # | `t` (sn) | Ders payı | Cümle sınırı (`METIN.md` "başlar") | Ekranda |
|---|---|---|---|---|
| 1 | 33,00 | %36,5 | cümle 4 başı (cümle 3 biter 32,45, altyazıda 32,53; ara 0,47 sn) | sahne 4 "Örnek 2", söz "İkinci kök." (33,00–33,88); kart 33,00–36,00 sahne içinde |

- Ders < 4 dk (90,43 sn) → 1 bildirim. Pakette `baslar.json` yok; cümle başları `METIN.md` "başlar" sütunundan (sözleşme satırı, simple-present-temel emsali).
- %30 hedefi 27,13 sn ilk 30 sn yasağına düşer. 30 sn sonrasındaki ilk cümle başı 33,00 alındı. Öteki adaylar: 48,84 (%54), 61,96 (%68,5), 66,43 (%73,5).
- 33,00'te ilk kök anlatılmış ("ilk bilgi verildikten sonra"); söz kısa bir geçiş cümlesi. 28,93 parça sınırı ("Bağlaç var…") ilk 30 sn içinde kaldığı için alınmadı.
- Son 20 sn sınırı 70,43; kart 36,00'da biter. Kart yeri `ortak/youtube/bildirim/yer.json`; sahne 4'teki İngilizce örnek kartı 34,13'te başlar, çakışmaya Nadir önizlemede bakacak.

## 5. Dilbilgisi iddiaları

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama 1. satır | ders Simple Present kuralını üç YDT soru kökünde uygular: bağlaçlı uzun cümle, durum fiilleri, tarifeli gelecek | kesin (cümle 2 "üç YDT kökü", cümle 3–5) |
| Bölüm "Hangi zaman? Önce kural: s ve does" | kural: he/she/it ile fiile s; olumsuz ve soruda does | kesin (cümle 2) |
| Bölüm "Although cümlesinde zaman: it gives" | although içeren cümlede ana fiil Simple Present kalır | kesin (cümle 3); genelleme yazılmadı, bkz. §6.6 |
| Bölüm "Durum fiilleri: owns ve costs" | own ve cost durum fiilidir | kesin (standart dilbilgisi listesi; cümle 4) |
| Bölüm "Tarifeli gelecek: takes off tomorrow" | tarifeli gelecek Simple Present ile söylenir | kesin (cümle 5) |
| Bölüm "Will mi, Simple Present mi? Özet" | soru; iddia yok | kesin |
| Gönderi 1. cümle | soru; iddia yok | kesin |
| Gönderi 2. cümle | tarifeli bir saat için Simple Present kullanırız: The flight takes off at nine. | kesin (tarife kullanımı; will'i dışlamaz) |
| Gönderi 3. cümle | derste durum fiilleri ve bağlaçlı uzun cümleler var | kesin (cümle 3, 4, 7) |
| Sabit yorum | bağlaç, durum fiili ve tarife örnekleri | kesin |
| Etiket "geniş zaman" | arama sözcüğü; denklik iddiası değil | jüri bakacak (§4 madde 4 yanlış denklik metin içindir; etiket kardeş paketlerle aynı) |
| "Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması" | 02-03-ydt-ileri konusu | kesin (`02-03-ydt-ileri/surumler.json` `konu`) |

Ana dersteki iddialar (yazılan metinlere girmedi; §1c gereği raporlanır, jüri bakacak):
- Cümle 6–7: öğrenci "will take off olmaz mıydı?" der, öğretmen "Hayır." der. "Our flight will take off at eleven tomorrow" dilbilgisi olarak doğrudur; tarifede Simple Present tipik seçimdir. "Hayır" will'i yanlış gösterir.
- Cümle 7: "Will is for predictions and sudden decisions." will'in öteki kullanımlarını (söz, teklif, gelecek bilgisi) saymaz.
- Cümle 4 ve 7: "ing almaz", "now gelse bile ing almaz": cost bazı bağlamlarda -ing alır ("This mistake is costing us a lot."). Kapsam sınırı yok (EK-5b).
- Kapak metni `YARIN ama WILL YOK` (gönderi görseli bu kapak): EK-5c adayı; kapak jürisi bakacak.

## 6. Açık noktalar

1. **Başlık çakışması:** `simple-present-temel` başlığı da "Simple Present | YDT İngilizce". Sözleşme kuralı (komşu derste çakışma → `surumler.json` `konu` alt başlığı) burada işlemez: `konu` alt başlıksız. Kardeş ileri paketlerin çoğu (simple-past, present-continuous, present-perfect-cont) aynı başlığı taşır; present-perfect-ileri alt başlık kullanır. Kalıp korundu. Hazır seçenek: "Simple Present: tarife ve durum fiilleri | YDT İngilizce" (56 karakter). Şef kararı.
2. **Dikey sürüm Shorts sayılabilir:** dikey 90,43 sn + giriş 3 + çıkış 20 = 113,43 sn ≤ 3 dk. YouTube bunu Shorts sayar; bölüm ve bildirim orada işlemeyebilir (sözleşme satırı, simple-present-temel). Şef kararı.
3. **Katalogda iki paket:** katalog `02-02-ydt-ileri` öğesinin `proje` alanı `02-02-ydt-ileri` paketini gösterir (419,12 sn, 16 sahne, kapak yok). İstem `simple-present-ileri` paketini (90,43 sn, 6 sahne, kapak var) verdi; veri bu pakete yazıldı. Panelin hangi paketi okuyacağı şef kararı.
4. **Giriş klibi:** giriş klibi eklenirse açıklama damgaları ve bölüm `t` değerleri kayar; araç düzeltir (sözleşme §3). Açıklamaya bu not yazılmadı.
5. **Damga yuvarlama:** 3 damga önceki bölümün son sözcüğüne düşer (0,29–0,45 sn, §3). Yukarı yuvarlama (00:33, 00:49, 01:02) sahne başından sonra düşer ama kardeş paket kuralından ayrılır. Betik kapısı `int(t)` kullanırsa 00:18 damgası "birebir değil" görünür.
6. **"Bağlaç var, zaman değişmez" (cümle 3):** genel kural olarak okunursa zaman bağlaçları (when, as soon as) için yanıltır. Bölüm adı genellemeyi taşımaz ("Although cümlesinde").
7. **Ders sayfası adresi:** `https://ydspublishing.com/grammar/02-02-ydt-ileri` kardeş paketlerin tabanından türedi (`simple-present-ileri-s1` pakette açıklama dosyası yok). Sözleşme satırına göre taban adres 15.11'de 404 verdi; bu adresin canlılığı ölçülmedi.
8. **Ders süresi:** 90,43 sn; skill hedefi yatay 5–7 dk. Bölüm sayısı 5 ile sınırlı kaldı.
9. **Zaman farkı:** `METIN.md` cümle 7 biter 89,43; `altyazi.json` son `t1` 89,51 (0,08 sn). Sonuca etkisi yok.
10. **`surumler.json` kapak alanı:** `ana-yatay` `null`; `dikey-tam` "TARİFE = SIMPLE" (metin; dosya adı değil, `KAPAK-RAPOR.md` metni `YARIN ama WILL YOK` ile de uyuşmaz). Gönderi görseli paket kökündeki `kapak.png`.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0202I).

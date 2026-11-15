# YV-0206T — `present-perfect-temel` YouTube yayın verisi · öz denetim · 15.11.2026

Üretici model: Claude Opus 5.5 (`claude-opus-5-5`), tek oturum, alt ajan yok. Jüri bu modelden farklı bir modelle koşmalı (`juri-olcutleri.md` §1e).
Yazılan dosyalar: `present-perfect-temel/youtube.json`, `present-perfect-temel/youtube-aciklama.md`, `present-perfect-temel-dikey/youtube.json`,
`present-perfect-temel-dikey/youtube-aciklama.md`, bu rapor. Dikey paket VAR (`surumler.json` `dikey-tam` → `proje: present-perfect-temel-dikey`).

Kaynaklar: `senaryo.json` (başlık "Present Perfect", kitle YDT), `surumler.json` (`video.etiketler`, `kod` ING-YDT-GR-02-06-T), `zaman.json`
(6 sahne, ders 94,86 sn), `ortak/anlatim/METIN.md` (cümle başları sütunu; pakette `baslar.json` yok), `ortak/anlatim/altyazi.json` (23 satır),
`ortak/kunye.js` (kitle YDT), `D/varlik/grammar/katalog.json` (ünite 02 "Tenses", GR-02-06 `sira` 6), `D/varlik/grammar/konu-adlari.json`
(GR-02-07 adı). Bağlantı tabanı ve utm biçimi: bu dersin kısasında (`present-perfect-temel-s1`) açıklama dosyası YOK; emsal 02-02 ve 02-04 kısalarının
`aciklama-*.md` dosyaları ve 02-04 / 02-02 ana YV dosyaları (`https://ydspublishing.com/grammar/<video kimliği>`, `utm_campaign` = `meta.kod` büyük harf).

## 1. Ölçüm (komut çıktısı)

Komut: `/usr/bin/python3 -I -` (iki paketin `youtube.json` ve `youtube-aciklama.md` dosyasını ayrıştırır; `len()` = karakter, `rb` okuma = bayt).
Ana paketin çıktısı aşağıdadır. Dikey paketin çıktısı utm satırı dışında aynıdır (`utm_content=dikey-tam`).

```
== present-perfect-temel ders sn 94.86
baslik 31 'Present Perfect | YDT İngilizce' kalip True
etiket sayi 15 duz toplam 158 virgullu 172 yineleme 0
  var: present perfect True
  var: ydt True
  var: i̇ngilizce True
  var: gramer True
  bolum t=0 sure=18.73 sahne_basi=True ad_kr=38 nfc=True damga=00:00 | Kaybettim: geçmişte oldu, sonucu şimdi
  bolum t=18.73 sure=15.43 sahne_basi=True ad_kr=32 nfc=True damga=00:19 | Have + üçüncü hâl: I have broken
  bolum t=34.16 sure=16.96 sahne_basi=True ad_kr=39 nfc=True damga=00:34 | For ve since: has played for five years
  bolum t=51.12 sure=16.07 sahne_basi=True ad_kr=38 nfc=True damga=00:51 | Deneyim: I have never flown in a plane
  bolum t=67.19 sure=27.67 sahne_basi=True ad_kr=38 nfc=True damga=01:07 | Neden hep üçüncü hâl? Sinyal sözcükler
  ilk0 True en az3 True min sure 15.43
  bildirim 34.71 oran 36.6% ilk30 disi True son20 disi True sayi 1 <4dk True
  sabitYorum cumle 1 110
  gonderi g1 gorsel var True soru ile baslar izcede hangi zamanla söylersin
  gonderi cumle sayisi 3
  aciklama bayt 684 satir 15
  damga eslesme True
  utm ['https://ydspublishing.com/grammar/02-06-ydt-temel?utm_source=youtube&utm_medium=video&utm_campaign=ING-YDT-GR-02-06-T&utm_content=ana-yatay']
  etiket satiri ['#YDT #İngilizce #gramer #PresentPerfect'] adet 4
  emoji []
altyazi satir 23 son t1 93.94
katalog unite Tenses konu sira 6 ['02-05-ydt-temel', '02-07-ydt-temel']
json-ayni        (cmp: iki paketin youtube.json dosyası bayt bayt aynı)
13c13            (diff: açıklamalar yalnız 13. satırda ayrılır: ana-yatay / dikey-tam)
```

Sabit yorum düzeltmesinden sonra (`örneğe` → `bölüme`) iki `youtube.json` yeniden ayrıştırıldı: ikisi de geçerli JSON, `sabitYorum` 110 karakter, `cmp` aynı.

## 2. `juri-olcutleri.md` §2f öz denetim

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | "Present Perfect \| YDT İngilizce" = 31 karakter (≤ 100). Kalıp `<Konu> \| <kitle> İngilizce`: konu = `senaryo.json` `baslik` ve `surumler.json` `konu`; kitle = `kunye.js` "YDT", `senaryo.json` `kitle` YDT |
| YV-2 | evet (B) · D jüri bakacak | 684 bayt (≤ 5.000), 15 satır. Sıra: satır 1 değer cümlesi → satır 2 kaydet → satır 4 "Bölümler:" + satır 5–9 damgalar → satır 11 sıradaki ders → satır 13 bağlantı (utm 4 alanı) → satır 15 etiket satırı (4 etiket, ≤ 5) |
| YV-3 | evet | İlk damga 00:00; 5 bölüm; süreler 18,73 · 15,43 · 16,96 · 16,07 · 27,67 sn (en kısa 15,43 ≥ 10). Her `t` bir `zaman.json` sahne başı. Sahne 1 "Giriş" (3,0 sn) tek başına < 10 sn → "Kanca" ile birleşti |
| YV-4 | evet (öz) · D jüri bakacak | Bölüm tablosu §3. İç ad ("Örnek 1", "Soru + Form") yok; her ad sahnenin söylenen içeriğinden. En uzun ad 39 karakter (≤ 40) |
| YV-5 | evet | 15 etiket; düz toplam 158, virgülle birleşik 172 karakter (≤ 500). Konu "Present Perfect", zaman adı "Present Perfect Tense", kitle "YDT", "İngilizce", "gramer" var. Büyük/küçük harf duyarsız yineleme 0. `surumler.json` 4 etiketi (İngilizce, temel, gramer, Present Perfect) içinde |
| YV-6 | öz denetim evet · D jüri bakacak | Her iddia §5'te. Emoji taraması 0 (iki paket, iki dosya). Yazım: "hâl", "hâlâ", "İngilizcede", "Present Perfect'i" denetlendi |
| YV-7 | evet | Katalog ünite 02 `ad` "Tenses", kitle `ydt` → "YDT", seviye `temel` → "Temel" → "Tenses · YDT Temel". GR-02-06 `sira` 6. Önceki `02-05-ydt-temel` (GR-02-05, `planli`), sonraki `02-07-ydt-temel` (GR-02-07, `planli`) |
| YV-8 | evet (json yarısı) · srt yarısı kanıt yok | `altyazi.json` 23 satır, son `t1` 93,94 ≤ ders 94,86. srt türetimi panelin işi (`youtube-saf.test.ts`); bu worktree'de ölçülmedi |
| YV-9 | evet | `gorsel` = `kapak.png`: pakette var, 1920×1080, `KAPAK-RAPOR.md` satır 4 "açık". Dikeyde aynı ad 1080×1920 açık kapağı gösterir (satır 5). Gönderi metninde emoji 0. Not: `surumler.json` `ana-yatay.kapak` = `null`; dosya adı yalnız `youtube.json` içinde geçer (§6) |

## 3. Bölüm tablosu

| `t` (sn) | Damga | İç ad (`zaman.json`) | İzleyici adı | Süre (sn) | İçerik kanıtı (METİN.md) |
|---|---|---|---|---|---|
| 0 | 00:00 | Giriş + Kanca | Kaybettim: geçmişte oldu, sonucu şimdi | 18,73 | cümle 1–2: "Kaybettim, kapıda kaldım." · "Anahtarı kaybettim: geçmişte oldu, ama sonucu şimdi bizimle." |
| 18,73 | 00:19 | Örnek 1 | Have + üçüncü hâl: I have broken | 15,43 | cümle 3: "I have broken my phone." · "Have, artı fiilin üçüncü hâli." |
| 34,16 | 00:34 | Örnek 2 | For ve since: has played for five years | 16,96 | cümle 4: "My brother has played the guitar for five years." · "For süreyi söyler. Başlangıç olsaydı since derdik." |
| 51,12 | 00:51 | Örnek 3 | Deneyim: I have never flown in a plane | 16,07 | cümle 5: "I have never flown in a plane." · cümle 7: "never ve ever deneyim" |
| 67,19 | 01:07 | Soru + Form | Neden hep üçüncü hâl? Sinyal sözcükler | 27,67 | cümle 6 (öğrenci): "Neden hep üçüncü hâl?" · cümle 7: "For ve since süre, never ve ever deneyim, just ve already yeni biten iş." |

Damga kuralı: `youtube.json` sahne başını ondalıklı tutar; açıklamadaki damga en yakın saniyedir (02-02 ve 02-04 emsali). Her damga sözden önce
düşer: söz başları 19,28 · 34,71 · 51,67 · 67,74. Bölüm 4 adındaki "Deneyim" sözcüğü sahne 5'te değil, cümle 7'de geçer; sahne 5 aynı fikri
"hayatın bugüne kadarki kısmı" diye söyler.

**Giriş klibi notu (açıklamaya yazılmadı):** YouTube sürümüne giriş klibi (≤ 3 sn) eklenince damgalar giriş süresi kadar kayar. Paketteki değer ders
zamanıdır; kaydırmayı API ve araç yapar (`youtube-yayin-verisi-sozlesme.md` §3). İlk damga 00:00 kalır.

## 4. Bildirim anı

| Ölçü | Değer |
|---|---|
| Ders süresi | 94,86 sn (< 4 dk) → 1 bildirim |
| ≈ %30 | 28,46 sn → ilk 30 sn yasağının içinde |
| Seçilen an | **34,71 sn** (%36,6), `sure` 3,0 → kart 34,71–37,71 |
| Cümle sınırı | `METIN.md` cümle 4 başı "İkinci örnek."; önceki cümle 3 34,16'da biter (0,55 sn sessiz); Örnek 2 sahnesi 34,16'da açılır |
| İlk 30 sn / son 20 sn | 34,71 ≥ 30 · 37,71 ≤ 94,86 − 20 = 74,86 |
| Neden bu an | 30 sn sonrasındaki ilk cümle başı. Öteki adaylar: 51,67 (%54,5), 67,74 (%71,4; kart 70,74'te biter, sınırda). İlk bilgi (form: "have, artı fiilin üçüncü hâli", 31,44–34,16) bu andan önce verildi |
| Seçenek (şef karar verir) | `altyazi.json` satır başı 31,44 sn ("Have, artı fiilin üçüncü hâli.", %33,1). Önceki tümce "İki parça var: have ve broken." 31,29'da biter. Gerçek tümce sınırıdır ama `METIN.md` cümle başı değildir |

Görsel çakışma: kart 36,00–39,12 arasında ekrandaki İngilizce örnekle ("My brother has played the guitar for five years.") aynı anda durur.
Yer sol alt (`ortak/youtube/bildirim/yer.json`). Render yok kuralı gereği kare çekmedim; çakışma görsel jürinin işidir (YT kapısı 2).

## 5. Dilbilgisi iddiaları

| Metin | Yer | Hüküm |
|---|---|---|
| "have / has ile fiilin üçüncü hâli" | açıklama satır 1, gönderi | kesin (form; broken, played, flown üçüncü hâl) |
| "for ile since farkı" | açıklama satır 1 | kesin (ders cümle 4 bu farkı anlatır; iddia ad düzeyinde) |
| "never, ever, just, already gibi sinyal sözcükler" | açıklama satır 1 | jüri bakacak: "sinyal" yumuşak söz, mutlak kural değil. Bu sözcükler başka zamanlarla da gelir (Amerikan İngilizcesinde just / already + Simple Past). Ders bu sözcükleri yalnız özet cümlesinde (81,63–88,83) sayar |
| "Kaybettim: geçmişte oldu, sonucu şimdi" | bölüm 1 | jüri bakacak: dersin kendi cümlesinin kısaltması; "Türkçe -dı = Present Perfect" denkliği kurmaz |
| "Have + üçüncü hâl: I have broken" | bölüm 2 | kesin |
| "For ve since: has played for five years" | bölüm 3 | kesin (örnek cümle doğru; has, tekil özne) |
| "Deneyim: I have never flown in a plane" | bölüm 4 | kesin (deneyim kullanımı; flown = fly üçüncü hâl) |
| "Neden hep üçüncü hâl? Sinyal sözcükler" | bölüm 5 | iddia yok (öğrenci sorusu) |
| "Anahtarını kaybettin ve hâlâ kapıdasın: bunu İngilizcede hangi zamanla söylersin?" | gönderi | jüri bakacak: soru tek doğru zaman ima eder. Sonucu şimdi süren olayda Present Perfect doğaldır; "I lost my key" de dilbilgisine uygundur (özellikle Amerikan İngilizcesi). Metin ötekini yanlış saymaz |
| "Present Perfect dersinde … üç örnekle gösteriyoruz" | gönderi | kesin (3 örnek: broken, played, flown) |
| "Sıradaki ders: Present Perfect: Since & For" | açıklama satır 11 | jüri bakacak: ad `konu-adlari.json` GR-02-07 (güven "yuksek"); kanıt alıntısı "Present Perfect Tense konu anlatımımıza devam ediyoruz." since/for sözünü taşımaz. Paket yok, `planli` |

Kısaltma: açıklama metninde kısaltma yalnız etiket satırındadır (`#YDT`). Başlıktaki "YDT" kalıbın gereğidir.

## 6. Açık noktalar

1. **Başlık çakışması yok:** `present-perfect-ileri` (`02-06-ydt-ileri`) konusu da "Present Perfect"; eş zamanlı YV işi o dersin başlığını ayırdı ("Present Perfect: since, for ve ago tuzağı | YDT İngilizce", 15.11 okundu). Temel ders kalıbın yalın biçimini taşır.
2. **Gönderi görseli adı:** `surumler.json` `ana-yatay.kapak` = `null`; `dikey-tam.kapak` bir metin ("KAYBETTİM = I HAVE LOST"), dosya adı değil. `kapak.png` adını `KAPAK-RAPOR.md` satır 4'ten aldım. API dosya izin listesi `youtube.json` adlarını da sayar, ama `surumler.json` `kapak` alanı doldurulmalı.
3. **Kapak kusuru:** `KAPAK-RAPOR.md` satır 18: karakter kolunda temizlenmemiş 2 beyaz bölge (düzeltilmedi). Gönderi görseli olarak paylaşılırsa görünür.
4. **Dikey sürüm Shorts sayılabilir:** dikey ders 94,86 sn. YouTube 3 dk'ya kadar dikey videoyu Shorts sınıfına alabilir (doğrulanmadı). Shorts'ta bölüm damgası, bildirim kartı ve bitiş ekranı çalışmayabilir. Karar şefte.
5. **Dikey gönderi:** iki `youtube.json` aynı; dikeyde `kapak.png` 1080×1920 açık kapaktır. Topluluk gönderisi ders başına bir kez paylaşılmalı (ana sürümden), yineleme olmamalı.
6. **Bağlantı canlılığı:** `https://ydspublishing.com/grammar/02-06-ydt-temel` emsal kısalardaki tabandan türedi; adres açılıp ölçülmedi. Bu dersin kısasında (`present-perfect-temel-s1`) açıklama dosyası yok, kısa v2'ye çevrilmemiş.
7. **v1 rozet metni:** `ortak/kunye.js` satır 52 `seviye: "YDT BASIC"` ve `senaryo.json` `giris.rozetler` "YDT · BASIC" taşır (huni-v2 §9 açık işi; yazma alanım dışı, dokunmadım).
8. **Liste komşuları:** `02-05-ydt-temel` ve `02-07-ydt-temel` katalogda `planli`; YouTube'a yüklenene kadar bitiş ekranı ve sıradaki ders bağı boş kalır.
9. **Bildirim anı %36,6:** standart "≈ %30" ile "ilk 30 sn yok" kuralı 95 sn'lik derste çakışır. Standarda "≈ %30 ya da ilk 30 sn sonrasındaki ilk cümle başı" yazılması önerilir (02-02 jürisi de önerdi).
10. **`yet`:** `surumler.json` `amaclar` "yet" sözcüğünü sayar; ders anlatımında "yet" geçmez. Etikete ve açıklamaya koymadım.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0206T).

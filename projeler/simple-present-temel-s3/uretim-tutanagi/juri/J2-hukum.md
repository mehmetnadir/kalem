# J2 hükmü — simple-present-temel-s3 (yayındaki kısa, kol a) · ÇIKTI jürisi · 15.11.2026

**Jüri modeli: Claude Sonnet 5.5 (`claude-sonnet-5-5`).**
Üretici modeli: sahne kodunu agy `kod` rolü yazdı (gemini-3.8-flash-high, sahne RAPOR.md dosyaları). Şef oturumunun modeli hiçbir raporda yazılı değil: **bilinmiyor**. Jüri ile üretici aynı aile olabilir; bu risk kapanmadı (juri-olcutleri §1e).

Ölçüt kaynağı: `juri-olcutleri.md` §1, §2a, §2c (hepsi); §2b'den yalnız bulgu çıkan maddeler. Üretim dosyalarını değiştirmedim; tek yazdığım dosya bu hüküm.
Küçük görünüm denemesi için 168 px indirmeleri `/tmp/j2s3/` altında yaptım (pakete girmez).

## Özet

| Hüküm | Sayı |
|---|---|
| Geçti (evet) | 34 |
| Kaldı (hayır) | 8 |
| Kanıt yok (= kaldı) | 4 |
| **Toplam kaldı** | **12** |

**Karar: KALDI.** Teslim kapısı (EK-4 / D-0338): önizleme adresi Nadir'e ve karta yazılmamalı.

En ağır 3 kusur: (1) 8 sahnenin hepsinde ve 5 türev karesinde rozet `YDT · BASIC` (standart `YDT · TEMEL`); çağrı karesinde ikisi aynı anda görünür. (2) Kural cümlesi `he, she, it` kapsamını söylemiyor; "geniş zaman eki = s" yanlış denkliği paket metaverisinde duruyor. (3) Karakter erkek, `kadro.ogrenci` kadın ve çağrıyı kadın ses okuyor (K22).

## Zaman damgaları (§1b)

| Kayıt | Zaman |
|---|---|
| Eski jüri `juri/s3.dil.md` | 15.11 18:54 (dosya zamanı) |
| Eski jüri `juri/s3.kaynak-kural.md` | 15.11 18:57 |
| `senaryo.json`, `sureler.json`, `zaman.json`, ses | 19:05–19:06 (v2 çevirisi, jüriden sonra) |
| Sahne HTML ve kare dosyaları | 19:27–19:54 |
| Son içerik dosyası (`hikaye-b.png`, `sahneler/08*/proje/index.html`) | 15.11 19:54:51 |
| `git log -1 -- projeler/simple-present-temel-s3` | 2026-11-15T20:06:16+03:00 (commit e745ad1) |

Eski jüri 57 dk ile 1 sa önce yazıldı, TASLAĞA baktı (`*-taslak.md`). Bu hüküm J2 ilk ÇIKTI jürisidir.

## Madde tablosu — §1 yapı

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| §1b jüri zamanı > son içerik zamanı | **hayır** | tablo yukarıda | eski jüri paketten eski; J2 bu boşluğu kapatır ama aşağıdaki düzeltmelerden sonra yeniden koşmalı |

## §2a — kısa video (huni v2)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | kare `01…-0.png` (0. sn), `02-paperjs-deger-8.4.png` (orta), `04-hyperframes-cagri-25.png` (son); piksel ölçümü 55 karede kanal bandı (y 285–345, x 60–600) dolu | logo x 60, `@ydspublishing` aynı bantta |
| HV-2 | evet | `senaryo.json` cümle 4 `"ses":"ogrenci"` (`oPC5I9GKjMReiaM29gjY`); `sentez.wav.rapor.json` | sesi dinlemedim; kayıt ve rapor |
| HV-3 | evet | `senaryo.json` cümle 4: "Dersin tamamı YDS Publishing YouTube kanalında."; Whisper "YEDESE Publishing…" benzerlik 1,0 | birebir |
| HV-4 | evet | `grep -rniE 'tam ders'` html/md/json/js (tutanak dizini hariç): 0 isabet; `ortak/kunye.js` dahil | sahne SPEC/RAPOR dosyaları "tam ders" sözünü yasak olarak anar; yüzey değil |
| HV-5 | evet | `dakika`, `dk` taraması: 0 yüzey isabeti | açıklama başlığındaki "25,08 sn" yayın metni değil, tutanak satırı |
| HV-6 | evet | sahne 3 `Kaydet` (kare 16.6); `aciklama-a.md` ve `aciklama-b.md` ilk satır "Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında." | |
| HV-7 | evet | `04-hyperframes-cagri-25.png`: ana kapak kartı x 60–960, y 620–1125; `ortak/kapak/ana-kapak.png` sha256 = `simple-present-temel/kapak.png` | kart sarı `GİDER = GOES` |
| HV-8 | evet | `senaryo.json` | 6/6: sınavda çıkar · en çok yanılınan · tek cümle · Türkçe köprü (`O gitmez.` / `O gider mi?`) · dersi izlemeden anlaşılır · sınav günü bakılır. Kapsam notu EK-5b'de |
| HV-9 | evet | `find projeler/simple-present-temel-s3 -name '*.mp4'`: boş | |
| HV-10 | evet | piksel sayımı 55 karede: y 0–280 koyu piksel 0, y 1570–1920 koyu piksel 0 | altyazı en alçak y ≈ 1520 |
| HV-11 | evet | `zaman.json`: 4 sahne, toplam 25,08 sn | hedef 22–26 |
| HV-12 | evet | `sureler.json`/`METIN.md`: ilk söz 1,00 sn; kanca biter 3,89 sn | eşik 1,00'da; sınırda, geçiyor |
| HV-13 | evet | `kaydet-16.6.png` ile `-18.png` kart bölgesi (x 60–960, y 560–900) piksel farkı 0; `zamanlar.json` kart tam 15,31 → 18,18 (2,87 sn); yer imi SVG; "Kaydet" hapı | emoji yok |
| HV-14 | evet | `cagri-25.png`: giriş sözü "Bu sadece başlangıç." Fredoka 700; kart y 620–1125; `@ydspublishing · YouTube` satırı | rozet kusuru EK-RZ'de |
| HV-15 | evet | "Bu sadece başlangıç." listede; s1 "Gerisi bizde.", s2 "Bitmedi, gel." — yineleme yok | |
| HV-16 | evet | "Bir arkadaşına gönder; o da karıştırıyor." listede; s1 "Sınavdan önce lazım olacak. Kaydet.", s2 "Bu kuralı kaybetme. Kaydet." | |
| HV-17 | evet | `ses-sozluk.json`: `"YDS": "YeDeSe"`; `sentez.wav.rapor.json` `ses_metni` "YeDeSe Publishing" | Whisper "YEDESE" duyuyor; standart §9 bunu kabul etti |
| HV-18 | evet | iki açıklama dosyasında ilk satır aynı; Reels ve TikTok metninde adres yok ("profildeki bağlantı") | |
| HV-19 | **hayır** | `grep utm_campaign` 6 paket: s3 büyük harf (`ING-YDT-GR-02-02-T`); `02-04-ydt-temel-s2` ve `s2b` `aciklama*.md` içinde küçük harf `ing-ydt-gr-02-04-t` (16 kayıt) | s3 kendi biçimi doğru; paketler arası tutarlılık bozuk. `utm_content=s3-a` / `s3-b` biçimi doğru |
| HV-20 | evet | `kapak-a|b|c.png` (kanal katmanı var, altyazı yok, A karakterli); `hikaye-a|b.png`; `aciklama-a|b.md` | `kapak.png` = A, `hikaye.png` = A (aynı boyut) |
| HV-21 | evet | `hikaye-a.png`, `hikaye-b.png`: kanal + kural + Kaydet; y 1150–1380 boş zemin (ölçüm: y 1570+ boş, y 1150–1380 görsel boş) | |
| HV-22 | **kanıt yok** | 8 sahne `RAPOR.md` "0 uyarı" diyor; `araclar/cakisma-kapisi.mjs` bu makinede yok, kapı çıktısı dosyası yok | gözle 10 karede çakışma görmedim; rapor cümlesi kanıt değil |
| HV-23 | evet | `sentez.wav.rapor.json`: çağrı parçası 1,0; en düşük parça 0,93 (`/dʌz/ varsa…`) | ≥ 0,9 |

## §2c — kapak ve hikâye karesi

Not: KS-1…KS-3 ders kapağı için yazılmış (yatay+dikey). Kısa kapağını `huni-v2` §6 ve §2 yerleşimi yönetir. Bu üç maddeyi kısa kapağına uyarlayarak yorumladım; standart kısa için sarı zemin ve sol %55 düzenini tanımlamıyor (ölçüt boşluğu, şef karar versin).

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| KS-1 | evet | `kapak-a|b|c.png` 1080×1920 (`file`); koyu karşılıkları `sahneler/0[567]*/k/koyu/kapak-*-koyu.png` | kökte koyu PNG yok; kısa YouTube'a yalnız açık gider |
| KS-2 | evet | kapak-a/b/c: ana yazı 2 satır Fredoka 700; sağ alt %15×%8 (x 918–1080, y 1766–1920) boş; kenar ≥ 60 px | ana yazı ortalı, huni §2 yerleşimi |
| KS-3 | evet | açık zemin `#f7f3ea`, koyu zemin `#1b1a17` (tema anayasası); koyu karede 10 px krem çıkartma kenarı görünür (`kapak-a-koyu.png`) | sarı `#fece00` zemin ders kapağına özgü |
| KS-4 | **hayır** | `kapak-c.png`: "DOES VARSA FİİL YALIN" | kural cümlesinin TAMAMI; kapak §3 "kural cümlesinin tamamını vermez" der. Aynı cümle sahne 3 kartı, hikâye B ve A başlığı. Kapak-a ve b geçer (3 ve 4 sözcük, merak bırakır) |
| KS-5 | **hayır** | `projeler/simple-present-temel-s3/ortak/kapak/` içinde `KAYNAK.json` yok; ana paketteki `KAYNAK.json` var (karakter.png sha256 aynı: a4198903…) | görselde yazı/harf/rakam/logo yok (kapak-a, b, c bakıldı); model `nano-banana-2` kaydı yalnız ana pakette |
| KS-6 | **kanıt yok** | `kapak-168.png` dosyası yok | 168×299 indirmemde kapak-a ("BU CÜMLE YANLIŞ") ve kapak-c okunuyor; yine de kanıt dosyası eksik |
| KS-7 | evet | `kapak-c.png` "FİİL" (büyük İ), `kapak-a.png` "YANLIŞ" (Ş), "CÜMLE" (Ü) | yedek yazı tipine düşme görmedim |
| KS-8 | evet | kapak-a/b/c, hikâye-a/b | taşma yok; kapak-c başlık x 65–955 |
| KS-9 | evet | 5 PNG + 5 koyu PNG + sahne kareleri | `✓`, `✗`, yer imi, uçak: SVG çizim; emoji değil |
| KS-10 | **hayır** | `senaryo.json` `kadro.ogrenci`: `cinsiyet:"kadin"`, `sac:"LongBangs"`; `ortak/kapak/KAYNAK.json` (ana paket): karakter "genç erkek, iri kıvırcık saç"; kapak-a, kanca ve çağrı karelerinde erkek figür | çağrıyı kadın ses (Gökçe Deniz) okuyor; ekranda erkek figür (K22). Ana derste aynı karakter |

## Ek maddeler (§2b ve jüri gözlemi)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| EK-RZ rozet metni (huni §9 açık iş, KS rozet) | **hayır** | 8 sahne + 5 türev + 5 koyu türev karesinde `YDT · BASIC`; `cagri-25.png` aynı karede kartın içinde `YDT · TEMEL` | `BRIEF-S3.md` satır 21 `YDT · BASIC` yazıyor; kaynak orada. Standart `YDT · TEMEL` ister |
| EK-1 | evet | `METIN.md`, `senaryo.json` | "YDT" ve kısaltma seste yok; "YDS" marka okunuşu `YeDeSe` (D-0340) |
| EK-2 | evet | 55 kare + sahne HTML | emoji yok |
| EK-3 | evet | kapsam: yön yalnız dikey (kısa); açık: 4 sahne + 5 türev; koyu: kanca, değer, kaydet, çağrı, kapak a/b/c, hikâye a/b | boş hücre yok; ama KARE-BAYAT'a bak |
| EK-5a | evet | `kapak-c.png`, `hikaye-a.png`, `01…-0.png` | üstü çizili/✗ işaretli yalnız `He doesn't goes.`; gerçekten hatalı. Doğru cümle (`He doesn't go.`) ✓ |
| EK-5b | **hayır** | (i) `senaryo.json` cümle 2, kare `02-paperjs-deger-8.4.png`, `aciklama-a.md`: "Olumsuzda ve soruda does girer, s ona geçer." (ii) `senaryo.json` `meta.canAlici[0]` ve `surumler.json` satır 14: "Türkçedeki geniş zaman eki = İngilizcedeki s: gider = goes" | (i) `does` yalnız he/she/it için girer; I/you/we/they için `do`. Kapsam sözü yok, cümle genel okunur. (ii) Yanlış denklik: İngilizce `-s` üçüncü tekil kişi uyumu, Türkçe `-r/-ir` geniş zaman eki; eşit değil (SP-s1 hatası). Paketin metaverisinde duruyor. (iii) bilgi: "Does varsa fiil yalın" ana fiil `does` için ("She does her homework") okunur yanlış; kısa bağlamda kabul edilebilir |
| EK-5c | evet | senaryo, başlık, kapak, açıklama | `always`, "her zaman", "hep" kural cümlesinde yok |
| EK-6 | evet | `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` (A kopyası, `diff` boş) | yazım hatası yok; "Sıradaki ders" `02-03-ydt-temel` konusuyla birebir |
| EK-7 | evet | koyu kareler (9 PNG) okundu | kontrast iyi |
| EK-8 | **kanıt yok** | yalnız kanca sahnesi için 6 karelik `k/ara/kontak-acik.png`; 4 sahnelik 30 karelik kontak yok | o 6 karede klişe işareti 0 |
| ST-1 | **hayır** | `kapak-c.png`, `hikaye-a.png`: kırmızı `✗` + kırmızı üstü çizgi; `kontak-acik.png`: kırmızı `?` | stil anayasası: "en çok 1 vurgu rengi + yeşil; gradyan, parlama, gölge yok". Sarı + amber + kırmızı birlikte. Zeminde hafif vinyet var (tüm karelerde) |
| KARE-BAYAT kare tazeliği | **kanıt yok** | `kapak-b.png` 19:53:23, kaynak `06*/proje/index.html` 19:54:34; `kapak-c.png` 19:52:17, `07*/proje/index.html` 19:53:06; `01*/k/*.png` 19:40:11, `01*/proje/index.html` 19:41:08 | HTML kareden sonra değişti; gördüğüm kare güncel çıktı mı bilmiyorum |
| DK-2 (bilgi) | — | altyazı satırları 37–41 karakter (`8.4`, `16.6` kareleri) | ders dikey kalıbı ≤ 24 ister; kısa için bağlayıcılığı tanımsız, madde sayıma girmedi |

## Kaldı maddeleri ve düzeltme önerisi

| Kimlik | Düzeltme (tek cümle) |
|---|---|
| §1b | Aşağıdaki düzeltmelerden sonra J2'yi yeniden koş; jüri zamanı paketin son içerik zamanından yeni olsun. |
| HV-19 | `02-04-ydt-temel-s2` ve `02-04-ydt-temel-s2b` açıklamalarında `utm_campaign` değerini `ING-YDT-GR-02-04-T` yap. |
| HV-22 | `cakisma-kapisi.mjs`'yi 8 sahne ve statik türevlerde koş, çıktısını `uretim-tutanagi/` altına yaz. |
| KS-4 | Kapak C ana yazısını tam kural olmayan bir merak sözüne çevir (örn. "S NEREYE GİTTİ?"). |
| KS-5 | Ana paketin `ortak/kapak/KAYNAK.json` dosyasını s3 `ortak/kapak/` altına kopyala. |
| KS-6 | `kapak-a|b|c-168.png` üret ve Read ile bak. |
| KS-10 | `kadro.ogrenci` ile karakteri eşle: kadın karakter üret ya da `kadro` ve sesi erkek karaktere göre güncelle; ana kapağı da etkiler, şef karar versin. |
| EK-RZ | `BRIEF-S3.md` satır 21 ve `Y.kunye_svg` rozetini `YDT · TEMEL` yap, 8 sahneyi ve 5 türevi yeniden çek. |
| EK-5b | Kural cümlesine "He, she, it için:" kapsamını ekle (ses yeniden sentez), `meta.canAlici[0]` ve `surumler.json` satırından "geniş zaman eki = s" denkliğini çıkar. |
| EK-8 | 4 sahne × açık tema 30 karelik kontak sayfası üret, klişe işaretini say. |
| ST-1 | `✗` ve üstü çizgiyi kırmızı yerine mürekkep/soluk tonda çiz ya da stil anayasasına "yanlış işareti kırmızı" istisnası yaz (şef karar). |
| KARE-BAYAT | Kapak B, kapak C ve kanca karelerini HTML'den sonra yeniden çek. |

## Ana derse geri besleme (`projeler/simple-present-temel/`)

| Bulgu | Yer |
|---|---|
| "git-er, go-es" eşlemesi; `gider = goes` kuralı yerine kelime çevirisi olarak kalmalı | `ortak/anlatim/METIN.md` satır 44; `senaryo.json` |
| "Türkçedeki geniş zaman eki = İngilizcedeki s" yanlış denklik | `senaryo.json` `meta.canAlici[0]`, `surumler.json` `canAlici` |
| Karakter erkek, `kadro.ogrenci` kadın (K22) | `ortak/kapak/KAYNAK.json` tarifi, `kadro` |
| Ana kapak rozeti `YDT · TEMEL`, kısa künyesi `YDT · BASIC`: iki seviye adı aynı karede | s3 çağrı karesi; BRIEF şablonu düzelmeli, öteki kısalar da aynı kaynaktan |
| Ana derste aynı yanlış denklik varsa kısalar onu devralıyor | s1, s2 de kontrol edilmeli |

## Yöntem notu

Okunan: `juri-olcutleri.md`, `huni-v2-standart.md`, `kapak-standardi.md`, skill `motion-grafik-ders` (bağlayıcı standartlar, stil anayasası, klişe listesi), `senaryo.json`, `METIN.md`, `sureler.json`, `sentez.wav.rapor.json`, `zaman.json`, `surumler.json`, 3 açıklama dosyası, 8 sahne RAPOR.md, sahne HTML metin taraması, 55 PNG (piksel ölçümü) ve şu karelerin gözle okunması: 6 açık sahne karesi, 5 türev, 9 koyu kare, kontak sayfası.
Okumadığım: ses dosyalarının dinlenmesi (EK-11, Nadir), mp4 (yok), canlı panel.

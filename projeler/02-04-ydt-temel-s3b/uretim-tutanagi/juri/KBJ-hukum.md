# KBJ-hukum — 02-04-ydt-temel-s3b (A/B kol b, değişken `kanca` = `yanlis-cumle`) · çıktı jürisi · 15.11.2026 (istem KBJ-0204S3)

**Jüri modeli:** Claude Sonnet 5.5 (`claude-sonnet-5-5`). **Üretici modeli:** Claude Opus 5.5 (`claude-opus-5-5`; `KBC-RAPOR.md` ilk tablo). Modeller farklı; §1e koşulu sağlandı. Ortak kör nokta riski kalır (ikisi de Claude ailesi).

Kapsam: juri-olcutleri §2a (HV, 27 satır), §2b (kısa jüriye giren DK-1, ST-1, ST-2, EK-1…EK-12), §2d (AB). Jüri hiçbir üretim dosyasını değiştirmedi. Bu dosya tek yazılan dosya.
Bakılan çıktı: `senaryo.json`, `sureler.json`, `sozcukler.json`, `sentez.wav.rapor.json` (Whisper), `METIN.md`, `altyazi.json`, `zaman.json`, `surumler.json`, `aciklama*.md`, `kapak-a.png`, `k/koyu/kapak-a-koyu.png` ve 20 kare (Read ile açıldı): sahne 01 açık 0 · 1,2 · 1,8 · 2,8 · 3,45 · 3,97 + koyu 1,8; sahne 02 açık 3 · 9,5 · 15,96 + koyu 13,5; sahne 08 açık 15,99 · 18,66 · 21,3 + koyu 19,6; sahne 03 açık 24,82 · 28,28 + koyu 27.
Kare notu: sahne 02, 08, 03 klasörleri kol a ile bayt aynı (`diff -rq` boş); bu sahnelerin kareleri kol a üretiminden gelir, yerel zaman kol b ile aynıdır.

## Özet

| Sonuç | Sayı |
|---|---|
| Geçti (evet) | 39 |
| Kaldı (hayır + kanıt yok) | 10 |
| Uygulanmaz | 7 |

Kaldı: HV-13 · HV-24 · DK-1 · ST-2 · EK-5b · EK-6 · EK-7 · EK-8 · EK-11 · AB-8.

## 1. Kısa video (HV)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | `sahneler/01…/k/…-0.png`, `02…-9.5.png`, `03…-28.28.png` | logo + `@ydspublishing`, x 60, y 296–339; üç karede de görünür |
| HV-2 | evet | `senaryo.json` cümle 6 `ogrenci`; `sureler.json` i=6; Whisper 1,00 | çağrı parçası öğrenci sesi |
| HV-3 | evet | `senaryo.json` cümle 6 metin; `sentez.wav.rapor.json` | "Dersin tamamı YDS Publishing YouTube kanalında." birebir; duyulan `YEDESE Publishing` (beklenen) |
| HV-4 | evet | metin taraması: `senaryo.json`, `altyazi.json`, `METIN.md`, `ortak/*.js`, `aciklama*.md`, `surumler.json`, sahne `proje/index.html`, `proje-ka*/index.html` → 0 sonuç | SPEC/RAPOR/`uret.py` içindeki yasak listeleri çıktı yüzeyi değil |
| HV-5 | evet | aynı tarama (`dakika`, `dk`, `full lesson`) → 0 | |
| HV-6 | evet | sahne 08 kare 21,3 (yer imi + "Kaydet" + "Arkadaşına gönder"); `aciklama-a.md`, `aciklama-b.md` satır 1 | kalıp listeden: "Bir arkadaşına gönder; o da karıştırıyor." |
| HV-7 | evet | `03…-28.28.png`: ana ders kapağı x 60–960, y 620–1126 | ölçü ≈ 900×506; standart ≈ 920×518 (−%2, kabul) |
| HV-8 | evet | `senaryo.json` | 6/6: sınavda çıkar, en çok yanılınan yer (öğrenci sorusu), tek cümle ("Tarife → leaves, plan → am going."), Türkçe köprü (tarife/plan), dersi izlemeden anlaşılır, sınav günü bakılır |
| HV-9 | evet | `find … -iname '*.mp4'` → boş | |
| HV-10 | evet | tüm kareler; en alt yazı 1530'da biter, en üst yazı 296'da başlar; `kapi-cikti.txt` 0 | 0–280 ve 1570–1920 boş |
| HV-11 | evet | `zaman.json`: 4 sahne (01, 02, 08, 03); 29,31 sn ≤ 35 | hedef 22–26 aşıldı; D-0279 kabul sınırı 35 |
| HV-12 | evet | ilk söz 0,41 sn; sahne 01 = 4,00 sn | kanca sınırda (≤ 4) |
| HV-13 | **hayır (kanıt yok)** | sahne 08 karelerinde 2 sn aralıklı çift yok: 18,66 ↔ 21,3 aralığı 2,64 sn ve kart farklı (`leaves` hapı → altçizgi) | `RAPOR.md` olay tablosu: hap 19,53'te söner; sabit pencere 17,00–19,53 (2,53 sn) ama bu pencereden iki kare kayıtlı değil. Yer imi SVG + "Kaydet" yazısı kare 21,3'te var (kapanış değişkeni `kaydet`, kanca değişkeni kapanışa dokunmaz) |
| HV-14 | evet | `03…-24.82.png`, `-28.28.png` | giriş sözü Fredoka 700; hap `@ydspublishing` + alt satır `YouTube` (tek satırda "·" yok; satır var) |
| HV-15 | evet | `senaryo.json` cümle 6 | "Bu sadece başlangıç." listeden; yinelenmiyor |
| HV-16 | evet | cümle 5 | kaydet kalıbı listeden; yinelenmiyor |
| HV-17 | evet | `ses-sozluk.json` satır 15 (`YDS → YeDeSe`); `sentez.wav.rapor.json` `ses_metni` "YeDeSe Publishing" | en düşük benzerlik 0,92 (parça 2·1) ≥ 0,9; öteki 0,98–1,00 |
| HV-18 | evet | `aciklama-a.md`, `aciklama-b.md` | ilk satır sabit; Reels bloğunda bağ yok ("profildeki bağlantı") |
| HV-19 | evet | bağ satırları (`utm_campaign=` süzgeci): A 5 bağ `ING-YDT-GR-02-04-T` + `s3b-a`; B 5 bağ aynı kampanya + `s3b-b`; kardeş paketler s1, s1b, s2, s2b, s3 aynı büyük harfli kod | |
| HV-20 | evet | `surumler.json`: `s3b-kapak-a`, `s3b-aciklama-a`, `s3b-aciklama-b`; `kapak-a.png` kanal katmanlı, altyazısız | kol b'de kapak B/C ve hikâye yok (AB §4 uyarınca) |
| HV-20a | evet | `kapak-a.png` 1080×1920; kanal y 296–339; künye 386–434; içerik 505–1378; sağ kenar ≤ 948; orta pikseli (247,243,234) = `#f7f3ea`; koyu (28,27,24) ≈ `#1b1a17`; `k/koyu/kapak-a-koyu.png` var | |
| HV-20b | evet | `kapak-a.png`: başlık "HATA NEREDE?" 2 sözcük; kapak A = kanca karesi | kare ayrıca kanca cümlesini taşır (kanca karesi gereği); B/C yok |
| HV-21 | uygulanmaz | AB §4: hikâye kol a'da | |
| HV-22 | evet | `kapi-cikti.txt` çıkış 0, 4 sahne "çakışma yok"; statik `kapak-a.png` gözle: taşma yok | |
| HV-23 | evet | `sentez.wav.rapor.json` cümle 6 parçaları 1,00 / 1,00 | |
| HV-24 | **hayır** | künye ve kapak rozeti `YDT · BASIC`: kare 0, 1,2, 28,28; `senaryo.json` `giris.rozetler`; `ortak/kunye.js` `KUNYE.rozet`; `yardim.py` `ROZET` | kare 28,28 aynı karede iki rozet metni: künye `YDT · BASIC`, kapak kartı `YDT · TEMEL` |
| HV-25 | evet | tüm kareler | altyazı en çok 2 satır; kanca 1 satır |

## 2. Ders ve ortak maddeler (kısa jüriye giren)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| DK-1 | **hayır** | sahne 02 (değer): `uret.py` `altyazi_v2_svg` tek `fill`, sözcük dolgusu yok; kare 9,5 sözcük vurgusu yok; `02…/RAPOR.md` satır 97 "düz altyazı" | zorunlu sahne (değer) karaokesiz. Sahne 08 altçizgi karaoke var (kare 21,3), sahne 03 dolgu karaoke var (kare 24,82). Kanca sahnesinde zorunlu değil. Ana derste aynı sahne |
| DK-2 | uygulanmaz | kısada HV-25 | |
| DK-3 | uygulanmaz | kısa jüriye girmez | |
| K23 | uygulanmaz | kısa jüriye girmez | |
| ST-1 | evet | kareler | bir karede tek sarı aile (`#ffe066` dolgu + `#d9900f` çizgi tema çifti); kırmızı, yeşil yok; üstü çizgi mürekkep renginde (kare 2,8); gradyan yok; vinyet köşe (222,218,210) ↔ orta (247,243,234) = 25/255, sınırda ≤ 25 |
| ST-2 | **hayır (kanıt yok)** | tutanakta `hyperframes check` çıktısı yok | yazı ailesi Fredoka/Lexend/Caveat evet. Ölçülen taban: altyazı 44, künye 34, rozet 26, kanal 40–44 (< 50). Huni §2 kanal 40–44 yazar; ST-2 "dikey 50" der: kural çakışması, şef karar verir |
| EK-1 | evet | `sentez.wav.rapor.json` | ses metninde YDT/BASIC yok; `YDS → YeDeSe` marka sözlüğünden |
| EK-2 | evet | 20 kare | emoji yok (ikonlar SVG) |
| EK-3 | evet | matris: dikey × açık+koyu × {01, 02, 08, 03} + kapak A açık/koyu | boş hücre yok. Yatay kısa için yok (uygulanmaz); kol b'de hikâye ve B/C yok (uygulanmaz) |
| EK-4 | evet | `KBC-RAPOR.md` §6-13 "Jüri koşmadı", Kovan kaydı yazılmadı | Nadir'e adres gittiğine dair kayıt yok; şef doğrular |
| EK-5a | evet | kare 2,8 | üstü çizili `is leave` gerçekten hatalı (`leaves` olmalı) |
| EK-5b | **hayır** | `senaryo.json` cümle 4; kare 15,96; `aciklama-a.md` başlık "Tarife geniş zaman, plan şimdiki zaman" | iki örnek cümle doğru ve ses/ekran doğru. Denklik kapsam sınırsız: planlanmış gelecek `be going to` ve `will` ile de kurulur; tarifeli gelecek yalnız kesinleşmiş tarife için geniş zaman alır; "çoğunlukla" / "kesinleşmiş" yazılı değil. Ana derste aynı denklik |
| EK-5c | evet | `senaryo.json`, `aciklama*.md`, kapak | "her zaman", "hep", "always" yok. (Kapak kartı "HER ZAMAN mi ŞİMDİ mi?" soru, kural değil) |
| EK-6 | **hayır** | `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` üst bilgi | şablon kaynaklı sabit cümle hatası: "Shorts: …-S3, 28,31 sn" (kol b 29,31 sn); başlık `02-04-ydt-temel-s3` (paket s3b); "Sürüm: A (`s3-aciklama-a`)" (kimlik `s3b-aciklama-a`); `aciklama-a.md` "Hikâye: `hikaye-a.png`" ve `aciklama-b.md` "Kapak: `kapak-b.png`", "`hikaye-b.png`" kol b'de olmayan dosyalar. Yayın metni (başlık, açıklama gövdesi, etiket) yazım hatasız |
| EK-7 | **hayır** | `08…/k/koyu/…-19.6.png` | `leaves` hapı sönerken yazı `#1b1a17`, hap (101,75,36): kontrast ≈ 2,1:1, okunmuyor (geçiş karesi). Öteki koyu kareler (1,8 · 13,5 · 27) okunur. Sahne kol a ile bayt aynı |
| EK-8 | **hayır** | kareler 1,2 · 1,8 · 2,8 | işaret sayısı 1: klişe 16 (metin duvarı): kapak karesinde 4 yazı satırı + altyazı = 5 satır (sınır ≤ 3). Üretici açık nokta 6 aynı sorunu yazdı. Kontak sayfası pakette yok; 18 maddeyi 20 karede elle taradım, öteki 17 temiz |
| EK-9 | evet | `senaryo.json` cümle 3 | öğrenci sorusu 1 adet, 10 sözcük; "Hata nerede?" öğretmen kancası, öğrenci soru anı değil |
| EK-10 | evet | `sentez.wav.rapor.json` cümle 4 `ses_metni` | `-ing → /ɪŋ/` IPA uygulanmış; şık harfi ve tire sorunu yok |
| EK-11 | **hayır (kanıt yok)** | `KBC-RAPOR.md` açık nokta 3 "Kulak denetimi yok" | yeni parça "Hata nerede?" (2 sözcük) Whisper 1,00; dinleme kaydı yok; Nadir dinler |
| EK-12 | evet | kareler 2,8 · 3,45 · 3,97; `sozcukler.json` | `leaves` 3,20, `at` 3,56, `7` 3,80 ses ile aynı anda yazılıyor. Kanca sahnesi (0–4 sn) başlık istisnası kullanıldı |

## 3. A/B kolu (AB)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| AB-1 | evet | kol a `surumler.json` `varyant` (`s3`/`a`/`kanca`/`kopru`); kol b (`s3`/`b`/`kanca`/`yanlis-cumle`) | grupta 2 kol; s3 → kanca |
| AB-2 | evet | `diff -rq`: 89 satır (jüri koşusu; üretici 90 bildirdi, `__pycache__` satırı farkı) | sınıfları denetledim: sahne 01; `senaryo.json` (cümle 1 + `giris` + `meta.kapak`); ses ve zaman türevleri; `surumler.json`; açıklamada yalnız `utm_content` (3 dosya, `diff` doğrulandı); `kapak-a.png`/`kapak.png`; çıkarılan grup türevleri; tutanak. Beklenmeyen fark yok. Süre +1,00 sn ve ilk söz 0,41 sn kanca parçasının sonucudur (açık nokta 1 ve 4) |
| AB-3 | evet | sahne 02, 08, 03, 04–07 klasörleri `diff -rq` boş; `ortak/kunye.js` iki kolda aynı; kadro/sesler `senaryo.json`'da aynı | çekirdek cümle (cümle 6) sha256 aynı |
| AB-4 | uygulanmaz | yayın sonrası | |
| AB-5 | uygulanmaz | yayın sonrası | |
| AB-6 | evet | `surumler.json` `s3b.varyant`; `aciklama-a.md` `utm_content=s3b-a`, `aciklama-b.md` `s3b-b` | `deger` `[a-z0-9-]` |
| AB-7 | uygulanmaz | yayın sonrası | |
| AB-8 | **hayır** | `ortak/kunye.js:8` `export const KOK = "/projeler/02-04-ydt-temel-s3/ortak";` (kol a yolu); `sahneler/04…`, `05…`, `06…`, `07…/proje/.hyperframes/video-state.json` kol a mutlak yolu | `kunye.js` iki kolda bayt aynı; kol a taşınır ya da silinirse kol b font ve logo yükleyemez. `KBC-RAPOR.md` "bağlar 0" doğru ama `KOK` taramasını yapmamış |
| AB-9 | evet | sha256: kol a `cumle-1…5` = kol b `cumle-2…6` (`af9343e6d690`, `a65bb1e43a13`, `d71bacefe538`, `9b7e70ce36dc`, `6a9927c66d00`) | yeniden sentez yok; yalnız `cumle-1.wav` (`142d55e5bbd0`) yeni |

## 4. İki kolun yan yana kıyası

| Öğe | Kol a | Kol b | Fark |
|---|---|---|---|
| Ekran metni, sahne 02/08/03 | aynı | aynı | yok (bayt aynı) |
| Ses cümle 2–6 (kol b) | aynı sha256 | aynı | yok |
| Kanca sesi | değer cümlesi (ilk söz 1,00 sn) | "Hata nerede?" (0,41 sn) | beklenen (değişken) |
| Kapak A | `TARİFE ≠ PLAN` | `HATA NEREDE?` + yanlış cümle | beklenen (kanca karesi) |
| Açıklama gövdesi, başlık, kapak B/C, hikâye | aynı | kapak B/C ve hikâye yok | beklenen; ama açıklama dosyaları olmayan kapak/hikâye adlarını gösteriyor (EK-6) |
| Süre | 28,31 sn | 29,31 sn | +1,00 sn (kanca sonucu) |

Değişken dışı söz, ekran metni, kapak, açıklama farkı yok. Kanal katmanı, çekirdek cümle, kadro aynı.

## 5. Kaldı maddeleri için düzeltme önerisi (tek cümle)

| Kimlik | Öneri |
|---|---|
| HV-13 | Sahne 08'de 17,5 ve 19,5 sn (yerel 1,5 ve 3,5) karelerini kaydet; kart bölgesi farkı 0 px ölçülsün. |
| HV-24 | Rozeti iki kolda birlikte `YDT · TEMEL` yap (`senaryo.json`, `kunye.js`, `yardim.py`, 4 sahne yeniden üret). |
| DK-1 | Sahne 02 altyazısına sahne 03'teki sözcük dolgusu karaokesini ekle (ana derste de geçerli). |
| ST-2 | `hyperframes check` çıktısını tutanağa yaz; "dikey 50" ile huni §2 çelişkisini şef çöz. |
| EK-5b | Kart ve başlıkta kapsam sınırı yaz ("çoğunlukla", "kesinleşmiş tarife") ya da başlığı "Tarifede geniş zaman, plan anlatırken şimdiki zaman" gibi sınırlı kur; ana derste de. |
| EK-6 | Üç `aciklama*.md` üst bilgisini kol b'ye göre düzelt (kimlik `s3b`, 29,31 sn, olmayan kapak/hikâye adlarını çıkar). |
| EK-7 | Sahne 08 `leaves` hap sönüşünde yazı rengini koyu temada açığa çevir ya da sönüşü kısalt (ana derste de). |
| EK-8 | Kanca karesinde altyazıyı gizle ya da kanca yanlış cümlesini tek satıra indir (≤ 3 satır). |
| EK-11 | Nadir "Hata nerede?" parçasını dinlesin; kaydı tutanağa yazılsın. |
| AB-8 | `ortak/kunye.js` `KOK` değerini `/projeler/02-04-ydt-temel-s3b/ortak` yap; `video-state.json` yollarını yeniden üretimle ya da kol b yoluna çevir. |

## 6. Ana derse geri besleme

- DK-1 (sahne 02 karaoke yok), EK-5b (denklik kapsamsız), EK-7 (08 koyu geçiş karesi), HV-24 (`BASIC` altı kısa pakette) ana kolda da geçerli; kol b yalnız devralıyor.
- HV-13 kanıtı ana kolda da eksik: iki kareli 2 sn ölçüsü hiçbir pakette kayıtlı değil (kol a `k/` aynı üç kare).
- ST-2 çelişkisi (dikey 50 ↔ huni 40–44) tüm kısa paketleri etkiler; jüri-olcutleri ST-2 satırı kısa için ayrı eşik ister.
- Süre: sesli kanca değişkeni toplam süreyi +1,00 sn artırır; sonuç okumasında izlenme yüzdesi kol a lehine eğilir (açık nokta 1; sözleşme §6).

Jüri zamanı: 15.11.2026. Paket içerik değişikliği yoksa bu hüküm güncel sayılır (§1b); düzeltme yapılırsa jüri yeniden koşar, bu dosya `J2-hukum-<GGAA-SSDD>.md` adıyla tarihli kalır.

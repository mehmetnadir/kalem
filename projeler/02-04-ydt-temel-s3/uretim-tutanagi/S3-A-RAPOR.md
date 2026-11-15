# İstem S3-A raporu — 02-04-ydt-temel-s3 huni seti taslağı · 15.11.2026

| Dosya | İçerik | Durum |
|---|---|---|
| `senaryo-taslak.md` | Shorts 3 sahne (kapak · örnek · tam ders çağrısı), 4 cümle (1 soru anı), ses/ekran/görsel tablosu, önbellek, süre | TASLAK |
| `kapak-taslak.md` | 3 kapak sürümü (A kod · B soru · C karşıt çift), ortak öğeler, yerleşim, platform kullanımı, `giris` alanları (A) | TASLAK |
| `hikaye-taslak.md` | 2 hikâye karesi (A bilgi kartı · B "hangisi doğru?"), dil, UTM | TASLAK |
| `aciklama-taslak.md` | 2 açıklama seti (A doğrudan · B soruyla) × YouTube / Instagram / TikTok, UTM tablosu, metin kaynağı, yer tutucular | TASLAK |
| `S3-A-RAPOR.md` | bu rapor | — |

Yapılmayan (istem kuralı): ses sentezi, ElevenLabs çağrısı, render, sahne kodu, git commit, alt ajan. Silinen dosya yok.
Yazma yalnız `projeler/02-04-ydt-temel-s3/uretim-tutanagi/` altında (dizini bu istem açtı).

## 1. Süre tahmini (hedef 24–28 sn, tavan 28)

| Cümle | Konuşan | sn | Başlar–biter | Ölçü |
|---|---|---|---|---|
| ilk söz | — | 1,00 | 0,00–1,00 | K23, S1 ile aynı |
| 1 tren + sinema (2 EN parça) | öğretmen | 6,01 | 1,00–7,01 | ölçülmüş parça: ana ders cümle 5 → 3,36 + 0,25 + 2,40 |
| ara | | 0,55 | | |
| 2 soru anı | öğrenci | 3,76 | 7,56–11,32 | ölçülmüş: ana ders cümle 6 (önbellek) |
| ara (öğrenciden sonra) | | 0,75 | | |
| 3 cevap (yeni TR) | öğretmen | 4,81 | 12,07–16,88 | hız: ana ders cümle 7, 28 sözcük / 14,96 sn = 0,534 sn/sözcük × 9 |
| ara | | 0,55 | | |
| 4 kapanış | öğretmen | 9,02 | 17,43–26,45 | ölçülmüş: S1 cümle 3 (önbellek) |
| kuyruk | | 1,00 | 26,45–27,45 | kalıp §1 kural 5 |
| **Toplam** | | **27,45** | | ölçülmüş 16,63 + tahmin 10,82 |

En kötü durum: S1'de yeni cümle tahmini %11 kısa kaldı (cümle 2: 11,8 → 13,08). Aynı sapma cümle 3'e gelirse +0,53 sn → 27,98 sn.
Cümle 1 ölçülmüş parçadan; aralığı 5,61–6,01 (üst değer alındı). Yedek: "bir" çıkar (≈ −0,3) · kuyruk 0,5 (−0,5).
Sahneler (tahmin): 01 0,00–3,00 · 02 3,00–16,88 · 03 16,88–27,45.

Önbellek kazancı (hesaplamadan önce 3 soru, soru 1): cümle 2 ana dersten, cümle 4 S1'den birebir → 2 cümle ücretsiz, Whisper kapısı
önbellekte. `el.py` anahtarı bağlamı içerir (satır 88, 142): cümle 1'in EN parçaları metin olarak aynı ama yeni sentez gerekir.
Yeni sentez ≈ 140 karakter (46 + 40 + 54) ≈ 0,69 TL (S1 oranı: 257 karakter ≈ 1,26 TL).

## 2. Sürümler arası fark

| Sürüm | A | B | C |
|---|---|---|---|
| Kapak | can alıcı kod: `TARİFE` / `≠ PLAN`; tren + bilet tutan figür, etiket `leaves` / `am going`; video ilk karesi | soru: `NEDEN -ING` / `YOK?`; tren + sarı `?`, kart `The train leaves …` | karşıt çift: `İKİSİ DE` / `GELECEK`; iki kart üst üste, tek vurgu `leaves` |
| Hikâye karesi | bilgi kartı: `TARİFE ≠ PLAN` + iki kart + `Tren tarifeye uyar` | soru kartı: `Hangisi doğru?` A train leaves (doğru) · B I go … tonight (yanlış) + ipucu `Tarife mi, plan mı?` | — |
| Açıklama | kuralla açılır; YouTube başlığı `Tarife geniş zaman, plan şimdiki zaman`; `utm_content=s3-a` | öğrenci sorusuyla açılır; YouTube başlığı `Tren de plana göre kalkmıyor mu? Neden -ing yok?`; `utm_content=s3-b` | — |

Ortak: S1 kimliği (rozet `YDT · BASIC`, hap `#ffe066` / `#1b2440`, logo sol alt, `@ydspublishing`, "kanal" yok, QR yok), S1 kapanış cümlesi
birebir, süre "dört buçuk dakika" / "4 dakika 26 saniye".

## 3. Kararlar ve gerekçe

1. **Kapanış S1 ile birebir.** Gerekçe: istem "S1 ile aynı kalıp"; jüriden geçmiş metin; ses önbellekten; S1 sahne 03 çapaları aynen geçerli.
2. **Soru anı ana ders cümle 6 ile birebir.** Gerekçe: istemin sorusu; ses önbellekten; ana derse geçen izleyici aynı sesi duyar.
3. **Cümle 1'de TR çerçeve yok.** Gerekçe: süre (§1). "İki cümle de geleceği anlatıyor" eklenirse ≈ 29,6 sn. "İkisi de gelecek" bilgisini
   zaman çizgisi (now'ın sağında `7 pm` ve `tonight`) taşır.
4. **Cevap tek cümle, 9 sözcük:** "Planı bir kişi yapar. Tren tarifeye uyar: geniş zaman." Öğrencinin iki sorusunu karşılar (plan kimin?
   neden -ing yok?). İki öbek ana ders cümle 7'den; birleşim yeni.
5. **Sahne 02 HyperFrames önerisi.** Gerekçe: balon, figür ve `bag` ana ders sahne 06'da (HyperFrames) hazır; zaman çizgisi sahne 09
   görünümünden SVG olarak çizilir.
6. **Hikâye B şık çifti `leaves` / `is leaving` değil.** Gerekçe: tarifeli olayda şimdiki zaman da kabul görebilir; tek doğru cevap kuralı
   tartışmalı olur. Seçilen çift: doğru tren cümlesi ↔ geniş zamanla kurulmuş plan cümlesi.

## 4. Açık noktalar

| # | Nokta | Önerim |
|---|---|---|
| 1 | `utm_campaign` istemle büyük harf (`ING-YDT-GR-02-04-T`); S1 küçük harf. Aynı ders iki kampanyaya bölünebilir | tek biçim seç; S1'i büyük harfe çekmek huni-plan §6 ile uyumlu. Nadir'e soru |
| 2 | "Rakam yazma": ses metninde uygulandı. Ekran kartı, hikâye ve açıklama `7 pm` yazar (ana ders kartıyla aynı) | ana dersle aynı kalsın. Ekrana da uygulanacaksa `seven pm` (kart, hikâye, açıklama) |
| 3 | Sahne 02 tek motorda balon + zaman çizgisi ister; ana derste ikisi ayrı motordaydı (06 HyperFrames, 09 canvas) | sahne kodu istemi karar verir; 3 sahne sınırı korunur |
| 4 | Yeni metinler jüri bekler: cümle 3; kapak `TARİFE ≠ PLAN`, `İKİSİ DE GELECEK`; hikâye `İkisi de gelecek`, şık B; açıklamadaki 4 yeni ifade (`aciklama-taslak.md` §5) | sentezden önce dil + kaynak jürisi |
| 5 | Süre tahmini cümle 3'ün hızına bağlı; ölçülen toplam 28'i aşabilir (en kötü 27,98) | sentez sonrası `zaman.json`; aşarsa `senaryo-taslak.md` §4 yedekleri |
| 6 | Kapak C'de figür yok (kalıp §4 "figür + nesne" sapması) | jüri reddederse sağ alta küçük öğretmen figürü |
| 7 | Yalnız kapak A videonun içinde. TikTok kapağı videodan kare seçiyorsa B ve C orada kullanılamaz (huni-plan §5, doğrulanmadı) | A'yı TikTok'ta, B ve C'yi YouTube Studio'da dene |
| 8 | Profil bağlantısı tek: iki açıklama seti aynı anda yayındaysa `bio` tıklaması seti ayırmaz | setleri sırayla yayınla; bio bağlantısı yayındaki setin `utm_content` değerini taşır |
| 9 | D-0278 yerel Kovan defterinde yok (srv21 kopyasında son karar D-0096) | istemdeki karar uygulandı; defter eşitlenince doğrula |
| 10 | Önbellek koşulu: eleven_v4, HIZ_EN 0,9, tohum 0. Biri değişirse cümle 2 ve 4 yeniden sentezlenir (≈ 3,76 + 9,02 sn ses) | ses isteminde ayar ana ders ve S1 ile aynı tutulur |
| 11 | `ortak/kunye.js` S3'te yok (yazma kapsamı dışı). S1 kopyası dikey pakete bağlı (S1-C açık nokta 4) | paket isteminde S1 `ortak/kunye.js` kopyalanır, yalnız `KOK` ve `cipler` değişir |
| 12 | `surumler.json` ve `huni-surumler.json` kaydı yok (yazma kapsamı dışı) | şef açar; kimlik önerisi `shorts-3`, `kapak-a/b/c`, `hikaye-a/b`, `aciklama-a/b` |
| 13 | S1'den devreden: `platform_url` canlılığı ölçülmedi; TikTok `@ydspublishing` doğrulanmadı | paylaşımdan önce adres açılır; hesap doğrulanır |

## 5. S3-C eki (15.11, jüri düzeltmeleri; ayrıntı `S3-duzeltme.md`)

- Kapak C başlığı `İKİ ÖRNEK` / `İKİ ZAMAN` oldu, sağ altta küçük öğretmen figürü (açık nokta 6 kapandı). Kapak B ve C can alıcısı
  `canAlici[1]` / `[1]`+`[2]` (kaynak jürisi madde 2).
- Hikâye A üst satır `İkisi geleceği anlatıyor`, kartlar kısa (`The train leaves …` / `I am going …`). Hikâye B = eski yedek B
  (`Tarife mi, plan mı?` + tren cümlesi + şıklar `TARİFE` / `PLAN`); şık B `I go …` çıktı.
- Açık nokta 4 listesine eksik yeni metin: hikâye A alt satır `Tren tarifeye uyar` (ana ders cümle 7 kısaltması; kaynak jürisi madde 4,
  metin doğru).
- Sahne 02 zaman çizgisine etiket: `gelecek · V-s`, `gelecek · am + V-ing` (kaynak jürisi madde 3; ses değişmedi).
- Ölçülen anlatım 26,56 sn (tahmin 27,45); cümle 1 5,45 sn (tahmin 6,01), cümle 3 4,48 sn (tahmin 4,81). Ayrıntı `S3-C-RAPOR.md`.

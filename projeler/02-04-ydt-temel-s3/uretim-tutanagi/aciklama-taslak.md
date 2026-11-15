# 02-04-ydt-temel-s3 · açıklama ve UTM taslağı (2 set × YouTube · Instagram · TikTok)

Durum: TASLAK (istem S3-A, 15.11.2026). Yükleme YOK.
Şablon: huni-plan §4 (açıklama), §5 (platform kısıtı), §6 (UTM), §7 (dil). Emsal: S1 `aciklama-taslak.md` ve `../../02-04-ydt-temel-s1/aciklama.md`.
Set A = kısa, doğrudan (kuralla açılır). Set B = soru ile açılır (öğrencinin sorusu, ana ders cümle 6).
Dil D-0278: Instagram ve TikTok öğretmene ve YDT öğrencisine seslenir; veli dili yok. YouTube: öğrenci + öğretmen ortak (huni-plan §7).

## 1. Alanlar

| Alan | Değer | Kaynak |
|---|---|---|
| `konu_adi` | Simple Present ve Present Continuous | ana ders `senaryo.json` → `baslik` |
| `ders_kodu` | `ING-YDT-GR-02-04-T` | ana ders `surumler.json` → `video.kod` |
| Shorts kodu | `ING-YDT-GR-02-04-T-S3` | dikey kalıp §7 |
| `gercek_sure` | 4 dakika 26 saniye (265,7 sn) | ana ders `cikti.mp4` (istem S3-A); S1 ile aynı |
| `sonraki_ders_adi` | Stative Verbs (02-05) | ana ders BRIEF §1, senaryo cümle 18 |
| `platform_url` | `https://ydspublishing.com/grammar/02-04-ydt-temel` | S1 `aciklama-taslak.md` §1 (aynı kaynak) |
| `uzun_video_url` | `{UZUN_VIDEO_URL}` | YER TUTUCU: ana ders YouTube'a yüklenmedi |
| Kimlik | `@ydspublishing` | karar A 05.11; TikTok doğrulanmadı |
| `kanca_id` (`utm_content`) | `s3-a` (set A) · `s3-b` (set B) | istem S3-A |

**UYARI:** `platform_url` belgeden türedi; canlılığı ölçülmedi (grammar-kapi Worker 11.11'de yayında değil; S1 §1). Yayından önce adresi aç.
Açılmazsa satır çıkarılır ya da `{PLATFORM_URL}` yer tutucusu konur.

## 2. UTM bağlantıları (huni-plan §6 şeması)

`utm_campaign` = ders kodu, olduğu gibi: `ING-YDT-GR-02-04-T` (istem S3-A).

**DİKKAT:** S1 küçük harf kullandı (`ing-ydt-gr-02-04-t`, S1-C düzeltme 5). Analitik büyük/küçük harfi ayırırsa aynı ders iki kampanyaya
bölünür. Karar şefte / Nadir'de (rapor açık nokta 1). Biçim değişirse yalnız bu dosyadaki `utm_campaign` değerleri değişir.

| Kullanım | Set A | Set B |
|---|---|---|
| YouTube açıklaması → uzun ders | `{UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-a` | `{UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-b` |
| YouTube açıklaması → ders sayfası | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-a` | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-b` |
| Instagram profil bağlantısı | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=bio&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-a` | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=bio&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-b` |
| TikTok profil bağlantısı | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=tiktok&utm_medium=bio&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-a` | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=tiktok&utm_medium=bio&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-b` |

- Hikâye çıkartması bağlantıları: `hikaye-taslak.md` §5 (`utm_medium=story`).
- `{UZUN_VIDEO_URL}` `watch?v=…` biçiminde gelirse ilk `?` yerine `&` yazılır.
- YouTube adresindeki UTM grammar-kapi kayıtlarına düşmez; YouTube tarafı Studio "Trafik Kaynakları" ile ölçülür (huni-plan §6).
- Instagram ve TikTok açıklamasına adres yazılmaz (tıklanmaz, huni-plan §5). Çağrı "profildeki bağlantı" olur.
- Profil bağlantısı tektir. İki set aynı anda yayındaysa profil tıklaması seti ayırmaz (rapor açık nokta 8).

## 3. Set A — kısa, doğrudan

### YouTube Shorts

Başlık:

```
Tarife geniş zaman, plan şimdiki zaman | YDT İngilizce #Shorts
```

Açıklama:

```
Simple Present ve Present Continuous konusunun püf noktası: iki cümle de geleceği anlatır, zamanları farklıdır.
The train to İzmir leaves at 7 pm today. → tarifeli gelecek, geniş zaman
I am going to the movie theater tonight. → planlanmış gelecek, şimdiki zaman
Planı bir kişi yapar. Tren plan yapmaz, tarifeye uyar.
Bu, iki zaman arasındaki üç farktan biri. Tam ders süresi: 4 dakika 26 saniye.
Dersin tamamını izle: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-a
Sıradaki ders: Stative Verbs
Ders sayfası: https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-a

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

Elle adım: Studio'da "İlgili video" = uzun ders (API alanı yok; huni-plan karar sorusu 2). Kapak: `kapak-taslak.md` (A, B ya da C).

### Instagram Reels

```
İki cümle de geleceği anlatıyor, zamanları farklı:
The train to İzmir leaves at 7 pm today. → tarifeli gelecek, Simple Present
I am going to the movie theater tonight. → planlanmış gelecek, Present Continuous
Bu, üç farktan biri. Üç farkın hepsi tam derste: 4 dakika 26 saniye.
Tam ders: profildeki bağlantı.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Stative Verbs

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

### TikTok

```
Tarifeli gelecek: The train leaves. Planlanmış gelecek: I am going.
Bu, üç farktan biri. Üç farkın hepsi tam derste (4 dakika 26 saniye). Tam ders: profildeki bağlantı.
Sıradaki ders: Stative Verbs
#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

## 4. Set B — soru ile açılır

### YouTube Shorts

Başlık:

```
Tren de plana göre kalkmıyor mu? Neden -ing yok? | YDT İngilizce #Shorts
```

Açıklama:

```
"Tren de plana göre kalkmıyor mu? Neden -ing yok?"
Simple Present ve Present Continuous (ING-YDT-GR-02-04-T) dersinde bir öğrencinin sorusu. Cevap: planı bir kişi yapar; tren plan yapmaz, tarifeye uyar.
I am going to the movie theater tonight. → planlanmış gelecek, şimdiki zaman
The train to İzmir leaves at 7 pm today. → tarifeli gelecek, geniş zaman
Bu, iki zaman arasındaki üç farktan biri. Tam ders süresi: 4 dakika 26 saniye.
Dersin tamamını izle: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-b
Sıradaki ders: Stative Verbs
Ders sayfası: https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s3-b

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

### Instagram Reels

```
"Tren de plana göre kalkmıyor mu? Neden -ing yok?"
Planı bir kişi yapar: I am going to the movie theater tonight.
Tren plan yapmaz, tarifeye uyar: The train to İzmir leaves at 7 pm today.
Bu, üç farktan biri. Üç farkın hepsi tam derste: 4 dakika 26 saniye.
Tam ders: profildeki bağlantı.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Stative Verbs

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

### TikTok

```
Tren de plana göre kalkmıyor mu? Neden -ing yok?
Planı bir kişi yapar: I am going. Tren tarifeye uyar: The train leaves.
Bu, üç farktan biri. Üç farkın hepsi tam derste (4 dakika 26 saniye). Tam ders: profildeki bağlantı.
Sıradaki ders: Stative Verbs
#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

TikTok `@ydspublishing` kullanıcı adı ve profil bağlantısı koşulu doğrulanmadı (dikey kalıp açık soru 4).

## 5. Metin kaynağı

| Metin | Kaynak |
|---|---|
| İki örnek cümle, "Planı bir kişi yapar", "Tren plan yapmaz, tarifeye uyar", "tarifeli / planlanmış gelecek" | ana ders cümle 5, 7 (D-0204 geçti) |
| Öğrenci sorusu | ana ders cümle 6, birebir |
| "Bu, (iki zaman arasındaki) üç farktan biri", "Üç farkın hepsi tam derste", "Öğretmenseniz sınıfınızla paylaşın" | S1 açıklaması (S1-B jürisi geçti) |
| "iki cümle de geleceği anlatır, zamanları farklıdır", "bir öğrencinin sorusu", set A YouTube başlığı | yeni: ana derste yok; S3-B dil jürisi geçti |
| "İki cümle de geleceği anlatıyor, zamanları farklı" | ana ders cümle 5 "İki cümle de geleceği anlatıyor" + yeni ek "zamanları farklı"; S3-C düzeltmesi (dil jürisi madde 1: eski "İki cümle de gelecek" fiil gibi okunuyordu) |
| "konusunun püf noktası" | S3-C düzeltmesi (dil jürisi madde 3: eski "konusu püf noktası" izafet eksik; ders kodu parantezi çıktı, kod UTM'de) |

## 6. Şablondan sapma

| Şablon (huni-plan §4, §6) | Bu taslak | Gerekçe |
|---|---|---|
| "Dersin tamamını kanalda izleyin" | "Dersin tamamını izle" | "kanal" sözü yok (karar A 05.11); S1 ile aynı |
| "Tüm alıştırmalar ve testler: {platform_url}" | "Ders sayfası: …" | ders sayfasında alıştırma ve test olduğu doğrulanmadı; S1 ile aynı |
| `ders_kodu` = `meta.kod` (Shorts) | ana ders kodu | açıklama ana dersi tanıtır; Shorts `utm_content` ile ayrılır; S1 ile aynı |
| `utm_campaign={ders_kodu}` | `ING-YDT-GR-02-04-T` (şablonla aynı) | istem S3-A "olduğu gibi". S1'den sapma: S1 küçük harf (rapor açık nokta 1) |

## 7. Yer tutucular

| Yer tutucu | Nerede | Doldurma koşulu |
|---|---|---|
| `{UZUN_VIDEO_URL}` | §2, §3 ve §4 YouTube açıklaması | ana ders YouTube'a yüklenince |
| (koşullu) `{PLATFORM_URL}` | §2, §3, §4 "Ders sayfası"; profil bağlantıları | grammar-kapi yayında değilse `https://ydspublishing.com/grammar/02-04-ydt-temel` yerine |
| süre `4 dakika 26 saniye` (koşullu) | §3, §4 | ana ders yeniden render olursa ffprobe değeriyle |

# 02-04-ydt-temel-s1 · açıklama ve UTM taslağı (YouTube · Instagram · TikTok)

Durum: TASLAK (istem S1-A, 15.11.2026). Yükleme YOK.
Şablon: huni-plan §4 (açıklama), §5 (platform kısıtı), §6 (UTM), §7 (dil).

## 1. Alanlar

| Alan | Değer | Kaynak |
|---|---|---|
| `konu_adi` | Simple Present ve Present Continuous | ana ders `senaryo.json` → `baslik` |
| `ders_kodu` | `ING-YDT-GR-02-04-T` | ana ders `surumler.json` → `video.kod` |
| Shorts kodu | `ING-YDT-GR-02-04-T-S1` | dikey kalıp §7 |
| `gercek_sure` | 4 dakika 26 saniye (265,7 sn) | ana ders `cikti.mp4` ffprobe (istem S1-A); commit cfa2511: 7970 kare / 30 fps |
| `sonraki_ders_adi` | Stative Verbs (02-05) | ana ders BRIEF §1, senaryo satır 18 |
| `platform_url` | `https://ydspublishing.com/grammar/02-04-ydt-temel` | dijital-anlatim `sozlesme.md` madde 5 + K35; `worker/grammar-kapi/wrangler.toml` rota `ydspublishing.com/grammar/*` |
| `uzun_video_url` | `{UZUN_VIDEO_URL}` | YER TUTUCU: ana ders YouTube'a yüklenmedi |
| Kimlik | `@ydspublishing` | karar A 05.11 (dikey kalıp açık soru 4: YouTube, X, Instagram doğrulandı; TikTok doğrulanmadı) |
| `kanca_id` (`utm_content`) | `s1` | Shorts sürüm kimliği |

**UYARI:** `platform_url` belgeden türedi; canlılığı ölçülmedi. Belgeye göre grammar-kapi Worker 10.11'de yerelde, 11.11'de
"Worker yayında değil, R2'ye yazılmadı" (`dijital-anlatim/.claude/docs/taslak/acik13-aciklama-pp-8-11-1111.json` g-8).
Yayından önce adres açılmazsa satır çıkarılır ya da `{PLATFORM_URL}` yer tutucusu konur.

## 2. UTM bağlantıları (§6 şeması)

`utm_campaign` = ana ders kodu küçük harf (`ing-ydt-gr-02-04-t`). Gerekçe: analitik büyük/küçük harfi ayırır; aynı kampanya iki
biçimle bölünmesin. K35 (yds.tc kısa kod anahtarı) yalnız biçim emsalidir, UTM kuralı değildir. Sapma §6 tablosunda (S1-C düzeltme 5).
Shorts `utm_content=s1` ile ayrılır.

| Kullanım | Bağlantı |
|---|---|
| YouTube açıklaması → uzun ders | `{UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1` |
| YouTube açıklaması → ders sayfası | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1` |
| Instagram profil bağlantısı | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=bio&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1` |
| Instagram hikâye çıkartması (elle) | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=story&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1` |
| TikTok profil bağlantısı | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=tiktok&utm_medium=bio&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1` |

- `{UZUN_VIDEO_URL}` `watch?v=…` biçiminde gelirse ilk `?` yerine `&` yazılır.
- YouTube adresindeki UTM grammar-kapi kayıtlarına düşmez; YouTube tarafı Studio "Trafik Kaynakları" ile ölçülür (§6).
- Instagram ve TikTok açıklamasına adres yazılmaz (tıklanmaz, §5). Çağrı "profildeki bağlantı" olur.

## 3. YouTube Shorts (öğrenci + öğretmen ortak dil, §7)

Başlık:

```
Yaşıyorum: I live mı, I am living mi? | YDT İngilizce #Shorts
```

Açıklama:

```
Simple Present ve Present Continuous (ING-YDT-GR-02-04-T) konusu püf noktası: Türkçede "yaşıyorum" tek sözcük, İngilizcede iki zaman.
I live in İstanbul. → kalıcı durum, geniş zaman
I am living with my uncle. → geçici durum, şimdiki zaman
Bu, iki zaman arasındaki üç farktan biri. Tam ders süresi: 4 dakika 26 saniye.
Dersin tamamını izle: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1
Sıradaki ders: Stative Verbs
Ders sayfası: https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

Elle adım: Studio'da "İlgili video" = uzun ders (API alanı yok; huni-plan karar sorusu 2).

## 4. Instagram Reels (öğretmen + YDT öğrencisi, `hikaye-taslak.md` §2)

```
Türkçede "yaşıyorum" tek sözcük. İngilizcede iki zaman:
I live in İstanbul. → kalıcı durum, Simple Present
I am living with my uncle. → geçici durum, Present Continuous
Bu, üç farktan biri. Üç farkın hepsi tam derste: 4 dakika 26 saniye.
Tam ders: profildeki bağlantı.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Stative Verbs

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

## 5. TikTok (öğretmen + YDT öğrencisi)

```
"Yaşıyorum" = I live mı, I am living mi?
Kalıcı durum: I live. Geçici durum: I am living.
Bu, üç farktan biri. Üç farkın hepsi tam derste (4 dakika 26 saniye). Tam ders: profildeki bağlantı.
Sıradaki ders: Stative Verbs
#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

TikTok `@ydspublishing` kullanıcı adı ve profil bağlantısı koşulu doğrulanmadı (dikey kalıp açık soru 4).

## 6. Şablondan sapma

| Şablon (huni-plan §4) | Bu taslak | Gerekçe |
|---|---|---|
| "Dersin tamamını kanalda izleyin" | "Dersin tamamını izle" | "kanal" sözü yok (karar A 05.11); bağlantı doğrudan uzun derse gider |
| "Tüm alıştırmalar ve testler: {platform_url}" | "Ders sayfası: …" | ders sayfasında alıştırma ve test olduğu doğrulanmadı; uydurma iddia yazılmaz |
| `ders_kodu` = `meta.kod` (Shorts) | ana ders kodu | açıklama ana dersi tanıtır; Shorts `utm_content=s1` ile ayrılır |
| `utm_campaign={ders_kodu}` (`ING-YDT-GR-02-04-T`) | küçük harf `ing-ydt-gr-02-04-t` | analitik büyük/küçük harfi ayırır, aynı kampanya iki biçimle bölünmesin; K35 yalnız biçim emsali (S1-C düzeltme 5). huni-plan §6 güncellemesi Nadir kararı |

## 7. Yer tutucular

| Yer tutucu | Nerede | Doldurma koşulu |
|---|---|---|
| `{UZUN_VIDEO_URL}` | §2 satır 1, §3 açıklama | ana ders YouTube'a yüklenince |
| (koşullu) `{PLATFORM_URL}` | §2, §3 | grammar-kapi yayında değilse `https://ydspublishing.com/grammar/02-04-ydt-temel` yerine konur |

## 8. Sürüm B — soru ile açılan set (istem S1-VAR, 15.11.2026)

Çıktı `aciklama-b.md` (paket kökü). A seti `aciklama-a.md` (= `aciklama.md` kopyası; tek fark `utm_content=s1` → `s1-a`).
`aciklama.md` değişmedi. Alanlar §1 ile aynı; tek fark `kanca_id` (`utm_content`) = `s1-b`.

| | A (`s1-a`) | B (`s1-b`) |
|---|---|---|
| İlk satır | yargı: "Türkçede yaşıyorum tek sözcük, İngilizcede iki zaman" | soru: "Yaşıyorum İngilizcede nasıl denir: I live mı, I am living mi?" |
| İkinci satır | örnekler | kısa cevap: "İkisi de doğru; seçimi anlam yapar." → örnekler |
| YouTube başlığı | `Yaşıyorum: I live mı, I am living mi? \| YDT İngilizce #Shorts` | `"Yaşıyorum" İngilizcede nasıl denir? \| YDT İngilizce #Shorts` |
| Gövde, süre, sıradaki ders, etiket | ortak | ortak |

YouTube başlığı (B):

```
"Yaşıyorum" İngilizcede nasıl denir? | YDT İngilizce #Shorts
```

YouTube açıklaması (B):

```
"Yaşıyorum" İngilizcede nasıl denir: I live mı, I am living mi?
İkisi de doğru; seçimi anlam yapar.
I live in İstanbul. → kalıcı durum, geniş zaman
I am living with my uncle. → geçici durum, şimdiki zaman
Bu, Simple Present ve Present Continuous (ING-YDT-GR-02-04-T) arasındaki üç farktan biri. Tam ders süresi: 4 dakika 26 saniye.
Dersin tamamını izle: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1-b
Sıradaki ders: Stative Verbs
Ders sayfası: https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1-b

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

Instagram Reels (B):

```
"Yaşıyorum" İngilizcede hangisi: I live mı, I am living mi?
Cevap anlama bağlı:
I live in İstanbul. → kalıcı durum, Simple Present
I am living with my uncle. → geçici durum, Present Continuous
Bu, üç farktan biri. Üç farkın hepsi tam derste: 4 dakika 26 saniye.
Tam ders: profildeki bağlantı.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Stative Verbs

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

TikTok (B):

```
Hangisi: I live mı, I am living mi?
"Yaşıyorum" ikisine de karşılık gelir. Kalıcı durum: I live. Geçici durum: I am living.
Bu, üç farktan biri. Üç farkın hepsi tam derste (4 dakika 26 saniye). Tam ders: profildeki bağlantı.
Sıradaki ders: Stative Verbs
#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

**DİKKAT (ölçüm sınırı):** profil bağlantısı (Instagram, TikTok `bio`) hesap başına tektir; aynı anda yalnız bir `utm_content`
taşır. A/B farkı UTM ile yalnız YouTube açıklama bağlantılarında ayrılır. Instagram ve TikTok'ta A/B karşılaştırması platform
istatistiğiyle yapılır (izlenme, kaydetme, profil ziyareti). `aciklama-b.md` profil satırlarını `s1-b` ile yazar; profil bağlantısı
hangi set yayındaysa onun değerini taşır.

Dil denetimi: "İkisi de doğru" yargısı derse dayanır (ana ders: aynı Türkçe sözcük, anlama göre iki zaman). Sen/siz hitabı yalnız
A ile aynı yerde ("Dersin tamamını izle", "Öğretmenseniz …"). "kanal" sözü yok.

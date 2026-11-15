# 02-04-ydt-temel-s2 · açıklama ve UTM taslağı — 2 set (YouTube · Instagram · TikTok)

Durum: TASLAK (istem S2-A, 15.11.2026). Yükleme YOK.
Şablon: huni-plan §4 (açıklama), §5 (platform kısıtı), §6 (UTM), §7 (dil). Emsal: S1 `aciklama-taslak.md` ve `../../02-04-ydt-temel-s1/aciklama.md`.
Set A = kısa, doğrudan (kural cümlesiyle açılır). Set B = soru ile açılır (kapak B ile aynı soru).
Düzeltme (istem S2-C, 15.11): jüri dil 3 (`konusunda püf nokta`), dil 2 + kaynak 3 (*today* satırı), kaynak 2 ("Bu" bağı), kaynak 4b
(dil gerekçesi), dil 1 + kaynak 1 (hikâye B cevap notu) işlendi; `S2-duzeltme.md`. Set A'da *today* satırı yok; set B'de *today* satırı
`geçebilir` ile, örneklerden ÖNCE durur: "Bu, üç farktan biri." her yerde iki örneğin hemen ardından gelir.

## 1. Alanlar

| Alan | Değer | Kaynak |
|---|---|---|
| `konu_adi` | Simple Present ve Present Continuous | ana ders `senaryo.json` → `baslik` |
| `ders_kodu` | `ING-YDT-GR-02-04-T` | ana ders `surumler.json` → `video.kod` |
| Shorts kodu | `ING-YDT-GR-02-04-T-S2` | dikey kalıp §7 |
| `gercek_sure` | 4 dakika 26 saniye (265,676 sn) | ana ders `cikti.mp4` ffprobe (15.11, bu istem) |
| `sonraki_ders_adi` | Stative Verbs (02-05) | ana ders BRIEF §1, senaryo cümle 18 |
| `platform_url` | `https://ydspublishing.com/grammar/02-04-ydt-temel` | S1 ile aynı (dijital-anlatim `sozlesme.md` madde 5 + K35; `worker/grammar-kapi/wrangler.toml`) |
| `uzun_video_url` | `{UZUN_VIDEO_URL}` | YER TUTUCU: ana ders YouTube'a yüklenmedi |
| Kimlik | `@ydspublishing` | karar A 05.11 (TikTok doğrulanmadı) |
| `kanca_id` (`utm_content`) | `s2-a` (set A) · `s2-b` (set B) | istem S2-A |
| Dil (Instagram/TikTok "öğretmen + YDT öğrencisi") | veli dili yok | gerekçe tablosu `hikaye-taslak.md` §2 (S2-C, jüri kaynak 4b) |

**UYARI:** `platform_url` belgeden türedi; canlılığı ölçülmedi (S1 ile aynı uyarı: grammar-kapi Worker 11.11'de yayında değil).
Yayından önce adresi aç. Açılmazsa adresi `{PLATFORM_URL}` ile değiştir ya da satırı çıkar.

## 2. UTM bağlantıları (§6 şeması)

`utm_campaign` = ders kodu olduğu gibi: `ING-YDT-GR-02-04-T` (istem S2-A). `utm_content` seti ayırır.

**DİKKAT:** S1 `utm_campaign=ing-ydt-gr-02-04-t` (küçük harf) yazar. Analitik büyük/küçük harfi ayırırsa S1 ve S2 aynı kampanyada toplanmaz.
S1 bu istemin yazma kapsamı dışında; eşitleme kararı şefte (`S2-A-RAPOR.md` açık nokta 1).

| Kullanım | Set A | Set B |
|---|---|---|
| YouTube açıklaması → uzun ders | `{UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-a` | `…&utm_content=s2-b` |
| YouTube açıklaması → ders sayfası | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-a` | `…&utm_content=s2-b` |
| Instagram profil bağlantısı | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=bio&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-a` | `…&utm_content=s2-b` |
| Instagram hikâye çıkartması (elle) | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=story&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-a` | `…&utm_content=s2-b` |
| TikTok profil bağlantısı | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=tiktok&utm_medium=bio&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-a` | `…&utm_content=s2-b` |

`…` = aynı satırın set A bağlantısı; yalnız son alan değişir.

- `{UZUN_VIDEO_URL}` `watch?v=…` biçiminde gelirse ilk `?` yerine `&` yazılır.
- YouTube adresindeki UTM grammar-kapi kayıtlarına düşmez; YouTube tarafı Studio "Trafik Kaynakları" ile ölçülür (§6).
- Profil bağlantısı hesap başına tektir: aynı anda yalnız bir set orada durur. Set A ve B profilde aynı anda ölçülemez (açık nokta 3).
- Instagram ve TikTok açıklamasına adres yazılmaz (tıklanmaz, §5). Çağrı "profildeki bağlantı" olur.

## 3. Set A — kısa, doğrudan

### YouTube Shorts (öğrenci + öğretmen ortak dil, §7)

Başlık:

```
Genel durum mu, konuşma anı mı? wears / is wearing | YDT İngilizce #Shorts
```

Açıklama:

```
Simple Present ve Present Continuous (ING-YDT-GR-02-04-T) konusunda püf nokta: genel durum geniş zaman, konuşma anı şimdiki zaman.
She wears her coat in the winter. → genel durum, geniş zaman
She is wearing her pink T-shirt today. → konuşma anı, şimdiki zaman
Bu, iki zaman arasındaki üç farktan biri. Tam ders süresi: 4 dakika 26 saniye.
Dersin tamamını izle: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-a
Sıradaki ders: Stative Verbs
Ders sayfası: https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-a

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

Elle adım: Studio'da "İlgili video" = uzun ders (API alanı yok). Kapak: `kapak-a.png` (sürüm A).

### Instagram Reels (öğretmen + YDT öğrencisi)

```
Genel durum: Simple Present. Konuşma anı: Present Continuous.
She wears her coat in the winter. → genel durum
She is wearing her pink T-shirt today. → konuşma anı
Bu, üç farktan biri. Üç farkın hepsi tam derste: 4 dakika 26 saniye.
Tam ders: profildeki bağlantı.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Stative Verbs

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

### TikTok (öğretmen + YDT öğrencisi)

```
Genel durum: wears. Konuşma anı: is wearing.
Bu, üç farktan biri. Üç farkın hepsi tam derste (4 dakika 26 saniye). Tam ders: profildeki bağlantı.
Sıradaki ders: Stative Verbs
#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

## 4. Set B — soru ile açılan

### YouTube Shorts

Başlık:

```
Today varsa hangi zaman? | YDT İngilizce #Shorts
```

Açıklama:

```
Cümlede today var: hangi zaman? Cevap sözcükte değil, anlamda: genel mi, şu an mı?
She wears her coat in the winter. → genel durum, geniş zaman
She is wearing her pink T-shirt today. → konuşma anı, şimdiki zaman
Simple Present ve Present Continuous (ING-YDT-GR-02-04-T): bu, iki zaman arasındaki üç farktan biri. Tam ders süresi: 4 dakika 26 saniye.
Dersin tamamını izle: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-b
Sıradaki ders: Stative Verbs
Ders sayfası: https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-b

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

Elle adım: Studio'da "İlgili video" = uzun ders. Kapak: `kapak-b.png` (sürüm B; başlık ile aynı soru).

### Instagram Reels

```
Cümlede today var: hangi zaman?
Today iki zamanda da geçebilir. Karar anlamda: genel mi, şu an mı?
She wears her coat in the winter. → genel durum, Simple Present
She is wearing her pink T-shirt today. → konuşma anı, Present Continuous
Bu, üç farktan biri. Üç farkın hepsi tam derste: 4 dakika 26 saniye.
Tam ders: profildeki bağlantı.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Stative Verbs

#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

### TikTok

```
Today varsa hangi zaman?
Today iki zamanda da geçebilir; farkı anlam yapar. Genel durum: wears. Konuşma anı: is wearing.
Bu, üç farktan biri. Üç farkın hepsi tam derste (4 dakika 26 saniye). Tam ders: profildeki bağlantı.
Sıradaki ders: Stative Verbs
#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

Hikâye soru kartı (`hikaye-taslak.md` §4) cevap notu, yalnız elle paylaşan için: doğru şık **B) is wearing** (`Look!` konuşma anını
gösterir; bugünkü kıyafet şu an görülüyor).

## 5. Set farkı

| | Set A | Set B |
|---|---|---|
| İlk satır | kural: "genel durum geniş zaman, konuşma anı şimdiki zaman" | soru: "Cümlede today var: hangi zaman?" |
| *today* | satır yok (S2-C, jüri kaynak 3 (b)) | açılış sorusu; cevap açılış satırında (YouTube) ya da 2. satırda (Instagram, TikTok), örneklerden önce |
| Eşleşen kapak | A (`GENEL` / `≠ ŞU AN`) | B (`TODAY VARSA` / `HANGİ ZAMAN?`) |
| Uzunluk (Instagram) | 9 satır | 9 satır; ilk satır daha kısa |
| Ortak | örnekler, "üç farktan biri", süre, sıradaki ders, etiketler, yer tutucular | aynı |

Kapak C ile hangi set eşleşir: ikisi de olur; önerim set A (C örneği gösterir, A örneği açıklar).

## 6. Şablondan sapma

| Şablon (huni-plan §4) | Bu taslak | Gerekçe |
|---|---|---|
| "Dersin tamamını kanalda izleyin" | "Dersin tamamını izle" | "kanal" sözü yok (karar A 05.11); S1 ile aynı |
| "Tüm alıştırmalar ve testler: {platform_url}" | "Ders sayfası: …" | ders sayfasında alıştırma ve test doğrulanmadı; S1 ile aynı |
| `ders_kodu` = `meta.kod` (Shorts) | ana ders kodu | açıklama ana dersi tanıtır; Shorts `utm_content` ile ayrılır; S1 ile aynı |
| `utm_content={kanca_id}` tek değer | `s2-a` / `s2-b` | iki açıklama seti (istem S2-A) |

`utm_campaign` şemaya uyar (`ING-YDT-GR-02-04-T`, olduğu gibi). S1'in küçük harf sapması bu sette yok.

## 7. Yer tutucular (S1 ile aynı)

| Yer tutucu | Nerede | Doldurma koşulu |
|---|---|---|
| `{UZUN_VIDEO_URL}` | §2 satır 1; §3 ve §4 YouTube açıklaması | ana ders YouTube'a yüklenince |
| `{PLATFORM_URL}` (koşullu) | §2; §3 ve §4 "Ders sayfası" | grammar-kapi yayında değilse `https://ydspublishing.com/grammar/02-04-ydt-temel` yerine |
| süre `4 dakika 26 saniye` (koşullu) | §3, §4 | ana ders yeniden render olursa ffprobe değeriyle (huni-plan §4: elle süre yasak) |

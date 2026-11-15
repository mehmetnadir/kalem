# simple-present-temel-s2 · açıklama ve UTM taslağı — 2 set (YouTube · Instagram · TikTok)

Durum: TASLAK (istem P0202-S2-A, 15.11.2026). Yükleme YOK.
Kural: `huni-v2-standart.md` §1 kural 4–6 ("Tam ders" yok, süre sözü yok, kaydet teşviki), §4 (ilk satır; Reels açıklamasında bağ yok, yalnız
`@ydspublishing`); `huni-plan-1211.md` §4 (alanlar), §5 (platform kısıtı), §6 (UTM), §7 (dil). Emsal biçim: `02-04-ydt-temel-s2/uretim-tutanagi/aciklama-taslak.md`.
Set A = kısa, doğrudan (kural cümlesiyle açılır). Set B = soru ile açılır (kapak B ile aynı soru). İki sette de ilk satır standart §4 satırıdır;
set B'nin sorusu ikinci satırdadır ve YouTube başlığını açar.

## 1. Alanlar

| Alan | Değer | Kaynak |
|---|---|---|
| `konu_adi` | Simple Present | ana ders `senaryo.json` → `baslik` |
| `ders_kodu` | `ING-YDT-GR-02-02-T` | ana ders `surumler.json` → `video.kod` |
| Shorts kodu | `ING-YDT-GR-02-02-T-S2` | dikey kalıp §7 |
| `sonraki_ders_adi` | Present Continuous ve Simple Present | `02-03-ydt-temel/ortak/anlatim/senaryo.json` → `baslik`; sıra kimlikten (02-02 → 02-03), katalogda doğrulanmadı |
| `platform_url` | `https://ydspublishing.com/grammar/02-02-ydt-temel` | `dijital-anlatim/worker/grammar-kapi/wrangler.toml` satır 6 (`/grammar/<kimlik>`); 02-04 S2 ile aynı kalıp |
| `uzun_video_url` | `{UZUN_VIDEO_URL}` | YER TUTUCU: ana dersin YouTube adresi bu pakette yok |
| Kimlik | `@ydspublishing` | standart §1 kural 1, §4 |
| `kanca_id` (`utm_content`) | `s2-a` (set A) · `s2-b` (set B) | istem P0202-S2-A |
| Dil | öğretmen + dil sınavı öğrencisi; veli dili yok | istem; gerekçe `hikaye-taslak.md` §2 |
| Süre | yazılmaz | standart §1 kural 5 (12.11 ölçümü: süre sözü yanlış çıkıyordu) |

**UYARI:** `platform_url` belgeden türedi; canlılığı ölçülmedi (02-04 S2 ile aynı uyarı). Yayından önce adresi aç. Açılmazsa satırı
`{PLATFORM_URL}` ile değiştir ya da çıkar.

## 2. UTM bağlantıları (huni-plan §6 şeması)

`utm_campaign` = ders kodu olduğu gibi: `ING-YDT-GR-02-02-T`. `utm_content` seti ayırır.

| Kullanım | Set A | Set B |
|---|---|---|
| YouTube açıklaması → ana ders | `{UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s2-a` | `…&utm_content=s2-b` |
| YouTube açıklaması → ders sayfası | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s2-a` | `…&utm_content=s2-b` |
| Instagram profil bağlantısı | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=instagram&utm_medium=bio&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s2-a` | `…&utm_content=s2-b` |
| Instagram hikâye çıkartması (elle) | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=instagram&utm_medium=story&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s2-a` | `…&utm_content=s2-b` |
| TikTok profil bağlantısı | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=tiktok&utm_medium=bio&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s2-a` | `…&utm_content=s2-b` |

`…` = aynı satırın set A bağlantısı; yalnız son alan değişir.

- `{UZUN_VIDEO_URL}` `watch?v=…` biçiminde gelirse ilk `?` yerine `&` yazılır.
- YouTube adresindeki UTM grammar-kapi kayıtlarına düşmez; YouTube tarafı Studio "Trafik Kaynakları" ile ölçülür (huni-plan §6).
- Profil bağlantısı hesap başına tektir: aynı anda yalnız bir set orada durur.
- Instagram açıklamasına adres ve "bağlantı" çağrısı yazılmaz (standart §4: yalnız `@ydspublishing`). TikTok açıklamasında adres tıklanmaz;
  "Ders sayfası: profildeki bağlantı." satırı durur.

## 3. Set A — kısa, doğrudan

### YouTube Shorts

Başlık:

```
Usually, always, every day = Simple Present | YDT İngilizce #Shorts
```

Açıklama:

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Simple Present (ING-YDT-GR-02-02-T) konusunda püf nokta: usually, always, every day alışkanlık işaretidir. Alışkanlık: Simple Present.
My brother usually goes to school by bus. → Kardeşim genellikle okula otobüsle gider.
Türkçede de geniş zaman: Her sabah yedide kalkarım.
Dersin tamamı: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s2-a
Ders sayfası: https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s2-a
Sıradaki ders: Present Continuous ve Simple Present

#YDT #İngilizce #gramer #SimplePresent
```

Elle adım: Studio'da "İlgili video" = ana ders (API alanı yok). Kapak: `kapak-a.png`.

### Instagram Reels

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Usually, always, every day: alışkanlık işareti. Alışkanlık: Simple Present.
My brother usually goes to school by bus. → alışkanlık, şu an olan iş değil
Türkçede de geniş zaman: Her sabah yedide kalkarım.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Present Continuous ve Simple Present

#YDT #İngilizce #gramer #SimplePresent
```

### TikTok

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Usually, always, every day: Simple Present. My brother usually goes to school by bus.
Ders sayfası: profildeki bağlantı. Sıradaki ders: Present Continuous ve Simple Present
#YDT #İngilizce #gramer #SimplePresent
```

## 4. Set B — soru ile açılan

### YouTube Shorts

Başlık:

```
Always varsa hangi zaman? | YDT İngilizce #Shorts
```

Açıklama:

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Cümlede always, usually ya da every day var: hangi zaman? Alışkanlık işareti: Simple Present. Şu an olan iş değil.
My brother usually goes to school by bus. → alışkanlık, geniş zaman
Türkçede de öyle: Her sabah yedide kalkarım.
Simple Present (ING-YDT-GR-02-02-T) dersinden.
Dersin tamamı: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s2-b
Ders sayfası: https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s2-b
Sıradaki ders: Present Continuous ve Simple Present

#YDT #İngilizce #gramer #SimplePresent
```

Elle adım: Studio'da "İlgili video" = ana ders. Kapak: `kapak-b.png` (başlık ile aynı soru).

### Instagram Reels

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Always varsa hangi zaman?
Usually, always, every day: alışkanlık işareti. İlk akla gelen: Simple Present.
My brother usually goes to school by bus. → şu an değil, alışkanlık
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Present Continuous ve Simple Present

#YDT #İngilizce #gramer #SimplePresent
```

### TikTok

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Always varsa hangi zaman? Usually, always, every day: alışkanlık. İlk akla gelen: Simple Present.
Ders sayfası: profildeki bağlantı. Sıradaki ders: Present Continuous ve Simple Present
#YDT #İngilizce #gramer #SimplePresent
```

Hikâye soru kartı (`hikaye-taslak.md` §4) cevap notu, yalnız elle paylaşan için: doğru şık **A) goes** (`usually` alışkanlık işaretidir;
alışkanlık Simple Present ister).

## 5. Set farkı

| | Set A | Set B |
|---|---|---|
| Başlık | kural kodu: `Usually, always, every day = Simple Present` | soru: `Always varsa hangi zaman?` |
| 2. satır | kural cümlesi (püf nokta) | soru, cevap aynı satırda (YouTube) ya da sonraki satırda (Instagram, TikTok) |
| "Şu an değil" | Instagram örnek satırında | YouTube 2. satırda, Instagram örnek satırında |
| Türkçe köprü | YouTube + Instagram | yalnız YouTube |
| Eşleşen kapak | A (`USUALLY` / `= ALIŞKANLIK`) | B (`ALWAYS VARSA` / `HANGİ ZAMAN?`) |
| Ortak | ilk satır, örnek, sıradaki ders, etiketler, yer tutucular | aynı |

Kapak C ile hangi set eşleşir: ikisi de olur; önerim set A (C kuralı kart olarak verir, A kuralı cümle olarak açar).

## 6. Şablondan sapma

| Şablon | Bu taslak | Gerekçe |
|---|---|---|
| huni-plan §4 "Dersin tamamını kanalda izleyin" | ilk satır standart §4 cümlesi; YouTube'da "Dersin tamamı: {bağlantı}" | standart §4 bağlayıcı |
| huni-plan §4 süre alanı (`gercek_sure`) | yok | standart §1 kural 5 |
| huni-plan §4 "Tüm alıştırmalar ve testler: {platform_url}" | "Ders sayfası: …" | ders sayfasında alıştırma/test doğrulanmadı; 02-04 S2 ile aynı |
| 02-04 S2 emsali "Tam ders: profildeki bağlantı" | Instagram'da yok; TikTok'ta "Ders sayfası: profildeki bağlantı." | standart §1 kural 4 ("Tam ders" yok), §4 (Reels'te yalnız `@ydspublishing`) |
| huni-plan §7 Instagram/TikTok veli dili | öğretmen + dil sınavı öğrencisi | istem; gerekçe `hikaye-taslak.md` §2 |

## 7. Yer tutucular

| Yer tutucu | Nerede | Doldurma koşulu |
|---|---|---|
| `{UZUN_VIDEO_URL}` | §2 satır 1; §3 ve §4 YouTube açıklaması | ana ders YouTube'a yüklenince |
| `{PLATFORM_URL}` (koşullu) | §2; §3 ve §4 "Ders sayfası" | grammar-kapi yayında değilse `https://ydspublishing.com/grammar/02-02-ydt-temel` yerine |

# simple-present-temel-s3 · açıklama ve UTM taslağı — 2 set (YouTube · Instagram · TikTok)

Durum: TASLAK (istem P0202-S3-A, 15.11.2026). Yükleme YOK. S3-C (15.11): jüri düzeltmeleri işlendi (`S3-duzeltme.md`); paket kökü
`aciklama-a.md`, `aciklama-b.md`, `aciklama.md` (= A) bu taslaktan.
Şablon: `huni-v2-standart.md` §4 (ilk satır), §1 kural 4–5 (yasak sözler); `huni-plan-1211.md` §4–§6 (açıklama, platform, UTM).
Emsal biçim: `02-04-ydt-temel-s2` `aciklama-taslak.md` ve v2 açıklaması `../../02-04-ydt-temel-s3/aciklama-b.md`.
Set A = kısa, doğrudan (kuralla açılır). Set B = soru ile açılır (kapak B ile aynı soru).
Her platform metninin ilk satırı standart §4 satırıdır: `Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.`
Set farkı ikinci satırdan ve YouTube başlığından başlar.

## 1. Alanlar

| Alan | Değer | Kaynak |
|---|---|---|
| `konu_adi` | Simple Present | ana `senaryo.json` → `baslik` |
| `ders_kodu` | `ING-YDT-GR-02-02-T` | ana `surumler.json` → `video.kod` |
| Shorts kodu | `ING-YDT-GR-02-02-T-S3` | dikey kalıp §7 |
| `sonraki_ders_adi` | Present Continuous ve Simple Present: ayrım alıştırması | `../../02-03-ydt-temel/surumler.json` → `video.konu` (katalog sırası; ana derste sonraki ders sözü yok) |
| `platform_url` | `https://ydspublishing.com/grammar/02-02-ydt-temel` | emsal kalıbı `grammar/<öğe kimliği>` |
| `uzun_video_url` | `{UZUN_VIDEO_URL}` | YER TUTUCU: ana ders YouTube'a yüklenmedi |
| Kimlik | `@ydspublishing` | standart §1 kural 1 |
| `kanca_id` (`utm_content`) | `s3-a` (set A) · `s3-b` (set B) | istem |
| Süre satırı | yok | standart §1 kural 5 |
| Dil | öğretmen + dil sınavı öğrencisi; veli dili yok | istem; gerekçe `hikaye-taslak.md` §2 (jüri kaynak 3) |

**UYARI:** `platform_url` belgeden türedi; canlılığı ölçülmedi (emsal uyarısı: grammar-kapi Worker 11.11'de yayında değil).
Yayından önce adresi aç. Açılmazsa adresi `{PLATFORM_URL}` ile değiştir ya da satırı çıkar.

## 2. UTM bağlantıları (huni-plan §6 şeması)

Şema: `?utm_source={youtube|instagram|tiktok}&utm_medium={short|reel|story|bio}&utm_campaign={ders_kodu}&utm_content={kanca_id}`.
`utm_campaign` = ders kodu olduğu gibi: `ING-YDT-GR-02-02-T`. `utm_content` seti ayırır.

| Kullanım | Set A | Set B |
|---|---|---|
| YouTube açıklaması → uzun ders | `{UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s3-a` | `…&utm_content=s3-b` |
| YouTube açıklaması → ders sayfası | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s3-a` | `…&utm_content=s3-b` |
| Instagram profil bağlantısı | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=instagram&utm_medium=bio&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s3-a` | `…&utm_content=s3-b` |
| Instagram hikâye çıkartması (elle) | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=instagram&utm_medium=story&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s3-a` | `…&utm_content=s3-b` |
| TikTok profil bağlantısı | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=tiktok&utm_medium=bio&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s3-a` | `…&utm_content=s3-b` |

`…` = aynı satırın set A bağlantısı; yalnız son alan değişir.

- `{UZUN_VIDEO_URL}` `watch?v=…` biçiminde gelirse ilk `?` yerine `&` yazılır.
- YouTube adresindeki UTM grammar-kapi kayıtlarına düşmez; YouTube tarafı Studio "Trafik Kaynakları" ile ölçülür (huni-plan §6).
- Profil bağlantısı hesap başına tektir: aynı anda yalnız bir set orada durur. Set A ve B profilde aynı anda ölçülemez.
- Instagram ve TikTok açıklamasına adres yazılmaz (tıklanmaz; standart §4 "Reels açıklamasında bağ yok"). Çağrı "profildeki bağlantı" olur.

## 3. Set A — kısa, doğrudan

### YouTube Shorts

Başlık:

```
Does varsa fiil yalın: He doesn't go | YDT İngilizce #Shorts
```

Açıklama:

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Simple Present (ING-YDT-GR-02-02-T) dersinden sınav tuzağı: does girince fiildeki s düşer.
YANLIŞ: He doesn't goes. → DOĞRU: He doesn't go.
YANLIŞ: Does she goes? → DOĞRU: Does she go?
Olumsuzda ve soruda does girer, s ona geçer; fiil yalın kalır.
Dersin tamamını izle: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s3-a
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması
Ders sayfası: https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s3-a

#YDT #İngilizce #gramer #SimplePresent
```

Elle adım: Studio'da "İlgili video" = uzun ders (API alanı yok). Kapak: `kapak-a.png` (kanca karesi; başlık kuralı söyler, kapak yanlış cümleyi gösterir). `kapak-c.png` bu başlıkla kullanılmaz:
ikisi aynı sözü taşır (`kapak-standardi.md` satır 41; dil jürisi 3).

### Instagram Reels

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Sınav tuzağı: does girince fiildeki s düşer.
YANLIŞ: He doesn't goes. DOĞRU: He doesn't go.
YANLIŞ: Does she goes? DOĞRU: Does she go?
Does varsa fiil yalın.
Ders sayfası: profildeki bağlantı.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması

#YDT #İngilizce #gramer #SimplePresent
```

Hikâye: `hikaye-a.png` (kural özeti + Kaydet). Bağlantı çıkartması: §2 tablosu, set A.

### TikTok

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Does varsa fiil yalın: He doesn't go. Does she go?
He doesn't goes ve Does she goes: ikisi de YANLIŞ.
Ders sayfası: profildeki bağlantı.
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması
#YDT #İngilizce #gramer #SimplePresent
```

## 4. Set B — soru ile açılan

### YouTube Shorts

Başlık:

```
Does gelince fiile s gelir mi? | YDT İngilizce #Shorts
```

Açıklama:

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Goes mu, go mu? Cümlede does ya da doesn't varsa fiil yalın kalır.
Olumsuzda ve soruda does girer, s ona geçer. Fiile s gelmez.
He doesn't go. → olumsuz, fiil yalın
Does she go? → soru, fiil yalın
Simple Present (ING-YDT-GR-02-02-T) dersinden bir sınav tuzağı.
Dersin tamamını izle: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s3-b
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması
Ders sayfası: https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s3-b

#YDT #İngilizce #gramer #SimplePresent
```

Elle adım: Studio'da "İlgili video" = uzun ders. Kapak: `kapak-b.png` (soru kapağı; başlık başka soruyu sorar, kapak iki şıkkı gösterir; dil jürisi 3).

### Instagram Reels

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Goes mu, go mu?
Does varsa fiil yalın: He doesn't go. Does she go?
Olumsuzda ve soruda does girer, s ona geçer. Fiile s gelmez.
Ders sayfası: profildeki bağlantı.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması

#YDT #İngilizce #gramer #SimplePresent
```

Hikâye: `hikaye-b.png` (soru kartı + Kaydet). Bağlantı çıkartması: §2 tablosu, set B.

### TikTok

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Goes mu, go mu?
Does varsa fiil yalın: He doesn't go. Does she go?
Ders sayfası: profildeki bağlantı.
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması
#YDT #İngilizce #gramer #SimplePresent
```

Hikâye soru kartı (`hikaye-taslak.md` §4) cevap notu, yalnız elle paylaşan için: doğru şık **A) go** (soruda does girer ve s'yi
taşır; fiil yalın kalır).

## 5. Set farkı

| | Set A | Set B |
|---|---|---|
| İkinci satır | kural: "does girince fiildeki s düşer" | soru: "Goes mu, go mu?" |
| Örnek biçimi | YANLIŞ → DOĞRU çiftleri (iki tuzak) | yalnız doğru cümleler + neden |
| Neden satırı | "s ona geçer; fiil yalın kalır" | "s ona geçer. Fiile s gelmez." |
| Eşleşen kapak | A (`BU CÜMLE` / `YANLIŞ`) | B (`GOES mu,` / `GO mu?`) |
| Eşleşen hikâye | `hikaye-a.png` | `hikaye-b.png` |
| Ortak | ilk satır (standart §4), sıradaki ders, etiketler, yer tutucular, UTM şeması | aynı |

## 6. Şablondan sapma

| Şablon (huni-plan §4) | Bu taslak | Gerekçe |
|---|---|---|
| ilk satır serbest | standart §4 sabit satırı | huni v2 standardı bağlayıcı |
| "Dersin tamamını kanalda izleyin" | "Dersin tamamını izle" | emsal S2 ve v2 açıklaması ile aynı |
| "Tüm alıştırmalar ve testler: {platform_url}" | "Ders sayfası: …" | ders sayfasında alıştırma ve test doğrulanmadı (emsal) |
| `gercek_sure` satırı | yok | standart §1 kural 5 |
| `ders_kodu` = Shorts kodu | ana ders kodu | açıklama ana dersi tanıtır; Shorts `utm_content` ile ayrılır (emsal) |
| `utm_content={kanca_id}` tek değer | `s3-a` / `s3-b` | iki açıklama seti (istem) |

## 7. Yer tutucular

| Yer tutucu | Nerede | Doldurma koşulu |
|---|---|---|
| `{UZUN_VIDEO_URL}` | §2 satır 1; §3 ve §4 YouTube açıklaması | ana ders YouTube'a yüklenince |
| `{PLATFORM_URL}` (koşullu) | §2; §3 ve §4 "Ders sayfası" | grammar-kapi yayında değilse `https://ydspublishing.com/grammar/02-02-ydt-temel` yerine |

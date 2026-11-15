# simple-present-temel-s1 · açıklama ve UTM taslağı — 2 set (YouTube · Instagram · TikTok) · huni v2

Durum: TASLAK (istem P0202-S1-A, 15.11.2026). Yükleme YOK.
Kural: `huni-v2-standart.md` §4 (ilk satır), §6 (yasak sözler); `huni-plan-1211.md` §4 (alanlar), §5 (platform kısıtı), §6 (UTM), §7 (dil).
Biçim emsali: 02-04-s2 `aciklama-taslak.md` (yer tutucular aynen). Eski kalıptaki süre satırı ve eski kapanış sözü v2'de yok.
Set A = kısa, doğrudan (kural ile sürer). Set B = soru ile açılır (Reels/TikTok kapak B'nin sorusuyla; YouTube başlığı kapaktan ayrı, jüri D4). İki sette de ilk satır standart §4 cümlesidir.
Dil: öğretmene ve dil sınavı öğrencisine; veli dili yok (istem; gerekçe 02-04-s2 `hikaye-taslak.md` §2).

## 1. Alanlar

| Alan | Değer | Kaynak |
|---|---|---|
| İlk satır | `Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.` | standart §4 |
| `konu_adi` | Simple Present | ana ders `senaryo.json` → `baslik` |
| `ders_kodu` | `ING-YDT-GR-02-02-T` | ana ders `surumler.json` → `video.kod` |
| Shorts kodu | `ING-YDT-GR-02-02-T-S1` | kalıp §7 |
| `sonraki_ders_adi` | Present Continuous ve Simple Present: ayrım alıştırması (02-03) | `../../02-03-ydt-temel/surumler.json` → `video.konu`; katalog sırası (huni-plan §4) |
| `platform_url` | `https://ydspublishing.com/grammar/02-02-ydt-temel` | 02-04-s2 adres kalıbı; `dijital-anlatim/worker/grammar-kapi/wrangler.toml` (`/grammar/<kimlik>` giriş sayfası); `sozlesme.md` K35 |
| `uzun_video_url` | `{UZUN_VIDEO_URL}` | YER TUTUCU: ana ders YouTube'a yüklenmedi |
| Kimlik | `@ydspublishing` | karar A 05.11 (TikTok doğrulanmadı) |
| `kanca_id` (`utm_content`) | `s1-a` (set A) · `s1-b` (set B) | istem P0202-S1-A |
| Süre alanı | yok | standart §1 kural 5 |

**UYARI:** `platform_url` belgeden türedi; canlılığı ölçülmedi (02-04-s2 ile aynı uyarı). Yayından önce adresi aç. Açılmazsa adresi
`{PLATFORM_URL}` ile değiştir ya da satırı çıkar.

## 2. UTM bağlantıları (huni-plan §6 şeması)

`utm_campaign` = ders kodu olduğu gibi: `ING-YDT-GR-02-02-T` (büyük harf; 02-04-s2 ile aynı yazım). `utm_content` seti ayırır.

| Kullanım | Set A | Set B |
|---|---|---|
| YouTube açıklaması → uzun ders | `{UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s1-a` | `…&utm_content=s1-b` |
| YouTube açıklaması → ders sayfası | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s1-a` | `…&utm_content=s1-b` |
| Instagram profil bağlantısı | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=instagram&utm_medium=bio&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s1-a` | `…&utm_content=s1-b` |
| Instagram hikâye çıkartması (elle) | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=instagram&utm_medium=story&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s1-a` | `…&utm_content=s1-b` |
| TikTok profil bağlantısı | `https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=tiktok&utm_medium=bio&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s1-a` | `…&utm_content=s1-b` |

`…` = aynı satırın set A bağlantısı; yalnız son alan değişir.

- `{UZUN_VIDEO_URL}` `watch?v=…` biçiminde gelirse ilk `?` yerine `&` yazılır.
- YouTube adresindeki UTM grammar-kapi kayıtlarına düşmez; YouTube tarafı Studio "Trafik Kaynakları" ile ölçülür (huni-plan §6).
- Profil bağlantısı hesap başına tektir: aynı anda yalnız bir set orada durur.
- Reels ve TikTok açıklamasında bağ yok; yalnız `@ydspublishing` (standart §4, huni-plan §5).

## 3. Set A — kısa, doğrudan

### YouTube Shorts

Başlık:

```
Simple Present: s yalnız he, she, it ile | YDT İngilizce #Shorts
```

Açıklama:

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Simple Present (ING-YDT-GR-02-02-T): Türkçedeki geniş zaman eki = İngilizcedeki s. Gider = goes.
My brother goes to school by bus. → my brother = he, fiile s gelir
He, she, it: s gelir. I, you, we, they: s yok.
Ders videosu: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s1-a
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması
Ders sayfası: https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s1-a

#YDT #İngilizce #gramer #SimplePresent
```

Elle adım: Studio'da "İlgili video" = uzun ders (API alanı yok). Kapak: `kapak-c.png` (sürüm C; cevap çifti, set A'nın doğrudan diliyle aynı).

### Instagram Reels

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Kardeşim gider → My brother goes.
He, she, it: fiile s gelir. I, you, we, they: s yok.
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması

#YDT #İngilizce #gramer #SimplePresent
```

### TikTok

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Kardeşim gider → My brother goes. He, she, it: s gelir. I, you, we, they: s yok.
#YDT #İngilizce #gramer #SimplePresent
```

## 4. Set B — soru ile açılan

### YouTube Shorts

Başlık:

```
My brother goes: s nereden geliyor? | YDT İngilizce #Shorts
```

Açıklama:

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Hangi özne fiile s getirir? Cevap: he, she, it. I, you, we, they ile s gelmez.
My brother goes to school by bus. → my brother = he, fiile s gelir
Simple Present (ING-YDT-GR-02-02-T): Türkçedeki geniş zaman eki = İngilizcedeki s. Gider = goes.
Ders videosu: {UZUN_VIDEO_URL}?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s1-b
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması
Ders sayfası: https://ydspublishing.com/grammar/02-02-ydt-temel?utm_source=youtube&utm_medium=short&utm_campaign=ING-YDT-GR-02-02-T&utm_content=s1-b

#YDT #İngilizce #gramer #SimplePresent
```

Elle adım: Studio'da "İlgili video" = uzun ders. Kapak: `kapak-b.png` (sürüm B; başlık kapağın sorusunu yinelemez, jüri D4).

### Instagram Reels

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Fiile s hangi özneyle gelir?
He, she, it: goes. I, you, we, they: go.
My brother goes to school by bus. (my brother = he)
Öğretmenseniz sınıfınızla paylaşın.
Sıradaki ders: Present Continuous ve Simple Present: ayrım alıştırması

#YDT #İngilizce #gramer #SimplePresent
```

### TikTok

```
Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında.
Fiile s hangi özneyle gelir? He, she, it: goes. I, you, we, they: go.
#YDT #İngilizce #gramer #SimplePresent
```

Hikâye soru kartı (`hikaye-taslak.md` §5) cevap notu, yalnız elle paylaşan için: doğru şık **A) go** (özne *my parents* = they;
they ile fiile s gelmez).

## 5. Set farkı

| | Set A | Set B |
|---|---|---|
| Satır 2 | köprü: "gider = goes" (YouTube) · "Kardeşim gider → My brother goes." (Reels, TikTok) | soru: "Fiile s hangi özneyle gelir?" |
| Kural | örnekten sonra | sorunun hemen cevabı |
| Eşleşen kapak | C (`HE GOES` / `I GO`) | B (`FİİLE -S` / `HANGİ ÖZNEYLE?`); YouTube B başlığı kapaktan ayrı (jüri D4) |
| Uzunluk (Reels) | 6 satır | 7 satır |
| Ortak | ilk satır, örnek, sıradaki ders, etiketler, yer tutucular | aynı |

Kapak A videonun ilk karesidir; platform kapağı seçilmezse akışta o görünür.

## 6. Şablondan sapma

| Şablon (huni-plan §4) | Bu taslak | Gerekçe |
|---|---|---|
| "{konu_adi} ({ders_kodu}) konusu püf noktası." | "Simple Present (…): Türkçedeki geniş zaman eki = İngilizcedeki s. Gider = goes." | jüri D3: "köprü" iç terim; ana dersin kendi cümlesi (`canAlici[0]`) |
| Süre satırı | yok | standart §1 kural 5 |
| "Dersin tamamını kanalda izleyin: {uzun_video_url}…" | ilk satır standart §4 + "Ders videosu: {UZUN_VIDEO_URL}…" | standart §4 ilk satır; kanal sözü ilk satırda bir kez |
| "Tüm alıştırmalar ve testler: {platform_url}" | "Ders sayfası: …" | ders sayfasında alıştırma ve test doğrulanmadı (02-04-s2 ile aynı) |
| `ders_kodu` = `meta.kod` (Shorts) | ana ders kodu | açıklama ana dersi tanıtır; Shorts `utm_content` ile ayrılır |

## 7. Yer tutucular

| Yer tutucu | Nerede | Doldurma koşulu |
|---|---|---|
| `{UZUN_VIDEO_URL}` | §2 satır 1; §3 ve §4 YouTube açıklaması | ana ders YouTube'a yüklenince |
| `{PLATFORM_URL}` (koşullu) | §2; §3 ve §4 "Ders sayfası" | grammar-kapi yayında değilse `https://ydspublishing.com/grammar/02-02-ydt-temel` yerine |

# 02-04-ydt-temel-s1 · açıklama metni (YouTube · Instagram · TikTok)

Kaynak: `uretim-tutanagi/aciklama-taslak.md` (S1-B jürisi + S1-C düzeltmeleri, `uretim-tutanagi/S1-duzeltme.md`).
Ana ders: Simple Present ve Present Continuous (`ING-YDT-GR-02-04-T`), tam ders süresi 4 dakika 26 saniye (`cikti.mp4` 265,7 sn).
Shorts: `ING-YDT-GR-02-04-T-S1`, 30,56 sn. Kimlik `@ydspublishing`. "kanal" sözü yok, QR yok.

**UYARI:** `https://ydspublishing.com/grammar/02-04-ydt-temel` belgeden türedi; canlılığı ölçülmedi (grammar-kapi Worker 11.11'de
yayında değil). Paylaşımdan önce adresi aç. Açılmazsa adresi `{PLATFORM_URL}` ile değiştir ya da satırı çıkar.

**UYARI:** Yayın anında ana ders `cikti.mp4` süresini ffprobe ile yeniden ölç. Süre değişirse "4 dakika 26 saniye" satırlarını düzelt.

## 1. YouTube Shorts

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

Elle adım: Studio'da "İlgili video" = uzun ders (API alanı yok). Kapak: `kapak.png`.

## 2. Instagram

Reels açıklaması:

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

Profil bağlantısı:
`https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=bio&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1`

Hikâye: `hikaye.png` (elle paylaşım). Bağlantı çıkartması (elle; uygulama özelliği, doğrulanmadı):
`https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=story&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1`

Açıklamaya adres yazılmaz (Instagram açıklamada bağlantı tıklanmaz).

## 3. TikTok

```
"Yaşıyorum" = I live mı, I am living mi?
Kalıcı durum: I live. Geçici durum: I am living.
Bu, üç farktan biri. Üç farkın hepsi tam derste (4 dakika 26 saniye). Tam ders: profildeki bağlantı.
Sıradaki ders: Stative Verbs
#YDT #İngilizce #gramer #SimplePresent #PresentContinuous
```

Profil bağlantısı:
`https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=tiktok&utm_medium=bio&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1`

**DİKKAT:** TikTok `@ydspublishing` kullanıcı adı ve profil bağlantısı koşulu doğrulanmadı. Hesap açılınca doğrula.

## 4. UTM kuralı

| Alan | Değer |
|---|---|
| `utm_source` | `youtube` · `instagram` · `tiktok` |
| `utm_medium` | `short` (YouTube açıklaması) · `bio` (profil bağlantısı) · `story` (Instagram hikâye çıkartması) |
| `utm_campaign` | `ing-ydt-gr-02-04-t` (ana ders kodu, küçük harf; huni-plan §6'dan sapma, gerekçe taslak §6) |
| `utm_content` | `s1` |

- `{UZUN_VIDEO_URL}` `watch?v=…` biçiminde gelirse ilk `?` yerine `&` yaz.
- YouTube adresindeki UTM grammar-kapi kayıtlarına düşmez; YouTube tarafını Studio "Trafik Kaynakları" ölçer.

## 5. Yer tutucular

| Yer tutucu | Nerede | Doldurma koşulu |
|---|---|---|
| `{UZUN_VIDEO_URL}` | §1 açıklama, "Dersin tamamını izle" satırı | ana ders YouTube'a yüklenince |
| `{PLATFORM_URL}` (koşullu) | §1 "Ders sayfası", §2 profil + hikâye, §3 profil | grammar-kapi yayında değilse `https://ydspublishing.com/grammar/02-04-ydt-temel` yerine |
| süre `4 dakika 26 saniye` (koşullu) | §1, §2, §3 | ana ders yeniden render olursa ffprobe değeriyle |

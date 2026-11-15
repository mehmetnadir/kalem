Jüri modeli: Claude Sonnet 5.5 (`claude-sonnet-5-5`) · üretici: Claude Opus 5.5 (`claude-opus-5-5`) → FARKLI (juri-olcutleri §1e sağlandı).

# YVJ-0210I — simple-past-ileri YouTube yayın verisi çıktı jürisi · 15.11.2026

## Özet

| Sonuç | Sayı |
|---|---|
| evet (geçti) | 15 |
| hayır | 0 |
| kanıt yok (kaldı) | 2 |

Bakılan çıktı: `youtube.json`, `youtube-aciklama.md` (ana + dikey paket), `zaman.json`, `ortak/anlatim/METIN.md` + `sozcukler.json` + `altyazi.json`, `kapak.png`
(görüldü), katalog (`varlik/grammar/katalog.json`, `konu-adlari.json`), `ortak/youtube/bildirim/yer.json`.
Pakette `senaryo.json`, `baslar.json`, `cikti.mp4`, Whisper dökümü YOK; senaryo yerine `METIN.md` (cümle başlar/biter) kullanıldı.
Ölçümler kendi komutlarımla: başlık 27 karakter · açıklama 699 bayt · etiket 61 ham / 67 virgüllü karakter · bölüm süreleri 13,47 / 19,68 / 15,84 / 17,20 / 25,35 sn
(son bölüm = 91,54 − 66,19) · dikey `youtube.json` ana ile `diff` farksız; dikey açıklama farkı yalnız `utm_content` (`dikey-tam`) · dikey `zaman.json` yalnız genişlik/yükseklikte farklı.

## Madde tablosu (§2f)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | "Simple Past \| YDT İngilizce" = 27 karakter ≤ 100; kalıp `<Konu> \| <kitle> İngilizce` | **Uyarı (madde dışı):** `simple-past-temel/youtube.json` başlığı BİREBİR aynı. Kalıpta seviye yok; kanalda iki aynı başlık. Öneri aşağıda (Ö-1) |
| YV-2 | evet | 699 bayt ≤ 5.000; sıra: değer cümlesi → "Sınav günü bakmak için kaydet." → "Bölümler:" + 5 damga → "Sıradaki ders" → "Ders sayfası" (utm) → 5 hashtag. Dil: yazım ve ek uyumu hatasız | utm_campaign büyük harf (`ING-YDT-GR-02-10-I`), katalog `kod` ile aynı |
| YV-3 | evet | ilk damga 00:00; 5 bölüm; en kısa bölüm 13,47 sn ≥ 10. Damgalar `zaman.json` sahne başları: 13,47→00:13 · 33,15→00:33 · 48,99→00:49 · 66,19→01:06; açıklama damgaları bunlarla birebir | Yuvarlama en çok 0,47 sn önceye düşer; o aralık sessiz/geçiş (cümle 2 biter 12,92; cümle 3 biter 32,60; cümle 5 biter 65,64): bölüm başı kesilmez |
| YV-4 | evet | 5 ad da izleyici dilinde, iç ad yok. İçerik denetimi (`METIN.md`): B1 = cümle 1–2 (tanım "A finished action at a definite time in the past") · B2 = cümle 3 (in 1911; begin–began–begun) · B3 = cümle 4 (used to / would; "durum: yalnız used to" kapakla da tutarlı) · B4 = cümle 5 (resigned two weeks ago … yet aynı cümlede ✓) · B5 = cümle 6–7 (öğrenci sorusu + "Olmaz") | B3 adı soru biçimidir; cevap derste var (would live yanlış → durumu yalnız used to taşır) |
| YV-5 | evet | toplam 61 karakter (YouTube sayımıyla ≈ 73) ≤ 500; konu "Simple Past", zaman adı "Present Perfect"/"geçmiş zaman", kitle "YDT", "İngilizce", "gramer" var; yineleme yok | "ileri" tek başına arama değeri düşük; madde dışı |
| YV-6 | evet | Gönderi: "ago … Present Perfect ile kullanılmaz; doğrusu resigned" — standart İngilizcede doğru. Açıklama değer cümlesi, bölüm adları, sabit yorum: mutlak kural, yanlış denklik ya da doğru cümleyi yanlış gösterme yok. Yazım hatası yok | Ana ders notları D-1 … D-3 aşağıda (§1c gereği raporlanır; yayın metinlerinde yansıması yok) |
| YV-7 | evet | katalog GR-02-10 `sira` 10 ✓; `videolar` içinde `02-10-ydt-ileri` ✓ (`proje: simple-past-ileri`); `02-09-ydt-ileri` ve `02-11-ydt-ileri` katalogda var; ünite "Tenses", seviye "İleri", kitle "YDT" → "Tenses · YDT İleri" ✓. "Past Continuous" = `konu-adlari.json` GR-02-11 ✓ | 02-11 durumu `planli`: bağlantı yüklenene kadar boş (standart §4 kapsamında) |
| YV-8 | evet | `altyazi.json` 21 satır; son `t1` 90,62 ≤ ders süresi 91,54 | srt panelde türetilir |
| YV-9 | evet | `gorsel: "kapak.png"`; ana 1920×1080, dikey 1080×1920 (`file`); kare görüldü: sarı açık tema kapak, kanal adı + "YDT · İLERİ". Gönderi metninde emoji yok | **Not (madde dışı):** kapak "USED TO mu WOULD mu?" diyor, gönderi metni ago/Present Perfect ile açılıyor; görsel ile ilk cümle farklı konu. Ö-2 |

## Bildirim kuralları (`youtube-surumu-standart.md` §3, madde YT-3)

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı (ders 91,54 sn < 4 dk → 1) | evet | `bildirimler` 1 satır |
| Zaman ≈ %30, cümle sınırı | evet | 33,15 sn = %36,2; `METIN.md` cümle 4 başlar 33,15; 30 sn sonrası ilk cümle başı bu. Cümle 3 biter 32,60 (ara 0,55 sn) |
| Ses yok | evet | kayıt `sure` dışında ses alanı yok |
| İlk 30 sn / son 20 sn dışı | evet | 33,15–36,15; son 20 sn sınırı 71,54 |
| Yer = `yer.json` ölçümü (yatay sol alt x240 y900 520×140; sağ alt değil) | evet | `youtube.json` kendi yerini taşımaz; tek kaynak `yer.json` |
| Yer çakışması: künye, altyazı, sahne öğesi (yatay) | **kanıt yok** | `cikti.mp4` yok; `ortak/youtube/bildirim/ders/` altında bu ders için kare yok (yalnız 02-04 ve simple-present). 33,15 sahne 3→4 BookFlip bitişine denk gelir; kartın 33,15'te başlaması geçişle çakışmaz (geçiş 32,75–33,15) ama sahne 4 ilk karelerinde alanın boş olduğu görülmedi |
| Dikeyde yer (ayrıca ölçülür) | **kanıt yok** | `ortak/youtube/dikey/bildirim/` altında yalnız `simple-present-temel-dikey` ölçümü var; `yer.json` yok, bu ders için dikey ölçüm yok |

## Kaldı maddeleri ve düzeltme önerisi

| Kimlik | Düzeltme |
|---|---|
| YT-3 yer çakışması (yatay) | Görsel jüri (G) 33,15–36,15 aralığında sahne 4'ten en az 3 kare alsın; kart 520×140 sol alt bölgenin boş olduğunu pikselle doğrulasın. mp4 yoksa kare `kare.mjs` ile sahneden alınır |
| YT-3 dikey yer | Dikey paket için `ortak/youtube/dikey/bildirim/olcum/simple-past-ileri-dikey` ölçümü koşsun (HUD %15 bandı dışı); sonuç `yer.json` dikey karşılığına yazılsın |

## Madde dışı öneriler (şef kararı; hüküm değiştirmez)

- **Ö-1 (YV-1):** kalıp seviyesiz olduğu için temel ve ileri başlığı aynı kalıyor. Önerilen yeni başlık: "Simple Past: Ago, Used to, Would | YDT İngilizce" (≤ 100; konu ve kitle korunur; kalıp `<Konu> | <kitle> İngilizce` bozulmaz). Kalıba seviye eklemek ise sözleşme değişikliğidir.
- **Ö-2 (YV-9):** gönderi ilk cümlesini kapakla eşle: "Used to mu would mu? Durum anlatan yalnız used to; ago varken de has resigned yazılmaz, doğrusu resigned."
- **Ö-3:** açıklamadaki damgalar ders zamanıdır; mp4'e 3 sn giriş klibi eklenince YouTube zamanı +3 sn kayar. Standart §2/§3 API'nin damgaları yeniden yazdığını söylüyor; panel testi bunu doğrulamalı (jüri bu paketten ölçemedi).

## Ana ders notları (§1c, yayın verisine girmedi; dil jürisi ana derse bakar)

| # | Cümle | Sorun | Öneri |
|---|---|---|---|
| D-1 | cümle 1 "Ago varsa Perfect yok." ve cümle 7 son kod "ago varsa Past" | Mutlak biçim: Past Perfect, aktarılan sözde ago ile kullanılabilir ("She said she had left two years ago") | Cümle "Ago varsa Present Perfect yok." olsun ("Perfect" belirsiz) |
| D-2 | cümle 7 "Present Perfect for, since, yet ister." | Zorunluluk gibi okunur; Present Perfect bu sözcükler olmadan da kurulur | "… for, since, yet ile sık kullanılır." |
| D-3 | cümle 7 "since varsa Perfect" | since yan cümlesi çoğu zaman Simple Past alır ("since I moved here") | "since + zaman noktası varsa ana cümle Perfect" |

Bu üç not mevcut ses kaydını değiştirir; ses yeniden üretimi ayrı karar (bu jüri ses üretmez).

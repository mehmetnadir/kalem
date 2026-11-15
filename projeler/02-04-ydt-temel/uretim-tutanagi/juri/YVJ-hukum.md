# YVJ-0204T — `02-04-ydt-temel` YouTube yayın verisi ÇIKTI jürisi · 15.11.2026

Jüri modeli: Claude Sonnet 5.5 (`claude-sonnet-5-5`). Üretici model: Claude Opus 5.5 (`YV-RAPOR.md` satır 10). Model farklı, aile aynı (`juri-olcutleri.md` §1e açık noktası sürer).
Kapsam: `youtube.json`, `youtube-aciklama.md`, dikey paket eşleri, `zaman.json`, `ortak/anlatim/{METIN.md, baslar.json, altyazi.json}`, katalog (`dijital-anlatim/varlik/grammar/katalog.json`, `konu-adlari.json`), `kapak.png`, `cikti.mp4`.
Hiçbir üretim dosyası değiştirilmedi. Sayıları kendim ölçtüm (python `-I`, `ffprobe`, `ffmpeg` kare farkı).

## Özet

| Sonuç | Sayı | Kimlikler |
|---|---|---|
| Geçti (evet) | 12 | YV-1 … YV-7, YV-9; §3 sayı, zaman, cümle sınırı, ilk 30 sn / son 20 sn |
| Kaldı (hayır) | 1 | §3 Yer (sağ üst) |
| Kanıt yok (= kaldı) | 4 | YV-8; §3 Ses (sessiz); dikey bildirim yeri; giriş kaymasının açıklamaya yansıması |

## Madde tablosu

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | başlık 52 karakter (≤ 100). `Simple Present ve Present Continuous \| YDT İngilizce` = `<Konu> \| <kitle> İngilizce` | — |
| YV-2 | evet | 972 bayt (916 karakter; ≤ 5.000). Sıra: değer cümlesi (satır 1) → kaydet satırı → `Bölümler:` damgaları → `Sıradaki ders` → bağlantı (utm) → etiket satırı | İlk satır 159 karakter; YouTube "daha fazla" öncesi yaklaşık ilk 100–120 karakteri gösterir, değer cümlesi bölünebilir. Kural ihlali değil, not. |
| YV-3 | evet | ilk damga 00:00; 13 bölüm (≥ 3); en kısa bölüm 13,37 sn, sonraki 14,89 sn (≥ 10). `youtube.json` `bolumler[].t` 13/13 `zaman.json` `t_bas` ile aynı. 13/13 damga `round(t)` ile `youtube.json` ile aynı | 3 damga yukarı yuvarlanmış (00:44 ← 43,85; 01:09 ← 68,84; 03:04 ← 183,79). Konuşma sonraki sınırda başlar (44,40 · 69,39 · 184,54), içerik kaçmaz. Giriş kayması için aşağıdaki "Ek" satırına bak. |
| YV-4 | evet | 13 bölüm adı `METIN.md` ile eşleştirildi, hepsi izleyici dilinde ve bölümün içeriğini söylüyor. Örnekler: 20,22–43,85 `wear` (cümle 3: coat / pink T-shirt); 43,85–68,84 `live` (cümle 4); 93,35–113,37 tren sorusu (cümle 6–7: öğrenci sorar, öğretmen tarife/plan ayırır); 130,40–145,29 ve 145,29–162,33 `today` iki cümlesi (cümle 9, 10); 162,33–183,79 `-yor` tuzağı (cümle 11–12); 183,79–205,30 `I live` ↔ `I am living` (cümle 13) | "Mini soru: boşluğa hangi şık?" (220,33–251,27) cevap açıklamasını da kapsar; ad soruyu söylüyor, kaldı sayılmaz. |
| YV-5 | evet | 9 etiket, toplam 115 karakter (virgüllü 123; tırnaklı en kötü sayım 133; ≤ 500). Konu (`Simple Present`, `Present Continuous`), zaman adı (`geniş zaman`, `şimdiki zaman`), kitle (`YDT`), `İngilizce`, `gramer` var | — |
| YV-6 | evet | Başlık, açıklama, sabit yorum, gönderi ve bölüm adlarındaki her dilbilgisi iddiası `METIN.md` ve gramer bilgisiyle ayrı ayrı doğrulandı: "üç kullanım farkı" (genel/an · kalıcı/geçici · tarife/plan) doğru; "Türkçede ikisi de yaşıyorum" doğru; `I live in Istanbul` kalıcı, `I am living with my uncle` geçici doğru; "Türkçedeki -yor eki" tuzağı doğru. Mutlak kural, yanlış denklik, doğru cümleyi yanlış gösterme yok. Yazım hatası yok; yasak sözcük taraması (`Tam ders`, `dakika`, `dk`, `BASIC`) boş | — |
| YV-7 | evet | katalog: `GR-02-04`, `sira` 4; önceki `02-03-ydt-temel`, sonraki `02-05-ydt-temel` (üçü de katalogda). Liste adı `Tenses · YDT Temel` = `<Ünite> · <kitle> <seviye>` (`uniteler[1].ad` = Tenses). `konu-adlari.json` GR-02-05 = "Simple Present vs Present Continuous: Stative Verbs" (güven yüksek); açıklamadaki "Stative Verbs" bunun alt başlığı, anlatımın son cümlesi ("-ing almayan fiilleri görüyoruz") ile uyumlu | Sıradaki ders adının kısa mı tam mı yazılacağı sözleşmede yok; kısa ad kabul. |
| YV-8 | kanıt yok | `altyazi.json` var (son satır t1 = 264,22 sn ≤ ders 264,64 sn ve ≤ mp4 265,68 sn). `altyazi.srt` pakette yok; sözleşme §2 "panel türetir" der, türetme betiği depoda yok (`altyazi.srt` taraması yalnız YV-RAPOR dosyalarında çıktı) | İki dosya karşılaştırılamadı. |
| YV-9 | evet | `gonderiler[0].gorsel` = `kapak.png`, pakette var; ortalama parlaklık 173 (`kapak-koyu.png` 80); görsel açık tema sarı kapak, "HER ZAMAN mı ŞİMDİ mi?" ile içerik uyumlu. Gönderi metninde ve `youtube.json` içinde emoji yok (Unicode `So` taraması boş) | — |

## `youtube-surumu-standart.md` §3 bildirim kuralları

| Kural | Hüküm | Kanıt | Not |
|---|---|---|---|
| Sayı | evet | ders 264,64 sn ≥ 240 sn → 2 bildirim; `youtube.json` 2 satır | — |
| Zaman (≈ %30 / %70) | evet | 69,39 sn = %26,2 · 184,54 sn = %69,7 | 1. bildirim hedeften 10 sn erken (%30 = 79,4 sn). Cümle sınırı kuralı için `baslar.json` sınırı olan 69,39 en yakın sınırdır (öteki 93,90). `METIN.md` cümle 5 içinde gerçek bir cümle başı 79,53 sn'de ("Kalkış saati…") vardır; `baslar.json` birimi değil. Kural metnine göre geçer, tolerans yazılmamış. |
| Cümle sınırı | evet | iki `t` değeri `baslar.json` cümle 5 ve cümle 13 başlangıcıyla birebir | — |
| İlk 30 sn / son 20 sn yok | evet | 69,39 > 30; 187,54 < 244,64 (= 264,64 − 20) | — |
| Yer: sağ üst | **hayır** | `cikti.mp4` 6 karede (69,6 · 71 · 72,2 · 184,8 · 186,2 · 187,4 sn) `zemin-acik.png` ile fark: sağ üst kutuda (1156,40 · 520×140 + 16 px pay) 5 karede 2.351–2.468 px dolu; sol alt kutuda (240,900) 0 px. `ortak/youtube/bildirim/yer.json` = `sol_alt` | Üretim kartı sol alta koymuş; `RAPOR.md` §5 sapmayı kayda almış, "karar Nadir'de". Kart çakışmıyor ama standart "sağ üst" diyor. Sapma onaylanana kadar kaldı. Ek ölçüm: kart girişinde (69,4 sn) kutuda 30.676 px fark var (BookFlip geçişinin son kareleri; 69,8 sn'den sonra 0). Kart 0,3 sn bir geçişin üstüne biner, okunmayı bozmaz. |
| Ses yok | kanıt yok | `youtube.json` ses alanı taşımaz; kart PNG sessiz; birleştirilmiş `youtube.mp4` henüz yok | mp4 üretilince `ffprobe` ile bildirim aralıklarının ses enerjisi ölçülmeli. |

## Ek (YV kimliği olmayan, jüri bulgusu)

| Konu | Hüküm | Kanıt | Not |
|---|---|---|---|
| Giriş kaymasının açıklamaya yansıması | kanıt yok | `RAPOR.md` §7 ve sözleşme §2: giriş klibi (3,00 sn) damgaları kaydırır. `youtube-aciklama.md` ders zamanıyla yazılı, kayma uygulanmamış; kaydıran araç ya da adım depoda görünmüyor | Olduğu gibi yüklenirse her damga 3 sn erken düşer (00:44 ← gerçek 00:47). |
| Dikey paket bildirim yeri | kanıt yok | `02-04-ydt-temel-dikey/youtube.json` yatay dosyayla birebir aynı (bildirim zamanı, gönderi, liste); standart §6 "dikeyde yer ayrıca ölçülür" der, ölçüm yok | `utm_content` doğru ayrılmış (`ana-yatay` / `dikey-tam`, `surumler.json` kimlikleriyle uyumlu). `utm_campaign=ING-YDT-GR-02-04-T` = `surumler.json` `kod`. |
| Kanal sabitleri | kanıt yok | sözleşme §2 `kalem/ortak/youtube/kanal.json` ister; dosya yok | YV-1…9 kapsamı dışı, bilgi. |

## Kaldı maddeleri için düzeltme önerisi (her biri tek cümle)

| Kimlik | Öneri |
|---|---|
| YV-8 | `altyazi.json` → `altyazi.srt` türetme ve karşılaştırma betiğini yaz ya da ölçütü "`altyazi.json` son satır t1 (264,22) ders süresini (264,64) aşmaz" biçimine daralt. |
| §3 Yer | Nadir sapmayı onaylarsa standart §2 ve §3 "sağ üst" yerine "sol alt (240, 900), sağ üstte içerik varken" olarak güncellensin; onaylamazsa kart sağ üstün boş kalacağı anlara taşınsın. |
| §3 Ses | `youtube.mp4` üretildikten sonra 69,39–72,39 ve 184,54–187,54 sn (+ giriş 3,00 sn) aralıklarında ses enerjisinin yalnız ders sesi olduğunu `ffprobe`/enerji ölçümüyle kanıtla. |
| Giriş kayması | `youtube-aciklama.md` damgalarını yüklemeden önce +3,00 sn kaydır: `00:00 · 00:23 · 00:47 · 01:12 · 01:36 · 01:56 · 02:13 · 02:28 · 02:45 · 03:07 · 03:28 · 03:43 · 04:14` (sırasıyla 13 bölüm). |
| Dikey yer | Dikey `youtube.mp4` için kart yerini ayrıca ölç ve `youtube.json` dikey kopyasına yaz. |

juri_model: Claude Sonnet 5.5 (`claude-sonnet-5-5`)
uretici_model: Claude Opus 5.5 (`claude-opus-5-5`) — kaynak `YV-RAPOR.md`. Aynı aile (Claude), farklı model; büyük harfle uyarı gerekmez.

# YVJ-0201I — present-continuous-ileri YouTube yayın verisi ÇIKTI jürisi · 15.11.2026

## Özet

| Küme | Geçti | Kaldı | Kanıt yok |
|---|---|---|---|
| §2f YV-1 … YV-9 | 8 | 1 (YV-6) | 0 |
| YT §3 bildirim kuralları (6 madde) | 4 | 0 | 2 (yer, ses) |
| Toplam | 12 | 1 | 2 |

Bakılan çıktı: `youtube.json`, `youtube-aciklama.md` (ana + dikey), `ortak/anlatim/senaryo.json`, `altyazi.json`, `zaman.json`, `anlatim.wav`,
`kapak.png` (Read ile görüldü), `katalog.json`, `katalog-durum.json`, `konu-adlari.json`, emsal `present-continuous/youtube*`.
Hiçbir üretim dosyası değiştirilmedi. Sayılar jüri tarafından ölçüldü (`/usr/bin/python3 -I`, salt okuma).

## Kendi ölçümüm

| Ölçüm | Değer |
|---|---|
| Başlık | 34 karakter |
| Açıklama | 587 bayt (558 karakter), ana ve dikey; tek fark `utm_content` (`ana-yatay` / `dikey-tam`) |
| `youtube.json` ana ↔ dikey | birebir eşit |
| Etiket | 6 etiket, ham 54 karakter, YouTube sayımı 63 |
| Emoji (`So` kategorisi) | açıklama, sabit yorum, gönderi: 0 |
| `anlatim.wav` süresi | 84,96 sn = `zaman.json` son `t_son` |
| `altyazi.json` son `t1` | 83,96 sn (≤ 84,96) |
| Bölüm süreleri | 15,25 · 14,33 · 12,49 · 12,01 · 30,88 sn (hepsi ≥ 10) |
| Bölüm damgaları | 00:00 · 00:15 · 00:30 · 00:42 · 00:54 (yuvarlama sahne başlarıyla tutarlı) |
| Sahne sınırları ana ↔ dikey `zaman.json` | 6 sahnenin `t_bas`/`t_son` aynı |
| Bildirim | `t` 30,13 sn, 3,0 sn; ders payı %35,5; önceki cümle 29,66'da biter |

## Madde tablosu — §2f

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | 34 ≤ 100; kalıp `<Konu> \| YDT İngilizce`; konu `senaryo.json` `baslik` ve `konu-adlari.json` GR-02-01 ile aynı | **Şefe çıkar (madde dışı):** temel pakette de başlık harfi harfine aynı ("Present Continuous \| YDT İngilizce"; `present-continuous/youtube.json`). Aynı kanalda iki video aynı başlığı alır. Kalıp seviye içermez, kural ihlali yok; karar sözleşmede |
| YV-2 | evet | sıra: değer cümlesi (78 kr) → kaydet satırı → "Bölümler:" + 5 damga → "Sıradaki ders" → "Ders sayfası" (utm) → hashtag satırı; 587 ≤ 5.000 bayt | utm_campaign `ING-YDT-GR-02-01-I` büyük harf, `meta.kod` ile aynı; temel paket `-T` ile tutarlı |
| YV-3 | evet | ilk damga 00:00; 5 bölüm; en kısa bölüm 12,01 sn; her `t` bir sahne `t_bas` değeri (0, 15,25, 29,58, 42,07, 54,08) | 29,58 → 00:30: YouTube'da cümle 3 biter (29,66), sessizlik, 30,13'te "İkinci kök." başlar; kayma zararsız |
| YV-4 | evet | 5 ad senaryoyla eşleşti: "Formül" = cümle 2; "is sleeping" = cümle 3 ("İki iş de şu anda sürüyor"); "this week" = cümle 4 ("Geçici bir durum. This week bunu söyler."); "tomorrow morning" = cümle 5 ("Planlı gelecek"); "Tuzak…" = cümle 6–7 (know/believe/own, He is always losing his keys). İç ad ("Örnek", "Kanca", "Soru + Form") yok | Not: ders "tuzak" sözcüğünü yalnız durum fiili için kullanır (cümle 1, 2); `always + -ing` için "Sınavda ikisi de çıkar" der. Bölüm adı ikisini "Tuzak" altında toplar; yanlış değil, ama dersin sözünden biraz geniş |
| YV-5 | evet | toplam 54 kr (YouTube sayımı 63) ≤ 500; konu "Present Continuous", zaman adı "şimdiki zaman" (`konu-adlari.json` kanıtı: "Present continuous tense şimdiki zaman"), kitle "YDT", "İngilizce", "gramer" | "ileri" arama değeri düşük, kural ihlali değil. Temel paketin 13 etiketine göre ileri 6 etiketle dar |
| **YV-6** | **hayır** | Açıklama 1. satırı: "Present Continuous'**u** …". "Continuous" okunuşu /kənˈtɪnjuəs/; yabancı sözcükte ek okunuşa uyar, son ünlü ı/ə → belirtme eki "'ı". Emsal temel paket: "Present Continuous'**ı** üç örnekle öğren". Aynı kanal, aynı konu adı, iki farklı ek: yazım hatası + paketler arası tutarsızlık (`juri-olcutleri.md` §1d) | Düzeltme önerisi aşağıda. Diğer dilbilgisi iddiaları aşağıdaki tabloda doğru |
| YV-7 | evet | `katalog.json`: ünite 02 "Tenses", GR-02-01 `sira` 1; `liste` "Tenses · YDT İleri" (temel emsali "Tenses · YDT Temel"); `onceki` null (ünitenin ilk konusu); `sonraki` `02-02-ydt-ileri` katalogda var (`katalog-durum.json`: uretimde); "Sıradaki ders: Simple Present" = GR-02-02 `konu-adlari.json` | `sonraki` videosu henüz yüklenmedi; bitiş ekranı bağı yüklemeye kadar boş (YV-RAPOR'da bildirilmiş) |
| YV-8 | evet | son `t1` 83,96 ≤ ders süresi 84,96 (`zaman.json` ve `anlatim.wav` ölçümü aynı) | pakette srt yok (panel türetir, sözleşme §2) |
| YV-9 | evet | `gorsel` = `kapak.png`; dosya iki pakette var (1920×1080 ve 1080×1920, `file`); görüldü: sarı açık tema kapağı, "KNOWING? OLMAZ!" gönderi sorusuyla aynı konu; emoji 0 | **Not (YV-9 dışı):** `KAPAK-RAPOR.md` açık kalan (a): `karakter.png` kol ile gövde arasında opak beyaz üçgen; kapakta sağ altta görüldü (x≈1480–1530, y≈860–930). Gönderi görseli olarak yayınlanırsa görünür kusur |

## Dilbilgisi iddiaları — bağımsız doğrulama (YV-6 kapsamı)

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama satır 1 | ders Present Continuous'u üç sınav köküyle gösterir, durum fiili tuzağını tanıtır | içerik doğru (üç kök: cümle 3–5; tuzak: cümle 6–7); **ek yanlış** (yukarıda) |
| Sabit yorum | kaydet teşviki + damgalara yönlendirme; tek cümle (1 nokta, 1 noktalı virgül) | doğru; iddia yok |
| Gönderi, 1. cümle | "Biliyorum için I am knowing denir mi?" | doğru; yazım notu: "Biliyorum" ve "I am knowing" tırnaksız. Tırnak önerilir (zorunlu değil) |
| Gönderi, 2. cümle | "Denmez: know bir durum fiili, doğrusu I know the answer." | doğru. Kapsam "biliyorum" anlamıyla sınırlı; standart İngilizcede "I am knowing the answer" kabul edilmez. Mutlak kural dili yok |
| Gönderi, 3. cümle | ders özeti | doğru |
| Bölüm adları | formül, is sleeping, this week, tomorrow morning | doğru (`am / is / are + verb-ing` dersin söylediği biçim) |

## Ana ders gözlemi (`juri-olcutleri.md` §1c; YV metinlerine taşınmamış, ana derste duruyor)

| Cümle | Metin | Sorun |
|---|---|---|
| 3 | "While, tam anı gösterir." | belirsiz; while eşzamanlı süreci bağlar ("-ken"), "tam an" doğru terim değil |
| 7 | "Know, believe, own, belong durum fiilidir, -ing almaz." / "Kod: olay -ing alır, durum almaz." | mutlak; think ("I am thinking about it") ve have ("I am having lunch") eylem anlamında -ing alır. Sınav düzeyi için basitleştirme |
| 7 | "Always artı -ing şikâyettir." | mutlak; "She is always helping people" olumlu bağlamda da geçer. "genellikle şikâyettir" daha doğru |

Bu üç satır YV kimliği altında kaldı sayılmadı (ders çıktısı, YV kapsamı dışı); ders jürisine aktarılmalı.

## YT §3 bildirim kuralları (`youtube-surumu-standart.md`)

| Kimlik | Madde | Hüküm | Kanıt |
|---|---|---|---|
| B-1 | Sayı: ders < 4 dk ise 1 | evet | ders 84,96 sn; `bildirimler` 1 satır |
| B-2 | Zaman: ≈ %30, ilk bilgiden sonra | evet | 30,13 sn = %35,5; izinli pencere [30,00 · 64,96] içindeki en erken cümle başı (YV-RAPOR'daki tablo `altyazi.json` ile yeniden hesaplandı: 30,13 · 42,62 · 54,63 · 60,40); formül + 1. kök anlatılmış |
| B-3 | Cümle sınırı, söz ortasında değil | evet | 30,13 = cümle 4 `t0` (önceki cümle 29,66 biter); pakette `baslar.json` yok, `altyazi.json` ilk `t0` ile türetildi (YV-RAPOR yöntemi, pilotta sınanmış) |
| B-4 | Yer: künye, altyazı, sahne öğesiyle çakışmaz; dikey ayrıca ölçülür | **kanıt yok** | pakette mp4 yok; sahne 4 ("Örnek 2") için kare yok (yalnız 01 ve 90 sahnelerinin kareleri var); dikey `youtube.json` yataydan farksız, dikey yer ölçümü yok |
| B-5 | Ses yok, efekt sesi yok | **kanıt yok** | mp4 yok; veride ses alanı yok. Render sonrası denetlenir (YT kapısı 2) |
| B-6 | İlk 30 sn ve son 20 sn bildirim yok | evet | kart 30,13–33,13 sn; son 20 sn sınırı 64,96 sn; giriş klibi (3 sn) eklense de 33,13–36,13, kural bozulmaz |

B-4 ve B-5 metin kusuru değil, render bağımlıdır; mp4 üretilince görsel jüri bunları kapatır.

## Kaldı maddeleri ve düzeltme önerisi

| Kimlik | Tek cümle | Önerilen yeni metin |
|---|---|---|
| YV-6 | Açıklama 1. satırdaki "Present Continuous'u" eki okunuşa aykırıdır ve temel paketle ("'ı") tutarsızdır. | `youtube-aciklama.md` (ana + dikey) satır 1: "Present Continuous'ı üç sınav köküyle görürsün; durum fiili tuzağını tanırsın." |
| B-4 | Kart yeri mp4 ve kare olmadan ölçülemez. | mp4 sonrası: sahne 4 karesi (t=30,13–33,13) ve dikey karesi ile `yer.json` çakışma ölçümü |
| B-5 | Ses yokluğu mp4 olmadan doğrulanamaz. | mp4 sonrası: bildirim aralığında ses iz denetimi |

Şefe çıkarılan (kural dışı, karar gerektirir): (1) temel ve ileri paketin başlığı aynı; (2) ana dersteki 3 mutlak/belirsiz ifade ders jürisine.

Son Güncelleme: 15.11.2026 — ilk sürüm (YVJ-0201I; jüri Sonnet 5.5).

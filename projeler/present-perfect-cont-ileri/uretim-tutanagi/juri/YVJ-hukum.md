# YVJ-0209I — `present-perfect-cont-ileri` YouTube yayın verisi çıktı jürisi · 15.11.2026

**Jüri modeli: Claude Sonnet 5.5** (`claude-sonnet-5-5`). Üretici: Claude Opus 5.5. Model farklı, aile aynı (juri-olcutleri §1e açık nokta: tek aile riski sürer).
Jüri hiçbir üretim dosyasını değiştirmedi. Sayılar jüri tarafından `youtube.json`, `youtube-aciklama.md`, `zaman.json`, `altyazi.json`,
`sozcukler.json`, `katalog.json` dosyalarından yeniden ölçüldü.

## Özet

| Sonuç | Sayı |
|---|---|
| Geçti (evet) | 9 / 9 YV + 5 / 5 bildirim kuralı |
| Kaldı (hayır) | 0 |
| Kanıt yok | 0 madde (1 kapsam dışı not: bildirim yeri ve çakışma, mp4 ve kare yok; YT-3 video jürisinde) |

Dikey paket: `youtube.json` ana paketle bayt bayt aynı (`cmp` farksız). `youtube-aciklama.md` farkı yalnız `utm_content=dikey-tam`.
`zaman.json` farkı yalnız `genislik`/`yukseklik`. Dikeyin `ortak/anlatim` dizini ana paketin anlatımına bağdır.

## YV maddeleri

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | başlık 42 karakter (≤ 100); kalıp `<Konu> \| YDT İngilizce`; konu = `senaryo.json` `baslik` "Present Perfect Continuous", kitle "YDT" | — |
| YV-2 | evet | 712 bayt (≤ 5.000), 15 satır. Sıra: değer cümlesi → kaydet satırı → Bölümler (5 damga) → Sıradaki ders → Ders sayfası (utm) → etiket satırı | utm: `utm_campaign=ING-YDT-GR-02-09-I` büyük harf, `utm_content` yatayda `ana-yatay`, dikeyde `dikey-tam`; emsal 02-04 ve 02-10 ile aynı kalıp. Adresin canlılığı ölçülemedi (ağ yok); YV-2 kapsamı dışı |
| YV-3 | evet | ilk damga 00:00; 5 bölüm; süreler (`zaman.json`) 17,25 · 16,43 · 15,52 · 12,67 · 24,06 sn, en kısa 12,67 (≥ 10); her `t` bir sahne `t_bas` değeri; açıklama damgaları `youtube.json` `t` değerlerinin en yakın saniyeye yuvarlanmışı (00:00, 00:17, 00:34, 00:49, 01:02) | 00:49 damgası cümle 4'ün son sözüne ("finished.", 48,56–49,20) düşer; bölüm başı için sorun değil (bildirim kuralı değil), kayıt için yazıldı |
| YV-4 | evet | senaryo ile bölüm adları eşleşti. B1 "Süreç mi, sonuç mu? have been + -ing" = cümle 1–2 (soru + kural). B2 "Since cümlesi: have been complaining" = cümle 3. B3 "Süreç ve sonuç: reading, finished" = cümle 4. B4 "Durum fiili know: have known" = cümle 5. B5 "Have been knowing olur mu? Özet" = cümle 6 (öğrenci sorusu) + 7 (cevap ve özet) | iç ad yok ("Giriş", "Örnek 1" vb.); ad uzunluğu 28–36 karakter |
| YV-5 | evet | 7 etiket, ham 78 karakter, YouTube sayımıyla 91 (≤ 500); yineleme yok; konu, zaman adları ("Present Perfect Continuous", "Present Perfect"), kitle "YDT", "İngilizce", "gramer" var | "ileri" arama değeri düşük genel sözcük; yönergeye aykırı değil |
| YV-6 | evet | bütün iddialar senaryo ve dilbilgisi bilgisiyle denetlendi (aşağıdaki tablo) | tek not: sabit yorumdaki "süreç ile sonuç farkına … doğrudan geç" ifadesi yerleşik Türkçe değil (öneri aşağıda); yazım hatası ve emoji yok |
| YV-7 | evet | `katalog.json` GR-02 "Tenses" (sira 2), konu GR-02-09 sira 9 = `liste.sira` 9; liste adı `Tenses · YDT İleri`; önceki `02-08-ydt-ileri` (katalogda var, durum planli); sonraki `02-10-ydt-ileri` (proje `simple-past-ileri`, `surumler.json` konu "Simple Past"); "Sıradaki ders: Simple Past" doğru; `simple-past-ileri/youtube.json` `onceki` = `02-09-ydt-ileri` (çift yönlü tutarlı) | Önceki ders yüklenene kadar bağ boş kalır (üretici notu doğru) |
| YV-8 | evet | `altyazi.json` 26 satır; ilk `t0` 1,00; son `t1` 85,01 ≤ ders süresi 85,93 (`zaman.json` son `t_son`) | srt pakette yok (tasarım gereği, panel türetir) |
| YV-9 | evet | `gorsel` = `kapak.png`; ana pakette 1920×1080, dikey pakette 1080×1920; jüri ana kapağı gözle okudu: sarı açık zemin, "SÜREÇ mi SONUÇ mu?", rozet "YDT · İLERİ" (koyu tema değil); gönderi, sabit yorum, açıklama ve `youtube.json` metinlerinde emoji yok (regex taraması boş) | Dikey pakette aynı ad dikey kapağı gösterir; topluluk gönderisinde hangisinin kullanılacağı panel kararı |

## YV-6 dilbilgisi iddiaları (jüri bağımsız doğrulaması)

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama satır 1 | kalıp have/has been + -ing; been -ing süreci, have + üçüncü hâl sonucu anlatır | doğru; mutlak kural sözü yok ("ayırırsın" dersin çerçevesi) |
| Bölüm adları (5) | kalıp, since'li örnek, süreç/sonuç, durum fiili know + have known, soru | doğru; genelleme yok |
| Gönderi, 2. cümle | süreç have been reading ile, sayıyla verilen sonuç have finished ile söylenir | doğru (sayı/miktar → Present Perfect basit; yerleşik ölçüt); "her zaman" türü sözcük yok |
| Gönderi, 1. ve 3. cümle | soru; derste since ipucu ve durum fiili tuzağı var | doğru (senaryo cümle 3, 5–7) |
| Sabit yorum | iddia yok | doğru |
| Etiket "Present Perfect" | have + üçüncü hâl = Present Perfect | doğru; derste ad geçmez ama kavram anlatılır |

Kapsam dışı gözlem (YV metinlerine girmedi, dil jürisine): senaryo cümle 5 ve 7 "Durum fiili -ing almaz" mutlak ifade; durum fiillerinin eylem anlamlı
kullanımı -ing alabilir ("I have been thinking about it"). Cümle 3 "Ana cümlede have been ve -ing gelir" since + geçmiş yan cümle için mutlak
okunabilir; dersin 3. örneği ("have known … since") bunu zaten çürütür. İkisi de YV kapısına değil, ders senaryosuna (HV/EK) aittir.

## Bildirim kuralları (`youtube-surumu-standart.md` §3)

| Kural | Hüküm | Kanıt | Not |
|---|---|---|---|
| Sayı: ders < 4 dk → 1 | evet | ders 85,93 sn; `bildirimler` 1 satır | — |
| Zaman ≈ %30 | evet (sapma kayıtlı) | t = 34,23 sn = %39,8. İlk 30 sn yasağı %30 hedefini (25,78 sn) kapatır; 30 sn sonrası ilk cümle başı 34,23 | Daha yakın uygun cümle başı yok: 17,80 (ilk 30 sn içinde), 49,75 (%57,9). Standarda "< 100 sn derste ilk 30 sn yasağı önceliklidir" cümlesi gerekir (öneri üreticinin §6 notuyla aynı) |
| Cümle sınırı | evet | 34,23 = `sozcukler.json` cümle 4 ilk sözcük "İkinci" `t0`; cümle 3 son sözcük 33,68'de biter (ara 0,55 sn); `baslar.json` pakette yok, değer sözcüklerden türetildi ve `altyazi.json` ile aynı | Kart söz ortasına düşmez; 30,32 bir parça başıdır, cümle başı değil (doğru elendi) |
| İlk 30 sn | evet | 34,23 > 30 | — |
| Son 20 sn | evet | kart 34,23–37,23; ders sonu − 20 = 65,93; çıkış klibi ayrıca eklenir | — |

Kapsam dışı not (YT-3, video jürisi): kartın yer ölçümü (`yer.json` sol alt) başka iki dersin karelerinden çıktı; bu dersin sahne 4 karelerinde (mp4 ve kare yok)
çakışma ölçülemedi, dikey yer "ayrıca ölçülür" hâlinde. Bu madde mp4 sonrası jüride kapatılır.

## Kaldı maddeleri için düzeltme önerisi

Kaldı madde yok. İsteğe bağlı iyileştirme (hüküm değiştirmez):

- Sabit yorum: "Sınavdan önce tekrar etmek için bu dersi kaydet; süreç ile sonucun farkını anlatan bölüme açıklamadaki damgalarla doğrudan geç."

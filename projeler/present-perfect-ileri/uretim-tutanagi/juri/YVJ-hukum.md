# YVJ-hukum — `present-perfect-ileri` YouTube yayın verisi ÇIKTI jürisi · 15.11.2026

Jüri modeli: **Claude Sonnet 5.5** (`claude-sonnet-5-5`). Üretici model (YV-RAPOR.md): Claude Opus 5.5. İki model FARKLI: kural §1 (3) sağlandı.
Bakılan çıktı: `youtube.json`, `youtube-aciklama.md` (ana ve dikey paket), `zaman.json`, `ortak/anlatim/METIN.md` (cümle başları),
`senaryo.json`, `altyazi.json`, `surumler.json`, katalog (`D/varlik/grammar/katalog.json`, `konu-adlari.json`), `kapak.png` (iki paket).
Hiçbir üretim dosyası değişmedi. Sayılar jüri tarafından ölçüldü (`/usr/bin/python3 -I`).

## Özet

| Sonuç | Sayı |
|---|---|
| Geçti (evet) | 12 (YV 8 + §3 4) |
| Kaldı (hayır) | 1 (YV-6) |
| Kanıt yok | 0 |

Dikey paket: `youtube.json` aynı (diff boş), `youtube-aciklama.md` yalnız `utm_content` farkıyla aynı. Hüküm iki pakette aynıdır.

## Madde tablosu (`juri-olcutleri.md` §2f)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | başlık 57 karakter (60 bayt) ≤ 100; kalıp `<Konu> \| YDT İngilizce` | temel dersin başlığı "Present Perfect \| YDT İngilizce"; ileri başlık ondan ayrı, çakışma yok |
| YV-2 | evet | açıklama 687 bayt (648 karakter) ≤ 5.000; sıra: değer cümlesi → kaydet → damgalar → sıradaki ders → bağlantı → etiket satırı | taban adres canlılığı kapsam dışı (sozlesme.md: 15.11'de 404; yayın öncesi ayrıca bakılır) |
| YV-3 | evet | ilk damga 00:00; 5 bölüm; en kısa bölüm 15,92 sn (`zaman.json` 17,97 → 33,89); damgalar en yakın sn: 00:18 · 00:34 · 00:51 · 01:09 | 3 sn'lik giriş sahnesi kanca bölümüne birleşti; her damga söz başından önce düşer |
| YV-4 | evet | senaryodan denetlendi: bölüm 1 formül cümlesi (cümle 2); bölüm 2 "Ever since the company launched… has doubled" (cümle 3); bölüm 3 `for` süre, `since` başlangıç (cümle 4; sahne 4 kodunda "since + başlangıç" kutusu var); bölüm 4 "…took off two hours ago, but it hasn't landed yet" (cümle 5); bölüm 5 "Finished time / Unfinished time" (cümle 7) | iç ad ("Örnek 1") yok; en uzun ad 36 karakter |
| YV-5 | evet | 14 etiket, düz toplam 137, tırnaklı sayımla 166 ≤ 500; yineleme yok; konu (Present Perfect), zaman adı (Simple Past, Present Perfect Tense), kitle (YDT), "İngilizce", "gramer" var | tek sözcüklü "ileri" etiketi arama değeri taşımaz; sınırı bozmaz, kaldı değil |
| **YV-6** | **hayır** | açıklama satır 1: "**ago içeren cümlede Present Perfect'in neden kullanılmadığını**". Dersin kendi üçüncü kök cümlesi "The plane took off two hours ago, but it hasn't landed yet." hem `ago` hem Present Perfect (`hasn't landed`) taşır; bölüm 4 adı da "ago ve yet aynı cümlede" der. Yani "ago içeren cümlede Present Perfect kullanılmaz" mutlak kuralı dersin kendi örneğiyle çelişir. Doğru ifade: `ago` ile verilen bitmiş zaman bildiriminin fiili Simple Past ister. YV-RAPOR §5 bu satırı "kesin" saymış; kanıt tersini gösterir | düzeltme önerisi aşağıda |
| YV-7 | evet | katalog: ünite 02 "Tenses"; `GR-02-06` konu sırası 6 (`konular[5]`); önceki `02-05-ydt-ileri` (`konular[4]`), sonraki `02-07-ydt-ileri` (`konular[6]`); liste adı "Tenses · YDT İleri" (`kitleler.ydt` = YDT, `seviyeler.ileri` = İleri) | "Sıradaki ders" adı katalogdaki "Present Perfect: Since & For" yerine "Present Perfect: since ve for" yazılmış; emsal 02-04 de adı kısaltır, hata sayılmadı |
| YV-8 | evet | `altyazi.json` son satır `t1` = 92,85 < ders süresi 93,77 (`zaman.json`); pakette srt yok (panel türetir) | |
| YV-9 | evet | `kapak.png` iki pakette var (1920×1080, 1080×1920); `KAPAK-RAPOR.md` satır 5–6: açık · koyu ayrı dosya, `kapak.png` açık; gönderi metninde emoji 0 | kapak görseli bkz. ek bulgu 1 |

## `youtube-surumu-standart.md` §3 bildirim kuralları

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | ders 93,77 sn < 4 dk → 1 bildirim; `bildirimler` 1 satır (t 34,44, sure 3,0) |
| Zaman ≈ %30 | evet | 34,44 / 93,77 = %36,7. Hedef 28,13 sn ilk 30 sn yasağına ve cümle sınırı kuralına (cümle başları 18,52 · 34,44 · 51,80) düşer; 30 sn sonrası ilk cümle başı = 34,44; sozlesme.md YV satırı (simple-present-temel: 28,04 → 43,91) aynı kuralı uygular |
| Cümle sınırı | evet | 34,44 = `METIN.md` cümle 4 başı ("İkinci kök."); önceki cümle 33,89'da biter |
| İlk 30 sn / son 20 sn | evet | 34,44 ≥ 30; kart 34,44–37,44; ders sonu 93,77 → son 20 sn başlangıcı 73,77; giriş klibi 3 sn eklenince kart 37,44–40,44 |

Kare üzerinden yer çakışması (YT-3 "kare") bu istemin kapsamı değil; mp4 yok, ölçülmedi.

## Kaldı maddesi için düzeltme önerisi

| Dosya | Yeni metin (satır 1) |
|---|---|
| `present-perfect-ileri/youtube-aciklama.md` ve `present-perfect-ileri-dikey/youtube-aciklama.md` | Present Perfect formülünü, since ile for ayrımını ve ago ile söylenen bitmiş zamanın neden Simple Past istediğini üç sınav köküyle öğren. |

Düzeltmeden sonra jüri YV-6'yı yeniden koşar (kural §1 (2)).

## Ek bulgular (kaldı değil; şef kararı, D-0205: "kaynağa uygun" ≠ "doğru")

1. **Ana ders ve kapak mutlak kural taşır.** Kanca cümlesi "Ago varsa Present Perfect yok." (cümle 1) ve kapak "AGO VARSA / PERFECT YOK" aynı mutlak kuralı verir; dersin kendi üçüncü kök cümlesi onu çürütür (`ago` + `hasn't landed`). Gönderi görseli bu kapaktır. Önerilen kanca/kapak sözü: "Ago varsa Simple Past." (kapak alt satırı "ago → Simple Past" doğru; `surumler.json` ve `senaryo.json meta.kapak` zaten "AGO VARSA SIMPLE PAST" der, kapak görseliyle tutarsız). Ses sentezi gerektirdiği için bu turda dokunulmadı.
2. **Ana dersteki mutlak ifadeler.** "Since cümleciği Simple Past alır" (cümle 3) ve "ago varsa Simple Past, yet varsa Present Perfect" (cümle 7) sınav kalıbı olarak kabul edilebilir; `since` cümleciği Present Perfect de alabilir ("since I've lived here"), `ago` Past Continuous ile de gelir. Metadata bu ifadeleri tekrarlamıyor; ders düzeyinde Ş karar verir.
3. **Dikey sürüm Shorts sayılır.** Giriş 3 + ders 93,77 + kısa çıkış ≤ 4 ≈ 100 sn ≤ 180 sn (`youtube-surumu-standart.md` §2). Bölüm damgaları ve bildirim kartı Shorts'ta işlemeyebilir; dikey `youtube.json` yine de tam yazılı. Ölçütte engel yok; yayın kararı Ş'de.
4. **"Sıradaki ders" tekrarı.** 02-07 konusu "Since & For"; bu ders bölüm 3'te since/for ayrımını zaten anlatıyor. İçerik planı notu, ölçüt dışı.

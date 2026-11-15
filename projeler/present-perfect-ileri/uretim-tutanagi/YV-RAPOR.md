# YV-RAPOR — `present-perfect-ileri` YouTube yayın verisi · 15.11.2026

İstem: `uretim-hatti/istemler/YV-0206I.md`. Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`). Jüri bu modelden farklı bir modelle koşmalıdır (`juri-olcutleri.md` §1e).

| Dosya | Durum |
|---|---|
| `present-perfect-ileri/youtube.json` | yazıldı, JSON ayrıştı |
| `present-perfect-ileri/youtube-aciklama.md` | yazıldı, 687 bayt |
| `present-perfect-ileri-dikey/youtube.json` | yazıldı, JSON ayrıştı (dikey paket var: `surumler.json` → `dikey-tam`, `proje: present-perfect-ileri-dikey`) |
| `present-perfect-ileri-dikey/youtube-aciklama.md` | yazıldı, 687 bayt, `utm_content=dikey-tam` |

Kaynaklar: `senaryo.json` (başlık "Present Perfect", kitle YDT, seviye ileri), `zaman.json` (6 sahne, ders 93,77 sn), `ortak/anlatim/METIN.md` (cümle başları sütunu),
`altyazi.json` (22 satır), `surumler.json` (`video.etiketler`, kod `ING-YDT-GR-02-06-I`), `D/varlik/grammar/katalog.json` (ünite 02 Tenses, konu sırası 6),
`D/varlik/grammar/konu-adlari.json` (GR-02-07 adı), `uretim-tutanagi/KAPAK-RAPOR.md` (kapak teması). Taban adres ve utm biçimi: `simple-present-temel-s3/aciklama-a.md`
ve `02-04-ydt-temel/youtube-aciklama.md` emsali (`present-perfect-ileri-s1` paketinde açıklama dosyası yok; §6).

## 1. Ölçüm komutu çıktısı (iki paket aynı; ana paket satırları)

```
== present-perfect-ileri JSON ayrıştı; ders süresi 93.77
baslik 57 karakter: Present Perfect: since, for ve ago tuzağı | YDT İngilizce | kalıp: True
etiket sayı 14 düz toplam 137 | virgül+tırnak dahil 166 | yineleme False
  bölüm 0 → 17.97 süre 17.97 | ad 36 kr | Formül: have / has + past participle | sahne başı: True
  bölüm 17.97 → 33.89 süre 15.92 | ad 35 kr | Ever since: iki cümlecik, iki zaman | sahne başı: True
  bölüm 33.89 → 51.25 süre 17.36 | ad 35 kr | Süre mi, başlangıç mı: for ve since | sahne başı: True
  bölüm 51.25 → 68.6 süre 17.35 | ad 30 kr | Tuzak: ago ve yet aynı cümlede | sahne başı: True
  bölüm 68.6 → 93.77 süre 25.17 | ad 35 kr | Bitmiş zaman mı, bitmemiş zaman mı? | sahne başı: True
damgalar youtube.json ile birebir (en yakın sn): True 5
  bildirim t 34.44 sure 3.0 | oran 36.7% | ilk30 dışı True | son20 dışı True | cümle başı True
giris True cikis True aciklamaDosya youtube-aciklama.md
sabitYorum 118 kr; cümle sayısı 1
gönderi g1 görsel kapak.png var: True | ilk cümle soru True | cümle 3
emoji 0
açıklama bayt 687 | hashtag ['#YDT', '#İngilizce', '#gramer', '#PresentPerfect', '#SimplePast']
yasak/kısaltma taraması: []
utm: ['utm_source=youtube', 'utm_medium=video', 'utm_campaign=ING-YDT-GR-02-06-I', 'utm_content=ana-yatay']
liste {'ad': 'Tenses · YDT İleri', 'sira': 6, 'onceki': '02-05-ydt-ileri', 'sonraki': '02-07-ydt-ileri'}
altyazı son t1 92.85 < ders sonu 93.77 True
present-perfect-ileri/kapak.png:       PNG image data, 1920 x 1080, 8-bit/color RGB, non-interlaced
present-perfect-ileri-dikey/kapak.png: PNG image data, 1080 x 1920, 8-bit/color RGB, non-interlaced
```

Dikey paketin satırları aynıdır; tek fark `utm_content=dikey-tam`. Dikey `zaman.json` sahne başları ana paketle aynı (0 · 3 · 17,97 · 33,89 · 51,25 · 68,6; son 93,77).
`METIN.md`, `altyazi.json` ve `senaryo.json` iki pakette bayt bayt aynı (`cmp` çıkışı 0).

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet (Ş bakacak, §6 madde 1) | 57 karakter ≤ 100; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu kısmı "Present Perfect: since, for ve ago tuzağı": temel paketin `senaryo.json` başlığı da "Present Perfect"; düz kalıp iki videoya aynı başlığı verir |
| YV-2 | evet | 687 bayt ≤ 5.000. Sıra: 1. satır değer cümlesi · 2. satır kaydet · 4–8. satır damgalar · 10. satır sıradaki ders · 11. satır bağlantı · 13. satır etiket |
| YV-3 | evet | ilk damga 0; 5 bölüm; en kısa bölüm 15,92 sn (Örnek 1). Giriş sahnesi (3 sn) kanca bölümüne birleşti |
| YV-4 | evet (D bakacak) | bölüm tablosu §3; her ad sahnede söylenen içeriği taşır, iç ad yok, en uzun 36 karakter ≤ 40 |
| YV-5 | evet | düz toplam 137; YouTube sayımıyla (virgül + boşluklu etikete tırnak) 166 ≤ 500. Konu "Present Perfect", zaman adları "Present Perfect", "Present Perfect Tense", "Simple Past", kitle "YDT" var; yineleme yok |
| YV-6 | evet (D bakacak) | §5 iddia tablosu; metinlerde mutlak kural ve yanlış denklik kullanmadım (Türkçe zaman karşılığı etiketi bilerek yok, §6 madde 7); yazım taraması: emoji 0, "Tam ders" / "dakika" / "dk" yok |
| YV-7 | evet | katalog: ünite `02` "Tenses", konu `GR-02-06` sıra 6; önceki `02-05-ydt-ileri`, sonraki `02-07-ydt-ileri`. Liste adı "Tenses · YDT İleri" (`kitleler.ydt` = YDT, `seviyeler.ileri` = İleri) |
| YV-8 | evet (pakette srt yok) | `altyazi.srt` panelde türetilir (sözleşme §2). Kaynak `altyazi.json` son satırı t1 = 92,85 < ders sonu 93,77 |
| YV-9 | evet | `kapak.png` pakette var, 1920×1080, açık tema (`KAPAK-RAPOR.md` satır 5). Gönderi metninde emoji 0 |

`youtube-surumu-standart.md` §3 bildirim kuralları:

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | ders 93,77 sn < 4 dk → 1 bildirim |
| Zaman ≈ %30 | kısmen | %36,7. Gerekçe §4 |
| Cümle sınırı | evet | 34,44 = `METIN.md` cümle 4 başı ("İkinci kök."); önceki cümle 33,89'da biter |
| İlk 30 sn / son 20 sn | evet | 34,44 ≥ 30; 34,44 + 3,0 = 37,44 ≤ 73,77 |
| `giris`, `cikis` | evet | ikisi de `true` |

## 3. Bölüm tablosu

| `t` (sn) | Damga | İç ad (`zaman.json`) | İzleyici adı | Süre (sn) |
|---|---|---|---|---|
| 0 | 00:00 | Giriş + Kanca | Formül: have / has + past participle | 17,97 |
| 17,97 | 00:18 | Örnek 1 | Ever since: iki cümlecik, iki zaman | 15,92 |
| 33,89 | 00:34 | Örnek 2 | Süre mi, başlangıç mı: for ve since | 17,36 |
| 51,25 | 00:51 | Örnek 3 | Tuzak: ago ve yet aynı cümlede | 17,35 |
| 68,6 | 01:09 | Soru + Form | Bitmiş zaman mı, bitmemiş zaman mı? | 25,17 |

Damga kuralı: `youtube.json` sahne başını ondalıklı tutar; açıklamadaki damga = en yakın saniye (pilot `simple-present-temel` ve `02-04-ydt-temel` ile aynı).
Her damga sözden önce düşer (söz başları 18,52 · 34,44 · 51,80 · 69,15). Ölçüm: `damgalar youtube.json ile birebir (en yakın sn): True 5` (iki paket).
Giriş klibi eklenirse damgalar giriş süresi kadar kayar; araç düzeltir (sözleşme §3; açıklamaya yazılmadı).

İlk bölümün içeriği: kanca cümlesi "Ago varsa Present Perfect yok." (1,00–3,48) ve formül "subject plus have or has plus past participle" (9,96–15,32).
Bölüm adı formülü öne alır; kanca 3,5 sn sürer, ayrı bölüm olamaz (≥ 10 sn kuralı).

## 4. Bildirim anı

Seçilen an: **34,44 sn** → `METIN.md` cümle 4 başı "İkinci kök." Önceki söz "…ana cümle Present Perfect." 33,89'da biter.
Kart 34,44–37,44 arasında durur. Bu aralıkta "İkinci kök. Selim has worked at this bank for thirty years" söylenir; kart sessizdir, sözü kesmez.
Kart sahne 4 geçişinden (33,89 + 12 kare BookFlip = 34,29) sonra başlar.

| Aday | Oran | Sonuç |
|---|---|---|
| %30 hedefi = 28,13 sn | %30,0 | YASAK: ilk 30 sn içinde |
| 29,73 ("Since cümleciği…", parça başı) | %31,7 | YASAK: ilk 30 sn içinde |
| **34,44 (cümle 4 başı)** | **%36,7** | seçildi: 30 sn sonrası ilk cümle sınırı; ilk bilgi (formül + 1. kök) verildi |
| 51,80 (cümle 5 başı) | %55,2 | hedefe daha uzak |

## 5. Dilbilgisi iddiaları

| Metin | Yer | İddia | Hüküm |
|---|---|---|---|
| "Present Perfect: since, for ve ago tuzağı" | başlık | iddia yok; "tuzak" dersin kendi sözü (cümle 5 "Tuzak burada.") | kesin |
| "ago içeren cümlede Present Perfect'in neden kullanılmadığını" | açıklama satır 1 | ago, bitmiş zaman bildirir; Present Perfect ile kullanılmaz | kesin |
| "Formül: have / has + past participle" | bölüm 1 | Present Perfect = have/has + past participle | kesin |
| "Ever since: iki cümlecik, iki zaman" | bölüm 2 | örnek cümlede since cümleciği Simple Past (launched), ana cümle Present Perfect (has doubled) | kesin (örnek için) |
| "Süre mi, başlangıç mı: for ve since" | bölüm 3 | for süre, since başlangıç noktası bildirir | kesin |
| "Tuzak: ago ve yet aynı cümlede" | bölüm 4 | örnek "The plane took off two hours ago, but it hasn't landed yet." iki sözcüğü birlikte taşır | kesin |
| "Bitmiş zaman mı, bitmemiş zaman mı?" | bölüm 5 | soru; iddia yok | kesin |
| "Ago varken has landed diyebilir miyiz?" | gönderi | soru; dersin cevabı "Hayır" (cümle 7) | kesin |
| "since, for ve ago farkını üç sınav köküyle" | gönderi | ders üç kök verir (cümle 3, 4, 5) | kesin |
| "Sıradaki ders: Present Perfect: since ve for" | açıklama | 02-07 konusunun adı | jüri bakacak (§6 madde 4) |

Bilerek yazmadığım iddialar (ana derste var, mutlak kural riski taşır; D jürisi ana derse bakmalı, `juri-olcutleri.md` §1c):
- "Since cümleciği Simple Past alır" (cümle 3): since cümleciği süren bir durumda Present Perfect de alabilir ("since I've lived here"). Bölüm 2 adı yalnız örneği anlatır.
- "Ago varsa Simple Past" (`canAlici`, cümle 7): ago Past Continuous ile de kullanılır ("two hours ago I was sleeping"). Açıklama yalnız "Present Perfect kullanılmaz" der.
- "Yet var, … Present Perfect" (cümle 5, 7): Amerikan İngilizcesi konuşma dilinde "didn't … yet" de görülür. Metinlere girmedi.

Yazım denetimi: Türkçe karakterler tam; kesme işareti "Present Perfect'in"; kısaltma yalnız "YDT" (yazılı metin; ses kuralı uygulanmaz) ve hashtag.

## 6. Açık noktalar

1. **Başlık (Ş karar):** düz kalıp "Present Perfect | YDT İngilizce" temel dersle aynı başlığı verir. Emsal `K/.claude/docs/sozlesme.md` satır 149 (başlık çakışırsa `surumler.json` `konu` alt başlığı); bu derste `konu` alt başlıksız ("Present Perfect"), alt başlığı dersin içeriğinden (amaçlar: since/for, ago tuzağı) yazdım. Şef düz kalıbı isterse yalnız `baslik` değişir.
2. **Gönderi görseli adı:** `surumler.json` `ana-yatay.kapak` = `null`; dikey satırdaki `kapak` alanı dosya adı değil, metin ("AGO VARSA SIMPLE PAST"). Dosya adını (`kapak.png`) paketten ve `KAPAK-RAPOR.md`'den aldım. Not: kapak görselinde metin "AGO VARSA / PERFECT YOK"; `surumler.json` ve `senaryo.json meta.kapak` alanı "SIMPLE PAST" der (paketler arası tutarsızlık; benim yazma alanım dışında).
3. **Taban adres:** `present-perfect-ileri-s1` paketinde `aciklama*.md` yok. `https://ydspublishing.com/grammar/02-06-ydt-ileri` emsal kalıptan türedi; canlılığı bu oturumda ölçülmedi; `K/.claude/docs/sozlesme.md` satır 149 taban adresin 15.11'de 404 verdiğini yazar.
4. **Sıradaki ders adı:** `konu-adlari.json` GR-02-07 = "Present Perfect: Since & For" (güven "yuksek"; kanıt cümlesi adı doğrudan söylemiyor). Katalogda `02-07-ydt-ileri` durumu `planli`; önceki `02-05-ydt-ileri` da `planli`.
5. **Bildirim oranı:** %36,7 (hedef ≈ %30 ilk 30 sn yasağına düşüyor; §4).
6. **Giriş klibi kayması:** damgalar ders zamanıdır; giriş klibi eklenince API kaydırır (sözleşme §3). Açıklamaya not yazılmadı.
7. **Türkçe zaman adı etiketi:** "yakın geçmiş zaman" gibi bir karşılık bilerek yok (yanlış denklik riski, YV-6).
8. **Dikey gönderi:** dikey paketteki `kapak.png` 1080×1920'dir. Topluluk gönderisinde hangi kapağın kullanılacağını takvim uygulaması seçer.
9. Etiket "YKS": YDT, YKS'nin yabancı dil testidir; pilot emsali.
10. **Dikey sürüm Shorts sayılabilir (Ş karar):** dikey ders 93,77 sn ≤ 3 dk. `K/.claude/docs/sozlesme.md` satır 148'e göre YouTube bu sürümü Shorts sayar; bölüm damgaları ve bildirim kartı orada işlemeyebilir. Dikey `youtube.json` verisi yine tam yazıldı.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0206I).

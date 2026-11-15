# YV-RAPOR — `simple-present-temel` YouTube yayın verisi · 15.11.2026

İstem: `uretim-hatti/istemler/YV-0202T.md`. Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`). Jüri bu modelden farklı bir modelle koşmalıdır (`juri-olcutleri.md` §1e).

| Dosya | Durum |
|---|---|
| `simple-present-temel/youtube.json` | yazıldı, JSON ayrıştı |
| `simple-present-temel/youtube-aciklama.md` | yazıldı, 661 bayt |
| `simple-present-temel-dikey/youtube.json` | yazıldı, JSON ayrıştı (dikey paket var: `surumler.json` → `dikey-tam`, `proje: simple-present-temel-dikey`) |
| `simple-present-temel-dikey/youtube-aciklama.md` | yazıldı, 661 bayt, `utm_content=dikey-tam` |

Kaynaklar: `senaryo.json` (başlık "Simple Present", kitle YDT), `zaman.json` (6 sahne, ders 93,47 sn), `ortak/anlatim/METIN.md` (cümle başları sütunu),
`altyazi.json` (26 satır), `surumler.json` (`video.etiketler`, kod `ING-YDT-GR-02-02-T`), `D/varlik/grammar/katalog.json` (ünite 02 Tenses, konu sırası 2),
kısa açıklaması `simple-present-temel-s1/aciklama-a.md` (taban adres, utm biçimi, sıradaki ders adı).

## 1. Ölçüm komutu çıktısı (iki paket aynı; ana paket satırları)

```
== simple-present-temel JSON ayrıştı; ders süresi 93.47
baslik 30 karakter: Simple Present | YDT İngilizce | kalıp: True
etiket sayı 13 düz toplam 134 | virgül+tırnak dahil 162 | yineleme False
  bölüm 0 → 15.45 süre 15.45 | ad 36 kr | Geniş zamandan köprü: Simple Present | sahne başı: True
  bölüm 15.45 → 27.69 süre 12.24 | ad 38 kr | Doğa kanunu: The sun rises in the east | sahne başı: True
  bölüm 27.69 → 43.36 süre 15.67 | ad 38 kr | Alışkanlık: usually, always, every day | sahne başı: True
  bölüm 43.36 → 60.47 süre 17.11 | ad 38 kr | Tarife ve program: Our plane takes off | sahne başı: True
  bölüm 60.47 → 93.47 süre 33.00 | ad 32 kr | Neden hep s? He, she, it ve does | sahne başı: True
damgalar youtube.json ile birebir: True 5   (ilk ölçüm aşağı yuvarlamayla; son hâl en yakın saniye, §3)
  bildirim t 43.91 sure 3.0 | oran 47.0% | ilk30 dışı True | son20 dışı True
sabitYorum 112 kr; cümle sayısı 1
gönderi g1 görsel kapak.png | ilk cümle soru o" diyoruz | cümle 3
emoji 0
açıklama bayt 661 | hashtag ['#YDT', '#İngilizce', '#gramer', '#SimplePresent']
yasak söz: []
utm: ['utm_source=youtube', 'utm_medium=video', 'utm_campaign=ING-YDT-GR-02-02-T', 'utm_content=ana-yatay']
simple-present-temel/kapak.png:       PNG image data, 1920 x 1080
simple-present-temel-dikey/kapak.png: PNG image data, 1080 x 1920
```

Dikey paketin satırları aynıdır; tek fark `utm_content=dikey-tam`. Dikey `zaman.json` sahne başları ana paketle aynı (0 · 3 · 15,45 · 27,69 · 43,36 · 60,47; son 93,47).
`METIN.md` ve `altyazi.json` iki pakette bayt bayt aynı (`cmp` çıkışı 0).

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 30 karakter; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu = `senaryo.json` `baslik` "Simple Present" |
| YV-2 | evet | 661 bayt (≤ 5.000). Sıra: 1. satır değer cümlesi · 2. satır kaydet · 4–8. satır damgalar · 10. satır sıradaki ders · 11. satır bağlantı · 13. satır etiket |
| YV-3 | evet | ilk damga 0; 5 bölüm; en kısa bölüm 12,24 sn (Örnek 1). Giriş sahnesi (3 sn) kanca bölümüne birleşti |
| YV-4 | evet (D bakacak) | bölüm tablosu §3; her ad sahnede söylenen içeriği taşır, iç ad yok, en uzun 38 karakter |
| YV-5 | evet | düz toplam 134; YouTube sayımıyla (virgül + boşluklu etikete tırnak) 162 ≤ 500. Konu "Simple Present", zaman adı "Present Simple", "geniş zaman", kitle "YDT" var; yineleme yok |
| YV-6 | evet (D bakacak) | §5 iddia tablosu; mutlak kural ve yanlış denklik kullanmadım; yazım taraması: emoji 0, "Tam ders" / "dakika" / "dk" yok |
| YV-7 | evet | katalog: ünite `02` "Tenses", konu `GR-02-02` sıra 2; önceki `02-01-ydt-temel`, sonraki `02-03-ydt-temel`. Liste adı "Tenses · YDT Temel" (`kitleler.ydt` = YDT, `seviyeler.temel` = Temel) |
| YV-8 | evet (pakette srt yok) | `altyazi.srt` panelde türetilir (sözleşme §2). Kaynak `altyazi.json` son satırı t1 = 92,55 < ders sonu 93,47 |
| YV-9 | evet | `kapak.png` pakette var, 1920×1080, açık tema (`KAPAK-RAPOR.md` satır 5). Gönderi metninde emoji 0 |

`youtube-surumu-standart.md` §3 bildirim kuralları:

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | ders 93,47 sn < 4 dk → 1 bildirim |
| Zaman ≈ %30 | kısmen | %47,0. Gerekçe §4 |
| Cümle sınırı | evet | 43,91 = `METIN.md` cümle 5 başı ("Üçüncü örnek."); önceki cümle 43,36'da biter |
| İlk 30 sn / son 20 sn | evet | 43,91 ≥ 30; 43,91 + 3,0 = 46,91 ≤ 73,47 |
| `giris`, `cikis` | evet | ikisi de `true` |

## 3. Bölüm tablosu

| `t` (sn) | Damga | İç ad (`zaman.json`) | İzleyici adı | Süre (sn) |
|---|---|---|---|---|
| 0 | 00:00 | Giriş + Kanca | Geniş zamandan köprü: Simple Present | 15,45 |
| 15,45 | 00:15 | Örnek 1 | Doğa kanunu: The sun rises in the east | 12,24 |
| 27,69 | 00:28 | Örnek 2 | Alışkanlık: usually, always, every day | 15,67 |
| 43,36 | 00:43 | Örnek 3 | Tarife ve program: Our plane takes off | 17,11 |
| 60,47 | 01:00 | Soru + Form | Neden hep s? He, she, it ve does | 33,00 |

Damga kuralı: `youtube.json` sahne başını ondalıklı tutar; açıklamadaki damga = en yakın saniye (sözleşme satırı 145, 02-04 YV-0204T ile aynı;
ilk ölçümde aşağı yuvarlamıştım, paketler arası tutarlılık için değiştirdim: 27,69 → 00:28). Her damga sözden önce düşer (söz başları 16,00 · 28,24 · 43,91 · 61,02).
Yuvarlama denetimi: `yuvarlama ile birebir: True` (iki paket), açıklama yine 661 bayt. Giriş klibi eklenirse damgalar giriş süresi kadar kayar; araç düzeltir (açıklamaya yazılmadı).

## 4. Bildirim anı

Seçilen an: **43,91 sn** → `METIN.md` cümle 5 başı "Üçüncü örnek." (önceki söz "Yine s harfi var." 43,36'da biter; Örnek 3 sahnesi 43,36'da açılır).

- %30 hedefi = 28,04 sn. Bu an ilk 30 sn yasağının içinde kalır.
- Ana pakette `baslar.json` yok. Cümle başları dosyası olarak `METIN.md` "başlar" sütununu kullandım (`senaryo.json` cümleleri).
- 30 sn sonrasındaki ilk cümle başı 43,91'dir. Sonrakiler 61,02 ve 65,73 (%30'dan daha uzak).
- Seçenek (jüri ya da şef karar verir): `altyazi.json` satır başı 32,74 sn ("Kardeşim genellikle okula otobüsle gider.", %35). Bu an gerçek cümle sınırıdır,
  ama `senaryo.json` cümle 4'ün içinde kalır ve örnek ile çevirisini ayırır.

## 5. Dilbilgisi iddiaları

Benim metinlerim:

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama 1. satır | Simple Present: doğa kanunu, alışkanlık, tarife; fiile gelen s (he, she, it) | kesin |
| Bölüm 1 | "Geniş zamandan köprü" (denklik değil, köprü) | jüri bakacak (sözcük seçimi) |
| Bölüm 2 | The sun rises in the east = doğa kanunu | kesin |
| Bölüm 3 | usually, always, every day alışkanlık işaretidir (tek zamana özgü demez) | kesin; jüri bakacak: always öteki zamanlarla da gelir, ad bunu dışlamaz |
| Bölüm 4 | Our plane takes off: tarife, program | kesin |
| Bölüm 5 | he, she, it ile s; olumsuz ve soruda does | kesin |
| Gönderi | "he goes" ama "I go"; üç örnekte fiile gelen s (rises, goes, takes off) | kesin |
| Sabit yorum | dilbilgisi iddiası yok | — |

Ana dersteki iddialar (benim metnime girmedi; `juri-olcutleri.md` §1c gereği raporluyorum):

| Yer | İddia | Hüküm |
|---|---|---|
| Senaryo cümle 2 | "İngilizcedeki karşılığı Simple Present" | jüri bakacak: kısmi denklik. Durum fiilleri çoğu kez -(I)yor ile çevrilir (I know → biliyorum); geniş zaman istek ve söz de taşır |
| Senaryo cümle 7 | "Türkçedeki er eki gibi: git-er, go-es" | jüri bakacak: -er her kişiyle gelir (giderim, gidersin); -s yalnız üçüncü tekil kişiyle gelir |
| `canAlici` 1 | "geniş zaman eki = İngilizcedeki s" | jüri bakacak: yanlış denklik riski (aynı gerekçe) |
| Senaryo cümle 7 | "Kod: always, usually, every day, Simple Present" | jüri bakacak: mutlak kural riski (always + Present Continuous / Present Perfect) |

## 6. Açık noktalar

1. **Dikey sürüm Shorts sayılır.** YouTube 15.10.2024'ten sonra yüklenen ≤ 3 dk kare ya da dikey videoyu Shorts sayar (Google yardım sayfası 15424877).
   Dikey ders 93,47 sn. Bölüm damgaları ve sessiz bildirim Shorts'ta işlemeyebilir (Shorts'ta bölüm desteği için kanıt bulamadım). Karar şefte.
2. Bildirim %47'de (§4). Daha yakın an istenirse 32,74 seçeneği var.
3. `surumler.json` `ana-yatay` satırında `kapak: null`; `dikey-tam` satırında `kapak` bir dosya adı değil, yazı ("GİDER = GOES").
   Gönderi görseli adı bu yüzden `surumler.json`'dan alınamadı; `kapak.png` kullandım (pakette var, açık tema). API dosya izni `youtube.json`'u da okur.
4. Dikey pakette aynı `g1` gönderisi var (istem gereği). Takvim uygulaması gönderiyi iki kez paylaşabilir. Dikey pakette `kapak.png` 1080×1920 dosyayı gösterir.
   Öneri: gönderiyi yalnız ana sürümden paylaş.
5. Başlık çakışması: `simple-present-ileri` (`02-02-ydt-ileri`) senaryo başlığı da "Simple Present". Kalıp iki derse aynı başlığı verir; ileri dersin YV işinde konu adı ayrılmalı.
6. Taban adres `https://ydspublishing.com/grammar/02-02-ydt-temel` kısalardan alındı; kısalardaki UYARI geçerli: canlılığı ölçülmedi.
7. Sıradaki ders adı katalog konusundan (`02-03-ydt-temel/surumler.json` `konu`): "Present Continuous ve Simple Present: ayrım alıştırması"; kısalarla aynı.
8. Sözleşmedeki kanal sabitleri dosyası `kalem/ortak/youtube/kanal.json` bu worktree'de yok (bu işin yazma alanı dışında).
9. Ana dersin giriş rozeti `senaryo.json` `giris.rozetler` "YDT · BASIC" (huni v2 §9 açık işi); yayın verisine girmedi.
10. Bildirim kartının yeri (sağ üst, 3 karede çakışma) görsel jüri işidir; kare çekmedim (render yok kuralı). `ortak/youtube/bildirim/yer.json` şu an `sol_alt` yazıyor; standart §3 "sağ üst" der.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0202T).

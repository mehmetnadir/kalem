# YV-RAPOR — `simple-past-temel` YouTube yayın verisi · 15.11.2026

İstem: `uretim-hatti/istemler/YV-0210T.md`. Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`). Jüri bu modelden farklı bir modelle koşmalıdır (`juri-olcutleri.md` §1e).

| Dosya | Durum |
|---|---|
| `simple-past-temel/youtube.json` | yazıldı, JSON ayrıştı |
| `simple-past-temel/youtube-aciklama.md` | yazıldı, 640 bayt |
| `simple-past-temel-dikey/youtube.json` | yazıldı, JSON ayrıştı (dikey paket var: `surumler.json` → `dikey-tam`, `proje: simple-past-temel-dikey`) |
| `simple-past-temel-dikey/youtube-aciklama.md` | yazıldı, 640 bayt, `utm_content=dikey-tam` |

Kaynaklar:

- Konu adı: `surumler.json` `video.konu` "Simple Past". Pakette `senaryo.json` yok. Konu adını iki kaynak doğrular: `D/varlik/grammar/konu-adlari.json` GR-02-10 "Simple Past" (güven yüksek) ve künye `ders: "SIMPLE PAST"`.
- Kitle: künye `ortak/kunye.js` (`seviye: "YDT BASIC"`) ve `surumler.json` `kitle: "YDT"`. Kod `ING-YDT-GR-02-10-T`.
- Zaman: `zaman.json` (6 sahne, ders 93,81 sn). Cümle başları: `ortak/anlatim/METIN.md` "başlar" sütunu. Pakette `baslar.json` yok.
- Altyazı: `ortak/anlatim/altyazi.json` (26 satır).
- Katalog: `D/varlik/grammar/katalog.json` (ünite `02` "Tenses", konu GR-02-10, sıra 10).
- Sıradaki ders adı: `konu-adlari.json` GR-02-11 "Past Continuous".
- Bağlantı tabanı ve utm biçimi: kısa paketi `simple-past-temel-s1` içinde açıklama dosyası yok. Taban ve biçimi emsal kısalardan aldım: `02-04-ydt-temel-s1/aciklama-a.md`, `simple-present-temel-s1/aciklama-a.md` (`https://ydspublishing.com/grammar/<ders kimliği>`, `utm_campaign` büyük harf ders kodu).
- Kurallar: `K/.claude/docs/sozlesme.md` satır 147 (damga en yakın saniye; bildirim cümle başında; `kapak` null iken kök `kapak.png`).

## 1. Ölçüm komutu çıktısı (iki paket aynı; ana paket satırları)

```
== simple-past-temel JSON ayrıştı; ders süresi 93.81
baslik 27 karakter: Simple Past | YDT İngilizce | kalıp: True
etiket sayı 13 düz toplam 130 | virgül+tırnak dahil 158 | yineleme False
  bölüm 0 → 14.8 süre 14.80 | ad 37 kr | Türkçe -di ekinden köprü: Simple Past | sahne başı: True
  bölüm 14.8 → 29.35 süre 14.55 | ad 36 kr | Düzenli fiile -ed: I watched a movie | sahne başı: True
  bölüm 29.35 → 47.82 süre 18.47 | ad 29 kr | Düzensiz fiil: go değil, went | sahne başı: True
  bölüm 47.82 → 64.78 süre 16.96 | ad 38 kr | Olumsuz ve soru: didn't, Did you play? | sahne başı: True
  bölüm 64.78 → 93.81 süre 29.03 | ad 38 kr | Neden -ed yok? Özet ve zaman ifadeleri | sahne başı: True
damgalar youtube.json ile birebir (en yakın saniye): True 5
  bildirim t 47.82 sure 3.0 | oran 51.0% | ilk30 dışı True | son20 dışı True | sayı 1 (ders<240: True)
sabitYorum 112 kr; cümle sayısı 1
gönderi g1 görsel kapak.png var: True | ilk cümle soru: "went" diyoruz? | cümle 3
emoji 0
açıklama bayt 640 | hashtag ['#YDT', '#İngilizce', '#gramer', '#SimplePast']
yasak söz: []
utm: ['utm_source=youtube', 'utm_medium=video', 'utm_campaign=ING-YDT-GR-02-10-T', 'utm_content=ana-yatay']
liste {'ad': 'Tenses · YDT Temel', 'sira': 10, 'onceki': '02-09-ydt-temel', 'sonraki': '02-11-ydt-temel'} | giris True cikis True
altyazi son t1 92.81 satır 26
simple-past-temel/kapak.png:       PNG image data, 1920 x 1080
simple-past-temel-dikey/kapak.png: PNG image data, 1080 x 1920
```

Dikey paketin satırları aynıdır; tek fark `utm_content=dikey-tam`. Kanıt:

- Dikey `zaman.json` sahne başları ana paketle aynı: 0 · 3 · 14,8 · 29,35 · 47,82 · 64,78; son 93,81.
- `METIN.md`, `altyazi.json`, `sozcukler.json` iki pakette bayt bayt aynı (`cmp` çıkışı 0).
- İki `youtube.json` bayt bayt aynı (`cmp` çıkışı 0). `diff` iki açıklama arasında yalnız 11. satırı gösterir.

Etiket sayımı: "düz toplam" = etiket karakterlerinin toplamı. "virgül+tırnak dahil" = YouTube sayımı: ayırıcı virgül eklenir, boşluklu etikete 2 tırnak eklenir.

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 27 karakter; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu "Simple Past" (`surumler.json` `video.konu`) |
| YV-2 | evet | 640 bayt (≤ 5.000). Sıra: 1. satır değer cümlesi · 2. satır kaydet · 4–8. satır damgalar · 10. satır sıradaki ders · 11. satır bağlantı · 13. satır etiket |
| YV-3 | evet | ilk damga 0; 5 bölüm; en kısa bölüm 14,55 sn (Örnek 1). Giriş sahnesi (3 sn) kanca bölümüne birleşti |
| YV-4 | evet (D bakacak) | bölüm tablosu §3; her ad sahnede söylenen ya da yazılan içeriği taşır; iç ad yok; en uzun 38 karakter |
| YV-5 | evet | düz toplam 130; YouTube sayımıyla 158 ≤ 500. Konu "Simple Past", zaman adı "Past Simple" ve "geçmiş zaman", kitle "YDT" var; yineleme yok |
| YV-6 | evet (D bakacak) | §5 iddia tablosu. Mutlak kural ve yanlış denklik kullanmadım. Yazım taraması: emoji 0; "Tam ders", "dakika", "dk", "BASIC" yok |
| YV-7 | evet | katalog: ünite `02` "Tenses", konu GR-02-10 sıra 10; önceki `02-09-ydt-temel` (GR-02-09), sonraki `02-11-ydt-temel` (GR-02-11). Liste adı "Tenses · YDT Temel" (`kitleler.ydt` = YDT, `seviyeler.temel` = Temel) |
| YV-8 | evet (pakette srt yok) | `altyazi.srt` panelde türer (sözleşme §2). `altyazi.json` son satırı t1 = 92,81 < ders sonu 93,81 |
| YV-9 | evet | `kapak.png` pakette var, 1920×1080, açık tema (`KAPAK-RAPOR.md` satır 5). Dikey: 1080×1920, açık (satır 6). Gönderi metninde emoji 0 |

`youtube-surumu-standart.md` §3 bildirim kuralları:

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | ders 93,81 sn < 4 dk → 1 bildirim |
| Zaman ≈ %30 | kısmen | %51,0. Gerekçe §4 |
| Cümle sınırı | evet | 47,82 = `METIN.md` cümle 5 başı ("Üçüncü örnek."); önceki söz 47,27'de biter |
| İlk 30 sn / son 20 sn | evet | 47,82 ≥ 30; 47,82 + 3,0 = 50,82 ≤ 73,81 |
| `giris`, `cikis` | evet | ikisi de `true` |

## 3. Bölüm tablosu

| `t` (sn) | Damga | İç ad (`zaman.json`) | İzleyici adı | Süre (sn) |
|---|---|---|---|---|
| 0 | 00:00 | Giriş + Kanca | Türkçe -di ekinden köprü: Simple Past | 14,80 |
| 14,8 | 00:15 | Örnek 1 | Düzenli fiile -ed: I watched a movie | 14,55 |
| 29,35 | 00:29 | Örnek 2 | Düzensiz fiil: go değil, went | 18,47 |
| 47,82 | 00:48 | Örnek 3 | Olumsuz ve soru: didn't, Did you play? | 16,96 |
| 64,78 | 01:05 | Soru + Form | Neden -ed yok? Özet ve zaman ifadeleri | 29,03 |

Adların sahne kaynağı:

- Bölüm 1: cümle 1–2 ("Türkçede biten işe -di ekleriz. İngilizce de -ed ekler.").
- Bölüm 2: cümle 3 ve formül kartı `V + -ed`, `watch → watch-ed`.
- Bölüm 3: cümle 4 ("Go değil, went.").
- Bölüm 4: cümle 5 (`We didn't play football yesterday.`, `Did you play football?`).
- Bölüm 5: cümle 6 (öğrenci: "birinde -ed var, ikisinde yok. Neden?") ve cümle 7 (iki kolon düzenli/düzensiz, `yesterday · ago · last year` kutuları, formül kartı).

Damga kuralı: `youtube.json` sahne başını ondalıklı tutar; açıklamadaki damga en yakın saniyedir (`sozlesme.md` satır 147).
Giriş klibi eklenirse damgalar giriş süresi kadar kayar; araç düzeltir. Bu not açıklamaya yazılmadı.

## 4. Bildirim anı

Seçilen an: **47,82 sn** → `METIN.md` cümle 5 başı "Üçüncü örnek.". Önceki söz ("İkinci hâlini ezberlersin.") 47,27'de biter. Örnek 3 sahnesi 47,82'de açılır.

- %30 hedefi = 28,14 sn. Bu an ilk 30 sn yasağının içinde kalır.
- `METIN.md` cümle başları: 1,00 · 3,39 · 14,80 · 29,35 · 47,82 · 64,78 · 69,33. 29,35 yasak bölgede (< 30). 30 sn sonrasındaki ilk cümle başı 47,82'dir.
- Öteki adaylar: 64,78 (öğrenci sorusu; soru balonuyla çakışır) ve 69,33 (%73,9; ikinci bildirimin yeri, bu derste yok).
- Seçenek (jüri ya da şef karar verir): `altyazi.json` satır başı 30,64 sn (`My uncle went to London two years ago.`, %32,7) ya da 33,85 sn ("Amcam iki yıl önce Londra'ya gitti.", %36,1). İki an da gerçek cümle sınırıdır. Ama ikisi de `METIN.md` cümle 4'ün içinde kalır ve örneğin ekrana geldiği anı böler.
- Emsal: `simple-present-temel` aynı yolu izledi (43,91 = "Üçüncü örnek.", %47,0).

## 5. Dilbilgisi iddiaları

Benim metinlerim:

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama 1. satır | watched gibi -ed alan fiiller, went gibi düzensiz fiiller, didn't ve did ile olumsuz ve soru | kesin (örneğe bağlı, kural genellemesi yok) |
| Bölüm 1 | "Türkçe -di ekinden köprü" (denklik değil, köprü) | jüri bakacak: -di her fiile gelir, -ed yalnız düzenli fiile gelir; "köprü" sözü bu farkı örtmüyor mu |
| Bölüm 2 | düzenli fiile -ed | kesin (yazım değişkenleri lived, studied, stopped yine -ed ekidir) |
| Bölüm 3 | go → went, düzensiz | kesin |
| Bölüm 4 | didn't, Did you play? | kesin (iki örnek, kural cümlesi yok) |
| Bölüm 5 | "Neden -ed yok?" (soru) | iddia yok |
| Gönderi g1 | dersin -ed ekini, düzensiz fiilleri ve did yapısını üç örnekle gösterdiği | kesin |
| Sabit yorum | iddia yok | — |

Ana dersteki iddialar (`juri-olcutleri.md` §1c: kaynağa uygun ≠ doğru; bu dosyaları değiştirmedim):

| Yer | İddia | Hüküm |
|---|---|---|
| `METIN.md` cümle 5 ve 7 | "Olumsuzda ve soruda did gelir, fiil yalın kalır." | jüri bakacak: `be` fiili istisnadır (I wasn't, Were you…?). Temel seviyede sadeleştirme olabilir |
| `surumler.json` `canAlici` | "Türkçedeki -di = İngilizcedeki -ed" | jüri bakacak: yanlış denklik riski (düzensiz fiil -ed almaz). Yayın metnine almadım |
| `METIN.md` cümle 2 | "Simple Past'in" (ek uyumu) | jüri bakacak: okunuşa göre "Past'ın" ya da "Past'in". Kendi metinlerimde ekli biçimi kullanmadım |

## 6. Açık noktalar

1. Bildirim %51,0; %30 hedefinden uzak. 30 sn yasağı ve cümle başı kuralı 94 sn'lik derste bu anı zorlar. Seçenek §4'te.
2. Damga yuvarlaması söz başını kırpar. Bu derste sahne başı = söz başı. 14,80 → 00:15, 47,82 → 00:48, 64,78 → 01:05 damgaları sözden 0,18–0,22 sn sonra düşer. Bölüme atlayan izleyici ilk hecenin bir parçasını kaçırabilir. Kural "en yakın saniye" (`sozlesme.md` satır 147); aşağı yuvarlama bu kırpmayı önler. Karar şefte.
3. Bildirim kartı 47,82'de sahne geçişiyle aynı anda başlar (sahne 4 → 5, `gecis_kare` 12 = 0,4 sn). Nadir önizlemede bakacak.
4. Bağlantı tabanı `https://ydspublishing.com/grammar/02-10-ydt-temel` emsal kısalardan türedi; canlılığı ölçülmedi. Emsal UYARI'sı geçerli: paylaşımdan önce adresi aç.
5. Sonraki öğe `02-11-ydt-temel` katalogda `durum: planli`. Liste sırası doğru. Ama "Sıradaki ders: Past Continuous" satırı ve bitiş ekranı bu ders üretilene kadar boşa bağlanır.
6. `surumler.json` `ana-yatay` `kapak` alanı `null`. Gönderi görseli paket kökündeki `kapak.png` (`sozlesme.md` satır 147 kuralı).
7. Künyede rozet metni `YDT BASIC` (sahne katmanı). Yayın verisi dosyalarına girmedi; yazma alanım dışında.
8. Etiket "YKS": kitle YDT, YKS sınavının bir oturumudur; emsal (`simple-present-temel`) ile aynı.
9. `senaryo.json` ve `baslar.json` pakette yok. Konu adını `surumler.json` + `konu-adlari.json` + künyeden, cümle başlarını `METIN.md` sütunundan aldım.

---
Yazan: Claude Opus 5.5 (`claude-opus-5-5`), 15.11.2026.

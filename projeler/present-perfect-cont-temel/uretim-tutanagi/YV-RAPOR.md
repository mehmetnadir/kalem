# YV-RAPOR — `present-perfect-cont-temel` YouTube yayın verisi · 15.11.2026

İstem: `uretim-hatti/istemler/YV-0209T.md`. Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`). Jüri bu modelden farklı bir modelle koşmalıdır (`juri-olcutleri.md` §1e).

| Dosya | Durum |
|---|---|
| `present-perfect-cont-temel/youtube.json` | yazıldı, JSON ayrıştı |
| `present-perfect-cont-temel/youtube-aciklama.md` | yazıldı, 716 bayt |
| `present-perfect-cont-temel-dikey/youtube.json` | yazıldı, JSON ayrıştı (dikey paket var: `surumler.json` → `dikey-tam`, `proje: present-perfect-cont-temel-dikey`) |
| `present-perfect-cont-temel-dikey/youtube-aciklama.md` | yazıldı, 716 bayt, `utm_content=dikey-tam` |

Kaynaklar: `senaryo.json` (başlık "Present Perfect Continuous", kitle YDT), `zaman.json` (6 sahne, ders 83,22 sn), `ortak/anlatim/METIN.md` (cümle başları sütunu),
`altyazi.json` (23 satır), `surumler.json` (`video.etiketler`, kod `ING-YDT-GR-02-09-T`, kimlik `02-09-ydt-temel`), `D/varlik/grammar/katalog.json` (ünite 02 Tenses,
konu `GR-02-09` sıra 9), `D/varlik/grammar/konu-adlari.json` (`GR-02-10` = "Simple Past"), `ortak/kunye.js` (`seviye: "YDT BASIC"`), `KAPAK-RAPOR.md` (kapak dosyaları).

## 1. Ölçüm komutu çıktısı (iki paket aynı; ana paket satırları)

Son hâl (bölüm 5 adı ve sabit yorum düzeltmesinden sonra):

```
cümle başları (METIN.md): [1.0, 3.39, 17.68, 32.83, 47.82, 62.06, 65.97]
== present-perfect-cont-temel JSON ayrıştı; ders süresi 83.22 | boyut 1920 x 1080
baslik 42 karakter: Present Perfect Continuous | YDT İngilizce | kalıp: True
etiket sayı 13 düz toplam 155 | virgül+tırnak dahil 183 | yineleme False
  bölüm 0 → 17.13 süre 17.13 | ad 37 kr | İki saattir çalışıyorum: -dir ve -yor | sahne başı: True
  bölüm 17.13 → 32.28 süre 15.15 | ad 34 kr | Süre için for: I have been waiting | sahne başı: True
  bölüm 32.28 → 47.27 süre 14.99 | ad 38 kr | Başlangıç için since: has been playing | sahne başı: True
  bölüm 47.27 → 61.51 süre 14.24 | ad 32 kr | Sokak ıslak: It has been raining | sahne başı: True
  bölüm 61.51 → 83.22 süre 21.71 | ad 39 kr | Neden hep been? Kalıp: have been + -ing | sahne başı: True
damgalar youtube.json ile birebir (en yakın saniye): True 5
  bildirim t 32.83 sure 3.0 | oran 39.4% | ilk30 dışı True | son20 dışı True | cümle başı True
sabitYorum 134 kr; nokta sayısı 1 ? 0
gönderi g1 görsel kapak.png | ilk cümle soru True | cümle 3
emoji 0
açıklama bayt 716 | hashtag ['#YDT', '#İngilizce', '#gramer', '#PresentPerfectContinuous']
yasak söz: []
utm: ['utm_source=youtube', 'utm_medium=video', 'utm_campaign=ING-YDT-GR-02-09-T', 'utm_content=ana-yatay']
liste {'ad': 'Tenses · YDT Temel', 'sira': 9, 'onceki': '02-08-ydt-temel', 'sonraki': '02-10-ydt-temel'}
altyazı son t1: 82.3 ≤ 83.22
iki youtube.json aynı: True
present-perfect-cont-temel/kapak.png:       PNG image data, 1920 x 1080, 8-bit/color RGB, non-interlaced
present-perfect-cont-temel-dikey/kapak.png: PNG image data, 1080 x 1920, 8-bit/color RGB, non-interlaced
```

Dikey paket: aynı satırlar; tek fark `utm_content=dikey-tam` ve boyut 1080 × 1920. Dikey `zaman.json` sahne başları ana paketle aynı
(0 · 3 · 17,13 · 32,28 · 47,27 · 61,51; son 83,22), ölçüm dikey paketin KENDİ `zaman.json` dosyasıyla koştu (`sahne başı: True`).
`METIN.md` ve `altyazi.json` iki pakette bayt bayt aynı (`cmp` çıkışı 0).

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 42 karakter; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu = `senaryo.json` `baslik` ve `surumler.json` `video.konu` "Present Perfect Continuous" |
| YV-2 | evet | 716 bayt (≤ 5.000). Sıra: 1. satır değer cümlesi · 2. satır kaydet · 4. satır "Bölümler:" + 5–9. satır damgalar · 11. satır sıradaki ders · 13. satır bağlantı · 15. satır etiket |
| YV-3 | evet | ilk damga 0; 5 bölüm; en kısa bölüm 14,24 sn (Örnek 3). Giriş sahnesi (3 sn) kanca bölümüne birleşti |
| YV-4 | evet (D bakacak) | bölüm tablosu §3; her ad sahnede söylenen içeriği taşır, iç ad yok, en uzun 39 karakter |
| YV-5 | evet | düz toplam 155; YouTube sayımıyla (virgül + boşluklu etikete tırnak) 183 ≤ 500. Konu "Present Perfect Continuous", zaman adı "Present Perfect Progressive", kitle "YDT" var; yineleme yok |
| YV-6 | evet (D bakacak) | §5 iddia tablosu; mutlak kural ve yanlış denklik kullanmadım; yazım taraması: emoji 0, "Tam ders" / "dakika" / "dk" / "vb." / "örn." yok |
| YV-7 | evet | katalog: ünite `02` "Tenses", konu `GR-02-09` sıra 9; önceki `02-08-ydt-temel`, sonraki `02-10-ydt-temel`. Liste adı "Tenses · YDT Temel" (`kitleler.ydt` = YDT, `seviyeler.temel` = Temel) |
| YV-8 | evet (pakette srt yok) | `altyazi.srt` panelde türetilir (sözleşme §2). Kaynak `altyazi.json` son satırı t1 = 82,30 < ders sonu 83,22 |
| YV-9 | evet | `kapak.png` pakette var, 1920 × 1080, açık tema (`KAPAK-RAPOR.md` tablo satırı 1). Dikey pakette `kapak.png` 1080 × 1920. Gönderi metninde emoji 0 |

`youtube-surumu-standart.md` §3 bildirim kuralları:

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | ders 83,22 sn < 4 dk → 1 bildirim |
| Zaman ≈ %30 | kısmen | %39,4. Gerekçe §4 |
| Cümle sınırı | evet | 32,83 = `METIN.md` cümle 4 başı ("İkinci örnek."); önceki cümle 32,28'de biter |
| İlk 30 sn / son 20 sn | evet | 32,83 ≥ 30; 32,83 + 3,0 = 35,83 ≤ 63,22 |
| `giris`, `cikis` | evet | ikisi de `true` |

## 3. Bölüm tablosu

| `t` (sn) | Damga | İç ad (`zaman.json`) | İzleyici adı | Süre (sn) |
|---|---|---|---|---|
| 0 | 00:00 | Giriş + Kanca | İki saattir çalışıyorum: -dir ve -yor | 17,13 |
| 17,13 | 00:17 | Örnek 1 | Süre için for: I have been waiting | 15,15 |
| 32,28 | 00:32 | Örnek 2 | Başlangıç için since: has been playing | 14,99 |
| 47,27 | 00:47 | Örnek 3 | Sokak ıslak: It has been raining | 14,24 |
| 61,51 | 01:02 | Soru + Form | Neden hep been? Kalıp: have been + -ing | 21,71 |

Damga kuralı: `youtube.json` sahne başını ondalıklı tutar; açıklamadaki damga = en yakın saniye (pilotlar YV-0202T, YV-0204T ile aynı; 61,51 → 01:02).
Her damga sözden önce düşer (söz başları 17,68 · 32,83 · 47,82 · 62,06). Giriş klibi eklenirse damgalar giriş süresi kadar kayar; araç düzeltir (açıklamaya yazılmadı).

## 4. Bildirim anı

Seçilen an: **32,83 sn** → `METIN.md` cümle 4 başı "İkinci örnek." (önceki söz "Kalıp: have been, artı fiile -ing." 32,28'de biter; Örnek 2 sahnesi 32,28'de açılır,
BookFlip geçişi 12 kare = 0,40 sn → 32,68'de biter; kart geçişten sonra gelir).

- %30 hedefi = 24,97 sn. Bu an ilk 30 sn yasağının içinde kalır.
- Pakette `baslar.json` yok. Cümle başları dosyası olarak `METIN.md` "başlar" sütununu kullandım (`senaryo.json` cümleleri; `sozcukler.json` ile aynı).
- 30 sn sonrasındaki ilk cümle başı 32,83'tür. Sonrakiler 47,82 (%57) ve 62,06 (%75; son 20 sn sınırına 1,16 sn kalır).
- `altyazi.json` satır başlarında da 30 ile 32,83 arasında sınır yok (27,64 → 32,83). Daha yakın bir seçenek yok.

## 5. Dilbilgisi iddiaları

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama 1. satır | kalıp have/has been + -ing | kesin |
| Açıklama 1. satır | "süre için for, başlangıç noktası için since" | kesin (for + süre, since + başlangıç anı; "her zaman" denmedi) |
| Açıklama 1. satır, gönderi | "izi (şimdi) görünen eylem" (It has been raining, sokak ıslak) | kesin; ders cümle 5 ile aynı |
| Gönderi 2. cümle | "Türkçede -dir ve -yor ile kurduğumuz bu cümleyi İngilizce have been ve -ing ile kurar" | jüri bakacak: parça parça denklik kurmadım (ders "gibi düşün" der), ama süreyi İngilizcede `for two hours` taşır; cümle bunu söylemez |
| Bölüm 1 adı | "-dir ve -yor" köprüsü | jüri bakacak (aynı köprü; denklik iddiası yok) |
| Bölüm 2–3 adları | süre için for, başlangıç için since | kesin |
| Bölüm 5 adı | "Kalıp: have been + -ing" | kesin (tekil kişide has been; bölüm 3 adı has been taşır) |
| Etiket | "Present Perfect Progressive" = aynı zamanın öteki adı | kesin |

## 6. Açık noktalar

1. **Bağlantı tabanı:** bu dersin kısası (`present-perfect-cont-temel-s1`, v1) açıklama dosyası taşımıyor. Taban adresi ve utm biçimini öteki derslerin kısalarından aldım
   (`simple-present-temel-s1/aciklama-a.md`, `02-04-ydt-temel-s1/aciklama-a.md`: `https://ydspublishing.com/grammar/<kimlik>`, `utm_campaign` = ders kodu büyük harf).
   Adres canlılığı ölçülmedi (kısalardaki UYARI ile aynı).
2. **Gönderi görseli adı:** `surumler.json` `ana-yatay.kapak` = `null`, `dikey-tam.kapak` = metin ("PRESENT PERFECT CONTINUOUS"), dosya adı değil.
   Dosya adını `KAPAK-RAPOR.md` ve dosya listesinden aldım: `kapak.png` (açık tema). Panelin izin listesi `youtube.json` adını da okur (sözleşme §3).
3. **Bildirim %30 sapması:** %39,4; ilk 30 sn yasağı ile %30 hedefi bu kısa derste çakışır (§4). Şef ya da jüri onaylar.
4. **Ana derste dil notu (§1c, kaynağa uygun ≠ doğru):** (a) `surumler.json` `canAlici` "Türkçedeki -dir ... -yor = İngilizcedeki have been ... -ing" eşitlik
   işareti taşır; anlatım (cümle 7) "gibi düşün" der. Yayın metinlerine eşitlik koymadım. (b) Cümle 5 çevirisi "Yağmur bir süredir yağıyor" yağmurun
   sürdüğünü söyler; "The street is wet. It has been raining." yağmurun yeni dinmiş olmasına da uyar. Dil jürisi bakacak; yayın metinlerinde "izi görünen eylem" dedim.
5. **Künye rozeti:** `ortak/kunye.js` `seviye: "YDT BASIC"`; huni v2 §9 rozet metnini `YDT · TEMEL` olarak bağlar. Yayın verisini etkilemez; ilk dokunuşta düzeltilecek açık iş.
6. **Giriş klibi:** eklenirse damgalar ve bildirim giriş süresi kadar kayar; API YouTube zamanını döner, açıklamadaki damga bloğunu yeniden yazar (sözleşme §3).
7. Etiket "YKS": YDT, YKS'nin dil oturumudur; pilot `simple-present-temel` ile aynı. Jüri gereksiz bulursa çıkarılır (sınır 183/500).

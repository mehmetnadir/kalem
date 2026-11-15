# YV-RAPOR — `present-continuous` YouTube yayın verisi · 15.11.2026

İstem: `uretim-hatti/istemler/YV-0201T.md`. Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`). Jüri bu modelden farklı bir modelle koşmalıdır (`juri-olcutleri.md` §1e).
Katalog öğesi: `02-01-ydt-temel` (`katalog.json` GR-02-01, `proje: present-continuous`, `eskiKod: ING-YDT-GR-01-PC`).

| Dosya | Durum |
|---|---|
| `present-continuous/youtube.json` | yazıldı, JSON ayrıştı |
| `present-continuous/youtube-aciklama.md` | yazıldı, 677 bayt |
| `present-continuous-dikey/youtube.json` | yazıldı, JSON ayrıştı, ana paketle bayt bayt aynı (dikey paket var: `surumler.json` → `dikey-tam`, `proje: present-continuous-dikey`) |
| `present-continuous-dikey/youtube-aciklama.md` | yazıldı, 677 bayt, tek fark `utm_content=dikey-tam` (`diff` çıktısı: yalnız satır 12) |

Kaynaklar: `surumler.json` (`video.konu` "Present Continuous", `kitle` YDT, `video.etiketler`), `zaman.json` (6 sahne, ders 87,33 sn), `ortak/anlatim/METIN.md`
("başlar" sütunu = cümle başları; pakette `baslar.json` yok), `senaryo.json` (7 cümle, `kartlar`), `altyazi.json` (24 satır), `D/varlik/grammar/katalog.json`
(ünite 02 Tenses, konu sırası 1), kısa `present-continuous-s1/surumler.json` (kod `ING-YDT-GR-02-01-T-S1`), emsal kısalar `simple-present-temel-s1b/aciklama-b.md`,
`02-04-ydt-temel-s2/aciklama-a.md` (taban adres ve utm biçimi), sıradaki ders `02-02-ydt-temel/surumler.json` (`konu` "Simple Present").

## 1. Ölçüm komutu çıktısı

Komut: `/usr/bin/python3 -I /tmp/yv_olc_0201t.py` (iki paket; dikey paketin satırları ana paketle aynı, tek fark utm satırı).

```
== present-continuous JSON ayrıştı; ders süresi 87.33
baslik 34 karakter: Present Continuous | YDT İngilizce | kalıp: True
etiket sayı 13 düz toplam 136 | virgül+tırnak dahil 164 | yineleme False
  bölüm 0 → 15.44 süre 15.44 | ad 34 kr | Gidiyorum: şimdiki zamanla gelecek | sahne başı: True
  bölüm 15.44 → 30.15 süre 14.71 | ad 32 kr | Şu an süren iş: I am sitting now | sahne başı: True
  bölüm 30.15 → 45.98 süre 15.83 | ad 34 kr | Bugünlerde süren iş: this semester | sahne başı: True
  bölüm 45.98 → 62.81 süre 16.83 | ad 39 kr | Şu an işareti: Look! Listen! Watch out! | sahne başı: True
  bölüm 62.81 → 87.33 süre 24.52 | ad 34 kr | Neden hep -ing? Am, is, are + -ing | sahne başı: True
damgalar youtube.json ile birebir (round): True 5
  bildirim t 30.15 sure 3.0 | oran 34.5% | ilk30 dışı True | son20 dışı True
sabitYorum 113 kr; cümle sayısı 1
gönderi g1 görsel kapak.png | ilk cümle soru True | cümle 3
emoji 0
açıklama bayt 677 | satır 14 | hashtag ['#YDT', '#İngilizce', '#gramer', '#PresentContinuous']
yasak söz: []
utm: ['utm_source=youtube', 'utm_medium=video', 'utm_campaign=ING-YDT-GR-02-01-T', 'utm_content=ana-yatay']
liste: {'ad': 'Tenses · YDT Temel', 'sira': 1, 'onceki': None, 'sonraki': '02-02-ydt-temel'} | giris True cikis True | aciklamaDosya youtube-aciklama.md
== present-continuous-dikey … (aynı) … utm_content=dikey-tam
altyazi satır 24 son t1 85.81 ≤ 87.33: True | sıra bozuk False
present-continuous/kapak.png:       PNG image data, 1920 x 1080
present-continuous-dikey/kapak.png: PNG image data, 1080 x 1920
```

Dikey `zaman.json` sahne başları ana paketle aynı (0 · 3 · 15,44 · 30,15 · 45,98 · 62,81; son 87,33). `METIN.md`, `altyazi.json`, `senaryo.json`, `sozcukler.json`
iki pakette bayt bayt aynı (`cmp` çıkışı 0). Bu yüzden dikey `bolumler` ve `bildirimler` ana paketle aynıdır.

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 34 karakter; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu = `surumler.json` `video.konu` "Present Continuous" (`senaryo.json` `baslik` iç ad taşır, §6.6) |
| YV-2 | evet | 677 bayt (≤ 5.000). Sıra: 1. satır değer cümlesi · 2. satır kaydet · 4. satır "Bölümler:" + 5–9. satır damgalar · 11. satır sıradaki ders · 12. satır bağlantı · 14. satır etiket |
| YV-3 | evet | ilk damga 0; 5 bölüm; en kısa bölüm 14,71 sn (Örnek 1). Giriş sahnesi (3 sn) kanca bölümüne birleşti |
| YV-4 | evet (D bakacak) | bölüm tablosu §3; her ad sahnede söylenen içeriği taşır; iç ad yok; en uzun 39 karakter (≤ 40) |
| YV-5 | evet | düz toplam 136; YouTube sayımıyla (virgül + boşluklu etikete tırnak) 164 ≤ 500. Konu "Present Continuous", zaman adı "şimdiki zaman" + "Present Progressive", kitle "YDT", "İngilizce", "gramer" var; yineleme yok (büyük/küçük harf duyarsız). `video.etiketler` 4 etiketin dördü de içinde |
| YV-6 | evet (D bakacak) | §5 iddia tablosu; mutlak kural ve yanlış denklik kullanmadım. Yazım taraması: emoji 0; "Tam ders", "dakika", "dk" yok; açıklama gövdesinde açılmamış kısaltma yok (YDT yalnız başlıkta ve etikette, emsalle aynı) |
| YV-7 | evet | katalog: ünite `02` "Tenses" (`sira` 2), konu GR-02-01 `sira` 1. `kitleler.ydt` = YDT, `seviyeler.temel` = Temel → "Tenses · YDT Temel". `onceki` null (listenin ilk öğesi, §6.8), `sonraki` `02-02-ydt-temel` (GR-02-02) |
| YV-8 | evet (pakette srt yok) | `altyazi.srt` panelde türetilir (sözleşme §2). Kaynak `altyazi.json` 24 satır, sıra bozuk değil, son satır t1 = 85,81 ≤ ders sonu 87,33 |
| YV-9 | evet | `kapak.png` pakette var, 1920×1080, açık tema (`KAPAK-RAPOR.md` tablo satırı 1: `kapak.png` · `kapak-koyu.png` = açık · koyu). Gönderi metninde emoji 0 |

`youtube-surumu-standart.md` §3 bildirim kuralları:

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | ders 87,33 sn < 4 dk → 1 bildirim |
| Zaman ≈ %30 | kısmen | %34,5. Gerekçe §4 (%30 anı ilk 30 sn yasağına düşer) |
| Cümle sınırı | evet | 30,15 = `METIN.md` cümle 4 başı ("İkinci örnek."); önceki cümle 29,60'ta biter |
| İlk 30 sn / son 20 sn | evet | 30,15 ≥ 30; 30,15 + 3,0 = 33,15 ≤ 87,33 − 20 = 67,33 |
| `giris`, `cikis` | evet | ikisi de `true` |
| Ses | evet | `youtube.json` ses alanı taşımaz |

## 3. Bölüm tablosu

| `t` (sn) | Damga | İç ad (`zaman.json` `bolum`) | İzleyici adı | Süre (sn) | Sahnede söylenen (`METIN.md`) |
|---|---|---|---|---|---|
| 0 | 00:00 | giris + kanca | Gidiyorum: şimdiki zamanla gelecek | 15,44 | c1 "Bu akşam amcamlara gidiyorum." · c2 "Türkçede şimdiki zamanla geleceği anlatırız. İngilizce de aynısını yapar." · kart `I'm going to my uncle's tonight.` |
| 15,44 | 00:15 | ornek1 | Şu an süren iş: I am sitting now | 14,71 | c3 "I am sitting in front of the camera now. … Olay tam konuşma anında sürüyor." |
| 30,15 | 00:30 | ornek2 | Bugünlerde süren iş: this semester | 15,83 | c4 "My sister is taking piano lessons this semester. … Ama bu günlerde süren bir iş." |
| 45,98 | 00:46 | ornek3 | Şu an işareti: Look! Listen! Watch out! | 16,83 | c5 "Look! The cat is climbing the tree. … Look, listen, watch out gibi sözcükler olayın tam şu anda olduğunu söyler." |
| 62,81 | 01:03 | form | Neden hep -ing? Am, is, are + -ing | 24,52 | c6 öğrenci "Neden hep -ing?" · c7 "Be fiili ise zamanı taşır: am, is, are şimdiki zaman demek." |

Damga kuralı: `youtube.json` sahne başını kesirli tutar; açıklamadaki damga en yakın saniyedir (sözleşme `K/.claude/docs/sozlesme.md` satır 147; iki pilotla aynı).
Bu pakette her cümle kendi sahnesinin başında başlar, bu yüzden iki damga sözden az sonra düşer: 45,98 → 00:46 ("Üçüncü" 45,98'de başlar, 0,02 sn kayıp) ve
62,81 → 01:03 ("Hocam" 62,81–63,53; ilk 0,19 sn kaçar). Aşağı yuvarlama ise önceki cümlenin son sözüne düşer (00:45 → "-ing." 44,63–45,43; 01:02 → "yapı." 61,51–62,26).
Tutarlılık için en yakın saniye kaldı; karar §6.3. Giriş klibi eklenirse damgalar giriş süresi kadar kayar; API yeniden yazar (açıklamaya yazılmadı).

## 4. Bildirim anı

Seçilen an: **30,15 sn** → `METIN.md` cümle 4 başı "İkinci örnek." (önceki söz "Be fiili, artı fiile -ing." 29,60'ta biter, 0,55 sn sessizlik; sahne 4 `04-canvas-ornek2` 30,15'te açılır).

| Aday (cümle başı) | Oran | Durum |
|---|---|---|
| 15,44 (c3) | %17,7 | ilk 30 sn yasağı |
| **30,15 (c4)** | **%34,5** | izinli; %30'a en yakın |
| 45,98 (c5) | %52,6 | izinli; daha uzak |
| 62,81 (c6) | %71,9 | izinli (65,81 ≤ 67,33); daha uzak |
| 66,72 (c7) | %76,4 | son 20 sn yasağı (69,72 > 67,33) |

- %30 hedefi = 26,20 sn. Bu an ilk 30 sn yasağının içinde kalır ve cümle 3'ün ortasına düşer ("İki parça var: am ve sitting.", parça 23,29–26,89).
- Kural birleşimi sözleşme satır 148 ile aynı: %30 anı yasak bölgedeyse 30 sn sonrasındaki ilk cümle başı.
- Seçenek (görsel jüri karar verir): 30,15 sahne 3 → 4 `BookFlip` geçişiyle (12 kare) aynı andadır. Kart geçişle çakışırsa `altyazi.json` satır başı 31,44
  ("My sister is taking piano lessons this semester.", %36,0) gerçek söz sınırıdır, ama cümle 4'ün içinde kalır.

## 5. Dilbilgisi iddiaları

Benim metinlerim:

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama 1. satır | be fiili + -ing formu; şu an süren iş; bugünlerde süren iş; Look! gibi işaret sözcükleri | kesin (üçü derste gösterilir; "her zaman" iddiası yok) |
| Bölüm 1 | "Gidiyorum: şimdiki zamanla gelecek" | jüri bakacak: İngilizcede Present Continuous yalnız kararlaştırılmış yakın gelecek için kullanılır; ad "her gelecek" demez, ama ayrımı da yapmaz. Ders cümle 2 aynı genellikte konuşur |
| Bölüm 2 | I am sitting now = şu an süren iş | kesin |
| Bölüm 3 | this semester = bugünlerde süren (geçici) iş | kesin. Yazım: "bugünlerde" TDK'de bitişik zarf; senaryo "bu günlerde" ayrı yazar → jüri bakacak |
| Bölüm 4 | Look! Listen! Watch out! = şu an işareti | kesin (işaret der, kural demez); jüri bakacak: "Watch out!" sonrasında başka zaman da gelebilir (Watch out! You'll fall.) |
| Bölüm 5 | Present Continuous formu am, is, are + -ing | kesin |
| Gönderi | "Bu akşam amcamlara gidiyorum" İngilizcede kurulur (derste: I'm going to my uncle's tonight.); be fiili + -ing üç örnekte (am sitting, is taking, is climbing) | kesin |
| Sabit yorum | dilbilgisi iddiası yok | — |

Ana dersteki iddialar (benim metnime girmedi; `juri-olcutleri.md` §1c gereği raporluyorum):

| Yer | İddia | Hüküm |
|---|---|---|
| Senaryo cümle 2 | "Bu derste … altı kullanımını görüyoruz." | jüri bakacak: ders 3 örnek + kanca gösterir (şu an, bugünlerde, Look!, gelecek); altı kullanım yok. Açıklamaya "altı" yazmadım |
| Senaryo cümle 2 | "Türkçede şimdiki zamanla geleceği anlatırız. İngilizce de aynısını yapar." | jüri bakacak: kısmi denklik; İngilizcede yalnız plan/düzenleme için |
| Senaryo cümle 7 | "-ing devam eden işi gösterir" | jüri bakacak: süreklilik be + -ing birleşimiyle gelir; -ing tek başına isim-fiil de olur (Swimming is fun.) |
| Senaryo cümle 7 + `canAlici` 1 | "-ing ekini Türkçedeki -yor gibi düşün" · "Türkçedeki -yor = İngilizcedeki -ing" | jüri bakacak: yanlış denklik riski; -yor durum fiilleriyle de gelir (biliyorum = I know, I am knowing değil). Senaryo "gibi" der, `canAlici` "=" der |
| `kunye.js` `KUNYE.seviye`, `senaryo.json` `giris.rozetler` | "YDT BASIC" · "YDT · BASIC" | huni v2 §9 açık işi (`YDT · TEMEL`); yayın verisine girmedi |

## 6. Açık noktalar

1. **Dikey sürüm Shorts sayılır.** Dikey ders 87,33 sn (≤ 3 dk). Sözleşme satır 148: bölüm ve bildirim Shorts'ta işlemeyebilir → şef kararı.
2. Bildirim 30,15 sahne geçişiyle aynı anda (§4); seçenek 31,44. Dikey bildirim yeri ayrıca ölçülecek (YT §3); kare çekmedim (render yok kuralı).
3. Damga yuvarlama: iki damga sözün ilk 0,02 ve 0,19 sn'sini kaçırır (§3). Betik kapısı ya da API aracı "en yakın saniye, söz başını geçerse aşağı" kuralını seçerse
   01:03 → 01:02 olur. Karar şefte; giriş klibi eklenince araç zaten yeniden yuvarlar.
4. **Ders kodu iki yerde farklı.** `surumler.json` `video.kod` = `ING-YDT-GR-01-PC` (katalogda `eskiKod`). `utm_campaign` için katalog `kod` ve kısa s1 yazımı
   `ING-YDT-GR-02-01-T` alındı. `surumler.json` yazma alanım dışında; güncellenmedi. Paketler arası utm betiği (`juri-olcutleri.md` §3.4) bu farkı görmelidir.
5. Kısa `present-continuous-s1` paketinde `aciklama-a.md` / `aciklama-b.md` yok (huni v2'ye çevrilmemiş). Taban adres `https://ydspublishing.com/grammar/02-01-ydt-temel`
   emsal kısaların kalıbından türedi; canlılığı ölçülmedi.
6. `senaryo.json` `baslik` = "Present Continuous — etkileşim önizleme 3" (prototip iç adı). Başlıkta `surumler.json` `video.konu` kullanıldı.
7. Başlık çakışması: `present-continuous-ileri` (02-01-ydt-ileri) aynı kalıpla aynı başlığı alır; ileri dersin YV işinde ayrım gerekir.
8. `liste.onceki` null: ders "Tenses · YDT Temel" listesinin ilk öğesi. Katalogda önceki konu GR-01-26 (`01-26-ydt-temel`) "Pronouns" listesindedir; listeler arası zincir istenirse o kimlik yazılır.
9. Gönderi g1 dikey pakette de var (istem gereği); dikey `kapak.png` 1080×1920. Öneri: gönderiyi yalnız ana sürümden paylaş.
10. Ders süresi 87,33 sn; skill `motion-grafik-ders` yatay hedefi 5–7 dk. Paket prototip 4 pilotudur (katalog `not`); YouTube'da kısa bir ders olarak çıkar.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0201T).

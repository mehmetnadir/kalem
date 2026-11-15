# YV-RAPOR — present-continuous-ileri YouTube yayın verisi · 15.11.2026 (istem YV-0201I)

| Dosya | Durum |
|---|---|
| `present-continuous-ileri/youtube.json` | yazıldı, JSON ayrıştırıldı (`json.tool`) |
| `present-continuous-ileri/youtube-aciklama.md` | yazıldı, 587 bayt, `utm_content=ana-yatay` |
| `present-continuous-ileri-dikey/youtube.json` | yazıldı; ana paketle bayt bayt aynı (`cmp` farksız) |
| `present-continuous-ileri-dikey/youtube-aciklama.md` | yazıldı, 587 bayt; tek fark `utm_content=dikey-tam` (`diff` 1 satır) |

Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`), sunucu oturumu (srv21). Jüri (YVJ) farklı modelle koşmalı (`juri-olcutleri.md` §1e).
Dikey paket: VAR (`present-continuous-ileri-dikey`; ana `surumler.json` `dikey-tam` satırı `proje` alanı). Dikey `zaman.json` dosyası
ana dosyadan farklıdır (genişlik, sahne alanları), ama 6 sahnenin `t_bas`/`t_son` değerleri aynıdır. Dikey `ortak/anlatim` ana pakete
bağdır (`readlink`). `bolumler` ve `bildirimler` dikeyin kendi dosyalarından hesaplandı; değerler aynı çıktı.

## 1. Ölçüm çıktısı (betik `/tmp/yv_olc_0201i.py`, iki paket için aynı)

```
== present-continuous-ileri JSON OK; ders süresi 84.96
YV-1 baslik 34 kr True
YV-5 etiket 6 ham kr 54 YouTube sayımı 63 yineleme False
YV-3 bölüm 5 ilk 0.0 süreler [15.25, 14.33, 12.49, 12.01, 30.88] min 12.01 hepsi sahne başı True ad kr [32, 33, 23, 32, 38]
damga birebir (round) True 5
YV-2 açıklama bayt 587 kr 558 hashtag 5 utm ['ana-yatay'] ilk satır kr 78
bildirim 30.13 %35.5 cümle başı [4] önceki cümle biter 29.66 ilk30 dışı True son20 dışı True
cümle başları {1: 0.64, 2: 3.71, 3: 15.8, 4: 30.13, 5: 42.62, 6: 54.63, 7: 60.4}
altyazı son t1 83.96 <= süre True
emoji False
gorsel var [True]
sabitYorum cümle 1 gönderi cümle 3 gönderi soru ile başlar True
yasak söz []
YV-7 ünite Tenses konu GR-02-01 sira 1 liste {'ad': 'Tenses · YDT İleri', 'sira': 1, 'onceki': None, 'sonraki': '02-02-ydt-ileri'}
   sonraki konu GR-02-02 [('02-02-ydt-ileri', 'uretimde')]
== present-continuous-ileri-dikey … (aynı değerler; utm ['dikey-tam'])
JSON-AYNI
```

Ders süresi = `zaman.json` son `t_son` = 84,96 sn. Pakette mp4 yok (render yasak); süre mp4 ile karşılaştırılmadı.

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 34 karakter; kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu = `senaryo.json` `baslik` ve katalog `konu-adlari.json` GR-02-01 ("Present Continuous"); kitle `surumler.json` `kitle` "YDT" |
| YV-2 | evet (D bakacak) | 587 bayt (≤ 5.000). Sıra: değer cümlesi → kaydet satırı → "Bölümler:" + 5 damga → "Sıradaki ders" → "Ders sayfası" (utm) → 5 etiket. İlk satır 78 karakter ("daha fazla" öncesine sığar) |
| YV-3 | evet | ilk damga 00:00; 5 bölüm; en kısa bölüm 12,01 sn ("Planlı gelecek"). Her `t` bir sahne `t_bas` değeri. Giriş (3 sn) Kanca ile birleşti |
| YV-4 | evet (D bakacak) | iç ad yok ("Örnek", "Kanca", "Soru + Form" taraması boş); en uzun ad 38 karakter (≤ 40). Ad ↔ içerik eşlemesi §3 |
| YV-5 | evet | 6 etiket, ham 54 karakter; YouTube sayımı (boşluklu etikete 2 tırnak + virgüller) 63 (≤ 500); yineleme yok. Konu ve zaman adı EN "Present Continuous", TR "şimdiki zaman"; kitle "YDT"; "İngilizce", "gramer" var |
| YV-6 | evet (D bakacak) | mutlak kural sözü ("her zaman", "asla") yok; iddialar §5. Yazım denetimi elle yapıldı (ek uyumu notu §5) |
| YV-7 | evet | katalog ünite 02 "Tenses"; konu GR-02-01 `sira` 1 → `liste.sira` 1; `onceki` null (ünitenin ilk konusu); `sonraki` `02-02-ydt-ileri` (GR-02-02, `uretimde`). Liste adı `<Ünite> · <kitle> <seviye>`, seviye katalog `seviyeler.ileri` = "İleri" |
| YV-8 | evet (pakette srt yok) | `altyazi.json` 21 satır, ilk `t0` 0,64, son `t1` 83,96 ≤ 84,96. `altyazi.srt` paneli türetir |
| YV-9 | evet | `gorsel` = `kapak.png`; dosya iki pakette var (ana 1920×1080, dikey 1080×1920; açık tema, `KAPAK-RAPOR.md`). Gönderi, sabit yorum, açıklamada emoji yok (Unicode `So` taraması boş) |

## 3. Bölüm tablosu

| Sahne (iç ad) | İzleyici adı | `t` (sn) | Damga | Süre (sn) | İçerik (`altyazi.json`) |
|---|---|---|---|---|---|
| 1 Giriş + 2 Kanca (birleşti; Giriş 3 sn) | Formül: am / is / are + verb-ing | 0,00 | 00:00 | 15,25 | "Formül tek satır. Subject, plus am, is, are, plus verb-ing." |
| 3 Örnek 1 | Şu anda süren iki iş: is sleeping | 15,25 | 00:15 | 14,33 | "The baby is sleeping … while I am talking … İki iş de şu anda sürüyor." |
| 4 Örnek 2 | Geçici durum: this week | 29,58 | 00:30 | 12,49 | "… we are staying at my uncle's house this week … Geçici bir durum." |
| 5 Örnek 3 | Planlı gelecek: tomorrow morning | 42,07 | 00:42 | 12,01 | "We are taking the bus to Izmir tomorrow morning … Planlı gelecek." |
| 6 Soru + Form | Tuzak: durum fiilleri ve always + -ing | 54,08 | 00:54 | 30,88 | öğrenci "I am knowing the answer olmaz mıydı?"; öğretmen durum fiilleri + "He is always losing his keys." |

Damga kuralı: `t` en yakın saniyeye yuvarlanır (pilot `02-04-ydt-temel` ile aynı). 29,58 → 00:30: aşağı yuvarlama (00:29) cümle 3'ün son
sözüne ("gösterir.", biter 29,66) düşer. 15,25 → 00:15: cümle 2'nin son 0,25 sn'si duyulur, sonra "Birinci kök." (15,80) gelir.
Bölüm adı "verb-ing" dersin söylediği biçimdir (cümle 2); `surumler.json` amaçlarındaki "V-ing" kısaltması kullanılmadı.

## 4. Bildirim anı

| # | `t` (sn) | Ders payı | Cümle sınırı | Ekranda |
|---|---|---|---|---|
| 1 | 30,13 | %35,5 | cümle 4 başı (cümle 3 biter 29,66; ara 0,47 sn) | sahne 4 "Örnek 2" (başı 29,58); söz "İkinci kök." |

- Ders < 4 dk (84,96 sn) → 1 bildirim. Kart 30,13–33,13 sn; son 20 sn sınırı 64,96 aşılmaz.
- **Çakışma:** %30 hedefi 25,49 sn'dir; bu an "ilk 30 sn" yasağının içindedir. İzinli pencere [30,00 · 61,96] içindeki cümle başları:
  30,13 (%35,5) · 42,62 (%50,2) · 54,63 (%64,3) · 60,40 (%71,1). %30'a en yakın 30,13 seçildi. Formül ve 1. kök anlatılmıştır
  ("ilk bilgi verildikten sonra" şartı karşılanır). Pay 30 sn'nin 0,13 sn üstündedir.
- Cümle başları dosyası: pakette `baslar.json` YOK. Cümle başları `altyazi.json` içinde her `cumle` değerinin ilk `t0` değerinden türetildi.
  Yöntem `02-04-ydt-temel` üzerinde sınandı: o paketin `altyazi.json` ilk `t0` değerleri `baslar.json` başlangıçlarıyla birebir aynı (1,0 · 6,91 · 20,77 · 44,4 · 69,39 · 93,9).
- Kart yeri (`yer.json` sol alt) ile sahne 4 öğelerinin çakışması kareyle ölçülmedi (render yok): görsel jüri bakacak.

## 5. Dilbilgisi iddiaları

| Metin | İddia | Hüküm |
|---|---|---|
| Açıklama 1. satır | ders Present Continuous'u üç sınav köküyle gösterir ve durum fiili tuzağını tanıtır | kesin (cümle 2 "formülü, üç sınav kökünü ve bir tuzağı görüyoruz"; cümle 7). "Üç kullanım" yazılmadı: derste dördüncü kullanım (always + -ing) da var |
| Açıklama 1. satır, yazım | "Present Continuous'u": okunuş /kənˈtɪnjuəs/, son ünlü "u" → belirtme eki "'u" | jüri bakacak (yabancı ad ek uyumu) |
| Bölüm "Formül: am / is / are + verb-ing" | formül | kesin (cümle 2) |
| Bölüm "Şu anda süren iki iş: is sleeping" | is sleeping şu anda süren işi anlatır | kesin (cümle 3 "İki iş de şu anda sürüyor") |
| Bölüm "Geçici durum: this week" | are staying … this week geçici durumu anlatır | kesin (cümle 4) |
| Bölüm "Planlı gelecek: tomorrow morning" | are taking … tomorrow morning planlı geleceği anlatır | kesin (cümle 5) |
| Bölüm "Tuzak: durum fiilleri ve always + -ing" | iki konu sınav tuzağıdır | kesin (cümle 7 "Sınavda ikisi de çıkar"); ad kural iddiası taşımaz |
| Gönderi 2. cümle | know bir durum fiilidir; "I am knowing" yerine "I know the answer" | kesin (cümle 7; know durum anlamında -ing almaz) |
| Gönderi 1. ve 3. cümle | soru; dersin içerik özeti | kesin |
| Sabit yorum | kaydet teşviki + damgalar; iddia yok | kesin |
| "Sıradaki ders: Simple Present" | GR-02-02'nin konusu | kesin (`konu-adlari.json` GR-02-02 "Simple Present", güven yüksek; katalog `02-02-ydt-ileri`) |

**Ana ders gözlemi (`juri-olcutleri.md` §1c; YV metinlerine taşınmadı, jüri bakacak):**
- Cümle 3 "While, tam anı gösterir.": while iki işin aynı zaman diliminde sürdüğünü bağlar; "tam an" ifadesi belirsiz.
- Cümle 7 "Always artı -ing şikâyettir.": genellikle şikâyet ya da yakınmadır; olumlu bağlamda da kullanılır ("She is always helping people"). Mutlak söz.
- Cümle 7 "Know, believe, own, belong durum fiilidir, -ing almaz." ve "Kod: olay -ing alır, durum almaz.": durum anlamı için doğru; bazı durum fiilleri eylem anlamında -ing alır (think, have). Basitleştirme.

## 6. Açık noktalar

- **Başlık çakışması (ölçüldü):** temel ders `present-continuous/youtube.json` (başka oturum, 15.11 23:32) başlığı da
  "Present Continuous | YDT İngilizce". Kalıp seviye içermez; aynı kanalda iki video aynı başlığı alır. Liste adları ayrıdır
  (`Tenses · YDT Temel` / `Tenses · YDT İleri`). Kalıba seviye eklenmesi sözleşme kararıdır; karar şefte.
- **Kısa paketinde açıklama yok:** `present-continuous-ileri-s1` içinde `aciklama-*.md` ya da utm geçen dosya yok. Bağlantı tabanı ve utm biçimi
  emsalden alındı: `02-04-ydt-temel-s1/aciklama-a.md` ve `02-02` kısaları (`https://ydspublishing.com/grammar/<katalog kimliği>`, büyük harf
  `utm_campaign`). Katalog kimliği `02-01-ydt-ileri` (`senaryo.json` `meta.kimlik`), ders kodu `ING-YDT-GR-02-01-I` (`meta.kod`).
- Ders sayfası adresinin canlılığı ölçülmedi (emsal kısa açıklamasındaki UYARI aynen geçerli: grammar-kapi Worker 11.11'de yayında değil).
- Giriş klibi (3 sn) eklenirse açıklama damgaları ve bölüm `t` değerleri kayar; araç düzeltir (sözleşme §2). Açıklamaya bu not yazılmadı.
- `liste.onceki` null: liste ünite kapsamlıdır, GR-02-01 ünitenin ilk konusudur. Önceki ünitenin son dersine bağ gerekiyorsa sözleşme kararı.
- `sonraki` = `02-02-ydt-ileri` katalogda `uretimde`; YouTube'a yüklenene kadar bitiş ekranı bağı boş kalır.
- `surumler.json` `kapak` alanı ana-yatay için `null`, dikey-tam için metin ("PRESENT CONTINUOUS"), dosya adı değil. Gönderi görseli paket kökündeki
  `kapak.png` (açık tema). Dikey pakette aynı ad 1080×1920 kapağı gösterir; topluluk gönderisinde hangisinin kullanılacağı panel/şef kararı.
- Etiket "ileri" (`surumler.json`'dan) genel bir sözcük; arama değeri düşük. Kaldırılmadı (kaynak etiket).
- Künye `seviye: "YDT ADVANCED"` (İngilizce). Başlıkta ve listede kitle "YDT", seviye katalogdan "İleri"; çakışma yok.
- Ders 85 sn; skill `motion-grafik-ders` istek künyesindeki yatay ders hedefi 5–7 dk değil. Bölüm ve bildirim kuralları bu süreyle karşılandı.
- Ölçüm betiği `/tmp/yv_olc_0201i.py` scratchpad'dedir; repoya girmedi. Kart yeri, ses ve dikey bildirim yeri mp4 olmadan ölçülemez.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0201I).

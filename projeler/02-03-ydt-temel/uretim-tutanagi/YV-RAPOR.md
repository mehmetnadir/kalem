# YV-RAPOR — 02-03-ydt-temel YouTube yayın verisi · 15.11.2026 (istem YV-0203T)

| Dosya | Durum |
|---|---|
| `02-03-ydt-temel/youtube.json` | yazıldı, JSON ayrıştırıldı (`json.load` OK) |
| `02-03-ydt-temel/youtube-aciklama.md` | yazıldı, 968 bayt, `utm_content=ana-yatay` |
| Dikey paket | **dikey paket yok**: `projeler/02-03-ydt-temel-dikey/` dizini yok; `surumler.json` yalnız `ana-yatay` sürümünü taşır |

Üretici model: **Claude Opus 5.5** (`claude-opus-5-5`), sunucu oturumu (srv21). Jüri (YVJ) farklı modelle koşmalı (`juri-olcutleri.md` §1e).
Kısa paketi de yok (`02-03-ydt-temel-s1` … yok). Bağlantı tabanı ve utm biçimi `02-04-ydt-temel-s1/aciklama-a.md` emsalinden türedi.

## 1. Ölçüm çıktısı (betik, `/usr/bin/python3 -I`)

```
JSON OK
ders süresi 280.43 | dikey paket False ['ana-yatay']
YV-1 baslik 71 kr True
YV-5 etiket 9 ham 115 YouTube sayımı 133 yineleme False
YV-3 bölüm 13 ilk 0.0 min süre 10.09 sahne başı True max ad kr 37
damga birebir True 13
YV-2 açıklama bayt 968 karakter 929 ilk satır kr 106 hashtag 5 utm ['utm_source=youtube', 'utm_medium=video',
     'utm_campaign=ING-YDT-GR-02-03-T', 'utm_content=ana-yatay']
bildirim 88.25 %31.5 cümle başı 8 ilk30 True son20 True
bildirim 188.29 %67.1 cümle başı 14 ilk30 True son20 True
emoji [] | gorsel var [True]
yasak söz []
```

- Ders süresi = `zaman.json` son `t_son` (280,43 sn = 4:40). Pakette mp4 yok; `ffprobe` ölçümü yapılmadı (render yasağı).
- "yasak söz" taraması: `Tam ders`, `dakika`, ` dk`, `BASIC`, `vb.`, `Örnek 1`, `Karşıt çift`, `Soru anı`, `Kural kartı` (açıklama + `youtube.json`).
- YouTube etiket sayımı: boşluklu etikete 2 tırnak + virgüller (en kötü durum).

## 2. `juri-olcutleri.md` §2f öz denetimi

| Kimlik | Hüküm | Kanıt |
|---|---|---|
| YV-1 | evet | 71 karakter (≤ 100). Kalıp `<Konu> \| YDT İngilizce` eşleşti. Konu = `surumler.json` `video.konu` ("Present Continuous ve Simple Present: ayrım alıştırması"; BRIEF künyesi de aynı). Kitle `YDT` (`surumler.json`, `senaryo.json`) |
| YV-2 | evet (dil kısmı D) | 968 bayt (≤ 5.000). Sıra: değer cümlesi (satır 1, 106 karakter) → kaydet satırı → `Bölümler:` + 13 damga → `Sıradaki ders` → `Ders sayfası` (utm) → 5 etiket |
| YV-3 | evet | ilk damga 00:00; 13 bölüm (≥ 3); en kısa bölüm 10,09 sn (Kapanış, 270,34 → 280,43). Yuvarlanmış damgayla en kısa aralık 04:30 → 280,43 = 10,43 sn. Her `t` bir sahne `t_bas` değeri |
| YV-4 | evet (D bakacak) | iç ad kalmadı (taramada `Örnek 1`, `Karşıt çift`, `Soru anı`, `Kural kartı` yok); en uzun ad 37 karakter (≤ 40). Ad ↔ cümle eşlemesi §3 |
| YV-5 | evet | 9 etiket, ham 115 karakter, YouTube sayımı 133 (≤ 500); yineleme yok. Konu adı, zaman adları (EN + TR), kitle, `İngilizce`, `gramer` var |
| YV-6 | evet (D bakacak) | mutlak kural sözü yok ("her zaman", "asla" yok; gönderide "çoğunlukla"). İddialar §5 tablosunda. Yazım denetimi elle yapıldı |
| YV-7 | evet | katalog ünite `02` ad `Tenses`; konu `GR-02-03` `sira` 3 → `liste.sira` 3. Önceki `GR-02-02` YDT temel = `02-02-ydt-temel` (uretimde), sonraki `GR-02-04` YDT temel = `02-04-ydt-temel` (uretimde). Liste adı `Tenses · YDT Temel` = 02-04 emsaliyle aynı |
| YV-8 | evet (pakette srt yok) | `altyazi.json` 52 satır, ilk `t0` 1,00, son `t1` 280,01 ≤ 280,43. `altyazi.srt` paneldedir (sözleşme §2) |
| YV-9 | evet | `gorsel` = `kapak.png`; dosya var, 1920×1080 (`file`), açık tema (`KAPAK-RAPOR.md`). Gönderi, sabit yorum ve açıklamada emoji yok (Unicode `So` taraması boş) |

## 3. Bölüm tablosu

| Sahne (iç ad) | İzleyici adı | `t` (sn) | Damga | Süre (sn) | Cümle (`METIN`) |
|---|---|---|---|---|---|
| 1 Giriş + 2 Kanca (birleşti; Giriş 3 sn) | Aynı fiil, iki zaman: sinyal sözcüğü | 0,00 | 00:00 | 15,31 | 1–2 |
| 3 Örnek 1 | Planlı gelecek: are leaving | 15,31 | 00:15 | 17,69 | 3 |
| 4 Örnek 2 | Geçici dönem: these days | 33,00 | 00:33 | 18,57 | 4 |
| 5 Örnek 3 | Değişim: nowadays, harder and harder | 51,57 | 00:52 | 16,99 | 5 |
| 6 Soru anı 1 | Neden -ing? Plan, dönem, değişim | 68,56 | 01:09 | 19,14 | 6–7 |
| 7 Kural kartı | Karar kartı: now, these days, usually | 87,70 | 01:28 | 21,83 | 8 |
| 8 Karşıt çift 1 | Tek cümlede iki zaman: usually ve now | 109,53 | 01:50 | 21,13 | 9 |
| 9 Karşıt çift 2-3 | Kartpostal: geçici mi, genel mi? | 130,66 | 02:11 | 36,86 | 10–11 |
| 10 Tuzak ve soru anı 2 | Tuzak: sinyal var, -ing yok | 167,52 | 02:48 | 20,02 | 12–13 |
| 11 Tuzak fiilleri | Believe, recommend, have: -ing tuzağı | 187,54 | 03:08 | 37,31 | 14 |
| 12 Ara özet | Özet: hangi sinyal, hangi zaman? | 224,85 | 03:45 | 15,51 | 15 |
| 13 Mini soru | Mini soru: now ile hangi şık? | 240,36 | 04:00 | 29,98 | 16–18 |
| 14 Kapanış | Sınavda iki adım: sinyal, sonra fiil | 270,34 | 04:30 | 10,09 | 19 |

- Sahne 1 (3 sn) 10 sn sınırının altında → sahne 2 ile birleşti. Cümle 1 zaten iki sahneye yayılır (1,00–5,00).
- "Karar kartı" iç ad değildir: anlatım cümle 8 bu sözle başlar. İç ad `Kural kartı` (zaman.json) kullanılmadı.
- Damga kuralı: en yakın saniye (sözleşme `K/.claude/docs/sozlesme.md` satır 147). Yan etki: 04:00 (240,36 → 240) ve 04:30 (270,34 → 270)
  aşağı yuvarlanır; önceki cümlenin son ≈ 0,4 sn'si duyulur (cümle 15 biter 240,36; cümle 18 biter 270,34). İçerik kaçmaz.
- Kapanış bölümü 10,09 sn ile sınıra yakın. YouTube sürümünde çıkış klibi (20 sn) bu bölüme eklenir; YouTube sayımında sınır sorunu doğmaz.

## 4. Bildirim anları

| # | `t` (sn) | Ders payı | Cümle sınırı (`baslar.json`) | Kart aralığı | Ekranda ve seste |
|---|---|---|---|---|---|
| 1 | 88,25 | %31,5 | cümle 8 başı (cümle 7 biter 87,70; ara 0,55 sn) | 88,25–91,25, sahne 7 içinde | sahne 7 kural kartı; söz "Karar kartı. Bu cümlelerde now net bir ipucudur…" |
| 2 | 188,29 | %67,1 | cümle 14 başı (cümle 13 biter 187,54; ara 0,75 sn) | 188,29–191,29, sahne 11 içinde | sahne 11; söz "Olmaz. Believe ve think bu anlamda geniş zamanla gelir." |

- Ders ≥ 4 dk (280,43 sn) → 2 bildirim. İlk 30 sn ve son 20 sn (260,43 sonrası) dışında.
- %30 hedefi 84,13 sn. `baslar.json` adayları: 73,94 (%26,4) ve 88,25 (%31,5). 88,25 daha yakın; üç örnek, öğrenci sorusu ve cevabı bitmiş ("ilk bilgi verildikten sonra").
- %70 hedefi 196,30 sn. Adaylar: 188,29 (%67,1) ve 225,40 (%80,4). 188,29 daha yakın.
- `sozcukler.json` cümle 14 içinde gerçek cümle başları vardır: 195,60 ("We are believing." %69,8) ve 197,29 ("Denmez." %70,4).
  Bunlar `baslar.json` birimi değildir; istem ve sözleşme `baslar.json` der, kullanılmadı.
- Geçiş: iki sahne de BookFlip ile başlar (12 kare = 0,4 sn). Kartlar geçiş bittikten sonra girer (87,70 + 0,4 < 88,25; 187,54 + 0,4 < 188,29).
- Kartın sol alt yerinde (`ortak/youtube/bildirim/yer.json`) sahne 7 ve sahne 11 öğesiyle çakışma ölçülmedi: mp4 yok. Görsel jüri kareyle bakacak.

## 5. Dilbilgisi iddiaları

| Metin | İddia | Hüküm |
|---|---|---|
| Başlık | "ayrım alıştırması"; iddia yok | kesin |
| Açıklama 1. satır | seçim sinyal sözcüğüne ve fiile bakarak yapılır | kesin (cümle 1, 8, 19; `canAlici` 1) |
| Bölüm "Aynı fiil, iki zaman: sinyal sözcüğü" | karar sinyal sözcüğündedir | kesin (cümle 1) |
| Bölüm "Planlı gelecek: are leaving" | kişisel plan gelecek için şimdiki zamanla gelir | kesin (cümle 3; kural kartı cümle 8) |
| Bölüm "Geçici dönem: these days" | these days geçici bir dönem gösterir | kesin (cümle 4) |
| Bölüm "Değişim: nowadays, harder and harder" | iki ipucu; değişimi `harder and harder` söyler | kesin (cümle 5) |
| Bölüm "Neden -ing? Plan, dönem, değişim" | üç örnekte üç ipucu | kesin (cümle 6–7) |
| Bölüm "Karar kartı: now, these days, usually" | yalnız sözcük listesi; iddia yok | kesin |
| Bölüm "Tek cümlede iki zaman: usually ve now" | bir cümlede iki zaman olur | kesin (cümle 9: `usually spends … is meeting … now`) |
| Bölüm "Tuzak: sinyal var, -ing yok" | sinyal olsa da -ing gelmeyen durum var | kesin (cümle 12 sözü aynen; bağlam `We believe this situation is temporary.`) |
| Bölüm "Believe, recommend, have: -ing tuzağı" | üç fiil -ing tuzağı kurar | jüri bakacak (ad "have"in yalnız "sahip olmak" anlamında -ing almadığını söylemez; cümle 14 bunu söyler) |
| Bölüm "Mini soru: now ile hangi şık?" · "Sınavda iki adım: sinyal, sonra fiil" | soru; iki adım | kesin (cümle 16–18; cümle 19) |
| Gönderi 2. cümle | now ve these days çoğunlukla şimdiki zamanı, usually ise geniş zamanı çağırır | jüri bakacak ("çoğunlukla" iki yana da okunabilir; ders now için "bu cümlelerde net ipucu", usually için "geniş zaman ister" der) |
| Gönderi 1. ve 3. cümle | soru; "believe gibi fiillerin tuzağı" | kesin (iddia yok) |
| Sabit yorum | kaydet teşviki + damgalar; iddia yok | kesin |
| "Sıradaki ders: Simple Present ve Present Continuous" | 02-04'ün konusu | kesin (`02-04-ydt-temel/youtube.json` başlık konusu; katalog `GR-02-04`) |

## 6. Açık noktalar

- Ders sayfası adresi `https://ydspublishing.com/grammar/02-03-ydt-temel`: 15.11'de `curl -I` = **404** (emsal `…/02-04-ydt-temel` de 404).
  Adres istem gereği kısa emsalinin tabanından alındı. Yayından önce adres açılmalı; açılmazsa satır panelde değiştirilir.
- Başlık: komşu ders 02-04 "Simple Present ve Present Continuous | YDT İngilizce" başlığını taşır. Senaryo başlığı tek başına kullanılsaydı iki başlık
  yalnız sözcük sırasıyla ayrılırdı. Bu yüzden `surumler.json` konusu alt başlığıyla alındı. "ayrım alıştırması" yerine "sinyal sözcükleri" daha
  aranır olabilir (kapak "ÖNCE SİNYALE BAK" der); karar şefte.
- `surumler.json` `kapak` alanı `null`. Gönderi görseli paket kökündeki `kapak.png` (sözleşme satır 147 kuralı).
- Giriş klibi (≤ 3 sn) eklenirse açıklama damgaları ve bölüm `t` değerleri kayar; araç düzeltir (sözleşme §2). Açıklamaya bu not yazılmadı.
- Bildirim kartının sol alt yerde sahne 7 ve 11 öğeleriyle çakışması ölçülmedi (mp4 yok). Kartın sessiz olduğu birleştirme sonrası `ffprobe` ile ölçülür.
- Liste bağı: önceki ve sonraki öğe `uretimde`; ikisi YouTube'a yüklenene kadar bitiş ekranı ve sıradaki ders bağı boş kalır.
- Etiket `temel` (`surumler.json` kaynağı) genel bir sözcük, arama değeri düşük. Kaynak etiket olduğu için kaldırılmadı.
- Künye `ortak/kunye.js` `seviye: "YDT BASIC"` (İngilizce); huni v2 rozet kararı `YDT · TEMEL`. Bu dosyaya dokunulmadı (yazma alanı dışı).
- Sözleşme kancası için `K/.claude/docs/sozlesme.md` dosyasına 1 satır eklendi (kısası olmayan pakette utm tabanı, başlık çakışması, 404).

---
Son Güncelleme: 15.11.2026 — ilk sürüm (YV-0203T).

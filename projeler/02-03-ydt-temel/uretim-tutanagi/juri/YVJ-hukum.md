# YVJ-0203T — `02-03-ydt-temel` YouTube yayın verisi ÇIKTI jürisi · 15.11.2026

Jüri modeli: Claude Sonnet 5.5 (`claude-sonnet-5-5`). Üretici modeli: Claude Opus 5.5. Aynı model DEĞİL.
Kapsam: yalnız ana paket. Dikey paket yok (`projeler/02-03-ydt-temel-dikey/` dizini yok; `surumler.json` yalnız `ana-yatay`): dikey eşler ölçülemedi.
Ölçülen girdi: `youtube.json`, `youtube-aciklama.md`, `zaman.json`, `ortak/anlatim/{baslar,sozcukler,altyazi}.json`, `anlatim.wav`, `kapak.png`, katalog, `ortak/youtube/bildirim/yer.json`.

## Özet

| Küme | evet | hayır | kanıt yok |
|---|---|---|---|
| YV-1 … YV-9 | 8 | 1 (YV-6) | 0 |
| `youtube-surumu-standart.md` §3 (8 satır) | 7 | 0 | 1 (çakışmama, kare) |
| Toplam | 15 | 1 | 1 |

Kaldı: YV-6 (hayır), §3 çakışmama (kanıt yok; render sonrası YT-3 karesi ister).

## YV tablosu (`juri-olcutleri.md` §2f)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | `baslik` = "Present Continuous ve Simple Present: ayrım alıştırması \| YDT İngilizce" · 71 karakter (≤ 100) · kalıp `<Konu> \| <kitle> İngilizce`; konu = `surumler.json` `video.konu`, kitle `YDT` | 02-04 başlığı "Simple Present ve Present Continuous \| YDT İngilizce": ikisi farklı, çift başlık yok |
| YV-2 | evet | `youtube-aciklama.md` 968 bayt, 929 karakter (≤ 5.000). Sıra: satır 1 değer cümlesi · satır 2 kaydet · `Bölümler:` + 13 damga · `Sıradaki ders` · `Ders sayfası` (4 utm alanı) · hashtag satırı. `utm_campaign=ING-YDT-GR-02-03-T` = katalog `kod`; büyük harf, 02-02 ve 02-04 ile aynı biçim | Damgalar ham ders zamanıdır; giriş klibi eklenince API yeniden yazar (sözleşme §3). Adres canlılığı bu jüride ölçülmedi (üretici raporu: 404) |
| YV-3 | evet | İlk damga 00:00. 13 bölüm. `zaman.json` sahne başları 0 · 15,31 · 33,00 · 51,57 · 68,56 · 87,70 · 109,53 · 130,66 · 167,52 · 187,54 · 224,85 · 240,36 · 270,34; son 280,43 (= `anlatim.wav` 280,43 sn, ölçüldü). Süreler: en kısa 10,09 (son bölüm), sonra 15,31. Açıklama damgası = en yakın saniye, 13 satırın hepsi `youtube.json` `bolumler[].t` ile birebir eşleşti | Yuvarlama 04:00 (240,36) ve 04:30 (270,34) damgalarını 0,36 / 0,34 sn erken açar: izleyici önceki cümlenin son 0,3 sn'sini duyar, içerik kaçmaz. Son bölüm yuvarlanmış damgayla 10,43 sn, sınırın üstünde |
| YV-4 | evet | Senaryo eşlemesi (`METIN.md` cümle numaraları): "Aynı fiil, iki zaman: sinyal sözcüğü" = 1–2 · "Planlı gelecek: are leaving" = 3 · "Geçici dönem: these days" = 4 · "Değişim: nowadays, harder and harder" = 5 · "Neden -ing? Plan, dönem, değişim" = 6–7 · "Karar kartı: now, these days, usually" = 8 · "Tek cümlede iki zaman: usually ve now" = 9 · "Kartpostal: geçici mi, genel mi?" = 10–11 · "Tuzak: sinyal var, -ing yok" = 12–13 · "Believe, recommend, have: -ing tuzağı" = 14 · "Özet: hangi sinyal, hangi zaman?" = 15 · "Mini soru: now ile hangi şık?" = 16–18 (cevap B) · "Sınavda iki adım: sinyal, sonra fiil" = 19. İç ad ("Örnek 1", "Soru anı", "Kural kartı", "Karşıt çift") yok; hepsi izleyici dilinde | "Believe, recommend, have" cümle 14'ün fiillerinin üçünü sayar (think, promise, agree adda yok); eksik sayım yanlış değil. `have` için bkz. YV-6 |
| YV-5 | evet | 9 etiket; virgülle birleşik 123 karakter, YouTube sayımı (boşluklu etikete 2 tırnak) 133 (≤ 500). Konu "Present Continuous ve Simple Present", zaman adları ("Present Continuous", "Simple Present", "şimdiki zaman", "geniş zaman"), kitle "YDT", "İngilizce", "gramer" var. Yineleme yok. `surumler.json` `video.etiketler` 6 etiketin hepsi içinde | "temel" tek başına arama değeri düşük; kaynak etiket olduğu için hata sayılmadı |
| YV-6 | **hayır** | Metinler sözce sözce okundu (başlık, açıklama satır 1–2, 13 bölüm adı, sabit yorum, gönderi g1). Mutlak kural ("her zaman", "asla") yok; yazım hatası yok; emoji (Unicode `So`) taraması boş. **Hata:** bölüm adı "Believe, recommend, **have**: -ing tuzağı" (`youtube.json` `bolumler[9]`, açıklama 03:08). `have` çıplak yazılınca "have -ing almaz" okunur; bu yanlıştır (`I am having dinner`, `She is having a baby`). Dersin kendi cümlesi bunu söyler: "Have **sahip olmak anlamındaysa** -ing almaz" (cümle 14) | Kaynağa uygun olması doğru olduğunu göstermez: dersin özet cümlesi (15) da "Believe ve have gibi fiiller" der, ama ders içinde cümle 14 sınırı çizer; YouTube bölüm adı bu sınırı taşımıyor. **Düzeltme önerisi:** `bolumler[9].ad` ve açıklama 03:08 satırı → "Believe, recommend, have (sahip olmak): -ing tuzağı" (52 karakter). Not (hata değil): gönderi "now ve these days çoğunlukla şimdiki zamanı, usually ise geniş zamanı çağırır": "çoğunlukla" ikinci yarıyı da kapsıyor okunur; ders de `usually` için aynı sözü kullanır; kabul. Önerilen daha açık biçim: "usually ise çoğunlukla geniş zamanı çağırır" |
| YV-7 | evet | `katalog.json`: GR-02-03 `sira` 3 → `liste.sira` 3 ✓; kitle `ydt`, seviye `temel` → "Tenses · YDT Temel" ✓ (02-04 ile aynı ad). Önceki `02-02-ydt-temel` (GR-02-02, YDT temel) ✓; sonraki `02-04-ydt-temel` (GR-02-04, YDT temel) ✓. "Sıradaki ders: Simple Present ve Present Continuous" = `02-04-ydt-temel/youtube.json` başlık konusu | `02-02-ydt-temel` paketinde henüz `youtube.json` yok; kimlik katalogda var, paket `uretimde` |
| YV-8 | evet | `altyazi.json`: 52 satır, her satır `t0 < t1`, sıra bozuk değil, son `t1` = 280,01 ≤ ders 280,43 (`zaman.json` ve `anlatim.wav` 280,43). Son satır cümle 19, `t0` 270,89 = `baslar.json` 19 başı | `altyazi.srt` pakette tutulmaz; srt eşitliği panel testine (`youtube-saf.test.ts`) aittir; bu worktree'de test dosyası bulunamadı, jüri o yarıyı yargılamadı (madde yalnız json yarısını ister) |
| YV-9 | evet | `gonderiler[0].gorsel` = `kapak.png`; dosya var, 1920×1080 (`file`). Kare okundu: sarı zemin, açık tema; `kapak-koyu.png` ayrı dosya. Gönderi metninde, açıklamada, sabit yorumda emoji 0 | Görsel metni ("ÖNCE SİNYALE BAK · now · usually · these days") ders içeriğine uygun |

## `youtube-surumu-standart.md` §3 bildirim kuralları

| Kural | Hüküm | Kanıt | Not |
|---|---|---|---|
| Sayı | evet | Ders 280,43 sn ≥ 4 dk (240 sn) → 2 bildirim; `bildirimler` uzunluğu 2 | |
| Zaman ≈ %30 / ≈ %70 | evet | 1.: t = 88,25 = %31,5 (hedef 84,13). 2.: t = 188,29 = %67,1 (hedef 196,30). Başka cümle başları: 73,94 (%26,4), 225,40 (%80,4); seçilenler hedefe en yakın | `sozcukler.json` içinde 195,60 (%69,8) cümle başıdır ama `baslar.json` birimi değil; standart `baslar.json` der |
| Cümle sınırı | evet | 88,25 = `baslar.json` cümle 8 başı = `sozcukler.json` "Karar" `t0` = `altyazi.json` cümle 8 `t0`; önceki cümle 87,70'te biter (boşluk 0,55). 188,29 = cümle 14 başı = "Olmaz." `t0`; önceki cümle 187,54'te biter (boşluk 0,75). Söz ortasında değil | `METIN.md` tablosu bu zamanlarla çelişir (cümle 8 başı 88,33; cümle 14 başı 189,25; son 281,69). Dört dosya ve ses süresi `baslar.json` ile uyumlu: `METIN.md` bayat. YV'yi etkilemez; jüri `METIN.md` zamanlarına dayanmadı |
| İlk 30 sn / son 20 sn | evet | 88,25 > 30 ve 188,29 > 30; kartlar 88,25–91,25 ve 188,29–191,29; son 20 sn sınırı 280,43 − 20 = 260,43, ikisi de altında | |
| Yer = `yer.json` | evet | Standart §3 ve `ortak/youtube/bildirim/yer.json`: sol alt, x 240 y 900, 520×140; sağ alt yok | |
| Çakışmama (künye, altyazı, sahne öğesi) | **kanıt yok** | mp4 ve kare yok (render yasak). Kısmi, geometrik: sahne 7 (88,25) en alt öğe kutusu `bn2` y ≤ 894, kart y ≥ 900 (pay 6 px); logo x 56–193, kart x ≥ 240; ajanda x sağda → çakışma görünmüyor. Sahne 11 (188,29–191,29, sahne içi 0,75–3,75 sn): alt sol kart 3'ün çerçevesi 216,90'da çizilir, kart anında sol alt boş beklenir; ölçülmedi (`11-…/RAPOR.md` kare üretmedi, "k/ boş") | Madde YT-3 (kare) kapsamındadır; YV verisini etkilemez. **Öneri:** birleştirmeden sonra 88,25 ve 188,29 + 3,0 sn (giriş) anlarında birer kare, kart kutusunda piksel çakışması sayımı |
| Ses (yok) | evet | `youtube.json` bildirimlerinde ses alanı yok; yalnız `t`, `sure` | Ölçüm render ister (YT-3) |
| `giris`, `cikis` alanları | evet | ikisi `true`; şema örneğiyle aynı | |

## Kaldı maddeleri — düzeltme önerisi

| Madde | Öneri |
|---|---|
| YV-6 | `bolumler[9].ad` ve `youtube-aciklama.md` 03:08 satırı: "Believe, recommend, have (sahip olmak): -ing tuzağı" |
| §3 çakışmama | Birleştirme sonrası YT-3 kare ölçümü (iki bildirim anı, kart kutusu piksel çakışması) |

Bilgi (kapsam dışı): `METIN.md` zamanları `baslar.json`, `sozcukler.json`, `altyazi.json`, `zaman.json` ile uyuşmuyor (bayat); üreticinin raporu (YV-RAPOR §6) "Ders sayfası" adresinin 404 verdiğini yazıyor, yayından önce açılmalı; dikey paket (`02-03-ydt-temel-dikey`) yok, sözleşme §3 uzun dikey sürümü YouTube'a sayar.

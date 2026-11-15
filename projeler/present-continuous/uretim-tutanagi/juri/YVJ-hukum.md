# YVJ-0201T — `present-continuous` YouTube yayın verisi ÇIKTI jürisi · 15.11.2026

Jüri modeli: **Claude Sonnet 5.5** (`claude-sonnet-5-5`). Üretici modeli: Claude Opus 5.5 (`claude-opus-5-5`, `YV-RAPOR.md` ilk satırı). Model farklı (§1e sağlandı).
Bakılan çıktı: `present-continuous/` ve `present-continuous-dikey/` içindeki `youtube.json`, `youtube-aciklama.md`, `zaman.json`, `ortak/anlatim/{senaryo.json,METIN.md,altyazi.json}`, `kapak.png` (yatay + dikey görüldü), `varlik/grammar/katalog.json`, komşu 23 paketin `youtube-aciklama.md` utm satırları. Hiçbir dosya değiştirilmedi.

## Özet

| Sonuç | Sayı | Maddeler |
|---|---|---|
| geçti (evet) | 12 | YV-1, 2, 3, 4, 5, 7, 8, 9 + bildirim sayı, zaman, cümle sınırı, ilk 30 sn / son 20 sn |
| kaldı (hayır) | 1 | YV-6 |
| kanıt yok | 1 | bildirim "Yer" (render yok; görsel jüri) |

## Madde tablosu (`juri-olcutleri.md` §2f)

| Kimlik | Hüküm | Kanıt (kendi ölçümüm) | Not |
|---|---|---|---|
| YV-1 | evet | Başlık "Present Continuous \| YDT İngilizce" = 34 karakter (≤ 100); kalıp `<Konu> \| <kitle> İngilizce`; konu = `surumler.json` `video.konu` | Başlık `present-continuous-ileri/youtube.json` ile BAYT AYNI (§Not 2) |
| YV-2 | evet | `wc -c` = 677 bayt (≤ 5.000); sıra: satır 1 değer cümlesi · satır 2 kaydet · "Bölümler:" + 5 damga · "Sıradaki ders" · bağlantı (utm) · hashtag; dikey dosya yalnız `utm_content` satırında farklı (`diff` çıktısı satır 12) | Giriş klibi kayması açıklamaya yazılmamış; API yeniden yazar (sözleşme §3) |
| YV-3 | evet | İlk damga `t: 0`; 5 bölüm; süreler 15,44 · 14,71 · 15,83 · 16,83 · 24,52 sn (en kısa 14,71 ≥ 10); `bolumler[].t` = `zaman.json` sahne başları (0 · 15,44 · 30,15 · 45,98 · 62,81; sahne 01+02 birleşik); damgalar 00:00 · 00:15 · 00:30 · 00:46 · 01:03 = `round(t)` | 01:03 sözün ilk 0,19 sn'sini kaçırır; önceki cümlenin sonuna düşmekten iyidir |
| YV-4 | evet | Her bölüm adı `METIN.md` sahnesinde söylenenle eşleşti: c1–c2 "gidiyorum", "şimdiki zamanla geleceği anlatırız" → bölüm 1; c3 "I am sitting … now" → bölüm 2; c4 "this semester … bu günlerde süren bir iş" → bölüm 3; c5 "Look, listen, watch out gibi sözcükler" → bölüm 4; c6 "Neden hep -ing?" + c7 "am, is, are şimdiki zaman demek" → bölüm 5. İç ad ("giris", "Örnek 1") yok; en uzun ad 39 karakter | Bölüm 4: "işaret" der, "kural" demez; kabul |
| YV-5 | evet | 13 etiket, düz toplam 136 karakter, virgülle birleşik 148; YouTube sayımıyla (boşluklu etikete tırnak) ≈ 164 ≤ 500; konu ("Present Continuous"), zaman adı ("şimdiki zaman", "Present Progressive"), kitle ("YDT", "YKS"), "İngilizce", "gramer" var; yineleme yok | "Present Progressive" doğru eş ad |
| YV-6 | **hayır** | Metinler temiz: açıklama satır 1 ("üç örnekle … be fiili + -ing … şu an süren iş, bugünlerde süren iş, Look! gibi işaret sözcükleri"), sabit yorum, gönderi g1 ("Bu akşam amcamlara gidiyorum" → derste `I'm going to my uncle's tonight.`; üç örnek am sitting / is taking / is climbing) mutlak kural ve yanlış denklik içermiyor; yazım ("bugünlerde" TDK bitişik) doğru; emoji 0. **KALDI NEDENİ:** gönderi g1 görseli `kapak.png` (yatay ve dikey, aynı yazı) iki dilbilgisi iddiası yayımlıyor: "GİDİYORUM = AM GOING" ve "-yor → -ing". "-yor" durum fiilleriyle de gelir (biliyorum ≠ I am knowing); "am going" tek başına tam yapı değildir ("I am going") | Kapak içeriği KS/kapak jürisinin alanıdır ama g1 onu gönderi olarak yayımlar; şef çıkarımı gerekir (aşağıda) |
| YV-7 | evet | `katalog.json`: ünite "02" Tenses (`sira` 2), konu GR-02-01 `sira` 1 (ilk), video `02-01-ydt-temel`; `kitleler.ydt` = YDT, `seviyeler.temel` = Temel → "Tenses · YDT Temel", `sira` 1, `onceki` null, `sonraki` `02-02-ydt-temel` (GR-02-02); sıradaki ders adı "Simple Present" = `simple-present-temel/surumler.json` `konu` | Listede GR-02-01 ilk; Present Continuous'ın Simple Present'ten önce gelmesi katalog kararıdır |
| YV-8 | evet | `altyazi.json` 24 satır, son `t1` 85,81 ≤ ders süresi 87,33; `t0` sıralı. Dikey paket `altyazi.json` bayt aynı. srt pakette yok (panel türetir) | `youtube-saf.test.ts` eşitliği bu jüride koşulmadı |
| YV-9 | evet | `kapak.png` var, yatay 1920×1080, dikey 1080×1920 (`file`); `KAPAK-RAPOR.md` satır 4–5: kapak = açık, kapak-koyu = koyu; gönderi `gorsel: kapak.png`; gönderi metninde emoji yok | Görsel içeriği YV-6'da |

## `youtube-surumu-standart.md` §3 bildirim

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | Ders 87,33 sn < 4 dk → 1 bildirim; `youtube.json` `bildirimler` tek satır |
| Zaman | evet | 30,15 sn = %34,5 (`zaman.json` sahne 4 başı = `METIN.md` cümle 4 başı). %30 anı 26,20 sn ilk 30 sn yasağında; seçilen an yasağın hemen ardındaki ilk cümle başı. Adaylar: 15,44 (ilk 30 sn yasak), 45,98 (%52,6 daha uzak) |
| Cümle sınırı | evet | Önceki cümle 29,60'ta biter, cümle 4 30,15'te başlar (`METIN.md`); söz ortası değil |
| İlk 30 sn / son 20 sn | evet | 30,15 ≥ 30; 30,15 + 3,0 = 33,15 ≤ 87,33 − 20 = 67,33 |
| Ses | evet | `youtube.json` ses alanı taşımıyor |
| Yer | kanıt yok | Kare yok (render yasak). `zaman.json` sahne 3 `gecis` BookFlip, 12 kare = 0,40 sn, `icerik_kare` 441 ↔ `kare` 453: geçiş sahne 4 başında oynar; kart 30,15'te açılırsa BookFlip ile çakışır. Çakışma ölçülemedi, kapıyı görsel jüri koşar |

## Kaldı maddeleri için düzeltme önerisi

- **YV-6 (kapak yazısı):** `kapak.png` ve dikey eşinde alt satırı "-yor → -ing" kaldır; ana satırı "GİDİYORUM = I AM GOING" yap (be fiili görünür, ek denkliği yok). Yeni kapak çıkana kadar g1 `gorsel` değerini değiştirme; yayından önce şef kapak jürisine yeniden gönderir. Tek kapak yenilenirse yatay + dikey ikisi birlikte yenilenir.
- **Bildirim "Yer" (kanıt yok):** görsel jüri 30,15–33,15 aralığında 3 kare (30,15 · 31,5 · 33,0) baksın; çakışma çıkarsa `t` değerini 31,44'e al (cümle 4 içinde `My sister is taking …` başı, %36,0; `altyazi.json` satır başı 31,44).

## Şef notu (kaldı sayılmadı)

1. **Dikey Shorts:** dikey paket `youtube.json` ana paketle bayt bayt aynı. Dikey ders 87,33 sn (giriş + kısa çıkış ≈ 94 sn ≤ 180): sözleşmeye göre Shorts sayılır, bölüm damgası ve bildirim orada işlemeyebilir. Sabit yorum "açıklamadaki bölüm damgalarından … geç" cümlesi dikeyde boş vaat olabilir. Karar şefte (`sozlesme.md` YV satırları).
2. **Başlık çakışması:** `present-continuous-ileri/youtube.json` başlığı temel dersle aynı ("Present Continuous | YDT İngilizce"). Emsal (YV-0206I): ileri başlık alt başlık alır, örneğin "Present Continuous: … | YDT İngilizce" (ileri paketin amaçlarından). Bu paketin başlığı değişmez.
3. **Ana ders cümleleri (§1c, kaynağa uygun ≠ doğru):** senaryo c7 "-ing ekini Türkçedeki -yor gibi düşün" ve `surumler.json` `canAlici` "Türkçedeki -yor = İngilizcedeki -ing" yanlış denklik riski taşır; c2 "İngilizce de aynısını yapar" kısmi denklik (yalnız planlanmış gelecek). Yayın verisine girmediler.
4. **Kod farkı:** `surumler.json` `video.kod` = `ING-YDT-GR-01-PC`; `utm_campaign` katalog kodu `ING-YDT-GR-02-01-T`. 23 komşu paketin utm biçimi (`ING-YDT-GR-02-0X-T`) ile tutarlı.

---
Jüri zamanı: 15.11.2026. Önceki hüküm dosyası yok.

Jüri modeli: Claude Sonnet 5.5 (`claude-sonnet-5-5`) · üretici: Claude Opus 5.5 → FARKLI model (§1e uyumlu)

# YVJ-0209T — `present-perfect-cont-temel` YouTube yayın verisi çıktı jürisi · 15.11.2026

## Özet

| Sonuç | Sayı |
|---|---|
| Geçti (evet) | 9 / 9 (YV-1 … YV-9) + §3 bildirim kuralları 5 / 5 |
| Kaldı (hayır) | 0 |
| Kanıt yok | 0 |
| Dikkat (kaldı değil) | 3 (aşağıda N-1, N-2, N-3) |

Ölçümler jüri tarafından salt okuma komutlarıyla yeniden yapıldı. Üretici raporuna güvenilmedi.
Hiçbir üretim dosyası değiştirilmedi.

## Madde tablosu (`juri-olcutleri.md` §2f)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | `baslik` = "Present Perfect Continuous \| YDT İngilizce", 42 karakter (≤ 100). Kalıp `<Konu> \| <kitle> İngilizce` eşleşir. Konu = `senaryo.json` `baslik` | — |
| YV-2 | evet | `youtube-aciklama.md` 716 bayt (≤ 5.000), `wc -c`. Sıra: değer cümlesi → "Sınav günü bakmak için kaydet." → "Bölümler:" + 5 damga → "Sıradaki ders" → "Ders sayfası" (utm) → hashtag satırı | N-3 |
| YV-3 | evet | İlk damga 00:00. 5 bölüm. Süreler `zaman.json`: 17,13 · 15,15 · 14,99 · 14,24 · 21,71 sn (hepsi ≥ 10). Açıklamadaki damga = `youtube.json` `t` değerinin en yakın saniyesi (00:17 · 00:32 · 00:47 · 01:02) | N-2 |
| YV-4 | evet | Senaryo (`METIN.md`) ile bölüm adları karşılaştırıldı: B1 "İki saattir çalışıyorum: -dir ve -yor" = cümle 1–2 (süre için -dir, süren iş için -yor). B2 "Süre için for: I have been waiting" = cümle 3. B3 "Başlangıç için since: has been playing" = cümle 4. B4 "Sokak ıslak: It has been raining" = cümle 5. B5 "Neden hep been? Kalıp: have been + -ing" = cümle 6–7. İç ad yok, her ad izleyici dilinde ve sahnede söylenen içeriği taşır | — |
| YV-5 | evet | 13 etiket, yineleme yok. Düz toplam 155 · virgüllü 167 · YouTube sayımı (boşluklu 8 etikete tırnak) 183 (≤ 500). Konu "Present Perfect Continuous", zaman adı "Present Perfect Progressive", kitle "YDT" var | — |
| YV-6 | evet | Başlık, açıklama, sabit yorum, gönderi metni, bölüm adları tek tek denetlendi. Mutlak kural yok, yanlış denklik yok, yazım hatası yok, emoji taraması 0. "for = süre, since = başlangıç noktası" ve "has been (tekil)" iddiaları doğru. "İzi şimdi görünen eylem" ders cümle 5 ile aynı ve doğru | N-1 |
| YV-7 | evet | Katalog (`varlik/grammar/katalog.json`): ünite 02 "Tenses"; `GR-02-08/09/10` sıra 8/9/10; `ING-YDT-GR-02-09-T` = ydt/temel. `konu-adlari.json`: GR-02-10 = "Simple Past". Liste "Tenses · YDT Temel", sıra 9, önceki 02-08-ydt-temel, sonraki 02-10-ydt-temel; açıklamadaki "Sıradaki ders: Simple Past" doğru | — |
| YV-8 | evet | `altyazi.json` 23 satır, son `t1` = 82,30 ≤ ders 83,22. Dikey paketin `altyazi.json` dosyası `cmp` ile bayt bayt aynı. Pakette `.srt` yok (panel türetir) | — |
| YV-9 | evet | `kapak.png` pakette var, 1920×1080, sarı açık tema (görsel okundu). `kapak-koyu.png` ayrı dosya. Dikeyde `kapak.png` 1080×1920 açık tema. Gönderi metninde emoji 0 | N-1 |

## `youtube-surumu-standart.md` §3 bildirim kuralları

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | Ders 83,22 sn < 4 dk → 1 bildirim; `bildirimler` tek satır |
| Zaman ≈ %30 | evet | 32,83 sn = %39,4. %30 hedefi 24,97 sn, ilk 30 sn yasağının içinde kalır. 30 sn sonrası ilk cümle başı 32,83 (cümle 4 başı, `METIN.md`). Başka aday: 47,82 (%57, daha uzak). Sapma zorunlu ve gerekçeli |
| Cümle sınırı | evet | 32,83 = cümle 4 "İkinci örnek." başı; cümle 3 32,28'de biter. Söz ortasında değil. Örnek 2 sahnesi 32,28'de açılır, geçiş 0,40 sn (32,68'de biter) |
| İlk 30 sn / son 20 sn | evet | 32,83 ≥ 30; bildirim sonu 35,83 ≤ 63,22 (83,22 − 20) |
| Ses, giriş, çıkış | evet | `sure` 3,0 sn; `giris: true`, `cikis: true` |

## Dikkat notları (kaldı değil; şef kararı)

| # | Konu | Öneri |
|---|---|---|
| N-1 | Gönderi görseli (`kapak.png`) "İKİ SAATTİR = HAVE BEEN" yazar. "Saattir" tek başına "have been" değildir; süreyi İngilizcede `for two hours` taşır. Bu yayın verisi metinlerinde yok; görsel kapak jürisinden geçmiş ayrı varlıktır, YV-9 yalnız dosyanın varlığını ve temasını ölçer. Gönderi metni ise "-dir ve -yor ile kurduğumuz cümleyi İngilizce have been ve -ing ile kurar" der: kalıp anlatımı, denklik değil, kabul | İstenirse gönderi cümlesi: "İki saattir çalışıyorum" İngilizcede nasıl söylenir? Süreyi for two hours taşır, "süren iş" anlamını have been + -ing kurar: I have been working for two hours. Kapak denkliği kapak jürisinde ele alınmalı |
| N-2 | Damgalar 00:17, 00:32, 00:47 sahne başından 0,13–0,28 sn ÖNCE düşer; izleyici önceki cümlenin son sözünün ("görüyoruz.", "-ing.", "-ing.") kuyruğuna iner. Yukarı yuvarlama (00:18, 00:33, 00:48) bu kez sözün başını keser (32,83 "İkinci" başlar) | Giriş klibi eklenince araç zaten yeniden hesaplar; araçta damgayı sahne başı − 0 yerine "sahne başı, aşağı yuvarlama" tutmak yeterli. Veri değişikliği gerekmez |
| N-3 | Açıklama ilk satırı 182 karakter; YouTube arama ve ana sayfada kısaltır. Standart sınır koymaz | İstenirse ilk cümle: "Present Perfect Continuous: have/has been + -ing kalıbı, süre için for, başlangıç için since." |

## Kaldı maddeleri için düzeltme önerisi

Kaldı madde yok. Veri bu hâliyle takvim uygulamasına verilebilir; N-1 kararı şefte.

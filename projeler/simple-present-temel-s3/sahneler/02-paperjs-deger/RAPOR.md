# 02-paperjs-deger — RAPOR (15.11, istem D-02-paperjs-deger, huni v2; render yok)

| Ölçüm | Değer |
|---|---|
| Motor | Paper.js · 1080×1920 · 30 fps · 281 kare · t_bas 3,89 · t_son 12,84 (`zaman.json` ile aynı) |
| `qa-yerel.sh … 3.95,8.40,12.75 8.40 --hazirla` | çıkış 0 (2 koşu; kare turu 1 sonrası yeniden) |
| `cakisma-kapisi.mjs … --sahne 02-paperjs-deger --port 41333 --sunucu 41022` | çıkış 0 · "çakışma yok (37 örnek, 667 kutu)" · uyarı 0 |
| Metin taraması (`tam ders\|dakika`, html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (3 açık + 1 koyu kare, piksel ölçümü) | 4 / 4 karede tablodaki yerde |
| Sözdizimi | `node --check` (`.mjs` kopyası) geçti; satır ≤ 120 |
| Tema | açık + koyu (koyu 8,40 karesi) |

## Yapım

| Adım | Kim | Çıktı |
|---|---|---|
| Kısa dosyalar | şef | `kalem-paper.js`, `sayfa.html`, `calistir.sh`, `nesneler.json` emsal `02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/` kopyası; Edit: import yolları `simple-present-temel-s3/ortak`, sahne adı, `N=281`, `TBAS=3.89`, `GLOBAL_SN` |
| Tasarım + spec | şef | `SPEC.md` (sabit tablosu, katman sırası, 18 olay, 8 bekçi, kabul) |
| `sahne-02.js` | agy-filo `tek --rol kod` (gemini-3.8-flash-high, 144 sn, 1 tur, başarılı) | özet `/home/sef/.claude/canavar/agy-filo/20261115-192600/ozet.md` |
| İnceleme | şef | dosya baştan sona okundu; SPEC'e uyuyor (sabitler, oge sırası, olaylar, bekçiler) |
| Şef Edit (kare turu 1) | şef | 3 küçük düzeltme: halka `DRY` 50 → 70, merkez −4 / −26 (halka `s`'nin alt sağını kesiyordu) · `O gider mi?` başlangıcı `go?` 254 → `she` 249, süre 10 (donma 268'de yazı bitmemişti) · düşen `es` `dy` 70 → 120 (5 karelik sönüşte düşüş ~35 px kalıyordu) |
| Sözleşme | şef | `K/.claude/docs/sozlesme.md` 1 satır (Paper.js kart dönüşümü, düşen parça, sözcük içi halka, TR donma payı) |

agy özetinin "değişen" listesinde başka paketlerin dosyaları var (`02-04-ydt-temel-s2/…`, `02-04-ydt-temel-s3/…`, `sozlesme.md`): filo
düzeyinde atıf, paralel oturumların işi. Bu koşuda agy yalnız `sahne-02.js`'i yazdı (dizinde başka yeni/değişen dosya yok).

## Olay listesi (yerel kare = round((t − 3,89) × 30); sözcük `ortak/anlatim/sozcukler.json` cümle 2)

| # | Olay | Kare | Çapa (küresel sn) | Konum |
|---|---|---|---|---|
| 1–2 | Kart 0 hazır: kutu + `He doesn't goes.` (Fredoka 80) | 0 | — (sahne 01'den) | kutu görünür x 62–758 × 480–639; yazı x 110, taban 582 |
| 3 | `does` sarı halka | 72 | does 6,28 | merkez ≈ (303,8; 556), yarıçap 92 × 70 |
| 4 | `es` (goes) arkası sarı bant (ek ayırma) | 101 | s 7,24 | x ≈ 585–676 |
| 5 | Kavisli ok `es` → `does` | 101–113 | s 7,24 | (629,8; 532) → (352,3; 532), yay kartın üstünden, tepe ≈ 476 |
| 6 | `es` (does) arkası sarı bant: `do-es` | 110 | ona 7,56 | x ≈ 308–398 |
| 7 | `es` (goes) kırmızı üstü çizgi; ok + bant 1 söner | 153–159 | s 8,99 | x ≈ 586–674, y ≈ 556–564 |
| 9 | Kırmızı ✗ (2 darbe) | 160 / 165 | gelmez. 9,23 | x 790–854 × 526–590 |
| 10 | Halka mürekkebe döner (sarı 6 karede söner) | 160 | gelmez. 9,23 | aynı halka |
| 11 | `es` düşer (120 px) ve solar; ✗ silinir; kart 0 söner | 194–199 | He 10,36 | — |
| 12–13 | Kart 1 kutusu + `He doesn't go.` (Fredoka 72) | 194 / 198, 201, 218 | He, doesn't, go. | kutu 480–699; taban 566 |
| 14 | Soluk TR `O gitmez.` (Caveat 52, ikincil) | 226–240 | go. + 8 | taban 644 |
| 15–16 | Kart 2 kutusu + `Does she go?` (Fredoka 72) | 234 / 242, 249, 254 | Does, she, go? | kutu 760–979; taban 846 |
| 17 | Soluk TR `O gider mi?` (Caveat 52) | 249–259 | she 12,20 | taban 924 |
| 18 | Kart karaoke: tek sarı altçizgi kayar (218 kart 1 `go`, 254 kart 2 `go`) | 198–268 | 10,36–12,36 | taban + 0,30 × 72 |

Kart 1 `He` 198'de (konuşma 194): kart 0 sönüşü (194–198) bitmeden yeni yazı gelseydi kapı yazı × yazı uyarısı verirdi.

## Kanal katmanı ve bantlar (karede ölçüm, eşik: zemin sapması > 90)

| Kare | Logo (görünür) | `@ydspublishing` | Künye | İçerik | Altyazı | 0–280 | 1570–1920 | x 961–1080 |
|---|---|---|---|---|---|---|---|---|
| 3,95 açık | x 61–239, y 298–330 | x 265–598, y 296–339 | x 60–509, y 386–433 | x 62–756, y 480–638 | y 1451–1483 | boş | boş | boş |
| 8,40 açık | aynı | aynı | aynı | x 62–756, y 473–638 | y 1421–1522 (2 satır) | boş | boş | boş |
| 12,75 açık | aynı | aynı | aynı | x 62–757, y 481–978 | y 1451–1493 | boş | boş | boş |
| 8,40 koyu | aynı | aynı | x 60–510 | x 62–756, y 473–638 | y 1421–1522 | boş | boş | boş |

Logo resim kutusu 53,2–246,7 × 291–339 (SVG iç boşluğu nedeniyle görünür 61–239 × 298–330; emsal ölçümüyle aynı). Yazı taban 330 (`y`/`p` kuyruğu 339).

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/02-paperjs-deger-3.95.png` | kart 0 tek başına; altyazı `Hata nerede?` (cümle 1 parçası, ortak altyazı modülü); taşma yok |
| `k/02-paperjs-deger-8.4.png` | halka + iki bant + ok; tur 1'de halka `s`'yi kesiyordu → düzeltildi; tur 2'de halka `s`–`n` arasından geçer (sıkı aralık, hafif yakınlık) |
| `k/koyu/02-paperjs-deger-8.4.png` | koyu temada bant turuncu (`vurguDolgu` #f2a93b, alfa 0,6), krem yazı okunur; kontrast açıktakinden düşük |
| `k/02-paperjs-deger-12.75.png` | kart 1 + kart 2; altçizgi yalnız kart 2 `go` altında (tek sarı) |
| ek kareler `~/qa-kare/simple-present-temel-s3/02-paperjs-deger-ek/` (9,60 · 10,45 · 10,62 · 11,50 · 12,83) | üstü çizili `es` + ✗; kart 0 sönüşü; kart 1 kutusu ve `He` altçizgisi; `O gitmez.` yazılıyor; donma karesinde `O gider mi?` tam |

## Açık noktalar

1. **Sahne 01 kartıyla eşleşme.** Kart 0 sabitleri: kutu `kutu(70, 490, 680, 140)` (görünür x 62–758, y 480–639), yazı x 110, taban 582,
   Fredoka 700 80, renk `murekkep`, dolgusuz kalem kenarı (`ikincil`, w 4). Sahne 01 (HyperFrames) kartı "kâğıt kart" ise dolgulu olabilir
   (sözleşme: S1 kaydet sahnesi dolgu `#fff9e6` / açık `#fffdf8`). Koyu temada açık dolgulu kart → dolgusuz kalem kutusu geçişi görünür
   bir sıçrama olur. Sahne 01 bu dosyadaki sabitleri ve dolgusuz kutuyu kullanmalı (ya da şef iki sahnenin kart dilini birleştirmeli).
2. **Sözcük içi halka.** `does` ile `n't` arasında harf boşluğu ~10 px; halka çizgisi (7,5 px) iki harfe de yakın geçer. 13.11 kuralı
   (halka harfe değmez) burada tam sağlanamaz; istem halkayı açıkça istediği için halka kaldı.
3. **Altyazı EN parçası.** 10,36–12,92'de altyazı bandı `He doesn't go. Does she go?` gösterir (ortak `altyazi.json` + `kunye.js`); kartlar
   da aynı metni taşır. Sahne kodunun kapsamı dışında; emsal ile aynı davranış.
4. **Ok kart üst kenarını keser.** Yay tepesi ≈ 476 (kart üst çizgisi 480); `isaret` türü kapıda muaf, karede okunur.

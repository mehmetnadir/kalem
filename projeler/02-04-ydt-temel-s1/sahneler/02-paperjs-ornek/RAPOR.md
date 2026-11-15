# 02-paperjs-ornek — RAPOR v2 (15.11, istem D-V2 huni v2; render yok)

| Ölçüm | Değer |
|---|---|
| Motor | Paper.js · 1080×1920 · 30 fps · 522 kare · t_bas 3,00 · t_son 19,99 (v1 ile aynı) |
| Değişen | yerleşim (içerik x 60–960, y 460–1380) + kanal katmanı + künye satırı; içerik ve olay sırası v1 ile aynı |
| `qa-yerel.sh … 3.05,11.50,19.90 11.50 --hazirla` | çıkış 0 (2 tur) |
| `cakisma-kapisi.mjs … --sahne 02-paperjs-ornek` | çıkış 0 · "çakışma yok (69 örnek, 3180 kutu)" · uyarı 0 |
| Metin taraması (`tam ders|dakika`, html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (3 açık + 1 koyu karede piksel ölçümü) | 4 / 4 karede yerinde |
| Yedek | `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/` (`ortak/kunye.js`, `sahneler/02-paperjs-ornek/` v1 dosyaları, `k-v1/`, `qa-kare-v1/`) |

## Yapım

| Adım | Kim | Çıktı |
|---|---|---|
| Tasarım + spec | şef | `SPEC.md` v2 (§A kunye.js, §B sahne-02.js; bantlar, sabit tablosu, bekçiler, olay listesi) |
| `ortak/kunye.js` v2 | agy-filo `tek --rol kod` (gemini-3.8-flash-high, 182 sn, 1 tur, başarılı) | `KANAL`, `kanalCiz`, v2 `KUNYE`, `konuDuzen`, `kunyeCiz` (çip yok), altyazı x 60–960 · özet `/home/sef/.claude/canavar/agy-filo/20261115-184957/ozet.md` |
| `sahne-02.js` v2 | agy-filo `tek --rol kod` (gemini-3.8-flash-high, 95 sn, 1 tur, başarılı) | sabitler, 2 yeni bekçi, `sahneKur` `bolum`suz · özet `/home/sef/.claude/canavar/agy-filo/20261115-185000/ozet.md` |
| İnceleme | şef | iki dosya diff ile baştan sona okundu; SPEC'e uyuyor; `node --check` iki dosyada geçti |
| Şef Edit (kare turu 1) | şef | `KUTU_PAY` 10: kart kutusu 70–950 (el çizimi köşe taşması dahil 62–957). Tur 1 ölçümü: kart çizgisi x 52–967, sağ 961–967 bandına girdi |
| Sözleşme | şef | `K/.claude/docs/sozlesme.md` 1 satır (canvas huni v2 künyesi, kutu taşma payı) |

`kalem-paper.js`, `sayfa.html`, `calistir.sh`, `bavul.svg` değişmedi (`kunyeCiz` `bolum`u yok sayar).
agy özetlerindeki "değişen" listesinde başka sahnelerin dosyaları var (`01-hyperframes-kapak`, `03-…`, `-s3`, ana ders `90-…`):
filo düzeyinde atıf, paralel oturumların işi. Bu koşularda agy yalnız hedef dosyasını yazdı (diff ile denetlendi).

## Kanal katmanı ve künye (karede ölçüm, eşik: zemin sapması > 90)

| Öğe | Tablo | Ölçülen (4 karede aynı) |
|---|---|---|
| Logo | resim x 53,2, görünür x 60, y 291–339 | görünür x 60/61–239, y 298–330 (SVG iç boşluğu); resim kutusu 53,2–246,7 × 291–339 |
| `@ydspublishing` | Lexend 700 42, x 263, taban 330 | x 264–598, y 296–339 (taban 330, `y`/`p` kuyruğu 339) |
| Künye | y 360–450, konu + rozet sağ uç ≤ 960 | x 60–863, y 386–433; konu boyu 34 (rozet hapı 661–863) |
| Kapı kutuları | `kunye:kanal`, `kunye:konu`, `kunye:rozet` | çakışma yok |

## Bantlar (karede ölçüm, tur 2)

| Kare | 0–280 | İçerik (455–1390) | Altyazı | 1560–1920 | x 961–1080 |
|---|---|---|---|---|---|
| 3,05 açık | boş | x 87–751, y 491–697 | x 79–939, y 1416–1522 (2 satır) | boş | boş |
| 11,50 açık | boş | x 62–957, y 499–953 | x 98–923, y 1449–1494 | boş | boş |
| 19,90 açık | boş | x 62–957, y 499–1363 | x 96–923, y 1449–1494 | boş | boş |
| 11,50 koyu | boş | x 62–957, y 499–953 | x 98–923 | boş | boş |

## Olay ↔ sözcük (yerel kare = round((t − 3,00) × 30); zaman `sozcukler.json`'dan `al()` ile)

| # | Olay | Kare | Cümle:sözcük (küresel sn) | v2 konum |
|---|---|---|---|---|
| 1 | İki TR satırı hazır (sahne 01'den), Caveat 80 | 0 | — | x 84, taban 560 / 680 |
| 2 | Karaoke altçizgi satır 2 `yaşı-yor-um.` | 12 | 1:3 yaşıyorum. (3,08) | taban 680 |
| 3 | ek_ayir satır 1 *yor* kutusu | 29 | 1:4 Türkçede (3,96) | x ≈ 551–636 |
| 4 | ek_ayir satır 2 *yor* kutusu | 86 | 1:7 yaşıyorum. (5,56) + 9 | x ≈ 482–567 |
| 5 | TR parçaları solar · iki çip kayar | 156–164 / 162–177 | 2:2 ayrılır. (8,19) | çip 1 → taban 540, çip 2 → 936 |
| 6–7 | Kart 1 kutusu + `I live in İstanbul.` + karaoke | 172 / 182–199 | 2:3–6 (9,08–9,64) | kutu 70–950 × 570–766, taban 650 |
| 8–10 | odak *live* · bag 1 · ev | 190 / 194 / 199 | 2:4–6 | ev 810–910 × 584–684 |
| 11 | `Hep orada.` (soluk, kalemle) | 245–279 | 2:7–8 (11,17–12,29) | taban 736 |
| 12–15 | `PERMANENT` · eksen 1 · now · uzun bant | 281 / 293 / 301–305 / 308 | 2:9–11 (12,37–13,25) | eksen y 816 |
| 16–17 | Kart 2 kutusu + `I am living` / `with my uncle.` | 341 / 351–382 | 2:13–18 (14,70–15,74) | kutu 70–950 × 966–1238, taban 1044 / 1124 |
| 18–20 | odak *am living* · bag 2 · bavul | 361 / 370 / 382 | 2:15–18 | bavul 810–910 × 980–1080 |
| 21 | `Şimdilik.` (soluk) | 391–420 | 2:19 (17,03–17,99) | taban 1208 |
| 22–24 | `TEMPORARY` · eksen 2 · now · kısa bant + çentik | 422 / 434–446 / 451–460 | 2:20–22 (18,07–19,03) | eksen y 1288, now taban 1364 |

## Kapı (tur 2, son satırlar)

```
== HAZIRLA
önizleme hazır
== KAPI
02-paperjs-ornek | çakışma yok (69 örnek, 3180 kutu)
== KARE (açık)
"png":"/home/sef/qa-kare/02-04-ydt-temel-s1/02-paperjs-ornek/02-paperjs-ornek-3.05.png"
"png":"/home/sef/qa-kare/02-04-ydt-temel-s1/02-paperjs-ornek/02-paperjs-ornek-11.5.png"
"png":"/home/sef/qa-kare/02-04-ydt-temel-s1/02-paperjs-ornek/02-paperjs-ornek-19.9.png"
== KARE (koyu)
"png":"/home/sef/qa-kare/02-04-ydt-temel-s1/02-paperjs-ornek/koyu/02-paperjs-ornek-11.5.png"
kapı çıkış kodu: 0
```
Ayrı çakışma kapısı (`--port 41333 --sunucu 41022`): çıkış 0, aynı satır, "uyar" geçen satır 0.

## Bakılan kareler (Read ile; `k/`, `k/koyu/`)

| Kare | Bulgu |
|---|---|
| `k/02-paperjs-ornek-3.05.png` | kare 0 durumu: iki TR satırı (84, 560 / 680), kanal + künye, altyazı 2 satır; içerik bandının alt yarısı boş (beklenen, kartlar 9,08'de gelir) |
| `k/02-paperjs-ornek-11.5.png` | kart 1 + ev + `Hep` yazılıyor; çip 1 kartın üstünde, bag oku *live*'a iner; çip 2 kart 2 yerinde bekler |
| `k/02-paperjs-ornek-19.9.png` | son durum: iki kart, iki zaman çizgisi; taşma, kesik yazı, üst üste binme yok; çip 2 ile eksen 1 `now` aynı sırada (x 370–470 / 670–755), değmez |
| `k/koyu/02-paperjs-ornek-11.5.png` | koyu tema: krem yazı, şeffaf logo (sarı `yds` + beyaz), turuncu rozet; okunur |

Tur 1 kareleri aynı adla üzerine yazıldı (qa-yerel kopyası); tur 1 bulgusu yukarıdaki ölçüm satırında.

## Açık noktalar

1. **Altyazı ortası 510 (x 60–960):** eski `W/2` (540) yerine; sağ 960–1080 platform düğmeleri. Sahne 01 `yardim.py` de `altyaziOrta 510`
   kullanıyor (geçişte sıçrama yok). Sahne 08 ve 03 aynı değeri almalı (bu oturumda denetlenmedi).
2. **Sahne 01 devri:** sahne 01 `devir.json` (18:55) sol 84, taban 560 / 680, *yor* x 550,08 / 481,28 → sahne 02 kare 0 ile uyuşuyor.
3. **Açık temada logo:** `yds-publishing-lacivert.svg` içindeki sarı `yds` krem zeminde düşük kontrastlı (BRIEF değeri; değiştirilmedi).
4. **`kalem-paper.js` baş yorumu** hâlâ "DİKEY … bolum" anlatır; dosya değişmedi, `bolum` artık `undefined` geçer ve yok sayılır.
5. Süre 31,75 sn (standart ≈ 22–26) bu sahnenin dışında; şef kararı (`uretim-tutanagi/V2-C-RAPOR.md`).

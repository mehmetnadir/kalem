# Sahne 11 — Tuzak konser (düz canvas, 913 kare, t_bas 259,61, cümle 38–42)

Durum: P2 yazıldı; önizleme hazırlığı koşuldu (koyu, sonra açık tema son). Render, kapı (çakışma) ve sahne-kare YOK (şef EK 13.11 12:40).
Künye: SIMPLE PRESENT · YDT ADVANCED, çip "Trap", ajanda etkin Roots. Renk yalnız kunye.js token'ları; kırmızı yalnız perde ünlemi.

## İçerik
- 38 perde: kırmızı ünlem, gelecek oku (söner 262,9–263,2).
- 39 kart tam genişlik (yaklas 0,94 → 1), begins ve ends sarı daire, saat + takvim, 40 TR çeviri, başlayacak altı çizgi.
- 41 soru anı 1: öğrenci başı + balon, sarı nokta balonda «begin» ve kartta «begins» (yanılgı: tomorrow → will).
- 42 yakın çekim «The concert» (kalan soluk), tarife tablosu (8:00 · 11:00), (özne cansız ya da kişi), resmî program / tarife → geniş zaman; kart küçülür (288,55–289,25), ikinci kart için yer açılır.

## Olay ↔ sözcük t0
| Olay | Küresel sn | Sözcük (t0) |
|---|---|---|
| Kırmızı ünlem | 260,80 | tuzak. |
| Gelecek oku | 261,76 | Gelecek |
| Kart çerçevesi (kasıtlı −0,34) | 263,25 | The (263,59) |
| begins sarı daire | 264,23 | begins |
| Saat çizimi | 264,87 | eight |
| Takvim çizimi | 265,35 | tomorrow |
| ends sarı daire | 266,79 | ends |
| TR çeviri sözcük sözcük | 268,70 / 271,42 | Konser / ve |
| başlayacak altı çizgi (+0,12) | 270,82 | başlayacak (270,70) |
| Balon sözcükleri | 273,65–277,03 | Hocam, … mı? |
| Sarı nokta begin | 275,90 | begin |
| Parıltı begins/ends | 278,53 | gelecek, |
| Yakın çekim kutusu | 280,93 | Konser |
| «tarife» etiketi | 281,41 | tarifeye |
| Tablo çerçevesi | 282,69 | Program |
| 8:00 · 11:00 | 283,81 · 284,17 | saat · değişmez. |
| (özne cansız ya da kişi) | 285,25 | Özne |
| resmî program / tarife | 288,61 | resmî |
| → geniş zaman | 289,01 | program. |

Sapma: her `tb` `T(sözcük, yakın)` ile sozcukler.json'dan okunur (bulunamazsa sahne yüklenmez).

## Yapılan doğrulama (kapı yerine)
- `node --check` sahne.js, sahne-ortak.js: tamam.
- Sahte tarayıcı (mock canvas): kur() 0 hata, 47 örnek kare (ilk 12, son 12 dahil) 0 hata; ilk görünme karesi 36 (≥ 12); içerik karesi 901 ile 912 aynı çizim sayısı (son 12 kare durgun).
- Sönme gerçek alfa çarpanıyla (02-02 temel 07 kalıbı; 02-03 `solar` kalıbı kullanılmadı).

## Kapı çıktısı / kareler
Koşulmadı; `k/` boş. QA şeridi bakmalı: kart içi halkalar ile 2. satır (y 284–298), balon ve öğrenci başı (x 1090–1840, y 470–730), tablo (150–670, 575–795) ile sağ metin (x 800), küçülen kart kutuları.

## Açık notlar
- Ekran metnine ek: tablo hücrelerindeki «begins / ends» ve «8:00 / 11:00» cümleden türetildi (yeni içerik yok).
- Kartın küçülmesi sahne 12'de kalemle yeniden çizilir (BookFlip sürekliliği yok).


## QA 13.11
Kapı (sunucu): çakışma yok (121 örnek, 2061 kutu). Kareler: k/11-canvas-tuzak-konser-{262.6,271,279.4,289.1}.png (açık), k/koyu/ içinde (bakılmadı). Göz: şef maddesi 2: tablo hücresi '8:00 begins / 11:00 ends' anlatımda söyleniyor (c40 'saat sekizde başlayacak ve on bir civarı bitecek') → kalsın. Kart içi halkalar ile 2. satır arası temiz. Düzeltme yok. Kalan: yok.

QA 13.11 ek 2: Halka kuralı: begins ve ends halkaları (concert/and/at'a değiyordu) altçizgiye çevrildi. Kapı: çakışma yok (121 örnek, 2061 kutu); k/11-canvas-tuzak-konser-279.4.png temiz.

zaman eşitleme 13.11: cümle 30 +0,38 sn. Mutlak zamanlar +0,38 sn, TBAS 259,61→259,99 (35 sabit). Kapı: çakışma yok (121 örnek, 2061 kutu). Kareler 271,4 / 279,8 / 289,5 temiz; altçizgiler begins/ends sözcüğünden sonra.

QA 13.11 ek 3: simge–etiket/cümle taraması: çizimler cümleyle uyumlu (kod ve kareler üzerinden); uyuşmazlık yok.

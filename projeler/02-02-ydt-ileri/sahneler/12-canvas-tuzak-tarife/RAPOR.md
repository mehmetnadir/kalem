# Sahne 12 — Tuzak uçak ve tarife (düz canvas, 796 kare, t_bas 289,65, cümle 43–46)

Durum: P2 yazıldı; önizleme hazırlığı koşuldu (koyu, sonra açık tema son). Render, kapı ve sahne-kare YOK (şef EK 13.11 12:40).
Künye: SIMPLE PRESENT · YDT ADVANCED, çip "Trap", ajanda etkin Roots. Kırmızı kullanılmadı.

## İçerik
- Konser kartı küçük (y 150–300), ikinci kart (y 340–600): My flight … 6 … 4, takes off sarı daire, uçak.
- 44 TR çeviri (söner 299,97–300,27). 45 dört ikon (otobüs, uçak, müzik, okul) + etiketler, sarı tarife çizgisi (söner 308,10–308,42).
- 46 fark tablosu: kişisel plan → şimdiki zaman (We are taking the bus to Izmir tomorrow morning) | resmî program → geniş zaman (concert, flight).

## Olay ↔ sözcük t0
| Olay | Küresel sn | Sözcük (t0) |
|---|---|---|
| Küçük konser kartı | 290,08 | (ilk 12 kare sonrası) |
| Uçak çizimi | 290,44 | flight |
| takes off sarı daire | 290,80 | takes |
| TR çeviri | 295,23 / 297,27 | Uçağım / bu |
| Otobüs · uçak · müzik · okul | 300,34 · 300,98 · 301,66 · 302,38 | Tren, · uçak, · konser, · ders |
| Tarife çizgisi | 303,78 | tarife. |
| Parıltı | 306,66 | geniş |
| kişisel plan | 308,49 | Kendi |
| → şimdiki zaman | 309,77 | şimdiki |
| İngilizce örnek | 311,37 · 312,01 | yarın · İzmir'e |
| resmî program | 313,45 | Resmî |
| müzik + concert | 313,85 | program |
| uçak + flight | 314,37 | varsa |
| → geniş zaman | 314,89 | geniş |

## Yapılan doğrulama
- `node --check` tamam; sahte tarayıcı: 0 hata, 47 kare; ilk görünme karesi 13 (≥ 12); içerik karesi 784 ile 795 aynı çizim sayısı.

## Kapı çıktısı / kareler
Koşulmadı; `k/` boş. QA bakmalı: 1. satır sonu ile uçak (x ≈ 1500+), icon etiketleri (y 975, künye alt satırı y 1030), kart + ikon yoğunluğu (y 340–975).

## Açık notlar
- Uçak kalkış hareketi eklenmedi (nefes kapalı, statik).


## QA 13.11
Kapı (sunucu): çakışma yok (106 örnek, 2225 kutu). Kareler: k/12-canvas-tuzak-tarife-{292.3,299.6,306.9,315.3}.png (açık), k/koyu/ içinde (bakılmadı). Göz: şef maddesi 3: uçak ile 1. satır sonu arası boşluk yeterli, ikon etiketleri ile künye alt satırı çakışmıyor (etiket y~960, künye ~1020), y 340–975 yoğun ama okunur. Düzeltme yok. Kalan: yok.

QA 13.11 ek 2: Halka kuralı: 'takes off' halkası (flight/at'a değiyordu) altçizgiye çevrildi, 'takes' + 0,6 sn'de başlar. Kapı: çakışma yok (106 örnek, 2225 kutu); k/12-canvas-tuzak-tarife-299.6.png temiz.

zaman eşitleme 13.11: cümle 30 +0,38 sn. Mutlak zamanlar +0,38 sn, TBAS 289,65→290,03 (33 sabit). Kapı: çakışma yok (106 örnek, 2225 kutu). Kareler 300,0 / 307,3 / 315,7 temiz.

QA 13.11 ek 3: Simge–etiket uyuşmazlığı: anlatım 'Tren, uçak, konser, ders programı' (c45) diyor, 'tren' etiketinin üstünde otobüs çizimi vardı. Düzeltme: sahne klasörüne tren.svg (Tabler çizgi stilinde buharlı lokomotif + vagon) eklendi, sahne.js'te bus.svg yerine kullanıldı. Kapı: çakışma yok (106 örnek, 2225 kutu); k/12-canvas-tuzak-tarife-307.3.png: tren okunuyor, uçak/nota/okul simgeleri etiketleriyle uyumlu.

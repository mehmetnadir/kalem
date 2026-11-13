# Sahne 08 Karşıt çift 1 (yatay) — RAPOR (13.11)

Motor: Düz canvas · 1920×1080 · 30 fps · 646 kare (zaman.json ile birebir) · t_bas 109,61 · cümle 9

## Durum (13.11, makine yükü nedeniyle yalnız yazım + önizleme hazırlığı)

| Adım | Sonuç |
|---|---|
| sahne.js yazıldı | evet (`sahne-ortak.js` örnek 04'ün kopyası: 02-03 yolları + `etkin` parametresi) |
| `ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu` ve açık | "önizleme hazır" (son koşu AÇIK) |
| `node --check` | geçti |
| Çakışma kapısı (adım 3) | KOŞULMADI (şef EK 13.11 12:40: QA şeridi koşar) |
| Kare görüntüsü (adım 4) | KOŞULMADI; `k/` boş; göz kontrolü QA şeridinde |
| Düğüm sahte-tuval denemesi (tarayıcısız, açık + koyu) | kur + her kare çizildi, hata yok; ilk çizim kare ≥ 12; son olay < içerik karesi; kutu taşması ve yazı kesişimi 0 (yaklaşık yazı genişliği 0,52 em) |

Not: tarayıcıda gerçek Fredoka genişliği ölçülür; sahne yazı tipini satır genişliğine göre kendisi sığdırır (`olc`).
Künye çipi ve ajanda: sahne `etkin` ajanda indeksini `KUNYE.ajanda`dan ad eşlemesiyle bulur; şef ajandayı değiştirince kendiliğinden uyar
(bulamazsa 08/09 için Rule, 11 için Trap).

## İçerik

Tek kart (çerçeve kalemle) içinde cümle iki satır: satır 1 alışkanlık (`usually spends`), satır 2 şu an (`now`, `is meeting`).
Sinyal sözcükleri sarı belirteç, fiiller sarı daire, sinyalden fiile iki yay ok. Altta zaman çizgisi: sol bant 8 nokta
(alışkanlık, `usually`), sağda `now` noktası ve nabız. Soluk Türkçe çeviri yok (taslakta bu sahne için yok).

## Olay ↔ sözcük t0 (küresel sn; kare = round((t − 109,61) × 30); sapma ≤ 0,15)

| Olay | t (sn) | Kare | Sözcük | Sözcük t0 | Sapma |
|---|---|---|---|---|---|
| kart çerçevesi | 110,20 | 18 | Karşıt | 110,16 | +0,04 |
| eksen çizgisi | 116,30 | 201 | Nancy (TR) | 116,26 | +0,04 |
| alışkanlık noktaları + usually etiketi | 117,54 | 238 | genellikle | 117,54 | 0 |
| şimdi noktası | 119,38 | 293 | şu | 119,38 | 0 |
| now etiketi | 119,54 | 298 | anda | 119,54 | 0 |
| usually altı çizgi | 122,98 | 401 | sinyal, | 122,98 | 0 |
| now altı çizgi | 123,10 | 405 | sinyal, | 122,98 | +0,12 |
| spends daire | 123,78 | 425 | fiil | 123,78 | 0 |
| is meeting daire | 123,90 | 429 | fiil | 123,78 | +0,12 |
| usually → spends yay ok | 124,90 | 459 | Usually | 124,90 | 0 |
| spends parıltı | 126,98 | 521 | spends. | 126,98 | 0 |
| now → is meeting yay ok | 128,10 | 555 | Now | 128,10 | 0 |
| is meeting parıltı | 130,10 | 615 | meeting. | 130,10 | 0 |
| cümle (karaoke) | 111,53–115,21 | 58 | Nancy … now. | `sozcukler.json` | 0 |

İlk çizim kare 18 (≥ 12); son olay kare 615 (içerik 634'te biter, son 12 kare olaysız).
Kapı çıktısı: koşulmadı. Kare yolları: `k/` boş (koşulmadı).

## Açık nokta

- Zaman çizgisindeki iki küçük etiket (`usually`, `now`) taslak ekran metninde yok; cümledeki sinyal sözcüklerinin tekrarı. İstenmezse sahne.js'te iki `elYazisi` satırı silinir.

## QA 13.11
- Kapı: çakışma yok (86 örnek, 1519 kutu). Kareler `k/08-canvas-karsit1-{111,116,122,130}.png`, koyu `k/koyu/08-canvas-karsit1-121.png`.
- Göz: usually→spends ve now→is meeting okları, zaman çizgisi doğru; ikinci ok metne bitişik ama okunur. Düzeltme yok. Kalan sorun yok.
- zaman eşitleme 13.11: sabit mutlak zamanlar (sahne.js, 17 değer) −0,08 sn kaydırıldı, TBAS 109,53. Kapı: çakışma yok (86 örnek, 1519 kutu). Kareler `k/08-canvas-karsit1-{112.5,115.5,118.8,129.5}.png`.
- QA 13.11 ek (halka/kutu taraması): spends ve is meeting halkaları altçizgi oldu. Kapı: çakışma yok (86 örnek, 1519 kutu).

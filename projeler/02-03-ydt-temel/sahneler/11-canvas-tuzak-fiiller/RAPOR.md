# Sahne 11 Tuzak fiilleri (yatay) — RAPOR (13.11)

Motor: Düz canvas · 1920×1080 · 30 fps · 1150 kare (zaman.json ile birebir) · t_bas 188,50 · cümle 14

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

Sol sütun üç kart alt alta: (1) `We believe.` ✓ · `We are believing.` + `ing` üstüne sarı çarpı; (2) `It has a great view of the sea.` (`has` sarı kutu);
(3) `I definitely recommend a holiday in this lovely city.` (`recommend` sarı daire). Sağ köşe liste, sesle büyür: `believe · think · have (own)` →
`simple present`; `promise · agree · recommend`, `performative:` (el yazısı) → `NO -ing`. Kategori etiketi yalnız promise · agree · recommend için;
believe ve think'te etiket yok (D-0205). Sağ altta iki küçük ikon: güneş (view), yatak (holiday).

## Olay ↔ sözcük t0 (küresel sn; kare = round((t − 188,50) × 30); sapma ≤ 0,15)

| Olay | t (sn) | Kare | Sözcük | Sözcük t0 | Sapma |
|---|---|---|---|---|---|
| kart 1 çerçevesi | 189,30 | 24 | Olmaz. | 189,25 | +0,05 |
| liste: believe | 190,37 | 56 | Believe | 190,37 | 0 |
| liste: think | 191,17 | 80 | think | 191,17 | 0 |
| ok → simple present | 192,37 | 116 | geniş | 192,37 | 0 |
| We believe. (karaoke) | 193,82 | 160 | We | 193,82 | 0 |
| ✓ | 195,35 | 205 | Böyle | 195,35 | 0 |
| We are believing. (karaoke) | 196,88 | 251 | We | 196,88 | 0 |
| ing üstüne çarpı | 198,57 | 302 | Denmez. | 198,57 | 0 |
| liste: promise | 199,85 | 340 | Promise, | 199,85 | 0 |
| liste: agree | 200,85 | 370 | agree | 200,85 | 0 |
| liste: recommend | 201,45 | 388 | recommend | 201,45 | 0 |
| performative: (el yazısı) | 202,65 | 425 | performative | 202,65 | 0 |
| ok + NO -ing | 207,10 | 558 | -ing | 207,21 | −0,11 |
| kart 2 çerçevesi | 209,60 | 633 | İki tuzak | 209,53 | +0,07 |
| has kutusu | 210,42 | 658 | has | 210,42 | 0 |
| güneş ikonu | 210,74 | 667 | great | 210,74 | 0 |
| liste: have (own) | 212,83 | 730 | Have | 212,83 | 0 |
| parıltı (have) | 215,07 | 797 | -ing | 215,07 | 0 |
| kart 3 çerçevesi | 216,90 | 852 | I | 217,00 | −0,10 |
| recommend daire | 217,80 | 879 | recommend | 217,80 | 0 |
| yatak ikonu | 218,60 | 903 | holiday | 218,60 | 0 |
| listede recommend altı çizgi | 220,85 | 970 | Tavsiye | 220,85 | 0 |
| simple present altı çizgi | 225,97 | 1124 | zaman. | 225,97 | 0 |

İlk çizim kare 24; son olay kare 1124 (içerik 1138'de biter).
Kapı çıktısı: koşulmadı. Kare yolları: `k/` boş (koşulmadı).

## Açık noktalar

- Sağ alt iki ikon (güneş, yatak) taslakta yok; boş sağ alt köşeyi dengeler. İstenmezse sahne.js'te iki `cizim` bloğu silinir.
- `→` ve `≠` yazı tipinde yok; oklar ve ≠ kalemle çizilir.

## QA 13.11
- Önizleme hazırlığı sunucuda yapıldı (--hazirla, açık). Kapı: çakışma yok (153 örnek, 3281 kutu). Kareler `k/11-canvas-tuzak-fiiller-{189.5,195,205,225.5}.png`, koyu `k/koyu/`.
- Düzeltme: amaçsız güneş ve yatak simgeleri kaldırıldı (`sahne.js`).
- Göz: üç kart, ✓ ve çarpı, liste (believe·think·have → simple present; performative → NO -ing) taşmıyor, çarpı yalnız -ing üstünde. Kalan sorun yok.
- zaman eşitleme 13.11: cümle 14 sesi yeniden üretildi (−0,96 ile −1,68 sn, düzensiz kayma). sahne.js 27 mutlak zaman, eski→yeni sözcük çapalarıyla (25 çapa) parça parça eşlendi; TBAS 187,54, KARE 1131, ICERIK 1119. Kapı: çakışma yok (151 örnek, 3267 kutu). Doğrulama: ✓ 194,47 sözcüğünden sonra (kare 194,8), çarpı 197,29 (kare 197,6), has kutusu 208,82 (kare 208,9), recommend halkası 216,12 (kare 216,4), performative/NO -ing ve have (own) listesi sözcük sırasında; erken ya da geç işaret görülmedi.
- QA 13.11 ek (halka/kutu taraması): recommend halkası ve has kutusu altçizgi oldu. Kapı: çakışma yok (151 örnek, 3267 kutu). 224,75 karesinde simple present altçizgisi tam (öbeğin tamamı), recommend ve has altçizgileri komşu sözcüğe değmiyor (`k/11-canvas-tuzak-fiiller-{216.4,224.75}.png`). Sahne 224,85 sn'de bittiği için 228 sn karesi bu sahneye düşmez.

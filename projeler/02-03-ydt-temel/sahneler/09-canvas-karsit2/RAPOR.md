# Sahne 09 Karşıt çift 2–3 (yatay) — RAPOR (13.11)

Motor: Düz canvas · 1920×1080 · 30 fps · 1118 kare (zaman.json ile birebir) · t_bas 130,74 · cümle 10 ve 11

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

İki sol/sağ kart çifti, ortada kalemle ≠. Üst çift (cümle 10): `I am staying here for a week` (`for a week` sarı belirteç, TEMPORARY)
≠ `My holiday package includes trips…` (`includes` sarı daire, GENERAL). Alt çift (cümle 11): `The region offers…` (`offers` sarı
belirteç; sol altta sahil çizgisi: iki dalga, kıyı, şemsiye; GENERAL) ≠ `People are really enjoying themselves a lot here.`
(`are really enjoying` sarı daire; Open Peeps `standing-2` figürü; RIGHT NOW). Dört cümle aynı yazı tipi boyunda.

## Olay ↔ sözcük t0 (küresel sn; kare = round((t − 130,74) × 30); sapma ≤ 0,15)

| Olay | t (sn) | Kare | Sözcük | Sözcük t0 | Sapma |
|---|---|---|---|---|---|
| sol kart 1 | 131,35 | 18 | Kartpostaldan | 131,29 | +0,06 |
| for a week belirteç | 134,10 | 101 | for | 134,10 | 0 |
| TEMPORARY | 136,35 | 168 | geçici. | 136,35 | 0 |
| sağ kart 1 | 137,50 | 203 | My | 137,64 | −0,14 |
| includes daire | 138,92 | 245 | includes | 138,92 | 0 |
| ≠ (çift 1) | 142,05 | 339 | Paketin | 142,05 | 0 |
| GENERAL (çift 1) | 142,61 | 356 | genel | 142,61 | 0 |
| TEMPORARY altı çizgi | 145,33 | 438 | Geçici: | 145,33 | 0 |
| GENERAL altı çizgi | 147,33 | 498 | Genel: | 147,33 | 0 |
| sol kart 2 | 149,55 | 564 | Bir | 149,48 | +0,07 |
| offers belirteç | 151,33 | 618 | offers | 151,33 | 0 |
| sahil dalgası 1 | 154,30 | 707 | Bölgenin | 154,30 | 0 |
| sahil dalgası 2 | 154,86 | 724 | sahilleri | 154,86 | 0 |
| kıyı çizgisi | 155,58 | 746 | hep | 155,58 | 0 |
| şemsiye | 155,82 | 752 | orada. | 155,82 | 0 |
| GENERAL (çift 2) | 157,26 | 796 | Genel | 157,26 | 0 |
| sağ kart 2 | 159,80 | 872 | People | 159,91 | −0,11 |
| are really enjoying daire | 160,23 | 885 | are | 160,23 | 0 |
| figür | 163,76 | 991 | Bu | 163,76 | 0 |
| RIGHT NOW | 164,00 | 998 | şu | 164,00 | 0 |
| ≠ (çift 2) | 165,36 | 1039 | değil. | 165,36 | 0 |
| figür sıçrar + 4 ışın | 166,72 | 1079 | Şimdiki | 166,72 | 0 |

İlk çizim kare 18; son olay kare 1079 (içerik 1106'da biter).
Kapı çıktısı: koşulmadı. Kare yolları: `k/` boş (koşulmadı).

## Açık noktalar

- "Figür kollarını açar": Open Peeps `standing-2` tek duruş, kol hareketi yok. Yerine 0,47 sn sıçrama + iki yanda 4 sarı ışın. Kolları açık başka duruş istenirse svg adı tek satır.
- Figür konuşan karakter değil (genel "People"); K22 yalnız öğrenci sesi için geçerli.

## QA 13.11
- Kapı: çakışma yok (149 örnek, 4379 kutu). Kareler `k/09-canvas-karsit2-{132,142,155,167}.png`, koyu `k/koyu/09-canvas-karsit2-155.png`.
- Göz: dört kart, ≠ işaretleri, TEMPORARY/GENERAL/RIGHT NOW etiketleri, sahil ve figür çizimleri örtüşmüyor. Düzeltme yok. Kalan sorun yok.
- zaman eşitleme 13.11: sabit mutlak zamanlar (28 değer) −0,08 sn kaydırıldı, TBAS 130,66 (cümle 10 ve 11 sesi değişmedi). Kapı: çakışma yok (149 örnek, 4379 kutu). Kareler `k/09-canvas-karsit2-*.png`.
- QA 13.11 ek (halka/kutu taraması): includes ve are really enjoying halkaları altçizgi oldu. Kapı: çakışma yok (149 örnek, 4379 kutu). Kare `k/09-canvas-karsit2-160.5.png`.

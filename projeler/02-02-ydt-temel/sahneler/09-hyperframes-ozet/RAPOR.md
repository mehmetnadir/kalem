# Sahne 09 — Ara özet (HyperFrames, 1083 kare = 1071 içerik + 12 geçiş; t_bas 280,71)

Tema: acik

Durum: önizleme hazır (koyu, sonra açık). Render, kapı ve kare görüntüsü bu turda YOK (şef EK 13.11 12:40).

## İçerik
- `ozet` beş madde kademeli (sarı el madde işareti): rutin · kalıcı durum · genel gerçek · he · she · it → s (s sarı kutu) · don't / doesn't · Do / Does (altı sarı çizgi: s yardımcı fiile geçer).
- Sıklık ölçeği (yatay ok, 100 % → 0 %): always usually often sometimes never, her biri söylenince halka + etiket; `every` ayrı etiket kutusunda (ölçeğin dışı).
- Tekrar sayısı kalıpları ayrı etiket satırı: once a week · on Mondays · in the mornings.
- Sağda Caveat kapanış notu: "önce geniş zamanı düşün" (altı sarı çizgi) · "kesin kural değil," · "ilk akla gelen zaman bu."
- Künye: bölüm `Summary`, ajanda etkin 4. sözcük (Trap) — ajandada özet için ayrı sözcük yok.

## Olay ↔ sözcük t0 (sapma ≤ 0,15; küresel sn, yerel = küresel − 280,71)
| Olay | Cümle / sözcük | Sözcük t0 | Olay küresel | Yerel | Sapma |
|---|---|---|---|---|---|
| madde 1 `rutin` | 51 rutini, | 283,10 | 283,10 | 2,39 | 0,00 |
| madde 2 `kalıcı durum` | 51 kalıcı | 283,82 | 283,82 | 3,11 | 0,00 |
| madde 3 `genel gerçek` | 51 genel | 284,86 | 284,86 | 4,15 | 0,00 |
| `s` kutusu (he · she · it → s) | 52 se | 288,86 | 288,86 | 8,15 | 0,00 |
| madde 5 `don't / doesn't` | 52 Olumsuzda | 289,90 | 289,90 | 9,19 | 0,00 |
| `always` halka + etiket | 53 always, | 296,62 | 296,62 | 15,91 | 0,00 |
| `never` halka + etiket | 53 never. | 300,94 | 300,94 | 20,23 | 0,00 |
| kalıp `once a week` | 53 once | 306,00 | 306,00 | 25,29 | 0,00 |
| not `önce geniş zamanı düşün` | 53 önce | 311,61 | 311,61 | 30,90 | 0,00 |
| not `ilk akla gelen zaman bu.` | 53 ilk | 315,01 | 315,01 | 34,30 | 0,00 |

## Kontroller (kapı/görüntü yok)
- Uret sırasında taşma sınaması (assert): madde satırı, kalıp çipleri sığıyor. `node --check` 2 blok OK · yinelenen id yok · negatif zaman yok.
- İlk hareket 0,55 sn (kare 16), son hareket 35,20 sn (içerik 35,70 sn). olaylar.json 32 olay (kare 16–1029).

## Açık
- Ajandada özet sözcüğü yok; Trap etkin bırakıldı (şef künye karar verir).

## QA 13.11
- Kapı: ölçülmedi (HyperFrames). Kareler k/09-…-285, -295, -305, -314, k/koyu/…-300. Göz: 5 madde, ölçek, "every" kutusu, "tekrar sayısı:" etiketi okunur; boşluk/taşma yok. Düzeltme yok, kalan yok.

- Halka kuralı: dokunulmadı. Madde ve ölçek noktaları (el_daire 15/13 px) yazıdan ayrı, metne değmiyor; kare k/…-305 doğrulandı.

- zaman eşitleme 13.11: KARE 1083 aynı (+1,02 sn kayma sözcükten okunuyor); --hazirla ile yeniden kuruldu; kareler k/…-290…316.

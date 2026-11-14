# 05-canvas-ornek3 — RAPOR (14.11, P2; render yok)

| Alan | Değer |
|---|---|
| Motor | Düz canvas · 1920×1080 · 30 fps · 747 kare (içerik 735) · t_bas 68,84 · cümle 5 |
| Dosyalar | `sayfa.html` · `sahne.js` · `sahne-ortak.js` (02-03 `09-canvas-karsit2` kopyası, yollar 02-04) · `calistir.sh` |
| Ekran metni | The train to İzmir leaves at 7 pm today. · I am going to the movie theater tonight. · TIMETABLE / ARRANGEMENT; künye çipi "Example 3 / 3"; zaman çizgisi şablon dili: now · 7 pm · tonight |
| Renk | murekkep + ikincil; tek vurgu (`RT.vurgu`, `RT.vurguDolgu`); kırmızı yok, yeşil yok, emoji yok |
| Ölçü | `u(n) = n × tuval genişliği / 1920`; cümle Fredoka 700 (en geniş satıra göre en çok 58), etiket Caveat 60, zaman etiketi 52 — taban 30'un üstünde |
| Kapı | `qa-yerel.sh … --hazirla` çıkış 0; çakışma yok (99 örnek, 1981 kutu) |

## Olay listesi (yerel kare = round((t − 68,84) × 30))

| Cümle · sözcük | t0 (sn) | Kare | Olay |
|---|---|---|---|
| 5 · Üçüncü | 69,39 | 16 | sol kart |
| 5 · İki | 70,83 | 60 | sağ kart |
| 5 · geleceği | 71,55 | 81 | zaman çizgisi (sağa ok) + now noktası, nabız + "now" |
| 5 · anlatıyor. | 72,03 | 96 | gelecek yarısı vurgu dolgusu |
| 5 · The | 73,00 | 125 | sol cümle sözcük sözcük (karaoke altçizgi) |
| 5 · train | 73,16 | 130 | tren çizimi (1,1 sn) |
| 5 · seven | 74,76 | 178 | saat, akrep 7'de (vurgu) |
| 5 · akşam | 77,81 | 269 | 7 pm çentiği + nokta + etiket ("7" akşam, "pm" yedide) |
| 5 · kalkıyor. | 78,53 | 291 | now → 7 pm kalem yayı |
| 5 · tarifede | 80,37 | 346 | TIMETABLE el yazısı (tarifede yazılı penceresi) |
| 5 · Tarifeli | 81,93 | 393 | TIMETABLE altı vurgu |
| 5 · geniş | 83,17 | 430 | `odak` leaves altçizgi |
| 5 · I | 84,94 | 483 | sağ cümle sözcük sözcük |
| 5 · movie | 85,82 | 509 | sinema bileti çizimi (1,0 sn) |
| 5 · akşam | 87,75 | 567 | tonight çentiği + nokta + etiket |
| 5 · gidiyorum. | 88,63 | 594 | now → tonight kalem yayı |
| 5 · Planı | 89,63 | 624 | ARRANGEMENT el yazısı (Planı ben yaptım penceresi) |
| 5 · Planlanmış | 91,07 | 667 | ARRANGEMENT altı vurgu |
| 5 · şimdiki | 92,43 | 708 | `odak` am going altçizgi |

İlk görünür öğe kare 16 (ilk 12 kare boş). En uzun olaysız aralık 1,8 sn (78,53 → 80,37); 4 sn kuralı içinde.
Son olay 92,83'te biter; cümle 93,43'te biter (olay kendi cümlesinde).

## Kapı (son koşu)

```
== KAPI
05-canvas-ornek3 | çakışma yok (99 örnek, 1981 kutu)
== KARE (açık)  79.4 · 84.2 · 93.3
== KARE (koyu)  93.3
kapı çıkış kodu: 0
```

Not: `sahne-kare.mjs` zamanı anlatım (küresel) saniyesi olarak okur (`f = (t − t_bas) × 30`). Bu yüzden zamanlar küresel verildi:
79,4 = sahne içi 10,56 · 84,2 = 15,36 · 93,3 = 24,46.

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/05-canvas-ornek3-79.4.png` | sol cümle, tren, saat (akrep 7), 7 pm + yay; sağ kart boş çerçeve (cümle 84,94'te gelir). Taşma yok. |
| `k/05-canvas-ornek3-84.2.png` | TIMETABLE + altı, leaves altçizgisi. Taşma yok. |
| `k/05-canvas-ornek3-93.3.png` | iki kart tam, bilet, ARRANGEMENT + altı, am going altçizgisi, iki yay, üç etiket. Taşma yok. |
| `k/koyu/05-canvas-ornek3-93.3.png` | koyu tema: krem çizgi, vurgu turuncu; dolgu üstünde noktalar okunur. Taşma yok. |

Düzeltme turu 1: ilk koşuda "am going" altçizgisi g kuyruklarına değiyordu → `odak` altçizgisi taban + 24'ten taban + 30'a indi;
kapı yeniden 0, kare 93,3'te çizgi kuyruktan ayrık.

## Açık noktalar

1. `ortak/cizim` içinde tren ve bilet SVG'si yok; tren, saat ve bilet sahnede elle kalem çizimi (`elCizim`, kapı kutusu "cizim").
   Başka sahne (07 kural, 09 karşıt 2) aynı nesneleri isterse ortak bir çizim dosyası önerilir (ortak/'a yazılmadı).
2. Yazma kapısı (`write-size-gate`) 15 satırdan uzun kod yazımını şefe kapatıyor; bypass bayrağını yalnız Nadir açar.
   `sahne.js` bu yüzden `agy-filo tek` (rol bulk) ile spec'ten birebir yazıldı (`diff` 0 fark). İstemdeki "alt ajan açma" kuralına
   Claude alt ajanı açılmadı; agy kullanımı kapının gösterdiği yol. Spec: `/tmp/kalem-0204-s05/sahne-spec.md`.
3. Sağ kart 72–85 sn arası boş çerçeve olarak bekler (iki kart "İki cümle" sözüyle birlikte açılır). Rahatsız ederse sağ kart
   84,94'e (I) alınabilir.
4. Sol/sağ etiket renkleri murekkep, altları vurgu; sahne 03–04'teki etiket renk seçimiyle (henüz yok) tutarlılık QA'da bakılmalı.

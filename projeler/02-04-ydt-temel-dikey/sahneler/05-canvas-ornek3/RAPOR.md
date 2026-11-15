# 05-canvas-ornek3 DİKEY — RAPOR (15.11, render yok)

Tema: koyu

| Alan | Değer |
|---|---|
| Motor | Düz canvas · 1080×1920 · 30 fps · 747 kare (içerik 735) · t_bas 68,84 · cümle 5 (49 sözcük) |
| Dosyalar | `SPEC.md` (şef) · `sahne.js` (agy, 554 satır) · `sahne-ortak.js`, `sayfa.html` (04 dikeyin birebir kopyası) · `calistir.sh` (04 dikey kopyası; N 747, t_bas 68,84, klasör) |
| Ekran metni | `The train to İzmir / leaves at 7 pm today.` · `I am going to the / movie theater tonight.` · TIMETABLE · ARRANGEMENT · şerit `leaves → TIMETABLE` · zaman çizgisi `now` · `7 pm` · `tonight`; çip `Example 3 / 3` |
| Ölçü | cümle Fredoka 700 72 (satır 92 / 100) · etiket Caveat 72 el yazısı · zaman etiketi Caveat 64 el yazısı · şerit 64 · tren 688×290 · saat r 150 · bilet ≈ 808×354 · simge 237×100 |
| Renk | `RT.*` yalnız; tek vurgu (altçizgi, akrep, now noktası); kırmızı, ham yeşil, emoji yok |
| Kapı | `qa-yerel.sh … --hazirla` çıkış 0; çakışma yok (99 örnek, 1571 kutu) |

## Olay listesi (yerel kare = round((t − 68,84) × 30))

| Sözcük | t (sn) | Kare | Olay |
|---|---|---|---|
| geleceği | 71,55 | 81 | zaman ekseni (y 1310, x 96→984, ok) |
| geleceği | 71,80 / 71,95 | 89 / 93 | now noktası + nabız · `now` el yazısı |
| anlatıyor. | 72,03 | 96 | gelecek bandı (`vurguDolgu` %45, açık uçlu) |
| — | 72,60 | 113 | kart A çerçevesi (y 380–620; ilk sözcükten 0,40 sn önce) |
| The … today. | 73,00–76,44 | 125 | kart A cümlesi sözcük zamanlı, karaoke altı |
| train | 73,16 | 130 | tren çizimi (1,1 sn) |
| seven | 74,76 | 178 | saat, akrep 7'de (vurgu) |
| akşam / yedide | 77,81 | 269 | 7 pm çentiği + nokta + `7 pm` (iki sözcük penceresi) |
| kalkıyor. | 78,53 | 291 | now → 7 pm kalem yayı |
| tarifede | 80,37 | 346 | TIMETABLE el yazısı (y 1150) |
| Tarifeli | 81,93 | 393 | TIMETABLE altı |
| geniş | 83,17 | 430 | `odak` *leaves* |
| — | 84,24–84,60 | 462–473 | grup A küçülür ve söner (çift kart kuralı) |
| — | 84,54–84,72 | 471–476 | şerit: `leaves` → ok → `TIMETABLE` + tren simgesi |
| I | 84,60 | 473 | kart B çerçevesi (y 490–730; ilk sözcükten 0,34 sn önce) |
| I … tonight. | 84,94–87,42 | 483 | kart B cümlesi sözcük zamanlı |
| movie | 85,82 | 509 | sinema bileti (1,0 sn) |
| akşam | 87,75 | 567 | tonight çentiği + nokta + `tonight` |
| gidiyorum. | 88,63 | 594 | now → tonight kalem yayı |
| Planı | 89,63 | 624 | ARRANGEMENT el yazısı (y 1200) |
| Planlanmış | 91,07 | 667 | ARRANGEMENT altı |
| şimdiki | 92,43 | 708 | `odak` *am going* (taban + 0,48 em, g kuyruğunun altı) |

İlk görünür öğe kare 81 (ilk 12 kare boş). Son hareket 92,83'te (kare 720) biter; son 12 kare durgun (nabız `ICERIK` 735'te durur).
En uzun olaysız aralık 1,4 sn (76,44 → 77,81). Boş çerçeve en çok 0,40 sn bekler. Aynı anda en çok 2 sarı altçizgi.

## Kapı (son koşu)

```
== HAZIRLA
tema: acik
önizleme hazır
== KAPI
05-canvas-ornek3 | çakışma yok (99 örnek, 1571 kutu)
== KARE (açık)  79.4 · 84 · 93.3
== KARE (koyu)  93.3
kapı çıkış kodu: 0
```

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/05-canvas-ornek3-79.4.png` | kart A tam, tren + saat (akrep 7) bant ortasında, 7 pm çentiği + yayı. Taşma yok. |
| `k/05-canvas-ornek3-84.png` | TIMETABLE + altı, *leaves* altı. Bant dolu. Taşma yok. |
| `k/05-canvas-ornek3-93.3.png` | şerit (`leaves → TIMETABLE` + tren simgesi), kart B, bilet, ARRANGEMENT + altı, *am going* altı, iki yay, üç etiket. Bant dolu; ARRANGEMENT altı ile tonight yayı arası ≈ 30 px. |
| `k/koyu/05-canvas-ornek3-93.3.png` | koyu tema: krem çizgi, vurgu turuncu, gelecek bandı koyu turuncu; noktalar okunur. |
| `k/ek/ek-4lu.png` (72,2 · 84,42 · 86,3 · 89,2) | zaman çizgisi çizilirken · grup A küçülürken (kutu yazmaz) · kart B + bilet çizilirken · ARRANGEMENT öncesi. Sorun yok. |
| `k/ek/going-kirp.png` (85,4) | *going* karaoke altı g kuyruğunun altından geçer, değmez. |

Düzeltme turu: 0 (ilk koşu geçti).

## agy koşusu

`agy-filo tek --rol kod` · gemini-3.8-flash-high · 262 sn · başarılı. Özet: `/home/sef/.claude/canavar/agy-filo/20261115-121233/ozet.md`.
Şef sahne.js'i baştan sona okudu; SPEC'e uyuyor, düzeltme gerekmedi. Özetin "değişen" listesindeki öteki dosyalar
(03-paperjs-ornek1, 02-04-ydt-temel-s1/s2/s3) agy çıktısında geçmiyor; koşu penceresinde eşzamanlı oturumların yazdığı dosyalardır.

## Açık noktalar

1. **Tren yüksekliği.** BRIEF "Tren y 640–1060 (420 px)" der. Yan görünüş tren (oran ≈ 2,4 : 1) saatle aynı satırda 984 px'e
   sığarken ≈ 290 px yükseklik alır (x 48–736, y 710–1000); saat 300 px. 420 px için seçenek: saati trenin üstüne almak ya da
   vagonu çıkarmak (tek kaynak çizim değişir). Şef / Nadir kararı.
2. **Sahne başı.** 69,24–71,55 içerik bandı boş ("Üçüncü örnek." söylenir), 71,55–72,60 yalnız zaman çizgisi var (4 sn kuralı içinde).
   04'teki "daire içinde 2" benzeri bir "3" BRIEF'te yok; eklenmedi.
3. **olaylar.json ve video yok.** Render yasak (`ONIZLE_YALNIZ=1`); `olaylar.json` yakalama koşusunda üretilir.

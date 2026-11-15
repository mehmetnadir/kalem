# 09-canvas-karsit2 DİKEY — RAPOR (15.11; render yok)

Tema: koyu

| Alan | Değer |
|---|---|
| Motor | Düz canvas · 1080×1920 · 30 fps · 523 kare (içerik 511) · t_bas 145,29 · t_son 162,33 · cümle 10 (37 sözcük) |
| Dosyalar | `SPEC.md` (şef tasarımı) · `sahne.js` (agy yazdı, 696 satır) · `sahne-ortak.js` (05-canvas-ornek3 dikey kopyası, `cmp` aynı) · `sayfa.html` (aynı) · `calistir.sh` (05 kalıbı; N, KLASOR, TBAS, GLOBAL_SN değişti) |
| Ekran metni | şerit `is wearing … today → this day only` + tişört simgesi · kart `The train to İzmir / leaves at 7 pm today.` + tren · not `today + 7 pm → timetable` · zaman çizgisi `now`, `7 pm` · alt `RIGHT NOW ≠ TIMETABLE`; çip `Contrast 2 / 2` |
| Renk | yalnız `RT.*`; tek vurgu `RT.vurgu`; karaoke `vurguDolgu` (kit); today bandı `vurguDolgu` %32; yeşil, kırmızı, emoji yok |
| Ölçü | kart cümlesi Fredoka 72 · şerit Fredoka/Caveat 56 (§ Açık nokta 2) · not satırı el yazısı 72 · etiketler el yazısı 64 · tren 267×112 px · tişört simgesi 96 px |
| Kapı | `qa-yerel.sh … --hazirla` çıkış 0; `çakışma yok (69 örnek, 1448 kutu)` |

## Yerleşim (BRIEF-DIKEY §3 satır 9; 08–09 ortak ölçüleri)

```
 352–472  şerit: is wearing … today → this day only                  [tişört 96]
 490–760  kart:  The train to İzmir                                  [tren, sağ üst iç köşe]
                 leaves at 7 pm today.          (satır tabanı 600 / 700)
 860      not:   today + 7 pm → timetable       (el yazısı 72)
1040–1180 today bandı x 200–880 + uç çentikleri
1180      eksen 96 → 984 · now ● 360 (nabız) · 7 pm ● 780 · yay now → 7 pm (bant içi)
1240      now · 7 pm etiketleri
1370      RIGHT NOW      ≠ (x 570)      TIMETABLE
1400–1536 altyazı (kit) · 1536–1920 boş
```

## Olay listesi (yerel kare = round((t − 145,29) × 30); t küresel sn)

| # | Olay | t (sn) | Kare | Cümle 10 sözcüğü |
|---|---|---|---|---|
| 0 | Kare 0–12 durgun 08 son düzeni: üst not `today`, kart `She is wearing her / pink T-shirt today.`, tişört + sarı halka, *is wearing* sarı altı, *today* altları ikincil, not `today → this day only`, bant, eksen, now + nabız, `now` (olaysız) | — | 0 | — |
| 1 | 08 düzeni şeride küçülür ve söner (0,24 sn) | 145,72 | 13 | — |
| 2 | Yeni kart çerçevesi | 145,80 | 15 | — (The 145,84) |
| 3 | Kart cümlesi sözcük sözcük + karaoke altı | 145,84–148,80 | 17 | The … today. |
| 4 | Şerit çerçevesi · metin 145,96 · ok 146,02 · tişört simgesi 146,04 · `this day only` 146,08 | 145,92 | 19 | — |
| 5 | Tren simgesi (kartın sağ üst iç köşesi) | 146,00 | 21 | train |
| 6 | Not `today` | 149,69 | 132 | today |
| 7 | *7 pm* sarı altı (dar öbek → `alti`) | 150,57 | 158 | saatle |
| 8 | Not `+ 7 pm` | 151,05 | 173 | geliyor: |
| 9 | Zaman çizgisinde 7 pm çentiği + nokta (x 780, bandın içinde) | 151,85 | 197 | akşam |
| 10 | `7 pm` etiketi | 152,25 | 209 | yedi. |
| 11 | now → 7 pm kalem yayı | 153,45 | 245 | henüz |
| 12 | Not oku + `timetable` (155,23–155,96) | 154,93 | 289 | tarifede · yazılı. |
| 13 | *leaves* sarı altı | 156,09 | 324 | Geniş |
| 14 | İki *today* sarı altı (şerit + kart); *7 pm* altı ikincile döner | 157,21 | 358 | Today |
| 15 | `≠` (kalem, 3 darbe) | 159,05 | 413 | Farkı |
| 16 | `RIGHT NOW` (now altında) | 160,57 | 458 | konuşma · anı |
| 17 | `TIMETABLE` (7 pm altında; 162,11'de biter) | 161,61 | 490 | tarife |

Sarı sayımı: en çok 3 (157,21: leaves + iki today). Boş çerçeve: kart 0,04 sn, şerit 0,04 sn. En uzun olaysız aralık 3,5 sn
(146,20 → 149,69; karaoke 148,80'e kadar sürer). Son hareket kare 505; son 12 kare durgun.

## Kapı (son koşu)

```
yuva 1 · kök /home/sef/01dev/_worktrees/kalem-0204 · önizleme 41022 · cdp 41333
== HAZIRLA
tema: acik
önizleme hazır
== KAPI
09-canvas-karsit2 | çakışma yok (69 örnek, 1448 kutu)
== KARE (açık)  149 · 156.6 · 162.2
== KARE (koyu)  162.2
kapı çıkış kodu: 0
```

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/09-canvas-karsit2-149.png` | şerit + tişört simgesi, kart cümlesi tam, tren köşede; karaoke *today.* altında; bant, now. Taşma yok. |
| `k/09-canvas-karsit2-156.6.png` | not satırı tam, 7 pm çentik + etiket + yay; *leaves* ve *7 pm* sarı altı. Taşma yok. |
| `k/09-canvas-karsit2-162.2.png` | iki *today* sarı, *7 pm* altı ikincil; `RIGHT NOW ≠ TIMETABLE` altyazı bandının üstünde (taban 1370). Çakışma yok. |
| `k/koyu/09-canvas-karsit2-162.2.png` | koyu tema: krem yazı, turuncu vurgu, bant koyu turuncu %32; yazılar okunur. |
| ek (scratchpad, `/tmp/s09olc/k/`): 145,4 · 145,82 · 146,5 | kare 0 = 08 düzeni tam; küçülme ortası ve şerit belirmesi temiz; yeni kart altında eski düzen kalmıyor. |

Düzeltme turu: 0 (ilk koşuda kapı 0, kare bulgusu yok).

## agy koşusu

`agy-filo tek --rol kod` (gemini-3.8-flash-high), 262 sn, başarılı. Özet: `/home/sef/.claude/canavar/agy-filo/20261115-122540`.
Şef okuması: kod SPEC'e uyuyor; Edit düzeltmesi gerekmedi. `node --check` geçti, satır ≤ 100.
Özet "değişen" listesindeki 06/07 dosyaları ve `.claude/docs/sozlesme.md` eş-oturumların işi (aynı worktree); agy yalnız `sahne.js` yazdı.

## Açık noktalar

1. Dikey 08 (`08-canvas-karsit1`) bu koşuda dizinde yoktu. Kare 0 BRIEF ortak ölçülerinden kuruldu: üst not `today` (Caveat 80,
   taban 450), kart satır tabanı 600 / 700, tişört 220 px x 772–992 + halka, not satırı `today → this day only` (taban 860), bant
   dolgu x 200–880 y 1040–1180. 08 yazılınca kare 0 ile 08 son karesi karşılaştırılmalı; farkı `ogelerH` sabitleri giderir.
2. Şerit 56 px: 64 px'te `is wearing … today → this day only` + 96 px simge 1032'yi aşar (ölçüm 999 px + simge). BRIEF §2.10
   küçülünce ≥ 48 kuralına uyar; §2.5'teki 64 değerinden sapmadır.
3. Altyazı (kit, `altyazi.json`) ses metnini yazar: `Izmir`, `seven p.m.`. Ekran metni (`İzmir`, `7 pm`) karttadır. Ortak
   altyazı dosyası bu sahnenin kapsamı dışında.
4. Not satırı (880) ile bant üstü (1040) arasında 160 px boşluk var; ölçüler 08–09 ortak sabitleridir, değiştirilmedi.
5. `olaylar.json` / `zamanlar.json` yalnız render koşusunda (`calistir.sh` yakala) üretilir; render yapılmadı.

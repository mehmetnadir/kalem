# Sahne 08 Karşıt çift 1 (DİKEY) — RAPOR (15.11)

Tema: koyu

Motor: düz canvas · 1080×1920 · 30 fps · 459 kare (içerik 447) · t_bas 130,40 · t_son 145,29 · cümle 9 · çip `Contrast 1 / 2`

## Durum

| Adım | Sonuç |
|---|---|
| Dosyalar | `SPEC.md` (şef), `sahne.js` (agy, 375 satır), `sahne-ortak.js` + `sayfa.html` (04 dikey kopyası, sha 215101d1…), `calistir.sh` |
| `node --check sahne.js` | geçti |
| `ONIZLE_YALNIZ=1` (`--hazirla`) | "önizleme hazır" |
| Kapı `qa-yerel.sh … 138.3,141.2,145.25 143.6 --hazirla` | çıkış kodu 0; çakışma yok (61 örnek, 660 kutu) |
| Ek kareler (`--kapisiz`) 131.5, 136.6, 139.6 · koyu 137.2 | altyazı ve açılış denetimi |
| Göz kontrolü | sorun yok; düzeltme turu 0 |
| mp4 render | YOK (istem gereği) |

## Yerleşim (08–09 ortak ölçüler)

```
 378–470  today (Caveat 80, x 88)                         başlık notu
 490–760  kart: She is wearing her / pink T-shirt today.  Fredoka 72, taban 596/688 · tişört 220 px sağ iç köşe
 790–880  ↳ this day only (Caveat 72)                     kanca ok kartın today'sinin altından
1040–1180 today bandı x 200–880 (vurguDolgu %45) + iki uç çentiği
1180      eksen x 96–984, sağ ok · now noktası x 360 + nabız
1252      now (Caveat 64)
```

## Olay ↔ sözcük (küresel sn; kare = round((t − 130,40) × 30))

| Olay | t (sn) | Kare | Cümle 9 sözcüğü |
|---|---|---|---|
| `today` başlık notu yazılır | 134,95–135,35 | 137 | today. |
| kart çerçevesi (ilk sözcükten 0,50 sn önce) | 135,11 | 141 | today. |
| cümle sözcük sözcük (karaoke altı) | 135,61–137,69 | 156–219 | She … today. (EN, yatay `EN`) |
| tişört kalemle | 136,87 | 194 | T-shirt |
| zaman çizgisi ekseni | 138,57 | 245 | Burada |
| odak *today* kartta + notta (çoklu) | 139,21 / 139,29 | 264 / 267 | today |
| today bandı + uç çentikleri | 139,93 / 140,03 / 140,15 | 286–292 | bugünü |
| kanca ok (↳) | 140,05–140,35 | 290–299 | bugünü |
| `this day only` yazılır | 140,29–140,89 | 297–315 | gösterir. |
| tişört sarı halkası; nottaki today `ikincil`e döner | 141,77 | 341 | kıyafet: |
| now noktası + nabız | 142,57 | 365 | konuşma |
| `now` etiketi | 143,05 | 380 | anında |
| odak *is wearing*; karttaki today `ikincil`e döner | 144,37 | 419 | şimdiki |

İlk öğe kare 137 (≥ 12). Son hareket 144,77'de biter (kare 431); nabız kare 447'de durur; son 12 kare durgun.
Son düzende sarı belirteç 3: halka + *is wearing* + now noktası (eski iki today altı `ikincil`).

## Altyazı (sahne içi düzeltme)

`ortak/anlatim/altyazi.json` cümle 9: EN parçası `138,57–142,97`, son TR parçası `143,05–145,37` yazılı; ses EN'yi
135,61–137,69'da, son TR parçasını 138,57'de başlatıyor. Kit olduğu gibi çizseydi EN söylenirken altyazı boş, "Burada today…"
söylenirken EN görünürdü. `sahne.js` `altyaziDuzelt()` yalnız bu sahnenin `S.K.altyazi` kopyasını düzeltir (`ortak/`a yazmaz):
EN → 135,61–137,69; son TR parçası `S.sozc[8..19]` sözcük zamanıyla ≤ 2 satır dilim (kit kuralı). Kare 136,6'da EN, 139,6 ve
141,2'de "Burada today … şimdiki", 145,25'te "zaman." görünüyor.

## Kapı çıktısı (son satırlar)

```
== KAPI
08-canvas-karsit1 | çakışma yok (61 örnek, 660 kutu)
== KARE (açık)
".../08-canvas-karsit1-138.3.png" · "...-141.2.png" · "...-145.25.png"
== KARE (koyu)
".../koyu/08-canvas-karsit1-143.6.png"
kapı çıkış kodu: 0
```

## Bakılan kareler

| Kare | Görünen | Bulgu |
|---|---|---|
| `k/08-canvas-karsit1-131.5.png` (açık) | HUD + altyazı cümle 9 TR 1 | içerik bandı boş (BRIEF planı, açık nokta 1) |
| `k/08-canvas-karsit1-136.6.png` (açık) | başlık notu, kart, cümle `pink`e kadar | altyazı EN doğru; taşma yok |
| `k/08-canvas-karsit1-138.3.png` (açık) | not + kart + cümle + tişört | temiz; sessizlikte altyazı boş (137,69–138,57) |
| `k/08-canvas-karsit1-139.6.png` (açık) | iki today sarı altı, eksen | temiz |
| `k/08-canvas-karsit1-141.2.png` (açık) | ↳ this day only, bant + çentikler | temiz; `this day only` sağ ucu ≈ 1005 (≤ 1032) |
| `k/08-canvas-karsit1-145.25.png` (açık) | son düzen | temiz; halka karta ve cümleye değmiyor; 3 sarı |
| `k/koyu/08-canvas-karsit1-143.6.png` (koyu) | aynı düzen, koyu zemin | okunur; bant koyu hardal, now noktası belirgin |

## agy koşusu

`agy-filo tek --rol kod` · gemini-3.8-flash-high · başarılı · 232 sn · özet `/home/sef/.claude/canavar/agy-filo/20261115-121950`.
Tek tur; şef düzeltmesi yok. Özetin "değişen" listesindeki 06, 09, 11 ve `sozlesme.md` dosyaları paralel oturumlarındır
(`sahne.js` dışında bu dizinde agy yazımı yok; mtime 12:23:21).

## Açık noktalar

1. **Açılış boşluğu:** 130,80 (geçiş sonu) → 134,95 arası içerik bandı boş, ≈ 4,15 sn (BRIEF §2.10 "≤ 4 sn durağanlık").
   BRIEF kartı 130,95'ten kaldırdı (4,7 sn boş çerçeve). Ses "Karşıt çift. İki cümlede aynı sözcük var:" diyor; ekran metni
   listesinde karşılığı yok. Karar şefte: kabul ya da 130,95'te bir açılış öğesi (ör. kalıcı kalan bir başlık).
2. **altyazi.json cümle 9 zamanı** ortak veride yanlış (yukarıda); sahne kendi kopyasını düzeltti. Ortak düzeltme gelirse
   `altyaziDuzelt()` aynı sonucu verir (sözcük zamanından türetir). Yatay 08 ve HyperFrames birleştirmesi etkilenebilir.
3. **Son altyazı dilimi tek sözcük** (`zaman.`, 144,77–145,37): kit kuralı açgözlü dilim; cümle sınırında bölme daha iyi okunur.
4. **Başlık notu `today` + not satırı:** BRIEF hem `today` notunu y 380–470'e hem `this day only`yi not satırına (790–880)
   koyuyor. Not satırı kanca okla kartın *today*'sine bağlandı (`today. ↳ this day only`). Sahne 09 145,72'de başlık notunu da
   şeride toplamalı (kare 0 = bu düzen).
5. Tişört 220 px (BRIEF satır 8); genel ölçek kuralı nesne 420–560 px. Kart içi simge olduğu için BRIEF satırı uygulandı.

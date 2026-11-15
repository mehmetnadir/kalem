# 04-canvas-ornek2 DİKEY — RAPOR (15.11, D-dikey; render yok)

Tema: koyu

Motor: düz canvas · 1080×1920 · 30 fps · 762 kare (içerik 750) · t_bas 43,85 · t_son 68,84 · cümle 4 · çip `Example 2 / 3`
(`KUNYE.cipler`). BRIEF-DIKEY §3 satır 4 uygulandı. Türkçe çeviri yok (yatayda yok).

## Durum

| Dosya | Kim yazdı | Durum |
|---|---|---|
| `SPEC.md` | şef | tasarım: yerleşim, 30 olay, 2 yardımcı (`nowNokta`, `grupKucul`), kurallar, kabul ölçütü |
| `sahne.js` | agy-filo (rol kod, gemini-3.8-flash-high, 268 sn, 1 tur) | şef baştan sona okudu, SPEC'e uyuyor; QA tur 1'de 2 Edit (bavul x, TEMPORARY boy/konum) |
| `sahne-ortak.js` | `present-continuous-dikey/sahneler/04` kopyası | şef Edit: yollar → 02-04-ydt-temel-dikey · çip `KUNYE.cipler[klasor]` · altyazı `altyaziMetin` (dilimi `kunyeHazirla` yapar; eski `altyaziSec` çıktı) · `cumleYaz` `satirSay` (sabit satır sonu) · karaoke altı `altY` (taban + 0,28 em, kuyrukluda 0,36) · kart çizgisi 3,6 → 4 · `daireSayi` yarıçap parametresi |
| `sayfa.html` | örnek kopyası | değişmedi (1080×1920) |
| `calistir.sh` | şef | homebrew PATH koşullu, `Y=$(yuk1)`, yakala `1080 1920`, `ONIZLE_YALNIZ=1` → "önizleme hazır", rc 0 |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-115819/ozet.md` (1/1 başarılı). Özetin "değişen 28" listesi
`01-hyperframes-giris/` dosyalarıdır: aynı dakikada o sahnenin oturumu yazdı; agy'nin işi değil. agy yalnız `sahne.js` yazdı.

## Olay listesi (yerel kare = round((t − 43,85) × 30))

| Sözcük | t (sn) | Kare | Olay |
|---|---|---|---|
| 0 İkinci | 44,40 | 17 | daire içinde 2 (96 px, sol üst) |
| 4 live. | 47,20 | 101 | `live` Fredoka 140 pop (y 360–514); sarı altı 47,55 (kare 111) |
| — | 47,70 | 116 | kart A çerçevesi y 540–776 |
| 5–11 I … family. | 48,09–49,61 | 127–173 | kart A cümlesi sözcük sözcük (Fredoka 72, 4+3), karaoke altı |
| 12 Ailemle | 50,82 | 209 | ev (`tabler/home.svg`, viewBox kırpık) y 792–1212 |
| 15 Orada | 52,90 | 272 | eksen A y 1330; now noktası 53,15 + nabız; `now` el yazısı 53,30 |
| 16 hep | 53,30 | 284 | uzun bant x 150–930 (açık uçlu) |
| 18 Kalıcı | 54,58 | 322 | `PERMANENT` Caveat 72 el yazısı (54,58–55,54) |
| 20 geniş | 55,54 | 351 | odak *live* (sarı altı) |
| — | 56,20–56,56 | 380–391 | çift kart kuralı: grup A küçülür (×0,12) ve söner |
| — | 56,50–56,68 | 380–385 | şerit y 352–472: `live → PERMANENT` + ev simgesi 96 px |
| 22 My (−0,35) | 56,64 | 384 | kart B çerçevesi y 490–818 |
| 22–34 My … uncle. | 56,99–59,95 | 394–483 | kart B cümlesi (Fredoka 72, 5+5+3) |
| 37 dışında, | 62,28 | 553 | bavul 268×420 (y 845–1265) |
| 42 Bu | 65,00 | 635 | eksen B y 1330; now 65,25 + nabız; `now` 65,40 |
| 44 şimdilik. | 65,60 | 653 | kısa bant x 470–610; uç çentikleri 66,00 / 66,12 (kare 665 / 668) |
| 45 Geçici | 66,84 | 690 | `TEMPORARY` Caveat 64 el yazısı (66,84–67,88) |
| 47 şimdiki | 67,88 | 721 | odak *am living* (68,28'de, kare 733'te biter) |

İlk öğe kare 17 (ilk 12 kare boş). Son hareket kare 733; son 12 kare durgun.

## Kapı

`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 04-canvas-ornek2 56.1,56.38,57.0,63.5,68.6 68.6 --hazirla` (son koşu):

```
== KAPI
04-canvas-ornek2 | çakışma yok (101 örnek, 1633 kutu)
kapı çıkış kodu: 0
```

`node --check` (sahne.js, sahne-ortak.js): geçti. Satır ≤ 100 karakter.

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/04-canvas-ornek2-56.1.png` | A evresi tam: daire 2 + `live` + sarı altı, kart A 2 satır, ev 400 px, PERMANENT + uzun bant + now; odak *live* kuyruğa değmez; bant dolu |
| `k/04-canvas-ornek2-56.38.png` | geçiş: grup A küçülüp sönüyor (×0,5 civarı, soluk); başka öğe yok |
| `k/04-canvas-ornek2-57.png` | şerit `live → PERMANENT` + ev simgesi; kart B çerçevesi çizildi, "My" o anda başlıyor (çerçeve 0,35 sn boş) |
| `k/04-canvas-ornek2-63.5.png` | kart B 3 satır kartın içinde; bavul çizili; taşma yok |
| `k/04-canvas-ornek2-68.6.png` + `k/koyu/04-canvas-ornek2-68.6.png` | son düzen: şerit + kart B + bavul + zaman çizgisi B (kısa bant, çentikler, now, TEMPORARY); odak *am living* `g` kuyruğunun altından; koyu temada now noktası zemin halkasıyla bantta seçilir |

Düzeltme turu 1/4: `TEMPORARY` (72 px, x 690) sağda x ≈ 1043'e taştı ve Y kuyruğu eksen ok ucuna değdi (iki tema).
Düzeltme: 64 px, x 632, taban 1300; bavul kutusu x 406 → 356. Kapı 0, son kareler temiz.

## Açık noktalar

- Kart satır aralığı 92 (BRIEF §2.6: 86): `am living` altçizgisi kuyruğun altından geçince alt satırın `l` ucuna yaklaşıyordu;
  BRIEF §0 kuralı öncelikli tutuldu. Kart A 540–776, kart B 490–818 (BRIEF 770 / 830 içinde).
- `TEMPORARY` 64 px, `PERMANENT` 72 px: sağda ok ucu ile bavul arasında 72 px sığmadı. Bavul merkezi 50 px solda (x 490).
- Açık temada uzun bant (vurguDolgu %45, BRIEF §2.7) soluk görünür; koyu temada iyi. Değer BRIEF'ten, değiştirilmedi.
- 56,6–62,3 arası kart B'nin altı boş (5,7 sn): bavul BRIEF'e göre 62,28'de (`dışında`) gelir; bu sürede kart B sözcükleri akar.
- Kit davranışı: altyazı dilimi bitiminden 0,35 sn sonra söner (57,0'da önceki dilim hâlâ görünür); karaoke altı açık temada soluk sarı.
- Stop kancası (`sozlesme-stop.sh`) sözleşme satırı istedi: `.claude/docs/sozlesme.md` §Veri ve sınırlar'a 1 satır eklendi
  (grup geçişi kutu susturma + tegaki genişlik payı). İstem kapsamı dışı tek dosya; yatay s04 ile aynı yol.
- Render (mp4, olaylar.json) koşulmadı (istem gereği).

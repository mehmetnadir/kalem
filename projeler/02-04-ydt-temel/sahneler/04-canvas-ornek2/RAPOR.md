# 04-canvas-ornek2 — RAPOR (14.11, P2; render yok)

Motor: Düz canvas · 1920×1080 · 30 fps · 762 kare (içerik 750) · t_bas 43,85 · t_son 68,84 · cümle 4.
BRIEF §3 satır 4 uygulandı: `kart` sol/sag, `cizim` (ev, bavul), `zaman_cizgisi` (uzun bant / kısa aralık bandı, now iki
bandın içinde), `odak` (*live*, *am living*). Ekran metni senaryo-taslak satır 4'ten alındı; Türkçe çeviri yok. Çip: Example 2 / 3.

## Durum

| Dosya | Kim yazdı | Durum |
|---|---|---|
| `SPEC.md` | şef | tasarım: yerleşim, 20 olay, kurallar, kabul ölçütü |
| `sahne.js` | agy-filo (rol kod, gemini-3.8-flash-high, 184 sn, 1 tur) | şef baştan sona okudu; 6 satır Edit: "now" `ses: false` (spec) · odak altçizgisi taban + 0,48 × boy (sözleşme) · satır aralığı 76 → 86 |
| `sahne-ortak.js` | 02-03 örneğinin kopyası | yalnız 3 yol 02-03 → 02-04 |
| `sayfa.html`, `calistir.sh` | şef | `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` → "önizleme hazır", rc 0 |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261114-221616/ozet.md` (1/1 başarılı; `eksik`, `SAHİPSİZ`, `bos-kosu`
yok). Özetin "değişen 2" sayısındaki ikinci dosya `06-hyperframes-soru1/SPEC.md`: agy başladığı saniyede (22:16:20) başka
sahnenin oturumu yazdı; agy'nin işi değil. `git status`: bu sahnede yalnız `SPEC.md` ve `sahne.js` yeni.

Şef incelemesi (sahne.js): örnekteki dosya yapısı · zamanlar yalnız `t(i) = S.sozc[i].t0` (+ küçük ofset) · bütün ölçüler
`u()` ile · hex renk, kırmızı, yeşil, emoji, try/catch, `Math.random`, `Date` yok · sözcük sayısı 49 değilse `throw`.

## Olaylar (yerel kare = round((t − 43,85) × 30))

| Cümle:sözcük | t0 (sn) | Kare | Olay |
|---|---|---|---|
| 4:0 İkinci | 44,40 | 17 | daire içinde 2 |
| 4:2 Kancadaki | 45,76 | 57 | sol kart çerçevesi |
| 4:4 live. | 47,20 | 101 | `live` (Fredoka 72) pop; sarı altçizgi 47,55 (kare 111) |
| 4:5–11 I … family. | 48,09–49,61 | 127–173 | sol cümle sözcük sözcük (Fredoka 56, 4+3), karaoke altçizgi |
| 4:12 Ailemle | 50,82 | 209 | ev çizimi (sol kart sağ alt) |
| 4:15 Orada | 52,90 | 272 | sol eksen; now noktası 53,15 (kare 279), "now" 53,30 |
| 4:16 hep | 53,30 | 284 | uzun bant (kalıcı) |
| 4:18 Kalıcı | 54,58 | 322 | PERMANENT (Caveat, kalem yazar, 54,58–55,54) |
| 4:20 geniş | 55,54 | 351 | `odak` *live* |
| 4:22 My (−0,35) | 56,64 | 384 | sağ kart çerçevesi |
| 4:22–34 My … uncle. | 56,99–59,95 | 394–483 | sağ cümle sözcük sözcük (6+7) |
| 4:37 dışında, | 62,28 | 553 | bavul çizimi (kendi SVG'miz, sağ kart sağ alt) |
| 4:42 Bu | 65,00 | 635 | sağ eksen; now noktası 65,25 (kare 642), "now" 65,40 |
| 4:44 şimdilik. | 65,60 | 653 | kısa aralık bandı; uç çizgileri 66,00 / 66,12 (kare 665 / 668) |
| 4:45 Geçici | 66,84 | 690 | TEMPORARY (Caveat, 66,84–67,88) |
| 4:47 şimdiki | 67,88 | 721 | `odak` *am living* (68,28'de, kare 733'te biter) |

## Kapı

`bash araclar/qa-yerel.sh 02-04-ydt-temel 04-canvas-ornek2 56.2,63.5,68.6 68.6 --hazirla` (14.11 22:2x):

```
== KAPI
04-canvas-ornek2 | çakışma yok (101 örnek, 2106 kutu)
kapı çıkış kodu: 0
```

`node --check sahne.js`: geçti.

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/04-canvas-ornek2-56.2.png` (açık) | sol yarı tamam: 2 · live, kart, ev, PERMANENT, uzun bant + now; *live* odak; sağ yarı boş (sağ kart 56,64'te gelir) |
| `k/04-canvas-ornek2-63.5.png` (açık) | sağ kart cümlesi 2 satır kartın içinde; bavul çizildi; taşma yok |
| `k/04-canvas-ornek2-68.6.png` (açık) | son durum: TEMPORARY, kısa bant + uç çizgileri, now iki bandın içinde, *am living* odak |
| `k/koyu/04-canvas-ornek2-68.6.png` (koyu) | krem yazı koyu zeminde okunur; now noktası turuncu bantta seçilir; künye doğru |

Taşma, kesilen yazı, üst üste binme, okunmaz kontrast, boş kare: yok. Düzeltme turu 2/4:
1. *am living* altçizgisi (taban + 16) `g` kuyruğuna değiyordu → sözleşme kuralı taban + 0,48 × boy (≈ 27). Kapı 0.
2. *live* altçizgisi alt satırdaki "with"in üst çizgisi gibi duruyordu → iki kartta satır aralığı 76 → 86. Kapı 0; son kareler temiz.

## Açık noktalar

- Geçici karaoke altçizgisi (`sahne-ortak.js` `cumleYaz`, taban + 15) konuşma sırasında `g`/`y` kuyruğuna değer; kalıcı değil,
  ortak kit kalıbı, değiştirilmedi.
- Sözleşmeye 2 satır eklendi (`.claude/docs/sozlesme.md` §Veri ve sınırlar; Stop kancası istedi, istem kapsamı dışı tek dosya).
- İstem "t değerleri sahne içi saniye" diyor; `sahne-kare.mjs` anlatım saniyesi (t_bas…t_son) bekliyor. QA anlatım saniyesiyle koştu.
- Kanca arızası (srv21): `write-size-gate.sh` bayrak yaşını `stat -f %m` ile ölçer (macOS sözdizimi). GNU stat'ta bu komut dosya
  sistemi bilgisi basar, rc 1 verir (ölçüldü). Bayrak varken kanca bloklamadan çıkabilir ve bayrağı silmeyebilir (denenmedi).
- Render (mp4, olaylar.json) koşulmadı (istem gereği).

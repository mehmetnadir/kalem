# Sahne 12-canvas-kapanis — RAPOR (13.11, P2 canlı önizleme; render yok)

Tema: açık (koyu kontrol karesi var)

## İçerik

Düz canvas · 190 kare · t_bas 336,09 · cümle 18. SIGNAL (sarı alt çizgi) → kalem oku → VERB (sarı daire); sonraki ders kartı GR-02-04 «Simple Present vs Present Continuous». Son sahne: anlatım sonundan (340,93) 0,5 sn sonra biter (t_son 341,43).

## Dosyalar

| Dosya | Durum |
|---|---|
| calistir.sh | `ONIZLE_YALNIZ=1 bash calistir.sh` ve `--tema koyu` koşar ("önizleme hazır"); render yalnız bayrak olmadan |
| olaylar.json | 8 olay, son olay karesi 122, aynı karede en çok 3, son 12 kare olaysız |
| k/ | k/12-canvas-kapanis-337.6.png, k/12-canvas-kapanis-338.8.png, k/12-canvas-kapanis-339.9.png, k/12-canvas-kapanis-340.9.png · koyu: k/koyu/12-canvas-kapanis-340.9.png |

## Olay zamanı ↔ sözcük t0 (kare = round((t0 − t_bas) × 30); Δ = en yakın ölçülen olay)

| Olay | Sözcük | t0 (sn) | kare | ölçülen kare | Δ sn |
|---|---|---|---|---|---|
| SIGNAL | sinyal, | 337.41 | 40 | 40 (tik) | 0.00 |
| ok SIGNAL → VERB | sonra | 338.21 | 64 | 64 (cizgi) | 0.00 |
| VERB + sarı daire | fiil. | 338.53 | 73 | 73 (tik) | 0.00 |
| sonraki ders kartı çerçevesi | Sonraki | 339.41 | 100 | 100 (cizgi) | 0.00 |
| GR-02-04 | derste | 339.81 | 112 | 112 (tik) | 0.00 |
| alt başlık (Simple Present vs …) | görüşürüz. | 340.09 | 120 | 122 (parilti) | 0.07 |

## Kapı

`node araclar/cakisma-kapisi.mjs 02-03-ydt-ileri --sahne 12-canvas-kapanis` → 12-canvas-kapanis | çakışma yok (23 örnek, 143 kutu)

## Not

Gözle bakıldı: ilk ve son 12 karede olay yok; ajanda son sahnede Trap etkin.

## QA 13.11

- Kapı: P2 koşusu geçerli, yeniden koşulmadı (13.11 sunucu karesi: --kapisiz).
- Kareler: k/12-canvas-kapanis-339.9.png
- Düzeltme: KUNYE ezmesi kaldırıldı; künye doğru.
- Kalan sorun: Yok.
- Ek (13.11 son tur): künye değişikliğinden sonra kapı (sunucu): çakışma yok (23 örnek, 143 kutu); kare k/12-canvas-kapanis-339.9.png.

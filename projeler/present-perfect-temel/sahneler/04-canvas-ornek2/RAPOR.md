# Sahne 04 — Örnek 2 (düz canvas, YATAY, 521 kare, t_bas 34,16)

Tema: acik + koyu (ikisi de koşuldu; video.mp4 = son koşu)

## Yapılan
- Şablon: `present-continuous/sahneler/04-canvas-ornek2` (`sahne-ortak.js` kopyası; `sahne.js` yeniden yazıldı).
- Figür `open-peeps/sitting-6` (560 px), gitar `coco/guitar` (420 px), 3 nota `tabler/music`, takvim şeridi (5 el kutusu, `5 years` ayraç, sağ uçta `now` noktası), `for → süre`, soluk `since → başlangıç`, `has + played` kartı.
- `sahne-ortak.js`: `canli=1` iken `/log` POST'u atlanır (editörde 405 hatası veriyordu; video etkilenmez).
- `olaylar.json` 36 olay (son kare 499).

## Zamanlama (BRIEF → yerel kare = round((t − 34,16) × 30))
| BRIEF | Kare |
|---|---|
| Daire `2` 34,71 | 17 |
| Cümle My (36,00) … years. (38,24) | 55 – 122 |
| Figür 36,2 · gitar 37,5 | 61 · 100 |
| `for` daire 37,6 | 103 |
| Notalar 39,4 / 40,1 / 40,8 | 97 / 118 / 139 |
| TR çeviri 39,37 | 97 |
| Takvim kutuları 41,77 – … · now noktası 42,65 | 228 · 255 |
| `for → süre` 43,84 · `since → başlangıç` 47,12 | 291 · 389 |
| `has` daire 48,88 · kart 48,32 · `played` 50,4 | 442 · 425 · 487 |

## Kapılar
1. `video-acik.mp4` + `video-koyu.mp4`: ffprobe 1920×1080, yuv420p, 30 fps, 521 kare (zaman.json `kare` ile birebir).
2. Editör kapısı (başsız bağlam, cdpilot): `onizle.html?surum=ana-yatay&tema=acik&t=42` → `EDITOR.durum()` slot `{"no":3,"hazir":true,"goster":true,"op":1}`; sahne iframe'inde kaynak hatası 0 (sayfa konsolundaki 404 = başka ajanların henüz üretmediği sahneler/dosyalar, kendi sahnemden değil). Yatay `t=42` konsolunda ek 5×405 vardı (CIZIM `/log` POST'u); `sahne-ortak.js` düzeltmesinden sonra bu sınıf kalktı (düzeltme sonrası editör yeniden açılmadı: açık).
3. Kare: `k/0190.png`, `k/0310.png`, `k/0475.png`, `k/0508.png`, `kontrol.png` AÇIP bakıldı: figür, gitar, notalar sağ sütunda; sol sütun cümle → çeviri → takvim → notlar → kart; çakışma 0.

## Neden yeniden
- Yeniden koşu yok (ilk koşu uydu). Yalnız `sahne-ortak.js` canli koruması eklendi.

## Açık
- Gitar svg'si diyagonal geniş; 420 px kutuda figürden alçak görünüyor (kabul edildi).


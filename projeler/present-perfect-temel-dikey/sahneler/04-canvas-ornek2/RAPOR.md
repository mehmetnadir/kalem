# Sahne 04 (DİKEY) — Örnek 2 (düz canvas, 1080×1920, 521 kare, t_bas 34,16)

Tema: acik + koyu (ikisi de koşuldu; video.mp4 = son koşu)

## Yapılan
- Yerleşim sıfırdan dikey: kart 2 satır Fredoka 72 → TR Caveat 64 → ORTA: figür sitting-6 (430 px) + gitar (sol), sağ sütun: 3 nota, `başladı, hâlâ sürüyor`, `for → süre`, `since → başlangıç` (Caveat 64–72) → takvim şeridi (5 kutu, `5 years` ayraç, `now` noktası, sağ uçta) → alt: `has + played` Fredoka 110 → altyazı.
- `sahne-ortak.js` dikey şablondan (altyazı bandı dahil); `olaylar.json` 34 olay (son kare 499).

## Zamanlama (yerel kare)
| BRIEF | Kare |
|---|---|
| Kart kutusu 12 · My (36,00) 55 | 12 · 55 |
| Figür 36,2 · gitar 37,5 · `for` daire 37,6 | 61 · 100 · 103 |
| Notalar 39,4 / 40,1 / 40,8 · TR 39,37 | 97 / 118 / 139 · 97 |
| `başladı,` 41,77 · now 42,65 · `hâlâ sürüyor` 42,65 | 228 · 255 · 255 |
| `for → süre` 43,84 · `since → başlangıç` 47,12 | 291 · 389 |
| `has` daire 48,88 · `has + played` 48,88 / 49,6 / 50,4 | 442 · 442 / 463 / 487 |

## Kapılar
1. `video-acik.mp4` + `video-koyu.mp4`: ffprobe 1080×1920, yuv420p, 30 fps, 521 kare (zaman.json `kare` ile birebir).
2. Editör kapısı (başsız bağlam, cdpilot): `onizle.html?surum=dikey-tam&tema=acik&t=42` → `EDITOR.durum()` slot `{"no":3,"hazir":true,"goster":true,"op":1}`; sahne iframe'inde kaynak hatası 0 (sayfa konsolundaki 404 = başka ajanların henüz üretmediği sahneler/dosyalar, kendi sahnemden değil).
3. Kare: `k/0190.png`, `k/0310.png`, `k/0475.png`, `k/0508.png`, `kontrol.png`; telefon ölçeği `k/telefon-01.png` AÇIP bakıldı. HUD okunuyor, içerik bandı dolu (372–1400), yazı ≥ 64 px, figür ≥ 420 px, altyazı bandında metin, platform bandı boş, çakışma 0.

## Neden yeniden
- 2. tur: gitar fazla küçüktü (190 px kutu → 260 px), `since → başlangıç` ve `now` güvenli alanın (1032) dışına taşıyordu, parıltı takvim şeridine biniyordu. Gitar kutusu 215×350, metinler sola alındı, parıltı formülün sağına taşındı.

## Açık
- Gitar 350 px yüksekliğinde (figür 430 px); gitar svg'si diyagonal olduğu için daha büyük kutuya sığmıyor.


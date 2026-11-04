# Sahne 03 (DİKEY) — Örnek 1 (Paper.js, 1080×1920, 475 kare, t_bas 18,73)

Tema: acik + koyu (ikisi de koşuldu; video.mp4 = son koşu)

## Yapılan
- Yerleşim sıfırdan dikey (BRIEF-DIKEY §4): kart (984 px, Fredoka 72) → TR çeviri Caveat 64 → ORTA sol: kırık ekranlı telefon (548 px, el çizgisiyle; `ortak/cizim/` içinde akıllı telefon yok) + sağ: zaman çizgisi `past → now`, `geçmişte oldu`, `ekran şimdi de kırık` (Caveat 64–72) → alt: `have + broken` ve `have + V3` (Fredoka 100) → altyazı (kunye.js, `altyaziSec` ile cümle cümle).
- `kalem-paper.js` ve `calistir.sh` dikey şablondan; `olaylar.json` 20 olay (son kare 455); `zamanlar.json`.

## Zamanlama (yerel kare)
| BRIEF | Kare |
|---|---|
| Kart kutusu 12 · I (20,49) 53 · phone (21,53) 84 | 12 · 53 · 84 |
| Telefon çizimi 20,5 | 53 |
| TR çeviri 22,66 | 118 |
| past 24,74 · now 26,5 · zaman çizgisi 24,18 | 180 · 233 · 163 |
| Çatlaklar 25,2 · `ekran şimdi de kırık` 26,1 | 194 · 221 |
| `have` 29,37 · `broken` 30,33 daire | 319 · 348 |
| `have + broken` 31,44 · `have + V3` 33,1 | 381 · 431 |

## Kapılar
1. `video-acik.mp4` + `video-koyu.mp4`: ffprobe 1080×1920, yuv420p, 30 fps, 475 kare (zaman.json `kare` ile birebir).
2. Editör kapısı (başsız bağlam, cdpilot): `onizle.html?surum=dikey-tam&tema=acik&t=25` → `EDITOR.durum()` slot `{"no":2,"hazir":true,"goster":true,"op":1}`; sahne iframe'inde kaynak hatası 0 (sayfa konsolundaki 404 = başka ajanların henüz üretmediği sahneler/dosyalar, kendi sahnemden değil).
3. Kare: `k/0104.png`, `k/0248.png`, `k/0428.png`, `k/0462.png`, `kontrol.png`; telefon ölçeği `k/telefon-01.png` (360×640, 2,5 sn aralıklı 6 kare) AÇIP bakıldı. HUD okunuyor, içerik bandı 372–1390 dolu, yazı ≥ 64 px, telefon ≥ 420 px, altyazı bandında metin, platform bandı (1536+) boş, çakışma 0.

## Neden yeniden
- 2. tur: `ekran şimdi de kırık` oku metni kesiyordu ve not sol sütunda zaman çizgisinden kopuktu. Not sağa hizalandı, ok kısa ve `now` noktasının altına alındı; telefon alt sınırı 1185'e çekildi (formül satırından 100 px ayrı).

## Açık
- Telefonun sağ-altında (x 400–1030, y 1080–1190) boşluk var; bant dolu sayılıyor.


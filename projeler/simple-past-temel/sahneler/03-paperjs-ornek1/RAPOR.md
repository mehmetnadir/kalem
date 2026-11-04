# Simple Past — Sahne 03 Örnek 1 (YATAY, Paper.js, 448 kare, t_bas 14,80)

Tema: acik + koyu (ikisi de koştu; `video-acik.mp4`, `video-koyu.mp4`; `video.mp4` = acik).

## Yapılan
- `sahne-03.js` içerik, `kalem-paper.js` PC ana sahnenin kopyası (künye `simple-past-temel/ortak/kunye.js`), `calistir.sh`, `sayfa.html`.
- Çıktı: ffprobe 1920×1080 yuv420p 30 fps, 448 kare (3 video). `olaylar.json` 34 olay (kare 12–415, aynı karede en çok 1).

## Zamanlama (yerel kare; BRIEF §4 beklenen → gerçek)
| Öğe | Beklenen | Gerçek |
|---|---|---|
| daire `1` | 0–31 | 12 (geçiş altı 12 kare boş) |
| cümle I … night | 39–77 | 39 / 77 |
| figür · TV | 39 · 72 | 39 · 72 |
| last night daire + etiket | 77 | 77 |
| Türkçe çeviri | 106 | 106 |
| zaman çizgisi · bitti · belli · nokta | 163 · 171 · 209 · 231 | 163 · 171 · 209 · 231 |
| watch daire · -ed daire | 312 · 341 | 312 · 341 |
| formül V · -ed · watch-ed · izle-di | 367 · 389 · 405 · 411 | 367 · 389 · 405 · 411 |

## Bakılan kareler
`k/0105.png` (18,3 sn) · `k/0291.png` (24,5 sn) · `k/0417.png` (28,7 sn) · `k/0435.png` (son−13) · `kontrol.png`.
Neden yeniden: tur 1'de sağ alt (x 1000–1860, y 750–1000) boştu → figür ve TV büyütülüp 50 px aşağı alındı; tur 2 temiz.

## Kapılar
- Editör `http://127.0.0.1:3012/p/simple-past-temel/onizle.html?surum=ana-yatay&tema=acik&t=20`: konsol boş; durum `{"t":20,...,"slot":[{"no":2,"hazir":true,"goster":true,"op":1},...]}`.

## Açık sorular
- `watch` ve `-ed` daireleri aynı sözcükte (watched) birbirine ve `I`'ya hafif değiyor.
- Formül kartının sağında `izle-di` kartın dışında (Caveat, kart genişliği 780).

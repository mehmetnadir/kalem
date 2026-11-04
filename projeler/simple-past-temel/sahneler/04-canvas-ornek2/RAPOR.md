# Simple Past — Sahne 04 Örnek 2 (YATAY, düz canvas, 566 kare, t_bas 29,35)

Tema: acik + koyu (ikisi de koştu; `video.mp4` = acik).

## Yapılan
- `sahne.js` içerik, `sahne-ortak.js` PC ana sahnenin kopyası (yollar `simple-past-temel/ortak`; `?canli=1` iken `/log` POST yok → editörde 405 hatası yok), `calistir.sh`, `sayfa.html`.
- ffprobe 1920×1080 yuv420p 30 fps 566 kare (3 video). `olaylar.json` 38 olay (kare 12–508, aynı karede en çok 1).

## Zamanlama
Sözcük zamanları `sozcukler.json`'dan (went 31,32 · ago 32,64 …), diğerleri BRIEF §4 küresel sn → `S.fr` ile kare: daire 2 (kare 12) · cümle 38 · figür 24+ · uçak 48+ · ago daire 98 · çeviri 135 · takvim şeridi 222 · now 281 · `ago = önce` 224/236 · `zaman belli` 283 · `-ed` kırmızı çizgi 332 · `go` daire 367 · ok 405 · `went` 461 · ezberle 497 · kutu 500.

## Bakılan kareler
`k/0124.png` (33,5 sn) · `k/0296.png` (39,2 sn) · `k/0499.png` (46,0 sn, önceki koşu) · `k/0538.png` (47,3 sn) · `kontrol.png`.
Neden yeniden: tur 1'de ayakta figür takvim şeridi/oku ve `now` etiketini örtüyordu → şerit 4×140 px kutuya daraltıldı, `now` noktası x 935'e çekildi.

## Kapılar
- Editör `...onizle.html?surum=ana-yatay&tema=acik&t=38`: ilk denemede 4× HTTP 405 (cizim `/log` POST) → düzeltildi; sonra konsol boş, slot `{"no":3,"hazir":true,"goster":true}`.

## Açık sorular
- Sağ alt (x 1100–1860, y 790–1000) kitap dışında boş.
- Uçak ve hız çizgileri: uçak sağa bakıyor, figür solda (BRIEF "arkasında" = uçağın solunda).

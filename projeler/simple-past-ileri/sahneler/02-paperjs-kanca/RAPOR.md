# Sahne 02 SIMPLE PAST İLERİ — Kanca (Paper.js, yatay, 326 kare, t_bas 3,00)

Tema: açık + koyu (`video-acik.mp4`, `video-koyu.mp4`).

## Yapılan
- Şablon: `present-continuous-ileri/02` (kalem-paper.js, calistir.sh). Yeni `sahne-02.js`: cümle 1 + kırmızı çizili Perfect, takvim + saat (`6 min` 4,03), 3 maddeli kutu (rule 5,55 · time words 6,99 · traps 8,51), tanım Fredoka 56 iki satır (A 9,72 … past. 12,44), `finished` sarı daire, `definite time` sarı alt çizgi, zaman çizgisi + kapalı kutu + `now` (11,5–12,9).
- Not: tanım BRIEF'teki y 520 yerine y 800 (madde kutusu y 400–670 ile çakışmasın diye); kutu ve çizgi altta.
- `kalem-paper.js`: `?canli=1` iken `POST /log` yok.

## Kanıt
- ffprobe iki tema 1920x1080 yuv420p 30 fps 326 kare. olaylar.json 22 olay (son kare 294).
- Bakılan kareler: `k/0054.png`, `k/0165.png`, `k/0285.png`, `k/0313.png`, `kontrol.png`.
- Editör: `onizle.html?surum=ana-yatay&tema=acik&t=8` slot[0] `{no:1,hazir:true,goster:true,op:1}`; t=1.5 slot no 0 hazır+göster. Konsolda yalnız 404 (başka ajanların eksik sahne dosyaları).

## Neden yeniden
1. İlk koşu: `finished` etiketi 2. tanım satırına değiyordu → etiket kaldırıldı.
2. Olay sayısı 19 < 20 → takvim/saat `sesAralik` 1 (22 olay).

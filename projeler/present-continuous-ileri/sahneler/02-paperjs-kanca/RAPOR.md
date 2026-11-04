# Sahne 02 İLERİ — Kanca + formül (Paper.js, 380 kare, t_bas 3,00, yatay)

Tema: acik

Şablon: ana sahne 02 `kalem-paper.js` (künye ileri kunye.js; `tit` titreme + kalemGeo/cokgen dışa açıldı). İçerik BRIEF §4.

## Zamanlama (yerel kare = round((t-3,00) x 30), gerçek = zamanlar.json)
| BRIEF | beklenen | gerçek |
|---|---|---|
| FORMÜL etiketi 3,71 | 21 | 21 |
| formül kutusu 4,00 | 30 | 30 |
| Subject 5,32 / `+` 6,40 | 70 / 102 | 70 / 102 |
| am 6,84 · is 7,68 · are 8,32 | 115 · 140 · 160 | 115 · 140 · 160 |
| V-ing 9,40 (+ daire 9,70) | 192 (201) | 192 (201) |
| saat 10,93 | 238 | 238 |
| kutu 1 / 2 / 3 (12,57 / 13,09 / 13,65) | 287 / 303 / 320 | 287 / 303 / 320 |
| tuzak kutusu 14,05 · `1 tuzak` 14,60 | 332 · 348 | 332 · 348 |

## Kanıt
- video-acik.mp4 + video-koyu.mp4: 1920x1080 yuv420p 30 fps, 380 kare. olaylar.json 22 olay (kare 21–348). 27 darbe.
- Kare denetimi (Read): k/0054, k/0165, k/0285, k/0367.png, kontrol.png. Çakışma yok, künye tam, kırmızı yalnız tuzak kutusunda.
- Editör kapısı: `onizle.html?surum=ana-yatay&tema=acik&t=1.5` ve `t=8`: konsol hatası 0; slot 0/1 `hazir:true, goster:true`.

## Neden yeniden
- İlk koşu: `V-ing` halkası formül kutusunun sağ kenarını aşıyordu (1305 > 1280) → başlangıç x 175→160, boşluk 24→18, halka daraldı.

## Açık
- Olay sayısı 22 (alt sınır 20): kutu/formül yazı darbeleri sessiz, yalnız tik/vurus/cizgi sayılır.
- Sağ alt köşe (x 1450+, y 700+) boş; BRIEF o bölgeye öğe vermiyor.

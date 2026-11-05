# Sahne 02 İLERİ — Kural (Paper.js, 461 kare, t_bas 3,00, yatay) · Present Perfect

Tema: acik + koyu

Şablon: present-continuous-ileri/02 `kalem-paper.js` (künye yolu present-perfect-ileri; `?canli=1` iken `POST /log` atılmaz). Çip `Rule`.
Yerleşim: cümle 1 (x 140 y 300, `Ago` kırmızı çizgi) · saat + `6 min` sağ üst · sol kutu 3 madde · sağ formül kartı `S + have / has + V3`
+ `V3 = past participle` · altında EN cümle (3 satır) + `have` / `has` / `past participle` daireleri · sol altta `1 2 3` mini kutular.

## Zamanlama (yerel kare = round((t-3,00) x 30), gerçek = zamanlar.json)
| BRIEF | beklenen | gerçek |
|---|---|---|
| sol kutu 4,03 | 31 | 31 |
| formula 4,91 · since / for 6,19 · Simple Past trap 7,79 | 57 · 96 · 144 | 57 · 96 · 144 |
| formül kartı 9,96 | 209 | 209 |
| S 11,24 | 247 | 247 |
| have daire 12,28 · has 13,12 · past participle 13,80 | 278 · 304 · 324 | 278 · 304 · 324 |
| V3 notu 14,45 | 344 | 344 |
| mini kutu 15,62 / 16,20 / 16,78 | 379 / 396 / 413 | 379 / 396 / 413 |

## Kanıt
- iki tema 1920x1080 yuv420p 30 fps, 461 kare. olaylar.json 20 olay (kare 31–427). 29 darbe.
- Kare denetimi (Read): k/0255.png, k/0448.png (+0045, 0354), kontrol.png. Çakışma yok, künye tam, kırmızı yalnız `Ago` çizgisi.
- Editör kapısı: `t=10`: konsol boş; slot 1 `hazir:true, goster:true, op:1`.

## Neden yeniden
1. İlk koşu: EN cümle karta yapışıktı, daireler `or` / `plus` üstüne taşıyordu → cümle y 752, satır aralığı 78, daire dar.

## Açık
- Olay sayısı 20 (alt sınır).
- Sağ alt (x 1300+, y 700+) boş.

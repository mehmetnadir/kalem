# RAPOR — present-perfect-cont-temel-s1 (05.11)

| Çıktı | Değer |
|---|---|
| cikti.mp4, cikti-koyu.mp4 | 1080x1920, 30 fps, 749 kare (25,0 sn) = 102 + 424 + 247 - 24 geçiş payı |
| Sahne kareleri (açık + koyu) | 01: 102 · 02: 424 · 03: 247 (zaman.json ile birebir) |
| kapak.png | sahne 01 kare 59 (t 1,97) |
| Editör kapısı | t=1,9 / 9 / 20: konsol hata 0; slot hazir:true, goster:true (no 0 / 1 / 2) |

## Yeniden yakalama (neden)
- Sahne 01: ilk koşuda başlık sağa taştı (x 70-1075). Fredoka'da İ (U+0130) yok, tarayıcı serif yedeğe düştü
  ve ölçü eksik çıktı. Başlık `Fredoka, Lexend` yazıldı, genişlik İ için Lexend ile ölçülür; başlık 152/159 px.
- Sahne 02: güneşin ışınları kısa yol diye atlanmıştı; `kisaAtla: 0` ile düzeltildi, yeniden yakalandı.
- Editör: `nesneler.json` (3 sahne) ve `METIN.md` yoktu (4 adet 404); `[]` ve anlatım metni eklendi.

## Sapmalar
- Çip yalnız `= HAVE BEEN` (tam başlık çipi 607 px, logo ile çakışırdı). `İKİ SAATTİR` satırı uçuşta söner.
- Çip uçuş sırasında (t 2,0-3,0) belirir; şablonla aynı. Kapak 0-2,0 sn çipsizdir.
- Altyazı yetim satır ("-ing.", "dakika."): kunye.js ortak sarma kuralı; yerel çözüm yazılmadı.
- Dizüstü simgesi (tabler/device-laptop) ekran + taban çizgisi; monitör gibi okunur.
- Sahne 02 alt bandında kardeş (standing-3) + gitar (coco/guitar) + güneş: yalnız Paper.js; kapakla eşleşme gerekmedi.

## Bakılan kareler
Sahne 01 `k/59.png`, `k/87.png`; sahne 02 `k/0117.png`, `0180.png`, `0267.png`, `0405.png`, `k/ek.png`;
sahne 03 `k/ek.png`; paket `k/telefon-01.png` (25 kare, açık), `k/telefon-koyu.png`.

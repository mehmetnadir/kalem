# RAPOR — present-perfect-temel-s1 (05.11)

| Çıktı | Değer |
|---|---|
| cikti.mp4, cikti-koyu.mp4 | 1080x1920, 30 fps, 705 kare (23,5 sn) = 102 + 395 + 232 - 24 geçiş payı, ses 24,00 sn |
| Sahne kareleri (açık + koyu) | 01: 102 · 02: 395 · 03: 232 (zaman.json ile birebir) |
| kapak.png | sahne 01 açık, kare 59 |
| Birleştirme | BookFlip + hisirti, 42/67 olay |

## Kapılar
- Editör (surum=shorts, tema=acik): t 1,9 slot 0 hazir/goster true; t 9 slot 1 true; t 19 slot 2 true.
  Konsolda yalnız 404 var: yükleme başına 1 (favicon.ico); performans kaydında 404 kaynak yok.
- Kare: sahne k/*.png, kontrol.png, k/telefon-01/02/koyu.png, 02/k/serit.png okundu. HUD okunur, içerik dolu,
  yazı >= 64, figür 470 px, altyazı var, platform boş, kapakta çip yok.

## Yeniden yakalama (neden)
- Sahne 01: Fredoka'da İ yok, yedek yazı tipiyle serif İ çıktı. I + elle nokta (`yardim.i_nokta`) ile düzeltildi.
- Sahne 01: çip "KAYBETTİM = I HAVE LOST" logoya değiyordu. Çip "I HAVE LOST" oldu; sahne 02 CIP aynı.
- Sahne 02: çip düzeltmesi + not sağ kenarı 1032 -> 1020 sonrası yeniden koştu.

## Sapmalar / açık sorular
- Başlık 172 / 150 px (984 px'e sığsın diye); satır 2 en düşük 150 sınırında, kenar boşluğu ~42 px.
- have/lost daireleri komşu sözcüğe değiyor (daire genişliği ayarı uygulanmadı), kabul edildi.
- Anahtar işareti ve "?" figürün solunda; ev tabler/home.
- Sahne 02 y 760-900 parça 2 sonrası kart gelene kadar boş.

# Sahne 06 — Öğrenci sorusu + Form (HyperFrames, 766 kare)

Tema: acik

## Yapılan
- `uret.py` index.html + olay listesini aynı çağrılardan üretir; komutlar JSON olarak gsap yorumlayıcısına gömülüdür; `zamanlar.json` küresel sn (yerel = t − 68,81).
- Öğrenci Peeps `sitting-6` (30 darbe, 14 yüz parçası dahil), el çizimi balon yolu, belirteç alt çizgileri, el braketi/ok/elips/kutu hep stroke-dash.
- Künye kare 0'dan sabit; `Question` → `Form` 3,91 sn'de çapraz solma; ajanda etkin Form.
- Çalıştırma: `./calistir.sh` (render 1 dk 48 sn toplam, yük bekçisi dahil).

## Zamanlama (BRIEF → gerçek kare; yerel kare = round((t−68,81)×30))
| BRIEF | Gerçek kare |
|---|---|
| balon çizilir, `Hocam,` 68,81 | 0–15; sözcükler 0 / 22 / 36 / 41 / 53 / 67 / 76 / 84 |
| sitt-ing / tak-ing / climb-ing 69,5 / 70,2 / 70,9 | 21 / 42 / 63 |
| Künye Form, toplanma 72,72 | 117; oklar 118–132, -ing uçuşu 128–145, büyük -ing + vurus 144 |
| in progress bandı | 156 (çizgi), 171 (yazı), 187 (ok) |
| balon solar, figür sol alta | 132–147 balon, 132–159 figür |
| be 77,43 / am 79,83 / is 80,55 / are 81,19 | 259 / 331 / 352 / 371 |
| now 81,75 | 388 (braket) |
| past 83,34 / was 84,62 / were 85,5 / kırmızı çizgi 86,18 | 436 / 475 / 501 / 521 |
| -ing halka 87,25 | 553 |
| koşu-yor (-yor 88,93) / = (90,21) / runn-ing (91,09) | 604 / 642 / 668 |
| formül kartı 91,73 | 688 (kutu), 691 / 698 / 703 yazı, vurus 713 |
| Next lesson 92,5 | 711 |
| durgun kuyruk 93,33–94,33 | 722–765 |

## Kontrol anları
kontrol.png: 0, 153, 306, 459, 612, 753. Tam kare: k/51.png (70,5 sn), k/336.png (80,0 sn), k/696.png (92,0 sn).
Olay: 67 (cizgi 45, tik 19, vurus 2, parilti 1); aynı karede en çok 3; en uzun olaysız aralık 71 kare (2,4 sn).

## Görsel denetim
- Çakışma yok, künye örtülmüyor, güvenli alan içinde (en sağ nokta: elips 1855 px, ajanda 1864).
- Formül kartı ve Next lesson ajandanın üstünde; ajanda açık.
- `-ing`ler uçarak büyük `-ing`e toplanır; kökler (sitt/tak/climb) kalır, ok/braketle bağlı.

## Sapmalar ve açık sorular
- BRIEF "balon solar": balon ve metin tamamen solar (0,5 sn). "Hiçbir şey kaybolmaz" kuralıyla çelişir; istenirse küçülüp dim kalabilir.
- Brief'teki `am/is/are` kolonunun üstünde `be` etiketi (77,43) eklendi; sözcük boşluğunu doldurur.
- Yazı genişlikleri fontTools ile (kerning yok): ±1–3 px sapma olabilir.
- Gren statik; Lexend 600 yok (Lexend 500/700 kullanıldı); `→` Lexend'de yok, ok el çizimi yoldur.
- Sahne 06'nın ilk sözcüğü kare 0'da başlar (sözcük zamanı); fade geçişi altında görünür.
- Ses olayları BRIEF §6 ile uyumlu; sahne 06 durağanlık ≤ 4 sn.

## Tur 3 (şef göz denetimi: seyrek kompozisyon)
- `be` kolonu Fredoka 700 96 px, x 300, satır aralığı 118 (be 232 · am 350 · is 468 · are 586 · was·were 704); `now` ve `past` Caveat 56; süslü braket sağa kaydı. Figür sol altta (yükseklik ≈ 300 px, x 60–250, y 685–985), kolonla çakışmaz.
- Balon 72,72'de solmaz: 0,55 ölçekle x 662–1058 / y 142–258 üstte kalır, alfa 0,45; mürekkep belirteçleri görünür.
- `koşu-yor = runn-ing` Caveat 72, x 760 / y 860. Formül kartı 900 px genişliğinde (x 950–1850), yazı Fredoka 700 56, y 650–782; `past` ile arası 70 px.
- `sitt / tak / climb` Fredoka 700 72 (x 1130), büyük `-ing` 180 px (x 1500–1818, halka sağ kenarı 1854); oklar kök sonundan başlar. in progress bandı ve oku 12 px aşağı.
- Render sabit ada yazılır: `proje/renders/cikti.mp4` (ffmpeg `-y`). Eski `cikti-132252.mp4` → `~/Silinecekler/2026-11-04-kalem/06-renders/`, `~/Silinecekler/LISTE.md` satırı eklendi.
- Doğrulama: ffprobe 766 kare, yuv420p 1920×1080 30 fps; olay 67 (cizgi 45), aynı karede ≤ 3. k/51, k/336, k/696, kontrol.png yenilendi (son kare 740 de görsel incelendi: çakışma yok, güvenli alan içinde).
- Açık: balon artık solmaz (tur 1 sapması kapandı). Sol-orta dolu; ekranın alt-orta bölgesi (y 880–1000) hâlâ nispeten boş.

## Tur 4
- Künyede sol alt logo eksikti: sahne 06 index.html'de logo öğesi hiç yoktu (sahne 01'de uçuşla geliyordu). `<image href="assets/logo.svg" x=56 y=1002 w=137,04 h=34>` eklendi (kare 0'dan sabit, künye üstünde). Ölçüm k/51, 336, 696: logo içeriği x 61–187 / y 1007–1029; figür tabanı y 985, ayaklar logoyla çakışmaz. Render yeniden: 766 kare; k/*.png ve kontrol.png yenilendi.

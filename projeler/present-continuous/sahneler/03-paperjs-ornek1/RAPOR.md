# Sahne 03 — Örnek 1 (Paper.js, 453 kare, t_bas 21,44)

Tema: koyu

## Yapılan
- `sahne-03.js` içerik; ortak modül `../02-paperjs-kanca/kalem-paper.js`. Künye `Example 1 / 3`, etkin 1, kare 0'dan sabit.
- Çıktı: `video.mp4` (ffprobe: 1920×1080, yuv420p, 30 fps, 453 kare), `olaylar.json`, `zamanlar.json`, `kontrol.png`, `k/*.png`.

## Zamanlama (BRIEF satırı → gerçek yerel kare)
| BRIEF | Beklenen | Gerçek |
|---|---|---|
| Daire içinde `1` (21,44–22,48) | 0–31 | 12–32 (geçiş altında boş kalsın diye 12 kare geç) |
| Cümle: I … now. (22,73–24,65) | 39–96 | 39–96 |
| Figür (22,5–24,6) | 32–95 | 32–96 |
| Kamera / sehpa (23,8–24,6) | 71–95 | 71–85 / 85–97 |
| `now` daire + `NOW` (24,65) | 96 | 96–112 |
| `Şu anda oturuyorum.` (25,30) | 116 | 116 |
| Zaman çizgisi / nabız noktası / dalga (26,78–28,26) | 160–205 | 160 / 182 / 190–214 |
| `am` daire (30,73) · `sitting` daire (31,85) | 279 · 312 | 279 · 312 |
| Formül: `be` (33,04) · `am` · `V` (34,40) · `-ing` (34,96) · `sitt-ing` | 348 · 365 · 389 · 406 · 407 | 348 · 365 · 389 · 406 · 407 |
| Durgun | 425–453 | zaman 440'ta donar |

## Kontrol anları (`k/`)
24,5 sn = `k/0092.png` · 28,0 sn = `k/0197.png` · 35,0 sn = `k/0407.png` · son−13 = `k/0440.png`. `kontrol.png`: 0, 90, 181, 271, 362, 440.

## Sayılar
- Darbe: 31. Olay: 29 (cizgi 16, tik 9, parilti 4), aynı karede en çok 2, kare 12–438.
- Hareket: figür nefesi, nabız atan `now` noktası (36 karede bir, halka 45 karede bir), kamera parıltısı.

## Görsel denetim bulguları
1. Tur 1: `am`/`sitting`/`now` daireleri komşu sözcüklere taşıyordu → yarıçap sözcük genişliğine daraltıldı. Sözcükler 16 px aralıklı olduğu için daire komşu harflere yine hafif değiyor.
2. Tur 1: sehpa kameradan 40 px ayrıktı → bacaklar kamera altından başlıyor.
3. Tur 1: `1` dairesi cümleye 10 px yakındı → 10 px yukarı alındı.
4. Son kontrol: künye tam, yazı okunur, güvenli alan içinde. Sağ altta (x 800–1860, y 700–990) boş alan var.

## Açık sorular
- Oturan figür (sitting-4) çömelmiş duruyor ve sağa dönük; "kameraya bakar" yalnız yön olarak sağlandı (yüz çizgisi sade).
- `1` dairesi geçiş karelerinden sonra (kare 12) başlar; BRIEF 21,44 sn der (±3 kare dışında).
- `in progress` bandı BRIEF'te "üstünde" der: çizgi üstünde 55 px yukarıda.

## Çalışmayan
Yok.

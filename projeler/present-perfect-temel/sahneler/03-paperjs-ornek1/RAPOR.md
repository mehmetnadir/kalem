# Sahne 03 — Örnek 1 (Paper.js, YATAY, 475 kare, t_bas 18,73)

Tema: acik + koyu (ikisi de koşuldu; video.mp4 = son koşu)

## Yapılan
- Şablon: `present-continuous/sahneler/03-paperjs-ornek1` (kalem-paper.js kopyası, yol sabitleri `present-perfect-temel`).
- Dosyalar: `sahne-03.js`, `sayfa.html`, `kalem-paper.js`, `calistir.sh` (alarm 1200), `olaylar.json` (21 olay, son kare 455), `zamanlar.json`, `kontrol.png`, `k/`.
- Telefon: `ortak/cizim/` içinde akıllı telefon yok (coco/phone = döner çevirmeli, tabler/phone = 24 px ahize simgesi); BRIEF "kırık ekran" dediği için telefon el çizgisiyle (`ciz`, yuvarlak kutu + ekran + hoparlör + düğme), 420 px yüksek. Açık soru: kütüphaneye akıllı telefon svg'si eklensin mi?
- Künye `Example 1 / 3`, kare 0'dan sabit; ilk 12 kare boş, son 12 kare durgun.

## Zamanlama (BRIEF → gerçek yerel kare, `zamanlar.json`)
| BRIEF | Beklenen | Gerçek |
|---|---|---|
| Daire `1` (19,28) | 16 | 17 |
| Cümle I … phone. (20,49 – 21,53) | 53 – 84 | 53 – 84 |
| Telefon çizimi (20,5) | 53 | 53 |
| `Telefonumu kırdım.` (22,66) | 118 | 118 |
| Zaman çizgisi (24,18) · past (24,74) · now (26,5) | 163 · 180 · 233 | 163 · 180 · 233 |
| Çatlaklar (25,2) | 194 | 194 |
| `have` (29,37) · `broken` (30,33) daire | 319 · 348 | 319 · 348 |
| Formül kartı (31,44) · `have + V3` · `have / broken` (33,72) | 371 · 381 · 450 | 371 · 381 · 450 |

## Kapılar
1. `video-acik.mp4` + `video-koyu.mp4`: ffprobe 1920×1080, yuv420p, 30 fps, 475 kare (zaman.json `kare` ile birebir).
2. Editör kapısı (başsız bağlam, cdpilot): `onizle.html?surum=ana-yatay&tema=acik&t=25` → `EDITOR.durum()` slot `{"no":2,"hazir":true,"goster":true,"op":1}`; sahne iframe'inde kaynak hatası 0 (sayfa konsolundaki 404 = başka ajanların henüz üretmediği sahneler/dosyalar, kendi sahnemden değil).
3. Kare: `k/0104.png`, `k/0248.png`, `k/0428.png`, `k/0462.png`, `kontrol.png` AÇIP bakıldı: künye tam, çakışma 0, güvenli alan içinde.

## Neden yeniden
- 2. tur: `now` etiketi nabız halkasına değiyordu (etiket y +18) ve parıltı `broken` sözcüğünün üstüne düşüyordu (kartın dışına, x 745'e taşındı). Acik yeniden koşuldu.

## Açık
- Sağ sütunda telefonun altı boş (x 1000–1860, y 700–1000); BRIEF yalnız telefon istiyor.


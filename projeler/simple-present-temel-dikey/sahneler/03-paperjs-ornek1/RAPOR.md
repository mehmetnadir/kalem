# Sahne 03 — Örnek 1 (DİKEY 9:16, Paper.js) · simple-present-temel-dikey

Tema: acik + koyu (ikisi de koşuldu; `video-acik.mp4`, `video-koyu.mp4`).

| Ölçüt | Sonuç |
|---|---|
| Kare | 379 (ffprobe: 1080×1920 yuv420p 30 fps, iki tema) |
| Olay | 21 (`olaylar.json`, son olay kare 355) |
| Altyazı | `altyaziMetin` + `altyaziCiz` (kunye.js, yerel çözüm YOK) |

Yerleşim (px): kart 372–618 (Fredoka 72, 2 satır, sözcük zamanlı) · TR Caveat 64 y 704 · doğa kanunu kutusu sağda ·
güneş 430 px (y 760–1190) + ok/`east` Caveat 96 · ufuk y 1196 · formül A `it + rise-s` y 1294, B `V + s` y 1390
(Fredoka 96) · altyazı 1400–1536 · platform boş.
Zamanlama (yerel kare): kart kutusu 18 · cümle 53 · ufuk 53 · güneş 58 · ok east 96 · TR 132 · kutu 188 · rises daire 284 ·
s daire 336 · formül A 341 · B 355 (365'te biter, 366 sonrası durgun).

Kare kapısı: `k/acik-0107,0272,0347,0366.png`, `k/0107..0366.png` (koyu), `kontrol.png` (koyu, 6 kare),
telefon kontak `k/telefon-01..03.png` (acik, 360×640). Hepsi Read ile açıldı: HUD okunuyor, içerik bandı dolu,
yazı ≥ 64, güneş ≥ 420, altyazı bandı dolu, platform bandı boş, çakışma 0.
Editör kapısı: `onizle.html?surum=dikey-tam&tema=acik&t=20` → slot no 2, `t=35` → slot no 3, ikisinde
`hazir:true, goster:true`. Konsolda 3×404 var: başka ajanın henüz yazmadığı sahne 01/06 sayfaları (sayfa.html 404).
Sahne sayfası tek başına (`sayfa.html?canli=1&tema=acik`) konsol boş.

Yeniden koşu nedenleri: (1) ilk koşuda kart tek satıra sığdı, TR kartın altına yapışıktı, formül satırları sıkıştı →
kart 2 satıra zorlandı, satır aralığı ve boşluk açıldı, `rise-s` bitişik. (2) TR–kart arası 20 px daha açıldı,
etiket kutusu kart çizgisine değiyordu.
Açık sorular: yok.
